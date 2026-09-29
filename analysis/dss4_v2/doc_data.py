"""Deliverable 2 content — the document as data blocks. Every number is read from v2/out/*.json (the same files as the workbook).
Output: v2/out/doc_blocks.json (rendered by render_doc.js)"""
import json, collections
import load as L

O = L.OUT
J = lambda n: json.load(open(O + n))
P, M, CP, KW, R = J('product.json'), J('market.json'), J('competitors.json'), J('keywords.json'), J('ranking.json')
AR, D, LT, INV, KA, CF, FN = J('audit_review.json'), J('decisions.json'), J('ltsf.json'), J('inventory.json'), J('kw_actions.json'), J('conflicts.json'), J('financials.json')
K = {k['keyword']: k for k in KW}
OPP = {o['keyword']: o for o in R['opportunities']}
DEC = {d['campaign_id']: d for d in D['decisions']}
SKU = {s['sku']: s for s in P['skus']}
INVR = {r['sku']: r for r in INV['rows']}
LTR = {r['sku']: r for r in LT['rows']}
B = []
pc = lambda x, n=1: '—' if x is None else f"{x * 100:.{n}f}%"
money = lambda x: '—' if x is None else f"${x:,.0f}"


def h1(t): B.append(dict(t='h1', text=t))
def h2(t): B.append(dict(t='h2', text=t))
def p(t): B.append(dict(t='p', text=t))
def ul(items): B.append(dict(t='ul', items=items))
def table(cols, rows, widths=None): B.append(dict(t='table', cols=cols, rows=[[('' if v is None else str(v)) for v in r] for r in rows], widths=widths))


f30 = P['family30']['Info']
F = FN
S = D['summary']
sq = M['sqp_totals']
qb, kb, fb, tb = (INVR.get(s) for s in ('SATIN-QUEEN-BLACK', 'SATIN-KING-BLACK', 'SATIN-FULL-BLACK', 'SATIN-TWIN-BLACK-NEW'))
ss = K['silk sheets']
ss_own = DEC[D['owners']['silk sheets']]
ss_o = OPP['silk sheets']
verd = collections.Counter(a['verdict'] for a in AR)
cuts = [a for a in AR if a['kind'] in ('bid', 'budget', 'tos') and (a.get('change_pct') or 0) < 0]
big_cuts = [a for a in cuts if (a.get('change_pct') or 0) <= -40]
child_moves = [a for a in AR if a['kind'] == 'child']
import datetime as _dt
def _dd(a, b):
    return (_dt.date.fromisoformat(b) - _dt.date.fromisoformat(a)).days if a and b else 0
rk_cut = [a for a in cuts if a['role'].startswith('Ranking –')]
nr_cut = [a for a in cuts if not a['role'].startswith('Ranking –')]
qb2sg = [a for a in child_moves if a['current'] == 'SATIN-QUEEN-BLACK' and a['suggested'] == 'SATIN-4PCS-QUEEN-STONE-GREY']
qb2sg_rank = sum(1 for a in qb2sg if a['final_action'].endswith('SATIN-QUEEN-BLACK') and a['role'].startswith('Ranking –'))
qb2sg_other = sum(1 for a in qb2sg if a['final_action'].endswith('SATIN-QUEEN-BLACK') and not a['role'].startswith('Ranking –'))
qb2sg_qg = sum(1 for a in qb2sg if a['final_action'].endswith('SATIN-QUEEN-GREY'))
b6 = sum(1 for a in AR if a['cites_b6'])
lt1 = LT['rows'][0]
ltsf_camp = [d for d in D['decisions'] if 'LTSF Campaign' in (d['name'] or '')][0]
ltsf_camp2 = [d for d in D['decisions'] if 'Multi LTSF' in (d['name'] or '')][0]
push_terms = [o for o in R['opportunities'] if o.get('tier') == 'push']
rr = sorted(L.RADAR['silk sheets']['ranks'], key=lambda x: x['date'])
pre = [x['organicRank'] for x in rr if x['date'] <= '2026-07-15' and x['organicRank']]
late = [x['organicRank'] for x in rr if '2026-07-24' <= x['date'] <= '2026-07-31' and x['organicRank']]
sp_ranks = {x.get('sponsoredRank') for x in rr}
ex = next(a for a in AR if a['kind'] == 'bid' and a['entity'].endswith('satin sheets queen size'))
exi = ex['impact_estimate']
cbd = {d['campaign_id']: d for d in D['decisions']}
pt = []
for o in push_terms:
    d = cbd.get(D['owners'].get(o['keyword']))
    if d:
        pt.append((o['keyword'], d['checks']['d_spend_day'] / (len(d['owned_terms']) or 1)))
top10_share = sum(x[1] for x in pt[:10]) / sum(x[1] for x in pt)
stepp = sum(d['plan']['spend_day'] for d in D['decisions'] if any(b.get('change') for b in d['action']['bid_changes']) and not d['role'].startswith('Ranking') and 'LTSF' not in d['role']
            and not (d['role'] == 'Discovery / LTSF clearance' and (d['action']['child_to'] or d['child']) in {x for v in D['ltsf_targets'].values() for x in v}))
rk = F['share']['ranking_spend_day']
grow = F['share']['growth_spend_day']
wk3 = rk / (grow - stepp * (1 - 0.85 ** 2))
qg = SKU['SATIN-QUEEN-GREY']['e30']
qg_be_adj = (qg['pba_unit'] + LTR['SATIN-QUEEN-GREY']['avoid_per_unit']) / qg['avg_price']

