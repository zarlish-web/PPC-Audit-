"""Stage 4 — Keywords: every search term with spend in 90 days (Command Center all-keywords lens) plus every Amazon SQP-tracked term,
each with its ad metrics (30/90 days), market metrics (SQP), organic rank from three sources, class, size, colour.
Output: v2/out/keywords.json"""
import json, re, collections, statistics as st
import load as L

P = json.load(open(L.OUT + 'product.json'))
K30 = {r['keyword']: r for r in L.KW30}
K90 = {r['keyword']: r for r in L.KW90}
CCRANK = {r['keyword']: r for r in L.RANKS}

ROSTER_BRANDS = {(e.get('brandName') or '').strip().lower() for e in L.MKT['roster']['entries'] if e.get('brandName')}
DD_BRANDS = set()
for d in L.NICHES.values():
    for r in d.get('competitors') or []:
        if r.get('brand'):
            DD_BRANDS.add(r['brand'].strip().lower())
BRANDS = {b for b in ROSTER_BRANDS | DD_BRANDS if len(b) > 2 and b not in ('n\\a', 'decolure')} | {'candory', 'mulberry park', 'juicy couture', 'amazon basics'}
OFF = ['chair cover', 'pillowcase', 'pillow case', 'bonnet', 'pajama', 'pyjama', 'robe', 'scrunchie', 'eye mask', 'sleep mask', 'dress', 'duvet', 'comforter',
       'quilt', 'blanket', 'curtain', 'throw', 'crib', 'baby', 'toddler', 'bamboo', 'linen', 'flannel', 'microfiber', 'jersey', 'percale', 'egyptian', 'mattress',
       'topper', 'rv ', 'bunk', 'dog', 'hair', 'scarf', 'fabric', 'cotton', 'fitted sheet only', 'waterproof', 'bedspread', 'skirt']
CORE = re.compile(r'satin|silk|sateen|silky|charmeuse|slik|siik|satn|stain sheet')
SPAN = re.compile(r'sábana|sabana|seda|juego de|satinad|draps|drap ')
COLOURS = ['black', 'white', 'grey', 'gray', 'silver', 'navy', 'blue', 'pink', 'blush', 'purple', 'lavender', 'lilac', 'plum', 'red', 'burgundy', 'wine', 'green',
           'sage', 'emerald', 'olive', 'gold', 'champagne', 'ivory', 'cream', 'beige', 'tan', 'taupe', 'rosewood', 'mauve', 'teal', 'orange', 'brown', 'yellow',
           'leopard', 'cheetah', 'striped', 'stripe', 'floral', 'print']


def kclass(k):
    t = k.lower()
    if re.match(r'^b0[a-z0-9]{8}$', t):
        return 'ASIN (product page)'
    if 'decolure' in t or re.search(r'\bdec[a-z]{0,3}l[a-z]{0,2}re\b', t):
        return 'Brand (own)'
    if any(re.search(r'\b' + re.escape(b) + r'\b', t) for b in BRANDS):
        return 'Competitor brand'
    if SPAN.search(t):
        return 'Spanish / French'
    if any(o in t for o in OFF) and not re.search(r'sheet', t):
        return 'Other product'
    if any(o in t for o in OFF):
        return 'Mixed (other product words)'
    if CORE.search(t):
        return 'Core satin/silk'
    if 'cool' in t:
        return 'Adjacent: cooling'
    return 'Adjacent: generic bedding'


def size_of(k):
    t = k.lower()
    if re.search(r'cal(ifornia)? ?king', t):
        return 'Cal King'
    for z in ('king', 'queen', 'full', 'twin'):
        if re.search(r'\b' + z + r'\b', t):
            return z.title()
    if re.search(r'\bdouble\b', t):
        return 'Full'
    return None


def colour_of(k):
    t = k.lower()
    for c in COLOURS:
        if re.search(r'\b' + c + r'\b', t):
            return c
    return None


# break-even ACoS of the child a ranking term would advertise: the size's Black (verified in ranking.py); generic → Queen Black
SKU = {s['sku']: s for s in P['skus']}
BLACK = {'Queen': 'SATIN-QUEEN-BLACK', 'King': 'SATIN-KING-BLACK', 'Full': 'SATIN-FULL-BLACK', 'Twin': 'SATIN-TWIN-BLACK-NEW'}


def be_acos_for(size):
    s = SKU.get(BLACK.get(size or 'Queen', 'SATIN-QUEEN-BLACK'))
    return (s['e30'] or {}).get('be_acos') if s else None


def radar_stats(k):
    r = L.RADAR.get(k)
    if not r:
        return {}
    xs = sorted(r['ranks'], key=lambda x: x['date'])
    q3 = [x['organicRank'] for x in xs if x['date'] >= '2026-07-01' and x['organicRank']]
    last7 = [x['organicRank'] for x in xs[-7:] if x['organicRank']]
    first14 = [x['organicRank'] for x in xs[:14] if x['organicRank']]
    ranked = [v for v in q3 if v < 101]
    return dict(radar_now=xs[-1]['organicRank'] if xs else None, radar_med7=st.median(last7) if last7 else None, radar_med_first14=st.median(first14) if first14 else None,
                radar_best=min(ranked) if ranked else None, radar_worst=max(ranked) if ranked else None, radar_days_unranked=sum(1 for v in q3 if v >= 101),
                radar_sp_med7=st.median([x['sponsoredRank'] for x in xs[-7:] if x.get('sponsoredRank')]) if xs else None)


