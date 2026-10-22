import pandas as pd, sys, re
src, out = sys.argv[1], sys.argv[2]
d = pd.read_excel(src, sheet_name='Sponsored Products Campaigns', dtype=str)
for c in ['Impressions','Clicks','Spend','Sales','Orders','Units']:
    d[c] = pd.to_numeric(d[c], errors='coerce').fillna(0)
d['camp'] = d['Campaign name (Informational only)'].fillna(d['Campaign name'])
# other campaigns advertising cooling-sheet SKUs outside CLCS4
pa = d[d.Entity == 'Product ad']
other = pa[pa.SKU.str.startswith('CL-COOLING-SHEET', na=False) & ~pa.camp.str.contains('CLCS4', na=False)]
print('cooling-sheet product ads outside CLCS4:', other[['camp','SKU','State','Spend']].to_string())
c = d[d.camp.str.contains('CLCS4', na=False)].copy()
camps = c[c.Entity == 'Campaign'].set_index('Campaign ID').rename(columns={'Campaign name': 'cname', 'Daily budget': 'budget'})
camps['Campaign name'] = camps.cname
def objective(n):
    m = re.search(r'\((Ranking|Conversion|Discovery|Conquest|Defensive)\)', n)
    return m.group(1) if m else ''
def size(n):
    m = re.search(r'\[Cooling\|(Queen|King|Full|Twin|California King)\]', n) or re.search(r'Rivals (Queen|King|Full|Twin)', n)
    return m.group(1).replace('California King', 'Cal King') if m else 'No size'
camps['objective'] = camps['Campaign name'].map(objective)
camps['size'] = camps['Campaign name'].map(size)
camps['role'] = camps.objective.map(lambda o: 'Ranking' if o == 'Ranking' else 'Halo')
ads = c[c.Entity == 'Product ad'].drop(columns=['Campaign name', 'Daily budget']).copy()
ads['colour'] = ads.SKU.str.replace(r'^CL-COOLING-SHEET-', '', regex=True)
ads = ads.join(camps[['Campaign name', 'objective', 'size', 'role']], on='Campaign ID')
ads['live'] = (ads.State == 'enabled') & (ads['Campaign state (Informational only)'] == 'enabled') & (ads['Ad group state (Informational only)'] == 'enabled')
kw = c[c.Entity == 'Keyword'].drop(columns=['Campaign name']).join(camps[['Campaign name', 'role', 'size']], on='Campaign ID')
agc = c[c.Entity == 'Ad group'].groupby('Campaign ID').size()
print('campaigns', len(camps), 'ad groups', int(agc.sum()), 'max ad groups per campaign', int(agc.max()))
print('campaign states', camps.State.value_counts().to_dict())
print('product ad states', ads.State.value_counts().to_dict(), 'eligibility', ads['Eligibility status (Informational only)'].value_counts().to_dict())
summ = ads.groupby('Campaign ID').agg(
    n_ads=('SKU', 'size'), n_enabled=('live', 'sum'),
    enabled_skus=('colour', lambda s: ', '.join(s[ads.loc[s.index, 'live']])),
    paused_skus=('colour', lambda s: ', '.join(s[~ads.loc[s.index, 'live']])),
    skus_with_spend=('Spend', lambda s: int((s > 0).sum())),
    spend=('Spend', 'sum'), clicks=('Clicks', 'sum'), orders=('Orders', 'sum'), sales=('Sales', 'sum'))
summ = camps[['Campaign name', 'objective', 'role', 'size', 'State', 'budget']].join(summ)
kws = kw[kw.State == 'enabled'].groupby('Campaign ID').apply(lambda g: ' | '.join(g['Keyword text'] + ' [' + g['Match type'] + ']'), include_groups=False)
summ['keywords'] = kws
summ['n_keywords'] = kw[kw.State == 'enabled'].groupby('Campaign ID').size()
summ.to_csv(f'{out}_campaigns.csv')
ads[['size', 'role', 'objective', 'Campaign name', 'Ad group name (Informational only)', 'SKU', 'ASIN (Informational only)', 'State', 'live', 'Eligibility status (Informational only)', 'Impressions', 'Clicks', 'Spend', 'Orders', 'Sales']].to_csv(f'{out}_ads.csv', index=False)
kw[['role', 'size', 'Campaign name', 'Keyword text', 'Match type', 'State', 'Bid', 'Impressions', 'Clicks', 'Spend', 'Orders']].to_csv(f'{out}_keywords.csv', index=False)
neg = c[c.Entity.isin(['Campaign negative keyword', 'Negative keyword'])].drop(columns=['Campaign name']).join(camps[['Campaign name', 'role']], on='Campaign ID')
neg[['role', 'Campaign name', 'Entity', 'Keyword text', 'Match type', 'State']].to_csv(f'{out}_negatives.csv', index=False)
print('total CLCS4 SP spend', round(ads.Spend.sum(), 2))
