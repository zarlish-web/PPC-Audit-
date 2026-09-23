"""Situation-based corrections document for DBS4 run 20260921-dbcd48b8."""
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
IMP = json.load(open(f'{S}/data/impact.json'))
A = json.load(open(f'{S}/a.json'))
OUT = os.environ.get('OUT', os.path.join(S, '..', '..', 'docs', 'DBS4_Corrections_by_Situation_20260921-dbcd48b8.docx'))

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
    b.append(f"In the deal (09-15 → 09-22): {R['deal8']['tos']['c']} top-of-search clicks ({c['deal_tos_day']:.1f}/day, against {c['pre_tos_day']:.1f}/day before it); last 3 days {R['d3']['t3']} clicks.")
    if c['need_day']:
        b.append(f"Plan needs {c['need_day']*7:.0f} paid clicks a week ({c['need_day']:.1f}/day).")
    if c['tos_is'] is not None:
        b.append(f"Top-of-search impression share {c['tos_is']}%.")
    if c['budget']:
        b.append(f"Budget ${c['budget']:.2f}/day, last 7 days {pct(c['util7'])} used.")
    if c['tos_rate'] and c['mkt_cvr']:
        b.append(f"Top of search converts {pct(c['tos_rate'],1)} against a market {c['mkt_cvr']}%.")
    b.append(f"The run {eng(c)}.")
    return ' '.join(b)


def example(c, extra=''):
    p = doc.add_paragraph(); r = p.add_run(c['short']); r.bold = True
    runs(p, ' — ' + story(c) + ((' ' + extra) if extra else ''))
    p.paragraph_format.space_after = Pt(5); p.paragraph_format.left_indent = Cm(0.4)


def top(cs, n=3, key=None):
    key = key or (lambda c: -(c['R']['d14']['spend'] + c['R']['deal8']['spend'] + (6 - (['VHSV', 'HSV', 'MSV', 'LSV', 'VLSV', 'NOSV'].index(c['tier']) if c['tier'] in ['VHSV', 'HSV', 'MSV', 'LSV', 'VLSV', 'NOSV'] else 6)) * 10))
    return sorted(cs, key=key)[:n]


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
t = doc.add_paragraph(); runs(t, 'Corrections to the 21 September run — Decolure Bamboo Sheets 4-Piece', bold=True, size=18, color=NAVY)
para('The goal this cycle is to climb the ranking keywords inside the Best Deal (15–28 September), so top-of-search clicks on the exact-match ranking campaigns are what matter now. Everything below is judged against that goal, the bids-and-placements standard, and each campaign’s own numbers — read over 90 days for conversion, over the last 14 days for where clicks land, over the last 3–7 days for whether the campaign is still serving, and over the deal days for what the deal is doing. Campaigns are grouped by the situation they are in; each section gives the rule, what the run did, two or three named campaigns as evidence, and the correction. The full list of which campaign sits where is at the end.', italic=False)

N = len(CATS)
thin = by(['THIN_PUSH', 'THIN_ZERO_IN', 'THIN_TINY', 'THIN_OUT', 'THIN_ZERO_OUT'])
doc.add_heading('What is already right and stays', 2)
tp_in = by(['THIN_PUSH', 'THIN_ZERO_IN'])
bullet(f"**Thin in-focus rows are mostly being pushed, not cut.** Of the {len(tp_in)} in-focus ranking campaigns with real search volume and under 15 top-of-search clicks, the run raises the top-of-search price on {sum(1 for c in tp_in if pdir(c)=='up')} and cuts it on {sum(1 for c in tp_in if pdir(c)=='down')}.")
tout = by(['THIN_OUT', 'THIN_ZERO_OUT'])
bullet(f"**Out-of-focus thin rows are mostly left alone.** {sum(1 for c in tout if not moved(c))} of {len(tout)} are held; the run’s own taper check says a rung down on a row that spends nothing “frees nothing for the focus”.")
bullet('**Where the run does fix placement, it holds the top-of-search price** — the base comes down and the modifier is re-solved so top of search pays the same.')
bullet('**The engine already has a per-keyword-group market price** (e.g. Bamboo|King clears at $5.62, limit $6.47; Bamboo at $5.50, limit $6.32). This document uses it as the ceiling on every push.')

