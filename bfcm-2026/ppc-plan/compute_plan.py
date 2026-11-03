"""BFCM 2026 PPC plan numbers: demand (from the tracker), deal-price break-even (Oct 27 deal sheet), current PPC (30 days),
BFCM 2025 day shape. Writes plan_numbers.json. Usage: python3 compute_plan.py ../competitor-tracker/competitor_dashboard.html"""
import csv, json, os, sys, statistics
HERE = os.path.dirname(os.path.abspath(__file__)); TR = os.path.join(HERE, "..", "competitor-tracker")
h = open(sys.argv[1]).read(); i = h.index("const D = ") + 10
D = json.loads(h[i:h.index("\nconst IMG")].rstrip().rstrip(";"))
INP = json.load(open(os.path.join(HERE, "inputs_2026-11-02.json")))
_YO = json.load(open(os.path.join(HERE, "..", "verification", "yoy_results.json")))
YO14 = {(r["market"], r["pid"]): r for mk in _YO["markets"] for r in _YO["markets"][mk]["rows"]}     # Oct 19 - Nov 1, 2025 vs 2026
YOBF = {(r["market"], r["pid"]): r for r in _YO["bfcm"]}                                           # BFCM 2025 per product
DEAL_PERF_FEE = 0.01           # Amazon deal fee, share of deal sales (corrected Nov 2: 1%)
DEAL_FLAT_FEE = 70.0           # flat fee per deal DAY (confirmed Nov 3: $70 x each day the deal runs; Best Deal 12 days, Lightning Deal 1)
CEIL_SHARE = 0.80              # TACoS ceiling = 80% of the break-even TACoS (keeps 20% of the pre-ad margin)
CA_COGS_FX = 1.40              # deal sheet CA COGS are the US$ figures next to C$ prices; converted to C$ (Nov 2025 rate 1.40)
sheet = {}
for r in csv.DictReader(open(os.path.join(TR, "data/deals/bfcm2026_deal_sheet_2026-10-27.csv"))):
    f = lambda k: float(r[k]) if r[k] not in ("", "None") else None
    sheet[(r["marketplace"], r["asin"])] = {"deal": f("deal_price"), "cur": f("current_price"),
                                            "cogs": (f("cogs") * CA_COGS_FX if r["marketplace"] == "CA" and f("cogs") is not None else f("cogs")), "fba": f("fba_fee"),
                                            "ref": f("referral_pct"), "type": r["deal_type"], "start": r["start"], "end": r["end"], "name": r["deal"]}
KEEP = {"DC B4", "DC B6", "DC S4", "DC S6", "SSS4", "DC Satin Fitted", "DC Silk Pillowcase", "CL Pillowcases", "SL Cooling 4pc", "SL Cooling Fitted",
        "SL Cooling Comforter", "SL Cooling Pillowcase", "SL B6", "SL Quilt Set", "DC Linen Curtains", "DC Chair Cover", "DC Bamboo Fitted",
        "DC Cooling 4pc", "CL Cooling Sheets"}
