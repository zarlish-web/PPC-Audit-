import pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D='/tmp/claude-0/-home-user-PPC-Audit-/6199518d-f662-55e7-a2b4-84935779d092/scratchpad/'
OUT='/home/user/PPC-Audit-/research/bedding-feasibility/charts/'
ACC='#2a78d6'; GREY='#898781'; LG='#c3c2b7'; INK='#0b0b0b'; INK2='#52514e'; GOOD='#0ca30c'; BAD='#d03b3b'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.edgecolor':LG,'axes.labelcolor':INK2,'xtick.color':INK2,'ytick.color':INK2,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#fcfcfb','axes.facecolor':'#fcfcfb'})
def fin(fig,ax,title,sub,src,name):
    fig.suptitle(title,x=0.02,ha='left',fontsize=13,fontweight='bold',color=INK,y=0.98)
    ax.set_title(sub,loc='left',fontsize=9.5,color=INK2,pad=10)
    fig.text(0.02,0.01,'Source: '+src,fontsize=8,color=GREY)
    fig.tight_layout(rect=(0,0.03,1,0.93)); fig.savefig(OUT+name,dpi=160); plt.close(fig)

# 1 market opportunity: tracked revenue by segment (Data Dive)
s=pd.read_csv(D+'data/niche_summary.csv'); e=pd.read_csv(D+'data/niche_summary_extra.csv')
seg=[('Generic sheet sets',79.6,26544),('Solid duvet covers',12.95,3194),('Cotton sheet sets',11.88,2453),('Bamboo sheet sets',8.99,2782),('Cooling sheet sets',8.41,1934),('Bamboo fitted sheets',6.93,224),('Mattress protectors',6.40,6073),('Satin sheet sets',6.12,1074),('Pre-washed cotton sets',4.53,492),('Quilt sets',3.75,1609),('Waffle duvet covers',2.81,131),('Linen sheets',1.28,1004),('Latex toppers',0.98,257)]
df=pd.DataFrame(seg,columns=['seg','rev','rev_med']).sort_values('rev')
fig,ax=plt.subplots(figsize=(9,5.2))
cols=[ACC if x in ('Pre-washed cotton sets','Cotton sheet sets','Waffle duvet covers') else LG for x in df.seg]
ax.barh(df.seg,df.rev,color=cols,height=0.6)
for y,(v,r) in enumerate(zip(df.rev,df.rev_med)): ax.text(v+0.6,y,f'${v:.1f}M · median {r:,} reviews',va='center',fontsize=8.5,color=INK2)
ax.set_xlabel('Estimated monthly revenue of tracked rivals, US ($M, upper bound)'); ax.set_xlim(0,105)
fin(fig,ax,'Cotton niches combine real demand with low review barriers','Tracked-rival revenue and median review count per segment (blue = shortlisted)','Data Dive niche snapshots, Mar–Oct 2026 (estimates; sibling ASINs can repeat parent sales)','01_market_opportunity_by_segment.png')

# 2 review barrier vs price
pts=[('Bamboo',88.99,2782),('Satin',26.99,1074),('Cooling',69.99,1934),('Quilt',29.99,1609),('Cotton sets',63.99,2453),('Pre-washed cotton',39.99,492),('Linen',129.89,1004),('Solid duvet',44.99,3194),('Waffle duvet',56.99,131),('Mattress protector',27.49,6073),('Generic sets',35.98,26544),('Satin fitted',18.49,662),('Bamboo fitted',49.99,224),('Latex topper',207,257)]
fig,ax=plt.subplots(figsize=(9,5.4))
for n,p,r in pts:
    c=ACC if n in ('Pre-washed cotton','Cotton sets','Waffle duvet') else GREY
    ax.scatter(p,r,s=60,color=c,edgecolor='white',zorder=3); ax.annotate(n,(p,r),xytext=(6,4),textcoords='offset points',fontsize=8.5,color=INK)
ax.set_yscale('log'); ax.set_xlabel('Median price of tracked rivals (USD)'); ax.set_ylabel('Median reviews (log scale)')
ax.axhline(500,color=LG,ls='--',lw=1); ax.text(150,520,'500 reviews',fontsize=8,color=GREY)
fin(fig,ax,'Pre-washed cotton and waffle duvets sit below the 500-review line at mid prices','Review barrier vs price by US segment','Data Dive niche snapshots, Mar–Oct 2026; Command Center roster 25 Oct 2026','02_review_barrier_vs_price.png')

