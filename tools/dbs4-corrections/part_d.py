# Part D — B4 and B6: why rank has not moved. Executed inside build_cat_doc.py's namespace (doc, para, lead, bullet, table, section, part, sec_no, CATS, A).
import statistics as _st
import diag as _dg
from docx.shared import Cm as _Cm

part[0] = 'D'; sec_no[0] = 0
doc.add_page_break()
doc.add_heading('Part D — B4 and B6: why rank has not moved, and what to do about it', 1)
para('Erik’s question: across the implementations and tuning so far, rank traction has not come. Is that because we are not driving enough traffic to the top of search (a **traffic gap**), or because we are there and not meeting the target CTR and CVR (a **performance gap**)? This part answers it for the main ranking keywords and syntax groups of both products — B4 (Bamboo Sheets 4-Piece, product 59) and B6 (Bamboo Sheets 6-Piece, product 30) — and adds what else should be running, the competitors, and the metrics the app should be reading.')

# ---------------------------------------------------------------- data
PLAN = {k['keyword']: k for k in A['brief']['sections']['targets']['keywords']}
KW4, KW6 = _dg.kw_table('b4', plan=PLAN), _dg.kw_table('b6')
GR4, GR6 = _dg.group_table('b4'), _dg.group_table('b6')
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


GIS4, GIS6 = group_is(KW4, 'b4'), group_is(KW6, 'b6')

# ---------------------------------------------------------------- D1 answer
section('The answer in one page')
lead('Short answer.', 'It is overwhelmingly a **traffic gap**. On the main ranking keywords of both products, top-of-search clicks beat the app’s own CTR bar (1.1× market CTR) and CVR bar (3× market CVR) wherever there is enough sample to judge — but we win only a sliver of the top-of-search auctions at the effective bids we pay, so the volume the plan needs never arrives. Rank cannot move on clicks that are not bought.')
bullet(f'**We are rarely at the top.** Amazon’s own top-of-search impression share on B4’s in-focus exact targets has a median of **{_st.median(_iss):.1f}%** ({sum(i < 10 for i in _iss)} of {len(_iss)} under 10%) — i.e. we lose more than nine top-of-search auctions in ten. On “bamboo sheets” it is 3.2% at a $7.42 effective top-of-search bid (B4) and 2.1% at $6.10 (B6); on “bamboo sheets queen size” 2.8% (B4) and 0.4% (B6); on “bamboo sheets king size” 0.6% on both.')
bullet(f'**The volume is a tenth of the plan.** The run’s own click requirements for the in-focus B4 campaigns add to {_need:.0f} top-of-search clicks a day; in the Best Deal they are getting **{_deal:.0f} a day ({_deal / _need * 100:.0f}%)**. The median campaign is at {_st.median(_nd) * 100:.0f}% of its own requirement; {sum(x >= 1 for x in _nd)} of {len(_nd)} are at or above it. By keyword: “bamboo sheets” needs 490 clicks a week and gets 218 at top of search (331 in the deal); “bamboo sheets queen size” needs 248 and gets 22; “bamboo sheets king size” needs 298 and gets 16; “cooling sheets” needs 232 and gets 23 (the brief’s per-keyword figures; the run’s campaign requirement for the flagship is 1,285 a week, 2.6× the brief’s 490 for the same keyword — the app should carry one number).')
bullet('**When we are there, we perform.** B4 at top of search: “bamboo sheets” CTR 3.4% vs a 1.9% bar, CVR 12.7% vs 8.3%; “queen size” 3.2% / 27% vs 1.8% / 13%; “king size” 6.7% / 16.5% vs 1.9% / 10.8%. B6 is the same shape (“bamboo sheets” 3.0% / 18.8%). A performance problem would show as sub-bar CTR or CVR on a decent sample; it doesn’t.')
bullet('**The real performance gap is narrow:** “cooling sheets” (B4 CVR 7.1% vs an 8.7% bar, ACoS 78%, rank flat at 55) and the cooling family generally, where the product is not the category’s natural answer and Bedsure sells at $59.99 with 64,900 reviews. More bid there buys more of the same shortfall.')
bullet('**The tuning worked against rank.** From July to the week before the deal the tuning took B4’s ad clicks from 401 to 235 a day and B6’s from 310 to 197 (and to 101 during B4’s deal). It optimised ACoS and the placement mix, and it did — B6’s ACoS fell from 29% to 24% — but rank follows the volume of converting clicks, and volume went the other way. B6’s group ranks slid (Bamboo 21 → 31, King 20 → 35, Queen 18 → 41) as its traffic was taken away.')
bullet('**B4 and B6 bid against each other.** 1,242 search terms are bought by both products; they carry 81% of B4’s and 87% of B6’s keyword spend. Amazon shows one ad per advertiser in an auction, so the two ASINs dilute each other’s top-of-search share. In the deal B4 took 379 top-of-search clicks on “bamboo sheets” and B6 48 — B6’s fell as B4’s rose.')
lead('What changes.', 'Buy the traffic where it performs (most in-focus terms): step the top-of-search price by rank gap every day of the deal, lift budgets where they cap, and watch top-of-search impression share rise with it — that is the proof the price is working. Where impression share does not respond to price, the constraint is not price (budget cut-off, a sibling ASIN winning the auction, or eligibility) and the fix is there. Hold price and fix the offer only on the terms with a genuine CTR/CVR shortfall. Give each shared keyword one owner between B4 and B6. Details and the per-keyword call follow.')

