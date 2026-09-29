# Template — decision trail examples (10 scenarios)

Worked trails in the workbook format: **Input → Metric → Logic (rule) → Decision → Action → Expected outcome → Validation**, plus the two lines every trail needs in its reasoning: *why this lever, not the adjacent one* and *what reverses it*. Writing rules: `references/12-writing-and-deliverables.md`.

**All numbers are examples from the B6 engagement** (bamboo sheet set, 6 pieces, sizes Twin–California King, Sep 2026; break-even ACoS 23.8%; margins per colour from Sellerboard, 27 Aug–25 Sep; CVR basis own top-of-search ≥50 clicks / linear blend 15–50 / size rate <15; ranking ceiling 2 × break-even; push step ≤ +30%/day; a deal was running, spend limit $1,300/day). B6's corrected plan ran its ACoS tests against the product-level 23.8%; a live analysis uses each advertised SKU's own break-even ACoS (its margin ÷ the price in force — register #1, never a blended parent), so treat the ACoS comparisons below as illustrative arithmetic. Stock: B6 gated pushes on the arrival test (ROOM / TIGHT) only; this framework also requires the advertised SKU to be Green (≥60 days) with projected cover staying Green through the push checkpoint (register #9, #10, #42) — trails 1 and 10 note where that changes the call. Rule IDs in the Logic rows are the B6 IDs; use the IDs of your own Decision rules tab. Narrative documents use the same reasoning without IDs.

Formulas used throughout:
- Break-even CPC = margin/unit × CVR of the placement bought. Ceiling = 2 × break-even. TOS price = base × (1 + boost).
- Push price = break-even × (1 + premium); premium = +25% if rank ÷ target ≤ 1.5, else (rank ÷ target − 1) × 50%; capped at the ceiling.
- Blend weight for CVR between 15 and 50 own clicks = (clicks − 15) ÷ 35 on the own rate, the rest on the size rate.

## Contents
1. Push term priced by the rank-gap premium
2. Push term above its ceiling
3. Waiting term — ceiling below what we already pay
4. Non-push ranking campaign brought to break-even
5. Mix fix (at-target term)
6. Non-ranking campaign cut on 30 and 90 days
7. Keyword BLOCK
8. Keyword HARVEST
9. Competitor ASIN — OFFENSIVE vs AVOID
10. Colour (variation) switch

---

## 1. Push term priced by the rank-gap premium — "bamboo sheets queen size"
| Step | Detail |
|---|---|
| Input | Exact ranking campaign on Queen White. 30 d: 100 clicks, 39% top of search / 61% product pages. TOS price $5.93 = base $1.37 × (1 + 333%). Rank 22 (daily crawl, 29 Sep; 12 a month earlier) → target 5. Own TOS CVR 20.0% (90 d, ≥50 clicks). Our TOS cost per click $4.80 (30 d). Plan 44 TOS clicks/day; getting ~1.3. Queen White 317 Available = 42 days at the 30-day pace; 1,002 arriving 30 Oct (31 days) → cover exceeds days to arrival. |
| Metric | Break-even $3.90 = $19.51 × 20.0%; ceiling $7.80. Rank ÷ target = 4.4 → premium (4.4 − 1) × 50% = 170% → push price $10.53 → capped at $7.80. Ceiling $7.80 ≥ our TOS CPC $4.80 → qualifies on cost. One step: $5.93 × 1.30 = $7.71 (≤ ceiling). |
| Logic (rule) | Qualifies: demand (plan), CVR above market at the top, within ~30 places, stock ROOM against the 30 Oct arrival, live, ceiling ≥ cost [R-P1]. Zone: 42 days = Yellow → under the house zones the raise loads only with a recorded, time-boxed owner acceptance to the 30 Oct arrival; without it → WAIT, no raise, dated re-entry [R-I, register #10, #42]. Premium and cap [R-P2, R-P3]. Below push price → raise ≤30% a day [R-P4]. Product pages 61% on ≥15 clicks and they sell → base −25%, boost re-solved in the same write [R-M1]. |
| Decision | PUSH (owner-accepted Yellow stock, time-boxed to the 30 Oct arrival) |
| Action | `PUSH — TOS price $5.93 → $7.71 (+30%): base $1.37 → $1.03, boost 333% → 649% (one write); budget → $156 (plan clicks × price + product-page spend, scaled so the product stays inside $1,300/day)` |
| Expected outcome | Top-of-search share of clicks from 39% toward 70%; top-of-search impression share toward ≥30% and a top-3 sponsored slot most hours; ~8.8 orders/day at full plan clicks; rank improves within ~5–19 days of the clicks landing. |
| Validation | Daily: impression share and sponsored rank — not holding → next step to $7.80 (the ceiling, not +30%). Day 3 at ceiling without holding the top → owner (time-limited ceiling raise or swap the term). Day 7: product pages still >20% → cut base again. 8–14 Oct (settled): rank vs 22. Stop the push if TOS CVR falls below market on 50+ clicks. |

- **Why this lever, not the adjacent one**: a boost raise alone would leave the base buying product pages (61% of clicks); a budget raise buys nothing while the price loses the auction (1.3 of 44 planned clicks); the full premium in one write would break the +30% step and hide what each step buys.
- **Landscape**: only Bedsure (#4) and Pure Bamboo (#12) sit at or above the target → stretch target; judge progress on rivals passed (first milestone: the next beatable rival ahead), not only distance to target. Competitor data does not change the price.
- **Reverses if**: rank falls >10 places (freeze price, find cause); TOS CVR below market on 50+ clicks (stop, back to break-even); Queen White cover drops below days to arrival by >7 days (switch to the backup colour, same size).

## 2. Push term above its ceiling — "full size bamboo sheets"
| Step | Detail |
|---|---|
| Input | Exact ranking campaign on Full White. TOS price $8.43 = base $1.87 × (1 + 351%). Prior run proposed a +75% jump to $14.77 (boost 779%). Rank 24 (16 a month earlier) → target 10. TOS CVR 14.1% (own, blended toward the size rate). Our TOS cost per click $6.32 (30 d). Product pages 29% of clicks, no product-page orders. Full White 61 Available, ~35 days; 6 arriving 6 Oct. |
| Metric | Break-even $3.12 = $22.06 × 14.1%; ceiling $6.24. Rank ÷ target = 2.4 → premium 70% → push price $5.30. Price $8.43 > ceiling. Cost per order at $8.43 = $8.43 ÷ 14.1% ≈ $60 vs $22.06 profit (≈2.7×); at $6.24 ≈ $44 (= 2 × margin); at the proposed $14.77 ≈ $105. |
| Logic (rule) | Above ceiling → cut to the ceiling now, never deferred [R-P5]. Proposed jump exceeds ceiling and step cap → not loaded [R-P3, R-P4, E17]. Product pages 29% with no orders → base −50%, boost re-solved [R-M1]. Ceiling ($6.24) is just below our TOS CPC ($6.32) → "thin": may not hold the top. |
| Decision | PUSH at ceiling (price cut). Full White ~35 days = Yellow → no further raises until Green or a time-boxed owner acceptance (register #10, #42); the cut to ceiling runs regardless |
| Action | `CUT — TOS price $8.43 → $6.24 (−26%, to ceiling): base $1.87 → $0.94, boost 351% → 564% (one write); budget → $32` |
| Expected outcome | Cost per top-of-search order falls from ~$60 to ~$44; product-page spend roughly halves; top-of-search share read daily — it may lose some auctions at $6.24. |
| Validation | Daily: impression share. Day 3 at ceiling without holding the top → owner. 8–14 Oct: rank vs 24, TOS CVR vs market. |

- **Why this lever**: a 15%/cycle gradual cut is for rows where we are learning; an over-ceiling price loses money on every order, so it goes straight to the ceiling. Pausing is wrong: the term converts, has a rank target and stock.
- **Landscape**: winnable — only beatable rivals between us and the target (first milestone KRIMANO #11). If it doesn't move at the ceiling in 7 days, the cause is ours (listing, colour, conversion), not the field.
- **Reverses if**: owner raises the ceiling for a set time (then +30%/day steps resume from $6.24, once stock is Green or the owner has accepted the Yellow cover for that window); Full White cover falls below days to next arrival (ease the push before the stock-out day).

## 3. Waiting term — ceiling below what we already pay — "bamboo bed sheets"
| Step | Detail |
|---|---|
| Input | Exact ranking campaign on King White. 30 d: 23 clicks, 5 orders, $129.61, ACoS 32.5%; 90 d ACoS 57.7%. 96% of clicks at the top. 93 TOS clicks in 90 d at 10.8% CVR (own). TOS price $6.58 = $1.87 × (1 + 252%). Our TOS cost per click $6.01 (90 d). Rank 26 → target 6. |
| Metric | Break-even $1.72 = $15.97 × 10.8%; ceiling $3.44 < our TOS CPC $6.01 (the top clears at ~1.7× our ceiling). Cost per order at $6.58 ≈ $61 vs $15.97 profit (3.8×). |
| Logic (rule) | Fails the qualification gate "ceiling ≥ our top-of-search cost per click" → WAIT for an owner decision on a time-limited ceiling raise [R-P1 gate, F25]. Price above ceiling → cut to ceiling now [R-P5]. Product pages 4% → no mix fix. |
| Decision | WAIT (price cut to ceiling now) |
| Action | `CUT — TOS price $6.58 → $3.44 (−48%, to ceiling): boost 252% → 84%, base $1.87 unchanged` + `REVIEW — owner: time-limited ceiling raise to join the push, or leave at $3.44` |
| Expected outcome | Loss per order bounded at ≤2 × margin; top-of-search clicks likely fall (price below clearing). |
| Validation | Owner decision recorded by the next weekly tune; 14 days: clicks and orders at $3.44. |

- **Why this lever**: money alone at a profitable price cannot hold the top here; buying rank above twice break-even needs the owner, not the rules. Pausing loses a converting term with a rank target.
- **Landscape**: stretch — Bedsure #2, Pure Bamboo #5, Bambaw #8 hold the ranks above target; competitor data is not a reason to lift a ceiling.
- **Reverses if**: owner approves a raise (dated end) → rejoins the push with +30%/day steps; TOS CVR improves on 50+ clicks (break-even and ceiling recomputed each run).

## 4. Non-push ranking campaign brought to break-even — "king size bamboo sheets set" (+ a step-down variant)
| Step | Detail |
|---|---|
| Input | Exact ranking campaign, not in the push (no funded plan). 30 d: 45 clicks, 11 orders, $273.47, ACoS 30.5%; 90 d ACoS 23.9%. 87% top / 13% product pages. 60 TOS clicks in 90 d at 25.0% CVR (own). TOS price $5.85 = $1.50 × (1 + 290%). Advertises King Light Blue (the backup) although King White has 1,388 Available (133 days). |
| Metric | Priced on King White because the ad moves to White in the same write: break-even $3.99 = $15.97 × 25.0%. Price $5.85 is 47% above break-even; the cut (−32%) fits inside one 50% step. |
| Logic (rule) | Non-push ranking above break-even with top-of-search clicks → step ≤50% toward break-even; here break-even is within one step, so straight to it [R-B2]. No raises outside the push during the event [R-B3]. Ranking ads on the size's best seller while it has room [R-C1]. Product pages 13% → no mix fix. |
| Decision | BREAK-EVEN |
| Action | `BREAK-EVEN — TOS price $5.85 → $3.99 (−32%): boost 290% → 166%, base $1.50 unchanged` + `SWITCH AD — King Light Blue → King White (same size), by hand, before the price loads` |
| Expected outcome | CPC falls toward $3.99; ACoS toward 23.8%; some top-of-search clicks may drop; orders roughly held (the term already converts at 25%). |
| Validation | 8–14 Oct (settled): ACoS and orders vs the prior 30 days; rank not down >10 places — if it is, restore one step. |

**Variant — step-down**: "queen bamboo sheets" exact on Queen White: 30 d 16 clicks, 0 orders, $78.29; 90 d ACoS 53.1%; 24 TOS clicks at 8.3% → blend weight (24 − 15) ÷ 35 = 0.26 → CVR = 0.26 × 8.3% + 0.74 × 16.2% = 14.2% → break-even $2.77 = $19.51 × 14.2%. Price $6.06 is >2× break-even, so one 50% step: `BREAK-EVEN — TOS price $6.06 → $3.03 (−50%) now → $2.77 next cycle: boost 307% → 103%`. With 0 top-of-search clicks in 30 days it would go straight to break-even [R-B1].

- **Why this lever**: the term sells, so it is priced, not paused; it is not a push term, so no premium; the boost carries the change because product pages are already ≤20%.
- **Reverses if**: rank drops >10 places after the cut (restore one step); the term later qualifies for the push (rejoins through the push rules).

## 5. Mix fix on an at-target term — "king bamboo sheets"
| Step | Detail |
|---|---|
| Input | Exact ranking campaign on King White. 30 d: 51 clicks, 8 orders, $168.51, ACoS 26.0%; 90 d 23.2%. **20% top / 80% product pages.** TOS price $5.18 = $2.50 × (1 + 107%). Rank 7 vs target 10. 28 own TOS clicks in 90 d at 25.0%. |
| Metric | CVR blend: weight (28 − 15) ÷ 35 = 0.37 → 0.37 × 25.0% + 0.63 × 20.0% = 21.9% → break-even $3.49 = $15.97 × 21.9%; ceiling $6.98. Price $5.18 sits between break-even and ceiling. Product pages 80% of clicks at a $2.50 base. |
| Logic (rule) | At or better than target → HOLD RANK: keep the price, no raise [R-P8]. Product pages >20% on ≥15 clicks and they bring orders → base −25%, boost raised so the TOS price holds, same write [R-M1]. |
| Decision | HOLD RANK + MIX FIX |
| Action | `MIX FIX — base $2.50 → $1.88 (−25%), boost 107% → 176%; TOS price $5.18 held` |
| Expected outcome | Product-page share toward ≤20% with the top-of-search price unchanged; rank stays ≤10; spend shifts from product pages to the top at similar total. |
| Validation | Day 7: placement split — product pages still >20% → cut the base again (≤50% per step; base never below price ÷ 10 = $0.52). Daily rank: slips past 10 → rejoins the push. |

- **Why the pair, not one lever**: a base cut alone would drop the TOS price to $3.89 ($1.88 × 2.07) and risk the rank we hold; a boost raise alone buys nothing while the base keeps winning product pages.
- **Reverses if**: rank slips past target (push rules apply); product-page orders fall and total orders drop >30% (restore half the base cut).

## 6. Non-ranking campaign over break-even on both windows — "bamboo sheets full" broad (discovery)
| Step | Detail |
|---|---|
| Input | Broad discovery campaign on Full White. 30 d: 66 clicks, 7 orders, $184.23, ACoS 41.4%; 90 d ACoS 41.4%. Base $2.70. Full White is the size's ranking colour (61 Available); Full Olive has 259 units (~480 days of cover). |
| Metric | ACoS 41.4% > break-even 23.8% on 30 d AND 90 d, ≥15 clicks; below 2 × break-even (47.6%). Formula cut = 1 − 23.8 ÷ 41.4 = 43% → capped at 30%. |
| Logic (rule) | Over break-even on both windows → base −(1 − BE ÷ ACoS), max −30% a step [R-N1]. Discovery advertises the size's clearance colour (≥180 days cover, or ≥90 while selling ≤ the size median) [R-C2]. Exact ranking terms stay negated in it (one owner per term) [R-S1]. |
| Decision | CUT |
| Action | `CUT — base $2.70 → $1.89 (−30%)` + `SWITCH AD — Full White → Full Olive (same size), by hand` |
| Expected outcome | ACoS toward 23.8% with orders held within about −30%; Full White stock kept for the ranking campaigns. |
| Validation | 14 settled days after the cut: ACoS and orders; orders down >30% → restore half the cut; still over break-even on both windows → next step (≤30%). |

- **Uncapped case**: "red bamboo sheets" (colour term, Profitable Conversion) at 30.5% / 33.2% ACoS → cut 1 − 23.8 ÷ 30.5 = 22%: base $1.12 → $0.87.
- **Why this lever**: a band is not profit — the trigger is break-even on both windows (one window over, the other inside → watch only). A discovery campaign is judged on its own ACoS; the search terms inside it are judged separately (terms >2 × break-even on ≥30 clicks go to BLOCK in discovery / REDUCE in their exact owner).
- **Reverses if**: 30-day ACoS back inside break-even for a settled read → hold; the size's clearance colour runs low (<7 days cover) → never advertise it.

## 7. Keyword BLOCK — "silk sheets"
| Step | Detail |
|---|---|
| Input | Search term from auto/broad discovery. Class: other product type. Relevancy label: Not Relevant. ~6,990 searches/month. 90 d: 14 clicks, 0 orders, $13.50. No exact owner. |
| Metric | Irrelevant term with ≥5 clicks (14 here; >10 clicks with 0 orders puts it first in the queue) and 0 orders over 90 d. Two words → negative exact (phrase only when it appears in ≥2 broad/auto occurrences and has ≥3 words). |
| Logic (rule) | Other product type / Not Relevant, ≥5 clicks, 0 orders (90 d) → BLOCK [R-K2, register #21]; negation tree: not relevant → negative exact [STR]. Brand and push terms are never blocked. |
| Decision | BLOCK |
| Action | `BLOCK — negative exact "silk sheets" in every discovery campaign that serves it — reactive` |
| Expected outcome | Spend on the term → ~$0; no effect on orders. |
| Validation | 14 days after: spend on the term ≈ 0; if not, check which campaign still serves it and where the negative sits. |

- **Contrast — REDUCE, not BLOCK**: "king size bamboo sheets set" had 61 orders in 90 d at 29.8% ACoS and 11 rivals advertise it → a term that still sells is reduced toward break-even in its exact owner, never blocked.
- **Contrast — relevant non-converter**: a relevant term with ≥20 clicks and 0 orders goes to REDUCE when it has a live exact owner, or to REVIEW (fix queue: listing, price, colour, placement) when it has none — not a negative (register #38); exact ranking terms are never negated.
- **Reverses if**: the listing changes to cover the product type (never, here); a relevancy re-score moves it to relevant.

## 8. Keyword HARVEST — "king size sheets with corner straps"
| Step | Detail |
|---|---|
| Input | Search term found by discovery. Class: adjacent generic (sheets). 90 d: 9 clicks, 3 orders, $7.82 spend, ACoS 3.2%. No live or paused exact owner (close variants checked). |
| Metric | ≥3 orders at ACoS ≤ break-even (23.8%). Only 9 clicks, but converting rows skip the sample gate. ACoS ≤15% → high-conviction exact tier. |
| Logic (rule) | Harvest: ≥3 orders at ≤ break-even ACoS, no exact owner → exact campaign at break-even, negative exact in the source in the same upload [R-K4, register #22]. Adjacent generic → Profitable Conversion objective, not Ranking [R-O1]. No builds on deal days → decide on the post-deal audit [R-S3, E1]. |
| Decision | HARVEST |
| Action | `HARVEST — build Exact "king size sheets with corner straps" (Profitable Conversion) at $3.19 (break-even: King White $15.97 × size TOS CVR 20.0%, until 15 own clicks) on the King variation that earned the orders; negative exact in the source campaign, same upload — 1 Oct` |
| Expected outcome | Its own bid at break-even; discovery stops paying for it; orders held or rising. |
| Validation | 14 days after launch: ACoS ≤ 23.8% on ≥15 clicks → keep; above → bid down ≤30% a step; source still buying it → fix the negative. |

- **Why this lever**: proven demand deserves its own price and clean read; leaving it in discovery means it is bid by a campaign priced for other terms.
- **Reverses if**: the exact runs >2 × break-even on ≥30 clicks (back to break-even, then pause after 7 days); 20 clicks with 0 orders (pause).

## 9. Competitor ASIN — OFFENSIVE vs AVOID
Class uses price, pieces, rating and reviews against our same-size set (6 pieces; King $72.24 / Queen $67.99 at deal price; 4.4★; 3,132 reviews). Money decisions on an ASIN already targeted still follow its own clicks and ACoS.

**9a. OFFENSIVE — GOKOTTA King (B0BR53P7DY)**
| Step | Detail |
|---|---|
| Input | $107.00, 4-piece, 4.4★, 3,233 reviews. Our King: $72.24, 6 pieces, 4.4★, 3,132 reviews. Targeted today in one product-targeting campaign: 4 clicks, 0 orders (90 d). |
| Metric | Price ≥ 1.1 × ours ($79.46) and rating ≤ ours + 0.1 → we are the cheaper, bigger set on their page. At list price after the deal (~$90) the test still passes (1.1 × ~$90 ≈ $99 < $107). 4 clicks = below the read floor. |
| Logic (rule) | OFFENSIVE class [competitor ASIN rule]; thin data → no money verdict (<15 clicks) [E3]; scale only mapped competitors that pay for themselves [R-X3]. Competitor data never sets the bid. |
| Decision | OFFENSIVE (MONITOR on money) |
| Action | `KEEP — in the conquest campaign at break-even bid (margin × product-page CVR, size rate until 15 clicks); judge after 15 clicks` |
| Expected outcome | Orders from shoppers comparing a $107 4-piece set with our $72 6-piece set. |
| Validation | After 15 clicks: ACoS ≤ break-even → SCALE (+≤25% a cycle up to the break-even CPC); above → REDUCE; ≥20 clicks 0 orders or >2 × break-even on ≥30 clicks → BLOCK (pause target). Re-class if either price changes >15%. |

**9b. AVOID — Bedsure Queen (B07YKCZHGK)**
| Step | Detail |
|---|---|
| Input | $61.19, 4.4★, 63,791 reviews. Our Queen $67.99, 3,132 reviews. Targeted in 3 campaigns; 90 d: 257 clicks, 19 orders, $495.46, ACoS 33.7% in the main one; 17 clicks, 1 order, 46.7% in another; 1 click in a third. |
| Metric | Cheaper than us with >5× our reviews → they win the comparison on their own page. Money: ACoS 33.7% > 23.8% on ≥15 clicks, below 2 × break-even; still sells (19 orders). Same ASIN in 3 campaigns. |
| Logic (rule) | AVOID class → never add or scale [competitor ASIN rule]; ACoS > break-even on ≥15 clicks → REDUCE toward break-even [R-X4]; one owner per ASIN [R-X6]. |
| Decision | AVOID (REDUCE in the owner; DEDUPLICATE elsewhere) |
| Action | `REDUCE — target bid toward break-even in the 257-click campaign (≤30% a step)` + `DEDUPLICATE — pause B07YKCZHGK in the other two campaigns` + remove it from any proposed conquest build |
| Expected outcome | Same orders from one owner at one price; ACoS toward 23.8%. |
| Validation | 14 settled days: owner ACoS ≤ 23.8%; total orders on the ASIN within −20%; if ACoS has not improved after two steps → escalate (pause the target or owner review), never a third identical cut (register #25); ≥2 × break-even on ≥30 clicks → BLOCK. |

- **Why the split**: class decides whether we *add or scale* a target; the money rules decide the bid on what is already running. A profitable AVOID is held at break-even, never scaled; an OFFENSIVE target still has to pay for itself.

## 10. Colour (variation) switch — "queen bamboo sheet set"
| Step | Detail |
|---|---|
| Input | Exact ranking campaign advertising **Queen Olive** (the size's 7th seller). TOS price $7.89 = $1.70 × (1 + 364%). Rank 26 → target 6. TOS CVR 23.5%. Product pages 55% of clicks. Our TOS cost per click $6.84. Prior run: switched it to Olive, then proposed a +75% jump to $13.80 on Olive. Queen White: 317 Available = 42 days at the 30-day pace; 1,002 arriving 30 Oct (31 days away). |
| Metric | On Olive: break-even $2.92 = $12.43 × 23.5%, ceiling $5.84 — today's $7.89 would already be over it. On White: break-even $4.59 = $19.51 × 23.5%, ceiling $9.18. Premium (26 ÷ 6 − 1) × 50% = 167% → push price $12.24 → capped at $9.18. Step $7.89 → $9.18 = +16% (≤30%). White cover 42 days ≥ 31 days to arrival → ROOM. |
| Logic (rule) | Ranking ads on the size's best seller [R-C1]; zone: 42 days = Yellow → the price raise needs the same time-boxed owner acceptance as trail 1, else WAIT on White (switch still made) [register #10, #42]; move to the backup only when the hero's cover falls short of its next arrival by >7 days (≤7-day gap = TIGHT: ease, don't swap) [R-C6, R-I3–R-I4]; never change size [R-C4]; price on the advertised SKU's margin in the same write [R-F1]. Product pages 55% → base cut; at the 900% cap the base can fall only to price ÷ 10 = $0.92 [R-M1, R-M2]. |
| Decision | PUSH on Queen White (switch first; owner-accepted Yellow stock to 30 Oct) |
| Action | `SWITCH AD — Queen Olive → Queen White (same size), by hand` then `PUSH — TOS price $7.89 → $9.18 (+16%, at ceiling): base $1.70 → $0.92, boost 364% → 898%; budget → $50` |
| Expected outcome | Higher conversion and margin per order on the hero; rank accrues to the variation that sells; product-page share falls. |
| Validation | Console shows the ad on Queen White before the price row loads. Day 7: placement split. Daily: Queen White cover vs the 30 Oct arrival — if it falls short by >7 days, switch to the backup (Queen Light Blue, 302 units, same price), same size. |

- **Contrast — hero out of stock**: Twin White had 0 Available (12 arriving 16 Oct) → Twin ranking ads run on Sage Green (54 Available) until White is available and selling.
- **Why this lever**: staying on Olive cuts the ceiling by over a third ($9.18 → $5.84; margin 36% lower) and routes rank to a slow colour; changing size is never a stock fix; the prior +75% jump on Olive broke both the ceiling and the step cap.
- **Reverses if**: the White arrival slips so cover falls short by >7 days (backup colour); rank drops >10 places after the switch (freeze price, find cause).
