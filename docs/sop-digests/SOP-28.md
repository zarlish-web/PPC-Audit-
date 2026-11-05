# SOP-28 Digest: Placement and Modifier Operations

Source: `PPC_SOP_28_Placement_and_Modifier_Operations_v2_0.pdf` (36 pages; extraction marks 18 source pages). Digest of the plain-text extraction; nothing added beyond the text. The extraction flattens several tables, so column alignment was reconstructed from content.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-28: Placement and Modifier Operations (Component #28 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead |
| Supersedes | SOP-28 v1.0 (2026-07-24) in full |
| Thresholds | Zero local thresholds. Every threshold, band, step size, limit and verdict lives in Criteria System v4.0 and KDR Template v3.0; this SOP owns the mechanics those decisions execute through |
| Size | 14 procedures (v1.0: 8), 12 failure modes (v1.0: 7), 4 worked examples (v1.0: 1), Elements 11 (ramp) and 12 (interfaces) added, 25-string closed vocabulary mapped, 16 amendment items |

**Verdict / purpose.** The three placements (top of search TOS, rest of search ROS, product pages PP) are **three products bought with one bid**, and the modifier is the only instrument that buys them separately. Two absolute rules: **no modifier rises without placement-level conversion proof**, and **no modifier changes without the ceiling worksheet**. This SOP owns mechanics that eleven other components consume (SOP-12 P4, SOP-14 P4, SOP-22, SOP-23 P10, SOP-24, SOP-25, SOP-26 P3 and P8, SOP-30, SOP-35, SOP-37, SOP-38); none of them derives a rung value, exit bid, floor or modifier.

**Most important operating sentence (Section 1.1):** Ledger external dependency **D3** (placement feed) is **OPEN**. T7 Manifest field group **B7 Placement splits (TOS/ROS/PP)**, source feed "TOS placement report", status **MISSING**, blocks "All T4 placement verdicts". **B6 Bid intelligence (suggested bid + gap)** also **MISSING**, blocking "Bid-gap sizing on ladders". Packet completeness stamps at **0.571**, below the **85% DEGRADED** floor of gate G8. Consequence is **asymmetric**: **modifier increases are suppressed account-wide** while B7 is MISSING; **modifier cuts and normalizations remain legal** (removing an unproven premium never needs proof). Ladder, ceiling worksheet, exit-bid arithmetic, floor register and bleeding-placement lever order run on base-bid and blended-CPC data and survive the outage. Strategic Doctrine v1.0 Section 15 item 5 states the same posture.

### v2.0 corrections of substance
1. v1.0 ladder worked example used a first rung of **5.769%** ($2.60 to $2.45) against v4.0 Section 10 rule **M3** step of **roughly 10% per week**, then ran four rungs where two reach the target. SOP-12 v2.0 had already corrected it ($2.60 -> $2.34 -> $2.24). v2.0 adopts the compliant ladder (WE-2).
2. Three numerals v1.0 attributed to v4.0 do not exist in v4.0 and are retired: the **modifier proof ratio** ("the v4.0 factor"), the **per-placement traffic minimum**, and the **modifier step size** ("the +25% top-of-search pattern"). Now AM-1, AM-2, AM-3.
3. v1.0's two-window hold and single re-probe after reverted rung retained as **corpus practice, labelled ungoverned** (AM-8, AM-9).

## 2. Scope and boundaries

### 2.1 Four decision surfaces owned (Section 1.2)
| Surface | What it decides | Number source |
|---|---|---|
| Ceiling worksheet | Whether a proposed base bid + modifier pair is legal, computed before staging | Effective-CPC arithmetic per Strategic Doctrine v1.0 Section 6.1; governing ceiling per v4.0 Section 10 rule **M4** (effective TOS CPC at/under min of max profitable CPC for the objective and Expected CPC plus tolerance) |
| The ladder | Rung value, rung date, hold prediction, reversion rule, where descent stops | M3 step ~10%/week; Section 9 rule **L2** per-change limit 50%, bid floor $0.50 |
| Exit bid and floor register | Where ladder aims and what it discovered when it stopped | v4.0 Section 3 family **F9** blended placement CPC row: bid **$0.05-0.10 below** blended CPC to leave an underperforming placement; L2 carries same decrement |
| Bleeding-placement lever order | Which lever moves first when one placement carries a term's failure | v4.0 Section 9 rule **L1** lever precedence; F9 decomposition classes; Section 8.8 **S-P5**, **S-P6** |

Per Ledger row 28, also owns: ladder execution mechanics, arbitrage setup, bleeding-placement response, exit-bid discovery, modifier sizing, split-exact test.

### 2.2 Three placement decomposition classes (F9; per placement per term, never per campaign)
| Class | Definition | Action |
|---|---|---|
| TOS-EARNS | TOS CVR **materially above** ROS with TOS CPA at/under ceiling | Justifies multiplier up to CPA ceiling (no factor exists for "materially": AM-1) |
| TOS-VANITY | TOS CVR at/below ROS | Cut multiplier (S-P5) |
| PP-LEAK | Product pages absorbing spend below product-page CVR norms | Exit placement via blended-CPC mechanic (S-P6) (no norm exists: AM-7) |

Blended line hides that a term can be profitable at ROS and ruinous at TOS or the reverse (WE-3: blended ACOS 38.47% while PP runs 147.92% losing $140.92/week).

### 2.3 Boundaries (Section 1.4)
| Excluded decision | Owner | Seam |
|---|---|---|
| Every threshold, band, step, limit, scenario, verdict | v4.0 (#8) | A numeral here without a v4.0 section beside it is a defect; 16 ungoverned numerals listed as AM items |
| Campaign-level bid, budget, status, structure incl. taper execution and duplicate consolidation | SOP-12 | This SOP derives rung value and compliant pair; SOP-12 P4 and P11 execute. Campaign edit made from this document is a defect |
| Whether a taper happens and when | SOP-12 P4, #23, #24, #25, #26 | Taper DECISIONS belong there; only taper MECHANICS here |
| Push sizing, authorized CPC envelope, achievement and stability tests | #23 | Receives achievement date, push bid, envelope at taper release; tests in-flight modifiers vs envelope |
| Descent schedule, dates, sequencing | #25 | Schedules rungs and consumes floors; this SOP returns step value per date |
| Which cohorts re-ladder and when; which bleeds cut inside code red | #26 | Supplies mechanics and step values; floor register format is this component's |
| Incrementality test design, continue-or-restore | #35 | Where v4.0 Section 4 rule **X12** makes a rung an incrementality step: this SOP stages rung and records floor |
| Negation walls incl. on placement split | #29 | Split-exact standup builds walls same session; SOP names requirement, never wall level |
| Staging, upload, effective-CPC pre-upload scan, T+1 diff | #38 | P6 scan is an arithmetic check against this SOP's worksheet, never a re-decision |
| Automation rule register and change control | #37 | Ladder holds are this component's; issues hold notice; never edits a rule |
| Family term ownership on shared term | #33 | Gate G11 bars restore step until lead declared |
| Event plan and armed window | #32 | G10 excludes event weeks and 14 days following |
| Non-SP format build on ENTER SBV ARBITRAGE | #17-19 | Supplies only paired SP-exact single ladder step down; SBV go-live step-down routes through #12 (Ledger row 17) |
| Budget envelope, M5 queue, budget release | Instrument layer | Per Ledger conflict C3: names T0 zone H and Account Rollup tab A2; never cites a #31 procedure |
| Dayparting | #45 | v4.0 rule **L10**: +/-15% hourly modifiers on Marketing Stream curves with 4+ weeks of hour-level evidence per campaign. T7 reads **D12 Hourly dayparting MISSING** and deferred. No hourly modifier built |

## 3. Triggers (Section 2)

| Trigger | Detecting artifact / observable | Max lag | Procedure |
|---|---|---|---|
| Weekly cadence | Monday cascade reaches T4 Placement & Bid with T2 OVERSIGHT filter applied | One weekly cycle (v4.0 Section 14 rule **V4** weekly full audit produces Master Action Records) | P1 |
| Modifier change request | Any Section 5 verdict proposing modifier move, in T2 block K9 or from adjacent component | Same cycle; worksheet is the gate | P2, then P3 or P4 |
| Taper release | TAPER: RANK ACHIEVED, STEP BIDS DOWN with achievement date, push bid, authorized CPC envelope | Same day for first rung derivation; not stated in v4.0 (AM-10) | P5, P6 |
| Scheduled descent rung | Dated rung on #25 descent schedule reaching T4 **Next Step Date** | Scheduled date; M3 ~1 week between rungs | P5 |
| Quarterly floor re-test | Cohort reaching re-test date in T4 **Discovered Floor $** and **Next Step Date** | One weekly cycle; M3 quarterly or after logged competitive shock; V4 quarterly cycle | P7 |
| Competitive shock on defended term | T5 Product Log **Event Type** = competitor entry, cross-read vs T2 **K8** competitor block | One weekly cycle | P7 |
| Bleeding placement | One placement failing its band while others hold, on T4 **Placement Verdict**; S-P5 on TOS-VANITY, S-P6 on PP-LEAK | Not stated in v4.0; weekly pass under V4 (AM-10) | P8 |
| TOS share below floor | T2 **TOS IS %** below **30** on a campaign with Ranking objective (Section 8.4 **S-R7**) | Same weekly read | P9 |
| Split candidacy | Divergent placement economics on one term across qualified reads on T4, persistent | Not stated; no window count (AM-15) | P10 |
| Bidding-strategy audit | Campaign with up-and-down bidding, T3 **Bidding Strategy** beside **Placement Mult TOS %** | Quarterly V4 cycle alongside M3 re-tests (ride-along stated, not governed) | P11 |
| Placement drift | T4 **Drift Flag**: placement mix shift **above 15 points over 4 weeks** with no logged change (F9) | Same weekly read | P12 |
| Margin recompute | T0 zone C margin table version change, fires **S-A9** | Same cycle; every keyword with CPC above new ceiling enters ladder queue | P5, P2 |
| Feed state change | T7 B7 or B6 status changing from MISSING | Same cycle; lifted by manifest read, not memory | P13 |
| Rung review date | T6 row with rung prediction reaching **Review Date** | Named review date (rule **V1**) | P14 |

## 4. Preconditions and gates (Section 3)

### 4.1 Live manifest state (Section 3.1)
| Group | Status | Cost to this component |
|---|---|---|
| B7 placement splits | **MISSING** | Every T4 performance column unreadable; every modifier increase suppressed account-wide; ladder unaffected |
| B6 bid intelligence | **MISSING** | Suggested-bid reference gone; F9 auction-moved read (gap widening **>=25% over 4 weeks**) uncomputable |
| A6 objective and per-term Expected CPC | **PARTIAL**, account reference **$2.80** in use | M4 computed vs account value, substitution written on record |
| D1 per-variation margin | **PARTIAL** | G9 PROVISIONAL tag on every ceiling |
| A8 PAT rows first-class | **PARTIAL** | T7 records PAT ladder verdicts blocked; PAT rung staged with coverage gap named |
| A1 four-period comparability | **MISSING** | Single-window reads carry the flag |
| D2 keyword-variation map | **PARTIAL** | Backup chain confirmed on head terms only |
| D6 sibling CPC view | **PARTIAL** | (G11 family ownership) |
| B8 economics chain | **PRESENT** on blended margin | - |
| D12 hourly dayparting | **MISSING**, deferred | No hourly modifier |

Under G8 a verdict whose gate fields are missing downgrades to a flag; v4.0 Section 13.3 rule **J7** makes hiding a fallback a process violation.

### 4.2 Gate table
| Manifest ID | Gate | Requirement | Observable |
|---|---|---|---|
| A4, A5 | G1 | No impossible-metric flag (CVR zero with orders, ACOS without orders, cross-table disagreement) | T2 **Flag: Zero-Quarantine** clear, **Validation State** not quarantined; quarantined row -> flag + data-refresh task, never rung or modifier |
| A4, A1 | G2 | **15+ clicks in 7 days** for bid read, **100+ clicks** for CVR verdict, **1,000+ impressions** for CTR verdict; below -> fall back to **60 days**; still thin -> EXTEND TEST | T2 **Clicks 7/30/60d** and **Sample State**. Minimums stated at keyword/campaign grain only; no per-placement bar (AM-2) |
| A3 | G3 | Campaign not truncated: in-budget **below 70%** of day marks every rate TRUNCATED, budget lever first | T3 **Truncation Flag (G3)** clear and **In-Budget Bucket** above 70%. Corpus alias: KDR Bands sheet labels **51-70 strained**; G3's 70% governs. Truncated week's placement read is void |
| A7 | G4 | Offer eligible and unsuppressed | T2 **Eligibility**; flip halts execution same day, opens listing task |
| D1, D2 | G6 | Targeted variation not RED; RED tapers to defense and re-points same day (outranks placement per v4.0 Section 12 rule **P1**) | T2 **Inventory Band**, **Days to Stockout** vs **Targeted Variation(s)** |
| A3 | G7 | Campaign budgets reconcile to product envelope; a modifier raise is a spend increase and must fit | T2 **Envelope Status**, T0 zone H available dollars; non-fitting raise = queue decision at instrument layer per C3 |
| All | G8 | Manifest reports present/stale/missing; **below 85%** gate-relevant fields = DEGRADED, flags only. Live read **0.571** | T7 Status column and completeness rollup on cycle header; every verdict carries the score |
| D1 | G9 | No price change on targeted variation in trailing **7 days**, else CVR/ACOS PROVISIONAL, no conversion verdict | T5 Event Type = price move vs T2 **Margin $/Unit**. Corpus alias per C9: SOP-12 v2.0, SOP-14, SOP-30, Data Architecture use G9 for margin freshness; both checked, reason string names which fired |
| D7 | G10 | Event weeks and **14 days following** excluded; no modifier change or probe rung inside armed window unless plan names it | T5 **Trend-Exclusion Flag**, T2 **Event Mode**. Corpus uses G12 for event freeze and G10 for objective tagging |
| D6 | G11 | Family ownership declared on shared term before restore step raises a bid | T2 **Family Conflict**, **Term Owner (Family)**, from Account Rollup A1 |
| B11 | G12 | Term in current MKL with syntax tag and relevancy score | T2 **Syntax Tags**, **Relevancy**. Corpus uses G12 for event freeze |
| B7 | Placement | Placement splits at TOS, ROS, PP grain | T4 performance columns carrying values rather than B7 build marker. MISSING: every placement UNREAD, raises suppressed, P1 structural only; Ledger D3 OPEN |
| B6 | Bid reference | Suggested bid and gap per row | T2 **Suggested Bid / Gap %**. MISSING: P7 step 8 routes to T5 log |
| B8, D1 | Economics chain | T0 zone C live: AOV, contribution per order, break-even ACOS, Target ACOS, Max Acceptable, Expected CPC reference | T0 zone C margin table version and fresh/provisional state; Ledger D1 OPEN |

Gate naming: v4.0 numbers govern; corpus aliases given per Ledger conflict **C9**; never mixed in one reason string.

## 5. Procedures (Section 4)

P1-P4 weekly read and modifier program; P5-P7 ladder, floor, re-test; P8-P12 response; P13 feed suppression; P14 scoring. First executions run roughly double the time estimates.

### P1. Weekly placement read (T4) (20-30 min/product at ~100 oversight-class terms x 3 placements)
1. Confirm T0 and T1 read first (v4.0 Section 8: product > syntax > keyword > format scenarios).
2. Score last cycle first: T6, filter Review Date to this cycle, write **V5 Score** on due rungs and modifier changes: **HIT, PARTIAL, MISS, WRONG-DIRECTION**.
3. Read T7 B7. MISSING: structural half only (skip steps 4-5, run step 6 fully, P13 governs). PRESENT/STALE: continue.
4. Per oversight keyword, read T4 one row per placement (TOS, ROS, PP): **Impressions, Clicks, CVR, CPC $, CPA $, Spend Share %, Sales Share %, IS %**.
5. Compute per placement, never per campaign:
   - **Proof read:** placement CVR vs campaign blended CVR and vs ROS CVR; record ratio (bar is AM-1, not governed).
   - **Ceiling read:** placement's own max profitable CPC = contribution/order (T0 zone C) x that placement's CVR, observed CPC beside it. Resolve ratio (observed CPC / own ceiling) into F1 bands: **<=0.8 SAFE; 0.8-1.0 AT-CEILING; 1.0-1.5 PUSH-ONLY; >1.5 UNJUSTIFIABLE** outside a sized push.
   - **Band read:** placement ACOS vs term's governing objective band from v4.0 Section 6 rule **O6** (not campaign blend).
6. Mark **UNREAD** any placement below sufficiency with reason. UNREAD can receive a probe under a verdict, never a premium. G2 keyword-grain minimums applied to placement row and substitution stated (AM-2).
7. Route: proof ratios -> P3; TOS-VANITY or PP-LEAK -> P8; drift flags -> P12; open ladders -> P5 on dated step; rows at recorded floor with no live verdict -> **HOLD; DEFEND LIGHTLY AT RANK** (logged as verdict).
8. Write cycle line into T4 header: rows read, rows UNREAD with reason, placements per F9 class, open ladders and next step dates, missing manifest groups (P14 scores against it).

### P2. Ceiling worksheet, mandatory before any modifier change (8-12 min/change; including cuts)
1. Read from T3: **Bid / AG Default $, Placement Mult TOS %, Placement Mult PP %, Bidding Strategy**. All four required.
2. Current effective CPC ceiling per touched placement = **base bid x (1 + placement modifier) x (1 + dynamic raise)**. Fixed and dynamic down-only: dynamic raise = 0. Dynamic up-and-down: platform can add up to a further **doubling at TOS**. Platform parameters (0-900% modifier range, up-and-down raise at TOS) from Strategic Doctrine v1.0 Section 6.1; not in v4.0 (AM-11).
3. Compute proposed effective ceiling for **every** placement (a base-bid move changes all three).
4. Governing ceiling: at maintenance = term's own max profitable CPC (contribution x placement CVR) from T2 **Max Profitable CPC $**; during funded push = authorized CPC envelope from #23 worksheet (I-4). Neither available -> worksheet stops, change does not stage.
5. Apply M4 minimum: proposed effective TOS CPC <= lower of (max profitable CPC for objective, Expected CPC + tolerance). Tolerance has no value (AM-4): apply first limb, record second unavailable. A6 PARTIAL ($2.80 account reference) -> substitution recorded.
6. Verdict: proposed <= governing -> **CLEARS** (to P3 or P4); else **BLOCKED** as staged.
7. BLOCKED raise: compute **compliant pair** (raise modifier, cut base, hold net effective ceiling inside governing). Solve base at which pair clears; stage both as one set, deploy together or not at all.
8. Attach worksheet as gate artifact (missing worksheet fails #38 staging QA). Records: current and proposed base, current and proposed modifier per placement, bidding strategy, both effective ceilings, governing ceiling with source, M4 limbs applied and unavailable, CLEARS/BLOCKED.

### P3. Modifier raise operations (10-15 min/raise) - **currently suppressed account-wide** (B7 MISSING; P13 governs)
1. Legal read first: v4.0 Section 9 rule **L3** permits placement adjustment only after G2 sufficiency and a **D1 diagnosis**. Raise on UNREAD placement = F2.
2. Proof condition: placement CVR exceeds ROS CVR on read-qualified traffic, and placement CPA <= T2 **CPA Ceiling $**. "Materially above" has no factor: record ratio, route raise to **human-mandatory tier** until AM-1 lands.
3. Run P2 (WE-1: $2.20 base with 150% modifier under up-and-down authorizes $11.00 click = 7.55x a $1.456 ceiling).
4. Confirm envelope (G7): raise fits or is a queue decision at T0 zone H.
5. Saturation (v4.0 Section 4 rule **X11**): if T2 **Marginal ACOS** > **1.5x** average **ACOS**, freeze at prior spend, re-test in **2 weeks**.
6. Confidence modulation (v4.0 Section 10 rule **M10**): halve lever step at LOW, standard at MEDIUM, upper end at HIGH. No modifier step exists (AM-3; v1.0 TOS pattern retired). Until then raise staged at compliant-pair output (arithmetic result, derivation recorded).
7. Log prediction: placement share shift and efficiency consequence, named review date (Doctrine Section 13).
8. Stage via #38 with reason string: verdict verbatim, v4.0 scenario ID, SOP and procedure number, worksheet result, computed proof ratio. Missing scenario ID does not deploy.
9. Every raise deployment human-mandatory (rule **P5**: every 500+ search-volume action and every bid move >25%; a cleared raise moves effective ceiling >25% in almost every case).

### P4. Modifier cut and normalization (6-10 min/cut) - legal throughout B7 outage
1. Cut class: **decomposition cut** (TOS-VANITY under S-P5: cut so term earns at ROS, **re-read in 2 weeks**); **bleed cut** (P8 lever 1); **normalization** (justification expired: push closed, deal window ended, rank achieved and tapered).
2. Normalization: prove expiry: T3 **Objective Tag** vs modifier's originating T6 row (e.g. raised for Ranking push, now tagged Conversions). No horizon in v4.0 (AM-16).
3. Run P2 on the cut (record of ceiling before cut).
4. Effect: placement spend at current vs proposed effective ceiling at constant clicks; conservative (realized spend reduction higher, orders lower); both directions in prediction.
5. Normalization to zero = single step; L2 50% limit governs bid values, not modifiers. Partial cut: residual must clear worksheet.
6. Stage via #38: verdict, scenario ID, worksheet result, expiry evidence for normalization.
7. Write T6 row with dated prediction.

### P5. The ladder: authoritative rung mechanics (8-12 min/rung)
Executed against by SOP-12 P4, SOP-14, SOP-22, SOP-23 P10, SOP-24, SOP-25, SOP-26 P3 and P8, SOP-30, SOP-35. Decides no descent; prices every one.
1. Confirm descent decision arrived from owner: from #23 at taper release (achievement date, push bid, envelope); from #25 (scheduled date); from #26 (cohort and probe instruction); from #35 (incrementality step). No artifact -> return to origin.
2. Read starting bid from T2 **Current Bid $** and confirm vs artifact; mismatch = F11 (derive from live value, record discrepancy).
3. Rung = **current bid x 0.90** (M3 ~10%/week). Write to T4 **Ladder State (step / date)** with date.
4. L2 tests: change inside **50%** of current value; resulting bid >= **$0.50**. Rung below $0.50 truncated to $0.50, truncation recorded (a limit, not a floor).
5. Exit target test (P6): if full 10% step would go below exit bid, rung lands exactly on exit bid = terminal rung (smaller than 10% is compliant).
6. Log hold prediction (position holds at reduced level), review date one read window out (V1). Undated rung = F4.
7. Hold one read window; no second rung before first scored.
8. Read at review date: held, or slipped past tolerance. M3 tolerance has no value (AM-5): record slip magnitude in positions, route to human-mandatory tier.
9. Hold -> record new value as ladder state; derive next rung at its date.
10. Slip -> revert one rung to prior held value and hold. No v4.0 hold period or re-probe count; corpus practice (SOP-25, SOP-26 v2.0) = **two-window hold** and **single re-probe**, applied as corpus practice and logged (AM-8, AM-9).
11. **A failed probe never lowers the register.** Reverted value is the recorded floor until a re-probe holds (F8).
12. Stage every rung through #38 as its own change set with next step's date in reason string.

### P6. Exit-bid discovery and the floor register (10-15 min at derivation; 5 min per update)
1. Compute exit bid at **start** of descent: blended placement CPC at achieved position minus decrement **$0.05-0.10** (F9, L2). Write to T4 **Placement-CPC Exit Bid $**.
2. Select decrement in band and record selection. Corpus value **$0.07** (Economics Worked-Example Set v1.0 case E5 and v1.0); a selection, not governed (AM-6).
3. Re-derive exit bid at each rung; record whether it moved.
4. Record floor when ladder stops: **term, floor bid, date, competitive context note** (Doctrine Section 6.2 makes context note part of the register).
5. Write to T4 **Discovered Floor $** with date; set **Next Step Date** to quarterly re-test. T4 has no context-note column: write note to T6 row of final rung and carry T6 date in register (finding N5).
6. Confirm register entry exists before descent marked complete (F9: ladder state is the taper protocol's memory). Missing = F7; reconstruct from T6 rung chain same day.
7. Hand downstream: #25 at transition exit; #26 for drift restoration and cohort construction; #12 restores to it on drift; #35 reads as defended value.

### P7. Quarterly floor re-test (25-40 min/cohort)
1. Receive cohort from #26 with member terms and recording quarter (SOP does not build or select cohorts).
2. Check G10: armed window or **14-day guard** suspends probe; next date moves out by guard period; record suspension with new date.
3. Run P2 for any member whose probe touches a modifier.
4. Probe rung = one M3 step down from recorded floor, inside L2 and above $0.50. Stage whole cohort in one change set (common read window).
5. Log hold prediction per term with review date.
6. Read at review date; apply P5 steps 8-11. Hold -> new lower floor with fresh context note. Slip -> revert, register unchanged.
7. Produce **register diff**: floors lowered, held, raised, each with date and context note (#26 reads it for released difference at harvest read).
8. Whole-cohort slip = competitive reading; route to v4.0 Section 7 rule **D7** inflation decomposition (market-driven vs self-inflicted) before re-probing. B6 MISSING -> decomposition runs on T5 product log and competitor block; record says so.

### P8. Bleeding-placement response, in lever order (15-20 min/bleeding placement; order never inverts)
1. Confirm one placement failing while others hold (failing everywhere is not a placement problem).
2. Gates first: G3 truncated week voids placement read; budget lever runs, conclusion defers (F12).
3. **Lever 1, premium first:** cut bleeding placement's modifier per P4; run P2; stage; hold one read window.
4. **Lever 2, base bid to bleeder's own CPC:** reduce base to bleeding placement's blended CPC minus F9 decrement. First compute effect on every other placement's effective ceiling (base is shared). If earner's verified weekly contribution at risk exceeds bleeder's weekly loss removed, do not take; step 5 governs.
5. **Lever 3, split** at persistent divergence -> P10 (structural correction, behind bid and placement in L1).
6. **Never a flat bid cut across the campaign** (L3; Doctrine 6.2). WE-3: 30% flat cut leaves PP bleeder $0.155/click unused headroom while stripping $0.29/click from TOS earner.
7. T6 row names lever taken, levers not taken, why.

### P9. Placement arbitrage standup and ROS inverse (M4 pattern) (20-30 min/standup). Raise half suppressed while B7 MISSING; base-siting and inverse executable
1. Entry: proven TOS CVR premium (P1), TOS impression-share deficit on a term whose objective values visibility, clear P2 at target. v4.0 Section 3 family **F6**: deficit line for Ranking campaigns = **TOS share below 30**; S-R7 fires.
2. Site base at ROS economics: at/under ROS max profitable CPC = contribution x ROS CVR.
3. Size modifier so base x (1 + modifier) reaches target TOS CPC (M4 minimum from P2 step 5) and no further.
4. Confirm bidding strategy. Doctrine Section 6.3: **fixed for ranking pushes; down-only default elsewhere**; up-and-down adds platform raise on top.
5. Inverse (ROS harvest) on term with strong organic position: base at ROS economics, modifier zero; needs no proof; legal while B7 MISSING.
6. Log placement-share prediction with review date; re-read at normal cadence.
7. If raise half suppressed: issue verdict, execute executable half, log blocked half vs T7 B7 row per P13 (WE-4).

### P10. Placement-split exact candidacy (15-25 min/candidacy; standup at SOP-12). Source: Doctrine Section 5.2 case 2 (Ledger row 9 records this SOP as implementing)
1. Candidacy: divergent placement economics on one term across qualified reads, persistent not single-window. No window count (AM-15): record windows observed, route to human-mandatory tier.
2. Divergence economic not volumetric: different CVR vs same contribution; compute both placements' max profitable CPC.
3. Split must be cheapest correction (creates second campaign, budget line, wall set). If modifier cut resolves it, cut is the answer.
4. Declare two roles in T3 before campaigns exist: TOS campaign runs P9 arbitrage (modest base, modifier funds premium); ROS campaign base at ROS economics, modifier zero. One of four legitimate duplicate roles in SOP-12 Section 1.2; undeclared pair = SOP-12 P7 territory.
5. Hand standup to SOP-12 P1, run twice, with roles, sited bases, sized modifiers.
6. Walls same session under #29.
7. Log standup prediction (pair combined efficiency vs pre-split blend); each campaign then grades on own placement economics (grading vs pre-split blend violates rule O6).

### P11. Bidding-strategy and effective-ceiling audit (30-45 min/product; quarterly with M3 re-tests). Source: Doctrine Section 6.3
1. Filter T3 to up-and-down campaigns; read **Placement Mult TOS %** and **Bid / AG Default $** (up-and-down + live modifier = target).
2. Run P2 on every row found, whether or not a change is proposed.
3. Rank by (authorized effective ceiling - governing ceiling) $/click x row's weekly clicks = **bounded weekly exposure** (ceiling on exposure, not a saving).
4. Correction = doctrine posture: fixed for ranking pushes, down-only default, up-and-down only with months of validated CVR and explicit ceiling math. Strategy change is a cut in ceiling terms, legal while B7 MISSING.
5. Record **April 2026 auction context** on rows whose CPC rose materially; route through rule D7 before any aggressiveness verdict. Doctrine 6.3 reports category CPC inflation of **18-27% against Q1 baselines** under dynamic raises (market observation, not authorized numeral).
6. Doctrine 6.3 instructs a CPC buffer on push sizing with no figure; v4.0 none (AM-12). Sizing currently unbuffered; record says so.
7. Issue **ladder-hold notice** to #37 naming every row under a live ladder or live worksheet. v4.0 Section 12 rule **P3** resolves collisions in the audit's favour.

### P12. Drift detection and structural-inspection handoff (weekly with P1; 8-12 min/product). Source: F9 drift row, v4.0 Section 4 rule **X6**
1. Read T4 **Drift Flag** (mix shift >15 points over 4 weeks with no logged change).
2. Confirm absence of logged change vs T6 and T5; shift matching a staged set is not drift.
3. Route unexplained drift to structural inspection before performance explanations. X6 fixed inspection order: item 2 = placement multipliers and effective TOS CPC; item 3 = bidding strategy (this SOP supplies both).
4. Sibling divergence: supply effective TOS CPC per sibling instance, not base bids. #33 makes ownership call.
5. Check G11 before any restore on shared term.
6. Write finding to T6 whether or not it produced a change.

### P13. Operating under a suppressed placement feed (every cycle while B7 MISSING; 10-15 min/product)
1. Read T7 B7 at cycle start; stamp status on T4 header.
2. Mark every placement UNREAD (unknown, not zero, not blend).
3. Run cut side in full: P4 normalizations, P8 lever 1 cuts where bleed visible from campaign-grain evidence, P5 rungs, P6 exit bids, P7 probes, P11 strategy corrections, P12 drift routing.
4. Suppress raise side entirely: no modifier increase on any row, verdict, confidence. Raise staged during outage = F10, escalates on discovery.
5. For every verdict requiring a raise: issue verdict, execute executable half, log blocked half against T7 B7 row with **term, campaign, verdict string, supporting evidence** (and dollar consequence). The log is the feed's business case.
6. Carry the statement onto every record (G8; J7).
7. When B7 flips to PRESENT: do not release backlog at once. Run P1 in full for first clean read, hold one window, then work blocked-verdict log in order of weekly loss dollars (A1 MISSING, so first clean read is single-window).

### P14. Scoring, calibration and register diff (weekly for rungs/modifiers; monthly for register diff; 15-25 min). Source: V1, V5
1. Score every due T6 row (rung holds, raise share-shift predictions, cut spend-reduction predictions, split combined-efficiency predictions): HIT, PARTIAL, MISS, WRONG-DIRECTION.
2. Separate error classes on missed rung: market moved (competitive finding -> T5 and D7) vs step too large (mechanics finding -> this document).
3. Monthly floor-register diff: floors lowered, held, raised, and floors past re-test date without probe (the finding; #26's F2 detected from this side).
4. Rule-level accuracy (V5): rule **below 50% accuracy over 10+ scored predictions** enters review (amendment, threshold change, or documented defense). M3 step size most likely to trip it.
5. Attach every missing-feed finding to that field group's T7 row with dollar consequence (same artifact as P13 step 5).
6. Rung with no score = F4; completed ladder with no register entry = F7. Repair from T6 chain.

## 6. Rules, thresholds and numbers

### 6.1 Formulas
| Formula | Definition |
|---|---|
| Effective CPC ceiling | base bid x (1 + placement modifier) x (1 + dynamic raise); dynamic raise 0 under fixed/down-only; up to +100% at TOS under up-and-down |
| Placement max profitable CPC | contribution per order x that placement's CVR |
| CPC ratio | observed CPC / own ceiling, banded per F1 |
| Compliant-pair base | governing ceiling / (1 + target modifier); BLOCKED if no base above $0.50 clears |
| Rung | current bid x 0.90; truncated to exit bid or $0.50 |
| Exit bid | blended placement CPC at achieved position - decrement ($0.05-0.10; corpus $0.07) |
| Bounded weekly exposure | (authorized effective ceiling - governing ceiling) x weekly clicks |
| Cut effect | spend at current vs proposed effective ceiling at constant clicks |

### 6.2 Numeric values
| Value | Meaning | Source |
|---|---|---|
| ~10%/week (x0.90) | Taper step; ~1 week between rungs | v4.0 Section 10 rule M3 |
| 50% | Per-change limit on bid values (not modifiers moving to zero) | rule L2 |
| $0.50 | Bid floor | rule L2 |
| $0.05-0.10 | Exit decrement below blended placement CPC | F9 and L2 |
| $0.07 | Corpus decrement selection (ungoverned) | Economics set E5, v1.0 |
| 15-25% | UNLOCK TRAFFIC bid steps | rule L2 / S-R1 |
| 20-30% | Budget step (S-P4; AM-3 notes budget steps 20-30%) | v4.0 |
| <=0.8 / 0.8-1.0 / 1.0-1.5 / >1.5 | SAFE / AT-CEILING / PUSH-ONLY / UNJUSTIFIABLE CPC-ratio bands | family F1 |
| 30 | TOS IS % deficit line on Ranking campaigns | family F6, S-R7 |
| 12-25 | KDR TOS IS band (WE-4 reading of 18) | KDR |
| >15 points over 4 weeks | Placement drift flag with no logged change | family F9 |
| >=25% over 4 weeks | Bid gap widening = auction-moved signal (needs B6) | family F9 |
| 1.5x | Marginal ACOS vs average ACOS saturation freeze; re-test in 2 weeks | rule X11 |
| 2 weeks | Re-read after TOS-VANITY cut (S-P5); incrementality capture window (#35) | S-P5, X12 |
| Halve / standard / upper end | Lever step at LOW / MEDIUM / HIGH confidence | rule M10 |
| 15+ clicks/7d; 100+ clicks; 1,000+ impressions; 60-day fallback | G2 bid read / CVR verdict / CTR verdict | gate G2 |
| 70% | In-budget truncation line (KDR alias 51-70 strained) | gate G3 |
| 85% | DEGRADED packet floor; live 0.571 | gate G8 |
| 7 days | Price stability window | gate G9 |
| 14 days | Post-event exclusion / probe guard | gate G10 |
| 500+ SV; bid >25% | Human-mandatory tier | rule P5 |
| 50% over 10+ predictions | Rule review | rule V5 |
| Quarterly | Floor re-test, or after logged competitive shock | M3, V4 |
| 0-900% | Platform modifier range | Doctrine 6.1 (AM-11) |
| Up to doubling at TOS | Up-and-down dynamic raise | Doctrine 6.1 (AM-11) |
| +/-15% hourly; 4+ weeks | Dayparting lever (not built) | rule L10 |
| 18-27% vs Q1 | Category CPC inflation, April 2026 (observation) | Doctrine 6.3 |
| $2.80 | Account Expected CPC reference in use (A6 PARTIAL) | T7 |
| 0.571 | Live packet completeness | T7 |

### 6.3 v4.0 rule references
| ID | Meaning as described |
|---|---|
| F1 | Max profitable CPC and CPC-ratio bands |
| F6 | TOS share deficit line 30 on Ranking campaigns |
| F9 | Placement decomposition classes; blended placement CPC exit row; drift row; auction-moved signal; ladder state is taper's memory |
| F10 | Truncation as step-zero precondition |
| F12 | Listed in companions |
| X2 | Raising modifier against conversion deficit buys more of the same rejection |
| X6 | Fixed structural inspection order (item 2 multipliers/effective TOS CPC, item 3 bidding strategy) |
| X9 | Product log ahead of any attribution to bids |
| X11 | Saturation: marginal ACOS >1.5x average, freeze, re-test 2 weeks |
| X12 | Rung doubling as incrementality step |
| G1-G12 | Gates (see 4.2) |
| O6 | Placement graded on objective band the row inherits; grading split vs pre-split blend is violation |
| O8 | Listed in companions |
| D1 | Diagnosis required before placement adjustment (L3) |
| D7 | Inflation decomposition (market-driven vs self-inflicted) |
| S-A3, S-A9 | S-A9: margin-table change puts every keyword with CPC above new ceiling in ladder queue |
| S-R1 | UNLOCK TRAFFIC; review modifiers suppressing serving |
| S-R3 | Traffic deficit: TOS multiplier and budget as levers (no magnitude) |
| S-R6, S-R10 | Listed in companions |
| S-R7 | TOS share below floor: placement problem precedes any bid verdict |
| S-R13 | Routed into RANK PUSH AT CONTROLLED CPC |
| S-P1, S-P4 | S-P4 = profitable headroom with budget step 20-30% (instruments mis-cite it; N2) |
| S-P5 / S-P6 | TOS-VANITY / PP-LEAK |
| S-M2, S-M5, S-D1, S-F3, S-F8 | Listed in companions |
| S-C1 to S-C6 | PAT/conquest scenarios (A8 PARTIAL gap) |
| L1 | Lever precedence: budget, bid, placement, then structure |
| L2 | 50% per-change limit, $0.50 floor, exit decrement, 15-25% unlock steps |
| L3 | Placement adjustment only after G2 and D1; no flat cut |
| L4 | Listed in companions |
| L8 | Format substitution (SBV) paired SP-exact step-down |
| L10 | Dayparting |
| M3 | ~10%/week step, reversion on slippage, quarterly re-test |
| M4 | Multiplier sizing: effective TOS CPC <= min(max profitable CPC, Expected CPC + tolerance) |
| M7 | Review trigger |
| M10 | Confidence modulation |
| P1 | G6 RED outranks placement posture |
| P3 | Audit value wins over automation |
| P5 | Human-mandatory tier |
| P8 | Data quality above urgency |
| J7 | Hiding a fallback is a process violation |
| V1 | Next cycle's first step is scoring the last |
| V4 | Weekly full audit; quarterly floor re-tests |
| V5 | Rule review below 50% over 10+ |
| V8 | Training corpus |

## 7. Data inputs required

**Catalog field groups (by ID):** A1 four-period comparability (MISSING), A3 pacing and in-budget, A4 sufficiency buckets, A5 threshold flags, A6 objective and per-term Expected CPC (PARTIAL), A7 eligibility, A8 PAT rows first-class (PARTIAL), B6 bid intelligence (MISSING), B7 placement splits TOS/ROS/PP (MISSING; source "TOS placement report"), B8 economics chain, B11 market context, D1 per-variation margin (PARTIAL), D2 keyword-variation map (PARTIAL), D6 sibling CPC view (PARTIAL), D7 decision log and V5, D12 hourly dayparting (reserved, unbuilt).

**T4 Placement & Bid (primary surface, all twenty columns), named:** Impressions, Clicks, CVR, CPC $, CPA $, Spend Share %, Sales Share %, IS %, Placement Verdict (values PREMIUM EARNED / CUT MULTIPLIER / EXIT PLACEMENT), Ladder State (step / date), Next Step Date, Discovered Floor $, Placement-CPC Exit Bid $, Drift Flag, Expected CPC; tab header cycle line.

**T3 Campaign Board:** Bid / AG Default $, Placement Mult TOS %, Placement Mult PP % (no ROS column; N4), Bidding Strategy, Truncation Flag (G3), In-Budget Bucket, Objective Tag; declared split roles.

**T2 Keyword Command:** Max Profitable CPC $, Expected CPC $, CPA Ceiling $, Current Bid $, Suggested Bid / Gap %, TOS Modifier %, TOS IS %, Marginal ACOS, ACOS, Family Conflict, Term Owner (Family), Clicks 7/30/60d, Sample State, Flag: Zero-Quarantine, Validation State, Eligibility, Inventory Band, Days to Stockout, Targeted Variation(s), Envelope Status, Margin $/Unit, Event Mode, Syntax Tags, Relevancy; block K8 competitor block; block K9 verdicts; OVERSIGHT filter.

**T0 Product Command:** zone C economics spine (AOV, contribution per order, break-even ACOS, Target ACOS, Max Acceptable, Expected CPC reference, margin table version and fresh/provisional state); zone H envelope headroom.

**T5 Product Log:** Event Type (price move, competitor entry), Trend-Exclusion Flag. **T6 Decision Log:** rungs, predictions, Review Date, V5 Score. **T7 Manifest:** status per group, completeness rollup. **Account Rollup:** A1 (term owner), A2 (budget).

**From other components:** #23 push worksheet / authorized CPC envelope, achievement date, push bid (I-4); #25 descent schedule; #26 cohort re-ladder instruction; #35 continue-or-restore call; #32 armed-window declaration; #33 family ownership declaration; #38 T+1 diff; #37 rule change log; #22 launch placement evidence; #41 per-variation margin table; Data Operations / #39 Raw Pull Pack (Monday 06:00).

## 8. Outputs and artifacts (Section 8)

| Artifact | Produced by | Storage and retention | Downstream consumer |
|---|---|---|---|
| Weekly placement read | P1 | T4, one row per oversight keyword per placement, cycle line on header; append-only log life | P3, P8, P12; #26 bleed evidence; T7 rows |
| Ceiling worksheet | P2 | Attached to change, referenced from T6; life of campaign | #38 pre-upload effective-CPC scan; #23 envelope test; next raise |
| Staged modifier change | P3, P4 | #38 staged set (verdict, scenario ID, SOP/procedure, worksheet result, proof ratio); T6 prediction | #12, #38, V5 |
| Dated rung | P5 | T4 Ladder State and Next Step Date; one T6 row per rung, append-only | #12 P4 and P11; #25; #26 P3 and P8; #35; #37 hold notice |
| Exit bid | P6 | T4 Placement-CPC Exit Bid $, re-derived each rung, prior in T6 | P5 step 5; #23; #30 seeds |
| Floor register entry | P6 | T4 Discovered Floor $ with date and Next Step Date; context note on final rung's T6 row; life of term | #25, #26, #12, #14 (Surface 3 defense floor), #35. Taper's gate artifact |
| Register diff | P7, P14 | Per cohort quarterly and monthly across product | #26 released-difference harvest read; P14 |
| Bleed response record | P8 | T6: lever taken, not taken, computed comparison | #26 cut sequence; F3 audit; V5 |
| Standup record | P9, P10 | T3 declared roles; T6 combined-efficiency prediction | #12 P1; #29 walls; registry |
| Audit finding list | P11 | Ranked by bounded weekly exposure, quarterly; ladder-hold notice | #37; #12; BM owner review |
| Blocked-verdict log | P13 | Against T7 B7 row: term, campaign, verdict string, evidence, dollar consequence; until feed lands | Data Operations and #39 business case; P13 step 7 work order; #26, #23 |
| Scored rung chain | P14 | T6 with V5 scores and two error classes; indefinite | V5 rule accuracy; V8 training corpus; v4.1 brief |

Retention ungoverned (AM-13).

## 9. Verdict-to-execution mapping (Section 5)

KDR Template v3.0 "Bands & Verdicts Reference" strings, with v4.0 Section 13.1 cross-map per Ledger conflict C10.

| KDR verdict | v4.0 13.1 cross-map | Placement and modifier execution |
|---|---|---|
| QUARANTINE: DATA REFRESH | FLAG: DATA REPAIR | Row leaves every read, ladder, worksheet; staged rung pulled (G1; rule P8) |
| UNLOCK TRAFFIC | No 13.1 member; S-R1 text | Bid steps 15-25% (L2) at SOP-12; reviews modifiers suppressing serving; raises none while B7 MISSING |
| FIX BUDGET (TRUNCATED) | No member; G3 response | Budget lever at #12; placement read void (F12 if ignored) |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | EXTEND TEST | No modifier change, no rung |
| FUND TEST (UNFUNDED PRIMARY) | FUND DELIBERATE TEST (50-CLICK CAP) | Modifiers zero at standup (L3) |
| RANK PUSH: FUND SIZED PUSH | RANK PUSH AT CONTROLLED CPC | Modifiers zero unless placement evidence exists; in-flight modifiers tested vs #23 envelope (I-4) |
| RECOVERY PUSH | No member; S-R13 routes into RANK PUSH AT CONTROLLED CPC | As above; pre-OOS ladder state and floor supplied to #24 as recovery bracket |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | No member; S-R3 text | Budget half at #12; multiplier half logged blocked (P13 step 5) |
| FIX CONVERSION FIRST; DEFER PUSH | Identical | No modifier moves (X2) |
| PLACEMENT FIX FIRST | No member; S-R7 text | The component's verdict: bids hold at #12; P1, P2, P9, P8. While B7 MISSING executable half named (WE-4) |
| RE-POINT VARIATION | Identical | #12 P10 same day; exit bid re-derived vs backup variation's own placement CPCs |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | TAPER TO FLOOR (POST-OBJECTIVE) | P5 in full, P6; execution #12 P4 |
| HOLD; DEFEND LIGHTLY AT RANK | No member; near-neighbour DEFEND AT FLOOR | No rung, no modifier change; logged as verdict |
| DEFEND AT FLOOR | Identical | No change at floor; drift above floor -> supply floor, #12 restores in one step (no worksheet) |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Identical | Bid edit at #12 to K6 max profitable CPC inside L2; cut >50% -> compliant multi-step program with dates |
| INCREMENTALITY LADDER | No member; mechanism at X12 | Stage single rung, record floor; two-week capture read and call at #35; confounded window -> void, no floor |
| ADD EXACT + RESTRUCTURE | Identical | Standup at #12 P1/P2, walls #29; modifiers zero at creation |
| CONSOLIDATE DUPLICATES | No member; carried inside ADD EXACT + RESTRUCTURE | #12 P7; survivor's modifiers sized from loser's placement evidence (#12 P7 step 4) |
| GRADUATE FROM DISCOVERY | GRADUATE + STEER | Owned by #30; supplies exit-bid seed where related root floor exists, else modifiers zero |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | CUT / NEGATE | Owned by #29; no placement execution |
| ENTER SBV ARBITRAGE | FORMAT SUBSTITUTION (SBV/SD) | Single SP-exact ladder step down (L8) dated to SBV go-live; one M3 rung, not cut to floor; video build #17-19 |
| OPEN / ROTATE / EXIT CONQUEST | No member; S-C1 to S-C6 | Owned by #16; PAT rungs carry A8 PARTIAL gap |
| STOP-LOSS: CONCEDE OR DEFER | Identical | Concede: step program from push bid to Conversions ceiling (multi-step per L2). Defer: ladder state and floor preserved |
| PAUSED-PENDING (REASON + RE-ENTRY) | PAUSE (LEVERS EXHAUSTED) | #12 P8; ladder state and floor survive pause (else F7) |
| LEAVE TO HARVEST | Identical | No exact, no placement program; discovery modifiers follow hosting campaign's O6 band |

**Campaign-level (5.1):** FUND / HOLD / TRIM BUDGET, RAISE / CUT MULTIPLIER, NEGATION PASS, CONSOLIDATE, RETAG OBJECTIVE, PAUSE (L7), ARCHIVE. RAISE MULTIPLIER only from P3 with all three conditions and P2 clear; suppressed while B7 MISSING. CUT MULTIPLIER from P4 and P8 lever 1, always legal. TRIM BUDGET follows (not leads) a bid/modifier cut.

**Retired strings (5.2):** RAISE MODIFIER (proof + worksheet), NORMALIZE MODIFIER, ENTER ARBITRAGE / ROS HARVEST, TAPER (from any SOP), RE-LADDER (QUARTERLY), PLACEMENT-SPLIT. Operations survive as procedures: raise P3 -> RAISE MULTIPLIER; normalization P4 -> CUT MULTIPLIER; arbitrage/harvest P9 -> PLACEMENT FIX FIRST; taper P5 -> TAPER: RANK ACHIEVED, STEP BIDS DOWN; quarterly re-test P7 -> DEFEND AT FLOOR or HOLD; DEFEND LIGHTLY AT RANK; split P10 -> ADD EXACT + RESTRUCTURE.

**Fourth vocabulary (5.3):** Data Architecture v1.0 Section 8 and Command Workbook T4 Placement Verdict values PREMIUM EARNED, CUT MULTIPLIER, EXIT PLACEMENT. Only CUT MULTIPLIER is in KDR campaign subset. SOP writes T4 with them (data-validation list) but issues verdicts from closed vocabularies (finding N3).

## 10. Decision rights

**Executable with audit:** full T4 read (P1), worksheet computation (P2), compliant-pair solve, rung derivation on schedule, exit-bid re-derivation, F5 expired-justification scan, drift test, P11 bounded-exposure ranking, register diff assembly, V5 scoring drafts.

**Human-mandatory:** every raise deployment and every arbitrage or split standup (rows "Structure creation (all SOPs)" and "Bulk deployments (#38)"); every re-ladder probe on a defended head term ("Weekly verdicts (established US)"); every F11 rule suspension ("Automation rules (#37)"); incrementality rung handoff ("Incrementality tests"); any restore step on a shared term ("Sibling declarations (S-series)"); every proof-ratio clearance until AM-1 lands. Rule P5 adds every 500+ SV action, gate failure, structural change, bid move >25%. Every slip (AM-5) and split candidacy (AM-15) routes to human tier.

| Authority Matrix row | Rights |
|---|---|
| Weekly verdicts (established US) | PPC Lead decides; incoming operator and PPC Manager execute; BM owner reviews (daily huddle = review not veto); CEO informed |
| Bulk deployments (#38) | PPC Lead reviews; incoming operator and PPC Manager execute; launch operator executes own scope |
| Structure creation (all SOPs) | PPC Lead decides or per SOP scope; incoming operator, launch operator, PPC Manager execute |
| Automation rules (#37) | PPC Lead decides; incoming operator executes and reviews; PPC Manager executes; CEO informed |
| Incrementality tests | PPC Lead reviews; incoming operator decides and executes; CEO and BM owner informed |
| Sibling declarations (S-series) | PPC Lead decides; incoming operator executes; BM owner reviews; CEO informed |
| Event plans (#32) | PPC Lead decides with deals calendar owner; operator executes; BM owner reviews |
| v4.0 threshold changes | CEO decides; PPC Lead executes and reviews; everyone else informed |

Vacancy rule: unfilled role's D reverts to PPC Lead, E to PPC Manager. Scope via Transition Brief v1.2.

**Cadence:** weekly T4 read, F5 scan, drift, due rungs in Monday cascade; deploy **Tuesday** via #38; **T+1 diff Wednesday**; per rung date where #25 sets other dates; monthly register diff; quarterly P7 re-tests and P11 audit; same day for G4 flip, G6 RED, S-A9 margin change, #23 taper release; every cycle P13 while B7 MISSING.

**Alarm routing:** same day to operator queue F6, F10, F11, F12; weekly worklist F2, F4, F5, F8; PPC Lead with T6 chain F1, F3, F7, F9 and any mode recurring in consecutive cycles. F6 and F10 escalate on discovery; F1 recurring escalates with raiser attributed; F11 to PPC Lead with T6 chain and #37 rule identity.

## 11. Failure modes (Section 7)

| ID | Failure | Detection | Response | Motivating incident |
|---|---|---|---|---|
| F1 | Modifier raised without placement proof | Raise with no proof ratio in reason string, or ratio on sub-sufficiency traffic | Normalize to zero at P4 same day; re-raise via P3 if proof exists | v1.0; Doctrine Section 14 named account failure class |
| F2 | UNREAD placement treated as read | Premium on placement below sufficiency, or verdict on row with B7 build marker | Normalize to zero; probe traffic first | v1.0; G2, L3 |
| F3 | Flat bid cut on single-placement bleed | Whole-campaign reduction where T4 shows one placement failing | Reverse to P8 order; restore earners | v1.0; WE-3: strips $0.29/click from earner, leaves bleeder $0.155/click headroom |
| F4 | Undated or unpredicted rungs | T4 Ladder State with no date, or rung with no T6 prediction/review date | Re-stage with date and prediction | v1.0; V1, F9 |
| F5 | Premiums outliving justification | Modifier live past closed push, ended deal, achieved/tapered rank (T3 Objective Tag vs T6) | P4 normalization; weekly scan | v1.0; Doctrine 14; v4.0 Section 16 Worked Pass 1: head term held at rank 2 vs target 3 for five consecutive weeks, Ranking objective expired three weeks earlier, spend never reduced |
| F6 | Up-and-down beneath live modifier, no worksheet | P11 finding | Worksheet immediately, then doctrine posture; escalates on discovery | v1.0; Doctrine 6.1: $1.50 bid + 300% TOS under up-and-down = $12.00 click |
| F7 | Floors unrecorded or lost at a pause | Completed ladder with no Discovered Floor $; term re-entering from PAUSED-PENDING at re-derived bid | Reconstruct from T6 chain same day with T5 context note | v1.0; F9; Ledger row 26 |
| F8 | Failed probe lowering register | T4 floor written on slipped rung, or re-test date advanced after reverted probe | Restore to last held rung, re-date | M3; SOP-26 v2.0 WE-3 confounded probe |
| F9 | Rung outside L2 limits | Step >50%, below $0.50, or multi-step target compressed into one | Re-stage as dated compliant program | SOP-26 v2.0 WE-1: code-red cuts needed two steps; 82.2% of saving landed week 1 |
| F10 | Modifier increase while B7 MISSING | #38 pre-upload scan or T+1 diff | Pull row; if deployed normalize same day; escalates on discovery | D3 OPEN; SOP-23 failed push $3,378.00 on B7 row |
| F11 | Automation and ladder stepping same bid | T6 rung chain interrupted by rule-fired change; current bid >1 rung from recorded state without human confirmation | Suspend rule pending #37 review, restore ladder state, re-issue P11 step 7 notice (rule P3) | SOP-26 v2.0 WE-1: rule stepped defensive term up six times from floor $0.62 to $1.10, $0.48/click premium across four rows at 380 clicks/week = $182.40, 11.3% of that week's overspend |
| F12 | Placement decision on truncated/quarantined week | G3 flag fired or Zero-Quarantine set | Void week's read, budget lever first | F10, G3 |

Any mode twice in consecutive cycles on same scope escalates regardless.

## 12. Interface contracts (Section 12)

22 handoffs. SOP-25 attached at v1.0 while Ledger records v2.0; SOP-24, SOP-32, SOP-33 rebuilt concurrently in Wave 5A, so their seams are from Ledger rows (Ledger v2.5 correction-register guidance).

### Upstream
| ID | Counterpart | Artifact and timing | Non-arrival |
|---|---|---|---|
| I-1 | Data Operations and #39 | B7 placement splits TOS/ROS/PP from TOS placement report; weekly with Raw Pull Pack Monday 06:00 | Live state. All UNREAD, raises suppressed, P1 structural, P13 governs; cuts/rungs/floors unaffected. D3 OPEN |
| I-2 | Data Operations and #39 | B6 suggested bid and gap; weekly | Auction-moved signal uncomputable; P7 step 8 falls back to T5. MISSING |
| I-3 | #41 economics | Per-variation margin table into T0 zone C; monthly and on event before Monday packet-ready | G9 PROVISIONAL on every ceiling; training base. D1 OPEN |
| I-4 | #23 | At taper release: achievement date, push bid, authorized CPC envelope; any in-flight modifier request | First rung guessed; in-flight falls back to maintenance ceiling, blocks legitimate push changes |
| I-5 | #25 | Dated rung instruction per term; weekly through descent | F4 from outside; descent stalls, invisible |
| I-6 | #26 | Cohort re-ladder instruction (members, recording quarter) quarterly; bleed cut decision inside cut sequence, same day | Floors unre-tested; code-red placement lever skipped or flat cut (F3) |
| I-7 | #35 | Continue-or-restore call at end of two-week capture window | Rung holds, no floor recorded |
| I-8 | #32 | Armed-window declaration with dates and affected campaigns; in-window allowance | G10 not applied; P7 step 2 suspends affected cohorts if plan absent |
| I-9 | #33 | Family ownership declaration before restore | G11 bars restore; escalate to #33 |
| I-10 | #38 | T+1 diff on every staged rung and modifier set | Slip vs never-landed indistinguishable |
| I-11 | #37 | Rule change log covering ladder window; held-rows confirmation | F11; unscoreable chain |
| I-12 | #22 | Launch placement evidence at standing-owner co-sign | Standing owner rediscovers; Ledger row 22 records as its I-16 |

### Downstream
| ID | Counterpart | Artifact and timing | Non-arrival |
|---|---|---|---|
| I-13 | #12 | Rung value with date, compliant pair, multi-step program; same cycle, same day on dated release | Taper stalls (SOP-12 F5, account's most expensive known failure class); half a pair worse than none |
| I-14 | #25 | Step values and exit targets per scheduled date | Locally derived step = invented threshold; Ledger row 25 I-4, capped by D3 |
| I-15 | #26 | Floor register format and content, register diff, lever order | No drift reset, no re-ladder baseline, no harvest verification |
| I-16 | #23 | Worksheet result on in-flight modifier vs push envelope | Sized push becomes unsized |
| I-17 | #38 | Staged sets with verdict, scenario ID, procedure, worksheet, next step date; Tuesday default | Rung silently does not happen |
| I-18 | #35 | Staged incrementality rung; recorded floor as defended value | Test measures nothing |
| I-19 | #14 | Surface 3 defense floor and exit-bid reference for defensive brand broad | Defense budget at untested price (Ledger row 14) |
| I-20 | #30 | Exit-bid reference and related root floor for seeding graduated exact; same day | Graduate starts above known floor (Ledger row 30) |
| I-21 | #37 | Ladder-hold notice each cycle ahead of rungs | Automation fights ladder |
| I-22 | T6 and verification layer at #6 | Dated predictions, V5 scores, separated error classes | M3 accuracy cannot compute |

## 13. Account-specific facts

- Live manifest: B7 MISSING, B6 MISSING, packet completeness **0.571**; A6 PARTIAL with account Expected CPC reference **$2.80**; D1 PARTIAL; A8 PARTIAL; A1 MISSING; D2 PARTIAL (backup chain on head terms only); D6 PARTIAL; B8 PRESENT on blended margin; D12 MISSING (deferred). Ledger D3 and D1 OPEN.
- Modifier increases suppressed account-wide as of this version.
- SOP-23 session traced a failed push of **$3,378.00** to the B7 row.
- Recorded automation incident (SOP-26 v2.0 WE-1): floor $0.62 stepped to $1.10, $182.40, 11.3% of week's overspend; code-red sequence 82.2% of saving in week 1.
- v4.0 Section 16 Worked Pass 1: head term held at rank 2 vs target 3 for five weeks after objective expired.
- April 2026 auction context: category CPC inflation 18-27% vs Q1 baselines under dynamic raises (Doctrine 6.3).
- "23 shipped SOPs" referenced; Wave 5A has four concurrent sessions; Ledger v2.5 conflicts run to C18.
- Worked examples use fictional training base (AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3%, CVR 5.2%); anonymized live per-variation spine not attached.

### Worked examples (illustrative)
| Case | Key figures |
|---|---|
| WE-1 Ceiling worksheet | Contribution $28.00, CVR 5.2% -> governing $1.456; base $1.30 + 25% TOS down-only = $1.625 (over by $0.169) -> BLOCKED; compliant base <= $1.1648, staged $1.15 -> $1.4375 (headroom $0.0185), base cut 11.54%; at 30 clicks/week $48.75 -> $43.13. Warning: $2.20 x 2.50 x 2.00 = $11.00 = 7.55x ceiling (UNJUSTIFIABLE; F6). RAISE MULTIPLIER human-mandatory but does not stage under B7 MISSING |
| WE-2 Ladder | Push bid $2.60, blended placement CPC $2.31 -> exit $2.24; rung 1 $2.34 (10.00%), rung 2 $2.24 (4.27% terminal); total 13.85%; rung 2 slips, reverts to $2.34, register unchanged; T5 shows two competitor deal windows (X9) -> probe uninformative; re-probe two windows later holds at $2.24. Weekly spend 30 clicks: $78.00 -> $67.20 (save $10.80; $561.60/yr); premium vs $1.456 = $0.784/click = $23.52/week ($3.36/day); organic contribution protected 3.1 orders/day x $28 = $86.80/day; protection ratio 25.8:1. E5 governs vs SOP-26 WE-3 ($23.40, $3.34; N6) |
| WE-3 Bleeding PP | Base $1.80, TOS 0%, PP +25%, down-only. TOS 150 clicks $1.55 CVR 6.4% net +$36.30 ACOS 30.27% ceiling $1.792 ratio 0.86; ROS 220 clicks $1.05 CVR 4.5% net +$46.20 ACOS 29.17% ceiling $1.260 ratio 0.83; PP 130 clicks $1.42 CVR 1.2% net -$140.92 ACOS 147.92% ceiling $0.336 ratio 4.23; blended 500 clicks $1.2962 $648.10 CVR 4.212% net -$58.42 ACOS 38.47%. PP = 28.48% of spend, 7.41% of sales. Lever 1 PP to 0%: week 2 PP 74 clicks $1.18 CVR 1.4% net -$58.31; loss removed $82.61; campaign net +$24.19. Lever 2 exit $1.11 = 38.33% base cut, risks TOS $36.30 to remove $58.31 (bounded gain $22.01, can be negative) -> P10. Flat 30% cut to $1.26 strips $0.29/click from TOS, PP keeps $0.155 headroom |
| WE-4 Arbitrage blocked | Ranking term, base $1.15, TOS 0%, up-and-down; blended CVR 4.9%, ROS 4.5%; 214 clicks; in-budget 100%; inventory GREEN; TOS IS 18 (KDR 12-25 band; below 30) -> S-R7. Governing $1.372; up-and-down authorized $2.30 (1.68x UNJUSTIFIABLE); fixed $1.15 (0.84x AT-CEILING); bounded exposure 63 x $1.15 = $72.45/week. ROS ceiling $1.26 (base at 0.91). Three blocks: AM-1 no bar, B7 missing TOS CVR, AM-4 no tolerance (+A6 $2.80). Verdict PLACEMENT FIX FIRST; executable half = strategy to fixed; blocked half logged with 12-point share gap |

## 14. Open items

### 14.1 Amendment register (16 items, Section 13.1)
| ID | Gap | Where it bites |
|---|---|---|
| AM-1 | No factor for placement CVR proof ratio ("materially above"). **Highest priority** | P3 step 2, P9 step 1, WE-4 |
| AM-2 | No per-placement traffic minimum (G2 is keyword/campaign grain) | Section 3, P1 step 6 |
| AM-3 | No modifier step size (bid steps ~10%/week, budget 20-30%; S-R3 no magnitude; v1.0 +25% pattern retired) | P3 step 6, P4 step 5 |
| AM-4 | M4 tolerance has no value | P2 step 5, WE-4 |
| AM-5 | M3 slippage tolerance has no value (duplicates SOP-25 item) | P5 step 8, P7 step 6 |
| AM-6 | No rule selects within $0.05-0.10 decrement ($0.07 corpus) | P6 step 2, WE-2 |
| AM-7 | No product-page CVR norm (S-P6) | P1 step 5, P8 step 1 |
| AM-8 | No hold period for reverted rung (corpus two-window) | P5 step 10, P7 step 6 |
| AM-9 | No re-probe count (SOP-26 v2.0 P3 single re-probe) | P5 step 10, P7 step 6 |
| AM-10 | No lag from taper release or bleed detection to procedure (duplicates SOP-25, SOP-30, SOP-17/18/19) | Section 2, P5 step 1, P8 |
| AM-11 | 0-900% modifier range and up-to-doubling dynamic raise not in v4.0 | P2 step 2, P11, WE-1, WE-4 |
| AM-12 | No CPC buffer for 2026 auction (duplicates SOP-23) | P11 step 6 |
| AM-13 | Record retention (duplicates SOP-25, SOP-26, SOP-29, SOP-30) | Section 8 |
| AM-14 | Gate numbering (duplicates Ledger C9) | Section 3 |
| AM-15 | No persistence bar for split candidacy | P10 step 1, Section 2 |
| AM-16 | No horizon for normalizing expired modifier justification (duplicates SOP-25) | P4 step 2, F5 |

### 14.2 Conflicts and findings
Registered Ledger conflicts binding this component and applied: **C3** (budget instrument naming), **C9** (gate numbering), **C10** (verdict vocabulary cross-map), **C17**, **C18**. Ledger register runs to C18 at v2.5; build brief pre-declared C1-C7. New findings N1-N7 (not C-numbered because Ledger v2.5 numbering rule assigns C-IDs at close-out):

| ID | Finding |
|---|---|
| N1 | Dayparting lever has two IDs: v4.0 L10 dayparting and L8 format substitution; Data Architecture Section 8 cites hourly columns as "(L8)" and T7 row D12 reads "L8 dayparting (reserved, do not build)" |
| N2 | Placement verdict set cited to wrong scenario: Data Architecture Section 8 "per S-P4" and T7 B7 "All T4 placement verdicts; S-P4; M4 arbitrage"; S-P4 is profitable headroom budget step 20-30%; correct are S-P5 and S-P6 |
| N3 | Fourth verdict vocabulary at placement grain (PREMIUM EARNED, CUT MULTIPLIER, EXIT PLACEMENT); extension of C10 and C18 |
| N4 | Instrument has two modifier columns (TOS, PP) where doctrine has three placement groups; no ROS column in T3 |
| N5 | Floor register has no context-note column in T4 |
| N6 | WE anchor at two figures: E5 $23.52/$3.36 vs SOP-26 WE-3 $23.40/$3.34 (rounding to $1.46); E5 governs; correct SOP-26 |
| N7 | SOP-25 v1.0 P5 and SOP-26 v2.0 P3 steps 4-8 restate ladder mechanics incl. ungoverned two-window hold and single re-probe; recommend they cite SOP-28 P5 by reference |

### 14.3 Missing / dependent items
- Ledger D3 (placement feed) OPEN; D1 (per-variation margin) OPEN; B6 MISSING; D12 deferred to #45.
- SOP-25 attached only at v1.0; SOP-24, SOP-32, SOP-33 in concurrent Wave 5A rebuild.
- #31 has no procedural document (C3).

### 14.4 Version review triggers (Section 10.1)
Any v4.0 increment touching L1, L2, L3, L8, M3, M4, M7, M10, F9, S-P5, S-P6, S-R7; any AM item landing (AM-1 and AM-3 convert P3 steps to mechanical tests); D3 landing (retires P13, makes P3 executable, opens backlog); D1 landing; B6 landing; any Amazon placement-control change (new placement group, modifier range, dynamic-raise behaviour); changes to #23 push worksheet/envelope, #25 descent schedule, #26 cohort construction; resolution of C9 or C10; quarterly minimum.

### 14.5 Live-defense questions (Section 11.1)
1. 38% blended vs 35% BE hiding $140/week PP loss (per-placement ceiling ratio). 2. Why exit bid below blended CPC. 3. Arithmetic before lever 2 (shared-base comparison). 4. Cost of modifier today, base cut Thursday. 5. Why register does not move on slip. 6. Siblings at same base paying differently (base, modifier, strategy). 7. TOS 18% vs 30% with no feed: verdict, executable half, blocked log. 8. Step program $3.10 -> $0.84 takes two weeks (L2 50%). 9. How an $11.00 click is assembled. 10. Three things the SOP cannot decide and who decides.

### 14.6 Companions
Criteria System v4.0 (sections listed in 6.3); KDR Template v3.0 "Bands & Verdicts Reference" and "Campaign Decision Record"; PPC Strategic Doctrine v1.0 Sections 5.2, 6.1, 6.2, 6.3, 13, 14, 15; Economics Worked-Example Set v1.0 case E5; Authority Matrix v2.0 Section 1; Master PPC Data Architecture v1.0 Sections 4, 6, 7, 8, 9, 12; PPC Command Workbook TEMPLATE v1.0 tabs T0, T2-T7; SOP-12, 14, 22, 23, 24, 25, 26, 29, 30, 32, 33, 35, 37, 38; Cross-Reference Ledger v2.5 (row 28, D3, C1-C18).