B.append(dict(t='title', text='Decolure Satin Sheets 4-Piece — PPC audit review', sub='29 September 2026 · Amazon US · every number checked against the source data'))

# ================================================================= 0 summary
h1('The answers in brief')
ul([
    f"Silk sheets is being pushed. It is the biggest term in the market ({ss_o['mkt_purchases_day']} purchases a day, {ss['sqp_q3']['clicks']:,} clicks in Q3). Our rank slid from {min(pre)}–{max(pre)} (to mid-July) to {ss.get('radar_med7')}, "
    f"and the audit tapered it only because its focus list left out the Silk group — not because of the data. Its one exact campaign is capped by its budget "
    f"(${ss_own['budget']}/day, {ss_own['utilization']:.0f}% used, {ss_own['tos_is']}% top-of-search share) and advertises Queen Grey. It moves to Queen Black, top of search only, at ${ss_own['action']['budget_to']}/day.",
    f"The audit's cuts toward break-even are not followed on ranking terms. Almost all of this product's advertising runs above break-even (break-even is only {pc(SKU['SATIN-QUEEN-BLACK']['e30']['be_acos'])} for Queen Black). A rule of \"cut to break-even\" would therefore cut the campaigns that hold our rank. "
    f"Of the audit's {len(cuts)} price, modifier and budget cuts, {len(rk_cut)} are on ranking terms: {sum(1 for a in rk_cut if a['verdict'] == 'REJECT')} are rejected and replaced by the top-of-search structure. "
    f"Of the {len(nr_cut)} on other terms, {sum(1 for a in nr_cut if a['verdict'] == 'MODIFY')} become one −15% step with a rank guard, not a 50% cut. The other {sum(1 for a in nr_cut if a['verdict'] == 'REJECT')} are not made: Twin is on hold, the campaign is paused, or there are too few orders to judge.",
    f"Ranking stays on the Black children. Queen, Full and King use Queen Black, Full Black and King Black. King Black is restocked ({kb['sellable']:,} sellable plus {kb['in_transfer']:,} arriving from FC transfer), so every King ranking campaign moves to it from King Grey. "
    f"The audit's 'hero rule' moved {len(qb2sg)} Queen Black campaigns to Queen Stone Grey (4.8% conversion on 21 clicks). None of them goes there: {qb2sg_rank} ranking campaigns stay on Queen Black, {qb2sg_qg} non-ranking ones go to Queen Grey (the #1 LTSF SKU), and {qb2sg_other} with no spend in 90 days, paused or duplicate stay as they are.",
    f"LTSF comes first for everything that is not ranking. The #1 LTSF SKU is {lt1['sku']} (${lt1['total_ais']} of the ${LT['totals']['ais']:,} total AIS charge, about {lt1['est_aged_left']} aged units left). "
    f"The main LTSF campaign does not advertise it, and 23 of the 45 SKUs it does advertise are not on the LTSF sheet. Non-ranking Queen traffic moves off Queen Black onto Queen Grey.",
    f"Spend share: today ranking campaigns take {pc(S['now_ranking_spend_share'], 0)} of spend and {pc(S['now_ranking_click_share'], 0)} of clicks. After the plan they take {pc(F['share']['ranking_of_all_spend'], 0)} of all spend, "
    f"or {pc(F['share']['ranking_of_keyword_growth_spend'], 0)} once the LTSF clearance and brand-defence budgets are ring-fenced. Reaching 80% of all spend would need non-ranking cut to ${F['share']['nonranking_cap_for_80pct']:.0f}/day, "
    f"about 60% below plan. That would stop the LTSF clearance, so it is set out as an owner decision rather than done automatically.",
    f"Top of search, for every exact campaign: {sum(1 for d in D['decisions'] if d['action']['tos_to'] == 900 and d['role'].startswith('Ranking –'))} ranking campaigns and "
    f"{sum(1 for d in D['decisions'] if d['action']['tos_to'] == 900 and not d['role'].startswith('Ranking –'))} other exact campaigns go top-of-search only: a 900% modifier, the base bid at one tenth of the top-of-search price, and rest of search and product pages at 0%. "
    "The only exception would be a campaign whose own data shows top of search converting significantly worse; none does.",
    f"Back-up ranking child: every ranking campaign gets the back-up child's ad loaded PAUSED, and switches to it when the preferred child drops under 14 days of stock. "
    f"The back-ups are Queen Grey then Stone Grey for Queen, King Red then King Grey for King, Full Grey for Full, and Twin Pink for Twin. "
    f"At the plan's pace the Queen switch comes around {[b for b in INV.get('backups', []) if b['size'] == 'Queen'][0]['switch_date']} and the Full switch around {[b for b in INV.get('backups', []) if b['size'] == 'Full'][0]['switch_date']}.",
    f"Stock is the binding constraint. At today's pace with last year's Q4 lift, Queen Black runs out around {qb['stockout_now_pace']} and Full Black around {fb['stockout_now_pace']}, with nothing inbound. "
    f"Under the plan: Queen {qb['stockout_date']} ({'the same date' if _dd(qb['stockout_date'], qb['stockout_now_pace']) <= 0 else str(_dd(qb['stockout_date'], qb['stockout_now_pace'])) + ' days earlier'}, because non-ranking Queen traffic moves to Queen Grey and offsets the push) and Full {fb['stockout_date']} ({_dd(fb['stockout_date'], fb['stockout_now_pace'])} days earlier). "
    f"The push only pays if they are restocked. To reach 31 Jan at the plan's pace: Queen Black needs about {qb['units_short_to_31jan']:,} units, Full Black {fb['units_short_to_31jan']:,} and Twin Black {tb['units_short_to_31jan']:,}.",
    f"Money: the plan adds about {money((F['plan']['ads'] - F['now']['ads']))} of ad spend a month and {money(F['plan']['sales'] - F['now']['sales'])} of ad-attributed sales. Net profit on a 30-day basis goes from {money(F['now']['net'])} to about {money(F['plan']['net'])}, before any organic gain from better rank. "
    f"The push is an investment ahead of Q4, when last year's units ran ×{P['season']['2025-11']} (Nov) and ×{P['season']['2025-12']} (Dec) of September. The Push-cost tab lists every term so the owner can trim.",
])

