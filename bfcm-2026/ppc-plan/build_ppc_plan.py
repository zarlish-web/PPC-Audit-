"""Builds BFCM_2026_PPC_Plan.xlsx from plan_numbers.json + inputs_2026-11-02.json. Usage: python3 build_ppc_plan.py OUT.xlsx"""
import json, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.comments import Comment
HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "plan_numbers.json"))); I = json.load(open(os.path.join(HERE, "inputs_2026-11-02.json")))
OUT = sys.argv[1]
NAVY, BLUE, GREENF = "1F3864", "0000FF", "008000"
AT = "Ad types by product"
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
NOTE = {"DC B4": "Hero. Room under the ceiling: full BFCM push.", "DC B6": "Hero. Deal is 6.5% cheaper than 2025. 29% of its spend is SB, SB video and SD (counted inside the cap).",
        "DC S4": "Hero. Deal 2.6% cheaper than 2025: plan near the high end.", "SSS4": "Running at 21% TACoS today, above its 12% Maintenance cap: cut to the cap before Nov 19.",
        "DC S6": "Lightning Deal Nov 23 only (Best Deal requested). Budget weighted to Nov 23.", "DC Satin Fitted": "Deal 34% above 2025 paid; plan near the low end.",
        "DC Silk Pillowcase": "Lightning Deal Nov 23. TACoS 32% today, cap 25%.", "CL Pillowcases": "TACoS 53% today (all ad types; 18% of spend is SB video and SB) vs a 14% cap at the $15.19 deal: cut hard. Queen White runs out ~Nov 6.",
        "SL Cooling 4pc": "TACoS 30% today (SP only); deal 16% above 2025 paid.", "SL Cooling Fitted": "Lightning Deal Nov 25. Budget weighted to Nov 25.",
        "SL Cooling Comforter": "Deal 47% above 2025 paid; low end.", "SL Cooling Pillowcase": "Small; keep to the ceiling.",
        "SL B6": "Thin margin at deal (16% break-even).", "SL Quilt Set": "Break-even about 1% at the deal price: no ads beyond brand defence.",
        "DC Linen Curtains": "Loses money per unit at the deal price before ads: no ads.", "DC Chair Cover": "Small; keep to the ceiling.",
        "DC Bamboo Fitted": "No deal: hold at today's daily spend.", "DC Cooling 4pc": "No deal. TACoS 31% today, above its 23% cap: cut to the cap.",
        "CL Cooling Sheets": "No deal. Sales about doubled in the last 2 weeks (~$2.2K a day, above the demand read). Holds today's ~$740 a day at 33% TACoS, inside the 25-40% Launch band; a third of it is SB video and SB."}
wb = Workbook()
# ---------------- Budget by product
bp = wb.active; bp.title = "Budget by product"; bp.sheet_view.showGridLines = False
bp["A1"] = "BFCM 2026 PPC plan: budget, growth-plan band and TACoS cap by product, Nov 19 - 30 (all ad types: SP, SB, SB video, SD)"; bp["A1"].font = F(size=13, bold=True, color=NAVY)
bp["A2"] = ("Units = the demand read (low = last-28-day pace x own 2025 BFCM lift x 12 days; high = current pace x lift x 12). Avg selling price = deal price weighted by each "
            "variation's 28-day units (Lightning Deals: 1 deal day + 11 regular days). Break-even TACoS = (price - COGS - FBA - referral - 1.5% deal fee - $100 per deal) / price; "
            "cap = the lower of 80% of break-even and the growth-plan band ceiling. TACoS now = the product's ad spend per day over the last 14 days across all ad types (SP, SB, SB video, SD; see the Ad types by product tab) / its "
            "sales per day over the same 14 days. Base = TACoS now x the deal-period factor (how far TACoS fell in BFCM 2025 vs the 30 days before). Growth floor in BFCM = the growth-plan band floor x "
            "the same factor (organic sales jump during the deal, so the same ad effort shows a lower TACoS). Plan TACoS = base, raised to the growth floor, never above the cap. "
            "Products with no deal: budget = today's sales per day x 12 x plan TACoS, where plan TACoS = today's all-ad-type TACoS, cut to the cap if above it. Blue = inputs, black = formulas, green = linked from the Ad types by product tab.")
