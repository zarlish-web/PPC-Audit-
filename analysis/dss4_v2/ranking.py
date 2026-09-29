"""Stage 5 — Preferred variation per size, then ranking opportunity per term.
Every threshold here comes from this product's own data (rank ↔ purchase-share curve from Amazon SQP + our Rank Radar; paid CVR from our ads).
Output: v2/out/ranking.json"""
import json, collections, statistics as st
import load as L

P = json.load(open(L.OUT + 'product.json'))
KW = {k['keyword']: k for k in json.load(open(L.OUT + 'keywords.json'))}
SKU = {s['sku']: s for s in P['skus']}
SEASON = P['season']
Q4_FACTOR_DAYS = 31 * SEASON['2025-10'] + 30 * SEASON['2025-11'] + 31 * SEASON['2025-12']   # Sep-2025-equivalent days of demand in Oct–Dec

# ---------------------------------------------------------------- paid top-of-search CVR per advertised child (CC, 90 days, SP campaigns)
child_of = {c['campaign_id']: c.get('child') for c in L.AUDIT['campaigns']}
paid = collections.defaultdict(lambda: collections.Counter())
for cid, r in L.CC_CAMP90.items():
    ch = child_of.get(cid)
    if not ch:
        continue
    p = paid[ch]
    p['clicks'] += r.get('clicks') or 0
    p['orders'] += r.get('orders') or 0
    p['spend'] += r.get('spend') or 0
    p['tos_clicks'] += r.get('tos_clicks') or 0
    p['tos_orders'] += (r.get('tos_clicks') or 0) * (r.get('tos_cvr') or 0) / 100
    p['tos_spend'] += (r.get('tos_clicks') or 0) * (r.get('tos_cpc') or 0)

# ---------------------------------------------------------------- current ranking traffic per size (exact SP campaigns the audit tags Ranking, CC 30 days)
A = {c['campaign_id']: c for c in L.AUDIT['campaigns']}
rank_orders_day = collections.Counter()
rank_child_orders = collections.defaultdict(collections.Counter)
size_tos = collections.defaultdict(lambda: [0.0, 0.0])
for cid, r in L.CC_CAMP30.items():
    c = A.get(cid, {})
    if (r.get('matchType') == 'Exact' or ' Exact' in (r['campaignName'] or '')) and (c.get('objective') or r.get('objective')) == 'Ranking':
        syn = c.get('syntax') or r.get('syntax') or ''
        z = syn.split('|')[1] if '|' in syn else L.size_of_sku(c.get('child') or '')
        rank_orders_day[z] += (r.get('orders') or 0) / 30
        rank_child_orders[z][c.get('child')] += r.get('orders') or 0
for cid, r in L.CC_CAMP90.items():
    ch = child_of.get(cid)
    z = L.size_of_sku(ch or '')
    if z and r.get('tos_clicks'):
        size_tos[z][0] += r['tos_clicks']
        size_tos[z][1] += r['tos_clicks'] * (r.get('tos_cvr') or 0) / 100
SIZE_TOS_CVR = {z: v[1] / v[0] for z, v in size_tos.items() if v[0] >= 50}