# ---------------------------------------------------------------- D2 performance vs tuning
section('Overall performance against the tuning so far')
lead('What happened.', 'Four 30-day-ish blocks from the daily product series, and the organic group rank at the start of each block. The deal is B4’s Best Deal (09-15 → 09-28); B6 had no deal in September.')
import json as _json
rows = []
for prod, lab in (('b4', 'B4'), ('b6', 'B6')):
    pts = _json.load(open(f'{_dg.B}/{prod}_daily.json'))['points']
    for a, b, wl in (('2026-06-24', '2026-07-23', '24 Jun – 23 Jul'), ('2026-07-24', '2026-08-23', '24 Jul – 23 Aug'), ('2026-08-24', '2026-09-14', '24 Aug – 14 Sep'), ('2026-09-15', '2026-09-22', 'Deal 15 – 22 Sep')):
        r = [x for x in pts if a <= x['date'] <= b]; n = len(r)
        s = lambda k: sum((x.get(k) or 0) for x in r)
        c, o, sp, sa = s('clicks'), s('orders'), s('spend'), s('sales')
        tac = [x['tacos'] for x in r if x.get('tacos')]
        rows.append([lab if a == '2026-06-24' else '', wl, f'{c / n:.0f}', f'{o / n:.1f}', f'${sp / n:,.0f}', f'${sa / n:,.0f}', f'{sp / sa * 100:.1f}%', f'{o / c * 100:.1f}%', f'${sp / c:.2f}', f'{sum(tac) / len(tac):.1f}%' if tac else '—'])
table(['Product', 'Window', 'Ad clicks/day', 'Ad orders/day', 'Spend/day', 'Ad sales/day', 'ACoS', 'CVR', 'CPC', 'TACoS (mean of days)'], rows, widths=[1.2, 2.8, 1.6, 1.6, 1.6, 1.7, 1.3, 1.2, 1.2, 1.8], size=7.5)
rows = []
for prod, lab, G in (('b4', 'B4', GR4), ('b6', 'B6', GR6)):
    for g in G:
        if g['group'].startswith('Size') or g['group'] == 'Organic & Natural' or (g['spend'] or 0) < 150: continue
        v = list(g['ranks'].values())
        rows.append([lab, g['group'], *['—' if x is None else x for x in v], f"${g['spend']:,.0f}"])
table(['Product', 'Syntax group', 'Rank 24 Jun', 'Rank 15 Aug', 'Rank 14 Sep', 'Rank 22 Sep', 'Spend 30d'], rows, widths=[1.2, 4, 2, 2, 2, 2, 2], size=8)
for prod, lab, cap in (('b4', 'B4', 'B4 — top of search and product-page clicks per day (all campaigns), the spend-weighted effective top-of-search bid, and group rank. Dashed lines: the change rounds of 24 Aug, 10 Sep, 15/16 Sep and 22 Sep; shaded: the Best Deal.'),
                       ('b6', 'B6', 'B6 — the same three panels. Dashed lines: B6’s logged change rounds (7, 11, 16, 20 Sep); shaded: B4’s Best Deal (B6 has no deal).')):
    p = f'{_dg.S}/data/chart_{prod}.png' if os.path.exists(f'{_dg.S}/data/chart_{prod}.png') else f'{_dg.S}/chart_{prod}.png'
    if os.path.exists(p):
        doc.add_picture(p, width=_Cm(16.5)); para(cap, size=8.5, color=GREY)
