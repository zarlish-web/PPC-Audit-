# Part D — B6: why rank has not moved. Executed inside build_cat_doc.py's namespace (doc, para, lead, bullet, table, section, part, sec_no, CATS, A).
import statistics as _st
import diag as _dg
from docx.shared import Cm as _Cm

part[0] = 'D'; sec_no[0] = 0
doc.add_page_break()
doc.add_heading('Part D — B6: why rank has not moved, and what to do about it', 1)
para('Erik’s question: across the implementations and tuning so far, rank traction has not come. Is that because we are not driving enough traffic to the top of search (a **traffic gap**), or because we are there and not meeting the target CTR and CVR (a **performance gap**)? This part answers it for B6’s main ranking keywords and syntax groups, and adds the performance-vs-tuning history, competitors, the campaign types that should also be running, and the metrics the app should be reading.')

# ---------------------------------------------------------------- data
PLAN = {k['keyword']: k for k in A['brief']['sections']['targets']['keywords']}
KW4 = _dg.kw_table('b6', plan=PLAN)
GR4 = _dg.group_table('b6')
PLAN = {k['keyword']: k for k in A['brief']['sections']['targets']['keywords']}
INF = [c for c in CATS if c['focus_in']]
_iss = [c['tos_is'] for c in INF if c.get('tos_is') is not None]
_need = sum(c['need_day'] or 0 for c in INF); _deal = sum(c['deal_tos_day'] or 0 for c in INF)
_nd = [(c['deal_tos_day'] or 0) / c['need_day'] for c in INF if c.get('need_day')]


def f1(x, d=1, suf=''):
    return '—' if x is None else f'{x:.{d}f}{suf}'


def rk(r):
    v = list(r['ranks'].values())
    return ' → '.join('—' if x is None else str(x) for x in (v[0], v[2], v[3]))


def verdict_short(v):
    return v.split(' — ')[0].replace('NOT PRESENT at top of search', 'NOT PRESENT').title()


# group-level IS: impression-weighted mean of the member keywords' measured target IS
def group_is(kws, prod):
    ti = _dg.targets_is(prod); k30 = _dg.kw_rows(prod, '30d')
    acc = {}
    for k, t in ti.items():
        r = k30.get(k)
        if not r or t['is_'] is None: continue
        w = r.get('tos_impr') or 0
        a = acc.setdefault(r['syntax'], [0, 0]); a[0] += t['is_'] * w; a[1] += w
    return {g: (a[0] / a[1] if a[1] else None) for g, a in acc.items()}


GIS4 = group_is(KW4, 'b6')

