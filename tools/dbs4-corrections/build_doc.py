import json, re, statistics, os
from collections import Counter, defaultdict
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

S = os.path.dirname(os.path.abspath(__file__))
O = json.load(open(f'{S}/analysis.json'))
ROWS = json.load(open(f'{S}/rows.json'))
A = json.load(open(f'{S}/a.json'))
OUT = os.path.join(S, '..', '..', 'docs', 'DBS4_Bids_Placements_Corrections_20260921-dbcd48b8.docx')

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x55, 0x55, 0x55)
RED = RGBColor(0xB0, 0x1E, 0x1E)
GREEN = RGBColor(0x1E, 0x7B, 0x34)
SEV_FILL = {'Critical': 'F4CCCC', 'High': 'FCE5CD', 'Medium': 'FFF2CC', 'OK': 'D9EAD3'}


def pct(x, d=0):
    return '—' if x is None else f'{x*100:.{d}f}%'


def usd(x):
    return '—' if x is None else f'${x:,.2f}'


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


from findings import trunc


def short(name):
    return name.replace('DBS4-SP-', '')


doc = Document()
st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(9.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
for lvl, size in ((1, 16), (2, 13), (3, 11)):
    h = doc.styles[f'Heading {lvl}']
    h.font.name = 'Calibri'
    h.font.size = Pt(size)
    h.font.color.rgb = NAVY
    h.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
sec = doc.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
for m in ('left_margin', 'right_margin'):
    setattr(sec, m, Cm(1.6))
sec.top_margin = sec.bottom_margin = Cm(1.4)
# footer page number
fp = sec.footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = fp.add_run('DBS4 · run 20260921-dbcd48b8 · corrections against "Bids and placements on Exact campaigns" · page ')
r.font.size = Pt(8); r.font.color.rgb = GREY
for t, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    run = fp.add_run()
    run.font.size = Pt(8)
    if t:
        e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), t); run._r.append(e)
    else:
        e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = txt; run._r.append(e)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    s = OxmlElement('w:shd'); s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill)
    tcPr.append(s)


def para(text='', bold=False, italic=False, size=None, color=None, space_after=3, style=None):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    if text:
        add_runs(p, text, bold=bold, italic=italic, size=size, color=color)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    return p


def add_runs(p, text, bold=False, italic=False, size=None, color=None):
    # **bold** segments
    parts = re.split(r'(\*\*[^*]+\*\*)', text)
    for part in parts:
        if not part:
            continue
        b = bold
        if part.startswith('**') and part.endswith('**'):
            part, b = part[2:-2], True
        run = p.add_run(part)
        run.bold = b; run.italic = italic
        if size: run.font.size = Pt(size)
        if color: run.font.color.rgb = color
    return p


def bullet(text, level=0):
    p = doc.add_paragraph(style='List Bullet' if level == 0 else 'List Bullet 2')
    add_runs(p, text)
    p.paragraph_format.space_after = Pt(1)
    return p


def labelled(label, text, color=NAVY):
    p = doc.add_paragraph()
    r = p.add_run(label + ' ')
    r.bold = True; r.font.color.rgb = color
    add_runs(p, text)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.4)
    return p


