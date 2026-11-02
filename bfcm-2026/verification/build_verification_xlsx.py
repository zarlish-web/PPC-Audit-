"""Builds BFCM_2026_PPC_Verification.xlsx from verify_results.json + the fresh source pulls.
Usage: python3 build_verification_xlsx.py OUT.xlsx"""
import json, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "verify_results.json")))
SRC = json.load(open(os.path.join(HERE, "source", "account_pulls_2026-11-02.json")))
CON = json.load(open(os.path.join(HERE, "source", "ads_console_sp_by_product_2026-10-19_to_11-01.json")))
INP = json.load(open(os.path.join(HERE, "..", "ppc-plan", "inputs_2026-11-02.json")))
OUT = sys.argv[1]
NAVY, BLUE, GREEN = "1F3864", "0000FF", "008000"
F = lambda **k: Font(name="Arial", size=k.pop("size", 9), **k)
HDR = PatternFill("solid", fgColor=NAVY); YEL = PatternFill("solid", fgColor="FFF2CC")
OKF = PatternFill("solid", fgColor="E2EFDA"); CHF = PatternFill("solid", fgColor="FFF2CC"); DFF = PatternFill("solid", fgColor="F8CBAD")
BOX = Border(*(Side(style="thin", color="BFBFBF"),) * 4)
WRAP = Alignment(wrap_text=True, vertical="top"); CEN = Alignment(horizontal="center", vertical="center", wrap_text=True)
CUR = {"US": '"$"#,##0', "CA": '"C$"#,##0', "": '#,##0.00'}

wb = Workbook()

def header(ws, row, cols, height=30):
    for j, (h, w) in enumerate(cols, 1):
        c = ws.cell(row=row, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX
        if w:
            ws.column_dimensions[CL(j)].width = w
    ws.row_dimensions[row].height = height

def title(ws, t, sub=None, merge="L"):
    ws["A1"] = t; ws["A1"].font = F(size=13, bold=True, color=NAVY)
    if sub:
        ws["A2"] = sub; ws["A2"].font = F(italic=True, size=8.5); ws["A2"].alignment = WRAP; ws.merge_cells(f"A2:{merge}2"); ws.row_dimensions[2].height = 40
    ws.sheet_view.showGridLines = False

def status_fmt(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"OK"'], fill=OKF))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"CHECK"'], fill=CHF))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"DIFF"'], fill=DFF))

# ------------------------------------------------------------------ All checks
ac = wb.active; ac.title = "All checks"
title(ac, "Every check: the source value, the plan's value, the gap and the verdict",
      "One row per check. Source = the number rebuilt independently from the original records; Plan = what the delivered PPC plan workbook shows. "
      "Gap and 'Re-test' are live formulas: Re-test repeats the tolerance test on the numbers in this row (relative or absolute, as in the Kind column). "
      "Status is the verdict: OK = matches within tolerance; CHECK = a judgment item or an input with no second record; DIFF = mismatch (none left).", "M")
ACOLS = [("#", 5), ("Section", 18), ("Market", 6), ("Product", 24), ("What is checked", 46), ("Source (rebuilt)", 13), ("Plan / delivered", 13),
         ("Gap (plan - source)", 11), ("Tolerance", 9), ("Kind", 6), ("Re-test", 8), ("Status", 8), ("Note", 60)]
header(ac, 4, ACOLS)
r = 5
for i, x in enumerate(R["checks"], 1):
    src, pl = x["source"], x["plan"]
    vals = [i, x["section"], x["mkt"], x["product"], x["item"], src, pl, None, x["tol"], x["kind"], None, x["status"], x["note"]]
    for j, v in enumerate(vals, 1):
        c = ac.cell(row=r, column=j, value=v); c.border = BOX; c.font = F(color=BLUE if j in (6, 7) else "000000")
        if j in (5, 13): c.alignment = WRAP
        if j in (6, 7, 8) and isinstance(v, float):
            c.number_format = "0.0000" if abs(v) < 2 else "#,##0.00"
    ac.cell(row=r, column=8, value=f'=IF(AND(ISNUMBER(F{r}),ISNUMBER(G{r})),G{r}-F{r},"")').number_format = "#,##0.0000;-#,##0.0000;0"
    ac.cell(row=r, column=11, value=(f'=IF(AND(ISNUMBER(F{r}),ISNUMBER(G{r}),ISNUMBER(I{r})),IF(J{r}="abs",IF(ABS(G{r}-F{r})<=I{r}+0.000001,"pass","fail"),'
                                     f'IF(ABS(G{r}-F{r})<=I{r}*MAX(ABS(F{r}),ABS(G{r}),0.000000001)+0.000001,"pass","fail")),IF(F{r}=G{r},"same","n/a"))'))
    for j in (8, 11): ac.cell(row=r, column=j).border = BOX; ac.cell(row=r, column=j).font = F()
    r += 1
