"""Judge every bid / placement / budget / state row of run 20260921-dbcd48b8 against
'Bids and placements on Exact campaigns'. Produces analysis.json (one record per campaign)."""
import json, re, os
from collections import defaultdict

S = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(f'{S}/a.json'))
ROWS = json.load(open(f'{S}/rows.json'))
SKU = json.load(open(f'{S}/skus.json'))
BE = A['brief']['sections']['margin']['be_acos']            # 0.3387
C_UNIT = A['brief']['sections']['margin']['contribution_per_unit']  # 25.06
DEAL = ('2026-09-15', '2026-09-28')
FLOOR, FULL = 15, 50
MKT_REF = None


def load_pl(label):
    p = f'{S}/placements_{label}.jsonl'
    out = {}
    if not os.path.exists(p):
        return out
    for line in open(p):
        r = json.loads(line)
        out[r['campaignId']] = r
    return out


P90, PRE, DEAL6 = load_pl('d90'), load_pl('pre_deal30'), load_pl('deal6')
DEAL8 = load_pl('deal8')
DEAL_SRC, DEAL_DAYS = (DEAL8, 8) if DEAL8 else (DEAL6, 6)


def plc(r, key):
    """clicks, orders, spend, impressions at one placement of a campaign row"""
    if not r:
        return dict(c=0, o=0, s=0.0, i=0)
    p = (r.get('placements') or {}).get(key) or {}
    c = p.get('clicks') or 0
    o = p.get('orders') or 0
    s = (p.get('cpc') or 0) * c
    return dict(c=c, o=o, s=s, i=p.get('impressions') or 0)


def exdeal(cid):
    """The priced window: the audit's own 90 days, 2026-06-23..2026-09-20, deal days INCLUDED
    (operator 2026-09-23: the Best Deal is the rank lever, its TOS clicks count)."""
    return {k: plc(P90.get(cid), k) for k in ('tos', 'detail', 'other', 'off')}


def window(cid, src):
    return {k: plc(src.get(cid), k) for k in ('tos', 'detail', 'other', 'off')}


# ---------- campaign registry ----------
CAMPS = {c['campaign_id']: c for c in A['campaigns']}
DEC = defaultdict(list)
for r in ROWS:
    DEC[r['cid']].append(r)
STOCK = {s['size']: s for s in A['context']['inventory']}
FREEZE = {c['campaignId']: c for c in A['context']['rank_freeze']['campaigns']}
TL = {t['keyword']: t for t in A['context']['rank_timelines']}
TGT = {t['keyword']: t for t in A['brief']['sections']['targets']['keywords']}


def size_of(child):
    if not child:
        return None
    for s, k in (('California King', 'CALIFKING'), ('King', '-KING-'), ('Queen', 'QUEEN'), ('Full', 'FULL'), ('Twin', 'TWIN')):
        if k in child:
            return s
    return None


def child_contrib(child):
    """Per-order contribution on the engine's own basis (list price x break-even ACoS),
    with the fee-model figure alongside. Flag when the price is missing."""
    v = SKU.get(child)
    if not v or v[0] is None:
        size = size_of(child)
        prices = [x[0] for k, x in SKU.items() if size_of(k) == size and x[0]]
        p = sum(prices) / len(prices) if prices else None
        return dict(price=p, be_basis=p * BE if p else C_UNIT, fee_model=None, flag='price/fees missing in Command Center; size-average price used')
    return dict(price=v[0], be_basis=v[0] * BE, fee_model=v[1], flag=None)


# child planning rates by placement, 90 days incl. deal, across every SP campaign advertising the child
CHILD_RATE = defaultdict(lambda: defaultdict(lambda: [0, 0]))
for cid, c in CAMPS.items():
    ch = c.get('child')
    if not ch or cid not in P90:
        continue
    x = exdeal(cid)
    for k in ('tos', 'detail', 'other'):
        CHILD_RATE[ch][k][0] += x[k]['c']
        CHILD_RATE[ch][k][1] += x[k]['o']
LANE = defaultdict(lambda: [0, 0])
for ch, v in CHILD_RATE.items():
    for k in v:
        LANE[k][0] += v[k][0]; LANE[k][1] += v[k][1]


