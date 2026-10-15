"""Independent re-verification of the competitor tracker.

Recomputes the key numbers straight from the raw source files with its own parsing (not the builder's code) and
compares them with BOTH outputs: the recalculated workbook and the dashboard payload. Writes
data/verification_report.json, which the dashboard shows in its verification section.

Usage: python3 verify_tracker.py RECALCULATED_WORKBOOK.xlsx competitor_dashboard.html
"""
import csv, glob, json, os, re, statistics, sys
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "data")
WB, HTML = sys.argv[1], sys.argv[2]

def rd(path):
    return list(csv.DictReader(open(path, encoding="utf-8-sig")))
def fnum(v):
    try:
        x = float(v)
        return x if x > 0 else None
    except (TypeError, ValueError):
        return None
def close(a, b, tol=0.006):
    if a is None or b is None:
        return a is None and b is None
    return abs(float(a) - float(b)) <= tol * max(1.0, abs(float(b)))

html = open(HTML).read()
i = html.index("const D = ") + len("const D = ")
P = json.loads(html[i:html.index("\nconst IMG")].rstrip().rstrip(";"))
results = []
def check(name, compared, total, bad, examples, note=""):
    results.append({"name": name, "compared": compared, "checked": total, "mismatches": bad, "status": "Pass" if bad == 0 else "Fail",
                    "examples": examples[:5], "note": note})

# 1. Keepa BFCM 2025 per competitor ASIN, recomputed from the raw daily files (US and CA separately)
def keepa_files(prefix_ca):
    if prefix_ca:
        fs = [os.path.join(D, "keepa", "keepa_history_ca.csv")]
    else:
        fs = [f for f in glob.glob(os.path.join(D, "keepa", "keepa_history_*.csv"))
              if not re.search(r"_(coverage|provenance)\.csv$", f) and "/keepa_history_ca" not in f and "/keepa_history_ours" not in f and "_p2_batch" not in f]
    rows = {}
    for f in sorted(fs):
        for r in rd(f):
            rows.setdefault(r["asin"], {})[r["date"]] = r
    return rows
def summarise(days):
    pre = [r for d, r in days.items() if "2025-11-01" <= d <= "2025-11-19"]
    bf = [r for d, r in days.items() if "2025-11-20" <= d <= "2025-12-01"]
    eff = lambda r: min([x for x in (fnum(r["buy_box_price"]), fnum(r["lightning_deal_price"]), fnum(r["prime_exclusive_price"])) if x] or [None]) if any(
        fnum(r[k]) for k in ("buy_box_price", "lightning_deal_price", "prime_exclusive_price")) else None
    ep, eb = [eff(r) for r in pre if eff(r)], [eff(r) for r in bf if eff(r)]
    rp, rb = [fnum(r["sales_rank"]) for r in pre if fnum(r["sales_rank"])], [fnum(r["sales_rank"]) for r in bf if fnum(r["sales_rank"])]
    return {"bf_pre": statistics.median(ep) if ep else None, "bf_low": min(eb) if eb else None,
            "bsr_pre": round(statistics.median(rp)) if rp else None, "bsr_bf": round(statistics.median(rb)) if rb else None}
for mkt in ("US", "CA"):
    raw = keepa_files(mkt == "CA")
    tot = bad = 0; ex = []
    for c in P["comps"]:
        if c["mkt"] != mkt or not c.get("bf_type") or c["child"] not in raw:
            continue
        s = summarise(raw[c["child"]])
        tot += 1
        for k in ("bf_pre", "bf_low", "bsr_pre", "bsr_bf"):
            if not close(c.get(k), s[k]):
                bad += 1; ex.append(f"{c['child']} {k}: dashboard {c.get(k)} vs raw {s[k]}"); break
    check(f"Competitor BFCM 2025 price and rank ({mkt})", f"Dashboard vs recomputed from the raw Keepa daily file{'s' if mkt == 'US' else ''}", tot, bad, ex)