lead('B4.', 'Through August and early September every round took volume out: ad clicks fell from 401 a day (late June/July) to 328 and then 235, orders from 46 a day to 28. The placement mix moved the right way (top of search from 26% to 37% of all clicks), but top-of-search clicks themselves fell from 97 to 84 a day — the mix improved because product pages were cut harder than top of search grew. Rank drifted: Bamboo 31 → 35, Bamboo|Queen 32 → 42. The deal round (15/16 Sep) is the first that bought volume: the effective top-of-search bid rose from $4.30 to $5.51, top-of-search clicks from 84 to 150 a day — and the one group given real top-of-search volume moved: Bamboo|King went 35 → 22 inside the deal (28 on the 22nd). Bamboo (38) and Bamboo|Queen (45) did not, and those are the ones still at 3% and under 1–3% impression share.')
lead('B6.', 'B6 lost its volume in two steps. First, after its own deals ended (July Best Deal 31 Jul–13 Aug, August Lightning 16 Aug), and then sharply between 26 August and 5 September — ad clicks from ~350 to 114 a day — with no price decision logged in Command Center in that span (the first logged B6 round is 7 September); that drop needs the Amazon console’s change history (budgets, pauses, manual bids) to explain. Then the logged rounds: 7 Sep (21 top-of-search raises, 12 base cuts), 11 Sep (176 price moves on 140 campaigns: 77 top-of-search cuts, 50 raises, 34 base cuts), 16 Sep (92 top-of-search raises) and 20 Sep (23 cuts, 35 raises, 12 base cuts). Around the 11 Sep round B6’s top-of-search clicks went from 55 to 44 a day; around 20 Sep they stayed near 40. Overall: ad clicks 310 → 265 → 197 a day, then 101 during B4’s deal; orders 45 → 13 a day. Product pages were cut from 204 to 60 clicks a day, which is the right direction, but top-of-search clicks fell too, from 111 to 44 a day, at an effective top-of-search bid that never moved off ~$5. ACoS looks healthy (24–28%) because it is buying less; every tracked group lost rank (Bamboo 21 → 31, Bamboo|King 20 → 35, Bamboo|Queen 18 → 41). B6 is the clearest case that efficiency tuning without volume costs rank.')
lead('The lesson for the app.', 'A round that improves ACoS or the mix but lowers top-of-search clicks on an in-focus keyword is a rank loss, not a win. Grade every round on top-of-search clicks delivered against the requirement, and on rank, before ACoS.')

# ---------------------------------------------------------------- D3 method
section('How traffic gap and performance gap are told apart')
lead('Performance bars.', 'The app’s own: target CTR = 1.1 × the market CTR of the keyword’s syntax group (Search Query Performance); target CVR = 3 × market CVR. CTR is judged only with 300+ top-of-search impressions, CVR only with 15+ top-of-search clicks — below that the call is “not enough sample”, never a verdict.')
lead('Traffic bars.', 'Three reads, any of which marks a traffic gap: Amazon’s measured top-of-search impression share on the target under 10% (we lose 9 of 10 top-of-search auctions at the effective bid we pay); fewer than 15 top-of-search clicks in 30 days; delivered top-of-search clicks under 70% of the plan’s weekly requirement.')
lead('Verdicts.', '**Traffic gap** — meets the bars when shown, not shown enough → buy the traffic. **Performance gap** — shown enough, under the CTR or CVR bar → fix the offer before buying more. **Both** — fix the offer while probing. **Not present** — under 100 top-of-search impressions in 30 days → eligibility/price first. **On track** — meets both, impression share ≥ 10% → scale while rank moves.')
lead('Caveat.', 'Amazon reports placement per campaign and performance per keyword, never both; the keyword-level top-of-search figures distribute each keyword’s traffic by its campaigns’ measured split (Command Center’s estimate, ± band shown there). Impression share and effective bid are measured per target. Where a keyword runs in one exact campaign — true of most ranking keywords — the split is that campaign’s own.')