LAST = r - 1
status_fmt(ac, f"L5:L{LAST}")
ac.conditional_formatting.add(f"K5:K{LAST}", CellIsRule(operator="equal", formula=['"fail"'], fill=DFF))
ac.freeze_panes = "E5"; ac.auto_filter.ref = f"A4:M{LAST}"

# ------------------------------------------------------------------ Summary (first)
sm = wb.create_sheet("Summary", 0)
title(sm, "BFCM 2026 PPC plan: independent verification (Nov 2, 2026)",
      "Every number in the PPC plan was rebuilt from the original records with separate code (no reuse of the plan's scripts), then compared with the delivered workbook. "
      "Account figures were re-pulled fresh today; per-product ad spend was cross-checked against a second data source (the ads console). Counts below are live formulas on the All checks tab.", "H")
for j, (h, w) in enumerate([("Section", 34), ("Checks", 9), ("OK", 9), ("CHECK", 9), ("DIFF", 9), ("No mismatch", 10), ("What was tested", 70)], 1):
    c = sm.cell(row=4, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX; sm.column_dimensions[CL(j)].width = w
SECT = [("1. Source records", "Fresh account pulls reconcile to the files the plan used: 2025 daily = period totals; 2025 product files = account totals; plan inputs (daily 2025, weekly ad types, history periods) = fresh pulls; lift and deal-period factor; Canada COGS currency; 14-day child rows cover the account."),
        ("2. Product numbers", "Per product, rebuilt from the deal sheet, SKU lists, inventory export, 2025 product files and raw 14-day child rows: units, price, expected sales, break-even, band, TACoS now, factor, SP share, cap, plan TACoS, budget, split by ad type, deal type, 2025 TACoS."),
        ("3. Cross-source", "SP spend per product vs the ads console; growth stage and TACoS band vs the console; Lightning Deal dates vs the deal sheet; every deal product has a budget line."),
        ("4. Workbook arithmetic", "Day weights vs fresh 2025 daily sales; each product's 12 days add up to its budget; totals by product, by ad type and by day agree; weekday alignment; Summary links; history checks A and B recomputed."),
        ("5. Decisions and wording", "Over-cap flags, the boost / no-raise lists in the rules tab and every number written in the Summary re-derived from the data."),
        ("6. Is the demand read still current", "Each product's last-14-day unit pace vs the 28-day pace the demand read uses (as of Oct 15), and the budget at today's pace.")]
for i, (s_, what) in enumerate(SECT):
    rr = 5 + i
    sm.cell(row=rr, column=1, value=s_).font = F(bold=True)
    sm.cell(row=rr, column=2, value=f"=COUNTIF('All checks'!$B$5:$B${LAST},A{rr})")
    for j, st in ((3, "OK"), (4, "CHECK"), (5, "DIFF")):
        sm.cell(row=rr, column=j, value=f"=COUNTIFS('All checks'!$B$5:$B${LAST},$A{rr},'All checks'!$L$5:$L${LAST},\"{st}\")")
    sm.cell(row=rr, column=6, value=f"=IF(B{rr}>0,(C{rr}+D{rr})/B{rr},\"\")").number_format = "0%"
    sm.cell(row=rr, column=7, value=what).alignment = WRAP; sm.row_dimensions[rr].height = 36
    for j in range(1, 8): sm.cell(row=rr, column=j).border = BOX; sm.cell(row=rr, column=j).font = F(bold=(j == 1))
tr = 5 + len(SECT)
sm.cell(row=tr, column=1, value="Total").font = F(bold=True)
for j in range(2, 6):
    sm.cell(row=tr, column=j, value=f"=SUM({CL(j)}5:{CL(j)}{tr-1})").font = F(bold=True)
sm.cell(row=tr, column=6, value=f"=IF(B{tr}>0,(C{tr}+D{tr})/B{tr},\"\")").number_format = "0%"
for j in range(1, 8): sm.cell(row=tr, column=j).fill = YEL; sm.cell(row=tr, column=j).border = BOX
rr = tr + 2
sm.cell(row=rr, column=1, value="Verdict").font = F(size=11, bold=True, color=NAVY); rr += 1
US_T, CA_T = R["totals"]["US"], R["totals"]["CA"]
VERD = [f"The plan's arithmetic is right: rebuilt independently, the US budget is ${US_T['budget']:,.0f} and Canada C${CA_T['budget']:,.0f}, matching the workbook to the dollar; all 25 products match on units, price, break-even, cap, plan TACoS, budget and split by ad type.",
        "Every source input reconciles with today's fresh pulls (2025 sales to the cent; 2025 ad spend within 0.4%, late attribution). Growth stages and TACoS bands match the ads console for all 22 banded products.",
        "Three wording errors were found and fixed in the plan (see Findings): Satin 4 Pc (US) was listed as a hero with room for a +20% bid raise while already over its 12% cap; the no-raise list had a stale entry and missed products; the Summary's over-cap list missed four Canadian products.",
        "Biggest judgment call: the demand read's base pace (Oct 15, including Prime Big Deal Days) is well above today's pace for the Bamboo heroes (US Bamboo 4 Pc sells 0.51x, Bamboo 6 Pc 0.62x that pace). At today's pace the same TACoS plan needs about $53K (US) / C$17K (CA). The 2025-history check gives $73K / C$20K. The $88K / C$25.5K plan is the ceiling; the agent's TACoS caps on actual sales keep spend from running ahead of sales.",
        "Approve as: base budget = history check (US $73K, CA C$20K), ceiling = plan (US $88K, CA C$25.5K), released only while each product stays under its TACoS cap."]
for t in VERD:
    c = sm.cell(row=rr, column=1, value="• " + t); c.alignment = WRAP; sm.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=7); sm.row_dimensions[rr].height = 52; rr += 1