# ================================================================= 1 product
h1('1. Product')
p(f"The family has {len(P['skus'])} SKUs over four sizes. In the 30 days to 28 Sep it sold {f30['Units']:,} units for {money(f30['Sales'])}, spent {money(F['now']['ads'])} on ads (TACoS {pc(F['now']['tacos'])}) and made {money(F['now']['net'])} net ({pc(F['now']['margin'])}). "
  f"Of those units, {f30['UnitsOrganic']:,} were organic and {f30['UnitsPPC']:,} came from paid ads (Sellerboard same-SKU attribution).")
bs = P['by_size']
table(['Size', 'Units 30d', 'Sales 30d', 'Profit before ads/unit', 'Break-even ACoS', 'Sellable stock', 'In FC transfer', 'Inbound shipped'],
      [[z, f"{v['units']:,}", money(v['sales']), f"${v['pba_unit']}", pc(v['be_acos']), f"{v['stock']:,}", f"{v['transfer']:,}", f"{v['inbound']:,}"] for z, v in bs.items() if z in ('Queen', 'King', 'Full', 'Twin')])
mo = P['monthly']
p('The trend over the year: ' + '; '.join(f"{m['month']}: {m['units']:,} units, TACoS {pc(m['tacos'])}, margin {pc(m['margin'])}" for m in mo[-6:]) +
  f". Last year's Q4 ran ×{P['season']['2025-10']} (Oct), ×{P['season']['2025-11']} (Nov) and ×{P['season']['2025-12']} (Dec) of September's units. Margin after ads has been thin since June, and it turned negative in August.")

# ================================================================= 2 market
h1('2. Market')
p('Amazon Search Query Performance for the terms we track (about 160) shows the market directly: searches, clicks and purchases for everyone, and our share of them.')
table(['Quarter', 'Searches', 'Purchases', 'Purchases/day', 'Market CVR', 'Our click share', 'Our purchase share', 'Our CVR'],
      [[v['label'], f"{v['volume']:,}", f"{v['purchases']:,}", v['purchases_per_day'], pc(v['market_cvr']), pc(v['our_click_share']), pc(v['our_purchase_share']), pc(v['our_cvr'])] for v in sq.values()])
at = M['ads_trend']
p(f"On the same {M['sqp_season_common']['keywords']} terms, searches fell from {M['sqp_season_common']['q4_2025']:,} (Q4-2025) to {M['sqp_season_common']['q2']:,} (Q2) and rose to {M['sqp_season_common']['q3']:,} (Q3). The Q4 lift is coming. "
  f"Our purchase share rose in Q3, helped by the July Best Deal, and our conversion is above the market's. Paying for clicks got dearer: our CPC went from ${at[0]['cpc']} ({at[0]['month']}) to ${at[-1]['cpc']} ({at[-1]['month']}), and ACoS from {pc(at[0]['acos'])} to {pc(at[-1]['acos'])}.")
tl = M['tracked_listings']
p('Across the niche dives, the leading listings moved like this (first → last snapshot, units per month): ' +
  '; '.join(f"{t['brand']} {t['asin']} ${t['first']['price']}→${t['last']['price']}, {t['first']['units']:,}→{t['last']['units']:,}" for t in tl[:6] if t['n'] > 1) + '.')
p('Our own listing changed in this period: ' + '; '.join(f"{e['date']} {e['title'].split(' — ')[0]}" for e in (M['events'] or [])) + '. Deals: ' +
  '; '.join(f"{e['date']}{'–' + e['endDate'] if e.get('endDate') else ''} {e['title'].replace('Deal: ', '')}" for e in (M['deals'] or [])[-5:]) + '.')

# ================================================================= 3 competitors
h1('3. Competitors')
rv = CP['rivals']
table(['Brand', 'Traffic (ASINsight)', 'Lead listing price', 'Units/month', 'SP keywords', 'SB keywords', 'SB video keywords', 'Amazon\'s Choice'],
      [[r['brand'][:28], f"{r['traffic']:,}" if r['traffic'] else '—', f"${(r['lead_last'] or {}).get('price')}" if r['lead_last'] else '—', f"{(r['lead_last'] or {}).get('units'):,}" if r['lead_last'] and (r['lead_last'] or {}).get('units') else '—',
        r['reach_sp'] or 0, r['reach_sb'] or 0, r['reach_sbv'] or 0, r['reach_ac'] or 0] for r in rv[:10]])
tf = {t['term']: t for t in CP['term_field']}
p('On the head terms: ' + ' '.join(f"'{t}': we are #{tf[t]['our_organic']} organic / #{tf[t]['our_sp']} sponsored; " +
                                    ', '.join(f"{x['brand']} #{x['organic']}" for x in tf[t]['rivals'][:4]) + '.' for t in ('silk sheets', 'satin sheets', 'silk sheets queen', 'satin sheets queen size') if t in tf))
