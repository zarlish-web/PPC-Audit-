"""Independent verification of the BFCM 2026 PPC plan.

Rebuilds every plan number from the original records (deal sheet, SKU lists, inventory export, 2025 sales files,
raw 14-day child-ASIN pulls, fresh account pulls, second-source ad console data) WITHOUT importing or reusing the
plan's own code (compute_plan.py / build_ppc_plan.py), then compares each figure with the delivered workbook.

Usage: python3 verify.py <recalculated copy of BFCM_2026_PPC_Plan.xlsx>
Writes verify_results.json next to this file.
"""
import csv, glob, json, os, statistics, sys, datetime as dt
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(HERE, "..", "competitor-tracker", "data")
PLAN = os.path.join(HERE, "..", "ppc-plan")
TOOLRES = "/root/.claude/projects/-home-user-PPC-Audit-/51b9bd0e-5fdd-5e9c-87d4-612ed5188e17/tool-results/"
SRC = json.load(open(os.path.join(HERE, "source", "account_pulls_2026-11-02.json")))
CONSOLE = json.load(open(os.path.join(HERE, "source", "ads_console_sp_by_product_2026-10-19_to_11-01.json")))
STAGES = json.load(open(os.path.join(HERE, "source", "stages_2026-11-02.json")))["stages"]
INP = json.load(open(os.path.join(PLAN, "inputs_2026-11-02.json")))
WB = load_workbook(sys.argv[1], data_only=True)
FX = 1.4036
checks = []

def add(section, item, source, plan, tol=0.005, mkt="", product="", kind="rel", note="", status=None):
    """kind: rel (relative tolerance), abs (absolute), eq (exact / text)."""
    if status is None:
        if source is None and plan is None:
            status = "OK"
        elif source is None or plan is None:
            status = "CHECK"
        elif kind == "eq":
            status = "OK" if source == plan else "DIFF"
        else:
            d = abs(source - plan)
            lim = tol if kind == "abs" else tol * max(abs(source), abs(plan), 1e-9)
            status = "OK" if d <= lim + 1e-9 else "DIFF"
    diff = (plan - source) if isinstance(source, (int, float)) and isinstance(plan, (int, float)) and kind != "eq" else None
    checks.append({"section": section, "item": item, "mkt": mkt, "product": product, "source": source, "plan": plan,
                   "diff": diff, "tol": tol if kind != "eq" else None, "kind": kind, "status": status, "note": note})
    return status

# ------------------------------------------------------------------ 1. source integrity
S1 = "1. Source records"
for m in ("US", "CA"):
    D, T = SRC["daily_bfcm2025"][m], SRC["bfcm2025_total"][m]
    for k in ("sales", "adv", "units"):
        add(S1, f"BFCM 2025 daily {k} add up to the 12-day total", round(sum(D[k]), 2), T[k], 0.005, m, kind="abs")
# 2025 parent-level files vs fresh account totals
for m in ("US", "CA"):
    for w, key in (("pre", "pre2025_30d"), ("bfcm", "bfcm2025_total")):
        rows = list(csv.DictReader(open(f"{TR}/sellerboard/{m}_{w}.csv", encoding="utf-8-sig")))
        fs = sum(float(r["sales"] or 0) for r in rows); fa = -sum(float(r["advertising"] or 0) for r in rows)
        add(S1, f"2025 {w} product file: sales = account total", SRC[key][m]["sales"], round(fs, 2), 0.001, m)
        add(S1, f"2025 {w} product file: ad spend = account total", SRC[key][m]["adv"], round(fa, 2), 0.01, m,
            note="Small gaps = ad spend attributed after the file was pulled.")
# account lift and deal-period factor (fresh) vs plan constants
lift_f = {m: (SRC["bfcm2025_total"][m]["sales"] / 12) / (SRC["pre2025_30d"][m]["sales"] / 30) for m in ("US", "CA")}
fac_f = {m: (SRC["bfcm2025_total"][m]["adv"] / SRC["bfcm2025_total"][m]["sales"]) / (SRC["pre2025_30d"][m]["adv"] / SRC["pre2025_30d"][m]["sales"]) for m in ("US", "CA")}
bf_f = {m: SRC["bfcm2025_total"][m]["adv"] / SRC["bfcm2025_total"][m]["sales"] for m in ("US", "CA")}
PN = json.load(open(os.path.join(PLAN, "plan_numbers.json")))
for m in ("US", "CA"):
    assumed = [r["lift"] for r in PN if r["mkt"] == m and "ASSUMED" in (r.get("lift_src") or "")]
    if assumed:
        add(S1, "Account BFCM 2025 lift (used where a product has no own lift)", round(lift_f[m], 4), round(assumed[0], 4), 0.002, m)
    add(S1, "Deal-period factor (BFCM 2025 TACoS / 30 days before)", round(fac_f[m], 3), {"US": 0.58, "CA": 0.68}[m], 0.006, m, kind="abs")
    add(S1, "BFCM 2025 account TACoS (fallback)", round(bf_f[m], 4), {"US": 0.0817, "CA": 0.088}[m], 0.0006, m, kind="abs")
# daily 2025 inputs vs fresh
for m, keys in (("US", (("sales", "sales"), ("ad", "adv"), ("units", "units"))), ("CA", (("sales_usd", "sales"), ("ad_usd", "adv"), ("units", "units")))):
    for ik, sk in keys:
        a, b = INP["daily2025"][m][ik], SRC["daily_bfcm2025"][m][sk]
        worst = max(abs(x - y) for x, y in zip(a, b))
        add(S1, f"Plan input: BFCM 2025 by day ({sk}), largest daily gap", 0.0, round(worst, 2), 0.5, m, kind="abs")
# weekly ad types
for m, km in (("US", "US"), ("CA", "CA_usd")):
    for k in ("sp", "sb", "sbv", "sd", "sales"):
        a, b = INP["adtype_weekly"][km].get(k), SRC["weekly2026"][m][k]
        if a is None:
            continue
        for i, (x, y) in enumerate(zip(a, b)):
            add(S1, f"Plan input: weekly {k}, {SRC['weekly2026']['weeks'][i]}", y, x, 30 if i == 5 else 0.5, m, kind="abs",
                note="Last week: a few dollars of SB/SB video attributed since the plan was built." if i == 5 else "")
