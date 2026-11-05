# SOP-27 Digest: Terminal and LTSF-Tier PPC Rules

Source: `PPC_SOP_27_Terminal_LTSF_Tier_Rules_v2_0.pdf` (27 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-27: Terminal and LTSF-Tier PPC Rules (Component #27 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-14 |
| Owner | PPC Lead with the LTSF Owner (jointly) |
| Supersedes | SOP-27 v1.0 (2026-07-24) in full |
| Closes | Cross-Reference Ledger conflict **C6**, on attachment of the **LTSF Master Decision and Operations System v2.1** |
| Thresholds | Zero local thresholds. Every threshold, band, scenario and verdict string lives in the **Master PPC Decision Criteria System v4.0** and the **Keyword Decision Record (KDR) Template v3.0** |
| Size | Rules R1-R7 (carried forward unchanged from v1.0), 14 procedures, 25 verdict mappings, 4 worked examples, 12 failure modes, 10-row operator ramp, 18 interface contracts |

**Verdict / purpose.** Terminal-tier PPC **executes a declaration it does not make**. The LTSF Master v2.1 decides SKU archetype, risk tier, tier movement, floor price, salvage comparison and every terminal option. This SOP owns only what PPC does on receipt of that declaration. On the day of the tag the **objective function switches from rank and share to net recovery per unit moved against the declared alternative**, and switches back only when the LTSF system retracts the tag. v1.0 was 2 pages / 7 rules because the deciding system was outside the corpus (C6 open); SOP Build Kit v1.0 Section 4 "The Depth Standard V2.0" used it as the honest 2-page example, which is void at v2.0. With LTSF Master v2.1 attached the component gains 4 archetype execution classes, 4 tier postures, 11 LTSF levers PPC executes across 3 lever families, a code-red precedence seam, and previously unwritable interfaces.

### 1.1 The seven rules R1-R7 (identified from procedure headings and citations; the SOP never tabulates them in one place)

| Rule | Content as used in the text |
|---|---|
| R1 | Objective switch and retag to liquidation objective on a terminal tag (P2) |
| R2 | Allowable ad cost per unit = net recovery at salvage price minus the alternative's per-unit value; maximum liquidation CPC = allowable ad cost x CVR (P3) |
| R3 | Cliff pacing: required units/day = remaining units / days to cliff; required clicks/day = required units / CVR; traffic check vs market CPC (P4) |
| R4 | Shut-off on terminal-tagged variations: rank objectives removed, funded pushes stopped, discovery closed, brand-defense allocation removed, placement modifiers normalized to zero; only proven converters at R2 ceiling remain (P6) |
| R5 | Structural quarantine: dated liquidation campaigns, tagged variation removed from standing structure, same week as the tag; quarantines the **tag, not the tier** (P5) |
| R6 | Expiry check: weekly comparison of realized recovery vs alternative and realized vs required pace; every terminal decision carries its expiry from the cliff calendar (P12) |
| R7 | Sunk COGS appears in no column of any computation (P3 step 7; LTSF Principle 2) |

**Identifier collision (Section 1.6, AM-6):** bare R-numbers = this SOP's rules. v4.0 Section 11 Recovery Mode rules are written "v4.0 R1" to "v4.0 R6". SOP-32 v2.0 P12 cites this SOP's R2, R3, R4, R5, R6 without prefix.

## 2. Scope and boundaries

### 2.1 The seam (Section 1.2)

| Decided by LTSF Master v2.1 (read, never derived) | Executed by this SOP |
|---|---|
| SKU archetype A/B/C/D, assigned by owning Brand Manager, confirmed by LTSF Owner (LTSF Section 5 "SKU Classification: The Four Archetypes") | Campaign-level execution class each archetype selects: objective, levers open/shut |
| Risk tier GREEN/YELLOW/RED/CRITICAL (LTSF Section 7.1 "Tier definitions and cadence") | PPC posture each tier selects; posture change staged same day tier changes |
| Tier movement (LTSF Section 7.3 "Tier movement rules") | Nothing. Tier move is an input event; PPC proposes no move |
| Floor price (LTSF Section 4.2 "The floor price (clearance authority)") | R2 allowable ad cost and max liquidation CPC from declared floor, salvage, unit fields |
| Salvage comparison: removal net, liquidation net, disposal net (LTSF Section 6.5 "Family 5: Terminal levers") | Nothing. PPC reads winning alternative's per-unit value as the R2 subtrahend |
| Every terminal option and execution, PO freezes, removal logistics | Lane-closure finding routed back when arithmetic says PPC cannot clear units |
| Discount, coupon, deal depth and max combined stack | Bid/budget consequences of a depth change and the CVR re-read that moves R2 ceiling |

### 2.2 Archetypes as PPC execution classes (Section 1.3)

| Archetype | Execution class / procedure | LTSF Section 6.2 Family 2 levers that open | What PPC does not do |
|---|---|---|---|
| A - Fixable Demand | Rebuild traffic on listing being repaired in parallel. **P7**. PPC does not wait for repair, does not substitute for it | Competitor keyword replication; new discovery campaigns; break-even PPC scaling once CVR read recovers | Does not lead with depth (price lever on broken listing = LTSF Principle 4) |
| B - Variation Overstock | Child-ASIN targeting problem on the D2 variation map with re-point machinery. **P8** | Refined targeting on non-preferred children; discovery scoped to those children | Does not touch parent or healthy children. No family-wide budget move, no shared coupon, no parent re-point |
| C - Structurally Dead | Clear what the ceiling buys and stop. **P9**. 7-day decide window | Break-even PPC scaling on proven converters only, at R2 ceiling, in dated liquidation campaign | No experiments: no discovery, no auto probe, no competitor replication, no new keyword test |
| D - Aged Healthy | Speed, not exit. **P10**. Batch racing a bracket date | Budget/bid increases on proven syntaxes; break-even scaling with spend ceiling at contribution above floor price | No retag to liquidation, no quarantine. Rank objectives stay legal on untagged terms |

**1.3.1 Archetype C and the 7-day window:** LTSF Section 5: no further experiments; decide within 7 days of classification. Every LTSF 6.2 discovery lever has a 7-14 day impact window, and LTSF Section 9.1 "Pre-registered 7-day tests" gives each lever a 7-day read before scaling. Read window >= decision window, so test has no decision value. Example: 480-unit batch in 366-455 day bracket at $6.90/unit/month: one 7-day window = 480 x 6.90 / 30 x 7 = **$772.80**. P9 opens no test; F7 is the failure.

### 2.3 Tiers as PPC postures (Section 1.4)

| Tier | PPC posture | Structural state | Cadence |
|---|---|---|---|
| GREEN | Standing ops unchanged. Only action: proactive velocity read when a large batch approaches the pre-LTSF window | No retag, no quarantine; units in standing campaigns | Weekly pass reads flag, does nothing else; P1 step 6 records the read |
| YELLOW | Velocity work live on aged children/batch at archetype's lever set. Push spend on affected variation frozen at current level by v4.0 Section 5 gate **G6** where inventory reads YELLOW for stockout reason, and by **P13** where freeze is LTSF-driven | No retag. Dedicated ad groups where aged units sit on specific children | Weekly inside Monday pass; P12 check line written whether or not tier moved |
| RED | Execution, not planning. Full archetype lever set at R2 ceiling. Archetype C and any terminal tag retag under R1, quarantine under R5 | Dated liquidation campaigns with cliff date in name for terminal-tagged units; dedicated ad groups for aged-batch units not yet terminal | Weekly minimum; daily pace watch armed inside final 14 days before cliff |
| CRITICAL | Emergency. R4 shuts everything not a proven converter at R2 ceiling. Lane clears at ceiling or finding routes back same working session | Quarantine complete; no terminal-tagged unit in a standing campaign | Twice weekly (LTSF 7.1) + daily Brand Management & PPC huddle line (LTSF 10.1); daily pace watch standing |

### 2.4 Adjacent components (Section 1.5)

| Component | Seam |
|---|---|
| LTSF Master v2.1 (outside PPC register) | Decides archetype, tier, movement, floor, salvage, depth, terminal options. Tier criterion/floor/archetype call written here is a defect |
| Criteria System v4.0 (#8) | Every threshold, band, gate, scenario, lever limit, verdict string. Threshold written here is a defect |
| #12 Exact campaign operations | Executes campaign creation, bid, budget, status, structure incl. the P10 re-point for Archetype B. This SOP issues liquidation campaign spec; #12 stands it up |
| #32 Deal and event window | Owns window plan, caps, arming, reconciliation. Its P12 computes a liquidation window under this SOP's R2, R3, R4, R6 |
| #26 Mature, defend and code red | Code-red declaration, same-day freeze, four-map diagnosis, loss-ordered cut sequence, exit test. Precedence seam at 1.5.1 / WE-4 |
| #25 Transition and maintenance | Descent from push to sustainable economics, hands exit to #26. Referenced by Ledger row 25 only; a terminal tag is not a transition. **Not attached to this session** |
| #28 Placement and modifier | Ladder mechanics, exit-bid discovery, modifier sizing. R4 normalizes modifiers to zero (a state, not a ladder) |
| #29 Negation architecture | Doctrine and wall levels. R5 quarantine built with #29 walls in same session as retag |
| #33 Sibling and family arbitration | Shared-term ownership. Terminal tag on one sibling is a family event; this SOP routes, never reassigns |
| #37 Automation platform rules | Excludes terminal-tagged entities from all rules; this SOP supplies protected-scope state feed |
| #38 Bulk-file deployment | Staging format, upload, T+1 verification. Every change deploys through it |
| #35 Incrementality testing | Test design, continue-or-restore. No incrementality test on a terminal-tagged entity (R4 removes defense allocation) |
| G6 inventory bands and D2 re-point chain | G6 measures stockout risk; reads GREEN on an overstocked variation correctly, not an authorization to scale. LTSF risk is separate |

**1.5.1 Precedence seam with #26:** v4.0 Section 11 rule **T8** orders Recovery Mode > Event Mode > stage defaults; does not name the terminal lane (AM-2). R5 quarantine is the mechanism: liquidation campaigns are not standing campaigns, so #26's loss-ordered cut sequence does not reach them. What binds: **v4.0 R3** - while Recovery Mode active, every bid move >15% and every budget move >$25/day is human-confirmed, including liquidation lane.

## 3. Triggers (Section 2)

v4.0 carries no interface-lag threshold; lags are cadence facts from LTSF 9.2, LTSF 7.1 or this SOP's R5 (gap AM-3).

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| New terminal/at-risk tag on a variation | LTSF row in LTSF Master Tracker (archetype, tier, floor price, salvage value, remaining units, cliff date), mirrored into T2 Keyword Command block **K2 "Targeted variation(s)"** as terminal flag | Same day. LTSF 9.2: 24 hours decision-to-live for PPC campaign changes; R5 requires quarantine inside tag week | P1, then P2, P3, P4, P5, P6 in sequence |
| Tier change on already-tagged SKU | Weekly auto-classification (LTSF 10.2 "The weekly cycle" step 3) landing in LTSF row | Same day for move into RED/CRITICAL; next Monday pass for a move down | P13, then archetype procedure |
| Archetype change or first assignment | Archetype column (LTSF 11.1 amendment 7) with date assigned and owner | Same day | P1 step 4, then P7/P8/P9/P10 |
| Cliff-calendar update incl. bracket crossing | Cliff calendar columns (LTSF 11.1 amendment 6): units per age bracket, date largest bracket crosses next cliff, weekly velocity-to-cliff requirement | Same working session | P4 in full, then P12 |
| Floor price, salvage value or depth change | Floor price column and salvage comparison columns (LTSF 11.1 amendments 2 and 3) | Same working session | P3 recompute, then P4 re-run |
| Weekly expiry check | T6 Decision Log rows with review date this cycle + LTSF outcome log (LTSF 9.4) | Monday, inside standing pass, before any new verdict | P12 |
| Daily pace watch inside final 14 days before cliff | Realized units vs R3 pace from **T3 Campaign Board group C4** order counts on dated liquidation campaigns | Daily, one read per working day; CRITICAL arms unconditionally | P12 step 5 |
| Deal/event window touching tagged variation | #32 armed-window declaration entering T2 with event flag under v4.0 gate **G12** | Before window opens | P11 step 4 (#32 P12 owns the plan) |
| Code-red declaration on product with terminal tag | **T0 Product Command zone A** verdict banner reading CODE-RED + #26 declaration record | Same day | P13 step 5 and 1.5.1 seam |
| Lane cannot buy required clicks at R2 ceiling | P4 traffic check output | Same working session; LTSF 7.4 escalates any decision blocked >5 business days | P14 |
| Tag retracted or units cleared to zero | Remaining units zero in LTSF row, or tag column clearing | Next Monday pass | P14 step 4, closure record |
| Day-7 read returns below half its logged prediction | Prediction and outcome log (LTSF 11.2) vs T6 prediction | Day the read is clear; LTSF 9.1 replaces lever rather than extending | P12 step 4 |

## 4. Preconditions and gates (Section 3)

Missing/stale field group suppresses its dependent execution class, recorded in **T7 Manifest**; pass continues on readable rows (v4.0 gate **G8**).

| Precondition | Manifest ID (T7 group) | Observable that proves it passed | Suppressed while failing |
|---|---|---|---|
| Declaration complete | Not a PPC group; LTSF row recorded in T7 as external feed row | **Seven fields present and dated:** archetype, tier, floor price, salvage value per unit, remaining units, cliff date, winning terminal option | Everything. P1 returns row to LTSF Owner. No partial execution, no estimated field |
| Converter evidence sufficient | **A4** sample sufficiency buckets | Proven converter set clicks at/above v4.0 gate **G2** on declaration window; below = CONTINUE TEST TO 50 CLICKS AT CAPPED BID, not a CVR read | R2 max liquidation CPC (function of CVR). P3 holds, P4 cannot run |
| No quarantined rows | Zero-flag columns feeding gate **G1** | No impossible-metric flag in liquidation set; CVR zero with orders present quarantines | Every verdict on that row. Verdict QUARANTINE: DATA REFRESH; repair task same day |
| Campaigns not truncated | **A3** pacing and in-budget | In-budget % at/above gate **G3** line on every dated liquidation campaign | Every bid conclusion; budget lever first per v4.0 Section 9 rule **L1** |
| Advertised SKUs eligible | **A7** eligibility | Eligibility live on every advertised child | All execution on target, same day (gate **G4**) |
| Variation map resolves | **D2** variation map | Every term maps to the specific aged child (not parent, not preferred child) | P8 in full; row carries D2-pending flag |
| Economics chain fresh | **D1** per-variation margin, **B8** economics chain | T0 zone C named cells live; margin table version dated inside **45-day staleness clock**; gate **G9** fresh not PROVISIONAL | Nothing suppressed, but ceiling-referencing actions stage with PROVISIONAL tag |
| Price stable | D1 + **T5 Product Log** price-move rows | No price change on advertised child in trailing **7 days** (G9). A depth change is a price change | Any CVR-derived conclusion; R2 ceiling holds at last value (P3 step 6) |
| Event windows known | Event-mode column in T2 block K2, fed by #32 | Armed-window declaration with dates before window opens (G12) | Structure changes inside window |
| Sibling conflicts resolved | Family conflict state in T2 block K2 | No sibling with active push objective on a term the lane buys (gate **G11**) | Scale on shared term until lead assigned; routes to #33 |
| Keyword list clean | MKL state feeding gate G12 MKL hygiene | Every term in liquidation campaign in current keyword list with syntax tag and relevancy score | Analysis of untagged terms (route to maintenance) |
| Automation excluded | **D6** automation platform rules export, status **OPEN** per Ledger | #37 exclusion list names every dated liquidation campaign; while D6 OPEN confirmed by manual read, recorded | Nothing formally; unexcluded campaign = F9 |

## 5. Procedures (Section 4)

Time estimates are planning figures per SKU per tier. Every staged change deploys through #38 with reason string carrying verdict and scenario ID.

### P1. Read and validate the declaration (12 min/SKU)
1. Open LTSF row in LTSF Master Tracker. Read the seven fields in order: archetype (A/B/C/D with date assigned and owner, LTSF 11.1 amendment 7), tier, floor price, salvage value per unit, remaining units by age bracket, cliff date of largest bracket, winning terminal option.
2. Any field blank/undated stops the procedure; return to LTSF Owner naming missing field and blocked execution class. PPC computes/estimates nothing.
3. Copy seven fields into **T2 block K2** against the variation, and into **T5 Product Log** as one dated event of type **targeting change** with LTSF row reference in **Link** column (makes later CVR/CPC swings attributable, v4.0 Section 7 rule **D5**).
4. Route on archetype (selection not overridable):
   - A -> P7 (listing repair parallel at Family 1); B -> P8 (child-ASIN, parent untouched); C -> P9 (proven converters at R2, zero experiments); D -> P10 (break-even scaling, no retag/quarantine); blank/disputed -> STOP, return to LTSF Owner.
5. Read tier, set posture per 1.4. Tier and archetype independent (RED Archetype A runs P7 at RED intensity, not P9).
6. GREEN: record read in **T6 Decision Log**, no staged change, stop (3 of the 12 minutes).

### P2. Objective switch and retag (R1) (15 min)
1. Trigger: terminal tag (Archetype C class and any unit the LTSF row marks terminal regardless of archetype). At-risk tag without terminal designation does not retag; posture only at P13.
2. Retag terms to liquidation objective in **T2 block K7 "Objective"** (mandatory under v4.0 Section 6 rule **O1**; untagged row flagged UNMANAGED).
3. Write grading metric into **K7 "Situation text"**: net recovery per unit moved (salvage price net of fees minus ad cost per unit) vs declared alternative's per-unit value. Rank/share/defense metrics stop applying.
4. Set K7 review date to **cliff date** (R6; LTSF Principle 5: no decision open-ended).
5. Record retag in T6 with prediction: units cleared by cliff, R3 required pace, review date. No logged prediction = does not deploy (v4.0 Section 14 rule **V1**).
6. Human-mandatory. Authority Matrix v2.0 row "Terminal/LTSF PPC lane": D = PPC Lead with LTSF Owner; incoming operator E.

### P3. Compute R2 allowable ad cost and max liquidation CPC (10 min)
1. Read: net recovery per unit at salvage price (declared), winning alternative's per-unit value (declared), converter CVR for proven set (PPC read from **T2 block K5**, subject to G2).
2. Allowable ad cost/unit = net recovery at salvage - alternative's per-unit value. Alternative usually negative, so ceiling usually rises.
3. Max liquidation CPC = allowable ad cost/unit x CVR.
4. Archetype D: ceiling comes from break-even PPC scaling lever (LTSF 6.2), spend ceiling per unit = contribution above floor price. Declaration carries contribution at current price and at floor price (PPC subtracts, does not model fees). Resulting CPC ceiling = v4.0 Section 3 family **F1** max profitable CPC (margin $ x CVR); break-even scaling = operate at that ceiling rather than target line.
5. Write ceiling and date into **T2 block K6** beside standing max profitable CPC. Both live in row, read apart; standing value governs untagged terms.
6. If G9 marks reads PROVISIONAL (price/depth change inside trailing 7 days), ceiling holds at last dated value; staged actions carry PROVISIONAL tag; not recomputed on provisional CVR.
7. Sunk COGS in no column (R7, LTSF Principle 2). Citing acquisition cost = F2.

### P4. Cliff pacing and traffic check (R3) (20 min)
1. Required units/day = remaining units / days to declared cliff date (both declaration fields).
2. Required clicks/day = required units/day / converter CVR.
3. Read market CPC on proven converter set from **T4 Placement & Bid column "Expected CPC"** and current suggested-bid values in **BULK-US Raw Pull Pack**, at the volume the lane needs (CPC clearing 40 clicks/day is not the CPC clearing 300).
4. Compare market CPC at required volume vs P3 ceiling:
   - <= ceiling -> **LANE OPEN**: stage full required-clicks budget; arm P12 pace watch.
   - above ceiling but residual volume clears at/under ceiling -> **LANE SPLIT**: buy what ceiling buys; state residual units; route remainder to LTSF Owner.
   - no volume clears at/under ceiling -> **LANE CLOSED**: P14; finding routes back same session (salvage price moves down raising CVR and re-runs, or terminal option on whole pool).
5. Lane open: daily budget = required clicks/day x market CPC, staged on dated liquidation campaign; re-derived whenever cliff date, unit count, floor price or CVR moves.
6. Split: state in T6 units PPC clears vs units terminal option takes; route second number to LTSF Owner same session. Normal outcome, not escalation.
7. Closed: run P14. Correct outcome, not failure.

### P5. Structural quarantine (R5) (35 min first campaign on SKU; 10 min per later variation)
1. Trigger: any P2 retag. Executes same week as tag, without exception.
2. Specify dated liquidation campaign, hand to #12: one campaign per tagged variation; **cliff date in campaign name**; advertised SKU = specific aged child from D2; one ad group with proven converter set only.
3. Remove tagged variation from standing family structure same week: **pause** terms where standing campaign advertises only that child; **negative-exact** them where standing campaign advertises several. #29 owns wall level; this SOP supplies term list and reason.
4. Record wall list in **T3 Campaign Board group C5 "Negation state per mode"** as wall-audit baseline.
5. Placement modifiers = zero on all three groups at creation.
6. Add campaign to **#37 exclusion list** and record it. While D6 OPEN, manual read logged.
7. Tagged variation still serving inside a standing campaign past the tag week = F3.

### P6. Shut-off execution (R4) (15 min)
1. On terminal-tagged variations stage as one set: rank objectives removed, funded pushes stopped, discovery spend closed, brand-defense allocation removed, placement modifiers normalized to zero.
2. What remains: exact and auto close match on proven converters only, at R2 ceiling.
3. Freed push budget does **not** return to the **M5 queue**; returns to the **LTSF recovery plan**. State amount and destination in same staged set.
4. Push/rank objective live on a tagged variation: R1 and R4 same day; F1.
5. Not in Recovery Mode: human-confirmed at standard v4.0 Section 12 rule **P5** tier. In Recovery Mode: v4.0 R3 tightened line applies to every step.

### P7. Archetype A: rebuild traffic while curve is repaired (40 min first build; 15 min/weekly pass)
1. Read diagnosed defect from declaration: click-through, conversion, or both (LTSF 5 diagnoses; PPC does not re-diagnose).
2. Do not lead with depth, do not wait for repair. Both tracks from day one: listing sprint is Design's under LTSF 9.2 **48-hour SLA**; paid rebuild is this procedure's under **24-hour SLA**.
3. Competitor keyword replication (LTSF 6.2: "single best-grounded targeting method"). Reference competitors named in declaration: same price, same rating, comparable offer, inside **top 10,000 BSR**. Pull ranking and bidding terms from **Keepa competitor pull** and **SQP export** in Raw Pull Pack. Stage exact set inside dated liquidation campaign, seeded at term's Expected CPC from T2 K6, capped at R2 ceiling.
4. Replication is a keyword lever, not a conquest open; does not target competitor ASIN. PAT/conquest stays with #16 on its weakness flags.
5. New discovery campaigns where declaration authorizes test budget: fixed budget, capped bid, dated stop-loss, **expiry before the cliff date**.
6. Break-even scaling opens only once CVR read recovers past declared benchmark (LTSF Principle 4: 40% discount on a listing converting far below norm sells 6 units instead of 4 at worse economics).
7. Each lever has logged prediction with basis tag before launch (LTSF 8.2 "Velocity uplift estimates (the judgment half)"): **HIST** (product's own lever history), **MARKET** (competitor-anchored ceiling), **TEST** (pre-registered 7-day test). Untagged multiplier renders blank in tracker and blocks the scenario from ranking.
8. Read at day 7; below half the prediction, replace rather than extend (LTSF 9.1).

### P8. Archetype B: child-ASIN targeting (35 min first build; 10 min/weekly pass)
1. Read which children hold aged units. LTSF 5 diagnostic: specific colors/sizes hold **80% or more** of aged units against a parent that sells well.
2. Open T2 K2 and D2 map; list every live campaign whose advertised SKU is the preferred child while aged units sit on a non-preferred child (aged children usually excluded entirely).
3. Stage re-point toward aged child at **#12 P10** against D2. Direction: G6 re-point moves spend away from thinning child to ranked backup; this moves spend **toward** overstocked child. Same machinery, opposite direction.
4. Term with no exact instance pointed at aged child: **ADD EXACT + RESTRUCTURE** in aged child's dedicated ad group, walls built same session.
5. Refined targeting: dedicated ad groups per aged child; per-child bids from child's own economics, not family blend (v4.0 Section 8.8 "Conversions Scenarios (S-P1 to S-P8)" scenario **S-P8** catches this error).
6. New discovery scoped to aged children only, fixed test budgets, where child demand never mapped.
7. Do not touch parent or healthy children (LTSF hard rule; F8).
8. Aged child shares a term with sibling product: G11 holds, route to #33 before any scale step.

### P9. Archetype C: clear what ceiling buys, then stop (20 min)
1. P2, then P5, then P6, in that order, inside tag week.
2. Build proven converter set from **lifetime search term reports** and **SP and SB search term reports** in Raw Pull Pack: terms with orders at/above G2 sufficiency line on declaration window. Nothing else enters.
3. Every bid at/under R2 max liquidation CPC. No ladder, no step size, no discovery from above.
4. No experiments (discovery, auto probe, competitor replication, new keyword test, placement test). F7.
5. Run P4. Archetype C lanes close most often (floor at/near salvage, thin ceiling). Route closure; do not widen term set.
6. Where declaration escalates a new launch with no organic traction to strategic viability review: PPC contributes lifetime converter list, untested-term map, tested-and-failed list, and stops. Exit/redesign/reposition is not PPC's.

### P10. Archetype D: break-even scaling vs bracket date (30 min first build; 12 min/weekly pass)
1. No retag, no quarantine. Rank objectives on other terms continue at #12.
2. Read weekly velocity-to-cliff requirement from cliff calendar; convert to required units/day and clicks/day under P4.
3. Identify proven syntaxes from **T1 Syntax Board group S5 "Four-quadrant diagnosis"**: STRONG and VISIBILITY syntaxes carrying the affected size/child. Budget/bid increases = fastest lever, **1-3 day** impact window.
4. Raise ceiling from target line to break-even line (P3 step 4); stage bid step to new ceiling on proven syntaxes only. Moves no price, damages no anchor, stacks with no coupon, zero margin dollars at break-even line.
5. Raise daily budget to required-clicks figure. Budget precedes bid when truncated (v4.0 Section 9 rule **L1**).
6. Guard: realized net price stays above declared floor price at every step. Depth rung from LTSF ladder fires -> net price falls, guard tightens, ceiling recomputed at P3.
7. Log prediction with basis tag; read day 7 (LTSF 9.1).
8. If pace math says batch clears before bracket date at break-even ceiling, no depth rung or terminal option needed; PPC says so in P12 check line.

### P11. Family 3-5 levers PPC executes (45 min first build; 10 min per later SKU)
1. **Sponsored Display retargeting** of family detail-page viewers with creative featuring aged SKUs and offer; **3-14 day** impact window. Judged on CPA vs R2 allowable ad cost/unit, not standing efficiency band. Mode: v4.0 Section 8.10 "Brand-Format Scenarios (S-F1 to S-F8)": **S-F5** CPC mode vs CPA ceiling; **S-F6** vCPM mode on new-to-brand and assisted conversions. Scoring vCPM on an efficiency band = structural error.
2. **Brand Store clearance page fed by Sponsored Brands**: one standing page aggregating every aged SKU, **1-2 week** build window, built once, maintained. Page build is Design's; SB traffic spec is this SOP's; execution #17-19.
3. Clearance page membership = the **tag, not the tier**: enters with terminal/at-risk tag, leaves when tag clears or units zero. P12 checks weekly against LTSF row.
4. Deal/event window on tagged variation: #32 P12 owns plan; this SOP supplies R2 and R3. Deal price raises CVR, raising max liquidation CPC proportionally. Re-run P3 and P4 at window CVR **before** window opens.
5. All other LTSF 6.3, 6.4, 6.5 levers executed outside PPC: coupons, Prime Exclusive Discounts, price drops, outlet deals, deals, brand tailored promotions, social codes, virtual bundles, cross-channel paths, every terminal lever. PPC reads their effect on CVR/net price and recomputes ceiling.

### P12. Weekly expiry check and pace watch (R6) (20 min/SKU weekly; 5 min/daily read)
1. Run before any new verdict is read on SKU (v4.0 Section 14 rule V1).
2. Write check line with exactly **four numbers**: realized recovery per unit moved, declared alternative's per-unit value, realized pace (units/day), R3 required pace. Written whether or not anything changed.
3. Alternative wins on first comparison -> PPC stops that week; route to P14.
4. Read every deployed lever vs day-7 prediction; below half -> replace (LTSF 9.1). Paid equivalent of zero-velocity coupon = discovery campaign at zero graduations.
5. Inside final **14 days** before cliff, and unconditionally at CRITICAL: read realized units vs R3 pace once per working day from **T3 group C4** order counts on dated liquidation campaigns.
6. Carry SKU line into daily Brand Management and PPC huddle (LTSF 10.1) when a rung target or expiry date at risk.
7. Re-derive R3 pace whenever remaining units, cliff date or CVR moved.

### P13. Tier posture change (15 min)
1. Trigger: weekly auto-classification moves tier, or archetype change. PPC proposes no tier move (LTSF 7.3).
2. Route on direction:
   - GREEN -> YELLOW: open archetype lever set on aged children/batch; no retag.
   - YELLOW -> RED: full lever set at R2 ceiling; retag and quarantine where terminal; arm daily pace watch inside final 14 days.
   - RED -> CRITICAL: R4 shut-off complete; twice-weekly cadence; daily pace watch standing; lane closes or clears same working session.
   - Any move down: relax at next Monday pass; do **not** un-quarantine on a tier move alone (R5 quarantines the tag).
3. Move into RED/CRITICAL: stage same day. Move down: next Monday pass.
4. Write posture change into T6 with tier on both sides and LTSF row reference.
5. Code-red on same product: lane continues inside quarantine; every step human-confirmed at v4.0 R3 tightened line.

### P14. Lane closure, handback and closure record (25 min)
1. Trigger: P4 lane closed, P12 alternative winning, cliff date arrives, or remaining units zero.
2. Write finding as **five numbers**: required clicks/day, R2 ceiling, market CPC at required volume, units PPC can clear at ceiling, residual. A conclusion without them is returned (F11).
3. Set rows to **PAUSED-PENDING (REASON + RE-ENTRY)**; re-entry criterion = declaration change that would reopen lane (lower floor price, deal-window CVR, more days to cliff). v4.0 Section 6 rule **O5** requires blocking reason, re-entry criterion, review date.
4. Units zero or tag cleared: closure record = units cleared through lane, total ad spend, realized recovery/unit vs alternative, predicted-vs-actual delta per lever for LTSF outcome log (basis tag HIST for next exit program).
5. Archive dated liquidation campaign only after closure record written; remove from #37 exclusion list and Brand Store clearance page same session.
6. Escalate rather than close if decision blocked **>5 business days** awaiting input (LTSF 7.4 "Escalation thresholds").

## 6. Rules, thresholds and numbers

### 6.1 Formulas
| Formula | Definition |
|---|---|
| R2 allowable ad cost/unit | Net recovery at salvage price - winning alternative's per-unit value |
| R2 max liquidation CPC | Allowable ad cost/unit x converter CVR |
| Archetype D ceiling | Spend ceiling per unit = contribution at current price - contribution at floor price; bid ceiling = contribution x CVR (= F1 max profitable CPC) |
| R3 required units/day | Remaining units / days to cliff |
| R3 required clicks/day | Required units/day / CVR |
| Liquidation daily budget | Required clicks/day x market CPC (at required volume) |
| R6 check line | Realized recovery/unit; alternative per-unit value; realized pace; required pace |
| Bracket-step cost | Units crossing x (next bracket rate - current rate) per month |
| Test-window charge | Units x monthly rate / 30 x days |

### 6.2 Numeric values quoted in the SOP (non-example)
| Value | Meaning / source |
|---|---|
| 7 days | Archetype C decide window (LTSF 5); lever read window (LTSF 9.1); G9 price stability trailing window |
| 7-14 days | Impact window of LTSF Family 2 discovery levers |
| 1-3 days | Impact window of budget/bid increases on proven syntaxes (Archetype D) |
| 3-14 days | SD retargeting impact window |
| 1-2 weeks | Brand Store clearance page build window |
| 24 hours | LTSF 9.2 decision-to-live for PPC campaign changes |
| 48 hours | LTSF 9.2 SLA for Design listing sprint |
| 14 days | Final window before cliff when daily pace watch arms |
| 5 business days | LTSF 7.4 escalation of blocked decision |
| 45 days | Margin table staleness clock (economics chain freshness) |
| 80% or more | Share of aged units on specific children = Archetype B diagnostic (LTSF 5) |
| Top 10,000 BSR | Reference competitor filter for replication (P7) |
| Half of logged prediction | Day-7 replace threshold (LTSF 9.1) |
| 50 clicks | In verdict string CONTINUE TEST TO 50 CLICKS AT CAPPED BID |
| >15% bid / >$25/day budget | v4.0 R3: human-confirmed while Recovery Mode active |
| >25% bid / >$50/day budget, 500+ search volume | v4.0 rule P5 permanent human-confirmed tier (with every gate failure, structural change, low-confidence verdict) |
| 4-7% | v4.0 family F2 mature TACOS reference band (WE-4); >2x band limb = code red (S-A4) |
| 50% accuracy over 10+ predictions | v4.0 rule V5 rule review (AM-9) |
| Twice weekly | CRITICAL cadence (LTSF 7.1) |

### 6.3 LTSF Section 3 rate card values quoted in the worked examples
| Bracket | Rate per unit per month |
|---|---|
| 211-240 days | $1.00 |
| Step at day 241 | $1.50 |
| 271-300 days (271-day cliff) | $5.45 |
| 366-455 days | $6.90 |
| 456+ days | $7.90 |

### 6.4 Criteria System v4.0 references
| ID | Meaning as described |
|---|---|
| G1 | Validation quarantine: impossible-metric flag (e.g. CVR zero with orders) quarantines row |
| G2 | Sample sufficiency line; proxy for proven converter set membership (AM-4) |
| G3 | In-budget/truncation line; truncated campaigns misread pace and CPC |
| G4 | Eligibility; ineligible ad halts execution same day |
| G6 | Inventory bands (stockout risk); freezes push spend where YELLOW for stockout reason; reads GREEN on overstock |
| G8 | Packet completeness; missing groups suppress dependent execution, recorded in T7 |
| G9 | Price stability (7 days) / freshness; PROVISIONAL tag |
| G11 | Sibling conflict; no scale on shared term until lead declared |
| G12 | Event window armed-declaration; MKL hygiene |
| F1 | Max profitable CPC = margin $ x CVR |
| F2 | Mature TACOS reference band 4-7% |
| O1 | Objective field mandatory; untagged = UNMANAGED |
| O5 | Pause requires blocking reason, re-entry criterion, review date |
| D5 | Product Log events make CVR/CPC swings attributable |
| L1 | Budget lever before bid when truncated |
| M1 | Cited in Q5 (Section 10) with F1 for break-even scaling legality |
| S-A4 | Product-level code-red scenario (Section 8.1) |
| S-A10 | CONSTRAINED, LTSF-burdened products on profit-only posture; LTSF velocity routed to deals/pricing (AM-1) |
| S-P8 | Child read against parent's blended line error (Section 8.8) |
| S-F5 / S-F6 | SD CPC mode vs CPA ceiling / vCPM mode on NTB and assisted conversions |
| T8 | Recovery > Event > stage defaults; no terminal lane named |
| v4.0 R3 | Recovery Mode: bid >15%, budget >$25/day human-confirmed; bars new Ranking objectives |
| v4.0 R4 | Recovery Mode daily with twice-weekly mini-audits (AM-8) |
| v4.0 R6 | Recovery lessons belong in post-exit review |
| P5 | Human-confirmed tier (500+ SV, gate failures, structural, bid >25%, budget >$50/day, low-confidence) |
| V1 | Unscored actions do not accumulate; prediction required |
| V3 | Cited for amendment routing (Q12) |
| V4 | Daily alerts, weekly full audit, monthly and quarterly reviews (AM-8) |
| V5 | Rule review below 50% accuracy over 10+ scored predictions |

## 7. Data inputs required

**LTSF declaration (LTSF row in LTSF Master Tracker, per LTSF Section 11.1):**
- Archetype (A/B/C/D) with date assigned and owner (amendment 7 column)
- Risk tier (GREEN/YELLOW/RED/CRITICAL)
- Floor price (amendment 2/3 columns)
- Salvage value per unit / net recovery at salvage price; salvage comparison columns: removal net, liquidation net, disposal net
- Winning terminal option
- Remaining units by age bracket
- Cliff calendar (amendment 6): units per age bracket, date largest bracket crosses next cliff, weekly velocity-to-cliff requirement
- Contribution at current price and contribution at floor price, per unit (Archetype D; from LTSF Owner with Finance, I-2)
- Diagnosed defect for Archetype A (click-through / conversion / both); declared CVR benchmark
- Reference competitors (Archetype A): same price, rating, comparable offer, top 10,000 BSR
- Authorized test budget (Archetype A)
- Children holding aged units (Archetype B)
- Tag column (terminal / at-risk); depth, coupon, deal levels
- LTSF prediction and outcome log (LTSF 9.4 / 11.2)
- LTSF rate card (LTSF Section 3)

**PPC Command Workbook:**
- T0 Product Command zone A (verdict banner, CODE-RED); zone C named economics cells and margin table version
- T1 Syntax Board group S5 "Four-quadrant diagnosis" (STRONG, VISIBILITY syntaxes)
- T2 Keyword Command blocks K2 "Targeted variation(s)" (terminal flag, event-mode column, family conflict state), K5 (converter CVR), K6 (standing max profitable CPC, Expected CPC, R2 ceiling and date), K7 "Objective" and "Situation text" and review date, K9 verdict
- T3 Campaign Board groups C1 (advertised SKU, campaign name), C4 (order counts on liquidation campaigns), C5 "Negation state per mode" (wall list)
- T4 Placement & Bid column "Expected CPC"
- T5 Product Log (price-move rows, targeting change events, Link column)
- T6 Decision Log (predictions, review dates, check lines)
- T7 Manifest (field groups, external feed row)
- KDR Cycle File (Monday afternoon values-only snapshot, block K9 verdict, scenario ID, expected outcome)
- Account Rollup A3 (V5 scoring consumer)

**Catalog field groups:** A3 pacing and in-budget, A4 sample sufficiency buckets, A7 eligibility, B8 economics chain, D1 per-variation margin, D2 variation map, D6 automation platform rules export (OPEN), D7 decision log.

**Raw Pull Pack:** BULK-US suggested-bid values; lifetime search term reports; SP and SB search term reports; Keepa competitor pull; SQP export; search-term joins feeding the converter set. Pack Monday 06:00, refresh complete 09:00 (I-4).

**Other:** MKL (syntax tag, relevancy score); #37 exclusion list; #38 T+1 verification report; #32 armed-window declaration; #26 code-red declaration record; #33 declared family term owner; per-variation margin (#41 owner); Brand Store clearance page membership; Authority Matrix v2.0.

## 8. Outputs and artifacts (Section 8)

| Event | Named record | Location and retention | Downstream consumer |
|---|---|---|---|
| Declaration receipt (P1) | Seven fields against variation + one dated T5 event type targeting change with LTSF row reference | T2 K2 and T5 Product Log; life of product log | Attribution reads (rule D5); #32 when window touches |
| Retag (P2) | Objective = liquidation in K7 with grading metric in situation text, review date = cliff date, plus T6 prediction row | T2 and T6; T6 retained as scoring corpus | V5 scoring; #37 exclusion; LTSF outcome log |
| Ceiling and pace (P3, P4) | R2 allowable ad cost/unit, max liquidation CPC with date, R3 required units and clicks/day, traffic-check result | T2 K6 beside standing max profitable CPC; recomputed not versioned | #32 P12 (window cap = R2 ceiling x R3 pace) |
| Quarantine (P5) | Liquidation campaign spec (cliff date in name), wall list, modifier-zero state, #37 exclusion entry | T3 groups C1 and C5; wall list retained as wall-audit baseline | #12, #29, #37, #38 |
| Shut-off (P6) | Staged set removing rank objectives, pushes, discovery, defense; freed budget amount and destination | Staged via #38; amount in T6 | LTSF recovery plan; #38 T+1 |
| Weekly check (P12) | R6 check line (four numbers) | T6, one row per SKU per cycle; life of tag plus closure record | LTSF Owner weekly cycle; daily huddle; Account Rollup A3 |
| Daily pace read (P12 step 5) | Units cleared vs required pace, one line per working day | T6; through closure | Daily BM and PPC huddle |
| Lane closure (P14) | Five-number handback + PAUSED-PENDING rows with re-entry criteria | T6 and LTSF row | LTSF Owner |
| Closure record (P14 step 4) | Units cleared, total ad spend, realized recovery/unit vs alternative, predicted-vs-actual per lever | T6 + LTSF prediction and outcome log (LTSF 11.2) | HIST basis for next exit program; incentive attribution (LTSF 10.4) |
| Cycle snapshot | Tagged rows in KDR Cycle File with K9 verdict, scenario ID, expected outcome | Generated Monday afternoon, values-only, frozen | Next cycle V5; audit trail |

## 9. Verdict-to-execution mapping (Section 5)

Strings verbatim from KDR Template v3.0 "Bands & Verdicts Reference", block "CLOSED VERDICT VOCABULARY (Framework Section 17)", cross-read with v4.0 Section 13.1.

| Verdict | Terminal-lane execution |
|---|---|
| QUARANTINE: DATA REFRESH | No change; repair task same day; R2 ceiling holds; repair ticket carries SKU's bracket rate |
| UNLOCK TRAFFIC | Bid step toward, never through, R2 ceiling; at ceiling -> P4 re-run |
| FIX BUDGET (TRUNCATED) | Budget lever only on liquidation campaign; week's bid read voids; cost measured in units not moved vs R3 |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Barred on C; legal on A, B, D, capped at R2, expires before cliff |
| FUND TEST (UNFUNDED PRIMARY) | As above; funding call with LTSF Owner |
| RANK PUSH: FUND SIZED PUSH | N/A on tagged entities (R1, R4); unchanged at #12 on untagged terms |
| RECOVERY PUSH | N/A on tagged entities |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Required clicks = R3's, not standing DSTR; if R2 can't buy them -> P14 |
| FIX CONVERSION FIRST; DEFER PUSH | Archetype A standing state; PPC holds at maintenance while repair lands |
| PLACEMENT FIX FIRST | No terminal-lane form (modifiers zero); untagged Archetype D terms at #28 |
| RE-POINT VARIATION | Archetype B core move at #12 P10, toward aged child |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | Does not apply |
| HOLD; DEFEND LIGHTLY AT RANK | Does not apply (R4) |
| DEFEND AT FLOOR | Does not apply; "floor" trap: LTSF floor = price/unit vs standing floor = discovered min viable CPC (F5) |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Profitable CPC on tagged entity = R2 max liquidation CPC, not K6 standing value; syntax cap at envelope instruments |
| INCREMENTALITY LADDER | Does not apply |
| ADD EXACT + RESTRUCTURE | Legal on A and B in liquidation campaign / aged child ad group; barred on C |
| CONSOLIDATE DUPLICATES | Executes at #12 P7; tagged term in both standing and liquidation = R5 failure (F3) |
| GRADUATE FROM DISCOVERY | Legal on A, B, D; lands in liquidation campaign with walls, expiry = cliff date; barred on C |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | Steering wall makes R5 real; #29 selects level; wall list recorded in T3 C5 |
| ENTER SBV ARBITRAGE | Does not apply; brand formats via P11 judged on recovery/unit |
| OPEN / ROTATE / EXIT CONQUEST | Does not apply; replication is a keyword lever; conquest stays with #16 |
| STOP-LOSS: CONCEDE OR DEFER | Terminal form = P14 lane closure; freed budget to LTSF recovery plan |
| PAUSED-PENDING (REASON + RE-ENTRY) | P14 step 3; re-entry = floor price, deal CVR, or more days |
| LEAVE TO HARVEST | Does not apply; terminal units have no harvest horizon |

Campaign-level (KDR "Campaign Decision Record"): FUND / HOLD / TRIM BUDGET, RAISE / CUT MULTIPLIER, NEGATION PASS, CONSOLIDATE, RETAG OBJECTIVE, PAUSE (L7), ARCHIVE. On terminal lane: RAISE MULTIPLIER never issues; RETAG OBJECTIVE once at P2; ARCHIVE once at P14 step 5 after closure record.

## 10. Decision rights

| Authority Matrix v2.0 row | D | Incoming operator | What SOP-27 does |
|---|---|---|---|
| Terminal/LTSF PPC lane | PPC Lead with LTSF Owner; BM owner reviews (R) | E | Whole document. Only row with D held jointly with a role outside PPC |
| Weekly verdicts (established US) | PPC Lead | E, assigned scope | P12 inside Monday pass; Section 5 execution |
| Structure creation (all SOPs) | PPC Lead or per SOP scope | E | Liquidation campaign spec (P5), ad-group builds (P8, P9); BM owner informed |
| Code-red declaration + close | PPC Lead | E | Read-only; P13 step 5 tightened confirmation |
| Event plans (#32) | PPC Lead with deals owner | E | Supplies R2/R3; re-runs P3/P4 at window CVR |
| Push funding (M5 queue) | CEO above envelope; PPC Lead within | E | P6 step 3 freed-budget routing only |
| Bulk deployments (#38) | No D; PPC Lead reviews | E | Every staged set, T+1 reconciliation (standing rule 2: E without D executes staged decisions only) |
| Sibling declarations (S-series) | PPC Lead | E | G11 check before scale step |
| Automation rules (#37) | PPC Lead | E and R | Protected-scope feed; reads exclusion list back |
| v4.0 threshold changes | CEO | I | Nothing; 10 amendment items |

Human-mandatory (Section 9): retag (P2), every lane closure (P14), quarantine execution (P5), confirmed jointly by D holders. Standing rule 5: unfilled role's D reverts to PPC Lead and E to PPC Manager. **LTSF Owner has no vacancy clause** in either document. Scope for incoming operator from Transition Brief v1.2 (standing rule 4). Rows outside ramp: "Launch-stage verdicts + batches" and "Canada weekly block" (launch and CA operator). Declaration fields are never computed by PPC at any tenure.

**Executable with audit:** P3 ceiling computation, P4 pace/traffic arithmetic, P12 check line and daily pace read, recomputation on input change, staging bid/budget rows inside ceiling, T6 drafting, F1-F12 alarms.

**Alarm routing:** F1, F3, F9, F12 to operator queue same day; F2, F5, F6, F10, F11 to weekly pass worklist; F4, F7, F8 to PPC Lead and LTSF Owner jointly with T6 history. Same failure mode twice in consecutive cycles on same scope escalates to PPC Lead.

## 11. Failure modes (Section 7)

| ID | Failure | Detection signal | Response |
|---|---|---|---|
| F1 | Rank spend on terminal stock | Push/rank objective in T2 K7 against terminal flag in K2 | R1 and R4 same day (Strategic Doctrine v1.0 Section 14 named pattern: spend continuing after objective achieved) |
| F2 | Sunk COGS in the math | Bid/ceiling citing acquisition cost in T6 reason string or P3 working | Recompute from LTSF row (R7; LTSF Section 2) |
| F3 | Mixed reads | Terminal units serving in standing campaigns past tag week (T3 C1 advertised SKU vs tagged list) | R5 quarantine; both reads re-baseline |
| F4 | Expiry ignored | Liquidation spend live past a week alternative won R6 or past cliff date | Stop same day (LTSF 9: prior pattern of a lever running a month unexamined) |
| F5 | Two floors confused | Bid at LTSF floor price or price at discovered min viable CPC; bid in same order of magnitude as product price at staging QA | Reject row; LTSF floor = price (LTSF); discovered floor = bid (#28) |
| F6 | Ceiling carried after input moved | R2 ceiling in K6 dated before last change to floor, salvage, units, cliff or CVR | P3 recompute same session, P4 re-run |
| F7 | Experiment on Archetype C | Discovery, auto probe, replication or keyword test dated after C classification | Close same day; intent to closure record ($772.80 per 7-day window example) |
| F8 | Parent damage on Archetype B | Price/coupon/budget change touching parent or healthy child | Revert same day, re-stage on aged children only |
| F9 | Automation reaching liquidation campaign | Bid/budget change in T+1 diff with no staged row, or campaign absent from #37 list | Route to #37 change control same day; restore staged value |
| F10 | Depth changed without ceiling re-read | Coupon/deal/price move on tagged child in T5 with no P3 recompute same cycle | P3 recompute, P4 re-run |
| F11 | Lane closure reported as a conclusion | P14 handback in T6 missing any of five numbers | Return and rewrite |
| F12 | Quarantine released on tier move | Tagged variation back in standing campaigns same cycle tier moved down, terminal flag still in K2 | Re-quarantine same day |

## 12. Interface contracts (Section 12)

Standing rules: **C1** artifact is the interface (verbal tag starts nothing); **C2** non-arrival recorded in T7 per G8; **C3** suppression, never substitution; **C4** cite Ledger row, not counterparty procedure number; **C5** no contract carries a max lag (AM-3).

| ID | Direction | Artifact | Sender -> receiver | Timing | Non-arrival |
|---|---|---|---|---|---|
| I-1 | Up | LTSF declaration (seven fields, LTSF 11.1 amendments 2, 3, 6, 7) | LTSF Owner -> PPC operator | On classification and weekly re-classification | P1 stops; on 624-unit batch at $5.45 = $113.36/day charge |
| I-2 | Up | Contribution at current and floor price per unit | LTSF Owner with Finance -> PPC | With declaration | P3 step 4 cannot run; lane holds at standing target line |
| I-3 | Up | Cliff-calendar update | Data Operations via LTSF row -> PPC | Monday with LTSF weekly refresh | R3 pace holds at last value, marked stale; F6 |
| I-4 | Up | Refreshed workbook + Raw Pull Pack (A3, A7, A4, search-term joins) | Data Operations -> PPC | Pack Monday 06:00; refresh complete 09:00 | T7 marks stale; verdicts downgrade to flags; R6 line still writes with last clean read dated |
| I-5 | Up | Per-variation margin and D2 map with aged children named | #41 owner and Brand Management -> PPC | On margin event and monthly | P8 does not start; D2-pending flag |
| I-6 | Up | Armed-window declaration with dates | #32 owner -> PPC | Before window opens | Ceiling not re-run at window CVR; #32 P12 cannot build cap |
| I-7 | Up | Code-red declaration record and tightened line | #26 owner -> PPC | Same day | Lane deploys at standard tier = governance breach |
| I-8 | Up | Declared family term owner | #33 owner -> PPC | Before scale step on shared term | G11 unresolved; lane runs reduced pace, shortfall stated vs R3 |
| I-9 | Up | #38 T+1 verification report | #38 owner -> PPC | T+1 after every deployment | Reads void for week; F9 cannot fire |
| I-10 | Down | R2 ceiling and R3 required units/day in T2 K6 | PPC -> #32 owner | Before any liquidation window planned | #32 P12 sizes from standing lift index (forbidden by its P12 step 3) |
| I-11 | Down | Five-number lane-closure handback | PPC -> LTSF Owner | Same session as P4 closure | Pool accrues; WE-2 batch $110.40/day; most expensive non-arrival |
| I-12 | Down | Protected-scope state feed (every liquidation campaign) | PPC -> #37 owner | Same session as quarantine and every archive | Automation ladders bid down, lane closes silently (F9) |
| I-13 | Down | Liquidation campaign spec | PPC -> #12 owner | Same week as tag (R5) | Not created; F3 |
| I-14 | Down | Wall list on new T3 row | PPC -> #29 owner | Same session as structure event | Wall audit has no baseline |
| I-15 | Down | Freed push budget with amount and destination | PPC -> LTSF recovery plan via LTSF Owner | Same cycle as shut-off | Dollars sit unallocated; quietest failure |
| I-16 | Down | R6 weekly check line and daily pace read | PPC -> LTSF Owner and daily huddle | Weekly Monday; daily final 14 days and at CRITICAL | Rung does not fire (LTSF 9.3 makes rung fire automatic on missed target) |
| I-17 | Down | Predicted-vs-actual per lever with basis tag | PPC -> LTSF Owner and Data Operations | Day-7 read and closure | No HIST basis for next exit program; no PPC record for LTSF 10.4 attribution |
| I-18 | Down | Section 11 as ramp content | PPC Lead -> #44 owner | Ledger due date for #44 | No cross-SOP certification; AM-10 |

Repeated non-arrival (twice consecutive cycles) escalates to PPC Lead and LTSF Owner jointly with T6 history and accrued charge; carried as Ledger-row disagreement.

## 13. Account-specific facts

- No live product economics spine attached; all worked-example economics are the fictional training base of PPC Economics Worked-Example Set v1.0: AOV $80.00, contribution $28.00/order, break-even ACOS 35.0%, Target ACOS 17.5%, Max Acceptable 26.3%, CVR 5.2% (illustrative).
- Ledger dependency **D6** (automation platform rules export) reads **OPEN**; #37 exclusion confirmed by manual read only.
- **LTSF Master Tracker V1.1** (routed by SOP Build Kit v1.0 Section 3) **not attached**; tracker column names taken from LTSF Master Section 11.1 spec.
- **SOP-25** (#25) not attached to this session.
- Component **#44** operator onboarding and certification not built.
- Companion named: **Hanging Closet Organizer Full Liquidation Action Plan v1.0** (a worked application of this lane at program scale).
- Strategic Doctrine v1.0 Section 14 lists the account's named pattern of spend continuing after objective achieved.
- LTSF Section 2 records that displaying lifetime profit inclusive of COGS causes paralysis on underwater SKUs.
- LTSF Section 9 records prior pattern: a non-performing lever ran for a month unexamined.

### Worked examples (all illustrative)
| Case | Inputs | Key results |
|---|---|---|
| WE-1 RED, Archetype D | 624 units in 271-300 bracket at $5.45; next 366-455 at $6.90 in 78 days; floor $58.40; salvage -$1.05; contribution $28.00 current, $6.40 at floor; terminal option removal | 8.0 units/day, 153.8 clicks/day; headroom $21.60/unit; ceiling 28.00 x 0.052 = $1.456 vs standing target line 80 x 0.175 x 0.052 = $0.728; market CPC $1.18 -> OPEN; budget $181.54/day; week: 56 units, 1,076.9 clicks, $1,270.77 spend, $4,480 sales, lane ACOS 28.4%, net $297.23/week, ad cost $22.69/unit, $5.31 retained; full clear 12,000 clicks, $14,160 spend vs $17,472 contribution, net $3,312; do-nothing at 3.1 units/day clears 242, 382 cross into $6.90 = $553.90/month; verdict TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS, basis HIST, pace watch arms day 64 |
| WE-2 CRITICAL, Archetype C | 480 units in 366-455 at $6.90; cliff to 456+ at $7.90 in 40 days; salvage nets $6.40; alternative -$3.10; CVR 4.0% (Economics set case E7 convention) | Allowable $9.50; max CPC $0.38; 12 units/day, 300 clicks/day; market CPC $0.55; residual 45 clicks/day = 1.8 units/day = 72 units, $684.00 spend -> LANE SPLIT, 408 units to terminal; discovery proposal = F7 ($772.80); removal 408 x $1.17 = $477.36 vs 408 x $7.90 = $3,223.20/month (factor 6.8); verdicts BID DOWN TO PROFITABLE CPC; CAP SYNTAX at $0.38 and PAUSED-PENDING |
| WE-3 YELLOW, Archetype B | 900 aged units, 738 (82.0%) on 3 non-preferred children; day 226 in 211-240 at $1.00 = $738/month; step $1.50 at day 241; 271-day cliff at $5.45 in 45 days; child AOV $64.00, contribution $19.20, CVR 4.6% | Child BE ACOS 30.0%, target 15.0%, max acceptable 22.5%, max CPC $0.883 (parent 35% would overstate by 5pp); 16.4 units/day, 356.5 clicks/day; market CPC $0.52 -> OPEN; $185.39/day; 45 days: $8,342.61 spend, $11.30/unit, ACOS 17.7%, contribution $14,169.60, net $5,826.99; charge avoided 738 x (5.45-1.50) = $2,915.10/month; verdicts RE-POINT VARIATION and ADD EXACT + RESTRUCTURE, basis MARKET |
| WE-4 RED lane inside code red | WE-1 product; weekly spend $4,100 vs sales $25,466 = TACOS 16.1%; F2 band 4-7%, 2.30x -> S-A4 | Cutting lane: spend -$1,270.77, contribution -$1,568.00, holding 624 x $5.45 = $3,400.80/month = $793.52/week -> net **$1,090.75/week worse**; post-cut TACOS 13.5% = 1.93x (looks better); no verdict issues on lane; finding files as amendment proposal into #26 post-exit review |

## 14. Open items

### 14.1 Amendment items (v4.1 list, Section 10.5)
| ID | Statement |
|---|---|
| AM-1 | v4.0 S-A10 puts CONSTRAINED LTSF-burdened products on profit-only posture routing velocity to deals/pricing; R2 authorizes ad cost above contribution. No rule for a unit in both; R5 quarantine is the operating separation; v4.0 should state or reject |
| AM-2 | T8 does not name terminal lane; no precedence for LTSF RED/CRITICAL + code-red; priced at $1,090.75/week (WE-4) |
| AM-3 | v4.0 has no interface-lag threshold; timings are cadence facts (LTSF 9.2, 7.1, Data Architecture Section 12) |
| AM-4 | No membership threshold for proven converter set (no order count, click count, window); G2 used as proxy |
| AM-5 | v4.0 carries no LTSF dimension (no bracket rate, floor, salvage, cliff, archetype, tier) |
| AM-6 | Rule-identifier collision R1-R7 vs v4.0 R1-R6 |
| AM-7 | Escalation rules count different things: LTSF 7.4 (dollars per product per month; 5 business days) vs PPC (same failure mode in consecutive cycles) |
| AM-8 | Cadence conflict: LTSF weekly / twice weekly CRITICAL / daily huddle vs v4.0 V4 and Recovery R4; SOP runs the stricter as a working choice |
| AM-9 | LTSF 9.1 half-of-prediction lever replace vs v4.0 V5 50% accuracy over 10+ predictions: same fraction, different objects |
| AM-10 | No aggregate pass mark for operator ramp; #44 not built |

### 14.2 Gaps and missing documents
- LTSF Master Tracker V1.1 not attached; column reconciliation owed at next build.
- No vacancy clause for the LTSF Owner.
- I-5, I-7, I-8 cite Ledger rows not procedure numbers (counterparties at later versions); I-6, I-10, I-13 cite procedures read directly in SOP-32 v2.0 and SOP-12 v2.1.
- SOP-25 not attached.
- Conflict **C6** closed by this version.

### 14.3 Version review triggers (Section 10)
1. Any LTSF Master version increment (fires most often). 2. Any LTSF rate card change (Section 3) incl. bracket boundary. 3. Any LTSF tracker spec change (Section 11.1). 4. Any v4.0 increment (re-validate Section 5 mapping; re-read 1.5.1 vs T8). 5. Any Cross-Reference Ledger version rewriting row 27 or counterparty rows. 6. Any re-issue of PPC Authority Matrix.

### 14.4 Companions referenced
LTSF Master Decision and Operations System v2.1; Criteria System v4.0; KDR Template v3.0; PPC Strategic Doctrine v1.0; PPC Economics Worked-Example Set v1.0 case E7; SOP-32 v2.0 P12; SOP-12 v2.1; SOP-26 v2.0; SOP-29, SOP-33, SOP-37, SOP-38, SOP-28; Master PPC Data Architecture v1.0 and PPC Command Workbook template; PPC Authority Matrix v2.0; PPC Cross-Reference Ledger row 27; Hanging Closet Organizer Full Liquidation Action Plan v1.0; SOP Build Kit v1.0; Transition Brief v1.2.

### 14.5 Live-defense questions (Section 11.5, abbreviated)
Q1 liquidation bid above contribution not a subsidy (R2, LTSF 4.2); Q2 lane closure correct outcome (R3, P14, WE-2); Q3 sunk COGS excluded (R7, LTSF Principle 2); Q4 no discovery on C (1.3.1, F7); Q5 break-even scaling legal (F1, M1, LTSF 6.2; guard = floor price); Q6 code red does not cut lane (1.5.1, WE-4); Q7 CRITICAL->RED quarantine stays (R5, F12); Q8 deal window can open closed lane (R2, P11 step 4); Q9 disagreeing with floor -> route five numbers (1.2, P14); Q10 check line on quiet week (R6, V1); Q11 G6 GREEN on 624 aged units is correct (G6); Q12 missing number -> amendment item (V3, Authority Matrix).
