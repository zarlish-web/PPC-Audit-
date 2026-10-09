import json, html, re, statistics
W = '/tmp/claude-0/cs/w/'
REPO = '/home/user/PPC-Audit-/deliverables/coolinens-cooling-sheets/'
SRC = open(REPO + 'coolinens-sheets-launch-plan.html').read()
D = json.load(open(W + 'hist_page.json'))
POS = json.load(open(W + 'pos_trend.json'))
TRF = json.load(open(W + 'traffic_hist.json'))
e = html.escape
M = D['MONTHS']
ML = {m: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][int(m[5:7]) - 1] + ' ' + m[2:4] for m in set(M) | set(D['DMONTHS']) | {r['month'][:7] for r in D['d2']} | {r['month'][:7] for r in D['s2']}}
def _f(v):
    try: return float(v)
    except (TypeError, ValueError): return None
money = lambda v, n=0: '' if v in (None, '') else (f'${_f(v):,.{n}f}' if _f(v) is not None else html.escape(str(v)))
pct = lambda v, n=1: '' if v in (None, '') else (f'{_f(v) * 100:.{n}f}%' if _f(v) is not None else html.escape(str(v)))
num = lambda v, n=0: '' if v in (None, '') else (f'{_f(v):,.{n}f}' if _f(v) is not None else html.escape(str(v)))
def fnum(x):
    try: return float(x)
    except (TypeError, ValueError): return None

