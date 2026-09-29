# Amazon Product Analysis — consolidated framework (single-file edition)
Give this file to Claude and say "follow the framework". It is the full skill in one document: the workflow (SKILL), owner defaults, 13 references, templates and a worked case. Section headings below are the original file names.
## Contents
- SKILL.md
- OWNER-DECISIONS.md
- references/01-intake-and-data.md
- references/02-metrics-and-formulas.md
- references/03-profitability-and-guardrails.md
- references/04-inventory-sku-ltsf.md
- references/05-keyword-research.md
- references/06-campaign-ppc-decisions.md
- references/07-placement-and-bidding.md
- references/08-competitor-market.md
- references/09-listing-positioning.md
- references/10-longitudinal-validation.md
- references/11-exceptions-and-failure-modes.md
- references/12-writing-and-deliverables.md
- references/13-source-map-and-conflicts.md
- templates/intake-request.md
- templates/report-outline.md
- templates/workbook-spec.md
- templates/decision-trail-examples.md
- examples/b6-case-study.md


---

<!-- FILE: SKILL.md -->
# FILE: SKILL.md


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

<!-- FILE: OWNER-DECISIONS.md -->
# FILE: OWNER-DECISIONS.md

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


---

<!-- FILE: references/01-intake-and-data.md -->
# FILE: references/01-intake-and-data.md

# 01 — Intake and data (Phase 0)

Read this before opening any file. Phase 0 ends when every input is received or confirmed absent, every file is read and reconciled, and the data-conditions register is written. No decision is taken before that.

## Contents
1. The one-batch rule and halt conditions
2. Intake by request type (analysis / plan / refinement)
3. Master input table
4. Reading discipline (how to open a file)
5. Joins and keys
6. Reconciliation checks
7. Data-validity quarantine
8. Freshness rules
9. Two-scope architecture (product vs campaign)
10. Unmeasured ≠ zero
11. Data-conditions register
12. Verifying what a column really measures
13. Open questions for the owner

---

## 1. The one-batch rule and halt conditions

1. **Request every input in one message** (template: `templates/intake-request.md`). Name each file, what it powers and the window you need. [PB, QA, SR]
2. **Do not start partially.** Wait until each item is supplied or the user explicitly confirms it does not exist this cycle. If only some arrive, list the missing ones back and ask once more. [PB, QA]
3. **Missing input = named gap**, never a guess or a substitute. Record it in the register (§11) with the decisions it blocks. Missing value = blank, never 0. [all]
4. **Ask once, then log.** An answerable gap is asked before it is logged; never log "revisit next cycle" for something the user could answer now; never ask about something already knowable from the files. [PB]
5. **Confirm before anything is computed:** product (parent ASIN + child SKUs), marketplace (**US or CA — never mixed**), exact portfolio name(s), window end date, stage, declared goal, owner settings (SKILL.md table). [SR, E, PB]

**Halt conditions — stop, report, no recommendations:**

| # | Condition | Why |
|---|---|---|
| H1 | Marketplace not confirmed, or files from two marketplaces mixed | Rates, prices and fees differ by marketplace [SR] |
| H2 | An advertised SKU has no economics (no margin/unit) | Never fall back to a global or blended break-even (source engines defaulted to 0.1986 — a known defect) [SR, 13§3] |
| H3 | Merge accuracy fails: DOH differs from source by > 0.5 day, or LTSF $/month by > $0.02 | The merged table no longer matches its source [SR] |
| H4 | Target CTR/CVR in the bulk drift > 2% from recomputation (Market × 1.10 / × 3.0) on > 10% of rows | Every quadrant verdict would rest on wrong targets [SR] |
| H5 | A relevant sheet was NOT-OPENED (§4) | A decision may contradict data you never read [WB] |
| H6 | Bulk IDs don't resolve (one unmatched Campaign/Keyword ID on an update) | Stale export; any upload built from it fails or edits the wrong row [CB] |
| H7 | Any cross-source mismatch that would move money (spend, margin, stock, price) and can't be explained | Nothing is guessed [SR, PB] |
| H8 | Plan request with no declared product goal | Hard stop until declared or a suggested goal is confirmed. If the owner will not declare, apply Profit-First for the ranking gate and record it [PB, SKILL] |

Smaller mismatches that don't move money → log as a data condition and continue.

---

## 2. Intake by request type

| | Analysis (diagnose what exists) | Plan — from scratch | Plan — refinement |
|---|---|---|---|
| Purpose | Audit an engine run, product or campaign set | Decide what to do next | Update an existing plan against new data |
| What to request | Everything the diagnosis needs, incl. the artefact under review (engine output, decided bulk, prior plan) | **Full batch** (§3), all windows | Read the whole existing plan first; classify each decision **stated / gap / stale**; request only what the gap and stale items need + the prior action log and impact ledger |
| Staleness | A **finding**, not a blocker (report it) | Blocks the verdicts that depend on it (e.g. stale margin blocks ceilings) | Stale decisions re-derived; stated ones kept unless the grade says otherwise |
| First computation | Reconcile the artefact against its sources | Reconcile sources; frame goal and economics | **Execution check, then grade every prior action** (executed? worked / flat / backfired / too soon / deal window) before any new decision |
| No prior log | n/a | n/a | Treat as first cycle: say "No prior cycle supplied — treated as first cycle"; no grades, no escalation; write the full baseline [SR] |
| Scope creep | Ask before expanding an analysis into a plan | — | Forward-only: no silent retro-rewrite of earlier decisions |
| Output | Findings + register | Full plan + workbook | Clean full plan + change log + change review sheet |

[PB, SR, WB] Ambiguous request → ask once which of the three it is.

---

## 3. Master input table

Windows: **current 7 d vs prior 7 d** = evidence a live action is judged on; **30 / 90 d** = judgement windows for non-ranking and keyword rules; **60–90 d** = baseline, sample size, trend. Attribution is 7-day: the last 7 days of any window read low. [PB, B6]

| # | Source | What it is | Required fields / columns | Window | Freshness limit | Used for | If missing → blocked |
|---|---|---|---|---|---|---|---|
| 1 | **SP bulk file — 3 windows** | Amazon Bulk Operations export with performance columns | Entity, Operation, Campaign/Ad Group/Keyword/PT IDs, Campaign Name, Portfolio, State (campaign, ad group, keyword), Bidding Strategy, Targeting Type, Match Type, Keyword/PT expression, Bid, Budget, Placement rows (Top / Rest Of Search / Product Page) + Percentage, Product Ad SKU/ASIN, Impressions, Clicks, Spend, Sales, Orders, Units. Engine-built bulks add Campaign Objective, Syntax, Target Rank, Organic Rank, TOS IS, Market/Target CTR/CVR, DSTR | Current 7 d · prior 7 d · 60–90 d (plus L30 if the engine uses it) | IDs must come from a fresh export (same day as any upload build) | Every campaign/keyword decision; routing (Product Ad rows); live state; bids, boosts, budgets | Everything in Phases 6–7. Only the prior-7 d file missing → no week-on-week evidence; long window missing → no baseline/sample reads |
| 2 | **Command Center / console campaign report** | Amazon Ads campaign performance by day; product tile by ASIN | Date, Campaign, Spend, Impressions, Clicks, Orders, Sales, budget and in-budget time where available | Daily, 30 / 90 d | Same window as bulk | Spend reconciliation; product-level spend (tile); deal-day spend; budget truncation | Product-scope spend check; truncation test (→ record "delivery unverified") |
| 3 | **Placement report** (campaign × placement) | Amazon placement report via Command Center | Campaign, Placement (TOS / ROS / PDP / off-Amazon), Impressions, Clicks, Spend, Orders, Sales | 30 d mix; 90 d for TOS CVR | Same window as bulk | Placement click share, TOS CVR, TOS CPC (clearing), break-even CPC per placement, mix fix | Placement-level pricing — ceilings fall back to blended CVR, which the framework forbids for pushes → no PUSH verdicts |
| 4 | **SP Targeting report** | Per-target report incl. top-of-search impression share | Targeting, Match Type, Campaign, **Top-of-search impression share**, Impressions, Clicks, Spend, 7 Day Advertised SKU Units | 7–30 d | Same window as bulk | TOS impression share (holding the top); PPC velocity per SKU | TOS IS reads → no "holding top" test; push step rule runs blind. **Required**, not optional [QA] |
| 5 | **Search Term Report (STR)** | Account-wide, one row per day × campaign × customer search term | Date, Portfolio name, Campaign Name, Match Type, Targeting, Customer Search Term, Impressions, Clicks, Spend, `7 Day Total Sales ` (note trailing space), `7 Day Total Orders (#)`, `7 Day Total Units (#)` | 60–90 d (B6 keyword rules read 90 d; 30 d for spend distribution) | ≤ 1 cycle old | Harvest, negation, zero-order, wasted spend, keyword decisions, auto split | Harvest/BLOCK/REDUCE at search-term level; WAS% |
| 6 | **SQP** (Brand Analytics Search Query Performance) | Raw child-ASIN export; roll up to parent (§5.4) | Search Query, Search Query Volume, Impressions/Clicks/Cart Adds/Purchases: **Total Count** (market) and **ASIN Count** (brand); Purchases: Price (Median), ASIN Price (Median) | 13 weeks (B6); monthly for trends | Latest complete period | Market vs brand CTR/CVR, shares, Target CTR/CVR, four-quadrant, DSTR feasibility | Four-quadrant falls back to portfolio medians, labelled **provisional**; Target CTR/CVR blank (never guessed) |
| 7 | **MKL** (master keyword list) | Keyword universe with volume, syntax, relevancy | MKL keyword, Search Volume, Relevancy (fallback Derived Relevancy), Categorization, Organic Rank, Syntax; optional Indexed, PPC-targeted flags, Final Relevancy (manual) | Monthly build | **> 30 days = stale** | Keyword universe, SV tiers, relevancy, coverage, launch candidates | Coverage/gap analysis; SV tiers; relevancy-driven negation (→ Manual Review). Syntax must be verified against the account taxonomy before use; the MKL indexing field is unvalidated → ask before it moves money |
| 8 | **Target Ranks** | Owner's rank targets per term | Portfolio Name (Informational only), Search Term, Rank Target (+ target date if kept) | Current | Current plan | Ranking objective flag; rank gap; push premium; HOLD RANK | Ranking verdicts (a term without a target has no premium and no push) |
| 9 | **Rank tracking** | Daily organic (and sponsored) rank per term | Keyword, Date, Organic Rank (Sponsored Rank if available). **Data Rova** (primary; long format; 0/blank = not ranked → 101). **Data Dive** Rank Radar (gap-fill; wide, `Search Terms` + ISO date columns; 101 = not ranked). Own daily crawl where available | ≥ 1 month history (ideally 3); 30 d for decisions | < 1 month history → **out of scope for a ranking verdict** | Rank arc, rank drop, ranking states, sufficiency stop | Every ranking verdict (→ OUT OF SCOPE). Two trackers can disagree by ~7 places (B6): name the one that governs |
| 10 | **Data Rova / ASIN Insights (keyword export)** | Per-keyword market export for our product | Keyword, DSTR, Weekly Sales, Organic Rank, Sponsored Rank, Traffic Distribution Organic / Ad | Weekly | ≤ 1 week | DSTR, organic traffic share (for netting), current rank | DSTR sizing → rows UNSIZED; organic netting impossible |
| 11 | **ASINsight exports** (competitor traffic tool) | Our export + one per mapped competitor; market keywords; competitor view; placement trends; addressability | Per keyword: 7-day traffic, traffic ratio, organic/ad distribution, organic & sponsored rank, placements, weekly search volume, SFR. Competitor view: totals, organic/paid split, hero ASINs, placement reach, contested/ours-only/theirs-only. Addressability: addressable / disqualified / unknown with reasons. Placement trends: daily scores per child ASIN (organic, SP, SB, SB video) | 7-day traffic snapshot; trends 30–60 d | Exports compared only if taken **≤ 2 days apart**; placement-trend feed may be retired — state its last day | Market size, our share, contest, ad gap, rivals present, push-term field check, gaps | Competitor landscape and influence checks (Phase 3/8) — report "competitor data not supplied"; never "no competitors" |
| 12 | **Data Dive niches** | Niche dives: listings, keywords, roots | Per listing: price, est. units & revenue/month, BSR, rating, reviews, variations, listing age, page-1 keyword count, advertised keywords; niche median price/reviews/units | Per dive date | Dated; re-dive if > 1 month for pricing claims (No source rule; decide and record) | Price ladder, niche benchmarks, rival profiles | Price/offer positioning; conquest entry test (price/rating/reviews) |
| 13 | **AdInsight per competitor ASIN** | `AdInsight_US_<ASIN>_<start>to<end>.xlsx` | ASIN Ad Traffic Score (daily), Ad Keyword Count, Ad Position Traffic Ratio, Keyword Count for Ad Position (SP/SB/SBV/HR/TRB/CPF/SOR), Top 10 <type> Ad Traffic | 7–30 d | Dated per file | Rival ad-type mix, dormancy, pull-back; brand resolved per ASIN | Ad-type gap sizing (→ state as unmeasured) |
| 14 | **Helium 10 Cerebro / Xray** | Reverse-ASIN keyword ranks; head-term page listing data | Keyword, SV, own & competitor organic ranks (multi-ASIN in one pull), H10 PPC Sugg. Bid (context only); Xray: title, price, rating, reviews, images, video, BSR | Dated | Dated | Coverage audit (LIVE/PAUSED/MISSING), listing comparison | Coverage gaps can't be demand-validated |
| 15 | **Sellerboard** (per SKU/colour) | Profit per SKU | SKU, ASIN, Units, Refunds (count), Sales, Amazon fees, COGS, Advertising, Net profit / Margin, ASP | **Last 30 days** (B6); deal-state separately | **> 45 days = stale**, or any price / fee / size-tier / packaging / freight / LTSF change → re-derive within 48 h | Margin/unit → break-even ACoS, break-even CPC, ceilings; TACoS; margin after ads | **All pricing** (H2). Stale margin blocks every ceiling-referencing verdict |
| 16 | **Inventory / DOH / inbound** (per SKU, full unfiltered export) | Stock and replenishment | SKU, ASIN, Available (FBA sellable), Reserved, On-hand, Inbound/transit units, Units in production, dated next arrival (`Next In Stock`: date / Today / Not in Horizon), velocity (Base SV / sv/day — planned, shown beside the 30-day actual pace that gates zones, 13 #49), today's DOH (first date-like column in the DOH matrix) | Snapshot same day as bulk | Same day | Zones, stock-out-before-arrival, variation routing, projected DOC | Every PUSH (inventory gate unknown → no push); backup switch |
| 17 | **LTSF / aged inventory** | Aged-inventory surcharge view + FBA Inventory Age report | SKU, size, price, units per age bracket (**all 8 brackets**), cu ft/unit, estimated monthly surcharge ("AIS"/"CHARGE" column), units shipped t7/t30/t60/t90 | Monthly (assessed on the 15th) | Current month | LTSF tier, floor price, break-even discount, clearance objective | Clearance/LTSF decisions; 4-bracket file = approximate charges (finding) |
| 18 | **Preferred / Backup mapping** | Owner's variation routing | Product, Keyword Syntax, Preferred SKU, Backup SKU (key = syntax lowercased, no spaces; `root|size` keys for size fallback) | Current | Current | Which SKU each campaign should advertise; switch simulation | Switch recommendations; **never auto-derive backups** — ask the user to paste pairs [INV] |
| 19 | **Deal / event calendar** | Dated deals and events | SKU, deal price, start–end dates, deal type, deal fees; season/peak weeks | Next 60 d + last 14 d | Current | Deal-state economics; deal-day exclusion; build freeze; spend-limit exceptions | Every rate read near an event is suspect → state "calendar not supplied" and exclude windows that may contain deals |
| 20 | **Listing copy** | Live title, bullets, backend terms, A+; screenshots of gallery and page-1 results | Title, bullets, description, backend search terms (Category Listings Report), images | Live | Same week | Relevancy scoring vs listing; indexing; four-quadrant listing checks | Relevancy re-score (keep MKL labels, flag); listing verdicts |
| 21 | **Product goal & owner settings** | Owner's declared goal and dials | Goal (Growth/Scale · Mixed · Profit-First · Clearance/LTSF), stage, spend limit ($/day or /week, event exceptions), margin rule, ranking ceiling multiple, step limits, TACoS target (only if set), approval thresholds | Current | Confirm each cycle | Ranking gate, spend limit, ceilings | See H8 |
| 22 | **Prior action log + impact ledger** | Last cycle's decisions and grades | Log ID (`cycleDate|CampaignID|KeywordID-or-PTID`), lever, before/after values, expected metric/direction/tolerance, review date; ledger key `CampaignID|Target/KeywordID`, consecutive no-impact count, history | Last 12 weeks rolling | Last cycle | Execution check, grading, escalation | Refinement grading → treat as first cycle (§2) |
| 23 | **Competitor roster** | Mapped competitors per product | Brand, parent ASIN, child/hero ASINs, marketplace, tier (Aspirational / Beatable / Poor), export present y/n, date | Current | Current | Coverage statement, tiering, ASIN classification (own / own other product / competitor / unmapped) | Competitor tiers; any "we win / they win" claim (→ unmeasured) |
| 24 | **Product/business report** (reporting.xlsx or Business Report by child ASIN) | Parent-level weekly trend: revenue, units, sessions, unit session %, organic sales | ASIN, week, revenue, units, ad spend, TACoS, organic sales % | 4 weeks + prior | Latest complete week | Product-scope metrics (single source of truth, never recomputed from bulk) | Product-scope dashboard; organic share |
| 25 | **Sibling bulks** (products sharing head terms) | Same windows as #1 | As #1 | As #1 | As #1 | Shared-term ownership, cross-sibling cannibalisation | Named gap: ownership of shared head terms unresolved |
| 26 | **Manager responses** (if a review loop exists) | Actions the manager took outside the plan | Key, Manager Action, Manager Lever, Manager Action Date | Last cycle | Last cycle | Ledger loop status | Manager-acted rows graded as ordinary rows |

Amazon suggested bid ranges are **not requested** — they are not used to set prices (owner rule; 13 #18). [B6]

---

## 4. Reading discipline

1. **Enumerate every sheet/tab** of every file before declaring anything missing. [PB, WB I-1]
2. Read content; extract each figure with file / sheet / window. Diff long vs short windows. [WB I-2–I-4]
3. Give each sheet a status: **READ-FULL / READ-PARTIAL / NOT-RELEVANT / NOT-OPENED**. NOT-RELEVANT only after comparing its content; a relevant sheet NOT-OPENED halts the run (H5). [WB I-5–I-7]
4. Read the **unfiltered** inventory export before any filtering. [WB]
5. Header rows move: bulk header = first of the top 8 rows containing `Entity` and `Bid`; Sellerboard header auto-detected in the top 15 rows; DOH header = the row whose column A is `SKU` (often row 14); KCP-form MKL header on row 2. [SR, E]
6. A **supplied column beats a derivation**; a supplied column that looks wrong is a finding, not something to silently recompute. [WB]
7. State price stability over the window (price changes split windows). [WB]
8. Produce one **scope-labelled census**: every campaign that spends on the product, with its scope (§9). [WB, B6 F13]

---

## 5. Joins and keys

### 5.1 Normalisation
| Key | Rule | Never |
|---|---|---|
| Search term / keyword | `strip().lower()`, collapse whitespace; **word order preserved**; singular↔plural and symbol variants merge (close variants) | Sorted-token form except for grouping reports; never for ownership or deployment [13 #14] |
| Rank join | Exact lowercase + trim only | Fuzzy or reordered matching (ruling 2026-07-16) [SR] |
| Size tokens | Longest first: California King / Cal King before King; Twin XL before Twin; Split King, Full XL, Olympic/Short/RV Queen before Queen | Checking King before California King [E, PH] |
| Display | Keep original casing in outputs | — |

### 5.2 Entity keys
- **SKU: exact match including colour.** Unmatched → flagged, never filled from a "similar" SKU, size or colour. [SR]
- **Portfolio: the exact `Portfolio name` string** copied from the STR/bulk — never retyped (retyping is the classic "0 rows" failure). [E]
- **Marketplace: never mixed**; competitors belong to one marketplace. [SR, E]
- **ASIN detection:** lowercased value matches `^b0[a-z0-9]{8}$`. [E]
- **Campaign → SKU:** from Product Ad rows, never from campaign names (names were wrong on 212 of 251 rows in one audit). Name parsing is a fallback for reports only (SKUs longest-first, then ASIN substring). [WB, INV]
- **Bulk IDs:** Campaign / Ad Group / Keyword / PT IDs as **text** (15-digit precision loss otherwise). Keywords resolved by Keyword ID, campaigns by exact stripped name. [CB]
- **Objective:** from targeting per campaign block, never from the name (reference 06). [OC]
- **Brand terms:** brand name + misspelling list, substring match on the lowercased term; a brand missing from the list gets its terms flagged for negation — check the list first. [E]

### 5.3 Join outcomes
No match → blank, never 0. Safe division everywhere (`a/b if b else blank`; Excel `IFERROR(x/y,"")`). [E]

### 5.4 SQP parent roll-up
1. Group by Search Query.
2. **Brand (`… ASIN Count`) → SUM** across child ASINs.
3. **Market (`… Total Count`), Search Query Volume, market median price → TAKE ONCE** (max per query). Summing market columns multiplies them by the number of children and destroys every share.
4. Ignore SQP's precomputed rates; recompute CTR, CVR, shares (reference 02 §6).
5. Brand price = median of children's `Purchases: ASIN Price (Median)`.
6. Verify: rows = unique queries; Market Impressions = raw Total Count; Brand ≤ Market; every share 0–100%.
[SQP, E]

---

## 6. Reconciliation checks

Run before analysis. A failure that would move money halts (H7); others become data conditions.

| # | Check | Pass condition / tolerance | On fail |
|---|---|---|---|
| C1 | Bulk spend vs Command Center spend, same window | Equal after removing shared multi-product campaigns; remaining difference explained (window, attribution, shared campaigns). No numeric tolerance in any source — state the difference in $ and % | Explain or halt if it changes a decision (No source rule on tolerance; decide and record) [B6] |
| C2 | Product tile spend vs sum of campaign rows | Difference = spend of shared campaigns on other products; product-basis spend = row spend × (tile ÷ rows) | Flag shared campaigns (exception: no colour/price automation) [B6] |
| C3 | Sellerboard units vs orders | Units ÷ orders stable (B6: 1.03 units/order); gross units = units + \|refund count\| | Investigate multi-packs/refund spikes before deriving per-unit costs [SR, B6] |
| C4 | Inventory on-hand − available − reserved | Gap ≤ 5 units | > 5 → verify at source before zoning [PB] |
| C5 | Merged DOH / LTSF vs source | DOH \|Δ\| ≤ 0.5 day; LTSF \|Δ\| ≤ $0.02 | Halt (H3) [SR] |
| C6 | Target CTR/CVR recompute | Within 2%; fail if > 10% of rows off | Halt (H4) [SR, PF] |
| C7 | SQP roll-up integrity | §5.4 step 6 | Rebuild the roll-up [SQP] |
| C8 | SV% | Σ SV% = 1.0 | Fix the denominator [MDB] |
| C9 | Keyword PPC totals | Keyword total = Σ its campaign rows | Rebuild the grouping [KCP] |
| C10 | STR spend distribution | Spend % sums to 100%; grand total = STR total for the portfolio | Rebuild [STR] |
| C11 | Rows in = rows out; spend to the cent after any merge | Exact | Rebuild the merge [PF] |
| C12 | kw + PT spend vs advertised-product report | Equal within the same window | Find missing rows (paused ad groups with spend, other portfolios) [PF] |
| C13 | LTSF charge | units × cu ft × rate vs invoice within a fraction of 1% | Show both scenarios; charges "approximate" [LTSF] |
| C14 | Execution of last cycle's changes | Actual vs recommended within $0.01 (EXECUTED); actual vs before within $0.005 (NOT EXECUTED) | Report execution rate; < 80% = follow-through problem [SR] |
| C15 | Two rank sources on the same term | Report both; name which governs (daily crawl / Data Rova primary) | Data condition if > ~7 places apart [B6] |
| C16 | Campaign census | Every campaign spending on the product's ASINs is in the decision list | Add missing campaigns and mark them; no write on a campaign without its current state [B6 F13] |
| C17 | Paused-ad-group rows with spend; blank Syntax / SV / Objective | Listed | Classify or hold [PF] |

---

## 7. Data-validity quarantine

Quarantined rows get **no recommendation**, only a refresh task (same-day where possible). [PB, WB, SR]

| Condition | Rule |
|---|---|
| CVR or ACoS stated with 0 orders; ACoS without sales | Quarantine |
| CTR stated with 0 impressions/clicks; CTR = 0 with clicks; CVR = 0 with orders | Quarantine |
| Same metric conflicting across bulk / console / Sellerboard / SQP | Quarantine until settled |
| Duplicate values copied across rows (identical odd numbers) | Quarantine; verify at source |
| Stale economics (§8) | Quarantine every ceiling-referencing verdict |
| Implausible volume (SV implausible vs SFR, identical odd SV across files — e.g. a 400k+ fragment repeated in 5 files) | Verify; exclude from totals [LP] |
| 0% in-budget time with $0 spend | **Missing data**, not budget truncation [PB] |
| Velocity from an out-of-stock, suppressed or deal window | Not at face value: record trailing velocity, correction factor and its basis; an unstated haircut is rejected [LTSF] |
| Window straddling a price change, lever change or deal | Split the window; judge the clean part only [LTSF, B6] |
| Placement verdict on < 30 clicks per arm | "Directional" only (reference 02 §10) [PF] |

---

## 8. Freshness rules

| Input | Limit | Consequence | Source |
|---|---|---|---|
| Economics (margin table) | > 45 days, or any price / fee / size tier / remeasure / packaging / freight / LTSF change | Re-derive margin and every ceiling within 48 h; until then no ceiling-referencing verdict | PB, SR |
| Sellerboard | True-up monthly | Margin trend (WoW / MoM) read separately from freshness | PB |
| MKL | > 30 days | Stale: coverage, tiers and relevancy flagged | PB |
| Rank history | < 1 month | Out of scope for ranking verdicts; ≥ 1 month (ideally 3) needed; exclude stock-out and re-route stretches | PB |
| Attribution | Last 7 days | Read low; compare settled windows only | B6 E2 |
| Deal window | During + 2 weeks after close | Excluded from trend verdicts; grading span overlapping a deal → no verdict (DEAL WINDOW) | PB, SR |
| ASINsight exports | > 2 days apart | Not comparable to each other | ASINsight tool |
| Bulk export | Not same-day as the upload build | IDs may be stale (H6) | CB |
| Inventory | Not same-day as the bulk | Re-pull before zoning | WB |
| Manifest completeness | < ~85% of expected inputs/fields | Run labelled "degraded" | PB |
| Pending dated COGS change | — | Carry current-COGS margin for live decisions + future-COGS margin as context | PB |

In an **Analysis**, staleness is reported as a finding; in a **Plan**, it blocks the dependent verdicts. [PB]

---

## 9. Two-scope architecture

| | Product scope | Campaign scope |
|---|---|---|
| Unit | Parent ASIN / product | Every campaign that advertises any of the product's SKUs |
| Source | Product report / Sellerboard / Command Center product tile — single source of truth, **never recomputed from bulk** | Bulk + STR + placement + targeting reports |
| Includes | Organic + ad sales, total units, TACoS, organic share, margin after ads | **Sibling portfolios** where the product's ranking spend lives (e.g. two portfolios for one product family); shared multi-product campaigns flagged |
| Used for | Trends, goal/stage signals, spend limit, margin rule | Every campaign, keyword and placement decision |

Rules:
1. Reconcile the two openly: campaign scope usually exceeds product scope because of halo sales on other ASINs. State the gap. [QA]
2. Using one portfolio when ranking spend sits in a sibling portfolio produces false reads (the "$94 artefact": ranking spend looked like $94 because the rest sat in the sibling). [QA]
3. **Shared campaigns** (advertise other products, multi-SKU LTSF/auto): excluded from colour and price automation; reviewed in their own product's analysis; spend attributed on product basis (C2). [B6 E13]
4. **Reverse sweep:** search the whole account for the product's child ASINs; every campaign found is decided or marked out of scope with an owner and date. [WB]

---

## 10. Unmeasured ≠ zero

1. A competitor without an export is **unmeasured**, not absent; its traffic is null, not 0. [ASINsight, R-CI12]
2. Every share, contest or "we win" figure states its **coverage** (e.g. "13 of 32 mapped competitors measured"). No conclusion about an unmeasured competitor. [R-CI12]
3. A term with no rank on a day is **unranked**, not a rank; unranked days count toward the median as 101 (not ranked); rank = NR if ≥ half the days are unranked. [B6, SR]
4. A day the crawler didn't run is marked missing, not unranked. [rank crawl]
5. A missing SQP match leaves targets blank. [E]
6. Zero conversions on a thin sample = unknown (affordable CPC = 0 → leave the bid, flag). [PB]
7. A missing section in a report reads "Not available" — never placeholder numbers. [QA]

---

## 11. Data-conditions register

One row per condition; write it at the end of Phase 0 and keep it through the cycle. [PB, DR, WB]

| Field | Content |
|---|---|
| ID | DC-01, DC-02… |
| Condition | What is missing, stale, conflicting or unverified |
| Evidence | File / sheet / column / window and the numbers showing it |
| Why it matters | The mechanism (e.g. "ceilings rest on a 52-day-old margin") |
| Actions gated | Exactly which decisions are held or labelled provisional because of it |
| Workaround used | Fallback applied and its label (e.g. "portfolio medians — provisional"), or "none" |
| Owner | Named role responsible for fixing it (a gap with no owner is not recorded) |
| Due | Date |
| Asked? | Date asked and answer (ask once before logging) |
| Status | Open / resolved / withdrawn (withdrawn findings stay with the overturning evidence) |

---

## 12. Verifying what a column really measures

Before using any column in a decision, confirm its meaning from the data, not the header. [PF, WB]

| Check | Example trap |
|---|---|
| **Grain** — campaign, keyword, placement, day? | Placement split is campaign-grain; a keyword's placement split is an estimate [B6] |
| **Does it carry orders?** | Bulk placement rows may carry no orders — placement CVR needs the placement report [SR gap] |
| **Attribution basis** | `7 Day Total Sales` includes halo (other ASINs; up to 81% halo seen); `7 Day Advertised SKU Units` does not [PF, INV] |
| **Market vs ours** | Data Rova "Weekly Sales" and DSTR are **market** figures at a rank, not our sales [PF] |
| **Snapshot vs window** | Bid, boost, budget and state are snapshots; performance columns are window sums |
| **Traffic vs scores** | ASINsight 7-day traffic is impression-like (not clicks or sales); placement-trend scores are scores — never add them to traffic |
| **Rank encoding** | 0 / blank / 101 = not ranked, depending on tool [SR] |
| **Units** | LTSF is $ per cubic foot, not per unit (per-unit reading overstates 1.4–4.8×) [LTSF] |
| **Sign conventions** | Sellerboard advertising cost is negative; profit before ads = Net profit + \|advertising\| |
| **Fee bundling** | Sellerboard fees bundle referral + FBA + storage + inbound; fee/ASP > 55% = contaminated (reference 02 §4) [SR] |
| **Inventory family view** | Use the full inventory export, never the variation/family page [PF] |
| **Budget cap vs spend** | A budget is a cap, not spend; committed spend = run-rate of enabled campaigns [WB] |
| **Precomputed rates** | Recompute SQP and engine rates from counts; never trust exported rates [SQP] |

Test method: recompute one row by hand from raw counts; compare two windows; compare against a second source; if it still doesn't reconcile, log a data condition and do not use the column for money.

---

## 13. Open questions for the owner

1. **Bulk vs Command Center spend tolerance (C1):** no source sets a numeric tolerance. Until the owner sets one, every unexplained gap is stated in $ and % and treated as a halt only when it changes a decision.
2. **Inventory velocity basis:** Resolved — see 13 #49: zones use the 30-day actual pace (deal/stock-out windows corrected and labelled), with the inventory file's planned velocity shown beside it; never the push pace.
3. **Data Dive niche freshness** for price claims has no source limit (§3 #12). Set one.


---

<!-- FILE: references/02-metrics-and-formulas.md -->
# FILE: references/02-metrics-and-formulas.md

# 02 — Metrics and formulas (dictionary)

Every metric the framework computes or cites: what it is, the exact formula, where it comes from, the window, how to validate it, the thresholds that use it, how it moves a decision, and the traps. Cite from here; don't redefine metrics elsewhere.

## Contents
1. Conventions (windows, blanks, rounding)
2. Traffic and funnel
3. Cost and efficiency
4. Unit economics and price limits
5. Placement and bidding
6. Market, SQP and keyword metrics
7. Rank and ranking sizing (DSTR)
8. Inventory and LTSF
9. Delivery, budgets and execution
10. Sample floors and significance
11. Competitor and market landscape
12. Open questions for the owner

Column key for the tables: **Formula** (definition = formula) · **Source / window** · **Validate** · **Thresholds** · **Drives** (decision it moves) · **Pitfalls**.

---

## 1. Conventions

1. **Safe division:** `a ÷ b` is blank when b = 0 — never 0, never ∞ in delivered text (engines may carry ∞ internally for ACoS with spend and no sales). [E]
2. **Recompute rates from summed counts**, never average rates. Group CTR = Σclicks ÷ Σimpressions. [SR, B6]
3. **Windows:** current 7 d vs prior 7 d = action evidence; 30 d and 90 d = judgement windows; 60–90 d = baseline; SQP 13 weeks. Attribution is 7-day: the last 7 days read low. Deal days and 2 weeks after a deal are excluded from verdicts. [PB, B6]
4. **Per SKU, per placement.** Money metrics are computed per advertised SKU (colour/size) and per placement; blended numbers are context only. [SKILL]
5. **Deal state separate:** margin, CVR, rank arc and counts are computed separately for deal and clean periods, never blended. [PB]
6. **Every number is dated** and names its source in delivered text. [PB]
7. **Rounding for sizing:** required clicks and budgets round **up** (ceil), never `round()`. [PF]

---

## 2. Traffic and funnel

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Impressions | Count of ad impressions | Bulk / Command Center; 30/90 d | Final on day one | CTR verdict needs ≥ 1,000 | CTR denominator; impression share | Deal days inflate [B6] |
| Clicks | Count of ad clicks | Bulk / Command Center / STR; 30/90 d | Final on day one | 15 = bid read floor; 100 = CVR verdict; 11 for product targets | Read floor for every judgement [PB, SR] | Clicks on paused-ad-group rows still count to spend (C17 in 01) |
| CTR | clicks ÷ impressions | Same; market CTR from SQP 13 wk | Recompute from counts | vs Target CTR = Market CTR × 1.10; fail < 0.9 × target | Four-quadrant; listing gate | Placement mix changes CTR — read at the delivering placement, not blended (blended 0.63% vs TOS 2.96% in one case) [DR] |
| Orders | Ad-attributed orders (7-day) | Bulk / STR `7 Day Total Orders (#)` | Last 7 d settle | Harvest ≥ 3; zero-order ≥ 20 clicks | Conversion, harvest, zero-order | Trailing-week under-count [B6] |
| Units | Ad-attributed units | STR `7 Day Total Units (#)`; Targeting `7 Day Advertised SKU Units` | Units ÷ orders stable (B6 1.03) | — | PPC velocity (advertised SKU only) | Total units include halo SKUs [INV] |
| CVR | orders ÷ clicks | Bulk / STR; 30/90 d | ≥ 100 clicks for a verdict | Keyword Target CVR = Market CVR × 3.0; syntax target Market × 1.10 | Break-even CPC; qualification; stop rule | Deal days lift CVR; don't read on < 15 clicks [B6] |
| CVR by placement (TOS / ROS / PDP) | placement orders ÷ placement clicks (campaign grain) | Placement report; **90 d** | Needs placement orders (bulk placement rows may lack them) | Conversion basis: own ≥ 50 clicks; blend 15–50; size/product rate < 15 (§5) | Break-even CPC per placement; push stop (TOS CVR < market on 50+ clicks) | Campaign grain only; keyword placement CVR is an estimate [B6] |

---

## 3. Cost and efficiency

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Spend | Σ ad cost | Bulk / Command Center; daily/30/90 d | Reconcile bulk vs console (01 C1–C2) | Owner spend limit | Spend limit, budgets | Product tile ≠ Σ campaign rows when campaigns are shared [B6] |
| CPC | spend ÷ clicks | Same | — | vs break-even CPC and ceiling | Price checks | Down-only bidding lowers realised CPC below the bid [B6] |
| Sales (ad) | Σ 7-day attributed sales | Bulk / STR `7 Day Total Sales ` | Settle 7 d | — | ACoS, RPC | Includes halo sales on other ASINs [PF] |
| ACoS | spend ÷ ad sales | Same; 30 and 90 d | Blank with 0 sales (quarantine if stated) | Break-even ACoS; 2 × BE = stop line; non-ranking: over BE on both 30 & 90 d → CUT ≤ 30% of base; > 2 × BE on ≥ 30 clicks → stop (proposed for owner confirmation; search term / target: BLOCK); ≤ 50% BE with orders → SCALE-eligible (+≤ 25%) | Non-ranking CUT/BLOCK/SCALE; keyword REDUCE/BLOCK | Deal price lowers AOV and raises ACoS [13 #16, B6] |
| Real ACoS | spend on rows **with** sales ÷ sales | STR | — | Healthy < BE (STR default 30%) | Match-type/root health | Excludes waste by design — always shown with WAS% [E] |
| ROAS | ad sales ÷ spend | Bulk | = 1 ÷ ACoS | — | Reported only | — |
| CPA (cost per order) | spend ÷ orders = CPC ÷ CVR | Derived | — | ≤ margin/unit (non-push); ≤ 2 × margin/unit (push) | Push loss bound; conversion objective judged on CPA vs ceiling | Blank with 0 orders [B6, PB] |
| AOV | sales ÷ orders | Sellerboard / bulk; 30 d | — | — | BE ACoS conversion; AOV source by objective: advertised SKU (Ranking, Conversion), routed SKU (Conquest), campaign blend (Discovery) | AOV shift from variation mix voids every ceiling until economics refreshed [PB] |
| RPC (revenue per click) | ad sales ÷ clicks | Bulk; per placement where possible | — | — | RPC ceiling | Basket sales incl. halo [PF] |
| RPC ceiling | RPC × break-even ACoS | Derived | = margin-based BE CPC when AOV matches | Caps any RPC-derived bid | Non-ranking bid cap | Uses blended RPC unless placement RPC exists [SR] |
| TACoS | ad spend ÷ total sales (refund-net) | Sellerboard / product report; weekly | Total sales from the product report | **No target unless the owner sets one**; PB bands (Launch ≤ 25%, Ranking push 12–15%, Transition 8–12%, Mature 4–7%, Harvest ≤ 4%) reference only | Monitor and decompose (paid vs organic movement); never a bid gate | Sizing spend on a "TACoS rung" was a documented failure [13 #17, B6 F24] |
| Organic share | (total sales − ad sales) ÷ total sales | Product report; weekly | Product scope only | Graduation signal: organic > ~40–50% sustained [PB]; Quick-audit floor 60% [QA] (reference) | Stage integrity (graduate / demote after 4 weeks below target) | Ad sales include halo; attribution double-counts are possible |
| WAS% (wasted-spend share) | spend on rows with 0 sales ÷ spend | STR; per campaign | — | Ceiling **10%** of campaign spend (**40%** discovery); product-level waste reported | Negation pass trigger | Negation is decided by relevance, not by WAS% alone [13 #24] |
| Waste share | group's zero-sale spend ÷ total zero-sale spend | STR | Σ = 100% | — | Where to look first | — |
| Marginal ACoS | Δspend ÷ Δad sales between two steps | Two clean windows around an executed change | Same length windows, no event | > 1.5 × average ACoS → freeze further raises at prior rung [SR]; > 2 × blended → unwind the step [PB] | Whether a raise bought profitable sales | Needs an executed step and clean windows |
| Marginal CPC | Δspend ÷ Δclicks | Same | Same | — | What the last step cost per extra click | Same |
| CPC ratio | realised CPC ÷ governing target price | Bulk | — | > 1.0 → push-only justification; > 1.5 → unjustifiable | Ceiling audit | Governing target = ceiling for pushes, BE CPC otherwise [SR] |
| Margin after ads | (profit before ads − ad spend) ÷ sales | Sellerboard; weekly | — | Owner margin rule (e.g. ≥ 10%; event exceptions dated) | Spend limit; weekly push cut from the bottom of the funded list | [B6 R-F5/F6] |

---

## 4. Unit economics and price limits

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Margin/unit (profit per unit before ads) | **Sellerboard profit before ads ÷ units, per SKU/colour, at the price in force** = (Net profit + \|advertising\|) ÷ units. Component build (say so): ASP − COGS/unit − Amazon fees/unit, with COGS and fees ÷ **gross units** (units + \|refund count\|) | Sellerboard; **last 30 d**; deal price during deals | Fee/ASP > 55% → fee/unit = portfolio median fee/ASP (from SKUs with ≥ 10 units, 0 < ratio ≤ 55%) × ASP, logged "verify"; < 10 units → same-size median (≥ 10 units, positive) capped at own | Stale > 45 d | Every break-even and ceiling | Never blended parent; colours differ 2–3×; wrong margin inflated every ceiling ~40% in B6 [13 #1, SR, WB] |
| Break-even ACoS (CM2) | margin/unit ÷ price (= CM2 = (ASP − COGS − fees) ÷ ASP when built from components; no returns term) | Derived per SKU | Flag if outside **5–70%** | Target ACoS = BE for non-push rows; Quick-audit reference: target 50% BE, max 75% BE | Non-ranking and keyword cuts | Deal price changes it — recompute [13 #1, QA] |
| Break-even CPC (break-even price) | margin/unit × CVR **of the placement being bought** | Derived | CVR basis per §5 | Non-ranking: price ≤ 1.0 × BE CPC at every placement | Pricing base for every campaign | Wrong colour → wrong break-even; blended CVR hides TOS vs PDP gap [B6] |
| Ceiling (ranking) | **2 × break-even CPC** on the ranking term's TOS price (owner may set another multiple, or a term-specific time-boxed raise) | Derived | Price > ceiling → cut to ceiling now | Hard cap on pushes | PUSH sizing; over-ceiling correction | "Cost + 15%" ceilings drift upward (B6 F23); flat $8–9 cap is the alternative owner setting [13 #3] |
| Push premium | +25% if rank ÷ target ≤ 1.5; else (rank ÷ target − 1) × 50%; 0 when rank ≤ target | Derived from rank | Rank from governing tracker | Capped by the ceiling (so ≤ +100% at 2×) | Push price | Flat premium across all terms = not derived [13 #4, PB] |
| Push price | break-even CPC × (1 + premium), ≤ ceiling | Derived | ≤ ceiling | Raise ≤ +30%/day toward it while not holding top | TOS price target for PUSH rows | Never set from competitor or suggested bids [B6] |
| Clicks-to-loss | margin/unit ÷ CPC | Derived | — | — | Quick read: clicks per order before a loss | [PB] |
| Weekly loss ceiling (ranking) | (push ACoS − BE ACoS) × projected sales at required spend | Derived | Basis stated; ≥ 1 day's spend | Hitting it → owner flag, not auto-stop | Ranking funding | [PB] |
| Deal-state margin | (deal price − COGS − fees − deal fees) per unit | Deal calendar + Sellerboard | Computed before the event | Deal-state ceiling = deal margin × CVR | No bid above the deal-state ceiling; in-deal CVR never justifies more | A discount cuts contribution by its full depth [PB] |
| Affordable CPC per placement | margin/unit × that placement's CVR | Derived | — | TOS / ROS / PDP each judged separately | Placement pricing | Never judge placements on one blended number [PB] |

---

## 5. Placement and bidding

**Conversion basis for any placement ceiling** (13 #2): n = own placement clicks (90 d). n ≥ 50 → own placement CVR. 15 ≤ n < 50 → linear blend: w = (n − 15) ÷ 35; CVR = w × own + (1 − w) × size rate. n < 15 → size (or product) placement rate. [B6]

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Base bid | Keyword/target bid (applies at ROS and PDP; PDP moves only via base) | Bulk snapshot | — | Base cut ≤ 50% per step; base ≥ TOS price ÷ 10; floor $0.35–0.50 (≥ clearing ÷ 10) | Mix fix | Base cut must not drag TOS price down [WB, B6] |
| Boost (TOS modifier) | Placement Top percentage | Bulk snapshot | 0–900% | ≤ 900% | TOS price | At cap: raise base only to price ÷ (1 + boost) [B6 R-M2] |
| **TOS price** | **base × (1 + boost)** | Derived | Recompute ±$0.03 | ≤ ceiling (push) / ≤ BE CPC (non-push) | The price every push rule writes | Down-only may pay less [B6] |
| Effective TOS bid (by strategy) | Fixed / down-only: base × (1 + boost). Up-and-down: up to base × (1 + boost) × 2.0 at TOS (Amazon may raise up to 100%) | Derived | Up-and-down effective bid must clear the ceiling × 1.05 | Breach → re-solve base = ceiling ÷ ((1 + boost) × multiplier) | Ceiling audit | Existing strategies are left unchanged [SR, 13 #8] |
| TOS rebuild (hold TOS price when base changes) | new boost % = (target TOS price ÷ new base − 1) × 100 | Derived | 0–900 | Written in the same row as the base change | Mix fix, base cuts | Letting TOS fall as base-cut residue is a defect [SR, WB] |
| Clearing CPC (TOS) | TOS spend ÷ TOS clicks per campaign (≥ 3 TOS clicks, else portfolio value) | Placement report; 30 d | — | Effective TOS < clearing → priced out (serves on PDP) | Placement-first diagnosis | Low sample → portfolio fallback, labelled [PF] |
| TOS CPC | TOS spend ÷ TOS clicks | Placement report | — | Ceiling ≥ TOS CPC to qualify a push | PUSH qualification (else WAIT) | [B6 R-P1] |
| TOS impression share | our TOS impressions ÷ available TOS impressions | SP Targeting report (required); 14–90 d | Per target | **≥ 30% plus top-3 sponsored = holding the top** (push stop/step test) [13 #40]; Quick-audit 22.5% = reporting reference only | Daily push step; at ceiling 3 days without top-3 sponsored and ≥ 30% → owner | With ≥ 5 rivals at SP #1–5, not a pass/fail signal alone — judge rank after 7 days [B6, R-CI5] |
| TOS click share | TOS clicks ÷ campaign clicks | Placement report; 30 d | Campaign grain | < 30% of clicks while clicks ≥ plan → MIX FIX before any price raise | Mix fix | Distinct from impression share [PB] |
| Placement mix (click shares TOS / ROS / PDP) | placement clicks ÷ campaign clicks | Placement report; 30 d | Σ = 100% (excl. off-Amazon) | Ranking: TOS 70–90%, PDP ≤ 20% (on ≥ 15 clicks) | MIX FIX: base −50% (−25% if PDP brings orders), boost raised so TOS price holds, same write; re-check day 7 | Keyword-level mix is an estimate [B6 R-M1] |
| Placement cost per order | placement spend ÷ placement orders | Placement report | — | — | Efficiency comparison across placements | Needs placement orders [PF] |

---

## 6. Market, SQP and keyword metrics

SQP rates are recomputed after the parent roll-up (01 §5.4): **brand counts summed, market counts taken once.**

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Market CTR / CVR | Mkt clicks ÷ Mkt impressions; Mkt purchases ÷ Mkt clicks | SQP; 13 wk | Brand ≤ Market | — | Benchmarks | Summing market columns across children destroys every share [SQP] |
| Brand CTR / CVR | Brand clicks ÷ Brand impressions; Brand purchases ÷ Brand clicks | SQP | — | E15 listing flag: ours < market on ≥ 30 clicks → WAIT (no push until listing checked) | Four-quadrant; push qualification | Brand = all our children, organic + paid [B6] |
| Impression / click / cart-add / purchase share | Brand count ÷ Market count at that stage | SQP | 0–100% | — | Share trend; Defensive "share held" (IS per branded query where available) | — |
| CTR / CVR variance | Brand − Market (points) | SQP | — | — | Reported | — |
| Market price / brand price | Market: `Purchases: Price (Median)` taken once; Brand: median of children's ASIN price | SQP | — | — | Price position | — |
| Revenue / Rev per click (SQP) | purchases × price; revenue ÷ clicks | SQP | — | — | Context | — |
| Target CTR | Market CTR × 1.10 | Derived | Recompute; > 2% drift on > 10% of rows → halt | — | Four-quadrant | Blank without SQP — never guessed [13 #20] |
| Target CVR | Keyword: Market CVR × 3.0 · Syntax: Market CVR × 1.10 | Derived | Same | — | Keyword/syntax diagnosis | Keyword vs syntax multipliers differ [QA] |
| Four-quadrant (per syntax) | CTR pass = CTR ≥ 0.9 × target; CVR pass likewise → **STRONG** (both pass: scale) · **VISIBILITY** (CTR fail, CVR ok: buy placement) · **CONVERSION** (CTR ok, CVR fail: fix offer, no rank push) · **BOTH FAILING** (reduce, fix listing first) | SQP + bulk | No SQP → portfolio medians, "provisional" | ≥ 4 weeks in a state = chronic (Conversion → bids at maintenance, no ranking allowance) | Mode of a syntax, never a keyword's bid | Medians are relative — half fail by construction [13 #20, PB] |
| SV (search volume) | Monthly searches (MKL/H10/SQP); weekly in ASINsight | MKL (≤ 30 d) | Sources don't reconcile — name the source | Tiers below; launch floor ~250; Cold gauntlet > 500 | Demand gate, tier, hero/halo | Artefact volumes (implausible vs SFR) excluded [B6, LP] |
| SV tier | VHSV ≥ 10,000 · HSV 1,000–9,999 · MSV 500–999 · LSV 100–499 · VLSV < 100 | Derived | — | VHSV/HSV (or rank-targeted) = hero, 1 keyword per campaign; MSV 3; LSV/VLSV 10 per halo campaign | Structure | [PH] |
| SV% | SV ÷ Σ SV (product universe) | Derived | Σ = 1.0 | — | Coverage % by volume, not keyword count | [MDB] |
| Relevancy % | Listing scorer vs live title + bullets (first match wins): disqualifier 0 · ≥ 3-word phrase verbatim 92 / 2-word 85 · 4-/3-/2-gram overlap 78 / 64 / 50 · off-topic 0 · theme match 36 · unigram round(15 + 15 × overlap ÷ words) · no match 0 | Listing copy + MKL | Keep original MKL label beside it | Decisions: **≥ 60% high · 35–60% moderate · < 35% not relevant** | Negation tree, harvest filter, launch tier | Non-English ≈ 0 means no on-page text, not irrelevance [13 #30, LP, STR] |
| Keyword CVR ratio vs market | our CVR ÷ market CVR | Bulk + SQP | ≥ 30 clicks | < 1.0 → listing check | Push qualification | [B6] |

---

## 7. Rank and ranking sizing (DSTR)

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Organic rank | Median daily organic position over the window; unranked days count as 101; NR if ≥ half the days unranked | Rank crawl / Data Rova (primary) / Data Dive (gap-fill); 30 d | ≥ 1 month history; exclude stock-out and re-route stretches | — | Premium, qualification, HOLD RANK | Two tables can disagree ~7 places — name the governing one [B6] |
| Sponsored rank | Observed ad position on the results page | ASINsight / hourly read | Not available for every term | Top-3 most hours = holding | Daily push step | [B6] |
| Rank ratio | current rank ÷ target rank | Derived | — | ≤ 1 at target; ≤ 1.5 moderate; > 1.5 full premium | Push premium | [B6, WB] |
| Rank gap | organic rank − target rank (places) | Derived | — | Reach ≈ 30 places for push candidacy | PUSH qualification; harvest objective (> 10 places → Ranking) | [KCP, B6] |
| Rank drop | rank now − rank 30 days ago | Rank crawl | — | > 10 places while getting clicks → freeze price, find cause (listing, colour, keyword state, competitor, stock) | Rank-loss investigation (never a bid raise) | Stock signature: collapse concentrated in one colour/size during an outage [B6, LTSF] |
| Rank arc | overall, 14 d and 7 d reads stated separately; clean arc governs, deal arc separate | Rank crawl | — | Shorter windows = early warning | Ranking state test (reference 06) | [PB] |
| **DSTR** (daily sales to rank) | Daily sales (organic + paid) needed at the target rank, from market data (Data Rova / ASIN Insights / competitor sales at that rank); **DSTR = max(1, ceil(stated))** | Data Rova / ASIN Insights; weekly | Feasibility: vs SQP market purchases ÷ 30 — DSTR > 50% of market daily purchases = re-scope (not a gate); market can't support 1/day → route out of Ranking | Floor 1/day | Push volume and budget, **never price** | Market weekly sales are the market's, not ours [13 #19, PF, SR] |
| Organic sales on the term (proxy) | DSTR × our organic traffic share on the term (or measured organic sales) — labelled **proxy** | ASIN Insights traffic distribution | organic + paid = DSTR ± 0.02 | — | Netting | SQP brand coverage can be ~1% — say what the proxy rests on [PF] |
| Paid sales needed | max(DSTR − current organic sales on the term, 0) | Derived | — | — | Required clicks | Not netting doubles spend (known defect) [13 #19] |
| Required TOS clicks/day | paid sales needed ÷ **own achieved TOS CVR** | Derived | Column must vary across terms | — | Budget | Never a target/planning CVR [PF] |
| Required budget/day | ceil(required clicks × TOS price × 1.05) | Derived | Budget ≥ requirement × 1.05 | Within spend limit; Σ requirements reconciled to product sales (upper bound) | Budget line, funding order | Requirements set volume, never price (B6 F21) |

---

## 8. Inventory and LTSF

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Available stock | FBA sellable units | Inventory export; snapshot | On-hand − available − reserved gap ≤ 5 units | < 7 days of cover → Red, no push (push itself needs Green ≥ 60 d and cover ≥ days to next arrival + 7); 0 → pause push, ranking ads to backup | Push gates | Transfers and customer orders are not available [B6 R-I6] |
| Velocity | units sold ÷ days | Sellerboard; **30-day pace** (7-day as warning) | Correct OOS/deal/suppressed windows with a stated factor | Clearance colour: velocity ≤ size median | Cover, clearance choice | Never the push pace (inflated forecast created a false stock-out in B6 F30) |
| PPC velocity | Σ 7-day advertised SKU units ÷ window | SP Targeting report | Advertised SKU only | — | Share of velocity bought by ads | [INV] |
| Days of cover (DOC / DOH) | available ÷ units per day | Derived | Same-day snapshot | **Green ≥ 60 · Yellow 21–59 · Red < 21**; stock-out before inbound arrives = Red regardless | Inventory gate; Yellow = no new push; Red = protect/re-point | High DOC with velocity down 15% WoW for 3 weeks = trajectory problem [13 #9, PB] |
| Days to next arrival | dated confirmed arrival − today | Inventory inbound | Confirmed dated only; "Not in Horizon" = blank | Gap ≤ 7 days = TIGHT (ease, don't swap); cover < arrival by > 7 days → switch to backup (same size) | Variation routing | Inbound counts only if ETA ≤ DOH [B6, WB] |
| Push stock test | DOC ≥ days to next arrival + 7 (in addition to Green ≥ 60 d) | Derived | — | Fails → no push | PUSH gate | [13 #9] |
| Max affordable velocity | stock ÷ lead time; incl. transit: (stock + transit) ÷ lead time | Inventory; lead time default 90 d | — | Velocity > max (stock) → reduce PPC aggression; < max (incl. transit) → scale carefully | Inventory × PPC action | Lead time is an input — confirm per product [INV] |
| Projected DOC | (stock + dated inbound) burned at baseline velocity + planned order gap, to the checkpoint date | Derived | Same data version as the push sizing | Must stay Green (≥ 60 d) through the push checkpoint, or the push is blocked, shrunk or time-boxed [13 #42]; the 21-day figure is only the launch floor for a new campaign (04 §4) | Blocks a push that would push the SKU into Yellow/Red | [PB, WB] |
| Backup cover | backup stock ÷ **preferred SKU's velocity**; also (stock + transit) ÷ velocity | Inventory + mapping | Only for advertised preferred SKUs | ≥ lead time = covers; ≥ 30 d = partial; else insufficient; stock + transit = 0 = backup also OOS | Backup switch recommendation | Backup already advertised → the swap competes with its own campaign [INV] |
| LTSF rate | $ per **cubic foot** per month by age: 181–210 d $0.50 · 211–240 $1.00 · 241–270 $1.50 · 271–300 **$5.45 (cliff)** · 301–330 $5.70 · 331–365 $5.90 · 366–455 $6.90 (or $0.30/unit if greater) · 456+ $7.90 (or $0.35/unit if greater); assessed on the 15th | Amazon rate card | Charge reconciles to invoice | Cliff at 271 d | Clearance timing | Rate card may change — confirm current [LTSF] |
| LTSF per unit | rate × cu ft/unit (≥ 366 d: max with per-unit floor) | Derived | — | — | Floor price | Per-unit reading overstates 1.4–4.8× [LTSF] |
| Months to clear | aged units ÷ monthly velocity (cap 12) | Derived | Velocity basis stated | > 3 → Yellow; > 6 → Red (tier script) | LTSF tier | [LTSF] |
| Floor price | (salvage + LTSF until sold + FBA fee) ÷ (1 − referral %) | Derived; LTSF until sold = LTSF/u/mo × min(months to clear, 12) | Floor ≥ price → no discount authority | — | Lowest price that beats salvage | COGS is sunk — never in the floor [LTSF] |
| Break-even discount | LTSF until sold ÷ net proceeds at current price (net = price × (1 − disc) − referral − FBA) | Derived | n/a if net ≤ 0 | < 20% coupon/price drop · 20–40% outlet · > 40% salvage comparison · > 100% no depth pays | Clearance route | [LTSF] |
| Salvage per unit | max(removal net, liquidation net, disposal) with removal net = resale − removal fee (~$1.07) − 3PL; liquidation net = price × 7.5% − price × 2.5% | Defaults stated | Replace defaults before terminal calls | — | Floor price | [LTSF] |
| Max combined depth | max(0, 1 − floor ÷ price) per child | Derived | — | Stacking cap | Promo depth | [LTSF] |

---

## 9. Delivery, budgets and execution

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Budget utilisation | spend ÷ daily budget | Console; 7–30 d | — | Floors: Defensive 100% · Ranking 80%+ · Discovery 70%+ | Budget before bids (Defensive) | A budget is a cap, not spend [PB, WB] |
| In-budget share (truncation) | share of the day the campaign stayed in budget | Console | 0% with $0 spend = missing data | **< 70% = truncated**: all rates unreliable, budget first | Delivery gate | Truncated data isn't bid evidence [PB] |
| Budget (push) | required TOS clicks × TOS price × 1.05 (+ expected PDP spend) | Derived | Price and budget rows load together | Min $10/day; > $500 → review; moves > $50/day (up or down) need owner confirmation [13 #41] | Push funding | A capped budget stops a push mid-day (B6 F14) [SR, PB] |
| Committed spend | run-rate spend of enabled campaigns (not caps) | Console; 60 d | — | Headroom = spend limit − committed | Funding order | [WB] |
| Pacing deviation | actual spend pace vs the product's day-of-week curve | Console daily | — | > ~25% swing → flag same day | Event/pacing control | [PB] |
| Execution status | EXECUTED if \|actual − recommended\| ≤ $0.01; NOT EXECUTED if \|actual − before\| ≤ $0.005; else PARTIAL | Current bulk vs action log | — | — | Grading eligibility | Never grade an unexecuted action [SR] |
| Execution rate | executed ÷ logged actions | Action log | — | **< 80% = follow-through problem** | Process finding | [SR] |
| Grade delta | Ranking: Δ organic rank; others: Δ ACoS (points) | Ledger | ≥ 15 fresh clicks; after horizon | ≤ −3 WORKED · ≥ +3 BACKFIRED · else FLAT; margin/BE shift > 10% → provisional | Escalation (2 consecutive flat/backfired) | Deal-window overlap → no verdict [SR] |

---

## 10. Sample floors and significance

| Read | Floor | Below the floor |
|---|---|---|
| Bid verdict | 15 clicks (product targets 11) | Hold; formula-only correction if over ceiling [13 #11] |
| CVR verdict | 100 clicks (own TOS CVR usable from 50) | Use the conversion basis blend (§5) |
| CTR verdict | 1,000 impressions | No CTR verdict |
| Zero-order rule | ≥ 20 clicks, 0 orders | REDUCE (relevant, live owner) / REVIEW fix queue (relevant, no live owner) / BLOCK (irrelevant or other product); irrelevant negation from 5 clicks; never negate an exact ranking or brand term [13 #12, #38] |
| Converting rows | Skip the sample gate | — |

**Significance test for two rates** (placement vs placement, period vs period) [PF]:
- SE = √( p1(1 − p1) ÷ n1 + p2(1 − p2) ÷ n2 )
- CI95 = (p1 − p2) ± 1.96 × SE
- CI excludes 0 → **proven**; min(n1, n2) < 30 → **directional** (no verdict); otherwise **insufficient**.
- Never a blanket TOS shift on a directional read.

---

## 11. Competitor and market landscape

Coverage rule: every figure states how many mapped competitors were measured; unmeasured ≠ zero. [R-CI12]

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| 7-day traffic (ASINsight) | Tool's 7-day traffic per keyword/ASIN — **impression-like**, not clicks or sales | ASINsight exports | Exports ≤ 2 days apart to compare | — | Market size, shares | Never add placement scores to it [ASINsight] |
| Share of tracked traffic | our 7-day traffic ÷ Σ tracked traffic (us + measured rivals) | ASINsight market | Coverage stated | — | "How big are we here" | Excludes unmeasured sellers (B6: 2.1% with 13 of 32 measured) |
| Addressability | keyword state: **addressable** (fit-tagged/relevant to our product) · **disqualified** (disqualifier term, other brand, wrong size/category) · **unknown** | ASINsight addressability | Disqualifier vs fit-tag conflicts listed | Push candidacy needs addressable | What we can act on | Unknown share is reported, not assumed irrelevant |
| Rivals present (consensus) | number of measured rivals ranking on the keyword | ASINsight market keywords | Coverage | Push candidate: a majority of measured rivals rank on it (B6: 7 of 13) + core wording [13 #46] | PUSH candidacy | Stated as a share of the measured roster, never a fixed count |
| Keyword state | contested (we and rivals rank) · ours only · theirs only | ASINsight | — | — | Gap lists | — |
| Win rate (contest) | contested keywords we win ÷ contested keywords; "win" = our traffic above the market average on that keyword (tool's contest call) | ASINsight competitor view | Coverage | — | Tier scoreboard | Working definition from the tool output (B6: win 11, lose 1,660 of 1,899) — confirm basis |
| Contest rate | contested keywords ÷ the rival's keywords | ASINsight competitor view | — | — | Overlap with a rival | No source formula; decide and record |
| Distance | our traffic ÷ their traffic (< 1 = they are bigger) | ASINsight competitor view | State whether total or contested-keyword basis | — | Rival profile ("almost level: distance 1.01") | Basis differs by tool view — say which |
| Paid share (market / ours) | paid traffic ÷ total traffic on the keyword | ASINsight | — | — | Ad intensity | — |
| Ad gap | market traffic × market paid share − our traffic × our paid share | ASINsight | Recompute one row | — | Where rivals out-advertise us | Traffic units (impression-like), not $ |
| Opportunity flag | **we_run_none** (they advertise, we don't) · **they_are_more_aggressive** (their ad share > ours) | ASINsight | — | Addressable core term ≥ 3,000 traffic with no search-term row → seed exact at break-even in discovery (B6 R-CI8) | Gap seeding | Engine is blind to terms with no clicks |
| Placement reach | keywords on which a seller appears per placement (organic, SP, SB, SB video, Amazon's Choice, product-page ads) | ASINsight competitor view | — | — | Ad-type gap (SB/SBV lane) | — |
| Placement scores | daily ASINsight scores per child ASIN: organic, SP, SB, SB video; compare first 7 vs last 7 days | ASINsight placement trends | Feed may be retired — state last day | — | Hero visibility trend | Scores, not traffic; never summed with traffic |
| Hero ASINs | fewest child ASINs carrying 80% of a seller's traffic | ASINsight | — | — | Which pages to target/defend | — |
| Traffic change | latest ÷ earlier export − 1 | ASINsight | Same basis both exports | Rival mover: traffic growth > 50%, price cut > 15%, new discount → hold our price 3 days before reading a CVR drop as a bid problem | Competitor-move hold (R-CI11) | Season moves everyone — compare to the rival median |
| BSR | Best Sellers Rank of the lead listing (lower = more sales) | Data Dive / Command Center brief | Dated | — | Rival size, trend | Category-specific; deal days distort |
| Est. units / revenue per 30 d | Data Dive estimate for the best-selling listing | Data Dive | Estimates — label | — | Rival profile, DSTR context | Listing, not whole brand |
| Rating / reviews | Stars; review count | Data Dive / Xray | Dated | New conquest target: OFFENSIVE **and** we win ≥ 2 of price / rating / review count, else TEST [13 #44] | Conquest gate; Cold gauntlet (reviews ≥ ~50% of top-5 median, rating within 0.3★) | [PB] |
| Review velocity | new reviews per week between two dated reads | Command Center brief / Data Dive reads | Blank without a second read | — | Momentum; Fader archetype | Review themes are not in any connected source |
| Value per piece | price ÷ pieces in the set (or per unit of the offer) | Listing data | Same size compared | OFFENSIVE ASIN: priced above us for fewer pieces, or same price with < 50% of our reviews. AVOID and TEST classes: reference 08 (B6 AVOID examples: cheaper sets with far more reviews; other-material sets) | Competitor ASIN class OFFENSIVE / TEST / AVOID (R-CI7) | Compare same size only |
| Price position | our price ÷ niche median (or rival price) | Data Dive / SQP | — | Cold gauntlet: ≤ ~1.25 × category median | Offer diagnosis; conquest watch-CPA | Price never set from competitor data [R-CI4] |
| Tier | Aspirational / Beatable / Poor (mapping) | Competitor roster | — | Stretch target: only Aspirational rivals at/above target → judge on rivals passed (first milestone) | Landscape verdict (agrees / stretch / reachable / challenge) | Tier is a mapping input, not computed |

---

## 12. Open questions for the owner

1. **TOS impression-share threshold:** Resolved — see 13 #40: decisions use ≥ 30% TOS impression share + top-3 sponsored; 22.5% stays a reporting reference.
2. **Marginal ACoS:** Resolved — see 13 #34: freeze raises at > 1.5 × average, unwind one step at > 2 × blended.
3. **Organic-share benchmark:** PB graduation ~40–50% vs Quick-audit floor 60%. Both are listed as references only; set the product's target.
4. **Contest rate, win rate and distance** have no formula in any source rulebook; the definitions above are read from the B6 tool outputs. Confirm the basis (total vs contested keywords).
5. **Rivals-present threshold:** Resolved — see 13 #46: stated as a share of the measured roster ("a majority of measured rivals"), not a fixed count.


---

<!-- FILE: references/03-profitability-and-guardrails.md -->
# FILE: references/03-profitability-and-guardrails.md

# 03 — Profitability and guardrails

Read in Phases 1–2 (frame the product, economics gate) and Phase 7 (pricing, budgets, spend). Everything that decides *how much money a row may spend* lives here. Inventory gates are in `04-inventory-sku-ltsf.md`; placement mechanics (backward-solve, mix fix, DSTR) in `07-placement-and-bidding.md`.

Source tags: [SR] optimization engine · [PB] plan builder · [DR] decision reasoning · [WB] workbook builder · [PF] placement-first · [QA] quick audit · [LTSF] LTSF dossier · [B6] B6 engagement, Sep 2026.

## Contents
1. Product goal and the goal gate
2. Lifecycle stages
3. Per-SKU economics (margin, break-even ACoS, fallbacks, freshness)
4. Break-even CPC per placement and the conversion basis
5. Ceilings and push price
6. Objective ACoS bands and the layered non-ranking rule
7. CPA ceiling, clicks-to-loss
8. Weekly loss ceiling for ranking pushes
9. Spend limit, margin rule and event exceptions
10. Deal-state vs clean-state economics (event mode)
11. TACoS — monitor and decompose
12. Marginal ACoS unwind rule
13. Human-confirm thresholds
14. Financial guardrail checklist (used by the quality gate)
15. Open questions for the owner

---

## 1. Product goal and the goal gate

**Ask for the goal before any ranking, launch or push decision.** It is an owner setting, not something to infer.

| Goal | Ranking allowance (the 2× ceiling on push terms) | Launch scope for new Exact | Rows priced at | What leads the four-dimension read |
|---|---|---|---|---|
| **Growth / Scale** | Available — Exact ranking rows only, each clearing the 5-property gate (Sized, Dated, Ceilinged, Predicted, Funded; see 06) | Highly + semi-relevant | Push terms up to ceiling; all else ≤ 1× break-even | Rank leads; margin softening tolerated inside the loss ceiling [PB] |
| **Mixed** (ranking + profitability) | Available on Exact → Ranking rows; product targets stay Profitable Conversion at standard ceiling | Highly + semi | Split by campaign objective; TACoS decomposed by tag | Split by campaign tag [PB] |
| **Profit-First** | No new pushes. Rank already won may be protected (HOLD RANK, placement discipline, rank-loss investigation) without the allowance | Highly only, permanently | ≤ 1× break-even everywhere | Margin and revenue lead; rank only to protect won positions [PB] |
| **Clearance / LTSF** | None — all rank considerations nullified, including protection | Highly only | Standard ceiling (1× break-even, forward-cash economics for aged units — §3.7) | Inventory and revenue lead: recovery per unit vs clearance timeline [PB] |
| **Undeclared** | Treat as **Profit-First** for this gate; mark every ranking verdict "pending goal" | Highly only | ≤ 1× break-even | — [PB, SKILL] |

Rules:
1. **Gate order:** product goal → syntax clearance. A syntax in chronic Conversion quadrant (≥ 4 weeks) loses the ranking allowance even under Growth. Both must clear. [PB]
2. The goal **authorises** spend; it never re-tags campaigns. Objectives still come from targeting. [PB]
3. The first time the gate authorises or removes a real ranking allowance on a product, **ask the owner before applying it** (provisional rule); the answer then holds for that product. [PB]
4. For a **Plan** request, no ranking allowance, launch or push is written until the goal is declared or a suggestion is confirmed. For an **Analysis** request, proceed with Profit-First treatment and list "goal undeclared" as a finding. [PB, SKILL]
5. If a code-red TACoS tier is in force (only possible when the owner has set a TACoS target — §11), it freezes all scale before the goal is read. [PB]

### 1.1 Suggesting a goal (when none is declared) [PB]
Run in this order; present the suggestion **with its numbers**; nothing downstream uses it until the owner confirms or overrides.
1. **Confirmed LTSF charge on record → suggest Clearance/LTSF.** Nothing else is weighed. Aged stock *without* a confirmed charge is a separate flag, never a Clearance trigger.
2. Otherwise weigh stage + TACoS position + margin trend together (the same three dimensions read every cycle):
   - **Growth/Scale** — Launch or Ranking-push stage, margin healthy or improving, TACoS well inside its reference band.
   - **Profit-First** — margin thin or declining, TACoS at or near its reference band ceiling, or product in Mature/Harvest.
   - **Mixed** — only when the data really splits by segment (some syntaxes show supported ranking opportunity while product economics call for caution). Never the default for "ambiguous".
3. Write it with evidence, e.g. "Suggesting Profit-First — margin/unit fell from $21.40 to $18.10 month on month, TACoS 11.3% vs a Mature reference band of 4–7%, organic share 58% and flat." A bare label fails.

### 1.2 Four-dimension read (every cycle) [PB]
Rank trend (overall, 14 d, 7 d) · revenue WoW and MoM · margin WoW and MoM · inventory posture. Weighted by goal (table above). Combined outcomes:
- All improving → spend plan as computed.
- Rank up + margin down → Growth: recompute at current margin; Profit-First: margin finding governs.
- Revenue up + inventory Yellow/Red → inventory caps spend regardless of goal (gate, not a weight).
- Rank, revenue and margin all declining → escalate a product-level finding before any mechanical spend change.
- One dimension diverging sharply → named finding.

---

## 2. Lifecycle stages

| Stage | Expected campaign mix | Graduates when | Notes |
|---|---|---|---|
| Launch | Discovery-heavy | Organic sales > ~40–50% of total, sustained (not profitability alone) | Launch floor: routed SKU ≥ 21 days of cover (04) [PB] |
| Ranking push | Exact concentrated on the primary syntax | Rank target reached → HOLD RANK for 2 clean weeks, then taper (06, 13 #26) | Push clock = weeks since *this* push began, restarts with a new push [PB] |
| Transition | Push tapering to maintenance | Organic share above target, CVR stable | — |
| Mature / defend | Defensive layer, brand-format coverage, display retargeting, low-budget auto sentinel; no active push | — | — |
| Harvest | Minimum spend, defend won positions | — | — |
| Clearance | Discovery on the clearance variation, break-even PPC on forward cash | Aged stock cleared or terminal decision made | See 04 §LTSF |

Rules:
1. Check the declared stage against evidence (profitability, organic share, review posture, CVR stability). A campaign stack that does not match the stage is a named finding, not something to reconcile silently. [PB]
2. **Demotion trigger:** organic sales share below target 4 consecutive weeks, or ad dependency rising past its declared ceiling → formal review for demotion to Transition. [PB]
3. Stage tags expire on their declared date; renewal needs evidence. Re-entering a ranking posture after stepping back needs a fresh realism check (06 gauntlet). [PB]
4. New-launch stage suppresses campaign turn-off and bidding-strategy changes. [SR]
5. Organic-share targets and dependency ceilings are **Owner decision — ask**; no source sets a default.

---

## 3. Per-SKU economics

### 3.1 Margin per unit — the number every price is built on
| Item | Rule | Tag |
|---|---|---|
| Source | Sellerboard **profit per unit before ads**, per advertised SKU/colour, last 30 days = (net profit + ad spend) ÷ units. Includes product cost, all Amazon fees, refunds, storage | [B6] |
| Price in force | Deal price during a deal (recompute margin at deal price, net of deal fees) | [B6, PB] |
| Granularity | Per advertised variation. **Never** a blended parent, category average or another product's number | [SR, PB, B6] |
| Component build (only when Sellerboard per-SKU profit is unavailable) | CM2 = (ASP − COGS/unit − Amazon fees/unit) ÷ ASP. COGS/unit and fees/unit = totals ÷ **gross units** (units + \|refund count\|). Fees = Sellerboard bundled (referral + FBA + storage + inbound). No returns term. Say which basis was used; never mix the two in one analysis | [SR] |
| AOV per objective | Ranking and Profitable Conversion: advertised SKU. Conquest: the routed-to SKU (never the competitor's price). Discovery: campaign-blended AOV until a child is confirmed | [PB] |

Why per SKU: colours of the same size differ widely. Example (B6): Queen White $19.51/unit vs Queen Olive $12.43/unit; the product blend was $18.81 ($18.18 at deal price), and the engine's $26.60 "profitability" figure put every ceiling ~40% too high — 154 of 180 ranking campaigns were already paying above true break-even at the top.

### 3.2 Break-even ACoS
- **Break-even ACoS = margin/unit ÷ price** (ASP; deal price in a deal). [B6, PB]
- Target ACoS for non-ranking rows = break-even. [B6]
- State break-even ACoS beside CPA-vs-ceiling on every push or cut; if the two disagree, flag it — never resolve silently. [PB]
- Example (B6): 23.8% break-even ACoS; 2× = 47.6%.

### 3.3 Fee-contamination fallback [SR]
If fees ÷ ASP > **55%**, the fee line is contaminated. Replace: fee/unit = **portfolio median fee/ASP × ASP**, median taken from clean SKUs only (≥ **10 units**, 0 < ratio ≤ 55%). Log "verify with Brand Management".

### 3.4 Sanity band and missing data
1. Break-even ACoS outside **5–70%** → flag the SKU; never use silently. [SR]
2. SKU with < 10 units: use the same-size median margin (SKUs with ≥ 10 units and positive margin), never higher than the SKU's own figure. [WB]
3. SKU with no economics at all → **halt pricing for that SKU**. Never fall back to a global default (the engine's silent 19.86% default is a known defect). [SR defect, 13 §3]
4. Negative margin → no click price can be profitable: affordable CPC = 0, leave the bid, no raises, refer to Brand Management (price/COGS/fees). Pull a 60–90-day window before recommending a stop. A negative margin is never "rescued" by a sibling's figure. [PB, WB, SR]

### 3.5 Freshness and change events
| Trigger | Action | Tag |
|---|---|---|
| Margin table > **45 days** old | Stale: blocks every ceiling-referencing verdict until refreshed | [SR, PB] |
| Any price, FBA fee, size-tier, remeasure, packaging, freight or LTSF change | Re-derive margin and ceilings within **48 h** | [PB] |
| Pending dated COGS change | Carry two columns: current-COGS margin (drives all live decisions) and future-COGS margin (context only) | [PB] |
| CVR drop coinciding with a logged price rise | Hold bids; revert the price, or accept it and recompute break-even, ceilings and targets before any verdict resumes | [PB] |
| AOV shift from a variation-mix change | Every ceiling and verdict on the old AOV is void; refresh economics and **re-run** the row (not patch) | [PB] |
| Economics differ > 10% from the value logged when an action was taken | Grade that action PROVISIONAL (no credit/blame) — see 10 | [SR] |
| Sellerboard true-up | Monthly | [PB] |

### 3.6 Re-route rebuild
Every change of advertised SKU (any cause) → rebuild margin, break-even and ceilings from the new SKU in the same write; reset CVR baseline, rank clock and ROS lift. Ceilings priced on a departing SKU are void. [PB, B6]

### 3.7 Aged stock — forward-cash economics
For units already aged or carrying LTSF: COGS is **sunk** and never enters the live decision column. Use forward cash: net proceeds/unit = price × (1 − discount) − referral − FBA fee, compared against salvage value and LTSF until sold. The deal (price/promo) is the clearance lever; PPC supports visibility. Full math, floor price and routing in `04-inventory-sku-ltsf.md`. [PB, LTSF]

---

## 4. Break-even CPC per placement and the conversion basis

**Break-even CPC = margin/unit × conversion rate of the placement being bought** (top of search, rest of search, product pages each separately). [B6, PB, DR]

Conversion basis (register #2) [B6]:
| Own placement clicks (90 d, campaign grain) | CVR used |
|---|---|
| ≥ 50 | Own placement CVR |
| 15–50 | Linear blend: w = (clicks − 15) ÷ 35; CVR = w × own + (1 − w) × size rate |
| < 15 | Size's placement rate for that placement (product rate if the size has none) |

Rules:
1. Placement data is campaign grain; any keyword-level placement split is an estimate — label it. [B6]
2. Exclude the last 7 days from CVR (7-day attribution settles late). [B6]
3. Deal days: separate deal-state CVR (§10); in-deal CVR never raises a clean-state ceiling. [PB]
4. Never set the planning CVR equal to the baseline being judged (circular). Baseline = the product's live CVR per placement each cycle. [PB]
5. Amazon suggested bids / "market price" are **not** inputs to any price. [B6 owner rule, register #18]

Arithmetic example (illustrative): margin $19.51 × TOS CVR 20% = break-even TOS CPC $3.90; ranking ceiling 2 × $3.90 = $7.80.

---

## 5. Ceilings and push price

| Row | Placement | Ceiling (default) | Tag |
|---|---|---|---|
| Ranking push term (goal gate passed, qualified — 06) | Top of search: **TOS price = base × (1 + boost)** | **2 × break-even TOS CPC** | [B6, register #3] |
| Ranking push term | Rest of search | 1 × break-even; lifted to ceiling only after 15+ ROS clicks converting ≥ the campaign's product-page rate, else runs at base | [PB] |
| Ranking push term | Product pages (base only, no modifier) | 1 × break-even PDP CPC | [PB, WB] |
| Ranking term at/beyond target (HOLD RANK) | TOS | Keep current price (≤ push ceiling), no raise; after 2 clean weeks taper ~10%/week to 5–10¢ under the placement's blended CPC (06) | [B6 R-P8, register #26] |
| Ranking campaign, not pushed | All | 1 × break-even. Walk down: 0 TOS clicks in 30 d → straight to BE; with TOS clicks → step down ≤ 50% per step toward BE, restore one step if rank falls > 10 places; price ≤ BE → hold | [B6 R-B1–B3] |
| All non-ranking objectives | Every placement | **≤ 1 × break-even CPC** | [register #3] |
| Conquest (competitor product targets) | Product page | ≤ break-even CPC; watch-CPA = lower of margin × CVR and a price-gap-adjusted figure (state which governs) | [B6, PB] |
| Discovery launch | — | Broad ~60%, Phrase ~80% of the Exact row's break-even price; no placement modifier at launch | [PB] |
| Cold candidate on a thin margin | — | CPC ≤ ~⅓ of margin/unit | [PB] |

Hard bounds on every write: TOS boost ≤ **900%**; base ≥ TOS price ÷ 10; base floor $0.35–0.50 (below it Amazon suppresses eligibility); the $0.50 minimum bid (provisional) loses to any lower ceiling. [B6, WB, SR, PB]

**Push price** (ranking push terms only) [B6, register #4]:
- Push price = break-even TOS CPC × (1 + premium), **capped at the ceiling**.
- Premium = +25% if rank ÷ target ≤ 1.5; else (rank ÷ target − 1) × 50%.
- Example: rank 30, target 10 → ratio 3.0 → premium 100% → push price 2 × BE = the ceiling.

Ceiling rules:
1. **Price above ceiling → cut to ceiling now.** Never deferred, never "owned by a later descent". Applies to raises and holds alike. [B6 R-P5]
2. Row under 15 clicks but over ceiling → formula-only correction to ceiling in one cycle; next cycle check for suppression (clicks collapse → fixed-bid trial, 07). [PB]
3. **Qualification:** a term is pushable only if its ceiling ≥ our current TOS cost per click; otherwise **WAIT** for an owner decision on a time-limited ceiling raise. [B6 R-P1, F25]
4. At ceiling **3 days** without top-3 sponsored position and ≥ 30% TOS impression share → **REVIEW** (owner decision): raise that term's ceiling for a stated period, or swap the term. [B6 R-P6]
5. TOS CVR below market on 50+ TOS clicks → stop the push, back to break-even. [B6 R-P7]
6. Up-and-down bidding doubles the TOS price the auction may charge: authorised TOS CPC = base × (1 + boost) × 2.0; breach if > ceiling × 1.05 → re-solve base = ceiling ÷ ((1 + boost) × 2.0). [SR]
7. Realised CPC ÷ target price > 1.0 = push-only territory; > 1.5 = unjustifiable, correct this cycle. [SR]
8. No price ever derives from a click requirement; click plans size volume and budget only. [B6 F21]

**Alternatives (owner settings, not defaults):** flat account ranking cap ~$8–9 with per-SKU margin only tightening it [PB, WB]; placement overlay 1.30 × break-even with push at 0.75 × [PF]; margin × CVR on every row including ranking (1×) [DR]. Record which the owner chose.

---

## 6. Objective ACoS bands and the layered non-ranking rule

### 6.1 Objective bands (reference — they report, break-even triggers) [SR]
| Objective | Band (max ACoS) | Note |
|---|---|---|
| Ranking / re-ranking | 50–80% | Reference only; ranking is judged on rank vs loss ceiling, never weekly ACoS |
| Market Share | 25–50% | Only when declared |
| Discovery | 15–30% | Core bid capped at break-even |
| Profitable Conversion | 15–25% | ≤ break-even |
| Defensive | 10–15% | |
| Brand Defensive | 5–10% | |
| Competitor / Conquest ASIN | 10–15% | |
| LTSF clearance | up to 50% | Reference only — the ceiling is 1 × break-even on forward-cash economics (13 #43) |
| Unknown | 25% | |

- Target ACoS = **50% of break-even**; Max acceptable = **75% of break-even** (house reporting thresholds). [SR, QA]
- RPC bid math: RPC = sales ÷ clicks; RPC ceiling = RPC × break-even ACoS; suggested bid = RPC × band max; **target bid = min(suggested, RPC × break-even)**. [SR]
- A band breach alone never cuts a row; only break-even does. [B6 F31]

### 6.2 Layered non-ranking rule (register #16) — first match wins
| # | Condition (non-ranking row) | Decision | Tag |
|---|---|---|---|
| 1 | < 15 clicks (30 d) | MONITOR — no change | [B6 E3] |
| 2 | ACoS > **2 × break-even** on ≥ 30 clicks (90 d) | Stop — proposed for owner confirmation (REVIEW, interim one CUT step; 06 §4.1): discovery term → BLOCK (negative exact); product target → pause / negative ASIN; in the term's exact owner: REDUCE | [B6 R-K3, R-X5] |
| 3 | ACoS > break-even on **both** 30 and 90 days, ≥ 15 clicks | CUT: base × BE/ACoS, i.e. cut −(1 − BE ÷ ACoS), **max −30% of base per step** | [B6 R-N1] |
| 4 | ACoS > break-even on 30 d but inside on 90 d | MONITOR (watch) | [B6] |
| 5 | ACoS ≤ **50% of break-even** with orders | SCALE-eligible: raise ≤ +25%/cycle, never above the 1× ceiling | [register #16, #5] |
| 6 | Otherwise | KEEP | — |

Magnitude inside rule 5 (provisional — confirm with owner before first use): CONFIRMED 15+ clicks / 2+ orders / CPA ≤ ~70% of ceiling → hold; STRONG 30+ / 3+ / ≤ ~60% → up to +10%; PROVEN 50+ / 5+ / ≤ ~50% → up to +15%. [PB]

Exceptions: LTSF/liquidation campaigns are not cut on ACoS — judged on stock cleared [B6 R-N2]. Brand Defensive judged on ACoS ≤ break-even plus share held [B6 R-N3, PB]. Deal days: no verdicts; bleed stops still run (§10).

---

## 7. CPA ceiling and clicks-to-loss

- **CPA = CPC ÷ CVR.** [PB, B6]
- **CPA ceiling:** non-ranking rows ≤ margin/unit (= break-even); ranking push at ceiling ≤ 2 × margin/unit (bounded loss per push order, still below the order value). Applies to Profitable Conversion, Defensive, Discovery, Conquest — **not** to Ranking inside its push window. [B6 R-F3, PB]
- CPA > 8 × ceiling → a single cut up to 50% is allowed. [PB]
- **Clicks-to-loss = margin/unit ÷ CPC** — the clicks per order at which a row breaks even. Example: $10 margin ÷ $4 CPC = 2.5 clicks per order. A row whose clicks-per-order (1 ÷ CVR) exceeds this loses money on every order. [PB]
- Zero orders on a thin sample = unknown, not zero CVR (see 06 zero-order rule: ≥ 20 clicks). [PB, B6]

---

## 8. Weekly loss ceiling for ranking pushes

- **Weekly loss ceiling = (push ACoS − break-even ACoS) × projected ad sales at the required spend**; never less than one day's spend; basis stated on the row. [PB, WB]
- Hitting it = **REVIEW** flag to the owner, not an automatic stop. [PB]
- Margin rule check (weekly): if product margin after ads falls below the owner's margin rule, cut pushes **from the bottom of the funded list** (funding order = revenue potential at target rank ÷ cost to close the gap). [B6 R-F6, PB]
- Example: push ACoS 38%, break-even 23.8%, projected ad sales $6,000/wk → loss ceiling (0.38 − 0.238) × $6,000 = $852/wk.

---

## 9. Spend limit, margin rule and event exceptions

| Rule | Detail | Tag |
|---|---|---|
| Spend limit | Owner-set daily/weekly $ for the product. **Refuse to size any push without one** | [B6 F03] |
| Margin rule | Owner-set, e.g. keep product margin after ads ≥ 10%. Margin after ads = (profit before ads − ad spend) ÷ sales | [B6] |
| Check | Push budgets + expected other spend ≤ limit. If over → scale push budgets down, cutting from the bottom of the funded list | [B6 R-F5, E19] |
| Spend basis | Product basis: campaign rows can include other products — product spend = row spend × (product tile ÷ row total). Shared multi-product campaigns are excluded from this product's price automation | [B6] |
| Not a TACoS rung | Never size spend on a TACoS "rung" or envelope unless the owner has set a TACoS target | [B6 F24] |
| Budgets | Push budget = plan clicks × price (+ expected product-page spend); ≥ required × 1.05, rounded up; budgets load **with** their price rows or not at all | [B6, PF, F14] |
| Minimums / referrals | Budget < $10/day → raise to $10; budget > $500/day → refer for review; budget moves > $50/day → human confirm | [SR, PB] |
| Event exception | Must be **explicit, time-boxed (dates), with the margin it produces stated**, approved before the event, never retroactively | [B6, PB] |

Example (B6): spend limit **$1,300/day on 29–30 Sep** — a stated two-day exception to the 10% margin rule, producing **~7% margin after ads** for those deal days; from 1 Oct the limit was reset by the post-deal audit.

---

## 10. Deal-state vs clean-state economics (event mode)

Deals distort price, margin, CVR and AOV at once (register #27). Rules:
1. **Compute deal-state margin, break-even and ceiling before the event** from deal price, net of deal fees (fixed + % of deal sales, stated separately from referral/FBA). A discount cuts contribution by its full depth, so the ceiling falls faster than the discount %. [PB]
2. Keep deal-state and clean-state **separately**: margin, CVR baseline, rank arc, sufficiency count. Never blend. The clean arc governs verdicts. [PB]
3. **No verdicts on deal data**: no ACoS/CVR judgement on a window with > 2 deal days; no new campaigns, folds or structural changes on deal days. [B6 E1, F01]
4. **Bleed stops still run** mid-deal (negations, placement leak cuts); a real loss (ACoS > deal-state break-even) is cut even mid-deal; gradual target-chasing cuts wait. [SR]
5. In-deal CVR never justifies a bid above the deal-state ceiling. [PB]
6. Deals **amplify an already-decided, gated push; they never originate one.** [PB]
7. Pre-event: set budget caps in advance; remove dayparting boosts; stage the bid plan against **max-sales-day** days of cover (04). Live: check pacing the same day against the event projection. [PB]
8. Post-event: exclude event days from trend reads for **2 weeks**; taper event bids over **3–5 days**; allow the 7-day attribution settle before any read. Floors/ceilings return to pre-event values unless the event produced durable evidence (e.g. sustained higher rank). [SR, PB, B6]
9. Deal report: sales, units, glance views, deal-page CVR, contribution at deal-state margin net of deal fees, net contribution before ads. [PB]
10. Pacing deviation > ~25% from the product's day-of-week curve → flag the same day. [PB]
11. Deployment sequencing: ceiling-math structural fixes deploy now; cut batches and launches that need clean-week CVR wait for the window to close. [PB]

---

## 11. TACoS — monitor and decompose (owner has not set targets)

**Default: TACoS is reported and explained, never a target, gate or bid input** (register #17). [B6 owner rule]

- TACoS = ad spend ÷ total sales (refund-net). [SR]
- Decompose every movement: TACoS = ACoS × (ad sales ÷ total sales). Report which moved — ad efficiency, paid share of sales (organic change), or both — and split by objective (push vs non-push) and by event days. [PB]
- A high TACoS is legitimate only alongside a gated push, a Green SKU and real rank movement. [PB]
- Never an across-the-board % cut to fix TACoS; any response runs the per-row decision order. [PB]

**Reference only — apply only if the owner sets a TACoS target:**
| Item | Values | Tag |
|---|---|---|
| Stage bands | Launch ≤ 25% (another source says 35–45%; 25% if asked), Ranking push 12–15%, Transition 8–12%, Mature 4–7%, Harvest ≤ 4% | [PB] |
| By weeks since current push | 1–6: ≤ 1.5 × BE ACoS · 7–12: < BE · 13–25: < 0.75 × BE · 26+: < 0.5 × BE | [PB] |
| Envelope | Weekly spend = target TACoS × projected weekly revenue; one pre-approved event week may run +50% | [PB] |
| Tiers (actual ÷ band) | Within ≤ 1.2× · Elevated 1.2–1.5× · Breach 1.5–2× (freeze new scale) · Code-red > 2× or > 1.5× for 2 weeks (freeze scale, per-row review within 48 h, daily cadence; exit after 2 clean weeks) | [PB] |
| Other house refs | Phase-4 TACoS ceiling 12%; organic sales floor 60% | [QA] |
| Routing use | TACoS ≤ 50% BE + broad-type row + orders > 0 + ACoS > BE + no aged/deal → hold bid and negate | [SR] — not applied by default |

---

## 12. Marginal ACoS unwind rule

After any scale step (bid, boost or budget raise), read the **step**, not the new blend:
- **Marginal ACoS = Δ spend ÷ Δ ad sales** across the two periods the step spans (marginal CPC = Δ spend ÷ Δ clicks). [PB, SR]
- Marginal ACoS > **1.5 ×** the running average → saturation: **freeze** further raises; record the prior rung (price and date). [SR]
- Marginal ACoS > **2 ×** the running blended ACoS → **unwind** the step to the prior rung, however acceptable the new blend looks. [PB]
- Judge only executed steps with ≥ 15 fresh clicks and no deal days in either period (10).

---

## 13. Human-confirm thresholds

Flagged rows are still written in full; they are marked for the reviewer, with the trade-off in the reviewer's units ("holds ~$180/wk of saving to keep ~66 orders/wk at $5.60 per order"). [PB]

| Trigger | Tag |
|---|---|
| Action on a keyword at ≥ 500 search volume | [PB] (13 #41, #54 — the WB 250 figure is not used) |
| Any gate failure on the row (inventory, provenance, budget truncation, other) | [PB] |
| Structural change: new campaign, routing/colour switch, match-type change, bidding-strategy change | [PB, B6 E8] |
| Bid move > 25% of current outside an approved push plan (an approved plan covers its own +30%/day steps) | [PB, 13 #41] |
| Budget move > $50/day; budget > $500/day | [PB, SR] |
| Spend envelope/limit change > 20% | [PB] |
| Ceiling raise for a named term (at ceiling 3 days without holding the top) | [B6 R-P6] |
| Weekly loss ceiling reached | [PB] |
| Provisional rule used for the first time on a product (goal gate, Defensive/Conquest allowances, harvest, sufficiency exit, graded push tiers, $0.50 floor) | [PB] |
| Negative or out-of-band (5–70%) break-even; fee contamination fallback used | [SR] |
| Terminal inventory call (removal, liquidation, disposal) | [LTSF] |

---

## 14. Financial guardrail checklist (quality gate — every item must return 0)

1. Any row priced from a blended parent, category, global default or another product's margin.
2. Any row whose margin is > 45 days old, or predates a logged price/fee/packaging change, used for a ceiling verdict.
3. Any break-even outside 5–70% or negative, used without a flag.
4. Any ranking-push TOS price > 2 × break-even TOS CPC (or the owner's chosen alternative).
5. Any non-ranking price > 1 × break-even CPC at any placement.
6. Any over-ceiling price left in place ("deferred").
7. Any ranking allowance on a product whose goal is not Growth or Mixed (or undeclared and unconfirmed), or on a syntax in chronic Conversion.
8. Any push where ceiling < current TOS cost per click (should be WAIT).
9. Any raise > +30%/day on a push, > +25%/cycle elsewhere; any gradual cut > 15%/cycle, non-ranking ACoS cut > 30% of base, or base cut > 50% per step (13 register #5).
10. Any boost > 900% or base < TOS price ÷ 10.
11. Any price derived from a click requirement or from Amazon suggested bids.
12. Push budgets + expected other spend > the stated spend limit, with no dated, margin-stated exception.
13. Any spend sized on a TACoS target the owner has not set.
14. Any verdict computed on a window with > 2 deal days, or any launch/fold on a deal day.
15. Any in-deal CVR used to lift a price above the deal-state ceiling.
16. Any weekly loss ceiling missing its basis on a push row.
17. Any executed scale step with marginal ACoS > 2 × blend left in place.
18. Any flagged human-confirm row without its trade-off stated.
19. Any budget row loaded without its price row, or vice versa.
20. Break-even ACoS not stated beside CPA-vs-ceiling on a push or cut row.

---

## 15. Open questions for the owner

1. **Marginal-step thresholds:** Resolved — see 13 #34: freeze at marginal ACoS > 1.5 × average, then unwind one step at > 2 × blended.
2. **LTSF-clearance ceiling:** Resolved — see 13 #43: 1 × break-even on forward-cash economics (COGS sunk); the 50% ACoS band is reference only.
3. **Search-volume trigger for human review:** Resolved — see 13 #41 / #54: SV ≥ 500 for both mandatory confirm and the Change Review Sheet.
4. **Defensive above-ceiling allowance** (PB: only with verified competitor presence on the brand term, withdrawn after 2 reads without it): partly resolved — 13 #45 allows 2 × break-even for Sponsored Brands / video on brand terms with verified competitor presence. For Sponsored Products brand rows it is not adopted by default (≤ 1 × break-even). Adopt for SP?
5. Organic-share graduation target and ad-dependency ceiling for demotion: no house default — set per product.


---

<!-- FILE: references/04-inventory-sku-ltsf.md -->
# FILE: references/04-inventory-sku-ltsf.md

# 04 — Inventory, variations and LTSF

Read in Phase 2. Output of this file: **which variation each campaign should advertise, which SKUs block pushing, and what to do with aged stock.** Economics used here (margin, break-even, ceilings) come from `03-profitability-and-guardrails.md`.

Source tags: [INV] inventory checkup · [LTSF] LTSF dossier · [PB] plan builder · [WB] workbook builder · [PF] placement-first · [SR] optimization engine · [DR] decision reasoning · [PH] phasing · [B6] B6 engagement, Sep 2026.

## Contents
1. Inputs and counting rules
2. Velocity and cover formulas
3. Stock-out-before-arrival test (ROOM / TIGHT / SWITCH)
4. Zones Green / Yellow / Red and actions
5. Projected days of cover through checkpoints
6. Push stock gate
7. Variation roles and routing rules
8. SKU provenance, halo rate, economics rebuild
9. Backup switch simulation
10. Recovery push
11. Inbound onto overstock, trajectory and peak-week rules
12. Distorted-window velocity correction
13. Inventory × PPC decision table
14. LTSF and aged inventory
15. Anti-patterns
16. Open questions for the owner

---

## 1. Inputs and counting rules

| Input | Fields | Rule | Tag |
|---|---|---|---|
| Inventory export per SKU (full, unfiltered — never the variation page) | SKU, ASIN, available, reserved, on-hand, units in production, units shipped/in transit, next in-stock date (date / "Today" / "Not in horizon"), planned daily velocity | Read the unfiltered file before filtering; audit on-hand − available − reserved: gap > **5 units** → verify at source before zoning | [INV, PB, PF, WB] |
| Product Ad rows (bulk) | advertised SKU per ad group, state | The only source of routing (§7) | [WB] |
| Advertised product / targeting report | 7-day advertised SKU units, spend | Spend > 0 = actively advertised | [INV] |
| Preferred → Backup pairs | per size/syntax | **Ask the owner to paste them. Never auto-derive.** Dedupe repeats | [INV] |
| Lead time | days | Default **90 days** (confirm) | [INV] |
| Aged inventory / LTSF charge file | units per age bracket (all 8), cu ft per unit, invoice | See §14 | [LTSF] |
| Deal calendar | dates, SKUs, deal price | Needed for distorted-window correction (§12) and event cover | [B6, PB] |

**Counting rules** [B6 R-I6, WB]:
1. Count **available** units plus **dated, confirmed** arrivals within the horizon. Transfers count toward replenishment only; customer orders never count.
2. Inbound counts toward cover only if its ETA ≤ the SKU's current days of cover; otherwise there is a gap before it lands.
3. Stock status comes from velocity + inbound + lead time, **never from "units > 0"**. [SR]
4. If a report has no SKU column, map campaign → SKU by name substring, **longest SKU first** (CALIFKING before KING), fallback ASIN substring — then verify against Product Ad rows. [INV]

---

## 2. Velocity and cover formulas

| Metric | Formula | Tag |
|---|---|---|
| Units/day (gating pace) | Units sold ÷ days, **30-day window**; 7-day pace shown as an early warning | [B6] |
| Planned velocity | Inventory file's planned daily velocity ("Base SV") — show beside the actual; gate on the 30-day actual | [INV, 13 #49] |
| PPC daily velocity | Σ 7-day advertised SKU units ÷ 7 (context: how much the ads move) | [INV] |
| Days of cover (available) | Available ÷ units/day | [INV, B6] |
| Total days incl. inbound | (Available + dated inbound in horizon) ÷ units/day | [INV] |
| Days to next arrival | Next dated arrival − today ("Today" = 0; none = blank → "no scheduled arrival") | [INV, B6] |
| Max affordable velocity (stock only) | Available ÷ lead time | [INV] |
| Max affordable velocity (incl. transit) | (Available + transit) ÷ lead time | [INV] |

Never compute cover on a push pace or an engine forecast — an inflated pace invents stock-outs. Example (B6): "White runs out at push pace 3 days before arrival" moved 75 Queen campaigns to the 7th-best colour; on the 30-day pace there was no stock-out. [B6 F30]

**Per-SKU velocity status (diagnostic, first match)** [INV]:
| Condition | Status | Implied action |
|---|---|---|
| Arrival scheduled and cover < days to arrival | OOS RISK | Protect: cut PPC aggression, pause ranking pushes until the shipment lands |
| Velocity > max affordable velocity (stock only) | Demand outruns stock | Reduce PPC aggression / slow velocity |
| Velocity < max affordable velocity (incl. transit) | Healthy | PPC OK — continue / scale carefully |
| Otherwise | Stable | Hold and monitor |
Sort: OOS RISK → Demand outruns stock → Stable → Healthy, then days left ascending. Zones (§4) still govern the decision; this status explains it.

---

## 3. Stock-out-before-arrival test

Run for every advertised SKU with a dated inbound. Cover on the 30-day pace. [B6, INV, register #9]

| Result | Condition | Zone | Action | Tag |
|---|---|---|---|---|
| ROOM | Cover ≥ days to next arrival | per §4 | Push allowed only if cover ≥ days to arrival **+ 7** and the SKU is Green | [B6 R-I2, register #9] |
| TIGHT | Cover < days to arrival by **≤ 7 days** | **Red** | Ease (taper) the push so stock lasts to the arrival; **no colour swap** — a swap costs more than a short ease | [B6 R-I3] |
| SWITCH | Cover < days to arrival by **> 7 days** | **Red** | Switch ranking ads to the size's backup colour (same size, same price) if the backup passes §9 | [B6 R-I4] |
| OUT | Available = 0 | Red | Pause the push; ranking ads to backup | [B6 R-I5] |
| — | Available < 7 days of cover | Red | No push; break-even pricing only | [B6 R-I1] |
| No arrival | No dated inbound | per §4 | Zone by cover alone | [INV] |

Why: stock-out before inbound arrives destroys rank regardless of how many days of cover the headline figure shows.

---

## 4. Zones and actions (resolved defaults)

| Zone | Condition (advertised variation) | Action | Tag |
|---|---|---|---|
| **Green** | ≥ **60** days of cover, and no stock-out before arrival | Push and scale allowed (other gates permitting) | [PB, WB] |
| **Yellow** | **21–59** days | **No new push, no raises; keep current spend**; write a dated re-entry plan: restock date, keywords resuming, target rank each resumes at | [register #10, PB] |
| **Red** | **< 21** days, **or** stock-out before inbound arrives (TIGHT/SWITCH/OUT) | Protect: taper to defence; re-point the same day to the next viable child of the same size (§7); no bids on zero-stock rows unless re-pointed | [PB, WB, PF, register #9] |

Rules:
1. Re-point order: follow the syntax's priority list; check each candidate's own zone; skip Yellow/Red; among viable children pick by velocity, margin and recent CVR (tie: higher CVR at lower CPC, then longer clean history). **All children Red → escalate as a supply problem.** [PB]
2. Taper size on Red rows: gradual cut cap (≤ 15%/cycle) unless the re-point makes the cut unnecessary; during a deal hold price and watch the stock-out date. [SR]
3. A Red child that is still selling keeps its ad; an ad is paused only at zero stock or on the owner's approved list. Re-pointing = enable/add the next child's ad. [WB]
4. Every Yellow/Red hold carries its dated re-entry plan; a hold without one fails the quality gate. [PB]
5. New campaign launch needs the routed SKU ≥ **21 days** of cover (launch floor, not the 60-day push gate); else no campaign. [PB]
6. New or added traffic (launches, re-points onto the SKU, raises) only while the SKU is Green (Yellow: keep current spend, no raises) **and** margin > 0; Red rows are tapered or re-pointed, not grown (rule 3). [WB, 13 #10]
7. The engine's 14/30-day bands are superseded (lead times of 60–90 days make them too late). [register #9]

---

## 5. Projected days of cover through checkpoints

- **Projected cover at checkpoint** = (available + dated inbound landing by then − (baseline units/day + the push's extra units/day) × days to checkpoint) ÷ baseline units/day. [PB, WB]
- Projected cover must stay **Green (≥ 60 days) through the push checkpoint** (13 #42). A push whose projected cover drops into Yellow or Red before its checkpoint is **blocking**: shrink the rank gap, wait for the inbound, or get an explicit time-boxed owner acceptance. [PB]
- Log the conflict to the Supply Chain register: SKU, projected date it leaves Green, the push causing it, fix (expedite, PO date, safety stock). [PB]
- Events: stage the bid plan against **max-sales-day** days of cover, not average daily cover. [PB]

---

## 6. Push stock gate (all must pass for PUSH)

1. Advertised variation is the size's hero (or its approved backup after a switch). [B6 R-C1]
2. Zone **Green** (≥ 60 days, 30-day pace). [PB]
3. Cover ≥ days to next dated arrival **+ 7**. [register #9]
4. Available ≥ 7 days of cover. [B6 R-I1]
5. Projected cover stays Green through every checkpoint (§5). [PB]
6. No trajectory flag (§11). [PB]
7. For a clearance push: the hero of that size is not Red. [SR]
Fail any → WAIT (name the failing item and its re-entry date).

---

## 7. Variation roles and routing rules

| Role | Definition | Advertised by | Tag |
|---|---|---|---|
| **Preferred / hero** | The size's best seller (Example (B6): White in every size; Twin used Sage Green while White was 0) | Ranking campaigns; brand/defensive campaigns | [B6 R-C1, R-N3] |
| **Backup** | Owner-named same-size alternative | Ranking campaigns when the hero fails §3 | [B6 R-C6, INV] |
| **Clearance colour** | Per size: ≥ **180 days** of cover, or ≥ **90 days** while selling ≤ the size's median velocity | Discovery (auto/broad/phrase) campaigns | [B6 R-C2] |
| **Named colour** | Colour in the search term | Campaigns on colour-named terms | [B6 R-C3, PH] |

Why: rank accrues to the hero; discovery traffic is broad and cheaper, so it should move slow stock while the hero's stock is reserved for ranking.

Routing rules (register #29):
1. **Read routing from Product Ad rows, never from campaign names.** In one audited account, 212 of 251 name-derived routings were wrong. [WB]
2. Ranking advertises the size's best seller; discovery advertises the clearance colour; colour-named terms advertise the named colour in the term's size. Sizeless terms → the size hero, else the product hero. [B6, SR]
3. **Size never changes** on any switch — hard block (only exception: correcting a wrong size). [B6 R-C4, E9]
4. Never add or switch to a colour with < **7 days** of cover. [B6 R-C5]
5. Attribute in the query (size/colour) routes only to the matching SKU; if that SKU is OOS, hold at the bid floor — no substitute. Close colours only where the account has ruled them equivalent. [PB, WB]
6. Colour target is set per objective before any other write on the campaign. [B6]
7. Switches are applied by hand (they do not upload), flagged for human confirmation, with size confirmed unchanged. [B6 E8]
8. Backup self-competition: if the backup is already advertised in another campaign, say "swapping competes with its own campaign"; else "clean to redeploy". [INV]
9. Transition back: suggest (never auto-swap) returning to the preferred SKU when its cover > **21 days**; pushing resumes only when it is Green again. [SR]
10. Live keyword for another product form (off-listing, e.g. for sheets: body, travel, sham, toddler, protector, insert, topper) → pause. [WB]
11. Foreign SKU (another product's child) in this product's campaign = finding. Shared multi-product campaigns are excluded from colour and price automation; decide them in their own product's audit. [WB, B6 E13]
12. Shared head term across sibling products: owner = highest **margin/order × sibling CVR on the shared root × sibling inventory days**; exact tie → human. [PB]
13. Routing actions: REPRICE TO ROUTED CHILD (bid only) ≠ SWITCH AD (two ad rows: enable new, keep/pause old). A held row with a Green sibling → SWITCH AD; Yellow sibling → time-boxed switch with a flip-back date; none → stay paused, naming the siblings checked. [WB]

---

## 8. SKU provenance, halo rate, economics rebuild

Before reading any CPA, CVR or rank on a row, establish **which SKU was advertised over the window** (Product Ad states over the long window and both 7-day windows). [PB §11, WB]

| Case | Meaning | Action | Tag |
|---|---|---|---|
| **Match** | Intended SKU advertised all window | Proceed | [PB] |
| **Mismatch** | Another SKU advertised all window | Correct price now if over the correct SKU's ceiling; read cleanly forward only | [PB] |
| **Mixed** | Changed mid-window | Use the post-change portion if ≥ 15 clicks; else formula-only corrections | [PB, WB] |
| **Wrong from the start** | Clear majority of conversions belong to another variation | Routing error: re-point, rebuild ceilings on the true margin/AOV, reset CVR baseline and rank clock | [PB] |

- **Halo rate** = units shipping on a non-advertised SKU ÷ total units attributed to the ad. Cite it on every re-route (e.g. basket sales incl. halo reached 81% in one product). [PB, PF]
- **Economics rebuild on re-route** (any cause): margin, break-even, ceilings from the new SKU in the same write; reset CVR baseline, rank clock, ROS lift. [PB, B6]
- Mass re-route: a pooled placement estimate may stand in, never as a shared verdict; each row graduates when **it** reaches 15 clicks on the correct SKU. [PB]
- Rank collapse concentrated in one colour/size family during an outage = **stock signature**, not a demand or relevance problem. [LTSF]

---

## 9. Backup switch simulation

Only for pairs whose preferred SKU is currently advertised. Apply the **preferred SKU's velocity** to the backup. [INV]

- Backup cover (stock) = backup available ÷ preferred velocity.
- Backup cover (incl. transit) = (backup available + transit) ÷ preferred velocity.

| Verdict | Condition | Written recommendation |
|---|---|---|
| **No — backup also OOS** (red) | Backup stock + transit = 0 | Needs production |
| **Yes — covers full lead time** (green) | Cover incl. transit ≥ lead time (default 90 d) | Switch fully sustains until replenishment |
| **Partial** (amber) | Cover incl. transit ≥ **30 days** | Partial bridge; watch |
| **No — only N days** (red) | Otherwise | Insufficient |
Extra wording: backup stock 0 but transit > 0 → "covers only after transit lands". Suffix per §7 rule 8. The switch also needs backup cover ≥ 7 days today (§7 rule 4).

---

## 10. Recovery push

Conditions (all): SKU back to Green; its best rank in the last 12 months was top 5–10; CVR ≥ benchmark; the loss is logged as an inventory cause. → Fund to the **pre-decline baseline**: week 1 re-point + maintenance, week 2 push, checkpoint at week 3. Recovery candidates inherit their prior ceiling and are funded before an equal Cold candidate. [PB]

---

## 11. Inbound onto overstock, trajectory and peak-week rules

1. **Inbound onto overstock:** compare units in production + transit with current days of cover and the product's cover ceiling. Inbound landing on an overstocked product regenerates LTSF exposure — a clear-only plan that ignores it treats the symptom. Cover ceiling: **Owner decision — ask** (engine carries an unused 120-day overstock marker). [LTSF, SR]
2. **Trajectory:** ≥ 60 days of cover with velocity down **15% WoW for 3 consecutive weeks** = cover rising because demand is falling. Not safe to push; diagnose first. [PB]
3. **Peak week:** where a demand calendar or deal schedule marks a week as peak, peak-week availability outranks aged-stock/LTSF economics (peak stock-out costs ~3× to recover; excess past peak only costs storage). Only when a calendar actually marks the week. [PB]
4. RED tier LTSF SKUs freeze future purchase orders (§14.5). [LTSF]

---

## 12. Distorted-window velocity correction

Never take velocity from an OOS, suppressed or deal window at face value. Record: trailing velocity, correction factor (e.g. 0.67), and its basis (which days removed, what replaced them). An unstated haircut or uplift is an untagged assumption and is **rejected**. [LTSF] Deal days are excluded from settled reads for 2 weeks (03 §10). [SR]

---

## 13. Inventory × PPC decision table

What each stock state allows, per objective, for the variation a campaign advertises. First apply 03's economics; this table only restricts further.

| Stock state | Ranking (push terms) | Ranking (HOLD RANK / non-push) | Defensive / brand | Profitable Conversion / Conquest | Discovery | Clearance (aged SKU) |
|---|---|---|---|---|---|---|
| **Green** (≥ 60 d, ROOM + 7) | PUSH allowed if goal gate + qualification pass | Hold / walk to break-even per 03 | Normal; keep on hero with enough budget | Normal; SCALE-eligible per 03 §6.2 | Advertise clearance colour; normal | Break-even PPC on forward cash; clearance push only if the size's hero is not Red |
| **Yellow** (21–59 d) | No new push, no raises; keep current spend; dated re-entry | Hold price; no raises | Hold; no raises | No raises; cuts per economics still run | No raises | No raises; continue ladder levers that are not PPC |
| **Red — TIGHT** (short ≤ 7 d before arrival) | Ease the push so stock reaches arrival; no swap | Ease; no swap | Ease; keep on hero | Taper | Must not advertise this SKU (clearance colour has ≥ 90 d) | n/a |
| **Red — SWITCH** (short > 7 d) or < 21 d | Stop push; re-point same day to backup (same size) if §9 passes; else taper to defence | Re-point or taper | Re-point to backup; keep the brand shelf | Taper ≤ 15%/cycle or re-point | Re-point | Never push; if hero Red, no clearance push on that size |
| **OUT** (available 0) | Pause push; ads to backup | Ads to backup | Ads to backup | No bids on this SKU | No bids on this SKU | — |
| **LTSF YELLOW/RED/CRITICAL** (§14.5) | Goal likely Clearance → no allowance (03 §1) | Standard ceiling | Unchanged | Standard ceiling | Route discovery to aged child | Ladder rung per §14.10; PPC is family 2 of 5 |
Always: ≤ 1 lever change per row per cycle; every hold names its re-entry date. [DR, PB, B6, SR, WB]

---

## 14. LTSF and aged inventory

Governing principles [LTSF]: rank options by **forward net recovery**; **COGS is sunk and never enters**; **floor = salvage parity, not break-even**; diagnose demand-curve defects before discounting; every decision has an expiry date.

### 14.1 Rate card — $ per **cubic foot** per month (never per unit)
Assessed on the **15th** of each month on the bracket held that day; surcharge starts at 181 days.

| Age (days) | $/cu ft/month | Per-unit minimum | × 181–210 rate | Rate one bracket later |
|---|---|---|---|---|
| 0–180 | 0.00 | — | — | 0.50 |
| 181–210 | 0.50 | — | 1.0× | 1.00 |
| 211–240 | 1.00 | — | 2.0× | 1.50 |
| 241–270 | 1.50 | — | 3.0× | 5.45 |
| **271–300** | **5.45** | — | **10.9× — the cliff** | 5.70 |
| 301–330 | 5.70 | — | 11.4× | 5.90 |
| 331–365 | 5.90 | — | 11.8× | 6.90 |
| 366–455 | 6.90 | $0.30/unit if greater | 13.8× | 7.90 |
| 456+ | 7.90 | $0.35/unit if greater | 15.8× | 7.90 |

- Effective $/unit/month = rate × cu ft per unit (from 366 d: the greater of that and the per-unit minimum).
- Reading it per unit overstates holding cost 1.4–4.8×. Examples: quilt set 0.704 cu ft → $3.84/unit at 271–300 d (per-unit reading $5.45 = 1.42× too high); satin sheet set 0.246 cu ft → $1.34 (3.7×). Same-age SKUs can differ 60% on volume, so allocation is not a pure velocity ranking. [LTSF]
- A flat-rate projection understates a batch approaching the cliff by up to 3.6×; always age units forward. [LTSF]

### 14.2 Fee defaults and timing [LTSF]
| Item | Default |
|---|---|
| Removal fee | $0.97–1.17/unit → use **$1.07** |
| Disposal fee | $1.07/unit |
| Liquidation recovery | 5–10% of ASP → **7.5%**; liquidation fee 2–3% → **2.5%** |
| Coupon redemption | $0.60 |
| 3PL handling (removal to resale) | $0.90/unit |
| Referral | 15% |
| Salvage resale value | 50% of price (replace with a real figure before any terminal call) |
| Critical product charge | $5,000/month |
| Months-to-clear cap | 12 |
Timing: units cleared or removed before the 15th avoid that month's charge; a removal order submitted by 23:59 PT on the deadline exempts the units even if unshipped. Outlet deals take 1–4 weeks to accept → submit **60–90 days before the cliff**; unaccepted as the cliff nears → price drop or removal now.

### 14.3 Decision math (run as a script; never hand-calculate) [LTSF]
```
Net proceeds/unit   = price × (1 − discount) − referral fee − FBA fee          (no COGS)
Removal net/unit    = resale salvage − removal fee − 3PL cost
Liquidation net     = price × recovery% − price × liquidation fee%
Disposal net        = − disposal fee
Salvage/unit        = MAX(removal net, liquidation net, disposal net)
LTSF/unit/month     = monthly charge ÷ aged units   (or rate × cu ft)
LTSF until sold     = LTSF/unit/month × min(months to clear, 12)
Floor price         = (salvage + LTSF until sold + FBA fee) ÷ (1 − referral%)
Break-even discount = LTSF until sold ÷ net proceeds at current price   (n/a if net ≤ 0)
Max combined depth  = max(0, 1 − floor ÷ price)        ← per-child stacking cap
Removal ROI/unit    = LTSF until sold − removal fee
Months to clear     = aged units ÷ monthly velocity
Weekly vel. to cliff= aged units ÷ weeks to next rate step
Age-forward charge  = Σ (units per bracket × next bracket's rate × cu ft)
Scenario recovery   = Σ months (units sold × net proceeds) − ad spend − LTSF at escalating rates − terminal salvage cost
```
- Highest forward net recovery wins, even if negative.
- Break-even discount **> 100%** → no depth pays for the storage → salvage comparison.
- **Floor ≥ price** → no discount authority; removal/salvage wins.
- Stacked promotions on one child never exceed its max combined depth.

### 14.4 Archetypes (classify first — misclassification is the costliest error) [LTSF]
| Archetype | Signals | Levers | Never |
|---|---|---|---|
| **A — Fixable demand** | Peers at the same price/rating sell far more; CTR/CVR below category; stock aged pre-launch | Listing repair (**48-hour SLA**); competitor keyword replication; break-even PPC after CVR recovers | Lead with a deep discount (40% off → 6 sales instead of 4) |
| **B — Variation overstock** | Parent healthy; specific colours/sizes hold the aged units | **Child-scoped only**: tailored promos, child coupons, targeting on non-preferred variations, virtual bundles | Parent price cut or family discount (scope violation) |
| **C — Structurally dead** | No organic traction for **6+ months** of genuine effort; return-defect signal; fixes already tested | Clear at floor now, or terminal | More experiments — decide within **7 days** |
| **D — Aged but healthy** | Sells, margin holds; batch aged via stock-out, season or overbuy | Velocity at/near break-even; PPC up on proven syntaxes; deals before the next bracket | Remove profitable units |
Parent B with C children → say so. C on a new launch = product-market-fit failure → strategic review (exit / redesign / reposition), not an LTSF problem. Before accepting "tested and failed", confirm the SKU ever had **dedicated** spend (5 SKUs were nearly liquidated on portfolio-wide evidence).

### 14.5 Risk tiers (first match, top down)
| Tier | Trigger | Cadence | Standing action |
|---|---|---|---|
| **CRITICAL** | Any units 366+ d, or product LTSF > **$5,000/month** | 2×/week | Removal, liquidation or deep discount within **48 h** |
| **RED** | Any units 271–365 d, **or** LTSF/unit > net proceeds/unit, **or months to clear > 6**, or velocity falling despite a boost | Weekly minimum | Execute, not plan; **freeze POs** on the SKU |
| **YELLOW** | Months to clear > 3 (units 181–270 d), or a large batch reaching 181 d within 60 days | Weekly | PPC velocity boost live; outlet deal submitted; break-even discount computed |
| **GREEN** | No aged units, or clears within 3 months | Weekly | Track; start velocity work if a batch nears 181 d |
Resolution note: the dossier text and its script differ. This framework uses the **union**: "months to clear > 6" is a RED trigger (script), and YELLOW starts at > 3 months (script) — the text's "2–6 months" lower bound overlapped GREEN. "Large batch" size: Owner decision — ask. [LTSF]
Escalations: product > $5k/month → executive review within 48 h. Portfolio > $25k/month two consecutive months → portfolio review + inbound freeze evaluation. Run-rate ÷ trailing-year charge > ~**1.5×** → the aged pool is forming faster than it clears → raise urgency. [LTSF]

### 14.6 Routing thresholds (precedence top down) [LTSF]
| # | Condition | Route |
|---|---|---|
| 1 | Units 366+ d and velocity < 2/month | REMOVAL — full stop |
| 2 | Units 271–365 d and velocity < 5/month | REMOVAL likely cheapest |
| 3 | Floor ≥ price | SALVAGE comparison — no discount authority |
| 4 | Break-even discount not computable | REVIEW — insufficient data |
| 5 | Break-even discount > 100% | SALVAGE comparison — no depth pays |
| 6 | Break-even discount > 40% | SALVAGE comparison — deep discount vs removal vs liquidation, cheapest total path |
| 7 | Break-even discount 20–40% | OUTLET deal at the computed depth |
| 8 | Break-even discount < 20% | COUPON / price drop at the computed depth |
Also: net margin after LTSF > 0 → keep selling, velocity focus; < 0 → floor discount or terminal **this week**. 100+ units at 456+ d → urgent removal/liquidation. Outlet unaccepted near the cliff → act now. Terminal calls belong to Brand Management + Supply Chain: present the comparison and a recommendation, never "settled" unless the Step-0 charge reconciliation passed.

### 14.7 Clearable vs structural split [LTSF]
- **Clearable** = best-case velocity (routing + max in-cap depth, basis-tagged) × weeks to the relevant cliff (monthly velocity ÷ 4.33 × weeks).
- **Structural** = max(aged − clearable, 0).
- Clearable → ladder (§14.10). Structural → salvage comparison **now** (paying bracket rates on units no realistic velocity can clear is waste).
- Removed structural stock on a continuing product → store for re-send or other channels; **never dispose of sellable stock** unless the side-by-side shows both alternatives net worse. Re-split every cycle.

### 14.8 Lever families [LTSF]
1. **Listing repair** — image, A+, title/bullets, offer, reviews, Vine.
2. **PPC velocity** — break-even scaling, competitor keyword replication, discovery routed to the aged child, targeting on non-preferred variations, bid/budget up on proven syntaxes, display retargeting, Sponsored Brands → store clearance page.
3. **Price / promotion** — coupons, Prime-exclusive, price drop, outlet, lightning/7-day deals, tailored promotions, social codes, virtual bundles, BOGO, Subscribe & Save, creator connections.
4. **Cross-channel** — TikTok Shop, DTC, FBM via 3PL, marketplace transfer.
5. **Terminal** — removal, liquidation, donation, disposal.
A single-family plan is incomplete. On variation overstock, price levers are scoped to the aged children only; a parent-wide lever is a scope violation, reported even if it worked.

### 14.9 Prediction rule [LTSF]
Every lever launches with a predicted uplift and a basis tag: **HIST** (measured response of this SKU or a close sibling to the same lever), **MARKET** (competitor-benchmarked ceiling), **TEST** (pre-registered). Read at **day 7** (and day 14). Actual **< 50% of prediction → replace, not extend** (verdicts: continue / replace / pending). Untagged uplift = blank and blocks scenario ranking. Two levers in the same window = confounded read.

### 14.10 Escalation ladder [LTSF]
Each aged SKU gets rungs with a velocity target and an expiry date anchored to its cliff calendar; a missed target fires the next rung automatically.
| Rung | Action | Target |
|---|---|---|
| 1 | Routing + shallow child-scoped depth; outlet deals submitted | 60% of velocity-to-cliff |
| 2 | Break-even PPC scaling; bundles / hero-as-X promotions | 100% of velocity-to-cliff during promo weeks |
| 3 | Off-anchor codes at clearance depth | Sustained 100% of velocity-to-cliff |
| 4 | Child base-price cut toward the floor, with a written restoration step | 80%+ of clearable units gone |
| 5 | Terminal execution on the remainder per salvage comparison | Zero positive-ROI cliff crossings |
**Skip-forward:** a SKU within **30 days** of its next rate step skips forward regardless of sequence. Depth is bought by the calendar, not by impatience.

### 14.11 Step-0 checks [LTSF]
1. **Charge reconciliation** — rebuild units × cu ft × rate per bracket vs the invoice; should agree within a fraction of a percent. A miss is almost always a per-unit rate somewhere.
2. **Bracket granularity** — request all 8 brackets; a 4-bracket source makes charges approximate (state it).
3. **SKU coverage** — SKUs in the charge file vs SKUs analysed; unrouted units are a stated gap.
4. **Velocity basis** — every haircut/uplift documented (§12).
5. **Untagged multipliers** — treated as blank.
6. **Scope violations** — parent-wide levers on variation overstock reported as findings.
7. **Inbound** — production + transit vs cover and ceiling (§11).
8. **Deployment verification** — what actually went live, before grading any lever.
A failed check is a **finding, not a blocker**: report it prominently, show both scenarios, name the document that would settle it, and continue. Terminal calls stay unsettled until check 1 passes.

### 14.12 PPC on aged stock [SR, B6, PB]
- Clearance/LTSF campaigns are judged on **stock cleared**, not ACoS. [B6 R-N2]
- SKU Green + aged units → PPC up to break-even on forward-cash economics (03 §3.7). Not Green → no push; move to price levers. Never a clearance push while the size's hero is Red. [SR]
- Negative contribution after LTSF → pricing decision (Brand Management), not a bid lever. [SR]
- Exit the clearance posture when aged stock drops below the next surcharge threshold. [SR]
- Deals are the clearance mechanism; PPC supports visibility of an already-scheduled clearance window. [PB]

---

## 15. Anti-patterns [LTSF, INV, WB, B6]

- LTSF per unit; flat-rate projections; no charge reconciliation.
- COGS in a clearance decision; floor set at break-even; deeper discount when break-even discount > 100% or floor ≥ price.
- Discounting Archetype A; parent-wide levers on B; stacking past the child cap; single-family plans; experimenting on C beyond 7 days; removing D stock; disposing sellable stock.
- Uncorrected distorted-window velocity; untagged multipliers; confounded reads; read windows straddling lever changes; grading undeployed actions; condemning SKUs that never had dedicated spend.
- Traffic into Conversion-quadrant syntaxes; stock signature read as relevance loss.
- Auto-derived backup pairs; ignoring backup self-competition; ignoring inbound.
- Cover computed on push pace; switches that change size; ranking on a slow colour; discovery on the hero; routing read from names.
- Pushing Yellow/Red stock; a hold with no re-entry date; zoning from "units > 0".

---

## 16. Open questions for the owner

1. **Velocity driver:** Resolved — see 13 #49: gate on the 30-day actual pace (deal/stock-out windows corrected and labelled), planned velocity shown beside it.
2. **TIGHT vs Red re-point:** the register makes any stock-out before arrival Red (re-point same day), while B6's TIGHT rule (shortfall ≤ 7 days) eases without swapping. This file treats TIGHT as Red with the swap waived. Confirm.
3. **Projected-cover threshold for a push:** Resolved — see 13 #42: projected cover must stay Green (≥ 60 days) through the push checkpoint, or the push is blocked, shrunk or time-boxed.
4. **Cover ceiling** (overstock) for the inbound check, and **"large batch"** size for LTSF YELLOW — no house values.


---

<!-- FILE: references/05-keyword-research.md -->
# FILE: references/05-keyword-research.md

# 05 — Keyword research, classification and keyword decisions

Phase 4 of the framework. Output: **every term with class, relevance, demand, position, owner and one decision**, each with its trail (input → metric → rule → decision → action → expected outcome → validation date). Campaign-level decisions are in `06-campaign-ppc-decisions.md`; placement pricing in `07-placement-and-bidding.md`; competitor keyword landscape in `08-competitor-market.md`; quadrant diagnosis and listing work in `09-listing-positioning.md`.

## Contents
1. Build the keyword universe
2. Normalise (resolved)
3. Classify every term
4. Demand tiers and hero / halo roles
5. Syntax and roots
6. Relevancy — scoring against the live listing, cut-offs
7. Indexing and rank
8. SQP roll-up, derived metrics, target CTR / CVR
9. Ownership — one live exact owner per term
10. The keyword decision order (16 steps)
11. Wasted spend and negation
12. Harvesting
13. Discovery candidacy and pricing
14. Phasing and launch selection
15. Gap keywords
16. Per-keyword output columns
17. Anti-patterns
18. Open questions for the owner

---

## 1. Build the keyword universe

**Universe = MKL ∪ SQP ∪ search-term report (STR) ∪ bulk targets (live and paused) ∪ competitor keywords ∪ Cerebro / Data Dive pulls.** One row per normalised term (§2). Record on each row which sources it came from — a term only in the STR is a discovery find; a term only in competitor pulls is a gap candidate.

| Source | Contributes | Rules |
|---|---|---|
| MKL | SV, relevancy (`Relevancy`, fallback `Derived Relevancy`; label `Categorization`), organic rank, syntax, indexed flag, PPC-targeted flags per match type | > ~30 days old = stale (finding). Syntax verified against the account taxonomy. Indexed field unvalidated → ask when it would move money. [E, PB] |
| SQP | Market and brand funnel per query, market price, query volume | Roll-up §8; 13-week window. [SQP, B6] |
| STR | Shopper terms (`Customer Search Term`) with spend/clicks/orders/sales per campaign × match type; bid keyword = `Targeting` | Filter to the exact `Portfolio name` string first, then aggregate. Bucket from `Targeting`: close-match / loose-match / substitutes / complements → Auto; `asin="…"` → product target; `category="…"` → category; else match type. Read 30 and 90 days. [STR, B6] |
| Bulk (all states) | Every exact / phrase / broad target, live or paused, and its advertised SKU | Ownership §9. Live = keyword AND campaign enabled. [PB, LP] |
| Target ranks | Rank target per term (presence = ranking flag); gap = organic − target | [STR] |
| Rank crawl (Data Rova, Data Dive gap-fill) | Organic and sponsored rank per day | §7. [SR, B6] |
| ASIN Insights / Data Rova | DSTR, organic vs ad traffic | Never invented; blank = unsized. [E, PF] |
| Competitor pulls (ASINsight / AdInsight / Data Dive / Cerebro multi-ASIN) | Rival ranks, traffic, ad types, contested terms | Brand-resolved, dated, coverage stated (`08`). Implausible or identical odd SV across files → verify, exclude from totals. [LP, B6] |
| Cerebro (own ASIN) | Extra terms, SV, own rank | Suggested-bid column = context only, never a price (owner rule). [E, #18] |

Join rules: key = `strip().lower()` of the term (display the original casing); no match → **blank, never 0**; safe division everywhere (`a/b if b else blank`). [E]

Example (B6): 841 search terms with spend in 30 or 90 days; 2,266 market keywords pulled from ASINsight (all addressable ones).

---

## 2. Normalise (resolved — conflict #14)

1. Lowercase, collapse spaces, strip symbols (`[^a-z0-9 ]`, incl. `%`, `+`, `™®©`). Keyword text written to a bulk must contain no symbols. [CB]
2. **Word order is preserved.** "queen bamboo sheets" ≠ "bamboo sheets queen". Word-order variants are separate terms with separate history — never duplicates. [PH, PB, #14]
3. **Singular ↔ plural and symbol variants merge** into one identity (close variants: "sheet"/"sheets", "100% bamboo"/"100 bamboo"). Keep the higher-SV form as the display/deploy form; aggregate SV. Singularise tokens of length > 3: `-ies → y`; `-ses / -xes / -zes / -ches / -shes` drop `es`; `-ss` unchanged; else drop trailing `s`. [PH, KCP, SR, B6]
4. **Sorted-token form** (tokens sorted, stop-words dropped: the, a, an, for, of, to, and, in, my, with, on, your, this, that, is, are, best, s, size) is allowed **only for grouping reports**. Never for ownership, duplicates or deployment. [KCP, #14]

Why: Amazon treats word order as a different query; plurals are served as close variants by Exact.

---

## 3. Classify every term

Run the classifier on the term text, first match wins, in this order. Classes drive objective eligibility, the decision order and variation routing.

| # | Class | Detect | Why it matters | Exact objective | Hard constraints |
|---|---|---|---|---|---|
| 1 | **ASIN** | `^b0[a-z0-9]{8}$` (lowercased) | Product-page intent | — (product-targeting loop) | Classify the ASIN's owner first: own / own other product / mapped competitor / unmapped (`08`). [E, B6 R-X] |
| 2 | **Brand (own)** + misspellings | Substring of brand name or any listed misspelling (keep the list, e.g. `decolure, decoloure, decloure, decolore`) | Cheapest, most profitable orders | Defensive | **Never blocked or negated.** A misspelling missing from the list gets flagged for negation (known failure). [E, B6 R-K8, OC] |
| 3 | **Competitor brand** | Mapped competitor brand list (`08`) | No organic rank on another brand; trademark risk | Profitable Conversion | Never Ranking. Existing conquest exact = live tactic; else evaluate-only. [B6 R-O1, LP] |
| 4 | **Other product type** | Category off-topic list (§6.1) or wrong material ("silk sheets" for bamboo) | Spend with no demand fit | — | Blocked on relevance (§11); never launched. [LP, B6 R-K2] |
| 5 | **Language / misspelling** | Non-English tokens ("sábanas"); misspelled generics | Usually uncontested; listing score ≈ 0 = no on-page copy, not irrelevance | Profitable Conversion | Never Ranking. [B6 R-O1, LP] |
| 6 | **Colour** | Product colour list | Shopper asked for a colour | Profitable Conversion | Advertise the named colour in the term's size. [B6 R-C3] |
| 7 | **Size** (+ core) | Size tokens (§5) | Shopper searched a size | Ranking allowed | Route only to that size; a switch never changes size. [PH, B6 R-C4] |
| 8 | **Attribute** (+ core) | cooling, deep pocket, organic, 6-piece… | Tests our differentiation | Ranking if the attribute is in the listing | Routes only to a matching SKU; OOS → hold at bid floor, no substitute. [PB, LP] |
| 9 | **Core** (niche generic) | Root material / form wording ("bamboo sheets") | Where organic rank is built | **Ranking** | Push only via push rules (`06`). [B6 R-O1] |
| 10 | **Generic head / adjacent** | Category words without the niche root ("bed sheets") | Field priced for another product; CVR can't carry our price | Profitable Conversion | **Never pushed, whatever volume**; guard §10 step 10. [B6 R-CI1] |

- The class decides whether an Exact campaign may carry the Ranking objective: a Ranking tag on a colour / competitor / language / misspelling / adjacent-generic term is blocked (→ Profitable Conversion). Campaign objective itself is decided from targeting at campaign level (`06`). [B6 E18, OC, #15]
- Classify against the MKL label too; labels can be wrong (Example (B6): "red bamboo sheets" labelled Not Relevant while converting at 33.6% ACoS). Where classifier and label disagree, show both and use the relevancy score (§6). [B6]

Example (B6): 429 core, 198 ASIN, 94 brand, 34 colour, 33 other product type, 28 adjacent generic, 18 competitor brand, 7 Spanish/misspelling.

---

## 4. Demand tiers and hero / halo roles

| Tier | Monthly SV | Keywords per campaign | Role |
|---|---|---|---|
| VHSV | ≥ 10,000 | 1 (isolated) | Hero |
| HSV | 1,000–9,999 | 1 (isolated) | Hero |
| MSV | 500–999 | 3 (halo stack) | Halo |
| LSV | 100–499 | 10 (halo cluster) | Halo |
| VLSV | < 100 | 10 (halo cluster) | Halo |

[PH v5, authoritative]

- **Hero** = VHSV / HSV, **or** has a rank target, **or** top term of its syntax (rank targets promote to Hero within each syntax). Everything else = Halo. [PH]
- Other SV gates used elsewhere: launch SV floor **~250** (confirm per product); Cold ranking candidate needs **SV > 500**; full per-row analysis at **SV ≥ 250 or top spend decile** (tail gets the same rules + exception alerts); human confirmation for decisions on **SV 500+**. [PB]
- **SV% = term SV ÷ Σ SV** of the universe; ΣSV% must equal 1.0. [MDB]
- Record the SV source: MKL (monthly, Helium 10/SQP) and ASINsight (weekly) do not reconcile — never mix them in one column. [B6]
- Concentration: one term > ~25% of product clicks, or top 5 > ~60% → needs a declared head-term push, else explained finding. [PB]

---

## 5. Syntax and roots

**Syntax** = the segment a term belongs to; it sets the diagnosis mode (quadrant, `09`), never a keyword's bid.

- Pipe form `Material|Size` (e.g. `Bamboo|King`, `Cooling|Queen`), plus labels `Generic`, `Generic_HSV`, `Generic_VLSV`, `Branded Keyword`, `Competitor Branded Keyword`, `ASIN Target`, `Irrelevant Fallback` (`*`). [PH, STR]
- Full taxonomy `Root | Product Form | Segment`; a 4th level only where a sibling needs disambiguating (e.g. `Cooling | Sheets | Queen | Core` because a `Color` sibling exists). Segment may be number + unit. [PB]
- **Precedence, first match wins: Branded → Competitor Branded → Irrelevant → Generic → Spanish/language → In-family.** No permanent Unclassified bucket; an unconfirmed near-miss mapping → ask. [PB]
- Material tokens per product (first = display material; e.g. bamboo line: bamboo, viscose, rayon). Size tokens, **longest first**: california king / cal king → California King; split king; twin xl; full xl; olympic queen; short queen; rv queen; queen; king; full; double; twin. **California King is checked before King in every regex and every classification stage** (a known defect matched KING inside CALKING). [PH, SR]
- Syntax logic for a product not already defined → ask; never invent. [MDB]

**Roots** (for root performance and drill-downs):
- A root = a phrase of **1–5 words, contiguous, word order preserved, appearing in ≥ 2 distinct search terms**. Root metrics = sum over every term containing it (roots over-count spend by design). Cap 250 child terms per root. [STR]
- Phasing drill-down: top 200 roots by total SV with ≥ 2 keywords and ≥ 1,000 SV; cap 50 keywords per root. [PH]
- Root status (STR engine; target = the product's break-even ACoS): orders ≥ 1 & ACoS < BE → Healthy/Scalable (scale, harvest best children to exact); orders ≥ 1 & ACoS ≥ BE → Needs Optimisation (reduce broad/auto spend in the root, promote best children); 0 orders & clicks ≥ 5 → Wasted (find and negate the driving children per §11); 0 orders & clicks < 5 → Low Data. [STR]

---

## 6. Relevancy — scoring against the live listing, cut-offs

**Resolution #30: the listing scorer gives the %, the STR cut-offs give the action.**

### 6.1 Listing scorer (second opinion; never overwrite the original)
Keep original `Relevancy` / `Derived Relevancy`; add `Updated Relevancy %`, `Updated Relevancy Source`, `Updated Relevancy Confidence`, and a methodology note. [LP]

Reference text = live title + all bullets; lowercase; strip ™®©–; keep a-z, 0-9, space, hyphen; drop "w/". Build: `words` = non-stopword tokens of length > 2; 2-, 3-, 4-gram sets (stop-words kept, so "for hot sleepers" survives); `full` = whole cleaned string. Stop-words (unigrams only): a an the and or with our your for to in on of is are that this will you from all every without w upgrade now discover indulge experience ensure ensures ensuring these those staying wake up perfect pure elevate enjoy.

| # | Test (first match wins) | Score | Source | Confidence |
|---|---|---|---|---|
| 1 | Category column says Irrelevant / Competitor Branded / = Branded Keyword (skip if the column is empty for every row) | 0 | disqualifier_override:category | HIGH |
| 2 | Keyword of ≥ 3 words appears verbatim in `full` / 2-word keyword is a listing bigram | 92 / 85 | phrase_match_listing | HIGH |
| 3 | Contiguous overlap, longest first: 4-gram / 3-gram / 2-gram | 78 / 64 / 50 | fourgram / trigram / bigram:<words> | 4-gram HIGH; 3-gram HIGH if keyword ≤ 4 words else MEDIUM; 2-gram MEDIUM if ≤ 3 words else LOW |
| 4 | Off-topic term or pillow regex | 0 | disqualifier_override:offtopic_term | HIGH |
| 5 | Theme trigger (longest trigger first) | 36 | theme_match:<theme> | MEDIUM if ≤ 3 words else LOW |
| 6 | Any non-stopword token overlap | round(15 + 15 × overlap ÷ keyword length) → 15–30 | unigram_partial | LOW |
| 7 | Nothing | 0 | no_match_in_listing | HIGH |

[LP relevancy_scorer]

- **Off-topic list** (swap per category). Sheets: chair, comforter, mattress protector, mattress topper, curtain, rug, decor, kitchen, "mat ", duvet, "blanket only", towel, cooler. **Pillow regex** `\bpillows?\b(?!\s*-?\s*cases?)(?!case)` — kills "cooling pillow", keeps "pillowcase", "pillow case", "pillow-top". Hand-check a sample of pillow terms after every run. [LP]
- **Themes** (use a theme only if its concept is actually in the listing; swap per category): cooling_comfort, hot_sleepers_sweat, moisture_breathable, material (bamboo/viscose/microfiber — swap for the real fabric), deep_pocket_fit (incl. the listing's depth figure, e.g. 17"), easy_care_durable, soft_luxury, sleep_quality, sheet_set_core. [LP]
- **Caveats — state them in the methodology note:** will disagree with the original columns (different vocabulary); non-English ≈ 0 = no on-page copy, not irrelevance; the reference variant's size/colour words give a slight edge to terms naming them; bullets contradicting the title variant (King title, "Queen" bullets) = listing defect → flag to `09`, score the literal text; own brand terms score 0 via the category override — brand decisions come from class (§3), never from this score. [LP]

### 6.2 Decision cut-offs (STR)
| Tier | Rule | Use |
|---|---|---|
| **High** | ≥ 60% or label "Highly Relevant" | Never negated on relevance; zero-order → fix queue / REDUCE |
| **Moderate** | 35–60% | Negative exact at ≥ 5 clicks, 0 orders, if not a rank target |
| **Not relevant** | < 35% or label "Not Relevant", or no relevancy signal | Negative exact at ≥ 5 clicks, 0 orders |

[STR]

### 6.3 Launch relevancy tiers (for §14)
- **Highly relevant** — has every defining attribute of the product; launches first and fully.
- **Semi-relevant** — missing a sibling-disambiguating feature, or a secondary synonym (e.g. "blanket" on a comforter).
- **Not relevant** — wrong category or material, competitor brand → never Exact; own brand → Defensive.
- **Unclassified** → re-score before any decision. [PB]

---

## 7. Indexing and rank

- **Indexing gate (before any spend):** not indexed → no spend, open an indexing/listing task. A ranking term present only in backend search terms → listing task before funding. [PB]
- Indexing proxy when no indexing check exists: crawl rank present = ranking; a rank-targeted term with no crawl rank → "Not ranking — check indexing"; blocks a push until fixed. [B6]
- **Organic rank** = median over the window, unranked days counted; **NR if half or more of the days are unranked**. 0 / blank in Data Rova = not ranked (store as 101). Match terms exact lowercase/trim only — no fuzzy or reordered matching; untracked → "not tracked". [B6, SR]
- Name the rank source on every row: two rank tables can disagree by ~7 places (Example (B6)). Ranking verdicts need **≥ 1 month** of rank history (ideally 3); less → out of scope for a ranking verdict. [B6, PB]
- Rank arc: state overall, 14-day and 7-day separately; exclude stock-out and re-route stretches; deal-state arc kept separate — the clean arc governs. Rank drop > 10 places in 30 days while getting clicks → freeze price moves, find the cause (`09` §5, `06` §6.3). [PB, B6 E4]
- Organic rank with no paid support on a relevant term = cheapest coverage (route aged SKUs there). Backend terms close coverage gaps first, free. [LTSF]

---

## 8. SQP roll-up, derived metrics, target CTR / CVR

### 8.1 Parent roll-up (child-ASIN export → one row per query)
- **Market columns (`… Total Count`) are identical on every child row → take once (max per query). Brand columns (`… ASIN Count`) → sum across children.** Summing market columns multiplies by the number of children and destroys every share. [SQP]
- Ignore SQP's precomputed rates; recompute:
  - Impression / Click / Cart-add / Purchase **share** = Brand ÷ Market at that funnel stage.
  - **Market CTR** = market clicks ÷ market impressions; **Brand CTR** = brand clicks ÷ brand impressions.
  - **Market CVR** = market purchases ÷ market clicks; **Brand CVR** = brand purchases ÷ brand clicks.
  - CTR / CVR variance = brand − market (percentage points).
  - Market price = `Purchases: Price (Median)` (fallback clicks median), take once; brand price = median of children's `Purchases: ASIN Price (Median)`; revenue = purchases × price; revenue per click = revenue ÷ clicks. Query volume take once. [SQP]
- Verify: rows = unique queries; market impressions = raw Total Count; brand ≤ market; shares 0–100%. Percent strings ("52%") → 0.52. [SQP]
- Impression-share proxy where no IS report exists: SQP brand impressions ÷ market impressions (label it a proxy). [E]

### 8.2 Targets and flags (resolution #20)
| Level | Target CTR | Target CVR | Fails when |
|---|---|---|---|
| Syntax (quadrant) | Market CTR × 1.10 | Market CVR × 1.10 | below 0.9 × target |
| Keyword | Market CTR × 1.10 | **Market CVR × 3.0** | below 0.9 × target |

- No SQP match → keyword targets **blank** (never guessed). Syntax level with no SQP → portfolio medians, labelled **provisional** (medians are relative: half fail by construction). [SQP, QA, #20]
- Targets supplied in a sheet are re-derived: > 2% drift on > 10% of rows → halt that input. [SR]
- **Listing flag:** our CTR or CVR below market (ratio < 1.0) on **≥ 30 clicks** → no push until the listing is checked (`09`). [B6 E15]

---

## 9. Ownership — one live exact owner per term

Build an **owner map on normalised terms (§2; close variants count)** across every exact target in the bulk, live and paused, and across sibling products' bulks for shared head terms (missing sibling bulk = named gap). [B6 R-S1, PB]

| Owner state | Meaning | Decision |
|---|---|---|
| One live exact owner | keyword AND campaign enabled, correct variation | OK; judge the term through §10 |
| > 1 live exact owner | same normalised term, same match type, ≥ 2 campaigns | Coexistence test, else **DEDUPLICATE** |
| Only paused exact owner(s) | exists but not serving | **CHECK OWNER**: restart the paused keyword (at break-even, after any deal window) if the term is wanted; never build a duplicate; no price change on a paused row |
| No exact owner | only discovery / phrase / broad / auto serve it | Candidate for HARVEST, launch or discovery rules |
| Exact owner exists and discovery campaigns also serve it | two prices on one term | Negative exact in the discovery lanes (isolation wall, §11.3) — brand terms only after the brand-negative gate |

[B6 R-S1, R-S2, R-K7, E6, E11]

**Coexistence test first** — both instances stand if one of these holds: [PB, #13]
1. **Stage-stack** — the instances deliberately serve different lifecycle stages of the plan.
2. **Placement-split** — the instances are deliberately split by placement.
3. **Variation-split** — each instance advertises a different variation (e.g. colour-named routing; "different SKU targeting" is not a duplicate). [KCP]
4. **Sibling ownership** — the other instance belongs to a sibling product under the family owner assignment (family owner score = margin/order × sibling CVR on the shared root × sibling inventory days; exact tie → human).

**Duplicate owner rule (resolution #13):** owner = **higher CVR at lower CPC with ≥ 15 clicks each**; below that, **most orders**; tie → **longer clean history**. The owner must advertise the right variation (ranking → the size's best seller; colour term → the named colour); if not, re-point it rather than pick another instance. Losers are **withheld (paused), nothing else changed** — no bid on a withheld row. [PB, B6, #13]

- Different match types on one term are purposeful, not duplicates; word-order variants are not duplicates. [SR, PB]
- Status rule: an instance is **Paused if keyword state OR campaign state is paused** (ad-group state is reported separately, not used for the duplicate status). A keeper sitting in a paused campaign won't serve — count and state these. [LP]
- Validate: no group with > 1 enabled instance; no duplicate group with 0 enabled instances; singletons untouched (report dormant count; ask before enabling). [LP]
- Several issues on one term → fix in this order: negate the variant in discovery → turn off same-SKU duplicate exact → turn off variant covered by a higher-SV form → review same-SKU normalised duplicates; different SKU = no action. [KCP]

Example (B6): 8 terms DEDUPLICATE ($748 / 90 days), 23 terms CHECK OWNER ($2,274 / 90 days); "bamboo queen sheet set" was bought by 4 live exact campaigns.

---

## 10. The keyword decision order (16 steps)

Applies to every search term (and every untargeted universe term through steps 1–6, 10, 15–16). **The first step that fires ends the row; record the step.** Preconditions from the master order run first: data validity (quarantine), goal and deal state (no verdict on deal-day data; no builds on deal days — negatives and reductions may load, harvests and new exacts wait for the post-deal audit), indexing (§7), live state. Windows: clicks/orders/ACoS on **90 days** unless stated; REDUCE reads **30 and 90**.

| # | Step | Fires when | Decision → action | Rule |
|---|---|---|---|---|
| 1 | **ASIN** | Term matches `^b0[a-z0-9]{8}$` | Judged with product targeting (own → DEFEND / cross-sell; competitor → OFFENSIVE / TEST / AVOID, SCALE / REDUCE / BLOCK) in `08` | [B6 R-X, E] |
| 2 | **Brand** | Own brand or misspelling | **DEFEND**: owned by brand exact campaign(s) on the hero variation, enough budget, judged on ACoS ≤ break-even. Never blocked. Brand negatives in generic discovery only after the brand exacts are defensive, on the hero and funded | [B6 R-K8, R-N3, R-S4] |
| 3 | **Funded push** | Term qualifies on every push gate and is funded within the spend limit | **PUSH** — price, base, boost and budget per the push plan (`06`, `07`) | [B6 R-K1, R-P1] |
| 4 | **Push candidate held** | Rank-targeted core term failing a push gate: listing flag (SQP CTR or CVR < market on ≥ 30 clicks), ceiling < our TOS CPC, hero stock not Green (< 60 days, stock-out before the next inbound, cover < days to next arrival + 7, or projected cover leaving Green before the checkpoint), keyword not live, not indexed | **WAIT** — name the failing gate; runs at break-even meanwhile; ceiling-below-cost needs an owner decision on a time-limited ceiling raise | [B6 R-P1, E14, E15, F25, F26, #9, #42, #50] |
| 5 | **At target** | Rank-targeted, organic rank ≤ target | **HOLD RANK** — keep today's price, no raise; rejoins the push if it slips past target; taper only after 2 clean weeks at target (`06`) | [B6 R-P8, #26] |
| 6 | **Too far** | Rank-targeted, current rank more than **~30 places** from target | **MONITOR (too far)** — discovery / break-even only; revisit when within ~30 places | [B6 R-P1 reach] |
| 7 | **Irrelevant / other product type** | Other product type, Not relevant (< 35% / "Not Relevant") or no relevancy signal, **≥ 5 clicks, 0 orders**; or moderate (35–60%) ≥ 5 clicks, 0 orders, not a rank target; or structurally off-target (competitor brand without a conquest owner, foreign ASIN, other category) | **BLOCK** — negative exact (or phrase, §11.1) in every discovery campaign that serves it. > 10 clicks & 0 orders listed first | [STR, PB, B6 R-K2, #12, #21] |
| 8 | **Zero-order, relevant** | High relevancy, **≥ 20 clicks, 0 orders** | Live exact owner → **REDUCE**: cut to the break-even floor or pause the exact keyword; review relevance and listing (fix queue). No exact owner → **REVIEW** (fix queue: price / listing / placement; not negated). Never negate an exact ranking term or a brand term | [B6 R-K2, STR, PB, #12] |
| 9 | **> 2 × break-even** | ACoS > 2 × break-even ACoS on **≥ 30 clicks**, not a rank target | **BLOCK** in discovery; **REDUCE** in its exact owner (bid to break-even). Guard: a term still selling (≥ 10 orders / 90 d) that rivals buy is REDUCE, never BLOCK; a BLOCK on an addressable term with ≥ 10,000 market traffic and ≥ 5 rivals advertising stands but is tagged "re-test" (back in discovery at break-even after 30 days or a listing/price change) | [B6 R-K3, R-CI9] |
| 10 | **Head-generic guard** | Generic head / adjacent generic class with **SV ≥ 50,000/month**, outside the niche | **MONITOR** — leave in discovery at break-even; never harvested to exact, never pushed, whatever the orders; re-check at 10+ orders | [B6, R-CI1] |
| 11 | **Harvest** | No exact owner (live or paused); **≥ 3 orders at ACoS ≤ break-even**; not other product type; relevant | **HARVEST** — exact campaign at break-even (post-deal), right variation; negative exact in the source in the same upload (§12) | [B6 R-K4, PB, STR, #22] |
| 12 | **Paused owner** | Exact owner exists but every instance is paused | **CHECK OWNER** — restart the paused keyword at break-even if the term is wanted; never build a duplicate | [B6 R-K7, R-S2, E6] |
| 13 | **Duplicate owners** | > 1 live exact owner, no coexistence reason | **DEDUPLICATE** — keep the owner per §9, pause the rest | [B6 R-K7, R-S1, PB, #13] |
| 14 | **Over break-even** | Live exact owner; ACoS > break-even on **both 30 and 90 days**; **≥ 15 clicks (30 d)** | **REDUCE** — bid toward break-even, ≤ 30% a step. 30-day over but 90-day inside → MONITOR ("watch") | [B6 R-K5, R-N1, #16] |
| 15 | **Thin** | < 15 clicks (90 d) | **MONITOR** — no change until 15 clicks; say whether low clicks fit low SV or mean the term is uncompetitive | [B6 R-K6, DR] |
| 16 | **Everything else** | None of the above | **MAINTAIN** — no change, within limits. Rank-targeted term within reach but not in the push → MAINTAIN (ranking, break-even): runs at break-even, enters the push when it qualifies | [B6 R-B3] |

Rules that bind the order:
- **Brand and push terms are never blocked. No exact ranking term is negated.** (quality gate) [B6, #12]
- Converting rows skip the thin-data gate: a term with orders is never parked for "< 15 clicks" (harvest at 3 orders on 9 clicks is valid). [PB, DR]
- Deal days: zero-order and > 2 × BE decisions may still load as negatives / reductions (bleed stops run during deals); harvests, restarts and new exacts wait for the post-deal audit. [B6, #27]
- One term, one direction: after deciding, reconcile across campaigns — no term cut in one campaign and raised in another. [DR]
- Push qualification (steps 3–4) uses the push gates in `06` (plan, TOS CVR above market, reach ~30 places, hero stock, live, ceiling ≥ TOS CPC, listing not flagged). [B6 R-P1]

Example (B6, 841 terms): MONITOR 430 · ASIN → competitor tab 198 · DEFEND 94 · MAINTAIN 38 · CHECK OWNER 23 · REDUCE 22 · PUSH 13 · DEDUPLICATE 8 · WAIT 4 · MONITOR (too far) 4 · BLOCK 3 · MAINTAIN (ranking, break-even) 2 · HOLD RANK 1 · HARVEST 1. "bed sheets" (3 orders on 6 clicks, 56,136 SV) → MONITOR by the head-generic guard: an exact at break-even would buy mostly non-niche shoppers. "cooling bed sheets" rank 70 vs target 10 → MONITOR (too far).

---

## 11. Wasted spend and negation

### 11.1 Wasted-spend list (read first every cycle)
- Include **every** term with clicks ≥ 1 and 0 orders; sort by clicks descending. **> 10 clicks & 0 orders → row RED** (top priority). Children = campaign × match-type slices; **exact-match child rows YELLOW** — always manual review before negating. [STR]
- **WAS% = spend on rows with 0 sales ÷ spend.** Ceiling **10% per campaign, 40% for discovery**; over the ceiling → negation pass. Product-level waste reported. Real ACoS = spend-with-sales ÷ sales. [SR, QA, #24]

### 11.2 Negation tree (relevance decides, clicks decide urgency — first match wins)
| # | Condition | Action |
|---|---|---|
| 1 | Brand term (own, incl. misspellings) | **Do not negate** |
| 2 | ASIN target (≥ 5 clicks context) | Negative exact (ASIN negative target) — unless it is our own ASIN under a stated defensive decision (`08`) |
| 3 | `*` auto catch-all | Negative exact |
| 4 | clicks < 5 | Manual review; monitor to 5+ clicks |
| 5 | High relevancy AND rank target | Manual review: cut bid / fix listing — **do not negate** |
| 6 | High relevancy core term, no rank target | Manual review: fix price / listing / placement, reduce bid |
| 7 | Not relevant (< 35%) or no relevancy signal | **Negative exact**; **negative phrase** if broad+auto occurrences ≥ 2 AND term ≥ 3 words |
| 8 | Moderate (35–60%), ≥ 5 clicks, not a rank target | **Negative exact** |

[STR, #21] Every negation reason cites that occurrence's clicks, spend, orders, relevancy and rank — no root-wide sweeps on non-structural terms. [PB]

### 11.3 Negation modes (name the mode on every negative)
| Mode | When | What |
|---|---|---|
| **Pre-load** | At launch, from the taxonomy + an own-catalogue scan | Other product types, off-topic words, competitor brands not under conquest, own-catalogue terms belonging to sibling products |
| **Reactive** | From the STR each cycle | §11.2 tree |
| **Steering** | When a term gets an exact owner (harvest, launch, decided ranking term) | The owned exact goes in as negative exact in the discovery lanes that also serve it |
| **Isolation wall** | Every owned exact | Owned exact as **negative exact in the lane's broad / phrase + auto / catch-all campaigns, in the same upload** as the exact build | 

[PB, WB]

- Negatives live only in Profitable Conversion, Discovery and Conquest campaigns; Ranking, Market Share and Defensive campaigns carry none; **exact targets are protected**. Placement: campaign-level negative exact / negative product target; target-level pause for a single-ASIN PAT. [SR]
- A decided ranking term with no live exact → same-day exact build + steering negatives in broad/auto (not a harvest case). [PB]
- **Brand-negative gate:** no brand negatives in generic discovery until the receiving brand exacts are defensive, on the hero variation and funded. [B6 R-S4, E10]
- Relevant non-converters go to the **fix queue**, never the negative list. [PB, SR]
- Auto own-ASIN matches: negated unless a stated defensive decision exists (`08`). [WB, DR]

Example (B6): only 3 terms met BLOCK ($105 / 90 d) — "silk sheets" (other product type, 14 clicks, 0 orders), "full xl bamboo sheets" (Not Relevant, 10 clicks), "cooling sheets twin" (25 clicks, 0 orders, owner paused — labelled Relevant, so under #38 it is REVIEW, not BLOCK).

---

## 12. Harvesting

**Rule (resolution #22):** search term with **≥ 3 orders and ACoS ≤ break-even**, relevant, not other product type, and **no live exact owner** → build an exact; **negate it at the source in the same deployment**. [PB, B6, STR]

1. Candidates: orders ≥ 1, discovered **outside exact** (auto, broad, phrase, product targets). Drop Not relevant / < 35%. Drop runaway rows: STR drops ACoS > 45% with < 3 orders (defined against its 30% default target — for another break-even: Owner decision — ask). Sort by SV desc, then spend. [STR]
2. Check ownership first: paused exact owner → CHECK OWNER (restart), never a new build. [B6 R-S2]
3. Head-generic guard (§10 step 10) overrides harvest. [B6]
4. Match type / campaign tier by ACoS (STR tiers, stated in the source against a 30% break-even; confirm the scaling for your product):

| ACoS (STR, BE 30%) | As share of BE | Suggested campaign | Match |
|---|---|---|---|
| ≤ 15% | ≤ 0.5 × BE | Hero — high-conviction exact, bid up | Exact |
| ≤ 20% | ≤ ~0.67 × BE | Standard exact | Exact |
| ≤ 30% | ≤ BE | Phrase first; promote to exact if it scales | Phrase |
| > 30% | > BE | Broad / phrase discovery; improve efficiency first (not a harvest) | Broad |
| none | — | Standard exact | Exact |

5. Objective: decided from targeting and term class per `06` §1 (resolutions #15, #36) — a harvested generic-niche exact is tagged Ranking and runs non-push at break-even until it qualifies for the push (goal gate applies); colour / competitor-brand / language / misspelling / adjacent-generic exacts → Profitable Conversion; Market Share **only if the owner declared it**. STR's ACoS-based objective suggestion (≤ 15% → PC; ACoS > 30% → Discovery; etc.) is reference only. Harvested exacts start at **break-even** on the right variation (colour-named → that colour; generic → size's best seller). [STR, B6 R-K4, #15]
6. Override: a decided ranking head carried by auto close-match graduates below 3 orders (say which case). [PB]
7. Auto terms are read split by close / loose / substitutes / complements; an untagged converting term is classified before harvest. [PB]
8. No harvest builds on deal days; queue for the post-deal audit. The harvest rule is the resolved default (#22); an owner override is recorded if given. [B6, PB, #22]

Example (B6): "king size sheets with corner straps" — no exact owner, 3 orders on 9 clicks at 3% ACoS → exact campaign at break-even on 1 Oct (an adjacent-generic term — no product-defining word — so its exact is tagged Profitable Conversion under #36/#55), then negative exact in the discovery source.

---

## 13. Discovery candidacy and pricing

- **Reactive path:** a term needs **≥ 100 qualified clicks on its own exact history** before a broad / phrase / SB / SBV layer is built. **Proactive path:** a syntax coverage gap (e.g. primary root at 0% phrase), judged on closing the gap. State which path. [PB, #23]
- < 100 clicks → ineligible, **no pricing**; near-miss = within ~20. Keyword vs root-cluster count basis → ask the owner. Singular/plural share one count; word-order variants don't. Check for an existing broad / phrase / auto instance before building. [PB]
- **Price below exact, no placement modifier at launch: Broad ~60%, Phrase ~80% of the exact ceiling** — here the exact term's **break-even** CPC, never the 2× push ceiling (#47); relevancy tier sets position (highly → upper end, semi → lower end). [PB, #47]
- Judge discovery from **15 clicks**, on converting terms per $100 and graduation into exact — not on CPA in its first 30 days. Four auto groups reported separately. Utilisation floor 70%+. [PB, DR]
- Discovery campaigns advertise the size's **clearance variation** (≥ 180 days cover, or ≥ 90 days while selling ≤ size median); ranking stock is reserved for exact. [B6 R-C2, #29]
- Alternative (PF, not default): build phrase/broad only when non-branded cost/order < exact average — record if the owner prefers it. [PF]
- Gap seeding (B6, proposed): addressable core terms with ≥ 3,000 market traffic and no search-term row get an exact target inside the discovery campaign of their size at break-even; no push premium; judged by §10 after 15 clicks. [B6 R-CI8]

---

## 14. Phasing and launch selection

### 14.1 Phases, statuses, groups
- **200-keyword cap per phase**, syntax-priority order, same-syntax overflow into the next phase. Sort: phase ↑ → syntax priority ↑ → Hero first → aggregated SV ↓. [PH]
- Status per keyword: **New Build** (no PPC activity) · **Already Running** (exactly one match type live — expand to the remaining types only if the discovery rule allows) · **Existing Campaign** (≥ 2 match types live — do not duplicate; marked "(existing — skip)"). Restart-before-build applies to paused owners. [PH, B6 R-S2]
- **Campaign Group ID** `{SLUG}-P{phase}-G{n}`, sequential per (phase, syntax, tier, preferred SKU, match type, status) block, tier-capped (1 / 1 / 3 / 10 / 10 keywords). **A group never mixes phase, syntax, tier, SKU, match type or status** (breaks STR attribution). [PH]

### 14.2 Match type and objective
- **Default SP Exact for every keyword, every phase, every tier.** Never broad/phrase by default. Single override: the MKL flags the term already running in another match type → surface that type; precedence SP Phrase → SP Broad → SB Exact → SB Phrase → SB Broad. [PH]
- Objective from targeting and class (`06` §1, #15, #36): generic-niche exact (core / attribute / size) → Ranking (push only when it qualifies; otherwise non-push at break-even); colour / competitor / language / misspelling / adjacent generic exact → Profitable Conversion, never Ranking; existing non-exact → per `06` §1 (Broad / Phrase → Discovery, #35). **Bidding strategy for every new campaign: dynamic bids – down only.** [PH, B6 R-O1, #8]
- Variation routing (colour-aware): term contains a colour and a matching colour SKU exists → that SKU; else the syntax's preferred SKU (ranking → the size's best seller; discovery → clearance variation); **size never changes**; routed SKU needs ≥ 21 days of cover to launch (not the 60-day push gate). [PH, PB, B6, #29]

### 14.3 Launch selection by goal and relevancy tier
| Declared goal | Exact launch set |
|---|---|
| Growth / Scale, Mixed | Highly relevant, then semi-relevant (semi only after its opening conditions) |
| Profit-First, Clearance / LTSF | **Highly relevant only, permanently** |
| Undeclared | Treated as Profit-First |

[PB]

- Order within the set: **tightest rank target first**; SV floor ~250 (confirm). Singular/plural = one identity; word-order variants stay separate. Attribute in the query routes only to a matching SKU; that SKU OOS → hold at bid floor, no substitute; a term failing routing eligibility is never built (not built-then-paused). [PB]
- **Semi-relevant opens only when all six clear:** (1) rank target reached or closing; (2) five-property gate cleared (sized, dated, ceilinged, predicted, funded — `06`); (3) TACoS within the owner's band, only if the owner set one (otherwise monitored only, #17); (4) margin holding; (5) spend ≈ plan; (6) minimum data window met. If 2–3 cycles of real lever fixes still fail, semi opens anyway with the reason stated. [PB]
- **Launch price = break-even maths, not Amazon's suggested range** (owner rule): base and TOS modifier solved from the routed SKU's break-even CPC per placement (`07`). The source's placement shape is kept: Growth / Mixed / Profit-First start with a TOS modifier (source: +100%), Clearance with none. [PB, #18, #33]
- Expected spend per keyword (phasing) = (DSTR − our organic sales on the term, labelled proxy; 0 for a new build) × CPC ÷ CVR, with CPC = the routed SKU's break-even CPC and CVR = own achieved CVR (0.20 only as the phasing default when no own rate exists — label it). Never DSTR ÷ CVR without organic netting (WB D-78). [PH, #18, #19]
- No launches, folds or structural builds on deal days. Human confirmation: SV 500+, gate failures, structural change, bid moves > 25% outside an approved push plan, budget move > $50/day. [B6 E1, PB, #41]

---

## 15. Gap keywords

A gap is a relevant, demanded term we do not target (or target without delivery). Every untargeted row ends as either an **entry candidate with a full launch spec** (match type, price basis, routed SKU, kill condition) or **declined with the reason named** — a declined term stops counting as unexploited opportunity. [DR]

| Gap type | Test | Default treatment |
|---|---|---|
| SQP gap | SQP volume > 0 AND not targeted (PPC "Not Targeted" / Currently Targeting ∈ {NO, N, blank}) | Priority by the syntax's quadrant (below) [AP] |
| Coverage gap | Relevant term ≥ volume threshold → LIVE / PAUSED / MISSING; MISSING with **3+ competitors in the top 30** first | Launch per §14; PAUSED without justification = finding [LTSF] |
| Organic without paid | Ranks organically, no paid support | Cheapest fill; route aged SKUs there [LTSF] |
| Engine-blind | Addressable term with competitor traffic and no search-term row | Gap seeding (§13) [B6] |
| Range gap | Validated demand across competitors for a size/attribute we have no SKU for | Product-plan item for Brand Management, not a campaign (`09`) [LTSF] |

Priority map for SQP gaps by syntax diagnosis (editable per product): STRONG → P1 scale / launch exact ranking; VISIBILITY → P1 launch exact + bid up TOS; CONVERSION → P2 launch selectively, bid to CVR; BOTH FAILING → P2 fix listing / CVR first, hold; niche sizes (e.g. Twin XL, Full XL, RV / Short / Olympic Queen) → P3 backlog; unmapped → review relevance before launch. Never launch gaps on BOTH-FAILING syntaxes or off-category terms. [AP]

- Cross-check coverage against the STR: exact-text matching overstates the gap (close variants already serve). Backend terms close gaps first, free. Sibling-brand overlap = cross-brand bid conflict — resolve before building. Track **SV coverage %**, not keyword count. [LTSF, PB]

---

## 16. Per-keyword output columns (Keyword decisions tab)

Every term, one row, in this order. Missing = blank, never 0.

| Group | Columns |
|---|---|
| Decision | Search term · **Decision** · Rule (id in workbook only) · Why (numbers doing the work) · Action · Expected outcome · Re-read date · Reversal condition |
| Identity | Normalised key · Sources present · Class · Syntax · Root(s) · Hero/Halo · SV tier |
| Demand | SV/month (source) · Weekly SV (source) · SV% · Market traffic |
| Relevancy | Original label and % · Updated % · Source · Confidence · Decision tier · Launch tier |
| Position | Organic rank (30-d median, source) · Sponsored rank · Target rank · Rank gap · Indexing |
| SQP | Market impr / clicks / purchases · Shares · Market & brand CTR, CVR · Target CTR, CVR · Ratios · Listing flag |
| Ownership | Exact owner(s) + state · Owner status · Coexistence reason · Advertised SKU · Correct SKU |
| Performance (30 d and 90 d) | Impr, clicks, CTR, orders, CVR, CPC, spend, sales, ACoS · TOS share / CVR / CPC · PDP share / CVR · ROS share (keyword placement = estimate) |
| Economics | Break-even ACoS and CPC of the routed SKU · Ceiling (ranking terms) |
| Landscape | Rivals present · Rivals advertising · Our share · Landscape verdict (`08`) |

[B6, KCP, MDB, DR]

---

## 17. Anti-patterns

Summing SQP market columns · reordering words or collapsing word-order variants · King before California King · negating on spend alone, or negating brand / rank-target / highly relevant / exact-ranking terms · harvesting a head generic · building beside a paused owner or on deal days · treating the listing score as truth · parking a converting term for thin clicks · contradictory directions on one term · suggested bids or Cerebro CPC used as a price · gap lists padded with close-variant or off-category terms. [SQP, PH, STR, B6, LP, DR, AP]

---

## 18. Open questions for the owner

1. **Relevant zero-order term with no live exact owner.** Resolved — see 13 #38: REVIEW (fix queue); BLOCK only when irrelevant or another product type; with a live owner → REDUCE.
2. **Label mapping.** MKL labels "Relevant", "Lower Relevant" and "Generic" have no tier in any source. This file uses the numeric score (listing scorer if absent). Confirm or give a mapping.
3. **Head-generic guard threshold.** SV ≥ 50,000 comes from one B6 case ("bed sheets", 56,136). Confirm per product, or set a class-only rule (R-CI1: generic terms never pushed, whatever volume).
4. **Harvest ACoS tiers and the 45% runaway filter** are stated against a 30% break-even. Confirm scaling them as shares of the product's break-even.


---

<!-- FILE: references/06-campaign-ppc-decisions.md -->
# FILE: references/06-campaign-ppc-decisions.md

# 06 — Campaign and PPC decisions

The core decision logic for campaigns. Every campaign in scope gets one objective, runs the master decision order once, and ends with exactly one decision label, one action, an expected outcome and a validation date. Keyword-level rules (HARVEST, BLOCK, REDUCE, DEDUPLICATE, CHECK OWNER, MONITOR per term) are in `05-keyword-research.md`; price mechanics (backward-solve, DSTR, budgets, fixed-bid trial) in `07-placement-and-bidding.md`; economics in `03-…`; stock and variation routing in `04-…`; exceptions in `11-…`; grading and escalation in `10-…`.

Source tags: see `13-source-map-and-conflicts.md`. "#n" = conflict-register row n. Rule IDs (R-P1 …) are allowed in workbook Rule columns, never in narrative text (#28).

## Contents
1. Objective assignment
2. Campaign classes
3. Master decision order applied to campaigns
4. The campaign decision set (labels) and pause rules
5. Push qualification
6. Ranking progress test
7. Non-ranking campaigns
8. Levers, holds and reconciliation
9. Structure rules
10. Decision table (the trail)
11. Open questions for the owner

---

## 1. Objective assignment

### 1.1 Rule — per campaign block (Campaign ID), first match wins

| # | Test on the block's targeting | Objective | Source |
|---|---|---|---|
| 1 | Any keyword contains the brand name (brand + misspelling list, substring on lowercased term) | **Defensive** (brand broad included) | [OC, B6 R-O2] |
| 2 | Product targets only; ASIN is in our own product family | **Defensive** (own-page defence) | [WB, B6 R-X1, #15] |
| 3 | Product targets only; ASIN is another of our own brand's products | **Profitable Conversion** (cross-sell) — judged on its own ACoS, never as conquest | [B6 R-X2] |
| 4 | Product targets only; ASIN is a mapped competitor | **Conquest** | [WB, PB, #15] |
| 5 | Category targets, or ASINs not mapped to a brand | **Profitable Conversion** (unmapped: no SCALE until mapped) | [OC, WB, B6 R-X6/E20] |
| 6 | Targeting type = Auto | **Discovery** | [OC] |
| 7 | All keywords Exact and the term is generic niche wording (core, attribute, size) | **Ranking** — or **Market Share** only when the owner has declared it for that syntax | [OC, B6 R-O1, PB, #15] |
| 8 | All keywords Exact and the term is colour, competitor brand, other language, misspelling or adjacent generic | **Profitable Conversion** — a Ranking tag here is blocked | [B6 R-O1, F12, E18] |
| 9 | All Broad, all Phrase, or Broad + Phrase | **Discovery** | [OC, B6 R-O2, WB] |
| 10 | Exact mixed with Broad/Phrase in one block | **Ranking** (when the exact term is generic niche) + **structural flag**: split; usual fix = pause the broad, keep the exact — never on an event day | [OC] |
| 11 | Exact block mixing generic-niche and non-ranking term classes | Ranking only if the block holds the term with the declared target rank, else Profitable Conversion; flag for split | derived from OC + R-O1; record the basis |
| 12 | Nothing found | Profitable Conversion by default + verify the build in the console | [OC, B6 E7] |

**Liquidation (Clearance) is declared, never inferred.** A campaign is Liquidation only when every SKU it advertises is under a confirmed clearance/LTSF plan (file 04) or the product goal is Clearance/LTSF. It changes how the campaign is judged (stock cleared, §7.2), not its targeting rule. Never on a brand Defensive campaign or on a ranking campaign advertising the hero. [B6 R-N2, SR, PB]

### 1.2 Assignment discipline
1. **Campaign level, never per keyword.** Decide once per block, write to every row (campaign, keyword, placement, PT). Only exception: PT rows inside a keyword campaign stay on the ASIN-targeting loop — note it in the basis. [OC, DR]
2. **Name is evidence, not authority.** "(Ranking)" in a name never makes a campaign Ranking; targeting decides. Where name and targeting disagree, say so in the basis. [OC, #15]
3. **The goal authorises, it never retags.** A Profit-First product's generic exacts stay Ranking; the goal gate decides whether they may push. [PB]
4. **Market Share is never assumed.** Only when declared per syntax. [PB, #15]
5. Record three audit fields per block: objective before, basis, change. [OC]
6. **Validation (all must be 0):** blocks with >1 objective (PT rows excepted); blocks with none; Defensive without a brand keyword or own-ASIN target; Ranking without Exact; Ranking on a colour/competitor/language/misspelling term. [OC, B6 E18]

### 1.3 How each objective is judged — and never judged

| Objective | Judged on | Never judged on | Source |
|---|---|---|---|
| Ranking | Rank movement vs declared target and the loss ceiling (progress test, §6) | Weekly CPA/ACoS inside the push window | [PB, DR, OC] |
| Ranking after sufficiency stop | Standard ceiling judgement (break-even) | — | [PB check 6] |
| Market Share | Impression-share band migration and cost to hold it | Organic rank | [PB] |
| Profitable Conversion | CPA vs ceiling (= ACoS vs break-even on 30 & 90 days); realised vs affordable CPC. PT: product-page placement, target ASIN relevant and in stock | Rank | [PB, OC, B6 R-N1] |
| Defensive | Share held per branded query vs its own baseline + cost of defence; ACoS ≤ break-even | CPA alone | [PB, B6 R-N3] |
| Discovery | Converting terms per $100 spend, graduations to exact, harvest performance, wasted spend ≤ 40% | CPA in the first 30 days; any verdict before 15 clicks | [DR, PB, SR] |
| Conquest | CPA vs watch-CPA + share of the target page | Keyword metrics | [PB] |
| Liquidation | Units cleared vs the clearance timeline | ACoS cuts | [B6 R-N2] |
| SB / SBV / SD | Their own metrics: view-through CTR, completion rate, new-to-brand %, CPA | SP metrics | [PB, B6 E12] |

---

## 2. Campaign classes

A Ranking campaign is **push** only while its term is funded in the push plan (passes §5). Every other Ranking campaign is **non-push** and runs the break-even rules (BREAK-EVEN, R-B1–B4). Push status flips as qualification changes; the objective does not. [B6]

| Class | Identify by | Objective | Advertised variation | Price basis / ceiling | Judged by | Notes |
|---|---|---|---|---|---|---|
| Auto | Targeting type Auto | Discovery | Clearance colour (≥ 180 d cover, or ≥ 90 d selling ≤ size median) | ≤ 1.0 × BE CPC | Converting terms/$100, harvests, WAS ≤ 40% | 4 auto groups judged separately; own-ASIN matches negated; mature stage keeps a low-budget sentinel [PB, WB, B6 R-C2] |
| Broad | All broad | Discovery (brand → Defensive) | Clearance colour | Launch ≈ 60% of the exact term's BE CPC (#47), no modifier | as Auto | Built after 100 exact clicks or a coverage gap [PB, #23] |
| Phrase | All phrase | Discovery | Clearance colour | Launch ≈ 80% of the exact term's BE CPC (#47), no modifier | as Auto | Primary root at 0% phrase = gap [PB] |
| Exact — ranking, push | Generic niche, funded | Ranking | Size's best seller (hero) | Push price, ceiling 2 × BE CPC | Progress test §6 | TOS 70–90% of clicks, PDP ≤ 20% [B6 R-P1–P8, R-C1] |
| Exact — ranking, non-push | Generic niche, not funded | Ranking | Hero | Toward BE CPC | Rank held at BE | Rejoins push when it qualifies [B6 R-B1–B4] |
| Exact — non-ranking | Colour / competitor / language / misspelling / adjacent | Profitable Conversion | Colour term → named colour, same size; else hero | ≤ 1.0 × BE CPC | Layered rule §7.1 | [B6 R-O1, R-C3] |
| PT — competitor | Mapped competitor ASIN | Conquest | Routed SKU | Watch-CPA; PDP lever, no TOS modifier | CPA + page share | OFFENSIVE / TEST / AVOID (file 08) [WB, B6 R-CI7] |
| PT — own family | Own ASIN | Defensive | Hero | Low bid; ACoS ≤ BE | ACoS ≤ BE, share | [B6 R-X1] |
| PT — own other product | Own brand, other product | Profitable Conversion (cross-sell) | Routed SKU | ≤ BE | Own ACoS | Not a conquest [B6 R-X2] |
| PT — category | category="…" | Profitable Conversion | Routed SKU | ≤ BE | CPA vs ceiling | Category targets can't be bulk-changed — console [CB] |
| Brand / Defensive | Brand word in keyword | Defensive | Hero | BE CPC; allowance only with verified rival presence | Share + cost; ACoS ≤ BE | Funded first when ≥ 3 rivals advertise [PB, B6 R-N3, R-CI6] |
| Liquidation | Declared (§1.1) | Targeting objective + flag | Aged SKU | BE on forward-cash economics | Units cleared | No ACoS cuts [B6 R-N2, SR] |
| SB / SBV / SD | Ad type | Own | — | Start at BE; ceiling 2 × BE on push terms and on brand terms with verified competitor presence, 1 × BE elsewhere (#45) | Own metrics | Outside the SP engine: by hand, own budget line, inside the spend limit; one SB format per push term [B6 E12, R-CI10, F17] |
| Shared multi-product | Advertises other products | — | — | — | Own product's audit | No colour/price automation; spend = row × (tile ÷ rows) [B6 E13, F29] |

---

## 3. Master decision order applied to campaigns

The first gate that fires ends the row; record which gate fired. Exception: a price above its ceiling is always corrected in the same run, whatever gate ends the row. [SKILL, PB, B6 R-P5]

| Step | Exact tests | If it fires | Label | Source |
|---|---|---|---|---|
| 1 Data validity | CVR/ACoS with 0 orders; CTR with 0 impressions; sources conflict (bulk / console / Sellerboard / SQP); margin > 45 days old or price/fee change not re-derived (48 h); no economics for the advertised SKU (halt — never a default break-even); no current state / not in scope list; SKU provenance mismatch | No recommendation; refresh task; over-ceiling price still corrected. Provenance: mixed window → post-change part if ≥ 15 clicks | REVIEW | [PB, SR, B6 F13, E7] |
| 2 Goal & event | Goal (undeclared → Profit-First; Profit-First → protect won rank only; Clearance → no rank logic). Deal day, window with > 2 deal days, 2-week post-event guard, last 7 days unsettled | No verdict on deal data; no launches/folds; deal-state margin and CVR separate; bleed stops and over-ceiling cuts still run; deals amplify a decided push, never originate one | MONITOR (no verdict) or the push plan's label | [PB, B6 E1/E2, #27] |
| 3 Economics | Margin/unit of the advertised SKU at the price in force; BE CPC = margin × placement CVR (own ≥ 50 clicks, blend 15–50, size rate < 15); ceiling = 2 × BE CPC at TOS for ranking, 1.0 × BE CPC at every placement for non-ranking; BE ACoS outside 5–70% → flag | Price > ceiling → to ceiling now, never deferred | PUSH (at ceiling) / BREAK-EVEN / CUT | [B6 R-P3/R-P5, SR, #3] |
| 4 Inventory | Advertised variation: Green ≥ 60 d cover (30-day pace), Yellow 21–59, Red < 21 or stock-out before next dated inbound; hero < 7 days; available 0; cover short of arrival by ≤ 7 d (TIGHT) or > 7 d | Red → taper, re-point to same-size backup same day (by hand). 0 → pause push. Hero < 7 d → break-even only. Yellow → no new push/raises, keep spend, dated re-entry. TIGHT → ease before stock-out, no swap | BREAK-EVEN / REVIEW (switch) / WAIT | [PB, B6 R-I1–I6, R-C6, #9, #10] |
| 5 Structure | Keyword, ad group, campaign enabled; right variation (§9 S4); indexed (not → no spend, indexing task; backend-only ranking term → listing task); objective matches targeting; one live exact owner; shared; SB/SD | Paused → restart decision, no price change. Duplicate → losers withheld. Retag. Switch variation by hand. Shared/SB/SD → out of automation | RESTART / REVIEW / DEDUPLICATE / CHECK OWNER | [PB, DR, B6 R-S1/R-S2, R-C1–C5, E6, E13] |
| 6 Sample | Bid read ≥ 15 clicks (30 d); CVR verdict ≥ 100 clicks (own TOS CVR usable from 50); CTR verdict ≥ 1,000 impressions; PT ≥ 11 clicks. **Any row with orders skips to the objective loop** | Below floor, 0 orders → no change; formula-only correction if over ceiling (< 15 clicks and 20–25% over → to ceiling in one cycle, then suppression check next cycle) | MONITOR | [PB, SR, B6 R-B4/E3, #11] |
| 7 Delivery | In-budget < 70% of day (0% with $0 = missing data). Ranking: PDP > 20% of clicks on ≥ 15; clicks ≥ plan but TOS < 30%. Boost at 900% and price unreachable. CPC well above ceiling AND low clicks (suppression) | Budget first; then MIX FIX before any price move; cap → base per R-M2; suppression → fixed-bid trial (owner-approved, file 07) | MIX FIX / REVIEW | [PB §4A, B6 R-M1/R-M2, WB, #7] |
| 8 Quality | Four-quadrant: CTR & CVR vs market × 1.10, fail < 0.9 × target. SQP CTR or CVR < market on ≥ 30 clicks. Rank −10 places in 30 d with clicks. Rival move (price cut > 15%, new discount, traffic > +50%). CVR drop after a logged price rise. Branded CVR collapse | Conversion → fix offer, no push (≥ 4 weeks chronic: bids at maintenance). Both failing → reduce, listing first. Listing flag → WAIT. Rank drop → freeze, find cause. Rival move → hold 3 days. Price rise → hold, revert or recompute BE | WAIT / REVIEW | [#20, B6 E4/E15, R-CI11, PB §10] |
| 9 Objective loop | Ranking: push qualification (§5) then progress test (§6). Non-ranking: §7 | per loop | PUSH / HOLD RANK / BREAK-EVEN / CUT / KEEP / SCALE / DEFEND | §5–7 |
| 10 Size & bound | Push ≤ +30%/day; other raises ≤ +25%/cycle; gradual cuts ≤ 15%/cycle; CUT ≤ 30% of base; BREAK-EVEN ≤ 50%/step; decisive cuts ≤ 50%; base ≤ 50%/step; boost ≤ 900%; base ≥ price ÷ 10; $0.50 floor (provisional; lower ceiling wins); budget = plan clicks × TOS price × 1.05 (+ PDP spend); min $10; spend limit | Cap the step; gap > cap → two dated steps. Over limit → scale push budgets, cut from the bottom of the funded list | (same label, sized) | [#5, B6 R-P4, E17, E19, SR, PB] |
| 11 Landscape | Competitor influence rules (file 08): agrees / stretch / reachable / challenge / engine-blind | Changes order, read window or wording — **never a price** | (same label) | [B6 R-CI4] |
| 12 Log | Trail: input → metric → rule → decision → action → expected outcome → validation date | — | — | [SKILL] |

**Human-confirm before shipping:** structural change (campaign, routing, match type, strategy, pause); bid move > 25% outside an approved push plan (an approved push plan covers its own +30%/day steps); budget move > $50/day; SV ≥ 500 terms; any gate failure. State the trade-off in reviewer units ("holds ~$180/wk of saving to keep ~66 orders/wk"). [PB §13A, #32, #41, #54]

---

## 4. The campaign decision set (labels) and pause rules

One label per campaign per cycle. The keyword-level labels (HARVEST, REDUCE, BLOCK, DEDUPLICATE, CHECK OWNER) are applied to terms inside the campaign and reconciled at campaign level (§8.5).

| Label | Applies to | Enter when | Action and bounds | Source |
|---|---|---|---|---|
| **PUSH** | Ranking, funded | Passes all push gates (§5), goal Growth/Mixed, stock Green | TOS price toward push price = BE × (1 + premium), ≤ +30%/day while not holding top, never above 2 × BE; budget = plan clicks × price; mix 70–90% TOS | [B6 R-P1–P4] |
| **WAIT** | Ranking, would-be push | A fixable gate fails: listing flag, ceiling < our TOS CPC, stock Yellow/TIGHT, missing property of the 5-property gate, event day for a new start. (Rank > ~30 places from target → MONITOR (too far), `05` §10 step 6) | No raise; price ≤ ceiling; blocker named with owner and re-test date; if the owner declines the fix, the row becomes BREAK-EVEN | [B6 R-P1, F25, F26, #50] |
| **HOLD RANK** | Ranking at/inside target | Organic rank ≤ target | Keep price, no raise; after 2 clean weeks taper −10%/week to a floor 5–10¢ below the delivering placement's blended CPC; restore on slip | [B6 R-P8, PB, #26] |
| **BREAK-EVEN** | Non-push ranking | Price > BE CPC | 0 TOS clicks in 30 d → straight to BE. TOS clicks > 0 → step down ≤ 50% toward BE; restore one step if rank falls > 10 places. Price ≤ BE → KEEP | [B6 R-B1–B3] |
| **CUT** | Non-ranking (PC, Discovery, Defensive) | ACoS > BE on both 30 & 90 d, ≥ 15 clicks | Base × (BE ACoS ÷ ACoS), i.e. −(1 − BE/ACoS), max −30% per step | [B6 R-N1, #16] |
| **MIX FIX** | Ranking | PDP > 20% of clicks on ≥ 15 clicks, or TOS < 30% of clicks at/above plan | Base −50% (−25% if product pages bring orders); boost raised in the same write so the TOS price holds; boost ≤ 900%, base ≥ price ÷ 10; re-check day 7 | [B6 R-M1, PB, WB] |
| **DEFEND** | Brand keywords, own-ASIN PT | Defensive objective | Keep on hero with enough budget (utilisation 100% before bids); ladder / restore per the six defensive states (§7.4); ACoS ≤ BE | [B6 R-N3, R-X1, PB] |
| **RESTART** | Paused campaign/keyword that owns a needed term | Term needed (ranking, harvest, defence) and a paused owner exists (close variants count) | Re-enable instead of building; non-push restarts at BE; state change only — no bid written in the same row; never on an event day | [B6 R-S2, F16, DR] |
| **KEEP** | Any | Inside its rule band: non-ranking BE ≥ ACoS > 50% BE; non-push ranking at ≤ BE; 30-d inside but 90-d over | No change; re-read next cycle | [B6 R-B3, R-N1] |
| **REVIEW** | Any | Owner decision needed: quarantined data; 3 days at ceiling without holding top; stop proposed (> 2 × BE); shared campaign; SB/SD; unmapped competitor; State E with no cause; variation switch; structural change; plan > capacity | Named question, evidence, options with trade-off; only downgrading interim actions (ceiling correction, one CUT step) | [B6 R-P6, E5, E7, E13, E20, PB] |
| **SCALE** | Non-ranking; competitor PT | ACoS ≤ 50% BE with orders (≥ 15 clicks); competitor PT ACoS ≤ BE on ≥ 15 clicks | Raise ≤ +25% per cycle, never above BE CPC; Green stock only (Yellow = no raises); not in a Conversion/Both-failing quadrant | [#16, #5, B6 R-X3] |
| **MONITOR** | Any | Below sample floor with 0 orders; event/deal data; 30-d over BE but 90-d inside | No change; named re-read date | [B6 R-B4, R-N1 WATCH, E1, E3] |

### 4.1 Pause and stop rules (all state changes are human-confirmed and never loaded on event days, except stock-out)
1. **Duplicate losers** → paused (withheld), nothing else changed. [PB, #13]
2. **Available = 0 on the hero** → pause the push; ranking ads to the same-size backup. Allowed on event days. [B6 R-I5]
3. **Non-ranking campaign ACoS > 2 × BE on ≥ 30 clicks (90 d)** → stop proposed (REVIEW); interim: one CUT step. [#16, B6 R-K3]
4. **Competitor PT ≥ 20 clicks 0 orders, or ACoS > 2 × BE on ≥ 30 clicks** → pause the target / negative ASIN. [B6 R-X5]
5. **Conquest exit** (§7.5) → pause the target, or rotate to a better-qualified ASIN. [PB]
6. **Push stop-loss** (4 consecutive flat reads, State B) → concede/defer; budget reallocated to the next winnable term; campaign returns to BREAK-EVEN. [PB]
7. **Push stop on conversion** (TOS CVR below market on ≥ 50 clicks) → back to BREAK-EVEN (price, not state). [B6 R-P7]
8. **Mixed Exact + Broad block** → pause the broad, keep the exact (post-event). [OC]
9. **Live keyword off the listing** (product type the listing doesn't sell) → pause. [WB]
10. **Zero-order terms** are not paused as a campaign action: irrelevant → negate (≥ 5 clicks); relevant ≥ 20 clicks 0 orders → REDUCE + fix queue with a live exact owner, REVIEW (fix queue) without one; never negate an exact ranking term or a brand term. [#12, #38]
11. **Never pause a converting row for thin clicks.** [PB, DR]

---

## 5. Push qualification

### 5.1 Product-level preconditions (before any term is considered)
- Goal authorises ranking spend: Growth/Scale or Mixed. Profit-First: no new push (won rank may be protected without the allowance). Clearance: none. Undeclared → Profit-First. [PB]
- Spend limit and margin rule stated for the window (no push can be sized without them); a baseline that excludes deal and settling days. [B6 F03, R-F5]
- Code-red TACoS state freezes all scale (only if the owner set a TACoS target — otherwise TACoS is monitored only). [PB, #17]
- Concentration: one term > ~25% of product clicks, or top 5 > ~60%, needs a declared head-term push, else a named finding. [PB]
- Candidate wording: core product wording only; generic category terms outside the core never enter the push, whatever their volume. *Example (B6): "bed sheets" (155k traffic) stays MONITOR; "bamboo sheets" qualifies; B6 also required ≥ 7 of 13 tracked rivals ranking on the term — state such consensus as a share of the measured roster (a majority of measured rivals), not a fixed count (#46).* [B6 R-CI1, #46]

### 5.2 Candidacy
| Type | Definition | Consequence |
|---|---|---|
| **Cold** | New push | Full realism gauntlet (5.4) |
| **Recovery** | Best rank in last 12 months was top 10, with a logged, resolvable cause | Inherits its prior ceiling; funded before an equal Cold term; recovery push rules (§6.7) |
| **Structure-blocked** | No live exact owner | Fix first: same-day exact build + steering negatives in broad/auto (first post-event day if in an event) — not a harvest case |

[PB, WB]

### 5.3 The six push gates (all must pass; else WAIT with the failing gate named — a reach failure is MONITOR (too far), `05` §10 step 6)
| # | Gate | Test | Source |
|---|---|---|---|
| 1 | Demand / plan | Term has a plan: target rank, DSTR, required units/clicks; core wording | [B6 R-P1, R-CI1] |
| 2 | Converts at the top | Own TOS CVR ≥ market CVR (SQP). CVR basis: own ≥ 50 TOS clicks; blend 15–50; overall/size rate below 15. SQP listing flag (our CTR or CVR < market on ≥ 30 clicks) fails the gate | [B6 R-P1, E15, F26] |
| 3 | Reach | Current organic rank within ~30 places of target | [B6 R-P1] |
| 4 | Stock | Advertised hero Green (≥ 60 d at 30-day pace), no stock-out before the next dated inbound, cover ≥ days to next arrival + 7, available ≥ 7 days; projected cover at push velocity stays out of Yellow/Red through the checkpoint. Cover never on the push pace | [#9, B6 R-I1/R-I2, F30, PB] |
| 5 | Keyword live | Keyword, ad group, campaign enabled; right variation's product ad enabled; indexed; one live owner | [B6 R-P1, PB] |
| 6 | Ceiling covers cost | Ceiling (2 × BE CPC) ≥ our current TOS CPC (TOS spend ÷ TOS clicks) | [B6 R-P1, F25] |

### 5.4 Realism gauntlet (Cold candidates; any fail → no push, name it)
SV > 500 · indexed and present in the listing · purchase intent · CVR ≥ benchmark · reviews ≥ ~50% of the top-5 median · rating no more than ~0.3★ below · price ≤ ~1.25 × category median · Green stock · thin margin → CPC ≤ ~⅓ of margin. Re-entering a ranking posture after stepping back needs a fresh gauntlet. [PB]

### 5.5 Five-property gate (missing one → no push; the missing property named; price held ≤ ceiling)
| Property | Must contain |
|---|---|
| **Sized** | Target rank; DSTR = daily sales at target rank (market data, floor 1/day); paid sales = DSTR − our organic sales on the term (labelled proxy); required TOS clicks = paid ÷ own achieved TOS CVR; budget = clicks × TOS price × 1.05; same data version; projected cover [#19] |
| **Dated** | Horizon and first checkpoint (7-day read) |
| **Ceilinged** | Price ceiling 2 × BE CPC; weekly loss ceiling = (push ACoS − BE ACoS) × projected sales at required spend — hitting it is a human flag, not an auto-stop |
| **Predicted** | Metric, direction, magnitude, horizon — written before money moves |
| **Funded** | Dated release inside the spend limit |

Plan clicks set volume and budget only, never price; reconcile the sum of term requirements to what the product sells. [PB, B6 F21]

### 5.6 Rank-credit and TOS-share checks
- **Rank credit:** auto + broad carry > ~40% of the term's clicks, or no live exact → OUT OF SCOPE for a ranking verdict; structural fix (isolation negatives / exact build). [PB]
- **TOS share:** clicks ≥ plan but TOS < 30% of clicks → MIX FIX first. [PB, WB]

### 5.7 Push pricing
| Item | Rule | Source |
|---|---|---|
| Break-even (TOS) | margin/unit of the advertised SKU × TOS CVR | [B6 R-F2] |
| Premium | rank ÷ target ≤ 1 → none (HOLD RANK); ≤ 1.5 → +25%; > 1.5 → (rank ÷ target − 1) × 50% | [B6 R-P2, #4] |
| Push price | BE × (1 + premium), capped at the ceiling (a premium > 100% always caps) | [B6 R-P2/R-P3] |
| Ceiling | 2 × BE CPC (owner may raise one named term's ceiling for a set time) | [B6 R-P3, #3] |
| Step | ≤ +30%/day while below push price or not holding top; never above ceiling | [B6 R-P4] |
| Over ceiling | Cut to ceiling now | [B6 R-P5] |
| At ceiling 3 days | Without top-3 sponsored and ≥ 30% TOS impression share → REVIEW: raise the ceiling for a set time, or swap the term | [B6 R-P6] |
| Conversion stop | TOS CVR below market on 50+ clicks → stop the push, back to BREAK-EVEN | [B6 R-P7] |
| At 900% boost | Target price > base × 10 → raise base only to price ÷ (1 + boost) with the boost set in the same write; never credit a capped step with new clicks | [B6 R-M2] |
| Bidding strategy | Unchanged; new push campaigns dynamic down-only; fixed only via the fixed-bid trial | [#8] |

*Example: rank 16, target 8 → ratio 2 → premium 50% → push price 1.5 × BE. Rank 12, target 8 → 1.5 → +25%. Rank 30, target 8 → 3.75 → 138% → capped at 2 × BE.*
*Example (B6): "bamboo sheets" at its $6.10 ceiling: hold $6.10, base $1.60 → $1.20, boost → 408% (1.20 × 5.08 = $6.10), ceiling question to the owner. Boost at the cap: base $0.50 × 10 = $5.00 max; correct write base $0.60 + boost 700% = $4.80, not base $1.40.*

### 5.8 Funding order and spend limit
1. Fund in order of revenue potential at target rank ÷ cost to close the gap, after gates. [PB]
2. When plan budget exceeds room: winnable-ground terms (beatable rivals between us and target) first, stretch terms second. [B6 R-CI3]
3. Push budgets + expected other spend ≤ the stated limit; over → scale push budgets, cut from the bottom of the funded list. [B6 R-F5, E19]
4. Weekly: margin after ads below the owner's rule → cut the push from the bottom of the funded list. [B6 R-F6]
5. Price and budget rows load together or not at all; withheld rows never reach the export. [B6 F14, F15]

---

## 6. Ranking progress test

### 6.1 Rank-trend read rules
- ≥ 1 month of rank history (ideally 3); < 1 month → OUT OF SCOPE for a ranking verdict. [PB]
- Organic rank = median over the window; unranked days count; not ranked if half the days are unranked. Use the daily crawl rank; state which rank table governs when two disagree. [B6]
- Exclude stock-out and re-route stretches (too short a remainder → OUT OF SCOPE). Target from the target-rank file/bulk only. [PB]
- State **overall, 14-day and 7-day** trend separately; shorter windows are early warnings. Keep a separate deal-state arc; **the clean arc governs**. [PB]
- Push read window 7 days. On push terms with ≥ 5 rivals at sponsored #1–5, judge rank after 7 days (not 3); TOS impression share alone is not pass/fail. The daily step and ceiling still apply. [B6, R-CI5]
- Estimates (target sales/clicks/budget) size direction; **rank movement governs** — say so on every row. [PB, DR]

### 6.2 States
| State | Condition | Action | Label |
|---|---|---|---|
| **A** | Clicks > plan, rank improving | **Hold price.** Budget rises only if the plan's clicks are budget-truncated and the spend limit allows; keep TOS ≥ 30% of clicks [#6] | PUSH (hold) |
| **B** | Clicks > plan, rank flat | Estimate was low: step price up (≤ +30%/day, ≤ ceiling), rebase targets from actuals, size by rank gap. **4 consecutive flat reads → STOP-LOSS** | PUSH → BREAK-EVEN on stop-loss |
| **C** | Clicks < plan, rank flat | Delivery problem: budget truncation → placement mix / TOS modifier → price step (lever order §8.1) | MIX FIX / PUSH |
| **D** | Clicks < plan, rank improving | Estimate was high, winning cheaply: hold | PUSH (hold) |
| **E** | Rank lost > 10 places despite delivery | Investigate (6.3); freeze price moves; **never scale** | REVIEW |
| **F** | Delivery ≈ 95–120% of plan | Too early; re-read. 4 cycles → re-diagnose (#25) | PUSH (hold) |
| OUT OF SCOPE | No sized plan, no tracked movement, rank credit fails, < 1 month history | Efficiency decision inside a Ranking campaign (break-even rules) | BREAK-EVEN / KEEP |

[PB, DR, WB, #6, #25]

### 6.3 State E investigation order (never a bid change)
1. Anchor the timing of the drop.
2. Own listing first: price, stock-out, reviews, content, coupon/deal ending, colour/variation switch, keyword state → listing finding.
3. Competitor wins ≥ 2 of price / rating / reviews, or competitor went out of stock → name it; route to conquest/PT.
4. Isolated term vs category-wide → category-wide escalates.
5. Nothing found → "investigated, no cause identified" → ask the owner.

[PB, B6 E4]

### 6.4 Competitive shock
- A rival in the term's top 10 makes a brief move (price cut > 15%, new discount, traffic growth > 50%) → hold our price 3 days; don't read the conversion drop as a bid problem. Over-ceiling cuts still apply. [B6 R-CI11]
- CVR ≥ benchmark, rank falling, no own event (and after the 3-day hold if a move was found) → check new entrant/deal/price cut → **one step within ceiling**, re-read in 1 week, log. [PB]
- Stretch target (only aspirational rivals at or above target): progress judged on rivals passed (first milestone); 14 days at ceiling with no rival passed → owner. [B6 R-CI2]

### 6.5 Stop-loss and escalation
- 4 consecutive flat grades on a push (State B) → STOP-LOSS: concede or defer, reallocate the budget to the next winnable term. [PB]
- 2 consecutive flat/backfired grades on any lever → escalate the lever (never repeat it a third time); same verdict 4 cycles with no effect → re-diagnose the row. [SR, PB, #25]
- Grading tolerance: ±3 ranks (ranking), ±3 ACoS points (others). [SR]

### 6.6 Sufficiency stop and incrementality ladder
1. Rank ≤ target → HOLD RANK: keep price, no raise, for the first **2 clean weeks**. [B6 R-P8, #26]
2. Then taper **−10%/week** to a floor **5–10¢ below the delivering placement's blended CPC**; record the floor. [PB]
3. **Restore** the last step (= the recorded floor) on slippage **> 2 places on a top-5 term**, or **any slip below target** outside the top 5; if the term slips past target, it rejoins the push. Re-test the floor quarterly or after a shock. [PB, B6 R-P8]
4. **Incrementality ladder** (organic rank ≤ 3, clean logs): spend −15%, hold 2 weeks; total orders hold → keep stepping; total orders fall > 10% → restore and record the floor. [PB]
5. After the stop, the campaign is judged at the standard (break-even) ceiling. [PB]

### 6.7 Recovery push
Entry: SKU back to Green, prior rank top 5–10 within 12 months, CVR ≥ benchmark, the loss logged to an inventory cause. Target = pre-decline baseline. Week 1 re-point + maintenance, week 2 push, checkpoint at 3 weeks. [PB, WB]

### 6.8 SBV arbitrage
Enter SBV on a push term when SBV CPC ≤ 0.6 × the SP exact CPC **and** SBV CPA clears its own ceiling. Exit when SBV CPC rises past 0.8 × SP exact CPC, or completion rate fades 2 consecutive weeks. Judge on SBV metrics only. Reactive path still needs the 100-click exact candidacy. One SB format per push term; built by hand, own budget line, counted in the spend limit; no launch on event days. [PB, B6 F17, R-CI10]

---

## 7. Non-ranking campaigns

### 7.1 Layered rule (Profitable Conversion, Discovery after its grace period, Defensive ACoS check) [#16, B6 R-N1]
Read campaign ACoS vs the advertised SKU's BE ACoS on **30-day and 90-day** windows; ≥ 15 clicks (30 d); windows with > 2 deal days not used.

| Condition (first match wins) | Decision | Action |
|---|---|---|
| < 15 clicks, 0 orders | MONITOR | none |
| ACoS > 2 × BE on ≥ 30 clicks (90 d) | REVIEW — stop proposed | interim one CUT step; keyword increases neutralised (§8.5) |
| ACoS > BE on 30 d **and** 90 d | CUT | base × (BE ÷ ACoS), max −30% per step |
| 30 d over, 90 d inside | MONITOR (watch) | none; re-read next cycle |
| 30 d inside, 90 d over | KEEP | recent window recovering |
| 50% BE < ACoS ≤ BE | KEEP | none |
| ACoS ≤ 50% BE with orders | SCALE | ≤ +25% per cycle, never above BE CPC at any placement |

- Sizing inside the SCALE cap (provisional — confirm with the owner before first use): CONFIRMED 15+ clicks / 2+ orders / CPA ≤ ~70% of ceiling → hold; STRONG 30+ / 3+ / ≤ ~60% → ≤ +10%; PROVEN 50+ / 5+ / ≤ ~50% → ≤ +15%. [PB, WB]
- Target ACoS 50% BE and max 75% BE are reported bands, not triggers — break-even triggers. [SR, B6 F31]
- A reduction on a term that still sells (≥ 10 orders in 90 days) and that rivals buy is a cut to break-even, never a block. *Example (B6): "king size bamboo sheets set" — 61 orders, 29.8% ACoS vs 23.8% BE, 11 rivals advertising → reduce to break-even.* [B6 R-CI9]
- Before a cut batch ships: does projected lost-order value exceed spend saved, at the more conservative margin? Withdraw failures. Check auction density before calling a cut safe. [PB]
- Price attribution: CVR drop coinciding with a logged price rise → hold; revert, or recompute BE from the new price. Profitable only at rest-of-search with no rank case → near-0 TOS modifier, stated. [PB]

### 7.2 Liquidation / clearance exemption [B6 R-N2, SR]
- Not cut on ACoS; judged on units cleared vs the clearance timeline (file 04 ladder).
- Price ceiling = BE on forward-cash economics (file 04); relevance-based blocks (irrelevant zero-order terms) still apply; spend limit still applies.
- Green → run up to BE; not Green → no push; never a clearance push while the hero of that size is Red; negative contribution → a pricing decision for the brand manager, not bids; exit when stock falls below the surcharge threshold.
- Lever reads at day 7 and 14; < 50% of the predicted uplift → replace the lever, don't extend it. Before calling a SKU "tested and failed", confirm it ever had dedicated spend. [LTSF]
- Peak-week availability outranks LTSF economics when a calendar marks the week as peak. [PB]

### 7.3 Discovery
- **Grace:** first 30 days judged only on converting terms per $100 and graduations; no campaign CUT. Term-level verdicts from 15 clicks. [DR, PB]
- **Metrics:** converting terms per $100 = terms with ≥ 1 order ÷ (spend ÷ 100); graduations = terms moved to their own exact (≥ 3 orders at ACoS ≤ BE, no live exact owner — HARVEST; negate at source in the same deployment); wasted spend ≤ 40% (above → negation pass). [DR, #22, #24]
- **Building a discovery layer:** reactive = ≥ 100 qualified clicks on the term's own exact history (near-miss ≈ 20); proactive = coverage gap (e.g. primary root at 0% phrase). < 100 → ineligible, no pricing. Check for an existing instance first. [PB, #23]
- **Variation:** size's clearance colour (≥ 180 d cover, or ≥ 90 d while selling ≤ size median); hero stock reserved for ranking. [B6 R-C2]
- After grace, the campaign runs the layered rule (§7.1). [B6 R-N1]

### 7.4 Defensive (provisional — confirm before first use) [PB, B6]
- Pricing: break-even CPC (margin × CVR of the advertised SKU); above-ceiling allowance only with a rival or non-brand seller actually seen on the branded term (STR or placement capture), bounded by 2 × BE CPC; withdrawn after 2 consecutive reads without presence.
- Share = impression share per branded query vs that query's own prior baseline (blended branded only as a named fallback).
- Keep on the hero, funded; judged ACoS ≤ BE. Brand terms with ≥ 3 rivals advertising → DEFEND at TOS, funded first, add own-ASIN PT. [B6 R-N3, R-CI6]

| State | Condition | Action |
|---|---|---|
| 1 Correct | Share held, ACoS within 10–15% of ceiling | Ladder −~10%/week to the floor that still holds share; record it; never scale past it |
| 2 Slipping | Share slipping, or a competitor ad on our detail page | Restore one ladder step + open/expand own-ASIN PT; the syntax's defence budget caps the response |
| 3 Under-spent | Utilisation < 100% | Budget to 100% utilisation before bids (Ranking 80%+, Discovery 70%+) |
| 4 Conquested | Competitor ad above our organic slot on our brand term | Restore step + SB headline on brand root (SBV if none) + own-ASIN PT on attacked ASINs; weekly review |
| 5 Inflating | Branded ACoS up while share holds | Find the cause; if a rival bids our brand up, cap at the defence budget; never chase past ceiling |
| 6 CVR collapse | Branded CVR falls | Listing first (suppression, buy box, reviews, variation break) |

### 7.5 Conquest (provisional) and competitor PT [PB, B6 R-X3–X6, R-CI7]
- Same ASIN already targeted → decide from that instance; one owner per ASIN.
- **Entry (new target, #44):** OFFENSIVE (file 08) **and** the routed SKU wins ≥ 2 of 3 (price, rating, review count), or target out of stock; else TEST; missing data → ask. Existing targets are judged on their own clicks and orders (verdicts below). *B6 form: OFFENSIVE = pricier for fewer pieces, or same price with < 50% of our reviews; AVOID negated in auto/PT.*
- **Ceiling = watch-CPA** = lower of the routed SKU's break-even CPC (margin × CVR) and the price-gap-adjusted figure; state which governs. Product-page lever, no TOS modifier.
- **Verdicts:** PT floor 11 clicks. SCALE (ACoS ≤ BE, ≥ 15 clicks) ≤ +25%/cycle up to BE CPC; REDUCE when ACoS > BE on ≥ 15 clicks; BLOCK at ≥ 20 clicks 0 orders or > 2 × BE on ≥ 30 clicks; unmapped ASIN → no SCALE.
- **Exit / rotate:** target delisted; target no longer wins 2-of-3 (hold); CPA > watch-CPA 2 consecutive reads with no page-share gain. Rotate when another ASIN clears the gate and is better (budget and structure carry over).
- CPC > 1.5 × family median on the same term → flag (family-wide = market; our row only = our bid).

### 7.6 Market Share (declared only) [PB]
| State | Condition | Action |
|---|---|---|
| Headroom | Primary root IS < ~12%, profitable in band | Expand exact + phrase coverage, step budget, track IS migration |
| Dominance too expensive | IS ≥ ~41%, ACoS over band | Hold share, ladder down to the minimum CPC that preserves it; marginal ACoS check |
| Cap enforced | Secondary syntax over its spend-share cap (~25%) | Cut to cap, excess to primary |
| Coverage worklist | Relevant size/colour/attribute cell with no funded campaign | Fund or decline and log; track SV coverage % |
| Step and verify | IS stuck at band floor ≥ 2 cycles, ACoS in band | One budget step; IS must move in 2 weeks, else TOS modifier / CPC |
| Structure gap | Primary root at 0% phrase | Stand up phrase at modest budget |
| Falling demand | Seasonal SV declining | Hold/contract; re-time expansion |
| Variation flow | Share on one stock-vulnerable child | Rebalance across children |

Marginal ACoS = Δspend ÷ Δad sales; > 2 × blended → unwind the step. [PB]

---

## 8. Levers, holds and reconciliation

### 8.1 Lever hierarchy (resolved, #7)
1. **Evidence first:** budget truncation (in-budget < 70% of the day) → budget before anything; truncated rates are not evidence.
2. **Placement mix / TOS modifier** — the rank lever (MIX FIX pair when PDP > 20%).
3. **Price step** (within caps).
4. **Base bid last** for ranking (if the campaign only wins product pages, the base goes below the PDP clearing price while the modifier carries the TOS price).
5. **Bidding strategy unchanged** unless the fixed-bid trial fires (owner approval).
- Non-ranking: the base bid is the lever. ROS lifted to ceiling only after 15+ ROS clicks converting ≥ the campaign's PDP rate. [DR, PB, WB]
- Never let TOS fall as the residue of a base cut; never lower a ranking campaign's effective TOS unless it is above the ceiling. [WB, PF]

### 8.2 One lever per row per cycle
- One lever per entity instance per cycle; different rows of a campaign may each move. [DR, PB]
- **Exemption:** one keyword's base bid + its placement modifiers form one backward-solve (TOS/ROS targets set first, then base, then both modifiers re-solved) — counts as one lever. MIX FIX is such a pair. [PB, B6 R-M1]
- Budget may ship with a price change only when both come from the same forward math (push plan). A campaign where only one lever type was ever written though budget, TOS and bid each warranted evaluation → re-examine. [PB]
- Two levers in the same window confound the read — say so in the grade. [LTSF]

### 8.3 Silent-hold list (exhaustive)
A hold at the objective-loop stage is allowed without asking only for: (1) both quality gates fail; (2) CTR passes, CVR fails (brand-management finding); (3) zero delivery; (4) budget truncation; (5) plan exceeds the campaign's capacity (escalate). Any other hold → ask the owner first and log the question and answer. Gate outcomes (quarantine, sample floor, stock, paused, duplicate, event day) are recorded with their gate, not as holds. [PB, DR]

### 8.4 No bid change when
- Row paused, withheld duplicate, or SKU below the stock gate; budget truncated; zero delivery; both quality gates fail; CTR passes and CVR fails. [DR, B6 E6]
- State E (rank collapse) — never a raise. [PB check 9]
- A rival's brief move in the last 3 days (except over-ceiling cuts). [B6 R-CI11]
- Rank dropped > 10 places in 30 days while getting clicks, until the cause is found. [B6 E4]
- Shared multi-product campaign, SB/SBV/SD (hand decisions only). [B6 E12, E13]
- Deal-day data would be the evidence. [B6 E1]
- Price came from Amazon's suggested bid or a competitor's CPC (never used). [#18, B6 R-CI4]
- Price attribution unresolved (CVR drop with a logged price rise). [PB]

### 8.5 Reconciliation at campaign level [SR, DR, B6]
1. Campaign referred for stop/turn-off or owner review (not a high-budget review) → every keyword **increase** inside it is neutralised to hold.
2. Budget raise dropped when ≥ 60% of the campaign's keyword rows are cuts/negations and none are increases.
3. Reconciliation only downgrades; it never invents an action; annotate the reason.
4. **One direction per term across campaigns** — a term cut in one campaign and raised in another fails; resolve to the single owner.
5. Price and budget rows load together; withheld rows never exported; every written value must match its label (a "taper" that raises price fails).

---

## 9. Structure rules

| # | Rule | Detail | Source |
|---|---|---|---|
| S1 | **One campaign per search term** | One live exact owner per term (close variants count: plural, symbols; word order is a different term). Negative exact for owned terms in the discovery campaigns that serve them (isolation wall), in the same upload as the owner goes live | [B6 R-S1, WB, #14] |
| S2 | **Duplicate owners** | First test coexistence: stage-stack (earlier-stage campaign deliberately left running), placement-split, variation-split (different size/colour child), sibling ownership (another product in the family owns its instance). Else owner = higher CVR at lower CPC with ≥ 15 clicks each; below that, most orders; tie → longer clean history. Losers withheld, nothing else changed. Check duplicates again after any re-enable | [#13, PB, PF] |
| S3 | **Paused owners** | Term exists (live or paused, close variants) → restart/reuse, never build a duplicate; a price change can't make a paused keyword serve; keeper inside a paused campaign won't serve (campaign-level edit needed) — count and state | [B6 R-S2, F16, E11, LP] |
| S4 | **Colour / variation** | Ranking = size's best seller; discovery = size's clearance colour; colour-named terms = that colour; size never changes (except correcting a wrong size); a colour with < 7 days of cover never added; switch to backup only when hero cover < days to arrival by > 7 d; switches by hand; routing read from Product Ad rows, never names. Every re-route rebuilds break-even from the new SKU and resets the CVR baseline and rank clock | [B6 R-C1–C6, E8, E9, #29, PB] |
| S5 | **Objective retags** | From targeting and term class only (§1); a Ranking tag on colour/competitor/language/misspelling is blocked; retag carries a verdict line | [B6 R-O1, F12, E18] |
| S6 | **No structural change mid-event** | Folds, splits, new structures, restarts of non-push campaigns → decided in the post-event audit | [B6 R-S3, E1, F19] |
| S7 | **Brand negatives last** | Negatives on brand terms in a brand broad only after the receiving brand exacts are Defensive, on the hero and funded | [B6 R-S4, E10, F18] |
| S8 | **No launches on event days** | New campaigns wait for the post-event audit (they learn on deal traffic and can't be judged); one SB format per term | [B6 F17, E1] |
| S9 | **Mixed match types** | Exact + broad in one campaign → split (pause broad, keep exact) post-event | [OC] |
| S10 | **Scope** | Only campaigns read in the current state get decisions; campaigns spending on the product but missing from the list are added and marked; shared campaigns excluded from automation | [B6 F13, F29] |
| S11 | **Build hygiene** | Exact is the default match type; dynamic down-only for new campaigns; launch price from break-even maths, never a suggested bid; routed SKU ≥ 21 days of cover to launch | [PH, #8, #18, PB] |

---

## 10. Decision table (the trail)

Every row carries input → metric → rule → decision → action → expected outcome → validation date. Outcomes are directional unless the row has its own measured step history; name any soft coefficient. Grade at ±3 ranks / ±3 ACoS points (file 10).

| Condition (metric + threshold) | Decision | Action | Expected outcome | Validation |
|---|---|---|---|---|
| Gates pass, goal authorises, Green, rank > target | PUSH | ≤ +30%/day toward BE × (1 + premium), ≤ 2 × BE; budget = clicks × price × 1.05 | Rank toward first milestone; TOS 70–90% of clicks; top-3 sponsored; TOS IS ≥ 30% | Day-7 rank read (overall/14d/7d); 3 days at ceiling → owner |
| Fixable push gate fails | WAIT | No raise; ≤ ceiling; blocker + owner + date | Term re-qualifies | Named date; owner declines → BREAK-EVEN |
| Organic rank ≤ target | HOLD RANK | Keep price 2 clean weeks, then −10%/week to floor | Rank held at lower cost | Weekly; slip > 2 (top 5) or below target → restore floor |
| Non-push ranking, price > BE | BREAK-EVEN | 0 TOS clicks → to BE; else ≤ −50% toward BE | Cost per order ≤ margin; rank held within 10 places | Next cycle; rank −10 places → restore one step |
| Non-ranking, ACoS > BE on 30 & 90 d, ≥ 15 clicks | CUT | Base × BE/ACoS, ≤ −30% | ACoS toward BE next 30-day window | ≥ 15 fresh clicks; flat twice → escalate lever |
| Ranking, PDP > 20% clicks on ≥ 15, or TOS < 30% at plan | MIX FIX | Base −50% (−25% if PDP sells) + boost so TOS price holds | PDP ≤ 20%, TOS 70–90%; TOS price unchanged | Day 7 placement report |
| Brand keyword / own-ASIN PT | DEFEND | Utilisation 100%; ladder or restore per state | Share per branded query ≥ baseline; ACoS ≤ BE | Weekly share read; 2 reads with no rival → allowance off |
| Paused owner of a needed term | RESTART | Enable (state only), BE price, post-event | Term serves with its history | First read at 15 clicks on the right SKU |
| Inside its band | KEEP | None | Stable | Next cycle |
| Owner decision needed (§4 list) | REVIEW | Question + evidence + options; downgrading interim only | Decision recorded | Owner answer by named date |
| ACoS ≤ 50% BE with orders; competitor PT ≤ BE on ≥ 15 clicks | SCALE | ≤ +25%/cycle, ≤ BE CPC | More orders at ACoS ≤ BE | Next cycle; marginal ACoS > 2 × blended → unwind |
| < 15 clicks & 0 orders; deal data; 30 d over / 90 d inside | MONITOR | None | Sample accrues / clean window | Named date (15 clicks or first clean week) |
| 4 flat push reads | PUSH → BREAK-EVEN (stop-loss) | Concede/defer, reallocate | Budget moves to a winnable term | Next term's day-7 read |
| TOS CVR < market on ≥ 50 clicks | BREAK-EVEN (push stopped) | Back to BE | Loss per order removed | Listing check before any re-entry |
| Hero available = 0 / Red | BREAK-EVEN + REVIEW (switch) | Pause push; ads to same-size backup | Rank protected on backup | Arrival date; re-entry plan |

---

## 11. Open questions for the owner

1. **Phrase-only blocks:** Resolved — see 13 #35: Discovery.
2. **Exact term class:** Resolved — see 13 #36: colour, competitor-brand, other-language and misspelled exacts → Profitable Conversion, on top of #15.
3. **CUT step:** Resolved — see 13 #37: over BE on both 30 and 90 days → cut up to 30% of base; the 15%/cycle limit applies only to target-chasing trims.
4. **Competitor PT SCALE:** Resolved — see 13 #5 / #16: raises other than push steps ≤ +25%/cycle.
5. **WAIT duration:** Resolved — see 13 #50: held until a named re-test date or until the owner declines the fix; then BREAK-EVEN.
6. **Non-push ranking term below BE outside an event:** Resolved — see 13 #51: KEEP (no raise) unless it qualifies for the push.


---

<!-- FILE: references/07-placement-and-bidding.md -->
# FILE: references/07-placement-and-bidding.md

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
| **TOS-share pre-check**: ranking row with clicks at or above plan but **TOS < 30% of clicks** | **MIX FIX first** (placement fix): base down toward PDP break-even, boost up to hold (or reach) the TOS target, ROS re-solved, all in one pass. No price raise is judged until the mix is fixed | [PB, WB] |
| Priced out (D2) on a qualified push term | Lever pair: base down (mix fix §4) and TOS price up by the push rules (§3). Target the push price, not `clearing × 1.08` in one write. PF's one-shot jump is replaced by the daily step (register #5) | [PF, B6, register #5] |
| Clearing CPC > ceiling on a push candidate | WAIT: the term cannot hold the top at a profitable price. Owner decides on a time-limited ceiling raise | [B6 R-P1, F25] |
| Ranking campaign, PDP > 20% of clicks on ≥15 clicks | MIX FIX (§4), paired in the same write | [B6 R-M1] |
| Ranking campaign with 0% boost | Defect. Backward-solve (§6) | [WB] |
| Ranking row at TOS price above overlay | Cut to the ceiling (2 × break-even). PF's 1.30× overlay and 0.75× push levels are replaced by register #3 | [register #3] |
| Visibility-quadrant syntax (CTR fails, CVR passes) | Use TOS impression share to find the cause: IS < 5%, TOS IS < 15% and rank > 4 → placement and auction (price step, then boost, then base under the bleeding placement); TOS IS < 15% and rank ≤ 4 → placement only (boost); TOS IS 15–30% → moderate gap (boost); TOS IS > 30% → listing issue (no bid change). No IS and no rank → undetermined, no CTR-driven bid change. Step sizes follow §3 and register #5 | [SR B1] |
| Non-TOS placement with a modifier > 0 that bleeds (0 orders on ≥ 3 clicks, or spend share > 1.5 × sales share and > 30%, or ACoS above break-even) | That placement modifier → 0%. Moves of ≤ 2 points are noise. Runs on deal days too (a bleed stop) | [SR, register #16, #27] |

---

## 3. Pricing a push term

A term is pushed only if it passed the push qualification in `06-campaign-ppc-decisions.md`: the product goal allows ranking spend; it converts at or above market at the top; it is within about 30 places of target; the advertised variation is Green with cover ≥ days to next arrival + 7, no stock-out before the next inbound, and projected cover staying Green through the checkpoint; the keyword and campaign are live; the ceiling ≥ our TOS CPC; and the listing is not flagged. A term that fails any of these is WAIT, not PUSH (a reach failure is MONITOR (too far), `05` §10 step 6). [B6 R-P1, register #9, #42]

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
| P6 | At the ceiling **3 days** without holding the top | **REVIEW** (owner decision): raise the ceiling for a set time, or swap the term. Money alone is not working at a profitable price | [B6 R-P6, E5] |
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
| Days 3–5 at $7.20, not holding | P6 | REVIEW (owner): time-limited ceiling raise or swap |
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
| M9 | **Re-check after 7 days**: PDP share, TOS share, TOS impression share. Still > 20% → next base step, ≤ 50%. At the base floor with PDP still > 20% → REVIEW (owner): fixed-bid trial candidate (§8.1). A strategy change needs approval | [B6, WB, register #8] |
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
- **Projected days of cover** through the checkpoint = (available + dated inbound on its ETA) burned at baseline velocity + the push's order gap. It must stay Green. Dropping into Yellow (< 60) or Red (< 21) blocks the push: shrink the gap, wait for inbound, or get an explicit time-boxed owner acceptance. Red is never accepted. Use the 30-day pace, never the inflated push pace. [PB, WB, B6 F30, register #9, #42]

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
| Approval | Any budget change **> $50/day** → owner approval (Change Review Sheet) | [PB, register #32, #41, #54] |
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
| Price | **Broad ~60%, Phrase ~80% of the exact ceiling.** Here "exact ceiling" = the exact term's break-even CPC (discovery never gets the ranking allowance). Relevancy tier sets the position: highly relevant → upper end, semi-relevant → lower | [PB, register #23, #47, WB] |
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
| Any deal-day spend limit is an explicit, dated, time-boxed exception with its margin stated (e.g. B6: $1,300/day on 29–30 Sep at ~7% margin after ads vs the 10% rule). A single event week may run up to +50% over the owner's spend limit, only as that pre-approved exception and never retroactive (no TACoS-derived envelope, register #17) | [B6 R-F5, PB] |
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

1. **Base cut cap vs over-ceiling base.** Resolved — see 13 #48: price over ceiling goes to ceiling this cycle via base + boost together; the 50% base-cut limit still applies, with a second step scheduled if needed.
2. **"Exact ceiling" for discovery pricing.** Resolved — see 13 #47: the exact term's break-even CPC, not the 2× push ceiling.
3. **Projected-cover threshold for a push.** Resolved — see 13 #42: projected cover must stay Green (≥ 60 days) through the push checkpoint, or the push is blocked, shrunk or time-boxed.
4. **Funding order.** B6 funds "in priority order" without defining the order. This file uses the plan-builder's order (revenue at target ÷ cost to close) with the workbook-builder's tie-breaks (DSTR, cover, CVR). Confirm, or give the B6 order.
5. **Approval for push steps.** Resolved — see 13 #41: an approved push plan covers its own +30%/day steps.
6. **Terms whose market cannot support 1 sale/day.** One engine routes these out of Ranking, while placement-first says feasibility never strips the objective. This file applies the strip only when the whole market is < 1 purchase/day and applies the re-scope otherwise. Confirm.


---

<!-- FILE: references/08-competitor-market.md -->
# FILE: references/08-competitor-market.md

# 08 — Competitor and market analysis

Phase 3 (market and competitors) and Phase 8 (competitor influence, gaps, ASIN targets). Competitor data decides **which terms, in which order, which pages, and how progress is judged**. It never sets a price: every price stays break-even-based (break-even CPC, ceiling, push price, TOS price = base × (1 + boost)).

## Contents
1. Data pulls, in order (what each gives, limits, coverage rule)
2. Roster, tiers, scoreboard, traffic trend
3. Per-rival profile checklist
4. Market view
5. Keyword landscape join
6. Engine-vs-landscape verdicts and first milestones
7. Competitor ASIN targeting (OFFENSIVE / TEST / AVOID / LOW TRAFFIC), conquest entry and exit
8. Competitor → engine influence rules R-CI1–R-CI12
9. Gap analysis (template, gap families, size battlegrounds, seed list)
10. Sponsored Brands / video test design
11. Limits (what no connected source gives)
12. Outputs and checks
13. Open questions for the owner

Thresholds tagged [B6] were set on one market (bamboo sheets, ASINsight 7-day traffic units). They are the defaults. For a much smaller or larger market the owner may rescale them — ask, and record the answer.

---

## 1. Data pulls, in order

Pull everything before you write a finding. Date every pull. Store raw JSON or exports beside the workbook.

### 1.1 Pull sequence

| # | Source / call | What it gives | Limits / traps |
|---|---|---|---|
| 1 | Command Center `traffic_products` → `traffic_competitors` | Our product id. Mapped roster: parent ASIN, brand, marketplace, **mapping tier** (Aspirational / Beatable / Poor), keyword count, 7-day traffic, import date | No export → traffic null. That means **unmeasured**, not zero [B6] |
| 2 | `traffic_market` | Roster state per rival (loaded / unmeasured / undated), coverage (loaded of mapped), tracked traffic, **our share of tracked traffic**, freshness spread | Compare exports only when the spread is ≤ 2 days ("comparable"). Totals describe the loaded rivals, not the category [B6] |
| 3 | `traffic_history` | Our traffic and keyword count per snapshot. The same per rival. Contested/won per rival snapshot. Roster joins and leaves | A rival snapshot is compared with our nearest snapshot on or before it. A tie is not a win |
| 4 | `traffic_market_keywords` — first page with `summary=true`, then **every addressable page** (`addressability=addressable`, `limit=200`, `summary=false`) until exhausted | Per keyword: consensus (rivals present), tracked traffic and ad traffic, ours, state (contested / ours_only / theirs_only), leader, addressability, segment, relevancy, weekly SV, opportunity (`we_run_none` / `they_are_more_aggressive`), ad gap, `rivalMetrics` per rival (traffic, ad traffic, organic rank, SP rank, placements). Summary blocks: scoreboard, segment gap, segment × tier grid, placement reach, PPC opportunities, byConsensus | Pull **all** addressable rows, not the top page. The biggest market pages are generic terms. Basis defaults to market average (avg); state the basis you used. 7-day traffic is impression-like: **not clicks, not sales** |
| 5 | `traffic_competitor` per loaded rival (comparison rows; `state=theirs_only` pages) | Rival totals, organic % / paid %, top-10 keyword share, top keyword. Segments (owned / matched-no-owner / unclassified). Relevancy mix. Placement reach per code. **Hero ASINs** (the fewest child ASINs carrying 80% of its traffic). Contested (we win / we lose / our zero-traffic), ours-only, theirs-only (keywords, their traffic), PPC openings, our share. Also **our** hero ASINs | Theirs-only rows page at 100. Page through them, or state that you sampled |
| 6 | `traffic_position_trends` (rival hero ASINs + `our_asins`) | Daily placement **scores** per child: organic, SP, SB, SB video, summary organic, summary advertising | **Scores, not traffic.** Never add them to 7-day traffic. The feed was retired and the series ends at a fixed date. The response states the newest day, so quote it. ASINs with no rows are listed as missing; say which |
| 7 | `traffic_addressability` | Addressable / disqualified / unknown keywords with traffic. Disqualified split by reason (disqualifier term, other brand, size not sold, fit tag). Share nothing classifies. Conflicts (a disqualifier and a fit tag disagree) | Review the conflict rows by hand before you use them in a gap list |
| 8 | `traffic_our_keywords` | Our export: 7-day traffic, organic/ad split, organic and SP rank and page, SV, SFR, top-3 click/conversion share, variations reached | Our ranks here are one week. Rank history comes from the rank source (ref 05) |
| 9 | Data Dive: `list_niches` → `get_niche_competitors` per niche (`create_niche_dive` / `create_niche_dive_from_competitors_list` if missing — these spend tokens, so confirm first). Optional: `get_niche_keywords`, `get_niche_roots`, `get_ranking_juice` | Per listing: price, est. units/30 d, est. revenue/30 d, BSR, rating, reviews, listing date, variations, page-1 keyword coverage (count and % of niche SV), advertised keywords, top-of-search keywords and SV, fulfilment, seller country. Per niche: keyword count, SV, median price / reviews / units, launch keywords | **Pull several niches:** (a) the broad size or category niche, all materials — this shows who owns the generic field and at what price; (b) the material / type niche for our product; (c) a size-specific material niche. Units and revenue are **estimates**. Ad detection sees only some sellers, so "0 advertised keywords" ≠ no ads |
| 10 | Command Center product brief — competitors section | Per mapped brand (all mapped, measured or not): price first → latest (Δ%), BSR first → latest, review count and Δ, **reviews/week**, discount now (depth %). Summary: on discount now, price cutters, price raisers | About 32 days and 6 weekly snapshots. Only strike-through discounts are seen: **coupons and lightning deals are not scraped** |
| 11 | AdInsight per-ASIN files `AdInsight_US_<ASIN>_<start>to<end>.xlsx` (when supplied) | Daily ad traffic score (cumulative on the latest row). Ad keyword count (daily, change rate, Total on the latest row). Ad position traffic ratio and keyword count per ad type (SP / SB / SBV / HR / TRB / CPF / SOR). Top 10 keywords per ad type (rank, keyword, 7-day traffic, ratio, SFR, weekly SV) | Visible keywords ≤ 70 per ASIN (10 × 7 types). "Ad Keyword Count (Total)" is account scale; never report it as the list you can see. `(None…)` sheets mean the ad type is not run. **Files carry no brand**, so resolve it (1.3) [LP] |
| 12 | Helium10 Cerebro (own + multi-ASIN competitor pull) | Keyword × ASIN organic/sponsored ranks, SV. Used for the coverage audit: each relevant term ≥ the volume threshold → **LIVE / PAUSED / MISSING**. Priority list = MISSING terms with **3+ competitors in the top 30** [LTSF] | Cerebro suggested bid / CPC is **never** used to set prices (owner rule, register #18). Cross-check the search-term report before you call a gap: exact-text matching overstates gaps [LTSF] |

When a product has conquest or PAT campaigns, dated competitor pulls (ASINsight / Helium10 / Cerebro) are a **required input** [PB, WB].

### 1.2 Coverage rule (applies to every competitor number)

1. **Profile all mapped competitors** that carry an export, not a sample. Profile the unmeasured ones from the brief and Data Dive.
2. **Unmeasured ≠ zero.** Draw no conclusion about a rival with no export. Report "unmeasured".
3. **State coverage on every share or contest figure**: "13 of 32 mapped competitors measured; figures describe those 13" [B6, R-CI12].
4. **Map the missing big sellers.** List every listing in the Data Dive niches that has high est. units or a low BSR and is **not mapped** (or mapped but unmeasured). Request mapping and an export for each, Beatable ones first. Example (B6): four unmapped sellers, one at BSR 456–691 and ~24k units/month.
5. Set a coverage target for the next audit. Example (B6): ≥ 20 of 32 measured.
6. Count **brands, not ASINs**. Two ASINs of one brand are one competitor in any "N rivals do X" count [LP].
7. Keep no padded competitor sets. A rival has to share our intent, material and category to count [LTSF].

### 1.3 Brand resolution (bare ASINs are rejected) [LP]

Resolve every ASIN to a brand before you present anything. Try in order: `"<ASIN>" amazon` → `site:amazon.com <ASIN>` → add the category words → aggregators (Ubuy, Walmart cross-listings, camelcamelcamel, roundup posts). Use the brand as the primary label and put the ASIN beside it. If a brand stays unresolved, list it as "unresolved". It cannot be scaled as a conquest target (R-X6).

### 1.4 AdInsight reads (per ASIN) [LP]

| Read | Formula / signal | Meaning |
|---|---|---|
| Traffic per keyword | latest ad traffic score ÷ latest Ad Keyword Count (Total) | High = tight, well-converting set. Low = long-tail spray |
| 7-day trend | latest score − earliest score | Call out sharp moves either way |
| Infrastructure mismatch | large keyword count, most ad types active, score ≈ 0 | Recent pull-back. Watch for re-entry; don't dismiss them as small |
| True dormancy | 0 score, 0 keywords, no ad types | Say it plainly |
| Isolated ad type | SBV or HR alone, no SP | Test or awareness play, not a push |

---

## 2. Roster, tiers, scoreboard, traffic trend

### 2.1 Tiers (mapping tier, set in Command Center)

| Tier | How the scoreboard treats it | How this skill uses it |
|---|---|---|
| **Aspirational** | Not beaten → severity *none* (no failure) | Leaders. A target rank held only by Aspirational rivals is a **stretch** (R-CI2). Their pages are usually AVOID or TEST |
| **Beatable** | Not beaten → severity **failure** | The rivals to pass. They set the first milestones and the winnable ground (R-CI3) |
| **Poor** | Beaten → *ok* | They should sit below us. If a Poor rival is ahead, that is a finding |

The tier is a mapping input. No source defines how to assign it. If a rival is untiered, or the evidence contradicts its tier (e.g. a "Poor" rival ahead of us on traffic and contests), raise it with the owner. Never retier silently.

### 2.2 Scoreboard reads (per rival)

| Field | Definition | Read |
|---|---|---|
| Traffic verdict | our 7-day traffic vs theirs | ahead / behind |
| Contest verdict | our wins on the keywords we both hold | ahead when we win most contested keywords (as observed: contest rate > 50%) |
| **Call** | beaten (both ahead) · not_beaten (both behind) · mixed (split) · unmeasured | Headline per rival |
| Severity | failure = Beatable/Poor not beaten · watch = mixed · ok = beaten · none = Aspirational not beaten | Count failures by tier |
| **Contest rate** | contest wins ÷ contested keywords (a tie is not a win) | Share of shared ground we win |
| **Distance** | their traffic ÷ our traffic | > 1 = they are bigger. Example (B6): Aspirational leader 15.0×; a Beatable 3-piece set 1.01× (level) |

The per-segment × tier grid gives the same call per segment. The worst call per segment is the one to act on, and the "push gap" is the Beatable traffic we don't have.

### 2.3 Traffic trend: season or share loss?

1. **Our trend**: our 7-day traffic across all snapshots (`traffic_history`). State the first → last and the Δ%.
2. **Rival trend**: each rival's previous export → latest export, as Δ%.
3. **Hero placement scores**: compare the average of the first 7 days with the average of the last 7 days, for organic and advertising. Report the change only when the first-week score is ≥ 50 (below that it is noise) [B6]. For rivals, sum their top 3 heroes. For us, sum our heroes.
4. **Verdict:**
   - If most rivals fell by a similar amount, the fall is **season**.
   - If our fall is larger than the median rival fall, the gap is **share loss**. Name the child ASIN and the placement (organic vs ad) that lost it.
   - If one rival rose while the field fell, it is a **mover**. Profile it and check the terms where it sits (5.6).
5. Split the read before and during events (deal run-ups lift everyone).

Example (B6): our traffic fell 37% over 7 weeks. Every measured rival but one also fell 7–24% between exports, but our four heroes' organic score fell by more than the rival median. King White (the ranking colour) lost the most, so the verdict was part season and part share loss on the hero.

---

## 3. Per-rival profile checklist

Fill every field for every measured rival. Unmeasured rivals get the fields that the brief and Data Dive can fill. A blank field is written as blank with a reason, never 0.

| # | Field | Source | How |
|---|---|---|---|
| 1 | Brand, parent ASIN, product name, tier, call | roster, scoreboard | brand-resolved |
| 2 | ASINs carrying traffic; **variation structure** (variation count, sizes, colours, packs) | hero list, Data Dive `variations` | |
| 3 | **Hero ASINs** with share of the rival's traffic and the keywords each leads | `traffic_competitor` heroAsins (80% coverage) | top 4 |
| 4 | **Pieces / bundle** (pack size, what's included) | listing title (Data Dive) | parse the piece count and flag "no flat sheet"-type omissions |
| 5 | **Price range** (min–max across listings read) and **price movement** | Data Dive, brief | first → latest (Δ%) |
| 6 | **Discount now** (depth %) | brief | strike-through only |
| 7 | **Units / revenue** (est. 30 d, best-selling listing) and **velocity** | Data Dive | label as estimate; best listing, not the whole brand |
| 8 | **BSR** (lead listing) and **BSR movement** | Data Dive reads on different dates; brief | "12,485 (28 Sep) → 10,390 (29 Sep)" style, dated |
| 9 | **Rating, reviews, review velocity** + method + source | brief (reviews/week over its window) where the brand is a mover. Otherwise two Data Dive reads of the same listing: (latest − first) ÷ days × 7. For a parent family with a shared count, use it only when the two counts differ by ≤ 3% of the base [B6] | name the source. A falling count is a finding (review loss) |
| 10 | **Keyword count and coverage** | export totals; Data Dive page-1 keywords (count, % of niche SV) | |
| 11 | **Organic % vs paid %**, top-10 keywords' share, top keyword (% of their traffic) | `traffic_competitor` totals | |
| 12 | **Top keywords** (their top 8 addressable, with their rank and ours) | `rivalMetrics` join | 5.1 |
| 13 | **Placement behaviour**: keywords with OR / SP / SB / SBV / AC / SOR | placement reach; Data Dive advertised and top-of-search keywords | → PPC behaviour label (3.1) |
| 14 | **Contest vs us**: contested, we win, we lose, our traffic ÷ theirs | comparison | |
| 15 | **Their-only keywords** (count, their traffic, share of theirs) | comparison | |
| 16 | Traffic change export → export; hero organic/ad score change | history, trends | |
| 17 | **Strengths / weaknesses** | rules 3.2 | |
| 18 | **Conquest archetype** (Fortress / Investor / Price Leader / Copier / Fader) | 7.5 | |
| 19 | **What it means for us** (3.3) | synthesis | one paragraph |

### 3.1 PPC behaviour label [B6]

Apply every tag that fires (kw = the rival's keyword count):

| Test | Tag |
|---|---|
| paid % ≥ 60% | ad-led |
| paid % ≤ 20% | organic-led, light ads |
| (SB + SBV keywords) ÷ kw > 0.3 | heavy Sponsored Brands + video (brand funnel) |
| else SBV ÷ kw > 0.3 | video-heavy |
| SP ÷ kw > 0.5 | SP on most keywords |
| SOR ÷ kw > 0.4 | strong product-page ads |
| none | mixed |

Add the AdInsight reads (1.4) when those files exist.

### 3.2 Strength / weakness rules [B6 values; rescale per category with the owner]

| Strength if | Weakness if |
|---|---|
| reviews > 10,000 | reviews < 1,000 |
| organic > 60% of traffic | paid > 60% of traffic (share falls when spend stops) |
| SB + SBV keywords > 1,000 | keyword count < 1,500 (narrow) |
| keyword count > 4,000 | price > our same-size price + $15 for fewer pieces |
| traffic Δ > +30% since previous export | traffic Δ < −15% |
| price < our price − $5 | rating ≤ 4.3 |
| variations > 150 | review count falling |
| rating ≥ 4.5 | fewer pieces than ours (e.g. 3-piece, missing component) |
| hero organic score > +25% | hero organic score < −25% |

Always compare against **our same-size, same-variation** listing (the advertised hero), never a blended parent.

### 3.3 "What it means for us" — write every paragraph to this pattern

1. The price and value position vs us: price, pieces, value per piece, reviews, rating.
2. Where they beat us: which terms, and at what rank.
3. Do they bound any of our targets? Say whether they make a target a stretch or show that it is reachable.
4. Their pages: OFFENSIVE / TEST / AVOID (section 7), and why.
5. What to watch: a price move, a discount, a traffic surge, an ad pull-back.

Example (B6): "Fastest-growing rival (+123% traffic): new 4-piece at our price with a tenth of our reviews, now #6–#11 on King terms. OFFENSIVE target; passing it is the first milestone on King terms."

---

## 4. Market view

Report each block with its coverage and its date.

| Block | Contents | Source |
|---|---|---|
| Tracked market | keywords, 7-day traffic, our traffic, **our share of tracked** | `traffic_market` totals |
| Addressable | keywords, traffic, our traffic, our share | addressability |
| Disqualified | keywords, traffic, split by reason (disqualifier term / other brand / size not sold / fit tag) | addressability |
| Unknown | keywords, traffic, % of traffic nothing classifies | addressability |
| **Contested** | keywords, market traffic, ours, we win / we lose, keywords where we have zero traffic | `contested` |
| **Theirs only** | keywords, traffic, share of tracked | `theirsOnly` |
| **Ours only** | keywords, our traffic | `oursOnly` |
| By consensus | keywords and traffic by the number of rivals present; where we are absent | `byConsensus` |
| PPC opportunities | `we_run_none` and `they_are_more_aggressive`: keywords, ad gap, all vs addressable | `ppcOpportunities` |
| **By kind (addressable only)** | per kind (5.2): keywords, traffic, ours, our share; "they advertise, we don't" (kw / traffic); "they out-advertise us" (kw / traffic) | keyword join |
| **Segment gaps + tier grid** | per segment: keywords, traffic, paid share, our traffic / share, keywords we are absent from, wins vs Beatable (of contested), wins vs Aspirational, worst call | `segmentGap`, `segmentTierGrid` |
| **Placement reach comparison** | us and each rival: keywords with OR / SP / SB / SBV / AC / SOR + behaviour label | `placementReach` + profiles |
| **Price ladder** | every relevant listing across the niches (latest read per ASIN): brand, ASIN, price, pieces, **$ per piece**, est. units, est. revenue, BSR, rating, reviews, variations, listed date, page-1 keywords, read date; sorted by price | Data Dive |
| **Niche benchmarks** | per niche: keywords, SV, median price, median reviews, median units, launch keywords, date | Data Dive |
| Offer vs field | our price, pieces, reviews, rating vs niche medians and vs each tier | derived |

**Offer checks carried into refs 06 and 09.**
- Price position among the tracked competitors is a **required standing input** before a CVR gap can be called PPC-fixable. Price and offer gaps go to Brand Management [PB].
- WB's cold-term parity reference for a new ranking term: reviews ≥ 50% of the top-5 median, rating within 0.3★, price ≤ 1.25× median [WB]. Report it; the push gates themselves live in ref 06.

**Where we win / where they win / where no one is strong.** End Phase 3 with three lists: kinds and segments where we lead; where Aspirational or Beatable rivals lead, with the size of the gap; and where the paid share is low and no tracked rival ranks in the top 10 (open ground).

Example (B6): "13 of 32 measured. We hold 2.1% of tracked traffic, and on 1,899 contested keywords we win 11 and lose 1,660. On core-material terms we advertise on almost all of them, so the gap there is ad intensity, not coverage. Cooling wording is the uncovered segment. Generic head terms are led by $15–50 microfiber sets."

---

## 5. Keyword landscape join

Join every market keyword (all addressable pages) with our keyword decisions (ref 05/06), the live owners (bulk / campaign targets) and the search-term report.

### 5.1 Field metrics per keyword

| Column | Definition |
|---|---|
| Kind, size | 5.2. Size by token (Cal King before King; Full = double) |
| Segment, relevancy, addressable | from the market pull |
| Weekly SV, market traffic, market paid share, rivals present (of N measured), traffic leader | market pull |
| **Best rival organic** | lowest organic rank among rivals, with its name and tier |
| **Best rival SP** | lowest SP rank, with its name |
| **Beatable rivals in organic top 10** | names and ranks |
| Aspirational in top 5 | names and ranks |
| **Rivals advertising** | rivals with an SP rank; separately, how many sit at SP #1–5 |
| **Rivals with brand banners** | rivals with SB or SBV among their placements |
| Top-3 rivals by traffic | names, traffic |
| **Our position** | our traffic, share, organic rank, SP rank, placements, paid share |
| Opportunity, ad gap | market pull |
| Our decision and evidence | decision, clicks / orders / ACoS 30 d, TOS CVR, owner campaign(s) — or "no search-term row" |
| Position class, landscape verdict, why, notes | 5.3, 6 |

Notes to add: "N rivals run SB/video on it — a banner sits above our top-of-search slot" when ≥ 3 rivals have banners; "rivals out-advertise us (their ad share X%, ours Y%)" when the opportunity is `they_are_more_aggressive` [B6].

### 5.2 Kinds (classify by tokens, first match wins) [B6, generalised]

| Kind | Definition | Example (B6) |
|---|---|---|
| Brand (own) | contains our brand | "decolure bamboo sheets" |
| Core | contains the product's defining material or type | bamboo / viscose / rayon |
| Benefit | the listing's main benefit wording, without the core word | cooling, hot sleepers, night sweats, breathable, moisture wicking |
| Pack match | our pack configuration | "6 piece", "six piece" |
| Generic — attribute | attributes that don't define our product | silk, satin, luxury, hotel, soft, deep pocket, organic |
| Generic | category head terms | "bed sheets", "king sheets" |

Competitor-brand, language, colour and other-product classes come from ref 05. Competitor-brand terms are evaluate-only (trademark risk) unless a conquest keyword already runs on that brand, in which case it is a "confirmed live tactic" [LP]. Spanish and other-language terms are usually uncontested, so read low volume as low volume, not as irrelevance [LP].

### 5.3 Position classes (first match wins) [B6]

| Class | Test |
|---|---|
| **Absent — they own it** | we have no traffic and no organic rank |
| **We lead** | our organic ≤ the best rival's organic (or no rival ranks organically) |
| **Direct fight** | our organic ≤ 20, or our SP ≤ 5 |
| **Within reach** | our organic ≤ 60 and ≥ 1 Beatable rival in the organic top 10 |
| **Within reach — Aspirational-led** | our organic ≤ 60, no Beatable rival in the top 10 |
| **Competitor advantage** | everything else |

### 5.4 High-value keywords

Revenue per keyword is **not available** from any connected source. Use the proxy **market traffic × weekly SV** to rank keywords within a kind, and label it as a proxy. Sort landscape tables by market traffic.

### 5.5 Data artifacts [LP]

A term with a weekly SV that is implausible for its SFR, or an identical, oddly specific SV repeated across several rivals' files, is a scrape artifact. Flag it, ask for it to be verified in the source tool, and **exclude it from totals**.

### 5.6 Rising-rival exposure (proxy)

Keyword-level history does not exist (each export is one week). Instead:
1. Take the rivals that are rising: traffic Δ > +50% (R-CI11), hero ad or organic score > +25%, or a mover in the brief.
2. List the core and benefit keywords where such a rival sits in the organic top 10 or the SP top 3 **and ranks ahead of us**.
3. Sort by market traffic.
4. Label the list "rival-level movement × current rank, not keyword history" [B6].

---

## 6. Engine-vs-landscape verdicts

Give every keyword decision that appears in the market pull a landscape verdict, and give every addressable keyword without one a gap verdict. The verdict **changes ordering, judging and gap-filling — never a price** (R-CI4).

### 6.1 Terms we have a decision on

| Decision | Test (in order) | Verdict |
|---|---|---|
| PUSH / WAIT / HOLD RANK | our organic ≤ best rival organic | **AGREES — we lead the tracked field** (the push is against untracked sellers; cap it to the stock plan) |
| | a rival sits at or above the target rank, and at least one of them is not Aspirational | **AGREES — reachable** (proof that a listing like ours can hold the target; name the rivals to pass first) |
| | every rival at or above the target is Aspirational | **AGREES — stretch target** (judge progress on the Beatable rivals passed, R-CI2) |
| | Beatable rivals hold the ranks between us and the target | **AGREES** — winnable ground (fund first, R-CI3) |
| | otherwise | AGREES (state the field) |
| DEFEND | rivals advertise on our brand term | **AGREES — defence needed** (state the rival count, the market ad share and our organic rank) |
| REDUCE | the term sells (≥ 10 orders in 90 d) and rivals buy it | **AGREES — keep live at break-even** (the cut is a price cut to break-even, never a block — R-CI9) |
| BLOCK / REDUCE | addressable, market traffic ≥ 10,000, ≥ 5 rivals advertise | **CHALLENGE — re-test later**: the cut stands (the money rule wins on the day), tagged re-test (R-CI9) |
| BLOCK / REDUCE | otherwise | AGREES (thin or low-value field) |
| MONITOR | addressable, market traffic ≥ 20,000, core or benefit kind | **CHALLENGE — under-funded**: give it an exact owner in discovery at break-even, no push premium, so it can be read |
| MONITOR | generic kind | AGREES (the field is priced for another product tier) |
| CHECK OWNER / DEDUPLICATE | — | **AGREES — fix owner first** (one live owner before any push) |
| HARVEST | — | AGREES (a real market term; give it an exact owner) |

### 6.2 Addressable terms with no search-term row (the engine is blind to them)

| Test (in order) | Verdict |
|---|---|
| not addressable | **Out of scope** |
| core kind, market traffic ≥ 3,000 | **GAP — engine blind**: seed an exact owner at break-even (R-CI8) |
| generic kind | **GAP — leave**: discovery only |
| benefit or pack kind, market traffic ≥ 3,000 | **GAP — engine blind** |
| generic-attribute kind, relevancy Highly Relevant / Relevant, market traffic ≥ 5,000 | **GAP — test**: discovery at break-even before any owner |
| generic-attribute kind, otherwise | **GAP — leave** |
| any kind, market traffic ≥ 5,000 | **GAP — engine blind** |
| otherwise | GAP — small: leave to auto/broad discovery |

Traffic thresholds are [B6] (ASINsight 7-day units).

### 6.3 First milestone (every push, waiting and at-target term)

- **First milestone** = the closest Beatable or Poor rival ranked **ahead of us** organically (the rival with the highest rank number still below ours).
- If only Aspirational rivals are ahead, write "none — only Aspirational rivals ahead".
- If no tracked rival is ahead, write "we lead the tracked field".
- Report progress at 7 and 14 days as **rivals passed**, alongside the distance to the target. A slow climb past Beatable rivals is not a failure at day 7 (R-CI2, R-CI5).
- If winnable-ground terms don't move in 7 days at the push price, the cause is ours (listing, colour, conversion), not the field.

Example (B6): on "bamboo sheets" the target #9 was held only by two Aspirational rivals, so the term was a stretch, and the first milestone was the Beatable rival sitting just above our #30. On King terms, a Beatable rival launched within the year already held #6–7, so those targets were reachable.

### 6.4 Summary outputs

- Pivot of decision × verdict, with counts.
- The share of our terms that appear in the market pull, and why the rest don't (ASIN targets, misspellings, colour terms, terms too small).
- Campaign-level checks, one row per campaign family:

| Campaign family | Checks |
|---|---|
| Ranking | fields, banners, stretch vs winnable |
| Waiting (ceiling below cost) | "keep the block; the owner decides a ceiling raise" |
| Brand DEFEND | rivals on our brand; add own-ASIN defence |
| Discovery | missing benefit and engine-blind terms |
| Conquest PAT | how much spend sits on AVOID vs OFFENSIVE pages; own ASINs mixed in |
| SB / video | presence vs rivals |
| Generic MONITOR | whether the field supports leaving it there |

---

## 7. Competitor ASIN targeting

### 7.1 Candidate set

Include every rival hero ASIN, every relevant-material listing in the Data Dive niches, the extra ASINs read, and every ASIN already targeted in our campaigns. Classify each candidate first [B6 R-X1/X2]:

| Class | Treatment |
|---|---|
| Own product (this family) | defence (DEFEND, low bid, judged ACoS ≤ break-even). Never conquest |
| Own brand, other product | cross-sell, judged on its own ACoS. Report it apart from conquest |
| Competitor, same material | 7.2 |
| Competitor, other material | 7.2 (usually AVOID) |
| Unmapped (brand unknown) | no SCALE until mapped (R-X6) |

### 7.2 Class tests (first match wins) [B6]

Compare against **our same-size advertised listing** (size read from the target's title; default = our main size): our price P, our rating R, our reviews N.

| # | Test | Class |
|---|---|---|
| 1 | est. units on that listing < **500/month** | **LOW TRAFFIC — skip** (too few shoppers on the page) |
| 2 | different material (e.g. microfiber / cotton / satin with no core-material word) | **AVOID — different material** |
| 3 | no price available (even after the family fallback, 7.3) | **TEST — no price read** |
| 4 | (price < 0.85 × P **and** reviews > N) **or** (price < P **and** reviews > 5 × N) | **AVOID — cheaper and better reviewed** |
| 5 | price < 0.70 × P | **AVOID — price gap too wide** |
| 6 | price ≥ 1.10 × P **and** rating ≤ R + 0.1 | **OFFENSIVE — we are cheaper** (state pieces: "for 6 pieces vs their 4") |
| 7 | reviews < 0.5 × N **and** price ≥ 0.90 × P | **OFFENSIVE — more reviews at the same price** |
| 8 | otherwise | **TEST — close match** |

Pieces and value per piece are stated in the "why" of every class. No source weights pieces inside the tests beyond R-CI7's wording ("above us on price for fewer pieces"). If pieces should change a class, that is an owner decision; record it.

### 7.3 Family-price fallback

If the listing has no price read, use the rival family's lowest price, its rating and its largest review count, and append "(family price/reviews)" to the why [B6].

### 7.4 Actions by class (targets that already exist keep their money rules)

| Class | Not targeted | Already targeted |
|---|---|---|
| OFFENSIVE | add to the conquest campaign at break-even | keep; judge by R-X3–X5 |
| TEST | optional test after the OFFENSIVE set | keep; judge after 15 clicks |
| AVOID | don't target; negate if auto/PAT finds it | ≥ 3 orders: **hold at break-even while it sells, never scale**. Otherwise remove / negate |
| LOW TRAFFIC | leave | keep only if it sells; judge after 15 clicks |

**Money on an existing target is decided by R-X3–X5 on its own 90-day clicks and orders, summed across every campaign that targets it** [B6]. The class never cuts a profitable target.

| Rule | Test | Action |
|---|---|---|
| R-X3 | mapped competitor, ≥ 15 clicks, ACoS ≤ break-even | SCALE: bid up ≤ +25% per cycle (register #5; B6 used ≤ 30% a step), never above the break-even CPC |
| R-X4 | ACoS > break-even on ≥ 15 clicks | REDUCE toward break-even (gradual cut ≤ 15%/cycle; a decisive cut ≤ 50%) |
| R-X5 | ≥ 20 clicks, 0 orders; or ACoS > 2 × break-even on ≥ 30 clicks | BLOCK (pause the target / negative ASIN) |
| R-X6 | same ASIN in > 1 campaign, or brand not mapped | one owner; no SCALE until mapped |

Product targets use the 11-click floor for a verdict (SKILL sample floors) and 15 clicks for R-X3/X4.

Example (B6): a microfiber page at $24.99 sat at 21% ACoS in one campaign. It is AVOID by class, yet kept at break-even and not scaled. Most conquest spend sat on AVOID pages while no OFFENSIVE page was targeted, so the campaign-level check was **CHALLENGE — shift new conquest to OFFENSIVE ASINs**.

### 7.5 Conquest entry, ceiling and exit [PB, provisional — confirm with the owner before it first drives a decision]

1. **Already targeted?** Search the account for the ASIN in any conquest campaign first. If it is there, decide from its state and performance (reactivate / adjust / leave). Only new targets go through the gate.
2. **Entry gate**: our routed SKU wins **≥ 2 of 3** (price, rating, review count) against the target, **or** the target is out of stock. Write it plainly: "we win on price and reviews, lose on rating — two of three." If data is missing, ask before logging a wait. Default here: a **new** target needs OFFENSIVE **and** 2-of-3. An OFFENSIVE ASIN that fails 2-of-3 is run as TEST (register #44).
3. **Ceiling (watch-CPA)** = the lower of: (a) routed SKU margin × CVR, i.e. the break-even CPC; (b) a price-gap-adjusted figure. State which governs. No source sizes the adjustment, so decide and record it. Either way it never goes above the break-even CPC (non-ranking ceiling, register #3).
4. **AOV** = the routed SKU's AOV, never the competitor's price.
5. **Share of target page** = impression or click share on that detail page from PT placement data. Never infer it from account ratios.
6. **Exit / rotate**: the target is delisted (drop it); it no longer loses 2-of-3 to us (hold); or CPA > watch-CPA for **2 consecutive reads** (2 validated weeks, SR) with no page-share gain (exit). Flag CPC > 1.5 × the family median.
7. **Archetypes** change watch-CPA, duration and review cadence, never entry:

| Archetype | Signal | Play |
|---|---|---|
| Fortress | deep review / IP moat | long, expensive game; size accordingly |
| Investor | spends heavily to buy position (ad-led) | spend-war risk; watch for them to stop funding |
| Price Leader | position is price | compete on relevance and proof, not price |
| Copier | newer entrant mimicking an established listing | often the easiest, time-limited win |
| Fader | reviews, rating or rank velocity declining | take it now |

8. **Rank-loss check (ranking state E)**: if a push term lost > 10 places while getting clicks, work through the causes in order. Own listing first (price, stock, reviews, content, coupon or deal end). Then competitor: a rival that wins ≥ 2 of 3 on price, rating and reviews, or a rival stock-out → name it and route to conquest/PAT. Then isolated vs category-wide. Never answer with a bid change [PB].

---

## 8. Competitor → engine influence rules R-CI1–R-CI12

Status: **Standing** = always applies · **Default** = applies unless the owner rules otherwise (B6 proposed it; confirm per product) · **Owner decision** = needs explicit approval per product.

| Rule | Area | Competitor signal | IF → THEN | Never changes | Example (B6) | Status |
|---|---|---|---|---|---|---|
| R-CI1 | Keyword selection | addressability, rivals present, organic field by tier | A term is a push candidate only if it is **addressable**, ranked on by **a majority of measured rivals** (B6: ≥ 7 of 13), and is core or benefit wording. | Generic terms never enter the push, whatever their volume | "bed sheets" (155k traffic) stays MONITOR; "bamboo sheets" qualifies | Default |
| R-CI2 | Ranking strategy | organic ranks of tracked rivals, by tier | If only Aspirational rivals sit at or above the target, the target is a **stretch**. Judge progress on rivals passed (first milestone). After **14 days at the ceiling with no rival passed**, take it to the owner. | Price rules; no automatic ceiling raise | "bamboo sheets" target #9 held only by 2 Aspirational rivals | Default |
| R-CI3 | Push order | Beatable rivals between us and the target | When plan budget exceeds room, fund **winnable-ground** terms first and stretch terms second. | Total push budget; scale factor | King and Full core terms before the Queen head term | Default |
| R-CI4 | Bids | — | Competitor data never sets a bid or price. Push price = break-even × (1 + premium), capped at 2 × break-even. | No competitor CPC, no suggested bid, no "market price" | — | Standing |
| R-CI5 | Read windows | rivals with brand banners; rivals at SP #1–5 | On push terms with **≥ 5 rivals at SP #1–5**, judge rank after **7 days** (not 3). Top-of-search impression share alone is not a pass/fail signal. | The +30%/day step and the ceiling still apply daily | all 13 funded terms had 5–9 banners | Default |
| R-CI6 | Defence | rivals advertising on our brand terms; our organic rank there | Brand terms with **≥ 3 rivals advertising** → DEFEND at top of search, funded first, plus own-ASIN product targeting. | Brand campaigns are judged at break-even like any other (defensive allowance per ref 06, only with verified rival presence) | "decolure bamboo sheets": 10 rivals, our organic #9 | Default |
| R-CI7 | Offence | price, pieces, rating, reviews vs our same-size set | Target **OFFENSIVE** ASINs only (above us on price for fewer pieces, or the same price with < 50% of our reviews). Negate **AVOID** ASINs in auto/PAT. | Each ASIN is judged by R-X3–X5 after 15 clicks | 4 rival heroes OFFENSIVE; 3 AVOID | Default |
| R-CI8 | Gap seeding | `we_run_none` / no search-term row on addressable core and benefit terms | Addressable core or benefit terms with **≥ 3,000 market traffic** and no search-term row get an **Exact target in the discovery campaign of their size, at break-even**. | No push premium; discovery colour rules; judged by keyword rules after 15 clicks | cooling list; engine-blind core terms | Default |
| R-CI9 | Block review | rivals advertising on a term we BLOCK or REDUCE | A REDUCE on a term that still sells (**≥ 10 orders / 90 d**) and that rivals buy is a price cut to break-even, **never a block**. A BLOCK on an addressable term with **≥ 10,000 market traffic** that **≥ 5 rivals** advertise on stands, tagged "re-test": it goes back into discovery at break-even after **30 days** or after a listing or price change. | The money rule always wins on the day | a set term with 61 orders, 29.8% ACoS, 11 rivals advertising → reduce to break-even | Default |
| R-CI10 | Campaign structure | rivals' Sponsored Brands / video reach | SB / video is outside the automated engine: a hand-built test on core push terms and brand terms, with its **own budget line**, priced by the same break-even rules (section 10). | Not written by the engine; excluded from push budgets; **counted in the product spend limit** | us: SB on 4 keywords vs the leader's 3,791 | Owner decision |
| R-CI11 | Competitor moves | brief movers: price cut > 15%, new discount, traffic growth > 50% | If a rival in a push term's top 10 makes such a move, **hold our price for 3 days** instead of reading a conversion drop as a bid problem; re-check after. | Cuts for money (over ceiling) still apply | a rival at +123% traffic; the leader on 19% discount | Default |
| R-CI12 | Measurement | competitor coverage | Report share, contest and "we win" figures with coverage (loaded of mapped). Draw no conclusion about an unmeasured competitor. | — | 13 of 32 measured; big sellers unmapped | Standing |

### 8.1 Where each rule enters the pipeline

| Pipeline stage (SKILL master order / phase) | Competitor input | Rules |
|---|---|---|
| Keyword classing (Phase 4) | addressability, kind, rivals present | R-CI1, R-CI9 |
| Push qualification (step 9, objective loop) | the gates are unchanged; the field read adds ordering and judging | R-CI2, R-CI3, R-CI5 |
| Price and ceiling (steps 3, 10) | **none** | R-CI4 |
| Budgets (step 10) | funding order only | R-CI3 |
| Discovery / harvest | seed list of engine-blind terms | R-CI8 |
| Product targeting | OFFENSIVE / TEST / AVOID class | R-CI7 (+ R-X1–X6) |
| Brand defence | rivals on our brand terms | R-CI6 |
| Quality gate (step 8) — competitor shock | movers | R-CI11 |
| Landscape check (step 11) | verdicts, section 6 | all |
| Validation (Phase 9) | rivals passed, competitor moves | R-CI2, R-CI5, R-CI11 |
| Reporting | coverage | R-CI12 |

Before calling a cut safe, also check **auction density** (the competitor advertised-keyword count on the term) [PB].

---

## 9. Gap analysis

### 9.1 Gap row template (every gap)

| Field | Content |
|---|---|
| # / Gap | short name |
| **Evidence** | the numbers, with coverage and date |
| **Size** | traffic, keywords, ad gap, or orders at stake |
| **Why it matters** | one or two sentences, in money or rank terms |
| **How to fill inside the guardrails** | the action; every fill keeps break-even, the ceiling, the step caps and the spend limit |
| **Rule** | rule id(s), in the workbook only |
| **Validation** | metric, threshold, read date |

### 9.2 Standard gap families (check every one; write "no gap" with evidence when one is clean)

| Family | Detect | Typical fill | Rule |
|---|---|---|---|
| **Brand defence** | rivals advertising on our brand terms; our organic rank on them; market paid share on brand terms | Brand exacts funded at top of search on the hero (DEFEND). Add an own-ASIN product-targeting defence. Brand negatives in generic discovery only after that is live. If a rival sits above our organic slot on our brand SERP: restore one ladder step, add an SB headline on the brand root (+ SBV if none), PAT self-target the ASINs under attack, and review weekly until the attacker drops [PB]. Never chase branded CPC past the ceiling | R-CI6, R-X1, R-K8, E10 |
| **SB / video lane** | our SB/SBV keyword reach vs rivals; banners on push terms | section 10 test | R-CI10 |
| **Core ad intensity** | `they_are_more_aggressive` on core terms (keywords, traffic, ad gap) | no new rule: the push list is the fill; competitor data orders it (winnable first) | R-P*, R-CI1–3 |
| **Benefit wording** | benefit kind: our share vs traffic; `we_run_none` count | Exact in the discovery campaign of each size at break-even, no premium. Check the listing states the benefit first | R-CI8 |
| **Engine-blind terms** | addressable, ≥ 3,000 traffic, no search-term row | seed list (9.4). If an owner exists but gets no traffic, check it is live and bid at break-even rather than building new | R-CI8 |
| **Protect leads with thin stock** | position "We lead" on terms whose advertised variation is Yellow/Red or short of the next arrival | keep push budgets to the stock plan; reorder; don't hand the ranking campaign to the backup colour | inventory rules (ref 04) |
| **Stretch head terms** | push terms with verdict "stretch" | no price change; report the first milestone; at 14 days at the ceiling with no rival passed → owner: a time-limited ceiling raise or step back to break-even | R-CI2 |
| **Competitor pages** | OFFENSIVE ASINs not targeted; spend on AVOID pages | OFFENSIVE into conquest at break-even; AVOID never targeted | R-CI7, R-X* |
| **Generic terms (deliberately not filled)** | generic kind: traffic, `we_run_none` | Leave to auto/broad discovery at break-even; never push. Exception: pack-match terms we already lead → harvest to exact at ≥ 3 orders with ACoS ≤ break-even and no live exact owner (register #22) | R-CI9, harvest |
| **Visibility loss** | hero organic/ad score Δ vs rival median (2.3) | the push fixes ads; on organic, a listing check on the hero (ref 09) and keep the hero advertised | R-C1, E15 |
| **Rivals moving** | brief movers, traffic surges | apply the 3-day hold; re-check movers every run | R-CI11 |
| **Measurement** | unmeasured and unmapped big sellers | exports for Beatable unmeasured rivals first; map the missing sellers; set a coverage target | R-CI12 |

### 9.3 Size battlegrounds

For core terms, give one row per size (then per segment, if segments differ from sizes): core keywords, market traffic, our traffic, our share, keywords we lead, our average organic rank, the most frequent traffic leader (top 2). Read it against stock per size. Our best position on the thinnest stock is a protect gap, not a push opportunity.

Example (B6): we led every tracked rival on the Full and Twin core terms, while the Full hero had 68 units.

### 9.4 Seed list (engine-blind and GAP — test terms)

One row per term, with these columns:

| Column | Content |
|---|---|
| Term, kind, size | from 5.2 |
| Weekly SV, market traffic, paid share, leader, our organic, opportunity | from the market pull |
| **Proposed owner** | the existing owner campaign if there is one; otherwise "New Exact in the <size> discovery campaign" (size unknown → the product's main size) |
| **How** | Exact, break-even base, no push premium |
| **Advertised variation** | discovery rule: the size's clearance colour, or "as the owner" |
| Verdict | from 6.2 |

- Judge each term with the keyword rules after 15 clicks: CVR ≥ the size rate → exact owner; ≥ 20 clicks and 0 orders → REDUCE (live owner) or REVIEW fix queue (no owner); negate only if the term proves irrelevant or another product type (register #12, #38).
- No builds on deal days (E1).

### 9.5 Campaign-structure read

For each campaign family (ranking, discovery, brand defence, conquest PAT, SB/video) record: today's state → what the competitor data says → the change. Prefer adding terms to existing campaigns over new campaign types.

---

## 10. Sponsored Brands / video test design

Use this when rivals' brand banners sit above the top-of-search slot we buy (≥ 3 rivals with SB/SBV on push terms) and we have little or no SB/SBV reach. The test is an **owner decision** (R-CI10), built by hand.

| Element | Rule |
|---|---|
| Terms | Core push terms with the most rival banners, plus the main brand term(s). **Skip** terms we already lead with thin stock |
| **One format per term** | headline (product collection / store spotlight) **or** video, never both on one term, so each read is clean [B6 F17]. Choose the format the field uses most on that term |
| Match | Exact only; no new negatives |
| Advertised / landing | the size's hero (the ranking colour) or its product page; a collection for the head term; the store for brand terms |
| **Start bid** | break-even of the advertised variation = margin/unit × the size's top-of-search CVR (own CVR per the SKILL conversion basis) |
| Steps | while the banner isn't showing: raise ≤ 30% a day, never above the ceiling. The ceiling is 2 × break-even on push terms, and on brand terms only with verified rival presence (defensive allowance, ref 06). Otherwise 1 × break-even |
| At 15 clicks | switch from the size rate to the campaign's own CVR (blend 15–50, own from 50); break-even and the ceiling move with it |
| Keyword stops | 20 clicks, 0 orders → pause the keyword. ACoS > 2 × break-even on ≥ 30 clicks → back to the break-even bid; pause if it stays there 7 days |
| **Budget** | a **separate budget line**, $/day × test days, counted in the product's total spend limit and excluded from SP push budgets |
| Dates | Never start on deal days. Read before the next deal |
| **Read** (end of the test, 14 days by default [B6]) | ACoS ≤ break-even ACoS (full-price margin) → keep; budget may grow ≤ 30% a step. Between break-even and 2× break-even → keep at the break-even bid. > 2× break-even → stop |
| **Halo check** (same dates) | The SP campaign on the same term: orders and TOS CVR not below the 7 days before the test, and organic rank not worse. If SP orders fall by more than SB adds, the banner is taking our own clicks → stop |
| Report | impressions, CTR, CPC, orders, ACoS, new-to-brand share; for brand terms, the rivals' share of the term in the next ASINsight export |
| Creative | the value position against the field (e.g. pieces vs rivals' sets); logo; no price claim; video 15–30 s showing the product and its main benefit. No video ready → run headline until it is |
| Registration | Register each SB campaign with the SP campaign on the same term as a cross-format pair |

Reference split for the ad-format mix: SP ~80% / SB 15–20% / SD 5–10% [QA, PB]. It is a reference, not a target.

Example (B6): SB-1 was a headline collection on "bamboo sheets". SBV-2 to SBV-4 were video on two size head terms and the cooling term, which had 8 rivals on video. SB-5 was a store spotlight on the brand terms, and SD-6 covered own product pages. Bids started at break-even (King $15.97 × 20.0% = $3.19), with a ceiling of $6.38. The test ran $85/day for 14 days (≈ $1,190) and was read the day before the next deal. The second format on the same term, and the Full term (led by us, 68 units in stock), were not built.

---

## 11. Limits (state them in the report)

| Not available | Consequence / workaround |
|---|---|
| **Review themes** (what buyers praise or complain about) | Not in any connected source. Needs a manual read of reviews or an external review tool; list it as a data gap in ref 09 |
| **Competitor bids, CPCs, CVR, campaign structure** | Not available, and deliberately not used (R-CI4). Placement reach and banners are the only paid-behaviour signals |
| **Keyword-level history** | Each export is one week. Use rival-level trend × current rank (5.6) and label it a proxy |
| Revenue per keyword | Use the proxy traffic × SV (5.4) |
| Sales / clicks from ASINsight | 7-day traffic is impression-like. Never convert it to sales |
| Placement trends | scores only; retired feed with a fixed end date; heroes may be missing |
| Units / revenue | Data Dive estimates, for the best listing only |
| Discounts | strike-through only; coupons and lightning deals are unseen |
| Unmeasured competitors | no keyword data; brief and Data Dive only |

---

## 12. Outputs and checks

**Workbook tabs**: Competitor landscape (findings, sources and limits, market size, trend, reach, segments, niche benchmarks, price ladder) · Competitor profiles (+ each rival's top keywords) · Hero ASINs & trends (+ movers, rising-rival exposure) · Competitive keywords (every pulled keyword, filterable) · Push terms vs field (first milestones) · Gaps & how to fill (+ size battlegrounds, seed list, campaign structure) · Competitor ASIN targets · Competitor → engine (R-CI table + pipeline) · SB & video test (if approved) · Engine vs landscape (pivot, per term, campaign checks).

**Document**: 8–12 numbered findings, each Finding → Why it matters → Action → Expected impact, ordered by money at stake. No tool names or rule ids in the narrative.

**Checks (fail = fix before you present):**
- Every share, contest or "we win" figure states its coverage and date.
- No unmeasured rival is reported as zero.
- Every rival is labelled by brand.
- Every measured rival has a full profile (every blank field has a reason).
- All addressable pages were pulled (the count equals the addressability total).
- Every push, waiting and at-target term has a verdict and a first milestone.
- Every OFFENSIVE / AVOID class shows the price, rating and reviews comparison against the same-size listing.
- Every gap has size, fill and validation.
- No competitor figure changed a price or ceiling.
- Estimates are labelled as estimates.
- Artifacts are excluded from totals.

---

## 13. Open questions for the owner

1. **Conquest entry.** Resolved — see 13 #44: a new target must be OFFENSIVE **and** win ≥ 2 of price / rating / reviews; otherwise TEST. Existing targets are judged on their own clicks and orders (R-X3–X5).
2. **R-X3 step size.** Resolved — see 13 #5: non-push raises (incl. conquest SCALE) are capped at ≤ +25% per cycle.
3. **Absolute thresholds** (500 units, 3,000 / 5,000 / 10,000 / 20,000 traffic, 10,000 reviews, 4,000 keywords, ±$5 / $15 price) are calibrated on one market. Should they scale with market size, and how?
4. **SB/video ceiling.** Resolved — see 13 #45: start at break-even; ceiling 2 × break-even on push terms and on brand terms with verified competitor presence; 1 × elsewhere.


---

<!-- FILE: references/09-listing-positioning.md -->
# FILE: references/09-listing-positioning.md

# 09 — Listing, offer and positioning

Phase 5. Answers the question the PPC numbers raise but cannot settle alone: **is the problem visibility (buy placement), conversion (fix the offer — no rank push), or both?** Output: a quadrant per syntax, a listing and offer comparison against the true competitor set, and a Brand Management findings register with owners. Keyword-level SQP metrics and targets are defined in `05` §8; competitor roster and tiers in `08`.

## Contents
1. Four-quadrant diagnosis per syntax
2. Listing audit — element criteria
3. Competitor comparison per element (1–10)
4. Offer and price positioning
5. Conversion diagnostics
6. Brand Management findings register
7. Review themes — manual read method
8. Open questions for the owner

---

## 1. Four-quadrant diagnosis per syntax

### 1.1 Benchmark and thresholds (resolution #20)
- Unit = syntax (root + modifier, e.g. `Bamboo|Queen`), from `05` §5.
- **Target CTR = Market CTR × 1.10; Target CVR = Market CVR × 1.10** (syntax level, SQP market rates recomputed from the parent roll-up). A metric **fails below 0.9 × target**. [QA, #20]
- Keyword-level CVR bar is **Market CVR × 3.0** (`05` §8.2) — use it for keyword diagnostics, never for the syntax quadrant.
- No SQP → portfolio medians, labelled **provisional** (medians are relative: half the syntaxes fail by construction). [LTSF, #20]
- Read CTR and CVR **at the delivering placement**, not blended. Example: blended CTR 0.626% vs a 1.75% target looked like a listing failure; top-of-search read 2.955% and passed by 1.68×. Show both. [DR]

### 1.2 Quadrants
| CTR | CVR | Diagnosis | Action | Examine | Do not |
|---|---|---|---|---|---|
| pass | pass | **STRONG** | Scale; protect | Nothing | Touch a working listing to solve another syntax's problem |
| fail | pass | **VISIBILITY** | Buy placement (TOS share, modifier — `07`) | Main image vs neighbouring thumbnails, title first 80 characters, price shown in results, badges | Rewrite bullets — shoppers who arrive convert |
| pass | fail | **CONVERSION** | Fix the offer; **no rank push until the fix ships** | Bullets, A+, gallery positions 2–7, price position, rating and review count vs the set | Main-image work (the click already happens); more traffic |
| fail | fail | **BOTH FAILING** | Reduce and reallocate; fix listing first | Whole offer — first check the syntax is genuinely relevant | Polish presentation on a term we should decline |

[LTSF, QA, PB]

- **Syntax sets the mode, never a keyword's bid.** [PB]
- **More traffic cannot fix a conversion problem.** A rank target on a CONVERSION syntax without a funded ranking plan is not a plan. [LTSF]
- Gap keywords on a BOTH-FAILING syntax are held; on CONVERSION launched selectively, bid to CVR (`05` §15). [AP]

### 1.3 CTR root cause (VISIBILITY and BOTH FAILING only)
Needs search-term impression share (IS), TOS impression share and IS rank:

| Reading | Cause | First lever |
|---|---|---|
| IS < 5%, TOS IS < 15%, IS rank > 4 | Placement + auction | Budget-truncation check first, then TOS modifier, then price step within ceiling; base (below the bleeding placement) last (register #7) |
| TOS IS < 15%, IS rank ≤ 4 | Placement only | TOS modifier up (within ceiling) |
| TOS IS 15–30% | Moderate gap | TOS modifier up (within ceiling) |
| TOS IS > 30% | **Listing issue** | Brand Management finding (§6); no CTR bid change |
| No IS and no rank | Undetermined | No CTR bid change; get the data |

[SR] Percentage steps from the source (+15–25%, +20–25%) are bounded by the step caps and ceilings in `07`.

### 1.4 Spend by quadrant, chronic vs transient
- **Report spend by quadrant** — the most actionable single number (how much money sits on CONVERSION and BOTH FAILING syntaxes). [LTSF]
- Also per syntax: keyword count, spend, CTR, CVR, ACoS, rank, quadrant, **weeks in state**, priority class, actual vs target spend share. Dossier only for chronic, off-share or oversight syntaxes; one scan table for the rest. [PB]
- **Chronic = ≥ 4 consecutive weeks in a state; transient = 1–2 weeks.** Chronic CONVERSION → bids frozen at maintenance, no ranking allowance for that syntax, open a listing / price project. [PB]
- Syntax spend shares: primary commonly ≥ ~60%, secondary ≤ ~25% unless a dated test runs above. Off-share = finding. [PB]

---

## 2. Listing audit — element criteria

Standard: every word, image and bullet is intentional and its job can be named. A word that cannot be justified is a candidate for replacement. Enter with the quadrant result; it decides which elements to examine (§1.2). [LTSF]

| Element | Criteria | Evidence to record |
|---|---|---|
| **Title** | First **80 characters** carry the lead syntax + the primary differentiator. **First 3 words** = the highest-volume, highest-intent syntax we rank for | Word-by-word table: word → syntax or claim served → SV / driver share. Flag dead words. High-volume terms we rank on but omit from the title = free relevance |
| **Main image** | Judged against the **top 8 thumbnails** on the head term, at thumbnail size, on mobile — "on a page of 48 results, what makes ours the click?" Name the category convention (bedding: sheen rendering, colour accuracy, set-contents clarity) and whether we follow it | What each rival thumbnail emphasises, what ours does, the specific difference |
| **Gallery 2–7** | One conversion job per position: fit and dimensions · construction close-up · lifestyle for the lead persona · objection kill · social proof · variation range. Secondary-segment imagery from position 4 onward, never the hero slots | Job per position and the objection/driver it addresses; missing jobs |
| **Bullets** | Ordered by decision priority; each answers one named objection or confirms one named driver, in customer language. A bullet mapping to nothing is deleted | Bullet → objection/driver map |
| **A+ / Brand Story** | Narrative, construction story, comparison module against the audited gaps, placements for secondary segments | Modules present, what each does |
| **Video** | Parity is the entry cost wherever category leaders have it. Existing creator/UGC assets unused = finding | Rivals with video; our assets and their use |
| **Backend search terms** | From the category listings report. Coverage gaps close here first, free. A ranking term that is backend-only needs a listing task before funding (`05` §7) | Terms present, gaps vs the coverage list |
| **Variation-range surfaces** | The variation-range image and the A+ comparison table are **routing surfaces** for aged colourways — show them by use case, not as leftovers | Which variations appear where |

[LTSF, PB]

- **Listing-copy defects:** bullets contradicting the title variant (King title, "Queen" / "4-piece" bullets) → flag to be fixed at source. [LP]
- **Range findings:** validated demand across several competitors for a size/attribute we have no SKU for = range gap (product plan, not campaigns). Low-demand variations carrying aged units justify themselves numerically or become retirement candidates — "a narrower range that turns beats a wide range that ages". [LTSF]
- Archetype A (fixable demand, `04`): listing repair runs on a **48-hour SLA** before any deep discount. [LTSF]

---

## 3. Competitor comparison per element (1–10)

- Set: the **top 5–8 true competitors** — same intent, same material, same category. State the inclusion rule and list what was excluded and why; a padded set invalidates the comparison. [LTSF]
- Score **title, main image, secondary images, bullets, A+, video — each 1–10**, with a note on what is emphasised and how. Our listing scored the same way. [LTSF]
- **No weighted listing-quality score exists in any source.** Do not invent weights or sum the scores into one index; report the element scores side by side and let the gaps speak. [13 §4]
- Per competitor also record: **angle and moat** (reason to exist, what protects it) · **traffic and ad strategy** (organic vs paid mix, share of voice on head terms, presence by ad type — SP / SB / SBV / product pages) · **trajectory** (what changed when their performance changed: price move, image refresh, review milestone, stock-out). [LTSF, B6]
- Conclude with a **gap list**, each item classed **Product** (needs specification investment) / **Offer** (positioning, price, messaging) / **Execution** (content quality), plus a **defensibility note**: how fast could the incumbent close it if we exploit it? [LTSF]

---

## 4. Offer and price positioning

Price position among tracked competitors is a **required input before calling a CVR gap fixable by PPC**. Price and offer gaps go to Brand Management, not to bids. [PB]

| Dimension | Read | Thresholds / rules in sources |
|---|---|---|
| **Price ladder** | Every mapped rival's price by size; our rank on the ladder; category median; SQP market price vs brand price (`05` §8) | Cold ranking candidate needs price ≤ ~1.25 × category median [PB] |
| **Value per unit** | Price ÷ pieces (or per unit of the product's natural measure) | Used for offensive ASIN targets: rival above us on price for fewer pieces [B6 R-CI7] |
| **Pieces / bundle** | Set contents vs rivals (e.g. 4-pc vs 6-pc) | Name the comparison unit |
| **Rating** | Star rating vs top-5 | Cold candidate: ≤ ~0.3★ below top-5 [PB] |
| **Review count and velocity** | Count vs top-5 median; reviews gained per month (trend) | Cold candidate: ≥ ~50% of top-5 median count [PB]; offensive ASIN: same price with < 50% of our reviews [B6 R-CI7] |
| **Variation breadth** | Sizes × colours offered vs rivals; missing cells | Range gaps → §6 |
| **Claims** | Material, certifications, benefit claims (cooling, deep pocket…) vs what the listing proves | Claims must match the SKU and be policy-safe |
| **Discounts / coupons** | Rival list vs sale price, coupons, deals running | Rival price cut > 15%, new discount or traffic growth > 50% in a push term's top 10 → hold our price 3 days before reading a CVR drop as a bid problem [B6 R-CI11] |

How to read positioning against the set:
1. Place us per rival tier (Aspirational / Beatable / Poor, `08`) — winning on price against an Aspirational rival means something different from winning against a Poor one. [B6]
2. **Win ≥ 2 of 3 (price, rating, review count)** vs a target → conquest entry is open for a target that is also OFFENSIVE (`08` §7; otherwise TEST — register #44); the same test answers "is a rival's win explaining our rank loss?" State it plainly: "we win on price and reviews, lose on rating — two of three". [PB]
3. Check whether the field is our product at all: a generic field of lower-priced substitutes means our CVR cannot carry our price there — decline, don't push. Example (B6): generic "sheets" terms were led by $15–$50 microfiber sets; a $72 bamboo set could not convert there at break-even. [B6]
4. **State coverage on every competitor claim** ("13 of 32 mapped rivals measured"); unmeasured is unknown, not absent. [B6 R-CI12]
5. **Withdraw overturned findings** into the register with the overturning evidence. Example (B6 source): "2.71× market price, OUTPRICED" was withdrawn after a 74-ASIN pull put the median at $79.99 and ours at 1.00–1.06×. [DR]
6. Competitor price data never sets our bid; prices stay break-even-based. [B6 R-CI4]

---

## 5. Conversion diagnostics

Separate offer, visibility, stock and event causes **before** any bid change.

| Signature | Diagnosis | Route |
|---|---|---|
| **Rank holds, CVR falls** | Offer problem | Listing / price / reviews → Brand Management; no bid increase [LTSF] |
| **Rank falls, CVR steady** | Visibility problem | Placement / delivery (`07`); check competitor moves [LTSF] |
| **Rank collapse concentrated in one size or colour family, coinciding with an outage** | **Stock signature** — not demand, not relevance | Inventory (`04`); do not attribute to the listing [LTSF] |
| CVR drop coinciding with a logged price increase | Price attribution | Hold bids; revert the price, or accept it and recompute break-even, ceilings and targets first [PB] |
| AOV shift from a variation-mix change | Economics changed | Every verdict on the old AOV is void; re-run the rows [PB] |
| CVR ≥ benchmark, rank falling, no own event | Competitive shock | Investigate before any bid: new entrant / deal / price cut; after a named rival move hold our price 3 days (`08` R-CI11); only then one ladder step within ceiling; re-read in 1 week; log [PB, B6] |
| Branded-term CVR collapse | Listing health | Check suppression, buy-box loss, review-score drop, variation break — almost always a listing finding, not a bid problem [PB] |
| Deal days in the window | Distorted | No CVR verdict on deal data; separate deal-state baseline; 2-week guard after the deal [PB, B6 E1] |

**Rank lost > 10 places despite delivery** (rank-drop freeze): no price moves; investigate in order — anchor the timing → own listing first (price, stock-out, reviews, content, coupon/deal ending → Brand Management) → competitor wins ≥ 2 of price / rating / reviews, or competitor went OOS (name it; route to conquest) → isolated vs category-wide (escalate if category-wide) → none found: "investigated, no cause identified" and ask. **Never a bid increase on a collapsing term.** [PB, B6 E4]

Quality gate at the delivering placement (decision order step 8): price, stock-out, rating/reviews, content, deal ending — any of these explains the row → Brand Management finding, no bid. [PB]

---

## 6. Brand Management findings register

Every non-PPC cause found in Phases 3–5 goes here — not into a bid. One row per finding.

| Column | Content |
|---|---|
| # / Category | **Price · Listing · Returns · Range gaps · Inventory / PO · Competitor advantage** |
| Finding | One sentence, with the real figure |
| Evidence | Numbers, source, window, date (quadrant, CVR vs market, rank arc, competitor comparison, SQP ratio) |
| Why it matters | Mechanism: profit, rank, velocity, inventory, share |
| Recommendation | Exact change (e.g. "move 'cooling' into the first 80 characters"; "reorder Full White") |
| Owner | Brand Management / Listing & creative / Supply chain / PPC (for coordination only) |
| PPC decisions gated | Which keyword or campaign decisions wait on it (e.g. WAIT on two push terms) |
| Expected effect | Magnitude-appropriate, labelled measured or estimated |
| Due / re-read date · Status | Open / in progress / shipped / withdrawn (with overturning evidence) |

[PB, LTSF, DR]

What triggers each category:
- **Price** — price above ~1.25 × category median on a ranking candidate; CVR drop after a price change; rivals discounting in a push term's top 10; deal-state margin too thin for the ceiling.
- **Listing** — CONVERSION or BOTH-FAILING syntax; SQP CTR or CVR < market on ≥ 30 clicks (listing flag → push WAIT); TOS IS > 30% with CTR failing; element scores below rivals; copy defects; ranking term backend-only.
- **Returns** — return / defect signal (e.g. a Structurally-dead archetype); branded CVR collapse traced to reviews.
- **Range gaps** — demand without a SKU; low-demand variations holding aged units.
- **Inventory / PO** — projected days of cover leaving Green because of a push (name SKU, date, the push causing it: fix = expedite, PO date, safety stock); stock signature on rank. [PB]
- **Competitor advantage** — a rival wins ≥ 2 of price / rating / reviews on our head terms; rival video/SB presence where we have none; rivals conquesting our brand terms.

Order the register by expected effect, not ease; mark **zero-cost items** (backend terms, variation ordering, A+ module changes) to execute now regardless of what else is agreed. [LTSF]

Example (B6): "bamboo sheets king size" and "bamboo sheets king" were held at WAIT — SQP showed conversion 0.68× / 0.81× and click-through 0.55× / 0.42× the market; the listing check on King White was logged as a Brand Management item gating both pushes.

---

## 7. Review themes — manual read method

Review themes are **not in any connected data source**. Either read them manually or use an external review tool; label the result "manual read" with its coverage. [13 §4]

Method:
1. **Scope:** our listing (per size/colour family where reviews are split) and the same top 5–8 true competitors as §3. Sample size and recency window: No source rule; decide and record (state N per listing and the date range).
2. **Capture per listing:** star distribution; review count and monthly velocity; top recurring **positive** themes (the drivers shoppers name); top recurring **negative** themes (objections: fit / sizing, material feel, durability / pilling, colour accuracy vs images, set contents, smell, shrinkage — adapt per category); claims that reviews confirm or contradict; reasons given for returns; review photos that show a mismatch with the main image.
3. **Count, don't quote:** record each theme as mentions ÷ reviews read, with one short example.
4. **Map each theme** to a listing element (objection → gallery "objection kill" image, bullet, A+ comparison) and to the quadrant it explains (negative themes on a CONVERSION syntax are the first place to look).
5. **Compare:** our negative themes that rivals do not share = offer/product gaps; rivals' negative themes we avoid = claims to promote (defensibility note, §3).
6. File every actionable theme in the register (§6) with evidence and owner.

---

## 8. Open questions for the owner

1. **Syntax CVR target.** Resolved — see 13 #20: syntax CTR and CVR vs Market × 1.10 (fail below 0.9 × target); keyword CVR target Market × 3.0.
2. **Review-read sample.** No source defines how many reviews or which window to read; set a house default.


---

<!-- FILE: references/10-longitudinal-validation.md -->
# FILE: references/10-longitudinal-validation.md

# 10 — Longitudinal validation: ledger, grading, escalation, validation plan

Read in Phase 9, and at the **start** of any refinement cycle (grading comes before any new decision). Every decision this skill makes is a prediction; this file is how predictions are recorded, checked and acted on.

## Contents
1. The cycle loop
2. Records: action log, impact ledger, manager responses
3. Week-1 (no prior cycle)
4. Execution verification
5. Grading order
6. Escalation loop
7. Marginal read and freeze
8. Refinement: grading a prior plan
9. Prediction format
10. Reversal conditions
11. Validation plan template and standard checkpoints
12. Read-window rules
13. What to surface every cycle
14. Open questions for the owner

---

## 1. The cycle loop

Run in this order every cycle. Do not decide anything new on a row until steps 1–4 are done for it.

1. Load the prior action log, the impact ledger and any manager responses. None supplied → Week-1 (§3). [SR]
2. **Verify execution** of every logged action against the new bulk/console state (§4). [SR, WB, LTSF]
3. **Grade** each executed action in the fixed order (§5). [SR, PB]
4. **Update the ledger**: counters, escalations, manager-acted grades, freezes/floors (§6–7). [SR]
5. Decide this cycle's rows (master decision order in SKILL.md). Escalated rows are held and referred, not re-decided by formula. [SR]
6. Write new log rows, each with a prediction (§9) and a reversal condition (§10). [SR, PB]
7. Write the validation plan (§11) — dated checkpoints with pass conditions and fallbacks. [B6]

Why this order: a lever that was never applied, or applied during a deal, or priced on economics that have since moved, cannot be credited or blamed. Grading first stops the next decision repeating a failure.

---

## 2. Records

### 2.1 Action log (one row per actioned unit per cycle)

**Which rows are logged:** any row with a new bid, new placement %, new budget, or an action containing negate / pause / refer / retag; plus by-hand actions (variation switches, SB/SD builds), which are verified from the console or next export. [SR, B6]

**Log ID** = `cycleDate|CampaignID|KeywordID-or-TargetID` — idempotent: re-running the same cycle overwrites, never duplicates. [SR]
**Unit** = keyword/target × match type × objective (summed across rows of the same unit). [SR]
**Lever recorded** (first that changed): Bid > Placement > Budget > Negation/Status. [SR]

| Group | Fields |
|---|---|
| Identity & context | Log ID, cycle date, campaign (name + ID), target/keyword ID + text, match type, advertised SKU, objective, stage, deal state, LTSF state, DOH/zone, break-even ACoS, target ACoS, max acceptable ACoS [SR] |
| Change | lever, action (decision label), reasoning, before → after bid, bid Δ%, before → after placement %, before → after budget [SR] |
| Baseline (as read this cycle) | spend, sales, orders, clicks, ACoS, TACoS, CTR, CVR, WAS%, TOS %, impression share, organic rank, RPC, DSTR, break-even used to price the action [SR] |
| Prediction | expected metric, direction, magnitude, tolerance, horizon/timeframe, basis tag (HIST / MARKET / TEST), review date [SR, PB, LTSF] |
| Reversal | reversal condition + what happens if it fires (§10) [PB, WB] |
| Result (filled next cycle) | execution status, verdict, actual value, root cause, follow-up [SR] |

Defaults when no prediction was written: expected metric = organic rank for Ranking / Re-Ranking objectives, ACoS otherwise; tolerance ±3 ranks / ±3 ACoS points; timeframe "within 1–2 cycles"; Result = OPEN. [SR]

**Retention:** keep every row forever; trailing reads and streaks use a **rolling 12-week window**. The log is the history store. [SR]

### 2.2 Impact ledger (one row per unit, carried forward; lives outside the workbook)

**Key** = `CampaignID|Target-or-KeywordID`. [SR, WB]

| Field | Meaning |
|---|---|
| IDs, keyword/target, SKU, objective | identity |
| Last cycle graded, last verdict | most recent grade |
| Consecutive no-impact | count of consecutive FLAT/BACKFIRED grades |
| Escalate | true when consecutive no-impact ≥ 2 |
| Last ACoS Δ / last rank Δ, last lever | what moved and with which lever |
| History | verdict string, e.g. `FLAT>FLAT>M:WORKED` (M: = manager-acted grade) |
| Loop status | OPEN → ESCALATED → MANAGER_ACTED → RECOVERED or MANAGER_INEFFECTIVE |
| Manager action / lever / date / baseline ACoS + rank / verdict | captured when a manager acts on an escalated unit |
| Freeze/floor bid + date | recorded on saturation (§7), on a BACKFIRED raise, and on every taper/ladder floor |
[SR]

### 2.3 Manager responses (input)
File columns: Key, Manager Action, Manager Lever, Manager Action Date. Read before grading so an escalated unit the manager changed is graded as MANAGER_ACTED, not as the formula's lever. [SR]

---

## 3. Week-1 (no prior cycle supplied)

- No impact review, no verdicts, no escalation. [SR]
- Write the full baseline for every unit: bid, budget, placement %, clicks, spend, sales, orders, ACoS, TACoS, CVR, CTR, rank, impression share, DSTR, inventory. [SR]
- State it in the output: "No prior cycle supplied — treated as first cycle. Impact review skipped. Baseline written." [SR]
- If an earlier plan exists but no log (refinement without a ledger), grade against the plan's written predictions (§8) and say the ledger starts now. [PB]

---

## 4. Execution verification

Verify before grading. An action that never reached the account cannot work or fail. [SR, WB, LTSF]

| Status | Test (bids) | Effect |
|---|---|---|
| **EXECUTED** | \|actual − recommended\| ≤ $0.01 | Graded normally |
| **NOT_EXECUTED** | \|actual − before\| ≤ $0.005 | No verdict, no counter movement; **re-issue** the recommendation (re-check it still holds) |
| **PARTIAL** | changed, but not to the recommended value | Graded with a note; **never counted** toward escalation |
| **UNVERIFIABLE** | no bid recommendation on the row (negation, status, referral) | Graded normally |
[SR]

- Placement %, budget and state changes: no source tolerance exists — treat an exact match to the written value as EXECUTED and record the rule used. Negations/pauses: verify where the new bulk shows them (negative row present, state = paused); otherwise UNVERIFIABLE. [SR; decide and record]
- **Execution rate** = EXECUTED ÷ (all logged actions with a verifiable value). Report every cycle. **< 80% = follow-through problem**, stated openly in the summary, not buried. [SR]
- Never blame an un-uploaded recommendation; never grade an undeployed action. [SR, WB, LTSF]

---

## 5. Grading order (first match wins)

| # | Test | Verdict | Counter |
|---|---|---|---|
| 1 | Logged this cycle (log date = cycle date), or horizon not yet reached | **TOO_SOON** | no change [SR, WB] |
| 2 | Grading span overlaps a deal/event window | **DEAL_WINDOW** — no WORKED/FLAT/BACKFIRED; re-grade on the first clean cycle | frozen [SR] |
| 3 | Unit absent from this cycle's data; or a second lever changed on it inside the window; or the advertised SKU changed (re-route) | **CONFOUNDED** | not counted [SR, LTSF, PB] |
| 4 | Execution (§4) | NOT_EXECUTED → stop here; PARTIAL → continue, flag | per §4 [SR] |
| 5 | Break-even the action was priced on vs current break-even shifted **> 10%** (price, fee, packaging, LTSF event); or a logged price change coincides; or an AOV shift from variation mix | **PROVISIONAL** — no credit, no blame | no change [SR, PB] |
| 6 | **< 15 fresh clicks** since the action was executed | **TOO_SOON** | no change [SR, WB] |
| 7 | Primary metric moved (current − baseline = Δ) | Δ ≤ −3 → **WORKED**; Δ ≥ +3 → **BACKFIRED**; else **FLAT**; metric missing → TOO_SOON | WORKED → 0; FLAT/BACKFIRED → +1 [SR] |

- **Primary metric:** the logged prediction's metric. Default: organic rank for Ranking / Re-Ranking (±3 places; lower number = better), ACoS for every other objective (±3 points). [SR]
- Other objectives graded on their own metric when the prediction names it — Defensive: share held per branded query; Discovery: converting terms per $100 / graduation; Conquest: CPA + share of target page; Market Share: impression-share band. Tolerance = the one stated in the prediction (no source default). [PB, OC]
- **Fresh clicks** means clicks since execution, not the cycle total (the SR code counts the cycle total — a known defect). [SR defect]
- Promotional/lever reads (price, coupon, deal-depth levers): read at **day 7 and day 14**; actual uplift **< 50% of predicted → replace the lever, don't extend it**. [LTSF]

---

## 6. Escalation loop

| Step | Rule |
|---|---|
| Count | FLAT or BACKFIRED → consecutive +1; WORKED → reset to 0; TOO_SOON / DEAL_WINDOW / CONFOUNDED / PROVISIONAL / NOT_EXECUTED / PARTIAL → no change [SR] |
| Escalate | **2 consecutive** FLAT/BACKFIRED → Escalate = true, loop status ESCALATED. The row is **held and referred** (decision REVIEW) — the formula does not move it again [SR] |
| Manager acts | Manager response captured → MANAGER_ACTED: record action, lever, date, baseline ACoS + rank; verdict this cycle TOO_SOON [SR] |
| Grade the manager's action | next cycle, same grading order: WORKED → **RECOVERED** (counter 0, escalate off); FLAT/BACKFIRED → **MANAGER_INEFFECTIVE** (stays escalated; **structural review**: listing, offer, inventory, objective) [SR] |
| Re-diagnose | the **same verdict for 4 consecutive cycles** without its predicted effect = diagnosis error → re-diagnose the row from Phase 0 inputs, not the lever [PB, WB] |
| Dead lever | **never repeat a failed lever a 3rd time.** After two failed grades on a lever the next move is a different lever (adjacent in the hierarchy) or escalation, and the reasoning names the lever that failed [SR] |

Related persistence rules: ranking State B (clicks over plan, rank flat) **4 consecutive flat reads → STOP-LOSS** (concede or defer, reallocate); State F (delivery 95–120% of plan) 4 cycles → escalate. [PB]

Why two thresholds: 2 failures says the lever is exhausted; 4 identical verdicts says the diagnosis behind every lever is wrong. [Register #25]

---

## 7. Marginal read and freeze

On every **EXECUTED raise**, compute from baseline → current deltas:
- **Marginal CPC** = ΔSpend ÷ ΔClicks; **marginal ACoS** = ΔSpend ÷ ΔSales. [SR]
- Marginal ACoS **> 1.5 × average ACoS** → saturation: **FREEZE** at the prior rung; record Freeze/Floor bid + date in the ledger. [SR]
- Marginal ACoS **> 2 × blended ACoS** → unwind the step. [PB]
- A **BACKFIRED raise** also records Freeze/Floor bid + date. [SR]
- Record every floor found by a taper or ladder too (sufficiency taper, defensive ladder, incrementality ladder). "Every unrecorded floor is paid for twice." [SR, PB]
- Never credit a step that was capped (e.g. top-of-search boost at 900%) with new clicks. [B6 R-M2]

---

## 8. Refinement: grading a prior plan

1. Read the whole prior plan; classify each decision **stated / gap / stale**; collect data only for gap and stale items. [PB]
2. **Before any new decision**, grade every prior actioned keyword against **its own prediction and reversal condition**: worked / flat / backfired / too soon (plus the execution and window verdicts above). Show the grade in a scoring table **and** in that keyword's reasoning. [PB]
3. Forward-only: never silently rewrite a prior decision; changes go in a change log. [PB, WB]
4. Reviewer marks and owner overrides from prior rounds persist; a regeneration that reverts one fails the gate. [PB]
5. A finding whose evidence was overturned moves to the withdrawn-findings register with the overturning evidence; it is not carried forward. [DR]
6. Plan and companion workbook headline figures (roster counts, budget totals, goal, sufficiency status, TACoS) must reconcile; record any difference. [PB]
7. The weekly audit opens with a prior-week action review: was it executed, what happened. [QA]

---

## 9. Prediction format

Written **before money moves**, on every actioned row. [PB]

| Element | Content | Example (B6) |
|---|---|---|
| Metric | the one number that should move | organic rank on "bamboo sheets queen size" |
| Direction | up / down / hold | down (better) |
| Magnitude | size of the move, with tolerance | ≥ 3 places (default tolerance) |
| Horizon | date or cycle count | by the 12 Oct weekly tune (settled read) |
| Basis | HIST (this SKU/sibling measured) / MARKET (competitor ceiling) / TEST (pre-registered) — untagged predictions block scenario ranking | HIST: last push step moved rank 4 places |
| Review date | the checkpoint in the validation plan | 12 Oct |
[PB, LTSF, SR]

Rules:
- Ranges, not false precision ("~38–42%"); label directional estimates. [AP]
- Any soft coefficient (uplift multiplier, click elasticity) is named as soft, with when and how it will be measured. [PB]
- Forecast credit for a price step is capped by what steps of that size bought before; paused keywords and retags get zero credit. [B6 F20]
- Click/volume requirements set volume and budget only, never price; reconcile their sum to what the product sells. [B6 F21]

---

## 10. Reversal conditions

Every action carries one: **metric + threshold + window + what happens**. Standard conditions:

| Action | Reverses when | Then |
|---|---|---|
| PUSH step | top-of-search share < 30% and not top-3 sponsored most hours | next +30% step, never above ceiling [B6 R-P4] |
| PUSH at ceiling | 3 days at ceiling without holding the top | owner: time-boxed ceiling raise, or swap the term [B6 R-P6] |
| PUSH (any) | TOS CVR below market on 50+ clicks | stop the push; back to break-even [B6 R-P7] |
| PUSH (weekly) | held the top a week with no rank movement | check listing, stock, conversion; swap [B6 R-P7] |
| HOLD RANK | rank slips past target | rejoin the push [B6 R-P8] |
| Sufficiency taper | slip > 2 places on a top-5 term, or any slip below target elsewhere | restore last step = recorded floor [PB] |
| Incrementality step (−15%) | total orders fall > 10% | restore, record floor [PB] |
| BREAK-EVEN step-down | rank falls > 10 places | restore one step [B6 R-B2] |
| Non-ranking CUT | orders fall > 30% on the settled read | restore half the cut [B6 R-N1] |
| MIX FIX | product pages still > 20% of clicks after 7 days | cut base again [B6 R-M1] |
| HARVEST exact | ACoS > break-even on ≥ 15 clicks, 14 days after launch | bid down [B6 R-K4] |
| BLOCK | spend on the blocked term not ≈ 0 after 14 days | check where the negative sits [B6 R-K2] |
| BLOCK on a contested term (≥ 10,000 market traffic, ≥ 5 rivals) | 30 days pass, or listing/price changes | re-test in discovery at break-even [B6 R-CI9] |
| Defensive above-ceiling allowance | no competitor/non-brand presence for 2 consecutive reads | withdraw; price at plain break-even [PB] |
| Conquest target | CPA > watch-CPA for 2 consecutive reads with no page-share gain; target loses 2-of-3 | exit or rotate [PB] |
| SBV arbitrage | SBV CPC > 0.8 × SP exact CPC, or completion rate fades 2 consecutive weeks | exit [PB] |
| Yellow/Red hold | restock date reached | resume named keywords at named target ranks (dated re-entry plan) [PB] |
| Formula-only price correction | fails either test: converts once clicked AND gets clicks at all | suppression check next cycle [PB] |
| Fixed-bid trial | judged at 15 clicks (multi-keyword: 7–8 day review) | keep fixed, or revert [PB] |
| Re-enable inside an event | CPA > ceiling for 7 days | pause again [DR] |
| Competitor price move (> 15% cut, new discount, traffic > +50%) | — | hold our price 3 days; don't read the conversion drop as a bid problem; over-ceiling cuts still apply [B6 R-CI11] |

---

## 11. Validation plan template and standard checkpoints

Template (one row per checkpoint; lives in the workbook "Validation plan" tab and the document's next-steps section):

| When | What | Metric | Pass | Fallback | Rule |
|---|---|---|---|---|---|

Standard set — include every row that applies to the product; replace bracketed values with the product's own. Rule IDs go in the workbook only, never in narrative text.

| When | What | Metric | Pass | Fallback | Rule |
|---|---|---|---|---|---|
| Daily through the push window | Push terms | TOS impression share; sponsored rank | ≥ 30% share and top-3 most hours | +30% price step, never above ceiling | [B6 R-P4] |
| Day 3 at ceiling | Push terms at ceiling | holding the top? | holding | owner: time-boxed ceiling raise, or swap | [B6 R-P6] |
| Daily | Product total ad spend | spend vs limit | ≤ limit (event exceptions dated) | lower push budgets from the bottom of the funded list | [B6 R-F5] |
| Weekly | Product | margin after ads vs owner rule | at or above rule | cut the push from the bottom of the list | [B6 R-F6] |
| Daily | Product | spend pace vs day-of-week curve | within ±25% | flag same day | [PB] |
| Daily until +7 days after an event | Head terms | organic rank | no term down > 10 places | find the cause before any price change | [B6 E4] |
| Daily | Stock (hero of each pushed size) | available cover (30-day pace) vs days to next dated arrival | cover ≥ days to arrival + 7 (push allowed) | cover ≥ arrival but < +7: no further push steps; short ≤ 7 days: ease, no swap; short > 7 days: switch to backup colour, same size | [B6 R-I2/R-I3/R-I4] |
| Each checkpoint of a push | Projected DOC (stock + dated inbound at baseline burn + order gap) | days of cover | ≥ 60 (Green) through the checkpoint | block, shrink or time-box the push; wait for inbound | [WB, PB, register #42] |
| Day after an event ends | Post-event audit | price back to regular; margin at full price | — | re-price every ceiling on full-price margin; taper event bids over 3–5 days | [B6, SR] |
| 7 days after each mix fix | Mix-fixed campaigns | product-page share of clicks | ≤ 20% | cut the base again | [B6 R-M1] |
| First settled week (7 clean days after attribution settle) | Break-even step-downs | ACoS, orders, rank | ACoS toward break-even; rank not down > 10 | restore one step | [B6 R-B2] |
| First settled week | Non-ranking cuts | ACoS, orders | orders within −30% | restore half the cut | [B6 R-N1] |
| Weekly push tune | Push plan | rank movement per term | moving (≥ 5 rivals at SP #1–5: judge after 7 days, not 3) | held top a week without moving → check listing, stock, conversion; swap | [B6 R-P7, R-CI5] |
| Any time, ≥ 50 TOS clicks | Push terms | TOS CVR vs market | ≥ market | stop the push | [B6 R-P7] |
| 14 days at ceiling, stretch target | Terms whose target is held only by aspirational rivals | rivals passed | ≥ 1 rival passed (first milestone) | owner decision | [B6 R-CI2] |
| 2 consecutive clean weeks at target | At-target terms | rank vs target | held | begin taper ~10%/week to floor 5–10¢ under blended CPC | [PB, B6 R-P8] |
| 14 days after harvest launch | Harvested exacts | ACoS on ≥ 15 clicks | ≤ break-even | bid down | [B6 R-K4] |
| 14 days after block | Blocked terms | spend on the term | ≈ 0 | check the negative's placement | [B6 R-K2] |
| Dated goal checkpoint | Product goal | e.g. top 10 on half the push terms | met | re-plan in the weekly tune | [B6] |
| Every event on the calendar | Events | no judgement on event days | — | size the push (price, clicks, budget, stock) ≥ 1 week ahead (major events ≥ 3 weeks); reads skip event days | [B6 E1, PB] |
| Day 7 and day 14 of a price/promo lever | Lever | actual vs predicted uplift | ≥ 50% of prediction | replace the lever | [LTSF] |
| Daily during an SB/video test | Banners | impressions; bid vs ceiling | showing on each term | +30% bid step, never above the SB ceiling (2 × break-even on push terms and on brand terms with verified rival presence; 1 × elsewhere) | [B6 R-CI10, register #45] |
| End of SB/video test (≥ 15 clicks) | SB/video campaigns | ACoS; same-term SP orders + TOS CVR; organic rank; new-to-brand share | ACoS ≤ break-even; SP orders not down | BE–2×BE: hold at break-even bid; > 2×BE: stop; SP orders fall more than SB adds: stop | [B6 R-CI10] |
| Next competitor export after a brand-defence change | Brand terms | rivals' share of the brand term | below the baseline share | keep brand exact funded; review | [B6 R-CI6] |
| Next cycle | Every logged action | execution status | EXECUTED | re-issue; report execution rate | [SR] |

Example (B6): push window daily 29 Sep–14 Oct; spend limit $1,300/day on deal days; head-term rank daily to 7 Oct; post-deal audit 1 Oct re-pricing on the $18.81 full-price margin; settled reads 8–14 Oct; weekly tunes 5, 12, 19 Oct; goal "top 10 on half the push terms" by 19 Oct; deal days 15 Oct and 22–28 Oct excluded; SB/video test read 14 Oct; brand-defence pass = rivals' share of "decolure bamboo sheets" below 48%.

---

## 12. Read-window rules

1. **Evidence vs context:** current 7 days vs prior 7 days is the evidence a live action is judged on; 60–90 days is baseline, sample and trend context only. [PB, WB]
2. **Attribution settle:** SP credits orders up to 7 days after the click (SB/SD reports use a longer window, up to 14 days). A window whose end falls inside the attribution period reads low — compare settled windows only. [B6 E2]
3. **Deal/event exclusion:** no ACoS/CVR/rank verdict on event days; for **2 weeks** after an event closes, event-week rates stay out of trend reads; floors, ladders and ceilings resume pre-event values after the guard unless the event produced real evidence (e.g. sustained higher rank). [SR, PB]
4. **Settled read:** 7 clean days that start after the attribution settle following the event. Example (B6): deal ended 30 Sep → watch-don't-judge 1–7 Oct → first clean read 8–14 Oct. [B6]
5. **Deal state is separate:** deal-state margin, CVR baseline and rank arc are kept apart from clean-state; the clean arc governs. [PB]
6. **Windows never straddle a lever change.** A read that crosses a change of lever, price or advertised SKU is CONFOUNDED; use the post-change portion only if it has ≥ 15 clicks. [LTSF, PB]
7. **Two levers in one window = confounded.** Stage changes so each lever gets its own window. [LTSF]
8. **Rank trends:** ≥ 1 month of history (ideally 3); state overall, 14-day and 7-day separately (shorter = early warning); exclude stockout/re-route stretches; median over the window with unranked days counted as unranked, not as a rank. [PB, B6]
9. **Non-ranking judgement** uses 30-day and 90-day windows together; over on 30 but inside on 90 → MONITOR (no change, named re-read date). [B6 R-N1]
10. **Velocity windows:** 30-day pace for cover; 7-day pace as a warning only; never the inflated push pace; distorted windows (stockout, suppression, deal) are corrected with a stated factor. [B6, LTSF]
11. **Economics freshness:** margin older than 45 days, or any price/fee/packaging/LTSF change, makes grades PROVISIONAL and ceilings stale until refreshed (within 48 h). [SR, PB]
12. **Budget-truncated windows** (in-budget < 70% of the day) are not evidence for bids; 0% in-budget with $0 spend = missing data. [PB]

---

## 13. What to surface every cycle

Verdict counts (by verdict), escalations opened / resolved (RECOVERED) / ineffective, execution rate and the NOT_EXECUTED list being re-issued, PROVISIONAL grades with the economics event behind them, freezes/floors recorded, rows re-diagnosed after 4 cycles, and the validation plan's next three dates. [SR, PB]

---

## 14. Open questions for the owner

1. Marginal read: Resolved — see 13 #34: freeze at the prior rung when marginal ACoS > 1.5 × average; unwind one step when > 2 × blended (freeze first, unwind second).
2. No source sets an execution tolerance for placement %, budget or state changes; exact match is used here. Confirm or set one.
3. No source sets a grading tolerance for defence share, discovery graduation, conquest page share or market-share band. Set per product when the prediction is written, or give house defaults.


---

<!-- FILE: references/11-exceptions-and-failure-modes.md -->
# FILE: references/11-exceptions-and-failure-modes.md

# 11 — Exceptions, BLOCK conditions and the failure register

Read **before finalising any decision**. Part A lists the conditions under which no automated change is made (the row is held, blocked, referred or asked about instead). Part B is the consolidated register of every known failure mode from the source skills and the B6 engagement, with a test for each. Run Part B's tests as part of the quality gate (reference 12).

Source tags: see reference 13. "(seen: B6 Fnn)" = the failure actually occurred in the B6 engine run of 28–29 Sep 2026. Examples marked "Ex (B6)" are illustrations from that case, not rules.

## Contents
- Part A — Exceptions and BLOCK conditions
  - A.1 Data, scope and intake
  - A.2 Events and deals
  - A.3 Goal, economics and pricing
  - A.4 Inventory, variations and LTSF
  - A.5 Structure and keywords
  - A.6 Quality, rank and market
  - A.7 Process, approval and the silent-hold list
- Part B — Failure register
  - B.1 Data and intake
  - B.2 Economics
  - B.3 Inventory and routing
  - B.4 Keywords and negation
  - B.5 Campaigns and objectives
  - B.6 Placement and pricing
  - B.7 Ranking
  - B.8 Competitors
  - B.9 Events and deals
  - B.10 Writing and deliverables
  - B.11 Process and engineering
- Open questions for the owner

---

# Part A — Exceptions and BLOCK conditions

**How to use:** check every row against this list after the master decision order produces a decision. If a condition fires, write the "instead" action, the decider, and the dated re-check. An exception is a decision, not a skipped row — it still gets a trail. Who decides: **Analyst** (the person running this skill), **Owner** (product owner), **Approver** (signs off uploads), **Brand Mgmt**, **Supply Chain**.

## A.1 Data, scope and intake

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-01 | A required input is missing and not confirmed absent | No partial start. Ask once, in one batch; record a named gap and the decisions it blocks [PB, QA, WB] | Analyst → Owner | — |
| A-02 | Data validity: CVR/ACoS with 0 orders, CTR with 0 clicks/impressions, values conflicting across bulk / console / Sellerboard / SQP | Quarantine: no recommendation; same-day refresh task [PB, SR, WB] | Analyst | — |
| A-03 | Source mismatch that moves money: DOH differs > 0.5 day or LTSF > $0.02 from source; target CTR/CVR drift > 2% on > 10% of rows; SKU not matched exactly (incl. colour) | Halt the run ("accuracy gate failed"); unmatched SKUs flagged, never filled [SR] | Analyst | — |
| A-04 | Advertised SKU has no economics; break-even outside 5–70%; fee ÷ price > 55% | Halt that SKU (never a default break-even); flag; contaminated fees → portfolio median fee ratio from clean SKUs (≥ 10 units), "verify with Brand Mgmt" [SR] | Analyst → Brand Mgmt | — |
| A-05 | Economics stale: margin > 45 days old, or any price / fee / packaging / LTSF change | Ceiling-based verdicts blocked; re-derive within 48 h; grades PROVISIONAL [SR, PB] | Analyst | — |
| A-06 | Missing state: campaign has no targets/bids in the audit, or isn't in the product's list | Confirm in the console; give break-even for reference only [B6 E7] | Analyst | Ex (B6): 29 campaigns; 6 found spending but missing from the list |
| A-07 | Read window ends inside the attribution period | Sales/orders read low; compare settled windows only [B6 E2] | Analyst | Every read |
| A-08 | Thin data: < 15 clicks (product targets < 11) | No change; formula-only correction allowed if over ceiling; converting rows are exempt [B6 E3, PB, SR] | Analyst | Ex (B6): 94 campaigns, 430 search terms |
| A-09 | Rank history < 1 month (or only stockout/re-route stretches) | OUT OF SCOPE for a ranking verdict; say "efficiency decision inside a ranking campaign" [PB, DR] | Analyst | — |
| A-10 | Budget truncation: in-budget < 70% of the day | No bid verdict; budget first. 0% in-budget with $0 spend = missing data, not truncation [PB] | Analyst | — |
| A-11 | No SQP targets; no impression-share data | Four-quadrant does not run ("no targets"); CTR root cause "undetermined" — no CTR-driven bid change [SR] | Analyst | — |
| A-12 | SKU provenance: a different SKU served all or part of the window | Correct price now if over ceiling; read only the post-change part if ≥ 15 clicks, else formula-only; rebuild economics, reset CVR baseline and rank clock [PB] | Analyst | — |
| A-13 | Shared campaign advertising other products | No colour or price automation from this product; review in its own product's audit [B6 E13] | Analyst | Ex (B6): DBS4 auto; B4 LTSF; LTSF multi-SKU |
| A-14 | Sponsored Brands / video / Display | Outside automated pricing; reported "not decided", never silently skipped; tests are hand-built with their own budget line and break-even bids [B6 E12, SR, B6 R-CI10] | Owner | Ex (B6): 33 campaigns; SB/video test approved, $85/day × 14 days |

## A.2 Events and deals

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-15 | Date inside a deal/event | No new campaigns, folds or structural changes; no ACoS/CVR verdicts on event data; pricing only per the push plan and cuts; bleed stops and over-ceiling cuts still run [B6 E1, SR] | Analyst | Ex (B6): 17 builds and 2 folds held on 29–30 Sep |
| A-16 | Event ahead with no deal-state economics | Compute the deal-state margin and ceiling (net of deal fees) before the event; in-deal CVR never justifies a bid above it [PB] | Analyst | Ex (B6): margin $18.81 → $18.18 at deal price |
| A-17 | Deal would originate a push; seasonal index falling | Deals amplify an already-gated push, never start one; falling index → deny new pushes, pre-emptive tapers [PB] | Owner | — |
| A-18 | Event spend above the normal limit | Only as a pre-approved, dated exception with its margin stated (≤ +50% one event week); never retroactive [PB, B6 R-F5] | Owner | Ex (B6): $1,300/day on 29–30 Sep |
| A-19 | Event closed | Taper event bids over 3–5 days (no cliff); 2-week guard on trend reads [SR, PB] | Analyst | — |

## A.3 Goal, economics and pricing

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-20 | Product goal undeclared | Hard stop for a plan; the ranking gate treats it as Profit-First; a suggested goal needs confirmation [PB] | Owner | — |
| A-21 | Goal is Profit-First or Clearance | Profit-First: no new push, protect won rank only. Clearance: no rank considerations, every row at the clearance ceiling (1 × break-even on forward-cash economics, register #43) [PB] | Owner | — |
| A-22 | Ceiling below our own top-of-search cost per click | WAIT; owner may raise that term's ceiling for a set time [B6 R-P1] | Owner | Ex (B6): "bamboo sheets king size" waiting |
| A-23 | 3 days at ceiling without top-3 sponsored and ≥ 30% TOS share | Owner: time-boxed ceiling raise, or swap the term [B6 E5] | Owner | Ex (B6): "bamboo sheets" |
| A-24 | Boost at 900% and target price unreachable | Review; raise base only to price ÷ (1 + boost), boost set in the same write [B6 E16] | Analyst | Ex (B6): Bamboo Sheets King Size |
| A-25 | Step too big: push raise > +30%/day, other raise > +25%/cycle, or base cut > 50% in one step (over-ceiling cuts go straight to the ceiling, register #5) | BLOCK; split into dated steps [B6 E17] | Analyst | Ex (B6): 12 "dose" rows |
| A-26 | Expected total spend > the limit | Scale push budgets; cut from the bottom of the funded list [B6 E19] | Analyst | Ex (B6): push budgets scaled to 45% on the three biggest |
| A-27 | Margin ≤ 0 on the advertised SKU; affordable CPC = 0 | Flag and refer pricing to Brand Mgmt (not a bid problem); leave the bid, flag [SR, PB] | Brand Mgmt | — |
| A-28 | Authorised TOS price (base × (1 + boost) × 2 under up-and-down) > ceiling × 1.05 | Referral with the exact correction; strategy changes are human-only [SR] | Owner | — |
| A-29 | Realised CPC > 1.5 × governing ceiling | State "unjustifiable"; cut the price to the ceiling this run. Above 1 × break-even CPC only on a sized push, up to its 2 × ceiling [SR, register #3] | Analyst | — |
| A-30 | Weekly loss ceiling reached on a push | Human flag, not auto-stop [PB] | Owner | — |
| A-31 | TACoS breach (only where the owner set a target): 1.5–2× band, or > 2× / > 1.5× two weeks | Breach → freeze new scale. Code-red → per-row review within 48 h, daily cadence; never a blanket % cut [PB] | Owner | — |
| A-32 | Budget > $500/day; budget change > $50/day | High-budget review; approval [SR, PB] | Approver | — |
| A-33 | Campaign ACoS and TOS ACoS both over the turn-off level on ≥ 15 clicks (Ranking 100%, Market Share 50%, Discovery 60%, Profitable Conversion 50%, Defensive/PAT 30%) | "Consider turning off — refer"; never auto-off; suppressed at New Launch [SR] | Owner | — |
| A-34 | Conversion deficit (≥ 40 clicks, CVR below target, exact/phrase) | No bid-up; refer listing/offer; bid −15% (hold during a deal) [SR] | Brand Mgmt | — |

## A.4 Inventory, variations and LTSF

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-35 | Hero available < 7 days, 0, or cover < days to arrival by > 7 days | BLOCK push; ranking ads to the backup colour, same size; gap ≤ 7 days = TIGHT: ease, don't swap [B6 E14, R-I1–I5] | Analyst | Ex (B6): Twin — White at 0, Sage Green serves |
| A-36 | Red zone (< 21 days, or stock-out before inbound) | Taper to defence; re-point same day to the next viable child; no raise. Deal + Red → hold + stock-out watch [PB, SR] | Analyst | — |
| A-37 | Yellow zone (21–59 days) | No new push, no raises; hold spend; dated re-entry plan [PB] | Analyst | — |
| A-38 | Every child Red; or a push drives projected cover out of Green | Escalate as supply problem; register entry naming SKU, date it leaves Green and the push causing it [PB] | Supply Chain | — |
| A-39 | Any change of advertised child | By hand (switches don't upload); confirm size unchanged [B6 E8] | Analyst | Ex (B6): 42 switches |
| A-40 | Switch that changes size | BLOCK, except correcting a wrong size [B6 E9] | Analyst | Ex (B6): one fix, Cal King campaign on King White → Cal King White |
| A-41 | Colour with < 7 days of cover | Never add to an ad or switch to it [B6 R-C5] | Analyst | — |
| A-42 | On backup and preferred SKU back above 21 days; backup pairs not supplied | Transition-back is a suggestion, never an auto-swap; backups pasted by the user, never derived [SR, INV] | Owner | — |
| A-43 | Clearance push with the hero size Red, or LTSF SKU not Green | No clearance push [SR] | Analyst | — |
| A-44 | LTSF terminal call (removal, liquidation, disposal, donation, deep discount; floor ≥ price; break-even discount > 100%) | Present salvage comparison + recommendation; not "settled" unless charge reconciliation passed; never dispose sellable stock unless both alternatives are net worse [LTSF] | Brand Mgmt + Supply Chain | — |
| A-45 | LTSF critical: 366+ days or product charge > $5,000/mo; portfolio > $25,000/mo two months | Exec review within 48 h; portfolio review + inbound-freeze evaluation; Red tier freezes POs [LTSF] | Brand Mgmt + Supply Chain | — |
| A-46 | Structurally dead SKU (no traction 6+ months, fixes tested) | Decide within 7 days; on a new launch → strategic review (exit / redesign / reposition) [LTSF] | Brand Mgmt | — |
| A-47 | "Tested and failed" SKU that never had dedicated spend | Not condemned; give it a test first [LTSF] | Analyst | — |
| A-48 | Calendar-marked peak week vs aged-stock economics | Peak availability governs [PB] | Owner | — |

## A.5 Structure and keywords

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-49 | Campaign or every keyword paused | No price change; RESTART decision instead [B6 E6] | Analyst | Ex (B6): 28 campaigns |
| A-50 | Keeper sits in a paused campaign; dormant singleton | Flag the campaign edit needed; ask before enabling singletons [LP] | Owner | — |
| A-51 | New campaign for a term that already has an exact (live or paused, close variants) | BLOCK; restart/reuse [B6 E11] | Analyst | Ex (B6): build 2035 |
| A-52 | Same term live in > 1 instance of one match type | DEDUPLICATE: coexistence test, else owner by rate; losers withheld (paused), nothing else changed [register #13] | Analyst | — |
| A-53 | Brand negatives before the receiving brand exacts are defensive, on the hero and funded | BLOCK the negatives [B6 E10] | Analyst | Ex (B6): row 2142 |
| A-54 | Ranking tag on a colour / competitor / Spanish / misspelled term | BLOCK the tag; Profitable Conversion [B6 E18, register #36] | Analyst | Ex (B6): 12 retags |
| A-55 | Exact and broad in one campaign | Ranking + structural flag; fix (pause broad, keep exact) needs confirmation [OC, PB] | Owner | — |
| A-56 | Rank credit out of scope: auto + broad > ~40% of the term's clicks, or no live exact | No ranking verdict; same-day exact build + steering negatives [PB] | Analyst | — |
| A-57 | Negation candidate is brand, an exact row, an exact ranking term, relevant but non-converting, or < 5 clicks | Brand/ranking exact: never. Exact rows: manual review. Relevant non-converter: fix queue. < 5 clicks: manual review [STR, PB] | Analyst | — |
| A-58 | Term not indexed, or ranking term backend-only | No spend; indexing / listing task [PB] | Brand Mgmt | — |
| A-59 | Category / keyword-group targets | Not bulk-changeable — console only [CB] | Analyst | — |
| A-60 | Competitor ASIN not mapped to a brand | No SCALE until mapped [B6 E20] | Analyst | Ex (B6): 10 ASIN targets with reads |
| A-61 | New Launch stage | No turn-off, no strategy change [SR] | Owner | — |

## A.6 Quality, rank and market

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-62 | Term lost > 10 places in 30 days while getting clicks | Freeze price moves; find the cause (colour, listing, keyword state, competitor) first [B6 E4] | Analyst | Ex (B6): 4 campaigns + "bamboo sheets queen" |
| A-63 | SQP: our CTR or CVR below market on ≥ 30 clicks | WAIT: no push until the listing is checked [B6 E15] | Brand Mgmt | Ex (B6): "bamboo sheets king size", "bamboo sheets king" |
| A-64 | Rank lost > 10 despite delivery | Never a bid change; own listing first → competitor wins 2 of price/rating/reviews → isolated vs category-wide; no cause → ask [PB] | Analyst → Owner | — |
| A-65 | Syntax in Conversion or Both-failing quadrant | No rank push; fix offer; ≥ 4 weeks = chronic → bids frozen at maintenance [PB, QA] | Brand Mgmt | — |
| A-66 | Branded CVR collapse | Listing check first (suppression, buy box, review score, variation break) [PB] | Brand Mgmt | — |
| A-67 | CVR drop coincides with a logged price rise; AOV shift from variation mix | Hold bids; revert price or recompute economics; void and re-run affected verdicts [PB] | Owner | — |
| A-68 | Competitive shock (CVR ≥ benchmark, rank falling, no own event); rival price cut > 15%, new discount, traffic > +50% | Investigate before any bid (new entrant, deal, price cut); hold our price 3 days after a rival move; only then one ladder step inside ceiling, re-read in 1 week; over-ceiling cuts still apply [PB, B6 R-CI11] | Analyst | Ex (B6): KRIMANO +123% traffic; Pure Bamboo 19% off |
| A-69 | Stretch target (only aspirational rivals at/above target) 14 days at ceiling, no rival passed | Owner decision [B6 R-CI2] | Owner | Ex (B6): "bamboo sheets" target #9 held only by two leaders |

## A.7 Process, approval and the silent-hold list

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-70 | **Silent-hold list (exhaustive):** both quality gates fail; CTR passes and CVR fails; zero delivery; budget truncation; plan exceeds campaign capacity | Hold without asking; route CTR-pass/CVR-fail to Brand Mgmt; escalate capacity. **Any other HOLD → ask first and log the answer** [PB, DR] | Analyst | — |
| A-71 | Human-confirm thresholds: search volume ≥ 500; any gate failure; structural change (campaign, routing, match type, strategy); bid move > 25% outside an approved push plan (the plan covers its own +30%/day steps); budget move > $50/day [register #41, #54] | Change Review Sheet row with the trade-off in reviewer units [PB, WB] | Approver | — |
| A-72 | A provisional rule would drive a real decision for the first time on this product (goal-gate mechanics, Defensive/Conquest, harvest, discovery count basis, sufficiency exit, graded push tiers, $0.50 floor) | Ask before use; the answer holds for the product until the owner changes it [PB] | Owner | — |
| A-73 | Ledger row escalated; manager's action graded ineffective | Hold + refer; structural review (listing, offer, inventory, objective) [SR] | Owner | — |
| A-74 | Upload before approval | Never; upload file is PREPARED only after zero-failure validation [SR] | Approver | — |
| A-75 | Bidding-strategy change | Only through the fixed-bid trial with owner approval [register #8] | Owner | Ex (B6): no strategy written |
| A-76 | Amazon suggested bid / "market price" offered as a price | Not used [register #18] | — | — |

---

# Part B — Failure register

Columns: **Failure** · **Why it's wrong** · **Correct behaviour** · **Test** (how to detect it; a test that finds ≥ 1 row fails the quality gate).

## B.1 Data and intake

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| D-01 | Starting before every input is supplied or confirmed absent | Partial reads drive decisions later contradicted | One batch request; halt until each item is in or confirmed N/A | Intake register: every item READ-FULL / confirmed absent [PB, QA, WB] |
| D-02 | Guessing: filling unmatched SKUs, invented rank, TOS%, IS, prices, targets; 0 for a blank | A fabricated number is indistinguishable from a real one downstream | Blank + named gap; "Not available" | Every value traces to a file/sheet/window; no 0 where source is blank [A, E, D] |
| D-03 | Missing current ranks (38 of 40 targets) (seen: B6 F22) | Rank gap drives the premium; no rank, no push logic | Read the daily crawl rank; untracked = "not tracked" | Keyword tab rank column populated for every push/target term [B6] |
| D-04 | Unranked days counted as a rank; two rank tables used interchangeably | Median distorts; tables disagreed ~7 places | Median with unranked days as NR (NR if half the days unranked); name the governing source | Rank source column on every rank figure [B6] |
| D-05 | Fuzzy / reordered keyword matching; retyped portfolio name; mixed portfolios or marketplaces | Wrong joins; "0 rows"; blended markets | Exact lowercase/trim match; copy the portfolio string; one product, one marketplace | Join-miss count reported; marketplace single-valued [A, E] |
| D-06 | One portfolio when ranking spend lives in a sibling | Understates spend ("$94 artifact") | Include sibling campaign scope; reconcile openly | Campaign-scope vs product-scope reconciliation shown [QA] |
| D-07 | Summing SQP market columns across child ASINs; using SQP's precomputed rates | Multiplies market by child count; every share wrong | Market taken once, brand summed; recompute rates | Brand ≤ market; shares 0–100% [SQP] |
| D-08 | Recomputing SSOT product metrics from the bulk; deriving a value that was supplied | Two versions of one number | Supplied column beats derivation; wrong-looking column = finding | One figure, one value across tabs [QA, WB] |
| D-09 | Skipping quarantine (CVR with 0 orders, CTR with 0 clicks, conflicting sources) | Decisions on impossible data | Quarantine, no recommendation, refresh | Quarantine count reported; no action on quarantined rows [PB, SR] |
| D-10 | Judging thin data; small-sample placement verdicts (seen: B6 F32) | < 15 clicks measures nothing | No change under 15 clicks (11 PT); placement comparisons use the significance test, n < 30 = directional | No actioned row < floor except formula-only [B6, PF, WB] |
| D-11 | Parking a converting row for thin clicks | Most common single violation; loses proven orders | Converting rows skip the sample gate | Rows with orders > 0 and HOLD(thin) = 0 [DR, PB] |
| D-12 | Gate read on blended data (0.626% blended vs 2.955% TOS) | Blended hides the delivering placement | Read at the delivering placement; show both | Every CTR/CVR gate cites its placement [DR] |
| D-13 | Truncated-budget data used as bid evidence; 0%/$0 read as truncation | Rates from a campaign that stopped mid-day are not rates | Budget first; 0%/$0 = missing data | No bid verdict where in-budget < 70% [PB] |
| D-14 | Changes on campaigns with no current state (seen: B6 F13) | Can raise a price on a paused or mis-coloured campaign | Read every in-scope campaign before any write | Every decision's campaign is in the state list [B6] |
| D-15 | Shared multi-product campaigns automated (seen: B6 F29) | Moves another product's ads | Exclude from colour/price automation | Shared flag on every such campaign; no writes [B6] |
| D-16 | Velocity from a distorted window (stockout, suppression, deal) uncorrected; untagged multipliers | Over/understates cover and clearance | Stated correction factor + basis | Every velocity cites window and factor [LTSF] |
| D-17 | Inventory from the variation page or units > 0; market "weekly sales" read as ours | Not sellable stock; not our sales | Full inventory export; available + dated inbound; label market data | Inventory source = full export [PF, INV] |

## B.2 Economics

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| E-01 | Break-even from the wrong margin / blended parent / another product (seen: B6 F02) | B6: $26.60 vs $18.81 → ceilings ~40% too high; 154 of 180 ranking campaigns already above true break-even | Sellerboard profit/unit before ads per advertised SKU/colour at the price in force | Break-even on every row = SKU margin × placement CVR [B6, SR] |
| E-02 | Silent default break-even when a SKU has no economics | Prices a SKU on nobody's margin | Halt that SKU | No row priced without SKU economics [SR] |
| E-03 | Limit set by what we paid (TOS cost + 15%) (seen: B6 F23) | Drifts up with every raise; ignores profit | Ceiling = 2 × break-even CPC (ranking); ≤ 1 × break-even elsewhere | Price ≤ ceiling on every row [B6] |
| E-04 | Push sized on a TACoS rung; TACoS used as a bid gate (seen: B6 F24) | Owner rule is margin after ads and a spend limit | Size spend against the limit and margin rule; TACoS monitored only | Total ≤ limit; no TACoS-derived budget [B6, register #17] |
| E-05 | Cuts triggered by leaving a band, not break-even (seen: B6 F31) | A band isn't profit | Cut when over break-even on both 30 and 90 days | Every non-ranking cut cites both windows vs break-even [B6] |
| E-06 | Per-unit ceiling used as a per-click ceiling | Allows bids ~1 ÷ CVR too high | Break-even CPC = margin × CVR | Ceiling unit = $/click [WB] |
| E-07 | Returns added to break-even; COGS in LTSF decisions; LTSF floor = break-even | Mixes locked definitions; COGS is sunk in clearance | Locked break-even (no returns); forward net recovery; floor = salvage parity | Formula audit [SR, LTSF] |
| E-08 | LTSF read per unit or at a flat rate | Overstates 1.4–4.8×; understates near-cliff batches up to 3.6× | Per cubic foot per month by age bracket, assessed on the 15th | Charge reconciles to invoice [LTSF] |
| E-09 | Trimming rows already ≤ break-even; raising > break-even rows "to gather data" | Cuts profit; buys losses | Leave ≤ BE rows; data-gathering only inside ceiling | No cut on ACoS ≤ BE without an aged-clear reason [SR] |
| E-10 | Across-the-board cut while TACoS is healthy; blanket % cut under code-red | Destroys profitable volume | Negate/harvest the leaks; per-row review | No uniform % change across > 5 rows [SR, PB] |
| E-11 | Cut batch not checked for opportunity cost | Saved spend can be worth less than lost orders | Re-test each cut at the deal-state margin; withdraw failures | Lost-order value < spend saved, per cut [PB] |
| E-12 | Price/fee event credited to or blamed on a lever | False WORKED/BACKFIRED | Break-even shift > 10% → PROVISIONAL | Grade vs break-even delta [SR] |

## B.3 Inventory and routing

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| I-01 | Ranking ads switched to a slow colour (Queen → 7th seller) (seen: B6 F09) | Lowers CVR and margin; costs rank | Ranking advertises the size's best seller; backup only when it can't last to arrival | Every ranking campaign = hero of its size or listed exception [B6] |
| I-02 | Colour switch that changes size (seen: B6 F10) | Breaks the listing the shopper searched | Size locked on every switch | Size-changing switches = 0 (one wrong-size fix allowed) [B6] |
| I-03 | Discovery on best sellers (seen: B6 F11) | Hero stock is for ranking; discovery should move slow stock | Discovery advertises the size's clearance colour (≥ 180 days cover, or ≥ 90 while selling ≤ size median) | Discovery colour = clearance colour [B6] |
| I-04 | Cover computed on the engine's inflated push pace (seen: B6 F30) | Creates a stock-out that isn't there | 30-day pace (7-day warning); TIGHT ≤ 7 days = ease, don't swap | Cover column cites the 30-day pace [B6] |
| I-05 | Push or raise on Red/Yellow; bids on 0-stock or non-serving rows | Push into a stock-out loses rank | Zone gate before performance | No raise where zone ≠ Green [SR, PF, PB] |
| I-06 | Routing read from campaign names (212 of 251 wrong) | Names drift | Read Product Ad rows | Routing source = product ad rows [WB, PB] |
| I-07 | Backups auto-derived; backup self-competition ignored; inbound ignored | Wrong fallback; swapped ad competes with its own campaign; overstock regenerates | Backups pasted by user; note existing ads; inbound vs DOH ceiling | Backup source recorded [INV, LTSF] |
| I-08 | Ceilings carried from the departing SKU after a re-route; baselines not reset | Wrong economics | Rebuild economics; reset CVR baseline, rank clock, ROS gate | Re-routed rows show new SKU economics [PB] |
| I-09 | Stockout signature read as relevance loss | Rank collapse in one colour/size during an outage is stock | Check stock timeline first | State E notes cite stock timeline [LTSF] |
| I-10 | High cover read as safe while velocity declines 15% WoW for 3 weeks | Cover rises because demand falls | Treat as trajectory problem | Velocity trend beside DOH [PB] |
| I-11 | LTSF: discounting a fixable-demand SKU; parent-wide levers on variation overstock; stacking past cap; experimenting on a dead SKU > 7 days; removing profitable aged stock; disposing sellable stock; single-family plan | Wrong archetype = costliest LTSF error | Classify archetype first; child-scoped levers; ≥ 2 lever families | Archetype + scope on every lever [LTSF] |

## B.4 Keywords and negation

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| K-01 | Negating an exact ranking term, a brand term or a relevant term (SR zero-order branch) | Kills rank and the most profitable orders | Brand/ranking exact never; relevant non-converter → fix queue; ≥ 20 clicks 0 orders → REDUCE (relevant, live owner) / REVIEW (relevant, no owner) / BLOCK (irrelevant) [register #38] | Brand and push terms never blocked [SR defect, STR, B6] |
| K-02 | Negating on spend alone, < 5 clicks, root-wide sweeps, or with no mode stated | Removes demand without evidence | STR tree; cite that occurrence's clicks/spend/orders; mode = pre-load / reactive / steering | Every negative cites its own numbers + mode [STR, PB] |
| K-03 | Brand variants missing from the brand list | Brand terms flagged for negation | Brand name + misspellings list | Brand-list check before negation pass [STR] |
| K-04 | Brand negatives added before brand exacts could serve (seen: B6 F18) | Moves profitable brand traffic to campaigns that can't serve it | Gate: receiving exacts defensive, on the hero, funded | Brand negatives only where gate passed [B6] |
| K-05 | Existing duplicates and paused owners left (seen: B6 F28) | Split data; self-bidding | One owner per term, close variants counted; restart or retire paused owners | One live exact owner per term [B6] |
| K-06 | Duplicate built beside a paused keyword (seen: B6 F16) | Loses history; self-competition | Restart before build | Build path checks every exact (live/paused/close variant) [B6] |
| K-07 | Word-order variants collapsed; singular + plural exacts both kept; "King" matched before "California King" | Amazon treats word order as distinct; plurals are close variants; wrong size | Word order preserved; plurals merge; longest size token first | Normalisation audit [PH, PB, E] |
| K-08 | De-dup using Ad Group State; silently enabling singletons; paused-campaign keeper unflagged; edits beyond State | Wrong status; unexpected serving | Keyword State OR Campaign State; ask before enabling; flag | No group with > 1 enabled or 0 enabled [LP] |
| K-09 | Duplicate check run before re-enables | Re-enable creates new duplicates | Dup check on the post-re-enable population | Dup check timestamp after re-enable set [PF] |
| K-10 | Relevancy scorer: overwriting the original; disqualifying "pillowcase"; non-English ≈ 0 read as irrelevant; "fixing" copy in the scorer | Destroys the second opinion; false negatives | Add columns, keep original; hand-check regex hits | Original relevancy column intact [LP] |
| K-11 | Trusting a relevancy label that is wrong (e.g. "red bamboo sheets" Not Relevant) | Blocks a real colour demand | Cross-check label against the term classifier | Label/classifier disagreements listed [B6] |
| K-12 | Harvest without negating the source; harvesting on BOTH-FAILING or off-category terms | Double-serving; scaling a broken syntax | Build exact at break-even, negate source same upload; quadrant check | Every harvest has a paired negative [PB, AP] |
| K-13 | Coverage gap from exact-text match without STR cross-check; padded coverage | Overstates the gap | Cross-check STR; relevant terms only | Gap list cites STR check [LTSF] |
| K-14 | Product targets called "search terms"; campaign-level negative on a single-ASIN PAT | Wrong entity; kills the campaign | Target-level pause for dedicated single-ASIN PAT | Negation format per entity [SR] |

## B.5 Campaigns and objectives

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| C-01 | Colour, competitor, Spanish, misspelled exacts retagged Ranking (seen: B6 F12) | Nobody builds organic rank on those; unlocks push logic wrongly | Generic niche exact → Ranking; others → Profitable Conversion; brand → Defensive [register #36] | Retags carry a classifier verdict [B6] |
| C-02 | Objective per keyword then mode-averaged; campaign name trusted over targeting; Defensive on a generic term | Objective is a campaign property from targeting | Decide per campaign from targeting | Blocks with > 1 objective = 0; Defensive has a brand keyword [OC, DR] |
| C-03 | Exact and broad in one campaign; judging on one campaign row; merging exact-ranking with broad-discovery | Mixed loops, wrong metric | Separate; judge the unit across its rows | Mixed-block flag count [OC, SR] |
| C-04 | Contradictory directions on one term (−20% here, +15% there); label contradicting the written value (seen: B6 F06) | Incoherent; a "taper" that raised price | Term-level reconciliation; notes must match value | One direction per term; label vs value check [DR, B6] |
| C-05 | Family-scoped / name-pattern batch actions; blanket root scale or cut | Not derived per row | Each row on its own data | No action justified by a group name [DR, PB, SR] |
| C-06 | Acting on rows that can't deliver: paused, duplicate, Red (seen: B6 F16 — prices raised on paused keywords) | A bid can't make a paused row serve | Restart decision; no bid on non-live rows | Bids on non-live rows = 0 [DR, B6] |
| C-07 | One lever with no alternative considered; > 1 lever per row per cycle; only one lever type ever evaluated | Misses the real constraint; confounds reads | Name why this lever, not the adjacent one; one lever per row (base+boost backward-solve exempt) | Reasoning names the alternative [DR, PB] |
| C-08 | Bidding strategy changed by default; Fixed as a default | Confounds every read; owner rule | Leave strategies; new = dynamic down-only; Fixed via trial only | No strategy written without approval [register #8] |
| C-09 | Mechanism change across many campaigns with no control arm | Can't tell effect from trend | Hold some campaigns unchanged | Control arm listed [PB] |
| C-10 | Silent HOLD outside the list; hold on a condition already met | Parks rows without a reason | Ask first; verify condition still holds | Every HOLD reason ∈ silent-hold list or logged ask [PB, WB] |
| C-11 | Paused ad group re-enabled in a different upload than its bids | Half-deployed state | Re-enable and bulk changes upload together | Upload pairing check [PF] |

## B.6 Placement and pricing

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| P-01 | +75% "dose" jumps (seen: B6 F04) | $50–100 per order vs $16–22 profit | Push price = BE × (1 + premium) ≤ 2 × BE; ≤ +30%/day | No raise > +30%; no push price > 2 × BE [B6] |
| P-02 | Over-ceiling price left in place (seen: B6 F05) | Loses money every order | Cut to ceiling in the same run, never deferred | No new price above ceiling [B6] |
| P-03 | Boost raised while the base keeps buying product pages (seen: B6 F07) | Boost only applies at the top | Mix fix: base −50% (−25% if PDP sells) + boost holds TOS price, one write | Boost raise refused when PDP > 20% without pair [B6] |
| P-04 | Escaping the 900% cap by raising base (+180%); crediting a capped step (seen: B6 F08) | Triples PDP bids; phantom clicks | Base = price ÷ (1 + boost), boost set together | No boost > 900%; base changes paired [B6] |
| P-05 | Budgets blocked while prices go live (seen: B6 F14) | Push stops mid-afternoon | Price and budget rows load together; budget = plan clicks × price | Every funded term has a budget row [B6] |
| P-06 | Uniform TOS bump / blanket TOS shift; TOS falling as residue of a base cut; ranking at 0% TOS; orphan modifiers | Not derived; kills rank | Backward-solve per campaign; TOS held on base cuts | Flat-value share across a sized set ≤ 45% non-zero; no 0% ranking TOS [PF, WB, SR] |
| P-07 | Cuts > 15%/cycle when gradual; flat above-ceiling premium across the roster | Overshoots; not sized by rank gap | Caps per register #5; premium per row by rank gap | Step and premium audit [SR, PB] |
| P-08 | Base below the eligibility floor ($0.35–0.50) | Suppresses delivery | Floor ≥ clearing ÷ 10; ceiling wins if lower | Base ≥ floor [WB] |
| P-09 | Up-and-down doubling ignored ("$12.00 authorised click") | Real max CPC 2× the written price | Authorised price includes × 2 | Authorised-ceiling audit [SR] |
| P-10 | Budget cap reported as spend; empty new budget; round() instead of ceil() | Misstates exposure; under-funds | Committed = run-rate spend; budget ≥ required × 1.05, ceil | Budget column checks [WB, PF] |
| P-11 | Required clicks at a target CVR; DSTR ÷ CVR without organic netting; fractional DSTR; ladder + netting double count | Doubles spend ($5,595 vs $1,965/day) | Paid = DSTR − organic; clicks = paid ÷ achieved TOS CVR; DSTR ≥ 1 | organic + paid = DSTR ± 0.02 [PF, register #19] |
| P-12 | Amazon suggested bid used as the price | Anchors to Amazon's range | Break-even maths only | No suggested-bid source on any price [register #18] |

## B.7 Ranking

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| R-01 | Pushing where the ceiling is below what we already pay (seen: B6 F25) | Burns money without moving rank | Qualify only if ceiling ≥ own TOS CPC; else WAIT | Push rows: ceiling ≥ TOS CPC [B6] |
| R-02 | Listing problems pushed with money (seen: B6 F26) | More traffic loses more when the listing loses the click/sale | SQP ratio < 1.0 on ≥ 30 clicks → WAIT (listing) | Push rows pass the listing check [B6] |
| R-03 | Focus group overriding qualification (seen: B6 F06) | Biggest qualifying term tapered | Qualification per term before focus | Every qualifying term with a plan is PUSH or WAIT with a reason [B6] |
| R-04 | Inflated click forecast (seen: B6 F20) | Justifies unbuyable spend; fakes stock-outs | Credit steps with what steps of that size bought | Forecast ≤ step book [B6] |
| R-05 | Click requirements not reconciled to the product (seen: B6 F21) | Sum exceeds what the product sells | Scale to the product; volume/budget only, never price | Σ requirements ≤ product sales [B6] |
| R-06 | Cutting a ranking row in a DSTR deficit; bidding up a conversion deficit; traffic into a Conversion syntax | Cuts velocity rank needs; pays for a listing problem | Deficit → hold or raise; conversion → fix offer | No cut where orders/day < DSTR [SR, LTSF] |
| R-07 | Estimate treated as a gate; at-plan row called a failure; collapsing rank given a bid-up | Rank movement governs; collapse needs a cause | States A–F; State E never a bid change | Validation checks 3, 9, 10 [DR, PB] |
| R-08 | Capacity used as a disqualifier; rank target with no funded campaign called a plan; invented DSTR | Not a plan; no basis | 5-property gate (sized, dated, ceilinged, predicted, funded) | Every push row passes 5 properties [PF, PB, LTSF] |
| R-09 | Secondary syntax ranked; re-entering a ranking posture without a fresh realism pass | Spend outside the declared priority | Secondary = self-funding only; realism pass on re-entry | Ranking rows on secondary roots capped [PF, SR, PB] |
| R-10 | Paying for rank already held | Money with no rank to buy | HOLD RANK 2 weeks, then taper | At-target rows have no raise [B6, register #26] |

## B.8 Competitors

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| X-01 | Own listings treated as competitors; one ASIN targeted in several campaigns; price-mismatched targets beside conquest (seen: B6 F27) | Own-page targeting is defence/cross-sell; duplicates self-bid | Classify each ASIN (own product / own other / competitor / non-category / unmapped); one owner per ASIN | ASIN classifier column complete [B6] |
| X-02 | Bare ASINs; counting ASINs not brands; conflating visible vs account keyword totals | Overcounts rivals; misreads scale | Resolve brand for every ASIN; same brand = one competitor | No bare-ASIN tables [LP] |
| X-03 | Dismissing a quiet-but-equipped competitor; volume artifacts in totals | Recent pull-back may re-enter; totals inflated | Watch infrastructure mismatch; verify and exclude artifacts | Artifact list stated [LP] |
| X-04 | Competitor data setting a bid or price | Owner rule; prices stay break-even-based | Competitor data chooses terms, order, targets, read windows | No competitor rule sets or raises a price [B6 R-CI4] |
| X-05 | Conclusions about unmeasured competitors | Unknown ≠ absent | Report coverage (e.g. 13 of 32) | Every competitor claim states coverage [B6 R-CI12] |
| X-06 | Carrying an overturned finding ("2.71× market price, OUTPRICED" after the 74-ASIN pull showed 1.00–1.06×) | Wrong premise drives actions | Withdrawn-findings register | Findings trace to current pull [DR] |
| X-07 | Generic category terms pushed for volume; blocking a term that still sells and rivals buy | Push should be winnable core terms; block loses sales | Push only addressable core terms ranked on by a majority of measured rivals (B6: ≥ 7 of 13; register #46); REDUCE to break-even, not block (≥ 10 orders/90 d) | Push-term classifier; block-review list [B6 R-CI1, R-CI9] |

## B.9 Events and deals

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| V-01 | Deal not read (seen: B6 F01) | Deal changes margin (−20%), CVR and every read | Calendar gate before any rule | No build/fold on deal days; no verdict with > 2 deal days in window [B6] |
| V-02 | No goal, spend limit or clean baseline; baseline includes deal days (seen: B6 F03) | Forecast can't be judged; baseline ~80% high | Goal block before pricing; baseline excludes event/settling days | Push budgets + other spend ≤ limit [B6] |
| V-03 | New campaigns launched during a deal; two SB formats on one term (seen: B6 F17) | Learn on deal traffic; formats compete | No launches on event days; one SB format per term | Deal-day builds = 0 [B6] |
| V-04 | Structural folds mid-deal (seen: B6 F19) | Destroys history the post-event audit needs | Decide folds after the event | Deal-day folds = 0 [B6] |
| V-05 | Deal used to excuse a bleed; unflagged mid-deal cut | Real losses continue; confounded reads | Deal blocks gradual cuts only; bleed stops run; flagged | Bleed stops present in deal cycles [SR] |
| V-06 | Deal originates a push; in-deal CVR justifies a bid above the deal-state ceiling | Push without gates; overpays at lower margin | Gate the push first; ceiling at deal-state margin | Deal-state ceiling column [PB] |
| V-07 | Grading on deal weeks; cliff exit after an event | False verdicts; rank shock | DEAL_WINDOW; 3–5 day taper; 2-week guard | See reference 10 §5, §12 [SR] |

## B.10 Writing and deliverables

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| W-01 | Verdict with no arithmetic; metrics beside the verdict, not inside it | Reader can't follow or check | Numbers doing the work, inline arithmetic, reversal, re-read date | Reasoning contains the ceiling arithmetic [DR, PB] |
| W-02 | Templated verdicts; scripted output presented as the full record | "Shared rules are law; shared verdicts are templating" | Row-specific reasoning; state which fields are mechanical | > 5 rows with same status + same change % + same first 120 chars → review; string-compare duplicates [SR, PB] |
| W-03 | Internal codes, "this skill", version history, personal names in delivered text | Unreadable to owners; leaks process | Rule IDs only in workbook rule columns | Text search for §, rule codes, "this skill", versions [PB, register #28] |
| W-04 | Columns lost between revisions; duplicated sections; totals ≠ components; several files where one is expected | Contract broken; can't reconcile | Diff columns vs prior file; one consolidated file | Column diff; totals reconcile [DR, LTSF] |
| W-05 | Instruction written in a recording column (State); one verb for two operations; retired verbs; verdict with no entity | Undeployable or ambiguous | Grammar: `BID $x → $y`, `MODIFIER n% → m%`; action = cells | Action vs cell values match [WB] |
| W-06 | Unnamed soft coefficients; untagged multipliers; false precision; implausible forecasts; promising ACoS cuts in an invest week | Unfalsifiable | Name soft coefficients; ranges; basis tags | Every projection has a basis tag [PB, LTSF, AP] |
| W-07 | Inventing or contradicting the decision sheet in a write-up; padding sections without evidence | Report diverges from what ships | Explain the sheet's logic; sections only with evidence | Report actions = workbook actions [AP] |
| W-08 | Numbers without source and date | Can't be checked | Source + window on every figure | Figure-source audit [PB, LTSF] |

## B.11 Process and engineering

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| G-01 | Withheld rows exported as changes (seen: B6 F15) | Loader applies what the engine declined | Export filter on verdict | Exported rows ⊆ changed verdicts [B6] |
| G-02 | Uploading before approval; shipping without log + upload file | Unreviewed changes; no history | Zero-failure validation → approval → upload | Approval record before upload [SR] |
| G-03 | Grading undeployed actions; blaming un-uploaded recommendations | False failures | Execution verification first | Execution status on every grade [SR, WB, LTSF] |
| G-04 | Repeating a dead lever a 3rd time | Known-failed spend | Escalate after 2 | No lever with 2 failed grades re-issued [SR] |
| G-05 | Confounded reads: two levers in one window; windows straddling a lever change | Can't attribute | One lever per window | Window vs change-date check [LTSF] |
| G-06 | Owner override or reviewer mark silently reverted on regeneration | Breaks trust; loses decisions | Overrides persist | Override register diff [PB] |
| G-07 | Gate that passes the defect; PASS beside non-zero fails; check scoped to one tab; self-reported gate | False assurance | Gate must fire on a known-bad case; coverage over every action tab | Self-test with a known-bad row [WB] |
| G-08 | Answerable gap logged as "revisit next cycle"; provisional rule applied "with a flag" instead of asked | Delays a decision the owner could make now | Ask once; ask before first use | Q&A log [PB] |
| G-09 | Bulk file defects: extra sheets, blank State, numeric dates, names > 128 chars, symbols in keywords, formulas/NaN, guessed IDs, keyword-group targets in bulk, file re-saved in Excel, re-uploading succeeded rows | Upload fails or cascades | Bulk canon; fix-file of failed rows only | Upload gate prints all pass [CB] |
| G-10 | Known source-code defects copied: freeze/backfire branches crash (undefined variables), freeze/floor never recorded; fresh clicks = cycle total; zero-order branch negates exact ranking terms; turn-off thresholds doubled twice; column-name mismatches blanking log fields; syntax roll-up reading a column never written; "KING" parsed before "CALKING"; silent break-even 0.1986; tolerance bug (0.9 × 1.1 ≈ 0.99 bar); DOH rename disabling inventory gates; duplicate log rows; single-metric verify | Silent wrong decisions | Implement the rules in this skill, not the code; regression tests for each | Regression suite covers each item [SR, DE, register §3] |
| G-11 | Formulas unconverted (LET → #NAME?); CSV exported before recalc; renderer recomputing steps | Broken or divergent numbers | Values only; recalc before export; render from the decided record | Zero formula errors [MDB, WB] |

---

## Open questions for the owner

1. **Turn-off thresholds (A-33):** the SR code doubles the objective turn-off level twice; the framework intent listed here (Ranking 100%, Market Share 50%, Discovery 60%, Profitable Conversion 50%, Defensive/PAT 30%) is inferred from the source notes, not stated by register 13. Confirm the levels.
2. **Zero-order rule vs silent-hold list:** (decision labels per 13 #38: REDUCE with a live owner, REVIEW without.) The house rule "≥ 20 clicks, 0 orders → REDUCE (owned)" is not on the PB exhaustive silent-hold list, but it is a REDUCE, not a HOLD, so no ask is triggered. Confirm this reading.
3. **Conversion deficit (A-34):** Resolved — see 13 #39: bid −15% and refer to Brand Management; no rank push until the offer is fixed.


---

<!-- FILE: references/12-writing-and-deliverables.md -->
# FILE: references/12-writing-and-deliverables.md

# 12 — Writing standard, deliverables and the quality gate

Read at Phase 10, and again before writing any reasoning cell. Everything here applies to every product; B6 numbers appear only as labelled examples.

## Contents
1. Writing standard (voice, reasoning chain, mandatory elements, banned content)
2. Action-string grammar
3. The decision trail (format + 3 filled examples)
4. Finding / Why it matters / Action / Expected impact (thesis and execution sequence)
5. Forecasting rules
6. Deliverables (decision document, decision workbook, competitor workbook, change review sheet, upload file, Google delivery)
7. Quality gate — consolidated checklist (run last, all must pass)
8. Open questions for the owner

---

## 1. Writing standard

### 1.1 Voice
1. Plain language for an owner who is not a PPC analyst. Short sentences. Name the thing ("product pages", "top of search"), not the jargon ("PDP", "TOS") in narrative text; abbreviations are fine in workbook column headers once defined in the Metrics dictionary. [B6, AP]
2. Write in the analysis's own voice: "this is the account's convention", never "this skill decided". [PB 23A]
3. Every verdict is falsifiable: it says what should happen, by when, and what would prove it wrong. [SKILL]
4. Say "this is a [waste / placement / visibility] problem, not a [demand / supply] problem" when the distinction drives the action. [AP]
5. End each diagnostic table with one **Conclusion** line that names the action it leads to ("What this table decides"). [AP, PB]
6. Measured vs estimated is stated in the text ("measured, 90 days" / "estimate, labelled proxy"). Conflicting sources → show both and name the one that governs. [LP, PB]
7. Missing value → "—" or "Not available", never 0; unmeasured ≠ zero. [all]

### 1.2 Reasoning chain — every reasoning cell, in this order [DR, PB]
1. **What is happening** — the row's current state in numbers (window stated).
2. **History** — what was done before, when, and whether it worked (grade from the impact ledger).
3. **Market** — SQP / competitor context for this term or target.
4. **Objective** — which objective the campaign has and which metric judges it.
5. **Actual vs estimate** — delivery vs plan (clicks, orders, rank); estimates size direction, rank movement governs.
6. **Action** — the exact change (action-string grammar, §2).
7. **Why this lever, not the adjacent one** — name the alternative considered (placement vs budget vs price vs listing vs colour) and why it loses.
8. **Why it is economically safe** — ceiling arithmetic inline; loss bounded; stock covers it.
9. **What reverses it, and when it is re-read** — a condition and a date.

Cold-reviewer test: a first-time reader must be able to answer, without a follow-up question, *what changed, why these numbers justify it, what would make it wrong*. Real numbers that do not connect to the verdict fail the test. [PB 17A]

### 1.3 Mandatory elements
| # | Element | Example (B6) | Source |
|---|---|---|---|
| 1 | **Named numbers doing work** — each number is inside the argument, not beside it; state the comparison and the ratio | "converts 19.1% at the top against a market of ~2% (≈9×)" | DR anti-pattern 1 |
| 2 | **Dated sources and windows** on every figure | "Sellerboard, 27 Aug–25 Sep"; "30 days to 29 Sep" | PB, B6 |
| 3 | **Rank arc** prior → recent → current, with the source of each and which one governs; overall, 14-day and 7-day stated separately; clean arc governs over deal arc | "27 (end Aug) → 33 (deal start) → 55 (29 Sep), daily crawl" | DR, PB |
| 4 | **Placement split before any bid** — top / rest / product pages share of clicks (and CVR where it decides) | "39% top / 56% product pages on 776 clicks" | DR, WB |
| 5 | **Ceiling arithmetic inline** — margin × CVR = break-even; × 2 = ceiling; price vs both | "$15.97 × 19.1% = $3.05; ceiling $6.10; today $6.10" | DR, B6 |
| 6 | **Why this lever, not the adjacent one** | "base cut, not a boost raise: the boost only applies at the top and the campaign isn't winning there" | DR, B6 |
| 7 | **Reversal and re-read** — condition + date | "restore one step if rank falls >10 places; read 8–14 Oct" | DR, PB |
| 8 | Previously flagged conditions on the row named (listing flag, rank drop, deal, stock) | "listing flag stands (CVR 0.68× market)" | DR |
| 9 | On cuts: auction density (how many rivals advertise the term) and opportunity cost | "11 rivals advertise it; 61 orders in 90 days → reduce, not block" | PB, B6 R-CI9 |
| 10 | On ranking premiums: inventory zone and stock cover beside the push | "King White 1,388 Available, 133 days" | PB |
| 11 | Formula-only corrections (thin data, over ceiling) name two reversal tests: converts once clicked AND gets clicks at all | — | PB |
| 12 | Confidence where thin; soft coefficients named with when/how they will be measured | "credit +5–15% steps with 0.85× net of drift (from own step history)" | PB 22 |
| 13 | Grade of the prior action on the same row (worked / flat / backfired / too soon / not executed) | — | SR, PB |

### 1.4 Banned in delivered text
| Banned | Why / test | Source |
|---|---|---|
| Internal codes: "§", rule IDs (R-P3, E15, S-C1), "State E", "PROVEN tier", "the sufficiency stop", gate numbers — even in parentheses | Owners can't decode them. **Rule IDs are allowed only in the workbook's Rule / Logic columns** | PB 23, register #28 |
| Tool, script and run names in narrative (script/function names, run IDs, "the engine's stage 7") | Data sources are named in source lines and captions ("Sellerboard", "search query data", "rank crawl"); internal tooling is not | PB 23 |
| "this skill", "not derived by this skill" | Self-reference | PB 23A |
| Version narration ("restored after the rewrite", "v5") | The document's own version number in the title block is fine | PB 23B |
| Personal names | Use roles: "the product owner", "the PPC manager", "the reviewer" | PB |
| Tracked changes, redlines, "we changed our mind" narrative | Deliver the clean current position; withdrawn findings go to the register with the overturning evidence | PB, DR 11 |
| Verdict without arithmetic; blended figure where a placement figure exists; estimate used as a gate | DR prohibited list | DR |
| Generic advice ("consider optimising bids") | Fails the bar in SKILL.md | SKILL |
| Templated reasoning: identical text (or identical except the row's own name) across rows of one entity type | String-compare every reasoning cell | PB 16, SR |

### 1.5 Number conventions
- Prices and bids $0.00; budgets $0; ACoS/CVR/CTR/share 0.0%; ranks integers; ratios "0.68×".
- Top-of-search price is always written as **TOS price = base × (1 + boost)**, with base and boost shown when either changes.
- Every % change shows its base: "$5.93 → $7.71 (+30%)".
- A value that does not change is left blank in "new" columns (same-value → blank). [WB]

---

## 2. Action-string grammar

One string per entity (keyword, target, placement, campaign, ad). Decision label first, then every changed value as before → after, then timing/how.

```
<DECISION> — <lever> <before> → <after> (<±%>)[; <lever> <before> → <after>] — <when / how it loads>
```

| Case | String (B6 example values) | Rule |
|---|---|---|
| Price with pair write | `PUSH — TOS price $5.93 → $7.71 (+30%): base $1.37 → $1.03, boost 333% → 649% (one write); budget → $156 — load now` | Base and boost of one campaign are one backward-solve [PB, B6] |
| Cut to ceiling | `CUT — TOS price $8.43 → $6.24 (−26%, to ceiling): base $1.87 → $0.94, boost 351% → 564%` | Over-ceiling never deferred [B6] |
| Staged move | `BREAK-EVEN — TOS price $6.06 → $3.03 (−50%) now → $2.77 on <date>` | Gap > cap = dated steps [PB, WB] |
| Hold | `HOLD RANK — TOS price $5.18 held; base $2.50 → $1.88, boost 107% → 176%` | Reason must be on the mechanical list or asked [PB 24] |
| State change | `RESTART — enable campaign; bid blank (unchanged) — 1 Oct` | State changes leave the bid blank on purpose [DR] |
| Duplicate | `DEDUPLICATE — pause; owner is <campaign>` | Nothing else changes on the loser [PB] |
| Negative | `BLOCK — negative exact "silk sheets" in <discovery campaigns> — reactive` | Mode named: pre-load / reactive / steering [PB] |
| Harvest | `HARVEST — build Exact "<term>" at $<BE> on <SKU>; negative exact in <source>, same upload — <date>` | [PB, B6] |
| Ad switch | `SWITCH AD — Queen Olive → Queen White (same size), by hand, before the price loads` | Size never changes [B6] |
| Owner call | `REVIEW — owner: raise ceiling $6.10 → $7.63 until 14 Oct, or hold $6.10` | Time-boxed [B6] |
| Placement only | `MIX FIX — base $1.60 → $1.20, boost 281% → 408%; TOS price $6.10 held` | Boost raise without the base pair is refused when product pages >20% [B6] |

Rules: never write instructions into the State column; retired verbs "RE-ROUTE" and "HOLD ENABLED" are not used; one lever per entity per cycle except the base+boost backward-solve; an action string must equal the values in the row's New Bid / New % / New Budget cells. [WB, DR]

---

## 3. The decision trail

Every campaign, keyword and competitor-target row carries this trail (workbook columns; narrative examples in the document use the same order without rule IDs).

| Step | Contents | Test |
|---|---|---|
| **Input** | Raw facts with windows: clicks, orders, spend, ACoS (30/90 d), placement split, price (base × (1+boost)), advertised SKU, rank now → target, stock | Every figure has a window and a source |
| **Metric** | The derived numbers that decide: break-even = margin × CVR (basis stated: own ≥50 / blend 15–50 / size <15), ceiling, push price, ACoS vs BE, PDP share, SQP ratio | Recomputes from Input |
| **Logic (rule)** | The gate that fired (master decision order) and the rule(s) applied; **rule IDs allowed here only** | First gate that fires is named |
| **Decision** | One label: PUSH / WAIT / HOLD RANK / BREAK-EVEN / CUT / MIX FIX / DEFEND / HARVEST / REDUCE / BLOCK / DEDUPLICATE / CHECK OWNER / MONITOR / RESTART / KEEP / REVIEW / SCALE / MAINTAIN (targets: OFFENSIVE / TEST / AVOID / LOW TRAFFIC) | Exactly one |
| **Action** | Action string (§2) | Equals the New cells |
| **Expected outcome** | Metric, direction, magnitude, horizon (a range, §5) | Falsifiable |
| **Validation** | Date(s), pass condition, fallback if it fails | Has a date and a fallback |

Full worked set (10 scenarios): `templates/decision-trail-examples.md`.

### Example 1 (B6) — head term already at its ceiling
| Step | Detail |
|---|---|
| Input | "bamboo sheets" exact, 30 d: 776 clicks, 119 orders, $3,037, ACoS 31.7%; 39% top / 56% product pages; top-of-search impression share 2.4%; TOS price $6.10 = $1.60 × (1 + 281%); advertises King White (1,388 Available, 133 days); rank 26 → target 9; plan 69 top-of-search clicks/day, getting 10; our TOS cost per click $5.66. |
| Metric | Break-even $3.05 = King White $15.97 × 19.1% (own TOS CVR, 90 d, ≥50 clicks); ceiling $6.10; premium (26 ÷ 9 − 1) × 50% = 94% → push price $5.93; market CVR ~2%. |
| Logic (rule) | Qualifies on all push gates (demand, CVR above market, reach, stock, live, ceiling ≥ cost) [R-P1]. Price $6.10 sits between push price and ceiling → hold [R-P4]. Product pages 56% on ≥15 clicks and they sell → base −25%, boost re-solved [R-M1]. At ceiling for weeks without holding the top → owner [R-P6]. |
| Decision | PUSH (at ceiling) + REVIEW (owner ceiling decision). |
| Action | `MIX FIX — base $1.60 → $1.20, boost 281% → 408%; TOS price $6.10 held; budget → $201` + `REVIEW — owner: ceiling 2.5× = $7.63 until 14 Oct, or hold $6.10`. |
| Expected outcome | Top-of-search share of clicks rises from 39% toward 70%; impression share up from 2.4%; organic rank moves within ~5–19 days of the clicks landing. |
| Validation | Daily: impression share and sponsored rank. Day 7: placement split (product pages >20% → cut base again). 8–14 Oct (settled): rank vs 26. Stop if TOS CVR falls below market on 50+ clicks. |

### Example 2 (B6) — non-ranking campaign over break-even on both windows
| Step | Detail |
|---|---|
| Input | "red bamboo sheets" exact (colour term), advertises Queen Burgundy; 30 d: 45 clicks, 5 orders, $120.29, ACoS 30.5%; 90 d ACoS 33.2%; base $1.12; tagged Ranking. |
| Metric | Break-even ACoS 23.8%; over on 30 d AND 90 d; cut = 1 − 23.8 ÷ 30.5 = 22% (≤30% cap). |
| Logic (rule) | Colour term → Profitable Conversion, not Ranking [R-O1, E18]. Over break-even on both windows, ≥15 clicks → base cut ≤30% [R-N1]. Colour-named term keeps its colour [R-C3]. |
| Decision | CUT (objective retag to Profitable Conversion). |
| Action | `CUT — base $1.12 → $0.87 (−22%); objective Ranking → Profitable Conversion`. |
| Expected outcome | ACoS toward 23.8% with orders held within about −30%. |
| Validation | 14 settled days after the cut: ACoS and orders; if orders fall >30%, restore half the cut. |

### Example 3 (B6) — brand broad: defend and hold the negatives
| Step | Detail |
|---|---|
| Input | Brand broad ("Decolure"), 30 d: 621 clicks, 123 orders, ACoS 11.7% (most profitable campaign on the product); advertises Queen Olive; tagged Discovery. Proposed: brand negatives added to it. Receiving brand exacts: Queen 2 clicks in 30 d on Queen Olive; King 33 clicks. |
| Metric | ACoS 11.7% vs break-even 23.8%; receiving campaigns not defensive-ready (wrong colour, no volume). |
| Logic (rule) | Brand broad → Defensive [R-O2]; keep on its history colour, Queen White [R-N3]; brand negatives only when receiving exacts are defensive, on the hero, funded [R-S4, E10]. |
| Decision | DEFEND. |
| Action | `DEFEND — objective Discovery → Defensive; SWITCH AD Queen Olive → Queen White by hand; brand negatives held`. |
| Expected outcome | Brand orders held (~123 per 30 d at ≤ break-even ACoS). |
| Validation | Brand exacts serve on White with budget for 7 days → then load the negatives; weekly brand-term share and orders. |

---

## 4. Finding / Why it matters / Action / Expected impact

Every section of the decision document is built from items in this four-part form. [AP]

| Part | Content | Rule |
|---|---|---|
| **Finding** | The real figure, dated | Never a generality |
| **Why it matters** | The mechanism: profit, rank, velocity, inventory, share or efficiency | Say which one |
| **Action** | The exact change with the target value from the workbook | Never invent or contradict a workbook decision |
| **Expected impact** | Magnitude-appropriate range and horizon (§5) | Directional labelled as such |

Number actions within a section (Action 5.1, 5.2 …) so the Next steps list can cite them.

### 4.1 Thesis (decide first; it governs every section) [AP]
Read the signals: ACoS vs break-even; TACoS trend (monitor only unless owner target); inventory (in-stock SKUs, cover, stock-out-before-arrival); top-of-search impression share; velocity vs peak; rank week on week (terms up vs down, % at target); wasted-spend share vs 10% (discovery 40%).

| Thesis | When | What the document leads with |
|---|---|---|
| **INVEST / DEFEND** | Profit green, inventory green, waste low, but visibility / rank / velocity slipping | Lift top-of-search on priority ranking terms (placement-first), fix BOTH-FAILING syntaxes before scaling, seal concentrated leaks, expand only proven syntaxes. ACoS may tick up — say so and bound it |
| **PROTECT-AND-CUT** | Over break-even, high waste, or stock-out risk | Protect at-risk SKUs (routing, backup switches), kill waste, reallocate off losing placements, fund starved winners, expand only proven syntaxes |

State the thesis in the Summary with **one binding constraint** (e.g. B6: "the push is capped by price, not money — 11 of 13 funded terms are at or near their ceiling on day one").

### 4.2 Execution sequence [AP]
Order actions and the Next steps list: **protect revenue → stop bleeding → reallocate → expand.**
1. Protect revenue: stock routing, hero colour on ranking ads, brand defence, over-ceiling cuts on converting rows.
2. Stop bleeding: over-ceiling prices, zero-order waste, over-break-even non-ranking cuts, placement leaks.
3. Reallocate: mix fix, fund budget-truncated winners, push budgets within the limit.
4. Expand: harvests, seeds, discovery builds, tests (after events, never on deal days).

### 4.3 Summary block
3–4 prose paragraphs (condition + thesis + binding constraint; 2–3 root causes; offence vs clean-up split from wasted-spend share) → the decisions list → "Needs your decision" (numbered, each with options and trade-off in reviewer units, e.g. "holds ~$180/wk of saving to keep ~66 orders/wk") → a headline-numbers box of 6–8 KPIs with windows. [AP, PB]

---

## 5. Forecasting rules

1. **Ranges, not false precision**: "ACoS ~38–42%", not "39.7%". [AP]
2. **Anchored**: every forecast starts from a workbook figure with its window; say which. [AP]
3. **Settled baselines**: exclude deal days and the 7-day attribution tail; exclude stock-out and re-route stretches. Example (B6): a baseline of $515/day included four deal days; normal spend was ~$283/day. [B6 F03, SR]
4. **Credit steps with what similar steps bought** in the product's own history; nothing for paused keywords, retags or capped steps. Example (B6): +5–15% steps bought 0.85× clicks net of drift; a +75% jump credited with 2.5× clicks was not supported. [B6 F20]
5. **Requirements set volume and budget, never price**; reconcile summed click requirements to what the product sells before presenting them (B6: plan 187 TOS clicks/day ≈ 36 orders/day vs ~30 in the deal and 14 before it → a plan to grow toward, not a day-one forecast). [B6 F21]
6. **Typical magnitudes** (directional unless measured): a clean placement or negation fix moves the affected entity's ACoS 5–15 points over 1–2 cycles; coverage expansion +10–15 points SV-weighted coverage; funding a starved campaign buys a clean read (15+ clicks), not instant ROI; total spend roughly flat when reallocating. [AP]
7. **Name every soft coefficient** (uplift, elasticity, organic share proxy) and when it will be measured. [PB 22]
8. **Ranking pushes state their loss ceiling** = (push ACoS − break-even ACoS) × projected sales at the required spend, and state the payback (organic units once rank holds). [PB, B6]
9. **Spend forecasts** = today's spend moved by the price change, capped by budgets and the spend limit; show expected vs limit. [B6]
10. **Cut batches** carry an opportunity-cost check: projected lost-order value vs spend saved, at the more conservative (deal-state) margin; withdraw cuts that fail. [PB 21]
11. Never promise ACoS cuts in an INVEST week; never round implausibly. [AP]

---

## 6. Deliverables

### 6.1 Decision document (Word or Google Doc)
Skeleton: `templates/report-outline.md` (17 sections + appendix). Minimum: Summary with decisions and what needs the owner · How to read this · Where things stand · Rules applied · Goals and spend limit · Calendar / transition plan · area sections in Finding → Why → Action → Impact form · Competitive landscape (with coverage) · Tests · Exceptions · Next steps with dates · Appendix of engine/process fixes. Every major table followed by "What this table decides"; charts titled with the finding, direct labels, threshold bands shaded. Last two content sections: risks/falsification (dated checks) and numbered decisions requested. [SKILL, PB, AP]

### 6.2 Decision workbook (xlsx)
Full tab-by-tab spec with columns: `templates/workbook-spec.md`. Required tab set and purpose:

| Tab | Purpose | Key columns (full list in spec) |
|---|---|---|
| Start here | What the workbook is, sources and windows, how to read the trail, tab index | Tab · What it answers |
| Overview | Spend vs limit, decisions at a glance, needs the owner's decision | Line · $ a day · Basis; Decision · count |
| Metrics dictionary | Every metric used | Metric · Family · Meaning · Formula · Source · Window · Validation · Thresholds · Influence · Pitfalls |
| Decision rules | Every rule applied | Rule ID · Family · Applies to · IF · THEN · Threshold · Why · Guardrail · Exception |
| Decision trails | Worked examples end to end | Step · Detail |
| Campaign decisions | Every campaign, one decision, full trail | Identity · Objective now → correct · Input · Metric · Logic (rule) · Decision · Action · Expected · Validation · When · How it loads · metrics |
| Keyword decisions | Every search term with spend | Term · Decision · Rule · Why · Action · Class · Relevancy · SV · Rank · Target · Indexing · Owner · 30/90 d funnel · placement |
| Harvest & negate | Keyword actions grouped | Term · Class · Relevancy · Clicks/Orders/ACoS/Spend 90 d · Owner · Action |
| Push plan | Funded / waiting / at-target terms | Status · Term · Rank → target · TOS CVR · BE · Push price · Ceiling · TOS CPC · Price now → write · Base/Boost · Plan clicks · Budget · Why |
| Placement | Campaign × placement read and mix fix | Shares · CVR · CPC per placement · Read · Base/Boost/Price now → new |
| Variation & stock | Preferred / backup / clearance per size; per-SKU margins | Size · Available · Pace 7/30 · Cover · Next arrival · Verdict · Backup · Clearance |
| Inventory × PPC | How stock gates each decision | Step · Check · Rule |
| Financial guardrails | Break-even, ceilings, limits, per colour | Guardrail · Formula · Value · Crossed when · What happens |
| Competitor landscape / profiles / keywords / ASIN targets / gaps | See 6.3 (inside the workbook or as a separate file) | — |
| Exceptions & BLOCK | No-automatic-change conditions with current cases | Code · Condition · Treatment · Scope · Current cases |
| Validation plan | Checkpoints | When · What · Metric · Pass · Fallback · Rule |
| Checks | Integrity checks computed from the workbook | Check · Result (derived) |

Also, when relevant: Data conditions register; Impact ledger / prior-cycle grades; Source rows (every engine/audit row with a verdict); New campaigns & restarts; By hand (colour switches, objective tags, budgets); Before → After; Failure register. [WB, PB, B6]

### 6.3 Competitor workbook (optional separate file)
Use when the competitor pull is large or the reader differs. Tabs: Competitor landscape (patterns, sources & limits, market size/share, traffic trend, placement reach, segments, niche benchmarks, price ladder) · Competitor profiles · Hero ASINs & trends · Competitive keywords · Push terms vs field · Gaps & how to fill · Competitor ASIN targets (OFFENSIVE / TEST / AVOID) · Competitor → decisions (influence rules; what each never changes) · Landscape check. Every tab states coverage (measured of mapped competitors) and export dates. Resolve every ASIN to a brand. [B6, LP]

### 6.4 Change Review Sheet (own file, generated last)
- One row per (target, lever), sorted by exposure ($/day at stake). Actions copied verbatim from the workbook. [WB]
- Columns: identity (campaign, target, SKU) · funnel (impr, clicks, orders, spend, window) · placement split · ceiling and price multiple before/after · before / after / Δ · argument (why; why not the alternative; effect + when; reversal) · exposure · **Reviewer decision** (approve / reject / modify) · **Reviewer note** (both blank).
- Reviewer marks are applied literally and persist through every later regeneration (a reverted mark is a gate failure). [PB 19]
- Rows that must go to review: any gate failure; structural change (campaign, routing, match type, strategy); bid move >25% outside an approved push plan (the plan's own +30%/day steps are covered by its approval); budget move >$50/day; search volume ≥ 500 (register #41, #54). State the trade-off in reviewer units. [PB, WB]

### 6.5 Upload file
Only rows that change; true Bulksheets 2.0 layout (one sheet `Sponsored Products Campaigns`, exact 54-column header, State on every row, IDs as text, dates as text `yyyyMMdd`, no formulas/NaN, names ≤128 chars, no symbols in keyword text); price and budget rows of one campaign load together or not at all; withheld rows never exported; colour switches and SB/SD builds listed "by hand". Tell the user to upload directly without re-saving in Excel/Sheets. [CB, B6 F14–F15]

### 6.6 Google Docs / Sheets delivery
- **Connector limits**: creating a Google Sheet from CSV gives **one tab per Sheet and no formatting**. Either one Sheet per workbook tab, or one Sheet per file with sections stacked under a title row ("■ Tab name"), a blank row between sections.
- Split any payload over ~90,000 characters into parts, repeating the header row in each part. Prefix cells starting with `=`, `+` or `@` with a space so they are not read as formulas. Write $ and % values as formatted text (the CSV carries no number formats). Truncate very long reasoning cells only with a visible "…". [B6]
- **For the full workbook with formatting and all tabs, upload the .xlsx to Drive and open/convert it with Google Sheets (Drive import)**; use CSV Sheets only for quick views.
- Docs: upload the .docx and convert, or write natively; check tables and headings survive conversion.
- Link every delivered file in the reply; say which version governs if Doc and xlsx differ (the workbook governs row-level numbers). [PB]

---

## 7. Quality gate — consolidated checklist

Run as a separate pass over the finished files, as if reviewing someone else's work. Every check returns a count; **all must be 0 failures**. Fix the cause, not the row, then re-run the whole gate. Record RAN / NOT RUN per check; the Checks tab result is computed from the count, never typed; "PASS" beside a non-zero count is itself a failure. [PB, PF, WB]

### 7.A Inputs and data validity
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| A1 | Every requested input received or confirmed N/A | Intake checklist complete | No blank "Received" | PB, QA |
| A2 | Every sheet of every file enumerated and read | Status per sheet READ-FULL / READ-PARTIAL / NOT-RELEVANT / NOT-OPENED | No relevant sheet NOT-OPENED | WB |
| A3 | Sources reconciled | Bulk vs Command Center spend; Sellerboard units vs orders; on-hand − available − reserved | Differences explained; inventory gap ≤5 units or verified | SKILL, PB |
| A4 | SQP aggregated correctly | Market columns taken once per query, brand summed; rates recomputed | Brand ≤ market; shares 0–100% | SQP |
| A5 | Targets recompute | Target CTR = market CTR × 1.10; keyword target CVR = market CVR × 3.0 | Drift ≤2% on ≥90% of rows | SR, PF 1 |
| A6 | Quarantine applied | Rows with CVR/ACoS on 0 orders, CTR on 0 impressions, conflicting sources | No recommendation on them; refresh task logged | PB, DR |
| A7 | SKU provenance checked | Every performance verdict's window has advertised-SKU check (match / mismatch / mixed) | 0 verdicts without it | PB 15 |
| A8 | Economics fresh and per SKU | Margin age ≤45 days, no price/fee/packaging change since; no global default | 0 stale or defaulted rows | PB, SR |
| A9 | Missing ≠ zero | Search for 0 in fields with no source value | 0 | all |
| A10 | Event windows excluded | Verdicts using a window with >2 deal days; last-7-day attribution unflagged | 0 | B6 F01, E2 |
| A11 | Scope complete and clean | Campaigns spending on the product but missing from the list; shared multi-product campaigns under automation | Missing ones added and marked; shared ones excluded | B6 F13, F29 |
| A12 | Labels and totals | Blank syntax/SV/objective rows dropped; paused-ad-group rows with spend; keyword + target spend vs advertised-product report | Flagged, not dropped; totals match | PF 3–5 |
| A13 | DSTR feasible | Stated DSTR vs market purchases/30 | >50% re-scoped with reason | PF 2 |

### 7.B Objectives and structure
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| B1 | One objective per campaign | Count distinct objectives per campaign block (PT rows in keyword campaigns excepted) | 0 blocks with >1 | DR 1, OC |
| B2 | Objective present and consistent with targeting | Blocks with none; Defensive without brand keyword; Ranking without Exact; PT tagged Ranking | 0 | OC, WB |
| B3 | No Ranking on colour / competitor / other-language / misspelled terms | Classifier tokens vs objective | 0 | B6 E18 |
| B4 | One live bid-carrying instance per term | Normalised term (word order kept, plural/symbol merged) across enabled campaigns | 0 without a coexistence reason | DR 4, PB |
| B5 | Restart before build | New builds on terms with an existing exact (live or paused, close variants) | 0 | B6 E11 |
| B6 | No bids on non-deliverable rows | Bids on paused keyword/campaign, withheld duplicates, non-serving ads, Red / 0-stock SKUs (unless substitute) | 0 | DR 7, PF 17–18 |
| B7 | No structure on event days | Builds, folds, brand negatives dated inside a deal | 0 | B6 E1 |
| B8 | Brand negatives gated | Brand negatives added before receiving exacts are defensive, on the hero, funded | 0 | B6 E10 |
| B9 | Re-enables deduplicated | Duplicate check run on the post-re-enable population; re-enable and bulk in one upload | Yes | PF 21 |
| B10 | Modifier ↔ keyword pairing | TOS modifier with no funded keyword; funded ranking keyword on a 0% modifier | 0 | PF 20, WB |
| B11 | Only allowed columns changed | Diff source bulk vs output: only decision columns (and approved state/ad ops) differ; rows in = rows out; spend to the cent | 0 other diffs | PF 6–8, OC |

### 7.C Economics and pricing
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| C1 | Break-even per advertised SKU | Each row's break-even = that SKU's margin × its CVR basis; no blended parent; deal price in deal | 0 mismatches | SKILL, B6 F02 |
| C2 | No price above its ceiling | Ranking TOS price ≤ 2 × break-even CPC (or owner's time-boxed raise); non-ranking bid and effective price ≤ 1.0 × break-even at every placement; Sponsored Brands / video per register #45; LTSF clearance ≤ 1 × forward-cash break-even (#43) | 0 | DR 5–6, PB 5, PF 13–15 |
| C3 | Above-break-even ranking authorised | Ranking rows above break-even without goal-gate clearance, or past the sufficiency point | 0 | PB 6 |
| C4 | Over-ceiling cut now | Rows above ceiling left in place or deferred | 0 | B6 F05 |
| C5 | Arithmetic recomputes | base × (1 + boost) = TOS price ±$0.03; every stated figure recomputed | 0 mismatches | PF 12, DR 13, PB 13 |
| C6 | Amazon limits | Boost >900%; base < price ÷ 10 on capped rows | 0 | B6 |
| C7 | Step caps | Push raise >+30%/day; other raise >+25%/cycle; gradual cut >15%/cycle (decisive ≤50%); base cut >50%; non-ranking cut >30% | 0 (caps, not targets) | B6, SR, PB |
| C8 | Strategy unchanged unless decided | Bidding-strategy diffs | 0 without fixed-bid-trial approval | B6, register #8 |
| C9 | No outside price anchors | Prices citing suggested bids, competitor CPCs or click requirements | 0 | register #18, B6 F21 |
| C10 | Deal-state ceiling respected | In-deal CVR used to justify a price above the deal-state ceiling | 0 | PB |

### 7.D Placement
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| D1 | Placement split before bids | Price rows without the campaign's placement split in reasoning | 0 | DR |
| D2 | Mix fix paired | Ranking campaigns with product pages >20% on ≥15 clicks given a boost raise without the base cut in the same write | 0 | B6 R-M1 |
| D3 | No TOS residue | Ranking TOS price lowered only as a side effect of a base cut | 0 | WB |
| D4 | Thin placement comparisons labelled | Two-rate comparisons with n <30 not marked "directional" | 0 | PF |

### 7.E Ranking and push
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| E1 | Qualifying terms decided | Terms passing every push gate not PUSH or WAIT-with-reason | 0 | B6 F06 |
| E2 | No unqualified push | PUSH on Red/Yellow stock, ceiling < own TOS CPC, listing flag, below-floor sample | 0 | SKILL, B6 |
| E3 | Rank collapse not funded | Rows that lost >10 places given a bid increase | 0 | DR 9 |
| E4 | At-plan not called failure | Delivery 95–120% of plan labelled failure / "estimate low" | 0 | DR 10 |
| E5 | Out-of-scope honoured | Ranking verdicts with <1 month rank history or no sized plan | 0 | DR 11 |
| E6 | No contradictory directions | Same term priced up in one campaign, down in another | 0 | DR 12 |
| E7 | Push terms complete | Target rank, date, clicks/day, budget, first milestone, re-read date on every push term | All present | PB, B6 |
| E8 | Sizing arithmetic | DSTR ≥1; organic + paid = DSTR ±0.02 (organic labelled proxy); clicks = paid ÷ own achieved TOS CVR; budget ≥ required × 1.05 (rounded up) | 0 failures | PF 9–11, 19, register #19 |
| E9 | Provisional rules confirmed | First use on this product of a provisional rule without a recorded confirmation | 0 | PB 25 |
| E10 | Holds justified | HOLD outside the mechanical list (both quality gates fail, CTR pass + CVR fail, zero delivery, budget truncation, plan > capacity) without a recorded ask | 0 | PB 24 |
| E11 | Infeasible plans escalated | Budget-infeasible plans not escalated; roster minimum budgets above cap without a pacing plan | 0 | DR 8, PB 18 |

### 7.F Inventory and variation
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| F1 | Stock gates on post-change state | Zone and stock-out-before-arrival computed after the planned change, 30-day pace | 0 pushes failing | SKILL, B6 F30 |
| F2 | Size locked | Ad switches that change size (except correcting a wrong size) | 0 | B6 E9 |
| F3 | Near-out colours kept out | SKUs with <7 days cover added to any ad | 0 | B6 R-C5 |
| F4 | Routing correct | Ranking ads on the size's best seller (or dated backup); discovery on the clearance colour; colour-named terms on their colour; routing read from Product Ad rows | 0 exceptions without reason | B6, WB |
| F5 | Economics rebuilt on reroute | Rerouted rows still priced on the departing SKU | 0 | PB |

### 7.G Budget and spend
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| G1 | Within the spend limit | Push budgets + expected other spend vs owner limit; event exceptions dated | ≤ limit | B6 R-F5 |
| G2 | Funded pushes have budgets | Push rows without budget; price and budget rows not paired in one load | 0 | B6 F14 |
| G3 | Truncation read first | Rate verdicts on campaigns in budget <70% of the day | 0 | PB |
| G4 | No invented TACoS target | Numeric TACoS target not set by the owner | 0 | register #17 |
| G5 | Cuts opportunity-checked | Cut batch without lost-order vs saved-spend test | 0 | PB 21 |
| G6 | Control arm | Mechanism change across many campaigns with none held unchanged | 0 | PB 20 |
| G7 | Soft coefficients named | Projections using an unnamed uplift/elasticity | 0 | PB 22 |

### 7.H Keywords, negatives, harvest
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| H1 | Every term decided | Search terms with spend and no decision | 0 | SKILL, B6 |
| H2 | Protected terms | Brand or push terms blocked; exact ranking terms negated | 0 | SKILL, register #12 |
| H3 | Negation evidence | Negatives without that occurrence's clicks/spend/orders or a structural reason; mode not named | 0 | PB |
| H4 | Relevant non-converters | Relevant terms negated instead of fix queue / reduce | 0 | PB, STR |
| H5 | Discovery candidacy | Broad/phrase/SB builds priced without 100 exact clicks or a stated coverage gap | 0 | PB 14 |
| H6 | Harvest complete | Harvests without ≥3 orders at ≤ break-even ACoS, or without the source negative in the same upload | 0 | register #22 |

### 7.I Competitor
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| I1 | Coverage stated | Competitor claims without "measured of mapped" and export date | 0 | B6 R-CI12 |
| I2 | No price from competitors | Any price or ceiling traced to competitor data | 0 | B6 R-CI4 |
| I3 | ASINs resolved | Targets without brand / own-product classification | 0 | LP, B6 R-X6 |
| I4 | Landscape verdicts | Push / waiting / at-target terms without a landscape verdict | 0 | B6 |
| I5 | Roster profiled | Measured competitors without a profile | 0 | B6 |

### 7.J Deliverable integrity
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| J1 | Full census | Campaigns in scope vs decision rows; in-focus campaigns without a decision | Counts equal; 0 undecided | SKILL, WB |
| J2 | Source rows verdicted | Every engine/audit row has a verdict; withheld rows absent from the upload | 0 | B6 F15 |
| J3 | Totals reconcile | Tab totals vs sums of components; plan headline figures vs workbook | Equal, or reconciliation recorded | SKILL, PB 27 |
| J4 | Overrides persist | Prior owner overrides / reviewer marks reverted | 0 | PB 19 |
| J5 | Column contract | Columns dropped vs previous version; tab names >31 chars; empty tabs without a reason | 0 | WB, DR 12 |
| J6 | Every action closable | Actions without re-read date and reversal condition | 0 | SKILL |
| J7 | Upload canon | Bulk file vs §6.5 rules | All pass | CB |
| J8 | Gate honesty | Checks typed rather than computed; PASS beside non-zero count | 0 | WB |

### 7.K Writing
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| K1 | Reasoning present and complete | Actioned rows without reasoning covering the §1.2 chain | 0 | DR 2, PB 2 |
| K2 | Converting rows not parked | Rows with orders held for "thin clicks" | 0 | DR 3 |
| K3 | No templated text | String-compare reasoning within each entity type; >5 rows sharing decision, % change and first 120 characters | 0 duplicates | PB 16, SR, PF 22 |
| K4 | Action = reasoning | Re-derive the number from the row's own data | 0 mismatches | PB 17 |
| K5 | Cold-reviewer test | Sample the 3–5 highest-exposure rows per tab and read cold | Followable without questions | PB 17A |
| K6 | Banned content | Search delivered narrative for §, rule-ID patterns, "State ", "tier", "this skill", version strings, personal names, script/run names | 0 hits | PB 23/23A/23B |
| K7 | Sources and dates | Figures without window/source | 0 | SKILL |
| K8 | References resolve | Section references vs the document's own contents | 0 broken | PB 26 |
| K9 | Ranking reasoning extras | Push rows missing organic-proxy label, front-load note, review date | 0 | PF 24–26 |

---

## 8. Open questions for the owner
1. **Hand-off search-volume threshold** for the Change Review Sheet: Resolved — see 13 #54 (and #41): SV ≥ 500, plus gate failures, structural changes, bid moves >25% outside an approved plan, budget moves >$50/day.
2. **Push daily steps vs the >25% hand-off rule**: Resolved — see 13 #41: an approved push plan covers its own +30%/day steps.
3. **Which bulk columns may change**: Resolved — see 13 #52: bid, placement %, budget, and explicitly decided state / product-ad rows; structural changes (new campaigns, colour switches, folds) built separately or by hand.
4. **Rule-ID scheme**: Resolved — see 13 #53: R-P push · R-B break-even · R-M placement mix · R-N non-ranking · R-C colour/variation · R-O objective · R-S structure · R-K keyword · R-X competitor ASIN · R-I inventory · R-F financial · R-CI competitor influence · E exceptions · F failures; extend within a family, never reuse an ID.


---

<!-- FILE: references/13-source-map-and-conflicts.md -->
# FILE: references/13-source-map-and-conflicts.md

# 13 — Source map and conflict register

This framework consolidates the skills below. Where they disagree, the **resolution** column is the default this skill applies; the alternative stays available as an owner setting. If a product owner has already ruled on one of these, their ruling wins and is recorded in the analysis.

## Contents
1. Source skills and what each contributed
2. Conflict register (resolved defaults)
3. Known defects in source implementations (do not copy)
4. Gaps in the sources (what no source defines)

---

## 1. Source skills

| Source | Short | Contributed |
|---|---|---|
| pmp-optimization-sr | SR | CM2 break-even (locked), objective ACoS bands, RPC bid math, bleed stops, TOS rebuild formula, CTR root-cause tree, DSTR floor, execution verification, impact ledger + grading + escalation, SOP-47 ceiling audit, deal-window exclusion, three-file output |
| pmp-ppc-decision-engine | DE | earlier engine (superseded by SR); Data Rova/Data Dive rank, four-quadrant vs market |
| ppc-plan-builder | PB | intake halt, product-goal gate, waterfall, decision order with quarantine/indexing, sample floors 15/100/1,000, placement backward-solve, fixed-bid trial, inventory zones 60/21, seven-state ranking test, 5-property gate, sufficiency stop, discovery candidacy, harvest, negation modes, TACoS bands, 27-check gate |
| ppc-decision-reasoning | DR | lever hierarchy, reasoning chain, action-string grammar, 13-check gate, worked examples, 12 anti-patterns |
| ppc-workbook-builder | WB | per-placement bounds, planning CVR, base floor, mix targets (70–90% TOS / ≤20% PDP), routing from Product Ad rows, deployment waves, change review sheet, ~120-check harness, defect register |
| ppc-placement-first-optimization | PF | effective TOS vs clearing CPC diagnosis, lever pair, significance test, DSTR netting organic, 15-tab approval workbook with reviewer register |
| str-audit | STR | root performance, wasted-spend negation tree, harvest tiers by ACoS, spend distribution |
| metrics-data-build | MDB | keyword master columns, SV%, syntax formulas |
| keyword-campaign-performance | KCP | keyword↔campaign grouped view, req clicks/budget, duplicate/hygiene priority |
| sqp-parent-aggregation | SQP | parent roll-up (brand summed, market once), recomputed rates |
| pmp-ppc-phasing | PH | SV tiers, hero/halo, 200-kw phase cap, match-type default Exact, naming, colour-aware routing |
| ppc-objective-correction | OC | objective from targeting at campaign level, validation |
| ppc-quick-audit | QA | 17-section audit, locked thresholds (TOS IS 22.5%, WAS 10%, target ACoS 50% BE, max 75%) |
| decolure-ppc-action-plan | AP | Finding/Why/Action/Impact, INVEST vs PROTECT thesis, execution sequence, gap keywords |
| campaign-builder | CB | bulk canon, naming (compact), upload-proof rules |
| ppc-inventory-checkup | INV | velocity, cover, OOS-before-arrival, backup switch simulation |
| ltsf-recovery-dossier | LTSF | rate card per cu ft, floor/break-even discount/salvage math, archetypes, risk tiers, ladder, listing audit, lever prediction rule |
| ppc-ltsf-plan | LP | de-dup engine, relevancy scorer vs listing, AdInsight competitor method |
| B6 engagement (Sep 2026) | B6 | push logic (premium, 2× ceiling, +30%/day), mix fix, colour rules, non-ranking 30/90-day rule, keyword decision order, competitor influence rules R-CI1–12, failure register (32), exceptions (20), SB/video test design |

---

## 2. Conflict register

| # | Topic | Sources disagree | Resolution (default) | Why |
|---|---|---|---|---|
| 1 | Break-even basis | SR: CM2 = (ASP − COGS − fees)/ASP, no returns. DE framework: includes returns / (Net+Ad)/Sales. B6: Sellerboard profit per unit before ads | **Sellerboard profit/unit before ads per SKU/colour at the price in force** (owner's source of truth). When building from components use SR's CM2 and say so. Never a blended parent | One trusted source; per SKU because colours differ 2–3× in margin |
| 2 | Conversion rate for ceilings | WB: fixed planning CVR per placement; PF: measured placement CVR (≥3 clicks); B6: own ≥50 / blend 15–50 / size rate <15 | **B6 method**: own placement CVR from 50 clicks (90 d); linear blend 15–50; size (or product) placement rate below 15 | Uses real data when there is enough, avoids circular thin-sample reads |
| 3 | Ranking ceiling | PB/WB: flat ~$8–9 (CM2 may tighten); PF: overlay 1.30× BE; DR: CM2×CVR on every row | **2 × break-even CPC on the ranking term's TOS price** (owner setting). Non-ranking: ≤ 1.0 × BE CPC at every placement | Cost per order ≤ 2× profit/unit, below order value; scales with the product instead of a flat $ |
| 4 | Push premium | WB: +25% ≤1.5 gap, else +min((r−1)×0.5, 4.0); B6 same without 4.0 | **Same formula**, capped by the ceiling | Sources agree once the ceiling applies |
| 5 | Price steps | SR ±50% envelope, cuts ≤15%/cycle; PB 25%/cycle (50% if CPA > 8× ceiling); WB 50% cut / 25% raise; PF one-shot; B6 +30%/day push, −50% base per step | Push: **≤ +30%/day** while not holding top. Other raises **≤ +25%/cycle**. Gradual cuts **≤ 15%/cycle**; decisive cuts (bleed, 0-order waste) up to 50%; **over-ceiling → straight to ceiling**. Base cut ≤ 50% per step | Gradual where learning; immediate where money is being lost |
| 6 | State A (clicks > plan, rank improving) | PB/WB: budget +20–30%; DR: hold, don't scale | **Hold price**; budget only rises if the plan's clicks are budget-truncated and the spend limit allows | Rank is moving at the current price; extra money is not needed to prove it |
| 7 | Lever order (ranking) | DR: TOS modifier → strategy → budget, base last; PB: budget first | **Evidence first** (budget truncation check) → **placement mix / TOS modifier** → price step → base last. Strategy: unchanged unless the fixed-bid trial fires | Truncated budgets invalidate every rate; the TOS modifier is the rank lever |
| 8 | Bidding strategy | SR code: switch Fixed/Up&Down → Down-only; WB: Fixed at launch for ranking; B6 owner: no strategy changes | **Leave existing strategies**; new campaigns dynamic down-only; Fixed only through the fixed-bid trial with owner approval | Owner rule; strategy changes confound every read |
| 9 | Inventory zones | PB/WB: Green ≥60 / Yellow 21–59 / Red <21; SR code: Red <14, Green ≥30; INV: OOS-before-arrival | **60 / 21**, plus **stock-out before inbound arrives = Red regardless of cover**; push also needs the advertised variation's cover ≥ days to next arrival + 7 | Lead times of 60–90 days make 14/30 too late |
| 10 | Yellow action | DR: hold; PB/WB: freeze push at current spend with dated re-entry | **No new push, no raises; keep current spend; dated re-entry plan** | Protects rank without accelerating stock-out |
| 11 | Sample floors | DR: 15 clicks zero-order; PB/WB: 15 bid / 100 CVR / 1,000 CTR; PF: ≥3 + significance; SR PT 11 | **15 / 100 / 1,000; PT 11**; placement comparisons use the significance test (n < 30 → "directional") | One set of floors, with a statistical test where two rates are compared |
| 12 | Zero-order handling | SR code: $0.50 + pause & negate any row; STR: tree by relevance; PB: relevant → fix queue; B6: ≥20 clicks 0 orders → REDUCE (owned) / BLOCK (irrelevant) | **B6 + STR tree**: irrelevant → negate (≥5 clicks); relevant ≥20 clicks 0 orders → reduce + fix queue; **never negate an exact ranking term or a brand term** | SR code negating exact ranking terms is a defect (see §3) |
| 13 | Duplicate owner | DR: instance with the traffic; PB/WB: higher CVR at lower CPC, 4 coexistence reasons; SR code: most orders > lowest ACoS; LP: sales > orders > ACoS…; KCP: sales then ACoS | **Coexistence test first** (stage-stack, placement-split, variation-split, sibling ownership). Else **owner = higher CVR at lower CPC with ≥15 clicks each; below that, most orders; tie → longer clean history**. Losers withheld (paused), nothing else changed | Rate beats volume when both have data; volume is the fallback |
| 14 | Normalisation | PH/WB: word order preserved, singular↔plural merge; KCP: sorted tokens, stop-words dropped; B6: close-variant (plural, %) | **Word order preserved; singular/plural and symbols merge**; sorted-token form only for grouping reports, never for ownership or deployment | Amazon treats word order as distinct; plurals are close variants |
| 15 | Objectives | OC: brand→Defensive, Auto/Broad→Discovery, Exact→Ranking, PT→PC; PB adds Market Share, Conquest; WB: own-PT Defensive, competitor PT Conquest | **OC table**, plus: competitor PT = Conquest, own PT = Defensive, category PT = Profitable Conversion; Market Share only when declared. Decided per campaign from targeting, never from the name | Targeting is structural; names drift |
| 16 | Non-ranking judgement | SR: RPC × objective band, Target ACoS 50% BE / Max 75%; B6: 30 & 90-day ACoS vs BE, cut ≤30% base, 2× BE on ≥30 clicks → block | **Layered**: over BE on both 30 & 90 d → cut ≤ 30% of base; > 2× BE on ≥ 30 clicks → block/stop; ≤ 50% BE with orders → scale-eligible (+≤25%) | Two windows avoid reacting to noise; bands give a scale test |
| 17 | TACoS | PB/WB: bands and tiers drive envelopes; SR: routing only; B6 owner: no numeric TACoS proposals | **Monitor and decompose; no TACoS target unless the owner sets one**; PB bands listed as reference only | Owner rule; TACoS mixes organic effects |
| 18 | Amazon suggested bids | PB/WB: required for launch bids; B6 owner: never | **Not used**; launch bids from break-even maths | Owner rule; avoids anchoring to Amazon's range |
| 19 | DSTR | PF: total sales at target, organic netted, ceil, floor 1; WB: market sales at target, ÷ CVR, no netting (WB defect D-78) ; SR: bulk DSTR, floor 1 | **DSTR = daily sales needed at target rank** (market data; floor 1/day). **Paid sales needed = DSTR − our current organic sales on the term** (labelled proxy). **Required TOS clicks = paid ÷ own achieved TOS CVR**; budget = clicks × TOS price × 1.05 | Netting avoids doubling spend; own achieved CVR, not a target CVR |
| 20 | Four-quadrant benchmark | SR: sheet targets (Market CTR × 1.10, CVR × 3.0 keyword); DE: ≥0.95 × market; QA: syntax × 1.10, fail < 0.9 × target; LTSF: market else medians | **Syntax: CTR and CVR vs Market × 1.10; fail below 0.9 × target. Keyword CVR target Market × 3.0.** No SQP → portfolio medians, labelled provisional | Keeps the locked quick-audit thresholds |
| 21 | Negation thresholds | PF ≥10 clicks; STR tree (5 clicks, relevance); WB occurrence evidence | **STR tree** (irrelevant ≥5 clicks; exact rows manual review; brand never); rows > 10 clicks & 0 orders flagged first | Relevance decides negation; clicks decide urgency |
| 22 | Harvest | PB: ≥3 orders; B6: ≥3 orders ≤30% ACoS; STR: tiers by ACoS (≤15 hero, ≤20 exact, ≤30 phrase-first) | **≥3 orders and ACoS ≤ BE, no live exact owner** → exact; match/campaign tier by STR ACoS tiers | Orders prove demand; BE keeps it profitable |
| 23 | Discovery build | PB: ≥100 exact clicks or coverage gap; Broad ~60%, Phrase ~80% of exact ceiling | **PB rule** | Only source with a rule |
| 24 | WAS ceiling | SR/QA: 10% (discovery 40%); PB: product waste <15% | **10% campaign (40% discovery)**; product-level waste reported | Campaign-level is actionable |
| 25 | Escalation | SR: 2 consecutive flat/backfired; PB/WB: same verdict 4 cycles = diagnosis error | **Both**: 2 → escalate the lever; 4 → re-diagnose the row | Different failure types |
| 26 | Sufficiency stop | PB: target 2 clean weeks → −10%/wk to floor 5–10¢ under blended CPC; SR: rank achieved → retag PC / ×0.9; B6: HOLD RANK (no raise) | **B6 HOLD RANK first 2 weeks, then PB taper**; restore on slip (>2 places top-5, any slip below target) | Protect new rank before tapering |
| 27 | Deals | PB: separate deal-state economics, 2-week guard, deals never originate a push; SR: deal blocks cuts but not bleed stops; B6: deal-day budget exception | **All three**: deal-state margin and CVR computed separately; no judging deal days; bleed stops still run; any deal budget is an explicit time-boxed exception | Deals distort every rate |
| 28 | Rule codes in text | PB: none in delivered text; DR examples use codes | **Rule IDs allowed in workbook Rule columns; never in narrative documents** | Traceability for analysts, readability for owners |
| 29 | Colour/variation routing | WB: from Product Ad rows; B6: ranking = White (best seller), discovery = clearance colour, switch never changes size | **Both**: read routing from Product Ad rows; ranking advertises the size's best seller; discovery advertises the clearance colour; size never changes | Rank accrues to the hero; clearance uses discovery traffic |
| 30 | Relevancy cut-offs | STR: ≥60 high / 35–60 moderate / <35 not; LP scorer 92/85/78/64/50/36/15–30/0 | **LP scorer for the % ; STR cut-offs for decisions** | Scorer gives the number, STR gives the action |
| 31 | Competitor tiers & influence | LP: brand-resolved AdInsight reads; B6: ASINsight tiers + R-CI rules | **B6 R-CI rules + LP brand resolution** | Combined |
| 32 | Minimum budget | SR: raise <$10 to $10; PB: budget cuts >$50/day need approval | **Both** | Compatible |
| 33 | Market/"suggested" price concept | WB/PB launch position "middle of suggested range" | **Replaced** by break-even-based launch price (see #18) | Owner rule |

### 2b. Additional resolutions (settled while writing the references)

| # | Topic | Resolution (default) |
|---|---|---|
| 34 | Marginal ACoS on a raise | Freeze the raise at the prior rung when marginal ACoS > 1.5 × average [SR]; unwind one step when > 2 × blended [PB]. Freeze first, unwind second |
| 35 | Phrase-only campaigns | **Discovery** (B6, WB). OC's script default of Profitable Conversion is not used |
| 36 | Exact terms that are not generic demand | Colour, competitor-brand, other-language, misspelled and adjacent-generic (no product-defining word, e.g. "king size sheets with corner straps" for a bamboo set) exact terms → **Profitable Conversion**, not Ranking [B6 R-O1], applied on top of #15 |
| 37 | Size of a non-ranking cut | Over break-even on **both** 30 and 90 days → cut up to **30% of base** in one step (#16). The 15%/cycle limit in #5 applies to target-chasing trims, not to this rule |
| 38 | Relevant term, ≥20 clicks, 0 orders, no live exact owner | **REVIEW** (fix queue: listing, price, colour, placement). BLOCK only when irrelevant or another product type. With a live owner → REDUCE |
| 39 | Conversion deficit (CVR far below target on ≥40 clicks) | Bid −15% and refer to Brand Management [SR]; no rank push until the offer is fixed |
| 40 | "Holding the top" | Decisions use **≥30% top-of-search impression share + top-3 sponsored**; the quick-audit 22.5% TOS IS stays a reporting reference |
| 41 | Human confirmation by search volume | SV ≥ 500, gate failures, structural changes, bid moves >25% outside an approved push plan, budget moves >$50/day. An approved push plan covers its own +30%/day steps |
| 42 | Stock during a push | Projected cover must stay **Green (≥60 days) through the push checkpoint**, or the push is blocked, shrunk or time-boxed |
| 43 | LTSF-clearance ceiling | 1 × break-even on forward-cash economics (COGS sunk); the 50% ACoS band is reference only |
| 44 | New conquest target | Must be OFFENSIVE **and** win ≥2 of price / rating / review count [PB]; else TEST. Existing targets are judged on their own clicks and orders (R-X3–X5) |
| 45 | Sponsored Brands / video bids | Start at break-even; ceiling 2 × break-even on push terms and on brand terms with verified competitor presence; 1 × elsewhere |
| 46 | Competitor-consensus thresholds | Stated as a share of the measured roster ("a majority of measured rivals"), not a fixed count |
| 47 | Discovery price anchor | "Exact ceiling" for Broad ~60% / Phrase ~80% means the exact term's **break-even** CPC, not the 2× push ceiling |
| 48 | Base far above product-page break-even | Price over ceiling → to ceiling this cycle via base + boost together; the 50% base-cut limit still applies, so a second step is scheduled if needed |
| 49 | Velocity for zones | 30-day actual pace (deal/stock-out windows corrected and labelled); the inventory file's planned velocity shown beside it |
| 50 | WAIT duration | Held until a named re-test date or until the owner declines the fix; then BREAK-EVEN |
| 51 | Non-push ranking term below break-even | KEEP (no raise) unless it qualifies for the push |
| 52 | What an upload may change | Bid, placement %, budget, and state / product-ad rows that were explicitly decided. Everything else untouched. Structural changes (new campaigns, colour switches, folds) are built separately or by hand [PF, WB, CB] |
| 53 | Rule-ID scheme | R-P push · R-B break-even · R-M placement mix · R-N non-ranking · R-C colour/variation · R-O objective · R-S structure · R-K keyword · R-X competitor ASIN · R-I inventory · R-F financial · R-CI competitor influence · E exceptions · F failures. Extend within a family; never reuse an ID |
| 55 | Objective of a harvested exact | By targeting and class: a core term (carries the product-defining word) is tagged Ranking and runs non-push at break-even until it qualifies for the push; colour / competitor / language / misspelling / adjacent-generic terms are Profitable Conversion (#36) |
| 56 | Label for "at ceiling 3 days without holding the top" | **REVIEW** (owner decision: time-limited ceiling raise or swap). CHECK OWNER is reserved for a paused/duplicate exact owner |
| 54 | Change Review Sheet threshold | Same as #41 (SV ≥ 500, gate failures, structural changes, bid moves >25% outside an approved plan, budget >$50/day) |

---

## 3. Known defects in source implementations (do not copy)

- SR impact review references undefined variables in the freeze/backfire branches (crash); Freeze/Floor never populated.
- SR zero-order branch writes "$0.50 + pause and negate" for any match type incl. exact Ranking — contradicts "exact protected".
- SR turn-off thresholds doubled twice (effective 200/120/100/60/50%).
- SR/DE silent global break-even default 0.1986 when a SKU has no economics — must halt instead.
- SR/DE CVAR, Yellow freeze, budget steps, harvest, deal-price break-even recompute: specified, not built.
- WB D-78: DSTR ÷ CVR without organic netting doubles required spend.
- B6 engine (29 Sep run): 32 failures documented in `examples/b6-case-study.md` (deal not read, blended margin, dose jumps, wrong colours, duplicate owners, brand negatives before exacts ready, etc.).

## 4. Gaps in the sources

- No weighted listing-quality score exists; use the 1–10 competitor comparison per element (reference 09).
- Review themes are not in any connected data source; require a manual read or an external review tool.
- Keyword-level competitor history is not available from single exports; use rival-level trend × current ranks as a proxy and label it.
- Quick-audit FRAMEWORK/locked-threshold files and the phasing matrix were not in the synced skills; thresholds here come from the SKILL/config text.


---

<!-- FILE: templates/intake-request.md -->
# FILE: templates/intake-request.md

# Template — intake request

Send the message in Part 1 in **one batch** before any analysis. Do not start partially: wait until every item is received or confirmed "doesn't exist / not needed this cycle". Record each answer in the Part 2 checklist and keep it with the deliverables. [PB, QA, SR]

Fill the `<…>` fields before sending. Delete a group only when the scope rules it out (a one-area request still needs groups A–C and G, because every area depends on economics, inventory and events).

---

## Part 1 — message to send

> **Subject: Inputs needed for the `<product / parent ASIN>` analysis (`<marketplace>`)**
>
> To analyse `<product>` properly I need the files and answers below, all in one go. Please send each as the raw export (not a filtered or re-saved copy), keep the original column headers, and tell me the date range of each. If something doesn't exist, just say so — I'll record it as a gap rather than guess.
>
> **A. Advertising data**
> 1. **Sponsored Products bulk file** (Bulksheets 2.0, all tabs, including paused and archived items) for three windows: **last 7 days**, **the 7 days before that**, and **the last 60–90 days**. `.xlsx`.
> 2. **Search term report** (Sponsored Products), daily rows, **last 60–90 days**, all campaigns in the portfolio(s). `.xlsx`. Please give me the exact portfolio name(s) as they appear in the report.
> 3. **Placement report** (campaign × top of search / rest of search / product pages) for **30 and 90 days**, and the **Sponsored Products targeting report** (for top-of-search impression share) for the same windows. `.xlsx` or `.csv`.
> 4. **Advertised product report** for the same windows (which child ASIN/SKU each ad served), so I can check which variation actually earned each result.
> 5. **Sponsored Brands / video / Display** campaign reports (30 and 90 days), if any run on this product.
> 6. If you use a dashboard (e.g. Command Center): the product-level ad spend, sales and orders **by day for the last 90 days**, and any **shared campaigns** that advertise other products too.
> 7. **Last cycle's outputs**, if there was one: the decision workbook or plan, the action log / change list with dates it was uploaded, and any reviewer marks or owner overrides.
>
> **B. Economics**
> 8. **Sellerboard (or equivalent) per SKU/colour, last 30 days**: units, price, refunds, Amazon fees, product cost, storage, and **profit per unit before ads**. `.xlsx` or `.csv`.
> 9. Any **price change, fee change, packaging change or new product cost** coming up, with dates.
> 10. **Business report** (child-ASIN detail, weekly, last 90 days): sessions, units, total sales — for organic share and TACoS.
>
> **C. Inventory and variations**
> 11. **Inventory per SKU** (full export, not the variation page): Available, reserved, inbound with **dated confirmed arrivals**, transfers, units in production; units sold per day over **7 and 30 days**; days of cover. `.xlsx`.
> 12. For each size (or syntax): the **preferred** variation for ranking, the **backup** variation, and any **clearance** colour you want pushed through discovery. Please list them — I won't derive them.
> 13. If any stock is aging: the **inventory-age export (all age brackets)**, the latest **long-term storage fee charge file**, and cubic feet per unit per SKU.
>
> **D. Keywords and rank**
> 14. **Master keyword list** (no older than ~30 days): search volume, relevancy, syntax/root, categorisation, indexed yes/no, currently targeted yes/no.
> 15. **Search Query Performance** (Brand Analytics) for the parent or all child ASINs, **last 13 weeks** (and monthly if you have it), raw export.
> 16. **Target ranks**: target organic rank and target date per search term.
> 17. **Rank history, daily, at least 1 month (ideally 3)** — organic and sponsored rank per term (Data Rova, Data Dive, Helium 10 or your rank crawl).
> 18. Your **syntax taxonomy** (if you have one) and every spelling of the **brand name** shoppers use.
>
> **E. Competitors**
> 19. The **competitor roster**: ASIN → brand, and which you consider aspirational / beatable.
> 20. **Competitor exports, dated**: ASINsight / AdInsight per competitor, Data Dive niches, Helium 10 Cerebro/X-ray multi-ASIN pulls, and any price / BSR / review movement brief. Tell me which mapped competitors have **no** export.
>
> **F. Listing**
> 21. The **live listing**: title, bullets, backend search terms, main and secondary images, A+ content, video, price, coupon, rating and review count — as they are today.
>
> **G. Calendar**
> 22. **Deals and events**, past 90 days and next 90 days: dates, deal type, deal price, deal fees; Prime Day / Black Friday plans; planned price or listing changes.
>
> **H. How you want it built**
> 23. Campaign naming convention and any structure template or example I should follow.
> 24. Output format: Excel + Word, Google Sheets + Docs, or both.
>
> **Questions about how you want the product run** (I'll use the house default in brackets only if you confirm it):
> 1. **Goal for this product**: Growth/Scale, Mixed (rank some terms, profit on the rest), Profit-First, or Clearance/LTSF? *(No default — this decides whether any ranking spend is allowed.)*
> 2. **Is this an analysis** of what exists, or a **plan** of what to do next? From scratch, or a refinement of an existing plan?
> 3. **Spend limit** for the product: $ per day or week, and any **event exceptions** (dates and how much). *(No default.)*
> 4. **Margin rule**: minimum margin after ads (e.g. "above 10%"), and any time-boxed exception. *(No default.)*
> 5. **Margin source**: Sellerboard profit per unit before ads, per SKU, last 30 days, deal price during deals? *(Default: yes.)*
> 6. **Ranking ceiling**: 2 × break-even cost per click on the top-of-search price? Any named term where you'd allow more for a set time? *(Default 2×; alternative: a flat account cap ~$8–9.)*
> 7. **Push step**: up to +30% a day while a pushed term isn't holding the top? *(Default: yes.)*
> 8. **TACoS**: do you want a numeric TACoS target, or monitor only? *(Default: monitor only.)*
> 9. **Bidding strategies**: leave existing ones as they are; new campaigns dynamic down-only; fixed bids only through a trial you approve? *(Default: yes.)*
> 10. **Amazon suggested bids**: never used to set prices? *(Default: not used.)*
> 11. **Stock zones**: Green ≥60 days of cover, Yellow 21–59, Red <21, and "stock-out before the next arrival" counts as Red, and a push needs projected cover to stay Green through its checkpoint? *(Default: yes.)*
> 12. **Zero-order rule**: ≥20 clicks and 0 orders → reduce (relevant, with a live exact owner), fix list (relevant, no live exact owner) or block (irrelevant or another product type); exact ranking and brand terms are never negated? *(Default: yes.)*
> 13. **Harvest**: ≥3 orders at or below break-even ACoS with no exact owner → build an exact campaign and negate at the source? *(Default: yes.)*
> 14. **Approvals**: which changes need your sign-off before upload (default: structural changes, bid moves >25% outside an approved push plan — the plan's own +30%/day steps are covered by approving it — budget moves >$50/day, any failed check, terms with search volume ≥ 500).
> 15. **Rules that need your confirmation before first use on this product**: defensive-campaign ladder and competitor-presence allowance; conquest entry/exit; harvest bar; discovery count basis (keyword vs root cluster); how a ranking push ends after target is held; graded raise tiers for non-ranking terms; a $0.50 minimum bid.
> 16. **Portfolios in scope**: this portfolio only, or also a sibling portfolio that buys the same head terms? Marketplace: US or CA (never mixed)?
>
> Thanks — once I have these I'll confirm what's in, what's missing, and which decisions each gap blocks before I start.

---

## Part 2 — receipt checklist

Status: **Y** received · **N** missing (named gap) · **N/A** confirmed not applicable. "Blocks" = what cannot be decided without it.

| # | Item | Window | Format | Status | Received on | File name | Freshness / check | Blocks if missing |
|---|---|---|---|---|---|---|---|---|
| 1 | SP bulk ×3 windows | 7 d / prior 7 d / 60–90 d | xlsx | | | | every tab listed; campaign count vs dashboard | all campaign decisions |
| 2 | Search term report | 60–90 d daily | xlsx | | | | portfolio name exact; min/max date | keyword decisions, harvest, negatives |
| 3 | Placement + targeting reports | 30 / 90 d | xlsx/csv | | | | campaign grain | placement, mix fix, ceilings |
| 4 | Advertised product report | same | xlsx/csv | | | | SKU per ad over window | SKU provenance, every verdict |
| 5 | SB / SBV / SD reports | 30 / 90 d | xlsx/csv | | | | — | brand-format decisions |
| 6 | Dashboard product totals, shared campaigns | 90 d daily | csv | | | | spend tile vs rows | spend reconciliation, event baseline |
| 7 | Prior cycle outputs | last cycle | xlsx/docx | | | | upload dates known | grading, escalation (else first cycle) |
| 8 | Sellerboard per SKU | 30 d | xlsx/csv | | | | ≤45 days old | break-even, every price |
| 9 | Price/fee/COGS changes | next 90 d | text | | | | — | future ceilings |
| 10 | Business report | 90 d weekly | csv | | | | — | organic share, TACoS |
| 11 | Inventory per SKU | snapshot + 7/30 d pace | xlsx | | | | full export, unfiltered | stock gates, pushes |
| 12 | Preferred / backup / clearance | — | list | | | | user-supplied | routing, colour switches |
| 13 | Age export, LTSF charge, cu ft | latest | xlsx | | | | all brackets | clearance decisions |
| 14 | MKL | ≤30 d old | xlsx/csv | | | | syntax verified | keyword universe |
| 15 | SQP | 13 weeks | csv | | | | market once, brand summed | four-quadrant, targets |
| 16 | Target ranks | — | csv | | | | — | push premium, HOLD RANK |
| 17 | Rank history | ≥1 month daily | csv | | | | <1 month → ranking out of scope | ranking verdicts |
| 18 | Syntax taxonomy, brand variants | — | list | | | | — | classification, brand protection |
| 19 | Competitor roster | — | list | | | | brands resolved | competitor sections |
| 20 | Competitor exports | dated | xlsx/json | | | | coverage n of mapped | landscape, ASIN targets |
| 21 | Live listing | today | text/images | | | | — | listing checks, relevancy |
| 22 | Deal / event calendar | −90 / +90 d | text | | | | — | event gate, windows |
| 23 | Naming / structure template | — | any | | | | — | builds |
| 24 | Output format | — | answer | | | | — | delivery |

### Owner settings — answers

| # | Setting | Answer | Default used? (Y/N) | Date confirmed | Notes |
|---|---|---|---|---|---|
| 1 | Product goal | | | | undeclared → treat as Profit-First for the ranking gate |
| 2 | Analysis / plan; scratch / refinement | | | | |
| 3 | Spend limit + event exceptions | | | | |
| 4 | Margin rule + exceptions | | | | |
| 5 | Margin source | | | | |
| 6 | Ranking ceiling (+ named raises, end dates) | | | | |
| 7 | Push step | | | | |
| 8 | TACoS target | | | | |
| 9 | Bidding strategy policy | | | | |
| 10 | Suggested bids | | | | |
| 11 | Stock zones | | | | |
| 12 | Zero-order rule | | | | |
| 13 | Harvest rule | | | | |
| 14 | Approval thresholds (default SV ≥ 500) | | | | |
| 15 | Provisional rules confirmed (list each) | | | | |
| 16 | Portfolios, marketplace | | | | |

### After receipt (before analysis)
1. List every sheet in every file; read each; mark READ-FULL / READ-PARTIAL / NOT-RELEVANT / NOT-OPENED. [WB]
2. Reconcile: bulk vs dashboard spend; Sellerboard units vs orders; inventory on-hand − available − reserved (gap >5 units → verify at source). [PB]
3. Reply once with: what's in, what's missing, which decisions each gap blocks, and any answerable question still open (ask once; don't log an answerable gap as "next cycle"). [PB]


---

<!-- FILE: templates/report-outline.md -->
# FILE: templates/report-outline.md

# Template — decision document outline

Skeleton for the written deliverable (Word or Google Doc). Modelled on the B6 corrections document (17 sections + appendix), generalised so it works for a plan, an audit of an engine run, or a single-area review. Keep section numbers stable across cycles so the workbook and next steps can cite them. Writing rules: `references/12-writing-and-deliverables.md` §1–§5.

Rules for every section:
- Only sections with evidence. An empty section is deleted, not padded; a section that exists but has no action says so in one line.
- Items inside sections use **Finding → Why it matters → Action → Expected impact**; number actions (5.1, 5.2 …).
- Every major table is followed by "What this table decides" (one line). Charts: title states the finding, direct labels, threshold band shaded.
- Every figure has a window and source; no internal codes, tool names, "this skill", version history or personal names; roles only ("the product owner", "the PPC manager").
- Where the document and the workbook disagree, the workbook governs row-level numbers — say so in the title block.

---

## Title block
- Title: "`<Product>` (`<short code>`) — `<analysis type>`" (e.g. "Corrections to the `<date>` PPC audit", "PPC plan", "Product analysis").
- Line 2: date · windows analysed · run/cycle reference if reviewing a run · companion files (decision workbook, competitor workbook, change review sheet) · "where they disagree, the workbook applies".

## Summary
1. One paragraph: what was reviewed/decided, the size of the change (N changes on M campaigns, K new builds), and the single most important context fact (e.g. a deal in progress that the prior process ignored).
2. The decisions / corrections as a short bulleted list, each one sentence + section reference.
3. **Budget statement**: the spend limit for each window, any stated exception (dates, margin impact), where the increase goes.
4. **What the plan can actually spend** vs the limit, and the binding constraint (price-capped vs money-capped). Example (B6): "about $750 a day on day one, well under $1,300 — 11 of 13 funded terms are at or near their ceiling".
5. **Needs your decision** — numbered, each with options, trade-off in reviewer units, and deadline.
6. Headline numbers box (6–8 KPIs with windows) — optional when the Section 1 table carries them.

## How to read this
Glossary table, two columns (Term · What it means here). Always include: top of search / product pages (and target mix 70–90% / ≤20%); base bid / top-of-search boost (900% cap); top-of-search price = base × (1 + boost); the product's bidding strategy and what it means for reads; break-even price (margin source + window per SKU; CVR basis own ≥50 / blend 15–50 / size <15); push price and ceiling; available stock (what counts); ranking vs clearance variation. Add product-specific terms only.

## 1. Where things stand
- Table by period: before event (settled) vs during event (and after, if any): ad spend/day, ad sales/day, ACoS, orders/day, top-of-search clicks/day, product-page clicks/day, top-of-search share, top-of-search price. Mark unsettled figures (7-day attribution).
- Two or three sentences: what changed and what didn't (e.g. "the deal tripled spend and doubled orders but didn't move the ads to the top").
- Rank arc on the 3–5 head terms (prior → recent → current, source).
- Chart: top vs product-page clicks/day, spend/day, organic rank on head terms; events shaded.

## 2. The rules these decisions apply
One short paragraph per rule family, plain language, no IDs: qualification for a push; push price, ceiling and step limit; mix fix; break-even for everything not pushed; margin source; one campaign per search term; variation/colour routing; non-ranking judged on its own break-even over two windows; events don't judge results (re-read after 7 settled days).

## 3. Goals, spend limit and margin rule
- What the prior plan/process set (or failed to set) and why its forecast can't be judged without goals; baseline correction (settled vs event days).
- **Correction / plan**: spend limit per window (with exceptions), margin rule, product goal with dated milestones (e.g. "top 10 on half the push terms by `<date>`"), hold-what-was-bought ranks, recovery targets, order floor (orders/day), placement target.

## 4. Calendar and transition plan
Dated blocks, each with actions and what is *not* done:
- Now → end of current event: what loads, what is held.
- Day 1 after the event: re-price on full-price margin, re-evaluate the limit, decide held builds/restarts/folds; the push continues without a gap.
- Settling week ("watch, don't judge"): daily checks (spend vs limit, orders vs floor, top-of-search share, head-term ranks, hero stock with cover and arrival dates); rank drop >10 → find cause first.
- First clean read: re-run break-even on 7 settled days; mix re-check; weekly tune dates.
- Next events (dated): size each push a week ahead (price, clicks, budget, stock); skip event days in reads.
- Peak season: ≥3 weeks ahead per event; arrivals that land in time.

## 5. Ranking: the push plan
- **5.1 What is wrong now** (review) or **What the data says** (plan): each issue with examples and numbers (e.g. economics on the wrong margin, step jumps above cap, boosts raised on campaigns not at the top, cap-bound campaigns, self-contradicting rows).
- **5.2 What a competitor shows is possible**: a rival's rank path on the push terms (dates, ranks, keyword sales) and our own history (median days to reach and hold top 10 once clicks land); where volume at the top is the blocker ("gets 10 of the 69 top-of-search clicks a day its plan needs").
- **5.3 The push plan**: table — term · rank now → target · TOS clicks/day plan · today · TOS CVR · orders/day plan · price to write (ceiling) · our TOS cost per click (thin flag) · budget; funded total row; table notes (CVR basis, CPC window, budget formula, scaling to the limit). Then **Waiting** table (term · rank → target · why it waits · meanwhile), **At target** paragraph, **Left out for now** (too far, falling — find cause, wrong objective), **What it costs** (budgets vs expected spend vs limit; margin impact), **Needs your decision** (ceiling raises with options), expected orders and payback, and **How each push term is tuned** (daily step, day-3-at-ceiling rule, weekly tune, stop rule).
- **5.4 How the correct price is worked out — examples**: 4–6 rows: campaign · break-even (margin × CVR) · rank → target · push price (ceiling) · now vs proposed · correct move (base/boost pair). Formula line under the table.
- **5.5 Every focus campaign gets a move**: counts by decision (pushed, waiting, holding, to break-even, stepped down, paused, already under).
- **5.6 Head-term deep dive**: the biggest term — demand, 30-day funnel, TOS CVR vs market, stock, what went wrong, the fix, and the owner decision.

## 6. Which variation each campaign advertises
- Rule in one paragraph (ranking = size's best seller unless it can't reach its next arrival; size never changes; discovery = clearance colour; colour-named terms keep their colour).
- Table per size: hero Available (cover, next arrival) · current serving variation · correct ranking variation.
- Named campaigns on the wrong variation (with spend), switches to make by hand, discovery clearance table (size · colour · stock/cover · campaigns to move), near-out colours to keep out of every ad.

## 7. Campaigns that can't serve
Table: term (target) · what is wrong (paused, duplicate owners, cap-bound, build over a paused keyword) · correct move. Restarts: now vs after the event, at break-even.

## 8. Placement: where the clicks land
Product-level split (top / rest / product pages share of clicks, CPC each). Table of the largest campaigns: clicks · top / product pages share · base now → correct · top-of-search price (push / held / break-even). Re-check date.

## 9. Campaign objectives
What was retagged right, what was wrong (colour, competitor, other-language, misspelling, ranking target tagged conversion), existing mis-tags, brand campaigns tagged discovery.

## 10. One owner per search term
Negatives to load (and any to hold), duplicate owners, structural folds (decide after events), exclusions of head terms from discovery.

## 11. Non-ranking campaigns and keywords
- Counts: inside break-even / over on both windows / too thin / liquidation / paused; the cuts (≤30% of base) with the largest examples.
- The most profitable campaign(s) and anything that threatens them (e.g. brand negatives before receiving exacts are ready).
- Keywords: harvest (build exact at break-even after events, negate at source), block (irrelevant / other product type), reduce (over break-even, still sells, or relevant 0-order with a live exact owner), review (relevant 0-order with no live exact owner → fix queue), de-duplicate, check owner — with counts, spend and 2–3 examples each.

## 12. Required clicks, budgets and the forecast
Requirements set volume and budget, never price; reconcile to what the product sells; credit steps with what similar steps bought; settled baselines; expected spend vs limit.

## 13. Rank drops and exceptions
Terms that fell >10 places while getting clicks: cause first (variation, listing, keyword state, competitor, stock) — never more spend. Other exceptions in force (listing flags, ceiling below cost, thin data, shared campaigns, event days).

## 14. Changes that should not load as written
(For reviews of an engine/plan run; for a fresh plan, rename "Change list" and summarise the upload.) Counts by type with the replacement: price/base rows, budgets, new campaigns (and what happens to each on the decision date), retags, specific rows held, restarts and when they load. Close with the prior process's own endorsement and what it left undecided.

## 15. Competitive landscape
- Scope line: competitors measured of mapped, keywords, export dates, niche data.
- Table: measure · us · the market (share of tracked traffic, traffic trend, core-term ad intensity, uncovered segment, brand-banner/video reach, offer and price ladder, reviews).
- **15.1 What it confirms**: push terms vs field table (term · decision · our organic · target · top rivals · next rival to pass · read: stretch / reachable / winnable / we lead).
- **15.2 What it changes (prices don't change)**: how stretch terms are judged, read on rank and orders, brand defence, seeding, reduce-not-block on sellers rivals buy, conquest targets (OFFENSIVE) vs AVOID, generic terms left to discovery, protect strongest ground by stock, rival-move holds.
- **15.3 What the data can't show**: review themes, competitor bids/CVR, unmeasured and unmapped sellers.
- Optional **15.4 Listing and offer** (when Phase 5 found issues): four-quadrant per syntax, offer vs rivals, listing checks by quadrant, owner and effect.

## 16. Tests
Per test: rationale from the landscape, table (id · format · keyword · advertises · start bid = break-even · ceiling — 2 × break-even on push terms and on brand terms with verified competitor presence, 1 × elsewhere · budget/day), total and budget line, start rule, daily step, re-baseline at 15 clicks, stop rules (20 clicks 0 orders; >2× break-even ACoS on ≥30 clicks), read date (before the next event), halo check on the same-term SP campaign, report metrics, what is not built and why, creative notes.

## 17. Next steps
Dated list in execution order (protect revenue → stop bleeding → reallocate → expand): today; to end of event; day 1 after; this week (by-hand changes); daily watch window; weekly tune dates; test read date; ≥3 weeks before each peak event. Then **Risks and falsification** (dated checks that would prove the plan wrong) and **Decisions requested** (numbered).

## Appendix — fixes for the engine / process
One line per systemic defect found (what it does, why it's wrong), grouped by area: calendar/events, goals/baseline, economics, pricing/steps, placement, focus vs qualification, variation routing, objectives, structure/builds, negatives, qualification checks, competitive blind spots, formats outside automation. Optional appendices: data sources and coverage; data conditions register; glossary.


---

<!-- FILE: templates/workbook-spec.md -->
# FILE: templates/workbook-spec.md

# Template — decision workbook spec

Tab-by-tab specification of the decision workbook (xlsx), generalised from the 34-tab B6 reference workbook and the B6 campaign-decisions workbook. Writing rules and the full quality gate: `references/12-writing-and-deliverables.md`.

## Contents
1. Conventions (all tabs)
2. Tab list at a glance
3. Tab specs — front matter (1–8)
4. Tab specs — keywords and campaigns (9–13)
5. Tab specs — competitors (14–24)
6. Tab specs — placement, stock, money, exceptions (25–29)
7. Tab specs — rows, operations, validation (30–33)
8. Checks tab (34)
9. Optional tabs

---

## 1. Conventions (all tabs)
1. Tab names ≤31 characters; order as in §2; an empty tab states why in its first row ("No product targets in scope"). [WB]
2. Row 1 title, row 2 subtitle (sources, windows, date), then sections; tables have one header row, frozen panes on the identity columns, auto-filter on long tables. [B6]
3. Formats: $ 0.00 for prices/bids, $ 0 for budgets, 0.0% for rates and shares, integers for ranks; missing = blank or "—", never 0. [all]
4. Decision cells colour-filled by label (one colour per label, legend on Start here); stock zones Green / Yellow / Red. [B6]
5. "New" columns are blank when the value does not change. Top-of-search price always = base × (1 + boost). [WB]
6. Every decision row carries the trail: **Input → Metric → Logic (rule) → Decision → Action → Expected outcome → Validation**. Rule IDs appear only in Rule / Logic columns. [B6, register #28]
7. Every figure is produced by the build from source data, never typed; the column set is a contract — diff against the previous version and never drop a column silently. [WB, DR]
8. Reasoning cells follow the chain in reference 12 §1.2 and must not repeat verbatim across rows. [DR, PB]

## 2. Tab list at a glance
| # | Tab | Required? | Answers |
|---|---|---|---|
| 1 | Start here | Always | What this is, sources, how to read, tab index |
| 2 | Overview | Always | Spend vs limit, decisions at a glance, what needs the owner |
| 3 | Process map | Review of an engine/plan run | Pipeline stages: what it does, where it failed, corrected logic |
| 4 | Failure register | Review of an engine/plan run | Each wrong decision, the data, the correction, the test |
| 5 | Before → After | Review or refinement | Same measures on prior version(s) vs corrected |
| 6 | Metrics dictionary | Always | Every metric used |
| 7 | Decision rules | Always | Every rule applied (IF → THEN) |
| 8 | Decision trails | Always | Worked end-to-end examples |
| 9 | Keyword decisions | Always | Every search term with spend |
| 10 | Harvest & negate | Always | Keyword actions grouped |
| 11 | Campaign logic | Always | How each type × objective is treated |
| 12 | Campaign decisions | Always | Every campaign, one decision, full trail |
| 13 | Push plan | When ranking is authorised | Funded / waiting / at-target terms |
| 14 | Competitor targeting | When product targets exist | Product targets and their performance |
| 15 | Competitor landscape | Always (may be a separate file) | Market, share, trends, segments, price ladder, patterns |
| 16 | Competitor profiles | Always (may be separate) | Each measured rival vs us |
| 17 | Hero ASINs & trends | When trend data exists | Rival heroes, movers, where rising rivals gain |
| 18 | Competitive keywords | Always (may be separate) | Every addressable market keyword |
| 19 | Push terms vs field | When ranking is authorised | Who stands between us and each target |
| 20 | Gaps & how to fill | Always | Gaps with size, fill inside guardrails, validation |
| 21 | Competitor ASIN targets | Always | OFFENSIVE / TEST / AVOID per rival ASIN |
| 22 | Competitor → decisions | Always | Influence rules; what each never changes |
| 23 | Tests | When a test is proposed | Test design, rules, read dates |
| 24 | Landscape check | Always | Each keyword/campaign decision vs the field |
| 25 | Placement | Always | Campaign × placement read and mix fix |
| 26 | Variation & stock | Always | Preferred / backup / clearance per size; SKU margins |
| 27 | Inventory × PPC | Always | How stock gates each decision |
| 28 | Financial guardrails | Always | Break-even, ceilings, limits, per SKU |
| 29 | Exceptions & BLOCK | Always | No-automatic-change conditions, current cases |
| 30 | Source rows | Review of a run | Every proposed row with a verdict |
| 31 | New campaigns | When builds/restarts exist | Builds and restarts with decision and date |
| 32 | By hand | When needed | Changes that don't upload (switches, tags, budgets, SB/SD) |
| 33 | Validation plan | Always | Checkpoints, pass, fallback |
| 34 | Checks | Always | Computed integrity checks |

---

## 3. Front matter

### 1. Start here
- **Purpose**: orient a cold reader in two minutes.
- **Content**: what the workbook is (one paragraph); versions compared (if a review); how the trail works and where rule IDs point; status legend (e.g. Fixed / Partly fixed / Not fixed / New finding); sources with windows and dates.
- **Table**: Tab · What it answers.

### 2. Overview
- **Spend vs limit** table: Line · $ a day · Basis — current spend (event and settled), outside-push today and after cuts, push today and expected day one, expected total, push budgets (full plan and scale factor), the limit (with exception terms).
- Binding-constraint sentence (e.g. price-capped: N of M funded terms at or within 5% of ceiling).
- **Needs your decision**: # · Decision · Detail (options, trade-off, deadline); already-decided items marked with date.
- **Decisions at a glance**: counts by campaign group, campaign decision, keyword decision, failure status.

### 3. Process map (reviews only)
- Columns: Stage · What it does · Inputs · Where it failed (failure IDs) · Corrected logic · Rules / guardrails · Validation.
- Stages (generic): scope & calendar → data read → economics → classification → targets & requirements → qualification → pricing → structure → variation → budgets & limit → forecast → review & loader → validation & tuning.

### 4. Failure register (reviews only)
- Columns: ID · Area · Scenario · What was decided · Example and data · Why it was wrong · Correct decision · Logic / guardrail changed · Version A result · Version B result · Status · How recurrence is prevented · Validation test · Rules.

### 5. Before → After
- Columns: Measure · Version A · Version B · Corrected · Source.
- Rows (generic): events recorded; margin / break-even ACoS; decisions / campaigns changed; campaigns in list; changes outside own list; price/base changes; jumps above cap; prices above ceiling; variation switches (and size changes); budgets; withheld rows exported; wrong retags; restarts; new campaigns; brand negatives; head-term price; cap-bound campaigns; forecast spend, ACoS, TOS clicks; review verdict; funded push terms.

### 6. Metrics dictionary
- Columns: Metric · Family · What it means · How it is calculated · Source · Window · Validation · Thresholds used · How it influences the decision · Pitfalls.
- Minimum rows: impressions, clicks, CTR, orders/units, CVR, TOS CVR, CPC, TOS CPC, spend (tile vs rows), ad sales, ACoS, TACoS, ROAS, AOV, margin per unit, break-even ACoS, break-even CPC, ceiling, push price, CPA, margin after ads, TOS price, base, boost, placement click share, TOS impression share, sponsored rank, organic rank, target rank/date, rank drop, search volume, relevancy, term class, indexing, market CTR/CVR (SQP), plan clicks, available stock, days of cover, days to arrival, velocity, event flag, event-day spend, budget.

### 7. Decision rules
- Columns: Rule ID · Family · Applies to · IF · THEN · Thresholds · Why · Guardrail / limit · Exception → review.
- Families: push, break-even, placement, non-ranking, variation, objective, structure, keyword, competitor target, inventory, financial, competitor influence.

### 8. Decision trails
- One section per example; table Step · Detail with rows Input, Metric, Logic, Decision, Action, Expected outcome, Validation, and (reviews) "Previously decided".
- Minimum set: head push term; over-ceiling term; variation switch; rank collapse; cap-bound campaign; brand campaign; discovery campaign; harvest; reduce; competitor ASIN. Template: `templates/decision-trail-examples.md`.

## 4. Keywords and campaigns

### 9. Keyword decisions
- **Scope**: every search term with spend in 30 or 90 days (plus market terms seeded from gaps).
- Columns: Search term · Decision · Rule · Why · Action · Class · Relevancy · Search volume/month · Weekly SV (competitor tool) · Organic rank (30 d median) · Sponsored rank · Target rank · Indexing · Exact owner(s) · Impr 30 d · Clicks 30 d · CTR 30 d · Orders 30 d · CVR 30 d · CPC 30 d · Spend 30 d · Sales 30 d · ACoS 30 d · Clicks 90 d · Orders 90 d · CVR 90 d · CPC 90 d · Spend 90 d · Sales 90 d · ACoS 90 d · TOS share · TOS CVR · TOS CPC · PDP share · PDP CVR · ROS share.
- Decision labels: PUSH / WAIT / HOLD RANK / BREAK-EVEN / REDUCE / REVIEW / BLOCK / HARVEST / DEDUPLICATE / CHECK OWNER / DEFEND / MONITOR / KEEP (REVIEW = relevant term, ≥20 clicks, 0 orders, no live exact owner → fix queue; register #38).
- Note in subtitle: placement shares at keyword grain are estimates (placement is reported per campaign).

### 10. Harvest & negate
- Sections: Harvest · Block · Reduce · Review (fix queue) · Deduplicate · Check owner — each titled with count and 90-day spend.
- Columns: Search term · Class · Relevancy · Clicks 90 d · Orders 90 d · ACoS 90 d · Spend 90 d · Owner(s) · Action (with timing and negation mode).
- Section for negatives proposed by the prior run: Seq · Campaign · Negatives now · After · Terms added · Verdict (Load / Hold, why).

### 11. Campaign logic
- Columns: Type · Objective · Purpose · Deciding metrics · Allowed actions · Not allowed · Advertised variation · Placement rule · Rules · Campaigns (count).
- Rows: Exact × Ranking / Profitable Conversion / Defensive; Broad-Phrase × Discovery; brand Broad × Defensive; Auto × Discovery; product targeting × Defensive (own) / Conquest (competitor) / Profitable Conversion (category) / cross-sell (own other product); SB/SBV; SD; Liquidation/LTSF.
- Paragraphs: how type is recognised (targeting, not name); how objective is set; what "focus" may and may not do.

### 12. Campaign decisions
- **Scope**: every campaign advertising the product (list + any spending on it but missing, marked).
- Identity: Group · Campaign · Campaign ID · In list · Ad type · Match · Size · Main term(s) · Status · Focus · Objective now → correct · Variation now → correct.
- Trail: INPUT · METRIC · LOGIC (rule) · DECISION · ACTION · EXPECTED OUTCOME · VALIDATION · Why (full reasoning) · Prior-run rows → verdict · When · How it loads.
- Numbers: Clicks 30 d · Orders 30 d · Spend 30 d · ACoS 30 d · ACoS 90 d · TOS share · PDP share · TOS clicks 90 d · TOS CVR 90 d · Margin/unit · CVR used (basis) · Break-even $ · Ceiling $ · Rank now → target · Base now/new · Boost now/new · TOS price now/new · Budget now/new · State new · Variation new · Objective new · Event-day spend.
- Sort: group order (push funded, waiting, at target, ranking break-even, profitable conversion, discovery, defensive, liquidation, SB/SD), then spend desc.

### 13. Push plan
- Columns: Status (PUSH / WAIT / HOLD RANK) · Term · Campaign · Variation now → correct · Rank now → target · TOS CVR (90 d, basis) · Break-even $ · Push price $ · Ceiling $ · Our TOS CPC (90 d) $ · Price now $ · Price to write $ · Base now → new · Boost now → new · Plan TOS clicks/day · Today TOS clicks/day · Plan orders/day · Budget $ · First milestone · Re-read date · Why.
- Footer: funded total; formula notes; scaling to the limit.

## 5. Competitors
All competitor tabs state coverage ("measured N of M mapped") and export dates in the subtitle; unmeasured ≠ zero; ASINs resolved to brands. [B6 R-CI12, LP]

### 14. Competitor targeting
- A. Product targets with own reads: Campaign · ASIN · Brand · Product · Price · Rating · Reviews · Relation (own product / own other product / competitor same material / competitor other material / unmapped) · Campaigns targeting it · Clicks · Orders · CVR · Spend · ACoS · Decision (DEFEND / KEEP / SCALE / REDUCE / BLOCK / MONITOR) · Why.
- B. Product-targeting campaigns (30/90 d): Campaign · Tag · Advertises · Targets · funnel 30/90 d · Decision · Why.
- C. Proposed conquest builds: ASIN · Brand · Product · Price · Rating · Reviews · Relation · Assessment.

### 15. Competitor landscape
- Numbered patterns that should steer PPC (8–12, each with numbers).
- Sources and limits: Source · What it gives · Date · Limits (include "not available anywhere": review themes, competitor CPC/CVR/structure).
- Market size, reach, share: Measure · Keywords · 7-day traffic · Our traffic · Our share · Note (whole market, addressable, disqualified, unknown, contested, theirs-only, ours-only, per segment).
- Traffic trend: Seller · Tier · Earlier export · Traffic then · Latest · Traffic now · Change.
- Placement reach: Seller · Tier · Keywords · Organic · SP · SB · SB video · Amazon's Choice · Product-page recs · Read.
- Segments: Segment · Keywords · Market traffic · Paid share · Our traffic · Our share · Absent keywords · Wins vs beatable.
- Niche benchmarks: Niche · Researched · Keywords · Monthly SV · Median price · Median reviews · Median units.
- Price ladder: Brand · ASIN · Listing · Price · Pieces · $ per piece · Est. units/30 d · Est. revenue · BSR · Rating · Reviews · Variations.

### 16. Competitor profiles
- One row per measured rival + us: heroes · variations · price · units · revenue · BSR · reviews · review velocity · keywords · organic vs paid split · placement behaviour · strengths · weaknesses · what it means for us.
- Section: each rival's top addressable keywords — Rival · Keyword · Kind · Weekly SV · Their traffic · Their paid · Their organic rank · Their SP rank · Placements · Our traffic · Our organic.

### 17. Hero ASINs & trends
- Heroes: Seller · Tier · ASIN · Share of seller traffic · Keywords led · Price · Rating · Reviews · Est. units · BSR · placement-score change.
- Movers (price, BSR, reviews, discount) over the window.
- Where rising rivals gain on core terms and we are behind.

### 18. Competitive keywords
- Every addressable market keyword: Keyword · Kind · Size · Segment · Relevancy · Addressable · Weekly SV · Market traffic · Paid share · Rivals present · Rivals advertising · Leader · Our organic · Our SP · Our traffic · Opportunity · Our decision · Landscape verdict.

### 19. Push terms vs field
- Columns: Term · Decision · Group · Our rank now · Competitor-tool organic · SP · Target · Weekly SV · Market traffic · Organic field (top 6 tracked, with tier) · Best rival SP · Rivals at SP #1–5 · Rivals with brand banner · Our paid share · Market paid share · First milestone (next beatable rival ahead) · Landscape verdict (stretch / winnable / reachable / we lead) · Why · Notes.
- Paragraphs: what this changes in how the push is judged — never how it is priced.

### 20. Gaps & how to fill
- Columns: # · Gap · Evidence · Why it matters · How to fill (inside break-even, ceiling, step, limit) · Rule · Validation.
- Plus: size battlegrounds (Size · Core keywords · Market traffic · Our traffic · Share · Keywords we lead · Avg organic · Most frequent leader); seed list (Term · Kind · Size · Weekly SV · Market traffic · Paid share · Leader · Our organic · Opportunity · Owner · How · Advertised variation); campaign structure (Area · Today · What the data says · Change).

### 21. Competitor ASIN targets
- Columns: Seller · Tier · ASIN · Share of seller traffic · Listing · Size · Their price · Our same-size price · Rating · Reviews · Est. units/30 d · BSR · In proposed build · Our campaigns targeting it · Today (performance) · Class (OFFENSIVE / TEST / AVOID / LOW TRAFFIC) · Why · Action.
- Footer: class uses price, pieces, rating, reviews only; money decisions on already-targeted ASINs still follow their own clicks and ACoS (a profitable AVOID is held at break-even, never scaled).

### 22. Competitor → decisions
- Columns: Rule · Decision area · Competitor signal · IF → THEN · What it never changes · Today's example · Status (standing / proposed / approved).
- Section: where each signal enters the pipeline (stage · input · rules).

### 23. Tests
- The campaigns: Id · Format · Keyword(s) · Advertised variation · Landing · Replaces which proposed build · Market traffic · Weekly SV · Rivals with headline / video · Start bid (break-even) · Ceiling · Budget/day · Why.
- Not built: builds · what · why not.
- Rules: When · Rule (start, daily step, 15-click re-baseline, 0-order stop, >2× break-even stop, read date, halo check, report).
- Build notes (by hand, budget line, creative, negatives).

### 24. Landscape check
- Crosstab: decision × landscape verdict (agrees / stretch / reachable / challenge / blind).
- Keyword list: Keyword · Decision · Clicks/Orders/ACoS 90 d · Market traffic · Rivals present · Rivals advertising · Our organic · Verdict · Why.
- Campaign-level checks: Decision · Landscape check · Verdict.

## 6. Placement, stock, money, exceptions

### 25. Placement
- Rules paragraph (70–90% top / ≤20% product pages for ranking; mix fix; discovery/conversion judged on ACoS; product-level split).
- Columns (campaigns with ≥15 clicks): Campaign · Group · Clicks 30 d · Top share · Rest share · PDP share · Top CVR · Rest CVR · PDP CVR · Top CPC · Rest CPC · PDP CPC · Placement read (leak / not competing / healthy / judged on ACoS) · Base now · Base new · Boost now · Boost new · TOS price now · TOS price new · Decision.

### 26. Variation & stock
- Per size: Size · Preferred (ranking) · Available · Units/day 30 d · Units/day 7 d · Cover (30 d pace) · Next dated arrival · Days to arrival · Inbound shipped · Current serving variation · Stock gate (ROOM / TIGHT / switch / none) · Verdict · Backup (same size) · Clearance (discovery) · Don't advertise (near-out).
- Per SKU: SKU · Units 30 d · Margin before ads/unit · Price · Break-even ACoS · Stock · Units/day · Days of stock · Role.

### 27. Inventory × PPC
- Steps table: Step · Check · Rule · Rule ID — count sellable units; pace (30 d, 7 d warning, never push pace); cover; zone (Green ≥60 / Yellow 21–59 / Red <21; a push needs projected cover to stay Green through its checkpoint — register #9, #42); minimum (<7 days); against the arrival (ROOM / TIGHT ≤7-day gap / switch); out of stock; discovery colour; events.
- Where each size stands: Size · Available · Cover · Next arrival · Stock gate · Push allowed?

### 28. Financial guardrails
- Columns: Guardrail · Formula · Product value · Crossed when · What happens · Rule.
- Rows: margin per unit; break-even ACoS; 2× break-even ACoS; break-even CPC; push ceiling; cost per order (push); target ACoS (non-push); spend limit; margin after ads; TACoS (reported); step limits.
- Per SKU grid: SKU · Margin · Price · Break-even ACoS · Break-even price at 10/15/20/25% CVR · Ceiling at 20% CVR.

### 29. Exceptions & BLOCK
- Columns: Code · Name · Condition · Treatment · Scope · Current cases (computed).
- Standard set: event days; attribution window; thin data; rank drop; at ceiling; paused; missing state; variation switch; size change; brand negatives; duplicate build; formats outside automation; shared campaigns; stock; listing flag; cap; big step; objective; spend limit; unmapped competitor.

## 7. Rows, operations, validation

### 30. Source rows (reviews)
- Every row the prior run proposed: Seq · Kind · Campaign · Now · Proposed · Prior review verdict · Our verdict (load / replace / hold / don't load) · Why.

### 31. New campaigns
- Builds: Seq · Type · Proposed campaign · Targets · Budget · Prior review · Decision (build on date / don't build / restart instead / test).
- Restarts: Campaign · Term · Variation · Price · When.

### 32. By hand
- Sections: variation switches (Campaign · Group · Now · Should be · When); objective tags (Campaign · Term · Now · Correct); push budgets (Campaign · Budget now · Budget new); SB/SD builds.

### 33. Validation plan
- Columns: When · What · Metric · Pass · Fallback · Rule.
- Minimum rows: daily push step read; day 3 at ceiling; daily spend vs limit; rank-drop watch; hero stock; day 1 after event; 7 days after mix fix; first settled read of cuts (break-even and non-ranking); weekly push tune; 50-click conversion stop; 14 days after harvest; 14 days after block; product-goal date; next events; test daily and read date; brand-defence re-read.

## 8. Checks (tab 34)
- Columns: Check · Result. Result is computed by the build from the workbook's own rows (count and PASS / FAIL (n)), never typed.
- Minimum computed checks (B6 set):
  1. No push price above 2 × break-even.
  2. No boost above 900%.
  3. No base cut deeper than 50% in one step.
  4. No push raise above +30% in one step (below ceiling).
  5. No price raise on non-push ranking campaigns during an event.
  6. Push budgets + expected other spend ≤ the spend limit (show the total).
  7. Every in-focus campaign has a decision.
  8. Every prior-run row has a verdict (show count).
  9. Every search term has a decision (show count).
  10. Brand and push terms never blocked.
  11. No bidding-strategy change written.
  12. No variation switch changes the size (list any allowed wrong-size corrections).
  13. Every failure has a status and a validation test (reviews).
  14. Every push / waiting / at-target term has a landscape verdict.
  15. All addressable market keywords pulled; all measured competitors profiled (show counts).
  16. No competitor rule sets or raises a price.
  17. Row census: campaigns in scope = decision rows; how many added from outside the list.
- Then run the full quality gate (reference 12 §7) and record its result on this tab: RAN / NOT RUN per group, failures by check.

## 9. Optional tabs
| Tab | When | Columns |
|---|---|---|
| Data conditions | Any unresolved data issue | Condition · Evidence · Why it matters · Actions gated · Owner · Due · Status (withdrawn findings kept with overturning evidence) [DR, PB] |
| Impact ledger | Any refinement cycle | Key · Campaign · Target · Lever · Before → after · Logged · Expected metric/direction/tolerance/horizon · Execution (executed / not / partial) · Grade (worked / flat / backfired / too soon / event window / confounded / provisional) · Consecutive no-impact · Escalate [SR] |
| Timeline | Events in the window | When · What [B6] |
| Negatives | Many negatives | Seq · Campaign · Negatives now · After · Terms · Verdict · Why [B6] |
| Deployment waves | Multi-step rollouts | Wave · Date · Rows · Daily $ · Cumulative $ [WB] |
| Brand management log | Listing/offer findings | Finding · Evidence · Recommendation · Owner · Expected effect [PB, LTSF] |


---

<!-- FILE: templates/decision-trail-examples.md -->
# FILE: templates/decision-trail-examples.md

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


---

<!-- FILE: examples/b6-case-study.md -->
# FILE: examples/b6-case-study.md

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
4. **Push qualification** (all required): a plan, CVR above market at the top, within ~30 places of target, hero stock ≥7 days and ≥ days to next arrival, keyword live, ceiling ≥ own TOS cost per click, no listing flag. Failing one → WAIT with the reason. (This framework adds the zone gate: advertised SKU Green ≥60 days with projected cover staying Green through the push checkpoint — register #9, #10, #42 — so a Yellow hero such as Queen White at 42 days pushes only with a time-boxed owner acceptance.)
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
| Value position | 6 pieces at $72/$68 vs 4-piece sets at $80–135; 3,128 reviews at 4.4★ vs niche median 2,630 | Conquest only on OFFENSIVE pages (pricier, fewer pieces, or same price with far fewer reviews; a new target must also win ≥2 of price / rating / review count — register #44); AVOID Bedsure ($60–70, 65k reviews), $40 sets, microfiber |
| Generic sheets | Led by $15–50 microfiber sets | Left to discovery at break-even; never pushed |

Standing rule throughout: **competitor data never set or raised a price** — break-even, the 2× ceiling, the +30% step and the spend limit stayed as they were. Competitor bids, conversion rates and review themes were not available and were not assumed.

## 7. The Sponsored Brands / video test
Approved by the product owner on 29 Sep; built by hand (the engine wrote Sponsored Products only).
- **Six campaigns, one format per term**: headline (product collection) on "bamboo sheets"; video on "bamboo sheets queen size", "bamboo sheets king size" (a waiting SP term — tests it without lifting the SP ceiling) and "bamboo cooling sheets" (8 rivals run video there); store-spotlight headline on the brand terms; Sponsored Display on our own product pages.
- **Budget**: $85/day for 14 days (~$1,190), a separate line inside the product's spend limit from 1 Oct, outside the SP push budgets.
- **Prices**: start bid = break-even with the size's TOS CVR (King White $15.97 × 20.0% = $3.19; Queen White $19.51 × 16.2% = $3.17); raise ≤30%/day while the banner isn't showing, never above 2× ($6.38 / $6.34) — under register #45 the 2× applies only on push terms and on brand terms with verified competitor presence, 1× elsewhere; at 15 clicks switch to the campaign's own CVR.
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