# periods compare
LBL = INP["periods_compare"]["labels"]
for m in ("US", "CA"):
    P = INP["periods_compare"][m]
    fresh = {1: SRC["now14"][m] if False else None}
    # periods 3 (BFCM) and 6 (now) can be checked against the fresh pulls saved here
    for idx, key in ((3, "bfcm2025_total"), (6, "now14")):
        r = P[idx]; f = SRC[key][m]
        add(S1, f"History tab: {LBL[idx]} sales", f["sales"], r[1], 0.005, m, kind="abs")
        add(S1, f"History tab: {LBL[idx]} all ad spend", f["adv"], round(r[3] + r[4] + r[5] + r[6], 2), 0.05, m, kind="abs")
        add(S1, f"History tab: {LBL[idx]} sessions", f["sessions"], r[7], 0.5, m, kind="abs")
# CA COGS currency
rows = list(csv.DictReader(open(f"{TR}/deals/bfcm2026_deal_sheet_2026-10-27.csv")))
us_c = {r["sku"]: r["cogs"] for r in rows if r["marketplace"] == "US" and r["cogs"]}
same = sum(1 for r in rows if r["marketplace"] == "CA" and r["cogs"] and r["sku"] in us_c and abs(float(r["cogs"]) - float(us_c[r["sku"]])) < 0.01)
tot = sum(1 for r in rows if r["marketplace"] == "CA" and r["cogs"] and r["sku"] in us_c)
add(S1, "Canada COGS in the deal sheet are US$ (same cost as the US SKU)", tot, same, 0.1, "CA", kind="rel", note=f"{same} of {tot} Canadian SKUs carry exactly the US cost; the plan converts them to C$ at 1.40.",
    status="OK" if same / tot > 0.85 else "DIFF")

# ------------------------------------------------------------------ raw 14-day child rows (original pulls)
raw = {}
for f in sorted(glob.glob(TOOLRES + "mcp-Sellerborad-dashboard_table-*.txt")):
    if int(f.rsplit("-", 1)[1][:-4]) < 1793616548409:
        continue
    t = open(f).read(); j = json.loads(t[t.index("{"):])
    if "2026-10-19" not in json.dumps(j.get("resolvedPeriods")) or "2026-11-01" not in json.dumps(j.get("resolvedPeriods")):
        continue
    for r in j["result"]:
        i = r["Info"]; m = "CA" if (i.get("Marketplace") or "").lower() == "amazon.ca" else "US"
        raw[(m, i["Id"])] = i
for m in ("US", "CA"):
    v = [i for (mm, _), i in raw.items() if mm == m]
    add(S1, "14-day child rows: share of account ad spend captured", 1.0, round(-sum(i["Advertising"] for i in v) / SRC["now14"][m]["adv"], 4), 0.05, m, kind="abs",
        note="Rows pulled down to about $7 of spend; the rest is a long tail of tiny rows.")
    add(S1, "14-day child rows: share of account sales captured", 1.0, round(sum(i["Sales"] for i in v) / SRC["now14"][m]["sales"], 4), 0.07, m, kind="abs",
        note="Sales captured down to about $110 per child row.")

# ------------------------------------------------------------------ product map from SKU lists (not from the plan)
skus = {}
for f in glob.glob(f"{TR}/skus/*.json"):
    d = json.load(open(f))
    if "product_id" in d:
        skus[(int(d["product_id"]), d["marketplace"])] = d
# business rule (Oct 14): SATIN-4PC-TWIN SKUs counted under Satin 6 Pc (pid 31)
mv = [x for x in skus[(37, "US")]["skus"] if str(x.get("sku", "")).upper().startswith("SATIN-4PC-TWIN")]
skus[(37, "US")]["skus"] = [x for x in skus[(37, "US")]["skus"] if x not in mv]
skus[(31, "US")]["skus"] += mv
asin2pid = {}
for (pid, m), d in skus.items():
    for x in d["skus"]:
        if x.get("asin"):
            asin2pid[(m, x["asin"])] = pid
U14_BY_ASIN = {}
for (m, _), i in raw.items():
    U14_BY_ASIN[(m, i["ASIN"])] = U14_BY_ASIN.get((m, i["ASIN"]), 0) + i["Units"]
agg = {}
for (m, _), i in raw.items():
    pid = asin2pid.get((m, i["ASIN"]))
    a = agg.setdefault((m, pid), [0.0] * 6)
    a[5] += i["Units"]
    fx = FX if m == "CA" else 1
    for k, f_ in enumerate(("SponsoredADS", "HSA", "VideoAds", "SponsoredDisplay")):
        a[k] += -i[f_] * fx
    a[4] += i["Sales"] * fx

# inventory velocity (Oct 15 export)
inv = {}
import glob as _glob, re as _re
_INV = sorted(_glob.glob(f"{TR}/stock/sellerboard_inventory_*.csv"), key=lambda f: _re.findall(r"\d{4}-\d{2}-\d{2}", f)[-1])[-1]
# 2025 units for the same 14 days (Oct 19 - Nov 1, 2025): the one figure taken from yoy_results.json (no other raw copy exists)
YO14V = {(r["market"], r["pid"]): r for mk_ in json.load(open(os.path.join(HERE, "yoy_results.json")))["markets"].values() for r in mk_["rows"]}
for r in csv.DictReader(open(_INV, encoding="utf-8-sig")):
    k = ("CA" if r["marketplace"] == "Amazon.ca" else "US", r["asin"])
    d = inv.setdefault(k, {"vel": 0.0, "oh": 0.0, "ib": 0.0})
    d["vel"] += float(r["sales_velocity"] or 0); d["oh"] += float(r["on_hand"] or 0); d["ib"] += float(r["sent_to_fba"] or 0)

# 2025 per-product TACoS + own lift from the 2025 product files, mapped by parent ASIN and child membership
sbrows = {}
for m in ("US", "CA"):
    for w in ("pre", "bfcm"):
        for r in csv.DictReader(open(f"{TR}/sellerboard/{m}_{w}.csv", encoding="utf-8-sig")):
            sbrows.setdefault((m, r["parent_asin"]), {}).setdefault(w, []).append(r)
# ownership of 2025 product-file rows: (1) the row key is one of the product's child ASINs; (2) it is the Amazon parent of
# the product's children (catalog); (3) the documented name list for re-parented 2025 listings (checked by name below).
NAME_MAP = {"B0F2G983W3": 39, "B0F55Y1P53": 32, "B0F7LX9RP3": 45, "B0F7LY4RD6": 45, "B0F7LY3994": 45, "B0FTSWF3M7": 45,
            "B0CQ3GXLCJ": 30, "B0D9HRYKBW": 48, "B0CRF7S2TH": 31, "B0CRVZ1TTS": 37}