def table(headers, rows, widths=None, size=8, header_fill='1F3A5F', zebra=True, fills=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = ''
        run = c.paragraphs[0].add_run(str(h)); run.bold = True; run.font.size = Pt(size); run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(c, header_fill)
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ''
            add_runs(cells[i].paragraphs[0], '' if v is None else str(v), size=size)
            if fills and fills[ri]:
                shade(cells[i], fills[ri])
            elif zebra and ri % 2:
                shade(cells[i], 'F2F5F9')
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


# ============================ data prep ============================
det = [a for a in O if a['changes'] or any(f['sev'] != 'OK' for f in a['F'] if f['code'] != 'DEAL')]
clean = [a for a in O if a not in det]
by_cid = {a['cid']: a for a in O}
ch_rows = [r for r in ROWS if r['verdict'] == 'change' and r['kind'] in ('tos', 'bid', 'budget', 'pp', 'ros', 'state')]
margin = A['brief']['sections']['margin']
outcome = A['run']['outcome']


def placements_total(label):
    src = {}
    for line in open(f'{S}/data/placements_{label}.jsonl'):
        r = json.loads(line); src[r['campaignId']] = r
    t = {k: sum(((r['placements'].get(k) or {}).get('clicks') or 0) for r in src.values()) for k in ('tos', 'detail', 'other')}
    sp = sum(r['spend'] or 0 for r in src.values()); sa = sum(r['sales'] or 0 for r in src.values())
    od = sum(r['orders'] or 0 for r in src.values())
    return t, sp, sa, od


PT = {k: placements_total(k) for k in ('d90', 'pre_deal30', 'deal6')}
DAYS = {'d90': 90, 'pre_deal30': 31, 'deal6': 6}

def camp(sub):
    return next(a for a in O if a['name'].startswith('DBS4-SP-' + sub))


def pps(sub):
    return pct(camp(sub)['share']['detail'])


RK = [a for a in O if a['obj'] == 'Ranking' and 'Exact' in a['name'] and a['tot'] >= 15]
LEAK = [a for a in RK if a['share']['detail'] > 0.20]
LEAK_CUT = [a for a in LEAK if any(r['kind'] == 'bid' and fnum(r['to']) is not None and fnum(r['to']) < fnum(r['now']) for r in a['changes'])]
DD = O[0].get('deal_days', 6)
DEAL_LABEL = f"09-15 → 09-{14 + DD}"


# row verdicts -----------------------------------------------------
BAD = {'WITHHELD', 'FREEZE', 'NOOP'}


def row_verdict(a, r):
    """KEEP / CORRECT (value) / HOLD / DROP with the reason codes that touch the row."""
    J = a['J']
    codes = [f['code'] for f in a['F'] if f['sev'] != 'OK' and any(x['seq'] == r['seq'] for x in f['rows']) and f['code'] not in ('DEAL', 'PREDICTION', 'CEILINGED', 'FLOOR', 'PLACEMENT-READ', 'CONTRIB')]
    info = [f['code'] for f in a['F'] if any(x['seq'] == r['seq'] for x in f['rows']) and f['code'] in ('DEAL', 'PREDICTION', 'CEILINGED', 'FLOOR', 'PLACEMENT-READ', 'CONTRIB')]
    now, to = fnum(r['now']), fnum(r['to'])
    if 'NOOP' in codes or 'DUP' in codes and r['kind'] == 'bid' and any(f['code'] == 'DUP' and r in f['rows'] for f in a['F']):
        return 'DROP', None, codes + info
    if set(codes) & {'WITHHELD', 'FREEZE', 'HISTORY'}:
        return 'HOLD', r['now'], codes + info
    val = None
    if r['kind'] == 'tos':
        val = J['mod']
        if J['price'] and a['price_eng'] and val is not None:
            same_price = abs(J['price'] - a['price_eng']) <= 0.02 * a['price_eng']
            held_price = a['price_now'] and abs(J['price'] - a['price_now']) <= 0.02 * a['price_now']
            if same_price and abs(val - (to or 0)) <= 3:
                return 'KEEP', r['to'], codes + info
            if held_price and J['base'] and a['base'] and abs(J['base'] - a['base']) < 0.01:
                return 'HOLD', r['now'], codes + info
            return 'CORRECT', val, codes + info
    elif r['kind'] == 'bid':
        head = a['head']
        if head and J['base'] and head['bid'] and now:
            val = round(now * J['base'] / head['bid'], 2)
        if a['tot'] < 15 and a['obj'] == 'Ranking':
            val = now
    elif r['kind'] == 'pp':
        val = 0
    elif r['kind'] == 'ros':
        val = J['ros']
    elif r['kind'] == 'budget':
        val = now
    elif r['kind'] == 'state':
        return ('KEEP', r['to'], codes + info)
    if val is None:
        return ('KEEP' if not codes else 'REVIEW'), r['to'], codes + info
    if to is not None and abs(val - to) <= max(0.02 * abs(to), 0.011 if r['kind'] == 'bid' else 1.0):
        return 'KEEP', r['to'], codes + info
    if now is not None and abs(val - now) <= max(0.02 * abs(now), 0.011 if r['kind'] == 'bid' else 1.0):
        return 'HOLD', r['now'], codes + info
    return 'CORRECT', val, codes + info


REG = []
for a in O:
    for r in a['changes']:
        v, val, codes = row_verdict(a, r)
        REG.append(dict(seq=r['seq'], camp=a['name'], kind=r['kind'], entity=r['entity'], now=r['now'], eng=r['to'], verdict=v, val=val, codes=codes, cid=a['cid']))
REG.sort(key=lambda x: x['seq'])
VC = Counter(x['verdict'] for x in REG)
json.dump(REG, open(f'{S}/register.json', 'w'), default=str)

# ============================ title ============================
t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.LEFT
add_runs(t, 'Decolure Bamboo Sheets 4 Piece (DBS4) — Corrections to PPC audit run 20260921-dbcd48b8', bold=True, size=20, color=NAVY)
add_runs(para(), 'Every bid, placement, budget and state row of the Command Center ranking audit, judged on its own campaign’s keyword, placement and budget data against the team document “Bids and placements on Exact campaigns”.', italic=True, size=11, color=GREY)
table(['Item', 'Value'], [
    ['Product', 'Decolure Bamboo Sheets 4 Piece · product 59 · US · prefix DBS4 · stage Re-Launch (ranking lane)'],
    ['Run reviewed', '20260921-dbcd48b8 · audited 2026-09-21 · exported 2026-09-23 · engine check: 140 passed, **2 failed and unnamed**'],
    ['Inputs', 'Audit JSON export (444 decisions, 2,396 considered rows, 353 campaigns); audit workbook (11 tabs); the team document; Command Center campaign placement reports for 90 days (2026-06-23 → 09-20), pre-deal 31 days (08-15 → 09-14), the deal days the audit read (09-15 → 09-20) and the deal to date (09-15 → 09-22); Command Center unit economics by SKU'],
    ['Scope', f'All {len(ch_rows)} numeric/state rows the run proposes (100 top-of-search modifiers, 59 bids, 6 budgets, 3 rest-of-search, 2 product-page, 5 state) on {sum(1 for a in O if a["changes"])} campaigns, plus every enabled Ranking campaign the run held ({len(O)} campaigns judged). Child swaps, retags, renames, structure and builds are outside the document’s scope and are only referenced where they change a price.'],
    ['Prepared', '2026-09-23'],
], widths=[4, 22.5], size=9)

# ============================ 1. executive summary ============================
doc.add_heading('1. Executive summary', 1)
para('**Verdict: do not deploy the bid, placement and budget rows of this run as written.** The engine’s direction on the focus groups is defensible, but the numbers it prices with are not the campaigns’ numbers, its reads sit inside a deal it did not see, and several of its own safeguards are contradicted by the rows it exports. The corrections below keep what the document supports and re-derive the rest from each campaign’s own data.')
para('What goes wrong, in order of consequence:', bold=True)
n_pr = sum(1 for a in O for f in a['F'] if f['code'] == 'PLACEMENT-READ')
bullets = [
    f'**The placement read is not the campaign’s placement.** On {n_pr} of the {sum(1 for a in O if any(r.get("tos_clk90") is not None for r in a["changes"]))} changed campaigns that state one, the engine’s top-of-search click count differs from Amazon’s campaign placement report by more than 20% (median: the engine sees 25% of the real clicks). Mix, top-of-search conversion, every ceiling and whether the distribution fix is owed are computed on the wrong base. Example: King Size Bamboo Sheet Sets — engine “71% TOS / 24% PP on 34 clicks”; Amazon: 122 TOS / 270 PP / 39 ROS of 431 (PP 63%).',
    f'**The run does not see the Best Deal it should be ranking on.** The Best Deal runs 2026-09-15 → 09-28 and is the velocity window this push depends on (doc §6: velocity “usually means a deal”). The brief lists it, but `engine_read` is null and the workbook Summary says “No deal in the window”, so no step is timed to the remaining deal days, rank claims are checkpointed as if the week were ordinary, and the budget rows read deal-day spend as “exhaustion”. Section 3 shows each focus campaign’s top-of-search delivery in the deal ({DEAL_LABEL}).',
    f'**35 rows the engine itself withholds are exported as changes.** Their RISKS section says “change → HOLD” (rank claim ungradeable); the verdict column says “change”. One of them (seq 529) is a move last week’s review held.',
    f'**The distribution fix is under-applied.** Across Ranking-Exact campaigns product pages took 45% of 90-day clicks; {len(LEAK)} of the {len(RK)} enabled Ranking-Exact campaigns with ≥15 clicks sit above the 20% line. The run cuts the base on {len(LEAK_CUT)} of them. In the deal the mix has moved sharply toward top of search on several (the flagship “Bamboo Sheets” is 97% TOS on deal days), and those keep their base until the deal ends; others still leak — “Bamboo Sheets Queen” MSV is PP {pps("Bamboo Sheets Queen-[Bamboo|Queen]-(MSV)")} over 90 days and the run holds it with “nothing to correct”.',
    '**Premiums above the ceiling on rows that are not proven pushes.** 67 top-of-search raises; 12 are on out-of-focus (taper) campaigns and many more lack a dollar loss ceiling, a funded budget, or a market CTR/CVR read. None of the 45 rows that state a loss per order states a weekly loss ceiling (doc §11 “Ceilinged”).',
    '**Budget raises are mis-triggered.** All six budget rows cite “budget exhausted” at 81–91% utilisation, which is not running out of money even on deal days; two sit on campaigns the same run is tapering; one is sized on 214 clicks/week while its own target section asks 17.',
    f'**The outcome model’s baseline is wrong.** It starts from 29.84 top-of-search clicks/week for the product; Amazon’s placement report shows ~838/week (90 days). The +62% spend ($808.75 → $1,312.30/day) and 40.2% after-ACoS (break-even 33.9%) are therefore not a reliable forecast.',
    '**Contribution is not the serving child’s.** Per-order contribution behind the prices ranges $17.87 → $40.46 across campaigns selling the same children (it is each campaign’s basket × break-even ACoS). The brief says $25.06/unit; the SKU fee model says $30.59 for King White and $30.62 for Queen White; California King White has no price or fees at all.',
]
_f = camp('Bamboo Sheets-(VHSV)-Exact')
_fd = _f['WD']
bullets.insert(2, f"**The flagship “Bamboo Sheets” is the deal’s engine and is carrying an unsigned premium.** Top-of-search clicks went from {_f['WP']['tos']['c']/31:.1f}/day before the deal to {_fd['tos']['c']/DD:.1f}/day in it ({_fd['tos']['c']/sum(_fd[k]['c'] for k in ('tos','detail','other')):.0%} of its clicks) at {usd(_fd['tos']['s']/_fd['tos']['c'])} CPC. Its TOS price {usd(_f['price_now'])} is above the {usd(_f['ceil']['tos'])} ceiling (about {usd(_f['price_now']/_f['rate']['tos'] - _f['contrib'])} lost per TOS order) and the plan needs {usd(_f['J']['need_budget'])}/day against a {usd(_f['budget'])} budget. Keep it through the deal; it needs a signed loss ceiling and a fund-or-descend decision for after 09-28.")
for b in bullets:
    bullet(b)
para('Row-level outcome of this review (Appendix A lists every row):', bold=True)
table(['Verdict', 'Rows', 'Meaning'], [
    ['KEEP', VC.get('KEEP', 0), 'The document supports the engine’s value on this campaign’s own data (its checkpoint is re-timed to the deal: read on deal days, rank at the deal’s end).'],
    ['CORRECT', VC.get('CORRECT', 0), 'Direction or size is wrong on this campaign’s data; the corrected value is given.'],
    ['HOLD', VC.get('HOLD', 0), 'Leave at today’s value: withheld by the engine’s own rule, a re-proposed held move, a freeze, or the document gives no reason to move it.'],
    ['DROP', VC.get('DROP', 0), 'No-op or duplicate row — remove from the file.'],
    ['REVIEW', VC.get('REVIEW', 0), 'No campaign-level target/bid data to re-derive a value; the finding stands and a person sets it.'],
], widths=[2.5, 1.5, 22.5], size=9)
para('In addition, this review adds distribution-fix base cuts on campaigns the run held (Section 5 lists them with values). Those are new rows, not corrections of existing ones.', italic=True, color=GREY)

# ============================ 2. method ============================
doc.add_heading('2. How each row was judged', 1)
para('Each campaign was rebuilt from its own data before the engine’s row was compared with it. The rules are the document’s; the numbers are the campaign’s.')
for b in [
    f'**Placement data** — Amazon’s campaign-grain placement report via Command Center (the grain Amazon actually reports; doc §16 Table 2). **Every correction is priced on the audit’s own 90 days, 2026-06-23 → 09-20, deal days included** — the Best Deal is the rank lever this cycle, so its top-of-search clicks count. Alongside: the 31 days before the deal (08-15 → 09-14) and the deal to date ({DEAL_LABEL}), to show what the deal is doing to top-of-search delivery campaign by campaign. Off-Amazon clicks are shown but excluded from the mix (they are not one of the document’s three placements).',
    '**Conversion rate per placement (doc §3)** — under 15 clicks at a placement: the serving child’s planning rate (the child’s 90-day rate at that placement across every campaign advertising it, or the lane rate if the child has <100 clicks there); 15+ clicks with orders: blend, weight = (clicks − 15) ÷ 35 capped at 1; 15+ with no orders: the child’s rate.',
    '**Contribution** — to keep the dispute on logic rather than margin, the engine’s own per-order figure is used where the row states one; otherwise the serving child’s list price × the run’s break-even ACoS (33.87%). The inconsistency of that basis is itself finding S6.',
    '**Ceilings** — contribution × blended rate, per placement. The base target is what product pages afford; the top-of-search ceiling is what top of search affords (doc §2).',
    '**Situation (doc §12)** — read off the 90-day mix: TOS <30% on ranking → mix first, no price or budget move; PP >20% → distribution fix; mix right → price/budget/demand question; <15 clicks in 90 days → no clicks arriving. Where the deal has already moved the mix (≥15 deal-day clicks at ≥70% TOS or ≤20% PP) the deal-day mix governs the writes for the remaining deal days, hold the base, modifier only.',
    '**Base (doc §10)** — cut only when PP >20% (toward what product pages afford; cap 50%, 25% where PP/ROS carry orders; floor $0.50 or TOS ÷ 10); held when PP ≤20%, when the row is not delivering, or when the deal-day mix is already ≤20% PP (re-tested post-deal on 10-06).',
    '**Top-of-search price (doc §4, §6, §8, §11, §14)** — a premium above the ceiling only on a Ranking-Exact push in focus with a rank on file, stock to sustain it, a budget that funds required clicks × price, and click-through and conversion above the market; +30% per write max; bounded by the market bound and the unit’s contribution. Otherwise the TOS price is the ceiling: a descent to it if above (a named point), a climb to it if below — except (a) an in-progress premium below 70% of its clicks is not cut (§14): it is held and the fund-or-descend decision is surfaced, and (b) out-of-focus rows are not climbed (the operator’s taper). The modifier is always solved backward: price ÷ base − 1.',
    '**Rest of search / product pages** — ROS modifier zero unless 15+ ROS clicks convert at or above the product-page rate (a switch); PP modifier zero.',
    '**Budget** — raised only if the campaign is running out of money on deal days (deal-day spend ≥95% of budget) — during the deal that is the one budget question that matters; an unfunded push is stated as a $/day shortfall for a person to fund or decline (doc §11).',
    '**Checkpoints** — timed to the deal: write 2026-09-24 so the step buys the remaining deal days; mechanism read 2026-09-27 on deal days only (09-24 → 09-27 against 09-15 → 09-23, like for like); rank read 2026-09-29 at the deal’s end; post-deal read 2026-10-06, where any premium bought for the deal is probed back down (§13).',
]:
    bullet(b)
para('Limits of this review: keyword-level placement does not exist (Amazon reports placement per campaign), so a multi-keyword campaign is priced on its head keyword and the same percentage step is applied to its other keywords; the target-level click counts are the engine’s effective-bid pack; SQP market CTR/CVR is only available where the engine’s rationale carried it — where it did not, the four conditions are recorded as “not shown”.', italic=True, color=GREY)

# ============================ 3. product context ============================
doc.add_heading('3. Product context the corrections rest on', 1)
st_rows = []
for s in A['brief']['sections']['stock']['sizes']:
    inv = next((x for x in A['context']['inventory'] if x['size'] == s['size']), {})
    st_rows.append([s['size'], 'yes' if s['in_focus'] else 'no', s['hero'], s['available'], s['rate_30d'], s['shelf_days'], s['shelf_band'],
                    inv.get('hero_room') or '—', s['serving_child'], s['serving_available'], s['next_arrival'] or '—'])
table(['Size', 'Focus', 'Hero', 'Hero avail.', 'Units/day 30d', 'Shelf days', 'Band', 'Hero room', 'Serving child', 'Serving avail.', 'Next arrival'], st_rows, size=8)
para('Queen’s hero (White) runs out 4 days before the 2026-10-27 arrival at push pace and Full/Twin heroes are at zero; the engine pushes those sizes “on the serving child”, yet 32 Ranking campaigns still advertise BAMBOO-QUEEN-WHITE and only 5 are re-pointed to Olive in this run.')
t90, sp90, sa90, od90 = PT['d90']; tp, spp, sap, odp = PT['pre_deal30']; td, spd, sad, odd = PT['deal6']
table(['Window', 'TOS clicks/wk', 'TOS share', 'PP share', 'Spend/day', 'ACoS', 'Orders/day'], [
    ['90 days (06-23 → 09-20)', f'{t90["tos"]/90*7:,.0f}', pct(t90['tos']/sum(t90.values())), pct(t90['detail']/sum(t90.values())), usd(sp90/90), pct(sp90/sa90, 1), f'{od90/90:.1f}'],
    ['Pre-deal 31 days (08-15 → 09-14)', f'{tp["tos"]/31*7:,.0f}', pct(tp['tos']/sum(tp.values())), pct(tp['detail']/sum(tp.values())), usd(spp/31), pct(spp/sap, 1), f'{odp/31:.1f}'],
    ['Deal days read (09-15 → 09-20)', f'{td["tos"]/6*7:,.0f}', pct(td['tos']/sum(td.values())), pct(td['detail']/sum(td.values())), usd(spd/6), pct(spd/sad, 1), f'{odd/6:.1f}'],
    ['Engine outcome model “before”', f'{outcome["tos_clicks_wk_before"]}', '—', '—', usd(outcome['spend_day_before']), pct(outcome['acos_before'], 1), '—'],
    ['Engine outcome model “after”', f'{outcome["tos_clicks_wk_after"]}', '—', '—', usd(outcome['spend_day_after']), pct(outcome['acos_after'], 1), '—'],
], size=8.5)
para('Workbook (ppc-audit-DBS4-20260921-dbcd48b8.xlsx): the Summary tab prints “Deal window: No deal in the window” while its own brief block lists the Best Deal 09-15 → 09-28; the Agent review tab is empty (“No agent review is stored for this run yet”), so all 72 “Needs a look” rows — among them 16 riskier bid rows and 9 riskier top-of-search rows — are unreviewed; the Decisions tab carries the 35 withheld rows as changes. The workbook and the JSON agree row for row; every finding below applies to both.')
doc.add_heading('Top-of-search delivery in the Best Deal — focus campaigns', 2)
para(f'The deal is the rank lever this cycle, so top-of-search clicks are what matter now. Every in-focus Ranking campaign with top-of-search clicks before or during the deal, sorted by deal-day top-of-search clicks. “Corrected TOS price” is this review’s write for the remaining deal days (Section 5 has the reasoning per campaign).')
drows = []
for a in sorted([a for a in O if a['in_focus'] and a['obj'] == 'Ranking' and (a['WD']['tos']['c'] or a['WP']['tos']['c'])], key=lambda a: -a['WD']['tos']['c']):
    d, pr = a['WD'], a['WP']
    dtot = sum(d[k]['c'] for k in ('tos', 'detail', 'other'))
    pre_d, deal_d = pr['tos']['c'] / 31, d['tos']['c'] / DD
    drows.append([short(a['name'])[:62], f'{pre_d:.1f}', f'{deal_d:.1f}', (f'{deal_d / pre_d - 1:+.0%}' if pre_d else '—'),
                  pct(d['tos']['c'] / dtot) if dtot else '—', pct(d['tos']['o'] / d['tos']['c'], 1) if d['tos']['c'] else '—',
                  usd(d['tos']['s'] / d['tos']['c']) if d['tos']['c'] else '—', usd(a['price_now']), usd(a['J']['price']),
                  (a['J']['write_kind'] or ['—'])[0][:70]])
table(['Campaign', 'TOS clicks/day pre-deal', f'TOS clicks/day deal', 'Change', 'TOS share in deal', 'TOS CVR in deal', 'TOS CPC in deal', 'TOS price now', 'Corrected TOS price', 'Corrected write'], drows,
      widths=[6.8, 1.6, 1.6, 1.4, 1.6, 1.6, 1.6, 1.6, 1.8, 6.5], size=7)
tp_d, td_d = sum(r['WP']['tos']['c'] for r in O if r['in_focus']) / 31, sum(r['WD']['tos']['c'] for r in O if r['in_focus']) / DD
para(f'Across all in-focus campaigns: {tp_d:.0f} top-of-search clicks/day before the deal, {td_d:.0f}/day in it ({td_d / tp_d - 1:+.0%}).', bold=True)
para(f'Margin in the brief: break-even ACoS {margin["be_acos"]*100:.2f}% · contribution {usd(margin["contribution_per_unit"])}/unit (profitability, 08-24 → 09-23). Prediction grades over 90 days: 5 HIT, 36 MISS, 1 WRONG_DIRECTION, 62 WITHDRAWN — hit rate 4.8%. Open tuner records: 388 (72 wrong direction, 53 stalled, 39 behind).')

# ============================ 4. systemic findings ============================
doc.add_heading('4. Run-level findings', 1)
para('Each finding: what is happening · the engine’s rationale · the issue against the document · the correction. Campaign sections in Section 5 cite these by number.')


def sysf(num, title, sev, what, why, issue, fix, extra=None):
    doc.add_heading(f'S{num}. {title}', 2)
    p = para(); add_runs(p, f'Severity: {sev}', bold=True, color=RED if sev in ('Critical', 'High') else GREY)
    labelled('What is happening.', what)
    labelled('Engine’s rationale.', why)
    labelled('Issue.', issue, RED)
    labelled('Correction.', fix, GREEN)
    if extra:
        extra()


def ex_placement():
    rows = []
    for a in sorted(O, key=lambda a: -a['W90']['tos']['c']):
        f = next((f for f in a['F'] if f['code'] == 'PLACEMENT-READ'), None)
        if not f:
            continue
        e = f['rows'][0]
        tot = sum(a['W90'][k]['c'] for k in ('tos', 'detail', 'other'))
        rows.append([short(a['name'])[:70], e['tos_clk90'], (e.get('mix') or '—')[:60], a['W90']['tos']['c'], a['W90']['detail']['c'], a['W90']['other']['c'], pct(a['W90']['detail']['c'] / tot if tot else None)])
    table(['Campaign', 'Engine TOS clicks 90d', 'Engine mix', 'Amazon TOS', 'Amazon PP', 'Amazon ROS', 'Amazon PP share'], rows[:25], widths=[8.5, 2, 7, 2, 2, 2, 2], size=7.5)
    para(f'Top 25 of {len(rows)} by top-of-search volume; every one is repeated in its campaign section.', italic=True, color=GREY)


sysf(1, 'The placement read is not the campaign’s placement report', 'Critical',
     f'On {n_pr} campaigns the engine’s “READ AT TOP OF SEARCH (N clicks …)” and RESHAPE mix differ from Amazon’s campaign placement report for the same 90 days by more than 20%; the median engine figure is a quarter of the real one. The engine’s mix often reads “right” where the campaign is leaking: Bamboo Sheets King Size — engine 34 TOS clicks; Amazon 211 TOS / 671 PP (72%).',
     'The engine reads placement at the keyword/term grain (“This campaign’s top-of-search delivery on the term”), an estimate Amazon does not publish.',
     'Doc §16 Table 2 requires one row per campaign per placement; §5 manages the mix on clicks. The TOS conversion that sets every ceiling (§3), the 20% product-page test (§10) and the <30% mix-first rule (§12) all run on these numbers, so a quarter-size, differently-shaped sample produces different decisions.',
     'Re-derive mix, conversion and ceilings from the campaign placement report (done for every campaign in Section 5). Fix the engine to read placement at campaign grain and to show the term estimate only as context.', ex_placement)

sysf(2, 'The run does not see the Best Deal it should be ranking on', 'Critical',
     'Best Deal 2026-09-15 → 09-28 is on the calendar (brief.deals); the audit ran on 09-21, day 7 of it. The deal is the velocity window for this re-launch (Section 3 shows each focus campaign’s top-of-search delivery before and during it). The engine’s rank checkpoints (09-25 on 42 rows, 09-28 on 15) and its day-4 reshape read of 09-15 compare deal days with pre-deal days.',
     '`deal.engine_read = null`; the workbook Summary prints “Deal window: No deal in the window”. Steps are sized from the plan and the “book” as if the week were ordinary; the budget pass reads deal-day spend as “budget exhausted”.',
     'Doc §6: velocity in the window — usually a deal — is the first of the four conditions; with it, “distance is not the constraint … run it inside the window where the velocity is available”. Doc §12: a deal changes every rate, so a step is graded like for like; a read that straddles the deal start (seq 12: 3 days before vs 3 days after 09-15) measures the deal, not the step.',
     'Use the deal: every correction here prices on the 90 days including deal days, and the moves are timed to buy the remaining deal days (write 09-24). Grade mechanism on deal days only (09-24 → 09-27 vs 09-15 → 09-23); read rank at the deal’s end (09-29); read again post-deal (10-06), when TOS clicks and CVR will fall back — any premium bought for the deal is then probed down in 3–5% steps (§13) rather than left in place. Record the deal on the run so the loader and grader see it.')

sysf(3, 'Rows the engine withholds are exported as changes', 'Critical',
     '35 rows on 21 campaigns carry verdict “change” while their RISKS section reads “IF MISSED: n/a — the rank claim is UNGRADEABLE … THEN: change → HOLD”. They are 16 top-of-search modifier raises, 2 modifier cuts, 14 bid cuts, 1 rest-of-search cut and 2 budget raises (seq 85, 92).',
     'The engine’s gate refuses a ranking move without a gradeable rank claim, then the export writes the move anyway.',
     'An exported change without a gradeable prediction is, by the run’s own how_to_read, an engine bug. The loader would deploy moves the engine refused.',
     'HOLD all 35 (listed in Appendix A with code WITHHELD). Fix the exporter to carry the gate’s verdict.')

sysf(4, 'Engine check failed twice and does not say where', 'High',
     'run.status = check_failed: 140 passed, 2 failed; brief.engine_check.failures is empty — “this run was stored before the check named them — a re-run would name them”.',
     'The operator ruling (2026-09-22) is that a failed check does not withhold the run.', 'Two unnamed failures cannot be confirmed before deploy, which is what the check exists for.',
     'Re-run the check (not the audit) to name the two failures before any row is deployed.')

sysf(5, 'Read floor: “15 clicks” is written, 100 is applied', 'Medium',
     'Seven rows say top of search “carries N clicks in 90 days, under the 15-click read floor” with N between 34 and 101, e.g. seq 14 (83 clicks) and seq 57.',
     'The engine’s own line: “the read floor is 32 top-of-search clicks a week (100 clicks ÷ 22 days × 7)”.',
     'Doc §3/§10: 15 clicks is the floor, 15–50 is blended, 50+ is the campaign’s own rate. A 100-click floor throws away readable evidence and then labels it with the document’s number.',
     'Price on the §3 blend (every campaign section shows the blend arithmetic). Correct the wording or the floor.')

contribs = sorted({r['contrib'] for r in ch_rows if r['contrib']})
sysf(6, 'Contribution per order is inherited from each campaign’s basket', 'High',
     f'Rows state contribution per order from ${contribs[0]:.2f} to ${contribs[-1]:.2f} for campaigns selling the same children. The brief carries $25.06/unit (profitability). Command Center’s fee model gives King White $30.59, Queen White $30.62, Queen Olive $34.87, King Creme $30.67; California King White, Taupe, Black, Burgundy and Charcoal have no price or fees (contribution unknown).',
     '“$26.55 contribution per order (this campaign’s own basket × break-even ACoS)”.',
     'Doc §2 and bound 1 of §8: every price traces to the serving child’s contribution; the base is derived from the serving child, never inherited; an open landed-cost question is flagged by name on the rows it touches. A basket figure moves with whatever the campaign happened to sell, including deal-price orders.',
     'Publish one contribution per child (reconcile the $25.06 profitability figure with the fee model) and price every campaign on its serving child. Until then, California King rows carry the flag “contribution unknown” and take no premium.')

sysf(7, 'The distribution fix is under-applied — and applied where it is not owed', 'High',
     f'Ranking-Exact product-page share over 90 days is 45% (6,468 of 14,232 clicks). {len(LEAK)} of the {len(RK)} enabled Ranking-Exact campaigns with ≥15 clicks exceed 20%. The run writes base cuts on {len(LEAK_CUT)}. Held with PP over 20%: Bamboo Sheets VHSV ({pps("Bamboo Sheets-(VHSV)-Exact")}, $198/day), Bamboo Sheets Queen MSV ({pps("Bamboo Sheets Queen-[Bamboo|Queen]-(MSV)")}), Purple Bamboo Sheets ({pps("Purple Bamboo Sheets")}), Cooling Sheets Queen HSV ({pps("Cooling Sheets Queen-(HSV)")}) and more (Section 5).',
     'Hold rows read “Product pages sits flat over a base priced at rest-of-search economics … there is nothing to correct” — i.e. the engine reads the PP modifier (0%) instead of PP click share.',
     'Doc §5/§10: product pages at or under 20% of clicks — always; above it, cut the base whatever the ceiling permits and re-solve the modifier so the TOS price holds. §12: under 30% TOS on a ranking campaign the fix takes precedence over any price or budget move.',
     'Add the base cuts listed per campaign (cap 25% where PP/ROS carry orders, 50% otherwise), TOS price held by re-solving the modifier. Where the engine climbs TOS on a campaign under 30% TOS (6 campaigns), the climb is removed.')

sysf(8, 'Premiums above the ceiling on rows that are not proven pushes', 'High',
     f'67 top-of-search raises: 54 on in-focus campaigns, 12 on out-of-focus (taper) campaigns. 45 rows state a loss per order (up to ${max((r["loss"] or 0) for r in ch_rows):.2f}). The market bound on 73 rows is “this campaign’s own top-of-search CPC + 15%”.',
     'The PRESS class (“every day behind is a missed opportunity”) and the plan’s price govern; the market bound is read from the campaign’s own CPC.',
     'Doc §6/§8/§11: a premium is the one exception and needs all five push properties and all four conditions (velocity, CTR above market, CVR above market, stock after); an out-of-focus row is a maintenance row priced to its ceiling. A market bound read from our own CPC at 1–5% impression share is not what the position clears at — it is circular.',
     'Out-of-focus and non-push rows: TOS price to the ceiling (descent or no climb). In-focus rows above the ceiling that fail a test: hold the price (doc §14 forbids cutting a push below 70% of its clicks) and put the fund-or-descend decision to the operator with the dollar shortfall. Replace the self-referential market bound with a per-term clearing price (e.g. the rivals’ band the engine already reports: “campaigns holding 30%+ share pay $5.14 effective”).')

sysf(9, 'Pushes are not ceilinged, and their size is not settled', 'High',
     'No row states a weekly dollar loss ceiling. Required clicks disagree inside single rows: seq 67 (Cool Sheets Queen) — TARGET asks 17 clicks/wk, the chain 40/wk, the budget is sized on 30.6/day = 214/wk. The plan rows are “an UPPER BOUND, not a measured gap”.',
     'The PRESS budget line sizes $377.58/day for Bamboo Sheets Queen Size against a $49.72 budget; the SIZING line says “the budget sustains it”.',
     'Doc §7/§11: required clicks/day = units/day at the target rank ÷ TOS conversion; budget = that × the price this write pays; loss ceiling = that week’s spend at risk. A push that cannot be funded is written as a $/day shortfall and becomes a decision.',
     'Each campaign section states required clicks, the $/day the push needs at today’s price, the budget and the shortfall.')

sysf(10, 'Budget raises on campaigns that did not run out of money', 'High',
     'All six budget rows (+30% each) are “CASE 1, BUDGET EXHAUSTED” at 81–91% utilisation; seq 67 and seq 85/92 sit on campaigns the same run tapers or withholds.',
     '“The pack flags the day as budget-capped”.',
     'Doc §6/§12: raise the budget when the campaign ran out of money, not out of auctions. With share at 1–5% the question is price (bid not clearing) or demand, and a campaign cannot be tapered and funded in the same run.',
     'Hold all six unless the campaign caps out on the remaining deal days (each campaign section shows deal-day spend against budget); where a push is funded, raise to the stated $/day as an operator decision.')

sysf(11, 'Predictions the step cannot deliver', 'Medium',
     '20 rows carry the book comparison; 16 ask at least twice what steps of that size have bought (median ×3.1). 13 rank claims promise 15+ positions in 14 days (e.g. seq 14: 49 → ≤16).',
     'The claim is filed from the plan’s requirement: “it comes from the plan’s requirement, not from the step, and is likely to grade as a miss even if the step is right.”',
     'Doc §11: the prediction is the written expectation of this write. The account’s hit rate is 4.8%; a prediction built to miss teaches nothing about the step.',
     'File the step’s own expected result (the book’s rate for the size) against post-deal data; keep the plan target as the destination only.')

sysf(12, 'The outcome model starts from the wrong baseline', 'High',
     f'Outcome: top-of-search clicks/week {outcome["tos_clicks_wk_before"]} → {outcome["tos_clicks_wk_after"]} (×21.6), spend ${outcome["spend_day_before"]} → ${outcome["spend_day_after"]}/day (+62%), ACoS {outcome["acos_before"]*100:.1f}% → {outcome["acos_after"]*100:.1f}%, TACoS {outcome["tacos_before"]*100:.1f}% → {outcome["tacos_after"]*100:.1f}%. Amazon’s report puts the product at ~{t90["tos"]/90*7:,.0f} TOS clicks/week.',
     'Δ TOS clicks × each campaign’s TOS price, from a 14-day (deal) base.',
     'The after-ACoS (40.2%) is above break-even (33.9%) even on the engine’s own numbers; with a baseline off by a factor of ~28, neither the spend nor the sales delta can be trusted.',
     'Recompute the outcome from the campaign placement report, separating deal days from the post-deal baseline, after the corrections in this document.')

sysf(13, 'Pushes on heroes that cannot ship through the window', 'High',
     '16 campaigns with price moves advertise a hero the stock gate marks UNDER_HORIZON or NO_ROOM (Queen White, Full White, Twin White, Cal King White) with “child_after: hold”.',
     'The write “rides under the file’s pick (PIVOT)” with a kill date at the next arrival.',
     'Doc §12: the serving child cannot ship → every read is void; §6: a position taken then lost to a stockout is rented, not bought.',
     'Re-point these campaigns to the serving child first (Queen → Olive, Full → Light Olive, Twin → Burgundy, Cal King → Burgundy) or hold their price rows.')

sysf(14, 'Bidding strategy on a push', 'High',
     'Bamboo Sheets Queen Size (HSV, “UD”) runs AUTO_FOR_SALES (dynamic up and down); 216 other Ranking campaigns run down-only.',
     '“takes the authorized ceiling $13.39 → $16.23, delivered through the modifier”.',
     'Up-and-down can lift the TOS bid 100%: a written $8.11 can clear at $16.21, over the $10.25 bound and the $26.55 unit. Doc §10: fixed while (re)launching; down-only on history, checked for suppression before a push price is raised; fixed as the last resort, stated as a trade.',
     'Switch that campaign to fixed or down-only before any TOS write. On down-only pushes that are not delivering, check suppression before raising price.')

sysf(15, 'No-op, duplicate and contradictory rows', 'Medium',
     'Seq 2052–2054 pause campaigns that are already paused (PAUSED → PAUSED) yet pass the “moves the value” code check. Seq 2160/2161, 2162/2163 and 2164–2169 write the same keyword twice. Seq 12, 66 and 143 are labelled with the plan keyword but change a different target (seq 12 names “cooling sheet”, bid $1.95, but moves “cool sheets” at $1.44). Seq 12 is labelled RESTORE $1.44 → $1.60 while its ENGINE DECISION says CUT $1.44 → $1.30, on a 0-click keyword (“cool sheets”) of a taper campaign, and its TAPER CHECK says “the step down is HELD … a human decides”.',
     '—', 'The file would carry writes that do nothing, double-count one, and reverse direction without a person deciding.',
     'Drop the no-ops and duplicates; hold seq 12 for the human decision its own rationale asks for.')

sysf(16, 'Moves re-proposed after last week’s review held them', 'Medium',
     'Seq 57 (Bamboo Cooling Sheets MSV 718% → 818%; held last week at 718 → 795), seq 529 (Bed Sheets Bamboo King 213% → 241%; held last week), and the California King modifier corrected last week to a +30% step.',
     'Open tuner records 2150 and 2113 are still inside their windows (to 2026-10-05); the deal guard still runs.',
     'Doc §10: “what the last step returned — a step that produced nothing is a finding, not a reason to repeat it”; the condition that held the move has not been read.',
     'Hold until the records are graded on post-deal data.')

n_res = sum(1 for a in O for f in a['F'] if f['code'] == 'RESIDUE')
sysf(17, 'The TOS price falls as a residue of taper bid cuts', 'Medium',
     f'On {n_res} ranking campaign(s) with a live TOS modifier the run cuts bids (taper −10%) without re-solving the modifier, so the TOS price drops by the same 10% with no named point (Deep Pocket King Sheet Set HSV, seq 368/369). The same pattern on PAT and Discovery campaigns with a 0% modifier is harmless — there the bid is the only price.',
     'SOP-47 P7 taper ladder: “modifier first, the bid follows”.',
     'Doc §9/§17: the top-of-search price never falls as a residue of a base cut; if it comes down it lands on a named point.',
     'Either re-solve the modifier to hold TOS, or state the TOS descent and its point (the ceiling).')

sysf(18, 'Non-ranking rows: sound direction, thin reads', 'Medium',
     'Conversions sweep rows cut bids to “AOV × break-even × CVR” on 24–32 clicks (seq 2160, 2164–2169) and cut TOS modifiers one rung on Conversions/Discovery campaigns, some with zero clicks in 90 days.',
     '“BID DOWN TO PROFITABLE CPC … a single step”.',
     'Doc scope: other objectives are priced inside their ceilings. The ceiling uses the campaign’s own rate on thin clicks without the §3 blend; modifier cuts on zero-click campaigns change nothing measurable.',
     'Keep direction where the price is above its ceiling; size on the blended rate (campaign sections). Zero-click modifier rows are harmless but ungradeable.')

# ============================ 5. campaigns ============================
doc.add_heading('5. Campaign by campaign', 1)
para(f'{len(det)} campaigns: every campaign with a numeric/state row in the run, plus every enabled Ranking campaign where this review finds a move owed. Ordered by focus group, then by spend. All placement figures are Amazon’s campaign placement report for the audit’s 90 days (2026-06-23 → 09-20, deal days included); deal-to-date columns show the Best Deal on its own.')

group_order = ['IN · Bamboo', 'IN · Bamboo|King', 'IN · Bamboo|Queen', 'IN · Cooling|King', 'OUT · taper', '']


def gkey(a):
    f = a['focus'] or ''
    return (group_order.index(f) if f in group_order else 5, -(a['spend_day'] or 0))


det.sort(key=gkey)
cur = None
for a in det:
    grp = a['focus'] or f'Not a Ranking campaign ({a["obj"]})'
    if grp != cur:
        cur = grp
        doc.add_heading(f'Focus: {grp}', 2)
    J, X = a['J'], a['X']
    doc.add_heading(short(a['name']), 3)
    stk = a['stock'] or {}
    para(f"Objective **{a['obj']}** · focus {a['focus'] or '—'} · advertised child {a['child']} → {a['child_after'].replace('→ ', '')} · bid strategy {a['bid_strategy']} · status {a['status']} · campaign id {a['cid']}", size=8.5, color=GREY)
    # snapshot table
    tot90 = sum(a['W90'][k]['c'] for k in ('tos', 'detail', 'other'))
    snap = [
        ['Budget / day', usd(a['budget']), 'Spend/day in the deal', usd(J.get('deal_spend')), 'Spend/day pre-deal', usd(J['pre_spend'])],
        ['Rank (keyword)', f"{a['rank_now'] or '—'} now → target {a['rank_tgt'] or '—'} ({a['kw'] or '—'}); 30d ago {a['rank_30'] or '—'}", 'Plan PPC clicks/wk', a['plan_wk'] or '—', 'TOS clicks', f"{a['tos_wk']:.1f} (90d) · {a['WP']['tos']['c']/31:.1f}/day pre-deal → {a['WD']['tos']['c']/DD:.1f}/day in the deal"],
        ['TOS impression share', f"{a['tos_is']}%" if a['tos_is'] is not None else '—', 'Market CTR / CVR (SQP)', f"{a['mkt_ctr'] or '—'}% / {a['mkt_cvr'] or '—'}%", 'Contribution / order used', usd(a['contrib']) + (' (engine)' if a['eng_contrib'] else ' (child price × BE)')],
        ['Stock (size)', f"{stk.get('size', '—')}: hero {stk.get('hero', '—')} {stk.get('available', '—')} units, {stk.get('shelf_days', '—')} shelf days, hero room {stk.get('hero_room', '—')}" if stk else '—', 'Serving child', f"{stk.get('serving_child', '—')} ({stk.get('serving_available', '—')})" if stk else '—', 'Situation (doc §12)', J['situation']],
    ]
    table(['', '', '', '', '', ''], snap, widths=[3, 7, 3.6, 4.4, 3.2, 5.3], size=7.5, header_fill='FFFFFF', zebra=False)
    # placement table
    prow = []
    for k, lab in (('tos', 'Top of search'), ('other', 'Rest of search'), ('detail', 'Product pages'), ('off', 'Off-Amazon')):
        x, w, d = X[k], a['W90'][k], a['WD'][k]
        tot = a['tot']
        share = (x['c'] / tot) if (tot and k != 'off') else None
        cvr = (x['o'] / x['c']) if x['c'] else None
        cpo = (x['s'] / x['o']) if x['o'] else None
        rate = a['rate'].get(k) if k != 'off' else None
        ceil = a['ceil'].get(k) if k != 'off' else None
        mod = {'tos': a['tos_mod'], 'other': a['ros_mod'], 'detail': a['pp_mod'], 'off': None}[k]
        prow.append([lab, x['c'], pct(share), x['o'] if k != 'off' else '—', pct(cvr, 1) if k != 'off' else '—', usd(x['s'] / x['c']) if x['c'] else '—', usd(cpo) if k != 'off' else '—',
                     f"{d['c']} / {pct(d['o']/d['c'], 1) if d['c'] and k!='off' else '—'}", pct(rate, 1) if rate is not None else '—', usd(ceil), f'{mod}%' if mod is not None else '—'])
    table(['Placement', 'Clicks 90d (incl. deal)', 'Share', 'Orders', 'CVR', 'CPC', 'Cost/order', f'Deal {DEAL_LABEL} clicks / CVR', 'Rate used (§3)', 'Ceiling', 'Modifier now'], prow, size=7.5)
    para('Rate basis — TOS: ' + a['why_rate']['tos'] + ' · PP: ' + a['why_rate']['detail'], size=7.5, color=GREY)
    # keyword table
    if a['targets']:
        krow = []
        ratio = (J['base'] / a['base']) if (J['base'] and a['base']) else 1
        mod_now, mod_eng, mod_j = a['tos_mod'], (a['tos_to'] if a['tos_to'] is not None else a['tos_mod']), J['mod']
        for t in a['targets']:
            if t['bid'] is None:
                continue
            en = t['state'] in ('ENABLED', None)
            eng_b = t['bid_to'] if t['bid_to'] is not None else t['bid']
            jb = round(t['bid'] * ratio, 2) if en and a['obj'] == 'Ranking' and a['tot'] >= 15 else (J['base'] if (a['head'] and t['label'] == a['head']['label']) else t['bid'])
            cv = (t['orders'] / t['clicks']) if t.get('clicks') else None
            krow.append([t['label'][:48], t.get('match') or '—', t['state'] or '—', t.get('clicks') if t.get('clicks') is not None else '—', t.get('orders') if t.get('orders') is not None else '—', pct(cv, 1),
                         usd(t['bid']), usd(eng_b), usd(jb) if en else '—',
                         usd(t['bid'] * (1 + mod_now / 100)), usd(eng_b * (1 + (mod_eng or 0) / 100)), usd(jb * (1 + (mod_j or 0) / 100)) if (en and mod_j is not None) else '—'])
        table(['Keyword / target', 'Match', 'State', 'Clicks*', 'Orders*', 'CVR*', 'Bid now', 'Bid engine', 'Bid corrected', 'TOS price now', 'TOS price engine', 'TOS price corrected'], krow, size=7.5)
        para('* the engine’s effective-bid pack read for the target. TOS price = bid × (1 + TOS modifier).', size=7, color=GREY)
    # engine rows
    if a['changes']:
        para('What the engine proposes and why:', bold=True)
        for r in a['changes']:
            v = next((x for x in REG if x['seq'] == r['seq']), None)
            txt = trunc(r.get('decision'), 460)
            bullet(f"**Seq {r['seq']} · {r['kind']} · {r['entity']}: {r['now']} → {r['to']}** — {txt}  **Review: {v['verdict']}" + (f" → {v['val']}" if v and v['verdict'] == 'CORRECT' else '') + '**')
    else:
        para('The engine holds every lever on this campaign.', bold=True)
    # findings
    fs = [f for f in a['F'] if f['sev'] != 'OK' or a['changes']]
    sev_order = {'Critical': 0, 'High': 1, 'Medium': 2, 'OK': 3}
    fs.sort(key=lambda f: sev_order[f['sev']])
    for i, f in enumerate(fs, 1):
        p = para(); add_runs(p, f"Finding {i} — {f['title']}  ", bold=True, color=NAVY); add_runs(p, f"[{f['sev']} · {f['code']}]", size=8, color=RED if f['sev'] in ('Critical', 'High') else (GREEN if f['sev'] == 'OK' else GREY))
        labelled('What is happening.', f['what'])
        if f['why']:
            labelled('Engine’s rationale.', f['why'])
        labelled('Issue.', f['issue'], RED if f['sev'] != 'OK' else GREEN)
        labelled('Correction.', f['fix'], GREEN)
    # correction box
    para('Corrected write for this campaign:', bold=True)
    crow = [
        ['Base (head keyword)', usd(a['base']), usd(a['base_to'] or a['base']), usd(J['base']), J['base_why'] or '—'],
        ['TOS modifier', f"{a['tos_mod']}%", f"{int(a['tos_to']) if a['tos_to'] is not None else a['tos_mod']}%", f"{J['mod']}%" if J['mod'] is not None else '—', 'solved backward: TOS price ÷ base − 1' + (' — over the 500% working cap: route to a person' if (J['mod'] or 0) > 500 else '')],
        ['TOS price', usd(a['price_now']), usd(a['price_eng']), usd(J['price']), '; '.join(J['write_kind']) or '—'],
        ['Ratio TOS : PP price', f"{a['price_now']/a['base']:.2f} : 1" if a['base'] and a['price_now'] else '—', f"{a['price_eng']/(a['base_to'] or a['base']):.2f} : 1" if a['base'] and a['price_eng'] else '—', f"{J['price']/J['base']:.2f} : 1" if J['base'] and J['price'] else '—', 'doc §5: state both prices, not the percentage'],
        ['ROS modifier', f"{a['ros_mod']}%", f"{int(a['ros_to']) if a['ros_to'] is not None else a['ros_mod']}%", f"{J['ros']}%", 'zero until 15+ ROS clicks convert ≥ the PP rate'],
        ['PP modifier', f"{a['pp_mod']}%", f"{int(a['pp_to']) if a['pp_to'] is not None else a['pp_mod']}%", '0%', 'product pages priced by the base'],
        ['Budget / day', usd(a['budget']), usd(a['budget_to'] or a['budget']), usd(J['budget']), J['budget_why'] or '—'],
    ]
    if J['price'] and a['rate']['tos']:
        cpo = J['price'] / a['rate']['tos']
        crow.append(['Cost / loss per order at TOS', '—', '—', f"{usd(cpo)} / {usd(max(0, cpo - a['contrib']))}", f"TOS price ÷ {pct(a['rate']['tos'],1)} vs {usd(a['contrib'])} contribution"])
    table(['Lever', 'Now', 'Engine', 'Corrected', 'Why'], crow, widths=[3.6, 2.4, 2.4, 2.8, 15.3], size=7.5)
    # checkpoint
    if a['changes'] or any(f['code'] == 'BASE-CUT-MISSING' for f in a['F']):
        pp_s = a['share']['detail']
        dtd = a['WD']['tos']['c'] / DD
        pred = []
        if J['base'] and a['base'] and J['base'] < a['base'] - 0.005:
            pred.append(f"product-page share {pct(pp_s)} → ≤ {pct(max(0.20, (pp_s or 0) - 0.10))} with deal-day TOS clicks held at {dtd:.1f}/day ± 15%")
        if J['price'] and a['price_now'] and J['price'] > a['price_now'] * 1.01:
            pred.append(f"deal-day TOS clicks {dtd:.1f}/day → about {dtd*1.3:.1f}/day (the book’s rate for a step this size), mix unchanged")
        if J['price'] and a['price_now'] and J['price'] < a['price_now'] * 0.99:
            pred.append(f"TOS cost per order falls from {usd(a['price_now']/a['rate']['tos'])} to about {usd(J['price']/a['rate']['tos'])}; TOS clicks may thin — the intended half of a descent")
        if not pred:
            pred.append('no price moves; re-read the mix and delivery at the checkpoint')
        labelled('Checkpoint and prediction.', 'Write 2026-09-24 (four deal days left). Mechanism read 2026-09-27 on deal days 09-24 → 09-27 against 09-15 → 09-23: ' + '; '.join(pred) + '. Rank read 2026-09-29 (deal end). Post-deal read 2026-10-06: TOS clicks and CVR will fall back with the deal — probe any premium bought for the deal down in 3–5% steps (§13); the base step stays.')
        labelled('Reversal.', 'Base step: if product-page share does not move, the leak is not price-driven — restore the base. Price step: if TOS clicks do not rise, read impression share and suppression before any further price. Descent: if TOS orders fall further than the click reduction explains, restore one step and record the floor.')

# ============================ Appendix A register ============================
doc.add_heading('Appendix A — Row-level register (every numeric and state row in the run)', 1)
para('Codes: see Appendix C. “Corrected” is the value to deploy for CORRECT rows; HOLD keeps today’s value; DROP removes the row. Informational codes (DEAL, PLACEMENT-READ, FLOOR, PREDICTION, CEILINGED, CONTRIB) mean the checkpoint and the prediction on that row must also be rewritten even where the value is kept.')
fillmap = {'KEEP': 'D9EAD3', 'CORRECT': 'FCE5CD', 'HOLD': 'FFF2CC', 'DROP': 'F4CCCC', 'REVIEW': 'EAD1DC'}
rows = [[x['seq'], short(x['camp'])[:60], x['kind'], x['entity'].replace('target · ', '')[:34], x['now'], x['eng'], x['verdict'], x['val'] if x['verdict'] in ('CORRECT', 'HOLD') else ('—' if x['verdict'] == 'DROP' else x['eng']), ', '.join(dict.fromkeys(x['codes']))] for x in REG]
table(['Seq', 'Campaign', 'Kind', 'Entity', 'Now', 'Engine', 'Verdict', 'Deploy', 'Codes'], rows, widths=[1.1, 8.2, 1.2, 4.2, 1.3, 1.3, 1.6, 1.4, 6.2], size=7, fills=[fillmap.get(r[6]) for r in rows], zebra=False)

# ============================ Appendix B clean ============================
doc.add_heading('Appendix B — Enabled Ranking campaigns reviewed with no correction', 1)
para('Held by the engine and, on their own 90-day data, owed no move under the document (mix within the lines, price at or under the ceiling, or too few clicks to act on).')
rows = []
for a in sorted(clean, key=lambda a: -(a['spend_day'] or 0)):
    rows.append([short(a['name'])[:80], a['focus'], a['tot'], pct(a['share']['tos']), pct(a['share']['detail']), usd(a['price_now']), usd(a['ceil']['tos']), usd(a['spend_day'])])
table(['Campaign', 'Focus', 'Clicks 90d', 'TOS share', 'PP share', 'TOS price', 'TOS ceiling', 'Spend/day 14d'], rows, widths=[10, 3.4, 2, 1.8, 1.8, 2, 2, 2], size=7)

# ============================ Appendix C codes ============================
doc.add_heading('Appendix C — Finding codes', 1)
codes = [
    ('PLACEMENT-READ', 'S1', 'Engine placement read ≠ campaign placement report'), ('DEAL', 'S2', 'Run blind to the Best Deal; moves not timed to it'),
    ('WITHHELD', 'S3', 'Rationale withholds, export changes'), ('FLOOR', 'S5', '100-click floor written as 15'), ('CONTRIB', 'S6', 'Contribution not the serving child’s'),
    ('BASE-CUT-MISSING', 'S7', 'PP >20% and the base is held'), ('BASE-CUT-NOT-OWED', 'S7', 'Base cut with PP ≤20%'), ('BASE-CUT-NO-DELIVERY', 'S7', 'Base cut on a non-delivering row'), ('PREMIUM-HELD', 'S8', 'Held TOS premium above the ceiling, push unproven'), ('BASE-CUT-DEAL', 'S7', 'Base cut while the deal mix is already ≤20% PP'),
    ('CLIMB-MIX-FIRST', 'S7', 'Price climb with TOS <30%'), ('PREMIUM-UNFUNDED', 'S8', 'Above-ceiling TOS on a non-push row'), ('PUSH-UNPROVEN', 'S8/S9', 'Above-ceiling climb failing a push test'),
    ('CUT-BEFORE-70', 'S8', 'TOS price cut on a push below 70% of its clicks'), ('CEILINGED', 'S9', 'Premium with no dollar loss ceiling'), ('BUDGET', 'S10', 'Budget raise not supported'),
    ('PREDICTION', 'S11', 'Claim larger than the step can buy'), ('STOCK', 'S13', 'Hero cannot ship'), ('STRATEGY', 'S14', 'Up-and-down bidding on a push'),
    ('NOOP / DUP', 'S15', 'Row does nothing / written twice'), ('HISTORY', 'S16', 'Re-proposes a held move'), ('RESIDUE', 'S17', 'TOS price falls as by-product of a base cut'),
    ('MOD-CAP', '—', 'Modifier above 500% working cap'), ('CLIMB-CAP', '—', 'Climb above +30%'), ('ROS-OK / PP-OK', '—', 'Row agrees with the document'), ('BASE-RAISE', '—', 'Base raised'), ('NONRANK-TOS-CUT', 'S18', 'TOS cut on a non-ranking row already inside its ceiling'),
]
table(['Code', 'Run-level finding', 'Meaning'], codes, widths=[4, 3, 19.5], size=8)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print('saved', OUT, VC, len(det), len(clean))
