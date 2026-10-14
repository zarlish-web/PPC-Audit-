import json,openpyxl,sys
S=json.load(open('/tmp/claude-0/cs/w/side.json'))
def build(p):
    w=openpyxl.load_workbook(p,data_only=True); s=w['Side_by_Side']
    hr=[r for r in range(1,40) if s.cell(r,1).value=='Keyword'][0]
    H={s.cell(hr,c).value:c for c in range(1,s.max_column+1)}
    g=lambda r,h: s.cell(r,H[h]).value
    rows=[]
    for r in range(hr+1,s.max_row+1):
        if not s.cell(r,1).value: break
        rows.append({'kw':g(r,'Keyword'),'b':g(r,'Batch'),'size':g(r,'Size') or 'none','obj':str(g(r,'Objective')).replace('Ranking — ',''),'mkl':g(r,'Search volume / mo: MKL (reference)'),
          'seas':g(r,'Search volume / mo: seasonal estimate') if 'Search volume / mo: seasonal estimate' in H else g(r,'Search Volume / mo: seasonal estimate'),
          'wk':g(r,'ASINsight weekly (6 Oct)'),'sv':g(r,'FINAL search volume / mo (used)'),'spd':g(r,'Searches / day'),'mcvr':g(r,'Market CVR (SQP)'),'mcd':g(r,'Market clicks / day'),
          'cs':g(r,'Click share at target'),'tr':g(r,'Target rank'),'req':g(r,'Clicks / day needed'),'plan':g(r,'Clicks / day planned'),'cvr':g(r,'Expected CVR'),'ords':g(r,'Orders / day'),
          'sales':g(r,'Ad sales / day'),'med':g(r,'Amazon median bid'),'ceil':g(r,'Ranking ceiling CPC'),'base':g(r,'Base bid'),'mod':g(r,'Top of search'),'eff':g(r,'Top of search bid'),
          'spend':g(r,'Spend / day'),'bud':g(r,'Campaign budget'),'acos':g(r,'Expected ACoS')})
    a=w['Assumptions']; econ={a.cell(r,1).value:[a.cell(r,c).value for c in range(2,12)] for r in range(33,38)}
    return rows,econ
def eq(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)): return abs(a-b)<1e-6
    if isinstance(a,dict): return set(a)==set(b) and all(eq(a[k],b[k]) for k in a)
    if isinstance(a,list): return len(a)==len(b) and all(eq(x,y) for x,y in zip(a,b))
    return (a or '')==(b or '')
rows,econ=build(sys.argv[1])
if sys.argv[2]=='check':
    print('rows',eq(S['rows'],rows),'econ',eq(S['econ'],econ))
    bad=[(x,y) for x,y in zip(S['rows'],rows) if not eq(x,y)][:2]
    for x,y in bad: print({k:(x[k],y.get(k)) for k in x if not eq(x[k],y.get(k))})
else:
    S['rows']=rows; S['econ']=econ; json.dump(S,open(sys.argv[2],'w'),default=str); print('written')
