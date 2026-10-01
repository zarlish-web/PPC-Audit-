# Independent review — PPC audit run 20260929-08832fbc

**Product:** Sleephoria Cooling Sheets 4 Piece (SCS4) · US · stage RANKING (Re-Launch)
**Run audited:** 2026-09-29 · **Reviewed:** 2026-10-01 · **Stored agent review:** #43 (endorse, 38 holds)
**Inputs:** `ppc-audit-20260929-08832fbc.json` (the full export) and `ppc-audit-SCS4-20260929-08832fbc.xlsx` (the same run, rendered)
**Row-by-row verdicts:** `SCS4-20260929-review-verdicts.xlsx` (all 395 decisions: review 43's verdict next to ours, with the reason for each)

---

## 1. Bottom line

**Verdict: endorse the direction, but don't deploy the run as it stands.** Pushing top of search on a slipping Cooling focus is the right call. But review 43 passed about 26 rows that contradict the run's own data, and 4 dose rows need their price capped. Separately, the run's money mostly goes to long-tail terms. Two of the three head terms the review gives as the reason for the push get almost nothing.

| | Before | Engine (all 395 rows) | After review 43 | After this review |
|---|---|---|---|---|
| Ad spend / day | $205.86 | $640.95 | $375.79 | ≈ $340–355 |
| ACoS | 29.6% | 44.2% | 35.2% | ≈ 34–35% |
| TACoS | 9.3% | 21.6% | 14.6% | ≈ 13.5–14% |
| Rows held | — | — | 38 | 64 held · 4 corrected · 23 flagged |

Break-even ACoS is 38.9% (brief.margin). However, 31 places in the sweep rows use 35.3%, so the run uses two break-even figures (§5).

**Before deploying:**
1. **The run is 2 days old.** Its day-4 and day-7 checkpoints are dated 2026-10-03 and 2026-10-06/07. If you deploy today (10-01), every read window is 2 days shorter than the engine assumed, and the stock it read is 2 days stale. Re-run, or move every prediction date forward by 2 days.
2. **Make sure only one run gets uploaded.** Run 20260928-556ec5e2, from one day earlier, was also endorsed (review 23). The latest "last read change" dates in this run are 09-13, so the 09-28 run looks like it was never uploaded. Confirm that before uploading this one (W1).
3. **Get the approvals your own rules require.** Under `config/thresholds.yml`:
   - Spend rises 83% even after holds. That is above the 15% envelope line, so the brand owner has to approve it (M7).
   - ACoS runs past break-even. That requires a below-break-even proposal with an end date, approved by the brand owner (`authority.below_breakeven_run`).
   - Several modifier moves are +150 to +330 points, against the weekly limit of 20 points per 14 days (W6).

   The engine runs on its own operator rulings, but these are your written gates.

---

## 2. The strategic gap: the head terms barely move

Review 43 justified the push with three head terms that are slipping. Here is what the run does for each:

| Term | SV | Rank 30d ago → now | What this run does |
|---|---|---|---|
| cooling sheets | 77,377 | 8 → 18 | TOS 160→204% reshape: **+0.54 TOS clicks/wk, +$0.20/day** (+30% budget) |
| cooling sheets queen | 30,225 | 32 → 46 (held #14 earlier) | **Nothing.** The engine ranked this dose #1 in its fill order, with the best odds (41%). It then held it as "NOT SERVING": $0 spent in 14 days, 359 impressions in 90 days, base $1.00, LEGACY_FOR_SALES. The fix it names (fixed bidding, re-price) is never written as a row for a person to act on. |
| cooling bed sheets | 12,715 | 10 → 20 | Human step to re-enable its paused owner (1849). The revive price is left as an "open ruling". The owner spent ~$111 in the last 14 days, so it was paused very recently, and that may be why the rank fell. |

Meanwhile, the new campaigns proposed by the run total $308.78/day. $193/day of it is 27 explores and 4 tails, almost all on terms with 500–1,000 SV, and the 15 doses add $76.66/day.

**Our recommendation, as manual steps this week:**
- **cooling sheets queen**
  - Switch the campaign to fixed bids.
  - Set base $1.00 and TOS ≈ 235%. That gives $3.35 effective, which is the group's own bound and still inside the $4.13 break-even ceiling the engine computed for this term.
  - Set budget $18/day.
- **cooling bed sheets:** re-enable 1849 today at its prior $1.00 bid.
- **cooling sheets:** the plan needs 1,352 paid clicks a week ($3,715/wk) to reach rank 3. The term's break-even ceiling is $1.96 against a $2.63 clearing price. That target can't be funded, so it should go back to target-setting rather than being under-funded in small steps.

---

## 3. What review 43 got right

- **Held 29 creates on QUEEN-WHITE and 7 on TWIN-WHITE.** QUEEN-WHITE has 84 units and TWIN-WHITE has 11. The engine's own LOAD rows (1291, 1288) say neither can carry the load, and the same mistake was held in review 23 the day before. This is an engine bug (§5).
- **Held the KING-GRAPHITE conquest (1401)** and **the Midnight Black dose (65)**. Both are stock-led.
- **Passed the 38 child swaps.** 31 King campaigns move from KING-GRAPHITE (18 available, 9 days, NO_ROOM) to KING-WHITE (776, 179 days). Six King-term campaigns that advertised a **Queen** child are corrected. Row 1280 re-points the conquest from FULL-WHITE (7 units) to FULL-NAVY-BLUE.
- **Negatives, retags, folds and pauses.** The 8 negative rows (cross-campaign walls plus 2 zero-order fences), 13 retags, 4 folds and 6 dead-duplicate pauses are all sound.
- **Last cycle's manual fix landed.** The Cal King campaign that advertised SAGE-GREEN (0 units) now serves CAL-KING-GRAPHITE.

---

## 4. Rows we change from review 43 (53 rows)

### 4a. Hold: contradicts the run's own data (26 rows)

| Rows | Move | Why it is held |
|---|---|---|
| 1853, 1854 | Re-enable "king sheets cooling", "cooling king sheets" | Both would come back on **KING-GRAPHITE** (18 units, 9 days, NO_ROOM) with no swap row, while the same run moves 31 campaigns *off* that child. Swap to KING-WHITE, then enable. |
| 1867, 1879, 1880, 1881, 1882 | "RE-PRICE or pause" (human step) | These campaigns are **already paused**. Their terms are rebuilt by creates whose own text says the paused owner "stays paused (SOP-29: never two enabled)". If a person acts on these rows, the term ends up with two enabled exacts. |
| 1864, 1874 | Re-price | The campaign is under a **rank-collapse freeze** (1886, 1888: every bid, modifier and budget holds). |
| 1858–1860, 1862, 1863, 1865 | Re-price (human step) | Already handled in this run: each campaign's TOS row already re-prices it. Acting on both moves the same lever twice. |
| 59 | Budget $10→$13 (Full, out of focus) | The engine's own read on this campaign is **TAPER −10%**, but the budget pass raised it 30% anyway. The campaign converts at 5.9% on 389 clicks (~$51/order against ~$28 contribution). |
| 146+149, 266+269 | Reshape pairs | Both hold the top-of-search price **to the cent** ($2.84) yet predict TOS clicks 0.31→32 and 0.08→32 a week. Rows 1857 and 1861 on the same campaigns say $2.84 is under 70% of the market bound, i.e. not in the auction. Let the human re-price instead. |
| 44 (+43, 47 as its pair) | Dose 150→385% | 6.9% CVR on 87 clicks means ~$58 per order against $28.69 contribution. The row states an $8.58 loss because its PRICES section was computed on the superseded 177% value. |
| 116 | Dose 122→288% | 0 orders on 18 top-of-search clicks, 5.9% blended CVR, and the term is already rank 4. |
| 402 | Dose 107→262% | 11 clicks, 0 orders. |
| 412 | Dose 145→329% ("best cooling sheets") | **46 clicks, 0 orders in 90 days.** Under `thresholds.yml` W4a that is a negation candidate, not a dose. |

### 4b. Correct: cap the dose at the engine's own market bound (4 rows)

A "dose" deliberately skips every price cap, including the campaign's own market bound (its observed TOS CPC + 15%). That makes these doses bid 1.5–1.6× the price the auction actually clears at. The odds don't support it: the engine's own figure is **~20% that a dose lands**, based on 97 past doses.

| Row | Term | Written (eff.) | Corrected | Why |
|---|---|---|---|---|
| 24 | cooling queen sheets | 474% ($7.75) | **280%** ($5.13) | bound $5.13; true cost ~$53/order vs $28.25 |
| 70 | queen cooling sheets | 581% ($6.13) | **334%** ($3.91) | bound $3.91 |
| 89 | queen bed sheets cooling | 525% ($7.56) | **285%** ($4.66) | bound $4.66; row says $1.14 loss, real ≈ $14 |
| 121 | queen size sheets cooling | 303% ($5.72) | **196%** ($4.20) | group bound $4.21; 8.1% CVR |

The King doses (39, 136, 213, 320) and 310 stay as written. Their campaigns convert at 12.5–15%, so even at the dose price they sit close to break-even per order.

### 4c. Flag: they stand, but a person should know (23 rows)

- **King explores 1502, 1514, 1778** (passed by review 43). They open at $3.36 effective TOS, which is 68% of the engine's own Cooling|King bound ($4.94). In this same run, the engine calls existing King campaigns at $3.17 "NOT IN THE AUCTION" because they are under 70% of that bound. So these explores are priced to miss their 15-click read. Open them at ~125% TOS ($4.29, the group's clearing price), or accept a slow read.
- **17 rows that move a lever together with a child swap on the same campaign** (13, 39, 136, 174, 180, 213, 285, 320, 276, 354, 427, 1, and the budgets 7, 38, 135, 212, 319).
  - The swaps are right. But the rank claims are still read **on the child being swapped out** (KING-GRAPHITE; on G18, QUEEN-GRAPHITE for a King term).
  - Review 23 held exactly this pattern ("swap first, then take the step next run"). Review 43 passed it.
  - At minimum, re-point the rank read to KING-WHITE. Otherwise those grades mean nothing.
- **34, 165:** the prediction is the flat 32/wk "read floor", not what the step buys.
- **1254 (G32 swap to KING-WHITE):** the campaign also holds an enabled **"cold bed sheets queen"** exact. After the swap, a Queen search would show a King set. Pause that one target (1 click, 0 orders) when you do the swap.

### 4d. Twin: same hold, different child

Review 43 held the 7 Twin creates and told the team to rebuild them on **TWIN-CREAM** (39 units). The engine's own variation row 761, and review 23, chose **TWIN-GRAPHITE**: 37 units + 30 inbound, 47 days of cover, 13.2% CVR on 167 clicks. We recommend TWIN-GRAPHITE.

---

## 5. Engine bugs to fix (not judgement calls)

1. **Creates ignore the serving-child rule.** 29 creates went onto QUEEN-WHITE and 7 onto TWIN-WHITE, even though the engine's own LOAD rows 1291 and 1288 rule against those children. This is the second run in a row; review 23 held the same rows.
2. **Dose rows mis-state their own economics.** PRICES, "LOSS per order" and the market bound are computed on the superseded reshape value (e.g. 239%), not the written dose value (e.g. 474%). This happens on all 15 doses.
3. **Predictions are set to the read floor rather than to the expected result.** Eight TOS rows claim 32 clicks a week, but the run's own `forecast_caps` count only 1.8–21. Rows 146 and 266 claim it at an unchanged price. These rows will grade as misses by construction and drag down the grade history for every other row.
4. **Several rank claims per row, and claims that contradict the row's own text.**
   - Row 24 carries three different rank claims: ≤11 by 10-07, ≤11 by 10-27, and ≤4 by 10-27.
   - Rows claim 31→≤10, 34→≤8 and 22→≤3 in 14 days. Their own TIMELINE section calls 15+ positions "a twelve-to-eighteen-month position".
5. **Rank claims are read on the child being swapped out**, in the same run that swaps it (§4c).
6. **The rank-collapse baseline is mislabelled.** Rows 1886 and 1887 say "lost in 30 days" but measure from 2026-04-01 and 2026-03-28, six months back.
7. **NOT-IN-THE-AUCTION structure rows are emitted for paused campaigns** (1867, 1879–1882).
8. **Explore prices use a different market figure than the auction test.** The explore price is the mean campaign TOS CPC ($3.36 King). The auction test uses the click-weighted clearing price ($4.29, bound $4.94).
9. **The budget pass overrides a TAPER verdict** (row 59).
10. **Enable rows don't check the child's stock** (1853, 1854).
11. **A held #1 dose produces no task for a person** ("cooling sheets queen"). The fix exists only inside a held row.
12. **Child swaps move the whole campaign, including terms for another size.** G32 (1254) moves to KING-WHITE but still carries the enabled exact "cold bed sheets queen". Bid row 58 for that target is also labelled "cool king sheets".
13. **Two break-even ACoS figures.** The brief and review use 38.94%; 31 sweep mentions use 35.3%. There are also 18 different "contribution per order" values, from $20.82 to $35.31.
14. **Mislabels.** Matching children are labelled "MISMATCH" (781, 802, 771). Rename 2055 writes TWIN-GRAPHITE into a name whose child stays QUEEN-GRAPHITE. Float artefacts appear in predictions (`0.11271500000000001`).

---

## 6. Things that can't be checked from the export

- **`brief.grades`: 0 graded in 90 days, hit rate null.** None of the engine's predictions have been scored yet. Every "the book bought ×3.76" figure is a prior, not a track record.
- **`brief.tuner`: 2 open records, AHEAD.** The export doesn't name the campaigns, so the "no conflict" answer can't be checked.
- **QUEEN-LIGHT-PINK stock (create 1610)** isn't in the brief. The row says it cleared the cover-unknown hard stop. Check it at the day-7 read.
- **Renaming 168 campaigns** keeps the IDs, so the bulk upload is safe. Anything keyed on the campaign name will lose its history mapping: DataDive campaign lists, Sellerboard tags, team sheets.

---

## 7. Deployment order (if approved)

1. **Today, by hand:**
   - Re-enable 1849 ("cooling bed sheets").
   - Fix "cooling sheets queen": fixed bids, $3.35 effective TOS, $18 budget.
   - Do the 38 child swaps.
2. **Bulk upload:**
   - Every row passed or corrected in `SCS4-20260929-review-verdicts.xlsx`.
   - Leave out every row marked *hold*.
3. **Human-built creates:**
   - SB and SBV for King (1345, 1353) on KING-WHITE.
   - The Queen and Twin creates rebuilt on QUEEN-GRAPHITE and TWIN-GRAPHITE.
   - Only open as many Twin creates as TWIN-GRAPHITE's cover carries.
4. **Day-4 / day-7 reads.** Shift the dates if you deploy after 10-01. Read top-of-search clicks first, then rank on the **new** child.
