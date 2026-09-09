"""Decide the quilt action set and write it into the change loader template."""
import pandas as pd, numpy as np

S = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
OUT = f'{S}/SLQS_change_loader_plan_JOSEPH_09Sep2026'
CAP, LINE = 13.20, 15
MECH, OUTC = '2026-09-16', '2026-09-23'

COLS = ['decision', 'campaign', 'entity_type', 'entity', 'match_type', 'attribute', 'placement',
        'new_value', 'prior_value', 'mechanism_metric', 'mechanism_level', 'mechanism_target',
        'mechanism_from', 'check_date', 'outcome_keyword', 'outcome_rank', 'outcome_bound',
        'outcome_date', 'fallback', 'rationale']
PLC = {'Placement Top': 'placementTop', 'Placement Rest Of Search': 'placementRestOfSearch',
       'Placement Product Page': 'placementProductPage'}
ET = {'Campaign': 'campaign', 'Ad Group': 'ad_group', 'Product Ad': 'product_ad',
      'Keyword': 'keyword', 'Product Targeting': 'product_target', 'Bidding Adjustment': 'campaign'}

d = pd.read_pickle(f'{S}/QZ_Sponsored_Products_Campaigns.pkl')
n = lambda s: pd.to_numeric(s, errors='coerce')
for c in ['Clicks', 'Spend', 'Sales', 'Orders', 'Percentage', 'Bid', 'CPC', 'ACOS']:
    d[c] = n(d[c])
d['camp'] = d['Campaign Name (Informational only)']
d['cps'] = np.where(d.Orders > 0, d.Spend / d.Orders, np.nan)

mark = d['PLACEMTNT'].astype(str).str.strip()
d['is_pause'] = mark.str.upper().isin(['PAUSE', 'PAUSED'])
num = lambda v: ('' if pd.isna(v) else (f'{v:g}' if float(v) % 1 else f'{int(v)}'))
rows = []


def add(sub, decision, attribute, new_of, prior_of, mech, entity_of, bound, fallback, rationale,
        match_of=lambda r: '', plc_of=lambda r: ''):
    first = True
    for _, r in sub.iterrows():
        m, lvl, tgt, frm = mech(r)
        rows.append({'decision': decision, 'campaign': r.camp, 'entity_type': ET[r.Entity],
                     'entity': entity_of(r), 'match_type': match_of(r), 'attribute': attribute,
                     'placement': plc_of(r), 'new_value': new_of(r), 'prior_value': prior_of(r),
                     'mechanism_metric': m, 'mechanism_level': lvl, 'mechanism_target': tgt,
                     'mechanism_from': frm, 'check_date': MECH, 'outcome_keyword': '',
                     'outcome_rank': '', 'outcome_bound': bound if first else '',
                     'outcome_date': OUTC if first else '', 'fallback': fallback if first else '',
                     'rationale': rationale if first else ''})
        first = False


kw = lambda r: (r['Keyword Text'] if pd.notna(r['Keyword Text'])
                else (r['Product Targeting Expression']
                      if pd.notna(r['Product Targeting Expression']) else ''))
mt = lambda r: (str(r['Match Type']).upper() if pd.notna(r['Match Type']) else '')
spend_zero = lambda r: ('spend_wk', 'campaign', '0', num(round(r.Spend, 2)))

# ---- 1. confirmed pauses (your marks that the data backs) --------------------
p = d[d.is_pause & (d.Clicks >= LINE) & ((d.Orders == 0) | (d.cps > CAP))]
add(p, 'confirmed pause', 'state', lambda r: 'paused', lambda r: 'enabled', spend_zero,
    lambda r: kw(r) if r.Entity in ('Keyword', 'Product Targeting') else '',
    f'spend on these {len(p)} entities falls to 0; orders per week hold, because none of them is '
    'returning a sale inside the $13.20 cap',
    're-enable at the prior bid only where total product orders fall more than 15% below the '
    '7-day average over five consecutive days',
    'Each of these passed the 15-click line in the 7-day window and either returned no order at '
    'all or cost more than $13.20 per order — the forward-cash cap on this clearance product. '
    'Paused rather than re-bid because the gap is too wide for a bid step to close.',
    match_of=mt)

