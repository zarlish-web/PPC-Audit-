"""LTSF view: the S4-LTSF sheet (column V = Total AIS Charge) joined to today's Sellerboard stock and sales.
Aged units left today are an estimate: the sheet's aged units − its 'Total Sold' (sales 7/15–8/27) − 30-day pace × 33 days (8/28–9/29), floored at 0,
assuming the oldest units sell first. Output: v2/out/ltsf.json"""
import json, collections
import load as L

P = json.load(open(L.OUT + 'product.json'))
SKU = {s['sku']: s for s in P['skus']}
S = json.load(open(L.RAW + 'ltsf/ltsf.json'))
rows = []
for i, r in enumerate(S['rows']):
    s = SKU.get(r['sku']) or {}
    e3, iv = s.get('e30') or {}, s.get('inv') or {}
    vel = (e3.get('units') or 0) / 30
    est_left = max(0.0, (r['ais_units'] or 0) - (r['total_sold'] or 0) - vel * 33)
    rows.append(dict(rank=i + 1, sku=r['sku'], asin=r['asin'], size=r['size'].title(), total_ais=r['total_ais'], ais_units=r['ais_units'], ais_per_unit=r['ais_per_unit'],
                     oldest_bucket=r['oldest_bucket'], status_sheet=r['status'], sold_sheet=r['total_sold'], margin_sheet=r['margin'], price_sheet=r['price'],
                     sellable_now=iv.get('sellable'), vel30=round(vel, 2), days_cover=iv.get('days_sellable_30'), est_aged_left=round(est_left),
                     pba_unit30=e3.get('pba_unit'), in_catalog=bool(s),
                     avg_charge_month=r['avg_charge_month'], moh=r['moh'],
                     # storage/AIS avoided by selling one aged unit now = the sheet's monthly charge per aged unit × its months on hand (columns AU, AT)
                     avoid_per_unit=round((r['avg_charge_month'] or 0) / r['ais_units'] * max(r['moh'] or 0, 0), 2) if r['ais_units'] and (r['avg_charge_month'] or 0) > 0 else 0.0))
by_size = collections.defaultdict(list)
for r in rows:
    by_size[r['size']].append(r)
# the size's LTSF target(s): by Total AIS Charge, only those with aged units still estimated left
targets = {z: [r['sku'] for r in v if r['est_aged_left'] > 0][:3] for z, v in by_size.items()}
json.dump(dict(rows=rows, targets_by_size=targets, totals=dict(ais=round(sum(r['total_ais'] for r in rows), 2), units=sum(r['ais_units'] for r in rows))),
          open(L.OUT + 'ltsf.json', 'w'), indent=1)
if __name__ == '__main__':
    for r in rows[:16]:
        print(r['rank'], r['sku'][:28].ljust(28), r['size'], r['total_ais'], r['ais_units'], r['oldest_bucket'][11:30], 'sold', r['sold_sheet'], '| now', r['sellable_now'], 'vel', r['vel30'], 'est aged left', r['est_aged_left'], r['status_sheet'])
    print(targets)