def cc_rank_stats(k):
    r = CCRANK.get(k)
    if not r:
        return {}
    cells = sorted([c for c in r['cells'] if c.get('state') == 'ranked'], key=lambda c: c['date'])
    if not cells:
        return dict(cc_tracked=r.get('tracked'))
    v = [c['rank'] for c in cells]
    return dict(cc_tracked=True, cc_rank_last=v[-1], cc_rank_med30=st.median([c['rank'] for c in cells if c['date'] >= '2026-08-31'] or v), cc_rank_best90=min(v), cc_days=len(v))


def m(r):
    if not r:
        return {}
    return {f: r.get(f) for f in ('impressions', 'clicks', 'ctr', 'cpc', 'orders', 'cvr', 'spend', 'sales', 'acos', 'units')}


terms = set(K90) | set(K30) | set(L.SQP['q3']) | set(L.SQP['q2'])
out = []
for k in terms:
    a, b = K30.get(k) or {}, K90.get(k) or {}
    q3, q2, q4 = L.SQP['q3'].get(k) or {}, L.SQP['q2'].get(k) or {}, L.SQP['q4_2025'].get(k) or {}
    z = size_of(k)
    row = dict(keyword=k, cls=kclass(k), size=z, colour=colour_of(k), relevancy=a.get('relevancy') or b.get('relevancy'), syntax=a.get('syntax') or b.get('syntax'),
               sv_library=a.get('searchVolume') or b.get('searchVolume'), sv_source=a.get('searchVolumeSource') or b.get('searchVolumeSource'),
               m30=m(a), m90=m(b), cc_rank_30d_median=a.get('rank') if a else b.get('rank'),
               sqp_q3=dict(volume=q3.get('searchQueryVolume'), clicks=q3.get('clicksTotalCount'), purchases=q3.get('purchasesTotalCount'), mkt_cvr=q3.get('cvrTotal'),
                           our_cvr=q3.get('cvrAsin'), our_impr_share=q3.get('impressionsAsinShare'), our_click_share=q3.get('clicksAsinShare'),
                           our_purchase_share=q3.get('purchasesAsinShare'), our_purchases=q3.get('purchasesAsinCount'), our_clicks=q3.get('clicksAsinCount')) if q3 else None,
               sqp_q2_share=q2.get('purchasesAsinShare'), sqp_q4_share=q4.get('purchasesAsinShare'), sqp_q4_volume=q4.get('searchQueryVolume'), sqp_q2_volume=q2.get('searchQueryVolume'),
               asinsight=dict(organic=(L.OUR_AS.get(k) or {}).get('organic_rank'), sp=(L.OUR_AS.get(k) or {}).get('sp_rank'),
                              weekly_sv=(L.OUR_AS.get(k) or {}).get('weekly_search_volume'), top3_click=(L.OUR_AS.get(k) or {}).get('top3_click_share'),
                              top3_conv=(L.OUR_AS.get(k) or {}).get('top3_conversion_share')) if k in L.OUR_AS else None,
               radar_ppc=dict(sp_rank=(L.RADAR_PPC.get(k) or {}).get('sponsoredRank'), impr_rank=(L.RADAR_PPC.get(k) or {}).get('impressionRank'),
                              impr_share=(L.RADAR_PPC.get(k) or {}).get('impressionRankShare')) if k in L.RADAR_PPC else None,
               be_acos=be_acos_for(z if z in BLACK else None))
    row.update(radar_stats(k))
    row.update(cc_rank_stats(k))
    out.append(row)
out.sort(key=lambda r: -((r['m90'] or {}).get('spend') or 0))
json.dump(out, open(L.OUT + 'keywords.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    print(len(out), collections.Counter(r['cls'] for r in out))
    by = collections.defaultdict(lambda: [0, 0, 0, 0])
    for r in out:
        x = by[r['cls']]
        x[0] += (r['m30'] or {}).get('spend') or 0; x[1] += (r['m30'] or {}).get('sales') or 0; x[2] += (r['m30'] or {}).get('orders') or 0; x[3] += (r['m30'] or {}).get('clicks') or 0
    for c, x in sorted(by.items(), key=lambda kv: -kv[1][0]):
        print(f'{c:28} spend30 {x[0]:8.0f} acos {x[0] / max(x[1], 1) * 100:5.1f}% orders {x[2]:5.0f} clicks {x[3]:6.0f}')
    for r in out[:8]:
        print(r['keyword'], r['cls'], r['size'], r['m30'].get('spend'), r.get('radar_now'), r.get('cc_rank_last'), (r['asinsight'] or {}).get('organic'))
