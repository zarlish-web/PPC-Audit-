# Amazon Product Analysis — quick-start edition

The workflow, principles, owner defaults, master decision order, output contract and open owner decisions (~25 KB). For the full rulebook (every threshold, formula, template and the worked case) use AMAZON_PRODUCT_ANALYSIS_FRAMEWORK.md or install the .skill.


# Amazon Product Analysis — the consolidated framework

This skill turns raw product data into decisions a reviewer can follow from input to validation. The bar is: **every decision is derived from the product's own numbers, placed in its competitive context, bounded by explicit guardrails, and falsifiable on a named date.** A surface-level audit (lists of metrics, generic advice, "consider optimising bids") is a failure.

It consolidates 18 existing skills and one real engagement (B6 bamboo sheets, Sep 2026). Where those sources disagree, this skill states one default and records the alternative in `references/13-source-map-and-conflicts.md`. Owner settings (the dials a product owner may change) are in the table below — **ask for them, don't assume them.**

## How to use this skill

1. **Classify the request** (ask once if unclear):
   - **Analysis** — diagnose what exists (audit an engine run, a product, a campaign set). Staleness is a finding, not a blocker.
   - **Plan** — decide what to do next (from scratch, or **refinement** of an existing plan: grade prior actions first).
   - **Scope** — full product (default) or one area (keywords only, competitors only, inventory only…). A one-area request still runs Phase 0–2, because every area depends on economics and inventory.
2. **Run the phases in order** (below). Each phase names the reference file to read at that point — read it then, not all up front.
3. **Deliver the output contract** (Phase 10) and pass the quality gate before you present anything.

## Principles (why the rules look the way they do)

1. **Nothing is guessed.** Missing input → ask, or record a named gap and the decisions it blocks. Missing value → blank, never 0. Unmeasured ≠ zero (a competitor with no export is unknown, not absent).
2. **Per-SKU economics decide money.** Break-even comes from the advertised variation's own margin at the price in force (deal price during a deal) — never a blended parent, category average or another product's number.
3. **Objective first, then the lever.** A campaign has one objective, set by its targeting. It is judged on that objective's metric (rank for ranking, CPA for conversion, share for defence, graduation for discovery) — never on another's.
4. **Gates before performance.** Data validity → goal → economics → inventory → structure → sample size → delivery → quality → objective loop. The first gate that fires decides the row.
5. **Placement-level, not blended.** Top of search, rest of search and product pages each have their own CVR, CPC and ceiling. Blended numbers hide the problem.
6. **Gradual, bounded, reversible.** Small steps with caps; every step has a ceiling, a reversal condition and a re-read date. One lever per row per cycle unless one backward-solve sets several.
7. **Context before verdict.** A number means something only against: its own history, the market (SQP/competitors), the objective, the stock position, and events (deals, season, price changes).
8. **Competitor data informs; it never sets a price.** It decides which terms, which order, which targets, how to judge progress — prices stay break-even-based.
9. **Longitudinal.** Before a new decision, check whether the last one was executed and whether it worked. A lever that failed twice is escalated, not repeated.
10. **Plain, traceable writing.** Every verdict cites the numbers doing the work, the arithmetic, why this lever and not the adjacent one, what would reverse it, and when it is re-read. No internal codes in delivered text.

## Owner settings — house defaults (confirm per product; record answers)

