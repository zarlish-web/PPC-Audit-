# 01 — Intake and data (Phase 0)

Read this before opening any file. Phase 0 ends when every input is received or confirmed absent, every file is read and reconciled, and the data-conditions register is written. No decision is taken before that.

## Contents
1. The one-batch rule and halt conditions
2. Intake by request type (analysis / plan / refinement)
3. Master input table
4. Reading discipline (how to open a file)
5. Joins and keys
6. Reconciliation checks
7. Data-validity quarantine
8. Freshness rules
9. Two-scope architecture (product vs campaign)
10. Unmeasured ≠ zero
11. Data-conditions register
12. Verifying what a column really measures
13. Open questions for the owner

---

## 1. The one-batch rule and halt conditions

1. **Request every input in one message** (template: `templates/intake-request.md`). Name each file, what it powers and the window you need. [PB, QA, SR]
2. **Do not start partially.** Wait until each item is supplied or the user explicitly confirms it does not exist this cycle. If only some arrive, list the missing ones back and ask once more. [PB, QA]
3. **Missing input = named gap**, never a guess or a substitute. Record it in the register (§11) with the decisions it blocks. Missing value = blank, never 0. [all]
4. **Ask once, then log.** An answerable gap is asked before it is logged; never log "revisit next cycle" for something the user could answer now; never ask about something already knowable from the files. [PB]
5. **Confirm before anything is computed:** product (parent ASIN + child SKUs), marketplace (**US or CA — never mixed**), exact portfolio name(s), window end date, stage, declared goal, owner settings (SKILL.md table). [SR, E, PB]

**Halt conditions — stop, report, no recommendations:**

| # | Condition | Why |
|---|---|---|
| H1 | Marketplace not confirmed, or files from two marketplaces mixed | Rates, prices and fees differ by marketplace [SR] |
| H2 | An advertised SKU has no economics (no margin/unit) | Never fall back to a global or blended break-even (source engines defaulted to 0.1986 — a known defect) [SR, 13§3] |
| H3 | Merge accuracy fails: DOH differs from source by > 0.5 day, or LTSF $/month by > $0.02 | The merged table no longer matches its source [SR] |
| H4 | Target CTR/CVR in the bulk drift > 2% from recomputation (Market × 1.10 / × 3.0) on > 10% of rows | Every quadrant verdict would rest on wrong targets [SR] |
| H5 | A relevant sheet was NOT-OPENED (§4) | A decision may contradict data you never read [WB] |
| H6 | Bulk IDs don't resolve (one unmatched Campaign/Keyword ID on an update) | Stale export; any upload built from it fails or edits the wrong row [CB] |
| H7 | Any cross-source mismatch that would move money (spend, margin, stock, price) and can't be explained | Nothing is guessed [SR, PB] |
| H8 | Plan request with no declared product goal | Hard stop until declared or a suggested goal is confirmed. If the owner will not declare, apply Profit-First for the ranking gate and record it [PB, SKILL] |

Smaller mismatches that don't move money → log as a data condition and continue.

---

## 2. Intake by request type

| | Analysis (diagnose what exists) | Plan — from scratch | Plan — refinement |
|---|---|---|---|
| Purpose | Audit an engine run, product or campaign set | Decide what to do next | Update an existing plan against new data |
| What to request | Everything the diagnosis needs, incl. the artefact under review (engine output, decided bulk, prior plan) | **Full batch** (§3), all windows | Read the whole existing plan first; classify each decision **stated / gap / stale**; request only what the gap and stale items need + the prior action log and impact ledger |
| Staleness | A **finding**, not a blocker (report it) | Blocks the verdicts that depend on it (e.g. stale margin blocks ceilings) | Stale decisions re-derived; stated ones kept unless the grade says otherwise |
| First computation | Reconcile the artefact against its sources | Reconcile sources; frame goal and economics | **Execution check, then grade every prior action** (executed? worked / flat / backfired / too soon / deal window) before any new decision |
| No prior log | n/a | n/a | Treat as first cycle: say "No prior cycle supplied — treated as first cycle"; no grades, no escalation; write the full baseline [SR] |
| Scope creep | Ask before expanding an analysis into a plan | — | Forward-only: no silent retro-rewrite of earlier decisions |
| Output | Findings + register | Full plan + workbook | Clean full plan + change log + change review sheet |

