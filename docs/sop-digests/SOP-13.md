# SOP-13 Digest: Phrase Campaign Operations and the Per-Family Pilot

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-13: Phrase Campaign Operations and the Per-Family Pilot |
| Type | PPC Department Operating SOP, Component #13 of the Operations Definition Register |
| Version | 2.0 |
| Date | 2026-07-28 |
| Owner | PPC Lead |
| Supersedes | SOP-13 v1.0 (2026-07-24) in full |
| Threshold policy | Thresholds live in the Master PPC Decision Criteria System only; zero local thresholds |
| Threshold authority for this build | Uploaded Master PPC Decision Criteria System **v3.0**, operating as the v4.0 authority per the 2026-07-28 session ruling **PPC-DR-02**; cited by its printed section headings |
| Length | 11 pages; 9 procedures, 25-string verdict mapping, 3 worked examples, 9 failure modes, Elements 11 and 12 |

**Verdict/purpose.** Phrase is **qualified discovery on proven roots**, and it is the account's one named structural gap at the match-type layer. Evidence: Criteria System F8 (Structure and Registry family) states a primary syntax at 0% phrase is a standing finding; scenario **S-H8** (Section 8.9 Discovery Scenarios) fires on a phrase layer at $0 spend on a product with proven exact roots; the **M6** structure targets (Section 10 Sizing Mathematics) set a **5-10% phrase spend destination**; Data Architecture v1.0 Section 11 (A4 Structure targets) records the **Bamboo 4pc product-wide $0 phrase** as a live one-cell finding. The SOP governs: family phrase campaign creation, the dated per-family pilot that closes the S-H8 gap, the weekly operating pass, stem-clustering read, phrase-broad dedup wall, CAP SYNTAX receipt, event-window overlay, pause and retirement, and stem graduation handoff. v2.0 claims Elements 11 and 12 were absent from all 25 shipped SOPs including the SOP-12 v2.0 exemplar.

## 2. Scope & Boundaries

### The two phrase surfaces (Section 1.1)
- **Surface 1 — family phrase campaign:** one campaign per primary syntax family, Objective = Discovery, seeded with family root as phrase plus validated modifier stems, budget-capped by design, never straddling two families (family is the cap-enforcement unit per rule **P4**, Section 12).
- **Surface 2 — standing long-tail stem coverage:** validated stems whose per-term volume never clears the graduation bar stay in the family phrase campaign at a profitable bid as a deliberate end state under **LEAVE TO HARVEST** ("graduating 20 micro-terms one by one is noise"). Movement off Surface 2 only via P4 stem routes; never mid-pass judgment.

### Session rulings and conflicts declared (Section 1.2)
- (a) **PPC-DR-02** (ruled): uploaded Criteria System v3.0 is the threshold authority the corpus cites as v4.0.
- (b) **PPC-DR-04** (provisional): verdict strings quoted from KDR Template v3.0 "Bands and Verdicts Reference" (25 strings); Criteria System S13.1 lists 18 differently worded actions; AM-1.
- (c) **Ledger conflict C3**: #31 has no procedural document; budget law referenced as instrument (T1 S3 spend-governance columns, M5 queue per Section 10).
- (d) **Citation drift**: uploaded Criteria System has no Section 4.2 naming convention; per its Section 17.2, naming remains authoritative in the v1.0 Criteria System (outside the pack); naming references SOP-12 v2.0 Appendix A.

### Boundaries

| Adjacent | Seam |
|---|---|
| Criteria System (v3.0 as v4.0) | Decides every threshold, band, gate, scenario, verdict, lever limit; this SOP executes |
| #30 Harvest and graduation | Decides which stems graduate. P4 routes candidates to #30; GRADUATE FROM DISCOVERY returns; SOP-12 stands exact up. This SOP never issues a graduation |
| #29 Negation architecture | Owns negation doctrine, wall rules, wall audit. This SOP builds prescribed walls same session and hands F2 breach findings to #29 |
| SOP-14 Broad operations | Owns shared weekly triage machinery (SOP-14 P3: three candidate routes, yield read, head-term check, staging). This SOP runs it by reference and adds only P4 and P5. A change to SOP-14 P3 increments both SOPs |
| SOP-12 Exact operations | Owns exact standup. Stem graduations and every ADD EXACT + RESTRUCTURE found in phrase execute in SOP-12 P1/P2; this SOP builds only the phrase-side steering negative |
| #31 Budget and envelope (instrument) | Budget deltas, CAP SYNTAX, pilot funding law from T1 S3 columns and M5 queue; never originated here; no #31 procedure number cited |
| #32 Deal and event windows | Owns event plan; this SOP freezes phrase structure inside armed G12 windows (P7) |
| #33 Sibling arbitration | Owns family term ownership; sibling-owned roots pre-loaded as negatives in P1 per declared S-F3 owner; phrase never seeds a sibling-owned root |
| #38 Bulk deployment mechanics | Owns pull, staging, upload, T+1 verification; every change staged in #38 format |
| Also referenced | #16 (conquest), #17-19 (SBV), #28 (placement/ladders), #35 (incrementality), SOP-23 (push), SOP-24 (recovery), SOP-06 (V5 scoring), #39 (Raw Pull Pack instrument; T6 retention fold-in), #41 (margin) |

