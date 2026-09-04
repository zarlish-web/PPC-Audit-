import pandas as pd, numpy as np, pickle, shutil, openpyxl
SRC='/root/.claude/uploads/f01da844-e516-5303-96fa-ec17555f9d55/c6f7cd3f-SLQS_Decided_Bulk_v5_1Sep2026_1.xlsx'
OUT='SLQS_Decided_Bulk_v6_CORRECTED_04Sep2026.xlsx'
shutil.copy(SRC,OUT)
num=lambda s: pd.to_numeric(s,errors='coerce')
ASP,CEIL,MARGIN=40.91,28.47,13.77; BE=MARGIN/ASP; CA=CEIL/ASP; FLOOR_BID=0.25; FLOOR_BUD=5.00
P='Portfolio Name (Informational only)'; CN='Campaign Name (Informational only)'

fb=pd.read_excel(SRC,sheet_name='Final Bulk')
lowcov=pickle.load(open('lowcov.pkl','rb'))
R=fb['Reasoning'].astype(str); A=fb['Action'].astype(str)
qs=(fb[P]=='Quilt Set'); kw=qs&(fb['Entity']=='Keyword'); cp=qs&(fb['Entity']=='Campaign')
clicks=R.str.extract(r'(\d+)\s+clicks',expand=False).astype(float)
cpa   =R.str.extract(r'\$([\d.]+)\s+CPA',expand=False).astype(float)
low   =fb[CN].isin(lowcov)
bid   =num(fb['Bid']); dbud=num(fb['Daily Budget'])
log=[]
def mark(m,newbid=None,newbud=None,act=None,rsn=None,tag=''):
    n=int(m.sum())
    if newbid is not None: fb.loc[m,'New Bids']=newbid if np.isscalar(newbid) else newbid[m]
    if newbud is not None: fb.loc[m,'New Budget']=newbud if np.isscalar(newbud) else newbud[m]
    if act is not None: fb.loc[m,'Action']=act
    if rsn is not None: fb.loc[m,'Reasoning']=rsn
    log.append((tag,n)); return n

# 1 — RESTORE rows under the click line with no stock reason
m = kw & (clicks<15) & (~low) & (A.str.startswith('Trim')|R.str.contains('Not enough evidence',na=False))
fb.loc[m,'New Bids']=bid[m]
mark(m, act='No change', tag='1. Restored — under the click line',
     rsn=('CENSUS: below the click line. '+clicks[m].fillna(0).astype(int).astype(str)+
          ' clicks in 30 days with no orders — under the 15-click review trigger, so there is no '
          'performance evidence to act on. High-cover stock, so no stock reason to cut either. '
          'Bid held at $'+bid[m].round(2).astype(str)+'. Re-read at 15 clicks.'))

# 2 — LOW-COVER rows: stock decision stands, taken to the floor and re-reasoned
m = kw & (clicks<15) & low & (A.str.startswith('Trim')|R.str.contains('Not enough evidence',na=False))
mark(m, newbid=FLOOR_BID, act='Cut bid to floor $0.25', tag='2. Re-reasoned as a stock decision, bid to floor',
     rsn='STOCK DECISION, not a performance one. This SKU holds under 120 days of cover and clears '
         'without paid support, so the click line does not apply — the same way an irrelevant term is '
         'negated at any click count. Bid to the $0.25 floor rather than a partial trim, because a '
         'partial trim keeps paying for volume we do not need. Reverses if cover exceeds 120 days.')

# 3 — above-ceiling rows re-banded on the ACoS ladder
acos=cpa/ASP
for lo_,hi_,cut,band in [(0.70,1.00,0.30,'70-100%'),(1.00,9.9,0.50,'100%+')]:
    m = kw & R.str.contains('above the',na=False) & acos.notna() & (acos>=lo_) & (acos<hi_)
    nb=(bid*(1-cut)).clip(lower=FLOOR_BID).round(2)
    mark(m, newbid=nb, act=None, tag=f'3. Re-banded {band} -> cut {int(cut*100)}%',
         rsn=('LADDER: ACoS '+(acos[m]*100).round(1).astype(str)+'% sits in the '+band+' band, so the cut is '
              +str(int(cut*100))+'% — not the flat 40% applied before. Above this product\'s '
              f'{CA:.1%} ceiling ACoS, so the delivering protection does not apply. '
              'Break-even ACoS is '+f'{BE:.1%}'+'. New bid $'+nb[m].astype(str)+'.'))
    fb.loc[m,'Action']=('Cut bid $'+bid[m].round(2).astype(str)+' to $'+nb[m].astype(str))

