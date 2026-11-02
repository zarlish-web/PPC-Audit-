"""Year-over-year, same 14 days (Oct 19 - Nov 1, 2025 vs 2026), product by product and ad type by ad type.
Splits the change in ad spend into: products sold both years (like-for-like), new products, products no longer advertised,
and within like-for-like, Sponsored Products vs the brand / video / display campaigns. Writes yoy_results.json."""
import json, glob, os, csv
HERE = os.path.dirname(os.path.abspath(__file__)); TR = os.path.join(HERE, "..", "competitor-tracker", "data")
TOOLRES = "/root/.claude/projects/-home-user-PPC-Audit-/51b9bd0e-5fdd-5e9c-87d4-612ed5188e17/tool-results/"
FX = 1.4036
ACCT = {"2025": {"US": dict(sales=375214.90, sp=50133.18, sb=2069.42, sbv=2412.80, sd=115.38, units=7603, sessions=117610, clicks=20349),
                 "CA": dict(sales=92110.54, sp=10870.81, sb=130.49, sbv=26.81, sd=0.0, units=2512, sessions=51229, clicks=8925)},
        "2026": {"US": dict(sales=255176.33, sp=42055.50, sb=3776.07, sbv=5804.45, sd=648.42, units=5208, sessions=77732, clicks=23537),
                 "CA": dict(sales=49548.47, sp=6852.81, sb=112.02, sbv=14.00, sd=0.92, units=1050, sessions=22310, clicks=6582)}}
skus = {}
for f in glob.glob(f"{TR}/skus/*.json"):
    d = json.load(open(f))
    if "product_id" in d: skus[(int(d["product_id"]), d["marketplace"])] = d
mv = [x for x in skus[(37, "US")]["skus"] if str(x.get("sku", "")).upper().startswith("SATIN-4PC-TWIN")]
skus[(37, "US")]["skus"] = [x for x in skus[(37, "US")]["skus"] if x not in mv]; skus[(31, "US")]["skus"] += mv
asin2pid = {}; names = {}
for (pid, m), d in skus.items():
    names[pid] = ((d.get("profile") or {}).get("brand") or "") + " " + ((d.get("profile") or {}).get("name") or "")
    for x in d["skus"]:
        if x.get("asin"): asin2pid[(m, x["asin"])] = pid
        if x.get("asin"): asin2pid.setdefault(("ANY", x["asin"]), pid)
NAME_MAP = {"B0F2G983W3": 39, "B0F55Y1P53": 32, "B0F7LX9RP3": 45, "B0F7LY4RD6": 45, "B0F7LY3994": 45, "B0FTSWF3M7": 45,
            "B0CQ3GXLCJ": 30, "B0D9HRYKBW": 48, "B0CRF7S2TH": 31, "B0CRVZ1TTS": 37}
for a_, p_ in NAME_MAP.items():
    asin2pid.setdefault(("ANY", a_), p_)
NAME_RULES = [("BreezeWeave", 45), ("Hanging Closet", 52), ("Boho Throw Blanket", 41), ("Bamboo Sheets Queen Size | 6 Pc", 30)]
names.setdefault(52, "Decolure Hanging Closet Organizer"); names.setdefault(41, "Sleephoria Boho Blanket")
def load(start_tag, end_tag, min_ts):
    rows = {}
    for f in sorted(glob.glob(TOOLRES + "mcp-Sellerborad-dashboard_table-*.txt")):
        if int(f.rsplit("-", 1)[1][:-4]) < min_ts: continue
        t = open(f).read(); j = json.loads(t[t.index("{"):]); rp = json.dumps(j.get("resolvedPeriods"))
        if start_tag not in rp or end_tag not in rp: continue
        for r in j["result"]:
            i = r["Info"]; m = "CA" if (i.get("Marketplace") or "").lower() == "amazon.ca" else "US"
            rows[(m, i["Id"])] = i
    return rows
