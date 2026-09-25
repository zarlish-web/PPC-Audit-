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
OUT = '/home/user/PPC-Audit-/docs/DBS4_Bids_Placements_Corrections_20260921-dbcd48b8.docx'

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
    for line in open(f'{S}/placements_{label}.jsonl'):
        r = json.loads(line); src[r['campaignId']] = r
    t = {k: sum(((r['placements'].get(k) or {}).get('clicks') or 0) for r in src.values()) for k in ('tos', 'detail', 'other')}
    sp = sum(r['spend'] or 0 for r in src.values()); sa = sum(r['sales'] or 0 for r in src.values())
    od = sum(r['orders'] or 0 for r in src.values())
    return t, sp, sa, od


PT = {k: placements_total(k) for k in ('d90', 'pre_deal30', 'deal8')}
DAYS = {'d90': 90, 'pre_deal30': 31, 'deal8': 10}

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
