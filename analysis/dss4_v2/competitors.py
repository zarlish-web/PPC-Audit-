"""Stage 3 — Competitors: roster, traffic & contest (ASINsight), listing economics over time (Data Dive), ad formats incl. SB video,
listing claims and videos found (web). Output: v2/out/competitors.json"""
import json, collections, re
import load as L

M = json.load(open(L.OUT + 'market.json'))
roster = {e['competitorProductId']: e for e in L.MKT['roster']['entries']}
score = {s['competitorProductId']: s for s in L.MKT['scoreboard']['rows']}
hist = {r['competitorProductId']: r for r in L.HIST['rivals']}
reach = collections.defaultdict(list)
for b in L.MKT['placementReach']['brands']:
    reach[b['label']].append({x['code']: x.get('keywords') for x in b['placements']})
movers = {m['brand'].strip().lower(): m for m in (M.get('brief_movers') or [])}
sbv = L.SBV_BRAND if isinstance(L.SBV_BRAND, list) else L.SBV_BRAND.get('brands') or L.SBV_BRAND.get('rows') or [L.SBV_BRAND]
tracked = {t['asin']: t for t in M['tracked_listings']}
heroes = {}
for cid, c in L.COMP.items():
    heroes[int(cid)] = [h['asin'] for h in (c.get('heroAsins') or {}).get('shortlist') or []]
video = L.VIDEO

rivals = []
for cid, s in score.items():
    e = roster.get(cid, {})
    h = hist.get(cid, {}).get('points') or []
    brand = s.get('brandName') or s.get('label') or ''
    lst = [tracked[a] for a in heroes.get(cid, []) if a in tracked]
    lead = max(lst, key=lambda t: t['last']['units'] or 0) if lst else None
    mv = movers.get(brand.strip().lower())
    rr = reach.get(s.get('label'), [{}])
    r0 = rr[0] if rr else {}
    rivals.append(dict(id=cid, brand=brand or s.get('label'), label=s.get('label'), product=s.get('productName'), parent=s.get('parentAsin'), tier=s.get('tier'),
                       measured=s.get('measured'), traffic=s.get('theirTraffic'), keywords=s.get('keywordCount'), contested=s.get('contestedKeywords'),
                       our_wins=s.get('contestWins'), win_rate=s.get('contestRate'), call=s.get('call'),
                       traffic_hist=[(p['date'], p['traffic']) for p in h], heroes=heroes.get(cid, [])[:4],
                       lead_asin=lead and lead['asin'], lead_first=lead and lead['first'], lead_last=lead and lead['last'],
                       reach_or=r0.get('OR'), reach_sp=r0.get('SP'), reach_sb=r0.get('SB'), reach_sbv=r0.get('SBV'), reach_ac=r0.get('AC'),
                       price_move=mv and mv.get('price'), bsr_move=mv and mv.get('bsr'), reviews=mv and mv.get('reviews'), discount=mv and mv.get('discount')))
rivals.sort(key=lambda x: -(x['traffic'] or 0))

# keyword overlap on the big terms: who ranks where (ASINsight), per term
BIG = ['silk sheets', 'satin sheets', 'silk sheets queen', 'satin sheets queen size', 'silk bed sheets', 'black silk sheets', 'silk sheets full', 'silk sheets king',
       'satin bed sheets', 'black satin sheets', 'satin sheets king', 'satin sheets full', 'queen silk sheets set', 'silk queen bed sheets set']
term_field = []
for t in BIG:
    m = L.MKW.get(t) or {}
    rm = m.get('rivalMetrics') or {}
    rows_ = []
    for k, v in rm.items():
        e = roster.get(int(k), {})
        rows_.append(dict(brand=e.get('brandName') or k, organic=v.get('organicRank'), sp=v.get('spRank'), traffic=v.get('traffic'), ad_traffic=round(v.get('adTraffic') or 0),
                          placements=v.get('placements')))
    rows_.sort(key=lambda r: (r['organic'] or 999))
    term_field.append(dict(term=t, weekly_sv=m.get('weeklySearchVolume'), our_organic=m.get('ourOrganicRank'), our_sp=m.get('ourSpRank'), our_traffic=m.get('ourTraffic'),
                           our_placements=m.get('ourPlacements'), leader=m.get('leader'), state=m.get('state'), rivals=rows_[:8]))

OUT = dict(rivals=rivals, term_field=term_field, sbv_by_brand=L.SBV_BRAND, sbv_keywords=L.SBV_KW, video=video)
json.dump(OUT, open(L.OUT + 'competitors.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    for r in rivals[:15]:
        print(r['brand'], r['tier'], r['traffic'], r['traffic_hist'][:1], r['traffic_hist'][-1:], r['lead_asin'], (r['lead_first'] or {}).get('price'), '→', (r['lead_last'] or {}).get('price'), (r['lead_last'] or {}).get('units'), 'SP', r['reach_sp'], 'SB', r['reach_sb'], 'SBV', r['reach_sbv'], 'AC', r['reach_ac'], r['call'])
    for t in term_field[:4]:
        print(t['term'], t['weekly_sv'], 'ours', t['our_organic'], t['our_sp'], [(x['brand'], x['organic'], x['sp'], x['placements']) for x in t['rivals'][:5]])
