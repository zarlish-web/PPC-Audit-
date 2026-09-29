"""Stage 7 — Every non-cosmetic decision in the audit export, re-judged on the campaign's objective and its second-order effects
(sales, organic rank and momentum, placement mix, TACoS/profit, stock, LTSF, competitors), not on break-even alone.
Output: v2/out/audit_review.json"""
import json, re, collections, statistics as st
import load as L

P = json.load(open(L.OUT + 'product.json'))
R = json.load(open(L.OUT + 'ranking.json'))
KW = {k['keyword']: k for k in json.load(open(L.OUT + 'keywords.json'))}
CB = {c['campaign_id']: c for c in json.load(open(L.OUT + 'campaigns_base.json'))}
LT = {r['sku']: r for r in json.load(open(L.RAW + 'ltsf/ltsf.json'))['rows']}
SKU = {s['sku']: s for s in P['skus']}
OPP = {o['keyword']: o for o in R['opportunities']}
RANK_SET = set(R['ranking_set'])
PREF = {z: v['chosen'] for z, v in R['preferred'].items()}
PUSH = {z for z, v in R['preferred'].items() if v['basis'].startswith('highest')}
ROSTER = {e['competitorProductId']: (e.get('brandName') or e.get('label') or '?') for e in L.MKT['roster']['entries']}
FAM_SALES_DAY = P['family30']['Info']['Sales'] / 30
LTSF_RANK = {s: i + 1 for i, s in enumerate(LT)}

# our paid clicks per term per day, all campaigns (Command Center keyword lens, 30 d)
AD_CLICKS_DAY = {k: ((v['m30'] or {}).get('clicks') or 0) / 30 for k, v in KW.items()}
COSMETIC = {'rename', 'retag'}


def child_facts(sku):
    s = SKU.get(sku) or {}
    e3, iv = s.get('e30') or {}, s.get('inv') or {}
    lt = LT.get(sku)
    return dict(sku=sku, size=s.get('size'), colour=s.get('colour'), units30=e3.get('units'), pba_unit=e3.get('pba_unit'), be_acos=e3.get('be_acos'),
                sellable=iv.get('sellable'), days_cover=iv.get('days_sellable_30'), inbound=iv.get('inbound_shipped_open'),
                ltsf_rank=LTSF_RANK.get(sku), ltsf_ais=lt and lt['total_ais'], ltsf_units=lt and lt['ais_units'], ltsf_oldest=lt and lt['oldest_bucket'])


def term_facts(t):
    k = KW.get(t) or {}
    o = OPP.get(t) or {}
    q3 = k.get('sqp_q3') or {}
    m = L.MKW.get(t) or {}
    riv = sorted(((ROSTER.get(int(cid), cid), v.get('organicRank'), v.get('spRank')) for cid, v in (m.get('rivalMetrics') or {}).items()
                  if v.get('organicRank') and v['organicRank'] <= 10), key=lambda x: x[1])[:5]
    first, last = k.get('radar_med_first14'), k.get('radar_med7')
    trend = None if first is None or last is None else ('improving' if last < first - 1 else 'slipping' if last > first + 1 else 'flat')
    vol = None
    if k.get('radar_best') and k.get('radar_worst'):
        vol = 'volatile' if k['radar_worst'] - k['radar_best'] >= 10 else 'steady'
    return dict(term=t, in_ranking_set=t in RANK_SET, mkt_purchases_day=round((q3.get('purchases') or 0) / 91, 2), mkt_clicks_day=round((q3.get('clicks') or 0) / 91, 1),
                our_purchase_share=q3.get('our_purchase_share'), rank_now=k.get('radar_now') or k.get('cc_rank_last'), rank_med7=last, rank_first14=first,
                rank_best_q3=k.get('radar_best'), rank_worst_q3=k.get('radar_worst'), trend=trend, volatility=vol, our_ad_clicks_day=round(AD_CLICKS_DAY.get(t, 0), 2),
                target=o.get('target'), target_clicks_day=o.get('target_clicks_day'), rivals_top10=riv, cls=k.get('cls'), colour=k.get('colour'), size=k.get('size'))


