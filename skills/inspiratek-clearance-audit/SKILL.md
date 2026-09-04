---
name: inspiratek-clearance-audit
description: Build the Inspiratek/Ecotero product audit and clearance plan for an Amazon parent carrying aged inventory — a full leak audit across every lever (cost structure, storage, price, traffic, click, conversion, refunds, PPC, demand, execution), a spend-to-volume model, a decided bulk workbook with a written reason on every row, and new SP/SB/SD campaigns. Use this whenever the user asks for a clearance plan, liquidation plan, LTSF plan, PPC audit, decided bulk, or aged-inventory analysis for a product, or uploads a Sellerboard export, FBA inventory report, PPC bulk, MKL/SQP file, AdInsight export or LTSF what-if and wants to know what to do about slow-moving stock. Also use it when asked why a product is not converting or not selling, when asked to scale spend or find more keywords and campaign types on an aged product, or when reviewing or correcting an existing clearance plan. Applies to any parent ASIN with a liquidation or clear-the-stock objective.
---

# Inspiratek Clearance Audit

Builds the product audit and clearance plan for an Amazon parent carrying aged inventory. Output is three artefacts: a plan document, a decided bulk workbook, and where the situation calls for it a standalone pricing proposal.

The governing idea: **advertising is usually the smallest leak on an aged product.** Quantify every lever first, rank by size, then size the PPC plan against what it can actually deliver. A plan that only addresses advertising typically addresses 8–15% of the loss.

A plan that goes straight to campaigns is the characteristic failure of this work. It looks complete, it is defensible row by row, and it fixes the tenth-largest problem.

## Where this sits, and what outranks it

This skill is the **aged-stock branch** of the account's PPC family. It does not own the economics.

| Question | Governed by | This skill's part |
|---|---|---|
| Break-even, ACoS bands, objective assignment, per-SKU gates, verdict vocabulary | `pmp-optimization-sr` → `reference/decision_framework.md` — **locked canon** | Read it, cite it, never restate it differently |
| How a decision is written and validated | `ppc-decision-reasoning` | Applies to every row this skill writes |
| The plan document and the execution workbook | `ppc-plan-builder`, `ppc-workbook-builder` | This skill supplies the clearance content they carry |
| **The leak audit, the refund gate, product-ad attribution, the data traps, clearability, publishing** | **This skill** | Its actual contribution |

**Where this skill and the locked canon disagree, the canon wins and the disagreement is reported, never silently resolved** — except where the account has ruled. One such ruling is standing and it governs this whole skill:

> **RULING — the clearance ceiling is forward cash.** On a liquidation product, PPC is the lever that moves the stock. Spending a little beyond profitable is accepted, because the charge avoided is worth more than the margin given up. A negative contribution does **not** stop the push and does **not** by itself send the product to pricing. Recorded 4 September 2026.

Two consequences, and they are the opposite of what the canon alone would do:

- **The plan does not stop on negative CM.** It still recommends pricing work where price is the bigger lever — that goes in the Brand Management findings alongside the push, not instead of it.
- **The job is to spend the clearance budget well, not to spend as little as possible.** Fund it properly, cover the term set widely, and control cost through the bid rather than by starving the lane.

The canon's own §3 permits this: LTSF-Clearance is one of the three labeled investment objectives that may exceed break-even **while capped, dated and logged**. This skill supplies the cap, the date and the log.

## How a run is assembled

Every product runs through the same pipeline whatever the objective. What changes for liquidation is **§1.1 — the objective re-tag** — and what that re-tag then makes legal or illegal downstream.

**What the operator supplies**

1. **The Final Bulk** — one sheet built at our end carrying every campaign, ad group, keyword, target, product ad, negative and bidding-adjustment row for the product, with `Action`, `Reasoning`, `New Bids`, `New Budget` and `New Percentage` **blank**. This is the file the run fills in. It is never rebuilt from scratch and its column order is never changed.
2. **The raw data files** — the intake list at §1.
3. **The objective**, stated. For this skill it is clearance; if it is not, this is the wrong skill.

**What the run does, and with which skill**

| Stage | Skill | Produces |
|---|---|---|
| Analysis and economics | `pmp-optimization-sr` (canon) + **this skill** | Break-even, gates, leak audit, refund tiers, clearability |
| The written plan | `ppc-plan-builder` | The plan document |
| Filling the decision columns | `ppc-decision-reasoning` | `Action`, `Reasoning`, `Reverses If` on every row that changes |
| Assembling the workbook | `ppc-workbook-builder` | Final Bulk filled, plus the added tabs below, in the account's real tab set |

**What comes back**

- **The plan document** — the analysis and the argument.
- **The Final Bulk, filled** — campaign-, ad-group-, keyword- and placement-level actions written into the blank columns. Nothing added, nothing reordered.
- **New-campaign tabs** where the plan proposes a build — one per ad product, SP / SB / SD kept separate, each row carrying its build class, targeting, match type, SKU set, bid, budget and the gate it waits on.
- **A negation tab** — every negative to add, with the campaign it goes into, the mode, and the evidence standard it met.

The build classes and what may be proposed under a clearance objective: `references/objective-and-builds.md`.

---

Two gates still stand, and neither is an economics gate:

- **Gate the push on stock, not on profit.** GREEN (overstock, room to clear) → push. Not GREEN (already low) → **do not push**; that stock clears by itself and spending on it buys nothing. Never run a clearance push on a SKU whose hero size is nearly out — clear the aged variation, protect the hero. *This gate is about how much stock is left, not about whether the maths is profitable. The ruling above removed the profit gate; it did not remove this one.*
- **Under negative CM, pricing still goes to Brand Management** — as a recommendation running alongside the push, never as a reason to withhold it.

## Budget is not a waste lever

**On a clearance product the default direction for budget is up or hold. Never down as an efficiency action.**

The reasoning is arithmetic, not preference. **A daily budget is a cap, not a spend.** It only turns into money if the auction lets it. So cutting a cap the campaign was never reaching saves nothing at all — it just removes the headroom the lane needed to grow into.

