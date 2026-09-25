# Part D — B6: why rank has not moved. Executed inside build_cat_doc.py's namespace (doc, para, lead, bullet, table, section, part, sec_no, CATS, A).
import statistics as _st
import glob as _glob
import json as _json
import diag as _dg
from docx.shared import Cm as _Cm
from collections import Counter

part[0] = 'D'; sec_no[0] = 0
doc.add_page_break()
doc.add_heading('Part D — B6: why rank has not moved, and what to do about it', 1)
para('Erik’s question: across the implementations and tuning so far, rank traction has not come. Is that because we are not driving enough traffic to the top of search (a **traffic gap**), or because we are there and not meeting the target CTR and CVR (a **performance gap**)? This part answers it for B6 on the data to 24 September — for the focus this run sets (Bamboo|Queen, Full, King and Cooling) and for the broad Bamboo terms now out of focus — and adds the performance-vs-tuning history, competitors, the campaign types that should also be running, and the metrics the app should be reading.')

# ---------------------------------------------------------------- data
PLAN = {k['keyword']: k for k in A['brief']['sections']['targets']['keywords']}
KW4 = _dg.kw_table('b6', plan=PLAN)
GR4 = _dg.group_table('b6')
INF = [c for c in CATS if c['focus_in']]
_iss = [c['tos_is'] for c in INF if c.get('tos_is') is not None]
_need = sum(c['need_day'] or 0 for c in INF); _deal = sum(c['deal_tos_day'] or 0 for c in INF)
_nd = [(c['deal_tos_day'] or 0) / c['need_day'] for c in INF if c.get('need_day')]
FK = {c['kw'] for c in INF if c.get('kw')}


def f1(x, d=1, suf=''):
    return '—' if x is None else f'{x:.{d}f}{suf}'


def rk(r):
    v = list(r['ranks'].values())
    return ' → '.join('—' if x is None else str(x) for x in (v[0], v[2], v[3]))


def verdict_short(v):
    return v.split(' — ')[0].replace('NOT PRESENT at top of search', 'NOT PRESENT').title()


def group_is(prod):
    ti = _dg.targets_is(prod); k30 = _dg.kw_rows(prod, '30d')
    acc = {}
    for k, t in ti.items():
        r = k30.get(k)
        if not r or t['is_'] is None: continue
        w = r.get('tos_impr') or 0
        a = acc.setdefault(r['syntax'], [0, 0]); a[0] += t['is_'] * w; a[1] += w
    return {g: (a[0] / a[1] if a[1] else None) for g, a in acc.items()}


GIS4 = group_is('b6')
_up = _n = 0
for _f in _glob.glob(f'{_dg.S}/b6_targets_30d_*.json'):
    _cid = _f.rsplit('_', 1)[1][:-5]
    try:
        _a = _json.load(open(_f)); _b = _json.load(open(f'{_dg.S}/b6_targets_deal_{_cid}.json'))
    except Exception:
        continue
    _bd = {r['target']: r.get('tosImpressionShare') for r in _b['rows']}
    for r in _a['rows']:
        x, y = r.get('tosImpressionShare'), _bd.get(r['target'])
        if x is not None and y is not None:
            _n += 1; _up += y > x
G = {g['group']: g for g in GR4}

