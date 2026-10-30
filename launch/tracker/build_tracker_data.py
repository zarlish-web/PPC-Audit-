"""Build the CooLinens Launch Tracker datasets (JSON row files) from the pulled sources.

Usage: python3 -I build_tracker_data.py <scratchpad>
Writes v8/dash/data/*.json. Text content (overlap, decisions, log) comes from v8/tracker_text.json.
"""
import json, os, re, sys
from math import comb
import pandas as pd

S = sys.argv[1]
V = f'{S}/v8'
OUT = f'{V}/dash/data'
os.makedirs(OUT, exist_ok=True)
P_EXP = 0.088  # plan Batch 1 expected CVR (blended)
BE = 0.437


def n(k):
    k = re.sub(r'\s+', ' ', str(k).lower().strip())
    return ' '.join(re.sub(r'(sheet|bedsheet|sleeper|pocket|set|sweat|bed|flash|pillowcase)s$', r'\1', w) for w in k.split())


def p_le(k, nn, p=P_EXP):
    return sum(comb(nn, i) * p ** i * (1 - p) ** (nn - i) for i in range(int(k) + 1))


def clean(v):
    if isinstance(v, float) and (pd.isna(v) or v in (float('inf'), float('-inf'))):
        return None
    return v


def dump(name, df):
    rows = [{k: clean(v) for k, v in r.items()} for r in df.to_dict('records')]
    json.dump(rows, open(f'{OUT}/{name}.json', 'w'), indent=0, default=str)
    print(name, len(rows))


# ---------------------------------------------------------------- daily
sb = pd.read_csv(f'{V}/sb_daily.csv')
ppc = pd.read_csv(f'{V}/sb_ppc_daily.csv').set_index('date')
cc = pd.read_csv(f'{V}/ppc_daily.csv').set_index('date')
T = json.load(open(f'{V}/tracker_text.json'))
notes = T['day_notes']
allr = sb[sb.scope == 'All'].set_index('date')
rows = []
for dt, r in allr.iterrows():
    pre = dt < '2026-10-16'
    if dt in ppc.index:
        a = ppc.loc[dt]; spend, impr, clk, orders, adsales = a.ad_spend, a.impressions, a.clicks, a.ad_orders, a.ad_sales
    elif not pre and dt in cc.index:  # Sellerboard not ingested yet: SP only from the command center
        a = cc.loc[dt]; spend, impr, clk, orders, adsales = r.ad_spend_alloc, a.impressions, a.clicks, a.orders, a.sales
    else:  # no campaign-level ad data yet (e.g. today's partial day): all-type spend from the profit dashboard
        impr = clk = orders = adsales = 0
        spend = 0 if pre else float(r.ad_spend_alloc)
    complete = 'no' if dt == T['partial_day'] else 'yes'
    rows.append(dict(date=dt, phase='Before ads' if pre else 'Ads live', complete=complete, units=int(r.units), sales=float(r.sales),
                     sessions=None if pd.isna(r.sessions) else int(r.sessions), ad_spend=float(spend), ad_impressions=int(impr), ad_clicks=int(clk),
                     ctr=(clk / impr) if impr else None, cpc=(spend / clk) if clk else None, ad_orders=int(orders), cvr=(orders / clk) if clk else None,
                     ad_sales=float(adsales), acos=(spend / adsales) if adsales else None, tacos=(spend / r.sales) if r.sales else None,
                     non_ad_units=int(r.units - orders), note=notes.get(dt, '')))
daily = pd.DataFrame(rows)
dump('daily', daily)

# ---------------------------------------------------------------- size_daily
camp = pd.read_csv(f'{V}/daily_campaigns.csv'); camp = camp[camp.campaignName.str.startswith('CLCS4')]
def size(nm):
    m = re.search(r'\[Cooling\|(Queen|King|Full|Twin|California King)\]', nm) or re.search(r'Rivals (Queen|King|Full|Twin|California King)', nm)
    return m.group(1).replace('California King', 'Cal King') if m else 'No size / head'
camp['size'] = camp.campaignName.map(size)
spc = camp.groupby(['date', 'size'])[['clicks', 'orders', 'spend']].sum()
srows = []
for _, r in sb[sb.scope != 'All'].iterrows():
    k = (r.date, r.scope)
    c = spc.loc[k] if k in spc.index else None
    srows.append(dict(date=r.date, size=r.scope, phase='Before ads' if r.date < '2026-10-16' else 'Ads live', units=int(r.units), ad_spend=float(r.ad_spend_alloc),
                      sp_clicks=int(c.clicks) if c is not None else 0, sp_orders=int(c.orders) if c is not None else 0, sp_spend=float(c.spend) if c is not None else 0.0))
for dt in sorted(set(camp.date)):
    k = (dt, 'No size / head')
    if k in spc.index:
        c = spc.loc[k]
        srows.append(dict(date=dt, size='No size / head', phase='Ads live', units=None, ad_spend=None, sp_clicks=int(c.clicks), sp_orders=int(c.orders), sp_spend=float(c.spend)))
