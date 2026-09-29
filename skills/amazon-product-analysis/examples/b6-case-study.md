# B6 — worked engagement (teaching case)

A real engagement, 28–29 September 2026: an automated PPC decision engine audited a bamboo sheet set mid-deal, and the audit had to be corrected before anything loaded. It shows most of what this framework guards against, with numbers. Roles only: "the product owner" decides limits and exceptions; "the PPC manager" runs the engine and loads changes.

## Contents
1. Context
2. What the engine proposed
3. What it got wrong — 32 failures in 11 groups
4. The corrected logic
5. What the corrected plan looked like
6. Competitor findings and how they changed decisions
7. The Sponsored Brands / video test
8. Lessons that generalise

---

## 1. Context
- **Product**: bamboo sheet set, 6 pieces, sizes Twin to California King, many colours; 357 campaigns in the engine's list; ~841 search terms with spend.
- **Calendar**: a Best Deal ran 26–30 Sep; a Lightning Deal was booked for 15 Oct and another Best Deal for 22–28 Oct, then Prime / Black Friday. Deal prices ~20% below list (King White $72.24, Queen White $67.99, Full White $59.49).
- **Where things stood** (all campaigns for the product):

| Period | Spend/day | Ad sales/day | ACoS | Orders/day | TOS clicks/day | Product-page clicks/day | TOS share | TOS bid |
|---|---|---|---|---|---|---|---|---|
| Before the deal (12–25 Sep, excl. a one-day deal) | $283 | $1,104 | 25.7% | 14.0 | 42 | 64 | 34% | $4.86 |
| Best Deal (26–28 Sep) | $907 | $2,095* | 43.3%* | 30.3* | 116 | 177 | 33% | $5.68 |

\* still settling (7-day attribution). The deal tripled spend and doubled orders but did not move ads to the top: product pages still took about half the clicks.
- **Margin**: Sellerboard profit per unit before ads $18.81 blended ($18.18 at deal price) → **break-even ACoS 23.8%**; per colour it ranged widely (King White $15.97, Queen White $19.51, Full White $22.06, Queen Creme $22.51, Queen Olive $12.43).
- **Owner rules**: margin after ads above 10%; **spend limit $1,300/day for 29–30 Sep as a stated two-day exception** (margin could run ~7%), with the increase going to top of search on pushed ranking terms; from 1 Oct a post-deal audit re-sets limit, margin rule, prices and goals. No numeric TACoS target; no bidding-strategy changes; Amazon suggested bids not used.

## 2. What the engine proposed
188 changes on 126 campaigns plus 17 new campaigns: twelve +75% top-of-search price jumps ("doses") on Queen, Full, King and cooling terms, colour switches, 62 objective retags, brand negatives on the brand broad campaign, two structural folds. Its forecast: spend $515 → $889/day, ACoS 29.7% → 42.9%, TACoS 9.7% → 15.7%. Its own review held a few rows and endorsed the run at $622/day. It recorded **no deal**.

## 3. What it got wrong — 32 failures in 11 groups
Status after the engine's second run (29 Sep): 7 fixed, 8 partly fixed, 13 not fixed, 4 new findings.