bp["A2"].font = F(italic=True, size=8.5); bp["A2"].alignment = WRAP; bp.merge_cells("A2:AB2"); bp.row_dimensions[2].height = 74
bp["A3"] = "Cap as share of break-even:"; bp["A3"].font = F(bold=True); bp["D3"] = 0.80; bp["D3"].number_format = "0%"; bp["D3"].font = F(bold=True, color=BLUE); bp["D3"].fill = YEL
bp["F3"] = "No-ads threshold (break-even TACoS at or below):"; bp["F3"].font = F(bold=True); bp["K3"] = 0.05; bp["K3"].number_format = "0%"; bp["K3"].font = F(bold=True, color=BLUE); bp["K3"].fill = YEL
COLS = [("Product", 24), ("BFCM 2026 deal", 16), ("Growth-plan stage", 11), ("Growth band floor (TACoS)", 8), ("Growth band ceiling (TACoS)", 8),
        ("Units low", 8), ("Units high", 8), ("Units plan (mid)", 8), ("Avg selling price", 9), ("Expected sales, 12 days", 11),
        ("Break-even TACoS at deal price", 9), ("80% of break-even", 8), ("TACoS now, all ad types", 8), ("Deal-period factor (2025 BFCM vs before)", 9),
        ("2025 BFCM TACoS (fallback)", 8), ("SP share of this product's ad spend (14 days)", 9), ("Base TACoS in BFCM, all ad types", 9), ("Growth floor in BFCM", 8),
        ("Cap (break-even or band ceiling)", 9), ("Plan TACoS", 8), ("Ad budget Nov 19-30 (all ad types)", 11), ("Budget at low units", 10), ("Budget at high units", 10),
        ("Budget per day (avg)", 9), ("Ad spend per day now, all ad types (14 days)", 10), ("Per-day change vs now (all ad types)", 9), ("Growth-plan check", 26), ("Note", 44)]
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
        plan_f = (f'=IF(M{R}="",0,IF(S{R}="",M{R},MIN(M{R},S{R})))' if not r["deal_type"] else
                  f'=IF(OR(K{R}="",K{R}<=$K$3),0,MIN(S{R},MAX(Q{R},IF(R{R}="",0,R{R}))))')
        check_f = (f'=IF(AND(M{R}<>"",S{R}<>"",M{R}>S{R}),"No deal: today\'s spend, cut to the cap","No deal: hold today\'s spend")' if not r["deal_type"] else
                   f'=IF(OR(K{R}="",K{R}<=$K$3),"No ads: break-even too thin",IF(R{R}="","Liquidation: judged on units, not TACoS",IF(R{R}>S{R},"Growth floor is above what break-even allows: capped",IF(ABS(T{R}-R{R})<0.0005,"Raised to the growth-plan floor",IF(ABS(T{R}-S{R})<0.0005,"At the cap","Within the growth band")))))')
        vals = [NAMES.get(r["short"], r["short"]), deal, st[0], (st[1] / 100 if st[1] is not None else None), (st[2] / 100 if st[2] is not None else None),
                round(r["units_lo"]), round(r["units_hi"]), f"=AVERAGE(F{R}:G{R})", round(r["asp"], 2), f"=H{R}*I{R}",
                round(r["be_tacos"], 4) if r["be_tacos"] is not None else None, f'=IF(K{R}="","",MAX(0,K{R}*$D$3))',
                f"='{AT}'!K{R}", fac, round(fb, 4), f"='{AT}'!G{R}",
                f'=IF(M{R}<>"",M{R}*N{R},O{R})', f'=IF(D{R}="","",D{R}*N{R})', f'=IF(L{R}="",IF(E{R}="","",E{R}),IF(E{R}="",L{R},MIN(E{R},L{R})))',
                plan_f, (f"=J{R}*T{R}" if r["deal_type"] else f"='{AT}'!J{R}*12*T{R}"), (f"=F{R}*I{R}*T{R}" if r["deal_type"] else f"=U{R}"), (f"=G{R}*I{R}*T{R}" if r["deal_type"] else f"=U{R}"), f"=U{R}/12", f"='{AT}'!I{R}",
                f'=IF(Y{R}>0,X{R}/Y{R}-1,"")', check_f, NOTE.get(r["short"], "")]
        for j, v in enumerate(vals, 1):
            c = bp.cell(row=row, column=j, value=v); c.border = BOX; c.font = F(color=(BLUE if j in (3, 4, 5, 6, 7, 9, 11, 14, 15) else GREENF if j in (13, 16, 25) else "000000"))
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
# ---------------- Ad types by product (same rows as Budget by product)
ap = wb.create_sheet(AT); ap.sheet_view.showGridLines = False
ap["A1"] = "Ad spend by product and ad type: what runs now, TACoS now across all ad types, and how each product's BFCM budget splits"; ap["A1"].font = F(size=13, bold=True, color=NAVY)
ap["A2"] = ("Spend and sales Oct 19 - Nov 1, 2026 (14 days) per product by ad type, summed over its child ASINs (covers 96-99% of ad spend and about 95% of sales; "
            "Canada converted to C$ at 1.4036). TACoS now = ad spend (all ad types) / sales, same 14 days. Each product's BFCM budget is split by its own current mix: products that run SB video "
            "(CooLinens, Bamboo) carry that cost inside their own cap. Rows line up with the Budget by product tab.")
ap["A2"].font = F(italic=True, size=8.5); ap["A2"].alignment = WRAP; ap.merge_cells("A2:U2"); ap.row_dimensions[2].height = 46
ACOLS = [("Product", 24), ("Sponsored Products, 14 days", 10), ("Sponsored Brands, 14 days", 10), ("SB video, 14 days", 10), ("Sponsored Display, 14 days", 10),
         ("All ad types, 14 days", 10), ("SP share", 7), ("SB + SB video + SD share", 8), ("Ad spend per day now, all ad types", 10), ("Sales per day (same 14 days)", 10),
         ("TACoS now, all ad types", 8), ("TACoS now, SP only (30 days)", 8), ("Break-even TACoS at deal price", 9), ("Cap (Budget by product)", 8),
         ("Now vs cap", 22), ("BFCM budget, all ad types", 10), ("of which SP", 10), ("of which SB", 10), ("of which SB video", 10), ("of which SD", 10), ("Where SB / SB video / SD run", 34)]
