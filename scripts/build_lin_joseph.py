"""Map the corrected linen changes into Joseph's change loader plan template.

Conventions taken from the template's own example rows:
  - attribute vocabulary: state / bid / budget / placement_multiplier / create_negative
  - placement in Amazon camelCase: placementTop, placementRestOfSearch
  - entity blank on campaign-level rows; the keyword text or target expression otherwise
  - decision repeats on every row of a group
  - mechanism_metric/level/target/from and check_date are PER ROW
  - outcome_bound, outcome_date, fallback and rationale sit on the group's first row
  - mechanism_target is scaled proportionally from the change, as the template's own
    bid example does: bid 2.06 -> 1.85 (x0.898) against cpc 4.37 -> 3.92 (x0.897)
  - values are plain numbers, no currency symbols
"""
import pandas as pd, numpy as np

SCRATCH = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
OUT = f'{SCRATCH}/LIN_change_loader_plan_JOSEPH_09Sep2026'
MECH, OUTC = '2026-09-16', '2026-09-23'

COLS = ['decision', 'campaign', 'entity_type', 'entity', 'match_type', 'attribute', 'placement',
        'new_value', 'prior_value', 'mechanism_metric', 'mechanism_level', 'mechanism_target',
        'mechanism_from', 'check_date', 'outcome_keyword', 'outcome_rank', 'outcome_bound',
        'outcome_date', 'fallback', 'rationale']

PLACEMENT = {'Placement Top': 'placementTop',
             'Placement Rest Of Search': 'placementRestOfSearch',
             'Placement Product Page': 'placementProductPage'}

df = pd.read_pickle(f'{SCRATCH}/LIN_fb.pkl')
n = lambda s: pd.to_numeric(s, errors='coerce')
for c in ['Bid', 'New Bids', 'Daily Budget', 'New Budget', 'Percentage', 'New Percentage',
          'LW Spend', 'LW Clicks', 'CPC']:
    df[c] = n(df[c])
act = df['Action'].fillna('')

num = lambda v: ('' if pd.isna(v) else (f'{v:g}' if float(v) % 1 else f'{int(v)}'))
rows = []


def emit(sub, decision, attribute, new_of, prior_of, mech, entity_of,
         bound, fallback, rationale, match_of=lambda r: '', placement_of=lambda r: ''):
    first = True
    for _, r in sub.iterrows():
        metric, level, target, frm = mech(r)
        rows.append({
            'decision': decision,
            'campaign': r['Campaign Name (Informational only)'],
            'entity_type': {'Campaign': 'campaign', 'Keyword': 'keyword',
                            'Product Targeting': 'product_target',
                            'Bidding Adjustment': 'campaign'}[r['Entity']],
            'entity': entity_of(r), 'match_type': match_of(r), 'attribute': attribute,
            'placement': placement_of(r), 'new_value': new_of(r), 'prior_value': prior_of(r),
            'mechanism_metric': metric, 'mechanism_level': level,
            'mechanism_target': target, 'mechanism_from': frm, 'check_date': MECH,
            'outcome_keyword': '', 'outcome_rank': '',
            'outcome_bound': bound if first else '',
            'outcome_date': OUTC if first else '',
            'fallback': fallback if first else '',
            'rationale': rationale if first else '',
        })
        first = False


# mechanism helpers -----------------------------------------------------------
spend_to_zero = lambda r: ('spend_wk', 'campaign', '0', num(round(r['LW Spend'], 2)))
cpc_scaled = lambda ratio: (lambda r: ('cpc', 'target',
                                       num(round(r['CPC'] * ratio(r), 2)) if r['CPC'] > 0 else '0',
                                       num(round(r['CPC'], 2))))
kw_text = lambda r: (r['Keyword Text'] if pd.notna(r['Keyword Text'])
                     else (r['Product Targeting Expression']
                           if pd.notna(r['Product Targeting Expression']) else ''))
mt = lambda r: (str(r['Match Type']).upper() if pd.notna(r['Match Type']) else '')

