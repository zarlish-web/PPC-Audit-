# SOP-12 Digest: Exact Campaign Operations

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-12: Exact Campaign Operations |
| Type | PPC Department Operating SOP, Component #12 of the Operations Definition Register |
| Version | 2.1 |
| Date | 2026-08-10 |
| Owner | PPC Lead |
| Amends | v2.0 (2026-07-26), adding Element 11 (Operator ramp) and Element 12 (Interface contracts); Sections 1-10 carry forward unchanged |
| Threshold policy | Thresholds live in Master PPC Decision Criteria System v4.0 only; zero local thresholds |
| Length | 15 pages; 12 procedures, 25-verdict mapping, 3 worked examples, 10 failure modes, 24 interface contracts, 14 live-defense questions |

**Verdict/purpose.** Exact campaigns are the control instrument of the account, carrying the **55-60% match-type spend destination of the M6 structure targets** and **100% of funded ranking pushes**, making this the highest-frequency SOP in the 39-component set. It governs the entire operating life of both exact structure classes: creation, launch settings, weekly operating pass, intraday funded-push pacing, verdict execution at campaign level, taper execution, promotion/demotion between classes, duplicate consolidation, event-window overlays, variation re-points, pause and archive mechanics. The SOP executes; it never decides (v4.0 decides).

## 2. Scope & Boundaries

### The two structure classes (Section 1.1)
Every exact keyword lives in exactly one class:
- **Class 1 — single-keyword oversight campaigns:** one campaign, one keyword, for every term carrying the oversight flag per v4.0 (roughly **100 terms per product driving over 90% of results**). Holds every funded push, every discovered floor, every dedicated defense.
- **Class 2 — consolidated syntax-exact tail campaigns:** one campaign per syntax family, **5-20 terms per ad group**, per-term bids, for exact terms below the oversight bar. The family is the cap-enforcement unit; a consolidated campaign never straddles two syntax families.
- Movement between classes: P5 (promotion) and P6 (demotion), fires only on v4.0 oversight criteria, never on judgment.

### Four legitimate duplicate roles (Section 1.2, per Doctrine 5.2)
Same term in 2+ live exact instances only when each carries one declared distinct role in T3:
1. **Stage-stack** — hot Ranking exact + cool Conversions exact simultaneously per O4, tagged and budgeted separately.
2. **Placement-split** — instances isolating placement groups per #28 evidence.
3. **Variation-split** — instances advertising different child SKUs per the D2 map.
4. **Sibling ownership** — instances on different family products per declared S-F3 term owner and role assignments.
Any second instance without a declared role = P7 territory the day it is found.

### Boundaries with adjacent SOPs

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 | Decides every verdict, threshold, band, scenario, limit. A threshold in this SOP is a defect |
| #31 Budget and envelope | Decides which pushes get funded (M5 queue) and envelope budget verdicts (CAP SYNTAX, envelope raises/cuts). This SOP receives budget deltas, never originates |
| #30 Harvest and graduation | Decides which terms graduate; this SOP receives GRADUATE FROM DISCOVERY and executes P1/P2 same day |
| #29 Negation architecture | Owns negation doctrine, wall rules, wall audit. This SOP builds prescribed walls at every structure event, same working session |
| #28 Placement and bid-modifier | Owns placement analysis, ladder step derivation, exit-bid discovery, modifier sizing. This SOP executes resulting campaign-level steps |
| #38 Bulk-file mechanics | Owns pull, staging format, upload, T+1 verification. This SOP produces staged change sets in #38 format and consumes verification report |
| #22 Launch-stage PPC | Owns deployment sequence and honeymoon. This SOP governs steady state from launch exit per launch-to-KDR handoff map |
| #32 Deal and event window | Owns event plan, ramp, caps, reconciliation. This SOP freezes structure changes inside armed windows (P9) |
| #33 Sibling arbitration | Owns composite computation and ownership on shared terms. This SOP checks declared owner (G11) before any scale action |
| #17-19 SB / SBV / SD | Own non-SP formats; on ENTER SBV ARBITRAGE this SOP executes only the SP-exact ladder step-down |
| #16 | Owns OPEN / ROTATE / EXIT CONQUEST |
| #35 | Incrementality measurement design and continue/restore call |
| #37 | Change control / automation rules (console-edit root causes) |
| #13, #15, #23, #41, #45 | Upstream/downstream interfaces (see Section 7) |

## 3. Triggers