# ---------------------------------------------------------------- D1 answer
section('The answer in one page')
lead('Short answer.', 'For B6 it is a **traffic gap** first, and a traffic gap the tuning made. On B6’s main ranking keywords, top-of-search clicks beat the app’s CTR bar (1.1× market) and CVR bar (3× market) wherever there is enough sample — but B6 wins almost none of the top-of-search auctions, and its ad traffic was cut by two-thirds over the last month. Rank has fallen on every tracked group as the traffic went.')
_wr = [c for c in INF if c.get('need_day')]
bullet(f'**We are rarely at the top.** Amazon’s own top-of-search impression share on B6’s in-focus exact targets has a median of **{_st.median(_iss):.1f}%** ({sum(i < 10 for i in _iss)} of {len(_iss)} under 10%). On “bamboo sheets” it is 2.1% at a $6.10 effective top-of-search bid over 30 days, and 0.5% in the last 8 days while B4 pushed the same term; “bamboo sheets queen size” 0.4% at $4.56; “bamboo sheets king size” 0.6% at $4.80.')
bullet(f'**The volume is a sliver of the plan.** The {len(_wr)} in-focus campaigns that carry a plan keyword need {sum(c["need_day"] for c in _wr):.0f} top-of-search clicks a day between them; over the last 8 days they got **{sum(c["deal_tos_day"] for c in _wr):.0f} a day**. By keyword: “bamboo sheets” needs 483 clicks a week and got 89 at top of search over 30 days (42 a week in the last 8 days); “bamboo sheets queen size” needs 307 and got 9; “bamboo sheets king size” 170 and 4; “bamboo sheets full” 151 and 8; “bamboo cooling sheets” 142 and 1.')
bullet('**When we are there, we perform.** “bamboo sheets” top-of-search CTR 3.0% vs a 1.9% bar, CVR 18.8% vs 8.3%; “queen size” 5.9% / 32.8% vs 1.8% / 13.3%; “viscose bamboo sheets” 4.6% / 23.4%. B6 converts better at the top than B4 on the same head term (18.8% vs 12.7%). The syntax-level estimate shows B6’s King, Queen and Full groups under the 3× CVR bar, but on 5–13 estimated orders from a split, not measured; the keyword rows do not show it (D.4).')
bullet('**The tuning took the traffic away.** Ad clicks fell from 310 a day (late June–July) to 265, 197 and then 101 in the last 8 days; orders from 45 to 13 a day. The 11 September round cut ranking spend in half and top-of-search clicks by a quarter. ACoS improved (29% → 24%) because B6 was buying less. Every tracked group lost rank: Bamboo 21 → 31, Bamboo|King 20 → 28, Bamboo|Queen 18 → 39 (7-day medians, June → 22 Sep).')
bullet('**The plan asks for terms the focus does not push.** B6’s plan asks for 307 clicks a week on “bamboo sheets queen size” and 1,301 a week across ten cooling terms, but Bamboo|Queen and the cooling groups are out of focus. Focus stays as it is (operator decision); instead, the out-of-focus terms that already convert above the bar at the top — 9 Queen, 9 Cooling|King and 5 others — get a two-week test at +10% (section B.1), and the result feeds the next focus decision. Queen stock supports it: 2,879 units across colours (70 days of cover) and 1,884 inbound on 10-30, though the white hero is short (379) — the Queen tests run on the olive child (518).')
bullet('**The one group that got volume moved.** “bamboo sheets full” took impression share from 1.2% to 17.7% in the last 8 days and its rank went 58 → 12 over the summer (organic 19, sponsored 7): price bought share, and share bought rank.')
lead('What changes.', 'Buy the traffic back where it performs: step the top-of-search price every day by the delivery gap, inside the loss stop (3× contribution per top-of-search order) and the spend envelope (Part A). Restore the campaigns the 11 September round took dark. Keep focus as the plan sets it and test the out-of-focus terms that convert. Keep B6’s terms during B4’s deal (operator decision) and read both listings’ share on the shared terms daily.')

# ---------------------------------------------------------------- D2 performance vs tuning
section('Overall performance against the tuning so far')
lead('What happened.', 'Four blocks from the daily product series, and the organic group rank (7-day median) at the start of each block. B6 had no deal in August or September; its last deals were the July Best Deal (31 Jul – 13 Aug) and an August Lightning Deal (16 Aug).')
import json as _json
rows = []
pts = _json.load(open(f'{_dg.B}/b6_daily.json'))['points']
for a, b, wl in (('2026-06-24', '2026-07-23', '24 Jun – 23 Jul'), ('2026-07-24', '2026-08-23', '24 Jul – 23 Aug'), ('2026-08-24', '2026-09-14', '24 Aug – 14 Sep'), ('2026-09-15', '2026-09-22', 'Last 8 days 15 – 22 Sep')):
    r = [x for x in pts if a <= x['date'] <= b]; n = len(r)
    s = lambda k: sum((x.get(k) or 0) for x in r)
    c, o, sp, sa = s('clicks'), s('orders'), s('spend'), s('sales')
    tac = [x['tacos'] for x in r if x.get('tacos')]
    rows.append(['B6' if a == '2026-06-24' else '', wl, f'{c / n:.0f}', f'{o / n:.1f}', f'${sp / n:,.0f}', f'${sa / n:,.0f}', f'{sp / sa * 100:.1f}%', f'{o / c * 100:.1f}%', f'${sp / c:.2f}', f'{sum(tac) / len(tac):.1f}%' if tac else '—'])