_mdtxt = 'Half of them took no top-of-search click at all in those 10 days.' if _st.median(_nd) == 0 else f'The median campaign is at {_st.median(_nd) * 100:.0f}% of its requirement.'
# ---------------------------------------------------------------- D1 answer
section('The answer in one page')
lead('Short answer.', 'A **traffic gap**, and a widening one. Where B6 reaches the top of search it beats the app’s CTR bar (1.1× market CTR) and CVR bar (3× market CVR) on every group with a readable sample. But its ad traffic has been cut by two-thirds since July, it wins a sliver of the top-of-search auctions, and in the last ten days — while B4’s deal bid up the same terms — its share fell further.')
bullet(f'**We are rarely at the top.** Amazon’s top-of-search impression share on the in-focus exact targets has a median of **{_st.median(_iss):.1f}%** ({sum(i < 10 for i in _iss)} of {len(_iss)} under 10%). On “bamboo sheets queen size” it is 0.5% at a $4.56 effective top-of-search bid; on “bamboo sheets king size” 0.8% at $4.80; on the out-of-focus head term “bamboo sheets” 1.8% at $6.10.')
bullet(f'**The volume is a small fraction of the plan.** The run’s click requirements for the {len(INF)} in-focus campaigns add to {_need:.0f} top-of-search clicks a day; over the last 10 days they got **{_deal:.1f} a day ({_deal / _need * 100:.0f}%)**. {_mdtxt} “bamboo sheets queen size” needs 307 clicks a week and got 4.')
bullet('**When we are there, we perform.** At the top of search over 30 days: Bamboo|Queen CVR 32.8% vs a 13.3% bar, Bamboo|Full 46.4% vs 12.2%, Bamboo|King 12.7% vs 10.8%; “bamboo sheets” 18.5% vs 8.3%, “bamboo sheets queen size” 33.4% vs 13.3%. CTR is over its bar on every group with a readable sample. Bamboo|Cooling has 16 top-of-search clicks in 30 days — not present, so the first job there is to get in the auction.')
bullet(f'**Share fell while B4’s deal ran.** Over the last 10 days B6’s impression share fell on the hero terms — “bamboo sheets” 1.8% → 0.5%, “bamboo sheets queen size” 0.5% → 0.1%, “bamboo sheets king size” 0.8% → 0.3% — and rose on {_up} of {_n} targets overall, mostly small ones. B4 raised its prices on the same terms for its deal: on the shared terms one listing can take the other’s auctions, which is why B6 keeps its terms but reads its share daily beside B4’s.')
bullet('**Rank follows the volume down.** On the 7-day median since June: Bamboo 21 → 31, Bamboo|Queen 18 → 40, Bamboo|King 20 → 28; Bamboo|Full recovered 27 → 22. “king size bamboo sheets set” went 9 → 29 and “bamboo sheets queen” 18 → 50.')
bullet('**The tuning took the traffic out.** From late June to the week before B4’s deal, B6’s ad clicks fell from 310 a day to 197, and to 102 in the last 10 days; orders from 45 a day to 14; top-of-search clicks from 77 to 44 a day. ACoS stayed near 25–28% and TACoS fell to 6.6% — the rounds bought efficiency by giving up the volume rank needs.')
lead('What changes.', 'Buy the traffic where it performs — every in-focus term meets its bars — by stepping the top-of-search price daily by the delivery gap, inside the loss stop, the engine-plan envelope and the TACoS guard (Part A), and read impression share with it. On Cooling, where B6 is barely in the auction, the push doubles as the eligibility check. Read B6’s share on the terms B4 is also pushing every day: if one rises as the other falls, the two listings are trading the same auctions and the plan needs one owner per term.')

# ---------------------------------------------------------------- D2 performance vs tuning
section('Overall performance against the tuning so far')
lead('What happened.', 'Four blocks from the daily product series, and the organic group rank (7-day median) at the start of each. The last block is the last 10 days (B4’s Best Deal; B6 had none).')
rows = []
pts = _json.load(open(f'{_dg.B}/b6_daily.json'))['points']
for a, b, wl in (('2026-06-24', '2026-07-23', '24 Jun – 23 Jul'), ('2026-07-24', '2026-08-23', '24 Jul – 23 Aug'), ('2026-08-24', '2026-09-14', '24 Aug – 14 Sep'), ('2026-09-15', '2026-09-24', '15 – 24 Sep')):
    r = [x for x in pts if a <= x['date'] <= b]; n = len(r)
    s = lambda k: sum((x.get(k) or 0) for x in r)
    c, o, sp, sa = s('clicks'), s('orders'), s('spend'), s('sales')
    tac = [x['tacos'] for x in r if x.get('tacos')]
    rows.append(['B6' if a == '2026-06-24' else '', wl, f'{c / n:.0f}', f'{o / n:.1f}', f'${sp / n:,.0f}', f'${sa / n:,.0f}', f'{sp / sa * 100:.1f}%', f'{o / c * 100:.1f}%', f'${sp / c:.2f}', f'{sum(tac) / len(tac):.1f}%' if tac else '—'])