# 1 refund gate pause ---------------------------------------------------------
emit(df[(df.Entity == 'Campaign') & (act == 'Pause — refund gate')],
     'refund gate pause', 'state', lambda r: 'paused', lambda r: 'enabled',
     spend_to_zero, lambda r: '',
     'spend on these 215 campaigns falls to 0; units cleared per week holds, because these SKUs '
     'return 37.5-45.5% of what they sell',
     'release in tranche C when the lab dip and re-shot images land; re-enable at the prior budget '
     'and read refund rate before any bid move',
     '12 BLOCK-tier SKUs refund at 37.5-45.5% on a reliable sample. Effective ad cost per unit '
     'actually cleared is $20.66-$23.67 against a $19.69 ceiling, so every incremental unit loses '
     'money. Return reason on file is "colour lighter than pictures" and these are the affected '
     'colourways and drops.')

# 2 net-negative pause --------------------------------------------------------
emit(df[(df.Entity == 'Campaign') & (act == 'Pause campaign')],
     'net-negative pause', 'state', lambda r: 'paused', lambda r: 'enabled',
     spend_to_zero, lambda r: '',
     'spend on these 82 campaigns falls to 0; the $32.99 of sales they carried is already '
     'net-negative after returns, so contribution improves',
     'if total product orders fall more than 15% below the 30-day average over any 5 consecutive '
     'days, re-enable only the campaigns that held an order, at the prior budget',
     'These 82 campaigns are net-negative after refunds: 1 order and $32.99 of sales against '
     '$72.95 of spend and 3 recorded returns.')

# 3 refund watch budget cut (corrected to the $5.00 floor) ---------------------
emit(df[(df.Entity == 'Campaign') & act.str.startswith('Cut budget') & (df['Daily Budget'] > 5)],
     'refund watch budget cut', 'budget', lambda r: '5', lambda r: num(r['Daily Budget']),
     lambda r: ('spend_wk', 'campaign', '35', num(round(r['LW Spend'], 2))), lambda r: '',
     'the weekly cap on these 12 campaigns falls from 70 to 35 against a run rate well under it; '
     'delivered spend does not move, because utilisation was 1.5% and the cap was never binding',
     'if a FLOOR SKU drops below 5 units a week, restore its campaigns to the prior budget rather '
     'than raising bids',
     '18 FLOOR-tier SKUs refund at 25.0-30.0%, an effective $17.21-$17.75 per unit cleared against '
     'the $19.69 ceiling — marginal rather than loss-making. Kept live at a bounded budget rather '
     'than paused. Corrected 8 September: the decided file cut all 73 to $3.00, below the $5.00 '
     'floor with no override stated; the 61 already at $5.00 are dropped, since a cut to a cap the '
     'lane never reached releases nothing.')

# 4 budget right-size ---------------------------------------------------------
emit(df[(df.Entity == 'Campaign') & act.str.startswith('Set budget') &
        (df['New Budget'] != df['Daily Budget'])],
     'budget right-size', 'budget', lambda r: num(r['New Budget']),
     lambda r: num(r['Daily Budget']),
     lambda r: ('spend_wk', 'campaign', num(round(r['New Budget'] * 7, 2)),
                num(round(r['LW Spend'], 2))), lambda r: '',
     'no change in delivered spend — portfolio utilisation was 1.5%, so these caps were never '
     'reached; the cap is squared to required budget so the number means something next cycle',
     'if any of these campaigns runs out of budget before 6pm on two consecutive days, restore the '
     'prior cap and re-read',
     'Budget right-sized to required budget on 12 FUND-tier SKUs (0-16.1% refunds). Utilisation '
     'across the portfolio was 1.5%, so budget was never the constraint — this squares the caps, '
     'it does not release spend.')

# 5/6/7 bids ------------------------------------------------------------------
kt = df[df.Entity.isin(['Keyword', 'Product Targeting'])]
ch = kt[kt['New Bids'].notna() & kt['Bid'].notna() & (kt['New Bids'] != kt['Bid'])]
ratio = lambda r: r['New Bids'] / r['Bid']
rw = ch[(ch['New Bids'] < ch['Bid']) & ch['Action'].astype(str).str.contains('refund watch')]
cz = ch[(ch['New Bids'] < ch['Bid']) & ~ch['Action'].astype(str).str.contains('refund watch')]
rz = ch[ch['New Bids'] > ch['Bid']]

