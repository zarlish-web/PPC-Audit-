# 13 — Source map and conflict register

This framework consolidates the skills below. Where they disagree, the **resolution** column is the default this skill applies; the alternative stays available as an owner setting. If a product owner has already ruled on one of these, their ruling wins and is recorded in the analysis.

## Contents
1. Source skills and what each contributed
2. Conflict register (resolved defaults)
3. Known defects in source implementations (do not copy)
4. Gaps in the sources (what no source defines)

---

## 1. Source skills

| Source | Short | Contributed |
|---|---|---|
| pmp-optimization-sr | SR | CM2 break-even (locked), objective ACoS bands, RPC bid math, bleed stops, TOS rebuild formula, CTR root-cause tree, DSTR floor, execution verification, impact ledger + grading + escalation, SOP-47 ceiling audit, deal-window exclusion, three-file output |
| pmp-ppc-decision-engine | DE | earlier engine (superseded by SR); Data Rova/Data Dive rank, four-quadrant vs market |
| ppc-plan-builder | PB | intake halt, product-goal gate, waterfall, decision order with quarantine/indexing, sample floors 15/100/1,000, placement backward-solve, fixed-bid trial, inventory zones 60/21, seven-state ranking test, 5-property gate, sufficiency stop, discovery candidacy, harvest, negation modes, TACoS bands, 27-check gate |
| ppc-decision-reasoning | DR | lever hierarchy, reasoning chain, action-string grammar, 13-check gate, worked examples, 12 anti-patterns |
| ppc-workbook-builder | WB | per-placement bounds, planning CVR, base floor, mix targets (70–90% TOS / ≤20% PDP), routing from Product Ad rows, deployment waves, change review sheet, ~120-check harness, defect register |
| ppc-placement-first-optimization | PF | effective TOS vs clearing CPC diagnosis, lever pair, significance test, DSTR netting organic, 15-tab approval workbook with reviewer register |
| str-audit | STR | root performance, wasted-spend negation tree, harvest tiers by ACoS, spend distribution |
| metrics-data-build | MDB | keyword master columns, SV%, syntax formulas |
| keyword-campaign-performance | KCP | keyword↔campaign grouped view, req clicks/budget, duplicate/hygiene priority |
| sqp-parent-aggregation | SQP | parent roll-up (brand summed, market once), recomputed rates |
| pmp-ppc-phasing | PH | SV tiers, hero/halo, 200-kw phase cap, match-type default Exact, naming, colour-aware routing |
| ppc-objective-correction | OC | objective from targeting at campaign level, validation |
| ppc-quick-audit | QA | 17-section audit, locked thresholds (TOS IS 22.5%, WAS 10%, target ACoS 50% BE, max 75%) |
| decolure-ppc-action-plan | AP | Finding/Why/Action/Impact, INVEST vs PROTECT thesis, execution sequence, gap keywords |
| campaign-builder | CB | bulk canon, naming (compact), upload-proof rules |
| ppc-inventory-checkup | INV | velocity, cover, OOS-before-arrival, backup switch simulation |
| ltsf-recovery-dossier | LTSF | rate card per cu ft, floor/break-even discount/salvage math, archetypes, risk tiers, ladder, listing audit, lever prediction rule |
| ppc-ltsf-plan | LP | de-dup engine, relevancy scorer vs listing, AdInsight competitor method |
| B6 engagement (Sep 2026) | B6 | push logic (premium, 2× ceiling, +30%/day), mix fix, colour rules, non-ranking 30/90-day rule, keyword decision order, competitor influence rules R-CI1–12, failure register (32), exceptions (20), SB/video test design |

---

## 2. Conflict register

