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
bp["A1"] = "BFCM 2026 PPC plan: budget, growth-plan band and TACoS cap by product, Nov 19 - 30 (all ad types: SP, SB, SB video, SD)"; bp["A1"].font = F(size=13, bold=True, color=NAVY)
bp["A2"] = ("Units = the demand read (low = last-28-day pace x own 2025 BFCM lift x 12 days; high = current pace x lift x 12). Avg selling price = deal price weighted by each "
            "variation's 28-day units (Lightning Deals: 1 deal day + 11 regular days). Break-even TACoS = (price - COGS - FBA - referral - 1.5% deal fee - $100 per deal) / price; "
            "cap = the lower of 80% of break-even and the growth-plan band ceiling. Base = today's 30-day product TACoS (Sponsored Products) x the deal-period factor (how far TACoS "
            "fell in BFCM 2025 vs the 30 days before), grossed up for Sponsored Brands, SB video and Display (now 20% of US spend). Growth floor in BFCM = the growth-plan band floor x "
            "the same factor (organic sales jump during the deal, so the same ad effort shows a lower TACoS). Plan TACoS = base, raised to the growth floor, never above the cap. "
            "Products with no deal hold today's daily spend. Blue = inputs, black = formulas.")
bp["A2"].font = F(italic=True, size=8.5); bp["A2"].alignment = WRAP; bp.merge_cells("A2:AB2"); bp.row_dimensions[2].height = 74
bp["A3"] = "Cap as share of break-even:"; bp["A3"].font = F(bold=True); bp["D3"] = 0.80; bp["D3"].number_format = "0%"; bp["D3"].font = F(bold=True, color=BLUE); bp["D3"].fill = YEL
bp["F3"] = "No-ads threshold (break-even TACoS at or below):"; bp["F3"].font = F(bold=True); bp["K3"] = 0.05; bp["K3"].number_format = "0%"; bp["K3"].font = F(bold=True, color=BLUE); bp["K3"].fill = YEL
COLS = [("Product", 24), ("BFCM 2026 deal", 16), ("Growth-plan stage", 11), ("Growth band floor (TACoS)", 8), ("Growth band ceiling (TACoS)", 8),
        ("Units low", 8), ("Units high", 8), ("Units plan (mid)", 8), ("Avg selling price", 9), ("Expected sales, 12 days", 11),
        ("Break-even TACoS at deal price", 9), ("80% of break-even", 8), ("SP TACoS now (30 days)", 8), ("Deal-period factor (2025 BFCM vs before)", 9),
        ("2025 BFCM TACoS (fallback)", 8), ("SP share of all ad spend", 8), ("Base TACoS in BFCM, all ad types", 9), ("Growth floor in BFCM", 8),
        ("Cap (break-even or band ceiling)", 9), ("Plan TACoS", 8), ("Ad budget Nov 19-30 (all ad types)", 11), ("Budget at low units", 10), ("Budget at high units", 10),
        ("Budget per day (avg)", 9), ("SP spend per day now (30 days)", 9), ("Per-day change vs now (all ad types)", 9), ("Growth-plan check", 26), ("Note", 44)]
for j, (h, w) in enumerate(COLS, 1):
    bp.column_dimensions[CL(j)].width = w
