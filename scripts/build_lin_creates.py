"""SP tranche A creates -> upload-ready Amazon bulk; all 671 creates -> Joseph's template."""
import pandas as pd, numpy as np

S = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
SHEET = 'Sponsored Products Campaigns'
START = '20260909'
STRATEGY = 'Dynamic bids - down only'

HEADER = ("Product, Entity, Operation, Campaign ID, Ad Group ID, Portfolio ID, Ad ID, Keyword ID, "
          "Product Targeting ID, Campaign Name, Ad Group Name, Campaign Name (Informational only), "
          "Ad Group Name (Informational only), Portfolio Name (Informational only), Start Date, "
          "End Date, Targeting Type, State, Campaign State (Informational only), "
          "Ad Group State (Informational only), Daily Budget, SKU, ASIN, "
          "Eligibility Status (Informational only), Reason for Ineligibility (Informational only), "
          "Ad Group Default Bid, Ad Group Default Bid (Informational only), Bid, Keyword Text, "
          "Native Language Keyword, Native Language Locale, Match Type, Bidding Strategy, Placement, "
          "Percentage, Product Targeting Expression, "
          "Resolved Product Targeting Expression (Informational only), Impressions, Clicks, "
          "Click-through Rate, Spend, Sales, Orders, Units, Conversion Rate, ACOS, CPC, ROAS, "
          "Campaign Serving Status (Informational only), Ad Group Serving Status (Informational only), "
          "Keyword Serving Status (Informational only), Ad Serving Status (Informational only), "
          "Product Targeting Serving Status (Informational only), "
          "Ad Serving Status Reason (Informational only)").split(', ')

sp = pd.read_pickle(f'{S}/LIN_New_SP_Campaigns.pkl')
sb = pd.read_pickle(f'{S}/LIN_New_SB_Campaigns.pkl')
sd = pd.read_pickle(f'{S}/LIN_New_SD_Campaigns.pkl')

# ============================ 1. SP tranche A bulk ============================
a = sp[sp.Tranche.str.startswith('A')].copy()
ORDER = {'Campaign': 0, 'Ad Group': 1, 'Product Ad': 2, 'Keyword': 3, 'Product Targeting': 4,
         'Bidding Adjustment': 5}
a['_o'] = a.Entity.map(ORDER)
a = a.sort_values(['CampaignId', '_o'], kind='stable').reset_index(drop=True)

out = pd.DataFrame({c: None for c in HEADER}, index=range(len(a)))
out['Product'] = 'Sponsored Products'
out['Entity'] = a.Entity.values
out['Operation'] = 'create'
out['Campaign ID'] = a.CampaignId.values                 # name placeholder on creates
out['Ad Group ID'] = a.AdGroupId.values
out['Campaign Name'] = a.CampaignName.values
out['Targeting Type'] = a.TargetingType.values
out['State'] = a.State.values
out['Daily Budget'] = a.DailyBudget.values
out['SKU'] = a.SKU.values
out['Bid'] = np.where(a.Entity.isin(['Keyword', 'Product Targeting']), a.Bid, None)
out['Ad Group Default Bid'] = np.where(a.Entity == 'Ad Group', a.Bid, None)
out['Keyword Text'] = a.KeywordText.values
out['Match Type'] = a.MatchType.map(lambda v: str(v).title() if pd.notna(v) else None).values
out['Percentage'] = a.Percentage.values

expr = a.Expr.where(a.Entity == 'Product Targeting')
out['Product Targeting Expression'] = expr.values
out['Placement'] = a.Expr.where(a.Entity == 'Bidding Adjustment').values

# Ad Group Name is required on Ad Group creates; children reference by Ad Group ID.
out['Ad Group Name'] = np.where(a.Entity == 'Ad Group', a.AdGroupId, None)

