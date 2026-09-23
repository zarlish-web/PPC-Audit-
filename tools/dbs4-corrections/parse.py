import json,re
d=json.load(open('slim.json'))
def f(p,t,cast=float):
    m=re.search(p,t,re.S)
    if not m: return None
    g=m.group(1).replace(',','')
    try: return cast(g)
    except: return g
rows=[]
for x in d['decisions']+d['considered']:
    if x['kind'] not in ('tos','bid','budget','pp','ros','state'): continue
    R={r['label']:r['text'] for r in (x.get('rationale') or [])}
    t=' '.join(R.values())
    r=dict(seq=x['seq'],kind=x['kind'],verdict=x['verdict'],cid=x['campaign_id'],camp=x['campaign'],entity=x['entity'],
      now=x['current_at_audit'],to=x['suggested'],rule=x.get('rule'),source=x.get('source'),riskier=x.get('riskier'),
      pred=x.get('prediction'),claim=x.get('rank_claim'),dist=x.get('rank_distance'),obj=x.get('objective'),focus=x.get('focus'))
    r['withheld']=('change → HOLD' in t)
    r['tos_clk90']=f(r'READ AT TOP OF SEARCH \((\d[\d,]*) clicks',t,int)
    r['tos_imp90']=f(r'READ AT TOP OF SEARCH \(\d[\d,]* clicks / (\d[\d,]*) impressions',t,int)
    r['tos_is']=f(r'TOS share ([\d.]+)%',t)
    r['tos_cvr']=f(r'CVR ([\d.]+)% vs bar',t)
    r['mkt_cvr']=f(r'Market from SQP[^:]*: CTR [\d.]+% / CVR ([\d.]+)%',t)
    r['mkt_ctr']=f(r'Market from SQP[^:]*: CTR ([\d.]+)%',t)
    r['tos_ctr']=f(r'READ AT TOP OF SEARCH[^:]*:[^.]*?CTR ([\d.]+)%',t)
    r['rank_now']=f(r'rank (\d+) now',t,int); r['rank_tgt']=f(r'→ target (\d+) by',t,int)
    r['kw']=f(r'\[TARGET\]|^"([^"]+)" on',R.get('TARGET',''),str) if 0 else f(r'^"([^"]+)" on',R.get('TARGET',''),str)
    r['plan_ppc_wk']=f(r'leaves PPC ([\d.]+) clicks/wk',t)
    r['deliv_wk']=f(r'delivers ([\d.]+) top-of-search clicks/wk on the term',t)
    r['mix']=f(r'(top of search \d+% \(\d+\), product pages \d+% \(\d+\), rest of search \d+% \(\d+\))',t,str)
    m=re.search(r'mix (RIGHT|WRONG) \(top of search (\d+)%, product pages (\d+)%\)',t)
    if m: r['mix2']=m.group(0)
    r['p_tos']=f(r'Top of search \$([\d.]+) against',R.get('PRICES',''))
    r['p_pp']=f(r'against \$([\d.]+) on product pages',R.get('PRICES',''))
    r['cpo']=f(r'= \$([\d.]+) against \$[\d.]+ contribution per order',R.get('PRICES',''))
    r['contrib']=f(r'against \$([\d.]+) contribution per order',R.get('PRICES','')) or f(r'against \$([\d.]+) contribution per order',t)
    r['loss']=f(r'LOSS of \$([\d.]+) per order',R.get('PRICES',''))
    r['bound']=f(r'Bound: ([^.]+)\.',R.get('PRICES',''),str)
    r['mkt_clear']=f(r'top of search clears at \$([\d.]+)',R.get('PRICES',''))
    r['mkt_bound']=f(r'the bound is \$([\d.]+)',R.get('PRICES',''))
    r['spend_day']=f(r'spends \$([\d.]+) of a \$[\d.]+ daily budget',t)
    r['budget']=f(r'spends \$[\d.]+ of a \$([\d.]+) daily budget',t)
    r['budget_bound']=('NOT budget-bound' not in t) if 'budget-bound' in t else None
    r['stock']=f(r'STOCK CHECKPOINT[^:]*: ([^—]+)',t,str)
    r['pick']=f(r"file's pick \((\w+)\)",t,str)
    r['focus_out']=('FOCUS: OUT' in t)
    r['press']=f(r'THE CERTAIN-WIN PRESS\] (\w+)',' '.join('['+k+'] '+v for k,v in R.items()),str)
    r['decision']=R.get('DECISION','')[:600]
    r['engine']=R.get('ENGINE DECISION','')[:600]
    r['text']=t
    rows.append(r)
json.dump(rows,open('rows.json','w'))
print(len(rows))