table(['Product', 'Window', 'Ad clicks/day', 'Ad orders/day', 'Spend/day', 'Ad sales/day', 'ACoS', 'CVR', 'CPC', 'TACoS (mean of days)'], rows, widths=[1.2, 2.8, 1.6, 1.6, 1.6, 1.7, 1.3, 1.2, 1.2, 1.8], size=7.5)
rows = []
for g in GR4:
    if g['group'].startswith('Size') or g['group'] == 'Organic & Natural' or (g['spend'] or 0) < 100: continue
    rows.append(['B6', g['group'], *['—' if x is None else x for x in g['ranks'].values()], f"${g['spend']:,.0f}"])
table(['Product', 'Syntax group', 'Rank 24 Jun', 'Rank 15 Aug', 'Rank 14 Sep', 'Rank 22 Sep', 'Spend 30d'], rows, widths=[1.2, 4, 2, 2, 2, 2, 2], size=8)
p = f'{_dg.S}/chart_b6.png'
if os.path.exists(p):
    doc.add_picture(p, width=_Cm(16.5)); para('B6 — top-of-search and product-page clicks per day (all campaigns), the spend-weighted effective top-of-search bid, and group rank (daily). Dashed lines: B6’s logged change rounds of 7, 11, 16 and 20 September; shaded: B4’s Best Deal (B6 has no deal).', size=8.5, color=GREY)
lead('B6.', 'B6 lost its volume in two steps. After its own deals ended in mid-August, and then sharply between 26 August and 5 September — ad clicks from about 350 to 114 a day — with no price decision logged in Command Center in that span (the first logged B6 round is 7 September); that drop needs the Amazon console’s change history (budgets, pauses, manual bids) to explain. Listing changes landed in the same weeks (new main image 23 Aug, swatches 26 Aug, secondary images 5 Sep, title and highlights 8 Sep). Then the logged rounds: 7 Sep (21 top-of-search raises, 12 base cuts), 11 Sep (176 price moves on 140 campaigns: 77 top-of-search cuts, 50 raises, 34 base cuts), 16 Sep (92 top-of-search raises) and 20 Sep (23 cuts, 35 raises, 12 base cuts). Product pages were cut from 204 to 60 clicks a day — the right direction — but top-of-search clicks fell with them, from 111 to 44 a day, at an effective top-of-search bid that never moved off about $5. ACoS looks healthy (24–28%) because B6 is buying less; TACoS fell from 12% to 6% because ad sales fell, not because organic sales rose.')
lead('The lesson for the app.', 'A round that improves ACoS or the mix but lowers top-of-search clicks on an in-focus keyword is a rank loss, not a win — the 11 September round did exactly that. Grade every round on top-of-search clicks delivered against the requirement, and on rank, before ACoS.')

# ---------------------------------------------------------------- D3 method
section('How traffic gap and performance gap are told apart')
lead('Performance bars.', 'The app’s own: target CTR = 1.1 × the market CTR of the keyword’s syntax group (Search Query Performance); target CVR = 3 × market CVR. CTR is judged only with 300+ top-of-search impressions, CVR only with 15+ top-of-search clicks — below that the call is “not enough sample”, never a verdict.')
lead('Traffic bars.', 'Three reads, any of which marks a traffic gap: Amazon’s measured top-of-search impression share on the target under 10% (we lose 9 of 10 top-of-search auctions at the effective bid we pay); fewer than 15 top-of-search clicks in 30 days; delivered top-of-search clicks under 70% of the plan’s weekly requirement.')
lead('Verdicts.', '**Traffic gap** — meets the bars when shown, not shown enough → buy the traffic. **Performance gap** — shown enough, under the CTR or CVR bar → fix the offer before buying more. **Both** — fix the offer while probing. **Not present** — under 100 top-of-search impressions in 30 days → eligibility/price first. **On track** — meets both, impression share ≥ 10% → scale while rank moves.')
lead('Caveat.', 'Amazon reports placement per campaign and performance per keyword, never both; the keyword-level top-of-search figures distribute each keyword’s traffic by its campaigns’ measured split (Command Center’s estimate, ± band shown there). Impression share and effective bid are measured per target. Where a keyword runs in one exact campaign — true of most ranking keywords — the split is that campaign’s own.')