emit(rw, 'refund watch bid cut', 'bid', lambda r: num(r['New Bids']), lambda r: num(r['Bid']),
     cpc_scaled(ratio), kw_text,
     'average bid on these 67 targets falls from 0.52 to 0.32; cost per unit cleared on the FLOOR '
     'SKUs comes back under the 19.69 ceiling',
     'restore the prior bid on any target that holds its orders and comes in under $19.69 per unit '
     'cleared for two consecutive weeks',
     'Parent campaign is on the refund watch list. Bids held down until the colour fix lands, so '
     'the lane keeps its placements without funding units that come back.', match_of=mt)

emit(cz, 'ceiling bid cut', 'bid', lambda r: num(r['New Bids']), lambda r: num(r['Bid']),
     cpc_scaled(ratio), kw_text,
     'cost per acquisition on these 22 targets moves toward the 19.69 ceiling; the thin ones are '
     'cut 40% and re-read rather than paused',
     'pause any target still above $19.69 CPA at the outcome read; re-read the thin ones after the '
     'post-listing-change window rather than judging them now',
     'These 22 targets convert above the $19.69 ceiling or are too thin to judge (2-5 clicks). Cut '
     '40% rather than paused — the converting ones are demonstrated demand and the thin ones have '
     'not had their chance.', match_of=mt)

emit(rz, 'bid raise to ceiling', 'bid', lambda r: num(r['New Bids']), lambda r: num(r['Bid']),
     cpc_scaled(ratio), kw_text,
     'average bid on these 55 targets rises from 0.55 to 0.70; clicks and orders on the FUND SKUs '
     'rise while CPA stays inside 19.69',
     'roll the bid back one step on any target whose CPA passes $19.69 at the outcome read',
     'These targets convert inside the $19.69 ceiling — one at $4.80 CPA — and only 14 keywords on '
     'this product do. Auto is the only lane with no keyword-selection risk and it is under-bid at '
     '0 orders on $2.12 of close-match spend.', match_of=mt)

# 8 placement modifier reset --------------------------------------------------
ba = df[df.Entity == 'Bidding Adjustment']
pl = ba[ba['New Percentage'].notna() & (ba['New Percentage'] != ba['Percentage'])]
emit(pl, 'placement modifier reset', 'placement_multiplier', lambda r: '0',
     lambda r: num(r['Percentage']),
     lambda r: ('cpc', 'placement',
                num(round(r['CPC'] / (1 + r['Percentage'] / 100), 2)) if r['CPC'] > 0 else '0',
                num(round(r['CPC'], 2))), lambda r: '',
     'effective bid at Top of Search and Rest of Search falls back to the base bid on 627 '
     'modifiers averaging 129% (max 275%); blended CPC falls and spend stops concentrating at '
     'Top of Search',
     'rebuild modifiers per campaign from a clean read taken after the outcome date, once the '
     '23 August listing change has washed through — never as a blanket value',
     'Placement evidence is contaminated by the 23 August listing change and a conflicting earlier '
     'read, so no modifier can be justified from current data. All non-zero modifiers go to 0% and '
     'are rebuilt from clean evidence next cycle. The mechanism target is each placement\'s own '
     'observed CPC divided by its current multiplier — the base the modifier was scaling.',
     placement_of=lambda r: PLACEMENT[r['Placement']])

out = pd.DataFrame(rows)[COLS]
out.to_csv(OUT + '.csv', index=False)
with pd.ExcelWriter(OUT + '.xlsx', engine='openpyxl') as xl:
    out.to_excel(xl, sheet_name='change loader plan', index=False)

print(out.groupby('decision', sort=False).size().to_string())
print('\nTOTAL', len(out))
print('\nattribute:', out.attribute.value_counts().to_dict())
print('placement:', out.placement.value_counts().to_dict())
print('entity_type:', out.entity_type.value_counts().to_dict())
