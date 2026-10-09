import json, os, glob, calendar, statistics
W = '/tmp/claude-0/cs/w/'
H = json.load(open(W + 'hist.json'))
S, D, C = H['Sleephoria_History'], H['Decolure_History'], H['Competitors']
P = json.load(open(W + 'page_final.json'))
VR = {v['kw']: v for v in json.load(open(W + 'verify_rows.json'))}

def sec(d, prefix):
    for k, v in d.items():
        if k.startswith(prefix): return v
    raise KeyError(prefix)

def table(rows, hdr_idx=0):
    hdr = rows[hdr_idx]
    return [dict(zip(hdr, r)) for r in rows[hdr_idx + 1:] if r and r[0] not in (None, '')]

MONTHS = ['2025-10', '2025-11', '2025-12', '2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06', '2026-07', '2026-08', '2026-09', '2026-10']

# ---------------------------------------------------------------- SQP monthly, Sleephoria Rank Radar
sqp = {}
for m in MONTHS:
    rows = []
    for pg in (1, 2):
        f = f'{W}sqp/p{pg}_{m}.json'
        if os.path.exists(f):
            d = json.load(open(f))
            if isinstance(d, list): rows += d
    for r in rows:
        k = r['keyword']; days = r.get('numberOfDaysWithData')
        e = sqp.setdefault(k, {})
        if not days or r.get('searchQueryVolume') is None:
            e[m] = None; continue
        y, mo = map(int, m.split('-'))
        scale = 30.0 / days
        e[m] = {'d': days,
                'sv': round(r['searchQueryVolume'] * scale),
                'clk': round((r['clicksTotalCount'] or 0) * scale),
                'pur': round((r['purchasesTotalCount'] or 0) * scale, 1),
                'cvr': r.get('cvrTotal'),
                'ctr': r.get('ctrTotal'),
                'cs': r.get('clicksAsinShare'),
                'ps': r.get('purchasesAsinShare'),
                'is': r.get('impressionsAsinShare'),
                'ac': r.get('clicksAsinCount'), 'ap': r.get('purchasesAsinCount'),
                'raw_sv': r['searchQueryVolume'], 'raw_clk': r['clicksTotalCount'], 'raw_pur': r['purchasesTotalCount']}
cover = {m: sum(1 for k in sqp if sqp[k].get(m)) for m in MONTHS}

# ---------------------------------------------------------------- ranks
s9 = sec(S, '9 ')
s9h = s9[0]
srank = {}
for r in s9[1:]:
    if not r or not r[0]: continue
    d = dict(zip(s9h, r))
    srank[d['keyword']] = {'sv': d.get('sv'), 'm': {m: d.get(m) for m in MONTHS}, 't10': d.get('top10_days_last30')}
d7 = sec(D, '7 ')
d7h = d7[0]
DMONTHS = [h for h in d7h if isinstance(h, str) and h[:2] == '20']
drank = {}; dsum = []
blk = 1
for r in d7[1:]:
    if not r or not r[0]: continue
    if r[0] == 'keyword': blk += 1; dsh = r; continue
    if blk == 2:
        dsum.append(dict(zip(dsh, r))); continue
    d = dict(zip(d7h, r))
    vals = {}
    for m in DMONTHS:
        v = d.get(m)
        try: v = float(v)
        except (TypeError, ValueError): v = None if v in (None, '', 'NR') else None
        vals[m] = v
    if any(v for v in vals.values()): drank[d['keyword']] = vals

# ---------------------------------------------------------------- lifetime keyword performance
def kwperf(rows, keys):
    out = {}
    for r in rows[2:]:
        if not r or not r[0]: continue
        d = dict(zip(rows[1], r))
        out[str(d['keyword']).lower()] = {k: d.get(src) for k, src in keys.items()}
    return out
s12 = kwperf(sec(S, '12 '), {'clk': 'clicks', 'cpc': 'cpc', 'ord': 'orders', 'cvr': 'cvr', 'sp': 'spend', 'sa': 'sales', 'acos': 'acos', 'med': 'median_rank', 'best': 'RR best rank', 'first10': 'RR first top-10', 'rel': 'relevancy'})
d10 = kwperf(sec(D, '10 '), {'clk': 'clicks', 'cpc': 'cpc', 'ord': 'orders', 'cvr': 'cvr', 'sp': 'spend', 'sa': 'sales', 'acos': 'acos', 'med': 'median_organic_rank', 'cls': 'class', 'rel': 'relevancy'})