rr += 1
sm.cell(row=rr, column=1, value="Tabs").font = F(size=11, bold=True, color=NAVY); rr += 1
for t in ["Findings: every issue found, its impact and what was done.", "All checks: the full list of checks with live re-tests.",
          "Products: the independent rebuild per product next to the plan's numbers.", "Budget scenarios: plan vs history check vs today's pace, per product.",
          "Cross-source: SP spend per product, sales-tracking data vs ads console.", "Account history: fresh pulls for 2025 and 2026 (periods, BFCM 2025 by day, 2026 by week).",
          "Sources: every record used, its date, and how it was verified.", "Method: how the rebuild stays independent of the plan."]:
    c = sm.cell(row=rr, column=1, value="• " + t); sm.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=7); rr += 1

# ------------------------------------------------------------------ Findings
fd = wb.create_sheet("Findings", 1)
title(fd, "Findings", "Severity: High = changes money or a decision; Medium = a rule or list that would send the wrong instruction; Low = wording or a gap with no budget effect; Info = context for the reader.", "H")
FCOLS = [("#", 4), ("Severity", 9), ("Area", 16), ("Finding", 52), ("Evidence", 46), ("Impact", 34), ("Action", 40), ("Status", 10)]
header(fd, 4, FCOLS)
p_by = {(p["mkt"], p["name"]): p for p in R["products"]}
b4, b6 = p_by[("US", "Decolure Bamboo 4 Pc")], p_by[("US", "Decolure Bamboo 6 Pc")]
alt_us = sum(p["alt_budget"] for p in R["products"] if p["mkt"] == "US"); alt_ca = sum(p["alt_budget"] for p in R["products"] if p["mkt"] == "CA")
FIND = [
 ("High", "Demand read", "The demand read's base pace for the Bamboo heroes is well above what they sell today.",
  f"US Bamboo 4 Pc sells {b4['pace14_units_per_day']:.1f} units/day vs a 28-day pace of {b4['u28']/28:.1f} (0.51x); Bamboo 6 Pc {b6['pace14_units_per_day']:.1f} vs {b6['u28']/28:.1f} (0.62x). The 28-day window (to Oct 15) includes Prime Big Deal Days. 19 of 26 products sell outside 0.8-1.25x of the base pace.",
  f"Same TACoS plan at today's pace: US ${alt_us:,.0f}, CA C${alt_ca:,.0f} (vs ${US_T['budget']:,.0f} / C${CA_T['budget']:,.0f}). Spend self-corrects because the agent paces to TACoS on actual sales.",
  "Approve the history level (US $73K / C$20K) as the base and the plan as the ceiling. Refresh the demand read with the Nov 1-14 pace before Nov 19.", "Open: decision for Joseph"),
 ("Medium", "Rules tab", "US Satin 4 Pc was listed as a Best Deal hero 'with room under the cap' (+20% bids, top-of-search boost) while it runs over its cap.",
  "All-ad-type TACoS now 12.7% vs a 12% Maintenance cap.", "A +20% raise and top-of-search boost on a product already over its cap.",
  "Removed from the boost list; raise only once daily TACoS is under 12%. US Bamboo 6 Pc (19.3% vs 19.3% cap) moved to the same 'wait' rule.", "Fixed"),
 ("Low", "Rules tab", "The no-raise list was stale: it named Sleephoria Bamboo 6 Pc (now under its cap, raised to the growth floor) and missed US Satin 6 Pc, Sleephoria Cooling 4 Pc, Sleephoria Cooling Pillowcase, Decolure Cooling 4 Pc and Canadian Satin Fitted / Sleep Sanctuary Satin 4 Pc.",
  "Re-derived from TACoS now (14 days, all ad types) vs each product's cap.", "Agent could raise bids on products over their cap.", "List rebuilt from the data (12 products).", "Fixed"),
 ("Low", "Summary", "The Summary's 'over the cap today' list missed Canadian Satin 4 Pc, Satin 6 Pc, Satin Fitted, Sleep Sanctuary Satin 4 Pc and US Sleephoria Cooling Pillowcase / Cooling 4 Pc.",
  "Same re-derivation.", "Joseph would not see that Canada's Maintenance products all need cutting.", "Summary bullet rewritten with US and Canada lists.", "Fixed"),
 ("Low", "Coverage", "Decolure Hanging Closet Organizer has a Best Deal in the deal sheet but no line in the PPC plan.", "Deal sheet: Best Deal Nov 19-30. Ads console: $130 SP in 14 days (~$9/day).",
  "About $110 of spend over the 12 days sits outside the plan.", "Treat as Liquidation (judged on units). Add a line if Joseph wants it budgeted.", "Open: minor"),
 ("Info", "Cross-source", "The ads console reads about 9% less SP spend than the sales-tracking data (US 0.91x, CA 0.91x), consistently across products.",
  f"US: console ${CON['account']['US']:,.0f} vs ${SRC['now14']['US']['sp']:,.0f}. Per product the ratio sits at 0.80-1.05 for all big spenders.",
  "None: the plan uses one source for both spend and sales, and shares are unaffected.", "None.", "No action"),
 ("Info", "Stages", "The ads console now shows a 7-12% TACoS band on the three Liquidation products (Quilt Set, Linen Curtains, Chair Cover); the plan judges them on units with no band.",
  "Console portfolio view, Oct 19 - Nov 1.", "None: Quilt and Curtains are no-ads; Chair Cover's 7.5% plan sits inside 7-12%.", "None.", "No action"),
 ("Info", "Prices", "CooLinens Cooling Sheets, Bamboo Fitted and Decolure Cooling 4 Pc have no deal-sheet row, so their price comes from the tracker's listing price only.",
  "No second record available for these three prices.", "Budget for no-deal products is set from today's spend and sales pace, not price, so the effect is nil.", "None.", "No action"),
 ("Info", "Currency", "Canadian COGS in the deal sheet are in US$; the plan's x1.40 conversion is correct.", "508 of 553 Canadian SKUs carry exactly the US cost.", "Confirms the Canadian break-even.", "None.", "Verified"),
]
for i, f_ in enumerate(FIND, 1):
    rr = 4 + i
    for j, v in enumerate((i,) + f_, 1):
        c = fd.cell(row=rr, column=j, value=v); c.alignment = WRAP; c.border = BOX; c.font = F(bold=(j == 2))
    fd.row_dimensions[rr].height = 78