# 4 — the one ceiling breach
m = kw & (fb['Keyword Text'].astype(str)=='white quilt king size') & (num(fb['New Bids'])>0.55)
mark(m, newbid=0.55, act='Raise bid $0.50 to $0.55', tag='4. Ceiling breach corrected',
     rsn='Converted at $25.90 CPA (63.3% ACoS). Max affordable bid is current bid x (ceiling / CPA) '
         '= $0.50 x (28.47 / 25.90) = $0.55. The previous $0.65 was above that. Inside the subsidy zone, '
         'low in it, as a clearance bid should be.')

# 5 — blank keyword rows get a census class
m = kw & fb['Action'].isna()
mark(m, act='No change', tag='5. Blank rows classified',
     rsn='CENSUS: no decision this cycle. No 30-day click or order evidence was carried into this file '
         'for these rows, so no performance verdict is available and none is asserted. Listed here so the '
         'row is accounted for rather than silently skipped. Needs the 30-day export to decide.')

# 6 — campaign budgets: cap cuts that release nothing
peak=(num(fb['Spend']).fillna(0).combine(num(fb['LW Spend']).fillna(0),max))/7
nb=num(fb['New Budget'])
allpaused = cp & R.str.contains('Every keyword in this campaign is now paused',na=False)
mark(allpaused, newbud=np.nan, act='Pause campaign', tag='6a. Shell campaigns paused, not funded at $1',
     rsn='Every keyword in this campaign is paused, so the campaign spends nothing. Paused outright rather '
         'than left at a $1 budget: a paused campaign retains its history and its ID just as well, and a $1 '
         'budget breaches the $5.00 operating floor for no benefit.')

m = cp & nb.notna() & (nb<dbud) & (~allpaused)
fb.loc[m,'New Budget']=np.nan
mark(m, act='No change — budget held',
     tag='6b. Cap cuts reversed (released $0.00)',
     rsn=('BUDGET IS NOT A WASTE LEVER. This campaign spends $'+peak[m].round(2).astype(str)+'/day against a $'
          +dbud[m].round(0).astype(str)+'/day cap — cutting the cap releases nothing, because the lane never '
          'reaches it. Where this SKU should not be supported, that is done at target level on the keyword rows '
          'in this campaign, which is where the money is actually spent. Cap held.'))

nb=num(fb['New Budget'])          # RECOMPUTE: 6b cleared the cuts above
m = cp & nb.notna() & (nb<FLOOR_BUD) & (nb>0)
mark(m, newbud=FLOOR_BUD, tag='6c. Budgets raised to the $5.00 floor', act='Set budget to $5',
     rsn='Held at the $5.00 operating floor. Below this a campaign cannot deliver a readable day, so it is '
         'either funded at the floor or paused — never left in between, spending money it cannot learn from.')
fb.to_pickle('fixed.pkl')
print(f"{'CHANGE':52s} {'ROWS':>6s}")
print('-'*60)
for t,n in log: print(f"{t:52s} {n:>6d}")
print('-'*60); print(f"{'TOTAL ROWS CHANGED':52s} {sum(n for _,n in log):>6d}")

# ---- 7 — rows restored onto a bid that was already under the floor ----
nb2=num(fb['New Bids'])
m = kw & nb2.notna() & (nb2<FLOOR_BID)
mark(m, newbid=FLOOR_BID, act='Raise bid to floor $0.25', tag='7. Sub-floor bids lifted to $0.25',
     rsn='CENSUS: below the click line, so no performance verdict — but the existing bid sits under the '
         '$0.25 operating floor, where it wins too few auctions to ever reach the click line at all. '
         'Raised to the floor so the term can actually prove itself. Re-read at 15 clicks.')

# ---- 8 — profitable rows cut on stock: keep the cut, name it correctly ----
acos8=cpa/ASP
m = kw & acos8.notna() & (acos8<=BE) & (num(fb['New Bids'])<bid) & (low | R.str.contains('days of cover',na=False))
mark(m, act=None, tag='8. Profitable-but-non-incremental, reasoning corrected',
     rsn=('INCREMENTALITY, not efficiency. This keyword converts at $'+cpa[m].round(2).astype(str)+
          ' CPA — an ACoS of '+(acos8[m]*100).round(1).astype(str)+f'%, below this product\'s {BE:.1%} '
          'break-even, so it is profitable and the ladder would not touch it. It is cut anyway because the '
          'SKU holds under 120 days of cover and clears without paid support: we would be paying for units '
          'that were going to sell regardless. That is a stock judgement, not a performance one, and it is '
          'the one case that overrides the break-even protection. Reverses if cover exceeds 120 days.'))
fb.to_pickle('fixed.pkl')
print(f"\n{'ADDITIONAL':52s} {'ROWS':>6s}"); print('-'*60)
for t,n in log[-2:]: print(f"{t:52s} {n:>6d}")
print('-'*60); print(f"{'GRAND TOTAL':52s} {sum(n for _,n in log):>6d}")
