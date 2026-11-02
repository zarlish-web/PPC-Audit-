"""Builds BFCM_2026_PPC_Plan.xlsx from plan_numbers.json + inputs_2026-11-02.json. Usage: python3 build_ppc_plan.py OUT.xlsx"""
import json, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.comments import Comment
HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "plan_numbers.json"))); I = json.load(open(os.path.join(HERE, "inputs_2026-11-02.json")))
OUT = sys.argv[1]
NAVY, BLUE = "1F3864", "0000FF"
F = lambda **k: Font(name="Arial", size=k.pop("size", 9), **k)
HDR = PatternFill("solid", fgColor=NAVY); YEL = PatternFill("solid", fgColor="FFF2CC"); GRN = PatternFill("solid", fgColor="E2EFDA"); RED = PatternFill("solid", fgColor="FCE4D6")
BOX = Border(*(Side(style="thin", color="BFBFBF"),) * 4); WRAP = Alignment(wrap_text=True, vertical="top"); CEN = Alignment(horizontal="center", vertical="center", wrap_text=True)
CUR = {"US": '"$"#,##0', "CA": '"C$"#,##0'}; CUR2 = {"US": '"$"#,##0.00', "CA": '"C$"#,##0.00'}
NAMES = {"DC B4": "Decolure Bamboo 4 Pc", "DC B6": "Decolure Bamboo 6 Pc", "DC S4": "Decolure Satin 4 Pc", "DC S6": "Decolure Satin 6 Pc",
         "SSS4": "Sleep Sanctuary Satin 4 Pc", "DC Satin Fitted": "Decolure Satin Fitted", "DC Silk Pillowcase": "Decolure Silk Pillowcase",
         "CL Pillowcases": "CooLinens Pillowcases", "SL Cooling 4pc": "Sleephoria Cooling 4 Pc", "SL Cooling Fitted": "Sleephoria Cooling Fitted",
         "SL Cooling Comforter": "Sleephoria Cooling Comforter", "SL Cooling Pillowcase": "Sleephoria Cooling Pillowcase", "SL B6": "Sleephoria Bamboo 6 Pc",
         "SL Quilt Set": "Sleephoria Quilt Set", "DC Linen Curtains": "Decolure Linen Curtains", "DC Chair Cover": "Decolure Chair Cover",
         "DC Bamboo Fitted": "Decolure Bamboo Fitted", "DC Cooling 4pc": "Decolure Cooling 4 Pc", "CL Cooling Sheets": "CooLinens Cooling Sheets"}
MKT_FACTOR = {"US": 0.58, "CA": 0.68}; MKT_BF = {"US": 0.0817, "CA": 0.088}
DAYS = ["Thu Nov 19", "Fri Nov 20", "Sat Nov 21", "Sun Nov 22", "Mon Nov 23", "Tue Nov 24", "Wed Nov 25", "Thu Nov 26", "Fri Nov 27 (BF)", "Sat Nov 28", "Sun Nov 29", "Mon Nov 30 (CM)"]
LD_DAY = {"DC S6": 4, "DC Silk Pillowcase": 4, "SL Cooling Fitted": 6}   # index into DAYS: Nov 23, Nov 23, Nov 25
NOTE = {"DC B4": "Hero. Room under the ceiling: full BFCM push.", "DC B6": "Hero. Deal is 6.5% cheaper than 2025: plan near the high end.",
        "DC S4": "Hero. Deal 2.6% cheaper than 2025: plan near the high end.", "SSS4": "Running at 25% TACoS today, above its 21% ceiling: cut to the ceiling before Nov 19.",
        "DC S6": "Lightning Deal Nov 23 only (Best Deal requested). Budget weighted to Nov 23.", "DC Satin Fitted": "Deal 34% above 2025 paid; plan near the low end.",
        "DC Silk Pillowcase": "Lightning Deal Nov 23. TACoS 28% today, ceiling 27%.", "CL Pillowcases": "TACoS 43% today vs 14% ceiling at the $15.19 deal: cut hard. Queen White runs out ~Nov 6.",
        "SL Cooling 4pc": "TACoS 20% today; deal 16% above 2025 paid.", "SL Cooling Fitted": "Lightning Deal Nov 25. Budget weighted to Nov 25.",
        "SL Cooling Comforter": "Deal 47% above 2025 paid; low end.", "SL Cooling Pillowcase": "Small; keep to the ceiling.",
        "SL B6": "Thin margin at deal (16% break-even).", "SL Quilt Set": "Break-even about 1% at the deal price: no ads beyond brand defence.",
        "DC Linen Curtains": "Loses money per unit at the deal price before ads: no ads.", "DC Chair Cover": "Small; keep to the ceiling.",
        "DC Bamboo Fitted": "No deal: hold at today's daily spend.", "DC Cooling 4pc": "No deal: hold at today's daily spend, under break-even.",
        "CL Cooling Sheets": "No deal: hold at today's daily spend (no BFCM increase)."}
