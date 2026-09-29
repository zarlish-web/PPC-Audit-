"""Deliverable 1 — the workbook. Every cell is read from v2/out/*.json (the same files the document is built from).
Output: v2/deliver/DSS4_Audit_Review_Workbook_20260929.xlsx"""
import json, os, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import load as L

O = L.OUT
J = lambda n: json.load(open(O + n))
P, M, CP, KW, R, CB = J('product.json'), J('market.json'), J('competitors.json'), J('keywords.json'), J('ranking.json'), J('campaigns_base.json')
AR, D, LT, INV, KA, CF, FN = J('audit_review.json'), J('decisions.json'), J('ltsf.json'), J('inventory.json'), J('kw_actions.json'), J('conflicts.json'), J('financials.json')
DEL = L.ROOT + 'v2/deliver/'
os.makedirs(DEL, exist_ok=True)
PATH = DEL + 'DSS4_Audit_Review_Workbook_20260929.xlsx'
wb = Workbook()
wb.remove(wb.active)
HEAD = PatternFill('solid', start_color='1F3864')
HF = Font(color='FFFFFF', bold=True)


def sheet(name, cols, rows, widths=None, note=None):
    ws = wb.create_sheet(name[:31])
    r0 = 1
    if note:
        ws.cell(1, 1, note).font = Font(italic=True)
        r0 = 3
    for j, c in enumerate(cols, 1):
        x = ws.cell(r0, j, c)
        x.fill, x.font = HEAD, HF
        x.alignment = Alignment(wrap_text=True, vertical='top')
    for i, row in enumerate(rows, r0 + 1):
        for j, v in enumerate(row, 1):
            if isinstance(v, (list, dict)):
                v = json.dumps(v, default=str)
            ws.cell(i, j, v)
    for j in range(1, len(cols) + 1):
        ws.column_dimensions[get_column_letter(j)].width = (widths[j - 1] if widths and j - 1 < len(widths) else 14)
    ws.freeze_panes = ws.cell(r0 + 1, 3)
    ws.auto_filter.ref = f"A{r0}:{get_column_letter(len(cols))}{max(r0 + 1, r0 + len(rows))}"
    return ws


pct = lambda x: None if x is None else round(x * 100, 2)
F = FN
S = D['summary']

# ---------------------------------------------------------------- Read me / Summary
ws = wb.create_sheet('Read me')
lines = [
    'Decolure Satin Sheets 4-Piece — audit review workbook (29 Sep 2026)',
    'Every number here is computed from the source pulls of 29 Sep 2026: Sellerboard (sales, fees, stock, shipments, live budgets and bids), Command Center (ad metrics 30/90 days with placements, keyword lens, ranks, audit export), '
    'Data Dive (Amazon Search Query Performance Q4-2025/Q2/Q3, Rank Radar daily ranks, advertised ASIN per campaign, niche dives, FC stock), ASINsight (competitor traffic, ad placements, SB video), and the S4-LTSF Google Sheet (column V = Total AIS Charge).',
    'The document and this workbook are generated from the same data files; the “Checks” tab lists the automated cross-checks between them.',
    'Tabs: Summary · Audit review (every non-cosmetic audit decision re-judged) · Campaigns (all 612, current state and final action) · Ranking terms · Preferred variation · Keywords · LTSF · LTSF campaigns · Inventory · Financials · '
    'Push cost by term · Market · Competitors · Video · Conflicts · New campaigns · Bulk upload · Checks.',
    'Plain-language definitions: break-even ACoS = profit before ads ÷ sales for the advertised child (Sellerboard, 30 days). Top of search (TOS) = the first row of results. '
    'Ranking – push = a term we are paying to climb; Ranking – maintain = a term we hold at today\'s clicks. LTSF = aged inventory charged the surcharge in the LTSF sheet.',
]
for i, t in enumerate(lines, 1):
    ws.cell(i, 1, t).alignment = Alignment(wrap_text=True)
ws.column_dimensions['A'].width = 160

