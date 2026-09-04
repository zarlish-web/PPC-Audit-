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

### Three numbers, and the bid sits between them

**Forward cash governs — that is ruled. Break-even is the reference you must know before deciding anything.** One says what you may spend; the other says where profit actually ended. Compute both, every time.

```
break-even ACoS    = (ASP - COGS - Amazon bundled fees) / ASP     no return allowance
margin $           = ASP - COGS - Amazon bundled fees
max profitable CPC = margin $ x CVR                          <- where profit ends
avoided charge     = storage per unit per month x min(2, months to clear)
ceiling            = contribution + avoided charge
max click price    = ceiling x CVR                           <- where forward cash ends, the hard cap
floor bid          = $0.25 default                           <- below this nothing wins
```

**Between max profitable CPC and max click price is the subsidy zone.** Spending there is deliberate: the sale loses money and the avoided charge pays for it. **Bid low in the zone** — the cap is a maximum, never a target.

### Pricing the subsidy

```
subsidy per click = bid - max profitable CPC
subsidy per unit  = subsidy per click / CVR
```

**Test: subsidy per unit at or under the charge avoided per unit.** Under it, the forward-cash argument holds and the plan says so with both numbers. Over it, we are paying more to avoid the charge than the charge costs — that is loss, not forward cash, and the gap is logged in dollars and routed to the pricing recommendation.

Same boundary as the ceiling, expressed per unit so a reader sees what the ceiling means without re-deriving it.

### When the floor sits above the ceiling

Not an error. Live example: both children's whole workable band sat below the $0.25 minimum bid, so the floor governed and each unit carried $0.48-$0.72 of loss beyond what the avoided charge justified. That is a finding about how marginal the clearance case is, and it belongs beside the pricing recommendation.

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

Real numbers from one live product, both children:

| | Child A | Child B |
|---|---|---|
| Contribution before storage | $3.07 | $3.07 |
| Storage per unit per month | $3.84 | $3.28 |
| Months to clear | 4.4 | 1.5 |
| Acceleration months, `min(2, mtc)` | **2.0** | **1.5** |
| Charge avoided per unit | $7.68 | $4.92 |
| **Ceiling** | **$10.75** | **$7.99** |
| Conversion rate | 2.18% | 2.95% |
| Floor bid | $0.25 | $0.25 |
| **Max profitable CPC** — profit ends | **$0.067** | **$0.091** |
| **Max click price** — forward cash ends | **$0.234** | **$0.236** |
| Subsidy per unit at the floor bid | $8.40 | $5.40 |
| Charge avoided per unit | $7.68 | $4.92 |
| **Gap** | **$0.72 over** | **$0.48 over** |
| Ad cost per unit shipped | $11.35 | $13.38 |
| Refund rate | 26.1% | 19.4% |
| **Ad cost per unit cleared** | **$15.36** | **$16.60** |

Two things this table shows that no single number would.

**The whole workable band sits below the floor.** Both children's max click price is under the $0.25 minimum bid, so the floor governs and every click is subsidised past what the avoided charge justifies — by 48 to 72 cents a unit. The push still runs, per the ruling, but the plan states that gap and sends it to the pricing recommendation, because a small price move changes every row here.

**The acceleration cap is doing real work.** Taken at Child A's full 4.4 months, its ceiling reads $19.97 and a max click price of $0.44, and the child looks comfortably affordable. Capped at two months it reads $10.75 and $0.234, and the same child is over. The cap is not conservatism for its own sake — it is the difference between two opposite readings of the same product.