# ---------------------------------------------------------------- D4 syntax
section('Syntax groups')
rows = []
for g in sorted(GR4, key=lambda r: -(r['spend'] or 0)):
    if not g['clicks']: continue
    is_ = GIS4.get(g['group'])
    v = _dg.verdict(g['tos_impr'], g['tos_clicks'], g['tos_ctr'], g['tos_cvr'], g['mctr'], g['mcvr'], is_=is_)
    rows.append([g['group'], f"${g['spend']:,.0f} / {g['clicks']:,}", f"{g['tos_clicks']:.0f} ({f1(g['tos_share'], 0)}%)", f"{f1(g['tos_ctr'])} / {f1(v['tctr'])}", f"{f1(g['tos_cvr'])} / {f1(v['tcvr'])}", f1(is_, 1, '%') if is_ is not None else '—',
                 f"{f1(g['tos_cpc'], 2)}", '—' if g['group'].startswith('Size') else ' → '.join('—' if x is None else str(x) for x in g['ranks'].values()), v['verdict']])
doc.add_heading('B6 — 30 days to 22 Sep', 3)
table(['Group', 'Spend / clicks 30d', 'TOS clicks (share)', 'TOS CTR / bar', 'TOS CVR / bar', 'TOS impr. share', 'TOS CPC', 'Rank 24 Jun → 15 Aug → 14 Sep → 22 Sep', 'Verdict'], rows, widths=[2.4, 1.5, 1.8, 1.5, 1.5, 1.3, 1.1, 2.2, 3.4], size=7)
para('Size groups (“Size: King” etc.) are cross-cutting: a keyword is in its primary group and in its size group, so the size rows re-count traffic already shown above. Impression share for a group is the impression-weighted mean of its member targets’ measured share.', size=8.5, color=GREY)
lead('Reading it.', 'The Bamboo group — two-thirds of B6’s spend — meets both bars at top of search at 2–3% impression share: a traffic gap. Bamboo|King, Bamboo|Queen and Bamboo|Full read under the 3× CVR bar at top of search, but that CVR is an estimate from each keyword’s campaigns’ placement split on 5–13 estimated orders, while the same groups convert at 12–16% overall and the keyword rows below convert above the bar; treat it as “verify on the campaign’s own placement report” before any bid goes in, not as a proven performance gap. The cooling groups are barely bought (under $1,000 in 30 days across all of them) — the plan asks for them, the focus does not include them.')

# ---------------------------------------------------------------- D5 keywords
section('The main ranking keywords — one call each')
lead('What the columns say.', 'The main ranking keywords (rank-tracked terms and top spenders with 20+ clicks in 30 days). Plan = the plan’s weekly PPC-click requirement for the keyword (B6 brief). TOS/wk = top-of-search clicks a week over 30 days, and over the last 8 days. IS = Amazon’s top-of-search impression share on the exact target, at the effective top-of-search bid shown. Org / SP = organic and sponsored position (ASINsight, 17 Sep). Rank = our tracked rank (7-day median) 24 Jun → 14 Sep → 22 Sep.')
rows = []
for r in [r for r in KW4 if (r['clicks'] or 0) >= 20][:16]:
    pl = PLAN.get(r['kw'])
    wk = r['tos_clicks'] / 30 * 7
    rows.append([r['kw'][:30], pl['ppc_clicks_target'] if pl and pl.get('ppc_clicks_target') else '—', f"{wk:.0f} / {r['deal_tos_day'] * 7:.0f}",
                 f"{f1(r['tos_ctr'])}/{f1(r['tctr'])}", f"{f1(r['tos_cvr'])}/{f1(r['tcvr'])}", f1(r['is_'], 1, '%') if r['is_'] is not None else '—', f"${r['eff']:.2f}" if r['eff'] else '—',
                 f"{r['org'] or '—'} / {r['sp'] or '—'}", rk(r), verdict_short(r['verdict'])])