fam = P['family30']['Info']
summ = [
    ('Product (30 days, Sellerboard)', f"Sales ${fam['Sales']:,.0f} · units {fam['Units']:,} · ad spend ${F['now']['ads']:,} · TACoS {pct(F['now']['tacos'])}% · net profit ${F['now']['net']:,} ({pct(F['now']['margin'])}%)"),
    ('Market (Amazon SQP, tracked terms)', ' · '.join(f"{v['label']}: {v['purchases']:,} purchases, our share {pct(v['our_purchase_share'])}%" for v in M['sqp_totals'].values())),
    ('Ranking spend share now', f"{pct(S['now_ranking_spend_share'])}% of spend, {pct(S['now_ranking_click_share'])}% of clicks"),
    ('Ranking spend share after plan (week 1)', f"{pct(F['share']['ranking_of_all_spend'])}% of all spend; {pct(F['share']['ranking_of_keyword_growth_spend'])}% of keyword spend once LTSF clearance and brand defence are ring-fenced; {pct(F['share']['ranking_of_all_clicks'])}% of clicks"),
    ('Non-ranking spend cap for 80% / 90% of all spend', f"${F['share']['nonranking_cap_for_80pct']}/day / ${F['share']['nonranking_cap_for_90pct']}/day (plan week 1: ${F['share']['all_spend_day'] - F['share']['ranking_spend_day']:.0f}/day)"),
    ('P&L after plan (30-day equivalent, direct ad effect only)', f"Sales ${F['plan']['sales']:,} · ad spend ${F['plan']['ads']:,} · TACoS {pct(F['plan']['tacos'])}% · net ${F['plan']['net']:,} ({pct(F['plan']['margin'])}%)"),
    ('Preferred ranking children', ' · '.join(f"{z}: {v['chosen']} ({v['basis'][:60]})" for z, v in R['preferred'].items())),
    ('Ranking terms', f"{len(R['ranking_set'])} push terms (80% of market purchases) at ${R['ranking_cost_day']}/day target; {len(R['maintain_set'])} maintain terms"),
    ('LTSF', f"Sheet total ${LT['totals']['ais']} AIS on {LT['totals']['units']:,} units; #1 {LT['rows'][0]['sku']} ${LT['rows'][0]['total_ais']} (~{LT['rows'][0]['est_aged_left']} aged units left)"),
    ('Stock', ' · '.join(f"{r['sku']}: out {r['stockout_date'] or 'after 31 Jan'} (short {r['units_short_to_31jan']})" for r in INV['rows'] if r['sku'] in ('SATIN-QUEEN-BLACK', 'SATIN-KING-BLACK', 'SATIN-FULL-BLACK', 'SATIN-TWIN-BLACK-NEW'))),
    ('Audit decisions re-judged', ' · '.join(f"{k}: {v}" for k, v in sorted(__import__('collections').Counter(a['verdict'] for a in AR).items()))),
]
sheet('Summary', ['Item', 'Value'], summ, [48, 170])

# ---------------------------------------------------------------- Audit review
rows = []
for a in AR:
    mt, cn, im = a.get('main_term') or {}, a.get('campaign_now') or {}, a.get('impact_estimate') or {}
    rows.append([a['seq'], a['kind'], a['campaign_id'], a['campaign'], a['entity'], a['current'], a['suggested'], a['audit_objective'], a['role'], a['audit_rule'],
                 a['cites_b6'], a['verdict'], a.get('final_action'), ' / '.join(a['analysis']), mt.get('term'), mt.get('in_ranking_set'), mt.get('mkt_purchases_day'), mt.get('rank_med7'),
                 mt.get('trend'), f"{mt.get('rank_best_q3')}–{mt.get('rank_worst_q3')}" if mt else None, a.get('campaign_share_of_our_paid_clicks_on_term'),
                 cn.get('clicks_day'), cn.get('orders_day'), cn.get('spend_day'), cn.get('acos'), cn.get('budget'), cn.get('utilization'), cn.get('tos_is'),
                 (a.get('child') or {}).get('sku'), (a.get('child') or {}).get('be_acos'), (a.get('child') or {}).get('days_cover'), (a.get('child') or {}).get('ltsf_rank'),
                 a.get('change_pct'), im.get('d_clicks_day'), im.get('d_orders_day'), im.get('d_sales_day'), im.get('d_spend_day'), im.get('d_profit_day'), im.get('d_tacos_pts'),
                 a['audit_why'][:400]])
sheet('Audit review', ['Seq', 'Kind', 'Campaign ID', 'Campaign', 'Entity', 'Audit: current', 'Audit: suggested', 'Audit objective', 'Role (this review)', 'Audit rule',
                       'Rule cites B6?', 'Verdict', 'Final action on the campaign', 'Evidence', 'Main term', 'Ranking term?', 'Market purchases/day', 'Rank (7-day median)', 'Trend', 'Q3 rank range',
                       'Campaign share of our paid clicks on term', 'Clicks/day', 'Orders/day', 'Spend/day', 'ACoS %', 'Budget', 'Budget used %', 'TOS impr. share %',
                       'Child', 'Break-even ACoS', 'Days of stock', 'LTSF rank', 'Change %', 'Δ clicks/day', 'Δ orders/day', 'Δ sales/day', 'Δ spend/day', 'Δ profit/day',
                       'Δ TACoS pts', 'Audit text (first 400 chars)'], rows,
      [6, 9, 17, 50, 30, 14, 22, 11, 22, 30, 8, 9, 40, 90, 24, 8, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 26, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 60],
      note='Every non-cosmetic decision in the audit export (renames and retags excluded). Verdict: ACCEPT / MODIFY / REJECT / HOLD / REVIEW, with the data behind it.')