dump('size_daily', pd.DataFrame(srows).sort_values(['date', 'size']))

# ---------------------------------------------------------------- terms
st = pd.read_csv(f'{V}/daily_search_terms.csv')
d = json.load(open(f'{S}/v4/data.json'))
M = pd.DataFrame(d['main']['rows'], columns=d['main']['cols'])
M = M.assign(nk=M.Keyword.map(n)).sort_values(['Batch', 'Search Volume / Month (Launch Window)'], ascending=[True, False]).drop_duplicates('nk')
pb = dict(zip(M.nk, M.Batch))
E = pd.DataFrame(d['excluded']['rows'], columns=d['excluded']['cols']); ex = set(E.Keyword.map(n))
last_rank = st.dropna(subset=['rank']).sort_values('date').groupby('term')['rank'].last()
g = st.groupby('term')[['clicks', 'orders', 'spend', 'sales']].sum().reset_index()
g['acos'] = g.spend / g.sales.replace(0, float('nan'))
g['rank'] = g.term.map(last_rank).map(lambda v: None if pd.isna(v) else str(v))
g['plan'] = g.term.map(lambda t: f'Batch {pb[n(t)]}' if n(t) in pb else 'Excluded' if n(t) in ex else 'Not in plan')
def read(r):
    if r.orders > 0 and (r.acos or 9) <= BE:
        return 'Working'
    if r.orders > 0:
        return f'Watch — ACoS {r.acos:.0%}'
    p0 = p_le(0, int(r.clicks))
    if p0 >= 0.05:
        return f'Too early — 0 orders on {int(r.clicks)} clicks happens {p0:.0%} of the time'
    return f'Problem — 0 orders on {int(r.clicks)} clicks ({p0:.0%} chance)'
g['read'] = g.apply(read, axis=1)
q = g[g.term.str.contains(r'\bqueen\b')].sort_values('spend', ascending=False)
k = g[g.term.str.contains(r'\bking\b') & ~g.term.str.contains(r'cal king|california')].sort_values('spend', ascending=False)
cols = ['term', 'plan', 'clicks', 'orders', 'spend', 'sales', 'acos', 'rank', 'read']
dump('queen_terms', q[cols]); dump('king_terms', k[cols])

# ---------------------------------------------------------------- queen campaigns
sc = pd.read_csv(f'{S}/v6/sb_campaigns.csv'); sc = sc[sc.Name.str.startswith('CLCS4') & sc.Name.str.contains('Queen')]
for c_ in ['AdSpend', 'Clicks', 'Orders', 'Impressions', 'dailyBudget', 'topOfSearch', 'startDate']:
    sc[c_] = pd.to_numeric(sc[c_], errors='coerce').abs()
END = pd.Timestamp('2026-10-30 13:00', tz='UTC').timestamp()
sc['days'] = ((END - sc.startDate) / 86400).clip(lower=1)
sc['budget_used'] = sc.AdSpend / (sc.dailyBudget * sc.days)
sc['objective'] = sc.Name.str.extract(r'-\((Ranking|Conversion|Conquest|Profit)\)-')[0] + sc.Name.map(lambda x: ' · fixed bids' if '-FIX-' in x else ' · down-only bids')
reads = T['queen_campaign_reads']
qc = pd.DataFrame(dict(campaign=sc.Name.str.replace(r'-CL-COOLING-SHEET.*|-CL69-.*', '', regex=True), objective=sc.objective, budget=sc.dailyBudget,
                       budget_used=sc.budget_used, tos_share=sc.topOfSearch / 100, impressions=sc.Impressions, clicks=sc.Clicks, orders=sc.Orders, spend=sc.AdSpend))
qc['read'] = qc.campaign.map(lambda c_: next((v for kk, v in reads.items() if kk in c_), ''))
dump('queen_campaigns', qc.sort_values('spend', ascending=False))

# ---------------------------------------------------------------- ranks (wide)
rk_long = f'{V}/daily_ranks.csv'
tgt = dict(zip(M.Keyword.map(n), M['Target Organic Rank (#)']))
if os.path.exists(rk_long):
    r = pd.read_csv(rk_long)
    r['kw'] = r.keyword
    r['date'] = r.date.astype(str).str.slice(0, 10)
    r = r[r.date >= '2026-10-15']
    r['val'] = r.apply(lambda x: '' if x.rank_state == 'not-crawled' else ('NR' if x.rank_state == 'unranked' or pd.isna(x.organic_rank) else f'#{int(x.organic_rank)}'), axis=1)
    wide = r.pivot_table(index='kw', columns='date', values='val', aggfunc='first')
    wide = wide.reindex(sorted(set(r.kw)))
else:
    rr = pd.read_csv(f'{V}/../v6/ranks.csv'); rr = rr[rr.tracked == 'yes']
    wide = rr.set_index('keyword')[['rank_15_16', 'r18', 'r19', 'r20']]
    wide.columns = ['2026-10-16', '2026-10-18', '2026-10-19', '2026-10-20']
