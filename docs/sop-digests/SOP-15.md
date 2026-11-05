# SOP-15 Digest: Auto Campaign Operations and the D5 Four-Way Split

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-15: Auto Campaign Operations and the D5 Four-Way Split |
| Type | PPC Department Operating SOP, Component #15 of the Operations Definition Register |
| Version | 2.0 |
| Date | 2026-08-05 |
| Owner | PPC Lead |
| Supersedes | SOP-15 v1.0 (2026-07-24) in full |
| Threshold policy | Thresholds live in Master PPC Decision Criteria System v4.0 only; zero local thresholds. Rebuilt to SOP Build Kit v1.0 twelve-element standard |
| Length | 16 pages; 12 procedures, 25-verdict mapping, 4 worked examples, 11 failure modes, 14 interface contracts, Appendix A (AM-1 to AM-5) |

**Verdict/purpose.** An auto campaign is **four different products sharing one wrapper**, and a blended auto produces one ACOS that hides four different decisions. Autos carry the **5-10% match-type spend destination** of the M6 structure targets (v4.0 S10 M6) and **100% of the account's auto-side discovery flow**: every close-match harvest candidate, every substitutes conquest signal, and the only standing indexing-health read the account owns. Governs: D5 conversion of blended autos into the four-group structure, phase-staged deployment on new products, the weekly per-group pass with keyword and ASIN routes, per-group bid/budget/verdict execution, group-evidence hygiene, trawler-and-probe two-tier pattern, per-variation autos, indexing-health read, event autos, and automation-interface upkeep keeping platform rules off protected auto scope. Absorbs the scheduled D5 spec deliverable (Completion Directive row closes against this document).

## 2. Scope & Boundaries

### The four targeting groups (Section 1.1)
D5 split = structural form of the four-group read in v4.0 S3 Family **F11** "Waste & Negation": each group judged separately on cost per discovered converter, waste %, graduation rate (also the Discovery objective-metric contract of rule **O6**). Per Strategic Doctrine v1.0 S4 "Auto Campaigns: Four Products in One Wrapper":

| Group | What it buys | Role | Bid posture |
|---|---|---|---|
| Close match | Queries closely matching listing's indexed content | Cleanest harvest source; indexing-health signal (P5) | Highest |
| Substitutes | Competitor detail pages | Conquest-lite; feeds S-C1 target lists (S8.7) via P3.3 | Second |
| Loose match | Semantically adjacent queries | Widest drift exposure; tightest waste control | Third |
| Complements | Adjacent-purchase pages | Basket demand, inbound advertisers; often event-only | Lowest |

v4.0 S8.9 scenario **S-H3** orders the split read before any judgment; D5 makes S-H3 permanent.

### Legitimate multi-auto structures (Section 1.2, Doctrine S4)
Exactly four legal:
1. **Four-way split** — one campaign per targeting group per product, each with own bid, budget, negation list, verdict (P1, P2).
2. **Trawler and probe two-tier price discovery** — low-bid wide harvester + dated higher-bid validator on same group; shared negation lists mandatory at standup (P4; SOP-29 P4.1).
3. **Per-variation autos** where variation demand diverges, each pointed at D2-mapped variation (P10).
4. **Dated event autos**, budget-capped, opened only inside a G12-armed window and closed with it (P6).

Illegitimate fifth: a second blended auto created because the first "stopped working" (diagnosis skip; autos degrade from negation neglect and bid drift; cloning resets data without fixing either). Any live auto matching none of four = F1.

### Boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 | Decides every threshold, band, scenario, stage condition, verdict; missing numbers are Appendix A items |
| #30 Harvest and graduation | Decides graduation. SOP-15 delivers candidate rows with evidence lines and group tokens (Route A); never issues GRADUATE FROM DISCOVERY |
| #29 Negation architecture | Owns doctrine, pre-load tables, wall standards, shared-list management, wall audit. SOP-15 detects and routes auto-side negation needs (Routes B, C, D) and applies #29 sets same session |
| #16 PAT and conquest | Owns target opens, flag tests, rotation, exits. SOP-15 routes converting substitutes ASINs to #16 (P3.3) and ingests #16's failed-target list as negative-ASIN input |
| #12 Exact operations | ADD EXACT + RESTRUCTURE receipts from head-term check execute at SOP-12 P1/P2; source group contributes steering wall after standup |
| SOP-14 Broad | Owns weekly three-route triage definition (SOP-14 P3); SOP-15 executes it on autos and adds two ASIN routes |
| #37 Automation rules | Owns rule register, reconciliation, change control. Every **ScaleInsights** rule touching autos routes there; SOP-15 maintains auto-side campaign states for #37 exclusion lists (P11) |
| #38 Bulk mechanics | Pull, staging, upload, T+1 |
| #32 Deal and event windows | Event plans, ramps, caps, reconciliation; P6 event autos only under armed plan |
| #22 Launch-stage PPC | Deployment sequence on new products; stage-skipping from launch routes back to #22 (F6) |
| #31 Budget and envelope | Envelope law in instruments (T0, T1, Account Rollup A2) per conflict C3; CAP SYNTAX deltas from T1 |
| #34 Canada annex | Owns Canada delta; everything here applies in CA unless #34 overrides |
| Also | #28 (placement), #17-19 (SBV), #41 (economics refresh), BM owner (indexing findings) |

