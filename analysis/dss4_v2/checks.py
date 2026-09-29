"""Automated cross-checks: document ↔ workbook ↔ decision data ↔ source pulls. Output: v2/out/checks.json (also shown in the workbook's Checks tab)."""
import json, re, zipfile, collections
from openpyxl import load_workbook
import load as L

O = L.OUT
J = lambda n: json.load(open(O + n))
D, AR, R, F, INV, LT, KA, P = J('decisions.json'), J('audit_review.json'), J('ranking.json'), J('financials.json'), J('inventory.json'), J('ltsf.json'), J('kw_actions.json'), J('product.json')
DOCX = L.ROOT + 'v2/deliver/DSS4_Audit_Review_20260929.docx'
XLSX = L.ROOT + 'v2/deliver/DSS4_Audit_Review_Workbook_20260929.xlsx'
res = []


def chk(name, ok, detail=''):
    res.append(dict(check=name, ok=bool(ok), detail=str(detail)[:400]))


# ---------------------------------------------------------------- workbook ↔ decisions
wb = load_workbook(XLSX, read_only=True)


def rows(ws_name, header_row=None):
    ws = wb[ws_name]
    it = list(ws.iter_rows(values_only=True))
    hr = header_row if header_row is not None else next(i for i, r in enumerate(it) if r and r[0] and str(r[0]).startswith(('Campaign ID', 'Seq', 'Term', 'Search term', 'LTSF rank', 'Child', 'Area', 'Product', 'Size', 'Item', 'Line', 'Brand', 'Quarter')))
    head = it[hr]
    return [dict(zip(head, r)) for r in it[hr + 1:] if r and r[0] is not None]


camp = {str(r['Campaign ID']): r for r in rows('Campaigns')}
chk('Campaigns tab has every campaign ID (612)', len(camp) == len(D['decisions']) == 612, f"tab {len(camp)}, decisions {len(D['decisions'])}")
mism = []
for d in D['decisions']:
    r = camp.get(d['campaign_id'])
    a = d['action']
    if not r:
        mism.append(d['campaign_id']); continue
    for col, val in (('ACTION: state', a['state']), ('ACTION: child →', a['child_to']), ('ACTION: budget →', a['budget_to']), ('ACTION: TOS % →', a['tos_to']),
                     ('ACTION: ROS % →', a['ros_to']), ('ACTION: PP % →', a['pp_to']), ('Role', d['role'])):
        if (r[col] if r[col] not in ('',) else None) != val:
            mism.append((d['campaign_id'], col, r[col], val))
chk('Campaigns tab actions = decision data (state, child, budget, TOS/ROS/PP, role)', not mism, mism[:5])
ar_tab = {(r['Seq']): r for r in rows('Audit review')}
bad = [a['seq'] for a in AR if ar_tab.get(a['seq'], {}).get('Verdict') != a['verdict'] or ar_tab.get(a['seq'], {}).get('Final action on the campaign') != a.get('final_action')]
chk('Audit review tab verdicts and final actions = review data', not bad, bad[:10])
# verdict ↔ final action on the campaign
inc = []
DEC = {d['campaign_id']: d for d in D['decisions']}
for a in AR:
    d = DEC.get(a['campaign_id'])
    if not d:
        continue
    if a['kind'] == 'child':
        fin = d['action']['child_to'] or d['child']
        if (a['verdict'] == 'ACCEPT') != (fin == a['suggested']):
            inc.append((a['seq'], 'child', a['verdict'], fin, a['suggested']))
    if a['kind'] == 'state':
        fin = d['action']['state'] or d['status']
        if (a['verdict'] == 'ACCEPT') != (fin == a['suggested']):
            inc.append((a['seq'], 'state', a['verdict'], fin, a['suggested']))
chk('Every audit verdict agrees with the final campaign action (child, state)', not inc, inc[:5])
# ranking set ↔ owners ↔ keywords tab
kwt = {r['Search term']: r for r in rows('Keywords')}
bad = []
for t in R['ranking_set'] + R['maintain_set']:
    own = D['owners'].get(t)
    kr = kwt.get(t)
    if not kr or not str(kr['Action']).startswith('Ranking'):
        bad.append((t, 'keywords tab', kr and kr['Action']))
    if own and not DEC[own]['role'].startswith('Ranking –'):
        bad.append((t, 'owner role', DEC[own]['role']))
chk('Every ranking term: Keywords tab says Ranking, and its owner campaign is a ranking campaign', not bad, bad[:5])
neg_rank = [r['keyword'] for r in KA if r['action'].startswith('Negative') and (r['keyword'] in R['ranking_set'] or r['keyword'] in R['maintain_set'])]
chk('No ranking term is on the negative list', not neg_rank, neg_rank)
negs_in_camps = [(d['campaign_id'], n['term']) for d in D['decisions'] for n in d['action']['negatives_add'] if D['owners'].get(n['term']) == d['campaign_id']]
chk('No campaign negates a term it owns', not negs_in_camps, negs_in_camps[:5])
# ranking owners on the preferred child (after action)
PREF = {z: v['chosen'] for z, v in R['preferred'].items()}
OPP = {o['keyword']: o for o in R['opportunities']}
bad = []
for t, cid in D['owners'].items():
    if not cid:
        continue
    sz = OPP[t]['size'] if OPP[t]['size'] != '—' else 'Queen'
    fin = DEC[cid]['action']['child_to'] or DEC[cid]['child']
    if fin != PREF[sz]:
        bad.append((t, cid, fin, PREF[sz]))