table(['Product', 'Window', 'Ad clicks/day', 'Ad orders/day', 'Spend/day', 'Ad sales/day', 'ACoS', 'CVR', 'CPC', 'TACoS (mean of days)'], rows, widths=[1.2, 2.8, 1.6, 1.6, 1.6, 1.7, 1.3, 1.2, 1.2, 1.8], size=7.5)
rows = []
for g in GR4:
    if g['group'].startswith('Size') or g['group'] == 'Organic & Natural' or (g['spend'] or 0) < 20: continue
    v = list(g['ranks'].values())
    rows.append([g['group'] + (' (in focus)' if g['group'] in ('Bamboo|Queen', 'Bamboo|Full', 'Bamboo|King', 'Bamboo|Cooling') else ''), *['—' if x is None else x for x in v], f"${g['spend']:,.0f}"])
table(['Syntax group', 'Rank 24 Jun', 'Rank 15 Aug', 'Rank 14 Sep', 'Rank 24 Sep', 'Spend 30d'], rows, widths=[5, 2, 2, 2, 2, 2], size=8)
p = f'{_dg.S}/chart_b6.png'
if os.path.exists(p):
    doc.add_picture(p, width=_Cm(16.5)); para('B6 — top of search and product-page clicks per day (all campaigns), the spend-weighted effective top-of-search bid, and the rank of three in-focus groups. Dashed lines: the change rounds of 26 Aug, 11 Sep, 16 Sep and 20 Sep; shaded: B4’s deal to 24 Sep.', size=8.5, color=GREY)
lead('B6.', 'Every round since July took volume out: ad clicks 310 → 265 → 197 → 102 a day, orders 45 → 35 → 28 → 14, top-of-search clicks 77 → 44 a day, product pages 139 → 62. The mix improved because product pages were cut harder than top of search — but top of search fell too, and rank followed: Bamboo 21 → 31, Bamboo|Queen 18 → 40, Bamboo|King 20 → 28. ACoS held at 24–29% and TACoS fell from 12% to under 7%. The 16 and 20 September rounds raised the top-of-search modifier on small campaigns; they did not reach the hero terms, and in the last 10 days, with B4 bidding up the same terms, B6’s share on them fell.')
lead('The lesson for the app.', 'A round that improves ACoS or the mix but lowers top-of-search clicks on an in-focus keyword is a rank loss, not a win — B6’s rounds since July did exactly that. Grade every round on top-of-search clicks delivered against the requirement, and on rank, before ACoS.')

# ---------------------------------------------------------------- D3 method
section('How traffic gap and performance gap are told apart')
lead('Performance bars.', 'The app’s own: target CTR = 1.1 × the market CTR of the keyword’s syntax group (Search Query Performance, 30 days — the last 10 days’ market figures are blank); target CVR = 3 × market CVR. CTR is judged only with 300+ top-of-search impressions, CVR only with 15+ top-of-search clicks — below that the call is “not enough sample”, never a verdict.')
lead('Traffic bars.', 'Three reads, any of which marks a traffic gap: Amazon’s measured top-of-search impression share on the target under 10%; fewer than 15 top-of-search clicks in 30 days; delivered top-of-search clicks under 70% of the requirement.')
lead('Verdicts.', '**Traffic gap** — meets the bars when shown, not shown enough → buy the traffic. **Performance gap** — shown enough, under the CTR or CVR bar → fix the offer before buying more. **Both** — fix the offer while probing. **Not present** — under 100 top-of-search impressions in 30 days → eligibility/price first. **On track** — meets both, impression share ≥ 10% → scale while rank moves. **Meets the bars, share not read** — the group’s CTR and CVR clear the bars but none of its member targets has a share reading (the size groups always).')
lead('Caveat.', 'Amazon reports placement per campaign and performance per keyword, never both; the keyword-level top-of-search figures distribute each keyword’s traffic by its campaigns’ measured split (Command Center’s estimate). Impression share and effective bid are measured per target. Where a keyword runs in one exact campaign — true of most ranking keywords — the split is that campaign’s own.')

