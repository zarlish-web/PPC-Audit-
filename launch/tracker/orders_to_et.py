"""Re-count units, sales and profit by US Eastern day, as Sellerboard's own dashboard shows them.

Usage: python3 -I orders_to_et.py <scratchpad> <order_page.txt> [<order_page.txt> ...]

Each order page is a saved Sellerboard dashboard_table result (entry_type order_item, search_query CL-COOLING-SHEET,
sorted orderdate asc). The API's day periods are UTC; the order timestamps let us move each order to its
Eastern-time day (UTC-4 until 1 Nov 2026, UTC-5 after). Ad spend is date-level and stays as pulled.

Writes v8/orders_et.csv (one row per order line) and rewrites units and sales in v8/sb_daily.csv for every
Eastern day the pages fully cover. Prints, per day and size, the sales, product cost, Amazon fees and order profit
(net before ads) to fill v8/day/<date>/profit.csv: net_profit there = order profit − that day's ad spend.
"""
import json, sys
from datetime import datetime, timezone, timedelta
import pandas as pd

S, pages = sys.argv[1], sys.argv[2:]
V = f'{S}/v8'


def et_day(ts):
    t = datetime.fromtimestamp(ts, timezone.utc)
    off = 4 if t < datetime(2026, 11, 1, 6, tzinfo=timezone.utc) else 5
    return (t - timedelta(hours=off)).date().isoformat()


rows = []
for p in pages:
    t = open(p).read(); d = json.loads(t[t.index('{'):])
    for r in d['result']:
        i = r['Info']
        rows.append(dict(order=i['OrderNumber'], ts=i['OrderDate'], sku=i['SKU'], status=i['OrderStatus'], units=i['Units'], sales=i['Sales'],
                         product_costs=-i['ProductCosts'], amazon_fees=-i['AmazonFees'], refunds=i.get('Refunds', 0), order_profit=i['NetProfit']))
o = pd.DataFrame(rows).drop_duplicates(['order', 'sku', 'ts'])
o['date'] = o.ts.map(et_day)
o['scope'] = o.sku.str.extract(r'CL-COOLING-SHEET-(CAL-KING|QUEEN|KING|FULL|TWIN)')[0].map({'QUEEN': 'Queen', 'KING': 'King', 'FULL': 'Full', 'TWIN': 'Twin', 'CAL-KING': 'Cal King'})
o.to_csv(f'{V}/orders_et.csv', index=False)

first, last = o.ts.min(), o.ts.max()
days = sorted(set(o.date))[1:]  # the first Eastern day may be cut by the UTC window start
sb = pd.read_csv(f'{V}/sb_daily.csv')
agg_all = o.groupby('date')[['units', 'sales']].sum()
agg_sz = o.groupby(['date', 'scope'])[['units', 'sales']].sum()
for i, r in sb.iterrows():
    if r.date not in days:
        continue
    k = r.date if r.scope == 'All' else (r.date, r.scope)
    src = agg_all if r.scope == 'All' else agg_sz
    sb.at[i, 'units'] = int(src.loc[k, 'units']) if k in src.index else 0
    sb.at[i, 'sales'] = round(float(src.loc[k, 'sales']), 2) if k in src.index else 0.0
sb.to_csv(f'{V}/sb_daily.csv', index=False)
print('Eastern days rewritten:', days[0], '→', days[-1], '| orders', len(o), '| units', int(o.units.sum()))
tab = pd.concat([o.assign(scope='All'), o]).groupby(['date', 'scope'])[['units', 'sales', 'product_costs', 'amazon_fees', 'order_profit']].sum().round(2)
print(tab.loc[days[-3]:].to_string())
