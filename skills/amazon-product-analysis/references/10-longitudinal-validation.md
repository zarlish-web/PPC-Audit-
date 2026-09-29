# 10 — Longitudinal validation: ledger, grading, escalation, validation plan

Read in Phase 9, and at the **start** of any refinement cycle (grading comes before any new decision). Every decision this skill makes is a prediction; this file is how predictions are recorded, checked and acted on.

## Contents
1. The cycle loop
2. Records: action log, impact ledger, manager responses
3. Week-1 (no prior cycle)
4. Execution verification
5. Grading order
6. Escalation loop
7. Marginal read and freeze
8. Refinement: grading a prior plan
9. Prediction format
10. Reversal conditions
11. Validation plan template and standard checkpoints
12. Read-window rules
13. What to surface every cycle
14. Open questions for the owner

---

## 1. The cycle loop

Run in this order every cycle. Do not decide anything new on a row until steps 1–4 are done for it.

1. Load the prior action log, the impact ledger and any manager responses. None supplied → Week-1 (§3). [SR]
2. **Verify execution** of every logged action against the new bulk/console state (§4). [SR, WB, LTSF]
3. **Grade** each executed action in the fixed order (§5). [SR, PB]
4. **Update the ledger**: counters, escalations, manager-acted grades, freezes/floors (§6–7). [SR]
5. Decide this cycle's rows (master decision order in SKILL.md). Escalated rows are held and referred, not re-decided by formula. [SR]
6. Write new log rows, each with a prediction (§9) and a reversal condition (§10). [SR, PB]
7. Write the validation plan (§11) — dated checkpoints with pass conditions and fallbacks. [B6]

Why this order: a lever that was never applied, or applied during a deal, or priced on economics that have since moved, cannot be credited or blamed. Grading first stops the next decision repeating a failure.

---

## 2. Records

### 2.1 Action log (one row per actioned unit per cycle)

**Which rows are logged:** any row with a new bid, new placement %, new budget, or an action containing negate / pause / refer / retag; plus by-hand actions (variation switches, SB/SD builds), which are verified from the console or next export. [SR, B6]

**Log ID** = `cycleDate|CampaignID|KeywordID-or-TargetID` — idempotent: re-running the same cycle overwrites, never duplicates. [SR]
**Unit** = keyword/target × match type × objective (summed across rows of the same unit). [SR]
**Lever recorded** (first that changed): Bid > Placement > Budget > Negation/Status. [SR]

| Group | Fields |
|---|---|
| Identity & context | Log ID, cycle date, campaign (name + ID), target/keyword ID + text, match type, advertised SKU, objective, stage, deal state, LTSF state, DOH/zone, break-even ACoS, target ACoS, max acceptable ACoS [SR] |
| Change | lever, action (decision label), reasoning, before → after bid, bid Δ%, before → after placement %, before → after budget [SR] |
| Baseline (as read this cycle) | spend, sales, orders, clicks, ACoS, TACoS, CTR, CVR, WAS%, TOS %, impression share, organic rank, RPC, DSTR, break-even used to price the action [SR] |
| Prediction | expected metric, direction, magnitude, tolerance, horizon/timeframe, basis tag (HIST / MARKET / TEST), review date [SR, PB, LTSF] |
| Reversal | reversal condition + what happens if it fires (§10) [PB, WB] |
| Result (filled next cycle) | execution status, verdict, actual value, root cause, follow-up [SR] |

Defaults when no prediction was written: expected metric = organic rank for Ranking / Re-Ranking objectives, ACoS otherwise; tolerance ±3 ranks / ±3 ACoS points; timeframe "within 1–2 cycles"; Result = OPEN. [SR]

**Retention:** keep every row forever; trailing reads and streaks use a **rolling 12-week window**. The log is the history store. [SR]

### 2.2 Impact ledger (one row per unit, carried forward; lives outside the workbook)

**Key** = `CampaignID|Target-or-KeywordID`. [SR, WB]