# ---------------------------------------------------------------- D4 syntax
section('Syntax groups — B4 and B6')
for prod, lab, G, GIS in (('b4', 'B4', GR4, GIS4), ('b6', 'B6', GR6, GIS6)):
    rows = []
    for g in sorted(G, key=lambda r: -(r['spend'] or 0)):
        if g['group'] == 'Organic & Natural' or (g['clicks'] or 0) < 20: continue
        is_ = GIS.get(g['group'])
        v = _dg.verdict(g['tos_impr'], g['tos_clicks'], g['tos_ctr'], g['tos_cvr'], g['mctr'], g['mcvr'], is_=is_)
        rows.append([g['group'], f"${g['spend']:,.0f}", f"{g['tos_clicks']:.0f} ({f1(g['tos_share'], 0)}%)", f"{f1(g['tos_ctr'])} / {f1(v['tctr'])}", f"{f1(g['tos_cvr'])} / {f1(v['tcvr'])}", f1(is_, 1, '%') if is_ is not None else '—',
                     f"{f1(g['tos_cpc'], 2)}", '—' if g['group'].startswith('Size') else rk(g), verdict_short(v['verdict'])])
    doc.add_heading(f'{lab} — 30 days to 22 Sep', 3)
    table(['Group', 'Spend', 'TOS clicks (share)', 'TOS CTR / bar', 'TOS CVR / bar', 'TOS impr. share', 'TOS CPC', 'Rank 24 Jun → 14 Sep → 22 Sep', 'Verdict'], rows, widths=[3, 1.4, 2, 1.7, 1.7, 1.5, 1.2, 2.4, 2.2], size=7)
para('Size groups (“Size: King” etc.) are cross-cutting: a keyword is in its primary group and in its size group, so the size rows re-count traffic already shown above. Impression share for a group is the impression-weighted mean of its member targets’ measured share.', size=8.5, color=GREY)
lead('Reading it.', 'B4: every Bamboo group meets its CTR and CVR bars at top of search and sits at low single-digit impression share — traffic gap. Cooling is the exception on CVR. B6: the Bamboo group itself meets the bars; the estimated CVR on Bamboo|King, Bamboo|Queen and Bamboo|Full sits under the 3× bar on small top-of-search samples (9, 13 and 5 orders), while the same groups’ overall CVR is 12–16%. Treat that as “verify at the campaign” rather than a proven performance gap: the split behind it is estimated, and the per-keyword rows (next) show the main B6 terms converting above the bar.')

# ---------------------------------------------------------------- D5 keywords
section('The main ranking keywords — one call each')
lead('What the columns say.', 'Plan = the plan’s weekly PPC-click requirement for the keyword (B4 brief). TOS/wk = top-of-search clicks a week over 30 days, and in the deal. IS = Amazon’s top-of-search impression share on the exact target, at the effective top-of-search bid shown. Org / SP = organic and sponsored position (ASINsight, 17 Sep). Rank = our tracked rank 24 Jun → 14 Sep → 22 Sep.')
for prod, lab, KW in (('b4', 'B4', KW4), ('b6', 'B6', KW6)):
    rows = []
    for r in KW[:24]:
        if (r['clicks'] or 0) < 10: continue
        pl = PLAN.get(r['kw']) if prod == 'b4' else None
        wk = r['tos_clicks'] / 30 * 7
        rows.append([r['kw'][:30], pl['ppc_clicks_target'] if pl else '—', f"{wk:.0f} / {r['deal_tos_day'] * 7:.0f}",
                     f"{f1(r['tos_ctr'])}/{f1(r['tctr'])}", f"{f1(r['tos_cvr'])}/{f1(r['tcvr'])}", f1(r['is_'], 1, '%') if r['is_'] is not None else '—', f"${r['eff']:.2f}" if r['eff'] else '—',
                     f"{r['org'] or '—'} / {r['sp'] or '—'}", rk(r), verdict_short(r['verdict'])])
    doc.add_heading(f'{lab}', 3)
    table(['Keyword', 'Plan clicks/wk', 'TOS/wk 30d / deal', 'CTR / bar', 'CVR / bar', 'IS', 'Eff. TOS bid', 'Org / SP', 'Rank', 'Verdict'], rows, widths=[3.4, 1.2, 1.7, 1.5, 1.6, 1.0, 1.3, 1.3, 2.0, 1.9], size=7)
