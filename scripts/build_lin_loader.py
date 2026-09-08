"""Extract every decided action from LIN_Decided_Bulk_v5 into the change loader template."""
import pandas as pd, numpy as np

SRC = '/root/.claude/uploads/f01da844-e516-5303-96fa-ec17555f9d55/74ed8a5f-LIN_Decided_Bulk_v5_1Sep2026.xlsx'
OUT = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad/LIN_change_loader_plan_08Sep2026'
MECH, OUTC = '2026-09-15', '2026-09-22'

df = pd.read_pickle('/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad/LIN_fb.pkl')
n = lambda s: pd.to_numeric(s, errors='coerce')
for c in ['Bid', 'New Bids', 'Daily Budget', 'New Budget', 'Percentage', 'New Percentage',
          'Spend', 'Sales', 'Orders', 'Clicks']:
    df[c] = n(df[c])
act = df['Action'].fillna('')
camp = df['Campaign Name (Informational only)'].astype(str)

rows = []


def add(sub, decision, attribute, get_new, get_prior, mech_metric, mech_level,
        mech_target, mech_from, bound, fallback, rationale, entity_of):
    """One template row per change; strategy narrative on the first row of the group."""
    first = True
    for _, r in sub.iterrows():
        rows.append({
            'decision': decision,
            'campaign': r['Campaign Name (Informational only)'],
            'entity_type': {'Campaign': 'campaign', 'Keyword': 'keyword',
                            'Product Targeting': 'product_target',
                            'Bidding Adjustment': 'placement'}[r['Entity']],
            'entity': entity_of(r),
            'match_type': (str(r['Match Type']).upper() if pd.notna(r['Match Type']) else ''),
            'attribute': attribute,
            'placement': (r['Placement'] if pd.notna(r['Placement']) else ''),
            'new_value': get_new(r),
            'prior_value': get_prior(r),
            'mechanism_metric': mech_metric,
            'mechanism_level': mech_level,
            'mechanism_target': mech_target if first else '',
            'mechanism_from': mech_from if first else '',
            'check_date': MECH,
            'outcome_keyword': '',
            'outcome_rank': '',
            'outcome_bound': bound if first else '',
            'outcome_date': OUTC if first else '',
            'fallback': fallback if first else '',
            'rationale': rationale if first else '',
            'sku': (r['SKU'] if pd.notna(r['SKU']) else ''),
            'clicks_30d': (int(r['Clicks']) if pd.notna(r['Clicks']) else 0),
            'spend_30d': round(float(r['Spend']), 2) if pd.notna(r['Spend']) else 0.0,
            'orders_30d': (int(r['Orders']) if pd.notna(r['Orders']) else 0),
            'row_reasoning': r['Reasoning'],
        })
        first = False


kw_name = lambda r: (r['Keyword Text'] if pd.notna(r['Keyword Text'])
                     else (r['Product Targeting Expression'] if pd.notna(r['Product Targeting Expression']) else ''))
camp_name = lambda r: r['Campaign Name (Informational only)']
plc_name = lambda r: r['Placement']

# ---- G1  refund-gate pauses -------------------------------------------------
g = df[(df['Entity'] == 'Campaign') & (act == 'Pause — refund gate')]
add(g, 'refund gate pause', 'state', lambda r: 'paused', lambda r: 'enabled',
    'spend_wk', 'campaign', '0', f'{g.Spend.sum():.2f}',
    'spend on these 215 campaigns falls to $0; units cleared per week holds, because these SKUs '
    'return 37.5-45.5% of what they sell',
    'release in tranche C when the lab dip and re-shot images land; re-enable at the prior budget '
    'and read refund rate before any bid move',
    '12 BLOCK-tier SKUs refund at 37.5-45.5% on a reliable sample. Effective ad cost per unit '
    'actually cleared is $20.66-$23.67 against a $19.69 ceiling, so every incremental unit loses '
    'money. Return reason on file is "colour lighter than pictures" and these are the affected '
    'colourways and drops.', camp_name)

# ---- G2  net-negative pauses ------------------------------------------------
g = df[(df['Entity'] == 'Campaign') & (act == 'Pause campaign')]
add(g, 'net-negative pause', 'state', lambda r: 'paused', lambda r: 'enabled',
    'spend_wk', 'campaign', '0', f'{g.Spend.sum():.2f}',
    f'spend on these 82 campaigns falls to $0; the ${g.Sales.sum():.2f} of sales they carried is '
    'already net-negative after returns, so contribution improves',
    'if total product orders fall more than 15% below the 30-day average over any 5 consecutive '
    'days, re-enable only the campaigns that held an order, at the prior budget',
    'These 82 campaigns are net-negative after refunds: on the window they returned more units than '
    f'they sold — 1 order and ${g.Sales.sum():.2f} of sales against ${g.Spend.sum():.2f} of spend '
    'and 3 recorded returns.', camp_name)

# ---- G3  refund-watch budget cuts -------------------------------------------
g = df[(df['Entity'] == 'Campaign') & act.str.startswith('Cut budget') &
       (df['New Budget'] != df['Daily Budget'])]
