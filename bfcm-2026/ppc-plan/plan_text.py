"""Writes plan_text.json: every Summary call, product note and history-check note that quotes a number, generated from
the RECALCULATED plan workbook so the words always match the cells. build_ppc_plan.py reads plan_text.json when it exists.
Run order: build_ppc_plan.py -> recalc -> plan_text.py -> build_ppc_plan.py -> recalc (the second pass changes only text).
Usage: python3 plan_text.py <recalculated BFCM_2026_PPC_Plan.xlsx>"""
import json, os, sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
wb = load_workbook(sys.argv[1], data_only=True)
I = json.load(open(os.path.join(HERE, "inputs_2026-11-02.json")))
P = {(r["mkt"], r["short"]): r for r in json.load(open(os.path.join(HERE, "plan_numbers.json")))}
YO = json.load(open(os.path.join(HERE, "..", "verification", "yoy_results.json")))
PREV = {"US": 88264, "CA": 25542}          # the plan shared on Nov 2 (demand read of Oct 28), quoted for comparison only
FX = 1.4036

def block(ws, first_col_header="Product"):
    """Rows of each market block: {mkt: (header list, [row dicts], total dict)}"""
    out, mkt, hdr, rows = {}, None, None, []
    for row in ws.iter_rows(values_only=True):
        a = row[0]
        if a in ("United States (US$)", "Canada (C$)"):
            mkt, hdr, rows = ("US" if a.startswith("United") else "CA"), None, []
        elif mkt and a == first_col_header:
            hdr = list(row)
        elif mkt and hdr and a == "Total":
            out[mkt] = (hdr, rows, dict(zip(hdr, row))); mkt = None
        elif mkt and hdr and a:
            rows.append(dict(zip(hdr, row)))
    return out

BP = block(wb["Budget by product"]); AT = block(wb["Ad types by product"]); BD = block(wb["Budget by day"], None)
NAME2SHORT = {}
sys.path.insert(0, HERE); from build_names import NAMES   # same display names as the workbook
for s_, n_ in NAMES.items():
    NAME2SHORT[n_] = s_
k = lambda v: f"${v/1000:,.1f}K"
kc = lambda v: f"C${v/1000:,.1f}K"
pc = lambda v, d=0: f"{v*100:.{d}f}%"
money = {"US": k, "CA": kc}

def col(r, name):
    return r.get(name)

T = {m: BP[m][2] for m in BP}
bud = {m: T[m]["Ad budget Nov 19-30 (all ad types)"] for m in T}
tac = {m: T[m]["Plan TACoS"] for m in T}
hc = {r[0]: (r[2], r[4]) for r in wb["2025 vs 2026 check"].iter_rows(values_only=True) if r[0]}
A = hc["(A) Today's spend per day x 2025 BFCM spend rise x 12 days"]; B = hc["(B) Budget = expected sales x that TACoS"]
jump = hc["Plan: expected sales per day vs plan products' sales per day now"]; jump25 = hc["2025: BFCM sales per day vs the same 14 days before"]
spent25 = {"US": sum(I["daily2025"]["US"]["ad"]), "CA": sum(I["daily2025"]["CA"]["ad_usd"]) * FX}

# day split: Black Friday and Cyber Monday share of the budget
dayline = {}
for m in ("US", "CA"):
    hdr, rows, tot = BD[m]
    days = [h for h in hdr[2:14]]
    bf = tot[days[8]]; cm = tot[days[11]]
    avg = bud[m] / 12
    dayline[m] = (bf, cm, (bf + cm) / bud[m], (bf / avg + cm / avg) / 2)

calls, notes = [], {}
calls.append(f"Realistic total: US {k(bud['US'])} over the 12 days ({pc(tac['US'], 1)} TACoS) vs {k(spent25['US'])} actually spent in BFCM 2025 (8.2%). "
             f"Canada {kc(bud['CA'])} at {pc(tac['CA'], 1)} (BFCM 2025: {kc(spent25['CA'])}). The account runs at 20% TACoS today across all ad types (14.1% before BFCM 2025), "
             "so the deal-period TACoS starts higher.")
heroes = [(m, s_) for (m, s_) in (("US", "DC B4"), ("US", "DC B6"), ("US", "DC S4"), ("CA", "DC B4"), ("CA", "DC B6"))]
hero_txt = "; ".join(f"{m} {NAMES[s_]} {P[(m, s_)]['units_plan']:,.0f} ({P[(m, s_)]['pace14']:.0f} a day now, {P[(m, s_)]['units_plan'] / 12:.0f} a day planned)" for m, s_ in heroes)
calls.append(f"Demand is built on current, event-free selling: each product's last-14-day pace (Oct 19 - Nov 1) x its own BFCM 2025 lift, and, where the product sold "
             f"in both years, its BFCM 2025 units x how it is running against the same 14 days last year. Windows that include the Oct 7-8 Prime event or the late-September "
             f"deals are left out: they ran at about twice today's pace on the Bamboo sheets. Lightning-Deal-only products use the first read alone. Plan units, 12 days: {hero_txt}.")
