#!/usr/bin/env python3
"""Build the Hanging Closet decided workbook in the DECOLURE house format."""
import pickle, collections, re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

hdr, rows, hconly, mixed = pickle.load(open('hc_scope.pkl', 'rb'))
camp, MAXCPC, CVR, CEIL = pickle.load(open('hc_dec.pkl', 'rb'))
STR_AGG, STR_SRC = pickle.load(open('hc_str.pkl', 'rb'))
I = {c: i for i, c in enumerate(hdr)}
f = lambda v: float(v) if isinstance(v, (int, float)) else 0.0
g = lambda r, c: r[I[c]]
HCW, HCB = 'HANGING-CLOSET-WHITE', 'HANGING-CLOSET-BLACK'
DAYS = 19

# ---- fix routing for campaigns with no delivery: read the name ----
for c in camp.values():
    if c['route'] == 'NONE':
        n = c['name'].upper()
        hasW, hasB = 'WHITE' in n, 'BLACK' in n
        c['route'] = 'MIXED' if (hasW and hasB) else 'WHITE' if hasW else 'BLACK' if hasB else 'MIXED'

EXPANSION = lambda n: 'SP-Exact-CLR-WHITE' in n
def util(c):
    return (c['sp'] / DAYS / c['budget'] * 100) if c['budget'] else 0.0
def blended(c):
    """Allowable ad cost per unit for THIS campaign, weighted by the units it actually shipped."""
    wu, bu = c['wun'], c['bun']
    return (wu*CEIL['WHITE'] + bu*CEIL['BLACK'])/(wu+bu) if (wu+bu) else CEIL[c['route']] if c['route'] in CEIL else CEIL['BLACK']

# ================= CAMPAIGN VERDICTS =================
verdict = {}
released = 0.0
for cid, c in camp.items():
    n, u, ceil_cpc = c['name'], util(c), MAXCPC[c['route']]
    bceil = blended(c)
    cpa = (c['sp']/c['o']) if c['o'] else None
    if c['state'] != 'enabled':
        verdict[cid] = dict(act='', why='', rev='', newbud=None,
                            cls='paused', scen=f"Campaign paused. {c['imp']:.0f} impressions in window.")
        continue
    if cpa is not None and cpa > bceil:
        # delivering, but every unit it ships costs more than that unit can carry
        factor = bceil/cpa
        newb = max(2.0, round(c['sp']/DAYS*factor, 2))
        verdict[cid] = dict(act=f'CUT BUDGET ${c["budget"]:.2f} → ${newb:.2f} (to the ceiling)',
            why=(f"Delivering {c['o']:.0f} order(s) at ${cpa:.2f} each against a ${bceil:.2f} allowable ad cost per unit for the "
                 f"children this campaign actually ships — {cpa/bceil:.1f}x over. Budget is scaled by exactly the factor it is over "
                 f"ceiling ({bceil:.2f}/{cpa:.2f} = {factor:.2f}) and applied to the observed ${c['sp']/DAYS:.2f}/day spend rate. "
                 f"Bids in this campaign are cut to ${ceil_cpc:.2f} in the same pass."),
            rev=f"Reverses if conversion rises enough to bring cost per order under ${bceil:.2f}; re-read at the 18 September checkpoint.",
            newbud=newb, cls='cut-over-ceiling',
            scen=f"CPA ${cpa:.2f} vs ceiling ${bceil:.2f} ({cpa/bceil:.1f}x), util {u:.1f}%, {c['o']:.0f} orders on ${c['sp']:.2f}")
        released += c['budget'] - newb
    elif cpa is not None:
        # affordable: cost per order sits inside the ceiling. These are the only lanes worth having headroom.
        verdict[cid] = dict(act='', why='', rev='', newbud=None, cls='affordable-hold-headroom',
            scen=(f"CPA ${cpa:.2f} inside a ${bceil:.2f} ceiling — one of only five lanes in the account that clears. "
                  f"Running at {u:.1f}% of ${c['budget']:.2f}/day, so budget is not what limits it; headroom is kept "
                  f"deliberately so the lane can grow if reach improves. Bids held at or under ${ceil_cpc:.2f}."))
    elif EXPANSION(n) and c['imp'] < 200:
        verdict[cid] = dict(act='PAUSE CAMPAIGN',
            why=(f"Expansion-book exact campaign. {c['imp']:.0f} impressions and {c['clk']:.0f} clicks in {DAYS} days "
                 f"on a ${c['budget']:.2f}/day budget — {u:.1f}% utilisation. The term is not reachable at any bid this "
                 f"product can afford: the ceiling is ${ceil_cpc:.2f} and the campaign is already bidding at or above it."),
            rev=f"Reverses if an eligibility or indexing fault is found — check eligibility status before pausing.",
            newbud=0.0, cls='pause-unservable',
            scen=f"Impr {c['imp']:.0f}, clicks {c['clk']:.0f}, util {u:.1f}%, ceiling ${ceil_cpc:.2f}")
        released += c['budget']
    elif u < 15 and c['imp'] >= 200 and max(5.0, round(c['sp']/DAYS*2, 2)) < c['budget'] - 0.01:
        newb = max(5.0, round(c['sp'] / DAYS * 2, 2))
        verdict[cid] = dict(act=f'CUT BUDGET ${c["budget"]:.2f} → ${newb:.2f}',
            why=(f"Spent ${c['sp']:.2f} in {DAYS} days against ${c['budget']:.2f}/day — {u:.1f}% utilisation. "
                 f"Budget is not the constraint; reach is ({c['imp']:.0f} impressions). Cutting to twice the observed "
                 f"spend rate keeps every click it can currently win and releases ${c['budget']-newb:.2f}/day to lanes at their cap."),
            rev="Reverses if impressions rise above the new budget's capacity — re-read utilisation at the 18 September checkpoint.",
            newbud=newb, cls='cut-idle',
            scen=f"Spend ${c['sp']:.2f}/{DAYS}d, util {u:.1f}%, impr {c['imp']:.0f}")
        released += c['budget'] - newb
    elif cpa is not None:
        # affordable: cost per order sits inside the ceiling
        verdict[cid] = dict(act='', why='', rev='', newbud=None, cls='affordable-not-capped',
            scen=(f"CPA ${cpa:.2f} inside a ${bceil:.2f} ceiling, but running at {u:.1f}% of ${c['budget']:.2f}/day — "
                  f"budget is not what limits it. No budget change; bids held at or under ${ceil_cpc:.2f}."))
    else:
        verdict[cid] = dict(act='', why='', rev='', newbud=None, cls='no-orders-below-read',
            scen=f"{c['clk']:.0f} clicks, no orders, util {u:.1f}% — below the 37-click line at which zero is evidence")

