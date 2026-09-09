"""Verdict every annotation in the quilt sheet: aligned with the data, or not."""
import pandas as pd, numpy as np

S = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
CEILING, LINE = 13.20, 15

d = pd.read_pickle(f'{S}/QZ_Sponsored_Products_Campaigns.pkl')
n = lambda s: pd.to_numeric(s, errors='coerce')
for c in ['Clicks', 'Spend', 'Sales', 'Orders', 'Percentage', 'ACOS']:
    d[c] = n(d[c])
d['camp'] = d['Campaign Name (Informational only)']

mk = d['PLACEMTNT'].astype(str).str.strip().str.upper()
ann = d[d['PLACEMTNT'].notna() | d['NEGATIVE'].notna() | d['BID'].notna()].copy()
ann['mark'] = ann['PLACEMTNT'].astype(str).str.strip()
ann['is_pause'] = ann['mark'].str.upper().isin(['PAUSE', 'PAUSED'])

rows = []
for _, r in ann.iterrows():
    clicks, orders, spend = r.Clicks, r.Orders, r.Spend
    cps = spend / orders if orders else np.nan

    if r['NEGATIVE'] == 'Remove from negation':
        action, verdict, why = 'remove from negation', 'CANNOT VERIFY', (
            'marked on an Ad Group row with no keyword named, so there is no term to check against '
            'the search-term report — tell me which term each one refers to')
    elif r.is_pause:
        action = f'pause {r.Entity.lower()}'
        if clicks < LINE:
            verdict, why = 'NOT ALIGNED', (
                f'{int(clicks)} clicks is below the {LINE}-click line'
                + (f' and it converted once at ${cps:.2f}' if orders else ' — no verdict is possible yet'))
        elif orders == 0:
            verdict, why = 'aligned', f'{int(clicks)} clicks, no orders — past the line with nothing to show'
        elif cps > CEILING:
            verdict, why = 'aligned', f'${cps:.2f} per order against the ${CEILING:.2f} cap'
        else:
            verdict, why = 'NOT ALIGNED', f'converting at ${cps:.2f}, inside the ${CEILING:.2f} cap'
    elif r.Entity == 'Bidding Adjustment':
        new = float(r['mark']) if r['mark'].replace('.', '').isdigit() else np.nan
        old = r.Percentage
        action = f'placement {r.Placement} {old:.0f}% -> {new:.0f}%'
        if clicks < LINE:
            verdict, why = 'NOT ALIGNED', f'{int(clicks)} clicks at this placement is below the line'
        elif new == 0 and (orders == 0 or cps > CEILING):
            verdict, why = 'aligned', (f'{int(clicks)} clicks, ' +
                                       ('no orders' if orders == 0 else f'${cps:.2f} per order') +
                                       ' — the premium is not earning')
        elif new == 0:
            verdict, why = 'NOT ALIGNED', f'this placement converts at ${cps:.2f}, inside the cap'
        elif new > 0 and orders and cps <= CEILING:
            verdict, why = 'aligned', f'kept a premium on a placement converting at ${cps:.2f}'
        else:
            verdict, why = 'NOT ALIGNED', (f'premium held at {new:.0f}% on a placement '
                                           + ('with no orders' if orders == 0 else f'at ${cps:.2f}'))
    elif str(r['mark']).upper().startswith('BID') or pd.notna(r['BID']):
        action = 'reduce bid'
        if clicks < LINE:
            verdict, why = 'NOT ALIGNED', f'{int(clicks)} clicks is below the line'
        elif orders == 0 or cps > CEILING:
            verdict, why = 'aligned', (f'{int(clicks)} clicks, ' +
                                       ('no orders' if orders == 0 else f'${cps:.2f} per order') +
                                       ' — a cut rather than a pause keeps it alive')
        else:
            verdict, why = 'NOT ALIGNED', f'converting at ${cps:.2f}, inside the cap'
    else:
        action, verdict, why = str(r['mark']), 'CANNOT VERIFY', 'unrecognised annotation'

    rows.append({'campaign': r.camp, 'entity': r.Entity,
                 'target': (r['Keyword Text'] if pd.notna(r['Keyword Text'])
                            else (r['Product Targeting Expression']
                                  if pd.notna(r['Product Targeting Expression']) else '')),
                 'your_action': action, 'clicks_7d': int(clicks) if pd.notna(clicks) else 0,
                 'spend_7d': round(spend, 2) if pd.notna(spend) else 0,
                 'orders_7d': int(orders) if pd.notna(orders) else 0,
                 'cost_per_order': round(cps, 2) if orders else None,
                 'verdict': verdict, 'why': why})

v = pd.DataFrame(rows)
v['grp'] = np.where(v.your_action.str.startswith('pause'), 'pause',
                    np.where(v.your_action.str.startswith('placement'), 'placement',
                             np.where(v.your_action == 'reduce bid', 'bid', 'negation')))

print('TOTAL ANNOTATIONS:', len(v))
print()
print(pd.crosstab(v.grp, v.verdict, margins=True).to_string())
print()
print('--- NOT ALIGNED ---')
na = v[v.verdict == 'NOT ALIGNED']
print(na[['campaign', 'entity', 'target', 'your_action', 'clicks_7d', 'spend_7d', 'orders_7d',
          'cost_per_order', 'why']].to_string(index=False))

with pd.ExcelWriter(f'{S}/SLQS_action_check_09Sep2026.xlsx', engine='openpyxl', mode='a',
                    if_sheet_exists='replace') as xl:
    v.drop(columns='grp').to_excel(xl, sheet_name='every action verdicted', index=False)
