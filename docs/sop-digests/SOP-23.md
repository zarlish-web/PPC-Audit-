# SOP-23 Digest: Ranking-Push Operations

Source: `PPC_SOP_23_Ranking_Push_Operations_v2_0.pdf` (16 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-23: Ranking-Push Operations (Component #23 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead |
| Supersedes | SOP-23 v1.0 (2026-07-24) in full |
| Thresholds | All in Master PPC Decision Criteria System v4.0; zero local thresholds. Verdict strings are quoted verbatim from the KDR Template v3.0 Bands and Verdicts Reference, with the v4.0 Section 13.1 cross-map where they diverge |

**Verdict / purpose.** A ranking push is spend that carries **five properties at once**. Spend moving toward rank without all five is not a slow push. It is an **unpriced subsidy** that pays full auction cost for no governed outcome.

| Property | Means |
|---|---|
| Sized | A complete M2 block |
| Dated | A horizon date and an ETA checkpoint |
| Ceilinged | A weekly loss ceiling, computed not estimated |
| Predicted | A V1 prediction with metric, direction, magnitude, horizon |
| Funded | An M5 queue release |

This SOP owns the arithmetic that produces those five, plus the operating cadence from candidacy to post-mortem. It does not own campaign mechanics, queue law, ladder mechanics, recovery or event overlays.

v2.0 changes from v1.0 (which was built to the superseded 10-element standard and measured 4 pages against a 10-18 page bar):
- procedures 7 to 13
- failure modes 7 to 13
- worked examples 1 to 4
- adds Elements 11 and 12, which exist in none of the 23 shipped SOPs
- retires 3 v1.0 verdict strings: bare CONTINUE, DIAGNOSIS BEFORE MONEY, bare TAPER
- carries forward the E3 sizing anchors and all 7 v1.0 incidents, now sourced

### 1.1 The five properties as tests
A row failing any test is not a push and falls under **S-R11** (8.4; CPC above 1.5x ceiling with no sized push and no M2 record), which returns an immediate ladder toward ceiling, not a smaller push.

| Property | Test (T2 / T6 / T0 fields) | Source |
|---|---|---|
| Sized | T2 **DSTR (orders/day)**, **Required Clicks/Day**, **Required Budget $/wk** all populated from the same worksheet version | **M2**: every push carries target rank, required clicks vs actual, budget, ceiling, ETA checkpoint, stop-loss |
| Dated | T2 **Target Rank**, **ETA Checkpoint**, **Review Date** carry dates | **O7**: every Ranking objective has a horizon date and renews only on evidence |
| Ceilinged | T2 **Loss Ceiling $/wk** = (ACOS above break-even) x projected sales, dated | M2 loss-ceiling clause |
| Predicted | T6 row with **Expected Outcome Window** and **Review Date** | **V1**: unscored actions do not accumulate |
| Funded | Term in **T0 zone H** as **FUNDED** with a dated release | **M5**: order = revenue potential at target rank / cost-to-close-gap |

### 1.2 Three candidacy classes (assigned before sizing; rule D10)
| Class | Condition (F6 best-rank row) | Consequence |
|---|---|---|
| Cold | NEVER-RANKED: no best rank ≤10 in trailing 12 months and no pre-OOS baseline ≤10 | Full O3 gauntlet, no history credit; sized on assumption; P13 calibration more valuable |
| Recovery | Best rank ≤10 within trailing 12 months, or pre-OOS baseline ≤10. **PROVEN** where that rank ≤5 | Inherits a proven ceiling, skips the cold-start realism penalty, funds at better M5 priority. The recovery push belongs to **SOP-24** (this SOP classifies and hands over at P2 step 6) |
| Structure-blocked | Priority term **≥500 SV** on a primary syntax with **zero exact campaigns**, or auto+broad carrying **>40%** of its clicks (**X10**) | **S-R12** bars any performance verdict until the exact stands up; deferred (re-enters at P1 after G2 sufficiency) |

### 1.3 Why the sizing is the document
The account's standing failure is spend that reaches break-even and keeps going with no arithmetic attached. **F16** records the case: **one term absorbing roughly a quarter of a product's ad clicks above break-even** with no plan. At **$6,000-8,000 per day of account spend**, **R1** puts a 2x stage-band breach at a four-figure daily leak. P3 turns that pattern into either a funded decision or a bid-down verdict, with nothing in between. Strategic Doctrine v1.0 Section 1 third principle: economics set ceilings, never targets; margin dollars rather than margin percent size every push.

## 2. Scope and boundaries
Per the Ledger, this component owns: push sizing math, DSTR and required clicks, daily pacing on funded pushes, taper trigger execution, and the push precondition block.

| Excluded decision | Owner | Seam |
|---|---|---|
| Every threshold, band, scenario, verdict | v4.0 | A number not quoting v4.0 is a defect; gaps go to Section 13 |
| Campaign creation, bid/budget edits, campaign-level taper execution | SOP-12 | This SOP issues the standup order and taper trigger; SOP-12 P1 creates, P4 executes. A bid value written by this SOP is a defect |
| Queue ranking, envelope law, budget release/return | #31 | This SOP submits a sized worksheet and receives a dated release; never ranks or moves budget. Conflict **C3**: #31 has no procedural document, so cite **T0 zone H, Account Rollup A2** |
| Ladder step derivation, exit-bid discovery, modifier sizing, ceiling worksheet | #28 | This SOP releases the taper trigger at P10 and stops. #28 is the authoritative ladder for SOPs 12, 23, 24, 25, 26 |
| Loss diagnosis, baseline restoration, recovery sizing, OOS overlays | SOP-24 | SOP-24 extends this document. A held-then-lost rank belongs to SOP-24 from the moment the loss is dated |
| Event plans, caps, arming, hangover routing | #32 | Windows amplify live pushes, never originate them; this SOP suspends/resumes at P12 |
| Family term ownership declaration and guard | #33 | The push block is a SOP-23 precondition; this SOP holds candidacy until the declaration lands |
| Post-objective normalization after taper | SOP-25 | The taper exits into SOP-25 |
| Negation walls at every structure event | #29 | Built the same session as the standup |
| Staging, upload, T+1 | #38 | No console edit outside the staged set |
| Terminal / LTSF-tiered units | #27 | Conflict **C6**: the deciding document is outside the corpus. CONSTRAINED earning-potential class bars pushes outright (**S-A10**) |

## 3. Triggers
| Trigger | Detecting artifact / observable | Max lag | Procedure |
|---|---|---|---|
| Candidacy scan | T2 Keyword Command, **OVERSIGHT filter**: Organic Rank worse than Target Rank, Objective = Ranking or blank | One weekly cycle (V4) | P1 |
| Funding release | T0 zone H M5 push queue entry → FUNDED with dated release | Not stated in v4.0 (AM-6) | P6 |
| Daily in-flight | T2 child rows for Objective = Ranking campaigns with a live M2 block, vs T2 In-Budget % and the daily rank series | Same day (V4) | P7 |
| Weekly in-flight | Monday cascade reaches T2 with a live push row | One weekly cycle | P8 |
| Velocity stall | T2 **Velocity (pos/wk)** in the FLAT band across the review window with **Actual Clicks/Day ≥ Required Clicks/Day** | Review window closes at the ETA horizon, **default 3 weeks** (F6) | P9 |
| Early ETA warning | T2 **ETA to Target (wks)** crossing into BEYOND | Same weekly read | P8 |
| Target touched | T2 Organic Rank ≤ Target Rank on the daily series | Same weekly read; stability window starts at the touch date | P10 |
| Stability confirmed | Organic Rank ≤ Target Rank for **2 consecutive weeks** (**S-R6**) | Same weekly read | P10 |
| Horizon reached | T2 ETA Checkpoint date arrives with target not held | Same weekly read (O7 bars auto-continuation) | P11 |
| Inventory band flip | T2 Inventory Band YELLOW/RED on the targeted variation, or **Days to Stockout ≤14** | Same day on RED (**S-I3**); YELLOW freezes at current spend, no same-day clause | P12 |
| Family conflict | T2 **Family Conflict** live, or **Sibling CPC View** showing a second sibling with a push objective | Not stated (G11; AM-7) | P12 |
| Product posture flip | T0 zone A verdict banner: push freeze or code red (**S-A3, S-A4**) | Same cycle on S-A3; S-A4 = Recovery Mode, daily cadence (**R4**) | P12 |
| Event window armed | T2 **Event Mode** PRE-EVENT or IN-EVENT from the #32 plan | Arming is T-1 per #32 | P12 |
| Push close | Any exit: target held, stop-loss, concession, candidacy withdrawn | Not stated (AM-8) | P13 |

## 3b. Preconditions and gates
**Live manifest state (account-specific).** The T7 Manifest in the current Command Workbook template reads **packet completeness 0.571**, below the 85% DEGRADED floor (**G8**). Four groups this SOP depends on are not fully present:
- **D8 competitor depth: MISSING** (degrades DSTR, which **F14** defines as set by competitor velocity analysis)
- **D9 daily rank series: PARTIAL**, head terms only (T7 names it as blocking push-window daily verification)
- **A6 objective and per-term Expected CPC: PARTIAL**, with an **account reference of $2.80** in use
- **D1 per-variation margin: PARTIAL**, which puts the G9 PROVISIONAL tag on every ceiling

| Manifest ID | Gate | Requirement | Observable |
|---|---|---|---|
| A4, A5 | G1 | No impossible metric (CVR 0 with orders, ACOS without orders, cross-table disagreement) | T2 **Flag: Zero-Quarantine** clear; **Validation State** not QUARANTINE. Quarantined → flag + data-refresh task, never a push |
| A4, A1 | G2 | **≥15 clicks/7d** bid read; **≥100 clicks** for the sizing CVR | T2 **Clicks 7/30/60d**, **Sample State**. <100 → 60-day fallback; still thin → EXTEND TEST, no push. **A1 reads MISSING** (no four-period trend context) |
| A3 | G3 | Not budget-truncated; in-budget **<70%** → TRUNCATED, budget lever first | T2 **In-Budget % ≥70**. KDR Bands labels 51-70 "strained"; G3's 70% governs. **A3 PARTIAL** (day-of-week curve unavailable) |
| A7 | G4 | Eligible and unsuppressed | T2 **Eligibility**; a flip halts the same day and opens a listing task |
| B1 | G5 | Indexed; on a rank objective placed in title or bullets | T2 **Indexed?** yes; **Listing Placement** title/bullets; backend-only → listing queue |
| D1, D2 | G6 | GREEN. YELLOW freezes push spend; RED tapers to defense and re-points same day | T2 **Inventory Band**, **Days to Stockout**, **Targeted Variation(s)**. GREEN = days on hand **> lead time + 21 days at max-sales-day velocity**. **D2 PARTIAL** (backup chain on head terms only) |
| A3 | G7 | Budgets reconcile to the envelope; product pacing **within 25%** of the day-of-week curve | T2 **Envelope Status**, T0 zone H available dollars. Not fitting the envelope = a queue decision at #31 |
| All | G8 | Manifest reports before analysis; **<85%** = DEGRADED, flags only | T7 Status column and completeness rollup on the cycle header (live **0.571**) |
| D1 | G9 | Price stability: no price change in **trailing 7 days**, else PROVISIONAL and no conversion verdict | T5 **Event Type** = price move vs T2 **Margin $/Unit**. Corpus alias: SOP-12 v2.0, SOP-14, SOP-30, Data Architecture use G9 for margin freshness; both states checked |
| D7 | G10 | Event weeks + **14 days** excluded from trend reads that size a push | T5 **Trend-Exclusion Flag**, T2 **Event Mode**. Corpus uses G10 for objective tagging and G12 for event freeze |
| D6 | G11 | No second sibling with an active push objective on the term | T2 **Family Conflict**, **Term Owner (Family)** from Account Rollup A1. **D6 PARTIAL**; **Bamboo root ownership left OPEN at cycle 1** (a live instance) |
| B11 | G12 | Term in the current MKL with syntax tag and relevancy; MKL not stale **>30 days** | T2 **Syntax Tags**, **Relevancy** (corpus uses G12 for event freeze) |
| B8, D1 | Economics chain | T0 zone C live: AOV, contribution/order, BE ACOS, Target ACOS, Max Acceptable, Expected CPC | Zone C margin table version and fresh/provisional state. **B8 PRESENT on blended margin; D1 PARTIAL** → every ceiling PROVISIONAL. External dependency **D1** (Ledger), open, caps this component by name |
| B3, D9 | Rank pack | Best rank with date, pre-OOS baseline, velocity, ETA, daily rank series | T2 **Best Rank (Hist) + Date**, **Pre-OOS Baseline**, **Velocity (pos/wk)**, **ETA to Target (wks)**. Both PARTIAL, head terms only. Outside coverage → cannot class at P2.1, does not proceed |
| B7 | Placement splits | Placement-level splits for the hosting campaign | T4 Placement and Bid rows with values. **B7 MISSING account-wide** → suppresses modifier increases at #28; S-R7 partially unexecutable (WE-2) |

## 4. Procedures

### P1. Candidacy assembly (weekly in Monday cascade; 25-40 min/product at ~100 oversight-class terms)
1. Open T2 Keyword Command; confirm T0 and T1 were read first (otherwise invalid).
2. Score last cycle first: T6 filtered to Review Date this cycle; write V5 Score (**HIT, PARTIAL, MISS, WRONG-DIRECTION**).
3. OVERSIGHT filter, then rows with Organic Rank worse than Target Rank. Blank Target Rank at **≥500 SV** = unmanaged (**O1**) → target-setting, not candidacy.
4. Drop rows below the SV floor: **O2** sets the ranking floor **above 500 SV**.
5. Drop rows whose **Syntax Priority** is secondary where the syntax is already at its spend-share cap (**P4**: syntax caps above single-keyword strength; a cap never rises mid-cycle).
6. Check **Seasonal SV Index Dir**. **T4** times pushes into a rising index and never after the peak; a falling index = defer with a dated re-entry.
7. Run every Section 3 precondition and record failures. A failure is the work item, never a reason for a smaller push or a bid change.
8. Write survivors into T2 **Situation** with the cycle date → P2. Queue entry without P2+P3 = F1.

### P2. O3 ranking-realism gauntlet (8-12 min/candidate; every clause must pass; rule O3)
1. **Class** from Best Rank (Hist) + Date and Pre-OOS Baseline: ≤10 in 12 months or baseline ≤10 → RECOVERY; ≤5 → PROVEN; else NEVER-RANKED. No B3/D9 coverage → stop and record the gap.
2. **Indexing and placement** (G5), recorded.
3. **Intent**: T2 **Intent Type** = purchase. Research/comparison intent belongs on cheaper surfaces (**F14** named error).
4. **Conversion**: T2 **Brand CVR ≥ Market CVR**, with **Benchmark Source** recorded. Broken SQP row → fallback file reference target, then account norm; fallback lowers confidence and routes to the human queue.
5. **Competitor credibility**:
   - **Review Position Gap** not FAR-BEHIND (**F4**: <50% of top-5 median review count, or ≥0.3 stars below it).
   - **Price Position Index** not OUTPRICED (**F5**: >1.25 = our price / median market price paid).
   - BEHIND allows pushes on long-tail and mid-volume terms only while review velocity closes the gap.
   - With D8 MISSING, this clause is evidenced on T2 **Competitor Best Rank** and **Price Competitiveness Flag** where present, else flagged unevidenced.
6. **Inventory**: G6 GREEN; YELLOW/RED → **S-I2/S-I3** at P12.
7. **THIN-margin clause**: T2 **Margin $/Unit**. **<$6/unit = THIN**, and O3 requires **Expected CPC ≤ margin $ / 3**. Compute, write both, decline on failure.
8. **Cost-to-close vs revenue potential**: carried forward to P5.
9. Any failure closes candidacy with the clause named in Situation; Objective → **Paused-pending** with blocking reason and re-entry criterion.

### P3. The sizing worksheet (15-20 min; rule M2, chain in F14)
1. Seven inputs into T2: Organic Rank, Target Rank, DSTR at target rank, validated CVR, Expected CPC $, contribution/order (T0 zone C), current daily orders (organic+paid). All read, never estimated.
2. **DSTR**: competitor velocity analysis at target rank (F14), sized from market purchases. D8 MISSING → unevidenced flag.
3. **Order gap = DSTR − current daily orders.**
4. **Required clicks/day = order gap / expected CVR** → Required Clicks/Day. With **≥8 weeks** of push history, correct by the term's observed **Rank Response Elasticity** (M2 amendment). Below 8 weeks unavailable; state so.
5. **Required spend/day = required clicks x Expected CPC**; weekly → Required Budget $/wk. No per-term Expected CPC (A6) → the account reference is written in as the assumption under test.
6. **Duration = rank distance / expected velocity** for the term class. v4.0 bands velocity only in positions/week, with no per-class cold-push reference: record the velocity assumption as an input under test (**AM-4**).
7. **Total push budget = required spend/day x duration.**
8. **Loss ceiling**:
   - push ACOS = required spend/day / projected daily sales
   - minus BE ACOS (T0 zone C)
   - times projected weekly sales

   → **Loss Ceiling $/wk** with date. No v4.0 scenario fires on the ceiling being reached (S-R5 fires on velocity), see AM-1.
9. **State what the worksheet could not see** in T2 Situation: D1 provisional margin, unevidenced DSTR (D8), account-reference Expected CPC (A6), absent elasticity correction. Required by G8; confidence theater violates **J7** (13.3).
10. **Ceiling read**: Max Profitable CPC = contribution x CVR; ratio = Expected CPC / Max Profitable CPC.
    - **≤0.8 SAFE**
    - **0.8-1.0 AT-CEILING**
    - **1.0-1.5 PUSH-ONLY**
    - **>1.5 UNJUSTIFIABLE** outside a sized push

    Above 1.5 inside a sized push, **S-R10** makes the cheap-surface arbitrage check mandatory: where **video CPC ≤0.6x SP exact CPC**, that surface enters for TOS presence and the SP exact steps down one rung. The check is recorded whether or not it fires.
11. **Prediction**: rank X to Y by the dated horizon, with the ETA checkpoint date, written before money moves.
12. **Version the worksheet** into the T2 plan block; later decisions cite the version.

### P4. Confidence scoring and step modulation (4-6 min; rules M10, D9)
1. Score from 3 drivers (sample size, benchmark source tier, manifest completeness). Bands: **≥75 HIGH, 50-74 MEDIUM, <50 LOW**.
2. LOW: **M10 bars pushes outright**, halves every lever and budget step, shortens review horizons to **1 week**. **D9**: only extend-test, data-repair and gate-driven verdicts are legal. Does not proceed to P5.
3. MEDIUM = standard steps; HIGH = upper end of step ranges permitted.
4. With T7 at 0.571 and benchmarks below the SQP tier, confidence is structurally depressed account-wide. This is a data problem with an owner, not a reason to relax.
5. Record the score and drivers on the Master Action Record.

### P5. Queue submission and funding decision (5-8 min)
1. M5 inputs: revenue potential at target rank / cost-to-close-gap → T2 **Cost to Close Gap $**.
2. Resolve the O3 clause from P2.8; unjustified → close with the concession logged.
3. Submit to the queue in T0 zone H. Ties break by margin-dollar class and earning-potential class (M5). This SOP does not rank.
4. Product posture:
   - **S-A2**: sign-off above the PPC Lead on new pushes while total ad-cost ratio reads ELEVATED.
   - **S-A3**: no new Ranking objectives during a push freeze.
   - **S-A4**: Recovery Mode; **R3** permits new Ranking objectives only on RECOVERY-class terms at HIGH confidence.
5. **S-A10**: CONSTRAINED earning-potential class bars ranking pushes; velocity needs route to deals/pricing.
6. On release, read the dated release → P6. No release = no push (spend without one = F1).

### P6. Execution standup (same day as release; 20-30 min; mechanics at SOP-12 P1)
1. Standup order to SOP-12 with five values only:
   - dedicated single-keyword exact structure
   - starting bid from the worksheet
   - **daily budget = required weekly budget / 7**
   - objective tag Ranking
   - horizon date

   A creation without a verdict-carried bid returns incomplete.
2. Bidding strategy **fixed** (Doctrine Section 6.3). The **April 2026 platform bidding change** weights placement-level conversion probability more aggressively, with category CPC inflation reported at **18-27% vs Q1 baselines** under dynamic raises.
3. Placement modifiers at **zero** on all three groups unless #28 placement evidence exists (B7 MISSING suppresses increases).
4. Walls built the same session under #29 (otherwise the same click is bought twice).
5. **Log the taper trigger at standup** in T6: achievement condition, stability requirement reference, ladder handoff (Doctrine Section 14 names post-achievement spend as an account failure class).
6. T6 row: **Rule / Scenario Fired, Change (prior -> new), $ Impact / wk, Expected Outcome Window, Review Date, Owner / Tier**. Tier human-mandatory (**P5**: every 500+ SV action and every structural change).
7. Deploy via #38 with T+1. The push does not count as started until the diff proves it landed.

### P7. Daily in-flight block (daily, twice on deployment days; 6-10 min/push; V4)
1. Pacing: T2 In-Budget % and cumulative spend vs the worksheet daily line. <70% → G3 truncated; budget lever first; the week's bid read void.
2. Rank: daily rank series vs the assumed velocity line. Outside D9 coverage the resolution is weekly and P8 checkpoint arithmetic uses the coarser interval.
3. Loss line: cumulative spend − orders x contribution vs the dated weekly ceiling. Surface the number; the scenario call is made at P8.
4. Gate flips (eligibility, inventory band, event mode) → P12 the same day.
5. **No bid changes, ever**, in this procedure. Pacing touches budget only. Every intervention writes a T6 line.

### P8. Weekly in-flight read (12-18 min/push)
1. Gates before metrics; a failing gate executes its lever and defers the verdict (P1 precedence).
2. Five-element story line with numbers (**X1**): position, trajectory, economics, cause, plan. A missing element → **J2** rejects the record.
3. Placement before bids: T2 **TOS IS %** below the **30% floor** (F6) → **S-R7** fires, placement is fixed before any bid verdict. B7 MISSING → modifier half not executable; log a blocked verdict class.
4. **Rank triad** (**X4**): CVR vs benchmark, clicks/day vs required, rank velocity. 8 cells → 4 outcomes:

| CVR | Clicks | Velocity | Outcome |
|---|---|---|---|
| ≥ benchmark | short | flat | Traffic deficit → fund |
| ≥ benchmark | met | >0 | Working → continue |
| ≥ benchmark | met | ~0 across window | Over-competitive → stop-loss |
| < benchmark | any | any | Fix-first |

5. ETA (F6):
   - **WITHIN**: at or inside the review horizon (default 3 weeks)
   - **BEYOND**: past it; opens the stop-loss conversation early and pre-stages the P11 renewal decision
   - **NEVER**: velocity ≤0
6. Saturation on any scale step: **marginal ACOS >1.5x average ACOS** → freeze at the prior spend level and re-test in **2 weeks** (applies to budget, bid and modifier increases).
7. Loss line vs ceiling: record % consumed. When the ceiling is reached, no v4.0 scenario fires (AM-1): route to the human-mandatory tier with the arithmetic.
8. One verdict from Section 5, cite its scenario, stage per #38. No scenario ID = no deploy.

### P9. Stop-loss execution (on S-R5; 10-15 min)
1. Confirm all 3 S-R5 conditions:
   - sufficient clicks and budget consumed per plan
   - CVR ≥ benchmark
   - rank velocity ~0 across the review window, or observed elasticity ~0 after adequate volume

   Failing on clicks = traffic deficit, a different verdict.
2. Confirm the P8.3 placement check already ran (otherwise F4).
3. Issue **STOP-LOSS: CONCEDE OR DEFER**. The push objective ends; the term re-classes; budget returns to the envelope for M5 reallocation at #31.
4. **Concede** → Conversions at Max Profitable CPC (contribution x realized CVR); bid step via SOP-12. Lever limits: **≤50% per change, $0.50 floor**.
5. **Defer** → requires a new worksheet through the queue. No informal continuation, no reduced-rate version.
6. No v4.0 execution deadline or re-queue cool-down exists (AM-2, AM-9). v1.0 asserted same-day execution and immediate re-queue.
7. Write the concession to T6 with realized figures; run P13.

### P10. Achievement, stability and taper release (8-12 min each, at touch and at confirmation; S-R6, T1)
1. Target touched starts the stability measurement; record the touch date in T6. Touching is not achieving; holding is.
2. Stability = **2 consecutive weeks** at or under target (S-R6 and T1; the only stability figure in v4.0).
3. Hold levers still through the window (moving them voids the measurement). The freeze and its spend are not governed by v4.0 (AM-3). WE-1: **$1,545.60 spend and $604.80 expected loss** unsized.
4. On confirmation, issue **TAPER: RANK ACHIEVED, STEP BIDS DOWN** (the trigger logged at standup executes). A rank-achieved row still at push-level spend = F6, the account's most expensive known failure class.
5. Hand off to SOP-12 P4 and the #28 ladder: achievement date, push bid, worksheet reference. No rung, step size or floor from this SOP.
6. Retag Ranking → post-objective state per T1. Tag and campaign-name objective segment update in the same staged set.
7. Run P13.

### P11. Horizon renewal decision (on horizon date; 15-20 min; O7, S-R16)
1. Confirm the horizon arrived and the target is not held. Objectives do not persist by inertia.
2. Read realized velocity across the whole push, plus realized CVR and cost vs assumptions.
3. Re-size:
   - remaining distance / realized velocity = remaining days
   - remaining days x required spend/day = remaining cost to close

   With ≥8 weeks of history, the elasticity correction applies. Below 8 weeks, realized velocity is this SOP's stated method (AM-5).
4. Apply M5 to the re-sized figure: compare re-sized cost-to-close per position vs the funding-time figure. Renewal is legal only if it still clears M5 against the current queue.
5. Clears → renew with a new horizon and a new worksheet version. Fails → Conversions at ceiling, concession logged.
6. T6 row with the arithmetic either way; a renewal without the re-sized number = F12.

### P12. Suspension and resumption on gate flips (same day; 10-20 min)
1. **YELLOW** (**S-I2**): freeze at current spend, no scale steps, review at the restock date.
2. **RED** (≤14 days to stockout): same day, taper to defense, re-point to the declared ranked backup, write the pre-OOS baseline snapshot (rank, CVR, CPC per keyword).
3. **Stockout despite taper** (**S-I4**): push objectives → Paused-pending with re-entry on restock confirmed; trend windows marked for exclusion. The push is closed; run P13.
4. **Family conflict** (G11): hold at current spend on both siblings until #33 assigns the lead.
5. **Product posture**:
   - **S-A3 push freeze**: an existing push continues only where velocity >0 AND loss is inside the ceiling (both tested and recorded).
   - **S-A4 code red**: Recovery Mode. **R3** tightens human confirmation to any bid move **>15%** and any budget move **>$25/day**, and caps step sizes at standard even at HIGH confidence.
6. **Event window**: the push continues, amplified per the #32 plan; in-window reads follow the plan's targets. G10 excludes the window + 14 days.
7. Every suspension/resumption writes a T6 row with the gate, flip date and resumption condition.

### P13. Post-mortem, scoring, calibration (every closed push; 20-30 min; V1, V5)
1. Score the standup prediction HIT/PARTIAL/MISS/WRONG-DIRECTION → T6 **V5 Score**.
2. Three separate calibration deltas: realized velocity vs assumed; realized CVR vs assumed; realized cost vs budget.
3. Name the single assumption that carried the error. If it is velocity, the finding attaches to AM-4.
4. Feed the realized **rank movement per 100 incremental clicks** into the elasticity series (corrects P3.4 at ≥8 weeks).
5. If a failure traces to a missing feed, attach the finding to that T7 row.
6. **V5 rule-level accuracy**: any rule **<50% accuracy over ≥10 scored predictions** enters review (amendment, threshold change, or documented defense).
7. A closed push without a post-mortem = F7.

## 5. Rules, thresholds and numbers

### v4.0 references
| ID | Meaning as described |
|---|---|
| M2 (Sec 10) | Every push carries target rank, required clicks vs actual, budget, ceiling, ETA checkpoint, stop-loss; loss ceiling = ACOS above BE x projected sales, capped and dated; elasticity correction at ≥8 weeks |
| M5 (Sec 10) | Order pushes by revenue potential at target rank / cost-to-close-gap; ties by margin-dollar class and earning-potential class |
| M10 (Sec 10) | Confidence bands ≥75 HIGH / 50-74 MED / <50 LOW; LOW bars pushes, halves steps, 1-week horizons |
| O1 | Blank target at ≥500 SV = unmanaged |
| O2 | Ranking floor above 500 SV |
| O3 | Ranking-realism gauntlet (indexing, intent, conversion, competitor credibility, inventory, THIN clause, cost-to-close) |
| O7 | Every Ranking objective carries a horizon date; renews only on evidence; no inertia |
| D9 | At LOW confidence only extend-test, data-repair, gate-driven verdicts |
| D10 | FAR/UNRANKED terms classed (recovery vs never-ranked) before objectives |
| F2 | A ranking-stage designation expires and must be renewed on rank evidence |
| F3 | Pre-OOS baseline |
| F4 | Review Position Gap FAR-BEHIND = <50% of top-5 median review count, or ≥0.3 stars below; listing-coverage rollup; syntaxes <60% coverage are listing projects |
| F5 | Price Position Index OUTPRICED >1.25 |
| F6 | Best-rank classes; velocity bands (FLAT etc., positions/week); ETA WITHIN/BEYOND/NEVER; default review horizon 3 weeks; TOS share floor 30% on ranking campaigns |
| F10 | Truncation as the step-zero precondition |
| F13 | Syntax-level version of rank spend renewing without movement |
| F14 | DSTR = competitor velocity analysis; paying purchase prices for research traffic is the named error |
| F16 | One term absorbing about a quarter of a product's clicks above BE with no plan |
| X1 | Five-element story line: position, trajectory, economics, cause, plan |
| X2 | Raising bids against adequate impression share buys more of the same rejection |
| X4 | Rank triad (8 cells → 4 outcomes) |
| X5 | Margin-dollar constraint (THIN case) |
| X6 | CPC ratio >1.5 across siblings fires structural inspection in fixed order |
| X10 | Auto+broad >40% of clicks |
| X12 | Incrementality mechanism |
| G1-G12 | As in the gates table (v4.0 numbering governs; corpus aliases noted) |
| P1 (Sec 12) | Gates > diagnosis > signals |
| P4 (Sec 12) | Syntax caps above single-keyword strength; no mid-cycle raise |
| P5 (Sec 12) | Every 500+ SV action and every structural change is human-mandatory |
| R1 | 2x stage-band breach = four-figure daily leak at $6-8k/day spend |
| R3 | Recovery Mode: new Ranking objectives only on RECOVERY at HIGH confidence; human confirm on bid >15%, budget >$25/day; steps capped at standard |
| R4 | Recovery Mode cadence daily |
| T1 | Post-objective transition at 2 weeks at/under target |
| T4 | Push into a rising seasonal index, never after the peak |
| J2 | Rejects an incomplete story line |
| J7 (13.3) | Confidence theater is a process violation |
| V1, V4, V5, V6, V8 | Predictions; cadence; scoring and rule accuracy (<50% over ≥10 → review); quarterly confidence calibration; training corpus |
| S-A2, S-A3, S-A4, S-A5, S-A10 (8.1) | ELEVATED sign-off; push freeze; code red/Recovery; incrementality; CONSTRAINED class bars pushes |
| S-B2 | Sibling scenario with PORTFOLIO CALL |
| S-D1 | Defend at floor |
| S-I2, S-I3, S-I4, S-I6 (8.3) | YELLOW freeze; RED taper and re-point; stockout pause; re-point |
| S-R1 | <15 clicks/7d, healthy budget, GREEN → bid steps 15-25% |
| S-R2 | Working push; utilization below 80% ranking target permits one budget step of 20-30% |
| S-R3 | Traffic deficit; re-check ETA in 2 weeks |
| S-R4 | Fix-first |
| S-R5 | Stop-loss on velocity ~0 with clicks met and CVR ≥ benchmark |
| S-R6 | 2 consecutive weeks at/under target → taper |
| S-R7 | TOS IS below 30% → placement fix first |
| S-R9 | Rank at target with CVR below benchmark → hold at minimum viable CPC |
| S-R10 | >1.5x ceiling inside a sized push → mandatory video arbitrage check (≤0.6x SP CPC) |
| S-R11 | CPC >1.5x ceiling with no sized push → ladder toward ceiling |
| S-R12 | Zero exacts / auto+broad >40% → no performance verdict |
| S-R13 | Recovery push routing |
| S-R15 | Pause (levers exhausted) |
| S-R16 | Horizon renewal requires the re-sized figure to clear M5 |
| S-Y9 | Stop-loss related scenario (listed with STOP-LOSS) |
| L-limits | ≤50% per change, $0.50 floor |

### Numbers
| Item | Value |
|---|---|
| Account spend | $6,000-8,000/day |
| Ranking SV floor | >500 SV |
| Recovery class | Best rank ≤10 in 12 months or pre-OOS ≤10; PROVEN ≤5 |
| Structure-blocked | ≥500 SV primary syntax, zero exacts, or auto+broad >40% |
| G2 | ≥15 clicks/7d; ≥100 clicks CVR; 60-day fallback |
| G3 | In-budget ≥70% (KDR 51-70 "strained") |
| G6 GREEN | Days on hand > lead time + 21 days at max-sales-day velocity; RED ≤14 days |
| G7 | Pacing within 25% of the day-of-week curve |
| G8 | DEGRADED <85%; live 0.571 |
| G9 | 7 days |
| G10 | Event + 14 days |
| G12 | MKL ≤30 days |
| THIN margin | <$6/unit; Expected CPC ≤ margin $/3 |
| Review gap FAR-BEHIND | <50% of top-5 median reviews or ≥0.3 stars below |
| OUTPRICED | PPI >1.25 |
| CPC ratio bands | ≤0.8 SAFE; 0.8-1.0 AT-CEILING; 1.0-1.5 PUSH-ONLY; >1.5 UNJUSTIFIABLE |
| SBV/video arbitrage | Video CPC ≤0.6x SP exact |
| Confidence | ≥75 HIGH; 50-74 MED; <50 LOW |
| Ranking ACOS envelope | 50-80% (as used in WE-1/WE-2) |
| TOS floor | 30% |
| ETA review horizon | 3 weeks default |
| Stability | 2 consecutive weeks |
| Saturation | Marginal ACOS >1.5x average → freeze, re-test in 2 weeks |
| Elasticity correction | ≥8 weeks push history |
| S-R1 | Bid steps 15-25% |
| S-R2 | Utilization <80% → one budget step 20-30% |
| Recovery Mode human tier | Bid >15%, budget >$25/day |
| Bid change limit | ≤50%, $0.50 floor |
| V5 review | <50% accuracy over ≥10 predictions |
| Daily budget | Required weekly / 7 |
| Category CPC inflation | 18-27% vs Q1 (April 2026 change; observation, not a numeral) |
| A6 account reference Expected CPC | $2.80 |
| Time estimates | P1 25-40m; P2 8-12m; P3 15-20m; P4 4-6m; P5 5-8m; P6 20-30m; P7 6-10m; P8 12-18m; P9 10-15m; P10 8-12m each; P11 15-20m; P12 10-20m; P13 20-30m |

### Worked examples (training base: AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max 26.3%; WE-1 anchors = Economics Worked-Example Set case E3)
- **WE-1:** Rank 22 → target 8 (14 positions). DSTR 4.0, current 1.6, gap 2.4, CVR 5.0%, Expected CPC $2.30.
  - Sizing: clicks 48.0/day; spend $110.40/day; duration 14 days at 1.0/day; budget $1,545.60. Paid orders 2.4/day = $67.20 contribution; loss $43.20/day = $604.80.
  - Ceiling: push ACOS 57.5%; 22.5 pts over BE; weekly sales $1,344.00; ceiling $302.40/wk ($604.80 over 14d). E3 operates at $650 ($45.20 above, AM-10).
  - Ceiling read: Max Profitable CPC $1.40; ratio 1.64 (UNJUSTIFIABLE outside a push). Video threshold $1.38 vs video $1.71 → no arbitrage.
  - Week 1: rank 14 (1.14/day); spend $756.00 vs $772.80 (97.8%); 329 clicks; 17 orders; CVR 5.17%; 47.0 clicks/day (97.9%); ACOS 55.6%; loss $280.00 (92.6% of the 1-week ceiling); TOS 41%; ETA 5.3 days WITHIN → CONTINUE; VERIFY MOMENTUM.
  - Touch day 13; confirmation day 27. The window adds $1,545.60 spend / $604.80 loss; cumulative $1,166.40 vs the $650 ceiling (over by $516.40, AM-3). Loss hits $650 on day 15.0 and nothing fires (AM-1).
  - P13: HIT; velocity 1.08 vs 1.0; CVR 5.06% vs 5.0%; cost $1,435 vs $1,545.60.
- **WE-2:** Rank 19 → 6 (13). DSTR 5.0, current 2.0, gap 3.0, CVR 4.8%, Expected CPC $2.60, push bid $2.74.
  - Sizing: 62.5 clicks; $162.50/day; 13/0.62 = 21 days; $3,412.50; ACOS 67.7%; ceiling $549.50/wk ($1,648.50 over 3 weeks); Max CPC $1.34 (1.93x); arbitrage threshold $1.56.
  - Week 1: rank 18 (FLAT); 432 clicks (98.7%); CVR 4.86%; $1,124.00; loss $536.00 (97.5%); TOS 21% → PLACEMENT FIX FIRST, blocked by B7 MISSING.
  - Week 2: rank 16; 866 clicks, 42 orders; $2,251.00; loss $1,075.00; TOS 22%; ETA 35 days BEYOND.
  - Week 3: rank 15; 0.190/day vs 0.62 (30.7%); $3,378.00 (99.0%); 1,299 clicks; 64 orders; CVR 4.93%; loss $1,586.00 (96.2%). Re-size: 47.25 days; $7,678.13; loss $3,709.13; cost/position $262.50 → $853.13 (3.25x); M5 priority at 30.8% → STOP-LOSS, concede.
  - Bid $2.74 → $1.38 (-49.6%). P13: MISS; CVR 102.7%, cost 99.0%, velocity 30.7%. The finding attaches to T7 B7.
- **WE-3:** Fitted-sheet term, rank 26 → 8, contribution $4.10, AOV $13.90. BE 29.5%, Target 14.8%, Max 22.1%. THIN; cap $1.37 vs Expected CPC $2.10. Max CPC = $4.10 x 0.118 = $0.48 (4.34x). Clicks-to-loss 1.95 → PAUSED-PENDING. Re-entry: contribution ≥$6.30 or Expected CPC ≤$1.37.
- **WE-4:** Shared queen-size term on two siblings. A: $3.24 CPC at rank 17. B: $1.48 at rank 6 (2.19x > 1.5, X6). The X6 inspection finds no objective tags; A has a +180% TOS modifier on a $1.75 base (effective $4.90; $9.80 under up-and-down); A on up-and-down vs B fixed; a legacy duplicate exact on A. Family target rank 3, DSTR 6.0, velocity 0.5/day.

  | | B | A |
  |---|---|---|
  | Orders / gap | 3.6 / 2.4 | 1.1 / 4.9 |
  | CVR | 5.5% | 5.1% |
  | Clicks/day | 43.6 | 96.1 |
  | Expected CPC | $1.60 | $2.90 |
  | Spend/day | $69.82 | $278.63 |
  | Distance / duration | 3 / 6 days | 14 / 28 days |
  | Cost to close | $418.91 | $7,801.57 |

  A is 18.62x more expensive → B lead. A holds Conversions at ceiling and gets repaired. Prediction: family blended CPC -35% within 2 weeks.

## 6. Data inputs required
- **T2 Keyword Command fields:** Organic Rank, Target Rank, Objective, OVERSIGHT filter, Syntax Priority, Seasonal SV Index Dir, Situation, plan block (worksheet versions), DSTR (orders/day), Required Clicks/Day, Required Budget $/wk, Loss Ceiling $/wk, ETA Checkpoint, Review Date, Cost to Close Gap $, Intent Type, Brand CVR, Market CVR, Benchmark Source, Review Position Gap, Price Position Index, Competitor Best Rank, Price Competitiveness Flag, Margin $/Unit, Expected CPC $, Best Rank (Hist) + Date, Pre-OOS Baseline, Velocity (pos/wk), ETA to Target (wks), Actual Clicks/Day, TOS IS %, In-Budget %, Eligibility, Indexed?, Listing Placement, Inventory Band, Days to Stockout, Targeted Variation(s), Envelope Status, Event Mode, Family Conflict, Term Owner (Family), Sibling CPC View, Syntax Tags, Relevancy, Flag: Zero-Quarantine, Validation State, Clicks 7/30/60d, Sample State; child rows; verdict block; rank block; economics block.
- **T0:** zone A (verdict banner: push freeze/code red), zone C (AOV, contribution/order, BE ACOS, Target ACOS, Max Acceptable, Expected CPC, margin table version + fresh/provisional state), zone H (M5 push queue: FUNDED/queued entries, dated release, available dollars, envelope headroom).
- **T1** syntax caps.
- **T4 Placement and Bid** rows (placement splits, B7).
- **T5 Product Log:** Event Type (price move), Trend-Exclusion Flag.
- **T6 Decision Log:** Rule / Scenario Fired, Change (prior -> new), $ Impact / wk, Expected Outcome Window, Review Date, Owner / Tier, V5 Score, taper trigger.
- **T7 Manifest:** Status column, completeness rollup; statuses for A1, A3, A6, B3, B6, B7, D1, D2, D8, D9 (I-6).
- **Catalog field groups:** A1 four-period comparability, A3 pacing/in-budget, A4 sufficiency, A5 threshold flags, A6 objective + per-term Expected CPC, A7 eligibility, B1 indexing/listing, B3 rank pack, B5 coverage counts, B7 placement splits, B8 economics chain, B11 market context / MKL, D1 per-variation margin, D2 keyword-variation map, D6 sibling view, D7 event exclusion, D8 competitor depth, D9 daily rank series.
- **Account Rollup A1** (family boards / term ownership) and **A2** (cross-product queue).
- **SQP** (brand vs market CVR; first benchmark tier), file reference targets, account norm.
- **Daily rank series** (D9).
- **Competitor velocity analysis** (for DSTR; D8).
- **Per-variation margin table** (#41; monthly).
- **#33 family term-ownership declaration**.
- **#32 armed event window** (T-14 intake, T-1 arming) with the affected campaign list.
- **Economics Worked-Example Set case E3**.
- **Video / SBV CPC on the term** (for the S-R10 check).
- **#38 T+1 diff**.
- **Rank Response Elasticity series** (rank movement per 100 incremental clicks).

## 7. Outputs and artifacts
| Artifact | By | Storage / retention | Consumer |
|---|---|---|---|
| Sizing worksheet, versioned | P3 | T2 plan block; life of the term; superseded versions kept | #31 (M5), #28 (authorized CPC envelope), SOP-24, P13 |
| Realism record | P2 | T2 situation/plan fields with cycle date; through the next candidacy | Next P1; listing, pricing, review owners |
| Confidence score + 3 drivers | P4 | Master Action Record; frozen into the cycle KDR file | P5 review-tier router; V6 quarterly calibration |
| Queue submission | P5 | T0 zone H with precedence reason | #31; Account Rollup A2 |
| Standup record with logged taper trigger | P6 | T6 append-only | SOP-12; P10; #38 |
| Daily pacing and rank lines | P7 | T6, one line per intervention; alarm evidence through close | F11 audit; P8 |
| Weekly in-flight verdict with scenario | P8 | T2 verdict block, mirrored into the cycle KDR file | #38; next V5 |
| Stop-loss or achievement record | P9/P10 | T6 with realized figures | #28, SOP-12 P4 (taper); #31 (concession); SOP-25 |
| Re-sized cost-to-close | P11 | T2 cost-to-close field, versioned vs the funding-time value | #31; M5 queue |
| Pre-OOS baseline snapshot | P12.2 | T2 pre-OOS fields; at least the trailing 12 months | SOP-24; future D10 classing |
| Post-mortem with 3 deltas | P13 | T6 with V5; deltas kept indefinitely as the elasticity series | P3.4; V5; V8 training corpus; T7 rows |

Gate artifacts: the daily pacing line in flight (its absence means the push was not operated); the post-mortem at close (a push cannot close without it).

### Verdict mapping
Two states the KDR 25 cannot express use v4.0 13.1 strings in place: **CONTINUE; VERIFY MOMENTUM** and **PORTFOLIO CALL: ASSIGN LEAD**.

| Verdict | v4.0 13.1 cross-map | Scenario | Action |
|---|---|---|---|
| RANK PUSH: FUND SIZED PUSH | RANK PUSH AT CONTROLLED CPC | S-R2, S-R3 | P2-P5; on release P6, P7 same day |
| RECOVERY PUSH | none; S-R13 → RANK PUSH AT CONTROLLED CPC | S-R13 | Class RECOVERY → SOP-24 with class, proven ceiling, pre-OOS baseline |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | none (S-R3 text) | S-R3 | Named lever only via SOP-12; never both levers; re-check ETA in 2 weeks |
| CONTINUE; VERIFY MOMENTUM (v4.0) | in place | S-R2 | No lever; utilization <80% permits one 20-30% budget step |
| PLACEMENT FIX FIRST | none (S-R7) | S-R7 | Bids hold; #28 program; B7 MISSING suppresses the modifier half |
| FIX CONVERSION FIRST; DEFER PUSH | identical | S-R4 | Cap at maintenance; route by funnel drop with price check first; Paused-pending until CVR back to benchmark |
| FIX BUDGET (TRUNCATED) | none (G3) | G3 | Budget lever only; bid read void |
| UNLOCK TRAFFIC | none (S-R1) | S-R1 | Pre-push <15 clicks/7d, healthy budget, GREEN: 15-25% bid steps |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | TAPER TO FLOOR (POST-OBJECTIVE) | S-R6 | P10 |
| HOLD; DEFEND LIGHTLY AT RANK | none (near-neighbour DEFEND AT FLOOR) | S-R9 | Rank at target, CVR below benchmark: hold at minimum viable CPC; fix-first in parallel |
| DEFEND AT FLOOR | identical | S-R9, S-D1 | Post-taper, SOP-25/26 |
| STOP-LOSS: CONCEDE OR DEFER | identical | S-R5, S-R16, S-Y9 | P9 |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | identical | S-R11 | Immediate ladder toward ceiling |
| ADD EXACT + RESTRUCTURE | identical | S-R12 | Defer at P1; SOP-12 + #29 walls |
| RE-POINT VARIATION | identical | S-I3, S-I6 | P12.2 with the baseline first |
| ENTER SBV ARBITRAGE | FORMAT SUBSTITUTION (SBV/SD) | S-R10 | Mandatory check at P3 (the procedure text cites step 11; the check is in step 10); this SOP does only the SP-exact single step down |
| PAUSED-PENDING (REASON + RE-ENTRY) | PAUSE (LEVERS EXHAUSTED) | S-R15, S-I4 | Reason + re-entry required |
| QUARANTINE: DATA REFRESH | FLAG: DATA REPAIR | G1, G8 | No push sizes; refresh task same day |
| PORTFOLIO CALL: ASSIGN LEAD (v4.0) | in place | G11, S-B2 | Both hold at P2 until #33; supply cost-to-close |
| INCREMENTALITY LADDER | none (X12) | X12, S-A5 | Post-objective (SOP-26); a push is never the test vehicle |

### Failure modes
| ID | Failure | Detection | Response | Incident |
|---|---|---|---|---|
| F1 | Unfunded drip push | Above-BE spend, no worksheet version in T2, no FUNDED in T0 H | S-R11 ladder, or size properly | F16 quarter-of-clicks pattern; **June 30, 2026 review**: "concentration without plans" |
| F2 | Push into stockout | Days to stockout < push duration + stability window | Blocked at G6; P12 taper + baseline | A head term fell from **rank 7** across a stockout and was later mistaken for a cold start (F3) |
| F3 | Unindexed / backend-only push | G5 fails | Route to indexing/listing owner | F4 listing-coverage rollup; syntaxes <60% coverage are listing projects |
| F4 | Stall answered with money | Bid/budget lift on a flat row before the placement read and triad | Enforce P8 order | X2; WE-2 |
| F5 | Stop-loss deferred informally | S-R5 met, push still live next cycle, no new worksheet | P9; escalates on first occurrence | F13 |
| F6 | Taper never fires | Rank ≥ target with push-level spend live | P10 immediately; shared audit line with SOP-12 F5 | v4.0 Section 16 Worked Pass 1: head term held at **rank 2 vs target 3 for 5 consecutive weeks**, objective expired 3 weeks earlier, spend never reduced |
| F7 | Worksheet never scored | Closed push without V5 or calibration | P13 late | V1 |
| F8 | Two siblings pushing one term | T2 family conflict / sibling CPC view | G11 holds both | June 30, 2026 review: **$3.24 vs $1.48** on one term; family root ownership open at the first cycle |
| F9 | Blended margin read as final | Ceiling cites a PROVISIONAL T0 block with no flag | PROVISIONAL carried (J7) | D1 open; the live manifest shows a **blended June 2026 figure** in use |
| F10 | Rank credited to a push auto carries | Auto+broad >40% or zero exacts on a Ranking term | S-R12 | v4.0 Section 16 Worked Pass 3: head term **74,000 SV**, zero exacts, two autos carrying **78%** of clicks at **$1.12**, rank 22 vs target 5 |
| F11 | Truncated-week read | In-budget <70% with a bid conclusion staged | G3 voids | F10 |
| F12 | Horizon passed without renewal decision | ETA date past, target not held, no re-sized T6 row | P11 now | O7: ranking objectives here persisted by inertia; F2 |
| F13 | Push opened inside an armed window | Standup in a window without a #32 reference | Revert unless the plan names it; exclusion extends | SOP-32 |

Escalation: F5 on first occurrence (emergency class). F1 as a standing audit line (shared with SOP-12 F5). F6, F8 → PPC Lead with T6 history. Any mode twice in consecutive cycles escalates. Recovery Mode tightens the human tier (R3). Alarm routing: same day F2, F3, F9, F11; weekly worklist F4, F7, F10, F13; PPC Lead F1, F5, F6, F8, F12.

### Interface contracts
| ID | Counterpart | Artifact | Timing | Non-arrival |
|---|---|---|---|---|
| I-1 | From #11 | Economics worked-example set (case E3) | Static; re-issues on v4.0 sizing change | Chain drifts across operators |
| I-2 | From #41 | Per-variation margin table into T0 zone C | Monthly + event-driven, before Monday packet-ready | All ceilings PROVISIONAL (D1 open; blocks SOP-23 sizing) |
| I-3 | From #33 | Family term-ownership declaration | On conflict; family ordering quarterly | G11 holds both indefinitely |
| I-4 | From #31 / instrument layer | Dated funding release in T0 zone H; envelope headroom | Weekly within products; quarterly across family | No push starts; pressure to start informally (F1); routes to PPC Lead by role (C3) |
| I-5 | From #32 | Armed window dates, affected campaigns, in-window allowance | T-14 intake, T-1 arming | P12.6 cannot run; silent distortion |
| I-6 | From #39 / Data Ops | T7 statuses for A1, A3, A6, B3, B6, B7, D1, D2, D8, D9 | Weekly; daily rank daily | P3.9 cannot state gaps → confident recommendation on an incomplete packet |
| I-7 | To SOP-12 | Standup order (structure, bid, daily budget, objective, horizon); taper release | Same day as release / stability | Incomplete creation; F6 on the taper side |
| I-8 | To #28 | Achievement date, push bid, authorized CPC envelope | On taper; on modifier requests | Ladder starts from a guess; ceiling worksheet falls back to maintenance |
| I-9 | To SOP-24 | Pre-OOS baseline, recovery class, discovered floor, prior push CPC | Same day on RED; at close | Recovery sized cold; misclassed NEVER-RANKED |
| I-10 | To SOP-25 | Taper handoff (achievement date, held rank, worksheet ref) | On stability | Retag never fires; false finding every cycle |
| I-11 | To #31 | Released daily budget; re-sized cost-to-close | Same cycle | Queue under-reports dollars |
| I-12 | To #38 | Staged sets with verdict and scenario ID | Tuesday; same day on a dated release | Change silently does not happen |
| I-13 | To T6 / verification | Predictions, V5 scores, 3 deltas | Standup, weekly, close | Rule accuracy cannot compute |
| I-14 | To #29 | Structure-event notice | Same session as standup | Same click bought twice |

## 8. Decision rights
| Authority Matrix row | Rights |
|---|---|
| Push funding (the M5 queue) | **CEO decides above the envelope; PPC Lead decides within it**; incoming operator executes |
| Weekly verdicts, established US | PPC Lead decides; incoming operator and PPC Manager execute; brand-management owner reviews (daily huddle; review, not veto; disagreements route up) |
| Structure creation, all SOPs | PPC Lead decides or per SOP scope; incoming operator executes |
| Bulk deployments | PPC Lead reviews; incoming operator and PPC Manager execute |
| Sibling declarations, S-series | PPC Lead decides; incoming operator executes; brand-management owner reviews |
| Event plans | PPC Lead decides with the deals calendar owner; operator executes |
| Code-red declaration and close | PPC Lead decides; incoming operator and PPC Manager execute |
| Launch-stage verdicts and batches | Launch operator decides and executes; PPC Lead reviews (launch-scope pushes route there) |

- Vacancy rule: D → PPC Lead, E → PPC Manager.
- **Human-mandatory:** P5 funding, P6 standup, P9 stop-loss confirmation, P10 taper release, P11 renewal, P12 suspension/resumption, every 500+ SV action, every structural change, a ceiling-reached row (AM-1), S-A2 sign-off above the PPC Lead while ELEVATED.
- **AI-executable with audit:** P1, P3, P4, P7, P8 evidence assembly, P11 arithmetic, P13.
- v4.1 threshold decisions: Criteria System owner.

## 9. Account-specific facts
- Account spend **$6,000-8,000 per day**.
- Live T7 packet completeness **0.571** (DEGRADED).
  - **MISSING:** D8 competitor depth, B7 placement splits (account-wide), A1 four-period comparability.
  - **PARTIAL:** D9 (head terms only), A6 (account reference Expected CPC **$2.80**), D1, D2 (head terms only), D6, A3 (day-of-week curve pending), B3.
  - **PRESENT:** B8, on blended margin.
- The live manifest uses a **blended June 2026 margin figure**. External dependency **D1** (per-variation margin) is open and blocks SOP-23 push sizing.
- **Bamboo root ownership left OPEN at cycle 1** (G11 live instance); a family root ownership question remains open.
- **June 30, 2026 review** recorded:
  - "concentration without plans"
  - the same (queen-size) term at **$3.24** on one sibling and **$1.48** on another
- Historical incidents (via v4.0):
  - a head term fell from rank 7 across a stockout and was mistaken for a cold start
  - a head term held at rank 2 vs target 3 for 5 weeks with the objective expired 3 weeks earlier
  - a 74,000 SV head term with zero exacts and two autos carrying 78% of clicks at $1.12, rank 22 vs target 5
  - one term absorbing about a quarter of a product's clicks above break-even
- April 2026 platform bidding change; category CPC inflation 18-27% vs Q1 baselines.
- WE-3 uses a fitted-sheet variation ($4.10 contribution, $13.90 AOV); WE-4 a queen-size term. Both are presented as illustrative cases on the training base, but WE-4's CPCs match the June 30 review.

## 10. Open items
| ID | Gap | Interim / evidence |
|---|---|---|
| AM-1 | No scenario fires on the loss ceiling being reached (highest priority) | Routes to the human-mandatory tier; v1.0 local rule retired |
| AM-2 | No execution deadline on a fired stop-loss | v1.0 asserted same day |
| AM-3 | Stability-window spend posture ungoverned and unsized | WE-1: +$1,545.60 spend, +$604.80 loss, $650 ceiling breached by $516.40 |
| AM-4 | No velocity reference for cold-push duration (F6 bands per week; duration runs per day) | Carried the whole error in WE-2 |
| AM-5 | No re-sizing basis below 8 weeks | Realized velocity used directly |
| AM-6 | No max lag from funding release to standup | - |
| AM-7 | No lag on the sibling-conflict hold | Indefinite hold |
| AM-8 | No interval for the post-mortem after close | - |
| AM-9 | No cool-down before a conceded term re-enters | Need an interval or a "what changed" citation |
| AM-10 | No rule for an operating ceiling above the computed one | E3 $650 vs $604.80 ($45.20) |
| AM-11 | No campaign-level pacing tolerance (G7 is 25% at product level) | A3 PARTIAL |
| AM-12 | No authorized CPC buffer under the 2026 auction (Doctrine 6.3, 18-27% observation) | Sizing unbuffered |
| AM-13 | No push concurrency limit per product | - |
| AM-14 | The closed vocabulary lacks continue and lead-assignment members | v4.0 quoted in place; tied to C10 |
| C3 | #31 has no procedural document | Instrument layer cited |
| C6 | #27 deciding document outside the corpus | S-A10 boundary |
| C9 | Gate-number aliases (G9 margin freshness vs price stability; G10 objective tagging vs event exclusion; G12 event freeze vs MKL hygiene) | v4.0 numbering governs |
| C10 | KDR 25 vs v4.0 13.1 vocabulary | - |
| Ledger | Conflicts C1-C15 referenced; component #23 row; external dependency D1 | - |
| Feeds owed | D1 per-variation margin, B7 placement splits, D8 competitor depth (each a version trigger) | - |
| Text inconsistency | The Section 5 ENTER SBV ARBITRAGE row cites "P3 step 11" for the mandatory check, but the S-R10 check is P3 step 10 (step 11 is the prediction) | As in the source |
| Named documents not present | Criteria System v4.0 (incl. Section 16 Worked Passes 1 and 3); KDR v3.0; Strategic Doctrine v1.0 (Sections 1, 2, 6, 6.3, 14); Economics Worked-Example Set v1.0 (E3); Authority Matrix v2.0; Data Architecture v1.0; Command Workbook; SOP-12, SOP-24, SOP-25, SOP-26, SOP-32; #11, #27, #28, #29, #31, #32, #33, #38, #39, #41; Cross-Reference Ledger; Supersession Map; June 30, 2026 review |

Version triggers:
- any v4.0 increment touching 8.4, M2, M5, M10, O3, O7 or G6
- any AM item landing (AM-1 turns P8.7/P9 into a fired scenario)
- D1, B7 or D8 landing
- changes to SOP-24 P3 or the #28 ladder
- quarterly at minimum
