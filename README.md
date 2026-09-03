# PPC Oversight System

An operating manual for running an Amazon Sponsored Ads portfolio at three tempos.

The daily tier **protects**, the weekly tier **steers**, the monthly tier **decides**. Each tier
reads only the signals that have matured by the time it runs. That separation is the whole point:
it is why accounts run this way compound instead of oscillate.

| | Daily | Weekly | Monthly |
|---|---|---|---|
| **Role** | Control — stop loss | Steering — the work | Strategy — the direction |
| **Timebox** | 15 min, exception-based | 75–90 min, fixed weekday | Half day, within 5 days of close |
| **Owner** | PPC Specialist | Manager decides, Specialist prepares | Account Lead with Manager |
| **Reads** | Spend, delivery, eligibility, stock, Buy Box | 14d bids, 30d budget & placement, 60d search terms | Settled P&L, TACoS, rank, mix, lever decay |
| **Moves** | Pauses and budget relief only | Bids, placements, budgets, negatives, harvests | Envelope, objective mix, structure, thresholds |
| **Never touches** | Bids, placements, negatives, structure | Envelope, architecture, margin assumptions | Individual keyword bids |

**Full manual:** [`docs/ppc-oversight-system.html`](docs/ppc-oversight-system.html) — §1 principles,
§2 signal maturity, §3–§5 the three tiers, §6 threshold library, §7 decision rights, §8 report
formats, §9 failure modes.

---

## The seven principles

1. **Match the window to the data's maturity.** SP attribution runs 7 days (14 on some reports).
   The last 72 hours of conversion data is always incomplete.
2. **Sufficiency before action.** No bid cut under 10 clicks, no negation under 2× target CPA,
   no CVR read under 20 clicks. Below the bar, "keep observing" is the decision — and it gets logged.
3. **One lever per entity per cycle.** Move the bid, or the placement, or the budget. Not all three,
   or you learn nothing about which one worked.
4. **Observation lock.** Anything changed is frozen 14 days; new campaigns 21. Re-judging early is
   the main cause of bids that never converge.
5. **Every action is graded.** Each cycle scores the changes from two cycles ago as
   worked / flat / backfired. A lever flat twice on one entity is retired for it.
6. **Thresholds are set before the breach.** They live in `config/thresholds.yml` and change only at
   the monthly review, with a dated reason.
7. **A null result is an output.** "No exceptions" is logged. An empty log and a skipped check look
   identical in hindsight.

---

## Daily — control (15 min)

Catch breakage and stop loss. Not an optimisation pass.

| ID | Check | Trigger |
|---|---|---|
| D1 | Account & ad eligibility | Any ineligible ad on a top-20 spend ASIN |
| D2 | Delivery integrity | 0 impressions 2 days after ≥ 500 impressions in prior 7d |
| D3 | Buy Box & inventory | BB < 90% · DOH < 21 days · any OOS advertised child ASIN |
| D4 | Spend pacing | MTD pace > ±10% of plan (P2 beyond ±20%) |
| D5 | Spend anomaly | Daily spend > 150% or < 50% of own trailing 7-day mean |
| D6 | Budget cap timing | Out of budget before 18:00 · before 20:00 if Ranking |
| D7 | Runaway spend | ≥ 3× target CPA, 0 orders, ≥ 5 rolling days |

**Pre-authorised:** pause OOS/BB-lost ads · budget relief ≤ +25% once per campaign per week ·
circuit-break pause on D7. **Out of scope:** bids, placements, negatives, structure.

**Output:** `templates/daily-exception-log.csv` — one row per exception, or one NIL row.

---

## Weekly — steering (75–90 min)

Run in order. Gates precede bids because a bid set before its gate is known is set blind.

| ID | Step | Key rule |
|---|---|---|
| W1 | Execution verification | Diff last cycle's approved log against the live bulk. **Approved ≠ uploaded.** Blocks the cycle. |
| W2 | Grade the matured cycle | Score changes from 2 cycles ago vs. their recorded expected outcome |
| W3 | Set the gates | DOH, that SKU's break-even ACoS, and the campaign objective — all three, or skip the SKU |
| W4 | Search-term pass | Negate ≥ 2× CPA / 0 orders / ≥ 10 clicks / 60d · harvest ≥ 2 orders at ≤ target ACoS |
| W5 | Bid pass | By objective. ±15% routine, ±25% correction, no direction reversal inside 14d |
| W6 | Placement pass | ≤ 20 points, one move per campaign per 14 days |
| W7 | Budget pass | Reallocate inside the envelope. Envelope changes escalate to monthly |
| W8 | Hygiene sweep | Nothing carried more than two cycles |
| W9 | Package, log, approve | Log written **before** upload; ≤ 25-word rationale, expected outcome, review date |

**Lever hierarchy:** bid → placement modifier → budget → negation/harvest → structure (escalates).

**Output:** decided bulk + `templates/weekly-change-log.csv` + a five-line summary.

---

## Monthly — strategy (half day)

The only tier that may change the envelope, the objective mix, the structure, or the thresholds.

| ID | Step | Key rule |
|---|---|---|
| M1 | Profit truth, not ACoS | CM2 after ads per SKU; TACoS 6-month trend |
| M2 | Objective mix vs. stage | Launch 50/30/15/5 · Scale 35/25/30/10 · Harvest 15/15/60/10 |
| M3 | Rank progression | Sufficiency stop at 21 days held; 8 weeks with no movement → re-diagnose |
| M4 | Lever effectiveness | Lever < 40% "worked" is a diagnosis problem, not a tuning problem |
| M5 | Coverage & competitive | Uncovered terms ≥ 500 SV, SOV, new entrants, price pressure |
| M6 | Structure & lifecycle | Sunset < 10 clicks / 0 orders / 60d · promote after 3 cycles at target |
| M7 | Next envelope | Capped by inventory cover; > +15% needs brand owner approval |
| M8 | Threshold review & report | Never-fired and always-fired are both defects |

**Output:** `templates/monthly-review-pack.md` + next envelope + threshold changes, with the
stakeholder summary written as Finding → Why it matters → Action → Expected impact.

---

## Severity ladder

| Level | Response | Who acts |
|---|---|---|
| **P1** | 2 hours | Specialist, under pre-authorisation; Manager told same hour |
| **P2** | Same business day | Specialist proposes, Manager approves |
| **P3** | Next weekly cycle | Manager |
| **P4** | Next monthly cycle | Account Lead |
| **P5** | Scheduled with the brand | Brand owner |

Severity comes from the threshold that fired, never from whoever noticed it — otherwise everything
becomes P1 within a month and the ladder stops carrying information.

Authority limits (who may move what, how far) are in `config/thresholds.yml` under `authority`,
and in §7.2 of the manual.

---

## Repository layout

```
docs/ppc-oversight-system.html   The full manual, §1–§9
config/thresholds.yml            Every threshold, in one versioned place
templates/daily-exception-log.csv
templates/weekly-change-log.csv
templates/monthly-review-pack.md
```

## Setting it up

1. Fill in `meta` and `skus` in `config/thresholds.yml` — per-SKU break-even ACoS is not optional;
   an account-wide ACoS target starves profitable products to subsidise thin ones.
2. Pick the weekly run day and hold it. Tuesday works well: the weekend has settled and there is
   still a working week to react in.
3. Run four weekly cycles before judging any threshold. The first W2 grade cannot exist until
   cycle 3.
4. At the first M8, retune the §6 values to your own CPA and volume — then leave them alone
   between monthly reviews.

The structure is the durable part. The numbers are a starting position.
