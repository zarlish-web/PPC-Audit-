import json, collections, os
OUT='/tmp/claude-0/-home-user-PPC-Audit-/51b9bd0e-5fdd-5e9c-87d4-612ed5188e17/scratchpad/dash/'
R=json.load(open('verify_results.json')); S=json.load(open('source/account_pulls_2026-11-02.json'))
C=collections.Counter((x['section'],x['status']) for x in R['checks'])
secs=sorted({x['section'] for x in R['checks']})
short={"1. Source records":"Source records","2. Product numbers":"Product numbers","3. Cross-source":"Cross-source","4. Workbook arithmetic":"Workbook arithmetic","5. Decisions and wording":"Decisions and wording","6. Is the demand read still current":"Demand still current"}
score=[{"section":short[s],"order":i+1,"ok":C[(s,'OK')],"check":C[(s,'CHECK')],"diff":C[(s,'DIFF')],"total":C[(s,'OK')]+C[(s,'CHECK')]+C[(s,'DIFF')]} for i,s in enumerate(secs)]
json.dump(score,open(OUT+'scorecard.json','w'))
p_by={(p["mkt"],p["name"]):p for p in R["products"]}
b4,b6=p_by[("US","Decolure Bamboo 4 Pc")],p_by[("US","Decolure Bamboo 6 Pc")]
alt_us=sum(p["alt_budget"] for p in R["products"] if p["mkt"]=="US"); alt_ca=sum(p["alt_budget"] for p in R["products"] if p["mkt"]=="CA")
src=open('build_verification_xlsx.py').read(); i=src.index("FIND = ["); j=src.index("\n]\n",i)
US_T,CA_T=R["totals"]["US"],R["totals"]["CA"]; CON=json.load(open('source/ads_console_sp_by_product_2026-10-19_to_11-01.json')); SRC=S
FIND=eval(src[i+7:j+2])
find=[{"n":k+1,"severity":f[0],"area":f[1],"finding":f[2],"impact":f[4],"action":f[5],"status":f[6]} for k,f in enumerate(FIND)]
json.dump(find,open(OUT+'findings.json','w'))
plan_b={(x['mkt'],x['product']):x['plan'] for x in R['checks'] if x['item']=='Ad budget Nov 19-30'}
prods=[]
for p in R['products']:
    m=p['mkt']
    prods.append({"key":f"{m} · {p['name']}","market":m,"product":p['name'],"stage":p['stage'],"deal":p['deal'] or "No deal",
      "budget_plan":round(plan_b[(m,p['name'])],2),"budget_rebuilt":round(p['budget'],2),"gap":round(plan_b[(m,p['name'])]-p['budget'],2),
      "plan_tacos":round(p['plan_t'],4),"tacos_now":None if p['now'] is None else round(p['now'],4),"cap":None if p['cap'] is None else round(p['cap'],4),
      "breakeven":p['be'],"units_day_now":round(p['pace14_units_per_day'] or 0,2),"units_day_read":round(p['u28']/28,2),
      "pace_ratio":round((p['pace14_units_per_day'] or 0)/(p['u28']/28),3) if p['u28'] else None,
      "budget_today_pace":round(p['alt_budget'],2),"sp":round(p['split'][0],2),"sb":round(p['split'][1],2),"sbv":round(p['split'][2],2),"sd":round(p['split'][3],2),
      "sp_14d_tracking":round(p['a14'][0],2),"sp_14d_console":p['console_sp'],"label":p['label']})
json.dump(prods,open(OUT+'products.json','w'))
hA={x['mkt']:x['source'] for x in R['checks'] if x['item'].startswith('History check A')}
hB={x['mkt']:x['source'] for x in R['checks'] if x['item'].startswith('History check B')}
sc=[]
for m in ('US','CA'):
    fx=1.4036 if m=='CA' else 1
    sc+= [{"key":f"{m} 1","market":m,"scenario":"BFCM 2025 actual","order":1,"budget":round(S['bfcm2025_total'][m]['adv']*fx,2)},
          {"key":f"{m} 2","market":m,"scenario":"Today's pace","order":2,"budget":round(sum(p['alt_budget'] for p in R['products'] if p['mkt']==m),2)},
          {"key":f"{m} 3","market":m,"scenario":"History check A","order":3,"budget":round(hA[m],2)},
          {"key":f"{m} 4","market":m,"scenario":"History check B","order":4,"budget":round(hB[m],2)},
          {"key":f"{m} 5","market":m,"scenario":"Plan (ceiling)","order":5,"budget":round(R['totals'][m]['budget'],2)}]
json.dump(sc,open(OUT+'scenarios.json','w'))
d=S['daily_bfcm2025']; daily=[]
for m in ('US','CA'):
    tot=sum(d[m]['sales'])
    for k,day in enumerate(d['days']):
        daily.append({"key":f"{m} {day}","market":m,"day":day,"sales":d[m]['sales'][k],"ad_spend":d[m]['adv'][k],"tacos":round(d[m]['adv'][k]/d[m]['sales'][k],4),"weight":round(d[m]['sales'][k]/tot,5),"sessions":d[m]['sessions'][k]})
json.dump(daily,open(OUT+'daily2025.json','w'))
W=S['weekly2026']; wk=[]
for m in ('US','CA'):
    for k,w in enumerate(W['weeks']):
        tot=sum(W[m][t][k] for t in ('sp','sb','sbv','sd'))
        wk.append({"key":f"{m} {w}","market":m,"week":w,"order":k+1,"sp":W[m]['sp'][k],"sb":W[m]['sb'][k],"sbv":W[m]['sbv'][k],"sd":W[m]['sd'][k],"sales":W[m]['sales'][k],"non_sp_share":round(1-W[m]['sp'][k]/tot,4),"tacos":round(tot/W[m]['sales'][k],4)})
json.dump(wk,open(OUT+'weekly2026.json','w'))
for f in sorted(os.listdir(OUT)): print(f, os.path.getsize(OUT+f))
print(score); print(sc)