| Group | Failures | Concrete examples |
|---|---|---|
| **Calendar and goals** | no deal read; no goals or spend target; spend sized on a "25% TACoS rung" | Deal recorded as null while three deals sat on the calendar. Baseline $515/day included four deal days; settled spend was ~$283/day. |
| **Economics** | wrong margin; limit tied to what was already paid | Priced on $26.60 profit/unit (33.8% break-even) instead of $18.81 (23.8%) → every break-even ~40% too high; 154 of 180 readable ranking campaigns already paid above the true break-even at the top. Limit = own TOS cost + 15%, which drifts up with every raise. |
| **Pricing and steps** | +75% jumps; over-limit prices left in place; 900% cap mishandled | Full Size Bamboo Sheets $8.43 → $14.77 (≈$105 per order vs $22 profit; its own notes put the odds at ~20%). At a $0.50 base the most a 900% boost can bid is $5.00 — the engine first raised the base +180% (lifting every placement), then took the boost to 900% and credited it with a +75% step's clicks. |
| **Placement** | boost raised on campaigns not at the top | Bamboo Cooling Sheets took 8% of clicks at the top and 89% on product pages; raising the boost bought nothing while the base kept buying product pages. |
| **Qualification and consistency** | focus overriding a qualifying term; no ceiling-vs-cost test; listing-flagged terms pushed | "bamboo sheets" (≈116,000 searches/month, 19.1% TOS CVR vs ~2% market) marked out of focus and labelled a taper, while the written change raised it $6.10 → $6.53 — above twice break-even. Terms converting 0.68× and clicked 0.55× the market were pushed with money. |
| **Variation routing** | hero moved to a slow colour; size changes; discovery on best sellers; push-pace stock-outs | 75 Queen campaigns switched to Queen Olive (7th seller) on a forecast "White runs out 3 days before arrival" computed at the inflated push pace; King Black → California King Black; discovery campaigns advertising White. |
| **Objectives** | colour / competitor / Spanish / misspelling terms retagged Ranking | Twelve wrong of 62: purple, burgundy, black… bamboo sheets; "bella sheets bamboo"; "sábanas de bamboo"; "bboo sheets"; and a real ranking target retagged conversions. |
| **Structure** | raises on paused keywords; duplicates; builds and folds mid-deal; brand negatives | Brand negatives added to the brand broad campaign (621 clicks, 123 orders, 11.7% ACoS in 30 d — the most profitable campaign) while the brand exacts that would take the traffic had 2 and 33 clicks and one advertised Queen Olive. |
| **Loader and scope** | changes outside its list; budgets blocked while prices loaded; withheld rows exported; shared campaigns | First run: 166 changes on 54 campaigns it had no state for; all 35 budget rows failed while price rows passed (a push without budget stops mid-afternoon); 18 rows its own text said to hold were exported. |
| **Forecast and data** | inflated click credit; requirements not reconciled; missing ranks; thin-data moves; band-triggered cuts | Top-of-search clicks forecast 69 → 884/week; own history showed +5–15% steps buying 0.85× net of drift. No current rank for 38 of 40 targets in the first run. |
| **Competitor targeting** | own listings treated as competitors; duplicate ASIN targets; mismatched targets | Product targets on the brand's own 4-piece set tagged conversion; one competitor ASIN in several campaigns; a $25 microfiber set beside bamboo conquest targets. |

