# SOP-41 Digest: Margin Table and Economics Refresh

Source: `PPC_SOP_41_Margin_Table_and_Economics_Refresh_v1_0.pdf` (10 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-41: Margin Table and Economics Refresh (PPC Department, Operating SOP, Component #41 of the Operations Definition Register) |
| Version | 1.0 (first build against SOP Build Kit v1.0 12-element standard; first document for component #41) |
| Date | 2026-07-28 |
| Due date honored | 2026-08-21, before Wave 1 opens |
| Owner | PPC Lead |
| Thresholds | Master PPC Decision Criteria System v4.0 only; **zero local thresholds** |
| Content | 12 procedures (P1-P12), 8 failure modes (F1-F8), 4 worked examples; arithmetic asserted programmatically at $0.01 and 0.1 pp tolerances |

**Verdict / purpose.** Every ceiling in the account derives from the margin table, and **today the margin table is one blended row**. The **T0 economics spine reads a single blended B4 figure: contribution $28.37 on AOV $81.05, break-even ACOS 35.0%, version Jun-2026**; so every Max Profitable CPC, Target and Max Acceptable ACOS, push loss ceiling and sibling composite input is computed from an average that is wrong for every variation. This SOP owns: monthly and event-driven refresh of the **D1 per-variation margin table**, validation, version stamping, the **G9 freshness state**, the **repoint of the T0 economics spine from blended to variation-weighted values**, and same-day routing of ceiling recomputation to the **ladder queue** when margin moves. Completing it **clears external dependency D1** (Cross-Reference Ledger Section 2), unblocking **#11 at live depth** and **SOP-23 push sizing** at real margins. It is a **data-stewardship SOP**: issues **no keyword verdicts**; produces states (**G9 fresh, PROVISIONAL, stale, quarantined**) and hands exactly one worklist downstream: the **S-A9 ladder-queue sweep**.

**Authority note (1.1):** attached threshold file is `Master_PPC_Decision_Criteria_System_v4_0.pdf` but internal labels read **3.0** on title page and every footer; program owner ruled **2026-07-28** that it is the governing v4.0 (logged A5). Instrument discrepancies in rule IDs/counts logged as A6; SOP quotes only material verbatim in the attached authority or KDR template (anti-drift rule 2).

## 2. Scope & boundaries

**Owns:** D1 refresh (monthly + event), validation, version stamp, G9 state, T0 spine repoint, ceiling recompute and ladder-queue list, class-flip broadcast, new-variation D1 onboarding, staleness watch, T7 D1 row update.
**Does not own:** setting any band; keyword verdicts; touching bids; manifest structure; push sizing; sibling composites/declarations; envelope decisions; RE-POINT VARIATION execution; worked-example arithmetic.

| Adjacent component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every band, class boundary, gate rule, ceiling formula (margin-dollar classes, return-rate bands, 50% and 75% BE lines, G9 price-stability window, O3 THIN bar, S-A9 recompute order). SOP executes, never sets a band. |
| #11 Economics worked-example set | Owns training arithmetic cases **E1-E8**. SOP never restates them; Element 11 sends operator to #11. |
| #39 Data feed & manifest operations | Owns feed definitions and T7 field-group scheme. SOP updates T7 D1 row as output. |
| SOP-23 Ranking-push operations | Consumes margin in **M2** sizing; SOP guarantees figure + freshness state only. |
| SOP-12 Exact campaign operations | Executes bid steps from S-A9 sweep. SOP hands queue; never touches a bid. |
| #33 Sibling arbitration | Consumes per-sibling margin per order with source state (SOP-33 Section 3). Composite and declaration live there. |
| #31 Budget & envelope | Envelope raises/cuts from margin change are envelope decisions in #31 instruments (per **Ledger conflict C3**: cite instrument, never #31 procedure number). |
| D2 keyword-variation map | Tab 2 of Economics & Context Pack, owned by **Logistics plus Catalog** per Pack READ ME. SOP reads ACTIVE-variation roster only; RE-POINT VARIATION belongs to **SOP-12 P10**. |
| #3 Authority Matrix | No v2.0 row for #41 refresh decisions; interim assignment from Context Pack ownership lines (A8). |

## 3. Triggers

Four of five carry same-day / same-session lag.

| Trigger | Detecting artifact | Max lag / procedure |
|---|---|---|
| Monthly refresh due | D1 tab **Version** column vs calendar month; **T7 D1 row Refresh field reads Monthly**. v4.0 "F1 Product Economics" contribution row: "Computed monthly from SellerBoard + finance; FIFO landed-cost basis." | P1 opens on Finance delivery; completed refresh lands **before next Monday 09:00 packet-ready read** (slot belongs to #4) |
| Margin-moving event | **T5 Product Log** and Context Pack **EVENT INTAKE** sheet, closed event types **"Price move"** and **"Fee/dimension change"**; Finance COGS change notice routes through same intake | **Same day.** S-A9: "All ceilings recompute immediately from the new margin table ... Ceilings are live values, not annual settings." **P9** opens day event lands |
| Return-rate band change | SellerBoard true-up read vs v4.0 F1 return-rate bands (LOW <4%, NORMAL 4-8%, HIGH 8-12%, SEVERE >12%) | Same session; re-opens **P2** for affected variation. SEVERE also freezes scale on variation per F1 and routes cause to product team |
| New ACTIVE variation | D2 map roster and listing registry: variation in D2 or in campaign targeting with no D1 row | **P10** before any ceiling-referencing verdict, ahead of first weekly pass reading the variation; until row exists, actions carry **G9 PROVISIONAL** per **SOP-12 B8 precondition** |
| Staleness clock expiry | **T7 D1 row Status** column vs **45-day version-age clock** (A1: from Data Architecture v1.0 Section 3, not yet in v4.0) | Same day: **P11** flips state, opens Finance task, tags downstream reads |

## 4. Procedures

### Preconditions & gates (Element 3)
Refresh runs only on validatable inputs; failure leaves prior version in force.

| Gate (manifest ID) | Requirement / passing observable |
|---|---|
| D1 delivery present (T7 row "D1 Per-variation margin") | Finance delivery via **P1.6 CM waterfall** covers every ACTIVE variation row. Observable: zero ACTIVE rows with blank Contribution $/unit after P4. Partial legal but G9 stays PROVISIONAL (Pack READ ME clearance rule) |
| Input validity (G1 pattern) | Contribution $/unit = AOV - COGS - FBA fee - referral - freight-in (freight = 0 if blank, per D1 header). Computed matches delivered within **$0.01**. Two values for one metric quarantines row (G1); prior version stays |
| Valuation consistency (Pack READ ME F1 check) | Freight-in treatment matches across valuation contexts; D1 uses landed unit economics. Cover note states freight basis; basis change = P2 finding, never silent absorb |
| Return-rate basis stated | Delivery states whether net of returns. Data Architecture Section 3 specifies D1 as post-returns; live blended row derives from net revenue -> standing convention **net-of-returns**. D1 tab has no return-rate column (A4). Cover note basis line reads net-of-returns |
| B8 economics chain live (T7 row "B8 Row economics") | T0 named cells **AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope at C18:C24** resolve without error before/after repoint; zero #REF/#VALUE after P6 |
| Completeness honesty (G8, F15) | T7 updated before downstream analysis: **FULL >=95%, WORKABLE 85-95%, DEGRADED <85%** of gate-relevant fields; DEGRADED = flags only. T7 D1 Status & completeness reflect refresh before Monday cascade |
| Price stability awareness (G9) | Price change on variation within **trailing 7 days** marks CVR & ACOS reads PROVISIONAL. Ceiling recomputes same day regardless. Refresh log lists variations with G9 price flag |

Time estimates assume one product, up to **10 ACTIVE variation rows**, scale roughly linearly (operating estimates, not thresholds). P1-P8 monthly spine; P9-P11 off-cycle; P12 closes every run.

### P1. Monthly intake & delivery check (15 min)
1. Open Economics & Context Pack, **D1 MARGIN TABLE** tab; confirm current Version stamp & Effective Date (live: **Jun-2026, 2026-06-30 on B4 blended row**).
2. Receive Finance delivery: per-variation **P1.6 CM waterfall** output, one line per ACTIVE variation: **AOV $, COGS $/unit, FBA fee $/unit, referral $/unit, freight-in $/unit, stated contribution $/unit**, on FIFO landed-cost basis.
3. Pull **SellerBoard monthly true-up** (financial source of truth per Data Architecture Section 12); hold beside delivery.
4. Roster check vs **D2 tab**: every ACTIVE variation in D1 plus every preferred or backup SKU in D2 must appear. Missing = partial delivery: proceed on received rows, list missing in P12 log, G9 PROVISIONAL.
5. Cover note must state freight-in basis and returns basis; missing either -> back to Finance same day with two-line request; nothing proceeds until stated.

### P2. Row validation (15 min)
1. Recompute contribution identity per row; compare at **$0.01** tolerance.
2. Identity failure -> **quarantine** (G1): row doesn't write; prior version's row (or blended row on first fill) stays; repair task to Finance same day; record carries **FLAG: DATA REPAIR**.
3. **Referral sanity:** referral $/unit / AOV should sit at category referral rate; off-rate = query to Finance, not an edit. Operator never edits a delivered value.
4. Reconcile product-level total vs SellerBoard true-up: variation contributions weighted by ordered units reconcile to SellerBoard product contribution within month's mix noise; material gap = P2 finding naming largest contributing row.
5. Return-rate read per variation from true-up, banded per F1; band change recorded in row Notes; **SEVERE** -> scale freeze + listing-quality diagnosis to product team; escalated in P12.

### P3. Class banding & band-change detection (5 min)
1. Margin-dollar class per F1: **THIN < $6, STANDARD $6-15, RICH > $15** per unit.
2. Compare to prior class; every change is a P8 broadcast item. F1 bars THIN variations from Ranking objectives on terms whose **Expected CPC > margin $ / 3** (O3 realism input).
3. Record **clicks-to-loss = margin $ / reference CPC** as row's tolerance line (display arithmetic, not a threshold).

### P4. Version stamping & D1 write (10 min)
1. Write validated rows into D1: one row per variation, **blue input cells only, formulas untouched**; Contribution $ and % compute in-sheet; confirm match P2.
2. Every written row same Version (month label) and Effective Date. **Mixed stamps inside one refresh illegal; refresh atomic per product.**
3. Blended row stays, marked blended, for reconciliation trail; after first full per-variation fill never again spine source.
4. **Never fork the table**: one editable D1 per product in Economics & Context Pack (Data Architecture design rule 2). Second editable location = F3.

### P5. G9 state evaluation (5 min) - first match wins
1. **QUARANTINE:** any ACTIVE row failed P2 -> those variations stay on prior version; product G9 stays PROVISIONAL; repair task carries release condition.
2. **CLEAR:** every ACTIVE row has Contribution $/unit and Version stamp, no quarantines, version age inside staleness clock -> G9 clears (Pack READ ME: "G9 flips from PROVISIONAL when every ACTIVE variation row carries Contribution $/unit and a Version stamp"); spine repoints in P6.
3. **PROVISIONAL:** >=1 ACTIVE row blank -> G9 PROVISIONAL; ceiling-referencing actions tagged (SOP-12 B8); missing rows named in T7.
4. **STALE:** no delivery and age past **45 days** (A1) -> P11; T7 D1 row STALE; escalation opens.

### P6. Spine repoint (10 min)
1. On G9 CLEAR, repoint T0 spine named cells **(C18:C24)** from blended row to variation-weighted values.
2. Weighting basis: **trailing 30-day ordered units per variation** from SellerBoard true-up (proposed here; A2). Basis written into spine's source note every refresh.
3. Recompute **M1 chain**: **BE ACOS = margin / AOV; Target = 50% of BE; Max Acceptable = 75% of BE** (formula cells; check they moved).
4. Per-variation ceilings flow to **T2 K6 economics block** via D1 link; confirm one oversight-class keyword row shows new per-variation Margin $/unit for its targeted variation.
5. Update **T0 zone C "Margin table version"** line and G9 state display same session (stale line = F1).

### P7. Ceiling recompute & ladder-queue sweep (20 min)
1. Execute S-A9: "All ceilings recompute immediately from the new margin table; every keyword whose CPC is above its new ceiling enters the ladder queue this cycle."
2. Filter T2 to rows where blended CPC > row's new **Max Profitable CPC = margin $ of targeted variation x row CVR** (F1). CPC ratio bands: **<=0.8x SAFE; 0.8-1.0x AT-CEILING; 1.0-1.5x PUSH-ONLY; >1.5x UNJUSTIFIABLE** outside a sized push.
3. Rows above ceiling with live **M2-sized push record** stay in push governance. Rows above ceiling with **no sizing record** enter ladder queue with **BID DOWN TO PROFITABLE CPC; CAP SYNTAX** (issued by v4.0, executed by SOP-12; SOP produces list only).
4. Hand queue to weekly pass with refresh version stamp so each bid step's reason string names the margin version.

### P8. Class-flip & eligibility broadcast (10 min)
1. Per P3 class change, notify objective owner in one line: into THIN arms F1/O3 bar; out of THIN releases it; return rate into SEVERE freezes scale.
2. Terms on newly THIN variation carrying Ranking objective flagged to weekly pass for O3 objective review (review/transition is v4.0 & SOP-12).
3. Notify #33 that per-sibling margin inputs changed, with G9 state (SOP-33 Section 3); re-arbitration on margin driver is **SOP-33 P6**.

### P9. Event-driven off-cycle refresh (25 min)
1. Trigger: T5 or EVENT INTAKE row of type Price move, Fee/dimension change, or Finance COGS notice touching ACTIVE variation.
2. Run P2-P7 for affected variations only, same day. Unaffected rows keep stamp; affected take **event-dated stamp** with event reference in Notes.
3. Price moves also arm **G9 price stability for trailing 7 days**: CVR & ACOS PROVISIONAL; ceiling recompute proceeds same day ("two clocks").
4. If event landed late (found in weekly read rather than within Pack's **24-hour intake window**), count & log days late in P12; route intake miss to intake owner.

### P10. New-variation onboarding (10 min)
1. Trigger: variation reaches ACTIVE in listing registry or appears in D2 as preferred/backup SKU with no D1 row.
2. Open D1 row with identity fields (**SKU, size, color, Status**) same day; request Finance line in next delivery or immediately if campaigns target sooner.
3. Until filled: G9 PROVISIONAL on every ceiling-referencing action; T7 D1 row names pending variation; **never given blended figure as its own**.

### P11. Staleness watch & escalation (5 min weekly)
1. Weekly in Monday manifest update: **version age = today - Effective Date**. Past **45 days** -> T7 D1 Status STALE, product's ceiling-referencing verdict classes PROVISIONAL, Finance task same day with age counted.
2. STALE never blocks weekly pass; changes what it may claim. If D1 absence pushes gate-relevant completeness **below 85%**, economics-dependent verdicts downgrade to flags.
3. Releases only via completed P1-P6 run; **no manual un-stale**.

### P12. Record close (10 min)
1. T7: update D1 row (Status, note naming missing variations/quarantines); let completeness recompute before cascade.
2. **T6 decision log** one entry per refresh: prior & new spine values (**MarginPerOrder, BE_ACOS**), version stamp, count of ladder-queue rows handed, class flips broadcast, quarantine list. Record, not prediction.
3. **KDR header**: next cycle file carries new **Margin Table Ver.** in its Gates block.
4. Escalate to PPC Lead with T6 history: SEVERE return band; repeated quarantines from same source; **second consecutive missed monthly delivery**.

## 5. Rules, thresholds & numbers

### 5.1 v4.0 rule references
| Rule / section | Meaning as described |
|---|---|
| F1 Product Economics | Contribution computed monthly from SellerBoard + finance; FIFO landed-cost basis; margin-dollar classes; return-rate bands; max profitable CPC = margin $ x CVR; CPC ratio bands; clicks-to-loss field; returns adjustment precedes every ceiling ("Adjusts margin to reality before any ceiling is computed"); SEVERE freezes scale |
| M1 (Layer 5 Sizing Mathematics M1-M10) | BE ACOS = margin / AOV; Target = 50% BE; Max Acceptable = 75% BE |
| M2 | Push sizing (SOP-23) |
| G1 (Layer 0 Gates G1-G12) | Two values for one metric -> quarantine |
| G8 / F15 Verification & Data Quality | FULL >=95%, WORKABLE 85-95%, DEGRADED <85% of gate-relevant fields; DEGRADED = flags only |
| G9 | v4.0 heading "Price stability (new)": price change in trailing 7 days -> CVR/ACOS PROVISIONAL. Instruments also use G9 for margin freshness (dual use, A3) |
| O3 (Layer 1 Objective Assignment O1-O8) | Realism input: THIN variation barred from Ranking objective where Expected CPC > margin $ / 3 |
| S-A9 (8.1 Product-Level Scenarios) | All ceilings recompute immediately from new margin table; every keyword with CPC above new ceiling enters ladder queue this cycle; ceilings are live values |
| 13.1 Closed Verdict Vocabulary | 18 actions declared (vs 25/26 elsewhere, A6) |
| J7-class honesty rule | Flags state fallbacks in the words the engine computed (F4 response) |

### 5.2 Numeric values
| Item | Value |
|---|---|
| Contribution identity tolerance | $0.01 |
| Worked example assertion tolerances | $0.01 and 0.1 pp |
| Margin-dollar class | THIN < $6; STANDARD $6-15; RICH > $15 per unit |
| Return-rate bands | LOW <4%; NORMAL 4-8%; HIGH 8-12%; SEVERE >12% |
| O3 THIN bar | Expected CPC > margin $ / 3 |
| BE / Target / Max Acceptable | BE = margin/AOV; Target 50% BE; Max Acc 75% BE (25-point gap below BE) |
| CPC ratio bands (CPC / ceiling) | <=0.8x SAFE; 0.8-1.0x AT-CEILING; 1.0-1.5x PUSH-ONLY; >1.5x UNJUSTIFIABLE outside sized push |
| Completeness bands | FULL >=95%; WORKABLE 85-95%; DEGRADED <85% |
| G9 price-stability window | Trailing 7 days |
| Staleness clock | 45 days version age (A1, from Data Architecture v1.0 Section 3) |
| Spine weighting basis | Trailing 30-day ordered units (A2, proposed) |
| Event intake routing window | 24 hours (Pack READ ME) |
| Monthly landing deadline | Before Monday 09:00 packet-ready read |
| T0 spine named cells | C18:C24 |
| Time estimate basis | 1 product, up to 10 ACTIVE variation rows |
| Durations | P1 15; P2 15; P3 5; P4 10; P5 5; P6 10; P7 20; P8 10; P9 25; P10 10; P11 5 weekly; P12 10 (minutes) |
| Escalation | Same failure twice in consecutive refreshes -> PPC Lead; SEVERE / recurring quarantine same source / 2nd consecutive missed monthly -> same day |

### 5.3 State mapping (Element 5)
| Refresh outcome | State set | Verdict classes affected |
|---|---|---|
| Full validated fill, all ACTIVE stamped | G9 CLEAR; spine variation-weighted | Ceiling-referencing classes shed PROVISIONAL; **RANK PUSH: FUND SIZED PUSH** (KDR v3.0) prices from real margin in M2 |
| Partial delivery | G9 PROVISIONAL, missing rows named in T7 | Ceiling actions tagged (SOP-12 B8); nothing halts |
| Row identity failure | Row quarantined; prior version governs | **FLAG: DATA REPAIR** (v4.0 13.1): repair task owner/date, no recommendation on row economics |
| Impossible/conflicting source read (delivery vs true-up) | G1 quarantine at intake | **QUARANTINE: DATA REFRESH** (KDR v3.0 Bands & Verdicts Reference): data-refresh task same day, no publish |
| Ceilings recomputed, rows above with no sizing record | Ladder queue populated (S-A9) | **BID DOWN TO PROFITABLE CPC; CAP SYNTAX** (v4.0 13.1); executed by SOP-12 |
| Inventory-driven target change in roster check | Out of scope; routed | **RE-POINT VARIATION** (v4.0 13.1) belongs to SOP-12 P10 on D2 instruction |
| Version age past clock | STALE; PROVISIONAL tags | Per G8/F15 DEGRADED completeness downgrades to flags |

### 5.4 Failure modes F1-F8
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Refresh lands, spine not repointed | T0 zone C margin version != D1 Version stamp | P6 immediately; re-read gap verdicts; log gap length in days |
| F2 | Ceilings recomputed, ladder sweep skipped | Ladder-queue count 0 in T6 while T2 shows rows above new ceiling w/o sizing | P7 re-runs, same stamp; quote S-A9 in entry |
| F3 | Parallel margin copy | Margin editable outside D1 (pasted table, hardcoded spine cell) | Delete copy, restore reference (design rule 2); origin to change control |
| F4 | Stale margin, untagged verdicts | T7 D1 STALE/PROVISIONAL while ceiling records unflagged | Re-tag this cycle (J7 honesty rule); process finding |
| F5 | Freight basis mismatch | P2 identity fails systematically one direction, or cover note basis changes | Quarantine delivery as a whole; reconcile with Finance per Pack F1 check |
| F6 | Pre-returns margin used | Contribution reconciles to gross not net revenue | Return for net basis; log under A4 |
| F7 | Class flip not broadcast | THIN variation carries Ranking objective on term with Expected CPC > margin/3 after flip | P8 re-run; O3 review; miss scored vs refresh entry |
| F8 | Variation live with no margin row | Variation in targeting or D2 with no D1 row | P10 same day; PROVISIONAL; never blended |
F1-F4 are the **June 30 review's finding** (ceilings ran on blended economics account-wide) decomposed.

## 6. Data inputs required

- **Economics & Context Pack v1.0** (per product):
  - **D1 MARGIN TABLE tab**: columns incl. Version, Effective Date, Status (ACTIVE), SKU, size, color, AOV $, COGS $/unit, FBA fee $/unit, referral $/unit, freight-in $/unit (0 if blank), Contribution $/unit, Contribution % (in-sheet formulas), Notes; blue input cells; B4 blended row. **No return-rate column** (A4).
  - **D2 KW-VARIATION MAP** (Tab 2): ACTIVE-variation roster; preferred and backup SKUs.
  - **EVENT INTAKE** sheet: event types "Price move", "Fee/dimension change"; Finance COGS notices.
  - **Pack READ ME**: G9 clearance rule, F1 valuation consistency check, ownership lines, 24-hour intake routing.
- **Finance P1.6 CM waterfall delivery file** (per-variation, FIFO landed-cost) with **cover note** stating freight-in basis and returns basis (net-of-returns).
- **SellerBoard monthly true-up export**: product contribution, per-variation ordered units (trailing 30 days), per-variation return rates; net vs gross revenue reconciliation.
- **Category referral rate** (for referral sanity ratio).
- **PPC Command Workbook:**
  - **T0** named cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope (C18:C24); **T0 zone C** "Margin table version" line + G9 state display
  - **T2** keyword rows: blended CPC, CVR, targeted variation, **K6 economics block** (Margin $/unit), Expected CPC, objective tag, M2 sizing/push record
  - **T5 Product Log** (Price move, Fee/dimension change)
  - **T6 decision log** (prior refresh entries)
  - **T7 manifest**: D1 row (Status, Refresh field, notes), B8 Row economics row, completeness score
- **Listing registry** (variation reaching ACTIVE); campaign targeting (variations targeted).
- **KDR cycle file** Gates block "Margin Table Ver." column.
- **Raw Pull Pack Additions v1.0**: not received (A7); bindings pending.
- Reference CPC (for clicks-to-loss).

## 7. Outputs / artifacts

Five artifacts close every run ("a refresh without all five did not happen").

| Artifact | Storage | Retention | Consumer |
|---|---|---|---|
| Versioned D1 rows (stamp + effective date) | Economics & Context Pack, D1 MARGIN TABLE tab | All versions retained; superseded rows archived in-tab by stamp | T0 spine, T2 K6, KDR Gates block, #33 A1 composite inputs, SOP-23 M2 |
| G9 state record | T0 zone C version line + T7 D1 row | Current live; history via T6 | Every ceiling verdict class; SOP-12 B8 |
| Refresh log entry (prior/new MarginPerOrder & BE_ACOS, version stamp, queue count, class flips, quarantine list, variations carrying G9 price flag, missing rows, days late, weighting basis) | T6 decision log, append-only | Permanent | Weekly audit scoring pass; escalation reviews |
| Ladder-queue handoff list (version-stamped) | Weekly pass worklist (T2 filter + list attached to T6 entry) | Until executed or superseded | SOP-12 P3/P11 execution; #31 instruments where syntax caps bind |
| Class-flip & eligibility notices (one-line) | To objective owners; mirrored in T6 | Permanent via T6 | O3 objective reviews; #33 re-arbitration triggers |
Also: Finance repair/delivery tasks (drafted); F1-F8 alarms with evidence lines (row, signal value, rule reference); spine source note with weighting basis.

## 8. Decision rights

- Authority Matrix v2.0 has **no #41 row** (A8). Interim: **PPC Lead confirms**; nearest row "Weekly verdicts (established US)", D = PPC Lead. **Finance owns input values** per Pack READ ME, never overridden in-sheet. D2 owned by Logistics plus Catalog. Intake owner: BM / Data Ops (24-hour routing).
- **Human-mandatory:** accepting any delivery that changes a published ceiling (**spine repoint confirm**, human-mandatory regardless of seniority); quarantine release after repair; **first unblended fill per product**; every escalation send.
- **AI-executable with audit:** identity & reconciliation checks, class banding, age computation, T7/T6 drafting, sweep-list drafting, notice drafting.
- Operator never edits a delivered value.
- Operator ramp: Week 1 reproduce all eight #11 computations cold, walk D1/T0/T7/T6, state current G9 state; Week 2 supervised P1-P8 + simulated P9 and P10 on copies; Week 4 unsupervised, PPC Lead audits (5 artifacts, sweep count reconciles to T2 filter, every flip broadcast, every quarantine has release condition).

## 9. Account-specific facts

- **Live blended B4 spine:** AOV **$81.05**, contribution **$28.37**, BE ACOS **35.0%**, version **Jun-2026**, effective **2026-06-30**. Blended ceiling at CVR 5.2% = 28.37 x 0.052 = **$1.48**.
- **June 30 review** found ceilings ran on blended economics account-wide.
- No live per-variation data exists yet; all per-variation figures in WE are illustrative; order shares 38/44/18% illustrative.
- **WE-1 (illustrative):** KING AOV $96.00, COGS $34.20, FBA $14.10, referral $14.40, freight $2.10 -> $31.20 (32.5%), RICH; QUEEN $78.00/$30.10/$12.60/$11.70/$1.90 -> $21.70 (27.8%), RICH; TWIN $52.00/$25.60/$10.90/$7.80/$1.90 -> $5.80 (11.2%), THIN. Referral 15.0% of AOV. Return rates 3.8% LOW, 4.6% NORMAL, 5.1% NORMAL. TWIN O3 bar at 5.80/3 = **$1.93**. Stamped Jul-2026. Weighted contribution **$22.45**; weighted AOV **$80.16**; new BE **28.0%** vs blended 35.0% (blended ceilings 25% too loose, 35.0/28.0 = 1.25); Target 14.0%, Max Acc 21.0%. Ceilings at CVR 5.2%: KING $1.62, QUEEN $1.13, TWIN $0.30 (blended 4.9x too loose for TWIN, too tight for KING). TWIN term CPC $0.72 = 2.4x -> UNJUSTIFIABLE -> ladder queue.
- **WE-2:** KING FBA fee $14.10 -> $16.85; Finance stated $29.90 vs identity $28.45 (diff $1.45) -> quarantine, FLAG: DATA REPAIR; confirmed $28.45 (29.6%), RICH; ceiling $1.48; spine $21.40, BE 26.7%. Keyword **"bamboo sheets king"** CPC $1.85 = 1.25x -> PUSH-ONLY with no push -> ladder queue BID DOWN TO PROFITABLE CPC; CAP SYNTAX.
- **WE-3:** Jun-2026 stamp, 2026-06-30; July delivery missed; clock expires **2026-08-14**; STALE flip, Finance task age 45.
- **WE-4:** QUEEN reprice $78.00 -> $69.00; referral $10.35; contribution $14.05 (20.4%); RICH -> STANDARD; ceiling $0.73 vs prior $1.13 (QUEEN terms $0.73-$1.13 sweep in); CVR/ACOS PROVISIONAL 7 days; spine $18.04, weighted AOV $76.20, BE 23.7%.
- Product appears to be bedding (KING/QUEEN/TWIN sizes; bamboo sheets) - per example keyword.
- Dependency D1 clears on completion, unblocking #11 live depth and SOP-23.

## 10. Open items

| ID | Amendment item (v4.1) |
|---|---|
| A1 | 45-day margin staleness clock exists in Data Architecture v1.0 Section 3 (Economics & Context Pack row: "version-dated, 45-day G9 staleness clock") but not v4.0; adopt into F1 or G9 |
| A2 | Spine repoint "variation-weighted values" with no weighting basis in corpus; SOP uses trailing 30-day ordered units; v4.1 to fix |
| A3 | G9 heading "Price stability (new)" while instruments (T0 zone C, Pack clearance rule, SOP-12 B8) use G9 for margin freshness; dual use of one ID |
| A4 | D1 schema has no return-rate column though Data Architecture specifies post-returns and F1 requires returns adjustment |
| A5 | Threshold file internal labels read 3.0 under v4_0 filename; ruled governing v4.0 on 2026-07-28; correct labels |
| A6 | Closed-vocabulary count conflict: v4.0 13.1 = 18; KDR v3.0 and SOP-12 v2.0 = 25; Data Architecture (rule 8) and Command Workbook REFERENCE header = 26 over 25-item validation list |
| A7 | Raw Pull Pack Additions v1.0 (Tier 2 item 3) not attached; Element 9 bindings unverified |
| A8 | Authority Matrix v2.0 has no #41 row |

**Conflicts:** Ledger conflict **C3** (#31 cite instrument not procedure).

**Interface contracts (7):**
| Direction | From -> To | Artifact/timing | On non-arrival |
|---|---|---|---|
| Up | Finance (P1.6) -> PPC Lead | Per-variation delivery + cover note, monthly | G9 PROVISIONAL; 45-day clock to STALE; escalate on 2nd consecutive miss; ceilings hold at last stamp |
| Up | Data Ops -> PPC Lead | SellerBoard monthly true-up | Refresh on Finance alone; P2 reconciliation & return banding deferred, named in T6/T7 |
| Up | Intake owner (BM/Data Ops, 24h) -> PPC Lead | T5/EVENT INTAKE rows | S-A9 fires late; days late logged; ceilings corrected retroactively; gap verdicts re-read |
| Down | PPC Lead -> T0, T2 K6, KDR | Repointed named cells & version line before Monday 09:00 | F1; cascade on old spine; gates-only on economics rows once detected |
| Down | PPC Lead -> #11 & SOP-23 | Cleared D1 | #11 stays on fictional training base; SOP-23 PROVISIONAL |
| Down | PPC Lead -> #33 (Rollup A1) | Per-sibling margin with source & G9 state | Composites on last stated values; margin-driver re-arbitration when fresh lands |
| Down | PPC Lead -> Data Ops (T7) | D1 manifest row each refresh | G8 misstates; same-day correction; affected verdicts re-read as flags |

**Review triggers:** v4.0 change to F1, M1, G9, G8, O3, S-A9 (re-validate Sections 2-7); Pack schema change (P2, P4); Finance P1.6 or accounting provider change (P1, Section 12); SellerBoard replacement; adoption of A1/A2; arrival of Raw Pull Pack Additions v1.0.

**Named documents not present:** Master PPC Decision Criteria System v4.0; Economics & Context Pack v1.0; Master PPC Data Architecture v1.0; #11 Economics Worked-Example Set; SOP-12, SOP-23, SOP-33, #31; Cross-Reference Ledger; SOP Build Kit v1.0; Raw Pull Pack Additions v1.0 (explicitly not received).