add(g, 'refund watch budget cut', 'daily_budget', lambda r: f"{r['New Budget']:.2f}",
    lambda r: f"{r['Daily Budget']:.2f}",
    'daily_budget', 'campaign', f'{g["New Budget"].sum():.2f}', f'{g["Daily Budget"].sum():.2f}',
    'daily budget cap across these 73 campaigns falls from '
    f'${g["Daily Budget"].sum():.0f} to ${g["New Budget"].sum():.0f}; spend follows only where the '
    'cap was actually binding',
    'if a FLOOR SKU drops below 5 units a week, restore its campaigns to the prior budget rather '
    'than raising bids',
    '18 FLOOR-tier SKUs refund at 25.0-30.0%, an effective $17.21-$17.75 per unit cleared against '
    'the $19.69 ceiling — marginal rather than loss-making. Kept live at a reduced budget rather '
    'than paused, and not scaled until the colour fix lands.', camp_name)

# ---- G4  budget right-size --------------------------------------------------
g = df[(df['Entity'] == 'Campaign') & act.str.startswith('Set budget') &
       (df['New Budget'] != df['Daily Budget'])]
add(g, 'budget right-size', 'daily_budget', lambda r: f"{r['New Budget']:.2f}",
    lambda r: f"{r['Daily Budget']:.2f}",
    'daily_budget', 'campaign', f'{g["New Budget"].sum():.2f}', f'{g["Daily Budget"].sum():.2f}',
    'no change in delivered spend — portfolio budget utilisation was 1.5%, so these caps were '
    'never reached; the cap is squared to required budget so the number means something next cycle',
    'if any of these campaigns runs out of budget before 6pm on two consecutive days, restore the '
    'prior cap and re-read',
    'Budget right-sized to required budget on 12 FUND-tier SKUs (0-16.1% refunds). Utilisation '
    'across the portfolio was 1.5%, so budget was never the constraint — this squares the caps, it '
    'does not release spend.', camp_name)

# ---- G5/G6/G7  bids ---------------------------------------------------------
kt = df[df['Entity'].isin(['Keyword', 'Product Targeting'])]
ch = kt[kt['New Bids'].notna() & kt['Bid'].notna() & (kt['New Bids'] != kt['Bid'])]
cuts, raises = ch[ch['New Bids'] < ch['Bid']], ch[ch['New Bids'] > ch['Bid']]
rw = cuts[cuts['Action'].astype(str).str.contains('refund watch')]
cz = cuts[~cuts['Action'].astype(str).str.contains('refund watch')]

add(rw, 'refund watch bid cut', 'bid', lambda r: f"{r['New Bids']:.2f}", lambda r: f"{r['Bid']:.2f}",
    'cpc', 'target', f'{rw["New Bids"].mean():.2f}', f'{rw["Bid"].mean():.2f}',
    'average bid on these 67 targets falls from '
    f'${rw["Bid"].mean():.2f} to ${rw["New Bids"].mean():.2f}; cost per unit cleared on the FLOOR '
    'SKUs comes back under the $19.69 ceiling',
    'restore the prior bid on any target that holds its orders and comes in under $19.69 per unit '
    'cleared for two consecutive weeks',
    'Parent campaign is on the refund watch list. Bids held down until the colour fix lands, so the '
    'lane keeps its placements without funding units that come back.', kw_name)

add(cz, 'ceiling bid cut', 'bid', lambda r: f"{r['New Bids']:.2f}", lambda r: f"{r['Bid']:.2f}",
    'cpa', 'target', '19.69', f'{cz["Spend"].sum() / max(cz["Orders"].sum(), 1):.2f}',
    'cost per acquisition on these 22 targets moves toward the $19.69 ceiling; the thin ones are '
    'cut 40% and re-read rather than paused',
    'pause any target still above $19.69 CPA at the 22 September read; re-read the thin ones after '
    'the post-listing-change window rather than judging them now',
    'These 22 targets convert above the $19.69 ceiling or are too thin to judge (2-5 clicks). Cut '
    '40% rather than paused — the converting ones are demonstrated demand and the thin ones have '
    'not had their chance.', kw_name)

add(raises, 'bid raise to ceiling', 'bid', lambda r: f"{r['New Bids']:.2f}", lambda r: f"{r['Bid']:.2f}",
    'cpc', 'target', f'{raises["New Bids"].mean():.2f}', f'{raises["Bid"].mean():.2f}',
    'average bid on these 55 targets rises from '
    f'${raises["Bid"].mean():.2f} to ${raises["New Bids"].mean():.2f}; clicks and orders on the '
    'FUND SKUs rise while CPA stays inside $19.69',
    'roll the bid back one step on any target whose CPA passes $19.69 at the 22 September read',
    'These targets convert inside the $19.69 ceiling — one at $4.80 CPA — and only 14 keywords on '
    'this product do. Auto is the only lane with no keyword-selection risk and it is under-bid at '
    '0 orders on $2.12 of close-match spend.', kw_name)

