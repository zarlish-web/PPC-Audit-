"""Situation-based corrections document for DBS4 run 20260924-5e8a0f10."""
import json, os, re
from collections import Counter, defaultdict
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

S = os.path.dirname(os.path.abspath(__file__))
CATS = json.load(open(f'{S}/cats.json'))
NR = json.load(open(f'{S}/nonrank.json'))
IMP = json.load(open(f'{S}/impact.json'))
A = json.load(open(f'{S}/a.json'))
import sys as _s0; _s0.path.insert(0, S); import diag as _dg0
KWSYN = {k: r.get('syntax') for k, r in _dg0.kw_rows('b4', '30d').items()}
SYNM = {r['groupName']: (r.get('market') or {}).get('marketCvr') for r in json.load(open(f'{S}/b46/b4_syntax_30d.json'))['rows']}
OUT = os.environ.get('OUT', '/home/user/PPC-Audit-/docs/DBS4_Corrections_by_Situation_20260924-5e8a0f10.docx')

NAVY = RGBColor(0x1F, 0x3A, 0x5F); GREY = RGBColor(0x55, 0x55, 0x55)


def pct(x, d=0):
    return '—' if x is None else f'{x*100:.{d}f}%'


def usd(x, d=2):
    return '—' if x is None else f'${x:,.{d}f}'


doc = Document()
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
for lvl, size in ((1, 16), (2, 13), (3, 11.5)):
    h = doc.styles[f'Heading {lvl}']; h.font.name = 'Calibri'; h.font.size = Pt(size); h.font.color.rgb = NAVY
    h.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
sec = doc.sections[0]
for m in ('left_margin', 'right_margin'):
    setattr(sec, m, Cm(2.0))
sec.top_margin = sec.bottom_margin = Cm(1.8)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill); tcPr.append(s)


def runs(p, text, bold=False, italic=False, size=None, color=None):
    for part in re.split(r'(\*\*[^*]+\*\*)', text):
        if not part:
            continue
        b = bold
        if part.startswith('**') and part.endswith('**'):
            part, b = part[2:-2], True
        r = p.add_run(part); r.bold = b; r.italic = italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = color
    return p


def para(text='', **kw):
    p = doc.add_paragraph(); runs(p, text, **kw); p.paragraph_format.space_after = Pt(5); return p


def lead(label, text):
    p = doc.add_paragraph(); r = p.add_run(label + ' '); r.bold = True; r.font.color.rgb = NAVY
    runs(p, text); p.paragraph_format.space_after = Pt(5); return p


def bullet(text):
    p = doc.add_paragraph(style='List Bullet'); runs(p, text); p.paragraph_format.space_after = Pt(2); return p


def table(headers, rows, widths=None, size=8.5):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = ''
        r = c.paragraphs[0].add_run(str(h)); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(c, '1F3A5F')
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


def by(cat):
    return [c for c in CATS if c['cat'] in (cat if isinstance(cat, (list, tuple)) else [cat])]


def eng(c):
    """what the run wrote on this campaign, in words"""
    e = c['em']; bits = []
    if e['tos']:
        d, a, b, s = e['tos']; bits.append(f"modifier {a:g}% → {b:g}%")
    if e['base']:
        d, a, b, s = e['base']; bits.append(f"base ${a:.2f} → ${b:.2f}")
    if e['budget']:
        d, a, b, s = e['budget']; bits.append(f"budget ${a:.2f} → ${b:.2f}")
    if not bits:
        return 'holds it'
    tail = ''
    if e.get('price_now') and e.get('price_eng') and abs(e['price_eng'] - e['price_now']) > 0.01:
        tail = f" — top-of-search price {usd(e['price_now'])} → {usd(e['price_eng'])}"
    return 'writes ' + ', '.join(bits) + tail


def eng_short(c):
    e = c['em']; bits = []
    if e['tos']:
        bits.append(f"mod {e['tos'][1]:g}→{e['tos'][2]:g}%")
    if e['base']:
        bits.append(f"base {'↓' if e['base'][0]=='down' else '↑'}{abs(e['base'][2]/e['base'][1]-1):.0%}")
    if e['budget']:
        bits.append(f"budget ${e['budget'][1]:g}→${e['budget'][2]:g}")
    if not bits:
        return 'holds'
    if e.get('price_now') and e.get('price_eng') and abs(e['price_eng'] - e['price_now']) > 0.01:
        bits.append(f"TOS {usd(e['price_now'])}→{usd(e['price_eng'])}")
    return '; '.join(bits)


def moved(c):
    e = c['em']; return bool(e['tos'] or e['base'] or e['budget'])


def pdir(c):
    return c['em'].get('price_dir')


def rank_s(c):
    if not c['rank_now']:
        return 'no rank on file'
    s = f"rank {c['rank_30']} → {c['rank_now']} in thirty days" if c['rank_30'] else f"rank {c['rank_now']}"
    return s + (f", target {c['rank_tgt']}" if c['rank_tgt'] else '')


def mix_s(c, w):
    r = c['R'][w]
    if not r['t3']:
        return 'no clicks'
    return f"{r['t3']} clicks — {r['tos']['c']} top of search, {r['detail']['c']} product pages, {r['other']['c']} rest of search ({pct(r['tos_sh'])} / {pct(r['pp_sh'])} / {pct(r['other']['c']/r['t3'])})"


def story(c):
    R = c['R']; b = []
    b.append(f"{rank_s(c)}.")
    b.append(f"90 days: {mix_s(c, 'd90')}, {R['d90']['orders']} orders.")
    b.append(f"Last 14 days: {mix_s(c, 'd14')}.")
    b.append(f"Deal so far (09-15 → 09-24): {R['deal8']['tos']['c']} top-of-search clicks ({c['deal_tos_day']:.1f}/day, against {c['pre_tos_day']:.1f}/day in the 31 days before); last 3 days {R['d3']['t3']} clicks.")
    if c['need_day']:
        b.append(f"Plan needs {c['need_day']*7:.0f} paid clicks a week ({c['need_day']:.1f}/day).")
    if c['budget']:
        b.append(f"Budget ${c['budget']:.2f}/day, last 7 days {pct(c['util7'])} used.")
    _g = KWSYN.get(c.get('kw')) or c['group']
    _mk = SYNM.get(_g) or SYNM.get((_g or '').split('|')[0])
    if c['tos_rate'] and _mk:
        b.append(f"Top of search converts {pct(c['tos_rate'],1)} against a market {_mk:.1f}% for {_g} (bar {3 * _mk:.1f}%).")
    b.append(f"The run {eng(c)}.")
    return ' '.join(b)


def example(c, extra=''):
    p = doc.add_paragraph(); r = p.add_run(c['short']); r.bold = True
    runs(p, ' — ' + story(c) + ((' ' + extra) if extra else ''))
    p.paragraph_format.space_after = Pt(5); p.paragraph_format.left_indent = Cm(0.4)


def top(cs, n=3, key=None):
    key = key or (lambda c: -(c['R']['d14']['spend'] + c['R']['deal8']['spend'] + (6 - (['VHSV', 'HSV', 'MSV', 'LSV', 'VLSV', 'NOSV'].index(c['tier']) if c['tier'] in ['VHSV', 'HSV', 'MSV', 'LSV', 'VLSV', 'NOSV'] else 6)) * 10))
    return sorted(cs, key=key)[:n]


def eng_compact(t):
    """collapse repeated 'bid a→b' items into one phrase"""
    import re as _re
    parts = [x.strip() for x in t.split(',')]
    bids = [x for x in parts if _re.match(r'bid [\d.]+→[\d.]+$', x)]
    rest = [x for x in parts if x not in bids]
    if len(bids) > 1:
        tos_ = sorted({x.split('→')[1] for x in bids})
        rest.insert(0, f"cuts {len(bids)} bids to ${'/$'.join(tos_)}" if all(float(x.split()[1].split('→')[0]) > float(x.split('→')[1]) for x in bids) else f"moves {len(bids)} bids")
    else:
        rest = bids + rest
    out = []
    for x in rest:
        m = _re.match(r'tos ([\d.]+)→([\d.]+)$', x)
        out.append((f"{'cuts' if float(m.group(2)) < float(m.group(1)) else 'raises'} the top-of-search modifier {m.group(1)}% → {m.group(2)}%") if m else x)
    return ', '.join(out).replace('holds', 'holds it')


