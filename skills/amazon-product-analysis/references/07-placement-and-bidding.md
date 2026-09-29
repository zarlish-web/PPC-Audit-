# 07 — Placement and bidding (Phase 7)

Use this file to turn a campaign or term decision (from `06-campaign-ppc-decisions.md`) into written numbers: base bid, top-of-search boost, rest-of-search modifier, budget, and the checks those numbers must pass. Economics inputs (margin per unit, conversion basis, break-even CPC, ceiling) come from `03-profitability-and-guardrails.md`. Metric definitions are in `02-metrics-and-formulas.md`.

## Contents
1. Placement model and price mechanics
2. Placement-first diagnosis
3. Pricing a push term
4. Mix fix (product pages over 20%)
5. Non-push ranking terms: down to break-even
6. Backward-solve procedure (one write per campaign)
7. DSTR → required clicks → budget → spend limit
8. Fixed-bid trial, graded push, discovery pricing
9. Day-1 spend forecast, event days, and the price checks
10. Open questions for the owner

---

## 1. Placement model and price mechanics

### 1.1 The three placements

Amazon reports placements **per campaign**, not per keyword. Every keyword in a campaign shares one top-of-search boost and one rest-of-search modifier. Placement data at keyword level is an estimate. [B6, PF]

| Placement | Where the ad shows | What it does for rank | What it does for profit | How it is priced |
|---|---|---|---|---|
| **Top of search (TOS)** | First row of search results for the term | The rank lever: paid sales on the searched term, in the slots shoppers use most. Ranking money belongs here | Usually the highest CVR and the highest CPC; judged on its own break-even CPC | `TOS price = base × (1 + boost)` |
| **Rest of search (ROS)** | Search results below the first row and later pages | Some rank value (still a search for the term); secondary | CVR usually between TOS and product pages | `base × (1 + ROS modifier)`. The modifier is lifted only when earned (§4.2) |
| **Product pages (PDP)** | Other listings' detail pages and our own | Not a rank lever for the term: the shopper is on a detail page, not searching the term | Often the cheapest click with the lowest CVR, and often where a priced-out campaign ends up spending | **Base only.** No PDP modifier is used to steer it |

Why this matters: a campaign that is priced out of the top still spends, but it spends on product pages. Blended CPC, CVR and ACoS hide this. Judge every placement against its own break-even. [PF, WB, PB, B6]

Example (B6, 30 days): "bamboo sheets" exact had 776 clicks: TOS 39%, ROS 4%, PDP 56%. TOS CVR was 19.1% at $5.66 CPC and PDP CVR was 11.6% at $2.78.

### 1.2 Price mechanics