sev = f"B5:B{4+len(FIND)}"
fd.conditional_formatting.add(sev, CellIsRule(operator="equal", formula=['"High"'], fill=DFF))
fd.conditional_formatting.add(sev, CellIsRule(operator="equal", formula=['"Medium"'], fill=CHF))
fd.conditional_formatting.add(f"H5:H{4+len(FIND)}", CellIsRule(operator="equal", formula=['"Fixed"'], fill=OKF))
fd.freeze_panes = "D5"

# ------------------------------------------------------------------ Products
pr = wb.create_sheet("Products")
title(pr, "Independent rebuild per product, next to the plan", "Rebuilt columns are blue (values from the rebuild); Plan columns are green (values read from the delivered workbook); Gap columns are formulas.", "Z")
PCOLS = [("Market", 6), ("Product", 24), ("Stage", 11), ("Deal", 13), ("Units low", 8), ("Units high", 8), ("Avg price", 8), ("Expected sales (rebuilt)", 11),
         ("Break-even (rebuilt)", 8), ("Cap (rebuilt)", 8), ("TACoS now (rebuilt)", 8), ("Factor", 6), ("Plan TACoS (rebuilt)", 8), ("Budget (rebuilt)", 10),
         ("Budget (plan)", 10), ("Gap", 8), ("SP", 9), ("SB", 8), ("SB video", 8), ("SD", 7), ("Spend 14 d", 9), ("Sales 14 d", 10), ("Units/day 14 d", 8),
         ("Units/day demand read", 8), ("Pace ratio", 7), ("Plan check label", 26)]