lead('B4 — what to do, by keyword.', '')
for kw, txt in [
    ('bamboo sheets', 'Traffic gap. Converts at 12.7% at the top (bar 8.3%), CTR 3.4% (bar 1.9%); 3.2% impression share at $7.42 and a budget used at 127% over the last 7 days. The deal doubled its top-of-search clicks (25 → 47 a day) and rank has not answered yet (32 → 41): 331 a week is still two-thirds of the 490 the plan needs. Raise the budget with the top-of-search step (it caps before the day ends — impression share counts the hours we are out), step the price +30% a day while impression share rises with it; this is also the term B6 contests (D8).'),
    ('bamboo sheets queen size', 'Traffic gap, the widest: 22 clicks a week against 248; CVR 27% at the top. Impression share 2.8% at $6.69 — and this campaign is on dynamic up-and-down bidding, which paid $11.99 a top-of-search click in the deal on a written $6.69 (A-section). Switch to fixed bids and step the price; budget is at 102%, lift it with the step.'),
    ('bamboo sheets king size', 'Traffic gap: 16 a week against 298, 0.6% impression share at $4.96 — the lowest effective bid of the three hero terms and the lowest share. Organic 15, sponsored 19. Step +30% a day; this is the cheapest volume on the list because CVR (16.5%) is well above the bar.'),
    ('cooling sheets', 'Performance gap on CVR (7.1% vs 8.7%) with ACoS 78% and rank flat at 55; 76% of our traffic on this term is paid. Do not add bid. The Cooling group’s market limit is the lowest in the product ($3.61) because the term converts poorly for us. Fix the offer for this query first (cooling claim in the first image and title, price against Bedsure’s $59.99) and re-test on a small probe; keep “bamboo cooling sheets”, which meets both bars, as the cooling entry point.'),
    ('bamboo sheets queen', 'Not present: 3 top-of-search clicks in 30 days, impression share 0% at $3.75 — the price is below anything that wins the top. Rank fell 29 → 71. Eligibility and price: this row needs the rank-gap step from a floor near the group’s clearing price ($6.39), not +30% of $3.75.'),
    ('queen bamboo sheet set', 'Not present: 0.1% impression share at $3.80. Same fix — reset the top-of-search price to the group clearing level, then step.'),
    ('king size bamboo sheets set', 'One of the few targets above 10% impression share (15% at $9.33 effective); 3.4 top-of-search clicks a day in the deal, CVR 26% at the top. Proof that price buys share on this account: keep stepping.'),
]:
    bullet(f'**{kw}** — {txt}')
lead('B6 — what to do.', 'B6 is out of focus for B4’s deal but it is a product in its own right with a rank that has fallen on every group. Its main terms (“bamboo sheets”, “viscose bamboo sheets”, “bamboo sheets queen size”, “king size bamboo sheets set”) meet the CTR and CVR bars at 0.4–7% impression share: a traffic gap, made worse by B6 being cut while B4 pushes the same terms. Decide the owner per term (D8); on the terms B6 keeps, restore top-of-search volume to the pre-cut level (111 a day in late August) at the pre-cut prices and grade it on rank, not ACoS. The B6 “Bamboo|King/Queen/Full” CVR shortfall is to be verified at campaign level before any bid goes into those groups.')

# ---------------------------------------------------------------- D6 why IS is low at the bid
section('Why a $5–7 effective bid wins only 1–5% of top-of-search')
lead('What we know.', 'Impression share at the top is low on almost every target, and among the hero-family targets the highest share (15%) sits on the highest effective bid ($9.33). The deal gives a first read on whether price moves it: after the 15 September raise (flagship modifier 216% → 299%), share on “bamboo sheets” went from 3.2% (30 days) to 5.5% (deal days), “bamboo sheets queen size” 2.8% → 4.1%, “king size bamboo sheets set” 15.1% → 19.7%, “king cooling sheets” 2.2% → 4.0%; across 57 B4 targets with both reads, 34 rose. Share does respond to price — it has not been given enough of it. Where it did not move (“bamboo sheets king size” 0.6% → 0.3% at $4.96; “bamboo sheets queen” 0.05% at $3.75) the price was not raised or is far below the slot. Four causes, each with its test:')
bullet('**Price below the top-slot winners.** The group “market limit” the engine uses (clearing price + 15%: Bamboo $6.32, King $6.47, Queen $6.39) is built from what we paid, not what wins the slot. A 3% share at $7.42 says the winning price is above it. Test: step the price and read impression share daily; if share climbs with price, it was price.')
bullet('**Budget cut-off.** Share is counted over the whole day. The flagship campaign used 127% of its budget in the last 7 days, Queen Size 102%, and six other in-focus campaigns are over 80% — they leave the auction before evening. Test: hours-out-of-budget per campaign (Amazon reports it); raise budget with the price step.')
bullet('**Our own second ASIN.** B4 and B6 enter the same auctions on 1,242 terms; Amazon serves one ad per advertiser per auction, so B6’s presence takes share from B4 and vice versa. Test: on the owner/non-owner split (D8), the owner’s share should rise when the other steps back.')
bullet('**Eligibility and relevance.** The Command Center note is right that low share on a high bid can be relevance — but relevance shows up as low CTR and CVR, and ours are above the bars. So this cause is least likely on the hero terms; it remains the check on rows still at zero after two steps (A-section daily read).')
lead('Correction for the app.', 'Read top-of-search impression share on every ranking target, every run, beside the effective bid. A push that raises the bid is graded on whether share rose. The engine currently has the field (tosImpressionShare) and does not use it.')