| Trigger | Signal | Procedure |
|---|---|---|
| Weekly cadence | Monday audit cascade reaches T2; exact rows in OVERSIGHT filter view | P3; deployment Tuesday per #38 |
| Graduation arrival | #30 issues GRADUATE FROM DISCOVERY, same day | P1 or P2 (class per v4.0 oversight criteria) + #29 walls, same session |
| Structure verdict | ADD EXACT + RESTRUCTURE, CONSOLIDATE DUPLICATES, TAPER, PAUSED-PENDING in T2 | P1/P2, P7, P4, P8 respectively |
| Funding release | M5 queue entry moves to FUNDED with dated release | P1 push stand-up (or bid/budget lift on existing dedicated campaign), same day; P12 arms |
| Class boundary crossing | Oversight flag gained or lost (v4.0 criteria) | P5 / P6 |
| Event window | G12 arms on a confirmed deal window | P9; structure changes freeze unless event plan names them |
| Inventory band change | G6 flips YELLOW or RED on targeted variation; D2 names ranked backup | P10 re-point same day on RED; push freeze on YELLOW per v4.0 verdict |
| Intraday, deployment days | Hourly truncation alarm on push campaigns during/after upload | P12 step 3; budget lever same day |
| Intraday, funded pushes | Twice-daily in-budget % and spend-curve check on every FUNDED row | P12 steps 1-2 |
| Verification return | #38 T+1 report flags landed-value mismatch | F10: redeploy delta same day |

## 4. Procedures

### Preconditions and gates (Section 3)
A missing/stale field group suppresses the dependent execution class; pass records what it could not see and continues on readable rows.

| Manifest field group | Requirement |
|---|---|
| A2 Deployment state | Current bulk state in-row; stale fails G2 freshness, pass stops for those rows |
| A6 Objective + Expected CPC | Exactly one declared objective per term; UNTAGGED routes to assignment per O2 before execution (G10). Expected CPC on every rank-objective row |
| A7 Eligibility | Advertised SKU eligible; eligibility flip halts all execution same day (G4), opens listing task |
| B1 Indexing and listing placement | Rank-objective creations require term indexed with title or bullet placement (G5); backend-only routes to listing queue before push funding |
| B5 Coverage counts | Registry counts per match type current, else promotion/consolidation/creation-legality unreadable |
| B8 Economics chain | T0 named cells live: AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC; G9 PROVISIONAL tag on ceiling-referencing actions while margin blended/stale |
| D2 Variation map | Targeted variation + ranked-backup chain known; if unmapped, point at preferred SKU, row carries D2-pending flag |
| Gates in force | G3 truncated campaign gets budget lever first, no bid changes read through truncated day. G6 RED blocks push creation and lifts. G11 shared-term scale actions check declared family owner. G12 active event mode freezes non-plan structure changes |

