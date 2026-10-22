"""Build the full report for one complete day and add it to v8/dash/data/day_reports.json.

Usage: python3 -I build_day_report.py <scratchpad> <YYYY-MM-DD>

Reads v8/day/<date>/ (written by the daily run from Sellerboard and the command center):
  profit.csv     date,scope,units,sales,product_costs,amazon_fees,ad_spend,sp,sb,sbv,sd,net_profit,sessions
                 one row per scope (All, Queen, King, Full, Twin, Cal King) for the day, plus an All row for the day before
  campaigns.tsv  id,name,type,budget,impressions,clicks,orders,spend,sales   every CLCS4 campaign with activity that day
  terms.tsv      term,impressions,clicks,orders,spend,sales (no header)      every search term that day
  ranks.csv      keyword,<day before>,<day>,<day after>                       organic rank; NR = not ranked
  notes.json     ["point to note", ...]                                       written by the analyst
Also reads v8/sb_ppc_daily.csv for the day and the day before (impressions, clicks, orders, ad sales).
The newest report is shown at the top of the tracker; older ones stay selectable.
"""
import csv, json, os, re, sys
import pandas as pd

S, DAY = sys.argv[1], sys.argv[2]
V = f'{S}/v8'
IN = f'{V}/day/{DAY}'
OUT = f'{V}/dash/data/day_reports.json'
BE = 0.391  # break-even ACoS after refunds (plan)

prof = pd.read_csv(f'{IN}/profit.csv')
prev_date = prof[prof.date != DAY].date.max()
cur = prof[(prof.date == DAY) & (prof.scope == 'All')].iloc[0]
prv = prof[(prof.date == prev_date) & (prof.scope == 'All')].iloc[0]
ppc = pd.read_csv(f'{V}/sb_ppc_daily.csv').set_index('date')
pc, pp = ppc.loc[DAY], ppc.loc[prev_date]

camp = pd.read_csv(f'{IN}/campaigns.tsv', sep='\t', dtype={'id': str})
assert abs(camp.spend.sum() - pc.ad_spend) < 0.05, ('campaign rows do not add up to the day total', camp.spend.sum(), pc.ad_spend)


def div(a, b):
    return (a / b) if b else None


def size(n):
    m = re.search(r'\[Cooling\|(Queen|King|Full|Twin|California King)\]', n) or re.search(r'Rivals (Queen|King|Full|Twin|Cal King)', n) or re.search(r'Video (Queen|King)', n)
    return m.group(1).replace('California King', 'Cal King') if m else 'No size'


def group(n, t):
    if 'Rivals' in n or 'Rival Pages' in n: return 'Ads on rival product pages'
    if 'Rival Video' in n: return 'Rival-product videos'
    if t == 'sb': return 'SB collections'
    if t == 'sbv': return 'SBV keyword videos'
    if '-Auto-' in n: return 'Auto'
    if 'Pillowcases' in n or 'Own Pages' in n: return 'Own-page defence'
    if '(Ranking)' in n: return 'SP ranking keywords'
    if 'Tail' in n: return 'SP long-tail keywords'
    return 'SP conversion keywords (main terms)'


TYPES = {'sp': 'Sponsored Products', 'sb': 'Sponsored Brands (collections)', 'sbv': 'Sponsored Brands Video', 'sd': 'Sponsored Display'}
camp['size'] = camp.name.map(size)
camp['group'] = [group(n, t) for n, t in zip(camp.name, camp.type)]
camp['campaign'] = camp.name.str.replace(r'^CLCS4-', '', regex=True).str.replace(r'-\[.*|-\(PAT\).*|-\(Contextual\).*', '', regex=True).str.replace(r'-Auto$', ' Auto', regex=True)
camp.loc[camp.name.str.contains('-Auto-'), 'campaign'] = 'SP-Auto'


def agg(by, label):
    g = camp.groupby(by)[['impressions', 'clicks', 'orders', 'spend', 'sales']].sum().reset_index().rename(columns={by: label})
    g['ctr'] = [div(c, i) for c, i in zip(g.clicks, g.impressions)]
    g['cpc'] = [div(s, c) for s, c in zip(g.spend, g.clicks)]
    g['cvr'] = [div(o, c) for o, c in zip(g.orders, g.clicks)]
    g['acos'] = [div(s, a) for s, a in zip(g.spend, g.sales)]
    return g.sort_values('spend', ascending=False)


types = agg('type', 'type'); types['type'] = types['type'].map(TYPES)
groups = agg('group', 'group')
csz = agg('size', 'size').set_index('size')
sizes = []
for _, r in prof[(prof.date == DAY) & (prof.scope != 'All')].iterrows():
    k = 'Cal King' if r.scope == 'Cal King' else r.scope
    c = csz.loc[k] if k in csz.index else None
    sizes.append(dict(size=r.scope, units=int(r.units), sales=float(r.sales), ad_spend=float(r.ad_spend), net_profit=float(r.net_profit),
                      camp_spend=float(c.spend) if c is not None else 0.0, camp_clicks=int(c.clicks) if c is not None else 0,
                      camp_orders=int(c.orders) if c is not None else 0, camp_acos=None if c is None or pd.isna(c.acos) else float(c.acos)))
if 'No size' in csz.index:
    c = csz.loc['No size']
    sizes.append(dict(size='No size (main terms)', units=None, sales=None, ad_spend=None, net_profit=None,
                      camp_spend=float(c.spend), camp_clicks=int(c.clicks), camp_orders=int(c.orders), camp_acos=None if pd.isna(c.acos) else float(c.acos)))