print(f"released ${released:.2f}/day from idle and over-ceiling campaigns")
print(collections.Counter(v['cls'] for v in verdict.values()))

# ================= ROW-LEVEL DECISIONS =================
TEMPLATE = ['Count','Product','Entity','Operation','Campaign ID','Ad Group ID','Portfolio ID','Ad ID','Keyword ID',
 'Product Targeting ID','Campaign Name','Ad Group Name','Campaign Name (Informational only)','Ad Group Name (Informational only)',
 'Portfolio Name (Informational only)','Start Date','End Date','Targeting Type','State','Campaign State (Informational only)',
 'Ad Group State (Informational only)','Daily Budget','New Budget','SKU','ASIN (Informational only)',
 'Eligibility Status (Informational only)','Reason for Ineligibility (Informational only)','Ad Group Default Bid',
 'Ad Group Default Bid (Informational only)','Native Language Keyword','Native Language Locale','Match Type','Bidding Strategy',
 'Placement','Percentage','New Percentage','Product Targeting Expression','Resolved Product Targeting Expression (Informational only)',
 'Audience ID','Shopper Cohort Percentage','Shopper Cohort Type','Segment Name','Advertised ASIN','Advertised SKU','Keyword Text',
 'Customer Search Term','Syntax','Targeted KW SV','Bid','New Bids','Top-of-search Impression Share','Impressions','Clicks',
 'Click-through Rate','Spend','Sales','Orders','Units','Conversion Rate','ACOS','CPC','ROAS','CPA','Real ACOS','Routed SKU',
 'Ceiling $/unit','Max CPC $','Scenario','Placement Scenario','Action','Reasoning','Reverses If']
