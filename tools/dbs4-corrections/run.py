import json,sys,re
sys.path.insert(0,'.')
from analysis import *
from findings import detect, detect_extra
ids=set(r['cid'] for r in ROWS if r['verdict']=='change' and r['kind'] in ('tos','bid','budget','pp','ros','state'))
for cid,c in CAMPS.items():
    if c['objective']=='Ranking' and c['status']=='ENABLED': ids.add(cid)
out=[]
for cid in ids:
    a=analyse(cid); j=judge(a)
    fm=None
    for r in a['rows']:
        m=re.search(r'carries (\d+) clicks in 90 days, under the 15-click read floor',r['text'])
        if m and int(m.group(1))>=15: fm=int(m.group(1))
    a['floor_misstated']=fm
    a.pop('rows')
    a['J']=j
    a['F']=detect_extra(a)+detect(a)
    for r in a['changes']: r.pop('text',None)
    out.append(a)
json.dump(out,open('analysis.json','w'),default=str)
from collections import Counter
print(len(out), Counter(f['code'] for a in out for f in a['F']))
