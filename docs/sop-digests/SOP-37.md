# SOP-37 Digest: Automation Platform Rules

Source: `PPC_SOP_37_Automation_Rules_Operations_v2_0.pdf` (page footer counts 20 pages; closing line says "Page 18 of 18"). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-37: Automation Platform Rules (PPC Department, Operating SOP, Component #37) |
| Version | 2.0 |
| Date | 2026-08-09 |
| Owner | PPC Lead |
| Supersedes | SOP-37 v1.0 (2026-07-24) in full |
| Thresholds | Criteria System v4.0 only; zero local thresholds. Every inventoried rule parameter is **recorded platform state carrying a reconciliation outcome, never an authority** |
| Growth vs v1.0 | v1.0 was 3 pages vs a 10-18 page bar (superseded 10-element standard). Procedures 7 -> 14; failure modes 6 -> 12; worked examples 1 -> 4; Elements 11 and 12 added; 25-string closed-vocabulary mapping replaces v1.0's 5-row table of register states |
| Amendment items | 13 (AM-1 to AM-13) |

**Verdict / purpose.** A rule is a **standing decision executing at machine speed**, legitimate only while **four things stay true at once**: (1) it is **registered with an owner**; (2) it **reconciles to a named v4.0 rule** or carries a dated documented exception; (3) its **scope excludes every entity whose objective function is not the one the rule assumes**; (4) **every change it makes is attributable in the T+1 diff**. A rule missing any of the four is **suspended on discovery**, not tolerated until the next pass. Motivating incident: one target-ACOS ladder walked a defensive term up **6 consecutive steps** against a target left stale by a retag; the code-red four-map diagnosis found it, not the automation layer.

**Governs:** rule register and schema; intake and registration; reconciliation of every live rule against v4.0; rule-class guardrails and scope-exclusion state machine; change control; weekly runaway watch; suspension and re-enable; rank-based taper rule and its single-rung boundary with #28; precedence arbitration (rule action vs staged manual action); portfolio-object governance (second budget-enforcement surface); sync at every v4.0 increment; quarterly full pass; automation posture in Recovery Mode and code red; platform capability, seat and export changes.

### 1.1 Dependency D6 (stated first)
Cross-Reference Ledger Section 2 external dependency **D6 = automation platform rules export, OPEN**. Ledger effect line: register cannot be reconciled against v4.0 without it. SOP's position: D6 blocks exactly **one thing - a machine-readable diff**. While OPEN, P1 runs as a **human transcription** of the live rule list (transcription risk; detection latency bounded by operator's pass). **Thirteen of fourteen procedures fully executable at D6 OPEN; one (P1) at reduced assurance.**

**Manifest state at build** (live T7 Manifest of Command Workbook TEMPLATE v1.0):

| Field group | State | Consequence |
|---|---|---|
| A1 four-period comparability | MISSING | Blocks all trend verdicts; P6 compares against single-window expected volume |
| A3 pacing buckets | PARTIAL (day-of-week curve pending) | P10 collisions surface as truncation, not pacing deviation |
| A6 objective + per-term Expected CPC | PARTIAL (Expected CPC at account reference) | Caps precision of every ladder-priced rule |
| A8 PAT rows first-class | PARTIAL | SBV-PAT reconciliation carries coverage gap in row |
| Packet completeness (G8) | **0.571**, below DEGRADED floor | Every outcome this cycle carries its manifest state beside it |

### 1.2 Four corrections of substance vs v1.0
1. v1.0 P5 sized runaway signature against "the v4.0 consecutive-step reference" - does not exist (v4.0 consecutive-period language governs weeks in scenario conditions, never ladder steps). Retired; AM-2.
2. v1.0 reconciled B-class pause thresholds against "v4.0 reactive thresholds per ad type"; S-H7 conditions on a threshold v4.0 does not state and F11 gives waste as a percentage -> documented exceptions pending AM-1.
3. v1.0 treated B-class pause as a click-count question; prior question is lever order (L1 places status last; L7 requires log naming exhausted levers) -> F7.
4. v1.0 P7 suspended rule action for a staged decision's read window, where v4.0 rule P3 has automation resuming from the audit value (Section 13.1). All six v1.0 failure modes and both account-history incidents carry forward.

### 1.3 The rule register: four classes, one schema
**Nine fields per rule:** name, class, trigger condition, action, bounds, scope, owner, reconciliation outcome with date, last-synced v4.0 version. Live rule outside register = F1, suspends on discovery. Inventory seeded from live platform in **2026-07**.

| Class | Inventoried trigger and action (recorded state) | Governing v4.0 surface and guardrail |
|---|---|---|
| **A. Inch-up** (traffic assurance) | Target bid raised by fixed **$0.05** where clicks run **under 3**, per ad type (SP, headline, SBV, SBV-PAT, SD). Bounds: SP roughly **$0.30-1.30**; video and display variants **$0.30-1.00** | G2: bid read needs >= 15 clicks in 7 days; S-R1 answers under-15-click case with bid steps of **15-25%** per L2. Direction agrees, step form does not (WE-1). Scoped OUT of push, event, terminal, settling entities and any entity deliberately at a bid floor |
| **B. Pause-at-zero** (waste control) | Pause + bid floor at zero orders over **10-day** window: SP >= **30** clicks, headline **30**, SBV **15**, SBV-PAT **15**, SD **12** | L1 places status last after documented exhaustion of budget, bid, placement, negation, structure; L7 requires log naming exhausted levers. S-H7 conditions on zero-sale spend above an unstated threshold. Lever-order defect (F7) + ungoverned parameters (AM-1). #29 converting-term guard rides every rule-fired pause |
| **C. Target-ACOS step ladders** | Step ladders toward target ACOS at **5, 10, 15, 20, 25, 30, 35%** tolerances, split by order state: **1-or-more-order family** (>= 3 clicks, max bid **$2.50**) and **zero-order family** (>= 3 clicks, top-of-search share capped at **30**, max bid **$1.20**) | THE scope-sensitive class. O6: each objective judged only on its own metric set; efficiency ladder on ranking/event/liquidation objective is a category error. Flat max bids vs M1 per-variation ceiling (contribution x CVR) (WE-2). Stale targets after retag = runaway root cause (F3) |
| **D. Rank-based taper** | At target rank with platform hold condition met, keyword steps down | S-R6: objective transition only after organic rank at or under target for **2 consecutive weeks**; S-E5: rank inside event window provisional until exclusion window closes. Rule executes **rung one** of #28 ladder and flags; step size M3 **roughly 10% per week**, derived at #28 |