doc.add_heading('Windows and sources', 2)
para('Amazon’s campaign placement report (Command Center) for: 90 days (06-23 → 09-20, the audit’s window, deal days included); the last 14 days (09-09 → 09-22); the last 7 (09-16 → 09-22); the last 3 (09-20 → 09-22); the deal to date (09-15 → 09-22); the 31 days before the deal (08-15 → 09-14); and 07–09 vs 11–14 September around the 10 September action. Orders on the last seven days are still filling in (7-day attribution) and read low. Placement is read per campaign — the grain Amazon reports — not the engine’s keyword estimate (section 12).')

sec_no = [0]


def section(title):
    sec_no[0] += 1
    doc.add_heading(f'{sec_no[0]}. {title}', 1)


# ---- 1. thin, in focus, with volume -> push
cs = by(['THIN_PUSH', 'THIN_ZERO_IN'])
section(f'{len(cs)} in-focus ranking campaigns taking under 15 clicks, on keywords with real search volume — push them')
lead('The rule.', 'A ranking campaign with almost no clicks is not underperforming — it is barely in the auction. The only lever that can produce clicks on a row that isn’t getting any is the top-of-search price; the base prices product pages and rest of search, which these rows are not using, and there is no mix to redistribute. So: raise the top-of-search modifier, hold the base, never cut. Size the first write to the room left under the keyword group’s market limit, up to 25%; read daily through the deal; step again while top-of-search clicks arrive; stop when the required clicks land or the price reaches the limit. “Under 15 clicks” is read on the last 14 days and the deal, not 90 days — a campaign near zero recent clicks is thin whatever its long-window total says. “Real volume” means LSV and above (100+ searches a month); VLSV/NOSV rows are section 2.')
up = [c for c in cs if pdir(c) == 'up']; down = [c for c in cs if pdir(c) == 'down']; held = [c for c in cs if not moved(c)]
steps = [c['em']['price_eng']/c['em']['price_now']-1 for c in up if c['em'].get('price_now')]
over = [c for c in up if c['em'].get('price_eng') and c['em']['price_eng'] > c['limit'][1]]
lead('What the run did.', f"Raised the top-of-search price on {len(up)} (steps from {min(steps):+.0%} to {max(steps):+.0%}), cut it on {len(down)}, held {len(held)}. {sum(1 for c in cs if c['cat']=='THIN_ZERO_IN')} took no clicks at all in 90 days or in the deal. The direction is right. What is missing: {len(held)} rows are held that should be pushed; {len(over)} raises land above the keyword group’s market limit; and a single write read at a checkpoint on 09-25 is a weekly cadence inside a two-week deal that wants a daily one.")
for c in top(cs):
    example(c, 'Correction: ' + push_price(c)[1] + '.')
lead('Correction.', 'Where the campaign is already spending its whole budget, the budget goes first (+30%) and the price waits until it stops capping. Otherwise push every one on the top-of-search modifier, first write up to +25% and never past the group limit, base held. Where the run cut or held, reverse that. Rows already at the limit hold price and go to an eligibility check (ad live, right child, listing buyable) — a row at the winners’ price that still wins nothing is not a price problem. The push doubles as the eligibility test: if clicks arrive it was price; if a raised row stays at zero, check the listing.')
rows = []
for c in sorted(cs, key=lambda c: c['short']):
    new, txt = push_price(c)
    rows.append([c['short'][:60], c['tier'], c['R']['d90']['tos']['c'], c['R']['deal8']['tos']['c'], eng_short(c), txt[:90]])
table(['Campaign', 'Tier', 'TOS clicks 90d', 'TOS clicks deal', 'The run', 'First write (TOS price)'], rows, widths=[5.2, 1.1, 1.3, 1.3, 3.8, 4.6], size=7.5)
lead('What to read.', 'Each day to 09-28: top-of-search clicks, and where the clicks landed. Clicks arriving at top of search — step again, re-sized to the remaining room. Clicks not arriving — stop stepping; the problem is not price. Clicks arriving on product pages — that is a base problem; cut the base, don’t touch the modifier. After the deal (10-06) probe any price above the group’s clearing price back down in 3–5% steps.')

