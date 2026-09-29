"""Stage 6 — Campaigns: every campaign id seen in any source (612), its current settings and metrics from each source side by side,
its role (ranking / non-ranking), and the action with the reason. Placements, preferred child, budget and spend-share follow from
ranking.py. Output: v2/out/campaigns.json"""
import json, re, os, collections, math
import load as L

P = json.load(open(L.OUT + 'product.json'))
R = json.load(open(L.OUT + 'ranking.json'))
KW = {k['keyword']: k for k in json.load(open(L.OUT + 'keywords.json'))}
SKU = {s['sku']: s for s in P['skus']}
ASIN2SKU = collections.defaultdict(list)
for s in P['skus']:
    ASIN2SKU[s['asin']].append(s['sku'])
PREF = {z: v['chosen'] for z, v in R['preferred'].items()}
PUSH_SIZES = {z for z, v in R['preferred'].items() if v['basis'].startswith('highest')}
OPP = {o['keyword']: o for o in R['opportunities']}
RANK_SET = set(R['ranking_set'])

IDS = json.load(open(L.RAW + 'campaign_ids.json'))
A = {a['campaign_id']: a for a in L.AUDIT['campaigns']}
C3, C9 = L.CC_CAMP30, L.CC_CAMP90
S3 = {r['Id']: r for r in L.rows(L.SB_PPC.get('campaign_W30', []))}
S9 = {r['Id']: r for r in L.rows(L.SB_PPC.get('campaign_W90', []))}
T = L.CC_TARGETS
DD = {}                                                    # Data Dive: campaign -> advertised ASINs (window 30 d)
if os.path.exists(L.RAW + 'dd/ads_by_asin.json'):
    for asin, v in json.load(open(L.RAW + 'dd/ads_by_asin.json'))['by_asin'].items():
        for c in v['campaigns']:
            d = DD.setdefault(str(c['campaignId']), dict(asins=set(), row=c))
            d['asins'].add(asin)

# family paid conversion (Command Center product totals, 30 days) — used only for the zero-order significance test
FAM = L.J(L.RAW + 'cc/summary.json')
PAID_CVR = None
try:
    t = FAM.get('totals') or FAM.get('summary') or FAM
    PAID_CVR = t['orders'] / t['clicks']
except Exception:
    PAID_CVR = 1572 / 11617


def p_zero(clicks, cvr):
    return (1 - cvr) ** clicks if clicks else 1.0


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def ad_type(cid, name):
    s = S3.get(cid) or S9.get(cid)
    if s:
        return {'sp': 'SP', 'sb': 'SB', 'sbv': 'SBV', 'sd': 'SD'}.get(s['TypeAD'], s['TypeAD'])
    c = C3.get(cid) or C9.get(cid)
    if c and c.get('adProduct'):
        return {'Sponsored Products': 'SP', 'Sponsored Brands': 'SB', 'Sponsored Display': 'SD'}.get(c['adProduct'], c['adProduct'])
    a = A.get(cid) or {}
    if a.get('objective') == 'Sponsored Brands':
        return 'SB'
    if a.get('objective') == 'Sponsored Display':
        return 'SD'
    n = (name or '').upper()
    if re.search(r'\bSBV\b|VIDEO', n):
        return 'SBV'
    if re.search(r'\bSB\b|HSA|HEADLINE', n):
        return 'SB'
    if re.search(r'\bSD\b|DISPLAY', n):
        return 'SD'
    return 'SP'


def name_child(name):
    m = re.search(r'(SATIN-[A-Z0-9 -]+?|SS-SATIN-[A-Z0-9 -]+?)(-V\d+)?\s*$', (name or '').upper())
    return m.group(1).strip() if m else None


def size_of_sku(s):
    return (SKU.get(s) or {}).get('size')


def targets_of(cid):
    """target texts with the source that listed them"""
    out = {}
    for src, c in (('cc30', C3.get(cid)), ('cc90', C9.get(cid))):
        if c and c.get('targets'):
            for t in str(c['targets']).split(' · '):
                out.setdefault(t.strip().lower(), set()).add(src)
    for t in (A.get(cid) or {}).get('targets') or []:
        out.setdefault((t.get('label') or '').strip().lower(), set()).add('audit')
    tt = T.get(cid)
    if tt:
        for t in tt.get('targets') or []:
            out.setdefault((t.get('target') or '').strip().lower(), set()).add('cc_targets')
    return {k: sorted(v) for k, v in out.items() if k}