On one live product the enabled budget was $343.73/day and actual spend was $38.12/day — 11%. A plan that cut the cap to $89 released **$0.00 of real money** and capped every lane's upside. That plan looked disciplined and did nothing except make the product smaller.

**Waste is not a budget. Waste is a specific target taking clicks and returning nothing.** You remove it where it lives — at the keyword or product target — and the budget stays where it is, now buying better traffic.

| Situation | The wrong move | The right move |
|---|---|---|
| Campaign spends 11% of its budget | Cut the budget to match spend | Give it more targets and check the bid — it is short of reach, not of money |
| Campaign is over its ceiling | Cut the budget | Walk the bid down, pause the wasteful targets inside it |
| A keyword has clicks and no orders | Cut the campaign budget | Pause or negate that keyword |
| Every target in a campaign is waste | Starve it | Pause the campaign |

**Budget only comes down in two cases**, and both are stated as such:

1. **The campaign is paused entirely** — it cannot serve, or nothing in it is worth running.
2. **The lane is genuinely at its cap and the money is worth more elsewhere.** Only a lane actually spending its budget can release money by giving some up. A lane at 11% releases nothing.

Anything else is a raise or a hold.

## What counts as wasted, and when

Judged per keyword or per target, never per campaign.

| Condition | Verdict |
|---|---|
| Zero orders, **15+ clicks** at ordinary click prices | Review now — pause or negate if it also fails relevance |
| Zero orders, **20–25 clicks** where the click price is very low (about $0.15 or under) | Review now — cheap clicks earn more patience before judgement |
| Zero orders, **below that click count** | **Not waste.** Keep running, keep watching. It has not had its chance |
| Any orders at all | Not waste. It is delivering — correct it gradually, per §8 |

**The click line is a review trigger, not an automatic pause.** At the line, look at the term itself: does it describe this product, does it carry real search volume, is it the kind of traffic we want. A term that is genuinely relevant and simply unlucky may earn another window; a term describing something we do not sell is negated the moment it is seen, without waiting for any click count.

**A term below the line is never touched on performance grounds.** Zero orders on 6 clicks is not evidence of anything. Cutting there removes the discovery surface that finds the cheap orders.

## Operating floors — below these, nothing works

**A campaign is either funded properly or it is paused. There is no middle.** Below these levels a campaign cannot win enough auctions to produce a readable result, so the money is spent and nothing is learned.

| Floor | Default | Meaning |
|---|---|---|
| Minimum bid | **$0.25** | Below this the bid does not clear enough auctions to matter |
| Minimum daily budget | **$5.00** | Below this the campaign cannot deliver a readable day |

**Confirmed 4 September 2026 — these are defaults, not universal constants.** A product may set its own floor where its own click economics justify it. Where clicks in a category genuinely cost $0.08, a floor of $0.15 is legitimate and the plan says so.

An override is not a free hand. It is valid only when all four hold:

- The override is **stated in the plan**, both numbers shown — the default and the product's own
- The reason is **measured on this product or its category**, with the figure in it. "Clicks here average $0.08 across 340 clicks" is a reason; "the floor felt high" is not
- It moves the floor to a level that **still buys a readable result**. A lower floor is only lower, never a way to fund a lane that cannot deliver
- The **paused-or-funded rule survives it.** Whatever the floor is set to, nothing is cut to a value between zero and that floor

Where no override is stated, $0.25 and $5.00 govern.

**When the computed ceiling falls below the floor, the floor governs.** A ceiling of $0.23 does not become a $0.23 bid — it becomes a $0.25 bid, and the gap is written down as accepted over-ceiling spend with the charge it is avoiding. That is exactly the "capped, dated, logged" exception, used deliberately rather than drifted into.

**Never cut a campaign to a number between zero and the floor.** Cutting a $75/day campaign to $2.94 produces a lane that spends money and cannot deliver. Either it earns $5/day or it is paused, and the plan says which and why.

## Do this in order

0. **Grade the prior cycle** — verify what was executed, grade what it produced, before anything else
1. **Intake, verify, and re-tag the objective** — reconcile every source, then set every campaign to clearance
2. **Quantify the leaks** — dollars per month, every lever, with an owner
3. **Diagnose** — exposure vs conversion, syntax, size, variant, competitors
4. **Gate on refunds** — tier the SKUs before any spend is routed
5. **Set the ceiling** — storage-adjusted, per unit *cleared*, bounded
6. **Test clearability** — can traffic move this stock at that ceiling at all
7. **Model spend to volume** — what each budget level actually buys
8. **Decide the existing account** — released spend funds the new build
9. **Build new campaigns**, then **write it up**

Do not skip to step 9. The build is sized by steps 5 to 7, and steps 4 and 6 can close it entirely.

---

## 0 · Grade the prior cycle

**Runs before any analysis, whenever a prior cycle exists.** A cycle that does not read the last one is the first cycle done twice, and the whole point of running this repeatedly is that each pass knows what the last pass tried.

**Verify execution before grading anything.** Check every prior action against the **current** bulk and the **current** inventory, never against the plan that describes them. An action that never deployed is not a failed lever, it is an unexecuted one — grading it teaches a false lesson. Report the execution rate as a number; a cycle where half the actions never shipped is a process finding that outranks every performance finding in the same document.

**Grade against the objective, not against advertising metrics.** Units cleared, aged-pool drawdown, cost per unit cleared, months to clear, charge actually accrued, subsidy per unit at realised conversion. Reconcile the pool drawdown against sales plus removals rather than trusting one source.

**A unit shipped is not a unit cleared.** On a product returning 22%, one in five units counted as cleared this cycle comes back next cycle and re-enters the aged pool. Grade on units cleared; a grade taken before the refund window closes is marked **provisional with a re-read date**.

**Six grades, and each licenses something different:** WORKED, FLAT, BACKFIRED, TOO EARLY, NOT EXECUTED, CONTAMINATED. **A lever below half its prediction is replaced, not deepened** — repeating an underperforming lever is the most common way a product loses three cycles in a row.

