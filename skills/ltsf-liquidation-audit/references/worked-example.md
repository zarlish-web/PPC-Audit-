# Worked example

A real run, with its numbers, including the places it went wrong. Read when a step is ambiguous.

Values are from one live product's cycle and are illustrative of method, not of any other product's economics.

---

## The product

A quilt-set parent, 21 child SKUs, carrying the largest single share of the portfolio's monthly aged-inventory charge. Objective: clear aged stock. No ranking objective. Units crossing a bracket boundary within weeks.

---

## Step 2 — what the corrections found

The audit's own conclusions changed once the corrections ran. Two of them:

**Landed cost was higher than the plan of record assumed.** The profit tool held unit cost only — the domestic shipping field was null on every child. The uplift in the charge file was freight and duty. Any ceiling built on the profit tool's cost alone would have been too generous.

**The charge was confirmed by two independent sources.** The inventory report and the deal tracker's own sheet agreed. That is what a *check that settles it* looks like: a correction is not settled by restating it more confidently, it is settled by a second source agreeing.

**What the corrections did not catch, and should have** — see §6.

---

## Step 3 — the ceiling, built line by line

```
realised average selling price                        $40.91   week stated
  − referral                                          −$6.14
  − fulfilment                                       −$12.50   driven by cube, not weight
  − refund cost at the current rate                   −$8.51   26% rate, sellable quota stated
  = contribution before advertising                  +$13.77
  + storage avoided by selling two months early      +$14.70   $7.35/unit/month × 2
  = CEILING ADOPTED                                   $28.47

  current ad cost per unit shipped                    $17.88   30-day basis
  headroom                                            $10.59
```

Three things to take from this:

**The acceleration window is bounded and stated.** Two months, not the full projected runway. Note what happens otherwise: the runway on this product was several months, so counting all of it would have roughly doubled the ceiling — on stock whose slow movement was the reason it aged. The bound is what stops the ceiling being most generous exactly where it should be least.

**Refund cost is inside the ceiling.** At a 26% return rate this is the third-largest line. A ceiling built on contribution before refunds would overstate by more than half the headroom.

**The ceiling counts the avoided charge**, which is what makes it larger than a margin-only allowance would be. A margin-only calculation gave roughly half this figure and omitted the largest avoidable cost on the product.

---

## Step 5 — where the framework and the file disagreed

This product carried the **largest charge in the portfolio** and, at its realised velocity, aged units that would take **hundreds of months to clear**.

A rule that scales intensity by charge alone would have directed the largest build in the portfolio at the least clearable stock in it. That is the inversion §5.2 of the decision framework exists to prevent, and this product is where it was found.

The correct reading: the size of the charge is the reason to close the lane faster and route to the terminal option, not the reason to spend into it. The portfolio's own file had already routed most of this stock to liquidation or removal.

**The check to run:** months to clear at current velocity, against days remaining. Where the first exceeds the second by a wide margin, no bid, budget or coverage change closes that gap.

---

## Step 6 and 7 — what the build got right

**Bidding strategy.** Every new campaign staged on a downward-only or fixed strategy. Not one on a strategy that can raise a bid at auction. This is the control that fails silently when it fails, and the file did not fail it.

**Separation held.** Zero within-ad-product keyword overlap across the new builds — several hundred keyword-and-match pairs in Sponsored Products, several dozen in Sponsored Brands, no duplicates inside either. Cross-product repetition was present and is correct.

**Every changed row carried a reasoning.** Over two thousand decided rows, none with an action and no reasoning.

**The match-type diagnosis argued for the reach layer independently.** The account was two-thirds exact in a category where phrase and broad converted cheapest — phrase winners at a fraction of the exact click price. That is the reach-layer case made from the product's own data rather than from doctrine.

---

## Step 16 — the spend curve, and an honest choice

Six spend levels, each with degraded click price and conversion:

| Spend/day | Units/day | Months to clear | Storage saved | Extra ad cost | Net benefit |
|---|---|---|---|---|---|
| lowest | 19.9 | 4.2 | $24,122 | — | **$24,122** |
| mid | 39.0 | 2.2 | $43,143 | $22,860 | $20,283 |
| highest | 73.7 | 1.1 | $52,529 | $39,374 | $13,156 |

**Net benefit peaks at the lowest spend and erodes upward**, because each extra dollar of advertising saves less storage than the last.

The plan recommended the middle level anyway, and said why: it clears the pool in roughly half the time, removing a bracket crossing that the net-benefit figure does not price.

That is the model for W3 and for §16 of the output format. The curve is shown, the peak is named, and the departure from it is stated as a choice with a reason — not hidden by only showing the recommended level.

---

## §6 — Where this run went wrong

Both failures are traceability, both were quiet, and both are why the validation gate exists.

**The companion workbook reference was stale.** The audit named a version two revisions behind what shipped, with a row count that did not match. Anyone later asking why a bid was set would have opened the wrong file.

**The lead decision asked for the wrong number.** Decision 1 asked for authorisation of a daily budget the plan had explicitly abandoned two sections earlier as too conservative — the build totalled roughly 40% more, and the recommendation section said so.

An executive reading only the decisions table would have approved a figure the plan was not built on. Neither error touched the analysis, which was sound. Both would have been caught by validation-gate checks 1 to 6, which take a few minutes and are the cheapest checks in the run.

**The general lesson:** the analysis is usually not where these documents fail. They fail at the joins — between the audit and its workbook, and between the body and the summary an approver actually reads.