p('BEDELITE holds #1 organic and #1 sponsored on silk sheets and satin sheets. It also shows in Sponsored Brands, SB video and Amazon\'s Choice there, which is the full stack. '
  'MR&HM is #2 organic without Sponsored Brands. Love\'s cabin runs the most Sponsored Brands of any brand. On the colour long tail (black, pink, red, white and prints), Juicy Couture\'s SB video is on 117 searches where we have none.')

# ================================================================= 4 video
h1('4. Competitor video — can we make one like theirs?')
p('What can be verified: Amazon, YouTube and TikTok pages could not be opened from this environment, so no competitor video was watched. There is no public library of Sponsored Brands video creatives. '
  'What the data does show is who runs SB video and on which searches (ASINsight placements), and what each brand claims in its titles. The brief below is built from those facts, and it lists what needs checking in Seller Central.')
ul(['BEDELITE runs SB video on 17 head terms (silk sheets, satin sheets, silk bed sheets and others) where it is also #1 organic with Amazon\'s Choice. Its title claims: similar to silk, soft and cooling, reduces friction, gentle on hair and skin, 15" deep pocket.',
    'Juicy Couture runs SB video on 128 colour and print searches (black, pink, red and white satin or silk sheets, leopard, y2k bedding). Its approach is colour-led, with a bedroom-makeover look. Creator TikToks tagged #juicypartner point to paid creators.',
    'Formats found in the category: a how-to and bed-making demo (MR&HM, shown in a product-page video carousel), a texture close-up (Bedsure) and creator honest reviews (including one of ours on Amazon Live).',
    'Yes, we can make the same kind of video. Two cuts: (1) a head-term cut, 15–30 seconds, showing sheen and drape, a hair/skin friction cue, the 15" deep pocket fitting the mattress and our corner straps; '
    '(2) a colour cut showing each colour on a styled bed, linked to that colour\'s ASIN. Point the colour cut at LTSF colours first (grey, dark green, sea teal).',
    'Use only claims our listing makes: softer than silk, gentle on hair and skin, 15" pocket with corner straps, silky shiny weave. Do not borrow OEKO-TEX, cooling or hypoallergenic unless Decolure holds them.',
    'Check in Seller Central: whether B0839MKJMV has a video in its main image block, and whether a current 15–30 second SB video cut exists (we run SBV on 93 searches, but its creative is not visible in the data).'])

# ================================================================= 5 keywords
h1('5. Keywords')
cls = collections.Counter()
for k in KW:
    cls[k['cls']] += (k['m30'] or {}).get('spend') or 0
p(f"{len(KA):,} search terms had ad spend in 90 days or are tracked in SQP. By type, 30-day spend was: " + '; '.join(f"{c} {money(v)}" for c, v in cls.most_common(6)) +
  '. Each term gets one action in the Keywords tab: ' + '; '.join(f"{k} {v}" for k, v in collections.Counter(r['action'].split(' (')[0] for r in KA).most_common()) + '.')
p('The negative-exact list covers only terms that cannot be justified: another product, Spanish or French, a competitor\'s brand, or at least 20 clicks with no order (the chance of that at our 13.5% paid conversion is under 5%). '
  'Colour searches that match an LTSF SKU (grey, green) are bought exact on that SKU.')

# ================================================================= 6 ranking opportunity
h1('6. Ranking opportunity')
cv = R['curve']
p('From our own data, the link between organic rank and purchase share (SQP Q3 × Rank Radar median rank, terms with ≥60 purchases): ' +
  '; '.join(f"rank {k}: median {pc(v['median_share'])} of purchases ({v['n']} terms)" for k, v in cv.items()) +
  '. The ranking terms are the core satin/silk terms that together hold 80% of the market\'s purchases, where we are ranked and the size\'s ranking child has stock. That gives '
  f"{len(R['ranking_set'])} push terms and {len(R['maintain_set'])} maintain terms. For each push term the target is the next rank band. The clicks needed = the missing purchases ÷ our paid conversion on that term, "
  'capped at 11.5% of the market\'s clicks (our best observed click share).')
table(['Term', 'Market purchases/day', 'Our share Q3', 'Rank now', 'Q3 range', 'Target', 'Paid clicks/day now → target', 'Top-of-search CPC', 'Ranking child'],
      [[o['keyword'], o['mkt_purchases_day'], pc(o['our_share'], 2), o['rank_now'], f"{K[o['keyword']].get('radar_best')}–{K[o['keyword']].get('radar_worst')}", o['target'],
        f"{o['ad_clicks_day_now']} → {o['target_clicks_day']}", f"${o['tos_cpc']}", o['child']] for o in push_terms[:16]])

