# SOP-20 Digest: AMC Operations

Source: `PPC_SOP_20_AMC_Operations_v2_0.pdf` (11 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-20: AMC Operations (Component #20 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-09 |
| Owner | PPC Lead |
| Supersedes | SOP-20 v1.0 (2026-07-24) in full |
| Thresholds | Master PPC Decision Criteria System v4.0 only. Zero local thresholds |
| Decision record | AMC Build-or-Defer Memo v1.0 (verdict: **BUILD**) |

**Verdict / purpose.** AMC is the account's only deduped, user-level, cross-format evidence source. It enters the system **exclusively as a measurement layer with named consumers**. It issues **zero verdicts** from the closed vocabulary, because v4.0 contains no AMC rule, band or threshold. Every decision an AMC read touches is issued elsewhere, with the filed AMC result attached as evidence.

v2.0 changes from v1.0:
- procedures 6 to 12
- failure modes 6 to 10
- worked examples 1 to 4
- adds Elements 11 and 12 (conflict C5)
- retires v1.0's 6-row verdict table: none of its strings is in the closed vocabulary, so they become operating states pending v4.1 (AM-1)

Scope: instance provisioning and linking across both entity ad accounts; schema versioning and console reconciliation; the versioned 5-query template library (Q1-Q5) and its build order; the monthly Q1-Q3 cycle and filing standard; reading rules; audience construction at platform minimums and handoff into SD; refresh, decay watch, retirement; the quarterly Q5 dayparting evidence gate; ad-hoc named-evidence runs; new-query governance.

Layer economics (Strategic Doctrine v1.0 Section 10 "AMC, DSP, and the Measurement Layer", platform state verified July 2026):
- **0 license cost** since the September 2025 self-service change
- **24-month lookback** in history
- **5 template queries**
- **2 audience platform constraints:** 2,000-user minimum, 500-user lookalike seed

### 1.1 A measurement layer, never a decision layer
1. No bid, budget, placement, negation, structure or status change cites an AMC number unless a v4.0-issued verdict names that filed result as evidence. A breach is F1 and escalates on first occurrence.
2. Every query exists because a named consumer SOP reads it into a named decision. A query without a consumer is retired (F3).
3. The layer's outputs are records, not actions: filed result sets, audience records, gate answers, log entries. Each carries a window, a query version and a schema version, so a consumer can audit the evidence in the same **30 seconds** v4.0 Section 13 demands of every Master Action Record.

### 1.2 Why zero verdicts
- **Closed vocabulary sources:** KDR Template v3.0 "Bands & Verdicts Reference" sheet (**25 strings**) and v4.0 Section 13.1 "The Closed Verdict Vocabulary" (**18 actions**). The 18-vs-25 divergence is a registered program finding (#41, #46 builds). This SOP quotes the KDR strings and names the v4.0 equivalent where they differ. Neither list contains an AMC action.
- **Nearest v4.0 touch points:**
  - G2 (per-cell sufficiency)
  - Section 8.10 "Brand-Format Scenarios (S-F1 to S-F8)" (consumes Q1-Q3)
  - Section 9 rule **L10** (dormant dayparting lever; Q5 is its evidence gate)
  - Section 14 rule **V4** (monthly/quarterly slots)
- **Precedent:** SOP-43 (Ledger row #43): issue nothing, run named operating states as register vocabulary, log every needed number as a v4.1 amendment.

## 2. Scope and boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold/band/gate/scenario/verdict; this SOP files evidence. The 5 missing numbers are AM-1 to AM-5 |
| SB/SBV/SD Playbook (#17-19) | Owns all SD execution: audience campaign entry, caps, click-attributed grading vs ceiling, Performance+ guardrails, every format verdict. This SOP hands over audience records and filed sets; it never creates, funds or grades a campaign. Referenced by component number/clause only: the Tier 2 copy attached to this build is **v1.0** while Ledger row #17 records **v2.0** as current (conflict **C8**, third occurrence), so no playbook procedure number is load-bearing |
| #45 Dayparting (deferred) | Owns the deferral and its trigger. This SOP produces quarterly Q5 evidence; it never deploys an hourly modifier. Per L10 dayparting stays dormant until the **Marketing Stream feed (Catalog D12, Ledger dependency D5)** lands with **≥4 weeks of hour-level evidence per campaign**. Q5 alone opens an evaluation, never a lever |
| #21 DSP and Sponsored TV | Both deferred per the Build-or-Defer Memo v1.0 Section 4, with named re-evaluation triggers. AMC audiences deploy into SD without DSP (the memo's stated reason the deferral stands) |
| #35 Incrementality testing | Owns test design/run/read. Q2 overlap is observational context; it never substitutes for a #35 test; no incrementality claim cites Q2 alone |
| #32 Event windows | Owns event plans and armed-window state; reads honor **G10** (event weeks + 14 days following excluded from trend verdicts) |
| #39 Data feeds and manifest | Owns feed definitions, T7 field groups, retention lines. AMC has **no Catalog field-group row in T7** today; the request is interface I-9 |
| #46 Access and permissions | Owns instance seats. An AMC seat without an Access Register row suspends on discovery; the cycle halts until it registers (I-10) |
| #6 V5 prediction scoring | Scores the memo's 5 quarter-one predictions and every gate-answer prediction (V1, V5) |

## 3. Triggers
Numeric max-lag values do not exist in v4.0 (AM-5). The binding lag is the calendar relationship stated in each row.

| Trigger | Detecting artifact | Procedure | Max lag |
|---|---|---|---|
| Monthly cycle | Query calendar rows in the AMC Query Register | P4 | Filed inside the same V4 monthly slot and **before the M6 structure-target check reads Account Rollup tab A4** |
| Audience window advance | Refresh date column on the live audience record | P8 | Same week as the date; past date = F4 territory |
| Weekly decay watch | Pool-size column on every live audience record | P8 step 1 | Inside the weekly V4 slot; sub-minimum notifies the playbook owner the same week |
| Quarterly deep read | Query calendar quarterly row; V4 quarterly slot | P9 | Gate answer filed before the quarterly framework review closes |
| Named-evidence verdict | T2 or T3 verdict draft citing AMC evidence | P10 | Before the verdict deploys (rule **P10**: a verdict without complete justification does not deploy) |
| New-query proposal | Written proposal in the governance log | P11 | Decision recorded before any build |
| Platform/schema change | Schema version at a run differs from the Instance Record | P3 re-document, P12 | Before the next filing |
| Reconciliation fault | P2 monthly check: a format row absent or divergent | P2 step 4 | Data-refresh task the same day (G1 pattern) |

## 3b. Preconditions and gates
AMC has no T7 field-group row. The Data Architecture v1.0 Section 9 group list runs **A1-A8, B1-B11, C1-C8, D1-D12, E**, and none of them is AMC. Until #39 assigns one, every filed set carries a **manifest surrogate** header: window dates, query version, schema version, UNREAD cell count. G8 still binds consumers: a verdict whose named AMC evidence is missing or stale downgrades to a flag.

| Gate | Requirement / observable |
|---|---|
| Instance provisioned and linked (P1 record) | Both entity ad accounts linked. The P2 query returns SP, SB and SD rows, each nonzero, for the trailing full month. The Instance Record has instance ID, linked account IDs, schema version |
| Backfill present (Doctrine Section 10) | 24-month lookback returns data at creation. A P2 run windowed 12 months back returns populated rows |
| G2 sample sufficiency (v4.0 Section 5 "Layer 0: Gates (G1-G12). Nothing Proceeds Until These Pass") | "CVR verdicts ≥100 clicks; CTR verdicts ≥1,000 impressions," applied per query cell. Below the bar = **UNREAD** (no rate judgment; keyword analog = EXTEND TEST). The UNREAD count equals the sub-bar cell count, checked mechanically |
| G8 packet completeness | Manifest surrogate line present with 4 fields; a set without it = missing evidence |
| G9 price stability | A CVR-bearing read (Q2 conversion rates, Q5 hourly CVR) whose window spans a price change → **PROVISIONAL**, read from T5 Product Log price-move rows, with the T5 row named |
| G10 event exclusion | "Event weeks and the 14 days following are excluded from trend verdicts." Q5 hour-cells and trend reads in armed #32 windows excluded, from T5 trend-exclusion flags. Excluded-window list on the filed set. (SOP-12 v2.0 and the Data Architecture T5 column label this G12 → conflict **C9**; this SOP follows v4.0's IDs) |
| NTB boundary (Doctrine Section 7) | NTB tightened January 2026; every Q3 window starts **2026-02-01 or later** |
| Audience platform minimums (Doctrine Section 10) | Minimum audience **2,000 users**; lookalike seed **500**. Platform constraints, not decision thresholds (decision floor and lookbacks = AM-2). The creation record shows projected count vs 2,000 and seed vs 500 before handoff |
| Access current (#46) | Every seat has an Access Register row; an unregistered live seat suspends and halts the cycle |

## 4. Procedures

### P1. Instance provisioning and account linking (one time; 2-3 h + propagation)
1. Amazon Ads Console (primary entity account) > Measurement & Reporting > Amazon Marketing Cloud. Create the self-service instance (0 license cost). Record instance ID and region.
2. Link both entity advertiser accounts (**Ecotero LLC, Inspiratek LLC**) from the account-management screen. Both show active.
3. Confirm backfill: any template query windowed 12 months back returns populated rows.
4. Write the AMC Instance Record: instance ID, region, linked account IDs, creation date, schema version string (as shown in the query editor), #46 seat list.
5. Register seats with #46 the same day. The record is incomplete until the Access Register rows exist.

### P2. Console reconciliation and schema documentation (45-60 min at setup; 15 min monthly)
1. Run the template attribution query for the trailing full calendar month, grouped by format (SP; SB with SBV; SD), returning attributed conversions and sales per format.
2. Pull the same month's per-format totals from the ad console (Sponsored Ads reports, campaign-type rollup, same attribution window as displayed).
3. Compare per format. AMC's modeled, deduped attribution will not equal console last-touch, so the check is directional: every format present, nonzero, same order of magnitude. Record the signed delta on the Instance Record. No tolerance exists (AM-4); the delta series is the evidence for setting one.
4. Branch:
   - **In range:** stamp RECONCILED and proceed.
   - **Any format absent, zero, or off by an order of magnitude:** open a data-refresh task the same day (G1 pattern), file nothing, notify consumers the cycle is HELD (F7).
5. Document the schema version on every run. A changed version → P3 re-documentation + P12 NEW BASELINE before anything files.

### P3. Template query library (build 4-6 h across Q1 of operation; maintain with P12)
Build order (Memo Section 5): **Q1-Q3 in the first month, Q4 in the second, Q5 in the first quarterly cycle.** Register row per query: query ID, version, owner, named consumer SOP, decision fed, window convention, output table spec.

| Query | Spec | Consumer / decision |
|---|---|---|
| Q1 Path to conversion | By product family: ordered format-touch sequences before purchase. Output: path share table with 5 rows (SP-only, SB-assisted, SBV-assisted, SD-assisted, multi-touch); share of converters and CVR per path; trailing full month | #17-19 monthly format-split read vs **M6** (v4.0 Section 10 "Layer 5: Sizing Mathematics (M1-M10)", SP ~80%, SB 15-20%, SD 5-10%, deviations are findings). Path evidence is what the marginal format dollar re-justifies with |
| Q2 Cross-format overlap | Deduped users touched by ≥2 formats; overlap share of converters; CVR of multi- vs single-format users; trailing full month | SB role grading under **S-F1, S-F2** (SB judged on NTB% and brand value, never SP metrics); SB incrementality read on deduped users |
| Q3 NTB depth | NTB share by format and term class; post-2026-01 windows only; trailing full month | Brand-growth composition strategy read; NTB% input to S-F1. A strategy read, not a bid input, unless a verdict names it |
| Q4 High-intent audiences | Cart abandoners; detail-page viewers without purchase; per family; lookback recorded on each audience record (no v4.0 window: AM-2); built as audiences only where P6 clears | Playbook SD audience entry (capped, click-attributed, ceiling-governed); this SOP hands the record only (I-3) |
| Q5 Hourly evidence | Conversions and CVR by hour, by family, **24 cells per family**; per-cell G2; event windows excluded (G10); quarterly window | #45 deferral: the quarterly evidence gate (P9). Deployment evidence is still L10's Marketing Stream condition |

### P4. Monthly cycle execution and filing (90-120 min)
1. Run P2 first. A failed reconciliation holds the cycle (F7).
2. Run Q1, Q2, Q3 at current versions, trailing full month, per family.
3. File each set with the manifest surrogate header: query ID and version, window start/end, schema version, row count, UNREAD cell count, PROVISIONAL and event-exclusion flags where they apply, and reading notes of **≤3 sentences per finding**.
4. T6 Decision Log entry (**11 columns** per Data Architecture v1.0 Section 9 "The Infrastructure Tabs: Logs and the Manifest (T5-T7)"): date, level, target = filed set IDs, rule reference = SOP-20 P4, expected outcome where a prediction is logged, review date = next cycle.
5. Notify the playbook owner the cycle is filed **before the monthly M6 check reads A4**. The consumer cites the filed result, never a screenshot (F9).

### P5. Reading rules (every read; 15 min/set)
1. Per cell G2: a CVR cell under 100 clicks or a CTR cell under 1,000 impressions = UNREAD. Never interpolated or averaged into neighbors (F2).
2. Classify the read: strategy input (default) or named evidence (only when a verdict names the filed set per P10). No bid or budget change cites AMC without a v4.0 verdict naming it (F1).
3. Exclude armed event windows + 14 days following from trend statements (G10; T5 flags, I-6).
4. Hold the NTB boundary: no Q3 comparison spans 2026-01 (F8).
5. Never trend across query versions; a changed query = new version = NEW BASELINE (P12, F5).

### P6. Audience construction from Q4 (30-45 min/audience)
1. Pull the projected member count from the audience-creation screen (plus seed count for lookalikes).
2. Decision tree:
   - **A:** projected ≥2,000 (and seed ≥500 if lookalike) → create at its recorded window.
   - **B:** projected <2,000 → do not create (never "created small"). Log the count and shortfall. Re-propose only when the pool grows or the window is legitimately widened, which is a new audience version.
   - **C:** minimums clear but the window deviates from the register convention for the class → create only with the deviation recorded (no v4.0 basis, AM-2).
3. Naming: **`AUD-<family>-<queryID>v<version>-<window>-<YYYY-MM>`**.
4. Audience record: name, query ID and version, window, projected count at creation, seed count, creation date, refresh date, status CREATED.
5. The creation decision belongs to the D-holder: PPC Lead (Authority Matrix v2.0 Section 1 row "AMC cycle (#20)"). The operator prepares.

### P7. Audience handoff into SD (15 min; execution = #17-19)
1. Hand the record to the playbook owner by component number. The playbook governs the campaign build, caps, click-attributed grading vs T0 ceiling cells, and every format decision. This SOP launches nothing.
2. Record the handoff date and receiving owner. Status stays CREATED until the playbook reports a hosting campaign (I-4), then LIVE.
3. Until a record exists and is handed over, playbook SD audiences run on console remarketing pools only (I-3).

### P8. Refresh, decay watch, retirement (10 min weekly + refresh events)
1. Weekly, read the pool size of every LIVE audience. Under 2,000: notify the playbook owner the same week; the hosting campaign pauses per that SOP; status → **DECAYED** (skipping the watch = F4).
2. On the refresh date, re-project. ≥2,000: refresh and update the record. <2,000: run the P6 tree (a widened window is a new version, not a silent edit).
3. Retire when the pool stays under 2,000 across **2 consecutive refresh checks** or the consumer campaign closes: status **RETIRED**, with date and reason. Records are never deleted.

### P9. Quarterly Q5 and the dayparting evidence gate (2-3 h/quarter)
1. Run Q5 per family, trailing quarter, excluding armed event windows and their 14-day tails.
2. Per family, G2 per hour-cell: count readable cells (CVR cells ≥100 clicks) and UNREAD out of 24.
3. Pattern read on readable cells only: pooled CVR per readable day-part vs the readable remainder, stated as points of premium and relative %. No interpolation (F2).
4. Decision tree:
   - **A:** readable majority (**≥13 of 24**) and a pattern the D-holder judges material → gate answer "pattern present"; the PPC Lead may open a dayparting evaluation toward #45. Deployment still waits on L10 (Marketing Stream, ≥4 weeks hour-level per campaign). The materiality bar does not exist (AM-3); the call is the D-holder's.
   - **B:** readable majority, no material pattern → DEFERRAL CONTINUES on evidence, filed with the computed premium.
   - **C:** UNREAD majority → DEFERRAL CONTINUES by insufficiency, filed with the UNREAD count.
5. File the gate answer with a V1 prediction where A opens an evaluation (metric, direction, magnitude, horizon). Write the T6 entry, route to the #45 owner (I-5), score through #6 next quarter.

### P10. Ad-hoc named-evidence runs (30-60 min/request)
1. Trigger: a T2/T3 verdict draft cites AMC. Run the named query at its current version for the needed window.
2. File the result versioned and cross-referenced to the verdict's record ID. The Master Action Record evidence line cites the filed set ID, never a screenshot or unfiled number (F9).
3. Per v4.0 Section 12 "Layer 7: Precedence and Conflict Resolution (P1-P10)" rule P10, the verdict does not deploy until justified. An AMC citation without a filed set is incomplete.
4. Log the run in the governance log with the requesting verdict.

### P11. New-query governance (30 min/proposal; quarterly review in V4 slot)
1. Written proposal: query, consumer SOP by number, decision fed, all written before anything is built ("Measurement without a consumer is a hobby").
2. Tree:
   - **A:** consumer + decision named, no existing coverage → ADMITTED, built at v1 with a complete register row.
   - **B:** consumer named but an existing query feeds that decision → DECLINED with a pointer.
   - **C:** no consumer or decision → DECLINED.
3. Quarterly: a query whose consumer has not cited a filing for **2 consecutive quarters** retires (RETIRED). This is library hygiene, not a spend threshold.
4. Admissions, declines and retirements go to the governance log with the D-holder sign-off.

### P12. Query versioning and re-baselining (10 min/change)
1. Any change to logic, dimensions, measures, window convention or underlying schema = new version. Increment the register row and record the change and date.
2. A new version is a NEW BASELINE: cross-version trends are void, and a filing that trends across the boundary re-files split at it (F5).
3. A platform schema change re-versions every affected query in one register pass before the next cycle files.

## 5. Rules, thresholds and numbers

### v4.0 and Doctrine references
| ID | Meaning as described |
|---|---|
| G1 | Same-day repair / data-refresh pattern |
| G2 | "CVR verdicts ≥100 clicks; CTR verdicts ≥1,000 impressions", applied per cell |
| G8 | Packet completeness; missing/stale named evidence downgrades the verdict to a flag |
| G9 | Price stability; CVR read spanning a price change → PROVISIONAL |
| G10 | Event weeks + 14 days excluded from trend verdicts (labeled G12 elsewhere, C9) |
| M6 (Sec 10, M1-M10) | SP ~80%, SB 15-20%, SD 5-10%; deviations are findings |
| S-F1, S-F2 (8.10) | SB judged on NTB% and brand value; S-F1 condition "NTB% healthy" |
| S-F3, S-F4 (8.10) | SBV arbitrage entry/exit (owned by #17-19) |
| S-F1 to S-F8 | Brand-Format Scenarios |
| L8 (Sec 9) | SBV substitution lever |
| L10 (Sec 9) | Dormant dayparting lever: Marketing Stream curves with ≥4 weeks of hour-level evidence per campaign |
| P10 (Sec 12) | A verdict without complete justification does not deploy |
| V1, V5 (Sec 14) | Prediction fields; unscored actions do not accumulate; scoring |
| V3 | Amendment protocol for admitting register vocabulary |
| V4 (Sec 14) | Daily/weekly/monthly/quarterly cadence slots |
| Sec 13 / 13.1 / 13.2 | 30-second Master Action Record audit; 18-action closed vocabulary; Human-mandatory review tier |

### Numbers
| Item | Value |
|---|---|
| License cost | $0 (self-service since September 2025) |
| Lookback | 24 months; backfill check at 12 months back |
| Template queries | 5 (Q1-Q5) |
| Audience minimum | 2,000 users (platform) |
| Lookalike seed minimum | 500 (platform) |
| CVR cell sufficiency | ≥100 clicks |
| CTR cell sufficiency | ≥1,000 impressions |
| Q5 cells | 24 per family; readable majority = ≥13 of 24 |
| Event exclusion | Event weeks + 14 days |
| NTB boundary | January 2026; Q3 windows start ≥2026-02-01 |
| Audience retirement | <2,000 across 2 consecutive refresh checks |
| Query retirement | No consumer citation for 2 consecutive quarters |
| L10 deployment evidence | ≥4 weeks hour-level per campaign |
| Reading notes | ≤3 sentences per finding |
| T6 row | 11 columns |
| Manifest surrogate | 4 fields (window dates, query version, schema version, UNREAD count) |
| Record audit | 30 seconds (v4.0 Section 13) |
| Filed set retention | Until superseded, minimum 24 months |
| Vocabulary counts | KDR 25 strings vs v4.0 13.1 18 actions |
| Procedure times | P1 2-3h; P2 45-60m setup / 15m monthly; P3 4-6h; P4 90-120m; P5 15m; P6 30-45m; P7 15m; P8 10m; P9 2-3h; P10 30-60m; P11 30m; P12 10m |
| Operator ramp | Reproduce all 8 Economics Worked-Example Set computations cold (E6, E8 defended verbally) |

### Worked examples (illustrative)
- **WE-1:** Window 2026-07-01 to 07-31, schema v2.4.1, Q2 v1, Q3 v1.
  - Q2: 20,000 deduped converters, 3,680 multi-format = 18.4%; multi CVR 8.1% vs single 5.2% = 1.56x.
  - Q3: SB-touched 2,400, 984 NTB = 41.0%; SP-only 14,100, 3,384 NTB = 24.0%. 0 UNREAD.
  - A4 shows SP 78.4% / SB 16.2% / SD 5.4%, all in band; no rebalance.
- **WE-2 (fictional base AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max 26.3%):** Q4 v1 cart-abandoner pool, satin family, 30d, projected 3,900 (95.0% headroom). Name `AUD-SATIN-Q4v1-30d-2026-08`. First read CPA $17.20 vs $28.00 = 61.4% of ceiling.
- **WE-3:** `AUD-DCLR-Q4v1-30d-2026-06` created at 2,240. Week 9: 1,760 (240 short = 12.0%; down 480 = 21.4%) → DECAYED. Widened to 60d re-projects 2,610, which is a new version: `AUD-DCLR-Q4v2-60d-2026-08`; v1 retired, "pool decay below platform minimum."
- **WE-4:** Q5 v1, DCLR family. 8 of 24 readable (6 evening, 2 midday); 16 UNREAD = 66.7%; near-misses at 87 and 41 clicks are UNREAD. Evening 780 clicks / 42 orders = 5.4%; midday 240 / 12 = 5.0%; premium 0.4 pts = 7.7% relative. Interpolation attempt → F2. Branch C, DEFERRAL CONTINUES.

## 6. Data inputs required
- **AMC instance**: query execution surface (query editor with schema version string); audience-creation screen with projected member counts and lookalike seed counts; instance ID, region, linked accounts.
- **Both entity advertiser accounts**: Ecotero LLC, Inspiratek LLC.
- **AMC template attribution query** results by format (SP; SB with SBV; SD): attributed conversions and sales, trailing full month.
- **Ad console Sponsored Ads reports**: campaign-type rollup per format, same month, same attribution window (for P2).
- **AMC Query Register and calendar rows** (query ID, version history, owner, consumer SOP, decision fed, window convention, output spec).
- **Query outputs**: Q1 path table, Q2 overlap, Q3 NTB by format and term class, Q4 cart abandoners / non-purchasing detail-page viewers per family, Q5 hourly conversions and CVR per family.
- **Audience records**: pool sizes, refresh dates, status, windows.
- **T5 Product Log**: price-move rows (G9) and trend-exclusion flags (G10).
- **Account Rollup Workbook tab A4** (Structure targets; the consumption check) and **A3** (scoreboard).
- **T6 Decision Log** (write-back; 11 columns).
- **T2 / T3 verdict drafts** citing AMC (P10 trigger).
- **T0 ceiling cells** (used by the playbook for grading).
- **#46 Access Register** filtered view (seats).
- **#32 armed event window dates**.
- **#17-19 deployed-audience campaign status**, weekly (I-4).
- **Build-or-Defer Memo v1.0** (build order Section 5, deferrals Section 4, risks Section 2, 5 quarter-one predictions).
- **Governance log**.
- **Economics Worked-Example Set v1.0** (operator ramp).

## 7. Outputs and artifacts
| Artifact | Content / storage | Retention | Consumer |
|---|---|---|---|
| AMC Instance Record | Instance ID, region, linked accounts, creation date, schema version history, reconciliation delta series, #46 seat list; 1 file in the AMC folder of the PPC document library, indexed by the Query Register | Life of instance + supersession per #1 | P2; #46; audits |
| AMC Query Register | 1 row per query: ID, version history, owner, consumer SOP, decision fed, window convention, calendar rows | Permanent, append-only | P3-P5, P11, P12; quarterly review; #44 |
| Monthly Filed Result Sets (Q1-Q3) | Versioned files with manifest surrogate header (query ID+version, window start/end, schema version, row count, UNREAD count, PROVISIONAL/event flags) + reading notes | Until superseded, min 24 months (retention line pending #39) | #17-19 M6 read and S-F grading; P10 verdicts |
| Audience Records | Name, provenance, counts vs minimums, window, status history (CREATED/LIVE/DECAYED/RETIRED), handoff line (date + receiving owner) | Permanent, append-only | #17-19 SD entry; P8; F10 audit |
| Quarterly Q5 Gate Answer | Readable and UNREAD counts, excluded windows, computed premium, branch, V1 prediction | Permanent | #45 (I-5); #6; quarterly framework review |
| Governance Log | P11 admissions/declines/retirements; P10 run log with requesting verdicts | Permanent, append-only | Quarterly review; #1 run ledger |
| T6 Decision Log entries | 11-column rows for cycles, audience decisions, gate answers | Permanent | Account Rollup A3; #6 |
| Data-refresh task | On a P2 fault | n/a | Data Operations |
| Alarms F1-F10 | Evidence lines (set ID, cell or record, gate or rule reference) | n/a | Per escalation routing |

### Verdict mapping
Zero closed-vocabulary verdicts. Retired v1.0 local strings: RUN CYCLE / FILE; CREATE / REFRESH / RETIRE AUDIENCE; UNREAD; OPEN DAYPARTING EVALUATION; DEFER CONTINUES; ADMIT / DECLINE / RETIRE QUERY.

**5.1 Verdicts that may name AMC evidence:**
| Verdict (KDR v3.0) | AMC role |
|---|---|
| ENTER SBV ARBITRAGE | Q1 path shares and Q2 overlap may inform candidacy; the inequality, entry and exit belong to #17-19 (S-F3, S-F4, L8). v4.0 13.1 equivalent: **FORMAT SUBSTITUTION (SBV/SD)** |
| INCREMENTALITY LADDER | Q2 is context; #35 owns it; no ladder cites Q2 alone |
| QUARANTINE: DATA REFRESH | On a P2 failure the consumer rows follow quarantine; v4.0 equivalent **FLAG: DATA REPAIR** (G1, G8) |

**5.2 Operating states (register vocabulary, pending AM-1):**
| State | Where set / what it permits |
|---|---|
| RECONCILED / HELD (cycle) | P2 step 4 |
| FILED (result set) | P4 step 3; only FILED sets may be cited |
| UNREAD (cell) | P5 step 1; forbids interpolation |
| CREATED / LIVE / DECAYED / RETIRED (audience) | P6-P8; DECAYED requires the same-week pause notice |
| ADMITTED / DECLINED / RETIRED (query) | P11 |
| DEFERRAL CONTINUES / EVALUATION OPEN (gate answer) | P9; EVALUATION OPEN routes to #45 and deploys nothing |
| STALE | Prior filed set when I-1 fails |
| NEW BASELINE | P12 |
| PROVISIONAL | G9 |

### Failure modes
| Mode | Detection | Response | Motivation |
|---|---|---|---|
| F1 Parallel decision system | Change citing AMC with no v4.0 verdict naming a filed set | Withdraw; route to owner; escalates on first occurrence | Doctrine Section 10 |
| F2 Sub-minimum interpretation | Reading interprets, averages or interpolates an UNREAD cell | Re-file with UNREAD marked | Memo Section 2 (misreads → confident nonsense) |
| F3 Orphan queries | No consumer citation for 2 consecutive quarters | Retire | Memo value test |
| F4 Audience decay unwatched | LIVE pool <2,000 or skipped weekly read | Same-week notice; pause; DECAYED | v1.0 F4 |
| F5 Unversioned query drift | Changed query filed under its old version; cross-version trend | Re-version, NEW BASELINE, re-file split | v1.0 F5 |
| F6 Dayparting on optics | Dayparting proposal without a filed Q5 gate answer | Decline at intake | The one institutional trace: dayparting planning sheets existed before any hour-level evidence |
| F7 Reconciliation divergence | Format absent, zero, or off by an order of magnitude | Data-refresh task same day; HELD; notify | New at v2.0 |
| F8 NTB boundary breach | Q3 window starting before 2026-02-01 or a trend spanning 2026-01 | Re-file post-boundary; comparison void | Doctrine Section 7 |
| F9 Screenshot citation | AMC number with no filed set ID | Run P10, file, re-issue | New at v2.0 |
| F10 Audience live without record | No creation record showing the 2,000/500 check, or a name that does not parse | Suspend handoff; write/reconstruct the record or retire | Mirrors #46 |

Escalation: F1 → PPC Lead on first occurrence, CEO informed. F7 → Data Operations same day. F2, F4, F5, F8, F9, F10 → monthly cycle review. F3, F6 → quarterly review.

### Interface contracts
| ID | Sender → receiver | Artifact / timing | Non-arrival |
|---|---|---|---|
| I-1 | AMC platform → here | Results and schema at every run | Files late with the gap noted; consumers read the prior set marked STALE |
| I-2 | Here → #17-19 | Monthly Q1-Q3 sets before the M6 check reads A4 | Split check runs console-only; no rebalance may cite AMC that month |
| I-3 | Here → #17-19 | Audience records on creation | SD runs on console remarketing pools only |
| I-4 | #17-19 → here | Deployed-audience campaign status, weekly | Treat live-unknown as LIVE; gap logged |
| I-5 | Here → #45 owner (PPC Lead) | Quarterly Q5 gate answer | Deferral continues; planning sheets stay empty |
| I-6 | #32 → here | Armed windows via T5 trend-exclusion flags | Trend claims suppressed to observations |
| I-7 | v4.0 owner (#8, PPC Lead) → here | Admitted AMC rules at each increment | Zero-verdict mapping stands; AM-1 to AM-5 open |
| I-8 | Here → #6 | Memo's 5 predictions + V1 predictions | Quarterly review flags the gap; scorecard held open |
| I-9 | Here → #39 | Request for T7 AMC field-group row + retention line | Self-carried surrogate header; missing evidence → flags per G8 |
| I-10 | #46 → here | Access Register rows | Unregistered seat suspends; cycle halts |
| I-11 | Here → T6 and A3 | Decision-log rows + V5 scores | Monday audit flags; predictions score late |

## 8. Decision rights
- Authority Matrix v2.0 Section 1 row **"AMC cycle (#20)"**: **CEO I, PPC Lead D, Incoming operator E, BM owner I.** Standing Rule 5 on vacancy: D → PPC Lead, E → PPC Manager.
- **AI-executable with audit:** query runs; filings with drafted notes; reconciliation computation; decay watch; Q5 counts and premium; drafted audience and T6 records.
- **Human-mandatory (D-holder):** audience creation and retirement; query admission and retirement; the P9 gate answer and any EVALUATION OPEN; any P10 evidence attachment to a verdict in the Human-mandatory review tier (v4.0 Section 13.2).
- The materiality call in P9 Branch A is the D-holder's.
- The incoming operator holds E; every D remains the PPC Lead's during and after the ramp.

## 9. Account-specific facts
- **Entities:** Ecotero LLC and Inspiratek LLC, two advertiser accounts linked to one AMC instance (primary entity account creates it).
- AMC platform state verified **July 2026**. Self-service change dated **September 2025**.
- The Build-or-Defer Memo verdict was BUILD. **DSP and Sponsored TV (#21) are deferred.** **Dayparting (#45) is deferred** pending the Marketing Stream feed (Catalog D12 / Ledger D5).
- Families named in examples (illustrative): **SATIN**, **DCLR**. Example schema v2.4.1 is illustrative.
- Institutional trace: dayparting planning sheets existed before any hour-level evidence (they must stay empty until the gate opens).
- v1.0 records no named, dated incidents.
- The Tier 2 copy of the #17-19 playbook attached to this build was v1.0 while the Ledger says v2.0 (C8).
- AMC has no T7 field-group row. T7 groups are A1-A8, B1-B11, C1-C8, D1-D12, E.

## 10. Open items
| ID | Item |
|---|---|
| AM-1 | Admission of the AMC operating states (5.2), or a standing register-vocabulary exception per V3, retiring v1.0's 6 local strings |
| AM-2 | Pool-entry floor and lookback windows for AMC/SD audiences as decision thresholds (2,000/500 are platform constraints only) |
| AM-3 | Q5 materiality bar (what CVR premium at what readable-cell coverage opens an evaluation) |
| AM-4 | P2 reconciliation divergence tolerance (AMC vs console) |
| AM-5 | Element 2 numeric lag table |
| C5 | Elements 11/12 absent from shipped SOPs; added |
| C8 | #17-19 version mismatch (attached v1.0 vs Ledger v2.0), third occurrence |
| C9 | G10 vs G12 labeling of event exclusion |
| 18-vs-25 | Closed vocabulary count divergence (registered by #41, #46) |
| Routed to #39 | T7 field-group assignment for AMC filed sets; retention policy line (I-9) |
| Close-out | This component's Ledger row returned with the build |
| v1.0 corrections | "the v4.0 conversion minimum" → G2 (carried); "the v4.0 lookback windows" → resolves to nothing (AM-2) |
| Named documents not present | Criteria System v4.0; KDR v3.0; AMC Build-or-Defer Memo v1.0; Strategic Doctrine v1.0 (Sections 7, 8, 10); #17-19 playbook; SOP-43; SOP-12 v2.0; #1, #6, #21, #32, #35, #39, #41, #44, #45, #46; Master PPC Data Architecture v1.0; Command Workbook READ ME; Authority Matrix v2.0; Cross-Reference Ledger; Economics Worked-Example Set v1.0; Supersession Map |

Version triggers:
1. Platform change to minimums, lookback, templates or schema.
2. A v4.0 increment admitting AM-1 to AM-5.
3. D5 Marketing Stream lands (Q5 becomes L10 deployment evidence, I-5 rewrites, #45 opens its build).
4. A Memo Section 4 re-evaluation trigger fires: an audience class hitting SD reach limits, a retargeting economics case, or a video pipeline plus material Q1 upper-funnel share. #21 reopens.
5. A #17-19 increment moves the SD audience-entry seam (I-3, I-4 re-pin).
6. Any MISS on the memo's 5 quarter-one predictions.