# 2. Workbook vs dashboard, every competitor row on every product tab
wb = openpyxl.load_workbook(WB, data_only=True)
COLS = {"Price ($)": "price", "List Price ($)": "lp", "BSR": "bsr", "Est weekly units": "wk", "Rating": "rating", "Reviews": "reviews",
        "Pre-event price ($)": "bf_pre", "BFCM 2025 low ($)": "bf_low", "BSR pre-event": "bsr_pre", "BSR BFCM wk": "bsr_bf"}
tab_of = {f"{p['mkt']} {p['short']}"[:31]: p["key"] for p in P["products"]}
by = {}
for c in P["comps"]:
    by.setdefault((c["key"], c["child"]), []).append(c)
tot = bad = 0; ex = []; gap_tot = gap_bad = 0; gap_ex = []
for ws in wb.worksheets:
    if ws.title not in tab_of:
        continue
    hdr = None
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        for cell in row:
            if cell.value == "Tracked child ASIN":
                hdr = cell.row; break
        if hdr:
            break
    if not hdr:
        continue
    names = {cell.value: cell.column for cell in ws[hdr] if cell.value}
    r = hdr + 1
    while ws.cell(row=r, column=names["Tracked child ASIN"]).value:
        ch = ws.cell(row=r, column=names["Tracked child ASIN"]).value
        cands = by.get((tab_of[ws.title], ch)) or []
        tot += 1
        if not cands:
            bad += 1; ex.append(f"{ws.title} {ch}: not in dashboard")
        else:
            ok = False
            for c in cands:
                if all(close(ws.cell(row=r, column=names[h]).value if isinstance(ws.cell(row=r, column=names[h]).value, (int, float)) else None, c.get(k))
                       for h, k in COLS.items() if h in names):
                    ok = True; break
            if not ok:
                bad += 1; ex.append(f"{ws.title} {ch}")
            g = ws.cell(row=r, column=names["Their price vs ours"]).value if "Their price vs ours" in names else None
            c0 = cands[0]
            if isinstance(g, (int, float)) and c0.get("gap") is not None:
                gap_tot += 1
                if not close(g, c0["gap"], 0.0005):
                    gap_bad += 1; gap_ex.append(f"{ws.title} {ch}: workbook {g:.4f} vs dashboard {c0['gap']:.4f}")
        r += 1
check("Workbook vs dashboard, competitor rows", "Price, List Price, rank, weekly units, rating, reviews and BFCM 2025 columns on every product tab", tot, bad, ex)
check("Price vs ours", "Workbook formula vs dashboard (their price ÷ our same-size price − 1)", gap_tot, gap_bad, gap_ex)

# 3. Our live prices vs the Xray exports
xr = {}
for f, m in ((os.path.join(D, "xray", "helium10_xray_2026-10-13.csv"), "US"), (os.path.join(D, "xray", "helium10_xray_ca_2026-10-14.csv"), "CA")):
    for r in rd(f):
        pk = next(k for k in r if k.startswith("Price"))
        if fnum(r.get(pk)):
            xr[(m, r["ASIN"])] = fnum(r[pk])
tot = bad = 0; ex = []
for p in P["products"]:
    for v in p["vars"]:
        if v["live"] and "Xray" in (v.get("src") or "") and (p["mkt"], v["asin"]) in xr:
            tot += 1
            if not close(v["price"], xr[(p["mkt"], v["asin"])], 0.0001):
                bad += 1; ex.append(f"{p['mkt']} {v['asin']}: {v['price']} vs Xray {xr[(p['mkt'], v['asin'])]}")
check("Our live variation prices", "Dashboard vs the Helium 10 Xray exports (US Oct 13, CA Oct 14)", tot, bad, ex)

# 4. Account-level BFCM 2025 lift from the raw SellerBoard files
for m in ("US", "CA"):
    pre = sum(float(r["sales"] or 0) for r in rd(os.path.join(D, "sellerboard", f"{m}_pre.csv")))
    bf = sum(float(r["sales"] or 0) for r in rd(os.path.join(D, "sellerboard", f"{m}_bfcm.csv")))
    lift = (bf / 12) / (pre / 30)
    dl = P["summary"][m]["accountLift"]
    check(f"Account BFCM 2025 sales lift ({m})", "Dashboard vs raw SellerBoard files (BFCM week ÷ 30 days before, per day)", 1, 0 if close(dl, lift, 0.0001) else 1,
          [] if close(dl, lift, 0.0001) else [f"dashboard {dl} vs raw {lift}"], f"{lift:.2f}x")