wb = Workbook()
# ---------------- Budget by product
bp = wb.active; bp.title = "Budget by product"; bp.sheet_view.showGridLines = False
bp["A1"] = "BFCM 2026 PPC plan: budget and TACoS ceiling by product, Nov 19 - 30"; bp["A1"].font = F(size=13, bold=True, color=NAVY)
bp["A2"] = ("Units = the demand read (low = last-28-day pace x own 2025 BFCM lift x 12 days; high = current pace x lift x 12). Avg selling price = deal price "
            "(weighted by each variation's 28-day units) for Best Deals; 1 deal day + 11 regular days for Lightning Deals. Break-even TACoS = (price - COGS - FBA - referral "
            "- 1.5% deal fee - $100 flat deal fee) / price. Ceiling = 80% of break-even. Plan TACoS = today's 30-day TACoS x the deal-period factor (how far TACoS fell "
            "during BFCM 2025 vs the 30 days before), never above the ceiling. Products with no deal hold today's daily spend. Blue = inputs, black = formulas.")
bp["A2"].font = F(italic=True, size=8.5); bp["A2"].alignment = WRAP; bp.merge_cells("A2:T2"); bp.row_dimensions[2].height = 62
bp["A3"] = "Ceiling as share of break-even:"; bp["A3"].font = F(bold=True); bp["D3"] = 0.80; bp["D3"].number_format = "0%"; bp["D3"].font = F(bold=True, color=BLUE); bp["D3"].fill = YEL
bp["F3"] = "No-ads threshold (break-even TACoS at or below):"; bp["F3"].font = F(bold=True); bp["J3"] = 0.05; bp["J3"].number_format = "0%"; bp["J3"].font = F(bold=True, color=BLUE); bp["J3"].fill = YEL
COLS = [("Product", 24), ("BFCM 2026 deal", 18), ("Units low", 8), ("Units high", 8), ("Units plan (mid)", 8), ("Avg selling price", 9), ("Expected sales, 12 days", 11),
        ("Break-even TACoS at deal price", 9), ("TACoS ceiling", 8), ("TACoS now (30 days)", 8), ("Deal-period factor (2025 BFCM vs before)", 9),
        ("2025 BFCM TACoS (fallback)", 8), ("Plan TACoS", 8), ("Ad budget Nov 19-30", 10), ("Budget at low units", 10), ("Budget at high units", 10),
        ("Budget per day (avg)", 9), ("Ad spend per day now (30 days)", 9), ("Per-day change vs now", 8), ("Note", 46)]
for j, (h, w) in enumerate(COLS, 1):
    bp.column_dimensions[CL(j)].width = w