# ---------------------------------------------------------------- D7 competitors
section('Competitors')
riv = _json.load(open(f'{_dg.B}/b6_context.json'))['competitors']['rivals']
rows = []
for r in sorted(riv, key=lambda r: -(r.get('estWeeklySales') or 0))[:14]:
    rows.append([r['brand'][:20], r['tier'], f"${r['price']:.2f}" + (f" (list ${r['listPrice']:.2f})" if r.get('listPrice') else ''), r['rating'], f"{r['reviews']:,}", r['estWeeklySales'], f"{r['bsr']:,}"])
table(['Brand', 'Tier', 'Price', 'Rating', 'Reviews', 'Est. units/wk', 'BSR'], rows, widths=[3.4, 2.2, 3.4, 1.3, 1.8, 1.8, 1.8], size=8)
bullet('**Our position.** B4 sells at about $74 (contribution $25.06 at 33.9%), B6 at $89. We hold **1.7% (B4) and 1.8% (B6)** of the traffic tracked across the 12 rivals with an ASINsight export (8.76M) — Pure Bamboo and Bedsure alone hold 5.2M. Twenty of the 32 mapped rivals have no export, so this is a share of the measured part of the market only.')
bullet('**Prices are rising around us.** Of the 32 rivals watched in B4’s brief, 15 raised price over the last six weeks and 3 cut; 8 are on a strike-through discount now (BAMPURE $94.99 with a 7.8% discount; ACCURATEX $62.99 at 25.9% off). Hotel Sheets Direct went $54.99 → $69.99, Bedsure $64.79 → $74.54. A Best Deal price into a rising market widens our price gap in our favour — that is why CVR is above the bar at the top and why this is the window to buy volume.')
bullet('**Who holds the top of the hero terms.** On “bamboo sheets” the top three ASINs take 40% of clicks but only 6.3% of conversions; on “queen size” 34% / 9.7%; “king size” 36% / 8.4%. Clicks concentrate at the top, purchases do not — the category is won on visibility, and our above-bar CVR means the clicks we buy at the top convert better than the leaders’. Our sponsored position on “bamboo sheets” is 18–19 (page 2 of ads) and organic 32–36.')
bullet('**The plan’s reference rivals per term** are BAMBAW (“bamboo sheets”, “queen size”, cooling; $89.99, 4.3★, 2,672 reviews), BC Bella Coterie (“king size”; $129.99), Sonoro Kate (deep-pocket and viscose terms; $59.99–$79.99) and Bedsure (cooling king/full). All but Sonoro Kate price above B4’s deal price.')
lead('Correction for the app.', 'Carry each rival’s current price, discount and review count beside the keyword it is the reference for; re-weight the push toward terms where our price gap is widest during a deal; flag the 20 rivals without an export (their traffic is unmeasured, not zero); add coupon/lightning-deal detection (the brief notes it is not scraped).')

# ---------------------------------------------------------------- D8 overlap
section('B4 and B6 compete with each other')
k4, k6 = _dg.kw_rows('b4', '30d'), _dg.kw_rows('b6', '30d'); d4, d6 = _dg.kw_rows('b4', 'deal'), _dg.kw_rows('b6', 'deal')
both = [k for k in k4 if k in k6 and (k4[k]['spend'] or 0) > 0 and (k6[k]['spend'] or 0) > 0]
rows = []
for k in sorted(both, key=lambda k: -(k4[k]['spend'] + k6[k]['spend'])):
    if k.startswith('b0') or 'decolure' in k: continue
    a, b = k4[k], k6[k]
    rows.append([k[:30], f"${a['spend']:,.0f}", f"{a['cvr']:.1f}%", f"{a['acos']:.0f}%" if a['acos'] else '—', f"${b['spend']:,.0f}", f"{b['cvr']:.1f}%", f"{b['acos']:.0f}%" if b['acos'] else '—',
                 f"{(d4.get(k) or {}).get('tos_clicks') or 0:.0f} / {(d6.get(k) or {}).get('tos_clicks') or 0:.0f}"])
    if len(rows) == 12: break