for j, (h, w) in enumerate(ACOLS, 1): ap.column_dimensions[CL(j)].width = w
A14 = I["adtype14"]
for m in ("US", "CA"):
    r0, r1, rt, rows = blocks[m]
    ap.cell(row=r0 - 2, column=1, value=("United States (US$)" if m == "US" else "Canada (C$)")).font = F(size=11, bold=True, color=NAVY)
    for j, (h, w) in enumerate(ACOLS, 1):
        c = ap.cell(row=r0 - 1, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX
    ap.row_dimensions[r0 - 1].height = 46
    for i, r in enumerate(rows):
        R = r0 + i; a = A14[m].get(str(r["pid"]), [0, 0, 0, 0, 0])
        s14 = a[4] / 14 if a[4] else None
        where = []
        if a[2] > 1: where.append(f"SB video {a[2] / max(sum(a[:4]), 1):.0%}")
        if a[1] > 1: where.append(f"SB {a[1] / max(sum(a[:4]), 1):.0%}")
        if a[3] > 1: where.append(f"SD {a[3] / max(sum(a[:4]), 1):.0%}")
        vals = [f"='Budget by product'!A{R}", a[0], a[1], a[2], a[3], f"=SUM(B{R}:E{R})", f"=IF(F{R}>0,B{R}/F{R},1)", f"=1-G{R}", f"=F{R}/14",
                round(s14, 2) if s14 else None, f'=IF(J{R}="","",I{R}/J{R})', r["tacos30"], f"='Budget by product'!K{R}", f"='Budget by product'!S{R}",
                f'=IF(OR(K{R}="",N{R}=""),"",IF(K{R}>N{R},"Over the cap now: bring down before Nov 19","Under the cap"))',
                f"='Budget by product'!U{R}", f"=P{R}*G{R}", f"=IF(F{R}>0,P{R}*C{R}/F{R},0)", f"=IF(F{R}>0,P{R}*D{R}/F{R},0)", f"=IF(F{R}>0,P{R}*E{R}/F{R},0)",
                ", ".join(where) if where else "SP only"]
        for j, v in enumerate(vals, 1):
            c = ap.cell(row=R, column=j, value=v); c.border = BOX
            c.font = F(color=(BLUE if j in (2, 3, 4, 5, 10, 12) else GREENF if j in (1, 13, 14, 16) else "000000"))
            c.number_format = {7: "0%", 8: "0%", 11: "0.0%", 12: "0.0%", 13: "0.0%", 14: "0.0%"}.get(j, CUR[m] if j != 15 and j != 21 else "General")
            if j in (15, 21): c.alignment = WRAP
        ap.cell(row=R, column=16).font = F(bold=True, color=GREENF)
    tot = ["Total"] + [f"=SUM({CL(k)}{r0}:{CL(k)}{r1})" for k in range(2, 7)] + [f"=IF(F{rt}>0,B{rt}/F{rt},1)", f"=1-G{rt}", f"=F{rt}/14", f"=SUM(J{r0}:J{r1})",
           f"=IF(J{rt}>0,I{rt}/J{rt},\"\")", "", "", "", "", f"=SUM(P{r0}:P{r1})", f"=SUM(Q{r0}:Q{r1})", f"=SUM(R{r0}:R{r1})", f"=SUM(S{r0}:S{r1})", f"=SUM(T{r0}:T{r1})", ""]
    for j, v in enumerate(tot, 1):
        c = ap.cell(row=rt, column=j, value=v); c.font = F(bold=True); c.border = BOX; c.fill = YEL
        c.number_format = {7: "0%", 8: "0%", 11: "0.0%"}.get(j, CUR[m])
    ap.cell(row=rt + 1, column=1, value=("Products in the plan only; about $250 of US spend in the 14 days sat on products outside the plan." if m == "US" else
                                          "Canada runs almost only Sponsored Products (a little SB on Bamboo 4 Pc and Satin 4 Pc).")).font = F(italic=True, size=8.5)
ap.freeze_panes = "B5"
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
 ("Bids", "Deal start (Nov 19, when the deal goes live)", "Best Deal heroes with room under the cap (US: Bamboo 4 Pc; CA: Bamboo 4 Pc, Bamboo 6 Pc): +20% on exact-match keywords that converted in the last 30 days. US Bamboo 6 Pc runs right at its cap (19.3%) and US Satin 4 Pc just over it (12.7% vs 12%): raise them only once their daily TACoS is under the cap. Products over their cap today (US: Sleep Sanctuary Satin 4 Pc, Satin 6 Pc, Satin Fitted, Sleephoria Cooling 4 Pc, CooLinens Pillowcases, Silk Pillowcase, Sleephoria Cooling Pillowcase, Decolure Cooling 4 Pc; CA: Satin 4 Pc, Satin 6 Pc, Satin Fitted, Sleep Sanctuary Satin 4 Pc): no raise; bring them down to the cap before Nov 19.", "The deal price lifts conversion, so the same bid buys more sales."),
 ("Bids", "Black Friday (Nov 27) and Cyber Monday (Nov 30)", "+30% on the top 10 converting keywords per hero product, 6 AM - 11 PM ET. Back to deal-start bids the next morning.", "In 2025 these two days were 31% of BFCM sales at the lowest TACoS of the event (6-7%)."),
 ("Bids", "Lightning Deal day (Satin 6 Pc and Silk Nov 23, Sleephoria Cooling Fitted Nov 25)", "+50% bids and 4x the normal day budget for the deal hours only; back to normal when the deal ends.", "One day of deal traffic; outside it they sell at the regular price."),
 ("Bids", "Wasted clicks", "Any search term with 15+ clicks and 0 orders during the event: negate. Any keyword with 20+ clicks and 0 orders: -50% bid; 40+ clicks: pause.", ""),
 ("Bids", "Keyword over break-even", "Keyword ACoS above the product's break-even for 2 days running (10+ clicks): -20% bid. Product TACoS for the day (all ad types) above its cap: -15% on all non-hero keywords and remove any top-of-search boost until it is back under.", ""),
 ("Bids", "Out of stock", "A variation out of stock or under 1 day of cover: stop ads on that ASIN within the hour. If the hero variation goes out, move its keywords to the next best in-stock variation.", "Spend on an unbuyable ASIN is lost."),
 ("Bids", "No-deal products", "CooLinens Cooling Sheets, Decolure Cooling 4 Pc, Bamboo Fitted: no BFCM increase. Hold at today's daily spend or lower, under break-even.", "Without a deal they don't get the deal lift."),
 ("Bids", "No-ads products", "Linen Curtains and Quilt Set lose money (or earn about 1%) per unit at the deal price before any ads: brand-defence only, no prospecting.", ""),
 ("Top of search", "Who gets a boost", "Only Best Deal heroes with room under the cap: Bamboo 4 Pc (US); Bamboo 4 Pc, Bamboo 6 Pc (CA). US Bamboo 6 Pc and Satin 4 Pc join once their daily TACoS is back under the cap.", "Top of search converts best when the deal badge shows."),
 ("Top of search", "How much", "Top-of-search modifier +50% Nov 19 - 26 and Nov 28 - 29; +100% on Nov 27 and Nov 30; back to today's setting on Dec 1.", ""),
 ("Top of search", "Cap", "Bamboo 4 Pc already puts 40-75% of its spend on top of search at an effective bid of about $3-6 a click (vs about $1.50 on product pages). Cap the effective top-of-search bid at $6.50 on Bamboo 4 Pc and 6 Pc; if top-of-search ACoS for the day is above break-even ACoS, cut the modifier by 25 points.", "Stops the boost from buying unprofitable clicks."),
 ("SB, SB video, SD", "Brand and video", "Keep the SB and SB video campaigns live with deal-badge creative where they run today: Bamboo 4 / 6 Pc, CooLinens Cooling Sheets and Pillowcases (SB video), Satin 4 Pc and Satin Fitted (SB). Their spend counts inside each product's own budget and cap (Ad types by product tab). Same deal-day step-ups as SP (Black Friday and Cyber Monday +30%). If a product is over its cap, cut SB video first on the Launch products where it is the biggest non-SP cost.", "They went live in October and are now 20% of US spend; on Bamboo 6 Pc and CooLinens Cooling Sheets they are about a third of the product's spend."),
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
       "TACoS now, ad spend per day and the split by ad type: spend (SP, SB, SB video, SD) and sales per child ASIN, Oct 19 - Nov 1, 2026 (14 days), summed per product. SP-only TACoS over 30 days (Oct 4 - Nov 2) kept for reference.",
       "BFCM 2025 by day and TACoS before / during BFCM 2025: account sales data, Nov 20 - Dec 1, 2025 and Oct 21 - Nov 19, 2025. Deal-period factor: US 0.58 (14.1% -> 8.2%), CA 0.68 (13.0% -> 8.8%) where a product has no reliable own history.",
       I["tos_b4_us"] + " (ads data, last 30 days)."]