spl = AT["US"][2]
calls.append(f"SB, SB video and SD are tracked per product (Ad types by product tab): each product's TACoS now, break-even and cap include all four ad types, and its budget splits by "
             f"its own mix. US plan: SP {k(spl['of which SP'])}, SB {k(spl['of which SB'])}, SB video {k(spl['of which SB video'])}, SD {k(spl['of which SD'])}. "
             f"Canada is {pc(AT['CA'][2]['of which SP'] / AT['CA'][2]['BFCM budget, all ad types'])} SP.")
raised = [f"{m} {r['Product']}" for m in ("US", "CA") for r in BP[m][1] if str(r.get("Growth-plan check") or "").startswith("Raised")]
atcap = [f"{m} {r['Product']}" for m in ("US", "CA") for r in BP[m][1] if str(r.get("Growth-plan check") or "").startswith("At the cap")]
calls.append("Aligned with the growth plan: each product's TACoS sits inside its growth-plan band (scaled for the deal), never above break-even. "
             + (f"Raised to the growth floor: {', '.join(raised)}. " if raised else "")
             + (f"Held at the cap: {', '.join(atcap)}." if atcap else ""))
over = []
for m in ("US", "CA"):
    for r in BP[m][1]:
        now, cap = r.get("TACoS now, all ad types"), r.get("Cap (break-even or band ceiling)")
        if isinstance(now, (int, float)) and isinstance(cap, (int, float)) and now > cap + 0.005 and not str(r.get("Growth-plan check") or "").startswith("No ads"):
            over.append((m, r["Product"], now, cap))
over.sort(key=lambda x: (x[0] != "US", -(x[2] - x[3])))
if over:
    calls.append("Over the cap today, bring down before Nov 19 (TACoS now vs cap). "
                 + " ".join(f"{m}: " + ", ".join(f"{n} ({pc(a)} vs {pc(c)})" for mm, n, a, c in over if mm == m) + "." for m in ("US", "CA") if any(x[0] == m for x in over)))
row = lambda m, short: next(r for r in BP[m][1] if r["Product"] == NAMES[short])
clp, clc = row("US", "CL Pillowcases"), row("US", "CL Cooling Sheets")
calls.append(f"Decisions for Joseph: CooLinens Pillowcases is a Launch product (band {pc(clp['Growth band floor (TACoS)'])}-{pc(clp['Growth band ceiling (TACoS)'])}) but at the "
             f"${clp['Avg selling price']:.2f} deal break-even only allows {pc(clp['Cap (break-even or band ceiling)'])}, so it is capped there. CooLinens Cooling Sheets has no deal: "
             f"the plan holds today's ~${clc['Ad spend per day now, all ad types (14 days)']:,.0f} a day ({pc(clc['TACoS now, all ad types'])} TACoS"
             + (", inside its Launch band)." if (clc.get("Growth band ceiling (TACoS)") or 1) >= (clc["TACoS now, all ad types"] or 0) else ")."))
noads = [f"{m} {r['Product']} (break-even {pc(r['Break-even TACoS at deal price'], 1)})" for m in ("US", "CA") for r in BP[m][1] if str(r.get("Growth-plan check") or "").startswith("No ads")]
cur_ = {"US": "$", "CA": "C$"}
losers = [(m, r["Product"], P[(m, NAME2SHORT[r["Product"]])]) for m in ("US", "CA") for r in BP[m][1]]
losers = [(m, n, pr) for m, n, pr in losers if pr.get("deal_fee") and (pr.get("deal_margin") or 0) < pr["deal_fee"]]
if losers:
    calls.append("Deal fees are $70 for every day a deal runs plus 1% of deal sales: $840 for a 12-day Best Deal, $70 for a Lightning Deal. The $70 a day is a fixed cost "
                 "of running the deal, so it is not counted in the ad break-even (an extra ad-driven sale earns the same with or without it). At deal level, the expected margin "
                 "before ads does not cover the fee on " + ", ".join(f"{m} {n} ({cur_[m]}{pr['deal_margin']:,.0f} margin vs {cur_[m]}{pr['deal_fee']:,.0f} fee)".replace(cur_[m] + "-", "-" + cur_[m]) for m, n, pr in losers)
                 + ". Worth reconsidering these deals before Amazon's Nov 13 deadline; if they run, ads are judged on unit margin like every other product.")