# ---- 2. thin, in focus, tiny volume
cs = by('THIN_TINY')
section(f'{len(cs)} in-focus rows on keywords with almost no search volume — hold, don’t spend the push here')
lead('The rule.', 'Under 100 searches a month (VLSV) or none recorded (NOSV), there is little to win even at 100% of the auctions. These rows keep their coverage at today’s price: no cut (they are thin, the read is empty), no push (the deal budget buys more on the terms with volume).')
lead('What the run did.', f"Raised {sum(1 for c in cs if pdir(c)=='up')}, cut {sum(1 for c in cs if pdir(c)=='down')}, held {sum(1 for c in cs if not moved(c))}.")
for c in top(cs, 2):
    example(c)
lead('Correction.', 'Hold at today’s price. A raise already written can stand only if it stays under the group limit — it is cheap — but no further steps. Anything cut goes back.')

# ---- 3. out of focus thin
cs = by(['THIN_OUT', 'THIN_ZERO_OUT'])
section(f'{len(cs)} out-of-focus rows under 15 clicks — hold them flat')
lead('The rule.', 'A campaign under 15 clicks has no readable conversion rate; out of focus means no new money, not a cut. A cut on a row spending nothing saves nothing and releases nothing to the focus — it only leaves the row a rung lower for whenever its group comes back into focus.')
lead('What the run did.', f"Held {sum(1 for c in cs if not moved(c))}; moved {sum(1 for c in cs if moved(c))} — raised the price on {sum(1 for c in cs if pdir(c)=='up')}, cut it on {sum(1 for c in cs if pdir(c)=='down')}. {sum(1 for c in cs if c['cat']=='THIN_ZERO_OUT')} of these took no click in 90 days or in the deal.")
movers = [c for c in cs if moved(c)]
for c in top(movers or cs, 3):
    example(c)
lead('Correction.', 'Hold every one at today’s price — reverse the cuts and the raises. Where an out-of-focus term is climbing organically on no paid clicks, record it: that is evidence for the next focus decision, not a reason to push around this one.')

# ---- 4. leak
cs = by('LEAK')
section(f'{len(cs)} campaigns with too many product-page clicks — fix where the clicks land before anything else')
lead('The rule.', 'On a ranking campaign 70–90% of clicks should be at top of search and product pages at or under 20%. Above 20%, the money is landing on the placement that does not move rank. The fix is a base cut sized to the leak with the modifier raised so top of search pays the same; no price climb and no budget raise until product pages are back under 20%. The mix is read on the last 14 days (the long window can show a leak that has already corrected), and the base is never cut on a row that stopped serving (section 7).')
lead('What the run did.', f"Cut the base on {sum(1 for c in cs if c['em']['base'] and c['em']['base'][0]=='down')} of {len(cs)}; raised the top-of-search price on {sum(1 for c in cs if pdir(c)=='up')} while product pages were still over the line; held {sum(1 for c in cs if not moved(c))}.")
for c in top(cs):
    example(c)
rows = []
for c in sorted(cs, key=lambda c: -(c['R'][c['mixw']]['pp_sh'] or 0)):
    r = c['R'][c['mixw']]; pp = r['pp_sh']; orders_pp = r['detail']['o'] + r['other']['o']
    step = 0.10 if pp < 0.30 else 0.20 if pp < 0.50 else 0.35
    cap = 0.25 if orders_pp else 0.50
    step = min(step, cap)
    nb = c['base'] * (1 - step) if c['base'] else None
    nm = (c['em']['price_now'] / nb - 1) * 100 if (nb and c['em'].get('price_now')) else None
    c['fix'] = (step, nb, nm)
    tos_new = min(c['em']['price_now'] * 1.25, c['limit'][1]) if (c['focus_in'] and c['em'].get('price_now') and c['em']['price_now'] < c['limit'][1]) else c['em'].get('price_now')
    nm = (tos_new / nb - 1) * 100 if (nb and tos_new) else None
    rows.append([c['short'][:58], f"{pct(pp)} ({c['mixw'].replace('d14','14 days').replace('deal8','deal').replace('d90','90 days')})", r['t3'], usd(c['base']), f"−{step:.0%} → {usd(nb)}", f"{nm:.0f}%" if nm is not None else '—', (usd(c['em'].get('price_now')) + (' → ' + usd(tos_new) if tos_new and c['em'].get('price_now') and tos_new > c['em']['price_now'] + 0.005 else ' (held)'))])