# Campaign creates carry Start Date, Targeting Type and Bidding Strategy (canon §2).
iscamp = out.Entity == 'Campaign'
out.loc[iscamp, 'Start Date'] = START
out.loc[iscamp, 'Bidding Strategy'] = STRATEGY
out['End Date'] = None

# State on every row (rule 3); the source leaves it blank on child rows.
out['State'] = [s if pd.notna(s) and str(s).strip() else 'enabled' for s in out['State']]

for c in ['Daily Budget', 'Bid', 'Ad Group Default Bid', 'Percentage']:
    out[c] = pd.to_numeric(out[c], errors='coerce').round(2)
out = out[HEADER].astype(object).where(pd.notna(out[HEADER]), None)

OUT_SP = f'{S}/LIN_UPLOAD_SP_CREATES_TRANCHE_A_09Sep2026.xlsx'
with pd.ExcelWriter(OUT_SP, engine='openpyxl') as xl:
    out.to_excel(xl, sheet_name=SHEET, index=False)
    ws = xl.sheets[SHEET]
    for col in ('O', 'P'):
        for cell in ws[col]:
            cell.number_format = '@'

print('SP tranche A bulk:', len(out), 'rows |', out.Entity.value_counts().to_dict())

# ==================== 2. all 671 creates -> Joseph's template =================
COLS = ['decision', 'campaign', 'entity_type', 'entity', 'match_type', 'attribute', 'placement',
        'new_value', 'prior_value', 'mechanism_metric', 'mechanism_level', 'mechanism_target',
        'mechanism_from', 'check_date', 'outcome_keyword', 'outcome_rank', 'outcome_bound',
        'outcome_date', 'fallback', 'rationale']
PLC = {'Placement Top': 'placementTop', 'Placement Rest Of Search': 'placementRestOfSearch',
       'Placement Product Page': 'placementProductPage'}
ET = {'Campaign': 'campaign', 'Ad Group': 'ad_group', 'Product Ad': 'product_ad',
      'Keyword': 'keyword', 'Product Targeting': 'product_target',
      'Bidding Adjustment': 'campaign'}
num = lambda v: ('' if pd.isna(v) else (f'{v:g}' if float(v) % 1 else f'{int(v)}'))

GROUPS = [
    ('SP', sp, 'A', 'new SP campaigns — tranche A', '2026-09-16', '2026-09-23',
     'the 15 new SP campaigns spend to their $256/day cap within two weeks and return a blended '
     'cost per sale under 19.69',
     'pause any new campaign whose cost per sale passes 19.69 at the outcome read; hold the rest '
     'one further cycle before judging',
     'Fifteen campaigns opening the width the account does not have: room, size and head roots on '
     'Broad, the working Phrase default, Exact reserved for the 17 terms at 25%+ market '
     'conversion, four isolated Auto lanes and two product-targeting lanes. Every placement opens '
     'at 0% because the 23 August listing change contaminated the placement evidence.'),
    ('SP', sp, 'B', 'new SP campaigns — gated on the 52x84 reprice', '', '',
     'held until the 52x84 reprice lands; nothing uploads before then',
     'do not upload — the gate is the reprice, not a date. Re-read once it lands',
     'Two head-root campaigns at $65/day. Head terms only pay at the repriced 52x84; uploading '
     'before the reprice funds the most expensive terms at the wrong price.'),
    ('SP', sp, 'C', 'new SP campaigns — gated on the colour fix', '', '',
     'held until the lab dip and re-shot images land; nothing uploads before then',
     'do not upload — the gate is the colour fix. These route to the BLOCK-tier colourways',
     'Three campaigns at $53/day routed to the 96 inch drop, grey and floor-length lanes — the '
     'same colourways paused by the refund gate. They open when the refund cause is fixed, not '
     'before.'),
    ('SB', sb, 'A', 'new SB campaigns — gated on brand registry', '', '',
     'held until brand registry clears; SB cannot run without it',
     'do not upload — the gate is brand registry. SB also needs a logo in the Creative Asset '
     'Library and, with no Store, lands on Amazon\'s generated collection page',
     'Five Sponsored Brands campaigns at $64/day. SB was Phrase-only before; Broad opens the same '
     'width on the surface where the lead competitor runs 97% of its impressions.'),
    ('SB', sb, 'B', 'new SB campaigns — gated on reprice + brand registry', '', '',
     'held until both the 52x84 reprice and brand registry clear',
     'do not upload — two gates, both open before this ships',
     'One head-root SB campaign at $20/day, carrying both the SB and the reprice gate.'),
    ('SD', sd, 'A', 'new SD campaigns — tranche A', '2026-09-16', '2026-09-23',
     'the two product-targeting SD campaigns spend to their $20/day cap; the three audience '
     'campaigns cannot be measured until they are built in console',
     'build SL-LC-SD-VIEWS, SL-LC-SD-PURCHASE and SL-LC-SD-AUDIENCE in console — they carry no '
     'targeting expression, so no bulk can create them',
     'Five Sponsored Display campaigns at $39/day: two product-targeting lanes onto nine '
     'competitor ASINs and price-banded categories, plus views, purchase and in-market audience '
     'remarketing. The three audience campaigns have no expression in the decided file and the '
     'account holds no example to model from, so they are console-built.'),
]