def restored(c):
    """the 10 September bid cuts were put back by a later bid move to the pre-cut value (or higher)"""
    cuts = [(lab, float(bf), float(af)) for lab, bf, af in c['restore'] if lab not in ('TOS modifier', 'ROS modifier', 'PP modifier') and float(af) < float(bf)]
    if not cuts:
        return False
    ups = [l for l in c['later'] if l[1] == 'bid']
    return all(any(float(l[4]) >= bf for l in ups) for lab, bf, af in cuts)


def dark_extra(c):
    """restore the base the 10 September round cut, and solve the modifier at the new top-of-search price"""
    if not c['restore']:
        return ''
    if restored(c):
        return '; already restored: the 10 September cuts were put back later — go straight to the push'
    cuts = [(bf, af) for lab, bf, af in c['restore'] if lab not in ('TOS modifier', 'ROS modifier', 'PP modifier') and float(af) < float(bf)]
    mods = [f"top-of-search modifier {bf}% → {af}%" for lab, bf, af in c['restore'] if lab == 'TOS modifier']
    p = c.get('push') or {}
    if cuts and p.get('price1'):
        b0 = max(float(cuts[0][0]), p['price1'] / 10); m = (p['price1'] / b0 - 1) * 100
        return (f"; restore first: the 10 September round cut its base ${float(cuts[0][0]):.2f} → ${float(cuts[0][1]):.2f}" + (f" (base now {usd(c['base'])})" if c.get('base') else '') + (f" and moved the {mods[0]}" if mods else '') +
                f" — write the base back to ${b0:.2f}" + (" (above the pre-cut value: at the new price the 900% wall needs it)" if b0 > float(cuts[0][0]) + 0.004 else "") + f" and solve the modifier at the new price: {m:.0f}% (instead of the modifier above)")
    return '; the 10 September round changed it (' + '; '.join(mods) + ') — read it the day after the push'


def issues(cs, n=3, bad=None):
    """examples where what the run did is the problem: the run's price move goes against the correction"""
    bad = bad or (lambda c: c['em'].get('price_dir') != 'up' and not (c.get('push') or {}).get('at_req'))
    return top([c for c in cs if bad(c)] or cs, n)


def push_price(c):
    if c['util7'] is not None and c['util7'] >= 0.8:
        return c['em'].get('price_now'), f"budget first — {pct(c['util7'])} of ${c['budget']:.2f} used in the last 7 days: ${c['budget']:.2f} → ${c['budget']*1.3:.2f}; price step only once it stops capping"
    p = c['em'].get('price_now')
    if not p:
        return None, 'no bid on file'
    lim = c['limit'][1]
    if p >= lim:
        return p, f"already at or over the {c['group']} limit {usd(lim)} — hold, and check the ad, the child and eligibility"
    new = min(p * 1.25, lim)
    return new, f"{usd(p)} → {usd(new)} ({new/p-1:+.0%}{', stopped at the ' + c['group'] + ' limit ' + usd(lim) if new == lim else ''})"


# ================================== document ==================================
t = doc.add_paragraph(); runs(t, 'Corrections to the 24 September run — Decolure Bamboo Sheets 4-Piece', bold=True, size=18, color=NAVY)
para('This run re-points B4’s focus on the operator’s rulings of 24 September: Bamboo|California King and Bamboo|Cooling are in focus (20 exact ranking campaigns); the Bamboo, Queen, King and Full terms that led the last run are out of focus. The Best Deal runs 15 → 28 September and the engine still does not read it. The goal is unchanged: climb the in-focus keywords by buying top-of-search clicks every day to the end of the deal — every in-focus exact ranking campaign is pushed on top of search until its top-of-search clicks arrive, none held for being thin or for review. What bounds the push is money: no campaign steps past a top-of-search cost per order of 3× contribution, the push runs inside one spend envelope, and new steps stop if weekly TACoS passes 21.7% (the run’s own projection). The target for where clicks land is top of search above 70% and product pages under 20%. Out-of-focus campaigns take no new money and are judged on their own numbers; the ones that convert at the top get a two-week test.')
para('Each section gives the rule, what the run did, two or three campaigns where the run’s action is the problem, and the correction. Everything the 21 September document raised has been re-checked on data to 24 September; where a finding changed, the section says so. Ranks throughout are the tracker’s 7-day median — the engine reads single days, and on “cooling bed sheets” that is 86 today against a 7-day median of 37. Part D answers Erik’s question for B4 — are we short of top-of-search traffic, or short of CTR/CVR at the top — for the new focus, with the performance-vs-tuning history, competitors, the campaign types that should also be running and the metrics the app should read.')

IN = [c for c in CATS if c['focus_in']]
OUTC = [c for c in CATS if not c['focus_in']]
PUSHED = [c for c in IN if c['push']]
PLAN_RATE = json.load(open(f'{S}/meta.json'))['plan_rate']


def mixtot(cs, w):
    t = sum(c['R'][w]['tos']['c'] for c in cs); p = sum(c['R'][w]['detail']['c'] for c in cs); o = sum(c['R'][w]['other']['c'] for c in cs)
    s = t + p + o
    return t, p, o, (t / s if s else None), (p / s if s else None)


doc.add_heading('Where clicks land today', 2)
rows = []
for lab, cs in (('In-focus exact ranking', IN), ('Out-of-focus exact ranking', OUTC), ('All exact ranking', CATS)):
    for w, wl in (('d14', 'last 14 days'), ('deal8', 'deal, 10 days')):
        t, p, o, ts, ps = mixtot(cs, w)
        rows.append([lab if w == 'd14' else '', wl, t, p, o, pct(ts), pct(ps)])
table(['Campaigns', 'Window', 'Top of search', 'Product pages', 'Rest of search', 'TOS share', 'PP share'], rows, widths=[4.5, 2.6, 2, 2, 2, 1.8, 1.8], size=8.5)
para('In focus the mix is already inside the target; the job there is volume — the 20 in-focus campaigns take about 10 top-of-search clicks a day between them. The product-page leak sits in the out-of-focus campaigns, where most of B4’s spend now is.')

doc.add_heading('Windows and sources', 2)
para('Amazon’s campaign placement report (Command Center), per campaign: 90 days (06-27 → 09-24) for conversion; the last 14 days (09-11 → 09-24) for where clicks land; the last 7 and 3 days for whether a campaign is still serving and for budget use; the deal so far (09-15 → 09-24, 10 days); the 31 days before it (08-15 → 09-14); and 19–21 vs 23–24 September around the 22 September round. Top-of-search impression share is Amazon’s per-target figure over 30 days (08-26 → 09-24) and over the deal. Orders in the last seven days are still filling in (attribution settled to 18 September). Stock is the run’s own read, with the planner figures from the 25 September review where they add to it.')

sec_no = [0]
part = ['A']


def section(title):
    sec_no[0] += 1
    doc.add_heading(f'{part[0]}.{sec_no[0]} {title}', 1)


names = {'OUT_TEST': 'B · Out of focus, converts — two-week test', 'OUT_FLAGSHIP': 'B · Out of focus, flagship — hold flat', 'IN_PAUSED': 'A · In focus — keyword paused (duplicate)', 'IN_PUSH': 'A · In focus — push top of search', 'IN_LEAK': 'A · In focus — base cut + push', 'IN_DARK': 'A · In focus — restore + push', 'IN_COLLAPSE': 'A · In focus — push + investigate', 'IN_ONTARGET': 'A · In focus — delivering, hold', 'THIN_PUSH': '1 · Thin, in focus, volume — push', 'THIN_ZERO_IN': '1 · Thin (zero), in focus — push', 'THIN_TINY': '2 · Thin, in focus, low volume — hold',
         'THIN_OUT': 'B · Out of focus, thin — hold', 'THIN_ZERO_OUT': 'B · Out of focus, zero — hold', 'LEAK': 'B · Out of focus, leak — base cut',
         'SHORT_PRICE': '5 · Mix right, short — raise modifier', 'SHORT_BUDGET': '5 · Mix right, short — raise budget', 'SHORT_ATLIMIT': '5 · At limit — check eligibility',
         'OUT_WORKING': 'B · Out of focus, working — hold flat', 'OUT_WEAK': 'B · Out of focus, weak — taper', 'DARK': 'B · Out of focus, went dark — restore', 'FADED': 'B · Out of focus, faded — investigate',
         'COLLAPSE': 'B · Out of focus, rank collapse — freeze', 'ROS_HEAVY': '9 · Rest-of-search heavy', 'ON_TARGET': '9 · On target — hold'}