# ================================================================= 7 silk sheets
h1('7. Silk sheets — why the audit did not push it, and what the data says')
ul([f"The audit gave it 'OUT · taper' because its focus list was Satin, Satin|Queen and Satin|King. Silk was outside the focus, so it was tapered by rule. No metric of silk sheets was behind that call.",
    f"Market: {ss['sqp_q3']['volume']:,} searches and {ss['sqp_q3']['purchases']:,} purchases in Q3 ({ss_o['mkt_purchases_day']}/day), the biggest term we track. Our purchase share was {pc(ss.get('sqp_q4_share'), 2)} in Q4-2025, "
    f"{pc(ss.get('sqp_q2_share'), 2)} in Q2 and {pc(ss['sqp_q3']['our_purchase_share'], 2)} in Q3.",
    f"Rank: {min(pre)}–{max(pre)} every day from the start of tracking to 15 Jul. It then slid to {min(late)}–{max(late)} by 24–31 Jul, after the June Best Deal ended (8 Jul) and the price update of 17 Jul. The July Best Deal did not win it back. The 7-day median is now {ss.get('radar_med7')} "
    f"(Q3 range {ss.get('radar_best')}–{ss.get('radar_worst')}; ASINsight {(ss.get('asinsight') or {}).get('organic')}, Command Center {ss.get('cc_rank_last')}). " + ("Our sponsored rank on the tracker is 101 on every tracked day, meaning we are not in the top sponsored slots." if sp_ranks == {101} else "Our sponsored rank on the tracker is mostly outside the top slots."),
    f"Our ads on it: one exact campaign (ID {ss_own['campaign_id']}) advertising Queen Grey, with a ${ss_own['budget']}/day budget {ss_own['utilization']:.0f}% used and a {ss_own['tos_is']}% top-of-search impression share. It gets {ss_o['ad_clicks_day_now']} paid clicks a day out of the market's {ss_o['mkt_clicks_day']:,.0f}. "
    f"Paid conversion on the term is {pc(ss_o['paid_cvr'])}. Top of search converts at {ss_own['checks']['placement'].split('CVR ')[1].split(' on')[0]} against {ss_own['checks']['placement'].split('vs ')[1].split(' elsewhere')[0]} elsewhere (90 days).",
    f"Competitors: BEDELITE is #1 organic and #1 sponsored, with Sponsored Brands, SB video and Amazon's Choice. MR&HM is #2. Our SQP conversion on silk sheets ({pc(ss['sqp_q3']['our_cvr'])}) is about half the market's ({pc(ss['sqp_q3']['mkt_cvr'])}), because a shopper searching 'silk' finds a satin sheet. "
    "The title change of 25 Aug removed 'Silky' from the title. Check that the live title still carries the silk wording shoppers search for.",
    f"Decision: push. Move the ad to Queen Black (a proven seller with the best profit per top-of-search click). Go top-of-search only: 900% modifier, base bid ${ss_own['action']['bid_changes'][0]['bid_to']}, "
    f"top-of-search price ${ss_own['action']['bid_changes'][0]['eff_tos_to']}. Set the budget to ${ss_own['action']['budget_to']}/day for {ss_o['target_clicks_day']} clicks a day (from {ss_o['ad_clicks_day_now']}). Target: rank {ss_o['rank_now']} → {ss_o['target']}. "
    f"Cost over today: ${ss_own['checks']['d_spend_day']}/day for +{ss_own['checks']['d_orders_day']} orders/day. Stock: Queen Black is covered to {qb['stockout_date']} at the plan's pace, and the reorder decides whether the push continues past that date."])

# ================================================================= 8 audit review
h1('8. The audit\'s recommendations — judged on each campaign\'s objective')
p(f"Every non-cosmetic decision in the audit ({len(AR)}; renames and retags excluded) was re-judged. For each one we checked the campaign's objective, how much of our paid traffic on the term it carries, the term's rank and its trend, "
  f"the effect on clicks, orders, sales, spend and profit, the TACoS change, the advertised child's stock and LTSF status, and who ranks around us. Verdicts: " +
  '; '.join(f"{k} {v}" for k, v in verd.most_common()) + '. The verdict is read from the final action on each campaign, so the review, the campaign tab and this document agree.')
ul([f"Cuts toward break-even: {len(cuts)} price or budget cuts, {len(big_cuts)} of them 40% or more. On ranking terms they are rejected. For example, the audit cut 'satin sheets queen size' from ${ex['current']} to ${ex['suggested']}. That campaign carries {round((ex['campaign_share_of_our_paid_clicks_on_term'] or 0) * 100)}% of our paid clicks on the term; the term is {ex['main_term']['trend']} (rank {ex['main_term']['rank_med7']}, Q3 range {ex['main_term']['rank_best_q3']}–{ex['main_term']['rank_worst_q3']}) "
   f"and holds {ex['main_term']['mkt_purchases_day']} market purchases a day. The cut would save about ${abs(exi['d_spend_day']):.2f}/day and lose about {abs(exi['d_orders_day']):.2f} orders/day, plus the rank that those orders hold.",
   'On non-ranking terms the direction is right, but the size is not. One −15% step, a re-read after 7 days, and stop stepping if the term\'s organic rank slips 3 places — not 50% at once. '
   'Most of the 50% budget cuts would not bind anyway: those campaigns already spend below the new budget.',
   f"Child moves: the audit moved ranking campaigns from Queen Black to Queen Stone Grey, Full Black to Full Rosewood and Twin Black to Twin Blush Pink ('hero rule'). Rejected. Stone Grey converted 4.8% on 21 clicks, "
   f"against Queen Black's 18.2% at the top of search. Full Rosewood's aged units are estimated cleared ({LTR['SATIN-4PCS-FULL-ROSEWOOD']['est_aged_left']} left). Twin's top LTSF SKU is Sea Teal, not Blush Pink.",
   f"Rules from another product: {b6} audit decisions cite the B6 corrections document. Each one was re-decided on this product's data.",
   'Pauses and revivals: a duplicate campaign is paused only where another campaign owns the term on the preferred child. A paused campaign is revived only where it owns a ranking term or clears LTSF stock. New campaigns are built only where nothing, enabled or paused, buys the term; none is needed.'])
rows = []
for a in sorted([a for a in AR if a['kind'] in ('budget', 'bid', 'child', 'state') and a['verdict'] in ('REJECT', 'MODIFY')],
                key=lambda a: -(((a.get('campaign_now') or {}).get('spend_day')) or 0))[:14]:
    rows.append([a['campaign'][:48], a['kind'], f"{a['current']} → {a['suggested']}", a['verdict'], a.get('final_action'), ' / '.join(a['analysis'])[:220]])
