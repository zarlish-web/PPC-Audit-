# 02 — Metrics and formulas (dictionary)

Every metric the framework computes or cites: what it is, the exact formula, where it comes from, the window, how to validate it, the thresholds that use it, how it moves a decision, and the traps. Cite from here; don't redefine metrics elsewhere.

## Contents
1. Conventions (windows, blanks, rounding)
2. Traffic and funnel
3. Cost and efficiency
4. Unit economics and price limits
5. Placement and bidding
6. Market, SQP and keyword metrics
7. Rank and ranking sizing (DSTR)
8. Inventory and LTSF
9. Delivery, budgets and execution
10. Sample floors and significance
11. Competitor and market landscape
12. Open questions for the owner

Column key for the tables: **Formula** (definition = formula) · **Source / window** · **Validate** · **Thresholds** · **Drives** (decision it moves) · **Pitfalls**.

---

## 1. Conventions

1. **Safe division:** `a ÷ b` is blank when b = 0 — never 0, never ∞ in delivered text (engines may carry ∞ internally for ACoS with spend and no sales). [E]
2. **Recompute rates from summed counts**, never average rates. Group CTR = Σclicks ÷ Σimpressions. [SR, B6]
3. **Windows:** current 7 d vs prior 7 d = action evidence; 30 d and 90 d = judgement windows; 60–90 d = baseline; SQP 13 weeks. Attribution is 7-day: the last 7 days read low. Deal days and 2 weeks after a deal are excluded from verdicts. [PB, B6]
4. **Per SKU, per placement.** Money metrics are computed per advertised SKU (colour/size) and per placement; blended numbers are context only. [SKILL]
5. **Deal state separate:** margin, CVR, rank arc and counts are computed separately for deal and clean periods, never blended. [PB]
6. **Every number is dated** and names its source in delivered text. [PB]
7. **Rounding for sizing:** required clicks and budgets round **up** (ceil), never `round()`. [PF]

---

## 2. Traffic and funnel

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Impressions | Count of ad impressions | Bulk / Command Center; 30/90 d | Final on day one | CTR verdict needs ≥ 1,000 | CTR denominator; impression share | Deal days inflate [B6] |
| Clicks | Count of ad clicks | Bulk / Command Center / STR; 30/90 d | Final on day one | 15 = bid read floor; 100 = CVR verdict; 11 for product targets | Read floor for every judgement [PB, SR] | Clicks on paused-ad-group rows still count to spend (C17 in 01) |
| CTR | clicks ÷ impressions | Same; market CTR from SQP 13 wk | Recompute from counts | vs Target CTR = Market CTR × 1.10; fail < 0.9 × target | Four-quadrant; listing gate | Placement mix changes CTR — read at the delivering placement, not blended (blended 0.63% vs TOS 2.96% in one case) [DR] |
| Orders | Ad-attributed orders (7-day) | Bulk / STR `7 Day Total Orders (#)` | Last 7 d settle | Harvest ≥ 3; zero-order ≥ 20 clicks | Conversion, harvest, zero-order | Trailing-week under-count [B6] |
| Units | Ad-attributed units | STR `7 Day Total Units (#)`; Targeting `7 Day Advertised SKU Units` | Units ÷ orders stable (B6 1.03) | — | PPC velocity (advertised SKU only) | Total units include halo SKUs [INV] |
| CVR | orders ÷ clicks | Bulk / STR; 30/90 d | ≥ 100 clicks for a verdict | Keyword Target CVR = Market CVR × 3.0; syntax target Market × 1.10 | Break-even CPC; qualification; stop rule | Deal days lift CVR; don't read on < 15 clicks [B6] |
| CVR by placement (TOS / ROS / PDP) | placement orders ÷ placement clicks (campaign grain) | Placement report; **90 d** | Needs placement orders (bulk placement rows may lack them) | Conversion basis: own ≥ 50 clicks; blend 15–50; size/product rate < 15 (§5) | Break-even CPC per placement; push stop (TOS CVR < market on 50+ clicks) | Campaign grain only; keyword placement CVR is an estimate [B6] |

---