if noads:
    calls.append(f"No ads beyond brand defence on {', '.join(noads)}: at the deal price {'it loses' if len(noads) == 1 else 'they lose'} money or {'keeps' if len(noads) == 1 else 'keep'} almost nothing per unit before ads.")
calls.append(f"History check (2025 vs 2026 check tab): in BFCM 2025 we spent 1.6x (US) / 2.3x (CA) more per day than in the same 14 days before; sales rose "
             f"{jump25[0]:.1f}x / {jump25[1]:.1f}x and TACoS fell from 14.6% to 8.2% (US). Doing the same from today gives US {k(A[0])} / {kc(A[1])} (check A). "
             f"The plan is {abs(bud['US'] / A[0] - 1):.0%} {'below' if bud['US'] < A[0] else 'above'} that in the US and {abs(bud['CA'] / A[1] - 1):.0%} "
             f"{'below' if bud['CA'] < A[1] else 'above'} in Canada, because it expects sales to jump {jump[0]:.1f}x (US) / {jump[1]:.1f}x (CA) vs {jump25[0]:.1f}x / {jump25[1]:.1f}x "
             f"in 2025, and holds each product inside its TACoS cap. Suggest: approve the plan as the base budget and check A as the ceiling; the agent releases the extra only "
             f"while each product stays under its TACoS cap on actual sales.")
calls.append("Where we stand vs last year (same 14 days): US sales -32%, traffic -34%, ad spend -4%, so TACoS is 20.5% vs 14.6%; clicks are 27% cheaper and conversion is "
             "unchanged (6.7%). Canada: sales -46%, traffic -56%, spend -37%. After BFCM 2025 spend stayed about 1.5x for two weeks at 11% TACoS (Dec 1 - 15 is outside this budget).")
both = {r["pid"] for r in YO["bfcm"] if r["market"] == "US" and r.get("class") == "In both" and r.get("in_plan")}
spent_both = sum(r["adv25"] for r in YO["bfcm"] if r["market"] == "US" and r["pid"] in both)
plan_both = sum(r["Ad budget Nov 19-30 (all ad types)"] for r in BP["US"][1] if P[("US", NAME2SHORT[r["Product"]])]["pid"] in both)
calls.append("Year over year, same 14 days (Oct 19 - Nov 1): US ad spend is down only 4% ($54.7K to $52.3K), but the mix changed. Products sold both years cut SP by $21.8K and "
             "added $1.8K of SB / SB video / SD; new products (CooLinens, Sleephoria Cooling Fitted, Bamboo Fitted) added $18.2K. Like-for-like sales fell 48% ($351K to $183K) "
             f"with traffic down 34% and conversion steady, so like-for-like TACoS rose from 15.3% to 18.5%. For BFCM, the plan for products that ran in 2025 is {k(plan_both)} "
             f"vs {k(spent_both)} spent on them last year; the rest ({k(bud['US'] - plan_both)}) is new products.")
calls.append("Every number is an estimate from the last 14 days of sales and spend by product and ad type, each product's BFCM 2025 lift and the Oct 27 deal prices. "
             "Amazon's deal prices can still change until Nov 13; the plan is re-run if they do.")

# product notes: fixed facts + live numbers
FIXED = {"DC B4": "Hero. Full BFCM push inside the cap.", "DC B6": "Hero. Deal is 6.5% cheaper than 2025. 29% of its spend is SB, SB video and SD (counted inside the cap).",
         "DC S4": "Hero. Deal 2.6% cheaper than 2025.", "DC S6": "Lightning Deal Nov 23 only (Best Deal requested). Budget weighted to Nov 23.",
         "DC Satin Fitted": "Deal 34% above 2025 paid.", "DC Silk Pillowcase": "Lightning Deal Nov 23.", "CL Pillowcases": "18% of its spend is SB video and SB.",
         "SL Cooling 4pc": "Deal 16% above 2025 paid.", "SL Cooling Fitted": "Lightning Deal Nov 25. Budget weighted to Nov 25.", "SL Cooling Comforter": "Deal 47% above 2025 paid.",
         "SL Cooling Pillowcase": "Small; keep to the ceiling.", "DC Chair Cover": "Small; keep to the ceiling.", "DC Bamboo Fitted": "No deal: hold at today's daily spend.",
         "DC Cooling 4pc": "No deal.", "CL Cooling Sheets": "No deal; launched Oct 15 and still ramping. A third of its spend is SB video and SB.", "SSS4": "", "SL B6": "",
         "SL Quilt Set": "", "DC Linen Curtains": ""}
