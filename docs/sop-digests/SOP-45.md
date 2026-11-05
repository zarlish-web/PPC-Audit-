# SOP-45 Digest: Dayparting Deferral Control

Source: `PPC_SOP_45_Dayparting_Deferral_Control_v1_0.pdf` (14 pages; the text calls itself 11 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-45: Dayparting Deferral Control (Operating SOP, Component #45) |
| Version | 1.0 (first build) |
| Date | Not stated in the header (references #44 due 2026-09-25; Ledger rows dated to 2026-08-10) |
| Owner | PPC Lead; "Roles, never names" |
| Thresholds | v4.0 only; **zero local thresholds**; **zero verdicts of its own**; **authorizes zero hourly modifiers** |

**Verdict / purpose.** Dayparting is **deferred, not undecided**; this SOP governs the **deferral**, not the practice. v4.0 Section 9 (Layer 4: Lever Library L1-L10) defines **L10**: "Dayparting (new, dormant until data): **plus or minus 15% hourly modifiers**, deployed only on **Marketing Stream curves** with **4 weeks minimum of hour-level evidence per campaign (Catalog D12)**. Until the feed lands, no dayparting decisions are made on guesswork." The feed has not landed: **Command Workbook T7 MANIFEST row "D12 Hourly dayparting"** reads **Source Feed "Marketing Stream", Refresh "Deferred", Status "MISSING"**. Master PPC Data Architecture v1.0 Section 12 lists **nine live feeds**; Marketing Stream is not one. Ledger records external dependency **D5 "Marketing Stream hourly feed" as OPEN**. Four jobs:
1. Hold the deferral in a stated, dated, weekly-checked condition.
2. Stop dayparting-shaped actions entering through side doors while the lever is dormant.
3. Convert the deferral into an execution build the day the feed lands.
4. Retire the slot permanently if evidence says the pattern doesn't exist.

**Why short (1.1):** Build Kit sets 10-18 pages and SOP-12 v2.0 floor is 12 procedures/4 examples; not reachable honestly. Ledger row #45 ownership: "**The deferral and its trigger condition.**" Must-not-restate: "**Nothing operational until the trigger fires.**" v4.0 gives only two numbers for the lever (±15%, 4 weeks); missing: **bucket granularity, step cadence, re-read interval, hold test, exit rule** (writing them would breach anti-drift rule 1). Precedent: Ledger registers **#21 "DSP and Sponsored TV deferrals"** as "COMPLETE as a closed decision ... No procedure exists and none is owed." Content: 10 standing procedures, hour-level sufficiency arithmetic, 10 failure modes, activation gate, 2 worked examples.

## 2. Scope & boundaries

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 | Decides every threshold incl. L10 ±15% and 4-week window. SOP executes deferral; never sizes an hourly modifier |
| #12 Exact campaign operations | Owns intraday funded-push pacing and **hourly truncation alarm on push campaigns**. SOP consumes alarms as confound list; never duplicates pacing |
| #28 Placement & bid-modifier operations | Owns ceiling worksheet and every modifier operation; hourly modifier is a **fourth multiplicand** in that worksheet. Referenced by number & clause only per **Ledger conflict C8**; attached copy superseded |
| #37 Automation platform rules | Owns rule register, weekly diff, change control. Time-conditioned rule registered there. SOP supplies the **exclusion reason**. Number & clause only (C8) |
| #20 AMC operations | Owns AMC audience & query lifecycle; produces hourly-pattern evidence (Strategic Doctrine v1.0 Section 10). SOP consumes as intake; never writes/runs a query |
| #39 Data feed & manifest operations | Owns feed definitions, manifest field groups, T7 layer; D12 row definition & status transitions. SOP reads, never edits |
| #38 Bulk-file deployment mechanics | Owns staging & T+1 diff. Only at activation does output pass through; before activation stages nothing |
| #21 DSP & Sponsored TV deferrals | Structural precedent only; no content borrowed |
| #1 Document governance, #2 A-to-Z System Map | Own status vocabulary & routing; SOP writes state back, never re-declares own status |
| #44 Operator onboarding | Consumes Element 11, due 2026-09-25 |
| #4 and #40 Operating cadence | Own the calendar slots for weekly & quarterly procedures |

## 3. Triggers

Lags are **proposed** (AM-2), not v4.0 thresholds.

| Trigger | Detecting artifact | Max lag (AM-2) | Procedure |
|---|---|---|---|
| Weekly deferral-state check | T7 MANIFEST row "D12 Hourly dayparting", column Status, after Monday 09:00 refresh | Same day | P1 |
| D12 status flip | D12 row reads anything other than MISSING | 1 business day | P8, then P1 suspends |
| Dayparting-shaped proposal | Any staged change reason string, any T6 DECISION LOG entry, or verbal proposal conditioning bid/budget/modifier on time of day | Same day | P3 using P2 |
| Time-conditioned automation rule found live | Weekly automation-platform rule diff (#37) | Same day | P4 |
| v4.0 increment | New Criteria System export whose Section 9 L10 or Section 5 G2 text differs from last read | 5 business days | P5 |
| AMC hourly-pattern evidence returned | #20 result set answering the **fifth query** of Strategic Doctrine v1.0 Section 10 | 5 business days | P6 |
| Quarterly deferral review | #40 calendar slot | On date | P7 |
| Retirement evidence accepted | P7 record carrying PPC Lead decision to retire | 5 business days | P9, then P10 |

## 4. Procedures

### Preconditions & gates (Element 3)
Unobservable precondition = failed, not assumed.
| Gate / ID | Requirement | Observable |
|---|---|---|
| **D12 Hourly dayparting** (T7) | Row exists, Status read this cycle. While MISSING, every procedure except P8 legal; **P8 barred** | D12 Status cell after 09:00 Monday refresh, date in P1 entry |
| **G8** Packet completeness | Manifest reports present/stale/missing before analysis; verdict with missing gate fields downgraded to flag; packets **<85%** of gate-relevant fields = flags only | **T7 PACKET COMPLETENESS SCORE** cell and D12 Status |
| **G2** Sample sufficiency | Bid reads **15 clicks min over 7 days**; CVR verdicts **100 clicks**; CTR verdicts **1,000 impressions**. Below -> **EXTEND TEST**, never rate judgment | P2 output: clicks per hour bucket vs 15/100, per bucket not per campaign |
| **G3** Budget truncation | In-budget **<70% of day** marks every rate TRUNCATED; budget lever evaluated before any bid conclusion | **T7 row A3 "Pacing buckets / in-budget %"** and campaign in-budget %. **A3 currently PARTIAL with day-of-week curve pending** (caps hourly claims even after truncation clears) |
| **G9** Price stability | Price change on targeted variation within trailing **7 days** -> CVR & ACOS PROVISIONAL | **T5 PRODUCT LOG** Event Type entries of type price move in window |
| **G10** Event exclusion | Event weeks and **14 days following** excluded from trend verdicts | T5 **Trend-Exclusion Flag** column |
| **G1** Validation quarantine | Impossible metrics quarantine row, flag, same-day data-refresh task | Zero-flag columns on any hour-level extract |
| **A6** Objective + per-term Expected CPC (T7) | Reads **PARTIAL**, Expected CPC held at account reference until per-term values land | A6 Status; hourly claims priced vs per-term Expected CPC inherit partial state |

### P1. Weekly deferral-state check (5 min)
1. Monday, after Data Ops lands **Raw Pull Pack at 06:00** and **Power Query refresh** completes product workbooks by **09:00**. Open product workbook, **T7 MANIFEST**.
2. Locate row "D12 Hourly dayparting"; read **Source Feed, Refresh, Status, Verdict Classes Blocked While Missing**.
3. Expected: "Marketing Stream", "Deferred", "MISSING". Any other Status -> stop, P8 within one business day.
4. One **T6 DECISION LOG** line: Date = cycle date; **Level = product** (AM-7: no component-level value; Target names component); Target = "#45 deferral state"; Rule / Scenario Fired = "v4.0 Section 9 L10"; Change (prior to new) = "DEFERRED to DEFERRED" or observed transition; Dollar Impact / wk = 0.00; Review Date = next quarterly slot; Owner / Tier = PPC Lead.
5. Where the product workbook set covers **five brands**, run once per product workbook; results reconcile. Status divergence across products = **F2** same day.

### P2. Hour-bucket sufficiency computation (20 min)
Every hour-level claim passes through this (operator, platform recommendation, AMC result).
1. Trailing 7-day clicks from **T3 CAMPAIGN BOARD**, or term clicks from **T2 KEYWORD COMMAND** for term-level claims. Same window as claim; unstated window -> claim fails, P3 branch D.
2. Bucket count: **24** (each clock hour pooled across 7 days) or **168** (day-of-week x hour). v4.0 doesn't choose (AM-3); **compute both** (differ by factor 7).
3. Clicks per bucket per week = trailing 7-day clicks / bucket count.
4. Weeks to bid read = **15 / clicks per bucket per week**; weeks to CVR verdict = **100 / clicks per bucket per week** (G2).
5. Compare to L10 4-week window; weeks-to-reach > 4 -> claim cannot clear G2 inside it.
6. Inverse: **required weekly clicks = minimum clicks x bucket count / 4**.
7. Write the computation (six lines) into the triage record.

### P3. Dayparting-shaped proposal triage (25 min)
Any proposal to condition a bid, budget, modifier, campaign state or automation rule on time of day. Exhaustive branches:
| Branch | Condition | Action |
|---|---|---|
| A | Cites hour-level data and campaign **TRUNCATED** per G3 (<70%) | Stop. Route to budget lever (v4.0 Section 9 **L1** places budget ahead of bid). Quote **"FIX BUDGET (TRUNCATED)"** (KDR v3.0). Re-read only after full validated window at in-budget 70% min (WE-B) |
| B | Hour data, not truncated, P2 bucket **below G2 minimum** | Stop. Quote **"EXTEND TEST"** (v4.0 13.1). Record P2 output with required weekly clicks (WE-A) |
| C | Hour data, not truncated, P2 bucket **at/above G2 minimum** | Stop anyway: D12 MISSING, source isn't Marketing Stream; sufficiency doesn't substitute for provenance. Route observation to P6 as candidate AMC evidence input |
| D | No window, bucket count, or click counts | Return unread with P2 template |
| E | Platform-side recommendation or vendor default with hourly schedule | Branch C plus F1: check if live as rule; if so P4 same day |
1. Log in T6 with branch letter in Rule / Scenario Fired cell alongside v4.0 citation.
2. Proposal from a role -> written response with the six arithmetic lines.

### P4. Time-conditioned automation rule check (15 min)
1. Read #37 weekly rule diff (SOP doesn't run diff or hold register).
2. Scan for rules whose trigger, schedule, or action window is conditioned on **clock time** rather than metric state.
3. For each, issue exclusion reason to #37 in one sentence citing v4.0 Section 9 L10 and D12 status; #37 writes register entry, suspension, reconciliation.
4. Live & unregistered = #37's register failure; raise there; **never edit an automation rule**.
5. Record count found & excluded in P1 weekly line. Count >0 for **two consecutive quarters** = finding for P7.

### P5. v4.0 increment re-read of L10 (20 min)
1. Open Section 9, read L10 in full.
2. Diff four things: modifier bound (±15%); evidence window (4 weeks per campaign); named feed (Marketing Stream); named catalog ID (D12).
3. Read Section 5 G2 same pass (changes every stored required-weekly-clicks figure).
4. Read **Section 17.1 adoption phase 4** ("Marketing Stream dayparting (L10) when the feed lands" is a phase-4 deliverable); phase change reported to #1.
5. If increment adds any of the five missing rules (AM-3 to AM-6), SOP is **superseded**, activation build starts; else record re-read with date & confirmed text.

### P6. AMC hourly-pattern evidence intake (45 min)
1. Trigger: #20 returns result set for the fifth of five queries in Strategic Doctrine v1.0 Section 10 ("hourly-pattern evidence that either justifies or permanently retires the deferred dayparting slot").
2. Receive as intake artifact.
3. Gates in order before reading an hour: **G1** (impossible values), **G10** (event weeks + 14 days), **G9** (price moves from T5), **G3** (every campaign in result set).
4. Run P2 on surviving campaigns; list which carry enough weekly clicks for a bucket to clear G2 inside L10 4-week window (the real output).
5. Intake note with three numeric findings: campaigns surviving gates; campaigns clearing P2; spread between best & worst bucket where both cleared. Attach to quarterly review file.
6. Intake **does not authorize a modifier** (AMC is neither Marketing Stream nor D12). Authorizes only a better-informed P7 and a retirement case under P9.

### P7. Quarterly deferral review (45 min, #40 slot)
1. Inputs: trailing **13 P1 weekly lines**, P3 triage counts by branch, P4 exclusion counts, any P6 intake note.
2. Read D12 status directly.
3. Answer in writing: has feed status moved; has account tried to reach lever by proxy and how often; has retirement evidence arrived.
4. Issue one of three states: **hold** (default, no case), **arm for activation** (requires D12 status change), **retire** (requires P6 intake note; moves to P9).
5. Write review record; route state to #1 (register line) and #2 (routing map). Quarter with no record = F6.

### P8. Activation gate (3 hours, then build session; runs once when D12 stops reading MISSING; deploys nothing)
1. Confirm status change at source with #39; change written by anyone else = F2.
2. Confirm feed coverage **per campaign**; record which campaigns covered from which date; partial coverage arms partial scope (F10 otherwise).
3. Start **4-week clock**; record end date. No dayparting decision legal before that date on any campaign.
4. End of week 4: run P2 across covered campaigns -> eligible list. Campaigns that can't clear G2 inside the window are out of scope permanently until click volume changes; required weekly clicks recorded against each.
5. Check five open rules: v4.0 must state **bucket granularity, modifier step cadence, re-read interval, hold test, exit rule** (AM-3 to AM-6). Any absent -> gate closes with written statement; account holds ("A modifier bound without a step cadence is not a lever, it is a range").
6. If all present: hand eligible list, coverage dates, open-rule confirmation to execution-SOP build session; modifier-into-ceiling question to #28. SOP superseded on that document's release.

### P9. Retirement path (30 min)
1. Trigger: P7 issues retire on strength of P6 note (Strategic Doctrine v1.0 Section 10: retirement is one of two legitimate AMC outcomes).
2. State case in numbers from intake note (surviving, clearing P2, bucket spread). No v4.0 evidence bar (AM-6); case presented, not threshold-cleared.
3. Decision: **PPC Lead**; L10 deletion itself is a v4.0 change -> **CEO** row on v4.0 threshold changes.
4. On acceptance route: retirement memo -> #1; L10 deletion request -> v4.1 amendment list; D12 row disposition -> #39.
5. Component closes like #21; SOP archived.

### P10. State handoff at activation or retirement (30 min)
1. Write component state to #1 with date & deciding artifact (#1 supplies the status word).
2. Return updated Ledger row for #45 in copy-paste form to Ledger close-out (close-out assigns version & any conflict ID).
3. Hand Element 11 to #44 (due 2026-09-25).
4. Release #40 quarterly slot on retirement, or convert to execution SOP's review cadence on activation.

## 5. Rules, thresholds & numbers

### 5.1 v4.0 references
| Rule | Meaning as described |
|---|---|
| L10 (Section 9 Lever Library L1-L10) | Dayparting, dormant until data: ±15% hourly modifiers, only on Marketing Stream curves with 4 weeks min hour-level evidence per campaign (Catalog D12) |
| L1 | Budget ahead of bid in lever precedence; sequence never skipped forward |
| L8 | Format substitution (cheap-surface pivot) - instruments wrongly cite L8 for dayparting (N1) |
| G1 | Impossible metrics quarantine |
| G2 | 15 clicks / 7 days bid read; 100 clicks CVR; 1,000 impressions CTR; below -> EXTEND TEST |
| G3 | In-budget <70% of day -> TRUNCATED; "a starved campaign's ACOS and CTR describe its worst hours, not its potential" |
| G8 | Completeness; <85% gate-relevant fields = flags only |
| G9 | Price change in trailing 7 days -> CVR/ACOS PROVISIONAL |
| G10 | Event weeks + 14 days excluded from trends |
| V3 | "New verdicts enter only by V3 amendment" (Section 13.1) |
| Section 13.1 | 18 actions, none dayparting. EXTEND TEST (primary scenarios G2, D9): "Evidence insufficient or confidence LOW; capped continuation to the sufficiency threshold". FLAG: DATA REPAIR (primary scenarios G1, G8, P8): "Quarantine/manifest failure; no recommendation; repair task with owner and date." |
| Section 17.1 | Adoption phase 4 deliverable: "Marketing Stream dayparting (L10) when the feed lands" |
| D9, P8 | Named as primary scenarios for EXTEND TEST / FLAG: DATA REPAIR |

### 5.2 Verdict strings quoted
| String | Source | When |
|---|---|---|
| EXTEND TEST | v4.0 13.1 | P3 branch B; F5 |
| FIX BUDGET (TRUNCATED) | KDR v3.0 Bands & Verdicts Reference | P3 branch A |
| FLAG: DATA REPAIR | v4.0 13.1 | F2: D12 status unsupported by feed table, or hourly extract fails G1 |
| QUARANTINE: DATA REFRESH | KDR v3.0 | KDR-side equivalent on keyword record |
KDR v3.0 "CLOSED VERDICT VOCABULARY (Framework Section 17)" sheet: 25 strings, none dayparting. Deferral states **held / armed / retired** are state text in T6, not verdicts (AM-1).

### 5.3 Numbers
| Item | Value |
|---|---|
| L10 modifier bound | ±15% hourly |
| L10 evidence window | 4 weeks minimum per campaign |
| G2 | 15 clicks (bid), 100 clicks (CVR), 1,000 impressions (CTR), over 7 days |
| G3 | 70% in-budget |
| G8 | 85% gate-relevant fields |
| G9 | 7 days |
| G10 | 14 days following event |
| Bucket options | 24 or 168 (factor 7) |
| Live feeds | 9 (Data Architecture Section 12); Marketing Stream not one |
| Raw Pull Pack | Monday 06:00; refresh by 09:00 |
| Product workbooks / brands | Five |
| Proposed lags (AM-2) | Same day; 1 business day (D12 flip); 5 business days (v4.0 increment, AMC return, retirement) |
| Quarterly review inputs | Trailing 13 P1 lines |
| Proxy finding | P4 count >0 two consecutive quarters |
| Escalation | F1, F7 on discovery; F2 same day; F6 at quarter boundary; 4+ consecutive P1 lines missing = F6 |
| Stale manifest (I-1) | Two consecutive stale cycles -> PPC Lead |
| AMC absence (I-2) | Four consecutive quarters no intake -> P7 finding to #20 and #1 |
| Durations | P1 5 min; P2 20; P3 25; P4 15; P5 20; P6 45; P7 45; P8 3 h + build; P9 30; P10 30 |

### 5.4 Failure modes
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Time-conditioned automation rule live | #37 diff returns clock-time rule | Exclusion reason to #37 same day; #37 suspends & registers. Motivation: register seeded from live platform inventory, so pre-register rules exist by construction |
| F2 | D12 marked present before feed lands | D12 Status not MISSING while Data Architecture Section 12 lists no Marketing Stream source, or five workbooks disagree | FLAG: DATA REPAIR; repair task (G8); confirm with #39 before P8 |
| F3 | Truncation read as hourly pattern | Hour claim on campaign with in-budget <70% | P3 branch A; **most likely failure in the account by a wide margin** |
| F4 | AMC evidence used as deployment authority | Staged reason string citing AMC query for time-conditioned change | Blocked at staging by #38 |
| F5 | Bucket claim below sufficiency | P2 under G2 min | EXTEND TEST; record required weekly clicks |
| F6 | Deferral rots | No P7 record across quarter, or >=4 consecutive P1 lines missing | Escalate to PPC Lead; #40 slot is structural fix |
| F7 | Dayparting by proxy | T6 shows repeating clock-pattern in T3 **Daily Budget $, State, or Placement Mult TOS %** with no verdict | Normalize; route to campaign-type SOP (budget/state) or #28 (modifier); record as proxy attempt |
| F8 | Activation without window | P8 step 4 with coverage <4 weeks | Hold; record end date |
| F9 | Contaminated first curve | First Marketing Stream window overlaps event/14 days (G10), price move in 7 days (G9), or G1 quarantine | Exclude affected days; extend window |
| F10 | Partial coverage treated as full | P8 step 2 partial coverage with account-wide eligible list | Scope to covered campaigns only |

## 6. Data inputs required

- **T7 MANIFEST** (each of five product workbooks): row **"D12 Hourly dayparting"** (Catalog ID + Field Group, Source Feed, Refresh, Status, Verdict Classes Blocked While Missing); row **A3 "Pacing buckets / in-budget %"** Status; row **A6** Objective + per-term Expected CPC Status; **PACKET COMPLETENESS SCORE** cell.
- **T3 CAMPAIGN BOARD**: Daily Budget $, State, Bidding Strategy, Placement Mult TOS %, trailing 7-day clicks, in-budget %.
- **T2 KEYWORD COMMAND**: trailing 7-day clicks (term-level claims).
- **T5 PRODUCT LOG**: Event Type (price move), Trend-Exclusion Flag.
- **T6 DECISION LOG**: Date, Level, Target, Rule / Scenario Fired, Change (prior to new), Dollar Impact / wk, Review Date, Owner / Tier; staged change reason strings.
- **#37 weekly automation-platform rule diff**.
- **#20 AMC result set** for query 5 of Strategic Doctrine v1.0 Section 10.
- **#12 intraday truncation alarms** on push campaigns (confound list).
- Hour-level exports / platform recommendations / vendor hourly schedules (inputs under triage).
- **v4.0** Section 9 L10 text, Section 5 G2 & G3 text, Section 13.1, Section 17.1.
- **Data Architecture v1.0 Section 12** feed table (and Section 8 hourly columns).
- **Marketing Stream** hourly feed (not landed; external dependency D5).
- #40 calendar slot; Ledger row #45.

## 7. Outputs / artifacts

| Record | Storage | Retention | Consumer |
|---|---|---|---|
| Deferral State Record (weekly) | T6, one line per product workbook per cycle | Life of workbook (AM-8) | P7; #1 |
| Hour-Bucket Sufficiency Sheet (six lines) | Attached to triage record | Until click volume changes materially | P3; P6 eligible list; P8 step 4 |
| Proposal Triage Record | T6 with branch letter in Rule / Scenario Fired | Life of workbook (AM-8) | P7 branch counts; proposing role in writing |
| Schedule-Rule Exclusion Note | Issued to #37 register; copy in P1 line | Held by #37 | #37 |
| AMC Evidence Intake Note (3 numeric findings) | Quarterly review file, attached to #20 result | Until superseded | P7; P9 |
| Quarterly Deferral Review Record (hold/arm/retire) | T6 + review file | Life of component (AM-8) | #1; #2; PPC Lead |
| Activation Packet (eligible list, coverage dates, open-rule confirmation) | Activation build session | Permanent | Execution SOP build; #28 ceiling worksheet |
| Retirement Memo | #1 with L10 deletion request | Permanent | #1; v4.1 list; #39 |
| Returned Ledger row #45 | Ledger close-out | Permanent | Subsequent build sessions |
Plus F1-F10 alarms with evidence lines. **Zero deployed changes**; stages nothing through #38 before activation.

## 8. Decision rights

- **AI-executable with audit:** P1 read & T6 line; P2; P3 branch selection & record; F7 scan; P6 gate filtering & eligible-list arithmetic.
- **PPC Lead decides:** P7 quarterly state call (rows "Automation rules (#37)": PPC Lead D, incoming operator E & R, PPC Manager E; "Structure creation (all SOPs)": PPC Lead D, operator E). P6 intake acceptance ("AMC cycle (#20)": PPC Lead D, incoming operator E). P9 retirement recommendation.
- **CEO decides:** L10 deletion request (P9) and any activation changing a v4.0 threshold ("v4.0 threshold changes": CEO D, PPC Lead E & R, incoming operator I).
- Vacancy rule: D -> PPC Lead, E -> PPC Manager.
- No Matrix row for deferral components (AM-10); inherits four rows. Checkpoint holder throughout: PPC Lead.
- Ramp: Week 1 locate D12 in all five workbooks, cite five numbers in source, observe P1 & #37 diff, reproduce P2 cold; Week 2 supervised P1 across five workbooks, P4 exclusion drafts, two P3 triages (one seeded branch A), draft P7 inputs; Week 4 unsupervised weekly cycle, one live proposal with written response, P6 dry run on synthetic set, walk P8 on paper. Six live-defense questions.

## 9. Account-specific facts

- D12 row: Source Feed "Marketing Stream", Refresh "Deferred", Status "MISSING".
- T7 **A3 "Pacing buckets / in-budget %"** reads **PARTIAL** (day-of-week curve pending); **A6** reads **PARTIAL** (Expected CPC at account reference).
- External dependency **D5 Marketing Stream hourly feed OPEN**.
- Product workbook set covers **five brands** / five product workbooks.
- Automation register seeded from live platform inventory (pre-register rules exist).
- Fictional base: AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max Acc 26.3%, CVR 5.2%; Max Profitable CPC $1.46; Target CPC $0.73 (case E1).
- **WE-A:** proposal to cut bids 15% 00:00-06:00 on single-keyword oversight exact campaign; 40 clicks/7 days; in-budget 91%. 24 buckets: 1.6667 clicks/bucket/wk -> 9.0 wks to 15 clicks, 60.0 wks to 100; 168 buckets: 0.2381 -> 63.0 and 420.0 wks. 4-week window holds 6.67 / 0.95 clicks per bucket. Required weekly clicks: 90 / 630 (15-click) and 600 / 4,200 (100-click). Cost: 630 x $0.73 = $459.90/wk; 4,200 = $3,066.00/wk; at $1.46: $919.80 / $6,132.00. 630 vs 40 = factor 15.75. Verdict EXTEND TEST.
- **WE-B:** ten hours 14:00-23:59 zero impressions; daily budget $45.00 exhausts at 14:00 -> in-budget 58.3% (TRUNCATED); burn $3.2143/h; CPC $1.00, 45 clicks, 2.34 orders, $187.20 sales, ACOS 24.0%, $65.52 contribution, $20.52 net/day. G3-implied budget: 16.8 h x $3.2143 = $54.00/day -> 54 clicks, 2.808 orders, $224.64 sales, ACOS 24.0%, $78.62 contribution, $24.62 net; delta **$4.10/day, $28.73/week**. Verdict FIX BUDGET (TRUNCATED); then branch C (A3 PARTIAL, D12 MISSING).

## 10. Open items

| ID | Item |
|---|---|
| AM-1 | Deferral-state vocabulary (held, armed, retired) not in v4.0 13.1 or KDR v3.0; admit via V3 (same class as #43, #46) |
| AM-2 | Element 2 lag table: v4.0 has no signal-to-start lags; lags proposed by this build (Ledger records same item for #20) |
| AM-3 | Hour-bucket granularity 24 vs 168 (factor 7; opposite verdicts) - **highest-value item** |
| AM-4 | Whether G2 minimums apply per hour bucket; P2 applies per bucket as conservative reading |
| AM-5 | Activation mechanics: step cadence, re-read interval, hold test, exit rule |
| AM-6 | Retirement evidence bar (Strategic Doctrine Section 10 permits retirement; v4.0 no bar) |
| AM-7 | T6 Level closed list (product, syntax, keyword, campaign, placement) has no component-level value; owner #39/workbook |
| AM-8 | Retention policy pending fold-in under #39 |
| AM-9 | Lever ID for dayparting: v4.1 should state L10 in one place (see N1) |
| AM-10 | Authority Matrix row for deferral/activation decisions (owner #3) |

**Findings (13.2; no IDs minted):**
- **N1 Lever ID drift L8 vs L10:** v4.0 assigns dayparting = L10, L8 = format substitution. Data Architecture v1.0 Section 8 (hourly dayparting columns reserved but unbuilt) cites **L8**; Command Workbook TEMPLATE v1.0 T7 D12 row names blocked class as **"L8 dayparting"**. L10 correct. Distinct from **C9** (G-series gate numbering).
- **N2 Pack state mismatch:** version note says Ledger v2.5 at 2026-08-08, Wave 4 closed, Wave 5A opening; attached Ledger header reads v3.3 at 2026-08-04 with Wave 1 most recent, while rows carry versions to 3.2 and dates to 2026-08-10 with Wave 5A and 5B rows. Ledger header stale.
- **C8 recurrence:** Tier 2 items arrived as SOP-28 v1.0 and SOP-37 v1.0 while Ledger records both at v2.0 (row versions 2.7 and 3.1); cited by number & one clause only.
- Conflicts referenced: C1-C7 (existing), C8, C9.

**Interface contracts:**
| ID | From -> To | Artifact | Timing | Non-arrival |
|---|---|---|---|---|
| I-1 | #39 -> #45 | T7 D12 Status | Weekly, Monday 09:00 | P1 on last known status, T6 line marked stale with age; 2 stale cycles -> PPC Lead |
| I-2 | #20 -> #45 | Query 5 hourly-pattern result set | AMC cycle date | P6 doesn't run; hold by default; 4 quarters no intake -> finding to #20, #1 |
| I-3 | #37 -> #45 | Weekly rule diff filtered to time-conditioned | Weekly | P4 can't run; exclusion set unverified (F1 precondition) |
| I-4 | #45 -> #37 | Exclusion reason string (L10 + D12) | Same day | Rule registered without basis; stays live; account dayparting undecided |
| I-5 | #45 -> #28 | At activation: hourly modifier as multiplicand + eligible list | Once at P8 | Ceiling understates effective max CPC by full hourly bound |
| I-6 | #12 -> #45 | Intraday truncation alarms | Weekly or on alarm | Branch A loses detection; truncation cases stopped at B for wrong reason; WE-B $28.73/wk finding never made |
| I-7 | #45 -> #1 | Component state line | On change; quarterly | Register shows NOT BUILT against live doc |
| I-8 | #45 -> #44 | Element 11 + six defense questions | By 2026-09-25 | Certification lacks dayparting module |
| I-9 | #45 -> #40 | Quarterly review slot | Once at release | F6 expected outcome |
| I-10 | #45 -> Ledger close-out | Returned row #45 | Session close | Next session builds vs seed NOT BUILT; anti-drift rule 3 check fails silently |
| I-11 | #45 -> #38 | At activation: staged modifier sets | Not before activation | N/A while deferral holds; any pre-activation staged set citing #45 = F4, blocked at pre-flight |

**Review triggers:** v4.0 increment touching L10; increment touching G2 or G3; any change to T7 D12 row (can supersede); AMC return under #20 query 5; platform change introducing native hour-level controls. Quarterly regardless (P7). On activation superseded in full; on retirement archived like #21.

**Named documents not present:** Master PPC Decision Criteria System v4.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0; Cross-Reference Ledger; Strategic Doctrine v1.0 Section 10; KDR Template v3.0; PPC Economics Worked-Example Set v1.0; SOP Build Kit v1.0; SOP-12 v2.0; SOP-28 and SOP-37 (attached copies superseded, C8); Authority Matrix v2.0.