| Setting | Default | Source / note |
|---|---|---|
| Product goal | **Must be declared**: Growth/Scale · Mixed · Profit-First · Clearance/LTSF. Undeclared → treat as Profit-First for the ranking gate | plan-builder |
| Margin source | Sellerboard profit per unit before ads, per SKU/colour, last 30 days; deal price during deals | B6, SR |
| Break-even ACoS | CM2 = (ASP − COGS/unit − Amazon fees/unit) ÷ ASP, no returns; flag if outside 5–70% | SR (locked) |
| Break-even CPC | margin/unit × conversion rate of the placement being bought | all |
| Conversion basis | own placement CVR from 50 clicks (90 d); blend own↔size 15–50; size/product rate below 15 | B6 |
| Ranking ceiling | **2 × break-even CPC** (alt: flat account cap ~$8–9) | B6 / plan-builder |
| Push premium | +25% if rank ÷ target ≤ 1.5, else (rank ÷ target − 1) × 50%, capped at ceiling | B6 |
| Step limits | push: ≤ +30%/day while not holding top · other raises ≤ +25%/cycle · cuts ≤ 15%/cycle (gradual), ≤ 50% base per step; over-ceiling → straight to ceiling | B6, SR, PB |
| Bidding strategy | leave existing strategies as they are; new campaigns dynamic down-only; fixed bid only via the fixed-bid trial | B6, PB |
| Amazon suggested bids / "market price" | **not used** to set prices (context only if owner allows) | B6 owner rule |
| Spend limit | owner-set daily/weekly $ for the product; event exceptions stated with dates and margin | B6 |
| Margin rule | owner-set (e.g. keep product margin after ads ≥ 10%); exceptions time-boxed | B6 |
| TACoS | monitored and decomposed; **no numeric TACoS target unless the owner sets one** | B6 owner rule; PB bands as reference |
| Inventory zones | Green ≥ 60 days of cover · Yellow 21–59 · Red < 21; "stock-out before inbound arrives" overrides all | PB, inventory-checkup |
| Sample floors | bid verdict 15 clicks · CVR verdict 100 clicks (own TOS CVR usable from 50) · CTR verdict 1,000 impressions · product targets 11 clicks | PB, SR |
| Zero-order rule | ≥ 20 clicks, 0 orders → REDUCE (relevant, live owner) / REVIEW fix queue (relevant, no owner) / BLOCK (irrelevant or other product); never negate exact ranking or brand terms | B6, STR audit |
| Holding the top | top-3 sponsored and ≥ 30% top-of-search impression share (22.5% TOS IS = reporting reference) | B6, SR, QA |
| Non-ranking cut | over break-even on both 30 and 90 days → cut ≤ 30% of base; > 2 × break-even on ≥ 30 clicks → stop | B6 |
| Harvest | ≥ 3 orders at ≤ break-even ACoS, no exact owner → build exact, negate at source | B6, PB, STR |
| Wasted-spend ceiling | 10% of spend (discovery 40%) | SR, quick audit |
| Placement mix (ranking) | 70–90% of clicks at top of search, ≤ 20% on product pages | B6 |
| Read windows | push: 7 days · settled read: 7 clean days after any event · deal days excluded 2 weeks | B6, SR |
| Escalation | 2 consecutive flat/backfired grades → escalate; never repeat a failed lever a 3rd time | SR |

## Phases

### Phase 0 — Intake and reconciliation → `references/01-intake-and-data.md`
Request every input in **one batch** (template: `templates/intake-request.md`). Do not start partially. For each file: window, freshness, portfolio/marketplace, key fields. Reconcile before analysing (bulk vs Command Center spend, Sellerboard units vs orders, inventory on-hand vs available). Halt on any source mismatch that would move money; log smaller ones as data conditions.

### Phase 1 — Frame the product → `references/03-profitability-and-guardrails.md`
Declared goal, lifecycle stage (launch / ranking / transition / mature / harvest / clearance), events on the calendar (deals, Prime, BFCM, price changes), and the owner settings above. Current state in numbers: sales, units, orders/day, ad spend/day, TACoS (monitor), organic share, rank on head terms, placement split — before and during any event.

### Phase 2 — Economics and inventory (the gates) → `references/03-…` and `references/04-inventory-sku-ltsf.md`
Per SKU/colour: price, margin/unit, break-even ACoS, break-even CPC per placement, ceiling. Per SKU: available, inbound (dated), velocity, days of cover, zone, stock-out-before-arrival test, preferred/backup/clearance variation, LTSF/aged exposure. **Output: which variation each campaign should advertise, and which SKUs block pushing.**