## 3. Triggers

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Pilot standup | T2 K9 verdict FUND TEST (UNFUNDED PRIMARY) with dated release from M5 queue | Same day as dated release; Tuesday default otherwise per #38 | P2 |
| Weekly cadence | Monday cascade reaches T2; search-term feed pull date = current week in T7 | Same session as Monday pass; deploy Tuesday | P3 -> P4 -> P5 |
| Pilot review gates | Paired T3 yield rows at day 14 and day 28 | Gate decision within 1 working day of read landing | P2 steps 7-9 |
| Family qualification | T2 K8 "# Exact" >= 1 on family root with Validation State clean, plus T1 family row live | Enters next weekly verdict queue | P1 |
| Stem graduation receipt | GRADUATE FROM DISCOVERY record from #30 | Phrase-side steering negative same working session as SOP-12 standup (same day) | P9 |
| CAP SYNTAX receipt | T1 row Cap Status = BREACH with staged delta from instrument layer | Budget rows staged same weekly session | P6 |
| Event window arms | T2 "Event Mode" column set from #32 plan (G12) | Freeze effective day window arms | P7 |
| WAS breach on phrase row | T3 "WAS %" above Discovery limit (Section 3, F11 Waste and Negation) | Negation pass same weekly session | P3 route via SOP-14 machinery; wall check P5 |

## 4. Procedures

### Preconditions and gates (Section 3)
Missing/stale field group suppresses dependent execution class; pass records what it could not see (G8).

| T7 manifest ID | Requirement | Observable |
|---|---|---|
| A2 Deployment state | Current bulk state for every phrase campaign | T7 A2 = PRESENT; T3 rows carry State, Daily Budget $, Bid / AG Default $ from current-week BULK-US pull |
| A6 Objective + Expected CPC | Every phrase row tagged Discovery; seed bid reference exists | T3 Objective Tag = Discovery on 100% of phrase rows. T7 A6 PARTIAL: account reference Expected CPC **$2.80** stands in; every seed bid carries PROVISIONAL note |
| B5 Coverage counts | Registry current per match type | T2 # Exact / # Phrase / # Broad / # Auto reconcile to T3 registry for family |
| B8 Economics chain | T0 named cells live (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC) | T0 zone C populated; while T7 D1 PARTIAL (blended margin), G9 PROVISIONAL on every ceiling-referencing action |
| Search-term feed | SP + SB search term reports and STIS in Raw Pull Pack (Data Architecture S12) | Pull date = current week. Absent: P3, P4, P5 suppressed for week, suppression recorded |
| Root validation | Family root carries validated exact structure | T2 K8 # Exact >= 1, Validation State clean, no G1 quarantine flag |
| Gates in force | G2 sufficiency, G3 truncation, G12 event, P4 syntax caps | KDR Bands Reference: clicks < 15 = no bid read; in-budget < 70% = every rate truncated; Event Mode clear or plan names change; T1 Cap Status inside cap |