out = []
for p in D["products"]:
    if p["short"] not in KEEP or not p.get("stock26"):
        continue
    m = p["mkt"]; st = p["stock26"]; lift = st["lift"]
    vel = sum(r["vel"] for r in st["rows"]); u28 = p.get("u28") or 0
    lo_prev, hi_prev = u28 / 28 * lift * 12, vel * lift * 12      # the Oct 28 demand read (28-day pace / account velocity, both incl. deal days)
    # Demand from current, event-free data (Nov 3): A = last-14-day pace (Oct 19 - Nov 1) x own BFCM 2025 lift x 12 days;
    # B = this product's BFCM 2025 units x (units Oct 19 - Nov 1, 2026 / same 14 days 2025), used only where both years have real volume.
    y14 = YO14.get((m, p["pid"])); yb = YOBF.get((m, p["pid"]))
    A = (y14["units26"] / 14 * lift * 12) if (y14 and lift) else None
    B = (yb["units25"] * y14["units26"] / y14["units25"]) if (y14 and yb and (y14.get("units25") or 0) >= 100 and (yb.get("units25") or 0) >= 200) else None
    if A is None:
        lo, hi, dsrc = lo_prev, hi_prev, "Oct 28 demand read (no 14-day sales for this product)"
    elif B is None:
        lo = hi = A; dsrc = "last-14-day pace x own 2025 lift"
    else:
        lo, hi = min(A, B), max(A, B); dsrc = "last-14-day pace x lift / 2025 BFCM units x 2026 trend"
    rows = [(v, sheet.get((m, v["asin"]))) for v in p["vars"]]
    w = lambda v: (v.get("u28") or 0) + 0.01
    dealrows = [(v, s) for v, s in rows if s and s["deal"]]
    allrows = [(v, s) for v, s in rows if s and s["cur"] and s["cogs"] is not None and s["fba"] is not None]
    def wavg(pairs, fn):
        ws = [(w(v), fn(v, s)) for v, s in pairs if fn(v, s) is not None]
        return sum(a * b for a, b in ws) / sum(a for a, _ in ws) if ws else None
    deal = wavg(dealrows, lambda v, s: s["deal"]); cur = wavg(allrows, lambda v, s: s["cur"]) or p.get("price")
    da = p.get("da") or {}
    ld = da.get("type") == "Lightning Deal"
    if ld and A is not None:   # one deal day only: last year's (Best Deal) BFCM units would overstate it, so read A alone
        lo = hi = A; dsrc = "last-14-day pace x own 2025 lift (Lightning Deal only: 2025 Best Deal units not used)"
    # margin per unit before ads at the deal price (or today's price where there is no deal)
    def margin(v, s, price):
        if price is None or s["cogs"] is None or s["fba"] is None: return None
        return price - s["cogs"] - s["fba"] - (s["ref"] or 0.15) * price - (DEAL_PERF_FEE * price if s["deal"] else 0)
    if dealrows:
        m_deal = wavg(dealrows, lambda v, s: margin(v, s, s["deal"]))
    else:
        m_deal = None
    m_cur = wavg(allrows, lambda v, s: margin(v, s, s["cur"]) + (DEAL_PERF_FEE * s["cur"] if s["deal"] else 0))
    plan_units = (round(lo) + round(hi)) / 2   # same whole units the workbook shows, so break-even and sales use one figure
    # average selling price over the 12 days: deal price all 12 days for a Best Deal; 1 deal day + 11 regular for a Lightning Deal
    if deal and not ld: asp = deal
    elif deal and ld: asp = (deal + 11 * cur) / 12
    else: asp = cur
    sales = plan_units * asp
    # Ad break-even = what an extra unit earns at the deal price (after COGS, FBA, referral and the 1% deal fee).
    # The $70-a-day deal fee is a fixed cost of running the deal: it is paid whatever is spent on ads, so it does not
    # change what an extra ad-driven sale earns. It is checked separately at deal level (deal_fee vs deal_margin).
    deal_fee = DEAL_FLAT_FEE * (1 if ld else 12) if deal else 0.0
    if deal and not ld: be = m_deal / deal
    elif deal and ld: be = ((m_deal + 11 * m_cur) / 12) / asp

    else: be = m_cur / cur if (m_cur is not None and cur) else (p.get("be") if isinstance(p.get("be"), (int, float)) else None)
    sb = {r["label"][:4]: r for r in (p.get("sb") or [])}
    pre = next((r for r in (p.get("sb") or []) if "before" in r["label"].lower() or "Oct" in r["label"]), None)
    bf = next((r for r in (p.get("sb") or []) if "BFCM" in r["label"] or "Nov 20" in r["label"]), None)
    t_pre = pre["adcost"] / pre["sales"] if pre and pre.get("sales") and pre.get("adcost") is not None else None
    t_bf = bf["adcost"] / bf["sales"] if bf and bf.get("sales") and bf.get("adcost") is not None else None
    c30 = INP["ppc30"][m].get(str(p["pid"]))
    out.append({"mkt": m, "short": p["short"], "pid": p["pid"], "name": p["brand"] + " " + p["name"], "deal_type": da.get("type"), "deal_dates": da.get("dates"),
                "lift": lift, "lift_src": st.get("liftSrc"), "units_lo": lo, "units_hi": hi, "units_plan": plan_units, "demand_src": dsrc,
                "units_lo_prev": lo_prev, "units_hi_prev": hi_prev, "deal_fee": deal_fee,
                "deal_margin": (sales * be if (deal and be is not None) else None), "pace14": (y14["units26"] / 14 if y14 else None), "units25": sum(v.get("u25") or 0 for v in p["vars"]),
                "deal_price": deal, "cur_price": cur, "asp": asp, "sales_plan": sales, "margin_deal": m_deal, "margin_cur": m_cur, "be_tacos": be,
                "tacos25_pre": t_pre, "tacos25_bf": t_bf, "spend30": c30[0] if c30 else None, "adsales30": c30[1] if c30 else None,
                "tacos30": (c30[2] / 100 if c30 and c30[2] is not None else None), "ld": ld})
json.dump(out, open(os.path.join(HERE, "plan_numbers.json"), "w"), indent=1, default=str)
for r in sorted(out, key=lambda r: (r["mkt"] != "US", -(r["sales_plan"] or 0))):
    f = lambda x, d=1: "-" if x is None else (f"{x*100:.{d}f}%")
    print(f"{r['mkt']} {r['short']:20s} units {r['units_lo']:6.0f}-{r['units_hi']:6.0f} asp {r['asp'] or 0:6.2f} sales {r['sales_plan']:8.0f} BE {f(r['be_tacos'])} "
          f"tacos30 {f(r['tacos30'])} 25pre {f(r['tacos25_pre'])} 25bf {f(r['tacos25_bf'])} spend30/d {((r['spend30'] or 0)/30):6.0f} {r['deal_type'] or 'no deal'} {r['deal_dates'] or ''}")
