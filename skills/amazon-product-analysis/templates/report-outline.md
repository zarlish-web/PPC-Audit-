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
