"""B4 run 20260928-9e6e6bb5 — campaign-by-campaign review against "Bids and Placements on Exact Campaigns" (25 Sep revision).
One row per enabled campaign. Every figure is read from Command Center pulls to 2026-09-27; the run export is the reference for
what the engine proposes. B4 only — no rule or figure from B6."""
import json, os, re, glob, statistics
from collections import defaultdict, Counter
from datetime import date, timedelta

S = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(f'{S}/a.json'))
END = '2026-09-27'
CONTRIB_DEFAULT = A['brief']['sections']['margin']['contribution_per_unit']
BE = A['brief']['sections']['margin']['be_acos']
SKU = json.load(open(f'{S}/skus.json'))
INV = {r['sku']: r for r in json.load(open(f'{S}/inventory_children.json'))}
LTSF = set(json.load(open(f'{S}/ltsf_skus.json'))) if os.path.exists(f'{S}/ltsf_skus.json') else None
DAYS = dict(d90=90, pre_deal30=31, deal=13, d30=30, d14=14, d7=7)


def load(label):
    p = f'{S}/placements_{label}.jsonl'
    return {json.loads(l)['campaignId']: json.loads(l) for l in open(p)} if os.path.exists(p) else {}


PL = {w: load(w) for w in DAYS}


def read(cid, w):
    r = PL[w].get(cid) or {}
    p = r.get('placements') or {}
    def pl(k):
        x = p.get(k) or {}
        c = x.get('clicks') or 0
        cvr = x.get('cvr')
        o = x.get('orders') if x.get('orders') is not None else (round(c * cvr / 100) if (cvr is not None and c) else 0)
        return dict(c=c, o=o or 0, i=x.get('impressions') or 0, cpc=x.get('cpc'), s=(x.get('cpc') or 0) * c)
    t, d, o = pl('tos'), pl('detail'), pl('other')
    clk = r.get('clicks') or 0
    return dict(have=bool(r), impr=r.get('impressions') or 0, clicks=clk, orders=r.get('orders') or 0, spend=r.get('spend') or 0,
                sales=r.get('sales') or 0, tos=t, pp=d, ros=o, t3=t['c'] + d['c'] + o['c'],
                tos_sh=(t['c'] / (t['c'] + d['c'] + o['c'])) if (t['c'] + d['c'] + o['c']) else None,
                pp_sh=(d['c'] / (t['c'] + d['c'] + o['c'])) if (t['c'] + d['c'] + o['c']) else None)


# ---- targets (top-of-search impression share, effective bid) per campaign
def targets(cid, win):
    p = f'{S}/b4_targets_{win}_{cid}.json'
    if not os.path.exists(p):
        return []
    t = open(p).read()
    try:
        d = json.loads(t)
    except Exception:
        d = json.loads(json.loads(t)[0]['text'])
    return d.get('rows') or []


# ---- ranks: tracker 7-day median
TRACK = {}
for r in json.load(open(f'{S}/b46/b4_ranks_keywords.json'))['rows']:
    if r.get('keyword'):
        TRACK[r['keyword']] = {c['date']: c.get('rank') for c in r.get('cells', []) if c.get('state') == 'ranked' and c.get('rank')}


