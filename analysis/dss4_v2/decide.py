"""Stage 8 — Final action for every campaign (612), built from this product's data only.
Order of judgement per campaign: objective → ranking tier / LTSF / defence → one owner per ranking term on the preferred child →
placement (top of search only where the campaign's own placement data supports it) → budget from the term's daily click target →
second-order checks (orders, sales, rank, placement mix, TACoS, stock, LTSF, competitors). Output: v2/out/decisions.json"""
import json, re, math, collections
import load as L
import colourmatch as CM

P = json.load(open(L.OUT + 'product.json'))
R = json.load(open(L.OUT + 'ranking.json'))
LT = json.load(open(L.OUT + 'ltsf.json'))
KW = {k['keyword']: k for k in json.load(open(L.OUT + 'keywords.json'))}
C = json.load(open(L.OUT + 'campaigns_base.json'))
AR = json.load(open(L.OUT + 'audit_review.json'))
SKU = {s['sku']: s for s in P['skus']}
ASIN2SKU = {}
for s in P['skus']:
    ASIN2SKU.setdefault(s['asin'], s['sku'])
OPP = {o['keyword']: o for o in R['opportunities']}
PUSH = {o['keyword'] for o in R['opportunities'] if o.get('tier') == 'push'}
MAINT = {o['keyword'] for o in R['opportunities'] if o.get('tier') == 'maintain'}
PREF = {z: v['chosen'] for z, v in R['preferred'].items()}
PUSH_SIZES = {z for z, v in R['preferred'].items() if v['basis'].startswith('highest')}
LTROW = {r['sku']: r for r in LT['rows']}
LTSF_TARGET = {z: [s for s in v if LTROW[s]['est_aged_left'] >= 20] for z, v in LT['targets_by_size'].items()}
FAM_SALES_DAY = P['family30']['Info']['Sales'] / 30
FAM_ADS_DAY = abs(P['family30']['Info'].get('Advertising') or 0) / 30
ROSTER = {e['competitorProductId']: (e.get('brandName') or '?') for e in L.MKT['roster']['entries']}
AUD = collections.defaultdict(list)
for a in AR:
    AUD[a['campaign_id']].append(a)
TBC = collections.defaultdict(list)                        # Sellerboard: one row per (campaign, target) with the live bid
try:
    for r in (json.load(open(L.RAW + 'sb_ppc/targets_by_campaign_W30.json')) + json.load(open(L.RAW + 'sb_ppc/targets_by_campaign_W90only.json'))):
        TBC[str(r.get('_campaign_id'))].append(r)
except Exception:
    pass
STEP = 0.15                                                 # one step on a non-ranking price: −15 %, re-read after 7 clean days (owner may change)
MIN_BID = 0.02
TOS_MAX = 900


def be(sku):
    return ((SKU.get(sku) or {}).get('e30') or {}).get('be_acos')


def pba(sku):
    return ((SKU.get(sku) or {}).get('e30') or {}).get('pba_unit') or 0


def days_cover(sku):
    return ((SKU.get(sku) or {}).get('inv') or {}).get('days_sellable_30')


def p_zero(clicks, cvr):
    return (1 - cvr) ** clicks if clicks else 1.0


def child_paid_cvr(sku):
    """the child's paid conversion across its campaigns (30 d); family figure if the child has <50 paid clicks"""
    cl = sum((c['m30'] or {}).get('clicks') or 0 for c in C if c['child'] == sku)
    od = sum((c['m30'] or {}).get('orders') or 0 for c in C if c['child'] == sku)
    return (od / cl) if cl >= 50 else 1572 / 11617


CVR_CHILD = {}


def cvr_of(sku):
    if sku not in CVR_CHILD:
        CVR_CHILD[sku] = child_paid_cvr(sku)
    return CVR_CHILD[sku]


def base_colour(c):
    c = (c or '').lower()
    for b in ('grey', 'gray', 'green', 'teal', 'ivory', 'taupe', 'rosewood', 'gold', 'orange', 'purple', 'black', 'white', 'blue', 'red', 'pink', 'champagne'):
        if b in c:
            return 'grey' if b == 'gray' else b
    return c


def colour_lt(colour_terms, size, child):
    """the LTSF SKU (≥20 aged units left) whose colour the term names (colourmatch rules); None if the child already is it or none matches"""
    if not colour_terms:
        return None
    if child and CM.matches(colour_terms[0], (SKU.get(child) or {}).get('colour'), child):
        return None                                   # the ad already shows the colour the shopper searched
    r = CM.ltsf_for_term(colour_terms[0], LT['rows'], SKU)
    return r['sku'] if r and r['sku'] != child else None