## 2. Scope and boundaries

**Owns (per Ledger row 37):** rule register, sync-check cadence, change control so automation never drifts from the criteria.

| Excluded decision | Owner | Seam |
|---|---|---|
| Every threshold, band, scenario, limit, verdict | v4.0 (#8) | Rules implement v4.0, never rival it. A numeral without a v4.0 section is recorded platform state or a defect; Section 13 lists the thirteen numerals v4.0 does not carry |
| Manual deployment path, staging format, upload, T+1 diff | #38 | This SOP consumes T+1 attribution report as precedence evidence and unlogged-edit detector; unattributable rule-fired change = #38 F4 class |
| Ladder mechanics: rung derivation, exit-bid discovery, floor register, modifier sizing | #28 | Ladder holds are #28's (Ledger row 28); it issues hold notice naming frozen rows. D-class executes rung one and hands off |
| Runaway diagnosis inside declared code red | SOP-26 P3 | Four-map diagnosis reads this SOP's rule-change log as automation check. This SOP owns weekly watch outside code red and suspension execution inside it |
| Terminal and LTSF-tier entities | SOP-27 | Excluded from B and C; computes nothing about units/tiers (conflict **C6**: deciding system outside corpus) |
| Auto-side rule scope state and per-group protected surfaces | SOP-15 P11 | SOP-15 maintains exclusion state feed, never edits a rule; this SOP registers, reconciles, suspends |
| Negation doctrine, wall levels, shared lists, converting-term guard | #29 | Rule-fired pause/negative applies #29 standards; this SOP routes |
| Envelope law, queue ordering, CAP SYNTAX, envelope raises/cuts | Instrument layer (T0 named cells, T1 caps, Account Rollup A2) per conflict **C3** | #31 has no numbered procedures; P10 reconciles against instrument and tab |
| Event-window arming, ramps, caps, reconciliation | #32 | Excludes armed and settling entities |
| Automation-platform seats, credentials, rotation | #46 | Seat change removing a rule owner triggers P7 same session |
| Billing continuity and outage response | #43 | #43 requests this SOP's rule log to clear its triage branch 4; this SOP owns post-restoration rule-read suspension |
| Which terms graduate; exact standups | #30, #12 | A rule never creates, retags or consolidates structure (human territory) |

## 3. Triggers
Lag measured from the artifact's own timestamp.

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Weekly register diff | Live rule list vs register, inside Monday cascade after packet-ready read | Same working day | P1 |
| New rule requested | Rule-intake row, or live unregistered rule found by P1 | 1 working day to registration or suspension | P2, P7 |
| v4.0 version increment | Criteria System file version stamp vs register last-synced field | 1 working day to open, 5 to close | P11, P3 |
| Quarterly full pass | Last full-pass date reaching **13 weeks** (V4 quarterly) | Scheduled week | P12, P3 |
| Campaign state change | Push standing up/closing, event arming/settling, terminal tag, manual hold; T2 gate columns and T3 campaign state | Same day | P4 |
| Runaway signature | Rule-fired change counts per entity per window in platform change log vs expected volume | Same working day as weekly read | P6 |
| Rule edit without a record | Register diff vs T6 change records | Same working day | P5, P7 |
| Rule vs manual collision | #38 T+1 diff attributing a change to a rule on an entity with a staged decision same cycle | Same day as T+1 report | P9 |
| Rank-target reached | Platform hold condition firing on D-class rule, cross-read vs organic rank T2 block K4 | Same day for flag; rung waits on #28 | P8 |
| Code red declared | Declaration written to T5 by SOP-26 P3 | Same day | P13 |
| Recovery Mode entry/exit | Recovery state per v4.0 Section 11 rules R1 and R5 | Same day | P13 |
| Portfolio object created/edited | Console portfolio list vs register portfolio section | Same working day as weekly read | P10 |
| Billing or platform outage restored | #43 restoration verification or platform incident close | Same day | P14 step 4 |
| Seat or credential change | #46 access reconciliation diff naming automation seat | Same day | P14 |
| Platform capability change | Vendor release note or new rule type in console | 5 working days to register class or decline in writing | P14, P2 |

## 4. Procedures

### Preconditions and gates (missing/stale group suppresses dependent class; per G8)

| Gate / precondition | Manifest ID / source | Observable |
|---|---|---|
| Register currency | Register last-synced fields | Last-synced version = attached Criteria System version; last full pass inside 13 weeks. Stale -> no outcome admissible |
| Live rule list readable | Ledger D6 (OPEN) | Dated console read of live rule list, transcribed by entity, initialled, this cycle; manual-read flag; F1 latency one cycle |
| Deployment state current | A2 in-row, T7 PRESENT | Current bid, budget, state for every entity with a live rule, timestamped this cycle. Stale A2 stops P9 |
| Attribution report present | A2 + #38 T+1 diff | T+1 diff for every deployment since last pass with zero unexplained mismatches. Absent -> **P6 and P9 do not run** |
| Threshold flags computed | A5 in-row, T7 PRESENT | Gate and band flags compute on affected T2 rows; reconciliation reads flags, never re-derives |
| Objective and Expected CPC | A6, T7 PARTIAL | Exactly one declared objective in **T2 block K7** on every entity with a C- or D-class rule; Expected CPC at account reference; ladder-priced rules carry A6 PARTIAL flag |
| Economics chain live | B8 chain, T0 named cells | AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, with D1 margin version and G9 state; max profitable CPC per variation (M1); G9 PROVISIONAL carries onto ceiling-referencing outcomes (cap dated, re-checked next refresh) |
| Coverage counts current | B5, T7 PRESENT | Registry counts per match type current |
| G1 validation quarantine | T2 zero-flag columns | No quarantined row in scope; rule action suspends until refresh task closes |
| G3 budget truncation | K2 in-budget %, worst hosting campaign | **>= 70% of the day** on every entity a C-class rule prices; below = TRUNCATED, rule-fired bid change void |
| G6 inventory adequacy | T2 block K2 inventory band, days to stockout, from D2 map | GREEN for any rule that can raise a bid; YELLOW/RED leave raise scope same day |
| G9 price stability | T5 price change log, trailing **7 days** | No price change in 7 days; inside window no conversion-driven outcome recorded as finding |
| G10 event exclusion | T2 block K2 event posture + #32 armed-window record | Event weeks and **14 days following** excluded from trend verdicts; D-class taper inside = F9 |
| G12 MKL hygiene | MKL refresh date | Current inside **30 days**; stale degrades manifest; untagged terms route to maintenance |
| G8 packet completeness | T7 completeness % | Below **85%** = DEGRADED; every outcome a flag with completeness stamp (build: 0.571) |
| Mode posture known | Recovery and event state | T8 and P7: Recovery > Event > stage defaults; read before any re-enable (R3 tightens confirm tier) |

### P1. Weekly register diff (25-40 min at 24 rules)
Inside Monday cascade, after packet-ready read, **before any T2 verdict work** (an overnight rule move changes every prior value).
1. Register beside live rule list; while D6 OPEN, transcription read top to bottom by ad type, never from memory.
2. Transcribe each rule's nine fields into dated working copy. **Match by name plus trigger, never name alone.**
3. Three-way diff: live+registered; live+not registered; registered+no longer live.
4. Live not registered = F1: suspend in console same session; route to P2 or written retirement.
5. Registered not live: confirm deletion staged in T6; else F4, row stays open with owner.
6. Field mismatch on live registered rule -> decision tree:
   1. T6 change record dated on/before platform last-change date naming this rule and field? Yes -> register stale; update row; carry outcome forward only if changed field is not the one outcome rests on; stop.
   2. No record, change inside registered bounds and scope? -> silent edit inside bounds, F4: revert to registered value pending review, reconstruct record from console history, route to P5.
   3. No record, outside bounds/scope -> suspend same session, route to P7; damage assessment on every entity touched since last-change date using #38 T+1 diffs.
   4. Console history cannot name actor -> escalate to PPC Lead with entity list; route seat question to #46 same day (access finding first).
7. Diff artifact: date, rules read, three counts, every mismatch with disposition, manual-read flag, operator initials.

### P2. Registering a rule and pre-go-live reconciliation (20-30 min per rule)
1. Collect nine fields from requester; missing bounds or scope -> returned, not completed by registrar.
2. Name governing v4.0 rule by section and rule ID; cannot -> declined at intake.
3. Run P3 before go-live; enters at AGREES, ADJUST (adjusted value applied), or DOCUMENTED EXCEPTION (owner + date). No provisional live period.
4. Set scope exclusions per P4 before enabling.
5. Bounds so largest possible action stays inside **L2: 50% of current value per change, floor $0.50**.
6. Confirm tier (rule **P5**): bid moves **> 25%**, budget moves **> $50/day**, actions on **500-plus SV** keywords, gate failures, structural changes, **LOW-confidence** verdicts are human-confirmed. Rule whose action can cross these registers only with crossing entities excluded.
7. T6 entry with v4.0 citation and prediction: metric, direction, magnitude, horizon, review date (V1).
8. Enable; first review at next weekly pass.

### P3. Reconciliation against v4.0 (10-15 min per rule; 4-6 h for full 24-rule pass)
Runs at every increment (P11), quarterly (P12), registration (P2). **Three outcomes only:**
- **AGREES:** implements v4.0 as written, same value, same condition, same limits; record section, rule ID, both values, date.
- **ADJUST:** diverges; moves to v4.0 value this session (staged per P5), prior and new recorded.
- **DOCUMENTED EXCEPTION:** deliberate divergence (reason + review date) or no v4.0 counterpart (needs Section 13 amendment item).
- Divergence with none = F5.

Per-class checks, in order:
1. **Lever order first, every class** (L1: budget, bid, placement, negation, structure, status). Later lever without evidence earlier ones pulled = F7.
2. **A-class step form:** fixed-dollar step vs L2 15-25% at both bounds. Outside at either: ADJUST if platform accepts percentage step, else DOCUMENTED EXCEPTION with AM-4. Record computed percentages.
3. **B-class parameters:** reconcile to nothing -> DOCUMENTED EXCEPTION, AM-1; #29 converting-term guard rides every pause.
4. **C-class scope:** ladders only where efficiency is declared objective (O6). Read objective tag on every entity, not campaign name. Mismatch = F2.
5. **C-class ceiling:** flat max bid vs entity's own max profitable CPC (M1, contribution x CVR). **Above 1.5x** -> S-R11 band, no exception available: ADJUST to tightest ceiling in scope or narrow scope.
6. **D-class transition:** platform hold != v4.0 test (S-R6 2 consecutive weeks; S-E5). Record divergence, enforce via scope (P4) and P8 flag.
7. Record every outcome with manifest state (DEGRADED -> flag not finding, G8).

### P4. Scope-exclusion state management (5 min per change same day; 20 min weekly)
1. **Standing exclusions from B and C at all times:** campaigns with open push worksheet; event campaigns and settling rows inside window and guard; terminal/LTSF-tagged entities (SOP-27); entities under declared manual hold. **A-class adds:** any entity deliberately at a bid floor (M3 discovered value).
2. Reason: pushes run on loss lines, events on caps, terminal on recovery mathematics, holds on a human's reason; efficiency ladder on any = O6 process violation.
3. Maintain same day both directions (push standup adds / close removes; window arming adds / settling removes at end of guard; terminal tag adds week it lands).
4. **Verify in platform, not register**; read scope back after every edit.
5. Weekly reconcile exclusion set vs T2 gate columns and T3 states both directions (stale exclusion = rule silently not running).
6. Apply SOP-15 P11 exclusion-state notices for protected auto scope same session; confirm receipt.

### P5. Change control (10-15 min per change)
1. Creations, edits, deletions are staged decisions: reason string, owner, version, T6 entry with prediction and review date.
2. Reason string per #38 staging contract: component tag, driving outcome/verdict, governing reference, evidence reference.
3. Apply in console, read back, record read-back.
4. Increment register version on every change.
5. Edit without record = F4: revert, reconstruct from console history and #38 T+1 diff.
6. Deletions keep their row, marked retired with date and reason.

### P6. Weekly runaway watch (20-30 min, immediately after P1)
1. Pull rule-fired change counts per entity per window for **trailing 7 days**; single-window comparison while A1 MISSING (artifact says so).
2. Signature = consecutive same-direction steps on one entity in one window. v4.0 has no count (AM-2): **detection convention - flag every entity at 3 or more same-direction rule-fired steps in the window**, recorded as convention, not threshold.
3. Suspend the **entity's** rule action pending read; suspend the rule only if **two or more entities on one rule** flag in same window.
4. Cause read in order: retag since target set; objective change; margin move recomputing ceiling (S-A9); excluded state P4 missed; G1 quarantine.
5. Classic cause = stale target after retag; SOP-12 P4 and P6 retag checklist carries rule-target update step.
6. Quantify before re-enabling: bid at window start vs now, premium per click, clicks in window, dollars.
7. Suspension packet to PPC Lead same day; entity to weekly pass; root cause to the checklist that should have prevented it. Second runaway from one cause escalates the checklist gap.

### P7. Suspension and re-enable (10 min suspend; 20-30 min re-enable)
1. Execute in console and record in register same session, trigger named (F1, F2, F3, F4, F5, F7 or P6 runaway).
2. Scope of freeze: entity, rule or class (class-wide only for defect in governing logic).
3. **Re-enable requires four things at once:** root cause named and fixed at source; reconciliation re-recorded vs current v4.0; scope exclusions verified in console; damage record closed with dollar figure.
4. Re-enable **human-mandatory** (PPC Lead decides, operator executes). **R3** in Recovery Mode: bid moves **> 15%** and budget moves **> $25/day** human-confirmed.
5. Re-enabled **twice for one root cause** -> no third; retires; need met by staged manual procedure.

### P8. Rank-based taper and single-rung boundary (10 min per firing)
1. Rule executes rung one, flags term to ladder process; never walks a term down unattended.
2. Rung value derived at #28 from M3 (~10%/week) inside L2; this SOP checks rule stopped after one.
3. Verify S-R6: organic rank at/under target **2 consecutive weeks**; shorter hold -> recorded, term back to weekly pass without a rung.
4. Verify event state (S-E5): firing inside armed window or its **14-day guard** = F9, reverts.
5. Flag: entity, rung executed, date, rank evidence; term then belongs to #28 and the descent owner.
6. Term inside a scheduled descent owned elsewhere -> revert rung (two descents compound into a step L2 does not permit).

### P9. Precedence: rule action vs staged manual action (15 min per collision)
1. Governing rule **P3**: weekly audit outranks automation between cycles; audit value wins on same target; automation's inter-cycle actions reviewed each audit.
2. Detection = #38 T+1 diff; change claimed by neither session nor rule escalates as #38's unlogged-edit class.
3. Restore audit value first, investigate second (audit value carries J-complete record under rule **P10**).
4. Suspend rule on that entity for the stated read window (this SOP's mechanism, not stated in P3; pending AM-13); immediate resume can re-move value = F6.
5. Record collision in T6 with **conflict flag** set.
6. Recurring collisions on one rule -> fix scope.

### P10. Portfolio-object governance (30-45 min first pass; 10 min weekly)
Console portfolios = second budget-cap surface; symptom = campaign-level truncation with no campaign-level cause.
1. Register every portfolio: name, member campaigns, cap type and value, owner, product envelope it sits inside. No owner -> cap removed, envelope governs alone.
2. Creation human-mandatory (Authority Matrix structure-creation row: PPC Lead decides/delegates, operator executes).
3. Reconcile cap vs envelope instruments (conflict C3): T0 weekly envelope named cell, T1 family caps, Account Rollup A2 cross-product queue. Portfolio caps inside a product, expressed weekly, vs product's declared weekly envelope.
4. Three outcomes: cap >= envelope -> envelope binds, object inert, record; cap < envelope -> portfolio binds, finding routed to envelope owner with suppressed dollars (WE-4); cap < envelope and set to enforce it -> raise cap to envelope or cut envelope to cap in one staged change; never both live.
5. Portfolio with campaigns from more than one product cannot reconcile; restructure (envelope is product-level).
6. v4.0 has no portfolio-cap tolerance or alert bar; G7 governs campaign budgets summing to envelope and pacing deviation **> 25%** vs day-of-week curve; AM-8. Divergence reported at dollar value.
7. Weekly diff console portfolio list vs register (unregistered portfolio = same class as unregistered rule).

### P11. Sync at every v4.0 increment (4-6 h across 24 rules; open within 1 working day, close inside 5)
1. Read change note; list touched rules (thresholds, bands, lever limits, scenario conditions, vocabulary changes).
2. Run P3 on every rule, not only those named.
3. Record new last-synced version on every row.
4. Increment closing an AM item -> move rules out of DOCUMENTED EXCEPTION; close Section 13 entry with the closing version.
5. Increment creating divergence -> ADJUST same session where platform permits, suspend where not.
6. Pass artifact: version from/to, rules read, outcome counts, adjustments prior/new, suspensions, amendments opened/closed.

### P12. Quarterly full pass (5-7 h)
1. P3 every rule, P4 entire exclusion set, P10 every portfolio.
2. Age every documented exception; past review date without renewal -> ADJUST or suspend (no v4.0 max life; AM-10).
3. Read quarter's suspensions as a set: one root cause twice = checklist gap; one class three times = narrower scope or retirement.
4. Re-verify bounds vs current economics (S-A9 ceilings recompute on margin move).
5. Score quarter's rule predictions in T6 (V1); report register's own accuracy beside the account's.
6. Quarterly artifact registered as next quarter's baseline.

### P13. Automation posture in code red and Recovery Mode (45-90 min declaration day; 15 min daily while live)
1. On T5 declaration, deliver product's rule-change log to SOP-26 P3 same day (one of four maps).
2. Freeze rule-fired increases on product same day.
3. Diagnosis names runaway rule -> suspend per P7, review inside protocol window.
4. R3 tightening on every live rule: bid **> 15%** and budget **> $25/day** human-confirmed; step sizes cap at standard even at HIGH confidence; rules that can exceed narrow scope or suspend.
5. Mode precedence (T8, P7): Recovery > Event > stage defaults; Recovery product entering event keeps Recovery posture.
6. On exit restore pre-mode posture as staged change with record; re-verify scope before re-enabling.

### P14. Platform capability, seats, exports, outage recovery (30 min seat change; 2-3 h new rule class)
1. New console rule type registered as class or declined in writing within **5 working days**.
2. New class only with governing v4.0 surface named, guardrails, standing exclusions; else declined, gap logged.
3. Seat/credential changes from #46: same-day reassignment of every row the seat owns; P7 suspension of rules with vacant owner. Vacancy rule: decisions to PPC Lead, execution to PPC Manager.
4. After billing/platform outage restored: suspend rule action on affected scope until **one clean full day** of data lands; G10 has no outage exclusion (AM-9); suspension window stated in T6; dates carry #43 trend-exclusion flag.
5. When D6 export lands: P1 becomes scheduled diff; manual-read flag retires; F1 detection one cycle -> one day; export schema registers (schema change = P14 event).

## 5. Rules, thresholds and numbers

### 5.1 Numeric values

| Value | Meaning / source |
|---|---|
| 4 conditions | Legitimacy test (registered+owner; reconciles; scope; attributable) |
| 9 fields | Register schema |
| 24 rules | Register size: 5 A, 5 B, 13 C (7 one-or-more-order at $2.50, 6 zero-order at $1.20), 1 D |
| $0.05; < 3 clicks | A-class inch-up step and trigger (platform state) |
| $0.30-1.30 / $0.30-1.00 | A-class bounds SP / video and display (platform state) |
| 10 days; 30/30/15/15/12 clicks | B-class window; SP/headline/SBV/SBV-PAT/SD click counts (platform state; AM-1) |
| 5-35% tolerances (step 5); >= 3 clicks; TOS share cap 30; $2.50 / $1.20 | C-class ladders (platform state) |
| 10% increment | C-class configured upward step (WE-3; platform state, not compliance) |
| >= 15 clicks in 7 days | G2 bid-read bar |
| 15-25% | L2 unlock step (S-R1) |
| 50% per change; floor $0.50 | L2 limits; rule bounds must fit |
| ~10% per week | M3 taper step (downward), derived at #28 |
| 2 consecutive weeks | S-R6 rank-at-target hold |
| 1.5x max profitable CPC | S-R11 unjustifiable band outside sized push; F8 detection |
| Max profitable CPC = contribution x CVR | M1 |
| > 25% bid; > $50/day budget; 500+ SV; gate failures; structural; LOW confidence | P5 human-confirm tier |
| > 15% bid; > $25/day budget | R3 Recovery Mode confirm tier |
| >= 70% of day in-budget | G3 truncation line |
| 7 days | G9 price window; P6 trailing window |
| 14 days | G10 post-event exclusion / guard |
| 30 days | G12 MKL currency |
| < 85% | G8 DEGRADED floor; build stamp 0.571 |
| > 25% pacing deviation | G7 alert vs day-of-week curve |
| 13 weeks | Quarterly full-pass interval; weekly artifact retention |
| 1 / 5 working days | Increment pass open / close; new capability registration |
| 3+ same-direction steps | P6 runaway detection convention (not a threshold; AM-2) |
| 2+ entities on one rule | Suspend rule rather than entity |
| 2 re-enables, 1 root cause | Retire (no third) |
| 1 clean full day | Post-outage suspension |
| 1 full cycle | Open suspension escalates to PPC Lead |
| 2 suspensions same root cause in a quarter | Document review trigger |
| 2026-09-25 | #44 operator onboarding due (I-15) |

### 5.2 Criteria System v4.0 references

| ID | Meaning as described |
|---|---|
| G1 | Validation quarantine; rule action suspends |
| G2 | Bid read needs >= 15 clicks in 7 days |
| G3 | In-budget >= 70%; below TRUNCATED, rule-fired bid change void |
| G6 | Inventory band; GREEN required for raises |
| G7 | Campaign budgets sum to envelope; pacing deviation > 25% |
| G8 | Packet completeness; < 85% DEGRADED |
| G9 | Price stability 7 days; PROVISIONAL |
| G10 | Event weeks + 14 days excluded; no outage exclusion |
| G12 | MKL hygiene 30 days |
| L1 | Lever order budget, bid, placement, negation, structure, status |
| L2 | 15-25% unlock step; 50% per-change limit; floor $0.50 |
| L7 | Pause requires log naming exhausted levers |
| M1 | Ceiling per variation = contribution x CVR |
| M2 | Required-clicks sizing (no rule computes) |
| M3 | Discovered floor; taper ~10%/week downward |
| M5 | Funding queue (rules never fund) |
| O6 | Each objective judged on own metric set; Defensive band 10-15% |
| P1 | Gates outrank every signal beneath them (a rule is a signal) |
| P3 | Weekly audit outranks automation between cycles; audit value wins; automation resumes from it |
| P5 | Human-confirm tier |
| P7, T8 | Mode precedence: Recovery > Event > stage defaults |
| P10 | No deploy without J-complete Master Action Record |
| R1, R5 | Recovery entry/exit |
| R3 | Recovery confirm tier tightening |
| V1 | Prediction scoring; unscored actions do not accumulate |
| V3 | Governs how framework changes (not exception life) |
| V4 | Quarterly cadence |
| V5 | Scoring (consumer of T6 change records) |
| S-R1 | Under-15-click case answered with 15-25% steps |
| S-R4 | Forbids bidding a conversion deficit |
| S-R6 | Objective transition after 2 consecutive weeks at/under target rank |
| S-R11 | Spend > 1.5x ceiling unjustifiable outside sized push |
| S-E5 | Rank gained in event window provisional until exclusion window closes |
| S-H7 | Zero-sale spend above an unstated threshold |
| S-A9 | Margin move recomputes ceilings |
| S-D1 | Discovered floor is the control on defended terms; branded terms never scale |
| F11 (family) | Waste as a percentage |
| Section 13.1 | Closed verdict vocabulary |

### 5.3 Verdict mapping: which verdicts a standing rule may execute

| Verdict | Rule may execute | Note |
|---|---|---|
| QUARANTINE: DATA REFRESH | No | G1; rule action suspends |
| UNLOCK TRAFFIC | **Yes, A-class** | S-R1 with L2 15-25% |
| FIX BUDGET (TRUNCATED) | No | Envelope at instrument layer (C3); no budget-class rule registered |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | No | Entity excluded for test duration |
| FUND TEST (UNFUNDED PRIMARY) | No | M5 queue |
| RANK PUSH: FUND SIZED PUSH | No | Push scope excluded; rule inside = F2 |
| RECOVERY PUSH | No | Recovery component |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | No | M2 sizing |
| FIX CONVERSION FIRST; DEFER PUSH | No | S-R4; entity excluded |
| PLACEMENT FIX FIRST | No | #28; no modifier-class rule registered |
| RE-POINT VARIATION | No | Human-mandatory, G6 |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | **Rung one only, D-class** | P8 |
| HOLD; DEFEND LIGHTLY AT RANK | No | Nothing changes |
| DEFEND AT FLOOR | No, entity excluded | Drift restores in one staged step |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | **Bid half only, C-class** | Syntax-cap half is envelope action |
| INCREMENTALITY LADDER | No | Rule stepping destroys read |
| ADD EXACT + RESTRUCTURE | No | Structure human-mandatory (P5) |
| CONSOLIDATE DUPLICATES | No | Survivor selection human |
| GRADUATE FROM DISCOVERY | No | #30 / #12 |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | **Routing only** | Rule surfaces candidates, places nothing |
| ENTER SBV ARBITRAGE | No | #12 |
| OPEN / ROTATE / EXIT CONQUEST | No | #16 |
| STOP-LOSS: CONCEDE OR DEFER | No | Owner concedes |
| PAUSED-PENDING (REASON + RE-ENTRY) | No | B-class pause approximates it = F7 |
| LEAVE TO HARVEST | No | #30 |

Campaign-level subset (FUND BUDGET, HOLD, TRIM BUDGET, RAISE MULTIPLIER, CUT MULTIPLIER, NEGATION PASS, CONSOLIDATE, RETAG OBJECTIVE, PAUSE, ARCHIVE): executed by owning components; **no registered rule executes any today**.

**Register state vocabulary (not verdicts; AM-7):** REGISTERED, SUSPENDED, RETIRED, AGREES, ADJUST, DOCUMENTED EXCEPTION; scope states EXCLUDED, IN SCOPE.

## 6. Data inputs required

| Input | Location / fields | Notes |
|---|---|---|
| Automation platform live rule list | Console; nine fields per rule | D6 export OPEN -> dated, initialled console transcription (I-1) |
| Platform change log | Rule-fired change counts per entity per window, last-change dates, actor (console history) | P1, P6 |
| Rule register | Nine fields + version + last-synced v4.0 version + last full-pass date + portfolio section | Automation section of workbook layer |
| Criteria System v4.0 file | Version stamp | Register currency |
| A2 deployment state | Current bid, budget, state per entity with live rule, timestamped | Stale stops P9 |
| #38 T+1 verification / attribution diff | Every change attributed to session or rule | Absent -> P6, P9 do not run; re-enables freeze (I-4) |
| A3 pacing buckets | PARTIAL | |
| A5 threshold flags in-row | Gate and band flag columns on T2 | |
| A6 objective and Expected CPC | T2 block K7 objective (exactly one per C/D-class entity); Expected CPC at account reference | PARTIAL |
| A8 PAT rows | PARTIAL | SBV-PAT coverage gap |
| A1 four-period comparability | MISSING | Single-window watch |
| B5 coverage counts | Registry counts per match type | |
| B8 economics chain / T0 named cells | AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC | Per variation contribution and CVR for M1 ceilings |
| D1 margin table (Economics and Context Pack) | Version + G9 freshness state | Monthly and on event (I-13) |
| D2 map | Inventory band derivation | |
| T2 block K2 gate columns | Validation (zero-flag), in-budget % (worst hosting campaign), eligibility, inventory band, days to stockout, envelope, cap, event mode/posture | |
| T2 block K4 | Organic rank | D-class verification |
| T3 | Campaign state and objective tags | |
| T5 Product Log | Price change log (trailing 7 days), outage events, code-red declarations | |
| T6 Decision Log | Change records, predictions, review dates, conflict flag | |
| T7 Manifest | Completeness % and field-group states | |
| T1 | Family caps | P10 |
| Account Rollup A2 | Cross-product queue | P10 |
| Console portfolio list | Name, members, cap type/value | P10 |
| MKL | Refresh date; term tags | G12 |
| #32 armed-window record | Dates; settling rows at window close | I-8 |
| SOP-15 P11 exclusion-state notices; SOP-15 per-group rule reporting | | I-2, I-3 |
| #28 ladder hold notice and rung values | | I-5, I-6 |
| SOP-27 / tier system terminal and LTSF tags with dated scope | | I-9 |
| #43 billing incident and restoration records with outage window | | I-10 |
| #46 access reconciliation diff | Automation seats, credential rotation | I-11 |
| Push worksheets (open) | Scope exclusion | |
| Recovery / event mode state | | |
| Floor register (#28 / M3 recorded floors) | | A-class exclusion; WE-3 |

## 7. Outputs / artifacts

| Artifact | Content and storage | Retention | Consumer |
|---|---|---|---|
| Rule register | Nine fields per rule + portfolio section; automation section of workbook layer, versioned continuously | Permanent; retired rows kept | Every procedure; SOP-26 P3; #38 P6 external-change classification |
| Weekly diff artifact | Date, rules read, three counts, mismatches with dispositions, manual-read flag, initials | 13 weeks rolling, then quarterly supersedes | Weekly pass; PPC Lead; P12 |
| Runaway watch report | Flagged entities, step counts, causes, suspensions, damage in dollars | 13 weeks rolling | PPC Lead same day; SOP-26 P3 |
| Reconciliation record | Per rule: outcome, v4.0 section and rule ID, both values, date, manifest state | Permanent, by version | v4.1 amendment brief; quarterly pass; #1 governance |
| Change records (T6) | Creations/edits/deletions with reason string, owner, prediction, review date | Permanent, append-only | V5 scoring; #38 attribution; audit |
| Suspension packet | Trigger, freeze scope, root cause, damage record, re-enable conditions | Permanent | PPC Lead; checklist owner |
| Exclusion set | Entity list by exclusion class with state that put each there | Live, reconciled weekly | SOP-15 P11; #32; SOP-27; weekly pass |
| Portfolio register section | Object, members, cap, owner, envelope reconciliation and dollar delta | Permanent | Envelope owner; #38 |
| Sync pass artifact | Version from/to, rules read, outcome counts, adjustments, suspensions, amendments | Permanent, one per increment | #1 Supersession Map; SOPs re-validating Element 10 |
| Quarterly full-pass artifact | Complete register state, exception ages, prediction scores, pattern read | Permanent | Next quarter's baseline; #44 onboarding |
| P8 flag | Entity, rung executed, date, rank evidence | | #28 |
| Reason string (P5) | Component tag, driving outcome/verdict, governing reference, evidence reference | | #38 |

Standing gate artifact = register at last sync. Weekly artifact = diff + runaway report; "a week with neither did not happen."

## 8. Decision rights

| Decision | Who |
|---|---|
| Authority Matrix automation-rules (#37) row | **PPC Lead decides**; incoming operator executes and reviews (holds E and R); PPC Manager executes; CEO and BM owner informed |
| Rule creation and re-enable | Human-mandatory; PPC Lead decides |
| Documented exceptions and renewals | Human-mandatory |
| Suspensions on push scope | Human-mandatory |
| Portfolio creation | Human-mandatory per structure-creation row (PPC Lead decides/delegates, operator executes) |
| P13 posture change on code red | Code-red row gives PPC Lead the close |
| Anything staged through #38 | Bulk-deployment row |
| Portfolio cap vs envelope finding | Envelope owner decides (WE-4) |
| E without D | Executes staged decisions only (matrix standing rule) |
| Vacancy rule | Decisions -> PPC Lead; execution -> PPC Manager |
| AI-executable with audit | P1 transcription and diff, reconciliation drafting, runaway detection and damage arithmetic, exclusion reconciliation from state feeds, P10 envelope arithmetic, every artifact draft |
| Requester of a rule | Must supply bounds, scope and governing v4.0 section |

**Escalation:** F2 on push/terminal scope same day; F7 and F8 on discovery (class not instance); second occurrence from same root cause escalates checklist gap; suspension open > one full cycle -> PPC Lead with damage record; unattributable edit -> PPC Lead + #46. Alarm routing: same day to operator queue F1, F2, F9, F10, F11; weekly worklist F3, F4, F5, F6, F12; PPC Lead on discovery F7, F8.

**Operator ramp:** Week 1 (written read of 5 rules naming v4.0 section and both values; list of procedures degraded by D6); Week 2 (supervised P1, P4, P5, P6; one P3 class reconciliation accepted unchanged; one correctly refused action above E-without-D line); Week 4 (four consecutive audited weekly sets with zero unexplained mismatches vs #38 T+1; one complete suspension packet; one amendment item with no invented number).

## 9. Account-specific facts

- **Register: 24 rules** seeded from live platform 2026-07: 5 A-class inch-up (one per ad type: SP, headline, SBV, SBV-PAT, SD), 5 B-class pause-at-zero, 13 C-class ladders (7 one-or-more-order @ $2.50 max bid, 6 zero-order @ $1.20), 1 D-class taper.
- v1.0 seeding pass: 21 AGREES, 1 ADJUST, 1 DOCUMENTED EXCEPTION, 1 SUSPENDED.
- **v2.0 re-run result (WE-1): 6 AGREES (6 zero-order C, with G9 provisional flag), 12 ADJUST (5 B-class: pause half removed, bid-floor half kept; 7 one-or-more-order C: $2.50 cap = 1.71x ceiling), 6 DOCUMENTED EXCEPTION (5 A-class safe-side AM-4; 1 D-class enforced via scope and P8)**; one ADJUST rule also suspended pending root-cause fix (WE-3); 2 scope exclusions landed same day.
- **Recorded incident 1 (F2):** zero-order ladder found live on **2 campaigns carrying open push worksheets**.
- **Recorded incident 2 (F3 / WE-3):** a C-class target-ACOS ladder walked a branded defensive term (retagged to Defensive, target left stale) up **6 consecutive weekly 10% steps** from discovered floor $1.10 to $1.95; found by code-red four-map diagnosis; survived **six weeks** (absence of I-14). Fix: bid restored to $1.10 in one step; SOP-12 P4/P6 retag checklist gains rule-target update step; branded defended terms at recorded floor added to A-class standing exclusion.
- No budget-class rule and no modifier-class rule is registered.
- Manifest at build: A1 MISSING; A3, A6, A8 PARTIAL; packet completeness **0.571** (DEGRADED).
- Decision on WE-2: account takes "cap to tightest ceiling" ($1.28) this cycle and "split per variation" at next quarterly pass, recording the 33.3% headroom cost.
- Worked examples on fictional training base (AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max Acc 26.3%, CVR 5.2%):
  - WE-1: A-class step 0.05/0.30 = 16.7% (inside band), 0.05/1.30 = 3.8%; in band only $0.30-$0.333 (3.3% of range); 3.9 firings to reach L2's smallest step at $1.30. Max profitable CPC 28.00 x 0.052 = $1.46; $2.50 / $1.46 = 1.71x.
  - WE-2: three variations ceilings $1.46, $1.28 (contribution $24.60), $1.92 (contribution $31.40, CVR 6.1%). At $2.50: cost/order $48.08, loss $20.08/order; 40 clicks/week = $100.00 spend, 2.08 orders, $58.24 contribution, net loss $41.76/week, $2,171.52/year; sales $166.40, ACOS 60.1% = 1.72x BE. Capping at $1.28 costs variation 3 33.3% headroom.
  - WE-3: CVR 18.0% branded; ladder $1.10 -> 1.21, 1.33, 1.46, 1.61, 1.77, 1.95; premium $0.85/click; 30 clicks/week = $25.50/week, $1,326.00/year; accumulated walk premium $2.73/click, $81.90; ACOS at floor 7.6% (cost/order $6.11), at end 13.5% (cost/order $10.83); Defensive band 10-15%; 77% more per click than floor.
  - WE-4 (illustrative): weekly envelope $4,259 ($608.43/day); 6 campaigns in one unregistered portfolio capped $500/day; in-budget 64.9% (< 70%); suppression $108.43/day, $759.00/week, 17.8% of envelope; fix options raise cap to $608/day or cut envelope to $3,500/week; blocked by armed #32 event window; staged for window close.

## 10. Open items

### Amendment register (v4.1)

| ID | Gap | Where it belongs |
|---|---|---|
| AM-1 (highest priority) | Per-ad-type zero-order pause parameters (click count and window) | Section 8.9 S-H7 (unstated threshold); Section 3 F11 (waste %) |
| AM-2 | Consecutive-step count defining a runaway | v4.0 consecutive-period language is weeks in scenarios, never ladder steps |
| AM-3 | Governed upward step size and per-window repeat cap for rule-fired increases | L2 (15-25% unlock, 50% limit); M3 (~10%/week downward); nothing governs repeated raises |
| AM-4 | Admission of fixed-dollar step form, or rule that steps are percent only | L2 percent; WE-1 16.7% vs 3.8% |
| AM-5 | Requirement that platform max-bid fields derive from entity's own ceiling | M1; S-A9 (Section 8.1) |
| AM-6 | Whether a rule-fired change owes its own justification record | Section 12 rule P10 (J-complete Master Action Record) |
| AM-7 | Formal admission of register-state vocabulary | Section 13.1 closed vocabulary |
| AM-8 | Portfolio-cap tolerance vs product envelope and alert bar | Section 5 G7 (doesn't name portfolio object) |
| AM-9 | Outage exclusion window for rule reads and trend verdicts | G10 (event weeks + 14 days only) |
| AM-10 | Maximum life for a documented exception | Section 14 V3 governs framework change only |
| AM-11 | Automation-platform export schema (D6) | Dependency specification, not v4.0 |
| AM-12 | Human-confirm tier for the standing decision, not only the action | Section 12 P5 (25% bids, $50/day budgets) |
| AM-13 | Whether a staged manual decision suspends rule action for its read window | Section 12 P3 (resume vs stand off) |

### Conflicts found (13.1; no identifiers minted)
1. **v4.0 rule P3 vs SOP-37 v1.0 P7** on post-collision behaviour (resume from audit value vs suspend for read window). Resolution: audit value restored unconditionally; read-window suspension carried as implementation mechanism (P9 step 4) pending AM-13.
2. **Two D-number namespaces collide:** Ledger Section 2 external dependencies D1-D7 (D6 = automation rules export) vs Metric Expansion Catalog / Data Architecture field groups D1-D12 (D6 = twin-set and sibling view). D1, D2 coincide; D3, D5, D6 do not. Fix: prefix Ledger dependency IDs.
3. **Ledger version narrative inconsistent:** header v2.9 describes Wave 1 return of #43 with Wave 2 gate met; Section 1 carries rows through Wave 5A up to v2.9; pack version note says Ledger v2.5 with Wave 4 closed and Wave 5A open.

### Already-registered items re-encountered (13.2)
- Gate-numbering divergence: corpus uses G12 for event-window freeze; v4.0 assigns G10 event exclusion, G12 MKL hygiene (registered by SB/SBV/SD playbook build). This SOP uses v4.0 numbering.
- Closed-vocabulary count divergence 18 / 25 / 26 strings (registered by #41 and #46 builds); this SOP maps the 25-string KDR v3.0 list.
- **C3:** #31 dangling procedure citations; P10 reconciles to instrument and tab.
- **C6:** LTSF/terminal tier system outside corpus.
- **D6:** automation platform rules export OPEN.
- Page count inconsistency: "Page 18 of 18" vs footer "of 20".

### 16 interface contracts (non-arrival)
I-1 platform via Data Ops (live rule list, change log; weekly before packet-ready): transcription with manual-read flag; if no console read, no outcomes, unread-week marker. I-2 SOP-15 P11 exclusion notices: auto groups stay in B/C scope by default; weekly P4 fallback. I-3 SOP-15 per-group rule reporting: account-level counts only. I-4 #38 T+1 diff: P6, P9 do not run; re-enables freeze. I-5 #28 hold notice: compounding descents; P8 step 6 catches late. I-6 #28 rung value: flag holds, no rung deploys. I-7 this SOP to SOP-26 P3 (rule-change log, same day): one map missing. I-8 #32 armed-window record: default exclude product entities from B/C on unconfirmed window signal. I-9 SOP-27 / tier system tags: weekly T2 fallback. I-10 #43 incident/restoration: F11 undetected. I-11 #46 access diff: vacancy rule by default. I-12 instrument layer envelope and family caps: unreconcilable caps removed, envelope governs alone. I-13 Economics and Context Pack D1 margin table: ceilings stale, G9 flag, F8 risk. I-14 this SOP to weekly pass and T6 (before T2 verdict work): prior values unreliable (caused the 6-week runaway survival). I-15 this SOP to #44 onboarding (due 2026-09-25). I-16 this SOP to #1 governance and Supersession Map.

### Failure modes
F1 unregistered rule; F2 rules on excluded scope; F3 stale target after retag; F4 silent rule edit; F5 undocumented divergence; F6 double-touch; F7 lever-order violation; F8 ceiling-blind cap (> 1.5x tightest ceiling); F9 event-window firing (window or 14-day guard); F10 rule firing through failed gate (G1, G3, G6 YELLOW/RED, G9); F11 post-outage firing; F12 portfolio-cap collision.

### Named documents referenced (not present)
Master PPC Decision Criteria System v4.0; Keyword Decision Record Template v3.0; PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0; PPC Cross-Reference Ledger; PPC Strategic Doctrine v1.0; Metric Expansion Catalog; Economics and Context Pack; Gap Register (portfolio-object fold-in absorbed); Supersession Map; SOP-12, 15, 26, 27, 28, 29, 30, 32, 38, 43, 44, 46; #1 governance; #31 (no procedures).