# 3 CPC vs break-even: ACoS vs break-even by product (YTD)
t=pd.read_csv(D+'data/ppc_product_table_ytd.csv'); ec=pd.read_csv(D+'data/economics.csv'); b=ec[ec['size']=='BLENDED']
m=t.merge(b[['product_id','marketplace','breakeven_acos']].assign(product_id=lambda x:x.product_id.astype(str)),left_on=[t.product_id.astype(str),'marketplace'],right_on=['product_id','marketplace'])
m=m[(m.marketplace=='US')&(m.spend>8000)].copy(); m['name']=m.product_name.str.replace('Decolure ','D. ').str.replace('Sleephoria ','S. ').str.replace('CooLinens ','CL ')
m=m.sort_values('acos_pct')
fig,ax=plt.subplots(figsize=(9,5.6))
y=range(len(m)); ax.barh(list(y),m.acos_pct,color=[BAD if a>b2 else GOOD for a,b2 in zip(m.acos_pct,m.breakeven_acos)],alpha=0.55,height=0.55)
ax.scatter(m.breakeven_acos,list(y),marker='|',s=300,color=INK,zorder=3,label='break-even ACoS')
ax.set_yticks(list(y)); ax.set_yticklabels(m.name,fontsize=8.5); ax.set_xlabel('ACoS, Jan–Oct 2026 (%)'); ax.legend(frameon=False,loc='upper right',bbox_to_anchor=(1,0.12))
fin(fig,ax,f'{(m.acos_pct>m.breakeven_acos).sum()} of {len(m)} US bedding lines advertise above break-even ACoS','ACoS (bar: green below / red above break-even) against each product\'s break-even ACoS (tick)','Command Center ppc_product_table YTD 2026 and unit economics snapshot 26 Oct 2026','03_acos_vs_breakeven.png')

# 4 unit economics waterfall P1
u=pd.read_csv(D+'model/out_unit_econ.csv').set_index('id').loc['P1_US_percale']
steps=[('Price',u.price),('Refunds',-u.refunds),('Referral',-u.referral),('FBA',-u.fba),('Factory FOB',-u.fob),('Freight+duty',-u.freight_duty),('Storage+inbound',-u.storage_inbound),('Unsellable returns',-u.unsellable_returns),('Promotions',-u.promo)]
fig,ax=plt.subplots(figsize=(9.5,5)); run=0
for i,(n,v) in enumerate(steps):
    if i==0: ax.bar(i,v,color=LG); run=v; ax.text(i,v+1,f'${v:.2f}',ha='center',fontsize=8.5)
    else:
        ax.bar(i,v,bottom=run,color=BAD,alpha=0.55); ax.text(i,run+1,f'{v:.2f}',ha='center',fontsize=8.5); run+=v
ax.bar(len(steps),run,color=GOOD,alpha=0.6); ax.text(len(steps),run+1,f'${run:.2f}',ha='center',fontsize=9,fontweight='bold')
ax.set_xticks(range(len(steps)+1)); ax.set_xticklabels([s[0] for s in steps]+['Contribution\nbefore ads'],rotation=30,ha='right',fontsize=8.5); ax.set_ylabel('USD per unit')
fin(fig,ax,'A $66.49 cotton set keeps $19.84 before advertising (29.8%)','P1 pre-washed cotton percale set, US, blended size mix (red = costs, green = contribution)','model.py; FOB is an assumption pending mill cost sheets','04_unit_economics_waterfall_P1.png')

# 5 capital low/base/high stacked
cap=pd.DataFrame({'Inventory (landed)':[30.5,50.8,81.3],'One-time set-up':[12.5,23.0,34.0],'Vine & coupons':[2.0,4.0,6.0],'PPC 90 days':[20,35,45],'Contingency':[6.5,16.9,33.3]},index=['Low','Base','High'])
fig,ax=plt.subplots(figsize=(8,5)); bottom=[0,0,0]; shades=[ACC,'#6da7ec','#9ec5f4','#cde2fb',LG]
for c,col in zip(cap.columns,shades):
    ax.bar(cap.index,cap[c],bottom=bottom,color=col,label=c,width=0.55); bottom=[a+b for a,b in zip(bottom,cap[c])]