def med7(kw, end):
    s = TRACK.get(kw)
    if not s:
        return None
    d0 = date.fromisoformat(end)
    v = sorted(s[(d0 - timedelta(days=i)).isoformat()] for i in range(7) if (d0 - timedelta(days=i)).isoformat() in s)
    return v[len(v) // 2] if v else None


# ---- keyword targets (DataRova): target rank and target units over the 30-day window
KT = {}
for f in glob.glob(f'{S}/b46/b4_keywords_30d_p*.json'):
    for r in json.load(open(f))['rows']:
        t = r.get('targets') or {}
        KT[r['keyword']] = dict(rank=t.get('rank'), units30=t.get('units'), clicks30=t.get('clicks'), ctr=r.get('ctr'), cvr=r.get('cvr'),
                                tos=(r.get('placements') or {}).get('tos') or {}, syntax=r.get('syntax'), sv=r.get('searchVolume'))

# ---- market CTR/CVR by syntax group (SQP, 30 days)
MKT = {r['groupName']: (r.get('market') or {}) for r in json.load(open(f'{S}/b46/b4_syntax_30d.json'))['rows']}

# ---- the run's decisions per campaign
DEC = defaultdict(list)
for x in A['decisions']:
    if x['verdict'] == 'change':
        DEC[x.get('campaign_id')].append(x)
DUP = json.load(open(f'{S}/dup_exact.json')) if os.path.exists(f'{S}/dup_exact.json') else {}
KWC = json.load(open(f'{S}/kwcamp/summary.json')) if os.path.exists(f'{S}/kwcamp/summary.json') else {}
RANKTERMS = {c.get('plan_keyword') for c in A['campaigns'] if c.get('status') == 'ENABLED' and c['objective'] == 'Ranking' and c.get('plan_keyword')}
short_name = lambda n: re.sub(r'^D[A-Z0-9]+-SP-', '', n)[:40]
HOLDS = defaultdict(list)
for x in A['considered']:
    HOLDS[x.get('campaign_id')].append(x)


def fnum(v):
    try:
        return float(v)
    except Exception:
        return None


def match_type(name):
    n = name
    if re.search(r'\bAuto\b|\(AUTO\)', n, re.I): return 'Auto'
    if 'PAT' in n or 'Targeting' in n or re.search(r'\bB0[0-9A-Z]{8}\b', n): return 'PAT'
    if 'Broad' in n: return 'Broad'
    if 'Phrase' in n: return 'Phrase'
    if re.search(r'Exact|\bEX\b', n): return 'Exact'
    return '?'


def name_objective(n):
    m = re.search(r'\((Ranking|Conversions?|Discovery|DISC|Defensive|Clearance|Liquidation|Conquesting)\)', n)
    if not m: return None
    return {'Conversion': 'Conversions', 'DISC': 'Discovery', 'Clearance': 'Liquidation'}.get(m.group(1), m.group(1))


def expected_objective(c, mt):
    """the standard: brand term = Defensive; Exact = Ranking; Auto/Broad/Phrase = Discovery (LTSF clearance keeps Liquidation);
    product targeting = Conversions"""
    n = c['campaign'].lower()
    brand = 'decolure' in n or 'defensive' in n
    if c['objective'] == 'Liquidation' or 'ltsf' in n:
        return 'Liquidation'
    if brand:
        return 'Defensive'
    return {'Exact': 'Ranking', 'Auto': 'Discovery', 'Broad': 'Discovery', 'Phrase': 'Discovery', 'PAT': 'Conversions'}.get(mt)


def child_size(sku):
    m = re.match(r'BAMBOO-(CALIFKING|KING|QUEEN|FULL|TWIN)-', sku or '')
    return m.group(1) if m else None


def term_size(text):
    t = ' ' + re.sub(r'[^a-z ]', ' ', text.lower()) + ' '
    for k, v in (('california king', 'CALIFKING'), ('cal king', 'CALIFKING'), ('calking', 'CALIFKING'), (' king ', 'KING'), (' queen ', 'QUEEN'), (' full ', 'FULL'), (' double ', 'FULL'), (' twin ', 'TWIN')):
        if k in t:
            return v
    return None


COLOURS = {'black': 'BLACK', 'white': 'WHITE', 'grey': 'GREY', 'gray': 'GREY', 'olive': 'OLIVE', 'moss green': 'OLIVE', 'sage': 'SAGEGREEN', 'navy': 'NAVYBLUE',
           'light blue': 'LIGHTBLUE', 'blue': 'BLUE', 'pink': 'PINK', 'purple': 'PURPLE', 'burgundy': 'BURGUNDY', 'red': 'BURGUNDY', 'cream': 'CREME',
           'creme': 'CREME', 'ivory': 'CREME', 'taupe': 'TAUPE', 'charcoal': 'CHARCOAL', 'army green': 'OLIVE', 'green': 'GREEN'}


def term_colour(text):
    t = ' ' + re.sub(r'[^a-z ]', ' ', text.lower()) + ' '
    for k in sorted(COLOURS, key=len, reverse=True):
        if f' {k} ' in t:
            return COLOURS[k]
    return None


def term_text(c):
    kw = c.get('plan_keyword')
    if kw:
        return kw
    n = re.sub(r'^D[A-Z0-9]+-SP-', '', c['campaign'])
    return re.split(r'-\[|-\(', n)[0]


def group_of(c):
    m = re.search(r'\[([^\]]+)\]', c['campaign'])
    if m:
        return m.group(1)
    kw = c.get('plan_keyword') or ''
    return (KT.get(kw) or {}).get('syntax') or 'Bamboo'


# ---- rates: the group's top-of-search and product-page rate stands in for the child's planning rate (no child rate exists)
_g = defaultdict(lambda: [0, 0, 0, 0])
ENABLED = [c for c in A['campaigns'] if c.get('status') == 'ENABLED']
for c in ENABLED:
    if c['objective'] == 'Ranking':
        r = read(c['campaign_id'], 'd90'); g = _g[group_of(c)]
        g[0] += r['tos']['c']; g[1] += r['tos']['o']; g[2] += r['pp']['c']; g[3] += r['pp']['o']
_all = [sum(v[i] for v in _g.values()) for i in range(4)]
PLAN_TOS = _all[1] / _all[0] if _all[0] else 0.12
PLAN_PP = _all[3] / _all[2] if _all[2] else 0.10
GR = {k: (v[1] / v[0] if v[0] >= 50 else PLAN_TOS, v[3] / v[2] if v[2] >= 50 else PLAN_PP) for k, v in _g.items()}


def blend(clicks, orders, child):
    if clicks < 15:
        return child, 'child rate (under 15 clicks)'
    if clicks < 50:
        if not orders:
            return child, f'child rate (no order on {clicks} clicks)'
        w = (clicks - 15) / 35
        return child + (orders / clicks - child) * w, f'blend {w:.0%} own on {clicks} clicks'
    return orders / clicks, f'own, {clicks} clicks'


def contrib_of(c):
    for x in DEC.get(c['campaign_id'], []) + HOLDS.get(c['campaign_id'], []):
        t = ' '.join(r['text'] for r in (x.get('rationale') or []))
        m = re.search(r'against \$([\d.]+) contribution per order', t)
        if m:
            return float(m.group(1)), 'run'
    s = SKU.get(c.get('child') or '')
    if s and s[1]:
        return s[1], 'child economics'
    return CONTRIB_DEFAULT, 'product margin'


def stock_of(sku):
    r = INV.get(sku or '')
    if not r:
        return None
    return dict(avail=r.get('fba_available'), inbound=r.get('inbound'), vel=r.get('velocity_day'), days=r.get('days_of_stock'))


HERO = {r['size']: r for r in A['context']['inventory']}
# the ranking SKU per size (operator 2026-09-28): White, unless White cannot carry the push — then the highest-selling variation with
# healthy stock, until White lands. Read on Sellerboard units (30 days), FBA stock and cover, 2026-09-28.
PREFERRED = {'KING': 'BAMBOO-KING-WHITE', 'CALIFKING': 'BAMBOO-CALIFKING-WHITE', 'QUEEN': 'BAMBOO-QUEEN-LIGHTBLUE',
             'FULL': 'BAMBOO-FULL-OLIVE', 'TWIN': 'BAMBOO-TWIN-NAVYBLUE'}
PREF_WHY = {'QUEEN': 'Queen White has 23 days of cover against a 27 Oct arrival and sells on its own; Light Blue is the next seller with 70 days',
            'FULL': 'Full White is out until 27 Oct; Olive is the size’s top seller with 75 days',
            'TWIN': 'Twin White has none available until 16 Oct; Navy Blue is the next seller with healthy stock (81 days)'}
SIZE_NAME = {'CALIFKING': 'California King', 'KING': 'King', 'QUEEN': 'Queen', 'FULL': 'Full', 'TWIN': 'Twin'}

DEAL_ON = False          # the Best Deal ran 09-15 -> 09-28; next dated deal 10-26 (placeholder)
FUNDED_PUSH = False      # framework §6/§11: no velocity window after 09-28, so no premium until a push is funded and dated


def review(c):
    cid = c['campaign_id']; name = c['campaign']; mt = match_type(name); obj = c['objective']
    R = {w: read(cid, w) for w in DAYS}
    r90, r30, r14, r7, pre, dl = R['d90'], R['d30'], R['d14'], R['d7'], R['pre_deal30'], R['deal']
    row = dict(cid=cid, campaign=name, status=c.get('status'), objective=obj, match=mt, child=c.get('child'), focus=(c.get('focus') or ''),
               budget=c.get('budget'), tos_mod=c.get('tos'), pp_mod=c.get('pp'), ros_mod=c.get('ros'), strategy=c.get('bid_strategy'),
               plan_kw=c.get('plan_keyword'), n_targets=len(c.get('targets') or []),
               enabled_targets=sum(1 for t in (c.get('targets') or []) if t.get('state') == 'ENABLED'))
    for w in ('d90', 'd30', 'd14', 'd7', 'pre_deal30', 'deal'):
        x = R[w]
        row[w] = dict(impr=x['impr'], clicks=x['clicks'], ctr=(x['clicks'] / x['impr'] * 100) if x['impr'] else None, orders=x['orders'],
                      cvr=(x['orders'] / x['clicks'] * 100) if x['clicks'] else None, spend=round(x['spend'], 2),
                      cpc=(x['spend'] / x['clicks']) if x['clicks'] else None, acos=(x['spend'] / x['sales'] * 100) if x['sales'] else None,
                      tos_c=x['tos']['c'], pp_c=x['pp']['c'], ros_c=x['ros']['c'], tos_sh=x['tos_sh'], pp_sh=x['pp_sh'], tos_o=x['tos']['o'], pp_o=x['pp']['o'])
    row['util7'] = (r7['spend'] / 7 / c['budget']) if (c.get('budget') and r7['have']) else None
    issues, fixes = [], []

    # ---------- 1. objective
    exp = expected_objective(c, mt); nob = name_objective(name)
    row['obj_expected'] = exp; row['obj_in_name'] = nob
    if exp and obj not in (exp, 'Sponsored Brands', 'Sponsored Display') and not (obj == 'Conversions' and mt == 'Exact' and 'FIX' in name and exp == 'Ranking' and False):
        issues.append(f"OBJECTIVE: tagged {obj} but a {mt} campaign is {exp} by the standard")
        fixes.append(f"retag {obj} → {exp}")
    if nob and nob != obj and obj not in ('Sponsored Brands',):
        issues.append(f"OBJECTIVE: the name says {nob}, the tag says {obj}")

    # ---------- 2. SKU (advertised child) against the campaign's job
    ch = c.get('child'); sz_ch = child_size(ch); sz_t = term_size(term_text(c))
    ranking = (exp == 'Ranking' or obj == 'Ranking') and mt == 'Exact'
    pref = PREFERRED.get(sz_ch or sz_t or '')
    row['preferred_child'] = pref
    col = term_colour(term_text(c) + ' ' + name.split('-DO-')[0].split('-FIX-')[0])
    row['term_colour'] = col
    if ranking and ch and col and col != 'WHITE':
        if col not in ch.replace(' ', ''):
            issues.append(f"SKU: the term names {col.title()} but the campaign advertises {ch}")
            fixes.append(f"advertise the {col.title()} child of the size")
    elif ranking and ch and pref and ch != pref:
        issues.append(f"SKU: ranking campaign advertises {ch}; the size’s ranking SKU is {pref}" + (f" ({PREF_WHY[sz_ch or sz_t]})" if PREF_WHY.get(sz_ch or sz_t) else ''))
        fixes.append(f"advertise {pref}")
    if mt in ('Auto', 'Broad', 'Phrase') and obj != 'Defensive':
        if LTSF is None:
            if ch and 'WHITE' in ch:
                issues.append(f"SKU: {mt} campaign advertises the White ranking SKU {ch}; it should advertise an LTSF SKU (list pending)")
        elif ch not in LTSF:
            issues.append(f"SKU: {mt} campaign advertises {ch}, not an LTSF SKU")
            fixes.append('advertise the size’s LTSF SKU')
    if sz_ch and sz_t and sz_ch != sz_t and mt in ('Exact', 'Phrase', 'Broad'):
        issues.append(f"SKU: the campaign’s term is {SIZE_NAME[sz_t]} but it advertises a {SIZE_NAME[sz_ch]} child ({ch})")
    row['stock'] = stock_of(ch)
    row['run'] = [f"{x['kind']} {x['current_at_audit']}→{x['suggested']}" for x in DEC.get(cid, [])]
    swap = [x for x in DEC.get(cid, []) if x['kind'] == 'child']
    if swap and (ranking or mt == 'Exact'):
        to = swap[0]['suggested']
        if pref and not col and to != pref:
            issues.append(f"RUN: swaps this campaign {swap[0]['current_at_audit']} → {to}; the ranking SKU for the size is {pref}")

    # ---------- 3. ranking economics and the framework's reads
    if ranking:
        kw = c.get('plan_keyword'); kt = KT.get(kw) or {}; grp = group_of(c)
        ctos, cpp = GR.get(grp, (PLAN_TOS, PLAN_PP))
        tos_rate, tos_src = blend(r90['tos']['c'], r90['tos']['o'], ctos)
        pp_rate, pp_src = blend(r90['pp']['c'], r90['pp']['o'], cpp)
        contrib, csrc = contrib_of(c)
        ceil_tos, ceil_pp = contrib * tos_rate, contrib * pp_rate
        tg = targets(cid, '30d'); tgd = targets(cid, 'deal')
        main = next((t for t in tg if t.get('target') == kw), None) or (max(tg, key=lambda t: t.get('spend') or 0) if tg else None)
        maind = next((t for t in tgd if main and t.get('target') == main.get('target')), None)
        base = (main or {}).get('bid'); eff = (main or {}).get('effBidTos')
        if base is None:
            base = next((t['bid'] for t in c.get('targets') or [] if t.get('label') == kw), None)
        tos_price = eff or (base * (1 + (c.get('tos') or 0) / 100) if base else None)
        is30 = (main or {}).get('tosImpressionShare'); isd = (maind or {}).get('tosImpressionShare')
        # required clicks/day = target units/day ÷ top-of-search conversion (framework §7)
        units_day = (kt.get('units30') or 0) / 30 if kt.get('units30') else None
        n_camp = sum(1 for x in ENABLED if x.get('plan_keyword') == kw and x['objective'] == 'Ranking') or 1
        req = (units_day / tos_rate / n_camp) if (units_day and tos_rate) else None
        deliv_pre = pre['tos']['c'] / 31; deliv_14 = r14['tos']['c'] / 14; deliv_deal = dl['tos']['c'] / 13 if dl['have'] else None
        rank_now, rank_30, rank_pre = med7(kw, END), med7(kw, '2026-08-28'), med7(kw, '2026-09-14')
        tgt_rank = kt.get('rank')
        mk = MKT.get(grp) or MKT.get(grp.split('|')[0]) or {}
        mctr, mcvr = mk.get('marketCtr'), mk.get('marketCvr')
        tos_ctr = (r30['tos']['c'] / r30['tos']['i'] * 100) if r30['tos']['i'] >= 300 else None
        tos_cvr = (r90['tos']['o'] / r90['tos']['c'] * 100) if r90['tos']['c'] >= 15 else None
        ctr_ok = None if (tos_ctr is None or not mctr) else tos_ctr >= 1.1 * mctr
        cvr_ok = None if (tos_cvr is None or not mcvr) else tos_cvr >= 3 * mcvr
        hero = HERO.get(SIZE_NAME.get(sz_ch or sz_t or '', ''), {})
        st = row['stock'] or {}
        stock_ok = (st.get('days') or 0) >= 30 or (st.get('inbound') or 0) > 0 and (st.get('days') or 0) >= 14
        conds = dict(velocity=DEAL_ON or FUNDED_PUSH, ctr=ctr_ok, cvr=cvr_ok, stock=stock_ok)
        row.update(kw=kw, group=grp, contrib=round(contrib, 2), contrib_src=csrc, tos_rate=tos_rate, tos_src=tos_src, pp_rate=pp_rate, pp_src=pp_src,
                   ceil_tos=round(ceil_tos, 2), ceil_pp=round(ceil_pp, 2), base=base, tos_price=round(tos_price, 2) if tos_price else None,
                   is30=is30, is_deal=isd, units_day=units_day, req_day=req, deliv_pre=deliv_pre, deliv_14=deliv_14, deliv_deal=deliv_deal,
                   rank_now=rank_now, rank_30=rank_30, rank_pre=rank_pre, rank_tgt=tgt_rank, mctr=mctr, mcvr=mcvr, tos_ctr=tos_ctr, tos_cvr=tos_cvr,
                   conds=conds, engine_ceiling=next((x.get('rule') for x in HOLDS.get(cid, []) + DEC.get(cid, []) if (x.get('rule') or '').startswith('ceiling')), None))
        # ---- the situation (framework §12), in order
        mix_w = r14 if r14['t3'] >= 15 else (pre if pre['t3'] >= 15 else r90)
        tsh, psh = mix_w['tos_sh'], mix_w['pp_sh']
        sit, act = None, []
        lost = (rank_now - rank_30) if (rank_now and rank_30) else None
        if r90['t3'] == 0 and r30['impr'] == 0:
            sit = 'DEAD — no impressions in 90 days'
            act.append('check the ad, the child and eligibility; price the term at its ceiling or pause it — nothing to read')
        elif lost is not None and lost > 10:
            sit = f'RANK COLLAPSING ({rank_30} → {rank_now})'
            act.append('never scale spend: freeze price and budget; check the listing, the child it serves, the rival now ahead, category-wide movement')
        elif tsh is not None and tsh < 0.30:
            sit = f'NOT A RANKING CAMPAIGN IN PRACTICE — top of search {tsh:.0%}'
            act.append('distribution fix first and only: cut the base, re-solve the modifier to hold the top-of-search price; no climb, no budget move')
        elif psh is not None and psh > 0.20:
            sit = f'LEAKING — product pages {psh:.0%}'
            act.append('distribution fix: base toward the product-page ceiling, modifier re-solved so top of search holds')
        elif mix_w['t3'] == 0:
            sit = 'NO CLICKS — on, not delivering'
            act.append('hold the base, move the modifier only (cutting the base of a row that is not delivering makes it worse)')
        elif rank_now and tgt_rank and rank_now <= tgt_rank:
            sit = f'AT TARGET RANK ({rank_now} vs {tgt_rank})'
            act.append('price probe: top of search −3–5%, watch click share, absolute clicks and rank; restore on any miss' + ('; organic top 3 → 15% incrementality step' if rank_now <= 3 else ''))
        elif rank_now is None:
            sit = 'NO RANK ON FILE'
            act.append('not a push (framework §6): top of search at the ceiling, no premium; becomes a push candidate once a rank read exists')
        else:
            sit = f'SHORT OF TARGET ({rank_now} vs {tgt_rank or "—"})'
            missing = [k for k, v in conds.items() if v is not True]
            if missing:
                act.append(f"maintenance: top of search at the ceiling ${ceil_tos:.2f}, no premium — push conditions missing: {', '.join(missing)}")
            else:
                act.append('funded push: premium sized on the binding gap, climb ≤30% a write')
        # ---- price decision (maintenance unless funded)
        if tos_price and ceil_tos:
            if 'COLLAPSING' in sit or 'DEAD' in sit:
                price_to = tos_price
            elif tos_price > ceil_tos * 1.005 and 'AT TARGET' not in sit:
                # descent to a named point (framework §9); a row with no delivery goes straight there, one with delivery in ≤50% steps
                price_to = ceil_tos if r30['tos']['c'] == 0 else max(ceil_tos, tos_price * 0.50)
                row['descent_final'] = round(ceil_tos, 2)
            elif tos_price < ceil_tos and 'LEAK' not in sit and 'NOT A RANKING' not in sit:
                price_to = min(ceil_tos, tos_price * 1.30)                   # climb to the ceiling, capped 30%
            elif 'AT TARGET' in sit:
                price_to = tos_price * 0.96
            else:
                price_to = min(tos_price, ceil_tos) if tos_price > ceil_tos else tos_price
            base_to = base
            if base and psh is not None and psh > 0.20 and 'COLLAPSING' not in sit and 'DEAD' not in sit:
                # distribution fix: the base comes down — toward what product pages afford where it sits above that, sized to the leak
                # otherwise; ≤50% a write, ≤25% where product pages carry orders; never raised, never under the $0.35 floor
                cap = 0.25 if (mix_w['pp']['o'] + mix_w['ros']['o']) else 0.50
                leak_step = 0.10 if psh < 0.30 else 0.20 if psh < 0.50 else 0.35
                want = max(base * (1 - cap), ceil_pp) if base > ceil_pp else base * (1 - leak_step)
                base_to = max(0.35, min(base, max(want, base * (1 - cap))))
            mod_to = (price_to / base_to - 1) * 100 if (base_to and price_to) else None
            if mod_to is not None and mod_to > 900:
                base_to = price_to / 10; mod_to = 900.0
            row.update(price_to=round(price_to, 2), base_to=round(base_to, 2) if base_to else None, mod_to=round(mod_to) if mod_to is not None else None)
        # ---- budget
        if row['util7'] is not None and row['util7'] >= 0.8 and 'LEAK' not in sit:
            act.append(f"budget capping ({row['util7']:.0%} used, 7 days) — raise it before reading price; rates are truncated")
        # ---- ROS modifier earns a lift only on 15+ clicks converting at or above product pages
        if (c.get('ros') or 0) > 0:
            ros_ok = r90['ros']['c'] >= 15 and r90['pp']['c'] and (r90['ros']['o'] / r90['ros']['c']) >= (r90['pp']['o'] / r90['pp']['c'] if r90['pp']['c'] else 1)
            if not ros_ok:
                issues.append(f"ROS modifier {c['ros']}% not earned (framework §8: 15+ rest-of-search clicks converting at or above product pages)")
                fixes.append('rest-of-search modifier → 0%')
        # ---- delivery vs requirement
        if req:
            d = deliv_14
            row['deliv_ratio'] = d / req if req else None
            reach = (d / (is30 / 100)) if (is30 and d) else None
            row['reach_day'] = reach
            if reach is not None and reach < req:
                issues.append(f"TRAFFIC: needs {req:.1f} top-of-search clicks/day; winning every auction at today’s volume would give ~{reach:.1f} — the requirement is above what the auction holds")
        row.update(situation=sit, action=act)
        # ---- judge the run's price move
        rp = [x for x in DEC.get(cid, []) if x['kind'] in ('tos', 'bid')]
        if rp and row.get('price_to') and tos_price:
            tosx = next((x for x in rp if x['kind'] == 'tos'), None); bidx = next((x for x in rp if x['kind'] == 'bid'), None)
            b1 = fnum(bidx['suggested']) if bidx else base
            m1 = fnum(tosx['suggested']) if tosx else (c.get('tos') or 0)
            if b1 and m1 is not None:
                run_price = b1 * (1 + m1 / 100)
                row['run_price'] = round(run_price, 2)
                if abs(run_price - row['price_to']) / max(row['price_to'], 0.01) > 0.10:
                    issues.append(f"RUN PRICE: the run takes top of search {tos_price:.2f} → {run_price:.2f}; the framework read gives {row['price_to']:.2f}")
    # ---------- 4. every other objective: priced inside its own ceiling (contribution × its conversion; ACoS ≤ break-even)
    if not ranking and obj not in ('Sponsored Brands', 'Sponsored Display'):
        x = r30
        acos = (x['spend'] / x['sales']) if x['sales'] else None
        acos90 = (r90['spend'] / r90['sales']) if r90['sales'] else None
        contrib, _ = contrib_of(c)
        cvr = (x['orders'] / x['clicks']) if x['clicks'] else None
        ceil_cpc = contrib * cvr if cvr else None
        cpc = (x['spend'] / x['clicks']) if x['clicks'] else None
        if obj == 'Liquidation':
            sit = 'CLEARANCE — priced on the storage fee it avoids'
            act = ['hold unless ACoS keeps rising; the LTSF lane sets the floor' + (f' (30d ACoS {acos:.0%})' if acos else '')]
        elif x['clicks'] < 15:
            sit = 'THIN (<15 clicks in 30 days)'
            act = ['hold at today’s values — no readable conversion rate']
        elif acos is None or acos > BE * 1.05:
            tgt = ceil_cpc if ceil_cpc else (cpc * 0.5 if cpc else None)
            step = max(-0.5 if not x['orders'] else -0.25, (tgt / cpc - 1)) if (tgt and cpc) else -0.25
            sit = f"OVER ITS CEILING — ACoS {'no orders' if acos is None else f'{acos:.0%}'} vs break-even {BE:.0%}"
            act = [f"base down {-step:.0%} (CPC ${cpc:.2f} → ${cpc * (1 + step):.2f}); the ceiling is ${ceil_cpc:.2f} a click" if (cpc and ceil_cpc) else f"base down {-step:.0%}"]
        else:
            sit = f'INSIDE ITS CEILING — ACoS {acos:.0%}'
            act = ['hold; nothing moves, including the top-of-search modifier']
        row.update(situation=sit, action=act, acos30=acos, acos90=acos90, ceil_cpc=ceil_cpc, cpc30=cpc)
        rm = DEC.get(cid, [])
        cut = [m for m in rm if m['kind'] in ('tos', 'bid') and fnum(m['suggested']) is not None and fnum(m['current_at_audit']) is not None and fnum(m['suggested']) < fnum(m['current_at_audit'])]
        raise_ = [m for m in rm if m['kind'] in ('tos', 'bid', 'budget') and fnum(m['suggested']) is not None and fnum(m['current_at_audit']) is not None and fnum(m['suggested']) > fnum(m['current_at_audit'])]
        if ('INSIDE' in sit or 'THIN' in sit) and cut:
            issues.append(f"RUN: cuts a campaign that is {sit.split(' —')[0].lower()} ({', '.join(m['kind'] + ' ' + m['current_at_audit'] + '→' + m['suggested'] for m in cut[:3])}) — hold instead")
        if 'OVER' in sit and raise_:
            issues.append(f"RUN: raises a campaign that is over its ceiling ({', '.join(m['kind'] + ' ' + m['current_at_audit'] + '→' + m['suggested'] for m in raise_[:3])})")
        if 'OVER' in sit and not any(m['kind'] == 'bid' for m in cut):
            issues.append('MISSING: over its ceiling and the run does not bring the base down')
    # ---------- 5. keyword ownership: one enabled exact owner per term
    for t in c.get('targets') or []:
        if t.get('state') == 'ENABLED' and (t.get('match') or '').upper() == 'EXACT':
            others = [x for x in DUP.get(t['label'].lower(), []) if x[0] != name[:60]]
            if others:
                mine = t.get('clicks') or 0; best = max([mine] + [x[3] or 0 for x in others])
                issues.append(f"KEYWORD: “{t['label']}” is also bought exact by {others[0][0]} — one owner per term; " + ('this campaign keeps it' if mine >= best and mine > 0 else 'pause it here (the other campaign carries more of its clicks)' if best > mine else 'keep the one on the ranking SKU, pause the other'))
    # ---------- 6. search terms: a ranking term bought by Auto/Broad/Phrase — the exact row is not earning its own rank credit
    kwn = c.get('plan_keyword')
    if ranking and kwn in KWC and 'decolure' not in (kwn or ''):
        leak = [x for x in KWC[kwn] if (x.get('matchType') or '').upper() not in ('EXACT', 'PRODUCT TARGETING') and (x.get('clicks') or 0) > 0 and 'Defensive' not in x['campaign']]
        if leak:
            tot = sum(x['clicks'] or 0 for x in KWC[kwn]); lc = sum(x['clicks'] for x in leak)
            issues.append(f"SEARCH TERM: “{kwn}” — {lc} of its {tot} clicks (30d) go to {', '.join(short_name(x['campaign']) + ' (' + str(x['clicks']) + ')' for x in leak[:3])}")
            fixes.append(f"negative-exact “{kwn}” in {', '.join(short_name(x['campaign']) for x in leak[:3])}")
    if mt in ('Auto', 'Broad', 'Phrase') and obj != 'Defensive':
        took = [(k, x['clicks'], x['spend']) for k, v in KWC.items() for x in v if x.get('campaignId') == cid and (x.get('clicks') or 0) > 0 and k in RANKTERMS and 'decolure' not in k]
        if took:
            issues.append(f"SEARCH TERM: buys {len(took)} exact ranking terms ({sum(t[1] for t in took)} clicks, ${sum(t[2] for t in took):.0f} in 30d) — " + ', '.join(f'“{t[0]}” {t[1]}' for t in sorted(took, key=lambda t: -t[1])[:5]))
            fixes.append('negative-exact the ranking terms it buys (they belong to their exact campaigns)')
    row['issues'] = issues; row['fixes'] = fixes
    return row


# ---------- King White push (operator, 28 Sep): King joins B4's focus, but only on the King terms the push actually needs.
# Selection: the term advertises King White; CTR ≥ 1.1× and CVR ≥ 3× market on a readable sample; stock holds; rank short of
# target; real demand (search volume / impressions); the requirement is reachable and fundable at a loss per order the unit can carry.
MARKET_TOL = 0.15          # framework §8: what top of search clears at on the term (its own 30-day TOS CPC) + 15%
PUSH_READ, PUSH_CHECK = '2026-10-05', '2026-10-12'
KING_PUSH = {
    '528754073143175': dict(stage='push now', term_cpc=6.16, predict='rank 22 → 15 by 12 Oct; 8 by the end of the 26 Oct deal'),
    '49275908512250': dict(stage='push after the mix is fixed', term_cpc=4.76, predict='rank 25 → 10 once top of search carries ≥70% of clicks'),
}


def apply_king_push(r):
    k = KING_PUSH.get(r['cid'])
    if not k:
        return r
    rank_gap = r['rank_now'] / r['rank_tgt']
    deliv_gap = (r['req_day'] / r['deliv_14']) if r.get('deliv_14') else None
    priced_deliv = deliv_gap if (k['stage'] == 'push now' and (r.get('util7') or 0) < 0.8 and (r.get('is30') or 100) < 20) else None   # a mix problem is not priced
    g = max(rank_gap, priced_deliv or 0)
    lift = 0 if g <= 1 else 0.25 if g <= 1.5 else (g - 1) * 0.5
    wants = r['ceil_tos'] * (1 + lift)
    bound = k['term_cpc'] * (1 + MARKET_TOL)
    target = min(wants, bound, r['contrib'])
    binds = 'market bound' if bound <= min(wants, r['contrib']) else 'gap' if wants <= r['contrib'] else 'per-unit bound'
    now = r['tos_price']
    cvr = r['tos_rate']
    push = dict(stage=k['stage'], rank_gap=round(rank_gap, 2), deliv_gap=round(deliv_gap, 2) if deliv_gap else None, lift=round(lift, 3),
                gap_wants=round(wants, 2), bound=round(bound, 2), target=round(target, 2), binds=binds,
                cpo=round(target / cvr, 2), loss_per_order=round(target / cvr - r['contrib'], 2), predict=k['predict'],
                read=PUSH_READ, checkpoint=PUSH_CHECK)
    if k['stage'] == 'push now':
        this = min(target, now * 1.30) if target > now else target
        base_to = r['base']
        other = (r['d30']['clicks'] - r['d30']['tos_c']) / 30 * r['base'] if r['d30']['clicks'] else 0
        day = r['req_day'] * this + other
        push.update(this_write=round(this, 2), budget_day=round(day), budget_week=round(day * 7), loss_ceiling_week=round(day * 7),
                    expected_loss_week=round(r['req_day'] * cvr * 7 * max(0, this / cvr - r['contrib'])))
        r['situation'] = f"KING WHITE PUSH — funded ({r['rank_now']} → {r['rank_tgt']})"
        r['action'] = [f"top of search {now:.2f} → {this:.2f} this write (target {target:.2f}, {binds}); base {base_to:.2f} held; budget ${r['budget']:.0f} → ${day:.0f}/day; read {PUSH_READ}, checkpoint {PUSH_CHECK}"]
        r.update(price_to=round(this, 2), base_to=base_to, mod_to=round((this / base_to - 1) * 100), descent_final=None)
    else:
        # mix first (framework §12: TOS under 30% → distribution fix takes precedence); the TOS price is held, not descended, because the
        # term is queued for the push — it never falls as a residue of the base cut
        base_to = r['base_to']
        this = now
        day = r['req_day'] * target
        push.update(this_write=round(this, 2), budget_day_at_target=round(day), entry='top of search ≥70% of clicks for 7 days')
        r['action'] = [f"distribution fix first: base {r['base']:.2f} → {base_to:.2f}, top of search held at {now:.2f} (queued for the King push, so not descended); push entry when top of search carries ≥70% of clicks for 7 days"]
        r.update(price_to=round(this, 2), base_to=base_to, mod_to=round((this / base_to - 1) * 100), descent_final=None)
    r['push'] = push
    r['issues'] = [i for i in r['issues'] if not i.startswith('RUN PRICE')]
    return r


if __name__ == '__main__':
    out = [apply_king_push(review(c)) for c in ENABLED]
    json.dump(out, open(f'{S}/review.json', 'w'), default=str)
    print(len(out), Counter(r.get('situation', '').split(' (')[0].split(' —')[0] for r in out if r.get('situation')))
    print('issues:', Counter(i.split(':')[0] for r in out for i in r['issues']))
