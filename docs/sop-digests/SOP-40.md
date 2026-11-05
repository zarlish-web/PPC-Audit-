# SOP-40 Digest: Monthly, Quarterly and Annual Cadence

Source: `PPC_SOP_40_Monthly_Quarterly_Annual_Cadence_v1_0.pdf` (10 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-40: Monthly, Quarterly and Annual Cadence (Operating SOP, Component #40 of the Operations Definition Register) |
| Version | 1.0 (first build, no prior version; nothing carried forward) |
| Date | 2026-08-10 |
| Owner | PPC Lead |
| Thresholds | Master PPC Decision Criteria System v4.0 only; **zero local thresholds, zero verdicts of its own** |
| Ledger grant | Ledger row 40: "the operating calendar above the weekly cycle" and nothing beyond it |

**Verdict / purpose.** The weekly cycle cannot see its own drift, so the calendar above it exists to run exactly the reads whose evidence window is longer than seven days. v4.0 Section 14 (Layer 9: Verification and Learning, V1-V8), **rule V4**, fixes the ladder: **monthly** = override review, structure targets (**M6**), objective mix (**O8**), stage reviews (**T7**); **quarterly** = floor re-tests (**M3**), defense budgets (**M8**), family-level **M5**, framework review. This SOP owns the **placement, convening, evidence assembly, gate clearance, deferral control and closure** of those slots, and nothing else; every band, tolerance and verdict belongs to v4.0 and to the owning SOP. Failure prevented (already exhibited by the account): weekly pass running cleanly for **thirteen weeks** while **structure mix sits 19.6 pp above its band top**, **phrase layer at $0 against a 5-10% floor**, and no scheduled read that would surface either.

**Evidence windows (1.1):** Monthly = reads needing **four consecutive weekly observations** (override rate, spend mix vs M6, objective mix vs stage target, stage tag). Quarterly = reads needing **thirteen weeks** (floor re-test vs moved auction, defense budget re-priced vs moved organic position, family-level M5 across siblings, framework accuracy). Annual = reads whose class cadence is set inside other components; **v4.0 sets no annual threshold of any kind**. "A slot is a position in time. A tolerance is a number. This SOP owns the first and never the second." Slip tolerance logged as amendment item, not written here.

Why 10 pages (1.2): the four things the corpus never wrote down: evidence assembly before each read, gate state (verdict vs flag), routing of each finding into an owned item in another SOP, recovery path when a slot is missed.

## 2. Scope & boundaries

**Owns:** slot placement, convening, evidence assembly, gate clearance, deferral control, closure; cadence register; annual read register; missed-slot recovery.
**Does not own:** any threshold, band, tolerance, verdict, or cadence rule (incl. V4 itself); never re-runs a weekly pass; never recomputes a margin; never edits a rule; never declares owner, window, or releases a dollar.

| Adjacent component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, scenario, verdict, cadence rule incl. V4. This SOP schedules/convenes, never decides. A tolerance in this SOP instead of v4.0 is a defect. |
| #4 Weekly & daily operating cadence | Owns day/time calendar for weekly cycle. This SOP places slots above it, never restates a weekly/daily slot. **Collisions resolve in favour of #4.** |
| #36 Weekly audit execution | Owns weekly audit pass & reconciliation. This SOP consumes accumulated output over 4 or 13 weeks; never re-runs a weekly pass in a monthly slot. |
| #6 V5 prediction scoring | Owns scoring rubric, debt sweep, owner-level calibration, quarterly confidence calibration. This SOP places the slots; files nothing into rubric. Current doc v2.0 per Ledger row #6; no procedure number load-bearing. |
| #35 Incrementality testing | Owns test register, class calendar, finding. This SOP de-conflicts quarterly re-ladder slot vs open tests (rung read and floor re-test never on one entity). Current doc v2.0; release seam runs to SOP-26 P12. |
| #26 Mature & defend incl. code red | Owns quarterly re-ladder by term cohort, annual defense-cost read, defensive membership register, code-red protocol. This SOP convenes; #26 decides. |
| #28 Placement & modifier operations | Owns ladder mechanics, descent floor derivation, drift restoration. Every quarterly floor re-test executes through it. |
| #12 Exact campaign operations | Executes campaign-level bid/budget steps a re-test produces; holds taper & floor record in its registry. |
| #33 Sibling & family arbitration | Owns shared-term ownership declaration & family composite. Quarterly family read hands ranking there; never declares owner. |
| #31 Budget & envelope | Absorbed into instruments per **conflict C3**. Queue ordering & envelope state read at Account Rollup **A2** tab and Command Workbook, never at a #31 procedure number. |
| #41 Margin table & economics refresh | Owns monthly per-variation margin refresh, version stamp, G9 freshness state. Treated as precondition; never recomputes margin. |
| #37 Automation platform rules | Owns rule register & change control. Monthly slot reads its diff as evidence; never edits a rule. |
| #38 Bulk-file deployment mechanics | Owns staging, upload, T+1 verification. Anything a cadence review stages leaves through it. |
| #32 Deal & event window operations | Owns window declaration & arming. This SOP blacks out slots inside armed windows and re-slots; never declares/lifts a window. |
| #1 Document governance & supersession | Owns numbering & Supersession Map; this SOP registers at publication and every version increment. |
| #44 Operator onboarding & certification | Consumes Element 11. Due **2026-09-25** per its Ledger row; until it exists, Element 11 runs under PPC Lead directly. |
| #3 Decision rights & authority matrix | Owns who decides. Authority Matrix v2.0 has no row for cadence-review decisions; inherited rows named in Element 11; missing row = **AM-6**. |
| #25 (descent), #30 (discovery graduation), #13 (restructure), Data Operations | Named as verdict issuers in Element 5 (see §5). |

## 3. Triggers

Slot positions are calendar anchors owned by this component, not tolerances; no late-slot tolerance written here (AM-1).

| Trigger | Detecting artifact | Procedure / slot position |
|---|---|---|
| Month end reached | Cadence line in PPC Command Workbook **READ ME** and **A0 Account Command** refresh for closing month | **P2** opens at first Monday cascade whose **T0-T2 pass has closed** after month end; never before (unclosed surface = partial month) |
| Quarter end reached | Same cascade close, with **thirteenth weekly T6 block** complete for quarter | **P8** at first Monday cascade after quarter end. Closing month's monthly slot runs first, same week; quarterly consumes its output |
| Annual anchor reached | Annual read register (Element 8) | **P13** opens at the quarterly slot carrying the annual anchor (no fifth slot class) |
| Margin refresh landed | Margin table version stamp and **G9** state from #41 | Precondition for P2 step 3. Stamp older than closing month holds every ceiling-referencing read at flag level |
| Manifest degradation | **T7 Manifest** completeness rollup per product | P2 step 4 decision tree, per v4.0 Section 5 (Layer 0: Gates G1-G12), **gate G8** |
| Event window armed across a slot | **G12** arming from #32 event plan, carried in **T2** and **T0 zone B** event posture | P1 step 5: blackout & re-slot. Reads in window + guard zone excluded per **gate G10** |
| Recovery Mode entered | Product code-red flag on **A0** and mode entry log | P1 step 6: mode precedence per v4.0 Section 12 (Layer 7, P1-P10) **rule P7**. Slots continue; scope narrows to mode's triage set |
| Recovery Mode exited | Exit log with recovered weekly dollars | Post-mortem required by v4.0 Section 11 **rule R6** and Section 14 **rule V7** enters next monthly docket as standing item |
| v4.0 version increment | Version stamp on Criteria System file and Supersession Map entry | **P12 step 5** re-validation at first slot of either class after increment, before any read runs |
| Rule accuracy breach | **A3 V5 Scoreboard** by rule & scenario ID, from #6 | Monthly docket item under **rule V5** (accuracy line + scored-prediction count that opens a rule review) |
| Scoring debt reported | Debt count returned by #6 | Monthly docket item; reported, never re-scored in slot |
| Slot missed | Cadence register's open-slot line | **P13 steps 4-6** recovery path (reconstruct, not skip) |

## 4. Procedures

### Preconditions & gates (Element 3)
A slot opens on artifacts, not availability. A field group short of requirement **does not stop the slot; it narrows it**, and the narrowing is recorded in the closing record with a count. (Field groups per T7 Manifest tab; see §6.)
Gates across every slot: **G8** packet completeness decides verdict-bearing vs flag-only; **G10** removes event weeks + guard from every trend read; **G12** MKL hygiene degrades manifest when keyword list stale (hits coverage & mix reads first). **Rule P8**: quarantine/degraded manifest ranks above every other consideration incl. urgency; degraded slot repairs data before producing findings.

### P1. Place the year: build slot skeleton (90 min/yr; 20 min per re-slot)
1. In cadence register write **12 monthly + 4 quarterly slots** for coming year. Each slot: slot class, anchor date, products in scope, convening role, reads it must produce.
2. Anchor monthly to **first Monday cascade after month end**; quarterly to **first Monday cascade after quarter end**. Anchor is the cascade, not calendar date.
3. Collision check vs #4 calendar. If monthly slot would consume cascade time #4 allocated, monthly slot moves to **same week's later day**; weekly cycle never displaced.
4. Write the four quarterly read lists from V4; mark which quarterly slot carries annual anchor (**one per year**; register names which).
5. **Blackout rule:** read confirmed deal windows from #32 event plan. Slot whose anchor falls inside armed window or post-window guard moves to **first cascade after guard closes**; register records original anchor, new anchor, window reference. Not compressed, not skipped.
6. **Mode rule:** product in Recovery Mode keeps slots; scope narrows to triage set; findings route inside the mode, per **rule T8** (Recovery Mode > Event Mode > stage defaults).
7. Publish skeleton to Element 11 roles; register against #1. Re-issued whole at any org change touching convening roles.

### P2. Monthly evidence assembly & packet-state call (45 min/product)
1. Confirm closing month's **four weekly cascades** all closed. Unclosed cascade = three-week month, reads as one; missing week named.
2. Pull: **T6 Decision Log** rows dated in month; **A3 V5 Scoreboard** detail for same rows; **A4 Structure Targets**; **T0 zone F** TACOS decomposition; **T0 zone E** product state vector; **T7 Manifest** as it stood at each of month's four refreshes.
3. Read margin state from #41. If stamp predates closing month, every ceiling-referencing read carries **provisional flag** and says so in finding line.
4. **Packet-state decision tree** (manifest completeness rollup):
   - At/above v4.0 Section 3 **family F15 FULL** line -> verdict-bearing findings routed to owning SOPs.
   - Inside **WORKABLE** band -> findings issue; each finding depending on a partial field group carries that group's ID in flag line.
   - Below **DEGRADED** line of **gate G8** -> **flags and data-repair tasks only** (with owners & dates), no verdict-bearing findings. "Not a reduced slot."
5. Record packet state, completeness figure, field groups short of requirement in **opening line** of monthly record (what it could not see before what it found).

### P3. Monthly read 1: override fold & rule-level accuracy (40 min)
1. Count month's drafted verdicts and human overrides (T6). **Override rate = overrides / drafted verdicts**; hold beside **prior three months** (direction, not level).
2. Group overrides by reason. Reason class recurring across products = candidate threshold/scenario amendment.
3. Rule- and scenario-level accuracy from A3 (#6); apply **V5** accuracy line & scored-prediction count. Rules crossing line enter review; slot lists, never amends.
4. Fold validated overrides into amendment docket as proposals under **rule V3** (versioned amendment with supersession note; forbids oral re-derivation). Proposal is not a live threshold.
5. Record scoring-debt count from #6 without re-scoring.

### P4. Monthly read 2: structure targets vs M6 (35 min/product)
1. Open A4. Read **match-type actual vs band** for exact, broad, phrase, auto, PAT; then **format actual vs band** for SP, SB, SD. Bands are v4.0 Section 10 (Layer 5 Sizing Mathematics M1-M10) **rule M6**, read where workbook computes them.
2. Compute deviation in **percentage points and dollars** for every out-of-band line. pp sizes; dollars route (2-pt deviation on $30,000 month outranks 9-pt on $900).
3. M6 governing clause: **deviations are findings to explain, never errors to auto-correct**. A blanket budget shift violates the rule.
4. Explained deviation -> keyword-level verdict that closes it (Element 5). Unexplained -> owning SOP with deviation figure and review date = next monthly slot.
5. **Carry forward:** deviation present at **three consecutive monthly slots** without closing verdict escalates to PPC Lead with the three figures.

### P5. Monthly read 3: objective mix vs stage target (30 min/product)
1. Read T0 zone F TACOS decomposition: spend and share of sales by **Ranking, Conversions, Defense, Discovery, Conquest, UNTAGGED**; rows reconcile to total TACOS.
2. Compare actual mix to stage target mix (targets & finding requirement in v4.0 Section 6, Layer 1 Objective Assignment O1-O8, **rule O8**: monthly product finding to be explained or corrected).
3. Read UNTAGGED alone: an assignment gap under **rule O1**; every dollar routes to assignment worklist.
4. Mix and structure both out of band on same product -> **one combined finding**.
5. File mix finding beside structure finding.

### P6. Monthly read 4: stage renewal (25 min/product)
1. Read stage tag, declaration date, evidence from **T0 zone E** and **A0 stage and expiry columns**.
2. Confirm or transition each tag per **rule T7**, read against stage gates of **rule T2**. Never carried because nothing changed.
3. Expired ranking-push tag without rank evidence transitions per T7, moving product TACOS band and re-posing product-level checks of v4.0 Section 8.1 (S-A).
4. Record every transition with evidence line and new band. Transition without evidence line = F9.
5. Hand transitioned products to weekly cycle (next pass reads under new band).

### P7. Monthly close (30 min)
1. Assemble **Monthly Cadence Record**: packet state & completeness; four reads with figures; every finding with owner & review date; amendment docket additions; count of reads deferred with reason.
2. Every finding names an owning component **by number** (otherwise this SOP is writing a verdict).
3. File record beside period's T6 rows; post docket additions to amendment register.
4. Close slot in cadence register with actual date; open next slot's anchor.

### P8. Quarterly evidence assembly (60 min)
1. Run closing month's monthly slot first, same week (quarter consumes **three monthly records**; two records = two-month quarter).
2. Pull 13-week surfaces: recorded floors & dates from exact registry; defense budget declarations by syntax; **A2** cross-product queue with funded & queued lines; **A3** grouped by confidence band.
3. Read open incrementality tests from #35; mark every entity under test -> **excluded from quarterly re-ladder slot** this quarter.
4. Apply P2 packet-state tree at quarter scope; record state.

### P9. Quarterly read 1: floor re-tests (50 min + execution by #28/#12)
1. List every recorded floor older than **rule M3** re-test interval (re-test discovered minimum viable CPC **quarterly or after a logged competitive shock**).
2. Sort by **premium $/week = (floor bid - term's max profitable CPC) x maintenance clicks/week**. Premium sizes the prize; age only qualifies.
3. Exclude: entities under incrementality test; entities inside armed event window; entities whose product is in Recovery Mode.
4. Hand cohort to #28 (ladder mechanics) and #12 (campaign execution) with Element 5 verdict string. Step size is v4.0 Section 9 (Layer 4 Lever Library L1-L10) **rule L2**; SOP does not size a step.
5. Set read date at interval executing SOPs carry; record cohort in quarterly record for scoring next quarter.

### P10. Quarterly read 2: defense budgets (40 min)
1. List every primary syntax with declared defense budget and declaration date.
2. Re-declare against **rule M8** (price from organic revenue at risk x displacement probability, bounded by syntax contribution margin; declaration required quarterly).
3. Read syntax organic share vs declared target beside budget. **Budget rising while organic share falls = renting pattern, scenario S-A5** -> routes there, not to larger budget.
4. Hand every re-declaration to #26 (declares). Slot produces schedule & evidence pack.
5. Record prior & new declarations side by side. Budget unmoved in **three quarterly slots** = either correct or unexamined.

### P11. Quarterly read 3: family-level M5 (45 min)
1. Open **A1 Family Boards** and **A2 Cross-product M5 Queue**. Every family with >1 live product must have both sibling rows populated.
2. Rank pushes across products on **rule M5** ordering: fund by **revenue potential at target rank / cost to close the gap**, at family level quarterly per Section 8.11 (Sibling & Portfolio Scenarios S-B1 to S-B6) **scenario S-B6**.
3. Tiebreak: **margin-dollar class, earning-potential class, inventory depth**. Ranking reversing a live within-product order = finding, stated with both figures.
4. Shared-term ownership -> #33 (declares); funding -> queue instrument. Slot ranks only.
5. Family board can't compute (empty sibling row) -> record **no-push guard** as standing and name missing input.

### P12. Quarterly read 4: framework review & confidence calibration (60 min)
1. Realized accuracy across confidence bands from A3; **rule V6** recalibrates confidence weights when band's realized accuracy contradicts label.
2. Rules that entered review under V5 in quarter's three monthly slots each close as amendment proposal, threshold-change proposal, or documented defense. **A rule may not stay in review across two quarterly slots.**
3. Assemble quarter's amendment docket: monthly override folds, V5 outcomes, V6 calibration result, Recovery post-mortems (R6), every AM item logged by build sessions in period.
4. Route docket to threshold owner as single versioned package under V3. Authority Matrix places v4.0 threshold-change decision with **CEO**.
5. On any v4.0 increment, re-validate Element 5 mapping and every citation before next slot of either class.

### P13. Annual reads & missed-slot recovery (50 min annual; 30 min per recovery)
1. Open annual read register: annual defense-cost read at **#26**; annual test classes at **#35**; any read another SOP has declared annual.
2. Convene each inside the quarterly slot carrying annual anchor. SOP schedules/assembles; owner reads/decides.
3. Annual read with no v4.0 threshold basis -> evidence pack + amendment item, **no number** (AM-2).
4. Recovery step 1: detect at next slot's opening (open slot whose anchor passed); by register, never memory.
5. Recovery step 2: **reconstruct rather than skip**; reads whose window is contaminated by event window or mode entry are marked **contaminated**.
6. Recovery step 3: record miss, cause class, reads recovered vs lost. **Two consecutive misses of one slot class escalate to PPC Lead** with both records.

## 5. Rules, thresholds & numbers

### 5.1 Criteria System v4.0 rule references

| Rule ID | Meaning as described in SOP-40 |
|---|---|
| V4 | Cadence ladder (daily, weekly, monthly, quarterly; stops, no annual). Monthly: override review, M6, O8, T7. Quarterly: M3, M8, family M5, framework review |
| V3 | Versioned amendment with supersession note; forbids oral re-derivation |
| V5 | Accuracy line + scored-prediction count that opens a rule review |
| V6 | Recalibrate confidence weights when band's realized accuracy contradicts its label |
| V7 | Recovery post-mortem obligation (with R6) |
| M3 | Re-test discovered minimum viable CPC quarterly or after logged competitive shock |
| M5 | Fund by revenue potential at target rank / cost to close gap; family level quarterly |
| M6 | Structure target bands (match-type and format); deviations are findings to explain, never auto-correct |
| M8 | Syntax defense budget from organic revenue at risk and displacement probability, bounded by syntax CM; declared quarterly |
| O1 | Objective assignment; UNTAGGED spend = assignment gap |
| O8 | Actual objective mix vs stage target = monthly product finding |
| T2 | Stage gates |
| T7 | Stage tag confirm/transition criteria; expired ranking-push tag without rank evidence transitions |
| T8 | Recovery Mode > Event Mode > stage defaults |
| R6 | Recovery Mode post-mortem |
| P7 | Mode precedence (Recovery Mode entry) |
| P8 | Quarantine/degraded manifest ranks above every other consideration incl. urgency; repair data same day |
| L2 | Ladder step size, approx. 10% per week (per WE-2) |
| G8 | Packet completeness: DEGRADED line -> flag-only |
| G9 | Margin freshness state (from #41) |
| G10 | Event weeks + guard excluded from trend verdicts |
| G12 | Event window arming; also MKL hygiene degrades manifest when keyword list stale |
| F15 | Section 3 family: completeness bands FULL / WORKABLE / DEGRADED |
| X12 | Section 4 rule cited with "DEFEND AT FLOOR, with the test" for cannibalization |
| S-A5 | Renting pattern (defense budget up while organic share down) |
| S-B6 | Family-level M5 quarterly |
| Section 8.1 S-A | Product-level scenarios (re-posed on stage transition) |
| Section 3 Layer M F1-F16 | Bands must pre-compute as columns |
| Section 13.1 | Closed Verdict Vocabulary (18 strings) |

### 5.2 Numbers and windows

| Item | Value |
|---|---|
| Monthly evidence window | 4 consecutive weekly observations |
| Quarterly evidence window | 13 weeks |
| Slots per year | 12 monthly + 4 quarterly; 1 quarterly carries annual anchor |
| Monthly anchor | First Monday cascade after month end (after T0-T2 pass closed) |
| Quarterly anchor | First Monday cascade after quarter end |
| Override rate trend | Current month beside prior 3 months |
| Structure carry-forward escalation | 3 consecutive monthly slots (AM-5) |
| Defense budget unmoved flag | 3 quarterly slots |
| Rule in review limit | Not across 2 quarterly slots |
| Missed slot escalation | 2 consecutive misses of one class (structural, not tolerance) |
| Undeclared defense escalation (I-5) | 2 consecutive quarters |
| Failure-mode escalation | Same failure at 2 consecutive slots of one class; F2, F6, F10 at first occurrence |
| Durations | P1 90 min/yr (20/re-slot); P2 45/product; P3 40; P4 35/product; P5 30/product; P6 25/product; P7 30; P8 60; P9 50 + execution; P10 40; P11 45; P12 60; P13 50 annual / 30 per recovery |
| Manifest | 28 field-group rows; partial weighted at 0.5 (manifest formula) |
| Retention | Cadence register: current + prior program year; Monthly record: 12 months min; Quarterly: current + prior program year; Deferral/miss log: permanent for program year |
| Closed vocab counts | 18 (v4.0 13.1), 25 (KDR v3.0), 26 (Data Architecture / Ledger #38 row) |
| #44 due | 2026-09-25 |
| Phrase floor | 5-10% band (5.0% floor) |
| Exact band top | 60.0%; broad band top 20.0% |

### 5.3 Zero local thresholds (5.1 statement)
- **No annual cadence rule** (V4 stops at quarterly) -> AM-2.
- **No slip tolerance** -> AM-1 (P13 escalation on 2 consecutive misses is structural).
- **No cadence-specific completeness line**; uses F15 bands and G8 line; whether valid at monthly scale -> AM-4.

### 5.4 Verdict mapping (Element 5) - verbatim strings
| Cadence finding | KDR v3.0 string | v4.0 13.1 string | Issued by |
|---|---|---|---|
| Recorded floor stale at quarterly slot, premium confirmed | TAPER: RANK ACHIEVED, STEP BIDS DOWN | TAPER TO FLOOR (POST-OBJECTIVE) | #28 mechanics, #12 execution |
| Floor re-test slips, restoration required | DEFEND AT FLOOR | DEFEND AT FLOOR | #28, #26 |
| Exact share above band top with dollars | BID DOWN TO PROFITABLE CPC; CAP SYNTAX | BID DOWN TO PROFITABLE CPC; CAP SYNTAX | #12 campaign level, cap half at instrument layer |
| Phrase/exact coverage short of band floor on proven roots | ADD EXACT + RESTRUCTURE | ADD EXACT + RESTRUCTURE | #12, #13 |
| Discovery yield unconverted across month | GRADUATE FROM DISCOVERY | GRADUATE + STEER | #30 |
| Defense budget re-declared, cannibalization suspected | INCREMENTALITY LADDER | DEFEND AT FLOOR, with the test per Section 4 rule X12 | #35 designs, #26 releases |
| Family read reverses within-product funding order | STOP-LOSS: CONCEDE OR DEFER | PORTFOLIO CALL: ASSIGN LEAD | #33 declares, queue instrument funds |
| Packet degraded at slot | QUARANTINE: DATA REFRESH | FLAG: DATA REPAIR | Data Operations, per G8 |
| Stage transition to lower band | HOLD; DEFEND LIGHTLY AT RANK | CONTINUE; VERIFY MOMENTUM | #25 on descent, #26 at steady state |
| Untagged spend in mix read | PAUSED-PENDING (REASON + RE-ENTRY) | PAUSE (LEVERS EXHAUSTED) where levers documented, otherwise assignment under O1 | Owning campaign-type SOP |

### 5.5 Failure modes F1-F12
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Slot silently skipped | Open slot, anchor passed, found at next opening | P13 recovery; 2 consecutive misses -> PPC Lead |
| F2 | Read on degraded packet as if clean | Finding with no packet-state line, or completeness below G8 with verdict-bearing findings | Void, re-issue as flags with field-group IDs, open repair tasks |
| F3 | Slot convened inside armed window | Anchor inside G12 window/guard with trend findings | Re-slot per P1.5; void window-contaminated reads (G10) |
| F4 | Findings without owner or date | Finding line lacking owning component number & review date | Return record to slot |
| F5 | Local verdict string minted | Action text not in KDR v3.0 vocab | Rewrite to verbatim string |
| F6 | Threshold invented where v4.0 silent | Number tracing to no v4.0 section (annual tolerance, slip limit) | Strike, log AM, run read without it |
| F7 | Cadence drift between classes | Quarterly read at monthly slot or vice versa | Restore class |
| F8 | Recovery Mode as cadence holiday | Code-red product slots closed "not applicable" | Run at mode scope; post-mortem under R6/V7 |
| F9 | Stage tag renewed without evidence | Confirmed tag w/o rank/stage evidence line | Transition per T7; re-pose checks |
| F10 | Override folded straight into threshold | Threshold value tracing to override fold not versioned amendment | Revert to v4.0 value; re-enter as V3 proposal |
| F11 | Two calendars in account | Slot in this register and another instrument with different anchors | Reconcile to register, correct other |
| F12 | Annual reads never anchored | Annual register entries without marked quarterly slot | Mark anchor at P1.4 |

Escalation routing (Element 9): F2, F3, F8 -> operator queue same day; F1, F4, F5, F7, F9, F11, F12 -> next slot's worklist; F6, F10 -> PPC Lead with offending record. F1/F12 escalate with count of periods lost.

## 6. Data inputs required

**PPC Command Workbook (TEMPLATE v1.0) tabs/zones:**
- **READ ME** cadence line (month-end detection)
- **A0 Account Command**: refresh for closing month; product code-red flag; stage and expiry columns
- **T0**: zone B event posture; zone E product state vector (stage tag, declaration date, evidence); zone F TACOS decomposition (spend & share of sales by Ranking, Conversions, Defense, Discovery, Conquest, UNTAGGED, reconciling to total TACOS); economics block named cells (populated from margin table, not blended carry)
- **T1** syntax spend-governance columns (syntax spend shares, caps, cap status)
- **T2** (G12 arming carried; K9 implied via #38 elsewhere; T0-T2 pass close)
- **T4** placement performance columns (B7)
- **T6 Decision Log**: rows dated in period; drafted verdicts; human overrides with reasons; review dates; scores; 13th weekly T6 block complete for quarter; cohort predictions
- **T7 Manifest**: field-group statuses (PRESENT/PARTIAL/MISSING) at each weekly refresh in period; completeness rollup per product

**Account Rollup Workbook v1.0 tabs:**
- **A1 Family Boards** (composites for both siblings; four-period comparability)
- **A2 Cross-product M5 Queue** (funded & queued lines; envelope state; queue ordering by value)
- **A3 V5 Scoreboard** (detail and by-rule/scenario rollup; grouped by confidence band; owner calibration)
- **A4 Structure Targets** (match-type actual vs band: exact, broad, phrase, auto, PAT; format actual vs band: SP, SB, SD; match-type attributed spend)

**T7 manifest field groups named as preconditions:**
| Group | Requirement | Observable |
|---|---|---|
| D1 Per-variation margin | Refreshed for closing month by #41, G9 readable | Margin version stamp dated in closing month; T0 economics cells from it, not blended carry |
| D7 Decision log & V5 scoring | Every T6 row with review date in period scored or in debt count | Count in period, count scored, count in debt reconcile (difference zero or = reported debt) |
| A5 Threshold flags in-row | Band flags computed for period | Flag columns populated on every oversight row (Section 3 Layer M) |
| B5 Coverage counts | Registry counts per match type current | A4 actual column computes without pending flag |
| C1-C8 Syntax layer | Syntax spend shares & caps current | T1 spend-governance columns filled, cap status resolved |
| B3 Rank pack | Rank, velocity, ETA on every term with stage-relevant objective | Stage renewal evidence per term; long-tail absence counted & named |
| D6 Sibling CPC view | Family grids for every family with >1 live product | A1 composite computes for both siblings |
| B7 Placement splits | Placement decomposition for terms with recorded floor | T4 performance columns filled. **Reads MISSING in current template** -> floor re-tests at flag level (AM-3) |
| E Composite indices | Composite & efficiency indices for ranked queues | A2 queue orders by value not entry date |
Other groups named in WE-3: A2, A4, A7, B1, B8, B10, B11 (PRESENT); A1, B6, D3, D8, D12 (MISSING).

**Other registers / feeds:**
- Exact registry floor records with dates (taper & floor record, held by #12)
- Defense budget declarations by syntax with dates; organic share vs declared target per syntax; defensive register incursion history (annual)
- Margin table version stamp & G9 state (#41)
- #32 event plan / window calendar (confirmed windows, arming dates, guard periods)
- #35 open test register & class calendar
- #6 scoring-debt count; owner calibration; confidence-band calibration
- #37 rule register diff for the period
- #4 weekly/daily calendar
- Recovery Mode entry log; exit log with recovered weekly dollars
- Criteria System v4.0 file version stamp; Supersession Map entry
- Cadence register (Element 8) & annual read register
- KDR Template v3.0 sheet "Bands & Verdicts Reference"
- 12 months defense spend by syntax (annual pack)
Rule: an absent binding suppresses its dependent read and is named by field-group ID; never reconstruct a missing feed from an adjacent one.

## 7. Outputs / artifacts

| Artifact | Produced by | Storage & retention | Consumer |
|---|---|---|---|
| Cadence register (annual skeleton + slot states; per slot: class, anchor date, products, convening role, reads; re-slot records original/new anchor & window ref) | P1, closed at P7, P12 | With Command Workbook set; current + prior program year | #4, #44, #1 |
| Monthly Cadence Record (one per product per month): packet state + completeness + field groups short (opening line); 4 reads with figures; findings with owner # & review date; docket additions; deferred-read count with reason | P7 | Beside period's T6 rows; 12 months min | Quarterly slot, owning SOPs, PPC Lead |
| Quarterly Cadence Record | P12 | With quarter's monthly records; current + prior program year | Threshold owner, #26, #33, #28, #12 |
| Amendment docket, versioned per quarter (carries own age in quarters) | P3.4, P12.3 | Amendment register until landed in v4.0 release or refused with reasons | v4.0 threshold owner, CEO |
| Floor re-test cohort with prediction | P9 | Quarterly record and T6 as prediction with review date | #28, #12, #6 |
| Defense budget re-declaration pack (prior & new side by side) | P10 | Quarterly record | #26 |
| Family-level ranking | P11 | Quarterly record, cross-ref A1 and A2 | #33, queue instrument |
| Annual read register & evidence packs | P13 | With cadence register, one entry per annual class | #26, #35 |
| Deferral & miss log (miss, cause class, reads recovered vs lost) | P7, P13 | Cadence register, permanent for program year | PPC Lead, #1 |
| Data-repair tasks (owners, dates) | P2 degraded path | - | Data Operations |
| F1-F12 alarms with evidence lines | Element 9 | - | Per routing above |
Gate artifact: closed record with every finding carrying owner and date; a slot with observations and no owned items has not closed.

## 8. Decision rights

- SOP decides nothing; owning components decide inside slots (#26 defense, #33 family ownership, #28/#12 execution, #35 tests, #6 scoring).
- Authority Matrix v2.0 has **no row for cadence-review decisions** (slot placement, deferral, docket routing) -> AM-6. Matrix standing rule 5: unfilled role -> D reverts to PPC Lead, E to PPC Manager.
- Human-mandatory checkpoints (10-80-10): every **stage transition** (PPC Lead decides, weekly-verdict row); every quarterly family ranking reversing live within-product order (**PPC Lead within envelope, CEO above**, push funding row); every amendment docket to threshold owner (**CEO decides**, v4.0 threshold changes row); every escalation on F2/F6/F10; closure of any slot run on degraded packet.
- AI-executable with audit: evidence assembly, packet-state computation, share/deviation arithmetic, cohort ranking/exclusion, record drafting, miss detector, docket assembly.
- Inherited Matrix rows (Element 11): Weekly verdicts (PPC Lead decides, operator executes); Automation rules #37 (PPC Lead decides, operator executes & reviews); Structure creation (PPC Lead or per SOP scope); Sibling declarations S-series (PPC Lead decides, operator executes, BM owner reviews); Incrementality tests (operator decides & executes, PPC Lead reviews); Code-red declaration & close (PPC Lead decides, operator executes); Push funding M5 queue (CEO above envelope, PPC Lead within, operator executes); v4.0 threshold changes (CEO decides, PPC Lead executes & reviews); standing rule 1 (one D per row per scope); standing rule 4 (Transition Brief scope stack controls).
- Operator ramp: Week 1 observation; Week 2 supervised P2-P7 on one product; Week 4 unsupervised across all products (PPC Lead audits closed records).

## 9. Account-specific facts

- Weekly pass ran cleanly **13 weeks** while **structure mix 19.6 pp above band top** and **phrase layer at $0 vs 5-10% floor**.
- **WE-1 (live Wk35 figures, Account Rollup A4, sourced from PPC Tactical Improvement Catalog v1.0):** exact $3,012.00, broad $774.00, phrase $0.00; total $3,786.00. Exact 79.6% vs 60.0% top = **+19.6 pp**; band top $2,271.60 -> **$740.40** above-band exact spend/month. Broad 20.4% vs 20.0% top = +0.4 pp = **$15.14** (recorded, not routed). Phrase 0% vs 5.0% floor = **$189.30** expected phrase spend not run. Outputs: Finding 1 routes $740.40 to "BID DOWN TO PROFITABLE CPC; CAP SYNTAX"; Finding 2 routes phrase gap to #13 "ADD EXACT + RESTRUCTURE". Slot does not move the $740.40.
- **WE-2 (illustrative training base, because D1 unblended per-variation margin table is still open):** AOV $80.00; contribution $28.00/order; break-even ACOS 35.0%; Target ACOS 17.5%; Max Acceptable 26.3%; CVR 5.2%; max profitable CPC = 28 x 0.052 = $1.456 ($1.46). Floor $2.24 -> premium $0.78/click; 30 maintenance clicks/wk -> $23.40/wk; x13 = $304.20/quarter. L2 step ~10%: $2.24 x 0.90 = $2.016 -> staged $2.02; weekly spend $67.20 -> $60.60 = $6.60/wk saving. Cohort 18 terms; 2 excluded (open #35 test), 1 (Recovery Mode) -> 15 staged. Prediction: 11 of 15 hold through two-week read -> $72.60/wk, $3,775.20 annualized. Slippers restore one rung, re-record floors.
- **WE-3 (pilot product):** T7 Manifest 28 field-group rows: 10 PRESENT (A2, A4, A5, A7, B1, B5, B8, B10, B11, D7), 6 MISSING (A1, B6, B7, D3, D8, D12), 12 PARTIAL. Manifest completeness (10 + 0.5x12)/28 = 16/28 = **0.571 (57.1%)**; KDR packet weighting (decision-blocking groups only) = **0.72**; both below G8 DEGRADED. Deal window armed, 2 of 4 weeks inside + guard. Result: P6 stage renewal proceeds; P4/P5 produce flags; quarterly floor re-test prep held (B7 MISSING); 3 data-repair tasks opened. Close: 2 reads produced, 2 flagged, 1 held, 3 repair tasks.
- **WE-4:** annual defense-cost read: evidence pack (12 months defense spend by syntax, organic share vs target, incursion history) -> #26; record states no v4.0 basis; AM-2. No number.
- Manifest group **B7 placement splits reads MISSING** in current template.
- Ledger dependency **D1** (unblended per-variation margin table) open.
- Two completeness weightings disagree by ~15 points on one product (AM-7).

## 10. Open items

**Amendment items (v4.1):**
| ID | Item |
|---|---|
| AM-1 | Cadence slip tolerance: v4.0 sets none, no escalation line for missed slot |
| AM-2 | No annual layer in V4 while >=2 components declare annual reads |
| AM-3 | Floor re-test readability with B7 MISSING: fallback basis or explicit suppression rule owed |
| AM-4 | Whether FULL/WORKABLE/DEGRADED and G8 bands hold at 4-week/13-week aggregation |
| AM-5 | Carry-forward escalation basis (3 consecutive monthly slots in P4.5; 2 consecutive quarters in I-5) - if tolerances, belong in v4.0 |
| AM-6 | Authority Matrix row for cadence-review decisions missing |
| AM-7 | Manifest completeness weighting: two in use (0.571 vs 0.72), ~15 pt disagreement; open until wiring standardizes |
| AM-8 | Annual anchor placement set by this SOP's register; moves if AM-2 lands |
| AM-9 | Closed-vocabulary count: 18 (v4.0 13.1) vs 25 (KDR v3.0) vs 26 (Data Architecture & Ledger #38 row) |

**Conflicts:** C3 (#31 Budget & envelope absorbed into instruments).

**Gaps/dependencies:** D1 margin table open; B7 placement feed missing; #44 not yet published (due 2026-09-25) at time of writing.

**Interface contracts (I-1 to I-16)** - non-arrival consequences:
| ID | From -> To | Artifact/timing | Non-arrival |
|---|---|---|---|
| I-1 | #4 -> SOP-40 | Weekly calendar at skeleton build/change | Anchor to Monday cascade alone; collision check "not run"; later collision moves cadence slot |
| I-2 | Data Ops -> SOP-40 | T7 statuses per product each weekly refresh | Flag-only by default; unknown = degraded |
| I-3 | #41 -> SOP-40 | Margin stamp + G9 monthly | Provisional flag on ceiling reads; floor cohort holds |
| I-4 | #6 -> SOP-40 | A3 by-rule accuracy, owner calibration, debt count monthly; confidence-band calibration quarterly | P3.3, P3.5, P12.1 don't run; debt carried as unknown not zero |
| I-5 | SOP-40 -> #26 | Defense re-declaration pack & annual defense-cost pack | #26 re-declares on last quarter's basis; 2 quarters undeclared -> PPC Lead |
| I-6 | SOP-40 -> #28 | Floor cohort with premium ranking & exclusions | Floors age; premium $/wk of delay stated |
| I-7 | SOP-40 -> #12 | Campaign execution set, staged via #38 | Cohort holds; flagged F4 |
| I-8 | SOP-40 -> #33 | Family M5 ranking with tiebreak | Shared roots unarbitrated; no-push guard stays (safe state) |
| I-9 | #35 -> SOP-40 | Open test register & class calendar | No cohort staged this quarter |
| I-10 | #32 -> SOP-40 | Window calendar with arming & guard | Trend reads marked unverified; findings don't route |
| I-11 | #37 -> SOP-40 | Rule register diff monthly | Docket records absence; never infer rule state from bid movement |
| I-12 | SOP-40 -> #38 | Staged change set | Nothing deploys; off-set change = F10-class event in #38, voided at T+1 |
| I-13 | SOP-40 -> v4.0 owner (CEO) | Quarterly amendment docket | Items accumulate; docket carries age |
| I-14 | SOP-40 -> #1 | Register publication/increments | Register stale; recorded unregistered |
| I-15 | SOP-40 -> #44 | Element 11 ramp content | Ramp under PPC Lead until #44 publishes |
| I-16 | SOP-40 -> #36 & campaign-type SOPs | Findings with owners/dates | Carry-forward counter detects at 3 slots, escalates |

**Review triggers (Element 10):** change to V4; change to M3, M5, M6, M8, O8 or T7; publication of Authority Matrix cadence row (retires AM-6); change to #4 calendar; publication of #44; landing of D1 (WE-2 to live values); landing of B7 (floor re-test to verdict level); rebuild of any Element 12 component.

**Companion documents named (not in this pack):** Master PPC Decision Criteria System v4.0 (Sections 3, 5, 6, 9, 10, 11, 12, 13.1, 14); Keyword Decision Record Template v3.0 ("Bands & Verdicts Reference"); PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0; Account Rollup Workbook v1.0; PPC Economics Worked-Example Set v1.0; PPC Strategic Doctrine v1.0 Sections 12-13; PPC Cross-Reference Ledger; SOP-12 Exact Campaign Operations v2.0 (format exemplar); PPC Tactical Improvement Catalog v1.0.