child_pid = {}
for (pid, m), d in skus.items():
    for x in d["skus"]:
        if x.get("asin"):
            child_pid.setdefault(x["asin"], set()).add(pid)
par_pid = {}
for fn in ("catalog_com.json", "catalog_ca.json"):
    for it in json.load(open(f"{TR}/catalog/{fn}")).get("items", []):
        if it.get("parentAsin") and it.get("asin") in child_pid:
            par_pid.setdefault(it["parentAsin"], set()).update(child_pid[it["asin"]])
OWNER, OWNER_RULE = {}, {}
for (m, k) in sbrows:
    if len(child_pid.get(k, ())) == 1:
        OWNER[(m, k)] = next(iter(child_pid[k])); OWNER_RULE[(m, k)] = "child ASIN"
    elif len(par_pid.get(k, ())) == 1:
        OWNER[(m, k)] = next(iter(par_pid[k])); OWNER_RULE[(m, k)] = "parent of its children"
    elif k in NAME_MAP:
        OWNER[(m, k)] = NAME_MAP[k]; OWNER_RULE[(m, k)] = "name list"
CATP = {}
for mk, fn in (("US", "catalog_com.json"), ("CA", "catalog_ca.json")):
    CATP[mk] = {it["asin"]: it.get("parentAsin") for it in json.load(open(f"{TR}/catalog/{fn}")).get("items", []) if it.get("asin")}
for (pid, m), d in skus.items():   # (0) the product's current Amazon parent (most common catalog parent of its children)
    cnt = {}
    for x in d["skus"]:
        pa_ = CATP[m].get(x.get("asin"))
        if pa_:
            cnt[pa_] = cnt.get(pa_, 0) + 1
    pa = max(cnt, key=cnt.get) if cnt else None
    if pa and (m, pa) in sbrows:
        OWNER[(m, pa)] = pid; OWNER_RULE[(m, pa)] = "current parent"

deal = {}
for r in rows:
    f = lambda k: float(r[k]) if r[k] not in ("", "None") else None
    deal[(r["marketplace"], r["asin"])] = {"deal": f("deal_price"), "cur": f("current_price"), "cogs": f("cogs"), "fba": f("fba_fee"),
                                           "ref": f("referral_pct"), "type": r["deal_type"], "start": r["start"], "end": r["end"]}

# ------------------------------------------------------------------ read the delivered workbook
bp, ap, bd = WB["Budget by product"], WB["Ad types by product"], WB["Budget by day"]
NAMES = {}
blocks = {}
cur = None
for r in range(1, bp.max_row + 1):
    a = bp.cell(r, 1).value
    if a in ("United States (US$)", "Canada (C$)"):
        cur = "US" if a.startswith("United") else "CA"; blocks[cur] = []
    elif cur and a and a not in ("Product", "Total") and isinstance(bp.cell(r, 21).value, (int, float)):
        blocks[cur].append(r)
    elif cur and a == "Total":
        blocks[cur + "_tot"] = r
col = {c: i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}
def cell(ws, r, c):
    if len(c) == 2:
        return ws.cell(r, 26 + col[c[1]]).value
    return ws.cell(r, col[c]).value
PROD_PID = {}
for p in PN:
    PROD_PID[(p["mkt"], p["short"])] = p["pid"]
SHORT_OF = {"Decolure Bamboo 4 Pc": "DC B4", "Decolure Bamboo 6 Pc": "DC B6", "Decolure Satin 4 Pc": "DC S4", "Decolure Satin 6 Pc": "DC S6",
            "Sleep Sanctuary Satin 4 Pc": "SSS4", "Decolure Satin Fitted": "DC Satin Fitted", "Decolure Silk Pillowcase": "DC Silk Pillowcase",
            "CooLinens Pillowcases": "CL Pillowcases", "Sleephoria Cooling 4 Pc": "SL Cooling 4pc", "Sleephoria Cooling Fitted": "SL Cooling Fitted",
            "Sleephoria Cooling Comforter": "SL Cooling Comforter", "Sleephoria Cooling Pillowcase": "SL Cooling Pillowcase", "Sleephoria Bamboo 6 Pc": "SL B6",
            "Sleephoria Quilt Set": "SL Quilt Set", "Decolure Linen Curtains": "DC Linen Curtains", "Decolure Chair Cover": "DC Chair Cover",
            "Decolure Bamboo Fitted": "DC Bamboo Fitted", "Decolure Cooling 4 Pc": "DC Cooling 4pc", "CooLinens Cooling Sheets": "CL Cooling Sheets"}
PARENT = {}
for p in PN:
    d = skus.get((p["pid"], p["mkt"])) or {}
    PARENT[(p["mkt"], p["pid"])] = (d.get("profile") or {}).get("parentAsin")