table(['Campaign', 'Product pages', 'Clicks', 'Base now', 'Base write', 'Modifier written', 'TOS price'], rows, widths=[5.4, 2.4, 1.2, 1.5, 2.2, 1.8, 1.8], size=7.5)
lead('In-focus rows also short of top-of-search clicks.', 'The base step and a top-of-search step may share one write (doc §9, combined write): the base cut is graded on product-page share, the price step on top-of-search clicks, so neither hides the other. On in-focus rows below, the top-of-search price also rises up to +25% within the group limit; out-of-focus rows get the base step only.')
lead('Correction.', 'Cut the base by the step shown (10% at 20–30% product pages, 20% at 30–50%, 35% above 50%; never more than 25% where product pages carry orders), re-solve the modifier so the top-of-search price holds to the cent, and remove any other price climb written on these rows until the mix is right. Read product-page share on 10-06 (and daily during the deal for in-focus rows). If it does not move, the leak is not price-driven — restore the base.')

# ---- 5. mix right but short
cs = by(['SHORT_PRICE', 'SHORT_BUDGET', 'SHORT_ATLIMIT'])
section(f'{len(cs)} in-focus campaigns with the right mix that are short of their clicks — find which of three things is in the way')
lead('The rule.', 'When 70%+ of clicks already land at top of search and delivery is still short of the requirement, the shortfall has one of three causes: the budget runs out (raise the budget — the price is not the problem); the price is not clearing enough auctions (raise the modifier in capped steps up to the group limit); or the price is already at the winners’ level and share still does not move (not a price problem — check the ad, the child, eligibility).')
for sub, label in (('SHORT_BUDGET', 'Budget running out (7-day use ≥ 80%) — raise the budget; price holds.'), ('SHORT_PRICE', 'Budget not the limit, price under the group limit — raise the modifier up to +25%, daily in the deal.'), ('SHORT_ATLIMIT', 'Price already at or over the group limit — hold price; check what else is binding.')):
    ss = by(sub)
    if not ss:
        continue
    doc.add_heading(label, 3)
    for c in top(ss, 3):
        extra = ''
        if sub == 'SHORT_PRICE':
            extra = 'Correction: ' + push_price(c)[1] + '.'
        elif sub == 'SHORT_BUDGET':
            over = c['em'].get('price_now') and c['em']['price_now'] > c['limit'][1]
            if c.get('bid_strategy') == 'AUTO_FOR_SALES':
                extra_ud = f" It also runs up-and-down bidding: in the deal it paid {usd(c['R']['deal8']['tos']['s']/c['R']['deal8']['tos']['c']) if c['R']['deal8']['tos']['c'] else '—'} per top-of-search click against a written {usd(c['em'].get('price_now'))} — switch it to down-only or fixed so the written price is the price."
            else:
                extra_ud = ''
            extra = f"Correction: budget ${c['budget']:.2f} → ${c['budget']*1.3:.2f} (+30%) for the rest of the deal; price holds" + (f" — it is already {usd(c['em']['price_now'])}, over the {c['group']} limit {usd(c['limit'][1])}, so no price step either; after 09-28 probe it down toward the limit in 3–5% steps and write a weekly loss ceiling on it." if over else ".") + extra_ud
        else:
            extra = f"Correction: hold at {usd(c['em'].get('price_now'))}; check the ad, the advertised child ({c['serving']}) and eligibility before any further price."
        example(c, extra)

# ---- 6. out of focus with volume
cs = by(['OUT_WORKING', 'OUT_WEAK'])
section(f'{len(cs)} out-of-focus campaigns with a readable record — judge each on its own numbers')
lead('The rule.', 'Out of focus means no new money; it does not mean take away what is working. A campaign that converts at or above the market at top of search, has the right mix, or is climbing, is held flat — no increase, no cut. One that is not working on its own numbers takes the taper.')
for c in top(cs, 4):
    verdict = 'Hold flat — no cut, no raise.' if c['cat'] == 'OUT_WORKING' else 'Taper stands — it is not earning its price on its own numbers.'
    example(c, 'Correction: ' + verdict)