## 3. Cost and efficiency

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Spend | Σ ad cost | Bulk / Command Center; daily/30/90 d | Reconcile bulk vs console (01 C1–C2) | Owner spend limit | Spend limit, budgets | Product tile ≠ Σ campaign rows when campaigns are shared [B6] |
| CPC | spend ÷ clicks | Same | — | vs break-even CPC and ceiling | Price checks | Down-only bidding lowers realised CPC below the bid [B6] |
| Sales (ad) | Σ 7-day attributed sales | Bulk / STR `7 Day Total Sales ` | Settle 7 d | — | ACoS, RPC | Includes halo sales on other ASINs [PF] |
| ACoS | spend ÷ ad sales | Same; 30 and 90 d | Blank with 0 sales (quarantine if stated) | Break-even ACoS; 2 × BE = block line; non-ranking: over BE on both 30 & 90 d → cut ≤ 30% of base; > 2 × BE on ≥ 30 clicks → BLOCK; ≤ 50% BE with orders → scale-eligible (+≤ 25%) | Non-ranking CUT/REDUCE/BLOCK/SCALE; keyword rules | Deal price lowers AOV and raises ACoS [13 #16, B6] |
| Real ACoS | spend on rows **with** sales ÷ sales | STR | — | Healthy < BE (STR default 30%) | Match-type/root health | Excludes waste by design — always shown with WAS% [E] |
| ROAS | ad sales ÷ spend | Bulk | = 1 ÷ ACoS | — | Reported only | — |
| CPA (cost per order) | spend ÷ orders = CPC ÷ CVR | Derived | — | ≤ margin/unit (non-push); ≤ 2 × margin/unit (push) | Push loss bound; conversion objective judged on CPA vs ceiling | Blank with 0 orders [B6, PB] |
| AOV | sales ÷ orders | Sellerboard / bulk; 30 d | — | — | BE ACoS conversion; AOV source by objective: advertised SKU (Ranking, Conversion), routed SKU (Conquest), campaign blend (Discovery) | AOV shift from variation mix voids every ceiling until economics refreshed [PB] |
| RPC (revenue per click) | ad sales ÷ clicks | Bulk; per placement where possible | — | — | RPC ceiling | Basket sales incl. halo [PF] |
| RPC ceiling | RPC × break-even ACoS | Derived | = margin-based BE CPC when AOV matches | Caps any RPC-derived bid | Non-ranking bid cap | Uses blended RPC unless placement RPC exists [SR] |
| TACoS | ad spend ÷ total sales (refund-net) | Sellerboard / product report; weekly | Total sales from the product report | **No target unless the owner sets one**; PB bands (Launch ≤ 25%, Ranking push 12–15%, Transition 8–12%, Mature 4–7%, Harvest ≤ 4%) reference only | Monitor and decompose (paid vs organic movement); never a bid gate | Sizing spend on a "TACoS rung" was a documented failure [13 #17, B6 F24] |
| Organic share | (total sales − ad sales) ÷ total sales | Product report; weekly | Product scope only | Graduation signal: organic > ~40–50% sustained [PB]; Quick-audit floor 60% [QA] (reference) | Stage integrity (graduate / demote after 4 weeks below target) | Ad sales include halo; attribution double-counts are possible |
| WAS% (wasted-spend share) | spend on rows with 0 sales ÷ spend | STR; per campaign | — | Ceiling **10%** of campaign spend (**40%** discovery); product-level waste reported | Negation pass trigger | Negation is decided by relevance, not by WAS% alone [13 #24] |
| Waste share | group's zero-sale spend ÷ total zero-sale spend | STR | Σ = 100% | — | Where to look first | — |
| Marginal ACoS | Δspend ÷ Δad sales between two steps | Two clean windows around an executed change | Same length windows, no event | > 1.5 × average ACoS → freeze further raises at prior rung [SR]; > 2 × blended → unwind the step [PB] | Whether a raise bought profitable sales | Needs an executed step and clean windows |
| Marginal CPC | Δspend ÷ Δclicks | Same | Same | — | What the last step cost per extra click | Same |
| CPC ratio | realised CPC ÷ governing target price | Bulk | — | > 1.0 → push-only justification; > 1.5 → unjustifiable | Ceiling audit | Governing target = ceiling for pushes, BE CPC otherwise [SR] |
| Margin after ads | (profit before ads − ad spend) ÷ sales | Sellerboard; weekly | — | Owner margin rule (e.g. ≥ 10%; event exceptions dated) | Spend limit; weekly push cut from the bottom of the funded list | [B6 R-F5/F6] |

---

## 4. Unit economics and price limits

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Margin/unit (profit per unit before ads) | **Sellerboard profit before ads ÷ units, per SKU/colour, at the price in force** = (Net profit + \|advertising\|) ÷ units. Component build (say so): ASP − COGS/unit − Amazon fees/unit, with COGS and fees ÷ **gross units** (units + \|refund count\|) | Sellerboard; **last 30 d**; deal price during deals | Fee/ASP > 55% → fee/unit = portfolio median fee/ASP (from SKUs with ≥ 10 units, 0 < ratio ≤ 55%) × ASP, logged "verify"; < 10 units → same-size median (≥ 10 units, positive) capped at own | Stale > 45 d | Every break-even and ceiling | Never blended parent; colours differ 2–3×; wrong margin inflated every ceiling ~40% in B6 [13 #1, SR, WB] |
| Break-even ACoS (CM2) | margin/unit ÷ price (= CM2 = (ASP − COGS − fees) ÷ ASP when built from components; no returns term) | Derived per SKU | Flag if outside **5–70%** | Target ACoS = BE for non-push rows; Quick-audit reference: target 50% BE, max 75% BE | Non-ranking and keyword cuts | Deal price changes it — recompute [13 #1, QA] |
| Break-even CPC (break-even price) | margin/unit × CVR **of the placement being bought** | Derived | CVR basis per §5 | Non-ranking: price ≤ 1.0 × BE CPC at every placement | Pricing base for every campaign | Wrong colour → wrong break-even; blended CVR hides TOS vs PDP gap [B6] |
| Ceiling (ranking) | **2 × break-even CPC** on the ranking term's TOS price (owner may set another multiple, or a term-specific time-boxed raise) | Derived | Price > ceiling → cut to ceiling now | Hard cap on pushes | PUSH sizing; over-ceiling correction | "Cost + 15%" ceilings drift upward (B6 F23); flat $8–9 cap is the alternative owner setting [13 #3] |
| Push premium | +25% if rank ÷ target ≤ 1.5; else (rank ÷ target − 1) × 50%; 0 when rank ≤ target | Derived from rank | Rank from governing tracker | Capped by the ceiling (so ≤ +100% at 2×) | Push price | Flat premium across all terms = not derived [13 #4, PB] |
| Push price | break-even CPC × (1 + premium), ≤ ceiling | Derived | ≤ ceiling | Raise ≤ +30%/day toward it while not holding top | TOS price target for PUSH rows | Never set from competitor or suggested bids [B6] |
| Clicks-to-loss | margin/unit ÷ CPC | Derived | — | — | Quick read: clicks per order before a loss | [PB] |
| Weekly loss ceiling (ranking) | (push ACoS − BE ACoS) × projected sales at required spend | Derived | Basis stated; ≥ 1 day's spend | Hitting it → owner flag, not auto-stop | Ranking funding | [PB] |
| Deal-state margin | (deal price − COGS − fees − deal fees) per unit | Deal calendar + Sellerboard | Computed before the event | Deal-state ceiling = deal margin × CVR | No bid above the deal-state ceiling; in-deal CVR never justifies more | A discount cuts contribution by its full depth [PB] |
| Affordable CPC per placement | margin/unit × that placement's CVR | Derived | — | TOS / ROS / PDP each judged separately | Placement pricing | Never judge placements on one blended number [PB] |

---

## 5. Placement and bidding

**Conversion basis for any placement ceiling** (13 #2): n = own placement clicks (90 d). n ≥ 50 → own placement CVR. 15 ≤ n < 50 → linear blend: w = (n − 15) ÷ 35; CVR = w × own + (1 − w) × size rate. n < 15 → size (or product) placement rate. [B6]

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Base bid | Keyword/target bid (applies at ROS and PDP; PDP moves only via base) | Bulk snapshot | — | Base cut ≤ 50% per step; base ≥ TOS price ÷ 10; floor $0.35–0.50 (≥ clearing ÷ 10) | Mix fix | Base cut must not drag TOS price down [WB, B6] |
| Boost (TOS modifier) | Placement Top percentage | Bulk snapshot | 0–900% | ≤ 900% | TOS price | At cap: raise base only to price ÷ (1 + boost) [B6 R-M2] |
| **TOS price** | **base × (1 + boost)** | Derived | Recompute ±$0.03 | ≤ ceiling (push) / ≤ BE CPC (non-push) | The price every push rule writes | Down-only may pay less [B6] |
| Effective TOS bid (by strategy) | Fixed / down-only: base × (1 + boost). Up-and-down: up to base × (1 + boost) × 2.0 at TOS (Amazon may raise up to 100%) | Derived | Up-and-down effective bid must clear the ceiling × 1.05 | Breach → re-solve base = ceiling ÷ ((1 + boost) × multiplier) | Ceiling audit | Existing strategies are left unchanged [SR, 13 #8] |
| TOS rebuild (hold TOS price when base changes) | new boost % = (target TOS price ÷ new base − 1) × 100 | Derived | 0–900 | Written in the same row as the base change | Mix fix, base cuts | Letting TOS fall as base-cut residue is a defect [SR, WB] |
| Clearing CPC (TOS) | TOS spend ÷ TOS clicks per campaign (≥ 3 TOS clicks, else portfolio value) | Placement report; 30 d | — | Effective TOS < clearing → priced out (serves on PDP) | Placement-first diagnosis | Low sample → portfolio fallback, labelled [PF] |
| TOS CPC | TOS spend ÷ TOS clicks | Placement report | — | Ceiling ≥ TOS CPC to qualify a push | PUSH qualification (else WAIT) | [B6 R-P1] |
| TOS impression share | our TOS impressions ÷ available TOS impressions | SP Targeting report (required); 14–90 d | Per target | **≥ 30% = holding the top** (push stop/step test); Quick-audit reporting target 22.5% | Daily push step; at ceiling 3 days without top-3 sponsored and ≥ 30% → owner | With ≥ 5 rivals at SP #1–5, not a pass/fail signal alone — judge rank after 7 days [B6, R-CI5] |
| TOS click share | TOS clicks ÷ campaign clicks | Placement report; 30 d | Campaign grain | < 30% of clicks while clicks ≥ plan → PLACEMENT FIX FIRST | Mix fix | Distinct from impression share [PB] |
| Placement mix (click shares TOS / ROS / PDP) | placement clicks ÷ campaign clicks | Placement report; 30 d | Σ = 100% (excl. off-Amazon) | Ranking: TOS 70–90%, PDP ≤ 20% (on ≥ 15 clicks) | MIX FIX: base −50% (−25% if PDP brings orders), boost raised so TOS price holds, same write; re-check day 7 | Keyword-level mix is an estimate [B6 R-M1] |
| Placement cost per order | placement spend ÷ placement orders | Placement report | — | — | Efficiency comparison across placements | Needs placement orders [PF] |

---

## 6. Market, SQP and keyword metrics

SQP rates are recomputed after the parent roll-up (01 §5.4): **brand counts summed, market counts taken once.**

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Market CTR / CVR | Mkt clicks ÷ Mkt impressions; Mkt purchases ÷ Mkt clicks | SQP; 13 wk | Brand ≤ Market | — | Benchmarks | Summing market columns across children destroys every share [SQP] |
| Brand CTR / CVR | Brand clicks ÷ Brand impressions; Brand purchases ÷ Brand clicks | SQP | — | E15 listing flag: ours < market on ≥ 30 clicks → WAIT (no push until listing checked) | Four-quadrant; push qualification | Brand = all our children, organic + paid [B6] |
| Impression / click / cart-add / purchase share | Brand count ÷ Market count at that stage | SQP | 0–100% | — | Share trend; Defensive "share held" (IS per branded query where available) | — |
| CTR / CVR variance | Brand − Market (points) | SQP | — | — | Reported | — |
| Market price / brand price | Market: `Purchases: Price (Median)` taken once; Brand: median of children's ASIN price | SQP | — | — | Price position | — |
| Revenue / Rev per click (SQP) | purchases × price; revenue ÷ clicks | SQP | — | — | Context | — |
| Target CTR | Market CTR × 1.10 | Derived | Recompute; > 2% drift on > 10% of rows → halt | — | Four-quadrant | Blank without SQP — never guessed [13 #20] |
| Target CVR | Keyword: Market CVR × 3.0 · Syntax: Market CVR × 1.10 | Derived | Same | — | Keyword/syntax diagnosis | Keyword vs syntax multipliers differ [QA] |
| Four-quadrant (per syntax) | CTR pass = CTR ≥ 0.9 × target; CVR pass likewise → **STRONG** (both pass: scale) · **VISIBILITY** (CTR fail, CVR ok: buy placement) · **CONVERSION** (CTR ok, CVR fail: fix offer, no rank push) · **BOTH FAILING** (reduce, fix listing first) | SQP + bulk | No SQP → portfolio medians, "provisional" | ≥ 4 weeks in a state = chronic (Conversion → bids at maintenance, no ranking allowance) | Mode of a syntax, never a keyword's bid | Medians are relative — half fail by construction [13 #20, PB] |
| SV (search volume) | Monthly searches (MKL/H10/SQP); weekly in ASINsight | MKL (≤ 30 d) | Sources don't reconcile — name the source | Tiers below; launch floor ~250; Cold gauntlet > 500 | Demand gate, tier, hero/halo | Artefact volumes (implausible vs SFR) excluded [B6, LP] |
| SV tier | VHSV ≥ 10,000 · HSV 1,000–9,999 · MSV 500–999 · LSV 100–499 · VLSV < 100 | Derived | — | VHSV/HSV (or rank-targeted) = hero, 1 keyword per campaign; MSV 3; LSV/VLSV 10 per halo campaign | Structure | [PH] |
| SV% | SV ÷ Σ SV (product universe) | Derived | Σ = 1.0 | — | Coverage % by volume, not keyword count | [MDB] |
| Relevancy % | Listing scorer vs live title + bullets (first match wins): disqualifier 0 · ≥ 3-word phrase verbatim 92 / 2-word 85 · 4-/3-/2-gram overlap 78 / 64 / 50 · off-topic 0 · theme match 36 · unigram round(15 + 15 × overlap ÷ words) · no match 0 | Listing copy + MKL | Keep original MKL label beside it | Decisions: **≥ 60% high · 35–60% moderate · < 35% not relevant** | Negation tree, harvest filter, launch tier | Non-English ≈ 0 means no on-page text, not irrelevance [13 #30, LP, STR] |
| Keyword CVR ratio vs market | our CVR ÷ market CVR | Bulk + SQP | ≥ 30 clicks | < 1.0 → listing check | Push qualification | [B6] |

---

## 7. Rank and ranking sizing (DSTR)

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Organic rank | Median daily organic position over the window; unranked days count as 101; NR if ≥ half the days unranked | Rank crawl / Data Rova (primary) / Data Dive (gap-fill); 30 d | ≥ 1 month history; exclude stock-out and re-route stretches | — | Premium, qualification, HOLD RANK | Two tables can disagree ~7 places — name the governing one [B6] |
| Sponsored rank | Observed ad position on the results page | ASINsight / hourly read | Not available for every term | Top-3 most hours = holding | Daily push step | [B6] |
| Rank ratio | current rank ÷ target rank | Derived | — | ≤ 1 at target; ≤ 1.5 moderate; > 1.5 full premium | Push premium | [B6, WB] |
| Rank gap | organic rank − target rank (places) | Derived | — | Reach ≈ 30 places for push candidacy | PUSH qualification; harvest objective (> 10 places → Ranking) | [KCP, B6] |
| Rank drop | rank now − rank 30 days ago | Rank crawl | — | > 10 places while getting clicks → freeze price, find cause (listing, colour, keyword state, competitor, stock) | Rank-loss investigation (never a bid raise) | Stock signature: collapse concentrated in one colour/size during an outage [B6, LTSF] |
| Rank arc | overall, 14 d and 7 d reads stated separately; clean arc governs, deal arc separate | Rank crawl | — | Shorter windows = early warning | Ranking state test (reference 06) | [PB] |
| **DSTR** (daily sales to rank) | Daily sales (organic + paid) needed at the target rank, from market data (Data Rova / ASIN Insights / competitor sales at that rank); **DSTR = max(1, ceil(stated))** | Data Rova / ASIN Insights; weekly | Feasibility: vs SQP market purchases ÷ 30 — DSTR > 50% of market daily purchases = re-scope (not a gate); market can't support 1/day → route out of Ranking | Floor 1/day | Push volume and budget, **never price** | Market weekly sales are the market's, not ours [13 #19, PF, SR] |
| Organic sales on the term (proxy) | DSTR × our organic traffic share on the term (or measured organic sales) — labelled **proxy** | ASIN Insights traffic distribution | organic + paid = DSTR ± 0.02 | — | Netting | SQP brand coverage can be ~1% — say what the proxy rests on [PF] |
| Paid sales needed | max(DSTR − current organic sales on the term, 0) | Derived | — | — | Required clicks | Not netting doubles spend (known defect) [13 #19] |
| Required TOS clicks/day | paid sales needed ÷ **own achieved TOS CVR** | Derived | Column must vary across terms | — | Budget | Never a target/planning CVR [PF] |
| Required budget/day | ceil(required clicks × TOS price × 1.05) | Derived | Budget ≥ requirement × 1.05 | Within spend limit; Σ requirements reconciled to product sales (upper bound) | Budget line, funding order | Requirements set volume, never price (B6 F21) |

---

## 8. Inventory and LTSF

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Available stock | FBA sellable units | Inventory export; snapshot | On-hand − available − reserved gap ≤ 5 units | ≥ 7 days of cover to push; 0 → pause push, ranking ads to backup | Push gates | Transfers and customer orders are not available [B6 R-I6] |
| Velocity | units sold ÷ days | Sellerboard; **30-day pace** (7-day as warning) | Correct OOS/deal/suppressed windows with a stated factor | Clearance colour: velocity ≤ size median | Cover, clearance choice | Never the push pace (inflated forecast created a false stock-out in B6 F30) |
| PPC velocity | Σ 7-day advertised SKU units ÷ window | SP Targeting report | Advertised SKU only | — | Share of velocity bought by ads | [INV] |
| Days of cover (DOC / DOH) | available ÷ units per day | Derived | Same-day snapshot | **Green ≥ 60 · Yellow 21–59 · Red < 21**; stock-out before inbound arrives = Red regardless | Inventory gate; Yellow = no new push; Red = protect/re-point | High DOC with velocity down 15% WoW for 3 weeks = trajectory problem [13 #9, PB] |
| Days to next arrival | dated confirmed arrival − today | Inventory inbound | Confirmed dated only; "Not in Horizon" = blank | Gap ≤ 7 days = TIGHT (ease, don't swap); cover < arrival by > 7 days → switch to backup (same size) | Variation routing | Inbound counts only if ETA ≤ DOH [B6, WB] |
| Push stock test | DOC ≥ days to next arrival + 7 | Derived | — | Fails → no push | PUSH gate | [13 #9] |
| Max affordable velocity | stock ÷ lead time; incl. transit: (stock + transit) ÷ lead time | Inventory; lead time default 90 d | — | Velocity > max (stock) → reduce PPC aggression; < max (incl. transit) → scale carefully | Inventory × PPC action | Lead time is an input — confirm per product [INV] |
| Projected DOC | (stock + dated inbound) burned at baseline velocity + planned order gap, to the checkpoint date | Derived | Same data version as the push sizing | Must stay Green (> 21 d minimum for launch floor) through the checkpoint | Blocks a push that would push the SKU into Yellow/Red | [PB, WB] |
| Backup cover | backup stock ÷ **preferred SKU's velocity**; also (stock + transit) ÷ velocity | Inventory + mapping | Only for advertised preferred SKUs | ≥ lead time = covers; ≥ 30 d = partial; else insufficient; stock + transit = 0 = backup also OOS | Backup switch recommendation | Backup already advertised → the swap competes with its own campaign [INV] |
| LTSF rate | $ per **cubic foot** per month by age: 181–210 d $0.50 · 211–240 $1.00 · 241–270 $1.50 · 271–300 **$5.45 (cliff)** · 301–330 $5.70 · 331–365 $5.90 · 366–455 $6.90 (or $0.30/unit if greater) · 456+ $7.90 (or $0.35/unit if greater); assessed on the 15th | Amazon rate card | Charge reconciles to invoice | Cliff at 271 d | Clearance timing | Rate card may change — confirm current [LTSF] |
| LTSF per unit | rate × cu ft/unit (≥ 366 d: max with per-unit floor) | Derived | — | — | Floor price | Per-unit reading overstates 1.4–4.8× [LTSF] |
| Months to clear | aged units ÷ monthly velocity (cap 12) | Derived | Velocity basis stated | > 3 → Yellow; > 6 → Red (tier script) | LTSF tier | [LTSF] |
| Floor price | (salvage + LTSF until sold + FBA fee) ÷ (1 − referral %) | Derived; LTSF until sold = LTSF/u/mo × min(months to clear, 12) | Floor ≥ price → no discount authority | — | Lowest price that beats salvage | COGS is sunk — never in the floor [LTSF] |
| Break-even discount | LTSF until sold ÷ net proceeds at current price (net = price × (1 − disc) − referral − FBA) | Derived | n/a if net ≤ 0 | < 20% coupon/price drop · 20–40% outlet · > 40% salvage comparison · > 100% no depth pays | Clearance route | [LTSF] |
| Salvage per unit | max(removal net, liquidation net, disposal) with removal net = resale − removal fee (~$1.07) − 3PL; liquidation net = price × 7.5% − price × 2.5% | Defaults stated | Replace defaults before terminal calls | — | Floor price | [LTSF] |
| Max combined depth | max(0, 1 − floor ÷ price) per child | Derived | — | Stacking cap | Promo depth | [LTSF] |

---

## 9. Delivery, budgets and execution

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| Budget utilisation | spend ÷ daily budget | Console; 7–30 d | — | Floors: Defensive 100% · Ranking 80%+ · Discovery 70%+ | Budget before bids (Defensive) | A budget is a cap, not spend [PB, WB] |
| In-budget share (truncation) | share of the day the campaign stayed in budget | Console | 0% with $0 spend = missing data | **< 70% = truncated**: all rates unreliable, budget first | Delivery gate | Truncated data isn't bid evidence [PB] |
| Budget (push) | required TOS clicks × TOS price × 1.05 (+ expected PDP spend) | Derived | Price and budget rows load together | Min $10/day; > $500 → review; cuts > $50/day need approval | Push funding | A capped budget stops a push mid-day (B6 F14) [SR, PB] |
| Committed spend | run-rate spend of enabled campaigns (not caps) | Console; 60 d | — | Headroom = spend limit − committed | Funding order | [WB] |
| Pacing deviation | actual spend pace vs the product's day-of-week curve | Console daily | — | > ~25% swing → flag same day | Event/pacing control | [PB] |
| Execution status | EXECUTED if \|actual − recommended\| ≤ $0.01; NOT EXECUTED if \|actual − before\| ≤ $0.005; else PARTIAL | Current bulk vs action log | — | — | Grading eligibility | Never grade an unexecuted action [SR] |
| Execution rate | executed ÷ logged actions | Action log | — | **< 80% = follow-through problem** | Process finding | [SR] |
| Grade delta | Ranking: Δ organic rank; others: Δ ACoS (points) | Ledger | ≥ 15 fresh clicks; after horizon | ≤ −3 WORKED · ≥ +3 BACKFIRED · else FLAT; margin/BE shift > 10% → provisional | Escalation (2 consecutive flat/backfired) | Deal-window overlap → no verdict [SR] |

---

## 10. Sample floors and significance

| Read | Floor | Below the floor |
|---|---|---|
| Bid verdict | 15 clicks (product targets 11) | Hold; formula-only correction if over ceiling [13 #11] |
| CVR verdict | 100 clicks (own TOS CVR usable from 50) | Use the conversion basis blend (§5) |
| CTR verdict | 1,000 impressions | No CTR verdict |
| Zero-order rule | ≥ 20 clicks, 0 orders | REDUCE (relevant, owned) / BLOCK (irrelevant); irrelevant negation from 5 clicks |
| Converting rows | Skip the sample gate | — |

**Significance test for two rates** (placement vs placement, period vs period) [PF]:
- SE = √( p1(1 − p1) ÷ n1 + p2(1 − p2) ÷ n2 )
- CI95 = (p1 − p2) ± 1.96 × SE
- CI excludes 0 → **proven**; min(n1, n2) < 30 → **directional** (no verdict); otherwise **insufficient**.
- Never a blanket TOS shift on a directional read.

---

## 11. Competitor and market landscape

Coverage rule: every figure states how many mapped competitors were measured; unmeasured ≠ zero. [R-CI12]

| Metric | Formula | Source / window | Validate | Thresholds | Drives | Pitfalls |
|---|---|---|---|---|---|---|
| 7-day traffic (ASINsight) | Tool's 7-day traffic per keyword/ASIN — **impression-like**, not clicks or sales | ASINsight exports | Exports ≤ 2 days apart to compare | — | Market size, shares | Never add placement scores to it [ASINsight] |
| Share of tracked traffic | our 7-day traffic ÷ Σ tracked traffic (us + measured rivals) | ASINsight market | Coverage stated | — | "How big are we here" | Excludes unmeasured sellers (B6: 2.1% with 13 of 32 measured) |
| Addressability | keyword state: **addressable** (fit-tagged/relevant to our product) · **disqualified** (disqualifier term, other brand, wrong size/category) · **unknown** | ASINsight addressability | Disqualifier vs fit-tag conflicts listed | Push candidacy needs addressable | What we can act on | Unknown share is reported, not assumed irrelevant |
| Rivals present (consensus) | number of measured rivals ranking on the keyword | ASINsight market keywords | Coverage | Push candidate: ≥ 7 of 13 rivals rank on it (B6 scale; restate per roster) + core wording | PUSH candidacy | Scale threshold to roster size — owner decision |
| Keyword state | contested (we and rivals rank) · ours only · theirs only | ASINsight | — | — | Gap lists | — |
| Win rate (contest) | contested keywords we win ÷ contested keywords; "win" = our traffic above the market average on that keyword (tool's contest call) | ASINsight competitor view | Coverage | — | Tier scoreboard | Working definition from the tool output (B6: win 11, lose 1,660 of 1,899) — confirm basis |
| Contest rate | contested keywords ÷ the rival's keywords | ASINsight competitor view | — | — | Overlap with a rival | No source formula; decide and record |
| Distance | our traffic ÷ their traffic (< 1 = they are bigger) | ASINsight competitor view | State whether total or contested-keyword basis | — | Rival profile ("almost level: distance 1.01") | Basis differs by tool view — say which |
| Paid share (market / ours) | paid traffic ÷ total traffic on the keyword | ASINsight | — | — | Ad intensity | — |
| Ad gap | market traffic × market paid share − our traffic × our paid share | ASINsight | Recompute one row | — | Where rivals out-advertise us | Traffic units (impression-like), not $ |
| Opportunity flag | **we_run_none** (they advertise, we don't) · **they_are_more_aggressive** (their ad share > ours) | ASINsight | — | Addressable core term ≥ 3,000 traffic with no search-term row → seed exact at break-even in discovery (B6 R-CI8) | Gap seeding | Engine is blind to terms with no clicks |
| Placement reach | keywords on which a seller appears per placement (organic, SP, SB, SB video, Amazon's Choice, product-page ads) | ASINsight competitor view | — | — | Ad-type gap (SB/SBV lane) | — |
| Placement scores | daily ASINsight scores per child ASIN: organic, SP, SB, SB video; compare first 7 vs last 7 days | ASINsight placement trends | Feed may be retired — state last day | — | Hero visibility trend | Scores, not traffic; never summed with traffic |
| Hero ASINs | fewest child ASINs carrying 80% of a seller's traffic | ASINsight | — | — | Which pages to target/defend | — |
| Traffic change | latest ÷ earlier export − 1 | ASINsight | Same basis both exports | Rival mover: traffic growth > 50%, price cut > 15%, new discount → hold our price 3 days before reading a CVR drop as a bid problem | Competitor-move hold (R-CI11) | Season moves everyone — compare to the rival median |
| BSR | Best Sellers Rank of the lead listing (lower = more sales) | Data Dive / Command Center brief | Dated | — | Rival size, trend | Category-specific; deal days distort |
| Est. units / revenue per 30 d | Data Dive estimate for the best-selling listing | Data Dive | Estimates — label | — | Rival profile, DSTR context | Listing, not whole brand |
| Rating / reviews | Stars; review count | Data Dive / Xray | Dated | Conquest entry: we win ≥ 2 of price / rating / review count, or target OOS | Conquest gate; Cold gauntlet (reviews ≥ ~50% of top-5 median, rating within 0.3★) | [PB] |
| Review velocity | new reviews per week between two dated reads | Command Center brief / Data Dive reads | Blank without a second read | — | Momentum; Fader archetype | Review themes are not in any connected source |
| Value per piece | price ÷ pieces in the set (or per unit of the offer) | Listing data | Same size compared | OFFENSIVE ASIN: priced above us for fewer pieces, or same price with < 50% of our reviews. AVOID and TEST classes: reference 08 (B6 AVOID examples: cheaper sets with far more reviews; other-material sets) | Competitor ASIN class OFFENSIVE / TEST / AVOID (R-CI7) | Compare same size only |
| Price position | our price ÷ niche median (or rival price) | Data Dive / SQP | — | Cold gauntlet: ≤ ~1.25 × category median | Offer diagnosis; conquest watch-CPA | Price never set from competitor data [R-CI4] |
| Tier | Aspirational / Beatable / Poor (mapping) | Competitor roster | — | Stretch target: only Aspirational rivals at/above target → judge on rivals passed (first milestone) | Landscape verdict (agrees / stretch / reachable / challenge) | Tier is a mapping input, not computed |

---

## 12. Open questions for the owner

1. **TOS impression-share threshold:** decisions use 30% ("holding the top", B6/SR/PB); the Quick Audit reports against 22.5%. This file keeps 30% for decisions and 22.5% as a reporting reference. Confirm.
2. **Marginal ACoS:** SR freezes raises above 1.5 × average ACoS; PB unwinds a step above 2 × blended. Applied here as a ladder (freeze at 1.5×, unwind at 2×). Confirm.
3. **Organic-share benchmark:** PB graduation ~40–50% vs Quick-audit floor 60%. Both are listed as references only; set the product's target.
4. **Contest rate, win rate and distance** have no formula in any source rulebook; the definitions above are read from the B6 tool outputs. Confirm the basis (total vs contested keywords).
5. **Rivals-present threshold** for push candidacy (≥ 7 of 13) was set for a 13-rival roster; how should it scale for other roster sizes?