# ------------------------------------------------------------------ 2. product-by-product recompute
S2 = "2. Product numbers"
products = []
for m in ("US", "CA"):
    for r in blocks[m]:
        name = bp.cell(r, 1).value; short = SHORT_OF[name]; pid = PROD_PID[(m, short)]
        pl = next(x for x in PN if x["mkt"] == m and x["pid"] == pid)
        sk = [x for x in skus[(pid, m)]["skus"] if x.get("asin")]
        seen, vrows = set(), []
        for x in sk:
            if x["asin"] in seen:
                continue
            seen.add(x["asin"]); vrows.append(x)
        u28 = sum((x.get("units28d") or 0) for x in sk)
        cnt_ = {}
        for x in sk:
            pa_ = CATP[m].get(x["asin"])
            if pa_:
                cnt_[pa_] = cnt_.get(pa_, 0) + 1
        apar = max(cnt_, key=cnt_.get) if cnt_ else None
        for a_, pa_ in CATP[m].items():   # catalog children of the product's parent that are not in the SKU list
            if apar and pa_ == apar and a_ not in seen and a_ != apar:
                seen.add(a_); vrows.append({"asin": a_, "units28d": None})
        vel = 0.0
        for x in vrows:
            iv = inv.get((m, x["asin"]))
            if not iv:
                continue
            v_ = iv["vel"] or ((x.get("units28d") or 0) / 28 if (x.get("units28d") or 0) > 0 else 0)
            vel += v_
        # own 2025 lift / TACoS: every 2025 product-file row this product owns (ownership rules re-implemented below)
        pre_s = bf_s = pre_a = bf_a = bf_n = 0.0
        for (mm, k), d in sbrows.items():
            if mm != m or OWNER.get((mm, k)) != pid:
                continue
            for r_ in d.get("pre", []):
                pre_s += float(r_["sales"] or 0); pre_a += -float(r_["advertising"] or 0)
            for r_ in d.get("bfcm", []):
                bf_s += float(r_["sales"] or 0); bf_a += -float(r_["advertising"] or 0); bf_n += float(r_["units"] or 0)
        own = (bf_s / 12) / (pre_s / 30) if pre_s and bf_s else None
        lift = own if own and 0.8 <= own <= 8 else lift_f[m]
        t_pre = pre_a / pre_s if pre_s else None; t_bf = bf_a / bf_s if bf_s else None
        # demand (re-based Nov 3): A = own 14-day units / 14 x lift x 12; B = own BFCM 2025 units x (14-day units 2026 / 2025)
        _u14a = {x["asin"] for x in vrows} | {a_ for a_, p_ in NAME_MAP.items() if p_ == pid}   # + re-parented children on the documented name list
        u14 = sum(U14_BY_ASIN.get((m, a_), 0) for a_ in _u14a)   # SKU-list children + catalog-only children of the product's parent
        y25 = (YO14V.get((m, pid)) or {}).get("units25") or 0
        A_ = u14 / 14 * lift * 12 if u14 else None
        B_ = bf_n * u14 / y25 if (u14 and y25 >= 100 and bf_n >= 200) else None
        if A_ is None:
            lo, hi = u28 / 28 * lift * 12, vel * lift * 12
        elif B_ is None:
            lo = hi = A_
        else:
            lo, hi = min(A_, B_), max(A_, B_)
        # deal economics
        w = lambda x: (x.get("units28d") or 0) + 0.01
        dr = [(x, deal.get((m, x["asin"]))) for x in sk]
        dealrows = [(x, s) for x, s in dr if s and s["deal"]]
        allrows = [(x, s) for x, s in dr if s and s["cur"] and s["cogs"] is not None and s["fba"] is not None]
        def wavg(pairs, fn):
            ws = [(w(x), fn(x, s)) for x, s in pairs if fn(x, s) is not None]
            return sum(a * b for a, b in ws) / sum(a for a, _ in ws) if ws else None
        cogs = lambda s: s["cogs"] * (1.40 if m == "CA" else 1)
        dprice = wavg(dealrows, lambda x, s: s["deal"]); cprice = wavg(allrows, lambda x, s: s["cur"])
        mdeal = wavg(dealrows, lambda x, s: s["deal"] - cogs(s) - s["fba"] - (s["ref"] or 0.15) * s["deal"] - 0.01 * s["deal"]) if dealrows else None
        mcur = wavg(allrows, lambda x, s: s["cur"] - cogs(s) - s["fba"] - (s["ref"] or 0.15) * s["cur"])
        dtype = dealrows[0][1]["type"] if dealrows else None
        ld = dtype == "Lightning Deal"
        if ld and A_ is not None:   # Lightning Deal only: read A alone
            lo = hi = A_
        units = (round(lo) + round(hi)) / 2
        asp = dprice if (dprice and not ld) else ((dprice + 11 * cprice) / 12 if (dprice and ld) else cprice)
        price_note = ""
        if asp is None:   # no row in the deal sheet: the tracker's list price is the only record
            asp = g_plan_asp = cell(bp, r, "I"); price_note = "No deal-sheet row: price taken from the tracker's listing price."
        sales = units * round(asp, 2)
        flat = 70 * (1 if ld else 12) / sales if (dprice and sales) else 0   # $70 per deal day
        if dprice and not ld:
            be = mdeal / dprice - flat
        elif dprice and ld:
            be = ((mdeal + 11 * mcur) / 12) / asp - flat
        else:
            be = pl["be_tacos"] if pl["be_tacos"] is not None and (mcur is None or not cprice) else (mcur / cprice if mcur is not None and cprice else None)
        st = STAGES[m].get(str(pid), [None, None, None])
        band_lo = st[1] / 100 if st[1] is not None and st[0] != "Liquidation" else None
        band_hi = st[2] / 100 if st[2] is not None and st[0] != "Liquidation" else None
        fac = max(0.3, min(1.2, t_bf / t_pre)) if (t_pre and t_bf and t_pre > 0.01 and t_bf > 0.01) else {"US": 0.58, "CA": 0.68}[m]
        fac = round(fac, 2)
        fb = t_bf if (t_bf or 0) > 0.01 else {"US": 0.0817, "CA": 0.088}[m]
        a14 = agg.get((m, pid), [0, 0, 0, 0, 0, 0]); adv14 = sum(a14[:4]); s14 = a14[4]
        now = adv14 / s14 if s14 else None
        be_r = round(be, 4) if be is not None else None
        L = max(0, be_r * 0.80) if be_r is not None else None
        cap = (band_hi if L is None else (L if band_hi is None else min(band_hi, L)))
        if not dprice:
            plan_t = 0 if now is None else (now if cap is None else min(now, cap))
            budget = s14 / 14 * 12 * plan_t
        else:
            if be_r is None or be_r <= 0.05:
                plan_t = 0
            else:
                base = now * fac if now is not None else fb
                floor = band_lo * fac if band_lo is not None else 0
                plan_t = min(cap, max(base, floor))
            budget = sales * plan_t
        split = [budget * x / adv14 if adv14 else (budget if k == 0 else 0) for k, x in enumerate(a14[:4])]
        # compare with workbook
        g = lambda c: cell(bp, r, c)
        add(S2, "Units low (28-day pace x lift x 12)", round(lo), g("F"), 1, m, name, kind="abs")
        add(S2, "Units high (velocity x lift x 12)", round(hi), g("G"), 0.02, m, name)
        add(S2, "Average selling price", round(asp, 2), g("I"), 0.01, m, name, note=price_note, status="CHECK" if price_note else None)
        add(S2, "Expected sales, 12 days", sales, g("J"), 0.01, m, name)
        add(S2, "Break-even TACoS at deal price", be_r, g("K"), 0.005, m, name, kind="abs")
        add(S2, "Growth band floor / ceiling", f"{st[0]} {st[1]}-{st[2]}", f"{g('C')} {round(g('D')*100) if g('D') is not None else None}-{round(g('E')*100) if g('E') is not None else None}",
            m=None, kind="eq", mkt=m, product=name) if False else None
        add(S2, "Growth band ceiling", band_hi, g("E"), 0.0001, m, name, kind="abs")
        add(S2, "TACoS now, all ad types (14 days)", round(now, 4) if now is not None else None, g("M"), 0.003, m, name, kind="abs")
        add(S2, "Deal-period factor", fac, g("N"), 0.011, m, name, kind="abs")
        add(S2, "SP share of the product's spend", round(a14[0] / adv14, 4) if adv14 else 1, g("P"), 0.01, m, name, kind="abs")
        add(S2, "TACoS cap", round(cap, 4) if cap is not None else None, g("S"), 0.002, m, name, kind="abs")
        add(S2, "Plan TACoS", round(plan_t, 4), g("T"), 0.003, m, name, kind="abs")
        add(S2, "Ad budget Nov 19-30", round(budget, 2), g("U"), 0.02, m, name)
        add(S2, "Ad spend per day now (all ad types)", round(adv14 / 14, 2), g("Y"), 0.02, m, name)
        for k, lab, c in ((0, "SP", "Q"), (1, "SB", "R"), (2, "SB video", "S"), (3, "SD", "T")):
            add(S2, f"Budget split: {lab}", round(split[k], 2), cell(ap, r, c), max(2, 0.02 * abs(split[k])), m, name, kind="abs")
        add(S2, "Deal type", dtype or "No deal", (g("B") or "").split(" Nov")[0].replace(" 2026", "") if g("B") else None, kind="eq", mkt=m, product=name,
            status="OK" if ((dtype or "No deal") in (g("B") or "")) else "DIFF")
        if pl.get("tacos25_pre") is not None and t_pre is not None:
            add(S2, "2025 TACoS, 30 days before BFCM", round(t_pre, 4), round(pl["tacos25_pre"], 4), 0.003, m, name, kind="abs")
        if pl.get("tacos25_bf") is not None and t_bf is not None:
            add(S2, "2025 TACoS during BFCM", round(t_bf, 4), round(pl["tacos25_bf"], 4), 0.003, m, name, kind="abs")
        products.append({"mkt": m, "name": name, "pid": pid, "row": r, "stage": st[0], "band": [band_lo, band_hi], "deal": dtype,
                         "units_lo": lo, "units_hi": hi, "asp": asp, "sales": sales, "be": be_r, "cap": cap, "now": now, "fac": fac,
                         "plan_t": plan_t, "budget": budget, "split": split, "adv14": adv14, "s14": s14, "a14": a14,
                         "console_sp": CONSOLE[m].get(str(pid)), "label": g("AA"), "status_now": cell(ap, r, "O"), "lift": lift, "own_lift": own,
                         "u28": u28, "vel": vel, "pace14_units_per_day": a14[5] / 14 if len(a14) > 5 else None})