doc.add_heading('Part A — In-focus exact ranking campaigns: push top of search every day', 1)
lead('The rule.', 'From 09-25 to the end of the deal (09-28) every in-focus exact ranking campaign is pushed on the top-of-search modifier, every day, until its required top-of-search clicks arrive. Nothing is held for being thin, for having no clicks yet, or for review — a campaign that is not getting clicks is not in the auction, and only the top-of-search price can put it there.')
lead('How big each day’s step is.', 'Sized by the delivery gap — top-of-search clicks a day over the deal so far (10 days) against the requirement: under 30% delivered +30%; 30–70% +20%; over 70% +10%; at or over the requirement, no step. Where the last raise (15 September) did not lift impression share, the step is halved: price that bought no share buys no more by being repeated. Rank distance only breaks ties. A campaign with no click requirement on file takes +20% — a stated departure from the logic document, which would hold it at the ceiling with no premium; these are low-volume terms, and the push doubles as the eligibility check.')
lead('What stops it.', f"Five things, each written on the row. (1) The loss stop: the top-of-search price may not pass the point where a top-of-search order costs more than 3× contribution — 3 × contribution (the advertised child’s at today’s price; ${sum(c['push']['contrib'] for c in PUSHED if c['push'].get('contrib')) / max(1, sum(1 for c in PUSHED if c['push'].get('contrib'))):.2f} on average across these rows) × the campaign’s top-of-search conversion rate, set as the framework (25 September version) sets it: under 15 top-of-search clicks in 90 days, the child’s planning rate; 15–49 clicks with at least one order, a blend weighted by clicks ((clicks − 15) ÷ 35 on the campaign’s own rate); 15–49 with no order yet, the child’s rate — no evidence is not evidence of zero; 50 or more, the campaign’s own rate, and there a rate of zero sets the ceiling to zero and top of search stops being priced. No child-level planning rate exists on this account (the run says so), so the rate of the campaign’s syntax group across all enabled exact ranking campaigns stands in for it (the product’s, {PLAN_RATE:.1%}, where the group has under 50 clicks). Every pushed row carries its cost and loss per order at the new price. (2) The share stop: impression share at 40% or more and not rising after the last step — the requirement is overstated, not the price; it is re-based from actual volume. (3) The reachability check: delivered clicks ÷ impression share is what winning the whole auction would buy; where the requirement is above that — true of most California King rows — the campaign is pushed toward share and graded on share and 7-day rank, not on an unbuyable click count. (4) The envelope (below). (5) The product guard: if weekly TACoS passes 21.7% — the run’s own projection, 1.2× the 18% ceiling of the ranking band — no new step is written and every row holds at its last price until it is back under (operator 2026-09-25). The deal week ran 19.4%.")
lead('What every write covers.', 'The base is held unless product pages are over 20% (then it comes down in the same write). The top-of-search modifier applies to every target in the campaign; a base cut is applied as the same percentage to every enabled target, and the price quoted is the plan keyword’s. Amazon caps the modifier at 900%: where a step would pass it (“Bamboo Cooling Sheets” is at 718% today) the base carries the rest of the raise (base = price ÷ 10, modifier 900%) and product-page share is read the next day. Every row is priced from live values on the morning of the write: the engine moved 10 bids and modifiers on 24 September, after the audit read them, and the rows here are priced from those. Where 80% or more of the budget was used in the last 7 days, the budget goes up 30% in the same write.')
lead('The daily read.', 'Each morning to 09-28, per campaign: top-of-search clicks yesterday, impression share, where the clicks landed, budget use and hours out of budget. The two levers are graded separately: the price step on impression share (rose → keep stepping; flat → halve the next step), the budget raise on hours out of budget. Clicks at the requirement — stop stepping. Clicks landing on product pages — cut the base, don’t stop the top-of-search push. Still zero after two steps — check the ad is live, the child it serves, and the listing, while the push continues.')
lead('After the deal (from 09-29).', 'The deal closes and every row is read. A campaign that reached its requirement moves to cost-per-click evaluation: probe down 3–5% a step while click share holds. One that did not reach it does not keep stepping: its top-of-search price steps down to break-even (contribution × its top-of-search conversion rate) over two writes four days apart, unless its 7-day rank has moved into the target range, in which case it holds one week at the push price and is read again. The decision is written on the row.')
nup = sum(1 for c in IN if c['push'] and c['em'].get('price_dir') == 'up')
nheld = sum(1 for c in IN if c['push'] and not moved(c))
ncut = sum(1 for c in IN if c['push'] and c['em'].get('price_dir') == 'down')
lead('What the run did.', f"Of the {len(PUSHED)} in-focus campaigns that should be pushed, the run raised the top-of-search price on {nup}, cut it on {ncut} and left it where it was on {len(PUSHED) - nup - ncut} ({nheld} untouched, {len(PUSHED) - nup - ncut - nheld} with other moves that leave the top-of-search price unchanged). It held rows for being thin, for no rank read, for a rank collapse, for sitting at its market bound, and on budget.")