for i,v in enumerate(bottom): ax.text(i,v+3,f'${v:.1f}k',ha='center',fontweight='bold')
ax.set_ylabel('USD thousands'); ax.legend(frameon=False,fontsize=8.5,loc='upper left')
fin(fig,ax,'A realistic US test needs about $130k; $72k at the floor','Capital to test one product family by component','Launch budget model (Profit_Scenarios / Launch_Budget tabs)','05_launch_capital.png')

# 6 sensitivity tornado
se=pd.read_csv(D+'model/out_sensitivity_p1.csv').iloc[::-1]
fig,ax=plt.subplots(figsize=(8.5,4.2)); base=se.contrib_base.iloc[0]
for i,r in enumerate(se.itertuples()):
    ax.barh(i,r.contrib_low-base,left=base,color=BAD,alpha=0.55,height=0.5); ax.barh(i,r.contrib_high-base,left=base,color=GOOD,alpha=0.55,height=0.5)
    ax.text(min(r.contrib_low,r.contrib_high)-0.3,i,f'${min(r.contrib_low,r.contrib_high):.2f}',ha='right',va='center',fontsize=8.5); ax.text(max(r.contrib_low,r.contrib_high)+0.3,i,f'${max(r.contrib_low,r.contrib_high):.2f}',va='center',fontsize=8.5)
ax.axvline(base,color=INK,lw=1); ax.set_yticks(range(len(se))); ax.set_yticklabels(se.variable,fontsize=9); ax.set_xlabel('Contribution before ads, USD per unit'); ax.set_xlim(12,28)
fin(fig,ax,'Price moves contribution most, then factory cost','P1 contribution before ads ($19.84 base) under each variable\'s low and high case','model.py sensitivity','06_sensitivity_tornado_P1.png')

# 7 scenarios
sc=pd.read_csv(D+'model/out_scenarios_monthly.csv')
fig,ax=plt.subplots(figsize=(9,5))
for n,c,lw in [('Conservative',GREY,1.8),('Upside','#b4b2a9',1.8),('Base',ACC,2.6)]:
    d=sc[sc.scenario==n]; ax.plot(d.month,d.contribution_after_ads/1000,color=c,lw=lw,marker='o',ms=4); ax.text(12.2,d.contribution_after_ads.iloc[-1]/1000,f'{n} ${d.contribution_after_ads.iloc[-1]/1000:.1f}k',va='center',fontsize=9)
ax.axhline(0,color=INK2,lw=1); ax.set_xlim(1,14.5); ax.set_xticks(range(1,13)); ax.set_xlabel('Month of selling'); ax.set_ylabel('Contribution after ads ($k per month)')
fin(fig,ax,'Base case turns contribution-positive in month 5; conservative never does','Monthly contribution after advertising by scenario','model.py scenario engine (inputs in Profit_Scenarios tab)','07_scenario_contribution.png')

# 8 account trend (two panels, no dual axis)
mo=pd.read_csv(D+'data/sb_monthly.csv'); us=mo[(mo.mp=='amazon.com')&(mo.month>='2025-01')]
fig,(ax,ax2)=plt.subplots(2,1,figsize=(9.5,6),sharex=True,gridspec_kw={'height_ratios':[3,2]}); x=list(range(len(us)))
ax.bar(x,us.Sales/1e6,color=LG,width=0.65); ax.set_ylabel('Sales ($M)')
ax2.plot(x,(-us.Ads/us.Sales*100),color=ACC,lw=2.2,marker='o',ms=3.5); ax2.set_ylabel('TACoS (%)')
for i in (0,len(x)-1): ax2.text(x[i],(-us.Ads/us.Sales*100).iloc[i]+0.8,f"{(-us.Ads/us.Sales*100).iloc[i]:.1f}%",ha='center',fontsize=8.5)
ax2.set_xticks(x); ax2.set_xticklabels(us.month.str[2:],rotation=45,fontsize=8)
fin(fig,ax,'US sales are falling while ad intensity climbs','Ecotero bedding account, Amazon.com, monthly sales (top) and TACoS (bottom); Oct 2026 partial (25 days)','Sellerboard, pulled 26 Oct 2026','08_account_trend_us.png')
print('ok')
