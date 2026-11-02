import json,re
R=json.load(open('source/bamboo_sku_rows_by_window.json'))
P=[('2026-09-18_2026-10-01',14,'Sep norm'),('2026-10-02_2026-10-08',7,'pre-step'),('2026-10-10_2026-10-19',10,'top price'),('2026-10-20_2026-10-26',7,'cut wk1'),('2026-10-27_2026-11-01',6,'cut wk2')]
def cls(r):
    sku=r['SKU']; n=r['Name'] or ''
    if not sku.startswith('BAMBOO-') or 'DECOLURE' not in n: return None
    line='B6' if '6PCS' in sku or '6 Pc' in n else 'B4'
    col='WHITE' if '-WHITE' in sku else 'OTHER'
    return line,col
F=['Units','UnitsPPC','UnitsOrganic','Sales','Advertising','NetProfit','sessions']
def agg(per,filt):
    t={k:0.0 for k in F}
    for r in R[per].values():
        c=cls(r)
        if c and filt(c,r):
            for k in F: t[k]+= (r.get(k) or 0)
    return t
def show(label,filt):
    print('\n==',label)
    print(f"{'period':10}{'u/d':>7}{'org/d':>7}{'ppc/d':>7}{'sess/d':>8}{'cvr':>7}{'ASP':>8}{'ad/d':>8}{'TACoS':>7}{'NP/d':>8}")
    for per,d,lab in P:
        t=agg(per,filt)
        u=t['Units']; s=t['sessions']
        print(f"{lab:10}{u/d:7.1f}{t['UnitsOrganic']/d:7.1f}{t['UnitsPPC']/d:7.1f}{s/d:8.0f}{(u/s*100 if s else 0):6.1f}%{(t['Sales']/u if u else 0):8.2f}{-t['Advertising']/d:8.0f}{(-t['Advertising']/t['Sales']*100 if t['Sales'] else 0):6.1f}%{t['NetProfit']/d:8.0f}")
for line in ['B4','B6']:
    show(line+' WHITE all sizes',lambda c,r,l=line:c==(l,'WHITE'))
    show(line+' OTHER colours',lambda c,r,l=line:c==(l,'OTHER'))
for asin,lab in [('B08KQHRDDG','B4 King White'),('B08KQJGM74','B4 Queen White'),('B0CQ2XQF9N','B6 King White'),('B0CQ2ZWGNQ','B6 Queen White')]:
    show(lab,lambda c,r,a=asin:r['ASIN']==a)