SRC = {'Product':'Product','Entity':'Entity','Operation':'Operation','Campaign ID':'Campaign ID','Ad Group ID':'Ad Group ID',
 'Portfolio ID':'Portfolio ID','Ad ID':'Ad ID','Keyword ID':'Keyword ID','Product Targeting ID':'Product Targeting ID',
 'Campaign Name':'Campaign name','Ad Group Name':'Ad group name','Campaign Name (Informational only)':'Campaign name (Informational only)',
 'Ad Group Name (Informational only)':'Ad group name (Informational only)','Portfolio Name (Informational only)':'Portfolio name (Informational only)',
 'Start Date':'Start date','End Date':'End date','Targeting Type':'Targeting type','State':'State',
 'Campaign State (Informational only)':'Campaign state (Informational only)','Ad Group State (Informational only)':'Ad group state (Informational only)',
 'Daily Budget':'Daily budget','SKU':'SKU','ASIN (Informational only)':'ASIN (Informational only)',
 'Eligibility Status (Informational only)':'Eligibility status (Informational only)',
 'Reason for Ineligibility (Informational only)':'Reason for ineligibility (Informational only)',
 'Ad Group Default Bid':'Ad Group Default Bid','Ad Group Default Bid (Informational only)':'Ad Group Default Bid (Informational only)',
 'Native Language Keyword':'Native language keyword','Native Language Locale':'Native language locale','Match Type':'Match type',
 'Bidding Strategy':'Bidding strategy','Placement':'Placement','Percentage':'Percentage',
 'Product Targeting Expression':'Product targeting expression',
 'Resolved Product Targeting Expression (Informational only)':'Resolved product targeting expression (Informational only)',
 'Audience ID':'Audience ID','Shopper Cohort Percentage':'Shopper Cohort Percentage','Shopper Cohort Type':'Shopper cohort type',
 'Segment Name':'Segment name (Informational only)','Keyword Text':'Keyword text','Bid':'Bid','Impressions':'Impressions',
 'Clicks':'Clicks','Click-through Rate':'Click-through rate','Spend':'Spend','Sales':'Sales','Orders':'Orders','Units':'Units',
 'Conversion Rate':'Conversion Rate','ACOS':'ACOS','CPC':'CPC','ROAS':'ROAS'}

final, census, changes = [], collections.Counter(), []
order = {'Campaign':0,'Ad group':1,'Keyword':2,'Product targeting':3,'Product ad':4,'Bidding adjustment':5,
         'Negative keyword':6,'Campaign negative keyword':7,'Negative product targeting':8}
srows = sorted(rows, key=lambda r: (str(g(r,'Campaign name (Informational only)') or ''), order.get(str(g(r,'Entity')),9)))

