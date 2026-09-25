"""Traffic gap vs performance gap, by syntax group and by keyword, for B4 (59) and B6 (30).
Targets follow the app's own bars: target CTR = 1.1 x market CTR, target CVR = 3 x market CVR (SQP)."""
import json, glob, os, re
from collections import defaultdict

S = os.path.dirname(os.path.abspath(__file__))
B = f'{S}/b46'
CTR_X, CVR_X = 1.1, 3.0


def J(p):
    return json.load(open(p))


def pages(prefix):
    fs = sorted(glob.glob(f'{B}/{prefix}_p*.json'), key=lambda f: int(re.search(r'_p(\d+)\.json', f).group(1)))
    if not fs and os.path.exists(f'{B}/{prefix}.json'):
        fs = [f'{B}/{prefix}.json']
    rows = []
    for f in fs:
        rows += J(f).get('rows', [])
    return rows


def syntax(prod, win):
    d = J(f'{B}/{prod}_syntax_{win}.json')
    out = {}
    for r in d['rows']:
        m = r.get('market') or {}
        out[r['groupName']] = dict(id=r.get('syntaxGroupId'), sv=r.get('searchVolume'), impr=r.get('impressions'), clicks=r.get('clicks'), ctr=r.get('ctr'), cvr=r.get('cvr'),
                                   orders=r.get('orders'), spend=r.get('spend'), sales=r.get('sales'), acos=r.get('acos'), share=r.get('spendShare'),
                                   mctr=m.get('marketCtr'), mcvr=m.get('marketCvr'), clickshare=m.get('clickShare'))
    return out


def rank_grid(prod):
    """group -> {date: rank} ; keyword -> {date: rank}"""
    g = {}
    fa = f'{B}/{prod}_ranks_groups_all.json'
    files = [fa] if os.path.exists(fa) else glob.glob(f'{B}/{prod}_ranks_group_*.json')
    for f in files:
        d = J(f)
        for r in d.get('rows', []):
            name = r.get('groupName') or r.get('keyword')
            g[name] = {c['date']: c.get('rank') for c in r.get('cells', []) if c.get('state') == 'ranked'}
    k = {}
    fk = f'{B}/{prod}_ranks_keywords.json'
    if os.path.exists(fk):
        for r in J(fk).get('rows', []):
            name = r.get('keyword') or r.get('groupName')
            k[name] = {c['date']: c.get('rank') for c in r.get('cells', []) if c.get('state') == 'ranked'}
    return g, k


def at(series, date, back=6):
    """rank as the median of the ranked days in the 7 days ending on the date (one reading swings too much)"""
    from datetime import date as D, timedelta
    d0 = D.fromisoformat(date)
    v = sorted(series[(d0 - timedelta(days=i)).isoformat()] for i in range(7) if series.get((d0 - timedelta(days=i)).isoformat()) is not None)
    if not v:
        return None
    n = len(v)
    return round(v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2)


def kw_rows(prod, win):
    rows = pages(f'{prod}_keywords_{win}')
    out = {}
    for r in rows:
        pl = r.get('placements') or {}
        t, dt, o = pl.get('tos') or {}, pl.get('detail') or {}, pl.get('other') or {}
        out[r['keyword']] = dict(sv=r.get('searchVolume'), rel=r.get('relevancy'), impr=r.get('impressions'), clicks=r.get('clicks'), ctr=r.get('ctr'), cvr=r.get('cvr'),
                                 orders=r.get('orders'), spend=r.get('spend'), acos=r.get('acos'), rank=r.get('rank'), syntax=r.get('syntax'),
                                 tos_impr=t.get('impressions'), tos_clicks=t.get('clicks'), tos_ctr=t.get('ctr'), tos_cvr=t.get('cvr'), tos_cpc=t.get('cpc'),
                                 tos_share=t.get('clicksShare'), pp_clicks=dt.get('clicks'), pp_share=dt.get('clicksShare'), pp_cvr=dt.get('cvr'),
                                 ros_clicks=o.get('clicks'))
    return out


def ourkw(prod):
    rows = pages(f'{prod}_ourkw')
    return {r['keyword']: r for r in rows}


def verdict(tos_impr, tos_clicks, tos_ctr, tos_cvr, mctr, mcvr, is_=None, tos_share=None, need_wk=None, days=30):
    """traffic gap = we are not shown / clicked enough at top of search; performance gap = shown, but CTR or CVR under target."""
    tctr = mctr * CTR_X if mctr else None
    tcvr = mcvr * CVR_X if mcvr else None
    ctr_ok = None if (tos_ctr is None or tctr is None or (tos_impr or 0) < 300) else tos_ctr >= tctr
    cvr_ok = None if (tos_cvr is None or tcvr is None or (tos_clicks or 0) < 15) else tos_cvr >= tcvr
    thin = (tos_clicks or 0) < 15
    low_is = is_ is not None and is_ < 10
    short = need_wk is not None and tos_clicks is not None and (tos_clicks / days * 7) < 0.7 * need_wk
    perf_bad = (ctr_ok is False) or (cvr_ok is False)
    traffic_bad = (tos_impr or 0) < 300 or thin or low_is or short
    if (tos_impr or 0) < 100:
        v = 'NOT PRESENT at top of search'
    elif perf_bad and traffic_bad:
        v = 'BOTH — short of traffic and under target'
    elif perf_bad:
        v = 'PERFORMANCE GAP — shown, but ' + ' and '.join(x for x, ok in (('CTR', ctr_ok), ('CVR', cvr_ok)) if ok is False) + ' under target'
    elif traffic_bad:
        v = 'TRAFFIC GAP — converts when shown, not shown/clicked enough'
    elif is_ is None:
        v = 'MEETS THE BARS — impression share not read'
    else:
        v = 'ON TRACK'
    return dict(verdict=v, tctr=tctr, tcvr=tcvr, ctr_ok=ctr_ok, cvr_ok=cvr_ok, thin=thin, low_is=low_is, short=short)