for s_ in SRC:
    c = ip.cell(row=r, column=1, value="• " + s_); c.alignment = WRAP; ip.merge_cells(start_row=r, start_column=1, end_row=r, end_column=14); ip.row_dimensions[r].height = 26; r += 1
# ---------------- Ad types
at = wb.create_sheet("Ad types"); at.sheet_view.showGridLines = False
at["A1"] = "Ad types: what runs now, what ran in BFCM 2025, and the BFCM 2026 split"; at["A1"].font = F(size=13, bold=True, color=NAVY)
at["A2"] = ("Sponsored Brands, SB video and Sponsored Display are tracked per product (Ad types by product tab) and sit inside each product's budget and cap; this tab adds them up. "
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
         "sbv": "SB video: CooLinens Cooling Sheets and Pillowcases, Bamboo 4 / 6 Pc: category terms, top of search.",
         "sd": "Retargeting on our own deal ASINs' viewers only; no broad audience during the event."}
for lab, k in (("Sponsored Products", "sp"), ("Sponsored Brands", "sb"), ("SB video", "sbv"), ("Sponsored Display", "sd")):
    at.cell(row=r, column=1, value=lab)
    c = at.cell(row=r, column=2, value=f"=SUM({CL(6)}{w0 + ['sp','sb','sbv','sd'].index(k)}:{CL(7)}{w0 + ['sp','sb','sbv','sd'].index(k)})/SUM(F{tr}:G{tr})"); c.number_format = "0.0%"
    c = at.cell(row=r, column=3, value=round(sum(B[k]) / sum(sum(B[x]) for x in B), 4)); c.number_format = "0.0%"; c.font = F(color=BLUE)
    c = at.cell(row=r, column=4, value=f"=IF(E{s0+4}>0,E{r}/E{s0+4},0)"); c.number_format = "0.0%"
    c = at.cell(row=r, column=5, value=f"='{AT}'!{CL(17 + ['sp','sb','sbv','sd'].index(k))}{blocks['US'][2]}"); c.number_format = '"$"#,##0'; c.font = F(bold=True, color=GREENF)
    c = at.cell(row=r, column=6, value=WHERE[k]); c.alignment = WRAP; at.merge_cells(start_row=r, start_column=6, end_row=r, end_column=9); at.row_dimensions[r].height = 26
    r += 1