section(f'The push in numbers ({sum(1 for c in PUSHED if c["push"]["step"] > 0)} stepped, {sum(1 for c in PUSHED if c["push"].get("at_req"))} at requirement, {len(by("IN_PAUSED"))} with its keyword paused)')
lead('What the correction writes.', 'Every in-focus campaign short of its clicks gets a top-of-search step sized by its delivery gap, in the same write as any base cut or budget raise it needs, inside the loss stop. The sections below take each situation in turn with the campaigns where the run got it most wrong; every campaign follows the same rule.')
rows = []
for lo, hi, lab in ((0.25, 1, '+30% — under 30% of required clicks delivered'), (0.175, 0.25, '+20% — 30–70% delivered (or no requirement on file)'), (0.125, 0.175, '+15% — +30% halved: share did not rise after the last raise'), (0.075, 0.125, '+10% — over 70% delivered, or +20% halved'), (-1, 0.075, 'No step — at requirement, share stop or loss stop')):
    cs_ = [c for c in PUSHED if lo < c['push']['step'] <= hi]
    if not cs_: continue
    los = [c['push']['loss'] for c in cs_ if c['push']['loss'] is not None]
    rows.append([lab, len(cs_), sum(1 for c in cs_ if pdir(c) == 'up'), sum(1 for c in cs_ if not moved(c) or pdir(c) == 'down'),
                 sum(1 for c in cs_ if 'loss stop' in c['push']['step_why']), sum(1 for c in cs_ if c['push']['unreachable']),
                 (lambda _m: f"${_m:.0f}" if _m >= 0.5 else (f"profit ${-_m:.0f}" if _m <= -0.5 else 'break-even'))(sorted(los)[len(los) // 2]) if los else '—', sum(1 for c in cs_ if c['push']['budget1'] != c['push']['budget0'])])
table(['Step', 'Campaigns', 'Run raised TOS', 'Run cut or held', 'At the loss stop', 'Requirement above what the auction holds', 'Median loss per order at new price', 'Budget +30%'], rows, widths=[5.0, 1.4, 1.5, 1.5, 1.4, 2.2, 2.0, 1.4], size=7.5)
_dsp = sum(c['R']['deal8']['spend'] for c in PUSHED) / 10
_proj = sum(c['R']['deal8']['spend'] / 10 * ((c['push']['price1'] or 0) / c['push']['price0']) for c in PUSHED if c['push']['price0'])
_full = sum((c['need_day'] or 0) * (c['push']['price1'] or c['push']['price0'] or 0) for c in PUSHED)
lead('The envelope.', f"These campaigns spent ${_dsp:,.0f} a day over the deal so far, against about $1,140 a day across the whole product. The envelope is 1.5× that — **${_dsp * 1.5:,.0f} a day**, **${_dsp * 1.5 * 4:,.0f}** for 09-25 → 09-28 (operator 2026-09-25). At the new prices with clicks unchanged these campaigns would spend about ${_proj:,.0f} a day; the rest is room for the clicks the push buys. Rows keep stepping daily while impression share rises, inside the loss stop and the TACoS guard, until the envelope is spent. Buying every in-focus requirement at the new prices would cost about ${_full:,.0f} a day — more than the auction holds on most of these terms (reachability), which is why share, not clicks, is the grade.")
para('TOS price = base × (1 + TOS modifier); the modifier is solved from the price decided and the base.', size=8.5, color=GREY)


def insit(cs, title, rule, correction, extra=None, n=3):
    if not cs:
        return
    section(title)
    lead('The rule.', rule)
    up = sum(1 for c in cs if c['em'].get('price_dir') == 'up'); dn = sum(1 for c in cs if c['em'].get('price_dir') == 'down'); hd = sum(1 for c in cs if not moved(c))
    lead('What the run did.', f"Raised the top-of-search price on {up}, cut it on {dn}, held {hd}.")
    for c in issues(cs, n):
        p = c['push']
        corr = (f"Correction: {'+' + format(p['step'], '.0%') if p['step'] else 'no step'} ({p['step_why']}) — TOS {usd(p['price0'])} → {usd(p['price1'])}; a top-of-search order then costs up to {usd(p['cpo'], 0)} ({('a loss of ' + usd(p['loss'], 0)) if p['loss'] >= 0 else ('still a profit of ' + usd(-p['loss'], 0))} against {usd(p['contrib'])} contribution; stop at {usd(p['stop_price'])})" + (f"; impression share {p['is30']:.1f}% (30 days) → {p['isd']:.1f}% (deal so far)" if p['is30'] is not None and p['isd'] is not None else '') + ('; the requirement is above what the whole auction holds — grade on share' if p['unreachable'] else '')) if p and p['price0'] else 'Correction: push (no bid on file — set one)'
        if p and p['base1'] and p['base0'] and abs(p['base1'] - p['base0']) > 0.004:
            corr += f"; {p['base_why']}: base {usd(p['base0'])} → {usd(p['base1'])}"
        if p and p['mod1'] is not None:
            corr += f"; modifier {p['mod1']:.0f}%"
        if p and p['budget1'] != p['budget0']:
            corr += f"; budget ${p['budget0']:.2f} → ${p['budget1']:.2f}"
        if p and p.get('price1') and c['em'].get('price_eng') and c['em']['price_eng'] > p['price1'] + 0.01 and c['em'].get('price_now'):
            corr += f"; the run’s own write goes further (top of search {usd(c['em']['price_now'])} → {usd(c['em']['price_eng'])}, {c['em']['price_eng'] / c['em']['price_now'] - 1:+.0%} in one write) — step it daily instead, so each step is graded on share"
        if extra:
            corr += extra(c)
        example(c, corr + '.')
    lead('Correction.', correction)


thin = [c for c in PUSHED if c['cat'] == 'IN_PUSH' and (c['R']['d14']['t3'] < 15 and c['R']['deal8']['t3'] < 15)]
insit(thin, f'{len(thin)} in-focus campaigns taking under 15 clicks — the thin ones, pushed not held',
      'A ranking campaign with almost no clicks is barely in the auction; trimming its price makes that less likely to change, and holding it wastes a day. Push the top-of-search modifier — the only lever that produces clicks on a row that isn’t getting any. This includes the low-volume (VLSV/NOSV) keywords and the ones with no clicks at all: each is cheap to test, and the push doubles as the eligibility check.',
      f"Push all {len(thin)} by the delivery-gap step, inside the loss stop. {sum(1 for c in thin if c['push']['zero'])} have taken no click in 90 days or in the deal — if still zero after two daily steps, check the ad, the child and the listing while the push continues. Reverse every cut or hold the run wrote on these.")
short = [c for c in PUSHED if c['cat'] == 'IN_PUSH' and c not in thin]
insit(short, f'{len(short)} in-focus campaigns with the right mix, short of their clicks',
      'Where 70%+ of clicks already land at top of search and delivery is short of the requirement, the lever is the top-of-search price — and the budget where it is running out. Both move in the same write. Impression share is the live read: rising with price means keep stepping; at 40% or more and flat means the requirement is overstated and the push stops (none is there today — share is 1–6% on almost every row).',
      'Push by the delivery-gap step; raise the budget 30% in the same write wherever the last 7 days used 80% or more of it. On most in-focus rows budget is not what holds clicks back (the median used a quarter of its budget in the last 7 days), so the lever is price; “Bamboo Cooling Sheets” is the exception at 108% and takes the budget raise with the step.',
      extra=lambda c: (f" It runs up-and-down bidding and paid {usd(c['R']['deal8']['tos']['s']/c['R']['deal8']['tos']['c'])} per top-of-search click in the deal so far against a written {usd(c['push']['price0'])} — switch it to fixed, starting near what dynamic actually paid rather than at the written figure plus a step — switching at the written price would roughly halve its bid" if c['push']['ud'] and c['R']['deal8']['tos']['c'] else ''))
leak = by('IN_LEAK')
insit(leak, f'{len(leak)} in-focus campaigns with product pages over 20% — cut the base and push top of search in the same write',
      'Product pages over 20% means money landing on the placement that does not move rank. On an in-focus campaign the fix is one combined write: the base comes down (sized to the leak, never more than 25% where product pages carry orders) and the top-of-search price goes up by the delivery-gap step. The base step is graded on product-page share, the price step on top-of-search clicks, so neither hides the other.',
      'Write both moves together. Read product-page share and top-of-search clicks daily; if product pages don’t fall, the leak isn’t price-driven — restore the base and keep the top-of-search push.')
dark = by('IN_DARK')
insit(dark, f'{len(dark)} in-focus campaigns that went dark or faded — restore, then push',
      'A campaign with a real record that stopped serving usually stopped after a cut. Put back the prices it last served at, and push top of search from there in the same write — a restore alone wastes a day.',
      'Restore the values it last served at where they have not been put back; where a later round already restored them and it still isn’t serving, go straight to the push and check the ad, child and eligibility the same day.',
      extra=lambda c: dark_extra(c))
col = by('IN_COLLAPSE')
insit(col, f'{len(col)} in-focus campaigns whose keyword lost more than 10 positions — push and investigate the same day',
      'A rank collapse has a cause price alone may not fix — the listing, the child the ad serves, a rival’s deal, or the term itself. The push still goes in; the cause is checked the same day, not before it.',
      'Push by the delivery-gap step and, the same day: check the listing and its badge, which child the ad serves and its stock, the rival now ahead and whether it is on a deal, and the term’s search volume. If the push buys clicks and rank keeps falling, the cause is not price — stop stepping and fix it.')
ont = by('IN_ONTARGET')
if ont:
    section(f'{len(ont)} in-focus campaign already delivering its clicks — the one exception')
    lead('The rule.', 'A campaign already delivering its required top-of-search clicks is not pushed further. If it is at its rank target and converting poorly, that is the one case to evaluate lowering cost per click; after the deal, probe the price down 3–5% and watch click share.')
    for c in ont:
        example(c, 'Correction: hold the price' + (f"; keep the budget raise (it used {pct(c['util7'])} of its budget in the last 7 days)" if (c['util7'] or 0) >= 0.8 else '') + '; after 09-28, evaluate cost per click.')
pz = by('IN_PAUSED') + [c for c in PUSHED if not c['push']['price0']]
if pz:
    section(f'{len(pz)} in-focus campaign{"s" if len(pz) != 1 else ""} that cannot serve — keyword paused or no bid on file')
    lead('The rule.', 'A campaign whose keywords are all paused cannot serve at any price. If the term is owned by another exact campaign, the pause is right — two instances of the same exact term split the read. If no other campaign carries it, the pause has taken an in-focus term out of ranking and needs a decision.')
    for c in pz:
        if c['cat'] == 'IN_PAUSED':
            example(c, 'Its only keyword is paused and no other enabled exact campaign carries the term, so the term has left the ranking programme without a decision. Correction: re-enable the keyword at its last serving values and put it in the push — or, if the pause was deliberate, take the campaign out of focus and say why.')
        else:
            _m = c['tos_mod'] or 0
            example(c, f"It is enabled with an enabled target but carries no bid on file, so it cannot serve and the push has nothing to step. Correction: set its bid so the top-of-search price sits at its market bound ({usd(c['limit'][1])}) at the current {_m:.0f}% modifier — a base of {usd(c['limit'][1] / (1 + _m / 100))} — then it joins the push on the next day’s read.")
hb = [c for c in PUSHED if c['push']['hero_bad']]
if hb:
    section(f'{len(hb)} in-focus campaigns advertising a hero that can’t ship — re-point the ad the same day')
    lead('The rule.', 'A push on a child that runs out before the next arrival rents the position instead of buying it. Switch the ad to the serving child the same day as the push. On Queen this applies to the in-focus campaign only: “Bamboo Cooling Sheets” (MSV) moves from Queen White (79 units, about 22 days, next arrival 27 October) to Queen Olive (337 units); the 14 out-of-focus campaigns on Queen White ($662 in the last 14 days) stay on the hero until stock lands (operator 2026-09-25). On California King the run already stages the swap to Cal King Olive — do it by hand, since the loader skips every swap, and watch conversion on the slower child in the first week.')
    lead('Check first.', 'Which child the rank tracker reads for each term. If a term is tracked on the hero child and the ad moves to another colour, the push buys sales the tracker does not watch and the read shows a miss that is not one — confirm the tracked child before the write, and grade on the child the sales land on.')
    for c in top(hb, 3):
        example(c, f"It advertises {c['serving']} (room: {c['stock'].get('hero_room')}); the serving child is {c['stock'].get('serving_child')} with {c['stock'].get('serving_available')} available. Correction: re-point the ad to the serving child in the same write as the push.")

# ================= Part B — out of focus =================
part[0] = 'B'; sec_no[0] = 0
doc.add_heading('Part B — Out-of-focus exact ranking campaigns: no new money, judged on their own numbers', 1)
cs = by('OUT_TEST')
if cs:
    section(f'{len(cs)} out-of-focus campaigns that convert at the top — a two-week test')
    lead('The rule.', 'Focus stays as this run sets it (Bamboo|California King and Bamboo|Cooling); everything else is out of focus. But an out-of-focus term that already converts at top of search above the bar — 3× the market CVR of its group, on 15 or more top-of-search clicks in 90 days — is tested rather than held: top-of-search price +10% for two weeks (09-25 → 10-08), inside the same loss stop (3× contribution per top-of-search order), on a child that can ship (operator 2026-09-25). A campaign whose rank collapsed is frozen instead (B.4) — the collapse rule wins over the test. A campaign that went dark gets its pre-cut base back first.')
    lead('The test budget.', f"No test budget is cut. Each test keeps its current budget, or takes one sized to about 15 top-of-search clicks over the two weeks at its test price (price × 15 ÷ 14 a day, at least $5) where that is higher: {usd(sum(c['test']['budget1'] for c in cs), 0)} a day across the {len(cs)}, against {usd(sum(c['budget'] or 0 for c in cs), 0)} today. At current clicks the +10% adds about $12 a day. Out of focus takes no other new money.")
    lead('The read on 10-08.', 'Keep the test price where top-of-search clicks rose and top-of-search conversion stayed above the bar; put it back where they did not. The result is evidence for the next focus decision on Bamboo, King, Queen and Full, not a change of focus.')
    _pri = Counter(c['test']['prior'] for c in cs); _grp = Counter(c['group'] for c in cs)
    lead('What the run did.', f"Raised the top-of-search price on {sum(1 for c in cs if pdir(c) == 'up')}, cut it on {sum(1 for c in cs if pdir(c) == 'down')}, held {sum(1 for c in cs if not moved(c))}. By group: " + ', '.join(f'{g} {n}' for g, n in _grp.most_common()) + '. Their situation otherwise: ' + ', '.join(f"{names.get(k, k).split(' — ')[0].split(', ')[-1]} {n}" for k, n in _pri.most_common()) + '.')
    for c in top(cs, 3, key=lambda c: -c['R']['d90']['tos']['c']):
        t = c['test']
        if t['price0']:
            corr = (f"Converts {t['ord90']} of {t['tos90']} top-of-search clicks ({t['rate']:.0%}), above the 3× market bar. Correction: test +10% — TOS {usd(t['price0'])} → {usd(t['price1'])}; a top-of-search order then costs up to {usd(t['cpo'], 0)} "
                    f"({('a loss of ' + usd(t['loss'], 0)) if t['loss'] >= 0 else ('still a profit of ' + usd(-t['loss'], 0))} against {usd(t['contrib'])} contribution; stop at {usd(t['stop'])})")
        else:
            corr = (f"Converts {t['ord90']} of {t['tos90']} top-of-search clicks ({t['rate']:.0%}), above the 3× market bar. It has no enabled priced target on file today. Correction: re-enable its keyword and set the top-of-search price at its group’s market bound ({usd(c['limit'][1])}), inside the stop ({usd(t['stop'])}), as the test")
        corr += (f"; budget {usd(t['budget0'])} → {usd(t['budget1'])} (about 15 top-of-search clicks in two weeks)" if abs(t['budget1'] - (t['budget0'] or 0)) > 0.004 else f"; budget held at {usd(t['budget0'])}")
        if t['repoint']:
            corr += f"; advertise {t['repoint']} — the hero {c['serving']} is short"
        if t['prior'] in ('DARK', 'FADED'):
            corr += dark_extra(dict(c, push=dict(price1=t['price1']))).replace('the push', 'the test')
        if t['prior'] == 'LEAK':
            _r = c['R'][c['mixw']]; _pp = _r['pp_sh'] or 0; _st = min(0.10 if _pp < 0.30 else 0.20 if _pp < 0.50 else 0.35, 0.25 if (_r['detail']['o'] + _r['other']['o']) else 0.50)
            corr += f"; product pages take {pct(_pp)} of its clicks — cut the base {_st:.0%} in the same write, with the modifier solved so top of search sits at the test price"

        if t['prior'] == 'COLLAPSE':
            corr += '; its rank collapsed — run the cause check the same day'
        example(c, corr + '; read on 10-08')
    lead('Correction.', f'Test all {len(cs)} for two weeks; do not cut any of them in the meantime.')
fl = by('OUT_FLAGSHIP')
if fl:
    c = fl[0]; t = c['test']
    section('The flagship — held flat, not tested')
    lead('The rule.', 'The flagship “Bamboo Sheets” (VHSV) qualifies for the test on its record, but it is the largest single spend on the product and the focus has moved off its keyword. It holds flat: no raise, no cut (operator 2026-09-25).')
    example(c, f"It converts {t['ord90']} of {t['tos90']} top-of-search clicks ({t['rate']:.0%}), above the 3× market bar, and a top-of-search order costs about {usd(t['price0'] / t['rate'], 0)} at today’s price against {usd(t['contrib'])} contribution. A +10% test here alone would add about $34 a day of out-of-focus money. Correction: hold top-of-search price, base and budget where they are; read it weekly with the TACoS guard.")

cs = by(['THIN_OUT', 'THIN_ZERO_OUT'])
section(f'{len(cs)} out-of-focus campaigns under 15 clicks — hold them flat')
lead('The rule.', 'A campaign under 15 clicks has no readable conversion rate; out of focus means no new money, not a cut. A cut on a row spending nothing releases nothing to the focus — it only leaves the row a rung lower for whenever its group comes back into focus.')
lead('What the run did.', f"Held {sum(1 for c in cs if not moved(c))}; moved {sum(1 for c in cs if moved(c))} — raised the price on {sum(1 for c in cs if pdir(c)=='up')}, cut it on {sum(1 for c in cs if pdir(c)=='down')}.")
for c in top([c for c in cs if moved(c)] or cs, 2):
    example(c, 'Correction: hold at today’s price.')
lead('Correction.', 'Hold every one — reverse the cuts and the raises. Where an out-of-focus term climbs organically on no paid clicks, record it as evidence for the next focus decision.')

cs = by('LEAK')
if cs:
  section(f'{len(cs)} out-of-focus campaigns with product pages over 20% — cut the base, top of search held')
  lead('The rule.', 'Out of focus, the leak is still money landing on the placement that does not move rank — and it is where most of the product’s product-page clicks sit. Cut the base sized to the leak (10% at 20–30%, 20% at 30–50%, 35% above; never more than 25% where product pages carry orders), re-solve the modifier so the top-of-search price holds to the cent. No price climb.')
  for c in cs:
      r = c['R'][c['mixw']]; pp = r['pp_sh']; ords = r['detail']['o'] + r['other']['o']
      step = min(0.10 if pp < 0.30 else 0.20 if pp < 0.50 else 0.35, 0.25 if ords else 0.50)
      nb = c['base'] * (1 - step) if c['base'] else None
      nm = (c['em']['price_now'] / nb - 1) * 100 if (nb and c['em'].get('price_now')) else None
      c['fix'] = (step, nb, nm)
  for c in top(cs, 3, key=lambda c: -(c['R'][c['mixw']]['pp_sh'] or 0)):
      step, nb, nm = c['fix']
      example(c, f"Correction: base −{step:.0%} → {usd(nb)}, modifier {nm:.0f}% so top of search stays at {usd(c['em'].get('price_now'))}." if nb and nm is not None else 'Correction: base cut sized to the leak; top of search held.')
  lead('Correction.', f'All {len(cs)} get the base cut sized to their leak with the top-of-search price held; none gets a price climb.')

cs = by(['OUT_WORKING', 'OUT_WEAK'])
if cs:
    section(f'{len(cs)} out-of-focus campaigns with a readable record — hold what works')
    lead('The rule.', 'Out of focus means no new money; it does not mean take away what is working. A campaign converting at or above the market at top of search, with the right mix or climbing, is held flat — no increase, no cut.')
    for c in issues(cs, 3, bad=moved):
        example(c, 'Correction: ' + ('hold flat — no cut, no raise.' if c['cat'] == 'OUT_WORKING' else 'taper stands.'))

cs = by(['DARK', 'FADED'])
if cs:
    section(f'{len(cs)} out-of-focus campaigns that went dark or faded')
    lead('The rule.', 'A campaign that stopped serving after a cut gets its pre-cut prices back and a next-day read; one that faded with nothing changed is an eligibility question, not a price one.')
    for c in top(cs, 3):
        ex = ('On 10 September: ' + '; '.join(f"{lab} {b}→{a}" for lab, b, a in c['restore'][:3]) + '. Correction: restore those values, read the next day.') if c['restore'] else ('Correction: check the ad, the child and eligibility — no recorded price change explains it.' if not c['later'] else 'Correction: restore the values before the 16 and 20 September changes and read the next day.')
        example(c, ex)

cs = by('COLLAPSE')
if cs:
    section(f'{len(cs)} out-of-focus campaigns whose keyword lost more than 10 positions — investigate')
    lead('The rule.', 'Out of focus there is no push to run; freeze price and budget and name the cause.')
    _mv = [c for c in cs if moved(c)]
    for c in (_mv + [c for c in top(cs, 6) if c not in _mv])[:3]:
        example(c, 'Correction: freeze price and budget; check the listing, the child the ad serves, the rival now ahead and the term’s volume.' + (' The run moved it anyway — reverse that.' if moved(c) else ''))
    lead('Correction.', f'Freeze all {len(cs)}; name the cause on each before any price moves again. Where the cause is a stock-out on the hero (Full White and Twin White at 0 units, Queen White short), open the case as a re-ranking case once stock lands rather than leave it to the taper.')
    lead('The engine’s 12 rank freezes, read on the 7-day median.', 'The run freezes 12 campaigns on single-day reads. On the tracker’s 7-day median (30 days back → 24 September), with the threshold kept at more than 10 positions lost (operator 2026-09-25): 9 stand, 2 are lifted, 1 cannot be read.')
    _fz = [('cooling full size sheets', '46 → 120', 'Real loss — Full White at 0 units', 'Freeze'), ('cooling fitted sheet full', '81 → 128', 'Real loss, mostly unranked', 'Freeze'), ('full bed sheets cooling', '81 → 122', 'Real loss', 'Freeze'), ('full size sheets cooling', '65 → 95', 'Real loss', 'Freeze'), ('cooling sheets full size', '56 → 83', 'Real loss', 'Freeze'),
           ('bamboo twin sheets', '24 → 60', 'Step on 21 Sep, the week Twin White sold out', 'Freeze'), ('twin sheets bamboo', '32 → 60', 'Step on 21 Sep', 'Freeze'), ('cooling bed sheets', '20 → 37', 'Slip of 17, with unranked days', 'Freeze'), ('cool sheets queen', '45 → 58', 'Slip of 13', 'Freeze'),
           ('bed sheets cooling', '52 → 54', 'No loss (engine read 37 → 125 on single days)', 'Lift'), ('queen cooling sheets', '71 → 78', 'No loss beyond 10 (engine read 49 → 132)', 'Lift'), ('cooling bedsheets queen size', '—', 'Not tracked; the engine’s read is 86 → 144', 'Freeze on the engine’s read; add to the tracker')]
    table(['Term', '7-day median 25 Aug → 24 Sep', 'Read', 'Verdict'], [list(x) for x in _fz], widths=[4.4, 3.2, 5.8, 3.4], size=8)

part[0] = 'C'; sec_no[0] = 0
doc.add_heading('Part C — Across the run', 1)

# ---- 10. last changes
section('What the last two rounds of changes did')
imp = IMP
def agg(rows, ob):
    g = Counter()
    for r in rows:
        if r['ob'] != ob: continue
        g['n'] += 1
        for k in r['a']: g[k + 'a'] += r['a'][k]; g[k + 'b'] += r['b'][k]
    return g
lead('The rule.', f"Every write is a test: read what the last one did before sizing the next. The account’s graded hit rate over 90 days is {A['brief']['sections']['grades']['hit_rate']:.1%} ({A['brief']['sections']['grades']['by_grade']['HIT']} of {A['brief']['sections']['grades']['graded']}); the tuner holds {A['brief']['sections']['tuner']['open']} open records and the run cites none.")
rows = []
for date, lab in (('2026-09-15', '15/16 Sep (11–14 vs 15–22 Sep, the deal start)'), ('2026-09-22', '22 Sep (19–21 vs 23–24 Sep)')):
    for ob in ('Ranking', 'Conversions', 'Discovery', 'Defensive'):
        g = agg(imp[date], ob)
        if g['n']:
            rows.append([lab if ob == 'Ranking' else '', ob, g['n'], f"${g['spa']:.0f} → ${g['spb']:.0f}", f"{g['tosa']:.0f} → {g['tosb']:.0f}", f"{g['oda']:.1f} → {g['odb']:.1f}"])
table(['Change round', 'Objective', 'Campaigns', 'Spend/day', 'TOS clicks/day', 'Orders/day'], rows, widths=[5, 2.2, 1.6, 2.4, 2.4, 2.4], size=8)
para('The 15/16 September round is the deal round and cannot be separated from the deal: on 90 ranking campaigns spend doubled (328 → 697 a day), top-of-search clicks rose from 52 to 99 a day and ranking orders from 8.5 to 12.9 — volume bought at a cost per order well above contribution. The 22 September round touched 18 small campaigns (about one top-of-search click a day between them); two days after it, with attribution still filling in, it cannot be graded and is not read as a result either way. The last run’s read of the 10 September round (spend down a quarter, top-of-search clicks 80 → 59 a day, orders nearly halved) still stands.')
lead('Correction.', 'Grade every change against its own campaign before the next write on that campaign — a before/after read of 3 days either side, like for like. A write whose predecessor went the wrong way is not repeated; it is reversed or investigated.')

# ---- 11. non-ranking
section('Other campaign types — priced against their own ceiling, on recent numbers')
lead('The rule.', 'Conversions, discovery, defensive and liquidation campaigns are priced inside their ceiling: what a click can cost = contribution × that campaign’s conversion rate, equivalently an ad cost of sale at or under break-even (33.8%). Read it on 14 days (drift shows there without being noise) against 90 days. Over the ceiling, the bid comes down; inside it, nothing moves — a top-of-search modifier on a campaign whose top of search pays is not cut because “the premium buys rank”.')
groups_ = [('Thin (<15 clicks in 14 days)', 'Under 15 clicks in 14 days — hold', 'No readable conversion rate; hold at today’s values, no cut and no raise.', lambda n: n['eng'] != 'holds'),
           ('Inside its ceiling', 'Inside the ceiling — leave it', 'Paying for itself on 14 and 90 days; nothing moves, including the top-of-search modifier. Where ACoS is drifting up, watch it rather than cut.', lambda n: n['eng'] != 'holds'),
           ('Over its ceiling', 'Over the ceiling on 14 days — bring the base down', 'The base comes down until the campaign is back inside contribution × its conversion rate; a top-of-search trim alone does not reach the product-page and rest-of-search clicks that carry the cost.', lambda n: 'bid' not in n['eng']),
           ('Clearance economics', 'Clearance (LTSF) campaigns — the storage-fee floor rules', 'Priced against the storage fee it avoids, not against break-even; flag only if ACoS keeps rising.', lambda n: False)]
for key, title_, rule_, bad_ in groups_:
    ns = [n for n in NR if n['verdict'].startswith(key)]
    if not ns: continue
    doc.add_heading(f'{len(ns)} {title_[0].lower() + title_[1:]}', 3)
    lead('The rule.', rule_)
    wrong = [n for n in ns if bad_(n)]
    lead('What the run did.', f"Moved {sum(1 for n in ns if n['eng'] != 'holds')} and held {sum(1 for n in ns if n['eng'] == 'holds')}; {len(wrong)} go against the rule.")
    if not wrong:
        para('Nothing to correct here — the run follows the rule on all of them.')
    for n in sorted(wrong, key=lambda n: -(n['s14'] or 0))[:3]:
        p = doc.add_paragraph(); r = p.add_run(n['short']); r.bold = True
        runs(p, f" — {n['obj']}; last 14 days {n['c14']} clicks, {n['o14']} orders, {('ACoS ' + pct(n['acos14'], 0) + ' (90 days ' + (pct(n['acos90'], 0) if n['acos90'] is not None else 'no orders') + ')') if n['acos14'] is not None else 'no orders on 14 or 90 days' if n['acos90'] is None else 'no orders in 14 days (90-day ACoS ' + pct(n['acos90'], 0) + ')'}. The run {eng_compact(n['eng'])}. Correction: {n['verdict']}")
        p.paragraph_format.space_after = Pt(5); p.paragraph_format.left_indent = Cm(0.4)

# ---- 12. file / engine defects
section('Rows in the change file that should not load')
DE = json.load(open(f'{S}/defects.json'))
for b in DE:
    bullet(b)

# ---- 13. app changes
section('What the app should change so the next run gets these right')
for b in [
    '**Read the right window for each question.** Conversion over 90 days (it needs sample); placement mix over the last 14 days; “is it still serving” over the last 3–7 days; deal days as their own window. Today every price input is 90 days.',
    '**Read placement at campaign grain.** The engine’s placement figures are a keyword-level estimate — on 25 campaigns in this run they differ from Amazon’s placement report by more than 20%.',
    '**See the deal.** `engine_read` is still null during the Best Deal (15–28 September). A deal is the velocity condition for a push; the run should size pushes to the window, read daily, and grade deal days against deal days.',
    '**In focus: push every exact ranking campaign on top of search, every day,** sized by the delivery gap (+30% under 30% delivered, +20% at 30–70%, +10% over 70%), halved where the last raise bought no impression share; no hold for being thin or under review. Money bounds instead of the circular market bound: a loss stop per row (cost per top-of-search order ≤ 3× contribution), a spend envelope, a share stop (≥40% and flat), a reachability check (requirement vs delivered ÷ share) and a product TACoS guard. After the deal, rows short of requirement step down to break-even. Out of focus: thin rows hold; rows with a record are judged on their own numbers; converting rows get a bounded test.',
    '**Re-point every campaign off a hero that cannot ship, largest first** — the run moved 32 small Queen campaigns off Queen White and left the two largest on it; the engine check caught one and the run did nothing with it.',
    '**Never write to a paused campaign or one the export does not carry** — 18 writes land on paused campaigns and 13 raises on six campaigns missing from the export. Scope every row to the run’s product (seq 2427 writes to a 6-piece campaign).',
    '**Freeze on the 7-day median, not a single day** — 2 of the 12 freezes do not hold on the median and 1 term is not tracked, and the engine read “cooling bed sheets” at 86 where the median is 37.',
    '**Re-read live values before export.** 10 bids and modifiers were moved on 24 September after the audit read them; 3 rows in this file would write over them.',
    '**Carry the gate’s verdict into the export** (33 rows say “change → HOLD” in their own text and export as changes), drop no-op rows, and label each bid row by the keyword it changes.',
    f"**Grade the last change before writing the next one** and cite the open tuner record for the same lever — {48}% of this run’s price rows (68 of 141) sit on campaigns whose own record reads behind, stalled or wrong-direction; none cites it.",
    '**Price every placement on the framework’s blended rate** — the child’s planning rate under 15 clicks, a click-weighted blend from 15 to 49, the campaign’s own from 50 (zero included). The account has no child planning rate; the group rate stands in, which is why the Cal King rows here price on 8.4% rather than the product’s 15%.',
    f"**Write predictions the step can deliver** — the book’s rate for the step size, on the window it runs in — not the plan’s requirement. B4’s graded hit rate over 90 days is {A['brief']['sections']['grades']['hit_rate']:.1%}.",
    '**Read top-of-search impression share beside the effective bid on every ranking target** and grade each push on whether share rose; compare delivered top-of-search clicks with the requirement every run (Part D).',
    '**Tell a traffic gap from a performance gap before choosing the lever:** under the CTR/CVR bars on a real sample → fix the offer, hold the price; above the bars with low share or short clicks → buy the traffic.',
    '**Give non-SP builds a way to happen** (a task with an owner and a date), sized to a readable click count; and put every in-focus term on the rank tracker (3 have no rank read).',
]:
    bullet(b)

# ---- Part D: B4 diagnosis for Erik
import sys as _sys; _sys.path.insert(0, S)
exec(open(f'{S}/part_d.py').read())

# ---- checklist
doc.add_heading('In order, starting 09-25', 1)
for i, b in enumerate([
    'Pull the rows in section C.3 before loading: withheld, overtaken by the 24 September moves, no-op and duplicate rows, the 18 writes on paused campaigns, and the 13 raises on the six Cooling campaigns missing from the export (held until confirmed); drop the budget raises on campaigns not using their budget; send seq 2423 and 2427 to the LTSF owner.',
    'Same day: re-point “Bamboo Cooling Sheets” from Queen White to Queen Olive and do the Cal King White → Cal King Olive swaps by hand; decide the in-focus campaign whose only keyword is paused; confirm the rank tracker reads the child each ad serves.',
    f"Write the push from live values: {sum(1 for c in PUSHED if c['push']['step'] > 0)} in-focus campaigns stepped on top of search by delivery gap, inside the loss stop, the envelope (${_dsp * 1.5:,.0f} a day to 09-28) and the 21.7% TACoS guard; base carries the raise past the 900% wall; budget +30% where 80%+ is used.",
    'Every morning to 09-28: top-of-search clicks, impression share, placement, budget use and hours out of budget per in-focus campaign; step again where clicks are short and share rose; halve the step where share was flat; stop at the loss stop, the share stop, the envelope or the TACoS guard; check eligibility where a campaign is still at zero after two steps.',
    'Same day as the push: start the cause check on “bamboo sheets cal king” (23 → 37).',
    f"Out of focus: hold the {len(by(['THIN_OUT','THIN_ZERO_OUT']))} thin rows and the flagship flat; freeze the {len(by('COLLAPSE'))} collapses (9 of the engine’s 12 freezes stand on the 7-day median, 2 are lifted); open the Queen, Full and Twin losses as re-ranking cases once stock lands.",
    f"Out of focus, converting: test the {len(by('OUT_TEST'))} campaigns in section B.1 at +10% top of search for two weeks with no budget cut; read on 10-08. Focus itself does not change.",
    'Other campaign types: bring the ones over their ceiling down on the base; leave the rest.',
    'Grade the price step and the budget raise separately: price on impression share, budget on hours out of budget.',
    'This week: build the Sponsored Brands headline and video on the two focus terms, Sponsored Display defence, and the conquest campaign on a child with stock (not Queen White), at readable budgets.',
    'From 09-29: campaigns at their requirement — probe cost per click down 3–5% a step while click share holds; campaigns short of it — step down to break-even over two writes four days apart (or hold one week where the 7-day rank reached the target range). Grade every write in this list.',
], 1):
    para(f'{i}. {b}')

# ---------------- register of every ranking campaign's situation and write ----------------
def action(c):
    k = c['cat']; p = c['em'].get('price_now')
    if c.get('push'):
        q = c['push']
        a = f"Push TOS +{q['step']:.0%} ({q['step_why']}): {usd(q['price0'])} → {usd(q['price1'])}"
        if q['base0'] and q['base1'] and abs(q['base1'] - q['base0']) > 0.004:
            a += f"; {q['base_why']}: base {usd(q['base0'])} → {usd(q['base1'])}"
        if q['mod1'] is not None:
            a += f"; modifier {q['mod1']:.0f}%"
        if q['budget1'] != q['budget0']:
            a += f"; budget ${q['budget0']:.2f} → ${q['budget1']:.2f}"
        if k == 'IN_DARK': a = 'Restore pre-cut prices, then ' + a[0].lower() + a[1:]
        if k == 'IN_COLLAPSE': a += '; investigate the rank loss the same day'
        if q['ud']: a = 'Switch to fixed bidding; ' + a
        if q['hero_bad']: a += '; re-point the ad to the serving child'
        return a + '; daily read to 09-28'
    if k == 'IN_PAUSED':
        return 'Only keyword paused and no other campaign carries the term — re-enable and push, or take out of focus'
    if k == 'IN_ONTARGET':
        return 'Delivering its clicks — hold; evaluate cost per click from 09-29'
    if k == 'LEAK':
        step, nb, nm = c.get('fix', (None, None, None))
        return f"Base −{step:.0%} → {usd(nb)}; TOS price held via modifier" if nb else 'Base cut sized to the leak; TOS held' 
    if k in ('THIN_PUSH', 'THIN_ZERO_IN', 'SHORT_PRICE'):
        return 'Push TOS modifier: ' + push_price(c)[1] + '; base held; daily read to 09-28'
    if k == 'THIN_TINY':
        return 'Hold at today’s price (low volume); a written raise may stand if under the group limit; no cut'
    if k in ('THIN_OUT', 'THIN_ZERO_OUT', 'OUT_WORKING'):
        return 'Hold flat — no cut, no raise'
    if k == 'OUT_WEAK':
        return 'Taper stands'
    if k == 'LEAK':
        step, nb, nm = c.get('fix', (None, None, None))
        return f"Base −{step:.0%} → {usd(nb)}; TOS price held via modifier; no other climb" if nb else 'Base cut sized to the leak; TOS held'
    if k == 'SHORT_BUDGET':
        return f"Budget ${c['budget']:.2f} → ${c['budget']*1.3:.2f}; price holds" + (' (already over group limit)' if p and p > c['limit'][1] else '')
    if k == 'SHORT_ATLIMIT':
        return 'Hold price (at/over group limit); check ad, child, eligibility'
    if k in ('DARK', 'FADED'):
        return 'Restore pre-cut prices and read next day; if already restored or never changed, check eligibility'
    if k == 'COLLAPSE':
        return 'Freeze price and budget; investigate the rank loss'
    if k == 'ON_TARGET':
        return 'Hold; keep budget raise if capping; probe −3–5% from 09-29'
    if k == 'OUT_TEST':
        t = c['test']
        return (f"Out of focus but converts ({t['rate']:.0%} at top of search vs bar {t['bar']:.1f}%): test TOS +10% {usd(t['price0'])} → {usd(t['price1'])} to 10-08; budget {usd(t['budget1'])}/day" if t['price0'] else f"Out of focus but converts ({t['rate']:.0%} vs bar {t['bar']:.1f}%): no priced target on file — re-enable and set TOS at {usd(c['limit'][1])} as the test, to 10-08") + (f"; advertise {t['repoint']}" if t['repoint'] else '') + ('; restore the pre-cut base first' if t['prior'] in ('DARK', 'FADED') else '')
    if k == 'OUT_FLAGSHIP':
        return 'Flagship, out of focus — hold flat (no test, no cut); read weekly with the TACoS guard'
    if k == 'ROS_HEAVY':
        return 'ROS modifier to 0%; else treat as leak'
    return ''



doc.save(OUT)
print('saved', OUT)


import openpyxl
from openpyxl.styles import Font, PatternFill
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Ranking campaigns'
hdr = ['Situation', 'Campaign', 'Focus', 'Tier', 'Group limit', 'Clicks 90d', 'Clicks 14d', 'PP share (read window)', 'TOS clicks/day 08-15→09-14', 'TOS clicks/day in the deal', 'Clicks last 3d',
       'Rank 30d → now → target', 'Budget', 'Budget use 7d', 'TOS price now', 'The run', 'Correction']
ws.append(hdr)
for c in sorted(CATS, key=lambda c: (names[c['cat']], c['short'])):
    ws.append([names[c['cat']], c['short'], c['focus'], c['tier'], c['limit'][1], c['R']['d90']['t3'], c['R']['d14']['t3'],
               round(c['R'][c['mixw']]['pp_sh'], 3) if c['R'][c['mixw']]['pp_sh'] is not None else None, round(c['pre_tos_day'], 1), round(c['deal_tos_day'], 1), c['R']['d3']['t3'],
               f"{c['rank_30'] or '—'} → {c['rank_now'] or '—'} → {c['rank_tgt'] or '—'}", c['budget'], round(c['util7'], 2) if c['util7'] is not None else None,
               round(c['em']['price_now'], 2) if c['em'].get('price_now') else None, eng_short(c), action(c)])
ws2 = wb.create_sheet('Other campaign types')
ws2.append(['Campaign', 'Objective', 'Clicks 14d', 'Orders 14d', 'ACoS 14d', 'ACoS 90d', 'The run', 'Correction'])
for n in NR:
    ws2.append([n['short'], n['obj'], n['c14'], n['o14'], round(n['acos14'], 3) if n['acos14'] is not None else None, round(n['acos90'], 3) if n['acos90'] is not None else None, n['eng'], n['verdict']])
for w in (ws, ws2):
    for cell in w[1]:
        cell.font = Font(bold=True, color='FFFFFF'); cell.fill = PatternFill('solid', fgColor='1F3A5F')
    w.freeze_panes = 'C2'; w.auto_filter.ref = w.dimensions
for col, wd in zip('ABCDEFGHIJKLMNOPQ', [30, 60, 16, 7, 9, 9, 9, 10, 10, 10, 9, 16, 9, 9, 10, 40, 70]):
    ws.column_dimensions[col].width = wd
for col, wd in zip('ABCDEFGH', [60, 12, 9, 9, 9, 9, 40, 70]):
    ws2.column_dimensions[col].width = wd
for prod, lab, KW in (('b4', 'B4', KW4),):
    w = wb.create_sheet(f'{lab} keyword diagnosis')
    w.append(['Keyword', 'Syntax', 'Plan clicks/wk', 'Weekly SV', 'Clicks 30d', 'TOS clicks 30d', 'TOS clicks/day 08-15→09-14', 'TOS clicks/day in the deal', 'TOS share', 'TOS CTR', 'CTR bar', 'TOS CVR', 'CVR bar', 'TOS impr. share', 'Eff. TOS bid', 'Organic', 'Sponsored', 'Rank 24 Jun', 'Rank 14 Sep', 'Rank 24 Sep', 'Verdict', 'Recommendation'])
    for r in KW:
        pl = PLAN.get(r['kw'])
        rv = list(r['ranks'].values())
        R2 = lambda x, n=2: None if x is None else round(x, n)
        w.append([r['kw'], r['syntax'], pl['ppc_clicks_target'] if pl else None, r['wsv'], r['clicks'], R2(r['tos_clicks'], 0), R2(r['pre_tos_day'], 1), R2(r['deal_tos_day'], 1), R2(r['tos_share'], 0), R2(r['tos_ctr']), R2(r['tctr']), R2(r['tos_cvr']), R2(r['tcvr']), R2(r['is_']), R2(r['eff']), r['org'], r['sp'], rv[0], rv[2], rv[3], r['verdict'], _dg.reco(r)])
    for cell in w[1]:
        cell.font = Font(bold=True, color='FFFFFF'); cell.fill = PatternFill('solid', fgColor='1F3A5F')
    w.freeze_panes = 'B2'; w.column_dimensions['A'].width = 34; w.column_dimensions['U'].width = 40; w.column_dimensions['V'].width = 80
w = wb.create_sheet('Syntax groups')
w.append(['Product', 'Group', 'Spend 30d', 'Clicks', 'TOS clicks', 'TOS share', 'TOS CTR', 'CTR bar', 'TOS CVR', 'CVR bar', 'TOS impr. share', 'TOS CPC', 'Rank 24 Jun', 'Rank 15 Aug', 'Rank 14 Sep', 'Rank 24 Sep', 'Verdict'])
for lab, G, GIS in (('B4', GR4, GIS4),):
    for g in G:
        v = _dg.verdict(g['tos_impr'], g['tos_clicks'], g['tos_ctr'], g['tos_cvr'], g['mctr'], g['mcvr'], is_=GIS.get(g['group']))
        R2 = lambda x, n=2: None if x is None else round(x, n)
        w.append([lab, g['group'], g['spend'], g['clicks'], R2(g['tos_clicks'], 0), R2(g['tos_share'], 0), R2(g['tos_ctr']), R2(v['tctr']), R2(g['tos_cvr']), R2(v['tcvr']), R2(GIS.get(g['group'])), R2(g['tos_cpc']), *g['ranks'].values(), v['verdict']])
for cell in w[1]:
    cell.font = Font(bold=True, color='FFFFFF'); cell.fill = PatternFill('solid', fgColor='1F3A5F')
w.column_dimensions['B'].width = 24; w.column_dimensions['Q'].width = 50
XL = OUT.replace('.docx', '.xlsx')
wb.save(XL); print('saved', XL)