table(['Keyword', 'B4 spend', 'B4 CVR', 'B4 ACoS', 'B6 spend', 'B6 CVR', 'B6 ACoS', 'Deal TOS clicks B4 / B6'], rows, widths=[3.8, 1.6, 1.4, 1.4, 1.6, 1.4, 1.4, 2.6], size=8)
lead('What is happening.', f'{len(both):,} search terms are bought by both products (B4 ${sum(k4[k]["spend"] for k in both):,.0f} and B6 ${sum(k6[k]["spend"] for k in both):,.0f} in 30 days — 81% and 87% of their keyword spend). Neither plan knows about the other; each run prices its product as if the other were not in the auction.')
lead('Correction.', 'One owner per shared ranking keyword, decided on the rank plan, not on ACoS: during B4’s deal B4 owns the generic and size-level Bamboo terms it is ranking (“bamboo sheets”, “… queen size”, “… king size”, “bamboo cooling sheets”); B6 keeps the terms where it ranks better or B4 is not pushing (“viscose bamboo sheets” org 12, “bamboo sheets with corner straps” org 11, “full bamboo sheets” org 12, “king size bamboo sheets set” SP 4). The non-owner sets its top-of-search modifier to 0% on that term (it keeps product pages and rest of search at a low base) — not a negative, so it can be handed back after the deal. Note: B6 converts better than B4 on “bamboo sheets” (13.6% vs 10.9%, ACoS 34% vs 62%) at a higher price; after the deal the owner of that term should be re-decided on rank and profit per click.')
lead('Correction for the app.', 'A cross-product view of the same brand’s ASINs on each keyword (a “sibling” check) before any bid is written, and an owner field in the plan per keyword.')

# ---------------------------------------------------------------- D9 more campaign types
section('Campaign types that should also be running')
lead('What the run proposes.', f"26 builds: 18 Sponsored Products exact “tail/coverage” rows and 1 discovery broad (loadable), and 8 that the loader cannot write (Sponsored Brands, Sponsored Brands Video, Sponsored Display, and product-targeting conquest) — marked PAUSED for a person to build. They sit in the file as PAUSED rows for a person to build, with nothing that makes that happen.")
rows = [
    ['Sponsored Brands headline — exact on the hero terms', 'Builds 2399 (“bamboo sheets”, $5.16/day), 2367 (“queen”, $10.07), 2383 (“king size”, $3.34)', 'A second top-of-page surface above the SP top slot; our above-bar CTR at the top says the creative will be clicked. Separate auction, so it adds top-of-page presence without bidding against our own SP.', 'Build all three this week; size budgets to ~50–100 clicks a week each (the planned $3–10 a day buys 1–3 clicks); read new-to-brand and branded-search lift, not only ACoS.'],
    ['Sponsored Brands Video — exact', 'Builds 2391 (“bamboo sheets”), 2375 (“queen”)', 'Video placements sit mid-search where we have no presence; sheets sell on feel and fit (deep pocket, cooling), which video shows.', 'Build as a 100-click probe each during the deal.'],
    ['Sponsored Display — own-page defence', 'Build 2407 (our own ASINs)', 'Product pages are where B4 still leaks clicks (39% of all product clicks in the deal) — and rivals’ ads on our pages take shoppers away. Defending our pages with our own ASINs keeps them in the family.', 'Build; keep it separate from ranking campaigns so the ranking mix is read clean.'],
    ['SP product targeting — conquest', 'Build 2415 (rival ASINs)', 'During the deal we undercut the reference rivals: BAMBAW $89.99, BC Bella Coterie $129.99, BAMPURE $94.99, Hotel Sheets Direct $69.99 (raised from $54.99). A cheaper, well-rated offer on their page converts.', 'Build against the rivals whose price is above ours and rating ≤ ours; own campaign, own ceiling (contribution × its CVR).'],
    ['SP phrase / broad discovery on the hero roots', 'Build 2742 (“cooling sheets king size” broad) only', 'The exact set covers ~2,800 terms; the market library holds 24,000 in the Bamboo group alone. Discovery finds converting variants to promote to exact.', 'One phrase campaign per in-focus root (bamboo / bamboo queen / bamboo king), low base, 0% top-of-search, harvest weekly.'],
    ['Branded defence', 'B6 “decolure bamboo sheets” 9% ACoS; B4 6.7%', 'Cheap and protects the brand shelf; needs one owner between B4 and B6.', 'Keep; give it one owner.'],
]
table(['Type', 'In the run', 'Why, from the data', 'What to do'], rows, widths=[3.4, 3.8, 5.4, 4.4], size=7.5)
lead('Correction for the app.', 'Non-SP builds need a way to load (or a task created for a person with a due date) — today they are written as PAUSED rows and nothing happens. Budgets on new formats should be sized to a readable click count in the read window, like the SP tail rows (15 clicks by 09-28).')

