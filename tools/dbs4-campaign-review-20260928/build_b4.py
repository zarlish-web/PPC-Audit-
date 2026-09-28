"""B4 — campaign-by-campaign review of run 20260928-9e6e6bb5 (docx + xlsx register)."""
import json, os, re
from collections import Counter, defaultdict
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

S = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(f'{S}/a.json'))
RV = json.load(open(f'{S}/review.json'))
ROWS = json.load(open(f'{S}/rows.json'))
SALES = json.load(open(f'{S}/child_sales.json'))
INV = {r['sku']: r for r in json.load(open(f'{S}/inventory_children.json'))}
OUT = os.environ.get('OUT', '/home/user/PPC-Audit-/docs/DBS4_Campaign_Review_20260928-9e6e6bb5.docx')
NAVY = RGBColor(0x1F, 0x3A, 0x5F); GREY = RGBColor(0x55, 0x55, 0x55)
_T = json.load(open(f'{S}/child_margin.json'))['base']
BE_RUN = A['brief']['sections']['margin']['be_acos']
BE = sum(x['margin_before_ads'] for x in _T) / sum(x['sales'] for x in _T)   # redline §1: realised margin before ads ÷ sales, 30 days outside any deal

doc = Document()
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
for lvl, size in ((1, 15), (2, 12.5), (3, 11)):
    h = doc.styles[f'Heading {lvl}']; h.font.name = 'Calibri'; h.font.size = Pt(size); h.font.color.rgb = NAVY
sec = doc.sections[0]
for m in ('left_margin', 'right_margin'):
    setattr(sec, m, Cm(1.8))
sec.top_margin = sec.bottom_margin = Cm(1.6)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill); tcPr.append(s)


def runs(p, text, bold=False, size=None, color=None):
    for part in re.split(r'(\*\*[^*]+\*\*)', text):
        if not part:
            continue
        b = bold
        if part.startswith('**') and part.endswith('**'):
            part, b = part[2:-2], True
        r = p.add_run(part); r.bold = b
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p


def para(t='', **k):
    p = doc.add_paragraph(); runs(p, t, **k); p.paragraph_format.space_after = Pt(4); return p


def lead(l, t):
    p = doc.add_paragraph(); r = p.add_run(l + ' '); r.bold = True; r.font.color.rgb = NAVY; runs(p, t); p.paragraph_format.space_after = Pt(4); return p


def bullet(t):
    p = doc.add_paragraph(style='List Bullet'); runs(p, t); p.paragraph_format.space_after = Pt(2); return p


def table(headers, rows, widths=None, size=8):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = ''
        r = c.paragraphs[0].add_run(str(h)); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shade(c, '1F3A5F')
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ''; runs(cells[i].paragraphs[0], '' if v is None else str(v), size=size)
            if ri % 2: shade(cells[i], 'F2F5F9')
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def pct(x, d=0):
    return '—' if x is None else f'{x * 100:.{d}f}%'


def usd(x, d=2):
    return '—' if x is None else f'${x:,.{d}f}'


def f1(x, d=1):
    return '—' if x is None else f'{x:.{d}f}'


def short(n):
    return re.sub(r'^DBS4-SP-', '', n)


sec_no = [0]; part = ['A']


def section(t):
    sec_no[0] += 1; doc.add_heading(f'{part[0]}.{sec_no[0]} {t}', 1)


RK = [r for r in RV if r.get('ceil_tos') is not None]
NR = [r for r in RV if r.get('ceil_tos') is None]
iss = lambda r, k: [i for i in r['issues'] if i.startswith(k)]

# ================================================================ title
t = doc.add_paragraph(); runs(t, 'B4 — campaign-by-campaign review of the 28 September run', bold=True, size=17, color=NAVY)
para('Decolure Bamboo Sheets 4-Piece · run 20260928-9e6e6bb5 · reviewed against “Bids and Placements on Exact Campaigns” (25 September revision, with the 28 September redline) · data to 27 September', size=9, color=GREY)
para(f"Every enabled campaign in the run — {len(RV)} of them — was re-read on its own numbers: objective, advertised SKU, clicks, impressions, CTR, CVR, spend, CPC and orders over 90, 30, 14 and 7 days and the month before the deal; top-of-search clicks and share, product-page share, top-of-search impression share on its keyword, the required clicks for its target rank, the 7-day median rank against target; and the bid, modifier, budget, placement and SKU the run proposes. B4 is judged on its own data only. Where the run, or the 25 September corrections, got a decision wrong, it is flagged and corrected here rather than carried forward.")
lead('Decisions applied (operator, 28 September).', '(1) The Best Deal ended on 28 September and the next dated deal is 26 October, so no ranking campaign has the velocity window a funded push needs: every ranking campaign is priced in maintenance — top of search at its own ceiling, no premium — until a push is funded again. (2) Ranking campaigns advertise White; where White cannot carry the traffic, the size’s highest-selling variation with healthy stock carries it until White lands. (3) Queen: White already sells well without its own ads and has 15 days of Available stock (82 units) against a 27 October arrival, so Queen ranking moves to the next seller with healthy stock. (4) Auto, Broad and Phrase campaigns advertise the size’s LTSF SKU, never White — the LTSF list is still to come (the tools reachable here carry no inventory age); every Auto/Broad/Phrase campaign on White is flagged now and the SKU is named once the list is in. (5) King joins B4’s focus for a King White push — but only on the King terms the push actually needs and can carry (A.2); every other King campaign stays in maintenance. (6) The 28 September redline of the framework is applied throughout: contribution is the realised margin before ads from Sellerboard; the planning rate comes from the same size and pack; a zero-order read becomes evidence once three orders were expected; the rank gap is counted in positions; the market bound is never a campaign’s own CPC; the requirement counts only incremental units and passes a reach and a sum check; budgets include the product-page clicks; a term another Decolure product also bids carries no premium until its family owner is named. The Best Deal of 15–28 September is confirmed in Seller Central (752 units, $53,568).')