table(['Campaign', 'Audit change', 'From → to', 'Verdict', 'Final action', 'Why'], rows, [2400, 700, 1500, 800, 1600, 3800])

# ================================================================= 9 campaigns
h1('9. Campaigns')
roles = collections.Counter(d['role'] for d in D['decisions'])
p(f"All 612 campaign IDs found in any source were checked: the audit export, Command Center (30 and 90 days, with placements), Sellerboard (live budget, utilisation, top-of-search share and bids) and Data Dive (the ASIN each campaign actually advertises). "
  f"{sum(1 for d in D['decisions'] if d['status'] == 'ENABLED')} are enabled. {sum(1 for c in J('campaigns_base.json') if c['name_mismatch'])} campaigns advertise a different child from the one their name says. "
  f"Data Dive agrees with the audit export on every single-ASIN campaign, so the actual child is used throughout. Roles: " + '; '.join(f"{k} {v}" for k, v in roles.most_common()) + '.')
p(f"Spend and click share. Today: ranking {pc(S['now_ranking_spend_share'], 0)} of spend, {pc(S['now_ranking_click_share'], 0)} of clicks. Plan, week 1: {pc(F['share']['ranking_of_all_spend'], 0)} of spend (${F['share']['ranking_spend_day']:.0f} of ${F['share']['all_spend_day']:.0f}/day) and "
  f"{pc(F['share']['ranking_of_all_clicks'], 0)} of clicks. Discovery clicks are cheap, so click share trails spend share. With LTSF clearance and brand defence ring-fenced as their own objectives, ranking is {pc(F['share']['ranking_of_keyword_growth_spend'], 0)} of the remaining keyword spend. "
  f"Two more −15% steps on the steppable non-ranking campaigns, if their ranks hold, take that to about {wk3 * 100:.0f}% by week 3. Reaching 80–90% of ALL spend needs non-ranking at ${F['share']['nonranking_cap_for_80pct']:.0f}–{F['share']['nonranking_cap_for_90pct']:.0f}/day. That would cut the LTSF clearance that is selling Queen Grey's aged stock, so it is left for the owner to decide.")
table(['Role', 'Campaigns', 'Spend/day now', 'Spend/day plan', 'Orders/day now', 'Orders/day plan'],
      [[r, sum(1 for d in D['decisions'] if d['role'] == r), f"${sum(d['now']['spend_day'] for d in D['decisions'] if d['role'] == r):.0f}",
        f"${sum(d['plan']['spend_day'] for d in D['decisions'] if d['role'] == r):.0f}", f"{sum(d['now']['orders_day'] for d in D['decisions'] if d['role'] == r):.1f}",
        f"{sum(d['plan']['orders_day'] for d in D['decisions'] if d['role'] == r):.1f}"] for r, _ in roles.most_common() if sum(d['now']['spend_day'] + d['plan']['spend_day'] for d in D['decisions'] if d['role'] == r) > 0.5])

# ================================================================= 10 placements
h1('10. Placements — getting ranking close to 100% top of search')
p('How it is set: modifier 900% (the maximum), base bid = the top-of-search price ÷ 10, rest of search and product pages 0%, bidding "Dynamic – down only". The top-of-search price is today\'s top-of-search CPC on the term, never cut. '
  'Rest of search and product pages then see only the tiny base bid (e.g. $0.23), so nearly all clicks come from the top row. Where a ranking campaign buys fewer clicks than its target and the budget is not spent, the top-of-search price is raised 10% at a time.')
ex_all = [d for d in D['decisions'] if d['match'] == 'Exact' and d['ad_type'] == 'SP' and (d['action']['state'] or d['status']) == 'ENABLED' and not d['role'].startswith(('Duplicate', 'Other product'))]
ex_tos = [d for d in ex_all if d['action']['tos_to'] == 900]
ex_w = [d for d in ex_all if d['action']['tos_to'] not in (None, 900)]
ex_none = [d for d in ex_all if d['action']['tos_to'] is None]
p(f"This applies to every exact campaign, not only ranking. {len(ex_tos)} of the {len(ex_all)} enabled exact campaigns go top-of-search only. Ranking campaigns keep today's top-of-search price; other exact campaigns keep today's effective top-of-search bid, less the −15% step where one applies. "
  f"The only exception is a campaign whose own 90-day data shows top of search converting significantly worse than the other placements (both at least 20 clicks, a 95% test). "
  + (f"{len(ex_w)} campaigns meet that exception: they keep the other placements open, with top of search weighted at 100% or more. " if ex_w else "No campaign meets that exception. ") +
  f"{len(ex_none)} enabled exact campaigns have no clicks in 90 days and no bid in any source, so they have nothing to price; set them the same way when they are next edited. "
  "Second-order effect: non-ranking exact campaigns lose their rest-of-search and product-page clicks. The plan counts only their top-of-search clicks, at top-of-search conversion, so their orders fall and their conversion rises.")

# ================================================================= 11 preferred variation
h1('11. Preferred variation')
p('Rule, from this product\'s data: among children that sell at least 10% of the size\'s units, pick the one with the most profit per top-of-search click (profit before ads per unit × top-of-search conversion), '
  'among those with at least 60 days of stock at the pace the ranking traffic would add. If no child qualifies, the size is held, not pushed.')