## 3. Triggers

Lags use v4.0 gate-response cadence terms and the Monday cascade (Data Architecture v1.0 S12 "Data Flow: Feed -> Columns -> Cadence").

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| D5 conversion due | T3 Campaign Board live SP Auto row with "Auto Group Split (D5)" = blended; D5 program row open in Definition Register run ledger | Same week found | P1 |
| Phase transition | T0 zone E stage read + v4.0 stage conditions clearing (S11 rule T2) | Next Monday pass | P2 |
| Weekly cadence | Monday cascade reaches auto rows of T2/T3; search-term data in Raw Pull Pack (Monday 06:00) | Same day (Monday) | P3, then P7, P8, P12 |
| Two-tier test opened | T2 K9 verdict naming capped test on starved group (CONTINUE TEST TO 50 CLICKS AT CAPPED BID or FUND TEST (UNFUNDED PRIMARY)) | Same day as funding release | P4 |
| Listing rewrite or monthly slot | T5 Product Log listing-change entry; otherwise V4 monthly cadence slot (S14) | Next weekly pass after log entry | P5 |
| Event window armed | G12 armed by #32 plan; dates in T2 K2 Event Mode | Per event plan ramp date | P6 |
| Group evidence requested downstream | #30's Monday harvest pass opens; SOP-30 S3 requires group-level auto evidence post-D5 | Same Monday pass | P9 |
| Structure state change | Any P1/P2/P4/P6 standup, close, pause; #38 staged set | Same day | P11 |
| Verification return | #38 T+1 report: landed-value mismatch or unattributed change on auto row | Same day | F10 via P11; redeploy per #38 |

## 4. Procedures

### Preconditions (Section 3) — T7 Manifest (Data Architecture S9)

| T7 row | Requirement / observable |
|---|---|
| **D5 Auto four-group split** | STR carries Targeting values close-match, loose-match, substitutes, complements; T3 "Auto Group Split (D5)" resolves per campaign. Observable: T7 D5 Status = PRESENT. MISSING/STALE -> group-level verdicts suppressed for window (not approximated from blend); suppression written into pass record |
| A2 Deployment state | Current bulk state (state, budget, default bid); T3 C2 cells populated with current pull date |
| A3 Pacing and in-budget | T3 C3 "In-Budget Bucket" resolved; G3 evaluable |
| A6 Objective + Expected CPC | Every auto Objective = Discovery (or event tag under P6); UNTAGGED routes to assignment per O2 (S6 rule O1). T3 C1 Objective Tag populated, zero UNTAGGED |
| A7 Eligibility | Advertised SKU eligible; flip halts execution same day (G4). T3 C2 Eligibility = Live |
| B5 Coverage counts | T2 K8 "# Auto" per term and per-group registry current |
| B8 Economics chain | T0 named cells live (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC); G9 PROVISIONAL on ceiling bids while margin blended/stale. T0 zone C shows margin-table version and fresh G9 state |
| D2 Variation map | T3 C1 "Targeted Variation + Band" resolved; unmapped rows carry D2-pending flag and bar P10 |
| ASIN-row identification | Search-term rows split keyword queries vs ASIN matches (Customer Search Term is an ASIN string); pass worksheet carries two-way split with row counts |
| Own-catalog ASIN list + #16 target-status list | Both current (version dates inside trailing week) for Route D |

**Gates in force:** G1 quarantines impossible rows (flags only). **G2**: bid reads >= 15 clicks (7d), CVR verdicts >= 100 clicks, CTR verdicts >= 1,000 impressions, with **60-day fallback** and EXTEND-class handling for thin rows; WoW swings > 50% on thin samples = noise; twin sets pool evidence. **G3**: rates TRUNCATED below **70% in-budget**, budget lever first on close and substitutes; loose and complements rows with T3 capped-by-design note graded on O6 discovery metrics at their cap (Discovery utilization target is **70%+, not 100%**, per v4.0 S3 F10 and KDR v3.0 "Utilization targets"; exemption class = AM-4). G6 inventory bands govern advertised SKUs. G9 ceiling reads PROVISIONAL after price change. G10 excludes event windows from trend verdicts. G12 freezes non-plan structure changes inside armed windows **and** requires every analyzed term in current MKL.