def metrics_cc(c):
    if not c:
        return None
    pl = c.get('placements')
    if pl:
        tos, pp, ros = pl.get('tos') or {}, pl.get('detail') or {}, pl.get('other') or {}
        g = lambda d, f: d.get(f)
    else:
        tos = {f: c.get('tos_' + f) for f in ('clicks', 'clicksShare', 'cvr', 'cpc', 'impressionsShare', 'spend')}
        pp = {f: c.get('detail_' + f) for f in ('clicks', 'clicksShare', 'cvr', 'cpc', 'impressionsShare', 'spend')}
        ros = {f: c.get('other_' + f) for f in ('clicks', 'clicksShare', 'cvr', 'cpc', 'impressionsShare', 'spend')}
    impr, clicks = c.get('impressions') or 0, c.get('clicks') or 0
    return dict(impressions=impr, clicks=clicks, ctr=round(clicks / impr * 100, 2) if impr else None, cpc=c.get('cpc'), orders=c.get('orders') or 0,
                cvr=round(c['cvr'], 2) if c.get('cvr') is not None else None, spend=round(c.get('spend') or 0, 2), sales=round(c.get('sales') or 0, 2), acos=c.get('acos'),
                tos_clicks=tos.get('clicks'), tos_share=tos.get('clicksShare'), tos_cvr=tos.get('cvr'), tos_cpc=tos.get('cpc'),
                ros_clicks=ros.get('clicks'), ros_cvr=ros.get('cvr'), ros_cpc=ros.get('cpc'),
                pp_clicks=pp.get('clicks'), pp_cvr=pp.get('cvr'), pp_cpc=pp.get('cpc'))


def metrics_sb(s):
    if not s:
        return None
    return dict(status=s.get('Status'), budget=s.get('dailyBudget'), utilization=round(s['BudgetUtilization'], 1) if s.get('BudgetUtilization') is not None else None,
                tos_is=s.get('topOfSearch'), spend=round(abs(s.get('AdSpend') or 0), 2), clicks=s.get('Clicks'), orders=s.get('Orders'), sales=s.get('Sales'),
                acos=s.get('ACOS'), cpc=s.get('AverageCPC'), impressions=s.get('Impressions'))


BRAND = re.compile(r'decolure|dec[a-z]{0,3}l[a-z]{0,2}re', re.I)

rows = []
for cid in IDS:
    a, c3, c9, s3, s9, dd = A.get(cid), C3.get(cid), C9.get(cid), S3.get(cid), S9.get(cid), DD.get(cid)
    name = (s3 or s9 or {}).get('Name') or (c9 or c3 or {}).get('campaignName') or (a or {}).get('campaign') or ((dd or {}).get('row') or {}).get('name')
    typ = ad_type(cid, name)
    # ---- status: Sellerboard (live), else audit, else Data Dive
    st_sb = (s3 or s9 or {}).get('Status')
    st_a = (a or {}).get('status')
    st_dd = ((dd or {}).get('row') or {}).get('state')
    status = {'Active': 'ENABLED', 'Paused': 'PAUSED'}.get(st_sb, st_sb) or st_a or st_dd
    # ---- advertised child: Data Dive (ASIN list) confirmed against the audit
    dd_skus = sorted({s for asin in (dd or {}).get('asins', ()) for s in ASIN2SKU.get(asin, [])})
    dd_main = [s for s in dd_skus if not re.match(r'^(Amazon\.Found|[A-Z0-9]{2}-[A-Z0-9]{4}-)', s)] or dd_skus
    a_child = (a or {}).get('child')
    n_child = name_child(name)
    if dd and len(dd['asins']) == 1:
        child, child_src = dd_main[0], 'Data Dive (1 advertised ASIN)'
    elif a_child:
        child, child_src = a_child, 'audit export'
    elif dd_main:
        child, child_src = None, f'Data Dive: {len(dd["asins"])} ASINs advertised'
    else:
        child, child_src = (n_child if n_child in SKU else None), 'campaign name'
    child_conflict = None
    if dd and len(dd['asins']) == 1 and a_child and a_child not in dd_skus:
        child_conflict = f'audit says {a_child}, Data Dive says {dd_main[0]}'
    name_mismatch = bool(child and n_child and n_child != child and n_child in SKU)
    # ---- settings
    tt = (T.get(cid) or {}).get('campaign') or {}
    pm = tt.get('placementModifiersPct') or {}
    ddp = ((dd or {}).get('row') or {}).get('placements') or {}
    mods = dict(tos=pm.get('tos', (a or {}).get('tos')), ros=pm.get('ros', (a or {}).get('ros')), pp=pm.get('pdp', (a or {}).get('pp')))
    budget = (s3 or s9 or {}).get('dailyBudget') or (a or {}).get('budget') or (((dd or {}).get('row') or {}).get('budget') or {}).get('amount')
    strategy = (a or {}).get('bid_strategy') or ((dd or {}).get('row') or {}).get('bidStrategy') or tt.get('biddingStrategy')
    tg = targets_of(cid)
    cc = c3 or c9 or {}
    match = cc.get('matchType') or ('Exact' if re.search(r'exact', name or '', re.I) else 'Phrase' if re.search(r'phrase', name or '', re.I) else
                                    'Broad' if re.search(r'broad', name or '', re.I) else 'Auto' if re.search(r'auto|catch', name or '', re.I) else
                                    'Product Targeting' if re.search(r'PAT|ASIN|B0[A-Z0-9]{8}', name or '') else None)
    rows.append(dict(campaign_id=cid, name=name, ad_type=typ, status=status, status_sources=dict(sellerboard=st_sb, audit=st_a, datadive=st_dd),
                     child=child, child_source=child_src, child_conflict=child_conflict, name_child=n_child, name_mismatch=name_mismatch,
                     dd_asins=sorted((dd or {}).get('asins', ())), size=size_of_sku(child) if child else None,
                     colour=(SKU.get(child) or {}).get('colour') if child else None,
                     budget=budget, utilization=(s3 or {}).get('BudgetUtilization'), tos_is=(s3 or {}).get('topOfSearch'),
                     tos_is_dd=((dd or {}).get('row') or {}).get('tosImpressionShare'), strategy=strategy, mods=mods,
                     mods_dd={k: (ddp.get(k) or {}).get('bidAdjustment') for k in ('topOfSearch', 'restOfSearch', 'productPage')} if ddp else None,
                     match=match, target_type=cc.get('targetType'), objective_cc=cc.get('objective'), objective_audit=(a or {}).get('objective'),
                     syntax=cc.get('syntax') or (a or {}).get('syntax'), targets=tg,
                     m30=metrics_cc(c3), m90=metrics_cc(c9), sb30=metrics_sb(s3), sb90=metrics_sb(s9),
                     audit_plan=dict(state_after=(a or {}).get('state_after'), child_after=(a or {}).get('child_after'), budget_to=(a or {}).get('budget_to'),
                                     tos_to=(a or {}).get('tos_to'), focus=(a or {}).get('focus'), plan_rank=(a or {}).get('plan_rank')) if a else None,
                     sources=[k for k, v in (('audit', a), ('cc30', c3), ('cc90', c9), ('sb30', s3), ('sb90', s9), ('datadive', dd)) if v]))

