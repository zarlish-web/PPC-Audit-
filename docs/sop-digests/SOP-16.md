# SOP-16 Digest: PAT and Conquest Operations

Source: `PPC_SOP_16_PAT_and_Conquest_Operations_v2_0.pdf` (15 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-16: PAT and Conquest Operations (Component #16 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-05 |
| Owner | PPC Lead |
| Supersedes | SOP-16 v1.0 (2026-07-24) in full; absorbs the scheduled PAT/conquest playbook deliverable |
| Thresholds | Live in the Master PPC Decision Criteria System v4.0 only. This SOP has zero local thresholds; a threshold appearing here instead of v4.0 is a defect |

**Verdict / purpose.** "Conquest opens on evidence, never on ambition." A target earns spend only when it passes v4.0 Section 8.7 row **S-C1** (we win at least 2 of price / rating / review count, or competitor flagged OOS). It is graded per target against the CPA ceiling (v4.0 Section 3 family **F1**: ceiling = margin $) inside the Conquesting metric contract (Section 6 rule **O6**: CPA vs ceiling, win-probability inputs, ACOS 10-15). It exits when the flag basis reverses (**S-C3**) or the ceiling fails for 2 consecutive validated weeks (**S-C2**). The rule carried from v1.0 unchanged: **blended conquest ACOS is never a decision input**. v2.0 expanded from 7 to 12 procedures, from a 6-row to a full scenario-wired verdict mapping, from 1 to 4 worked examples, and from 6 to 11 failure modes. It also tightened the open test: v1.0 opened on any single active weakness flag; v2.0 opens only on S-C1. The two v1.0 flag classes S-C1 does not admit ("off-deal while we run one"; conversion evidence alone) become queue-priority signals and go to the v4.1 amendment list.

The SOP covers the whole life of product-targeting spend: **offense** (conquest against competitor ASINs and refined categories) and **defense** (self-targeting on own pages, complements, virtual-bundle listings). That means intake from 3 sources, flag profiles and F12 classification, the open test and mechanics, the weekly per-target read and its decision tree, rotation, exit and the failed-target register, category-refined standing conquest, the defense PAT standing set, counter-conquest evaluation, reporting, and the event-window overlay.

### Two structure classes of PAT spend (Section 1.1)
| Class | Contents | Legal read |
|---|---|---|
| Class 1: per-target conquest | ASIN-targeted campaigns grouped by flag class; every offensive open and every counter-conquest response | Every target is its own decision row; blended number is for reporting only |
| Class 2: refined-class conquest + defense set | Category campaigns with refinements (price floor above ours, rating ceiling below ours) that enforce the S-C1 axes continuously; plus the standing self-targeting defense set | The category refinement is the **one legal blend** in conquest (P7 keeps the refinements true). Defense is graded on its own product: page occupancy for own-ASIN defense, basket lift for complements/VBs. Never on conquest economics or ACOS optics |

## 2. Scope and boundaries

**Owns:** all PAT spend (offense and defense). See the list above.

**Does not own / seams:**

| Adjacent component | Seam |
|---|---|
| Criteria System v4.0 | Decides every verdict, threshold, band, scenario and limit: 8.7 rows S-C1 to S-C6, Section 3 F12 (BEATABLE/WINDOW), F1 (CPA ceiling), Section 6 O2/O6/O7, Section 5 gates, Section 9 levers, Section 13 vocabulary. This SOP executes only |
| SOP-15 Auto operations | Owns the substitutes auto that scouts candidates. SOP-15 P3.3 routes converting substitute ASINs here with evidence lines ("SOP-15 routes, this SOP decides"). Failed targets go back to SOP-15's substitutes surface only as SOP-29 negative-ASIN entries |
| SOP-29 Negation architecture | Owns walls, negative-ASIN mechanics, shared lists, the wall audit. This SOP hands failed-target register entries to SOP-29 the same week as every exit (SOP-29 Section 3 names "the failed-PAT-target list from #16" as a required input; SOP-29 P1 pre-loads it into every substitutes creation) |
| SOP-26 Mature/defend + code red | Owns incursion detection (P4) and defense-stage posture, including the annual defense-cost read (P2). SOP-26 P4 routes persistent incursors here for P10 counter-conquest; this SOP returns the evaluation record. Defense PAT mechanics live here (Ledger row #26) |
| SOP-17/18/19 playbook | Owns SD contextual execution. Its P7.2 runs this SOP's flag workflow unchanged and restates zero flag rules; target list, flags, open/rotate/exit calls come from this SOP |
| SOP-30 Harvest | Owns keyword graduation. Keyword converters go to #30; ASIN converters come here via SOP-15 P3.3 |
| #33 Sibling arbitration | Owns family term ownership. Conquest targets are ASINs, so **G11** rarely binds; where a defense-set decision touches a family-owned surface, check the declared owner first |
| #32 Deal and event window | Owns event plans, ramps, caps, reconciliation. This SOP executes S-C5 / S-E3 stand-downs inside armed windows and freezes non-plan structure per G12 |
| #38 Bulk mechanics | Owns staging format, upload, T+1 verification. Every change exists first as a staged set per #38 |
| #37 Automation rules | Owns the rule register. Any automation touching PAT bids is inventoried there; a rule change touching conquest triggers a re-check of this SOP's Section 5 mapping |
| Strategic Doctrine v1.0 | Section 9 states the conquest doctrine ("conquest is opened on evidence, not ambition") and the defense-PAT and substitutes-scout roles |

## 3. Triggers

| Trigger | Detecting artifact | Procedure | Max lag |
|---|---|---|---|
| Candidate arrival | SOP-15 P3.3 PAT candidate handoff list (weekly pass outputs); competitor tracker adding an ASIN (T2 col DR "Competitor Depth (D8)"); P7 category scan | P1 intake, then P2 flag profile | Same weekly pass; profile complete before the next Monday cascade opens |
| Flag change on an open target | Daily reversal watch over T2 DR source fields (price, rating, review count, stock, deal state) on every open target | P4 read for that target | Same day the feed shows it; disposition staged same day |
| Weekly cadence | Monday cascade reaches conquest rows: T3 filtered to Type = PAT plus per-target rows from the targeting join | P4 full per-target reads; P11 reporting | Inside the Monday cascade; deploy Tuesday per #38 |
| Competitor deal window live | Deal-state field in flag profile / T2 DR; T5 "Competitor entry" event rows | P4 branch 2 (S-C5 stand-down) | Same day; during armed events, daily event cadence per G7 |
| WINDOW review date | 2-week review date written at every OOS-class open per S-C1 | P4 dated re-review | On the dated day; a lapsed date is failure mode F4 |
| Incursion escalation | SOP-26 P4 routes a persistent incursor with its response record | P10 counter-conquest evaluation | Same weekly cycle as escalation |
| Our reprice lands | T5 "Price move" event row on the product | P7 refinement refresh | Same week as the price move |
| Quarterly refresh date | v4.0 Section 14 rule V4 quarterly slot on cadence calendar | P7 refresh; P8 defense floor re-check with the #28 ladder | Inside the quarterly window |
| VB status check result | Weekly virtual-bundle knocked-out check from catalog owner | P9 pause or resume | Same week as the check |
| Event window arms | G12 arms on a confirmed deal window touching the product (#32 plan) | P12 event overlay | Same day the window arms |

Lags are given in corpus cadence vocabulary (same day / same pass / same week) where no number exists. A clock-hour SLA for the reversal watch is amendment A-5.

## 3b. Preconditions and gates (Section 3)
A failing gate suppresses its dependent execution class, and the pass records what it could not see (gate **G8**).

| Gate (T7 manifest ID) | Requirement / observable |
|---|---|
| Competitor depth current (T7 row "D8 Competitor depth (price/rating/deal/OOS)") | Flag-profile source fields present with source + date per flag. Observable: T7 Status cell for D8, plus per-flag date stamps. **T7 template ships D8 as MISSING**, blocked classes "Conquest open/rotate/exit; defend-context reads". While MISSING, opens are suppressed to flags per G8. PARTIAL: a decision on partial flags with coverage noted is legal; a decision on stale flags is not. No OPEN deploys on a flag dated before the current read window. Feed = Ledger external dependency **D4**. A numeric flag-age bar is A-4 |
| Per-target rows readable (T7 row "A8 PAT rows first-class") | Targeting join delivers per-target clicks, spend, orders for every open target. **Template ships A8 PARTIAL** ("row-level PAT reads thin"). Rows the join cannot deliver read as flags, never as approximations from the campaign blend (mirrors SOP-15 Section 3's suppress-not-approximate rule) |
| Economics chain live (T7 row "B8 Row economics (BE chain)") | T0 named cells live: AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC. Observable: T2 col **CO "CPA Ceiling $"** and **CM "Expected CPC $"** populated. **G9 PROVISIONAL** tag carries onto any ceiling-referencing open while margin is blended or stale (per SOP-12 v2.0 Section 3). G9 gate-ID dual use is an open amendment item from the #41 build |
| Sample sufficiency (G2) | "Bid reads need ≥15 clicks (7d); CVR verdicts ≥100 clicks... Below threshold, fall back to the 60-day window; if still thin, the verdict is EXTEND TEST, never a rate judgment." Observable: T2 col **V "Clicks 7/30/60d"**, **W "Sample State"**. S-C2's "validated weeks" = weeks that pass G2 |
| Inventory adequacy (G6) and variation (D2) | Advertised SKU on every conquest/defense campaign is the D2-preferred variation; T2 col **AD "Inventory Band"** must read GREEN for any open or scale (v4.0 8.3 row **S-I1**; RED blocks per G6). Observable: T3 col **H "Targeted Variation + Band"** |
| Eligibility (G4) | Advertised SKU eligible. Observable: T3 col **O "Eligibility + Reason"**. A flip halts all execution for the target the same day |
| Event mode (G12) | T2 col **AI "Event Mode"** clear, or the #32 event plan names the change. S-C5/S-E3 stand-downs are always live inside windows |
| Prediction and horizon (P10, O7, V1) | Every OPEN carries its per-target prediction (metric, direction, magnitude, horizon, review date per V1) and O7 horizon date before deploy. Observable: T6 row exists with review date. Missing = no deploy (P10); failure mode F7 |
| Do-not-target exclusion list current | Standing brand-safety and policy exclusion list checked before any open. Observable: profile carries an exclusion-check line. Owner/criteria = A-6 |

## 4. Procedures

### P1. Candidate intake and queue maintenance (20-30 min, weekly pass)
1. Open the conquest candidate queue (standing register block beside T3 in the product Command Workbook; one row per candidate ASIN). Columns: Candidate ASIN, Brand, Source (SUBSTITUTES / TRACKER / CATEGORY-SCAN), Evidence line, Date added, Profile state (PENDING / BUILT), Queue rank, Exclusion-check result.
2. Source 1, substitutes converters: SOP-15 P3.3 handoff list. Each comes with an evidence line (clicks, orders, our price vs theirs where the feed has it). They are "conquest-lite validated" and go to the top of the queue, but still need the P3 open test (S-C1 says target lists "feed from the auto substitutes group and Keepa signals" while entry = win test).
3. Source 2, competitor tracker: tracked set per family from T2 col DR "Competitor Depth (D8)" and the Keepa pull rows of the Raw Pull Pack. Add untracked ones with source TRACKER.
4. Source 3, category scans: Ads Console > SP campaign creation > product-targeting step > product's leaf category > suggested-products list filtered to the product's price and rating window. Record top sellers in the window that are not already queued, with source CATEGORY-SCAN. This refreshes with every P7 refresh.
5. Run the exclusion check on every new candidate. Failures are marked EXCLUDED with a reason and never profiled.
6. De-duplicate against the failed-target register (P6). A register ASIN re-enters only under the re-open rule (new flag class), and the queue row names the new class.
7. Ranking: substitutes converters first, then tracker candidates already reading BEATABLE, then category-scan entries. Ties go to the larger evidence line. Zero passable candidates while conquest budget sits idle = sourcing gap, escalate F8. Never lower the S-C1 bar.

### P2. Flag-profile construction and F12 classification (5-8 min/candidate)
1. One profile per PENDING candidate. Each flag carries source and date: their price vs ours + delta %; their rating vs ours; review count vs ours + gap; stock state (IN / LOW / OOS); deal state (ON / OFF); conversion evidence (clicks/orders from the substitutes evidence line); coverage note (fields the feed could not fill).
2. Classify per F12: "we win a comparison on ≥2 of price / rating / reviews = BEATABLE; competitor OOS = WINDOW (time-boxed)." Write the class and the axes won. Fewer than 2 of 3 and no OOS = **NOT-ENTERABLE** (stays as a watch row).
3. D8 PARTIAL: classify on the fields present, with coverage noted. D8 MISSING: the profile is a flag only, not an entry basis.
4. Deal state ON at profile time does not block classification. It blocks the open until the window ends (S-C5).
5. Profile state becomes BUILT. The profile is the gate artifact for any open.

### P3. Open test and OPEN mechanics (15-25 min/open)
1. Test: S-C1 only. Anything else is ambition (F2). A WINDOW open writes its 2-week review date at open.
2. Gates: all of Section 3 (D8 currency with per-flag dates inside the read window; G6 GREEN on the D2-preferred variation; G4; G12; economics chain with G9 state; exclusion check).
3. Structure: conquest campaigns grouped by flag class per product, one ad group per class (**BEATABLE-PRICE-LED, BEATABLE-RATING-LED, WINDOW**). Never one campaign per ASIN, never a mixed-class ad group. Name per v4.0 Section 4.2 with objective segment **Conquest**. Naming non-compliance is the SOP-12 F6 pattern, and renames ride alone.
4. Objective: rule **O2** "Competitor ASIN target → Conquesting." T3 objective tag and campaign-name segment are set in the same staged set.
5. Targeting: exact ASIN targeting. Expanded (their variations) only where the profile shows the basis holds family-wide, with each variation's price/rating read carried. A flag proven on one child does not license the family.
6. Entry bid: seeded at Expected CPC (T2 CM; F9 "Expected CPC (what the position should cost)") within **L2** limits ("±50% per change, $0.50 floor"). v1.0's "category CPC reference" does not exist in v4.0 (A-1). The bid is never invented; a driving verdict that carries a bid governs.
7. Budget: the class campaign gets a capped daily budget from the product envelope per #31 instruments. It competes inside the envelope by **M5** ordering, never by escalation (v4.0 Section 12 rule **P2**).
8. Prediction: T6 row with "CPA at or under the ceiling (T2 CO) by review date, conditional on flag basis holding" plus the O7 horizon date. O7: "every Ranking and Conquesting objective carries a horizon date," and renewal requires "CPA within ceiling." No prediction, no deploy (P10; F7).
9. Deploy: stage per #38 with scenario ID **S-C1** in the reason string. Tuesday by default; same day when the driving signal is dated (a fresh-stockout WINDOW open does not wait). T+1 verification per #38.

### P4. Weekly per-target read (30-45 min for 8-15 open targets)
1. Pull per-target rows: SP targeting data joined to T2 campaign child rows (Data Architecture Section 6.1). Trailing 7d, with 30d and 60d behind it (G2 fallback). Per row: clicks, spend $, orders, sales $, CPA, current flag fields + dates.
2. Score last cycle first: V5-score every T6 conquest row with a review date this cycle (V1: unscored actions do not accumulate).
3. Verify gates per row before any metric read: G2 (col V), flag dates in the read window, G6 band, G12 flag. A failing gate executes its response and defers the verdict.
4. Re-run F12 on current flags for every open target (S-C3: "the leading indicator outranks the trailing one").
5. Walk the decision tree. Write the disposition, scenario ID and numbers into the read sheet, and stage per #38 with scenario IDs.
6. Compute the blended class line for reporting only, labeled **REPORTING-ONLY**. A verdict citing it = F1. The only legal class read is the P7 refined category campaign.

**P4 decision tree (per target, in order, first match wins):**

| # | Condition | Action |
|---|---|---|
| 0 | Row fails G1 validation or G2 sufficiency | No rate verdict. Quarantine flag or EXTEND TEST per gate text; budget assurance only |
| 1 | Entry basis gone: BEATABLE now wins <2 of 3, or WINDOW restocked, or 2-week review date arrives | Exit at this review regardless of CPA (S-C3, S-C1 time-box). Released spend goes to P5. Register reason FLAG-REVERSED or WINDOW-CLOSED |
| 2 | Target's deal state ON | Stand down on the target for the window, stage the resume date (S-C5). Not an exit; the target clock pauses |
| 3 | Basis holds, CPA ≤ ceiling (CO), ACOS inside O6 10-15 band | Continue. Scale steps legal (S-C1 "Enter/scale conquest within the 10-15% band") inside L2. If target-page CVR ≥ our detail-page CVR, **S-C4** also applies: scale within band and mine the target's page for the winning offer element; the insight goes to the listing team |
| 4 | Basis holds, CPA ≤ ceiling, ACOS above band | No scale. One L2 ladder step down toward the CPC that prices the band; re-read next cycle |
| 5 | Basis holds, CPA > ceiling, first validated week | Mark week 1 of the S-C2 clock; one L2 step down; no exit |
| 6 | Basis holds, CPA > ceiling, second consecutive validated week | EXIT per S-C2 ("Exit that target; keep the campaign; rotate the target list"). P6 register + SOP-29 handoff the same week |
| 7 | Refined category class row above band | P7 step 4 (S-C6): tighten the refinement one step. A class that cannot reach band after 2 refinement passes exits |

### P5. Rotation (10 min/event)
1. On any branch-1, branch-6 or S-C6 exit, quantify the released weekly spend (the exiting target's trailing 7-day spend).
2. Open the next queue candidate that passes S-C1, per P3, in the matching flag-class ad group. The released spend is its starting reference.
3. If none passes, the budget returns to the product envelope (#31) and the queue logs the F8 sourcing signal. The bar does not move.
4. Every rotation writes a T6 pair: the exit scored against its open prediction, plus the new open's prediction and horizon.

### P6. Exit and failed-target register (10-15 min/exit)
1. Register row: Target ASIN, Exit reason (**CEILING-S-C2 / FLAG-REVERSED-S-C3 / WINDOW-CLOSED-S-C1 / REFINEMENT-EXIT-S-C6**), Flag state at exit (axes + values), Weeks open, Total spend and orders, Date.
2. SOP-29 handoff the same week: CEILING exits are staged as negative-ASIN into the substitutes auto. SOP-29 P1 pre-loads "Failed-PAT-target ASINs (negative ASIN, from #16's list)". A missed handoff = F3.
3. FLAG-REVERSED and WINDOW-CLOSED exits do not stage a negative-ASIN (the page did not fail), and the target may re-enter when a basis returns.
4. Re-open rule: a CEILING-exited target re-opens only on a **new flag class** (failed price-led, can re-open on a rating collapse or OOS). The re-entry row names the new class and the register row it supersedes.

### P7. Category-refined standing conquest (25-40 min/refresh; weekly read inside P4)
1. One category campaign per product family. Refinements: price floor above our current price, rating ceiling below our current rating (the refinement is the flag test running continuously).
2. Band construction: price floor = **one cent above our live price** (T5-confirmed); rating ceiling = **one displayed step below our live rating**. Record both values, source reads and refresh date on the refinement band record.
3. Budget capped by design (T3 note set, SOP-15 precedent). Graded on class CPA vs ceiling and the O6 band (the single exception to the per-target rule).
4. Above-band: S-C6 "tighten the refinement set (price floor, rating floor) one step; a category campaign that cannot reach band after two refinement passes exits." The pass count lives on the band record.
5. Refresh triggers: quarterly V4 slot, plus always our own reprice the same week (T5 price-move event). Stale = F6.
6. Every refresh re-runs the P1 category scan, stages edits per #38, and logs a T6 prediction (class CPA vs ceiling and band by the next quarterly read).

### P8. Defense PAT: own-ASIN and complement self-targeting (15-20 min weekly; quarterly floor re-check rides #28 ladder)
1. Own-ASIN self-targeting at floor, permanent (cheapest defense, Doctrine Section 9). Floor bids = discovered floors from the #28 ladder, read per term from T4 Placement & Bid columns **"Discovered floor $"** and **"Ladder state (step # + date)"**. Drift above floor without a verdict resets to floor in one staged step (DEFEND AT FLOOR). Expansion trigger, v4.0 8.6 row **S-D2**: "Branded IS slipping, or competitor ads appearing on our detail pages → Restore one ladder step; open/expand PAT self-targeting to occupy our own pages; the syntax defense budget (**M8**) is the ceiling."
2. Complement self-targeting, capped: graded on the basket (units per order and AOV vs the pre-standup baseline), never ACOS optics (F5). Own-catalog negative-ASIN walls in the complements auto belong to SOP-29 P1.
3. The annual defense-cost read belongs to SOP-26 P2. This SOP supplies the defense spend rows.
4. Weekly: read for occupancy (competitor ads on our pages yes/no) and floor integrity. S-D2 expansion executes the week the trigger shows.

### P9. Virtual-bundle self-targeting (10-15 min weekly where VBs exist)
1. PAT on our VB listings targeting our own component listings. Each VB campaign is a T3 row (Type = PAT, Objective Tag = Defensive), and col **AP "Moves Received"** carries the pause/resume actions.
2. Grading: AOV and units-per-order lift vs the **pre-standup 4-week baseline**, never ACOS (VB conversions often land on component listings). No numeric bar in v4.0 (A-3).
3. Weekly knocked-out check from the catalog owner: a knocked-out VB pauses the same week as **PAUSED-PENDING**, reason **VB-KNOCKED-OUT**, re-entry **VB-RESTORED**. A missing check = unknown = not servable; pause pending the check (row I-6).
4. The baseline clock annotates knocked-out gaps, so lift reads never span a broken period.

### P10. Counter-conquest evaluation (20-30 min/escalation)
1. Input: a persistent incursor from SOP-26 P4 with its response record (incursion held above the defense ceiling).
2. Full P2 profile + F12 classification.
3. BEATABLE/WINDOW: open per P3 in the matching class group, escalation reference in the T6 row.
4. NOT-ENTERABLE: stay defensive and return the record to SOP-26 with the profile ("conquest against a competitor who wins the comparison is a donation"; F10).
5. Every evaluation is a written record: profile, class, decision, and where declined, the counterfactual that would flip it (rule **J5**).

### P11. Reporting, logging, cascade integration (15-20 min, Monday cascade)
1. Read T0 and T1 first. Product posture and family caps govern (Data Architecture Section 2 rule 1).
2. Weekly gate artifact = per-target read sheet: per open target clicks, spend, orders, CPA vs CO ceiling, flag fields with dates, F12 class, disposition, scenario ID; plus refined-class row, defense and VB rows, and the REPORTING-ONLY blend.
3. No scenario ID in the #38 reason string, no deploy.
4. T6 rows per deployed change with predictions and review dates. Material structure events (class campaign creation, category refresh, VB pause) also write T5 product-log entries.
5. BM owner's R = daily huddle (Authority Matrix Section 2): review, not veto; disagreements route up.

### P12. Event-window overlay (10 min at arm/disarm)
1. Arm on G12: the #32 plan's confirmed window flags every conquest row through the window plus the post-event guard.
2. Inside the window: competitor deal detection executes v4.0 8.12 row **S-E3**, which routes to **S-C5**. Detection rides the daily event cadence (**G7**).
3. Competitor stockouts in events remain legal WINDOW opens if the plan does not forbid the structure change. The 2-week review still applies; read windows are excluded from trend verdicts (**G10**).
4. Structure changes beyond plan-named actions freeze (G12). Stand-downs and reversal exits are never frozen.
5. Post-window: resume by staged resume dates; reconciliation belongs to #32.

## 5. Rules, thresholds and numbers

### Criteria System v4.0 references
| ID | Meaning as described |
|---|---|
| S-C1 | "Candidate ASIN where we win ≥2 of price / rating / review count, or competitor flagged OOS → Enter/scale conquest within the 10-15% band; competitor stockouts are time-boxed offensives (review in 2 weeks)." Target lists "feed from the auto substitutes group and Keepa signals" |
| S-C2 | "CPA above ceiling for 2 consecutive validated weeks on a target ASIN → Exit that target; keep the campaign; rotate the target list." |
| S-C3 | "Win-probability degrades mid-flight (competitor price cut or review surge flips the ≥2-of-3 test) → Exit at the next review, not at the CPA lag: the leading indicator outranks the trailing one." |
| S-C4 | "Conquest CVR on target pages ≥ our own detail-page CVR → Scale within band and mine the target's page for the offer element winning the comparison." |
| S-C5 | "Competitor deal window live (deal state flag) → Stand down on that target for the window; resume at window end." ("conquesting into a deal price is buying the worst comparison of the month") |
| S-C6 | "Category targeting with refinements running above band → Refine or exit: tighten the refinement set (price floor, rating floor) one step; a category campaign that cannot reach band after two refinement passes exits." |
| S-D2 (8.6) | Branded IS slipping or competitor ads on our detail pages → restore one ladder step; open/expand PAT self-targeting; syntax defense budget (M8) is the ceiling |
| S-E3 (8.12) | Competitor deal detection inside event windows; routes to S-C5 |
| S-I1 (8.3) | Inventory band GREEN required for open/scale; RED blocks per G6 |
| F1 (Sec 3) | "Sets the CPA ceiling (= margin $)" |
| F9 (Sec 3) | "Expected CPC (what the position should cost)" |
| F12 (Sec 3) | "we win a comparison on ≥2 of price / rating / reviews = BEATABLE; competitor OOS = WINDOW (time-boxed)" |
| O2 (Sec 6) | "Competitor ASIN target → Conquesting" |
| O6 (Sec 6) | "Conquesting: CPA vs ceiling, win-probability inputs, ACOS 10-15" |
| O7 (Sec 6) | "every Ranking and Conquesting objective carries a horizon date"; renewal at horizon requires "CPA within ceiling"; objectives do not persist by inertia |
| G1 | Validation; failure = quarantine flag (FLAG: DATA REPAIR) |
| G2 | "Bid reads need ≥15 clicks (7d); CVR verdicts ≥100 clicks... Below threshold, fall back to the 60-day window; if still thin, the verdict is EXTEND TEST, never a rate judgment." |
| G4 | Eligibility; a flip halts all execution same day |
| G6 | Inventory adequacy; RED blocks |
| G7 | Daily event cadence for deal detection when armed |
| G8 | Failing gate suppresses its dependent execution class; pass records what it could not see |
| G9 | PROVISIONAL tag while margin is blended/stale (gate-ID dual use is an open amendment item) |
| G10 | Event read windows excluded from trend verdicts |
| G11 | Sibling/family term ownership (rarely binds for ASIN targets) |
| G12 | Event mode freezes non-plan structure changes |
| L2 (Sec 9) | "±50% per change, $0.50 floor" |
| M5 | Envelope ordering that conquest budget competes within |
| M6 | Monthly structure review context (consumer of the refinement band record) |
| M8 | Syntax defense budget, the ceiling on S-D2 expansion |
| P2 (Sec 12) | Conquest competes inside the envelope, never by escalation |
| P10 | Record missing prediction/horizon does not deploy |
| V1 (Sec 14) | Prediction fields (metric, direction, magnitude, horizon, review date); unscored actions do not accumulate |
| V4 (Sec 14) | Quarterly refresh slot |
| V5 | Scoring of T6 rows |
| J5 | Declined decisions record the counterfactual that would flip them |
| J7 | Stale state written on every affected record |

### Numbers
| Item | Value |
|---|---|
| Conquest ACOS band | 10-15% (O6) |
| CPA ceiling | Contribution / margin $ per order (F1) |
| Win test | ≥2 of 3 axes (price, rating, review count) or competitor OOS |
| WINDOW review | 2 weeks from open |
| S-C2 exit | 2 consecutive validated weeks CPA > ceiling |
| S-C6 exit | Class still above band after 2 refinement passes |
| Bid change limit | ±50% per change, $0.50 floor (L2) |
| Sample: bid reads | ≥15 clicks (7d) |
| Sample: CVR verdicts | ≥100 clicks; fallback 60-day window |
| Read windows | Trailing 7d, plus 30d and 60d |
| Refinement price floor | Our live price + $0.01 |
| Refinement rating ceiling | One displayed step below our live rating |
| VB baseline | Pre-standup 4-week baseline |
| Procedure times | P1 20-30m; P2 5-8m/candidate; P3 15-25m; P4 30-45m (8-15 targets); P5 10m; P6 10-15m; P7 25-40m; P8 15-20m; P9 10-15m; P10 20-30m; P11 15-20m; P12 10m |
| Operator ramp | 1-2-4 week schedule; 2 consecutive clean audited weeks close the ramp |
| Authority Matrix re-issue window | 1 week |

### Worked-example fictional base (illustrative only; not account data)
AOV $80.00, contribution $28.00/order, BE ACOS 35.0%, Target ACOS 17.5%, Max Acceptable 26.3%; ceiling $28.00; band 10-15%.
- **WE-1:** T1 BEATABLE 3/3: 84 clicks, CPC $1.15, $96.60, 9 orders, CPA $10.73, ACOS 13.4% → continue (branch 3). T2 WINDOW restocked at review: $42.00, 4 orders, CPA $10.50, ACOS 13.1% → exit (branch 1), WINDOW-CLOSED, no negative. T3 2/3: 82 clicks, CPC $2.50, $205.00, 5 orders, CPA $41.00, ACOS 51.3%; prior week CPA $33.60 → EXIT S-C2, negative-ASIN. Blend: $343.60 / 18 orders = $19.09 CPA, 23.9% ACOS, which looks fine and is misleading (v1.0 case recorded a blended $26.90). Released $247.00/wk.
- **WE-2:** Stale flag (D8 PARTIAL, flag 9 days old, competitor restocked day 3). Week A $66.00 / 1 order (ACOS 82.5%); Week B $60.00 / 1 order (75.0%). $126.00 spend vs $56.00 contribution = net -$70.00. Scored WRONG-DIRECTION.
- **WE-3:** Reprice $80.00 → $72.00. Floor $80.01 → $72.01; rating ceiling 4.4 (ours 4.6). Read 1: 240 clicks, $0.95 CPC, $228.00, 12 orders, CPA $19.00, ACOS 26.4% → S-C6 pass 1, floor to $75.00. Read 2: 170 clicks, $0.70, $119.00, CPA $9.92, ACOS 13.8% → holds.
- **WE-4:** VB baseline 1.18 units/order, AOV $80.00 → 1.31 (+0.13), AOV $88.80 (+$8.80); 92 orders/wk. Row: $84.00/wk spend (70 clicks, $1.20), 4 attributed orders, $355.20, ACOS 23.6%. Basket lift $809.60/wk vs $84.00 = 9.6:1 gross. Week 5 knocked out → PAUSED-PENDING; weeks 5-6 annotated.

## 6. Data inputs required
- **SOP-15 P3.3 PAT candidate handoff list** (substitutes converters with evidence lines: clicks, orders, our price vs theirs).
- **Keepa competitor pull, Raw Pull Pack** → T2 column **DR "Competitor Depth (D8)"**: competitor price, rating, review count, stock state (IN/LOW/OOS), deal state (ON/OFF), each with source + date. Daily for open targets.
- **Ads Console category scan**: SP campaign creation product-targeting step, leaf category suggested-products list filtered to price/rating window.
- **Do-not-target exclusion list** (brand-safety and policy).
- **Conquest candidate queue** (register block beside T3).
- **Failed-target register** (block beside the queue).
- **T7 Manifest** rows: **D8** Competitor depth (price/rating/deal/OOS), **A8** PAT rows first-class, **B8** Row economics (BE chain), with Status cells and blocked-classes cells.
- **T0 named cells**: AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC (Finance / Economics Pack; weekly refresh, monthly true-up).
- **T1** (family caps; read before conquest rows).
- **T2 columns**: CO "CPA Ceiling $", CM "Expected CPC $", AD "Inventory Band", V "Clicks 7/30/60d", W "Sample State", AI "Event Mode", DR "Competitor Depth (D8)"; campaign child rows.
- **T3 columns**: D (objective tag), H "Targeted Variation + Band", O "Eligibility + Reason", AP "Moves Received", Type filter = PAT, note set (capped-by-design).
- **T4 Placement & Bid**: "Discovered floor $", "Ladder state (step # + date)" (from the #28 ladder).
- **T5 product log event rows**: "Price move", "Competitor entry", deal window.
- **T6 Decision Log**: prior predictions to V5-score; review dates.
- **Sponsored Products targeting data / targeting join** (per-target clicks, spend, orders, sales; trailing 7/30/60d) joined to T2 child rows (Data Architecture Section 6.1).
- **D2-preferred variation** mapping.
- **Weekly VB knocked-out status check** from the catalog owner (Brand Management).
- **Pre-standup 4-week baseline**: units per order, AOV (family level).
- **Own detail-page CVR** (for the S-C4 comparison).
- **SOP-26 P4 incursion escalation + response record**.
- **#32 event plan / armed-window declaration**.
- **Refinement band record** (price floor, rating ceiling, source reads, refresh date, S-C6 pass count).
- **#37 automation rule register** (rules touching PAT bids).
- **#38 T+1 verification report**.
- **Cadence calendar** (V4 quarterly slot).
- **KDR v3.0 "Bands & Verdicts Reference"** sheet (vocabulary).

## 7. Outputs and artifacts
| Artifact | Record / storage | Consumer |
|---|---|---|
| Candidate queue with flag profiles | Conquest queue block beside T3; one row per candidate (columns in P1); profiles with per-flag source + date | P3; SOP-17/18/19 P7.2; P10 |
| Open records | T6 rows: prediction, O7 horizon, review date, scenario ID S-C1 | V5 scoring; Verification scoreboard (Account Rollup A3) |
| Per-target read sheet | Weekly; one row per open target (clicks, spend, orders, CPA vs CO, flag fields+dates, F12 class, disposition, scenario ID) + class, defense, VB rows + REPORTING-ONLY blend; stored with cycle KDR snapshot | Monday cascade, BM huddle; P7.2; SOP-26 P2 |
| Rotation and exit packets | Staged #38 sets with scenario IDs; paired T6 rows | #38 deploy, T+1; V5 |
| Failed-target register | ASIN, exit reason code, flag state at exit, weeks open, spend and orders, date; never pruned | SOP-29 P1 pre-load and P3.4; P1 step 6; audits |
| Refinement band record | Price floor, rating ceiling, source reads, refresh date, S-C6 pass count; with the category campaign's T3 row | P7; monthly structure review (M6) |
| Defense and VB basket reads | Weekly occupancy, floor-integrity; VB units/order and AOV lift vs annotated baseline | SOP-26 P2; P9 |
| Counter-conquest evaluation records | Profile, F12 class, decision, counterfactual (J5) | SOP-26 P4 return; T6 |
| T5 product-log entries | Class campaign creation, category refresh, VB pause | Product log |
| F1-F11 alarms | Detection signal + evidence line + routing tier | F4, F9 same day to the operator queue; F1, F2, F6, F7, F11 to the weekly worklist; F3, F5, F8, F10 to the PPC Lead with T6 history |

Retention: a pending #39 fold-in. Until then, the register and read sheets are kept without pruning.

### Verdict mapping (Section 5; closed vocabulary)
| Verdict string (source) | Execution |
|---|---|
| "OPEN / ROTATE / EXIT CONQUEST" (KDR v3.0) | OPEN → P3 on S-C1; ROTATE → branch 1 + P5; EXIT → branch 6 (S-C2) + P6. S-C5, S-C1 scaling, S-C4, S-C6 ride the same record as campaign moves |
| "DEFEND AT FLOOR" (KDR v3.0; v4.0 13.1) | P8 standing state |
| "PAUSED-PENDING (REASON + RE-ENTRY)" (KDR v3.0) | P9 VB pause; any conquest pause with reason + re-entry |
| "NEGATE (PRE-LOAD / REACTIVE / STEERING)" (KDR v3.0) | Receipt side only: the P6 handoff; SOP-29 deploys |
| "EXTEND TEST" (v4.0 13.1) | Branch 0 below G2 |
| "FLAG: DATA REPAIR" (v4.0 13.1) | G1 quarantine or D8-MISSING; repair task with owner + date |

Retired v1.0 strings: "REFRESH REFINEMENTS", "DEFENSE STATES". Boundary: "ENTER SBV ARBITRAGE" belongs to SOP-17/18/19; "GRADUATE FROM DISCOVERY" to #30. SOP-12 does no exact-campaign execution on conquest rows "unless the verdict names a shared-term bid step."

### Failure modes
| Mode | Detection | Response |
|---|---|---|
| F1 Blended conquest read | Verdict/change citing whole-campaign/class ACOS outside the P7 class | Re-issue per target (WE-1) |
| F2 Unflagged open | Live target without S-C1 basis or with no profile | Exit or classify honestly |
| F3 Failed target re-bought | CEILING ASIN serving in the substitutes auto | Stage negative now; SOP-29 wall audit with session attribution |
| F4 Flag reversal unnoticed | Flag dates outside the read window; WINDOW past 2-week date | Expired time-boxes read as expired (WE-2: -$70.00) |
| F5 Defense graded on ACOS optics | VB/complement judged vs 10-15% band | Basket metrics govern (WE-4) |
| F6 Stale refinements | Band record unmoved after a T5 price move or past the quarterly slot | P7 refresh now |
| F7 Open without prediction/horizon | Deployed target without T6 row or O7 date | Write both, date horizon from open date, name session |
| F8 Sourcing starvation | Zero S-C1-passing candidates with idle budget for a cycle | Escalate as sourcing gap; never lower the bar |
| F9 Conquest into a deal window | Spend on a target with deal-state ON | Stand down same day (S-C5) |
| F10 Counter-conquest without basis | Open from SOP-26 escalation with NOT-ENTERABLE/missing record | Exit; write the record retroactively |
| F11 Class-blend leakage | Blend applied to per-target groups by analogy to P7 | Re-issue per target |

Escalation: F3 via the SOP-29 wall audit; F8 to the PPC Lead in the cycle found; the same mode twice in consecutive cycles on the same scope goes to the PPC Lead with T6 history.

### Interface contracts (I-1 to I-10)
| Row | Direction | Artifact / timing | Non-arrival consequence |
|---|---|---|---|
| I-1 | SOP-15 → here | P3.3 handoff list, weekly | Continue on tracker/category; starved queue → F8 |
| I-2 | Data Ops (Raw Pull Pack Keepa) → T2 DR | Competitor fields with dates; weekly pull, daily watch; T7 D8 | D8 MISSING: opens suppressed; WINDOW boxes still expire; no new opens |
| I-3 | SOP-26 P4 → here | Incursor escalation, same weekly cycle | No evaluation; defense continues; no self-originated offense |
| I-4 | Here → SOP-29 | Register entries for negative-ASIN, same week as CEILING exit | F3; SOP-29 monthly wall audit detects; register backfills |
| I-5 | Here → SOP-17/18/19 P7.2 | Target list, flag states, open/rotate/exit calls + read sheet | SD competitor contextual holds closed while D4 stands; own-page SD unaffected |
| I-6 | Catalog owner (Brand Mgmt) → P9 | Weekly VB check | Pause pending; annotate; resume on first passing check |
| I-7 | Finance / Economics Pack (T0) → CO/CM | Weekly refresh, monthly true-up; T7 B8 | G9 PROVISIONAL; ceiling-driven opens defer; existing targets hold; J7 |
| I-8 | Here → #38 | Staged sets; Tuesday, same day for dated signals; T+1 | Unverified = not live; reads void; redeploy same day; console edits → change control (SOP-12 F10) |
| I-9 | Here → Monday cascade/BM huddle | Read sheet + T6, weekly | Process finding; PPC Lead audits retroactively; V5 still runs |
| I-10 | #32 → P12 | Armed-window declaration at G12 arm | No structure changes beyond stand-downs/exits; S-C5/S-E3 still live |

## 8. Decision rights
- Authority Matrix row **"PAT/conquest opens and exits"**: Incoming operator **D** and **E**; PPC Lead **R**; BM owner **I** (Section 11 also references BM I/R seats at the huddle). Vacancy (standing rule 5): D reverts to the PPC Lead, E to the PPC Manager.
- **AI-executable with audit:** P1 queue maintenance/ranking, P2 profiles/classification, P4 read-sheet drafts and dispositions, F4 reversal/staleness detection, P6 register + SOP-29 handoff staging, P7 band drafts, P8-P9 occupancy/basket reads, P10 evaluation drafts.
- **Human-mandatory:** every OPEN (including WINDOW), every counter-conquest decision, every refinement band change, every pause, every deployment confirm.
- BM owner's R = daily huddle review, not veto; disagreements route up.
- PPC Lead: owner; receives F3/F5/F8/F10 and repeat-mode escalations; audits operator weeks.
- Listing team receives S-C4 offer-element insights; catalog owner supplies VB checks; Finance supplies T0.

## 9. Account-specific facts
- No live product economics spine is attached to this build. All worked examples use the standard fictional base (AOV $80.00 etc.); none are account data.
- Template/manifest state as shipped: T7 **D8 = MISSING** (blocked classes "Conquest open/rotate/exit; defend-context reads"); **A8 = PARTIAL** ("row-level PAT reads thin"). The competitor-depth feed is Ledger external dependency **D4**, not landed.
- SD competitor contextual (SOP-17/18/19) is held closed at structural depth while D4 stands.
- #44 operator certification due **2026-09-25** (per its Ledger row); #42 ad policy due **2026-08-17**.
- The v1.0 register recorded 6 failure patterns without dated incidents. No dates are invented.
- No product names, ASINs or account dollar figures appear in this SOP.

## 10. Open items
| ID | Item |
|---|---|
| A-1 | PAT entry-bid rule: v1.0 cited a "category CPC reference" that does not exist in v4.0; v2.0 seeds at Expected CPC (F9) within L2 |
| A-2 | Additional entry flag classes: "off-deal while we run one" and "proven conversion from their page" are not admitted by S-C1; v4.1 must add them if wanted |
| A-3 | VB basket-lift bar: no numeric threshold in v4.0 |
| A-4 | Flag-age limit: no numeric staleness window for competitor flags |
| A-5 | Reversal-watch SLA: clock-hour SLA owed (mirrors the Element 2 lag item from the #17/18/19 build) |
| A-6 | Do-not-target exclusion list: owner, criteria and change control owed, coupled to #42 ad policy (due 2026-08-17) |
| Existing register items referenced (not re-opened) | 18/25/26 closed-vocabulary count; stale v3.0 cover labels; G9 gate-ID dual use (#41 build) |
| C5 | Program conflict C5 resolution: Elements 11 and 12 added from primary sources |
| Ledger correction | ASIN-converter route is SOP-15 P3.3; the seed Ledger row attributed it to SOP-30 |
| Pending fold-ins | #39 retention policy; Ledger's pending exclusion-list fold-in for #16 (closed structurally) |
| Named documents not present | Criteria System v4.0; KDR Template v3.0; Strategic Doctrine v1.0; SOP-15, SOP-26, SOP-29, SOP-30, SOP-12; #28, #31, #32, #33, #37, #38, #39, #41, #42, #44; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0; Authority Matrix v2.0; Cross-Reference Ledger; Economics Worked-Example Set (cases E2, E4); Supersession Map |

Version triggers (Section 10): D4 feed lands (D8 → PRESENT); a new weakness class admitted to v4.0; SOP-17/18/19 SD contextual opens at structural depth on D4; Authority Matrix re-issue touching the row; VB program mechanics change; A-1 to A-6 land in v4.1. Review monthly and on any v4.0 increment.

Operator ramp live-defense questions (Section 11): 7 cold questions covering the passing-CPA-at-restock case, blend legality, the ceiling as $ not %, re-open on a new class, a 1-of-3 incursor, a competitor deal during our event (S-E3 then S-C5), and what may be done when D8 is MISSING.
