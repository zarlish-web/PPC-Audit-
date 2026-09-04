# Decision framework

Steps 1–5 of the run. Read alongside `prompts.md`.

**This file carries no thresholds.** Every band, gate line and cadence is named by its source and read at run time. A number written into this file would become a second place for a value to go stale, and the first place would win.

## Contents

1. Inputs and what each decides
2. Context corrections
3. The ceiling
4. The required pace
5. The clearability gate
6. Archetype boundaries
7. The test boundary
8. What is never decided here

---

## 1. Inputs and what each decides

| Input | Source | What it decides |
|---|---|---|
| The seven declared fields | LTSF row | Whether the run may start at all |
| Archetype | Declaration | The boundaries at §6 |
| Risk tier | Declaration | Cadence and posture |
| Floor price, salvage value, terminal option | Declaration | The ceiling |
| Remaining units by bracket, cliff date | Cliff calendar | The pace |
| Contribution at price and at floor | Declaration with Finance | The ceiling on aged-healthy stock |
| Monthly charge per product | Charge file | The intensity band |
| Realised velocity per SKU | Charge file or profit export | The clearability read |
| Converter conversion rate | Performance data, subject to the sufficiency gate | The ceiling and the required-clicks figure |
| Market click price at the required volume | Placement data and current suggested bids | Whether the lane opens |
| Keyword set with syntax, relevancy, volume, suggested bid | Master keyword list | Tier assignment |
| Variation map naming the aged children | Variation map | Archetype B scope |
| Live campaign and keyword inventory | Bulk export | The separation check |

A missing input suppresses its dependent step and is recorded. It never licenses an estimate, a smaller version of the action, or a value carried from a prior cycle without its date.

---

## 2. Context corrections

Corrections come **before** verdicts, because a correction that arrives after the section it would have reversed does not reverse anything.

The purpose is not caution. It is that on this class of product the raw numbers are usually measured on the wrong thing, and an audit built on them is confidently wrong rather than obviously wrong — which is harder to catch and more expensive.

### 2.1 Scope

Campaigns outside the product's portfolio frequently advertise its children — brand-defence campaigns especially. Portfolio-scoped spend misses them.

Compute spend both ways. Where an independent source reports total advertising cost for the same window, reconcile against it and state the match to the cent. A scope correction that reconciles is settled; one that does not is a named gap.

### 2.2 Entity

Reading keyword rows alone captures only part of spend, because automatic targeting, product targeting and placement adjustments sit elsewhere. The cost per order computed on keyword rows can differ substantially from the real one.

State what share each level captures and the figure each produces.

### 2.3 Window

A deal window or a price change inside a comparison period makes week-on-week reads meaningless. Name the dates, say which comparisons are void, and identify the one window that is readable.

Where a discount sits inside the period, note that it cuts contribution close to its full depth, because cost of goods and the non-referral fees do not fall with price.

### 2.4 Term

Rank and performance stories differ completely depending on which term is being described — a head term declining while the terms actually carrying the spend recover, for instance.

State each reading separately. Averaging is what hides a divergence.

### 2.5 Provenance

Which child was actually enabled over the window the performance history spans, and does each campaign advertise the child its name implies?

Performance history attributed to the wrong child is worse than no history, because it is trusted.

---

## 3. The ceiling

The maximum a click may cost. Computed, never chosen, and recomputed whenever any input moves.

### 3.1 Construction

```
realised average selling price          window stated
  − referral fee
  − fulfilment fee
  − refund cost at the current rate
  = contribution before advertising
  + the avoided charge over a bounded acceleration window
  = CEILING ADOPTED  (allowable ad cost per unit)

maximum click price = ceiling adopted × converter conversion rate
headroom            = ceiling adopted − current ad cost per unit shipped
```

Where the units are aged but not terminal and the product still sells at margin, the ceiling comes instead from contribution above the floor price, and the guard is that realised net price stays above the declared floor at every step.

### 3.2 The rules that govern it

**The avoided charge is bounded.** Count it over a stated acceleration window, not the whole projected hold. The full runway inflates the ceiling most on the stock least able to justify it — slow-moving stock has the longest projected hold and the weakest case for spending against it.

**Sunk cost of goods appears in no term.** It is identical across every option for the same units, so it can never change which option wins. Showing it makes every option on an underwater product look like a loss, which produces paralysis rather than a decision.

**Do not assume the sign of the declared subtrahend.** Both signs occur in live data. State the value read and which direction it moved the ceiling.

**The ceiling is stale the moment any input moves** — floor price, salvage value, unit count, cliff date, conversion rate. A ceiling dated earlier than its inputs is recomputed before anything is staged against it.

**Where a price or depth change lands inside the trailing stability window**, conversion reads are provisional. The ceiling holds at its last dated value and is not recomputed on a provisional rate.

