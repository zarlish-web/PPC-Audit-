# SOP-35 Digest: Incrementality Testing Operations

Source: `PPC_SOP_35_Incrementality_Testing_v2_0.pdf` (17 pages; the last footer also reads "Page 12 of 12", an extraction artifact). Digest of the plain-text extraction; nothing added beyond the text. Some tables were flattened in extraction and their columns were rebuilt from the content.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-35: Incrementality Testing Operations (Component #35 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | **The incoming operator decides and executes, with the PPC Lead reviewing**, per PPC Authority Matrix v2.0 Section 1 row "Incrementality tests" (Section 10 also cites matrix standing rule 4: the matrix records the Transition Brief's assignment on incrementality) |
| Supersedes | SOP-35 v1.0 (2026-07-24) in full |
| Thresholds | Every tolerance, window, band, gate and verdict lives in Criteria System v4.0 and KDR Template v3.0. Zero local thresholds |
| Size | 13 procedures (v1.0: 6); closed vocabulary quoted verbatim (v1.0: 6-row table); 4 worked examples (v1.0: 2); 12 failure modes (v1.0: 6); operator ramp; 12 interface contracts; 8 amendment items |

**Verdict / purpose.** Incrementality asks the one question that justifies mature and defensive spend: **what happens to TOTAL orders when this spend steps down.** It answers with **controlled step-downs reading total (organic plus paid) capture, never paid orders**, per v4.0 Section 4 rule **X12**. The test is "how the burden of proof gets discharged, in dollars, on a date". It is not research. The reader is the operator holding incrementality scope; someone who has never run a test should be able to execute P1-P13 from the page.

### Three corrections of substance at v2.0
1. All **six v1.0 verdict strings retired** (none in the KDR v3.0 closed vocabulary): OPEN TEST, RUNG HOLDS / NEXT RUNG, RESTORE + RECORD FLOOR, EXTEND WINDOW (once), VOID READ, RELEASE TO QUEUE / DEFEND FLOOR.
2. v1.0 release seam "released budget posts to #31 via the SOP-26 P5 pipeline" retired per Ledger conflict **C3**. It now routes to **SOP-26 P12 release verification**, posting to the instrument layer at **T0 zone H and Account Rollup tab A2**. At SOP-26 v2.0, P5 is the annual defense-cost read and P12 is the release pipeline.
3. Two v1.0 citations of non-existent v4.0 objects retired: the "v4.0 baseline window" (AM-2) and the class-calendar cadences (AM-5).
- Also: the SOP-24 citation is updated from P1 to **P3** per the attached SOP-24 v2.0.

### The two test classes (Section 1.1)
| Class | Covers | Step mechanics |
|---|---|---|
| **Class 1: rung tests** | Rank-sensitive entities: category terms holding rank, and **every E2-flagged term at rank 1-3** | One **#28-derived rung** per rule **M3** (**about 10% per week**), inside rule **L2** limits (**50% cap per change, $0.50 bid floor**). Category rank burns while it is measured; an off-cliff test destroys the position it is reading (F2) |
| **Class 2: branded zero tests** | **Branded defense classes only** | May test **to zero directly** (brand position does not decay like category rank). Executes as a **dated campaign state action** staged per #38, deployed at #12, **never as a bid edit**. Whether zero needs an explicit L2 per-change-cap exemption is ungoverned (AM-6) |

Both classes read **total capture vs a filed baseline over a 2-week window per rung** (rule X12 and scenario **S-D4**: "watch total capture 2 weeks"). **The 2-week capture window is the one governed duration in this document.**

### Why the test exists (Section 1.2)
- Strategic Doctrine v1.0 Section 13: step spend down and read whether total orders hold. This is the only honest test of whether a dollar buys incremental demand or rents demand already owned.
- v4.0 Section 3 family **F16**: the **E2 cannibalization estimate** compares expected organic capture at current rank against paid share of sales on the term. **The flag fires when paid share > expected paid share at that rank + tolerance.**
- Rule **X12**: spend above the discovered floor on flagged terms is "by definition rented, not earned".
- Scenario **S-A5** (Section 8.1): a **RENTING mature product** gets **taper-and-verify**, with the burden of proof flipped onto the spend.

## 2. Scope and boundaries (Section 1.3)

| Component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides test mechanic (X12), flag (F16, E2), scenarios (S-D4, S-A5, S-Y10), capture window, ladder math (M3), lever limits (L2), gates, verdicts. **The capture tolerance does not exist in v4.0** (AM-1), never a local number |
| #28 Placement and modifier | Owns rung derivation, ladder mechanics, exit-bid discovery, floor register format that **T4** implements. This SOP requests rungs and records floors through #28's format; never derives a step. Cited per Ledger row (v2.0, Wave 5A) |
| #12 Exact | Executes every campaign-level change: rung deployment confirmations, zero test's dated state action, restore deployments, **RE-POINT VARIATION on G6 RED** |
| **SOP-24 P3 (#24)** | Owns confound and void determination; publishes **five confound classes** consumed by name: **event or deal window (G10); competitor deal window (S-C5); price test (G9); listing change inside 14 days (family F4); adjacent-variation stockout (S-I6)**. This SOP hands windows in and receives classifications |
| **SOP-26 (#26), three seams** | **Inbound**: its **P2 step 6** issues INCREMENTALITY LADDER on an E2 flag, stages the rung, hands design and continue-or-restore call here (**its I-9**). **Outbound 1**: NON-INCREMENTAL findings route to its **P12 release verification**, which alone posts to the instrument layer. **Outbound 2**: its **P5 annual defense-cost read** consumes this SOP's P13 evidence package for the cannibalization-adjusted figure |
| #32 Deal/event windows | Owns event plans, arming, settle marks. This SOP applies G10 against #32 declarations and T5; never schedules around an assumed window length. Ledger row (v2.0, Wave 5A) |
| #33 Sibling arbitration | G11: no test arms on a shared term without the declaration |
| #38 Bulk deployment | Every rung, zero step, restore is a staged, reasoned #38 deployment; no window starts until its rung is proven landed |
| #37 Automation rules | This SOP declares frozen scope as an exclusion state and reads the rule change log; never edits a rule. A rule firing on frozen scope voids the read and the rule suspends pending #37 review |
| #6 V5 scoring | Owns rubric. This SOP files predictions (V1), scores (V5) in P1, hands voids with class refs so **a VOID is never filed as a MISS** |
| Instrument layer (M5 queue) | Releases post to T0 zone H and Account Rollup A2 **through SOP-26 P12 verification only**. No #31 procedure (C3). Never post directly (F10) |
| #41 economics | Margin refresh into T0 zone C (I-6) |

**Section 1.4:** no numeral is local. **Eight gaps** are logged; the first, the **X12 capture tolerance**, is "the single number this component is built around". A tolerance, window or cadence without a v4.0 heading or AM reference is a defect to raise.

## 3. Triggers (Section 2)
No per-trigger lag table in v4.0; lags anchored to rule **V4** daily/weekly/quarterly slots (AM-7).

| Trigger | Signal and detecting artifact | Max lag | Procedure / authority |
|---|---|---|---|
| E2 flag handoff | SOP-26 P2 step 6 stages INCREMENTALITY LADDER on a branded or rank 1-3 term. Artifact: staged rung in #38 format + T6 entry with review date (SOP-26 I-9) | One weekly cycle | P1, P4. S-D4 governs; the rung is theirs, the read is this SOP's |
| Product RENTING flag | **T0 zone E flywheel row**: ad share rising while organic share falls **3+ weeks** on a **Mature** product. Artifact: **F2 directional flag** read at SOP-26 P1 step 7 | One weekly cycle | P1 batch under S-A5: all rank 1-3 and branded terms of the product |
| Syntax RENTING | Ad dependency rising vs declared organic-share target on a primary syntax. Artifact: **T1 syntax board organic-share columns** vs declared target | One weekly cycle | P1 batch under **S-Y10**: syntax's rank-held terms; **M8 defense budget** binds the syntax until organic share recovers |
| Quarterly floor re-test on flagged term | **T4 "Next Step Date"** reaches date on an E2-flagged term. Artifact: T4 **"Discovered Floor $", "Ladder State (step / date)", "Next Step Date"** | One weekly cycle | P1. Rule M3: on E2-flagged terms the taper doubles as the incrementality test (X12); V4 sets floor re-tests quarterly |
| Structural re-open | **T5 Product Log** event on a tested entity: price move, listing/image/A+ change, competitor entry. Artifact: T5 event types (**closed list of 8**) with affected keywords | One weekly cycle | P1 re-open (carried from v1.0 Section 2) |
| Capture-window expiry | A rung's 2-week window closes. Artifact: T6 review date on the rung's prediction row | Same cycle | P7, then P9 where SOP-26 holds the rung |
| Confound signal | T5 entry, #32 arming notice, or #37 rule-log entry inside an open window. Artifacts: T5 trend-exclusion flag, #32 armed-window declaration, #37 rule change log | Same day | P8 via SOP-24 P3; G10 computes guard end; read restarts clean |

## 4. Procedures

### Preconditions (Section 3.1): T7 manifest, with the LIVE state
**Live: T7 packet completeness score 0.571, below the 85% DEGRADED floor of gate G8.** Conclusions on affected rows cap at flags; every design states the manifest state on its face.

| T7 field group | Live status | Requirement / suppression |
|---|---|---|
| **A1** Four-period comparability (L30/P30/B30/L60) | **MISSING** | Every baseline states the single-window limitation; **X8 trajectory read at P7 Branch C runs on WoW block only** |
| **B8** Row economics (BE chain) | **PRESENT (blended)** | T0 zone C cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC. **D1 per-variation margin PARTIAL**, so every ceiling-referencing statement carries **G9 PROVISIONAL** |
| **B11** Market context (SQP shares) | **PRESENT** | Organic-capture estimate limb of E2 (expected organic capture from **SQP click curves**, F16). One row on benchmark fallback lowers **E7 confidence** per rule **D3**; record names the source |
| **D7** Decision log and V5 | **PRESENT** | T6 with review dates and scores |
| **D9** Daily rank series | **PARTIAL (head terms)** | Rank-sensitive rung tests legal only where D9 covers the term; elsewhere weekly **K4** block, coarser grain stated |
| **D8** Competitor depth | **MISSING** | Competitor deal-window confound visible only via manually logged T5 competitor entries; every read states the gap (Ledger dependency **D4 OPEN**) |
| **B9** WoW deltas | **PARTIAL** | Substitutes for A1 trend context; fills from cycle 2 |

### Gates in force (Section 3.2; v4.0 numbering, C9 alias at first use; schemes never mixed in a reason string)
| Gate | Observable on a test entity |
|---|---|
| **G1** Validation quarantine | T2 zero-flag column Clean on every row in scope. Mid-test fire removes the row, voids its window with **no confound class**; verdict QUARANTINE: DATA REFRESH with owner and date |
| **G2** Sample sufficiency | T2 "Sample State" adequate for rate reads. Capture read is order-count arithmetic, but any CVR statement obeys the **100-click limb** |
| **G6** Inventory adequacy | T2 "Inventory Band" GREEN or YELLOW. **RED aborts same day**, routes RE-POINT VARIATION to #12; OOS is simultaneously a SOP-24 P3 confound for adjacent reads |
| **G8** Packet completeness | T7 score stated on design and conclusion; DEGRADED (0.571) caps conclusions to flags per rule **P8** |
| **G9** Price stability (alias: margin freshness) | No price change on targeted variation in **trailing 7 days** (T5 filtered to price moves), or test start moves past the price window and CVR-adjacent reads carry PROVISIONAL. Record says which reading fired |
| **G10** Event exclusion (alias: G12 event freeze) | No armed/guarded event window overlaps a baseline or read window: **event weeks + 14 days following** excluded. From #32 declarations and T5 trend-exclusion flag; **guard end computed to a date** |
| **G11** Sibling conflict | Family ownership declared per #33 on any shared term before arming. No declaration, no test |
| **G12** MKL hygiene | Every tested term in current MKL with syntax tag and relevancy; untagged goes to MKL maintenance first |

Run cadence: P1-P2 weekly in the Monday cascade; P3-P6 per test; P7-P9 per rung window; P10-P11 per conclusion; P12 weekly scoring + quarterly backlog; P13 annually per primary syntax. First executions take roughly double the time.

### P1. Candidate intake and the test register (25 min weekly)
1. Open the **test register** (held with the product Command Workbook **beside T6**). **Score last cycle first**: T6 rows whose review dates land this cycle get V5 HIT / PARTIAL / MISS / WRONG-DIRECTION (V1).
2. **Source 1, E2 flags**: filter T2 to rows whose **block K6 E2 estimate** fires the flag. On branded and rank 1-3 terms the flag arrives through SOP-26 P2 step 6 with the staged rung and INCREMENTALITY LADDER; enter with handoff reference.
3. **Source 2, product RENTING**: T0 zone E flywheel row RENTING (family F2) means batch entry under **S-A5**: every rank 1-3 and branded term, each its own row with S-A5 reference.
4. **Source 3, syntax RENTING**: S-Y10 on a primary syntax means the syntax's rank-held terms as a batch. Record that **M8 defense budget** is the binding syntax ceiling (the number is **T1 group S7's**); #26 with the instrument layer enforces it.
5. **Source 4, defensive classes**: every class in the **SOP-26 P4 defended-set declaration** with **no capture evidence on file in the trailing year** (because SOP-26 P5 subtracts E2-flagged spend from its numerator). Companion to SOP-26's F4.
6. **Source 5, quarterly floor re-tests**: T4 "Next Step Date" on an E2-flagged term (M3 doubling).
7. **Source 6, structural re-opens**: T5 event (price move, listing/image/A+ change, competitor entry) on a concluded entity re-opens its test with the T5 reference.
8. **Register row schema**: entity (term or campaign class); class (rung or zero); source reference (scenario ID, SOP-26 handoff, T4 date, or T5 event); entry date; **state (QUEUED / DESIGNED / ARMED / READING / VOID-RESTART / CONCLUDED-UNACTED / CLOSED)**; owner; review date. **No source reference = does not enter** (flag- and trigger-driven, never curiosity-driven). State names are register vocabulary, not verdicts (AM-8).

### P2. Testing calendar and slotting (15 min weekly, same pass)
1. Two sequencing rules: **one variable per entity** (a second test on the same entity queues behind the first); **one test per family** (two open tests sharing an **Account Rollup A1 Family Boards grid** confound each other; v1.0 F3).
2. Priority: **SOP-26 handoffs first**; then S-A5 and S-Y10 batches; then M3 doublings on T4 dates; then defensive-class candidates; then re-opens. **Ties break by weekly spend at the tested level, descending.**
3. Governed anchors: floor re-tests **quarterly** (V4); protected terms review **quarterly** (**S-D6**). Retired ungoverned cadences: v1.0's semi-annual on branded classes and annual per term cohort (AM-5). P12 backlog review guards against never-testing.
4. Nothing tests continuously: an entity past designed windows without conclusion = **F6**.
5. Write slot decisions into the register with dates.

### P3. Baseline construction (20 min per test)
1. The baseline artifact files **before any rung deploys** and carries: total orders/week on entity from all sources; paid split (orders, spend, clicks, CPC) by campaign from **T2 child rows (block K5)**; organic rank series (**K4**, daily link where D9 covers); share context from **K3** (SQP brand purchase share, benchmark source named per D3); economics snapshot from **T0 zone C** with margin table version and G9 state.
2. Total-orders source by class:
   - **Product-scope zero tests**: weekly product orders from the **SellerBoard figure in T0 zone B** (validated; never a console estimate).
   - **Term-scope rung tests**: term total capture = paid orders from **K5 cross-type totals** + organic estimate from E2 machinery (expected organic capture at current rank from SQP click curves, F16), labelled as an estimate with benchmark source.
3. Clean-window check: no event week, no post-event guard. Read T5 for deal windows, cross-check #32 settle marks, apply G10 (+14 days). Event-week baseline = **F7**. If recent history is wall-to-wall events, the baseline waits.
4. Baseline length: **v4.0 defines none** (AM-2); state the window on the artifact as an input under test, built from whole validated weeks. A1 MISSING means state the single-window limitation.
5. No rung deploys until the P4 prediction is filed against this baseline.

### P4. Test design and prediction (25 min per test)
1. **One variable**: one campaign or one term class stepped; everything else on the entity freezes.
2. Class selection: rank-sensitive = rung at M3 step inside L2; branded defense = may zero; anything else designing to zero = **F2**, restored on discovery.
3. Capture window per rung = **2 weeks** (X12, S-D4).
4. Prediction (V1 and Section **13.2** record contract): named metric (**total orders on the entity**), direction (**holds**), magnitude (the design's **stated hold bound**, plus a **stated rank bound** on rung tests), horizon (2-week window), review date. The hold bound is an **input under test** (AM-1): never presented as a threshold, never reused across designs without restatement; every conclusion states the bound it was read against (F12 otherwise).
5. **Design packet**: entity and class; baseline reference; stepped variable with prior and proposed values; rung schedule with dates; prediction; confound watch list (the **five SOP-24 P3 classes**, named); the restore rule quoted from X12 ("on a capture drop, restore and record the defended value"); abort conditions (**G6 RED, G1 quarantine, G4 eligibility flip**).
6. Zero-test specifics: dated campaign state action (budget to zero or paused for the window), staged per #38, executed at #12, **resume value recorded**. It is a designed test step, **not PAUSE (LEVERS EXHAUSTED)**.

### P5. Ownership, gate clearance, freeze (15 min per test)
1. **G11 first** on any shared term: #33 declaration before arming; otherwise escalate to #33 and the flag owner's rung holds.
2. Read gates from **T0 zone D strip** and **T2 flag columns**: G1 Clean; G2 for rate statements; G6 GREEN/YELLOW; G8 stated; G9 clear or start moves; G10 clear across every planned window; G12 MKL current.
3. **Declare the freeze**: no bid, budget, modifier, negation, or structure change on frozen scope except designed steps. Freeze list into register row and T6.
4. **Exclusion notice to #37**: declare frozen scope to the automation rule register. Mid-test rule change on frozen scope voids the read; the rule suspends pending #37 review.
5. Register row to **ARMED** with first rung date.

### P6. Rung staging and deployment (10 min per rung)
1. Rung value from **#28 mechanics** (zero tests: the designed state action). Never derive a step; without the derived value the window moves out.
2. Stage per #38 with the **four-segment reason string**: (a) verdict string verbatim **INCREMENTALITY LADDER**; (b) v4.0 scenario reference (**S-D4**, or S-A5 / S-Y10, or the M3 doubling); (c) **this SOP and procedure number**; (d) **test register reference**. Missing scenario reference = does not deploy.
3. Deploy on rung date; read the **#38 T+1 verification diff** next day. Unlanded rung = window not started; re-date from landed day.
4. Write the rung into T6 with V1 prediction fields; register row to **READING**.

### P7. The capture read at each rung (20 min per read)
1. At window close: **total orders on the entity across the window's validated weeks** beside the baseline, as a **level and a percentage**. Paid orders and spend are the mechanism, never the answer (citing paid metrics = **F1**).
2. Rung tests: read the rank axis (K4; daily where D9). **Capture hold with rank sliding past the stated rank bound classifies as a drop.**
3. Run the **P8 confound sweep before classifying**; classify only after SOP-24 P3 returns clean.
4. Four-branch tree:

| Branch | Condition | Resolution |
|---|---|---|
| **A. Capture holds** | Total capture inside stated bound **and** rank inside its bound | Spend at the tested level was non-incremental. Rung holds; ladder proceeds to next rung (X12: ladder continues, floor recorded). Held rung registers in **T4** via #28 format with test reference |
| **B. Capture drops** | Total capture past bound, **or** rank past its bound | Incremental spend confirmed. **Restore one rung** (X12: restore and record the defended value). Incremental floor records at restored level in T4 with test ref; standing verdict **DEFEND AT FLOOR** |
| **C. Ambiguous** | Inside bound but deteriorating across window (**X8 trajectory**) | No v4.0 extension allowance (AM-4; v1.0 single-extension retired). Design's own review date governs; ambiguity stated; where trajectory runs against prediction, conservative execution is **Branch B restore** per X8's one-step-conservative rule |
| **D. Void** | Confound inside window per P8 | Read restarts clean after G10 guard; register **VOID-RESTART** with class. **The rung does not move** (no evidence either way) |

5. Score the rung's prediction in T6 at the read. **A VOID is a VOID, never a MISS.**
6. Repeat P6-P7 until a Branch B restore, a designed stop, or the **L2 floor value** ($0.50); never step below it.

### P8. Confound watch and void protocol (10 min per read + same-day handling)
1. Watch across every open window (not only at close): T5 entries in the five SOP-24 P3 classes; #37 rule log vs frozen scope; #32 arming notices.
2. D8 MISSING: competitor deal-window class visible only via manual T5 competitor entries; every read states the gap.
3. Confound inside an open window means VOID per SOP-24 P3 (owns the determination). Rung does not move on a void.
4. Compute guard end explicitly (event week + 14 days per G10); re-date the window; register VOID-RESTART with class and T5 refs.
5. Hand the void to **#6** so the score files as VOID.
6. **Never hand a confounded read forward as clean.** SOP-26 I-9 calls it the worse failure (F8; WE-3 incident).

### P9. The continue-or-restore call (15 min per call)
1. For tests riding an SOP-26 rung (P2 step 6 handoff or P3 quarterly doubling), the call returns to SOP-26 at end of the 2-week window (its I-9): **CONTINUE** (capture held; ladder proceeds; SOP-26 records floor at held rung) or **RESTORE** (capture dropped; SOP-26 restores and records defended value).
2. Call carries: window dates, baseline reference, capture arithmetic, rank axis, bound read against, SOP-24 P3 determination.
3. Confounded window: the call is the void with class refs, never a reading; SOP-26 holds the rung, no floor recorded; re-dated window returns.
4. Lands **same cycle the window closes**, on the V4 weekly anchor. Late call leaves counterpart's rung undated past review (its F9 exposure; AM-7).

### P10. Conclusion and finding record (20 min per test)
1. Exactly one finding class: **NON-INCREMENTAL AT THE TESTED LEVEL** (capture held at final held level; **finding value per week = pre-test spend - held-level spend**) or **INCREMENTAL FLOOR** (a Branch B restore; floor value with test reference). Register vocabulary, not verdict strings.
2. Finding files with: entity; class; rung history with dates and T+1 confirmations; capture arithmetic per rung; bound(s); confound record; **finding value in $/week**; acted consequence (P11 routing or T4 record).
3. INCREMENTAL FLOOR: record in **T4 ("Discovered Floor $", "Ladder State (step / date)", "Next Step Date")** via #28 format, with a **context note naming the test and the market state**. Standing verdict DEFEND AT FLOOR; next quarterly date per V4.
4. NON-INCREMENTAL: value routes per P11. Entity's standing state = stage verdict, commonly **HOLD; DEFEND LIGHTLY AT RANK** on a held mature term.
5. Restoration verification: #38 T+1 diff on the restore + next validated week's rank read vs pre-rung position. "A restore without verification is a bid with a label."
6. Register row to **CONCLUDED-UNACTED** until P11 routing or T4 record lands, then **CLOSED**. CONCLUDED-UNACTED is hunted by P12.

### P11. Release integration (10 min per finding)
1. A NON-INCREMENTAL finding is a **candidate release, not a posting**. Hands to **SOP-26 P12** (verification on rank and share axes, withheld-portion split); the verified difference posts to **T0 zone H and Account Rollup A2**.
2. **Never post to the queue directly**. SOP-26's recorded harvest case: **41.8% of a raw monthly release was money buying shelf presence**; unverified posting over-subscribes M5 and surfaces as a failed push (F10).
3. Entities outside the mature defended set route through the product's **harvest-read owner** with the same verification demand (M5 funds from landed savings only; Doctrine Section 12).
4. Write routing into T6 and the register row.

### P12. Scoring, calibration, quarterly backlog review (45 min quarterly + weekly scoring in P1)
1. Weekly scoring per V1. Rule-level accuracy per **V5**: **a design pattern below 50% accuracy over 10 or more scored predictions enters review**, which produces an amendment, a change proposal, or a documented defense.
2. Calibration: a MISS on a hold prediction re-weights the register priority toward classes whose predictions miss.
3. Quarterly (V4 framework-review slot): sweep for **CONCLUDED-UNACTED** rows and entities past designed windows (F6). Quantify each unacted finding in **$/week**; the total is the review headline. **F5 escalates here** (WE-4: $2,099.50 on three rows).
4. Reconcile register vs **T4** (every INCREMENTAL FLOOR has a floor row) and vs **T0 zone H** (every routed release reached SOP-26 P12 or is dated in its queue).

### P13. Annual defense-read feed (30 min annually per primary syntax)
1. SOP-26 P5 subtracts E2-flagged spend from the defense-cost numerator and states the adjusted figure beside raw. Package per defended syntax: trailing-year findings (class, tested level, value, dates), current T4 floors with test references, open register rows.
2. Lands **before the SOP-26 P5 read date** (trigger is SOP-26's Element 2 row). A defended syntax with no capture evidence re-enters P1.

## 5. Rules, thresholds and numbers

| Value | Meaning | Source |
|---|---|---|
| **2 weeks** | Capture window per rung; the one governed duration | X12, S-D4 |
| **About 10% per week** | Rung step size | M3 |
| **50% per change; $0.50 bid floor** | Lever limits; ladder never steps below the floor | L2 |
| Rank 1-3 | E2-flagged rank-sensitive scope / S-A5 batch scope | Section 1.1 |
| **3+ weeks** | Ad share rising while organic share falls, Mature product, so RENTING | T0 zone E / F2 |
| E2 flag | Paid share > expected paid share at rank + tolerance | F16 |
| Quarterly | Floor re-tests (V4); protected-term review (S-D6) | |
| **0.571** | Live T7 packet completeness | T7 |
| **85%** | DEGRADED floor | G8 |
| **7 days** | Trailing price-change window | G9 |
| **14 days** | Post-event exclusion; listing change inside 14 days confound (F4) | G10; SOP-24 P3 |
| **100 clicks** | G2 limb for CVR statements | G2 |
| **< 50% accuracy over >= 10 scored predictions** | Design pattern enters review | V5 |
| Trailing year | Defensive class with no capture evidence enters intake | P1 step 5 |
| Closed list of 8 | T5 event types | T5 |
| Five | SOP-24 P3 confound classes | SOP-24 P3 |
| 41.8% | Share of a raw release buying shelf presence (SOP-26 harvest case) | P11 |
| Finding value/week = pre-test spend - held-level spend | NON-INCREMENTAL value | P10 |
| Hold bound / rank bound | **Design-stated inputs under test** (no v4.0 value) | AM-1, AM-3 |
| Target 50% / Max Acceptable 75% of break-even | Via the example base (17.5% / 26.3% of 35.0%) | Examples |
| Week 4 audit | Branch misclassification returns operator to week-2 supervision on P7 only | Section 11.3 |

### v4.0 IDs referenced
| ID | As described |
|---|---|
| X12 | Controlled step-down reading total capture; "if total capture (organic + paid) holds within tolerance for 2 weeks"; spend above discovered floor on flagged terms is rented; restore on capture drop and record defended value |
| X8 | Trajectory read; one-step-conservative rule (Branch C) |
| X9 | Listed among companions |
| F16 / E2 | Cannibalization estimate and flag |
| E7 | Confidence lowered by benchmark fallback (D3) |
| F2 (family) | Product State; RENTING flywheel flag |
| F3 (family) | Pre-OOS snapshot (one of only two baselines v4.0 defines, with the T5 recovery baseline) |
| F4 (family) | Listing change inside 14 days confound |
| S-D4 | Branded/rank-held incrementality: watch total capture 2 weeks |
| S-D6 | Quarterly protected-term review |
| S-D1 to S-D6 | Defense scenarios (companion list) |
| S-A5 | RENTING mature product: taper-and-verify, burden flipped |
| S-Y10 | Syntax RENTING; M8 defense budget binds |
| S-C5 | Competitor deal window |
| S-I6 | Adjacent-variation stockout |
| M3 | Rung step ~10%/week; on E2-flagged terms taper doubles as incrementality test; "on slippage beyond tolerance, restore one step" (no numeral) |
| M8 | Defense budget (T1 group S7 "Defense budget $") |
| L2 | 50% per change, $0.50 floor |
| L9 | RE-POINT VARIATION execution at #12 |
| G1, G2, G4, G6, G8, G9, G10, G11, G12 | Gates as above (G4 eligibility flip is an abort condition) |
| P8 (precedence) | Data quality beats test calendar; DEGRADED caps to flags |
| D2, D8 | Chronic conversion failure; a fix running (PAUSED-PENDING boundary) |
| D3 | Benchmark source naming / confidence |
| O5 | Paused state with re-entry criterion |
| V1, V4, V5 | Prediction contract; cadence slots; scoring/accuracy |
| 13.1, 13.2 | Closed verdict vocabulary (18-string list); record contract |

### Verdict mapping (Section 5; KDR v3.0 25-string closed vocabulary; v4.0 13.1 has 18 strings)
| KDR verdict | Execution here |
|---|---|
| **INCREMENTALITY LADDER** (no identical v4.0 string; nearest DEFEND AT FLOOR, "Branded/held term at discovered floor; incrementality-tested where flagged") | Entry verdict, **issued by the flag owner** (SOP-26 P2 step 6 on S-D4; batch under S-A5, S-Y10), **never by this SOP**. Received, designed P4, read P7, returned P9 |
| DEFEND AT FLOOR | Branch B outcome; restore instruction in P9 call or P10 finding; #28 mechanics / #12 execute |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN (v4.0: TAPER TO FLOOR (POST-OBJECTIVE)) | State a Branch A continuation rides when the test doubles an M3 taper; this SOP supplies capture evidence |
| HOLD; DEFEND LIGHTLY AT RANK | Standing state after NON-INCREMENTAL on held mature term; SOP-26 owns posture |
| QUARANTINE: DATA REFRESH (v4.0: FLAG: DATA REPAIR) | G1 fire removes row, voids window with no confound class; refresh task with owner and date |
| RE-POINT VARIATION | G6 RED aborts test same day; #12 per L9; OOS is confound for adjacent reads |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Boundary: click-quota is for traffic tests (Doctrine 13); incrementality windows are dated, not click-counted. Never issued here |
| STOP-LOSS: CONCEDE OR DEFER | Boundary: a test takes no stop-loss; a live push inside proposed scope is a one-variable violation (test waits or scope narrows) |
| PAUSED-PENDING (REASON + RE-ENTRY) | Boundary: entity blocked (D2 chronic conversion failure, D8 fix running) waits under its O5 state |

**Campaign-level subset (5.1, KDR "Campaign Decision Record" tab):** FUND / HOLD / TRIM BUDGET; RAISE / CUT MULTIPLIER; NEGATION PASS; CONSOLIDATE; RETAG OBJECTIVE; PAUSE (L7); ARCHIVE. Inside frozen scope: RAISE/CUT MULTIPLIER and TRIM BUDGET barred except as designed steps; NEGATION PASS defers to window close unless it is a #29-prescribed pre-load riding a structure event outside frozen scope; the zero test is a designed budget/status action, not PAUSE (L7).

## 6. Data inputs required
- **T0 PRODUCT COMMAND**: **zone B** (weekly validated spend, sales, orders from the **SellerBoard** read; product total orders for zero tests); **zone C** named cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, margin version, G9 state; **zone D** gates strip; **zone E** flywheel row (RENTING; ad share vs organic share); **zone H** (M5 queue, post-verification).
- **T1 SYNTAX BOARD**: organic-share columns vs declared target; **group S7 "Defense budget $"**.
- **T2 KEYWORD COMMAND**: **K2** (Inventory Band, Event Mode, family conflict state); **K3** (SQP brand purchase share, benchmark source); **K4** (organic rank series, daily link, pre-OOS baseline); **K5** (cross-type totals, campaign child rows paid split: orders, spend, clicks, CPC; WoW block; zero-flag column); **K6** (E2 estimate, Max Profitable CPC, Expected CPC); "Sample State"; T2 flag columns.
- **T4**: "Discovered Floor $", "Ladder State (step / date)", "Next Step Date" (floor register via #28 format).
- **T5 PRODUCT LOG**: event types (closed list of 8), trend-exclusion flag, price moves, listing/image/A+ changes, competitor entries (manual), deal windows.
- **T6 DECISION LOG**: review dates, V5 scores, predictions.
- **T7 MANIFEST**: A1, B8, B9, B11, D7, D8, D9 statuses; packet completeness score.
- **Test register** (beside T6 in the product Command Workbook).
- **Account Rollup Workbook**: A1 Family Boards grid (one-test-per-family); A2 (posting after verification).
- **SQP click curves** (organic capture estimate); **SellerBoard** weekly validated totals (Monday 06:00; workbooks 09:00).
- **D1 per-variation margin** (PARTIAL).
- **#32** armed-window declarations and settle marks; **#37** rule change log; **#38** T+1 diff; **SOP-26 I-9** handoff channel and P4 defended-set declaration; **SOP-24 P3** determinations; **#33** declarations; **#41** margin refresh; **#28** rung derivations; MKL.

## 7. Outputs / artifacts

| Event | Record | Storage | Retention | Consumer |
|---|---|---|---|---|
| Intake/slotting (P1-P2) | Test register (entity, class, source ref, state, dates, owner) | Register block with product Command Workbook beside T6 | Append-only log life | P12; weekly cascade; SOP-26 handoff reconciliation |
| Baseline (P3) | Totals, paid split, rank series, share context, economics snapshot, clean-window statement | With register row; sources T0 zone B/C, T2 K3-K5 | Life of test chain | Every P7 read; #6 |
| Design (P4-P5) | Design packet with V1 prediction, freeze list, confound watch list, abort conditions | Register row + T6 prediction entry | Life of test chain | #38; #37 exclusion; checkpoint holder |
| Rung (P6) | Staged set with four-segment reason string; T+1 diff | #38 format; T6 | Append-only | #38 verification; window clock |
| Read (P7-P8) | Capture read with branch; void records with class and T5 refs | T6; register state | Life of test chain | P9; #6; SOP-24 P3 round-trip |
| Call (P9) | Continue-or-restore call (window dates, arithmetic, bound, determination) | SOP-26 I-9 channel; copy in T6 | Life of test chain | SOP-26 P2/P3 |
| Conclusion (P10) | Finding record (class, rung history, values, acted consequence) | Register row; T4 for floors (#28 format) | Life of the term in the register | SOP-26 P12; #28 / T4; P13 |
| Routing (P11) | Release handoff with finding value and evidence | T6; SOP-26 P12 intake | Append-only | SOP-26 P12; T0 zone H and A2 after verification |
| Review (P12) | Quarterly backlog review with theater total $/week | T6, filed against register | Append-only | PPC Lead; v4.1 amendment path |
| Defense feed (P13) | Evidence package per defended syntax | Filed against T1 group S7's syntax | Annual; superseded by next | SOP-26 P5 |

No v4.0 retention rule exists (AM-8). Alarm routing: same day to operator queue **F2, F8, F10** plus any G1/G6 abort; weekly worklist **F1, F4, F7, F9, F11, F12**; to PPC Lead with register history **F3, F5, F6** and any mode recurring in consecutive cycles. Evidence line: entity, signal value, v4.0 rule/gate ref, artifact where read.

## 8. Decision rights
- **"Incrementality tests"** row: **incoming operator decides and executes; PPC Lead reviews; CEO and BM owner informed.**
- Human-mandatory: **every test arming, every zero test, every restore instruction, every finding routing, every void notification**; every staged deployment confirm ("Bulk deployments (#38)": PPC Lead reviews, operator executes); any test touching a shared defended term ("Sibling declarations (S-series)": PPC Lead decides, BM owner reviews) via #33; release posting is never this skill's action ("Push funding (the M5 queue)": CEO above envelope, PPC Lead within).
- "Weekly verdicts (established US)": PPC Lead decides, operator executes assigned scope, BM owner reviews in daily huddle (review, not veto).
- Vacancy rule: D reverts to PPC Lead, E to PPC Manager.
- AI-executable with audit: register upkeep and scoring, baseline assembly, design drafting, capture arithmetic, branch drafts, void detection drafts, call drafting, finding drafts, backlog quantification, P13 package.
- **SOP-24 P3** decides confound/void classification; **SOP-26** issues INCREMENTALITY LADDER and executes restore/floor; **SOP-26 P12** decides what release is real; **#28** derives rungs; **#12** executes.
- Escalation: F2 same day with rank cost; F8 on discovery to every consumer; F10 on discovery; F5 at quarterly review with dollars; any mode recurring in consecutive cycles on same scope to PPC Lead.
- Ramp: Week 1 reproduce a closed test's capture computation and trace a T4 floor; walk the five confound classes; observe a Monday cascade and BM huddle. Week 2 supervised: design one rung test and one zero test, one historical read, one void with G10 guard-date computation, stage one rung, draft one finding with routing, one G11 check. Week 4 unsupervised with audit: own register, one full test to CLOSED, one void end to end, one backlog sweep.

## 9. Account-specific facts
- **Live T7 packet completeness 0.571** (below 85% DEGRADED): conclusions cap at flags.
- Live T7 statuses: **A1 MISSING; B8 PRESENT (blended); D1 per-variation margin PARTIAL; B11 PRESENT; D7 PRESENT; D9 PARTIAL (head terms); D8 MISSING; B9 PARTIAL (fills from cycle 2).**
- Ledger dependency **D4 OPEN** (competitor depth).
- The account's **one dated incident** touching this component (recorded in the **SOP-26 v2.0 rebuild's worked cases**): a quarterly probe on a defended head term whose capture window contained **two competitor deal windows**. The read was voided and re-run clean; it is the origin of the interface clause "a confounded read handed over as clean is worse than no read" (F8, WE-3).
- **SOP-26 recorded harvest case: 41.8% of a raw monthly release was money buying shelf presence.**
- The anonymized live product economics spine was **not attached**; examples use the fictional base: AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3%, CVR 5.2%; Max Profitable CPC $1.46.

### Worked examples (illustrative)
- **WE-1 branded zero test**: brand exact defense $84.00/week, CPC $0.75, 112 clicks, 31 paid orders (27.7% CVR). Baseline 212 total orders/week (SellerBoard, T0 zone B); brand organic position 1. Bound: 3.0% fall. Read: total 210/week (-2, **0.94%**), position 1; organic absorption 29/31 = **93.5%**. NON-INCREMENTAL: **$84.00/week, $4,368.00/year**; routes to SOP-26 P12; HIT.
- **WE-2 rank-3 rung test**: floor $1.90; Max Profitable CPC $1.46 ($0.44 over). Baseline 41 total orders/week (14 paid, 27 organic estimate per K3); 269 paid clicks; spend $511.10. Rung $1.71 (10.0%). Bound 5.0% fall, rank 3-4. Read: 37.3 (-9.0%), rank toward 5. Branch B. Saving 269 x $0.19 = $51.11/week vs contribution lost 3.7 x $28 = $103.60; net **-$52.49/week**; ratio **2.03**. Restore to $1.90; floor recorded; DEFEND AT FLOOR; MISS.
- **WE-3 confounded window**: floor $2.24, rung $2.02 (9.8%); two competitor deal windows on top-10 holders in T5; SOP-24 P3 classifies S-C5, VOID for both rank and capture reads. Re-run clean: Branch A; floor $2.02 with context note. Premium over $1.46 falls from $0.78 to $0.56; at 30 maintenance clicks/week, $23.40 to $16.80 = **$6.60/week, $343.20/year**.
- **WE-4 backlog**: three CONCLUDED-UNACTED rows over a 13-week quarter: $84.00 (branded, unrouted) + $47.50 (defensive complement-PAT class, unrouted) + $30.00 (unwritten floor: bid $2.10 vs proven $1.85 x 120 clicks) = **$161.50/week; $2,099.50/quarter**. Unrouted releases total $131.50/week (quiet direction); unwritten floor is the loud direction.

## 10. Open items

### Amendment register (Section 10.3, 8 items)
| ID | Gap |
|---|---|
| **AM-1** (highest) | **Capture tolerance**: X12 "holds within tolerance for 2 weeks" has no numeral anywhere in v4.0. Each design states its own bound as input under test |
| AM-2 | Baseline window: no "v4.0 baseline window" exists (only baselines: F3 pre-OOS snapshot and T5 recovery baseline) |
| AM-3 | Rank-slip tolerance: M3 "slippage beyond tolerance, restore one step" has no numeral (likely duplicates ladder-owning sessions) |
| AM-4 | Ambiguous-read rule / extension allowance (v1.0 one extension retired; Branch C on X8) |
| AM-5 | Standing re-test cadence per class (v1.0 semi-annual branded / annual per cohort retired) |
| AM-6 | Zero-test step-size exemption from L2 50% cap |
| AM-7 | Lag table (per-trigger and per-call lags); echoes a prior format-playbook session's Element 2 gap |
| AM-8 | Record retention + register-state vocabulary admission (QUEUED ... CLOSED); retention duplicates prior sessions' items |

### Conflicts / dependencies
- **C3** (#31 no procedures; release via SOP-26 P12); **C9** (gate numbering); vocabulary count conflict (KDR 25 vs v4.0 13.1's 18 strings).
- **D4** OPEN (D8 competitor depth feed).
- #28, #32 cited by Ledger row (v2.0, Wave 5A rebuild); v1.0 procedure numbers not cited.

### Gaps / references not present
- Live economics spine not attached.
- D8 MISSING, A1 MISSING, D9 PARTIAL, D1 per-variation margin PARTIAL.
- Referenced documents: Master PPC Decision Criteria System v4.0; KDR Template v3.0 (incl. "Campaign Decision Record" tab); PPC Strategic Doctrine v1.0 (Sections 12, 13); Master PPC Data Architecture v1.0 (Sections 4, 6, 8, 9, 11); PPC Authority Matrix v2.0; **PPC Economics Worked-Example Set v1.0 case E5** (premium arithmetic reused in WE-3); Transition Brief; Cross-Reference Ledger; SOP-6, 12, 24 (P3), 26 (P1 step 7, P2 step 6, P3, P4, P5, P12, I-9, Element 2), 28, 29, 32, 33, 37, 38, 41.

### Version-governance triggers (10.1)
Any v4.0 increment (re-validate X12 and its window, S-D4, S-A5/S-Y10 conditions, M3 doubling sentence, Section 5 gate set); AM-1 landing (re-opens every open design that day); #28 ladder/register-format change; SOP-24 P3 confound-class change; SOP-26 P2 step 6 / I-9 / P12 change; D8 landing or full D9 coverage; every quarterly P12 review that finds theater.

### Interface contracts (12)
| ID | Counterpart | Non-arrival |
|---|---|---|
| I-1 | SOP-26 upstream (INCREMENTALITY LADDER handoff: staged rung, T6 entry, E2 evidence) | Nothing arms; P1 reconciliation catches a rung running without a design and returns it |
| I-2 | #28 upstream (rung derivation, floor register format) | Rung does not stage; window moves out; counterpart re-test date inherits the slip |
| I-3 | SOP-24 P3 upstream (confound/void determination) | No read classifies; window holds open with gap stated |
| I-4 | #32 upstream (armed-window declarations, settle marks) | G10 cannot apply prospectively; retrospective T5 scan voids; each preventable void recorded as an I-4 miss |
| I-5 | #33 upstream (ownership declaration) | Test does not arm; escalate to #33 |
| I-6 | #41 economics upstream (monthly and on event) | Ceiling statements carry G9 PROVISIONAL; capture arithmetic continues |
| I-7 | Data Operations upstream (SellerBoard totals to T0 zone B, Mon 06:00 / 09:00) | Week not validated; windows extend to next validated week; no console estimates |
| I-8 | #38 both directions (staged sets / T+1 diff) | Rung unproven, window does not start |
| I-9 | #37 both directions (exclusion state / rule change log) | Rule on frozen scope voids read, rule suspends; missing exclusion = exposure carried on register row |
| I-10 | SOP-26 downstream (continue-or-restore call on its I-9) | Rung holds, no floor; late call is a weekly-cascade finding |
| I-11 | SOP-26 P12 and T4 downstream | Unrouted release (quiet) / unwritten floor (loud); WE-4 |
| I-12 | #6 V5 and SOP-26 P5 downstream | Uncalibrated designs; void-as-MISS corrupts series; without P13 the SOP-26 P5 adjusted figure degrades to raw |

### Failure modes (F1-F12)
F1 paid-orders read; F2 off-cliff on rank-sensitive term (same-day escalation with rank cost); F3 concurrent family tests; F4 event contamination; F5 test theater; F6 permanent testing; F7 dirty baseline (new); F8 confounded read passed as clean (new; dated incident); F9 restore skipped after breach (new; WE-2 rate $52.49/week); F10 direct queue posting (new; 41.8%); F11 shared-term test without declaration (new); F12 bound drift (new: "an improvised tolerance is a local threshold wearing a prediction costume").