table(['Keyword', 'Plan clicks/wk', 'TOS/wk 30d / last 8d', 'CTR / bar', 'CVR / bar', 'IS', 'Eff. TOS bid', 'Org / SP', 'Rank', 'Verdict'], rows, widths=[3.4, 1.2, 1.7, 1.5, 1.6, 1.0, 1.3, 1.3, 2.0, 1.9], size=7)
lead('What to do, by keyword.', '')
for kw, txt in [
    ('bamboo sheets', 'Traffic gap. Converts at 18.8% at the top (bar 8.3%), CTR 3.0% (bar 1.9%). Impression share 2.1% at $6.10 over 30 days, 0.5% in the last 8 days while B4 pushed the same term with a bigger bid; top-of-search clicks fell from 14.4 a day (08-15 → 09-14) to 6.1. Rank 23 → 36 (7-day median). The flagship campaign used 16% of its $250 budget, so the lever is price: the delivery-gap step (9% delivered → +30%) is halved because share fell after the 16 September raise, to $7.01 — about $37 a top-of-search order at its 19.2% conversion, well inside its $16.83 loss stop. It also went quiet after the 11 September base cut ($2.22 → $1.88) — restore that base in the same write. Read share daily beside B4’s on this term.'),
    ('bamboo sheets queen size', 'Traffic gap: 9 clicks a week against the plan’s 307; CVR 32.8% at the top; impression share 0.4% at $4.56; sponsored position 4, organic 36. Bamboo|Queen stays out of focus (operator decision), so there is no full push; its converting campaigns — including the head-term “Bamboo Sheets Queen” (59 orders on 264 top-of-search clicks, 22%) — are in the two-week test on the olive child (section B.1). If the test holds, it is the case for bringing Queen into focus.'),
    ('bamboo sheets king size', 'Traffic gap: 4 a week against 170; 0.6% impression share at $4.80; rank 15 → 36. Its campaign “Bamboo Sheets King Size-(HSV)” went dark after the 11 September round left it at a $0.50 base with an 860% modifier — restore the base and push.'),
    ('bamboo sheets full', 'The proof that price buys rank on B6: impression share 1.2% → 17.7% in the last 8 days at $6.50, rank 58 → 12 over the summer (organic 19, sponsored 7). 18% of its requirement delivered → +30% to $8.46, about $38 a top-of-search order. Keep stepping while share rises.'),
    ('viscose bamboo sheets', 'At its (small) requirement — 8 clicks a week planned, 14 delivered; rank 16 → 12, organic 12. No step; evaluate cost per click from 09-29. Its campaign leaks to product pages; the base cut in A4 applies.'),
    ('bamboo cooling sheets / cooling sheets', 'Not present: 1 top-of-search click a week on “bamboo cooling sheets” against 142 planned; “cooling sheets” (460 planned, organic 78, Bedsure leading at $59.99 against B6’s $89) is barely bought. Cooling stays out of focus; its 90-day ACoS is 40%, over break-even. Nine Cooling|King campaigns that convert above the bar at the top are in the two-week test (section B.1); the head term is not.'),
]:
    bullet(f'**{kw}** — {txt}')