## 4. The corrected logic
1. **Calendar gate first**: deal days → no judgement on deal data, no builds, folds or structural changes; a stated spend limit; a dated exit plan; 7-day settle after each deal.
2. **Goals before pricing**: spend limit and margin rule per window; product goal with dated milestones (top 10 on at least half the push terms by 19 Oct, the rest by early November); a settled baseline.
3. **Economics per advertised SKU**: break-even CPC = that colour's Sellerboard margin × the campaign's TOS CVR (own ≥50 clicks, blend 15–50, size rate below 15). A colour switch changes the break-even in the same write (Queen Olive $12.43 vs Queen White $19.51).
4. **Push qualification** (all required): a plan, CVR above market at the top, within ~30 places of target, hero stock ≥7 days and ≥ days to next arrival, keyword live, ceiling ≥ own TOS cost per click, no listing flag. Failing one → WAIT with the reason.
5. **Push price** = break-even × (1 + premium) (+25% if rank ÷ target ≤ 1.5, else (ratio − 1) × 50%); **ceiling 2 × break-even**; raises ≤ +30%/day while not holding the top (top-3 sponsored most hours and ≥30% TOS impression share); over-ceiling → ceiling now; 3 days at ceiling without the top → owner; TOS CVR below market on 50+ clicks → stop; at target → HOLD RANK.
6. **Mix fix in the same write**: product pages >20% on ≥15 clicks → base −50% (−25% where product pages sell), boost re-solved to hold the TOS price; boost ≤900%, base ≥ price ÷ 10.
7. **Everything not pushed at its own break-even**: non-push ranking straight to break-even with no TOS clicks, else ≤50% steps; non-ranking cut ≤30% only when over break-even on both 30 and 90 days; no raises outside the push during a deal; liquidation judged on stock cleared.
8. **Routing**: ranking = White of the size (backup only if White can't reach its next arrival; ≤7-day gap = TIGHT, ease not swap); discovery = the size's clearance colour; colour-named terms keep their colour; size never changes; cover on the 30-day pace.
9. **Structure**: one exact owner per term (close variants), negated in discovery; restart before build; brand negatives only after brand exacts are defensive, on White and funded.
10. **Requirements set volume and budget, never price**; reconciled to what the product sells.

## 5. What the corrected plan looked like
- 18 terms passed demand, conversion, reach and stock: **13 funded, 4 waiting, 1 at target**. Waiting reasons: two King terms on a listing flag; three terms whose ceiling sat below what they already paid (e.g. "bamboo bed sheets": ceiling $3.44 vs $6.01 paid).
- Push budgets $774/day (full plan $1,317; the three biggest scaled to 45% so budgets could never take the product past $1,300). **Expected day-one spend ~$750** (push ~$230, rest ~$525 after cuts) — well under the limit, because **11 of 13 funded terms were at or near their ceiling**: the push was capped by price, not money.
- The one lever to spend more at the top was a **time-limited ceiling raise** on named terms — the owner's decision, starting with "bamboo sheets" (at its $6.10 ceiling = 2 × $3.05 for weeks, 2.4% TOS impression share; option 2.5× = $7.63 until 14 Oct).
- Every focus campaign got a move: of 77, 10 pushed, 3 waiting, 1 holding, 34 to break-even, 17 stepped down 50%, the rest paused / already under.
- Non-ranking: 104 campaigns — 13 inside break-even, 10 over on both windows (cut ≤30%, incl. the four size broads at 41–114% ACoS), 75 too thin, 4 liquidation, 2 paused.
- Colour: Queen stayed on White (317 units, 42 days vs 31 to a 1,002-unit arrival); 18 discovery campaigns moved to clearance colours; the brand broad back to Queen White.
- Held: all 17 builds, both folds, the brand negatives; 3 restarts at break-even on 1 Oct; "bamboo sheets full" restarted immediately as a push term.
- Worked trails for these cases: `templates/decision-trail-examples.md`.

## 6. Competitor findings and how they changed decisions
Coverage: 13 of 32 mapped competitors measured (competitor keyword exports 28–29 Sep, 12,197 keywords, 2,225 addressable), plus three niche pulls (~60 listings) and a price/BSR/review movement brief. Unmeasured sellers are unknown, not absent.

| Finding | Number | Decision it changed |
|---|---|---|
| We are small | 2.1% of tracked 7-day traffic (170,565 of 8,086,848); Pure Bamboo 15× ours, Bedsure 13× | Context only: targets on head terms are stretch |
| Falling, partly seasonal | Our traffic −37% since 6 Aug, +8% since 17 Sep; rivals −7–24% except KRIMANO | Rank loss not blamed on price alone; listing check on the King hero |
| Core terms: ad intensity, not coverage | We advertise on almost all 197 core bamboo terms; rivals out-advertise us on 79 carrying **88%** of core traffic | Push list confirmed (all 18 are core terms); order: winnable terms first |
| Stretch vs reachable | On 9 push terms only the two aspirational rivals sit at or above target; on King terms beatable KRIMANO already holds #6–#7 | Stretch terms judged on **rivals passed** (first milestone), not only distance; 14 days at ceiling with none passed → owner |
| Brand banners everywhere | 5–9 rivals run a brand banner above top of search on every push term; we run SB on **4 keywords, no video** (Pure Bamboo 3,791 / 2,524 video) | Push read on rank and orders, not TOS impression share alone; SB/video test |
| Cooling wording uncovered | 1.1% of 673,458 cooling traffic is ours; rivals advertise on 110 such terms where we run nothing | Seed cooling terms as exact in King/Queen discovery at break-even on the clearance colour |
| Brand term contested | 10 rivals advertise on our main brand term (48% of its traffic paid, theirs); we rank #9 organically | DEFEND funded first; store-spotlight banner and own-page defence in the test |
| Strongest ground on thin stock | We out-rank every tracked rival on the main Full and Twin bamboo terms; Full White ~61–68 units | Full push held to the stock plan; reorder Full White; no Full banner |
| Rivals moving | KRIMANO traffic +123% (launched a year earlier, 240–335 reviews); Pure Bamboo list $79.99 → $104.99 with 19% off; 11 of 32 on discount | Rival price cut >15% or new discount in a push term's top 10 → hold our price 3 days before reading a conversion drop |
| Value position | 6 pieces at $72/$68 vs 4-piece sets at $80–135; 3,128 reviews at 4.4★ vs niche median 2,630 | Conquest only on OFFENSIVE pages (pricier, fewer pieces, or same price with far fewer reviews); AVOID Bedsure ($60–70, 65k reviews), $40 sets, microfiber |
| Generic sheets | Led by $15–50 microfiber sets | Left to discovery at break-even; never pushed |

Standing rule throughout: **competitor data never set or raised a price** — break-even, the 2× ceiling, the +30% step and the spend limit stayed as they were. Competitor bids, conversion rates and review themes were not available and were not assumed.

## 7. The Sponsored Brands / video test
Approved by the product owner on 29 Sep; built by hand (the engine wrote Sponsored Products only).
- **Six campaigns, one format per term**: headline (product collection) on "bamboo sheets"; video on "bamboo sheets queen size", "bamboo sheets king size" (a waiting SP term — tests it without lifting the SP ceiling) and "bamboo cooling sheets" (8 rivals run video there); store-spotlight headline on the brand terms; Sponsored Display on our own product pages.
- **Budget**: $85/day for 14 days (~$1,190), a separate line inside the product's spend limit from 1 Oct, outside the SP push budgets.
- **Prices**: start bid = break-even with the size's TOS CVR (King White $15.97 × 20.0% = $3.19; Queen White $19.51 × 16.2% = $3.17); raise ≤30%/day while the banner isn't showing, never above 2× ($6.38 / $6.34); at 15 clicks switch to the campaign's own CVR.
- **Stops**: 20 clicks, 0 orders on a keyword → pause it; ACoS >2× break-even on ≥30 clicks → back to break-even, pause after 7 days.
- **Read 14 Oct** (before the next deal): ≤ break-even → keep, budget may grow ≤30%/step; between 1× and 2× → hold at break-even bid; above 2× → stop. **Halo check**: the same-term SP campaign's orders and TOS CVR not below the prior 7 days and rank not worse; if SP orders fall more than SB adds, the banner is taking our own clicks → stop.
- **Not built**: second formats on the same terms; "bamboo sheets full" probes (we already lead with little stock).

## 8. Lessons that generalise
1. **Read the calendar before any rule.** A deal changes margin, conversion and the meaning of every metric; judging, launching or restructuring on deal traffic corrupts the next audit.
2. **Economics come from the advertised SKU's real margin.** A 40% error in margin silently turns "below break-even" into loss on every row.
3. **A ceiling scales with the product; a limit anchored to what you already pay drifts.** Twice break-even keeps cost per order under the order value.
4. **Money cannot fix placement.** When product pages take the clicks, a boost raise buys nothing — fix the mix in the same write.
5. **Qualification before focus.** A priority label may limit new money; it must never override a qualifying term or disguise a raise as a taper. Every written value must match its label.
6. **Stock decisions use the settled pace, not the push forecast.** The inflated pace invented a stock-out and moved the hero to a slow colour.
7. **Structure waits for clean data; profitable traffic is protected first.** No builds or folds on event days; no brand negatives until the receiving campaigns can serve.
8. **Know when the constraint is price, not budget.** B6 could spend ~$750 of a $1,300 limit; the honest answer was an owner decision on ceilings, not bigger budgets.
9. **Competitor data changes what you fight for and how you judge progress — never the price.** State coverage every time.
10. **Every decision needs a re-read date and a reversal condition**, and every prior decision is graded before a new one (the second run fixed 7 of 32 failures; the rest carried a named test until fixed).