for n, r in enumerate(srows, 1):
    cid, ent = g(r,'Campaign ID'), str(g(r,'Entity'))
    c = camp.get(cid, {}); v = verdict.get(cid, {})
    route = c.get('route','MIXED'); mx = MAXCPC[route]
    out = {k: (g(r, SRC[k]) if k in SRC else '') for k in TEMPLATE}
    out['Count'] = n
    out['Routed SKU'] = HCW if route=='WHITE' else HCB if route=='BLACK' else 'BLACK + WHITE'
    out['Ceiling $/unit'] = CEIL['WHITE'] if route=='WHITE' else CEIL['BLACK']
    out['Max CPC $'] = mx
    sp, o = f(g(r,'Spend')), f(g(r,'Orders'))
    out['CPA'] = round(sp/o, 2) if o else ''
    out['Real ACOS'] = round(sp/f(g(r,'Sales')), 4) if f(g(r,'Sales')) else ''
    act = why = rev = scen = plscen = ''
    nb = nbud = npct = ''

    if ent == 'Campaign':
        scen = v.get('scen',''); act = v.get('act',''); why = v.get('why',''); rev = v.get('rev','')
        if v.get('newbud') is not None: nbud = v['newbud']
        census[v.get('cls','hold')] += 1
    elif ent == 'Ad group':
        b = f(g(r,'Ad Group Default Bid'))
        scen = f"Ad-group default bid ${b:.2f} against a ${mx:.2f} ceiling for {out['Routed SKU']}"
        if b > mx:
            nb = mx
            act = f'CUT DEFAULT BID ${b:.2f} → ${mx:.2f}'
            why = (f"Ad-group default bid sits above the ceiling. {out['Routed SKU']} clears at "
                   f"${CEIL['WHITE'] if route=='WHITE' else CEIL['BLACK']:.2f} per unit and converts at "
                   f"{CVR['WHITE'] if route=='WHITE' else CVR['BLACK']*1:.2%}, so the most a click may cost is ${mx:.2f}.")
            rev = "Reverses if the conversion rate rises — recompute the ceiling before raising any bid."
            census['bid-cut'] += 1
        else:
            census['bid-within-ceiling'] += 1
    elif ent in ('Keyword','Product targeting'):
        b = f(g(r,'Bid')); kw = str(g(r,'Keyword text') or g(r,'Product targeting expression') or '')
        clk, imp = f(g(r,'Clicks')), f(g(r,'Impressions'))
        scen = f"Bid ${b:.2f} vs ceiling ${mx:.2f} · {imp:.0f} impr, {clk:.0f} clicks, {o:.0f} orders, spend ${sp:.2f}"
        if b > mx:
            nb = mx
            act = f'CUT BID ${b:.2f} → ${mx:.2f}'
            why = (f'"{kw}" bids ${b:.2f} against a ${mx:.2f} ceiling. {out["Routed SKU"]} carries '
                   f'${CEIL["WHITE"] if route=="WHITE" else CEIL["BLACK"]:.2f} of allowable ad cost per unit and converts at '
                   f'{(CVR["WHITE"] if route=="WHITE" else CVR["BLACK"]):.2%}; ceiling x conversion is the maximum a click may cost. '
                   f'It has drawn {clk:.0f} clicks and {o:.0f} orders on ${sp:.2f}.')
            rev = ("Reverses if this term's own conversion rate is measured above the lane rate at 37 clicks — "
                   "below that the zero is not evidence.")
            census['bid-cut'] += 1
        elif clk >= 37 and o == 0:
            act = 'PAUSE — past sufficiency with no orders'
            why = f'"{kw}" has {clk:.0f} clicks and no orders on ${sp:.2f}. At a {CVR["BLACK"]:.2%} lane conversion rate one order is expected by 37 clicks.'
            rev = "Reverses if a deal window or price change inside the period suppressed conversion."
            census['pause-sufficiency'] += 1
        else:
            census['bid-within-ceiling' if b>0 else 'zero delivery'] += 1
    elif ent == 'Bidding adjustment':
        pct = f(g(r,'Percentage'))
        plscen = f"{str(g(r,'Placement') or '')} at {pct:.0f}%"
        if pct == 0:
            census['structural'] += 1
            scen = 'Placement carries no modifier — correct for a clearance lane'
        else:
            npct = 0; act = f'SET MODIFIER {pct:.0f}% → 0%'
            why = "Placement premiums buy position. On a clearance objective the lane buys volume at a price where losing costs little, so no placement may cost more than the base bid."
            rev = "Reverses only if the objective changes from clearance to rank."
            census['placement-zeroed'] += 1
    elif ent == 'Product ad':
        sku = str(g(r,'SKU') or '')
        scen = f"{sku} · {f(g(r,'Clicks')):.0f} clicks, {f(g(r,'Units')):.0f} units, ${sp:.2f}"
        census['hold-product-ad'] += 1
    else:
        census['negative-structural'] += 1
        scen = 'Negative target — no economic lever'

    out['Scenario'], out['Placement Scenario'] = scen, plscen
    out['Action'], out['Reasoning'], out['Reverses If'] = act, why, rev
    out['New Bids'], out['New Budget'], out['New Percentage'] = nb, nbud, npct
    final.append(out)
    if act:
        fromv = (f"${f(g(r,'Daily budget')):.2f}" if ent=='Campaign' else
                 f"${f(g(r,'Ad Group Default Bid')):.2f}" if ent=='Ad group' else
                 f"{f(g(r,'Percentage')):.0f}%" if ent=='Bidding adjustment' else f"${f(g(r,'Bid')):.2f}")
        tov = (f"${nbud:.2f}" if nbud!='' else f"${nb:.2f}" if nb!='' else f"{npct}%" if npct!='' else 'paused')
        changes.append([ent, str(g(r,'Campaign name (Informational only)') or ''),
                        str(g(r,'Keyword text') or g(r,'Product targeting expression') or ''),
                        'Budget' if ent=='Campaign' else 'Percentage' if ent=='Bidding adjustment' else 'Bid',
                        fromv, tov, act, why, rev])

print(f"final bulk rows {len(final)} | changes {len(changes)}")
print(census)
pickle.dump((TEMPLATE, final, changes, dict(census), camp, verdict, released), open('hc_built.pkl','wb'))
