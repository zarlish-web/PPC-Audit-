import json, collections, os
OUT='/tmp/claude-0/-home-user-PPC-Audit-/51b9bd0e-5fdd-5e9c-87d4-612ed5188e17/scratchpad/dash/'
R=json.load(open('verify_results.json')); S=json.load(open('source/account_pulls_2026-11-02.json'))
C=collections.Counter((x['section'],x['status']) for x in R['checks'])
secs=sorted({x['section'] for x in R['checks']})
short={"1. Source records":"Source records","2. Product numbers":"Product numbers","3. Cross-source":"Cross-source","4. Workbook arithmetic":"Workbook arithmetic","5. Decisions and wording":"Decisions and wording","6. Is the demand read still current":"Demand still current","7. Growth plan":"Growth plan","8. Key days":"Key days"}
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

# ---- year over year, BFCM vs plan, growth plan, key days
YO = json.load(open('yoy_results.json'))
yrows = []
for m in ('US', 'CA'):
    for x in YO['markets'][m]['rows']:
        if x['adv25'] + x['adv26'] + x['sales25'] + x['sales26'] < 1: continue
        yrows.append({"key": f"{m} · {x['product']}", "market": m, "product": x['product'], "group": x['class'], "sales25": x['sales25'], "sales26": x['sales26'],
                      "sp25": x['sp25'], "sp26": x['sp26'], "nonsp25": x['nonsp25'], "nonsp26": x['nonsp26'], "ads25": x['adv25'], "ads26": x['adv26']})
json.dump(yrows, open(OUT + 'yoy.json', 'w'))
bridge = []
for m in ('US', 'CA'):
    D = YO['markets'][m]['decomp']
    steps = [("All ads, 2025", D['adv25'], "total"), ("Same products: SP", D['lfl_sp'], "step"), ("Same products: SB, video, SD", D['lfl_nonsp'], "step"),
             ("New products", D['new'], "step"), ("Older listings and long tail", D['old_and_tail'], "step"), ("All ads, 2026", D['adv26'], "total")]
    for k, (lab, v, kind) in enumerate(steps):
        bridge.append({"key": f"{m} {k+1}", "market": m, "order": k + 1, "step": lab, "amount": round(v, 2), "kind": kind})
json.dump(bridge, open(OUT + 'yoybridge.json', 'w'))
lfl = []
for m in ('US', 'CA'):
    D = YO['markets'][m]['decomp']
    lfl.append({"market": m, "sales25": round(D['lfl_sales25'], 2), "sales26": round(D['lfl_sales26'], 2), "sales_change": round(D['lfl_sales26'] / D['lfl_sales25'] - 1, 4),
                "tacos25": round(D['lfl_adv25'] / D['lfl_sales25'], 4), "tacos26": round(D['lfl_adv26'] / D['lfl_sales26'], 4),
                "sp_tacos25": round(D['lfl_sp25'] / D['lfl_sales25'], 4), "sp_tacos26": round(D['lfl_sp26'] / D['lfl_sales26'], 4),
                "new_sales26": round(D['new_sales26'], 2), "sessions_day25": round(D['sessions25'] / 14), "sessions_day26": round(D['sessions26'] / 14),
                "cvr25": round(D['cvr25'], 4), "cvr26": round(D['cvr26'], 4), "cpc25": round(D['cpc25'], 2), "cpc26": round(D['cpc26'], 2),
                "ads25": round(D['adv25'], 2), "ads26": round(D['adv26'], 2)})
json.dump(lfl, open(OUT + 'yoykpi.json', 'w'))
bfg = []
for m in ('US', 'CA'):
    B = [x for x in YO['bfcm'] if x['market'] == m]
    for grp in ("In both", "New since BFCM 2025", "Not in the 2026 plan"):
        S = [x for x in B if x['class'] == grp]
        bfg.append({"key": f"{m} · {grp}", "market": m, "group": grp, "spend25": round(sum(x['adv25'] for x in S), 2), "plan26": round(sum(x['plan_budget26'] for x in S), 2),
                    "sales25": round(sum(x['sales25'] for x in S), 2), "plan_sales26": round(sum(x['plan_sales26'] for x in S), 2)})
json.dump(bfg, open(OUT + 'bfcmcompare.json', 'w'))
g7 = {(x['mkt'], x['product']): x for x in R['checks'] if x['section'] == '7. Growth plan'}
gr = []
for p in R['products']:
    lo, hi = p['band']; x = g7.get((p['mkt'], p['name']))
    gr.append({"key": f"{p['mkt']} · {p['name']}", "market": p['mkt'], "stage": p['stage'], "band": (f"{lo*100:.0f}-{hi*100:.0f}%" if lo is not None else "no band"),
               "floor_bfcm": round(lo * p['fac'], 4) if lo is not None else None, "cap": None if p['cap'] is None else round(p['cap'], 4), "plan_tacos": round(p['plan_t'], 4),
               "result": (x['status'] if x else ""), "note": (x['note'] or "Inside the band") if x else ""})
json.dump(gr, open(OUT + 'growth.json', 'w'))
from openpyxl import load_workbook
wbp = load_workbook('/tmp/claude-0/-home-user-PPC-Audit-/51b9bd0e-5fdd-5e9c-87d4-612ed5188e17/scratchpad/final_chk.xlsx', data_only=True)['Budget by day']
DAYS26 = ["Thu Nov 19", "Fri Nov 20", "Sat Nov 21", "Sun Nov 22", "Mon Nov 23", "Tue Nov 24", "Wed Nov 25", "Thu Nov 26", "Fri Nov 27 (BF)", "Sat Nov 28", "Sun Nov 29", "Mon Nov 30 (CM)"]
kd = []; blk = None
for r in range(1, wbp.max_row + 1):
    a = wbp.cell(r, 1).value
    if a in ("United States (US$)", "Canada (C$)"): blk = "US" if a.startswith("United") else "CA"
    if blk and a == "Total":
        for k in range(12):
            kd.append({"key": f"{blk} {k+1:02d}", "market": blk, "order": k + 1, "day": DAYS26[k], "budget": round(wbp.cell(r, 3 + k).value, 2),
                       "peak": k in (8, 11), "ld": ("Lightning Deals: Satin 6 Pc, Silk" if (blk == "US" and k == 4) else ("Lightning Deal: Sleephoria Cooling Fitted" if (blk == "US" and k == 6) else ""))})
json.dump(kd, open(OUT + 'keydays.json', 'w'))
for f in sorted(os.listdir(OUT)):
    if f.endswith('.json'): print(f, os.path.getsize(OUT + f))
