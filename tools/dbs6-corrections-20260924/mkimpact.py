import json,os
old=json.load(open('../b6run/impact.json'))
def L(n):
    p=f'placements_{n}.jsonl'
    return {json.loads(l)['campaignId']:json.loads(l) for l in open(p)} if os.path.exists(p) else {}
pre,post=L('pre0920'),L('post0920')
H=[json.loads(l) for l in open('decisions_hist.jsonl')]
cids={h['campaignId'] for h in H if h.get('decided')=='2026-09-20' and h.get('campaignId') and h.get('field') in ('bid','placement_multiplier','budget')}
def pd(r,days):
    if not r: return dict(sp=0,cl=0,tos=0,pp=0,od=0)
    p=r['placements'];return dict(sp=round((r['spend'] or 0)/days,2),cl=(r['clicks'] or 0)/days,tos=((p.get('tos') or {}).get('clicks') or 0)/days,pp=((p.get('detail') or {}).get('clicks') or 0)/days,od=(r['orders'] or 0)/days)
out=[]
if pre and post:
    for c in cids:
        r=pre.get(c) or post.get(c)
        out.append(dict(cid=c,nm=r['campaignName'] if r else c,ob=r['objective'] if r else 'UNSET',a=pd(pre.get(c),3),b=pd(post.get(c),3)))
json.dump({'2026-09-16':old['2026-09-16'],'2026-09-20':out},open('impact.json','w')); print(len(cids),len(out))