# ---------------------------------------------------------------- Campaigns
ARC = {}
for a in AR:
    ARC.setdefault(a['campaign_id'], []).append(a)
rows = []
for d in D['decisions']:
    n, a = d['now'], d['action']
    bc = '; '.join(f"{b.get('term')}: {b.get('bid_from')}→{b.get('bid_to') or b.get('change')}" for b in a['bid_changes'])
    rows.append([d['campaign_id'], d['name'], d['ad_type'], d['status'], d['role'], d['child'], d['size'], d['colour'], ', '.join(d['terms'][:6]) + ('…' if len(d['terms']) > 6 else ''),
                 ', '.join(d['owned_terms']), d['budget'], d['utilization'] and round(d['utilization'], 1), d['tos_is'], d['mods'].get('tos'), d['mods'].get('ros'), d['mods'].get('pp'),
                 d['strategy'], n['clicks_day'] * 30 if n['clicks_day'] is not None else None, n['cpc'], n['orders_day'] * 30, n['cvr'], n['spend_day'] * 30, n['sales_day'] * 30, n['acos'],
                 n['tos_clicks'], n['tos_cvr'], n['ros_clicks'], n['ros_cvr'], n['pp_clicks'], n['pp_cvr'], n['clicks90'], n['orders90'], n['spend90'], n['acos90'], n['tos_cvr90'],
                 d['be_acos'] and round(d['be_acos'] * 100, 1),
                 a['state'], a['child_to'], a['budget_to'], a['tos_to'], a['ros_to'], a['pp_to'], a['strategy_to'], bc, len(a['negatives_add']),
                 ', '.join(a['ads_add']), ', '.join(a['ads_pause']), ', '.join(a.get('ads_add_paused') or []), a.get('switch_rule'), d['plan']['spend_day'], d['plan']['clicks_day'], d['plan']['orders_day'],
                 d['checks'].get('d_spend_day'), d['checks'].get('d_orders_day'), d['checks'].get('d_sales_day'), d['checks'].get('d_profit_day'), d['checks'].get('d_tacos_pts'),
                 d['checks'].get('placement'), d['checks'].get('rank') or d['checks'].get('rank_risk'), d['checks'].get('stock_child_days'), d['checks'].get('ltsf'),
                 ' | '.join(d['why']), ' | '.join(f"{x['kind']} {x['current']}→{x['suggested']}: {x['verdict']}" for x in ARC.get(d['campaign_id'], []))])
sheet('Campaigns', ['Campaign ID', 'Campaign', 'Ad type', 'Status', 'Role', 'Advertised child (actual)', 'Size', 'Colour', 'Targets', 'Ranking terms it owns', 'Budget $/day',
                    'Budget used %', 'TOS impr. share %', 'TOS %', 'ROS %', 'PP %', 'Bid strategy', 'Clicks 30d', 'CPC', 'Orders 30d', 'CVR %', 'Spend 30d', 'Sales 30d',
                    'ACoS 30d %', 'TOS clicks', 'TOS CVR %', 'ROS clicks', 'ROS CVR %', 'PP clicks', 'PP CVR %', 'Clicks 90d', 'Orders 90d', 'Spend 90d', 'ACoS 90d %',
                    'TOS CVR 90d %', 'Break-even ACoS %', 'ACTION: state', 'ACTION: child →', 'ACTION: budget →', 'ACTION: TOS % →', 'ACTION: ROS % →', 'ACTION: PP % →',
                    'ACTION: strategy →', 'ACTION: bids', 'ACTION: negatives (count)', 'ACTION: product ads add', 'ACTION: product ads pause', 'ACTION: back-up ad (add PAUSED)', 'Back-up switch rule', 'Plan spend/day',
                    'Plan clicks/day', 'Plan orders/day', 'Δ spend/day', 'Δ orders/day', 'Δ sales/day', 'Δ profit/day', 'Δ TACoS pts', 'Placement check', 'Rank check',
                    'Child days of stock', 'Child LTSF rank', 'Why', 'Audit said → our verdict'], rows,
      [17, 50, 6, 9, 24, 26, 7, 9, 36, 30] + [9] * 39 + [26, 60] + [9] * 7 + [50, 50, 8, 7, 120, 80])