### P1. D5 conversion: blended auto to four groups — 60-90 min per product + parallel-window watch
1. **Inventory:** T3 filter Type = SP Auto, read "Auto Group Split (D5)": list every blended row with **trailing 60-day spend, sales, both negative lists (keyword and ASIN)** from SP bulk sheets in Raw Pull Pack. Convert by trailing spend, largest first.
2. **Create four campaigns**, one targeting group enabled each, group token in KW/Root/Auto naming position (SOP-12 v2.0 Appendix A): **Auto-Close, Auto-Sub, Auto-Loose, Auto-Comp**. Objective = Discovery; down-only bidding with capped test bids (Doctrine S2 control-gradient Discovery row). In bulk file the four rows differ only in which **Product Targeting Expression** is enabled (close-match, substitutes, loose-match, complements), other three paused.
3. **Seed bids** by group ordering (close > substitutes > loose > complements): from blended auto's own group-level CPC history where split report provides it, else verdict's Expected CPC reference (T0 named cell). No invented bid; no evidence seed = incomplete (AM-3).
4. **Split budget** by trailing group spend share. Loose and complements get **capped-by-design note** in T3 at creation (Budget Verdict cell records cap as decision) — exempts from FIX BUDGET (TRUNCATED).
5. **Migrate negatives, then pre-load fresh:** keyword negatives -> Auto-Close and Auto-Loose; ASIN negatives -> Auto-Sub and Auto-Comp. Apply SOP-29 P1 pre-load table same session: broad keyword set to close and loose; failed-PAT-target ASINs to substitutes; **own-catalog ASINs to complements** (self-cannibalization wall) and NOT to close or loose. Without pre-load = SOP-29 F1 and F3 exposure here.
6. **Parallel window:** four split campaigns run beside legacy blended auto at capped budgets; at window end legacy pauses as PAUSED-PENDING (REASON + RE-ENTRY), reason = D5 split, re-entry = none. Duration/pause day = AM-2 (operating value recorded in product's T6 conversion entry).
7. **Watch daily:** combined spend vs pre-split baseline, legacy state. Legacy spending past recorded pause day = F5, pause immediately.
8. **Registry and log:** T2 K8 "# Auto" updates per term; four T3 rows with tokens; one T6 entry with decomposition prediction (blend's single ACOS decomposes into four group reads, each with own verdict at first post-split cycle). P11 same day.

### P2. Phase-staged deployment on new products — 20-30 min per standup
1. Four groups never deploy simultaneously. Staging per v4.0 deployment sequence and stage conditions (S11 rule **T2**, Launch/Scale graduation criteria, Phase 1-4 model): **close match at Phase 2 entry** with broad; **substitutes at Phase 3 entry** (scale stage) under organic-share and review conditions; **loose and complements late and rarely**: capped, often event-only, only where close and substitutes sit at band.
2. Each standup runs P1 steps 2-5 for its group; T6 entry names authorizing stage condition (else no deploy).
3. Skipping a stage requires a verdict; all groups at once = unpriced-risk pattern (Doctrine S2); group live without condition = F6.

### P3. Weekly pass: SOP-14 P3 machinery + auto routes — 25-40 min per product
1. Enter after T0 and T1; score last cycle's due T6 rows (V1).
2. **Pull and split:** Raw Pull Pack SP Search Term Report filtered to product's auto campaigns, **trailing 60 days with 7-day and 30-day columns visible**. Split keyword vs ASIN rows. Confirm group token from Targeting column; unresolvable -> P9 quarantine.
3. **Keyword routes per SOP-14 P3:** Route A converters at/above graduation bar -> #30 with evidence (clicks, orders, window, source campaign with group token, CPC); decision #30's vs S8.9 **S-H1** (discovery term reaching **3 or more orders** graduates) and price-class validation rules. Route B proven waste: WAS limits **40% discovery, 10% elsewhere (S-H2)** -> negative exact with evidence, executed to SOP-29 P3 standards incl. converting-term guard. Route C drift clusters: negative phrase on cluster root.
4. **Route D, ASIN routes:**
   - **P3.3 substitutes converters:** converting ASINs in Auto-Sub -> #16 as PAT target candidates with evidence (clicks, orders, our price vs theirs where competitor depth feed carries it; else line notes coverage gap). #16 decides; feeds S-C1.
   - **P3.4 negative-ASIN:** own-catalog ASINs in complements or loose served terms -> negative-ASIN same pass (F3 wall); ASINs on #16 failed-target list -> negative-ASIN in Auto-Sub. Standards SOP-29 P3.
5. **Head-term check:** priority term served by auto, T2 child rows "Spend Share of KW %": **auto or broad > 40%** of priority term's clicks with no live exact -> ADD EXACT + RESTRUCTURE before any performance verdict (S4 **X10**, S8.4 **S-R12**). Receipt to SOP-12 same day; steering wall after standup per SOP-29 P2.
6. **Off-taxonomy converters:** below relevancy bar/outside taxonomy -> **S-H6** MKL classification first (G12); expand with logged tag and test plan, or negate.
7. Stage, deploy, verify, log: #38 rows with verdict + scenario ID; Tuesday deploy after BM huddle; T+1; T6 line per change. Route counts **A/B/C/D per group** feed P12.

**Routing decision tree (any served-term row)**
```
Group token resolved? no -> P9 quarantine
+-- ASIN row?
|   +-- In Auto-Sub and converting ........ Route D1: evidence line -> #16 (P3.3)
|   +-- Own-catalog ASIN (Comp/Loose) ..... Route D2: negative-ASIN this pass (F3 wall)
|   +-- On #16 failed-target list ......... Route D2: negative-ASIN in Auto-Sub
|   +-- Otherwise ......................... hold; grade inside group's O6 read
+-- Keyword row?
    +-- Orders at/above S-H1 bar .......... Route A: candidate row + token -> #30
    +-- Converting, off-taxonomy .......... S-H6: MKL decision first (G12)
    +-- Zero-sale past S-H7 line .......... Route B: CUT / NEGATE (relevant primary instead -> 50-click capped test)
    +-- WAS breach, proven waste .......... Route B: negative exact + evidence line
    +-- Wrong-intent cluster .............. Route C: negative phrase on root
    +-- Priority term, auto share >40% .... X10/S-R12: ADD EXACT + RESTRUCTURE -> #12
    +-- Otherwise ......................... stays; G2 sufficiency governs
```

### P4. Trawler and probe — 30 min standup, 10 min per weekly read
1. Standup only via verdict opening test on named group. **Trawler**: low-bid, wide, harvest-focused, held at **L2 floor $0.50** (S9 rule L2) or group's evidence-carried low seed. **Probe**: dated, higher-bid, runs to click quota at verdict's capped bid (usual carrier: CONTINUE TEST TO 50 CLICKS AT CAPPED BID; the 50-click capped test is the **S-H7** relevant-primary route). Must carry different bids.
2. Shared negation lists mandatory at standup (SOP-29 P4.1), recorded in T3.
3. At quota: probe CPC and CVR vs **Max Profitable CPC = margin $ x CVR** (S3 F1) and Expected CPC. Viable discovered CPC re-seeds standing group bid via L2-compliant steps (**no single change > 50%, $0.50 floor**); failed probe closes STOP-LOSS: CONCEDE OR DEFER. Either way probe parks PAUSED-PENDING with test outcome as reason.
4. T6 chain one row per event (standup, quota reached, re-seed or stop-loss) each with prediction.

### P5. Indexing-health read — 20 min per product per monthly slot
1. On V4 monthly slot or next pass after a T5-logged listing rewrite: export Auto-Close served-term distribution (**top terms by impressions, trailing 30 days**), compare against family's intended syntax map in **T1 (S1 identity columns and taxonomy tags)**.
2. Material divergence (bar = AM-5; qualitative with evidence until v4.1) = indexing/listing-content finding, not bid problem -> BM owner via cross-framework handoff with served-term evidence. Bids never fix indexing (G5 logic).
3. Files as T6 product-level entry either way; clean read recorded, not skipped.

### P6. Event autos — 20 min per window
1. Dated, budget-capped, opened only inside G12-armed window, **expiry in campaign name**; sized per #32 plan (event sizing S10 rule **M9**); closed with window. Event rates never enter trend verdicts (G10).
2. Never converts to standing silently: requires verdict, fresh Objective tag, P1-style pre-load check. Live past expiry = F11.

### P7. Per-group bid and verdict execution — 10-15 min
1. Every change staged as #38 row (prior, new, reason with verdict + scenario ID). Console edit found = F10.
2. L2 at execution: **traffic-unlock steps 15-25%** where clicks under G2 bid-read bar; **changes capped at 50% per step**; **$0.50 floor**; **ladder steps ~10% per week**; **placement-exit mechanic $0.05-0.10 below a placement's blended CPC** where a placement read exists. Step exceeding L2 fails staging QA.
3. Lever order L1: budget first where G3 failing on close or substitutes, then bid, placement, negation, structure, status; pause last after documented exhaustion. v1.0 auto lever-order variant parked as AM-1.
4. One lever per row per cycle unless verdict names two; opposite trends never share an execution.

### P8. Group budget and cap mechanics — 10 min
1. FIX BUDGET (TRUNCATED) applies to Auto-Close and Auto-Sub: below 70% in-budget, budget lever first and rates marked TRUNCATED (G3). Auto-Loose and Auto-Comp with capped-by-design note graded at caps on O6 (AM-4).
2. CAP SYNTAX receipts from T1 (instrument layer, C3): auto budgets in breaching family reduce **with broad, loose and complements first, close and substitutes last**; delta staged per #38 with T1 reference.
3. **S-H5:** group whose cost per discovered converter > **2x account norm** for the group steps budget down **25%**; loose and complements usual offenders; close and substitutes retain priority. One #38 row with S-H5 in reason string.
4. Recovery Mode overlay: discovery budgets floor at **sentinel levels**, autos stay on small (S11 rule **R3**); sentinel state set by product verdict and recorded in T3; P8 never scales a sentinel row.

### P9. Group-evidence hygiene — 5-10 min
1. Post-D5 every auto-sourced evidence leaving this SOP carries its **group token**: candidate rows to #30 (SOP-30 S3 gate requires group-level auto evidence, never blended), ASIN handoffs to #16, negation evidence to #29. Token = campaign name group segment + report's Targeting value; must agree.
2. Unresolvable token (report gap, renamed campaign, legacy blend still serving) -> quarantine: routes nowhere; T7 manifest note records gap; re-enters when resolved. Forwarding blended evidence = F7.
3. Term with evidence in two groups: one candidate row listing both sources and both tokens (SOP-30 P1 dedupe rule), so walls land in every source.

### P10. Per-variation autos — 25 min per standup
1. Legal only where variation demand diverges (size- or color-specific intent, Doctrine S4 case 3) and D2 resolves variation with ranked backup. Advertised SKU = D2-mapped variation; variation in name; inherits group token structure (refinement of a group, never replacement for D5).
2. Standup via P1 steps 2-5; T6 names divergence evidence (CVR-by-variation or demand split). G6 per variation; RE-POINT VARIATION on RED per D2 backup same day (SOP-12 P10 mechanics).
3. No divergence evidence in T6 = F1-class; consolidates back.

### P11. Automation-interface upkeep — 10 min per structure event and weekly
1. Every ScaleInsights rule touching autos inventoried and change-controlled in #37 (register Section 2 classes A-D); SOP-15 never edits a rule. SOP-15 owns the state feed: at every P1 parallel-window open/close, P4 probe standup/close, P6 event-auto open/close, any manual-hold or sentinel state, affected campaign names go to #37 exclusion-list maintenance same day (SOP-37 P3).
2. Read #38 T+1 attribution report every cycle for auto rows: rule-fired change on parallel-window, capped-by-design, probe or event row = F10 here, F2 in #37; change claimed by neither session nor rule escalates as unlogged edit.
3. Weekly audit outranks inter-cycle automation on shared target: audit value wins, automation resumes from it (S12 rule **P3**).

### P12. Pass close and per-group yield reporting — 10-15 min
1. Per group write to T3: **cost per discovered converter, WAS %, Harvest Yield (converting terms found), Graduations (Qtr), "Auto Group Split (D5)" state** — the O6 metrics that grade the group (not group ACOS alone).
2. Route counts close the pass: Route A to #30 (with tokens), Route B/C to #29 standards, Route D handoffs to #16 and negative-ASIN counts, head-term receipts to #12. Missing any count = incomplete.
3. Group at **zero graduations across the quarter** -> S-H5/S-H7 reads; loose/complements -> retirement question under P8 cap logic; retirement is a verdict (PAUSED-PENDING), never drift.

## 5. Rules, Thresholds & Numbers

| Item | Value | Source |
|---|---|---|
| Auto share of match-type spend (M6) | 5-10% | v4.0 S10 M6 |
| Auto-side discovery flow | 100% (all close-match harvest, substitutes conquest, indexing read) | Verdict |
| Groups | 4 (close, substitutes, loose, complements) | F11, Doctrine S4 |
| Bid ordering | close > substitutes > loose > complements | Doctrine S4 |
| Legal multi-auto structures | 4 | Doctrine S4 |
| G2 bid read | >= 15 clicks (7d) | G2 |
| G2 CVR verdict | >= 100 clicks | G2 |
| G2 CTR verdict | >= 1,000 impressions | G2 |
| G2 fallback | 60-day; EXTEND-class handling; WoW > 50% on thin samples = noise; twin sets pool | G2 |
| G3 truncation | < 70% in-budget -> TRUNCATED; budget lever first (close, sub) | G3 |
| Discovery utilization target | 70%+ (not 100%) | F10; KDR "Utilization targets" |
| S-H1 graduation | discovery term reaching 3 or more orders | S8.9 |
| S-H2 WAS limits | 40% discovery; 10% elsewhere | S8.9 |
| X10 auto dominance | auto or broad > 40% of priority term's clicks with no live exact | S4 |
| S-H5 | cost per discovered converter > 2x account norm -> budget -25% | S8.9 |
| S-H7 | zero-sale past S-H7 line -> CUT / NEGATE; relevant primary -> 50-click capped test | S8.9 |
| L2 floor | $0.50 | S9 L2 |
| L2 per-change cap | 50% | S9 L2 |
| L2 unlock steps | 15-25% where clicks under G2 bid-read bar | S9 L2 |
| L2 ladder steps | ~10% per week | S9 L2 |
| L2 placement exit | $0.05-0.10 below placement's blended CPC | S9 L2 |
| Max Profitable CPC | margin dollars x CVR | F1 |
| Discovery Max-ACOS band | 15-30% (KDR "Objective Max-ACOS bands") | WE-1 |
| D5 inventory window | trailing 60-day spend, sales | P1 |
| P3 STR window | trailing 60 days with 7-day and 30-day columns | P3 |
| P5 indexing window | top terms by impressions trailing 30 days | P5 |
| Phase staging | close at Phase 2 entry (with broad); substitutes at Phase 3 entry; loose/complements late, capped, often event-only | T2 |
| v1.0 parallel window (operating value in T6 only) | 7-day window, legacy pause day 8 | AM-2 |
| Zero graduations | across quarter -> S-H5/S-H7 reads, retirement question | P12 |
| Data timing | Monday 06:00 landing; refresh by 09:00 | I-1 |
| Procedure times | P1 60-90; P2 20-30; P3 25-40; P4 30 + 10/wk; P5 20/month; P6 20; P7 10-15; P8 10; P9 5-10; P10 25; P11 10; P12 10-15 min (planning estimates, not thresholds) | Section 4 |

### v4.0 rule IDs referenced

| ID | Meaning as described |
|---|---|
| M6 | Structure targets (auto 5-10%) |
| M9 | Event sizing mathematics |
| F1 | Product Economics (Max Profitable CPC) |
| F10 | Budget & Pacing (discovery utilization 70%+) |
| F11 | Waste & Negation (four-group read) |
| O1 | Objective tagging; UNTAGGED |
| O2 | Assignment of untagged |
| O6 | Discovery objective-metric contract (cost per discovered converter, waste %, graduation rate) |
| S-H1 | 3+ orders graduates |
| S-H2 | WAS limits 40% discovery / 10% elsewhere |
| S-H3 | Split read before any judgment (made permanent by D5) |
| S-H5 | 2x norm -> -25% budget |
| S-H6 | Off-taxonomy converter -> MKL decision |
| S-H7 | Zero-sale line; relevant primary -> 50-click capped test |
| S-C1 | Conquest target lists (fed by P3.3) |
| S-R12 | Priority term with zero exact -> ADD EXACT + RESTRUCTURE |
| X10 | Auto/broad > 40% priority term clicks |
| L1 | Lever order |
| L2 | Step sizes, caps, floor, unlock, ladder, placement exit |
| L5 | Lever rule (negation) referenced in skill logic |
| T2 | Deployment sequence, stage conditions, Launch/Scale criteria, Phase 1-4 |
| R3 | Recovery Mode sentinel discovery floors |
| P3 | Audit value wins over automation |
| P10 | Unlogged change does not deploy at any tier |
| V1 | Unscored actions do not accumulate |
| V4 | Monthly cadence slot |
| G1, G2, G3, G4, G5, G6, G8, G9, G10, G12 | Quarantine; sufficiency; truncation; eligibility; indexing logic; inventory; packet completeness; PROVISIONAL margin/price; event exclusion; event freeze + MKL presence |

### Verdict-to-execution mapping (autos)

| Verdict | Auto execution |
|---|---|
| QUARANTINE: DATA REFRESH | No changes (G1); P9 holds downstream routing |
| UNLOCK TRAFFIC | L2 unlock on named group (close/substitutes in practice); no rate judgment until G2 |
| FIX BUDGET (TRUNCATED) | P8.1 on Auto-Close and Auto-Sub only; capped loose/comp exempt |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | P4 probe (or in-group capped test) to quota; budget assurance only |
| FUND TEST (UNFUNDED PRIMARY) | P2 staged standup or P4 probe; stage condition in T6 |
| RANK PUSH: FUND SIZED PUSH | Never on auto; receipt to SOP-12; steering wall after standup |
| RECOVERY PUSH | Exact-side at SOP-12; auto history = evidence only |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Exact-side; wall choking needed source -> #29 P7 removal control |
| FIX CONVERSION FIRST; DEFER PUSH | No auto scale on term; group holds cap; fix to D8-named owner |
| PLACEMENT FIX FIRST | Rare; bids hold; #28 |
| RE-POINT VARIATION | P10.2 same day per D2 backup; baseline reset in T6 |
| TAPER | Exact-side; confirm steering wall still stands (no removal on taper) |
| HOLD; DEFEND LIGHTLY AT RANK | No auto change |
| DEFEND AT FLOOR | Auto-Comp and trawler rows at floor: no change; drift restores in one step |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Bid toward ceiling per L2; syntax-cap half via P8.2 |
| INCREMENTALITY LADDER | Not an auto instrument; branded term in auto = wall gap to #29 |
| ADD EXACT + RESTRUCTURE | P3.5 receipt to SOP-12 same day; note names carrying group |
| CONSOLIDATE DUPLICATES | Illegitimate clone or evidence-free per-variation auto consolidates; SOP-12 P7 precedence with group token as role test |
| GRADUATE FROM DISCOVERY | Steering negative in source group(s) same day per SOP-29 P2; T3 Graduations (Qtr) increments |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | P1.5 pre-loads; P3 Routes B/C/D; steering at graduation; negative-ASIN = auto-specific surface |
| ENTER SBV ARBITRAGE | No auto execution |
| OPEN / ROTATE / EXIT CONQUEST | #16 decides; EXIT echo: failed targets -> negative-ASIN in Auto-Sub |
| STOP-LOSS: CONCEDE OR DEFER | P4 probe close or P6 event close; freed budget to envelope |
| PAUSED-PENDING (REASON + RE-ENTRY) | P1.6 legacy pause; P4 probe park; P6 close; P12.3 retirements |
| LEAVE TO HARVEST | Term stays in source group at capped bid; re-enters via #30 pool re-eval date |

## 6. Data Inputs Required

**Amazon reports / files**
- **Sponsored Products Search Term Report** (Raw Pull Pack): filtered to auto campaigns; trailing 60 days with 7-day and 30-day columns; **Targeting** column tokens (close-match, loose-match, substitutes, complements); Customer Search Term (keyword vs ASIN string); clicks, orders, spend, CPC; impressions (P5 top terms by impressions trailing 30d).
- **SP bulk sheets** (Raw Pull Pack): auto campaigns, Product Targeting Expression rows, state, budget, default bid, keyword and ASIN negative lists; trailing 60-day spend and sales per blended auto.
- **#38 T+1 verification / attribution report** (incl. ScaleInsights change log).

**Command Workbook**
- **T0**: zone C named cells (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC) with margin-table version and G9 state; zone E stage read; zone I action summary (consumer).
- **T1**: family syntax map, S1 identity columns, taxonomy tags; cap enforcement / CAP SYNTAX deltas.
- **T2**: K2 Event Mode; K8 "# Auto" per term, per-group registry, "# Exact"; K9 verdicts; campaign child rows "Spend Share of KW %".
- **T3 Campaign Board**: Type = SP Auto; "Auto Group Split (D5)"; C1 Objective Tag, "Targeted Variation + Band"; C2 deployment cells, Eligibility; C3 "In-Budget Bucket"; Budget Verdict cell (capped-by-design); cost per discovered converter; WAS %; Harvest Yield; Graduations (Qtr); shared-list attachments; sentinel state.
- **T5 Product Log**: listing-change entries; platform notes.
- **T6 Decision Log**: predictions; D5 conversion entry (parallel-window operating value); probe chains.
- **T7 Manifest**: rows D5, A2, A3, A6, A7, B5, B8, D2.

**Other**
- **Own-catalog ASIN list** (current within trailing week).
- **#16 target-status list and failed-target register extract**.
- **Competitor depth feed** (price position; not yet landed — evidence lines note coverage gap).
- SOP-29 P1 pre-load table; P4.1 shared lists.
- D2 variation map (Economics & Context Pack) with ranked backups.
- #32 event plan (dates, caps).
- #41 economics refresh.
- MKL (syntax tags, relevancy).
- Definition Register run ledger (D5 program row).
- Account norm for cost per discovered converter per group (S-H5 comparison).
- Economics Worked-Example Set (ramp).

## 7. Outputs / Artifacts

| Event | Artifacts | Consumers |
|---|---|---|
| Weekly pass (P3, P7, P8, P12) | Per-group verdict rows in T2/T3; staged #38 set with verdict + scenario IDs; deployed set with T+1; route-count artifact (A/B/C/D, head-term receipts); token-carrying candidate rows; P3.3 handoff list; reactive negation sets with evidence; per-group yield reads in T3; T6 entries with prediction and review date. Storage: Command Workbook (T2, T3, T6) and #38 staging store; T6 append-only, never purged | #30, #16, #29, #38, V5, T0 zone I |
| D5 conversion (P1) | Conversion record: inventory line, four T3 rows with tokens and capped-by-design notes, migrated and fresh pre-load lists, parallel-window watch lines, legacy pause entry, T6 decomposition prediction. **Gate artifact = first post-split cycle showing four distinct group verdicts** | #29, #37, Definition Register run ledger |
| Standups/closes (P2, P4, P6, P10) | T3 rows created/parked with reasons and re-entry; T6 citing stage condition/test verdict/window; shared-list attachments; P11 notices | #37, #32, weekly pass |
| Indexing-health (P5) | Served-term distribution extract, divergence read vs T1 syntax map, handoff packet to BM owner; clean logs as clean. T6 product-level entry | BM owner |
| Interface upkeep (P11) | Exclusion-state notices (campaign names, dates); T+1 attribution review note; F10 escalation packets | #37 |

**Alarm routing:** F3, F5, F10 same day to operator queue; F2, F4, F7, F11 weekly worklist; F1, F6, F8, F9 to PPC Lead with T6 history.

### Failure modes

| ID | Failure | Detection | Response | Incident |
|---|---|---|---|---|
| F1 | Second auto cloned because first "stopped working" | New blended auto, no group token, no driving verdict; T3 diff | Pause clone; diagnose (negation neglect/bid drift); consolidate | v1.0 S7 diagnosis-skip; Doctrine S4 |
| F2 | Blended read after split exists | Verdict citing whole-auto ACOS with group rows available | Re-issue per group; blend is reporting only | Account's pre-D5 state |
| F3 | Own-ASIN cannibalization | Own-catalog ASINs in comp/loose served terms (P3.4) | Negative-ASIN same pass; #29 audit adds campaign | Account paid to serve its own pages |
| F4 | Loose drift explosion | Root-containing share of Auto-Loose collapses after relevance shift | Route C aggressive; verify cap; T5 note | 2024-2026 semantic widening (Doctrine S3.3) |
| F5 | Legacy auto never paused post-split | Spending past recorded pause day | Pause immediately; reconcile double-coverage spend | Double coverage bought same queries twice |
| F6 | Stage-skipping deployment | Sub/loose/comp live without cited stage condition | Pause to correct stage; route to #22 if launch-originated | Doctrine S2 unpriced risk |
| F7 | Token-less evidence forwarded | P9 finds row lacking token, or SOP-30 F3 gate returns it | Quarantine, re-pull by campaign, re-route | New; WE-3 |
| F8 | Substitutes converters never handed to #16 | Converting Auto-Sub ASINs with no P3.3 row; #16 queue idle | Hand off same pass; repeat = SOP-16 S7 sourcing-gap escalation | New |
| F9 | Auto carrying head term unrouted | Auto > 40% of priority term clicks, # Exact = 0, no receipt | P3.5 receipt immediately; pass reopens | Account's named failure class: head terms carried by auto with zero exacts (v4.0 S1, S16 Worked Pass 3, six-piece pattern) |
| F10 | Automation firing on protected auto scope | T+1 attribution shows rule-fired changes on parallel-window/capped/probe/event rows | P11 sync same day; damage review; #37 F2; audit value wins | Stale-scope runaway (SOP-37 S6: ladders running on funded-loss campaigns) |
| F11 | Event auto silently standing | Window-named campaign live past expiry with no conversion verdict | Close per #32; convert only via verdict, tag, pre-load | New |

Escalation: F1, F5 on first recurrence; F3 recurring via #29 audit; F6 to launch handoff owner; F7 recurring to PPC Lead; F9 on first occurrence; F10 on push/event/terminal-adjacent scope same day per SOP-37.

## 8. Decision Rights

| Authority Matrix v2.0 row | Coding |
|---|---|
| **D5 conversions + auto operations** | D and E: incoming operator; R: PPC Lead |
| Weekly verdicts (established US) | E under operator's assigned scope; BM owner R at daily huddle |
| Bulk deployments (#38) | E own scope |
| Automation rules (#37) | D: PPC Lead; E and R: incoming operator; rule changes never made here, P11 notices only |
| Event plans (#32) | E |

- **Human-mandatory:** every P1 conversion decision, every P2 staged standup, P4 probe standups and closes, P6 event-auto opens, P10 per-variation standups, group retirements, every deployment confirm.
- **AI-executable with audit:** full P3 drafting per group, ASIN route lists, decomposition tables, token hygiene checks, S-H5 computations, F-mode detection, T6 drafting.
- Vacancy (Matrix S2 rule 5): D -> PPC Lead, E -> PPC Manager. Checkpoint holder: PPC Lead.
- #30 decides graduation; #16 decides conquest; BM owner owns indexing/listing fixes; D8-named owner for conversion fixes; instrument layer owns envelope/caps.
- Ramp: Week 1 shadow pass, locate artifacts, reproduce WE-1 decomposition to the cent. Week 2 supervised P3 on one product; one P4 probe standup and one P11 notice drafted; pass bar zero forwarded rows without tokens. Week 4 own scope incl. one live P1 conversion or P2 standup; two clean audit weeks close ramp. Eight live-defense questions.

## 9. Account-Specific Facts

- Account pre-D5 state: blended autos ("one ACOS hiding four decisions"); D5 program row open in Definition Register run ledger; D5 program completing across portfolio retires P1 into standing detection sweep.
- Automation platform: **ScaleInsights** (rules touching autos).
- Account's named failure class: head terms carried entirely by auto with zero exacts (six-piece pattern, v4.0 S16 Worked Pass 3).
- v1.0 operating value: 7-day parallel window, legacy pause day 8.
- Competitor depth feed not yet landed.
- Worked examples (fictional base; Tier 3 live spine not attached): AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3%.
  - **WE-1 decomposition:** blend $210.00 spend, 7 orders, $560.00 sales, ACOS 37.5%. Close $92/100 clicks/5 orders/$400 (ACOS 23.0%, CPC $0.92, CVR 5.0%, MPC $1.40, 0.66x SAFE, CPDC $30.67 = 1.28x norm $24.00). Sub $58/40/1/$80 (72.5%). Loose $47/50/1/$80 (58.75%, CPC $0.94 vs ceiling $0.56 = 1.68x; CPDC $47.00 = 1.96x norm). Comp $13/20/0.
  - **WE-2:** Route A "bamboo sheets split king" Auto-Close 12 clicks 3 orders CPC $1.05; Route B "silk pillowcase" 24 clicks 0 orders $21.60; Route C six "curtain" terms 31 clicks 0 orders; Route D Auto-Sub ASIN 9 clicks 1 order, our $80.00 vs their $86.40 (8.0% above); head term "bamboo sheets king" 68 clicks, Auto-Close 31 = 45.6% > 40%, # Exact = 0.
  - **WE-3:** "queen sheets deep pocket" blended 16 clicks 3 orders; split Close 7 clicks 2 orders, Loose 9 clicks 1 order (neither meets S-H1). Auto-Comp CPDC $61.00 vs $24.00 = 2.54x -> budget $12.00 -> $9.00/day.
  - **WE-4:** Auto-Loose trawler $0.50; probe $0.90; day 11: 50 clicks, $45.00, 3 orders, $240 sales, CVR 6.0%, ACOS 18.75%; MPC $1.68; 0.54x ceiling; Expected CPC reference $1.10; re-seed $0.50 -> $0.75 (+50%) -> $0.90 (+20%).

## 10. Open Items

| ID | Item |
|---|---|
| AM-1 | Auto lever-order variant from v1.0 (bids before placements before budget, pause last) diverges from L1; parked per Ledger row #15; L1 governs |
| AM-2 | D5 parallel-window duration and legacy-pause day (v1.0: 7 days, pause day 8; recorded only in T6) |
| AM-3 | Per-group bid seed references (v4.0 has Expected CPC per keyword, none per auto group) |
| AM-4 | Capped-by-design exemption class for G3 (marker: T3 Budget Verdict cell) |
| AM-5 | Indexing-health divergence bar (P5 qualitative until v4.1) |

- **Conflicts:** Ledger C3 (#31 no procedural doc; instruments T0, T1, Account Rollup A2).
- **Observed text issues:** SOP-15 uses "G12" for both event freeze and MKL presence (consistent with C9 dual meaning registered in SOP-14). Recovery sentinel cited as R3 here (SOP-06 cites R3 as tightened human-review lines).
- **Not present / pending:** competitor depth feed; Tier 3 live economics spine; v4.1 items above.
- Review triggers: monthly; any v4.0 increment (re-validate S-H, O6, F10, F11, G2, G3, G12, L2, X10 references); D5 program completion; Amazon change to auto targeting groups or STR Targeting tokens (breaks P9); #37 register change on auto-relevant rule classes; competitor depth feed landing; any v4.1 resolution of Appendix A.