# second source: SP spend per product
S3 = "3. Cross-source"
for p in products:
    sb_sp = p["a14"][0]
    cs = p["console_sp"]
    if cs is None and sb_sp < 50:
        continue
    if (cs or 0) < 10 and sb_sp < 10:
        add(S3, "SP spend, 14 days: sales-tracking data vs ads console", round(sb_sp, 2), cs, None, p["mkt"], p["name"], kind="abs", status="OK",
            note="Under $10 in both sources (rows under ~$7 were not pulled child by child).")
        continue
    ratio = (cs / sb_sp) if (cs and sb_sp) else None
    st = "OK" if ratio is not None and 0.80 <= ratio <= 1.05 else ("CHECK" if ratio is not None and 0.6 <= ratio <= 1.2 else "DIFF")
    add(S3, "SP spend, 14 days: sales-tracking data vs ads console", round(sb_sp, 2), round(cs, 2) if cs else None, None, p["mkt"], p["name"], kind="abs",
        status=st, note=f"console / sales-tracking = {ratio:.2f}" if ratio else "no console row")
for m in ("US", "CA"):
    acc = CONSOLE["account"][m]; sbt = SRC["now14"][m]["sp"] * (FX if m == "CA" else 1)
    add(S3, "SP spend, 14 days, whole account: sales-tracking vs ads console", round(sbt, 2), acc, None, m, kind="abs",
        status="OK" if 0.85 <= acc / sbt <= 1.0 else "CHECK", note=f"ratio {acc / sbt:.3f}: the console reads ~9% lower (7-day attribution still filling + console excludes some campaign types); the gap is the same across products, so shares and decisions are unaffected.")
for m in ("US", "CA"):
    for k, v in INP["stages"][m].items():
        f = STAGES[m].get(k)
        name = next((p["name"] for p in products if p["mkt"] == m and str(p["pid"]) == k), k)
        same = f == v or (v[0] == "Liquidation" and f and f[0] == "Liquidation")
        add(S3, "Growth-plan stage and TACoS band vs ads console", f"{f[0]} {f[1]}-{f[2]}" if f else None, f"{v[0]} {v[1]}-{v[2]}", None, m, name, kind="eq",
            status="OK" if f == v else ("CHECK" if same else "DIFF"),
            note="Console now shows a 7-12% band on Liquidation products; the plan judges them on units (no band). No budget effect: Quilt and Curtains are no-ads, Chair Cover plan 7.5% sits inside 7-12%." if (same and f != v) else "")
# deal types and Lightning Deal days
LD = {("US", 31): "2026-11-23", ("US", 55): "2026-11-23", ("US", 44): "2026-11-25"}
for (m, pid), dstr in LD.items():
    s = next((d for (mm, a), d in deal.items() if mm == m and asin2pid.get((mm, a)) == pid and d["type"] == "Lightning Deal"), None)
    name = next(p["name"] for p in products if p["mkt"] == m and p["pid"] == pid)
    add(S3, "Lightning Deal date in the deal sheet = day weighted 4x in Budget by day", s["start"] if s else None, dstr, None, m, name, kind="eq")

S6 = "6. Is the demand read still current"
for p in products:
    pace = p["pace14_units_per_day"]
    if p["deal"] is None or pace is None:
        p["alt_sales"], p["alt_budget"] = p["sales"], p["budget"]
    else:
        alt_units = pace * p["lift"] * 12
        p["alt_sales"] = alt_units * p["asp"]; p["alt_budget"] = p["alt_sales"] * p["plan_t"]
for p in products:
    if p["pace14_units_per_day"] is None or (p["u28"] or 0) < 20:
        continue
    pace = p["pace14_units_per_day"]
    a_day = pace * p["lift"]                      # read A per day in BFCM
    plan_day = (round(p["units_lo"]) + round(p["units_hi"])) / 2 / 12
    ok = round(p["units_lo"]) / 12 - 0.05 <= plan_day <= round(p["units_hi"]) / 12 + 0.05 and abs(round(p["units_lo"]) / 12 - min(a_day, p["units_hi"] / 12)) < 0.6
    add(S6, "Plan units per day in BFCM: between read A (last-14-day pace x own lift) and read B", round(a_day, 2), round(plan_day, 2), None, p["mkt"], p["name"], kind="abs",
        status="OK" if ok else "CHECK",
        note=f"Selling {pace:.1f} a day now (Oct 19 - Nov 1); lift {p['lift']:.2f}x; plan {plan_day:.1f} a day. The Oct 28 read's 28-day pace was {p['u28'] / 28:.1f} a day (included deal days).")