# ---------------------------------------------------------------- Ranking terms
own = D['owners']
nm = {d['campaign_id']: d['name'] for d in D['decisions']}
rows = []
for o in R['opportunities']:
    k = next((x for x in KW if x['keyword'] == o['keyword']), {})
    riv = ', '.join(f"{r['brand']} #{r['organic']}" for r in (CP and [])) if False else None
    rows.append([o['keyword'], o.get('tier') or '—', o.get('set_reason'), o['size'], o['child'], o['sqp_volume_q3'], o['mkt_purchases_day'], o.get('mkt_clicks_day'),
                 pct(o['our_share']), pct(o['share_q2']), pct(o['share_q4']), pct(o['our_cvr_sqp']), pct(o['mkt_cvr']), o['cvr_index'], o['rank_radar'], o['rank_cc'],
                 o['rank_asinsight'], o['rank_best90'], o.get('radar_worst_q3'), o['days_unranked'], o['sp_rank'], o['target'], pct(o['target_share']),
                 o['add_purchases_day'], pct(o['paid_cvr']), o['cvr_source'], o['tos_cpc'], o.get('ad_clicks_day_now'), o.get('target_clicks_day'), o.get('capped'),
                 o.get('target_cost_day'), o['spend30'], o['acos30'], o['be_acos'] and round(o['be_acos'] * 100, 1), own.get(o['keyword']), nm.get(own.get(o['keyword'])),
                 round(o['cum_share_of_market'] * 100, 1)])
sheet('Ranking terms', ['Term', 'Tier', 'Why in / out', 'Size', 'Ranking child', 'SQP searches Q3', 'Market purchases/day', 'Market clicks/day', 'Our purchase share Q3 %',
                        'Q2 %', 'Q4-2025 %', 'Our CVR (SQP) %', 'Market CVR %', 'CVR index', 'Rank Radar 7-day', 'CC rank', 'ASINsight rank', 'Best Q3', 'Worst Q3',
                        'Days unranked Q3', 'Sponsored rank', 'Target band', 'Target share %', '+ purchases/day needed', 'Paid CVR used %', 'CVR source', 'TOS CPC $',
                        'Paid clicks/day now', 'Target clicks/day', 'Capped at 11.5% click share?', 'Target cost/day', 'Spend 30d', 'ACoS 30d %', 'Break-even %',
                        'Owner campaign ID', 'Owner campaign', 'Cumulative % of market purchases'], rows, [26, 9, 40] + [9] * 34,
      note='Rank→share curve from our own data (SQP Q3 × Rank Radar median): ' + '; '.join(f"rank {k}: {pct(v['median_share'])}% (n={v['n']})" for k, v in R['curve'].items()))

# ---------------------------------------------------------------- Preferred variation
rows = []
for z, v in R['preferred'].items():
    for c in v['candidates']:
        rows.append([z, c['sku'], c['sku'] == v['chosen'], c['units90'], pct(c['share_units90']), c['pba_unit90'], pct(c['tos_cvr90']), c.get('tos_basis'),
                     c['value_per_tos_click'], c['stock_all'], c['pace'], c.get('push_pace'), c['days_at_push_pace'], c['q4_need'], c['usp30'], v['basis']])
sheet('Preferred variation', ['Size', 'Child', 'Chosen', 'Units 90d', 'Share of size %', 'Profit before ads/unit 90d', 'TOS CVR 90d %', 'TOS CVR basis',
                              'Value per TOS click $', 'Stock (all)', 'Pace/day', 'Push pace/day', 'Days at push pace', 'Q4 need', 'Unit session %', 'Rule'], rows,
      [7, 30, 7] + [10] * 12 + [70])
BKP = {(b['size'], b['backup']): b for b in INV.get('backups', [])}
rows = []
for z, v in R['preferred'].items():
    for i, b in enumerate(v.get('backups') or []):
        x = BKP.get((z, b['sku']), {})
        rows.append([z, v['chosen'], i + 1, b['sku'], b['level'], b['days_at_push_pace'], b['value_per_tos_click'], pct(b['tos_cvr']), b['tos_basis'], pct(b['share']), b['stock'],
                     x.get('switch_date'), x.get('ranking_orders_moved'), x.get('backup_stockout')])