# ---------------------------------------------------------------- D6 why IS is low at the bid
section('Why a $5–7 effective bid wins so little of top-of-search')
lead('What we know.', 'Share at the top is low on almost every B6 target. The exceptions show what moves it: “bamboo sheets full” went from 1.2% to 17.7% and “bamboo sheets with corner straps” sits at 14–19%. Four causes, each with its test:')
bullet('**Price below the top-slot winners.** The engine’s bound on each campaign (its own top-of-search CPC + 15%) is built from what B6 paid, not from what wins the slot. Test: step the price and read impression share daily; if share climbs with price, it was price.')
bullet('**Base cuts left campaigns unable to serve.** The 11 September round cut bases 20–25% on the campaigns that then went dark (e.g. Bamboo Sheets King Size at a $0.50 base behind an 860% modifier). A very low base with a very high modifier serves unevenly; restore the base before stepping.')
bullet('**The 4-piece in the same auctions.** B4 bids on 1,242 of B6’s search terms and raised its prices for its Best Deal; on “bamboo sheets” B4 took 379 top-of-search clicks in the last 8 days to B6’s 48, and B6’s share on the term fell from 2.1% to 0.5%. B6 keeps its terms (operator decision), so both listings are read side by side daily.')
bullet('**Eligibility and relevance.** Low share on a high bid can be relevance, but relevance shows as low CTR and CVR, and B6’s are above the bars. It remains the check on rows still at zero after two steps.')
lead('Correction for the app.', 'Read top-of-search impression share on every ranking target, every run, beside the effective bid. A push that raises the bid is graded on whether share rose.')

# ---------------------------------------------------------------- D7 competitors
section('Competitors')
riv = _json.load(open(f'{_dg.B}/b6_context.json'))['competitors']['rivals']
rows = []
for r in sorted(riv, key=lambda r: -(r.get('estWeeklySales') or 0))[:14]:
    rows.append([r['brand'][:20], r['tier'], f"${r['price']:.2f}" + (f" (list ${r['listPrice']:.2f})" if r.get('listPrice') else ''), r['rating'], f"{r['reviews']:,}", r['estWeeklySales'], f"{r['bsr']:,}"])
table(['Brand', 'Tier', 'Price', 'Rating', 'Reviews', 'Est. units/wk', 'BSR'], rows, widths=[3.4, 2.2, 3.4, 1.3, 1.8, 1.8, 1.8], size=8)
bullet('**Our position.** B6 sells at about $89 (contribution $26.46 at 33.8%) — mid-market: above Bedsure ($59.99, 64,900 reviews) and Hotel Sheets Direct ($79.99), level with BAMBAW ($89.99), below Pure Bamboo ($109.99) and BC Bella Coterie ($129.99). It holds **1.8%** of the traffic tracked across the 12 rivals with an ASINsight export (8.76M); twenty of the 32 mapped rivals have no export.')
bullet('**Prices are rising around us.** 15 of 32 rivals raised price over the last six weeks and 3 cut; 8 are on a strike-through discount now (BAMPURE $94.99 at 7.8% off; ACCURATEX $62.99 at 25.9% off). With no deal of its own, B6’s price gap is narrowing on the rivals that raised — which supports its above-bar CVR at the top.')
bullet('**Who holds the top of the hero terms.** On “bamboo sheets” the top three ASINs take 40% of clicks but only 6.3% of conversions; “queen size” 34% / 9.7%; “king size” 36% / 8.4%. B6’s organic position is 36–37 on all three and its sponsored position 19 on “bamboo sheets” (page 2 of ads) — but 4 on “queen size”, where it is not even in focus.')
lead('Correction for the app.', 'Carry each rival’s current price, discount and review count beside the keyword it is the reference for; flag the 20 rivals without an export (unmeasured, not zero); add coupon/lightning-deal detection.')

# ---------------------------------------------------------------- D8 overlap
section('The 4-piece listing in B6’s auctions')
k4, k6 = _dg.kw_rows('b4', '30d'), _dg.kw_rows('b6', '30d'); d4, d6 = _dg.kw_rows('b4', 'deal'), _dg.kw_rows('b6', 'deal')
both = [k for k in k6 if k in k4 and (k4[k]['spend'] or 0) > 0 and (k6[k]['spend'] or 0) > 0]
rows = []
for k in sorted(both, key=lambda k: -k6[k]['spend']):
    if k.startswith('b0') or 'decolure' in k: continue
    a = k6[k]; b_ = k4[k]
    rows.append([k[:30], f"${a['spend']:,.0f}", f"{a['cvr']:.1f}%", f"{a['acos']:.0f}%" if a['acos'] else '—', f"{b_['cvr']:.1f}%", f"{(d6.get(k) or {}).get('tos_clicks') or 0:.0f}", f"{(d4.get(k) or {}).get('tos_clicks') or 0:.0f}"])
    if len(rows) == 10: break
