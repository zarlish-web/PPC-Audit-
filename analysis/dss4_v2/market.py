"""Stage 2 — Market: Amazon Search Query Performance (via Data Dive), niche dives over time, ASINsight share and ad presence,
CPC trend. Output: v2/out/market.json"""
import json, collections, re
import load as L

Q = ('q4_2025', 'q2', 'q3')
QLAB = {'q4_2025': 'Oct–Dec 2025', 'q2': 'Apr–Jun 2026', 'q3': 'Jul–Sep 2026'}


def tot(q, f):
    return sum((r.get(f) or 0) for r in L.SQP[q].values())


sqp_tot = {}
for q in Q:
    v, c, p, oc, op, oi, ti = (tot(q, 'searchQueryVolume'), tot(q, 'clicksTotalCount'), tot(q, 'purchasesTotalCount'), tot(q, 'clicksAsinCount'),
                               tot(q, 'purchasesAsinCount'), tot(q, 'impressionsAsinCount'), tot(q, 'impressionsTotalCount'))
    sqp_tot[q] = dict(label=QLAB[q], keywords=sum(1 for r in L.SQP[q].values() if r.get('searchQueryVolume')), volume=v, impressions=ti, clicks=c,
                      purchases=p, market_ctr=round(c / ti, 4) if ti else None, market_cvr=round(p / c, 4), our_impr_share=round(oi / ti, 4) if ti else None,
                      our_click_share=round(oc / c, 4), our_purchase_share=round(op / p, 4), our_cvr=round(op / oc, 4) if oc else None, purchases_per_day=round(p / 91, 1))

# per keyword, 3 quarters
kw = []
for k, r3 in L.SQP['q3'].items():
    row = dict(keyword=k)
    for q in Q:
        r = L.SQP[q].get(k) or {}
        row[q] = dict(volume=r.get('searchQueryVolume'), clicks=r.get('clicksTotalCount'), purchases=r.get('purchasesTotalCount'),
                      our_clicks=r.get('clicksAsinCount'), our_purchases=r.get('purchasesAsinCount'), our_impr_share=r.get('impressionsAsinShare'),
                      our_click_share=r.get('clicksAsinShare'), our_purchase_share=r.get('purchasesAsinShare'), mkt_cvr=r.get('cvrTotal'), our_cvr=r.get('cvrAsin'),
                      mkt_ctr=r.get('ctrTotal'), our_ctr=r.get('ctrAsin'), days=r.get('numberOfDaysWithData'))
    kw.append(row)
kw.sort(key=lambda x: -(x['q3']['volume'] or 0))

# seasonality of search volume: same keywords present in all three quarters
common = [x for x in kw if all(x[q]['volume'] for q in Q)]
season = {q: sum(x[q]['volume'] for x in common) for q in Q}

# ---------------------------------------------------------------- niche dives over time (satin 4-piece listings only)
dives = []
for nid, d in L.NICHES.items():
    date = (d.get('latestResearchDate') or '')[:10]
    comp = d.get('competitors') or []
    dives.append(dict(id=nid, date=date, n=len(comp), stats=d.get('statistics'), benchmark=d.get('benchmark')))
dives.sort(key=lambda x: x['date'])
SATIN = re.compile(r'satin|silk|silky|charmeuse', re.I)
track = collections.defaultdict(dict)       # asin -> date -> snapshot
brand_of = {}
for nid, d in L.NICHES.items():
    date = (d.get('latestResearchDate') or '')[:10]
    for r in d.get('competitors') or []:
        if not SATIN.search(r.get('title') or ''):
            continue
        track[r['asin']][date] = dict(price=r.get('price'), units=r.get('sales'), revenue=round(r.get('revenue') or 0), bsr=r.get('bsr'),
                                      rating=r.get('rating'), reviews=r.get('reviewCount'), p1=r.get('kwRankedOnP1'), adv=r.get('advertisedKws'),
                                      tos=r.get('tosKwsAds'), niche=nid)
        brand_of[r['asin']] = (r.get('brand') or '').strip()
tracked = []
for a, snaps in track.items():
    ds = sorted(snaps)
    tracked.append(dict(asin=a, brand=brand_of[a], dates=ds, first=snaps[ds[0]] | dict(date=ds[0]), last=snaps[ds[-1]] | dict(date=ds[-1]), n=len(ds)))
tracked.sort(key=lambda x: -(x['last']['units'] or 0))

# ---------------------------------------------------------------- ASINsight: tracked traffic, ad presence per brand
cov = L.MKT['roster']['coverage']
reach = []
for b in L.MKT['placementReach']['brands']:
    p = {x['code']: x for x in b['placements']}
    reach.append(dict(brand=b['label'], ours=b.get('ours', False), keywords=b.get('keywordCount'),
                      **{f'{c}_kw': (p.get(c) or {}).get('keywords') for c in ('OR', 'SP', 'SB', 'SBV', 'AC')},
                      **{f'{c}_share': round((p.get(c) or {}).get('share') or 0, 4) for c in ('OR', 'SP', 'SB', 'SBV')}))
hist_ours = L.HIST['ours']['points']

# ---------------------------------------------------------------- CPC / CVR trend (our ads, Command Center daily, by month)
mon = collections.defaultdict(lambda: collections.Counter())
for p in L.DAILY['points']:
    m = mon[p['date'][:7]]
    for f in ('spend', 'sales', 'clicks', 'orders', 'impressions'):
        m[f] += p.get(f) or 0
ads_trend = [dict(month=k, spend=round(v['spend']), sales=round(v['sales']), clicks=int(v['clicks']), orders=int(v['orders']),
                  cpc=round(v['spend'] / v['clicks'], 2), cvr=round(v['orders'] / v['clicks'], 4), ctr=round(v['clicks'] / v['impressions'], 4),
                  acos=round(v['spend'] / v['sales'], 4)) for k, v in sorted(mon.items())]

OUT = dict(sqp_totals=sqp_tot, sqp_keywords=kw, sqp_season_common=dict(keywords=len(common), **season), dives=dives, tracked_listings=tracked,
           asinsight=dict(tracked_traffic=cov['trackedTraffic'], our_traffic=cov['ourTraffic'], our_share=cov['ourShareOfTracked'],
                          measured=cov['loaded'], roster=cov['total'], our_history=hist_ours, reach=reach),
           ads_trend=ads_trend, events=L.DAILY.get('events'), deals=L.DAILY.get('deals'), brief_movers=L.AUDIT['brief']['sections']['competitors'].get('movers'),
           brief_summary=L.AUDIT['brief']['sections']['competitors'].get('summary'))
json.dump(OUT, open(L.OUT + 'market.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    for q, v in sqp_tot.items():
        print(q, v)
    print('season (common kws)', OUT['sqp_season_common'])
    for x in dives:
        print('dive', x['id'], x['date'], x['n'])
    for t in tracked[:14]:
        print(t['brand'][:16], t['asin'], t['n'], 'first', t['first']['date'], t['first']['price'], t['first']['units'], t['first']['bsr'], '→ last', t['last']['date'], t['last']['price'], t['last']['units'], t['last']['bsr'], t['last']['reviews'])
    for r in reach[:12]:
        print(r)
    for a in ads_trend:
        print(a)