sheet('Back-up ranking child', ['Size', 'Preferred child', 'Back-up #', 'Back-up child', 'Can carry', 'Days at push pace', 'Profit per TOS click $', 'TOS CVR %', 'TOS CVR basis',
                                'Share of size units %', 'Stock', 'Projected switch date', 'Ranking orders/day it takes over', 'Back-up stock-out (after taking over)'], rows,
      [7, 24, 8, 30, 22] + [11] * 9,
      note='Rule: other children with positive profit per TOS click and ≥5% of the size\'s units (≥3% if none, flagged); ≥60 days at push pace can carry the push, 30–59 days the maintain level. '
           'Switch the ranking product ad when the preferred child drops under 14 days of stock or goes out of stock; switch back at ≥30 days. The back-up ad is loaded now, PAUSED, in every ranking campaign.')

# ---------------------------------------------------------------- Keywords
rows = [[r['keyword'], r['cls'], r['size'], r['colour'], r['action'], r['why'], r['tier'], r['owner'], r['clicks30'], r['orders30'], r['spend30'], r['acos30'], r['cvr30'],
         r['cpc30'], r['clicks90'], r['orders90'], r['spend90'], r['acos90'], r['sqp_volume_q3'], r['mkt_purchases_q3'], pct(r['our_purchase_share_q3']),
         pct(r['share_q2']), pct(r['share_q4_2025']), r['rank_radar'], r['rank_cc'], r['rank_asinsight'], r['be_acos'] and round(r['be_acos'] * 100, 1)] for r in KA]
sheet('Keywords', ['Search term', 'Class', 'Size', 'Colour', 'Action', 'Why', 'Tier', 'Owner campaign', 'Clicks 30d', 'Orders 30d', 'Spend 30d', 'ACoS 30d %', 'CVR 30d %',
                   'CPC 30d', 'Clicks 90d', 'Orders 90d', 'Spend 90d', 'ACoS 90d %', 'SQP searches Q3', 'Market purchases Q3', 'Our share Q3 %', 'Q2 %', 'Q4-2025 %',
                   'Rank Radar', 'CC rank', 'ASINsight rank', 'Break-even %'], rows, [30, 18, 7, 8, 30, 60] + [9] * 21)

# ---------------------------------------------------------------- LTSF
routed = __import__('collections').Counter()
routed_o = __import__('collections').Counter()
for d in D['decisions']:
    ch = d['action']['child_to'] or d['child']
    routed[ch] += 1 if d['plan']['spend_day'] else 0
    routed_o[ch] += d['plan']['orders_day']
rows = [[r['rank'], r['sku'], r['asin'], r['size'], r['total_ais'], r['ais_units'], r['ais_per_unit'], r['oldest_bucket'], r['status_sheet'], r['sold_sheet'],
         r['sellable_now'], r['vel30'], r['days_cover'], r['est_aged_left'], r['avg_charge_month'], r['moh'], r['avoid_per_unit'], r['pba_unit30'],
         routed.get(r['sku'], 0), round(routed_o.get(r['sku'], 0), 2)] for r in LT['rows']]
sheet('LTSF', ['LTSF rank (col V)', 'SKU', 'ASIN', 'Size', 'Total AIS Charge (V)', 'AIS units', 'AIS/unit', 'Oldest bucket (15 Jul)', 'Sheet action', 'Sold 15 Jul–27 Aug',
               'Sellable now', 'Units/day (30d)', 'Days of stock', 'Aged units left (estimate)', 'AVG charge/month (AU)', 'MOH (AT)', 'Storage/AIS avoided per unit sold $',
               'Profit before ads/unit', 'Campaigns advertising it after plan', 'Plan ad orders/day'], rows, [7, 30, 12, 7] + [11] * 16,
      note='Source: S4-LTSF Google Sheet (totals verified: $1,632.92, 3,121 units). Aged units left = sheet aged units − sheet sales − 30-day pace × 33 days (oldest sell first).')
rows = []
for d in D['decisions']:
    if re.search(r'LTSF|AGED|Clr|clearance', d['name'] or '', re.I):
        rows.append([d['campaign_id'], d['name'], d['ad_type'], d['status'], d['role'], d['now']['spend_day'] * 30, d['now']['orders_day'] * 30, d['now']['acos'],
                     ', '.join(d['action']['ads_add']), ', '.join(d['action']['ads_pause']), ' | '.join(d['why'])])