def terms_of(c):
    return list(c['targets'].keys())


def rivals(term):
    m = L.MKW.get(term) or {}
    rv = sorted(((ROSTER.get(int(k), k), v.get('organicRank'), v.get('spRank'), round(v.get('traffic') or 0)) for k, v in (m.get('rivalMetrics') or {}).items()
                 if v.get('organicRank') and v['organicRank'] <= 10), key=lambda x: x[1])
    return [dict(brand=b, organic=o, sp=s, traffic=t) for b, o, s, t in rv[:5]]


def cur_bids(c):
    """live target bids: Sellerboard targets-by-campaign, else the audit's target rows, else Command Center targets"""
    out = {}
    for r in TBC.get(c['campaign_id'], []):
        out[(r.get('Name') or '').lower()] = dict(bid=r.get('current_bid'), state=r.get('Status'), match=r.get('KeywordType'), src='sellerboard', id=r.get('Id'))
    a = next((x for x in L.AUDIT['campaigns'] if x['campaign_id'] == c['campaign_id']), None)
    for t in (a or {}).get('targets') or []:
        out.setdefault((t.get('label') or '').lower(), dict(bid=t.get('bid'), state=t.get('state'), match=t.get('match'), src='audit export', id=t.get('entity_id')))
    for t in (L.CC_TARGETS.get(c['campaign_id']) or {}).get('targets') or []:
        out.setdefault((t.get('target') or '').lower(), dict(bid=t.get('bid'), state=None, match=t.get('targetType'), src='command center', eff_tos=t.get('effBidTos'),
                                                            tos_is=t.get('tosImpressionShare')))
    return out


# ============================================================================ 1. ranking term owners (one enabled exact campaign per term)
exact = [c for c in C if c['ad_type'] == 'SP' and c['match'] == 'Exact' and c['target_type'] != 'ASIN']
owners, dups = {}, collections.defaultdict(list)
for term in sorted(PUSH | MAINT):
    o = OPP[term]
    size = o['size'] if o['size'] != '—' else 'Queen'
    pref = PREF[size]
    cands = [c for c in exact if term in c['targets']]
    if not cands:
        owners[term] = None
        continue

    def key(c):
        m9 = c['m90'] or {}
        return (c['status'] == 'ENABLED', c['child'] == pref, m9.get('clicks') or 0, len(c['targets']) == 1)
    best = max(cands, key=key)
    owners[term] = best['campaign_id']
    for c in cands:
        if c['campaign_id'] != best['campaign_id']:
            dups[c['campaign_id']].append(term)
OWNED = collections.defaultdict(list)
for t, cid in owners.items():
    if cid:
        OWNED[cid].append(t)

