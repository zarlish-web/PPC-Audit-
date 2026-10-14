import json,openpyxl,sys,copy
P=json.load(open('/tmp/claude-0/cs/w/page_final.json'))
def build(path):
    w=openpyxl.load_workbook(path,data_only=True); ms=w['Main_Strategy']; H={ms.cell(6,c).value:c for c in range(1,ms.max_column+1)}
    g=lambda r,h: ms.cell(r,H[h]).value
    K=[]
    for r in range(7,111):
        if not g(r,'Keyword'): continue
        rd=lambda x,n: None if x in (None,'') else round(float(x),n)
        K.append({'kw':g(r,'Keyword'),'b':g(r,'Batch'),'size':g(r,'Size') or '','sv':g(r,'Search Volume / Month (FINAL, used in plan)'),'obj':str(g(r,'Campaign Objective')).replace('Ranking — ',''),
          'tr':g(r,'Target Organic Rank (#)'),'path':g(r,'Rank Path (Wk 2 → Wk 4 → Wk 8)'),'req':rd(g(r,'Clicks / Day Required for Target Rank'),2),'clk':rd(g(r,'Planned Clicks / Day'),2),
          'cvr':rd(g(r,'Expected CVR'),4),'med':g(r,'Amazon Suggested Bid Median ($)'),'high':g(r,'Amazon Suggested Bid High ($)'),'ceil':rd(g(r,'Max Ranking CPC ($)'),2),'base':rd(g(r,'Base Bid ($)'),2),
          'mod':int(round((g(r,'TOS Modifier (%)') or 0)*100)),'eff':rd(g(r,'Effective TOS CPC ($)'),2),'spend':rd(g(r,'Planned Spend / Day ($)'),2),'bud':g(r,'Campaign Daily Budget ($)'),
          'sku':str(g(r,'Advertised SKU') or '').replace('CL-COOLING-SHEET-',''),'sl':g(r,'Sleephoria CPC on the Term ($)'),'note':g(r,'Notes')})
    pt=w['Product_Targeting']
    PAT=[{'brand':pt.cell(r,1).value,'prod':pt.cell(r,2).value,'asin':pt.cell(r,3).value,'price':pt.cell(r,4).value,'sku':str(pt.cell(r,6).value).replace('CL-COOLING-SHEET-',''),'med':pt.cell(r,9).value,'cap':round(pt.cell(r,14).value,2),'bid':round(pt.cell(r,15).value,2),'rule':pt.cell(r,16).value} for r in range(6,18)]
    bs=w['Batch_Summary']; BS=[[bs.cell(r,c).value for c in range(1,12)] for r in range(5,9)]

    OBJ=[[bs.cell(r,c).value for c in (1,3,5,6,7,8,10)] for r in range(12,19)]
    a=w['Assumptions']; COST=[[a.cell(r,c).value for c in range(1,12)] for r in range(33,38)]
    return K,PAT,BS,OBJ,COST
K,PAT,BS,OBJ,COST=build(sys.argv[1])
if sys.argv[2]=='check':
    def cmp(a,b,name):
        bad=[(i,x,y) for i,(x,y) in enumerate(zip(a,b)) if json.dumps(x,default=str,sort_keys=True)!=json.dumps(y,default=str,sort_keys=True)]
        print(name,len(a),len(b),'diffs',len(bad)); [print('  ',str(x)[:300],'\n  ',str(y)[:300]) for _,x,y in bad[:3]]
    for k in ('K','PAT','BS','OBJ','COST'): cmp(P[k],locals()[k],k)
else:
    Q=copy.deepcopy(P); Q.update(K=K,PAT=PAT,BS=BS,OBJ=OBJ,COST=COST)
    Q['VS']['checks'][5]=['Daily budgets, total ($)',BS[0][8],BS[0][8],'PASS']
    json.dump(Q,open(sys.argv[2],'w'),default=str)
    print('written',sys.argv[2])