### Phase 3 — Market and competitors → `references/08-competitor-market.md`
Full roster (all mapped competitors; tiers Aspirational / Beatable / Poor); per rival: variation structure, price, units/revenue, BSR and movement, reviews/rating/velocity, keyword coverage, organic vs paid, placement behaviour (SP/SB/SBV/product pages), heroes and trends, strengths/weaknesses. Market: tracked traffic, our share, contested / theirs-only / ours-only, addressable set, segment gaps, price ladder, niche benchmarks. **Output: where we win, where they win, where no one is strong.**

### Phase 4 — Keyword universe → `references/05-keyword-research.md`
Build the universe (MKL ∪ SQP ∪ search-term report ∪ competitor keywords). Normalise, classify (core / attribute / size / colour / brand / competitor brand / other product / language), tier by volume, syntax/root, relevancy (scored against the live listing), indexing, organic/sponsored rank, SQP funnel vs market, ownership (one live exact owner per term). **Output: every term with class, relevance, demand, position and owner.**

### Phase 5 — Listing, offer and positioning → `references/09-listing-positioning.md`
Four-quadrant diagnosis per syntax (CTR × CVR vs market). Offer vs rivals (price, pieces, value per unit, reviews, rating, variations, claims). Listing checks by quadrant. **Output: which problems are visibility (buy placement), conversion (fix offer — no rank push), or both.**

### Phase 6 — Campaign and keyword decisions → `references/06-campaign-ppc-decisions.md`
Objective per campaign (from targeting). Run every campaign and every search term through the **master decision order** (below) to one decision: PUSH / WAIT / HOLD RANK / BREAK-EVEN / CUT / MIX FIX / DEFEND / HARVEST / REDUCE / BLOCK / DEDUPLICATE / CHECK OWNER / MONITOR / RESTART / KEEP / REVIEW. Every in-scope campaign gets an action; out-of-scope campaigns are judged on their own metrics.

### Phase 7 — Placement and pricing execution → `references/07-placement-and-bidding.md`
Backward-solve each campaign's base bid and top-of-search modifier from its target prices; mix fix; budget sizing from plan clicks × price; spend-limit check; step and ceiling checks. Ranking plan per push term (target rank, required clicks/orders, price path, budget, first milestone).

### Phase 8 — Competitor influence and gaps → `references/08-competitor-market.md` (§ influence rules, gaps)
Check each decision against the landscape (agrees / stretch / reachable / challenge / engine-blind). List gaps with size, owner, how to fill inside the guardrails, and validation. Competitor ASIN targets classed OFFENSIVE / TEST / AVOID.

### Phase 9 — Exceptions, validation plan, longitudinal loop → `references/10-longitudinal-validation.md`, `references/11-exceptions-and-failure-modes.md`
Where no automatic change is allowed (listing flag, ceiling below cost, thin data, deal days, shared campaigns, stock). Checkpoints with pass conditions and fallbacks. Impact ledger: grade prior actions (executed? worked / flat / backfired / too soon / deal window), escalate repeats.

### Phase 10 — Deliverables and quality gate → `references/12-writing-and-deliverables.md`
Workbook + decision document (+ optional Google/Slack versions). Run the quality gate; fix every failure before presenting.

## Master decision order (every campaign and every term)

The first gate that fires ends the row; record which gate fired.

1. **Data validity** — CVR/ACoS with 0 orders, CTR with 0 impressions, conflicting sources, stale economics → quarantine: no recommendation, refresh task.
2. **Goal & event gate** — product goal authorises ranking spend? Deal or LTSF state active (deal-state economics, no judging on deal days)?
3. **Economics** — margin, break-even CPC, ceiling for the advertised variation; price above ceiling → cut to ceiling now (never deferred).
4. **Inventory** — advertised variation's zone and stock-out-before-arrival; Red → protect (taper, re-point to backup); Yellow → no new push.
5. **Structure** — live state (keyword AND campaign enabled), indexing, advertised variation correct (ranking = best seller/White of the size; discovery = clearance variation; a switch never changes the size), objective matches targeting, one live exact owner per term (duplicates → withheld).
6. **Sample** — below the floor → hold (formula-only corrections allowed if over ceiling); converting rows skip the zero-order gate.
7. **Delivery** — budget truncation (in-budget < 70% of the day) → budget first; placement mix wrong (product pages > 20% on ranking) → mix fix before price.
8. **Quality** — four-quadrant: conversion problem → fix offer, no push; listing flag → WAIT; competitor shock → investigate before any bid.
9. **Objective loop** — ranking push logic / break-even / conversion CPA / defence share / discovery graduation / conquest page share.
10. **Size & bound** — step caps, ceilings, spend limit, budget = plan clicks × price.
11. **Landscape check** — does the field make the decision sensible? (never changes a price).
12. **Log** — trail: input → metric → rule → decision → action → expected outcome → validation date.