# ============================================================================ 2. per-campaign decision
DEC = []
for c in C:
    cid = c['campaign_id']
    m3, m9, sb3 = c['m30'] or {}, c['m90'] or {}, c['sb30'] or {}
    spend_day = (m3.get('spend') or sb3.get('spend') or 0) / 30
    clicks_day = (m3.get('clicks') or sb3.get('clicks') or 0) / 30
    orders_day = (m3.get('orders') or sb3.get('orders') or 0) / 30
    sales_day = (m3.get('sales') or sb3.get('sales') or 0) / 30
    acos = m3.get('acos') if m3 else sb3.get('acos')
    if (orders_day * 30) >= 3:
        ev_acos, ev_orders, ev_basis = acos, orders_day * 30, '30 days'
    elif (m9.get('orders') or 0) >= 3:
        ev_acos, ev_orders, ev_basis = m9.get('acos'), m9.get('orders'), '90 days'
    else:
        ev_acos, ev_orders, ev_basis = acos, orders_day * 30, '30 days'
    child = c['child']
    size = c['size']
    ts = terms_of(c)
    bids = cur_bids(c)
    d = dict(campaign_id=cid, name=c['name'], dd_asins=c['dd_asins'], ad_type=c['ad_type'], status=c['status'], match=c['match'], child=child, size=size, colour=c['colour'],
             terms=ts, budget=c['budget'], utilization=c['utilization'], tos_is=c['tos_is'], mods=c['mods'], strategy=c['strategy'],
             now=dict(spend_day=round(spend_day, 2), clicks_day=round(clicks_day, 2), orders_day=round(orders_day, 2), sales_day=round(sales_day, 2), acos=acos,
                      cvr=m3.get('cvr'), cpc=m3.get('cpc'), tos_share=m3.get('tos_share'), tos_cvr=m3.get('tos_cvr'), ros_cvr=m3.get('ros_cvr'), pp_cvr=m3.get('pp_cvr'),
                      tos_clicks=m3.get('tos_clicks'), ros_clicks=m3.get('ros_clicks'), pp_clicks=m3.get('pp_clicks'),
                      clicks90=m9.get('clicks'), orders90=m9.get('orders'), spend90=m9.get('spend'), acos90=m9.get('acos'),
                      tos_cvr90=m9.get('tos_cvr'), ros_cvr90=m9.get('ros_cvr'), pp_cvr90=m9.get('pp_cvr'), tos_clicks90=m9.get('tos_clicks'),
                      ros_clicks90=m9.get('ros_clicks'), pp_clicks90=m9.get('pp_clicks')),
             be_acos=be(child), current_bids=bids, audit=[dict(kind=a['kind'], current=a['current'], suggested=a['suggested']) for a in AUD.get(cid, [])])
    act = dict(state=None, child_to=None, budget_to=None, tos_to=None, ros_to=None, pp_to=None, strategy_to=None, bid_changes=[], negatives_add=[], ads_add=[],
               ads_pause=[])
    why, checks = [], {}
    plan_spend = spend_day
    plan_clicks = clicks_day
    plan_orders = orders_day
    role = c['role']
    rank_owned = OWNED.get(cid, [])
    dup_terms = dups.get(cid, [])

    # ---------------- other products sharing the list (satin fitted, bamboo)
    if re.search(r'D-SF-|BAMBOO|Bamboo', c['name'] or '') or (c['ad_type'] in ('SB', 'SBV') and not re.search(r'satin|silk', c['name'] or '', re.I)):
        role = 'Other product (out of scope)'
        why.append('Advertises another product (satin fitted sheet or bamboo); decided in that product\'s audit, not here')

    # ---------------- ranking owners
    elif rank_owned and c['status'] != 'ARCHIVED':
        tiers = {t: OPP[t]['tier'] for t in rank_owned}
        role = 'Ranking – push' if 'push' in tiers.values() else 'Ranking – maintain'
        sz = OPP[rank_owned[0]]['size'] if OPP[rank_owned[0]]['size'] != '—' else 'Queen'
        pref = PREF[sz]
        tgt_clicks = sum(OPP[t]['target_clicks_day'] or 0 for t in rank_owned)
        tgt_cost = sum(OPP[t]['target_cost_day'] or 0 for t in rank_owned)
        now_term_clicks = sum(OPP[t]['ad_clicks_day_now'] for t in rank_owned)
        if c['status'] != 'ENABLED':
            act['state'] = 'ENABLED'
            why.append('Paused owner of a ranking term: re-enable (keeps its history) rather than build a new campaign')
        if child != pref:
            act['child_to'] = pref
            act['ads_add'].append(pref)
            if child:
                act['ads_pause'].append(child)
            why.append(f"Advertises {child}; the {sz} ranking child is {pref} ({R['preferred'][sz]['basis']}). Add the {pref} product ad, pause {child}")
        # placement: top of search only where the campaign's own 90-day placement read supports it
        tc, tv = m9.get('tos_clicks') or 0, m9.get('tos_cvr')
        oth = [(m9.get('ros_clicks') or 0, m9.get('ros_cvr')), (m9.get('pp_clicks') or 0, m9.get('pp_cvr'))]
        oth_cl = sum(x[0] for x in oth)
        oth_cvr = (sum(x[0] * (x[1] or 0) for x in oth) / oth_cl) if oth_cl else None
        if tc >= 20 and (oth_cvr is None or tv is None or tv >= 0.9 * oth_cvr):
            support = f"supported: top-of-search CVR {tv:.1f}% on {tc} clicks vs {oth_cvr:.1f}% elsewhere (90 d)" if (tv is not None and oth_cvr is not None) else f"supported: {tc} top-of-search clicks, no competing placement read"
            tos_ok = True
        elif tc < 20:
            szcvr = R['preferred'][sz]['candidates'][0]['tos_cvr90'] if R['preferred'][sz]['candidates'] else None
            support = f"campaign has only {tc} top-of-search clicks in 90 d; judged on the {sz} preferred child's top-of-search CVR ({szcvr and round(szcvr * 100, 1)}%)"
            tos_ok = True
        else:
            support = f"NOT supported: top-of-search CVR {tv:.1f}% vs {oth_cvr:.1f}% elsewhere on {tc}/{oth_cl} clicks — keep rest-of-search/product pages open"
            tos_ok = False
        checks['placement'] = support
        # prices: keep today's top-of-search clearing price (never cut a ranking term); if it buys fewer clicks than the target, the budget moves first
        tos_now = [OPP[t]['tos_cpc'] for t in rank_owned if OPP[t]['tos_cpc']]
        tos_price = round(max(tos_now), 2) if tos_now else None
        cur_eff = []
        for t in rank_owned:
            b = bids.get(t) or {}
            if b.get('bid') is not None and c['mods'].get('tos') is not None:
                cur_eff.append(b['bid'] * (1 + (c['mods']['tos'] or 0) / 100))
        if cur_eff and tos_price:
            tos_price = round(max(tos_price, max(cur_eff)), 2) if role == 'Ranking – push' else tos_price
        if tos_ok and tos_price:
            base = max(MIN_BID, round(tos_price / (1 + TOS_MAX / 100), 2))
            act.update(tos_to=TOS_MAX, ros_to=0, pp_to=0, strategy_to='Dynamic bids - down only')
            for t in rank_owned:
                b = bids.get(t) or {}
                act['bid_changes'].append(dict(term=t, bid_from=b.get('bid'), bid_to=base, eff_tos_to=round(base * (1 + TOS_MAX / 100), 2), src=b.get('src')))
            why.append(f"Top-of-search only: modifier {TOS_MAX}%, base bid ${base} (top-of-search price ${round(base * (1 + TOS_MAX / 100), 2)}, "
                       f"= today's top-of-search CPC ${tos_price}); rest of search and product pages 0% → those placements drop to the ${base} base")
        elif tos_price:
            act.update(tos_to=max(c['mods'].get('tos') or 0, 100))
            for t in rank_owned:
                b = bids.get(t) or {}
                act['bid_changes'].append(dict(term=t, bid_from=b.get('bid'), bid_to=round(tos_price / 2, 2), eff_tos_to=tos_price, src=b.get('src')))
            why.append('Top-of-search weighted (modifier ≥100%) but rest-of-search/product pages kept, because the placement data does not support TOS-only')
        budget = max(5.0, math.ceil((tgt_cost + max(0.0, clicks_day - sum(OPP[t]['ad_clicks_day_now'] for t in rank_owned)) * ((spend_day / clicks_day) if clicks_day else 0)) * 1.2)) if tgt_cost else c['budget']
        act['budget_to'] = budget if budget != c['budget'] else None
        why.append(f"Budget ${budget}/day = the daily click target {round(tgt_clicks, 1)} × top-of-search CPC, +20% headroom "
                   f"(today {round(now_term_clicks, 1)} paid clicks/day on {', '.join(rank_owned[:3])}{'…' if len(rank_owned) > 3 else ''})")
        if c['utilization'] and c['utilization'] >= 90:
            why.append(f"Today the budget ${c['budget']} is {c['utilization']:.0f}% used — the campaign is budget-capped")
        # clicks this campaign buys on its other (non-ranking) terms stay as they are
        other_clicks = max(0.0, clicks_day - sum(OPP[t]['ad_clicks_day_now'] for t in rank_owned))
        other_cpc = (spend_day / clicks_day) if clicks_day else 0
        plan_spend = (tgt_cost or 0) + other_clicks * other_cpc if tgt_cost else spend_day
        plan_clicks = (tgt_clicks or 0) + other_clicks if tgt_clicks else clicks_day
        cv = (OPP[rank_owned[0]].get('paid_cvr') or cvr_of(pref))
        plan_orders = (tgt_clicks or 0) * cv + other_clicks * ((orders_day / clicks_day) if clicks_day else 0)
        # other terms in the same campaign that are not ranking terms → leave them, but note
        extra = [t for t in ts if t not in rank_owned]
        if extra:
            why.append(f"Also buys {len(extra)} other term(s) ({', '.join(extra[:3])}) — they follow the campaign's top-of-search setting")
        checks['rank'] = '; '.join(f"{t}: rank {OPP[t]['rank_now']} → {OPP[t]['target']} (Q3 {KW[t].get('radar_best')}–{KW[t].get('radar_worst')}), "
                                   f"market {OPP[t]['mkt_purchases_day']}/day" for t in rank_owned[:4])
        checks['competitors'] = {t: rivals(t) for t in rank_owned[:2]}

    # ---------------- duplicate exact on a ranking term (another campaign owns it)
    elif dup_terms and c['match'] == 'Exact':
        own = {t: owners[t] for t in dup_terms}
        others = [t for t in ts if t not in dup_terms]
        if not others:
            role = 'Duplicate of a ranking owner'
            act['state'] = 'PAUSED' if c['status'] == 'ENABLED' else None
            plan_spend, plan_clicks, plan_orders = 0, 0, 0
            why.append(f"Buys {', '.join(dup_terms)} exact, which campaign {', '.join(sorted(set(own.values())))} owns on the preferred child; "
                       f"the owner's budget is sized to the whole term target, so its clicks move there — pause this one (one owner keeps the rank read clean)")
        else:
            role = 'Exact with a duplicated ranking term'
            act['negatives_add'] = [dict(term=t, match='NEGATIVE_EXACT') for t in dup_terms]
            why.append(f"Negative-exact {', '.join(dup_terms)} here (owned by {', '.join(sorted(set(own.values())))}); keep its other terms")

    # ---------------- auto / broad / phrase → discovery and LTSF clearance
    elif c['match'] in ('Auto', 'Phrase', 'Broad') and c['ad_type'] == 'SP':
        role = 'Discovery / LTSF clearance'
        tgt = LTSF_TARGET.get(size or '', [])
        named_colour = any((KW.get(t) or {}).get('colour') not in (None, 'black') for t in ts)
        is_ltsf_campaign = bool(re.search(r'LTSF', c['name'] or '', re.I))
        if is_ltsf_campaign and len(c['dd_asins']) > 1:
            adv = [ASIN2SKU.get(a, a) for a in c['dd_asins']]
            lt_top = [r['sku'] for r in LT['rows'] if r['est_aged_left'] >= 20]
            missing = [s for s in lt_top[:12] if s not in adv]
            not_lt = [s for s in adv if s not in LTROW]
            cleared = [s for s in adv if s in LTROW and LTROW[s]['est_aged_left'] < 1]
            act['ads_add'] = missing
            act['ads_pause'] = not_lt + cleared
            why.append(f"LTSF campaign advertising {len(adv)} SKUs: add the LTSF SKUs it is missing ({', '.join(missing) or 'none'}); pause the {len(not_lt)} SKUs not on the "
                       f"LTSF sheet and the {len(cleared)} whose aged units are estimated cleared — the budget then buys clicks for the aged units only")
        elif tgt and child not in tgt and not named_colour and child != PREF.get(size or ''):
            act['child_to'] = tgt[0]
            act['ads_add'].append(tgt[0])
            if child:
                act['ads_pause'].append(child)
            lr = LTROW[tgt[0]]
            why.append(f"Route to {tgt[0]}: LTSF #{lr['rank']} (${lr['total_ais']} AIS, ~{lr['est_aged_left']} aged units left, {lr['sellable_now']} sellable); "
                       f"{child} is not an LTSF priority")
        elif tgt and child == PREF.get(size or '') and size in ('Queen',) and not named_colour:
            act['child_to'] = tgt[0]
            act['ads_add'].append(tgt[0])
            act['ads_pause'].append(child)
            lr = LTROW[tgt[0]]
            why.append(f"Move off {child} (the ranking child, {days_cover(child)} days of stock and nothing inbound — keep it for the ranking terms) onto "
                       f"{tgt[0]}: LTSF #{lr['rank']}, ~{lr['est_aged_left']} aged units left")
        # a discovery campaign that advertises the same ranking child competes with the owner for the same term (and buys it off the top of search):
        # negative-exact that size's push terms there. Discovery on LTSF children keeps the head terms — they are where aged stock sells.
        fin = act['child_to'] or child
        if c['status'] == 'ENABLED' and size and fin == PREF.get(size):
            neg = sorted(t for t in PUSH if owners.get(t) and (OPP[t]['size'] == size or (OPP[t]['size'] == '—' and size == 'Queen')))
            act['negatives_add'] = [dict(term=t, match='NEGATIVE_EXACT', scope='campaign') for t in neg]
            if neg:
                why.append(f"Advertises the {size} ranking child: negative-exact its {len(neg)} push terms here so they are bought top-of-search-only in their owner campaigns")
        b_ = be(act['child_to'] or child)
        lrow = LTROW.get(act['child_to'] or child) or {}
        lt_adj = lrow.get('avoid_per_unit') or 0 if (lrow.get('est_aged_left') or 0) > 0 else 0
        price = ((SKU.get(act['child_to'] or child) or {}).get('e30') or {}).get('avg_price') or 30
        be_adj = (b_ or 0) + lt_adj / price
        if ev_acos is not None and b_ and ev_acos / 100 > be_adj and ev_orders >= 3:
            act['bid_changes'].append(dict(term='(all targets)', change=f'−{int(STEP * 100)}%', reason='step toward break-even'))
            plan_spend = spend_day * (1 - STEP)
            plan_clicks = clicks_day * (1 - STEP)
            plan_orders = orders_day * (1 - STEP)
            why.append(f"ACoS {ev_acos}% vs break-even {be_adj * 100:.1f}% (incl. ${lt_adj}/unit storage/AIS avoided, LTSF sheet) on {ev_orders:.0f} orders ({ev_basis}): one −{int(STEP * 100)}% step, "
                       f"re-read after 7 days — not a one-shot cut to break-even")
        elif c['status'] == 'ENABLED' and clicks_day * 30 >= 20 and orders_day == 0 and p_zero(clicks_day * 30, cvr_of(child)) < 0.05:
            act['state'] = 'PAUSED'
            plan_spend = plan_clicks = plan_orders = 0
            why.append(f"{clicks_day * 30:.0f} clicks, 0 orders in 30 days (chance of that at this child's paid CVR {cvr_of(child) * 100:.1f}% = "
                       f"{p_zero(clicks_day * 30, cvr_of(child)) * 100:.1f}%): pause")
        else:
            why.append((f"Keep: ACoS {acos}% vs break-even {be_adj * 100:.1f}%" + (f" (LTSF-adjusted: selling an aged unit avoids ${lt_adj} of storage/AIS)" if lt_adj else ''))
                       if acos is not None else 'Keep: no spend in 30 days')

    # ---------------- brand defence / product targeting / SB / SD
    elif role in ('Brand / listing defence',):
        why.append(f"Brand defence: ACoS {acos}% — keep; protects our own pages and brand searches")
    elif role == 'Product targeting':
        if ev_acos is not None and be(child) and ev_acos / 100 > be(child) and ev_orders >= 3:
            act['bid_changes'].append(dict(term='(all targets)', change=f'−{int(STEP * 100)}%', reason='step toward break-even'))
            plan_spend, plan_clicks, plan_orders = spend_day * (1 - STEP), clicks_day * (1 - STEP), orders_day * (1 - STEP)
            why.append(f"Competitor-page targeting at ACoS {ev_acos}% vs break-even {be(child) * 100:.1f}% on {ev_orders:.0f} orders ({ev_basis}): one −15% step")
        elif c['status'] == 'ENABLED' and clicks_day * 30 >= 20 and orders_day == 0 and p_zero(clicks_day * 30, cvr_of(child)) < 0.05:
            act['state'] = 'PAUSED'
            plan_spend = plan_clicks = plan_orders = 0
            why.append(f"{clicks_day * 30:.0f} clicks, 0 orders: pause")
        else:
            why.append(f"Keep: ACoS {acos}%" if acos is not None else 'Keep: no spend in 30 days')
    elif c['ad_type'] in ('SB', 'SBV', 'SD'):
        why.append(f"{c['ad_type']}: ${spend_day * 30:.0f} in 30 days, {orders_day * 30:.0f} orders — keep as is; see the video section for the SB-video plan")

    # ---------------- remaining exact: colour terms, long-tail, off-core, twin on hold
    elif c['match'] == 'Exact':
        colour_terms = [t for t in ts if (KW.get(t) or {}).get('colour') not in (None, 'black')]
        twin_rank = [t for t in ts if t in OPP and OPP[t]['size'] == 'Twin']
        ltsf_child = child in LTROW and LTROW[child]['est_aged_left'] >= 20
        if twin_rank:
            role = 'Ranking term, size on hold (stock)'
        elif colour_terms:
            role = 'Colour exact' + (' (LTSF)' if ltsf_child else '')
        elif role == 'Exact: off-core term':
            role = 'Off-core exact'
        else:
            role = 'Long-tail exact (non-ranking)'
        zero_sig = c['status'] == 'ENABLED' and clicks_day * 30 >= 20 and orders_day == 0 and p_zero(clicks_day * 30, cvr_of(child)) < 0.05
        if zero_sig:
            act['state'] = 'PAUSED'
            plan_spend = plan_clicks = plan_orders = 0
            why.append(f"{clicks_day * 30:.0f} clicks, 0 orders in 30 days (chance at the child's paid CVR {cvr_of(child) * 100:.1f}% = "
                       f"{p_zero(clicks_day * 30, cvr_of(child)) * 100:.1f}%): pause")
        elif role.startswith('Colour exact') and ltsf_child:
            vol = max(((KW.get(t) or {}).get('sqp_q3') or {}).get('volume') or 0 for t in colour_terms)
            o90 = (m9.get('orders') or 0)
            if c['status'] != 'ENABLED' and (vol >= 1000 or o90 >= 3):
                act['state'] = 'ENABLED'
                plan_spend = max(spend_day, (m9.get('spend') or 0) / 91)
                plan_clicks = max(clicks_day, (m9.get('clicks') or 0) / 91)
                plan_orders = max(orders_day, o90 / 91)
                why.append(f"Paused colour exact on an LTSF child ({child}, LTSF #{LTROW[child]['rank']}, ~{LTROW[child]['est_aged_left']} aged units left); "
                           f"the term has {vol:,} searches in Q3 / {o90} orders in 90 days — re-enable it to clear aged stock")
            else:
                why.append(f"Colour term on an LTSF child ({child}, LTSF #{LTROW[child]['rank']}, ~{LTROW[child]['est_aged_left']} aged units left): keep — it clears aged stock")
        elif role.startswith('Colour exact') and colour_lt(colour_terms, size, child):
            t0 = colour_lt(colour_terms, size, child)
            act['child_to'] = t0
            act['ads_add'].append(t0)
            if child:
                act['ads_pause'].append(child)
            role = 'Colour exact (LTSF)'
            why.append(f"Colour term '{colour_terms[0]}' matches LTSF SKU {t0} (LTSF #{LTROW[t0]['rank']}, ~{LTROW[t0]['est_aged_left']} aged units left); "
                       f"today it advertises {child} — move the ad to the aged stock of the same colour")
        elif role == 'Ranking term, size on hold (stock)':
            tb = PREF['Twin']
            why.append(f"Twin ranking term, but Twin's best child {tb} has {R['preferred']['Twin']['candidates'][0]['days_at_push_pace']} days of stock at push pace "
                       f"(needs 60): hold spend flat until it is restocked, then push")
        elif ev_acos is not None and be(child) and ev_acos / 100 > be(child) and ev_orders >= 3:
            act['bid_changes'].append(dict(term='(all targets)', change=f'−{int(STEP * 100)}%', reason='step toward break-even; stop if the term\'s organic rank slips ≥3 places'))
            plan_spend, plan_clicks, plan_orders = spend_day * (1 - STEP), clicks_day * (1 - STEP), orders_day * (1 - STEP)
            why.append(f"Not a ranking term (outside 95% of market purchases or unranked). ACoS {ev_acos}% vs break-even {be(child) * 100:.1f}% on {ev_orders:.0f} orders ({ev_basis}): "
                       f"one −15% step, re-read after 7 days, stop stepping if organic rank slips ≥3 places")

        elif c['status'] == 'ENABLED' and spend_day > 0:
            if acos is None:
                why.append(f"Keep: ${spend_day * 30:.0f} spend, {clicks_day * 30:.0f} clicks, 0 orders in 30 days — too few clicks to call it (a pause needs ≥20 clicks with 0 orders)")
            else:
                why.append(f"Keep: ACoS {acos}% vs break-even {be(child) and round(be(child) * 100, 1)}% on {orders_day * 30:.0f} orders")
        else:
            why.append('Paused or no spend in 30 days — no change' if c['status'] != 'ENABLED' else 'Enabled, no spend in 30 days — no change')
    else:
        why.append('No spend and no ranking role — no change' if not spend_day else f'Keep ({role})')

    # ---------------- non-ranking Queen exact on the Queen ranking child → Queen's LTSF #1 (keeps Queen Black's stock for the ranking terms)
    if role in ('Long-tail exact (non-ranking)', 'Off-core exact') and c['status'] == 'ENABLED' and size == 'Queen' and child == PREF['Queen'] \
            and LTSF_TARGET.get('Queen') and (m9.get('spend') or 0) > 0 and act['state'] != 'PAUSED' and not act['child_to']:
        t0 = LTSF_TARGET['Queen'][0]
        act['child_to'] = t0
        act['ads_add'].append(t0)
        act['ads_pause'].append(child)
        why.append(f"Move off {child} (Queen ranking child, {days_cover(child)} days of stock, nothing inbound) onto {t0} (LTSF #1, ~{LTROW[t0]['est_aged_left']} aged units): "
                   f"not a ranking term, so its orders are better spent clearing aged stock")

    # ---------------- second-order checks (all actions)
    d_sp, d_cl, d_or = plan_spend - spend_day, plan_clicks - clicks_day, plan_orders - orders_day
    ch = act['child_to'] or child
    aov = sales_day / orders_day if orders_day else (((SKU.get(ch) or {}).get('e30') or {}).get('avg_price') or 30)
    checks.update(d_spend_day=round(d_sp, 2), d_clicks_day=round(d_cl, 2), d_orders_day=round(d_or, 2), d_sales_day=round(d_or * aov, 2),
                  d_profit_day=round(d_or * pba(ch) - d_sp, 2), d_tacos_pts=round(d_sp / FAM_SALES_DAY * 100, 3),
                  stock_child_days=days_cover(ch), ltsf=(LTROW.get(ch) or {}).get('rank'))
    if act['state'] == 'PAUSED' or (d_sp < -0.5 and role.startswith(('Long', 'Colour', 'Discovery', 'Off', 'Product'))):
        rk = [t for t in ts if t in OPP]
        checks['rank_risk'] = ('none on the ranking set: ' + (', '.join(f"{t} rank {OPP[t]['rank_now']}" for t in rk[:3]) if rk else 'no SQP-tracked term')) \
            if not any(t in PUSH | MAINT for t in ts) else 'ranking term — see owner'
    d.update(role=role, action=act, why=why, checks=checks, plan=dict(spend_day=round(plan_spend, 2), clicks_day=round(plan_clicks, 2), orders_day=round(plan_orders, 2)),
             owned_terms=rank_owned, duplicate_of={t: owners[t] for t in dup_terms})
    DEC.append(d)