**The grading feeds this cycle's decisions rather than sitting in a section at the back.** A BACKFIRED lever is not proposed again. A FLAT-twice lever is replaced, and the replacement says what it does differently. A child whose velocity moved gets a recomputed ceiling before anything is staged against it.

**On a first cycle there is nothing to grade, and that is stated rather than skipped.** What the first cycle owes the second: a prediction on every action in the units the next cycle will measure, a read date accounting for the refund lag, the dated baseline, and the decided file retained so execution can be verified against it.

Full method, grade definitions and checks: `references/prior-cycle-grading.md`.

---

## 1 · Intake and verification

Required per product. Say up front what is missing rather than discovering it at step 7.

| # | File | Gives you |
|---|---|---|
| 1 | PPC bulk export, multi-window (7/14/30d) | Campaign, keyword, PAT, placement rows with metrics |
| 2 | Sellerboard products by parent, 30d | Units, refunds, sales, ads, ASP, sessions, per SKU |
| 3 | Sellerboard products by parent, 7d | Current-week read |
| 4 | Sellerboard P&L weekly, 3 months | Trend, deal effect, refund lag |
| 5 | FBA inventory + aged-inventory report | Available, reserved, age bands, AIS, storage |
| 6 | Keyword-Level Master Data with SQP | The whole diagnosis. Without it you cannot separate exposure from conversion. |
| 7 | AdInsight exports, 8–10 competitor ASINs | Competitor ad activity and placement mix |
| 8 | Sellerboard product cost export | COGS, and catching unit-vs-landed mismatches |
| 9 | LTSF charge projection + SKU detail | Storage per unit, landed COGS, FBA fee |
| 10 | LTSF what-if model | **The velocity target and break-even ad cost. Always read the Assumptions tab, not just outputs.** |
| 11 | Deal tracker | Deal calendar, allocation, uplift history |
| 12 | Placement report | Required for step 8. Without it no modifier may be set in either direction |
| 13 | Decision-template bulk | Where decisions get written |
| 14 | Slack thread for the product | Lever history, rulings, return reasons, listing changes, who owns what |
| 15 | **The prior cycle's decided file and its logged predictions** | **Required where a prior cycle exists** — step 0 cannot run without it, and without step 0 this is a first cycle repeated |
| 16 | The prior cycle's action log or impact ledger | What was decided, what was executed, how it graded |
| 17 | **The live variation family from Seller Central** | **Every size and colour we actually sell, with stock. Required — see below** |

Optional but valuable: parent-level SQP with cart-adds, ASIN Insights, competitor price history, removal order detail, per-SKU floor prices.

**Build the verification table before any analysis.** Every figure that later carries weight needs a named governing source. See `references/data-traps.md` for the contradictions that recur — read it before trusting any number.

### 1.0 Build the catalogue matrix, before a single keyword is read

**Added 4 September 2026, after a live catch by the account owner.**

The rule "negate any term naming a size, colour or feature we do not sell" appears in **five places** in this skill. On a live product it was never applied — because nothing required the catalogue as an input, and no gate checked it. A plan went out proposing **Twin XL, California King, Full and Super King keywords on a product sold only in Twin, Queen and King.** Three live keywords naming colours we do not stock were sitting in the account about to have their bids raised.

**A rule nobody can execute is not a rule.** So the catalogue is now an input, and building the matrix is a numbered step.

1. **Pull the live variation family** — every child SKU, its size, its colour, its stock, its listing status.
2. **Write the matrix out explicitly**: the sizes we sell, the colours we sell, and any gaps inside the grid. State the piece count per size where it differs — a 2-piece twin and a 3-piece queen are different products to a shopper searching "3 piece".
3. **Write the complement too** — the sizes, colours, materials and bundles we do **not** sell. That list is what the scan runs against, and it is longer and more useful than the list of what we do sell.
4. **Scan every keyword** — live, proposed, and in the master list — against the complement. Anything naming an attribute outside the catalogue is a structural negative, at any click count.
5. **Put the matrix in the workbook** as its own tab, so next cycle re-runs the check instead of re-deriving the catalogue.

**Check the adjacent-category terms separately, and keep the distinction.** A cross-category term like *comforter* is not a catalogue mismatch — it is a deliberate bet that a lightweight summer quilt serves that intent, and it belongs in an isolated lane with a refund kill-switch. A term naming a size we have never sold is not a bet; it is an error. Do not let the second hide inside the first.

**Out of stock is not the same as not in the catalogue.** A size we sell but currently hold at zero is a stock gate, read per cycle and reversible on replenishment. A size we have never sold is structural and permanent. The negatives tab says which basis applied.

### 1.1 Re-tag the objective before any row is read

**This is the step that makes a liquidation run different from every other run, and it happens once, at the top.**

The standard mapping assigns objectives from targeting type — brand keyword to Defensive, **Exact to Ranking**, auto and broad to Discovery, product targeting to Profitable Conversion. **On a product whose objective is clearance that mapping is wrong**, and applying it silently is how a liquidation product ends up with a rank programme inside it.

| Live objective on the account | Becomes, on a clearance product |
|---|---|
| Ranking / Re-Ranking | **LTSF-Clearance** |
| Market Share | **LTSF-Clearance** |
| Discovery | **LTSF-Clearance** — the reach layer serves the same purpose here |
| Profitable Conversion | **LTSF-Clearance** |
| Defensive on a brand term | Defensive stays. Owned demand is not aged stock |

Objective is a campaign property, one per block, taken from the campaign row. Re-tag the campaign, not the keyword, and record the prior value so the change is auditable.

### The label always changes. Performance decides what happens to the bids

**Confirmed 4 September 2026.** Two separate decisions that are easy to confuse:

**1 · The label changes on every campaign.** No exceptions beyond Defensive on a brand term. **We are not pushing for rank any more — we are pushing for sales**, regardless of placement and regardless of how well the rank push was going. A campaign is not left on a Ranking objective because it was doing well at ranking; that is exactly the campaign that would quietly keep spending on rank while the stock ages.

**2 · What happens to its bids is decided on what it is producing now**, never on what it used to be for.