### P1. Create single-keyword exact campaign (oversight class)
1. Confirm class: T2 column K1 oversight flag. If not, P2.
2. Creation legal: read T2 K8 (# Exact count) and T3 registry. Live instance with no declared role -> P7. Live instance with declared role admits creation only if new instance carries one of the four roles, declared in T3 before campaign exists.
3. Gates: G6 GREEN on D2-preferred variation (RED blocks push creation); G12 clear or event plan names it; G9 fresh where verdict references a ceiling; G5 passed on rank-objective terms.
4. Name per v4.0 Section 4.2 convention (Appendix A); objective segment must parse or T3 flags non-compliance and F6 fires.
5. Stage settings as bulk rows per #38: portfolio = product's portfolio; daily budget = T2 Required Budget $/wk / 7; bidding strategy per v4.0 Section 4.4 for declared objective.
6. One ad group. Advertised SKU = D2-preferred variation, never the parent by default.
7. Single keyword, match Exact. Starting bid = verdict-carried value (ladder start, discovered floor, or push sizing from T2 K7). Never invented; no verdict bid -> returns to T2 incomplete.
8. Placement modifiers = 0 on all three groups unless #28 placement evidence exists. Modifier earned, not defaulted.
9. Walls same session per #29: negative-exact the term in every phrase, broad, auto campaign that could serve it, and sibling campaigns per declared family ownership. Record wall list in T3 row.
10. Registry: T2 K8 increments; new T3 row with objective tag, role, owner, wall list; T1 family spend formulas pick it up via syntax tag.
11. Log creation in T6 with prediction (metric, direction, magnitude, horizon, review date). No prediction = does not deploy.
12. Deploy via #38: Tuesday default; same day for dated release (funded push, graduation). Same-day deploys still get T+1 verification.

### P2. Create or extend consolidated syntax-exact campaign (tail class)
1. One campaign per syntax family; never straddle families. Extend if exists; create only if none.
2. Naming encodes family root in keyword position; Objective = family's dominant tail objective (typically Conversions or Discovery-graduate). Shifts retag per O7 as logged transition.
3. Ad group 5-20 terms. At 20, open second ad group in same campaign before second campaign; second campaign on same family = F4.
4. Per-term bids from each term's verdict-carried value; never blanket bid.
5. Walls per #29 for every added term, same session, recorded in T3.
6. Registry and T6 as P1 steps 10-11; prediction covers added terms as a named cohort with one review date.

### P3. Weekly operating pass (Monday cascade)
1. Enter T2 only after T0 and T1 read (product posture and family caps govern). Skipping = invalid.
2. Score last cycle first: T6 rows whose review dates land this cycle, record V5 scores.
3. Apply OVERSIGHT filter view. Per row, verify gate columns before metrics: G2 freshness, G3 truncation (K2), G6 inventory, G12 event. Failing gate -> execute gate's lever (budget for G3), defer metric verdict to next clean cycle.
4. Read row verdict (K9), map to Section 5 execution. Two rows with opposite trends never receive same execution; four-period trend context travels in reason string.
5. One-lever rule: one lever per row per cycle (bid or budget, never both) unless verdict names a two-lever program.
6. Expand campaign child rows where verdict names a specific campaign; execute at that campaign only. Multi-instance terms: verdict only on instance whose role it addresses.
7. Stage as bulk rows per #38: entity, current value, new value, reason string with verdict and scenario ID. Missing scenario ID = no deploy.
8. Tuesday: deploy per #38 after BM huddle. T+1 verification; mismatches -> F10 same day.
9. Log every deployed change in T6 with prediction.

### P4. Taper execution at rank achievement
1. Trigger: TAPER verdict (rank achieved, hold confirmed per v4.0 stability requirement). Trigger was logged the day push objective was set; rank-achieved row still carrying push spend = F5.
2. Execute dated ladder steps from #28: bid step-downs at M3 step size on named dates toward placement-CPC exit bid; modifier step-downs where raised for push.
3. Normalize daily budget toward maintenance as spend falls; budget follows bid down, never leads.
4. Retag objective Ranking -> Conversions (or Defensive where brand-adjacent). T3 objective tag and campaign-name objective segment update in same staged set; mismatch = F7.
5. Each step = T6 entry predicting rank hold. WRONG-DIRECTION (slip past v4.0 tolerance) reverts one step and holds per #28; restored value = floor candidate.
6. At discovered floor, record floor in T2 K8 with date; re-tests on v4.0 quarterly cycle or after logged competitive shock.
7. Evaluate P6 at floor: floor-holding term that lost oversight flag demotes; retaining flag stays Class 1 at DEFEND AT FLOOR.

### P5. Promotion: tail -> single-keyword
1. Trigger: term meets v4.0 oversight criteria (volume, spend share, or push designation).
2. Create dedicated campaign per P1 in full (walls, T6 prediction).
3. Pause (never delete) term in consolidated ad group same session.
4. No negative structurally required in consolidated campaign; add one anyway when that campaign also hosts phrase or broad ad groups.
5. Budget share: consolidated budget reduces by term's trailing daily spend; new campaign carries it as starting floor, plus T2 K7 push sizing where push drove promotion.
6. Registry updates; T6 predicts dedicated efficiency vs consolidated baseline at named review date.

### P6. Demotion: single-keyword -> tail
1. Trigger: taper complete, floor discovered, v4.0 stability met at floor; or oversight flag lost.
2. Add term to family consolidated campaign at discovered floor bid. Set dedicated campaign PAUSED-PENDING with reason and named re-entry condition (re-promotes on recovery verdict or new funded push).
3. Registry updates; T6 predicts efficiency hold.

### P7. Consolidate duplicates
1. Trigger: CONSOLIDATE DUPLICATES verdict, or registry shows term live in 2+ exact instances with no declared role.
2. Survivor precedence: (a) instance with declared role; (b) instance winning S-R14 evidence read (higher CVR at lower CPC over validated window); (c) split read -> longer clean history with settings matching current objective. **Human-mandatory.**
3. Pause loser; move budget to survivor; carry every negation list loser held that survivor lacks.
4. Loser's placement evidence -> hand to #28 with consolidation note.
5. Registry decrements; T6 predicts survivor combined efficiency + root-cause line naming how duplicate arose (feeds F4; recurring source escalates).

### P8. Pause and archive
1. PAUSED-PENDING always carries reason + re-entry condition in T2 and T3; else incomplete.
2. Paused rows on weekly pass as re-entry check only (test criterion, re-enter or hold; never re-litigate).
3. Archive only campaigns paused beyond governance period with no re-entry met. Irreversible, human-mandatory; T6 archive entry closes history with final registry state.

### P9. Event-window overlay
1. Arm on G12: #32 event plan confirmed deal window enters T2 with dates; every exact row carries event flag through window + post-event guard.
2. Inside window: structure changes (creations, consolidations, promotions, demotions, archives) freeze unless event plan names them. G3 budget assurance and event plan staged actions stay live.
3. Event-week rates excluded from trend verdicts through guard period; weekly pass reads affected rows for gates only.
4. Post-window: ladders and floors resume from pre-event values unless #32 reconciliation justifies new ones; resumption is a staged, logged set.

### P10. Variation re-point
1. Trigger: RE-POINT VARIATION, or G6 RED on targeted variation with D2 naming ranked backup.
2. Stage advertised-SKU edit to D2-named variation, deploy same day (RED does not wait for Tuesday).
3. Log in T6 as product event: CVR baselines reset, trend clock restarts, gates-only until v4.0 sufficiency window refills.
4. On restock, re-point back per T7 recovery play; pre-OOS floor and ladder restore from T2 K8 record.

### P11. Bid and budget change mechanics
1. Every change exists first as staged bulk row per #38 (prior, new, reason with verdict + scenario ID). No console edits; console edit found = F10 with named root cause.
2. Step sizes, floors, per-change limits read from v4.0 L2 lever rules at execution time; never restated. Step exceeding L2 limit fails staging QA.
3. Budget precedes bid when G3 failing; bid reads resume next untruncated day. Tapers: budget follows bid down.
4. Ladders deploy one step per staged set with next step's date in reason string (V5 scores each step).

### P12. Intraday funded-push pacing
1. Twice daily on every FUNDED row: in-budget % and cumulative spend curve vs day-of-week expectation from T2 K7 sizing block. Materially off-curve -> budget lever or PPC Lead per alarm severity, same day.
2. Loss check with pacing: cumulative weekly spend - (orders x contribution) vs verdict-carried loss ceiling. Ceiling comparison and scenario call are v4.0's; this only surfaces numbers.
3. Hourly truncation alarm on push campaigns on deployment days: in-budget breach -> budget lever same day, voids week's bid read (F1).
4. Every intraday intervention writes T6 line; pacing interventions never change bids.

## 5. Rules, Thresholds & Numbers

### Numeric values stated

| Item | Value |
|---|---|
| Exact share of match-type spend (M6 structure target destination) | 55-60% |
| Funded ranking pushes in exact | 100% |
| Oversight class size | roughly 100 terms per product driving over 90% of results |
| Class 2 ad group size | 5-20 terms; at 20 open second ad group in same campaign |
| Daily budget at creation | T2 Required Budget $/wk / 7 |
| Placement modifiers at creation | 0 / 0 / 0 unless #28 evidence |
| Levers per row per cycle | 1 (unless verdict names two) |
| Pacing check | twice daily |
| Truncation alarm | hourly on push campaigns during deployment days |
| Deploy day | Tuesday (after BM huddle); same day on dated release / RED re-point |
| Verification | T+1 |
| Floor re-test | v4.0 quarterly cycle or after logged competitive shock |
| P5 human-confirmed tier (permanent) | every 500+ SV keyword action, every gate failure, every structural change, every bid move > 25%, every budget move > $50/day, every LOW-confidence verdict |
| Data timing | Raw Pull Pack Monday 06:00; refresh complete 09:00; KDR generated Monday PM |
| Ramp | 10 matrix rows, 3 checkpoints (week 1, week 2, week 4; week 3 repeats week 2); 9 week-1 artifacts; 14 live-defense questions |
| Ledger due date #44 | 2026-09-25 |

### v4.0 rule / gate IDs referenced (as described in this SOP)

| ID | Meaning as described here |
|---|---|
| M6 | Structure targets (exact = 55-60% match-type spend destination) |
| M5 | Funding queue for pushes (#31) |
| M3 | Taper step size; floor |
| M2 | Sizing mathematics; loss line binds inside sized push |
| M8 | Incrementality spend step-down program |
| M10 | LOW confidence: step sizes and budget steps halve, horizon shortens, pushes barred |
| O2 | UNTAGGED routes to objective assignment |
| O4 | Stage-stack (hot Ranking + cool Conversions exact) |
| O7 | Objective retag as logged transition |
| G2 | Freshness (deployment state) [note: SOP-06 uses G2 for sample sufficiency; Q8 here also cites G2 for sufficiency] |
| G3 | Truncation; budget lever first |
| G4 | Eligibility flip halts execution |
| G5 | Indexing with title/bullet placement for rank objective |
| G6 | Inventory band GREEN/YELLOW/RED |
| G8 | Manifest STALE/MISSING downgrades verdicts to flags |
| G9 | Margin fresh / PROVISIONAL |
| G10 | Untagged objective gate |
| G11 | Shared-term declared family owner |
| G12 | Event window armed (deal window) |
| L1 | Lever precedence (budget first) |
| L2 | Lever step sizes, floors, per-change limits (also unlock mechanics) |
| S-F3 | Declared sibling term owner and role |
| S-R12 | Recovery push sizing toward pre-OOS baseline; also stem/phrase graduation receipts |
| S-R14 | Duplicate survivor evidence read (higher CVR at lower CPC) |
| S-A9 | Margin sweep recomputing ceilings (#41) |
| T1 | Objective transition evidenced by rank held |
| P3 | Audit value wins over automation; conflict flagged in T6 |
| P5 | Human-confirmed tier |
| P9 | Portfolio calls bind product plans |
| P10 | No unstaged changes / J-complete record |
| V1, V3, V5, V6 | Prediction fields; amendment protocol; rule accuracy review; version-pin sync rule |
| D6 | Named owner for conversion fixes |
| Section 4.2 / 4.4 | Naming convention / bidding strategy per objective |

### Verdict-to-execution mapping (25 verdicts)

| Verdict | Exact-campaign execution |
|---|---|
| QUARANTINE: DATA REFRESH | No changes deploy; refresh task carries staged set forward |
| UNLOCK TRAFFIC | Bid steps up per L2 unlock on named campaign; no rate judgment until G2 sufficiency |
| FIX BUDGET (TRUNCATED) | Budget lever only (G3, P11 step 3) |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | No change except G3 budget assurance |
| FUND TEST (UNFUNDED PRIMARY) | P1/P2 at capped test bid; test status + stop-loss date into T2 K7 |
| RANK PUSH: FUND SIZED PUSH | P1 or bid/budget lift on funding release date; bidding per 4.4; T2 K7 governs budget; P12 arms same day |
| RECOVERY PUSH | As above, sized toward pre-OOS baseline per S-R12; T2 pre-OOS floor/ladder informs starting bid |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Bid or budget lift per verdict's named lever; never both |
| FIX CONVERSION FIRST; DEFER PUSH | Cap at maintenance; fix routes to D6-named owner; re-enter on stated criterion |
| PLACEMENT FIX FIRST | Bids hold; #28 executes; deploy only #28 campaign-level rows |
| RE-POINT VARIATION | P10 same day |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | P4 |
| HOLD; DEFEND LIGHTLY AT RANK | No change; WoW block read next cycle |
| DEFEND AT FLOOR | No bid change; drift from floor -> restore to floor in one staged step |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Bid to T2 K6 Max Profitable CPC, single step; syntax-cap half at T1 per #31 |
| INCREMENTALITY LADDER | Dated spend step-downs per M8; design and call belong to #35 and v4.0 |
| ADD EXACT + RESTRUCTURE | P1/P2 + #29 steering walls; note names source campaign carrying term |
| CONSOLIDATE DUPLICATES | P7 |
| GRADUATE FROM DISCOVERY | P1/P2 same day + walls; discovery CPC and order evidence seed verdict bid |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | Owned by #29; structural walls at P1/P2/P5/P7 |
| ENTER SBV ARBITRAGE | One SP-exact ladder step down dated to SBV go-live; SBV build at #17-19 |
| OPEN / ROTATE / EXIT CONQUEST | Owned by #16; only a named shared-term bid step per P11 |
| STOP-LOSS: CONCEDE OR DEFER | Push campaign to maintenance or PAUSED-PENDING; freed budget to envelope/M5 at #31 |
| PAUSED-PENDING (REASON + RE-ENTRY) | P8 steps 1-2 |
| LEAVE TO HARVEST | No exact stood up; any live exact evaluated for P6/P8; discovery economics under #30 |

### Interface contract standing rules (12.1)
- C1 artifact is the interface; C2 non-arrival recorded in T7 ("Verdict Classes Blocked While Missing", G8); C3 suppression never substitution; C4 cite Ledger row not counterparty procedure number; C5 no maximum lag (v4.0 has no interface-lag thresholds). (Note: these C1-C5 are contract rules, distinct from Ledger conflict IDs such as C3.)

## 6. Data Inputs Required

**Command Workbook tabs and columns**
- **T0** — named cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC (product posture); zone H (funding queue).
- **T1** — family caps; family spend formulas (pick up campaigns via syntax tag).
- **T2** — OVERSIGHT filter view; K1 oversight flag; K2 truncation / in-budget %; K6 Max Profitable CPC; K7 sizing block (Objective, DSTR, Required clicks/day, Required budget $/wk, Loss ceiling $/wk, ETA checkpoint date, Review date; test status, stop-loss date; day-of-week spend curve); K8 # Exact count, discovered floor with date, pre-OOS floor and ladder state; K9 verdict; WoW block; event flag; four-period trend context; Required Budget $/wk field.
- **T3** — campaign registry: Campaign Name, Objective Tag, role, owner, wall list, naming-compliant flag, per-source yield, pacing C3.
- **T4** — Ladder State (step / date), Placement-CPC Exit Bid $, Discovered Floor $, Next Step Date.
- **T5** — product log (material structure events).
- **T6** — Decision Log (predictions, Review Date, V5 scores, conflict-flag column).
- **T7** — Manifest field groups and column "Verdict Classes Blocked While Missing"; rows B7 Placement splits (TOS/ROS/PP), D1 Per-variation margin; T7 recovery play.

**Manifest catalog IDs (input bindings):** A2 deployment state, A3 pacing and in-budget, A5 threshold flags, A6 objective + Expected CPC, A7 eligibility, B1 indexing and placement, B5 coverage counts, B8 economics chain, B9 WoW deltas, D2 variation map (preferred SKU + ranked backup chain, D2 map mismatch column), D7 decision log.

**External artifacts**
- Raw Pull Pack (BULK-US, 20 sheets) — Data Operations, Monday 06:00.
- Bulk file / #38 staging format; #38 T+1 verification report (landed vs staged).
- Search-term data (for F2 double-buying detection).
- #30 graduation log line (term, sources, evidence, outcome, class, family, verdict-carried starting bid, discovery CPC).
- #13 stem and phrase graduation packets and S-R12 receipts.
- #15 head-term receipt (ADD EXACT + RESTRUCTURE).
- #29 prescribed wall set (levels, sources, negation state per source).
- #28 derived ladder step, exit bid, floor, next step date; placement evidence.
- Funding release (T0 zone H queue, Account Rollup A2).
- Account Rollup A1 Family Boards, "Term owner + assignment basis" columns (#33).
- #32 event plan and armed-window declaration.
- #22 launch exit handoff (campaign inventory, objective tags, honeymoon-guard end date) per launch-to-KDR handoff map.
- #17-19 SBV go-live date and paired SP-exact step-down instruction.
- #23 push standup order (sizing worksheet reference, achievement condition, taper trigger).
- #35 incrementality step-down design (dated schedule, measurement window).
- #41 recomputed ceilings from S-A9 sweep with G9 state.
- KDR Cycle File; Account Rollup A3 Verification scoreboard.
- Transition Brief v1.2 (operator scope stack); PPC Authority Matrix v2.0; Cross-Reference Ledger row #12.

## 7. Outputs / Artifacts

| Event | Artifact set |
|---|---|
| Weekly pass (P3) | Updated T2 rows (verdict execution state), T3 registry current, staged bulk change set per #38 with verdict + scenario ID reason strings, deployed-and-verified bulk set with T+1 report, T6 entries with prediction and review date, V5 scores for last cycle's due rows |
| Structure events (P1/P2/P5/P6/P7/P8) | T3 row created/updated with role, owner, wall list; T2 K8 count change; T5 entry for material structure events; T6 prediction row |
| Ladders (P4, P11 step 4) | Dated T6 chain one row per step; recorded floor with date in T2 K8 |
| Intraday (P12) | Pacing and loss-line T6 entries; F1 alarm evidence; zero bid changes |
| Event windows (P9) | Armed-window record in T2; deviation log (empty = pass); post-window resumption staged set |

**Staged bulk row format:** entity, prior/current value, new value, reason string carrying verdict and scenario ID (and next step date for ladders).

**Alarm spec:** F1-F10 each with detection signal, evidence line (row, signal value, gate or rule reference), routing tier: F1/F3/F10 same day to operator queue; F2/F6/F7/F9 weekly pass worklist; F4/F5/F8 to PPC Lead with T6 history.

**Downstream contracts:** I-15 staged bulk set to #38 (Tuesday after BM huddle); I-16 T+1 report back; I-17 wall list to #29; I-18 loser placement evidence to #28; I-19 T6 entries -> KDR Cycle File (Monday PM) -> Account Rollup A3; I-20 freed STOP-LOSS budget to envelope (T0 zone H, A2); I-21 post-graduation outcome per term to #30 (per-source yield in T3); I-22 P12 alarms/pacing as confound list to #45 (dayparting deferral); I-23 F10 console-edit root cause to #37; I-24 Section 11 to #44 by 2026-09-25.

**Naming convention (Appendix A):** (Short Brand + Short Product) + Campaign Type + KW/Root/Auto + SV Type + Match Type + Objective + Bidding Strategy + SKU + Audience (optional). Class 2 places family root in keyword position. Example: `DBS4-SP-bamboo sheets king-HSV-Exact-Rank-Fix-B4-KING-WHITE`.

### Failure modes

| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Push starved by truncation | In-budget % < 100 on push row (T2 K2); P12 hourly alarm | Budget lever same day; week's bid read voided; cause into T6 |
| F2 | Graduate double-buying (wall missed) | Same search term converting in exact AND source campaign | Wall immediately per #29; root cause names skipped session |
| F3 | Wrong advertised variation vs D2 | D2 mismatch column; CVR anomaly vs family | P10; CVR baseline reset |
| F4 | Duplicate re-creation after consolidation | Registry # Exact > 1 with no declared role | P7 re-run + root cause; recurring escalates to PPC Lead |
| F5 | Taper never triggered post-rank | Rank at/better than target + push-level spend + weeks-at-verdict accruing | P4 immediately; standing audit line (account's known failure class) |
| F6 | Naming non-compliance | T3 naming-compliant flag | Rename via bulk; nothing else rides the rename |
| F7 | Objective retag missed after taper | T3 tag vs campaign-name segment mismatch | Retag both in one staged set; V5 marks taper step as process miss |
| F8 | Structure change inside armed event window | T6 structure entry in G12 window, no event-plan reference | Revert unless named; escalate per #32; trend exclusions extend from revert date |
| F9 | Wall at wrong level | Source impressions collapse on adjacent tail terms | Replace with negative-exact per #29; restore serving; root cause to wall audit |
| F10 | Landed values differ from staged | #38 T+1 mismatch; console edits | Redeploy delta same day; affected reads void; actor named, route to #37 |

Escalation: same failure twice in consecutive cycles on same scope -> PPC Lead with T6 history. Same interface failing twice in consecutive cycles -> PPC Lead, carried as Ledger-row disagreement.

## 8. Decision Rights

- **Human-mandatory:** campaign creation on funded pushes, P7 survivor selection, P8 archives, cross-family budget movement, every deployment confirm; plus the permanent P5 tier.
- **AI-executable with audit:** staging bulk rows for issued verdicts, wall additions, registry updates, T6 drafting, intraday pacing reads, verification reconciliation.

| Authority Matrix v2.0 row | D holder | Incoming operator | SOP-12 role |
|---|---|---|---|
| Weekly verdicts (established US) | PPC Lead | E, assigned scope | P3 |
| Structure creation (all SOPs) | PPC Lead, or per SOP scope | E | P1, P2, P5-P8; BM owner is I |
| Push funding (M5 queue) | CEO above envelope; PPC Lead within envelope | E | Standup on dated release only |
| Bulk deployments (#38) | No D; PPC Lead reviews | E | Standing rule 2: E without D executes staged decisions only |
| Sibling declarations (S-series) | PPC Lead | E | G11 check |
| Event plans (#32) | PPC Lead with deals owner | E | P9 |
| Incrementality tests | Incoming operator (Transition Brief v1.2 scope) | D and E | Dated step-downs (only row operator holds D) |
| Code-red declaration + close | PPC Lead | E | Exact half of code-red program |
| Automation rules (#37) | PPC Lead | E and R | F10 root cause routing |
| v4.0 threshold changes | CEO | I | Nothing; missing numbers = amendment requests |

- Not conferred: "Launch-stage verdicts + batches" and "Canada weekly block" (launch/CA operator D and E).
- Standing rule 4: product scope from Transition Brief v1.2. Standing rule 5: unfilled role D -> PPC Lead, E -> PPC Manager; ramp continues.
- Week-1 reviewers: PPC Lead (W1.1, W1.2, W1.4, W1.5, W1.7, W1.8), PPC Manager (W1.3, W1.6, W1.9). Week 2 closes when review changed no staged value on final cycle. Week 4 audit checks five things (verdict + scenario ID; prediction + review date; no P5-tier item unconfirmed; gate failures executed gate lever; last cycle scored first). P5-tier item deployed unconfirmed stops ramp same day.

## 9. Account-Specific Facts

- Account's known/named failure classes: F5 taper never triggered post-rank; spend moving toward rank with no funded release; head terms carried by campaigns that choose their own traffic.
- Worked examples (illustrative; live values from T0/T2):
  - **WE-1** term "bamboo sheets king", rank 18 vs target 5; AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3%, Expected CPC $2.50; CVR 5.2% on 212 clicks; Max Profitable CPC $1.46. Funded +$180/wk on existing $142/wk = $322/wk -> $46.00/day; loss ceiling $40/wk; prediction rank 18 -> 11 in 14 days. SKU B4-KING-WHITE (47 days cover). Bid $2.60. Day 7: spend $301, 118 clicks, CPC $2.55, 6 orders, CVR 5.1%, ACOS 62.7% (2.39x Max Acceptable), rank 13, velocity 0.71/day; gross weekly loss $133; v4.0 returns CONTINUE. Day 14 rank 10, day 21 rank 9 -> TAPER: $2.60 -> $2.34 (M3), then to exit reference $2.24 (blended placement CPC $2.31 minus offset). Retag Ranking -> Conversions.
  - **WE-2** "cooling bamboo sheets queen", 4 orders from B4 broad family; added as 15th term in ad group of 14; bid $1.20 (from $1.12 discovery CPC); prediction CVR >= discovery read in 30d at CPC <= $1.30. 30d: 96 clicks, 7 orders, CVR 7.3%, CPC $1.18, spend $113, sales $560, ACOS 20.2%; enters top spend decile -> P5; $3.77/day spend share moves.
  - **WE-3** "satin sheets queen": A 14 months, CVR 6.1% CPC $1.62, $98/wk spend on $420 sales (ACOS 23.3%); B 5 months, CVR 4.8% CPC $2.19, $63/wk on $168 (ACOS 37.5%); combined 27.4%. Survivor A; B's $9.00/day budget and 3 negatives move; prediction blended ACOS to 24.0% within 2 cycles. Root cause: B created during the March launch push without a registry read (P1 step 2 skipped).
- Product references: B4 (bamboo sheets) broad family campaign, two B4 autos, sibling 6-piece broad; brand prefix DBS4.

## 10. Open Items

- **Interface lag limits:** v4.0 carries no rule on how late is late; v4.1 amendment item.
- **#31 counterparty:** no procedural document (Ledger conflict C3); I-7 and I-20 written to instruments (T0 zone H, Account Rollup A2).
- **#44 certification:** not built, due 2026-09-25; I-24 has receiving owner but no document; aggregate pass mark is a v4.1 item.
- **Counterparty procedure numbers:** I-3, I-4, I-11, I-12, I-13, I-14, I-22 cite Ledger rows because those components are at later versions than copies routed to the session.
- **Inconsistencies observed in text (not flagged by the SOP itself):**
  - Gate numbering differs from SOP-06: here G2 = freshness (though Q8 cites G2 for sample sufficiency), G10 = untagged objective, G12 = event window; SOP-06 uses G10 = event exclusion, G12 = MKL hygiene, G2 = sample sufficiency.
  - W4.3 lists four permitted V5 values (HIT, PARTIAL, MISS, WRONG-DIRECTION); SOP-06 v2.0 adds VOID as a fifth.
- Review triggers added at v2.1: Section 11 re-issues within one week of Authority Matrix re-issue; Section 12 re-issues on Ledger version rewriting row #12 or any counterparty row; Section 11.5 re-issues on v4.0 increment changing a rule cited in a defense answer. Review monthly and on any v4.0 increment.