# ---------------------------------------------------------------- competitor rank matrix
cm = sec(C, '2 ')
hdr = None; cmat = {}
for r in cm:
    if r and r[0] == 'Keyword': hdr = r; continue
    if hdr and r and r[0]:
        cmat[r[0]] = {hdr[i]: r[i] for i in range(2, min(len(hdr), len(r))) if r[i] not in (None, '')}
profiles = table(sec(C, '1 '))

# ---------------------------------------------------------------- keyword bundle (plan keywords)
def sqp_series(k):
    e = sqp.get(k, {})
    return [e.get(m) for m in MONTHS]

def trend(series):
    pts = [(i, x['sv']) for i, x in enumerate(series) if x and i < 12]
    if len(pts) < 6: return None
    w = {i: v for i, v in pts}
    def avg(ix):
        v = [w[i] for i in ix if i in w]
        return sum(v) / len(v) if v else None
    winter = avg([1, 2, 3, 4])          # Nov to Feb
    summer = avg([6, 7, 8, 9])          # Apr to Jul
    late = avg([9, 10, 11])             # Jul to Sep 2026
    early = avg([0, 1, 2])              # Oct to Dec 2025
    pk = max(pts, key=lambda t: t[1]); lo = min(pts, key=lambda t: t[1])
    return {'winter': winter, 'summer': summer, 'season': (summer / winter) if winter and summer else None,
            'late_vs_early': (late / early - 1) if late and early else None,
            'peak': MONTHS[pk[0]], 'peakv': pk[1], 'low': MONTHS[lo[0]], 'lowv': lo[1]}

kws = []
for k in P['K']:
    kw = k['kw']; ser = sqp_series(kw); v = VR.get(kw, {})
    kws.append({'kw': kw, 'b': k['b'], 'size': k['size'], 'obj': k['obj'], 'sv': k['sv'], 'tr': k['tr'], 'base': k['base'], 'mod': k['mod'],
                'eff': k['eff'], 'ceil': k['ceil'], 'med': k['med'], 'cvr': k['cvr'], 'clk': k['clk'], 'spend': k['spend'],
                'wsv': v.get('wsv'), 'top3': v.get('top3'), 'mkl': v.get('lw'),
                'sqp': [None if x is None else {kk: x[kk] for kk in ('d', 'sv', 'clk', 'pur', 'cvr', 'cs', 'ps')} for x in ser],
                'tr_': trend(ser),
                'sr': srank.get(kw, {}).get('m'), 'dr': drank.get(kw),
                'sl': s12.get(kw), 'dc': d10.get(kw), 'riv': cmat.get(kw)})

# ---------------------------------------------------------------- market aggregates over plan keywords (Batch 1 to 3)
plan = [k for k in kws if k['b'] in (1, 2, 3)]
def sizeg(k):
    s = k['size'] or ''
    return 'No size' if not s else ('Queen' if s == 'Queen' else ('King' if s == 'King' else 'Full, Twin, Cal King'))
agg = []
for i, m in enumerate(MONTHS):
    row = {'m': m, 'n': 0, 'sv': 0, 'clk': 0, 'pur': 0, 'ac': 0, 'ap': 0, 'g': {}}
    for k in plan:
        x = sqp.get(k['kw'], {}).get(m)
        if not x: continue
        row['n'] += 1; row['sv'] += x['sv']; row['clk'] += x['clk']; row['pur'] += x['pur']
        row['ac'] += (x['ac'] or 0) * 30.0 / x['d']; row['ap'] += (x['ap'] or 0) * 30.0 / x['d']
        g = sizeg(k); row['g'][g] = row['g'].get(g, 0) + x['sv']
    row['cvr'] = row['pur'] / row['clk'] if row['clk'] else None
    row['cs'] = row['ac'] / row['clk'] if row['clk'] else None
    row['ps'] = row['ap'] / row['pur'] if row['pur'] else None
    agg.append(row)

# ---------------------------------------------------------------- business history
s2 = table(sec(S, '2 '), 1)
d2 = table(sec(D, '2 '), 1)
s3 = table(sec(S, '3 '))
d3 = table(sec(D, '3 '))
s4 = table(sec(S, '4 '))
s5 = table(sec(S, '5 ')); d4 = table(sec(D, '4 '))
s8 = table(sec(S, '8 ')); d6 = table(sec(D, '6 '))
s11 = table(sec(S, '11 ')); d9 = table(sec(D, '9 '))
s1 = sec(S, '1 '); d1 = sec(D, '1 ')

