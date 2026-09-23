"""Read what is happening on every campaign and put it in one situation, with the correction
that situation calls for. Output: cats.json (one record per campaign)."""
import json, re, os
from collections import defaultdict

S = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(f'{S}/a.json'))
AN = {a['cid']: a for a in json.load(open(f'{S}/analysis.json'))}
HIST = [json.loads(l) for l in open(f'{S}/data/decisions_hist.jsonl')]
BE = A['brief']['sections']['margin']['be_acos']


def load(label):
    p = f'{S}/data/placements_{label}.jsonl'
    return {json.loads(l)['campaignId']: json.loads(l) for l in open(p)} if os.path.exists(p) else {}


def pct(x):
    return '—' if x is None else f'{x*100:.0f}%'


W = {k: load(k) for k in ('d90', 'pre_deal30', 'deal8', 'd14', 'd7', 'd3', 'pre0910', 'post0910')}
DAYS = {'d90': 90, 'pre_deal30': 31, 'deal8': 8, 'd14': 14, 'd7': 7, 'd3': 3, 'pre0910': 3, 'post0910': 4}

# the engine's own per-group market price (its text: "<group> clears at $X ... the bound is $Y")
GROUP_LIMIT = {'LANE': (5.38, 6.19), 'Bamboo|Twin': (5.27, 6.06), 'Cooling|King': (4.50, 5.18), 'Bamboo|Full': (6.28, 7.22),
               'Bamboo|King': (5.62, 6.47), 'Bamboo|Cooling': (4.93, 5.68), 'Bamboo|Queen': (5.55, 6.39), 'Bamboo': (5.50, 6.32),
               'Cooling': (3.14, 3.61)}
HARD_STOP_X = 3.0      # top-of-search ad cost per order may not exceed 3 x contribution (operator 2026-09-23)
SHARE_STOP = 40.0      # impression share at/above this and not rising after the last step -> stop stepping


def _median(xs):
    xs = sorted(xs); n = len(xs)
    return None if not n else (xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2)


# one rank source: the tracker, 7-day median (a single day swings 16 -> 44 on the head term)
TRACK = {}
_tk = f'{S}/data/b46/b4_ranks_keywords.json'
if os.path.exists(_tk):
    for r in json.load(open(_tk)).get('rows', []):
        TRACK[r['keyword']] = {c['date']: c.get('rank') for c in r.get('cells', []) if c.get('state') == 'ranked' and c.get('rank')}


def rank7(kw, end):
    from datetime import date, timedelta
    ser = TRACK.get(kw)
    if not ser:
        return None
    d0 = date.fromisoformat(end)
    v = [ser[(d0 - timedelta(days=i)).isoformat()] for i in range(7) if (d0 - timedelta(days=i)).isoformat() in ser]
    return round(_median(v)) if v else None


def target_is(cid, kw, win):
    p = f'{S}/data/b46/b4_targets_{win}_{cid}.json'
    if not os.path.exists(p):
        return None
    rows = [r for r in (json.load(open(p)).get('rows') or []) if 'Exact' in (r.get('targetType') or '')]
    r = next((r for r in rows if r.get('target') == kw), None) or (max(rows, key=lambda r: r.get('spend') or 0) if rows else None)
    return None if r is None else r.get('tosImpressionShare')


TIER_RANK = {'VHSV': 5, 'HSV': 4, 'MSV': 3, 'LSV': 2, 'VLSV': 1, 'NOSV': 0}


def read(cid, label):
    r = W[label].get(cid)
    out = {'days': DAYS[label]}
    for k in ('tos', 'detail', 'other', 'off'):
        p = ((r or {}).get('placements') or {}).get(k) or {}
        c = p.get('clicks') or 0
        out[k] = dict(c=c, o=p.get('orders') or 0, s=(p.get('cpc') or 0) * c, i=p.get('impressions') or 0)
    out['clicks'] = (r or {}).get('clicks') or 0
    out['orders'] = (r or {}).get('orders') or 0
    out['spend'] = (r or {}).get('spend') or 0
    out['sales'] = (r or {}).get('sales') or 0
    t = sum(out[k]['c'] for k in ('tos', 'detail', 'other'))
    out['t3'] = t
    out['tos_sh'] = out['tos']['c'] / t if t else None
    out['pp_sh'] = out['detail']['c'] / t if t else None
    return out


