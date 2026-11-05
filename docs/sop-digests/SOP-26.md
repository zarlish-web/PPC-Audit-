# SOP-26 Digest: Mature and Defend Operations, Including the Code-Red Protocol

Source: `PPC_SOP_26_Mature_Defend_and_Code_Red_v2_0.pdf` (18 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-26: Mature and Defend Operations, Including the Code-Red Protocol (Component #26 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead, with the Brand Management counterpart per product on the defended-set declaration |
| Supersedes | SOP-26 v1.0 (2026-07-24) in full |
| Thresholds | Master PPC Decision Criteria System v4.0 and Keyword Decision Record Template v3.0 only; zero local thresholds |

**Verdict / purpose.** "Mature operations are floor operations." The product holds its earned position at the lowest CPC that still holds it; the difference between last quarter's price and this quarter's floor is harvested and re-queued; and blended efficiency above the mature band is treated as the emergency the Criteria System says it is, not as a bad week. Governs the mature stage from entry to exit: weekly posture read, floor maintenance and drift restoration, quarterly re-ladder by term cohort, standing defensive architecture and membership register, annual defense-cost read, breach-band holding, code-red declaration and same-day freeze, four-map diagnosis, loss-dollar cut sequence, first re-read, exit-test close with structural escalation branch, incursion detection and response inside the defense ceiling, monthly profit-harvest read funding the queue, and post-exit review turning every recovery into an amendment proposal.

v2.0 vs v1.0: procedures 5 -> 14; verdict mapping 5 rows -> full 25; worked examples 1 -> 4; failure modes 5 -> 12; adds operator ramp and sixteen interface contracts. **Three corrections of substance**:
1. Code-red trip restated as v4.0's **two-part test** (not v1.0's single-limb 1.5x reading).
2. Protocol close moved from **day 14** to the **two-consecutive-week exit test** of rule R5.
3. Four locally minted v1.0 verdict strings retired.
Also: v1.0 P5 "#31" citation retired (C3, AM-9); v1.0 48-hour diagnosis window retired (AM-12). Thresholds carried forward with traces re-verified: mature band 4-7% and quarterly floor re-test.

### 1.1 The two operating states and the band separating them
Read from one number: **product TACOS vs the mature stage band**. v4.0 Section 3 F2: **Mature 4-7%**; deviation **WITHIN <= 1.2x band; ELEVATED 1.2-1.5x; BREACH 1.5-2x; CODE RED > 2x, or > 1.5x for 2 validated weeks**.

| State | Reading | Governing scenario | What this SOP runs |
|---|---|---|---|
| Floor state | WITHIN or ELEVATED | S-A1 healthy posture; S-A2 product review this cycle on ELEVATED or deteriorating trend across 3+ weeks | P1, P2, P3, P4, P5, P11, P12 |
| Breach band | BREACH (1.5-2x) for 1 validated week | S-A3 push freeze | P13 breach hold. Freeze has tripped, protocol has not. Second consecutive week > 1.5x converts to declaration |
| Code-red state | CODE RED (> 2x any validated week, or > 1.5x for 2 validated weeks) | S-A4 (enter Recovery Mode); Section 11 R1-R6 | P6, P7, P8, P9, P10, P14 |

The breach vs code-red distinction is "the single most consequential reading." A product at 1.7x in one validated week is in S-A3 push freeze, not Recovery Mode; declaring code red there applies the R3 override set (tightened human-confirmation thresholds, discovery budgets floored at sentinel levels, no new Ranking objectives) to a product that has not earned it. 1.6x for a second consecutive validated week is Recovery Mode regardless. Neither is a judgement call.

### 1.2 Why mature carries an emergency protocol
- Strategic Doctrine v1.0 Section 14 names "Blended efficiency far above target on mature products, treated as normal" as an account failure class.
- v4.0 F2: **"The account's current ~20% blended TACOS against mature-stage products is a standing CODE RED and is why Section 11 exists."**
- At maturity spend is frequently re-buying a position the listing already holds. F16 names this **E2** (incrementality and cannibalization estimate); S-A5 fires Taper-and-verify with the burden of proof flipped onto the spend. **Every dollar above the discovered floor is presumed rented until an incrementality read proves otherwise.**

## 2. Scope and boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides mature band, deviation classes, code-red trip, R1-R6, every scenario, lever limit, verdict |
| #25 Transition | Owns post-objective normalization; hands stage entry ("exits into SOP-26"). SOP-26 begins at handoff, never re-runs normalization |
| #28 Placement and modifier | Ladder mechanics, exit-bid discovery, ceiling worksheet, floor register format, bleeding-placement lever order. SOP-26 issues re-ladder and bleed decisions |
| #12 Exact | Campaign-level bid/budget/status/structure; P4 taper, P6 demotion at floor, P7 duplicate consolidation |
| #14 Broad | Defensive brand broad (P4) at defense floors; routes branded IS and incursion terms here. SOP-26 declares defense-set membership |
| #16 PAT and conquest | Defense PAT mechanics, own-ASIN and virtual-bundle self-targeting, counter-conquest evaluation on P11 escalations |
| #17-19 SB, SBV, SD | Every non-SP format build; on SOV rebuild SOP-26 names terms and defense budget. Ledger row 17: defense-set membership and escalation are SOP-26's property |
| #29 Negation | Doctrine, wall levels, wall audit; SOP-26 supplies evidence lines |
| #30 Harvest | Graduation decision; harvest never stops at maturity; no code-red suspends it |
| #35 Incrementality | Test design and continue-or-restore call; SOP-26 executes the rung and records floor |
| #37 Automation rules | Rule register and change control; SOP-26 reads change log, issues suspension notice, never edits a rule |
| #38 Bulk deployment | Staging, upload, T+1 diff. "Emergencies get faster queues, never lower standards" |
| #32 Deal and event window | T8: Recovery Mode > Event Mode > stage defaults; product in Recovery entering event runs at defense-and-proven-terms posture only |
| #33 Sibling arbitration | Family ownership declaration before any restore step on shared defended term |
| Budget envelope and M5 queue | Released dollars post to M5 queue at T0 zone H and Account Rollup tab A2. C3: never cite a #31 procedure (AM-9) |
| Cross-framework read | Pricing, competitive position, product decisions beyond PPC; structural close at P10 hands four maps out of PPC. SOP-26 does not diagnose price or product |
| #24 | Recovery push execution (R3 exception); re-ranking case |
| #6 / V5 | Scoring |

Section 1.4: no numeral is local; gaps go to amendment register (twelve at this version). A threshold without a v4.0 section heading beside it is a defect to raise, not execute.

## 3. Triggers

Lag measured from when artifact carries the signal, not when read.

| Trigger | Signal and detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Stage entry | #25 normalization handoff with floor register and dated ladder state. T2 block K8 discovered-floor values with dates + T6 chain of closing ladder steps | One weekly cycle | P1. Entry without recorded floors refused back to #25 |
| Weekly cadence | Monday cascade reaches T0 on Mature-tagged product. T0 zone B row 3 (TACOS vs stage band) and zone F (TACOS decomposition by objective) | Same cycle | P1, then P2. Deploy Tuesday per #38 after BM huddle |
| Trip watch | Daily product TACOS vs mature band. Account Rollup tab A0 TACOS-vs-band column and code-red flag cell | Same day | P6 on CODE RED per R1; P13 on BREACH. A0 flag and R1 trip are different tests; declare on R1 (AM-1) |
| Second-week confirmation | Product above 1.5x last validated week reads above 1.5x again. T6 entry from prior week's P13 hold vs this week's T0 zone B | Same day | P6 (the limb that fires most often; invisible to v1.0) |
| Quarterly re-ladder | Term cohort reaches re-test date. T4 "Discovered Floor $" and "Next Step Date"; M3 requires floor re-tested quarterly or after logged competitive shock | One weekly cycle | P3 via #28 P5 mechanics |
| Competitive shock | Logged shock on defended term ahead of quarterly date. T5 event type "Competitor entry" + T2 K8 competitor block (top-holder price, rating, reviews, deal and OOS flags) | One weekly cycle | P3 out-of-cycle probe on affected cohort only |
| Incursion flag | Branded IS falls, or competitor brands in brand campaign's served terms. T2 K3 "Brand Impr Share" and "IS% Band" on branded rows; #14 P4 weekly brand-broad read | One weekly cycle | P11 (S-D2 governs restore step) |
| Share-of-voice failure | SOV composite below PRESENT class on product's top-10 terms. E5 composite (F12) on defended set | One weekly cycle | P4 step 5 rebuild under S-F8 |
| Cannibalization flag | E2 fires on branded or rank-3-or-better defended term. T2 K6 economics with E2 estimate; S-D4 | One weekly cycle | P2 step 6 -> incrementality ladder (#35) |
| Monthly harvest read | Harvest-read date. T6 filtered to floor-state spend vs prior-quarter baseline in same log | Two working days | P12, posting to T0 zone H |
| Annual defense read | Defense-cost read date per primary syntax. T1 group S7 "Defense budget $" (M8 declares quarterly; read scores annually) | One weekly cycle | P5. No read on file = F4 |
| Recovery exit | Two consecutive validated weeks within 1.2x band with no gate backlog (R5). T0 zone D gates strip + two dated T0 zone B readings | Same cycle | P10 close, then P14 within one week per R6 |

## 4. Procedures

### 4.0 Preconditions and gates (Section 3)

**3.1 T7 manifest preconditions**
| Field group | Requirement / effect if missing |
|---|---|
| A1 four-period comparability | L30, P30, B30, L60 present. Without it trip test reads single window; P6 declarations legal only on current-week reading with limitation recorded in T6; P3 re-ladder predictions suppressed entirely |
| A2 deployment state | Current bulk state in-row for every defended campaign. Stale suppresses P2 drift restoration for those rows |
| A3 pacing and in-budget | Present on every defensive campaign. L4: defensive utilization target **100%**; under target takes budget lever before any bid reading |
| A6 objective and Expected CPC | Every defended row exactly one declared objective. Untagged row on mature product = S-A8 stage-mismatch finding; routes to assignment before grading |
| B7 placement splits | TOS, ROS, PP present. Missing -> P7 Map 2 "not readable"; cut sequence proceeds on other three maps with gap named. Ledger dependency **D3 OPEN** |
| B8 row economics | T0 spine live at named cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC. Blended/stale margin -> G9 PROVISIONAL on every ceiling-referencing action |
| D6 sibling CPC view | Same-term CPC across siblings from Account Rollup tab A1. Absence suppresses sibling limb of P7 Map 3 |
| D7 decision log and V5 | T6 live with review dates and scores. Without it, two-week limb of trip test unreadable |
| D8 competitor depth | Top-holder price, rating, deal, stockout. Absence suppresses incursion cause classification at P11 step 2; ladder runs on IS signal alone. Ledger dependency **D4 OPEN** |

**3.2 Gates in force** (v4.0 name and number; corpus alias at first use; never mix schemes in one reason string; C9)
| Gate | Observable on a mature product |
|---|---|
| G1 Validation quarantine | T2 "Flag: Zero-Quarantine" Clean on every row entering a cut sequence. Quarantined row -> flag and data-refresh task, never a cut. P8: quarantine or DEGRADED manifest beats every other consideration including urgency |
| G2 Sample sufficiency | T2 "Sample State" = Full on any row receiving a rate-driven cut; below -> EXTEND TEST, leaves cut list |
| G3 Budget truncation | T3 "Truncation Flag (G3)" clear, or budget lever first |
| G6 Inventory adequacy | T2 "Inventory Band" GREEN or YELLOW on defended variation. RED tapers to defense and re-points same day; outranks every mature posture (P1 precedence rule) |
| G7 Envelope and pacing | T0 zone H reconciles: sum of campaign budgets vs declared weekly envelope. Non-reconciling P12 release = accounting error |
| G8 Packet completeness | T7 completeness score on cycle header. **DEGRADED < 85%** of gate-relevant fields -> flags only; code-red declaration on DEGRADED packet carries completeness score in its record |
| G9 Price stability (corpus alias: margin freshness) | No price change on defended variation in trailing **7 days**, else CVR/ACOS PROVISIONAL, no conversion verdict. Reason string states which reading fired |
| G10 Event exclusion (corpus alias: G12 event freeze) | Event weeks and **14 days following** excluded from trend verdicts. Suspends quarterly re-ladder; never suspends a code-red declaration; never outranks Recovery Mode (T8) |
| G11 Sibling conflict | Family ownership declared on shared defended term before a restore step raises a bid |
| G12 MKL hygiene (corpus alias: the event freeze number, G10) | Every defended term in current MKL with syntax tag and relevancy; otherwise "an unexamined habit", routes to MKL maintenance |

**Code-red precondition (not a gate):** the protocol trips on the number and runs. Gates govern which cuts are legal, not whether the declaration stands (G1 removes a row from cut list; G8 caps verdicts to flags; neither delays declaration, freeze or diagnosis). The one condition: the reading is **validated** = week closed, packet present, **sales figure is the SellerBoard read rather than an in-console estimate**. R1 uses "validated" in both limbs.

Time estimates assume packet present and prior experience; first executions run roughly double. P1-P5, P11-P12 = floor-state cadence; P13 = breach hold; P6-P10, P14 = code-red protocol.

### P1. Weekly mature posture read (20 min per product)
1. Read T0 first. v4.0 Section 8 matrix precedence: product (S-A) > syntax (S-Y) > inventory-keyword (S-I) > keyword objective matrices.
2. Score last cycle first: T6 rows with review dates this cycle; V5 HIT / PARTIAL / MISS / WRONG-DIRECTION. Most important on mature: ladder rungs and release postings.
3. T0 zone B row 3: weekly PPC spend vs weekly sales = product TACOS beside stage band ceiling. Compute **ratio to band ceiling** explicitly; write into cycle header.
4. Classify: CODE RED -> P6 same day, stop. BREACH -> P13. ELEVATED -> continue and open S-A2 review (step 5). WITHIN -> continue.
5. ELEVATED only, four S-A2 reads in order, each recorded in T6: (a) **E12 concentration** (T2 sorted by spend; largest single term's share of product ad clicks and spend); (b) **E1 inflation decomposition** on any term whose CPC rose materially; (c) **X10 auto-dominance sweep** (share of priority term's clicks carried by auto and broad); (d) re-verify top-10 spend terms vs declared objectives. New pushes need sign-off above the PPC Lead until WITHIN.
6. T0 zone F objective mix vs stage. O8 mature target: "Mature: defense + conversions dominant, TACOS 4-7%." Discovery-heavy or ranking-heavy mix = S-A8 stage-mismatch -> written objective-mix correction plan with **2-week convergence date**. UNTAGGED trending toward zero is the adoption metric; any dollar in it is unmanaged.
7. T0 zone E flywheel-health row. F2: **mature primary syntax organic share target >= 60-70%**; **RENTING = ad share rising while organic share falls for 3+ weeks**. RENTING fires S-A5 taper-and-verify: every rank-3-or-better and branded term -> incrementality ladder at P2 step 6. RENTING overrides good keyword-level ACOS.
8. T0 zone D gates strip: record failed gates and blocked action classes; carry into every procedure this cycle.
9. Posture line on cycle header: state, ratio to band, mix status, flywheel status, gates failing (reviewed by BM huddle).

### P2. Floor maintenance and drift restoration (25 min per product)
1. T2 OVERSIGHT filter + defended set: rows tagged Defensive, plus Conversions rows carrying a recorded discovered floor in K8. Defended set is a named list declared at P4.
2. Each row: current bid vs recorded discovered floor and date. F9: "the ladder state is the taper protocol's memory: without it every taper restarts from scratch."
3. Bid above floor with no authorising verdict -> **DEFEND AT FLOOR**, restore to floor in one staged step (most common quiet failure).
4. Bid below floor and position slipped -> restore to floor, record slip in T6. Not slipped -> leave; mark candidate for next quarterly probe. Floors recorded only by P3, never by drift.
5. Held and at floor -> **HOLD; DEFEND LIGHTLY AT RANK**, change nothing (logged as a verdict).
6. E2 cannibalization check on every branded and rank-3-or-better row. Fires -> S-D4: one ladder step down, total capture watched **two weeks**, ladder continues while capture holds. Issue **INCREMENTALITY LADDER**, stage single step; #35 owns design and continue-or-restore.
7. Defensive utilization row in T3: S-D3 budget precedes bids; defensive campaign under utilization target takes budget lever first.
8. Stage as bulk rows per #38 with **four-segment reason string**: verdict verbatim, v4.0 scenario ID, this SOP and procedure number, floor register reference. Missing scenario ID does not deploy.
9. Deploy Tuesday after BM huddle; read #38 T+1 diff; redeploy any delta same day.

### P3. Quarterly re-ladder by term cohort (40 min per cohort)
1. Build cohort: defended set grouped by **syntax family** and **quarter in which each floor was recorded** (T4 "Discovered Floor $", "Ladder State (step / date)", "Next Step Date"). Cohorts run separately.
2. Check G10 before probing: armed window or 14-day guard suspends probe for that cohort; next date moves out by guard period.
3. Confirm #28 P2 ceiling worksheet for any cohort whose probe touches a modifier (effective-CPC arithmetic is multiplicative; mandatory).
4. Probe **one rung down** from recorded floor at M3 step size, within L2 per-change limits and above L2 floor (read at execution). Stage whole cohort in one change set (common read window).
5. Log hold prediction per term (position holds at reduced level), review date one read window out.
6. Hold one read window; read at review date.
7. Hold -> record new lower floor in T4 with date and **competitive context note**.
8. Slip -> revert one rung to prior floor, **hold two read windows**, then re-probe once or close cohort at prior floor. A probe that failed does not lower the register.
9. Produce **register diff** (floors lowered, held, raised; dated with context notes) = cohort's artifact; P12 reads it.
10. Whole-cohort slip = competitive-shock reading; run E1 decomposition before re-probing.

### P4. Standing defensive architecture and membership register (30 min, monthly)
1. Declare defended set in writing: **term, surface, objective tag, floor bid, defense budget line, reason** (Ledger row 17: this component's artifact).
2. Brand broad: **one brand-broad campaign per brand at defense floors**, run by #14 P4; SOP-26 confirms membership and floor; #14 returns weekly branded IS and incursion terms.
3. Own-page defense: own-ASIN self-targeting at floor bids, permanently, per #16 (Doctrine Section 8: own-ASIN contextual is cheapest page defense).
4. Shelf presence: brand-format placement on head terms where format split justifies. Grade on **E5 Share of Voice composite** (F12): **DOMINANT > 40%; PRESENT 15-40%; MARGINAL < 15%** of measured top-of-page real estate. Target = presence at minimum defense cost.
5. MARGINAL on top-10 terms -> rebuild under **S-F8**: cheapest surface first at defense budgets, SP CPC escalation last. Name terms and budget line; format and build belong to #17-19.
6. Grade every defensive row against its own band. **O6: Defensive graded on IS held, ACOS 10-15, incrementality (E2)**; judging on another objective's metrics is a process violation.
7. Defensive ACOS above band with IS held -> **S-D5 auction-pressure check** before touching bid: competitor conquesting intensified -> hold and log pressure period; not -> overbidding, ladder resumes at P3.
8. Defense-priority tag -> **S-D6**: protected; evaluated vs defense budget and SOV target, not weekly ACOS. Declared, budgeted, quarterly-reviewed; no quarterly review on file -> loses protection.

### P5. Annual defense-cost read (60 min per primary syntax)
1. Read T1 group S7 "Defense budget $". **M8: per primary syntax, defense budget $ = (syntax organic revenue at risk x displacement probability), bounded by syntax contribution margin; declared quarterly.** Read scores it; does not re-derive.
2. Sum trailing defense spend across **all surfaces**: brand broad, brand exact, own-ASIN PAT, complement PAT, brand-format placements (cross-surface aggregation mandatory).
3. Compute branded revenue protected from syntax's organic and branded sales lines; state displacement assumption explicitly.
4. Divide: defense spend / branded revenue protected (%) beside M8 ceiling and syntax contribution margin.
5. Subtract spend on E2-flagged terms from numerator; state adjusted figure beside raw.
6. No read on file = F4.

### P6. Code-red declaration and same-day freeze (45 min, same day, mandatory)
1. Confirm trip vs **R1: TACOS > 2x stage band any validated week, or > 1.5x for 2 validated weeks, or by executive directive.** Write arithmetic: week's spend, week's sales, TACOS, band ceiling, ratio, which limb fired.
2. Confirm validated (closed week, packet present, SellerBoard sales). DEGRADED -> declare anyway, carry T7 completeness score.
3. Declare in T5 as dated event; set product state to Recovery Mode. R1 requires logging **entry TACOS, target band, projected weekly overspend $**. **Overspend = week's actual spend - (band ceiling x week's sales).** The mode's denominator.
4. Freeze all non-defensive bid increases immediately, product-wide, plus all modifier increases.
5. Apply **R3 overrides** same session and record live: no new Ranking objectives except RECOVERY-class terms at HIGH confidence; discovery budgets floored at sentinel levels (auto on and small); tightened human-confirmation thresholds on bid and budget moves (v4.0 numbers read at execution); step sizes capped at standard even at HIGH confidence.
6. Set **R4 cadence**: daily pacing and gate checks; **twice-weekly mini-audits on the triage set**; weekly full cycle unchanged.
7. Confirm declaration with checkpoint holder before freeze deploys (Matrix row "Code-red declaration + close": PPC Lead decides; launch-stage product: launch operator declares, PPC Lead closes).
8. Notify BM owner (informed) and deals owner where an event window is armed or approaching (T8).

### P7. Four-map diagnosis (3-4 hours)
R2 fixes triage order. Nothing cut until all four maps exist or are recorded unreadable. **R2 governs two windows only: gates sweep same day; top-20 spend terms each get a full Master Action Record this week.** No overall deadline (v1.0 48-hour window retired; AM-12).

- **Map 0, gates sweep (R2 step 1)**: quarantines, truncations, eligibility, MKL hygiene, inventory bands across every campaign, same day. Record each failure with blocked action class; G4 eligibility flip halts execution and opens listing task same day; G1 quarantine removes row from all maps.
- **Map 1, waste map (R2 step 2)**:
  1. Top-20 spend terms in spend order at record grain.
  2. Columns: window clicks, CPC, spend, CVR, orders, contribution recovered (= orders x contribution per order), loss (= spend - contribution recovered).
  3. Each term's own **Max Profitable CPC = contribution per order x that term's own CVR**, observed CPC beside it (per term, never per product).
  4. Rank by **weekly loss dollars descending** (loss dollars outrank ACOS: "a 90% ACOS on eleven dollars is a rounding error and a 41% ACOS on nine hundred is the emergency").
  5. Flag R2 obvious-waste classes for immediate execution: zero-sale spend on irrelevant terms; **GRADUATED-UNSTEERED** leaks (exact live, source never negated); duplicates.
  6. Sum loss $ as share of weekly overspend ("was this a term-level problem").
- **Map 2, placement bleed map**:
  1. T4 per campaign per placement for waste-map campaigns: spend, clicks, orders, CPC, CVR, placement ACOS vs term's governing band.
  2. Each placement's reading as a multiple of campaign's blended reading.
  3. Placement under v4.0 traffic minimum = **UNREAD** (probe yes, premium never, never enters cut list on inferred reading).
  4. B7 MISSING -> map "not readable", gap named in declaration record.
  5. Sum bleed $ as share of overspend.
- **Map 3, duplicate and structure scan (R2 step 4)**:
  1. T2 K8 registry counts: terms live in two or more same-type instances with no declared distinct role. **Four legitimate roles declared at SOP-12 Section 1.2**; anything else consolidates to winner.
  2. **S-R12 add-exact check**: priority term with zero exacts, or auto and broad above X10 share of its clicks = structure failure, repaired before judged.
  3. **X6 sibling divergence check** (where D6 present): same term across siblings at CPC ratio above v4.0 factor -> structural inspection in X6's fixed order; "settings archaeology is the presumption."
  4. Consolidations to #12 P7; add-exact to #12 P1 or P2. Survivor selection human-mandatory.
- **Map 4, automation check**:
  1. #37 rule change log across window; every automated change touching a defended or high-spend row.
  2. Test for ladder runaway (rule stepping a bid one direction repeatedly vs stale target without human confirmation); compare current bid vs recorded floor and count steps.
  3. Runaway -> suspend rule pending #37 review; record suspension notice to #37. Never edit a rule.
  4. Attribute runaway $ (spend above floor on affected rows) as share of overspend.
- **Close**: reconcile four shares vs declaration's overspend; unaccounted portion stated as **residual** and named in close.

### P8. Cut sequence ordered by loss dollars (2-3 hours)
Cuts in **loss-dollar order**, each obeying **L1 lever precedence: budget (if G3 truncated) -> bid -> placement -> negation -> structure (graduation/consolidation) -> status**. Pause last, after documented exhaustion. Never skip forward; emergencies license a faster queue, not lever-skipping.
1. Waste map in loss-$ order; issue v4.0 matrix verdict and execute. Common: **BID DOWN TO PROFITABLE CPC; CAP SYNTAX** as single-step bid edit to row's own Max Profitable CPC (T2 K6). Two terms with opposite four-period trends never receive the same execution; trend context in reason string.
2. Levers exhausted and **L7** conditions met -> **PAUSE (LEVERS EXHAUSTED)** entered as PAUSED-PENDING with reason and named re-entry; missing either returns to pass.
3. Bleeding placements per **#28 P6 lever order**: modifier first, then base bid reduced vs bleeding placement's own CPC, then placement split at persistent divergence. Never flat bid cut across campaign.
4. Negation sweep: zero-sale and off-taxonomy terms to #29 with evidence lines at #29's wall level.
5. Structure repairs: consolidations to #12 P7; add-exact to #12 P1/P2 with steering walls same session per #29.
6. Confirm each suspended automation rule with #37.
7. Stage every cut through #38 with **code-red reference in reason string**.
8. Log each cut's expected weekly savings in T6 at staging (R4 scoreboard = running total vs entry overspend).
9. Apply tightened R3 confirmation thresholds to every cut.

### P9. First re-read at close of validated week 1 (45 min)
1. Week's TACOS and ratio (as P1 step 3) beside entry reading.
2. Read direction, not level. **X8: trajectory beats snapshot**; improving reading continues current treatment even at ugly absolute level.
3. Not at band with clear inflection = acceptable, continue without deepening. Not turning -> deepen: extend waste map from top-20 to **next spend decile**, re-run P8 on extension.
4. R4 scoreboard: expected weekly savings vs realized change in weekly spend. Large gap with cuts deployed and verified -> diagnosis missed a driver; four maps re-open.
5. Confirm freeze and R3 overrides still live.

### P10. The close, or the structural escalation (60 min)
Day 7 = close of validated week 1 after declaration; day 14 = week 2; day 21 = week 3.
1. Classify day-14 reading. **R5 exit: TACOS within 1.2x stage band for 2 consecutive validated weeks, with no gate backlog; logged with recovered weekly dollars.** A single in-band week is the first of two.
2. Day 14 within 1.2x -> week one of exit test; hold freeze and R3; re-read day 21. Day 21 also within 1.2x and gate backlog clear -> exit legal.
3. Day 14 approaching but above 1.2x -> continue on R4 cadence; exit clock not started ("Approaching is not within").
4. Still elevated with no credible trajectory -> escalate **STRUCTURAL**: pricing, competition or product "wearing a PPC costume"; four maps route out of PPC. **D6**: Price Position Index precedes any listing spend. SOP stops at routing.
5. Legal exit: log recovered weekly dollars (entry vs exit weekly spend at comparable sales, $ and %). Clear R3 overrides in one recorded action.
6. Artifact chain complete before close accepted: declaration with ratio arithmetic, four maps, cut records with staged sets and T+1 diffs, both re-reads, exit reading pair.
7. Return to floor state, re-enter P1. Floors discovered during cut sequence recorded in T4 with context note "discovered under Recovery conditions."

### P11. Incursion detection and response ladder (30 min)
1. Detect weekly from two artifacts: T2 K3 branded IS and band on branded rows; competitor brands/ASINs in brand campaign's served terms (#14 P4 read).
2. Classify cause using D8 where present: competitor entry, deal window, price move, review surge. D8 MISSING -> respond on IS signal, record gap.
3. Respond inside defense ceiling. **S-D2: "Restore one ladder step; open/expand PAT self-targeting to occupy our own pages; the syntax defense budget (M8) is the ceiling."** One step, not matched escalation.
4. Hold the ceiling absolutely; above it the fight moves to conversion assets, not bids.
5. Persistent incursor -> escalate to **#16 P10** for counter-conquest evaluation with flag profile inputs. Unflagged, answer stays defensive ("conquest against a stronger competitor is a donation").
6. Receive #16 evaluation record; file with incursion record; escalation not closed until it returns.
7. Incursion coinciding with competitor deal window -> **S-C5** through #16: stand down on that target for the window, resume at window end.

### P12. Monthly profit-harvest read (50 min per product)
"A spend reduction is not a release until the position it was buying is proven to have held."
1. Current floor-state spend on defended set across all surfaces for the month (T6 floor-state rows reconciled vs T3 campaign spend).
2. Prior-quarter baseline for same set from same log; if membership changed, compare on intersection and state difference.
3. Raw difference = candidate, not release.
4. Verify on two axes: **rank** (mean and per-term position vs prior period) and **share** (E5 SOV composite vs prior class). Release real only where both held flat or better.
5. Rank held but share fell a class -> release attributable to those terms **withheld**, routed to S-F8 rebuild at P4 step 5 (not deferred; "a saving that was not real").
6. Both held -> post verified difference to M5 queue at T0 zone H and Account Rollup tab A2 (C3).
7. Write posting into T6 with verification evidence: both axes, periods compared, withheld portion and reason.
8. Floor-state spend rising vs baseline with position unchanged = drift the weekly pass missed -> back to P2 step 3, count recorded as F2 detection.

### P13. Breach-band hold (35 min)
1. Confirm: ratio **1.5x-2x**, one validated week, **no prior week above 1.5x** (else -> P6).
2. Freeze new Ranking objectives on the product.
3. Test every live push on two conditions: **rank velocity above zero** and **spend inside recorded loss ceiling**. Failing either -> its own stop-loss.
4. Cap CPCs above the 1.5x-ceiling line to the PUSH-ONLY boundary pending review. **F1: <= 0.8x ceiling SAFE; 0.8-1.0x AT-CEILING; 1.0-1.5x PUSH-ONLY; > 1.5x UNJUSTIFIABLE outside a sized push.** Cap = 1.5 x row's own ceiling (from own CVR), within L2 per-change limit.
5. **E6 opportunity-cost reallocation**: EV of best unfunded push vs EV of worst-performing funded spend of equal size. Positive = standing order to move budget.
6. Record hold in T6 with week's ratio and dated re-read at next validated week (what the second-week trigger reads).
7. Next validated week >= 1.5x -> declare per P6 same day; below -> hold lifts, return to ELEVATED/WITHIN path at P1.

### P14. Post-exit review (90 min, within one week of exit)
1. Answer **R6** in writing: which rules, had they been enforced, would have prevented entry (enforcement, not content).
2. Reconcile four maps' shares vs entry overspend; state residual and whether explained.
3. Score cut records: expected vs realized weekly savings per cut.
4. File as **V3 amendment proposals** through threshold-change path (Matrix: v4.0 threshold changes CEO decides, PPC Lead executes and reviews). Proposal with evidence, never an edit.
5. Rule fired correctly and overridden -> log override reason (falling override rate = system quality metric).
6. Entry traced to a detection failure -> raise against this SOP's Element 2 trigger table at next increment.

## 5. Rules, thresholds and numbers

### 5.1 Numeric values
| Item | Value | Source |
|---|---|---|
| Mature TACOS band | 4-7% (ceiling 7.0%) | F2 |
| Deviation classes | WITHIN <= 1.2x; ELEVATED 1.2-1.5x; BREACH 1.5-2x; CODE RED > 2x or > 1.5x for 2 validated weeks | F2, S-A4, R1 |
| Code-red trip | TACOS > 2x band any validated week; > 1.5x for 2 validated weeks; or executive directive | R1 |
| Instrument divergence | KDR "Code-red at >1.5x band"; Data Architecture s11 tab A0 "Code-red flag (T6: TACOS > 1.5x band or spend untraceable to objectives)"; Doctrine s14 "trip at 1.5x band" | AM-1 |
| Recovery exit | within 1.2x band, 2 consecutive validated weeks, no gate backlog | R5 |
| Post-exit review | within one week of exit | R6 |
| R4 cadence | daily pacing and gate checks; twice-weekly mini-audits on triage set; weekly full cycle | R4 |
| R2 windows | gates sweep same day; top-20 spend terms full Master Action Record this week | R2 |
| S-A2 trigger | ELEVATED or deteriorating trend across 3+ weeks | S-A2 |
| S-A8 correction | written objective-mix plan with 2-week convergence date | S-A8 |
| Organic share target (mature primary syntax) | >= 60-70% | F2 |
| RENTING | ad share rising while organic share falls for 3+ weeks | F2 |
| Defensive band | IS held, ACOS 10-15, incrementality (E2) | O6 |
| Defensive utilization target | 100% | L4 |
| SOV bands | DOMINANT > 40%; PRESENT 15-40%; MARGINAL < 15% of top-of-page real estate | F12 / E5 |
| CPC/ceiling bands | <= 0.8x SAFE; 0.8-1.0x AT-CEILING; 1.0-1.5x PUSH-ONLY; > 1.5x UNJUSTIFIABLE outside sized push | F1 |
| Breach CPC cap | 1.5 x row's own Max Profitable CPC | P13 / F1 |
| Max Profitable CPC | contribution per order x term's own CVR | P7 |
| Overspend | actual spend - (band ceiling x week's sales) | R1 / P6 |
| Incrementality ladder | one step down; total capture watched two weeks | S-D4, X12 |
| Re-ladder | one rung down from floor at M3 step; hold one read window; on slip revert, hold two windows, re-probe once or close | P3, #28 P5 |
| M3 step | ~10% (WE-3: 2.24 x 0.90) | M3 |
| L2 per-change limit | 50% of current value; bid floor value (WE-1 cuts stay above "the L2 floor value") | L2 |
| Floor re-test | quarterly, or after logged competitive shock | M3, V4 |
| M8 defense budget | per primary syntax: (organic revenue at risk x displacement probability), bounded by syntax contribution margin; declared quarterly | M8 |
| Price stability | no price change in trailing 7 days | G9 |
| Event exclusion | event weeks + 14 days | G10 |
| DEGRADED packet | < 85% gate-relevant fields | G8 |
| P9 deepening | extend waste map from top-20 to next spend decile | P9 |
| Harvest read lag | two working days | Trigger table |
| Defense-cost read | annual | P5 |
| Defended-set declaration review | monthly | P4 |
| Calendar | Monday cascade; Tuesday deploy after BM huddle; Wednesday T+1; packet lands Monday 06:00, workbooks by 09:00 | I-2, cadence |
| Time estimates | P1 20 min; P2 25; P3 40/cohort; P4 30 monthly; P5 60/syntax; P6 45 same day; P7 3-4 h; P8 2-3 h; P9 45; P10 60; P11 30; P12 50; P13 35; P14 90 | SOP |

### 5.2 Criteria System v4.0 rule IDs referenced
| ID | Meaning as described |
|---|---|
| F1 | CPC-to-ceiling bands |
| F2 | Product State & Strategy: stage bands, deviation classes, organic-share target, RENTING, ~20% TACOS standing CODE RED |
| F9 | Ladder state is the taper protocol's memory |
| F12 | E5 Share of Voice composite bands |
| F16 | E2 incrementality and cannibalization estimate |
| E1 | Inflation decomposition (market vs self-inflicted) |
| E2 | Incrementality / cannibalization estimate |
| E5 | Share of Voice composite |
| E6 | Opportunity-cost reallocation |
| E12 | Concentration read |
| X6 | Sibling divergence check; settings archaeology presumption; fixed inspection order |
| X8 | Trajectory beats snapshot |
| X9 | Product log consulted before bids blamed |
| X10 | Auto/broad share threshold on priority term |
| X12 | Incrementality ladder |
| G1-G12 | Gates (Section 4.0) |
| O6 | Defensive grading: IS held, ACOS 10-15, E2; cross-objective grading is a process violation |
| O8 | Mature mix: defense + conversions dominant, TACOS 4-7% |
| D6 | Price Position Index precedes any listing spend |
| D10 | RECOVERY class (R3 exception) |
| S-A1 | Healthy posture |
| S-A2 | Product review on ELEVATED or 3+ week deteriorating trend (E12, E1, X10, top-10 objective re-verify) |
| S-A3 | Push freeze at BREACH |
| S-A4 | Enter Recovery Mode |
| S-A5 | Taper-and-verify (burden of proof on spend) |
| S-A8 | Stage-mismatch finding |
| S-A1 to S-A10 | Section 8.1 companions |
| S-D1 to S-D6 | Section 8.6 defense scenarios: S-D2 incursion restore step; S-D3 budget before bids on defensive; S-D4 cannibalization incrementality test; S-D5 auction-pressure check; S-D6 defense-priority tag |
| S-F8 | SOV rebuild: cheapest surface first, SP CPC escalation last (Section 8.10) |
| S-C5 | Stand down on competitor deal window |
| S-R12 | Add-exact check |
| L1 | Lever precedence: budget (if truncated) -> bid -> placement -> negation -> structure -> status |
| L2 | Per-change limit and bid floor |
| L4 | Defensive utilization target 100% |
| L7 | Pause conditions (levers exhausted) |
| L1-L7 | Section 9 companions |
| M3 | Taper step; quarterly floor re-test or after competitive shock |
| M8 | Defense budget formula |
| T8 | Recovery > Event > stage defaults |
| R1 | Trip conditions; entry log contents |
| R2 | Triage order (gates sweep, waste map, ..., structure scan as step 4) |
| R3 | Recovery overrides |
| R4 | Recovery cadence and scoreboard |
| R5 | Exit test |
| R6 | Post-exit review question |
| P1 | Precedence: inventory RED outranks mature posture |
| P8 | Data quality beats urgency |
| P1 to P8 | Section 12 companions |
| V3 | Amendment proposals |
| V5 | Scoring |
| V7 | Post-mortem filing obligation |
| C3, C9, C10 | Ledger conflicts |

## 6. Data inputs required

### 6.1 Command Workbook tabs
- **T0 zone A**: posture line echo, verdict banner.
- **T0 zone B** (row 3): weekly PPC spend, weekly sales (SellerBoard read), TACOS vs stage band ceiling.
- **T0 zone C** economics spine named cells: AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope.
- **T0 zone D**: gates strip.
- **T0 zone E**: product state vector (flywheel health, stage integrity).
- **T0 zone F**: TACOS decomposition by objective (incl. UNTAGGED).
- **T0 zone H**: envelope and M5 queue.
- **T1**: group S3 cap status; group S7 "Defense budget $".
- **T2** (OVERSIGHT filter + defended set):
  - K1 oversight flag, coverage state;
  - K2 validation state, sample state, in-budget %, inventory band, event mode;
  - K3 "Brand Impr Share", "IS% Band";
  - K5 four-period trend (L30, P30, B30, L60), WoW block, "Flag: Zero-Quarantine";
  - K6 margin per unit, BE ACOS, max profitable CPC, expected CPC, CPA ceiling, E2 estimate;
  - K8 registry counts, duplicate flag, current bid, TOS modifier, sibling CPC view, competitor block (top-holder price, rating, reviews, deal and OOS flags), discovered-floor values with dates.
- **T3**: utilization, in-budget bucket, "Truncation Flag (G3)", objective tag, campaign verdict, campaign spend.
- **T4**: per campaign per placement spend, clicks, orders, CPC, CVR; "Discovered Floor $", "Ladder State (step / date)", "Next Step Date", placement verdict.
- **T5 PRODUCT LOG**: event types incl. "Competitor entry", deal windows; code-red declaration event; Recovery Mode state.
- **T6 DECISION LOG**: V5 scores, breach-hold entries, floor-state spend rows, prior-quarter baseline, cut records, ladder chains.
- **T7 MANIFEST**: A1, A2, A3, A6, B7, B8, D6, D7, D8 statuses; completeness score.
- **Account Rollup Workbook**: tab **A0** (code-red flag cell, TACOS vs band column), tab **A1** (sibling same-term CPC, D6), tab **A2** (cross-product M5 queue).

### 6.2 Feeds, reports and external records
- **SellerBoard** weekly sales read (validated week requirement); weekly packet landed Monday 06:00, workbooks refreshed by 09:00 (Data Operations).
- Bulk file / current deployment state (A2) for every defended campaign.
- Placement splits TOS / ROS / PP (B7).
- #41 margin table refresh (monthly and on event).
- #37 rule change log (diagnosis window).
- #14 P4 weekly brand-broad read (branded IS, incursion terms, competitor brands/ASINs in served terms).
- #28 ladder step derivation, exit-bid discovery, ceiling worksheet (#28 P2), bleed lever order (#28 P6).
- #32 armed-window declaration and event plan.
- #33 family ownership declarations.
- #35 continue-or-restore call.
- #38 T+1 verification diff.
- #16 counter-conquest evaluation record.
- Competitor depth (D8): top-holder price, rating, deal, stockout.
- Syntax organic and branded sales lines (for P5 branded revenue protected).
- Current MKL (syntax tag, relevancy).
- KDR Template v3.0 "Bands & Verdicts Reference" and "Campaign Decision Record" tabs.

## 7. Outputs / artifacts

| Event | Record | Storage | Retention | Consumer |
|---|---|---|---|---|
| P1 | Posture line: state, ratio to band, mix status, flywheel status, gates failing | Cycle header, echoed to T0 zone A | Append-only log life | BM huddle; every keyword verdict this cycle; Account Rollup A0 |
| P2 | Staged restoration set with floor references + T6 rows with prediction and review date | T6; #38 staged set | Append-only | #38 T+1; V5 next cycle |
| P3 | Register diff: floors lowered, held, raised, each dated with competitive context note | T4 "Discovered Floor $", "Ladder State (step / date)", "Next Step Date" | Life of the term in register | P12; #28; #35 |
| P4 | Defended-set membership register: term, surface, objective tag, floor bid, defense budget line, reason | T1 S7 for budget line; membership with product's defended set | Life of set, versioned per declaration | #14 P4, #16, #17-19 |
| P5 | Defense spend vs branded revenue protected, displacement assumption, cannibalization-adjusted figure | T6 against syntax; M8 in T1 S7 | Annual, superseded | Quarterly M8 declaration; BM owner review |
| P6 | Declaration record: ratio arithmetic, limb fired, entry TACOS, target band, projected weekly overspend, packet completeness, R3 override list | T5 dated event; product state Recovery | Life of product log | #37, #32, Account Rollup A0, checkpoint holder |
| P7 | Four maps + gates sweep with shares of overspend and reconciliation with residual | Attached to declaration in T5; source reads in T2, T3, T4 | Life of artifact chain | #28, #12, #29, #37, cross-framework read |
| P8 | Cut records: staged sets with code-red reference, expected weekly savings, T+1 diffs | T6; #38 format | Append-only | #38; R4 scoreboard; V5; P14 |
| P9, P10 | Day-7 and day-14 readings with ratios, scoreboard line, exit pair with recovered weekly $ | T5 vs declaration; T6 scoreboard | Life of chain | P14; A0; amendment path |
| P11 | Incursion record: detection artifact, cause classification or gap, ladder step, ceiling reference, returned counter-conquest evaluation | T6, cross-filed to defended-set register | Append-only | #16 P10; #14 P4 |
| P12 | Release posting with verification evidence (both axes, both periods, withheld portion and reason) | T0 zone H; Account Rollup A2; evidence in T6 | Append-only | M5 queue; #35; family-level M5 quarterly |
| P13 | Hold record: week ratio, pushes tested and outcomes, capped rows, E6 reallocation, dated re-read | T6 | Append-only | Second-week confirmation trigger |
| P14 | R6 review: prevention answer, map reconciliation, cut scoring, override reasons, amendment proposals | Filed with declaration in T5; proposals to threshold-change path | Life of chain | v4.1 amendment brief; V7; this SOP's Element 2 |

No v4.0 retention period (AM-8). **Reason-string format**: four segments: verdict verbatim, v4.0 scenario ID, SOP and procedure number, floor register reference (plus code-red reference inside protocol). Alarm evidence line: row or product, signal value, v4.0 rule/gate reference, artifact where read.

**Campaign-level verdicts** (KDR "Campaign Decision Record"): FUND / HOLD / TRIM BUDGET; RAISE / CUT MULTIPLIER; NEGATION PASS; CONSOLIDATE; RETAG OBJECTIVE; PAUSE (L7); ARCHIVE. On mature: TRIM BUDGET follows the bid down; RAISE MULTIPLIER barred inside a code red; RETAG OBJECTIVE catches push-era campaign tagged Ranking (F5).

**Retired v1.0 strings**: RE-LADDER (QUARTERLY); CODE-RED: FREEZE / CUT / DEEPEN / CLOSE / STRUCTURAL; INCURSION RESPONSE; RELEASE TO QUEUE. Only DEFEND AT FLOOR carried forward unchanged.

### Verdict mapping (25 KDR strings)
| Verdict | Mature-stage execution |
|---|---|
| QUARANTINE: DATA REFRESH | Row leaves every map and cut list, including inside code red (P8 rule); refresh task with owner and date |
| UNLOCK TRAFFIC | Rare, always a finding (mis-scoped defense or quiet position loss); barred inside code red by P6 freeze |
| FIX BUDGET (TRUNCATED) | Budget lever only at #12 P11 step 3; S-D3 case on defensive campaigns |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Budget assurance only; inside code red runs at R3 sentinel level |
| FUND TEST (UNFUNDED PRIMARY) | Not issued here; barred in BREACH/Recovery; otherwise M5 queue decision |
| RANK PUSH: FUND SIZED PUSH | Not this SOP's; stage question or #24 re-ranking; barred by S-A3 in BREACH and by R3 in Recovery (except RECOVERY class at HIGH) |
| RECOVERY PUSH | Only push class R3 permits in Recovery, only D10 RECOVERY-class at HIGH confidence; execution #24, standup #12 |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Not mature; rank case live; stage tag reviewed at monthly renewal |
| FIX CONVERSION FIRST; DEFER PUSH | Cap at maintenance and hold; fix to funnel-drop-point owner; often chronic syntax-level conversion failure (bids frozen at maintenance across syntax) |
| PLACEMENT FIX FIRST | Bids hold; #28 executes; inside code red = second cut lever at P8 step 3 |
| RE-POINT VARIATION | #12 P10 same day on G6 RED; inventory outranks mature posture |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | Arrives from #25; mid-stage mechanics #28 P5, execution #12 P4; SOP records floor |
| HOLD; DEFEND LIGHTLY AT RANK | Standing state of mature stage |
| DEFEND AT FLOOR | No change at floor; drift restored in one staged step (P2 step 3) |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Workhorse cut verdict; single step to row's own Max Profitable CPC (T2 K6) within L2; syntax cap at T1 via instrument layer |
| INCREMENTALITY LADDER | P2 step 6 on E2-flagged branded or rank-3-or-better term; #35 owns read |
| ADD EXACT + RESTRUCTURE (13.1 identical) | From P7 Map 3; #12 P1/P2 with walls per #29 |
| CONSOLIDATE DUPLICATES | #12 P7; survivor selection human-mandatory, not delegated inside code red |
| GRADUATE FROM DISCOVERY (13.1: GRADUATE + STEER) | #30; code red freezes bid increases, not graduation pipeline; mid-protocol graduate stood up and walled same day |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) (13.1: CUT / NEGATE) | #29; SOP supplies evidence lines; P8 step 4 |
| ENTER SBV ARBITRAGE | Via SOV route (MARGINAL -> S-F8); format build #17-19; paired SP step-down #12 |
| OPEN / ROTATE / EXIT CONQUEST | #16; SOP escalates at P11 step 5 |
| STOP-LOSS: CONCEDE OR DEFER | Any push live at BREACH/Recovery entry failing velocity or loss-ceiling test (P13 step 3); freed budget to envelope via M5 |
| PAUSED-PENDING (REASON + RE-ENTRY) | #12 P8 with reason and re-entry; inside code red last lever |
| LEAVE TO HARVEST | No exact stood up; live exact evaluated for demotion; discovery economics under #30 |

## 8. Decision rights

PPC Authority Matrix v2.0 Section 1:
| Row | Rights |
|---|---|
| Code-red declaration + close | PPC Lead decides; operator executes; PPC Manager executes; BM owner informed. Launch-stage product: launch operator declares, PPC Lead closes |
| Automation rules (#37) | PPC Lead decides; operator executes and reviews (every pause and rule suspension human-mandatory) |
| Structure creation (all SOPs) | Every structural change and survivor selection human-mandatory |
| Bulk deployments (#38) | PPC Lead reviews; operator and PPC Manager execute |
| Push funding (the M5 queue) | CEO decides above envelope; PPC Lead within; release posting human-mandatory |
| Incrementality tests | PPC Lead reviews; operator decides and executes |
| PAT/conquest opens and exits | PPC Lead reviews; operator decides and executes |
| Sibling declarations (S-series) | PPC Lead decides; BM owner reviews |
| Weekly verdicts (established US) | PPC Lead decides; operator executes assigned scope; BM owner reviews in daily huddle (review not veto; disagreements route up) |
| v4.0 threshold changes | CEO decides; PPC Lead executes and reviews |

- **AI-executable with audit**: posture read and classification, four maps, reconciliation, cut drafting in loss-$ order with L2 step decomposition, re-ladder rung drafting, drift detection, release computation and verification arithmetic, breach-hold record, defense-cost arithmetic, P14 reconciliation.
- **Human-mandatory**: declaration confirm and close; every pause and rule suspension; every structural change and survivor selection; STRUCTURAL escalation; every deployment confirm; release posting; incrementality hand-off; counter-conquest escalation; shared-term restore step. No Recovery-Mode discount.
- New pushes on an ELEVATED product require sign-off above the PPC Lead until WITHIN.
- Vacancy rule: D -> PPC Lead; E -> PPC Manager. R3 tightened thresholds read while mode live.
- Escalation: F1 on discovery with days-silent quantified; F6 and F7 on discovery; STRUCTURAL close by definition with four maps and residual; any mode twice in consecutive cycles on same scope -> PPC Lead with T6 history.
- Alarm routing: same day to operator queue F1, F6, F7, F8, F11; weekly worklist F2, F3, F9, F10; PPC Lead with T6 history F4, F5, F12 and recurring modes.

### Cadence
Daily: trip watch on every mature-tagged product vs A0 and T0 zone B; pacing and gate checks. Weekly: P1 and P2 in Monday cascade; deploy Tuesday; T+1 Wednesday; incursion scan; F9 expired-rung scan. Monthly: P12; P4 declaration review. Quarterly: P3 per cohort; M8 re-declaration. Annually: P5. Recovery Mode: R4 overlay.

### Operator ramp
Week 1: reproduce posture read on three mature products; trace floor register end to end on one term (premium over own Max Profitable CPC per click and per week); read a closed code-red chain; locate every Element 8 artifact; observe Monday cascade and BM huddle. Week 2: supervised P1-P2, historical four-map diagnosis, L2-compliant cut sequence, one re-ladder cohort, harvest read with split, one #16 escalation and one #35 hand-off. Week 4: unsupervised with audit; misclassified posture read returns operator to week-2 supervision on that procedure only. Ten live-defense questions (Section 11.4).

### Failure modes
| ID | Failure | Detection |
|---|---|---|
| F1 | Trip normalized | Validated week meeting either R1 limb with no T5 declaration, or T6 breach-hold with no dated re-read |
| F2 | Floor rot | Cohort past quarterly re-test date in T4 "Next Step Date", or P12 finds floor-state spend rising with position unchanged |
| F3 | Brand bidding war above ceiling | Defense bid above M8 line on incursion response, or two consecutive restore steps on one term |
| F4 | Defense theatre | Defended set with no defense-cost read, or read on one surface |
| F5 | Push-era structure surviving into mature | Undemoted push campaigns with floors recorded, or Ranking-tagged campaign in mature mix (T0 zone F) |
| F6 | Trip tested on wrong number | Declaration citing campaign ACOS, blended conquest ACOS or ad-attributed ACOS instead of product TACOS vs stage band |
| F7 | Single-week close | Code red closed on one in-band reading |
| F8 | Recovery discipline suspended for event | Event-plan actions outside defense-and-proven-terms posture in Recovery, or R3 cleared before R5 exit |
| F9 | Undated or oversized rungs | T4 step with no date/prediction, or staged step exceeding L2 |
| F10 | Release posted without verification | T0 zone H posting with no rank and share evidence in T6, or changed membership without intersection statement |
| F11 | Runaway automation found late | Defended row more than one rung above floor with no human confirmation in T6, or #37 log entry with no matching T6 line |
| F12 | Post-mortem never filed | Recovery exit with no P14 within one week, or review with no amendment proposals |

## 9. Account-specific facts

- v4.0 F2: **the account's current ~20% blended TACOS against mature-stage products is a standing CODE RED** (why Section 11 exists).
- Strategic Doctrine v1.0 Section 14 failure class: "Blended efficiency far above target on mature products, treated as normal."
- v1.0 recorded as account patterns: absence of a formal code-red protocol (normalized trip, F1); defense theatre (F4) as a standing pattern; push-era structure surviving into mature (F5); floor rot; brand bidding war above ceiling.
- **The v1.0 code-red incident** (recomputed in WE-1): five waste terms; product-page bleed at **2.3x blended**; one undeclared duplicate pair; one automation rule that stepped a defensive term **six rungs** against a stale target (premium carried **11.3%** of week's overspend). v1.0 recorded 61% term waste, 22% placement bleed, "remainder the runaway rule".
- Account Rollup tab A0 flags code red at TACOS > 1.5x band (diverges from R1; AM-1).
- Ledger dependencies **D3 (placement feed B7) OPEN** and **D4 (competitor depth D8) OPEN**.

### Worked examples (training base: AOV $80.00; contribution $28.00/order; break-even ACOS 35.0%; Target 17.5%; Max Acceptable 26.3%; CVR 5.2% unless stated)
- **WE-1 code red from declaration to legal exit**: band 4-7%, ceiling 7.0%. Week 1: $4,494.00 / $42,000.00 = 10.7%, 1.53x (BREACH, held at P13). Week 2: $4,578.00 / $42,400.00 = 10.8%, 1.54x -> R1 second limb. Overspend = 4,578.00 - (0.07 x 42,400.00 = 2,968.00) = **$1,610.00/wk ($230.00/day)**. Waste map: W1 210 clicks, $2.40, $504.00, 4.0%, 8.40 orders, $235.20 contribution, loss $268.80, ceiling $1.12; W2 160, $2.10, $336.00, 4.5%, 7.20, $201.60, $134.40, $1.26; W3 130, $2.80, $364.00, 3.5%, 4.55, $127.40, $236.60, $0.98; W4 95, $3.10, $294.50, 3.0%, 2.85, $79.80, $214.70, $0.84; W5 88, $2.25, $198.00, 2.5%, 2.20, $61.60, $136.40, $0.70; total 683 clicks, $1,696.50, 25.20 orders, $705.60, loss **$990.90 = 61.5%** of overspend. L2 decomposition: W1 $2.40->$1.20 (50.0%) ->$1.12 (6.7%), $252.00 + $16.80; W2 $2.10->$1.26 (40.0%) one step, $134.40; W3 $2.80->$1.40 (50.0%)->$0.98 (30.0%), $182.00 + $54.60; W4 $3.10->$1.55 (50.0%)->$0.84 (45.8%), $147.25 + $67.45; W5 $2.25->$1.13 (49.8%)->$0.70 (38.1%), $98.56 + $37.84; week 1 $814.21 + week 2 $176.69 = $990.90; **82.2%** lands week 1. Map 2: blended ACOS 4,578.00 / 13,080.00 ad sales = 35.0%; product pages on two campaigns at 2.3x = 80.5% ACOS on $620.00 spend; PP sales $770.19; contribution $269.57; loss **$350.43 = 21.8%**. Map 3: one undeclared duplicate pair. Map 4: floor $0.62 x 1.10^6 = $1.0984 -> $1.10; premium $0.48/click x 380 clicks/wk = **$182.40 = 11.3%**. Reconciliation $1,523.73 vs $1,610.00; **residual $86.27 = 5.4%**. Day 7 (week 3): $3,780.00 / $42,470.00 = 8.9%, 1.27x ELEVATED, inflected; expected savings $1,347.04 vs realized $798.00 (59.2%). Day 14 (week 4): $2,900.00 / $42,650.00 = 6.8%, 0.97x WITHIN; reduction $1,678.00 = 124.6% of expectation (V5 HIT); not a close (v1.0 closed here). Day 21 (week 5): $2,760.00 / $42,900.00 = 6.4%, 0.92x; legal exit; reduction **$1,818.00/wk (39.7%)** on sales 1.2% higher; **$94,536.00 annualized**; ceiling spend $3,003.00, exits $243.00 under.
- **WE-2 breach not code red**: week before WE-1, 1.53x one week; A0 cell lights but R1 does not fire; declare on R1, read A0 as prompt for P13. Two pushes: one velocity 0.6 pos/wk inside loss ceiling continues; one velocity 0.0 -> STOP-LOSS. Cap: Max Profitable CPC $1.46; 1.5x line $2.19; row at $2.64 (UNJUSTIFIABLE) capped to $2.19 (17.0% cut); 120 clicks: $316.80 -> $262.80, saving $54.00/wk. E6: 6.24 orders = $174.72 vs $262.80 spend, deficit $88.08; reallocation is standing order. Next week 1.54x -> WE-1.
- **WE-3 re-ladder slip, revert, confound**: floor $2.24; ceiling $1.46; premium $0.78/click; 30 clicks/wk = $23.40/wk ($3.34/day). Protects ~3.1 organic orders/day = $86.80/day; ratio 26.0:1. Probe $2.02 (9.8%), prediction rank 4 or better; reads 6 -> revert to $2.24, hold two windows, register unchanged. T5 shows two competitor deal windows (X9) -> probe uninformative; E2-flagged term's incrementality read voided, handed to #35. Re-probe at $2.02 holds; new floor $2.02; premium $0.56 = $16.80/wk ($2.40/day); ratio 36.2:1; saving $6.60/wk = **$343.20/yr**.
- **WE-4 harvest release not real**: 11 terms; baseline $3,120.00/month; current $2,704.00; raw $416.00. Rank mean 3.2 -> 3.1 (held). SOV top-10 22% -> 13% (PRESENT -> MARGINAL). Three terms carry share loss = $174.00 withheld (41.8%); verified release **$242.00/month**. Weekly: $96.00 vs $55.85; difference $40.15/wk = 71.9% over-subscription. Posted $242.00 to T0 zone H and A2.

## 10. Open items

### 10.1 Amendment register (twelve items for v4.1)
| ID | Item |
|---|---|
| AM-1 | Code-red trip stated at two tests: v4.0 F2 / S-A4 / R1 two-part test vs KDR "Code-red at >1.5x band", Data Architecture v1.0 s11 tab A0 "Code-red flag (T6: TACOS > 1.5x band or spend untraceable to objectives)", Doctrine v1.0 s14 "trip at 1.5x band forces the protocol". Highest priority |
| AM-2 | Stage bands diverge v4.0 F2 vs KDR Bands sheet: Ranking push 10-18% vs 12-15%; Transition 7-12% vs 8-12%; Harvest <= 3% vs <= 4%. Mature 4-7% agrees |
| AM-3 | KDR Bands sheet and five calibration rows cite superseded Decision Framework rule IDs: TACOS bands to M7 and T6, concentration limits to M10, recovery zone to S-R12, objective-less spend to G10 (under v4.0: marginal mathematics, harvest-to-exact pipeline, confidence-weighted sizing, add-exact scenario, event exclusion). Distinct from C9 and C10 |
| AM-4 | No numeral for incursion detection bar (S-D2 "Branded IS slipping" with no magnitude or window) |
| AM-5 | No numeral for day-7 inflection test |
| AM-6 | No tolerance for "held flat or better" in harvest verification (rank and share) |
| AM-7 | No pass/fail ratio for annual defense-cost read |
| AM-8 | Record retention (duplicate; fold once) |
| AM-9 | Dangling #31 citation (C3) closed at source |
| AM-10 | No residual tolerance at diagnosis close |
| AM-11 | Gate numbering (C9; duplicate) |
| AM-12 | No window for code-red diagnosis completion or #37 log delivery; v1.0 48-hour window retired |

(Register says twelve items; IDs AM-1 to AM-12, with AM-12 listed before AM-11 in the source.)

### 10.2 Ledger conflicts referenced
C3 (#31 no procedural document; five dangling citations, one closed here), C9 (gate numbering), C10 (verdict counts; two divergent rows cross-mapped).

### 10.3 Version governance triggers
Any v4.0 increment (re-validate F2 mature band, deviation classes and both R1 limbs, R1-R6 incl. R5, Section 5 mapping); F2 band table change; M8 formula change; #28 ladder mechanics change; every STRUCTURAL close (review maps for coverage); every Recovery exit (P14 may raise trigger-table gap); resolution of C9 or C10; landing of D3 placement feed and D4 competitor depth feed.

### 10.4 Interface contracts (I-1 to I-16)
I-1 #25 stage-entry floor register (highest consequence; entry refused back without it); I-2 Data Operations weekly packet with SellerBoard sales, Monday 06:00 / 09:00 (missing/estimated sales suspends trip test; breach-hold still writes with gap); I-3 #41 margin table (G9 PROVISIONAL; cut deploys with tag); I-4 #14 P4 branded IS and incursion terms; I-5 #28 step derivation, exit-bid, ceiling worksheet (no staging without; F2 exposure recorded); I-6 #37 rule change log (Map 4 unreadable; re-run on arrival; no delivery window governed, AM-12); I-7 #32 armed-window and plan (P3 suspends for affected cohorts); I-8 #33 ownership (no restore step; escalate); I-9 #35 continue-or-restore (rung holds; floor not recorded); I-10 #38 T+1 diff (readings void); I-11 #16 escalation and return (carried open until record returns); I-12 #17-19 membership and S-F8 rebuild; I-13 #12 structure repairs; I-14 #29 negation evidence lines; I-15 instrument-layer release posting (T0 zone H, A2); I-16 V5 and amendment path (T6 predictions; P14 within one week).

### 10.5 Documents named but not present
Master PPC Decision Criteria System v4.0 (and v4.1); Keyword Decision Record Template v3.0; PPC Strategic Doctrine v1.0 (Sections 6, 8, 9, 12, 14); Master PPC Data Architecture v1.0 (Sections 4, 6, 8, 9, 11); PPC Authority Matrix v2.0 Section 1; PPC Economics Worked-Example Set v1.0 (cases E5, E8); PPC Cross-Reference Ledger (component 26 row); Account Rollup Workbook; Transition Brief stack; SOP-12, -14, -16, -17-19, -24, -25, -28, -29, -30, -32, -33, -35, -37, -38, -41; #31 has no procedural document (C3).