# ---------------------------------------------------------------- D10 metrics
section('Metrics the app should be reading')
rows = [
    ['Top-of-search impression share, per target', 'Measured by Amazon; in Command Center; not read by the engine', 'B4 median 5.6%; hero terms 0.6–3.2%', 'The direct measure of “are we at the top”; grade every push on it.'],
    ['Required vs delivered top-of-search clicks', 'Plan has the requirement; engine does not compare', 'B4 in focus: 80 of 788 a day (10%)', 'The traffic-gap test; sizes the push.'],
    ['Budget hours out', 'Not read', 'Flagship at 127% of budget', 'Separates “price” from “budget” as the cause of low share.'],
    ['Sibling ASIN on the same keyword', 'Not read', '1,242 shared terms, 81–87% of spend', 'Stops the two products bidding against each other.'],
    ['Sponsored rank and organic rank per term', 'ASINsight has it; not used', '“bamboo sheets” SP 18–19, organic 32–36', 'Shows where the ad actually sits; a TOS push should move SP rank to page 1.'],
    ['Paid share of our own traffic per term', 'ASINsight traffic_dist_ad', '“cooling sheets” 76% paid; “bamboo sheets” 36%', 'High paid share with flat rank = buying clicks that do not convert into rank.'],
    ['Top-3 click and conversion share', 'ASINsight', '“bamboo sheets” 40% / 6.3%', 'How concentrated the term is; how much share the top needs.'],
    ['Brand click and purchase share (SQP)', 'Field present, empty (clickShare null)', '—', 'The rank driver itself: our share of the term’s purchases vs the ranks above us.'],
    ['Price, discount and reviews vs the reference rival', 'In the brief, not tied to keywords', '15 rivals raised price', 'Explains CVR moves; re-weights pushes during a deal.'],
    ['Rank response per 100 top-of-search clicks', 'Not computed', 'Bamboo|King 35 → 22 on ~+3 TOS clicks/day per term in the deal', 'Tells the push how much volume a position costs; replaces a fixed step.'],
    ['TACoS and organic sales trend', 'Daily TACoS available', 'B4 ~14% → 19.5% in the deal; B6 12% → 6%', 'The payoff of rank is organic sales; B6’s falling TACoS is falling ad sales, not rising organic.'],
    ['CVR by child/size and the serving child', 'Stock rules only', 'Heroes at YELLOW shelf', 'A push on a size whose hero is short converts on the wrong child.'],
]
table(['Metric', 'Today', 'Value now', 'Why it matters'], rows, widths=[4, 3.6, 4, 5.4], size=7.5)

# ---------------------------------------------------------------- D11 recommendations
section('What to do — B4 and B6')
for b in [
    '**B4, in the deal (to 09-28):** push every in-focus exact ranking campaign on top of search daily by rank gap (Part A), with the budget raised where it caps. Read top-of-search impression share and clicks every morning; share rising with price = keep stepping; share flat after a price step = check budget hours out, the B6 sibling, and eligibility, in that order.',
    '**B4 hero terms:** “bamboo sheets”, “bamboo sheets queen size” (fixed bids first), “bamboo sheets king size”: +30% a day, budget +30%, until top-of-search clicks reach the plan (490 / 248 / 298 a week). Rows at 0–0.1% share (“bamboo sheets queen”, “queen bamboo sheet set”) are reset to the group’s clearing price before stepping.',
    '**B4 cooling:** no extra bid on the head term “cooling sheets” until the offer answers the cooling query; the cooling terms that meet both bars at the top — “bamboo cooling sheets”, “cooling sheets queen” (CVR 21.8% vs 12.1%), “king cooling sheets” — are traffic gaps and are pushed like the Bamboo terms.',
    '**B6:** assign owners on shared terms; on B6-owned terms restore top-of-search volume to late-August levels at the pre-cut prices and grade on rank; verify the King/Queen/Full CVR shortfall at campaign level before adding bid there.',
    '**Both:** build the SB headline, SBV, SD defence and conquest rows this week at readable budgets; add phrase discovery on the hero roots.',
    '**From 09-29:** evaluate cost per click only on terms now receiving their required clicks; hold the rest on the push until they do.',
]:
    bullet(b)