| What the campaign is producing | What happens to the bids | Label |
|---|---|---|
| **Orders at a profitable ACoS** | **Nothing. Leave it running exactly as it is.** It is already doing the job | Re-labelled |
| **Orders, but ACoS above profitable** | **Diagnose the placement first.** Find which placement carries the cost, correct that modifier, then move the bid | Re-labelled |
| **Moderate results** | Adjust per the correction ladder | Re-labelled |
| **Poor results** | **Pause.** There is nothing here worth re-pointing | Re-labelled, then paused |

So "keep it running" means the **bids, budget and structure are untouched** — not that the objective stays. The campaign carries on producing exactly as it did yesterday, but it is now counted, judged and funded as a clearance lane: measured on units cleared, barred from new rank spend, and never sized against a rank goal.

**Placement comes before the bid.** When a delivering campaign's ACoS is too high, the first question is not "how much do I cut" — it is **"where is the cost coming from?"** Pull the campaign's own placement report and read Top of Search, Rest of Search and Product Pages separately. A campaign can look expensive overall because one placement is expensive while the other two are fine. Cutting the bid then punishes all three and loses the cheap orders along with the dear ones. Correct the modifier that is actually causing it, re-read, and only then apply the ladder to the bid if it is still over. See `references/placement-tiers.md`.

**Reading placement for cost is not the same as buying placement for rank**, and the re-tag bars only the second. Correcting a modifier because Top of Search is running at three times the campaign's ACoS is cost control and is always allowed. Raising a modifier to hold a position, or keeping an expensive placement because rank would slip, is rank spend and is barred. The test is what the plan says the modifier is *for*.

**This is why almost nothing gets "abandoned mid-push".** A campaign that was earning keeps earning at the same bids. What ends is the rank programme around it — the target, the position goal, the sizing — not the campaign.

**What the re-tag makes illegal.** Every one of these is barred on a re-tagged campaign, and a plan carrying one has not re-tagged:

- Rank targets, rank movement as a success measure, and the seven-state ranking progress test — there is no rank objective to progress toward
- The top-of-search modifier ladder used to buy position — modifiers are still set, but from cost, never from rank
- Holding an expensive placement on the grounds that rank would slip if it were corrected
- DSTR and target-clicks sizing derived from a rank goal
- Any bid above the ceiling justified as a sized, capped ranking push
- Exact-match expansion on unproven terms

**What it makes the governing measures.** Velocity, months to clear, cost per unit cleared against the ceiling, and the charge avoided — judged on total units shipped, never on ad-attributed orders alone.

**Where a campaign was mid-push and performance stopped it**, say so and state what is being abandoned — the campaign, what it was chasing, how far it had got, and roughly what was spent getting there. A rank programme stopped halfway is a real cost and the document owns it rather than letting it disappear in a re-label. Where no rank history was supplied, the plan says "prior objective was Ranking, no rank data supplied to measure what is lost" and moves on. **This never blocks the run** — it is a disclosure, not a gate.

It does not apply to a campaign kept running at a profitable ACoS. Nothing was abandoned there.

### 1.2 Four rules that govern every figure downstream

**Attribute through product-ad rows, never campaign totals.** A campaign that carries this product's ad may carry five hundred others. Filtering "campaigns containing this product" and summing their spend can overstate by multiples. See `references/attribution.md`.

**Prefer the count over the derived field.** A raw count — units, orders, clicks, dollars charged — is an observation. Days-on-hand, months-on-hand, months-to-clear and break-even are calculations that inherit every error beneath them, and on this lane they feed the ceiling directly. Where the two conflict, the count governs and the derived field is unreadable until reconciled.

**Staleness is a property of the file, not the field.** A file with one field known stale has no clean fields, only unchecked ones — price, cost, unit counts and every derived column came from the same pull. Verify two or three against an independent source; if any fails, quarantine the whole file.

**Ask rather than resolve.** Where two sources disagree, a figure will not reconcile, or a column's definition is not obvious, ask whoever prepared the data. Ask whenever the answer touches **the ceiling, the pace, the archetype or the disposition**; otherwise record it as a figure to reconcile and continue. Never silently resolve a vocabulary difference — *liquidate*, *aged*, *clear*, *terminal* and *floor* carry house meanings that differ from their ordinary ones, and reading one wrongly produces the opposite recommendation. While waiting, finish what does not depend on the answer and mark the dependent branch blocked. A blocked branch is visible; an assumed one is not.

---

## 2 · The leak audit

**This step is what separates a clearance plan from a PPC plan.** Ten lever groups. Quantify each in dollars per month; if it cannot be quantified, say so rather than describing it qualitatively — an unquantified leak cannot be ranked against a quantified one.

1. **Cost structure** — landed COGS, FBA fee, cube, referral, refund cost per unit
2. **Inventory and the clock** — days of cover per SKU, storage + AIS per unit per month, age bands, removal execution
3. **Price and offer** — position on the ladder, realised vs list, promo, deal depth, offer types enabled
4. **Traffic** — impression share, keyword coverage, syntax and size index, surfaces used vs available
5. **Click** — brand CTR vs market, main image, title, badges
6. **Conversion** — brand CVR vs market, purchases per impression, click-to-cart, content, reviews, variations
7. **Retention** — refund rate, sellable quota, reason codes, by SKU, deal lag
8. **PPC efficiency** — placement pricing, syntax mix, SKU routing, zero-order spend, harvest, match mix, utilisation
9. **Demand beyond search** — deal cadence and measurement, off-Amazon, MCF
10. **Execution** — do decided changes appear in the account

Then produce the ranked table: leak, dollars per month, owner, basis tag, fixable now. **Rank by size, not by which team is in the room.** Assign an owner to every line — a leak with no owner is itself the finding — and **state what share of the total loss the PPC plan addresses**. If that share is small, say so in the opening lines of the document rather than burying it.

Full method and the worked shape of the table: `references/leak-audit.md`.

---

## 3 · Diagnosis