row = 5; blocks = {}
for m in ("US", "CA"):
    bp.cell(row=row, column=1, value=("United States (US$)" if m == "US" else "Canada (C$)")).font = F(size=11, bold=True, color=NAVY); row += 1
    for j, (h, w) in enumerate(COLS, 1):
        c = bp.cell(row=row, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX
    bp.row_dimensions[row].height = 46; row += 1; r0 = row
    rows = sorted([r for r in P if r["mkt"] == m], key=lambda r: -(r["sales_plan"] or 0))
    for r in rows:
        fac = None
        if r["tacos25_pre"] and r["tacos25_bf"] and r["tacos25_pre"] > 0.01 and r["tacos25_bf"] > 0.01:
            fac = max(0.3, min(1.2, r["tacos25_bf"] / r["tacos25_pre"]))
        fac = round(fac if fac is not None else MKT_FACTOR[m], 2)
        fb = r["tacos25_bf"] if (r["tacos25_bf"] or 0) > 0.01 else MKT_BF[m]
        deal = f"{r['deal_type']} {r['deal_dates']}" if r["deal_type"] else "No deal"
        vals = [NAMES.get(r["short"], r["short"]), deal, round(r["units_lo"]), round(r["units_hi"]), f"=AVERAGE(C{row}:D{row})", round(r["asp"], 2), f"=E{row}*F{row}",
                round(r["be_tacos"], 4) if r["be_tacos"] is not None else None, f'=IF(H{row}="","",MAX(0,H{row}*$D$3))',
                round(r["tacos30"], 4) if r["tacos30"] is not None else None, fac, round(fb, 4),
                (f'=IF(G{row}>0,MIN(R{row}*12,IF(I{row}="",R{row}*12,G{row}*I{row}))/G{row},0)' if not r["deal_type"] else
                 f'=IF(OR(H{row}="",H{row}<=$J$3),0,MIN(I{row},IF(J{row}<>"",J{row}*K{row},L{row})))'), f"=G{row}*M{row}", f"=C{row}*F{row}*M{row}", f"=D{row}*F{row}*M{row}",
                f"=N{row}/12", round((r["spend30"] or 0) / 30, 2), f'=IF(R{row}>0,Q{row}/R{row}-1,"")', NOTE.get(r["short"], "")]
        for j, v in enumerate(vals, 1):
            c = bp.cell(row=row, column=j, value=v); c.border = BOX; c.font = F(color=(BLUE if j in (3, 4, 6, 8, 10, 11, 12, 18) else "000000"))
            c.number_format = {3: "#,##0", 4: "#,##0", 5: "#,##0", 6: CUR2[m], 7: CUR[m], 8: "0.0%", 9: "0.0%", 10: "0.0%", 11: "0.00", 12: "0.0%", 13: "0.0%",
                               14: CUR[m], 15: CUR[m], 16: CUR[m], 17: CUR[m], 18: CUR[m], 19: "+0%;-0%;0%"}.get(j, "General")
            if j in (2, 20): c.alignment = WRAP
        bp.cell(row=row, column=14).font = F(bold=True); bp.cell(row=row, column=13).fill = GRN
        row += 1
    r1 = row - 1
    tot = ["Total", "", f"=SUM(C{r0}:C{r1})", f"=SUM(D{r0}:D{r1})", f"=SUM(E{r0}:E{r1})", "", f"=SUM(G{r0}:G{r1})", "", "", "", "", "", f"=N{row}/G{row}",
           f"=SUM(N{r0}:N{r1})", f"=SUM(O{r0}:O{r1})", f"=SUM(P{r0}:P{r1})", f"=N{row}/12", f"=SUM(R{r0}:R{r1})", f"=Q{row}/R{row}-1", ""]
    for j, v in enumerate(tot, 1):
        c = bp.cell(row=row, column=j, value=v); c.font = F(bold=True); c.border = BOX; c.fill = YEL
        c.number_format = {3: "#,##0", 4: "#,##0", 5: "#,##0", 7: CUR[m], 13: "0.0%", 14: CUR[m], 15: CUR[m], 16: CUR[m], 17: CUR[m], 18: CUR[m], 19: "+0%;-0%;0%"}.get(j, "General")
    blocks[m] = (r0, r1, row, rows); row += 3
bp.freeze_panes = "B5"
# ---------------- Budget by day
bd = wb.create_sheet("Budget by day"); bd.sheet_view.showGridLines = False
bd["A1"] = "BFCM 2026 PPC budget by day (follows how sales were spread over the 12 days of BFCM 2025)"; bd["A1"].font = F(size=13, bold=True, color=NAVY)
bd["A2"] = ("Day weights = each day's share of BFCM 2025 sales (Nov 20 - Dec 1, 2025; the days line up by weekday: Black Friday and Cyber Monday are day 9 and day 12 both years). "
            "Lightning Deal products put 4x the normal weight on their deal day. Each product's day = its budget x the day weight.")
bd["A2"].font = F(italic=True, size=8.5); bd["A2"].alignment = WRAP; bd.merge_cells("A2:O2"); bd.row_dimensions[2].height = 34
bd.column_dimensions["A"].width = 28; bd.column_dimensions["B"].width = 11
for k in range(12): bd.column_dimensions[CL(3 + k)].width = 10
bd.column_dimensions[CL(15)].width = 11
row = 4
for m in ("US", "CA"):
    r0, r1, rt, rows = blocks[m]
    s25 = I["daily2025"][m]["sales" if m == "US" else "sales_usd"]
    bd.cell(row=row, column=1, value=("United States (US$)" if m == "US" else "Canada (C$)")).font = F(size=11, bold=True, color=NAVY); row += 1
    hdr = ["", "Total"] + DAYS + ["Check"]
    for j, h in enumerate(hdr, 1):
        c = bd.cell(row=row, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX
    bd.row_dimensions[row].height = 30; row += 1
    srow = row; bd.cell(row=row, column=1, value=f"BFCM 2025 sales that day ({'US$' if m == 'US' else 'US$, CA'})").font = F(italic=True)
    for k, v in enumerate(s25):
        c = bd.cell(row=row, column=3 + k, value=round(v, 2)); c.font = F(color=BLUE); c.number_format = '"$"#,##0'; c.border = BOX
    c = bd.cell(row=row, column=2, value=f"=SUM(C{row}:N{row})"); c.number_format = '"$"#,##0'; c.border = BOX; row += 1
    wrow = row; bd.cell(row=row, column=1, value="Day weight (share of the 12 days)").font = F(bold=True)
    for k in range(12):
        c = bd.cell(row=row, column=3 + k, value=f"={CL(3+k)}{srow}/$B${srow}"); c.number_format = "0.0%"; c.border = BOX; c.font = F(bold=True)
    c = bd.cell(row=row, column=2, value=f"=SUM(C{row}:N{row})"); c.number_format = "0%"; c.border = BOX; row += 1
    pr0 = row
    for i, r in enumerate(rows):
        br = r0 + i
        bd.cell(row=row, column=1, value=f"='Budget by product'!A{br}").border = BOX
        c = bd.cell(row=row, column=2, value=f"='Budget by product'!N{br}"); c.number_format = CUR[m]; c.border = BOX; c.font = F(bold=True)
        ld = LD_DAY.get(r["short"]) if r["ld"] else None
        for k in range(12):
            col = CL(3 + k); wl = f"{CL(3+ld)}${wrow}" if ld is not None else None
            f = (f"=$B{row}*{col}${wrow}*{4 if k == ld else 1}/(1+3*{wl})" if ld is not None else f"=$B{row}*{col}${wrow}")
            c = bd.cell(row=row, column=3 + k, value=f); c.number_format = CUR[m]; c.border = BOX
            if k in (8, 11) or k == ld: c.fill = YEL
        c = bd.cell(row=row, column=15, value=f"=SUM(C{row}:N{row})-B{row}"); c.number_format = '0;-0;"ok"'; c.border = BOX
        row += 1
    bd.cell(row=row, column=1, value="Total").font = F(bold=True)
    for k in range(13):
        col = CL(2 + k); c = bd.cell(row=row, column=2 + k, value=f"=SUM({col}{pr0}:{col}{row-1})"); c.number_format = CUR[m]; c.font = F(bold=True); c.fill = YEL; c.border = BOX
    row += 3
bd.freeze_panes = "C4"
# ---------------- Rules
ru = wb.create_sheet("Bid and placement rules"); ru.sheet_view.showGridLines = False
ru.column_dimensions["A"].width = 6; ru.column_dimensions["B"].width = 34; ru.column_dimensions["C"].width = 80; ru.column_dimensions["D"].width = 30
ru["A1"] = "Deal-day bid and top-of-search rules"; ru["A1"].font = F(size=13, bold=True, color=NAVY)
RULES = [
 ("Bids", "Deal start (Nov 19, when the deal goes live)", "Best Deal heroes with room under the ceiling (Bamboo 4 Pc, Bamboo 6 Pc, Satin 4 Pc, Satin Fitted): +20% on exact-match keywords that converted in the last 30 days. Products already at or over the ceiling (Sleep Sanctuary Satin 4 Pc, CooLinens Pillowcases, Silk Pillowcase): no raise; bring them down to the ceiling first.", "The deal price lifts conversion, so the same bid buys more sales."),
 ("Bids", "Black Friday (Nov 27) and Cyber Monday (Nov 30)", "+30% on the top 10 converting keywords per hero product, 6 AM - 11 PM ET. Back to deal-start bids the next morning.", "In 2025 these two days were 31% of BFCM sales at the lowest TACoS of the event (6-7%)."),
 ("Bids", "Lightning Deal day (Satin 6 Pc and Silk Nov 23, Sleephoria Cooling Fitted Nov 25)", "+50% bids and 4x the normal day budget for the deal hours only; back to normal when the deal ends.", "One day of deal traffic; outside it they sell at the regular price."),
 ("Bids", "Wasted clicks", "Any search term with 15+ clicks and 0 orders during the event: negate. Any keyword with 20+ clicks and 0 orders: -50% bid; 40+ clicks: pause.", ""),
 ("Bids", "Keyword over break-even", "Keyword ACoS above the product's break-even for 2 days running (10+ clicks): -20% bid. Product TACoS for the day above its ceiling: -15% on all non-hero keywords and remove any top-of-search boost until it is back under.", ""),
 ("Bids", "Out of stock", "A variation out of stock or under 1 day of cover: stop ads on that ASIN within the hour. If the hero variation goes out, move its keywords to the next best in-stock variation.", "Spend on an unbuyable ASIN is lost."),
 ("Bids", "No-deal products", "CooLinens Cooling Sheets, Decolure Cooling 4 Pc, Bamboo Fitted: no BFCM increase. Hold at today's daily spend or lower, under break-even.", "Without a deal they don't get the deal lift."),
 ("Bids", "No-ads products", "Linen Curtains and Quilt Set lose money (or earn about 1%) per unit at the deal price before any ads: brand-defence only, no prospecting.", ""),
 ("Top of search", "Who gets a boost", "Only Best Deal heroes with room under the ceiling: Bamboo 4 Pc, Bamboo 6 Pc, Satin 4 Pc, Satin Fitted (US); Bamboo 4 Pc, Bamboo 6 Pc, Satin 4 Pc (CA).", "Top of search converts best when the deal badge shows."),
 ("Top of search", "How much", "Top-of-search modifier +50% Nov 19 - 26 and Nov 28 - 29; +100% on Nov 27 and Nov 30; back to today's setting on Dec 1.", ""),
 ("Top of search", "Cap", "Bamboo 4 Pc already puts 40-75% of its spend on top of search at an effective bid of about $3-6 a click (vs about $1.50 on product pages). Cap the effective top-of-search bid at $6.50 on Bamboo 4 Pc and 6 Pc; if top-of-search ACoS for the day is above break-even ACoS, cut the modifier by 25 points.", "Stops the boost from buying unprofitable clicks."),
 ("Top of search", "Product pages", "Keep product-targeting ads on our own listings at today's bids to hold deal traffic on our pages; no boost.", ""),
]
ru.append([]); hr = 3
for j, h in enumerate(["Area", "Rule", "What to do", "Why"], 1):
    c = ru.cell(row=hr, column=j, value=h); c.font = F(bold=True, color="FFFFFF"); c.fill = HDR; c.border = BOX
for i, (a, b, cc, d) in enumerate(RULES, hr + 1):
    for j, v in enumerate((a, b, cc, d), 1):
        c = ru.cell(row=i, column=j, value=v); c.alignment = WRAP; c.border = BOX; c.font = F(bold=(j == 2))
r = hr + len(RULES) + 3
ru.cell(row=r, column=1, value="What the agent does every hour, and what a person checks").font = F(size=13, bold=True, color=NAVY); r += 1
for j, h in enumerate(["Who", "When", "What", "Escalate if"], 1):
    c = ru.cell(row=r, column=j, value=h); c.font = F(bold=True, color="FFFFFF"); c.fill = HDR; c.border = BOX
AG = [
 ("Agent", "Every hour", "Pace: spend so far vs the day's budget for each product. Over 120% of pace: -10% on the lowest-return keywords. Under 70% of pace and the product is under its ceiling: +10% on the top converters.", "A product reaches its day budget before 6 PM ET"),
 ("Agent", "Every hour", "TACoS check: today's TACoS for each product vs its ceiling. Over the ceiling: -15% on non-hero keywords and remove the top-of-search boost.", "Over the ceiling 3 hours running"),
 ("Agent", "Every hour", "Stock: stop ads on any ASIN out of stock or under 1 day of cover; move hero keywords to the backup variation.", "A hero variation goes out of stock"),
 ("Agent", "Every hour", "Deal status: if a deal is suppressed, ended early or the deal price changed, put bids back to pre-deal levels on that product.", "Always (deal problems go to the deal desk)"),
 ("Agent", "Every hour", "Waste: negate search terms with 15+ clicks and 0 orders; apply the keyword rules on the Rules list.", ""),
 ("Agent", "Every hour", "Log every change (product, keyword, old bid, new bid, reason) so the person can undo it.", ""),
 ("Person (PPC owner)", "9 AM, 3 PM and 9 PM ET daily", "Spend vs budget and TACoS vs ceiling per product; read the agent's log; approve any day budget raise over 25% of plan; approve stopping ads on a hero product.", ""),
 ("Person (PPC owner)", "Nov 27 and Nov 30", "Hourly war-room review: top keywords, top-of-search share, stock, Buy Box.", ""),
 ("Person (PPC owner)", "End of each day", "Post a 5-line summary in the BFCM thread: spend, sales, TACoS vs plan, changes made, decisions needed.", ""),
 ("Person (Joseph)", "When escalated", "Moves budget between products (e.g. from an out-of-stock product to one with room), and signs off any change to a ceiling.", ""),
]
for i, row_ in enumerate(AG, r + 1):
    for j, v in enumerate(row_, 1):
        c = ru.cell(row=i, column=j, value=v); c.alignment = WRAP; c.border = BOX; c.font = F(bold=(j == 1))
# ---------------- Inputs
ip = wb.create_sheet("Inputs"); ip.sheet_view.showGridLines = False
ip["A1"] = "Inputs and sources"; ip["A1"].font = F(size=13, bold=True, color=NAVY)
ip.column_dimensions["A"].width = 26
for k in range(2, 16): ip.column_dimensions[CL(k)].width = 11
r = 3
ip.cell(row=r, column=1, value="BFCM 2025 by day (US$; Canada sales are recorded in US$)").font = F(bold=True, color=NAVY); r += 1
for j, h in enumerate(["", "Total"] + I["daily2025"]["US"]["days"], 1):
    c = ip.cell(row=r, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN
r += 1
for lab, arr in (("US sales", I["daily2025"]["US"]["sales"]), ("US ad spend", I["daily2025"]["US"]["ad"]), ("US units", I["daily2025"]["US"]["units"]),
                 ("CA sales (US$)", I["daily2025"]["CA"]["sales_usd"]), ("CA ad spend (US$)", I["daily2025"]["CA"]["ad_usd"]), ("CA units", I["daily2025"]["CA"]["units"])):
    ip.cell(row=r, column=1, value=lab)
    for k, v in enumerate(arr):
        c = ip.cell(row=r, column=3 + k, value=v); c.font = F(color=BLUE); c.number_format = "#,##0" if "units" in lab else '"$"#,##0'
    c = ip.cell(row=r, column=2, value=f"=SUM(C{r}:N{r})"); c.number_format = "#,##0" if "units" in lab else '"$"#,##0'
    r += 1
for lab, a, b in (("US TACoS that day", r - 5, r - 6), ("CA TACoS that day", r - 2, r - 3)):
    ip.cell(row=r, column=1, value=lab)
    for k in range(13):
        col = CL(2 + k); c = ip.cell(row=r, column=2 + k, value=f"={col}{a}/{col}{b}"); c.number_format = "0.0%"
    r += 1
r += 2
ip.cell(row=r, column=1, value="Sources").font = F(bold=True, color=NAVY); r += 1
SRC = ["Demand (units low / high): BFCM 2026 competitor tracker, demand read posted Oct 28 (28-day units and current pace per variation x own BFCM 2025 lift).",
       "Deal prices, COGS, FBA fee, referral %: team deal sheet, Oct 27, 2026 export (Umair). Canada COGS in the export are US$ figures next to C$ prices; converted at 1.40.",
       "Deal fees: 1.5% of deal sales + $100 per deal (Erik, Oct 19).",
       "TACoS now and ad spend per day: ads data, Oct 4 - Nov 2, 2026 (30 days; the last 7 days of ad sales still fill in, so TACoS reads slightly high).",
       "BFCM 2025 by day and TACoS before / during BFCM 2025: account sales data, Nov 20 - Dec 1, 2025 and Oct 21 - Nov 19, 2025. Deal-period factor: US 0.58 (14.1% -> 8.2%), CA 0.68 (13.0% -> 8.8%) where a product has no reliable own history.",
       I["tos_b4_us"] + " (ads data, last 30 days)."]
for s_ in SRC:
    c = ip.cell(row=r, column=1, value="• " + s_); c.alignment = WRAP; ip.merge_cells(start_row=r, start_column=1, end_row=r, end_column=14); ip.row_dimensions[r].height = 26; r += 1
# ---------------- Summary (first)
sm = wb.create_sheet("Summary", 0); sm.sheet_view.showGridLines = False
sm.column_dimensions["A"].width = 46; sm.column_dimensions["B"].width = 16; sm.column_dimensions["C"].width = 16; sm.column_dimensions["D"].width = 60
sm["A1"] = "BFCM 2026 PPC plan (Amazon US and CA), Nov 19 - 30"; sm["A1"].font = F(size=14, bold=True, color=NAVY)
sm["A2"] = "Draft by Shayan Rana for Joseph Fisher's approval · Nov 2, 2026 · numbers recalculate if you change a blue input"; sm["A2"].font = F(italic=True)
for j, h in enumerate(["", "US (US$)", "Canada (C$)", "What it means"], 1):
    c = sm.cell(row=4, column=j, value=h); c.font = F(bold=True, color="FFFFFF"); c.fill = HDR; c.border = BOX
us, ca = blocks["US"], blocks["CA"]
LINES = [("Expected sales, Nov 19 - 30 (plan units x deal price)", f"='Budget by product'!G{us[2]}", f"='Budget by product'!G{ca[2]}", "Mid-point of the demand read.", CUR),
         ("Ad budget, Nov 19 - 30", f"='Budget by product'!N{us[2]}", f"='Budget by product'!N{ca[2]}", "Sum of each product's plan TACoS x its expected sales.", CUR),
         ("Range (low - high demand)", f"=TEXT('Budget by product'!O{us[2]},\"$#,##0\")&\" - \"&TEXT('Budget by product'!P{us[2]},\"$#,##0\")",
          f"=TEXT('Budget by product'!O{ca[2]},\"$#,##0\")&\" - \"&TEXT('Budget by product'!P{ca[2]},\"$#,##0\")", "Budget moves with sales: the agent paces to it daily.", None),
         ("Plan TACoS (blended)", f"='Budget by product'!M{us[2]}", f"='Budget by product'!M{ca[2]}", "BFCM 2025 ran at 8.2% (US) and 8.8% (CA).", "pct"),
         ("Ad budget per day (average)", f"='Budget by product'!Q{us[2]}", f"='Budget by product'!Q{ca[2]}", "Black Friday and Cyber Monday get about 2.6x an average day.", CUR),
         ("Ad spend per day now (last 30 days, these products)", f"='Budget by product'!R{us[2]}", f"='Budget by product'!R{ca[2]}", "", CUR),
         ("Black Friday budget (Nov 27)", f"='Budget by day'!K{blocks['US'][2]-blocks['US'][0]+0}", None, "", CUR)]
rr = 5
for lab, a, b, note, fmt in LINES[:6]:
    sm.cell(row=rr, column=1, value=lab).font = F(bold=True)
    for j, v in ((2, a), (3, b)):
        c = sm.cell(row=rr, column=j, value=v); c.border = BOX
        c.number_format = (CUR["US"] if j == 2 else CUR["CA"]) if fmt is CUR else ("0.0%" if fmt == "pct" else "General")
    sm.cell(row=rr, column=4, value=note).alignment = WRAP; rr += 1
rr += 1
sm.cell(row=rr, column=1, value="Key calls in this plan").font = F(size=11, bold=True, color=NAVY); rr += 1
CALLS = ["Push the heroes that have room under their ceiling: Bamboo 4 Pc, Bamboo 6 Pc, Satin 4 Pc and Satin Fitted (US); Bamboo 4 Pc, Bamboo 6 Pc and Satin 4 Pc (CA). They carry most of the budget.",
         "Cut before Nov 19 where today's TACoS is already above the ceiling: CooLinens Pillowcases (43% now vs 14% ceiling at the $15.19 deal), Sleep Sanctuary Satin 4 Pc (25% vs 21%) and Silk Pillowcase (28% vs 27%).",
         "No ads beyond brand defence on Linen Curtains and Quilt Set: at the deal price they lose money (or earn about 1%) per unit before any ads.",
         "No BFCM increase on products without a deal (CooLinens Cooling Sheets, Decolure Cooling 4 Pc, Bamboo Fitted).",
         "Lightning Deal products (Satin 6 Pc and Silk on Nov 23, Sleephoria Cooling Fitted on Nov 25) concentrate budget on the deal day. If their Best Deal is approved, re-plan them as Best Deals.",
         "Every number is an estimate from the demand read and the Oct 27 deal prices. Amazon's deal prices can still change until Nov 13; the plan is re-run if they do."]
for t in CALLS:
    c = sm.cell(row=rr, column=1, value="• " + t); c.alignment = WRAP; sm.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=4); sm.row_dimensions[rr].height = 30; rr += 1
rr += 1
sm.cell(row=rr, column=1, value="Tabs").font = F(size=11, bold=True, color=NAVY); rr += 1
for t in ["Budget by product: units, price, break-even, ceiling, plan TACoS and budget for every product.", "Budget by day: each product's budget spread over Nov 19 - 30.",
          "Bid and placement rules: deal-day bids, top of search, what the agent does hourly and what a person checks.", "Inputs: BFCM 2025 by day and the sources."]:
    c = sm.cell(row=rr, column=1, value="• " + t); sm.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=4); rr += 1
for ws in wb.worksheets:
    for row_ in ws.iter_rows():
        for c in row_:
            if c.font is None or c.font.name != "Arial":
                c.font = Font(name="Arial", size=c.font.size or 9, bold=c.font.bold, italic=c.font.italic, color=c.font.color)
wb.save(OUT); print("saved", OUT)