[PB, SR, WB] Ambiguous request → ask once which of the three it is.

---

## 3. Master input table

Windows: **current 7 d vs prior 7 d** = evidence a live action is judged on; **30 / 90 d** = judgement windows for non-ranking and keyword rules; **60–90 d** = baseline, sample size, trend. Attribution is 7-day: the last 7 days of any window read low. [PB, B6]

| # | Source | What it is | Required fields / columns | Window | Freshness limit | Used for | If missing → blocked |
|---|---|---|---|---|---|---|---|
| 1 | **SP bulk file — 3 windows** | Amazon Bulk Operations export with performance columns | Entity, Operation, Campaign/Ad Group/Keyword/PT IDs, Campaign Name, Portfolio, State (campaign, ad group, keyword), Bidding Strategy, Targeting Type, Match Type, Keyword/PT expression, Bid, Budget, Placement rows (Top / Rest Of Search / Product Page) + Percentage, Product Ad SKU/ASIN, Impressions, Clicks, Spend, Sales, Orders, Units. Engine-built bulks add Campaign Objective, Syntax, Target Rank, Organic Rank, TOS IS, Market/Target CTR/CVR, DSTR | Current 7 d · prior 7 d · 60–90 d (plus L30 if the engine uses it) | IDs must come from a fresh export (same day as any upload build) | Every campaign/keyword decision; routing (Product Ad rows); live state; bids, boosts, budgets | Everything in Phases 6–7. Only the prior-7 d file missing → no week-on-week evidence; long window missing → no baseline/sample reads |
| 2 | **Command Center / console campaign report** | Amazon Ads campaign performance by day; product tile by ASIN | Date, Campaign, Spend, Impressions, Clicks, Orders, Sales, budget and in-budget time where available | Daily, 30 / 90 d | Same window as bulk | Spend reconciliation; product-level spend (tile); deal-day spend; budget truncation | Product-scope spend check; truncation test (→ record "delivery unverified") |
| 3 | **Placement report** (campaign × placement) | Amazon placement report via Command Center | Campaign, Placement (TOS / ROS / PDP / off-Amazon), Impressions, Clicks, Spend, Orders, Sales | 30 d mix; 90 d for TOS CVR | Same window as bulk | Placement click share, TOS CVR, TOS CPC (clearing), break-even CPC per placement, mix fix | Placement-level pricing — ceilings fall back to blended CVR, which the framework forbids for pushes → no PUSH verdicts |
| 4 | **SP Targeting report** | Per-target report incl. top-of-search impression share | Targeting, Match Type, Campaign, **Top-of-search impression share**, Impressions, Clicks, Spend, 7 Day Advertised SKU Units | 7–30 d | Same window as bulk | TOS impression share (holding the top); PPC velocity per SKU | TOS IS reads → no "holding top" test; push step rule runs blind. **Required**, not optional [QA] |
| 5 | **Search Term Report (STR)** | Account-wide, one row per day × campaign × customer search term | Date, Portfolio name, Campaign Name, Match Type, Targeting, Customer Search Term, Impressions, Clicks, Spend, `7 Day Total Sales ` (note trailing space), `7 Day Total Orders (#)`, `7 Day Total Units (#)` | 60–90 d (B6 keyword rules read 90 d; 30 d for spend distribution) | ≤ 1 cycle old | Harvest, negation, zero-order, wasted spend, keyword decisions, auto split | Harvest/BLOCK/REDUCE at search-term level; WAS% |
| 6 | **SQP** (Brand Analytics Search Query Performance) | Raw child-ASIN export; roll up to parent (§5.4) | Search Query, Search Query Volume, Impressions/Clicks/Cart Adds/Purchases: **Total Count** (market) and **ASIN Count** (brand); Purchases: Price (Median), ASIN Price (Median) | 13 weeks (B6); monthly for trends | Latest complete period | Market vs brand CTR/CVR, shares, Target CTR/CVR, four-quadrant, DSTR feasibility | Four-quadrant falls back to portfolio medians, labelled **provisional**; Target CTR/CVR blank (never guessed) |
| 7 | **MKL** (master keyword list) | Keyword universe with volume, syntax, relevancy | MKL keyword, Search Volume, Relevancy (fallback Derived Relevancy), Categorization, Organic Rank, Syntax; optional Indexed, PPC-targeted flags, Final Relevancy (manual) | Monthly build | **> 30 days = stale** | Keyword universe, SV tiers, relevancy, coverage, launch candidates | Coverage/gap analysis; SV tiers; relevancy-driven negation (→ Manual Review). Syntax must be verified against the account taxonomy before use; the MKL indexing field is unvalidated → ask before it moves money |
| 8 | **Target Ranks** | Owner's rank targets per term | Portfolio Name (Informational only), Search Term, Rank Target (+ target date if kept) | Current | Current plan | Ranking objective flag; rank gap; push premium; HOLD RANK | Ranking verdicts (a term without a target has no premium and no push) |
| 9 | **Rank tracking** | Daily organic (and sponsored) rank per term | Keyword, Date, Organic Rank (Sponsored Rank if available). **Data Rova** (primary; long format; 0/blank = not ranked → 101). **Data Dive** Rank Radar (gap-fill; wide, `Search Terms` + ISO date columns; 101 = not ranked). Own daily crawl where available | ≥ 1 month history (ideally 3); 30 d for decisions | < 1 month history → **out of scope for a ranking verdict** | Rank arc, rank drop, ranking states, sufficiency stop | Every ranking verdict (→ OUT OF SCOPE). Two trackers can disagree by ~7 places (B6): name the one that governs |
| 10 | **Data Rova / ASIN Insights (keyword export)** | Per-keyword market export for our product | Keyword, DSTR, Weekly Sales, Organic Rank, Sponsored Rank, Traffic Distribution Organic / Ad | Weekly | ≤ 1 week | DSTR, organic traffic share (for netting), current rank | DSTR sizing → rows UNSIZED; organic netting impossible |
| 11 | **ASINsight exports** (competitor traffic tool) | Our export + one per mapped competitor; market keywords; competitor view; placement trends; addressability | Per keyword: 7-day traffic, traffic ratio, organic/ad distribution, organic & sponsored rank, placements, weekly search volume, SFR. Competitor view: totals, organic/paid split, hero ASINs, placement reach, contested/ours-only/theirs-only. Addressability: addressable / disqualified / unknown with reasons. Placement trends: daily scores per child ASIN (organic, SP, SB, SB video) | 7-day traffic snapshot; trends 30–60 d | Exports compared only if taken **≤ 2 days apart**; placement-trend feed may be retired — state its last day | Market size, our share, contest, ad gap, rivals present, push-term field check, gaps | Competitor landscape and influence checks (Phase 3/8) — report "competitor data not supplied"; never "no competitors" |
| 12 | **Data Dive niches** | Niche dives: listings, keywords, roots | Per listing: price, est. units & revenue/month, BSR, rating, reviews, variations, listing age, page-1 keyword count, advertised keywords; niche median price/reviews/units | Per dive date | Dated; re-dive if > 1 month for pricing claims (No source rule; decide and record) | Price ladder, niche benchmarks, rival profiles | Price/offer positioning; conquest entry test (price/rating/reviews) |
| 13 | **AdInsight per competitor ASIN** | `AdInsight_US_<ASIN>_<start>to<end>.xlsx` | ASIN Ad Traffic Score (daily), Ad Keyword Count, Ad Position Traffic Ratio, Keyword Count for Ad Position (SP/SB/SBV/HR/TRB/CPF/SOR), Top 10 <type> Ad Traffic | 7–30 d | Dated per file | Rival ad-type mix, dormancy, pull-back; brand resolved per ASIN | Ad-type gap sizing (→ state as unmeasured) |
| 14 | **Helium 10 Cerebro / Xray** | Reverse-ASIN keyword ranks; head-term page listing data | Keyword, SV, own & competitor organic ranks (multi-ASIN in one pull), H10 PPC Sugg. Bid (context only); Xray: title, price, rating, reviews, images, video, BSR | Dated | Dated | Coverage audit (LIVE/PAUSED/MISSING), listing comparison | Coverage gaps can't be demand-validated |
| 15 | **Sellerboard** (per SKU/colour) | Profit per SKU | SKU, ASIN, Units, Refunds (count), Sales, Amazon fees, COGS, Advertising, Net profit / Margin, ASP | **Last 30 days** (B6); deal-state separately | **> 45 days = stale**, or any price / fee / size-tier / packaging / freight / LTSF change → re-derive within 48 h | Margin/unit → break-even ACoS, break-even CPC, ceilings; TACoS; margin after ads | **All pricing** (H2). Stale margin blocks every ceiling-referencing verdict |
| 16 | **Inventory / DOH / inbound** (per SKU, full unfiltered export) | Stock and replenishment | SKU, ASIN, Available (FBA sellable), Reserved, On-hand, Inbound/transit units, Units in production, dated next arrival (`Next In Stock`: date / Today / Not in Horizon), velocity (Base SV / sv/day — planned, shown beside the 30-day actual pace that gates zones, 13 #49), today's DOH (first date-like column in the DOH matrix) | Snapshot same day as bulk | Same day | Zones, stock-out-before-arrival, variation routing, projected DOC | Every PUSH (inventory gate unknown → no push); backup switch |
| 17 | **LTSF / aged inventory** | Aged-inventory surcharge view + FBA Inventory Age report | SKU, size, price, units per age bracket (**all 8 brackets**), cu ft/unit, estimated monthly surcharge ("AIS"/"CHARGE" column), units shipped t7/t30/t60/t90 | Monthly (assessed on the 15th) | Current month | LTSF tier, floor price, break-even discount, clearance objective | Clearance/LTSF decisions; 4-bracket file = approximate charges (finding) |
| 18 | **Preferred / Backup mapping** | Owner's variation routing | Product, Keyword Syntax, Preferred SKU, Backup SKU (key = syntax lowercased, no spaces; `root|size` keys for size fallback) | Current | Current | Which SKU each campaign should advertise; switch simulation | Switch recommendations; **never auto-derive backups** — ask the user to paste pairs [INV] |
| 19 | **Deal / event calendar** | Dated deals and events | SKU, deal price, start–end dates, deal type, deal fees; season/peak weeks | Next 60 d + last 14 d | Current | Deal-state economics; deal-day exclusion; build freeze; spend-limit exceptions | Every rate read near an event is suspect → state "calendar not supplied" and exclude windows that may contain deals |
| 20 | **Listing copy** | Live title, bullets, backend terms, A+; screenshots of gallery and page-1 results | Title, bullets, description, backend search terms (Category Listings Report), images | Live | Same week | Relevancy scoring vs listing; indexing; four-quadrant listing checks | Relevancy re-score (keep MKL labels, flag); listing verdicts |
| 21 | **Product goal & owner settings** | Owner's declared goal and dials | Goal (Growth/Scale · Mixed · Profit-First · Clearance/LTSF), stage, spend limit ($/day or /week, event exceptions), margin rule, ranking ceiling multiple, step limits, TACoS target (only if set), approval thresholds | Current | Confirm each cycle | Ranking gate, spend limit, ceilings | See H8 |
| 22 | **Prior action log + impact ledger** | Last cycle's decisions and grades | Log ID (`cycleDate|CampaignID|KeywordID-or-PTID`), lever, before/after values, expected metric/direction/tolerance, review date; ledger key `CampaignID|Target/KeywordID`, consecutive no-impact count, history | Last 12 weeks rolling | Last cycle | Execution check, grading, escalation | Refinement grading → treat as first cycle (§2) |
| 23 | **Competitor roster** | Mapped competitors per product | Brand, parent ASIN, child/hero ASINs, marketplace, tier (Aspirational / Beatable / Poor), export present y/n, date | Current | Current | Coverage statement, tiering, ASIN classification (own / own other product / competitor / unmapped) | Competitor tiers; any "we win / they win" claim (→ unmeasured) |
| 24 | **Product/business report** (reporting.xlsx or Business Report by child ASIN) | Parent-level weekly trend: revenue, units, sessions, unit session %, organic sales | ASIN, week, revenue, units, ad spend, TACoS, organic sales % | 4 weeks + prior | Latest complete week | Product-scope metrics (single source of truth, never recomputed from bulk) | Product-scope dashboard; organic share |
| 25 | **Sibling bulks** (products sharing head terms) | Same windows as #1 | As #1 | As #1 | As #1 | Shared-term ownership, cross-sibling cannibalisation | Named gap: ownership of shared head terms unresolved |
| 26 | **Manager responses** (if a review loop exists) | Actions the manager took outside the plan | Key, Manager Action, Manager Lever, Manager Action Date | Last cycle | Last cycle | Ledger loop status | Manager-acted rows graded as ordinary rows |

Amazon suggested bid ranges are **not requested** — they are not used to set prices (owner rule; 13 #18). [B6]

---

## 4. Reading discipline

1. **Enumerate every sheet/tab** of every file before declaring anything missing. [PB, WB I-1]
2. Read content; extract each figure with file / sheet / window. Diff long vs short windows. [WB I-2–I-4]
3. Give each sheet a status: **READ-FULL / READ-PARTIAL / NOT-RELEVANT / NOT-OPENED**. NOT-RELEVANT only after comparing its content; a relevant sheet NOT-OPENED halts the run (H5). [WB I-5–I-7]
4. Read the **unfiltered** inventory export before any filtering. [WB]
5. Header rows move: bulk header = first of the top 8 rows containing `Entity` and `Bid`; Sellerboard header auto-detected in the top 15 rows; DOH header = the row whose column A is `SKU` (often row 14); KCP-form MKL header on row 2. [SR, E]
6. A **supplied column beats a derivation**; a supplied column that looks wrong is a finding, not something to silently recompute. [WB]
7. State price stability over the window (price changes split windows). [WB]
8. Produce one **scope-labelled census**: every campaign that spends on the product, with its scope (§9). [WB, B6 F13]

---

## 5. Joins and keys

### 5.1 Normalisation
| Key | Rule | Never |
|---|---|---|
| Search term / keyword | `strip().lower()`, collapse whitespace; **word order preserved**; singular↔plural and symbol variants merge (close variants) | Sorted-token form except for grouping reports; never for ownership or deployment [13 #14] |
| Rank join | Exact lowercase + trim only | Fuzzy or reordered matching (ruling 2026-07-16) [SR] |
| Size tokens | Longest first: California King / Cal King before King; Twin XL before Twin; Split King, Full XL, Olympic/Short/RV Queen before Queen | Checking King before California King [E, PH] |
| Display | Keep original casing in outputs | — |

### 5.2 Entity keys
- **SKU: exact match including colour.** Unmatched → flagged, never filled from a "similar" SKU, size or colour. [SR]
- **Portfolio: the exact `Portfolio name` string** copied from the STR/bulk — never retyped (retyping is the classic "0 rows" failure). [E]
- **Marketplace: never mixed**; competitors belong to one marketplace. [SR, E]
- **ASIN detection:** lowercased value matches `^b0[a-z0-9]{8}$`. [E]
- **Campaign → SKU:** from Product Ad rows, never from campaign names (names were wrong on 212 of 251 rows in one audit). Name parsing is a fallback for reports only (SKUs longest-first, then ASIN substring). [WB, INV]
- **Bulk IDs:** Campaign / Ad Group / Keyword / PT IDs as **text** (15-digit precision loss otherwise). Keywords resolved by Keyword ID, campaigns by exact stripped name. [CB]
- **Objective:** from targeting per campaign block, never from the name (reference 06). [OC]
- **Brand terms:** brand name + misspelling list, substring match on the lowercased term; a brand missing from the list gets its terms flagged for negation — check the list first. [E]

### 5.3 Join outcomes
No match → blank, never 0. Safe division everywhere (`a/b if b else blank`; Excel `IFERROR(x/y,"")`). [E]

### 5.4 SQP parent roll-up
1. Group by Search Query.
2. **Brand (`… ASIN Count`) → SUM** across child ASINs.
3. **Market (`… Total Count`), Search Query Volume, market median price → TAKE ONCE** (max per query). Summing market columns multiplies them by the number of children and destroys every share.
4. Ignore SQP's precomputed rates; recompute CTR, CVR, shares (reference 02 §6).
5. Brand price = median of children's `Purchases: ASIN Price (Median)`.
6. Verify: rows = unique queries; Market Impressions = raw Total Count; Brand ≤ Market; every share 0–100%.
[SQP, E]

---

## 6. Reconciliation checks

Run before analysis. A failure that would move money halts (H7); others become data conditions.

| # | Check | Pass condition / tolerance | On fail |
|---|---|---|---|
| C1 | Bulk spend vs Command Center spend, same window | Equal after removing shared multi-product campaigns; remaining difference explained (window, attribution, shared campaigns). No numeric tolerance in any source — state the difference in $ and % | Explain or halt if it changes a decision (No source rule on tolerance; decide and record) [B6] |
| C2 | Product tile spend vs sum of campaign rows | Difference = spend of shared campaigns on other products; product-basis spend = row spend × (tile ÷ rows) | Flag shared campaigns (exception: no colour/price automation) [B6] |
| C3 | Sellerboard units vs orders | Units ÷ orders stable (B6: 1.03 units/order); gross units = units + \|refund count\| | Investigate multi-packs/refund spikes before deriving per-unit costs [SR, B6] |
| C4 | Inventory on-hand − available − reserved | Gap ≤ 5 units | > 5 → verify at source before zoning [PB] |
| C5 | Merged DOH / LTSF vs source | DOH \|Δ\| ≤ 0.5 day; LTSF \|Δ\| ≤ $0.02 | Halt (H3) [SR] |
| C6 | Target CTR/CVR recompute | Within 2%; fail if > 10% of rows off | Halt (H4) [SR, PF] |
| C7 | SQP roll-up integrity | §5.4 step 6 | Rebuild the roll-up [SQP] |
| C8 | SV% | Σ SV% = 1.0 | Fix the denominator [MDB] |
| C9 | Keyword PPC totals | Keyword total = Σ its campaign rows | Rebuild the grouping [KCP] |
| C10 | STR spend distribution | Spend % sums to 100%; grand total = STR total for the portfolio | Rebuild [STR] |
| C11 | Rows in = rows out; spend to the cent after any merge | Exact | Rebuild the merge [PF] |
| C12 | kw + PT spend vs advertised-product report | Equal within the same window | Find missing rows (paused ad groups with spend, other portfolios) [PF] |
| C13 | LTSF charge | units × cu ft × rate vs invoice within a fraction of 1% | Show both scenarios; charges "approximate" [LTSF] |
| C14 | Execution of last cycle's changes | Actual vs recommended within $0.01 (EXECUTED); actual vs before within $0.005 (NOT EXECUTED) | Report execution rate; < 80% = follow-through problem [SR] |
| C15 | Two rank sources on the same term | Report both; name which governs (daily crawl / Data Rova primary) | Data condition if > ~7 places apart [B6] |
| C16 | Campaign census | Every campaign spending on the product's ASINs is in the decision list | Add missing campaigns and mark them; no write on a campaign without its current state [B6 F13] |
| C17 | Paused-ad-group rows with spend; blank Syntax / SV / Objective | Listed | Classify or hold [PF] |

---

## 7. Data-validity quarantine

Quarantined rows get **no recommendation**, only a refresh task (same-day where possible). [PB, WB, SR]

| Condition | Rule |
|---|---|
| CVR or ACoS stated with 0 orders; ACoS without sales | Quarantine |
| CTR stated with 0 impressions/clicks; CTR = 0 with clicks; CVR = 0 with orders | Quarantine |
| Same metric conflicting across bulk / console / Sellerboard / SQP | Quarantine until settled |
| Duplicate values copied across rows (identical odd numbers) | Quarantine; verify at source |
| Stale economics (§8) | Quarantine every ceiling-referencing verdict |
| Implausible volume (SV implausible vs SFR, identical odd SV across files — e.g. a 400k+ fragment repeated in 5 files) | Verify; exclude from totals [LP] |
| 0% in-budget time with $0 spend | **Missing data**, not budget truncation [PB] |
| Velocity from an out-of-stock, suppressed or deal window | Not at face value: record trailing velocity, correction factor and its basis; an unstated haircut is rejected [LTSF] |
| Window straddling a price change, lever change or deal | Split the window; judge the clean part only [LTSF, B6] |
| Placement verdict on < 30 clicks per arm | "Directional" only (reference 02 §10) [PF] |

---

## 8. Freshness rules

| Input | Limit | Consequence | Source |
|---|---|---|---|
| Economics (margin table) | > 45 days, or any price / fee / size tier / remeasure / packaging / freight / LTSF change | Re-derive margin and every ceiling within 48 h; until then no ceiling-referencing verdict | PB, SR |
| Sellerboard | True-up monthly | Margin trend (WoW / MoM) read separately from freshness | PB |
| MKL | > 30 days | Stale: coverage, tiers and relevancy flagged | PB |
| Rank history | < 1 month | Out of scope for ranking verdicts; ≥ 1 month (ideally 3) needed; exclude stock-out and re-route stretches | PB |
| Attribution | Last 7 days | Read low; compare settled windows only | B6 E2 |
| Deal window | During + 2 weeks after close | Excluded from trend verdicts; grading span overlapping a deal → no verdict (DEAL WINDOW) | PB, SR |
| ASINsight exports | > 2 days apart | Not comparable to each other | ASINsight tool |
| Bulk export | Not same-day as the upload build | IDs may be stale (H6) | CB |
| Inventory | Not same-day as the bulk | Re-pull before zoning | WB |
| Manifest completeness | < ~85% of expected inputs/fields | Run labelled "degraded" | PB |
| Pending dated COGS change | — | Carry current-COGS margin for live decisions + future-COGS margin as context | PB |

In an **Analysis**, staleness is reported as a finding; in a **Plan**, it blocks the dependent verdicts. [PB]

---

## 9. Two-scope architecture

| | Product scope | Campaign scope |
|---|---|---|
| Unit | Parent ASIN / product | Every campaign that advertises any of the product's SKUs |
| Source | Product report / Sellerboard / Command Center product tile — single source of truth, **never recomputed from bulk** | Bulk + STR + placement + targeting reports |
| Includes | Organic + ad sales, total units, TACoS, organic share, margin after ads | **Sibling portfolios** where the product's ranking spend lives (e.g. two portfolios for one product family); shared multi-product campaigns flagged |
| Used for | Trends, goal/stage signals, spend limit, margin rule | Every campaign, keyword and placement decision |

Rules:
1. Reconcile the two openly: campaign scope usually exceeds product scope because of halo sales on other ASINs. State the gap. [QA]
2. Using one portfolio when ranking spend sits in a sibling portfolio produces false reads (the "$94 artefact": ranking spend looked like $94 because the rest sat in the sibling). [QA]
3. **Shared campaigns** (advertise other products, multi-SKU LTSF/auto): excluded from colour and price automation; reviewed in their own product's analysis; spend attributed on product basis (C2). [B6 E13]
4. **Reverse sweep:** search the whole account for the product's child ASINs; every campaign found is decided or marked out of scope with an owner and date. [WB]

---

## 10. Unmeasured ≠ zero

1. A competitor without an export is **unmeasured**, not absent; its traffic is null, not 0. [ASINsight, R-CI12]
2. Every share, contest or "we win" figure states its **coverage** (e.g. "13 of 32 mapped competitors measured"). No conclusion about an unmeasured competitor. [R-CI12]
3. A term with no rank on a day is **unranked**, not a rank; unranked days count toward the median as 101 (not ranked); rank = NR if ≥ half the days are unranked. [B6, SR]
4. A day the crawler didn't run is marked missing, not unranked. [rank crawl]
5. A missing SQP match leaves targets blank. [E]
6. Zero conversions on a thin sample = unknown (affordable CPC = 0 → leave the bid, flag). [PB]
7. A missing section in a report reads "Not available" — never placeholder numbers. [QA]

---

## 11. Data-conditions register

One row per condition; write it at the end of Phase 0 and keep it through the cycle. [PB, DR, WB]

| Field | Content |
|---|---|
| ID | DC-01, DC-02… |
| Condition | What is missing, stale, conflicting or unverified |
| Evidence | File / sheet / column / window and the numbers showing it |
| Why it matters | The mechanism (e.g. "ceilings rest on a 52-day-old margin") |
| Actions gated | Exactly which decisions are held or labelled provisional because of it |
| Workaround used | Fallback applied and its label (e.g. "portfolio medians — provisional"), or "none" |
| Owner | Named role responsible for fixing it (a gap with no owner is not recorded) |
| Due | Date |
| Asked? | Date asked and answer (ask once before logging) |
| Status | Open / resolved / withdrawn (withdrawn findings stay with the overturning evidence) |

---

## 12. Verifying what a column really measures

Before using any column in a decision, confirm its meaning from the data, not the header. [PF, WB]

| Check | Example trap |
|---|---|
| **Grain** — campaign, keyword, placement, day? | Placement split is campaign-grain; a keyword's placement split is an estimate [B6] |
| **Does it carry orders?** | Bulk placement rows may carry no orders — placement CVR needs the placement report [SR gap] |
| **Attribution basis** | `7 Day Total Sales` includes halo (other ASINs; up to 81% halo seen); `7 Day Advertised SKU Units` does not [PF, INV] |
| **Market vs ours** | Data Rova "Weekly Sales" and DSTR are **market** figures at a rank, not our sales [PF] |
| **Snapshot vs window** | Bid, boost, budget and state are snapshots; performance columns are window sums |
| **Traffic vs scores** | ASINsight 7-day traffic is impression-like (not clicks or sales); placement-trend scores are scores — never add them to traffic |
| **Rank encoding** | 0 / blank / 101 = not ranked, depending on tool [SR] |
| **Units** | LTSF is $ per cubic foot, not per unit (per-unit reading overstates 1.4–4.8×) [LTSF] |
| **Sign conventions** | Sellerboard advertising cost is negative; profit before ads = Net profit + \|advertising\| |
| **Fee bundling** | Sellerboard fees bundle referral + FBA + storage + inbound; fee/ASP > 55% = contaminated (reference 02 §4) [SR] |
| **Inventory family view** | Use the full inventory export, never the variation/family page [PF] |
| **Budget cap vs spend** | A budget is a cap, not spend; committed spend = run-rate of enabled campaigns [WB] |
| **Precomputed rates** | Recompute SQP and engine rates from counts; never trust exported rates [SQP] |

Test method: recompute one row by hand from raw counts; compare two windows; compare against a second source; if it still doesn't reconcile, log a data condition and do not use the column for money.

---

## 13. Open questions for the owner

1. **Bulk vs Command Center spend tolerance (C1):** no source sets a numeric tolerance. Until the owner sets one, every unexplained gap is stated in $ and % and treated as a halt only when it changes a decision.
2. **Inventory velocity basis:** Resolved — see 13 #49: zones use the 30-day actual pace (deal/stock-out windows corrected and labelled), with the inventory file's planned velocity shown beside it; never the push pace.
3. **Data Dive niche freshness** for price claims has no source limit (§3 #12). Set one.