header(pr, 4, PCOLS, 44)
plan_budget = {}
for x in R["checks"]:
    if x["item"] == "Ad budget Nov 19-30":
        plan_budget[(x["mkt"], x["product"])] = x["plan"]
rr = 5
for p in R["products"]:
    m = p["mkt"]
    vals = [m, p["name"], p["stage"], p["deal"] or "No deal", round(p["units_lo"]), round(p["units_hi"]), round(p["asp"], 2), round(p["sales"], 2),
            p["be"], p["cap"], p["now"], p["fac"], p["plan_t"], round(p["budget"], 2), plan_budget.get((m, p["name"])), f"=O{rr}-N{rr}",
            *[round(v, 2) for v in p["split"]], round(p["adv14"], 2), round(p["s14"], 2), round(p["pace14_units_per_day"] or 0, 2), round(p["u28"] / 28, 2),
            f"=IF(X{rr}>0,W{rr}/X{rr},\"\")", p["label"]]
    for j, v in enumerate(vals, 1):
        c = pr.cell(row=rr, column=j, value=v); c.border = BOX
        c.font = F(color=GREEN if j == 15 else (BLUE if j in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24) else "000000"))
        c.number_format = {7: CUR[m].replace('#,##0', '#,##0.00'), 8: CUR[m], 9: "0.0%", 10: "0.0%", 11: "0.0%", 12: "0.00", 13: "0.0%", 14: CUR[m], 15: CUR[m],
                           16: '#,##0.00;-#,##0.00;"0"', 17: CUR[m], 18: CUR[m], 19: CUR[m], 20: CUR[m], 21: CUR[m], 22: CUR[m], 23: "0.0", 24: "0.0", 25: '0.00"x"'}.get(j, "General")
        if j == 26: c.alignment = WRAP
    rr += 1
pr.conditional_formatting.add(f"Y5:Y{rr-1}", FormulaRule(formula=[f"AND(ISNUMBER(Y5),OR(Y5<0.8,Y5>1.25))"], fill=CHF))
for m in ("US", "CA"):
    pr.cell(row=rr, column=2, value=f"Total {m}").font = F(bold=True)
    for j in (8, 14, 15, 17, 18, 19, 20, 21, 22):
        c = pr.cell(row=rr, column=j, value=f'=SUMIF($A$5:$A${rr-1 if m=="US" else rr-2},"{m}",{CL(j)}$5:{CL(j)}${rr-1 if m=="US" else rr-2})')
        c.number_format = CUR[m]; c.font = F(bold=True); c.fill = YEL; c.border = BOX
    pr.cell(row=rr, column=16, value=f"=O{rr}-N{rr}").number_format = '#,##0.00;-#,##0.00;"0"'
    rr += 1
pr.freeze_panes = "C5"

# ------------------------------------------------------------------ Budget scenarios
bs = wb.create_sheet("Budget scenarios")
title(bs, "Three ways to size the budget", "Plan = TACoS plan x the demand read's expected sales (no-deal products: today's spend at today's pace, capped). Today's pace = the same plan TACoS x (last-14-day units/day x BFCM lift x 12 x avg price). "
      "History check A = today's account spend x how much spend rose in BFCM 2025 (account level). Change the yellow cell to test another lift on today's pace.", "J")
