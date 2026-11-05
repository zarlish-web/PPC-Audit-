# SOP-29 Digest: Negation Architecture Operations

Source: `PPC_SOP_29_Negation_Architecture_v2_0.pdf` (18 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-29: Negation Architecture Operations (Operating SOP, Component #29 of the PPC Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-07 |
| Owner | PPC Lead |
| Supersedes | SOP-29 v1.0 (2026-07-24) in full |
| Thresholds | Criteria System v4.0 only; zero local thresholds |
| Size | 12 procedures (v1.0: 7), 12 failure modes (v1.0: 5), 5 worked examples (v1.0: 2), Section 5 mapping expanded from 4-row local table to full 25-verdict closed vocabulary, Elements 11 and 12 added, 13 v4.1 amendment items |

**Verdict / purpose.** **Negation is traffic routing, not cleanup.** Negative lists are the fences that make the control gradient real; each is versioned structure carrying an evidence line, not maintenance debris. A campaign's negative list is part of its structure and is versioned with it (Strategic Doctrine v1.0 Section 11). Governs: the three negation states, wall-level selection, pre-load standard at every structure event, steering walls closing the graduation chain, reactive execution standards on the weekly routes, negative-ASIN standards, shared-list management, sibling and brand walls, monthly wall audit, removal control, negation-state reconciliation, event and recovery overlays.

**The one governing sentence:** every negative carries **five things**: (1) a declared state (pre-load, reactive or steering, per v4.0 Section 9 rule **L5**), (2) a wall level (negative exact, negative phrase or negative ASIN), (3) an evidence line or event reference, (4) a named owner, (5) a verification line proving it landed in the list it was staged against. Missing any = **structure debt**. A negative nobody can explain is itself a finding.

### 1.1 The three negation states (v4.0 Section 9 rule L5; per-term field at Section 3 family F11). Not severity levels, not a sequence

| State | What fires it | When placed | Evidence carried | v4.0 reference |
|---|---|---|---|---|
| PRE-LOAD | Taxonomy-known irrelevance: MKL already knows class is wrong (wrong material, size class, intent) | In creation session, before campaign serves an impression | Event reference, not performance: creating SOP, creation date, taxonomy class fenced | L5 pre-loaded mode; Section 8.9 **S-H2** "pre-load negatives from the taxonomy at launch so irrelevant syntaxes never spend" |
| REACTIVE | Proven waste on served evidence: **WAS%** breach vs objective limit, or spend without sales on a term the relevance check already failed | Staged Monday in weekly pass, deployed Tuesday per #38 | Full performance line: clicks, orders, window dates, source campaign, CPC, spend, relevance-check result | L5 reactive mode; F11 (WAS% limits); S-H2, **S-H7** |
| STEERING | Control-level change that must not double-buy: graduation, sibling ownership declaration, brand-defense assignment, phrase-to-broad dedup | Same day the control change lands; mechanical at graduation | Event reference + full source list (every campaign that served the term) | L5 steering mode; family **F8** (steering-negation state); **S-H1**, **S-H4** |

State written per term on T2 campaign child rows, column **Negation State on Term (child)**; rolled to campaign in **T3 group C5 Negation State (pre/reactive/steering)**. Values: the three states plus **none**. A term whose exact instance is live while sources read none = **GRADUATED-UNSTEERED** (F8) - the most expensive readable state this SOP owns (source buys at uncontrolled CPC while exact fights it with our own money).

### 1.2 The three wall levels

| Wall level | Fences | Correct use | Misapplication failure |
|---|---|---|---|
| Negative exact | Exactly one served term and close variants; one term, one wall point | Every steering wall; every Route B reactive term; every graduated exact held out of its sources | Under-fencing: drift family of 40 needs 40 points; operator places 3, other 37 spend |
| Negative phrase | Every current and future term containing the root, in order; one wall point, unbounded futures | Route C drift clusters; sibling-owned roots; brand roots held out of generic discovery; stem wall at stem graduation | Over-fencing: root chosen by string prefix rather than taxonomy fences owned terms (F5, WE-3) |
| Negative ASIN | One product detail page on product-targeting surface only: auto substitutes, auto complements, PAT | Own-catalog pages out of complements (self-cannibalization wall); failed conquest targets out of substitutes | Applied to auto close/loose = no-op that reads as coverage (those serve queries, not pages) |

### 1.3 What a wall is not
- Not a bid lever: v4.0 rule **L1** places negation **fourth**, after budget, bid, placement.
- Not a cleanup pass: placed at named events on named evidence, never swept.
- Not a relevance judgment at execution time: relevance decided upstream in MKL; F11: relevance check always precedes the negative; relevant non-converter routes to the fix queue.
- Not reversible without a case: removal through P10 with named case class and evidence.

## 2. Scope and boundaries (Section 1.4, against Cross-Reference Ledger v1.7 row 29)

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Every threshold, band, gate, scenario, lever, verdict incl. three L5 modes, WAS% limits, reactive rules. SOP sets execution standards, never a number |
| #30 Harvest and graduation | Decides which terms graduate, assembles source list. This SOP owns the wall half of the atomic chain and returns verification line to #30's chain record. Change to either half increments both |
| #14 Broad operations | Owns weekly three-route search-term triage generating reactive candidates. This SOP owns standards; never re-runs triage |
| #13 Phrase operations | Owns phrase-broad dedup wall build/audit and phrase-side graduation handoff (Ledger row 13). This SOP supplies wall standard |
| #15 Auto operations, D5 split | Owns four-group structure; detects and routes candidates at P1.5 and P3 Routes B-D. This SOP owns prescribed pre-load sets applied same session (Ledger row 15) |
| #12 Exact campaign operations | Owns exact standups. This SOP prescribes walls SOP-12 builds at every P1, P2, P5, P7 structure event, same session, recorded in T3 |
| #16 PAT and conquest | Decides target opens, rotations, exits; declares failed-target list. This SOP places negative ASINs; never decides a target failed |
| #33 Sibling arbitration | Candidacy detection, composite, ownership declaration. This SOP builds/moves walls same day, protects non-owner's defense posture |
| #38 Bulk-file deployment | Staging, pull, transcription, validation, upload, T+1, rollback. This SOP owns what/where; #38 owns proof it landed |
| #37 Automation rules | Rule register and change control. Negation never routes through a rule without #37 register entry |
| #32 Deal and event window | Event plan and named actions. This SOP freezes non-plan wall changes inside armed window (P12) |
| #31 Budget and envelope | COMPLETE by absorption; no procedural doc (Ledger conflict **C3**). Names T0 zone H and Account Rollup A2, never a #31 procedure |

## 3. Triggers (Section 2)

Lag measured from the artifact's timestamp. A trigger firing without its procedure starting inside the lag is a failure mode.

| Trigger | Detecting artifact | Max lag | Procedure | Evidence it fired |
|---|---|---|---|---|
| Structure event | Staged creation block in #38 change set from SOP-12 P1/P2, SOP-13 P1, SOP-14 P1 or SOP-15 P2, carrying pre-load set as a unit per #38 P1 step 3 | Same session; pre-load never deploys later than the campaign | P2 via P1 tree | T3 row shows populated list attachment and non-empty negation-state field |
| Graduation approval | SOP-30 P1 graduation log row reading **APPROVE** with full source list per SOP-30 P1.1 | Same day, walls placed and verification line returned | P3 | Each source's list shows entry; line written into #30 chain record |
| Weekly reactive routes | SOP-14 P3 Route B and Route C output with evidence lines in Monday cascade at T2 | Staged Monday, deployed Tuesday. **Two consecutive passes at zero negatives with spend active = F12** | P4 | One row per Route B term and per Route C cluster root, complete reason string |
| ASIN route | SOP-15 P3.3 substitutes handoff; #16 failed-target declaration; own-catalog appearances in served-ASIN feed for complements and loose | Same pass as detection | P5 | ASIN entries present; own-catalog scan returns zero own ASINs serving |
| Shared-list edit | Version increment on any named shared list, or F4 divergence alarm | Same day re-attach; divergence source named before session closes | P6 | Version log shows addition with evidence; all attached campaigns read same version |
| Sibling declaration | SOP-33 P4 declaration record, P6 re-arbitration changing owner, or P6.3 stewardship grant | Same day declaration date carries; disagreement = F8 here, F3 at #33 | P7 | Non-owner's discovery campaigns show negative phrase on owned root; owner's carry nothing |
| Brand assignment | Brand-defense plan change from SOP-14 P4 structure, or new brand entering catalog | Same session as defense structure change | P8 | Zero brand-term appearances in every generic discovery campaign's served terms at next pull |
| Monthly audit | Calendar slot registered against component #4 (AM-4: slot ungoverned) | Completes inside the month; findings stage day found | P9 | Artifact with points-checked count; zero-breach months recorded |
| Removal request | Any proposal to delete a negative incl. from an automation rule | No removal deploys in session proposed | P10 | Removal log: case class, evidence, confirming role |
| Registry reconciliation | T2 campaign child rows and T3 group C5 vs served-term feed at each weekly pull | Same pass; GRADUATED-UNSTEERED closes in cycle found (S-H4) | P11 | Zero rows exact-live with source state none |
| Event window arms | #32 event plan entering T2 with dates, arming event gate | Same day window arms | P12 | Armed-window record lists live and frozen wall classes |
| Recovery mode entry | Product entering Recovery Mode per S-A4 and Section 11 rules R1-R6 | Pass on recovery cadence from day of entry | P12 | Recovery triage record names negation pass among completed steps |

## 4. Preconditions and gates (Section 3)

A stale or missing field group **suppresses** its dependent wall class (not degrades). No wall against a list not provably current. Pass records what it could not see and continues.

### 4.1 Input preconditions
| Manifest field group | Requirement | Observable |
|---|---|---|
| B5 Coverage counts | Registry counts per match type current in **T2 block 8**; feed: campaign registry, weekly | T7 B5 PRESENT; T2 **#Exact / #Phrase / #Broad / #Auto** reconcile to T3 campaign count |
| Search-term feed | Served-term rows for every campaign with per-campaign split; absence suppresses P4 for affected campaigns | T2 child rows carry non-null **Spend Share of KW %** (computes only when join landed) |
| Served-ASIN feed | Product-target served rows for substitutes and complements, else P5 suppresses; post-D5 evidence carries group token, never blended | T3 row for each auto group shows populated **Auto Group Split (D5)** link; child rows carry group tokens |
| Graduated-term list | From registry, current to last completed harvest pass (P9 population, P3 wall list) | Graduation log last row date inside current cycle; count matches trailing registry delta |
| Brand-term list | Current per brand across **all five brands**, incl. variants and misspellings | List version date inside current month; P8 zero-appearance check clean |
| S-series declarations | SOP-33 declaration register current, each with date and named re-arbitration triggers | Every root in 2+ siblings' campaigns has a declaration row or open S-series finding inside deadline |
| Own-catalog ASIN list | Complete across **both entities and all five brands**, incl. child variations | List count equals catalog count in **Economics and Context Pack** for current month |
| Failed-target list | Declared by #16 per exit decisions; never inferred from CPA | Each entry carries #16 exit verdict reference and declaration date |
| T3 list attachments | Each campaign's shared lists named and versioned in T3 row | Every campaign sharing a discovery role reads same list name and version string |

### 4.2 Gates in force (v4.0 Section 5 numbering; corpus alias given; conflict C9 / AM-11)
| Gate | What it blocks here | Observable |
|---|---|---|
| G8 Packet completeness (governing gate) | Wall class whose input list is missing is suppressed and stated. **DEGRADED at under 85%** gate-relevant fields, flags only | T7 completeness on pass header; every suppressed class named |
| G12 MKL hygiene (corpus calls the event freeze G12) | Pre-load in full. Every term in current MKL with syntax tag and relevancy score; untagged/irrelevant route to MKL maintenance and taxonomy pre-negation. v4.0: refresh **bi-weekly**, manifest degrades **past 30 days stale** | MKL version date inside 30 days; pre-load resolves to tagged taxonomy classes |
| G10 Event exclusion (corpus number G12) | Non-plan wall changes inside armed window; event-week rates as reactive evidence. Excludes event weeks and **14 days following** | Armed-window record in T2 with dates; zero non-plan wall rows dated inside |
| G2 Sample sufficiency | Reactive negative below thresholds: **15+ clicks in 7 days** bid reads, **100+** CVR verdicts, **1,000+ impressions** CTR verdicts. Below = test continuation. **Twin sets pool evidence** | Every Route B evidence line shows click count at/above applicable threshold |
| G1 Validation quarantine | Any wall on a quarantined row (flag, no recommendation, data-refresh task same day) | Zero staged negation rows on a term with T2 zero-quarantine flag |
| G11 Sibling conflict | Sibling wall placement while contested root undeclared | Every root with 2+ sibling appearances has declaration row or open finding with #33 P2 guards |
| G3 Budget truncation | Named so not misapplied: truncated campaign's WAS% describes worst hours; L1 puts budget before negation | T3 **Truncation Flag (G3)** clear on every campaign whose WAS% is read as reactive evidence |
| G9 Price stability (corpus G9 = margin-table freshness; both named) | Reactive reasoning on conversion economics while price change inside **7 days** or margin table provisional | Reason string carries provisional tag where either holds |

## 5. Procedures (Section 4)

Time estimates: one operator, one product of roughly **280 tracked terms**, feeds landed. Every staged row in **#38 P1 format**, one row per change; reason string pattern: **`[SOP-29][verdict][state and wall level][evidence reference]`**.

### P1. Select the wall level (3 min per decision; runs inside every procedure placing a negative)
Decision tree:
1. Target is a product detail page? -> **negative ASIN**, go to P5; only in auto substitutes, auto complements, PAT (close/loose = no-op).
2. One specific served term, no expected unenumerated siblings? -> **negative exact**. **Every steering wall is negative exact, without exception** (phrase-walling a graduated term fences the modifier space the source should keep discovering).
3. Root exists that (a) appears in every cluster member, (b) appears in no term this product or any sibling owns, and (c) survives the reverse test? -> **negative phrase** on root. Else negative exact on each member and log cluster as **unbounded** for re-test next pass.
4. **Reverse test (mandatory before any negative phrase):** query trailing window's served terms for the root across every campaign the wall will touch; count terms containing it; subtract cluster members. Remainder > 0 -> root wrong, return to step 3 with longer root. Remainder goes in reason string whether zero or not.

Steps:
1. Read candidate from source (graduation record, Route B term, Route C cluster, declaration, brand list entry).
2. Walk tree; record branch and reverse-test remainder in reason string.
3. For negative phrase record **fenced member count** (so P9 can compute what one wall point holds).
4. Disagreement on root: **longer root wins** (over-fencing costs earning contribution, larger and harder to detect).

### P2. Pre-load standard at every structure event (12-20 min per campaign created)
Executes in creation session, staged in creating SOP's settings block per #38 P1 step 3. Creation without pre-load = F1 here and in creating SOP. Sets prescribed here, applied by creating SOP (Ledger boundary rows 12-15).

| Campaign created | Prescribed pre-load set | Why |
|---|---|---|
| Family broad / Family phrase | Every graduated exact in family: negative exact, one point each. All brand terms across both entities: negative exact on enumerated terms + negative phrase on each brand root. Sibling-owned roots per current declarations: negative phrase. Known-irrelevant taxonomy classes: negative phrase on each class root | Discovery surfaces are entry for every drift class; fence before it serves |
| Auto close / Auto loose | Same keyword-side set as family broad. Own-catalog ASINs **not** negated here | Close/loose serve queries; own-ASIN negative fences nothing, false coverage |
| Auto substitutes | Failed-PAT-target ASINs from #16 list: negative ASIN. Own-catalog ASINs: negative ASIN. No keyword pre-load beyond brand set | Substitutes is conquest signal source (F11); stops re-proposing exited targets |
| Auto complements | Own-catalog ASINs incl. child variations: negative ASIN. Failed-target ASINs: negative ASIN | Self-cannibalization wall; only pre-load with no keyword analogue |
| Exact campaigns | No keyword pre-load. Brand campaigns exclude competitor-brand terms only where defense plan names them | Exact cannot drift |
| PAT campaigns | Own-catalog ASINs: negative ASIN. Failed-target ASINs from prior rotations on same target list | Conquest on own pages = same money both sides |

1. Open creating SOP's staged creation block; read campaign type and syntax family from name segments.
2. Pull current lists (graduated terms for family, brand terms, sibling-owned roots, own-catalog ASINs, #16 failed-target list where type calls). Check version dates; stale list suppresses its own line; suppression written to pass artifact header naming its T7 MANIFEST row.
3. Resolve known-irrelevant taxonomy classes from MKL, not recall (G12).
4. Walk P1 per entry: graduated and brand terms -> negative exact; brand roots, sibling roots, taxonomy classes -> negative phrase; ASIN entries -> negative ASIN.
5. Stage every entry as own row in creation block (partial pre-load shows as row-count delta).
6. Write list attachment into new campaign's T3 row; set negation-state field to pre-load. Empty attachment field = F1 detection.
7. Record pre-load row count vs prescribed count for type; must match or difference named before creation deploys.

### P3. Steering walls at graduation (6-10 min per graduated term). Coupled half of SOP-30 P3 atomic chain
1. Receive term and full source list from SOP-30 P1.1 queue row: every campaign that served term in evidence window (term validated in broad and served by auto close = one graduation with walls in both).
2. Verify list vs served-term feed: query term across every campaign on product and declared siblings; campaign in feed but absent from list is added; discrepancy returns to #30 as queue-assembly finding.
3. Place negative exact in each source (typically family broad, family phrase, auto close, auto loose, sibling discovery carrying root per declaration).
4. Check ad group structure: campaign with **2+ ad groups** takes negative at level covering all of them (keyword-level negative on multi-group campaign leaves others serving = **list-scope error class**, passes naive list check).
5. Stem graduations (SOP-30 P4): negative phrase on stem in phrase source (fencing every member) + negative exact in broad. Members not walled individually.
6. Stage all wall rows in one change set with graduation record reference in every reason string.
7. Verify same day: each source list shows entry at step-4 level; write verification line into #30 chain record (pass incomplete without it).
8. Verify again at next pull: term absent from all sources' served terms (list entry + term still serving = breach).

### P4. Reactive execution standards on weekly routes (25-40 min per product per pass)
SOP-14 P3 sorts window's served terms into three routes; Routes B and C handed here. SOP does not re-run triage.
1. **Route B, proven waste:** one negative exact per term. Mandatory evidence line: clicks, orders, window dates, source campaign, CPC, spend, relevance-check result. Row without one returns to #14 (not completed from feed).
2. **Route C, drift clusters:** one negative phrase per cluster root via P1 tree with reverse test and remainder. Evidence: root, member count, combined clicks and spend.
3. **Converting-term guard:** never negate a term that converted in-window without a diagnosis note; in-window conversion overrides click rule pending read (F11 owns rule). Staged negative with in-window orders is held, not deployed (F3).
4. **Truncation check:** read T3 Truncation Flag (G3) before reading WAS% breach as negation case; truncated -> budget lever first, re-read next clean cycle.
5. **Sufficiency:** click count vs G2 thresholds for the judgment; below -> term stays in source under capped, dated test.
6. Stage every row in #38 P1 format with SOP pattern reason strings; deploy Tuesday.
7. Pass arithmetic: terms fenced, clusters fenced, member count per cluster, window spend removed, resulting WAS% per campaign (counts without dollars cannot be scored).
8. Write to **T6 DECISION LOG**: **Level, Target, Rule / Scenario Fired, Change (prior -> new), Expected Outcome Window, Review Date**. Prediction as WAS% figure with date, never as direction.

### P5. Negative-ASIN standards (10-15 min per product per pass)
1. Own-catalog appearances: scan served-ASIN feed for complements and loose each pass; any own ASIN stages as negative ASIN in that campaign same pass. Include child variations.
2. Failed conquest targets: place what #16 declares, when declared, into auto substitutes and PAT campaigns on same target list. Never infer failure from CPA (Ledger row 16).
3. Group discipline: negative ASINs in substitutes, complements, PAT only. Read group from T3 **Auto Group Split (D5)**. Wrong group = inert.
4. Evidence: own-catalog wall reason string = ASIN, parent, clicks and spend drawn in window, catalog-list version. Failed target = #16 exit verdict reference and declaration date.
5. Own-catalog walls are permanent structure, not re-litigated. Failed-target wall removable only through P10 on #16 re-entry declaration.

### P6. Shared negative-list management (8-12 min per pass; +20 min per new list)
1. Sharing by rule: structures share a list where they share a discovery role: **trawler and probe pair** at standup (SOP-15 P4), and **family broad + family phrase** pair (share graduated, brand, sibling sets). Doctrine Section 11.
2. Naming and versioning: name identifies family and role; version string increments on every addition or removal; additions log with evidence lines.
3. One edit, everywhere. Editing a campaign's own list for something the shared list should carry = divergence source (F4).
4. Attachment is structure: lives in T3 row, read at every creation and audit (rebuild can drop an attachment silently).
5. Divergence check each pass: compare entry counts and version strings of every role-sharing pair; mismatch names diverged campaign, divergence count, bypassing direct edits. Tolerance ungoverned (AM-7).

### P7. Sibling and family walls (10 min per declaration, same day)
1. Open SOP-33 declaration register row for root (owner, declaration date, composite table, re-arbitration triggers). Non-owner's discovery campaigns get **negative phrase on owned root**; owner's carry nothing.
2. Protect non-owner defense posture: ownership is of the **root, not the modifier space naming the sibling**. Non-owner holds exact defense at floor on its own model-specific variants (root + size, count or model terms). Over-walling = F9 here, F4 at #33. Run reverse test against non-owner's own exact list as well as served terms.
3. Re-arbitration changing owner: walls move same day. Old owner's discovery gains the wall; new owner's loses it via P10 (declaration as evidence). Both in one change set.
4. Temporary stewardship grant (SOP-33 P6.3): wall moves with stewardship, carries **reversion date** in reason string (missing = F10).
5. Twin sets carry shared negatives (v4.0 Section 8.11 **S-B4**, Section 9 rule **L6**): one managed term, one bid posture, shared negatives; diverging twin lists = one finding.

### P8. Brand-term walls (15 min per brand per month)
1. Brand terms live in defense only. Every generic discovery campaign across the family carries brand set: negative exact on enumerated brand terms + negative phrase on each brand root (variants, misspellings).
2. **Five brands walled across both entities**, not per entity.
3. Defensive brand-broad campaign (SOP-14 P4) is the one structure holding brand terms; carries competitor-brand negatives only where defense plan names them (plan is #14's and #17-19's).
4. Competitor brands in brand campaign's served terms = conquest context, route to #16; not negated on sight.
5. Proof: **zero brand-term appearances** in served terms of every generic discovery campaign at the pull.

### P9. Monthly wall audit (90-140 min per product). Runs on calendar slot registered against #4 (AM-4)
1. Population: every term graduated in **trailing quarter** with full source list. Sampling floor ungoverned (AM-3), so runs **full population**, not a sample.
2. Two sides per wall point: side one, list shows entry at P3 step 4 level; side two, source's served terms do not contain term. Either failure = breach.
3. Brand check: zero brand terms in generic discovery served terms.
4. Own-ASIN check: zero own-catalog ASINs in complements' or loose's served rows; appearance stages negative ASIN same day with window spend in finding.
5. Sibling check: wall state matches declaration date; compute **lag in days** for mismatch.
6. Shared-list check: every role-sharing pair reads same version.
7. **Breach rate = breaches / wall points checked**, recorded even if zero, with T7 MANIFEST completeness score.
8. Attribute every breach to the creation or graduation session that should have placed the wall.
9. Stage all fixes same day. Artifact: points-checked count, breach list with session attribution, fixes staged, named root causes.

### P10. Removal control (15 min per removal; never same-session)
Exactly four case classes:
| Case | Trigger | Evidence |
|---|---|---|
| 1 Sibling re-arbitration | Declaration changed; outgoing non-owner's wall comes down | New declaration record with both composites |
| 2 Brand-strategy change | Brand term moves scope, or competitor-brand negative lifted | Plan revision |
| 3 Erroneous negation with evidence | Wall fenced something unintended | Served-term or contribution collapse (WE-3) |
| 4 #16 target re-entry | Failed target re-declared as candidate | #16 re-entry declaration |

A failed graduate is **not** a removal case (SOP-30 P6: diagnosis; source walls stay).
1. No removal deploys in session proposed; case class named and evidence attached first.
2. Removals log like additions: entity, wall level, case class, evidence, confirming role, date.
3. Removal human-mandatory in every case.
4. Unexplained removal found in audit: reinstated pending review; escalates on first occurrence (clock ungoverned, AM-8).

### P11. Negation-state reconciliation (20-30 min per product per pass)
1. Open **T2 KEYWORD COMMAND**, apply **OVERSIGHT** filter view, expand campaign child rows; read **Negation State on Term (child)** beside **Spend Share of KW % (child)**.
2. Unsteered-graduate scan: rows where exact instance live and a source campaign's state reads none = GRADUATED-UNSTEERED (F8, **S-H4**); close leak same cycle; reclassify source's spend on term as **structure waste** in audit. Data Architecture v1.0 Section 6.1 labels this filter **S-H6** (conflict **C12**; correct is S-H4).
3. Auto-dominance cross-check: priority term with auto or broad carrying **more than 40% of its clicks** (v4.0 Section 4 rule **X10**) = structure failure; route to #12 as **ADD EXACT + RESTRUCTURE**; SOP contributes steering wall once exact stands up.
4. Reconcile vs **T3 CAMPAIGN BOARD group C5 Negation State (pre/reactive/steering)**: campaign clean at C5 while any child reads none = rollup defect.
5. Record counts: rows scanned, unsteered found, closed this cycle, carried with named reason.

### P12. Event-window and recovery overlays (10 min to arm; 5 min per pass while armed)
1. Arming: when #32 plan enters T2 with dates, classify every wall class as frozen or live; record in armed-window record.
2. **Live** in window: steering walls at graduation; own-catalog negative ASINs; any wall the event plan names.
3. **Frozen** in window: reactive negation from weekly routes and Route C cluster walls (event-week evidence excluded by G10).
4. Post-window: frozen queue re-reads vs post-window evidence (not deployed as staged); **14-day exclusion** after window applies.
5. Recovery Mode (S-A4; Section 11 R1-R6): negation pass on recovery cadence, named step in recovery triage record; v4.0 rule **R3** tightens human-review tiers.
6. Mode precedence (Section 11 rule **T8**, Section 12 rule **P7**): Recovery > Event > stage defaults; freeze list follows that ordering.

## 6. Rules, thresholds and numbers

### 6.1 Numeric values
| Value | Meaning | Source |
|---|---|---|
| WAS% <=10% everywhere; <=40% Discovery | Reactive negation firing limits (F11). KDR Bands tab reads "Standard <10% · Discovery <40%" (boundary sense conflict, AM-12) | v4.0 F11; KDR |
| 10% / 10-15% / 15-20% | KDR product-type WAS sub-bands: non-subjective / semi-subjective / subjective (not in v4.0; AM-12) | KDR Bands tab |
| THIN under $6; STANDARD $6-15; RICH over $15 | v4.0 F1 margin-dollar class (vs undefined "price class", AM-2) | v4.0 F1 |
| 15+ clicks/7d; 100+ clicks; 1,000+ impressions | G2 bid read / CVR verdict / CTR verdict | G2 |
| 85% | G8 DEGRADED line | G8 |
| Bi-weekly; 30 days | MKL refresh cadence; manifest degrades past 30 days stale | G12 |
| 14 days | Post-event exclusion | G10 |
| 7 days | Price stability window | G9 |
| >40% of clicks | Auto/broad dominance on priority term = structure failure | v4.0 Section 4 rule X10 |
| 2+ ad groups | Negative must be placed at level covering all groups | P3 step 4 |
| 2 consecutive passes | Zero negatives with active spend = F12 | Section 2 |
| Five brands, both entities | Brand wall and own-catalog scope | P8, Section 3.1 |
| ~280 tracked terms | Planning basis per product | Section 4 |
| Trailing quarter | Audit population | P9 |
| 3 orders | Graduation bar cited in WE-2 (L6, S-H1) | WE-2 |

### 6.2 Formulas
| Formula | Definition |
|---|---|
| WAS% | Zero-order spend across all served terms / campaign spend (per WE-1, WE-5) |
| Reverse-test remainder | Count of trailing-window served terms containing root across all touched campaigns - cluster members |
| Breach rate | Breaches / wall points checked |
| Wall points (audit) | Sum over graduated terms of source count |
| Skipped-wall cost | Source spend - (source clicks x exact seeded bid) |
| Sibling lag | Days between declaration date and wall move |

### 6.3 v4.0 references
| ID | Meaning as described |
|---|---|
| L1 | Lever precedence: budget, bid, placement, then negation fourth |
| L5 | Three negation modes (pre-loaded, reactive, steering); names "spend-without-sales" without a figure |
| L6 | Graduation bar; twin sets one managed term, shared negatives |
| F1 | Margin-dollar class |
| F8 | Steering-negation state; GRADUATED-UNSTEERED leak |
| F11 | Per-term negation field; WAS% limits; relevance check precedes negative; relevant non-converter to fix queue; substitutes as conquest signal source; satin cooling incident |
| S-H1 | Graduation / steering |
| S-H2 | Pre-load from taxonomy at launch; negation pass fires on WAS% breach |
| S-H4 | Close GRADUATED-UNSTEERED leak same cycle |
| S-H7 | "Zero-sale spend above threshold on an irrelevant term" (no threshold; AM-1) |
| S-H1 to S-H8 | Section 8.9 scenario range (review trigger) |
| S-A4 | Recovery Mode / code red |
| S-B4 | Twin sets carry shared negatives (Section 8.11) |
| S-R12 | Resolved via ADD EXACT + RESTRUCTURE |
| X10 | Auto/broad >40% of clicks on priority term = structure failure |
| G1, G2, G3, G8, G9, G10, G11, G12 | See Section 4.2 |
| R1-R6 | Recovery Mode rules; R3 tightens human-review tiers |
| T8, P7 | Recovery > Event > stage defaults |
| V1, V5 | Scoring; rule-level accuracy |
| V4 | Monthly items list does not include this audit (AM-3, AM-4) |

## 7. Data inputs required

- **Search-term feed** (served terms per campaign with per-campaign split) from **SP and SB search term reports** and **STIS** in the **Raw Pull Pack**, Monday 06:00, workbook refresh complete 09:00 (I-12)
- **Served-ASIN feed** (product-target served rows for substitutes, complements, loose) with **D5 group tokens**
- **T2 KEYWORD COMMAND**: campaign child rows, **Negation State on Term (child)**, **Spend Share of KW % (child)**, OVERSIGHT filter view, zero-quarantine flag, armed-window record / Event dates; **block 8** registry counts **#Exact / #Phrase / #Broad / #Auto**
- **T3 CAMPAIGN BOARD**: group **C5** (Negation State (pre/reactive/steering), Duplicate / Self-Overlap, Harvest Yield, Graduations (Qtr), Auto Group Split (D5)); **C4 WAS %**; **C3 Truncation Flag (G3)**; list attachment names and versions per campaign; campaign count
- **T6 DECISION LOG** (Level, Target, Rule / Scenario Fired, Change (prior -> new), Expected Outcome Window, Review Date)
- **T7 MANIFEST** status per field group incl. **B5 Coverage counts**; completeness score
- **Campaign registry** / graduated-term list (from T2 block 8); **SOP-30 graduation log** (P1 rows with APPROVE and P1.1 source lists; chain record)
- **SOP-14 P3** Route B terms and Route C clusters with evidence lines
- **SOP-13** phrase-broad dedup wall requests; **SOP-15** P1.5 / P3 / P3.3 auto route detections
- **Brand-term list** per brand (five brands, both entities, variants, misspellings) with version date
- **SOP-33 S-series declaration register** (owner, date, composites, re-arbitration triggers, stewardship grants with reversion dates)
- **Own-catalog ASIN list** (both entities, five brands, child variations) and **Economics and Context Pack** catalog count
- **#16 failed-target list** with exit verdict references and declaration dates; #16 re-entry declarations
- **MKL** with syntax tags and relevancy scores (version date)
- **#32 event plan** with window dates and named actions; recovery triage record
- **#38** creation blocks, session records, **T+1 diff report**
- **Shared list objects** with version logs; **removal register**
- Defense plan (SOP-14 P4 / #17-19)

## 8. Outputs and artifacts (Section 8)

| Record | Storage | Retention | Consumer |
|---|---|---|---|
| Pre-load checklist per creation | T3 row: list attachment + Negation State field; staged rows in #38 creation block | Campaign's operating life plus governance period after archive | P9 baseline; F1 check in SOP-12/13/14/15; ramp week 1 |
| Wall verification line per graduation | SOP-30 chain record, mirrored into T6 as graduation's negation half | Trailing four quarters minimum | SOP-30 P3 step 3; P9; V5 |
| Reactive change set with evidence lines | #38 session record; deployed rows in T6; counts in pass artifact | With #38 session record | #38 P6 T+1 diff; V5; WAS% re-read |
| Versioned shared lists with add/remove logs | List object, named and versioned; attachment in T3 | Full version history, permanent | P6, P9, every creation |
| Negative-ASIN register | T3 group C5 with served-ASIN scan output attached | Permanent (own-catalog); campaign life (failed-target) | #16 rotation; P9; RE-POINT VARIATION re-check |
| Monthly wall audit artifact | Report: points checked, breach list with session attribution, fixes, root causes, breach rate | Rolling 12 months minimum | PPC Lead; SOP-30 F1 root-causing; Section 10 trigger; ramp week 4 |
| Removal log | Removal register: entity, wall level, case class, evidence, confirming role, date | Permanent | P9; escalation; #33 re-arbitration trail |
| Negation-state reconciliation counts | T2 child rows and T3 C5; counts in weekly pass artifact | Weekly, with workbook cycle history | P11; S-H4 close; skill alarm feed |
| Suppression record | Pass artifact header naming every suppressed wall class and T7 row | With pass artifact | T7 completeness; G8; next pass re-attempt list |
| v4.1 amendment register | Section 10.3 | Until v4.1 folds or declines | Threshold owner; CEO |

Gate artifacts: **weekly** = deployed negation change set with complete evidence line on every row and T+1 diff attached; **monthly** = wall audit report (even if empty); **graduation event** = verification line.

## 9. Verdict-to-wall mapping (Section 5)

KDR Template v3.0 tab "Bands & Verdicts Reference", 25 strings. v4.0 Section 13.1 carries an **eighteen-item** list; Data Architecture v1.0 Section 2 rule 8 and Ledger row 8 state **twenty-six** (conflict **C10**).

### 9.1 Ten verdicts producing a wall action
| Verdict | Execution |
|---|---|
| NEGATE (PRE-LOAD / REACTIVE / STEERING) (v4.0: "CUT / NEGATE") | Owned end to end: pre-load -> P2, reactive -> P4, steering -> P3 or P7; mode recorded per F11 |
| GRADUATE FROM DISCOVERY (v4.0: "GRADUATE + STEER") | P3 in full same day in every source, verification line to #30 |
| ADD EXACT + RESTRUCTURE | Steering half once #12 stands exact up: negative exact in every source, same day (resolves X10 auto-dominance and S-R12) |
| CONSOLIDATE DUPLICATES | Carry every negation list the paused instance held that survivor lacks, same change set (F11) |
| OPEN / ROTATE / EXIT CONQUEST | On EXIT only: target into #16 failed list; negative ASIN in substitutes and PAT (P5) |
| FUND TEST (UNFUNDED PRIMARY) | No wall on tested term; new campaign gets P2 pre-load |
| RANK PUSH: FUND SIZED PUSH | No wall on pushed term; dedicated campaign gets P2; post-graduation walls re-verified |
| RECOVERY PUSH | As sized push + pre-OOS wall set re-verified before push funds |
| RE-POINT VARIATION | No keyword wall; own-catalog negative-ASIN set re-checked vs new variation same day |
| PAUSED-PENDING (REASON + RE-ENTRY) | No wall unless paused term sits in campaign hosting phrase or broad ad groups that can still serve it |

### 9.2 Fifteen verdicts producing no wall
| Reason class | Verdicts | Operator does instead |
|---|---|---|
| A different lever owns it | UNLOCK TRAFFIC; FIX BUDGET (TRUNCATED); PLACEMENT FIX FIRST; BID DOWN TO PROFITABLE CPC; CAP SYNTAX; TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | L1 negation fourth. Truncated WAS% held per P4 step 4; traffic deficit caused by over-broad wall routes to P10 case 3, never bid lift |
| A wall would destroy the evidence or the demand | QUARANTINE: DATA REFRESH; CONTINUE TEST TO 50 CLICKS AT CAPPED BID; FIX CONVERSION FIRST; DEFER PUSH; INCREMENTALITY LADDER; STOP-LOSS: CONCEDE OR DEFER; LEAVE TO HARVEST | G1 blocks/pulls walls on quarantined rows. FIX CONVERSION FIRST = most common source of incorrect reactive negative (relevant non-converter to fix queue, F11). Wall in live incrementality measurement held until it closes. Conceded term not fenced (prevents deferred re-entry). LEAVE TO HARVEST = converting demand below graduation bar |
| Walls already stand, read at audit | TAPER: RANK ACHIEVED, STEP BIDS DOWN; HOLD; DEFEND LIGHTLY AT RANK; DEFEND AT FLOOR; ENTER SBV ARBITRAGE | Steering walls hold through taper (SOP-30 P6). Defended brand term: P8 confirms walled out of generic discovery. SBV pivot changes surface, not whether bought |

Campaign-level: T3 group **C6** subset vocabulary carries **NEGATION PASS** = routing instruction to run P4 on the named campaign, never a substitute for a term-level verdict.

## 10. Decision rights

**AI-executable with audit:** pre-load drafting from the four lists, wall drafting from #30 source lists, P1 tree walk incl. reverse test, reactive staging from delivered routes, evidence-line assembly, list version diffs, full monthly audit with two-sided breach detection and attribution, reconciliation scan, all pass arithmetic.

**Human-mandatory:** every P10 removal without exception; every sibling wall move and every stewardship wall; every F3 hold disposition; every reverse test returning non-zero remainder (F5 decision point); the deployment confirm itself (#38's checkpoint). Recovery Mode tightens these per v4.0 R3.

| Authority Matrix v2.0 row | Holders |
|---|---|
| Structure creation (all SOPs) | PPC Lead D or per SOP scope; incoming operator E; PPC Manager E; BM owner I |
| Weekly verdicts, established US | PPC Lead D; incoming operator E within scope; PPC Manager E; BM owner R at huddle |
| Sibling declarations, S-series | PPC Lead D; incoming operator E; Launch/CA operator I; BM owner R |
| D5 conversions and auto operations | PPC Lead R; incoming operator D and E |
| PAT and conquest opens and exits | PPC Lead R; incoming operator D and E |
| Bulk deployments, #38 | PPC Lead R; incoming operator E; PPC Manager E (upload action stays with #38 holder) |
| Event plans, #32 | PPC Lead D with deals owner; incoming operator E; PPC Manager E; BM owner R |
| Code-red declaration and close | PPC Lead D; incoming operator E; PPC Manager E |
| v4.0 threshold changes | CEO D; PPC Lead E and R; operator I |

Standing rules: one D per row per scope; E without D executes staged decisions only; BM owner R = daily huddle review, not veto; vacancy: D reverts to PPC Lead, E to PPC Manager.

**Cadence:** event-driven same session for creations; same day for graduations, declarations, stewardship grants, #16 declarations; weekly Monday pass for reactive routes, ASIN scans, shared-list divergence, reconciliation; deploy Tuesday; monthly wall audit on #4 slot; served-term breach scan at every pull.

**Alarm routing:** same day to operator queue F1, F2, F5, F6; weekly worklist F3, F4, F9, F11, F12; PPC Lead with audit history F7 (first occurrence), F8 (jointly with #33), F10 (with reversion record). Every alarm carries window spend at stake; alarm without dollar figure does not route.

## 11. Failure modes (Section 7)

| ID | Failure | Detection | Response | Incident |
|---|---|---|---|---|
| F1 | Creation without pre-load | T3 list attachment empty or pre-load row count below P2 prescribed count | Pre-load same day via P2; creating session named; creating SOP's F-line notified | Satin cooling terms (v4.0 F11), WE-1 |
| F2 | Wall-less standup, chain broken | P3 verification line absent from #30 chain record, or term in source served terms after graduation | Walls same day; harvest pass reopens; session root-caused | GRADUATED-UNSTEERED (F8) |
| F3 | Converting term negated without diagnosis | Staged negative whose evidence shows in-window orders, no diagnosis note | Hold before deployment; read; fix queue if relevant | None dated; preventive (F11) |
| F4 | Shared-list drift | Role-sharing campaigns with different entry counts or versions at P6 | Re-attach; find divergence source (usually direct edits); name bypassing session | None dated; Doctrine 11; tolerance AM-7 |
| F5 | Wall built at wrong level | Served-term count or adjacent tail clicks collapse window-over-window with no other change; or phrase row with non-zero remainder | P10 case 3; replace root with exact on members; remainder in every phrase reason string | SOP-12 v2.0 F9 "Wall built at the wrong level"; WE-3 |
| F6 | List-scope error | List shows entry and term still serves (only P9 side two catches) | Re-place at level covering all ad groups; audit creating session's other multi-group walls | None dated; WE-4 breach 3 |
| F7 | Uncontrolled removal | Negative absent with no removal-log entry | Reinstate pending review; escalate on first occurrence (only finding escalating without repeat) | None dated; clock AM-8 |
| F8 | Sibling wall not moved at re-arbitration | Declaration date vs wall state disagree; lag in days | P7 same day; #33 adds wall step to checklist | SOP-33 v1.0 F3 "Walls lagging declaration"; SOP-29 v1.0 F5; Bamboo-root 4pc vs 6pc call open through first cycle (Data Architecture Section 11 A1); WE-4 |
| F9 | Over-walling the non-owner | Non-owner's model-specific variants return zero impressions after sibling wall | Restore P7 step 2 posture | SOP-33 v1.0 F4 |
| F10 | Stewardship wall without reversion date | Stewardship wall with no reversion date, or still standing past owner's restock plus recovery | Revert per dated record | SOP-33 v1.0 F5 "Immortal stewardship" |
| F11 | Survivor inherits traffic without fences | After consolidation, survivor list missing entries the paused instance held | Carry missing entries in same change set as pause | None dated; SOP-12 v2.0 P7 step 3 |
| F12 | Negation cadence stalls | Zero negatives across two consecutive passes on campaign with active spend | P4 immediately; cause named as feed-absent or pass-skipped | Doctrine 3.3: broad campaigns without negation cadence leak by design |

Escalation: F7 first occurrence; F1 and F2 on second instance from same session (with attribution and audit history); F12 to PPC Lead on second consecutive stalled pass; F8 jointly with #33. Every escalation carries wall points, window spend at stake, session attribution; without a dollar figure returns to sender.

## 12. Interface contracts (Section 12; from Ledger v1.7 row 29)

| ID | Sender -> receiver | Artifact | Timing | Non-arrival |
|---|---|---|---|---|
| I-1 | SOP-30 PPC Lead -> this SOP operator E | Graduation approval row with full source list (SOP-30 P1.1) | Same day as approval | GRADUATED-UNSTEERED; P11 catches as S-H4; F2 with session attribution; #30 F1 |
| I-2 | This SOP -> SOP-30 PPC Lead | Wall verification line per source into #30 chain record | Same day as walls | #30 harvest pass cannot close; F2 |
| I-3 | SOP-14 operator E -> this SOP | Route B terms and Route C clusters with complete evidence lines | Monday cascade; Tuesday deploy | P4 suppresses; two consecutive = F12 |
| I-4 | SOP-13 -> this SOP | Phrase-broad dedup wall requests, phrase-side steering handoffs (Ledger row 13) | Weekly | Same demand at two control levels; attributes to phrase side |
| I-5 | SOP-15 operator D and E -> this SOP | Auto Routes B-D detections with group tokens (SOP-15 P1.5, P3) | Weekly | Auto waste unfenced; receiving end of SOP-15's I-10 |
| I-6 | This SOP -> SOP-12, 13, 14, 15 | Prescribed pre-load set staged in creation block | Same session as creation | F1 here and in creating SOP; SOP-15 records its F1 and F3 |
| I-7 | SOP-16 operator D and E -> this SOP | Failed-target declaration with exit verdict reference | On declaration | Exited targets re-proposed; no wall without declaration |
| I-8 | SOP-33 PPC Lead -> this SOP | Declaration record, re-arbitration outcome, stewardship grant with reversion date | Same day as declaration date | F8 here, F3 at #33; F10 under stewardship |
| I-9 | This SOP -> SOP-33 | Same-day wall confirmation per placement or move | Same day | #33 gate artifact incomplete |
| I-10 | This SOP -> SOP-38 operator E | Staged negation set in #38 P1 format, complete reason strings | Monday stage, Tuesday deploy | Row with incomplete reason string held and returned; wall waits a cycle |
| I-11 | SOP-38 -> this SOP | T+1 diff on negation rows | Morning after deployment | Walls unverified; A2 stale. Diff proves landing, not correctness (WE-3) |
| I-12 | Data Operations -> this SOP | Search-term and served-ASIN feeds with per-campaign splits and D5 tokens, from SP and SB search term reports and STIS in Raw Pull Pack | Monday 06:00; refresh by 09:00 | P4 and P5 suppress per G8, recorded in pass header |
| I-13 | Brand Management -> this SOP | Current MKL with syntax tags and relevancy; brand-term list across both entities | Bi-weekly (G12); stale past 30 days degrades | Taxonomy line suppresses; creation deploys part-fenced (satin mechanism) |
| I-14 | SOP-32 PPC Lead with deals owner -> this SOP | Event plan with window dates and named actions | Same day window arms | Reactive walls deploy on event evidence; fence outlives window |
| I-15 | This SOP -> SOP-37 PPC Lead | Notice of any negation class routed through automation rule | Before rule arms | Walls with no session record read as F7 |
| I-16 | This SOP -> T6 Decision Log, PPC Lead | One entry per deployed change with prediction (metric, direction, magnitude, horizon, review date) | Every deployment | V1/V5 cannot score |

## 13. Account-specific facts

- **Five brands across two entities** (Inspiratek & Ecotero); brand walls and own-catalog lists span both.
- Planning basis ~280 tracked terms per product.
- Named incident (v4.0 F11): **satin product tracking cooling terms** it cannot rank = pre-load + MKL hygiene failure.
- **Bamboo-root ownership** between the **4pc** and the **6pc** sat open through the first cycle (Data Architecture v1.0 Section 11 tab A1 note).
- Data Architecture v1.0 Section 6.1 mislabels unsteered-graduate filter as S-H6 (C12).
- Worked examples use fictional training base (AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3%, CVR 5.2%); no live operator economics attached. Product names (satin 4pc, bamboo, 6-pc) appear in them.

### Worked examples
| Case | Key figures |
|---|---|
| WE-1 Satin cooling pre-load failure | Satin 4pc auto loose, Discovery, 28-day window, spend $612.00; 6 cooling terms, 118 clicks at $1.42 = $167.56; 5 terms zero orders on 104 clicks = $147.68; 1 order ($80, contribution $28) -> net loss $139.56; campaign zero-order spend $271.32 -> WAS% 44.33% (> 40% Discovery, fires S-H2); cooling = 54.43% of waste; $5.98/day = $2,184.26/yr. Negative phrase "cooling" (reverse-test remainder 0) in satin family broad, auto close, auto loose = 3 wall points vs 18 exacts; MKL tags cooling out-of-taxonomy for satin line |
| WE-2 Steering at graduation | "bamboo sheets split king": family broad 11 clicks $1.72 = $18.92, 2 orders; auto close 6 clicks $1.53 = $9.18, 1 order; sibling 6-pc broad 4 clicks $1.66 = $6.64, 0 orders; 21 clicks, 3 orders, $34.74 (clears graduation bar, L6/S-H1); blended $1.65 vs seeded exact bid $1.30; skipping walls = $7.44/window, $386.88/yr (27% premium). Family broad has 2 ad groups. Sibling 6-pc walled because declaration assigns bamboo root to 4pc. 3 wall points, 0 breaches |
| WE-3 Over-broad root "cool" | Drift pair "cooler bag sheets", "cooler king sheets"; phrase "cool" without reverse test fenced owned "cooling" (3 terms, 8 orders/28 days). Served terms 61 -> 38 (23 fenced vs 2 intended); clicks 92 -> 41; contribution $8.00/day; 6 days live = $48.00 lost. T+1 passed (landing != correctness); caught by P11 (F5). P10 case 3; replace with exact on 2 terms ("cooler" remainder 0). Prediction: served terms back to 58-61 within 2 windows |
| WE-4 Monthly audit | Audit 2026-08-03; 14 terms graduated in trailing quarter, 3-4 sources each = 48 wall points; 45 clean, 3 breaches = 6.25%. Breaches 1-2: session 2026-07-13 missed auto loose (no P3 step 2 verification). Breach 3: 2 ad groups, negative at keyword level in AG1 only (P3 step 4). Own child ASIN in complements 22 clicks at $0.86 = $18.92/30 days = $230.19/yr. Sibling declaration changed 2026-07-21, 13 days lag. 5 findings, 5 fixes, 2 root causes |
| WE-5 Reactive pass with guard | Bamboo family broad, Discovery, budget capped by design; 92 clicks at $1.72 = $158.24; zero-order spend $91.16 -> WAS% 57.61%; 6 Route B terms, 1 with an order held (guard); 5 terms 34 clicks = $58.48; Route C "crib" 3 terms 9 clicks = $15.48 (remainder 0); fenced $73.96/window = $3,845.92/yr; post-pass spend $84.28, zero-order $17.20, WAS% 20.41%. 6 rows (5 exact + 1 phrase). Prediction WAS% <= 25% next window |

## 14. Open items

### 14.1 v4.1 amendment register (Section 10.3; 13 items)
| ID | Gap |
|---|---|
| AM-1 | Reactive-negation firing threshold: S-H7 "Zero-sale spend above threshold on an irrelevant term" and L5 "spend-without-sales" state no clicks-at-zero-orders or spend figure; Route B runs on an unquotable rule |
| AM-2 | "Price class" (SOP-14 P3 Route B, SOP-29 v1.0 P3.1) not a v4.0 dimension; F1 defines margin-dollar class THIN <$6, STANDARD $6-15, RICH >$15; readings diverge |
| AM-3 | Wall-audit population/sampling rule (v1.0 "all terms graduated in the trailing quarter, minimum"; V4 silent); P9 runs full population as local choice |
| AM-4 | Wall-audit calendar slot (v1.0 "first Monday of the month"; not in V4 monthly items); should be registered against #4 |
| AM-5 | Negative-phrase cluster bounds: minimum members, maximum root breadth, served-term-collapse tolerance (produced WE-3) |
| AM-6 | Own-catalog negative-ASIN rule has no rule ID (Doctrine 11 only): groups, formats, child scope, permanence |
| AM-7 | Shared-list divergence tolerance (fires F4) |
| AM-8 | Removal-control escalation clock (hours to reinstate, review window) |
| AM-9 | Wall-breach escalation rate / per-session repeat count |
| AM-10 | Steering-wall verification lag (max hours deploy to verification line; "same day" is SOP-30's rule) |
| AM-11 | Gate numbering divergence (v4.0 G9 price / G10 event / G12 MKL vs corpus G9 margin freshness / G10 objective tagging / G12 event freeze) = conflict C9 |
| AM-12 | WAS% boundary sense (v4.0 "<=10% / Discovery <=40%" vs KDR "<10% / <40%") and KDR sub-bands 10% / 10-15% / 15-20% not in v4.0; bedding and sleep products span subjective classes |
| AM-13 | Record retention for any PPC operating record |

### 14.2 Conflicts referenced
- **C1**: v1.0's 10-element 4-page structure superseded; exemplar SOP-12 v2.0.
- **C3**: #31 has no procedural document.
- **C9**: gate numbering (AM-11).
- **C10**: verdict vocabulary (KDR 25 vs v4.0 13.1 eighteen vs Data Architecture / Ledger twenty-six).
- **C12**: Data Architecture Section 6.1 S-H6 label vs correct S-H4.

### 14.3 v1.0 carry-forward notes (Section 10.2)
- Thresholds carried forward: none (v1.0 had zero decision numerals).
- Incidents carried forward: none from v1.0 (illustrative only); incidents drawn from v4.0 F11 (satin), F8 (GRADUATED-UNSTEERED), SOP-12 v2.0 F9 (wrong-level wall), SOP-33 v1.0 F3/F4/F5, Data Architecture Section 11 tab A1 (Bamboo root), Doctrine 3.3 (leak by design).
- New in v2.0: P1 with reverse test, P5 standalone, P8, P11, P12; F3, F6, F7, F11, F12; four of five worked examples; full 25-verdict mapping; Elements 11-12.

### 14.4 Version review triggers (Section 10.1)
Any v4.0 increment touching L5, F8, F11, S-H1 to S-H8, G2, G8, G11, G12; any SOP-30 chain definition change (increments both); any #38 P1 staging format change; any D5 change at #15 adding/removing/redefining an auto group; any new brand or entity; two consecutive monthly audits with rising breach rate; v4.1 publication. Coupled to SOP-30 (atomic chain) and SOP-14 (routes; SOP-13 and SOP-15 run same machinery, so a route-definition change increments all four).

### 14.5 Live-defense questions (Section 11.1, abbreviated)
1. 40 clicks, zero orders, relevance passes -> no negative, fix queue, F11. 2. Graduation lists 2 sources, feed shows 4. 3. One phrase vs twelve exacts; asymmetry decides default (longer root). 4. WAS% 61% with truncation flag -> L1 budget first. 5. Failing graduate: walls stay (SOP-30 P6). 6. Zero-breach audit artifact still written. 7. Sibling declaration 9 days old, wall not moved -> F8 here, F3 at #33. 8. Own ASIN in profitable complements -> wall anyway. 9. Event arms tomorrow with 11 Route B staged: what deploys/freezes. 10. Missing reactive threshold -> log amendment, do not write a number.

### 14.6 Companions
Criteria System v4.0; KDR Template v3.0 "Bands & Verdicts Reference"; PPC Strategic Doctrine v1.0 Sections 3.1-3.4, 4, 11; PPC Authority Matrix v2.0 Section 1; Master PPC Data Architecture v1.0 Sections 6, 6.1, 7, 9; PPC Command Workbook TEMPLATE v1.0 (T3, T6, T7); PPC Economics Worked-Example Set v1.0; PPC Cross-Reference Ledger v1.7 row 29; SOP-30, SOP-14, SOP-13, SOP-15, SOP-12, SOP-33, SOP-16, SOP-38, SOP-32, SOP-37.
