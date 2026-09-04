# The ceiling, and what spend belongs to this product

Steps 1.1 and 5. Two subjects in one file because the ceiling is only as good as the spend figure tested against it.

---

## Part 1 — Attribution

### Attribute through product-ad rows

A bulk export is account-wide. A campaign that carries this product's ad may carry hundreds of other SKUs, and catch-all, brand-defence and portfolio-level campaigns routinely carry every SKU in the account.

Three ways to scope, and only one is right:

| Method | What it gives | Verdict |
|---|---|---|
| Portfolio filter | Misses children advertised from outside the portfolio | Understates |
| Campaigns containing this product's ad | Pulls in every other SKU in those campaigns | Overstates, sometimes by multiples |
| **Product ad rows for this product's SKUs** | This product's spend, clicks, sales and units | **Correct** |

Then reconcile: the attributed total should land within a percent or two of an independent source such as Sellerboard. Where it does, the scope correction is settled and can be stated as settled. Where it does not, it is a named gap.

### Which campaigns enter the decided bulk

A campaign whose product ads are entirely this product's SKUs is in scope. A campaign carrying any foreign SKU is **excluded and named as excluded**, with its SKU count and this product's share of its spend. It is not this product's campaign to decide, and editing it changes other products.

### Conversion rate is per child, from attributed rows

`CVR = units attributed to that child ÷ clicks attributed to that child`, both from product-ad rows. A blended account CVR applied to a child with different economics is how a wrong maximum click price gets into a bulk.

---

## Part 2 — The ceiling

### Construction

```
contribution = ASP − referral − FBA − refund cost per unit shipped
ceiling      = contribution + (storage per unit per month × months of acceleration)

months of acceleration = min(2, months to clear at realised velocity)

maximum click price = ceiling × conversion rate
```

Where the units are aged but not terminal and the product still sells at margin, the ceiling comes instead from contribution above the declared floor price, and the guard is that realised net price stays above that floor at every step.

### The rules that govern it

**COGS is sunk and appears in no term.** It is identical across every option for the same units, so it cannot change which option wins. Showing it makes every option on an underwater product look like a loss, which produces paralysis rather than a decision.

**The acceleration window is capped at two months.** The default exists because the whole projected hold inflates the ceiling most on exactly the stock least able to justify it: a slow variant has the longest runway and the weakest case for spending against it. And it is capped again at the real clearance time — a variant that clears in 1.5 months cannot avoid two months of charge.

**Count the charge once.** It sits either inside the fees line reducing contribution, or added back as avoided charge — never both. Check the fees line against the modelled fee: a gap of roughly the per-unit surcharge means the charge is already inside it.

**Do not assume the sign of the declared subtrahend.** Both signs occur in live data. State the value read and which direction it moved the ceiling.

**Months-to-clear is computed, never read.** Derive it from charge-bearing units at realised velocity. Do not take it from a supplied cover, days-on-hand or months-on-hand column — those are derived, frequently stale, and the ceiling is a direct function of this number.

**The ceiling is stale the moment any input moves** — price, storage rate, unit count, velocity, conversion rate. A ceiling dated earlier than its inputs is recomputed before anything is staged against it. Where a price or depth change lands inside the trailing stability window, conversion reads are provisional and the ceiling holds at its last dated value.

### The test is per unit cleared

```
ad cost per unit shipped  = attributed spend ÷ TOTAL units shipped   (not ad-attributed units)
ad cost per unit cleared  = ad cost per unit shipped ÷ (1 − refund rate)
```

Both denominators matter and they are not interchangeable:

| Measure | Denominator | Use for |
|---|---|---|
| Cost per ad-attributed order | Orders advertising claims | Keyword and target decisions |
| Cost per unit shipped | Every unit that left | **The ceiling test** |
| Cost per unit cleared | Units that left and stayed gone | **The ceiling test on a product with refunds** |

Where advertising attributes three quarters of units the first two differ by a third; where it attributes a quarter they differ by four times. A verdict computed on one and tested against the other is not a verdict.

### Per-campaign ceilings

A campaign that ships more than one child does not take the lower child's ceiling by default, and never its name's implied child. Weight by the units it actually shipped:

```
campaign ceiling = Σ(units_child × ceiling_child) ÷ Σ(units_child)
```

Where a campaign shipped nothing, fall back to the route implied by its product ads, and only then to its name — and mark which fallback was used.

### Bringing a lane back to its ceiling

For a delivering campaign above its ceiling, scale the budget by exactly the factor it is over:

```
new budget = observed daily spend × (ceiling ÷ cost per unit cleared)
```

This is arithmetic rather than judgement, it is checkable from the file, and it does not round to a convenient number. Bids in the same campaign are cut to `ceiling × CVR` in the same pass — a budget cut without a bid cut just spends the same money faster.

### Worked shape

| | Child A | Child B |
|---|---|---|
| Contribution before storage | $3.07 | $3.07 |
| Storage per unit per month | $3.84 | $3.28 |
| Months to clear | 4.4 | 1.5 |
| Acceleration months, `min(2, mtc)` | **2.0** | **1.5** |
| **Ceiling** | **$10.75** | **$7.99** |
| Conversion rate | 2.18% | 2.95% |
| **Maximum click price** | **$0.23** | **$0.24** |
| Ad cost per unit shipped | $11.35 | $13.38 |
| Refund rate | 26.1% | 19.4% |
| **Ad cost per unit cleared** | **$15.36** | **$16.60** |
| Position | 1.43x over | 2.08x over |

Note what the capped window does to Child A: taken at 4.4 months its ceiling reads $19.97 and the child looks comfortably inside. Capped at two months it reads $10.75 and the same child is 43% over. The cap is not conservatism for its own sake — it is the difference between two opposite recommendations.
