# SOP-14 Digest: Broad Campaign Operations

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-14: Broad Campaign Operations |
| Type | PPC Department Operating SOP, Component #14 of the Operations Definition Register |
| Version | 2.0 |
| Date | 2026-08-07 (built Wave 4, session s9 W4 #14; Ledger version 1.9 on returned row) |
| Owner | PPC Lead |
| Supersedes | SOP-14 v1.0 (2026-07-24) in full |
| Threshold policy | Thresholds live in Master PPC Decision Criteria System v4.0 only; zero local thresholds. Built to SOP Build Kit v1.0 twelve-element standard against SOP-12 v2.0 depth floor |
| Length | 17 pages; 13 procedures, 25-verdict mapping, 4 worked examples, 12 failure modes, 16 interface contracts, 6 amendment items |

**Verdict/purpose.** Broad is the **fenced discovery engine; the fence is the product, and the fence is built weekly or not at all**. A broad campaign is graded on **cost per discovered converter, WAS percentage and graduation rate, never on its own ACOS** (v4.0 S6 rule O6: judging a campaign on another objective's metrics is a process violation). Broad carries the **15-20% match-type spend destination** of the M6 structure targets (v4.0 S10 M6). The SOP governs the three broad surfaces: family discovery standup, modified-broad fence, weekly three-route triage, defensive brand broad, graduation yield accounting, negation-cadence audit, dated-test governance, CAP SYNTAX receipt, capped-by-design budget mechanics, event and recovery overlays, variation re-point, restructure-or-retire. **P3 is an account-wide shared definition** (run by SOP-13, SOP-15; SOP-29 executes against its outputs).

## 2. Scope & Boundaries

### The three broad surfaces (Section 1.1)

| Surface | Structure and posture | Why / exit |
|---|---|---|
| 1. Family discovery broad | One campaign per syntax family, Objective = Discovery, seeded with family root + validated modifier roots, budget-capped by design, never straddling families (v4.0 S12 rule P4). Bidding down-only (Doctrine v1.0 S6.3). Placement modifiers 0 on all three groups at creation | Pay algorithm to reveal demand MKL hasn't mapped (Doctrine S1 principle 1, Control Gradient). Exit: winners up through #30, losers sideways through negation; campaign exits only via P13 |
| 2. Modified broad | Same family campaign with required-word lock on drifting keyword (e.g. +bamboo +sheets). Unfenced version pauses in same change set. Bid carried from paused keyword | Middle rung when open broad drifts but phrase too narrow (Doctrine S3.3). Exit back to open broad when root-containment recovers, or up to phrase (SOP-13) |
| 3. Defensive brand broad | One campaign per brand, Objective = Defensive, broad on brand terms, floor bids at discovered floor. Every generic discovery campaign carries steering negatives on brand terms | Captures misspellings and word-order variants. Judged on branded impression share held and incrementality (O6 Defensive metric set). Permanent; ladder re-runs to re-discover floor |

Movement between surfaces = staged, logged structure event.

### P3 shared definition (Section 1.2)
SOP-13 v2.0 S1.3 runs it on phrase (adds stem-clustering and dedup). SOP-15 v2.0 P3 runs it on every auto group's keyword rows (adds two ASIN routes). SOP-29 v2.0 S1 owns standards Routes B and C execute against, never re-runs triage. **A change to P3 increments SOP-13, SOP-14, SOP-15, SOP-29 together.** Cite P3 by step number.

### Rulings and conflicts declared (Section 1.3)

| Item | Statement | Handling |
|---|---|---|
| Version note | Criteria System file cover/footers read v3.0 — known stale header on correct current file | Cited as v4.0 with printed headings; not a finding |
| **C9 gate numbering** | v4.0 S5: G9 = price stability, G10 = event exclusion, G12 = MKL hygiene. Corpus (SOP-14 v1.0 S3, SOP-12 v2.0 S3, SOP-30 S3, Data Architecture) uses G9 = margin freshness, G10 = objective tagging, G12 = event freeze | Named by v4.0 number with corpus alias; rides to v4.1 as SOP-29's AM-11 |
| **C10 verdict vocabulary** | v4.0 S13.1 = 18 strings; KDR v3.0 = 25; Data Architecture v1.0 S2 rule 8 = 26 | Quotes KDR 25 verbatim with cross-map on two divergent rows |
| **C12 scenario ID** | Data Architecture v1.0 S6.1 labels exact-live-with-source-unnegated filter S-H6; v4.0 S8.9 carries it as S-H4 | S-H4 = unsteered graduate; S-H6 only for off-taxonomy converter |
| **C3 component #31** | #31 has no procedural document; five documents cite it as if numbered | Names instrument and tab (T1 group S3, T0 zone H, M5 queue) |
| Naming citation | v1.0 P1 step 2 cites "4.2 convention"; no S4.2 in uploaded Criteria System; S17.2 keeps it in v1.0 Criteria System outside pack | References SOP-12 v2.0 Appendix A; AM-6 |

### Boundaries

| Adjacent | Seam |
|---|---|
| v4.0 (#8) | Decides every threshold/band/gate/scenario/verdict/lever limit |
| #30 Harvest and graduation | Decides graduation, pools evidence across sources, issues verdict. Route A delivers candidates; SOP-14 never validates/graduates |
| #29 Negation architecture | Owns doctrine, wall-level selection tree, pre-load standard, reactive execution standards, monthly wall audit. SOP-14 produces Routes B/C with evidence and owns weekly cadence read |
| #12 Exact | Every head term in broad -> ADD EXACT + RESTRUCTURE receipt at SOP-12 P1/P2; SOP-14 builds broad-side steering negative afterwards |
| #13 Phrase | Owns phrase surfaces, stem read, phrase-broad dedup wall decision. SOP-14 supplies P3 and takes dedup wall broad-side placement from #13 |
| #15 Auto, D5 split | Owns four-group auto structure and two ASIN routes; SOP-14 supplies keyword-route definition; never touches auto bids/budgets/verdicts |
| #28 Placement and bid-modifier | Owns ladder derivation, exit-bid, modifier sizing incl. brand-broad defense floor; SOP-14 deploys rows #28 stages |
| #16 PAT and conquest | Competitor-brand strings in Surface 3 served terms = incursion evidence routed to #16 |
| #33 Sibling arbitration | Sibling-owned root = pre-load negative, never seeded; G11 before scale |
| #32 Deal and event windows | Freeze broad structure in armed windows |
| #35 Incrementality | Surface 3 step-downs executed here; continue/restore call is #35's |
| #38 Bulk deployment | Every change staged in #38 format |
| #37 Automation rules | SOP-14 sends exclusion-state notices (dated tests, modified-broad parallel states, event freezes, sentinel floors); never edits a rule |
| Budget/envelope (instrument) | T1 group S3, T0 zone H, M5 queue; receive deltas only |

## 3. Triggers

Lag measured from artifact timestamp; starting later = failure mode.

| Trigger | Detecting artifact | Max lag | Procedure | Evidence it fired |
|---|---|---|---|---|
| Weekly cadence | Monday cascade reaches T2 KEYWORD COMMAND; T7 MANIFEST search-term join row shows current refresh date | Same session; deploy Tuesday | P3, P5, P7 | Route counts A/B/C per campaign in T6; yield in T3 "Harvest Yield" |
| New family standup | T1 SYNTAX BOARD row live, "Gap KWs" > 0, T2 K8 "# Broad" = 0 across family root | Next weekly verdict queue | P1 | T3 row with Objective Tag = Discovery, capped-by-design note, non-empty pre-load wall list |
| WAS breach on broad row | T3 "WAS %" above Discovery limit (S3 F11 "Waste & Negation") | Same weekly session | P3 Routes B and C | Staged negation rows with evidence lines; recomputed WAS |
| Root-containment drift | P2 step 1 read (this vs prior window on T3) | Modified-broad staged same session | P2 | Both window reads on T3 with delta in pp |
| Graduation approval returned | SOP-30 P1 graduation log row = APPROVE with this campaign in source list | Same day as standup; wall confirmation closes before session does | P6 | Negative list shows entry; term absent at next pull |
| Head-term detection | T2 campaign child rows "Spend Share of KW %" vs v4.0 S4 rule X10 with K8 "# Exact" | Receipt to #12 same day | P3 step 7 | Receipt in #12 queue; term's clicks/spend excluded from yield base |
| Dated-test expiry | T1 group S3 "Dated Test / Stop-Loss" expiry, or T2 K7 "Test Status" click quota filling | Verdict within 1 working day | P8 | Closed verdict string + scored T6 row |
| CAP SYNTAX receipt | T1 "Cap Status" = BREACH with staged delta | Same weekly session | P9 | Reduced broad budget at T+1; T1 share inside cap |
| Event window arms | T2 K2 "Event Mode" from #32 (v4.0 G10 event exclusion; corpus alias G12 event freeze) | Freeze effective day window arms | P11 | No structure event in window without event-plan reference |
| Recovery Mode entry | T0 zone A code-red flag, or product TACOS vs stage band per v4.0 S8.1 scenario S-A4 | Same day as entry log | P11 step 5 | Discovery budgets at sentinel; reduction total logged as expected weekly savings |
| Inventory band change | T2 K2 "Inventory Band" YELLOW or RED, D2 names ranked backup | Same day on RED; next pass on YELLOW | P12 | Advertised SKU matches D2 backup at T+1 |
| Yield failure | T3 "Harvest Yield" zero across governance window with spend active | Same weekly pass second zero lands | P13 | Written evaluation (seed refresh, negation audit, budget rebalance) before retirement |
| Sibling declaration change | #33 record / re-arbitration / stewardship grant in T2 K8 "Term Owner (Family)" | Same day | P1 step 6, P3 step 3 | Non-owner's broad has negative phrase on owned root |
| Verification return | #38 T+1 report mismatch | Redeploy same day | P10 step 5 | Delta verifies clean; week's reads void |

## 4. Procedures

### Preconditions (Section 3) — T7 MANIFEST
Missing/stale field group suppresses dependent execution class (G8).

| Manifest | Requirement | Observable |
|---|---|---|
| Search-term join (Raw Pull Pack) | SP + SB search term reports + STIS joined to T2 campaign child rows (Data Architecture S12). Absent feed **suppresses P3 entirely** (no degraded read, no yield) | T2 child rows carry per-term-per-campaign splits with non-zero "Spend Share of KW %"; T3 "WAS %" populated. No dedicated T7 row (AM-1) |
| A2 Deployment state | Current bulk state; stale fails freshness | T7 A2 = PRESENT; T3 State, Daily Budget $, Bid / AG Default $ from current-week pull |
| A3 Pacing buckets | In-budget % per campaign to distinguish capped-by-design from truncation | T3 "In-Budget Bucket" and "Truncation Flag (G3)" populated; capped-by-design note on capped rows |
| A5 Threshold flags | Precomputed band/flag columns (Data Architecture S2 rule 4) | T2 K5 flags: ACOS band, CTR-versus-market, CVR-versus-market, zero-quarantine |
| A6 Objective + Expected CPC | Every broad tagged Discovery or Defensive (v4.0 S6 O1; corpus alias G10) | T3 "Objective Tag" on 100% of broad rows. A6 PARTIAL: account reference Expected CPC rides provisional |
| B5 Coverage counts | Registry counts per match type | T2 K8 "# Exact", "# Phrase", "# Broad", "# Auto" for every served term |
| B8 Economics chain | T0 named cells AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC | T0 zone C fresh; G9 price-stability flag and corpus margin-freshness flag on ceiling actions |
| B9 WoW deltas | Prior-window figures for P2 and P7 | T2 K5 "WoW Block"; T3 holds prior yield and negation counts |
| D2 Variation map | Targeted variation + ranked backup | T2 K2 "Targeted Variation(s)" and "Inventory Band"; unmapped = D2-pending flag, preferred SKU |
| D7 Decision log | Prior-cycle due T6 rows available (V1) | Due rows carry V5 score before P3 step 1 completes |

**Gates in force**

| Gate (v4.0 / [corpus alias]) | Effect |
|---|---|
| G1 Validation quarantine | Flag + data-refresh task, never a route; term stays in source |
| G2 Sample sufficiency | Below v4.0 S5 read thresholds -> term stays in source under capped dated test |
| G3 Budget truncation | Budget lever before bid conclusion; deliberate discovery cap is not truncation (P10 step 1) |
| G6 Inventory adequacy | RED -> P12 same day; YELLOW freezes spend increases on family discovery at current level |
| G7 Envelope and pacing | Budgets reconcile to product envelope; breaching discovery rise refused at staging |
| G8 Packet completeness | Missing gate fields -> flag; enforces search-term suppression |
| G9 Price stability [margin freshness] | Price change in trailing window -> CVR and ACOS provisional; no conversion verdict on provisional read |
| G10 Event exclusion [objective tagging] | Event weeks + guard leave trend reads feeding P2/P7; corpus alias covers O1 (untagged broad unmanaged) |
| G11 Sibling conflict | Shared root with two products' discovery = portfolio decision; nothing scales until #33 |
| G12 MKL hygiene [event freeze] | Every analyzed term in current MKL with syntax tag and relevancy score; untagged -> MKL maintenance and taxonomy pre-negation. Alias covers armed-window freeze (P11) |

### P1. Create family discovery broad campaign — 35-50 min
1. Family qualifies: T1 SYNTAX BOARD row live, "Gap KWs" > 0, not in chronic CONVERSION diagnosis (S8.2 **S-Y5** freezes bids at maintenance across chronic conversion syntax).
2. Creation legal: T2 K8 "# Broad" across root + T3 registry. One broad per syntax family; extend if exists; second without declared split = F8.
3. Gates: G6 GREEN on D2-preferred; G12 (event) clear or plan names it; G12 MKL hygiene on every seed; G11 clear vs #33.
4. Name per SOP-12 v2.0 Appendix A, family root in keyword position, Objective = Discovery; must parse or T3 naming flag.
5. Stage per #38: portfolio = product's; bidding **down-only** (Doctrine S6.3); placement modifiers **0** on all three groups.
6. Daily budget from family's discovery allocation share in **T1 group S3** spend-governance columns; capped by design. Write **capped-by-design note** into T3 same session (stops G3 firing).
7. Seeds: family root in broad + validated modifier roots where family has proven structure. Never seed sibling-owned root (pre-load negative).
8. Pre-load negative set same session per #29. **Four classes:** (a) taxonomy-known irrelevant terms; (b) every already-graduated exact as negative exact; (c) all brand terms as steering negatives; (d) sibling-owned roots. Record in T3 "Negation State". Skipping = F10 and F12 root cause.
9. Advertised SKU = D2-preferred variation, never parent by default.
10. Registry: T2 K8 "# Broad" increments per seeded root; T3 row with Objective Tag, owner, capped-by-design note, wall list; T1 "MT Cov Broad %" picks it up.
11. T6: discovery prediction = expected validated terms routed per $100 of spend by first review date (V1). No prediction = no deploy.
12. Deploy via #38 Tuesday default; T+1.

### P2. Modified-broad deployment (fence step-up) — 20-30 min per keyword
1. Root-containment read = served terms containing family root / all served terms, %. Record this and prior window on T3 with delta in pp. **No v4.0 firing threshold (AM-2).** What fires: WAS above Discovery limit (F11), read after step 2 truncation check.
2. Lever order (S9 **L1**): budget > bid > placement > negation > structure. Read T3 "Truncation Flag (G3)" first; truncated -> budget lever, re-read next clean cycle. Modified broad is last rung.
3. Fence or list: waste concentrated in few enumerable terms -> Routes B/C, no fence. Waste distributed across many terms lacking required word -> fence.
4. Add modified version with required word locked (+bamboo +sheets). Bid carried from paused keyword; later steps obey L2.
5. Pause unfenced version in same change set (both live = F9).
6. Carry paused keyword's keyword-scoped negatives to ad-group level; verify graduated-exact walls still apply.
7. Exclusion-state notice to #37 same day.
8. T6 prediction: root-containment read expected at next pull with review date.

### P3. Weekly three-route search-term triage — 30-45 min per product (SHARED DEFINITION; steps 1-9)
1. Enter T2 only after T0 and T1 (Data Architecture S2 rule 1). Score last cycle first (V5 on due T6 rows).
2. Pull STR: Amazon Ads console > Measurement and Reporting > Sponsored ads reports > Create report > Sponsored Products > Search term, summary, date range aligned to pass window, filtered to campaigns in scope. Working columns: **Campaign Name, Ad Group Name, Targeting, Match Type, Customer Search Term, Impressions, Clicks, Spend, 7 Day Total Orders (#), 7 Day Conversion Rate, Cost Per Click (CPC)**. Confirm pull row/campaign count vs T3 campaign list; missing campaign = suppression.
3. Two guards before sorting: (a) **G12 MKL hygiene** — no syntax tag/relevancy score -> MKL maintenance; (b) **G11 ownership** — sibling-owned root -> wall build, not Route A.
4. **Route A, converters:** every term with in-window orders -> candidate row to #30 with evidence line (clicks, orders, window dates, source campaign, CPC, spend). Do NOT test vs graduation bar (pooling and decision are #30's vs S8.9 **S-H1**).
5. **Route B, proven waste:** spend with zero in-window orders -> negative exact with evidence in reason string. Firing numeral not printed in v4.0 (AM-3; SOP-29 AM-1). Rows go to #29 P4 (converting-term guard, sufficiency check). Incomplete evidence returns here.
6. **Route C, drift clusters:** irrelevant families sharing a root (wrong category/material/intent) -> one negative phrase on cluster root. Evidence: root, member count, combined clicks and spend. Wall level and reverse test are #29's.
7. **Head-term check:** for every priority term served, T2 child rows "Spend Share of KW %" vs K8 "# Exact". Discovery campaign with materially dominant share of a priority term's clicks and no live exact -> ADD EXACT + RESTRUCTURE before any performance verdict (S4 **X10**, S8.4 **S-R12**). Receipt to #12 same day; term leaves Route A and leaves P5 yield base.
8. **Off-taxonomy converters:** converting term below relevancy bar or outside taxonomy -> S8.9 **S-H6** MKL classification first; taxonomy expands deliberately (logged syntax tag + test plan) or term negates.
9. Stage, deploy, verify, log: bulk rows per #38 with verdict + scenario ID (missing = no deploy). Tuesday deploy after brand-management huddle; T+1; mismatch = SOP-12 F10. Route counts A/B/C per campaign close the pass.

**P3 route decision tree (table order, first match wins)**

| Condition | Route | Executed by |
|---|---|---|
| No syntax tag or relevancy score in current MKL | MKL maintenance and taxonomy pre-negation (G12) | Brand Management owns list; #29 places pre-negation |
| Root owned by sibling per #33 | Wall build on owned root; never candidate | #29 wall; #33 declaration |
| Priority term, dominant discovery click share, no live exact (X10, S-R12) | ADD EXACT + RESTRUCTURE receipt same day; excluded from yield base | #12 stands up; SOP-14 walls at P6 |
| Converting, relevancy >= bar, inside taxonomy | Route A candidate to #30 with evidence | #30 |
| Converting below relevancy bar or off-taxonomy (S-H6) | MKL classification decision, then expand or negate | Brand Management (taxonomy); #29 negates |
| Spend, zero orders, enumerable and isolated | Route B negative exact | #29 P4 standards; staged here |
| Spend, zero orders, terms share root and irrelevance class | Route C one negative phrase on cluster root | #29 P1 tree and reverse test |
| Evidence below G2 thresholds | No route; capped dated test (P8) | This SOP |

### P4. Defensive brand broad — 15-25 min per brand
1. One brand-broad per brand, Objective = Defensive.
2. Bids at floor discovered by #28's ladder (deploy #28 rows). Budget runs to the Defensive utilization target (S3 family **F10** "Budget & Pacing"); the one objective where budget filled before bids touched (S8.6 **S-D3**).
3. Brand terms steering-negatived out of every generic discovery campaign; brand term in Surface 1 = F10, fixed same day.
4. Weekly read, three figures: branded impression share held; ACOS vs Defensive band (O6); incursion list. No discovery yield read.
5. Competitor brand strings in served terms = incursion evidence -> #16.
6. Incrementality test on branded terms: dated step-downs per #35 schedule; record capture read at each step.
7. T6 each step with prediction and review date.

### P5. Graduation yield computation — 10-15 min per product
1. Numerator: validated terms routed to #30 in window from this campaign; head-term receipts excluded.
2. Denominator: window spend less spend of terms excluded in step 1.
3. Yield = validated terms routed / window spend x 100, per $100, **two decimals**.
4. Write into T3 "Harvest Yield" beside trailing baseline on same row.
5. Credit per source: a term validated in this campaign and an auto group credits both. #30 P7 computes same figure; divergence = data-quality finding.
6. Single zero window with spend active not automatic failure; triggers P13 when it repeats across governance window.

### P6. Graduation handoff and source-side wall confirmation — 10 min
1. Trigger: SOP-30 P1 graduation log = APPROVE naming this campaign. Graduation = decided, stood up, walled (#30 owns chain, #29 wall standard).
2. Confirm negative exact for graduated term in this campaign's negative list at level #29 selected, same session as standup.
3. Verify at next pull: term absent from served terms.
4. Remove term from next window's yield numerator and spend from denominator.
5. Wall not landed by session end = F2 = F8 GRADUATED-UNSTEERED; **S-H4** fires next pass (per C12, S-H4 not S-H6).

### P7. Negation-cadence audit — 10 min per product (exclusive ownership of SOP-14)
1. Four figures per campaign, this and prior pass: negatives added at Route B; cluster roots added at Route C; member count behind roots; window spend removed.
2. Spend removed = sum over negated terms of in-window clicks x CPC.
3. Cadence state: negatives added = 0 across **two consecutive passes** with spend active = leak-by-design = F1. Name cause: (a) feed absent, pass suppressed under G8; or (b) feed present, pass skipped.
4. Write counts and dollars into T6 (Level, Target, Rule / Scenario Fired, Change, Expected Outcome Window, Review Date); expected outcome = WAS % at next read.
5. Two consecutive F1 on same campaign -> PPC Lead with T6 history.

### P8. Dated-test governance — 15 min open, 15 min close
1. Every test at creation: start date, click quota or stop-loss date, capped bid. Missing any = no deploy (Doctrine S13).
2. Quota and capped bid read from verdict that opened test; recorded into T1 group S3 "Dated Test / Stop-Loss" and T2 K7 "Test Status".
3. No lever moves inside window except G3 budget assurance; mid-window bid step restarts window.
4. Exclusion-state notice to #37 at open.
5. At expiry: success -> term scales into standing campaign at verdict-carried bid; failure -> STOP-LOSS: CONCEDE OR DEFER with deferral condition in words (what evidence re-opens, when re-read).
6. Close = scored V5 row vs open prediction.

### P9. CAP SYNTAX receipt on discovery — 15-20 min
1. Trigger: T1 "Cap Status" = BREACH with staged delta (instrument layer owns cap decision, M5 reallocation, envelope arithmetic).
2. **Broad budgets in breaching family reduce first** (discovery most deferrable; push loses velocity and defense loses share when starved).
3. Reduction = family spend - capped allowance; lands on family broad daily budget first. v4.0 states no per-step limit on cap-driven budget reduction; the **+/-50% L2 limit is a bid limit** (AM-4); executed to the cap.
4. If removal takes broad below serving floor, excess routes back to instrument layer for reallocation across family's other discovery surfaces.
5. Re-read: family share vs cap on T1; product match-type broad share vs M6 destination.
6. T6: expected weekly dollars freed and review date.

### P10. Bid/budget mechanics on capped-by-design campaigns — 10 min per change set
1. Capped-by-design: discovery spending full budget daily is capped, not truncated; T3 note (P1 step 6) read by G3 before firing budget lever. Missing note -> reads as truncated -> unintended budget rise = F11.
2. Every change staged per #38 (prior, new, reason with verdict + scenario ID). No console edits.
3. Step sizes/floors/limits from S9 **L2** at execution; step exceeding L2 fails staging QC.
4. Lever order **L1**: budget (where G3 failing) > bid > placement > negation > structure > status. On capped-by-design campaigns first rung usually unavailable, pushing work to negation and structure (intended).
5. T+1 mismatch: redeploy same day, week's reads void, root cause; console edit names actor, routes to #37.

### P11. Event-window overlay and recovery-mode sentinel floor — 10 min arm, 10 min release
1. Arm on #32 plan in T2 K2 "Event Mode"; every broad row flagged through window + guard.
2. Inside window, structure changes freeze unless plan names them: no creations, fence changes, retirements, new dated tests (S8.12 **S-E1**: no new experiments enter pre-event window). G3 budget assurance and plan actions live.
3. Reactive negation (Routes B, C) continues; Route C cluster walls deploy normally.
4. Event-week rates leave P2/P7 trend reads through guard (G10 event exclusion); gates-only reads.
5. **Recovery Mode:** discovery budgets floor at **sentinel levels** (not zero); sentinel level arrives with entry log from instrument layer (not owned here). Human-review thresholds tighten; every discovery budget move confirmed against tightened tier.
6. Release: resume pre-window budgets/fence states unless reconciliation justifies new; staged logged set.

### P12. Variation re-point on broad — 10 min
1. Trigger: RE-POINT VARIATION or G6 RED with D2 backup.
2. Stage advertised-SKU edit, deploy same day.
3. T6 product event: CVR baseline resets, trend clock restarts, gates-only until sufficiency refills.
4. Yield baseline on T3 resets too.
5. Restock: re-point back. No D2 ranked backup -> hold on preferred SKU with D2-pending flag, escalate same day; SOP-14 does not choose backup.

### P13. Restructure or retire, pause, archive, re-entry — 25-40 min
1. Trigger: zero graduation yield across governance window with spend active, or ACOS outside Discovery band (O6) with Routes B and C exhausted.
2. Evaluate in order, record each: (a) seed refresh (new validated modifier roots since last seeding?); (b) negation audit (P2 containment + P7 cadence; stalled cadence = unrun procedure); (c) budget rebalance (compare yield figures of family's other discovery surface on T3); (d) only then retirement.
3. Retirement = PAUSED-PENDING with reason + named re-entry in T2 and T3; paused rows re-entry check only.
4. Two broad campaigns on one root with no declared split -> consolidate (SOP-12 P7 precedence: declared role, evidence read, longer clean history); loser's negation lists carry over in full.
5. Archive only past governance period, no re-entry; irreversible, human-mandatory; T6 closes with final registry state and yield figure.
6. Every outcome is a scored T6 prediction; retirement predicts family validated-term flow holds/improves at lower spend; silent reduction of output = WRONG-DIRECTION with written root cause.

## 5. Rules, Thresholds & Numbers

| Item | Value | Source |
|---|---|---|
| Broad share of match-type spend (M6) | 15-20% | v4.0 S10 M6 |
| Placement modifiers at creation | 0 on all three groups | P1 step 5 |
| Bidding strategy | Down-only outside ranking pushes | Doctrine S6.3 |
| Yield formula | validated terms routed / window spend x 100, two decimals | P5 |
| Spend removed | sum(clicks x CPC) over negated terms | P7 |
| WAS | zero-order spend / spend | WE-1 |
| Head-term share | campaign clicks on term / term clicks across all campaign types | Section 9 |
| Root containment | served terms containing root / all served terms | P2 |
| Cadence stall (F1) | 0 negatives across 2 consecutive passes with spend active | P7 |
| L2 limit | +/-50% (bid limit, not budget limit); $0.50 floor referenced in WE-3 | S9 L2 |
| Lever order L1 | budget > bid > placement > negation > structure > status | S9 L1 |
| Dated test | start date + click quota or stop-loss date + capped bid; verdict within 1 working day of read | P8 |
| Secondary family reference share (WE-4) | 25.0% capped allowance (family read at 30.0% above "secondary reference share" of F13) | F13 Syntax Rollups |
| Unrouted validated term | 2 passes = pass-quality finding | I-4 |
| Data timing | Monday 06:00 landing, refresh by 09:00 | I-1 |
| Defense floor re-test | Quarterly per #28 | Section 9 |
| Escalation | F1/F4 on 2nd occurrence; F3/F12 on 1st; others twice in consecutive cycles | Section 7 |
| Procedure times | P1 35-50; P2 20-30/kw; P3 30-45/product; P4 15-25/brand; P5 10-15; P6 10; P7 10; P8 15+15; P9 15-20; P10 10; P11 10+10; P12 10; P13 25-40 min | Section 4 |

### v4.0 rule IDs referenced

| ID | Meaning as described |
|---|---|
| O1 | Untagged campaign unmanaged; routes to assignment (corpus alias G10) |
| O6 | Objective-metric contract; Discovery graded on cost per discovered converter, WAS %, graduation rate; Defensive on branded IS and incrementality |
| M6 | Structure targets (broad 15-20%) |
| M5 | Funding / reallocation queue |
| P4 | Family is cap-enforcement unit |
| P5 | Human-mandatory tier (structural changes, gate failures, deployment confirms) |
| L1 | Lever order |
| L2 | Step sizes, +/-50% bid limit, floors |
| L4 | Sizes budget increases |
| L5 | Spend-without-sales negation (no figure) |
| X10 | Auto/discovery dominance read on priority term |
| F1 | Product Economics (Discovery Max-ACOS band) |
| F8 | Structure/Registry; GRADUATED-UNSTEERED state |
| F9 | Placement drift flag (different metric; not broad drift) |
| F10 | Budget & Pacing (Defensive utilization target) |
| F11 | Waste & Negation (Discovery WAS limit) |
| F13 | Syntax Rollups (secondary reference share) |
| S-H1 | Graduation bar |
| S-H2 | WAS breach fires negation pass |
| S-H4 | Unsteered graduate (exact live, source unnegated) |
| S-H6 | Off-taxonomy converter |
| S-H7 | "Zero-sale spend above threshold" (no threshold stated) |
| S-R12 | Priority term with zero exact -> ADD EXACT + RESTRUCTURE |
| S-Y5 | Chronic conversion syntax freezes bids at maintenance |
| S-Y7 | Reduce to cap |
| S-A4 | TACOS vs stage band (Recovery Mode entry) |
| S-A6 | Reduce until envelope holds |
| S-D3 | Defensive budget filled before bids touched |
| S-E1 | No new experiments in pre-event window |
| G1-G12 | See gates table (v4.0 numbering with corpus aliases) |
| V1 | Prediction with review date; unscored actions do not accumulate |

### Verdict-to-execution mapping (broad)

| Verdict | Broad execution |
|---|---|
| QUARANTINE: DATA REFRESH | No route, no negative; term stays; refresh task (G1) |
| UNLOCK TRAFFIC | Bid step per L2 on named broad keyword; budget lever not the response on capped-by-design |
| FIX BUDGET (TRUNCATED) | Only where T3 lacks capped-by-design note (else F11) |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | P8 step 3 |
| FUND TEST (UNFUNDED PRIMARY) | P8 opens dated test at capped bid; quota and stop-loss in T1 S3 and T2 K7; never uncapped |
| RANK PUSH: FUND SIZED PUSH | No broad execution; routing defect -> #12 (Doctrine S3.1) |
| RECOVERY PUSH | No broad execution; steering wall after exact live (P6) |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | No broad execution (#12) |
| FIX CONVERSION FIRST; DEFER PUSH | Family discovery holds at current spend; no new seeds (S-Y5) |
| PLACEMENT FIX FIRST | Bids hold; #28 |
| RE-POINT VARIATION | P12 same day on G6 RED |
| TAPER | No broad execution |
| HOLD; DEFEND LIGHTLY AT RANK | Surface 3 only; hold at floor |
| DEFEND AT FLOOR | Surface 3 only; restore to floor in one step on drift |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | CAP SYNTAX half first per P9; bid-down per P10 vs T2 K6 ceiling |
| INCREMENTALITY LADDER | Surface 3 only, execution only on #35's schedule |
| ADD EXACT + RESTRUCTURE | Receipt to #12 same day; steering negative after; excluded from yield base |
| CONSOLIDATE DUPLICATES | P13 step 4 |
| GRADUATE FROM DISCOVERY | Issued by #30; P6 here. v4.0 S13.1 cross-map: "GRADUATE + STEER" |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | Pre-load P1 step 8; reactive P3 B/C; steering P6; cadence P7. v4.0 cross-map: "CUT / NEGATE" |
| ENTER SBV ARBITRAGE | No broad execution |
| OPEN / ROTATE / EXIT CONQUEST | No broad execution; incursions to #16 |
| STOP-LOSS: CONCEDE OR DEFER | P8 step 5 |
| PAUSED-PENDING | P13 step 3 |
| LEAVE TO HARVEST | No structural change; re-eval date in #30's pool |

## 6. Data Inputs Required

**Amazon reports**
- **Sponsored Products Search Term Report** (summary; columns: Campaign Name, Ad Group Name, Targeting, Match Type, Customer Search Term, Impressions, Clicks, Spend, 7 Day Total Orders (#), 7 Day Conversion Rate, Cost Per Click (CPC)), window aligned to pass (WEs use 14-day window).
- **Sponsored Brands search term report** and **STIS** (Raw Pull Pack, joined to T2 campaign child rows).
- **Bulk file** current-week pull (State, Daily Budget $, Bid / AG Default $); staged change sets in #38 format.

**Command Workbook**
- **T0**: zone A code-red flag; zone C named cells (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC); zone H (envelope).
- **T1**: SYNTAX BOARD row ("Gap KWs"); group S3 spend-governance columns (family discovery allocation share; "Dated Test / Stop-Loss"); "Cap Status"; "MT Cov Broad %"; family share.
- **T2 KEYWORD COMMAND**: K2 "Event Mode", "Inventory Band", "Targeted Variation(s)"; K5 flag columns (ACOS band, CTR-versus-market, CVR-versus-market, zero-quarantine), "WoW Block"; K6 economics block (ceiling); K7 "Test Status"; K8 "# Exact", "# Phrase", "# Broad", "# Auto", "Term Owner (Family)"; campaign child rows "Spend Share of KW %".
- **T3 CAMPAIGN BOARD**: State, Daily Budget $, Bid / AG Default $, Objective Tag, "WAS %", "Harvest Yield" + trailing baseline, "Negation State", "In-Budget Bucket", "Truncation Flag (G3)", capped-by-design note, naming-compliance flag, owner, root-containment reads (this/prior window).
- **T5 PRODUCT LOG**: platform relevance shifts, material structure events.
- **T6 DECISION LOG**: Level, Target, Rule / Scenario Fired, Change, Expected Outcome Window, Review Date, V5 scores.
- **T7 MANIFEST**: A2, A3, A5, A6, B5, B8, B9, D2, D7.

**Other**
- Master Keyword List (syntax tags, relevancy scores, refresh cadence) — Brand Management.
- #33 term-ownership declaration / stewardship grants.
- #29 pre-load table, wall-level selection, steering walls.
- SOP-30 P1 graduation log row (APPROVE, source list); #30 pool re-eval dates.
- #32 event plan; instrument layer recovery entry log with sentinel levels.
- D2 variation map (Economics & Context Pack) with ranked backups.
- #28 ladder / defense floor; #35 incrementality schedule.
- Economics Worked-Example Set cases E1, E2 (ramp).

## 7. Outputs / Artifacts

| Event | Artifact | Storage / retention | Consumer |
|---|---|---|---|
| Weekly pass (P3) | Route A candidate list (one row per term with all serving sources and evidence line); Route B and C staged sets with evidence; route counts per campaign | With #38 session record; counts in T6 append-only | #30 P1; #29 P4; #38 |
| Yield (P5) | Per-campaign yield with trailing baseline | T3 "Harvest Yield"; history in T6 | #30 P7; T1 and audit |
| Cadence (P7) | Negatives added, cluster roots, member counts, spend removed $ | T6 with expected WAS and review date | #29 monthly wall audit; V5 |
| Structure events (P1, P2, P13) | T3 row (Objective Tag, owner, capped-by-design note, wall list); T2 K8 change; T6 prediction | T3; T5 for material events; T6 | #29; #38; next pass |
| Head-term receipt | Receipt: term, source campaign, click share, exact count, exposure window | #12 same-day queue; T6 copy | #12; #29 |
| Graduation confirmation (P6) | Wall confirmation line + next-pull absence check | T3 "Negation State"; written into #30 chain record | #30; #29 |
| Dated tests (P8) | Test record (start, quota/stop-loss, capped bid, closing verdict + scored prediction) | T1 S3; T2 K7; T6 | M5 queue; V5 |
| CAP SYNTAX (P9) | Reduction record (excess, dollars removed, new daily budget, serving-floor check, both shares) | T3; T1; T6 | Instrument layer; T1; A4 structure-targets view |
| Every deployment | Staged bulk set with verdict + scenario ID; T+1 report | #38 session record | #38 |
| Session close | Updated Ledger row #14 | Cross-Reference Ledger | Next build session |

**Weekly gate artifact:** deployed change set with complete evidence line on every negation row, T+1 report, yield figure beside baseline. Routes without yield, or yield without baseline = not closed.

**Alarm routing:** F3, F12 same day to operator queue (PPC Lead copied); F2, F9, F10 same day into change set; F6, F7, F8, F11 weekly worklist; F1, F4 to PPC Lead on second occurrence; F5 to instrument layer with T1 share figures.

### Failure modes

| ID | Failure | Detection | Response | Incident |
|---|---|---|---|---|
| F1 | Negation cadence stalls | 0 negatives 2 consecutive passes with spend | P3 immediately; name cause (feed absent/G8 vs pass skipped) | v1.0 F1 leak-by-design |
| F2 | Graduated term still serving in broad | Approved graduation term in served terms next pull (F8 GRADUATED-UNSTEERED, S-H4) | Wall same day; #29 audit adds campaign | v1.0 F2 |
| F3 | Head term carried by broad | P3 step 7 (X10, S-R12) | Receipt to #12 same day; exposure recorded | v1.0 F3, account's named failure class |
| F4 | Drift explosion after relevance-model shift | Root-containment falling sharply across several families | P2; Route C aggressively; enter shift in T5 | v1.0 F4; semantic matching widened broad drift 2024-2026 (Doctrine S3.3) |
| F5 | Discovery cannibalizing family cap | Family discovery share above allocation on T1 | P9 | v1.0 F5 |
| F6 | Pass run on partial feed | Pull campaign count short vs T3, routes produced anyway | Void routes; reverse deployed negatives; 2nd miss escalates to Data Ops | New |
| F7 | Yield on contaminated base | Route A includes head-term/graduated term or denominator not reduced | Recompute; correct T3; re-score T6 | New (WE-2: 1.69 -> 2.10) |
| F8 | Second broad on one family root | Registry > 1 live broad, no declared split | Consolidate per P13 step 4 | New; Doctrine S5.3 micro-splitting illegitimate |
| F9 | Fenced and unfenced serving together | Both return served terms in same window | Pause open version; reads void | New |
| F10 | Brand terms in generic discovery | Brand strings in Surface 1 served terms | Steering negative same day | New |
| F11 | Capped-by-design read as truncated | FIX BUDGET (TRUNCATED) on campaign lacking note | Restore note; reverse rise; re-read | New |
| F12 | Sibling-owned root seeded | Seed/served term on root assigned to another product, no stewardship grant | Remove seed; negative phrase; G11 check | New |

## 8. Decision Rights

- **Human-mandatory:** campaign creation (P1), fence decision (P2 step 3), every head-term receipt (P3 step 7), dated-test opens and closes (P8), CAP SYNTAX execution (P9), retirement and archive (P13), every deployment confirm; plus v4.0 P5 tier.
- **AI-executable with audit:** route sorting with evidence-line drafting, yield and cadence computation, root-containment reads, wall-confirmation checks, staged bulk drafting, T6 drafting. Nothing deploys from the skill.

| Authority Matrix v2.0 row | Coding |
|---|---|
| Weekly verdicts (established US) | PPC Lead D; incoming operator E (assigned scope); PPC Manager E; brand-management owner R at daily huddle (review, not veto) |
| Structure creation (all SOPs) | PPC Lead D or per SOP scope; incoming operator and PPC Manager E |
| Bulk deployments (#38) | PPC Lead R; operators E own scope |
| Automation rules (#37) | PPC Lead D; incoming operator E and R |
| Sibling declarations (S-series) | PPC Lead D; incoming operator E; brand-management owner R |
| Code-red declaration + close | PPC Lead D; incoming operator and PPC Manager E (governs P11 sentinel floor) |

- Checkpoint holder: PPC Lead. Matrix rule 5 vacancy reversion.
- Taxonomy decision (S-H6): Brand Management. MKL ownership: Brand Management.
- Ramp: Week 1 reproduce E1 and E2 to the cent; shadow Monday pass; locate listed artifacts unaided; name three surfaces; recite four pre-load classes. Week 2 pass bar: zero rows forwarded to #29 without complete evidence line. Week 4: two clean audit weeks with zero F1, F6, F7 attributable to own sessions. Eight live-defense questions.

## 9. Account-Specific Facts

- Worked examples use fictional base (no live economics spine attached): AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target ACOS 17.5%, Max Acceptable 26.3%.
- **WE-1 (Bamboo broad):** budget $25.00/day capped; 14-day: 9,800 impr, 92 clicks, $158.24, 4 orders; CPC $1.72, CTR 0.94%, CVR 4.35%, sales $320, ACOS 49.5%; WAS 78.3% ($123.84 zero-order); 61 served terms. Route A: "bamboo sheets split king" (11 clicks, 2 orders), "bamboo sheet set deep pocket king" (9 clicks, 1 order) — first clears 3 orders combined with auto close-match. Route B: "bamboo shoots plant" 14, "bamboo flooring cleaner" 8, "bamboo pillow" 6, "bamboo cutting board" 5 = 33 clicks $56.76. Route C: "crib" cluster 3 members 9 clicks $15.48. Removed $72.24; projected WAS 60.0%. Yield 1.26/$100.
- **WE-2 (Cooling broad):** 7,400 impr, 118 clicks, $237.18, 5 orders, CPC $2.01, ACOS 59.3%. "cooling sheets king" broad 47 / auto loose 19 / phrase 9 / exact 0 = 75 clicks; broad share 62.7%. Yield corrected 1.69 -> 2.10 ($94.47 removed, base $142.71). Receipt Monday, exact Thursday; exposure ~10.07 clicks = $20.24.
- **WE-3 (Satin broad):** 125 clicks, $212.50, CPC $1.70, 6 orders on 68 converting clicks (CVR 8.82%); zero-order $96.90 (57 clicks across 39 terms, 1.46 avg); WAS 45.6%; in-budget 96%; containment 44/61 (72.1%) -> 33/68 (48.5%), -23.6pp; "+satin +sheets" at carried bid $1.35.
- **WE-4 (Cooling family CAP SYNTAX):** product weekly tracked spend $1,840.00; Cooling = Secondary family at $552.00 (30.0%); capped allowance 25.0% = $460.00; excess $92.00. Split exact $268, broad $168, phrase $71, auto $45. Broad $168 -> $76/wk ($24.00 -> $10.86/day, -54.8%); 6.31 clicks/day at $1.72. Product broad $404 (22.0%, above M6) -> $312 (17.0%, inside 15-20%).
- Account's named failure class: head term carried by campaigns that choose their own traffic (F3).

## 10. Open Items

| ID | Gap |
|---|---|
| AM-1 | Search-term join has no dedicated T7 MANIFEST row (sits across B5 and B9; manifest groups A1 to E) |
| AM-2 | Broad drift (root-containment fall) has no firing threshold; v4.0 F9 is placement drift |
| AM-3 | Reactive-negation firing threshold and "price class" dimension (S-H7, L5 no figure); duplicates SOP-29 AM-1/AM-2 |
| AM-4 | No per-step limit on cap-driven budget reduction (L4 increases; L2 +/-50% bid; S-Y7, S-A6 no bound) |
| AM-5 | Verdict vocabulary reconciliation (18 / 25 / 26; Ledger C10) |
| AM-6 | Dangling naming citation (S4.2); overlaps SOP-13 AM-2 |

- **Conflicts:** C3 (#31 no procedural doc); C9 (gate numbering; rides to v4.1 as SOP-29 AM-11); C10 (vocabulary); C12 (S-H4 vs S-H6 label); **C13 (new)** Bamboo window yield anchor 1.27 on rounded $158 (SOP-30 v1.0, SOP-13 v2.0) vs 1.26 on $158.24 (SOP-29 v2.0 WE-5).
- **Named but not present:** v1.0 Criteria System (naming authority); dedicated T7 search-term row; unblended per-variation margin table (provisional flag until it lands).
- Review triggers: Criteria System increment; any P3 change (increments SOP-13/14/15/29); C10 ratification; #29 pre-load standard change; margin table landing; C9 resolution; any session returning Ledger row #14.