row = 5; blocks = {}
for m in ("US", "CA"):
    bp.cell(row=row, column=1, value=("United States (US$)" if m == "US" else "Canada (C$)")).font = F(size=11, bold=True, color=NAVY); row += 1
    for j, (h, w) in enumerate(COLS, 1):
        c = bp.cell(row=row, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX
    bp.row_dimensions[row].height = 58; row += 1; r0 = row
    rows = sorted([r for r in P if r["mkt"] == m], key=lambda r: -(r["sales_plan"] or 0))
    for r in rows:
        fac = None
        if r["tacos25_pre"] and r["tacos25_bf"] and r["tacos25_pre"] > 0.01 and r["tacos25_bf"] > 0.01:
            fac = max(0.3, min(1.2, r["tacos25_bf"] / r["tacos25_pre"]))
        fac = round(fac if fac is not None else MKT_FACTOR[m], 2)
        fb = r["tacos25_bf"] if (r["tacos25_bf"] or 0) > 0.01 else MKT_BF[m]
        deal = f"{r['deal_type']} {r['deal_dates']}" if r["deal_type"] else "No deal"
        st = I["stages"][m].get(str(r["pid"]), [None, None, None])
        R = row
        plan_f = (f'=IF(J{R}>0,MIN(Y{R}/P{R}*12,IF(L{R}="",Y{R}/P{R}*12,J{R}*L{R}))/J{R},0)' if not r["deal_type"] else
                  f'=IF(OR(K{R}="",K{R}<=$K$3),0,MIN(S{R},MAX(Q{R},IF(R{R}="",0,R{R}))))')
        check_f = ('No deal: hold today\'s spend' if not r["deal_type"] else
                   f'=IF(OR(K{R}="",K{R}<=$K$3),"No ads: break-even too thin",IF(R{R}="","Liquidation: judged on units, not TACoS",IF(R{R}>S{R},"Growth floor is above what break-even allows: capped",IF(ABS(T{R}-R{R})<0.0005,"Raised to the growth-plan floor",IF(ABS(T{R}-S{R})<0.0005,"At the cap","Within the growth band")))))')
        vals = [NAMES.get(r["short"], r["short"]), deal, st[0], (st[1] / 100 if st[1] is not None else None), (st[2] / 100 if st[2] is not None else None),
                round(r["units_lo"]), round(r["units_hi"]), f"=AVERAGE(F{R}:G{R})", round(r["asp"], 2), f"=H{R}*I{R}",
                round(r["be_tacos"], 4) if r["be_tacos"] is not None else None, f'=IF(K{R}="","",MAX(0,K{R}*$D$3))',
                round(r["tacos30"], 4) if r["tacos30"] is not None else None, fac, round(fb, 4), I["sp_share_recent"][m],
                f'=IF(M{R}<>"",M{R}*N{R},O{R})/P{R}', f'=IF(D{R}="","",D{R}*N{R})', f'=IF(L{R}="","",IF(E{R}="",L{R},MIN(E{R},L{R})))',
                plan_f, f"=J{R}*T{R}", f"=F{R}*I{R}*T{R}", f"=G{R}*I{R}*T{R}", f"=U{R}/12", round((r["spend30"] or 0) / 30, 2),
                f'=IF(Y{R}>0,X{R}/(Y{R}/P{R})-1,"")', check_f, NOTE.get(r["short"], "")]
        for j, v in enumerate(vals, 1):
            c = bp.cell(row=row, column=j, value=v); c.border = BOX; c.font = F(color=(BLUE if j in (3, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16, 25) else "000000"))
            c.number_format = {4: "0%", 5: "0%", 6: "#,##0", 7: "#,##0", 8: "#,##0", 9: CUR2[m], 10: CUR[m], 11: "0.0%", 12: "0.0%", 13: "0.0%", 14: "0.00", 15: "0.0%",
                               16: "0%", 17: "0.0%", 18: "0.0%", 19: "0.0%", 20: "0.0%", 21: CUR[m], 22: CUR[m], 23: CUR[m], 24: CUR[m], 25: CUR[m], 26: "+0%;-0%;0%"}.get(j, "General")
            if j in (2, 27, 28): c.alignment = WRAP
        bp.cell(row=row, column=21).font = F(bold=True); bp.cell(row=row, column=20).fill = GRN
        row += 1
    r1 = row - 1
    tot = ["Total", "", "", "", "", f"=SUM(F{r0}:F{r1})", f"=SUM(G{r0}:G{r1})", f"=SUM(H{r0}:H{r1})", "", f"=SUM(J{r0}:J{r1})", "", "", "", "", "", "", "", "", "",
           f"=U{row}/J{row}", f"=SUM(U{r0}:U{r1})", f"=SUM(V{r0}:V{r1})", f"=SUM(W{r0}:W{r1})", f"=U{row}/12", f"=SUM(Y{r0}:Y{r1})", "", "", ""]
    for j, v in enumerate(tot, 1):
        c = bp.cell(row=row, column=j, value=v); c.font = F(bold=True); c.border = BOX; c.fill = YEL
        c.number_format = {6: "#,##0", 7: "#,##0", 8: "#,##0", 10: CUR[m], 20: "0.0%", 21: CUR[m], 22: CUR[m], 23: CUR[m], 24: CUR[m], 25: CUR[m]}.get(j, "General")
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
        c = bd.cell(row=row, column=2, value=f"='Budget by product'!U{br}"); c.number_format = CUR[m]; c.border = BOX; c.font = F(bold=True)
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
 ("Bids", "Deal start (Nov 19, when the deal goes live)", "Best Deal heroes with room under the cap (US: Bamboo 4 Pc, Bamboo 6 Pc, Satin 4 Pc; CA: Bamboo 4 Pc, Bamboo 6 Pc): +20% on exact-match keywords that converted in the last 30 days. Products at or over their cap (Sleep Sanctuary Satin 4 Pc, Satin Fitted, CooLinens Pillowcases, Silk Pillowcase, Sleephoria Bamboo 6 Pc; CA Satin 4 and 6 Pc): no raise; bring them down to the cap before Nov 19.", "The deal price lifts conversion, so the same bid buys more sales."),
 ("Bids", "Black Friday (Nov 27) and Cyber Monday (Nov 30)", "+30% on the top 10 converting keywords per hero product, 6 AM - 11 PM ET. Back to deal-start bids the next morning.", "In 2025 these two days were 31% of BFCM sales at the lowest TACoS of the event (6-7%)."),
 ("Bids", "Lightning Deal day (Satin 6 Pc and Silk Nov 23, Sleephoria Cooling Fitted Nov 25)", "+50% bids and 4x the normal day budget for the deal hours only; back to normal when the deal ends.", "One day of deal traffic; outside it they sell at the regular price."),
 ("Bids", "Wasted clicks", "Any search term with 15+ clicks and 0 orders during the event: negate. Any keyword with 20+ clicks and 0 orders: -50% bid; 40+ clicks: pause.", ""),
 ("Bids", "Keyword over break-even", "Keyword ACoS above the product's break-even for 2 days running (10+ clicks): -20% bid. Product TACoS for the day (all ad types) above its cap: -15% on all non-hero keywords and remove any top-of-search boost until it is back under.", ""),
 ("Bids", "Out of stock", "A variation out of stock or under 1 day of cover: stop ads on that ASIN within the hour. If the hero variation goes out, move its keywords to the next best in-stock variation.", "Spend on an unbuyable ASIN is lost."),
 ("Bids", "No-deal products", "CooLinens Cooling Sheets, Decolure Cooling 4 Pc, Bamboo Fitted: no BFCM increase. Hold at today's daily spend or lower, under break-even.", "Without a deal they don't get the deal lift."),
 ("Bids", "No-ads products", "Linen Curtains and Quilt Set lose money (or earn about 1%) per unit at the deal price before any ads: brand-defence only, no prospecting.", ""),
 ("Top of search", "Who gets a boost", "Only Best Deal heroes with room under the cap: Bamboo 4 Pc, Bamboo 6 Pc, Satin 4 Pc (US); Bamboo 4 Pc, Bamboo 6 Pc (CA).", "Top of search converts best when the deal badge shows."),
 ("Top of search", "How much", "Top-of-search modifier +50% Nov 19 - 26 and Nov 28 - 29; +100% on Nov 27 and Nov 30; back to today's setting on Dec 1.", ""),
 ("Top of search", "Cap", "Bamboo 4 Pc already puts 40-75% of its spend on top of search at an effective bid of about $3-6 a click (vs about $1.50 on product pages). Cap the effective top-of-search bid at $6.50 on Bamboo 4 Pc and 6 Pc; if top-of-search ACoS for the day is above break-even ACoS, cut the modifier by 25 points.", "Stops the boost from buying unprofitable clicks."),
 ("SB, SB video, SD", "Brand and video", "Keep the SB and SB video campaigns live on Bamboo 4 / 6 Pc and Satin 4 Pc with deal-badge creative; their spend counts inside each product's budget and cap. Same deal-day step-ups as SP (Black Friday and Cyber Monday +30%). Keep their share near 19-20% of total (Ad types tab).", "They went live in October and are now 21% of US spend; leaving them out would under-plan the budget."),
 ("SB, SB video, SD", "Display", "Retargeting on viewers of our own deal ASINs only, about 1% of spend; switch off broad audiences for the event.", "Display has the weakest return; keep it to warm traffic."),
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
 ("Agent", "Every hour", "TACoS check (all ad types): today's TACoS for each product vs its cap. Over the cap: -15% on non-hero keywords and remove the top-of-search boost.", "Over the ceiling 3 hours running"),
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
# ---------------- Ad types
at = wb.create_sheet("Ad types"); at.sheet_view.showGridLines = False
at["A1"] = "Ad types: what runs now, what ran in BFCM 2025, and the BFCM 2026 split"; at["A1"].font = F(size=13, bold=True, color=NAVY)
at["A2"] = ("Sponsored Brands, SB video and Sponsored Display have no per-product report, so they are planned inside each product's budget and split at account level here. "
            "In the US they went from 3% of ad spend in late September to 21% last week, after the new SB, SB video and SD campaigns went live (Bamboo first, from Oct 14).")
at["A2"].font = F(italic=True, size=8.5); at["A2"].alignment = WRAP; at.merge_cells("A2:I2"); at.row_dimensions[2].height = 34
at.column_dimensions["A"].width = 30
for k in range(2, 10): at.column_dimensions[CL(k)].width = 13
r = 4
W = I["adtype_weekly"]["US"]
for j, h in enumerate(["US, by week (US$)"] + W["weeks"], 1):
    c = at.cell(row=r, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN
r += 1; w0 = r
for lab, k in (("Sponsored Products", "sp"), ("Sponsored Brands", "sb"), ("SB video", "sbv"), ("Sponsored Display", "sd"), ("Sales", "sales")):
    at.cell(row=r, column=1, value=lab)
    for i, v in enumerate(W[k]):
        c = at.cell(row=r, column=2 + i, value=v); c.font = F(color=BLUE); c.number_format = '"$"#,##0'
    r += 1
at.cell(row=r, column=1, value="Total ad spend").font = F(bold=True)
for i in range(6):
    col = CL(2 + i); c = at.cell(row=r, column=2 + i, value=f"=SUM({col}{w0}:{col}{w0+3})"); c.number_format = '"$"#,##0'; c.font = F(bold=True)
tr = r; r += 1
at.cell(row=r, column=1, value="Share not Sponsored Products")
for i in range(6):
    col = CL(2 + i); c = at.cell(row=r, column=2 + i, value=f"=1-{col}{w0}/{col}{tr}"); c.number_format = "0%"
r += 1
at.cell(row=r, column=1, value="TACoS (all ad types)")
for i in range(6):
    col = CL(2 + i); c = at.cell(row=r, column=2 + i, value=f"={col}{tr}/{col}{w0+4}"); c.number_format = "0.0%"
r += 3
B = I["adtype_bfcm2025"]["US"]
for j, h in enumerate(["BFCM 2026 split (US$)", "Last 2 weeks", "BFCM 2025", "Plan share", "Plan budget", "Where it goes"], 1):
    c = at.cell(row=r, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN
r += 1; s0 = r
WHERE = {"sp": "Every deal product: exact-match heroes, top of search for heroes under their cap, product-page defence.",
         "sb": "Brand headline on Bamboo 4 / 6 Pc and Satin 4 Pc: branded and category terms, deal-badge creative.",
         "sbv": "SB video on Bamboo 4 / 6 Pc (live since Oct 14): category terms, top of search.",
         "sd": "Retargeting on our own deal ASINs' viewers only; no broad audience during the event."}
for lab, k in (("Sponsored Products", "sp"), ("Sponsored Brands", "sb"), ("SB video", "sbv"), ("Sponsored Display", "sd")):
    at.cell(row=r, column=1, value=lab)
    c = at.cell(row=r, column=2, value=f"=SUM({CL(6)}{w0 + ['sp','sb','sbv','sd'].index(k)}:{CL(7)}{w0 + ['sp','sb','sbv','sd'].index(k)})/SUM(F{tr}:G{tr})"); c.number_format = "0.0%"
    c = at.cell(row=r, column=3, value=round(sum(B[k]) / sum(sum(B[x]) for x in B), 4)); c.number_format = "0.0%"; c.font = F(color=BLUE)
    c = at.cell(row=r, column=4, value=f"=B{r}"); c.number_format = "0.0%"; c.fill = GRN
    c = at.cell(row=r, column=5, value=f"=D{r}*'Budget by product'!U{blocks['US'][2]}"); c.number_format = '"$"#,##0'; c.font = F(bold=True)
    c = at.cell(row=r, column=6, value=WHERE[k]); c.alignment = WRAP; at.merge_cells(start_row=r, start_column=6, end_row=r, end_column=9); at.row_dimensions[r].height = 26
    r += 1
at.cell(row=r, column=1, value="Total").font = F(bold=True)
c = at.cell(row=r, column=4, value=f"=SUM(D{s0}:D{r-1})"); c.number_format = "0%"
c = at.cell(row=r, column=5, value=f"=SUM(E{s0}:E{r-1})"); c.number_format = '"$"#,##0'; c.font = F(bold=True)
r += 2
c = at.cell(row=r, column=1, value=("Canada: about 98% Sponsored Products (SB C$40-120 a week, no SB video or SD yet), so the Canadian budget is planned as SP. "
                                     "Plan share = the last two weeks' mix; change the green cells to move money between ad types.")); c.alignment = WRAP
at.merge_cells(start_row=r, start_column=1, end_row=r, end_column=9); at.row_dimensions[r].height = 30
# ---------------- Summary (first)
sm = wb.create_sheet("Summary", 0); sm.sheet_view.showGridLines = False
sm.column_dimensions["A"].width = 46; sm.column_dimensions["B"].width = 16; sm.column_dimensions["C"].width = 16; sm.column_dimensions["D"].width = 60
sm["A1"] = "BFCM 2026 PPC plan (Amazon US and CA), Nov 19 - 30"; sm["A1"].font = F(size=14, bold=True, color=NAVY)
sm["A2"] = "Draft by Shayan Rana for Joseph Fisher's approval · Nov 2, 2026 · numbers recalculate if you change a blue input"; sm["A2"].font = F(italic=True)
for j, h in enumerate(["", "US (US$)", "Canada (C$)", "What it means"], 1):
    c = sm.cell(row=4, column=j, value=h); c.font = F(bold=True, color="FFFFFF"); c.fill = HDR; c.border = BOX
us, ca = blocks["US"], blocks["CA"]
NOW_ALL = {"US": round(sum(I["adtype_weekly"]["US"][k][-1] for k in ("sp", "sb", "sbv", "sd")) / 7, 2),
           "CA": round(sum(I["adtype_weekly"]["CA_usd"][k][-1] for k in ("sp", "sb", "sbv", "sd")) / 7 * 1.40, 2)}
LINES = [("Expected sales, Nov 19 - 30 (plan units x deal price)", f"='Budget by product'!J{us[2]}", f"='Budget by product'!J{ca[2]}", "Mid-point of the demand read.", CUR),
         ("Ad budget, Nov 19 - 30 (SP + SB + SB video + SD)", f"='Budget by product'!U{us[2]}", f"='Budget by product'!U{ca[2]}", "Each product's plan TACoS x its expected sales; split by ad type on the Ad types tab.", CUR),
         ("Range (low - high demand)", f"=TEXT('Budget by product'!V{us[2]},\"$#,##0\")&\" - \"&TEXT('Budget by product'!W{us[2]},\"$#,##0\")",
          f"=TEXT('Budget by product'!V{ca[2]},\"$#,##0\")&\" - \"&TEXT('Budget by product'!W{ca[2]},\"$#,##0\")", "Budget moves with sales: the agent paces to it daily.", None),
         ("Plan TACoS (blended, all ad types)", f"='Budget by product'!T{us[2]}", f"='Budget by product'!T{ca[2]}", "BFCM 2025 ran at 8.2% (US) and 8.8% (CA); last week the account ran at 19.8% (US).", "pct"),
         ("Ad budget per day (average)", f"='Budget by product'!X{us[2]}", f"='Budget by product'!X{ca[2]}", "Black Friday and Cyber Monday get about 2.6x an average day.", CUR),
         ("Ad spend per day now, all ad types (Oct 26 - Nov 1)", NOW_ALL["US"], NOW_ALL["CA"], "Includes the new SB, SB video and SD campaigns (21% of US spend last week).", CUR)]
rr = 5
for lab, a, b, note, fmt in LINES[:6]:
    sm.cell(row=rr, column=1, value=lab).font = F(bold=True)
    for j, v in ((2, a), (3, b)):
        c = sm.cell(row=rr, column=j, value=v); c.border = BOX
        c.number_format = (CUR["US"] if j == 2 else CUR["CA"]) if fmt is CUR else ("0.0%" if fmt == "pct" else "General")
    sm.cell(row=rr, column=4, value=note).alignment = WRAP; rr += 1
rr += 1
sm.cell(row=rr, column=1, value="Key calls in this plan").font = F(size=11, bold=True, color=NAVY); rr += 1
CALLS = ["Realistic total: US $75.5K over the 12 days is in line with the $76.2K we actually spent in BFCM 2025, at a 10.4% TACoS (2025: 8.2%; the account ran at 19.8% last week). Canada C$24.0K at 10.5%.",
         "All ad types are in: Sponsored Brands, SB video and Display went from 3% of US spend in late September to 21% last week after the new campaigns went live. The plan keeps that mix: SP $60.7K, SB $5.4K, SB video $8.4K, SD $0.9K (Ad types tab). Canada is still about 98% SP.",
         "Aligned with the growth plan: each product's TACoS sits inside its growth-plan band (scaled for the deal), never above break-even. Bamboo 6 Pc (US and CA), Sleephoria Cooling Fitted and CA Satin Fitted are raised to the growth floor; Maintenance products are held to the 12% band ceiling (Sleep Sanctuary Satin 4 Pc down from 25%, Satin Fitted, CA Satin 4 and 6 Pc).",
         "Decisions for Joseph: CooLinens Pillowcases is a Launch product (band 25-40%) but at the $15.19 deal break-even only allows 14%, so it is capped at 14%. Silk Pillowcase is at its 25% cap.",
         "No ads beyond brand defence on Linen Curtains and Quilt Set (they lose money or make about 1% per unit at the deal price before ads). No BFCM increase on products without a deal (CooLinens Cooling Sheets, Decolure Cooling 4 Pc, Bamboo Fitted).",
         "Every number is an estimate from the demand read, the Oct 27 deal prices and last week's ad mix. Amazon's deal prices can still change until Nov 13; the plan is re-run if they do."]
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
