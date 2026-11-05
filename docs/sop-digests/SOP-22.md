# SOP-22 Digest: Launch-Stage PPC Operations and the Launch-to-KDR Handoff

Source: `PPC_SOP_22_Launch_Stage_and_KDR_Handoff_v2_0.pdf` (18 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-22: Launch-Stage PPC Operations and the Launch-to-KDR Handoff (Component #22 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-07 |
| Owner | PPC Lead for PPC execution, jointly with the launch department for the plan this SOP executes inside |
| Supersedes | SOP-22 v1.0 (2026-07-24) in full; absorbs the scheduled Launch-to-KDR Handoff Map deliverable |
| Thresholds | Criteria System v4.0 only; zero local thresholds. Every launch-stage value v4.0 does not govern is named in Section 13 (AM-1 to AM-16), never written into a procedure |

**Verdict / purpose.** Launch-stage PPC buys an organic flywheel with **sequenced, batched, deliberately unprofitable traffic**. It is the only stage where the governing threshold set is incomplete. The discipline that replaces the missing numbers is **artifact verification**: every gate passes on a named artifact held by a named role, never on a judgment that a condition "looks met."

Two failure classes account for the stage's cost:
1. **Deploying every campaign type at once**, which turns a sequenced purchase into unpriced risk.
2. **The handoff seam**: a product graduating without a co-signed packet arrives in the standing cycle blind, and the standing system pays the launch spend again to relearn what launch already knew.

v2.0 expands v1.0:
- procedures 7 to 13
- failure modes 6 to 12
- worked examples 1 to 4
- from a 5-row table of locally invented strings to the full 25-verdict closed vocabulary, quoted verbatim
- adds Element 11 (operator ramp) and Element 12 (interface contracts)

### 1.1 What this SOP owns
PPC execution inside the launch department's plan, across 7 surfaces:
1. Phase 1 standup and its batch-1 deployment session
2. The honeymoon daily block
3. The batch progression pass and its envelope-neutral funding rule
4. Phase 2 discovery entry and its condition-artifact verification
5. The product-type overlay (when placement premiums may be tested)
6. The launch weekly audit interface
7. The Launch-to-KDR Handoff Map, which moves a graduating product into the standing system with a **zero-day orphan window**

Closing artifact: the co-signed handoff line in the Command Workbook T6 Decision Log with the first standing cascade attached.

### 1.2 Phase-condition dependency (critical)
- v1.0 and the Ledger row for #22 direct phase definitions and graduation conditions to "v4.0 Sections 3 and 9." In v4.0, Section 3 is "Layer M: The Master Metric Criteria Dictionary (F1-F16)" and Section 9 is "Layer 4: The Lever Library (L1-L10)". **Neither carries phase definitions, Phase 2 entry conditions or graduation conditions.**
- Section 11 "Layer 6: Transitions, Stages, Modes (T1-T8) and Recovery Mode (R1-R6)" rule **T2**: "the Launch/Scale graduation criteria and Phase 1-4 model stand." It names 5 dimensions without values: **profitability, organic sales %, review posture, CVR stability, TACOS vs CM2**.
- Section 17.2 "Supersession note (per V3)" assigns the stage/phase framework to the **Master PPC Decision Criteria System v1.0 of March 2026, which is not held in this corpus**.
- Treatment: like SOP-27 handles LTSF tier declaration under conflict **C6**. Execute fully once a condition is declared met; never infer condition values; name the declaring artifact and owner at every gate. Until v4.1, every phase and graduation gate passes on the **launch department's plan values**, with source and version recorded in the phase-advance record.

## 2. Scope and boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, gate, scenario, lever limit, sizing rule, verdict string |
| The launch department | Owns the launch plan, strategy, audits, and the keyword research producing batch lists with indexing status and product-type classification. This SOP never authors the plan |
| #23 Ranking push | Owns push sizing math, the DSTR / required-clicks worksheet, pacing on funded pushes, taper triggers. Launch runs batched mini-worksheets under its rules |
| #12 Exact operations | Exact creation, naming, class assignment, taper execution, duplicate consolidation. Every batch and Halo exact stands up through SOP-12 P1 or P2 |
| #13 / #14 / #15 | Phrase, broad, auto mechanics. This SOP decides only when Phase 2 entry is verified, not how campaigns are built |
| #29 Negation | Doctrine, wall-level selection, wall audit. This SOP requires walls at every structure event in the same session and records the list |
| #30 Harvest | Decides graduation. Launch products enter its weekly pass from the first Monday of Phase 2 |
| #28 Placement | Ladder derivation, exit-bid discovery, modifier sizing. The P8 overlay decides when a placement test is legal; #28 sizes it |
| #38 Bulk mechanics | Staging, upload, T+1. Launch urgency never bypasses staging |
| #32 Deal/event windows | Launches do not go live inside an armed window on the parent brand unless the plan names the launch |
| #33 Sibling arbitration | Declaration on shared terms. A shared head term with a live sibling is a portfolio decision first |
| #31 Budget and envelope | Funding queue and envelope law. Per conflict **C3** it has no procedural document, so the instrument layer is referenced: **T0 zone H** and **Account Rollup A2**. No #31 procedure number is cited |
| #41 Margin table | Per-variation margin refresh and freshness. Launch runs on a provisional spine by design and is upgraded at handoff |
| #36 Weekly audit | Receives the product at co-sign; from then the standing T0 to T2 cascade governs and this SOP is silent |

## 3. Triggers
A trigger detected later than its allowance is logged in T6 as a process miss with the delay in days.

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Launch scheduled | Launch dept dated plan with batch-1 list | Same day | P1 |
| Readiness clear | P1 checklist evidenced, countersigned by launch operator | 2 days | P2 |
| Product go-live | Offer live and buyable; batch-1 indexed for the D2 preferred variation | Same day | P3 (day 0) |
| Honeymoon open | Standup record with dated honeymoon exit | Daily | P4 |
| Batch mark reached | Batch calendar entry in T5 Product Log (plan cadence, recorded not derived) | 1 day | P5 |
| Progression closed | P5 log (held/continued/failed + available funding) | 1 day | P6 |
| Phase 2 requested | Launch operator request with condition artifact set | 2 days | P7 |
| Product type declared | Plan's subjective / non-subjective classification | At standup | P8 |
| Weekly audit lands | Launch dept weekly audit document | 1 day | P9 |
| G6 flips YELLOW/RED | T2 block K2 Inventory Band and Days to Stockout on the targeted variation | Same day on RED | P4 step 5; re-point via SOP-12 P10 |
| Graduation claimed | Launch operator declaration with graduation artifact set | 2 days | P10 |
| Packet complete | P10 checklist at 11 of 11 | Same week | P11, P12 |
| Co-sign lands | Countersigned T6 handoff line with first cascade | 30 days | P13 |
| T7 drops DEGRADED | T7 completeness below 85% of gate-relevant field groups | Same day | All verdict-issuing procedures downgrade to flags |

## 3b. Preconditions and gates
Per v4.0 Section 12 rule **P1**, gates outrank diagnosis and diagnosis outranks signals. Conflict **C9**: the corpus and v4.0 assign different meanings to G9, G10, G12, so each gate is named by its v4.0 number with the corpus alias.

| Gate | T7 manifest ID | Requirement | Observable |
|---|---|---|---|
| G5 Indexing and listing placement | B1 | Every batch-1 term indexed for the D2 preferred variation, with title or bullet placement on any term with a rank objective. No bid ranks an unindexed term | T2 block K2 columns **Indexed?** and **Listing placement**, dated in the batch window; backend-only terms carry a listing-queue ticket |
| G6 Inventory adequacy | D2 | Launch cover on the D2 preferred variation sized against the **full batching plan**. RED = projected stockout **≤14 days** | T2 K2 **Inventory Band** GREEN with **Days to Stockout**; ranked backup chain in the **Keyword-to-Variation Map** |
| G9 Price stability (corpus alias: margin freshness) | D1 | No price change on the targeted variation in the **trailing 7 days**, or all CVR/ACOS reads in the window marked PROVISIONAL. The launch spine is separately PROVISIONAL until per-variation margin lands | T5 price-move rows; **T0 zone C Margin table version cell** showing version and provisional state |
| G12 MKL hygiene (corpus alias: event freeze) | C1-C8 | Every batch term in the current Master Keyword List with a syntax tag and relevancy score. MKL stale **>30 days** degrades the manifest | T2 block **K1 Syntax tags and Relevancy**; MKL refresh date in T7 inside 30 days |
| G12 Event window (v4.0 number: G10 event exclusion) | - | No go-live inside an armed parent-brand window unless the plan names it. Event weeks + **14 days** excluded from trend verdicts | T5 deal-window row cross-checked to the #32 plan; a recorded absence is the passing observable |
| G11 Sibling conflict | D6 | A shared batch term with a live sibling has a declared lead before it is funded | **Account Rollup A1 Family Boards** ownership row with basis; T2 block **K8 Term owner (family)** |
| G7 Envelope and pacing | A3 | Budgets reconcile to the declared launch envelope. Per **S-A6** (8.1), budgets summing **>110%** of the weekly envelope trigger same-day reconciliation | **T0 zone B Weekly PPC spend** vs the **WeeklyEnvelope** named cell; T3 Campaign Board daily budget column summing inside it |
| G8 Packet completeness | All | Manifest reports present/stale/missing before any verdict. Per **F15**, DEGRADED = **<85%** of gate-relevant field groups → flags only | T7 completeness rollup on the cycle header; **Verdict Classes Blocked** column filled for every non-PRESENT row |
| G2 Sample sufficiency | A4 | Bid reads **≥15 clicks/7d**; CVR verdicts **≥100 clicks**; CTR verdicts **≥1,000 impressions**. Below = capped test | T2 K2 **Clicks 7/30/60d** and **Sample state**. At launch this fails on most rows by construction (expected) |
| G3 Budget truncation | A3 | In-budget **<70%** of the day → every rate TRUNCATED; budget lever first | T2 K2 **In-budget %** on the worst hosting campaign; T3 In-budget bucket column |
| G4 Eligibility | A7 | Advertised SKU eligible; a flip halts all lever activity same day and opens a listing task | **T3 group C2 Eligibility status and reason**, at standup and daily |
| G1 Validation quarantine | A5 | Impossible metrics quarantine the row: flag, no recommendation, same-day data-refresh task | T2 K2 **Validation state**; zero-flag quarantine column in **block K5** |

**Escalation interaction (AM-16).** **F2** sets the **Launch TACOS reference band 15-25%**:

| Deviation class | Range |
|---|---|
| WITHIN | ≤1.2x band |
| ELEVATED | 1.2-1.5x |
| BREACH | 1.5-2x |
| CODE RED | >2x, or >1.5x for 2 validated weeks |

A first-weeks launch product has almost no organic revenue and trips CODE RED mechanically. **T8** sets Recovery Mode above stage defaults with no launch exemption. This SOP does not suspend the rule: the reading is recorded, flagged and routed to the PPC Lead under Authority Matrix row "v4.0 threshold changes" (CEO decides; PPC Lead executes and reviews).

## 4. Procedures

### P1. Pre-standup readiness audit (90 min; day -5 to -1; launch operator executes, PPC Lead reviews)
1. Extract 5 fields from the plan:
   - batch-1 term list
   - product-type classification (subjective / non-subjective)
   - declared envelope $/week
   - D2 preferred variation
   - dated honeymoon exit

   Missing any → back to the launch department.
2. G5 indexing check per term vs D2; record in T2 K2 Indexed? and Listing placement. "Not indexed" terms do not enter batch 1 at any bid; route to the Brand Management indexing owner, ticket reference into the **T2 K7 Situation text** field.
3. G12 MKL hygiene: syntax tag + relevancy in T2 K1; T7 MKL refresh date within 30 days. Untagged → MKL maintenance.
4. G6 on D2 and its ranked backup chain; days of cover vs the full batching horizon. YELLOW at readiness = a plan conversation first.
5. G11 sibling check vs Account Rollup A1 Family Boards; a declared lead is needed before funding.
6. Event-window check vs the #32 plan; record a T5 deal-window row even when no window exists.
7. Assemble the checklist (one evidence line per row), countersign with the launch operator, file as the P1 artifact.
8. Failing rows → dated blocker list with an owner each; the standup date moves or the terms drop from batch 1 (drop logged).

### P2. Workbook pre-clone and provisional economics spine (60 min; day -3; PPC Lead + Data Operations)
1. Clone the PPC Command Workbook template; name it for the product code per the READ ME.
2. Set **T0 zone C cells C18-C24**: named cells **AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope**.
3. Derive (never type) per **M1**: **BE_ACOS = MarginPerOrder / AOV; TargetACOS = 50% of BE_ACOS; MaxAccACOS = 75% of BE_ACOS**. A typed value is a build defect.
4. Tag the margin version cell **PROVISIONAL**.
5. Load the batch-1 list AND the full market keyword list into T2 (coverage state is a column).
6. Set T7 status: **A1 four-period comparability** and **B9 week-over-week deltas** read **MISSING** at launch; record them with blocked verdict classes.
7. Stamp the T7 completeness rollup. **<85%**: launch proceeds, but every verdict issues as a flag (G8), stated in the standup record.

### P3. Phase 1 standup, day 0 (3-4 h for a batch of 8-12 terms; launch operator D+E; human-mandatory)
1. Confirm the P1 checklist is countersigned and the P2 workbook is live (else F1).
2. Deploy **SP Exact single-keyword campaigns on batch-1 terms only** via SOP-12 P1. Fixed bids; one campaign, one keyword, one ad group; advertised SKU = D2 preferred variation, never the parent by default.
3. Deploy the plan's **Halo exacts** the same way, writing each **retirement condition into its T3 row at creation** (missing = F3 on the creation date).
4. Deploy nothing else: no broad, phrase, auto, brand format or conquest. Per **O8**, the launch stage carries a discovery-heavy mix target, which is earned in Phase 2.
5. Build negation walls the same session per #29; record the list in each T3 row.
6. Mini-worksheet per term under SOP-23 P2 logic: target rank, DSTR for that rank, validated or modelled CVR, Expected CPC, required clicks/day, required budget/day, share of loss budget. Version into T2 block **K7** columns **DSTR, Required clicks/day, Required budget $/wk, Loss ceiling $/wk**.
7. One objective per term in **T2 K7** (6-value dropdown): rank-sized = **Ranking**; capped tests = **Discovery**. Untagged → assignment worklist (**O1**).
8. Reconcile the sum of daily budgets vs **WeeklyEnvelope** before staging; **>110%** reconciles same day, worst value first (S-A6).
9. Placement modifiers = **zero** on all three groups.
10. Stage via #38 with objective + worksheet reference in the reason string; same-day deploy permitted on release date, still with full T+1.
11. Write the plan's dated honeymoon exit into the standup record and into T5 as a targeting-change row.
12. One T6 prediction row per term: metric, direction, magnitude, horizon, review date (**V1**).

### P4. Honeymoon daily block (20 min/day; launch operator, PPC Lead I)
1. Gates first, daily: **G4** (T3 C2), **G6** and **G3** (T2 K2), **G1**.
2. Read rank velocity and CVR per term from the **DataRova daily series** and **T2 block K5 cross-type totals**. Record; do not act.
3. Withhold efficiency tightening: bids do not step down on ACOS optics while the window is open (a plan rule, held to the dated exit).
4. A CVR materially below the launch model goes to the launch department as a listing/offer read. Per **D6** the conversion diagnosis opens with the **Price Position Index**; **D8**'s funnel drop point names the owner.
5. Gate responses run immediately: **G6 RED** → same-day taper and re-point under **S-I3** (8.3) via SOP-12 P10, baseline snapshot first. P1 precedence: gate responses are never withheld.
6. **G3** budget lever same day on any truncation.
7. Every intervention goes to T6 with its gate reference. Pacing and gate interventions do not change bids.
8. At the dated exit, close the window in T5 and move to normal scenario governance.

### P5. Batch progression pass (2 h at each batch mark; launch operator D, PPC Lead R, BM owner R)
1. Score last cycle first: V5 = **HIT, PARTIAL, MISS, WRONG-DIRECTION**.
2. Gates per row: G2, G3, G6, G1, G9. A failing gate executes its lever and defers the read.
3. Classify every live term (tree below).
4. **Funding for the next batch = released budget + unspent envelope.**
   - Released budget comes only from **HELD** terms and terms capped at maintenance by a fix-first verdict.
   - Unspent = declared envelope for the window minus actual spend.

   This makes batching **envelope-neutral**: no batch is funded by an envelope increase.
5. A term at target but not held for the v4.0 interval is not HELD. Rule **T1**: the post-objective transition fires at **2 weeks at or under target rank**. An earlier launch hold read = AM-5.
6. Progression log: held terms with released $; continued; failed with read and routed owner; computed funding for batch N+1; step-1 scores.
7. Where **fewer than half** the terms delivered required clicks, check the envelope and per-term split before bids. The fix is fewer terms at full pressure.

**Batch term classification tree (in order, first match wins):**
| # | Condition | Class / action |
|---|---|---|
| 1 | Row fails a gate | **GATED**: execute the gate lever, defer, release nothing |
| 2 | At/under target rank and held for the T1 interval | **HELD**: step pressure down within **L2**, release freed budget |
| 3 | Delivered ≥ required clicks/day with rank velocity intact | **CONTINUED**: no change |
| 4 | Delivered required clicks, CVR ≥ benchmark, rank velocity ~0 across window | **FAILED, over-competitive** → **S-R5** stop-loss (8.4) |
| 5 | ≥100 clicks, CVR below benchmark | **FAILED, conversion** → **S-R4** fix-first, cap at maintenance, release the difference |
| 6 | Under required clicks, CVR ≥ benchmark | **CONTINUED, traffic deficit** → **S-R3**, feed the named lever only |
| 7 | Sample below the G2 line | **CONTINUED, capped test**; runs to its click quota |

### P6. Batch N+1 deployment (2-3 h; within 1 day of P5; human-mandatory)
1. Take the plan's batch list in priority order (not re-ranked).
2. Size the batch to P5 funding, not list length.
3. If funding supports fewer ranking-sized terms: fund the priority subset at ranking size and put the rest at the capped test level per **S-H7** (8.9), a **dated 50-click capped test** with success criteria. Spreading thinner = F4.
4. Full P1 gate set on every new term.
5. Stand up via SOP-12 P1/P2 by class; walls the same session; record in T3.
6. Mini-worksheet in T2 K7 + T6 prediction.
7. Stage via #38; the window's log closes when T+1 returns clean.

### P7. Phase 2 discovery entry on verified conditions (2 h + receiving-SOP time; launch operator D, PPC Lead R)
1. Verify on artifacts, not stated belief.
2. Record the source of condition values (plan document, version, dated section).
3. Verify T7 first (rule **P8**: data-quality precedence beats urgency). DEGRADED refuses.
4. Verify each condition vs its artifact; unverifiable = blocker with owner and date.
5. On clean verification stand up via owning SOPs:
   - family broad via **SOP-14 P1**, capped budgets, down-only bidding
   - auto close match via **SOP-15 P2**
   - phrase only where SOP-13's proven-root preconditions hold
6. Register with #30 from the first Monday after entry.
7. Discovery objective per **O6** (judged on cost per discovered converter, waste %, graduation rate).
8. A failure is refused in writing with the failing condition, artifact, owner and re-test date.

**Phase 2 entry tree:**
| # | Check | If fail |
|---|---|---|
| 1 | T7 ≥85% of gate-relevant groups | REFUSE, data-repair task, re-test next refresh |
| 2 | Condition values present, sourced, dated in plan | REFUSE, escalate to PPC Lead as AM-1 dependency |
| 3 | Every condition verifies against its artifact | REFUSE, name the condition and owner |
| 4 | Event window armed on parent brand and plan does not name the advance | DEFER to window close + exclusion period |
| 5 | All clear | **ADVANCE**: stand up via SOP-13/14/15, register #30, write the phase-advance record |

### P8. Product-type overlay (rides every placement/discovery decision; launch operator)
1. Record the plan's classification once in T5 as a targeting-change row.
2. **Non-subjective:** a top-of-search test opens only after conversion evidence exists on the term; modifiers stay at zero until then.
3. **Subjective:** test top-of-search and rest-of-search together; discovery enters earlier within Phase 2 once P7 verifies.
4. **F9** on every placement read: a TOS premium survives only where its conversion beats ROS inside the CPA ceiling. A **mix shift >15 points across 4 weeks** with no logged change → structural inspection first.
5. Waste limits: **F11 sets 10% standard and 40% discovery** with no product-type split. KDR v3.0 carries a product-type split that v4.0 does not govern. Apply v4.0 and log the divergence (AM-10).

### P9. Launch weekly audit interface (60 min; within 1 day of the audit landing)
1. The launch department's weekly audit is the governing review; PPC delivers into it.
2. Keyword-level table, 6 columns:
   - rank vs target with history
   - clicks delivered vs required
   - CVR vs launch model with benchmark source named
   - spend vs batch budget
   - gate state
   - current P5 classification
3. Benchmark source on every CVR per **D3**: **SQP brand-vs-market first, file reference targets second, account norm third**; confidence drops on fallback.
4. Carry flags honestly (provisional reads, fallback benchmarks, manifest gaps). Hiding a fallback violates **J7** (13.3).
5. Stage actions via #38.
6. Record the audit reference in T5.

### P10. Graduation verification and the 11-field handoff packet (3 h; within 2 days of claim; launch operator assembles, PPC Lead R)
1. Verify graduation conditions vs artifacts; record the source document, version and date (T2 names 5 dimensions without values; AM-2).
2. Completeness = fields present / required. **Below 11 of 11 it does not proceed.**

| # | Field | Standard |
|---|---|---|
| 1 | Batch history with scored predictions | Every window, held/continued/failed, each prediction V5-scored |
| 2 | Per-term validated CVR | Only terms ≥100 clicks carry a CVR; others carry click count, no CVR |
| 3 | Discovered CPC ranges per term | Observed range with window dates (feeds Expected CPC) |
| 4 | Rank states vs targets | Current, target, best with date, velocity (for **D10** recovery vs never-ranked) |
| 5 | Campaign registry with objectives | Type, objective tag, role, advertised SKU, matching T3 exactly |
| 6 | Negative and wall lists | Per campaign at each structure event (#29 baseline) |
| 7 | Open tests with dates | Click-count progress and review date |
| 8 | Halo retirement states | Written condition and whether met |
| 9 | Inventory and variation state | D2 preferred, backup chain, current band, pre-OOS baselines |
| 10 | Realized economics | Blended validated CVR across qualifying terms, realized AOV, recomputed max profitable CPC |
| 11 | Launch audit trail reference | Pointer to the launch department's audit series |

3. Short fields name the missing element, owner and date; never waived for schedule.
4. Recompute max profitable CPC from realized data (**F1**: margin $ x CVR).

### P11. Workbook standup and reclassification (2-3 h; same week as packet; PPC Lead, launch operator executes)
1. Upgrade the T0 zone C spine: realized **AOV (C18)** and **MarginPerOrder (C19)**; the chain recomputes. Clear PROVISIONAL only where per-variation margin now exists.
2. Seed T2 with the launch keyword set plus the full market load.
3. Import the launch registry into T3, preserving objective tags, roles, SKUs.
4. Retire Halo exacts whose conditions are met: **PAUSED-PENDING** with the charter as reason and no re-entry (**O5**). Pause, never delete.
5. Retag batch exacts:
   - continuing rank objective → keeps Ranking with target and horizon
   - at target → transitions per **T1**
   - capped term → carries its fix-first re-entry criterion
6. Discovery campaigns move to SOP-13/14/15 governance unchanged. No rebuild at handoff (tagging, not restructure).
7. T7: A1 and B9 MISSING rows begin filling from the first standing cycle.

### P12. First standing cascade and co-sign (90 min in the Monday cascade; PPC Lead + launch operator, dual human-mandatory)
1. Full T0 → T1 syntax caps → T2 per-term verdicts; skipping T0/T1 is invalid.
2. Closed vocabulary only.
3. Every verdict to T6 with prediction and review date.
4. Both owners co-sign the same T6 row, with the packet reference and first cascade attached.
5. **Seam rule:** until the co-sign the launch owner holds the product; after it the standing owner does. Ownership never transfers by calendar, verbal handover, or conditions being met.
6. If the co-sign does not land, ownership stays and the delay escalates (Authority Matrix standing rule 3: route up). The v1.0 escalation interval does not trace to v4.0 (AM-14).

### P13. Post-handoff calibration (90 min; 30 days after co-sign; PPC Lead, launch dept I)
1. Score the launch model vs realized on 3 lines:
   - assumed CVR vs blended validated CVR
   - assumed Expected CPC vs discovered ranges
   - assumed rank velocity vs realized, per term class
2. Each delta as % → launch department for the next plan.
3. Read the first **4 standing cycles** for orphan symptoms (no objective tag, no wall list, tests past review, unscored launch predictions). Each = F6, naming the packet field.
4. File amendment proposals per **V3** (versioned, supersession note; oral re-derivation = violation).
5. Close the launch record.

## 5. Rules, thresholds and numbers

### v4.0 references
| ID | Meaning as described |
|---|---|
| G1 | Validation quarantine: flag, no recommendation, same-day data-refresh task |
| G2 | ≥15 clicks/7d bids; ≥100 clicks CVR; ≥1,000 impressions CTR |
| G3 | In-budget <70% → TRUNCATED; budget lever first |
| G4 | Eligibility flip halts same day |
| G5 | Indexing + listing placement |
| G6 | Inventory; RED = stockout ≤14 days |
| G7 | Envelope/pacing |
| G8 | Packet completeness; DEGRADED → flags only |
| G9 | Price stability (7 days) / corpus alias margin freshness |
| G10 | Event exclusion (corpus calls it G12): event weeks + 14 days |
| G11 | Sibling conflict; lead declaration |
| G12 | MKL hygiene (v4.0 meaning) / corpus alias event freeze |
| F1 | Ranking envelope ACOS 50-80% (as used in WE-1); max profitable CPC = margin $ x CVR |
| F2 | Launch TACOS band 15-25%; WITHIN ≤1.2x, ELEVATED 1.2-1.5x, BREACH 1.5-2x, CODE RED >2x or >1.5x for 2 validated weeks |
| F9 | TOS premium survives only where conversion beats ROS inside CPA ceiling; mix shift >15 pts / 4 weeks without logged change → structural inspection |
| F11 | Waste limits 10% standard, 40% discovery |
| F15 | DEGRADED = <85% of gate-relevant field groups |
| M1 | BE_ACOS = MarginPerOrder/AOV; Target = 50% of BE; MaxAcc = 75% of BE |
| M2 | Required clicks = DSTR / expected CVR; required budget = clicks x Expected CPC |
| M5 | Push funding queue |
| O1 | Untagged row → assignment worklist |
| O5 | PAUSED-PENDING carries reason + re-entry; Halo retirement mechanism |
| O6 | Discovery judged on cost per discovered converter, waste %, graduation rate |
| O8 | Launch stage carries a discovery-heavy mix target |
| D3 | Benchmark order: SQP brand-vs-market, file reference targets, account norm |
| D6 | Conversion diagnosis opens with the Price Position Index |
| D8 | Funnel drop point names the owner |
| D10 | Recovery vs never-ranked classing |
| L2 | ±50% per change, $0.50 floor |
| L9 | Re-point bid seeded at backup's Expected CPC |
| X10 (Sec 4) | Phase 2 surface carrying >40% of a batch term's clicks |
| T1 | Post-objective transition at 2 weeks at/under target rank |
| T2 | Launch/Scale graduation criteria and Phase 1-4 model stand; 5 dimensions |
| T8 | Recovery Mode above stage defaults; no launch exemption |
| P1 (Sec 12) | Gates > diagnosis > signals |
| P5 (Sec 12) | 25% bid-move line; structural changes human-mandatory regardless of size |
| P8 (Sec 12) | Data-quality precedence beats urgency |
| J7 (13.3) | Hiding provisional/fallback is a violation |
| V1, V3, V5 | Predictions; amendment protocol; scoring (HIT/PARTIAL/MISS/WRONG-DIRECTION) |
| S-A6 (8.1) | Budgets >110% of weekly envelope → same-day reconciliation |
| S-I3, S-I5 (8.3) | RED → taper and re-point; restock recovery play with 3-week ETA checkpoint |
| S-R1 (8.4) | Bids up 15-25% incrementally when clicks below G2 with budget healthy and inventory GREEN |
| S-R3 / S-R4 / S-R5 (8.4) | Traffic deficit / fix-first / stop-loss |
| S-R12 (8.4) | Head term carrying all traffic through auto with zero exact campaigns |
| S-H7 (8.9) | Dated 50-click capped test for underfunded relevant term |

### Numbers
| Item | Value |
|---|---|
| Batch size (time estimate basis) | 8-12 terms |
| Standup phase | Day 0; readiness day -5 to -1; pre-clone day -3 |
| Envelope breach line | 110% |
| T7 DEGRADED | <85% |
| In-budget truncation | <70% |
| Inventory RED | ≤14 days to stockout |
| MKL staleness | >30 days |
| Price stability window | 7 days |
| Event exclusion | Event weeks + 14 days |
| Capped test | 50 clicks |
| CVR validation | ≥100 clicks |
| HELD interval | 2 weeks at/under target (T1) |
| Re-batch check | Fewer than half the terms delivering required clicks |
| Launch TACOS band | 15-25% |
| Waste limits | 10% standard / 40% discovery |
| Placement mix shift | >15 points across 4 weeks |
| Auto/broad carrying a batch term | >40% (X10) |
| Bid change limit | ±50%, $0.50 floor; bid-move line 25% (P5) |
| Unlock traffic | +15-25% incrementally (S-R1) |
| Packet | 11 fields, must be 11/11 |
| Calibration | 30 days after co-sign; first 4 standing cycles read |
| Time estimates | P1 90m; P2 60m; P3 3-4h; P4 20m/day; P5 2h; P6 2-3h; P7 2h; P9 60m; P10 3h; P11 2-3h; P12 90m; P13 90m |
| I-18 timing | Raw Pull Pack Monday 06:00 for a 09:00 packet |

### Worked examples (fictional base: AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max 26.3%, launch model CVR 5.2%, Expected CPC $2.50)
- **WE-1:** 8 batch-1 terms + 3 Halos, non-subjective, envelope $210.00/day.
  - Max profitable CPC = 28.00 x 0.052 = $1.46; Target CPC = 80 x 0.175 x 0.052 = $0.73.
  - Sizing: T1 DSTR 1.30 → 25.0 clicks → $62.50/day; T2 1.04 → 20.0 → $50.00; T3 0.78 → 15.0 → $37.50 (ranked subtotal 60.0 clicks / $150.00). 5 capped tests at 50 clicks x $2.50 = $125.00 over 14 days = $8.93/day each ($44.64). 3 Halos at $5.00 = $15.00. Total $209.64 = 99.8% of envelope.
  - Day 14:
    - T1: 344 clicks, 18 orders, $866.88, ACOS 60.2% (inside the Ranking 50-80% envelope), CVR 5.2%, 98.4% of clicks, rank 14 vs target 10, loss $362.88 ($25.92/day) → CONTINUED.
    - T2: 277 clicks, 15 orders, $686.96, ACOS 57.2%, CVR 5.4%, rank 11 vs 12, first window → HOLD; DEFEND LIGHTLY (not HELD).
    - T3: 129 clicks, 4 orders, $297.99, ACOS 93.1%, CVR 3.1%, 61.3% of clicks → FIX CONVERSION FIRST.
    - Tests: 224 clicks, 7 orders, $548.80, ACOS 98.0%. Halos $210.00.
  - Total spend $2,610.63 vs $2,940.00 envelope (88.8%), unspent $329.37. T3 capped from $21.29 to $8.93/day releases $12.36/day = $172.99. Batch 2 funding $502.36 = $35.88/day → 4 capped tests ($35.71). 14-day TACOS $2,610.63 / $4,000.00 (incl. $480.00 organic) = 65.3% = 2.6x band top → CODE RED mechanically → AM-16.
- **WE-2:** Day 9 of a 21-day honeymoon; D2 Days to Stockout 11 → RED. Baseline: T1 rank 16, CVR 5.2%, CPC $2.52; T2 rank 11, CVR 5.4%, CPC $2.48. Re-point to backup Expected CPC $2.35: T1 $2.60 → $2.35 (-9.6%), T2 $2.45 → $2.35 (-4.1%). Day-14 pass classifies 6 terms not 8. Restock → S-I5 recovery with 3-week ETA checkpoint.
- **WE-3:** Week 6 Phase 2 request. T7: 24 groups, 17 PRESENT, 4 PARTIAL, 3 MISSING = 70.8% (21/24 needed). The plan states 2 of 3 conditions without version date; the 3rd is missing. Refused on both grounds; QUARANTINE: DATA REFRESH; 3 repair tasks. Clears 11 days later at 87.5%.
- **WE-4:** Week 14. Packet 9/11 (81.8%): field 2 has CVRs on 61, 74, 88 clicks; field 6 is missing walls for 2 of 3 Halos. Repaired to 11/11. Six terms ≥100 clicks: 1,067 clicks, 52 orders, CVR 4.9% vs 5.2% (-6.3%). Max profitable CPC $1.46 → $1.36 ($28.00 x 0.04873). Conditions met day 96; no co-sign by day 105; co-sign day 107. Orphan window zero days.

## 6. Data inputs required
- **Launch department plan:** batch lists (in priority order) with indexing status, product-type classification, declared envelope $/week, D2 preferred variation, dated honeymoon exit, batch cadence, Halo exacts list, batch loss budget, Phase 2 condition values (sourced, versioned, dated), graduation condition values on the 5 T2 dimensions.
- **Launch department weekly audit document** and audit series.
- **Keyword-to-Variation Map** with adequacy bands and ranked backups (Logistics and Catalog via Economics and Context Pack tab 2).
- **Margin table** with contribution per variation and version stamp (#41 + Finance).
- **Declared launch envelope and funding queue position:** **T0 zone H**, **Account Rollup A2**.
- **#29 pre-load negative sets** from the taxonomy; wall lists.
- **#23 mini-worksheet method and field set**.
- **#32 armed event-window declaration** with dates.
- **#33 lead-product declaration** via **Account Rollup A1 Family Boards**.
- **Master Keyword List (MKL)** (syntax tags, relevancy scores, refresh date) and the **full market keyword list**.
- **DataRova daily series** (rank velocity, CVR per term).
- **SQP brand-vs-market** (first benchmark source), file reference targets, account norm.
- **Price Position Index** (D6).
- **Raw Pull Pack** with period sheets (Monday 06:00).
- **#38 T+1 verification report**.
- **T7 Manifest** status by field group (via #39 / Data Operations): completeness rollup, Verdict Classes Blocked column, MKL refresh date.
- **T0:** zone B (Weekly PPC spend; TACOS line), zone C cells C18-C24 (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope) plus the Margin table version cell, zone H.
- **T1** syntax caps.
- **T2 blocks:** K1 (Syntax tags, Relevancy); K2 (Indexed?, Listing placement, Inventory Band, Days to Stockout, Clicks 7/30/60d, Sample state, In-budget %, Validation state); K4 (Pre-OOS baseline); K5 (cross-type totals; zero-flag quarantine column); K6 (Max profitable CPC); K7 (Situation text, DSTR, Required clicks/day, Required budget $/wk, Loss ceiling $/wk, objective dropdown, test status, stop-loss date); K8 (Term owner (family); negation mode); K9 (verdict); campaign child rows.
- **T3 Campaign Board:** group C2 (Eligibility status and reason), daily budget column, In-budget bucket column, registry rows (type, objective tag, role, advertised SKU, wall list, Halo retirement condition).
- **T5 Product Log:** price-move rows, deal-window rows, targeting-change rows (honeymoon exit, product type, phase advance), batch calendar entries, audit references.
- **T6 Decision Log:** predictions, V5 scores, interventions, handoff line.
- **Catalog field groups (skill bindings):** A3 pacing/in-budget, A4 sufficiency buckets, A6 objective/Expected CPC, A7 eligibility, B1 indexing/listing placement, B3 rank pack, B5 coverage counts, B8 economics chain (T0 C18-C24), B9 WoW deltas (MISSING at launch), C1-C8 MKL hygiene, D1 per-variation margin (PROVISIONAL), D2 variation map with backup chains, D7 decision log. A1 four-period comparability (MISSING at launch).
- **Ads Console** (offer live and buyable; eligibility).
- **PPC Command Workbook TEMPLATE v1.0** and its READ ME (naming).

## 7. Outputs and artifacts
| Artifact | From | Storage | Retention | Consumer |
|---|---|---|---|---|
| Readiness checklist, countersigned | P1 | Launch record, referenced from T5 | To P13 close (AM-13) | P3; launch audit series |
| Command Workbook, cloned and spined | P2 | Product's Command Workbook T0-T7 | Permanent | All procedures; standing cascade |
| Standup record with mini-worksheets | P3 | T2 K7, T3 rows, T6 predictions | T6 append-only; K7 in place, worksheet versioned | P5; SOP-23 calibration; packet field 1 |
| Wall lists per campaign | P3, P6 | T3 row | Campaign life; packet field 6 | #29 monthly wall audit |
| Honeymoon daily lines | P4 | T6 (one line per intervention with gate ID) | Append-only | P5; F2 detection |
| Pre-OOS baseline snapshots | P4.5 | T2 K4 | Until recovery closes or term retires | S-I5; packet field 9 |
| Batch progression log | P5 | T6 with classification and funding computation | Append-only | P6; packet field 1; P13 |
| Phase-advance record | P7 | T5 targeting-change row + artifact set | Permanent | #30; launch audit; v4.1 reconciliation |
| Keyword-level audit table (6 columns) | P9 | Launch weekly audit; reference in T5 | Launch dept retention | Launch audit; BM owner |
| Handoff packet (11 fields) | P10 | Launch record, referenced from T6 co-sign line | Permanent | P11; standing owner |
| Co-signed handoff line | P12 | T6, one row, both signatures, cascade attached | Append-only, permanent | #36 standing cycle; Register run ledger |
| Calibration record | P13 | Launch record + T6; proposals to v4.1 register | To next launch of same product class | Next plan; SOP-23 assumptions; v4.1 brief |
| Blocker list | P1 | Dated, owner each | n/a | Launch dept |

Retention is by rule (T6 append-only, pause never delete, workbook permanent); no numeric period (AM-13; #39 pending fold-in).

### Verdict mapping (KDR v3.0 25 strings → launch execution; v4.0 13.1 cross-map)
| KDR verdict | Launch execution | v4.0 cross-map |
|---|---|---|
| QUARANTINE: DATA REFRESH | No change; refresh task same day; refuses the phase advance at P7 | FLAG: DATA REPAIR |
| UNLOCK TRAFFIC | Bids up per S-R1 15-25% when clicks are below G2 with budget healthy and inventory GREEN; common in week 1 | - |
| FIX BUDGET (TRUNCATED) | Budget lever only, same day; the week's bid read void | - |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Test runs to quota; budget assurance only; standard for most launch terms | EXTEND TEST |
| FUND TEST (UNFUNDED PRIMARY) | P6.3 creation at capped bid; test status and stop-loss date into T2 K7 (S-H7) | FUND DELIBERATE TEST (50-CLICK CAP) |
| RANK PUSH: FUND SIZED PUSH | P3/P6 standup at worksheet sizing via SOP-12 P1 | RANK PUSH AT CONTROLLED CPC |
| RECOVERY PUSH | Only after an in-stage stockout, sized to the P4.5 baseline; no baseline = cold start | - |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Named lever only; P5 branch 6 | - |
| FIX CONVERSION FIRST; DEFER PUSH | Cap at maintenance, release the difference, route per D8; in honeymoon the cap waits for the exit | Same |
| PLACEMENT FIX FIRST | Bids hold; #28 executes; non-subjective cannot issue before conversion evidence | - |
| RE-POINT VARIATION | SOP-12 P10 same day, baseline first; CVR baseline resets | Same |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | SOP-12 P4; only after the T1 interval | TAPER TO FLOOR (POST-OBJECTIVE) |
| HOLD; DEFEND LIGHTLY AT RANK | No change; releases no budget | CONTINUE; VERIFY MOMENTUM |
| DEFEND AT FLOOR | Drift restores in one step; rare in launch | Same |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Bid to T2 K6 Max profitable CPC, single step; syntax cap at T1; in honeymoon the bid half waits | Same |
| INCREMENTALITY LADDER | Not issued in launch (no organic baseline); after co-sign under #35 | - |
| ADD EXACT + RESTRUCTURE | SOP-12 P1/P2 + steering walls; fires when a Phase 2 surface carries a batch term's clicks (X10 >40%) | Same |
| CONSOLIDATE DUPLICATES | SOP-12 P7; survivor human-mandatory; usual cause Halo + batch exact on one term | - |
| GRADUATE FROM DISCOVERY | From #30; SOP-12 same day, walls same session; no exception | GRADUATE + STEER |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | #29; pre-load at P3, walls at P6, steering on graduation; mode per term in T2 K8 | CUT / NEGATE |
| ENTER SBV ARBITRAGE | Not in launch; after co-sign under #17-19 | FORMAT SUBSTITUTION (SBV/SD) |
| OPEN / ROTATE / EXIT CONQUEST | Not in launch; conquest is a Phase 3-4 surface (#16) | - |
| STOP-LOSS: CONCEDE OR DEFER | Maintenance or PAUSED-PENDING; freed budget funds the next batch via P5.4; P5 branch 4 | Same |
| PAUSED-PENDING (REASON + RE-ENTRY) | Reason + re-entry in T2 and T3 (O5); standard re-entry = next batch window; Halo retirement (no re-entry) | PAUSE (LEVERS EXHAUSTED) |
| LEAVE TO HARVEST | No exact; discovery economics under #30; only after Phase 2 entry | Same |

- v4.0 **PORTFOLIO CALL: ASSIGN LEAD** has no KDR counterpart; executed as the G11 response at P1.5 / P6.4, with the declaration held by #33 (extends **C10**).
- Retired v1.0 strings (conflict **C17**): DEPLOY BATCH N, HOLD BATCH, PHASE ADVANCE, HALO RETIRE, HANDOFF.

### Failure modes
| Mode | Detection | Response | Incident |
|---|---|---|---|
| F1 Everything-at-once | Any broad/phrase/auto/brand/conquest live before the P7 record | Pause to sequence same day | Launching every type together |
| F2 Premature efficiency tightening | Honeymoon bid step-down citing ACOS | Revert; gate responses carry a gate ID | Carried v1.0 |
| F3 Immortal Halo | Halo past its condition, or no condition in T3 | Retire at P11.4 | Halos outliving purpose by months |
| F4 Batch spread | Live terms above the plan's batch with under-delivered clicks across most rows | Re-batch to priority set at full pressure | One term absorbing about a quarter of a product's clicks above break-even |
| F5 Handoff orphan | Graduation verified, no co-sign, no cascade | Seam rule; escalate the delay | Carried v1.0 |
| F6 Launch data lost | Standup missing packet fields | Re-run checklist; handoff waits | WE-4 61-click CVR |
| F7 Invented verdict strings | K9/T6/staged reason outside the 25 | Re-issue from Section 5 | v1.0 itself (C17) |
| F8 Phase advance on calendar | No condition artifact set or unrecorded source | Revert; hold Phase 2 at current budgets | The gap this rebuild found |
| F9 Phase 2 surface carrying a batch term | Auto/broad >40% of a batch term's clicks (X10) on T2 child rows | ADD EXACT + RESTRUCTURE or steering walls | S-R12 head-term-through-auto case |
| F10 Provisional treated as live | Ceiling action while PROVISIONAL without a flag in the reason | Flag rides to P11 (J7) | Blended margin used where per-variation margin owed |
| F11 Sibling collision | Batch term active on a sibling with no lead in A1 | Neither scales until the portfolio call | **$3.24 vs $1.48 CPC on the same term across two siblings** ("settings archaeology") |
| F12 Predictions never scored | Launch T6 rows past review with empty V5 at P13 | Score late, record delay | Pattern V-layer ends |

Escalation: F1, F4 → launch owner + PPC Lead jointly on first occurrence. F5, F8 → PPC Lead with the artifact set. F7, F10, F12 → P13 audit lines. Recurrence in consecutive windows escalates with T6 history. Alarm routing: same day F2, F9, F10, F11; next progression worklist F3, F4, F6, F7; PPC Lead F1, F5, F8; P13 F12.

### Interface contracts (I-1 to I-20)
| ID | Artifact | Sender → Receiver | Timing | Non-arrival |
|---|---|---|---|---|
| I-1 | Launch plan (batch lists, indexing, type, envelope, honeymoon exit) | Launch dept → launch operator | Day -5 | P1 cannot open; standup moves; nothing inferred |
| I-2 | Keyword-to-Variation Map | Logistics & Catalog via Economics and Context Pack tab 2 → operator | Day -5, monthly | G6 cannot pass; capped tests only on declared SKU with D2-pending flag |
| I-3 | Margin table + version | #41 + Finance → PPC Lead, T0 C18-C24 | Day -3, monthly | Launch model with PROVISIONAL; never blocks; unflagged = F10 |
| I-4 | Envelope + funding queue | T0 zone H, Account Rollup A2 (C3) → operator | Day -3, weekly | No batch sizes |
| I-5 | Pre-load negative sets | #29 → operator | At P3 same session | Standup does not close |
| I-6 | Mini-worksheet method | #23 → operator | Standing | No ranking-size deploys; capped only |
| I-7 | Wall lists | #29 → operator, T3 | Same session each event | Event incomplete; term unsteered |
| I-8 | Staged sets | Operator → #38 | Same day on release | Nothing deploys |
| I-9 | T+1 report | #38 → operator | Day after deploy | Treated as unlanded |
| I-10 | Armed window declaration | #32 → operator | Day -5 and on arming | G12 event check fails; recorded absence is valid, silence is not |
| I-11 | Lead-product declaration | #33 via A1 → operator | Day -5 and on new shared term | G11 blocks funding; capped only |
| I-12 | Exact standups | Operator → #12 | P3, P6 | Terms unfunded |
| I-13 | Phase 2 verification | Operator → #13/14/15 | P7, within 2 days | No discovery standup |
| I-14 | Harvest registration | Operator → #30 | First Monday after Phase 2 | No graduation destination |
| I-15 | Graduation issuances | #30 → operator | Weekly from Phase 2 | Proven terms stuck on discovery |
| I-16 | Placement evidence | Operator → #28 | Post-conversion per P8 | Modifiers stay zero |
| I-17 | T7 status | #39 via Data Ops → operator | Weekly at packet-ready | Treated as DEGRADED |
| I-18 | Raw Pull Pack | Data Ops → Command Workbook | Monday 06:00 for 09:00 packet | Gates-only read; four-period sheets MISSING by construction |
| I-19 | Keyword-level audit table | Operator → launch dept, BM owner | Within 1 day of audit | 2 consecutive misses escalate |
| I-20 | Co-signed handoff line | Operator + PPC Lead → standing owner (#36) | Same week packet completes | Launch owner keeps the product; delay escalates |

## 8. Decision rights
Authority Matrix v2.0 rows:
- **"Launch-stage verdicts + batches":** launch operator **D and E**, PPC Lead **R**, BM owner **R** (reviews), CEO **I**. Every batch deployment and phase advance is human-mandatory and never auto-applies.
- **"Structure creation (all SOPs)":** PPC Lead D (or owning SOP scope), launch operator E in launch scope.
- **"Push funding (the M5 queue)":** PPC Lead D within envelope, **CEO above envelope**. A batch needing an envelope increase leaves this SOP.
- **"Bulk deployments (#38)":** PPC Lead R; launch operator E in own scope.
- **"Code-red declaration + close"** with standing rule 1: on launch products, **launch operator declares, PPC Lead closes**.
- **"Event plans (#32)":** PPC Lead D with deals owner; launch operator E.
- **"v4.0 threshold changes":** CEO decides; PPC Lead executes and reviews (AM-16 routing).
- **P12 co-sign:** dual human-mandatory (PPC Lead + launch operator).
- Standing rule 3: disagreements route up. Standing rule 5: vacancy D → PPC Lead, E → PPC Manager.
- P1: launch operator executes, PPC Lead reviews. P2: PPC Lead + Data Operations. P13: PPC Lead, launch dept informed.
- AI-executable with audit: gate assembly, worksheet computation, classification drafts, funding drafts, completeness counts, packet assembly, P9 table, V5 drafts, P13 deltas, alarm detection. Nothing auto-applies.

## 9. Account-specific facts
- No Tier 3 launch-stage economics spine is attached. The attached **Command Workbook B4 v1.0** is a **mature-stage product** whose spine does not transfer. All examples use the fictional base.
- Account-history incidents cited: a product where one term absorbed roughly a quarter of its clicks above break-even (F4); a **$3.24 vs $1.48 CPC divergence on the same term across two siblings**, found to be "settings archaeology rather than auction reality" (F11); a head term carrying all traffic through auto with zero exact campaigns (S-R12, F9); the account's standing condition of blended margin used where per-variation margin was owed (F10).
- The phase framework lives in the **Master PPC Decision Criteria System v1.0 (March 2026)**, which is not in the corpus.
- At launch, T7 A1 and B9 read MISSING by construction.

## 10. Open items
| ID | Item / interim |
|---|---|
| AM-1 | Phase 1 → Phase 2 entry conditions with values; P7 uses plan values with source recorded |
| AM-2 | Graduation conditions on the 5 T2 dimensions; P10 uses the plan |
| AM-3 | Honeymoon window duration and exit rule; the plan's dated exit |
| AM-4 | Batch size limit and cadence; plan cadence; P6 sizes to funding |
| AM-5 | Launch hold read before the standing transition; fallback to T1 2 weeks |
| AM-6 | Envelope-setting rule for a no-history product; the plan's declared envelope |
| AM-7 | Launch batch loss ceiling (M2 sizes from projected sales a launch term lacks); the plan's loss budget as a stated input |
| AM-8 | Sufficiency substitute below G2; none used, capped tests instead |
| AM-9 | Legal condition set for a Halo retirement charter; a written condition required, form unconstrained |
| AM-10 | Product-type waste bands (KDR has them, v4.0 does not); apply F11 10%/40% |
| AM-11 | Stage TACOS band reconciliation across 3 documents; use F2 (conflict **C16**) |
| AM-12 | Whether launch batch exacts inherit the **30% top-of-search requirement** before conversion evidence; flagged, not resolved |
| AM-13 | Retention schedule for launch artifacts |
| AM-14 | Co-sign escalation interval |
| AM-15 | Provisional economics tolerance at launch |
| AM-16 | Launch interaction with CODE RED and Recovery Mode precedence |
| C3 | #31 has no procedural document; instrument layer referenced |
| C6 | SOP-27 LTSF tier declaration precedent |
| C9 | G9/G10/G12 meaning divergence |
| C10 | 18 vs 25 vocabulary divergence; PORTFOLIO CALL: ASSIGN LEAD extension |
| C16 | Stage TACOS bands stated differently in 3 documents |
| C17 | v1.0 invented verdict strings |
| Ledger | Conflicts C1-C18 referenced; component #22 row |
| Named documents not present | Master PPC Decision Criteria System v1.0 (March 2026); Criteria System v4.0; KDR v3.0; Authority Matrix v2.0; Data Architecture v1.0 (Sections 4, 6, 8, 9); Command Workbook TEMPLATE v1.0 and READ ME; Strategic Doctrine v1.0 (Sections 1-3); Economics Worked-Example Set v1.0; SOP-12, 13, 14, 15, 23, 27, 28, 29, 30, 32, 33, 36, 38, 39, 41; Economics and Context Pack (tab 2); launch department plan and weekly audit frameworks; Supersession Map; Completion Directive |

Review triggers: any v4.1 increment landing an AM item; any v4.0 increment; any launch plan template change (8 gates take values from it); C10 resolution; a P13 delta beyond what the next plan can absorb; the first launch run after publication.