# 5. Our 2025 deal units per product from the raw deals file
raw_units = {}
for r in rd(os.path.join(D, "deals", "our_deals_bfcm2025_v2.csv")):
    if r["status"] == "ran":
        sid = re.search(r"source_id=([0-9a-f]+)", r["notes"] or "")
        k = (r["marketplace"], sid.group(1) if sid else r["deal_start"])
        raw_units[k] = raw_units.get(k, 0) + int(float(r["units_sold"] or 0))
txt_units = sorted(int(u.replace(",", "")) for p in P["products"] for u in re.findall(r"([\d,]+) units\)", p.get("deals") or "") if p.get("deals"))
ran = sorted(u for u in raw_units.values() if u)
miss = [u for u in txt_units if u not in ran]
check("Our BFCM 2025 deal units", "Units in each product's deal line vs the raw deals file", len(txt_units), len(miss), [f"{u} units not found in raw file" for u in miss])

# 6. Integrity: no zero or negative prices or ranks, photos present, plan mapped, assumption arithmetic
neg = [f"{c['child']} {k}={c[k]}" for c in P["comps"] for k in ("price", "lp", "bsr", "bf_pre", "bf_low") if isinstance(c.get(k), (int, float)) and c[k] <= 0]
check("No zero or negative values", "Competitor price, List Price, rank, BFCM prices (blank means unknown)", len(P["comps"]), len(neg), neg)
imgjs = open(os.path.join(os.path.dirname(os.path.abspath(HTML)), "images.js")).read()
keys = {c["img"] for c in P["comps"] if c.get("img")} | {v["img"] for p in P["products"] for v in p["vars"] if v.get("img")}
missing = [k for k in keys if f'"{k}":' not in imgjs]
check("Photos", "Every photo the dashboard points to is shipped in images.js", len(keys), len(missing), missing)
xm = [(p["mkt"], v["asin"], v["img"]) for p in P["products"] for v in p["vars"] if v.get("img") and v["img"][:2] != p["mkt"]] + \
     [(c["mkt"], c["child"], c["img"]) for c in P["comps"] if c.get("img") and re.match(r"(US|CA)_", c["img"]) and c["img"][:2] != c["mkt"]]
xbad = [f"{m} {a} uses {k}" for m, a, k in xm if k[3:] != a]
check("Photos from the other marketplace", "Each one is the same ASIN as the item it illustrates (never another ASIN)", len(xm), len(xbad), xbad)
plan = rd(os.path.join(D, "deals", "our_deals_bfcm2026_plan.csv"))
unm = [r["product_name"] for r in plan if r["pid"] and not any(p["pid"] == int(r["pid"]) and p["mkt"] == r["marketplace"] and p.get("plan26") for p in P["products"])]
check("BFCM 2026 plan mapped", "Every planned deal for a tracked product shows on that product", sum(1 for r in plan if r["pid"]), len(unm), unm,
      f"{sum(1 for r in plan if not r['pid'])} planned deal(s) for a product not tracked here (Hanging Closet Organizer)")
arith = [p["key"] for p in P["products"] if p.get("da") and p["da"].get("ref") and not close(p["da"]["deal"], round(p["da"]["ref"] * (1 - p["da"]["depth"]), 2), 0.0001)]
check("Assumed 2026 deal price arithmetic", "Deal = reference × (1 − discount)", sum(1 for p in P["products"] if p.get("da") and p["da"].get("ref")), len(arith), arith)

rep = {"generated": "2026-10-15", "checks": results, "passed": sum(1 for r in results if r["status"] == "Pass"), "total": len(results)}
json.dump(rep, open(os.path.join(D, "verification_report.json"), "w"), indent=1)
for r in results:
    print(f"{r['status']:4}  {r['name']}: {r['checked']} checked, {r['mismatches']} mismatches {('· ' + r['note']) if r['note'] else ''}{('  e.g. ' + '; '.join(r['examples'][:2])) if r['examples'] else ''}")
print(f"{rep['passed']}/{rep['total']} checks passed")
