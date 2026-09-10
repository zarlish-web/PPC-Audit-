"""Build the linen Sponsored Display creates bulk, mirroring the account's own SD syntax.

Shapes copied verbatim from live campaigns in the account export:
  contextual product/category targeting -> Tactic T00020, Entity "Contextual Targeting"
  views / purchases remarketing         -> Tactic T00030, Entity "Audience Targeting"
"""
import pandas as pd, numpy as np

S = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
OUT = f'{S}/LIN_UPLOAD_SD_CREATES_10Sep2026.xlsx'
SHEET = 'Sponsored Display Campaigns'
START = '20260910'

tpl = pd.read_pickle(f'{S}/TPL_Sponsored_Display_Campaigns.pkl')
HEADER = list(tpl.columns)

sd = pd.read_pickle(f'{S}/LIN_New_SD_Campaigns.pkl')
SKUS = sd[sd.Entity == 'Product Ad'].SKU.dropna().unique().tolist()
ASINS = sd[(sd.Entity == 'Product Targeting') &
           sd.Expr.astype(str).str.startswith('asin=')].Expr.unique().tolist()

rows = []


def row(**kw):
    r = {c: None for c in HEADER}
    r['Product'] = 'Sponsored Display'
    r['Operation'] = 'create'
    r.update(kw)
    rows.append(r)


def build(cid, budget, tactic, cost_type, bid_opt, default_bid, targets, target_entity, bid):
    ag = f'{cid}-AG'
    row(Entity='Campaign', **{'Campaign ID': cid, 'Campaign Name': cid, 'Start Date': START,
                              'State': 'enabled', 'Tactic': tactic, 'Budget Type': 'Daily',
                              'Budget': budget, 'Cost Type': cost_type})
    row(Entity='Ad Group', **{'Campaign ID': cid, 'Ad Group ID': ag, 'Ad Group Name': ag,
                              'State': 'enabled', 'Ad Group Default Bid': default_bid,
                              'Bid Optimization': bid_opt})
    for sku in SKUS:
        row(Entity='Product Ad', **{'Campaign ID': cid, 'Ad Group ID': ag, 'State': 'enabled',
                                    'SKU': sku})
    for expr in targets:
        row(Entity=target_entity, **{'Campaign ID': cid, 'Ad Group ID': ag, 'State': 'enabled',
                                     'Bid': bid, 'Targeting Expression': expr})


# 1. competitor product targeting — contextual, exactly as the account runs it
build('SL-LC-SD-PT-COMPETITOR', 12.0, 'T00020', 'cpc', 'Optimize for conversions', 0.53,
      ASINS, 'Contextual Targeting', 0.55)

# 2. views remarketing on our own detail pages
build('SL-LC-SD-VIEWS', 8.0, 'T00030', 'cpc', 'Optimize for conversions', 0.53,
      ['views=(exact-product lookback=30)', 'views=(similar-product lookback=30)'],
      'Audience Targeting', 0.53)

# 3. purchase remarketing into the buyer base
build('SL-LC-SD-PURCHASE', 5.0, 'T00030', 'cpc', 'Optimize for conversions', 0.53,
      ['purchases=(exact-product lookback=30)', 'purchases=(related-product lookback=30)'],
      'Audience Targeting', 0.53)

out = pd.DataFrame(rows)[HEADER]
for c in ['Budget', 'Bid', 'Ad Group Default Bid']:
    out[c] = pd.to_numeric(out[c], errors='coerce').round(2)
out = out.astype(object).where(pd.notna(out), None)

with pd.ExcelWriter(OUT, engine='openpyxl') as xl:
    out.to_excel(xl, sheet_name=SHEET, index=False)
    ws = xl.sheets[SHEET]
    for col in ('O', 'P'):                     # Start Date, End Date -> text
        for cell in ws[col]:
            cell.number_format = '@'

print('rows', len(out), '| by entity:', out.Entity.value_counts().to_dict())
print('header matches the account export:', HEADER == list(tpl.columns), '| columns', len(HEADER))
print('sheets: 1 |', SHEET)
print('End Date non-null:', out['End Date'].notna().sum(),
      '| State blank:', out['State'].isna().sum())
print('SKUs per campaign:', len(SKUS), '| competitor ASINs:', len(ASINS))
