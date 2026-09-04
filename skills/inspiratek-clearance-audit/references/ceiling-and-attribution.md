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

### Two constructions, and they disagree

**Construction A — the canon (`pmp-optimization-sr` §3, §8.3).** The surcharge is a margin drag; it makes break-even *worse*.

```
break-even ACoS    = (ASP − COGS − Amazon bundled fees) ÷ ASP    no return allowance
margin $           = ASP − COGS − Amazon bundled fees
max profitable CPC = margin $ × CVR at the delivering placement
CM after carry     = margin $ − (storage per unit per month × months held to sale)
```

`CM after carry` negative → **ROUTE TO BM.** The lever is price. No bid work is authorised.
`CM after carry` positive → clearance objective, **up to break-even ACoS and no further**, ring-fenced, labeled, tagged separately in TACoS, and exited when stock clears below the surcharge threshold.

**Construction B — forward cash (this skill's inherited rule).** Selling now avoids charge later, so the charge is added *to* the ceiling.

```
contribution = ASP − referral − FBA − refund cost per unit shipped
ceiling      = contribution + (storage per unit per month × min(2, months to clear))
max click price = ceiling × conversion rate
```

**They point opposite ways on the same product, and the gap is not small.** On one live child: Construction A gives a max profitable CPC of **$0.067**; Construction B gives a ceiling of $10.75 and a max click price of **$0.23** — and taken at months-to-clear rather than the two-month cap, $19.97 and $0.44. A plan built on A stops; a plan built on B funds a reach layer.

**Compute both. Show both. Name the one the plan acted on. File the choice as a decision requested.** Under the canon, Construction B is only available as one of the three labeled investment objectives, and then only while **capped, dated and logged**.

Where the units are aged but not terminal and the product still sells at margin, the ceiling comes instead from contribution above the declared floor price, and the guard is that realised net price stays above that floor at every step.

### The rules that govern it

**COGS is sunk and appears in no term.** It is identical across every option for the same units, so it cannot change which option wins. Showing it makes every option on an underwater product look like a loss, which produces paralysis rather than a decision.

**Under Construction B, the acceleration window is capped at two months.** The default exists because the whole projected hold inflates the ceiling most on exactly the stock least able to justify it: a slow variant has the longest runway and the weakest case for spending against it. And it is capped again at the real clearance time — a variant that clears in 1.5 months cannot avoid two months of charge.

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

**Two levers, and neither is the budget.**

**1 · Walk the bid down.** 5 cents per cycle, every cycle, until it reaches the ceiling.

```
new bid = max(current bid − 0.05, ceiling × CVR, 0.25 floor)
cycles to arrive = ceil((current bid − target) ÷ 0.05)
```

State the cycle count and the completion date. A bid at $0.45 walking to $0.25 is four cycles, and the plan says so rather than implying it lands next week. The same 5-cent limit applies upward.

**2 · Remove the waste inside it.** Pause or negate the specific targets that have passed the click line with no orders. That is where the money is actually leaking, and removing it lowers the campaign's cost per unit without lowering its reach.

**The budget is not a lever here.** Cutting it reduces the units the lane clears, which is the opposite of the objective, and where the lane is not spending its cap the cut saves nothing at all. Budget comes down only when the campaign is paused outright, or when a lane genuinely at its cap is asked to fund a better one.

### The click line for waste

Per keyword or per target, never per campaign:

| Click price | Clicks with zero orders before review |
|---|---|
| About $0.15 or under | **20–25** — cheap clicks earn more patience |
| Ordinary | **15** |

At the line, review the term on its merits — relevance, search volume, whether it describes this product — then pause, negate, or grant another window. It is a trigger for judgement, not an automatic kill. Below the line nothing is touched on performance grounds.

Terms describing a material, size or feature the product does not have are negated on sight, at any click count, because that is a relevance decision rather than a performance one.

### Worked shape

| | Child A | Child B |
|---|---|---|
| Contribution before storage | $3.07 | $3.07 |
| Storage per unit per month | $3.84 | $3.28 |
| Months to clear | 4.4 | 1.5 |
| Acceleration months, `min(2, mtc)` | **2.0** | **1.5** |
| **Ceiling** | **$10.75** | **$7.99** |
| Conversion rate | 2.18% | 2.95% |
| **B — maximum click price** | **$0.23** | **$0.24** |
| A — break-even ACoS | 7.68% | 7.68% |
| A — margin $ | $3.07 | $3.07 |
| **A — max profitable CPC** | **$0.067** | **$0.091** |
| A — CM after carry | **−$13.83** | **−$1.85** |
| **A — verdict** | **ROUTE TO BM** | **ROUTE TO BM** |
| Ad cost per unit shipped | $11.35 | $13.38 |
| Refund rate | 26.1% | 19.4% |
| **Ad cost per unit cleared** | **$15.36** | **$16.60** |
| Position | 1.43x over | 2.08x over |

Both children carry negative CM after the surcharge, so under the canon this product does not get a bid plan at all — the verdict is ROUTE TO BM and the lever is price. Construction B, on the same inputs, funds a reach layer at 23–24 cents. That is the whole disagreement in one table, and it is why both rows belong in every document.

Note what the capped window does to Child A under Construction B: taken at 4.4 months its ceiling reads $19.97 and the child looks comfortably inside. Capped at two months it reads $10.75 and the same child is 43% over. The cap is not conservatism for its own sake — it is the difference between two opposite recommendations.