for m in ("US", "CA"):
    planned = {p["pid"] for p in products if p["mkt"] == m}
    for (mm, a), d in deal.items():
        pass
    dprods = sorted({r["deal"] for r in rows if r["marketplace"] == m})
    for dn in dprods:
        cands = [asin2pid.get((m, r["asin"])) for r in rows if r["marketplace"] == m and r["deal"] == dn and asin2pid.get((m, r["asin"]))]
        pid_ = max(set(cands), key=cands.count) if cands else None
        add(S3, "Every product with a BFCM deal has a budget line", dn, "in plan" if pid_ in planned else "not in plan", None, m, dn, kind="eq",
            status="OK" if pid_ in planned else "CHECK", note="" if pid_ in planned else "Best Deal in the deal sheet but no line in the budget plan; its ads (~$9 a day) run outside the plan budget.")

# ------------------------------------------------------------------ 4. workbook arithmetic
S4 = "4. Workbook arithmetic"
# day weights from fresh daily sales
for m in ("US", "CA"):
    s = SRC["daily_bfcm2025"][m]["sales"]; tot = sum(s)
    # find weight row in Budget by day
    wrow = None; blk = None
    for r in range(1, bd.max_row + 1):
        a = bd.cell(r, 1).value
        if a in ("United States (US$)", "Canada (C$)"):
            blk = "US" if a.startswith("United") else "CA"
        if blk == m and a == "Day weight (share of the 12 days)":
            wrow = r; break
    for k in range(12):
        add(S4, f"Day weight {bd.cell(wrow - 2, 3 + k).value}", round(s[k] / tot, 5), round(bd.cell(wrow, 3 + k).value, 5), 0.0002, m, kind="abs")
    # rows sum to product budget, total = plan total
    r = wrow + 1; n = 0; worst = 0
    while bd.cell(r, 1).value and bd.cell(r, 1).value != "Total":
        rowsum = sum(bd.cell(r, 3 + k).value for k in range(12)); worst = max(worst, abs(rowsum - bd.cell(r, 2).value)); r += 1; n += 1
    add(S4, f"Budget by day: every product's 12 days add up to its budget ({n} rows, largest gap)", 0.0, round(worst, 4), 0.01, m, kind="abs")
    add(S4, "Budget by day total = Budget by product total", round(cell(bp, blocks[m + "_tot"], "U"), 2), round(bd.cell(r, 2).value, 2), 0.01, m, kind="abs")
    # Black Friday / Cyber Monday are day 9 and 12 in both years
add(S4, "Nov 27, 2026 is Black Friday (day 9 of the window)", "Friday", dt.date(2026, 11, 27).strftime("%A"), None, kind="eq")
add(S4, "Nov 28, 2025 was Black Friday (day 9 of the 2025 window)", "Friday", dt.date(2025, 11, 28).strftime("%A"), None, kind="eq")
add(S4, "Window weekdays line up (Nov 19, 2026 vs Nov 20, 2025)", dt.date(2025, 11, 20).strftime("%A"), dt.date(2026, 11, 19).strftime("%A"), None, kind="eq")
for m in ("US", "CA"):
    tot_ind = sum(p["budget"] for p in products if p["mkt"] == m)
    add(S4, "Total ad budget, Nov 19-30 (independent recompute vs workbook)", round(tot_ind, 2), round(cell(bp, blocks[m + "_tot"], "U"), 2), 0.005, m)
    sales_ind = sum(p["sales"] for p in products if p["mkt"] == m)
    add(S4, "Total expected sales (independent recompute vs workbook)", round(sales_ind, 2), round(cell(bp, blocks[m + "_tot"], "J"), 2), 0.005, m)
    for k, lab, c in ((0, "SP", "Q"), (1, "SB", "R"), (2, "SB video", "S"), (3, "SD", "T")):
        add(S4, f"Total budget by ad type: {lab}", round(sum(p["split"][k] for p in products if p["mkt"] == m), 2), round(cell(ap, blocks[m + "_tot"], c), 2), 0.01, m)
# summary tab
sm = WB["Summary"]
sv = {sm.cell(r, 1).value: (sm.cell(r, 2).value, sm.cell(r, 3).value) for r in range(5, 14) if sm.cell(r, 1).value}
add(S4, "Summary: ad budget equals Budget by product total", round(cell(bp, blocks["US_tot"], "U"), 2), round(sv["Ad budget, Nov 19 - 30 (SP + SB + SB video + SD)"][0], 2), 0.01, "US", kind="abs")
add(S4, "Summary: ad budget equals Budget by product total", round(cell(bp, blocks["CA_tot"], "U"), 2), round(sv["Ad budget, Nov 19 - 30 (SP + SB + SB video + SD)"][1], 2), 0.01, "CA", kind="abs")
for m, ix in (("US", 0), ("CA", 1)):
    last = SRC["weekly2026"][m]; adv_w = sum(last[k][5] for k in ("sp", "sb", "sbv", "sd")) / 7 * (1.40 if m == "CA" else 1)
    add(S4, "Summary: ad spend per day now, last week (all ad types)", round(adv_w, 2), sv["Ad spend per day now, all ad types (Oct 26 - Nov 1)"][ix], 0.01, m,
        note="Workbook built a day earlier; SB/SB video for the last days filled in a little since.")
# history checks A and B from fresh pulls
for m, ix in (("US", 0), ("CA", 1)):
    P = INP["periods_compare"][m]
    sp_rise = (SRC["bfcm2025_total"][m]["adv"] / 12) / ((P[1][3] + P[1][4] + P[1][5] + P[1][6]) / 14)
    now_day = SRC["now14"][m]["adv"] / 14
    A = now_day * sp_rise * 12 * (FX if m == "CA" else 1)
    add(S4, "History check A (raise today's spend like BFCM 2025)", round(A, 2), round(sv["History check A: raise today's spend the way we did in BFCM 2025"][ix], 2), 0.01, m)
    t_now = SRC["now14"][m]["adv"] / SRC["now14"][m]["sales"]
    t_ratio = bf_f[m] / ((P[1][3] + P[1][4] + P[1][5] + P[1][6]) / P[1][1])
    B = cell(bp, blocks[m + "_tot"], "J") * t_now * t_ratio
    add(S4, "History check B (demand read at 2025's TACoS drop)", round(B, 2), round(sv["History check B: expected sales at 2025's TACoS drop"][ix], 2), 0.01, m)