def tier(n):
    m = re.search(r'\((VHSV|HSV|MSV|LSV|VLSV|NOSV)\)', n)
    return m.group(1) if m else None


def group(c):
    m = re.search(r'\[([A-Za-z|]+)\]', c['campaign'])
    if m:
        return m.group(1)
    if c.get('syntax') and c['syntax'] != 'OUT':
        return c['syntax']
    n = c['campaign'].lower()
    if 'cool' in n:
        return 'Cooling|King' if 'king' in n else 'Cooling'
    if 'queen' in n:
        return 'Bamboo|Queen'
    if 'king' in n:
        return 'Bamboo|King'
    if 'full' in n:
        return 'Bamboo|Full'
    if 'twin' in n:
        return 'Bamboo|Twin'
    return 'Bamboo'


# last change per campaign (price / budget / state), from the decision record
LAST = defaultdict(list)
for h in HIST:
    if h['move_id'] and h['field'] in ('bid', 'placement_multiplier', 'budget', 'state') and h['deployState'] in ('api_confirmed', 'recorded'):
        LAST[h['campaignId']].append(h)

DEC = defaultdict(list)
for x in A['decisions']:
    if x['kind'] in ('tos', 'bid', 'budget', 'pp', 'ros', 'state'):
        DEC[x['campaign_id']].append(x)
FREEZE = {c['campaignId']: c for c in A['context']['rank_freeze']['campaigns']}
TUNER = {c['campaign_id']: c for c in A['brief']['sections']['tuner']['campaigns_behind_or_wrong']}


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def engine_moves(cid, an):
    """What the engine did to the TOS price, the base and the budget on this campaign."""
    xs = DEC.get(cid, [])
    out = dict(rows=[x['seq'] for x in xs], tos=None, base=None, budget=None, withheld=False)
    for x in xs:
        a, b = fnum(x['current_at_audit']), fnum(x['suggested'])
        txt = ' '.join(r['text'] for r in x['rationale'])
        if 'change → HOLD' in txt:
            out['withheld'] = True
        if a is None or b is None or a == b:
            continue
        d = 'up' if b > a else 'down'
        if x['kind'] == 'tos':
            out['tos'] = (d, a, b, x['seq'])
        elif x['kind'] == 'bid' and out['base'] is None:
            out['base'] = (d, a, b, x['seq'])
        elif x['kind'] == 'budget':
            out['budget'] = (d, a, b, x['seq'])
    pn, pe = an.get('price_now') if an else None, an.get('price_eng') if an else None
    out['price_now'], out['price_eng'] = pn, pe
    out['price_dir'] = None if not (pn and pe) else ('up' if pe > pn * 1.01 else 'down' if pe < pn * 0.99 else 'flat')
    return out


