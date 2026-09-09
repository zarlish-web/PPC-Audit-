"""Cut the upload-ready Amazon SP bulk from the corrected LIN change loader plan.

Update rows only, no creates. Values are written into the live Amazon columns and
Operation is set to update; every ID comes from the source export.
"""
import pandas as pd, numpy as np

SCRATCH = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
OUT = f'{SCRATCH}/LIN_UPLOAD_SP_UPDATES_08Sep2026.xlsx'
SHEET = 'Sponsored Products Campaigns'

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
assert len(HEADER) == 54, len(HEADER)

df = pd.read_pickle(f'{SCRATCH}/LIN_fb.pkl')
n = lambda s: pd.to_numeric(s, errors='coerce')
for c in ['Bid', 'New Bids', 'Daily Budget', 'New Budget', 'Percentage', 'New Percentage', 'Clicks', 'Spend']:
    df[c] = n(df[c])
act = df['Action'].fillna('')

blocks, console = [], []


def take(mask, apply):
    sub = df[mask].copy()
    apply(sub)
    blocks.append(sub)
    return sub


# --- campaign state pauses (297) ---------------------------------------------
# Budget is blanked so a pause row changes exactly one field. Three of these campaigns already
# run at $3.00 live — pre-existing, not from this cycle — and re-sending that value would
# re-assert a sub-floor budget the plan never decided.
take((df.Entity == 'Campaign') & act.str.lower().str.startswith('pause'),
     lambda s: (s.__setitem__('State', 'paused'), s.__setitem__('Daily Budget', None)))

# --- daily budget: 65 right-sized + 12 refund-watch cuts to the $5.00 floor ---
take((df.Entity == 'Campaign') & act.str.startswith('Set budget') &
     (df['New Budget'] != df['Daily Budget']),
     lambda s: s.__setitem__('Daily Budget', s['New Budget']))
take((df.Entity == 'Campaign') & act.str.startswith('Cut budget') & (df['Daily Budget'] > 5.00),
     lambda s: s.__setitem__('Daily Budget', 5.00))

# --- bids (144), minus any keyword-group target: console only ----------------
kt = df[df.Entity.isin(['Keyword', 'Product Targeting'])]
bidmask = (df.index.isin(kt.index) & df['New Bids'].notna() & df['Bid'].notna() &
           (df['New Bids'] != df['Bid']))
# Dropped 9 Sep: six ceiling cuts sat on targets with zero clicks and zero spend — a performance
# verdict on no evidence. One of them was the keyword-group target on D-LC-TESTING-NEW-FEATURE,
# which Bulksheets rejects whatever the bid says, so nothing is left needing a console edit.
# Refund watch cuts are a policy hold on FLOOR SKUs, not a performance read, and are untouched.
dropped = (bidmask & (df['New Bids'] < df['Bid']) & (df['Clicks'] == 0) & (df['Spend'] == 0) &
           ~df['Action'].astype(str).str.contains('refund watch'))
take(bidmask & ~dropped, lambda s: s.__setitem__('Bid', s['New Bids']))

# --- placement modifiers (627) -----------------------------------------------
take((df.Entity == 'Bidding Adjustment') & df['New Percentage'].notna() &
     (df['New Percentage'] != df['Percentage']),
     lambda s: s.__setitem__('Percentage', s['New Percentage']))

up = pd.concat(blocks, ignore_index=True)
up['Operation'] = 'update'

# --- typing per canon §4 ------------------------------------------------------
for c in HEADER:
    if c not in up.columns:
        up[c] = None
up = up[HEADER]

for c in ['Campaign ID', 'Ad Group ID', 'Portfolio ID', 'Ad ID', 'Keyword ID',
          'Product Targeting ID']:
    up[c] = up[c].apply(lambda v: str(int(v)) if pd.notna(v) else None)

up['Start Date'] = up['Start Date'].apply(lambda v: f'{int(v)}' if pd.notna(v) else None)
up['End Date'] = None

# State on every row (rule 3); placement rows inherit their campaign's decided state.
camp_state = (up[up.Entity == 'Campaign'].set_index('Campaign ID')['State'].to_dict())
live_state = (df[df.Entity == 'Campaign']
              .assign(cid=lambda d: d['Campaign ID'].astype(str))
              .set_index('cid')['Campaign State (Informational only)'].to_dict())
up['State'] = [s if pd.notna(s) and str(s).strip() else
               camp_state.get(cid, live_state.get(cid, 'enabled'))
               for s, cid in zip(up['State'], up['Campaign ID'])]

# Product Targeting updates: the ID identifies the target, the expression must be blank.
up.loc[up.Entity == 'Product Targeting', 'Product Targeting Expression'] = None

# Keyword updates: the Keyword ID identifies the row and Keyword Text is not a required field
# (canon §2). Three live keywords carry a "+" ("blackout curtains 90+ inches long"); rewriting the
# text of an existing keyword is not a bid change, so the text is dropped rather than cleaned.
# The change loader plan carries every keyword by name for reading.
up.loc[up.Entity == 'Keyword', 'Keyword Text'] = None

for c in ['Daily Budget', 'Bid', 'Ad Group Default Bid', 'Percentage']:
    up[c] = n(up[c]).round(2)

# Performance and serving-status columns are read-only; strip them from an update file.
for c in HEADER:
    if '(Informational only)' in c or c in ['Impressions', 'Clicks', 'Click-through Rate', 'Spend',
                                            'Sales', 'Orders', 'Units', 'Conversion Rate', 'ACOS',
                                            'CPC', 'ROAS']:
        up[c] = None

up = up.astype(object).where(pd.notna(up), None)

with pd.ExcelWriter(OUT, engine='openpyxl') as xl:
    up.to_excel(xl, sheet_name=SHEET, index=False)
    ws = xl.sheets[SHEET]
    for col in ('O', 'P'):                       # Start Date, End Date -> text
        for cell in ws[col]:
            cell.number_format = '@'
    for col in ('D', 'E', 'F', 'G', 'H', 'I'):   # numeric IDs -> text
        for cell in ws[col]:
            cell.number_format = '@'

print('rows', len(up), '| by entity:'); print(up.Entity.value_counts().to_string())
print('\nsheets: 1 |', SHEET, '| columns', len(up.columns))
print('State blank:', up.State.isna().sum(), '| End Date non-null:', up['End Date'].notna().sum())
print('console-only rows routed out:', sum(len(c) for c in console))
if console:
    pd.concat(console)[['Campaign Name (Informational only)', 'Product Targeting Expression',
                        'Bid', 'New Bids']].to_csv(f'{SCRATCH}/LIN_console_only_08Sep2026.csv',
                                                   index=False)
