# SOP-06 Digest: V5 Prediction Scoring

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-06: V5 Prediction Scoring |
| Type | Operating SOP, Component #6 of the Operations Definition Register |
| Version | 2.0 |
| Date | 2026-08-10 |
| Owner | PPC Lead |
| Supersedes | SOP-06 v1.0 (2026-07-24) in full |
| Threshold policy | Thresholds and tolerances live in the Master PPC Decision Criteria System v4.0 only; this SOP carries zero local thresholds |
| Length | 22 pages; 14 procedures, 13 failure modes, 4 worked examples, 16 interface contracts, operator ramp |

**Verdict/purpose.** V5 scores the *prediction*, never the *outcome*. Grading outcomes teaches deciders to predict nothing falsifiable; grading predictions produces a rule-level accuracy number that amends the framework itself (v4.0 Section 14 rule V5). The SOP governs the whole loop: intake standard that makes a prediction scoreable, the Monday arrival sweep, realized-value assembly, confound/void determination (consumed from SOP-24 P3), the five-value outcome rubric, the four-value cause tag, filing to two instruments (T6 and A3), scoring-debt sweep, rule-level accuracy (V5), owner-level calibration, quarterly confidence calibration (V6), override fold-in (V2), human-vs-agent comparison (V8, only evidence for widening agent drafting scope), and routing failing rules into V3 amendment proposals.

Two axes kept apart: (a) did the prediction hold (score), and (b) whose fault was any gap (cause tag). Example: a push reaching rank 8 because a competitor went OOS is not a good prediction; a push that misses because the wrong bid landed is not a bad decision.

v2.0 corrects three v1.0 defects: (1) four-value rubric dropped WRONG-DIRECTION; (2) confound citation pointed at SOP-24 P1 (now loss dating) instead of SOP-24 v2.0 P3; (3) scoring rules stated as adjectives instead of numbers.

## 2. Scope & Boundaries

**Owns:** prediction intake screen (form only), scoring loop P1-P14, the score vocabulary (HIT/PARTIAL/MISS/WRONG-DIRECTION/VOID), the four cause tags (JUDGMENT/EXECUTION/WORLD/DATA), rule-level accuracy, owner calibration, confidence calibration, override fold-in, human-vs-agent comparison, amendment routing.

**Prediction definition:** a written claim about a future measured value, filed at decision time in T6 Decision Log column "Expected Outcome Window" with its "Review Date". v4.0 S14 rule V1 fixes five fields: metric, direction, magnitude, horizon, review date. v4.0 S13.2 field `expected_outcome` fixes written form: named metric, direction, magnitude, horizon.

**Explicitly does NOT own (with seam):**