def child_rate(ch, k):
    c, o = CHILD_RATE[ch][k] if ch in CHILD_RATE else (0, 0)
    if c >= 100 and o > 0:
        return o / c, f'child {ch} {o}/{c}'
    lc, lo = LANE[k]
    return lo / lc, f'lane {lo}/{lc} (child under 100 clicks)'


def blend(clicks, orders, ch, k):
    """doc §3: under 15 -> child's rate; 15+ with orders -> blend weighted (clicks-15)/35; 15+ no orders -> child's."""
    base, src = child_rate(ch, k)
    if clicks < FLOOR:
        return base, f'child planning rate {base:.1%} ({src}); campaign has {clicks} clicks, under the 15-click floor'
    if orders == 0:
        return base, f'child planning rate {base:.1%} ({src}); {clicks} clicks, no orders — absence of evidence'
    own = orders / clicks
    w = min(1.0, (clicks - FLOOR) / 35)
    r = base + (own - base) * w
    return r, f'blend: child {base:.1%} + (own {own:.1%} − child) × weight {w:.2f} [{clicks} clicks, {orders} orders] = {r:.1%}'


def gap_lift(ratio):
    if ratio is None:
        return 0.0
    if ratio <= 1.0:
        return 0.0
    if ratio <= 1.5:
        return 0.25
    return (ratio - 1) * 0.5


def money(x):
    return None if x is None else round(x, 2)