Y = {"2025": load("2025-10-19", "2025-11-01", 1793619400000), "2026": load("2026-10-19", "2026-11-01", 1793616548409)}
out = {"window": "Oct 19 - Nov 1 (14 days), 2025 vs 2026", "fx": FX, "markets": {}}
for m in ("US", "CA"):
    fx = FX if m == "CA" else 1
    prod = {}
    unm = {"2025": [], "2026": []}
    for y, rows in Y.items():
        for (mm, _), i in rows.items():
            if mm != m: continue
            pid = asin2pid.get((m, i["ASIN"])) or asin2pid.get(("ANY", i["ASIN"]))
            if pid is None:
                nm_ = i.get("Name") or i.get("Title") or ""
                pid = next((p_ for k_, p_ in NAME_RULES if k_.lower() in nm_.lower()), None)
            key = pid if pid is not None else "other"
            if pid is None: unm[y].append((i.get("Name") or i.get("Title") or i["ASIN"])[:60])
            p = prod.setdefault(key, {y_: dict(sales=0.0, units=0.0, sp=0.0, sb=0.0, sbv=0.0, sd=0.0, ppc=0.0) for y_ in ("2025", "2026")})
            a = p[y]; a["ppc"] += (i.get("SalesPPC") or 0) * fx
            a["sales"] += i["Sales"] * fx; a["units"] += i["Units"]; a["sp"] += -i["SponsoredADS"] * fx; a["sb"] += -i["HSA"] * fx
            a["sbv"] += -i["VideoAds"] * fx; a["sd"] += -i["SponsoredDisplay"] * fx
    # rows not pulled (long tail) = account total - pulled
    for y in ("2025", "2026"):
        tail = prod.setdefault("tail", {y_: dict(sales=0.0, units=0.0, sp=0.0, sb=0.0, sbv=0.0, sd=0.0, ppc=0.0) for y_ in ("2025", "2026")})
        for k in ("sales", "units", "sp", "sb", "sbv", "sd"):
            pulled = sum(v[y][k] for kk, v in prod.items() if kk != "tail")
            tail[y][k] = ACCT[y][m][k] * (fx if k not in ("units",) else 1) - pulled
    rows_out = []
    for key, p in prod.items():
        a, b = p["2025"], p["2026"]
        adv25 = a["sp"] + a["sb"] + a["sbv"] + a["sd"]; adv26 = b["sp"] + b["sb"] + b["sbv"] + b["sd"]
        if key == "tail": cls = "Long tail (rows not pulled)"
        elif key == "other": cls = "Not in today's catalog"
        elif b["sales"] > 0 and a["sales"] < 0.05 * b["sales"]: cls = "New (not selling here last year)"
        elif a["sales"] > 0 and b["sales"] < 0.05 * a["sales"]: cls = "Gone / not sold now"
        else: cls = "Sold both years"
        rows_out.append({"market": m, "pid": key, "product": names.get(key, "Rows not pulled (long tail)" if key == "tail" else "Older listings not in today's catalog"),
                         "class": cls, "sales25": round(a["sales"], 2), "sales26": round(b["sales"], 2), "units25": round(a["units"]), "units26": round(b["units"]),
                         "sp25": round(a["sp"], 2), "sp26": round(b["sp"], 2), "nonsp25": round(a["sb"] + a["sbv"] + a["sd"], 2), "nonsp26": round(b["sb"] + b["sbv"] + b["sd"], 2),
                         "sbv25": round(a["sbv"], 2), "sbv26": round(b["sbv"], 2), "ppc25": round(a.get("ppc", 0), 2), "ppc26": round(b.get("ppc", 0), 2), "adv25": round(adv25, 2), "adv26": round(adv26, 2)})
    rows_out.sort(key=lambda r: -(r["adv26"] + r["adv25"]))
    out["markets"][m] = {"rows": rows_out, "unmapped_examples": {y: sorted(set(v))[:12] for y, v in unm.items()}}