| Field | Meaning |
|---|---|
| IDs, keyword/target, SKU, objective | identity |
| Last cycle graded, last verdict | most recent grade |
| Consecutive no-impact | count of consecutive FLAT/BACKFIRED grades |
| Escalate | true when consecutive no-impact ≥ 2 |
| Last ACoS Δ / last rank Δ, last lever | what moved and with which lever |
| History | verdict string, e.g. `FLAT>FLAT>M:WORKED` (M: = manager-acted grade) |
| Loop status | OPEN → ESCALATED → MANAGER_ACTED → RECOVERED or MANAGER_INEFFECTIVE |
| Manager action / lever / date / baseline ACoS + rank / verdict | captured when a manager acts on an escalated unit |
| Freeze/floor bid + date | recorded on saturation (§7), on a BACKFIRED raise, and on every taper/ladder floor |
[SR]

### 2.3 Manager responses (input)
File columns: Key, Manager Action, Manager Lever, Manager Action Date. Read before grading so an escalated unit the manager changed is graded as MANAGER_ACTED, not as the formula's lever. [SR]

---

## 3. Week-1 (no prior cycle supplied)

- No impact review, no verdicts, no escalation. [SR]
- Write the full baseline for every unit: bid, budget, placement %, clicks, spend, sales, orders, ACoS, TACoS, CVR, CTR, rank, impression share, DSTR, inventory. [SR]
- State it in the output: "No prior cycle supplied — treated as first cycle. Impact review skipped. Baseline written." [SR]
- If an earlier plan exists but no log (refinement without a ledger), grade against the plan's written predictions (§8) and say the ledger starts now. [PB]

---

## 4. Execution verification

Verify before grading. An action that never reached the account cannot work or fail. [SR, WB, LTSF]

| Status | Test (bids) | Effect |
|---|---|---|
| **EXECUTED** | \|actual − recommended\| ≤ $0.01 | Graded normally |
| **NOT_EXECUTED** | \|actual − before\| ≤ $0.005 | No verdict, no counter movement; **re-issue** the recommendation (re-check it still holds) |
| **PARTIAL** | changed, but not to the recommended value | Graded with a note; **never counted** toward escalation |
| **UNVERIFIABLE** | no bid recommendation on the row (negation, status, referral) | Graded normally |
[SR]

- Placement %, budget and state changes: no source tolerance exists — treat an exact match to the written value as EXECUTED and record the rule used. Negations/pauses: verify where the new bulk shows them (negative row present, state = paused); otherwise UNVERIFIABLE. [SR; decide and record]
- **Execution rate** = EXECUTED ÷ (all logged actions with a verifiable value). Report every cycle. **< 80% = follow-through problem**, stated openly in the summary, not buried. [SR]
- Never blame an un-uploaded recommendation; never grade an undeployed action. [SR, WB, LTSF]

---

## 5. Grading order (first match wins)

| # | Test | Verdict | Counter |
|---|---|---|---|
| 1 | Logged this cycle (log date = cycle date), or horizon not yet reached | **TOO_SOON** | no change [SR, WB] |
| 2 | Grading span overlaps a deal/event window | **DEAL_WINDOW** — no WORKED/FLAT/BACKFIRED; re-grade on the first clean cycle | frozen [SR] |
| 3 | Unit absent from this cycle's data; or a second lever changed on it inside the window; or the advertised SKU changed (re-route) | **CONFOUNDED** | not counted [SR, LTSF, PB] |
| 4 | Execution (§4) | NOT_EXECUTED → stop here; PARTIAL → continue, flag | per §4 [SR] |
| 5 | Break-even the action was priced on vs current break-even shifted **> 10%** (price, fee, packaging, LTSF event); or a logged price change coincides; or an AOV shift from variation mix | **PROVISIONAL** — no credit, no blame | no change [SR, PB] |
| 6 | **< 15 fresh clicks** since the action was executed | **TOO_SOON** | no change [SR, WB] |
| 7 | Primary metric moved (current − baseline = Δ) | Δ ≤ −3 → **WORKED**; Δ ≥ +3 → **BACKFIRED**; else **FLAT**; metric missing → TOO_SOON | WORKED → 0; FLAT/BACKFIRED → +1 [SR] |

