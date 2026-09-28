"""LTSF SKUs (operator, 28 Sep: a low-selling child with high stock). Per product, on its own Sellerboard stock and 30-day units:
LTSF = a non-White child with 180+ days of Available cover, or 90+ days with 30-day units at or below its size's median.
The size's pick for Auto/Broad/Phrase = the LTSF child with the most units beyond 90 days of cover among those that sold 5+ units in 30 days (else among all)."""
import json, re, sys
from statistics import median
d = sys.argv[1]
INV = json.load(open(f'{d}/inventory_children.json')); S = {x['sku']: x for x in json.load(open(f'{d}/child_sales.json'))['d30']}
out, pick = [], {}
for sz in ('KING', 'QUEEN', 'CALIFKING', 'FULL', 'TWIN'):
    rows = [r for r in INV if re.match(rf'BAMBOO-{sz}-', r['sku'])]
    med = median([S.get(r['sku'], {}).get('units', 0) or 0 for r in rows])
    cand = []
    for r in rows:
        if 'WHITE' in r['sku']:
            continue
        a = r['fba_available'] or 0; v = r['velocity_day'] or 0; u = S.get(r['sku'], {}).get('units', 0) or 0
        if a < 20:
            continue
        days = a / v if v else 9999
        if days >= 180 or (days >= 90 and u <= med):
            excess = a - v * 90
            cand.append(dict(sku=r['sku'], size=sz, units30=u, available=a, days=round(days) if days < 9999 else None, excess=round(excess)))
    cand.sort(key=lambda x: -x['excess'])
    out += cand
    sold = [x for x in cand if x['units30'] >= 5]      # prefer a child that still sells: a 1-unit-a-month child drags a discovery campaign's conversion
    pick[sz] = (sold or cand)[0]['sku'] if cand else None
json.dump([x['sku'] for x in out], open(f'{d}/ltsf_skus.json', 'w'))
json.dump(dict(rows=out, pick=pick), open(f'{d}/ltsf_detail.json', 'w'), indent=1)
print(d, pick)
for x in out: print('   ', x)