## Output contract (minimum)

- **Decision document** (Word/Google Doc): summary with the decisions and what needs the owner · how to read · current state · rules applied · each area's findings (Finding → Why it matters → Action → Expected impact) · competitive landscape · tests · exceptions · next steps with dates · appendix of engine/process fixes. Outline: `templates/report-outline.md`.
- **Decision workbook** (xlsx): Start here · Overview · Metrics dictionary · Decision rules · Campaign decisions (every campaign, with trail) · Keyword decisions (every term) · Push plan · Placement · Variation & stock · Inventory × PPC · Financial guardrails · Competitor landscape / profiles / keywords / ASIN targets / gaps · Exceptions · Validation plan · Checks. Spec: `templates/workbook-spec.md`.
- **Decision trail on every row**: Input → Metric → Logic (rule id) → Decision → Action → Expected outcome → Validation.

## Quality gate (must all pass — full list in `references/12-writing-and-deliverables.md`)

No price above its ceiling · no step above its cap · no push on Red/Yellow stock or unqualified terms · no blended-parent break-even · every in-focus campaign has a decision · every term has a decision · no brand or push term blocked · no exact ranking term negated · one live owner per term · spend within the limit (events stated) · no bidding-strategy change unless decided · every number sourced and dated · every competitor claim states coverage · every action has a re-read date and a reversal condition · no internal codes or tool names in delivered text · totals reconcile.

## Reference map

| File | Read when |
|---|---|
| `references/01-intake-and-data.md` | Phase 0: inputs, fields, windows, joins, reconciliation, halt rules |
| `references/02-metrics-and-formulas.md` | any time a metric is computed or cited |
| `references/03-profitability-and-guardrails.md` | Phases 1–2, 7: economics, ceilings, spend limits, deals |
| `references/04-inventory-sku-ltsf.md` | Phase 2: cover, zones, variation routing, backup switch, LTSF |
| `references/05-keyword-research.md` | Phase 4: universe, classification, tiers, relevancy, SQP, harvest/negate, de-dup |
| `references/06-campaign-ppc-decisions.md` | Phase 6: objectives, decision logic per objective, ranking states, discovery, conquest |
| `references/07-placement-and-bidding.md` | Phase 7: placement-first diagnosis, backward-solve, mix fix, DSTR, budgets, fixed-bid trial |
| `references/08-competitor-market.md` | Phases 3, 8: data pulls, rival profile, keyword landscape, ASIN targeting, gaps, influence rules |
| `references/09-listing-positioning.md` | Phase 5: four-quadrant, listing rubric, offer and price positioning |
| `references/10-longitudinal-validation.md` | Phase 9: impact ledger, grading, escalation, validation plan |
| `references/11-exceptions-and-failure-modes.md` | before finalising any decision: exceptions/blocks and the failure register |
| `references/12-writing-and-deliverables.md` | Phase 10: writing standard, trail format, deliverables, quality gate |
| `references/13-source-map-and-conflicts.md` | when two rules seem to disagree, or to trace a rule to its source skill |
| `OWNER-DECISIONS.md` | open points with the default applied until the owner rules — cite the default used |
| `templates/` | intake request, report outline, workbook spec, decision-trail examples |
| `examples/b6-case-study.md` | a worked end-to-end example (what failed, what was corrected) |


---

# Owner decisions — defaults applied until the owner rules

The sources leave these open. The framework applies the **default** now and says so in the analysis. When the owner rules, record the answer in the product's analysis (and, if it should apply to every product, in `SKILL.md` owner settings and `references/13-…`).

