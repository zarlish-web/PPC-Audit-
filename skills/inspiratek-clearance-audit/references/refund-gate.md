# The refund gate

Before routing any spend by days of cover, check whether refund rates vary by variant. If they do, cover alone will send money at stock that comes back.

## Why cost per unit *cleared* is the right measure

A returned unit costs the advertising, costs the refund handling, and returns to stock. So:

```
ad cost per unit cleared = ad cost per unit shipped ÷ (1 − refund rate)
```

Worked example at $12.91 per unit shipped against a $19.69 ceiling:

| Refund rate | Per unit cleared | Verdict |
|---|---|---|
| 0% | $12.91 | Fund |
| 10% | $14.34 | Fund |
| 25% | $17.21 | Marginal |
| 30% | $18.44 | Marginal |
| 37.5% | $20.66 | Loss-making |
| 45.5% | $23.69 | Loss-making |

## Tiers

- **BLOCK** — reliable sample, rate at or above 35%. Pause. Advertising converts spend into reverse logistics.
- **FLOOR** — reliable sample, 22–35%, or named in quality complaints. Keep live at a reduced budget. Marginal, not loss-making. Do not scale.
- **FUND** — everything else. Advertise normally and carry on every new campaign.

## Sample-size guard

**Require at least 10 units sold in 30 days before acting.** One variant showed a 125% refund rate on four units sold and five returned — far too thin to block on, and blocking it would have removed 245 units of stock from the plan on noise.

## Two things to watch

**The gate can contradict the search data.** On one product the best-converting colour term in the entire category (6.91% market CVR, 375 units in stock) belonged to the variation named in the colour-accuracy complaints. Search data said fund it; refund data said floor it. Refund data wins, and the document should say so explicitly rather than quietly dropping the term.

**Restrict Auto and remarketing too.** Auto campaigns and views remarketing will route traffic to blocked variants unless the SKU list excludes them.

## Say what the gate costs

If the gate blocks a large share of the pool, the plan cannot promise volume growth. State plainly what percentage is held back, what releases it, and who owns that fix — it is usually the highest-value item on the product and it is not a PPC item.