- **Primary metric:** the logged prediction's metric. Default: organic rank for Ranking / Re-Ranking (±3 places; lower number = better), ACoS for every other objective (±3 points). [SR]
- Other objectives graded on their own metric when the prediction names it — Defensive: share held per branded query; Discovery: converting terms per $100 / graduation; Conquest: CPA + share of target page; Market Share: impression-share band. Tolerance = the one stated in the prediction (no source default). [PB, OC]
- **Fresh clicks** means clicks since execution, not the cycle total (the SR code counts the cycle total — a known defect). [SR defect]
- Promotional/lever reads (price, coupon, deal-depth levers): read at **day 7 and day 14**; actual uplift **< 50% of predicted → replace the lever, don't extend it**. [LTSF]

---

## 6. Escalation loop

| Step | Rule |
|---|---|
| Count | FLAT or BACKFIRED → consecutive +1; WORKED → reset to 0; TOO_SOON / DEAL_WINDOW / CONFOUNDED / PROVISIONAL / NOT_EXECUTED / PARTIAL → no change [SR] |
| Escalate | **2 consecutive** FLAT/BACKFIRED → Escalate = true, loop status ESCALATED. The row is **held and referred** (decision REVIEW) — the formula does not move it again [SR] |
| Manager acts | Manager response captured → MANAGER_ACTED: record action, lever, date, baseline ACoS + rank; verdict this cycle TOO_SOON [SR] |
| Grade the manager's action | next cycle, same grading order: WORKED → **RECOVERED** (counter 0, escalate off); FLAT/BACKFIRED → **MANAGER_INEFFECTIVE** (stays escalated; **structural review**: listing, offer, inventory, objective) [SR] |
| Re-diagnose | the **same verdict for 4 consecutive cycles** without its predicted effect = diagnosis error → re-diagnose the row from Phase 0 inputs, not the lever [PB, WB] |
| Dead lever | **never repeat a failed lever a 3rd time.** After two failed grades on a lever the next move is a different lever (adjacent in the hierarchy) or escalation, and the reasoning names the lever that failed [SR] |

Related persistence rules: ranking State B (clicks over plan, rank flat) **4 consecutive flat reads → STOP-LOSS** (concede or defer, reallocate); State F (delivery 95–120% of plan) 4 cycles → escalate. [PB]