# ================================================================ Part A — logic errors
doc.add_heading('Part A — What the run (and the earlier corrections) got wrong', 1)

# A.1 pricing after the deal
_DP = {p['date']: p for p in json.load(open(f'{S}/b46/b4_daily.json'))['points']}
_tk = [k for k in _DP if '2026-08-29' <= k <= '2026-09-27' and _DP[k].get('tacos')]
_tac30 = sum(_DP[k]['spend'] for k in _tk) / sum(_DP[k]['spend'] / (_DP[k]['tacos'] / 100) for k in _tk) * 100
_t7 = [k for k in _tk if k >= '2026-09-21']
_tac7 = sum(_DP[k]['spend'] for k in _t7) / sum(_DP[k]['spend'] / (_DP[k]['tacos'] / 100) for k in _t7) * 100
section('Ranking prices after the deal — maintenance, not a push')
above = [r for r in RK if r.get('tos_price') and r['tos_price'] > r['ceil_tos'] * 1.005]
run_up = [r for r in RK if r.get('run_price') and r.get('tos_price') and r['run_price'] > r['tos_price'] + 0.01]
run_up_above = [r for r in run_up if r['run_price'] > r['ceil_tos']]
lead('The rule.', f'Top of search may sit above its ceiling (contribution × the campaign’s blended top-of-search conversion) only on a funded push. Contribution is the realised margin before ads on the serving child — Sellerboard sales less product cost, every Amazon fee (storage and LTSF included), refunds and promotions — over the 30 days before the deal (15 Aug → 13 Sep), because the go-forward price is the non-deal one. It is far below what the run priced on: King White earns $17.88 a unit before ads (the run used $24.49 for the product, the catalogue $30.59 for King White), and the product as a whole $20.64 — a break-even ACoS of {pct(BE, 1)}, not the run’s {pct(BE_RUN, 1)}. A push must be sized, dated, ceilinged, predicted and funded, and it needs all four conditions: a velocity window, CTR above market, CVR above market, stock to hold the position. The velocity window closed with the deal on 28 September. Without it a campaign is in maintenance: top of search at its ceiling, no premium, the 70/20 mix, and a real modifier. A price above the ceiling comes down to it as a decision in its own right — straight there on a row with no top-of-search clicks, in steps of at most 50% on a row that has them.')
lead('Posture first.', f"The framework now reads the product’s TACoS against its stage band before any premium is sized. B4 ran {_tac30:.1f}% over the last 30 days and about {_tac7:.0f}% in the deal’s last week, against an 18% ranking-band ceiling (the 25 September ruling; SOP-26’s own band is not in the run file — confirm it). That is elevated, not a breach, so premiums are allowed where everything else holds — but see below: on B4 today nothing else holds.")
lead('What the run does.', f"It keeps pushing: of {len(RK)} ranking campaigns read, {len(above)} sit above their ceiling today, and the run raises the top-of-search price on {len(run_up)} — {len(run_up_above)} of them to a price above the ceiling. Its own rows cite ‘the press’ and the operator’s focus, not a funded window.")
lead('What the 25 September corrections did — also wrong now.', 'They pushed every in-focus campaign daily by the delivery gap, bounded by a loss stop of 3× contribution per order. That was sized for the deal. After 28 September it has no velocity window behind it and the framework does not allow a premium; the loss stop is replaced by the ceiling.')
ex = sorted([r for r in above if r['d30']['spend']], key=lambda r: -r['d30']['spend'])[:5]
table(['Campaign', 'Focus', 'Ceiling (rate basis)', 'TOS price now', 'Run writes', 'Corrected (this write → end point)'],
      [[short(r['campaign'])[:55], 'in' if r['focus'].startswith('IN') else 'out', f"{usd(r['ceil_tos'])} ({pct(r['tos_rate'], 1)}, {r['tos_src']})", usd(r['tos_price']), usd(r.get('run_price')), f"{usd(r.get('price_to'))} → {usd(r.get('descent_final') or r.get('price_to'))}"] for r in ex],
      widths=[6.2, 1.2, 4.2, 2, 2, 3.4], size=7.5)
lead('Correction.', 'Price every ranking campaign at its ceiling until a push is funded and dated (the 26 October deal is the next window). The base carries product pages; where product pages take more than 20% of clicks the base comes down toward what product pages afford and the modifier is re-solved to hold top of search. Re-open the push case for the in-focus terms that meet the other three conditions when the deal is confirmed — today that is “bamboo cooling sheets” and “king sheets bamboo cooling”; the Cal King terms do not yet show CVR above the market on a readable sample. The King White campaigns in A.2 are funded for volume at their ceiling; the redline leaves them no premium today.')