# ---------------------------------------------------------------- preferred variation per size
pref = {}
for size in ('Queen', 'King', 'Full', 'Twin'):
    cands = []
    size_units = sum((s['e30'] or {}).get('units') or 0 for s in P['skus'] if s['size'] == size)
    size_units90 = sum((s['e90'] or {}).get('units') or 0 for s in P['skus'] if s['size'] == size)
    for s in P['skus']:
        if s['size'] != size or s.get('alias_of'):
            continue
        e3, e9, iv = s['e30'] or {}, s['e90'] or {}, s['inv']
        if (e9.get('units') or 0) < 0.03 * size_units90:
            continue
        pd = paid.get(s['sku'], {})
        own_tos = pd['tos_orders'] / pd['tos_clicks'] if pd and pd['tos_clicks'] >= 50 else None
        tos_cvr = own_tos or SIZE_TOS_CVR.get(size)
        tos_basis = 'own (≥50 top-of-search clicks, 90 days)' if own_tos else f'size average (own has {int(pd["tos_clicks"]) if pd else 0} top-of-search clicks) — estimate'
        cvr = pd['orders'] / pd['clicks'] if pd and pd['clicks'] >= 50 else None
        pba90 = e9.get('pba_unit')
        vel = max(iv['vel30'], iv['vel90'])                        # pace: the higher of 30- and 90-day (King Black was short of stock in the 30 days)
        stock_all = (iv['sellable'] or 0) + (iv['res_transfer'] or 0) + (iv['inbound_shipped_open'] or 0)
        q4_need = round(vel * Q4_FACTOR_DAYS)
        main_now = rank_child_orders[size].most_common(1)[0][0] if rank_child_orders[size] else None
        push_pace = vel + (0 if s['sku'] == main_now else rank_orders_day[size])
        days_push = round(stock_all / push_pace) if push_pace else None
        cands.append(dict(sku=s['sku'], asin=s['asin'], colour=s['colour'], units30=e3.get('units'), units90=e9.get('units'),
                          share_units90=round((e9.get('units') or 0) / size_units90, 4) if size_units90 else None,
                          sessions30=e3.get('sessions'), usp30=e3.get('usp'), pba_unit30=e3.get('pba_unit'), pba_unit90=pba90, be_acos30=e3.get('be_acos'),
                          be_acos90=e9.get('be_acos'), avg_price30=e3.get('avg_price'), paid_clicks90=int(pd['clicks']) if pd else 0,
                          paid_cvr90=round(cvr, 4) if cvr else None, tos_clicks90=int(pd['tos_clicks']) if pd else 0, tos_cvr90=round(tos_cvr, 4) if tos_cvr else None, tos_basis=tos_basis,
                          is_current_ranking_child=s['sku'] == main_now, push_pace=round(push_pace, 2), days_at_push_pace=days_push,
                          value_per_tos_click=round(pba90 * tos_cvr, 2) if (pba90 and tos_cvr) else None, sellable=iv['sellable'], transfer=iv['res_transfer'],
                          inbound=iv['inbound_shipped_open'], stock_all=stock_all, pace=round(vel, 2), days_all=round(stock_all / vel) if vel else None,
                          q4_need=q4_need, covers_q4=stock_all >= q4_need, lost_sales_units=iv['lost_sales_units']))
    # rule: among children with ≥60 days of stock at the pace they would sell with the size's ranking traffic on them,
    # at least 10% of the size's 90-day units (a proven seller), the highest profit per top-of-search click; none viable → the best seller, flagged, no push
    viable = [c for c in cands if (c['days_at_push_pace'] or 0) >= 60 and c['value_per_tos_click'] and c['value_per_tos_click'] > 0 and (c['share_units90'] or 0) >= 0.10]
    pick = max(viable, key=lambda c: c['value_per_tos_click']) if viable else max(cands, key=lambda c: c['units90'] or 0)
    pick_basis = 'highest profit per top-of-search click among proven sellers (≥10% of the size) with ≥60 days of stock at push pace' if viable else 'no child has 60 days of stock at push pace: best seller kept, no push'
    black = next((c for c in cands if c['colour'].lower() == 'black'), None)
    pref[size] = dict(candidates=sorted(cands, key=lambda c: -(c['units90'] or 0)), chosen=pick['sku'], black=black and black['sku'],
                      black_is_chosen=bool(black and black['sku'] == pick['sku']), size_units30=size_units, size_units90=size_units90, basis=pick_basis,
                      viable=[c['sku'] for c in viable], rank_orders_day=round(rank_orders_day[size], 1), current_ranking_child=rank_child_orders[size].most_common(1)[0][0] if rank_child_orders[size] else None)