Why two thresholds: 2 failures says the lever is exhausted; 4 identical verdicts says the diagnosis behind every lever is wrong. [Register #25]

---

## 7. Marginal read and freeze

On every **EXECUTED raise**, compute from baseline → current deltas:
- **Marginal CPC** = ΔSpend ÷ ΔClicks; **marginal ACoS** = ΔSpend ÷ ΔSales. [SR]
- Marginal ACoS **> 1.5 × average ACoS** → saturation: **FREEZE** at the prior rung; record Freeze/Floor bid + date in the ledger. [SR]
- Marginal ACoS **> 2 × blended ACoS** → unwind the step. [PB]
- A **BACKFIRED raise** also records Freeze/Floor bid + date. [SR]
- Record every floor found by a taper or ladder too (sufficiency taper, defensive ladder, incrementality ladder). "Every unrecorded floor is paid for twice." [SR, PB]
- Never credit a step that was capped (e.g. top-of-search boost at 900%) with new clicks. [B6 R-M2]

---

## 8. Refinement: grading a prior plan

1. Read the whole prior plan; classify each decision **stated / gap / stale**; collect data only for gap and stale items. [PB]
2. **Before any new decision**, grade every prior actioned keyword against **its own prediction and reversal condition**: worked / flat / backfired / too soon (plus the execution and window verdicts above). Show the grade in a scoring table **and** in that keyword's reasoning. [PB]
3. Forward-only: never silently rewrite a prior decision; changes go in a change log. [PB, WB]
4. Reviewer marks and owner overrides from prior rounds persist; a regeneration that reverts one fails the gate. [PB]
5. A finding whose evidence was overturned moves to the withdrawn-findings register with the overturning evidence; it is not carried forward. [DR]
6. Plan and companion workbook headline figures (roster counts, budget totals, goal, sufficiency status, TACoS) must reconcile; record any difference. [PB]
7. The weekly audit opens with a prior-week action review: was it executed, what happened. [QA]

---

## 9. Prediction format

Written **before money moves**, on every actioned row. [PB]

| Element | Content | Example (B6) |
|---|---|---|
| Metric | the one number that should move | organic rank on "bamboo sheets queen size" |
| Direction | up / down / hold | down (better) |
| Magnitude | size of the move, with tolerance | ≥ 3 places (default tolerance) |
| Horizon | date or cycle count | by the 12 Oct weekly tune (settled read) |
| Basis | HIST (this SKU/sibling measured) / MARKET (competitor ceiling) / TEST (pre-registered) — untagged predictions block scenario ranking | HIST: last push step moved rank 4 places |
| Review date | the checkpoint in the validation plan | 12 Oct |
[PB, LTSF, SR]

Rules:
- Ranges, not false precision ("~38–42%"); label directional estimates. [AP]
- Any soft coefficient (uplift multiplier, click elasticity) is named as soft, with when and how it will be measured. [PB]
- Forecast credit for a price step is capped by what steps of that size bought before; paused keywords and retags get zero credit. [B6 F20]
- Click/volume requirements set volume and budget only, never price; reconcile their sum to what the product sells. [B6 F21]

---

## 10. Reversal conditions

Every action carries one: **metric + threshold + window + what happens**. Standard conditions:

| Action | Reverses when | Then |
|---|---|---|
| PUSH step | top-of-search share < 30% and not top-3 sponsored most hours | next +30% step, never above ceiling [B6 R-P4] |
| PUSH at ceiling | 3 days at ceiling without holding the top | owner: time-boxed ceiling raise, or swap the term [B6 R-P6] |
| PUSH (any) | TOS CVR below market on 50+ clicks | stop the push; back to break-even [B6 R-P7] |
| PUSH (weekly) | held the top a week with no rank movement | check listing, stock, conversion; swap [B6 R-P7] |
| HOLD RANK | rank slips past target | rejoin the push [B6 R-P8] |
| Sufficiency taper | slip > 2 places on a top-5 term, or any slip below target elsewhere | restore last step = recorded floor [PB] |
| Incrementality step (−15%) | total orders fall > 10% | restore, record floor [PB] |
| BREAK-EVEN step-down | rank falls > 10 places | restore one step [B6 R-B2] |
| Non-ranking CUT | orders fall > 30% on the settled read | restore half the cut [B6 R-N1] |
| MIX FIX | product pages still > 20% of clicks after 7 days | cut base again [B6 R-M1] |
| HARVEST exact | ACoS > break-even on ≥ 15 clicks, 14 days after launch | bid down [B6 R-K4] |
| BLOCK | spend on the blocked term not ≈ 0 after 14 days | check where the negative sits [B6 R-K2] |
| BLOCK on a contested term (≥ 10,000 market traffic, ≥ 5 rivals) | 30 days pass, or listing/price changes | re-test in discovery at break-even [B6 R-CI9] |
| Defensive above-ceiling allowance | no competitor/non-brand presence for 2 consecutive reads | withdraw; price at plain break-even [PB] |
| Conquest target | CPA > watch-CPA for 2 consecutive reads with no page-share gain; target loses 2-of-3 | exit or rotate [PB] |
| SBV arbitrage | SBV CPC > 0.8 × SP exact CPC, or completion rate fades 2 consecutive weeks | exit [PB] |
| Yellow/Red hold | restock date reached | resume named keywords at named target ranks (dated re-entry plan) [PB] |
| Formula-only price correction | fails either test: converts once clicked AND gets clicks at all | suppression check next cycle [PB] |
| Fixed-bid trial | judged at 15 clicks (multi-keyword: 7–8 day review) | keep fixed, or revert [PB] |
| Re-enable inside an event | CPA > ceiling for 7 days | pause again [DR] |
| Competitor price move (> 15% cut, new discount, traffic > +50%) | — | hold our price 3 days; don't read the conversion drop as a bid problem; over-ceiling cuts still apply [B6 R-CI11] |

---

## 11. Validation plan template and standard checkpoints

Template (one row per checkpoint; lives in the workbook "Validation plan" tab and the document's next-steps section):

| When | What | Metric | Pass | Fallback | Rule |
|---|---|---|---|---|---|

Standard set — include every row that applies to the product; replace bracketed values with the product's own. Rule IDs go in the workbook only, never in narrative text.

| When | What | Metric | Pass | Fallback | Rule |
|---|---|---|---|---|---|
| Daily through the push window | Push terms | TOS impression share; sponsored rank | ≥ 30% share and top-3 most hours | +30% price step, never above ceiling | [B6 R-P4] |
| Day 3 at ceiling | Push terms at ceiling | holding the top? | holding | owner: time-boxed ceiling raise, or swap | [B6 R-P6] |
| Daily | Product total ad spend | spend vs limit | ≤ limit (event exceptions dated) | lower push budgets from the bottom of the funded list | [B6 R-F5] |
| Weekly | Product | margin after ads vs owner rule | at or above rule | cut the push from the bottom of the list | [B6 R-F6] |
| Daily | Product | spend pace vs day-of-week curve | within ±25% | flag same day | [PB] |
| Daily until +7 days after an event | Head terms | organic rank | no term down > 10 places | find the cause before any price change | [B6 E4] |
| Daily | Stock (hero of each pushed size) | available cover (30-day pace) vs days to next dated arrival | cover ≥ days to arrival + 7 (push allowed) | cover ≥ arrival but < +7: no further push steps; short ≤ 7 days: ease, no swap; short > 7 days: switch to backup colour, same size | [B6 R-I2/R-I3/R-I4] |
| Each checkpoint of a push | Projected DOC (stock + dated inbound at baseline burn + order gap) | days of cover | ≥ 60 (Green) through the checkpoint | block, shrink or time-box the push; wait for inbound | [WB, PB, register #42] |
| Day after an event ends | Post-event audit | price back to regular; margin at full price | — | re-price every ceiling on full-price margin; taper event bids over 3–5 days | [B6, SR] |
| 7 days after each mix fix | Mix-fixed campaigns | product-page share of clicks | ≤ 20% | cut the base again | [B6 R-M1] |
| First settled week (7 clean days after attribution settle) | Break-even step-downs | ACoS, orders, rank | ACoS toward break-even; rank not down > 10 | restore one step | [B6 R-B2] |
| First settled week | Non-ranking cuts | ACoS, orders | orders within −30% | restore half the cut | [B6 R-N1] |
| Weekly push tune | Push plan | rank movement per term | moving (≥ 5 rivals at SP #1–5: judge after 7 days, not 3) | held top a week without moving → check listing, stock, conversion; swap | [B6 R-P7, R-CI5] |
| Any time, ≥ 50 TOS clicks | Push terms | TOS CVR vs market | ≥ market | stop the push | [B6 R-P7] |
| 14 days at ceiling, stretch target | Terms whose target is held only by aspirational rivals | rivals passed | ≥ 1 rival passed (first milestone) | owner decision | [B6 R-CI2] |
| 2 consecutive clean weeks at target | At-target terms | rank vs target | held | begin taper ~10%/week to floor 5–10¢ under blended CPC | [PB, B6 R-P8] |
| 14 days after harvest launch | Harvested exacts | ACoS on ≥ 15 clicks | ≤ break-even | bid down | [B6 R-K4] |
| 14 days after block | Blocked terms | spend on the term | ≈ 0 | check the negative's placement | [B6 R-K2] |
| Dated goal checkpoint | Product goal | e.g. top 10 on half the push terms | met | re-plan in the weekly tune | [B6] |
| Every event on the calendar | Events | no judgement on event days | — | size the push (price, clicks, budget, stock) ≥ 1 week ahead (major events ≥ 3 weeks); reads skip event days | [B6 E1, PB] |
| Day 7 and day 14 of a price/promo lever | Lever | actual vs predicted uplift | ≥ 50% of prediction | replace the lever | [LTSF] |
| Daily during an SB/video test | Banners | impressions; bid vs ceiling | showing on each term | +30% bid step, never above the SB ceiling (2 × break-even on push terms and on brand terms with verified rival presence; 1 × elsewhere) | [B6 R-CI10, register #45] |
| End of SB/video test (≥ 15 clicks) | SB/video campaigns | ACoS; same-term SP orders + TOS CVR; organic rank; new-to-brand share | ACoS ≤ break-even; SP orders not down | BE–2×BE: hold at break-even bid; > 2×BE: stop; SP orders fall more than SB adds: stop | [B6 R-CI10] |
| Next competitor export after a brand-defence change | Brand terms | rivals' share of the brand term | below the baseline share | keep brand exact funded; review | [B6 R-CI6] |
| Next cycle | Every logged action | execution status | EXECUTED | re-issue; report execution rate | [SR] |

Example (B6): push window daily 29 Sep–14 Oct; spend limit $1,300/day on deal days; head-term rank daily to 7 Oct; post-deal audit 1 Oct re-pricing on the $18.81 full-price margin; settled reads 8–14 Oct; weekly tunes 5, 12, 19 Oct; goal "top 10 on half the push terms" by 19 Oct; deal days 15 Oct and 22–28 Oct excluded; SB/video test read 14 Oct; brand-defence pass = rivals' share of "decolure bamboo sheets" below 48%.

---

## 12. Read-window rules

1. **Evidence vs context:** current 7 days vs prior 7 days is the evidence a live action is judged on; 60–90 days is baseline, sample and trend context only. [PB, WB]
2. **Attribution settle:** SP credits orders up to 7 days after the click (SB/SD reports use a longer window, up to 14 days). A window whose end falls inside the attribution period reads low — compare settled windows only. [B6 E2]
3. **Deal/event exclusion:** no ACoS/CVR/rank verdict on event days; for **2 weeks** after an event closes, event-week rates stay out of trend reads; floors, ladders and ceilings resume pre-event values after the guard unless the event produced real evidence (e.g. sustained higher rank). [SR, PB]
4. **Settled read:** 7 clean days that start after the attribution settle following the event. Example (B6): deal ended 30 Sep → watch-don't-judge 1–7 Oct → first clean read 8–14 Oct. [B6]
5. **Deal state is separate:** deal-state margin, CVR baseline and rank arc are kept apart from clean-state; the clean arc governs. [PB]
6. **Windows never straddle a lever change.** A read that crosses a change of lever, price or advertised SKU is CONFOUNDED; use the post-change portion only if it has ≥ 15 clicks. [LTSF, PB]
7. **Two levers in one window = confounded.** Stage changes so each lever gets its own window. [LTSF]
8. **Rank trends:** ≥ 1 month of history (ideally 3); state overall, 14-day and 7-day separately (shorter = early warning); exclude stockout/re-route stretches; median over the window with unranked days counted as unranked, not as a rank. [PB, B6]
9. **Non-ranking judgement** uses 30-day and 90-day windows together; over on 30 but inside on 90 → MONITOR (no change, named re-read date). [B6 R-N1]
10. **Velocity windows:** 30-day pace for cover; 7-day pace as a warning only; never the inflated push pace; distorted windows (stockout, suppression, deal) are corrected with a stated factor. [B6, LTSF]
11. **Economics freshness:** margin older than 45 days, or any price/fee/packaging/LTSF change, makes grades PROVISIONAL and ceilings stale until refreshed (within 48 h). [SR, PB]
12. **Budget-truncated windows** (in-budget < 70% of the day) are not evidence for bids; 0% in-budget with $0 spend = missing data. [PB]

---

## 13. What to surface every cycle

Verdict counts (by verdict), escalations opened / resolved (RECOVERED) / ineffective, execution rate and the NOT_EXECUTED list being re-issued, PROVISIONAL grades with the economics event behind them, freezes/floors recorded, rows re-diagnosed after 4 cycles, and the validation plan's next three dates. [SR, PB]

---

## 14. Open questions for the owner

1. Marginal read: Resolved — see 13 #34: freeze at the prior rung when marginal ACoS > 1.5 × average; unwind one step when > 2 × blended (freeze first, unwind second).
2. No source sets an execution tolerance for placement %, budget or state changes; exact match is used here. Confirm or set one.
3. No source sets a grading tolerance for defence share, discovery graduation, conquest page share or market-share band. Set per product when the prediction is written, or give house defaults.