# ---------------------------------------------------------------- D4 syntax
section('Syntax groups')
rows = []
for g in sorted(GR4, key=lambda r: -(r['spend'] or 0)):
    if not g['clicks']: continue
    is_ = GIS4.get(g['group'])
    v = _dg.verdict(g['tos_impr'], g['tos_clicks'], g['tos_ctr'], g['tos_cvr'], g['mctr'], g['mcvr'], is_=is_)
    rows.append([g['group'], f"${g['spend']:,.0f} / {g['clicks']:,}", f"{g['tos_clicks']:.0f} ({f1(g['tos_share'], 0)}%)", f"{f1(g['tos_ctr'])} / {f1(v['tctr'])}", f"{f1(g['tos_cvr'])} / {f1(v['tcvr'])}", f1(is_, 1, '%') if is_ is not None else '—',
                 f"{f1(g['tos_cpc'], 2)}", '—' if g['group'].startswith('Size') else ' → '.join('—' if x is None else str(x) for x in g['ranks'].values()), v['verdict']])
doc.add_heading('B6 — 30 days to 24 Sep', 3)
table(['Group', 'Spend / clicks 30d', 'TOS clicks (share)', 'TOS CTR / bar', 'TOS CVR / bar', 'TOS impr. share', 'TOS CPC', 'Rank 24 Jun → 15 Aug → 14 Sep → 24 Sep', 'Verdict'], rows, widths=[2.4, 1.5, 1.8, 1.5, 1.5, 1.3, 1.1, 2.2, 3.4], size=7)
para('Size groups (“Size: King” etc.) are cross-cutting: a keyword is in its primary group and in its size group, so the size rows re-count traffic already shown above. Impression share for a group is the impression-weighted mean of its member targets’ measured share.', size=8.5, color=GREY)
lead('Reading it.', 'Every group with a readable sample meets its CTR and CVR bars at top of search at low single-digit impression share — a traffic gap, B6-wide. The Cooling groups are the exception only in having almost no top-of-search presence to read (Bamboo|Cooling 16 clicks, Cooling 12): not present, so price and eligibility come first.')

# ---------------------------------------------------------------- D5 keywords
section('The main ranking keywords — one call each')
lead('What the columns say.', 'Req/wk = the run’s weekly click requirement for the campaign carrying the keyword, else the brief’s per-keyword figure. TOS/wk = top-of-search clicks a week over 30 days, and over the last 10 days. IS = Amazon’s top-of-search impression share on the exact target, at the effective top-of-search bid shown. Rank = our tracked rank (7-day median) 24 Jun → 14 Sep → 24 Sep.')
_req = {c['kw']: c['plan_wk'] for c in INF if c.get('kw')}
for title_, pick in (('In focus — Bamboo|Queen, Full, King and Cooling', lambda r: r['kw'] in FK and (r['clicks'] or 0) >= 10), ('Out of focus — the main terms', lambda r: r['kw'] not in FK and (r['clicks'] or 0) >= 60)):
    rows = []
    for r in [r for r in KW4 if pick(r)][:16]:
        pl = PLAN.get(r['kw'])
        req = _req.get(r['kw']) or (pl or {}).get('ppc_clicks_target')
        wk = r['tos_clicks'] / 30 * 7
        rows.append([r['kw'][:34], f'{req:.0f}' if req else '—', f"{wk:.0f} / {r['deal_tos_day'] * 7:.0f}",
                     f"{f1(r['tos_ctr'])}/{f1(r['tctr'])}", f"{f1(r['tos_cvr'])}/{f1(r['tcvr'])}", f1(r['is_'], 1, '%') if r['is_'] is not None else '—', f"${r['eff']:.2f}" if r['eff'] else '—',
                     rk(r), verdict_short(r['verdict'])])
    doc.add_heading(title_, 3)
    table(['Keyword', 'Req/wk', 'TOS/wk 30d / last 10d', 'CTR / bar', 'CVR / bar', 'IS', 'Eff. TOS bid', 'Rank', 'Verdict'], rows, widths=[3.8, 1.1, 1.7, 1.5, 1.6, 1.1, 1.3, 2.2, 2.1], size=7)
