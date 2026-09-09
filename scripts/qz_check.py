"""Check the quilt action annotations for internal consistency and against performance."""
import pandas as pd, numpy as np

S = '/tmp/claude-0/-home-user-PPC-Audit-/f01da844-e516-5303-96fa-ec17555f9d55/scratchpad'
CEILING = 13.20          # SLQS forward-cash ad ceiling, per unit cleared
ECON = 17.01             # economic ceiling incl. avoided storage
CLICK_LINE = 15          # nothing judged on performance below this

d = pd.read_pickle(f'{S}/QZ_Sponsored_Products_Campaigns.pkl')
n = lambda s: pd.to_numeric(s, errors='coerce')
for c in ['Clicks', 'Spend', 'Sales', 'Orders', 'Units', 'ACOS', 'CPC', 'Bid']:
    d[c] = n(d[c])

mark = d['PLACEMTNT'].astype(str).str.strip().str.upper()
d['act'] = np.where(mark.isin(['PAUSE', 'PAUSED']), 'PAUSE',
                    np.where(d['PLACEMTNT'].notna(), 'OTHER', ''))
d['camp'] = d['Campaign Name (Informational only)']

TARGETS = ['Keyword', 'Product Targeting']
live = d[d['State'] == 'enabled']

rows = []
for camp, g in d[d.camp.notna()].groupby('camp'):
    crow = g[g.Entity == 'Campaign']
    camp_state = crow['State'].iloc[0] if len(crow) else ''
    camp_marked = (crow['act'] == 'PAUSE').any() if len(crow) else False

    tg = g[g.Entity.isin(TARGETS)]
    tg_live = tg[tg['State'] == 'enabled']
    tg_marked = (tg_live['act'] == 'PAUSE').sum()
    tg_total = len(tg_live)

    ag = g[g.Entity == 'Ad Group']
    ag_live = ag[ag['State'] == 'enabled']
    ag_marked = (ag_live['act'] == 'PAUSE').sum()

    pa = g[g.Entity == 'Product Ad']
    pa_live = pa[pa['State'] == 'enabled']
    pa_marked = (pa_live['act'] == 'PAUSE').sum()

    spend, sales, orders, clicks = (g[g.Entity == 'Campaign'][['Spend', 'Sales', 'Orders', 'Clicks']]
                                    .sum().tolist()) if len(crow) else (0, 0, 0, 0)
    cps = spend / orders if orders else np.nan

    flags = []
    # Rule 1 — everything inside is off, but the campaign is left running
    if not camp_marked and camp_state == 'enabled':
        if tg_total and tg_marked == tg_total:
            flags.append('all live targets paused, campaign left running')
        elif len(ag_live) and ag_marked == len(ag_live):
            flags.append('all live ad groups paused, campaign left running')
        elif len(pa_live) and pa_marked == len(pa_live):
            flags.append('all live product ads paused, campaign left running')
    # Rule 2 — campaign is going off, so the child marks are redundant
    if camp_marked and (tg_marked or ag_marked or pa_marked):
        flags.append('campaign paused AND children marked — child rows are redundant')
    # Already off
    if camp_marked and camp_state != 'enabled':
        flags.append(f'campaign already {camp_state} — pause is a no-op')

    if camp_marked or tg_marked or ag_marked or pa_marked:
        rows.append({
            'campaign': camp, 'campaign_state': camp_state,
            'campaign_marked_pause': camp_marked,
            'live_targets': tg_total, 'targets_marked': tg_marked,
            'live_adgroups': len(ag_live), 'adgroups_marked': ag_marked,
            'live_product_ads': len(pa_live), 'product_ads_marked': pa_marked,
            'clicks_7d': clicks, 'spend_7d': round(spend, 2), 'sales_7d': round(sales, 2),
            'orders_7d': int(orders), 'cost_per_sale': round(cps, 2) if orders else None,
            'vs_ceiling_13.20': ('' if not orders else
                                 ('OVER' if cps > CEILING else 'under')),
            'flags': ' | '.join(flags),
        })

out = pd.DataFrame(rows).sort_values(['flags', 'spend_7d'], ascending=[False, False])

# --- target-level performance recheck -----------------------------------------
tl = d[d.Entity.isin(TARGETS) & (d['act'] == 'PAUSE')].copy()
tl['cost_per_sale'] = np.where(tl.Orders > 0, tl.Spend / tl.Orders, np.nan)
tl['verdict'] = np.where(tl.Clicks < CLICK_LINE, 'BELOW CLICK LINE — not enough evidence',
                         np.where(tl.Orders == 0, 'confirmed: no orders past the click line',
                                  np.where(tl.cost_per_sale > CEILING,
                                           'confirmed: over the $13.20 ceiling',
                                           'CHECK: converting under the ceiling')))
tl = tl[['camp', 'Keyword Text', 'Product Targeting Expression', 'Match Type', 'Bid', 'Clicks',
         'Spend', 'Sales', 'Orders', 'ACOS', 'cost_per_sale', 'verdict']]

camps = d[(d.Entity == 'Campaign') & (d['act'] == 'PAUSE')].copy()
camps['cost_per_sale'] = np.where(camps.Orders > 0, camps.Spend / camps.Orders, np.nan)
camps['verdict'] = np.where(camps.Clicks < CLICK_LINE, 'BELOW CLICK LINE — not enough evidence',
                            np.where(camps.Orders == 0, 'confirmed: no orders past the click line',
                                     np.where(camps.cost_per_sale > CEILING,
                                              'confirmed: over the $13.20 ceiling',
                                              'CHECK: converting under the ceiling')))
camps = camps[['camp', 'State', 'Clicks', 'Spend', 'Sales', 'Orders', 'ACOS', 'cost_per_sale',
               'verdict']]

OUT = f'{S}/SLQS_action_check_09Sep2026.xlsx'
with pd.ExcelWriter(OUT, engine='openpyxl') as xl:
    out.to_excel(xl, sheet_name='campaign consistency', index=False)
    camps.to_excel(xl, sheet_name='campaign pauses vs data', index=False)
    tl.to_excel(xl, sheet_name='target pauses vs data', index=False)

print('campaigns touched:', len(out))
print('\nFLAGS:')
print(out.loc[out['flags'] != '', 'flags'].value_counts().to_string())
print('\nCAMPAIGN PAUSES —', len(camps))
print(camps.verdict.value_counts().to_string())
print('\nTARGET PAUSES —', len(tl))
print(tl.verdict.value_counts().to_string())