def analyse(cid):
    c = CAMPS.get(cid)
    rows = [r for r in DEC.get(cid, [])]
    changes = [r for r in rows if r['verdict'] == 'change']
    name = c['campaign'] if c else (changes[0]['camp'] if changes else cid)
    obj = (c or {}).get('objective') or (changes[0]['obj'] if changes else None)
    child = (c or {}).get('child')
    ca = (c or {}).get('child_after') or 'hold'
    serving = ca.replace('→ ', '') if ca and ca.startswith('→') else child
    econ = child_contrib(serving) if serving else dict(price=None, be_basis=C_UNIT, fee_model=None, flag='no advertised child')
    # engine's own per-order contribution where it stated one
    eng_contrib = next((r['contrib'] for r in rows if r.get('contrib')), None)
    contrib = eng_contrib or econ['be_basis']

    X = exdeal(cid)
    W90 = window(cid, P90)
    WP = window(cid, PRE)
    WD = window(cid, DEAL_SRC)
    tos, pp, ros = X['tos'], X['detail'], X['other']
    tot = tos['c'] + pp['c'] + ros['c']
    share = {k: (X[k]['c'] / tot if tot else None) for k in ('tos', 'detail', 'other')}
    rate = {}
    why_rate = {}
    for k in ('tos', 'detail', 'other'):
        rate[k], why_rate[k] = blend(X[k]['c'], X[k]['o'], serving, k)
    ceil = {k: contrib * rate[k] for k in rate}
    cpc = {k: (X[k]['s'] / X[k]['c'] if X[k]['c'] else None) for k in X}
    cvr_own = {k: (X[k]['o'] / X[k]['c'] if X[k]['c'] else None) for k in X}

    # targets
    tg = [t for t in (c or {}).get('targets', [])]
    en = [t for t in tg if t['state'] in ('ENABLED', None)]
    head = max(en, key=lambda t: (t['clicks'] or 0, t['bid'] or 0)) if en else None
    tos_mod = (c or {}).get('tos') or 0
    def row_to(kind):
        r = next((r for r in changes if r['kind'] == kind), None)
        try:
            return float(r['to']) if r else None
        except (TypeError, ValueError):
            return None
    tos_to = row_to('tos') if row_to('tos') is not None else (c or {}).get('tos_to')
    pp_mod, ros_mod = (c or {}).get('pp') or 0, (c or {}).get('ros') or 0
    base = head['bid'] if head else None
    base_to = head.get('bid_to') if head else None
    price_now = base * (1 + tos_mod / 100) if base else None
    price_eng = (base_to or base) * (1 + (tos_to if tos_to is not None else tos_mod) / 100) if base else None

    # rank / plan
    kw = (c or {}).get('plan_keyword')
    tl = TL.get(kw) if kw else None
    tgt = TGT.get(kw) if kw else None
    rr = next((r for r in rows if r.get('rank_now')), None)
    rank_now = (tl or {}).get('rank_now') or (rr or {}).get('rank_now') or (tgt or {}).get('rank_now')
    rank_tgt = (tl or {}).get('plan_target') or (rr or {}).get('rank_tgt') or (tgt or {}).get('rank_target')
    rank_30 = (tl or {}).get('rank_30d_ago') or (tgt or {}).get('rank_30d_ago')
    plan_wk = next((r['plan_ppc_wk'] for r in rows if r.get('plan_ppc_wk')), None) or next((float(m) for r in rows for m in re.findall(r'against a declared ([\d.]+)/wk', r['text'])), None) or (tl or {}).get('plan_clicks_wk') or None
    tos_is = next((r['tos_is'] for r in rows if r.get('tos_is') is not None), None)
    if tos_is is None:
        tos_is = next((float(m) for r in rows for m in re.findall(r'wins ([\d.]+)% of the top-of-search impressions', r['text'])), None)
    mkt_cvr = next((r['mkt_cvr'] for r in rows if r.get('mkt_cvr') is not None), None)
    mkt_ctr = next((r['mkt_ctr'] for r in rows if r.get('mkt_ctr') is not None), None)
    tos_ctr = (tos['c'] / tos['i']) if tos['i'] else None
    focus = (c or {}).get('focus') or ''
    in_focus = focus.startswith('IN')
    budget = (c or {}).get('budget')
    spend_day = ((c or {}).get('spend_14d') or 0) / 14
    days = 90
    tos_wk = tos['c'] / days * 7
    size = size_of(serving)
    st = STOCK.get(size) if size else None
    frozen = cid in FREEZE

    return dict(deal_days=DEAL_DAYS, cid=cid, name=name, obj=obj, child=child, child_after=ca, serving=serving, size=size,
                econ=econ, eng_contrib=eng_contrib, contrib=contrib, X=X, W90=W90, WP=WP, WD=WD, share=share, rate=rate,
                why_rate=why_rate, ceil=ceil, cpc=cpc, cvr_own=cvr_own, targets=tg, head=head, tos_mod=tos_mod,
                tos_to=tos_to, pp_mod=pp_mod, ros_mod=ros_mod, pp_to=row_to('pp'), ros_to=row_to('ros'),
                base=base, base_to=base_to, price_now=price_now, price_eng=price_eng, kw=kw, rank_now=rank_now,
                rank_tgt=rank_tgt, rank_30=rank_30, plan_wk=plan_wk, tos_is=tos_is, mkt_cvr=mkt_cvr, mkt_ctr=mkt_ctr,
                tos_ctr=tos_ctr, focus=focus, in_focus=in_focus, budget=budget, budget_to=row_to('budget') or (c or {}).get('budget_to'),
                spend_day=spend_day, tos_wk=tos_wk, stock=st, frozen=frozen, bid_strategy=(c or {}).get('bid_strategy'),
                status=(c or {}).get('status'), clicks_90d=(c or {}).get('clicks_90d'), orders_90d=(c or {}).get('orders_90d'),
                rows=rows, changes=changes, tot=tot)


# ======================= judgement against the document =======================
def pct(x):
    return '—' if x is None else f'{x:.0%}'


def usd(x):
    return '—' if x is None else f'${x:,.2f}'