# A.2 King White push
section('King White push — only the terms that need it, and what the redline leaves of it')
KP = [r for r in RV if r.get('push')]
a = next(r for r in KP if r['push']['stage'] == 'push now'); b = next(r for r in KP if r['push']['stage'] != 'push now')
pa, pb = a['push'], b['push']
lead('The decision (operator, 28 September).', 'King White joins B4’s focus on the King terms that need a push and can carry one — not across all 108 King ranking campaigns. It is B4’s best-selling King child (220 units in 30 days), with 298 Available (29 days) and 1,448 in FC transfer, and it beats the market on click-through and conversion on its main King terms. Two campaigns were selected: “Bamboo Sheets King” to push now, and “Bamboo Sheets King Size” once its placement mix is fixed.')
lead('What the redline does to it.', f"Four of its changes land on this push at once. (1) Contribution is realised: King White earns ${a['contrib']:.2f} a unit before ads, so the ceiling on “bamboo sheets king” is {usd(a['ceil_tos'])}, not the $5.62 priced earlier. (2) The rank gap is {pa['positions']} positions, a lift of {pa['lift']:.2f}, so the gap would want {usd(pa['gap_wants'])}. (3) The market bound may no longer be the campaign’s own CPC plus 15%; the only reference allowed is the account’s $2.80 + 15% = {usd(pa['bound'])}, which sits below the ceiling — so it stops any premium outright. (4) B6 bids “bamboo sheets king” and “bamboo sheets king size” exact too, and the redline says the family owner prices a shared term while the other holds at its ceiling; no owner is named. Any one of (3) or (4) is enough: today the push cannot carry a premium.")
table(['', short(a['campaign'])[:48], short(b['campaign'])[:48]], [
    ['Stage', 'Funded volume at the ceiling', 'Fix the mix first'],
    ['Rank 08-28 → 09-14 → now · target', f"{a['rank_30']} → {a['rank_pre']} → {a['rank_now']} · {a['rank_tgt']}", f"{b['rank_30']} → {b['rank_pre']} → {b['rank_now']} · {b['rank_tgt']}"],
    ['TOS CTR / CVR vs market', f"{f1(a['tos_ctr'], 2)}% vs {a['mctr']}% · {f1(a['tos_cvr'])}% vs {a['mcvr']}%", f"{f1(b['tos_ctr'], 2)}% vs {b['mctr']}% · {f1(b['tos_cvr'])}% vs {b['mcvr']}%"],
    ['Mix (30 days) TOS / PP', f"{pct(a['d30']['tos_sh'])} / {pct(a['d30']['pp_sh'])}", f"{pct(b['d30']['tos_sh'])} / {pct(b['d30']['pp_sh'])} (14 days: 7% TOS)"],
    ['Contribution · ceiling', f"${a['contrib']:.2f} ({a['contrib_src']}) × {pct(a['tos_rate'], 1)} = {usd(a['ceil_tos'])}", f"${b['contrib']:.2f} × {pct(b['tos_rate'], 1)} = {usd(b['ceil_tos'])}"],
    ['Required TOS clicks/day', f"{pa['req_raw']} → {pa['req']} ({pa['req_basis']}); delivered {f1(a['deliv_14'])} (14d)", f"{pb['req_raw']} → {pb['req']} ({pb['req_basis']}); delivered {f1(b['deliv_14'])}"],
    ['Gap → lift → what the gap wants', f"{pa['positions']} positions → {pa['lift']:.2f} → {usd(pa['gap_wants'])}", f"{pb['positions']} positions → {pb['lift']:.2f} → {usd(pb['gap_wants'])}"],
    ['What stops it', pa['binds'], pb['binds']],
    ['This write', f"TOS {usd(a['tos_price'])} → {usd(pa['this_write'])} (to the ceiling); base {usd(a['base'])} held; modifier {a['tos_mod']}% → {a['mod_to']}%", f"base {usd(b['base'])} → {usd(b['base_to'])} (−25%, product pages carry orders); TOS {usd(b['tos_price'])} → {usd(pb['this_write'])}; modifier → {b['mod_to']}%"],
    ['Budget', f"${a['budget']:.0f} kept (the requirement needs ${pa['budget_need_day']}/day: {pa['req']} × {usd(pa['this_write'])} + the product-page clicks at the base)", f"unchanged until entry; at entry about ${pb['budget_day_at_target']}/day"],
    ['Dated', 'read 5 Oct; checkpoint 12 Oct', 'read 5 Oct: mix; entry once TOS ≥ 70% for 7 days'],
    ['What reverses it', 'delivery under 70% of the requirement at 12 Oct → fix delivery (budget, bid-strategy suppression), never a price cut below the ceiling; rank no better than 22 with delivery met → back to maintenance', 'mix not at 70% TOS after the base cut → second base step, then fixed bidding'],
], widths=[4.2, 6.8, 6.8], size=7.5)
lead('What would put a premium back — two decisions and one input.', f"(1) Name B4 the family owner of the King terms it shares with B6 (SOP-33), so B6 holds its ceiling on them. (2) Supply a per-term clearing price for top of search — Amazon’s suggested top-of-search bid for the term, or an auction read that is not our own CPC; the redline forbids building it from what we paid. With both, the push prices at the lower of {usd(pa['gap_wants'])} and that clearing price plus 15%, climbing at most 30% a write, one write a two-week cycle outside a deal (the redline’s cadence), and the loss per order is written on the row. (3) A weekly envelope for B4, set at the monthly review; the push is funded from it or written as a shortfall.")
lead('Also on “bamboo sheets king”.', 'Negative-exact the term in “LTSF-ALL-Broad-(Clearance)” (10 of its 50 clicks) and the VHSV Broad (1) so the exact row earns the rank credit, and check the down-only bid strategy is not pulling top of search back before any later raise.')
KW_REASON = [
    ('bamboo sheets', 'Not pushed — maintenance. The head term: realised contribution puts its ceiling at {c}, against {n} today; it needs {q} top-of-search clicks a day after the reach and sum checks. B6 bids it too. The deal already paid for it: $4,309 in 13 days at 81% ACoS moved it 38 → 30.'),
    ('cooling sheets king', 'Not pushed. Half its clicks go to product pages and its requirement is above what the auction holds; fix the mix at maintenance.'),
    ('king size cooling sheets', 'Not pushed. Passes CTR and CVR, but the demand is small (48 searches a month) at rank 42 against 11.'),
    ('bamboo king size sheets set', 'Not pushed. Passes CTR and CVR, but 21 searches a month.'),
    ('king bed bamboo sheets', 'Not pushed. Under 15 top-of-search clicks — conversion not read yet.'),
    ('king size bamboo sheets', 'Not pushed. 11 clicks, no orders — conversion not read.'),
    ('cooling sheets', 'Not pushed. The King child takes under 30% of its clicks at top of search, and CTR/CVR are not readable on it.'),
]
rows = []
for kw, why in KW_REASON:
    r = next((x for x in RV if x.get('kw') == kw and x.get('child') == 'BAMBOO-KING-WHITE' and x.get('ceil_tos') is not None), None) or next((x for x in RV if x.get('kw') == kw and x.get('preferred_child') == 'BAMBOO-KING-WHITE'), None)
    if r:
        rows.append([kw, f"{r.get('rank_now') or '—'} / {r.get('rank_tgt') or '—'}", 'yes' if r['conds']['ctr'] else '—', 'yes' if r['conds']['cvr'] else '—', usd(r['d30']['spend'], 0), why.format(c=usd(r.get('ceil_tos')), n=usd(r.get('tos_price')), q=f1(r.get('req_day')))])
