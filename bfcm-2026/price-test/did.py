import json
exec(open('analyse.py').read().split("for line in")[0])
F2=F+['SponsoredADS','HSA','VideoAds','SponsoredDisplay']
def A(pers,filt):
    t={k:0.0 for k in F2}; d=0
    for per,days in pers:
        d+=days
        for r in R[per].values():
            c=cls(r)
            if c and filt(c,r):
                for k in F2: t[k]+=(r.get(k) or 0)
    t['d']=d; return t
TOP=[('2026-10-10_2026-10-19',10)]; AFT=[('2026-10-20_2026-10-26',7),('2026-10-27_2026-11-01',6)]; SEP=[('2026-09-18_2026-10-01',14)]
groups=[('B4 White',lambda c,r:c==('B4','WHITE')),('B4 Other',lambda c,r:c==('B4','OTHER')),('B4 parent',lambda c,r:c and c[0]=='B4'),
('B6 White',lambda c,r:c==('B6','WHITE')),('B6 Other',lambda c,r:c==('B6','OTHER')),('B6 parent',lambda c,r:c and c[0]=='B6'),
('B4 King W',lambda c,r:r['ASIN']=='B08KQHRDDG'),('B4 Queen W',lambda c,r:r['ASIN']=='B08KQJGM74'),('B6 King W',lambda c,r:r['ASIN']=='B0CQ2XQF9N'),('B6 Queen W',lambda c,r:r['ASIN']=='B0CQ2ZWGNQ'),('All 10 White',lambda c,r:c and c[1]=='WHITE')]
out={}
print(f"{'grp':12}{'u/d top>aft':>16}{'chg':>6}{'org/d':>14}{'cvr':>14}{'sess/d':>12}{'ad/d':>12}{'SP':>11}{'SB+vid':>11}{'NP/d':>12}{'pre-ad/d':>14}")
for g,f in groups:
    a,b,s=A(TOP,f),A(AFT,f),A(SEP,f)
    pd=lambda t,k:t[k]/t['d']
    cv=lambda t:t['Units']/t['sessions']*100
    out[g]={'sep':s,'top':a,'aft':b}
    print(f"{g:12}{pd(a,'Units'):7.1f}>{pd(b,'Units'):5.1f}{(pd(b,'Units')/pd(a,'Units')-1)*100:+6.0f}%{pd(a,'UnitsOrganic'):6.1f}>{pd(b,'UnitsOrganic'):5.1f}{cv(a):6.1f}>{cv(b):5.1f}%{pd(a,'sessions'):5.0f}>{pd(b,'sessions'):4.0f}{-pd(a,'Advertising'):5.0f}>{-pd(b,'Advertising'):4.0f}{-pd(a,'SponsoredADS'):5.0f}>{-pd(b,'SponsoredADS'):4.0f}{-(pd(a,'HSA')+pd(a,'VideoAds')):5.0f}>{-(pd(b,'HSA')+pd(b,'VideoAds')):4.0f}{pd(a,'NetProfit'):6.0f}>{pd(b,'NetProfit'):5.0f}{pd(a,'NetProfit')-pd(a,'Advertising'):7.0f}>{pd(b,'NetProfit')-pd(b,'Advertising'):5.0f}")
json.dump(out,open('white_test_results.json','w'))