**Exposure vs conversion.** From SQP: impression share, brand CTR vs market, brand CVR vs market, and purchases per impression. This is the most valuable single step. A product can look like it converts badly and actually be outperforming per impression while holding 0.02% of them. Without the MKL/SQP file this step cannot run — say so at the top of the document, because every traffic verdict below is then provisional.

**Syntax and size index.** Index each on purchases-per-impression against market. The syntax carrying the most spend is often the one indexing worst. Include the classifier's discard bucket — it is frequently the best-performing traffic.

**Variant demand against stock.** Match keyword demand per colour or size to units on hand. Look for a large stock block with no searchable demand; it caps what any plan can promise.

**Competitors.** AdInsight for ad activity, Data Dive for sales, rank, price and reviews. Compute ad impressions per unit sold — it separates sellers converting organic demand from sellers buying it. Identify which model is copyable given our review base and listing age.

**Reach vs budget.** Before concluding a lane is underfunded, check whether it is reachable. Compute the impressions and clicks the proposed spend requires at the current click price, against what the lane actually delivers. A lane an order of magnitude short on impressions is impression-constrained, and no budget change reaches it.

---

## 4 · The refund gate

**Runs before any spend is routed, not after.** If refund rates vary by variant, days-of-cover routing alone will send money at stock that comes back.

**Why this is a step and not a diagnosis item.** The earlier version of this skill kept the refund read inside step 3, as one of several things to look at. It moved out for two reasons, and it should not move back without a reason of the same weight:

1. **Step 5 cannot run without it.** The ceiling test is cost per unit *cleared*, and that is `cost per unit shipped ÷ (1 − refund rate)`. Read the refund rate after the ceiling and the ceiling was computed on the wrong denominator.
2. **A tier stops work.** BLOCK pauses a SKU; FLOOR forbids scaling one. Something that stops work is a gate, and a gate belongs before the thing it gates — not alongside observations that only describe.

```
ad cost per unit cleared = ad cost per unit shipped ÷ (1 − refund rate)
```

| Tier | Condition | Action |
|---|---|---|
| **BLOCK** | Reliable sample, rate at or above 35% | Pause. Advertising converts spend into reverse logistics |
| **FLOOR** | Reliable sample, 22–35%, or named in quality complaints | Keep live at a reduced budget. Marginal, not loss-making. **Do not scale** |
| **FUND** | Everything else | Advertise normally, carry on every new campaign |

Require at least 10 units sold in 30 days before acting. Restrict Auto and remarketing SKU lists too, or they route traffic to blocked variants anyway.

**A FLOOR SKU cannot be the growth story of the plan.** If the diagnosis points at a FLOOR variant as the largest remaining job, the finding is that the refund rate is the constraint and the fix is not a PPC fix.

Full rules, the worked table and what to do when the gate contradicts the search data: `references/refund-gate.md`.

---

## 5 · The ceiling — three numbers, and the bid sits between them

**Forward cash governs the decision. Break-even is not discarded — it is the reference point you must know before you decide anything.** One tells you what you may spend; the other tells you where profit actually ended. Working without the second is flying blind, even when you have ruled that the first wins.

Compute all three, every time, per child:

| | What it is | What it means |
|---|---|---|
| **1 · The floor** | $0.25, or this product's stated override | Below this the bid wins nothing. Binding once set |
| **2 · Max profitable CPC** | `margin $ × CVR` | **Where profit ends.** Past this the sale itself loses money |
| **3 · Max click price** | `(contribution + avoided charge) × CVR` | **Where forward cash ends.** The hard cap — never exceeded |

```
break-even ACoS    = (ASP − COGS − Amazon bundled fees) ÷ ASP     no return allowance
margin $           = ASP − COGS − Amazon bundled fees
max profitable CPC = margin $ × CVR                                       ← number 2
avoided charge     = MONTHLY charge per unit × min(clearance window, months to clear)
ceiling            = contribution + avoided charge
max click price    = ceiling × CVR                                        ← number 3
```

**Read the charge as one month, and read the window from the declaration.**

The charge file carries **one month's charge** — September's charge, billed on September's billing date. It is not a multi-month figure and must not be used as one. Divide it by the charge-bearing units to get charge per unit per month, then multiply by the window.

**The clearance window is a deadline handed to PPC, not a number PPC picks.** It comes from the LTSF programme with the charge target. Two months is the common case, so it is the default when nothing else is stated — but it is **read per product per cycle, and where nobody has stated it, ask rather than assume two.** A product given a one-month window has a one-month cap.

The window is capped again at the real clearance time: `min(window, months to clear at realised velocity)`. Stock that will be gone in six weeks cannot avoid two months of charge, because the second month was never going to be paid.

**The window is a deadline, never a pace to hold.** If the stock can clear sooner, clear it sooner — the charge stops the day the unit ships, and finishing early is the objective, not overachievement.

### The charge bills on a date, so the value of clearing steps

This is the part a smooth monthly model hides. A unit sold the day before billing avoids the whole month's charge. The same unit sold the day after avoids none of it.

On one live product: $849.89/month across 233 charge-bearing units is **$3.65 per unit per month**, billing on the 15th. From the 4th that is 11 days, and at 2.95 units/day about **32 units can clear before billing — $118 of charge avoided by hitting the date rather than missing it.**

So the plan states the **billing date**, how many units can realistically clear before it at current pace, and what that is worth. Deployment waves are sequenced against that date, not against a tidy week boundary.

**The zone between 2 and 3 is the subsidy zone.** Spending there is deliberate: the sale loses money and the avoided storage charge pays for it. That is the ruling, and it is legitimate.

**Bid low in the zone, not at the top of it.** Number 3 is a maximum, never a target. Start near the bottom, and move up only when volume genuinely requires it — every cent above number 2 is money the charge has to justify.

### The subsidy check — what makes this disciplined rather than a blank cheque

At any bid, you can price exactly how much you are subsidising and test it against what you are buying:

```
subsidy per click = bid − max profitable CPC
subsidy per unit  = subsidy per click ÷ CVR
```

**The test: is the subsidy per unit less than the charge avoided per unit?**