| # | Question | Default applied now | Where used |
|---|---|---|---|
| 1 | Product goal (Growth / Mixed / Profit-First / Clearance) | Must be declared; undeclared = Profit-First for the ranking gate | 03, 06 |
| 2 | Ranking ceiling multiple | 2 × break-even CPC on the TOS price (alt: flat ~$8–9 account cap) | 03, 07 |
| 3 | Spend limit and margin rule per product; event exceptions | Owner sets; exceptions stated with dates and margin | 03, 07 |
| 4 | TACoS target | None — monitored and decomposed only | 03 |
| 5 | Tolerance between bulk spend and Command Center / console spend | State the gap in $ and %; halt only if it would change a decision | 01 |
| 6 | Freshness limit for Data Dive niche data used in price / sales claims | Show the research date beside every figure; > 30 days = flagged | 01, 08 |
| 7 | Organic-share benchmark (graduation 40–50% vs quick-audit floor 60%) | Both shown as references; no decision driven by either | 02, 03 |
| 8 | Basis for contest rate, win rate, distance (ASINsight) | Working definitions in 02, labelled | 02, 08 |
| 9 | Brand-term Sponsored Products bids above break-even | Only with verified competitor presence on the brand term, capped at 2 × break-even | 03, 06 |
| 10 | Cover short of next arrival by ≤ 7 days ("tight") | Treated as Red for pushing; no colour swap unless cover < days to arrival | 04 |
| 11 | Overstock cover ceiling; "large batch" size for LTSF Yellow | No house value — state the figure used | 04 |
| 12 | Mapping of MKL labels "Relevant", "Lower Relevant", "Generic" | Use the numeric relevancy score (≥60 high / 35–60 moderate / < 35 not) | 05 |
| 13 | Head-generic guard | SV ≥ 50,000 generic head terms → MONITOR, never pushed | 05 |
| 14 | Harvest ACoS tiers (≤15 / 20 / 30%) and the 45% runaway filter | Scaled to the product's own break-even ACoS (tiers = 0.5 / 0.67 / 1.0 × BE; runaway 1.5 × BE) | 05 |
| 15 | Funding order when push budgets exceed the spend limit | Revenue at target ÷ cost to close; ties by DSTR, cover, CVR; big terms scaled first | 07 |
| 16 | Market under 1 purchase/day on a ranking term | Route out of Ranking only when the whole market is below 1/day; otherwise re-scope DSTR | 07 |
| 17 | Graded push tiers for non-ranking SCALE (CONFIRMED / STRONG / PROVEN) | Applied as provisional: hold / +≤10% / +≤15% | 06, 07 |
| 18 | Defensive share ladder | Provisional: held share with ACoS within 10–15% of ceiling → −10%/week to a recorded floor | 06 |
| 19 | Absolute competitor thresholds (500 units/month, traffic bands, review / keyword counts, $ price gaps) | Applied as calibrated on one market; restate as shares of the market when the market is much larger/smaller | 08 |
| 20 | Review-theme read size | 50 most recent critical + 50 most recent positive reviews per top rival, last 6 months | 09 |
| 21 | "Executed" tolerance for placement %, budget and state changes | Exact match; bids ±$0.01 | 10 |
| 22 | Grading movement for defence share, discovery graduation, conquest page share, market-share band | State the movement used; no house threshold | 10 |
| 23 | Objective turn-off ACoS levels | Ranking 100%, Market Share 50%, Discovery 60%, Profitable Conversion 50%, Defensive / product targeting 30% — as referral to the owner, never automatic | 11 |
| 24 | Zero-order REDUCE / REVIEW without asking | REDUCE executes within the step caps; REVIEW goes to the fix queue with an owner | 05, 11 |
| 25 | Minimum bid floor | $0.50 (provisional); a lower ceiling wins | 07 |
| 26 | Discovery candidacy count basis (keyword vs root cluster) | Keyword; singular/plural share a count | 05 |
| 27 | Amazon suggested bids | Not used for pricing | 03, 07 |
| 28 | Bidding-strategy changes | None, unless the fixed-bid trial fires and the owner approves | 07 |