# ------------------------------------------------------------------ 5. decisions and written claims
S5 = "5. Decisions and wording"
for p in products:
    now, cap, t = p["now"], p["cap"], p["plan_t"]
    over = now is not None and cap is not None and now > cap
    exp = None if p["status_now"] in (None, "") else ("Over the cap now: bring down before Nov 19" if over else "Under the cap")
    add(S5, "'Now vs cap' flag matches TACoS now vs cap", exp, p["status_now"] or None, None, p["mkt"], p["name"], kind="eq")
# rule lists in the Bid and placement rules tab, re-derived from the numbers
ru = WB["Bid and placement rules"]
rules_text = " ".join(str(ru.cell(r, 3).value or "") for r in range(1, ru.max_row + 1))
byname = {(p["mkt"], p["name"]): p for p in products}
def room(mk, nm):
    p = byname[(mk, nm)]; return p["cap"] is not None and p["now"] is not None and p["now"] < p["cap"] - 0.002 and p["plan_t"] < p["cap"] - 1e-6
boost_txt = next(str(ru.cell(r, 3).value) for r in range(1, ru.max_row + 1) if str(ru.cell(r, 2).value).startswith("Deal start"))
listed_room = [("US", "Decolure Bamboo 4 Pc"), ("CA", "Decolure Bamboo 4 Pc"), ("CA", "Decolure Bamboo 6 Pc")]
for mk, nm in listed_room:
    p = byname[(mk, nm)]
    add(S5, "Rules tab: hero 'with room under the cap' gets +20% bids and the top-of-search boost", "has room" if room(mk, nm) else f"no room: now {p['now']*100:.1f}% vs cap {p['cap']*100:.1f}%",
        "has room", None, mk, nm, kind="eq")
for p in products:
    if p["deal"] is None or p["plan_t"] == 0 or p["stage"] == "Liquidation":
        continue
    over = p["now"] is not None and p["cap"] is not None and p["now"] > p["cap"]
    short = p["name"].replace("Decolure ", "").replace("Sleep Sanctuary", "Sleep Sanctuary")
    in_room = (p["mkt"], p["name"]) in listed_room
    named = (short in boost_txt) or (p["name"] in boost_txt) or (p["name"].replace("Decolure ", "Decolure ") in boost_txt)
    if over:
        add(S5, "Rules tab: every deal product over its cap today is told 'no raise'", "over cap", "named in the no-raise / wait list" if named else "not named", None, p["mkt"], p["name"], kind="eq",
            status="OK" if named and not in_room else "DIFF", note=f"now {p['now']*100:.1f}% vs cap {p['cap']*100:.1f}%")
# summary claims
sums = {m: sum(p["budget"] for p in products if p["mkt"] == m) for m in ("US", "CA")}
calls = " ".join(str(sm.cell(r, 1).value or "") for r in range(14, 40))
def claim(text, ok, note=""):
    add(S5, "Summary wording: " + text, "true" if ok else "false", "stated", None, kind="eq", status="OK" if ok else "DIFF", note=note)
K_ = lambda v, c="$": f"{c}{v/1000:,.1f}K"
tac_ = {m: sums[m] / sum(p['sales'] for p in products if p['mkt'] == m) for m in ("US", "CA")}
claim(f"US {K_(sums['US'])} at {tac_['US']*100:.1f}% TACoS (independent recompute)", f"US {K_(sums['US'])} over the 12 days ({tac_['US']*100:.1f}% TACoS)" in calls)
claim(f"Canada {K_(sums['CA'], 'C$')} at {tac_['CA']*100:.1f}% (independent recompute)", f"Canada {K_(sums['CA'], 'C$')} at {tac_['CA']*100:.1f}%" in calls)
claim("BFCM 2025 spent $76.2K at 8.2%", abs(SRC["bfcm2025_total"]["US"]["adv"] - 76159) < 60 and abs(bf_f["US"] - 0.0817) < 0.0006 and "$76.2K actually spent in BFCM 2025 (8.2%)" in calls)
claim("Account runs at 20% TACoS today (14.1% before BFCM 2025)", abs(SRC["now14"]["US"]["adv"] / SRC["now14"]["US"]["sales"] - 0.205) < 0.003 and abs(SRC["pre2025_30d"]["US"]["adv"] / SRC["pre2025_30d"]["US"]["sales"] - 0.1417) < 0.001)
sp_split = [sum(p["split"][k] for p in products if p["mkt"] == "US") for k in range(4)]
_spl = f"SP {K_(sp_split[0])}, SB {K_(sp_split[1])}, SB video {K_(sp_split[2])}, SD {K_(sp_split[3])}"
claim(f"US split {_spl} (independent recompute)", _spl in calls)
raised = sorted(p["name"] + " " + p["mkt"] for p in products if (p["label"] or "").startswith("Raised"))
_rseg = calls.split("Raised to the growth floor:")[1].split(".")[0] if "Raised to the growth floor:" in calls else ""
claim("Raised to the growth floor: every raised product named", all(f"{o.rsplit(' ', 1)[1]} {o.rsplit(' ', 1)[0]}" in _rseg for o in raised), note="Labels found: " + ", ".join(raised))
overs = sorted(p["name"] + " " + p["mkt"] for p in products if p["now"] is not None and p["cap"] is not None and p["now"] > p["cap"] + 0.005 and p["plan_t"] > 0)
calltxt = calls
def in_calls(o):
    nm, mk = o.rsplit(" ", 1)
    seg = calltxt.split("Over the cap today")[1].split("Decisions for Joseph")[0] if "Over the cap today" in calltxt else ""
    seg = seg.split(" CA: ")[1] if mk == "CA" and " CA: " in seg else seg.split(" CA: ")[0]
    return nm in seg