def classify(c):
    cid = c['campaign_id']
    an = AN.get(cid, {})
    R = {k: read(cid, k) for k in W}
    n90, d14, d7, d3, dl, pre = R['d90'], R['d14'], R['d7'], R['d3'], R['deal8'], R['pre_deal30']
    tos90 = n90['tos']['c']
    focus_in = (c.get('focus') or '').startswith('IN')
    tr = tier(c['campaign'])
    grp = group(c)
    lim = GROUP_LIMIT.get(grp, GROUP_LIMIT['LANE'])
    em = engine_moves(cid, an)
    budget = c.get('budget') or 0
    util7 = (d7['spend'] / 7 / budget) if budget else None
    util14 = (d14['spend'] / 14 / budget) if budget else None
    rank_now, rank_30, rank_tgt = an.get('rank_now'), an.get('rank_30'), an.get('rank_tgt')
    rank_src = 'engine'
    if an.get('kw') in TRACK:
        rank_now, rank_30, rank_src = rank7(an['kw'], '2026-09-22') or rank_now, rank7(an['kw'], '2026-08-23') or rank_30, 'tracker, 7-day median'
    plan_wk = an.get('plan_wk')
    tos_is = an.get('tos_is')
    contrib = an.get('contrib') or 25.06
    tos_rate = (an.get('rate') or {}).get('tos')
    ceil_tos = (an.get('ceil') or {}).get('tos')
    mkt_cvr, mkt_ctr = an.get('mkt_cvr'), an.get('mkt_ctr')
    st = an.get('stock') or {}
    hero_bad = bool(st) and an.get('serving') == st.get('hero') and st.get('hero_room') in ('NO_ROOM', 'UNDER_HORIZON') and (c.get('child_after') or 'hold') == 'hold'
    # which window reads the mix: 14 days if it has 15+ clicks, else the deal, else 90 days
    mixw = 'd14' if d14['t3'] >= 15 else ('deal8' if dl['t3'] >= 15 else 'd90')
    mix = R[mixw]
    deal_tos_day = dl['tos']['c'] / 8
    pre_tos_day = pre['tos']['c'] / 31
    need_day = plan_wk / 7 if plan_wk else None
    last = sorted(LAST.get(cid, []), key=lambda h: h['decided'])
    last_date = last[-1]['decided'] if last else None
    stale = [h for h in last if h['decided'] >= '2026-09-21']

    cat, why = None, ''
    if cid in FREEZE:
        rank_now, rank_30 = FREEZE[cid]['now'], FREEZE[cid]['ago30']
    lost = (rank_now - rank_30) if (rank_now and rank_30) else None
    if cid in FREEZE or (lost is not None and lost > 10 and c['objective'] == 'Ranking'):
        cat = 'COLLAPSE'
    elif n90['t3'] >= 45 and d7['t3'] == 0 and dl['t3'] <= 2:
        cat = 'DARK'
    elif n90['t3'] >= 90 and (d14['t3'] / 14) < 0.25 * (n90['t3'] / 90):
        cat = 'FADED'
    elif d14['t3'] < 15 and dl['t3'] < 15:
        if n90['t3'] == 0 and dl['t3'] == 0:
            cat = ('THIN_ZERO_IN' if TIER_RANK.get(tr, 0) >= 2 else 'THIN_TINY') if focus_in else 'THIN_ZERO_OUT'
        elif focus_in and TIER_RANK.get(tr, 0) >= 2:
            cat = 'THIN_PUSH'
        elif focus_in:
            cat = 'THIN_TINY'
        else:
            cat = 'THIN_OUT'
    elif mix['pp_sh'] is not None and mix['pp_sh'] > 0.20:
        cat = 'LEAK'
    elif mix['tos_sh'] is not None and mix['tos_sh'] >= 0.70:
        short = need_day is not None and deal_tos_day < 0.7 * need_day
        if not focus_in:
            perf = (tos_rate is not None and mkt_cvr is not None and tos_rate * 100 >= mkt_cvr) or (lost is not None and lost < 0)
            cat = 'OUT_WORKING' if perf else 'OUT_WEAK'
        elif short or need_day is None:
            if util7 is not None and util7 >= 0.80:
                cat = 'SHORT_BUDGET'
            elif em['price_now'] and em['price_now'] >= lim[1]:
                cat = 'SHORT_ATLIMIT'
            else:
                cat = 'SHORT_PRICE'
        else:
            cat = 'ON_TARGET'
    else:
        cat = 'ROS_HEAVY'

    # ---- in focus: every campaign is pushed on top of search during the deal (operator 2026-09-23) ----
    push = None
    tg = c.get('targets') or []
    all_paused = bool(tg) and not any(t['state'] in ('ENABLED', None) for t in tg)
    if focus_in and all_paused:
        cat = 'IN_PAUSED'
    elif focus_in:
        if cat == 'COLLAPSE':
            cat = 'IN_COLLAPSE'
        elif cat in ('DARK', 'FADED'):
            cat = 'IN_DARK'
        elif cat == 'ON_TARGET' and need_day and deal_tos_day >= need_day:
            cat = 'IN_ONTARGET'
        elif (cat == 'LEAK' and mixw != 'd90') or (mixw != 'd90' and mix['tos_sh'] is not None and mix['tos_sh'] < 0.30):
            cat = 'IN_LEAK'
        else:
            cat = 'IN_PUSH'
        if cat != 'IN_ONTARGET':
            # step sized by the delivery gap (operator 2026-09-23), halved where share did not answer the last raise
            is30, isd = target_is(cid, an.get('kw'), '30d'), target_is(cid, an.get('kw'), 'deal')
            is_now = isd if isd is not None else is30
            raised_0915 = any(h['decided'] >= '2026-09-15' and h['field'] == 'placement_multiplier' and h.get('placement') == 'placementTop' and fnum(h['after']) and fnum(h['before']) is not None and fnum(h['after']) > fnum(h['before']) for h in last)
            share_flat = (is30 is not None and isd is not None and isd <= is30)
            reach_day = (deal_tos_day / (is_now / 100)) if (is_now and deal_tos_day) else None
            need_eff = min(need_day, reach_day) if (need_day and reach_day) else need_day
            unreachable = bool(need_day and reach_day and reach_day < need_day)
            deliv = (deal_tos_day / need_eff) if need_eff else None
            if deliv is not None:
                step = 0.30 if deliv < 0.30 else 0.20 if deliv < 0.70 else 0.10
                step_why = f"{deliv:.0%} of required top-of-search clicks delivered → +{step:.0%}"
            else:
                step, step_why = 0.20, 'no click requirement on file → +20% (a stated departure: the logic document would hold at the ceiling)'
            at_req = deliv is not None and deliv >= 1
            if at_req:
                step, step_why = 0.0, f"{deliv:.0%} of required top-of-search clicks delivered — at requirement, no step; evaluate cost per click after the deal"
            if raised_0915 and share_flat and not at_req:
                step /= 2; step_why += f"; halved — impression share did not rise after the 15 Sep raise ({is30:.1f}% → {isd:.1f}%)"
            share_stop = bool(is_now is not None and is_now >= SHARE_STOP and (share_flat or not raised_0915))
            if share_stop:
                step, step_why = 0.0, f"share stop — {is_now:.0f}% impression share and not rising: the requirement is re-based from actual volume, not bought"
            # conversion rate for the loss stop: own top of search with 30+ clicks, else the product's planning rate
            rate = (n90['tos']['o'] / tos90) if tos90 >= 30 else PLAN_RATE
            rate_src = 'own top of search, 90 days' if tos90 >= 30 else 'product planning rate'
            stop_price = HARD_STOP_X * contrib * rate
            p0, b0 = em.get('price_now'), an.get('base')
            b1 = b0
            base_why = 'base held'
            leak = mixw in ('d14', 'deal8') and (mix['pp_sh'] or 0) > 0.20
            if (cat == 'IN_LEAK' or leak) and b0:
                pp = mix['pp_sh'] or 0
                ords = mix['detail']['o'] + mix['other']['o']
                cut = 0.10 if pp < 0.30 else 0.20 if pp < 0.50 else 0.35
                cut = min(cut, 0.25 if ords else 0.50)
                b1 = max(0.50, b0 * (1 - cut))
                base_why = f"base −{cut:.0%} for product pages at {pct(pp)} ({mixw})"
            udp = (dl['tos']['s'] / dl['tos']['c']) if (c.get('bid_strategy') == 'AUTO_FOR_SALES' and dl['tos']['c']) else None
            p1 = p0 * (1 + step) if p0 else None
            if udp and p0:
                p1 = max(p1, udp); step_why += f"; fixed bidding starts near what dynamic paid in the deal ({udp:.2f})"
            stopped = False
            if p1 and p1 > stop_price:
                if p0 >= stop_price:
                    p1, stopped = p0, True; step_why = f"loss stop reached — at {p0:.2f} a top-of-search order already costs {p0 / rate:.0f} (stop {HARD_STOP_X:.0f}× contribution = {HARD_STOP_X * contrib:.0f})"
                else:
                    p1 = stop_price; step_why += f"; stopped at the loss stop {stop_price:.2f}"
            m1 = (p1 / b1 - 1) * 100 if (p1 and b1) else None
            if m1 is not None and m1 > 900:
                b1 = p1 / 10; m1 = 900.0
                base_why += '; modifier would pass the 900% wall — base lifted as a stated trade'
            bud1 = round(budget * 1.3, 2) if (util7 is not None and util7 >= 0.8) else budget
            cpo = (p1 / rate) if (p1 and rate) else None
            push = dict(step=step, step_why=step_why, price0=p0, price1=p1, base0=b0, base1=b1, base_why=base_why, mod0=an.get('tos_mod'),
                        mod1=m1, budget0=budget, budget1=bud1, over_limit=bool(p1 and p1 > lim[1]), cpo=cpo,
                        loss=(cpo - contrib) if cpo else None, zero=(n90['t3'] == 0 and dl['t3'] == 0), rate=rate, rate_src=rate_src, stop_price=stop_price, stopped=stopped,
                        share_stop=share_stop, is30=is30, isd=isd, reach_day=reach_day, unreachable=unreachable, deliv=deliv, udp=udp,
                        n_targets=sum(1 for t in tg if t.get('state') in ('ENABLED', None)), at_req=at_req, contrib=contrib,
                        ud=(c.get('bid_strategy') == 'AUTO_FOR_SALES'), hero_bad=hero_bad, leak=(cat == 'IN_LEAK' or leak))

    restore = []
    for h in last:
        if h['decided'] == '2026-09-10' and h['field'] in ('bid', 'placement_multiplier'):
            restore.append((h['entityLabel'] if h['field'] == 'bid' else ('TOS modifier' if h['placement'] == 'placementTop' else 'ROS modifier' if h['placement'] == 'placementRestOfSearch' else 'PP modifier'), h['before'], h['after']))
    later = [(h['decided'], h['field'], h['placement'], h['before'], h['after']) for h in last if h['decided'] > '2026-09-10']
    return dict(push=push, restore=restore, later=later, cid=cid, name=c['campaign'], short=c['campaign'].replace('DBS4-SP-', ''), obj=c['objective'], focus=c.get('focus'),
                focus_in=focus_in, tier=tr, group=grp, limit=lim, cat=cat, R=R, mixw=mixw, tos90=tos90, budget=budget,
                util7=util7, util14=util14, rank_now=rank_now, rank_30=rank_30, rank_tgt=rank_tgt, lost=lost, plan_wk=plan_wk,
                need_day=need_day, deal_tos_day=deal_tos_day, pre_tos_day=pre_tos_day, tos_is=tos_is, contrib=contrib,
                tos_rate=tos_rate, ceil_tos=ceil_tos, mkt_cvr=mkt_cvr, mkt_ctr=mkt_ctr, hero_bad=hero_bad, stock=st,
                serving=an.get('serving'), child_after=c.get('child_after'), em=em, base=an.get('base'), tos_mod=an.get('tos_mod'),
                last=[(h['decided'], h['field'], h['placement'], h['before'], h['after'], h['entityLabel']) for h in last[-4:]],
                last_date=last_date, stale=[(h['decided'], h['field'], h['placement'], h['before'], h['after']) for h in stale],
                tuner=TUNER.get(cid, {}).get('by_trajectory'), kw=an.get('kw'), bid_strategy=c.get('bid_strategy'), rank_src=rank_src)


_tc = _to = 0
for c in A['campaigns']:
    if c.get('status') == 'ENABLED' and c['objective'] == 'Ranking' and 'Exact' in c['campaign']:
        r = read(c['campaign_id'], 'd90'); _tc += r['tos']['c']; _to += r['tos']['o']
PLAN_RATE = _to / _tc if _tc else 0.10
out = []
for c in A['campaigns']:
    if c.get('status') != 'ENABLED':
        continue
    if c['objective'] == 'Ranking' and 'Exact' in c['campaign']:
        out.append(classify(c))
json.dump(out, open(f'{S}/cats.json', 'w'), default=str)
if __name__ == '__main__':
    from collections import Counter
    print(len(out), Counter(x['cat'] for x in out))