### P1. Create a family phrase campaign (standing state) — 45-75 min per family
1. Family qualifies: T2 K8 # Exact >= 1 on root, Validation State clean. Unproven root = broad's job (SOP-14); phrase on unvalidated root = F3.
2. No family phrase campaign exists: filter T3 Type = SP-P on family syntax tag. If exists, extend; second = F7-adjacent duplicate -> CONSOLIDATE DUPLICATES.
3. Gates: G12 clear (T2 Event Mode blank or plan names it); G3 not relevant at creation; #33 check (no seed on sibling-owned root per S-F3).
4. Name per SOP-12 v2.0 Appendix A, family root in keyword position, objective segment = **Disc**; non-parsing = SOP-12 F6, renames ride alone.
5. Stage on Sponsored Products Campaigns sheet per #38: Entity = Campaign, then Ad Group, then Keyword rows; Operation = Create; State = enabled; Targeting Type = Manual; Bidding Strategy = **Dynamic bids - down only** (Doctrine v1.0 S6.3: down-only default outside pushes); Daily Budget = family discovery allocation share from instrument layer, capped by design.
6. One ad group. Keyword rows: Keyword Text = family root, Match Type = phrase, plus each validated modifier stem as its own phrase row where stem volume justifies dedicated coverage. Bid = verdict-carried value; absent per-term Expected CPC, account reference **$2.80** with PROVISIONAL note in reason string.
7. Pre-load negatives per #29 in same staged set: negativeExact rows for every graduated exact the family holds, brand terms, sibling-owned roots, taxonomy-known irrelevant classes (Section 9, L5 pre-loaded mode).
8. **Control-level dedup wall:** negativeExact rows for every phrase seed term placed in the family BROAD campaign, same staged set. Record wall list in T3 (Negation State column). Skipping = F2 root cause.
9. Registry: T2 # Phrase increments per seeded term; new T3 row with Objective Tag, owner, wall list; T1 column MT Cov Phrase % picks it up via syntax tag.
10. Log in T6 with prediction (metric, direction, magnitude, horizon, review date; V1). No prediction = no deploy.
11. Deploy via #38: Tuesday default; same day for dated release; full T+1 verification.

### P2. The pilot (closes the S-H8 gap) — standup 60-90 min; gates 20-30 min each
1. Scope: one phrase campaign in each primary family with proven structure, **strongest family first**. Family in chronic CONVERSION diagnosis excluded until diagnosis clears (Section 8.2, **S-Y5**).
2. Funding **envelope-neutral**: reallocates from family's existing discovery share, never expands envelope (rule **P2**, Section 12). Record three numbers: $ stepped out of family broad budget; $ drawn from family's unspent discovery allocation; unchanged family discovery total.
3. Duration: dated window with reads at **day 14** and **day 28**. Standup T6 prediction: expected validated-term yield per $100 of spend vs family broad baseline, day-28 review date. No dated window + prediction = no deploy (F1).
4. Standup: execute P1 in full including step 8.
5. Instrumentation: T3 rows for pilot and family broad both carry yield read every pass (**Harvest Yield** column).
6. Weekly in window: P3-P5 normal; daily pacing glance on capped budget; **no scale steps inside window**.
7. **Day-14 gate, health only, 3 checks:** (1) spend pacing to cap (in-budget healthy per KDR budget-state bands); (2) negation cadence live (negatives added in both weekly passes); (3) zero wall breaches from P5. No scale/kill at day 14 unless stop-loss fires.
8. **Day-28 decision as verdict:** **SCALE** (extend P1 to remaining qualified families; pilot -> standing state); **HOLD** (extend window once, open question named); **RETIRE** (PAUSED-PENDING with re-entry condition; yield evidence to T6; S-H8 gap declared closed-by-evidence). Rule reads **yield and walls first**; ACOS governs only through Discovery objective band (Section 6, **O6**). "Comparable CPC" tolerance not in Criteria System (AM-3).
9. Day-28 decision is a scored V5 row vs standup prediction; gate artifact = decision table with both campaigns' yield reads side by side.

