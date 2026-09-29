# 06 — Campaign and PPC decisions

The core decision logic for campaigns. Every campaign in scope gets one objective, runs the master decision order once, and ends with exactly one decision label, one action, an expected outcome and a validation date. Keyword-level rules (HARVEST, BLOCK, REDUCE, DEDUPLICATE, CHECK OWNER, MONITOR per term) are in `05-keyword-research.md`; price mechanics (backward-solve, DSTR, budgets, fixed-bid trial) in `07-placement-and-bidding.md`; economics in `03-…`; stock and variation routing in `04-…`; exceptions in `11-…`; grading and escalation in `10-…`.

Source tags: see `13-source-map-and-conflicts.md`. "#n" = conflict-register row n. Rule IDs (R-P1 …) are allowed in workbook Rule columns, never in narrative text (#28).

## Contents
1. Objective assignment
2. Campaign classes
3. Master decision order applied to campaigns
4. The campaign decision set (labels) and pause rules
5. Push qualification
6. Ranking progress test
7. Non-ranking campaigns
8. Levers, holds and reconciliation
9. Structure rules
10. Decision table (the trail)
11. Open questions for the owner

---

## 1. Objective assignment

### 1.1 Rule — per campaign block (Campaign ID), first match wins

| # | Test on the block's targeting | Objective | Source |
|---|---|---|---|
| 1 | Any keyword contains the brand name (brand + misspelling list, substring on lowercased term) | **Defensive** (brand broad included) | [OC, B6 R-O2] |
| 2 | Product targets only; ASIN is in our own product family | **Defensive** (own-page defence) | [WB, B6 R-X1, #15] |
| 3 | Product targets only; ASIN is another of our own brand's products | **Profitable Conversion** (cross-sell) — judged on its own ACoS, never as conquest | [B6 R-X2] |
| 4 | Product targets only; ASIN is a mapped competitor | **Conquest** | [WB, PB, #15] |
| 5 | Category targets, or ASINs not mapped to a brand | **Profitable Conversion** (unmapped: no SCALE until mapped) | [OC, WB, B6 R-X6/E20] |
| 6 | Targeting type = Auto | **Discovery** | [OC] |
| 7 | All keywords Exact and the term is generic niche wording (core, attribute, size) | **Ranking** — or **Market Share** only when the owner has declared it for that syntax | [OC, B6 R-O1, PB, #15] |
| 8 | All keywords Exact and the term is colour, competitor brand, other language, misspelling or adjacent generic | **Profitable Conversion** — a Ranking tag here is blocked | [B6 R-O1, F12, E18] |
| 9 | All Broad, all Phrase, or Broad + Phrase | **Discovery** | [OC, B6 R-O2, WB] |
| 10 | Exact mixed with Broad/Phrase in one block | **Ranking** (when the exact term is generic niche) + **structural flag**: split; usual fix = pause the broad, keep the exact — never on an event day | [OC] |
| 11 | Exact block mixing generic-niche and non-ranking term classes | Ranking only if the block holds the term with the declared target rank, else Profitable Conversion; flag for split | derived from OC + R-O1; record the basis |
| 12 | Nothing found | Profitable Conversion by default + verify the build in the console | [OC, B6 E7] |

**Liquidation (Clearance) is declared, never inferred.** A campaign is Liquidation only when every SKU it advertises is under a confirmed clearance/LTSF plan (file 04) or the product goal is Clearance/LTSF. It changes how the campaign is judged (stock cleared, §7.2), not its targeting rule. Never on a brand Defensive campaign or on a ranking campaign advertising the hero. [B6 R-N2, SR, PB]

### 1.2 Assignment discipline
1. **Campaign level, never per keyword.** Decide once per block, write to every row (campaign, keyword, placement, PT). Only exception: PT rows inside a keyword campaign stay on the ASIN-targeting loop — note it in the basis. [OC, DR]
2. **Name is evidence, not authority.** "(Ranking)" in a name never makes a campaign Ranking; targeting decides. Where name and targeting disagree, say so in the basis. [OC, #15]
3. **The goal authorises, it never retags.** A Profit-First product's generic exacts stay Ranking; the goal gate decides whether they may push. [PB]
4. **Market Share is never assumed.** Only when declared per syntax. [PB, #15]
5. Record three audit fields per block: objective before, basis, change. [OC]
6. **Validation (all must be 0):** blocks with >1 objective (PT rows excepted); blocks with none; Defensive without a brand keyword or own-ASIN target; Ranking without Exact; Ranking on a colour/competitor/language/misspelling term. [OC, B6 E18]

### 1.3 How each objective is judged — and never judged

| Objective | Judged on | Never judged on | Source |
|---|---|---|---|
| Ranking | Rank movement vs declared target and the loss ceiling (progress test, §6) | Weekly CPA/ACoS inside the push window | [PB, DR, OC] |
| Ranking after sufficiency stop | Standard ceiling judgement (break-even) | — | [PB check 6] |
| Market Share | Impression-share band migration and cost to hold it | Organic rank | [PB] |
| Profitable Conversion | CPA vs ceiling (= ACoS vs break-even on 30 & 90 days); realised vs affordable CPC. PT: product-page placement, target ASIN relevant and in stock | Rank | [PB, OC, B6 R-N1] |
| Defensive | Share held per branded query vs its own baseline + cost of defence; ACoS ≤ break-even | CPA alone | [PB, B6 R-N3] |
| Discovery | Converting terms per $100 spend, graduations to exact, harvest performance, wasted spend ≤ 40% | CPA in the first 30 days; any verdict before 15 clicks | [DR, PB, SR] |
| Conquest | CPA vs watch-CPA + share of the target page | Keyword metrics | [PB] |
| Liquidation | Units cleared vs the clearance timeline | ACoS cuts | [B6 R-N2] |
| SB / SBV / SD | Their own metrics: view-through CTR, completion rate, new-to-brand %, CPA | SP metrics | [PB, B6 E12] |

---

## 2. Campaign classes

A Ranking campaign is **push** only while its term is funded in the push plan (passes §5). Every other Ranking campaign is **non-push** and runs the break-even rules (BREAK-EVEN, R-B1–B4). Push status flips as qualification changes; the objective does not. [B6]

| Class | Identify by | Objective | Advertised variation | Price basis / ceiling | Judged by | Notes |
|---|---|---|---|---|---|---|
| Auto | Targeting type Auto | Discovery | Size's clearance colour (≥ 180 d cover, or ≥ 90 d while selling ≤ size median) | ≤ 1.0 × BE CPC every placement | Converting terms/$100, harvests, WAS ≤ 40% | Report and judge the 4 auto groups (close / loose / substitutes / complements) separately; own-ASIN auto matches negated. Mature stage keeps a low-budget auto sentinel [PB, WB, B6 R-C2] |
| Broad | All-broad keywords | Discovery (brand broad → Defensive) | Clearance colour | Launch ≈ 60% of the exact ceiling, no modifier | as Auto | Built only after 100 exact clicks or a coverage gap (§7.3) [PB, #23] |
| Phrase | All-phrase keywords | Discovery | Clearance colour | Launch ≈ 80% of the exact ceiling, no modifier | as Auto | Primary root at 0% phrase = structure gap [PB] |
| Exact — ranking, push | Generic niche exact, funded push term | Ranking | Size's best seller (hero) | TOS price → push price, ceiling 2 × BE CPC | Progress test §6 | One live owner per term; 70–90% of clicks at TOS, PDP ≤ 20% [B6 R-P1–P8, R-C1] |
| Exact — ranking, non-push | Generic niche exact, not funded | Ranking | Hero | Toward BE CPC (R-B1–B3) | Rank protection at BE | Rejoins push when it qualifies |
| Exact — non-ranking | Colour / competitor / language / misspelling / adjacent exact | Profitable Conversion | Colour terms: the named colour in the term's size; others: hero | ≤ 1.0 × BE CPC every placement | Layered rule §7.1 | [B6 R-O1, R-C3] |
| PT — competitor | Mapped competitor ASIN | Conquest | Routed SKU | Watch-CPA (§7.5); product-page lever, no TOS modifier | CPA + page share | Classified OFFENSIVE / TEST / AVOID (file 08) [WB, B6 R-CI7] |
| PT — own family | Own ASIN | Defensive | Hero | Low bid; ACoS ≤ BE | ACoS ≤ BE, share | [B6 R-X1] |
| PT — own other product | Own brand, other product | Profitable Conversion (cross-sell) | Routed SKU | ≤ BE | Own ACoS | Not a conquest [B6 R-X2] |
| PT — category | category="…" | Profitable Conversion | Routed SKU | ≤ BE | CPA vs ceiling | Category targets can't be bulk-changed — console [CB] |
| Brand / Defensive | Brand word in keyword | Defensive | Hero ("keep on White" in B6) | CM2 × CVR; above-ceiling allowance only with verified competitor presence | Share + cost; ACoS ≤ BE | Funded first when ≥ 3 rivals advertise on brand terms [PB, B6 R-N3, R-CI6] |
| Liquidation / clearance | Declared (§1.1) | Targeting objective + Liquidation flag | Aged/clearance SKU | BE on forward-cash economics (file 04) | Units cleared | Never cut on ACoS [B6 R-N2, SR] |
| SB / SBV / SD | Ad type | Own | — | Same break-even rules | Own metrics | Outside the SP engine: built and priced by hand, own budget line, counted in the spend limit; one SB format per push term [B6 E12, R-CI10, F17] |
| Shared multi-product | Advertises other products | — | — | — | In its own product's audit | No colour or price automation from this product; spend = row × (product tile ÷ rows) [B6 E13, F29] |

---

## 3. Master decision order applied to campaigns

The first gate that fires ends the row; record which gate fired. Exception: a price above its ceiling is always corrected in the same run, whatever gate ends the row. [SKILL, PB, B6 R-P5]

| Step | Exact tests | If it fires | Label | Source |
|---|---|---|---|---|
| 1 Data validity | CVR/ACoS computed with 0 orders; CTR with 0 impressions/clicks; values conflict across bulk / console / Sellerboard / SQP; margin table > 45 days old or any price/fee/packaging change not re-derived (re-derive within 48 h); no economics for the advertised SKU (halt — never a default break-even); campaign has no current state or isn't in the scope list; SKU provenance mismatch over the window (another SKU advertised) | No recommendation; refresh task; over-ceiling price still corrected (provenance mismatch: correct price now, clean read forward; mixed window: use the post-change part if ≥ 15 clicks) | REVIEW | [PB, SR, B6 F13, E7] |
| 2 Goal & event | Goal declared? (undeclared → Profit-First for the ranking gate). Profit-First → no new push, protect won rank only. Clearance → no rank considerations at all. Event day (deal) or window with > 2 deal days, 2-week post-event guard, last 7 days unsettled | Deal/event: no ACoS/CVR verdict on deal data, no launches/folds/structure, deal-state margin and CVR computed separately, bleed stops and over-ceiling cuts still run. Deals amplify a decided push, never originate one | MONITOR (no verdict) or the push plan's label | [PB, B6 E1/E2, #27] |
| 3 Economics | Margin/unit of the advertised SKU at the price in force; BE CPC = margin × placement CVR (own ≥ 50 clicks, blend 15–50, size rate < 15); ceiling = 2 × BE CPC at TOS for ranking, 1.0 × BE CPC at every placement for non-ranking; BE ACoS outside 5–70% → flag | Price > ceiling → to ceiling now, never deferred | PUSH (at ceiling) / BREAK-EVEN / CUT | [B6 R-P3/R-P5, SR, #3] |
| 4 Inventory | Zone of the advertised variation: Green ≥ 60 d cover (30-day pace), Yellow 21–59, Red < 21 or stock-out before the next dated inbound. Hero available < 7 days; available = 0; cover short of arrival by ≤ 7 d (TIGHT) or > 7 d | Red → protect: taper, re-point ranking ads to the same-size backup same day (by hand). Available 0 → pause the push. Hero < 7 d → no push, break-even only. Yellow → no new push, no raises, keep spend, dated re-entry. TIGHT → existing push eases before the stock-out day, no swap | BREAK-EVEN / REVIEW (switch) / WAIT | [PB, B6 R-I1–I6, R-C6, #9, #10] |
| 5 Structure | Keyword, ad group and campaign enabled; product ad on the right variation (ranking = size's best seller; discovery = clearance colour; colour term = named colour; size never changes); indexed (not indexed → no spend, indexing task; ranking term only in backend → listing task); objective matches targeting; one live exact owner; shared campaign; SB/SD | Paused → no price change, restart decision. Duplicate → losers withheld. Wrong objective → retag. Wrong variation → switch (by hand, same size). Shared/SB/SD → out of automation | RESTART / REVIEW / DEDUPLICATE / CHECK OWNER | [PB, DR, B6 R-S1/R-S2, R-C1–C5, E6, E13] |
| 6 Sample | Bid read ≥ 15 clicks (30 d); CVR verdict ≥ 100 clicks (own TOS CVR usable from 50); CTR verdict ≥ 1,000 impressions; PT ≥ 11 clicks. **Any row with orders skips to the objective loop** | Below floor, 0 orders → no change; formula-only correction if over ceiling (< 15 clicks and 20–25% over → to ceiling in one cycle, then suppression check next cycle) | MONITOR | [PB, SR, B6 R-B4/E3, #11] |
| 7 Delivery | In-budget < 70% of the day → rates truncated (0% with $0 spend = missing data, not truncation). Ranking: PDP > 20% of clicks on ≥ 15 clicks; clicks ≥ plan but TOS < 30% of clicks. Boost at 900% and price not reachable. CPC well above ceiling AND low clicks (suppression) | Budget first; then MIX FIX before any price move; cap → base per R-M2; suppression → fixed-bid trial (owner-approved, file 07) | MIX FIX / REVIEW | [PB §4A, B6 R-M1/R-M2, WB, #7] |
| 8 Quality | Four-quadrant per syntax: CTR & CVR vs market × 1.10, fail < 0.9 × target. SQP: our CTR or CVR < market on ≥ 30 clicks. Rank lost > 10 places in 30 days while getting clicks. Rival move (price cut > 15%, new discount, traffic > +50%). CVR drop with a logged price rise. Branded CVR collapse | Conversion quadrant → fix offer, no push (≥ 4 weeks = chronic: bids frozen at maintenance). Both failing → reduce, fix listing first. Listing flag → WAIT. Rank drop → freeze price, find cause. Rival move → hold price 3 days. Price rise → hold, revert or recompute BE | WAIT / REVIEW | [#20, B6 E4/E15, R-CI11, PB §10] |
| 9 Objective loop | Ranking: push qualification (§5) then progress test (§6). Non-ranking: §7 | per loop | PUSH / HOLD RANK / BREAK-EVEN / CUT / KEEP / SCALE / DEFEND | §5–7 |
| 10 Size & bound | Push ≤ +30%/day while not holding top; other raises ≤ +25%/cycle; gradual cuts ≤ 15%/cycle; non-ranking CUT ≤ 30% of base; BREAK-EVEN ≤ 50% per step; decisive cuts (bleed, 0-order waste) ≤ 50%; base ≤ 50% per step; boost ≤ 900%; base ≥ price ÷ 10; $0.50 bid floor (provisional; a lower ceiling wins); budget = plan clicks × TOS price × 1.05 (+ product-page spend); min budget $10; spend limit | Cap the step; gap > cap → two dated steps. Over limit → scale push budgets, cut from the bottom of the funded list | (same label, sized) | [#5, B6 R-P4, E17, E19, SR, PB] |
| 11 Landscape | Competitor influence rules (file 08): agrees / stretch / reachable / challenge / engine-blind | Changes order, read window or wording — **never a price** | (same label) | [B6 R-CI4] |
| 12 Log | Trail: input → metric → rule → decision → action → expected outcome → validation date | — | — | [SKILL] |

**Human-confirm before shipping:** structural change (campaign, routing, match type, strategy, pause); bid move > 25%; budget move > $50/day; SV ≥ 500 terms; any gate failure. State the trade-off in reviewer units ("holds ~$180/wk of saving to keep ~66 orders/wk"). [PB §13A, #32]

---

## 4. The campaign decision set (labels) and pause rules

One label per campaign per cycle. The keyword-level labels (HARVEST, REDUCE, BLOCK, DEDUPLICATE, CHECK OWNER) are applied to terms inside the campaign and reconciled at campaign level (§8.5).

| Label | Applies to | Enter when | Action and bounds | Source |
|---|---|---|---|---|
| **PUSH** | Ranking, funded | Passes all push gates (§5), goal Growth/Mixed, stock Green | TOS price toward push price = BE × (1 + premium), ≤ +30%/day while not holding top, never above 2 × BE; budget = plan clicks × price; mix 70–90% TOS | [B6 R-P1–P4] |
| **WAIT** | Ranking, would-be push | A fixable gate fails: listing flag, ceiling < our TOS CPC, rank > ~30 places from target, stock Yellow/TIGHT, missing property of the 5-property gate, event day for a new start | No raise; price ≤ ceiling; blocker named with owner and re-test date; if the owner declines the fix, the row becomes BREAK-EVEN | [B6 R-P1, F25, F26] |
| **HOLD RANK** | Ranking at/inside target | Organic rank ≤ target | Keep price, no raise; after 2 clean weeks taper −10%/week to a floor 5–10¢ below the delivering placement's blended CPC; restore on slip | [B6 R-P8, PB, #26] |
| **BREAK-EVEN** | Non-push ranking | Price > BE CPC | 0 TOS clicks in 30 d → straight to BE. TOS clicks > 0 → step down ≤ 50% toward BE; restore one step if rank falls > 10 places. Price ≤ BE → KEEP | [B6 R-B1–B3] |
| **CUT** | Non-ranking (PC, Discovery, Defensive) | ACoS > BE on both 30 & 90 d, ≥ 15 clicks | Base × (BE ACoS ÷ ACoS), i.e. −(1 − BE/ACoS), max −30% per step | [B6 R-N1, #16] |
| **MIX FIX** | Ranking | PDP > 20% of clicks on ≥ 15 clicks, or TOS < 30% of clicks at/above plan | Base −50% (−25% if product pages bring orders); boost raised in the same write so the TOS price holds; boost ≤ 900%, base ≥ price ÷ 10; re-check day 7 | [B6 R-M1, PB, WB] |
| **DEFEND** | Brand keywords, own-ASIN PT | Defensive objective | Keep on hero with enough budget (utilisation 100% before bids); ladder / restore per the six defensive states (§7.4); ACoS ≤ BE | [B6 R-N3, R-X1, PB] |
| **RESTART** | Paused campaign/keyword that owns a needed term | Term needed (ranking, harvest, defence) and a paused owner exists (close variants count) | Re-enable instead of building; non-push restarts at BE; state change only — no bid written in the same row; never on an event day | [B6 R-S2, F16, DR] |
| **KEEP** | Any | Inside its rule band: non-ranking BE ≥ ACoS > 50% BE; non-push ranking at ≤ BE; 30-d inside but 90-d over | No change; re-read next cycle | [B6 R-B3, R-N1] |
| **REVIEW** | Any | Owner decision needed: quarantined data; 3 days at ceiling without holding top; stop proposed (> 2 × BE); shared campaign; SB/SD; unmapped competitor; State E with no cause; variation switch; structural change; plan > capacity | Named question, evidence, options with trade-off; only downgrading interim actions (ceiling correction, one CUT step) | [B6 R-P6, E5, E7, E13, E20, PB] |
| **SCALE** | Non-ranking; competitor PT | ACoS ≤ 50% BE with orders (≥ 15 clicks); competitor PT ACoS ≤ BE on ≥ 15 clicks | Raise ≤ +25% per cycle, never above BE CPC; Green/Yellow stock only, not in a Conversion/Both-failing quadrant | [#16, #5, B6 R-X3] |
| **MONITOR** | Any | Below sample floor with 0 orders; event/deal data; 30-d over BE but 90-d inside | No change; named re-read date | [B6 R-B4, R-N1 WATCH, E1, E3] |

### 4.1 Pause and stop rules (all state changes are human-confirmed and never loaded on event days, except stock-out)
1. **Duplicate losers** → paused (withheld), nothing else changed. [PB, #13]
2. **Available = 0 on the hero** → pause the push; ranking ads to the same-size backup. Allowed on event days. [B6 R-I5]
3. **Non-ranking campaign ACoS > 2 × BE on ≥ 30 clicks (90 d)** → stop proposed (REVIEW); interim: one CUT step. [#16, B6 R-K3]
4. **Competitor PT ≥ 20 clicks 0 orders, or ACoS > 2 × BE on ≥ 30 clicks** → pause the target / negative ASIN. [B6 R-X5]
5. **Conquest exit** (§7.5) → pause the target, or rotate to a better-qualified ASIN. [PB]
6. **Push stop-loss** (4 consecutive flat reads, State B) → concede/defer; budget reallocated to the next winnable term; campaign returns to BREAK-EVEN. [PB]
7. **Push stop on conversion** (TOS CVR below market on ≥ 50 clicks) → back to BREAK-EVEN (price, not state). [B6 R-P7]
8. **Mixed Exact + Broad block** → pause the broad, keep the exact (post-event). [OC]
9. **Live keyword off the listing** (product type the listing doesn't sell) → pause. [WB]
10. **Zero-order terms** are not paused as a campaign action: irrelevant → negate (≥ 5 clicks); relevant ≥ 20 clicks 0 orders → reduce + fix queue; never negate an exact ranking term or a brand term. [#12]
11. **Never pause a converting row for thin clicks.** [PB, DR]

---

## 5. Push qualification

### 5.1 Product-level preconditions (before any term is considered)
- Goal authorises ranking spend: Growth/Scale or Mixed. Profit-First: no new push (won rank may be protected without the allowance). Clearance: none. Undeclared → Profit-First. [PB]
- Spend limit and margin rule stated for the window (no push can be sized without them); a baseline that excludes deal and settling days. [B6 F03, R-F5]
- Code-red TACoS state freezes all scale (only if the owner set a TACoS target — otherwise TACoS is monitored only). [PB, #17]
- Concentration: one term > ~25% of product clicks, or top 5 > ~60%, needs a declared head-term push, else a named finding. [PB]
- Candidate wording: core product wording only; generic category terms outside the core never enter the push, whatever their volume. *Example (B6): "bed sheets" (155k traffic) stays MONITOR; "bamboo sheets" qualifies; B6 also required ≥ 7 of 13 tracked rivals ranking on the term.* [B6 R-CI1]

### 5.2 Candidacy
| Type | Definition | Consequence |
|---|---|---|
| **Cold** | New push | Full realism gauntlet (5.4) |
| **Recovery** | Best rank in last 12 months was top 10, with a logged, resolvable cause | Inherits its prior ceiling; funded before an equal Cold term; recovery push rules (§6.7) |
| **Structure-blocked** | No live exact owner | Fix first: same-day exact build + steering negatives in broad/auto (first post-event day if in an event) — not a harvest case |
[PB, WB]

### 5.3 The six push gates (all must pass; else WAIT with the failing gate named)
| # | Gate | Test | Source |
|---|---|---|---|
| 1 | Demand / plan | Term has a plan: target rank, DSTR, required units/clicks; core wording | [B6 R-P1, R-CI1] |
| 2 | Converts at the top | Own TOS CVR ≥ market CVR (SQP). CVR basis: own ≥ 50 TOS clicks; blend 15–50; overall/size rate below 15. SQP listing flag (our CTR or CVR < market on ≥ 30 clicks) fails the gate | [B6 R-P1, E15, F26] |
| 3 | Reach | Current organic rank within ~30 places of target | [B6 R-P1] |
| 4 | Stock | Advertised hero Green (≥ 60 d at 30-day pace), no stock-out before the next dated inbound, cover ≥ days to next arrival + 7, available ≥ 7 days; projected cover at push velocity stays out of Yellow/Red through the checkpoint. Cover never on the push pace | [#9, B6 R-I1/R-I2, F30, PB] |
| 5 | Keyword live | Keyword, ad group, campaign enabled; right variation's product ad enabled; indexed; one live owner | [B6 R-P1, PB] |
| 6 | Ceiling covers cost | Ceiling (2 × BE CPC) ≥ our current TOS CPC (TOS spend ÷ TOS clicks) | [B6 R-P1, F25] |

### 5.4 Realism gauntlet (Cold candidates; any fail → no push, name it)
SV > 500 · indexed and present in the listing · purchase intent · CVR ≥ benchmark · reviews ≥ ~50% of the top-5 median · rating no more than ~0.3★ below · price ≤ ~1.25 × category median · Green stock · thin margin → CPC ≤ ~⅓ of margin. Re-entering a ranking posture after stepping back needs a fresh gauntlet. [PB]

### 5.5 Five-property gate (missing one → no push; the missing property named; price held ≤ ceiling)
| Property | Must contain |
|---|---|
| **Sized** | Target rank; DSTR = daily sales at target rank (market data, floor 1/day); paid sales = DSTR − our organic sales on the term (labelled proxy); required TOS clicks = paid ÷ own achieved TOS CVR; budget = clicks × TOS price × 1.05; same data version; projected cover [#19] |
| **Dated** | Horizon and first checkpoint (7-day read) |
| **Ceilinged** | Price ceiling 2 × BE CPC; weekly loss ceiling = (push ACoS − BE ACoS) × projected sales at required spend — hitting it is a human flag, not an auto-stop |
| **Predicted** | Metric, direction, magnitude, horizon — written before money moves |
| **Funded** | Dated release inside the spend limit |
Plan clicks set volume and budget only, never price; reconcile the sum of term requirements to what the product sells. [PB, B6 F21]

### 5.6 Rank-credit and TOS-share checks
- **Rank credit:** auto + broad carry > ~40% of the term's clicks, or no live exact → OUT OF SCOPE for a ranking verdict; structural fix (isolation negatives / exact build). [PB]
- **TOS share:** clicks ≥ plan but TOS < 30% of clicks → MIX FIX first. [PB, WB]

### 5.7 Push pricing
| Item | Rule | Source |
|---|---|---|
| Break-even (TOS) | margin/unit of the advertised SKU × TOS CVR | [B6 R-F2] |
| Premium | rank ÷ target ≤ 1 → none (HOLD RANK); ≤ 1.5 → +25%; > 1.5 → (rank ÷ target − 1) × 50% | [B6 R-P2, #4] |
| Push price | BE × (1 + premium), capped at the ceiling (a premium > 100% always caps) | [B6 R-P2/R-P3] |
| Ceiling | 2 × BE CPC (owner may raise one named term's ceiling for a set time) | [B6 R-P3, #3] |
| Step | ≤ +30%/day while below push price or not holding top; never above ceiling | [B6 R-P4] |
| Over ceiling | Cut to ceiling now | [B6 R-P5] |
| At ceiling 3 days | Without top-3 sponsored and ≥ 30% TOS impression share → REVIEW: raise the ceiling for a set time, or swap the term | [B6 R-P6] |
| Conversion stop | TOS CVR below market on 50+ clicks → stop the push, back to BREAK-EVEN | [B6 R-P7] |
| At 900% boost | Target price > base × 10 → raise base only to price ÷ (1 + boost) with the boost set in the same write; never credit a capped step with new clicks | [B6 R-M2] |
| Bidding strategy | Unchanged; new push campaigns dynamic down-only; fixed only via the fixed-bid trial | [#8] |

*Example: rank 16, target 8 → ratio 2 → premium 50% → push price 1.5 × BE. Rank 12, target 8 → 1.5 → +25%. Rank 30, target 8 → 3.75 → 138% → capped at 2 × BE.*
*Example (B6): "bamboo sheets" at its $6.10 ceiling: hold $6.10, base $1.60 → $1.20, boost → 408% (1.20 × 5.08 = $6.10), ceiling question to the owner. Boost at the cap: base $0.50 × 10 = $5.00 max; correct write base $0.60 + boost 700% = $4.80, not base $1.40.*

### 5.8 Funding order and spend limit
1. Fund in order of revenue potential at target rank ÷ cost to close the gap, after gates. [PB]
2. When plan budget exceeds room: winnable-ground terms (beatable rivals between us and target) first, stretch terms second. [B6 R-CI3]
3. Push budgets + expected other spend ≤ the stated limit; over → scale push budgets, cut from the bottom of the funded list. [B6 R-F5, E19]
4. Weekly: margin after ads below the owner's rule → cut the push from the bottom of the funded list. [B6 R-F6]
5. Price and budget rows load together or not at all; withheld rows never reach the export. [B6 F14, F15]

---

## 6. Ranking progress test

### 6.1 Rank-trend read rules
- ≥ 1 month of rank history (ideally 3); < 1 month → OUT OF SCOPE for a ranking verdict. [PB]
- Organic rank = median over the window; unranked days count; not ranked if half the days are unranked. Use the daily crawl rank; state which rank table governs when two disagree. [B6]
- Exclude stock-out and re-route stretches (too short a remainder → OUT OF SCOPE). Target from the target-rank file/bulk only. [PB]
- State **overall, 14-day and 7-day** trend separately; shorter windows are early warnings. Keep a separate deal-state arc; **the clean arc governs**. [PB]
- Push read window 7 days. On push terms with ≥ 5 rivals at sponsored #1–5, judge rank after 7 days (not 3); TOS impression share alone is not pass/fail. The daily step and ceiling still apply. [B6, R-CI5]
- Estimates (target sales/clicks/budget) size direction; **rank movement governs** — say so on every row. [PB, DR]

### 6.2 States
| State | Condition | Action | Label |
|---|---|---|---|
| **A** | Clicks > plan, rank improving | **Hold price.** Budget rises only if the plan's clicks are budget-truncated and the spend limit allows; keep TOS ≥ 30% of clicks [#6] | PUSH (hold) |
| **B** | Clicks > plan, rank flat | Estimate was low: step price up (≤ +30%/day, ≤ ceiling), rebase targets from actuals, size by rank gap. **4 consecutive flat reads → STOP-LOSS** | PUSH → BREAK-EVEN on stop-loss |
| **C** | Clicks < plan, rank flat | Delivery problem: budget truncation → placement mix / TOS modifier → price step (lever order §8.1) | MIX FIX / PUSH |
| **D** | Clicks < plan, rank improving | Estimate was high, winning cheaply: hold | PUSH (hold) |
| **E** | Rank lost > 10 places despite delivery | Investigate (6.3); freeze price moves; **never scale** | REVIEW |
| **F** | Delivery ≈ 95–120% of plan | Too early; re-read. 4 cycles → re-diagnose (#25) | PUSH (hold) |
| OUT OF SCOPE | No sized plan, no tracked movement, rank credit fails, < 1 month history | Efficiency decision inside a Ranking campaign (break-even rules) | BREAK-EVEN / KEEP |
[PB, DR, WB, #6, #25]

### 6.3 State E investigation order (never a bid change)
1. Anchor the timing of the drop.
2. Own listing first: price, stock-out, reviews, content, coupon/deal ending, colour/variation switch, keyword state → listing finding.
3. Competitor wins ≥ 2 of price / rating / reviews, or competitor went out of stock → name it; route to conquest/PT.
4. Isolated term vs category-wide → category-wide escalates.
5. Nothing found → "investigated, no cause identified" → ask the owner.
[PB, B6 E4]

### 6.4 Competitive shock
- A rival in the term's top 10 makes a brief move (price cut > 15%, new discount, traffic growth > 50%) → hold our price 3 days; don't read the conversion drop as a bid problem. Over-ceiling cuts still apply. [B6 R-CI11]
- CVR ≥ benchmark, rank falling, no own event (and after the 3-day hold if a move was found) → check new entrant/deal/price cut → **one step within ceiling**, re-read in 1 week, log. [PB]
- Stretch target (only aspirational rivals at or above target): progress judged on rivals passed (first milestone); 14 days at ceiling with no rival passed → owner. [B6 R-CI2]

### 6.5 Stop-loss and escalation
- 4 consecutive flat grades on a push (State B) → STOP-LOSS: concede or defer, reallocate the budget to the next winnable term. [PB]
- 2 consecutive flat/backfired grades on any lever → escalate the lever (never repeat it a third time); same verdict 4 cycles with no effect → re-diagnose the row. [SR, PB, #25]
- Grading tolerance: ±3 ranks (ranking), ±3 ACoS points (others). [SR]

### 6.6 Sufficiency stop and incrementality ladder
1. Rank ≤ target → HOLD RANK: keep price, no raise, for the first **2 clean weeks**. [B6 R-P8, #26]
2. Then taper **−10%/week** to a floor **5–10¢ below the delivering placement's blended CPC**; record the floor. [PB]
3. **Restore** the last step (= the recorded floor) on slippage **> 2 places on a top-5 term**, or **any slip below target** outside the top 5; if the term slips past target, it rejoins the push. Re-test the floor quarterly or after a shock. [PB, B6 R-P8]
4. **Incrementality ladder** (organic rank ≤ 3, clean logs): spend −15%, hold 2 weeks; total orders hold → keep stepping; total orders fall > 10% → restore and record the floor. [PB]
5. After the stop, the campaign is judged at the standard (break-even) ceiling. [PB]

### 6.7 Recovery push
Entry: SKU back to Green, prior rank top 5–10 within 12 months, CVR ≥ benchmark, the loss logged to an inventory cause. Target = pre-decline baseline. Week 1 re-point + maintenance, week 2 push, checkpoint at 3 weeks. [PB, WB]

### 6.8 SBV arbitrage
Enter SBV on a push term when SBV CPC ≤ 0.6 × the SP exact CPC **and** SBV CPA clears its own ceiling. Exit when SBV CPC rises past 0.8 × SP exact CPC, or completion rate fades 2 consecutive weeks. Judge on SBV metrics only. Reactive path still needs the 100-click exact candidacy. One SB format per push term; built by hand, own budget line, counted in the spend limit; no launch on event days. [PB, B6 F17, R-CI10]

---

## 7. Non-ranking campaigns

### 7.1 Layered rule (Profitable Conversion, Discovery after its grace period, Defensive ACoS check) [#16, B6 R-N1]
Read campaign ACoS vs the advertised SKU's BE ACoS on **30-day and 90-day** windows; ≥ 15 clicks (30 d); windows with > 2 deal days not used.

| Condition | Decision | Action |
|---|---|---|
| < 15 clicks, 0 orders | MONITOR | none |
| ACoS > BE on 30 d **and** 90 d | CUT | base × (BE ÷ ACoS), max −30% per step |
| 30 d over, 90 d inside | MONITOR (watch) | none; re-read next cycle |
| 30 d inside, 90 d over | KEEP | recent window recovering |
| ACoS > 2 × BE on ≥ 30 clicks (90 d) | REVIEW — stop proposed | interim one CUT step; keyword increases neutralised (§8.5) |
| 50% BE < ACoS ≤ BE | KEEP | none |
| ACoS ≤ 50% BE with orders | SCALE | ≤ +25% per cycle, never above BE CPC at any placement |

- Sizing inside the SCALE cap (provisional — confirm with the owner before first use): CONFIRMED 15+ clicks / 2+ orders / CPA ≤ ~70% of ceiling → hold; STRONG 30+ / 3+ / ≤ ~60% → ≤ +10%; PROVEN 50+ / 5+ / ≤ ~50% → ≤ +15%. [PB, WB]
- Target ACoS 50% BE and max 75% BE are reported bands, not triggers — break-even triggers. [SR, B6 F31]
- A reduction on a term that still sells (≥ 10 orders in 90 days) and that rivals buy is a cut to break-even, never a block. *Example (B6): "king size bamboo sheets set" — 61 orders, 29.8% ACoS vs 23.8% BE, 11 rivals advertising → reduce to break-even.* [B6 R-CI9]
- Before a cut batch ships: does projected lost-order value exceed spend saved, at the more conservative margin? Withdraw failures. Check auction density before calling a cut safe. [PB]
- Price attribution: CVR drop coinciding with a logged price rise → hold; revert, or recompute BE from the new price. Profitable only at rest-of-search with no rank case → near-0 TOS modifier, stated. [PB]

### 7.2 Liquidation / clearance exemption [B6 R-N2, SR]
- Not cut on ACoS; judged on units cleared vs the clearance timeline (file 04 ladder).
- Price ceiling = BE on forward-cash economics (file 04); relevance-based blocks (irrelevant zero-order terms) still apply; spend limit still applies.
- Green → run up to BE; not Green → no push; never a clearance push while the hero of that size is Red; negative contribution → a pricing decision for the brand manager, not bids; exit when stock falls below the surcharge threshold.
- Lever reads at day 7 and 14; < 50% of the predicted uplift → replace the lever, don't extend it. Before calling a SKU "tested and failed", confirm it ever had dedicated spend. [LTSF]
- Peak-week availability outranks LTSF economics when a calendar marks the week as peak. [PB]

### 7.3 Discovery
- **Grace:** first 30 days judged only on converting terms per $100 and graduations; no campaign CUT. Term-level verdicts from 15 clicks. [DR, PB]
- **Metrics:** converting terms per $100 = terms with ≥ 1 order ÷ (spend ÷ 100); graduations = terms moved to their own exact (≥ 3 orders at ACoS ≤ BE, no live exact owner — HARVEST; negate at source in the same deployment); wasted spend ≤ 40% (above → negation pass). [DR, #22, #24]
- **Building a discovery layer:** reactive = ≥ 100 qualified clicks on the term's own exact history (near-miss ≈ 20); proactive = coverage gap (e.g. primary root at 0% phrase). < 100 → ineligible, no pricing. Check for an existing instance first. [PB, #23]
- **Variation:** size's clearance colour (≥ 180 d cover, or ≥ 90 d while selling ≤ size median); hero stock reserved for ranking. [B6 R-C2]
- After grace, the campaign runs the layered rule (§7.1). [B6 R-N1]

### 7.4 Defensive (provisional — confirm before first use) [PB, B6]
- Pricing: CM2 × CVR on the advertised SKU; above-ceiling allowance only with a competitor or non-brand seller actually seen on the branded term (STR or placement capture), bounded by the ranking ceiling (2 × BE CPC); withdrawn after 2 consecutive reads without presence.
- Share = impression share per branded query vs that query's own prior baseline (blended branded only as a named fallback).
- Keep on the hero, funded; judged ACoS ≤ BE. Brand terms with ≥ 3 rivals advertising → DEFEND at TOS, funded first, add own-ASIN PT. [B6 R-N3, R-CI6]

| State | Condition | Action |
|---|---|---|
| 1 Correct | Share held, ACoS within 10–15% of ceiling | Ladder −~10%/week to the floor that still holds share; record it; never scale past it |
| 2 Slipping | Share slipping, or a competitor ad on our detail page | Restore one ladder step + open/expand own-ASIN PT; the syntax's defence budget caps the response |
| 3 Under-spent | Utilisation < 100% | Budget to 100% utilisation before bids (Ranking 80%+, Discovery 70%+) |
| 4 Conquested | Competitor ad above our organic slot on our brand term | Restore step + SB headline on brand root (SBV if none) + own-ASIN PT on attacked ASINs; weekly review |
| 5 Inflating | Branded ACoS up while share holds | Find the cause; if a rival bids our brand up, cap at the defence budget; never chase past ceiling |
| 6 CVR collapse | Branded CVR falls | Listing first (suppression, buy box, reviews, variation break) |

### 7.5 Conquest (provisional) and competitor PT [PB, B6 R-X3–X6, R-CI7]
- Existing instance first (same ASIN elsewhere → decide from its state; one owner per ASIN).
- **Entry:** routed SKU wins ≥ 2 of 3 (price, rating, review count) vs the target, or the target is out of stock. Missing data → ask before logging a wait. B6 form: OFFENSIVE = above us on price for fewer pieces, or same price with < 50% of our reviews; AVOID ASINs negated in auto/PT.
- **Ceiling = watch-CPA** = lower of routed-SKU CM2 × CVR and the price-gap-adjusted figure; state which governs. Product-page lever, no TOS modifier.
- **Verdicts:** PT floor 11 clicks. SCALE (ACoS ≤ BE, ≥ 15 clicks) ≤ +25%/cycle up to BE CPC; REDUCE when ACoS > BE on ≥ 15 clicks; BLOCK at ≥ 20 clicks 0 orders or > 2 × BE on ≥ 30 clicks; unmapped ASIN → no SCALE.
- **Exit / rotate:** target delisted; target no longer wins 2-of-3 (hold); CPA > watch-CPA 2 consecutive reads with no page-share gain. Rotate when another ASIN clears the gate and is better (budget and structure carry over).
- CPC > 1.5 × family median on the same term → flag (family-wide = market; our row only = our bid).

### 7.6 Market Share (declared only) [PB]
| State | Condition | Action |
|---|---|---|
| Headroom | Primary root IS < ~12%, profitable in band | Expand exact + phrase coverage, step budget, track IS migration |
| Dominance too expensive | IS ≥ ~41%, ACoS over band | Hold share, ladder down to the minimum CPC that preserves it; marginal ACoS check |
| Cap enforced | Secondary syntax over its spend-share cap (~25%) | Cut to cap, excess to primary |
| Coverage worklist | Relevant size/colour/attribute cell with no funded campaign | Fund or decline and log; track SV coverage % |
| Step and verify | IS stuck at band floor ≥ 2 cycles, ACoS in band | One budget step; IS must move in 2 weeks, else TOS modifier / CPC |
| Structure gap | Primary root at 0% phrase | Stand up phrase at modest budget |
| Falling demand | Seasonal SV declining | Hold/contract; re-time expansion |
| Variation flow | Share on one stock-vulnerable child | Rebalance across children |
Marginal ACoS = Δspend ÷ Δad sales; > 2 × blended → unwind the step. [PB]

---

## 8. Levers, holds and reconciliation

### 8.1 Lever hierarchy (resolved, #7)
1. **Evidence first:** budget truncation (in-budget < 70% of the day) → budget before anything; truncated rates are not evidence.
2. **Placement mix / TOS modifier** — the rank lever (MIX FIX pair when PDP > 20%).
3. **Price step** (within caps).
4. **Base bid last** for ranking (if the campaign only wins product pages, the base goes below the PDP clearing price while the modifier carries the TOS price).
5. **Bidding strategy unchanged** unless the fixed-bid trial fires (owner approval).
- Non-ranking: the base bid is the lever. ROS lifted to ceiling only after 15+ ROS clicks converting ≥ the campaign's PDP rate. [DR, PB, WB]
- Never let TOS fall as the residue of a base cut; never lower a ranking campaign's effective TOS unless it is above the ceiling. [WB, PF]

### 8.2 One lever per row per cycle
- One lever per entity instance per cycle; different rows of a campaign may each move. [DR, PB]
- **Exemption:** one keyword's base bid + its placement modifiers form one backward-solve (TOS/ROS targets set first, then base, then both modifiers re-solved) — counts as one lever. MIX FIX is such a pair. [PB, B6 R-M1]
- Budget may ship with a price change only when both come from the same forward math (push plan). A campaign where only one lever type was ever written though budget, TOS and bid each warranted evaluation → re-examine. [PB]
- Two levers in the same window confound the read — say so in the grade. [LTSF]

### 8.3 Silent-hold list (exhaustive)
A hold at the objective-loop stage is allowed without asking only for: (1) both quality gates fail; (2) CTR passes, CVR fails (brand-management finding); (3) zero delivery; (4) budget truncation; (5) plan exceeds the campaign's capacity (escalate). Any other hold → ask the owner first and log the question and answer. Gate outcomes (quarantine, sample floor, stock, paused, duplicate, event day) are recorded with their gate, not as holds. [PB, DR]

### 8.4 No bid change when
- Row paused, withheld duplicate, or SKU below the stock gate; budget truncated; zero delivery; both quality gates fail; CTR passes and CVR fails. [DR, B6 E6]
- State E (rank collapse) — never a raise. [PB check 9]
- A rival's brief move in the last 3 days (except over-ceiling cuts). [B6 R-CI11]
- Rank dropped > 10 places in 30 days while getting clicks, until the cause is found. [B6 E4]
- Shared multi-product campaign, SB/SBV/SD (hand decisions only). [B6 E12, E13]
- Deal-day data would be the evidence. [B6 E1]
- Price came from Amazon's suggested bid or a competitor's CPC (never used). [#18, B6 R-CI4]
- Price attribution unresolved (CVR drop with a logged price rise). [PB]

### 8.5 Reconciliation at campaign level [SR, DR, B6]
1. Campaign referred for stop/turn-off or owner review (not a high-budget review) → every keyword **increase** inside it is neutralised to hold.
2. Budget raise dropped when ≥ 60% of the campaign's keyword rows are cuts/negations and none are increases.
3. Reconciliation only downgrades; it never invents an action; annotate the reason.
4. **One direction per term across campaigns** — a term cut in one campaign and raised in another fails; resolve to the single owner.
5. Price and budget rows load together; withheld rows never exported; every written value must match its label (a "taper" that raises price fails).

---

## 9. Structure rules

| # | Rule | Detail | Source |
|---|---|---|---|
| S1 | **One campaign per search term** | One live exact owner per term (close variants count: plural, symbols; word order is a different term). Negative exact for owned terms in the discovery campaigns that serve them (isolation wall), in the same upload as the owner goes live | [B6 R-S1, WB, #14] |
| S2 | **Duplicate owners** | First test coexistence: stage-stack (earlier-stage campaign deliberately left running), placement-split, variation-split (different size/colour child), sibling ownership (another product in the family owns its instance). Else owner = higher CVR at lower CPC with ≥ 15 clicks each; below that, most orders; tie → longer clean history. Losers withheld, nothing else changed. Check duplicates again after any re-enable | [#13, PB, PF] |
| S3 | **Paused owners** | Term exists (live or paused, close variants) → restart/reuse, never build a duplicate; a price change can't make a paused keyword serve; keeper inside a paused campaign won't serve (campaign-level edit needed) — count and state | [B6 R-S2, F16, E11, LP] |
| S4 | **Colour / variation** | Ranking = size's best seller; discovery = size's clearance colour; colour-named terms = that colour; size never changes (except correcting a wrong size); a colour with < 7 days of cover never added; switch to backup only when hero cover < days to arrival by > 7 d; switches by hand; routing read from Product Ad rows, never names. Every re-route rebuilds break-even from the new SKU and resets the CVR baseline and rank clock | [B6 R-C1–C6, E8, E9, #29, PB] |
| S5 | **Objective retags** | From targeting and term class only (§1); a Ranking tag on colour/competitor/language/misspelling is blocked; retag carries a verdict line | [B6 R-O1, F12, E18] |
| S6 | **No structural change mid-event** | Folds, splits, new structures, restarts of non-push campaigns → decided in the post-event audit | [B6 R-S3, E1, F19] |
| S7 | **Brand negatives last** | Negatives on brand terms in a brand broad only after the receiving brand exacts are Defensive, on the hero and funded | [B6 R-S4, E10, F18] |
| S8 | **No launches on event days** | New campaigns wait for the post-event audit (they learn on deal traffic and can't be judged); one SB format per term | [B6 F17, E1] |
| S9 | **Mixed match types** | Exact + broad in one campaign → split (pause broad, keep exact) post-event | [OC] |
| S10 | **Scope** | Only campaigns read in the current state get decisions; campaigns spending on the product but missing from the list are added and marked; shared campaigns excluded from automation | [B6 F13, F29] |
| S11 | **Build hygiene** | Exact is the default match type; dynamic down-only for new campaigns; launch price from break-even maths, never a suggested bid; routed SKU ≥ 21 days of cover to launch | [PH, #8, #18, PB] |

---

## 10. Decision table (the trail)

Every row carries input → metric → rule → decision → action → expected outcome → validation date. Outcomes are directional unless the row has its own measured step history; name any soft coefficient. Grade at ±3 ranks / ±3 ACoS points (file 10).

| Condition (metric + threshold) | Decision | Action | Expected outcome | Validation |
|---|---|---|---|---|
| Six gates pass, goal authorises, Green, rank > target | PUSH | TOS price ≤ +30% toward BE × (1 + premium), ≤ 2 × BE; budget = clicks × price × 1.05 | Rank moves toward first milestone; TOS 70–90% of clicks; sponsored top-3 most hours; TOS IS ≥ 30% | Day 7 rank read (overall / 14d / 7d); daily step check; 3 days at ceiling → owner |
| A push gate fails but is fixable (listing flag, ceiling < TOS CPC, reach > 30, Yellow, missing property) | WAIT | No raise; price ≤ ceiling; blocker + owner + date | Blocker resolved, term re-qualifies | Re-test on the named date; owner declines → BREAK-EVEN |
| Organic rank ≤ target | HOLD RANK | Keep price 2 clean weeks, then −10%/week to floor | Rank held at lower cost | Weekly; slip > 2 (top 5) or below target → restore floor |
| Non-push ranking, price > BE | BREAK-EVEN | 0 TOS clicks → to BE; else ≤ −50% toward BE | Cost per order ≤ margin; rank held within 10 places | Next cycle; rank −10 places → restore one step |
| Non-ranking, ACoS > BE on 30 & 90 d, ≥ 15 clicks | CUT | Base × BE/ACoS, ≤ −30% | ACoS toward BE next 30-day window | ≥ 15 fresh clicks; flat twice → escalate lever |
| Ranking, PDP > 20% clicks on ≥ 15, or TOS < 30% at plan | MIX FIX | Base −50% (−25% if PDP sells) + boost so TOS price holds | PDP ≤ 20%, TOS 70–90%; TOS price unchanged | Day 7 placement report |
| Brand keyword / own-ASIN PT | DEFEND | Utilisation 100%; ladder or restore per state | Share per branded query ≥ baseline; ACoS ≤ BE | Weekly share read; 2 reads with no rival → allowance off |
| Paused owner of a needed term | RESTART | Enable (state only), BE price, post-event | Term serves with its history | First read at 15 clicks on the right SKU |
| Inside its band | KEEP | None | Stable | Next cycle |
| Owner decision needed (at ceiling 3 d, > 2 × BE, shared, SB/SD, unmapped, State E unresolved, switch, structure) | REVIEW | Question + evidence + options; downgrading interim only | Decision recorded with date | Owner answer by the named date |
| Non-ranking ACoS ≤ 50% BE with orders; competitor PT ≤ BE on ≥ 15 clicks | SCALE | ≤ +25%/cycle, ≤ BE CPC | More orders at ACoS ≤ BE; marginal ACoS ≤ 2 × blended | Next cycle; marginal ACoS > 2 × blended → unwind |
| < 15 clicks & 0 orders; deal data; 30 d over / 90 d inside | MONITOR | None | Sample accrues / clean window | Named date (15 clicks or first clean week) |
| 4 flat push reads | PUSH → BREAK-EVEN (stop-loss) | Concede/defer, reallocate | Budget moves to a winnable term | Next term's day-7 read |
| TOS CVR < market on ≥ 50 clicks | BREAK-EVEN (push stopped) | Back to BE | Loss per order removed | Listing check before any re-entry |
| Hero available = 0 / Red | BREAK-EVEN + REVIEW (switch) | Pause push; ads to same-size backup | Rank protected on backup | Arrival date; re-entry plan |

---

## 11. Open questions for the owner

1. **Phrase-only campaigns:** the objective-correction script defaults phrase-only blocks to Profitable Conversion; B6 and the workbook builder put phrase in Discovery. This file uses Discovery (row 9, §1.1). Confirm.
2. **Exact term class vs "Exact = Ranking":** the conflict register adopts the objective-correction table (all exact → Ranking); B6 R-O1 sends colour/competitor/language/misspelling exacts to Profitable Conversion. This file applies R-O1 as a refinement (targeting = the term). Confirm.
3. **CUT step size:** register #16 caps a non-ranking cut at 30% of base; register #5 caps gradual cuts at 15% per cycle. This file treats #16 as the specific rule for non-ranking CUT. Confirm.
4. **Competitor PT SCALE step:** B6 R-X3 allowed +30% per step; register #5 caps non-push raises at +25%. This file uses +25%.
5. **WAIT duration:** no source sets how long a ranking term may sit in WAIT before BREAK-EVEN applies. No source rule; decide and record (this file: until the named re-test date or the owner declines).
6. **Non-push ranking term priced below BE outside an event:** no source says whether it may rise to BE without push qualification. This file keeps it (KEEP). Decide and record.
