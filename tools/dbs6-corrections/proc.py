import json,sys,os
f,label=sys.argv[1],sys.argv[2]
S=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(f))
out=os.path.join(S,f'placements_{label}.jsonl')
log=os.path.join(S,f'placements_{label}.offsets')
done=set(open(log).read().split()) if os.path.exists(log) else set()
if str(d['offset']) in done:
    print('offset already done',d['offset']);sys.exit()
keys=['campaignId','campaignName','objective','matchType','syntax','impressions','clicks','orders','spend','sales','acos','cpc']
with open(out,'a') as o:
    for r in d['rows']:
        c={k:r.get(k) for k in keys}
        pl={}
        for pk,pv in (r.get('placements') or {}).items():
            if not isinstance(pv,dict): continue
            p={k:pv.get(k) for k in ['impressions','clicks','cvr','cpc','spendShare']}
            if p['cvr'] is not None and p['clicks'] is not None:
                p['orders']=round(p['clicks']*p['cvr']/100)
            pl[pk]=p
        c['placements']=pl
        o.write(json.dumps(c,separators=(',',':'))+'\n')
open(log,'a').write(f"{d['offset']}\n")
print(label,d['window'],'total',d['total'],'offset',d['offset'],'returned',d['returned'],'lines',sum(1 for _ in open(out)))