at.cell(row=r, column=1, value="Total").font = F(bold=True)
c = at.cell(row=r, column=4, value=f"=SUM(D{s0}:D{r-1})"); c.number_format = "0%"
c = at.cell(row=r, column=5, value=f"=SUM(E{s0}:E{r-1})"); c.number_format = '"$"#,##0'; c.font = F(bold=True)
r += 2
c = at.cell(row=r, column=1, value=("Canada: about 98% Sponsored Products (SB C$40-120 a week, no SB video or SD yet), so the Canadian budget is planned as SP. "
                                     "Plan budget by ad type = the sum of each product's own split (Ad types by product tab).")); c.alignment = WRAP
at.merge_cells(start_row=r, start_column=1, end_row=r, end_column=9); at.row_dimensions[r].height = 30
# ---------------- 2025 vs 2026 check
HC = "2025 vs 2026 check"
hc = wb.create_sheet(HC); hc.sheet_view.showGridLines = False
hc["A1"] = "History check: how BFCM 2025 ramped, where 2026 stands today, and what that says about the budget"; hc["A1"].font = F(size=13, bold=True, color=NAVY)
hc["A2"] = ("Whole account, all ad types (SP, SB, SB video, SD). Same calendar windows both years. Canada amounts are recorded in US$; the C$ lines convert at the rate in the yellow cell. "
            "Two independent checks: (A) raise today's spend the way spend rose in BFCM 2025; (B) grow today's sales the way sales rose in BFCM 2025 and apply today's TACoS scaled by how far TACoS fell in BFCM 2025.")
hc["A2"].font = F(italic=True, size=8.5); hc["A2"].alignment = WRAP; hc.merge_cells("A2:S2"); hc.row_dimensions[2].height = 34
hc["A3"] = "C$ per US$:"; hc["A3"].font = F(bold=True); hc["C3"] = 1.4036; hc["C3"].font = F(bold=True, color=BLUE); hc["C3"].fill = YEL; hc["C3"].number_format = "0.0000"
HCOLS = [("Period", 30), ("Days", 6), ("Sales", 11), ("Units", 8), ("SP spend", 10), ("SB spend", 9), ("SB video spend", 9), ("SD spend", 8), ("All ad spend", 10),
         ("Sessions", 10), ("SP clicks", 9), ("Sales per day", 10), ("Ad spend per day", 10), ("TACoS (all ad types)", 8), ("Share not SP", 7), ("Sessions per day", 9),
         ("Conversion (units / sessions)", 9), ("Units per day", 8), ("SP cost per click", 8)]