bs["A3"] = "Lift multiplier applied to today's pace (1.00 = as rebuilt):"; bs["A3"].font = F(bold=True); bs["E3"] = 1.0; bs["E3"].font = F(bold=True, color=BLUE); bs["E3"].fill = YEL
BCOLS = [("Market", 7), ("Product", 26), ("Plan TACoS", 9), ("Expected sales: demand read", 12), ("Budget: plan", 11), ("Sales at today's pace", 12), ("Budget at today's pace", 11), ("Difference", 11), ("Deal", 13)]
header(bs, 5, BCOLS, 36)
rr = 6
for p in R["products"]:
    m = p["mkt"]
    vals = [m, p["name"], p["plan_t"], round(p["sales"], 2), (f"=C{rr}*D{rr}" if p["deal"] else round(p["budget"], 2)), round(p["alt_sales"], 2), (f"=C{rr}*F{rr}*$E$3" if p["deal"] else f"=E{rr}"), f"=G{rr}-E{rr}", p["deal"] or "No deal (holds today's spend)"]
    for j, v in enumerate(vals, 1):
        c = bs.cell(row=rr, column=j, value=v); c.border = BOX; c.font = F(color=BLUE if j in (3, 4, 6) else "000000")
        c.number_format = {3: "0.0%", 4: CUR[m], 5: CUR[m], 6: CUR[m], 7: CUR[m], 8: '#,##0;(#,##0);"-"'}.get(j, "General")
    rr += 1
last = rr - 1
for m in ("US", "CA"):
    bs.cell(row=rr, column=2, value=f"Total {m}").font = F(bold=True)
    for j in (4, 5, 6, 7, 8):
        c = bs.cell(row=rr, column=j, value=f'=SUMIF($A$6:$A${last},"{m}",{CL(j)}$6:{CL(j)}${last})'); c.number_format = CUR[m]; c.font = F(bold=True); c.fill = YEL; c.border = BOX
    rr += 1
rr += 1
bs.cell(row=rr, column=1, value="Account-level history check (from the 2025 vs 2026 check tab of the plan, recomputed from fresh pulls)").font = F(bold=True, color=NAVY); rr += 1
hA = {x["mkt"]: x["source"] for x in R["checks"] if x["item"].startswith("History check A")}
hB = {x["mkt"]: x["source"] for x in R["checks"] if x["item"].startswith("History check B")}
for lab, d in (("History check A: raise today's spend like BFCM 2025", hA), ("History check B: demand read at 2025's TACoS drop", hB)):
    bs.cell(row=rr, column=2, value=lab)
    for j, m in ((5, "US"), (7, "CA")):
        c = bs.cell(row=rr, column=j, value=round(d[m], 2)); c.number_format = CUR[m]; c.font = F(color=BLUE)
    bs.cell(row=rr, column=4, value="US"); bs.cell(row=rr, column=6, value="CA"); rr += 1

# ------------------------------------------------------------------ Cross-source
cs = wb.create_sheet("Cross-source")
title(cs, "SP spend per product, Oct 19 - Nov 1: sales-tracking data vs the ads console",
      "Two independent records of the same spend. The console reads about 9% lower across the board (7-day attribution still filling in; some campaign types excluded). What matters is that the ratio is steady product to product.", "F")
header(cs, 4, [("Market", 7), ("Product", 28), ("Sales-tracking SP", 13), ("Ads console SP", 13), ("Console / tracking", 11), ("Status", 9)])
rr = 5
for p in R["products"]:
    if p["console_sp"] is None and p["a14"][0] < 10:
        continue
    m = p["mkt"]
    for j, v in enumerate([m, p["name"], round(p["a14"][0], 2), p["console_sp"], f"=IF(AND(C{rr}>0,ISNUMBER(D{rr})),D{rr}/C{rr},\"\")",
                           f"=IF(E{rr}=\"\",\"n/a\",IF(AND(E{rr}>=0.8,E{rr}<=1.05),\"OK\",\"CHECK\"))"], 1):
        c = cs.cell(row=rr, column=j, value=v); c.border = BOX; c.font = F(color=BLUE if j in (3, 4) else "000000")
        c.number_format = {3: CUR[m], 4: CUR[m], 5: '0.00"x"'}.get(j, "General")
    rr += 1
status_fmt(cs, f"F5:F{rr-1}")
for m in ("US", "CA"):
    cs.cell(row=rr, column=2, value=f"Whole account {m}").font = F(bold=True)
    c = cs.cell(row=rr, column=3, value=round(SRC["now14"][m]["sp"] * (1.4036 if m == "CA" else 1), 2)); c.number_format = CUR[m]; c.font = F(color=BLUE)
    c = cs.cell(row=rr, column=4, value=CON["account"][m]); c.number_format = CUR[m]; c.font = F(color=BLUE)
    cs.cell(row=rr, column=5, value=f"=D{rr}/C{rr}").number_format = '0.00"x"'
    for j in range(1, 7): cs.cell(row=rr, column=j).fill = YEL; cs.cell(row=rr, column=j).border = BOX
    rr += 1