### 3.3 Track it per unit, not only per click

The click price is what gets staged, but the ceiling's real test is **ad cost per unit shipped against the ceiling adopted**. A lane can sit under its click ceiling and still exceed the per-unit ceiling if conversion falls. Report both.

---

## 4. The required pace

```
required units per day  = remaining units ÷ days to the declared cliff date
required clicks per day = required units per day ÷ converter conversion rate
required daily budget   = required clicks per day × market CPC at that volume
```

**Read market click price at the volume the lane needs.** The price that clears a small number of clicks a day is not the price that clears a large one, and reading the current figure understates the cost of the pace — often by enough to flip the gate result.

Re-derive whenever remaining units, the cliff date or the conversion rate moves. A pace figure carried against a unit count that has fallen overstates the requirement; carried against a cliff date that has moved, it understates it.

---

## 5. The clearability gate

### 5.1 The three outcomes

| Result | Meaning | What follows |
|---|---|---|
| **OPEN** | Market click price at the required volume is at or under the ceiling | Fund the full required-clicks budget |
| **SPLIT** | Only a residual click volume clears at or under the ceiling | Buy what the ceiling buys; state the residual and route it |
| **CLOSED** | No click volume clears at or under the ceiling | Build nothing. Hand back the five numbers |

**A closed lane is a correct outcome.** It routes the choice to a price move or the terminal option, both of which recover more than spending above the ceiling would. Closing on arithmetic is the finding the deciding system needs.

The response to a closure is never to widen the term set.

### 5.2 Charge never overrides the gate

Charge measures what stock costs to hold. It says nothing about whether traffic can move it, and the two are frequently inverted: the largest charge in a portfolio is often the least clearable stock in it, because low velocity is what aged it in the first place.

```
months to clear at current velocity = aged units ÷ realised units per month
```

Read against the days remaining. Where the figure exceeds the runway by a wide margin, the arithmetic has already answered the question and the traffic check confirms it rather than rescuing it. No bid, budget or coverage change closes a gap of that shape.

**Clearability decides whether to build. Charge decides only how much.**

### 5.3 The unmeasured lane

Where converter evidence sits below the sufficiency line, the conversion rate is unreadable, so the ceiling and the required-clicks figure are both unavailable. The lane is neither open nor closed — it is **unmeasured**.

This is a real state and it needs naming, because the alternative is a run that stalls silently while the charge accrues.

The resolution is the reach layer at floor bids, run to accumulate clicks to the sufficiency line. That is legal under the test boundary at §7 because it buys sales rather than position, and it costs a small fraction of the accruing charge.

Record it as unmeasured **with a dated read**. A lane is never left in this state undated.

---

## 6. Archetype boundaries

The structure of the build is the same for all four. The archetype sets what may be touched.

| Archetype | Boundary |
|---|---|
| **Fixable demand** | Reach traffic only. A conversion defect is not fixed by buying more clicks — listing repair runs in parallel and PPC neither waits for it nor substitutes for it. Scaling a defect multiplies the defect |
| **Variation overstock** | Only the aged children enter any campaign. The parent and the healthy children are excluded from every SKU list and every group. No family-wide budget move, no shared coupon, no parent re-point. The healthy children subsidise the fix; their economics and price anchors are not spent on it |
| **Structurally dead** | The reach layer runs. No ranking spend of any kind, at any charge level, ever. The decision window is short enough that a test whose read arrives after the decision is pure charge |
| **Aged healthy** | The product still sells at margin, so budget headroom is larger at the same charge band. No retag and no quarantine — the reach campaigns sit alongside the standing structure rather than replacing it |

---

## 7. The test boundary

Ranking spend is barred on tagged units, and experiments are barred where the read window exceeds the decision window. Those rules stand. This states what they reach, because the reach layer is a form of testing and was being caught by wording aimed at something else.

> **Allowed — a reach test.** Buys sales at bids at or under the ceiling. Bid tiers, new match types, new attribute groups, a new surface. Costs little; a null result is cheap.
>
> **Barred — a ranking test.** Buys position. Any bid above the ceiling, any top-of-search premium, any funded push, any rank objective.

**The dividing line is checkable from the bulk file: does the bid sit above the ceiling?** Above it, barred. At or under it, allowed.

This is consistent with the rule excluding experiments on structurally dead stock, which targets tests that spend real money to buy *information* inside a decision window too short to use it. A reach test buys sales, not information.

---

## 8. What is never decided here

Route these out with the evidence attached:

- Archetype, risk tier, tier movement
- Floor price, salvage value, the salvage comparison
- Discount, coupon and deal depth
- Every terminal option and its execution
- Any number that neither the criteria authority nor the declaration carries — name what the decision needs, state that neither answers it, and file it

An operator who computes a floor price, a salvage value or an archetype has made the error this framework exists to prevent. The competence being installed is the refusal.
