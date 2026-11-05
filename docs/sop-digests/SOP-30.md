# SOP-30 Digest: Harvest and Graduation Operations

Source: `PPC_SOP_30_Harvest_and_Graduation_v2_0.pdf` (17 pages). Digest of the plain-text extraction; nothing added beyond the text. Some tables were flattened in extraction and their columns were rebuilt from the content.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-30: Harvest and Graduation Operations (Component #30 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-07 |
| Owner | PPC Lead |
| Supersedes | SOP-30 v1.0 (2026-07-24) in full |
| Thresholds | Zero local thresholds. Thresholds, bands, scenarios and verdict issuance live only in Master PPC Decision Criteria System v4.0 |
| Standard | Rebuilt to the SOP Build Kit v1.0 twelve-element standard |
| Size | 12 procedures (v1.0: 7), 25-string closed vocabulary mapped (v1.0: 5 rows), 4 worked examples (v1.0: 1), 12 failure modes (v1.0: 5), operator ramp and interface contracts added, 15 amendment items |

**Verdict / purpose.** Graduation is "the single most valuable recurring event in the account", because it moves converting demand up the control gradient where its economics improve. This SOP owns the **decide** half of graduation and the **assembly of the source list**. It covers: the weekly harvest pass over candidates routed from every discovery source, evidence qualification against the sufficiency gate, validation and disposition, class assignment and family routing, the atomic same-day execution chain and its verification, stem graduation, the head-term fast path, management and aging of the LEAVE TO HARVEST pool, failed-graduate handling, dual-source / twin-set / sibling-shared graduations, the event and Recovery overlays, and per-source yield reporting. **The pass discovers nothing; it adjudicates.**

### The Chain Rule (Section 1.1)
A graduation is **one event with three parts: decide, stand up, wall**. It is incomplete until all three land and the third is verified.
- v4.0 Section 11 rule **T6**: graduations batch weekly. Each graduation deploys an exact campaign with an objective tag, a seed bid at Expected CPC, steering negation at source, a registry entry and a review date. A graduation missing any element is incomplete.
- PPC Strategic Doctrine v1.0 Section 3.4: the most expensive form of structure debt is the graduated term never negated at source, which then buys itself twice at two control levels.
- v4.0 Section 3 Family **F8** "Structure & Registry" names that state **GRADUATED-UNSTEERED**. Section 8.9 scenario **S-H4** orders it closed in the same cycle.
- The three parts run in three components: **this SOP decides**, **SOP-12 stands the exact up (P1 or P2)**, **SOP-29 places the steering walls (P2)**. A pass is closed only when SOP-29 returns a wall verification line for every source campaign attached to every approved term.

### v2.0 corrections
- Two v1.0 verdict strings fixed. "CONTINUE TEST TO 50 CLICKS" is restored to **CONTINUE TEST TO 50 CLICKS AT CAPPED BID**. "REJECT (logged reason)", which is in no closed vocabulary, is replaced by the S-H6 route and its two terminal states.
- The v1.0 citation of a "v4.0 aging rule" for the LEAVE pool is withdrawn. No such rule exists; the gap is logged as AM-4.
- Registered in the Supersession Map. The Ledger row for component #30 is returned with a seed-row scope correction.

## 2. Scope and boundaries

### The four candidate sources (Section 1.2)
Nothing enters except as a routed candidate row carrying an evidence line.

| Source | What arrives / route owner | Evidence line must carry | What this SOP does NOT take from it |
|---|---|---|---|
| **SOP-14 P3 Route A** | Converters from family broad and, through the same shared machinery, from family phrase. SOP-14 owns the weekly three-route triage | Clicks, orders, window, source campaign, CPC, per the route that produced it | The routing decision itself, and the negation cadence that produces Routes B and C |
| **SOP-13 P4 stem routes** | A validated high-volume stem with its member long-tail set named | Stem string, member set, pooled member evidence | Stem clustering, the dated pilot, phrase-side standing coverage under LEAVE TO HARVEST |
| **SOP-15 P3 Route A** | Auto-side converters, one row per term per targeting group, each with its group token | Group token plus the standard fields. Post-D5 evidence is group-level, never blended | The D5 split, per-group verdicts, the two ASIN routes |
| **Head-term receipts** | ADD EXACT + RESTRUCTURE receipts from any source's head-term check | Carrying campaign, its share of the term's clicks, absence of a live exact | The head-share computation (each source runs it on its own served terms) |

**ASIN converters are not candidates** and never enter this pass. SOP-15 P3.3 routes converting substitute ASINs straight to SOP-16, which decides. The Cross-Reference Ledger component-16 row records this and corrects an earlier attribution of the route to #30.

### The three dispositions (Section 1.3)

| Disposition | Condition | Verdict issued |
|---|---|---|
| Approve | Orders at or above the S-H1 bar; relevancy and taxonomy clear per G12; evidence group-level where source is auto | **GRADUATE FROM DISCOVERY** (v4.0 Section 13.1 issues the same decision as **GRADUATE + STEER**; both citations kept) |
| Hold | Converting below the S-H1 bar, relevant, still earning inside its source's discovery economics | **LEAVE TO HARVEST** |
| Route out | Evidence contradicts relevance or taxonomy membership, whatever the order count | G12 route runs first; terminal states are a **logged taxonomy expansion** or **NEGATE (PRE-LOAD / REACTIVE / STEERING)** |

The bar is stated three times in v4.0: **S-H1** (Section 8.9), **L6** (Section 9, structure lever), **T1** (Section 11, objective transition). The SOP calls this "the strongest signal in the corpus that the bar is not negotiable at execution time".

### Boundaries with adjacent components (Section 1.4)

| Component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, scenario, gate, lever and verdict, including the graduation bar. A threshold appearing in this SOP is a defect; a number v4.0 does not carry becomes an Appendix A item, never a local value |
| #14 Broad | Owns the weekly three-route triage and the definition of Route A. This SOP consumes Route A output; it never re-runs the triage or re-derives an evidence line |
| #13 Phrase | Owns stem clustering, the four stem routes, the phrase-side graduation handoff, and Surface-2 standing long-tail stem coverage. This SOP decides only whether a routed stem graduates |
| #15 Auto | Owns the D5 four-group structure, per-group verdicts, group-token hygiene. This SOP refuses blended post-D5 auto evidence and returns the row |
| #12 Exact | Owns exact standup on both classes (P1 single-keyword, P2 consolidated tail) and promotion/demotion between them (P5, P6). This SOP assigns the entry class; it never executes a promotion |
| #29 Negation | Owns negation doctrine, the wall-level selection tree, steering wall standards, the monthly wall audit. This SOP hands over the approved term with its full source list and consumes the wall verification line. Without that line the pass cannot close |
| #16 PAT and conquest | Owns target opens, flag tests, rotation, exits. ASIN converters reach #16 via SOP-15 P3.3 |
| #33 Sibling arbitration | Owns the family ownership declaration and its composite. This SOP reads the declaration to assemble the source list and satisfy G11 |
| #38 Bulk mechanics | Owns pull, staging format, upload, T+1 verification. This SOP produces staged rows in #38 format and consumes the verification report |
| #32 Deal/event window | Owns the event plan, armed-window declaration, reconciliation. This SOP stages normally inside an armed window and deploys only what the plan names |
| #31 Budget/envelope | Decides funding, CAP SYNTAX and every envelope-level budget verdict. Per Ledger conflict **C3**, #31 has no procedural document, so this SOP names the instrument and tab (**T0 zone H, Account Rollup A2**) and never cites a #31 procedure number |
| #28 Placement/modifier | Owns ladder step derivation and exit-bid discovery. A graduate's seed bid comes from the verdict and the Expected CPC reference, never from a ladder this SOP computes |

Depth note: the v1.0 ran to 3 pages and left four gaps unwritten: source-list assembly, the dual-source credit rule, pool aging, and every non-arrival consequence. The SOP says those four gaps are where the account's graduated-unsteered leaks actually happen.

## 3. Triggers (Section 2)
Calendar anchors come from the Command Workbook READ ME "CADENCE AND OWNERSHIP" line: **Monday 06:00 feed landing, 09:00 packet ready, Tuesday deploy after the BM huddle, T+1 verification**. Cadence classes are v4.0 Section 14 rule **V4**. v4.0 has no numeric signal-to-start lag table; lags in hours are planning figures (AM-12).

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Weekly cadence | Monday cascade reaches T2 KEYWORD COMMAND after T0 and T1 are read; candidate rows from SOP-14 P3, SOP-13 P4, SOP-15 P3 in the pass worklist with evidence lines | Same day; starts once the T7 MANIFEST completeness stamp is read and T6 rows due this cycle are scored | P1, then P2-P5, then P12 |
| Head-term receipt | ADD EXACT + RESTRUCTURE receipt from any head-term check, visible as a **T2 K9 "Action Source (Finding IDs)"** entry naming the carrying campaign | Same day on arrival, outside the weekly rhythm. Waiting for Monday = **F5** | P7 immediately; validation queue skipped |
| Stem route | SOP-13 P4 routes a validated stem with member set | The same weekly pass | P6 |
| Re-evaluation date | **T2 K7 "Review Date"** on a LEAVE TO HARVEST row reaches/passes cycle date; PAUSED-PENDING and pool filter views surface them | The pass in which the date lands. Passing untouched = **F4** | P8 |
| Wall verification return | SOP-29 returns a line per source, or the #38 T+1 report shows a wall point missing or a graduated term still serving in a source's served terms | Same day. A chain open past T+1 reopens the pass | P5 step 6; **F1** on miss |
| Registry conflict | **T2 K8 "# Exact"** at 2 or more for one term, "Duplicate Flag" set, no declared role in the T3 row | Same pass, before any further graduation on that term | P1 step 5 dedupe (text says step 5; dedupe is P1 step 7); consolidation at SOP-12 P7 |
| Failed graduate | Graduated exact's **T2 K9 "Last Cycle Prediction Score"** returns MISS or WRONG-DIRECTION against the graduation prediction at review date | The pass in which the score lands | P9. Source walls stay whatever the outcome |
| MKL refresh | Bi-weekly MKL refresh changes a tracked term's syntax tag or relevancy, visible in **T2 K1 "Relevancy" and "Syntax Tags"** | Next pass. A term whose relevancy fell below bar cannot graduate on evidence gathered before the change | P3 step 4 (text) re-tests G12 on every candidate and open pool entry |
| Event window arming | #32 lands an armed-window declaration in **T2 K2 "Event Mode"** with dates | Before the next staging step inside the window | P11 event overlay; staging continues, deployment follows the plan |
| Recovery Mode entry | **T0 zone A** carries CODE-RED, or product enters Recovery per v4.0 Section 11 rule **R1** | Same pass | P11 Recovery overlay; R3 tiers apply to every chain |

## 4. Procedures (Section 4)
Time figures are planning estimates for scheduling the Monday block. Nothing branches on them.

### Preconditions and gates (Section 3)
Each gate is listed with its v4.0 ID, the T7 MANIFEST field group that proves it can be read, and the observable that shows it passed. Per Ledger conflict **C9**, the corpus numbers three gates differently (alias given; AM-11). A gate that cannot be read has not passed: **G8** downgrades a verdict whose gate fields are missing to a flag.

| Gate (v4.0 Section 5) | T7 field group | Effect on this pass | Observable |
|---|---|---|---|
| **G1** Validation quarantine | A4, A5, B11 | Impossible-metric row produces a flag + data-refresh task, never a candidacy. Candidate whose evidence line contains a quarantined row does not enter the queue | **T2 K5 "Flag: Zero-Quarantine"** reads Clean on every evidence row. Canonical case: Bamboo 4pc file's broken SQP rows (CVR zero with orders present) |
| **G2** Sample sufficiency | A4, A1 | Sets what may be read, not whether the term graduates. S-H1 is an order count and clears at its own count; CVR/CTR verdicts that would price the seed bid clear only at their own thresholds | **T2 K2 "Sample State"** and **"Clicks 7/30/60d"**. Below the CVR threshold the ceiling falls back to product reference CVR from T0, recorded |
| **G3** Budget truncation | A3 | Truncated source's rates describe its worst hours. Order count still counts; its CPC is marked and does not seed a bid on its own | **T3 "Truncation Flag (G3)"** and **"In-Budget Bucket"** on every source campaign |
| **G4** Eligibility | A7 | Ineligible advertised SKU halts all lever work. No standup; candidate holds with listing task as re-entry criterion | **T2 K2 "Eligibility"** = Live and **T3 C2 "Eligibility + Reason"** clear on receiving campaign |
| **G5** Indexing and listing placement | B1 | Bars a rank-objective standup on an unindexed term. Conversions or Discovery-graduate objectives unaffected; Ranking routes to indexing queue first | **T2 K2 "Indexed?"** and **"Listing Placement"** = Yes and Title or Bullets for rank-objective graduates |
| **G6** Inventory adequacy | D2, F3 inputs | RED on targeted variation blocks the standup and re-points ranking campaigns to the declared backup same day. Graduate whose D2-preferred variation is RED holds; the walls do not | **T2 K2 "Inventory Band"** and **"Days to Stockout"**, D2 map naming the ranked backup |
| **G8** Packet completeness | T7 rollup | DEGRADED manifest = flags only. Pass runs on readable rows, records suppressed classes, never approximates missing evidence | **T7 "PACKET COMPLETENESS SCORE"** stamp on cycle header, blocked verdict classes named in-row |
| **G9** Price stability (corpus alias: G9 margin freshness) | D1 | Price change on targeted variation inside trailing **7 days** marks CVR and ACOS reads PROVISIONAL. Order count unaffected | T2 K2 and T0 economics spine G9 state. Economics chain (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC in **T0 C18:C24**) fresh or record states PROVISIONAL |
| **G10** Event exclusion (corpus alias: G12 event freeze) | A1, T5 | Event weeks and the **14 days following** are excluded from trend verdicts. Graduations still stage; standups deploy outside frozen scope unless the event plan names them | **T2 K2 "Event Mode"** and **T5 PRODUCT LOG "Trend-Exclusion Flag"** |
| **G11** Sibling conflict | D6 | Term with two siblings carrying active push objectives is a portfolio decision first. Declared owner determines whose exact receives the graduate and which sibling campaigns join the source list | **T2 K8 "Term Owner (Family)"** reads a declared owner (not UNDECLARED) and **T2 K2 "Family Conflict"** clear |
| **G12** MKL hygiene (corpus alias: G10 objective tagging) | B2 inputs via the Hub | Every candidate must be in the current MKL with a syntax tag and relevancy score. Untagged/below-bar routes to MKL maintenance and taxonomy pre-negation, not graduation, whatever the order count | **T2 K1 "Syntax Tags"** and **"Relevancy"** populated; MKL refresh inside bi-weekly cadence. MKL past **30 days** degrades the manifest. Motivating case: satin product's cooling terms |

Standing preconditions: (1) every candidate row carries an evidence line or it does not enter; (2) post-D5 auto evidence is group-level with group token. A blended auto row validates nothing (F3); SOP-15 P9 quarantines token-blocked rows at source.

### P1. Candidate queue assembly and dedupe (15-25 min per product)
1. Enter only after **T0 PRODUCT COMMAND** and **T1 SYNTAX BOARD** are read. A T2 pass that skipped T0/T1 is invalid. Read **T0 zone D (twelve-cell gates strip)** and **T0 zone C (economics block)** first; seed bids are priced against **T0 C18:C24**.
2. Score last cycle first. Open **T6 DECISION LOG**, filter to "Review Date" this cycle and "Level" = Keyword; record **"V5 Score"** as HIT / PARTIAL / MISS / WRONG-DIRECTION. Unscored actions do not accumulate (rule **V1**). Graduation rows scoring MISS or WRONG-DIRECTION go to P9 this pass.
3. Read **T7 MANIFEST** before the queue; record status of **A1, A4, B5, B8, D1, D2, D6**. A MISSING group does not stop the pass; it suppresses the classes in that row's "Verdict Classes Blocked While Missing" cell, and the suppression is written into the pass artifact.
4. **One row per TERM, not per arrival.** Collect from SOP-14 P3 Route A, SOP-13 P4, SOP-15 P3 Route A and head-term receipts. The same term arriving from two or more sources is ONE candidate row with all sources attached. Treating it as two = **F2**.
5. **Attach the full source list.** For each candidate open the T2 keyword parent row, expand the campaign child rows with the outline control, and record every campaign with non-zero clicks on the term in the window. Read child **"Camp Type (child)", "Camp Objective (child)", "Spend Share of KW %"**. The source list is every campaign that SERVED the term, not only the one that routed it. A list built from the routing arrival alone is "the single most common origin of a graduated-unsteered leak".
6. Extend across the family. Read **T2 K8 "Term Owner (Family)"**. If family-shared and declared, the non-owner's discovery campaigns join the source list (they need the sibling wall). If **UNDECLARED**, G11 holds the chain and the term routes to #33 for a declaration; it stays queued with the block recorded.
7. **Dedupe against live structure.** Read **T2 K8 "# Exact"** and **"Duplicate Flag"**. A term with a live exact is not a candidate: either already graduated and unsteered (route to the S-H4 close; the steering wall is the whole remedy) or a duplicate with no declared role (route to SOP-12 P7). Neither adds a second exact.
8. Rank by the loss the delay costs: head-term receipts first (leave immediately under P7), then dual-source terms by largest combined window spend, then single-source.

### P2. Evidence qualification (10-20 min per product)
1. Read the evidence line as it arrived; do not recompute from raw pull. A line missing any of clicks, orders, window, source campaign or CPC returns to source.
2. Check the group token on every auto row. A row with no resolvable token should have been quarantined by SOP-15 P9; if one appears, return it and record the exposure (F3).
3. **Dual-source pooling:** clicks, orders and spend sum across sources. CPC = pooled spend / pooled clicks, labelled a **blended discovery CPC**, never carried forward as a bid.
4. **Twin sets:** rule G2 pools twin-set evidence for sufficiency; **T2 K1 "Twin-Set ID"** identifies the set. v4.0 does not say whether the S-H1 order count pools across a twin set, so record the partner's evidence beside the candidate's and **do not add the counts** (AM-15).
5. Apply G2 to what the evidence can price, not to whether the term graduates. The order bar clears at its own count. Below the CVR threshold the ceiling uses the product reference CVR in T0, and the record carries the fallback and its confidence effect (v4.0 Section 7 rules **D3, D9**).
6. Mark every line whose source carries the G3 truncation flag. Its CPC is not a price signal; seed reference falls to Expected CPC alone, and the record says which input was unusable.

### P3. Validation and disposition (20-35 min per product)
1. **Run G12 first, before reading the order count.** Open T2 K1: current syntax tag and relevancy at or above bar? Below bar or off-taxonomy routes to the MKL classification decision whatever the orders: taxonomy expands deliberately (logged with syntax tag and test plan) or the term negates. This is scenario **S-H6**, the one place where meeting the bar does not graduate. "Three incidental sales do not create a market position."
2. Read pooled orders against S-H1. At or above means approval subject to steps 3-4; below means hold.
3. Test relevance against the evidence. Orders landing at a price point or variation the product does not serve contradict the relevancy score; route to step 1's MKL decision, reason logged.
4. Test the execution-blocking gates: **G4** eligibility, **G5** indexing (if Ranking objective), **G6** inventory on the D2-preferred variation, **G11** family ownership. Failing one = **approved on evidence, held on execution**, with the blocking gate and re-entry criterion named. The record shows both states.
5. Write the disposition into **T2 K9 "VERDICT"** with the closed-vocabulary string and fired scenario IDs in **"Scenario ID(s)"**. A staged row without a scenario ID does not deploy.
6. Log the reason on every non-approval. A hold carries accumulated evidence and a review date; a route-out carries the gate fired and the owner. Nothing exits silently.

**P3 decision tree**
```
Candidate row (evidence line complete? no -> return to source SOP)
 +- G12: in current MKL, tagged, relevancy >= bar?
 |    No  -> S-H6 route: MKL classification decision first. Terminal: logged taxonomy
 |           expansion, or NEGATE (PRE-LOAD / REACTIVE / STEERING)
 |    Yes -> continue
 +- Auto-sourced row without group token? -> F3: return to SOP-15 P9. No verdict.
 +- Pooled orders >= S-H1 bar?
      No, relevant and converting       -> LEAVE TO HARVEST; pool entry + evidence + review date (P8)
      No, zero-sale past the S-H7 line  -> not this pass: reactive route (SOP-14 P3 Route B / SOP-15 P3 Route B)
      Yes, orders contradict relevance  -> step 3: back to S-H6 route
      Yes                               -> GRADUATE FROM DISCOVERY, then:
           G4/G5/G6/G11 all clear?  -> approve and execute: P4 then P5
           One or more failing      -> approve on evidence, hold on execution; name gate + re-entry criterion
```

### P4. Class assignment and family routing (10-15 min per product)
1. Read **T2 K1 "Oversight Flag"** (Y/N); do not judge it. v4.0 basis: Section 12 rule **P5** (every **500+ SV** keyword action human-confirmed) and Section 6 rule **O2** (SV floor **above 500** for a Ranking objective). The Data Architecture and KDR Template add a second limb, **top spend decile**, which v4.0 does not carry. A term qualifying only on that limb is recorded as resting on the ungoverned limb (AM-3).
2. Assign the class. **Flag Y = single-keyword class, standup at SOP-12 P1. Flag N = consolidated tail class, standup at SOP-12 P2.** Read from the flag, never from the week's strength (assigning on judgment = **F12**).
3. Assign the syntax family from the root using the family map in **T2 K1 "Syntax Tags"**. The family decides which consolidated campaign receives a tail graduate and which caps apply (the family is the cap-enforcement unit).
4. Read cap state before routing a tail graduate: **T1 SYNTAX BOARD, S3 group, "Cap status" and "Share vs target (pp)"**. A family already over cap **still receives the graduate**, because a graduation is a structure change, not a spend increase. The cap consequence is a budget verdict executed at T1 through the instrument layer.
5. Carry the objective. Tail graduate enters on the receiving campaign's dominant tail objective; oversight graduate on the objective the verdict declares. No untagged graduate (an untagged row is UNMANAGED and cannot be evaluated).
6. Carry the seed bid. Rule **T6** seeds at Expected CPC from **T2 K6 "Expected CPC $"**. Record beside it the ceiling, **Max Profitable CPC from T2 K6** = margin dollars x CVR (Family **F1**, rule **M1**). If the seed is above the ceiling, record that and name the objective that permits it; if no objective permits it, enter at the ceiling and log the difference. A bid is never invented at standup; SOP-12 P1 step 7 returns a creation whose verdict carried no bid.
7. Write **class, family, objective, seed bid, ceiling** onto the graduation record before standup. Missing any of the five means SOP-12 returns it.

**P4 decision tree**
```
Approved term
 +- T2 K1 Oversight Flag = Y -> Class 1 single-keyword -> SOP-12 P1
 |     (qualifies only on top-spend-decile limb? record ungoverned basis; AM-3)
 +- Oversight Flag = N
      Family consolidated campaign exists?        -> extend it -> SOP-12 P2
      No family campaign exists                   -> SOP-12 P2 creates one; never straddle two families
      Receiving ad group already at its size cap  -> SOP-12 P2 opens a second ad group in the SAME
                                                     campaign, never a second campaign on the family
```

### P5. The atomic execution chain (20-30 min per approval batch)
1. Issue the verdict: **GRADUATE FROM DISCOVERY** into T2 K9 with scenario IDs **S-H1** and, where the head-term path applied, **S-R12**. Human confirmation is mandatory on every approval and every rejection (Authority Matrix v2.0 row "Weekly verdicts (established US)"; rule **P5**).
2. Hand the standup to SOP-12 the same day with class, family, objective, seed bid and ceiling. This SOP does not create campaigns, set placement modifiers or write campaign names.
3. Hand the term and its **FULL source list** (P1 steps 5 and 6) to SOP-29 in the same session. SOP-29 owns wall levels; this SOP owns that no source is missing.
4. Confirm the registry moved: **T2 K8 "# Exact"** increments; a **T3 CAMPAIGN BOARD** row exists or is extended, with **C5 "Graduations (Qtr)"** incrementing on the receiving campaign. If the registry did not move, the standup did not land.
5. Write the **T6 entry with the prediction before deployment**: metric, direction, magnitude, horizon. The prediction is the exact's CPA against its blended discovery CPA at review date, with the CPC ceiling as the constraint. A creation without a logged prediction does not deploy at any tier (rule **P10**).
6. **Close on the verification line, not on deployment.** SOP-29 returns one line per source confirming the negative is present; #38's T+1 report confirms landed values on the standup. The chain closes when every source has returned its line AND the term is absent from every source's served terms in the following window. Walls not verified = **F1**; the pass reopens.
7. If the chain cannot close because a wall could not be placed, record the open wall point, reason and owner. Exposure = **(blended discovery CPC - exact seed bid) x clicks the source continues to take**.

### P6. Stem graduation (15 min per stem)
1. Receive the routed stem from SOP-13 P4 with member long-tail set named. The stem construct belongs to #13.
2. Read **pooled member evidence** against S-H1. No single member needs to clear the bar alone.
3. Graduate the stem **ONCE**, as the stem phrase into exact. Members stay in phrase as standing coverage under LEAVE TO HARVEST (#13's Surface-2 responsibility, not re-opened weekly).
4. Specify the wall pattern on the record: **stem as negative phrase in the phrase source (fencing every member) plus negative exact in broad**. Members are not walled individually. SOP-29 executes it.
5. Log the member count fenced beside the wall count.
6. Record the standing gap: v4.0 has no stem construct and so no once-only rule. The rule is carried from #13 and #29 conventions (AM-14).

### P7. Head-term fast path (20-30 min per receipt, same day)
1. Trigger: ADD EXACT + RESTRUCTURE receipt. v4.0 Section 4 rule **X10**: auto or broad carrying **more than 40%** of a priority term's clicks is a structure failure, not a performance signal. Section 8.4 scenario **S-R12** orders ADD EXACT + RESTRUCTURE before any performance verdict on a priority term with **zero exact campaigns**.
2. Run immediately on arrival, outside the weekly rhythm; validation queue skipped. A receipt sitting in the weekly queue = **F5**, escalates on first occurrence.
3. Build the source list as in P1 step 5, then run P4. A priority term at **500+ SV** carries the oversight flag and enters single-keyword class.
4. Execute P5 in full (standup SOP-12, walls SOP-29, registry, prediction, verification). Steering negation closes the leak the same day the exact goes live.
5. Record the exposure closed: carrying campaign's share of clicks, its CPC, and the exact's seed bid. Standing example: the **six-piece satin case** (all head-term traffic through auto, zero exacts); the **6pc auto-dominance finding** surfaces as a one-cell read in **Account Rollup A4**.

### P8. LEAVE TO HARVEST pool management (10-20 min per product)
1. The pool is a reviewed list. Open T2 with the **PAUSED-PENDING filter view** and **K7 "Review Date"**. Every entry carries accumulated evidence, source list at entry, and review date.
2. At re-evaluation re-read **G12 first**. Relevancy below bar at last MKL refresh means the entry leaves through S-H6 whatever its orders.
3. Test accumulated window against S-H1. Clearing means graduate via P4 and P5 this pass. Not clearing means hold with evidence carried forward and a new review date.
4. Record the aging gap on every hold. v4.0 has no aging rule or re-evaluation interval; the interval used is an operating value in the entry's T6 row (AM-4).
5. Report the pool as a **distribution**: entries, age bands, oldest entry's age. Count-only reporting hides rot (F4). Alarm bar ungoverned (AM-5).
6. Re-attach the source list at re-evaluation (paused campaigns drop out; newly serving campaigns join).

**P8 decision tree**
```
Pool entry reaching review date
 +- G12 re-read: still tagged, relevancy >= bar?  No -> S-H6 route; entry leaves pool
 +- Accumulated orders >= S-H1 bar?              Yes -> GRADUATE FROM DISCOVERY: P4, P5, source list re-attached at today's state
 +- Still converting in trailing window?
      Yes                        -> LEAVE TO HARVEST holds; evidence carried; new review date (AM-4 interval)
      No, and spend continues    -> reactive negation route owns zero-sale term (SOP-14 P3 Route B)
      No, and spend has stopped  -> entry closes with reason; re-entry needs new-window evidence line (ungoverned, AM-10)
```

### P9. Failed-graduate handling (15 min per case)
1. Trigger: graduation prediction scores MISS or WRONG-DIRECTION at review date in T6 (source CVR did not transfer).
2. The verdict is diagnosis, not un-graduation.
3. **Source walls STAY regardless of outcome.** SOP-29 P7 removal control admits four named case classes and this is not one of them.
4. Route the exact to its own verdict path at SOP-12 (bid step toward ceiling, taper, or pause, as v4.0 issues). It does not return to the harvest queue.
5. Attribution check first: **T5 PRODUCT LOG** for listing change, price move, OOS window, deal window or competitor entry inside the graduation window (rule **D5**).
6. Record the failure against the **source**, not only the term (yield-quality finding for the discovery SOP). Failure horizon ungoverned (AM-9).

### P10. Dual-source, twin-set and sibling-shared graduations (10 min inside the pass)
1. Dual-source: one row, all sources attached, one graduation, walls in every source; evidence pools (P2 step 3).
2. Twin sets (**T2 K1 "Twin-Set ID"**): one managed term with one bid posture and shared negatives (Family **F8**; Section 8.11 scenario **S-B4**). A graduating twin carries its partner's source campaigns into the wall list.
3. Sibling-shared: **G11** holds until **T2 K8 "Term Owner (Family)"** names an owner. The owner's exact receives the graduate; the non-owner's discovery campaigns get the sibling wall.
4. If the declaration changes after landing, the walls move with it (declaration = #33; wall move = SOP-29 P5). The graduation record names the declaration and its date.
5. **Credit yield to each source that served the term** (no v4.0 basis, AM-7). Apply consistently and state on every yield read.

### P11. Event-window and Recovery-Mode overlays (5-10 min per window)
1. Inside an armed event window, graduations stage normally. Deployment follows the #32 event plan, outside the frozen scope unless the plan names the standup.
2. Event-window evidence is read for the order count only. Event weeks + **14 days following** are excluded from trend verdicts (G10). Event CVR/CPC does not price a seed; the seed falls to the **pre-window Expected CPC** and the record carries the exclusion flag.
3. Rank gains inside an event are provisional (Section 8.12 scenario **S-E5**). A Ranking-objective graduate during a window carries the provisional state so the taper clock does not start on an event spike.
4. Recovery Mode (rule **R3**): **bid moves above 15%** and **budget moves above $25 per day** are human-confirmed; step sizes cap at standard even at HIGH confidence. Graduations are structure repairs inside **R2's fourth triage band**, so they continue rather than freeze.
5. Record the overlay on the pass artifact, so the next cycle's V5 scores stay readable.

### P12. Pass close: yield, registry reconciliation, T6 chain (15-20 min per product)
1. Per-source yield = **validated graduations credited per $100 of source campaign window spend**. Spend from **T3 C4 "Spend $ (L30)"** scoped to window; write into **T3 C5 "Harvest Yield"**; "Graduations (Qtr)" increments. These reads grade the discovery SOPs.
2. v4.0 sets no floor for yield. Rule **O6** names graduation rate as one of three Discovery objective metrics without a band; reported against own trailing baseline (AM-8).
3. Registry reconciliation: for every approval, "# Exact" moved by **exactly one**; no term at **2 or more** without a declared role in T3. A move of two = **F2**.
4. Wall reconciliation: one verification line per attached source per approved term. Write **wall points checked** and **wall points confirmed**. Equal is the passing state; any difference is open exposure.
5. Write the pass artifact (graduation log, one row per candidate): term, sources, evidence, disposition, class, family, seed bid, ceiling, wall points and verification state, prediction, review date. "A pass without it did not happen."
6. Close the T6 chain: every deployed change has prediction + review date; next cycle's P1 step 2 scores it. Name any suppression/overlay and its manifest cause.

## 5. Rules, thresholds and numbers

### Numeric values in the text

| Value | Meaning | Source |
|---|---|---|
| **3 or more orders** | S-H1 graduation bar (discovery term to exact, declared objective, negated at source). No evidence window stated (AM-1) | v4.0 S-H1; restated L6, T1 |
| **50 clicks** | CONTINUE TEST TO 50 CLICKS AT CAPPED BID: candidate stays in source at capped test bid until quota | KDR closed vocabulary |
| **500+ SV** | Every keyword action human-confirmed; oversight flag basis; priority head term enters single-keyword class | v4.0 P5 |
| **SV above 500** | Floor for Ranking objective | v4.0 O2 |
| Top spend decile | Second oversight limb in Data Architecture/KDR Template; not in v4.0 | AM-3 |
| **More than 40%** of a priority term's clicks in auto or broad | Structure failure (head-term trigger) | v4.0 X10 |
| Zero exact campaigns on priority term | S-R12 ADD EXACT + RESTRUCTURE | v4.0 S-R12 |
| **7 days** | G9 trailing price-change window, makes CVR/ACOS PROVISIONAL | G9 |
| **14 days** after event weeks | Excluded from trend verdicts | G10 |
| **30 days** | MKL older than this degrades the manifest | G12 |
| Bi-weekly | MKL refresh cadence | G12 / I-11 |
| 7d / 30d / 60d | G2 click buckets ("Clicks 7/30/60d"), for rate reads only | G2 |
| **15%** bid moves, **$25/day** budget moves | Recovery Mode human-confirmation thresholds | v4.0 R3 |
| R2 fourth triage band | Where graduations sit in Recovery (continue) | v4.0 R2 |
| 2 or more | "# Exact" count that signals registry conflict | T2 K8 |
| Exactly 1 | Required "# Exact" increment per approval | P12 |
| Per $100 window spend | Yield unit | P12 |
| THIN under $6, STANDARD $6-15, RICH above $15 | v4.0 margin-dollar class (Family F1), cited in AM-2 | v4.0 F1 |
| Max Profitable CPC = contribution x CVR | Ceiling | F1, M1 |
| Target = 50% of break-even; Max Acceptable = 75% of break-even | Used in worked-example chain | Economics Worked-Example Set |
| Monday 06:00 / 09:00 / Tuesday / T+1 | Feed land / packet ready / deploy after BM huddle / verification | Command Workbook READ ME |
| 2 consecutive passes | With spend active and zero Route A arrivals = stalled negation cadence; escalate to PPC Lead | I-1 |
| 2 clean audit weeks | Close the operator ramp | Section 11 |

### v4.0 rule / scenario IDs referenced

| ID | As described |
|---|---|
| G1 | Validation quarantine |
| G2 | Sample sufficiency; twin sets pool for sufficiency |
| G3 | Budget truncation |
| G4 | Eligibility |
| G5 | Indexing and listing placement |
| G6 | Inventory adequacy |
| G8 | Packet completeness; missing gate fields downgrade a verdict to a flag |
| G9 | Price stability (corpus: margin freshness) |
| G10 | Event exclusion (corpus: objective tagging) |
| G11 | Sibling conflict |
| G12 | MKL hygiene (corpus: event freeze) |
| O2 | SV floor above 500 for Ranking objective |
| O6 | Graduation rate is one of three Discovery objective metrics; no band (WAS limit beside it has one) |
| D3, D9 | CVR fallback to product reference CVR and its confidence effect |
| D5 | Consult the product log before crediting/blaming PPC for any swing |
| L6 | Structure lever (restates S-H1) |
| T1 | Objective transition (restates S-H1) |
| T6 | Graduation unit: weekly batch; exact + objective tag + seed at Expected CPC + steering negation at source + registry entry + review date |
| R1 | Recovery Mode entry |
| R2 | Triage bands; graduations in fourth band, continue |
| R3 | Recovery confirmation tiers: bid >15%, budget >$25/day human-confirmed; step sizes cap at standard |
| P5 | Every 500+ SV keyword action human-confirmed |
| P10 | A creation without a logged prediction does not deploy at any tier |
| M1 | Max Profitable CPC sizing |
| M5 | Push funding queue (RANK PUSH) |
| M6 | Structure check that loses an input if yield reads are missing (I-14) |
| V1 | Unscored actions do not accumulate |
| V4 | Cadence classes |
| V5 | Score of a T6 row: HIT / PARTIAL / MISS / WRONG-DIRECTION |
| X10 | Auto/broad >40% of priority term clicks = structure failure |
| F1 (family) | Product Economics |
| F8 (family) | Structure & Registry; GRADUATED-UNSTEERED; twin sets |
| S-H1 | 3+ orders graduates to exact |
| S-H4 | GRADUATED-UNSTEERED closed same cycle |
| S-H6 | Off-taxonomy / below-relevancy term: MKL classification decision first |
| S-H7 | Zero-sale line; reactive route owns it |
| S-R12 | ADD EXACT + RESTRUCTURE on priority term with zero exacts |
| S-B4 | Twin set = one managed term |
| S-E5 | Rank gains inside an event are provisional |

### Closed vocabulary mapping (Section 5, all 25 strings, from KDR Template v3.0 "Bands & Verdicts Reference")
Per Ledger conflict **C10** the vocabulary appears at three different counts across the corpus.

| Verdict | This SOP's execution |
|---|---|
| GRADUATE FROM DISCOVERY | Owned here: P3, P4, P5. Only after G12 clears and pooled orders reach S-H1. v4.0 13.1 string GRADUATE + STEER (maps to S-H1, T6). KDR string goes in T2 K9 because the workbook's data validation list is built from it |
| LEAVE TO HARVEST | P8 pool entry with evidence, source list, review date. No exact |
| ADD EXACT + RESTRUCTURE | P7 fast path. Restructure note names the carrying campaign |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | Steering half owned by #29. This SOP delivers term + full source list and consumes verification; never sets wall level. Pre-load and reactive never originate here |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Not yet a candidate; no action, no pool entry |
| FUND TEST (UNFUNDED PRIMARY) | Capped dated test created at SOP-12; this SOP records under-test and defers candidacy to quota |
| QUARANTINE: DATA REFRESH | No candidacy; refresh task with owner and date; re-enters on next clean pull, evidence re-read |
| CONSOLIDATE DUPLICATES | Detected at P1 step 7; consolidation at SOP-12 P7; no second exact |
| RANK PUSH: FUND SIZED PUSH | None. Push funding is M5 queue's, sizing is #23's |
| RECOVERY PUSH | None; recovery-class term not a discovery candidate |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | None; executes at SOP-12 on live exact |
| UNLOCK TRAFFIC | None |
| FIX BUDGET (TRUNCATED) | None; truncation makes the source CPC unusable as seed (P2 step 6) |
| FIX CONVERSION FIRST; DEFER PUSH | None; never re-opens the graduation |
| PLACEMENT FIX FIRST | None; #28. Graduate modifiers start unearned (SOP-12 P1 step 8) |
| RE-POINT VARIATION | Precondition: advertised SKU is D2-preferred. G6 RED before standup = hold; flip after = SOP-12 P10 |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | None; SOP-12 P4 |
| HOLD; DEFEND LIGHTLY AT RANK | None |
| DEFEND AT FLOOR | None; brand terms are steering-negatived out of generic discovery, never candidates |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | None; cap breach on receiving family does not stop graduation (P4 step 4); budget half at T1 |
| INCREMENTALITY LADDER | None; measurement #35, ladder #28 |
| ENTER SBV ARBITRAGE | None |
| OPEN / ROTATE / EXIT CONQUEST | None; ASINs to #16 via SOP-15 P3.3 |
| STOP-LOSS: CONCEDE OR DEFER | None on term; records candidacy path closed so not re-queued from stale evidence |
| PAUSED-PENDING (REASON + RE-ENTRY) | Used on approvals held by a blocking gate; reason = gate, re-entry = clearance |

## 6. Data inputs required
- **Candidate rows with evidence lines**: SOP-14 P3 Route A (broad + phrase), SOP-13 P4 stems (stem string, member set, pooled member evidence), SOP-15 P3 Route A (with group tokens), head-term receipts (carrying campaign, its click share, no live exact). Required fields: clicks, orders, window, source campaign, CPC.
- **Command Workbook tabs/blocks/columns:**
  - **T0 PRODUCT COMMAND**: zone A (CODE-RED / Recovery), zone C economics block, zone D twelve-cell gates strip, zone H (budget instrument), economics spine **C18:C24** (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC) with G9 freshness state; product reference CVR.
  - **T1 SYNTAX BOARD**: S3 group "Cap status", "Share vs target (pp)".
  - **T2 KEYWORD COMMAND**: K1 (Twin-Set ID, Syntax Tags, Relevancy, SV, Oversight Flag, Coverage State); K2 (Validation State, Clicks 7/30/60d, Sample State, Eligibility, Indexed?, Listing Placement, Targeted Variation, Inventory Band, Days to Stockout, Family Conflict, Event Mode); K5 cross-type totals and "Flag: Zero-Quarantine"; K6 (Max Profitable CPC, Expected CPC $, CPA Ceiling); K7 (Review Date, Test Status); K8 (# Exact, Duplicate Flag, Term Owner (Family)); K9 (VERDICT, Scenario ID(s), Action Source (Finding IDs), Last Cycle Prediction Score, Campaign Moves (prior -> new)). PAUSED-PENDING filter view and pool filter view.
  - **T2 campaign child rows**: "Camp Type (child)", "Camp Objective (child)", "Spend Share of KW %", "Negation State on Term"; clicks per campaign on the term.
  - **T3 CAMPAIGN BOARD**: C2 "Eligibility + Reason", C4 "Spend $ (L30)", C5 "Harvest Yield" and "Graduations (Qtr)", "Truncation Flag (G3)", "In-Budget Bucket", declared role on duplicates, wall baseline.
  - **T5 PRODUCT LOG**: "Trend-Exclusion Flag"; listing change, price move, OOS window, deal window, competitor entry (P9 attribution).
  - **T6 DECISION LOG**: Review Date, Level, V5 Score, Expected Outcome Window, prediction fields.
  - **T7 MANIFEST**: field groups A1, A3, A4, A5, A7, B1, B2, B5, B8, B11, D1, D2, D6, F3; "Verdict Classes Blocked While Missing"; "PACKET COMPLETENESS SCORE".
  - **Account Rollup A2** (budget instrument) and **A4** (structure targets, auto-dominance one-cell read).
- **MKL** (bi-weekly refresh from Brand Management): syntax tags, relevancy scores.
- **D2 variation map** (Economics and Context Pack): keyword-to-variation map with ranked backups.
- **#33 family ownership declaration** with declaration date.
- **#41 economics refresh** feeding T0 C18:C24.
- **#32 armed-window declaration** (dates, named actions).
- **#38 T+1 verification report** and staged change set.
- **SOP-29 wall verification lines**, plus **served-terms scan** (search-term report) for the following window, per source.
- SQP rows (G1 canonical case: Bamboo 4pc broken SQP rows).
- The KDR Cycle File generated Monday from T2 K1-K9.

## 7. Outputs / artifacts

| Record | Storage | Retention | Consumer |
|---|---|---|---|
| **Graduation log** (pass artifact) | KDR Cycle File generated Monday from T2 K1-K9, one frozen row per candidate. Columns: term, sources, evidence, disposition, class, family, seed bid, ceiling, wall points and verification state, prediction, review date | KDR cycle file's; period ungoverned (AM-13) | V5 scoring next cycle; SOP-29 wall audit (wall-point population); operator ramp week-1 artifact |
| **Standup instruction** | Staged #38 change set + T2 K9 "Campaign Moves (prior -> new)" | With #38 staged set | SOP-12 P1/P2 same day; carries class, family, objective, seed bid, ceiling |
| **Source list** | Issued to SOP-29 with approval; recorded on T3 row of each source campaign as wall baseline | With T3 row for campaign's life | SOP-29 P2: one wall per source, one verification line per source |
| **Wall verification lines** | In the graduation log chain record | With graduation log | P5 step 6 close; monthly wall audit |
| **Per-source yield reads** | T3 C5 "Harvest Yield", "Graduations (Qtr)" | Rolling with T3 row | Grades #13, #14, #15; rolls into Account Rollup A4; no v4.0 floor (AM-8) |
| **LEAVE pool report** | T2 rows under PAUSED-PENDING view with K7 Review Date and accumulated evidence; distribution (entries, age bands, oldest age) | Until entry graduates, negates or closes | Next P8; F4 surface |
| **T6 entries** | T6 DECISION LOG, one row per deployed change with prediction, magnitude, horizon, review date | Append-only; never edited, only scored | V5; MISS/WRONG-DIRECTION to P9 |
| **Rejection / route-out records** | Graduation log row with gate fired and owner | With graduation log | Brand Management works MKL decisions (re-entry standard AM-10) |
| **Suppression statement** | Pass artifact header: manifest groups STALE or MISSING and blocked classes | With graduation log | States what the analysis could not see before recommending |
| Staged bulk rows | #38 format, verdict and scenario ID in reason string | | #38 Tuesday deploy |

Skill outputs (Section 9): drafted graduation log; drafted standup instructions in #38 format; drafted source lists to SOP-29; verification reconciliation reports; pool distribution report; per-source yield reads; drafted T6 entries; suppression statement; F1-F12 alarms with evidence lines (row, signal value, gate/rule reference).

Alarm routing: **F1, F3, F5, F6, F8** same day to operator queue (**F5, F6** escalate on first occurrence); **F2, F7, F9, F11, F12** into the weekly pass worklist; **F4, F10** into the pass close.

## 8. Decision rights
- **AI-executable with audit**: queue assembly and dedupe, source-list construction, evidence pooling, gate reads, disposition drafting, class-assignment drafting, chain checklists, verification reconciliation, pool aging reports, yield computation, T6 drafting, suppression statement.
- **Human-mandatory**: every APPROVE, every route-out confirmation, every class assignment on an oversight-class term (Matrix row "Weekly verdicts (established US)", D = PPC Lead); every head-term fast-path standup and every structure creation ("Structure creation (all SOPs)"); every deployment confirm ("Bulk deployments (#38)"); graduations on launch-stage products ("Launch-stage verdicts + batches", D and E = launch operator); any chain on a family-shared term pending a declaration ("Sibling declarations (S-series)"). v4.0 human-review tier applies on top: every 500+ SV keyword action, every gate failure, every structural change, every LOW-confidence verdict.
- Authority Matrix v2.0 rows (Section 11):

| Row | D | E | R |
|---|---|---|---|
| Weekly verdicts (established US) | PPC Lead | Incoming operator (assigned scope), PPC Manager | BM owner |
| Structure creation (all SOPs) | PPC Lead or per SOP scope | Incoming operator, PPC Manager, launch operator (launch and CA scope) | |
| Bulk deployments (#38) | | Incoming operator, PPC Manager | PPC Lead |
| Launch-stage verdicts + batches | Launch operator | Launch operator | PPC Lead, BM owner |
| Sibling declarations (S-series) | PPC Lead | Incoming operator | BM owner |

- Vacancy rule: an unfilled role's D reverts to PPC Lead, E to PPC Manager.
- **Brand Management** owns the MKL classification decision (S-H6); F6 escalates jointly to Brand Management and PPC Lead.
- Operator ramp: Week 1 observation (reproduce WE-1 pooling and yield arithmetic to the cent); Week 2 supervised on one established US product (zero approvals with an unreconciled source list; one failure fails the week); Week 4 unsupervised with PPC Lead auditing (audit samples source-list reconciliation on 3 chains, one wall verification set, yield vs log, one pool distribution); **2 clean audit weeks close the ramp**. Launch-stage and Canada graduations stay outside scope until Matrix rows transfer.
- Escalation: F5 on first occurrence; F1 and F8 on recurrence in same source/session pattern with wall-audit session attribution; F6 on first occurrence to BM + PPC Lead.

## 9. Account-specific facts
- **Bamboo 4pc file**: broken SQP rows (CVR fields zero with orders present) are the canonical G1 case.
- **Satin product cooling terms**: the satin product tracks cooling terms it cannot rank and takes clicks on them. Threshold authority classes this as a pre-load failure plus MKL hygiene failure ("the taxonomy knew and the campaigns did not"). Motivates G12 / F6.
- **Six-piece satin case**: all head-term traffic through auto with zero exacts; the account's named failure class. The **6pc auto-dominance finding** is a one-cell read in **Account Rollup A4**.
- **SOP-29 monthly wall audit incident**: **2 breaches across 41 wall points on 12 graduated terms**, breach rate **4.9%**. Both traced to one creation session where **Auto-Loose** was missed as a source.
- Campaign names in examples: family broad, Auto-Close, Auto-Loose, sibling 6-piece broad, family phrase, Deep Pocket family.
- Ledger dependency **D2** (variation map) is **OPEN** and caps depth of variation/backup specification.
- The copy of SOP-29 attached to the build session was the superseded **v1.0**; the Ledger records #29 at v2.0 with interface contracts I-1/I-2 as the two halves of this chain.
- The live product economics spine was **not attached**; all worked examples use the PPC Economics Worked-Example Set v1.0 training base, **not live data**: AOV **$80.00**, contribution **$28.00**/order, BE ACOS **35.0%**, Target ACOS **17.5%**, Max Acceptable **26.3%** (26.25%), reference CVR **5.2%**, Max Profitable CPC **$1.456** (carried $1.46).

### Worked-example figures (illustrative)
- **WE-1**: Term A "bamboo sheets split king": broad 11 clicks @ $1.72 = $18.92; Auto-Close 6 @ $1.12 = $6.72; pooled 17 clicks, 3 orders, $25.64; blended CPC $1.51; CPA $8.55; ACOS 10.7%; SV 720, oversight Y, seed $1.40, ceiling $1.46; 3 sources (incl. sibling 6-piece broad). Projected CPA 1.40/0.1765 = $7.93. Prediction: exact CPA <= $8.55 within 30 days at CPC <= $1.46. Term B "bamboo sheet set deep pocket king": 9 clicks @ $1.68 = $15.12, 3 orders, CPA $5.04, ACOS 6.3%, SV 210, tail, seed $1.30, family Bamboo campaign 14 to 15 terms. Term C "split king bamboo sheet set": 14 @ $1.50 = $21.00, 2 orders, CPA $10.50, ACOS 13.1%: LEAVE. Yield: family broad $158.00 spend, 2 credited = 1.27/$100; Auto-Close $92.00, 1 credited = 1.09/$100. 4 wall points, 4 confirmed.
- **WE-2**: Auto-Loose missed (source list 3 of 4 = 75%). Auto-Loose CPC $1.94 vs seed $1.40 = $0.54/click premium; 4 clicks = $7.76 spend, $2.16 premium; uncaught 28 clicks and $15.12 per week, $786.24 per year on one term.
- **WE-3**: "cooling bamboo sheets" blended 41 clicks, 3 orders, $63.55, CPC $1.55, CPA $21.18. Groups: Close 12/2/$13.44/$1.12/$6.72; Loose 21/1/$40.11/$1.91/$40.11; Substitutes 5/0/$8.05/$1.61; Complements 3/0/$1.95/$0.65. Seed off blend would be $0.43 too high. "Cooling satin pillowcase": 19 clicks, 3 orders, CPC $1.36, $25.84, CPA $8.61, ACOS 10.8%, refused on G12 (Cooling syntax on Bamboo product, relevancy below bar).
- **WE-4**: stem "split king", 6 members, 4 served: pooled 31 clicks, 4 orders, $47.42, CPC $1.53, CPA $11.86, ACOS 14.8%, seed $1.35. Pool 7 entries, 3 due; "deep pocket king sheets" accumulated 17 clicks, 3 orders, $26.12, CPA $8.71 graduates (SV 340, tail, Deep Pocket family at **27.4% vs 25.0% secondary cap, +2.4pp**, routes anyway); "split king sheets bamboo cooling" holds at 2 orders; "cooling king sheet set" exits on relevancy. Pool closes at 5 entries, oldest 4 windows. Family phrase $71.00, 1 credited = 1.41/$100.

## 10. Open items

### Appendix A amendment items (15)

| Item | Gap | Notes |
|---|---|---|
| **AM-1** | Graduation evidence window: S-H1 / L6 / T1 name no window; G2 7/30/60d buckets are for rate reads only | **Highest priority** |
| AM-2 | "Price class" (SOP-14 P3, SOP-29, SOP-30 v1.0) undefined in v4.0, which carries margin-dollar class THIN <$6 / STANDARD $6-15 / RICH >$15 | Duplicate of #29 AM-2 |
| AM-3 | Oversight second limb (top spend decile) not in v4.0 | |
| AM-4 | LEAVE pool aging rule and re-evaluation interval | |
| AM-5 | Pool distribution alarm bar | Proposal: add to O6 |
| AM-6 | Same-day atomicity clock: Doctrine 3.4 says same day; T6 names no clock; S-H4 says "same cycle" | |
| AM-7 | Dual-source yield credit convention | |
| AM-8 | Graduation-rate floor under O6 | |
| AM-9 | Failed-graduate horizon | |
| AM-10 | Re-entry evidence for routed-out candidate | |
| AM-11 | Gate numbering (G9/G10/G12 vs corpus) | Duplicate of Ledger C9 and #29 AM-11 |
| AM-12 | Element 2 lag table | Duplicate of SOP-17/18/19 item A-7 |
| AM-13 | Record retention (Ledger row 39 "Pending fold-in: retention policy lines") | Duplicate of #29 AM-13 |
| AM-14 | Stem construct absent from v4.0 | |
| AM-15 | Whether S-H1 order count pools across twin set | |

### Ledger conflicts / dependencies
- **C3**: #31 Budget has no procedural document; cite T0 zone H / Account Rollup A2.
- **C9**: gate numbering mismatch (AM-11).
- **C10**: closed vocabulary stated at three different counts.
- **D2**: variation map OPEN.

### Gaps / referenced documents not present
- Live product economics spine not attached to the build session.
- The SOP-29 copy available was superseded v1.0; I-5/I-6 written from the Ledger row.
- No v4.0 signal-to-start lag table.
- Internal inconsistency in Section 2: the registry-conflict trigger points to "P1 step 5 dedupe", but the dedupe is P1 step 7. The MKL-refresh trigger points to "P3 step 4 re-tests gate G12", but G12 is P3 step 1 and P8 step 2.
- Referenced documents: Master PPC Decision Criteria System v4.0; KDR Template v3.0; PPC Strategic Doctrine v1.0 (Sections 3.1, 3.4, 5.1, 11, 13); PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; Command Workbook READ ME; PPC Cross-Reference Ledger; PPC Economics Worked-Example Set v1.0; SOP Build Kit v1.0; Supersession Map; SOP-12, 13, 14, 15, 16, 23, 28, 29, 31, 32, 33, 35, 38, 39, 41.

### Version-governance triggers (beyond monthly review)
Re-validate on any v4.0 increment (S-H1, S-H4, S-H6, S-R12, T6, T1, L6, O6, G2, G11, G12, X10, P5, M1). Specific triggers: (1) any change to S-H1 bar or window (a change to one of S-H1/L6/T1 without the others opens a conflict report); (2) any change to the atomic chain on either side (SOP-29 coupling); (3) any candidate route definition change; (4) D5 completion across the portfolio (F3 becomes a detection sweep); (5) oversight-class definition change incl. AM-3; (6) D2 map landing at full depth; (7) v4.1 resolving any Appendix A item.

### Interface contracts (Section 12) non-arrival consequences
| # | Interface | Non-arrival |
|---|---|---|
| I-1 | SOP-14 P3 Route A rows | Pass runs on what arrived; 2 consecutive passes with spend and zero Route A arrivals escalates to PPC Lead |
| I-2 | SOP-13 P4 stems | P6 does not run; deferral logged |
| I-3 | SOP-15 P3 Route A with tokens | Tokenless rows refused (F3); token-blocked row travels as quarantine note so the pass learns a campaign served the term |
| I-4 | Head-term receipts | Escalates on first occurrence at either end |
| I-5 | Approval + full source list to #29 | Highest-consequence: GRADUATED-UNSTEERED at every omitted source |
| I-6 | #29 verification lines | Chain stays open, F1 fires |
| I-7 | Standup instruction to SOP-12 | SOP-12 returns it (F7) |
| I-8 | T2 K8 registry + child rows (Monday 09:00 packet) | Approvals suspend on affected terms |
| I-9 | #41 economics to T0 C18:C24 | Seed/ceiling PROVISIONAL; approvals continue; re-price at next fresh refresh |
| I-10 | D2 variation map | Standup on preferred SKU with D2-pending flag; G6 flip escalates same day |
| I-11 | MKL from Brand Management | G12 unreadable: no graduation; MKL >30 days degrades manifest |
| I-12 | #33 ownership declaration | G11 holds family-shared terms |
| I-13 | #38 staged set and T+1 | Nothing deploys / chain cannot close; mismatch returns same day |
| I-14 | Yield reads to T3 C5 / Account Rollup A4 | Discovery SOPs ungraded; M6 structure check loses input |
| I-15 | #32 event plan arming | Staging continues, deployment does not; live window with no plan escalates to deals owner |
| I-16 | T6 predictions to V5 | Unlogged change does not deploy; blocks staged set at QA (F11) |

### Failure modes (F1-F12)
F1 wall-less standup; F2 double graduation across sources; F3 validation on blended auto evidence; F4 rotting LEAVE pool; F5 head-term receipt queued; F6 graduation on a term failing G12 (standup reverses, walls stay pending MKL decision); F7 seed bid invented at standup; F8 source list truncated to validating source (distinct from F1: source never on list); F9 standup deployed in armed window without plan naming it (revert; trend-exclusion window extends from revert date; no prior incident); F10 yield credited wrongly; F11 graduation deployed without prediction (block at QA); F12 class assigned on judgment ("caps outrank single-keyword strength"; move via SOP-12 P5/P6).
