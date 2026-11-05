# SOP-44 Digest: Operator Onboarding and Certification

Source: `PPC_SOP_44_Operator_Onboarding_and_Certification_v1_0.pdf` (18 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-44: Operator Onboarding and Certification (PPC Department, Operating SOP, Component #44 of the Operations Definition Register) |
| Version | 1.0 (first build, no predecessor; nothing carried forward) |
| Date | 2026-08-10 |
| Owner | PPC Lead, **intake by CEO** |
| Thresholds | v4.0 only; **zero local thresholds**; **zero closed-vocabulary keyword verdicts** |
| Content | 13 procedures, 11 failure modes, 3 worked examples, 24 interface contracts, certification record schema (Gap Register estimated 2 pages under superseded 10-element standard; superseded) |

**Verdict / purpose.** **Certification is an artifact, not an impression**, and is the gate between reading the system and deploying against the live account. Owns the path from zero to scope: reading order through the canon, **arithmetic gate**, **instrument gate**, **per-SOP comprehension check** assembled from that SOP's Element 11, **three-checkpoint ramp at weeks 1, 2 and 4**, **live defense**, certification record, its wiring into PPC Authority Matrix v2.0, and suspension/revocation. Also owns the **skills-conversion gate**: **no agent skill enters production on a component until at least one human is certified on that component** ("a skill reviewed by an uncertified human is an unreviewed skill"). Certification grants scope; it **never moves a human-confirmation line** and **never confers a threshold-setting right**.

**Four separable claims a record asserts (1.1):**
1. Holder can locate every number the assigned SOP consumes without being told.
2. Holder executes the SOP's procedures such that the checkpoint holder changes **no staged value on the final supervised cycle**.
3. Holder defends the reasoning behind governing rules **without reciting values**.
4. Holder **routes every item that belongs to someone else**, incl. every item in the permanent human-confirmed tier (fails most often; ends a ramp rather than delaying it).
Does not assert: may set a threshold; may deploy human-confirmed-tier items unconfirmed; scope beyond assignment. Scope set by **PPC Operations Transition Brief v1.2 stack** (Authority Matrix v2.0 Section 2 Standing Rule 4).

**Permanent line (1.2):** v4.0 Section 12 (Layer 7 P1-P10) **rule P5** places in the human-confirmed tier: **every 500+ SV keyword action, every gate failure, every structural change, every bid move above 25%, every budget move above $50/day, every LOW-confidence verdict**. Tier is a property of the action, not the operator. v4.0 Section 11 **rule R3** tightens inside Recovery Mode to **every bid move above 15% and every budget move above $25/day**.

**What v1.0 cannot certify (1.4):** Ledger row #44 says this component consumes Element 11 from **all 23 SOPs**. **Only one has delivered**: **SOP-12 Exact Campaign Operations v2.1 Section 11 "Operator Ramp"** (its 11.6 and contract **I-24** name #44 as consumer; handoff dated **2026-09-25**). At v1.0: one complete track (component #12); every other component track opens **DEFERRED (NO ELEMENT 11)**. **22 of 23** tracks deferred; skills-conversion gate reads DEFERRED for 22 components.

## 2. Scope & boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 | Decides every threshold, band, scenario, verdict, human-review tier a test examines. This SOP tests comprehension; never sets. Number not traceable to v4.0 with section heading = defect |
| #3 Authority Matrix v2.0 | Owns D/E/R/I and vacancy rule. Every competence = one matrix row turned into a demonstration. Matrix is the destination of the record; not rewritten here |
| #1 Operations Definition Register & Supersession Map | Owns component status & version numbering. P2 reading order sequenced from register wave order; SOP doesn't grade status |
| Each operating SOP, #06 and #12 through #46 | Owns own Element 11. This SOP consumes/aggregates; never authors a competence for another component |
| #11 Economics Worked-Example Set v1.0 | Owns cases E1-E8 & standard training base. P3 administers them |
| #46 Access & Permissions | Owns provisioning/deprovisioning & access register. SOP sends certification & suspension signals; never provisions/suspends directly |
| #06 V5 Prediction Scoring | Owns scoring method & four score values. SOP reads per-owner series as evidence; grades no prediction |
| #37 Automation rules & skills program | Owns rule registration & skill conversion. SOP owns only the human precondition (>=1 certified operator) |
| #40 Monthly/quarterly/annual cadence | Will carry recertification ritual once built; until then P11 states its own cadence |
| #45 Dayparting deferral | Authorizes zero hourly modifiers; no certification scope includes an hourly modifier (lever dormant) |

## 3. Triggers

No maximum lag is a v4.0 number (none exists); each is a cadence fact from a named source; governing lag = AM-2.

| Trigger | Detecting artifact | Stated lag & source | Procedure |
|---|---|---|---|
| Operator intake | Named scope assignment in Transition Brief v1.2 stack, or CEO intake decision (Gap Register owner line) | Same day as assignment recorded (Matrix Section 2 rule 4) | P1 |
| Ramp content arrives | Operating SOP publishes/amends Element 11, visible as Ledger row rewrite | Before next intake on that scope (Ledger Section 4 "The Accretion Rule": row is the handoff) | P5; P11 step 4 re-test |
| Checkpoint due | Week 1, 2, 4 dates on open certification file | Recorded on checkpoint date; late recorded with true date, never back-dated | P6, P7, P8 |
| Live defense due | All week 4 audit competences recorded (P8) | End of week 4 (SOP-12 v2.1 Section 11.5) | P9 |
| Skill conversion proposed | Skill file for component N enters conversion queue | Before conversion begins, not before deployment (Gap Register **Definition-of-Done addition 9**) | P13 |
| Authority Matrix re-issue | New Matrix version (re-issues within one week of any org change touching its roles, Section 2 rule 6) | Same week | P11 step 2 |
| v4.0 increment | New Criteria System version or landed v4.1 batch | Before next live defense on any scope citing changed rule | P11 step 3 |
| Override or accuracy signal | Per-owner override entries in **T6 Decision Log**; per-owner V5 hit rate on **Account Rollup A3 Verification scoreboard** | Monthly (rule **V2** override review); quarterly (rule **V6** confidence calibration) | P11 steps 5-6 |
| Confirmed unconfirmed deployment | P5-tier item deployed without confirmation record, found in **#38 T+1 verification report** or cycle's T6 entries | Same day | P12 first branch |
| Role vacancy | Checkpoint holder role unfilled during open ramp | Same day (Matrix Section 2 rule 5: D -> PPC Lead, E -> PPC Manager) | P1 step 5; ramp continues |

## 4. Procedures

### Preconditions & gates (Element 3)
| Gate | Source | Observable |
|---|---|---|
| Scope exists | Transition Brief v1.2 scope stack (Matrix rule 4) | Named product or decision-class scope on file header, assigning role recorded |
| Ramp content exists | Target component's Element 11, cited by Ledger row | Ledger row names an Element 11 in its **Owns exclusively** cell; else DEFERRED, P5 step 6 |
| Matrix currency | Matrix v2.0 Section 1 "The Matrix" | Matrix version on file = current published; mismatch re-runs P11 step 2 first |
| Threshold pin | v4.0 cited by section heading in every defense answer | v4.0 version string on file = version answers written against |
| Arithmetic source | Economics Worked-Example Set v1.0 E1-E8 | Eight cases available in full ("Use and Governance" makes cold reproduction the onboarding standard) |
| Instrument access | **PPC Command Workbook TEMPLATE v1.0** tabs **T0 PRODUCT COMMAND through T7 MANIFEST plus REFERENCE**, and **Account Rollup Workbook** | Candidate opens live product workbook read-only; READ ME drill path present |
| Login rights reconcile | #46 access register | Access-register row at required tier; access without track or track without access = F7 |
| Packet readable | **T7 MANIFEST** columns **"Catalog ID + Field Group", "Status", "Verdict Classes Blocked While Missing"**; gate **G8** | Status on every field group. DEGRADED doesn't block ramp; changes what week 2 can be graded on; blocked classes written on checkpoint record |
| Scoring surface live | **T6 DECISION LOG** and **Account Rollup A3 Verification scoreboard** (Data Architecture v1.0 Section 9 "Infrastructure Tabs: Logs and the Manifest (T5-T7)" and Section 11 "Account Rollup Workbook") | Per-owner rows resolve on A3; else P11 steps 5-6 record **NO EVIDENCE AVAILABLE** |
| Vocabulary source pinned | **KDR Template v3.0 sheet "Bands & Verdicts Reference"** | Verdict-string list from that sheet with count recorded on file |

### P1. Open certification file & set scope target (25 min)
1. Create record per Appendix A. Header: candidate role, assigning role, scope statement, target component numbers, matrix version, v4.0 version, Ledger version, open date.
2. Copy scope statement **verbatim** from Transition Brief v1.2 stack; brief wins over any rewording.
3. For each target component, copy its Ledger row **Owns exclusively** cell into file.
4. Checkpoint holder per component = **D role** on the rows the component executes (Matrix Section 1).
5. **Vacancy substitution** per Matrix rule 5; record substituted holder; ramp continues.
6. State **IN RAMP**, or **DEFERRED (NO ELEMENT 11)**.

### P2. Reading order pass (3-5 working days, inside week 1)
Fixed order (Gap Register): register -> doctrine -> Criteria System -> SOPs in wave order.
1. **PPC Operations Definition Register v1.1** and **PPC A-to-Z System Map v0.9**. Output: name the five layers and what each owns.
2. **PPC Strategic Doctrine v1.0**, Section 1 "Verdict and First Principles" through failure-pattern mapping. Output: restate **five governing principles**; for two known failure patterns, name the preventing doctrine clause.
3. **Criteria System v4.0** in stack order per Section 2 "The Decision Stack: Eleven Layers From Raw Metric to Deployed Action" (gates -> objectives -> diagnosis -> scenarios -> levers -> sizing). Output: list the **twelve gates** from Section 5; for three, name the action class blocked.
4. **Master PPC Data Architecture v1.0** and Command Workbook READ ME. Output: drill path from memory, **T0 through T4**, with **T5-T7 named as memory tabs**.
5. Assigned SOPs in wave order, each against its Ledger row. Output: Owns exclusively cell restated and reconciled.
6. Recorded done/not done per item; **no score**.

### P3. Arithmetic gate (90 min, closed book)
1. Administer all eight cases **E1-E8** with **inputs changed, structure held** (variation method per "Use and Governance").
2. Candidate computes, showing steps: break-even chain from contribution & AOV; max profitable CPC; target CPC; cost per order & loss line at stated CVR; push sizing chain (order gap -> required clicks -> required spend -> duration -> loss ceiling); two-products-same-ACOS margin-class comparison; CVR-adjusted cross-format comparison; liquidation allowable-cost; TACOS identity.
3. Marking per case, correct/not correct. **No aggregate percentage** (no pass mark exists; AM-1).
4. Not-correct case repeats **once in week 2** against a third variation; still not correct -> **NOT DEMONSTRATED**, travels to P9 as cold defense question.
5. Tests arithmetic, not recall of training base.

### P4. Instrument gate (2 hours, at workbook)
1. Open assigned scope's product workbook; walk **T0 PRODUCT COMMAND** zone by zone stating what each constrains below it.
2. Open **T7 MANIFEST**; list every field group **MISSING or PARTIAL** with its "Verdict Classes Blocked While Missing" entry. Read naming fewer blocked classes than manifest lists is **returned** (G8).
3. Open **T2 KEYWORD COMMAND**, apply **OVERSIGHT filter view**, expand one keyword to its campaign child rows; state which campaigns run against the term and each one's **spend share** of the keyword.
4. Open **T6 DECISION LOG**; list rows whose **Review Date** lands in current cycle; score nothing.
5. Open **Account Rollup A1 Family Boards**; name one shared head term with declared owner (or state owner undeclared).
6. Record each of five as demonstrated/not with the artifact produced.

### P5. Assemble per-SOP comprehension check (60 min per component)
1. Open target's Element 11; copy competence rows **unedited**.
2. Copy its live-defense questions and sources.
3. Add Section 5 verdict-string items the component's Element 5 mapping uses, verbatim from KDR v3.0.
4. Add Ledger row boundary items as **routing items**: for each thing the component doesn't own, candidate names the owning component number.
5. **Provenance line**: component number, document version, Element 11 section, Ledger version.
6. **No Element 11 branch:** don't write one; record DEFERRED (NO ELEMENT 11), name component & Ledger due date. Candidate may still run P2, P3, P4 (component-independent) and work the scope under ordinary Matrix supervision.

### P6. Week 1 checkpoint: observation & artifact familiarity (45 min to record)
1. **Nothing deploys under the candidate's name in week 1.**
2. Record P2 outputs, P3 results, P4 reads.
3. Record each component-specific week 1 competence with evidence artifact and reviewing role.
4. Not demonstrated -> repeats in week 2; doesn't block ramp.
5. Close when every competence carries demonstrated/not-demonstrated; **a blank closes nothing**.

### P7. Week 2 checkpoint: supervised execution (45 min at week close)
1. Candidate stages; checkpoint holder reviews **every staged row** (and reason string) before deployment path.
2. Record component-specific week 2 competences.
3. **Refusal competence**: at least one item in the week identified as needing a number v4.0 doesn't carry and routed as amendment request instead of executed. Declining nothing in two weeks = not demonstrated (not waived).
4. **Prediction competence**: every staged change carries **metric, direction, magnitude, horizon, review date** (v4.0 Section 14 rule **V1**).
5. Week 2 closes when review **changed no staged value on the final cycle** of the week and every staged row carried a **verdict and scenario ID**. Otherwise week 2 repeats as week 3.

### P8. Week 4 checkpoint: unsupervised execution under audit (60 min)
1. Week 3 repeats week 2 on full assigned scope. From week 4, candidate deploys within scope without pre-review; P5-tier & human-mandatory exceptions permanently intact.
2. Post-deployment evidence audit: holder reads cycle's T6 entries vs deployed change set and T+1 report, checking **five things**: every deployed row carries verdict & scenario ID; every deployed row carries prediction with review date; no human-confirmed-tier item deployed unconfirmed; every gate failure executed its gate lever rather than a metric verdict; last cycle's due rows scored before this cycle's verdicts read.
3. Record component-specific week 4 audit competences.
4. **Two finding classes:** staged value holder would have chosen differently = **conversation (note)**; deployed value that broke evidence chain, or human-confirmed-tier item deployed unconfirmed = **stop**, routes to P12 same day.

### P9. Live defense (60-90 min, cold, no documents)
1. Questions = assembled set (P5 step 2) + arithmetic questions for any P3 case not demonstrated.
2. Every question tests **why**. Reciting a value without reasoning fails; reasoning without knowing where to find the value is incomplete (marked as such).
3. Marked demonstrated/not against named source.
4. Question whose cited rule changed is withdrawn and rewritten from current v4.0 before session (P11 step 3).
5. Written record: every question, mark, one sentence per not-demonstrated answer stating what was missing.

### P10. Certification issuance & matrix wiring (40 min) - decision tree, first match governs
| Condition | Record state | Action |
|---|---|---|
| Target component has no published Element 11 | DEFERRED (NO ELEMENT 11) | No certification at any performance level; names component & Ledger due date; reopens at P5 step 1 when ramp lands |
| Any week 4 audit competence recorded as a stop (P8.4) | NOT DEMONSTRATED; scope returns to supervised | No certification; scope to week 2 conditions; competence re-run; P12 if unconfirmed deployment |
| All checkpoints closed, >=1 competence or defense answer not demonstrated | CERTIFIED FOR SCOPE, WITH NAMED GAPS | Issues with gaps named & routed to checkpoint holder; gap list = P11 step 1 re-test list. **Gap in routing or refusal competences not eligible** -> falls to branch above |
| All closed, all demonstrated | CERTIFIED FOR SCOPE | Issues for named scope |
Then: (1) write record per Appendix A, route to **Authority Matrix holder** for tier assignment; (2) certification signal to **#46**; (3) state to **skills-conversion queue**; (4) set next standing review date; (5) record names scope & component versions (version pin).

### P11. Standing review, re-test, recertification (30 min monthly; 90 min quarterly)
1. **Gap clearance (monthly):** work named-gap list; cleared gaps re-marked with evidence & date.
2. **Matrix remap (on re-issue, within the week):** re-read every competence's source row; D or E letter moved -> re-test before holder next executes that row.
3. **Defense re-validation (on v4.0 increment):** re-read questions; changed-rule questions rewritten; every holder certified against old answer re-takes it.
4. **Ramp re-validation (on component rebuild):** diff new Element 11 vs P5 provenance line; new/changed competences re-tested on every holder.
5. **Override review (monthly):** per-owner override entries in T6. Rule **V2**: falling override rate is the quality metric of the system; validated overrides route back into thresholds/scenarios/skills. Record holder's series direction; route validated overrides to threshold owner. **No operator pass/fail computed.**
6. **Accuracy review (quarterly):** per-owner V5 hit-rate series on A3 (hit rate by product, by rule/scenario ID, by owner). **V5** accuracy threshold governs rules not people; **V6** recalibrates confidence bands not operators. Operator-level bar = AM-1.
7. **Recertification cadence:** until #40 publishes, monthly & quarterly cadence per **V4**; hands to #40. Interval in months = AM-3.

### P12. Suspension, revocation, re-entry (same day for suspension)
1. **Suspension triggers (any one):** human-confirmed-tier item deployed without confirmation record; deployment outside certified scope; threshold written into a document, reason string or workbook cell without v4.0 basis; deployed change with no prediction and no review date, **repeated after first finding raised**.
2. On trigger: **SUSPENDED same day**; scope to week 2 supervised (P7); notify **#46**.
3. Name the **competence**, not the person.
4. **Re-entry:** re-run named competence under P7, then one full cycle under P8. **Two consecutive clean cycles** -> CERTIFIED FOR SCOPE, suspension retained in history.
5. **Revocation (REVOKED):** scope withdrawal, role exit, or **second suspension for same competence after re-entry**. Routes to #46 same day and Matrix holder (vacancy rule).
6. Revocation is a scope statement, not performance verdict; record states which of three causes.

### P13. Skills-conversion gate (20 min per component)
1. Trigger: skill file for component N enters conversion queue.
2. Read certification register for N. **>=1 operator CERTIFIED FOR SCOPE** covering N -> gate passes; record holder role & date.
3. None -> gate **fails**; conversion doesn't begin.
4. No Element 11 -> gate fails in **DEFERRED** state; blocking item is missing ramp (owner: component owner) not missing operator (owner: PPC Lead scheduling intake).
5. Record gate result against component.

## 5. Rules, thresholds & numbers

### 5.1 v4.0 references
| Rule | Meaning as described |
|---|---|
| P5 (Section 12 Layer 7 P1-P10) | Human-confirmed tier: every 500+ SV keyword action, every gate failure, every structural change, every bid move >25%, every budget move >$50/day, every LOW-confidence verdict |
| R3 (Section 11 Layer 6 T1-T8, R1-R6) | Recovery Mode tightens tier to bid moves >15% and budget moves >$25/day |
| P8 | Correct urgent action on bad data is fixing the data |
| G2 (Section 5) | Sample sufficiency; striking rate on thin sample produces no rate verdict |
| G8 (Section 5) | Missing field group blocks verdict classes; "analysis states what it could not see" |
| Section 5 | Twelve gates (G1-G12) |
| Section 2 | The Decision Stack: Eleven Layers From Raw Metric to Deployed Action |
| F15 (Section 3 Layer M F1-F16) | Confidence bands |
| M10 (Section 10 Layer 5 M1-M10) | LOW confidence: step sizes and budget steps halve, review horizon shortens (uncertainty buys smaller steps, never bigger) |
| T1 (Section 11) | Taper trigger is rank held, not rank touched |
| V1 | Prediction carries metric, direction, magnitude, horizon, review date |
| V2 | Monthly override review; falling override rate = system quality metric; validated overrides fold into thresholds/scenarios/skills |
| V3 | Amendment protocol |
| V4 | Monthly & quarterly cadence for override review and calibration |
| V5 | Rule-level accuracy threshold (governs rules, not people) |
| V6 | Confidence calibration quarterly (recalibrates bands, not operators) |
| V8 | Listed among prediction/override/accuracy machinery |
| 13.1 | Closed Verdict Vocabulary: states 18 actions, lists 18 |

### 5.2 Numbers
| Item | Value |
|---|---|
| Ramp checkpoints | Weeks 1, 2, 4 (week 3 repeats week 2) |
| Element 11 consumers | 23 SOPs; 1 delivered (SOP-12 v2.1); 22 deferred |
| SOP-12 handoff date | 2026-09-25 |
| Arithmetic cases | 8 (E1-E8); one repeat in week 2 |
| Instrument gate items | 5 |
| Week 1 competences | 9 (W1.1-W1.9); Week 2: 8 (W2.1-W2.8); Week 4: 6 (W4.1-W4.6) |
| Live-defense questions (this SOP's own ramp) | 12 (Q1-Q12) |
| Matrix rows touched | 8; SOP is I on 6 of 8 |
| Re-entry | Two consecutive clean cycles |
| Revocation | Second suspension same competence after re-entry |
| Durations | P1 25 min; P2 3-5 days; P3 90 min; P4 2 h; P5 60 min/component; P6 45; P7 45; P8 60; P9 60-90; P10 40; P11 30 monthly / 90 quarterly; P13 20 |
| Matrix re-issue | Within 1 week of org change |
| Corpus correction register | ~40 owed corrections across six documents (C4) |
| Retention | File: life of role + one full recertification cycle after revocation; issuance record: permanent; standing review: current + prior; suspension history: permanent |
| Escalation | F2, F3 first occurrence; F9 first occurrence to owning component owner + PPC Lead; others on second occurrence within two consecutive standing reviews |
| Text typo | Section 5.3 says P11 step 7 runs "on the v4.4 cadence" (context indicates V4) |

### 5.3 Thresholds consumed / missing (5.3)
| Need | Source | State |
|---|---|---|
| Actions human-confirmed at every tenure | P5 | Available |
| Recovery Mode tightened line | R3 | Available |
| Sample sufficiency | G2 | Available |
| What missing field group blocks | G8 | Available |
| Confidence bands & step-size effect | F15; M10 | Available |
| Prediction/override/accuracy machinery | V1, V2, V4, V5, V6, V8 | Available; V5/V6 govern rules & bands not operators |
| Certification pass mark | None ("established pass bar" from LTSF rollout precedent; LTSF Master Decision & Operations System outside corpus per **Ledger conflict C6**) | AM-1 |
| Max lag trigger -> procedure | None | AM-2 |
| Recertification interval | None | AM-3 |

### 5.4 Record states (outside closed vocabulary; AM-4)
| State | Asserts |
|---|---|
| IN RAMP | File open, scope named, checkpoints pending |
| DEFERRED (NO ELEMENT 11) | No ramp published; names component & Ledger due date; blocks P13 deferred |
| CERTIFIED FOR SCOPE | All demonstrated at named versions; routes to Matrix & #46 |
| CERTIFIED FOR SCOPE, WITH NAMED GAPS | Open gap list; ineligible where gap is routing or refusal |
| NOT DEMONSTRATED | Week 4 stop; supervised |
| SUSPENDED | P12 trigger; supervised same day; access notified |
| REVOKED | Scope withdrawn, role exit, or second suspension same competence |

### 5.5 Verdict strings the check uses (KDR v3.0 verbatim)
| Verdict | Check asks |
|---|---|
| RANK PUSH: FUND SIZED PUSH | Block that must exist before issue; number that ends the push |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | Why rank held not touched (T1) |
| STOP-LOSS: CONCEDE OR DEFER | Why deferral needs new funded worksheet |
| FIX CONVERSION FIRST; DEFER PUSH | Why no bid closes conversion deficit; which owner drop point routes to |
| ADD EXACT + RESTRUCTURE | Why control precedes judgement when source campaign carries most of priority term's clicks |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Why striking rate on thin sample gives no verdict (G2) |
| QUARANTINE: DATA REFRESH | Why fix the data (P8) |
| GRADUATE FROM DISCOVERY | Why walls built same session |
| LEAVE TO HARVEST | Why tracked aged pool entry is a decision, untracked is a leak |
V5 score values (T6 "V5 Score", Data Architecture v1.0 Section 9): **HIT, PARTIAL, MISS, WRONG-DIRECTION**; check asks which one requires a written root cause.

### 5.6 Failure modes
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Certification without matrix row behind it | Competence source column blank or house standard | Strike, re-derive from matrix or remove |
| F2 | Pass mark invented to close record | Any %/score/count functioning as bar | Strike same day; AM-1 |
| F3 | Week 4 read as promotion out of confirmed tier | Certified holder deploys human-confirmed item unconfirmed | P12 same day |
| F4 | Issued against unpinned version | Record lacking component, matrix or v4.0 version | Re-issue with pins before routing |
| F5 | Stale defense questions | Answer cites amended/moved rule | Withdraw, rewrite; re-test holders |
| F6 | Competence recorded blank | Closed checkpoint with unmarked row | Checkpoint doesn't close |
| F7 | Access & certification diverge | Access row with no certification, or certified with no access row | Route both to #46 same day |
| F8 | Suspension as judgement about person | Suspension naming no competence | Rewrite naming competence |
| F9 | Ramp written here for component without own | Check provenance names this document | Withdraw; DEFERRED; route to owner |
| F10 | Certification treated as permanent | No standing review since issuance while versions incremented | P11 steps 2-4 immediately |
| F11 | Register overstates coverage | Certified count >0 on unpinned or superseded-Element-11 records | Re-mark pending re-test; correct register; re-run P13 |
Alarm routing: F2, F3, F9 same day to PPC Lead (F9 also to owning component owner); F4, F7, F11 into monthly standing review; F1, F5, F6, F8, F10 onto next checkpoint worklist. Evidence line: certification file ID, competence ID, source cell or artifact, version pin.

## 6. Data inputs required

- **Cross-Reference Ledger**: rows for every target component (**Owns exclusively** and **Interfaces** cells) and #44's own row; Ledger version; Section 4 Accretion Rule.
- **Each target component's Element 11** (competence rows, live-defense questions, week structure, provenance data); Element 5 verdict mappings.
- **PPC Authority Matrix v2.0** Section 1 "The Matrix" cells (D/E/R/I) and Section 2 "Standing Rules" 1-6 (esp. 4, 5, 6); matrix version.
- **PPC Operations Transition Brief v1.2** scope stack.
- **Economics Worked-Example Set v1.0** cases E1-E8 with input variables; "Use and Governance" section.
- **PPC Command Workbook TEMPLATE v1.0**: READ ME (drill path); **T0 PRODUCT COMMAND** (zones); **T2 KEYWORD COMMAND** (OVERSIGHT filter view, campaign child rows, spend share per campaign); **T5-T7**; **T6 DECISION LOG** (Review Date, owner, overrides, "V5 Score"); **T7 MANIFEST** columns "Catalog ID + Field Group", "Status", "Verdict Classes Blocked While Missing"; **REFERENCE** tab (KW VERDICT (26) header).
- **Account Rollup Workbook**: **A1 Family Boards** (shared head terms, declared owners); **A3 Verification scoreboard** (per-owner V5 hit rate by product, rule/scenario ID, owner).
- **#38 T+1 verification report** and deployed change sets.
- **#46 access register** (candidate row & tier).
- **KDR Template v3.0** sheet "Bands & Verdicts Reference".
- **Criteria System v4.0** version string and landed amendment batch.
- **#39** field-group & manifest definitions.
- **#06** prediction-score outputs (no step-level procedures yet; marked from T6 "V5 Score" directly).
- **#1 Operations Definition Register v1.1** (component status, wave order), **PPC A-to-Z System Map v0.9**, **Gap Register v1.0**, **PPC Strategic Doctrine v1.0**, **Master PPC Data Architecture v1.0** (reading order).
- Certification register (own).
- Skills-conversion queue entries.

## 7. Outputs / artifacts

| Event | Record & storage | Retention / consumer |
|---|---|---|
| P1 intake | Certification file (one per operator per scope, Appendix A schema), stored with Authority Matrix and Transition Brief in program document set | Life of role + one full recertification cycle after revocation; checkpoint holder, later readers |
| P2-P4 | Reading-order completion list; arithmetic marking sheet per case (variant + expected value); instrument-gate artifacts (manifest read, drill note, T2 expand note, family-board note) | With file; P9 |
| P5 | Assembled comprehension check with provenance line | Until component next rebuilds; P11 step 4 |
| P6-P8 | Three checkpoint records (per-competence table with evidence artifact & reviewing role) | With file; P10, P11 step 1 |
| P9 | Defense record (questions, marks, one-sentence gap per not-demonstrated) | With file; P10, P11 step 3 |
| P10 | Certification record with three version pins & scope | Permanent; Matrix tier assignment, #46, P13 |
| P11 | Review record (gap movements, remap results, re-test results, per-owner override direction, per-owner V5 series as observations) | Current + prior review; threshold owner, amendment brief |
| P12 | Suspension/revocation record naming competence & cause | Permanent in file history; #46, vacancy-rule holders |
| P13 | Per-component gate result (passed with holder role & date / failed / deferred with blocking item) | Until component rebuild; skills-conversion queue |
| Register | **Certification register**: one row per component: certified holders, deferral state, conversion-gate result | Standing artifact; program owner |

**Appendix A schema:** Identity (candidate role, assigning role, checkpoint holder role per component, substituted holder & rule); Scope (verbatim brief statement + target components); **Version pins** (three mandatory: component version per target, Authority Matrix version, Criteria System version; Ledger version as boundary pin); Gate results (reading per item; arithmetic per case with variant & expected value; instrument per read with artifact); Competence table (ID, source matrix row, checkpoint week, mark, evidence artifact, reviewing role, date; **no aggregate row**); Defense record; Record state & full history; Routing log (three routings with dates: matrix tier, access, conversion queue); Open items (named gaps with re-test dates; blocked gates with interface ID & counterparty; vocabulary count in force).

**Appendix B reading-order card:** Register & Map -> Doctrine -> Criteria System in stack order (gates, objectives, diagnosis, scenarios, levers, sizing, transitions, precedence, justification, verification) -> Data Architecture & READ ME (T0-T4; T5-T7 memory) -> assigned SOPs in wave order vs Ledger rows. Standing habits: read the manifest before the account; score last cycle before reading this one. Standing refusal: a number the system doesn't carry is an amendment request.

## 8. Decision rights

- **Human-mandatory:** every demonstrated/not-demonstrated mark (checkpoint holder holds D on covered rows); live defense in full; P10 issuance; P12 suspension & revocation; P13 gate result.
- **AI-executable with audit:** check assembly & provenance, arithmetic-variant generation & marking, instrument-gate set comparison, register roll-up, standing-review data assembly, P11 step 4 diff, record drafting.
- Matrix row "v4.0 threshold changes": **CEO D**; operator and this SOP **I** (pass-mark gap routes, not resolves).
- Checkpoint holder = D role on rows component executes; vacancy -> PPC Lead (D) / PPC Manager (E).
- Owner PPC Lead; intake by CEO; scope from Transition Brief.

**Matrix rows touched (11.1):**
| Row | D holder | This SOP |
|---|---|---|
| v4.0 threshold changes | CEO | I |
| Weekly verdicts (established US) | PPC Lead | R |
| Structure creation (all SOPs) | PPC Lead or per SOP scope | R |
| Incrementality tests | Incoming operator (per Transition Brief) | R (audited hardest at week 4) |
| Sibling declarations (S-series) | PPC Lead | I |
| Automation rules (#37) | PPC Lead | I (P13 only) |
| Bulk deployments (#38) | No D; PPC Lead reviews | I (Standing rule 2: E without D executes staged decisions only) |
| Code-red declaration & close | PPC Lead | I |
Not conferred: "Launch-stage verdicts + batches" and "Canada weekly block" (D & E with launch & CA operator).

**This SOP's own ramp (Element 11):** W1.1-W1.9 (read ramp, permanent tier, provenance literacy, deferral count, arithmetic from marker's side with E1/E3/E8 variants, instrument-gate reference list, authority literacy, two finding classes, observe defense); W2.1-W2.8 (open track, assemble check, mark arithmetic, mark instrument by set comparison, refusal competence, P10 tree, own refusal, route on issuance); week 4 permanent exceptions (issuance/revocation/P13 stay confirmed; no pass mark at any tenure) + five-point audit; W4.1-W4.6. Limits (11.6): no aggregate pass mark; no authority over 6 of 8 rows where SOP is I; aggregation competence demonstrated at sample of one.

## 9. Account-specific facts

- Only **SOP-12 v2.1** has a published Element 11 (per this document at 2026-08-10); 22 of 23 tracks DEFERRED.
- Standard fictional base: AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max Acc 26.3%, CVR 5.2%.
- **WE-1 (#12 clean track):** max profitable CPC 28.00 x 0.052 = $1.46; target CPC 80 x 0.175 x 0.052 = $0.73; loss case CPC $2.10 CVR 5.0% -> $42.00/order, -$14.00/order; 40 clicks/wk = $84.00 spend, 2.0 orders, $56.00 contribution, $28.00/wk net loss, $1,456/yr; push sizing 2.4 orders/day gap -> 48 clicks/day; CPC $2.30 -> $110.40/day; 14 days $1,545.60; recovery $67.20/day; loss $43.20/day, $604.80 total; margin class: 32.0% ACOS on $80 AOV = $25.60 ad cost/order -> +$2.40 at $28.00 contribution, -$3.20 at $22.40; TACOS 0.35 x 0.40 = 0.14. 8/8 correct. T7: 5 MISSING + 11 PARTIAL = 16 named. T2 head term 4 campaign child rows. Week 2: 2 values changed first cycle, 0 final. 14/14 defense. CERTIFIED FOR SCOPE. Checkpoint-holder time 560 min = 9 h 20 min over 4 weeks.
- **WE-2:** 7/8 first attempt; cross-format repeat: SBV $0.95 at CVR 3.2% vs SP $2.10 at 5.0% -> 0.95 x (5.0/3.2) = $1.48 SP-equivalent, 29.3% under SP. Week 4 structural change deployed unconfirmed -> NOT DEMONSTRATED + P12 suspension (routing competence). Defense 13/14 (confidence/M10 question failed). Re-entry -> CERTIFIED FOR SCOPE, WITH NAMED GAPS; +3 weeks.
- **WE-3:** skill for non-#12 component; 0 certified, no Element 11 -> P13 fails DEFERRED; routes to component owner.

## 10. Open items

| ID | Item |
|---|---|
| AM-1 | Certification pass mark: Gap Register names "the established pass bar" from LTSF rollout precedent; LTSF Master Decision & Operations System not in corpus (**Ledger conflict C6**); v4.0 has no certification threshold |
| AM-2 | Max lag trigger -> procedure; none in v4.0 (same gap SOP-12 v2.1 recorded; likely corpus-level) |
| AM-3 | Recertification interval; none in v4.0 |
| AM-4 | Certification record states outside closed vocabulary (second instance after #46 access-state vocabulary) |
| AM-5 | Verdict-count discrepancy: v4.0 13.1 states & lists 18; KDR v3.0 lists 25; SOP-12 v2.0/v2.1 map "the full 25-verdict closed vocabulary"; Data Architecture K9 specifies 26-value; Command Workbook REFERENCE heads column "KW VERDICT (26)" over 25 entries. Ledger logs as 18/25/26 on #46 row. Section 5.2 quotes KDR list; count recorded on every file |
| AM-6 | Matrix row for this component; routed to #3 as I-24 |

**Conflicts referenced:** C3 (#31 envelope; competences cite instrument not procedure), C6 (LTSF system outside corpus).

**Contract rules (12.1):** C1 artifact is the interface; C2 non-arrival recorded not absorbed (G8); C3 suppression never substitution; C4 cite Ledger row not counterparty procedure number (~40 owed corrections across 6 documents); C5 no contract carries lag in hours/days (AM-2).

**Upstream contracts I-1 to I-14:**
| ID | Artifact | From -> to | Timing | Non-arrival |
|---|---|---|---|---|
| I-1 | Element 11 per component | Component owner -> PPC Lead | Before intake; #12 at v2.1 dated 2026-09-25 | DEFERRED; standing for 22 of 23 |
| I-2 | Authority Matrix v2.0 Sections 1-2 | #3 -> PPC Lead | Intake; within 1 week of org change | No checkpoint marked; superseded-matrix mark = F1 |
| I-3 | Transition Brief v1.2 scope | Transition owner -> PPC Lead | Intake | No file opens |
| I-4 | E1-E8 | #11 -> PPC Lead | Before P3 | Arithmetic gate suppressed; taken before P9 |
| I-5 | Command Workbook READ ME & live workbook T0-T7 | Instrument owner -> PPC Lead | Before P4 | Instrument gate suppressed (screenshot not a competence) |
| I-6 | #39 field-group/manifest definitions | #39 -> PPC Lead | Before P4 step 2 | P4 step 2 suppressed |
| I-7 | v4.0 version string & amendment batch | Threshold owner (CEO) -> PPC Lead | Before any defense | Defenses provisional |
| I-8 | KDR v3.0 Bands & Verdicts Reference | Template owner -> PPC Lead | Before P5 step 3 | Vocabulary items omitted, noted on provenance |
| I-9 | #46 access row at required tier | #46 -> PPC Lead | Before week 2 | Week 2 can't start; blocked gate against #46 |
| I-10 | Per-owner V5 series on A3 | Data Ops -> PPC Lead | Quarterly | NO EVIDENCE AVAILABLE; routes to Data Ops |
| I-11 | Per-owner override entries in T6 | Scope's PPC Lead -> holder | Monthly | Gap recorded; slow loss |
| I-12 | Current Ledger | Ledger owner -> PPC Lead | Intake; every P11.4 | P1.3, P5.4 can't run |
| I-13 | #06 score outputs | #06 -> PPC Lead | Week 4; quarterly | Standing: #06 has no step-level procedures; mark from T6 V5 Score directly |
| I-14 | Component status & wave order (#1, Gap Register) | #1 -> PPC Lead | Before P2 step 5 | P2 step 5 waits |

**Downstream I-15 to I-24:** I-15 record -> #3 tier assignment (same day); I-16 certified count & gate -> #37 / skills program; I-17 scope-grant confirmation -> scope's PPC Lead & PPC Manager; I-18 access-tier request/suspension/revocation -> #46; I-19 competence-gap findings -> component owners (aggregated monthly; three candidates failing same = ramp defect); I-20 ungoverned-number requests -> threshold owner (CEO) monthly; I-21 certification register -> #1; I-22 per-owner V5 & override series -> #06 & A3 quarterly; I-23 dates -> #40 (not built; standing condition); I-24 matrix-row request -> #3 (CEO deciding).

**Review triggers:** any Element 11 publication/amendment (highest frequency); Matrix re-issue; v4.0 increment changing a cited rule; Ledger version rewriting row 44 or a counterparty row; #40 publication; #31 procedural document or C3 resolution; resolution of verdict-count finding.

**Named documents not present:** Master PPC Decision Criteria System v4.0; PPC Authority Matrix v2.0; PPC Operations Transition Brief v1.2; PPC Economics Worked-Example Set v1.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0; Account Rollup Workbook; KDR Template v3.0; SOP-12 v2.1 (Sections 11-12); PPC Cross-Reference Ledger; PPC SOP Program Gap Register v1.0; PPC Operations Definition Register v1.1; PPC A-to-Z System Map v0.9; PPC Strategic Doctrine v1.0; LTSF Master Decision and Operations System (outside corpus).