wide = wide.reset_index().rename(columns={'kw': 'keyword', 'index': 'keyword'})
wide['size'] = wide.keyword.map(lambda t: 'Queen' if 'queen' in t else 'Cal King' if re.search('cal king|california', t) else 'King' if 'king' in t else 'Full' if 'full' in t else 'Twin' if 'twin' in t else 'No size')
wide['plan'] = wide.keyword.map(lambda t: f'Batch {pb[n(t)]}' if n(t) in pb else 'Excluded' if n(t) in ex else 'Not in plan')
wide['target_rank'] = wide.keyword.map(lambda t: tgt.get(n(t)))
datecols = [c_ for c_ in wide.columns if re.match(r'\d{4}-\d{2}-\d{2}', str(c_))]
for c_ in (datecols if not os.path.exists(rk_long) else []):
    wide[c_] = wide[c_].map(lambda v: 'NR' if pd.isna(v) or str(v).strip() in ('', 'None', 'nan', 'NR') else f'#{int(float(v))}')
wide = wide[['keyword', 'size', 'plan', 'target_rank'] + datecols]
wide = wide[wide['plan'].str.startswith('Batch')]
dump('ranks', wide.sort_values(['size', 'keyword']))

# ---------------------------------------------------------------- stock
inv = pd.read_csv(f'{S}/v5/inv_now.csv')
m = inv.SKU.str.extract(r'CL-COOLING-SHEET-(CAL-KING|QUEEN|KING|FULL|TWIN)-(.+)')
inv['size'] = m[0].map({'QUEEN': 'Queen', 'KING': 'King', 'FULL': 'Full', 'TWIN': 'Twin', 'CAL-KING': 'Cal King'}); inv['colour'] = m[1].str.replace('-', ' ').str.title()
PUSH = {'Queen': 1.20, 'King': 1.14, 'Full': 0.54, 'Twin': 0.27, 'Cal King': 0.34}
ROLE = T['stock_roles']
rows = []
for _, r in inv.iterrows():
    role = ROLE.get(r.SKU, '')
    if r['size'] != 'Queen' and not role:
        continue
    push = PUSH[r['size']] if role.startswith('Ad SKU') else 0.0
    vel = float(r.Vel or 0); dem = vel + push
    cover = (r.FBA / dem) if dem > 0 else None
    status = 'OK' if (cover is None or cover >= 90) else 'Watch' if cover >= 21 else 'Switch to backup'
    rows.append(dict(size=r['size'], colour=r.colour, sku=r.SKU, role=role or 'Not advertised', fba=int(r.FBA), sales_day=vel, push_orders_day=push, cover_days_push=cover, status=status))
dump('stock', pd.DataFrame(rows).sort_values(['size', 'fba'], ascending=[True, False]))


# ---------------------------------------------------------------- sizes (all live sizes) and proposed actions
scs = pd.read_csv(f'{S}/v6/sb_campaigns.csv'); scs = scs[scs.Name.str.startswith('CLCS4')]
for c_ in ['AdSpend', 'Clicks', 'Orders', 'Sales']:
    scs[c_] = pd.to_numeric(scs[c_], errors='coerce').abs()
scs['size'] = scs.Name.map(size).replace({'No size / head': 'No size / head terms'})
ads_days = daily[(daily.phase == 'Ads live') & (daily.complete == 'yes') & (daily.ad_impressions > 0)].shape[0] or 1
zrows = []
for z in T['sizes']:
    x = scs[scs['size'] == z['size']]
    sp, sa, cl, od = x.AdSpend.sum(), x.Sales.sum(), x.Clicks.sum(), x.Orders.sum()
    u = sb[sb.scope == z['size']]
    pre = u[u.date < '2026-10-16'].units.mean() if len(u) else None
    post = u[(u.date >= '2026-10-16') & (u.date <= daily[daily.complete == 'yes'].date.max())].units.mean() if len(u) else None
    zrows.append(dict(size=z['size'], campaigns=z['campaigns'], ad_sku_live=z['ad_sku_live'], ad_sku_recommended=z['ad_sku_recommended'],
                      ad_spend=sp, spend_day=sp / ads_days, plan_spend_day=z['plan_spend_day'], ad_clicks=cl, ad_orders=od, ad_sales=sa,
                      acos=(sp / sa) if sa else None, cvr=(od / cl) if cl else None, units_day_before=pre, units_day_after=post,
                      plan_light_push_day=z.get('plan_light_push_day'), plan_light_share=z.get('plan_light_share'), rank_note=z['rank_note'], read=z['read']))
dump('sizes', pd.DataFrame(zrows))
dump('actions', pd.DataFrame(T['actions']))

# ---------------------------------------------------------------- overlap, decisions, log
dump('overlap', pd.DataFrame(T['overlap']))
dump('decisions', pd.DataFrame(T['decisions']))
log = pd.DataFrame(T['log'])
for c_ in ['results', 'observations', 'actions', 'reasoning', 'followups']:
    if c_ in log:
        log[c_] = log[c_].map(lambda v: '\n'.join(v) if isinstance(v, list) else v)
dump('log', log)