# ---- 2. placement premiums removed ------------------------------------------
ba = d[(d.Entity == 'Bidding Adjustment')]
pz = ba[(mark == '0') & (ba.Clicks >= LINE) & ((ba.Orders == 0) | (ba.cps > CAP))]
add(pz, 'placement premium removed', 'placement_multiplier', lambda r: '0',
    lambda r: num(r.Percentage),
    lambda r: ('cpc', 'placement', num(round(r.CPC / (1 + r.Percentage / 100), 2))
               if r.CPC > 0 else '0', num(round(r.CPC, 2))), lambda r: '',
    f'effective bid at these {len(pz)} placements falls back to the base bid; blended cost per '
    'order comes down without losing the base auction',
    'restore the prior percentage on any placement that drops below one order a week after the '
    'change',
    'These placements carry a premium that is not earning it: past the click line with either no '
    'orders or a cost per order above $13.20. The premium goes, the base bid stays.',
    plc_of=lambda r: PLC[r.Placement])

# ---- 3. placement premiums stepped down, not removed ------------------------
ps = ba[mark.isin(['20', '30']) & (ba.Clicks >= LINE)]
add(ps, 'placement premium stepped down', 'placement_multiplier',
    lambda r: mark.loc[r.name], lambda r: num(r.Percentage),
    lambda r: ('cpc', 'placement',
               num(round(r.CPC * (1 + float(mark.loc[r.name]) / 100) / (1 + r.Percentage / 100), 2))
               if r.CPC > 0 else '0', num(round(r.CPC, 2))), lambda r: '',
    'cost per order at these placements moves toward $13.20 while the volume they carry is kept',
    'take the modifier to 0% at the outcome read if cost per order has not come inside $13.20',
    'These two placements run just over the cap — $14.63 and $14.02 per order — on real volume, '
    'nineteen orders in the case of the auto catch-all. One step down rather than removal: the '
    'gap is small enough that a full cut would lose more volume than it saves.',
    plc_of=lambda r: PLC[r.Placement])


out = pd.DataFrame(rows)[COLS]
out.to_csv(OUT + '.csv', index=False)

# --- watch list: untouched, past the line, but not worth an action this cycle ---
camp = d[(d.Entity == 'Campaign') & (d.State == 'enabled')].copy()
touched = set(d.loc[d['PLACEMTNT'].notna() | d['BID'].notna(), 'camp'].dropna())
un = camp[~camp.camp.isin(touched) & (camp.Clicks >= LINE) &
          ((camp.Orders == 0) | (camp.cps > CAP))].copy()
un['why_no_action'] = np.where(
    un.Orders == 0, 'past the click line with no order, but on $4-$21 of spend — the line triggers '
                    'a review, not an automatic pause. Re-read 23 September.',
    'cost per order $13.36-$16.30, only just over the $13.20 cap, on real orders. Left alone rather '
    'than corrected — the gap is inside the noise on a 7-day window.')
un = un[['camp', 'Clicks', 'Spend', 'Orders', 'cps', 'why_no_action']]
un.columns = ['campaign', 'clicks_7d', 'spend_7d', 'orders_7d', 'cost_per_order', 'why_no_action']

with pd.ExcelWriter(OUT + '.xlsx', engine='openpyxl') as xl:
    out.to_excel(xl, sheet_name='change loader plan', index=False)
    un.sort_values('spend_7d', ascending=False).to_excel(xl, sheet_name='watch, no action', index=False)

print(out.groupby('decision', sort=False).size().to_string())
print('\nTOTAL ACTIONS', len(out))
print('watch list:', len(un), '| their spend %.2f' % un.spend_7d.sum())
print('\nattribute:', out.attribute.value_counts().to_dict())
print('entity_type:', out.entity_type.value_counts().to_dict())