def targets_is(prod):
    """keyword -> best exact target row across pulled campaigns (by spend): tos IS, eff TOS bid, campaign"""
    out = {}
    for f in glob.glob(f'{B}/{prod}_targets_30d_*.json'):
        try:
            d = J(f)
        except Exception:
            continue
        cid = d.get('campaignId')
        for r in d.get('rows') or []:
            if 'Exact' not in (r.get('targetType') or ''):
                continue
            k = r.get('target')
            cur = out.get(k)
            if cur is None or (r.get('spend') or 0) > cur['spend']:
                t = (r.get('placements') or {}).get('tos') or {}
                out[k] = dict(cid=cid, is_=r.get('tosImpressionShare'), eff=r.get('effBidTos'), bid=r.get('bid'), spend=r.get('spend') or 0,
                              clicks=r.get('clicks'), tclicks=t.get('clicks'), tcpc=t.get('cpc'), tctr=t.get('ctr'), tcvr=t.get('cvr'), timpr=t.get('impressions'))
    return out


def group_members(prod):
    """keyword -> set of syntax groups it belongs to (from the keyword rows' own 'syntax' plus size tokens)"""
    sizes = {'King': ['king'], 'Queen': ['queen'], 'Full': ['full', 'double'], 'Twin': ['twin'], 'California King': ['california king', 'cal king']}
    def groups(k, prim):
        g = {prim} if prim else set()
        kl = k.lower()
        for s, toks in sizes.items():
            if any(t in kl for t in toks):
                if s == 'King' and ('california king' in kl or 'cal king' in kl):
                    continue
                g.add(f'Size: {s}')
        return g
    return groups


def group_table(prod, win='30d'):
    syn = syntax(prod, win)
    kws = kw_rows(prod, win)
    gfn = group_members(prod)
    agg = defaultdict(lambda: defaultdict(float))
    for k, r in kws.items():
        for g in gfn(k, r['syntax']):
            a = agg[g]
            for f in ('tos_impr', 'tos_clicks', 'pp_clicks', 'ros_clicks'):
                a[f] += r.get(f) or 0
            if r.get('tos_cvr') is not None:
                a['tos_orders'] += (r.get('tos_clicks') or 0) * r['tos_cvr'] / 100
                a['cvr_clicks'] += r.get('tos_clicks') or 0
            a['tos_spend'] += (r.get('tos_clicks') or 0) * (r.get('tos_cpc') or 0)
    gr, _ = rank_grid(prod)
    out = []
    for g, s in syn.items():
        a = agg.get(g, {})
        ti, tc = a.get('tos_impr', 0), a.get('tos_clicks', 0)
        allc = tc + a.get('pp_clicks', 0) + a.get('ros_clicks', 0)
        tctr = tc / ti * 100 if ti >= 100 else None
        tcvr = a.get('tos_orders', 0) / a['cvr_clicks'] * 100 if a.get('cvr_clicks') else None
        v = verdict(ti, tc, tctr, tcvr, s['mctr'], s['mcvr'])
        ser = gr.get(g, {})
        ranks = {d: at(ser, d) for d in ('2026-06-24', '2026-08-15', '2026-09-14', '2026-09-24')}
        out.append(dict(group=g, **s, tos_impr=ti, tos_clicks=tc, tos_share=tc / allc * 100 if allc else None, tos_ctr=tctr, tos_cvr=tcvr,
                        tos_cpc=a.get('tos_spend', 0) / tc if tc else None, ranks=ranks, **v))
    return out


BRANDY = ('decolure', 'b0')


