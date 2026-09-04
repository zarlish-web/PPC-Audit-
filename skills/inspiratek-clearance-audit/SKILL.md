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

**Where this skill and the locked canon disagree, the canon wins and the disagreement is reported, never silently resolved.** One such disagreement is live and material — see §5.

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

Two canon rules that decide most clearance products before any campaign is opened:

- **Under negative CM the LTSF answer is pricing, not bids.** Route to Brand Management. An aged SKU whose contribution does not survive the surcharge cannot be advertised into profit at any bid, and a bid book built for it is wasted work.
- **Gate the push on stock.** GREEN (overstock, room to clear) → aggressive up to break-even. Not GREEN (already low) → **do not push**; it clears naturally, and the LTSF is flagged in the Suggestion rather than funded. Never run a clearance push on a SKU whose hero size is RED — clear the aged variation, protect the hero.

## Do this in order

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

Optional but valuable: parent-level SQP with cart-adds, ASIN Insights, competitor price history, removal order detail, per-SKU floor prices, the prior cycle's prediction register.

**Build the verification table before any analysis.** Every figure that later carries weight needs a named governing source. See `references/data-traps.md` for the contradictions that recur — read it before trusting any number.

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

**What the re-tag makes illegal.** Every one of these is barred on a re-tagged campaign, and a plan carrying one has not re-tagged:

- Rank targets, rank movement as a success measure, and the seven-state ranking progress test — there is no rank objective to progress toward
- The top-of-search modifier ladder used to buy position
- DSTR and target-clicks sizing derived from a rank goal
- Any bid above the ceiling justified as a sized, capped ranking push
- Exact-match expansion on unproven terms

**What it makes the governing measures.** Velocity, months to clear, cost per unit cleared against the ceiling, and the charge avoided — judged on total units shipped, never on ad-attributed orders alone.

**Where a re-tagged campaign was mid-push**, say so and state what is being abandoned. A rank programme stopped halfway is a real cost and the document owns it rather than letting it disappear in a re-tag.

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

## 5 · The ceiling

**Start from the canon, not from this skill.** Compute and state first:

```
break-even ACoS  = (ASP − COGS − Amazon bundled fees) ÷ ASP     no return allowance
margin $         = ASP − COGS − Amazon bundled fees
max profitable CPC = margin $ × CVR at the delivering placement
clicks-to-loss   = margin $ ÷ CPC
CPA              = CPC ÷ CVR
```

Then apply the surcharge **the way the canon applies it**: *the surcharge is a margin drag, so the SKU's effective break-even is worse.* Recompute break-even net of the drag, and check the sign:

```
CM after carry = margin $ − (storage per unit per month × months held to sale)
```

**If CM after carry is negative, stop.** The verdict is ROUTE TO BM — the lever is price, not bids — and no campaign work is authorised. This is the most common outcome on genuinely aged stock and it is a finding, not a failure.

If CM after carry is positive, the clearance objective runs at **break-even ACoS: sell the aged stock out up to break-even, no further**, ring-fenced, labeled, and tagged separately in TACoS, under the objective's own cap.

**Exit clearance when stock clears below the surcharge threshold**, and say on the face of the plan what that threshold is.

### The disagreement to report, not resolve

This skill's inherited construction adds avoided storage *to* the ceiling:

```
ceiling = contribution + (storage per unit per month × min(2, months to clear))
```

That is a forward-cash argument — selling now avoids charge later — and it moves the ceiling **up**. The canon treats the same surcharge as a margin drag and moves break-even **down**. On the same product the two produce opposite recommendations, and the gap is large: on one live product the forward-cash ceiling read $19.97 per unit where the canon's max profitable CPC read 6.7 cents.

**Do not pick one silently.** Compute both, show both, name which one the plan acted on, and file the choice as a decision requested. Under the canon's own rule the forward-cash figure is only available as one of the three labeled investment objectives, and then **only while capped, dated and logged** — never as an open-ended raise.

### Rules that hold under either construction

**COGS never enters a live decision column on aged stock.** It is identical across every option for the same units, so it cannot change which option wins.

**The ceiling test is cost per unit *cleared*, built from cost per unit *shipped*.** Not cost per ad-attributed order — advertising may attribute only a fraction of units, and the two denominators produce very different numbers. CPA per order is for keyword-level decisions only.

**Where a campaign ships more than one child, its ceiling is weighted by the children it actually ships**, not by its name and not by the lower child by default.

**Deal-state and clean-state are computed separately, never blended.** A window containing a deal is read twice — once from deal-state data, once from clean-state — and neither substitutes for the other. Clean-state governs ordinary decisions.

**Every anchor is stale past 45 days, or after any price, fee, packaging or LTSF change.** A verdict resting on a stale anchor is provisional and says so.

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
| **UNMEASURED** | Converter evidence below the sufficiency line, so no conversion rate can be read | Reach layer at floor bids to accumulate clicks, with a dated read |

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

**Released budget is not automatically redeployed.** Before recommending a reallocation, check that some lane inside its ceiling is actually budget-capped. Where every lane that clears runs far below its budget and every lane with reach sits above ceiling, the money has nowhere to go — release it and say so. Utilisation measures whether a lane *can* spend, never whether it *should*.

---

## 8 · Decide the existing account

Preserve the original file exactly — every sheet, every column, in order. Fill `New Bids`, `New Budget`, `New Percentage`, `Action`, `Reasoning` and `Reverses If`.

- `Action` is short and imperative: "Raise bid $0.58 to $0.75", "Pause", "Set to +20%"
- `Reasoning` carries the evidence with the number in it
- `Reverses If` names what would undo the decision, and when it is read
- Colour-code Action: green raise, amber cut, red pause

Decide from 30-day data, not the 7-day window — a thin window produces too few winners to act on.

**Placement modifiers are set per campaign per placement from that campaign's own conversion data.** Never a blanket percentage in either direction — a blanket 0% is the same mistake as a blanket 135%, just cheaper. Top of Search is often the best placement on conversion and revenue per click while being worst on CPA, so the fix is usually to reduce the modifier, not remove it. See `references/placement-tiers.md`.

**Two thresholds, and they are not the same threshold.** The canon's sample gate parks a **zero-order row under 15 clicks** — hold and wait, and say whether low clicks are consistent with low search volume. The negation line is separate and further out: at conversion rate *c*, one order is not expected until roughly `1/c` clicks, so a term below that showing zero orders is not evidence of failure and negating it removes discovery surface. Both are stated, and neither is used in place of the other. **A row with orders is never parked by either gate.**

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

**Cover every surface.** SP, SB (Product Collection across Broad, Phrase, Exact and ASIN targeting — not Phrase-only), SD (competitor, category, views, purchase, audiences), Auto split into four isolated campaigns. The six build classes, the separation rules and the added-tab structure: `references/objective-and-builds.md`.

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
- `references/objective-and-builds.md` — what the clearance objective permits, the six build classes, the added tabs
- `references/output-format.md` — document spine, workbook tabs, validation gate, publishing
