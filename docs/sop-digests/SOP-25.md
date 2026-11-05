# SOP-25 Digest: Transition and Maintenance Operations

Source: `PPC_SOP_25_Transition_and_Maintenance_v2_0.pdf` (17 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-25: Transition and Maintenance Operations (Component #25 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead |
| Supersedes | SOP-25 v1.0 (2026-07-24) in full; Ledger row for #25 replaces the 2026-07-28 seed row |
| Standard | Rebuilt to SOP Build Kit v1.0 twelve-element standard |
| Thresholds | Master PPC Decision Criteria System v4.0 only; zero local thresholds. Numbers v4.0 lacks go to Appendix A amendment items |

**Verdict / purpose.** "Transition is the deliberate descent from push economics to sustainable economics without surrendering the rank the pushes bought, and it is a scheduled program with dates, not a drift." The SOP governs product-level normalization: stage-entry verification, the term-state inventory, the sequenced descent schedule, monthly milestone construction and the dual-limb checkpoint, weekly rung execution, the rank guard during descent, single-term slip reversion, cluster detection and schedule pause, accumulated-waste cleanup, the objective-mix rebalance, event and Recovery overlays, and the exit handoff into SOP-26.

**Governing rule (1.1): the descent is priced before it runs.** A transition is a dated schedule of named actions whose arithmetic is written before the first rung deploys; a month closes on two readings: the actions that landed and the posture that moved.
- v4.0 Section 11 rule **T1**: Ranking flips to post-objective at 2 weeks at or under target rank, then M3.
- v4.0 Section 8.4 scenario **S-R6**: same flip; ranking spend persisting past this point is the definition of unmanaged spend.
- PPC Strategic Doctrine v1.0 Section 1 principle 5: structure that cannot be scored is opinion.
- Account incident: v4.0 Section 16 **Worked Pass 1, "the taper the account never runs"**: head term at rank 2 vs target 3, held five consecutive weeks, Ranking tag expired three weeks earlier and never transitioned, CPC **$1.85** on a THIN **$4.10-margin** variation at **48% ACOS vs 29.5% break-even**. The failure was a missing transition.

v2.0 vs v1.0: procedures 6 -> 14; verdict mapping 5 rows -> full 25 strings; worked examples 1 -> 4; failure modes 5 -> 12; adds operator ramp and interface contracts; corrects one v1.0 threshold (Transition band 8-12% -> v4.0's 7-12%); withdraws v1.0's "met within tolerance" milestone practice.

## 2. Scope and boundaries

### 2.1 Product-level normalization vs term-level taper
A taper = one term walking down a dated ladder. A transition = the product-level program deciding which terms taper, in what order, on what dates, funded from what, checked against what, closed by what artifact. **This SOP owns the program; it owns no rung mechanics.**

| Layer | What decides it | What this SOP does |
|---|---|---|
| Bar to taper a term | v4.0 S-R6 and T1: rank at/under target for 2 consecutive weeks | Reads it; never re-derives, waives, or applies early |
| Size of one rung | v4.0 Section 10 rule M3 inside Section 9 rule L2 limits | Schedules rung on a date; step size read, never chosen |
| Exit target of a ladder | SOP-28 P5: placement-CPC exit bid = blended placement CPC at achieved position less the v4.0 decrement | Records target on schedule row so rung count is knowable in advance |
| Which rung deploys, how | SOP-12 P4 executes; #38 stages, uploads, verifies at T+1 | Issues dated instruction; consumes verification return |
| Order and dating of the whole set | This SOP, P4 | The sequencing is the deliverable |

### 2.2 Three entry routes and one exit
| Route | Condition / source | What arrives |
|---|---|---|
| Taper handoff from completed push | SOP-23 P6.3: hold confirmed, TAPER issues, handoff to SOP-12 P4 and #28 ladder. Ledger #23 row: taper exits into SOP-25 | Push worksheet from T2 K7, standup-logged taper trigger, post-mortem calibration line, prior push CPC |
| Stage renewal at monthly slot | v4.0 rule **T7**: monthly, every product's stage tag confirmed or transitioned; expired Ranking-push tags without rank evidence auto-transition to Transition stage and its TACOS band (mechanically triggers Section 8.1 product-level posture checks) | A stage tag and a band only (thinnest entry; most often finds unfinished push structure) |
| Objective expiry on the terms | v4.0 Section 6 rule **O7**: every Ranking objective carries a horizon date and renews only on evidence; else transitions per T1 or exits per stop-loss | Worklist of terms whose horizon passed, each with T6 history |

Single exit: v4.0 rule T7 is the decision slot; SOP-26 Section 3 requires this SOP's **floor register** as the artifact; SOP-26 Section 2 names the trigger as the SOP-25 handoff. "Operating mature without recorded floors is operating blind."

### 2.3 Adjacent components
| Component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, scenario, gate, lever, verdict incl. stage bands and transition condition |
| #23 Ranking push | Owns push sizing, worksheet, funding, in-flight, achievement, hold confirmation, post-mortem. Open funded pushes at entry continue under SOP-23; descent sequences around them |
| #24 Re-ranking and recovery | Owns loss diagnosis, baseline restoration, recovery sizing, OOS overlays. A slip inside a controlled taper is not a recovery case (F2) |
| #28 Placement and modifier | Owns ladder mechanics at its P5: rung definition, exit-target computation, reversion rule, floor register schema. SOP-25 schedules and consumes floors; derives no step, computes no exit bid |
| #12 Exact operations | Taper execution at P4; promotion/demotion at P5/P6; duplicate consolidation at P7; bid and budget change mechanics at P11 |
| #26 Mature and defend | Floor operations, quarterly re-ladder, defensive architecture, code-red protocol, monthly profit-harvest read. SOP-25 hands over the closed program record with floor register and stops |
| #29 Negation | Doctrine, wall levels, reactive execution standards, monthly wall audit. P10 sweep staged into #29's standards; SOP-25 sets no wall level, writes no evidence line |
| #30 Harvest | Weekly harvest pass never stops during descent; discovery caps tighten to stage allocation (F4) |
| #38 Bulk mechanics | Pull, staging format, upload, T+1 verification |
| #32 Deal/event window | Event plan, armed-window declaration, reconciliation. Descent steps do not deploy inside an armed window |
| #33 Sibling arbitration | Family ownership declaration, read before scheduling a family-shared term |
| #31 Budget and envelope | Funding and envelope verdicts incl. where freed descent dollars go. No procedural document (C3): name T0 zone H and Account Rollup A2 |
| #37 Automation rules | Rule register and change control. Live automation rule touching a scheduled term suspended for the descent window |
| #35 | Incrementality measurement design and continue-or-restore call |
| #16 | Conquest targets |
| #41 | Economics refresh into T0 C18:C24 |
| #39 | Feed and manifest definitions, retention policy (pending) |

## 3. Triggers

Calendar anchors (PPC Command Workbook TEMPLATE v1.0 READ ME "CADENCE AND OWNERSHIP"): **Monday 06:00 feed landing, 09:00 packet ready, Tuesday deploy after the BM huddle, T+1 verification**. Cadence classes from v4.0 rule V4. v4.0 has no numeric lag table (AM-9).

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Stage entry, taper handoff | SOP-23 P6.3 issues TAPER with hold confirmed; T2 K7 push worksheet closes; T6 standup row with logged taper trigger reaches horizon | Same week. No schedule row by following Monday = F3 | P1, then P2, P4 |
| Stage entry, T7 renewal | Monthly stage review writes Transition tag into T0 zone E "PRODUCT STATE VECTOR", dimension "Stage integrity", with date | Same week the tag lands | P1 in full (thinner entry; P2 carries more) |
| Objective horizon reached | T2 K7 "Review Date" on a Ranking-objective row passes unrenewed; PUSHES LIVE filter view surfaces it vs T2 K4 rank | The pass in which the date lands | P2 step 4 classifies; P4 schedules |
| Weekly cadence | Monday cascade reaches T2 on a Transition-tagged product after T0 and T1 read; rungs dated this week due | Same day; stage Monday, deploy Tuesday | P6, then P7 |
| Rank slip on a tapering term | T2 K4 daily rank series (feed D9) worse than rung's logged hold prediction; T6 rung row scores MISS or WRONG-DIRECTION | Same day (daily guard while any rung live) | P8 |
| Slip cluster | Two or more actively tapering terms slip vs predictions in one read window (two T6 rung rows MISS in same window) | Same day second slip lands. Count ungoverned (AM-5) | P9 |
| Monthly milestone date | Milestone date on program record in T5 PRODUCT LOG reaches cycle date | Pass in which date lands; passing unchecked = F3 | P11 |
| Event window arming | #32 armed-window declaration in T2 K2 "Event Mode" with dates; T5 "Trend-Exclusion Flag" set | Before next scheduled rung inside window | P12 event overlay |
| Recovery Mode entry | T0 zone A carries CODE-RED verdict, or product trips v4.0 rule R1 | Same pass | P12 Recovery overlay (R3 tightened tiers) |
| Margin table change | T0 zone C "ECONOMICS BLOCK" shows new margin table version; every ceiling repoints | Same cycle (S-A9) | P5 re-sizes remaining schedule |
| Exit conditions read | T7 monthly stage renewal reaches product with descent landed and floor register populated in T2 K8 | The monthly slot | P13 |

## 4. Procedures

### 4.0 Preconditions and gates (Section 3)
Gate that cannot be read is not a gate that passed (G8 downgrades to a flag). Corpus aliases per C9 (numbering to v4.1 as AM-11).

| Gate | T7 manifest group | Effect on the program | Observable |
|---|---|---|---|
| G1 Validation quarantine | A4, A5, B11 | Impossible-metric row -> flag + data-refresh task, never a rung. Quarantined term does not enter or exit schedule; holds at current rung | T2 K5 "Flag: Zero-Quarantine" = Clean on every scheduled term |
| G2 Sample sufficiency | A4, A1 | Sets what the rung read can conclude, not whether it deploys. Hold prediction is a rank read; CVR/ACOS reads that price next rung clear only at their own thresholds | T2 K2 "Sample State", "Clicks 7/30/60d". Below CVR threshold, ceiling falls back to T0 reference CVR; record says so |
| G3 Budget truncation | A3 | Under in-budget threshold -> every rate TRUNCATED; budget lever before any bid conclusion. Rung on truncated read = F11 | T3 "Truncation Flag (G3)" and "In-Budget Bucket" clear on every hosting campaign |
| G4 Eligibility | A7 | Ineligible SKU halts all lever work; scheduled rung holds with listing task as re-entry; schedule does not skip forward | T2 K2 "Eligibility" = Live; T3 C2 "Eligibility + Reason" clear |
| G5 Indexing and listing placement | B1 | Bars rank-objective standup on unindexed term. Tapering term unaffected; term re-pointed to Ranking objective is | T2 K2 "Indexed?" and "Listing Placement" = Yes and Title or Bullets where rank objective retained |
| G6 Inventory adequacy | D2, F3 inputs | YELLOW freezes push spend at current level (descent already satisfies). RED routes term out of program into SOP-24 P4.1 pre-OOS taper (different instrument: preserving rank memory, not discovering a floor) | T2 K2 "Inventory Band" and "Days to Stockout" GREEN or YELLOW; D2 map names ranked backup |
| G8 Packet completeness | T7 rollup | DEGRADED -> flags only. Program runs rungs it can read, records suppressed classes; never estimates a missing rank series and calls it a hold | T7 "PACKET COMPLETENESS SCORE" stamp on cycle header; blocked verdict classes in-row |
| G9 Price stability (corpus alias: G9 margin freshness) | D1 | Price change in trailing window -> CVR/ACOS PROVISIONAL. Rank read unaffected; ceiling pricing the exit target is; schedule row carries flag | T2 K2 and T0 spine G9 state. T0 C18:C24 (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC) fresh or record states PROVISIONAL |
| G10 Event exclusion (corpus alias: G12 event freeze) | A1, T5 | Event weeks and following days excluded from trend verdicts. No rung inside armed window; rank achieved inside one provisional (S-E5: T1 clock starts after exclusion window). Entering schedule on event spike = F6 | T2 K2 "Event Mode" and T5 "Trend-Exclusion Flag" clear |
| G11 Sibling conflict | D6 | Family-shared term with sibling active push = portfolio decision before schedule row | T2 K8 "Term Owner (Family)" declared (not UNDECLARED); T2 K2 "Family Conflict" clear |
| G12 MKL hygiene (corpus alias: G10 objective tagging) | B2 inputs via the Hub | Every scheduled term in current MKL with syntax tag and relevancy; off-taxonomy term routes to MKL classification | T2 K1 "Syntax Tags" and "Relevancy" populated; MKL refresh inside cadence |

Three standing preconditions: (1) entry artifact set complete (stage tag with date, P2 term-state inventory, live economics chain); (2) open funded pushes identified and excluded before schedule built; (3) no automation rule live on a scheduled term (per Ledger #28 row, #37 holds the ladder on automation rules).

Time figures below are planning estimates, not decision numerals.

### P1. Stage-entry verification and the descent mandate (20-30 min, once per entry)
1. Name entry route and produce its artifact. T0 zone E "PRODUCT STATE VECTOR", "Stage integrity" row. One of three routes evidenced (SOP-23 P6.3 handoff with T2 K7 worksheet closed; T7 renewal tag with date; T2 K7 "Review Date" set of expired Ranking objectives). No route artifact -> return to stage owner.
2. Read entry posture in both currencies: T0 zone B "SIX-NUMBER HEADER" (weekly PPC spend, weekly sales, TACOS vs stage ceiling). Record as % and weekly $. Schedule built in dollars, reported in percent.
3. Classify the deviation (F2): **Transition reference band 7-12%**; **WITHIN <= 1.2x band; ELEVATED 1.2-1.5x; BREACH 1.5-2x; CODE RED > 2x, or > 1.5x for 2 validated weeks**. Write class on program record. Class decides whether a Section 8.1 product-level scenario fires alongside the descent, not whether the descent runs.
4. Read gates strip before schedule: T0 zone D twelve cells G1-G12, each PASS/FAIL/N-A with one-line evidence. Record every FAIL and terms it blocks; those enter inventory with block and get no dates until cleared.
5. Read T7 MANIFEST: record status of **A1, A3, A4, B3, B7, D1, D2, D9**. MISSING suppresses classes in "Verdict Classes Blocked While Missing" cell; write suppression into record. D9 absence changes program shape (rank guard cannot run daily; hold predictions score late).
6. Confirm economics chain live: T0 zone C C18:C24 named cells **AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope**. Blended or stale margin -> G9 PROVISIONAL on every ceiling-referencing row.
7. Write mandate in one line with two numbers: entry posture, band ceiling in dollars, distance between them per week (the program's whole budget of work).

### P2. Term-state inventory (30-45 min per product)
1. Enter T2 only after T0 and T1. Apply **FULL LIST** filter view, not OVERSIGHT (descent touches consolidated tail terms).
2. Score last cycle first: T6 DECISION LOG, rows with "Review Date" this cycle; V5 score HIT / PARTIAL / MISS / WRONG-DIRECTION (V1: unscored actions do not accumulate). Rung row MISS or WRONG-DIRECTION -> P8 in same pass.
3. Classify every tracked term into exactly one of **five states** (read T2 K7 "Objective", K4 rank vs target, K8 "# Exact"):
   - **AT TARGET AND HELD** (rank <= target, hold confirmed, still on push economics)
   - **MID-PUSH** (open worksheet in K7 with funded release)
   - **MAINTENANCE** (post-objective, at or near a recorded floor)
   - **DISCOVERY-ONLY** (no exact instance; discovery surfaces)
   - **BLOCKED** (P1 step 4 gate failure)
   Count of each on the program record.
4. Test AT TARGET AND HELD vs S-R6 (rank <= target for 2 consecutive weeks) on T2 K4 rank **series**, not current cell. One week at target = not yet a row. Five weeks at target with Ranking tag live = Worked Pass 1 case = highest-priority row.
5. Exclude MID-PUSH; note each one's expected achievement date (push landing month 2 -> schedule row month 3; placeholder shown).
6. Read T2 K8 "Term Owner (Family)". UNDECLARED on family-shared term -> G11 holds; route to #33. Sibling with active push on same term -> row does not schedule this cycle.
7. Record ladder state: T4 PLACEMENT & BID "Ladder State (step / date)", "Discovered Floor $", "Placement-CPC Exit Bid $", "Next Step Date" per keyword and placement. Term with prior floor re-probes from floor; no ladder state -> step 0, rung count unknown until P5.

### P3. Objective-mix and structure-mix baseline (15-20 min per product)
1. T0 zone F "TACOS DECOMPOSITION": six rows **Ranking, Conversions, Defense, Discovery, Conquest, UNTAGGED**, each spend $ and share of sales, summing to total TACOS. Read UNTAGGED first (O1: untagged cannot be graded).
2. v4.0 rule O8 sets mix targets for Launch, Ranking push and Mature, none for Transition. Report mix vs own trailing baseline and vs Mature target; missing Transition target = AM-15.
3. Structure mix: Account Rollup **A4 "Structure targets"** (match-type spend split vs v4.0 Section 10 rule **M6** targets). Deviations are findings to explain, not auto-correct.
4. Confirm discovery still funded: **T1 SYNTAX BOARD group S3** spend by objective per family. Caps tighten, do not close. No discovery yield reads = F4 (presence of reads, not level).
5. Write mix line onto program record with milestone path; re-read at every monthly checkpoint. Total fell while composition held = smaller spend of same shape, not a transition.

### P4. Descent schedule build (45-60 min per product, once per entry)
1. Population: AT TARGET AND HELD terms that cleared P2 step 4, plus MAINTENANCE terms whose current bid sits above recorded floor with no verdict authorizing the drift.
2. **Sequence, never batch**: term-by-term ladders sequenced within a syntax family, never started simultaneously inside one family (carried from v1.0 and SOP-28 P5; v4.0 has no rule: AM-4).
3. Order within family: **strongest holds first, contested last** (T2 K4 "Rank gap", "4-wk trend"). Risk ordering, not size ordering.
4. Compute each term's **rung count** before dating: current bid (T3) to exit target (T4 "Placement-CPC Exit Bid $") at **M3 step ~10% per week** inside **L2 limits of +/-50% per change and a $0.50 floor**; count = number of compounding steps reaching target.
5. Date every rung: deploy date, ladder reference, predicted hold position, review date. Undated = intended, not scheduled.
6. Attach reversion budget per term: one rung of reversion per week = (rung CPC - prior rung CPC) x weekly clicks.
7. Version the schedule into T5 PRODUCT LOG program record with P5 milestone dates and P1 mandate. Change = new entry, not edit.

### P5. Milestone construction (25-35 min per product)
1. Build milestone from actions, never reverse: sum weekly removal of the month's scheduled rungs, cleanups, normalizations; compute posture at held sales. Round-percentage milestone populated afterwards = F5 in advance.
2. **Taper rung removal** = CPC delta x weekly clicks; click-hold assumption stated (clicks constant across rung for sizing; checkpoint reads realized clicks).
3. **Negation sweep removal** sized vs campaign utilization (T3 C3 "Utilization %" vs objective target): below target -> removed spend leaves envelope; at budget -> redistributes inside campaign (cleanliness, not savings). Only the first counts toward a milestone.
4. **Modifier normalization** removal = S x m / (100 + m) (S = placement spend, m = modifier %), at held placement clicks. Mechanics belong to SOP-28 P3.2.
5. **Duplicate consolidation** removal = pair's combined spend before less survivor's spend after (not the loser's spend).
6. Re-size on any margin-table change (S-A9: recompute every ceiling immediately; every keyword with CPC above new ceiling enters ladder queue this cycle).
7. Under LOW confidence halve every step (M10: halves lever and budget steps, shortens review horizons to one week, bars pushes). Slower, never suspended.

### P6. Weekly rung execution (20-30 min per product per week)
1. Take only rungs dated this week; no pulling forward. Missed rung = P11 finding; re-dating = explicit schedule amendment.
2. Re-read gates on each due term before staging: **G3 first** (budget lever first per L1 precedence), then G6, G9, G10, G11.
3. Step size read at execution from M3 inside L2 limits; step exceeding L2 limit fails staging QA.
4. **One rung per term per cycle** (one-lever rule) unless verdict names both. **Budget follows the bid down and never leads it** (SOP-12 P4 step 3).
5. **Retag objective at the first rung**, not the last: T1 flips Ranking to post-objective; SOP-12 P4 step 4 retags Ranking -> Conversions, or Defensive where brand-adjacent, in T3 objective tag and campaign-name objective segment in same staged set (F10).
6. T6 entry before deployment: prediction of rank hold at reduced level with metric, direction, magnitude, horizon, review date. v4.0 Section 12 rule **P10**: change without logged prediction does not deploy at any tier.
7. Stage per #38 (entity, prior value, new value, reason string with verdict and scenario ID); Tuesday deploy after BM huddle; T+1 report confirms; mismatch returns same day.

### P7. Rank guard during descent (10 min daily while any rung live)
1. Read daily rank series (T2 K4 from D9) on every tapering term vs rung's logged hold prediction. Runs daily while rung live; stops when term reaches floor and holds. V4 names no descent cadence; daily carried from v1.0 (AM-8).
2. Read position, then the log (D5): T5 PRODUCT LOG for listing change, price move, OOS window, deal window, competitor entry in rung's window.
3. Slip vs noise on G2: week-over-week swings above threshold on thin samples are noise by definition; read the series, not the point.
4. Single confirmed slip -> P8; second confirmed slip in same window -> P9.
5. Record clean guard reads as reads.

### P8. Single-term slip response: one-rung reversion (15 min per case)
1. Revert exactly one rung (M3: restore one step on slippage beyond tolerance; restored value = recorded minimum viable CPC). SOP-28 P5 mechanics: revert one rung, **hold two windows**, then re-probe or record floor at last held rung. Reverting two rungs discards information.
2. Record tolerance gap: v4.0 defines no tolerance; reversion executes on logged hold prediction being missed; basis stated on row (AM-6).
3. Price reversion in $/week (P4 step 6 figure); enters month's checkpoint arithmetic.
4. **Do not fund a recovery.** Recovery during descent needs SOP-24 gate in full: named cause, RESOLVED, with verification artifact. Live competitor deal window = named but unresolved cause (closes by calendar). F2.
5. Hold two windows, then decide (re-probe or record floor). Never re-probed = F7.
6. Write floor register entry when floor lands: term, floor bid, date, competitive context note (schema SOP-28's).

Decision tree (P8 text):
```
Rung's hold prediction missed on daily read
 +-- T5 log shows listing/price/OOS/deal/competitor event in window?
 |    Yes -> attribution first (D5): hold the rung, record cause, re-read after exclusion window
 |    No  -> continue
 +-- Series or single point? (G2)
 |    Single point, thin sample -> noise; no action
 |    Series -> confirmed slip
 +-- Second confirmed slip same window on another tapering term?
      No  -> P8: revert ONE rung, hold two windows, price give-back, then re-probe or record floor
      Yes -> P9: pause schedule, run cause classes. Never fund a recovery push (F2)
```

### P9. Cluster detection and schedule pause (30-45 min per occurrence)
1. Pause schedule on the cluster before diagnosing (slips across **2 or more** tapering terms in one window; count from v1.0; AM-5).
2. Run SOP-24 P1 cause classes in order only: date loss from daily series, then OOS event, price change, review shock, listing event, competitor surge, deal hangover, taper too deep (checked last).
3. Name one primary cause with evidence; UNKNOWN is legal, routes to deeper read, never default resumption or push.
4. Route by cause class: outside PPC -> brand-management owner, schedule paused until resolved; competitive cause with calendar end -> hold to that calendar; only "taper too deep" resumes directly, re-sized (P5 recomputes exit targets on affected family).
5. Escalate re-read findings regardless of outcome.
6. Resume with re-probe of reverted rung on paused terms; unaffected terms resume dates. Resuming all at once = F1 late.

### P10. Accumulated-waste cleanup (45-90 min per cleanup class)
1. Descent is the scheduled occasion for push-era debris; each cleanup class lands inside a named month per P5.
2. Reactive negation sweep: zero-sale and above-limit terms from discovery surfaces handed to #29 P3 with evidence lines. Relevance check precedes negative; relevant non-converter -> fix queue, never negative list.
3. Duplicate consolidation: T2 K8 "Duplicate Flag" and T3 role declarations. Second live exact instance without one of the **four declared roles** = SOP-12 P7 territory. Survivor selection human-mandatory (SOP-12); SOP-25 supplies month and expected release.
4. Placement-modifier normalization on expired push justifications: SOP-28 P3.2 steps toward zero on ladder cadence. Trigger = objective's own closure (AM-12).
5. Quantify every cleanup class in weekly dollars; feed to P11.
6. Keep harvest running: #30 weekly pass; yields land in T3 C5 "Harvest Yield".

### P11. Monthly milestone checkpoint: dual-limb read (30-40 min per milestone)
1. **Action limb first**: #38 deployment records for the month: rungs landed vs dated, cleanup classes executed vs scheduled, reversions.
2. **Posture limb second**: T0 zone B spend and TACOS vs P5 milestone figure.
3. **Fail if either limb fails.** Ratio at target with actions unlanded = milestone theater; ratio improved by sales growth while spend unnormalized detected by re-reading same spend against **entry sales base**. Actions landed, posture unmoved = sizing error -> P5.
4. Name miss cause in one of two classes: **actions unexecuted** or **actions executed without effect**.
5. Record miss: realized figure, gap, gap's weekly dollar value. No milestone tolerance in v4.0 (AM-3).
6. Re-read objective mix beside posture.
7. Reschedule explicitly: dated amendment naming unexecuted actions.

### P12. Event-window and Recovery-Mode overlays (10-15 min per window)
1. Inside armed event window: schedule holds, staging continues; rungs dated to window end.
2. Event-window rank is not a hold; rung overlapping event re-reads after exclusion period.
3. Refuse a term whose rank was achieved inside an event (S-E5; F6).
4. Recovery Mode: tighten confirmation tier, keep descending. **R3: human-confirms bid moves > 15% and budget moves > $25/day; caps step sizes at standard even at HIGH confidence.**
5. Mode precedence **T8: Recovery Mode > Event Mode > stage defaults**. Product in Recovery entering event runs event at defense-and-proven-terms posture only.
6. Record the overlay on the checkpoint.

### P13. Transition exit: floor register handoff (30-40 min, once per exit)
1. Verify exit at T7 monthly slot only, never mid-month (F12).
2. State boundary: T2 refers stage gates to Launch/Scale graduation criteria and Phase 1-4 model in Criteria System v1.0 (March 2026), not held. SOP verifies posture vs band, floor register completeness, scored schedule; hands stage decision to PPC Lead with BM owner (AM-7).
3. Complete floor register before handoff: every closed ladder carries floor in T2 K8 with date and competitive context note. Ladders ended in reversion without re-probe listed as open with reverted rung and reason (F8). SOP-26 P1.1 resets drift above floor to floor.
4. Name floors at or above ceiling: compare each floor vs term's Max Profitable CPC (T2 K6). Floor above ceiling = position rented, not earned; lets SOP-26 P5 harvest read and v4.0 Section 4 rule **X12** incrementality ladder decide.
5. Close program record: rungs deployed, V5 scores by class, reversions, cluster pauses, milestones met/missed with causes, realized descent in weekly $ vs P1 mandate.
6. Route freed dollars, do not spend: post released weekly spend to M5 push queue at T0 zone H and Account Rollup A2 as funding supply (C3).

### P14. Program close and carry-forward (20 min, once per exit)
1. Calibration line: realized vs planned rung count; realized vs sized removal; realized reversion count vs priced reversion budget.
2. Score schedule as a whole (rungs mostly HIT while posture missed = sequenced right, sized wrong).
3. Return per-term floors to T4 and register; floors re-test on V4 quarterly cycle under SOP-26 P1.2, or earlier after logged competitive shock.
4. File program record in T5; leave T6 chain open (post-exit review dates still score, routed to SOP-26 holder).
5. Hand back amendment items generated.

### Appendix B operator card (18 lines, compressed P1-P14)
No entry without artifact; posture in % and weekly $; classify deviation, don't act on it; gates and manifest before schedule; five states; test at-target on series, never on event-window read; sequence within family strongest first; compute rung counts and price reversions before dating; build milestone from actions; one rung per term per cycle, budget follows bid, retag at first rung; T6 prediction before deploy, stage Monday, deploy Tuesday, reconcile T+1; guard daily, log before ladder, series before slip; one slip reverts one rung holds two windows, two slips pause and run SOP-24 P1 classes; reversion not recovery; close on both limbs, re-read spend vs entry sales base; name every miss by cause class; exit only at T7 slot with register complete, name floors above ceiling; post freed dollars to queue.

## 5. Rules, thresholds and numbers

### 5.1 Numeric values
| Item | Value | Source |
|---|---|---|
| Transition TACOS band | **7-12%** (v4.0). Corpus instruments carry 8-12% (AM-1) | F2 |
| Other stage bands (instrument vs v4.0 divergence, AM-1) | Ranking push 10-18% vs 12-15%; Launch 15-25% vs "<=25% dated"; Harvest "<=3%" vs "<=4%"; instruments label set "(M7)" where v4.0 M7 is marginal mathematics | AM-1 |
| Deviation classes | WITHIN <= 1.2x band; ELEVATED 1.2-1.5x; BREACH 1.5-2x; CODE RED > 2x or > 1.5x for 2 validated weeks (matches R1). Instruments say "Code-red at >1.5x band" with no duration (AM-2) | F2, R1 |
| Transition condition | Rank <= target for 2 consecutive weeks | S-R6, T1 |
| M3 rung | ~10% per week reduction (4 rungs = 0.9^4 = 0.6561; 3 rungs = 0.729) | M3 |
| L2 limits | +/-50% per change; $0.50 floor | L2 |
| Reversion | revert one rung; hold two windows | M3, SOP-28 P5 |
| Slip cluster | 2 or more tapering terms in one window (v1.0 carry; ungoverned) | AM-5 |
| Modifier premium removal | S x m / (100 + m) | P5 |
| Reversion cost | (rung CPC - prior rung CPC) x weekly clicks | P4/P8 |
| Recovery Mode confirmation | bid moves > 15%, budget > $25/day human-confirmed; step sizes capped at standard even at HIGH | R3 |
| Human-review tier (standard) | every 500+ SV keyword action, every gate failure, every structural change, every bid move > 25%, every budget move > $50/day | P5 (Section 12) |
| Mode precedence | Recovery Mode > Event Mode > stage defaults | T8 |
| LOW confidence | halve lever and budget steps; review horizons one week; bars pushes | M10 |
| Ranking ACOS envelope | 50-80% (a Ranking-tagged term is graded against it) | (F10 / I-3) |
| Target / Max Acceptable | Target = 50% of break-even; Max Acceptable = 75% of break-even | WE chain |
| Max Profitable CPC | contribution x CVR | WE chain |
| Floor re-test | quarterly (V4) under SOP-26 P1.2 | V4 |
| Rank guard without D9 | slow to one rung per term per two windows | I-7 |
| Calendar | Monday 06:00 feed; 09:00 packet ready; Tuesday deploy after BM huddle; T+1 verification | Workbook READ ME |
| Operator ramp close | two clean audit months | Section 11 |

### 5.2 Criteria System v4.0 rule IDs referenced
| ID | Meaning as described |
|---|---|
| F2 | Product State and Strategy family: Transition band 7-12%, deviation classes; notes a mature product running a launch-shaped spend structure is a finding |
| F3 | Inventory inputs (G6) |
| G1-G12 | Gates (Section 4.0 table); G2 also: WoW swings above threshold on thin samples are noise |
| G8 | Missing gate fields downgrade verdict to a flag |
| O1 | Untagged row cannot be graded |
| O7 | Ranking objective carries horizon date; renews only on evidence |
| O8 | Stage mix targets for Launch, Ranking push, Mature; none for Transition; actual-vs-target mix is monthly product finding |
| D5 | Product log consulted before PPC credited or blamed |
| S-R6 | Taper condition: rank <= target 2 consecutive weeks; spend past it is unmanaged |
| S-R9 | Conversion deficit: hold rank at minimum viable CPC while deficit routes to owner |
| S-R10 | SBV arbitrage paired with SP-exact step down one rung |
| S-R12 | ADD EXACT + RESTRUCTURE; structure repair before any performance verdict |
| S-R13 | RECOVERY-class push |
| S-A1 to S-A9 | Product-level scenarios (Section 8.1); S-A3 freezes new Ranking objectives at BREACH; S-A9 recompute ceilings on margin move and queue keywords above new ceiling |
| S-E5 | Rank achieved during events provisional; T1 clock starts after exclusion |
| S-C5 | Funding into competitor deal price buys worst comparison of month (Section 8.7 conquest) |
| S-D1 | Mapped (with S-R6) to TAPER TO FLOOR (POST-OBJECTIVE) in 13.1 |
| T1 | Ranking -> post-objective at 2 weeks at/under target, then M3 |
| T2 | Stage gates refer to Launch/Scale graduation criteria and Phase 1-4 model (Criteria System v1.0) |
| T7 | Monthly stage renewal; expired Ranking-push tags without rank evidence auto-transition |
| T8 | Mode precedence |
| R1 | Code-red trip |
| R3 | Recovery Mode tightened confirmation tiers; bars new pushes outside RECOVERY class |
| M1 | Listed for re-validation |
| M3 | ~10%/week taper step; restore one step on slippage beyond tolerance; on cannibalization-flagged terms the taper is the incrementality test |
| M5 | Push queue |
| M6 | Match-type structure targets |
| M7 | Marginal mathematics (cited in AM-1) |
| M10 | LOW-confidence step halving |
| L1 | Budget lever precedence before bid conclusions |
| L2 | Per-change limits +/-50%, $0.50 floor |
| X10 | Structure repair ordering (auto/broad carrying a term) |
| X12 | Incrementality ladder: total organic + paid capture holding for two windows before ladder continues |
| P5 | Human-review tier (500+ SV, gate failure, structural change, bid > 25%, budget > $50/day) |
| P10 | Change without logged prediction does not deploy at any tier |
| V1 | Unscored actions do not accumulate |
| V4 | Cadence classes; daily for pushes and events; quarterly floor re-tests |
| V5 | Scoring HIT / PARTIAL / MISS / WRONG-DIRECTION |
| C3, C9, C10, C12 | Ledger conflicts |

## 6. Data inputs required

### 6.1 Command Workbook (PPC Command Workbook TEMPLATE v1.0)
- **T0 zone A**: verdict banner, stage tag, CODE-RED verdict.
- **T0 zone B "SIX-NUMBER HEADER"**: weekly PPC spend, weekly sales (all sources), TACOS vs stage ceiling.
- **T0 zone C "ECONOMICS BLOCK"** cells **C18:C24**: AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope; margin table version; G9 freshness state.
- **T0 zone D**: twelve-cell gates strip G1-G12 (PASS / FAIL / N-A + evidence note).
- **T0 zone E "PRODUCT STATE VECTOR"**: "Stage integrity" and state-vector rows.
- **T0 zone F "TACOS DECOMPOSITION"**: Ranking, Conversions, Defense, Discovery, Conquest, UNTAGGED (spend $ and share of sales).
- **T0 zone H "M5 PUSH QUEUE"**.
- **T1 SYNTAX BOARD group S3**: "Spend Share Actual %", "Share vs Target (pp)", "Cap Status", "Spend by Objective ($)".
- **T2** (filter views FULL LIST, OVERSIGHT, PUSHES LIVE):
  - K1 identity: Syntax Tags, Relevancy, SV, Oversight Flag.
  - K2 gates: Validation State, Sample State, Clicks 7/30/60d, In-Budget %, Eligibility, Indexed?, Listing Placement, Inventory Band, Days to Stockout, Family Conflict, Event Mode.
  - K4 rank: organic rank daily series, Target rank, Rank gap, WoW delta, 4-wk trend, Velocity, OOS overlay flag.
  - K5: Flag: Zero-Quarantine.
  - K6 economics: Max profitable CPC, Expected CPC, CPA ceiling.
  - K7 plan: Objective, Loss ceiling, Review Date, Weeks-at-verdict; push worksheet.
  - K8 registry: # Exact, Duplicate Flag, Term Owner (Family), Current bid vs suggested, TOS modifier %, floor register (floor bid, date, competitive context note).
  - K9: verdict column (KDR data-validation list).
- **T3**: C1 "Objective Tag" and "Stage-Stack Role"; C2 deployment (Daily Budget, Bidding Strategy, Placement Mult TOS %, "Eligibility + Reason"); C3 pacing (Utilization %, In-Budget Bucket, Truncation Flag (G3)); C5 structure (Harvest Yield, Graduations (Qtr)); role declarations; current bid.
- **T4 PLACEMENT & BID**: all six bid-mechanics columns, esp. "Placement-CPC Exit Bid $", "Ladder State (step / date)", "Discovered Floor $", "Next Step Date" per keyword and placement.
- **T5 PRODUCT LOG**: events (listing change, price move, OOS window, deal window, competitor entry, eligibility flip) with Trend-Exclusion Flag; the program record (schedule, mandate, inventory, milestones).
- **T6 DECISION LOG**: rung rows with predictions, Review Date, V5 scores.
- **T7 MANIFEST**: groups A1, A3, A4, A5, A7, B1, B3, B7, B11, D1, D2, D6, D9; "Verdict Classes Blocked While Missing"; "PACKET COMPLETENESS SCORE".
- **REFERENCE tab** (carries the divergent 8-12% band; AM-1).
- **Account Rollup A2** (queue/funding) and **A4 "Structure targets"** (match-type split vs M6).

### 6.2 Feeds, reports and external artifacts
- D9 daily rank feed (organic rank per tracked term with OOS overlay), daily.
- #38 deployment records / staged change sets and T+1 verification report.
- SOP-23 closed push worksheet, standup taper trigger, post-mortem calibration line, prior push CPC.
- #28 P5 rung definition, step size reference, reversion rule, per-term placement-CPC exit bid (position CPC data).
- SOP-24 P1 ordered cause-class list; SOP-24 P2 restoration verification artifact.
- Brand Management dated event log entries.
- #29 P3 sweep, SOP-12 P7 duplicate set, #28 P3.2 expired-justification modifier set.
- #30 P12 per-source yield reads and "Graduations (Qtr)".
- #41 economics refresh (before Monday 09:00 packet-ready read).
- #32 armed-window declarations with dates and named actions.
- #33 declared term owner with declaration date.
- #37 rule-change log confirming suspension.
- Discovery surfaces' zero-sale and above-limit terms (for negation sweep).
- Master Keyword List (via the Hub; B2 inputs).
- KDR Template v3.0 "Bands & Verdicts Reference" sheet.

## 7. Outputs / artifacts

| Record | Storage | Retention | Consumer |
|---|---|---|---|
| Program record (schedule, mandate, inventory, milestones) | T5 PRODUCT LOG, versioned, one entry per schedule version | Product log's; ungoverned (AM-10) | P11, P13, operator ramp, next transition's calibration |
| Dated rung schedule | Inside program record: each rung's date, ladder reference, predicted hold, review date | With program record | P6 weekly; SOP-12 P4 one dated instruction per rung; F3 detection |
| Staged rung sets | #38 staged change set: prior value, new value, reason string with verdict and scenario ID | With #38 set | SOP-12 P4 deploys; #38 T+1; action limb of P11 |
| Monthly milestone verifications | Program record, one row per milestone: actions dated, actions landed, posture planned, posture realized, cause class on miss | With program record | PPC Lead monthly review; escalation on second miss; P14 |
| Reversion records | Program record and T4 "Ladder State (step / date)" | With T4 row for term's life | P8 step 5; F7; checkpoint give-back |
| Cluster pause findings | Program record with SOP-24 P1 cause class, evidence, resolution calendar | With program record | Escalated regardless; P5 re-size if taper too deep |
| Floor register | T2 K8 per term (floor bid, date, competitive context note); T4 "Discovered Floor $" | Rolling with term's row | **Exit gate.** SOP-26 P1.1 reset to floor, P1.2 quarterly re-ladder one rung per cohort; #28 P5 schema |
| Cleanup quantifications | Program record, one line per cleanup class: weekly $ and utilization test | With program record | P11 action limb |
| T6 decision-log entries | T6, one row per deployed rung: prediction, magnitude, horizon, review date | Append-only, never edited | V5 scoring; MISS/WRONG-DIRECTION -> P8; #6 rubric |
| Released-spend posting | T0 zone H "M5 PUSH QUEUE" and Account Rollup A2 | Rolling | Queue funding supply; allocation is envelope owner's |
| Suppression statement | Program record header: T7 groups STALE/MISSING and classes blocked | With program record | States what analysis could not see |

Stage gate artifact at exit: closed program record with floor register. Skill outputs mirror these plus daily guard reads (slip/noise) and F1-F12 alarms (evidence line: row, signal value, gate/rule reference).

### Verdict mapping (25 KDR strings)
| Verdict | Transition execution |
|---|---|
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | The verdict this SOP schedules (P4, P6 via SOP-12 P4, P7, P8). 13.1 cross-map: TAPER TO FLOOR (POST-OBJECTIVE), mapped to S-R6 and S-D1. KDR string written into T2 K9 (data-validation list) |
| HOLD; DEFEND LIGHTLY AT RANK | State between P2 qualification and P4 slot; parked past scheduled date = F3 |
| DEFEND AT FLOOR | Terminal state of completed ladder; drift above floor restored in one staged step at SOP-12; SOP-26 P1.1 operates thereafter |
| INCREMENTALITY LADDER | On cannibalization-flagged terms the taper is the incrementality test (M3; X12: two windows); measurement and call belong to #35 |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Distinct from taper (economics failed vs objective achieved); term leaves schedule; single-step edit at SOP-12; syntax cap at T1 via instrument layer |
| CONSOLIDATE DUPLICATES | P10 step 3 schedules month and release; SOP-12 P7 executes; survivor selection human-mandatory |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | P10 step 2 occasion and count; #29 owns. 13.1: CUT / NEGATE |
| PLACEMENT FIX FIRST | Descent holds on that term while #28 runs placement program |
| RECOVERY PUSH | No transition execution; F2 boundary; SOP-24 gate in full. v4.0 carries at S-R13 not S-R12 (AM-13) |
| RANK PUSH: FUND SIZED PUSH | No transition execution; S-A3 freezes new Ranking objectives at BREACH; R3 bars outside RECOVERY class in Recovery Mode; funded push leaves schedule to SOP-23 |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | No transition execution (live push; SOP-12) |
| STOP-LOSS: CONCEDE OR DEFER | Term closed by stop-loss at entry enters inventory as MAINTENANCE, not AT TARGET AND HELD |
| FIX CONVERSION FIRST; DEFER PUSH | Caps at maintenance, leaves schedule until fix (S-R9) |
| FIX BUDGET (TRUNCATED) | Rung holds; budget lever first (L1); F11 |
| RE-POINT VARIATION | Term exits schedule the day G6 reads RED; SOP-24 P4.1 pre-OOS taper is a different instrument |
| PAUSED-PENDING (REASON + RE-ENTRY) | Scheduled term held by blocking gate; row stands; reason = gate, re-entry = clearance |
| QUARANTINE: DATA REFRESH | No rung; holds; refresh task with owner and date |
| UNLOCK TRAFFIC | No transition execution |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | No transition execution |
| FUND TEST (UNFUNDED PRIMARY) | No transition execution; funding a test during descent is legitimate |
| GRADUATE FROM DISCOVERY | No transition execution; harvest continues. 13.1: GRADUATE + STEER |
| ENTER SBV ARBITRAGE | S-R10 pairs arbitrage with SP-exact one-rung step; that rung is the arbitrage's; schedule deploys no own rung that cycle |
| OPEN / ROTATE / EXIT CONQUEST | No transition execution (#16) |
| LEAVE TO HARVEST | No transition execution (#30) |
| ADD EXACT + RESTRUCTURE | Structure gap in P2 routes to #12 and #29 before scheduling (X10, S-R12) |

## 8. Decision rights

PPC Authority Matrix v2.0 rows (D = decides, E = executes, R = reviews):
| Row | Rights |
|---|---|
| Weekly verdicts (established US) | D PPC Lead; E incoming operator (assigned scope), E PPC Manager; R BM owner. Weekly rung pass and schedule sign-off |
| Structure creation (all SOPs) | D PPC Lead or per SOP scope; E operator and PPC Manager. Every stage-entry declaration and stage advance |
| Bulk deployments (#38) | R PPC Lead; E operator and PPC Manager. Every staged rung set |
| Launch-stage verdicts + batches | D and E launch operator; R PPC Lead and BM owner. Descent on launch-stage product not this operator's |
| Sibling declarations (S-series) | D PPC Lead; E operator; R BM owner |
| Automation rules (#37) | D PPC Lead; E and R operator. Authority to suspend a rule for descent window |
| Push funding (M5 queue) | D CEO above envelope, PPC Lead within; E operator (posts freed dollars, does not allocate) |

- **AI-executable with audit**: term-state inventory, schedule drafting and sequencing, rung-count computation, milestone sizing, weekly rung staging, daily rank-guard and slip-vs-noise test, reversion pricing, cleanup quantification, checkpoint arithmetic, floor-vs-ceiling comparison, suppression statement.
- **Human-mandatory**: schedule sign-off; every cluster-pause re-read and cause-class call; every stage advance and stage-entry declaration; every deployment confirm; any descent on a launch-stage product; any schedule row on a family-shared term pending declaration; any automation-rule suspension. v4.0 human-review tier on top (P5), tightened by R3 in Recovery Mode.
- Stage decision at exit: PPC Lead with BM owner.
- BM owner's R = daily huddle, review not veto; disagreements route up. Vacancy rule: D -> PPC Lead, E -> PPC Manager.
- Escalation: F2 first occurrence to PPC Lead; F3 on second consecutive occurrence with list; F5 first occurrence; P9 cluster findings always; F12 to PPC Lead and BM owner jointly.
- Alarm routing: F2, F5, F12 same day to PPC Lead; F6, F9, F11 same day to operator queue; F1, F7, F10 weekly worklist; F3, F4, F8 monthly checkpoint and exit.
- Operator ramp: week 1 observe (reproduce WE-1 month 1 taper arithmetic to the cent); week 2 supervised (zero rungs on truncated campaign is pass bar); week 4 unsupervised; two clean audit months close ramp. Launch-stage and Canada products outside scope until Matrix rows transfer.

### Failure modes
| ID | Failure | Detection |
|---|---|---|
| F1 | Simultaneous family tapers | Two same-family ladders sharing start window, or two T6 rung rows on one family same week |
| F2 | Recovery push on a descent slip | Recovery standup on tapering term with no SOP-24 P2 restoration artifact |
| F3 | Schedule drift | Milestone date passing with actions unexecuted, or term at HOLD past slot. Two consecutive misses escalate |
| F4 | Harvest stopped | No yield reads in T3 C5, or discovery spend zero in T0 zone F |
| F5 | Milestone theater | Posture limb passes while #38 shows unlanded actions; re-read spend vs entry sales base |
| F6 | Descent on event-provisional rank | Qualifying at-target weeks inside T5 trend-exclusion window, or T2 K2 Event Mode flag at P2 step 4 (no prior incident) |
| F7 | Reversion never re-probed | T4 reverted rung with no probe date past two-window hold |
| F8 | Exit on partial floor register | Recorded floors in T2 K8 fewer than ladders closed, or floor missing date/context |
| F9 | Budget leading bid down | Budget cut dated before/with rung on same term in #38 set |
| F10 | Objective never retagged | T3 "Objective Tag" still Ranking during ladder, or T3 vs campaign-name mismatch (SOP-12 F7) |
| F11 | Rung on truncated read | T3 "Truncation Flag (G3)" set in same window as deployed rung |
| F12 | Stage advance on one reading | Mature tag in T0 zone E outside T7 slot, or advance without three P13 artifacts |

## 9. Account-specific facts

- v4.0 **Worked Pass 1**: head term rank 2 vs target 3, held five consecutive weeks, Ranking tag expired three weeks earlier and never transitioned; CPC $1.85 on THIN $4.10-margin variation; 48% ACOS vs 29.5% break-even.
- "The account's post-objective spend persistence" is the named pattern; it survives in the five v1.0 gaps (entry-artifact set, milestone arithmetic, reversion cost, cluster basis, non-arrival consequences).
- Ledger dependency **D3 (#28 placement feed) OPEN**; dependency **D1 (economics) OPEN**.
- SOP-23, SOP-24 and SOP-26 copies attached to this build session were at v1.0, so I-1, I-8, I-13 seams written from Ledger rows.
- Bamboo family used as the sequencing family in WE-1 (illustrative).
- Copies of the Transition band in the KDR Template v3.0, the Command Workbook REFERENCE tab and Doctrine Section 2 read 8-12%; v1.0 sized against 8-12%.

### Worked examples (training base, illustrative)
Training base: **AOV $80.00; contribution $28.00/order; break-even ACOS 35.0%; Target ACOS 17.5%; Max Acceptable 26.3% (26.25%); reference CVR 5.2%; Max Profitable CPC $1.456 (carried $1.46)**.

- **WE-1 clean program**: entry via T7 renewal (tag expired, auto-transitioned). Weekly spend $4,489.00, sales $33,500.00; TACOS 13.4%; band ceiling 12.0% = $4,020.00; distance $469.00/wk; deviation 1.12x = WITHIN. Gates twelve PASS. Inventory 21 terms: 7 AT TARGET AND HELD, 2 MID-PUSH, 9 MAINTENANCE, 3 DISCOVERY-ONLY; one held 6 weeks with Ranking tag live (first slot). Month 1 tapers (4 rungs each): A $2.42, 96 clicks, $232.32 -> $1.5878, $152.43, removes $79.89; B $2.14, 78, $166.92 -> $1.4041, $109.52, $57.40; C $1.96, 64, $125.44 -> $1.2860, $82.30, $43.14; D $1.78, 55, $97.90 -> $1.1679, $64.23, $33.67; set $622.58 -> $408.48, removes $214.10. Negation sweep: 23 zero-sale terms, $148.20/wk, two discovery campaigns at 61% utilization (not capped). Month 1 removes $362.30; spend $4,126.70; TACOS 12.3%; 16 rungs dated and landed. Month 2 tapers: E $2.28, 88, $200.64 -> $1.4959, $131.64, $69.00; F $2.05, 71, $145.55 -> $1.3450, $95.50, $50.05; G $1.92, 59, $113.28 -> $1.2597, $74.32, $38.96; set $459.47 -> $301.46, $158.01. Two consolidations: losers $214.90, survivors $131.60, release $83.30. Month 2 removes $241.31; spend $3,885.39; TACOS 11.6%. Month 3: 5 expired push justifications, $986.00/wk TOS at +45% modifier; premium 986 x 0.45/1.45 = $306.00; spend $3,579.39; TACOS 10.7%. Program: **$909.61/wk removed = 20.3% of entry spend = $47,299.72 annualized**.
- **WE-2 slip cluster**: month 2 week 2, term E rank 7 vs hold 4-5, term F rank 9 vs hold 6-7, both on rung 4. T5 competitor entry: deal price on two competing ASINs. Cluster -> pause; cause = competitor surge (not taper too deep; targets stand). Reversion: E $1.4959 -> $1.6621 (delta $0.1662 x 88 = $14.63); F $1.3450 -> $1.4945 ($0.1494 x 71 = $10.61); total $25.24/wk. Recovery push refused (F2). Realized removal $216.07; spend $3,910.63; TACOS 11.7% vs 11.6% milestone: action limb passes, posture misses by 0.1pp = $25.24/wk, $1,312.48 annualized; cause class "actions executed without full effect".
- **WE-3 two refusals**: (a) sales rise to $36,800.00, spend unchanged $4,489.00 (none of 16 rungs staged; #38 record empty); TACOS 12.2% beats 12.3% milestone but fails action limb; at entry sales base still 13.4%; $362.30/wk not removed = $18,839.60 annualized; F5, cause "actions unexecuted". (b) Term rank 4 vs target 5 held two weeks inside armed deal window -> not scheduled; HOLD; DEFEND LIGHTLY AT RANK with window as re-entry (F6).
- **WE-4 exit**: month 3 at 10.7%. 13 floors in T2 K8; mean $1.27, high $1.59, low $0.94. E and F open (reversion, re-probe pending). vs Max Profitable CPC $1.46: 11 under; two above ($1.59, $1.50) = rented. 21 rungs scored: 14 HIT, 5 PARTIAL, 2 WRONG-DIRECTION = 66.7% hit rate. Milestones: met, missed posture by $25.24/wk, met. $909.61/wk posted to M5 queue.

## 10. Open items

### 10.1 Appendix A amendment items (AM-1 to AM-15)
| ID | Gap | Notes |
|---|---|---|
| AM-1 | Transition TACOS band at two values (v4.0 7-12% vs KDR / Workbook REFERENCE / Doctrine s2 8-12%); also Ranking push, Launch, Harvest divergences; "(M7)" label misuse | Highest priority; reported as new conflict |
| AM-2 | Code-red trip at two values (v4.0 >2x or >1.5x for 2 validated weeks vs instruments ">1.5x band" no duration) | New conflict |
| AM-3 | No milestone tolerance | P11 records miss with $ value |
| AM-4 | No family taper sequencing / concurrency rule | P4 steps 2-3 |
| AM-5 | No slip-cluster count | P9 uses 2 |
| AM-6 | No taper slip tolerance (M3 "beyond tolerance") | P8 uses missed hold prediction |
| AM-7 | Stage entry/exit criteria in Criteria System v1.0 (March 2026), not held; T7 has one entry route and no Transition->Mature exit criteria | P13 hands decision up |
| AM-8 | No rank-guard cadence for a descent in V4 | P7 daily |
| AM-9 | No signal-to-start lag table | Duplicate of SOP-17/18/19 A-7 and SOP-30 AM-12 |
| AM-10 | Record retention (Ledger row 39 "Pending fold-in: retention policy lines") | Duplicate of SOP-29 / SOP-30 AM-13 |
| AM-11 | Gate numbering (G9/G10/G12) | Duplicate of C9 and SOP-29 / SOP-30 AM-11 |
| AM-12 | No horizon for expired push justification (SOP-28 P3.2) | P10 uses objective closure |
| AM-13 | RECOVERY scenario identifier S-R13 vs S-R12 in KDR and SOP-12 v2.0 s5 | Analogous to C12; new conflict |
| AM-14 | Concurrency of descent and open push on one product unstated | S-A3 only freezes new pushes at BREACH |
| AM-15 | No Transition-stage objective-mix target in O8 | P3 uses trailing baseline and Mature target |

### 10.2 Ledger conflicts referenced
C3 (#31 no procedural document), C9 (gate numbering), C10 (vocabulary stated at three counts across corpus), C12 (analogue for AM-13).

### 10.3 Version governance triggers
Monthly review and on any v4.0 increment (re-validate S-R6, S-R9, S-R10, S-R12, S-A1 to S-A9, S-E5, S-D1, T1, T2, T7, T8, R1, R3, O1, O7, O8, M1, M3, M6, M10, L1, L2, X12, X10, G2, G3, G6, G9, G10, G11, G12, D5, P5, P10, V1, V4). Specific: Transition band or deviation-class change; S-R6/T1 change; M3/L2 change; SOP-28 P5 change; SOP-24 P1 cause-class change; SOP-26 entry requirements change; D9 feed status change; any Appendix A item resolved.

### 10.4 Interface contracts (I-1 to I-19)
I-1 SOP-23 P6.3 taper handoff (highest consequence; two weeks at/under target with no handoff escalates to PPC Lead); I-2 T7 stage tag; I-3 O7 horizon expiries via T2 K7; I-4 #28 P5 ladder mechanics and exit targets (fallback: Max Profitable CPC as stated interim reference; D3 OPEN); I-5 dated rung instruction to SOP-12 P4 (staged Monday); I-6 #38 staged set and T+1; I-7 D9 daily rank (fallback: one rung per term per two windows); I-8 SOP-24 P1 cause classes; I-9 SOP-24 P2 recovery gate (absence = gate working); I-10 Brand Management event log (without it, guard holds rung, reversion waits); I-11 cleanup execution to #29 P3, SOP-12 P7, #28 P3.2; I-12 #30 P12 harvest continuity; I-13 floor register to SOP-26 P1; I-14 #41 economics to T0 C18:C24 (D1 OPEN); I-15 #32 event arming (unannounced live window escalates to deals owner); I-16 #33 family ownership; I-17 #37 automation rule suspension (no confirmation -> term leaves schedule); I-18 released spend to T0 zone H / A2; I-19 T6 predictions to V5 at #6.

### 10.5 Documents named but not present
Master PPC Decision Criteria System v4.0 (and v4.1 pending); Master PPC Decision Criteria System v1.0 (March 2026; Phase 1-4 model; not held); Keyword Decision Record Template v3.0; PPC Strategic Doctrine v1.0 (Sections 1, 2, 6.2); PPC Economics Worked-Example Set v1.0; SOP Build Kit v1.0; PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0 (READ ME, REFERENCE tab); PPC Cross-Reference Ledger; Supersession Map; SOP-12, -16, -23, -24, -26, -28, -29, -30, -32, -33, -35, -37, -38, -39, -41; #31 has no procedural document (C3).