sheet('LTSF campaigns', ['Campaign ID', 'Campaign', 'Type', 'Status', 'Role', 'Spend 30d', 'Orders 30d', 'ACoS %', 'Add product ads (LTSF SKUs missing)',
                         'Pause product ads (not on LTSF sheet / cleared)', 'Why'], rows, [17, 55, 6, 9, 26, 9, 9, 8, 60, 70, 120])

# ---------------------------------------------------------------- Inventory
rows = [[r['sku'], r['size'], r['colour'], r['sellable'], r['in_transfer'], r['inbound_shipped'], r['inbound_plan_only'], r['stock_total'], r['units_day_30'],
         r['ad_orders_day_now'], r['plan_ad_orders_day'], r['land_share'], r['plan_pace_sep_equiv'], r['stockout_now_pace'], r['short_now_pace'], r['stockout_date'],
         r['units_short_to_31jan'], r['lost_sales_units_sb']] for r in INV['rows']]
sheet('Inventory', ['Child', 'Size', 'Colour', 'Sellable', 'In FC transfer', 'Inbound shipped', 'Inbound plan only', 'Stock counted', 'Units/day (30d)', 'Ad orders/day now',
                    'Ad orders/day plan', 'Share of ad orders landing on this child', 'Plan pace (Sep-equivalent)', 'Stock-out at today\'s pace', 'Short to 31 Jan (today\'s pace)',
                    'Stock-out under plan', 'Short to 31 Jan (plan)', 'Sellerboard lost-sales units'], rows, [30] + [11] * 17,
      note='Seasonality = last year\'s units ÷ Sep-2025 units (Sellerboard): ' + ', '.join(f"month {k}: ×{v}" for k, v in INV['season'].items()))

# ---------------------------------------------------------------- Financials
rows = [['Now (30 days)', F['now']['sales'], F['now']['ads'], pct(F['now']['tacos']), F['now']['net'], pct(F['now']['margin'])],
        ['Plan (30-day equivalent, direct ad effect only)', F['plan']['sales'], F['plan']['ads'], pct(F['plan']['tacos']), F['plan']['net'], pct(F['plan']['margin'])]]
rows += [[f"Component: {k}", round(v['d_sales_day'] * 30), round(v['d_spend_day'] * 30), None, round(v['d_profit_day'] * 30), None] for k, v in F['components'].items()]
rows += [['Monthly: ' + m['month'], m['sales'], m['ads'], pct(m['tacos']), m['net'], pct(m['margin'])] for m in P['monthly']]
sheet('Financials', ['Line', 'Sales $', 'Ad spend $', 'TACoS %', 'Net profit $', 'Margin %'], rows, [55, 12, 12, 10, 12, 10],
      note=F['note'] + f" Ranking share: {pct(F['share']['ranking_of_all_spend'])}% of all spend; {pct(F['share']['ranking_of_keyword_growth_spend'])}% with LTSF and brand defence ring-fenced.")
rows = []
dec = {d['campaign_id']: d for d in D['decisions']}
for o in R['opportunities']:
    if o.get('tier') != 'push':
        continue
    d = dec.get(own.get(o['keyword']))
    if not d:
        continue
    n = len(d['owned_terms']) or 1
    rows.append([o['keyword'], o['size'], o['mkt_purchases_day'], o['rank_now'], o['target'], o['ad_clicks_day_now'], o['target_clicks_day'], o['target_cost_day'],
                 round(d['checks']['d_spend_day'] / n, 2), round(d['checks']['d_orders_day'] / n, 2), round(d['checks']['d_profit_day'] / n, 2), d['campaign_id']])
sheet('Push cost by term', ['Term', 'Size', 'Market purchases/day', 'Rank now', 'Target', 'Paid clicks/day now', 'Target clicks/day', 'Target cost/day', 'Δ spend/day',
                            'Δ orders/day', 'Δ profit/day', 'Owner campaign'], rows, [28] + [11] * 11,
      note='What each push term costs over today (direct ad effect). The owner can drop a term here; its campaign then moves to the maintain settings.')

# ---------------------------------------------------------------- Market
rows = [[v['label'], v['keywords'], v['volume'], v['clicks'], v['purchases'], v['purchases_per_day'], pct(v['market_cvr']), pct(v['our_impr_share']), pct(v['our_click_share']),
         pct(v['our_purchase_share']), pct(v['our_cvr'])] for v in M['sqp_totals'].values()]