lead('The King terms considered and left out.', 'Everything else on King White — collapsing, no rank on file, dead or thin — stays in maintenance as the register shows.')
table(['Term', 'Rank / target', 'CTR ok', 'CVR ok', 'Spend 30d', 'Why not in the push'], rows, widths=[3.4, 1.8, 1.2, 1.2, 1.6, 8.6], size=7.5)
lead('Stock and the engine flag.', 'PPC intensity is judged on Available stock only. King White has 298 Available — 29 days at today’s 10.3 a day — so it runs normally; its 1,461 reserved (1,448 FC transfer, 13 FC processing, 6 customer orders) count only for replenishment. The engine counts 228 units (22 days) and still marks the 26 King campaigns “held on a RED hero”; that is over the 7-day line on its own count, so the flag is wrong — override it on these two campaigns.')

# A.3 SKU
section('Ranking SKU — White, and the backup where White cannot carry it')
lead('The rule.', 'Ranking campaigns advertise White. Where White cannot carry the traffic — out of stock, or cover shorter than the time to the next arrival — the size’s highest-selling variation with healthy stock carries it until White lands, and the ads go back on arrival. Colour-specific terms (“black bamboo sheets”, “moss green sheets king”) advertise their own colour.')
size_rows = []
PREF = {'KING': 'BAMBOO-KING-WHITE', 'CALIFKING': 'BAMBOO-CALIFKING-WHITE', 'QUEEN': 'BAMBOO-QUEEN-LIGHTBLUE', 'FULL': 'BAMBOO-FULL-OLIVE', 'TWIN': 'BAMBOO-TWIN-NAVYBLUE'}
S30 = {r['sku']: r for r in SALES['d30']}
RUNPICK = Counter()
for x in A['decisions']:
    if x['kind'] == 'child' and x['verdict'] == 'change' and 'WHITE' in (x['current_at_audit'] or ''):
        RUNPICK[(x['current_at_audit'], x['suggested'])] += 1
for sz, nm in (('KING', 'King'), ('QUEEN', 'Queen'), ('CALIFKING', 'Cal King'), ('FULL', 'Full'), ('TWIN', 'Twin')):
    w = f'BAMBOO-{sz}-WHITE'; wi = INV.get(w, {}); ws = S30.get(w, {})
    top = sorted([r for r in SALES['d30'] if r['sku'].startswith(f'BAMBOO-{sz}-')], key=lambda r: -r['units'])
    rank_w = next((i + 1 for i, r in enumerate(top) if r['sku'] == w), None)
    runp = ', '.join(f"{b.split('-', 2)[2].title()} ({n})" for (a, b), n in RUNPICK.items() if a == w) or '—'
    p = PREF[sz]; pi = INV.get(p, {}); ps = S30.get(p, {})
    size_rows.append([nm, f"{ws.get('units', 0)} units (#{rank_w} in size); {wi.get('fba_available')} Available = {(wi.get('fba_available') or 0) / wi['velocity_day']:.0f} days; reserved {wi.get('reserved')} ({(wi.get('reserved_breakdown') or {}).get('fc_transfers', 0)} FC transfer, {(wi.get('reserved_breakdown') or {}).get('fc_processing', 0)} processing, {(wi.get('reserved_breakdown') or {}).get('customer_orders', 0)} customer orders); {wi.get('inbound')} inbound",
                      runp, p.split('-', 2)[2].title() + (f" — {ps.get('units')} units, {pi.get('fba_available')} Available = {(pi.get('fba_available') or 0) / pi['velocity_day']:.0f} days" if p != w else ' — keep')])
table(['Size', 'White: 30-day units · stock', 'The run moves ranking to', 'Ranking SKU (corrected)'], size_rows, widths=[1.6, 7.6, 3.4, 5.8], size=7.5)
para('Units are Sellerboard’s 30-day units by child (08-29 → 09-27); stock is Sellerboard on 28 September. PPC is judged on Available stock only (days = Available ÷ weighted velocity): under 5 days with reserved mostly FC transfer → throttle; under 5 days with reserved mostly customer orders → stockout risk; 7+ days → normal. Reserved FC transfer and FC processing count only for replenishment; customer orders never count. Arrivals: King White 16 Oct, Queen White 27 Oct, Full White 27 Oct (18 units), Twin White 16 Oct; Cal King White has 120 inbound with no date.', size=8, color=GREY)
lead('Where the run is wrong.', 'Queen → Olive, Full → Light Olive, Twin → Burgundy and Cal King → Burgundy are the hero rule picking the child with the most units on hand, not the next seller: Full Light Olive and Twin Burgundy are among the slowest-moving children in their sizes (261 and 665 days of stock) — candidates for the LTSF lane, not for ranking. Cal King White has about 30 days of cover and still sells — its move to Burgundy is not justified. King White has 298 Available (29 days), over the 7-day line, so King ranking stays on White and runs normally; the engine’s “held on a RED hero” flag on 26 King campaigns (the engine-check failure) is wrong even on its own 228-unit count (22 days). Twin White has 0 Available: its 154 reserved are FC transfers, sellable in about 3–10 days. Under the reserved-inventory rule that is a throttle, so Twin ranking comes off White now and runs on Navy Blue (57 available, 80 days) until the transfers show as Available, then goes back to White. The run’s choice of Burgundy is still wrong — Navy Blue is the better seller with the stock.')
lead('Queen White — why it moves.', 'Queen White is the size’s best seller (109 units in 30 days) and Amazon credits only 13 of them to its own ads — it sells without PPC, and its generic Queen ranks are falling (“bamboo sheets queen size” 36 → 45, “bamboo sheets queen” 53 → 67 on the 7-day median) while Available stock covers 15 days against a 27 October arrival. Pushing it through PPC drains stock it needs to keep selling; ranking moves to Light Blue (71 units, 202 Available = 57 days, 102 inbound) until White lands. Taupe (68 units, 846 inbound) is the second choice once its inbound lands. Caveat: Sellerboard’s PPC split credits only same-SKU ad sales, so the organic share is an upper bound.')
sku_iss = [r for r in RV if iss(r, 'SKU: ranking') or iss(r, 'SKU: the term')]
lead('Correction.', f"{len(sku_iss)} ranking campaigns advertise a child other than the size’s ranking SKU (the register names each). Re-point them by hand — the loader skips every swap — and date the switch back to White on each arrival.")