# ------------------------------------------------------------------ Account history
ah = wb.create_sheet("Account history")
title(ah, "Fresh account pulls (Nov 2, 2026), all ad types", "Canada amounts are recorded in US$. TACoS and per-day figures are formulas.", "N")
header(ah, 4, [("Period", 30), ("Market", 7), ("Days", 6), ("Sales", 12), ("Ad spend", 11), ("Sessions", 10), ("Units", 8), ("Sales/day", 10), ("Spend/day", 10), ("TACoS", 8)])
rr = 5
PER = [("2025: 30 days before BFCM (Oct 21 - Nov 19)", "pre2025_30d", 30), ("2025: BFCM (Nov 20 - Dec 1)", "bfcm2025_total", 12), ("2026: last 14 days (Oct 19 - Nov 1)", "now14", 14)]
for lab, k, d in PER:
    for m in ("US", "CA"):
        x = SRC[k][m]
        for j, v in enumerate([lab, m, d, x["sales"], x["adv"], x["sessions"], x["units"], f"=D{rr}/C{rr}", f"=E{rr}/C{rr}", f"=E{rr}/D{rr}"], 1):
            c = ah.cell(row=rr, column=j, value=v); c.border = BOX; c.font = F(color=BLUE if j in (4, 5, 6, 7) else "000000")
            c.number_format = {4: '"$"#,##0', 5: '"$"#,##0', 6: "#,##0", 7: "#,##0", 8: '"$"#,##0', 9: '"$"#,##0', 10: "0.0%"}.get(j, "General")
        rr += 1
rr += 1
ah.cell(row=rr, column=1, value="BFCM 2025 by day").font = F(size=11, bold=True, color=NAVY); rr += 1
days = SRC["daily_bfcm2025"]["days"]
header(ah, rr, [("Metric", None), ("Market", None)] + [(d_[5:], None) for d_ in days] + [("Total", None)], 22)
for j in range(3, 16): ah.column_dimensions[CL(j)].width = max(ah.column_dimensions[CL(j)].width or 0, 10)
rr += 1
for m in ("US", "CA"):
    for k in ("sales", "adv", "units", "sessions"):
        ah.cell(row=rr, column=1, value=k); ah.cell(row=rr, column=2, value=m)
        for i, v in enumerate(SRC["daily_bfcm2025"][m][k]):
            c = ah.cell(row=rr, column=3 + i, value=v); c.font = F(color=BLUE); c.number_format = "#,##0"; c.border = BOX
        c = ah.cell(row=rr, column=15, value=f"=SUM(C{rr}:N{rr})"); c.number_format = "#,##0"; c.font = F(bold=True); c.border = BOX
        rr += 1
rr += 1
ah.cell(row=rr, column=1, value="2026 by week (ad types)").font = F(size=11, bold=True, color=NAVY); rr += 1
W = SRC["weekly2026"]
header(ah, rr, [("Metric", None), ("Market", None)] + [(w, None) for w in W["weeks"]], 22); rr += 1
for m in ("US", "CA"):
    for k in ("sp", "sb", "sbv", "sd", "sales"):
        ah.cell(row=rr, column=1, value=k); ah.cell(row=rr, column=2, value=m)
        for i, v in enumerate(W[m][k]):
            c = ah.cell(row=rr, column=3 + i, value=v); c.font = F(color=BLUE); c.number_format = "#,##0"; c.border = BOX
        rr += 1
    ah.cell(row=rr, column=1, value="share not SP"); ah.cell(row=rr, column=2, value=m)
    for i in range(6):
        col = CL(3 + i); c = ah.cell(row=rr, column=3 + i, value=f"=1-{col}{rr-5}/SUM({col}{rr-5}:{col}{rr-2})"); c.number_format = "0.0%"; c.border = BOX
    rr += 1
ah.freeze_panes = "C5"