lead('In focus — what to do, by keyword.', '')
for kw, txt in [
    ('bamboo sheets queen size', 'Traffic gap, the widest: CVR 33% at the top against a 13% bar, 0.5% impression share at $4.56 (0.1% in the last 10 days), 4 top-of-search clicks a week against 307. The delivery-gap step (+30%) is the minimum; read share daily and keep stepping while it rises, inside the loss stop.'),
    ('king size bamboo sheets set / bamboo sheets king size', 'Traffic gaps with the steepest rank loss (9 → 29 and 26 → 36 on the 7-day median). Both convert above the bar at the top (17% vs 11%); share is 4.0% and 0.8% — push both, and check which child each ad serves the same day.'),
    ('bamboo sheets full / bamboo full size bed sheets', 'Full is the group holding rank (12 and 22–24); CVR 46% at the top on the group. Keep stepping while share rises — this is where B6’s volume converts best.'),
    ('bamboo cooling sheets', 'Not present: 3 top-of-search clicks in 30 days, 0% share at $3.16 — far below anything that wins the top. B4 pushes the same term this week. Step it from a floor near its group’s clearing price, read share the next day, and read B4’s share beside it.'),
]:
    bullet(f'**{kw}** — {txt}')
lead('Out of focus.', '“bamboo sheets” is a traffic gap (CVR 18.5% vs 8.3%, 1.8% share at $6.10, rank 29 → 36) and holds flat this run with the flagship; “viscose bamboo sheets” and “bamboo sheets with corner straps” are climbing (14 → 12, 16 → 12) and are in the out-of-focus test (B.1).')

# ---------------------------------------------------------------- D6 why IS is low at the bid
section('Why a $4–7 effective bid wins only 0–4% of top-of-search')
lead('What we know.', 'Impression share at the top is low on almost every target, and on the hero terms it fell over the last 10 days with no cut on B6’s side. Four causes, each with its test:')
bullet('**Price below the top-slot winners.** The engine’s per-campaign market bound is built from what we paid, not what wins the slot. A 0.5% share at $4.56 says the winning price is well above it. Test: step the price and read impression share daily; if share climbs with price, it was price.')
bullet('**Our own 4-piece in the same auctions.** B4’s deal raised its prices on the shared terms from 15 September, and B6’s share on them fell in the same days. Test: read both listings’ share on the shared terms daily; if B6 rises when B4 steps back, the plan needs one owner per term.')
bullet('**Budget cut-off.** Share is counted over the whole day; a campaign out of budget by evening loses the evening auctions. Test: hours out of budget per campaign; raise budget with the price step where 80%+ is used.')
bullet('**Eligibility and relevance.** Relevance shows as low CTR and CVR, and ours are above the bars — so it remains the check on rows still at zero after two steps (the Cooling terms first).')
lead('Correction for the app.', 'Read top-of-search impression share on every ranking target, every run, beside the effective bid; grade every push on whether share rose. The engine has the field (tosImpressionShare) and does not use it.')

# ---------------------------------------------------------------- D7 competitors
section('Competitors')
riv = _json.load(open(f'{_dg.B}/b6_context.json'))['competitors']['rivals']
rows = []
for r in sorted(riv, key=lambda r: -(r.get('estWeeklySales') or 0))[:12]:
    rows.append([r['brand'][:20], r['tier'], f"${r['price']:.2f}" + (f" (list ${r['listPrice']:.2f})" if r.get('listPrice') else ''), r['rating'], f"{r['reviews']:,}", r['estWeeklySales'], f"{r['bsr']:,}"])
table(['Brand', 'Tier', 'Price', 'Rating', 'Reviews', 'Est. units/wk', 'BSR'], rows, widths=[3.4, 2.2, 3.4, 1.3, 1.8, 1.8, 1.8], size=8)
_cs = A['brief']['sections']['competitors']['summary']
bullet(f"**Prices around us.** The run’s brief watches {_cs['competitorCount']} rivals ({_cs['withHistory']} with history): {_cs['priceRaisers']} raised price, {_cs['priceCutters']} cut, {_cs['onDiscountNow']} are on a strike-through discount now. B6’s six-piece set sits against four-piece rivals on most terms; the offer converts at the top, which is what the bars measure.")
bullet('**Who holds the top of the terms.** On the hero terms the top three ASINs take a third or more of clicks but a small share of conversions: clicks concentrate at the top, purchases do not — the category is won on visibility, and our above-bar CVR at the top means the clicks we buy there convert.')
lead('Correction for the app.', 'Carry each rival’s current price, discount and review count beside the keyword it is the reference for; re-weight the push toward terms where the price gap is widest during a deal; flag rivals without an ASINsight export (their traffic is unmeasured, not zero); add coupon/lightning-deal detection (the brief notes it is not scraped).')