### P3. Weekly operating pass — 30-45 min per family, Monday cascade
1. Enter T2 only after T0 and T1 read (Data Architecture S2 rule 1).
2. Score last cycle first (V1).
3. Pull search-term data: Ads console > Measurement and Reporting > Sponsored ads reports > Create report > Sponsored Products > Search term, summary, date range aligned to **14-day pass window**, filtered to family phrase and family broad campaigns. Working columns: **Campaign Name, Ad Group Name, Targeting, Match Type, Customer Search Term, Impressions, Clicks, Spend, 7 Day Total Orders (#), 7 Day Conversion Rate, Cost Per Click (CPC)**.
4. Run SOP-14 P3 shared triage by reference (three candidate routes, yield read, head-term check, staging and deployment).
5. Run P4 and P5.
6. Stage per #38 with verdict and scenario ID; Tuesday deploy after BM huddle; T+1; mismatch = SOP-12 F10.

### P4. Stem-clustering read — 20-40 min
1. Normalize every served term: lowercase, strip terminal pluralization, sort tokens into a signature (same as Section 3 F8 twin-set detection, at stem grain).
2. Group by modifier stem around family root: size stems, attribute stems, use-case stems. Pool clicks and orders at stem level (G2 governs sufficiency; stem pooling has no explicit G2 clause, AM-4).
3. Route each stem through the tree; route by stem never by term (stem graduates once; F4 guard).
4. Append stem map to T3 notes in fixed line format: `stem | terms | clicks | orders | status | route | date`.

**P4 decision tree (4 branches)**

| Condition on pooled stem | Route | Executed by |
|---|---|---|
| Stem validated (orders at **S-H1** graduation bar, S8.9) AND volume clears dedicated-coverage read | Graduate stem as stem phrase: candidate to #30; on GRADUATE FROM DISCOVERY, SOP-12 stands exact up; P9 builds phrase-side steering negative same session | #30 decides; SOP-12 executes; SOP-13 P9 walls |
| Stem validated AND long-tail (below dedicated-coverage read) | LEAVE TO HARVEST: stays in phrase at profitable bid, noted per stem, re-read every pass | This SOP, Surface 2 |
| Stem invalid (clicks at reactive-negation bar with zero orders, F11 reactive mode) | Negative phrase on stem in family phrase campaign, staged this session | This SOP + #29 doctrine |
| Served string is a priority head term (oversight class) with # Exact = 0 | ADD EXACT + RESTRUCTURE at T2 per **S-R12** (S8.4 "Priority term (500+ SV, primary syntax) with zero exact campaigns"); head term clicks excluded from phrase yield read | T2 verdict; SOP-12 executes (WE-3, F6) |

### P5. Dedup wall audit — 10 min
1. Join served-term sets on Customer Search Term: family phrase vs family broad, from same P3 step-3 pull.
2. Any intersection = F2. Build negative-exact wall in broad on every intersecting term same day; record in T3 wall list.
3. Mark both campaigns' rate reads on intersecting terms confounded for window; exclude from yield read; double-bought spend reclassifies as **structure waste** (mirrors S8.9 treatment of **S-H4** unsteered leak).
4. Root-cause line in T6 names session that skipped wall step; recurring source escalates.

### P6. CAP SYNTAX receipt — 10-15 min
1. Trigger: T1 family row Cap Status = BREACH and instrument layer stages family delta.
2. Discovery reduces first in a capped family, **phrase and broad proportionally to their current discovery spend shares**; split executed here, cap decision not.
3. Stage Daily Budget reductions as #38 rows with CAP SYNTAX verdict and T1 finding ID in reason string; T6 predicts family share returning inside cap by next weekly read.

### P7. Event-window overlay
1. Arm on G12: #32 dates into T2 Event Mode; every phrase row flagged through window + post-event guard.
2. Inside window: phrase structure changes freeze (no seed additions, creations, stem graduation standups) unless plan names them. **Reactive and wall negation stays live.**
3. Event-week rates excluded from trend and yield verdicts through guard (G10); gates only. Pilot window never starts inside armed window and **pauses its day-count across one** (F9).
4. Post-window: seeds, bids, pilot clock resume from pre-event values as staged logged set per #32 reconciliation.

### P8. Pause, retirement, re-entry
1. PAUSED-PENDING carries reason and re-entry in T2 and T3; else incomplete.
2. RETIRE from pilot: pause campaign, disposition every standing stem (follows family broad as ordinary discovery, or negates), state re-entry condition (typically family diagnosis change or demand-signal change on root).
3. Paused rows = re-entry check only.
4. Archive only past governance period with no re-entry; human-mandatory; T6 archive entry closes history with final stem map.

### P9. Stem graduation handoff — same session as SOP-12 standup
1. On GRADUATE FROM DISCOVERY from #30, hand SOP-12 the graduation packet: stem phrase string, discovery CPC, pooled click and order evidence, served-term list under stem.
2. Build phrase-side steering negative same session exact goes live: negativeExact on graduated string in family phrase campaign; record in T3 wall list (closes F8 GRADUATED-UNSTEERED leak from phrase side).
3. T6 handoff line references SOP-12 creation prediction; no second prediction (one graduation, one scored prediction).

## 5. Rules, Thresholds & Numbers

| Item | Value | Source |
|---|---|---|
| Phrase spend destination (M6) | 5-10% | Section 10, M6 |
| Primary syntax at 0% phrase | Standing finding | F8 |
| S-H8 | Fires on phrase layer at $0 spend on product with proven exact roots | S8.9 |
| Family qualification | T2 K8 # Exact >= 1 on root, Validation State clean, no G1 flag | Section 3 |
| Account reference Expected CPC | $2.80 (PROVISIONAL) | T7 A6 PARTIAL |
| G2 bid read | clicks < 15 = no bid read | KDR Bands Reference |
| G3 truncation | in-budget < 70% = every rate truncated | KDR Bands Reference |
| Objective tag coverage | Discovery on 100% of phrase rows | A6 |
| Bidding strategy | Dynamic bids - down only (outside pushes) | Doctrine v1.0 S6.3 |
| Pilot window | reads at day 14 and day 28; HOLD extends once | P2 |
| Pilot day-14 checks | 3 (pacing to cap; negation cadence in both weekly passes; zero wall breaches) | P2 step 7 |
| Pilot gate decision lag | within 1 working day of read landing | Section 2 |
| Search-term window | 14-day pass window | P3 |
| Stem routing branches | 4 | P4 |
| S-R12 head term | Priority term (500+ SV, primary syntax) with zero exact campaigns -> ADD EXACT + RESTRUCTURE | S8.4 |
| Yield formula | validated terms routed / spend x 100 | Section 9 |
| Unrouted validated stem | sitting unrouted 2 passes = pass-quality finding | Section 12 |
| F8 negation lapse | WAS % above Discovery limit for 2 consecutive passes | F11 bands |
| Procedure times | P1 45-75 min; P2 standup 60-90 min, gates 20-30 min; P3 30-45 min/family; P4 20-40 min; P5 10 min; P6 10-15 min | Section 4 |
| Data timing | Raw Pull Pack Monday 06:00; refreshed by 09:00 | Data Architecture S12 |
| #41 D1 margin due | 2026-08-21 | Section 10 |

### Criteria System rule IDs referenced

| ID | Meaning as described |
|---|---|
| F8 | Structure and Registry family; 0% phrase finding; twin-set normalized-token signature; GRADUATED-UNSTEERED state |
| F11 | Waste and Negation family; WAS % Discovery limit; reactive mode |
| S-H1 | Graduation bar (orders) |
| S-H4 | Unsteered leak; spend reclassified as structure waste |
| S-H6 | Off-taxonomy converting terms negate if taxonomy does not expand |
| S-H8 | Phrase layer at $0 on product with proven exact roots |
| S-Y5 | Chronic CONVERSION diagnosis excludes family from pilot |
| S-R12 | Priority term (500+ SV primary syntax) with zero exact -> ADD EXACT + RESTRUCTURE before any performance verdict |
| S-F3 | Declared sibling term owner |
| M6 | Structure targets (phrase 5-10%) |
| M2 | Required-clicks chain (rank-objective instrument) |
| M5 | Funding queue |
| O6 | Discovery objective band (ACOS governs pilot only through this) |
| P2 | Envelope-neutral funding; never expand envelope |
| P4 | Family is cap-enforcement unit / syntax caps |
| G1 | Quarantine (QUARANTINE: DATA REFRESH) |
| G2 | Sufficiency |
| G3 | Truncation |
| G8 | Missing/stale field group suppresses execution class |
| G9 | PROVISIONAL margin tag |
| G10 | Event-week rates excluded from trend/yield through guard |
| G11 | Seeding into undeclared ownership conflict |
| G12 | Event window armed (also cited as rationale for cooling-in-satin class and MKL classification route) |
| L2 | Unlock mechanics |
| L5 | Pre-loaded negation mode |
| V1 | Prediction fields; score last cycle first |
| V6 | Version-pin sync rule |

### Verdict-to-execution mapping (phrase)

| Verdict | Phrase execution |
|---|---|
| QUARANTINE: DATA REFRESH | No changes; staged set carried to next clean cycle (G1) |
| UNLOCK TRAFFIC | Bid steps up per L2 on named phrase row; no rate judgment until G2 |
| FIX BUDGET (TRUNCATED) | Budget lever only (G3) |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Budget assurance only |
| FUND TEST (UNFUNDED PRIMARY) | Pilot standup enters via this verdict (P2), envelope-neutral funding stated |
| RANK PUSH: FUND SIZED PUSH | No phrase execution (exact; SOP-12, SOP-23); push citing phrase row = routing defect reported to T2 |
| RECOVERY PUSH | No phrase execution (SOP-24); same routing-defect rule |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | No phrase execution (M2 rank instrument) |
| FIX CONVERSION FIRST; DEFER PUSH | Phrase seeds hold at maintenance; no new seeds; pilot exclusion |
| PLACEMENT FIX FIRST | Bids hold; #28 |
| RE-POINT VARIATION | Advertised-SKU edit per SOP-12 P10 pattern on family campaign |
| TAPER | No phrase execution (SOP-12 P4) |
| HOLD; DEFEND LIGHTLY AT RANK | No change on any phrase instance |
| DEFEND AT FLOOR | No phrase execution |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Bid half on named phrase row one step; CAP SYNTAX half from T1 via P6 |
| INCREMENTALITY LADDER | No phrase execution (#35, #28) |
| ADD EXACT + RESTRUCTURE | P4 branch 4: SOP-12 standup; phrase-side steering negative same session; excluded from yield |
| CONSOLIDATE DUPLICATES | Two phrase campaigns on one family -> SOP-12 P7 precedence; this SOP flags |
| GRADUATE FROM DISCOVERY | P9 same session; stems graduate as stem phrases, never term by term |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | #29 doctrine; pre-load at P1 step 7, reactive at P3/SOP-14 and P4 branch 3, steering at P1 step 8 and P9 step 2 |
| ENTER SBV ARBITRAGE | No phrase execution |
| OPEN / ROTATE / EXIT CONQUEST | No phrase execution (#16) |
| STOP-LOSS: CONCEDE OR DEFER | Pilot RETIRE path or dated phrase test expiry: P8 steps 1-2 with yield evidence |
| PAUSED-PENDING | P8 steps 1-3 |
| LEAVE TO HARVEST | P4 branch-2 standing state |

## 6. Data Inputs Required

**Amazon reports / pulls**
- **Search Term Report (STR)**: Sponsored Products > Search term, summary, 14-day window, filtered to family phrase and broad campaigns. Columns: Campaign Name, Ad Group Name, Targeting, Match Type, Customer Search Term, Impressions, Clicks, Spend, 7 Day Total Orders (#), 7 Day Conversion Rate, Cost Per Click (CPC).
- **SB search term report** and **STIS** sheets in the Raw Pull Pack (Data Architecture S12), with current pull date.
- **BULK-US bulk pull** (current week): State, Daily Budget $, Bid / AG Default $; Sponsored Products Campaigns sheet for staging (Entity, Operation, State, Targeting Type, Bidding Strategy, Daily Budget, Keyword Text, Match Type incl. negativeExact / negativePhrase).
- Raw Pull Pack (#39 instrument), Monday 06:00.

**Command Workbook**
- **T0**: zone C named cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC.
- **T1**: family rows; Cap Status (BREACH); S3 spend-governance columns; MT Cov Phrase %; T1 finding IDs.
- **T2**: K8 # Exact / # Phrase / # Broad / # Auto; Validation State; K9 verdict; Event Mode; Syntax Tags; G1 quarantine flag.
- **T3**: Type (SP-P), Objective Tag, State, Daily Budget $, Bid / AG Default $, WAS %, Harvest Yield, Negation State (wall list), owner, notes (stem map).
- **T6**: Decision Log (predictions, review dates, V5 scores; gate table attachments).
- **T7**: Manifest rows A2, A5, A6, B5, B8, D1, D7; search-term feed pull date.

**Other**
- M5 queue (dated releases); family discovery allocation from instrument layer.
- #30 GRADUATE FROM DISCOVERY record.
- #32 event plan (armed-window dates).
- Account Rollup **A1** declared family term owners (S-F3).
- KDR Template v3.0 "Bands and Verdicts Reference" (budget-state bands, verdict strings).
- MKL (classification for off-taxonomy terms, F8 response).
- Family broad baseline yield (from SOP-14 read, on paired T3 row).
- PPC Economics Worked-Example Set v1.0 cases E1, E2 (ramp).

## 7. Outputs / Artifacts

| Artifact | Storage | Retention | Consumer |
|---|---|---|---|
| Stem map (`stem | terms | clicks | orders | status | route | date`) | T3 notes on phrase campaign row, product Command Workbook | With workbook; superseded maps in row history | Next weekly pass; #30; #29 |
| Pilot gate tables (day-14 health, day-28 decision with both yield reads) | T6 attachment on gate rows | Append-only with T6 | PPC Lead; SOP-06 |
| Staged bulk change sets (creations, negatives, budget deltas) | #38 staging, #38 format, reason strings with verdict + scenario ID | Per #38 incl. T+1 report | Data Operations / #38 |
| T6 rows with predictions and review dates | T6 Decision Log, append-only | Per #39 fold-in (pending) | SOP-06 V5; A3 verification scoreboard |
| Wall lists (pre-load, dedup, steering) | T3 Negation State column | With campaign row; closes at P8 step 4 | #29 wall audit |
| Updated Ledger row #13 | Section 14 five-column form | Pasted into PPC_Cross_Reference_Ledger | Next build session |

**Deterministic functions:** (1) stem signature = lowercase, de-pluralized, token-sorted; (2) yield = validated terms routed / spend x 100; (3) wall-breach set = served-terms(phrase) intersect served-terms(broad) on Customer Search Term; (4) P2 gate rule over paired T3 rows.

**Alarm routing:** F2/F9 same day to operator queue with PPC Lead copied; F3/F4/F5/F8 weekly worklist; F1 blocks at staging QA; F6/F7 to PPC Lead with T6 history.

### Failure modes

| ID | Failure | Detection | Response | Incident |
|---|---|---|---|---|
| F1 | Pilot without dated stop | Standup missing window dates or prediction | No deploy; 50-click test discipline (Doctrine S13) applies to every dated phrase test | None on file |
| F2 | Phrase-broad double-buying | P5 join non-empty | Wall same day; reads confounded; structure waste; root cause | F8 GRADUATED-UNSTEERED is the account's named leak pattern; P5 is phrase-side twin |
| F3 | Phrase on unproven root | Root # Exact = 0 or Validation State unclean | Pause; root to broad discovery (SOP-14) | None |
| F4 | Term-by-term graduation noise | Multiple single-term candidates from one stem | P4 stem routing | None |
| F5 | Pilot judged on ACOS not yield | Kill rec citing ACOS while yield >= baseline with clean walls | Yield and walls first; ACOS via O6 | Blended-number habit (Criteria System S1) |
| F6 | Head term in phrase with no exact | Oversight string served with # Exact = 0 | S-R12; SOP-12; P9; exclude clicks | 6-piece head term carried by auto with 0 exacts, June 30 review (S16 Worked Pass 3) |
| F7 | Family straddle | Seeds tagged to 2 families (T2 Syntax Tags vs T3) | Split same session | Cooling-terms-inside-satin-tracker class |
| F8 | Negation cadence lapse | WAS % above Discovery limit 2 consecutive passes | Reactive pass; off-taxonomy -> MKL classification first, taxonomy expands or negate (S-H6) | Satin product taking clicks on cooling terms it cannot rank |
| F9 | Structure change inside armed window | T6 entry in G12 window w/o plan reference | Revert; escalate per #32; exclusions extend; day-count correction logged | None; mirrors SOP-12 F8 |

Escalation: same failure twice consecutive cycles same scope -> PPC Lead with T6 history; F2 recurrences also via #29 wall audit.

## 8. Decision Rights

- **Human-mandatory:** pilot standup, both pilot gates, stem graduations (via #30 confirm), P8 archives, every deployment confirm.
- Authority Matrix v2.0: "Structure creation (all SOPs)" — PPC Lead decides; incoming operator and PPC Manager execute. "Weekly verdicts (established US)" — PPC Lead decides; operator executes assigned scope; BM owner reviews at daily huddle (review, not veto).
- Vacancy rule 5: unfilled D -> PPC Lead; E -> PPC Manager.
- Graduation decision: #30. Exact standup: SOP-12. Budget/cap decision: instrument layer. Event plan: deals owner + PPC Lead.
- Cap breach with no staged delta: reported to PPC Lead same day.
- Ramp: Week 1 reproduce Economics Worked-Example Set E1 and E2 cold; shadow P3-P5 and produce matching stem map; name the four dedup wall placements of P1 from memory. Week 2 run pass under review (STR to spec, P5 join, one negation set and one seed addition staged, one graduation walked). Week 4 own the pass for assigned families, run one pilot gate read, zero F2 findings attributable to own sessions. Six live-defense questions.

## 9. Account-Specific Facts

- **Bamboo 4pc product-wide $0 phrase** — live one-cell finding (Data Architecture v1.0 S11, A4 Structure targets); the account's one named structural gap at match-type layer.
- **Account reference Expected CPC $2.80** (T7 A6 PARTIAL; per-term values not yet landed).
- **T7 D1 PARTIAL** (blended margin) -> G9 PROVISIONAL on ceiling actions until **#41 lands (due 2026-08-21)**.
- June 30 review: 6-piece head term carried by auto with 0 exacts (Criteria System S16 Worked Pass 3).
- Satin product taking clicks on cooling terms it cannot rank (F11 pre-load failure); cooling demand owned elsewhere per #33 declaration.
- Worked examples (illustrative):
  - **WE-1 (Bamboo):** broad baseline yield 1.27 validated terms/$100; seeds "bamboo sheets" + stems "deep pocket", "split king", "cooling". Funding: $11/day out of broad ($25 -> $14/day), $7/day from unspent allocation, pilot $18/day; family discovery $25/day spent -> $32/day within unchanged allocation. Prediction >= 1.5/$100 by day 28. Day 14: $247 of $252 (98.0%). Day 28: $498 of $504 (98.8%), 259 clicks, CPC $1.92, 13 orders, CVR 5.0%, 78 served terms; "split king" (3 terms) graduates; "deep pocket" (4 terms) LEAVE TO HARVEST; "rv" (3 terms, 8 clicks, 0 orders) negated; 7 validated; yield 1.41 (+11%). SCALE; V5 PARTIAL.
  - **WE-2 (Satin):** week 3 mid-window seed "deep pocket" without wall; "satin sheets queen deep pocket" phrase 42 clicks $2.05 = $86.10, 1 order; broad 31 clicks $1.71 = $53.01, 1 order; total 73 clicks $139.11, blended CPC $1.91 -> structure waste; recomputed yield 5 on $460 = 1.09 vs 1.27 -> HOLD (wall artifact, not demand verdict).
  - **WE-3:** head root "bamboo sheets" served in phrase, 66 clicks in 14 days (4.7/day), 19% of campaign clicks, # Exact = 0 -> S-R12 ADD EXACT + RESTRUCTURE; clicks excluded from yield.

## 10. Open Items

| ID | Item |
|---|---|
| AM-1 | Verdict vocabulary reconciliation: Criteria System S13.1 = 18 actions; KDR v3.0 and SOP-12 v2.0 S5 = 25 (PPC-DR-04) |
| AM-2 | Section-citation map: corpus cites v4.0 S4.2 (naming) and S4.4 (bidding strategy); uploaded Criteria System contains neither; S17.2 keeps naming authoritative in v1.0 (outside pack) |
| AM-3 | Pilot decision-rule tolerance: "above baseline at comparable CPC" has no numeric tolerance |
| AM-4 | Stem-level evidence pooling: G2 pools twin sets explicitly; stem pooling unstated |
| AM-5 | Dedicated-coverage volume bar for seeding a stem as its own phrase row (P1 step 6, P4 branch 1) |

- **Rulings/conflicts:** PPC-DR-02 (v3.0 operating as v4.0); PPC-DR-04 (provisional, vocabulary); Ledger C3 (#31 no SOP); Ledger C5 (interface contracts built from Ledger Interfaces column plus Data Architecture).
- **Version note:** This SOP cites Criteria System v3.0 as authority; SOP-06/SOP-12 v2.1 cite v4.0 directly. Pilot standing state pending day-28 gate. T6 retention pending #39 fold-in.
- **Named but not in pack:** v1.0 Criteria System (naming convention authority); Criteria System S4.2/S4.4.
- Review triggers: Criteria System increment; PPC-DR-04 ratification; any SOP-14 P3 change; pilot day-28 gate (SCALE converts P2 to standing); D1 margin landing (#41); any session returning Ledger row #13.
- Ledger row #13 returned in Section 14 (owns exclusively: P1, P2, P4, P1 step 8/P5, P6, P7, P8, P9, Surface-2 coverage).