# ------------------------------------------------------------------ Sources
so = wb.create_sheet("Sources")
title(so, "Records used and how each was verified", None)
header(so, 3, [("Record", 34), ("Date / window", 20), ("Used for", 40), ("How it was verified", 60)])
SRCS = [
 ("Account pulls, fresh (all ad types, sessions, units)", "Pulled Nov 2, 2026", "2025 lift, deal-period factor, day weights, history checks, account TACoS", "BFCM 2025 daily figures add up to the period total to the cent; matched to the plan's inputs line by line."),
 ("2025 product-level sales files (30 days before, BFCM)", "Oct 21 - Nov 19 and Nov 20 - Dec 1, 2025", "Each product's own 2025 lift and 2025 TACoS", "File totals = fresh account totals (sales exact; ad spend within 0.4%). Row ownership re-implemented: child ASIN, current Amazon parent, older parent, documented name list."),
 ("Child-ASIN rows, 14 days, by ad type", "Oct 19 - Nov 1, 2026", "TACoS now (all ad types), SP share, budget split, today's unit pace", "Re-aggregated from the raw pulls (not the saved CSV); 99% of ad spend and about 95% of sales captured; mapped to products from the SKU lists."),
 ("Ads console: SP spend per product", "Oct 19 - Nov 1, 2026", "Second source for per-product spend", "Ratio to sales-tracking SP is 0.80-1.05 for every product above $100 spend."),
 ("Ads console: growth stage and TACoS band per product", "Pulled Nov 2, 2026", "Band floors and ceilings", "All 22 banded products match; 3 Liquidation products differ with no budget effect."),
 ("Deal sheet export", "Oct 27, 2026", "Deal prices, deal types and dates, COGS, FBA fee, referral %", "Lightning Deal dates match the plan's 4x day; Canadian COGS confirmed in US$; every deal product checked for a budget line."),
 ("SKU lists per product (with 28-day units)", "Oct 14, 2026", "Variation membership, 28-day units, demand weights", "Units and weights match the plan for all 25 products; Satin 4 Pc Twin rule applied (counted under Satin 6 Pc)."),
 ("Inventory export (sales velocity)", "Oct 15, 2026", "Demand read high case", "Velocity matches the plan for all products (catalog-only children included)."),
 ("Product catalog (parent / child ASINs)", "Oct 2026", "Current Amazon parent of each product", "Used to map 2025 rows; results match the plan's 2025 TACoS for every product."),
]
for i, s_ in enumerate(SRCS):
    for j, v in enumerate(s_, 1):
        c = so.cell(row=4 + i, column=j, value=v); c.alignment = WRAP; c.border = BOX; c.font = F(bold=(j == 1))
    so.row_dimensions[4 + i].height = 40

# ------------------------------------------------------------------ Method
me = wb.create_sheet("Method")
title(me, "How the rebuild stays independent", None)
ME = ["New code (verification/verify.py) reads the original records directly. It does not import or call the plan's scripts (compute_plan.py, build_ppc_plan.py) or the tracker's builder.",
      "Formulas were re-implemented from the plan's written method: break-even = (price - COGS - FBA - referral - 1% deal fee - $70 per deal) / price; cap = lower of 80% of break-even and the growth-band ceiling; base = TACoS now x deal-period factor; plan = min(cap, max(base, band floor x factor)); no-deal products hold today's spend at today's pace, cut to the cap.",
      "Account figures were pulled fresh on Nov 2 rather than read from files saved earlier; per-product spend was compared with a second, separate record (the ads console).",
      "The delivered workbook was recalculated and read cell by cell; every comparison carries its tolerance, and the All checks tab re-runs the tolerance test with live formulas.",
      "Business rules that are decisions rather than data (Satin 4 Pc Twin counted under Satin 6 Pc; the name list for re-parented 2025 listings; Liquidation judged on units) were applied as documented and are listed here so they can be challenged.",
      "Limits: the deal sheet, SKU lists and inventory export have no second record, so they are checked for internal consistency (currency, dates, membership) rather than against another system. Three no-deal prices come from the tracker's listing price only."]
for i, t in enumerate(ME):
    c = me.cell(row=3 + i, column=1, value=f"{i+1}. {t}"); c.alignment = WRAP; me.merge_cells(start_row=3 + i, start_column=1, end_row=3 + i, end_column=8); me.row_dimensions[3 + i].height = 44
me.column_dimensions["A"].width = 20
for k in range(2, 9): me.column_dimensions[CL(k)].width = 16

wb.move_sheet("All checks", offset=wb.sheetnames.index("Method") - wb.sheetnames.index("All checks"))
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if c.font is None or c.font.name != "Arial":
                c.font = Font(name="Arial", size=c.font.size or 9, bold=c.font.bold, italic=c.font.italic, color=c.font.color)
wb.save(OUT); print("saved", OUT, "checks", len(R["checks"]))