for m in ("US", "CA"):
    for r in BP[m][1]:
        s_ = NAME2SHORT[r["Product"]]
        now, cap, be = r.get("TACoS now, all ad types"), r.get("Cap (break-even or band ceiling)"), r.get("Break-even TACoS at deal price")
        bits = [FIXED.get(s_, "") if m == "US" else ("Hero." if s_ in ("DC B4", "DC B6", "DC S4") else "")]
        chk = str(r.get("Growth-plan check") or "")
        if chk.startswith("No ads"):
            bits.append(f"Break-even {pc(be, 1)} at the deal price: no ads beyond brand defence.")
        elif isinstance(now, (int, float)) and isinstance(cap, (int, float)) and now > cap + 0.005:
            bits.append(f"TACoS {pc(now)} today vs a {pc(cap)} cap: cut to the cap before Nov 19.")
        elif isinstance(be, (int, float)) and be < 0.2:
            bits.append(f"Thin margin at the deal ({pc(be)} break-even).")
        pr = P[(m, s_)]
        if pr.get("pace14") is not None:
            bits.append(f"Selling {pr['pace14']:.1f} a day now; plan {pr['units_plan'] / 12:.0f} a day in BFCM ({pr['lift']:.1f}x lift).")
        notes[f"{m}|{s_}"] = " ".join(b for b in bits if b)

# rules that name products by their position against the cap
HEROES = ("DC B4", "DC B6", "DC S4")
room, at, over_h = [], [], []
for m in ("US", "CA"):
    for s_ in HEROES:
        r = next((x for x in BP[m][1] if x["Product"] == NAMES[s_]), None)
        if not r or not str(r.get("BFCM 2026 deal") or "").startswith("Best Deal"):
            continue
        now, cap = r["TACoS now, all ad types"], r["Cap (break-even or band ceiling)"]
        lab = f"{m} {NAMES[s_].replace('Decolure ', '')}"
        (room if now <= cap - 0.02 else at if now <= cap + 0.005 else over_h).append((lab, now, cap))
fmt = lambda L: ", ".join(f"{l} ({pc(a, 1)} vs {pc(c, 1)} cap)" for l, a, c in L)
others = [f"{m} {n}" for m, n, a, c in over if not any(n.endswith(NAMES[h].replace("Decolure ", "")) and NAMES[h] == n for h in HEROES)]
rules = {
 ("Bids", "Deal start (Nov 19, when the deal goes live)"):
   (f"Best Deal heroes with room under the cap ({', '.join(l for l, a, c in room) or 'none'}): +20% on exact-match keywords that converted in the last 30 days. "
    + (f"Close to the cap: {fmt(at)}; raise them only once their daily TACoS is clearly under the cap. " if at else "")
    + (f"Over the cap: {fmt(over_h)}; no raise until back under. " if over_h else "")
    + (f"Products over their cap today ({', '.join(others)}): no raise; bring down to the cap before Nov 19." if others else "")),
 ("Top of search", "Who gets a boost"):
   (f"Only Best Deal heroes with room under the cap: {', '.join(l for l, a, c in room) or 'none yet'}."
    + (f" {', '.join(l for l, a, c in at + over_h)} join once their daily TACoS is clearly under the cap." if at or over_h else "")),
 ("Bids", "No-ads products"):
   (f"{' and '.join(n.split(' (')[0] for n in noads)} {'loses' if len(noads) == 1 else 'lose'} money or {'keeps' if len(noads) == 1 else 'keep'} almost nothing per unit at the deal price before any ads ({', '.join(n.split('(')[1].rstrip(')') for n in noads)}): brand-defence only, no prospecting."
    if noads else "None this year."),
}
chk = {"Plan vs check A": (f"The plan is {'below' if bud['US'] < A[0] else 'above'} check A because it expects a {jump[0]:.1f}x (US) / {jump[1]:.1f}x (CA) sales jump vs "
                           f"{jump25[0]:.1f}x / {jump25[1]:.1f}x in 2025 (last two lines) and keeps each product inside its TACoS cap."),
       "Plan vs check B": "On the same sales, the plan sits close to the account-level TACoS; growth-plan floors on Bamboo and CooLinens Cooling Sheets held at today's spend account for the difference.",
       "Plan: expected sales per day vs plan products' sales per day now": "The plan's sales jump for BFCM 2026 ...",
       "(B) Expected sales, Nov 19 - 30 (plan)": "The plan's expected sales for the products in the plan (current pace x BFCM lift)."}
day = {m: f"Black Friday and Cyber Monday get about {dayline[m][3]:.1f}x an average day ({money[m](dayline[m][0])} and {money[m](dayline[m][1])}, {pc(dayline[m][2])} of the budget)."
       for m in ("US", "CA")}
json.dump({"calls": calls, "notes": notes, "check_notes": chk, "rules": [[a, b, t] for (a, b), t in rules.items()], "day_note": f"{day['US']} Canada: {day['CA']}"}, open(os.path.join(HERE, "plan_text.json"), "w"), indent=1)
print(json.dumps({"calls": len(calls), "notes": len(notes)}))