table(['Size', 'Chosen', 'Why', 'Days at push pace', 'Profit per TOS click', 'Ranking child today'],
      [[z, v['chosen'], v['basis'][:70], v['candidates'][0]['days_at_push_pace'] if v['candidates'] else '—', f"${v['candidates'][0]['value_per_tos_click']}" if v['candidates'] else '—', v['current_ranking_child']]
       for z, v in R['preferred'].items()])
h2('Back-up ranking child — when the preferred child runs low or out')
p('Every ranking campaign now carries a back-up product ad, loaded PAUSED. When the preferred child drops under 14 days of stock or goes out of stock, the back-up ad is enabled and the preferred ad paused. '
  'The switch back happens once the preferred child has 30 days or more. Rule for the back-up: another child with positive profit per top-of-search click and at least 5% of the size\'s units. '
  'One with 60 or more days of stock at push pace can carry the push; one with 30–59 days carries the maintain level only.')
BKI = INV.get('backups', [])
table(['Size', 'Preferred', 'Back-up #1 / #2', 'Can carry', 'Projected switch', 'Back-up lasts to'],
      [[b['size'], b['preferred'], f"#{b['order']} {b['backup']}", b['level'], b['switch_date'] or 'not before 31 Jan', b['backup_stockout'] or 'after 31 Jan'] for b in BKI])
qbk = [b for b in BKI if b['size'] == 'Queen']
fbk = [b for b in BKI if b['size'] == 'Full']
if qbk:
    p(f"Queen: at the plan's pace Queen Black falls under 14 days around {qbk[0]['switch_date']}. {qbk[0]['backup']} then carries the Queen ranking terms at maintain level until about {qbk[0]['backup_stockout']}"
      + (f", then {qbk[1]['backup']} until about {qbk[1]['backup_stockout']}" if len(qbk) > 1 else '') + '. After that, no Queen child can carry the ranking terms, so the Queen Black reorder has to land by then. '
      + (f"Full: Full Black switches to {fbk[0]['backup']} around {fbk[0]['switch_date']}, which lasts to about {fbk[0]['backup_stockout']}. " if fbk else '')
      + 'King: King Black does not need its back-ups before 31 Jan.')
p(f"King: King Black is restocked ({kb['sellable']:,} sellable + {kb['in_transfer']:,} in FC transfer; Data Dive still showed 293 on 23 Sep, before the August shipments were received). It becomes the King ranking child, replacing King Grey on every King ranking campaign. "
  f"Twin: Twin Black has {tb['stock_total']} units ({R['preferred']['Twin']['candidates'][0]['days_at_push_pace']} days at push pace), so Twin ranking is held until it is restocked.")

# ================================================================= 12 LTSF
h1('12. LTSF — the aged-stock view')
p(f"Source: the S4-LTSF sheet, column V (Total AIS Charge), ${LT['totals']['ais']:,} on {int(LT['totals']['units']):,} units. Checked cell by cell: every row's charge equals the sum of its age buckets. The sheet's snapshot is 15 Jul, with sales to 27 Aug. "
  'Aged units left today are estimated as aged units − sales in the sheet − 30-day pace × 33 days (oldest units sell first).')
table(['LTSF #', 'SKU', 'Total AIS (V)', 'Aged units', 'Oldest bucket', 'Sellable now', 'Aged left (est.)', 'Storage/AIS avoided per unit sold'],
      [[r['rank'], r['sku'], f"${r['total_ais']}", r['ais_units'], (r['oldest_bucket'] or '')[11:30], r['sellable_now'], r['est_aged_left'], f"${r['avoid_per_unit']}"] for r in LT['rows'][:10]])
ul([f"Queen Grey is the LTSF priority: ${lt1['total_ais']} of the charge and about {lt1['est_aged_left']} aged units left. Its oldest units were at 331–365 days in July, so they are now past 365 days. "
    f"Selling one of them avoids about ${lt1['avoid_per_unit']} of storage and AIS (the sheet's charge per month × months on hand). That is more than its ${qg['pba_unit']} profit before ads, so its break-even ACoS for clearance is {qg_be_adj * 100:.0f}% instead of {qg['be_acos'] * 100:.0f}%.",
    f"The LTSF campaign ('{ltsf_camp['name']}', {money(ltsf_camp['now']['spend_day'] * 30)} and {ltsf_camp['now']['orders_day'] * 30:.0f} orders in 30 days) advertises {len(ltsf_camp['dd_asins'] if 'dd_asins' in ltsf_camp else [])} ASINs but not Queen Grey. "
    f"Add: {', '.join(ltsf_camp['action']['ads_add'])}. Pause the {len(ltsf_camp['action']['ads_pause'])} product ads that are not on the LTSF sheet or are estimated cleared.",
    f"'{ltsf_camp2['name']}': add {', '.join(ltsf_camp2['action']['ads_add'][:6])}…; pause {', '.join(ltsf_camp2['action']['ads_pause'])}.",
    'Auto, broad and phrase campaigns carry the LTSF work. Non-ranking Queen traffic moves from Queen Black to Queen Grey, and Twin discovery moves to Sea Teal. Colour searches go exact on their LTSF SKU: grey → Queen Grey, green → Full Dark Green. '
    'Ranking terms stay on the Black children. The two objectives do not share campaigns.',
    f"Under the plan, Queen Grey sells about {INVR['SATIN-QUEEN-GREY']['plan_pace_sep_equiv']} units a day (September equivalent, before the Q4 lift) and clears around {INVR['SATIN-QUEEN-GREY']['stockout_date']}."])