def kw_table(prod, n_spend=15, plan=None):
    k30, kd = kw_rows(prod, '30d'), kw_rows(prod, 'deal')
    syn = syntax(prod, '30d')
    _, kr = rank_grid(prod)
    ti = targets_is(prod)
    ok = ourkw(prod) if glob.glob(f'{B}/{prod}_ourkw*') else {}
    keys = [k for k in kr if not any(b in k for b in BRANDY)]
    for k, r in sorted(k30.items(), key=lambda x: -(x[1]['spend'] or 0)):
        if len(keys) >= len(kr) + n_spend:
            break
        if k not in keys and not any(b in k for b in BRANDY) and r.get('rel') in ('Highly Relevant', 'Relevant', None):
            keys.append(k)
    out = []
    for k in keys:
        r = k30.get(k) or {}
        d = kd.get(k) or {}
        s = syn.get(r.get('syntax')) or {}
        t = ti.get(k) or {}
        o = ok.get(k) or {}
        ser = kr.get(k, {})
        ranks = {x: at(ser, x) for x in ('2026-06-24', '2026-08-15', '2026-09-14', '2026-09-24')}
        tc30, tcd = r.get('tos_clicks') or 0, d.get('tos_clicks') or 0
        pre_day = (tc30 - tcd) / 20 if tc30 else 0
        need = (plan or {}).get(k, {}).get('ppc_clicks_target')
        v = verdict(r.get('tos_impr'), tc30, r.get('tos_ctr'), r.get('tos_cvr'), s.get('mctr'), s.get('mcvr'), is_=t.get('is_'), need_wk=need)
        wsv = o.get('weekly_search_volume')
        out.append(dict(kw=k, syntax=r.get('syntax'), sv=r.get('sv'), wsv=wsv, clicks=r.get('clicks'), orders=r.get('orders'), acos=r.get('acos'), spend=r.get('spend'),
                        tos_impr=r.get('tos_impr'), tos_clicks=tc30, tos_share=r.get('tos_share'), pp_share=r.get('pp_share'), tos_ctr=r.get('tos_ctr'), tos_cvr=r.get('tos_cvr'),
                        tos_cpc=r.get('tos_cpc'), deal_tos_day=tcd / 10, pre_tos_day=pre_day, is_=t.get('is_'), eff=t.get('eff'), cid=t.get('cid'),
                        mctr=s.get('mctr'), mcvr=s.get('mcvr'), ranks=ranks, org=o.get('organic_rank'), sp=o.get('sp_rank'), top3c=o.get('top3_click_share'),
                        top3v=o.get('top3_conversion_share'), ad_dist=o.get('traffic_dist_ad'),
                        wk_share=(tc30 / 30 * 7 / wsv * 100) if wsv else None, **v))
    return out


def reco(r):
    v = r['verdict']
    gap = None
    rk = r['ranks'].get('2026-09-24')
    if v.startswith('NOT PRESENT'):
        return 'Eligibility first: confirm the exact campaign is enabled and its TOS price clears the group market limit; then push +25% on TOS and read in 3 days.'
    if v.startswith('TRAFFIC'):
        return 'Buy the traffic: it converts at top of search. Raise the TOS modifier by the rank-gap step, lift budget if it caps, and hold base so PDP does not grow.'
    if v.startswith('PERFORMANCE'):
        what = []
        if r['ctr_ok'] is False: what.append('CTR (main image, price shown, review stars, title vs query)')
        if r['cvr_ok'] is False: what.append('CVR (price vs rivals, deal badge/coupon, the size/colour child the ad lands on)')
        return 'More bid buys more of the same shortfall. Hold the TOS price, fix ' + ' and '.join(what) + '; re-test the bid after the fix.'
    if v.startswith('BOTH'):
        return 'Fix the offer first, then buy traffic: a small TOS probe (+10%) only while the CTR/CVR fix is made.'
    return 'Meets the CTR/CVR bars and wins TOS: scale while rank moves; if rank stalls, the gap is volume vs rivals — raise by the rank-gap step.'


if __name__ == '__main__':
    import sys
    prod = sys.argv[1] if len(sys.argv) > 1 else 'b6'
    if len(sys.argv) > 2:
        f = lambda x, n=1: '-' if x is None else f'{x:.{n}f}'
        for r in kw_table(prod):
            print(f"{r['kw'][:30]:30} {str(r['syntax'])[:12]:12} wsv {r['wsv']} clk {r['clicks']} | TOS {f(r['tos_clicks'],0)} ({f(r['tos_share'],0)}%) ctr {f(r['tos_ctr'])}/{f((r['tctr'] or 0))} cvr {f(r['tos_cvr'])}/{f(r['tcvr'] or 0)} IS {f(r['is_'])} eff {f(r['eff'],2)} | d/day {f(r['deal_tos_day'])} pre {f(r['pre_tos_day'])} | rk {list(r['ranks'].values())} org {r['org']} sp {r['sp']} | {r['verdict'][:22]}")
        sys.exit()
    for r in sorted(group_table(prod), key=lambda r: -(r['spend'] or 0)):
        f = lambda x, n=2: '-' if x is None else f'{x:.{n}f}'
        print(f"{r['group'][:22]:22} sp {f(r['spend'],0):>6} clk {r['clicks']} ctr {f(r['ctr'])} cvr {f(r['cvr'])} mkt {r['mctr']}/{r['mcvr']} | TOS {f(r['tos_clicks'],0)} ({f(r['tos_share'],0)}%) tctr {f(r['tos_ctr'])} tcvr {f(r['tos_cvr'])} tcpc {f(r['tos_cpc'])} | rank {list(r['ranks'].values())} | {r['verdict']}")