table(['Keyword', 'B6 spend 30d', 'B6 CVR', 'B6 ACoS', 'B4 CVR', 'B6 TOS clicks last 8d', 'B4 TOS clicks last 8d'], rows, widths=[4.0, 1.8, 1.4, 1.4, 1.4, 2.4, 2.4], size=8)
lead('What is happening.', f'{len(both):,} of B6’s search terms are also bought by the Decolure 4-piece — ${sum(k6[k]["spend"] for k in both):,.0f} of B6’s 30-day keyword spend (87%). Neither run knows about the other. During B4’s Best Deal, B4 raised its prices on the shared terms and B6’s top-of-search clicks on them fell.')
lead('Decision.', 'B6 keeps its terms (operator 2026-09-23): no top-of-search cut on the shared terms. B4’s document is left as it is. Read both listings’ impression share on the shared hero terms daily: if both fall when both push, each is taking the other’s auctions.')
lead('Correction for the app.', 'Before writing a bid, check whether another of the brand’s ASINs is bidding on the same keyword, and carry an owner per keyword in the plan.')

# ---------------------------------------------------------------- D9 more campaign types
section('Campaign types that should also be running')
lead('What is already running, and what the run proposes.', 'B6 already runs 26 enabled Sponsored Brands / Sponsored Brands Video campaigns: $2,104 of spend in 30 days at 25.4% ACoS, inside break-even (33.8%). The run proposes 10 builds: 6 Sponsored Products exact coverage/tail rows (loadable) and 4 the loader cannot write — a Sponsored Brands headline and a video probe on “bamboo sheets”, Sponsored Display own-page defence and a product-targeting conquest campaign — marked PAUSED for a person to build, with nothing that makes that happen.')
rows = [
    ['Sponsored Brands headline — exact on the hero terms', 'Build 1934 (“bamboo sheets”, “viscose bamboo sheets”, $7.30/day); existing SB campaigns', 'SB already pays for itself on B6 (25% ACoS). A headline on the hero terms adds a top-of-page surface in a separate auction from SP, where B6 wins 2% of the slot.', 'Build 1934 this week at a budget sized to ~100 clicks a week; point the existing SB headline at the in-focus terms.'],
    ['Sponsored Brands Video — exact', 'Build 1942 (“bamboo sheets”, $10.55/day)', 'B6 has live SBV that performs; a 6-piece set sells on the extra pillowcases and deep pockets, which video shows.', 'Build as a 100-click probe.'],
    ['Sponsored Display — own-page defence', 'Build 1950 (our own ASINs)', 'Product pages still take 47% of out-of-focus ranking clicks; rivals’ ads on our pages take shoppers away.', 'Build; keep separate from ranking campaigns.'],
    ['SP product targeting — conquest', 'Build 1958 (rival ASINs, $22.29/day)', 'Rivals are raising prices (15 of 32); B6 at $89 converts above the bar. Target rivals priced above B6 with rating ≤ B6’s (Pure Bamboo $109.99, BC Bella Coterie $129.99, BAMPURE $94.99).', 'Build; own campaign, own ceiling (contribution × its CVR).'],
    ['Queen and cooling — out of focus, converting', 'Not in the run', '“bamboo sheets queen size” (307 clicks/wk planned, CVR 32.8%) and the cooling terms (1,301/wk planned) have no in-focus campaign; 23 out-of-focus campaigns convert above the bar.', 'Two-week +10% test on the converters (B.1); decide focus on the 10-07 read.'],
    ['SP phrase discovery on the hero roots', 'Not in the run', 'Finds converting variants to promote to exact.', 'One phrase campaign per in-focus root, low base, 0% top of search, harvest weekly.'],
]
table(['Type', 'In the run', 'Why, from the data', 'What to do'], rows, widths=[3.4, 3.8, 5.4, 4.4], size=7.5)
lead('Correction for the app.', 'Non-SP builds need a way to load (or a task created for a person with a due date). Budgets on new formats should be sized to a readable click count in the read window.')