# ======================================================================================= role
for r in rows:
    ts = list(r['targets'])
    rank_terms = [t for t in ts if t in RANK_SET]
    twin_terms = [t for t in ts if t in OPP and OPP[t]['size'] == 'Twin' and OPP[t]['cum_share_of_market'] <= 0.80 + 1e-9]
    if r['ad_type'] in ('SB', 'SBV'):
        role = 'Sponsored Brands' + (' video' if r['ad_type'] == 'SBV' else '')
    elif r['ad_type'] == 'SD':
        role = 'Sponsored Display'
    elif r['match'] == 'Exact' and r['target_type'] != 'ASIN' and rank_terms:
        role = 'Ranking'
    elif r['match'] == 'Exact' and twin_terms:
        role = 'Ranking term, size on hold (stock)'
    elif any(BRAND.search(t) for t in ts) or (r['objective_cc'] == 'Defensive') or re.search(r'defens', r['name'] or '', re.I):
        role = 'Brand / listing defence'
    elif r['match'] in ('Product Targeting',) or r['target_type'] == 'ASIN':
        role = 'Product targeting'
    elif r['match'] == 'Auto':
        role = 'Auto discovery'
    elif r['match'] in ('Phrase', 'Broad'):
        role = 'Keyword discovery (phrase/broad)'
    elif r['match'] == 'Exact':
        cls = collections.Counter(KW[t]['cls'] if t in KW else ('Core satin/silk' if re.search(r'satin|silk|sateen|silky', t) else 'unknown') for t in ts)
        col = any((KW.get(t) or {}).get('colour') not in (None, 'black') for t in ts)
        role = 'Exact: colour/variant term' if col else ('Exact: other satin/silk term' if cls.get('Core satin/silk') else 'Exact: off-core term')
    else:
        role = 'Unclassified'
    r['role'] = role
    r['rank_terms'] = rank_terms
    r['is_ranking'] = role == 'Ranking'

json.dump(rows, open(L.OUT + 'campaigns_base.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    print(len(rows), collections.Counter(r['status'] for r in rows))
    print(collections.Counter(r['role'] for r in rows))
    print('child sources', collections.Counter(r['child_source'] for r in rows))
    print('name mismatch', sum(r['name_mismatch'] for r in rows), 'child conflicts', sum(1 for r in rows if r['child_conflict']))
    sp = collections.Counter(); cl = collections.Counter()
    for r in rows:
        sp[r['role']] += (r['m30'] or {}).get('spend') or 0
        cl[r['role']] += (r['m30'] or {}).get('clicks') or 0
    tot = sum(sp.values())
    for k, v in sp.most_common():
        print(f'{k:38} spend30 {v:9.0f} {v / tot * 100:5.1f}%  clicks {cl[k]:6.0f}')