| Item | Rule | Source |
|---|---|---|
| TOS price | `TOS price = base × (1 + boost)`. In a keyword campaign, "base" means the keyword's own bid. Every push rule writes this number and every ceiling check reads it (PF calls it the effective TOS bid) | [B6, PF, SR] |
| Boost range | 0–900%. A boost above 900% cannot be written | [B6, WB, CB] |
| Maximum TOS price at a given base | `base × 10`, which is the 900% cap | [B6 R-M2] |
| Base floor | base ≥ **TOS price ÷ 10** (so the price is reachable within 900%) **and** base ≥ **$0.35–0.50**. Below that floor the campaign is suppressed from eligibility: the price stays the same or rises while TOS impression share stays flat or falls. If the break-even CPC or ceiling is below $0.50, the lower number wins | [B6 R-M1, WB, PB — $0.50 is provisional: ask] |
| Base ceiling | base ≤ **PDP break-even CPC** (margin/unit × PDP CVR). Non-ranking campaigns: every placement ≤ 1.0 × its break-even CPC | [WB, register #3] |
| TOS ceiling (ranking) | **2 × break-even CPC** of the ranking term at TOS. This is an owner setting; the owner may raise it for a named term for a set time | [B6 R-P3, register #3] |
| Rounding | Boost is a whole percent. After rounding, `base × (1 + boost)` must match the target within **±$0.03**. If rounding would put the price above the ceiling, round the boost down | [PF gate 12] |

### 1.3 Bidding strategy effects

**Default: leave every existing campaign's strategy as it is.** New campaigns use dynamic bids – down only. Fixed bids come only through the fixed-bid trial (§8.1), with owner approval. Do not copy the engine behaviour that switches Fixed or Up & Down to Down-only automatically. Why: a strategy change alters CPC, placement and CVR all at once, so no read after it is clean. [register #8, B6 owner rule, PB]

| Strategy | What Amazon does | What it means for the written price | Ceiling check |
|---|---|---|---|
| **Dynamic – down only** | Lowers the bid in real time when a click looks less likely to convert | The written price is a **maximum**. Realised CPC is at or below it | `base × (1 + boost) ≤ ceiling` |
| **Dynamic – up and down** | Raises the bid up to +100% at top of search (Amazon also allows up to +50% elsewhere) and lowers it when conversion looks unlikely | The authorised TOS price is `base × (1 + boost) × 2.0` | `base × (1 + boost) × 2.0 ≤ ceiling`. If it breaches, re-solve `base = ceiling ÷ ((1 + boost) × 2.0)` or lower the boost; the strategy is not changed [SR SOP-47, PB] |
| **Fixed** | Uses the exact bid. No real-time adjustment; placement boosts still apply | The written price is what can be paid at every auction | `base × (1 + boost) ≤ ceiling` |

Read realised CPC against the written price. Under down-only, a realised TOS CPC well below the written price is normal, and it is not headroom to spend. [B6 metrics]

---

## 2. Placement-first diagnosis

Run this before any price decision on a ranking campaign, and on every campaign with ≥15 clicks in the window. Why: "only a few keywords can rank" often means "their bids are not clearing the top". [PF]

### 2.1 Portfolio sweep first

Before looking at any row, build these two tables for the product: [WB, PF]

1. **Campaign × placement table.** For every campaign: clicks, spend, orders, sales, CPC, CVR, revenue/click, and share of clicks, impressions and spend, for TOS, ROS and PDP separately. Add the current base, boost and TOS price, the TOS clearing CPC, TOS impression share, and the objective.
2. **Portfolio summary.** Distribution of boosts. Ranking campaigns with a **0% boost** (a defect). Ranking campaigns that do not isolate a term (several terms sharing one boost). Spread of the TOS:PDP price ratio, stated as numbers, e.g. "$5.85 vs $3.00, 1.95:1". Share of live keywords priced below their TOS clearing CPC. Clicks and spend by placement for the whole product.

A product-level roll-up alone is not enough. Keep the re-solve table (§6) beside the campaign table.

Observed in the source engagement (context, not a rule): a boost of 0% → 50% moved TOS click share from 3.8% to 72.7%; 50–99% → 100–199% added about 3 points; above 100% mostly buys auction share; above 200% was untested. [WB]

### 2.2 Per-campaign tests

| # | Test | Formula / rule | Output | Source |
|---|---|---|---|---|
| D1 | **TOS clearing CPC** | `clearing = TOS spend ÷ TOS clicks` (campaign placement row). Use the campaign's own value if TOS clicks ≥ 3, otherwise the portfolio value (the same fallback applies to revenue/click and PDP figures) | Price the top actually costs | [PF] |
| D2 | **Priced-out test** | `TOS price < clearing` → priced out: Amazon serves the ad where the bid clears, usually product pages | Shortfall per click = clearing − TOS price | [PF] |
| D3 | **Revenue per click by placement** | `placement sales ÷ placement clicks`. Use the advertised-product basket (7-day total sales, halo included) and state the halo rate | Diagnostic of value per click | [PF] |
| D4 | **Break-even CPC by placement** | `margin/unit of the advertised SKU × that placement's CVR`, using the conversion basis (own ≥50 clicks; linear blend 15–50; size or product rate <15). PF's `revenue/click × margin %` gives the same figure when one unit is sold per order and there is no halo; where they differ, the margin × CVR form governs | TOS, ROS, PDP break-even | [register #1–2, PF] |
| D5 | **Price vs break-even and ceiling** | Per placement: price under break-even / between break-even and ceiling / above ceiling. Above ceiling → cut to ceiling in this write (§3.2 P5) | Position of each price | [B6, register #3] |
| D6 | **Cost per order by placement** | `placement spend ÷ placement orders` | Non-ranking campaigns: this decides where money should shift. Ranking campaigns: reported only; the mix target governs, because PDP orders do not build the term's rank | [PF, B6 R-M1] |
| D7 | **Significance of a placement CVR gap** | `SE = √(p₁(1−p₁)/n₁ + p₂(1−p₂)/n₂)`; `CI95 = (p₁ − p₂) ± 1.96 × SE` | Verdict only if both n ≥ 30 **and** the interval excludes 0. Otherwise label it "directional" and justify any action on absolute economics. Never apply a blanket shift to the top across the portfolio | [PF, register #11] |
| D8 | **Placement mix** (ranking) | TOS share of clicks and PDP share of clicks, 30 days, on ≥15 clicks | Target 70–90% TOS and ≤20% PDP. PDP >20% → MIX FIX (§4) | [B6, WB] |
| D9 | **TOS impression share** | Our TOS impressions ÷ available | ≥30% together with a top-3 sponsored slot = "holding the top" | [B6] |

Example (B6, "bamboo sheets", 30 days): TOS 19.08% CVR on 306 clicks vs PDP 11.55% on 436. SE = 0.0272; CI95 of the gap = +2.2 to +12.9 points. This excludes 0, so it is a verdict: the top converts better. Cost per order was TOS $29.67 vs PDP $24.10, so PDP was cheaper per order. It is a ranking campaign, though, so the 56% PDP share still triggers a mix fix.

### 2.3 Decisions from the diagnosis

| Condition | Decision | Source |
|---|---|---|
| Ranking campaign in-budget < 70% of the day | Fix the budget first (§7.6). Every placement rate from a truncated campaign is invalid. 0% time-in-budget with $0 spend = missing data, not truncation | [PB, register #7] |
| **TOS-share pre-check**: ranking row with clicks at or above plan but **TOS < 30% of clicks** | **PLACEMENT FIX FIRST**: base down toward PDP break-even, boost up to hold (or reach) the TOS target, ROS re-solved, all in one pass. No price raise is judged until the mix is fixed | [PB, WB] |
| Priced out (D2) on a qualified push term | Lever pair: base down (mix fix §4) and TOS price up by the push rules (§3). Target the push price, not `clearing × 1.08` in one write. PF's one-shot jump is replaced by the daily step (register #5) | [PF, B6, register #5] |
| Clearing CPC > ceiling on a push candidate | WAIT: the term cannot hold the top at a profitable price. Owner decides on a time-limited ceiling raise | [B6 R-P1, F25] |
| Ranking campaign, PDP > 20% of clicks on ≥15 clicks | MIX FIX (§4), paired in the same write | [B6 R-M1] |
| Ranking campaign with 0% boost | Defect. Backward-solve (§6) | [WB] |
| Ranking row at TOS price above overlay | Cut to the ceiling (2 × break-even). PF's 1.30× overlay and 0.75× push levels are replaced by register #3 | [register #3] |
| Visibility-quadrant syntax (CTR fails, CVR passes) | Use TOS impression share to find the cause: IS < 5%, TOS IS < 15% and rank > 4 → placement and auction (price step, then boost, then base under the bleeding placement); TOS IS < 15% and rank ≤ 4 → placement only (boost); TOS IS 15–30% → moderate gap (boost); TOS IS > 30% → listing issue (no bid change). No IS and no rank → undetermined, no CTR-driven bid change. Step sizes follow §3 and register #5 | [SR B1] |
| Non-TOS placement with a modifier > 0 that bleeds (0 orders on ≥ 3 clicks, or spend share > 1.5 × sales share and > 30%, or ACoS above break-even) | That placement modifier → 0%. Moves of ≤ 2 points are noise. Runs on deal days too (a bleed stop) | [SR, register #16, #27] |

---

## 3. Pricing a push term

A term is pushed only if it passed the push qualification in `06-campaign-ppc-decisions.md`: the product goal allows ranking spend; it converts at or above market at the top; it is within about 30 places of target; the advertised variation is Green with cover ≥ days to next arrival + 7; the keyword and campaign are live; the ceiling ≥ our TOS CPC; and the listing is not flagged. A term that fails any of these is WAIT, not PUSH. [B6 R-P1, register #9]

### 3.1 Formulas

| Quantity | Formula | Source |
|---|---|---|
| Break-even CPC | `margin/unit (advertised SKU, price in force) × TOS CVR (conversion basis)` | [B6 R-F2, register #1–2] |
| Premium | rank ÷ target ≤ 1 → HOLD RANK (no push). 1 < ratio ≤ 1.5 → **+25%**. Ratio > 1.5 → **(rank ÷ target − 1) × 50%** | [B6 R-P2, WB, register #4] |
| Push price | `break-even × (1 + premium)`, capped at the ceiling | [B6 R-P2] |
| Ceiling | `2 × break-even`. Cost per order at the ceiling ≤ 2 × margin, which is below the order value | [B6 R-P3, R-F3] |
| Holding the top | Top-3 sponsored slot most hours **and** ≥ 30% TOS impression share | [B6 R-P6] |

With the ceiling at 2 × break-even, any premium above +100% is capped. WB's +400% premium cap only matters if the owner raises a named term's ceiling. [register #4]

### 3.2 Price-path rules (apply in order, every day of the push)

| # | Condition | Action | Source |
|---|---|---|---|
| P5 | Today's TOS price > ceiling | **Cut to the ceiling now**, in this write. Never deferred | [B6 R-P5, F05] |
| P8 | Rank ≤ target | **HOLD RANK**: keep today's price, no raise. Rejoin the push if the term slips past target. After 2 clean weeks at target, taper per `06` (about −10%/week to 5–10¢ under the placement's blended CPC; restore on a slip of > 2 places in the top 5, or any slip below target) | [B6 R-P8, register #26] |
| P7 | TOS CVR < market CVR on **50+ TOS clicks** | **STOP** the push. Back to break-even (§5 path). Extra auctions are worse ones | [B6 R-P7] |
| P6 | At the ceiling **3 days** without holding the top | **CHECK OWNER**: raise the ceiling for a set time, or swap the term. Money alone is not working at a profitable price | [B6 R-P6, E5] |
| P4 | Price < push price, or not holding the top while below the ceiling | Raise **≤ +30% of today's price per day**, never above the ceiling | [B6 R-P4, register #5] |
| — | Holding the top below the push price | Hold. Do not pay for rank that is already bought | [B6] |
| — | Rank fell > 10 places in 30 days while getting clicks | Freeze price moves (except P5) and find the cause: colour, listing, keyword state, competitor | [B6 E4, PB state E] |
| — | Deal day | Push pricing only as the approved push plan says; no judging on deal data | [B6 E1] |

Recompute break-even and ceiling every run from current margin and CVR. Never use last cycle's ceiling. Why: the conversion basis moves as clicks accumulate, and a variation switch changes the margin. [B6 F23, PB]

### 3.3 Worked example (generic)

Advertised SKU margin $20.00/unit. Own TOS CVR 18.0% on 80 TOS clicks (≥ 50, so own rate). Rank 30, target 10. Current base $1.60, boost 150% → TOS price $4.00. Holding the top: no.

| Step | Arithmetic | Result |
|---|---|---|
| Break-even | $20.00 × 18.0% | **$3.60** |
| Ceiling | 2 × $3.60 | **$7.20** (cost per order at ceiling $7.20 ÷ 18% = $40 = 2 × margin) |
| Premium | 30 ÷ 10 = 3.0 > 1.5 → (3.0 − 1) × 50% | +100% |
| Push price | $3.60 × 2.00 = $7.20, cap $7.20 | **$7.20** |
| Day 1 | $4.00 × 1.30 | $5.20 (boost 225% at base $1.60) |
| Day 2 (still not holding) | $5.20 × 1.30 | $6.76 (boost 323%) |
| Day 3 (still not holding) | $6.76 × 1.30 = $8.79 → capped | **$7.20** (boost 350%) |
| Days 3–5 at $7.20, not holding | P6 | CHECK OWNER: time-limited ceiling raise or swap |
| If holding on day 2 | P4 no longer fires | Hold $6.76 |
| If, at 50+ TOS clicks, TOS CVR 9% vs market 11% | P7 | STOP. Back to break-even $3.60 (§5) |

Closer term: rank 11, target 8 → ratio 1.375 → +25% → push price $4.50. From $4.00, day 1 → $4.50. If the term is still not holding the top, P4 lets it keep stepping (≤ +30%/day) toward the $7.20 ceiling.

Example (B6, "bamboo sheets"): King White margin $15.97 × own TOS CVR 19.1% (1,352 TOS clicks, 90 days) = break-even $3.05, ceiling $6.10. Rank 26 vs target 9 → premium (26/9 − 1) × 50% = +94% → push price $5.93. Today's price was $6.10: at or above the push price and under the ceiling, so it held at $6.10. It was at its ceiling with 2.4% TOS impression share, so it went to the owner under P6.

---

## 4. Mix fix (product pages over 20%)

### 4.1 Trigger and moves

| # | Rule | Source |
|---|---|---|
| M1 | **Trigger**: ranking campaign, PDP > 20% of clicks on ≥ 15 clicks (30 days) | [B6 R-M1, WB] |
| M2 | **Base −50%**, or **−25%** if product pages bring orders (≥ 1 PDP order in the window) | [B6 R-M1] |
| M3 | **Boost raised in the same write** so the TOS price holds, or reaches today's allowed push step. `new boost = (TOS target ÷ new base − 1) × 100`, ≤ 900% | [B6 R-M1, F07] |
| M4 | **Floor**: new base ≥ TOS target ÷ 10 and ≥ $0.35–0.50. If −50% or −25% would break the floor, cut only to the floor | [B6, WB] |
| M5 | **At the 900% cap** (target price > base × 10): raise the base only to `price ÷ (1 + boost)`, with the boost set in the same write. Choose a boost below 900% that reaches the price. Never credit a capped step with new clicks | [B6 R-M2, F08] |
| M6 | **TOS never falls as base-cut residue**: a base cut without a boost re-solve lowers the TOS price. That is forbidden unless the TOS price itself is meant to fall (over ceiling, or the §5 path). Rebuild formula: `boost = (TOS price ÷ new base − 1) × 100` | [WB, SR] |
| M7 | **PDP only via base.** Do not use a product-page modifier to steer PDP spend | [WB, PB] |
| M8 | **Boost raise refused** on a ranking campaign with PDP > 20% unless the base cut is in the same write (F07: a boost alone buys nothing if the campaign is not winning the top) | [B6 F07] |
| M9 | **Re-check after 7 days**: PDP share, TOS share, TOS impression share. Still > 20% → next base step, ≤ 50%. At the base floor with PDP still > 20% → CHECK OWNER: fixed-bid trial candidate (§8.1). A strategy change needs approval | [B6, WB, register #8] |
| M10 | Base above the PDP break-even CPC after the step → it keeps stepping down on later cycles (≤ 50% per step) until base ≤ PDP break-even | [WB, E17] |

WB's alternative step sizes (30% if PDP > 30%, else 15%) and its "TOS climbs ≤ 0.5 × new base per write" are not used. The B6 −50%/−25% mix fix and the +30%/day push step apply. [register #5]

### 4.2 Rest of search: lifted only when earned

- ROS runs **at base** (modifier 0%) until the campaign has **≥ 15 ROS clicks converting ≥ the campaign's PDP CVR**. This also applies to TOS on non-ranking campaigns and to every placement on Phrase, Broad, product-targeting and discovery campaigns. [WB, PB]
- Once earned: `ROS price = base + (ROS ceiling − base) × min(1, CVR_ROS ÷ CVR_PDP − 1)`, where ROS ceiling = margin/unit × ROS CVR (1.0 × break-even; never the ranking allowance). `ROS modifier = (ROS price ÷ base − 1) × 100`. [WB]
- It resets after a variation re-route (new SKU, new rates). [PB]

### 4.3 Combined write rule

One campaign gets one write per cycle. That write carries every lever the backward-solve (§6) sets: base, boost, ROS modifier and budget. The pair is written together or not at all. [B6 F07, F14, PB independence exception]

| Situation | TOS price after the write | Base | Boost |
|---|---|---|---|
| Mix fix only (term at HOLD RANK, non-push, or holding the top) | = today's (held) | −50% / −25% | re-solved to hold |
| Mix fix + push step (funded, not holding the top, below ceiling) | today's × ≤ 1.30, ≤ ceiling | −50% / −25% | re-solved to the new price |
| Mix fix + over ceiling | = ceiling | −50% / −25% | re-solved to the ceiling |
| Mix fix + non-push ranking above break-even | §5 target (break-even or −50% step) | −50% / −25% | re-solved |
| No mix trigger | per §3 / §5 | unchanged | re-solved |

### 4.4 Worked example (generic)

Ranking campaign, 30 days: 120 clicks, of which TOS 60 (50%), ROS 12 (10%) and PDP 48 (40%, 3 orders, CVR 6.25%). Margin $20.00. TOS break-even $3.60, ceiling $7.20. Base $1.80, boost 150% → TOS $4.50.

| Case | Arithmetic | Write |
|---|---|---|
| Term at HOLD RANK | PDP 40% > 20% on ≥ 15 clicks; PDP sells → base −25% = $1.35. Boost = 4.50 ÷ 1.35 − 1 = 233%. Check: 1.35 × 3.33 = $4.50. Floor 4.50 ÷ 10 = $0.45 ≤ $1.35 | Base $1.35, boost 233%, TOS $4.50 held |
| Term in funded push, not holding the top | Same base; TOS $4.50 × 1.30 = $5.85 ≤ $7.20. Boost = 5.85 ÷ 1.35 − 1 = 333% | Base $1.35, boost 333%, TOS $5.85 |
| ROS | 12 ROS clicks < 15 → not earned | ROS modifier 0% (runs at $1.35) |
| ROS if earned (18 clicks, CVR 11%) | ROS ceiling 20 × 11% = $2.20. Ratio 11 ÷ 6.25 = 1.76 → min(1, 0.76) = 0.76. Price 1.35 + 0.85 × 0.76 = $2.00. Modifier 48% | ROS +48% |
| Next cycle | PDP break-even = 20 × 6.25% = $1.25 < base $1.35 | Next base step after the 7-day re-check |

Example (B6, "bamboo sheets queen size"): break-even $3.90 (Queen White $19.51 × 20.0%), ceiling $7.80. Rank 22 vs target 5 → premium +170% → push price capped at $7.80. PDP 61% of clicks, and PDP sells, so base −25%: $1.37 → $1.03. Push step $5.93 × 1.30 = $7.71. Boost 333% → 649% (1.03 × 7.49 = $7.71), all in one write. Example (B6, R-M2, "bamboo sheets king size"): base $0.50 with boost 860% gives $4.80, near the cap. It was rewritten as base $0.60 + boost 700% = $4.80 (0.60 = 4.80 ÷ 8.00) and held at WAIT for a listing check.

---

## 5. Non-push ranking terms: down to break-even

These are ranking campaigns that are not in the funded push (WAIT, stopped, or out of focus). They are priced to break-even, gradually where there is rank to protect. [B6 R-B1–B4]

| # | Condition | Action | Source |
|---|---|---|---|
| B0 | Price > ceiling (2 × break-even) | Cut to the ceiling now, then apply the rules below from the next cycle | [B6 R-P5] |
| B4 | < 15 clicks (30 days) | Hold (formula-only corrections if above the ceiling) | [B6 R-B4, E3] |
| B1 | Price > break-even and **0 TOS clicks** (30 days) | **Straight to break-even.** There is no measured rank to protect | [B6 R-B1] |
| B2 | Price > break-even **with** TOS clicks | Step down: `new price = max(break-even, price × 0.50)` per step | [B6 R-B2] |
| B2r | After a step, rank falls **> 10 places** | Restore one step | [B6 R-B2] |
| B3 | Price ≤ break-even | Hold. Any raise waits for the next clean audit; **no raises during events** | [B6 R-B3] |
| — | Rank fell > 10 places in 30 days (before the step) | Freeze the step; find the cause first (E4) | [B6 E4] |
| — | Deal days | Cuts allowed; no raises | [B6 R-B1 exception, R-B3] |

Examples (B6): "Queen Sheets Set Bamboo" had 1 TOS click and 98.6% PDP. Price $4.72: a −50% step gives $2.36, which is below break-even $3.17, so it landed at $3.17. Base −25% ($1.65 → $1.24, PDP sells) and boost 186% → 156% (1.24 × 2.56 = $3.17) went in one write. "King Size Bamboo Sheets Set" had a healthy mix (87% TOS): $5.85 → break-even $3.99 (−32%, inside the 50% step), with base $1.50 held and boost 290% → 166%.

---

## 6. Backward-solve procedure (one write per campaign)

A campaign's base and modifiers are one decision. Solve them from target prices; do not pick them. [PB, WB, PF]

### 6.1 Steps

1. **Targets first.** For each placement, set the target price from its rule:
   - TOS: push price or step (§3), hold (P8), break-even path (§5), or cut to ceiling.
   - ROS: base unless earned (§4.2).
   - PDP: = base, ≤ PDP break-even.
2. **Set the base** = the lowest of: today's base after any mix-fix step (§4), the PDP break-even CPC, and the ROS target when ROS is not earned. Then apply the limits: ≥ TOS target ÷ 10, ≥ $0.35–0.50 (unless the ceiling is lower), cut ≤ 50% per step. **Name the binding bound** in the row (PDP break-even / floor / step cap / 900% cap). [WB, B6]
3. **Re-solve the modifiers**: `boost = (TOS target ÷ base − 1) × 100`, clamped to 0–900. `ROS modifier = (ROS target ÷ base − 1) × 100`, or 0 when not earned.
4. **Cap hit?** If the boost needs to exceed 900%, apply §4.1 M5: raise the base only to `TOS target ÷ (1 + boost)`. That raises the PDP price too, so the base must still be ≤ PDP break-even. If it cannot be, hold the price reachable at 900% and flag the row (E16).
5. **Strategy check**: under up & down, the authorised TOS price is ×2.0 and must be ≤ ceiling (§1.3).
6. **Verify**: `base × (1 + boost)` = TOS target ± $0.03. TOS ≤ ceiling. Step caps respected (§9.3). A base cut on a mix-fix campaign is paired with a boost re-solve.
7. **Budget** from the new prices (§7).

Launch pricing for new or restarted exact campaigns uses the same solve. Targets come from break-even maths with the conversion basis below 15 clicks (size or product rate), not from Amazon's suggested bids. Harvested terms and restarts of non-push campaigns start at break-even. [register #18, B6 R-K4, R-S2]

### 6.2 One campaign modifier across several keywords

One boost serves every keyword in a campaign. Solve for a **feasible band** of boosts that lets every funded keyword reach its TOS target without any keyword passing its ceiling. [PF]

- **Keyword bids can move this cycle:** pick one boost *m*, then set each bid `b_k = T_k ÷ (1 + m)`. Check every `b_k` against its own PDP break-even (upper bound) and its floor (≥ T_k ÷ 10, ≥ $0.35–0.50). The band of feasible *m* is where every keyword passes both.
- **Keyword bids held this cycle** (step caps, thin data): `m_low = max_k (T_k ÷ b_k) − 1`, `m_high = min_k (C_k ÷ b_k) − 1`, where C_k is keyword k's ceiling. Feasible if `m_low ≤ m_high`.
- **No feasible band:** set the boost to the highest value at which no keyword breaches its ceiling (`m_high`). Flag the campaign for a split into single-term campaigns. Never silently take one keyword's answer.
- Non-push keywords in a push campaign must not be carried above their own ceilings by the push boost. That is part of the band. [PF, register #3]

### 6.3 Orphan-modifier check (both directions)

Run it on the finished write set; each list must be empty. [PF gate 20]
- **Orphan modifier:** a boost change that no funded keyword in the campaign needs.
- **Orphan keyword:** a funded push keyword whose TOS target is not reachable at the campaign's written boost and its own bid.
- Also flag: a ranking campaign left at 0% boost, and a boost raise with no budget change when the budget is truncated. [WB]

---

## 7. DSTR → required clicks → budget → spend limit

Budgets are outputs of the chain: rank target → sales needed → clicks → price → budget. They are never set by feel, and never by a TACoS rung. [LTSF standards, B6 F24]

### 7.1 Required clicks (resolved method — register #19)

| Step | Formula | Rule | Source |
|---|---|---|---|
| DSTR | Daily sales needed at the target rank (Data Rova DSTR or competitor sales at the target rank; total, organic + paid) | `DSTR = max(1, ceil(stated))`. Blank → UNSIZED (no push budget) | [PF, SR B9, WB] |
| Feasibility | Market daily purchases = SQP market purchases ÷ 30 | Stated DSTR > market daily → the period was misread: re-scope to market daily × 0.25. This sets the level only and **never strips the Ranking objective**. If the market cannot support 1 sale/day → flag, and treat the term as a conversion term | [PF, SR] |
| Organic | Our current organic sales on the term. When not measured: `DSTR × organic traffic share` | Label it **PROXY** on every row | [PF] |
| Paid | `max(DSTR − organic, 0)` | organic + paid = DSTR (± 0.02) | [PF] |
| Required TOS clicks/day | `ceil(paid ÷ own achieved TOS CVR)` | Achieved CVR from the conversion basis, **never** a target or planning CVR. No rank ladder on top of netting (that double counts) | [register #19, PF] |
| Reconcile | Σ required units across push terms vs what the product sells | Requirements set **volume and budget, never price**. If the sum is unrealistic, scale the terms to the product | [B6 F21] |

Front-loading: organic share is measured at today's rank. During the climb the paid need is higher than the steady-state figure, and it tapers as rank arrives. Note this on every row. [PF]

### 7.2 Budget per push term

`Push budget = ceil(required TOS clicks × TOS price × 1.05 + expected non-TOS spend)`

- Expected non-TOS spend = today's ROS and PDP clicks per day × the new base (× ROS modifier where earned). This is the product-page spend the base still buys. [B6 "plan clicks × price + product-page spend", register #19]
- Use the post-solve TOS price. Round up (`ceil`), never `round()`. [PF]
- A push capped by price rather than money cannot use more budget. More budget does not buy the top below the ceiling; the lever is the owner's ceiling decision (P6). [B6]

### 7.3 Worked example (generic)

Stated DSTR 6.4 → 7. Organic traffic share 30% → organic 2.1 (PROXY) → paid 4.9. Own TOS CVR 20% → 24.5 → **25 TOS clicks/day**. TOS price $5.00 → 25 × 5.00 × 1.05 = $131.25. PDP 6 clicks/day × base $1.00 = $6.00. **Budget $138/day.**

### 7.4 Loss ceiling and projected cover

- **Loss ceiling** = (push ACoS − break-even ACoS) × projected sales at the required spend, stated weekly with its basis. Push ACoS = TOS price ÷ (TOS CVR × AOV). Cross-check it as (CPA − margin) × paid orders. Hitting it = human flag, not an automatic stop. [PB, WB]
  - Example: price $5.00, CVR 20%, AOV $70 → CPA $25, push ACoS 35.7%. Break-even ACoS 20 ÷ 70 = 28.6%. Sales/day 25 × 20% × $70 = $350 → loss $25/day, which equals ($25 − $20) × 5 orders. **$175/week.**
- **Projected days of cover** through the checkpoint = (available + dated inbound on its ETA) burned at baseline velocity + the push's order gap. It must stay Green. Dropping into Yellow (< 60) or Red (< 21) blocks the push: shrink the gap, wait for inbound, or get an explicit time-boxed owner acceptance. Red is never accepted. Use the 30-day pace, never the inflated push pace. [PB, WB, B6 F30, register #9]

### 7.5 Funding order when budget room is short

1. **Order the funded list** by revenue potential at target rank ÷ cost to close the gap. Tie-breaks: DSTR ↓, days of cover ↓, CVR ↓. Only qualified terms enter; Yellow/Red variations never do. [PB, WB]
2. **Room** = spend limit − expected other spend. Expected other spend is the run-rate spend of every other enabled campaign, moved by this write's price changes (§9.1). It is never the budget caps. [WB, B6 F03]
3. **Plan budget per term** = plan clicks × price + product-page spend (§7.2).
4. **If Σ push budgets > room:** leave terms with budgets ≤ $100 at full plan. Apply one scale factor to the terms above $100: `s = (room − Σ budgets ≤ $100) ÷ Σ budgets > $100`, capped at 1. Each big term's budget = `ceil(plan × s)`. Check: push budgets + expected other spend ≤ limit. [B6 R-F5, E19]
5. **If still over, or s would be too small to buy a clean read:** drop terms from the bottom of the list (they become WAIT, "unfunded", with the shortfall stated). Never cut price to fit budget. [B6 R-F6, WB]
6. **Weekly:** if margin after ads falls below the owner's rule, cut the push from the bottom of the funded list. [B6 R-F6]

Example (B6, deal days 29–30 Sep): the full plan was $1,317/day against a $1,300 limit. After expected other spend, the three biggest terms were scaled to 45% ("bamboo sheets": 69 plan TOS clicks/day at $6.10 → $201 budget). Expected spend still sat far under the limit, because 11 of 13 funded terms were at or within 5% of their ceiling: the push was capped by price, not money.

### 7.6 Budget rules outside the push

| Rule | Value | Source |
|---|---|---|
| Budget truncation | In-budget < **70%** of the day → all rates truncated → budget first, before any bid verdict. 0% with $0 spend = missing data | [PB, register #7] |
| Utilisation targets | Ranking **80%+**, Discovery **70%+**, Defensive **100%** (fix utilisation before touching bids) | [PB, B2] |
| Clicks above plan with rank improving | Hold price. Budget rises only if the plan's clicks are truncated and the spend limit allows | [register #6] |
| Minimum budget | Raise any budget < **$10/day** to **$10** | [SR, register #32] |
| Approval | Any budget change **> $50/day** → owner approval (Change Review Sheet) | [PB, register #32] |
| High budget | Budget > $500/day → refer for review | [SR] |
| Roster minimums > cap | Pacing plan (release 3–5 campaigns a week inside the cap, highest value first) | [PB check 18] |
| Pairing | Price and budget rows load together or not at all; a funded push term always has its budget | [B6 F14] |

---

## 8. Fixed-bid trial, graded push, discovery pricing

### 8.1 Fixed-bid trial (the only route to a strategy change)

| Item | Rule | Source |
|---|---|---|
| Trigger | CPC materially above the ceiling **and** low clicks (suppression signature). Also fires on a row already corrected to the ceiling whose clicks stay low, and on a mix-fix campaign at the base floor with PDP still > 20% | [PB §8, WB] |
| Pre-step | The price correction to the ceiling lands before or with the switch. Every formula correction is checked next cycle for suppression (TOS price the same or up while TOS impression share is flat or down) | [PB, WB] |
| Action | Switch to Fixed at the **same price, match type and negative wall**. Owner approval required | [PB, register #8] |
| Judge | At **15 clicks** | [PB] |
| Caps | Single-keyword campaign: **$10–15/day** budget cap. Multi-keyword: no cap, **7–8 day** review | [PB, WB] |
| Scope | Any objective | [PB] |

### 8.2 Graded push (non-ranking rows, and ranking rows after the sufficiency stop) — provisional: ask before first use

| Tier | Evidence | Move |
|---|---|---|
| CONFIRMED | ≥ 15 clicks, ≥ 2 orders, CPA ≤ ~70% of ceiling | Hold |
| STRONG | ≥ 30 clicks, ≥ 3 orders, CPA ≤ ~60% of ceiling | Up to +10% |
| PROVEN | ≥ 50 clicks, ≥ 5 orders, CPA ≤ ~50% of ceiling | Up to +15% |

Non-ranking ceiling = 1.0 × break-even CPC at every placement. These tiers size a raise that the scale test in `06` allows (ACoS ≤ 50% of break-even with orders → SCALE, ≤ +25%/cycle). The tier sets the step within that limit. CPA > 8 × ceiling may take a 50% cut. [PB, WB, register #5, #16]

### 8.3 Discovery pricing

| Item | Rule | Source |
|---|---|---|
| Candidacy | Reactive: **≥ 100 exact clicks** on the term's own history (near-miss about 20). Proactive: a syntax coverage gap (e.g. primary root at 0% phrase). State which path | [PB, register #23] |
| Existing instance | Check for an existing Broad/Phrase/Auto instance before building (restart beats build) | [PB, B6 R-S2] |
| Price | **Broad ~60%, Phrase ~80% of the exact ceiling.** Here "exact ceiling" = the exact term's break-even CPC (discovery never gets the ranking allowance). Relevancy tier sets the position: highly relevant → upper end, semi-relevant → lower | [PB, register #23, WB] |
| Modifiers | **No placement modifier at launch.** Modifiers are earned by the §4.2 rule | [PB, WB] |
| Cheaper-order test | Launch Phrase/Broad on a term only if its proven non-branded cost per order is below the exact average. These layers buy coverage, not rank | [PF] |
| Variation | Discovery advertises the size's clearance variation | [B6 R-C2, register #29] |
| Judgement | From 15 clicks | [PB] |
| Timing | No launches on deal days | [B6 E1] |

---

## 9. Day-1 spend forecast, event days, and the price checks

### 9.1 Expected spend on day 1

Forecast from today's spend moved by the new prices. Do not use budget caps, and do not credit extra clicks for price steps. [B6 F20, WB]

`expected spend = TOS spend/day × (new TOS price ÷ old TOS price) + (ROS + PDP spend/day) × (new base ÷ old base)`, each ≤ the campaign's new budget.

- Use a settled baseline: exclude deal days and the 7-day attribution-settle days. [B6 F03, E2]
- Paused keywords, retagged rows and capped steps (boost at 900%) earn **0** extra clicks. [B6 F20, R-M2]
- Any uplift or elasticity coefficient must be named as soft and tied to when it will be measured. [PB check 22]
- Shared multi-product campaigns: product share = row spend × (product tile ÷ rows). They are excluded from this product's price automation. [B6, E13]
- Total: Σ expected spend (push + other) ≤ spend limit. Report expected vs limit on the Overview. [B6 R-F5]

### 9.2 Deal and event days

| Rule | Source |
|---|---|
| Compute deal-state margin, break-even and ceiling from the deal price **before** the event. In-deal CVR never justifies a price above the deal-state ceiling | [PB, register #27] |
| Deals amplify an already-decided, gated push; they never originate one | [PB] |
| Any deal-day spend limit is an explicit, dated, time-boxed exception with its margin stated (e.g. B6: $1,300/day on 29–30 Sep at ~7% margin after ads vs the 10% rule). A single event week may run up to +50% over the derived envelope, pre-approved and never retroactive | [B6 R-F5, PB] |
| Budget caps are set in advance; dayparting boosts are removed for the window; the plan is staged against max-sales-day cover | [PB event mode] |
| Pacing is checked the same day against the event's projection. A pace > ~25% off the day-of-week curve is flagged | [PB] |
| On deal days: no ACoS/CVR verdicts, no launches, no folds or structure; cuts allowed; **no raises on non-push ranking**; bleed stops still run | [B6 E1, R-B3, SR, register #27] |
| After the event: 7-day attribution settle; deal weeks are excluded from trend reads for 2 weeks; floors, ladders and ceilings return to pre-event values unless the event produced real evidence | [B6 E2, PB, SR] |

### 9.3 Price checks the quality gate runs (each must return 0)

| # | Check | Source |
|---|---|---|
| Q1 | Any TOS price (`base × (1 + boost)`, × 2.0 under up & down) above its ceiling: 2 × break-even for ranking, 1.0 × break-even at every placement for non-ranking | [B6 R-P3/R-P5, register #3] |
| Q2 | Any boost > 900% or < 0% | [B6, CB] |
| Q3 | Any base below TOS price ÷ 10, or below $0.35–0.50 (unless the ceiling is lower) | [B6 R-M1, WB] |
| Q4 | Any base cut > 50% in one step. Any non-ranking over-break-even cut > 30% of base, unless it is a decisive bleed or zero-order cut (≤ 50%) | [B6 E17, R-N1, register #5, #16] |
| Q5 | Any push raise > +30% of today's price in one day. Any other raise > +25%/cycle | [B6 E17, register #5] |
| Q6 | Any raise on a non-push ranking term during an event | [B6 R-B3] |
| Q7 | `base × (1 + boost)` ≠ written target ± $0.03 | [PF gate 12] |
| Q8 | Base cut on a ranking campaign that lowers its TOS price without a rule that lowers it (base-cut residue). Boost raise on a campaign with PDP > 20% without the paired base cut | [WB, B6 F07] |
| Q9 | Ranking campaign in the push at a 0% boost. Orphan modifier or orphan keyword (§6.3) | [WB, PF] |
| Q10 | ROS or non-ranking TOS modifier > 0 without ≥ 15 placement clicks converting ≥ PDP CVR | [WB, PB] |
| Q11 | Price change on a paused keyword/campaign or a withheld duplicate. Price move under 15 clicks other than a cut to the ceiling | [B6 E6, E3, PB] |
| Q12 | Bidding strategy changed outside an approved fixed-bid trial | [register #8] |
| Q13 | Push budgets + expected other spend > spend limit (events stated with dates). Any push budget < `ceil(required clicks × price × 1.05)` that is not a stated scale-down. Any budget < $10. Budget change > $50/day without approval | [B6 R-F5, PF, SR, PB] |
| Q14 | Funded push term with no budget row. Price row loaded without its budget pair | [B6 F14] |
| Q15 | Capped step (900%) credited with new clicks in the forecast | [B6 R-M2, F20] |
| Q16 | A price write without a ceiling basis, a reversal condition and a re-read date | [SKILL quality gate] |

---

## 10. Open questions for the owner

1. **Base cut cap vs over-ceiling base.** If the base is more than 2× the PDP break-even, the "over ceiling → straight to ceiling" rule and the "base cut ≤ 50% per step" block (E17) disagree. This file applies the 50% cap and steps down over later cycles (§4.1 M10). Confirm.
2. **"Exact ceiling" for discovery pricing.** The source prices Broad/Phrase at ~60%/~80% of "the exact ceiling". This file reads that as the exact term's break-even CPC (the non-ranking cap), not the 2× ranking ceiling. With the ranking ceiling, Broad would price at 1.2 × break-even. Confirm.
3. **Projected-cover threshold for a push.** The plan-builder blocks a push whose projected cover drops into Yellow (< 60 days). The workbook-builder only requires > 21 days. This file blocks on Yellow unless the owner gives an explicit time-boxed acceptance. Confirm.
4. **Funding order.** B6 funds "in priority order" without defining the order. This file uses the plan-builder's order (revenue at target ÷ cost to close) with the workbook-builder's tie-breaks (DSTR, cover, CVR). Confirm, or give the B6 order.
5. **Approval for push steps.** The plan-builder requires human confirmation for any bid move > 25%, but the push step is +30%/day. This file treats an approved push plan as confirmation of its daily steps. Confirm.
6. **Terms whose market cannot support 1 sale/day.** One engine routes these out of Ranking, while placement-first says feasibility never strips the objective. This file applies the strip only when the whole market is < 1 purchase/day and applies the re-scope otherwise. Confirm.
