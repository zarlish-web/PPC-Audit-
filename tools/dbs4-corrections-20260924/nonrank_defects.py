import json, re, os
S=os.path.dirname(os.path.abspath(__file__))
A=json.load(open(f'{S}/a.json')); BE=A['brief']['sections']['margin']['be_acos']
def L(n): return {json.loads(l)['campaignId']:json.loads(l) for l in open(f'{S}/placements_{n}.jsonl')}
D14,D90,D7=L('d14'),L('d90'),L('d7')
DEC={}
for x in A['decisions']:
    if x['kind'] in ('tos','bid','budget','pp','ros','state'): DEC.setdefault(x['campaign_id'],[]).append(x)
out=[]
for c in A['campaigns']:
    if c.get('status')!='ENABLED' or c['objective'] in ('Ranking','Sponsored Brands','Sponsored Display','UNSET'): continue
    a=D14.get(c['campaign_id'],{}); b=D90.get(c['campaign_id'],{})
    c14,o14,s14,sa14=a.get('clicks') or 0,a.get('orders') or 0,a.get('spend') or 0,a.get('sales') or 0
    if c14==0 and not DEC.get(c['campaign_id']): continue
    acos14=s14/sa14 if sa14 else None; acos90=(b.get('spend') or 0)/(b.get('sales') or 1) if b.get('sales') else None
    xs=DEC.get(c['campaign_id'],[])
    e=', '.join(f"{x['kind']} {x['current_at_audit']}→{x['suggested']}" for x in xs) or 'holds'
    cpc=s14/c14 if c14 else None
    if c['objective']=='Liquidation':
        v='Clearance economics — the LTSF lane sets its floor; flag if ACoS keeps rising' + (f' (14d {acos14:.0%})' if acos14 else '')
    elif c14<15:
        v='Thin (<15 clicks in 14 days) — hold; ' + ('reverse the TOS cut' if any(x['kind']=='tos' for x in xs) else 'no change')
    elif acos14 is None or acos14>BE*1.05:
        tgt=cpc*BE/acos14 if acos14 else cpc*0.75
        step=max(-0.5 if o14==0 else -0.25, tgt/cpc-1)
        v=f"Over its ceiling on 14 days — base down {-step:.0%} (CPC ${cpc:.2f} → ${cpc*(1+step):.2f})" + ('; 90 days was inside — drifting, read weekly' if (acos90 is not None and acos90<=BE) else '')
    else:
        v=('Inside its ceiling but drifting (ACoS ' + f"{acos90:.0%} over 90 days → {acos14:.0%} over 14" + ') — hold, read weekly' if (acos90 and acos14 > 1.5*acos90) else 'Inside its ceiling — hold') + ('; reverse the TOS modifier cut' if any(x['kind']=='tos' and float(x['suggested'])<float(x['current_at_audit']) for x in xs) else '')
    out.append(dict(short=c['campaign'].replace('DBS4-SP-',''),obj=c['objective'],c14=c14,o14=o14,s14=s14,acos14=acos14,acos90=acos90,eng=e,verdict=v))
out.sort(key=lambda n:-n['s14'])
json.dump(out,open(f'{S}/nonrank.json','w'))
print(len(out))
for n in out[:12]: print(n['short'][:50],n['c14'],n['acos14'],n['eng'][:40],'|',n['verdict'])
# ---- defects
rows=json.load(open(f'{S}/rows.json'))
ch=[r for r in rows if r['verdict']=='change' and r['kind'] in ('tos','bid','budget','pp','ros','state')]
wh=[r['seq'] for r in ch if r['withheld']]
reg=json.load(open(f'{S}/register.json'))
dup=[x['seq'] for x in reg if 'DUP' in x['codes'] and x['verdict']=='DROP']
noop=[x['seq'] for x in reg if 'NOOP' in x['codes']]
lab=[x['seq'] for x in reg if 'LABEL' in x['codes']]
H=[json.loads(l) for l in open(f'{S}/decisions_hist.jsonl')]
late={}
for h in H:
    if h['decided']>='2026-09-24' and h['field'] in ('bid','placement_multiplier','budget'):
        k=(h['campaignId'],'tos' if (h['field']=='placement_multiplier' and h.get('placement')=='placementTop') else 'pp' if h['field']=='placement_multiplier' and h.get('placement')=='placementProductPage' else 'ros' if h['field']=='placement_multiplier' else h['field'])
        late[k]=h