def camp_facts(c):
    m3 = c.get('m30') or {}
    sb = c.get('sb30') or {}
    clicks_day = (m3.get('clicks') or 0) / 30
    return dict(clicks_day=round(clicks_day, 2), orders_day=round((m3.get('orders') or 0) / 30, 2), spend_day=round((m3.get('spend') or 0) / 30, 2),
                sales_day=round((m3.get('sales') or 0) / 30, 2), cvr=m3.get('cvr'), cpc=m3.get('cpc'), acos=m3.get('acos'), tos_share=m3.get('tos_share'),
                tos_cvr=m3.get('tos_cvr'), ros_cvr=m3.get('ros_cvr'), pp_cvr=m3.get('pp_cvr'), budget=c.get('budget'), utilization=sb.get('utilization'),
                tos_is=sb.get('tos_is'), orders90=(c.get('m90') or {}).get('orders'), clicks90=(c.get('m90') or {}).get('clicks'))


def num(x):
    try:
        return float(str(x).replace('$', '').replace(',', ''))
    except (TypeError, ValueError):
        return None


def impact(cf, ch, frac_clicks):
    """change in clicks/orders/sales/spend/profit per day if the campaign's clicks move by frac_clicks (−0.3 = −30 %)"""
    dc = cf['clicks_day'] * frac_clicks
    cvr = (cf['cvr'] or 0) / 100
    do = dc * cvr
    aov = cf['sales_day'] / cf['orders_day'] if cf['orders_day'] else None
    ds = do * aov if aov else 0.0
    dsp = cf['spend_day'] * frac_clicks
    dp = do * (ch.get('pba_unit') or 0) - dsp
    return dict(d_clicks_day=round(dc, 2), d_orders_day=round(do, 2), d_sales_day=round(ds, 2), d_spend_day=round(dsp, 2), d_profit_day=round(dp, 2),
                d_tacos_pts=round(dsp / FAM_SALES_DAY * 100, 3))


