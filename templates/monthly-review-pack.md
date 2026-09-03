# Monthly Review Pack — <Portfolio> — <Month YYYY>

Owner: Account Lead with PPC Manager · Run within 5 working days of month close.
One tab / section per step M1–M8. Every finding cites the §6 trigger ID that produced it.

---

## 1 · Summary

Five lines, written last. Spend, sales, ACoS, TACoS, and the single most important thing that changed.

| Metric | This month | Last month | Δ | Note |
|---|---|---|---|---|
| Ad spend | | | | |
| Ad sales | | | | |
| ACoS | | | | |
| TACoS | | | | |
| CM2 after ads | | | | |

---

## 2 · M1 — Profit truth

Per SKU: spend, ad sales, ACoS, break-even ACoS, CM2 after ads, contribution.
TACoS plotted across six months. Read profit, not efficiency — they disagree on multi-SKU portfolios.

| SKU | Spend | Ad sales | ACoS | Break-even | CM2 after ads | Verdict |
|---|---|---|---|---|---|---|

**Trigger check:** M1 fires at TACoS +3 pts over 3 months → full efficiency review.

---

## 3 · M2 — Objective mix vs. product stage

Share of spend by objective against the reference mix for each product's stage.

| SKU | Stage | Ranking | Discovery | Profitable | Defensive | Drift vs. reference |
|---|---|---|---|---|---|---|

Reference: Launch 50/30/15/5 · Scale 35/25/30/10 · Harvest 15/15/60/10. Alert at 10 pts drift.

---

## 4 · M3 — Rank progression

Target keywords vs. rank targets, from the weekly rank log. The question is whether ranking spend
is buying rank or only buying sales at a worse ACoS than the profit campaigns would have returned.

| Keyword | SV | Rank target | Start of month | End of month | Weeks funded | Spend | Verdict |
|---|---|---|---|---|---|---|---|

**Sufficiency stop:** target rank held 21 days → step ranking spend down 20% per cycle and watch.
**Alert:** 8 weeks of ranking spend with no movement → re-diagnose listing, price or reviews. Not bids.

---

## 5 · M4 — Lever effectiveness

Aggregate this month's W2 grades by lever. Levers decay; a lever below a 40% "worked" rate is a
diagnosis problem, not a tuning problem.

| Lever | Changes | Worked | Flat | Backfired | Worked rate | Action |
|---|---|---|---|---|---|---|
| Bid | | | | | | |
| Placement modifier | | | | | | |
| Budget | | | | | | |
| Negation / harvest | | | | | | |

---

## 6 · M5 — Coverage & competitive position

- Uncovered terms ≥ 500 SV: 
- Share of voice, top-20 terms: 
- New advertisers on head terms: 
- Competitor price / Buy Box pressure: 

---

## 7 · M6 — Structure & lifecycle

| Campaign | Stage | Spend 60d | Clicks 60d | Orders 60d | Action | Rationale |
|---|---|---|---|---|---|---|

**Sunset:** < 10 clicks and 0 orders over 60 days → archive (keep the keyword in the master list).
**Promote:** 3 consecutive cycles at ≤ target ACoS → scale.

---

## 8 · M7 — Next month's envelope

| Objective | This month | Next month | Δ | Inventory cover check |
|---|---|---|---|---|
| Ranking | | | | |
| Discovery | | | | |
| Profitable conversion | | | | |
| Defensive | | | | |
| **Total** | | | | |

Envelope increase > 15% requires brand owner approval with a forecast attached.
No objective may be funded past its SKU's inventory cover.

---

## 9 · M8 — Threshold review

Thresholds that never fired and thresholds that fired constantly are both defects.

| Threshold ID | Times fired | Verdict | Change | Reason | Effective |
|---|---|---|---|---|---|

All changes are written back to `config/thresholds.yml` with a dated entry in its `changelog`.

---

## Stakeholder summary

For the brand owner. One block per finding, in this order — it is the only format non-specialists
reliably act on.

### Finding 1 — <headline>
- **Finding:** what the data shows. Cite the trigger ID.
- **Why it matters:** the money or the rank consequence, quantified.
- **Action:** what will be done, by whom, by when.
- **Expected impact:** the number we expect to move, and when we will know.