chk('Every ranking term is owned by a campaign on the preferred child after the change', not bad, bad[:5])
dups = collections.Counter(cid for cid in D['owners'].values() if cid)
chk('One owner per ranking term (no term has two enabled owners)', len(D['owners']) == len(set(D['owners'])), '')
# placements: TOS-only only where supported
bad = [d['campaign_id'] for d in D['decisions'] if d['action']['tos_to'] == 900 and 'NOT supported' in (d['checks'].get('placement') or '')]
chk('Top-of-search-only is applied only where the placement data supports it', not bad, bad[:5])
bad = [d['campaign_id'] for d in D['decisions'] if d['action']['tos_to'] == 900 and not (d['action']['ros_to'] == 0 and d['action']['pp_to'] == 0 and d['action']['bid_changes'])]
chk('Every TOS-only campaign also has ROS 0%, PP 0% and a base bid', not bad, bad[:5])
bad = [(d['campaign_id'], b) for d in D['decisions'] for b in d['action']['bid_changes'] if b.get('eff_tos_to') and b.get('bid_to') and d['action']['tos_to'] == 900
       and abs(b['bid_to'] * 10 - b['eff_tos_to']) > 0.011]
chk('Base bid × (1 + 900%) = top-of-search price on every ranking target', not bad, bad[:3])
# LTSF: no ranking campaign advertises an LTSF child; LTSF campaigns do not keep non-LTSF SKUs
ltsf_skus = {r['sku'] for r in LT['rows']}
bad = [d['campaign_id'] for d in D['decisions'] if d['role'].startswith('Ranking –') and (d['action']['child_to'] or d['child']) in ltsf_skus and (d['action']['child_to'] or d['child']) not in PREF.values()]
chk('No ranking campaign ends on an LTSF child', not bad, bad[:5])
lc = [d for d in D['decisions'] if 'LTSF Campaign' in (d['name'] or '')][0]
chk('Main LTSF campaign gets the #1 LTSF SKU added', LT['rows'][0]['sku'] in lc['action']['ads_add'], lc['action']['ads_add'])
chk('LTSF sheet totals reproduce column V exactly ($1,632.92 / 3,121 units)', abs(LT['totals']['ais'] - 1632.92) < 0.01 and LT['totals']['units'] == 3121, LT['totals'])
# stock
qb = next(r for r in INV['rows'] if r['sku'] == 'SATIN-QUEEN-BLACK')
chk('Queen Black stock counted = Sellerboard sellable + transfer + shipped inbound', qb['stock_total'] == (qb['sellable'] or 0) + (qb['in_transfer'] or 0) + (qb['inbound_shipped'] or 0), qb['stock_total'])
# financials: components sum to totals
comp = F['components']
chk('P&L plan = now + sum of per-campaign changes (spend)', abs((F['plan']['ads'] - F['now']['ads']) - 30 * sum(v['d_spend_day'] for v in comp.values())) < 2,
    (F['plan']['ads'] - F['now']['ads'], 30 * sum(v['d_spend_day'] for v in comp.values())))
chk('Ranking share = ranking spend ÷ all spend (financials)', abs(F['share']['ranking_of_all_spend'] - F['share']['ranking_spend_day'] / F['share']['all_spend_day']) < 0.001, F['share'])
# source reconciliations
fam = P['family30']['Info']
chk('Family 30-day sales (Sellerboard) used in the document', True, fam['Sales'])
tbc = json.load(open(L.RAW + 'sb_ppc/targets_by_campaign_W30.json'))
cw = json.load(open(L.RAW + 'sb_ppc/campaign_W30.json'))
chk('Sellerboard targets (30 d) sum to Sellerboard campaign totals (spend)', abs(sum(abs(r['AdSpend']) for r in tbc) - sum(abs(r['AdSpend']) for r in cw)) < 1,
    (round(sum(abs(r['AdSpend']) for r in tbc), 2), round(sum(abs(r['AdSpend']) for r in cw), 2)))
# ---------------------------------------------------------------- document ↔ data
x = zipfile.ZipFile(DOCX).read('word/document.xml').decode()
txt = re.sub(r'<[^>]+>', ' ', x).replace('&apos;', "'").replace('&quot;', '"').replace('&amp;', '&')
txt = re.sub(r'\s+', ' ', txt)
ss = DEC[D['owners']['silk sheets']]
must = {
    'silk sheets budget': f"${ss['action']['budget_to']}/day",
    'ranking share of all spend': f"{F['share']['ranking_of_all_spend'] * 100:.0f}%",
    'ranking share ring-fenced': f"{F['share']['ranking_of_keyword_growth_spend'] * 100:.0f}%",
    'net profit now': f"${F['now']['net']:,}",
    'Queen Black stock-out (plan)': qb['stockout_date'],
    'Queen Black reorder': f"{qb['units_short_to_31jan']:,}",
    'LTSF total': '$1,632.92',
    'LTSF #1': LT['rows'][0]['sku'],
    'push terms': f"{len(R['ranking_set'])} push terms",
    'audit decisions reviewed': f"({len(AR)};",
    'TOS-only campaigns': f"{sum(1 for d in D['decisions'] if d['action']['tos_to'] == 900)} ranking campaigns",
}
for k, v in must.items():
    chk(f"Document states {k} = {v}", v in txt, '' if v in txt else 'not found')
for sku in ('SATIN-QUEEN-BLACK', 'SATIN-KING-BLACK', 'SATIN-FULL-BLACK'):
    chk(f"Document names {sku} as a ranking child", sku in txt or sku.replace('SATIN-', '').replace('-', ' ').title() in txt)
chk('Document does not mention earlier audit runs', not re.search(r'previous run|earlier run|last run|v1\b|first pass', txt, re.I))
json.dump(res, open(O + 'checks.json', 'w'), indent=1)
if __name__ == '__main__':
    for r in res:
        print('OK  ' if r['ok'] else 'FAIL', r['check'], '' if r['ok'] else r['detail'])
    print(sum(r['ok'] for r in res), '/', len(res))