| Excluded decision | Owner | Seam |
|---|---|---|
| Every threshold, band, tolerance, gate, scenario, verdict | v4.0 (#8) | A numeral here without a v4.0 section is a defect; missing numerals are AM items, never local values |
| Confound and void cause classes; diagnosis score naming a loss | SOP-24 | SOP-24 v2.0 P3 publishes five confound classes and hands each void here; this SOP consumes, never re-derives |
| Deployment accuracy, T+1 diff, disposition of a value that landed wrong | #38 | Every staged set passes through #38; EXECUTION-tagged rows route there; this SOP grades no deployment |
| The predictions themselves (what to change, what to expect) | Every campaign-type SOP | Each owning SOP writes its prediction; this SOP screens form at P1, never authors content |
| Push sizing, required-clicks worksheet, loss ceiling | SOP-23 | Scores push predictions; returns systematic magnitude error to worksheet owner; never re-sizes |
| Ladder rungs, step derivation, discovered floor, reversion rule | #28 | Scores rung prediction against recorded floor; a step size written here is a defect |
| Incrementality test design, register, call | #35 | Scores X12 capture prediction; consumes #35's void where a test rode a confounded window |
| Automation rule registration, weekly diff, retirement | #37 | Reads rule change log only to separate external change from execution cause |
| Recovery Mode entry, posture, close | SOP-26 | Scores predictions written inside the mode; never declares/runs/closes it |
| Who holds which decision, escalation paths | #3 (Authority Matrix v2.0) | Elements 9 and 11 drawn from Authority Matrix v2.0 Section 1 rows by name |
| Terminal / LTSF-tiered units | #27 | Per Ledger conflict C6 the deciding doc is outside the corpus; terminal-tier predictions score on own stated metric only |
| Envelope law, queue ranking, funding release | Instrument layer | Per Ledger conflict C3, #31 has no procedural doc; this SOP names T0 zone H and Account Rollup tab A2 |
| Operator certification and pass bar | #44 | NOT BUILT, due 2026-09-25; this SOP supplies Element 11 as input |

Other adjacent: SOP-25 (objective flip post rank-hold), #7 (10-80-10 method/skills program), #4 (operating calendar), SOP-12 v2.0 (format exemplar).

## 3. Triggers

Lag measured from the moment the artifact is readable.

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| A review date has arrived | T6 Decision Log, Review Date <= today AND V5 Score = Pending | Same Monday cascade | P2, then P3-P7 |
| A prediction is filed | T6 new row written at deployment | At staging step, before row leaves for #38 | P1 intake screen |
| A T+1 diff reports a mismatch | #38 verification diff, Wednesday | 1 working day | P6 EXECUTION branch |
| A confound is declared on a read | SOP-24 P3 handover with class, or T5 Product Log Trend-Exclusion Flag set across read window | Same scoring pass | P4, then P5 VOID branch |
| Monthly batch date | Operating calendar (#4); v4.0 S14 rule V4 (monthly = override review and stage review slot) | Within calendar month | P8, P9, P10, P12 |
| Rule-level accuracy crosses its line | Account Rollup A3 V5 Scoreboard, hit rate by rule/scenario ID at >= 10 scored predictions | Same monthly batch | P9, then P14 |
| Quarterly confidence read | v4.0 S14 rule V6 quarterly slot, read against E7 bands on A3 | Within quarter-close week | P11 |
| Recovery Mode exits | SOP-26 exit log; v4.0 S14 rule V7 (R6 review files as amendment proposals within 1 week) | 1 week from exit | P14 |
| Agent drafting-scope request opens | Skills program docket under 10-80-10 method (#7) | Before any scope change deploys | P13 |
| Prediction fails intake screen | P1 checklist result | Same working session | Return to author; F5 |

## 4. Procedures

Instruments open: product Command Workbook (T5, T6, T7), Account Rollup Workbook (A3), current #38 session record. Weekly load at 31 filed predictions per product: 55-80 min for P2-P8 combined.

### Preconditions / Gates (Section 3)

| Gate | Manifest ID | Rule | Observable proving pass |
|---|---|---|---|
| Decision log present | T7 row D7 "Decision log + V5 scoring", source feed T6, refresh Weekly | V1: unscored actions do not accumulate | D7 reads PRESENT; T6 has a row for every change deployed in window; count matched against #38 session record close count |
| G8 packet completeness | T7 PACKET COMPLETENESS SCORE cell | G8: DEGRADED (<85% gate-relevant fields) produces flags only. F15: FULL >=95%, WORKABLE 85-95%, DEGRADED <85% | Rollup >= 85%; below it scores file as flags and pass states what it could not see |
| G2 sample sufficiency | T7 A4 Statistical significance buckets (PRESENT), B9 WoW deltas | G2: bid reads >=15 clicks in 7 days; CVR verdicts >=100 clicks; CTR verdicts >=1,000 impressions; WoW swings >50% on thin samples = noise | Realized window carries required sample; short of it, not a MISS; read extends |
| G1 validation quarantine | T7 rows feeding K2 gate block; zero-flag columns | G1: impossible metrics quarantine row, flag, no recommendation, data-refresh task same day | Zero zero-flag fires on scored rows; quarantined row scores nothing |
| G10 event exclusion | T5 Trend-Exclusion Flag; T2 Event Mode | G10: event weeks + 14 days following excluded from trend verdicts | Guard end date computed explicitly and written into score row; overlap with read window -> P4 |
| G9 price stability | T7 D1 Per-variation margin (PARTIAL); T5 event type price move | G9: price change on targeted variation within trailing 7 days marks CVR and ACOS reads PROVISIONAL | No price move in trailing 7 days of review date, or score carries PROVISIONAL flag (per S13.3 rule J7) |
| G12 MKL hygiene | T7 MKL refresh state | G12: MKL stale past 30 days degrades packet manifest | MKL refresh within 30 days of review date; scored term has syntax tag and relevancy score |
| Trend comparability | T7 A1 Four-period comparability (L30/P30/B30/L60), status MISSING, blocking all trend verdicts | F7: trend classes IMPROVING, STABLE, DETERIORATING, VOLATILE (VOLATILE = variance >50% on adequate samples) | Not currently passable; trend-class predictions score on single-window read with limitation stated (AM-10) |
| Rank series resolution | T7 D9 Daily rank series overlay (PARTIAL, head terms only); B3 Rank pack (PARTIAL) | F6: IMPROVING >=2 positions/week toward target; FLAT +/-1; SLIPPING; ETA WITHIN horizon <= review horizon (default 3 weeks), BEYOND, NEVER at velocity <=0 | Term in daily series; long-tail outside D9 scores date accuracy at weekly resolution |
| Deployment truth | #38 T+1 verification diff for deploying session | No deployment complete until next-day diff proves values landed | Closed session record, zero unexplained mismatches; absent it EXECUTION cannot be excluded, P6 withholds JUDGMENT |
| Justification completeness | Master Action Record field presence, checked by code | P10: verdict without J-complete MAR does not deploy; J1: missing fields reject at deploy | Record carries expected_outcome and review_date; a T6 row without them = P1 failure caught late |

### P1. Prediction intake screen (at staging, before row leaves for #38) — 60-90 s per prediction
1. Read MAR field `expected_outcome`. Confirm four separate values: metric (named, matching a column in T2, T3 or T4), direction (up/down/hold), magnitude (number or bound, never "better"), horizon (days or weeks).
2. `review_date` is an actual calendar date = decision date + horizon, landing on a **Monday** (scoring runs in Monday cascade). Mid-week dates move forward to next Monday and horizon restated to match.
3. Conditions written: inventory band (G6), whether event window armed, confidence E7 with three drivers (S13.2 field confidence), benchmark source tier (S12 rule P6). No conditions = can never be VOID.
4. Horizon vs confidence: M10 — LOW confidence (E7 < 50) shortens horizon to 1 week and bars pushes. LOW row with 3-week horizon fails intake.
5. Write row into T6 with all **eleven columns**: Date, Level, Target, Rule / Scenario Fired, Change (prior -> new), $ Impact / wk, Expected Outcome Window, Review Date, V5 Score (=Pending), SI Conflict Note, Owner / Tier. Tier from S12 rule P5.
6. Never retro-write. Date later than deployment date = F10. T6 is append-only.

### P2. Monday arrival sweep (first in cascade) — 5-8 min per product
1. Filter T6: Review Date <= today AND V5 Score = Pending. Do NOT filter on Date.
2. Count worklist. Separately count rows whose Review Date passed in an earlier cycle with no documented G2 extension note = **scoring debt**; reports every week even at zero (F2). Debt boundary = cycle boundary (no v4.0 day count; AM-4).
3. Sort by $ Impact / wk descending.
4. Read T7 Manifest before any realized value: record completeness rollup and status of rows A1, B3, D7, D8, D9. Apply Section 3 gates. Skipping = F13.
5. Open T5 Product Log; list every event inside union of all read windows (one read serves P4).

### P3. Realized-value assembly — 2-4 min per prediction (5-7 min for rank outside daily series)
Rule: realized value from the same feed and same window definition the prediction named.
1. Route metric class: rank -> T2 block K4 with daily-series link (backed by T7 D9); CVR, CTR, CPC, ACOS, CPA, orders, clicks, spend -> T2 block K5 cross-type totals; placement-level -> T4; campaign budget/utilization -> T3; TACOS and envelope -> T0 and Account Rollup A0.
2. Realized window = same length as predicted horizon, ending on review date (3-week prediction = 21 days).
3. Apply G2: <15 clicks (bid read), <100 clicks (CVR read), <1,000 impressions (CTR read) -> stop; not a MISS; read extends, row returns with new review date one cycle out; record extension.
4. Rank in D9 (head terms): read daily series, record achievement date and velocity (positions/day). Outside D9: weekly resolution; mark "date accuracy: weekly resolution". Magnitude still scores exactly.
5. Write both predicted and realized numbers into score note (S13.3 rule J2).

### P4. Confound and void determination — 3-5 min per event-touched prediction
1. Test read window against the five SOP-24 P3 step 4 confound classes:
   - event or deal window (G10)
   - competitor deal window (S8.7 rule S-C5)
   - price test in progress (G9)
   - listing change inside 14 days (S3 family F4)
   - stockout on an adjacent variation shifting traffic mix (S8.3 rule S-I6)
2. Compute G10 guard end = last day of event window + 14 days; write date into score row.
3. Separate windows: confound on decision date corrupts diagnosis (SOP-24); inside read window corrupts score (here). Score row states which.
4. Confound inside read window -> VOID, with class name and v4.0 gate/rule reference. Else -> P5 clean.
5. Do NOT extend loss ceiling. VOID changes calibration, not spend authority. Push hitting ceiling inside suppressed interval stops at ceiling (S8.4 rule S-R5); continuation = fresh funding decision via Account Rollup A2.
6. If an incrementality test rode the window, hand void to #35 too. Confounded read handed on as clean = F8.

### P5. Five-value rubric — 1-2 min; walk in order, first match wins

| Step | Test | Outcome |
|---|---|---|
| 1 | Confound (P4) inside read window? | VOID |
| 2 | Realized moved opposite to predicted direction? | WRONG-DIRECTION (Strategic Doctrine v1.0 S13 requires written root cause) |
| 3 | A stated condition failed to hold, read clean? | MISS |
| 4 | Right direction, magnitude AND date inside tolerance? | HIT |
| 5 | Right direction, magnitude or date outside tolerance | PARTIAL (residual; most calibration signal) |

Tolerance: v4.0 uses the word 7 times (S3 F1, S3 F16 metric E2, S4 X12, S9 lever rules, S10 M3 and M4, S16) and quantifies none. Until v4.1, apply the prediction's own stated bound only ("rank 8 by day 14" = HIT only at rank <=8 on or before day 14). No bound stated -> not HIT, not PARTIAL; UNSCORABLE, return to author (F5). AM-1.

### P6. Cause tagging on every non-HIT — 2-4 min
VOID rows carry confound class instead. Every PARTIAL, MISS, WRONG-DIRECTION carries exactly one tag + one line of evidence.

| Tag | Definition / evidence | Routing |
|---|---|---|
| JUDGMENT | Decision logic or assumptions wrong with info available at decision time. Evidence: record's scenario line showing which of the five X1 story elements carried the faulty read | Calibrates decider; counts in P10 and P9 |
| EXECUTION | Right decision, landed wrong. Evidence: #38 T+1 diff delta, or unlogged console edit surfaced by diff | Routes to #38; excluded from P10 entirely |
| WORLD | World moved in ways stated conditions could not name. Evidence: T5 entry of event type competitor entry, or documented platform change | Calibrates condition writing; feeds P1 checklist, not owner hit rate |
| DATA | Inputs wrong/stale. Evidence: T7 row STALE or MISSING for the field group, G1 zero-flag fire, or G9 PROVISIONAL mark | Feed owner and gate discipline; excluded from P10; accumulates as manifest finding |

Order: (1) EXECUTION first — compare #38 T+1 diff intended vs landed; delta = EXECUTION. (2) No T+1 diff -> do NOT tag JUDGMENT; file with tag withheld; P10 excludes (I-2). (3) DATA vs T7, then WORLD vs T5; JUDGMENT = residual only after other three excluded with evidence. (4) One evidence line per tag or it does not file (F4).

### P7. Filing to both instruments — 30-45 s
1. Write outcome to T6 column "V5 Score" with exact literal strings: `HIT`, `PARTIAL`, `MISS`, `WRONG-DIRECTION`, `VOID`. A3 counts via COUNTIFS on literal strings; variants count as zero.
2. Cause tag, evidence line, predicted and realized numbers into T6 Notes (or adjacent cell).
3. Paste row into Account Rollup A3 DETAIL block: Product, Date, Target, Change (prior -> new), $ Impact /wk, Review Date, V5 Score. Summary block computes Predictions Logged, Scored, Pending, per-value counts, Hit Rate. Monday flow (A3 READ ME): Data Ops pastes T6 rows into A3 detail; PPC Lead scores arrived reviews on A3.
4. Confirm both agree (else F7).
5. VOID: no column in either; file literal `VOID` in T6 V5 Score and A3 detail; counted by none of the four summary formulas (excluded from Hit Rate); record VOID count in pass note.

### P8. Scoring-debt sweep and monthly batch — 10-15 min per product per month
1. Filter T6: V5 Score = Pending AND Review Date in past. Split: extended rows (with P3 step 3 G2 extension note + new review date) vs debt rows (nothing). Only second list is debt.
2. Score debt list in $ Impact / wk order through P3-P7.
3. Report debt count and debt dollars (sum of $ Impact / wk) as one line, even at zero.
4. If superseded by a later change on the same target, score against the value at the original review date.
5. v4.0 sets no debt threshold (AM-4); PPC Lead decides.

### P9. Rule-level accuracy and V5 rule review — 20-30 min per monthly batch
1. On A3, group scored predictions by Rule / Scenario Fired. E8 (F16) = prediction accuracy per rule ID and per owner; A3 carries hit rate by product, rule/scenario ID, owner on 13-week trend.
2. Accuracy = HIT / scored count; exclude VOID from denominator; record excluded count beside ratio.
3. V5: rule < 50% accuracy over >= 10 scored predictions enters review. Both must hold (20% on 4 does not enter; it accumulates).
4. Read cause-tag distribution of non-HITs: mostly EXECUTION -> failing deployment path, route to #38; mostly JUDGMENT on one shared assumption -> rule defect, route to P14.
5. Review produces exactly one of: amendment, threshold change, or documented defense. None = stays in review.
6. Record account-wide hit rate alongside per-rule numbers.

### P10. Owner-level calibration — 8-12 min per owner per month
1. Filter by Owner / Tier. Exclude EXECUTION, DATA, VOID. Remaining: HIT/PARTIAL/MISS/WRONG-DIRECTION with JUDGMENT or WORLD.
2. Four numbers per owner: hit rate, PARTIAL rate, direction of PARTIAL magnitudes (overshot vs undershot counts), WRONG-DIRECTION count.
3. PARTIAL direction = primary signal; systematic optimism = assumption defect (correction to assumption set, e.g. SOP-23 worksheet reference), not person.
4. VOID rate per owner on all rows including VOIDs; no ceiling (AM-5); every VOID must carry documented confound class.
5. No owner-level minimum count in v4.0 (AM-6); state denominator in same line as hit rate.

### P11. Confidence calibration, quarterly — 30-40 min
1. Group trailing-quarter scored predictions by E7 band at decision time: HIGH >= 75, MEDIUM 50-74, LOW < 50 (F15).
2. Hit rate per band; expected HIGH > MEDIUM > LOW.
3. V6: LOW outperforming its band or HIGH underperforming -> E7 weights recalibrate. E7 = composite of sample size, benchmark source tier, manifest completeness, attribution cleanliness; name which driver carried the error.
4. Route proposal via P14 (CEO decides, PPC Lead executes and reviews).
5. Second-order check: M10 — LOW halves lever step sizes and budget steps, shortens horizons to 1 week, bars pushes. State how many trailing-quarter rows would have crossed the LOW line.

### P12. Override fold-in, monthly — 15-20 min (closes Ledger "Pending fold-in: V2 override-feedback loop")
1. Pull every row where a human overrode an AI-drafted verdict in trailing month, with logged reason (Data Architecture v1.0 S10 KDR column carrying human confirmation stamp per P5 tier).
2. Score overrides against their own expected outcome.
3. Override rate and direction of travel. V2: falling override rate = system quality metric. Rising rate + high override hit rate = drafting layer behind humans; rising rate + low override hit rate = humans second-guessing correct drafts.
4. Fold validated overrides (override scored HIT while replaced draft would have scored otherwise on same read) into thresholds/scenarios/skills via P14.

### P13. Human-vs-agent comparison and agent scope — 20-30 min per scope request
1. Matched decision classes only. P5 puts into human queue: every >= 500 search-volume action, every gate failure, every structural change, every bid move > 25%, every budget move > $50/day, every LOW-confidence verdict.
2. Hit rate, PARTIAL rate, WRONG-DIRECTION count for both, same rule IDs, same window, VOIDs excluded from both denominators.
3. Report to PPC Lead with denominators. Authority Matrix row Automation rules (#37): PPC Lead decides, incoming operator executes and reviews; platform-rule scope changes route via #37 register.
4. No promotion threshold exists (AM-8); decision is a named human's on the record.

### P14. Amendment routing — 15-25 min per amendment
1. V3 form: which rule replaced, why, evidence. Oral re-derivations and parallel side-rules are process violations.
2. Attach rule ID, scored count, hit rate, cause tag distribution, specific rows.
3. Route: CEO decides, PPC Lead executes and reviews, all others informed.
4. Recovery Mode exit source: file within 1 week of exit (V7, R6 review).
5. Track to landed v4.1 section or documented rejection.

## 5. Rules, Thresholds & Numbers

### Numeric values

| Item | Value | Source |
|---|---|---|
| G8 packet completeness | FULL >= 95%; WORKABLE 85-95%; DEGRADED < 85% (flags only) | v4.0 S5 G8, S3 F15 |
| G2 bid read | >= 15 clicks in 7 days | G2 |
| G2 CVR verdict | >= 100 clicks | G2 |
| G2 CTR verdict | >= 1,000 impressions | G2 |
| G2 WoW noise | swings > 50% on thin samples | G2 |
| G10 guard | event weeks + 14 days following | G10 |
| G9 price window | trailing 7 days -> PROVISIONAL | G9, J7 |
| G12 MKL staleness | > 30 days | G12 |
| F4 listing-change confound | inside 14 days | F4 |
| F7 VOLATILE | variance > 50% on adequate samples | F7 |
| F6 velocity | IMPROVING >= 2 positions/week; FLAT +/-1; ETA default horizon 3 weeks; NEVER at velocity <= 0 | F6 |
| F6 TOS | TOS % >= 30 on ranking campaigns | F6 |
| E7 confidence bands | HIGH >= 75; MEDIUM 50-74; LOW < 50 | F15 |
| M10 LOW confidence | horizon 1 week; bars pushes; halves lever step sizes and budget steps | M10 |
| V5 rule review | < 50% accuracy AND >= 10 scored predictions | V5 |
| P5 human queue | >= 500 SV actions; bid move > 25%; budget move > $50/day; gate failures; structural changes; LOW confidence | S12 P5 |
| R3 Recovery Mode tightened lines | bid moves > 15%; budget moves > $25/day | S11 R3 |
| M3 taper | bid down 10% per week from rank achieved | M3 |
| L2 unlock | bids raised in 15-25% steps below 15 clicks | L2 |
| G3 budget | in-budget < 70% marks every rate TRUNCATED | G3 |
| F1 CPC ratio bands | <= 0.8 SAFE; 0.8-1.0 AT-CEILING; 1.0-1.5 PUSH-ONLY; > 1.5 UNJUSTIFIABLE outside sized push. Max profitable CPC = margin $ x CVR | F1 |
| X12 ladder | one step down; capture holds within tolerance for 2 weeks -> continue, floor recorded | X12 |
| X10 structure failure | auto or broad carrying > 40% of a priority term's clicks | X10 |
| T6 graduation | >= 3 orders with full unit deployed | S11 T6 |
| T1 at-target clock | 2 weeks at target -> post-objective -> taper | S11 T1 |
| L8 SBV arbitrage | SP exact CPC >= 1.5x ceiling AND SBV CPC <= 0.6x SP CPC | L8 |
| Conquest Max-ACOS band | 10-15% | F1 |
| D10 recovery | RECOVERY at best rank <= 10 in trailing 12 months; PROVEN at <= 5 | S7 D10 |
| M2 required clicks | DSTR / expected CVR; E4 elasticity correction engages at >= 8 weeks push history | M2 |
| Test cap | 50-click cap (FUND DELIBERATE TEST) | S13.1 |
| A3 trend window | 13 weeks | A3 |
| Weekly load | 55-80 min for P2-P8 at 31 predictions/product | SOP |
| T7 refresh timing | Monday 06:00 refresh, packet ready 09:00 | I-4 |
| Retention | Debt line, override read: rolling 12 months; confidence calibration: rolling 8 quarters; A3: 13-week trend with detail retained | Section 8 |
| Escalation | F2: debt rising 2 consecutive monthly batches; F8, F10: first occurrence; others: second occurrence within a quarter | Section 7 |

### v4.0 rule IDs referenced

| ID | Meaning as described |
|---|---|
| V1 | Prediction must carry metric, direction, magnitude, horizon, review date; unscored actions do not accumulate; scoring last cycle is next cycle's first step |
| V2 | Override feedback loop; falling override rate = quality metric; fold validated overrides back |
| V3 | Amendment only by versioned proposal (rule replaced, why, evidence); oral re-derivations and side-rules are violations |
| V4 | Weekly full audit; monthly override and stage review slot |
| V5 | Rule < 50% over >= 10 scored predictions enters review; outputs amendment, threshold change, or documented defense |
| V6 | Quarterly confidence calibration; recalibrate E7 weights if LOW outperforms or HIGH underperforms |
| V7 | Every Recovery Mode exit files R6 review as amendment proposals within 1 week |
| V8 | Scored log, override reasons, worked records = training corpus for AI skill files |
| G1 | Impossible metrics quarantine row, no recommendation, refresh task same day |
| G2 | Sample sufficiency (15/100/1,000) |
| G3 | In-budget < 70% -> TRUNCATED |
| G6 | Inventory bands |
| G8 | Packet completeness DEGRADED < 85% |
| G9 | Price change trailing 7 days -> PROVISIONAL |
| G10 | Event exclusion + 14 days |
| G12 | MKL stale > 30 days |
| F1 | Max profitable CPC and CPC ratio bands; objective Max-ACOS bands |
| F4 | Listing change (inside 14 days) |
| F6 | Rank velocity classes, ETA, TOS >= 30% |
| F7 | Trend classes |
| F8 | Structure states |
| F15 | Completeness bands, E7 confidence composite, E8 |
| F16 | E8 prediction accuracy per rule ID and owner; metric E2 |
| X1 | Five story elements of a scenario |
| X4 | Rank triad |
| X10 | Structure failure > 40% auto/broad |
| X12 | Incrementality ladder |
| O2 | Tail objective |
| O5 | Paused-pending formal objective with blocking reason and re-entry criterion |
| D10 | Recovery / Proven rank history |
| S-C5 | Competitor deal window |
| S-I6 | Adjacent variation stockout shifting traffic |
| S-R3 | Traffic-deficit fund verdict scenario |
| S-R5 | Stop-loss at ceiling (sufficient clicks, CVR >= benchmark, rank velocity near zero) |
| S-E5 | Rank inside armed window provisional; T1 clock starts after exclusion window closes |
| L2, L5, L6, L8, L9 | Unlock bids; three negation modes; consolidate duplicates/graduation; SBV pivot; re-point variation on YELLOW to RED same day |
| M2, M3, M4, M8, M10 | Required clicks; taper/floor; effective placement CPC; defense budget ceiling; LOW confidence sizing |
| T1, T6, R3 | Transition/re-entry; graduation at 3 orders; Recovery tightened human-review lines |
| P5, P6, P10 | Review tiers/human queue; benchmark precedence; no deploy without J-complete MAR |
| J1, J2, J7 | Missing fields reject; conclusion needs both numbers; PROVISIONAL wording |
| R1-R6 | Recovery Mode rules (S11) |
| E4, E7, E8 | Rank Response Elasticity; confidence; prediction accuracy |

### Verdict -> predicted metric contract (25 KDR v3.0 strings)

| Verdict | Prediction metric | Test source |
|---|---|---|
| QUARANTINE: DATA REFRESH | Manifest/zero-flag state | G1 |
| UNLOCK TRAFFIC | Clicks/day vs pre-change | L2; G2 |
| FIX BUDGET (TRUNCATED) | In-budget % of day | G3; horizon one cycle |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Cumulative clicks vs 50-click cap, orders at cap | S13.1; never ACOS mid-test |
| FUND TEST (UNFUNDED PRIMARY) | Clicks and orders in capped test | G2; S8.9 |
| RANK PUSH: FUND SIZED PUSH | Organic rank vs target, achievement date | M2; F6 (3-week default) |
| RECOVERY PUSH | Organic rank vs pre-loss baseline | D10; F6; cause class from SOP-24 |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Clicks/day vs required clicks/day | X4; M2 |
| FIX CONVERSION FIRST; DEFER PUSH | CVR vs named benchmark | G2 (100 clicks); P6; G9 |
| PLACEMENT FIX FIRST | TOS impression share, placement CVR | F6 (TOS >=30%); M4 |
| RE-POINT VARIATION | Rank and orders on backup variation vs baseline | G6; L9 |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | Rank held <= target, CPC reached | M3 (10%/week; restore one step = min viable CPC) |
| HOLD; DEFEND LIGHTLY AT RANK | Rank held, maintenance spend/week | S8.6; M8 |
| DEFEND AT FLOOR | Rank held at discovered floor CPC | M3 (quarterly re-test) |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | CPC vs max profitable CPC, ACOS vs band | F1 |
| INCREMENTALITY LADDER | Total capture organic + paid | X12 |
| ADD EXACT + RESTRUCTURE | Share of term clicks on new exact | X10; F8 |
| CONSOLIDATE DUPLICATES | Survivor efficiency vs pre-consolidation blend | L6 |
| GRADUATE FROM DISCOVERY | New exact CPA vs discovery source CPA | L6; T6; T1 |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | WAS % or source term click share after steering | L5; KDR WAS% bands |
| ENTER SBV ARBITRAGE | CVR-adjusted cost per SP-equivalent conversion | L8 |
| OPEN / ROTATE / EXIT CONQUEST | Cost per order vs objective band | S8.7; F1 (10-15%) |
| STOP-LOSS: CONCEDE OR DEFER | Spend vs loss ceiling, rank velocity at stop | S-R5 |
| PAUSED-PENDING (REASON + RE-ENTRY) | Re-entry criterion met / not met | O5; T1 |
| LEAVE TO HARVEST | Discovery-surface orders at re-eval date | O2; S8.9; EC7 |

## 6. Data Inputs Required

**Product Command Workbook (per product)**
- **T6 Decision Log** — all eleven columns: Date, Level, Target, Rule / Scenario Fired, Change (prior -> new), $ Impact / wk, Expected Outcome Window, Review Date, V5 Score, SI Conflict Note, Owner / Tier; plus Notes/adjacent cell. Append-only.
- **T5 Product Log** — columns Date, Event Type (e.g. price move, competitor entry), Affected Scope, Trend-Exclusion Flag.
- **T7 Manifest** — rows A1 (Four-period comparability L30/P30/B30/L60), A4 (Statistical significance buckets), B3 (Rank pack), B9 (WoW deltas), D1 (Per-variation margin), D3, D7 (Decision log + V5 scoring), D8 (Competitor depth), D9 (Daily rank series overlay); PACKET COMPLETENESS SCORE cell; MKL refresh state; row states PRESENT / STALE / MISSING / PARTIAL.
- **T2** — block K4 (rank, daily-series link, best rank), block K5 (cross-type totals, CTR, CVR, CPC, ACOS), block K2 gate block (zero-flag columns), Event Mode.
- **T3** — campaign rows (budget, utilization).
- **T4** — placement-level values.
- **T0** — zones C-F (envelope, TACOS); zone H (envelope law/queue).

**Account Rollup Workbook**
- **A3 V5 Scoreboard** — summary block (Predictions Logged, Scored, Pending, HIT/PARTIAL/MISS/WRONG-DIR counts, Hit Rate; by product, rule/scenario ID, owner, 13-week trend) and DETAIL block (Product, Date, Target, Change (prior -> new), $ Impact /wk, Review Date, V5 Score); READ ME refresh flow.
- **A0** — envelope and TACOS.
- **A2** — funding queue (M5 queue) for fresh funding decisions.

**Other artifacts**
- Master Action Record (MAR) fields `expected_outcome`, `review_date`, `confidence` (E7 + three drivers), benchmark source tier.
- #38 T+1 verification diff and session record (close count, mismatches).
- #37 rule change log.
- SOP-24 P3 void handovers with class references.
- #35 incrementality test result and total-capture read.
- SOP-26 Recovery Mode exit log (with recovered weekly dollars).
- KDR cycle file (frozen snapshot V5 scores against); KDR column with human confirmation stamp (override pull).
- Keyword Decision Record Template v3.0 sheet "Bands & Verdicts Reference" (25 verdict strings, WAS% band line) and "Read Me".
- MKL (refresh date, syntax tag, relevancy score per term).
- Skills program docket (#7, 10-80-10).
- Operating calendar (#4).
- SOP-23 push worksheets (required clicks, loss ceiling).

## 7. Outputs / Artifacts

| Artifact | Location | Retention | Consumer |
|---|---|---|---|
| Filed score: outcome value, cause tag, evidence line, predicted and realized values | Product Command Workbook T6, column V5 Score + adjacent note | Life of workbook; append-only | Next P2; KDR cycle file |
| Account scoreboard rows | Account Rollup A3, summary + DETAIL | 13-week rolling trend, detail retained beyond | P9, P10, PPC Lead Monday flow, BM owner daily huddle |
| Scoring-debt line (row count + summed $ Impact / wk) | Monthly batch note with A3 refresh | Rolling 12 months | PPC Lead; F2 escalation |
| Rule-review docket (rule ID, scored count, hit rate, excluded VOID count, cause distribution, one of amendment/threshold change/defense) | Monthly batch, v4.1 amendment queue | Until rule leaves review | v4.0 threshold owner via P14 |
| Quarterly confidence calibration (hit rate by E7 band with driver) | Quarter-close batch | Rolling 8 quarters | v4.0 threshold owner |
| Override fold-in read (rate, direction, validated overrides) | Monthly batch note | Rolling 12 months | Threshold/scenario/skill owners |
| Human-vs-agent comparison with both denominators | Skills program docket (#7) | Life of agent scope grant | PPC Lead; #37 |
| EXECUTION-tagged rows with T+1 diff refs | #38 session review | Life of session record | #38 |
| Systematic PARTIAL-magnitude findings by rule | Monthly batch note, routed to owning SOP | Until assumption corrects | SOP-23, #28, SOP-24 |

**Gate artifact:** a scoring cycle closes only when T6 non-Pending count = arrived-review count minus documented G2 extensions, and A3 Scored count reconciles per product.

**Interface contracts (I-1 to I-16):** I-1 campaign SOPs -> P1 (MAR expected_outcome/review_date; non-arrival = undeployable, F5); I-2 #38 -> P6 (T+1 diff Wednesday; else JUDGMENT withheld); I-3 SOP-24 P3 -> P4 (void + class; else F8); I-4 Data Ops -> P2 (T7, Monday 06:00/09:00; else G8 flags); I-5 Brand Management via T5 -> P4 (same day; else WORLD unevidenced); I-6 #35 -> P3 (test close; else ladder predictions extend); I-7 #37 -> P6 (weekly); I-8 SOP-26 -> P14 (exit log); I-9 Data Ops -> A3 (Mondays; else F7); I-10 P7 -> T6/A3; I-11 P6 -> #38 (EXECUTION rows; WE-3 $140.80); I-12 P10 -> SOP-23/SOP-24/#28; I-13 P9/P14 -> v4.0 threshold owner; I-14 P13 -> skills program; I-15 Element 11 -> #44 (NOT BUILT, due 2026-09-25); I-16 P12 -> threshold/scenario/skill owners.

**Alarms computable without human reading:** F2, F7, F9, F13.

## 8. Decision Rights

Authority Matrix v2.0 coding (D decides, E executes, R reviews, I informed):

| Row | Coding | Applies to |
|---|---|---|
| Weekly verdicts (established US) | PPC Lead D; incoming operator E within assigned scope; PPC Manager E; BM owner R | Human confirms every JUDGMENT tag |
| Bulk deployments (#38) | PPC Lead R; incoming operator E; PPC Manager E | Every EXECUTION disposition |
| Incrementality tests | Incoming operator D and E; PPC Lead R | Voids shared with #35; P4 |
| v4.0 threshold changes | CEO D; PPC Lead E and R; all others I | Every P14 amendment and P11 recalibration; operator never holds D |
| Automation rules (#37) | PPC Lead D; incoming operator E and R; PPC Manager E | Every P13 agent-scope change |
| Code-red declaration + close | PPC Lead D; incoming operator E; PPC Manager E | Scoring Recovery Mode predictions (R3 tightened lines) |
| Launch-stage verdicts + batches and Canada weekly block | Launch/CA operator D and E; PPC Lead R; BM owner R or I | Not incoming operator's scope; observe only |

- AI-executable with audit: P2 sweep and counts, P3, P4 guard-end arithmetic, P5 on clean unambiguous reads, P8, P9/P10/P11 computations, P13 arithmetic, both P7 writes.
- Monday flow: Data Ops pastes T6 rows into A3; PPC Lead scores arrived reviews.
- Debt threshold decisions: PPC Lead (no v4.0 trigger).
- Agent scope promotion: named human on the record (PPC Lead).
- Standing rule 3: BM owner review on verdict rows is the daily huddle; disagreements route up, not sideways.
- Standing rule 5: vacant role's D reverts to PPC Lead and E to PPC Manager.
- Operator ramp: week 1 observe, week 2 supervised, week 4 unsupervised-audited; week-4 gate for weekly verdicts = two consecutive weeks with arrived reviews scored on time and every miss root-caused in writing; Lead audits sample of 5 rows re-walked through P5. Transition Brief v1.2: day-1 confirm V5 scoring backlog with PPC Lead; execute arrived-unscored reviews under supervision.

## 9. Account-Specific Facts

- Weekly load estimate assumes **31 filed predictions per product**.
- T7 live state: **A1 MISSING** (blocking all trend verdicts), **D8 MISSING** (blocking competitor-context reads), **D3 MISSING**, **D9 PARTIAL** (head terms only), **B3 PARTIAL**, **D1 PARTIAL**, A4 PRESENT.
- Account's recorded calibration instance: velocity assumptions feeding SOP-23 push worksheets — magnitude consistently reached late; correction is a worksheet reference tightening returned to SOP-23.
- Canonical edge cases (account history, exist nowhere else):

| Case | Score at v2.0 |
|---|---|
| EC1 Push rank 22 -> 8 by day 14, achieved day 13 | HIT |
| EC2 Same push achieved day 19 | PARTIAL, WORLD (documented competitor deal) or JUDGMENT (velocity assumption; SOP-23 corrects) |
| EC3 Rank never moved, full traffic delivered | MISS, JUDGMENT (validated CVR was thin; tighten validation standard for class) |
| EC4 Event window mid-push | VOID (no ceiling extension at v2.0) |
| EC5 Graduation CPA above source; diff shows wrong bid | MISS, EXECUTION |
| EC6 Taper rung predicted hold, slipped, reverted | Rung MISS; process HIT (scored separately) |
| EC7 LEAVE re-eval date passed unscored | P8 debt row (F2) |
| EC8 "Sales will improve" | P1 intake failure (origin of F5) |
| EC9 Bid reduced to close ACOS gap; ACOS rose, read clean | WRONG-DIRECTION, JUDGMENT (new at v2.0) |

- Worked examples use **fictional base** from PPC Economics Worked-Example Set v1.0 (live economics spine not attached): AOV $80.00, contribution $28.00/order, margin 35.0%, break-even ACOS 35.0%, Target ACOS 17.5%, Maximum Acceptable 26.3%, CVR 5.2% default.
  - WE-1 (case E3): rank 22 -> 8, DSTR 4.0 orders/day at rank 8, current 1.6, gap 2.4; CVR 5.0% -> 48.0 clicks/day; CPC $2.30 -> $110.40/day; 14-day planned $1,545.60; planned loss $43.20/day, $604.80 over 14 days vs ceiling $650.00. Realized: rank 8 day 13, 613.6 clicks, CPC $2.34, spend $1,435.82, 30.68 orders, $859.04 recovered, loss $576.78 (88.7% of ceiling). Velocity 1.077/day (+7.7%), 7.54 positions/week. HIT, E7 = 78.
  - WE-2: deal window day 6-9; guard end day 23; day-14 loss $604.80 (93.0%); re-dating adds 9 x $43.20 = $388.80 -> $993.60 (152.9% of ceiling, breach $343.60). Correct: VOID, ceiling stays $650, stop day 15, continuation priced $388.80 via A2 M5 queue.
  - WE-3: graduation at 4 orders; CVR 12.5% -> 8.0 clicks/order; seed $2.80 -> CPA $22.40; realized CPA $28.80 over 22 orders; landed bid $3.60 vs staged $2.80 (+28.6%, above 25% P5 line); overrun $6.40/order, $140.80 total; MISS, EXECUTION.
  - WE-4: S-R3 14 rows across 5 products in 13 weeks: 5 HIT, 3 PARTIAL, 4 MISS, 1 WRONG-DIRECTION, 1 VOID; 5/13 = 38.5% (5/14 = 35.7% incl VOID); 6 JUDGMENT rows all < 8 weeks push history (M2 E4 not engaged); defense 5/7 = 71.4% but 7 < 10 -> stays in review; AM-7.

## 10. Open Items

### Amendment register (11 items for v4.1)

| ID | Missing number/rule | Where it bites |
|---|---|---|
| AM-1 | Tolerance bands per prediction class (HIT vs PARTIAL) | P5 steps 4-5; largest open item |
| AM-2 | VOID as defined score value and treatment in E8 denominator | S5.3, P7 step 5, P9 step 2, F9, WE-4; no column in T6/A3 |
| AM-3 | Re-dating rule after confound; whether suppressed interval extends loss ceiling | P4 step 5, WE-2; mirrors SOP-24 v2.0 AM-5 |
| AM-4 | Scoring-debt threshold (days and escalation count) | P8 step 5 |
| AM-5 | VOID-rate ceiling per decider and decision class | P10 step 4, F3 |
| AM-6 | Minimum scored count for owner-level read | P10 step 5, F11 |
| AM-7 | Interim required-clicks correction for terms < 8-week push history (M2/E4) | WE-4 |
| AM-8 | Agent scope-promotion criterion (bar, sample, margin) | P13 step 4, F12 |
| AM-9 | Default review horizon per verdict class (23 of 25 strings lack one) | P1 step 2, S5.2 |
| AM-10 | Scoring rule for trend-class predictions while four-period comparability unavailable | S3, F13 |
| AM-11 | Verdict vocabulary count reconciliation 18 (v4.0 S13.1) / 25 (KDR v3.0) / 26 (Transition Brief v1.2, Ledger #8) | S5.1-5.2; open on Ledger #46 |

### Conflicts and findings
- Ledger conflicts referenced: C3 (#31 has no procedural document), C6 (terminal/LTSF tier document outside corpus); C1-C7 as declared; Ledger rows reference conflicts through C23 while Section 3 lists seven.
- Finding 1: score vocabulary defined three ways across four documents; v4.0 contains none of the five strings.
- Finding 2: Ledger row for #6 cites SOP-24 P1 for confound classes; should be P3 (Must-not-restate cell needs edit).
- Finding 3: attached Tier 2 copy of SOP-38 is v1.0; Ledger names v2.0 superseding.
- Finding 4: pack state asserted three ways (Ledger v2.5 Wave 4 closed vs Ledger header v3.3 dated 2026-08-04 vs rows with Wave 5A/5B returns for #20, #24, #28, #32, #33, #35, #37, #42; SOP-24 v2.0 records Ledger v2.8).
- Finding 5: v4.0 has no prediction-scoring section (structural reason for 9 of 11 AM items).

### Named but not present / not built
- #44 Operator onboarding and certification: NOT BUILT, due 2026-09-25.
- #31 envelope law: no procedural document.
- #27 terminal/LTSF tier deciding document outside corpus.
- Live product economics spine not attached (worked examples use fictional base).
- Footer inconsistency: last page footer reads "Page 14 of 14" while document is 22 pages.