section('Stock — PPC runs on Available units only')
lead('The rule (28 September guideline).', 'Ads can only sell Available units. PPC intensity is judged on Available ÷ daily sales. Under 5 days with reserved mostly FC transfer → throttle: pause ranking and aggressive top-of-search campaigns, cut broad and low-efficiency spend, keep branded and proven exact winners on a lower budget, scale back once the transfers show as Available. Under 5 days with reserved mostly customer orders → stockout risk: cut hard, branded defence only, push replenishment. 7+ days → normal. Customer orders are never stock; FC transfer and FC processing count for replenishment only.')
SR = [r for r in RV if (r.get('situation') or '').startswith(('STOCK', 'LOW STOCK'))]
table(['Campaign', 'Advertised SKU', 'Available · days', 'Reserved (transfer / processing / orders)', 'Spend 7d', 'Decision'],
      [[short(r['campaign'])[:48], (r.get('child') or '').replace('BAMBOO-', ''), f"{r['stock']['avail']} · {f1(r['stock']['avail_days'])}", f"{r['stock']['res_transfer']} / {r['stock']['res_processing']} / {r['stock']['res_orders']}", usd(r['d7']['spend'], 0), r['action'][0]] for r in SR],
      widths=[5.2, 2.6, 1.8, 2.6, 1.2, 5], size=7.5)
lead('What the run does.', f"It keeps these campaigns spending on children customers cannot buy today — ${sum(r['d7']['spend'] for r in SR):.0f} in the last 7 days." + ' Every other advertised child has 7+ days of Available stock; the ranking SKUs are all clear (King White 29 days, Cal King White 28, Queen Light Blue 57, Full Olive 70, Twin Navy Blue 80). Queen White has 15 days Available — over the line; Queen stays on Light Blue on the organic-sales decision, not on stock.')

# A.3 objectives
section('Campaign objectives')
ob = Counter()
for r in RV:
    for i in iss(r, 'OBJECTIVE'):
        ob[re.sub(r'\d+', '#', i.split(':', 1)[1].strip())[:80]] += 1
lead('The rule.', 'The objective follows the targeting: Exact = Ranking, Auto/Broad/Phrase = Discovery (the LTSF clearance campaigns keep Liquidation), product targeting = Conversions, the brand term = Defensive — one objective per campaign. The objective decides how a campaign is priced and graded; a wrong tag prices a ranking term as a conversion campaign or the reverse.')
table(['Finding', 'Campaigns'], [[k, v] for k, v in ob.most_common()], widths=[14, 2.5], size=8)
lead('What it means.', 'The 53 Exact campaigns tagged Conversions are the “FIX”/tail exact rows — 18 of them are even named “(Ranking)”. Under the standard they are ranking campaigns: priced on the ranking ceilings above, placement-managed to 70/20, and read against a rank target where one exists; with no rank on file they sit at the ceiling with no premium, which is where a conversion campaign would sit too — so the retag changes their grading and their placement management, not their spend. The brand-term Exact campaigns tagged Ranking are Defensive: their job is to hold the brand shelf, not to climb. The Broad “Cooling Sheets” campaign tagged Ranking is Discovery — a broad row cannot own a term’s rank credit — and the two product-targeting campaigns tagged Ranking are Conversions. The run’s 34 retags of untagged campaigns are consistent with this rule where they tag Exact rows Ranking; the 19 it tags CONVERSIONS on Exact rows are not.')

# A.4 required clicks / traffic
section('Required clicks and whether the traffic exists')
tr = [r for r in RK if iss(r, 'TRAFFIC')]
withreq = [r for r in RK if r.get('req_day')]
lead('The rule.', 'Required top-of-search clicks a day = the units a day the market sells at the target rank ÷ the campaign’s top-of-search conversion (framework §7), split across the campaigns that carry the same term. That sets volume and budget — never the price. The shortfall is priced only when the budget is intact and impression share is low; where share is already high the requirement is re-based from actuals; and where winning every auction at today’s volume (delivered ÷ share) still falls short, the requirement is above what the auction holds.')
_PPS = json.load(open(f'{S}/postpass.json'))
lead('What the redline changes.', f"The requirement now counts only the units a term does not already sell (target units less the paid units it sells today; organic units per term are not in the data, so the figure is still an upper bound), is re-based to what winning every auction would buy, and must not add up past the product. On this product the terms’ incremental units add to {_PPS['terms_units_day']:.0f} a day against {_PPS['units_day']:.0f} sold in total, so every requirement is scaled by {_PPS['scale']:.2f}. The budget is the requirement at this write’s top-of-search price plus the product-page clicks it brings (about 3 for every 7) at the base.")
lead('What the data shows.', f"{len(withreq)} ranking campaigns carry a term with a DataRova target (target rank and units). {sum(1 for r in withreq if r.get('deliv_14') is not None and r['deliv_14'] >= 0.7 * r['req_day'])} deliver 70% or more of their requirement; {len(tr)} have a requirement above what the whole auction holds at today’s volume. The run’s own requirement (the “leaves PPC … clicks/wk” figure) is often a flat 40 a week per campaign; the market-sized figure is shown in the register beside what each campaign actually takes.")
ex = sorted(tr, key=lambda r: -(r['d30']['spend'] or 0))[:6]
table(['Campaign', 'Target rank · now', 'Required TOS/day', 'Delivered (14d)', 'TOS impr. share', 'Most the auction holds'],
      [[short(r['campaign'])[:50], f"{r.get('rank_tgt') or '—'} · {r.get('rank_now') or '—'}", f1(r.get('req_day')), f1(r.get('deliv_14')), f"{f1(r.get('is30'))}%", f1(r.get('reach_day'))] for r in ex], widths=[6.5, 2.4, 2.2, 2.2, 2.2, 2.6], size=7.5)