def judge(a):
    F = []          # findings: dict(code, title, what, rationale, issue, fix)
    corr = {}       # corrected values
    X, sh, ceil = a['X'], a['share'], a['ceil']
    tos, pp, ros = X['tos'], X['detail'], X['other']
    ranking = (a['obj'] == 'Ranking')
    exact = ('Exact' in a['name'])
    tot = a['tot']
    base, pnow = a['base'], a['price_now']
    pp_orders = pp['o'] + ros['o']

    # ---- situation (doc §12) ----
    if a['frozen']:
        sit = 'Rank collapsing >10 positions — never scale; investigate listing, rival, category first (§12)'
    elif tot < FLOOR:
        sit = 'Campaign on, (almost) no clicks arriving — nothing to redistribute: hold the base, move the modifier only (§12)'
    elif sh['tos'] is not None and sh['tos'] < 0.30 and ranking and not (sum(a['WD'][k]['c'] for k in ('tos', 'detail', 'other')) >= FLOOR and a['WD']['tos']['c'] / sum(a['WD'][k]['c'] for k in ('tos', 'detail', 'other')) >= 0.70):
        sit = 'Top of search under 30% on a ranking campaign — distribution fix takes precedence: no price climb, no budget move (§12)'
    elif sh['detail'] is not None and sh['detail'] > 0.20:
        sit = 'Product pages over 20% — money leaking to the placement that does not move rank: distribution fix (§12)'
    elif sh['tos'] is not None and sh['tos'] >= 0.70:
        sit = 'Mix right (TOS ≥70%, PP ≤20%) — delivery is a price/budget/demand question, not a mix one (§12)'
    else:
        sit = 'PP ≤20% but TOS under 70% — rest of search is carrying the difference; ROS modifier and base are the levers (§12)'

    # ---- push case (§6 four conditions, §11 five properties) ----
    st = a['stock'] or {}
    hero_bad = False
    if st:
        hero = st.get('hero')
        hero_bad = (a['serving'] == hero and st.get('hero_room') in ('NO_ROOM', 'UNDER_HORIZON')) or (a['serving'] == hero and 'UNDER_HORIZON' in (st.get('why') or '') ) or (a['serving'] == hero and 'NO_ROOM' in (st.get('why') or ''))
    rank_on_file = a['rank_now'] is not None
    ctr_ok = None if (a['tos_ctr'] is None or a['mkt_ctr'] is None) else (a['tos_ctr'] * 100 >= a['mkt_ctr'])
    cvr_ok = None if (a['rate']['tos'] is None or a['mkt_cvr'] is None) else (a['rate']['tos'] * 100 >= a['mkt_cvr'])
    req_day = a['plan_wk'] / 7 if a['plan_wk'] else None
    need_budget = req_day * pnow if (req_day and pnow) else None
    funded = None if (need_budget is None or a['budget'] is None) else (a['budget'] >= need_budget)
    push_case = ranking and exact and a['in_focus'] and rank_on_file and not a['frozen'] and not hero_bad
    conditions = dict(velocity='met — Best Deal live to 2026-09-28 (the engine did not read it)',
                      ctr=ctr_ok, cvr=cvr_ok, stock=not hero_bad)

    # ---- the price at top of search ----
    tceil = ceil['tos']
    rank_gap = (a['rank_now'] / a['rank_tgt']) if (a['rank_now'] and a['rank_tgt']) else None
    deliv_gap = (req_day / (a['tos_wk'] / 7)) if (req_day and a['tos_wk']) else None
    lift = max(gap_lift(rank_gap), 0 if (a['tos_is'] is not None and a['tos_is'] >= 50) else gap_lift(deliv_gap) if rank_on_file else 0)
    mkt_bound = next((r['mkt_bound'] for r in a['rows'] if r.get('mkt_bound')), None)
    unit_bound = a['contrib']
    target = None
    bound_name = None
    if tceil:
        target = tceil * (1 + lift) if push_case else tceil
        bound_name = 'ceiling' if not push_case or lift == 0 else f'ceiling × (1 + {lift:.2f} lift)'
        if mkt_bound and target > mkt_bound:
            target, bound_name = mkt_bound, "market bound (engine's own TOS CPC +15%)"
        if target > unit_bound:
            target, bound_name = unit_bound, 'per-unit bound (no click may cost more than the unit earns)'

    write_price = pnow
    write_kind = []
    below70 = (a['tos_wk'] / 7) < 0.7 * req_day if req_day else True
    _wd = a['WD']; _dt = sum(_wd[k]['c'] for k in ('tos', 'detail', 'other'))
    deal_tos_ok = _dt >= FLOOR and _wd['tos']['c'] / _dt >= 0.70
    mix_first = (sh['tos'] is not None and sh['tos'] < 0.30 and ranking and tot >= FLOOR and not deal_tos_ok)
    if pnow and target:
        if a['frozen']:
            write_price = pnow; write_kind.append('hold (rank collapse)')
        elif push_case and funded and ctr_ok and cvr_ok:
            if pnow < target and not mix_first and not (a['tos_is'] is not None and a['tos_is'] >= 50):
                write_price = min(target, pnow * 1.30); write_kind.append('funding step (≤ +30%)')
            elif pnow > target and not below70:
                write_price = max(target, pnow * 0.95); write_kind.append('price probe (−3–5%)')
            else:
                write_kind.append('price held')
        elif push_case:
            missing = [n for n, v in (('funded', funded), ('CTR above market', ctr_ok), ('CVR above market', cvr_ok)) if not v]
            if pnow > tceil * 1.02:
                write_kind.append('price held above the ceiling — the premium is not a proven push (' + ', '.join(missing) + ' not shown); operator decision owed: prove/fund it or descend to the ceiling')
            elif pnow < tceil * 0.98 and not mix_first:
                write_price = min(tceil, pnow * 1.30); write_kind.append('climb toward the ceiling only (≤ +30%) — no premium until ' + ', '.join(missing) + ' shown')
            else:
                write_kind.append('price held')
        elif not ranking:
            if pnow > tceil * 1.02:
                write_price = tceil; write_kind.append('descent to a named point: the TOS ceiling (non-ranking objective — bounded at every placement)')
            else:
                write_kind.append('price held — inside its ceiling; the objective is governed outside this document')
        else:
            if pnow > tceil * 1.02:
                write_price = tceil; write_kind.append('descent to a named point: the TOS ceiling')
            elif pnow < tceil * 0.98 and not mix_first and a['in_focus']:
                write_price = min(tceil, pnow * 1.30); write_kind.append('maintenance climb toward ceiling (≤ +30%)')
            elif pnow < tceil * 0.98:
                write_kind.append('price held under its ceiling (out of focus: the operator\'s taper releases this spend; the document would allow up to the ceiling)')
            else:
                write_kind.append('price held at ceiling')

    # ---- the base ----
    WD = a['WD']
    deal_tot = sum(WD[k]['c'] for k in ('tos', 'detail', 'other'))
    deal_pp = WD['detail']['c'] / deal_tot if deal_tot else None
    deal_ok_mix = ranking and deal_tot >= FLOOR and deal_pp is not None and deal_pp <= 0.20 and (sh['detail'] or 0) > 0.20
    base_new = base
    base_why = None
    if base:
        cap = 0.25 if pp_orders > 0 else 0.50
        if a['frozen']:
            base_why = 'held — rank collapse freeze'
        elif tot < FLOOR:
            base_why = 'held — no clicks arriving; cutting the base of a row that is not delivering makes delivery worse (§12)'
        elif not ranking:
            c_all = sum(X[k]['c'] for k in ('tos', 'detail', 'other'))
            o_all = sum(X[k]['o'] for k in ('tos', 'detail', 'other'))
            ch_c = sum(CHILD_RATE[a['serving']][k][0] for k in ('tos', 'detail', 'other')) if a['serving'] in CHILD_RATE else 0
            ch_o = sum(CHILD_RATE[a['serving']][k][1] for k in ('tos', 'detail', 'other')) if a['serving'] in CHILD_RATE else 0
            ch_r = ch_o / ch_c if ch_c else 0.12
            if c_all < FLOOR or o_all == 0:
                r_all = ch_r
            else:
                w = min(1.0, (c_all - FLOOR) / 35)
                r_all = ch_r + (o_all / c_all - ch_r) * w
            c_ceiling = a['contrib'] * r_all
            corr['click_ceiling'] = c_ceiling
            if base > c_ceiling * 1.02:
                base_new = max(c_ceiling, base * (1 - cap))
                base_why = f"non-ranking objective: base {usd(base)} above what a click affords on the campaign's blended rate ({pct(r_all)} × {usd(a['contrib'])} = {usd(c_ceiling)}; {c_all} clicks / {o_all} orders 90 days, child {pct(ch_r)}) → toward it, cap {int(cap*100)}%"
            else:
                base_why = f"non-ranking objective: base inside what a click affords ({pct(r_all)} × {usd(a['contrib'])} = {usd(c_ceiling)}) — held"
        elif deal_ok_mix:
            base_why = f"PP {pct(sh['detail'])} over 90 days, but {pct(deal_pp)} on the {deal_tot} deal-day clicks — the mix is already right in the deal; base held for the remaining deal days, re-test on post-deal days (10-06)"
        elif sh['detail'] is not None and sh['detail'] > 0.20:
            tgt_b = ceil['detail']
            if base > tgt_b:
                base_new = max(tgt_b, base * (1 - cap))
            else:
                step = 0.10 if sh['detail'] < 0.25 else 0.20 if sh['detail'] < 0.35 else cap
                base_new = base * (1 - min(step, cap))
            base_why = f"PP {pct(sh['detail'])} > 20% → cut toward what product pages afford ({usd(ceil['detail'])}); cap {int(cap*100)}% ({'real sales on PP/ROS: ' + str(pp_orders) + ' orders' if pp_orders else 'no PP/ROS orders'})"
        else:
            base_why = f"PP {pct(sh['detail'])} ≤ 20% — the base is doing its job; no reason to touch it (§10)"
        if write_price and base_new and write_price < base_new and not a['frozen']:
            nb = max(write_price, base * (1 - cap))
            if nb < base_new:
                base_new = nb
                base_why = (base_why or '') + f'; the TOS price is landing at {usd(write_price)}, under the base — the base comes down with it (descent, cap {int(cap*100)}%)'
        floor_b = max(0.50, (write_price or 0) / 10)
        if base_new < floor_b:
            base_new = floor_b
            base_why += f'; floored at {usd(floor_b)}'
    mod_new = None
    if base_new and write_price:
        mod_new = write_price / base_new - 1
        if mod_new > 9.0:
            base_new = write_price / 10
            mod_new = 9.0
            base_why = (base_why or '') + '; modifier would pass the 900% wall — base lifted as a stated trade (§10)'
        mod_new = max(0.0, mod_new)
    corr.update(base=money(base_new), price=money(write_price), mod=None if mod_new is None else round(mod_new * 100),
                write_kind=write_kind, base_why=base_why, target=money(target), bound_name=bound_name, lift=lift,
                rank_gap=rank_gap, deliv_gap=deliv_gap)
    # ROS / PP modifier
    ros_earned = ros['c'] >= FLOOR and pp['c'] > 0 and (ros['o'] / ros['c']) >= (a['rate']['detail'] or 0)
    corr['ros'] = a['ros_mod'] if (a['ros_mod'] == 0 or ros_earned) else 0
    corr['pp'] = 0
    # budget
    budget_new = a['budget']
    budget_why = None
    pre_spend = sum(a['WP'][k]['s'] for k in a['WP']) / 31 if a['WP'] else None
    corr['deal_spend'] = sum(a['WD'][k]['s'] for k in a['WD']) / DEAL_DAYS
    if deal_ok_mix:
        sit += f" — but on deal days PP is {pct(deal_pp)} of {deal_tot} clicks: the deal has fixed the mix for now"
    if a['budget'] is not None:
        if push_case and funded is False and need_budget:
            budget_why = f"push needs {usd(need_budget)}/day ({req_day:.1f} clicks/day × {usd(pnow)}); budget {usd(a['budget'])} → shortfall {usd(need_budget - a['budget'])}/day — a decision to take, not a rung"
        elif mix_first:
            budget_why = 'no budget move while the mix is below 30% TOS (§12)'
        else:
            dsp = sum(a['WD'][k]['s'] for k in a['WD']) / DEAL_DAYS
            corr['deal_spend'] = dsp
            if dsp >= 0.95 * a['budget'] and a['in_focus']:
                budget_why = f"deal days average {usd(dsp)}/day against {usd(a['budget'])} — capping in the deal: raise for the remaining deal days (a funding decision above $50/day)"
            else:
                budget_why = f"held — deal days average {usd(dsp)}/day against {usd(a['budget'])} ({dsp / a['budget']:.0%}); the campaign is not running out of money" if a['budget'] else 'no budget'
    corr.update(deal_ok_mix=deal_ok_mix, deal_pp=deal_pp, deal_tot=deal_tot, premium_ok=bool(push_case and funded and ctr_ok and cvr_ok), budget=budget_new, budget_why=budget_why, pre_spend=pre_spend, need_budget=need_budget, req_day=req_day,
                funded=funded, push_case=push_case, conditions=conditions, hero_bad=hero_bad, situation=sit,
                below70=below70, mix_first=mix_first)
    return corr