stale=[];stale_ex=[]
for r in ch:
    h=late.get((r['cid'],r['kind']))
    if h:
        stale.append(r['seq'])
        if len(stale_ex)<1: stale_ex.append(f"{r['seq']} proposes {r['now']} → {r['to']}; live is {h['after']} since {h['decided']}")
bud=[];cap=[];nocap=[]
for x in A['decisions']:
    if x['kind']=='budget':
        s7=(D7.get(x['campaign_id'],{}).get('spend') or 0)/7; b0=float(x['current_at_audit']); u=s7/b0
        t=f"{x['seq']} ({x['campaign'].replace('DBS4-SP-','')[:34]}: ${s7:.2f}/day of ${b0:.2f} = {u:.0%})"
        (cap if u>=0.8 else nocap).append(t)
D=[f"**{len(wh)} rows the engine itself withholds** — their text says “change → HOLD” (no gradeable rank claim) but they export as changes: seq {', '.join(map(str,wh)) or 'none'}."]
if stale: D.append(f"**{len(stale)} rows overtaken by live changes after the audit** — the same lever was already moved after the audit, so these would write over a newer value: seq {', '.join(map(str,stale))} (e.g. {stale_ex[0]}).")
if cap or nocap: D.append(f"**Budget raises: keep {len(cap)}, drop {len(nocap)}.** On the last 7 days, these are running out of money and keep their raise: " + ('; '.join(cap) or 'none') + ". These are not, and the raise is dropped (price is the lever): " + ('; '.join(nocap) or 'none') + ".")
if noop or dup: D.append(f"**No-op and duplicate rows**: " + (f"seq {', '.join(map(str,noop))} change nothing (pause what is already paused or write today’s value)" if noop else '') + ('; ' if noop and dup else '') + (f"seq {', '.join(map(str,dup))} repeat a keyword already written" if dup else '') + ".")
if lab: D.append(f"**Rows labelled with the wrong keyword**: seq {', '.join(map(str,lab))} name the plan keyword but change a different target.")
CS={c['campaign_id']:c for c in A['campaigns']}
pz=[x['seq'] for x in A['decisions'] if x['verdict']=='change' and x['kind'] in ('tos','bid','ros','pp','budget') and CS.get(x['campaign_id'],{}).get('status')=='PAUSED']
if pz: D.append(f"**{len(pz)} writes on campaigns that are paused at the audit** — bids, modifiers and rest-of-search on campaigns that cannot serve: seq {', '.join(map(str,pz))}. Drop them; if a campaign is meant to come back, that is a state decision first.")
ms=[x for x in A['decisions'] if x['verdict']=='change' and x['kind'] in ('tos','bid','budget') and x.get('campaign_id') and x['campaign_id'] not in CS]
up=[x for x in ms if float(x['suggested'])>float(x['current_at_audit'])]; dn=[x for x in ms if x not in up]
_nc=len({x['campaign_id'] for x in up})
if ms: D.append(f"**{len(up)} raises on {_nc} campaigns the export does not carry** — new Bamboo|Cooling campaigns with no impressions in 90 days: bids +25% (seq {', '.join(str(x['seq']) for x in up if x['kind']=='bid')}), top-of-search modifiers (seq {', '.join(str(x['seq']) for x in up if x['kind']=='tos')}) and a budget ${' '.join(x['current_at_audit'] + ' → $' + x['suggested'] for x in up if x['kind']=='budget')} a day (seq {', '.join(str(x['seq']) for x in up if x['kind']=='budget')}). With no status, child or read in the export, hold them until each campaign’s status, child and targets are confirmed (operator 2026-09-25); once confirmed enabled and dark, they join the in-focus push under Part A. The {len(dn)} cuts on campaigns missing from the export (seq {', '.join(str(x['seq']) for x in dn)}) stand, flagged for the same check.")
D.append("**Negative walls written across products** — seq 2427 walls a DBS6 (6-piece) liquidation campaign and seq 2423 a DBS4 LTSF campaign from inside this ranking run. Both go to the LTSF owner; a run scoped to product 59 should not write to another product’s campaign.")
_ec=A['brief']['sections'].get('engine_check') or {}
if _ec.get('failed'): D.append(f"**{_ec['failed']} engine check failed** ({_ec.get('passed')} passed): " + '; '.join(_ec.get('failures') or []) + ". The campaign is out of focus; under the 25 September decision only the in-focus Queen White campaign is re-pointed, so this one is flagged and stays on the hero until stock lands.")
json.dump(D,open(f'{S}/defects.json','w'))
print('\n'.join(D))