# ---------------------------------------------------------------- back-up ranking children (used when the preferred child runs low or out)
# rule: other children with positive profit per top-of-search click and ≥5% of the size's 90-day units; first those with ≥60 days of stock at
# push pace (by profit per TOS click), then the rest by days at push pace (≥30 days) — the latter can carry the maintain level only
for size, v in pref.items():
    others = [c for c in v['candidates'] if c['sku'] != v['chosen'] and (c['value_per_tos_click'] or 0) > 0 and (c['share_units90'] or 0) >= 0.05]
    full = sorted([c for c in others if (c['days_at_push_pace'] or 0) >= 60], key=lambda c: -c['value_per_tos_click'])
    part = sorted([c for c in others if 30 <= (c['days_at_push_pace'] or 0) < 60], key=lambda c: -(c['days_at_push_pace'] or 0))
    chain = [dict(sku=c['sku'], level='push' if c in full else 'maintain only', days_at_push_pace=c['days_at_push_pace'], value_per_tos_click=c['value_per_tos_click'],
                  tos_cvr=c['tos_cvr90'], tos_basis=c.get('tos_basis'), share=c['share_units90'], stock=c['stock_all']) for c in (full + part)[:2]]
    if not chain:                      # nothing at ≥5%: allow ≥3% sellers with ≥30 days at push pace, flagged
        thin = sorted([c for c in v['candidates'] if c['sku'] != v['chosen'] and (c['value_per_tos_click'] or 0) > 0 and (c['share_units90'] or 0) >= 0.03
                       and (c['days_at_push_pace'] or 0) >= 30], key=lambda c: -(c['days_at_push_pace'] or 0))
        chain = [dict(sku=c['sku'], level=('push' if (c['days_at_push_pace'] or 0) >= 60 else 'maintain only') + ' (small seller, estimate)',
                      days_at_push_pace=c['days_at_push_pace'], value_per_tos_click=c['value_per_tos_click'], tos_cvr=c['tos_cvr90'], tos_basis=c.get('tos_basis'),
                      share=c['share_units90'], stock=c['stock_all']) for c in thin[:1]]
    v['backups'] = chain

# ---------------------------------------------------------------- rank ↔ purchase-share curve (own data: SQP Q3 × Rank Radar Q3 median)
pts = []
for k, r in L.SQP['q3'].items():
    rr = L.RADAR.get(k)
    if not rr or (r.get('purchasesTotalCount') or 0) < 60:
        continue
    ranks = [x['organicRank'] for x in rr['ranks'] if x['date'] >= '2026-07-01' and x['organicRank'] and x['organicRank'] < 101]
    if len(ranks) < 45:
        continue
    pts.append((st.median(ranks), r.get('purchasesAsinShare') or 0, k))