rows = []
for d in L.AUDIT['decisions']:
    if d['kind'] in COSMETIC:
        continue
    cid = d.get('campaign_id')
    c = CB.get(cid) or {}
    terms = list((c.get('targets') or {}).keys())
    ent = d.get('entity') or ''
    if ent.startswith('target · '):
        terms = [ent.split('target · ', 1)[1].strip().lower()]
    tf = [term_facts(t) for t in terms if t in KW]
    main = max(tf, key=lambda x: x['mkt_purchases_day'], default=None)
    cf = camp_facts(c) if c else None
    child = c.get('child')
    chf = child_facts(child) if child else {}
    role = c.get('role') or ('Proposed new campaign' if d['kind'] == 'build' else '?')
    share_of_term = None
    if main and cf and main['our_ad_clicks_day']:
        share_of_term = round(min(1.0, cf['clicks_day'] / main['our_ad_clicks_day']), 3)
    cur, sug = d.get('current_at_audit'), d.get('suggested')
    ev = dict(seq=d['seq'], kind=d['kind'], campaign_id=cid, campaign=d['campaign'], entity=ent, current=cur, suggested=sug, audit_objective=d.get('objective'),
              audit_rule=d.get('rule'), audit_why=(d.get('why') or '')[:600], cites_b6='B6' in json.dumps(d), role=role, main_term=main, terms=[t['term'] for t in tf],
              campaign_now=cf, child=chf, campaign_share_of_our_paid_clicks_on_term=share_of_term)
    verdict, reason, est = None, [], None
    in_rank = bool(main and main['in_ranking_set'])
    k = d['kind']

    if k == 'child':
        to = sug
        tof = child_facts(to)
        ev['child_to'] = tof
        if role == 'Ranking' or in_rank:
            size = chf.get('size')
            pref = PREF.get(size)
            if size in PUSH and child == pref:
                verdict = 'REJECT'
                reason.append(f"Ranking campaign already on the preferred child {pref}; the move to {to} would put ranking traffic on a child that converts "
                              f"at {tof.get('be_acos') and '—'} a weaker, unproven rate")
            elif size in PUSH:
                verdict = 'MODIFY'
                reason.append(f"Ranking term: move it to the preferred child {pref}, not to {to}")
            else:
                verdict = 'HOLD'
                reason.append(f"{size} has no child with 60 days of stock at push pace, so no ranking move; keep as is until {PREF.get(size)} is restocked")
            # data on the two children, stated
            sf, tf2 = SKU.get(child, {}), SKU.get(to, {})
            reason.append(f"From {child}: {chf.get('sellable')} sellable, {chf.get('days_cover')} days; to {to}: {tof.get('sellable')} sellable, "
                          f"{tof.get('units30')} units in 30 days, profit before ads ${tof.get('pba_unit')}/unit vs ${chf.get('pba_unit')}")
            if tof.get('ltsf_rank'):
                reason.append(f"{to} is LTSF #{tof['ltsf_rank']} (${tof['ltsf_ais']} AIS on {tof['ltsf_units']:.0f} units): clear it through auto/broad/phrase and "
                              f"its own colour terms, not through the ranking terms")
        else:
            if tof.get('ltsf_rank') and not chf.get('ltsf_rank'):
                verdict = 'ACCEPT'
                reason.append(f"Non-ranking campaign; {to} is LTSF #{tof['ltsf_rank']} (${tof['ltsf_ais']} AIS) — routing its traffic there serves the LTSF goal")
            elif main and main.get('colour') and main['colour'] not in (tof.get('colour') or ''):
                verdict = 'REJECT'
                reason.append(f"Term names the colour '{main['colour']}', the new child is {tof.get('colour')} — the ad would not match the search")
            else:
                verdict = 'REVIEW'
                reason.append('Non-ranking campaign; neither child is an LTSF priority — no data reason to move')

    elif k in ('bid', 'budget', 'tos'):
        a, b = num(cur), num(sug)
        frac = (b / a - 1) if a and b is not None and a > 0 else None
        if k == 'tos' and a is not None and b is not None:
            frac = (1 + b / 100) / (1 + a / 100) - 1          # change in the top-of-search price at a fixed base bid
        if k == 'budget' and cf and (cf['utilization'] or 0) < 80 and frac is not None:
            frac_eff = min(0.0, (b - cf['spend_day'] * 1.0) / cf['spend_day']) if cf['spend_day'] else 0.0
            frac_eff = max(frac_eff, frac)
        else:
            frac_eff = frac
        est = impact(cf, chf, frac_eff) if (cf and frac_eff is not None) else None
        ev['change_pct'] = round(frac * 100, 1) if frac is not None else None
        ev['impact_estimate'] = est
        if in_rank and frac is not None and frac < 0:
            rising = main['target_clicks_day'] and main['target_clicks_day'] > main['our_ad_clicks_day']
            verdict = 'REJECT'
            reason.append(f"'{main['term']}' is a ranking term (market {main['mkt_purchases_day']}/day purchases, rank {main['rank_med7']} "
                          f"{'(' + main['trend'] + ')' if main['trend'] else ''}, Q3 range {main['rank_best_q3']}–{main['rank_worst_q3']}); "
                          f"this campaign carries {share_of_term and round(share_of_term * 100)}% of our paid clicks on it")
            if est:
                reason.append(f"The cut removes about {abs(est['d_clicks_day'])} clicks and {abs(est['d_orders_day'])} orders a day "
                              f"(${abs(est['d_sales_day'])} sales) to save ${abs(est['d_spend_day'])}/day; net profit effect ${est['d_profit_day']}/day, "
                              f"TACoS −{abs(est['d_tacos_pts'])} pts — a small saving against lost ranking sales on a term we are trying to climb")
            reason.append('Replaced by the ranking plan: top-of-search-only placement and a budget sized to the term\'s daily click target' +
                          (f" ({main['target_clicks_day']} clicks/day vs {main['our_ad_clicks_day']} now)" if main['target_clicks_day'] else ''))
        elif frac is not None and frac < 0:
            acos, be = (cf or {}).get('acos'), chf.get('be_acos')
            if acos is not None and be and acos / 100 > be and (cf['orders_day'] * 30) >= 3:
                verdict = 'ACCEPT' if frac >= -0.3 else 'MODIFY'
                reason.append(f"Not a ranking term; ACoS {acos}% vs break-even {be * 100:.1f}% on {cf['orders_day'] * 30:.0f} orders in 30 days — trimming toward break-even is right" +
                              ('' if frac >= -0.3 else '; but step it (−15% now, re-read after 7 days) rather than ' + f"{frac * 100:.0f}% at once"))
            elif acos is not None and be and acos / 100 <= be:
                verdict = 'REJECT'
                reason.append(f"ACoS {acos}% is already inside break-even {be * 100:.1f}% — cutting loses profitable orders")
            else:
                verdict = 'REVIEW'
                reason.append('Too few orders to judge the cut on 30 days')
            if est:
                reason.append(f"Effect: {est['d_clicks_day']} clicks, {est['d_orders_day']} orders, ${est['d_sales_day']} sales, ${est['d_spend_day']} spend, "
                              f"${est['d_profit_day']} profit per day")
        else:
            verdict = 'ACCEPT' if in_rank else 'REVIEW'
            reason.append('Raises or holds the price' + (' on a ranking term — consistent with the push' if in_rank else ''))

    elif k in ('ros', 'pp'):
        if in_rank or role == 'Ranking':
            other = (cf or {}).get('ros_cvr' if k == 'ros' else 'pp_cvr')
            tos = (cf or {}).get('tos_cvr')
            verdict = 'ACCEPT'
            reason.append(f"Ranking campaign: rest-of-search/product-page modifiers to 0 keeps clicks at the top of search " +
                          (f"(top-of-search CVR {tos:.1f}% vs {k.upper()} {other:.1f}% in 30 days)" if tos is not None and other is not None else '(placement split not measured on this campaign)'))
        else:
            verdict = 'REVIEW'
            reason.append('Non-ranking campaign: placement modifiers follow the placement that converts; no ranking reason')

    elif k == 'state':
        if sug == 'PAUSED':
            dup = 'duplicate' in json.dumps(d).lower() or 'already buys' in json.dumps(d).lower()
            if in_rank and not dup:
                verdict = 'REJECT'
                reason.append(f"Only exact campaign carrying '{main['term']}' — pausing removes ranking traffic")
            elif dup:
                verdict = 'ACCEPT'
                reason.append('Another enabled exact campaign already buys the same term: one owner per term keeps the ranking read clean; '
                              'the owner must be on the preferred child and absorb this campaign\'s clicks (its budget is set from the term target)')
            else:
                acos, be = (cf or {}).get('acos'), chf.get('be_acos')
                verdict = 'ACCEPT' if (acos and be and acos / 100 > be) else 'REVIEW'
                reason.append(f"Non-ranking: ACoS {acos}% vs break-even {be and round(be * 100, 1)}%")
        else:
            verdict = 'REVIEW'
            reason.append('Re-enable: judged with the structure revivals')

    elif k == 'structure':
        if d.get('cites_b6') or 'B6' in json.dumps(d):
            reason.append('Rule text cites the B6 corrections document — a different product; re-decided here on this product\'s data only')
        if in_rank:
            verdict = 'ACCEPT'
            reason.append(f"'{main['term']}' is in the ranking set; reviving the paused exact owner keeps its history — put it on {PREF.get(main['size'] or 'Queen')} "
                          f"with top-of-search-only placement")
        elif main and (cf or {}).get('orders90'):
            verdict = 'REVIEW'
            reason.append(f"Not a ranking term (market {main['mkt_purchases_day']}/day purchases); revive only if the term fits an LTSF colour or a conversion need")
        else:
            verdict = 'REJECT'
            reason.append('No ranking role and no order history to justify reviving')

    elif k == 'build':
        verdict = 'REJECT' if ('SD' in (d['campaign'] or '') and 'OwnPage' in (d['campaign'] or '')) else 'REVIEW'
        reason.append('New campaign: only if the existing structure cannot do the job. ' +
                      ('Own-page SD defence on a child that is not the LTSF priority adds campaigns without an objective the data asks for' if verdict == 'REJECT'
                       else 'Competitor-page harvest: check the ASINs against existing product-targeting campaigns before building'))

    elif k == 'negatives':
        verdict = 'ACCEPT' if not in_rank else 'REVIEW'
        reason.append('Negative exact on served terms with no orders (the export gives counts, not the terms): ' +
                      ('safe on a discovery campaign — the ranking terms are bought by their exact owners' if not in_rank else 'check none of them is a ranking-set term'))

    ev['verdict'], ev['reason'] = verdict or 'REVIEW', reason
    rows.append(ev)

