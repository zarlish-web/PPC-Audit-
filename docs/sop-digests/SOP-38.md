# SOP-38 Digest: Bulk-File Deployment Mechanics

Source: `PPC_SOP_38_Bulk_File_Deployment_Mechanics_v2_0.pdf` (16 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-38: Bulk-File Deployment Mechanics (PPC Department, Operating SOP, Component #38 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-07 |
| Owner role | PPC Lead (holds R on the Authority Matrix "Bulk deployments (#38)" row; no role holds D) |
| Supersedes | SOP-38 v1.0 (2026-07-24) in full |
| Thresholds | Criteria System v4.0 only; zero local thresholds; **eleven ungoverned operating numerals** logged as v4.1 amendment items (AM-1 to AM-11) |
| Growth vs v1.0 | v1.0: 1,808 words, 8 procedures, 6 failure modes, 1 worked example (vs Build Kit v1.0 12 elements at 10-18 pages and SOP-12 v2.0 exemplar floor of 6,367 words, 12 procedures, 10 failure modes, 3 worked examples). v2.0: 14 procedures, 12 failure modes, 4 worked examples; verdict mapping from 4-row session-control table to full 25-verdict vocabulary with cross-map to v4.0 Section 13.1 18-string list; Elements 11 and 12 added |

**Verdict / purpose.** Deployment is **the only step where a correct decision can still cost money**: every other component is judged on what it decided, this one on **what actually landed**. Governs the path from a staged verdict to a value live in the console, proven live by a next-day diff: staging contract, session pre-flight, bulk pull and pre-state snapshot, transcription by entity ID, the **eight pre-upload validations**, effective-CPC ceiling scan, upload and processing-report reading, delta classification and session close, **T+1 verification diff**, mismatch disposition, rollback, compressed same-day path, console single-value edit control, session record with state write-back.

**Two rules outrank everything:**
1. A session closes **only when success count = staged count**, or when every difference carries a written row, cause and disposition.
2. **No deployment is complete until the T+1 diff proves the values landed** (unverified and failed are indistinguishable from inside the workbook).

**Standing rule:** the **workbook is the source of truth; the bulk file is transport, never record**. A value's authority comes from **T2 K9** and the **T6 log**. P14 writes A2 from verified values, not from the uploaded file.

### 1.1 No decision rights
Authority Matrix v2.0 Section 1 row "Bulk deployments (#38)" is the **only operating row with no D cell**: PPC Lead R; incoming operator E; launch and CA operator E on own scope; PPC Manager E; CEO and BM owner absent. Matrix **Standing Rule 2**: an E without a D "executes staged decisions only; the #38 precedence rule applies." A transcriber who disagrees with a staged value **routes it back to its owner and never edits it**, at any tier, in any mode. Every defect this component can produce is an **accuracy defect**.

### 1.2 Three deployment paths

| Path | What travels it | Owner | Proof of landing |
|---|---|---|---|
| Manual bulk session | Every staged change set from operating SOPs: bids, budgets, states, placement multipliers, negatives, creations, target and SKU swaps | This SOP, P1-P14 | P9 T+1 diff with zero unexplained mismatches |
| Automation rule firing | Inch-up, pause-at-zero, target-ACOS ladders, rank-based taper rung one | #37 | P9 diff attributes to the rule; #37 P7 precedence resolves overlap |
| Console single-value edit | Genuine urgencies only, one value at a time, never a batch | This SOP, P13, with same-day back-fill | P9 diff + back-filled session record; unmatched = F4 |

A change that travels no path is an **incident** (F4 opens with an attribution question).

## 2. Scope and boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, gate, scenario, lever limit, verdict string. This SOP transports and proves, never decides; a threshold here is a defect (SOP-12 v2.0 Section 1.3) |
| #37 Automation rules | Owns rule register, reconciliation states, scope exclusions, rule change control. This SOP owns the manual path and supplies T+1 attribution that #37 P7 uses |
| #12, #13, #14, #15, #16, #17-19, #29 | Own what changes and why; hand a staged set meeting P1; consume P9 diff. This SOP never re-derives values or re-reads evidence |
| #28 Placement and bid modifiers | Owns ladder step derivation, exit-bid discovery, modifier sizing. This SOP runs P6 ceiling scan as arithmetic check, never a re-decision |
| Budget envelope (instrument layer) | T0 zone H and Account Rollup A2 per Ledger conflict **C3**; never cites a #31 procedure (none exists) |
| #32 Deal and event window | Inside armed window deploys only what the plan names; every row carries event reference in reason string |
| #6 V5 prediction scoring | Owns rubric; this SOP supplies execution-cause routing (miss because value did not land returns here) |
| #39 Data feed and manifest | Owns feed definitions and T7 field groups; this SOP reads T7, never redefines |
| #43 Billing continuity | INCIDENT-OPEN broadcast freezes new deployments account-wide until #43 P8 passes; this SOP holds |
| #46 Access and permissions | Owns Access Register and unrecognized-actor response; this SOP's T+1 attribution report is the real-time detector #46 P10 consumes |
| #34 Canada annex | Staging contract, validations, verification standard apply unchanged to CA; only the marketplace field and deploying role differ |

## 3. Triggers
Lags are calendar facts from Master PPC Data Architecture v1.0 Section 12 "Assembly cadence" and v4.0 gates' same-day language.

| Trigger | Detecting artifact | Max lag | Procedure | Source |
|---|---|---|---|---|
| Weekly deployment | **KDR Cycle File generated Monday PM** with Master Action Queue; T2 K9 verdict rows carrying **campaign_moves** | **Tuesday same cycle, after BM huddle** | P2-P9 full session | Data Architecture v1.0 Section 12 |
| Graduation chain | GRADUATE FROM DISCOVERY in T2 K9 with #30 graduation record | Same day | P12 | SOP-12 v2.0 Section 2 |
| Funding release | M5 queue entry flips to FUNDED with dated release in T0 zone H | Same day | P12 | SOP-12 v2.0 Section 2 |
| Inventory RED | T2 K2 band flips RED on targeted variation; D2 names ranked backup | Same day | P12 with RE-POINT VARIATION reason string | G6 |
| Eligibility flip | T3 C2 eligibility status change with reason code | Same day | P12 for halt rows (listing task not this SOP's) | G4 |
| Event window action | #32 plan names dated action inside armed window | Date plan names | P12, event reference mandatory | G10 + #32 plan |
| Code-red action | Recovery Mode entry logged with entry TACOS and projected weekly overspend | Same day at tightened tier | P12 under P2 step 6 authority re-read | Section 11 R1, R3 |
| Verification | Any closed upload session | **Next day, unconditionally** | P9, then P10 on mismatch | Component's own mechanic |
| Rollback need | P10 deployment-error classification, or V5 WRONG-DIRECTION in T6 naming execution | Same day | P11 | V1 + P10 |
| Account freeze | #43 INCIDENT-OPEN | Immediate stop | P2 step 2 refuses session | Ledger row 43 interface I-6 |
| Held-row return | Row held at P5/P6 re-enters with corrected value | Next scheduled session | P1 re-validation, normal path | No governed lag (AM-4) |

## 4. Procedures

### Preconditions (T7 MANIFEST field groups; PARTIAL/MISSING -> dependent row class does not deploy, per G8)

| ID | Field group / source | Requirement | Observable |
|---|---|---|---|
| A2 | Deployment state in-row (bid, budget, state); SP bulk sheets from Raw Pull Pack | Current console state for every affected entity; the single group this SOP both consumes and writes | T7 PRESENT with refresh timestamp later than last closed session's T+1 diff |
| A5 | Threshold flags in-row | Bands/flags computed so P6 reads flags | T7 PRESENT; **T2 K6** max profitable CPC and Expected CPC populated on every bid row |
| A6 | Objective + per-term Expected CPC; objective owners, T0 reference | Exactly one declared objective per staged entity | **T3 C1** objective tag non-blank; UNTAGGED rows return |
| A7 | Eligibility in-row; SP bulk | No affected target ineligible/suppressed | **T3 C2** eligibility clear across affected-campaign list |
| B5 | Coverage counts per match type; campaign registry | Registry current (creation legal; negative has live parent) | **T2 K8** counts refreshed in same pull as A2 |
| B8 | Row economics, break-even chain; T0 named cells | AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC | **T0 cells C18 to C24** populated; margin table version stamped |
| D1 | Per-variation margin; Finance | Margin basis known for every bid row scanned | T7 status with G9 state; PROVISIONAL carries onto ceiling rows |
| D7 | Decision log and V5 scoring; T6 | T6 reachable, append-only | T6 accepts rows; prior session's rows present and scored or dated |

**Gates at session open:**

| Gate | v4.0 | Effect |
|---|---|---|
| G1 | Validation quarantine | Quarantined row's change does not deploy; **returned, not held** (evidence void) |
| G6 | Inventory adequacy (GREEN scales, YELLOW freezes push spend, RED tapers and re-points same day) | YELLOW blocks rows raising push spend; RED admits only taper, re-point, defense rows on same-day path |
| G7 | Envelope and pacing (budgets reconcile to envelope; pacing deviation > 25% vs day-of-week curve alerts) | Budget set breaking envelope **returns whole**; never deploys the profitable half |
| G8 | Packet completeness (DEGRADED < 85% of gate-relevant fields -> flags only) | DEGRADED closes session to verdict-driven rows; gate-driven and data-repair rows still deployable (rule P8) |
| G9 | Price stability (price change in trailing 7 days -> CVR/ACOS PROVISIONAL) | PROVISIONAL rides into reason string; does not block |
| G10 | Event exclusion (event weeks + 14 days excluded from trend verdicts) | Inside armed window only plan-named rows deploy. Corpus alias = **G12** (Ledger conflict **C9**) |
| G12 | MKL hygiene (term in current MKL with syntax tag and relevancy score) | Row on untagged term returns to MKL maintenance |

Gate-name discipline: C9 records v4.0 vs corpus assign G9, G10, G12 to different subjects. v1.0 used "G2" for bulk-file freshness (matches neither v4.0's sample sufficiency nor SOP-12 v2.0's manifest freshness alias) - retired; file freshness is a P3 precondition, no G-number (AM-11).

Time estimates assume **20 to 40 staged rows on one marketplace**, trained operator; first unsupervised session roughly double.

### P1. Staging standard (contract validated at P5 step 1)
1. **One row per change** (verdict moving bid and budget = two rows). Columns in order: **marketplace | entity type | campaign ID | ad group ID | keyword or target ID | entity name (reference only, never match key) | current value | new value | change type | reason string | staging owner role | review date | confirmation tier**.
2. **Entity type (8):** campaign, ad group, keyword, product ad, product target, placement, negative keyword, negative target. **Change type (10):** bid, budget, state, placement modifier, bidding strategy, negative-add, negative-remove, target swap, SKU swap, creation.
3. **Reason string: four bracketed segments, fixed order:** `[SOP-##][verdict string, verbatim][scenario or gate reference][evidence reference]`. Example: `[SOP-12][TAPER: RANK ACHIEVED, STEP BIDS DOWN][S-R6 to T1][T6 2026-08-04 step 2 of 4]`. Missing/malformed segment -> returns to owner (v4.0 Section 12 rule **P10** "Justification completeness": no J-complete Master Action Record, no deploy, any tier, any mode; checked mechanically).
4. Verdict segment **verbatim** from the 25-string vocabulary (KDR Template v3.0 "Bands & Verdicts Reference"; mirrored in Command Workbook REFERENCE sheet **KW VERDICT** validation list). Never paraphrased, abbreviated or case-folded (T+1 attribution matches on it). Compound verdicts legal where workbook READ ME admits: both strings joined by a plus sign, each verbatim.
5. **Creations carry full settings block as one unit**, never split across sessions: campaign name per naming convention, portfolio, daily budget, bidding strategy, ad group, advertised SKU, keyword/target with match type, starting bid, placement modifiers, pre-load negative set. Without negative set -> incomplete, returns whole.
6. **Confirmation tier stamped by producing SOP** (rule **P5**): human-confirmed = every **500+ SV** keyword action, every gate failure, every structural change, every bid move **> 25%**, every budget move **> $50/day**, every **LOW-confidence** verdict; routine tail auto-applies with spot checks. Recovery Mode (rule **R3**): bid **> 15%**, budget **> $25/day**.
7. Staged set carries session identifier, row count by change type, producing components, T7 completeness score at staging. No count block -> cannot validate, no session.

### P2. Session pre-flight (10-15 min; before any download)
1. Freeze conditions, in order: (a) open #43 INCIDENT-OPEN; (b) unresolved delta from prior session on affected scope; (c) armed event window on affected product; (d) Recovery Mode entry on affected product. First three block or narrow; fourth re-tiers.
2. Unresolved delta freezes **affected scope only = campaign IDs in the open delta log** (not product, not marketplace).
3. Affected-campaign list = distinct campaign IDs across staged rows; session boundary; touching anything else = F10.
4. Read T7 for the eight field groups; record completeness score; DEGRADED (G8) -> narrow to gate-driven and data-repair rows, written down.
5. Confirm huddle on weekly path (BM owner's R exercised in daily huddle per Authority Matrix **Standing Rule 3**: review, not veto; disagreement routes up).
6. Re-read every row's tier vs P5 (or R3 where Recovery live). Human-mandatory rows grouped; confirmations collected **before upload, never during**; confirming role = the one the Matrix names for the decision class, not the session operator.
7. Open session record: session identifier, date and clock time, marketplace, operator role, staged count by change type, producing components, T7 score, freeze conditions and state, affected-campaign list.

### P3. Pull and pre-state snapshot (10-20 min)
1. Download fresh bulk sheets scoped to affected entities and a window covering every row's current value. **Never edit a previously downloaded file.**
2. Record download clock time; operator records age at upload (no governed max age; AM-2).
3. **Snapshot pre-state:** save untouched fresh download, timestamped, under session ID, **before any cell is edited**. Rollback reference for P11. Snapshot taken after first edit -> no rollback path -> **abort**.
4. Filter working views to affected-campaign list.
5. Confirm pull covers every staged row; absent entity = registry disagreement (archived, moved, never existed) -> returns to owner before transcription (cheapest catch of F9).

### P4. Transcription by entity ID with ordering discipline (1.5-3 min per value row; 8-12 min per creation block)
1. **Match by ID, never by name** (v4.0 rule **O4** makes dual objectives on one keyword legal and tagged; e.g. hot Ranking exact and cool Conversions exact on same term).
2. **Three blocks in sequence:** Block 1 creations; Block 2 value modifications (bids, budgets, placement modifiers, bidding strategy); Block 3 state changes last (a pause before a dependent edit voids the edit and the platform reports it as success).
3. Within Block 1, parent-first: campaign -> ad group -> product ad -> keyword/target -> negatives.
4. Reconcile staged current value vs fresh pull; **disagreement stops the row** and returns it to owner for re-read; **never adjusted** to the new current value.
5. New values exactly as staged; **bids carry two decimal places**; value needing rounding = staging defect, returns.
6. Leave every unnamed column untouched.

### P5. Pre-upload validation: the eight checks (15-25 min; every check's result recorded)
1. **Count check** by change type, not only total.
2. **Reason-string completeness:** four bracketed segments; mechanically per v4.0 Section 13.3 rule **J1** (field presence checked by code).
3. **Verdict-string verbatim check** vs 25-string KDR vocabulary character for character; near-misses fail.
4. **Spot check:** sample verified end to end (entity ID, current value, new value, reason string, tier). No governed sample size; record count sampled and selection basis (AM-1; v1.0's five-row sample not carried forward).
5. **Ceiling scan** per P6; above ceiling with no sizing block -> **HELD** and returned with arithmetic; never repaired.
6. **Lever-limit check:** rule **L2** max **+/-50% per change**, floor **$0.50**; outside -> returns.
7. **Scope diff** as a set comparison vs affected-campaign list.
8. **Encoding pass** on created names (round-trip through upload template, segments intact); no character-set rule (AM-9).

### P6. Ceiling scan arithmetic (2-4 min per bid row, or seconds with flags)
1. **Effective CPC ceiling = base bid x (1 + placement modifier) x (1 + dynamic raise)** (PPC Strategic Doctrine v1.0 Section 6.1; up-and-down bidding can add **up to 100% at top of search**).
2. Ceiling from **T2 K6**: max profitable CPC (v4.0 family **F1**: margin dollars x CVR) and Expected CPC (family **F9**: what the position should cost).
3. **CPC ratio bands (F1 "Product Economics"):** <= 0.8x = **SAFE**; 0.8-1.0x = **AT-CEILING**; 1.0-1.5x = **PUSH-ONLY**; > 1.5x = **UNJUSTIFIABLE** outside a sized push.
4. Disposition: SAFE and AT-CEILING proceed; PUSH-ONLY only where reason string references a sizing block (rule **M2**: target rank, required clicks vs actual, budget, weekly loss ceiling, ETA checkpoint, stop-loss); UNJUSTIFIABLE **HELD** regardless (scenario **S-R11**: CPC > 1.5x ceiling with no M2 record must ladder toward ceiling).
5. Placement-modifier rows same identity; rule **M4** sizes multiplier so effective TOS CPC <= lesser of max profitable CPC for objective and Expected CPC + tolerance; tolerance unnumbered -> test against lesser of two hard values, record untested margin (AM-8).
6. PROVISIONAL margin (T7 D1 PARTIAL or G9 clock live) -> every ceiling provisional; flag into reason string.

### P7. Upload and processing-report reading (5 min upload; 10-20 min report)
1. Human-mandatory confirmations in hand; **upload action itself human-mandatory in every session**.
2. Upload three blocks in P4 order (single file -> block order = row order).
3. Read processing report completely at **row level** (partial success is the dangerous case).
4. Classify non-success: **Rejected** (platform names cause; fix, re-upload same session); **Silently skipped** (found by success vs attempted count, never by error list); **Format errors** (fix the sheet, never the intent, never by changing a value).
5. Re-upload corrected rows same session; read second report same way; **attempt counter** increments.
6. **Never re-upload the whole file** to fix a subset.

### P8. Delta classification and session close (10-20 min). Decision tree: success vs attempted
- **A:** success = attempted -> upload half closes; proceed to P9.
- **B:** success < attempted, cause named -> fix and re-upload; if fix needs a value change, row returns to owner and becomes a delta.
- **C:** success < attempted, no cause -> set difference transcribed vs landed; each missing row = delta row (row identifier, entity ID, staged value, cause where determinable, disposition, owner); undetermined logged as undetermined.
- **D:** error cascade (multiple rejects, one cause) -> **ABORT**; fix cause; restart from P3 with fresh pull.
- **E:** stale-file discovery mid-session or scope contamination after upload -> **ABORT**, P11 rollback for anything landed, restart from P3.
1. Close only at success = staged or every difference logged as delta with cause and disposition; no third close state.
2. Unresolved delta freezes affected campaign IDs only.
3. **Held rows are not deltas** (never in attempted count); logged separately with hold reason and owner; return through next cascade.

### P9. T+1 verification diff (20-35 min; day after every deployment, unconditionally)
1. Second fresh pull on affected-campaign list.
2. Diff row by row, intended vs deployed, **every row in attempted set** (not a sample).
3. Match on entity ID and change type; read reason string from session record to attribute; match + reason string = verified.
4. Classify every mismatch per P10 before any correction.
5. Scan for unstaged changed values on affected entities; unclaimed by session or rule log = **F4**, routed to #46 as attribution question.
6. Artifact = diff report with **zero unexplained mismatches** (explained = classified, dispositioned, dated).
7. **Write A2 from verified values**; close session record.

### P10. Mismatch classification and disposition (5-15 min each). Ask in order, stop at first yes
1. **#37 rule change log shows a firing on this entity inside window?** -> external change, rule-attributed. Rule **P3**: audit value wins, automation resumes from it. Restore audited value; raise scope exclusion with #37.
2. **Another session record or console-edit log claims entity?** -> external change, human-attributed; identify role, reconcile intents, route unlogged half to F4.
3. **Landed = staged under platform transformation** (rounding to platform precision, currency/percentage format, modifier expressed differently)? -> transformed; record raw and transformed values (no tolerance; AM-5). **Platform lag** is a sub-class: re-check once on a later pull, dated (no lag tolerance; AM-3).
4. **Otherwise landed differs from staged** -> **deployment error** (this component's). Stage correction as new mini-session P1-P9 in full; week's performance reads on affected rows **void**.
5. **Landed = pre-state value, no error reported** -> silent skip found at T+1 (P8 missed it); redeploy; record P8 miss (validation failure).
- Deployment error triggers root-cause line naming which validation would have caught it (count, verbatim, spot check, ceiling scan, lever limit, scope diff, or none). "None" -> validation set short by one -> Section 10 trigger.
- Every classified mismatch writes to T6 with class, disposition, close date.
- (Text says "Four branches" but lists five.)

### P11. Rollback (30-50 min; full standard)
1. Trigger: P10 branch-4 deployment error, or V5 WRONG-DIRECTION whose root cause is **execution, not judgment** (judgment -> re-decided by owning SOP as new staged set).
2. Restore from **P3 snapshot** (not memory, not workbook prior-value column).
3. Own session with reason string `[SOP-38][ROLLBACK][session reference][defect class from P10]`; P5, P7, P8, P9 in full.
4. State rollbacks record elapsed window in T6 (paused hours absent from next read; G2 judges on actual clicks).
5. Restore budgets alongside states; record forgone spend across paused window (T0 zone H envelope reconciliation).
6. Rollback does not re-litigate the decision.

### P12. Same-day and emergency compressed path (35-60 min for 1 to 8 rows). Entry tree
- G1 quarantine or DEGRADED manifest live on affected rows -> **stop** (rule **P8** "Data-quality precedence": beats every consideration incl. urgency; fix data same day).
- Recovery Mode live -> re-tier every row to R3 (bid > 15%, budget > $25/day).
- Event window armed -> only plan-named rows, event reference in reason string.
- Otherwise proceed.
1. Full standard with smaller set: P1; P2 steps 1-3 and 6; P3; P4; P5 all eight checks; P7; P8; P9 next day.
2. Ceiling scan survives compression (same-day rows disproportionately push and event rows with stacked modifiers).
3. On 1-8 rows spot check and count check converge: every row verified end to end.
4. T+1 not compressible; skipped -> open session, scope frozen.

### P13. Console single-value edit control and back-fill (2 min edit; 10-15 min back-fill)
1. Only for genuine urgency that cannot wait for P12; **one value on one entity** (two values = bulk session).
2. Log to T6 **at the moment of the edit**: date, level, target, rule/scenario fired, prior and new value, expected outcome window, review date, acting role and tier (T6 append-only).
3. Back-fill session record same day: session ID, affected entity, staged-equivalent row with four-segment reason string, confirmation tier.
4. Edit still receives T+1 diff.
5. Unlogged console edit = **F4** regardless of size or seniority; response is attribution, not correction.

### P14. Session record, state write-back, retention (10-15 min)
1. Close record: staged count, held count with reasons and owners, attempted count, success count, delta log, upload attempt count, processing reports, T+1 diff report, mismatch classifications with dispositions, clock times of P3 pull and P7 upload.
2. **A2 from verified values only** ("single most damaging shortcut" otherwise).
3. Write T6 predictions carried from staged row: metric, direction, magnitude, horizon, review date (rule **V1**).
4. Route execution causes (MISS / WRONG-DIRECTION because value did not land -> this component).
5. Retain artifact set (no retention period; #39 Ledger row carries "retention policy lines" pending fold-in; AM-6).

### Operator card (Appendix B, 15 steps)
Freeze check in order (billing, open delta, armed window, Recovery) -> affected-campaign list -> T7 score -> tiers and confirmations before upload -> fresh pull with clock time and untouched snapshot -> match by ID, creations/values/states -> current-value disagreement stops row -> eight checks with recorded results -> ceiling breach with no sizing reference HELD -> upload human-mandatory, read report at row level -> find missing rows by subtraction -> close at success = staged or log every difference -> T+1 diff every time incl. console edits -> classify before correcting (rule, human, transformation, deployment error, silent skip) -> A2 from verified only; one T6 prediction row per deployed change.

## 5. Rules, thresholds and numbers

### 5.1 Numeric values

| Value | Meaning / source |
|---|---|
| 8 / 10 | Entity types / change types |
| 4 segments | Reason string grammar |
| 13 columns | Staged row fields (Appendix A) |
| 8 checks | P5 validations (7 pure set/string ops + 1 sampling) |
| 8 field groups | A2, A5, A6, A7, B5, B8, D1, D7 |
| 3 blocks | Creations, values, states |
| 2 decimal places | Bid precision |
| +/-50% per change; $0.50 floor | L2 bid lever limit |
| > 25% bid; > $50/day budget; 500+ SV; gate failures; structural; LOW confidence | P5 human-confirmed tier |
| > 15% bid; > $25/day budget | R3 Recovery Mode tier |
| <= 0.8x / 0.8-1.0x / 1.0-1.5x / > 1.5x | CPC ratio bands SAFE / AT-CEILING / PUSH-ONLY / UNJUSTIFIABLE (F1) |
| Effective CPC = bid x (1+modifier) x (1+dynamic raise) | Doctrine 6.1 |
| up to 100% | Up-and-down dynamic raise at TOS |
| Max profitable CPC = margin $ x CVR | F1 |
| Target CPC = AOV x Target ACOS x CVR | WE-1 arithmetic |
| < 85% | G8 DEGRADED |
| > 25% | G7 pacing deviation alert |
| 7 days | G9 PROVISIONAL window |
| 14 days | G10 post-event exclusion |
| 20-40 rows | Time-estimate basis per session |
| 1 to 8 rows | P12 compressed set size |
| Monday 06:00, 09:00 | Raw Pull Pack lands / workbooks refreshed (I-11) |
| Monday PM / Tuesday after BM huddle | KDR Cycle File / weekly session |
| T+1 | Verification the next day, unconditional |
| 18-27% CPC inflation | Doctrine 6.3: Amazon late-April 2026 dynamic bidding update vs Q1 baselines |
| 7 of 25 / 18 / 11 | KDR strings character-identical in v4.0 13.1 / divergent / v4.0 strings with no KDR counterpart |
| 18 / 25 / 26 | Vocabulary counts: v4.0 13.1 / KDR + workbook / Data Architecture rule 8 + Ledger row 8 (C10) |
| Retired v1.0 numerals | Five-row spot check; plus-one-day platform-lag re-check; 24-hour freeze escalation clock |

### 5.2 Criteria System v4.0 references

| ID | Meaning as described |
|---|---|
| G1 | Validation quarantine; row returned |
| G2 | Sample sufficiency (judges post-rollback read on actual clicks) |
| G3 | Truncation: bid read through truncated day unreadable; budget row deploys ahead of bid row |
| G4 | Eligibility; listing fix task same day |
| G6 | Inventory adequacy |
| G7 | Envelope and pacing; set returns whole |
| G8 | Packet completeness < 85% DEGRADED |
| G9 | Price stability 7 days PROVISIONAL |
| G10 | Event exclusion (corpus alias G12; C9) |
| G12 | MKL hygiene |
| L2 | +/-50% per change, $0.50 floor |
| M2 | Push sizing block (target rank, required clicks vs actual, budget, weekly loss ceiling, ETA checkpoint, stop-loss) |
| M4 | Multiplier sizing: effective TOS CPC <= lesser of max profitable CPC and Expected CPC + tolerance |
| M5 | Funding queue (FUNDED release) |
| O4 | Dual objectives on one keyword legal and tagged |
| P3 | Weekly audit outranks automation; audit value wins; automation resumes from it |
| P5 | Human-review tiers |
| P8 | Data-quality precedence: quarantine/DEGRADED beats urgency |
| P10 | Justification completeness: no J-complete MAR, no deploy |
| J1 (Section 13.3) | Field presence checked by code |
| R1, R3 | Recovery Mode entry; tightened tiers |
| V1 | Predictions; unscored actions do not accumulate |
| V5 | Rule-level prediction scoring |
| S-R11 | CPC > 1.5x ceiling with no M2 record must ladder toward ceiling |
| S-R6 | Referenced in example reason string |
| F1 (family) | Product Economics; CPC ratio bands; max profitable CPC |
| F8 (family) | GRADUATED-UNSTEERED state |
| F9 (family) | Expected CPC; "Expected CPC + tolerance" |
| Section 13.1 | 18-string closed vocabulary |

### 5.3 Verdict mapping (deployment treatment; v4.0 13.1 cross-map)

| KDR verdict | Deployment treatment | v4.0 13.1 cross-map |
|---|---|---|
| QUARANTINE: DATA REFRESH | No row deploys; set returned; data-repair row may deploy | FLAG: DATA REPAIR |
| UNLOCK TRAFFIC | Bid row; P6 and L2 checks | none |
| FIX BUDGET (TRUNCATED) | Budget row ahead of any bid row on same entity | none |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Usually no-change; budget-assurance row deploys; bid change = staging defect | EXTEND TEST |
| FUND TEST (UNFUNDED PRIMARY) | Creation block or bid+budget pair at capped test value | FUND DELIBERATE TEST (50-CLICK CAP) |
| RANK PUSH: FUND SIZED PUSH | Creation or bid+budget lift; PUSH-ONLY admitted only with M2 reference | RANK PUSH AT CONTROLLED CPC |
| RECOVERY PUSH | As above; pre-OOS baseline in evidence segment | none |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | One lever per row per cycle | none |
| FIX CONVERSION FIRST; DEFER PUSH | Bid and budget rows capping at maintenance; fix itself never a bulk row | FIX CONVERSION FIRST; DEFER PUSH |
| PLACEMENT FIX FIRST | Placement-modifier rows only; bid rows same entity = defect | none |
| RE-POINT VARIATION | SKU swap at ad level, same day P12 on G6 RED; Block 2 | RE-POINT VARIATION |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | One ladder step per session; next step date in evidence | TAPER TO FLOOR (POST-OBJECTIVE) |
| HOLD; DEFEND LIGHTLY AT RANK | No row; staged row = defect | CONTINUE; VERIFY MOMENTUM |
| DEFEND AT FLOOR | No row unless drift; one bid row restores floor | DEFEND AT FLOOR |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Bid row to T2 K6 max profitable CPC, single step, L2 tested; syntax cap via instrument layer | BID DOWN TO PROFITABLE CPC; CAP SYNTAX |
| INCREMENTALITY LADDER | Dated step-down rows, one step per session | none |
| ADD EXACT + RESTRUCTURE | Creation block + steering negatives as one unit (split = F9's most common origin) | ADD EXACT + RESTRUCTURE |
| CONSOLIDATE DUPLICATES | State row pausing loser, budget row to survivor, negative-add rows; states last | none |
| GRADUATE FROM DISCOVERY | Creation block + steering negatives at source, P12 same day; discovery CPC seeds bid (not seeded here) | GRADUATE + STEER |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | Negative-add rows in Block 1 after parents; mode in evidence segment | CUT / NEGATE |
| ENTER SBV ARBITRAGE | Only SP-exact ladder step-down row, dated to paired go-live | FORMAT SUBSTITUTION (SBV/SD) |
| OPEN / ROTATE / EXIT CONQUEST | Product-target add, bid or state rows; target IDs only | none |
| STOP-LOSS: CONCEDE OR DEFER | Bid/budget to maintenance or state to paused; freed budget via instrument layer | STOP-LOSS: CONCEDE OR DEFER |
| PAUSED-PENDING (REASON + RE-ENTRY) | State row, Block 3, last; reason and re-entry live in T2/T3 | PAUSE (LEVERS EXHAUSTED) |
| LEAVE TO HARVEST | No row | LEAVE TO HARVEST |

Session-control decisions (execution states, not verdicts): **DEPLOY, HOLD ROW, ABORT SESSION, ROLLBACK**. C10 resolves in favour of KDR's 25 (matching SOP-12 v2.0 Section 5); KDR string written, v4.0 string cross-mapped (AM-10). The seven character-identical pairs: FIX CONVERSION FIRST; DEFER PUSH, RE-POINT VARIATION, DEFEND AT FLOOR, BID DOWN TO PROFITABLE CPC; CAP SYNTAX, ADD EXACT + RESTRUCTURE, STOP-LOSS: CONCEDE OR DEFER, LEAVE TO HARVEST.

## 6. Data inputs required

| Input | Location / fields | Notes |
|---|---|---|
| Staged change sets (P1 contract) | From #12, #13, #14, #15 (incl. D5 per-group budgets), #16 (target IDs), #17-19 (with dated SP-exact step-down), #28 (ladder steps/modifiers inside rows), #29 (negatives with mode), instrument layer (envelope deltas as budget rows) | 13 fields per row + count block, session ID, producing components, T7 score |
| KDR Cycle File + Master Action Queue | Generated Monday PM | Weekly trigger |
| T2 K9 | Verdict rows with **campaign_moves** | Source of truth with T6 |
| Fresh SP bulk sheets (Raw Pull Pack) | Scoped to affected-campaign list; two pulls (P3, P9) | Download clock time recorded |
| Pre-state snapshot | Untouched timestamped download | Rollback reference |
| Processing report(s) | Row-level success/reject/skip per upload attempt | |
| A2 deployment state | T3 CAMPAIGN BOARD group C2 (bid, budget, state) | Consumed and written |
| A5 / T2 K6 | Max profitable CPC, Expected CPC on every bid row | Ceiling scan |
| A6 / T3 C1 | Objective tag (exactly one) | UNTAGGED returns |
| A7 / T3 C2 | Eligibility status and reason code | |
| B5 / T2 K8 | Registry counts per match type; live parent/twin resolution | |
| B8 / T0 cells C18-C24 | AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC; margin table version | |
| D1 | Per-variation margin from Finance with G9 state | |
| D7 / T6 DECISION LOG | Append-only; predictions; V5 scores; prior session rows | |
| D2 | Ranked backup for re-point | |
| T2 K2 | Inventory band | G6 |
| T0 zone H | M5 FUNDED releases; envelope reconciliation | |
| T7 MANIFEST | Status and completeness for eight groups | |
| KDR Template v3.0 / Command Workbook REFERENCE KW VERDICT list | 25 verdict strings | Verbatim check |
| Command Workbook READ ME | Admissible compound verdicts | |
| #37 rule change log | Firings on entity inside window | P10 branch 1 |
| Console-edit logs / other session records | | P10 branch 2 |
| #43 incident broadcast state | INCIDENT-OPEN / CLEAR | |
| #32 event plan | Dated actions, armed windows | |
| Recovery Mode entry log | Entry TACOS, projected weekly overspend | |
| #30 graduation record | With discovery CPC | |
| Delta log / held-row register from prior sessions | Campaign IDs frozen | |
| Authority Matrix confirmation stamps | Per human-mandatory row | I-14 |
| Naming convention / upload template | Encoding pass | |

## 7. Outputs / artifacts

| Artifact | Storage | Retention | Consumer |
|---|---|---|---|
| Session record (staged/held/attempted/success counts, delta log, clock times, freeze checks, T7 score, upload attempt count) | Deployment session folder keyed by session ID | Not governed (AM-6) | Next session's P2 step 2 freeze check; #6 execution-cause routing |
| Pre-state snapshot | Same folder | Not governed | P11 rollback |
| Processing report(s), one per upload attempt | Same folder | Not governed | P8; F12 escalation; #43 triage branches 2-4 |
| T+1 diff report (zero unexplained mismatches) | Same folder, dated to verification day | Not governed | Gate artifact; #12 F10, #29, #13, #14, #16 landed-value proof; #37 P7 attribution; #46 P10 detector; #43 triage |
| A2 deployment state (verified values) | Command Workbook T3 group C2, refreshed into T7 PRESENT | Live, overwritten each cycle | Next-cycle P4 step 4; every Section 3 gate |
| T6 rows, one per deployed change with prediction | T6 DECISION LOG, append-only | Log life | V5 scoring (V1); Account Rollup A3 scoreboard |
| Held-row register (hold reason, owner role) | Session record, carried forward | Until redeployed or formally declined | Producing SOP's next pass |
| Delta log (row identifier, entity ID, staged value, cause, disposition, owner) | Session record | Until every row dispositioned | Next session's P2 step 2 (freeze scoped to campaign IDs) |
| Root-cause lines on deployment errors | T6 alongside correcting row | Log life | Section 10 version governance |
| Ceiling-scan results with ratio stated; F1-F12 alarms (row, signal value, rule/gate ref); execution-cause routing packets to #6; attribution report and scope-exclusion requests to #37; unattributed-change lines to #46 | | | Downstream I-16 to I-22 |

## 8. Decision rights

| Role / row | Rights |
|---|---|
| "Bulk deployments (#38)" | **No D cell.** PPC Lead R; incoming operator E; launch and CA operator E on own scope; PPC Manager E |
| Standing Rule 2 | E without D executes staged decisions only; disagreement routes back to owner |
| Standing Rule 3 | BM owner's R exercised in daily huddle: review, not veto |
| Human-mandatory every session | Upload action itself; ABORT and ROLLBACK decisions; held-row dispositions |
| Human-mandatory per row | P5 tiers (R3 under Recovery), confirmed by role the Matrix names for the decision class, not session operator |
| "Code-red declaration + close" | PPC Lead D (P12 authority re-read routes there) |
| "Automation rules (#37)" | PPC Lead D (F11 scope-exclusion request routes there) |
| AI-executable with audit | Transcription drafting, all eight P5 validations, P6 arithmetic, processing-report parsing, delta classification, full T+1 diff, P10 classification draft |
| Skill must refuse | Compute a bid; repair a ceiling breach; complete a reason string; choose between two vocabularies; invent a spot-check size; assert a platform-lag tolerance; close at success < attempted without delta log |

**Escalation:** F4 on second occurrence with attribution; F8 and F10 on first occurrence; same failure twice in consecutive cycles on same scope -> PPC Lead with T6 history; F12 -> PPC Lead with processing report.

**Operator ramp:** Week 1 (observe two sessions; explain no-D row; locate artifacts; reproduce ceiling identity and $1.46 / $0.73; state four bands and source; 25-string vocabulary diverges on 18 of 25). Week 2 (supervised; 15+ rows; all eight checks recorded; hold a seeded ceiling breach; find silent skip by subtraction; tiering incl. R3; P10 in order; Lead confirms upload every session - permanent). Week 4 (three consecutive sessions zero unexplained mismatches; one correct abort under D or E; one rollback from snapshot with window and forgone spend; one root-caused deployment error; all held rows and deltas dispositioned).

## 9. Account-specific facts

- No live product economics spine attached; worked examples use **PPC Economics Worked-Example Set v1.0** training base: AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max Acceptable 26.3%, CVR 5.2%.
- Dated environment facts: Amazon **late-April 2026** dynamic bidding engine update, CPC inflation **18-27%** vs Q1 baselines under dynamic raises (Doctrine 6.3). **2026-08-01 billing failure** around which #43 was built (Ledger row #46).
- Worked examples (illustrative):
  - **WE-1:** 27 rows (15 bid, 5 budget, 4 negative-add, 2 creation, 1 state), 4 components, 14 campaign IDs; 8 human-mandatory (4 bids > 25%, 2 budgets > $50/day, 2 creations), 19 auto; pull 09:40, snapshot 09:44; largest bid move $1.40 -> $1.87 = 33.6%; largest budget $45.00 -> $102.00 (+$57.00/day); max profitable CPC $1.46, Target CPC $0.73; one row $1.40 x 1.45 x 1.00 = $2.03 = 1.39x (PUSH-ONLY with M2) = $0.57/click above ceiling; 27/27 success and verified; pull-to-upload age 3 h 6 min; ~2 h 18 min across two days; eleven artifacts.
  - **WE-2:** 31 rows; row 12 CVR 4.1%, bid $2.40, TOS +90% under up-and-down: 2.40 x 1.90 x 2.00 = $9.12 vs ceiling $1.15 = 7.94x -> HELD; attempted 30; row 19 negative-exact on parent archived 6 days earlier (presence passed as archived row) rejected, re-pointed via T2 K8; silent skip: 28 success vs 30 attempted with 1 rejection; after fix 29/30; delta $1.74 "keyword archived between staging and upload"; 29 + 1 held + 1 delta = 31; freeze on single campaign ID; other 13 IDs open.
  - **WE-3:** 24 rows; 20 match; 2 transformed (budget settling); 1 rule-attributed ($1.19 vs $1.31 staged, target-ACOS ladder fired overnight); 1 deployment error: $1.62 staged landed $16.20 (decimal transposition) = 11.13x ceiling; 38 clicks; spend $615.60; 1.976 orders; contribution $55.33; net loss $560.27 vs $6.23 had it landed = **$554.04** cost; scan saw $1.62 = 1.11x (PUSH-ONLY with M2); spot check missed the row.
  - **WE-4:** Tuesday 10:20 pause of 3 campaigns (consolidation); Friday 10:20 V5 WRONG-DIRECTION, execution cause (survivor never given loser's negative lists); restore from Tuesday 09:44 snapshot; budgets $34.00 + $27.00 + $18.00 = $79.00/day; 72 h window; forgone spend $237.00; reason string `[SOP-38][ROLLBACK][session 2026-08-04-US-01][P10 branch 4]`; 3/3 verified; negatives come later as #29 set.

## 10. Open items

### Amendment items (v4.1)

| ID | Missing numeral | Where it bites |
|---|---|---|
| AM-1 | Spot-check sample size and selection rule | P5 step 4; v4.0 P5 names "spot checks" with no count; WE-3 $554.04; v1.0's five rows unsourced |
| AM-2 | Maximum bulk-file age pull-to-upload | P3 step 2; age recorded not bounded |
| AM-3 | Platform-lag re-check window at T+1 | P10 branch 3; v1.0 asserted one day once; overlaps **SOP-29 AM-10** (verification lag); reconcile as one numeral |
| AM-4 | Escalation clock on unresolved delta; held-row return lag | P8 step 2, F12, Section 2; v1.0 asserted 24 h unsourced |
| AM-5 | Landed-value tolerance for platform transformation | P10 branch 3 |
| AM-6 | Retention for session records, snapshots, processing and diff reports | Element 8, P14 step 5; #39 Ledger row "retention policy lines" pending |
| AM-7 | Consecutive-step reference for runaway signature | F11; SOP-37 P5 and Element 9 cite a non-existent v4.0 reference (this cites SOP-37 v1.0; SOP-37 v2.0 has already retired it as its own AM-2) |
| AM-8 | Tolerance term in placement-multiplier ceiling | P6 step 5; M4 and F9 "Expected CPC + tolerance" unnumbered |
| AM-9 | Character-set and separator rule for reason strings and names | P5 step 8 |
| AM-10 | Which vocabulary a reason string carries; canonical string on the 18 divergent rows | P1 step 4, Section 5; C10 resolves citation, not machine attribution |
| AM-11 | Gate number for deployment-file freshness, or ruling it is not a gate | Section 3; G2 used for three subjects (v4.0, SOP-12 v2.0, SOP-38 v1.0) |

### Conflicts and gaps
- **C3:** #31 has no procedural document; envelope at T0 zone H / Account Rollup A2.
- **C9:** gate-number divergence (G9, G10, G12) between v4.0 and corpus; G10 event exclusion aliased G12.
- **C10:** vocabulary counts 18 (v4.0 13.1) / 25 (KDR, workbook) / 26 (Data Architecture rule 8, Ledger row 8); 7 common.
- P3 step 5 presence test passes on presence, not state (check-design gap surfaced in WE-2).
- Internal inconsistency: P10 header says "Four branches" but five are listed; skill block says P8 has five branches and P10 five-branch classifier.
- Cross-document: F11 cites "#37 P7" read-window suspension and "#37 P5" consecutive-step reference (SOP-37 v1.0 numbering); SOP-37 v2.0 moved precedence to P9 and retired the reference.
- Ledger pending fold-in "rollback and restore snapshot procedure" closed by P3 step 3 and P11.
- v1.0 retired numerals: five-row spot check; +1 day lag re-check; 24-hour freeze escalation.

### Failure modes
F1 stale-file editing; F2 partial success unread; F3 name-based matching on wrong twin; F4 unlogged console edit; F5 verification skipped; F6 state-change ordering voiding an edit; F7 reason string incomplete or verdict not verbatim; F8 ceiling breach repaired instead of held; F9 orphaned child row (parent archived between staging and upload); F10 scope contamination; F11 rule and manual double-touch in one window; F12 session frozen on unresolved delta past escalation point. Most carry no dated incident in the pack (stated explicitly).

### Interface contracts (22)
Upstream I-1 #12, I-2 #13, I-3 #14, I-4 #15 (missing steering negative -> GRADUATED-UNSTEERED, F8 family, a live leak), I-5 #16, I-6 #29 (escalate on second consecutive cycle), I-7 #17-19 (step-down held rather than alone), I-8 #28, I-9 instrument layer (set returns whole), I-10 #32 (no plan -> nothing deploys), I-11 Data Ops Raw Pull Pack Monday 06:00/09:00 (session defers), I-12 #39 T7 (unknown = DEGRADED), I-13 #37 rule log (ambiguity escalates same day), I-14 Matrix confirmation (rows do not deploy; narrows, not aborts), I-15 #43 broadcast (frozen until CLEAR). Downstream I-16 T+1 diff to producers, I-17 A2 to next cascade ("highest-consequence non-arrival"), I-18 #6 execution-cause packet, I-19 #37 attribution + exclusion requests, I-20 #46 unattributed-change lines, I-21 #43 diff and A2 for triage, I-22 T6 predictions.

### Named documents referenced (not present)
Master PPC Decision Criteria System v4.0; Keyword Decision Record Template v3.0; PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; Command Workbook READ ME / REFERENCE; PPC Strategic Doctrine v1.0 Sections 6.1-6.3; PPC Economics Worked-Example Set v1.0; SOP Build Kit v1.0; SOP-12 v2.0; SOP-37; PPC Cross-Reference Ledger; Supersession Map; Metric Expansion / Catalog IDs; KDR Cycle File; Master Action Queue; components #6, #13-19, #28-30, #32, #34, #39, #43, #46.