# ============================================================================ 3. ranking terms with no campaign → new exact (only where nothing exists)
NEW = []
NO_OWNER_MAINTAIN = []
for t, cid in owners.items():
    if cid is None and OPP[t]['tier'] == 'maintain':
        NO_OWNER_MAINTAIN.append(t)       # today's clicks on it come from discovery campaigns; holding them needs no new campaign
    elif cid is None:
        o = OPP[t]
        sz = o['size'] if o['size'] != '—' else 'Queen'
        base = max(MIN_BID, round((o['tos_cpc'] or 1.5) / (1 + TOS_MAX / 100), 2))
        NEW.append(dict(term=t, tier=o['tier'], match='Exact', child=PREF[sz], budget=max(5.0, math.ceil((o['target_cost_day'] or 3) * 1.2)), base_bid=base, tos=TOS_MAX,
                        ros=0, pp=0, strategy='Dynamic bids - down only', target_clicks_day=o['target_clicks_day'],
                        why=f"'{t}' is a {o['tier']} ranking term ({o['mkt_purchases_day']} market purchases/day, rank {o['rank_now']}) and no campaign — enabled or paused — buys it exact"))

# ============================================================================ 4. spend and click share after the plan
share = collections.Counter()
share_c = collections.Counter()
now_s = collections.Counter()
now_c = collections.Counter()
for d in DEC:
    if d['role'] == 'Other product (out of scope)':
        continue
    grp = 'ranking' if d['role'].startswith('Ranking –') else 'non-ranking'
    share[grp] += d['plan']['spend_day']
    share_c[grp] += d['plan']['clicks_day']
    now_s['ranking' if d['role'].startswith('Ranking –') or d['role'] == 'Duplicate of a ranking owner' else 'non-ranking'] += d['now']['spend_day']
    now_c['ranking' if d['role'].startswith('Ranking –') or d['role'] == 'Duplicate of a ranking owner' else 'non-ranking'] += d['now']['clicks_day']