json.dump(out, open(os.path.join(HERE, "yoy_results.json"), "w"), indent=1)
for m in ("US", "CA"):
    R = out["markets"][m]["rows"]
    print(m)
    for r in R: print(f"  {r['class'][:22]:22s} {r['product'][:34]:34s} sales {r['sales25']:9.0f} -> {r['sales26']:9.0f} | SP {r['sp25']:7.0f} -> {r['sp26']:7.0f} | nonSP {r['nonsp25']:6.0f} -> {r['nonsp26']:6.0f}")
    print("  unmapped", out["markets"][m]["unmapped_examples"])

# ---------------------------------------------------------------- decomposition per market
for m in ("US", "CA"):
    R = out["markets"][m]["rows"]
    g = lambda cls, k: sum(r[k] for r in R if r["class"] == cls)
    LFL = "Sold both years"; NEW = "New (not selling here last year)"
    old = [c for c in {r["class"] for r in R} if c not in (LFL, NEW)]
    adv25 = sum(r["adv25"] for r in R); adv26 = sum(r["adv26"] for r in R)
    dec = {"adv25": adv25, "adv26": adv26,
           "lfl_sp": g(LFL, "sp26") - g(LFL, "sp25"), "lfl_nonsp": g(LFL, "nonsp26") - g(LFL, "nonsp25"),
           "new": g(NEW, "adv26") - g(NEW, "adv25"), "old_and_tail": sum(g(c, "adv26") - g(c, "adv25") for c in old),
           "lfl_sales25": g(LFL, "sales25"), "lfl_sales26": g(LFL, "sales26"), "new_sales26": g(NEW, "sales26"),
           "lfl_adv25": g(LFL, "adv25"), "lfl_adv26": g(LFL, "adv26"), "lfl_sp25": g(LFL, "sp25"), "lfl_sp26": g(LFL, "sp26"),
           "lfl_ppc25": g(LFL, "ppc25"), "lfl_ppc26": g(LFL, "ppc26"), "sales25": sum(r["sales25"] for r in R), "sales26": sum(r["sales26"] for r in R)}
    a25, a26 = ACCT["2025"][m], ACCT["2026"][m]
    dec["cpc25"] = a25["sp"] / a25["clicks"]; dec["cpc26"] = a26["sp"] / a26["clicks"]
    dec["cvr25"] = a25["units"] / a25["sessions"]; dec["cvr26"] = a26["units"] / a26["sessions"]
    dec["sessions25"] = a25["sessions"]; dec["sessions26"] = a26["sessions"]
    out["markets"][m]["decomp"] = dec
    print(m, {k: (round(v, 4) if abs(v) < 5 else round(v)) for k, v in dec.items()})

# ---------------------------------------------------------------- BFCM 2025 actual vs 2026 plan, product by product
rows_sb = {}
for m in ("US", "CA"):
    for w in ("pre", "bfcm"):
        for r in csv.DictReader(open(f"{TR}/sellerboard/{m}_{w}.csv", encoding="utf-8-sig")):
            rows_sb.setdefault((m, r["parent_asin"]), {}).setdefault(w, []).append(r)
child_pid = {}
for (pid, m), d in skus.items():
    for x in d["skus"]:
        if x.get("asin"): child_pid.setdefault(x["asin"], set()).add(pid)
CATP = {}
for mk, fn in (("US", "catalog_com.json"), ("CA", "catalog_ca.json")):
    CATP[mk] = {it["asin"]: it.get("parentAsin") for it in json.load(open(f"{TR}/catalog/{fn}")).get("items", []) if it.get("asin")}
par_pid = {}
for mk in CATP:
    for a_, pa_ in CATP[mk].items():
        if pa_ and a_ in child_pid: par_pid.setdefault(pa_, set()).update(child_pid[a_])
OWNER = {}
for (m, k) in rows_sb:
    if len(child_pid.get(k, ())) == 1: OWNER[(m, k)] = next(iter(child_pid[k]))
    elif len(par_pid.get(k, ())) == 1: OWNER[(m, k)] = next(iter(par_pid[k]))
    elif k in NAME_MAP: OWNER[(m, k)] = NAME_MAP[k]