ws = sheet('Market', ['Quarter (SQP)', 'Terms', 'Searches', 'Clicks', 'Purchases', 'Purchases/day', 'Market CVR %', 'Our impr. share %', 'Our click share %',
                      'Our purchase share %', 'Our CVR %'], rows, [16] + [12] * 10,
           note=f"Same {M['sqp_season_common']['keywords']} terms in all three quarters: searches Q4-2025 {M['sqp_season_common']['q4_2025']:,} · Q2 {M['sqp_season_common']['q2']:,} · Q3 {M['sqp_season_common']['q3']:,}")
r0 = ws.max_row + 2
ws.cell(r0, 1, 'Our ads by month (Command Center)').font = Font(bold=True)
for i, a in enumerate(M['ads_trend'], r0 + 1):
    for j, v in enumerate([a['month'], a['spend'], a['sales'], a['clicks'], a['orders'], a['cpc'], pct(a['cvr']), pct(a['ctr']), pct(a['acos'])], 1):
        ws.cell(i, j, v)
r0 = ws.max_row + 2
ws.cell(r0, 1, 'Listings tracked in niche dives (first → last snapshot)').font = Font(bold=True)
for i, t in enumerate(M['tracked_listings'][:25], r0 + 1):
    for j, v in enumerate([t['brand'], t['asin'], t['first']['date'], t['first']['price'], t['first']['units'], t['last']['date'], t['last']['price'], t['last']['units'],
                           t['last']['reviews'], t['last']['rating']], 1):
        ws.cell(i, j, v)
r0 = ws.max_row + 2
ws.cell(r0, 1, 'Listing events and deals').font = Font(bold=True)
for i, e in enumerate((M['events'] or []) + (M['deals'] or []), r0 + 1):
    ws.cell(i, 1, e['date']); ws.cell(i, 2, e.get('endDate')); ws.cell(i, 3, e['title'])

# ---------------------------------------------------------------- Competitors
rows = [[r['brand'], r['tier'], r['traffic'], r['traffic_hist'][0][1] if r['traffic_hist'] else None, r['lead_asin'], (r['lead_first'] or {}).get('price'),
         (r['lead_last'] or {}).get('price'), (r['lead_last'] or {}).get('units'), r['reach_sp'], r['reach_sb'], r['reach_sbv'], r['reach_ac'], r['contested'], r['our_wins'],
         r['call']] for r in CP['rivals']]
ws = sheet('Competitors', ['Brand', 'ASINsight tier', 'Traffic (latest)', 'Traffic (first)', 'Lead listing', 'Price first', 'Price last', 'Units/month (last dive)',
                           'SP keywords', 'SB keywords', 'SB video keywords', 'Amazon\'s Choice keywords', 'Contested keywords', 'Our wins', 'Call'], rows, [26] + [11] * 14)
r0 = ws.max_row + 2
ws.cell(r0, 1, 'Who ranks where on the head terms (ASINsight)').font = Font(bold=True)
i = r0 + 1
for t in CP['term_field']:
    ws.cell(i, 1, t['term']); ws.cell(i, 2, f"weekly searches {t['weekly_sv']}; us organic {t['our_organic']}, sponsored {t['our_sp']}")
    ws.cell(i, 3, '; '.join(f"{x['brand']} org {x['organic']} / sp {x['sp']} {'+'.join(x['placements'] or [])}" for x in t['rivals'][:6]))
    i += 1

# ---------------------------------------------------------------- Video
vr = open(L.RAW + 'video/video_research.md').read()
ws = wb.create_sheet('Video')
for i, line in enumerate(vr.splitlines(), 1):
    ws.cell(i, 1, line)
ws.column_dimensions['A'].width = 200

# ---------------------------------------------------------------- Conflicts / New campaigns
sheet('Conflicts', ['Area', 'Source A', 'Source B', 'What was checked', 'What the plan uses', 'Status'],
      [[c['area'], c['source_a'], c['source_b'], c['checked'], c['resolution'], c['status']] for c in CF], [34, 55, 55, 60, 60, 12])
sheet('New campaigns', ['Term', 'Tier', 'Match', 'Child', 'Budget $/day', 'Base bid', 'TOS %', 'ROS %', 'PP %', 'Strategy', 'Target clicks/day', 'Why'],
      [[n['term'], n['tier'], n['match'], n['child'], n['budget'], n['base_bid'], n['tos'], n['ros'], n['pp'], n['strategy'], n['target_clicks_day'], n['why']]
       for n in D['new_campaigns']], [26] + [11] * 10 + [90])

# ---------------------------------------------------------------- Bulk upload (Amazon Sponsored Products bulk format)
TBC = {}
try:
    for r in (json.load(open(L.RAW + 'sb_ppc/targets_by_campaign_W30.json')) + json.load(open(L.RAW + 'sb_ppc/targets_by_campaign_W90only.json'))):
        TBC.setdefault(str(r['_campaign_id']), []).append(r)
