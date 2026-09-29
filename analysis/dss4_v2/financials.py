"""Stage 12 — P&L now vs the plan (30-day basis, Sellerboard family totals + the plan's per-campaign changes), TACoS evaluated not targeted,
and the ranking share under two definitions. Output: v2/out/financials.json"""
import json, collections
import load as L

P = json.load(open(L.OUT + 'product.json'))
D = json.load(open(L.OUT + 'decisions.json'))
f = P['family30']['Info']
sales, ads, net = f['Sales'], abs(f.get('Advertising') or 0), f['NetProfit']
comp = collections.defaultdict(lambda: collections.Counter())
for d in D['decisions']:
    if d['role'] == 'Other product (out of scope)':
        continue
    g = ('Ranking – push' if d['role'] == 'Ranking – push' else 'Ranking – maintain' if d['role'] == 'Ranking – maintain' else
         'LTSF clearance' if ('LTSF' in d['role'] or (d['role'] == 'Discovery / LTSF clearance' and (d['action']['child_to'] or d['child']) in
                                                       {s for v in D['ltsf_targets'].values() for s in v})) else
         'Brand defence' if d['role'] == 'Brand / listing defence' else 'Other non-ranking')
    x = comp[g]
    for k in ('d_spend_day', 'd_orders_day', 'd_sales_day', 'd_profit_day'):
        x[k] += d['checks'].get(k) or 0
    x['now_spend_day'] += d['now']['spend_day']
    x['plan_spend_day'] += d['plan']['spend_day']
    x['now_clicks_day'] += d['now']['clicks_day']
    x['plan_clicks_day'] += d['plan']['clicks_day']
tot = collections.Counter()
for x in comp.values():
    tot.update(x)
plan = dict(sales=sales + tot['d_sales_day'] * 30, ads=ads + tot['d_spend_day'] * 30, net=net + tot['d_profit_day'] * 30)
rk = comp['Ranking – push']['plan_spend_day'] + comp['Ranking – maintain']['plan_spend_day']
allsp = sum(x['plan_spend_day'] for x in comp.values())
growth = allsp - comp['LTSF clearance']['plan_spend_day'] - comp['Brand defence']['plan_spend_day']
rkc = comp['Ranking – push']['plan_clicks_day'] + comp['Ranking – maintain']['plan_clicks_day']
allc = sum(x['plan_clicks_day'] for x in comp.values())
OUT = dict(now=dict(sales=round(sales), ads=round(ads), net=round(net), tacos=round(ads / sales, 4), margin=round(net / sales, 4), units=f['Units'],
                    ppc_units=f.get('UnitsPPC'), organic_units=f.get('UnitsOrganic')),
           plan=dict(sales=round(plan['sales']), ads=round(plan['ads']), net=round(plan['net']), tacos=round(plan['ads'] / plan['sales'], 4),
                     margin=round(plan['net'] / plan['sales'], 4)),
           components={k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in comp.items()},
           share=dict(ranking_of_all_spend=round(rk / allsp, 3), ranking_of_keyword_growth_spend=round(rk / growth, 3), ranking_of_all_clicks=round(rkc / allc, 3),
                      ranking_spend_day=round(rk, 2), all_spend_day=round(allsp, 2), growth_spend_day=round(growth, 2),
                      nonranking_cap_for_80pct=round(rk / 0.8 - rk, 2), nonranking_cap_for_90pct=round(rk / 0.9 - rk, 2)),
           note='Direct ad effects only (30-day equivalent). Organic sales gained from better rank are not counted — they are the return the push is buying.')
json.dump(OUT, open(L.OUT + 'financials.json', 'w'), indent=1)
if __name__ == '__main__':
    print(json.dumps(OUT, indent=1))