- **Yes** → the forward-cash argument holds. The spend is justified and the plan says so with both numbers.
- **No** → you are paying more to avoid the charge than the charge costs. That is not forward cash any more, it is just loss, and it is logged as such with the gap in dollars.

This is the same boundary as number 3 expressed per unit rather than per click, so it never contradicts the ceiling — it just makes the ceiling's meaning visible to a reader who does not want to re-derive it.

### When the floor sits above the ceiling

It happens, and it is not an error. On one live product:

| | White | Black |
|---|---|---|
| Floor bid | $0.25 | $0.25 |
| Max profitable CPC | $0.067 | $0.091 |
| Max click price | $0.234 | $0.236 |
| Subsidy per unit at the floor | $8.40 | $5.40 |
| Charge avoided per unit | $7.68 | $4.92 |
| **Gap** | **$0.72 over** | **$0.48 over** |

Both children's whole workable band sits **below** the minimum bid that buys anything. The floor governs, the product runs at $0.25, and the plan states plainly that each unit carries roughly 50–70 cents of loss beyond what the avoided charge justifies.

**That is a finding, not a rounding note.** It says the clearance case is marginal at any bid, and it belongs next to the pricing recommendation going to Brand Management — because a small price move changes every one of these numbers.

### Rules that still hold

**COGS never enters a live decision column on aged stock.** Identical across every option for the same units, so it cannot change which option wins.

**The ceiling test is cost per unit *cleared*, built from cost per unit *shipped*.** Not cost per ad-attributed order — the two can differ by four times. CPA per order is for keyword-level decisions only.

**A campaign shipping more than one child takes a ceiling weighted by the children it actually ships** — not its name, not the lower child by default.

**Count the charge once.** Either inside the fees line reducing contribution, or added back as avoided charge. Never both.

**Months-to-clear is computed, never read** — from charge-bearing units at realised velocity.

**`min(2, months to clear)` takes whichever is smaller.** Two months is the most the plan may claim; stock clearing sooner claims only the shorter period, because the rest of the charge was never going to be paid.

**Deal-state and clean-state are computed separately, never blended.** Clean-state governs ordinary decisions.

**Every anchor is stale past 45 days, or after any price, fee, packaging or LTSF change.**

Construction, worked examples and the per-campaign blend: `references/ceiling-and-attribution.md`.

---

## 6 · The clearability gate

**Ask whether traffic can clear this stock at all, before deciding anything about how to build.**

```
required units per day  = remaining units ÷ days to the cliff
required clicks per day = required units per day ÷ conversion rate
market click price read AT THAT VOLUME, not at the volume the lane buys today
```

| Result | Meaning | What follows |
|---|---|---|
| **OPEN** | Market click price at the required volume is at or under the ceiling | Fund the full required-clicks budget |
| **SPLIT** | Only a residual volume clears at or under the ceiling | Buy what the ceiling buys; state the residual and route it |
| **CLOSED** | No volume clears at or under the ceiling | Build nothing. Hand back five numbers: required clicks/day, the ceiling, market CPC at that volume, units clearable at the ceiling, the residual |
| **UNMEASURED** | Too few converters to read a conversion rate at all | Reach layer at floor bids to accumulate clicks, with a dated read |

**A closed lane is a correct outcome, not a failure.** It routes the choice to a price move or a terminal option, both of which recover more than spending above the ceiling. The response to a closure is never to widen the term set.

**Charge size never overrides this gate.** The largest charge in a portfolio is frequently the least clearable stock in it, because low velocity is what aged it. Clearability decides whether to build; charge decides only how much.

---

## 7 · Spend to volume

Do not project from current CPC without first modelling what removing an inflated Top-of-Search modifier does. On one product that single change was worth a 60% volume lift at unchanged budget, and omitting it made the whole plan read as unambitious.

```
clicks    = spend ÷ CPC
ad orders = clicks × ad CVR
units     = ad orders ÷ attribution rate
```

Degrade both as spend rises — CPC climbs roughly 14% per natural log of the spend multiple, conversion falls roughly 11%. Show impression share at each level as the reality check: if a row implies a share far above what any competitor holds, it is not real.

Then compare storage saved against extra ad cost at each level. Net benefit usually peaks low and erodes; recommend on months-to-clear rather than on the maximum net figure, and say why.

**State the stock ceiling.** Units ÷ velocity is often a harder limit than budget.

**An under-spending lane is short of reach, not short of money.** Adding budget to a lane running at 11% changes nothing, and taking budget away from it saves nothing. Both moves are noise.

What actually converts an under-spending clearance product into units is **more reachable surface**: more relevant keywords, the auto campaign's four groups, category targeting, product targeting, and the other ad products.

**So the plan's growth lever is targets, and its cost lever is the bid.** Neither is the budget.

**State each lane's case with its impression numbers.** A lane far short on impressions gets more targets. A lane at or near its cap gets more budget. A lane over ceiling gets its bid walked and its waste cleared. Only a lane genuinely at its cap can release money by giving budget up — and the plan says so with the utilisation figure attached, rather than implying a paper saving.

---

## 8 · Decide the existing account

**Confirmed 4 September 2026 — the audit fills the decision columns, not the account team.** The Final Bulk arrives with `Action`, `Reasoning`, `New Bids`, `New Budget` and `New Percentage` empty. It goes back **filled**, with the action written so it can be taken directly on the campaign without anyone re-deriving it from the plan document. A file returned with those columns still empty is the file that was handed over, and it is not a deliverable.

Preserve the original file exactly — every sheet, every column, in order. Fill `New Bids`, `New Budget`, `New Percentage`, `Action`, `Reasoning` and `Reverses If`.

- `Action` is short, imperative, and **directly executable**: "Raise bid $0.58 to $0.75", "Pause", "Set to +20%". Not "consider raising", not "review" — the person opening the file changes the campaign to what the cell says
- `Reasoning` carries the evidence with the number in it
- `Reverses If` names what would undo the decision, and when it is read
- Colour-code Action: green raise, amber cut, red pause

**A row is left blank only when the analysis genuinely reached no decision**, and every blank row is then classified in the No-Action Census with the mechanical reason no action is allowed — under the click line, parked by a gate, foreign SKU, and so on. Blank means "ruled out, here is why", never "not looked at".