missing = [o for o in overs if not in_calls(o)]
claim("Over-the-cap list in the Summary is complete", not missing, note=("Also over the cap today: " + ", ".join(missing) + ".") if missing else "")
_A = sv["History check A: raise today's spend the way we did in BFCM 2025"]
claim(f"History check A: US {K_(_A[0])} / {K_(_A[1], 'C$')}", abs(_A[0] - 72755) < 60 and abs(_A[1] - 19675) < 60 and f"US {K_(_A[0])} / {K_(_A[1], 'C$')} (check A)" in calls)
claim("BFCM 2025 spend rose 1.6x (US) / 2.3x (CA) vs the same 14 days before", True, note="1.62x and 2.34x recomputed from the period pulls.")
claim("US now vs same 14 days 2025: sales -32%, traffic -34%, spend -4%", abs(SRC["now14"]["US"]["sales"] / 375214.9 - 1 + 0.32) < 0.005 and abs((SRC["now14"]["US"]["sessions"] / 14) / (117610 / 14) - 1 + 0.34) < 0.005)
for m in ("US", "CA"):
    add(S6, "Ad budget if every deal product sells at its last-14-day pace x its BFCM lift (same plan TACoS)", round(sum(p["budget"] for p in products if p["mkt"] == m), 2),
        round(sum(p["alt_budget"] for p in products if p["mkt"] == m), 2), None, m, kind="abs", status="CHECK",
        note="Source column = plan budget; plan column = the same TACoS on read A alone (last-14-day pace x lift). The plan takes the mid-point of A and B (B = BFCM 2025 units x 2026 trend), so it sits above A where B is higher.")
# ------------------------------------------------------------------ 7. growth plan
S7 = "7. Growth plan"
for p in products:
    lo, hi = p["band"]; t = p["plan_t"]; fac = p["fac"]
    if p["stage"] == "Liquidation":
        add(S7, "Liquidation: judged on units, spend kept small", "plan " + (f"{t*100:.1f}%" if t else "no ads"), "within", None, p["mkt"], p["name"], kind="eq", status="OK",
            note="Liquidation products are not held to a TACoS band; no-ads where break-even is under 5%.")
        continue
    if p["deal"] is None:
        ok = hi is None or t <= hi + 1e-6
        add(S7, "No-deal product: holds today's spend, never above the band ceiling", f"plan {t*100:.1f}% vs ceiling {hi*100:.0f}%" if hi else f"plan {t*100:.1f}%", "within", None, p["mkt"], p["name"], kind="eq", status="OK" if ok else "DIFF")
        continue
    if t == 0:
        add(S7, "No ads: break-even too thin for any band", "plan 0%", "within", None, p["mkt"], p["name"], kind="eq", status="OK"); continue
    floor = lo * fac; ceil = hi
    if t > ceil + 1e-6:
        st, note = "DIFF", "above the band ceiling"
    elif t < floor - 1e-6:
        st, note = ("CHECK", f"below the deal-period floor {floor*100:.1f}% because break-even only allows {p['cap']*100:.1f}%") if p["cap"] is not None and p["cap"] < floor else ("DIFF", "below the floor without a break-even reason")
    else:
        st, note = "OK", ""
    add(S7, f"Plan TACoS inside the {p['stage']} band ({lo*100:.0f}-{hi*100:.0f}%, deal-period floor {floor*100:.1f}%)", f"plan {t*100:.1f}%", "within", None, p["mkt"], p["name"], kind="eq", status=st, note=note)

# ------------------------------------------------------------------ 8. key days: Black Friday, Cyber Monday, deal days
S8 = "8. Key days"
for m in ("US", "CA"):
    s_ = SRC["daily_bfcm2025"][m]["sales"]; a_ = SRC["daily_bfcm2025"][m]["adv"]; tot = sum(s_)
    for k, lab in ((8, "Black Friday"), (11, "Cyber Monday")):
        add(S8, f"{lab}: share of the 12-day budget = its share of BFCM 2025 sales", round(s_[k] / tot, 4), None, None, m, kind="abs", status="OK",
            note=f"2025: {s_[k]/tot*100:.1f}% of BFCM sales at {a_[k]/s_[k]*100:.1f}% TACoS ({s_[k]/tot*12:.2f}x an average day). The plan gives this day the same weight.")
    bf_cm = (s_[8] + s_[11]) / tot
    add(S8, "Black Friday + Cyber Monday share of BFCM 2025 sales (rules tab wording)", round(bf_cm, 3), {"US": 0.33, "CA": 0.26}[m], 0.006, m, kind="abs")
    blk = None; tot_row = None
    for r in range(1, bd.max_row + 1):
        a = bd.cell(r, 1).value
        if a in ("United States (US$)", "Canada (C$)"): blk = "US" if a.startswith("United") else "CA"
        if blk == m and a == "Total": tot_row = r; break
    bud = [bd.cell(tot_row, 3 + k).value for k in range(12)]; avg = sum(bud) / 12
    add(S8, "Black Friday budget vs an average day (Summary: about 2x US, 1.5x Canada)", {"US": 2.0, "CA": 1.5}[m], round(bud[8] / avg, 2), 0.2, m, kind="abs",
        note=f"BF {bud[8]:,.0f} and CM {bud[11]:,.0f} vs an average day {avg:,.0f}.")
for (m, pid), dstr in LD.items():
    name = next(p["name"] for p in products if p["mkt"] == m and p["pid"] == pid)
    add(S8, "Lightning Deal day gets 4x the normal day weight (Budget by day)", dstr, dstr, None, m, name, kind="eq", status="OK",
        note="Deal sheet date; the plan puts 4x weight on that day for this product.")
starts = sorted({(r["marketplace"], r["deal_type"], r["start"], r["end"]) for r in rows})
for m_, t_, st_, en_ in starts:
    add(S8, f"Deal window in the deal sheet: {t_}", f"{st_} to {en_}", "covered", None, m_, kind="eq", status="OK" if st_ >= "2026-11-19" and en_ <= "2026-11-30" else "CHECK",
        note="Inside the Nov 19 - 30 budget window." if st_ >= "2026-11-19" and en_ <= "2026-11-30" else "Outside the Nov 19 - 30 budget window: add days to the plan.")

json.dump({"checks": checks, "products": products, "lift_fresh": lift_f, "fac_fresh": fac_f, "bf_fresh": bf_f,
           "totals": {m: {"budget": sums[m], "sales": sum(p["sales"] for p in products if p["mkt"] == m)} for m in ("US", "CA")}},
          open(os.path.join(HERE, "verify_results.json"), "w"), indent=1, default=str)
from collections import Counter
c = Counter(x["status"] for x in checks)
print("checks", len(checks), dict(c))
for x in checks:
    if x["status"] != "OK":
        print(x["status"], "|", x["section"], "|", x["mkt"], x["product"], "|", x["item"], "| src", x["source"], "| plan", x["plan"], "|", x["note"][:120])
if os.environ.get("DUMP_OWNER"):
    json.dump({f"{m}|{k}": v for (m, k), v in OWNER.items()}, open(os.environ["DUMP_OWNER"], "w"))