| # | Topic | Sources disagree | Resolution (default) | Why |
|---|---|---|---|---|
| 1 | Break-even basis | SR: CM2 = (ASP − COGS − fees)/ASP, no returns. DE framework: includes returns / (Net+Ad)/Sales. B6: Sellerboard profit per unit before ads | **Sellerboard profit/unit before ads per SKU/colour at the price in force** (owner's source of truth). When building from components use SR's CM2 and say so. Never a blended parent | One trusted source; per SKU because colours differ 2–3× in margin |
| 2 | Conversion rate for ceilings | WB: fixed planning CVR per placement; PF: measured placement CVR (≥3 clicks); B6: own ≥50 / blend 15–50 / size rate <15 | **B6 method**: own placement CVR from 50 clicks (90 d); linear blend 15–50; size (or product) placement rate below 15 | Uses real data when there is enough, avoids circular thin-sample reads |
| 3 | Ranking ceiling | PB/WB: flat ~$8–9 (CM2 may tighten); PF: overlay 1.30× BE; DR: CM2×CVR on every row | **2 × break-even CPC on the ranking term's TOS price** (owner setting). Non-ranking: ≤ 1.0 × BE CPC at every placement | Cost per order ≤ 2× profit/unit, below order value; scales with the product instead of a flat $ |
| 4 | Push premium | WB: +25% ≤1.5 gap, else +min((r−1)×0.5, 4.0); B6 same without 4.0 | **Same formula**, capped by the ceiling | Sources agree once the ceiling applies |
| 5 | Price steps | SR ±50% envelope, cuts ≤15%/cycle; PB 25%/cycle (50% if CPA > 8× ceiling); WB 50% cut / 25% raise; PF one-shot; B6 +30%/day push, −50% base per step | Push: **≤ +30%/day** while not holding top. Other raises **≤ +25%/cycle**. Gradual cuts **≤ 15%/cycle**; decisive cuts (bleed, 0-order waste) up to 50%; **over-ceiling → straight to ceiling**. Base cut ≤ 50% per step | Gradual where learning; immediate where money is being lost |
| 6 | State A (clicks > plan, rank improving) | PB/WB: budget +20–30%; DR: hold, don't scale | **Hold price**; budget only rises if the plan's clicks are budget-truncated and the spend limit allows | Rank is moving at the current price; extra money is not needed to prove it |
| 7 | Lever order (ranking) | DR: TOS modifier → strategy → budget, base last; PB: budget first | **Evidence first** (budget truncation check) → **placement mix / TOS modifier** → price step → base last. Strategy: unchanged unless the fixed-bid trial fires | Truncated budgets invalidate every rate; the TOS modifier is the rank lever |
| 8 | Bidding strategy | SR code: switch Fixed/Up&Down → Down-only; WB: Fixed at launch for ranking; B6 owner: no strategy changes | **Leave existing strategies**; new campaigns dynamic down-only; Fixed only through the fixed-bid trial with owner approval | Owner rule; strategy changes confound every read |
| 9 | Inventory zones | PB/WB: Green ≥60 / Yellow 21–59 / Red <21; SR code: Red <14, Green ≥30; INV: OOS-before-arrival | **60 / 21**, plus **stock-out before inbound arrives = Red regardless of cover**; push also needs the advertised variation's cover ≥ days to next arrival + 7 | Lead times of 60–90 days make 14/30 too late |
| 10 | Yellow action | DR: hold; PB/WB: freeze push at current spend with dated re-entry | **No new push, no raises; keep current spend; dated re-entry plan** | Protects rank without accelerating stock-out |
| 11 | Sample floors | DR: 15 clicks zero-order; PB/WB: 15 bid / 100 CVR / 1,000 CTR; PF: ≥3 + significance; SR PT 11 | **15 / 100 / 1,000; PT 11**; placement comparisons use the significance test (n < 30 → "directional") | One set of floors, with a statistical test where two rates are compared |
| 12 | Zero-order handling | SR code: $0.50 + pause & negate any row; STR: tree by relevance; PB: relevant → fix queue; B6: ≥20 clicks 0 orders → REDUCE (owned) / BLOCK (irrelevant) | **B6 + STR tree**: irrelevant → negate (≥5 clicks); relevant ≥20 clicks 0 orders → reduce + fix queue; **never negate an exact ranking term or a brand term** | SR code negating exact ranking terms is a defect (see §3) |
| 13 | Duplicate owner | DR: instance with the traffic; PB/WB: higher CVR at lower CPC, 4 coexistence reasons; SR code: most orders > lowest ACoS; LP: sales > orders > ACoS…; KCP: sales then ACoS | **Coexistence test first** (stage-stack, placement-split, variation-split, sibling ownership). Else **owner = higher CVR at lower CPC with ≥15 clicks each; below that, most orders; tie → longer clean history**. Losers withheld (paused), nothing else changed | Rate beats volume when both have data; volume is the fallback |
| 14 | Normalisation | PH/WB: word order preserved, singular↔plural merge; KCP: sorted tokens, stop-words dropped; B6: close-variant (plural, %) | **Word order preserved; singular/plural and symbols merge**; sorted-token form only for grouping reports, never for ownership or deployment | Amazon treats word order as distinct; plurals are close variants |
| 15 | Objectives | OC: brand→Defensive, Auto/Broad→Discovery, Exact→Ranking, PT→PC; PB adds Market Share, Conquest; WB: own-PT Defensive, competitor PT Conquest | **OC table**, plus: competitor PT = Conquest, own PT = Defensive, category PT = Profitable Conversion; Market Share only when declared. Decided per campaign from targeting, never from the name | Targeting is structural; names drift |
| 16 | Non-ranking judgement | SR: RPC × objective band, Target ACoS 50% BE / Max 75%; B6: 30 & 90-day ACoS vs BE, cut ≤30% base, 2× BE on ≥30 clicks → block | **Layered**: over BE on both 30 & 90 d → cut ≤ 30% of base; > 2× BE on ≥ 30 clicks → block/stop; ≤ 50% BE with orders → scale-eligible (+≤25%) | Two windows avoid reacting to noise; bands give a scale test |
| 17 | TACoS | PB/WB: bands and tiers drive envelopes; SR: routing only; B6 owner: no numeric TACoS proposals | **Monitor and decompose; no TACoS target unless the owner sets one**; PB bands listed as reference only | Owner rule; TACoS mixes organic effects |
| 18 | Amazon suggested bids | PB/WB: required for launch bids; B6 owner: never | **Not used**; launch bids from break-even maths | Owner rule; avoids anchoring to Amazon's range |
| 19 | DSTR | PF: total sales at target, organic netted, ceil, floor 1; WB: market sales at target, ÷ CVR, no netting (WB defect D-78) ; SR: bulk DSTR, floor 1 | **DSTR = daily sales needed at target rank** (market data; floor 1/day). **Paid sales needed = DSTR − our current organic sales on the term** (labelled proxy). **Required TOS clicks = paid ÷ own achieved TOS CVR**; budget = clicks × TOS price × 1.05 | Netting avoids doubling spend; own achieved CVR, not a target CVR |
| 20 | Four-quadrant benchmark | SR: sheet targets (Market CTR × 1.10, CVR × 3.0 keyword); DE: ≥0.95 × market; QA: syntax × 1.10, fail < 0.9 × target; LTSF: market else medians | **Syntax: CTR and CVR vs Market × 1.10; fail below 0.9 × target. Keyword CVR target Market × 3.0.** No SQP → portfolio medians, labelled provisional | Keeps the locked quick-audit thresholds |
| 21 | Negation thresholds | PF ≥10 clicks; STR tree (5 clicks, relevance); WB occurrence evidence | **STR tree** (irrelevant ≥5 clicks; exact rows manual review; brand never); rows > 10 clicks & 0 orders flagged first | Relevance decides negation; clicks decide urgency |
| 22 | Harvest | PB: ≥3 orders; B6: ≥3 orders ≤30% ACoS; STR: tiers by ACoS (≤15 hero, ≤20 exact, ≤30 phrase-first) | **≥3 orders and ACoS ≤ BE, no live exact owner** → exact; match/campaign tier by STR ACoS tiers | Orders prove demand; BE keeps it profitable |
| 23 | Discovery build | PB: ≥100 exact clicks or coverage gap; Broad ~60%, Phrase ~80% of exact ceiling | **PB rule** | Only source with a rule |
| 24 | WAS ceiling | SR/QA: 10% (discovery 40%); PB: product waste <15% | **10% campaign (40% discovery)**; product-level waste reported | Campaign-level is actionable |
| 25 | Escalation | SR: 2 consecutive flat/backfired; PB/WB: same verdict 4 cycles = diagnosis error | **Both**: 2 → escalate the lever; 4 → re-diagnose the row | Different failure types |
| 26 | Sufficiency stop | PB: target 2 clean weeks → −10%/wk to floor 5–10¢ under blended CPC; SR: rank achieved → retag PC / ×0.9; B6: HOLD RANK (no raise) | **B6 HOLD RANK first 2 weeks, then PB taper**; restore on slip (>2 places top-5, any slip below target) | Protect new rank before tapering |
| 27 | Deals | PB: separate deal-state economics, 2-week guard, deals never originate a push; SR: deal blocks cuts but not bleed stops; B6: deal-day budget exception | **All three**: deal-state margin and CVR computed separately; no judging deal days; bleed stops still run; any deal budget is an explicit time-boxed exception | Deals distort every rate |
| 28 | Rule codes in text | PB: none in delivered text; DR examples use codes | **Rule IDs allowed in workbook Rule columns; never in narrative documents** | Traceability for analysts, readability for owners |
| 29 | Colour/variation routing | WB: from Product Ad rows; B6: ranking = White (best seller), discovery = clearance colour, switch never changes size | **Both**: read routing from Product Ad rows; ranking advertises the size's best seller; discovery advertises the clearance colour; size never changes | Rank accrues to the hero; clearance uses discovery traffic |
| 30 | Relevancy cut-offs | STR: ≥60 high / 35–60 moderate / <35 not; LP scorer 92/85/78/64/50/36/15–30/0 | **LP scorer for the % ; STR cut-offs for decisions** | Scorer gives the number, STR gives the action |
| 31 | Competitor tiers & influence | LP: brand-resolved AdInsight reads; B6: ASINsight tiers + R-CI rules | **B6 R-CI rules + LP brand resolution** | Combined |
| 32 | Minimum budget | SR: raise <$10 to $10; PB: budget cuts >$50/day need approval | **Both** | Compatible |
| 33 | Market/"suggested" price concept | WB/PB launch position "middle of suggested range" | **Replaced** by break-even-based launch price (see #18) | Owner rule |

### 2b. Additional resolutions (settled while writing the references)

| # | Topic | Resolution (default) |
|---|---|---|
| 34 | Marginal ACoS on a raise | Freeze the raise at the prior rung when marginal ACoS > 1.5 × average [SR]; unwind one step when > 2 × blended [PB]. Freeze first, unwind second |
| 35 | Phrase-only campaigns | **Discovery** (B6, WB). OC's script default of Profitable Conversion is not used |
| 36 | Exact terms that are not generic demand | Colour, competitor-brand, other-language and misspelled exact terms → **Profitable Conversion**, not Ranking [B6 R-O1], applied on top of #15 |
| 37 | Size of a non-ranking cut | Over break-even on **both** 30 and 90 days → cut up to **30% of base** in one step (#16). The 15%/cycle limit in #5 applies to target-chasing trims, not to this rule |
| 38 | Relevant term, ≥20 clicks, 0 orders, no live exact owner | **REVIEW** (fix queue: listing, price, colour, placement). BLOCK only when irrelevant or another product type. With a live owner → REDUCE |
| 39 | Conversion deficit (CVR far below target on ≥40 clicks) | Bid −15% and refer to Brand Management [SR]; no rank push until the offer is fixed |
| 40 | "Holding the top" | Decisions use **≥30% top-of-search impression share + top-3 sponsored**; the quick-audit 22.5% TOS IS stays a reporting reference |
| 41 | Human confirmation by search volume | SV ≥ 500, gate failures, structural changes, bid moves >25% outside an approved push plan, budget moves >$50/day. An approved push plan covers its own +30%/day steps |
| 42 | Stock during a push | Projected cover must stay **Green (≥60 days) through the push checkpoint**, or the push is blocked, shrunk or time-boxed |
| 43 | LTSF-clearance ceiling | 1 × break-even on forward-cash economics (COGS sunk); the 50% ACoS band is reference only |
| 44 | New conquest target | Must be OFFENSIVE **and** win ≥2 of price / rating / review count [PB]; else TEST. Existing targets are judged on their own clicks and orders (R-X3–X5) |
| 45 | Sponsored Brands / video bids | Start at break-even; ceiling 2 × break-even on push terms and on brand terms with verified competitor presence; 1 × elsewhere |
| 46 | Competitor-consensus thresholds | Stated as a share of the measured roster ("a majority of measured rivals"), not a fixed count |
| 47 | Discovery price anchor | "Exact ceiling" for Broad ~60% / Phrase ~80% means the exact term's **break-even** CPC, not the 2× push ceiling |
| 48 | Base far above product-page break-even | Price over ceiling → to ceiling this cycle via base + boost together; the 50% base-cut limit still applies, so a second step is scheduled if needed |
| 49 | Velocity for zones | 30-day actual pace (deal/stock-out windows corrected and labelled); the inventory file's planned velocity shown beside it |
| 50 | WAIT duration | Held until a named re-test date or until the owner declines the fix; then BREAK-EVEN |
| 51 | Non-push ranking term below break-even | KEEP (no raise) unless it qualifies for the push |

---

## 3. Known defects in source implementations (do not copy)

- SR impact review references undefined variables in the freeze/backfire branches (crash); Freeze/Floor never populated.
- SR zero-order branch writes "$0.50 + pause and negate" for any match type incl. exact Ranking — contradicts "exact protected".
- SR turn-off thresholds doubled twice (effective 200/120/100/60/50%).
- SR/DE silent global break-even default 0.1986 when a SKU has no economics — must halt instead.
- SR/DE CVAR, Yellow freeze, budget steps, harvest, deal-price break-even recompute: specified, not built.
- WB D-78: DSTR ÷ CVR without organic netting doubles required spend.
- B6 engine (29 Sep run): 32 failures documented in `examples/b6-case-study.md` (deal not read, blended margin, dose jumps, wrong colours, duplicate owners, brand negatives before exacts ready, etc.).

## 4. Gaps in the sources

- No weighted listing-quality score exists; use the 1–10 competitor comparison per element (reference 09).
- Review themes are not in any connected data source; require a manual read or an external review tool.
- Keyword-level competitor history is not available from single exports; use rival-level trend × current ranks as a proxy and label it.
- Quick-audit FRAMEWORK/locked-threshold files and the phasing matrix were not in the synced skills; thresholds here come from the SKILL/config text.