# ---- 7. dark
cs = by(['DARK', 'FADED'])
section(f'{len(cs)} campaigns that stopped serving or faded to a trickle — restore before anything else')
lead('The rule.', 'Cutting the base of a row that is not delivering makes delivery worse. A campaign with a real 90-day record that now takes no clicks (last 7 days) or under a quarter of its usual daily clicks (last 14 days) is not a placement problem or a price problem to be tuned — it went dark or faded, usually after a cut. A long-window mix read on it describes a campaign that no longer exists. Put its price back to the last level that served and read the next day.')
for c in top(cs, 4):
    if c['restore']:
        r = '; '.join(f"{lab} {b}→{a}" for lab, b, a in c['restore'][:4])
        lt = '; '.join(f"{d} {f}{'/'+p.replace('placement','') if p else ''} {b}→{a}" for d, f, p, b, a in c['later'][:3])
        befores = {b for lab, b, a in c['restore']}
        undone = [x for x in c['later'] if x[4] in befores]
        if undone and len(undone) >= min(2, len(c['restore'])):
            ex = f"On 10 September the run wrote: {r}. On 15 September those were put back ({lt}) — and it still is not serving. Correction: price is not the cause; check the ad, the advertised child and eligibility before any write."
        else:
            ex = f"On 10 September the run wrote: {r}." + (f" Since then: {lt}." if lt else '') + " Correction: put back the values from before 10 September (the prices it last served at), nothing else, read the next day."
    elif c['later']:
        lt = '; '.join(f"{d} {f}{'/'+p.replace('placement','') if p else ''} {b}→{a}" for d, f, p, b, a in c['later'][:3])
        ex = f"No 10 September change; later changes: {lt}. Correction: restore the values before those changes and read the next day."
    else:
        ex = "Nothing was changed on it — it faded on its own, so price is not the cause. Correction: check the ad, the advertised child and eligibility before any write."
    example(c, ex)
lead('Correction.', 'Restore each to its price before the last cut (the change record above), write nothing else on it, read the next day. If it serves, the cut was the cause. If it stays dark at the old price, check the listing, the child and eligibility.')

# ---- 8. collapse
cs = by('COLLAPSE')
section(f'{len(cs)} campaigns whose keyword lost more than 10 positions in thirty days — investigate, never scale')
lead('The rule.', 'A rank collapse has a cause price cannot fix — the listing lost something, the ad serves the wrong child, a competitor took the spots with a deal, or the term itself shifted. Freeze price and budget on the row until the cause is named; negatives still run.')
rows = [[c['short'][:60], c['kw'] or '—', f"{c['rank_30']} → {c['rank_now']}", eng_short(c)] for c in sorted(cs, key=lambda c: -(c['lost'] or 0))]
table(['Campaign', 'Keyword', 'Rank 30d → now', 'The run'], rows, widths=[6, 4, 2, 5], size=8)
lead('Correction.', 'Hold every price and budget row listed. Each cause is checkable in a day: listing and badge, which child the ad serves and its stock, the rival now ahead of us and whether it is on a deal, and search volume for the term.')

# ---- 9. ROS heavy / on target
cs = by(['ROS_HEAVY', 'ON_TARGET'])
if cs:
    section(f'{len(cs)} campaign{"s" if len(cs) != 1 else ""} delivering or placed on rest of search')
    for c in cs:
        v = 'Rest of search carries the clicks product pages don’t — set the rest-of-search modifier to 0% (it earns a lift only at 15+ clicks converting at or above the product-page rate); if it is already 0%, the base prices it, so treat as a leak.' if c['cat'] == 'ROS_HEAVY' else ('Delivering its requirement but running out of budget in the deal (' + pct(c['util7']) + ' used) — keep the budget raise, price holds; after the deal probe the price down 3–5% and watch click share.' if (c['util7'] or 0) >= 0.8 else 'Delivering its requirement — hold; after the deal probe the price down 3–5% and watch click share.')
        example(c, 'Correction: ' + v)

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
lead('The rule.', 'Every write is a test: read what the last one did before sizing the next. The run does this on 31 ranking rows and nowhere else; Command Center holds 776 decisions on this product since 15 August and none has been scored.')
rows = []
for date, lab in (('2026-09-10', '10 Sep (07–09 vs 11–14 Sep, before the deal)'), ('2026-09-15', '15/16 Sep (11–14 vs 15–22 Sep, overlaps the deal start)')):
    for ob in ('Ranking', 'Conversions', 'Discovery', 'Defensive'):
        g = agg(imp[date], ob)
        if g['n']:
            rows.append([lab if ob == 'Ranking' else '', ob, g['n'], f"${g['spa']:.0f} → ${g['spb']:.0f}", f"{g['tosa']:.0f} → {g['tosb']:.0f}", f"{g['oda']:.1f} → {g['odb']:.1f}"])
