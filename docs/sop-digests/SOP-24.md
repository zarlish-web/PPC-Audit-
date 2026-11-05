# SOP-24 Digest: Re-Ranking and Recovery Operations

Source: `PPC_SOP_24_Reranking_and_Recovery_v2_0.pdf` (34 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-24: Re-Ranking and Recovery Operations (Component #24 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead, with the brand-management counterpart per product on the listing, price and review cause classes (these resolve outside PPC) |
| Supersedes | SOP-24 v1.0 (2026-07-24) in full |
| Parent | Extends SOP-23 and inherits its sizing chain by reference; everything here is the delta |
| Thresholds | Master PPC Decision Criteria System v4.0 only; zero local thresholds |
| Verdict strings | Quoted verbatim from Keyword Decision Record (KDR) Template v3.0 "Bands & Verdicts Reference" sheet, with the v4.0 Section 13.1 cross-map stated where they diverge (Ledger conflicts C10 and C18) |
| Ledger | PPC Cross-Reference Ledger v2.8; this row closes Wave 5A at v2.9 (also the Wave 5B gate) |

**Verdict / purpose.** "A lost rank has a cause, and recovery spend released before the cause is resolved buys rank the cause takes back." Ranking and recovery run on identical thresholds and opposite disciplines: a ranking push asks "can we win this position"; a recovery asks "why did we stop holding it." A recovery that skips the second question "is a ranking push wearing a cheaper velocity assumption." The SOP owns: loss dating, the seven cause classes, the confound and void determination (consumed by SOP-06 and #35), baseline restoration and its verification artifacts, the observation window (self-recovery vs bought rank), recovery-adjusted sizing, the pre-OOS overlay and post-restock standup, compressed in-flight verification, the recovery close, and the serial-recovery escalation out of PPC. It owns no threshold, no ladder rung, no push sizing chain and no campaign edit.

**Why diagnosis is the document.** An unsized push leaks at a rate; an undiagnosed loss buys a rank that reverts, so the whole recovery budget returns nothing and the term re-enters the queue looking like a fresh candidate. v4.0 rule X9: the product log is consulted before PPC is credited or blamed for any swing.

### 1.1 What changed at v2.0
- v1.0 measured 3 pages against a 10-18 page bar. Procedures 5 -> 14; failure modes 5 -> 13; worked examples 1 -> 4; full 25-verdict closed vocabulary (not 5 rows); adds Element 11 (operator ramp) and Element 12 (interface contracts).
- Six corrections of substance (Section 10.2):
  1. v1.0 header cited "v4.0 Section 8.2" as recovery authority; 8.2 is Syntax-Level Scenarios (S-Y). Recovery authority is **Section 8.4 S-R13, Section 8.3 S-I5, Section 11 T5**.
  2. Three v1.0 numerals attributed to v4.0 and not present there are retired: **2.0 positions/day recovery velocity** (AM-1), **day-4 checkpoint** (AM-12), **third-recovery escalation count** (AM-6).
  3. Four locally minted v1.0 verdict strings retired (Section 5.2).
  4. v1.0 citation "#31 / P1.4" for OOS forecasting retired to the instrument layer per Ledger conflict C3.
  5. v1.0 "observe per the v4.0 observation window for the cause class" retired; no such table exists (AM-2).
  6. Recovery-zone definitional divergence registered fresh at AM-13 (distinct from C17).
- Carried forward: all seven cause classes (now sourced), all five v1.0 incidents (F1-F5), the bid-seeding bracket (converted from generator into a test), and doctrine lines: rank memory holds better on a taper than a hard stop; the drift is the cost of waiting; UNKNOWN is a legal finding; PPC is neither credited nor blamed until the attribution check completes; diagnosis is scored separately from prediction.

### 1.2 The seven cause classes (the document's primary asset)
No other document carries this list. SOP-06 defers its confound cause classes to SOP-24 P1 by name; #35 defers its void classes here; the Ledger row for the diagnosis engine records SOP-24 P1 as one of its two entry points. Closed at seven; a new confirmed class increments this SOP and propagates to SOP-06, #35 and SOP-25. **Tested in this fixed order** (order required by v4.0 rules D5 and D6, not order of likelihood):

| # | Class | What dates it / evidence | Consequence; who resolves |
|---|---|---|---|
| 1 | **OOS event** | T5 Product Log event type "OOS start-end per variation" vs T2 OOS Overlay Flag and the daily rank series. Rank series inflects **within** the stockout window, not before. | Only class resolved by an arrival not a decision. Restoration is the restock; P4 verification = landed-stock artifact; P11 deploys at day 0. v4.0 F3: a term that held rank 6 before a stockout is a RECOVERY candidate with a proven ceiling under D10, not a never-ranked hopeful. |
| 2 | **Price move** | T5 event type "price move" on our side, or Price Position Index (E10) crossing a class boundary on the market side. F5 bands: **ADVANTAGED < 0.92; PAR 0.92-1.08; PREMIUM 1.08-1.25; OUTPRICED > 1.25**. | Rule D6 puts price check first in every conversion diagnosis, so tested before the four below. OUTPRICED routes to pricing and vetoes listing spend as primary remedy. Restoration = price back to PAR or better; PPC restores nothing. Live constraint: T7 field group D3 SQP median price reads MISSING, so market limb not computable (WE-2). |
| 3 | **Review shock** | T2 rating and review count vs Review Position Gap (E11). F4: **FAR-BEHIND = under 50% of top-5 median review count, or 0.3 stars or more below it**. | FAR-BEHIND fails the O3 competitor-credibility clause outright; recovery cannot be funded at any bid while it holds. Closes on review velocity, not spend. Routes to brand-management owner. BEHIND permits recovery on long-tail and mid-volume terms only while velocity closes it. |
| 4 | **Listing event** | T5 event types "listing / image / A+ change" and "eligibility flip". F4 flags CVR and CTR PROVISIONAL for any main-image or price-adjacent change inside **14 days**. | Restoration = edit reverted or suppression lifted, verified with artifact. Gate G5 governs indexing limb: a term out of index ranks at no bid; a rank-objective term moved to backend-only is a listing task before a bidding task. Routes to listing owner. |
| 5 | **Competitor surge** | T2 Competitor Depth (D8) block: competitor deal window, launch, price cut or review surge on a top-10 holder. Rule D7 splits market inflation from self-inflicted inflation through E1 before any aggressiveness verdict. | No restoration step (nothing of ours changed). Decision: is position still winnable on O3 competitor-credibility test at new market state. Recovery funded into a competitor deal window buys the worst comparison of the month under S-C5. Live constraint: D8 MISSING, so evidenced only where T5 carries a manually logged competitor entry. |
| 6 | **Deal hangover** | T5 event type "deal window" with trend-exclusion flag set, read against #32 settle marks. Gate G10 excludes event weeks and the 14 days following. | Not a recovery case. Per Ledger row for #32, post-deal dip inside settle is a hangover resolving by calendar; F13 classes it TRANSIENT at 1-2 weeks. Hold and observe; open only if depression survives settle expiry. |
| 7 | **Taper too deep** | T6 decision log: rank series inflects on a dated ladder step. Cross-read T4 Ladder State (step / date) and Discovered Floor $ vs T2 current bid. Also #37 rule change log (runaway automation rule stepping against stale target = same signature without a human ladder entry). | Only class where PPC is the cause; remedy is a rung not a push. v4.0 Section 10 rule M3: on slippage beyond tolerance, restore one step; that value is the recorded minimum viable CPC. WE-4: misreading costs 59.4x the correct remedy. |
| 8 | **UNKNOWN** | No class carries evidence. | Legal finding. Routes to a deeper read, never to a default push. |

## 2. Scope and boundaries

Per the Cross-Reference Ledger, this component owns **baseline restoration, the pre-OOS overlays, and the void and confound cause classes**. Everything below is referenced, never restated.

| Excluded decision | Owner | Seam |
|---|---|---|
| Every threshold, band, scenario, verdict issuance | v4.0 (#8) | A numeral here without a v4.0 section beside it is a defect. Missing numerals are amendment items (Section 10.3). |
| Push candidacy, the O3 gauntlet, the M2 sizing worksheet, funding, in-flight operation, achievement and stability confirmation | SOP-23 | Inherits worksheet chain by reference. Dated seam: a rank held then lost belongs to SOP-24 from the moment the loss is dated at P1, and returns to SOP-23's operating cadence once the recovery worksheet is funded. SOP-23 classifies at candidacy; SOP-24 consumes, never re-runs. |
| Ladder rungs, step derivation, exit-bid discovery, reversion rule, floor register, modifier sizing | #28 | #28 is the authoritative ladder for SOPs 12, 23, 24, 25, 26. SOP-24 decides whether/when a taper happens (P9, P13); every rung value, floor, reversion arithmetic is #28's. A step size written here is a defect. |
| Campaign creation, bid/budget edits, re-point execution, taper execution at campaign level | SOP-12 | SOP-24 issues standup order and restore instruction carrying verdict-borne values; SOP-12 executes. A bid invented here is a defect. |
| Post-objective normalization sequence and descent schedule | SOP-25 | A recovery reaching baseline exits into SOP-25 exactly as an achieved push does. SOP-25's F2 exists because descent slip and recovery get confused; SOP-24's cause classes separate them. |
| Floor operations, quarterly re-ladder, code-red protocol, Recovery Mode posture | SOP-26 | Product-level Recovery Mode and keyword-level recovery are different objects sharing a word. SOP-24 reads product posture as a constraint at P8; never declares, runs or closes the protocol. |
| Event plans, caps, arming, settle marks, hangover class | #32 | Post-deal dip inside the 14-day settle is #32's hangover, not a loss. SOP-24 opens only at settle expiry; cites Ledger row, not a #32 procedure number. |
| Family term ownership and lead declaration | #33 | Gate G11 holds the restore step until lead assigned. SOP-24 supplies recovery class and cost-to-close; adjudicates neither side. |
| OOS forecasting, restock dates and cover | Instrument layer | v1.0 cited "#31 / P1.4"; per C3 #31 has no procedural document. Instrument and feed: T2 Inventory Band, Days to Stockout and Targeted Variation(s), fed daily from the Economics and Context Pack inventory feed. |
| Queue ranking, envelope law, budget release and return | Instrument layer | T0 zone H and Account Rollup tab A2. SOP-24 submits a sized worksheet, receives a dated release; never ranks the queue, never cites a #31 procedure number. |
| Negation walls at every structure event | #29 | Restored/re-pointed campaign needs walls rebuilt in same working session. SOP-24 names requirement, never wall level. |
| Staging, upload, T+1 verification | #38 | Every change staged and proven by next-day diff; no console edit outside staged set. |
| Prediction scoring rubric and tolerances | #6 | SOP-24 supplies confound cause classes that make VOID legal and the diagnosis score; #6 owns the rubric. |
| Which units are terminal or LTSF-tiered | #27 | Per C6, deciding document outside corpus. CONSTRAINED earning-potential class bars recovery pushes outright under v4.0 Section 8.1 S-A10; SOP-24 stops at that boundary. |

Other adjacent: #16 (conquest), #30 (harvest/graduation), #35 (incrementality), #37 (automation rules), #39 and Data Operations (feeds), #41 (economics), components 17-19 (SBV video build).

## 3. Triggers

| Trigger | Detecting artifact / observable | Max lag to start | Proc |
|---|---|---|---|
| Rank loss on a held term | T2 Organic Rank moving from AT or NEAR to worse position class vs Best Rank (Hist) + Date, on daily rank series (D9) | **Not stated in v4.0.** F6 bands position classes and velocity but no loss threshold or detection interval. **AM-1** (highest priority; trigger of the entire document) | P1 |
| Rank slipping at a held position | T2 Velocity (pos/wk) reading SLIPPING (F6: outside FLAT band of +/-1 position/week) | One weekly cycle (V4 sets weekly full audit producing Master Action Records) | P1 |
| Inventory RED forecast | T2 Inventory Band flipping RED, or Days to Stockout <= 14 on a ranked term's targeted variation | Same day (S-I3 and F3: pre-OOS taper trigger at 14 projected days) | P9 |
| Stockout occurred | T2 OOS Overlay Flag set, variation unbuyable despite P9 taper | Same day (S-I4: push and share objectives to Paused-pending; trend windows marked for exclusion) | P10 |
| Restock confirmed | OOS variation returns to in-stock on inventory feed, cross-read vs T2 Targeted Variation(s) | Same day (F3: recovery play triggers at restock confirmation; S-I5: conditional on a pre-OOS baseline existing) | P11 |
| Cause resolution | P4 restoration artifact lands: stock in, price PAR or better, listing edit reverted, suppression lifted, or ladder rung restored | Not stated (artifact-to-observation interval). **AM-3** | P5 |
| Observation window closes | T2 Organic Rank still depressed vs baseline after P5 window, restoration artifact on file | Not stated per cause class; F13 carries persistence at syntax grain only. **AM-2** | P6 |
| Recovery funded | T0 zone H entry state -> FUNDED with dated release | Same day for post-restock (F3). Other classes not stated: **AM-8** | P11 |
| Daily in-flight verification | Daily rank series on live recovery vs worksheet velocity line and T2 In-Budget % | Same day (T5: daily rank checks for 3 weeks; V4: oversight-class checks daily during pushes) | P12 |
| ETA checkpoint | T2 ETA Checkpoint date arriving with baseline not reached | Same weekly read (S-R13 and S-I5: recovery ETA checkpoint at 3 weeks) | P13 |
| Baseline reached | T2 Organic Rank at or better than T2 Pre-OOS Baseline | Same weekly read (T5: baseline reached = recovery mode exit; S-R6: 2 consecutive weeks at/under target rank = taper trigger). Can differ: **AM-4** | P13 |
| Confound detected | T5 trend-exclusion flag, armed window from #32, or dated competitor event inside a live recovery's read window | Same weekly read (G10: event weeks + 14 days excluded; S-E5: rank achieved during events provisional) | P3 |
| Repeat loss on one term | T6 carrying a prior closed recovery on same term inside review period | Not stated; no recovery-count rule or window. **AM-6** | P14 |
| Product posture flip | T0 zone A entering push freeze or code red (S-A3, S-A4) | Same cycle on S-A3. S-A4 enters Recovery Mode (cadence daily under R4; R3 permits new Ranking objectives only on RECOVERY-class terms at HIGH confidence) | P8 |

## 4. Procedures

Fourteen procedures. P1-P8 = diagnosis and sizing spine (every cause class). P9-P11 = OOS lane. P12-P14 close every recovery. Time estimates assume packet refreshed and OVERSIGHT filter applied.

### Preconditions and gates (Section 3) - must read current on T7 before Section 4 runs
v4.0 gate numbers govern; corpus aliases given per C9; the two schemes are never mixed inside one reason string.

| Manifest ID | Gate | Requirement | Observable that proves it |
|---|---|---|---|
| A4, A5 | G1 | No impossible-metric flag: no CVR of zero with orders, no ACOS without orders, no cross-table disagreement | T2 Flag: Zero-Quarantine clear; Validation State not QUARANTINE. Quarantined row -> flag + data-refresh task, never a recovery. Rule P8: beats urgency (stockout in progress does not license diagnosis on broken data). |
| A4, A1 | G2 | Sample sufficiency: **>= 15 clicks in 7 days for a bid read; >= 100 clicks for the CVR that sizes the recovery** | T2 Clicks 7/30/60d and Sample State. Below 100, CVR falls back to **60-day** window; if outage consumed that too, pre-OOS baseline CVR is the stated input under test. A1 MISSING -> four-period trend context unavailable. |
| A3 | G3 | Hosting campaign not budget-truncated. **In-budget < 70%** marks every rate TRUNCATED; forces budget lever before any bid conclusion | T2 In-Budget % >= 70. Corpus alias: KDR Bands sheet labels **51-70 "strained"**; G3's 70% governs. A3 PARTIAL -> day-of-week curve behind G7 unavailable. |
| A7 | G4 | Advertised offer eligible and unsuppressed (eligibility flip is itself a cause class; read as evidence at P2 before as precondition at P11) | T2 Eligibility = eligible. Flip halts all execution for target same day and opens listing task. |
| B1 | G5 | Term indexed and, on a rank objective, placed in title or bullets | T2 Indexed? = yes; Listing Placement = title or bullets. Read as a cause first; re-indexing is the restoration artifact. |
| D1, D2 | G6 | Targeted variation GREEN before a recovery deploys. **GREEN = days on hand > lead time + 21 days at max-sales-day velocity** | T2 Inventory Band and Days to Stockout vs Targeted Variation(s). YELLOW freezes recovery spend at current level (S-I2); RED routes to P9. D2 PARTIAL -> backup chain confirmed on head terms only. |
| A3 | G7 | Campaign budgets reconcile to product envelope; product pacing **within 25%** of day-of-week curve | T2 Envelope Status and T0 zone H available dollars. A recovery not fitting envelope is a queue decision at instrument layer, not a smaller recovery. |
| All | G8 | Packet manifest reports present/stale/missing before analysis. **Below 85%** of gate-relevant fields = DEGRADED, flags only | T7 Status column and completeness rollup on cycle header. **Live read 0.571.** |
| D1 | G9 | Price stability: **no price change on targeted variation in trailing 7 days**, else CVR and ACOS carry PROVISIONAL; no conversion verdict | T5 Event Type = price move vs T2 Margin $/Unit. Corpus alias: SOP-12 v2.0, Data Architecture and several SOPs use G9 for margin freshness; v4.0 assigns G9 to price stability; both checked here. |
| D7 | G10 | Event weeks and the **14 days following** excluded from trend reads that date a loss or score a recovery | T5 Trend-Exclusion Flag and T2 Event Mode. Corpus alias: corpus uses G12 for event freeze and G10 for objective tagging; v4.0 assigns G10 to event exclusion. Void determination's instrument; P3 runs on it. |
| D6 | G11 | No second sibling carries an active push or recovery objective on same term | T2 Family Conflict and Term Owner (Family), sourced from Account Rollup tab A1. D6 PARTIAL; Bamboo root ownership OPEN at cycle 1. |
| B11 | G12 | Term exists in current Master Keyword List with syntax tag and relevancy score; list **not stale past 30 days** | T2 Syntax Tags and Relevancy populated. Corpus alias: G12 used for event freeze across corpus; v4.0 assigns G12 to keyword-list hygiene. |
| B3, D9 | Rank pack (not numbered) | Best rank + date, pre-OOS baseline, velocity, ETA present; daily rank series for dating and in-flight | T2 Best Rank (Hist) + Date, Pre-OOS Baseline, Velocity (pos/wk), ETA to Target (wks). Both PARTIAL on head terms only. Term outside head-term coverage cannot have loss dated and does not proceed past P1; finding attaches to T7 D9 row. |
| B8, D1 | Economics chain (not numbered) | T0 zone C live: AOV, contribution per order, break-even ACOS, Target ACOS, Max Acceptable, Expected CPC reference | T0 zone C margin table version and fresh/provisional state. B8 PRESENT on blended margin; D1 PARTIAL -> every ceiling PROVISIONAL. External dependency D1 (open) caps this component. |
| D3, D8 | Cause evidence (not numbered) | SQP median market price and competitor depth present | T2 Price Competitiveness Flag and Competitor Depth (D8) carrying values, not build markers. Both MISSING account-wide; P2 can return UNKNOWN on a term whose cause is readable from data not yet held; P2 step 7 requires writing it as a manifest finding. |

### P1. Loss dating (mandatory first; precedes every other read). 12-20 min per loss. Source: X9, D5.
1. Open T2; confirm T0 and T1 read first (product posture and syntax caps constrain everything; a recovery sized under an unread S-A3 push freeze is void at P8).
2. Read T2 Best Rank (Hist) + Date and Pre-OOS Baseline; write both into record **before** reading anything current. Question: "when did it stop being what it was", not "how bad is rank now".
3. Pull daily rank series (D9) across **trailing 12 months** (D10 window); locate inflection = first date series leaves held band and does not return. Write to T2 Situation. Daily coverage -> exact date; otherwise weekly -> **+/-7 day interval** travels with every downstream comparison. Record which applies. Never average weekly into false daily date.
4. Loss magnitude in position classes (F6): **AT = at/under target; NEAR = target to target+10; MID = 11-30 absolute; FAR = above 30; UNRANKED**. Record the class transition.
5. Read T2 Velocity (pos/wk) and 4-week trend. SLIPPING = outside FLAT +/-1 pos/week. Still slipping = live cause; fell and stabilised = resolved/one-time cause (different P5 windows).
6. Open T5 Product Log filtered to inflection date +/- interval. List every event across all **eight closed event types**, none excluded. Read the window, do not search for a confirming entry.
7. Empty window: say so. Evidence, not absence: removes four of seven classes, points at competitor surge or taper too deep (neither produces a T5 entry).
8. Write the attribution statement: one line naming inflection date, interval, position-class transition, events in window, classes admitted/not admitted. PPC neither credited nor blamed until it exists.

### P2. Cause classification against the seven classes. 20-30 min. Exactly one primary cause, or UNKNOWN.
1. **Price first, always** (D6). T2 Price Competitiveness Flag (our side) and SQP median market price (market side). D3 MISSING -> compute limb you can, name the limb you cannot, carry gap to step 7.
2. **OOS.** Compare inflection date to T5 stockout window on the targeted variation. Directional: inflection **inside** window admits; inflection **before** window rules out; stockout starting after rank fell is coincidence.
3. **Listing event.** T5 listing/image/A+/eligibility events; re-read G5 as evidence (Indexed? = no or Listing Placement = backend is a cause). F4: CVR/CTR PROVISIONAL 14 days after main-image or price-adjacent change; conversion read inside that window not admissible as counter-evidence.
4. **Review shock.** Review Position Gap; FAR-BEHIND (<50% top-5 median count or >=0.3 stars below) fails O3 competitor-credibility outright = bar on funding while it holds.
5. **Competitor surge.** T2 Competitor Depth (D8) for deal window, launch, price cut, review surge on top-10 holder; run E1 decomposition (D7) before any aggressiveness verdict. D8 MISSING -> evidenced only from manually logged T5 competitor entry; absence is coverage gap, not negative finding.
6. **Deal hangover, then taper too deep.** T5 deal window with trend-exclusion flag: dip inside settle = #32 hangover; stop, record TRANSIENT (F13), hand to P5 observation only. Then T6 for dated ladder step at inflection, and #37 rule change log for automated step vs stale target. Inflection on our own ladder date = taper too deep; remedy is a rung.
7. Name one primary cause with evidence, or UNKNOWN. Two classes fit -> the one with dated artifact wins; other recorded as contributing condition (two primaries score nothing at P14). No evidence -> UNKNOWN, route to P3 deeper read, not default push. Untestable due to missing feed -> write **"not testable"**, never "not found" (manifest finding vs diagnostic conclusion).
8. Write into T2 Situation every gap ridden over: unevidenced price limb (D3), competitor limb (D8), weekly-resolution date (D9), provisional margin (D1). G8 requires stating what it could not see; hiding a fallback is a process violation under v4.0 Section 13.3 rule J7.

### P3. Confound and void determination. 8-12 min per loss and per in-flight read. Source: G10, Section 8.12 S-E5. Consumed by SOP-06 and #35 by name.
1. Test dating window and read window separately (confound on inflection date corrupts diagnosis; on checkpoint corrupts score; record which).
2. Apply G10: event weeks + 14 days following excluded. Read T5 Trend-Exclusion Flag and T2 Event Mode across both windows; compute guard end date explicitly.
3. Confound inside a read window -> read is **VOID, not MISS**.
4. Classify the confound (the **five confound classes this SOP publishes**):
   - event or deal window (G10)
   - competitor deal window (S-C5)
   - price test in progress (G9)
   - listing change inside 14 days (F4)
   - stockout on an adjacent variation shifting traffic mix (S-I6)
5. Rank reached inside an armed window -> S-E5: achievement provisional; two-week at-target clock under T1 starts only after exclusion window closes; no taper on event spike.
6. Hand void and class references to #6 (score) and #35 (where incrementality read rode same window).
7. Confound voids a read -> re-date checkpoint to guard end rather than deeming recovery failed. v4.0 has no re-dating rule or ceiling extension; extension recorded as input under test, **AM-5**.

### P4. Baseline restoration and its verification artifact. 10-25 min per resolved cause. No recovery spend deploys before this closes.
1. Restore by class: stock landed; price back to PAR or better on PPI; listing edit reverted/re-approved; suppression lifted; index confirmed; or ladder rung restored one step per M3 (rung value from #28).
2. Verify with an artifact per class, filed against record: inventory feed showing variation in stock and buyable; T5 price-move entry with restored value and PPI recomputed; listing owner's confirmation with live page state; eligibility flag = eligible; or T6 row with restored rung and prior/new values. No artifact = F1 condition.
3. Competitor surge: nothing to restore. Record "resolved-by-nothing"; go to O3 credibility retest at P6. Funding against a permanent competitor price cut = a subscription.
4. Deal hangover: restoration is the calendar. Record settle expiry date and hold; do not restore, size or open before that date.
5. Re-run G9: a price restoration is itself a price change inside trailing 7 days; CVR/ACOS PROVISIONAL; reason P5 reads rank not rate.
6. Listing/indexing fix: re-verify G5 rather than assume propagation. No re-check interval in v4.0: input under test, **AM-9**.
7. Write restoration record to T5 as dated event and to T6 with verification artifact referenced.

### P5. Observation window and self-recovery test. 5 min to open, 10 min to read.
1. Open window on restoration date; read **rank only** (rates PROVISIONAL under G9 / F4).
2. Some losses recover on restoration alone; test is whether velocity turns positive without spend.
3. At window close, three outcomes vs pre-OOS baseline:
   - recovered to baseline -> no recovery funds; term returns to standing objective;
   - moving toward baseline at positive velocity -> window **extends by one read**;
   - flat or still slipping -> proceed to P6.
4. AMENDMENT: no per-cause-class window in v4.0. F13 (syntax grain): **TRANSIENT 1-2 weeks, DEVELOPING 3 weeks, CHRONIC 4+ consecutive weeks**; T5 sets daily rank checks for 3 weeks on post-restock mode. Window used for other classes = input under test, **AM-2**.
5. OOS class is the governed exception: F3 triggers recovery play at restock confirmation; P11 deploys day 0; P5 does not run.
6. Window closes with rank recovered -> still score the diagnosis at P14.
- Verdict while under observation: HOLD; DEFEND LIGHTLY AT RANK (logged as a verdict).

### P6. Recovery classification and ceiling inheritance. 8-12 min. Source: D10, F6.
1. Confirm class SOP-23 assigned (do not re-derive). **D10**: every FAR or UNRANKED term is **RECOVERY** where best rank <= 10 within trailing 12 months or pre-OOS baseline <= 10; **PROVEN** where that rank <= 5; **NEVER-RANKED** otherwise. If SOP-23 has not classed it, read T2 Best Rank (Hist) + Date, apply D10, record that SOP-24 did so.
2. Note corpus divergence: KDR v3.0 defines recovery zone as "within 10 of Best Rank" citing S-R12; v4.0 F6 = best rank <= 10 absolute, and S-R12 is ADD EXACT + RESTRUCTURE with RECOVERY scenario at S-R13. Identifier half = C17 (v4.0 governs). Definitional half = **AM-13** (on a best rank of 24 the tests disagree completely).
3. Inherit proven ceiling: RECOVERY-class skips cold-start realism penalty; carries CPC and CVR at which it previously held position, from T2 Pre-OOS Baseline and T4 floor register.
4. Re-test O3 clauses vs baseline state (S-R13: fundamentals intact or better vs baseline period): indexing and placement (G5); purchase intent; CVR at/above benchmark with source recorded; competitor-credibility pair (Review Position Gap not FAR-BEHIND; PPI not OUTPRICED); inventory GREEN; on THIN margin-dollar variations **Expected CPC <= margin dollars / 3**.
5. Any clause moved against us -> downgrade to NEVER-RANKED realism for sizing; record the clause.
6. Write class, inherited ceiling, re-tested clauses to T2 Situation.

### P7. Recovery-adjusted sizing: three adjustments to SOP-23 worksheet. 15-20 min. Source: S-R13, S-I5 (M2 sizing against proven ceiling).
1. Assemble M2 inputs into T2 exactly as SOP-23: current rank, target or baseline rank, DSTR at target, validated CVR, Expected CPC, contribution per order (T0 zone C), current daily orders. Compute order gap, required clicks/day, required spend/day, duration, total budget, weekly loss ceiling.
2. **Adjustment 1, target**: size toward pre-OOS or best-rank baseline, not standing target. Where different, write both and state which duration used.
3. **Adjustment 2, velocity**: recovered terms move faster (relevance retained). AMENDMENT: no recovery velocity reference in v4.0; v1.0's 2.0 positions/day traces to no source. Record as input under test, log vs **AM-1**. WE-1: $1,592.96 planned-spend difference.
4. **Adjustment 3, bid seeding**: bracket = [previously discovered floor (T4 register), prior push CPC (T6)]. Bracket is a test, not a generator: Expected CPC under M2 supplies seed; bracket confirms seed is inside demonstrated range. Seed outside bracket = finding to explain. AMENDMENT: no rule for value inside bracket, **AM-7** (WE-1 bracket spans $0.55 = $34.63/day at 62.96 clicks/day = $415.56 over 12 days).
5. Ceiling read: Max Profitable CPC = contribution x CVR; ratio = Expected CPC / Max Profitable CPC. F1 bands (below). Above 1.5 inside a sized recovery -> S-R10 cheap-surface arbitrage check mandatory this cycle at **0.6x** threshold; recorded whether or not it fires.
6. Recovery ACOS must sit inside the **50-80% ranking envelope** (F1 outer band); outside = sizing failure, return to step 1.
7. Elasticity correction: M2 amendment corrects click requirement by observed Rank Response Elasticity once **8+ weeks** of push history exist; use wherever available.
8. State what worksheet could not see: provisional margin (D1), unevidenced DSTR (D8), account-reference Expected CPC (A6), baseline CVR standing in for validated read (G2). J7: confidence theater is a process violation.
9. Decision confidence score from three drivers vs F15: **HIGH >= 75; MEDIUM 50-74; LOW < 50**. LOW: M10 bars pushes outright, halves every step, shortens review horizons to one week; D9 limits verdicts to extend-test, data-repair tasks, gate-driven actions. **LOW-confidence recovery does not proceed to P8.**
10. Version worksheet into T2 plan block; later decisions cite it by version.

### P8. Queue submission and funding decision under product posture. 5-8 min.
1. M5 ordering inputs: revenue potential at baseline rank / cost-to-close-gap. Write T2 Cost to Close Gap $. D10: RECOVERY terms funded at better M5 priority as a consequence of the shorter denominator, not a separate bonus (applying twice double-counts).
2. Read product posture: S-A3 push freeze grants no new Ranking objectives. S-A4 Recovery Mode: R3 permits new Ranking objectives only on RECOVERY-class terms at HIGH confidence (single exception to code-red funding freeze; P6 class + P7 confidence authorize it).
3. S-A10: CONSTRAINED earning-potential class bars ranking pushes; routes velocity to deals and pricing. Tiering outside corpus (C6); stop at boundary.
4. G11: sibling holds/contests term -> both restore steps hold until #33 declares lead; supply recovery class and cost-to-close.
5. Submit worksheet to queue in T0 zone H and, for family arbitration, Account Rollup tab A2 (name instrument and tab, never a #31 procedure).
6. On release, read dated release and proceed to P11. No dated release = no recovery; spend drifting toward baseline without one = SOP-23's F1 unfunded-drip condition; S-R11 answers with immediate ladder toward ceiling.

### P9. Pre-OOS taper overlay (proactive). Same day on RED flip, 15-25 min. Source: S-I3, F3.
1. Confirm trigger: projected stockout **<= 14 days** on targeted variation, computed by formula from days on hand, max-sales-day velocity, incoming POs with arrival estimates and lead time; never eyeballed.
2. **Write pre-OOS baseline snapshot first, before any bid moves**: rank, CVR, CPC per keyword (S-I3) to T2 Pre-OOS Baseline. It is the recovery contract; without it the term is misclassified NEVER-RANKED next candidacy. "Single highest-leverage step... costs two minutes."
3. Taper toward defense rather than stopping. Request rung values from #28 and stage. Campaign stays live at floor, not paused (rank memory holds better on a taper than a hard stop).
4. AMENDMENT: S-I3 "taper to defense on the variation's terms" sets no rung count, interval or floor; depth = input under test, **AM-10**.
5. Re-point ranking campaigns to declared ranked backup variation same day per L9, bid seeded at backup's Expected CPC. Issue RE-POINT VARIATION, hand execution to SOP-12. No D2 backup chain -> not executable; record as blocked verdict class against D2 manifest row.
6. Pre-build recovery worksheet (P6, P7) during outage.
7. Log planned recovery standup against restock date in T6, with pre-built worksheet version. Write taper, snapshot, re-point and planned standup as one dated chain.

### P10. Stockout window hold. 10-15 min, then standing daily check.
1. S-I4: defensive floor only on branded terms; all push and share objectives to Paused-pending, re-entry "restock confirmed". Issue PAUSED-PENDING (REASON + RE-ENTRY) with both fields; one field = incomplete.
2. Mark trend windows for exclusion (S-I4 requires, G10 mechanism).
3. Stop spend into unbuyable offer same day. Test is **buyability** not eligibility (offer can read eligible under G4 while buy box lost or variation unorderable). AMENDMENT: no buy-box/buyability gate in v4.0; SOP's method, **AM-11**.
4. Read restock estimate daily vs T2 Days to Stockout and inventory feed; update planned standup date in T6 on movement.
5. If outage extends past the point at which pre-OOS baseline ages out of D10's 12-month window, flag: term on a clock to lose RECOVERY class; route to inventory owner with funding-priority consequence quantified.

### P11. Post-restock standup at day 0. Same day as landing, 25-35 min incl. staging. Source: F3, S-I5.
1. Deploy the day stock lands. Quantify drift: each day of delay = order gap x contribution per order (WE-1: **$95.20/day**). Write into T6 on any delay.
2. OOS class: P4 restoration and trigger are same event; P5 does not run.
3. Buyability check: offer live, buy box held, variation orderable, verified with artifact (AM-11).
4. G6 must read GREEN (not merely not-RED): restock below lead time + 21 days cover at max-sales-day velocity funds into the next stockout.
5. Reverse re-point to primary variation per L9; stage re-point and recovery bid in one set.
6. Standup order to SOP-12 carries **five values** from pre-built worksheet only: campaign; re-entry bid; daily budget = required weekly budget / 7; objective tag; ETA checkpoint date. No invented bid; creation with no verdict-carried bid returns incomplete.
7. Bidding strategy fixed (Strategic Doctrine v1.0 Section 6.3: fixed for ranking pushes; April 2026 platform bidding change weights placement-level conversion probability more aggressively, with category CPC inflation reported at **18-27%** vs Q1 baselines under dynamic raises).
8. Walls intact under #29 in same working session.
9. Exclude honeymoon-window reads per S-I5; mark exclusion in T5.
10. Cadence per T5: daily rank checks for 3 weeks; ETA checkpoint at 3 weeks (S-I5, S-R13). Write T6 prediction row now: metric, direction, magnitude, horizon, review date.
11. Deploy via #38 with T+1 verification; recovery not started until diff proves it landed.

### P12. Compressed in-flight verification. Daily for 3 weeks, 6-10 min each. Source: T5, V4.
1. Daily rank series vs worksheet velocity line; plot realized positions/day. Weekly-only D9 -> coarser interval stated; never fabricate daily read.
2. Pacing: T2 In-Budget % and cumulative spend vs daily line. **< 70%** = truncated (G3): budget lever first; week's bid read void.
3. Loss line: cumulative spend minus orders x contribution vs dated weekly ceiling. Surface the number; scenario call is v4.0's.
4. Re-read gates that are also cause classes (eligibility, inventory band, price stability, event mode). Any flip routes back to P2.
5. AMENDMENT (corrects v1.0): no day-7 or day-4 checkpoint in v4.0; governed cadence = daily for 3 weeks, ETA checkpoint at 3 weeks. Interval at which flat series becomes a diagnosis miss: **AM-12**.
6. No bid changes here. Pacing interventions touch budget only. Every intervention writes a T6 line.
7. Run P3 on every read.

### P13. Recovery close: taper handoff, renewal, or downgrade. 15-25 min. Source: S-I5, S-R13, S-R16, T1, T5.
1. Read both exit tests: T5 exit at **baseline reached**; S-R6 taper trigger and T1 objective transition at **2 consecutive weeks at/under target rank**. No precedence in v4.0; read both, write both, **route on the stricter** until AM-4.
2. Baseline reached and target held 2 consecutive weeks -> TAPER: RANK ACHIEVED, STEP BIDS DOWN; hand to SOP-12 and #28 ladder. SOP-24 supplies achievement date, recovery bid, worksheet reference only.
3. Retag objective per T1: update T3 tag and campaign-name objective segment in same staged set. Term exits into SOP-25 normalization.
4. Checkpoint reached, baseline not held, velocity > 0 -> S-R16 renewal decision (never automatic): re-size on realized velocity, apply M5 to re-sized figure; renew only if re-sized cost-to-close still clears priority vs current queue.
5. Checkpoint reached, velocity at/near zero after required clicks delivered -> S-R5 stop-loss -> STOP-LOSS: CONCEDE OR DEFER. Confirm **all three** S-R5 conditions, and that top-of-search read at S-R7's **30% floor** ran first.
6. Downgrade: S-R13 recovery failure -> NEVER-RANKED realism (also T5's second exit). Write to T2 and to record SOP-23 reads.
7. Any close other than baseline reached -> freed daily budget returns to envelope, reallocated at instrument layer same cycle. No cool-down before re-entry: **AM-14**.
8. Every outcome writes a T6 row with its arithmetic. A renewal without the re-sized number is not a renewal.

### P14. Post-mortem, diagnosis scoring, serial-recovery escalation. Every closed recovery, 25-35 min. Source: V1, V5, SOP-06 rubric.
1. Score standup prediction **HIT / PARTIAL / MISS / VOID** vs named horizon; write T6 V5 Score. P3 confound -> VOID with class.
2. Cause tag on every non-HIT (#6 rubric): **JUDGMENT, EXECUTION, WORLD, DATA**. EXECUTION routes to #38, never to decider's calibration.
3. Score diagnosis separately: did rank hold after close? Hit rank then lost it within review period = HIT prediction, MISS diagnosis. Write both.
4. Three calibration deltas separately: realized vs assumed velocity; realized vs assumed CVR; realized cost vs budget. Velocity error attaches to AM-1.
5. Feed realized rank movement per 100 incremental clicks into elasticity series (M2 correction at 8+ weeks).
6. Failure on a condition a missing feed made unfixable -> attach finding to that T7 field group row with dollar figure.
7. Serial-recovery test: read T6 for prior closed recoveries on same term. Repeated losses = product/price/competitive problem "wearing a PPC costume" -> structural review routing cause records out of PPC (as SOP-26's structural close). D6: PPI precedes any listing spend. No count/window in v4.0; count used = SOP's stated method, **AM-6**.
8. V5: any rule **< 50% accuracy over 10+ scored predictions** enters review -> amendment, threshold change, or documented defense. Applies to cause classes too.
9. Closed recovery with no post-mortem = F7.

## 5. Rules, thresholds and numbers

### 5.1 Numeric values

| Item | Value | Source |
|---|---|---|
| PPI bands (F5) | ADVANTAGED < 0.92; PAR 0.92-1.08; PREMIUM 1.08-1.25; OUTPRICED > 1.25 | F5 |
| Review Position Gap FAR-BEHIND (F4) | < 50% of top-5 median review count, or >= 0.3 stars below | F4 / E11 |
| Listing-change provisional window | 14 days (CVR, CTR PROVISIONAL after main-image or price-adjacent change) | F4 |
| Event exclusion | Event weeks + 14 days following | G10 |
| Deal hangover persistence | TRANSIENT 1-2 weeks | F13 |
| Persistence classes | TRANSIENT 1-2 wks; DEVELOPING 3 wks; CHRONIC 4+ consecutive wks (syntax grain) | F13 |
| Position classes | AT <= target; NEAR target to target+10; MID 11-30 absolute; FAR > 30; UNRANKED | F6 |
| Velocity FLAT band | +/-1 position per week; outside = SLIPPING | F6 |
| Pre-OOS taper trigger | Days to Stockout <= 14 projected | S-I3, F3 |
| GREEN inventory | Days on hand > lead time + 21 days at max-sales-day velocity | G6 / F3 |
| YELLOW inventory | Freezes recovery spend at current level | S-I2 |
| Sufficiency | >= 15 clicks/7d bid read; >= 100 clicks for CVR; fallback 60-day window | G2 |
| In-budget | >= 70% (below = TRUNCATED). KDR alias: 51-70 "strained" | G3 |
| Pacing | within 25% of day-of-week curve | G7 |
| Packet completeness | < 85% = DEGRADED; live read 0.571 | G8 |
| Price stability | no price change in trailing 7 days | G9 |
| MKL staleness | not stale past 30 days | G12 |
| D10 lookback | trailing 12 months | D10 |
| RECOVERY / PROVEN / NEVER-RANKED | best rank (12 mo) or pre-OOS baseline <= 10 / <= 5 / otherwise | D10 |
| THIN margin O3 clause | Expected CPC <= margin dollars / 3 | O3 |
| CPC/ceiling ratio bands (F1) | <= 0.8 SAFE; 0.8-1.0 AT-CEILING; 1.0-1.5 PUSH-ONLY; > 1.5 UNJUSTIFIABLE outside a sized push | F1 |
| Cheap-surface arbitrage check | Mandatory above 1.5x ceiling inside sized recovery, at 0.6x threshold | S-R10 |
| Ranking ACOS envelope | 50-80% | F1 |
| Elasticity correction | once 8+ weeks push history | M2 amendment |
| Confidence bands | HIGH >= 75; MEDIUM 50-74; LOW < 50 | F15 |
| LOW confidence effects | pushes barred; every step halved; review horizons one week | M10, D9 |
| Recovery cadence | daily rank checks for 3 weeks | T5 |
| ETA checkpoint | 3 weeks (day 21) | S-I5, S-R13 |
| Taper trigger | 2 consecutive weeks at/under target rank | S-R6, T1 |
| Top-of-search floor | 30% (PLACEMENT FIX FIRST fires below) | S-R7 |
| UNLOCK TRAFFIC | clicks < 15 in 7 days with healthy budget and GREEN inventory | S-R1 |
| Traffic deficit ETA re-check | 2 weeks | S-R3 |
| Rule accuracy review | < 50% over 10+ scored predictions | V5 |
| Standup daily budget | required weekly budget / 7 | P11 |
| Weekly loss ceiling | (recovery ACOS - break-even ACOS) x projected weekly sales; capped and dated | M2 |
| Max Profitable CPC | contribution per order x CVR | F1 / P7 |
| Category CPC inflation (April 2026 platform change) | 18-27% vs Q1 baselines under dynamic raises | Strategic Doctrine v1.0 s6.3 |
| Floor re-tests | Quarterly (V4) | V4 |
| Retired numerals (NOT governed) | 2.0 positions/day recovery velocity; day-4 checkpoint; third-recovery escalation count | v1.0, retired |
| SOP-23 cold velocity | 1.0 position per day (as used in WE-1 comparison) | SOP-23 |
| Time estimates | P1 12-20 min; P2 20-30; P3 8-12; P4 10-25; P5 5+10; P6 8-12; P7 15-20; P8 5-8; P9 15-25; P10 10-15 + daily; P11 25-35; P12 6-10 daily; P13 15-25; P14 25-35 | SOP |

### 5.2 Criteria System v4.0 rule IDs referenced

| ID | Meaning as described in SOP-24 |
|---|---|
| F1 | CPC-ratio bands and ranking ACOS envelope 50-80% |
| F2 | Records account standing state: ~20% blended TACOS vs mature-stage products = standing CODE RED |
| F3 | Inventory/recovery contract: pre-OOS taper at 14 days; recovery play triggers at restock confirmation; GREEN definition; rank-6 pre-stockout term is RECOVERY candidate |
| F4 | Review Position Gap bands; CVR/CTR PROVISIONAL 14 days after listing change |
| F5 | Price Position Index bands |
| F6 | Position classes, velocity bands (FLAT +/-1), recovery zone (best rank <= 10 absolute) |
| F13 | Persistence classes (TRANSIENT/DEVELOPING/CHRONIC) at syntax grain |
| F15 | Decision confidence bands |
| F16 | Listed among companions (no content described) |
| E1 | Decomposition splitting market vs self-inflicted inflation |
| E10 | Price Position Index |
| E11 | Review Position Gap |
| X1, X4, X5, X8, X10 | Listed among companions; X10 = share threshold above which auto and broad carrying a term triggers structure repair |
| X9 | Product log consulted before PPC is credited or blamed for any swing |
| X12 | Carries the incrementality mechanism |
| G1-G12 | Gates (table in Section 4) |
| O3 | Push candidacy gauntlet, incl. competitor-credibility clause (RPG not FAR-BEHIND, PPI not OUTPRICED), indexing, intent, CVR >= benchmark, inventory GREEN, THIN margin clause |
| O5, O7 | Listed among companions |
| D5 | Attribution check vs product log ahead of any lever explanation |
| D6 | Price check first in every conversion diagnosis; PPI precedes listing spend |
| D7 | E1 decomposition before any aggressiveness verdict |
| D9 | At LOW confidence, legal verdicts limited to extend-test, data-repair, gate-driven actions |
| D10 | RECOVERY/PROVEN/NEVER-RANKED classification; RECOVERY funded at better M5 priority |
| S-A3 | Push freeze: no new Ranking objectives |
| S-A4 | Enters Recovery Mode (code red) |
| S-A10 | CONSTRAINED earning-potential class bars ranking pushes; velocity routed to deals and pricing |
| S-C5 | Competitor deal window (worst comparison of the month) |
| S-I2 | YELLOW freezes recovery spend at current level |
| S-I3 | Pre-OOS taper to defense at 14 days; snapshot rank, CVR, CPC per keyword |
| S-I4 | Stockout: defensive floor on branded only; push/share objectives Paused-pending re-entry "restock confirmed"; mark trend windows |
| S-I5 | Post-restock recovery play conditional on pre-OOS baseline; ETA checkpoint 3 weeks; exclude honeymoon reads |
| S-I6 | Stockout on adjacent variation shifting traffic mix (a confound class) |
| S-R1 | UNLOCK TRAFFIC at < 15 clicks/7d with healthy budget and GREEN inventory |
| S-R3 | TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS; re-check ETA in 2 weeks |
| S-R5 | Stop-loss conditions (three) |
| S-R6 | Taper trigger at 2 consecutive weeks at/under target rank |
| S-R7 | Top-of-search 30% floor; PLACEMENT FIX FIRST outranks triad read |
| S-R10 | Cheap-surface arbitrage check above 1.5x ceiling, at 0.6x |
| S-R11 | Unfunded drift: immediate ladder toward ceiling (BID DOWN TO PROFITABLE CPC; CAP SYNTAX) |
| S-R12 | ADD EXACT + RESTRUCTURE: bars any performance verdict until exact stands up |
| S-R13 | Recovery push: M2 sizing vs proven ceiling, conditioned on fundamentals intact vs baseline; 3-week ETA; failures downgrade to NEVER-RANKED |
| S-R16 | Renewal decision at checkpoint (never automatic) |
| S-R1 to S-R16 | Section 8.4 listed as companions |
| S-E5 | Rank achieved during events provisional; T1 clock starts after exclusion window |
| L1, L2, L5, L9 | Levers. L2 per-change limit and floor; L9 re-point to backup variation and reverse re-point |
| M2 | Sizing chain; loss ceiling capped and dated; elasticity amendment |
| M3 | On slippage beyond tolerance, restore one step; that value = recorded minimum viable CPC |
| M5 | Queue ordering: revenue potential / cost-to-close |
| M10 | LOW confidence bars pushes, halves steps, shortens horizons |
| T1 | Objective transition at 2 consecutive weeks at/under target |
| T5 | Recovery mode: daily rank checks 3 weeks; exit at baseline reached; downgrade as second exit |
| T8 | Listed among companions |
| R1-R6 | Recovery Mode rules; R3 = new Ranking objectives only on RECOVERY-class terms at HIGH confidence, tightened confirmation thresholds; R4 = daily cadence |
| P1, P5 | Section 12 rules listed as companions |
| P8 | Data quarantine beats urgency |
| J7 | Hiding a fallback / confidence theater is a process violation (Section 13.3) |
| V1 | Unscored actions do not accumulate |
| V4 | Weekly full audit cadence; daily oversight-class checks during pushes; quarterly floor re-tests |
| V5 | Prediction scoring; rule-level accuracy review |
| V8 | Training corpus |
| C9, C10, C17, C18, C3, C6 | Ledger conflicts (see Section 10) |

## 6. Data inputs required

### 6.1 Command Workbook tabs and fields
- **T0** (read first): zone A product posture (push freeze / code red); zone C economics spine (AOV, contribution per order, break-even ACOS, Target ACOS, Max Acceptable, Expected CPC reference, margin table version, fresh/provisional state); zone H queue (available dollars, entry state FUNDED, dated release, queue submission).
- **T1**: syntax caps (read before T2).
- **T2** fields:
  - Rank block: Organic Rank; Best Rank (Hist) + Date; Pre-OOS Baseline (rank, CVR, CPC per keyword); OOS Overlay Flag; Velocity (pos/wk); ETA to Target (wks); ETA Checkpoint date.
  - Gates block: Inventory Band; Days to Stockout; Targeted Variation(s); Eligibility; Indexed?; Listing Placement; Event Mode; Flag: Zero-Quarantine; Validation State; Clicks 7/30/60d; Sample State; In-Budget %; Envelope Status; Margin $/Unit; Family Conflict; Term Owner (Family); Syntax Tags; Relevancy.
  - Cause evidence: Price Competitiveness Flag; Competitor Depth (D8) block; rating and review count; Review Position Gap.
  - Situation (attribution statement, cause record, gaps, class/ceiling).
  - Plan block (versioned worksheet); economics block (ceilings); Cost to Close Gap $; current bid.
- **T3**: objective tag.
- **T4**: Ladder State (step / date); Discovered Floor $ (floor register).
- **T5 Product Log**: eight closed event types including OOS start-end per variation, price move, listing / image / A+ change, eligibility flip, deal window (+ trend-exclusion flag), competitor entries (manual), targeting changes, fee-dimension changes; Trend-Exclusion Flag. Primary evidence surface.
- **T6 Decision Log** (append-only): predictions, ladder dates, prior push CPC, V5 Score, prior closed recoveries, restoration rows.
- **T7 Manifest**: Status column and completeness rollup.
- **Account Rollup tabs**: A1 (family term ownership source for G11), A2 (family-level queue arbitration), A3 (consumes post-mortems).

### 6.2 T7 manifest field groups (Catalog IDs) and live state
| ID | Content | Live state |
|---|---|---|
| A1 | Four-period comparability | MISSING |
| A3 | Pacing and in-budget (day-of-week curve) | PARTIAL |
| A4 | Sufficiency buckets | - |
| A5 | Threshold flags | - |
| A6 | Objective and per-term Expected CPC | (account-reference Expected CPC noted) |
| A7 | Eligibility | - |
| B1 | Indexing and listing placement | - |
| B3 | Rank pack | PARTIAL, head terms only |
| B7 | Placement modifier data | MISSING account-wide |
| B8 | Economics chain | PRESENT on blended margin |
| B11 | Market context / MKL | - |
| D1 | Per-variation margin | PARTIAL (G9 PROVISIONAL on every ceiling) |
| D2 | Keyword-variation map and backup chains | PARTIAL (blocks REPOINT VARIATION) |
| D3 | SQP median price | MISSING |
| D6 | Sibling view | PARTIAL |
| D7 | Decision log and V5 | - |
| D8 | Competitor depth | MISSING |
| D9 | Daily rank series | PARTIAL, head terms only |

### 6.3 External reports and feeds
- Daily rank series (D9), trailing 12 months.
- SQP median market price paid (D3) for PPI.
- Inventory feed (Economics and Context Pack): days on hand, max-sales-day velocity, incoming purchase orders with arrival estimates, lead time, restock dates, in-stock/buyable state; daily.
- Per-variation margin table (#41, monthly + event-driven) into T0 zone C.
- Competitor depth (D8): deal windows, launches, price cuts, review surges on top-10 holders.
- #37 rule change log (automation rules).
- #28 floor register with dated entries, rung values, reversion rule, exit-bid references.
- #32 armed windows, dates, settle marks, pre-window baseline snapshot.
- #33 family term-ownership declaration.
- SOP-26 product Recovery Mode state and R3 override set.
- SOP-25 descent schedule with dated rungs.
- Restoration artifacts from listing, pricing and review owners (live page state, restored price with PPI recomputed, eligibility flag, review-velocity plan).
- Buyability evidence: offer live, buy box held, variation orderable.
- Master Keyword List (syntax tag, relevancy, freshness <= 30 days).
- KDR Template v3.0 "Bands & Verdicts Reference" sheet and "Campaign Decision Record" tab (vocabulary).
- Staged change sets and T+1 diff from #38.

## 7. Outputs / artifacts

| Artifact | Produced by | Storage / retention | Downstream consumer |
|---|---|---|---|
| Attribution statement (inflection date, interval, position-class transition, log window) | P1 | T2 Situation with cycle date; through term's next candidacy | P2; next cycle's P1 |
| Cause record (one primary class + evidence, contributing conditions, "not testable" marks) | P2 | T2 Situation and T5 dated event; life of the term | SOP-06; #35; SOP-25 descent-slip diagnosis; the diagnosis engine |
| Void determination with confound class | P3 | T6 against affected read, guard dates computed | #6 (VOID not MISS); #35 |
| Restoration verification artifact | P4 | T5 dated event with artifact referenced; T6 for ladder-restore case | P11; F1 audit line; listing/pricing/review owners |
| Pre-OOS baseline snapshot (rank, CVR, CPC per keyword) | P9 step 2 | T2 Pre-OOS Baseline; at least trailing 12 months | P6; SOP-23 candidacy; D10 read |
| Pre-built recovery worksheet, versioned | P7 | T2 plan block; superseded versions kept for calibration | Instrument-layer M5; #28 CPC envelope; P14 |
| Queue submission with cost-to-close | P8 | T0 zone H; Account Rollup tab A2 | M5 queue; #33 |
| Standup record with prediction (metric, direction, magnitude, horizon, review date) | P11 | T6, append-only | SOP-12; #38; P14 |
| Daily rank and pacing lines | P12 | T6, one line per intervention; through close | P13; F9 coverage audit |
| Close record (taper handoff, renewal arithmetic, or downgrade) | P13 | T6 with realized figures; downgrade to T2 | SOP-12, #28, SOP-25, SOP-23, instrument layer |
| Post-mortem (prediction score, cause tag, separate diagnosis score, three calibration deltas) | P14 | T6 with V5 score; deltas retained indefinitely | P7 next recovery; V5; Account Rollup A3; V8 training corpus; T7 rows |

Gate artifacts: pre-funding = restoration verification artifact; in flight = daily rank line; at close = post-mortem with separate diagnosis score. No v4.0 retention period (AM-15).

**Skill-conversion outputs**: drafted attribution statements, cause records with not-testable marks, void determinations, pre-built worksheets with manifest-gap statements, standup packets, daily rank/pacing lines with drift-cost, close records with dual exit test, post-mortems, F1-F13 alarms. Alarm evidence-line format: row identifier, signal value, v4.0 rule/gate reference, artifact where read, routing tier.

**Campaign-level verdicts** (KDR "Campaign Decision Record"): FUND / HOLD / TRIM BUDGET, RAISE / CUT MULTIPLIER, NEGATION PASS, CONSOLIDATE, RETAG OBJECTIVE, PAUSE (L7), ARCHIVE. RETAG OBJECTIVE catches campaign still tagged Ranking after close (F11). PAUSE (L7) never applies to a pre-OOS campaign.

### 7.1 Full verdict-to-execution mapping (25 KDR strings + 2 v4.0 13.1 strings)
| Verdict (verbatim) | v4.0 13.1 cross-map | Recovery-stage execution |
|---|---|---|
| RECOVERY PUSH | None; v4.0 routes S-R13 into RANK PUSH AT CONTROLLED CPC | Primary verdict: P1, P2, P4 (artifact), P5, P6, P7, P8, P11. Only on resolved cause + artifact + RECOVERY/PROVEN class. SOP-12 v2.0 maps to S-R12; v4.0 S-R13 governs (C17). |
| RANK PUSH: FUND SIZED PUSH | RANK PUSH AT CONTROLLED CPC | Boundary; SOP-23's. Means term NEVER-RANKED; routes to SOP-23. If term holds pre-OOS baseline <= 10 -> F6 misclassification; re-test at P6. |
| RE-POINT VARIATION | Identical | P9 step 5 (same day RED flip, after snapshot); reverse at P11 step 5. Execution SOP-12; no D2 chain = blocked. |
| PAUSED-PENDING (REASON + RE-ENTRY) | PAUSE (LEVERS EXHAUSTED) | P10 step 1, re-entry "restock confirmed". Also on UNKNOWN cause: reason = untestable class, re-entry = feed that would test it. |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | TAPER TO FLOOR (POST-OBJECTIVE) | P13 step 2. Pre-OOS taper at P9 is NOT this verdict. |
| STOP-LOSS: CONCEDE OR DEFER | Identical | P13 step 5 (three S-R5 conditions + S-R7 read first). Concede downgrades to NEVER-RANKED; defer needs new worksheet. |
| FIX CONVERSION FIRST; DEFER PUSH | Identical | Conversion-deficit loss: cap at maintenance, route by funnel drop point (price first), re-entry at CVR back to benchmark. |
| QUARANTINE: DATA REFRESH | FLAG: DATA REPAIR | No dating/sizing on quarantined row; refresh task same day with owner and date. |
| EXTEND TEST | Identical | Most frequent G2 outcome; only legal verdict class at LOW confidence (D9). |
| ADD EXACT + RESTRUCTURE | Identical | S-R12: structure repair before recovery (exact paused during outage, or auto/broad carrying above X10 share). Execution SOP-12, walls #29. |
| PLACEMENT FIX FIRST | None; S-R7 verdict text | Below 30% TOS floor; bids hold; modifier program #28. B7 MISSING -> modifier half not executable; blocked verdict class on T7. |
| DEFEND AT FLOOR | Identical | Taper-too-deep remedy: M3 one-step restore ($6.60/wk vs $392.00 in WE-4). |
| HOLD; DEFEND LIGHTLY AT RANK | None; near-neighbour DEFEND AT FLOOR | P5 observation verdict. |
| CONTINUE; VERIFY MOMENTUM (v4.0) | Quoted from 13.1 | Live recovery tracking velocity line at P12 (C18). |
| PORTFOLIO CALL: ASSIGN LEAD (v4.0) | Quoted from 13.1 | G11 holds both restore steps until #33 declares (C18). |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Identical | S-R11 on unfunded drift (F1 unfunded-recovery condition). |
| UNLOCK TRAFFIC | Identical | S-R1 post-restock, clicks < 15/7d, healthy budget, GREEN. |
| FIX BUDGET (TRUNCATED) | None; G3 response | Budget lever only at P12 step 2; week's bid read void. |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | None; S-R3 verdict text | Named lever only on dedicated campaign via SOP-12; never both levers on one row in one cycle; ETA re-check 2 weeks. |
| ENTER SBV ARBITRAGE | FORMAT SUBSTITUTION (SBV/SD) | Mandatory check at P7 step 5 above 1.5x; SOP-24 executes only the SP-exact single ladder step down; video build = components 17-19. |
| INCREMENTALITY LADDER | None; mechanism at X12 | Owned by #35 and SOP-26; voids hand to #35. |
| CONSOLIDATE DUPLICATES | Identical | Boundary; SOP-12 P7, survivor selection human-mandatory. |
| GRADUATE FROM DISCOVERY | GRADUATE + STEER | Boundary; #30. Harvest never stops; graduate mid-recovery stood up and walled same day. |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | CUT / NEGATE | Boundary; #29. |
| OPEN / ROTATE / EXIT CONQUEST | Identical | Boundary; #16. Recovery never the vehicle for conquest. |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Identical | Boundary; routes to EXTEND TEST. |
| FUND TEST (UNFUNDED PRIMARY) | FUND DELIBERATE TEST (50-CLICK CAP) | Not issued here; no rank history = #30 or SOP-23. |
| LEAVE TO HARVEST | Identical | Boundary; #30. Diagnosis closes as recorded. |

Retired v1.0 strings (Section 5.2): RANK PUSH: RECOVERY PUSH; HOLD FOR OBSERVATION; TAPER (PRE-OOS); RETURN TO DIAGNOSIS.

## 8. Decision rights

Drawn from PPC Authority Matrix v2.0 Section 1.

| Matrix row | Rights |
|---|---|
| Weekly verdicts (established US) | PPC Lead decides; operator and PPC Manager execute assigned scope; brand-management owner reviews in daily huddle (review, not veto; disagreements route up) |
| Push funding (the M5 queue) | CEO decides above the envelope; PPC Lead within it; operator executes |
| Structure creation (all SOPs) | PPC Lead decides (or per SOP scope); operator executes; every creation on a funded recovery human-mandatory at deployment |
| Bulk deployments (#38) | PPC Lead reviews; operator and PPC Manager execute |
| Sibling declarations (S-series) | PPC Lead decides; operator executes; brand-management owner reviews |
| Event plans (#32) | PPC Lead decides with deals calendar owner; operator executes |
| Code-red declaration and close | PPC Lead decides; operator and PPC Manager execute |
| Terminal and LTSF PPC lane | PPC Lead decides with LTSF owner; operator executes; brand-management owner reviews |

- **Executable with audit (skill/operator)**: loss dating and inflection search, cause-evidence assembly, void determination, drift-cost quantification, pre-built worksheet during outage, daily pacing and rank lines, re-sized renewal arithmetic, post-mortem deltas.
- **Human-mandatory**: cause confirmation and restoration sign-off; funding decision; standup; every deployment confirm; shared-term restore step; downgrade to NEVER-RANKED realism; F4 structural escalation.
- Vacancy rule: unfilled role's decision right reverts to PPC Lead, execution to PPC Manager.
- Recovery Mode tightens confirmation thresholds per R3; no Recovery-Mode discount on human-mandatory tier.
- Restoration owners: listing owner, pricing owner, brand-management owner (reviews), inventory owner.
- Operator ramp: week 1 observe, week 2 supervised (checkpoint holder reviews), week 4 unsupervised audited. Ten live-defense questions (Section 11.1).

### Cadence
- Daily: rank-loss scan on every held term; pre-OOS trigger watch on every ranked term's variation; in-flight rank and pacing for 3 weeks per live recovery.
- Same day: RED flip and P9; stockout hold; restock standup at day 0; eligibility flips; product posture changes.
- Weekly: cause classification and observation reads inside the **Monday** cascade; deployment **Tuesday** per #38; T+1 verification **Wednesday**.
- 3-week checkpoint: P13. On close: post-mortem. Per review period: serial-recovery read across T6. Quarterly minimum review alongside V4 floor re-tests.

### Failure modes and alarm routing
| ID | Failure | Routing |
|---|---|---|
| F1 | Recovery deployed before cause resolved (no P4 artifact, or cause UNKNOWN) | Same day operator queue; escalates on discovery |
| F2 | Waiting out the restock (drift $95.20/day on WE-1) | PPC Lead with T6 history |
| F3 | Cold sizing on a recovery ($1,592.96 on WE-1) | Weekly worklist |
| F4 | Serial recovery without escalation ($4,137.78 in WE-4) | PPC Lead; escalates by definition |
| F5 | Spend into unbuyable offer | Same day; escalates same day on first occurrence with spend quantified (emergency class) |
| F6 | Recovery misclassified as cold start | PPC Lead |
| F7 | Closed with no post-mortem or no diagnosis score | PPC Lead |
| F8 | Confound filed as MISS | Weekly worklist |
| F9 | Diagnosis on stale/unavailable rank series | Weekly worklist |
| F10 | Recovery funded during push freeze or outside R3 exception | Same day; escalates on discovery |
| F11 | Objective retag missed after close | Weekly worklist |
| F12 | Pre-OOS baseline never written | Same day; standing weekly audit line on every RED/YELLOW variation |
| F13 | Restored rung read as market loss | Weekly worklist |
Any mode occurring twice in consecutive cycles on same scope escalates to PPC Lead with T6 history.

## 9. Account-specific facts

- **T7 packet completeness 0.571**, below the 85% G8 DEGRADED floor.
- Field groups: **D3 SQP median price MISSING; D8 competitor depth MISSING; D9 daily rank series PARTIAL (head terms only); D2 keyword-variation map PARTIAL (blocks REPOINT VARIATION); D1 per-variation margin PARTIAL (G9 PROVISIONAL on every ceiling); A1 MISSING; A3 PARTIAL; B3 PARTIAL head terms only; B8 PRESENT on blended margin; D6 PARTIAL; B7 MISSING account-wide.**
- **Bamboo root ownership left OPEN at cycle 1** (live G11 / I-8 instance).
- v4.0 F2 records standing state: **roughly 20% blended TACOS against mature-stage products = standing CODE RED** on multiple products (makes R3 exception live).
- v4.0 Section 16 **Worked Pass 3** (live instance): head term at **74,000 search volume with zero exacts, two autos carrying 78% of its clicks, rank 22 vs target 5, best rank 7 fourteen months ago pre-OOS**.
- Data Architecture: first cycle logged a **126-against-101 rank disagreement** between sources, correctly filed as a flag (F9 instance).
- SOP-23's F2: a head term fell from **rank 7** across a stockout and was later mistaken for a cold start (F12 instance).
- SOP-26's F11: one automation rule stepped a defensive term **six rungs** against a stale target, nothing alarmed (each step inside its own limit).
- v1.0 recorded five account incidents (F1-F5); WE-1 is "the v1.0 incident" (king variation OOS 9 days).
- External dependency D1 (per-variation margin) open; caps this component. Dependency D3 (#28) OPEN.

### Worked examples (training base, not live economics)
Training base: **AOV $80.00, contribution $28.00/order, break-even ACOS 35.0%, Target ACOS 17.5%, Max Acceptable 26.3%**. WE-1 DSTR anchor from Economics Worked-Example Set case E3; WE-4 floor anchor from case E5.

- **WE-1 clean post-OOS recovery**: king variation OOS 9 days; held rank 7, reads 31 at restock; target 8. Snapshot rank 7, CVR 5.4%, CPC $2.40; floor $1.85. Distance 23; DSTR at rank 8 = 4.0 orders/day; current 0.6; gap 3.4; clicks/day 62.96; seed $2.30 inside [$1.85, $2.40]; spend/day $144.81; $1,013.70/wk; 12 days at 2.0/day (input under test); total $1,737.78; contribution $95.20/day; loss/day $49.61, $595.38 total; ACOS 53.24%; 18.24 pts above BE; weekly sales $1,904.00; weekly loss ceiling $347.30; Max Profitable CPC $1.51; ratio 1.52x -> S-R10 check at $1.38. Cold sizing at 1.0/day: 23 days, $3,330.74, loss $1,141.14 -> saving $1,592.96 spend, $545.76 loss. Day 4: rank 24 (1.75/day). Day 12: rank 8, 1.92/day (95.8%). Stability window 14 days: +$2,027.41 spend, +$694.61 loss; cumulative loss by day 26 $1,289.99. Close day 26; HIT; deltas velocity 1.92 vs 2.00, CVR 5.38% vs 5.40%, cost $1,681 vs $1,737.78.
- **WE-2 dating overturns cause**: held rank 6 for 11 weeks, reads 22; 6-day stockout on secondary variation; inflection Tuesday, stockout Saturday = 4 days before -> OOS ruled out. Price $79.95 unchanged; D3 and D8 MISSING; Review gap PAR. Verdict UNKNOWN -> PAUSED-PENDING, reason "cause UNKNOWN; D3 and D8 unavailable", re-entry "Price Position Index computable and at or better than PAR, or a dated competitor event in T5". Wrong-call cost: distance 16; DSTR at 6 = 5.0; current 2.1; gap 2.9; clicks 60.42/day at CVR 4.8%; CPC $2.60; $157.08/day; 8 days; $1,256.67; contribution $81.20/day; loss $75.88/day, $607.07; ACOS 67.7%; MPC $1.34; ratio 1.93x. $1,256.67 attached to D3/D8 T7 rows.
- **WE-3 confound**: bamboo head term rank 25 vs baseline 6; distance 19; DSTR 5.0; current 1.4; gap 3.6; CVR 5.2%; clicks 69.23; CPC $2.15; $148.85/day; 10 days; $1,488.46; contribution $100.80/day; loss $48.05/day; ACOS 51.7%; MPC $1.456; ratio 1.48 (PUSH-ONLY, S-R10 not fired). Deal window days 9-13; guard to day 27; checkpoint day 21 -> VOID. Re-dating 6 days = $893.08 spend, $288.28 loss (AM-5).
- **WE-4 serial recovery / taper too deep**: three recoveries: $1,737.78, $980.00, $1,420.00 = $4,137.78. Loss 2 actually taper too deep: floor $2.24 probed to $2.02 (9.8% step, inside M3 and L2 limit, above L2 floor); rank 4 -> 9. M3 restore $2.02 -> $2.24 (10.9%); at 30 maintenance clicks/wk = $6.60/wk. Sized recovery: DSTR at 4 = 4.4/day; current 3.1; gap 1.3; 25.0 clicks/day at $2.24 = $56.00/day = $392.00/wk. Difference $385.40/wk, factor 59.4, annualized $20,040.80. Floor register returns to $2.24; $2.02 marked failed probe.

## 10. Open items

### 10.1 Amendment register (AM-1 to AM-15) for v4.1
| ID | Gap | Where it bites |
|---|---|---|
| AM-1 | No recovery velocity reference (v1.0's 2.0/day unsourced); also no rank-loss detection threshold/interval. Highest priority | P7 step 3; trigger table; all WEs |
| AM-2 | No observation window per cause class | P5 step 4; Section 2 |
| AM-3 | No interval between restoration artifact and observation start | P4 step 7; Section 2 |
| AM-4 | Two exit tests (baseline reached vs 2 weeks at target) with no precedence | P13 step 1; WE-1 |
| AM-5 | No re-dating rule when G10 suppresses checkpoint read; no ceiling extension | P3 step 7; P13; WE-1; WE-3 |
| AM-6 | No recovery count or window for serial-recovery escalation | P14 step 7; F4; WE-4 |
| AM-7 | Bid-seeding bracket constrains without determining | P7 step 4; WE-1 |
| AM-8 | No max lag from funding release to standup outside restock case | Section 2; P11 |
| AM-9 | No re-check interval after indexing/listing restoration | P4 step 6 |
| AM-10 | No depth, rung count or interval for pre-OOS taper | P9 step 4 |
| AM-11 | No buyability (buy box / orderability) gate | P10 step 3; P11 step 3 |
| AM-12 | No interval at which a flat recovery becomes a diagnosis miss | P12 step 5 |
| AM-13 | Recovery-zone defined two ways (KDR "within 10 of Best Rank" vs v4.0 best rank <= 10 absolute) | P6 step 2 |
| AM-14 | No cool-down before a downgraded term re-enters queue | P13 step 7 |
| AM-15 | No record retention period (duplicates prior sessions' items) | Section 8 |

### 10.2 Ledger conflicts referenced
- **C3**: #31 has no procedural document; "#31 / P1.4" is one of five dangling citations; name instrument and tab instead.
- **C6**: LTSF/terminal tier deciding document sits outside corpus.
- **C9**: Gate numbering aliases between v4.0 and operating corpus (G9, G10, G12).
- **C10**: KDR verdict vocabulary quoted verbatim.
- **C17**: S-R12 vs S-R13 identifier inversion (SOP-12 v2.0 Section 5 still maps RECOVERY PUSH to S-R12; Data Architecture Section 6.1 maps zero-exact structure filter to S-R13 where v4.0 assigns S-R12).
- **C18**: KDR 25 lacks "working recovery continuing" and "family-level lead assignment"; v4.0 13.1 quoted in place.
- Ledger conflicts C1 to C23 cited in companions.

### 10.3 Reported findings beyond pre-declared list (Section 13)
1. Recovery-zone definitional divergence (AM-13), reported for registration.
2. #28's Ledger row names #24 among taper deciders (with #12 P4, #23, #25, #26) but its 22 interface contracts carry rows for #23, #25, #26 and none for #24; reciprocal rows owed at #28's next increment.
3. SOP-12 v2.0 Section 5 C17 instance located (still present).
4. Data Architecture Section 6.1 inversion in opposite direction (within C17 scope).
- Pack-state note: version note recorded Ledger at v2.5 with Wave 5A open on four rows; Ledger actually reads v2.8; this row closes wave at v2.9.

### 10.4 Interface contracts (I-1 to I-18)
Upstream: I-1 SOP-23 (pre-OOS baseline, D10 class, proven ceiling, floor and prior-push CPC history; highest-consequence non-arrival); I-2 inventory feed / Data Operations (no workaround); I-3 #39 / Data Ops (T7 statuses for A1, A3, A6, B3, D1, D2, D3, D6, D8, D9 weekly; daily rank series daily); I-4 Brand Management (T5 completeness; log with gaps more dangerous than empty one); I-5 #28 (rung values, floor register, exit-bid references); I-6 #32 (armed windows, settle marks, pre-window baseline); I-7 #41 economics (per-variation margin into T0 zone C, monthly + event, before Monday packet-ready read); I-8 #33 (lead declaration); I-9 #37 (rule change log); I-10 listing/pricing/review owners (restoration artifacts); I-11 SOP-26 (Recovery Mode state and R3 override set); I-12 SOP-25 (both directions: cause classes out, descent schedule in). Downstream: I-13 #6; I-14 #35; I-15 SOP-12 (standup order, re-point, ladder-restore, retag); I-16 #28 (achievement date and bid, restored floor, failed-probe marking); I-17 instrument layer (queue submission, released budget line; stalled release routes to PPC Lead by role); I-18 #38 (reason strings with verdict and scenario ID; Tuesday default, same day on restock or RED flip).

### 10.5 Documents named but not present in this corpus
- Master PPC Decision Criteria System v4.0 (referenced throughout; v4.1 pending).
- Keyword Decision Record Template v3.0; PPC Strategic Doctrine v1.0 (principles 3, 4; Sections 6.3, 14); PPC Economics Worked-Example Set v1.0 (cases E3, E5); PPC Authority Matrix v2.0 Section 1; Master PPC Data Architecture v1.0 (Sections 4, 6, 9, 11, 12) and Command Workbook; PPC Cross-Reference Ledger v2.8; Supersession Map; Economics and Context Pack.
- Components referenced by number: #6, #16, #17-19, #23, #25, #26, #27 (outside corpus per C6), #28, #29, #30, #31 (no procedural document per C3), #32, #33, #35, #37, #38, #39, #41.