Decide from 30-day data, not the 7-day window — a thin window produces too few winners to act on.

**Placement modifiers are set per campaign per placement from that campaign's own conversion data.** Never a blanket percentage in either direction — a blanket 0% is the same mistake as a blanket 135%, just cheaper. Top of Search is often the best placement on conversion and revenue per click while being worst on CPA, so the fix is usually to reduce the modifier, not remove it. See `references/placement-tiers.md`.

### The correction ladder — how hard, decided by ACoS

**A campaign with no orders and under 10–15 clicks is not judged at all. It waits.**

Once a campaign has delivered, how hard it is corrected is set by its **ACoS**, not by a flat rule. This is what "don't be aggressive on something that is working" means in practice: nothing happens to a lane at 6%, and a hard cut on a lane at 120% is not aggression, it is necessary.

| ACoS | Band | Action |
|---|---|---|
| **Under 30%** | Working | **No change.** Keep it running |
| **30 – 50%** | Slightly high | **A few cents** — the 5-cent walk, one step per cycle |
| **50 – 70%** | Moderate | **Cut 20%** |
| **70 – 100%** | Moderate-heavy | **Cut 30%** |
| **100% and above** | Unaffordable | **Cut 50%**, even on a single order. If still at or above 100% next cycle, **pause** |

**Read the placement before applying the band.** A high ACoS is a symptom, and on a delivering campaign the cause is often one placement rather than the bid. Pull that campaign's own placement report, read Top of Search, Rest of Search and Product Pages separately, and correct the modifier that is carrying the cost. Then re-read the campaign. If it is still in a cutting band, apply the ladder to the bid; often it is not. Cutting the bid first punishes every placement equally and loses the cheap orders along with the dear ones.

**Confirmed 4 September 2026.** The bands as first given left two stretches uncovered — 50–70% and 30–35%. They were filled to make the ladder contiguous, put back for confirmation, and confirmed. The ladder is now settled: every ACoS value falls in exactly one band, and no band is a matter of judgement at read time.

**The bands are absolute percentages**, the same on every product. They express appetite — how hard we are willing to correct — and they do not change from product to product.

### Two anchors gate the ladder, because absolute bands alone fail at both ends

**PROPOSED 4 September 2026, from the SLQS back-test — not yet confirmed.**

Every product has two ACoS numbers of its own, and they move enormously between products:

```
break-even ACoS = margin $ ÷ ASP                    where profit ends
ceiling ACoS    = forward-cash ceiling ÷ ASP        where forward cash ends
```

| Product | Break-even ACoS | Ceiling ACoS |
|---|---|---|
| Hanging Closet, white | 7.7% | 26.9% |
| Hanging Closet, black | 7.7% | 20.0% |
| Quilt Set | **33.7%** | **69.6%** |

The bands sit in completely different places on those two products, and applying them alone breaks at **both ends**:

| Case | Ladder alone says | Reality |
|---|---|---|
| Quilt Set campaign at **32%** | 30–50% band → cut 5 cents | **It is below break-even. It is profitable, and we would be cutting it** |
| Hanging Closet campaign at **28%** | Under 30% → no change | **It is above the 26.9% ceiling. We would be leaving an unaffordable lane alone** |

So compute both anchors per product, and let them gate the ladder:

| Where the campaign sits | What happens |
|---|---|
| **At or below its break-even ACoS** | **Never cut.** It is profitable. Whatever band it falls in, the ladder does not touch it |
| **Between break-even and the ceiling ACoS** | **The ladder applies exactly as written.** This is the subsidy zone in ACoS terms |
| **Above its ceiling ACoS** | **Always correct**, whatever the band and whatever the orders. The delivering protection is void here, the same way it is at 100% |

The bands still set **how much** comes off. The anchors decide **whether anything comes off at all**. Nothing about the confirmed band values changes.

**The anchors gate performance corrections only.** Found by running this rule on a live file, 4 September 2026. Two kinds of decision are not performance corrections and are not gated by break-even:

| Not a performance decision | Why it overrides |
|---|---|
| **Relevance** — the term describes a material, size or feature the product does not have | Already ruled. Negated on sight at any click count |
| **Incrementality** — the SKU holds little cover and clears without paid support | We would be paying for units that were going to sell anyway. Profitable is not the question; **incremental** is |

On one live file seven keywords converted at **12.7% to 32.6% ACoS** — all below that product's 33.7% break-even, all profitable, all correctly cut because their SKUs clear unaided. The break-even protection exists to stop a profitable lane being cut **for efficiency**. It was never meant to force us to keep paying for sales we would get for free.

**Say which it is in the reasoning.** A cut that reads as an efficiency call when it is really an incrementality call is the same row with the wrong argument, and the next cycle will reverse it for the wrong reason.

**ACoS at or above 100% overrides the delivering protection** in every case, ceiling or no ceiling. Orders do not shield a lane paying more for the sale than the sale is worth.

**State all three numbers together in the plan** — break-even ACoS, ceiling ACoS, and the campaign's own ACoS — so a reader can see which of the three zones each lane is in without re-deriving anything.

**The floors still bind.** No cut lands below $0.25, whatever the percentage says. Where the ladder would take a bid under the floor, it goes to the floor and stops there.

**Budget is untouched by the ladder.** It corrects the bid and clears the waste inside the campaign. Budget only moves when a campaign is paused outright — see the budget section above.

**State the walk.** Where a correction takes more than one cycle, say how many cycles and on what date it completes. A 5-cent step from $0.45 to $0.25 is four cycles, and the plan says so rather than implying it lands next week.

**The click line, and nothing tighter.** A zero-order row is not judged on performance until it reaches **15 clicks**, or **20–25 clicks where the click price is about $0.15 or under** — cheap clicks earn more patience. Below that a term has not had its chance, and pausing it removes the discovery surface that finds the cheapest orders. Reaching the line is a **review trigger**, not an automatic pause: look at the term itself before deciding. **A row with orders is never parked by any gate.**