table(['Change round', 'Objective', 'Campaigns', 'Spend/day', 'TOS clicks/day', 'Orders/day'], rows, widths=[5, 2.2, 1.6, 2.4, 2.4, 2.4], size=8)
para('The 10 September round is the clean read: on 194 ranking campaigns it took spend down a quarter and top-of-search clicks from 80 to 59 a day, and orders nearly halved — the thing the deal needed. The 15 September round cannot be separated from the deal; totals rose, but some campaigns fell inside it (named in sections 4 and 7).')
lead('Correction.', 'Grade every change against its own campaign before the next write on that campaign — a before/after read of 3 days either side, like for like (deal days against deal days). A write whose predecessor went the wrong way is not repeated; it is reversed or investigated.')

# ---- 11. non-ranking
section('Other campaign types — priced against their own ceiling, on recent numbers')
lead('The rule.', 'Conversions, discovery, defensive and liquidation campaigns are priced inside their ceiling: what a click can cost = contribution × that campaign’s conversion rate, equivalently an ad cost of sale at or under break-even (33.9%). Read it on 14 days (drift shows there without being noise) against 90 days. Over the ceiling, the bid comes down; inside it, nothing moves — a top-of-search modifier on a campaign whose top of search pays is not cut because “the premium buys rank”.')
rows = []
for n in NR[:18]:
    rows.append([n['short'][:55], n['obj'][:11], f"{n['c14']} / {n['o14']}", pct(n['acos14'], 0) if n['acos14'] is not None else '—', pct(n['acos90'], 0) if n['acos90'] is not None else '—', n['eng'][:40], n['verdict']])
table(['Campaign', 'Objective', 'Clicks / orders 14d', 'ACoS 14d', 'ACoS 90d', 'The run', 'Correction'], rows, widths=[4.8, 1.8, 1.8, 1.3, 1.3, 3.2, 3.8], size=7.5)

# ---- 12. file / engine defects
section('Rows in the change file that should not load')
DE = json.load(open(f'{S}/defects.json'))
for b in DE:
    bullet(b)

# ---- 13. app changes
section('What the app should change so the next run gets these right')
for b in [
    '**Read the right window for each question.** Conversion over 90 days (it needs sample); placement mix over the last 14 days; “is it still serving” over the last 3–7 days; deal days as their own window. Today every price input is 90 days.',
    '**Read placement at campaign grain.** The engine’s placement figures are a keyword-level estimate — on 55 changed campaigns they differ from Amazon’s placement report by more than 20% (median a quarter of the real clicks).',
    '**See the deal.** `engine_read` is null and the Summary says “No deal in the window” during the Best Deal. A deal is the velocity condition for a push; the run should size pushes to the window, read daily, and grade deal days against deal days.',
    '**Thin in-focus rows with volume: push the modifier, never cut; size the step to the room under the group’s market limit.** Out-of-focus thin rows: hold. Out-of-focus rows with a record: judge on their own numbers.',
    '**Make the 70/20 check stop a reduction** instead of printing “fails” beside it; and never cut the base on a row with no recent clicks.',
    '**Budget raises only at 80%+ utilisation on recent days**, for the ordinary pass and the deal pass alike.',
    '**Grade the last change before writing the next one**, on every campaign and every objective, and cite the open tuner record for the same lever (42% of this run’s price rows sit on campaigns whose own record reads behind, stalled or wrong-direction; none cites it).',
    '**Re-read live values before export.** 9 rows in this file were overtaken by changes deployed on 22 September.',
    '**Carry the gate’s verdict into the export** (35 rows say “change → HOLD” in their own text and export as changes), drop no-op rows, and label each bid row by the keyword it changes.',
    '**Write predictions the step can deliver** — the book’s rate for the step size, on the window it runs in — not the plan’s requirement. The account’s hit rate is 4.8%.',
]:
    bullet(b)