# ---------------------------------------------------------------- D10 metrics
section('Metrics the app should be reading')
rows = [
    ['Top-of-search impression share, per target', 'In Command Center; not read by the engine', f'B6 median {_st.median(_iss):.1f}%; “bamboo sheets” 2.1% → 0.5%', 'The direct measure of “are we at the top”; grade every push on it.'],
    ['Required vs delivered top-of-search clicks', 'Plan has the requirement per keyword; the run does not carry it per campaign', f'{sum(c["deal_tos_day"] for c in _wr):.0f} of {sum(c["need_day"] for c in _wr):.0f} a day', 'The traffic-gap test; sizes the push.'],
    ['Plan terms with no in-focus campaign', 'Not checked', 'Queen 307/wk, cooling 1,301/wk', 'A requirement nothing is pushing is a plan error or a focus error.'],
    ['Sibling ASIN on the same keyword', 'Not read', '1,242 terms shared with the 4-piece, 87% of B6’s spend', 'Stops our own listings bidding against each other unknowingly.'],
    ['Changes made outside the app', 'Not read', 'Ad clicks 350 → 114 a day, 26 Aug – 5 Sep, no logged decision', 'A drop with no logged cause cannot be graded or reversed.'],
    ['Sponsored rank and organic rank per term', 'ASINsight has it; not used', '“bamboo sheets” SP 19, organic 36; “queen size” SP 4', 'Shows where the ad actually sits.'],
    ['Brand click and purchase share (SQP)', 'Field present, empty', '—', 'The rank driver itself.'],
    ['TACoS and organic sales trend', 'Daily TACoS available', '12% → 6% (ad sales falling)', 'Falling TACoS with falling rank is lost volume, not efficiency.'],
]
table(['Metric', 'Today', 'Value now', 'Why it matters'], rows, widths=[4, 3.6, 4, 5.4], size=7.5)

# ---------------------------------------------------------------- D11 recommendations
section('What to do')
for b in [
    '**From 09-24:** push every in-focus exact ranking campaign on top of search daily by the delivery gap (Part A), inside the loss stop (3× contribution per top-of-search order) and the envelope; restore the bases the 11 September round cut on the campaigns that went dark, in the same write. Read impression share and clicks every morning; share flat after a step = halve the next step and check the base, the 4-piece on the same term, and eligibility.',
    '**Hero terms:** “bamboo sheets” (flagship, +15% to $7.01 with its pre-cut base restored), “bamboo sheets full” (+30% to $8.46 — the term already proving that share buys rank), “bamboo sheets king size” (restore, then push). Budget is not the constraint on B6 — the flagship uses 16% of its budget.',
    '**Out of focus, converting:** focus stays as planned; test the 23 out-of-focus campaigns that convert above the bar at +10% for two weeks (Queen on the olive child, 1,884 Queen units landing 10-30), read on 10-07, and take that read into the next focus decision.',
    '**Find the late-August drop:** pull the Amazon console change history for 26 Aug – 5 Sep (budgets, pauses, manual bids) — ad clicks fell by two-thirds with no logged decision.',
    '**Shared terms with B4:** B6 keeps them; read both listings’ share daily.',
    '**New formats:** build the SB headline, SBV probe, SD defence and conquest this week at readable budgets; extend the SB that already pays for itself.',
    '**From 09-29:** terms at their requirement — evaluate cost per click, probing down 3–5% a step; terms short of it — step down to break-even over two writes four days apart, unless the 7-day rank reached the target range (then hold one week and read).',
]:
    bullet(b)