lead('Correction.', 'Grade these on impression share and rank, not on a click count the auction cannot supply, and re-base their requirement; they are not reasons to raise price.')

# A.5 placement / ROS / distribution
section('Placement — where the clicks land')
lk = [r for r in RK if 'LEAK' in (r.get('situation') or '') or 'NOT A RANKING' in (r.get('situation') or '')]
ros = [r for r in RV if any('ROS modifier' in i for i in r['issues'])]
lead('The rule.', 'Ranking campaigns aim for 70–90% of clicks at top of search and product pages at or under 20%. Over 20% → the base comes down toward what product pages afford (≤50% a write, ≤25% where product pages carry orders) and the modifier is re-solved so top of search holds; under 30% at top of search that fix takes precedence over any price or budget move. Rest of search stays at 0% until it earns a lift on 15+ clicks converting at or above the product-page rate.')
lead('What the data shows.', f"{sum(1 for r in lk if 'NOT A RANKING' in r['situation'])} ranking campaigns take under 30% of their clicks at top of search, and {sum(1 for r in lk if 'LEAK' in r['situation'])} more lose over 20% to product pages. {len(ros)} carry a rest-of-search modifier that has not been earned.")
ex = sorted(lk, key=lambda r: -(r['d30']['spend'] or 0))[:6]
table(['Campaign', 'Clicks 30d', 'TOS / PP share', 'Base now → corrected', 'TOS price now → corrected', 'The run'],
      [[short(r['campaign'])[:50], r['d30']['clicks'], f"{pct(r['d30']['tos_sh'])} / {pct(r['d30']['pp_sh'])}", f"{usd(r.get('base'))} → {usd(r.get('base_to'))}", f"{usd(r.get('tos_price'))} → {usd(r.get('price_to'))}", '; '.join(r['run'][:2]) or 'holds'] for r in ex], widths=[6, 1.4, 2.2, 3, 3, 3.6], size=7.5)

# A.5b keywords and search terms
section('Keywords and search terms — one owner per ranking term')
st_r = [r for r in RV if iss(r, 'SEARCH TERM') and r.get('ceil_tos') is not None]
st_b = [r for r in RV if iss(r, 'SEARCH TERM') and r['match'] in ('Auto', 'Broad', 'Phrase')]
kd = [r for r in RV if iss(r, 'KEYWORD')]
lead('The rule.', 'A ranking term earns rank credit only through the exact campaign that owns it. Where an Auto, Broad or Phrase campaign also buys the term, the exact row is not earning its own credit (framework §12) — the term is negative-exact in the broad/auto campaign. Two enabled exact campaigns on the same term split the read; one keeps it.')
lead('What the data shows.', f"{len(st_r)} ranking terms are also bought by broad or auto campaigns, and {len(st_b)} broad/auto/phrase campaigns buy exact ranking terms. The largest is the clearance campaign “DBS6-SP-LTSF-ALL-Broad” (advertising B4’s Queen Olive), which took 164 clicks on “bamboo sheets” ($409 in 30 days) and clicks on most of the other ranking terms. {len(kd)} campaigns share an exact term with another enabled exact campaign.")
table(['Campaign', 'What it buys (30 days)'], [[short(r['campaign'])[:55], iss(r, 'SEARCH TERM')[0].split(' — ', 1)[-1][:150]] for r in sorted(st_b, key=lambda r: -(r['d30']['spend'] or 0))], widths=[6.5, 11], size=7.5)
lead('Correction.', 'Negative-exact every ranking term in the Auto, Broad and Phrase campaigns that buy it (the register lists each), starting with the LTSF Broad; keep one exact owner per term — the campaign on the ranking SKU with the clicks — and pause the duplicate. The run proposes negative-wall changes on the three clearance campaigns (seq 2338, 2339, 2347); check each wall adds the ranking terms that campaign buys rather than removing them.')

ME, OTHER, OTHER_DIR = 'B4', 'B6', 'b6v3'
# shared-term section, inserted into both builders; ME / OTHER are 'B4' / 'B6'
section('Terms B4 and B6 both bid — one family owner per term')
_other = json.load(open(f'{S}/../{OTHER_DIR}/review.json'))
def _best(rows, kw):
    xs = [r for r in rows if r.get('kw') == kw and r.get('ceil_tos') is not None]
    return max(xs, key=lambda r: r['d30']['spend']) if xs else None
_sh = sorted({r['kw'] for r in RV if r.get('sibling') and r.get('kw')})
_rows = []
for kw in _sh:
    m, o = _best(RV, kw), _best(_other, kw)
    if not (m and o):
        continue
    mo, oo = m['d30']['tos_o'], o['d30']['tos_o']
    mc, oc = m['d30']['tos_c'], o['d30']['tos_c']
    sug = ME if (mo, m['d30']['spend']) >= (oo, o['d30']['spend']) else OTHER
    _rows.append((m['d30']['spend'] + o['d30']['spend'], [kw, f"{m.get('rank_now') or '—'} / {o.get('rank_now') or '—'}", f"${m['d30']['spend']:,.0f} · {mc} → {mo}", f"${o['d30']['spend']:,.0f} · {oc} → {oo}", sug]))
