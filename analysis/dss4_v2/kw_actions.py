"""Stage 10 — Every search term with ad spend in 90 days (Command Center all-keywords lens), and every SQP-tracked term, gets one action
consistent with the campaign decisions. Output: v2/out/kw_actions.json"""
import json, collections, re
import load as L
import colourmatch as CM

KWS = json.load(open(L.OUT + 'keywords.json'))
R = json.load(open(L.OUT + 'ranking.json'))
D = json.load(open(L.OUT + 'decisions.json'))
LT = json.load(open(L.OUT + 'ltsf.json'))
P = json.load(open(L.OUT + 'product.json'))
SKU = {s['sku']: s for s in P['skus']}
OPP = {o['keyword']: o for o in R['opportunities']}
OWN = D['owners']
PREF = {z: v['chosen'] for z, v in R['preferred'].items()}
FAM_CVR = 1572 / 11617
def base_colour(c):
    c = (c or '').lower()
    for b in ('grey', 'gray', 'green', 'teal', 'ivory', 'taupe', 'rosewood', 'gold', 'orange', 'purple', 'black', 'white', 'blue', 'red', 'pink', 'champagne'):
        if b in c:
            return 'grey' if b == 'gray' else b
    return c


LTSF_BY_SIZE_COLOUR, LTSF_BY_COLOUR = {}, {}
for r in LT['rows']:                                   # rows are in LTSF order (Total AIS Charge), so the first hit is the priority SKU
    s = SKU.get(r['sku'])
    if s and r['est_aged_left'] >= 20:
        LTSF_BY_SIZE_COLOUR.setdefault((s['size'], base_colour(s['colour'])), r)
        LTSF_BY_COLOUR.setdefault(base_colour(s['colour']), r)
EXACT_TERMS = set()
for d in D['decisions']:
    if d['match'] == 'Exact' and d['status'] == 'ENABLED':
        EXACT_TERMS.update(d['terms'])
COLOUR_ALIAS = {'gray': 'grey', 'silver': 'grey', 'blush': 'pink', 'lilac': 'lavender', 'plum': 'purple', 'wine': 'burgundy'}

out = []
for k in KWS:
    t = k['keyword']
    m9, m3 = k['m90'] or {}, k['m30'] or {}
    q3 = k.get('sqp_q3') or {}
    o = OPP.get(t)
    clicks9, orders9, spend9 = m9.get('clicks') or 0, m9.get('orders') or 0, m9.get('spend') or 0
    if not spend9 and not q3:
        continue
    p0 = (1 - FAM_CVR) ** clicks9 if clicks9 else 1.0
    size = k.get('size') if k.get('size') in PREF else None
    col = COLOUR_ALIAS.get(k.get('colour'), k.get('colour'))
    be = k.get('be_acos')
    acos9 = m9.get('acos')
    action, why = 'No change', []
    if o and o.get('tier') in ('push', 'maintain'):
        action = f"Ranking – {o['tier']}"
        why.append(f"owned by campaign {OWN.get(t) or 'NEW exact campaign'} on {PREF[o['size'] if o['size'] != '—' else 'Queen']}; "
                   f"target {o['target_clicks_day']} paid clicks/day at the top of search (rank {o['rank_now']} → {o['target'] if o['tier'] == 'push' else 'hold'})")
    elif o and o['size'] == 'Twin' and o['cum_share_of_market'] <= 0.95:
        action = 'Hold (Twin stock)'
        why.append('Twin ranking term; Twin Black has under 60 days of stock at push pace')
    elif k['cls'] in ('Other product', 'Spanish / French') and orders9 == 0 and clicks9 >= 5:
        action = 'Negative exact (discovery campaigns)'
        why.append(f"{k['cls']}: {clicks9} clicks, 0 orders, ${spend9:.0f} in 90 days")
    elif k['cls'] == 'Competitor brand' and orders9 == 0 and clicks9 >= 10:
        action = 'Negative exact (discovery campaigns)'
        why.append(f"competitor brand search: {clicks9} clicks, 0 orders in 90 days")
    elif clicks9 >= 20 and orders9 == 0 and p0 < 0.05 and k['cls'] != 'Brand (own)':
        action = 'Negative exact (discovery campaigns)'
        why.append(f"{clicks9} clicks, 0 orders in 90 days — chance of that at our paid CVR {FAM_CVR * 100:.1f}% is {p0 * 100:.1f}%")
    elif col and col != 'black' and CM.ltsf_for_term(t, LT['rows'], SKU) and ((q3.get('volume') or 0) >= 1000 or orders9 >= 3):
        r = CM.ltsf_for_term(t, LT['rows'], SKU)
        action = 'Exact on LTSF child' + (' (already exact)' if t in EXACT_TERMS else ' (add to the existing colour/LTSF exact campaign)')
        why.append(f"colour term for {r['sku']} (LTSF #{r['rank']}, ~{r['est_aged_left']} aged units): SQP {q3.get('volume')} searches in Q3")
    elif k['cls'] == 'Core satin/silk' and orders9 >= 3 and t not in EXACT_TERMS and acos9 is not None and be and acos9 / 100 <= be * 1.5:
        action = 'Harvest candidate (no new campaign — add as exact target where a campaign of the same size/objective exists)'
        why.append(f"{orders9} orders at ACoS {acos9}% (break-even {be * 100:.1f}%) in 90 days, not bought exact")
    elif clicks9:
        why.append(f"{clicks9} clicks, {orders9} orders, ACoS {acos9}% in 90 days — no rule fires")
    out.append(dict(keyword=t, cls=k['cls'], size=k.get('size'), colour=k.get('colour'), action=action, why='; '.join(why),
                    clicks30=m3.get('clicks'), orders30=m3.get('orders'), spend30=m3.get('spend'), acos30=m3.get('acos'), cvr30=m3.get('cvr'), cpc30=m3.get('cpc'),
                    clicks90=clicks9, orders90=orders9, spend90=round(spend9, 2), acos90=acos9, sqp_volume_q3=q3.get('volume'), mkt_purchases_q3=q3.get('purchases'),
                    our_purchase_share_q3=q3.get('our_purchase_share'), share_q2=k.get('sqp_q2_share'), share_q4_2025=k.get('sqp_q4_share'),
                    rank_radar=k.get('radar_med7'), rank_cc=k.get('cc_rank_med30'), rank_asinsight=(k.get('asinsight') or {}).get('organic'),
                    be_acos=be, tier=o and o.get('tier'), owner=OWN.get(t)))
out.sort(key=lambda r: -(r['spend90'] or 0))
json.dump(out, open(L.OUT + 'kw_actions.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    c = collections.Counter(r['action'].split(' (')[0] for r in out)
    print(len(out), c)
    sp = collections.Counter()
    for r in out:
        sp[r['action'].split(' (')[0]] += r['spend90'] or 0
    print({k: round(v) for k, v in sp.items()})
    for r in out:
        if r['action'].startswith('Exact on LTSF'):
            print(r['keyword'], r['why'])