# ---- checklist
doc.add_heading('In order, before the change file loads', 1)
for i, b in enumerate([
    'Pull the rows in section 12 (withheld, overtaken, no-op, duplicate).',
    f"Restore the {len(by(['DARK','FADED']))} campaigns that went dark or faded; confirm they serve.",
    f"Freeze the {len(by('COLLAPSE'))} rank-collapse campaigns and start the cause checks.",
    f"Push the {len(by(['THIN_PUSH','THIN_ZERO_IN']))} in-focus thin rows with volume on the modifier, sized to each row’s room, daily to 09-28.",
    f"Fix the mix on the {len(by('LEAK'))} leaking campaigns — base cut, top-of-search price held (in-focus rows may add one capped top-of-search step in the same write).",
    'On in-focus rows with the right mix and short clicks: budget where it runs out, modifier where it doesn’t, eligibility check where price is already at the limit.',
    f"Hold the {len(by(['THIN_OUT','THIN_ZERO_OUT','THIN_TINY']))} thin out-of-focus / low-volume rows flat, and the out-of-focus rows that are working.",
    'Non-ranking: bring the over-ceiling ones down on the base; leave the ones inside their ceiling alone.',
    'After the deal (10-06): probe down any price bought for the deal, re-read the mix, grade every write in this list.',
], 1):
    para(f'{i}. {b}')

# ---- appendix
doc.add_heading('Appendix — every ranking campaign by situation', 1)
names = {'THIN_PUSH': '1 · Thin, in focus, volume — push', 'THIN_ZERO_IN': '1 · Thin (zero), in focus — push', 'THIN_TINY': '2 · Thin, in focus, low volume — hold',
         'THIN_OUT': '3 · Thin, out of focus — hold', 'THIN_ZERO_OUT': '3 · Zero, out of focus — hold', 'LEAK': '4 · Product-page leak — fix mix',
         'SHORT_PRICE': '5 · Mix right, short — raise modifier', 'SHORT_BUDGET': '5 · Mix right, short — raise budget', 'SHORT_ATLIMIT': '5 · At limit — check eligibility',
         'OUT_WORKING': '6 · Out of focus, working — hold flat', 'OUT_WEAK': '6 · Out of focus, weak — taper', 'DARK': '7 · Went dark — restore', 'FADED': '7 · Faded — restore / investigate',
         'COLLAPSE': '8 · Rank collapse — investigate', 'ROS_HEAVY': '9 · Rest-of-search heavy', 'ON_TARGET': '9 · On target — hold'}
rows = []
for c in sorted(CATS, key=lambda c: (names[c['cat']], c['short'])):
    rows.append([names[c['cat']], c['short'][:62], c['R']['d90']['t3'], c['R']['d14']['t3'], c['R']['deal8']['tos']['c'], pct(c['R'][c['mixw']]['pp_sh']), eng_short(c)])
table(['Situation', 'Campaign', 'Clicks 90d', 'Clicks 14d', 'TOS clicks deal', 'PP share', 'The run'], rows, widths=[3.4, 5.4, 1.2, 1.2, 1.3, 1.2, 3.6], size=7)
doc.save(OUT)
print('saved', OUT)


# ---------------- register of every ranking campaign's situation and write ----------------
def action(c):
    k = c['cat']; p = c['em'].get('price_now')
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
        return 'Hold; keep budget raise if capping; post-deal probe −3–5%'
    if k == 'ROS_HEAVY':
        return 'ROS modifier to 0%; else treat as leak'
    return ''


import openpyxl
from openpyxl.styles import Font, PatternFill
wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Ranking campaigns'
hdr = ['Situation', 'Campaign', 'Focus', 'Tier', 'Group limit', 'Clicks 90d', 'Clicks 14d', 'PP share (read window)', 'TOS clicks/day pre-deal', 'TOS clicks/day deal', 'Clicks last 3d',
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
XL = OUT.replace('.docx', '.xlsx')
wb.save(XL); print('saved', XL)