# ---------------------------------------------------------------- the verdict is read from the FINAL action on the campaign (decisions.json), so the
# review, the campaign tab and the document cannot disagree; the analysis above stays as the evidence
DD = json.load(open(L.OUT + 'decisions.json'))
DEC = {d['campaign_id']: d for d in DD['decisions']}
NEWT = {n['term'] for n in DD['new_campaigns']}


def f(x):
    return num(x)


for ev in rows:
    d = DEC.get(ev['campaign_id'])
    k, cur, sug = ev['kind'], ev['current'], ev['suggested']
    ev['analysis'] = ev.pop('reason')
    if not d:
        ev['verdict'], ev['final_action'] = ('REJECT', 'No campaign is built for this; see New campaigns') if k == 'build' else ('REVIEW', 'campaign not found')
        if k == 'build':
            ev['analysis'].append('Only new campaigns with no existing owner are built (New campaigns tab); this proposal is not one of them')
        continue
    a = d['action']
    ev['role'] = d['role']
    fin_txt = ''
    if k == 'child':
        fin = a['child_to'] or d['child']
        fin_txt = f"advertised child → {fin}"
        ev['verdict'] = 'ACCEPT' if fin == sug else ('REJECT' if fin == cur else 'MODIFY')
    elif k == 'state':
        fin = a['state'] or d['status']
        fin_txt = f"state → {fin}"
        ev['verdict'] = 'ACCEPT' if fin == sug else 'REJECT'
    elif k == 'structure':
        fin = a['state'] or d['status']
        fin_txt = f"state → {fin}"
        ev['verdict'] = 'ACCEPT' if ('ENABLE' in (sug or '').upper()) == (fin == 'ENABLED') else 'REJECT'
    elif k in ('budget', 'tos') and any(b.get('change') for b in a['bid_changes']) and (f(sug) or 0) < (f(cur) or 0):
        fin_txt = 'budget/modifier unchanged; all targets −15% (one step, re-read after 7 days, rank guard)'
        ev['verdict'] = 'MODIFY'
    elif k == 'budget':
        fb, c0, s0 = f(a['budget_to'] or d['budget']), f(cur), f(sug)
        fin_txt = f"budget → ${fb}"
        if None in (fb, c0, s0):
            ev['verdict'] = 'REVIEW'
        elif s0 < c0:
            ev['verdict'] = 'REJECT' if fb >= c0 else ('ACCEPT' if abs(fb - s0) <= 0.05 * c0 else 'MODIFY')
        else:
            ev['verdict'] = 'ACCEPT' if fb >= c0 else 'REJECT'
    elif k in ('tos', 'ros', 'pp'):
        fv = a[k + '_to'] if a[k + '_to'] is not None else d['mods'].get(k)
        fin_txt = f"{k.upper()} modifier → {fv}%"
        c0, s0 = f(cur), f(sug)
        if fv is None or s0 is None:
            ev['verdict'] = 'REVIEW' if fv is None else 'MODIFY'
        else:
            ev['verdict'] = 'ACCEPT' if abs(fv - s0) < 1 else ('MODIFY' if (c0 is not None and (fv - c0) * (s0 - c0) > 0) else 'REJECT')
    elif k == 'bid':
        term = ev['entity'].split('target · ', 1)[-1].strip().lower()
        bc = next((b for b in a['bid_changes'] if b.get('term') == term), None) or next((b for b in a['bid_changes'] if b.get('term') == '(all targets)'), None)
        c0, s0 = f(cur), f(sug)
        if bc and bc.get('bid_to') is not None and a.get('tos_to') == 900:
            fin_txt = f"base ${bc['bid_to']} with TOS 900% → top-of-search price ${bc.get('eff_tos_to')}"
            ev['verdict'] = 'REJECT' if (s0 is not None and c0 is not None and s0 < c0) else 'MODIFY'
            ev['analysis'].append('Replaced by the top-of-search-only structure: the price at the top of search is held at today\'s clearing CPC; rest of search/product pages drop to the base')
        elif bc and bc.get('change'):
            fin_txt = f"all targets {bc['change']} (one step)"
            ev['verdict'] = 'MODIFY' if (s0 is not None and c0 is not None and s0 < c0 and abs(s0 / c0 - 0.85) > 0.03) else 'ACCEPT'
        else:
            fin_txt = 'bid unchanged'
            ev['verdict'] = 'REJECT' if (s0 is not None and c0 is not None and s0 != c0) else 'ACCEPT'
    elif k == 'build':
        ev['verdict'], fin_txt = 'REJECT', 'not built'
    elif k == 'negatives':
        ev['verdict'], fin_txt = ev['verdict'], 'negatives from the Keywords tab (zero-order terms, itemised)'
    ev['final_action'] = fin_txt
    ev['final_why'] = ' | '.join(d['why'])
json.dump(rows, open(L.OUT + 'audit_review.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    print(len(rows), sorted(collections.Counter((r['kind'], r['verdict']) for r in rows).items()))