except Exception:
    pass
bulk = []
for d in D['decisions']:
    if d['ad_type'] != 'SP':
        continue
    a, cid = d['action'], d['campaign_id']
    if a['state'] or a['budget_to'] or a['strategy_to']:
        bulk.append(['Sponsored Products', 'Campaign', 'Update', cid, '', '', '', '', (a['state'] or '').lower(), a['budget_to'] or '', '', '', '', a['strategy_to'] or '', ' | '.join(d['why'])[:250]])
    for pl, v in (('Placement Top', a['tos_to']), ('Placement Rest Of Search', a['ros_to']), ('Placement Product Page', a['pp_to'])):
        if v is not None:
            bulk.append(['Sponsored Products', 'Bidding Adjustment', 'Update', cid, '', '', '', '', '', '', '', pl, v, '', 'placement'])
    rows_t = {(r.get('Name') or '').lower(): r for r in TBC.get(cid, [])}
    for b in a['bid_changes']:
        if b.get('term') == '(all targets)':
            for nm_, r in rows_t.items():
                if r.get('current_bid'):
                    ag, kid = (r['Id'].split('|') + [''])[:2]
                    bulk.append(['Sponsored Products', 'Keyword' if r.get('KeywordType') in ('EXACT', 'PHRASE', 'BROAD', 'Exact', 'Phrase', 'Broad') else 'Product Targeting',
                                 'Update', cid, ag, kid, nm_, r.get('KeywordType'), '', '', round(r['current_bid'] * 0.85, 2), '', '', '', 'step −15%'])
        else:
            r = rows_t.get(b['term'])
            ag, kid = ((r['Id'].split('|') + [''])[:2]) if r else ('', '')
            bulk.append(['Sponsored Products', 'Keyword', 'Update', cid, ag, kid, b['term'], 'exact', '', '', b.get('bid_to'), '', '', '',
                         'ranking base bid' + ('' if r else ' — keyword ID not in the Sellerboard pull: find it in the console')])
    for n in a['negatives_add']:
        bulk.append(['Sponsored Products', 'Campaign Negative Keyword', 'Create', cid, '', '', n['term'], 'negativeExact', 'enabled', '', '', '', '', '', 'ranking term owned elsewhere'])
    ags = sorted({(r['Id'].split('|')[0]) for r in TBC.get(cid, [])})
    for sku in a['ads_add']:
        bulk.append(['Sponsored Products', 'Product Ad', 'Create', cid, ags[0] if len(ags) == 1 else '(ad group)', '', '', '', 'enabled', '', '', '', '', '', f"add SKU {sku}"])
    for sku in a.get('ads_add_paused') or []:
        bulk.append(['Sponsored Products', 'Product Ad', 'Create', cid, ags[0] if len(ags) == 1 else '(ad group)', '', '', '', 'paused', '', '', '', '', '', f"back-up SKU {sku} — load PAUSED; enable only per the switch rule"])
    for sku in a['ads_pause']:
        bulk.append(['Sponsored Products', 'Product Ad', 'Update', cid, ags[0] if len(ags) == 1 else '(ad group)', '', '', '', 'paused', '', '', '', '', '', f"pause SKU {sku} (Ad ID from the console)"])
sheet('Bulk upload', ['Product', 'Entity', 'Operation', 'Campaign ID', 'Ad Group ID', 'Keyword ID', 'Keyword Text', 'Match Type', 'State', 'Daily Budget', 'Bid',
                      'Placement', 'Percentage', 'Bidding Strategy', 'Note'], bulk, [16, 22, 9, 17, 17, 17, 28, 12, 8, 10, 8, 22, 9, 22, 60],
      note='Amazon bulk-sheet columns. Product-ad create/pause needs the SKU and Ad ID in the console; keyword IDs come from the Sellerboard live pull where available.')
if os.path.exists(O + 'checks.json'):
    ck = json.load(open(O + 'checks.json'))
    sheet('Checks', ['Check', 'Result', 'Detail'], [[c['check'], 'OK' if c['ok'] else 'FAIL', c['detail']] for c in ck], [90, 8, 90],
          note='Automated cross-checks between this workbook, the document and the decision data (run after both were built).')
wb.save(PATH)
json.dump(dict(path=PATH, bulk_rows=len(bulk)), open(O + 'book_meta.json', 'w'))
print(PATH, 'bulk rows', len(bulk))
