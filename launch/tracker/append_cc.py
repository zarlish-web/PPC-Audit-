"""Replace/append command-center days in daily_campaigns.csv, daily_search_terms.csv and daily_ranks.csv.
Usage: python3 -I append_cc.py <scratchpad> <date> [<date> ...]   (reads v8/raw/camp_<date>.json, kw_<date>.json if present, ranks_kw.json)"""
import json, os, sys
import pandas as pd
S = sys.argv[1]; V = f'{S}/v8'; days = sys.argv[2:]
c = pd.read_csv(f'{V}/daily_campaigns.csv', dtype={'campaignId': str}); c = c[~c.date.isin(days)]
add = []
for d in days:
    for x in json.load(open(f'{V}/raw/camp_{d}.json'))['rows']:
        add.append(dict(date=d, campaignId=x['campaignId'], campaignName=x['campaignName'], objective=x['objective'], targetType=x['targetType'], matchType=x['matchType'],
                        impressions=x['impressions'], clicks=x['clicks'], orders=x['orders'], spend=x['spend'], sales=x['sales']))
c = pd.concat([c, pd.DataFrame(add)]).sort_values(['date']); c.to_csv(f'{V}/daily_campaigns.csv', index=False); print('campaigns rows', len(c))
st = pd.read_csv(f'{V}/daily_search_terms.csv'); kd = [d for d in days if os.path.exists(f'{V}/raw/kw_{d}.json')]; st = st[~st.date.isin(kd)]
add = []
for d in kd:
    for x in json.load(open(f'{V}/raw/kw_{d}.json'))['rows']:
        add.append(dict(date=d, term=x['keyword'], relevancy=x.get('relevancy'), searchVolume=x.get('searchVolume'), impressions=x['impressions'], clicks=x['clicks'],
                        orders=x['orders'], spend=x['spend'], sales=x['sales'], rank=x.get('rank'), syntax=x.get('syntax')))
st = pd.concat([st, pd.DataFrame(add)]).sort_values('date'); st.to_csv(f'{V}/daily_search_terms.csv', index=False); print('terms rows', len(st))
rk = pd.read_csv(f'{V}/daily_ranks.csv'); sv = rk.groupby('keyword').searchVolume_mkl.first().to_dict()
rows = []
for r in json.load(open(f'{V}/raw/ranks_kw.json'))['rows']:
    for cell in r['cells']:
        rows.append(dict(keyword=r['keyword'], date=cell['date'], organic_rank=cell.get('rank'), rank_state=cell.get('state'), sponsored_rank=None, searchVolume_mkl=sv.get(r['keyword'])))
new = pd.DataFrame(rows); keep = rk[~rk.set_index(['keyword', 'date']).index.isin(new.set_index(['keyword', 'date']).index)]
rk = pd.concat([keep, new]).sort_values(['keyword', 'date']); rk.to_csv(f'{V}/daily_ranks.csv', index=False); print('ranks rows', len(rk), 'latest', rk.date.max())
