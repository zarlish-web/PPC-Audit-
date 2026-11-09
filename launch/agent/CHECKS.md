# The 8 daily checks

Every morning the agent runs these 8 checks on yesterday, the newest complete day, for each product in `products/`. Each check reads one fixed source and applies one written rule. The result is one plain line in the Slack post.

The agent is read-only on the ad account. It never changes a bid, budget, status or target. When a check fails its rule, it writes a proposal, and the owner decides.

| # | Check | Source | Rule | Flags when |
|---|---|---|---|---|
| 1 | Sales and profit | Sellerboard `dashboard_period`, All and each size | Units, sales, ads split SP / SB / SBV / SD, TACoS and net profit, compared with the day before and the pre-ads baseline. A storage-fee day is shown with and without the fee. | Net is negative without the storage fee, or units are below the 7-day pace by more than 25% |
| 2 | Parent check | Sellerboard `dashboard_table` (product, group by parent) | The parent ASIN must equal the SKU-prefix total. Any SKU outside the parent is named. | Parent differs from the total |
| 3 | Ad efficiency | Sellerboard (SP) and brand table `CLCS4-SB` | ACoS by ad type against break-even (`economics.break_even_acos`). Each size's share of ad spend against its share of units. | A size takes much more of the ad money than its share of units, or an ad type stays above 2× break-even for 3 days |
| 4 | Stop-loss | Cumulative campaign rows (`source/sb_campaigns.csv`) | A campaign with at least 30 clicks and 3 days of data whose ACoS is above 2× break-even is a cut (D25). Campaigns between 22 and 29 clicks are listed as "next to reach 30". | Any campaign crosses the line |
| 5 | Waste | Search terms and campaigns | Pause rule: more than 10 clicks and 0 orders over 2–3 days. Searches that are not about cooling sheets become relevance negatives. | Any term or campaign meets the rule |
| 6 | Rank guards | Command center `ppc_ranks` | Head and size terms, day on day, with the 7-day median. Each guard in `rank_guards` is tested. | A guard is hit, or a head term moves 10 or more places on 2 crawls in a row |
| 7 | Stock and reorder (variation level) | Sellerboard `inventory` and `fba_shipments`; command center `ltsf_portfolio` | Work at colour level, not only size level. For each SKU: days of stock (FBA ÷ velocity) against its boat date, the highest daily pace that still lasts to the boat, and the age bracket counted from the shipment's receive date. Compare with the owner's BFCM projection for each colour once there is one. | A colour is out of stock or will run out before its boat; it needs a slower pace than it has now; or it will still hold units when it reaches 181 days |
| 8 | Engine audit | Command center `ppc_decisions` | Yesterday's engine changes are counted (raises, cuts, budget delta). Owner moves are matched to a logged decision. Our open proposals are checked to see whether they were applied. | The engine made a change no decision explains, or it acted against an open owner decision |

## Gates the agent respects

- **No decisions on early data.** Nothing new is cut before 14 full days. A cut needs at least 3 consistent daily reads. The last 2 days are still filling with late orders.
- **One day never changes a call** on its own.
- **Owner decisions win.** When the owner has a logged decision (D-number), the agent reports against its gate and return line. It never argues with the decision in the post.