def tbl(head, rows, num_cols=(), tid='', cls=''):
    h = ''.join(f'<th class="{"n" if i in num_cols else ""}">{x}</th>' for i, x in enumerate(head))
    b = ''.join('<tr>' + ''.join(f'<td class="{"n" if i in num_cols else ""}">{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<div class="tw {cls}"><table{(" id=" + chr(34) + tid + chr(34)) if tid else ""}><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
chip = lambda t, k='': f'<span class="chip {k}">{e(t)}</span>'
V, EST, GAP = chip('Verified', 'ok'), chip('Estimate', 'warn'), chip('Not available', 'bad')

def card(cid, title, rng, src, status=V, note=''):
    return (f'<figure class="viz" id="{cid}"><figcaption><div class="vt">{title}</div>'
            f'<div class="vm"><span class="rng">{rng}</span> · {src} {status}</div></figcaption>'
            f'<div class="vtabs" role="tablist"><button type="button" class="vb on" data-v="chart">Chart</button><button type="button" class="vb" data-v="table">Table</button></div>'
            f'<div class="vbody" data-chart="{cid}"></div>{("<p class=vnote>" + note + "</p>") if note else ""}</figure>')

KW = {k['kw']: k for k in D['kws']}
FULL = lambda m: ML[m][:4] + '20' + m[2:4]
PLAN = [k for k in D['kws'] if k['b'] in (1, 2, 3)]

# ------------------------------------------------------------------ market panel (keywords with SQP in every month Oct 25 to Sep 26)
panel = [k for k in PLAN if all(k['sqp'][i] for i in range(12))]
ptot = [sum((k['sqp'][i] or {}).get('sv', 0) for k in panel) if all(k['sqp'][i] for k in panel) or i == 12 else None for i in range(13)]
ptot = [sum((k['sqp'][i] or {}).get('sv', 0) for k in panel) for i in range(13)]
pk = max(range(12), key=lambda i: ptot[i]); lo = min(range(12), key=lambda i: ptot[i])
ratio = ptot[pk] / ptot[lo]
oct_yoy = ptot[12] / ptot[0] - 1
agg = D['agg']
cvr_rng = (min(a['cvr'] for a in agg[:12]), max(a['cvr'] for a in agg[:12]))

def season(k):
    s = k['sqp']
    w = [s[i]['sv'] for i in (1, 2, 3, 4) if s[i]]; su = [s[i]['sv'] for i in (6, 7, 8, 9) if s[i]]
    return (sum(su) / len(su)) / (sum(w) / len(w)) if len(w) >= 2 and len(su) >= 2 else None
def sizeg(k):
    s = k['size'] or ''
    return 'No size' if not s else s
grp = {}
for k in PLAN:
    r = season(k)
    if r: grp.setdefault(sizeg(k), []).append(r)
seas_rows = [[e(g), len(v), f'{statistics.median(v):.2f}x', f'{min(v):.2f}x to {max(v):.2f}x'] for g, v in sorted(grp.items(), key=lambda t: -statistics.median(t[1]))]

def yoy(k):
    a, b = k['sqp'][0], k['sqp'][12]
    return (b['sv'] / a['sv'] - 1) if a and b and a['sv'] else None
ylist = sorted([(yoy(k), k) for k in PLAN if yoy(k) is not None and (k['sqp'][0]['sv'] >= 400)], key=lambda t: -t[0])
emerging = [t for t in ylist if t[0] >= 0.25][:8]
declining = [t for t in ylist[::-1] if t[0] <= -0.2][:8]

# keyword trend label
def label(k):
    r = season(k); y = yoy(k)
    parts = []
    if r: parts.append('strong summer peak' if r >= 1.8 else ('moderate summer peak' if r >= 1.3 else 'flat across the year'))
    if y is not None: parts.append(('Oct up ' if y >= 0 else 'Oct down ') + f'{abs(y) * 100:.0f}% on Oct 2025')
    return ', '.join(parts)

def srk(k, m):
    if not k['sr']: return None
    v = fnum(k['sr'].get(m))
    return v

# ------------------------------------------------------------------ keyword history table (all plan keywords)
khist = []
for k in sorted(PLAN, key=lambda x: (x['b'], -x['sv'])):
    s = k['sqp']; sv = lambda i: num(s[i]['sv']) if s[i] else '<span class="na">no data</span>'
    rk = lambda m: ('NR' if srk(k, m) == 101 else num(srk(k, m))) if srk(k, m) is not None else '<span class="na">n/a</span>'
    best = None
    if k['sr']:
        vals = [fnum(v) for v in k['sr'].values() if fnum(v) not in (None, 101)]
        best = min(vals) if vals else None
    dmed = (k['dc'] or {}).get('med')
    riv = k['riv'] or {}
    rb = []
    for b, v in riv.items():
        mm = re.match(r'#(\d+)', str(v))
        if mm: rb.append((int(mm.group(1)), b))
    rb.sort()
    r = season(k)
    khist.append([f'<a href="#kx" class="kxl" data-k="{e(k["kw"])}">{e(k["kw"])}</a>', k['b'], num(k['sv']), sv(0), sv(3), sv(9), sv(12),
                  (f'{r:.2f}x' if r else '<span class="na">n/a</span>'), rk('2025-10'), rk('2026-01'), rk('2026-07'), rk('2026-10'),
                  (num(best) if best else '<span class="na">n/a</span>'), (num(dmed) if dmed else '<span class="na">n/a</span>'),
                  (f'{e(rb[0][1])} #{rb[0][0]}' if rb else '<span class="na">n/a</span>')])

# ------------------------------------------------------------------ rank map (Sleephoria, Decolure)
def rcell(v):
    v = fnum(v)
    if v is None: return '<td class="hm na">·</td>'
    if v >= 101: return '<td class="hm nr">NR</td>'
    c = 'h1' if v <= 5 else 'h2' if v <= 10 else 'h3' if v <= 20 else 'h4' if v <= 50 else 'h5'
    return f'<td class="hm {c}">{v:.0f}</td>'
sall = sorted([t for t in D['srank_all'].items() if sum(1 for m in M if fnum(t[1]['m'].get(m)) is not None) >= 3], key=lambda t: -(fnum(t[1]['sv']) or 0))[:60]
smap = ('<div class="tw hmw"><table class="hmt"><thead><tr><th>Keyword</th><th class="n">Search vol.</th>' + ''.join(f'<th class="n">{ML[m]}</th>' for m in M) + '</tr></thead><tbody>'
        + ''.join(f'<tr><td>{e(k)}</td><td class="n">{num(v["sv"])}</td>' + ''.join(rcell(v['m'].get(m)) for m in M) + '</tr>' for k, v in sall) + '</tbody></table></div>')
DM = D['DMONTHS']
dmap = ('<div class="tw hmw"><table class="hmt"><thead><tr><th>Keyword</th>' + ''.join(f'<th class="n">{ML[m]}</th>' for m in DM) + '</tr></thead><tbody>'
        + ''.join(f'<tr><td>{e(k)}</td>' + ''.join(rcell(v.get(m)) for m in DM) + '</tr>' for k, v in D['drank_all'].items()) + '</tbody></table></div>')
dsumt = tbl(['Keyword', 'Days crawled', 'Days ranked', 'Best rank', 'Best date', 'Days in top 20', 'First top 20'], [[e(str(r.get('keyword'))), num(r.get('crawled_days')), num(r.get('ranked_days')), ('#' + num(r.get('best_rank'))) if r.get('best_rank') else '<span class=na>never ranked</span>', e(str(r.get('best_date') or '')), num(r.get('days_top20')), e(str(r.get('first_top20') or ''))] for r in D['dsum'] if r.get('crawled_days')], num_cols=(1, 2, 3, 5))
legend_hm = '<div class="hml"><span class="hm h1">1 to 5</span><span class="hm h2">6 to 10</span><span class="hm h3">11 to 20</span><span class="hm h4">21 to 50</span><span class="hm h5">51 to 100</span><span class="hm nr">NR not in top 100</span><span class="hm na">· no reading</span></div>'

# ------------------------------------------------------------------ competitors
bench = D['bench']
brows = [[e(b['date']), e(b['niche']), b['n'], money(b['price'], 2), num(b['sales']), money(b['rev']), num(b['reviews']), b['rating'], num(b['kw']), num(b['launch_kw'])] for b in bench]
mrows = []
for mv in D['moves']:
    a, z = mv['pts'][0], mv['pts'][-1]
    ch = lambda x, y: '' if not x or not y else (f'+{(y / x - 1) * 100:.0f}%' if y >= x else f'{(y / x - 1) * 100:.0f}%')
    mrows.append([f'{e(mv["brand"])}<div class="sub">{e(mv["asin"])}</div>', f'{ML[a["date"][:7]]} to {ML[z["date"][:7]]}', f'{num(a["bsr"])} to {num(z["bsr"])}',
                  f'{num(a["sales"])} to {num(z["sales"])}', ch(a['sales'], z['sales']), f'{money(a["price"], 2)} to {money(z["price"], 2)}',
                  f'{num(a["reviews"])} to {num(z["reviews"])}', f'{a["adv"] or 0} to {z["adv"] or 0}'])
# snapshot table (latest dive of each ASIN, Oct 2026 dives)
latest = {}
for s in D['snaps']:
    if s['asin'] not in latest or s['date'] > latest[s['asin']]['date']: latest[s['asin']] = s
def fabric(s):
    t = s['title'].lower()
    if s['brand'].upper() in ('SLEEPHORIA', 'DECOLURE'): return 'Our brands'
    return 'Bamboo, viscose or rayon' if re.search(r'bamboo|viscose|rayon|tencel|lyocell', t) else 'Synthetic cooling fabric'
scat = [{'b': s['brand'], 'a': s['asin'], 'x': s['sales'], 'y': s['price'], 'g': fabric(s), 'd': s['date'], 'r': s['reviews']} for s in latest.values() if s['sales'] and s['price']]
# traffic snapshots
trows = []
for r in TRF['rivals']:
    p = r['pts']
    if not p: continue
    a, z = p[0], p[-1]
    trows.append([e(r['label']), e(r['tier'] or ''), f'{e(a["date"])}' + (f' to {e(z["date"])}' if len(p) > 1 else ''), num(a['traffic']) + (f' to {num(z["traffic"])}' if len(p) > 1 else ''),
                  (f'{(z["traffic"] / a["traffic"] - 1) * 100:+.0f}%' if len(p) > 1 and a['traffic'] else '<span class="na">one snapshot</span>'), num(z['keywords'])])
ours_t = TRF['ours']
# placement scores
pos = POS['asins']
pos_m = sorted({m for v in pos.values() for m in v['m']})
prow = []
for a, v in sorted(pos.items(), key=lambda t: -(t[1]['m'].get('2026-09', [0])[0])):
    prow.append([e(v['name'])] + [num(v['m'].get(m, [None])[0]) if m in v['m'] else '' for m in pos_m] + [num(v['m'].get(m, [None, None])[1]) if m in v['m'] else '' for m in ('2026-04', '2026-09')])
prof = D['profiles']
profrows = [[e(str(p.get('Brand', ''))), e(str(p.get('Main child ASIN', ''))), e(str(p.get('Material', '') or '')), e(str(p.get('Queen / ref price', '') or '')), e(str(p.get('Rating', '') or '')), e(str(p.get('Reviews', '') or '')),
             e(str(p.get('BSR (latest)', '') or '')), e(str(p.get('Est. sales', '') or '')), e(str(p.get('"cooling sheets" organic / SP rank', '') or '')), e(str(p.get('Strengths', '') or '')), e(str(p.get('Weaknesses', '') or ''))] for p in prof]

# ------------------------------------------------------------------ Sleephoria / Decolure business series
s2 = [r for r in D['s2'] if r['month']]
d2 = [r for r in D['d2'] if r['month']]
s1 = dict((r[0], r[1]) for r in D['s1']); d1 = dict((r[0], r[1]) for r in D['d1'])
def period_rows(rows, key):
    out = []
    for r in rows:
        if str(r.get(key, '')).startswith('DELTA'): continue
        out.append(r)
    return out
s3 = D['s3']
s3rows = [[e(r['period']), r['days'], money(r['spend']), money(r['ad_sales']), f'{fnum(r["acos"]):.1f}%' if fnum(r['acos']) is not None else '', money(r['total_sales']), f'{fnum(r["tacos"]):.1f}%' if fnum(r['tacos']) is not None else '',
           money(r.get('cpc'), 2), f'{fnum(r.get("cvr")):.1f}%' if fnum(r.get('cvr')) is not None else '', num(r.get('orders'))] for r in s3]
d3rows = []
for r in D['d3']:
    w = str(r['window'])
    d3rows.append([e(w.replace('..', ' to ')), e(str(r['spend'])), e(str(r['ad_sales'])), e(str(r['acos_pct'])), e(str(r['tacos_pct'])), e(str(r['cpc'])), e(str(r['cvr_pct'])), e(str(r['total_sales'])), e(str(r['units'])), e(str(r['asp']))])
def sizerows(rows):
    return [[e(str(r.get('size'))), e(str(r.get('window'))), num(r.get('units')), (f"{fnum(r.get('share_units_pct')):.1f}%" if fnum(r.get('share_units_pct')) is not None else ''), money(r.get('sales')), money(r.get('asp'), 2), (f"{fnum(r.get('cvr_pct')):.2f}%" if fnum(r.get('cvr_pct')) is not None else ''), money(r.get('np_per_unit'), 2), money(r.get('ad_spend'))] for r in rows]
def mtrows(rows, k):
    return [[f'<b>{e(str(r[k]))}</b>', '', '', '', '', '', '', ''] if str(r.get('spend')) == 'spend' else [e(str(r[k])), money(r.get('spend')), money(r.get('sales')), num(r.get('orders')), num(r.get('clicks')), pct(r.get('ACoS')) if r.get('ACoS') is not None else '', pct(r.get('CVR')) if r.get('CVR') is not None else '', money(r.get('CPC'), 2) if r.get('CPC') is not None else ''] for r in rows]
s4rows = [[e(str(r.get('keyword'))), e(str(r.get('first_top20') or '')), e(str(r.get('first_top10') or '')), e(str(r.get('days_from_ad_start_to_top10') or '')), money(r.get('oct25_targeted_kw_spend')), money(r.get('oct25_spend_per_day'), 2), num(r.get('oct25_clicks_per_day'), 1), num(r.get('oct25_orders_per_day'), 2), (f"{fnum(r.get('oct25_acos')):.1f}%" if fnum(r.get('oct25_acos')) is not None else '')] for r in D['s4']]
s11rows = [[e(str(r.get('period'))), e(str(r.get('direction'))), e(str(r.get('evidence'))), e(str(r.get('cause'))), e(str(r.get('confidence')))] for r in D['s11']]
d9rows = [[e(str(r.get('date_or_week'))), e(str(r.get('direction'))), e(str(r.get('magnitude'))), e(str(r.get('likely_cause'))), e(str(r.get('confidence')))] for r in D['d9']]
def strows(st):
    return [[e(str(r.get('SKU'))), e(str(r.get('start'))), e(str(r.get('end'))), e(str(r.get('days'))), e(str(r.get('type')).split(' (')[0]), num(fnum(r.get('est_lost_units_sku')), 0), money(r.get('est_lost_sales_sku_usd'))] for r in st['top']]

# ------------------------------------------------------------------ comparison facts
sl_head = KW['cooling sheets queen']; ch = KW['cooling sheets']
cmp_rows = [
    ['Selling price (average)', f'{money(s1["Avg selling price"], 2)} lifetime; {money(78.39, 2)} Oct 2026', f'{money(d1["Avg selling price"], 2)} lifetime; {money(39.58, 2)} Oct 2026', '$79.99 Queen at launch', 'Niche median $72.49 (Bamboo dive, 5 Oct 2026); $36.97 (Decolure 4 PC dive)'],
    ['Lifetime sales', money(s1['Lifetime sales']) + ' (Jul 2025 to Oct 2026)', money(d1['Lifetime sales']) + ' (Oct 2023 to Oct 2026)', 'None yet', ''],
    ['Lifetime TACoS', pct(s1['Lifetime TACoS']), pct(d1['Lifetime TACoS']), 'Plan: 38.9% ACoS in Batch 1', ''],
    ['Lifetime net profit', money(s1['Lifetime net profit']) + f' ({pct(s1["Net margin"])})', money(d1['Lifetime net profit']) + ' after $27,837 LTSF and removals', '', ''],
    ['Ad conversion, exact match', '12.8% (Exact, full history)', 'Exact 59% ACoS; product targeting 15.4% CVR', 'Plan 7.9% Batch 1', 'Market CVR (all brands, SQP) ' + f'{cvr_rng[0] * 100:.1f}% to {cvr_rng[1] * 100:.1f}% a month'],
    ['Best organic rank, cooling sheets', '#3 (Mar 2026 median)', '#4 best day (25 Apr 2025); #9 median Apr to May 2025', 'Target: top 10 by week 8', 'Leader today: Bedsure PureWoven #2'],
    ['Best organic rank, cooling sheets queen', '#5 (Oct to Nov 2025 median)', '#3 best day (25 Apr 2025); #6 median May 2025', 'Target: top 5 by week 8', "Love's cabin #5, Bedsure #6"],
    ['Time from first ad to top 10', '9 to 11 days on head terms (Oct 2025, at $4 to $6 CPC)', 'Not measured: already in the top 20 when tracking began (1 Apr 2025)', 'Plan path: top 20 wk 2, top 10 wk 4', ''],
    ['Low season (Jan)', 'Sales $24.4k (Jan 2026) vs $72.4k (Oct 2025); queen rank #67', 'Sales $4.8k (Jan 2024) after spend cut; rank fell', 'Floor $25 to $30 a day on Queen', 'Search volume Jan 2026 at its low: ' + f'{ptot[lo]:,.0f} vs peak {ptot[pk]:,.0f} on the panel'],
    ['Stock-outs (estimated lost sales)', money(D['sst']['lost']) + f' across {D["sst"]["n"]} SKU events', money(D['dst']['lost']) + f' across {D["dst"]["n"]} SKU events', '4,024 units, no inbound', ''],
]

# ------------------------------------------------------------------ JSON bundle for charts
def ser(rows, key, mkey='month', f=lambda v: v):
    return [f(fnum(r.get(key))) if fnum(r.get(key)) is not None else None for r in rows]
CH = {
  'm_panel': {'x': [ML[m] for m in M], 'series': [{'n': f'Search volume, {len(panel)} keyword panel', 'v': ptot}], 'fmt': 'int', 'kind': 'bar', 'partial': [12]},
  'm_heads': {'x': [ML[m] for m in M], 'series': [{'n': k, 'v': [x['sv'] if x else None for x in KW[k]['sqp']]} for k in ('cooling sheets', 'cooling sheets queen', 'cooling sheets king size', 'cooling bed sheets')], 'fmt': 'int'},
  'm_cvr': {'x': [ML[m] for m in M], 'series': [{'n': 'Market conversion (purchases / clicks, all brands)', 'v': [a['cvr'] for a in agg]}], 'fmt': 'pct', 'zero': True},
  'm_share': {'x': [ML[m] for m in M], 'series': [{'n': 'Sleephoria share of clicks', 'v': [a['cs'] for a in agg]}, {'n': 'Sleephoria share of purchases', 'v': [a['ps'] for a in agg]}], 'fmt': 'pct', 'zero': True},
  's_sales': {'x': [ML[r['month'][:7]]  for r in s2], 'series': [{'n': 'Total sales', 'v': ser(s2, 'sales')}, {'n': 'Ad sales', 'v': ser(s2, 'ad_sales')}], 'fmt': 'usd', 'zero': True},
  's_eff': {'x': [ML[r['month'][:7]]  for r in s2], 'series': [{'n': 'ACoS', 'v': ser(s2, 'ppc_acos_pct', f=lambda v: v / 100)}, {'n': 'TACoS', 'v': ser(s2, 'tacos_pct', f=lambda v: v / 100)}], 'fmt': 'pct', 'zero': True},
  's_asp': {'x': [ML[r['month'][:7]]  for r in s2], 'series': [{'n': 'Average selling price', 'v': ser(s2, 'asp')}], 'fmt': 'usd2'},
  's_rank': {'x': [ML[m] for m in M], 'series': [{'n': k, 'v': [fnum(KW[k]['sr'].get(m)) if KW[k]['sr'] else None for m in M]} for k in ('cooling sheets', 'cooling sheets queen', 'cooling sheets king size', 'cooling sheets twin')], 'fmt': 'rank', 'invert': True},
  'd_sales': {'x': [ML[r['month'][:7]] for r in d2], 'series': [{'n': 'Total sales', 'v': ser(d2, 'total_sales')}, {'n': 'Ad sales', 'v': ser(d2, 'ppc_ad_sales')}], 'fmt': 'usd', 'zero': True},
  'd_eff': {'x': [ML[r['month'][:7]] for r in d2], 'series': [{'n': 'ACoS', 'v': ser(d2, 'ppc_acos_pct', f=lambda v: v / 100)}, {'n': 'TACoS', 'v': ser(d2, 'tacos_ppc_pct', f=lambda v: v / 100)}], 'fmt': 'pct', 'zero': True},
  'd_asp': {'x': [ML[r['month'][:7]] for r in d2], 'series': [{'n': 'Average selling price', 'v': ser(d2, 'asp')}], 'fmt': 'usd2'},
  'd_rank': {'x': [ML[m] for m in DM], 'series': [{'n': k, 'v': [D['drank_all'].get(k, {}).get(m) for m in DM]} for k in ('cooling sheets', 'cooling sheets queen', 'cooling sheets king size') if k in D['drank_all']], 'fmt': 'rank', 'invert': True},
  'c_pos': {'x': [ML[m] for m in pos_m], 'series': [{'n': pos[a]['name'], 'v': [pos[a]['m'].get(m, [None])[0] for m in pos_m]} for a in ('B0DN1DVKH5', 'B07YKCZHGK', 'B0FT7LV7PP', 'B0F7LY3K8C')], 'fmt': 'int', 'zero': True},
  'c_scatter': {'pts': scat, 'groups': ['Bamboo, viscose or rayon', 'Synthetic cooling fabric', 'Our brands']},
}
KX = {k['kw']: {'b': k['b'], 'size': k['size'], 'obj': k['obj'], 'sv': k['sv'], 'tr': k['tr'], 'base': k['base'], 'mod': k['mod'], 'eff': k['eff'], 'ceil': k['ceil'], 'med': k['med'], 'cvr': k['cvr'], 'clk': k['clk'], 'spend': k['spend'],
              'wsv': k['wsv'], 'mkl': k['mkl'], 'top3': k['top3'], 'sqp': [[x['sv'], x['cvr'], x['cs'], x['ps'], x['d']] if x else None for x in k['sqp']],
              'sr': [fnum(k['sr'].get(m)) for m in M] if k['sr'] else None, 'dr': [k['dr'].get(m) for m in DM] if k['dr'] else None,
              'sl': k['sl'], 'dc': k['dc'], 'riv': k['riv'], 'lab': label(k)} for k in D['kws']}
BUNDLE = json.dumps({'CH': CH, 'KX': KX, 'M': [ML[m] for m in M], 'DM': [ML[m] for m in DM]}, separators=(',', ':'), default=str)

# ------------------------------------------------------------------ text pieces
sl_cs0, sl_cs7, sl_cs9 = agg[0]['cs'], agg[9]['cs'], agg[11]['cs']
kopts = ''.join(f'<optgroup label="Batch {b}">' + ''.join(f'<option value="{e(k["kw"])}"{" selected" if k["kw"] == "cooling sheets queen" else ""}>{e(k["kw"])}</option>' for k in sorted(PLAN, key=lambda x: -x['sv']) if k['b'] == b) + '</optgroup>' for b in (1, 2, 3))
kopts += '<optgroup label="Removed from the batches">' + ''.join(f'<option value="{e(k["kw"])}">{e(k["kw"])}</option>' for k in D['kws'] if k['b'] == 'Removed') + '</optgroup>'

cov_rows = [
 ['Keyword search demand by month', 'Amazon Search Query Performance (Brand Analytics) through the DataDive Rank Radar on Sleephoria (B0FTSWF3M7)', 'Oct 2025 to 8 Oct 2026', 'Monthly, scaled to a 30 day month from the days reported', f'132 tracked; {sum(1 for k in PLAN if any(k["sqp"]))} of {len(PLAN)} plan keywords', V, 'Nothing before Oct 2025 (the Rank Radar started then), so no full year on year. A query only reports in weeks Sleephoria was shown for it: Queen terms have gaps in Jun to Jul 2026 when Sleephoria dropped out of the top 100. Oct 2026 covers 8 days.'],
 ['Current search volume (used in the plan)', 'ASINsight weekly export, 6 Oct 2026, x 4.33', '6 Oct 2026', 'Snapshot', '86 plan keywords', V, 'Checked against SQP: cooling sheets queen 34,224 plan vs 34,995 SQP (Oct 2026, scaled).'],
 ['Reference search volume', 'DataDive master keyword list (MKL) and the seasonal Oct to Jan estimate', 'Build dates in the workbook', 'Static', 'All 104', EST, 'Used only where ASINsight has no reading (18 long tail keywords).'],
 ['Sleephoria organic rank', 'DataDive Rank Radar daily crawl', 'Oct 2025 to Oct 2026', 'Daily, shown as the monthly median', '132 keywords', V, 'NR = outside the top 100 that month.'],
 ['Decolure organic rank', 'Command center daily rank crawl', '1 Apr 2025 to Oct 2026', 'Daily, shown as the monthly median', f'{len(D["drank_all"])} keywords monthly; {len(D["dsum"])} with best rank and days in the top 20', V, 'Nothing before 1 Apr 2025, so the 2023 launch and the 2024 season have no rank history.'],
 ['Sleephoria business and PPC', 'Sellerboard; command center ppc_daily', 'Jul 2025 to 7 Oct 2026', 'Monthly', 'Whole listing', V, 'PPC launched 3 Oct 2025; Oct 2026 is month to date.'],
 ['Decolure business and PPC', 'Sellerboard from Oct 2023; PPC from Sellerboard to Jun 2025, command center from Jul 2025', 'Oct 2023 to 7 Oct 2026', 'Monthly', 'Whole listing', V, 'Two PPC sources join in Jul 2025; keyword level PPC only from Apr 2025.'],
 ['Keyword PPC results', 'Command center ppc_keywords', 'Sleephoria Oct 2025 to Oct 2026; Decolure Apr 2025 to Oct 2026', 'Lifetime totals per keyword', '1,662 and 313 search terms', V, 'Totals, not monthly: monthly keyword PPC is not stored.'],
 ['Price matched conversion', 'Command center, Sleephoria at $71 to $78', '17 Aug to 9 Oct 2026', 'Window total', '9 keywords with 100+ clicks', V, ''],
 ['Competitor sales, price, BSR, reviews', 'DataDive niche dives', 'Feb 2025, Mar 2026, May 2026, Oct 2026', 'Point snapshots', '7 dives, 152 listings', EST, 'Each dive has its own competitor set, so medians are not like for like; sales are DataDive 30 day estimates.'],
 ['Competitor placement (organic and ad) scores', 'ASINsight daily scores through the command center', '8 Apr to 4 Oct 2026', 'Daily, shown as the monthly mean', '12 rivals and Sleephoria', V, 'Scores, not traffic or rank. The Decolure Queen listing has no rows.'],
 ['Competitor traffic', 'ASINsight 7 day traffic exports', 'Aug to Oct 2026', 'Weekly snapshots, 1 or 2 per rival', '28 rivals', V, 'Too few snapshots for a trend on half the rivals.'],
 ['Competitor rank by keyword', 'ASINsight exports', 'Late Sep 2026', 'Snapshot', '20 rivals x 104 keywords', V, 'No monthly rank history for rivals: they are not on a Rank Radar.'],
 ['Stock-outs', 'Sellerboard inventory history', 'Sleephoria Jul 2025 on; Decolure Oct 2023 on', 'Event level', f'{D["sst"]["n"]} and {D["dst"]["n"]} events', EST, 'Many events are inferred from monthly units (confidence stated per row in the workbook).'],
 ['CooLinens', 'No history', 'Listing live for Vine, ads start 15 Oct 2026', '', '8 reviews, 4.2 stars', GAP, 'No own sales, rank or ad history yet: the plan reads its own conversion at 50 to 100 clicks a keyword.'],
]
missing = ['Search demand before Oct 2025, so no complete year on year comparison (October 2026 against October 2025 is the only like for like month, and October 2026 has 8 days).',
           'Monthly organic rank for competitors on each keyword. Only the late September 2026 snapshot and the daily placement scores (Apr to Oct 2026) exist.',
           'Decolure rank before 1 April 2025: the 2023 launch and the whole 2024 season have sales history but no rank history.',
           'Monthly keyword level PPC for either brand. Keyword results are lifetime totals.',
           'Like for like competitor sales over time: each niche dive tracked a different set of listings.',
           'Any CooLinens history: the listing has not been advertised.']

nav = ('<nav class="idx" aria-label="Sections"><div class="ng">History and market</div>'
       '<a href="#top">Overview</a><a href="#format">About this page</a><a href="#coverage">Data coverage</a><a href="#market">Market and demand</a><a href="#kx">Keyword explorer</a>'
       '<a href="#khist">Keyword history table</a><a href="#rankmap">Rank history map</a><a href="#comp">Competitors</a><a href="#sleep">Sleephoria history</a><a href="#deco">Decolure history</a><a href="#cmp">Comparisons</a>'
       '<div class="ng">Launch plan</div><a href="#batches">The three batches</a><a href="#b1">Batch 1</a><a href="#queen">Queen pushes</a><a href="#all">Batch 1 keywords</a><a href="#pat">Product targeting</a>'
       '<a href="#b2">Batch 2</a><a href="#b3">Batch 3</a><a href="#side">Side by side</a><a href="#verify">Verification</a><a href="#evidence">Evidence</a><a href="#tracking">Launch tracking</a><a href="#decisions">Decisions</a><a href="#risks">Risks</a></nav>')

hdr_old = SRC[SRC.find('<header id="top">'):SRC.find('</header>') + 9]
kpis_old = hdr_old[hdr_old.find('<div class="kpis">'):hdr_old.find('<h3>The plan in brief</h3>')]
brief_old = hdr_old[hdr_old.find('<h3>The plan in brief</h3>'):hdr_old.find('</header>')]
header = f'''<header id="top">
 <div class="eyebrow">CooLinens · Cooling Sheets 4 Piece · Amazon US · PPC launch 15 Oct 2026</div>
 <h1>CooLinens Cooling Sheets: market history and launch plan</h1>
 <div class="owner"><div><span class="lab">Owner</span><b>Shayan Rana</b></div><div><span class="lab">Updated</span>10 Oct 2026</div><div><span class="lab">Data to</span>8 Oct 2026</div><div><span class="lab">Working files</span><a href="https://docs.google.com/spreadsheets/d/1KRK_4Vn9J22aplEeM2ygu-Egd7L5OSRjRpHQHR5GeMk/edit?usp=sharing">Google Sheet (working copy)</a> · CooLinens_Cooling_Sheets_4PC_Launch_Strategy.xlsx · Batch 1 upload file</div></div>
 <p class="lede">The full history behind the launch: how every keyword's demand and ranking moved, how Sleephoria and Decolure performed, how the competitors changed, and what that means for CooLinens. The launch plan follows in three batches. Every chart states its date range, interval and source, and every gap is named.</p>
 <div class="status"><span class="chip ok">Upload file matches the workbook: 64 of 64</span><span class="chip ok">Workbook: 8,307 formulas, 0 errors</span><span class="chip ok">192 input checks, 0 failures</span><span class="chip warn">D1 Sleephoria stand down: awaiting sign off</span></div>
 <div class="kpis">
  <div class="kpi"><span class="lab">Demand swing</span><span class="val">{ratio:.1f}x</span><span class="sub">{ML[M[pk]]} peak vs {ML[M[lo]]} low, {len(panel)} keyword panel</span></div>
  <div class="kpi"><span class="lab">October vs October</span><span class="val">{oct_yoy * 100:+.0f}%</span><span class="sub">panel search volume, Oct 2026 (8 days) vs Oct 2025</span></div>
  <div class="kpi"><span class="lab">Market conversion</span><span class="val">{cvr_rng[0] * 100:.1f} to {cvr_rng[1] * 100:.1f}%</span><span class="sub">all brands, monthly, plan keywords</span></div>
  <div class="kpi"><span class="lab">Sleephoria click share</span><span class="val">{sl_cs0 * 100:.1f}% to {sl_cs9 * 100:.1f}%</span><span class="sub">Oct 2025 vs Sep 2026 (low {sl_cs7 * 100:.1f}% in Jul)</span></div>
 </div>
 <h3>The launch plan</h3>{kpis_old}{brief_old}
</header>'''

fmt_sec = '''<section id="format"><h2>About this page</h2>
<p>Format: one interactive page in two parts. <b>Part 1, history and market</b>: data coverage, market and demand, a keyword explorer for every keyword in the plan, the keyword history table, rank history maps, competitors, Sleephoria, Decolure, and the comparisons. <b>Part 2, launch plan</b>: the three batches and everything needed to run them.</p>
<ul class="fmt"><li>Every chart has a <b>Chart / Table</b> switch, hover detail, and a caption with its <b>date range</b>, <b>interval</b> and <b>source</b>.</li>
<li>Every dataset carries a status: ''' + V + ''' measured from the source, ''' + EST + ''' modelled or estimated by the source, ''' + GAP + ''' does not exist.</li>
<li>Months are calendar months. Search volume is scaled to a 30 day month. Ranks are monthly medians of a daily crawl; lower is better and NR means outside the top 100.</li>
<li>Sleephoria (the sister listing) and Decolure (the earlier bamboo listing) are reference and context. The plan's bids come from the market, not from them.</li></ul></section>'''

cov_sec = (f'<section id="coverage"><h2>Data coverage and limitations</h2><p class="lede">Which history exists, for which dates, at which interval, and what it cannot tell us.</p>'
           + tbl(['Dataset', 'Source', 'Date range', 'Interval', 'Coverage', 'Status', 'Limitation'], cov_rows, cls='wide')
           + '<h3>Not available, and not filled with assumptions</h3><ul>' + ''.join(f'<li>{e(x)}</li>' for x in missing) + '</ul></section>')

def kwlist(L):
    return ', '.join(f'<b>{e(k["kw"])}</b> {y * 100:+.0f}%' for y, k in L) or 'none'
mkt_sec = f'''<section id="market"><h2>Market and demand trends</h2>
<p class="lede">How search demand, conversion and Sleephoria's share of the market moved month by month. The panel is the {len(panel)} plan keywords with a reading in every month from Oct 2025 to Sep 2026, so months are comparable.</p>
<div class="grid2">{card('m_panel', 'Search volume, keyword panel', 'Oct 2025 to Oct 2026 (Oct 2026 = 8 days, scaled)', 'SQP via DataDive', V, f'Peak {ML[M[pk]]}: {ptot[pk]:,.0f}. Low {ML[M[lo]]}: {ptot[lo]:,.0f}. October 2026 is running {oct_yoy * 100:+.0f}% on October 2025.')}
{card('m_heads', 'Head terms: search volume', 'Oct 2025 to Oct 2026, monthly', 'SQP via DataDive', V, 'Gaps on cooling sheets queen in Jun 2026 are months with no SQP reading (Sleephoria was not shown), not zero demand.')}
{card('m_cvr', 'Market conversion, all brands', 'Oct 2025 to Oct 2026, monthly', 'SQP purchases / clicks over plan keywords', V)}
{card('m_share', "Sleephoria's share of the market", 'Oct 2025 to Oct 2026, monthly', 'SQP ASIN share over plan keywords', V, 'Share of all clicks and purchases on the plan keywords. It fell from May 2026 when stock ran out and rank was lost.')}</div>
<h3>Seasonality by size: summer (Apr to Jul) against winter (Nov to Feb)</h3>
{tbl(['Size in the query', 'Keywords', 'Median ratio', 'Range'], seas_rows, num_cols=(1, 2))}
<h3>Early October read: October 2026 against October 2025</h3>
<p><b>Growing</b> (25% or more): {kwlist(emerging)}.</p><p><b>Falling</b> (20% or more): {kwlist(declining)}.</p>
<p class="vnote">October 2026 has 8 days of data, so treat this as an early read. Keywords with fewer than 400 searches in October 2025 are left out.</p>
<h3>What the market history says</h3><ul>
<li>Demand is seasonal: the panel ran {ratio:.1f}x higher in {FULL(M[pk])} than in {FULL(M[lo])}. The launch on 15 Oct starts on the way down to the winter low; the ranking push has to be paid for in a falling market and protected through January.</li>
<li>Conversion barely moves with the season ({cvr_rng[0] * 100:.1f}% to {cvr_rng[1] * 100:.1f}% a month), so the swing is in traffic, not buyer intent: a rank held into the spring is worth about {ptot[pk] / ptot[0]:.1f}x the October traffic at the July peak.</li>
<li>Sleephoria's share of clicks went from {sl_cs0 * 100:.1f}% (Oct 2025) to {sl_cs7 * 100:.1f}% (Jul 2026) during the peak season, the months of its stock-outs and rank loss. The summer demand went to Bedsure, Love's cabin and KRIMANO instead, whose organic placement scores rose from April to July (see Competitors).</li></ul>
</section>'''

kx_sec = f'''<section id="kx"><h2>Keyword explorer</h2>
<p class="lede">The complete history of any keyword in the plan: demand by month, Sleephoria and Decolure rank by month, Sleephoria's share, lifetime ad results for both brands, today's competitors, and the plan for CooLinens.</p>
<div class="kxbar"><label for="kxs">Keyword</label><select id="kxs">{kopts}</select><input id="kxf" type="search" placeholder="Type to find a keyword" aria-label="Find a keyword" list="kxlist"><datalist id="kxlist">{''.join(f'<option value="{e(k["kw"])}">' for k in D['kws'])}</datalist></div>
<div id="kxhead" class="kxhead"></div>
<div class="grid2">{card('kx_sv', 'Search volume', 'Oct 2025 to Oct 2026, monthly', 'SQP via DataDive', V, 'Empty months: no SQP reading that month.')}
{card('kx_rank', 'Organic rank, monthly median', 'Oct 2025 to Oct 2026, monthly median (Decolure from Apr 2025 is in the rank map)', 'Rank Radar; command center', V, 'Lower is better. Points at 101 = outside the top 100.')}
{card('kx_share', "Sleephoria share of this keyword", 'Oct 2025 to Oct 2026, monthly', 'SQP ASIN share', V)}
{card('kx_cvr', 'Market conversion on this keyword', 'Oct 2025 to Oct 2026, monthly', 'SQP purchases / clicks, all brands', V)}</div>
<div class="grid3"><div class="panel" id="kxplan"></div><div class="panel" id="kxbrands"></div><div class="panel" id="kxriv"></div></div>
</section>'''

khist_sec = (f'<section id="khist"><h2>Keyword history table</h2><p class="lede">Every keyword in Batches 1 to 3 on one line. Search volume is SQP, scaled to a month; ranks are Sleephoria monthly medians. Click a keyword to open it in the explorer.</p>'
             '<div class="filters" role="group" aria-label="Filter by batch"><button type="button" class="hb on" data-b="all">All batches</button><button type="button" class="hb" data-b="1">Batch 1</button><button type="button" class="hb" data-b="2">Batch 2</button><button type="button" class="hb" data-b="3">Batch 3</button></div>'
             + tbl(['Keyword', 'Batch', 'Plan volume', 'SQP Oct 25', 'SQP Jan 26', 'SQP Jul 26', 'SQP Oct 26', 'Summer / winter', 'SL rank Oct 25', 'SL rank Jan 26', 'SL rank Jul 26', 'SL rank Oct 26', 'SL best', 'Decolure median rank', 'Best rival today'], khist, num_cols=tuple(range(1, 14)), tid='kht', cls='wide')
             + '</section>')

rank_sec = f'''<section id="rankmap"><h2>Rank history map</h2>
<p class="lede">Monthly median organic rank, darker is better. Sleephoria: the 60 largest of its 132 tracked keywords. Decolure: every keyword with a rank history.</p>{legend_hm}
<h3>Sleephoria · Oct 2025 to Oct 2026 · monthly median of the daily Rank Radar crawl {V}</h3>{smap}
<h3>Decolure · Apr 2025 to Oct 2026 · monthly median of the daily crawl {V}</h3>{dmap}<h3>Decolure best rank and time in the top 20, 1 Apr 2025 to Oct 2026 {V}</h3>{dsumt}
<div class="grid2">{card('s_rank', 'Sleephoria head terms: rank', 'Oct 2025 to Oct 2026, monthly median', 'DataDive Rank Radar', V, 'Lower is better; 101 = outside the top 100.')}
{card('d_rank', 'Decolure head terms: rank', 'Apr 2025 to Oct 2026, monthly median', 'Command center', V, 'Lower is better.')}</div>
<h3>What the rank history says</h3><ul>
<li>Sleephoria reached the top 10 on 13 of 14 tracked head terms between 9 and 23 October 2025, within three weeks of the first ad on 3 October, at $4 to $6 per click. Ranks held through November, slipped in December, and collapsed in January (cooling sheets queen #67) when spend was cut to $1,634 for the month.</li>
<li>Ranks came back in February to April 2026 without heavy spend (cooling sheets #3 to #4), then fell out of the top 100 in July 2026 during the brand-wide stock-out of the hero Queen Graphite.</li>
<li>Decolure held cooling sheets queen at #6 to #12 in spring 2025 and lost it over the winter (#98 in Jan 2026). Its head term ranks have not recovered (cooling sheets #124 in Jun 2026).</li>
<li>Twin is the most stable: Sleephoria held cooling sheets twin at #2 to #6 for most of the year, which is why Twin stays capped for CooLinens.</li></ul>
</section>'''

pos_head = ['Rival'] + [f'Organic {ML[m]}' for m in pos_m] + ['Ads Apr 26', 'Ads Sep 26']
comp_sec = f'''<section id="comp"><h2>Competitors</h2>
<p class="lede">Who sells, at what price, how that changed between the niche dives of Feb 2025, Mar 2026, May 2026 and Oct 2026, and how each rival's organic and ad presence moved from April to October 2026.</p>
<h3>Market benchmarks by dive date {EST}</h3>{tbl(['Dive date', 'Niche', 'Listings', 'Median price', 'Median monthly sales', 'Median monthly revenue', 'Median reviews', 'Median rating', 'Keywords', 'Launch keywords'], brows, num_cols=(2, 3, 4, 5, 6, 7, 8, 9))}
<p class="vnote">Each dive tracked its own set of listings, so read the medians as the market each dive saw, not as one panel over time.</p>
<h3>Listings seen in more than one dive {EST}</h3>{tbl(['Listing', 'Dives', 'BSR', 'Monthly sales (est.)', 'Change', 'Price', 'Reviews', 'Advertised keywords'], mrows, num_cols=(4,))}
<div class="grid2">{card('c_pos', 'Organic placement score: risers vs Sleephoria', '8 Apr to 4 Oct 2026, monthly mean of daily scores', 'ASINsight via command center', V, 'Scores, not traffic. Higher is more organic visibility.')}
{card('c_scatter', 'Price against monthly sales, latest dive', 'Snapshots Feb 2025 to Oct 2026 (latest per listing)', 'DataDive niche dives', EST, 'Monthly sales on a log scale. Our brands = Sleephoria and Decolure.')}</div>
<h3>Organic and ad placement by month, every tracked rival {V}</h3>{tbl(pos_head, prow, num_cols=tuple(range(1, len(pos_head))), cls='wide')}
<h3>ASINsight 7 day traffic, latest snapshots {V}</h3>{tbl(['Rival', 'Tier', 'Snapshots', '7 day traffic', 'Change', 'Keywords'], trows, num_cols=(3, 4, 5))}
<p class="vnote">Sleephoria for comparison: {', '.join(f"{p['date']} {p['traffic']:,}" for p in ours_t if not p.get('coverageSuspect'))}. Snapshots marked suspect by the feed are left out.</p>
<h3>What changed in the competition</h3><ul>
<li><b>Love's cabin</b> is the biggest mover: monthly sales of about 6,500 (Mar 2026) rose to about 22,000 (Oct 2026), with the price cut from $49.99 to $37.99 and reviews up from 381 to 1,854. Its organic score more than tripled from April to July. It now holds #1 to #5 on most Queen cooling terms.</li>
<li><b>CGK Unlimited</b> (the category's BSR #2 sheet) started advertising: 0 advertised keywords in the Feb 2025 dive, 337 in Oct 2026, 202 of them at top of search. It is a $24.99 microfiber set, so it competes on price, not on cooling.</li>
<li><b>BC Bella Coterie</b> moved to paid: 327 advertised keywords (68% of the niche) in Oct 2026, and its sales eased from about 12,600 to 10,300 a month.</li>
<li><b>Premium cooling rivals stayed small</b>: REST (about 3,900 a month at $261.75), Breescape (about 1,500 at $107 to $160), Elegear (about 280, organic score falling every month). The premium, non bamboo cooling space has no leader with volume.</li>
<li><b>New entrants</b> in 2026: Amazon Basics Cooling (listed Apr 2026, about 5,200 a month by May at $49.99), KRIMANO (organic score up from 44 in April to 584 in July), Pillcase, TWK, Elegear.</li>
<li><b>Decolure</b> fell from about 477 a month (May 2026) to about 210 (Oct 2026), with the Queen Graphite out of stock and the listing showing no active FBA seller.</li></ul>
<details><summary>Competitor profiles (35 listings, ASINsight late Sep 2026 and the 8 Oct capture)</summary>{tbl(['Brand', 'Main child', 'Material', 'Price', 'Rating', 'Reviews', 'BSR', 'Est. sales', 'cooling sheets organic / ad', 'Strengths', 'Weaknesses'], profrows, cls='wide')}</details>
</section>'''

sl_sec = f'''<section id="sleep"><h2>Sleephoria history (sister listing, same product)</h2>
<p class="lede">Listing live July 2025 (Vine), PPC from 3 October 2025. Lifetime sales {money(s1['Lifetime sales'])}, {num(s1['Lifetime units'])} units, net profit {money(s1['Lifetime net profit'])} ({pct(s1['Net margin'])}), TACoS {pct(s1['Lifetime TACoS'])}. Best month {ML['2026-03']}.</p>
<div class="grid2">{card('s_sales', 'Sales and ad sales', 'Jul 2025 to Oct 2026 (Oct = month to date), monthly', 'Sellerboard; command center', V)}
{card('s_eff', 'ACoS and TACoS', 'Oct 2025 to Oct 2026, monthly', 'Command center; Sellerboard', V)}
{card('s_asp', 'Average selling price', 'Jul 2025 to Oct 2026, monthly', 'Sellerboard', V, 'Price rose from about $61 at launch to $78 in October 2026; conversion fell with it.')}</div>
<h3>Periods compared {V}</h3>{tbl(['Period', 'Days', 'Spend', 'Ad sales', 'ACoS', 'Total sales', 'TACoS', 'CPC', 'Ad CVR', 'Ad orders'], s3rows, num_cols=tuple(range(1, 10)))}
<h3>Launch rank entry, October 2025: what top 10 cost {V}</h3>{tbl(['Keyword', 'First top 20', 'First top 10', 'Days to top 10', 'Spend in Oct', 'Spend a day', 'Clicks a day', 'Orders a day', 'ACoS'], s4rows, num_cols=(3, 4, 5, 6, 7, 8))}
<h3>Size performance {V}</h3>{tbl(['Size', 'Window', 'Units', 'Share', 'Sales', 'ASP', 'CVR', 'Net profit a unit', 'Ad spend'], sizerows(D['s5']), num_cols=(2, 3, 4, 5, 6, 7, 8))}
<h3>Match type, targeting and placement, full PPC history {V}</h3>{tbl(['Type', 'Spend', 'Sales', 'Orders', 'Clicks', 'ACoS', 'CVR', 'CPC'], mtrows(D['s8'], 'match type'), num_cols=(1, 2, 3, 4, 5, 6, 7))}
<h3>Largest stock-outs (estimated lost sales {money(D['sst']['lost'])} across {D['sst']['n']} SKU events) {EST}</h3>{tbl(['SKU', 'Start', 'End', 'Days', 'Type', 'Lost units', 'Lost sales'], strows(D['sst']), num_cols=(3, 5, 6))}
<h3>Major rises and declines, with causes</h3>{tbl(['Period', 'Direction', 'Evidence', 'Cause', 'Confidence'], s11rows, cls='wide')}
</section>'''

dc_sec = f'''<section id="deco"><h2>Decolure history (earlier bamboo listing)</h2>
<p class="lede">Listing from October 2023 at $32 to $40. Lifetime sales {money(d1['Lifetime sales'])}, {num(d1['Lifetime units'])} units, PPC spend {money(d1['Lifetime PPC spend'])} (ACoS {pct(d1['Lifetime PPC ACoS'])}, TACoS {pct(d1['Lifetime TACoS'])}), net profit {money(d1['Lifetime net profit'])} after {money(-d1['LTSF + removal fees'])} of long term storage and removal fees. Best month {ML['2024-08']}.</p>
<div class="grid2">{card('d_sales', 'Sales and ad sales', 'Oct 2023 to Oct 2026 (Oct = month to date), monthly', 'Sellerboard; command center', V)}
{card('d_eff', 'ACoS and TACoS', 'Oct 2023 to Oct 2026, monthly', 'Sellerboard; command center', V)}
{card('d_asp', 'Average selling price', 'Oct 2023 to Oct 2026, monthly', 'Sellerboard', V)}</div>
<h3>Same period, year on year {V}</h3>{tbl(['Window', 'Spend', 'Ad sales', 'ACoS %', 'TACoS %', 'CPC', 'CVR %', 'Total sales', 'Units', 'ASP'], d3rows, num_cols=tuple(range(1, 10)), cls='wide')}
<h3>Size performance {V}</h3>{tbl(['Size', 'Window', 'Units', 'Share', 'Sales', 'ASP', 'CVR', 'Net profit a unit', 'Ad spend'], sizerows(D['d4']), num_cols=(2, 3, 4, 5, 6, 7, 8))}
<h3>Match type, targeting and placement, Apr 2025 to Oct 2026 {V}</h3>{tbl(['Type', 'Spend', 'Sales', 'Orders', 'Clicks', 'ACoS', 'CVR', 'CPC'], mtrows(D['d6'], 'match_type'), num_cols=(1, 2, 3, 4, 5, 6, 7))}
<h3>Largest stock-outs (estimated lost sales {money(D['dst']['lost'])} across {D['dst']['n']} SKU events) {EST}</h3>{tbl(['SKU', 'Start', 'End', 'Days', 'Type', 'Lost units', 'Lost sales'], strows(D['dst']), num_cols=(3, 5, 6))}
<h3>Major rises and declines, with causes</h3>{tbl(['Date', 'Direction', 'Magnitude', 'Likely cause', 'Confidence'], d9rows, cls='wide')}
</section>'''

cmp_sec = f'''<section id="cmp"><h2>Historical comparisons: gaps, opportunities and risks</h2>
{tbl(['Measure', 'Sleephoria', 'Decolure', 'CooLinens (plan)', 'Market'], cmp_rows, cls='wide')}
<div class="grid3">
<div class="panel"><h3>Gaps</h3><ul>
<li><b>Summer was lost, not missed by the market.</b> Search volume peaked in Jun to Jul 2026 while Sleephoria's sales fell to $29.9k (Jul) and its click share to {sl_cs7 * 100:.1f}%: the hero Queen Graphite and other colours were out of stock and rank fell out of the top 100. {V}</li>
<li><b>Premium cooling has no volume leader.</b> REST, Breescape and Elegear sell 280 to 3,900 a month at $86 to $262; the volume sits with bamboo at $35 to $68. A $79.99 synthetic cooling set sits between them. {EST}</li>
<li><b>Queen is open.</b> Sleephoria now ranks #45 on cooling sheets queen and #64 on queen sheets cooling; Decolure is unranked. King and Twin are still Sleephoria's (#4, #5). {V}</li></ul></div>
<div class="panel"><h3>Opportunities</h3><ul>
<li><b>Ranks recover cheaply in Feb to Mar.</b> Sleephoria went from #67 (Jan) to #8 (Mar) on cooling sheets queen on $3,291 to $5,382 a month: the Batch 3 push in Feb to Mar matches that. {V}</li>
<li><b>Product targeting is the cheapest order format.</b> Decolure: 15% ACoS on 2,488 orders; Sleephoria branded 14%. Batch 1 includes 12 premium rival ASINs. {V}</li>
<li><b>Fast entry is proven.</b> 9 to 11 days to top 10 on head terms at launch in Oct 2025, with $1,185 spent on cooling sheets queen that month. {V}</li>
<li><b>Growing terms</b> this October: {kwlist(emerging[:4])}. {V}</li></ul></div>
<div class="panel"><h3>Risks</h3><ul>
<li><b>Winter rank loss.</b> Both brands lost head term rank in Dec to Jan when spend was cut (Sleephoria #67, Decolure #98). The plan holds a $25 to $30 a day Queen floor. {V}</li>
<li><b>Price and conversion.</b> Sleephoria's ad conversion fell from 18.3% at $61 (Oct 2025) to about 10.5% at $71 to $78; CooLinens launches at $79.99. {V}</li>
<li><b>Stock.</b> Sleephoria lost an estimated {money(D['sst']['lost'])} to stock-outs and Decolure {money(D['dst']['lost'])}; CooLinens has 4,024 units and nothing inbound (decision D5). {EST}</li>
<li><b>Paid pressure is rising.</b> CGK and BC Bella Coterie moved to heavy advertising in 2026; Love's cabin took organic share at $37.99. {EST}</li></ul></div>
</div></section>'''

# ------------------------------------------------------------------ CSS and JS additions
css_add = '''
nav.idx .ng { font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); margin:14px 0 4px; }
nav.idx .ng:first-child { margin-top:0 }
.owner { display:flex; flex-wrap:wrap; gap:10px 26px; margin:4px 0 14px; padding:12px 14px; background:var(--surface); border:1px solid var(--line); border-radius:10px; font-size:14px }
.owner .lab { display:block; font-family:var(--mono); font-size:10.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted) }
.owner b { font-size:17px }
.owner a { color:var(--accent) }
.fmt li { margin:4px 0 }
.grid2 { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,430px),1fr)); gap:16px; margin:14px 0 }
.grid3 { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:16px; margin:14px 0 }
.panel { background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:14px 16px; min-width:0 }
.panel h3 { margin-top:0 }
.panel ul { padding-left:18px; margin:0 } .panel li { margin:6px 0; font-size:14.5px }
figure.viz { margin:0; background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:14px 14px 10px; min-width:0; position:relative }
figure.viz figcaption .vt { font-family:var(--display); font-weight:700; font-size:15.5px }
figure.viz figcaption .vm { font-size:12.5px; color:var(--muted); margin-top:2px }
figure.viz .rng { font-family:var(--mono); font-size:11.5px }
.vtabs { position:absolute; top:12px; right:12px; display:flex; gap:2px; background:var(--bg); border-radius:7px; padding:2px }
.vb { font:inherit; font-size:12px; border:0; background:transparent; color:var(--muted); padding:3px 9px; border-radius:5px; cursor:pointer }
.vb.on { background:var(--surface); color:var(--ink); box-shadow:0 0 0 1px var(--line) }
.vbody { margin-top:10px; min-height:60px }
.vbody svg { display:block; width:100%; height:auto; overflow:visible }
.vnote { font-size:12.5px; color:var(--muted); margin:8px 0 0 }
.vleg { display:flex; flex-wrap:wrap; gap:4px 14px; font-size:12.5px; color:var(--muted); margin-bottom:6px }
.vleg span { display:inline-flex; align-items:center; gap:6px }
.vleg i { width:14px; height:3px; border-radius:2px; display:inline-block }
.vleg i.dot { width:9px; height:9px; border-radius:50% }
.vtip { position:fixed; z-index:20; pointer-events:none; background:var(--surface); color:var(--ink); border:1px solid var(--line); border-radius:8px; padding:8px 10px; font-size:12.5px; box-shadow:0 6px 18px rgba(0,0,0,.14); max-width:280px; display:none }
.vtip b { display:block; margin-bottom:3px; font-family:var(--display) }
.vtip .r { display:flex; gap:8px; align-items:center; justify-content:space-between } .vtip .r i { width:10px; height:3px; display:inline-block; border-radius:2px; margin-right:6px }
.viz-root { --s1:#2a78d6; --s2:#eb6834; --s3:#1baf7a; --s4:#eda100; --grid:#e6e9eb; --axis:#8a969d; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .viz-root { --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; --grid:#2a343a; --axis:#7f8d95; } }
:root[data-theme="dark"] .viz-root { --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; --grid:#2a343a; --axis:#7f8d95; }
.vbody .tw { max-height:340px }
.kxbar { display:flex; flex-wrap:wrap; gap:8px 12px; align-items:center; margin:10px 0 }
.kxbar label { font-weight:700 }
.kxbar select, .kxbar input { font:inherit; font-size:15px; padding:7px 10px; border:1px solid var(--line); border-radius:8px; background:var(--surface); color:var(--ink); max-width:100% }
.kxhead { background:var(--accent-soft); border-radius:10px; padding:12px 14px; }
.kxhead h3 { margin:0 0 4px; font-size:20px }
.kxhead .facts { display:flex; flex-wrap:wrap; gap:6px 18px; font-size:14px }
.kv { display:grid; grid-template-columns:auto 1fr; gap:3px 12px; font-size:14px; margin:0 }
.kv dt { color:var(--muted) } .kv dd { margin:0; font-variant-numeric:tabular-nums; text-align:right }
.na { color:var(--muted); font-style:italic; font-size:12.5px }
.sub { color:var(--muted); font-size:12px }
.hmw { max-height:620px }
table.hmt td.hm, .hml .hm { text-align:center; font-variant-numeric:tabular-nums; font-size:12.5px; min-width:46px }
.hm.h1 { background:#184f95; color:#fff } .hm.h2 { background:#2a78d6; color:#fff } .hm.h3 { background:#6da7ec; color:#0b1a2b } .hm.h4 { background:#b7d3f6; color:#0b1a2b } .hm.h5 { background:#e3eefb; color:#2b3a47 }
.hm.nr { background:repeating-linear-gradient(45deg,var(--bg),var(--bg) 4px,var(--line) 4px,var(--line) 5px); color:var(--muted) }
.hm.na { color:var(--muted) }
.hml { display:flex; flex-wrap:wrap; gap:6px; margin:8px 0 } .hml .hm { padding:3px 8px; border-radius:5px }
details summary { cursor:pointer; font-weight:700; margin:14px 0 8px }
.tw.wide table { min-width:900px }
.part { border-top:2px solid var(--ink); padding-top:18px } .ph { font-size:28px }
a.kxl { color:var(--accent); text-decoration:none } a.kxl:hover { text-decoration:underline }
@media (max-width: 860px) { .wrap { grid-template-columns:minmax(0,1fr) } nav.idx { position:static } .vtabs { position:static; margin-top:8px; width:max-content } }
'''

js = r'''
<div class="vtip" id="vtip" role="status" aria-live="polite"></div>
<script id="hist-data" type="application/json">__BUNDLE__</script>
<script>
(function(){
var B=JSON.parse(document.getElementById('hist-data').textContent), CH=B.CH, KX=B.KX;
var SC=['var(--s1)','var(--s2)','var(--s3)','var(--s4)'], tip=document.getElementById('vtip');
function f(v,t){ if(v===null||v===undefined||isNaN(v)) return 'no data';
  if(t==='pct') return (v*100).toFixed(1)+'%'; if(t==='usd') return '$'+Math.round(v).toLocaleString('en-US');
  if(t==='usd2') return '$'+v.toFixed(2); if(t==='rank') return v>=101?'not in top 100':'#'+Math.round(v);
  return Math.round(v).toLocaleString('en-US'); }
function fa(v,t){ if(t==='pct'){ var q=v*100; return (Math.abs(q-Math.round(q))<1e-6?q.toFixed(0):q.toFixed(1))+'%'; } if(t==='usd'||t==='usd2'){ return v>=1000?'$'+(v/1000).toFixed(v>=10000?0:1)+'k':'$'+Math.round(v);} if(t==='rank') return v>=101?'NR':'#'+Math.round(v); return v>=1000?(v/1000).toFixed(v>=10000?0:1)+'k':Math.round(v)+''; }
function nice(mx){ if(mx<=0) return 1; var p=Math.pow(10,Math.floor(Math.log10(mx))), n=mx/p; return (n<=1?1:n<=2?2:n<=2.5?2.5:n<=5?5:10)*p; }
function showTip(ev,html){ tip.innerHTML=html; tip.style.display='block'; var x=ev.clientX+14, y=ev.clientY+14, w=tip.offsetWidth, h=tip.offsetHeight;
  if(x+w>innerWidth-8) x=ev.clientX-w-14; if(y+h>innerHeight-8) y=ev.clientY-h-14; tip.style.left=x+'px'; tip.style.top=y+'px'; }
function hideTip(){ tip.style.display='none'; }
function legend(series,dot){ if(series.length<2) return ''; return '<div class="vleg">'+series.map(function(s,i){return '<span><i class="'+(dot?'dot':'')+'" style="background:'+SC[i]+'"></i>'+s.n+'</span>';}).join('')+'</div>'; }
function table(c){ var h='<div class="tw"><table><thead><tr><th>Month</th>'+c.series.map(function(s){return '<th class="n">'+s.n+'</th>';}).join('')+'</tr></thead><tbody>';
  c.x.forEach(function(x,i){ h+='<tr><td>'+x+'</td>'+c.series.map(function(s){return '<td class="n">'+f(s.v[i],c.fmt)+'</td>';}).join('')+'</tr>'; });
  return h+'</tbody></table></div>'; }
function line(el,c){
  var W=Math.max(300,el.clientWidth||600), H=Math.round(Math.min(300,Math.max(210,W*0.48))), L=46, R=c.series.length>1?118:18, T=10, Bm=26, iw=W-L-R, ih=H-T-Bm;
  var vals=[]; c.series.forEach(function(s){ s.v.forEach(function(v){ if(v!==null&&v!==undefined&&!isNaN(v)) vals.push(v); }); });
  if(!vals.length){ el.innerHTML='<p class="na">No data in this window.</p>'; return; }
  var inv=!!c.invert, lo=c.zero||c.kind==='bar'?0:Math.min.apply(null,vals), hi=Math.max.apply(null,vals);
  var stp=null; if(inv){ lo=1; hi=Math.min(101,Math.max(10,hi)); } else { if(!c.zero && c.kind!=='bar'){ var pad=(hi-lo)*0.12||hi*0.1; lo=Math.max(0,lo-pad); } stp=nice((hi-lo)/4); lo=Math.floor(lo/stp)*stp; hi=Math.ceil(hi/stp)*stp; if(hi<=lo) hi=lo+stp; }
  var n=c.x.length, xs=function(i){ return c.kind==='bar'? L+iw*(i+0.5)/n : L+(n<2?iw/2:iw*i/(n-1)); };
  var ys=function(v){ return inv? T+ih*(v-lo)/(hi-lo) : T+ih*(1-(v-lo)/(hi-lo)); };
  var ticks=[], k; if(inv){ ticks=[1,10,20,50,101].filter(function(t){return t<=hi;}); } else { for(var tv=lo;tv<=hi+stp/2;tv+=stp) ticks.push(tv); }
  var s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+(c.title||'chart')+'">';
  ticks.forEach(function(t){ var y=ys(t); s+='<line x1="'+L+'" x2="'+(L+iw)+'" y1="'+y+'" y2="'+y+'" stroke="var(--grid)" stroke-width="1"/><text x="'+(L-6)+'" y="'+(y+4)+'" text-anchor="end" font-size="11" fill="var(--axis)">'+fa(t,c.fmt)+'</text>'; });
  var step=Math.ceil(n/(W<480?5:9));
  c.x.forEach(function(x,i){ if(i%step===0||i===n-1) s+='<text x="'+xs(i)+'" y="'+(H-8)+'" text-anchor="middle" font-size="11" fill="var(--axis)">'+x+'</text>'; });
  if(c.kind==='bar'){ var bw=Math.max(4,Math.min(34,iw/n-6)); c.series[0].v.forEach(function(v,i){ if(v===null||v===undefined) return; var y=ys(v), x=xs(i)-bw/2, h=T+ih-y, r=Math.min(4,h/2);
      var part=(c.partial||[]).indexOf(i)>=0; s+='<path d="M'+x+','+(T+ih)+'V'+(y+r)+'Q'+x+','+y+' '+(x+r)+','+y+'H'+(x+bw-r)+'Q'+(x+bw)+','+y+' '+(x+bw)+','+(y+r)+'V'+(T+ih)+'Z" fill="var(--s1)" '+(part?'fill-opacity=".45" stroke="var(--s1)" stroke-dasharray="3 2"':'')+'/>'; });
  } else {
    c.series.forEach(function(se,si){ var d='', pen=false, last=null;
      se.v.forEach(function(v,i){ if(v===null||v===undefined||isNaN(v)){ pen=false; return; } d+=(pen?'L':'M')+xs(i).toFixed(1)+','+ys(Math.min(v,hi)).toFixed(1); pen=true; last=i; });
      s+='<path d="'+d+'" fill="none" stroke="'+SC[si]+'" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>';
      se.v.forEach(function(v,i){ if(v===null||v===undefined||isNaN(v)) return; var lone=(i===0||se.v[i-1]==null)&&(i===n-1||se.v[i+1]==null); if(lone) s+='<circle cx="'+xs(i)+'" cy="'+ys(Math.min(v,hi))+'" r="3.5" fill="'+SC[si]+'" stroke="var(--surface)" stroke-width="2"/>'; });
      se._last=last; });
    if(c.series.length>1){ var labs=c.series.map(function(se,si){ return se._last===null?null:{si:si,y:ys(Math.min(se.v[se._last],hi)),t:se.n}; }).filter(Boolean).sort(function(a,b){return a.y-b.y;});
      for(k=1;k<labs.length;k++){ if(labs[k].y-labs[k-1].y<13) labs[k].y=labs[k-1].y+13; }
      labs.forEach(function(l){ var t=l.t.length>19?l.t.slice(0,18)+'…':l.t; s+='<text x="'+(L+iw+6)+'" y="'+(l.y+4)+'" font-size="11" fill="var(--muted)">'+t+'</text>'; }); }
  }
  s+='<line class="xh" x1="0" x2="0" y1="'+T+'" y2="'+(T+ih)+'" stroke="var(--axis)" stroke-width="1" stroke-dasharray="3 3" style="display:none"/>';
  s+='<rect x="'+L+'" y="'+T+'" width="'+iw+'" height="'+ih+'" fill="transparent" class="hit"/></svg>';
  el.innerHTML=legend(c.series)+s;
  var svg=el.querySelector('svg'), xh=svg.querySelector('.xh'), hit=svg.querySelector('.hit');
  hit.addEventListener('mousemove',function(ev){ var r=svg.getBoundingClientRect(), px=(ev.clientX-r.left)*W/r.width, i;
    if(c.kind==='bar') i=Math.floor((px-L)/iw*n); else i=Math.round((px-L)/iw*(n-1)); i=Math.max(0,Math.min(n-1,i));
    xh.setAttribute('x1',xs(i)); xh.setAttribute('x2',xs(i)); xh.style.display='';
    var h='<b>'+c.x[i]+((c.partial||[]).indexOf(i)>=0?' (partial month, scaled)':'')+'</b>'+c.series.map(function(se,si){ return '<div class="r"><span><i style="background:'+SC[si]+'"></i>'+se.n+'</span><span>'+f(se.v[i],c.fmt)+'</span></div>'; }).join('');
    showTip(ev,h); });
  hit.addEventListener('mouseleave',function(){ xh.style.display='none'; hideTip(); });
}
function scatter(el,c){
  var W=Math.max(300,el.clientWidth||600), H=Math.round(Math.min(320,Math.max(230,W*0.52))), L=50, R=16, T=10, Bm=30, iw=W-L-R, ih=H-T-Bm;
  var xsV=c.pts.map(function(p){return p.x;}), ysV=c.pts.map(function(p){return p.y;});
  var x0=Math.log10(Math.max(1,Math.min.apply(null,xsV)*0.8)), x1=Math.log10(Math.max.apply(null,xsV)*1.25), y1=nice(Math.max.apply(null,ysV));
  var xs=function(v){return L+iw*(Math.log10(Math.max(1,v))-x0)/(x1-x0);}, ys=function(v){return T+ih*(1-v/y1);};
  var s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Price against monthly sales">';
  for(var k=0;k<=4;k++){ var t=y1*k/4, y=ys(t); s+='<line x1="'+L+'" x2="'+(L+iw)+'" y1="'+y+'" y2="'+y+'" stroke="var(--grid)"/><text x="'+(L-6)+'" y="'+(y+4)+'" text-anchor="end" font-size="11" fill="var(--axis)">$'+Math.round(t)+'</text>'; }
  [10,100,1000,10000,100000].forEach(function(t){ var lt=Math.log10(t); if(lt<x0||lt>x1) return; var x=xs(t); s+='<line x1="'+x+'" x2="'+x+'" y1="'+T+'" y2="'+(T+ih)+'" stroke="var(--grid)"/><text x="'+x+'" y="'+(H-10)+'" text-anchor="middle" font-size="11" fill="var(--axis)">'+(t>=1000?(t/1000)+'k':t)+'</text>'; });
  s+='<line x1="'+L+'" x2="'+(L+iw)+'" y1="'+ys(79.99)+'" y2="'+ys(79.99)+'" stroke="var(--ink)" stroke-dasharray="4 3" stroke-width="1"/><text x="'+(L+iw-4)+'" y="'+(ys(79.99)-5)+'" text-anchor="end" font-size="11" fill="var(--ink)">CooLinens Queen $79.99</text>';
  c.pts.forEach(function(p,i){ var g=c.groups.indexOf(p.g); s+='<circle data-i="'+i+'" cx="'+xs(p.x).toFixed(1)+'" cy="'+ys(p.y).toFixed(1)+'" r="'+(g===2?6:4.5)+'" fill="'+SC[g]+'" fill-opacity="'+(g===2?1:.8)+'" stroke="var(--surface)" stroke-width="1.5"/>'; });
  s+='</svg>';
  el.innerHTML='<div class="vleg">'+c.groups.map(function(g,i){return '<span><i class="dot" style="background:'+SC[i]+'"></i>'+g+'</span>';}).join('')+'</div>'+s;
  el.querySelectorAll('circle').forEach(function(ci){ ci.addEventListener('mousemove',function(ev){ var p=c.pts[+ci.getAttribute('data-i')];
    showTip(ev,'<b>'+p.b+'</b>'+p.a+'<div class="r"><span>Price</span><span>$'+p.y.toFixed(2)+'</span></div><div class="r"><span>Monthly sales (est.)</span><span>'+Math.round(p.x).toLocaleString('en-US')+'</span></div><div class="r"><span>Reviews</span><span>'+(p.r||0).toLocaleString('en-US')+'</span></div><div class="r"><span>Dive</span><span>'+p.d+'</span></div>'); });
    ci.addEventListener('mouseleave',hideTip); });
}
function sctable(c){ var h='<div class="tw"><table><thead><tr><th>Listing</th><th>Group</th><th class="n">Price</th><th class="n">Monthly sales</th><th class="n">Reviews</th><th>Dive</th></tr></thead><tbody>';
  c.pts.slice().sort(function(a,b){return b.x-a.x;}).forEach(function(p){ h+='<tr><td>'+p.b+' <span class="sub">'+p.a+'</span></td><td>'+p.g+'</td><td class="n">$'+p.y.toFixed(2)+'</td><td class="n">'+Math.round(p.x).toLocaleString('en-US')+'</td><td class="n">'+(p.r||0).toLocaleString('en-US')+'</td><td>'+p.d+'</td></tr>'; });
  return h+'</tbody></table></div>'; }
function render(id){ var fig=document.getElementById(id); if(!fig) return; var body=fig.querySelector('.vbody'), c=CH[id]; if(!c) return;
  var mode=fig.getAttribute('data-mode')||'chart';
  if(mode==='table') body.innerHTML = c.pts? sctable(c) : table(c); else (c.pts? scatter : line)(body,c); }
document.querySelectorAll('figure.viz').forEach(function(fig){ fig.classList.add('viz-root');
  fig.querySelectorAll('.vb').forEach(function(b){ b.addEventListener('click',function(){ fig.querySelectorAll('.vb').forEach(function(x){x.classList.toggle('on',x===b);}); fig.setAttribute('data-mode',b.getAttribute('data-v')); render(fig.id); }); }); });
function renderAll(){ Object.keys(CH).forEach(render); }
// keyword explorer
var sel=document.getElementById('kxs'), inp=document.getElementById('kxf');
function money(v,n){ n=n===undefined?2:n; return v===null||v===undefined||v===''?'n/a':'$'+(+v).toLocaleString('en-US',{minimumFractionDigits:n,maximumFractionDigits:n}); }
function pc(v){ return v===null||v===undefined||v===''?'n/a':((+v)*100).toFixed(1)+'%'; }
function nn(v){ return v===null||v===undefined||v===''?'n/a':Math.round(+v).toLocaleString('en-US'); }
function kv(rows){ return '<dl class="kv">'+rows.map(function(r){return '<dt>'+r[0]+'</dt><dd>'+r[1]+'</dd>';}).join('')+'</dl>'; }
function showKw(k){ var d=KX[k]; if(!d) return; sel.value=k;
  var sq=d.sqp||[], M=B.M, last=null, peak=null;
  sq.forEach(function(x,i){ if(x){ last=i; if(peak===null||x[0]>sq[peak][0]) peak=i; } });
  document.getElementById('kxhead').innerHTML='<h3>'+k+'</h3><div class="facts"><span><b>Batch '+d.b+'</b></span><span>'+(d.size||'No size')+'</span><span>'+d.obj+'</span><span>Target '+(d.tr?'#'+d.tr:'n/a')+'</span><span>Plan volume '+nn(d.sv)+' a month</span>'+(peak!==null?'<span>SQP peak '+M[peak]+' '+nn(sq[peak][0])+'</span>':'<span class="na">no SQP history</span>')+(d.lab?'<span>'+d.lab+'</span>':'')+'</div>';
  CH.kx_sv={x:M,series:[{n:'Search volume',v:sq.map(function(x){return x?x[0]:null;})}],fmt:'int',kind:'bar',partial:[12]};
  var rs=[]; if(d.sr) rs.push({n:'Sleephoria',v:d.sr});
  if(d.dr){ var dm=B.DM, map={}; dm.forEach(function(m,i){map[m]=d.dr[i];}); rs.push({n:'Decolure',v:M.map(function(m){return map[m]===undefined?null:map[m];})}); }
  CH.kx_rank= rs.length? {x:M,series:rs,fmt:'rank',invert:true} : {x:M,series:[{n:'No rank history',v:M.map(function(){return null;})}],fmt:'rank'};
  CH.kx_share={x:M,series:[{n:'Share of clicks',v:sq.map(function(x){return x?x[2]:null;})},{n:'Share of purchases',v:sq.map(function(x){return x?x[3]:null;})}],fmt:'pct',zero:true};
  CH.kx_cvr={x:M,series:[{n:'Market conversion',v:sq.map(function(x){return x?x[1]:null;})}],fmt:'pct',zero:true};
  ['kx_sv','kx_rank','kx_share','kx_cvr'].forEach(render);
  document.getElementById('kxplan').innerHTML='<h3>Plan for CooLinens</h3>'+kv([['Batch',d.b],['Objective',d.obj],['Target rank',d.tr?'#'+d.tr:'n/a'],['Volume used (FINAL)',nn(d.sv)],['ASINsight weekly (6 Oct)',nn(d.wsv)],['MKL reference',nn(d.mkl)],['Expected CVR',pc(d.cvr)],['Clicks a day planned',d.clk===null?'n/a':(+d.clk).toFixed(2)],['Amazon median bid',money(d.med)],['Ranking ceiling',money(d.ceil)],['Base bid',money(d.base)],['Top of search',(d.mod||0)+'%'],['Top of search bid',money(d.eff)],['Spend a day',money(d.spend)]]);
  var sl=d.sl||{}, dc=d.dc||{};
  document.getElementById('kxbrands').innerHTML='<h3>Brand history on this keyword</h3><p class="sub">Sleephoria Oct 2025 to Oct 2026; Decolure Apr 2025 to Oct 2026. Lifetime totals.</p>'+kv([['Sleephoria clicks',nn(sl.clk)],['Sleephoria CVR',pc(sl.cvr)],['Sleephoria CPC',money(sl.cpc)],['Sleephoria ACoS',pc(sl.acos)],['Sleephoria ad sales',money(sl.sa,0)],['Sleephoria best rank',sl.best?'#'+nn(sl.best):'n/a'],['First top 10',sl.first10||'n/a'],['Decolure clicks',nn(dc.clk)],['Decolure CVR',pc(dc.cvr)],['Decolure ACoS',pc(dc.acos)],['Decolure median rank',dc.med?'#'+nn(dc.med):'n/a'],['Decolure verdict',dc.cls||'n/a']]);
  var riv=d.riv||{}, L=Object.keys(riv).map(function(b){ var t=String(riv[b]), m=/#(\d+)/.exec(t)||/^(\d+(?:\.\d+)?)$/.exec(t), sp=/SP(\d+)/.exec(t); return {b:b,o:m?+m[1]:999,s:sp?+sp[1]:null,t:riv[b]}; }).sort(function(a,b){return a.o-b.o;});
  document.getElementById('kxriv').innerHTML='<h3>Competitors on this keyword</h3><p class="sub">Organic rank and sponsored position, ASINsight late Sep 2026 (snapshot).</p>'+(L.length?'<div class="tw"><table><thead><tr><th>Rival</th><th class="n">Organic</th><th class="n">Sponsored</th></tr></thead><tbody>'+L.map(function(r){return '<tr><td>'+r.b+'</td><td class="n">'+(r.o<999?'#'+r.o:'n/a')+'</td><td class="n">'+(r.s?'#'+r.s:'')+'</td></tr>';}).join('')+'</tbody></table></div>':'<p class="na">No rival export carries this keyword.</p>');
}
sel.addEventListener('change',function(){ showKw(sel.value); });
inp.addEventListener('change',function(){ var v=inp.value.trim().toLowerCase(); if(KX[v]) showKw(v); });
document.querySelectorAll('a.kxl').forEach(function(a){ a.addEventListener('click',function(){ showKw(a.getAttribute('data-k')); }); });
var hb=document.querySelectorAll('.hb'), hr=document.querySelectorAll('#kht tbody tr');
hb.forEach(function(b){ b.addEventListener('click',function(){ hb.forEach(function(x){x.classList.toggle('on',x===b);}); var f=b.getAttribute('data-b'); hr.forEach(function(r){ r.hidden=!(f==='all'||r.children[1].textContent===f); }); }); });
showKw('cooling sheets queen'); renderAll();
var rt; addEventListener('resize',function(){ clearTimeout(rt); rt=setTimeout(renderAll,150); });
})();
</script>
'''.replace('__BUNDLE__', BUNDLE.replace('</', '<\\/'))

# ------------------------------------------------------------------ assemble
style_end = SRC.find('</style>')
head = SRC[:style_end] + css_add + SRC[style_end:SRC.find('<nav')]
plan = SRC[SRC.find('<section id="batches"'):SRC.find('</main>')]
plan = plan.replace('5,483 formulas', '8,307 formulas')
tail_script = SRC[SRC.find('<script>', SRC.find('</main>')):SRC.rfind('</script>') + 9]
out = head + nav + '\n<main>\n' + header + '\n' + fmt_sec + '\n' + cov_sec + '\n' + mkt_sec + '\n' + kx_sec + '\n' + khist_sec + '\n' + rank_sec + '\n' + comp_sec + '\n' + sl_sec + '\n' + dc_sec + '\n' + cmp_sec + '\n<div class="part"><h2 class="ph">Part 2 · Launch plan</h2></div>\n' + plan + '</main>\n</div>\n' + tail_script + js + '\n'
out = out.replace(' — ', ', ').replace('/ —<', '/ none<').replace('>—<', '><')
open(W + 'hist_page.html', 'w').write(out)
print(len(out), 'panel', len(panel), 'ratio', round(ratio, 2), 'oct', round(oct_yoy, 3), 'emerging', [(round(y, 2), k['kw']) for y, k in emerging], 'declining', [(round(y, 2), k['kw']) for y, k in declining])