rows = []
for product, src, tr, decision, mech_d, out_d, bound, fallback, rationale in GROUPS:
    sub = src[src.Tranche.str.startswith(tr)]
    if not len(sub):
        continue
    first = True
    for _, r in sub.iterrows():
        ent = r['Entity']
        attr = {'Campaign': 'create_campaign', 'Ad Group': 'create_ad_group',
                'Product Ad': 'create_product_ad', 'Keyword': 'create_keyword',
                'Product Targeting': 'create_target',
                'Bidding Adjustment': 'placement_multiplier'}[ent]
        if ent == 'Campaign':
            new = num(r['DailyBudget'])
        elif ent == 'Ad Group':
            new = num(r['Bid'])
        elif ent in ('Keyword', 'Product Targeting'):
            new = num(r['Bid'])
        elif ent == 'Bidding Adjustment':
            new = num(r['Percentage'])
        else:
            new = r['SKU'] if pd.notna(r['SKU']) else ''
        entity = (r['KeywordText'] if pd.notna(r['KeywordText'])
                  else (r['Expr'] if ent == 'Product Targeting' and pd.notna(r['Expr'])
                        else (r['SKU'] if pd.notna(r['SKU']) else '')))
        rows.append({
            'decision': decision, 'campaign': r['CampaignId'], 'entity_type': ET[ent],
            'entity': entity,
            'match_type': str(r['MatchType']).upper() if pd.notna(r['MatchType']) else '',
            'attribute': attr,
            'placement': PLC.get(r['Expr'], '') if ent == 'Bidding Adjustment' else '',
            'new_value': new, 'prior_value': 'none',
            'mechanism_metric': 'spend_wk', 'mechanism_level': 'campaign',
            'mechanism_target': num(r['DailyBudget'] * 7) if pd.notna(r['DailyBudget']) else '',
            'mechanism_from': '0', 'check_date': mech_d,
            'outcome_keyword': '', 'outcome_rank': '',
            'outcome_bound': bound if first else '', 'outcome_date': out_d if first else '',
            'fallback': fallback if first else '', 'rationale': rationale if first else '',
        })
        first = False

creates = pd.DataFrame(rows)[COLS]
OUT_PLAN = f'{S}/LIN_creates_change_loader_plan_JOSEPH_09Sep2026'
creates.to_csv(OUT_PLAN + '.csv', index=False)
with pd.ExcelWriter(OUT_PLAN + '.xlsx', engine='openpyxl') as xl:
    creates.to_excel(xl, sheet_name='change loader plan', index=False)

print('\ncreates in template:', len(creates))
print(creates.groupby('decision', sort=False).size().to_string())