BANDS = [('1-3', 1, 3), ('4-5', 4, 5), ('6-10', 6, 10), ('11-20', 11, 20), ('21-40', 21, 40)]
curve = {}
for lab, lo, hi in BANDS:
    xs = [s for m, s, _ in pts if lo <= m <= hi]
    curve[lab] = dict(n=len(xs), median_share=round(st.median(xs), 4) if xs else None, p25=round(sorted(xs)[len(xs) // 4], 4) if len(xs) >= 4 else None)
TARGET_SHARE = {'≤3': curve['1-3']['median_share'], '≤5': curve['4-5']['median_share'], '≤10': curve['6-10']['median_share']}

# ---------------------------------------------------------------- ranking opportunity per term
BLACK_OF = {z: pref[z]['chosen'] for z in pref}
opp = []
for k, r in KW.items():
    q3 = r.get('sqp_q3')
    if r['cls'] not in ('Core satin/silk',) or not q3 or not q3.get('purchases'):
        continue
    col = r.get('colour')
    if col and col not in ('black',):
        continue                                             # colour terms are conversion terms, not ranking terms for the family
    size = r.get('size') if r.get('size') in BLACK_OF else None
    child = BLACK_OF[size or 'Queen']
    ch = SKU[child]
    mkt_day = q3['purchases'] / 91
    share = q3.get('our_purchase_share') or 0
    rank = r.get('radar_med7') or r.get('cc_rank_med30') or (r.get('asinsight') or {}).get('organic')
    if rank is None:
        continue
    target = '≤10' if rank > 10 else ('≤5' if rank > 5 else ('≤3' if rank > 3 else 'hold'))
    tshare = TARGET_SHARE.get(target)
    add_day = max(0.0, mkt_day * ((tshare or share) - share)) if target != 'hold' else 0.0
    m30, m90 = r['m30'] or {}, r['m90'] or {}
    cvr_term = (m90.get('orders') or 0) / m90['clicks'] if (m90.get('clicks') or 0) >= 50 else None
    pd = paid.get(child)
    cvr_child = pd['tos_orders'] / pd['tos_clicks'] if pd and pd['tos_clicks'] >= 50 else 0.15
    cvr = cvr_term or cvr_child
    cpc = (L.KW30P.get(k) or {}).get('tos_cpc') or m30.get('cpc') or m90.get('cpc')
    clicks_day = add_day / cvr if cvr else None
    cost_day = clicks_day * cpc if (clicks_day is not None and cpc) else None
    pba = (ch['e90'] or {}).get('pba_unit')
    invest_day = cost_day - add_day * pba if cost_day is not None and pba is not None else None
    opp.append(dict(keyword=k, size=size or '—', child=child, sqp_volume_q3=q3['volume'], mkt_purchases_day=round(mkt_day, 2), our_share=share,
                    share_q2=r.get('sqp_q2_share'), share_q4=r.get('sqp_q4_share'), our_cvr_sqp=q3.get('our_cvr'), mkt_cvr=q3.get('mkt_cvr'),
                    cvr_index=round(q3['our_cvr'] / q3['mkt_cvr'], 2) if q3.get('our_cvr') and q3.get('mkt_cvr') else None,
                    rank_now=rank, rank_radar=r.get('radar_med7'), rank_cc=r.get('cc_rank_med30'), rank_asinsight=(r.get('asinsight') or {}).get('organic'),
                    rank_best90=r.get('radar_best') or r.get('cc_rank_best90'), days_unranked=r.get('radar_days_unranked'), target=target, target_share=tshare,
                    add_purchases_day=round(add_day, 2), paid_cvr=round(cvr, 4) if cvr else None, cvr_source='term (90d, ≥50 clicks)' if cvr_term else 'child top-of-search (90d)',
                    tos_cpc=round(cpc, 2) if cpc else None, add_clicks_day=round(clicks_day, 1) if clicks_day is not None else None,
                    cost_day=round(cost_day, 2) if cost_day is not None else None, pba_unit=pba, invest_day=round(invest_day, 2) if invest_day is not None else None,
                    spend30=m30.get('spend'), clicks30=m30.get('clicks'), orders30=m30.get('orders'), acos30=m30.get('acos'), spend90=m90.get('spend'), acos90=m90.get('acos'),
                    be_acos=r.get('be_acos'), sp_rank=(r.get('radar_ppc') or {}).get('sp_rank')))
opp.sort(key=lambda x: -x['mkt_purchases_day'])

# ---------------------------------------------------------------- ranking set: the core terms that together hold 80% of the market's purchases
# (SQP Q3), ranked within the tracked range, on a size whose preferred child can take a push (≥60 days of stock at push pace)
MAX_CLICK_SHARE = 0.115                                      # our best observed click share on a term with ≥100 purchases (SQP Q3)
tot = sum(x['mkt_purchases_day'] for x in opp)
cum = 0.0
for x in opp:
    cum += x['mkt_purchases_day']
    x['cum_share_of_market'] = round(cum / tot, 4)
    in_pareto = cum - x['mkt_purchases_day'] < 0.80 * tot
    r = KW[x['keyword']]
    q3 = r['sqp_q3']
    x['mkt_clicks_day'] = round((q3.get('clicks') or 0) / 91, 1)
    x['ad_clicks_day_now'] = round(((r['m30'] or {}).get('clicks') or 0) / 30, 2)
    x['ad_orders_day_now'] = round(((r['m30'] or {}).get('orders') or 0) / 30, 2)
    x['radar_worst_q3'] = r.get('radar_worst')
    size_ok = pref.get(x['size'] if x['size'] != '—' else 'Queen', {}).get('basis', '').startswith('highest')
    unranked = (x['rank_now'] or 101) >= 101
    if not in_pareto:
        x['in_ranking_set'], x['set_reason'] = False, 'outside the terms holding 80% of market purchases'
    elif unranked:
        x['in_ranking_set'], x['set_reason'] = False, 'not ranked in the top 100 (no position to push from)'
    elif not size_ok:
        x['in_ranking_set'], x['set_reason'] = False, 'size has no child with 60 days of stock at push pace'
    else:
        x['in_ranking_set'] = True
        x['set_reason'] = ('push: rank ' + str(x['rank_now']) + ' → ' + x['target']) if x['target'] != 'hold' else 'defend: already top 3'
    # daily clicks the ranking campaign(s) should buy on this term: today's ad clicks + the clicks for the missing purchases, capped at the absorbable share
    cap = x['mkt_clicks_day'] * MAX_CLICK_SHARE
    want = x['ad_clicks_day_now'] + (x['add_clicks_day'] or 0)
    x['target_clicks_day'] = round(min(want, cap), 1) if x['in_ranking_set'] else None
    x['capped'] = bool(x['in_ranking_set'] and want > cap)
    x['target_cost_day'] = round(x['target_clicks_day'] * x['tos_cpc'], 2) if x['in_ranking_set'] and x['tos_cpc'] else None
RANK_SET = [x for x in opp if x['in_ranking_set']]
# second tier — "maintain": the next core terms up to 95% of market purchases where we already rank in the top 20 on a pushable size.
# They keep today's paid clicks at the top of search (no increase); price steps down only while their organic rank holds.
for x in opp:
    size_ok = pref.get(x['size'] if x['size'] != '—' else 'Queen', {}).get('basis', '').startswith('highest')
    if x['in_ranking_set']:
        x['tier'] = 'push'
    elif (x['cum_share_of_market'] - x['mkt_purchases_day'] / tot) < 0.95 and size_ok and (x['rank_now'] or 101) <= 20:
        x['tier'] = 'maintain'
        x['target_clicks_day'] = x['ad_clicks_day_now']
        x['target_cost_day'] = round(x['ad_clicks_day_now'] * x['tos_cpc'], 2) if x['tos_cpc'] else None
        x['set_reason'] = f"maintain: rank {x['rank_now']}, {x['mkt_purchases_day']} market purchases/day (80–95% band)"
    else:
        x['tier'] = None
MAINTAIN_SET = [x for x in opp if x['tier'] == 'maintain']
OUT = dict(preferred=pref, curve=curve, curve_points=[dict(rank=m, share=s, keyword=k) for m, s, k in sorted(pts)], target_share=TARGET_SHARE,
           q4_factor_days=round(Q4_FACTOR_DAYS, 1), opportunities=opp, ranking_set=[x['keyword'] for x in RANK_SET], maintain_set=[x['keyword'] for x in MAINTAIN_SET],
           maintain_cost_day=round(sum(x['target_cost_day'] or 0 for x in MAINTAIN_SET), 2),
           ranking_cost_day=round(sum(x['target_cost_day'] or 0 for x in RANK_SET), 2), max_click_share=MAX_CLICK_SHARE)
json.dump(OUT, open(L.OUT + 'ranking.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    for z, v in pref.items():
        print('   backups', [(b['sku'], b['level'], b['days_at_push_pace']) for b in v['backups']])
        print('==', z, 'chosen', v['chosen'], 'black', v['black'], v['black_is_chosen'], v['basis'], 'rank orders/d', v['rank_orders_day'], 'current', v['current_ranking_child'])
        for c in v['candidates'][:6]:
            print('   ', c['sku'], 'days@push', c['days_at_push_pace'], 'u90', c['units90'], 'share', c['share_units90'], 'pba90', c['pba_unit90'], 'tosCVR', c['tos_cvr90'], 'val/click', c['value_per_tos_click'], 'stock_all', c['stock_all'], 'pace', c['pace'], 'q4need', c['q4_need'], 'covers', c['covers_q4'], 'usp', c['usp30'])
    print(curve, TARGET_SHARE)
    print('ranking set', len(RANK_SET), 'cost/day', OUT['ranking_cost_day'], '| maintain', len(MAINTAIN_SET), OUT['maintain_cost_day'])
    for o in opp[:45]:
        print(f"{o['keyword']:30} {o['size']:5} mkt/d {o['mkt_purchases_day']:5.1f} share {o['our_share']*100:5.2f}% rank {o['rank_now']} → {o['target']} +{o['add_purchases_day']}/d cvr {o['paid_cvr']} cpc {o['tos_cpc']} +clicks/d {o['add_clicks_day']} cost/d {o['cost_day']} invest/d {o['invest_day']} cvrIdx {o['cvr_index']} | set {o['in_ranking_set']} now {o['ad_clicks_day_now']}c → {o['target_clicks_day']}c \${o['target_cost_day']} {o['set_reason']}")