_rows.sort(key=lambda t: -t[0])
lead('The rule (redline, 28 September).', 'Where another Decolure product bids the same term, the family owner prices it (SOP-33) and the others hold at their ceiling with no top-of-search premium. A ceiling computed as if the sibling were not in the auction is too high for both, and each one’s raise is a bid against the other.')
lead('What the data shows.', f"{ME} and {OTHER} both run enabled exact campaigns on {len(_sh)} of {ME}’s ranking terms ({sum(1 for r in RV if r.get('sibling'))} {ME} ranking campaigns). No owner is named for any of them, so no premium is allowed on either side until one is. The suggestion below gives each term to the product that took more top-of-search orders on it in the last 30 days — a starting point for the operator’s ruling, not the ruling.")
table(['Term', f'Rank {ME} / {OTHER}', f'{ME}: spend · TOS clicks → orders', f'{OTHER}: spend · TOS clicks → orders', 'Suggested owner'], [r for _, r in _rows[:18]], widths=[4.4, 2.2, 3.8, 3.8, 2.2], size=7.5)
lead('Correction.', f"Name an owner per shared term. The non-owner keeps its campaign at its ceiling (it still sells), takes no premium, and is not raised against the owner; where the owner is the other product and this product’s campaign adds nothing, pause it. All {len(_rows)} shared terms are in the register (“SIBLING”).")

# A.6 non-ranking
section('Other campaign types — inside their own ceilings')
wrong = [r for r in NR if any(i.startswith('RUN:') or i.startswith('MISSING') for i in r['issues'])]
lead('The rule.', f'Conversions, Discovery, Defensive and Liquidation campaigns are priced inside their ceiling: a click may cost contribution × that campaign’s conversion, an ACoS at or under break-even ({pct(BE, 1)}). Read on 30 days against 90. Over the ceiling the base comes down; inside it nothing moves, including the top-of-search modifier; under 15 clicks there is no readable rate and nothing moves. Clearance campaigns are priced on the storage fee they avoid.')
lead('What the run does.', f"{len(wrong)} go against the rule — mostly cuts to campaigns that are inside their ceiling or too thin to read.")
table(['Campaign', 'Objective', 'Clicks / orders 30d', 'ACoS 30d (90d)', 'The run', 'Corrected'],
      [[short(r['campaign'])[:48], r['objective'], f"{r['d30']['clicks']} / {r['d30']['orders']}", f"{pct(r.get('acos30'))} ({pct(r.get('acos90'))})", '; '.join(r['run'][:2]) or 'holds', (r.get('action') or [''])[0][:70]] for r in sorted(wrong, key=lambda r: -(r['d30']['spend'] or 0))[:10]],
      widths=[5.4, 2, 2.2, 2.4, 3.4, 4.8], size=7.5)

# A.7 rows that should not load
section('Rows in the change file that should not load')
CS = {c['campaign_id']: c for c in A['campaigns']}
ch = [x for x in A['decisions'] if x['verdict'] == 'change']
pz = [x['seq'] for x in ch if x['kind'] in ('tos', 'bid', 'ros', 'pp', 'budget') and CS.get(x['campaign_id'], {}).get('status') == 'PAUSED']
ms = [x for x in ch if x['kind'] in ('tos', 'bid', 'budget', 'ros', 'pp', 'state') and x.get('campaign_id') and x['campaign_id'] not in CS]
wh = [r['seq'] for r in ROWS if r['verdict'] == 'change' and r['withheld']]
wl = [x for x in ch if x['kind'] == 'negatives' and not x['campaign'].startswith('DBS4')]
bullet(f"**{len(wh)} rows the engine itself withholds** (their text says “change → HOLD”) but export as changes: seq {', '.join(map(str, wh))}.")
bullet(f"**{len(pz)} writes on campaigns paused at the audit**: seq {', '.join(map(str, pz))}.")
bullet(f"**{len(ms)} rows on {len({x['campaign_id'] for x in ms})} campaigns the export does not carry** (they appear in Amazon’s placement report with 83 clicks in 90 days between them): hold every raise until each campaign’s status, child and targets are confirmed; the cuts stand, flagged.")
bullet(f"**{len(wl)} negative walls on clearance campaigns outside the DBS4 set** (seq {', '.join(str(x['seq']) for x in wl)}) — send to the LTSF owner.")
bullet('**All 64 SKU swaps skip at load** (the loader has no product-ad roster) — the SKU corrections in A.3 are manual.')
bullet('**Engine check, 2 failures**: the 26 King campaigns “on a RED hero” (see A.2 and A.3 — King White has 29 days of Available stock), and a video probe placed beside a Sponsored Brands probe on the same group (R14) — hold that build.')

# ================================================================ Part B — register
new = doc.add_section(); new.orientation = WD_ORIENT.LANDSCAPE
new.page_width, new.page_height = sec.page_height, sec.page_width
for m in ('left_margin', 'right_margin'):
    setattr(new, m, Cm(1.2))
part[0] = 'B'; sec_no[0] = 0
doc.add_heading('Part B — Every campaign, one row each', 1)
para('Sorted by objective, then 30-day spend. Clicks/CTR/CVR/ACoS are 30 days (08-29 → 09-27); TOS/PP are the share of clicks at top of search and on product pages; Req/Del are required vs delivered top-of-search clicks a day (14 days); IS is top-of-search impression share on the campaign’s keyword (30 days). Price = the top-of-search price (base × (1 + modifier)); “now → corrected” is this write. The last column is the corrected decision; “!” marks what the run or the earlier corrections got wrong.', size=8, color=GREY)
order = {'Ranking': 0, 'Conversions': 1, 'Discovery': 2, 'Defensive': 3, 'Liquidation': 4}


def verdict(r):
    bits = []
    if r.get('situation'):
        bits.append(r['situation'])
    if r.get('ceil_tos') is not None and r.get('price_to') is not None:
        bits.append(f"TOS {usd(r.get('tos_price'))} → {usd(r['price_to'])}" + (f" (then {usd(r['descent_final'])})" if r.get('descent_final') and abs(r['descent_final'] - r['price_to']) > 0.01 else '') + (f"; base {usd(r.get('base'))} → {usd(r.get('base_to'))}" if r.get('base_to') and r.get('base') and abs(r['base_to'] - r['base']) > 0.004 else '') + (f"; mod {r['mod_to']}%" if r.get('mod_to') is not None else ''))
    elif r.get('action'):
        bits.append(r['action'][0])
    for fx in r.get('fixes', []):
        bits.append(fx)
    for i in r['issues']:
        if i.startswith(('RUN', 'MISSING', 'OBJECTIVE', 'SKU', 'TRAFFIC', 'SEARCH TERM', 'KEYWORD', 'ROS')):
            bits.append('! ' + i)
    return '. '.join(bits)[:520]