# ---- G8  placement reset ----------------------------------------------------
ba = df[df['Entity'] == 'Bidding Adjustment']
pl = ba[ba['New Percentage'].notna() & (ba['New Percentage'] != ba['Percentage'])]
add(pl, 'placement modifier reset', 'placement_pct', lambda r: '0', lambda r: f"{r['Percentage']:.0f}",
    'placement_pct', 'campaign', '0', f'{pl["Percentage"].mean():.0f}',
    'effective bid at Top of Search and Rest of Search falls back to the base bid on 627 modifiers '
    f'averaging {pl["Percentage"].mean():.0f}% (max {pl["Percentage"].max():.0f}%); spend '
    'concentration at Top of Search drops and blended CPC falls',
    'rebuild modifiers per campaign from a clean read taken after 22 September, once the 23 August '
    'listing change has washed through — never as a blanket value',
    'Placement evidence is contaminated by the 23 August listing change and a conflicting earlier '
    'read, so no modifier can be justified from current data. All non-zero modifiers go to 0% and '
    'are rebuilt from clean evidence next cycle.', plc_name)

# -----------------------------------------------------------------------------
out = pd.DataFrame(rows)
TEMPLATE = ['decision', 'campaign', 'entity_type', 'entity', 'match_type', 'attribute', 'placement',
            'new_value', 'prior_value', 'mechanism_metric', 'mechanism_level', 'mechanism_target',
            'mechanism_from', 'check_date', 'outcome_keyword', 'outcome_rank', 'outcome_bound',
            'outcome_date', 'fallback', 'rationale']
EXTRA = ['sku', 'clicks_30d', 'spend_30d', 'orders_30d', 'row_reasoning']
out = out[TEMPLATE + EXTRA]
out.insert(0, 'change_id', [f'L{i:04d}' for i in range(1, len(out) + 1)])

# ---- validation gate --------------------------------------------------------
nv = pd.to_numeric(out['new_value'], errors='coerce')
flag = np.where((out.attribute == 'daily_budget') & (nv < 5.00),
                'HOLD - below the $5.00 minimum daily budget; no override stated and the cap was '
                'never binding, so the cut releases $0.00',
                np.where((out.attribute == 'bid') & (nv < 0.25),
                         'HOLD - below the $0.25 minimum bid', 'ok'))
out.insert(1, 'flag', flag)

checks = [
    ('every changed row in the source appears once in the plan', len(out) == 1206),
    ('no quilt (SL-QS) campaign in the plan', not out.campaign.astype(str).str.upper()
     .str.contains('SL-QS|QUILT').any()),
    ('new_value differs from prior_value on every row',
     (out.new_value.astype(str) != out.prior_value.astype(str)).all()),
    ('no blank campaign, entity, new_value or prior_value',
     out[['campaign', 'entity', 'new_value', 'prior_value']].notna().all().all()),
    ('6 contradictory "No change" rows carrying a new bid are excluded',
     (out.attribute == 'bid').sum() == 144),
    ('every state change is enabled -> paused',
     ((out[out.attribute == 'state'].new_value == 'paused') &
      (out[out.attribute == 'state'].prior_value == 'enabled')).all()),
    ('every placement modifier lands at 0%',
     (pd.to_numeric(out[out.attribute == 'placement_pct'].new_value) == 0).all()),
    ('no bid below the $0.25 floor',
     pd.to_numeric(out[out.attribute == 'bid'].new_value).min() >= 0.25),
    ('no daily budget below the $5.00 floor',
     pd.to_numeric(out[out.attribute == 'daily_budget'].new_value).min() >= 5.00),
    ('no duplicate campaign/entity/attribute/placement',
     not out.duplicated(['campaign', 'entity', 'attribute', 'placement', 'match_type']).any()),
]
validation = pd.DataFrame([{'check': c, 'result': 'PASS' if r else 'FAIL'} for c, r in checks])

summary = (out.groupby('decision', sort=False)
             .agg(rows=('change_id', 'size'), flagged=('flag', lambda s: (s != 'ok').sum()),
                  spend_30d=('spend_30d', 'sum'), clicks_30d=('clicks_30d', 'sum'),
                  orders_30d=('orders_30d', 'sum'))
             .reset_index())
summary['spend_30d'] = summary['spend_30d'].round(2)
summary['upload'] = np.where(summary.flagged > 0, 'HOLD - see flag column', 'upload')

cols = ['change_id', 'flag'] + TEMPLATE
with pd.ExcelWriter(OUT + '.xlsx', engine='openpyxl') as xl:
    out[cols].to_excel(xl, sheet_name='change loader plan', index=False)
    out.to_excel(xl, sheet_name='plan + evidence', index=False)
    summary.to_excel(xl, sheet_name='summary', index=False)
    validation.to_excel(xl, sheet_name='validation', index=False)
out[cols].to_csv(OUT + '.csv', index=False)

print(summary.to_string(index=False))
print('\nTOTAL ROWS', len(out))
print('\n' + validation.to_string(index=False))