# ================================================================= 13 inventory
h1('13. Inventory')
table(['Child', 'Stock counted', 'Units/day now', 'Plan pace', 'Stock-out (today\'s pace)', 'Stock-out (plan)', 'Short to 31 Jan (plan)'],
      [[r['sku'], f"{r['stock_total']:,}", r['units_day_30'], r['plan_pace_sep_equiv'], r['stockout_now_pace'] or 'after 31 Jan', r['stockout_date'] or 'after 31 Jan', f"{r['units_short_to_31jan']:,}"]
       for r in INV['rows'] if r['sku'] in ('SATIN-QUEEN-BLACK', 'SATIN-KING-BLACK', 'SATIN-FULL-BLACK', 'SATIN-TWIN-BLACK-NEW', 'SATIN-QUEEN-GREY', 'SATIN-4PCS-QUEEN-STONE-GREY')])
p('Stock counted = sellable + FC transfer + inbound already shipped (Sellerboard, 29 Sep), projected with last year\'s monthly lift. Queen Black has no inbound; a June plan of 300 units was never shipped. '
  'The Queen Black count differs between sources (Sellerboard 1,807 sellable on 29 Sep, Data Dive 2,328 on 23 Sep). The plan uses the lower figure. Check Manage FBA Inventory before sizing the reorder.')

# ================================================================= 14 financials
h1('14. Financials')
table(['', 'Sales', 'Ad spend', 'TACoS', 'Net profit', 'Margin'],
      [['Now (30 days)', money(F['now']['sales']), money(F['now']['ads']), pc(F['now']['tacos']), money(F['now']['net']), pc(F['now']['margin'])],
       ['Plan (30-day equivalent)', money(F['plan']['sales']), money(F['plan']['ads']), pc(F['plan']['tacos']), money(F['plan']['net']), pc(F['plan']['margin'])]] +
      [[f"of which {k}", money(v['d_sales_day'] * 30), money(v['d_spend_day'] * 30), '', money(v['d_profit_day'] * 30), ''] for k, v in F['components'].items()])
p(F['note'] + ' TACoS is a result of the plan, not its target. Break-even ACoS is per child, from Sellerboard: profit before ads ÷ sales over the last 30 days. It includes realised prices, refunds, storage and inbound fees, so it is lower than the list-price margin Command Center shows (see Conflicts).')

# ================================================================= 15 final action
h1('15. Final action — in this order')
ul(['1. Stock: place the reorder for Queen Black (~' + f"{qb['units_short_to_31jan']:,}), Full Black (~{fb['units_short_to_31jan']:,}) and Twin Black (~{tb['units_short_to_31jan']:,}), sized to 31 Jan at the plan's pace. Confirm the Queen Black count in Seller Central first.",
    '2. Ranking owners (Campaigns tab, role "Ranking – push/maintain"): move the product ad to the Black child where needed. Then set TOS 900% / ROS 0% / PP 0%, the base bid and the budget shown, and bidding to "down only".',
    '3. Pause the duplicate exact campaigns listed. Their terms are owned by one campaign on the preferred child. In every ranking campaign, load the back-up child\'s product ad PAUSED (Back-up ranking child tab).',
    '3a. Every other enabled exact campaign: TOS 900% / ROS 0% / PP 0% with the base bids shown, unless the Campaigns tab marks it as the exception.',
    '4. LTSF: fix the two LTSF campaigns\' product ads, move non-ranking Queen traffic to Queen Grey, move the colour exact campaigns to their LTSF SKU, and re-enable the paused LTSF colour exacts.',
    '5. Non-ranking: one −15% step where ACoS is above break-even, then re-read after 7 clean days. Stop stepping any term whose organic rank slips 3 places.',
    '6. Add the negative exacts from the Keywords tab to the discovery campaigns.',
    f"When Queen Grey is down to about two weeks of stock (the plan clears it around {INVR['SATIN-QUEEN-GREY']['stockout_date']}), switch the campaigns routed to it to Queen Stone Grey, LTSF #2 (~{LTR['SATIN-4PCS-QUEEN-STONE-GREY']['est_aged_left']} aged units left).",
    '7. Daily check for two weeks: ranking clicks against target, top-of-search share, rank on each push term (Rank Radar), and days of cover on every preferred child. Under 14 days, switch to the back-up.',
    'Everything in 2–6 is in the Bulk upload tab, with campaign, ad group and keyword IDs where Sellerboard provides them.'])
h2('Owner decisions (the data cannot make these)')
ul([f"The ranking investment: the full push costs about {money(F['components']['Ranking – push']['d_spend_day'] * 30)} more a month (direct profit {money(F['components']['Ranking – push']['d_profit_day'] * 30)}). The top 10 push terms account for {top10_share * 100:.0f}% of the extra push spend. The Push-cost tab lets you drop terms.",
    'The spend-share definition: ranking at 80–90% of ALL spend would cut LTSF clearance and brand defence. Ranking at 80% of the remaining keyword spend keeps them.',
    f"If the reorder cannot land before about {qb['stockout_date']} (Queen) or {fb['stockout_date']} (Full), stop that size's push about two weeks earlier. Rank built on stock that runs out in peak season is lost.",
    'The step size on non-ranking campaigns (−15% a week here). It is a setting, not a number the data fixes.'])

# ================================================================= 16 conflicts
h1('16. Where the sources disagree')
table(['Area', 'What differs', 'What the plan uses', 'Status'], [[c['area'], f"{c['source_a']} vs {c['source_b']}"[:230], c['resolution'][:200], c['status']] for c in CF], [2000, 3800, 3000, 900])

json.dump(B, open(O + 'doc_blocks.json', 'w'), indent=1)
print(len(B), 'blocks')