rows = []
for r in sorted(RV, key=lambda r: (order.get(r['objective'], 9), -(r['d30']['spend'] or 0))):
    d = r['d30']
    rows.append([short(r['campaign'])[:60], f"{r['objective'][:4]}→{(r.get('obj_expected') or r['objective'])[:4]}" if r.get('obj_expected') and r.get('obj_expected') != r['objective'] else r['objective'][:4],
                 (r.get('child') or '—').replace('BAMBOO-', ''), f"{d['clicks']}/{f1(d['ctr'], 2)}%/{f1(d['cvr'])}%", usd(d['spend'], 0), pct(d['acos'] / 100 if d['acos'] is not None else None),
                 f"{pct(d['tos_sh'])}/{pct(d['pp_sh'])}", f"{r.get('rank_now') or '—'}/{r.get('rank_tgt') or '—'}", f"{f1(r.get('req_day'))}/{f1(r.get('deliv_14'))}",
                 f1(r.get('is30')), '; '.join(r['run'][:3]) or 'holds', verdict(r)])
table(['Campaign', 'Obj', 'SKU', 'Clk/CTR/CVR', 'Spend', 'ACoS', 'TOS/PP', 'Rank/tgt', 'Req/Del', 'IS', 'The run', 'Corrected decision'], rows,
      widths=[5.2, 1.3, 2.4, 2.2, 1.2, 1.1, 1.5, 1.3, 1.4, 0.9, 3.2, 8.5], size=6)

doc.save(OUT); print('saved', OUT)

# ================================================================ xlsx register
import openpyxl
from openpyxl.styles import Font, PatternFill
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Every campaign'
hdr = ['Campaign', 'Campaign ID', 'Status', 'Objective', 'Objective (standard)', 'Match', 'Advertised SKU', 'Ranking SKU for size', 'Focus', 'Budget', 'Budget use 7d',
       'Impr 30d', 'Clicks 30d', 'CTR 30d', 'Orders 30d', 'CVR 30d', 'Spend 30d', 'CPC 30d', 'ACoS 30d', 'Clicks 90d', 'Orders 90d',
       'TOS clicks 30d', 'TOS share 30d', 'PP share 30d', 'TOS clicks pre-deal/day', 'TOS clicks/day 14d',
       'Keyword', 'Rank 30d ago', 'Rank now', 'Target rank', 'Units/day at target', 'Required TOS clicks/day', 'Most the auction holds/day', 'TOS impr share 30d',
       'Contribution', 'TOS rate', 'TOS rate basis', 'PP rate', 'TOS ceiling', 'PP ceiling (base)', 'Base now', 'TOS mod now', 'TOS price now', 'Run TOS price',
       'Corrected TOS price (this write)', 'End point', 'Corrected base', 'Corrected modifier',
       'Situation', 'Action', 'The run', 'Issues', 'Fixes']
ws.append(hdr)
for r in sorted(RV, key=lambda r: (order.get(r['objective'], 9), -(r['d30']['spend'] or 0))):
    d = r['d30']
    ws.append([r['campaign'], r['cid'], r['status'], r['objective'], r.get('obj_expected'), r['match'], r.get('child'), r.get('preferred_child'), r['focus'], r.get('budget'), r.get('util7'),
               d['impr'], d['clicks'], d['ctr'], d['orders'], d['cvr'], d['spend'], d['cpc'], d['acos'], r['d90']['clicks'], r['d90']['orders'],
               d['tos_c'], d['tos_sh'], d['pp_sh'], r.get('deliv_pre'), r.get('deliv_14'),
               r.get('kw'), r.get('rank_30'), r.get('rank_now'), r.get('rank_tgt'), r.get('units_day'), r.get('req_day'), r.get('reach_day'), r.get('is30'),
               r.get('contrib'), r.get('tos_rate'), r.get('tos_src'), r.get('pp_rate'), r.get('ceil_tos'), r.get('ceil_pp'), r.get('base'), r.get('tos_mod'), r.get('tos_price'), r.get('run_price'),
               r.get('price_to'), r.get('descent_final'), r.get('base_to'), r.get('mod_to'),
               r.get('situation'), ' | '.join(r.get('action') or []), ' | '.join(r['run']), ' | '.join(r['issues']), ' | '.join(r.get('fixes') or [])])
for cell in ws[1]:
    cell.font = Font(bold=True, color='FFFFFF'); cell.fill = PatternFill('solid', fgColor='1F3A5F')
ws.freeze_panes = 'B2'; ws.auto_filter.ref = ws.dimensions; ws.column_dimensions['A'].width = 60
w2 = wb.create_sheet('Child sales & stock')
w2.append(['SKU', 'Units 30d', 'PPC units 30d (Sellerboard)', 'Organic units 30d (Sellerboard)', 'Units pre-deal', 'FBA available', 'Reserved', 'Inbound', 'Velocity/day', 'Days of stock'])
pre = {r['sku']: r for r in SALES['pre']}
for r in sorted(SALES['d30'], key=lambda r: (r['sku'].split('-')[1], -r['units'])):
    i = INV.get(r['sku'], {})
    w2.append([r['sku'], r['units'], r['ppc_units'], r['organic_units'], (pre.get(r['sku']) or {}).get('units'), i.get('fba_available'), i.get('reserved'), i.get('inbound'), i.get('velocity_day'), i.get('days_of_stock')])
for cell in w2[1]:
    cell.font = Font(bold=True, color='FFFFFF'); cell.fill = PatternFill('solid', fgColor='1F3A5F')
XL = OUT.replace('.docx', '.xlsx'); wb.save(XL); print('saved', XL)