for (pid, m), d in skus.items():
    cnt = {}
    for x in d["skus"]:
        pa_ = CATP[m].get(x.get("asin"))
        if pa_: cnt[pa_] = cnt.get(pa_, 0) + 1
    if cnt:
        pa = max(cnt, key=cnt.get)
        if (m, pa) in rows_sb: OWNER[(m, pa)] = pid
V = json.load(open(os.path.join(HERE, "verify_results.json")))
bf = []
for m in ("US", "CA"):
    fx = FX if m == "CA" else 1
    plan = {p["pid"]: p for p in V["products"] if p["mkt"] == m}
    agg = {}
    for (mm, k), d in rows_sb.items():
        if mm != m: continue
        pid = OWNER.get((mm, k), "other")
        a = agg.setdefault(pid, {"sales": 0.0, "adv": 0.0, "sp": 0.0, "units": 0.0, "sessions": 0.0, "units_ppc": 0.0,
                                 "pre_sales": 0.0, "pre_adv": 0.0, "pre_units": 0.0, "pre_sessions": 0.0})
        for r_ in d.get("bfcm", []):
            a["sales"] += float(r_["sales"] or 0) * fx; a["adv"] += -float(r_["advertising"] or 0) * fx; a["sp"] += -float(r_["sponsored_ads"] or 0) * fx
            a["units"] += float(r_["units"] or 0); a["sessions"] += float(r_["sessions"] or 0); a["units_ppc"] += float(r_["units_ppc"] or 0) + float(r_["units_sd"] or 0)
        for r_ in d.get("pre", []):
            a["pre_sales"] += float(r_["sales"] or 0) * fx; a["pre_adv"] += -float(r_["advertising"] or 0) * fx
            a["pre_units"] += float(r_["units"] or 0); a["pre_sessions"] += float(r_["sessions"] or 0)
    for pid in sorted(set(agg) | set(plan), key=lambda x: str(x)):
        a = agg.get(pid, {"sales": 0.0, "adv": 0.0, "sp": 0.0, "units": 0.0, "sessions": 0.0, "units_ppc": 0.0, "pre_sales": 0.0, "pre_adv": 0.0, "pre_units": 0.0, "pre_sessions": 0.0}); p = plan.get(pid)
        if a["adv"] < 1 and a["sales"] < 1 and not p: continue
        bf.append({"market": m, "pid": pid, "product": p["name"] if p else names.get(pid, "Other / older listings"),
                   "in_plan": bool(p), "sales25": round(a["sales"], 2), "adv25": round(a["adv"], 2), "sp25": round(a["sp"], 2),
                   "units25": round(a["units"]), "sessions25": round(a["sessions"]), "units_ads25": round(a["units_ppc"]),
                   "pre_sales25": round(a["pre_sales"], 2), "pre_adv25": round(a["pre_adv"], 2), "pre_units25": round(a["pre_units"]), "pre_sessions25": round(a["pre_sessions"]),
                   "plan_sales26": round(p["sales"], 2) if p else 0.0, "plan_budget26": round(p["budget"], 2) if p else 0.0,
                   "class": ("New since BFCM 2025" if p and a["sales"] < 0.05 * max(p["sales"], 1) else ("In both" if p else "Not in the 2026 plan"))})
out["bfcm"] = bf
for m in ("US", "CA"):
    B = [r for r in bf if r["market"] == m]
    for cls in ("In both", "New since BFCM 2025", "Not in the 2026 plan"):
        S = [r for r in B if r["class"] == cls]
        print(m, cls, "2025 spend", round(sum(r["adv25"] for r in S)), "2026 plan", round(sum(r["plan_budget26"] for r in S)), "2025 sales", round(sum(r["sales25"] for r in S)), "2026 plan sales", round(sum(r["plan_sales26"] for r in S)), [r["product"] for r in S][:12])
json.dump(out, open(os.path.join(HERE, "yoy_results.json"), "w"), indent=1, default=str)