# ---------------------------------------------------------------- D8 more campaign types
section('Campaign types that should also be running')
_bl = A['builds']
lead('What the run proposes.', f"{len(_bl)} builds: " + ', '.join(f"{n} {t}" for t, n in Counter(b['ad_type'] for b in _bl).most_common()) + ". The ones the loader cannot write (Sponsored Brands, video, display) are written as PAUSED rows for a person to build, with nothing that makes that happen; the engine check failed on one of the video probes (R14).")
rows = [[b['ad_type'], b['campaign'].replace('DBS6-', '')[:70], f"${float(b['budget']):.2f}" if b.get('budget') not in (None, 'None') else '—'] for b in _bl]
table(['Type', 'Build', 'Budget/day'], rows, widths=[3.6, 11, 2.4], size=7.5)
lead('What to do.', 'Build the Sponsored Brands headline and video rows on the in-focus terms this week at budgets sized to a readable click count (~50 clicks a week each), and settle the failed engine check on the video probe before it loads; keep own-page display defence separate from ranking campaigns so the ranking mix reads clean.')
lead('Correction for the app.', 'Non-SP builds need a way to load (or a task created for a person with a due date). Budgets on new formats should be sized to a readable click count in the read window.')

# ---------------------------------------------------------------- D9 metrics
section('Metrics the app should be reading')
rows = [
    ['Top-of-search impression share, per target', 'Measured by Amazon; in Command Center; not read by the engine', f'In-focus median {_st.median(_iss):.1f}%; hero terms fell in the last 10 days', 'The direct measure of “are we at the top”; grade every push on it.'],
    ['Required vs delivered top-of-search clicks', 'Run has the requirement; engine does not compare', f'In focus: {_deal:.0f} of {_need:.0f} a day ({_deal / _need * 100:.0f}%)', 'The traffic-gap test; sizes the push.'],
    ['Sibling ASIN on the same keyword', 'Not read', 'B4 and B6 both in focus on Bamboo|Cooling; B4’s deal on the shared hero terms', 'Stops our own listings bidding against each other.'],
    ['Budget hours out', 'Not read', '—', 'Separates price from budget as the cause of low share.'],
    ['Rank response per 100 top-of-search clicks', 'Not computed', 'Bamboo|Queen 18 → 40 as its top-of-search clicks fell', 'Tells the push how much volume a position costs; replaces a fixed step.'],
    ['TACoS and organic sales trend', 'Daily TACoS available', '12% (July) → 6.6% (last 10 days); guard 14.1%', 'The payoff of rank is organic sales; a push that lifts rank should show TACoS falling after it.'],
    ['Brand click and purchase share (SQP)', 'Field present, empty', '—', 'The rank driver itself: our share of the term’s purchases vs the ranks above us.'],
]
table(['Metric', 'Today', 'Value now', 'Why it matters'], rows, widths=[4, 3.6, 4, 5.4], size=7.5)

# ---------------------------------------------------------------- D10 recommendations
section('What to do')
for b in [
    '**From 09-25 (first window to 09-29):** push every in-focus exact ranking campaign on top of search daily by the delivery gap (Part A), inside the loss stop (3× contribution per top-of-search order), the engine-plan envelope ($1,072 a day) and the 14.1% TACoS guard. Read impression share and clicks every morning; share rising with price = keep stepping; share flat after a step = halve the next step and check budget hours out, the child the ad serves and B4’s share on the same term.',
    '**Queen, King, Full:** every one of these terms meets its bars at the top — push, starting with “bamboo sheets queen size” (4 clicks a week against 307) and the King terms that lost the most rank.',
    '**Cooling:** B6 is barely in the auction — step from a floor near the group’s clearing price and treat the first two days as the eligibility check; read B4’s share on the same terms beside it.',
    '**Out of focus:** hold the head term and the flagship flat; freeze the rank collapses; run the +10% test on the converting out-of-focus campaigns for two weeks.',
    '**From 09-30:** terms at their requirement — evaluate cost per click, probing down 3–5% a step; terms short of it — step down to break-even over two writes four days apart, unless the 7-day rank reached the target range (then hold one week and read).',
]:
    bullet(b)