camp['budget_used'] = [div(s, b) for s, b in zip(camp.spend, camp.budget)]
camp['ctr'] = [div(c, i) for c, i in zip(camp.clicks, camp.impressions)]
camp['acos'] = [div(s, a) for s, a in zip(camp.spend, camp.sales)]


def flag(r):
    f = []
    if (r.budget_used or 0) >= 1: f.append('Budget-capped')
    if r.orders == 0 and r.spend >= 20: f.append('No orders')
    if r.acos is not None and r.acos <= BE: f.append('Profitable')
    return ' · '.join(f)


camp['flag'] = camp.apply(flag, axis=1)
camp['type'] = camp.type.str.upper()
campaigns = camp.sort_values('spend', ascending=False)[['campaign', 'type', 'size', 'group', 'budget', 'budget_used', 'impressions', 'clicks', 'ctr', 'orders', 'spend', 'sales', 'acos', 'flag']]

terms = pd.read_csv(f'{IN}/terms.tsv', sep='\t', header=None, names=['term', 'impressions', 'clicks', 'orders', 'spend', 'sales'])


def bucket(r):
    t = r.term.lower()
    if re.fullmatch(r'b0[a-z0-9]{8}', t): return 'Rival product page'
    if 'coolinens' in t: return 'Our brand'
    if 'sleephoria' in t: return 'Sister brand'
    if re.search(r'cool|cold|temperature', t) and re.search(r'sheet|bedding|bed set', t):
        return 'Converted' if r.orders > 0 else 'Relevant, no order yet'
    return 'Not a cooling-sheet search'


terms['bucket'] = terms.apply(bucket, axis=1)
terms['acos'] = [div(s, a) for s, a in zip(terms.spend, terms.sales)]
tb = terms.groupby('bucket')[['clicks', 'orders', 'spend', 'sales']].sum().reset_index()
tb['terms'] = terms.groupby('bucket').size().values
tb = tb.sort_values('spend', ascending=False)

rk = pd.read_csv(f'{IN}/ranks.csv', dtype=str).fillna('')
rank_dates = [c for c in rk.columns if c != 'keyword']
ranks = [dict(keyword=r.keyword, **{d: ('NR' if r[d] in ('NR', '', '0') else '#' + r[d]) for d in rank_dates}) for _, r in rk.iterrows()]

summary = []
def row(metric, a, b, fmt, better='up'):
    ch = div(a - b, abs(b)) if (a is not None and b not in (None, 0)) else None
    summary.append(dict(metric=metric, day=a, prev=b, change=ch, fmt=fmt, better=better))
row('Units', int(cur.units), int(prv.units), 'int')
row('Sales', float(cur.sales), float(prv.sales), 'money')
row('Ad spend (all types)', float(cur.ad_spend), float(prv.ad_spend), 'money', 'down')
row('Impressions', int(pc.impressions), int(pp.impressions), 'int')
row('Clicks', int(pc.clicks), int(pp.clicks), 'int')
row('CTR', pc.clicks / pc.impressions, pp.clicks / pp.impressions, 'pct')
row('CPC', pc.ad_spend / pc.clicks, pp.ad_spend / pp.clicks, 'money2', 'down')
row('Ad orders', int(pc.ad_orders), int(pp.ad_orders), 'int')
row('Ad conversion rate', pc.ad_orders / pc.clicks, pp.ad_orders / pp.clicks, 'pct')
row('Ad sales', float(pc.ad_sales), float(pp.ad_sales), 'money')
row('ACoS', pc.ad_spend / pc.ad_sales, pp.ad_spend / pp.ad_sales, 'pct', 'down')
row('TACoS (ads ÷ all sales)', cur.ad_spend / cur.sales, prv.ad_spend / prv.sales, 'pct', 'down')
row('Units without an ad order', int(cur.units - pc.ad_orders), int(prv.units - pp.ad_orders), 'int')
row('Net profit', float(cur.net_profit), float(prv.net_profit), 'money')

clean = lambda df: json.loads(df.to_json(orient='records'))
rep = dict(date=DAY, prev_date=prev_date,
           pnl=dict(sales=float(cur.sales), product_costs=float(cur.product_costs), amazon_fees=float(cur.amazon_fees), ad_spend=float(cur.ad_spend), net_profit=float(cur.net_profit)),
           summary=summary, types=clean(types), sizes=sizes, groups=clean(groups), campaigns=clean(campaigns),
           terms=clean(terms.sort_values(['spend', 'orders'], ascending=False)), term_buckets=clean(tb), rank_dates=rank_dates, ranks=ranks,
           notes=json.load(open(f'{IN}/notes.json')) if os.path.exists(f'{IN}/notes.json') else [],
           terms_cover=dict(spend=float(terms.spend.sum()), not_split=float(cur.ad_spend - terms.spend.sum())))
allr = json.load(open(OUT)) if os.path.exists(OUT) else []
allr = [r for r in allr if r['date'] != DAY] + [rep]
allr.sort(key=lambda r: r['date'], reverse=True)
json.dump(allr, open(OUT, 'w'), indent=0, default=str)
print('day_reports', [r['date'] for r in allr], 'campaigns', len(campaigns), 'terms', len(terms), 'spend', round(camp.spend.sum(), 2))