def stock(rows):
    t = table(rows)
    ev = [r for r in t if str(r.get('SKU', '')).startswith('E')]
    sk = [r for r in t if not str(r.get('SKU', '')).startswith('E')]
    tot = 0
    for r in sk:
        try: tot += float(r.get('est_lost_sales_sku_usd') or 0)
        except (TypeError, ValueError): pass
    top = sorted(sk, key=lambda r: -float(r.get('est_lost_sales_sku_usd') or 0) if str(r.get('est_lost_sales_sku_usd') or '').replace('.', '', 1).isdigit() else 0)[:8]
    return {'n': len(sk), 'lost': tot, 'top': top, 'events': ev}
sst = stock(sec(S, '10 ')); dst = stock(sec(D, '8 '))

# ---------------------------------------------------------------- competitor snapshots over time (DataDive niche dives)
NICHES = {'lqH2AckqFv': 'Cooling Sheet niche', 'HlVDiTOac7': 'cooling sheets niche', 'T60bma1v17': 'Sleephoria 4 PC niche',
          'MTFXKB24sK': 'Cooling Sheet, new', 'ZapxdRplSL': 'Sleephoria niche', 'Vpg4pK4e4u': 'Bamboo Cooling Sheets', 'zjPiUVJDbS': 'Decolure 4 PC niche'}
snaps = []; bench = []
for nid, lab in NICHES.items():
    d = json.load(open(f'{W}niche/{nid}.json'))
    dt = d['latestResearchDate'][:10]
    b = d['benchmark']
    bench.append({'niche': lab, 'date': dt, 'n': len(d['competitors']), 'price': b['price'], 'sales': b['sales'], 'rev': b['revenue'], 'reviews': b['reviewCount'], 'rating': b['rating'],
                  'kw': d['statistics']['numKeywords'], 'sv': d['statistics']['totalSvOfKeywords'], 'launch_kw': d['opportunityEvaluation']['numLaunchKeywords']['value']})
    for c in d['competitors']:
        snaps.append({'date': dt, 'niche': lab, 'brand': c['brand'], 'asin': c['asin'], 'bsr': c['bsr'], 'price': c['price'], 'sales': c['sales'], 'rev': c['revenue'],
                      'reviews': c['reviewCount'], 'rating': c['rating'], 'adv': c['advertisedKws'], 'tos': c['tosKwsAds'], 'p1': c['kwRankedOnP1'],
                      'created': c['listingCreationDate'], 'title': c['title'][:110], 'ful': c['fulfillment']})
bench.sort(key=lambda x: x['date'])
by = {}
for s in snaps: by.setdefault(s['asin'], []).append(s)
moves = []
for a, L in by.items():
    L = sorted({x['date']: x for x in L}.values(), key=lambda x: x['date'])
    if len(L) >= 2: moves.append({'asin': a, 'brand': L[-1]['brand'], 'title': L[-1]['title'], 'pts': L})
moves.sort(key=lambda m: -max(p['sales'] or 0 for p in m['pts']))

out = {'MONTHS': MONTHS, 'DMONTHS': DMONTHS, 'cover': cover, 'kws': kws, 'agg': agg,
       's1': s1, 'd1': d1, 's2': s2, 'd2': d2, 's3': s3, 'd3': d3, 's4': s4, 's5': s5, 'd4': d4, 's8': s8, 'd6': d6, 's11': s11, 'd9': d9,
       'sst': sst, 'dst': dst, 'srank_all': srank, 'drank_all': drank, 'dsum': dsum, 'profiles': profiles, 'bench': bench, 'moves': moves, 'snaps': snaps}
json.dump(out, open(W + 'hist_page.json', 'w'), default=str)
print('kws', len(kws), 'with sqp', sum(1 for k in kws if any(k['sqp'])), 'cover', cover)
print('agg', [(a['m'], a['n'], a['sv'], round(a['cvr'] or 0, 4), round(a['cs'] or 0, 4)) for a in agg])
print('moves', len(moves), [(m['brand'], [(p['date'], p['sales']) for p in m['pts']]) for m in moves[:12]])
print('bench', bench)
print('sst', sst['n'], round(sst['lost']), 'dst', dst['n'], round(dst['lost']))
print('drank', len(drank), DMONTHS)