for j, (h, w) in enumerate(HCOLS, 1): hc.column_dimensions[CL(j)].width = w
PC = I["periods_compare"]; hrow = 5; HR = {}
for m in ("US", "CA"):
    hc.cell(row=hrow, column=1, value=("United States (US$)" if m == "US" else "Canada (recorded in US$)")).font = F(size=11, bold=True, color=NAVY); hrow += 1
    for j, (h, w) in enumerate(HCOLS, 1):
        c = hc.cell(row=hrow, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN; c.border = BOX
    hc.row_dimensions[hrow].height = 34; hrow += 1; p0 = hrow
    for lab, r in zip(PC["labels"], PC[m]):
        d, s_, u, sp, sb, sbv, sd, se, cl, _ = r; R = hrow
        vals = [lab, d, s_, u, sp, sb, sbv, sd, f"=SUM(E{R}:H{R})", se, cl, f"=C{R}/B{R}", f"=I{R}/B{R}", f"=IF(C{R}>0,I{R}/C{R},\"\")", f"=IF(I{R}>0,1-E{R}/I{R},\"\")",
                f"=J{R}/B{R}", f"=IF(J{R}>0,D{R}/J{R},\"\")", f"=D{R}/B{R}", f"=IF(K{R}>0,E{R}/K{R},\"\")"]
        for j, v in enumerate(vals, 1):
            c = hc.cell(row=R, column=j, value=v); c.border = BOX; c.font = F(color=(BLUE if 2 <= j <= 8 or j in (10, 11) else "000000"), bold=("BFCM" in lab or "now" in lab) and j == 1)
            c.number_format = {2: "0", 4: "#,##0", 10: "#,##0", 11: "#,##0", 14: "0.0%", 15: "0%", 16: "#,##0", 17: "0.00%", 18: "#,##0", 19: '"$"0.00'}.get(j, '"$"#,##0')
            if "BFCM" in lab: c.fill = YEL
            if "now" in lab: c.fill = GRN
        hrow += 1
    HR[m] = p0; hrow += 2
# rows: p0+0 Sep21-Oct18 25, +1 Oct19-Nov1 25, +2 run-up, +3 BFCM 25, +4 after, +5 Sep21-Oct18 26, +6 now
hrow += 0
hc.cell(row=hrow, column=1, value="What the numbers say").font = F(size=11, bold=True, color=NAVY); hrow += 1
for j, h in enumerate(["", "", "United States", "", "Canada", "", "How to read it"], 1):
    c = hc.cell(row=hrow, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CEN
hc.merge_cells(start_row=hrow, start_column=1, end_row=hrow, end_column=2); hc.merge_cells(start_row=hrow, start_column=7, end_row=hrow, end_column=15); hrow += 1
u, c_ = HR["US"], HR["CA"]
pb = blocks
CHECK = [
 ("BFCM 2025: spend per day vs Oct 19 - Nov 1, 2025", f"=M{u+3}/M{u+1}", f"=M{c_+3}/M{c_+1}", "x", "How much harder we spent in BFCM 2025 than in the same 14 days we are in now."),
 ("BFCM 2025: spend per day vs the run-up (Nov 2 - 19)", f"=M{u+3}/M{u+2}", f"=M{c_+3}/M{c_+2}", "x", ""),
 ("BFCM 2025: sales per day vs Oct 19 - Nov 1, 2025", f"=L{u+3}/L{u+1}", f"=L{c_+3}/L{c_+1}", "x", "Sales rose much more than spend, so TACoS fell."),
 ("BFCM 2025: sessions per day vs Oct 19 - Nov 1, 2025", f"=P{u+3}/P{u+1}", f"=P{c_+3}/P{c_+1}", "x", "Traffic rose about as much as sales; conversion stayed about the same."),
 ("BFCM 2025: TACoS vs Oct 19 - Nov 1, 2025", f"=N{u+3}/N{u+1}", f"=N{c_+3}/N{c_+1}", "x", "Deal-period factor for the whole account."),
 ("After BFCM 2025 (Dec 2 - 15): spend per day vs Oct 19 - Nov 1", f"=M{u+4}/M{u+1}", f"=M{c_+4}/M{c_+1}", "x", "Spend stayed about 1.5x for two weeks after BFCM (holiday tail), at 11% TACoS."),
 ("2026 now vs 2025 same 14 days: sales per day", f"=L{u+6}/L{u+1}-1", f"=L{c_+6}/L{c_+1}-1", "pct", "2026 is selling about a third less than this time last year (Canada about half)."),
 ("2026 now vs 2025 same 14 days: sessions per day", f"=P{u+6}/P{u+1}-1", f"=P{c_+6}/P{c_+1}-1", "pct", "Traffic is down by about as much as sales: fewer visitors, not worse conversion."),
 ("2026 now vs 2025 same 14 days: ad spend per day", f"=M{u+6}/M{u+1}-1", f"=M{c_+6}/M{c_+1}-1", "pct", "We spend almost what we spent last year on a smaller sales base, so TACoS is higher."),
 ("2026 now vs 2025 same 14 days: SP cost per click", f"=S{u+6}/S{u+1}-1", f"=S{c_+6}/S{c_+1}-1", "pct", "Clicks are cheaper this year."),
 ("2026: TACoS now vs same 14 days 2025", f"=N{u+6}-N{u+1}", f"=N{c_+6}-N{c_+1}", "pts", "Percentage points."),
 ("(A) Today's spend per day x 2025 BFCM spend rise x 12 days", f"=M{u+6}*C{hrow}*12", f"=M{c_+6}*E{hrow}*12*$C$3", "cur", "History check A: raise spend the way we did last year. (Same answer as growing today's sales like 2025 at 2025's TACoS drop.)"),
 ("(B) Expected sales, Nov 19 - 30 (demand read)", f"='Budget by product'!J{pb['US'][2]}", f"='Budget by product'!J{pb['CA'][2]}", "cur", "The plan's expected sales for the products in the plan."),
 ("(B) Account TACoS in BFCM if it falls like 2025", f"=N{u+6}*C{hrow+4}", f"=N{c_+6}*E{hrow+4}", "pct1", "Today's all-ad-type TACoS x the 2025 deal-period factor."),
 ("(B) Budget = expected sales x that TACoS", f"=C{hrow+12}*C{hrow+13}", f"=E{hrow+12}*E{hrow+13}", "cur", "History check B: the demand read's sales at last year's TACoS behaviour."),
 ("Plan budget (Budget by product tab)", f"='Budget by product'!U{pb['US'][2]}", f"='Budget by product'!U{pb['CA'][2]}", "cur", "Built product by product: plan TACoS x expected sales, inside growth bands and break-even caps."),
 ("Plan vs check A", f"=C{hrow+15}/C{hrow+11}-1", f"=E{hrow+15}/E{hrow+11}-1", "pct", "Main reason the plan is higher: the demand read expects sales to jump more than they did in 2025 (last two lines)."),
 ("Plan vs check B", f"=C{hrow+15}/C{hrow+14}-1", f"=E{hrow+15}/E{hrow+14}-1", "pct", "On the same sales, the plan is a little above the account-level TACoS: growth-plan floors on Bamboo / Sleephoria and CooLinens Cooling Sheets held at 33%."),
 ("Plan: expected sales per day vs plan products' sales per day now", f"='Budget by product'!J{pb['US'][2]}/12/'{AT}'!J{pb['US'][2]}", f"='Budget by product'!J{pb['CA'][2]}/12/'{AT}'!J{pb['CA'][2]}", "x", "The demand read's sales jump for BFCM 2026 ..."),
 ("2025: BFCM sales per day vs the same 14 days before", f"=C{hrow+2}", f"=E{hrow+2}", "x", "... vs what actually happened in 2025. If 2026 only matches 2025, sales and spend land near check A, because the agent paces each product to its TACoS on actual sales."),
]
h0 = hrow
for lab, us_f, ca_f, fmt, note in CHECK:
    hc.cell(row=hrow, column=1, value=lab).font = F(bold=lab.startswith("(") or lab.startswith("Plan"))
    hc.merge_cells(start_row=hrow, start_column=1, end_row=hrow, end_column=2)
    for col, v, mk in ((3, us_f, "US"), (5, ca_f, "CA")):
        c = hc.cell(row=hrow, column=col, value=v); c.border = BOX; c.font = F(bold=True)
        c.number_format = {"x": '0.00"x"', "pct": "+0%;-0%;0%", "pct1": "0.0%", "pts": '+0.0%;-0.0%', "cur": CUR[mk]}[fmt]
        if lab.startswith("(A)") or lab.startswith("(B) Budget") or lab.startswith("Plan budget"): c.fill = YEL
    c = hc.cell(row=hrow, column=7, value=note); c.alignment = WRAP; hc.merge_cells(start_row=hrow, start_column=7, end_row=hrow, end_column=15)
    hrow += 1
hc.freeze_panes = "B5"
HIST = {"A": h0 + 11, "B": h0 + 14}
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
         ("Ad budget, Nov 19 - 30 (SP + SB + SB video + SD)", f"='Budget by product'!U{us[2]}", f"='Budget by product'!U{ca[2]}", "Each product's plan TACoS x its expected sales; split by ad type on the Ad types by product tab.", CUR),
         ("Range (low - high demand)", f"=TEXT('Budget by product'!V{us[2]},\"$#,##0\")&\" - \"&TEXT('Budget by product'!W{us[2]},\"$#,##0\")",
          f"=TEXT('Budget by product'!V{ca[2]},\"$#,##0\")&\" - \"&TEXT('Budget by product'!W{ca[2]},\"$#,##0\")", "Budget moves with sales: the agent paces to it daily.", None),
         ("Plan TACoS (blended, all ad types)", f"='Budget by product'!T{us[2]}", f"='Budget by product'!T{ca[2]}", "BFCM 2025 ran at 8.2% (US) and 8.8% (CA); last week the account ran at 19.8% (US).", "pct"),
         ("Ad budget per day (average)", f"='Budget by product'!X{us[2]}", f"='Budget by product'!X{ca[2]}", "Black Friday and Cyber Monday get about 2.6x an average day.", CUR),
         ("Ad spend per day now, all ad types (Oct 26 - Nov 1)", NOW_ALL["US"], NOW_ALL["CA"], "Includes the new SB, SB video and SD campaigns (21% of US spend last week).", CUR),
         ("History check A: raise today's spend the way we did in BFCM 2025", f"='{HC}'!C{HIST['A']}", f"='{HC}'!E{HIST['A']}", "BFCM 2025 spend was 1.6x (US) / 2.3x (CA) the same 14 days before. Suggested base budget.", CUR),
         ("History check B: expected sales at 2025's TACoS drop", f"='{HC}'!C{HIST['B']}", f"='{HC}'!E{HIST['B']}", "Demand read's sales x today's TACoS x the 2025 deal-period factor.", CUR)]
rr = 5
for lab, a, b, note, fmt in LINES:
    sm.cell(row=rr, column=1, value=lab).font = F(bold=True)
    for j, v in ((2, a), (3, b)):
        c = sm.cell(row=rr, column=j, value=v); c.border = BOX
        c.number_format = (CUR["US"] if j == 2 else CUR["CA"]) if fmt is CUR else ("0.0%" if fmt == "pct" else "General")
    sm.cell(row=rr, column=4, value=note).alignment = WRAP; rr += 1
rr += 1
sm.cell(row=rr, column=1, value="Key calls in this plan").font = F(size=11, bold=True, color=NAVY); rr += 1
CALLS = ["Realistic total: US $88.2K over the 12 days (12.1% TACoS) vs $76.2K actually spent in BFCM 2025 (8.2%). The account runs at 20% TACoS today across all ad types (14.1% before BFCM 2025), so the deal-period TACoS starts higher. Canada C$25.5K at 11.1%.",
         "SB, SB video and SD are now tracked per product (Ad types by product tab): each product's TACoS now, break-even and cap include all four ad types, and its budget splits by its own mix. US plan: SP $68.5K, SB $8.8K, SB video $8.9K, SD $1.9K. SB video sits mostly on Bamboo 6 Pc, Bamboo 4 Pc and CooLinens Cooling Sheets and Pillowcases. Canada is 98% SP.",
         "Aligned with the growth plan: each product's TACoS sits inside its growth-plan band (scaled for the deal), never above break-even. Sleephoria Cooling Fitted, Sleephoria Bamboo 6 Pc and CA Bamboo 6 Pc are raised to the growth floor; Maintenance products are held to the 12% band ceiling (Sleep Sanctuary Satin 4 Pc down from 21%, Satin Fitted, CA Satin 4 and 6 Pc).",
         "Over the cap today, bring down before Nov 19. US: CooLinens Pillowcases (53% vs 14%), Sleephoria Cooling Pillowcase (52% vs 19%), Silk Pillowcase (32% vs 25%), Decolure Cooling 4 Pc (31% vs 23%), Sleephoria Cooling 4 Pc (30% vs 25%), Sleep Sanctuary Satin 4 Pc (21% vs 12%), Satin 4 Pc, Satin 6 Pc and Satin Fitted (13-18% vs 12%). Canada: Satin 4 Pc (20%), Satin 6 Pc (17%), Satin Fitted (16%) and Sleep Sanctuary Satin 4 Pc (15%), all vs 12%. US Bamboo 6 Pc sits right at its 19% cap.",
         "Decisions for Joseph: CooLinens Pillowcases is a Launch product (band 25-40%) but at the $15.19 deal break-even only allows 14%, so it is capped at 14%. CooLinens Cooling Sheets has no deal but sales doubled in two weeks: the plan holds today's ~$740 a day (33% TACoS, inside its Launch band).",
         "No ads beyond brand defence on Linen Curtains and Quilt Set (they lose money or make about 1% per unit at the deal price before ads).",
         "History check (2025 vs 2026 check tab): in BFCM 2025 we spent 1.6x (US) / 2.3x (CA) more per day than in the same 14 days before; sales rose 2.9x / 3.2x and TACoS fell from 14.6% to 8.2% (US). Doing the same from today gives US $72.8K / C$19.7K. The plan is higher because the demand read expects a bigger jump (3.5x US, 4.1x CA). Suggest: approve the history level as the base daily budget and the plan as the ceiling; the agent releases the extra only while each product stays under its TACoS cap on actual sales.",
         "Where we stand vs last year (same 14 days): US sales -32%, traffic -34%, ad spend -4%, so TACoS is 20.5% vs 14.6%; clicks are 27% cheaper and conversion is unchanged (6.7%). Canada: sales -46%, traffic -56%, spend -37%. After BFCM 2025 spend stayed about 1.5x for two weeks at 11% TACoS (Dec 1 - 15 is outside this budget).",
         "Every number is an estimate from the demand read, the Oct 27 deal prices and the last 14 days of spend and sales by ad type. Amazon's deal prices can still change until Nov 13; the plan is re-run if they do."]
for t in CALLS:
    c = sm.cell(row=rr, column=1, value="• " + t); c.alignment = WRAP; sm.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=4); sm.row_dimensions[rr].height = 30; rr += 1
rr += 1
sm.cell(row=rr, column=1, value="Tabs").font = F(size=11, bold=True, color=NAVY); rr += 1
for t in ["Budget by product: units, price, break-even, ceiling, plan TACoS and budget for every product.", "Budget by day: each product's budget spread over Nov 19 - 30.",
          "Bid and placement rules: deal-day bids, top of search, what the agent does hourly and what a person checks.", "Ad types by product: SP, SB, SB video and SD spend per product, TACoS now and the BFCM split.", "2025 vs 2026 check: before / during / after BFCM 2025 vs 2026 so far (sales, spend, TACoS, traffic) and the two history checks.", "Inputs: BFCM 2025 by day and the sources."]:
    c = sm.cell(row=rr, column=1, value="• " + t); sm.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=4); rr += 1
for ws in wb.worksheets:
    for row_ in ws.iter_rows():
        for c in row_:
            if c.font is None or c.font.name != "Arial":
                c.font = Font(name="Arial", size=c.font.size or 9, bold=c.font.bold, italic=c.font.italic, color=c.font.color)
wb.move_sheet(HC, offset=1 - wb.sheetnames.index(HC))
wb.save(OUT); print("saved", OUT)