for n in NEW:
    share['ranking'] += (OPP[n['term']]['target_cost_day'] or 0)
    share_c['ranking'] += (OPP[n['term']]['target_clicks_day'] or 0)
SUMMARY = dict(plan_spend_day=dict(share), plan_clicks_day=dict(share_c), now_spend_day=dict(now_s), now_clicks_day=dict(now_c),
               plan_ranking_spend_share=round(share['ranking'] / sum(share.values()), 3), plan_ranking_click_share=round(share_c['ranking'] / sum(share_c.values()), 3),
               now_ranking_spend_share=round(now_s['ranking'] / sum(now_s.values()), 3), now_ranking_click_share=round(now_c['ranking'] / sum(now_c.values()), 3),
               new_campaigns=len(NEW), owners=len([1 for v in owners.values() if v]), roles=collections.Counter(d['role'] for d in DEC))
json.dump(dict(decisions=DEC, new_campaigns=NEW, no_owner_maintain=NO_OWNER_MAINTAIN, owners=owners, summary=SUMMARY, ltsf_targets=LTSF_TARGET), open(L.OUT + 'decisions.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    print(json.dumps(SUMMARY, indent=1, default=str))
    for n in NEW:
        print('NEW', n['term'], n['child'], n['budget'], n['base_bid'])