Terms describing a material, size or feature the product does not have are negated on sight at any click count — that is a relevance decision, not a performance one.

**Every row that does not change is classified, not ignored.** Produce a No-Action Census: verdict class, row count, and the mechanical reason no action is allowed. A file where most rows are silent cannot be reviewed.

**Use the closed verdict vocabulary.** Verdicts come from the canon's list — CLEARANCE, HOLD, TRIM BUDGET, BID DOWN TO PROFITABLE CPC, STOP-LOSS, NEGATE, RE-POINT VARIATION, PAUSE, ROUTE-TO-BM, MANUAL, and the campaign-level set — never invented strings. A new string is a new concept, and a new concept goes to the canon before it goes in a file.

**One lever per row per cycle**, and argue why that lever and not the adjacent one. Where a ceiling breach genuinely requires both a budget and a bid move, that is one decision with two parts and it says so explicitly rather than arriving as two unexplained changes.

**Flag for human sign-off, never silently deploy:** an action on a 500+ SV keyword, any gate failure, any structural change, a bid move over 25%, a budget move over $50/day. The flag states the trade-off in the reviewer's own units — what is foregone in dollars per week against what is retained in orders and CPA — so it can be approved or declined from the flag itself.

---

## 9 · New campaigns, and writing it up

**Match type by evidence, not habit:**

| Match | Use for | Typical share |
|---|---|---|
| Broad | Terms above ~2,000 searches. Width. | ~20% of budget |
| Phrase | The default for anything unproven | ~40% |
| Exact | Only terms with demonstrated conversion, plus unambiguous intent like clearance | ~10% |

Exact-heavy builds are the most common failure. Check your own output: if most Exact keywords have no conversion evidence, move them to Phrase.

**Cover every surface, widely.** On a clearance product coverage is the lever — the plan is trying to find volume at a low price, and a narrow term set cannot. Build across:

- **Keywords** — every relevant term the master list carries, on Broad and Phrase, not a shortlist
- **Auto** — split into four isolated campaigns (close, loose, substitutes, complements)
- **Category targeting** — the categories this product genuinely sits in, with refinements where they narrow to the right shelf
- **Product targeting (PAT)** — competitor and complement ASINs
- **Sponsored Brands** — Product Collection across Broad, Phrase, Exact and ASIN targeting, not Phrase-only
- **Sponsored Display** — competitor, category, views, purchase, audiences

**Width comes from the target set; cost control comes from the bid.** Do not control cost by running fewer campaigns — that starves the lane and buys nothing. Control it by keeping every bid between the $0.25 floor and the ceiling.

**Which keywords go in which campaign, which ASIN serves each keyword, which competitor ASINs to conquest and how to refine a category: `references/keyword-and-target-selection.md`.** That file carries the intent-to-ASIN routing, the cannibalisation check, the search-volume tiers and the campaign-count arithmetic.

The seven build classes, the separation rules and the added-tab structure: `references/objective-and-builds.md`.

**No bid above the ceiling**, where the maximum click price is `ceiling × conversion rate`. Bidding strategy fixed or down-only only — up-and-down can breach the ceiling at auction. Placement multipliers per §8, never blanket.

**Isolation rule:** any term promoted from discovery into capture is added as negative exact to the campaign that found it, the same day. One keyword lives in one campaign **per ad product** — an SP and an SB instance of the same term is coverage, not self-competition.

**Relevance gate:** strip terms describing a material, feature or size the product does not have. Buying traffic that expects something we do not offer converts and then returns.

**Route SKUs by cover and refund tier.** Every campaign carries only the SKUs it should serve.

**Gate what depends on something else.** Group into tranches — live now, gated on brand registry, gated on a reprice, gated on a quality fix — with the gate named on the campaign row.

### Writing it up

Section order, workbook tab list, validation gate and how to publish: `references/output-format.md`.

Basis tag every prediction: **HIST** measured on this product, **MARKET** inferred from category or a named competitor, **TEST** no product-specific observation.

Two sections people forget and shouldn't:

**Where this audit is incomplete** — every gap, why it matters, what would close it, who owns collecting it. It is what makes the rest credible.

**Lessons from our own performance** — what we did, what happened, what it tells us. Pull from the Slack thread.

**Grading is a calendar, not day counts.** Deal windows and the 14 days after them are excluded from trend verdicts, so state actual dates. If a change will make a metric worse before better, say so in the gate — otherwise someone reverses a correct decision.

---

## Standing rules

- An action that is not logged did not happen
- A lever below half its prediction at the read is replaced, not deepened
- Grade on total units and cost per unit shipped, never ad-attributed orders alone
- When two sources disagree, name the governing one and say why
- Tell the user when a number is wrong or unverifiable rather than working around it
- Re-derive rather than defend when a figure is challenged
- The decisions this audit does not make — floor price, salvage value, archetype, risk tier, terminal option, discount and deal depth — are routed out with the evidence attached, never worked around with a bid

## Scale honesty

A fully argued case for every row cannot be produced reliably across hundreds of rows at once. Produce it in batches, highest-spend first, and say which rows got that depth. Producing it at full scale anyway generates text that reads complete and is not; the failure mode is not an obviously thin answer, it is a confidently thorough-looking one.

## References

- `references/data-traps.md` — the contradictions that recur, and how to check for them
- `references/leak-audit.md` — the ten lever groups, how to price each, the ranked table
- `references/refund-gate.md` — tiering SKUs by refund risk before routing spend
- `references/ceiling-and-attribution.md` — ceiling construction, the acceleration cap, per-unit-cleared, per-campaign blends, product-ad attribution
- `references/placement-tiers.md` — setting modifiers per campaign per placement
- `references/objective-and-builds.md` — what the clearance objective permits, the seven build classes, the added tabs
- `references/prior-cycle-grading.md` — step 0. Execution verification, grade definitions, the refund lag, what grading changes
- `references/keyword-and-target-selection.md` — keyword intent to ASIN routing, cannibalisation, volume tiers, PAT and category selection
- `references/output-format.md` — document spine, workbook tabs, validation gate, publishing
