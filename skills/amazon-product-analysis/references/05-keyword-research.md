# 05 — Keyword research, classification and keyword decisions

Phase 4 of the framework. Output: **every term with class, relevance, demand, position, owner and one decision**, each with its trail (input → metric → rule → decision → action → expected outcome → validation date). Campaign-level decisions are in `06-campaign-ppc-decisions.md`; placement pricing in `07-placement-and-bidding.md`; competitor keyword landscape in `08-competitor-market.md`; quadrant diagnosis and listing work in `09-listing-positioning.md`.

## Contents
1. Build the keyword universe
2. Normalise (resolved)
3. Classify every term
4. Demand tiers and hero / halo roles
5. Syntax and roots
6. Relevancy — scoring against the live listing, cut-offs
7. Indexing and rank
8. SQP roll-up, derived metrics, target CTR / CVR
9. Ownership — one live exact owner per term
10. The keyword decision order (16 steps)
11. Wasted spend and negation
12. Harvesting
13. Discovery candidacy and pricing
14. Phasing and launch selection
15. Gap keywords
16. Per-keyword output columns
17. Anti-patterns
18. Open questions for the owner

---

## 1. Build the keyword universe

**Universe = MKL ∪ SQP ∪ search-term report (STR) ∪ bulk targets (live and paused) ∪ competitor keywords ∪ Cerebro / Data Dive pulls.** One row per normalised term (§2). Record on each row which sources it came from — a term only in the STR is a discovery find; a term only in competitor pulls is a gap candidate.

| Source | Contributes | Rules |
|---|---|---|
| MKL | SV, relevancy (`Relevancy`, fallback `Derived Relevancy`; label `Categorization`), organic rank, syntax, indexed flag, PPC-targeted flags per match type | > ~30 days old = stale (finding). Syntax verified against the account taxonomy. Indexed field unvalidated → ask when it would move money. [E, PB] |
| SQP | Market and brand funnel per query, market price, query volume | Roll-up §8; 13-week window. [SQP, B6] |
| STR | Shopper terms (`Customer Search Term`) with spend/clicks/orders/sales per campaign × match type; bid keyword = `Targeting` | Filter to the exact `Portfolio name` string first, then aggregate. Bucket from `Targeting`: close-match / loose-match / substitutes / complements → Auto; `asin="…"` → product target; `category="…"` → category; else match type. Read 30 and 90 days. [STR, B6] |
| Bulk (all states) | Every exact / phrase / broad target, live or paused, and its advertised SKU | Ownership §9. Live = keyword AND campaign enabled. [PB, LP] |
| Target ranks | Rank target per term (presence = ranking flag); gap = organic − target | [STR] |
| Rank crawl (Data Rova, Data Dive gap-fill) | Organic and sponsored rank per day | §7. [SR, B6] |
| ASIN Insights / Data Rova | DSTR, organic vs ad traffic | Never invented; blank = unsized. [E, PF] |
| Competitor pulls (ASINsight / AdInsight / Data Dive / Cerebro multi-ASIN) | Rival ranks, traffic, ad types, contested terms | Brand-resolved, dated, coverage stated (`08`). Implausible or identical odd SV across files → verify, exclude from totals. [LP, B6] |
| Cerebro (own ASIN) | Extra terms, SV, own rank | Suggested-bid column = context only, never a price (owner rule). [E, #18] |

Join rules: key = `strip().lower()` of the term (display the original casing); no match → **blank, never 0**; safe division everywhere (`a/b if b else blank`). [E]

Example (B6): 841 search terms with spend in 30 or 90 days; 2,266 market keywords pulled from ASINsight (all addressable ones).

---

## 2. Normalise (resolved — conflict #14)

1. Lowercase, collapse spaces, strip symbols (`[^a-z0-9 ]`, incl. `%`, `+`, `™®©`). Keyword text written to a bulk must contain no symbols. [CB]
2. **Word order is preserved.** "queen bamboo sheets" ≠ "bamboo sheets queen". Word-order variants are separate terms with separate history — never duplicates. [PH, PB, #14]
3. **Singular ↔ plural and symbol variants merge** into one identity (close variants: "sheet"/"sheets", "100% bamboo"/"100 bamboo"). Keep the higher-SV form as the display/deploy form; aggregate SV. Singularise tokens of length > 3: `-ies → y`; `-ses / -xes / -zes / -ches / -shes` drop `es`; `-ss` unchanged; else drop trailing `s`. [PH, KCP, SR, B6]
4. **Sorted-token form** (tokens sorted, stop-words dropped: the, a, an, for, of, to, and, in, my, with, on, your, this, that, is, are, best, s, size) is allowed **only for grouping reports**. Never for ownership, duplicates or deployment. [KCP, #14]

Why: Amazon treats word order as a different query; plurals are served as close variants by Exact.

---

## 3. Classify every term

Run the classifier on the term text, first match wins, in this order. Classes drive objective eligibility, the decision order and variation routing.

| # | Class | Detect | Why it matters | Exact objective | Hard constraints |
|---|---|---|---|---|---|
| 1 | **ASIN** | `^b0[a-z0-9]{8}$` (lowercased) | Product-page intent | — (product-targeting loop) | Classify the ASIN's owner first: own / own other product / mapped competitor / unmapped (`08`). [E, B6 R-X] |
| 2 | **Brand (own)** + misspellings | Substring of brand name or any listed misspelling (keep the list, e.g. `decolure, decoloure, decloure, decolore`) | Cheapest, most profitable orders | Defensive | **Never blocked or negated.** A misspelling missing from the list gets flagged for negation (known failure). [E, B6 R-K8, OC] |
| 3 | **Competitor brand** | Mapped competitor brand list (`08`) | No organic rank on another brand; trademark risk | Profitable Conversion | Never Ranking. Existing conquest exact = live tactic; else evaluate-only. [B6 R-O1, LP] |
| 4 | **Other product type** | Category off-topic list (§6.1) or wrong material ("silk sheets" for bamboo) | Spend with no demand fit | — | Blocked on relevance (§11); never launched. [LP, B6 R-K2] |
| 5 | **Language / misspelling** | Non-English tokens ("sábanas"); misspelled generics | Usually uncontested; listing score ≈ 0 = no on-page copy, not irrelevance | Profitable Conversion | Never Ranking. [B6 R-O1, LP] |
| 6 | **Colour** | Product colour list | Shopper asked for a colour | Profitable Conversion | Advertise the named colour in the term's size. [B6 R-C3] |
| 7 | **Size** (+ core) | Size tokens (§5) | Shopper searched a size | Ranking allowed | Route only to that size; a switch never changes size. [PH, B6 R-C4] |
| 8 | **Attribute** (+ core) | cooling, deep pocket, organic, 6-piece… | Tests our differentiation | Ranking if the attribute is in the listing | Routes only to a matching SKU; OOS → hold at bid floor, no substitute. [PB, LP] |
| 9 | **Core** (niche generic) | Root material / form wording ("bamboo sheets") | Where organic rank is built | **Ranking** | Push only via push rules (`06`). [B6 R-O1] |
| 10 | **Generic head / adjacent** | Category words without the niche root ("bed sheets") | Field priced for another product; CVR can't carry our price | Profitable Conversion | **Never pushed, whatever volume**; guard §10 step 10. [B6 R-CI1] |

- The class decides whether an Exact campaign may carry the Ranking objective: a Ranking tag on a colour / competitor / language / misspelling / adjacent-generic term is blocked (→ Profitable Conversion). Campaign objective itself is decided from targeting at campaign level (`06`). [B6 E18, OC, #15]
- Classify against the MKL label too; labels can be wrong (Example (B6): "red bamboo sheets" labelled Not Relevant while converting at 33.6% ACoS). Where classifier and label disagree, show both and use the relevancy score (§6). [B6]

Example (B6): 429 core, 198 ASIN, 94 brand, 34 colour, 33 other product type, 28 adjacent generic, 18 competitor brand, 7 Spanish/misspelling.

---

## 4. Demand tiers and hero / halo roles

| Tier | Monthly SV | Keywords per campaign | Role |
|---|---|---|---|
| VHSV | ≥ 10,000 | 1 (isolated) | Hero |
| HSV | 1,000–9,999 | 1 (isolated) | Hero |
| MSV | 500–999 | 3 (halo stack) | Halo |
| LSV | 100–499 | 10 (halo cluster) | Halo |
| VLSV | < 100 | 10 (halo cluster) | Halo |

[PH v5, authoritative]

- **Hero** = VHSV / HSV, **or** has a rank target, **or** top term of its syntax (rank targets promote to Hero within each syntax). Everything else = Halo. [PH]
- Other SV gates used elsewhere: launch SV floor **~250** (confirm per product); Cold ranking candidate needs **SV > 500**; full per-row analysis at **SV ≥ 250 or top spend decile** (tail gets the same rules + exception alerts); human confirmation for decisions on **SV 500+**. [PB]
- **SV% = term SV ÷ Σ SV** of the universe; ΣSV% must equal 1.0. [MDB]
- Record the SV source: MKL (monthly, Helium 10/SQP) and ASINsight (weekly) do not reconcile — never mix them in one column. [B6]
- Concentration: one term > ~25% of product clicks, or top 5 > ~60% → needs a declared head-term push, else explained finding. [PB]

---

## 5. Syntax and roots

**Syntax** = the segment a term belongs to; it sets the diagnosis mode (quadrant, `09`), never a keyword's bid.

- Pipe form `Material|Size` (e.g. `Bamboo|King`, `Cooling|Queen`), plus labels `Generic`, `Generic_HSV`, `Generic_VLSV`, `Branded Keyword`, `Competitor Branded Keyword`, `ASIN Target`, `Irrelevant Fallback` (`*`). [PH, STR]
- Full taxonomy `Root | Product Form | Segment`; a 4th level only where a sibling needs disambiguating (e.g. `Cooling | Sheets | Queen | Core` because a `Color` sibling exists). Segment may be number + unit. [PB]
- **Precedence, first match wins: Branded → Competitor Branded → Irrelevant → Generic → Spanish/language → In-family.** No permanent Unclassified bucket; an unconfirmed near-miss mapping → ask. [PB]
- Material tokens per product (first = display material; e.g. bamboo line: bamboo, viscose, rayon). Size tokens, **longest first**: california king / cal king → California King; split king; twin xl; full xl; olympic queen; short queen; rv queen; queen; king; full; double; twin. **California King is checked before King in every regex and every classification stage** (a known defect matched KING inside CALKING). [PH, SR]
- Syntax logic for a product not already defined → ask; never invent. [MDB]

**Roots** (for root performance and drill-downs):
- A root = a phrase of **1–5 words, contiguous, word order preserved, appearing in ≥ 2 distinct search terms**. Root metrics = sum over every term containing it (roots over-count spend by design). Cap 250 child terms per root. [STR]
- Phasing drill-down: top 200 roots by total SV with ≥ 2 keywords and ≥ 1,000 SV; cap 50 keywords per root. [PH]
- Root status (STR engine; target = the product's break-even ACoS): orders ≥ 1 & ACoS < BE → Healthy/Scalable (scale, harvest best children to exact); orders ≥ 1 & ACoS ≥ BE → Needs Optimisation (reduce broad/auto spend in the root, promote best children); 0 orders & clicks ≥ 5 → Wasted (find and negate the driving children per §11); 0 orders & clicks < 5 → Low Data. [STR]

---

## 6. Relevancy — scoring against the live listing, cut-offs

**Resolution #30: the listing scorer gives the %, the STR cut-offs give the action.**

### 6.1 Listing scorer (second opinion; never overwrite the original)
Keep original `Relevancy` / `Derived Relevancy`; add `Updated Relevancy %`, `Updated Relevancy Source`, `Updated Relevancy Confidence`, and a methodology note. [LP]

Reference text = live title + all bullets; lowercase; strip ™®©–; keep a-z, 0-9, space, hyphen; drop "w/". Build: `words` = non-stopword tokens of length > 2; 2-, 3-, 4-gram sets (stop-words kept, so "for hot sleepers" survives); `full` = whole cleaned string. Stop-words (unigrams only): a an the and or with our your for to in on of is are that this will you from all every without w upgrade now discover indulge experience ensure ensures ensuring these those staying wake up perfect pure elevate enjoy.

| # | Test (first match wins) | Score | Source | Confidence |
|---|---|---|---|---|
| 1 | Category column says Irrelevant / Competitor Branded / = Branded Keyword (skip if the column is empty for every row) | 0 | disqualifier_override:category | HIGH |
| 2 | Keyword of ≥ 3 words appears verbatim in `full` / 2-word keyword is a listing bigram | 92 / 85 | phrase_match_listing | HIGH |
| 3 | Contiguous overlap, longest first: 4-gram / 3-gram / 2-gram | 78 / 64 / 50 | fourgram / trigram / bigram:<words> | 4-gram HIGH; 3-gram HIGH if keyword ≤ 4 words else MEDIUM; 2-gram MEDIUM if ≤ 3 words else LOW |
| 4 | Off-topic term or pillow regex | 0 | disqualifier_override:offtopic_term | HIGH |
| 5 | Theme trigger (longest trigger first) | 36 | theme_match:<theme> | MEDIUM if ≤ 3 words else LOW |
| 6 | Any non-stopword token overlap | round(15 + 15 × overlap ÷ keyword length) → 15–30 | unigram_partial | LOW |
| 7 | Nothing | 0 | no_match_in_listing | HIGH |

[LP relevancy_scorer]

- **Off-topic list** (swap per category). Sheets: chair, comforter, mattress protector, mattress topper, curtain, rug, decor, kitchen, "mat ", duvet, "blanket only", towel, cooler. **Pillow regex** `\bpillows?\b(?!\s*-?\s*cases?)(?!case)` — kills "cooling pillow", keeps "pillowcase", "pillow case", "pillow-top". Hand-check a sample of pillow terms after every run. [LP]
- **Themes** (use a theme only if its concept is actually in the listing; swap per category): cooling_comfort, hot_sleepers_sweat, moisture_breathable, material (bamboo/viscose/microfiber — swap for the real fabric), deep_pocket_fit (incl. the listing's depth figure, e.g. 17"), easy_care_durable, soft_luxury, sleep_quality, sheet_set_core. [LP]
- **Caveats — state them in the methodology note:** will disagree with the original columns (different vocabulary); non-English ≈ 0 = no on-page copy, not irrelevance; the reference variant's size/colour words give a slight edge to terms naming them; bullets contradicting the title variant (King title, "Queen" bullets) = listing defect → flag to `09`, score the literal text; own brand terms score 0 via the category override — brand decisions come from class (§3), never from this score. [LP]

### 6.2 Decision cut-offs (STR)
| Tier | Rule | Use |
|---|---|---|
| **High** | ≥ 60% or label "Highly Relevant" | Never negated on relevance; zero-order → fix queue / REDUCE |
| **Moderate** | 35–60% | Negative exact at ≥ 5 clicks, 0 orders, if not a rank target |
| **Not relevant** | < 35% or label "Not Relevant", or no relevancy signal | Negative exact at ≥ 5 clicks, 0 orders |

[STR]

### 6.3 Launch relevancy tiers (for §14)
- **Highly relevant** — has every defining attribute of the product; launches first and fully.
- **Semi-relevant** — missing a sibling-disambiguating feature, or a secondary synonym (e.g. "blanket" on a comforter).
- **Not relevant** — wrong category or material, competitor brand → never Exact; own brand → Defensive.
- **Unclassified** → re-score before any decision. [PB]

---

## 7. Indexing and rank

- **Indexing gate (before any spend):** not indexed → no spend, open an indexing/listing task. A ranking term present only in backend search terms → listing task before funding. [PB]
- Indexing proxy when no indexing check exists: crawl rank present = ranking; a rank-targeted term with no crawl rank → "Not ranking — check indexing"; blocks a push until fixed. [B6]
- **Organic rank** = median over the window, unranked days counted; **NR if half or more of the days are unranked**. 0 / blank in Data Rova = not ranked (store as 101). Match terms exact lowercase/trim only — no fuzzy or reordered matching; untracked → "not tracked". [B6, SR]
- Name the rank source on every row: two rank tables can disagree by ~7 places (Example (B6)). Ranking verdicts need **≥ 1 month** of rank history (ideally 3); less → out of scope for a ranking verdict. [B6, PB]
- Rank arc: state overall, 14-day and 7-day separately; exclude stock-out and re-route stretches; deal-state arc kept separate — the clean arc governs. Rank drop > 10 places in 30 days while getting clicks → freeze price moves, find the cause (`09` §5, `06` §6.3). [PB, B6 E4]
- Organic rank with no paid support on a relevant term = cheapest coverage (route aged SKUs there). Backend terms close coverage gaps first, free. [LTSF]

---

## 8. SQP roll-up, derived metrics, target CTR / CVR

### 8.1 Parent roll-up (child-ASIN export → one row per query)
- **Market columns (`… Total Count`) are identical on every child row → take once (max per query). Brand columns (`… ASIN Count`) → sum across children.** Summing market columns multiplies by the number of children and destroys every share. [SQP]
- Ignore SQP's precomputed rates; recompute:
  - Impression / Click / Cart-add / Purchase **share** = Brand ÷ Market at that funnel stage.
  - **Market CTR** = market clicks ÷ market impressions; **Brand CTR** = brand clicks ÷ brand impressions.
  - **Market CVR** = market purchases ÷ market clicks; **Brand CVR** = brand purchases ÷ brand clicks.
  - CTR / CVR variance = brand − market (percentage points).
  - Market price = `Purchases: Price (Median)` (fallback clicks median), take once; brand price = median of children's `Purchases: ASIN Price (Median)`; revenue = purchases × price; revenue per click = revenue ÷ clicks. Query volume take once. [SQP]
- Verify: rows = unique queries; market impressions = raw Total Count; brand ≤ market; shares 0–100%. Percent strings ("52%") → 0.52. [SQP]
- Impression-share proxy where no IS report exists: SQP brand impressions ÷ market impressions (label it a proxy). [E]

### 8.2 Targets and flags (resolution #20)
| Level | Target CTR | Target CVR | Fails when |
|---|---|---|---|
| Syntax (quadrant) | Market CTR × 1.10 | Market CVR × 1.10 | below 0.9 × target |
| Keyword | Market CTR × 1.10 | **Market CVR × 3.0** | below 0.9 × target |

- No SQP match → keyword targets **blank** (never guessed). Syntax level with no SQP → portfolio medians, labelled **provisional** (medians are relative: half fail by construction). [SQP, QA, #20]
- Targets supplied in a sheet are re-derived: > 2% drift on > 10% of rows → halt that input. [SR]
- **Listing flag:** our CTR or CVR below market (ratio < 1.0) on **≥ 30 clicks** → no push until the listing is checked (`09`). [B6 E15]

---

## 9. Ownership — one live exact owner per term

Build an **owner map on normalised terms (§2; close variants count)** across every exact target in the bulk, live and paused, and across sibling products' bulks for shared head terms (missing sibling bulk = named gap). [B6 R-S1, PB]

| Owner state | Meaning | Decision |
|---|---|---|
| One live exact owner | keyword AND campaign enabled, correct variation | OK; judge the term through §10 |
| > 1 live exact owner | same normalised term, same match type, ≥ 2 campaigns | Coexistence test, else **DEDUPLICATE** |
| Only paused exact owner(s) | exists but not serving | **CHECK OWNER**: restart the paused keyword (at break-even, after any deal window) if the term is wanted; never build a duplicate; no price change on a paused row |
| No exact owner | only discovery / phrase / broad / auto serve it | Candidate for HARVEST, launch or discovery rules |
| Exact owner exists and discovery campaigns also serve it | two prices on one term | Negative exact in the discovery lanes (isolation wall, §11.3) — brand terms only after the brand-negative gate |

[B6 R-S1, R-S2, R-K7, E6, E11]

**Coexistence test first** — both instances stand if one of these holds: [PB, #13]
1. **Stage-stack** — the instances deliberately serve different lifecycle stages of the plan.
2. **Placement-split** — the instances are deliberately split by placement.
3. **Variation-split** — each instance advertises a different variation (e.g. colour-named routing; "different SKU targeting" is not a duplicate). [KCP]
4. **Sibling ownership** — the other instance belongs to a sibling product under the family owner assignment (family owner score = margin/order × sibling CVR on the shared root × sibling inventory days; exact tie → human).

**Duplicate owner rule (resolution #13):** owner = **higher CVR at lower CPC with ≥ 15 clicks each**; below that, **most orders**; tie → **longer clean history**. The owner must advertise the right variation (ranking → the size's best seller; colour term → the named colour); if not, re-point it rather than pick another instance. Losers are **withheld (paused), nothing else changed** — no bid on a withheld row. [PB, B6, #13]

- Different match types on one term are purposeful, not duplicates; word-order variants are not duplicates. [SR, PB]
- Status rule: an instance is **Paused if keyword state OR campaign state is paused** (ad-group state is reported separately, not used for the duplicate status). A keeper sitting in a paused campaign won't serve — count and state these. [LP]
- Validate: no group with > 1 enabled instance; no duplicate group with 0 enabled instances; singletons untouched (report dormant count; ask before enabling). [LP]
- Several issues on one term → fix in this order: negate the variant in discovery → turn off same-SKU duplicate exact → turn off variant covered by a higher-SV form → review same-SKU normalised duplicates; different SKU = no action. [KCP]

Example (B6): 8 terms DEDUPLICATE ($748 / 90 days), 23 terms CHECK OWNER ($2,274 / 90 days); "bamboo queen sheet set" was bought by 4 live exact campaigns.

---

## 10. The keyword decision order (16 steps)

Applies to every search term (and every untargeted universe term through steps 1–6, 10, 15–16). **The first step that fires ends the row; record the step.** Preconditions from the master order run first: data validity (quarantine), goal and deal state (no verdict on deal-day data; no builds on deal days — negatives and reductions may load, harvests and new exacts wait for the post-deal audit), indexing (§7), live state. Windows: clicks/orders/ACoS on **90 days** unless stated; REDUCE reads **30 and 90**.

| # | Step | Fires when | Decision → action | Rule |
|---|---|---|---|---|
| 1 | **ASIN** | Term matches `^b0[a-z0-9]{8}$` | Judged with product targeting (own → DEFEND / cross-sell; competitor → OFFENSIVE / TEST / AVOID, SCALE / REDUCE / BLOCK) in `08` | [B6 R-X, E] |
| 2 | **Brand** | Own brand or misspelling | **DEFEND**: owned by brand exact campaign(s) on the hero variation, enough budget, judged on ACoS ≤ break-even. Never blocked. Brand negatives in generic discovery only after the brand exacts are defensive, on the hero and funded | [B6 R-K8, R-N3, R-S4] |
| 3 | **Funded push** | Term qualifies on every push gate and is funded within the spend limit | **PUSH** — price, base, boost and budget per the push plan (`06`, `07`) | [B6 R-K1, R-P1] |
| 4 | **Push candidate held** | Rank-targeted core term failing a push gate: listing flag (SQP CTR or CVR < market on ≥ 30 clicks), ceiling < our TOS CPC, hero stock not Green (< 60 days, stock-out before the next inbound, cover < days to next arrival + 7, or projected cover leaving Green before the checkpoint), keyword not live, not indexed | **WAIT** — name the failing gate; runs at break-even meanwhile; ceiling-below-cost needs an owner decision on a time-limited ceiling raise | [B6 R-P1, E14, E15, F25, F26, #9, #42, #50] |
| 5 | **At target** | Rank-targeted, organic rank ≤ target | **HOLD RANK** — keep today's price, no raise; rejoins the push if it slips past target; taper only after 2 clean weeks at target (`06`) | [B6 R-P8, #26] |
| 6 | **Too far** | Rank-targeted, current rank more than **~30 places** from target | **MONITOR (too far)** — discovery / break-even only; revisit when within ~30 places | [B6 R-P1 reach] |
| 7 | **Irrelevant / other product type** | Other product type, Not relevant (< 35% / "Not Relevant") or no relevancy signal, **≥ 5 clicks, 0 orders**; or moderate (35–60%) ≥ 5 clicks, 0 orders, not a rank target; or structurally off-target (competitor brand without a conquest owner, foreign ASIN, other category) | **BLOCK** — negative exact (or phrase, §11.1) in every discovery campaign that serves it. > 10 clicks & 0 orders listed first | [STR, PB, B6 R-K2, #12, #21] |
| 8 | **Zero-order, relevant** | High relevancy, **≥ 20 clicks, 0 orders** | Live exact owner → **REDUCE**: cut to the break-even floor or pause the exact keyword; review relevance and listing (fix queue). No exact owner → **REVIEW** (fix queue: price / listing / placement; not negated). Never negate an exact ranking term or a brand term | [B6 R-K2, STR, PB, #12] |
| 9 | **> 2 × break-even** | ACoS > 2 × break-even ACoS on **≥ 30 clicks**, not a rank target | **BLOCK** in discovery; **REDUCE** in its exact owner (bid to break-even). Guard: a term still selling (≥ 10 orders / 90 d) that rivals buy is REDUCE, never BLOCK; a BLOCK on an addressable term with ≥ 10,000 market traffic and ≥ 5 rivals advertising stands but is tagged "re-test" (back in discovery at break-even after 30 days or a listing/price change) | [B6 R-K3, R-CI9] |
| 10 | **Head-generic guard** | Generic head / adjacent generic class with **SV ≥ 50,000/month**, outside the niche | **MONITOR** — leave in discovery at break-even; never harvested to exact, never pushed, whatever the orders; re-check at 10+ orders | [B6, R-CI1] |
| 11 | **Harvest** | No exact owner (live or paused); **≥ 3 orders at ACoS ≤ break-even**; not other product type; relevant | **HARVEST** — exact campaign at break-even (post-deal), right variation; negative exact in the source in the same upload (§12) | [B6 R-K4, PB, STR, #22] |
| 12 | **Paused owner** | Exact owner exists but every instance is paused | **CHECK OWNER** — restart the paused keyword at break-even if the term is wanted; never build a duplicate | [B6 R-K7, R-S2, E6] |
| 13 | **Duplicate owners** | > 1 live exact owner, no coexistence reason | **DEDUPLICATE** — keep the owner per §9, pause the rest | [B6 R-K7, R-S1, PB, #13] |
| 14 | **Over break-even** | Live exact owner; ACoS > break-even on **both 30 and 90 days**; **≥ 15 clicks (30 d)** | **REDUCE** — bid toward break-even, ≤ 30% a step. 30-day over but 90-day inside → MONITOR ("watch") | [B6 R-K5, R-N1, #16] |
| 15 | **Thin** | < 15 clicks (90 d) | **MONITOR** — no change until 15 clicks; say whether low clicks fit low SV or mean the term is uncompetitive | [B6 R-K6, DR] |
| 16 | **Everything else** | None of the above | **MAINTAIN** — no change, within limits. Rank-targeted term within reach but not in the push → MAINTAIN (ranking, break-even): runs at break-even, enters the push when it qualifies | [B6 R-B3] |

Rules that bind the order:
- **Brand and push terms are never blocked. No exact ranking term is negated.** (quality gate) [B6, #12]
- Converting rows skip the thin-data gate: a term with orders is never parked for "< 15 clicks" (harvest at 3 orders on 9 clicks is valid). [PB, DR]
- Deal days: zero-order and > 2 × BE decisions may still load as negatives / reductions (bleed stops run during deals); harvests, restarts and new exacts wait for the post-deal audit. [B6, #27]
- One term, one direction: after deciding, reconcile across campaigns — no term cut in one campaign and raised in another. [DR]
- Push qualification (steps 3–4) uses the push gates in `06` (plan, TOS CVR above market, reach ~30 places, hero stock, live, ceiling ≥ TOS CPC, listing not flagged). [B6 R-P1]

Example (B6, 841 terms): MONITOR 430 · ASIN → competitor tab 198 · DEFEND 94 · MAINTAIN 38 · CHECK OWNER 23 · REDUCE 22 · PUSH 13 · DEDUPLICATE 8 · WAIT 4 · MONITOR (too far) 4 · BLOCK 3 · MAINTAIN (ranking, break-even) 2 · HOLD RANK 1 · HARVEST 1. "bed sheets" (3 orders on 6 clicks, 56,136 SV) → MONITOR by the head-generic guard: an exact at break-even would buy mostly non-niche shoppers. "cooling bed sheets" rank 70 vs target 10 → MONITOR (too far).

---

## 11. Wasted spend and negation

### 11.1 Wasted-spend list (read first every cycle)
- Include **every** term with clicks ≥ 1 and 0 orders; sort by clicks descending. **> 10 clicks & 0 orders → row RED** (top priority). Children = campaign × match-type slices; **exact-match child rows YELLOW** — always manual review before negating. [STR]
- **WAS% = spend on rows with 0 sales ÷ spend.** Ceiling **10% per campaign, 40% for discovery**; over the ceiling → negation pass. Product-level waste reported. Real ACoS = spend-with-sales ÷ sales. [SR, QA, #24]

### 11.2 Negation tree (relevance decides, clicks decide urgency — first match wins)
| # | Condition | Action |
|---|---|---|
| 1 | Brand term (own, incl. misspellings) | **Do not negate** |
| 2 | ASIN target (≥ 5 clicks context) | Negative exact (ASIN negative target) — unless it is our own ASIN under a stated defensive decision (`08`) |
| 3 | `*` auto catch-all | Negative exact |
| 4 | clicks < 5 | Manual review; monitor to 5+ clicks |
| 5 | High relevancy AND rank target | Manual review: cut bid / fix listing — **do not negate** |
| 6 | High relevancy core term, no rank target | Manual review: fix price / listing / placement, reduce bid |
| 7 | Not relevant (< 35%) or no relevancy signal | **Negative exact**; **negative phrase** if broad+auto occurrences ≥ 2 AND term ≥ 3 words |
| 8 | Moderate (35–60%), ≥ 5 clicks, not a rank target | **Negative exact** |

[STR, #21] Every negation reason cites that occurrence's clicks, spend, orders, relevancy and rank — no root-wide sweeps on non-structural terms. [PB]

### 11.3 Negation modes (name the mode on every negative)
| Mode | When | What |
|---|---|---|
| **Pre-load** | At launch, from the taxonomy + an own-catalogue scan | Other product types, off-topic words, competitor brands not under conquest, own-catalogue terms belonging to sibling products |
| **Reactive** | From the STR each cycle | §11.2 tree |
| **Steering** | When a term gets an exact owner (harvest, launch, decided ranking term) | The owned exact goes in as negative exact in the discovery lanes that also serve it |
| **Isolation wall** | Every owned exact | Owned exact as **negative exact in the lane's broad / phrase + auto / catch-all campaigns, in the same upload** as the exact build | 

[PB, WB]

- Negatives live only in Profitable Conversion, Discovery and Conquest campaigns; Ranking, Market Share and Defensive campaigns carry none; **exact targets are protected**. Placement: campaign-level negative exact / negative product target; target-level pause for a single-ASIN PAT. [SR]
- A decided ranking term with no live exact → same-day exact build + steering negatives in broad/auto (not a harvest case). [PB]
- **Brand-negative gate:** no brand negatives in generic discovery until the receiving brand exacts are defensive, on the hero variation and funded. [B6 R-S4, E10]
- Relevant non-converters go to the **fix queue**, never the negative list. [PB, SR]
- Auto own-ASIN matches: negated unless a stated defensive decision exists (`08`). [WB, DR]

Example (B6): only 3 terms met BLOCK ($105 / 90 d) — "silk sheets" (other product type, 14 clicks, 0 orders), "full xl bamboo sheets" (Not Relevant, 10 clicks), "cooling sheets twin" (25 clicks, 0 orders, owner paused — labelled Relevant, so under #38 it is REVIEW, not BLOCK).

---

## 12. Harvesting

**Rule (resolution #22):** search term with **≥ 3 orders and ACoS ≤ break-even**, relevant, not other product type, and **no live exact owner** → build an exact; **negate it at the source in the same deployment**. [PB, B6, STR]

1. Candidates: orders ≥ 1, discovered **outside exact** (auto, broad, phrase, product targets). Drop Not relevant / < 35%. Drop runaway rows: STR drops ACoS > 45% with < 3 orders (defined against its 30% default target — for another break-even: Owner decision — ask). Sort by SV desc, then spend. [STR]
2. Check ownership first: paused exact owner → CHECK OWNER (restart), never a new build. [B6 R-S2]
3. Head-generic guard (§10 step 10) overrides harvest. [B6]
4. Match type / campaign tier by ACoS (STR tiers, stated in the source against a 30% break-even; confirm the scaling for your product):

| ACoS (STR, BE 30%) | As share of BE | Suggested campaign | Match |
|---|---|---|---|
| ≤ 15% | ≤ 0.5 × BE | Hero — high-conviction exact, bid up | Exact |
| ≤ 20% | ≤ ~0.67 × BE | Standard exact | Exact |
| ≤ 30% | ≤ BE | Phrase first; promote to exact if it scales | Phrase |
| > 30% | > BE | Broad / phrase discovery; improve efficiency first (not a harvest) | Broad |
| none | — | Standard exact | Exact |

5. Objective: decided from targeting and term class per `06` §1 (resolutions #15, #36) — a harvested generic-niche exact is tagged Ranking and runs non-push at break-even until it qualifies for the push (goal gate applies); colour / competitor-brand / language / misspelling / adjacent-generic exacts → Profitable Conversion; Market Share **only if the owner declared it**. STR's ACoS-based objective suggestion (≤ 15% → PC; ACoS > 30% → Discovery; etc.) is reference only. Harvested exacts start at **break-even** on the right variation (colour-named → that colour; generic → size's best seller). [STR, B6 R-K4, #15]
6. Override: a decided ranking head carried by auto close-match graduates below 3 orders (say which case). [PB]
7. Auto terms are read split by close / loose / substitutes / complements; an untagged converting term is classified before harvest. [PB]
8. No harvest builds on deal days; queue for the post-deal audit. The harvest rule is the resolved default (#22); an owner override is recorded if given. [B6, PB, #22]

Example (B6): "king size sheets with corner straps" — no exact owner, 3 orders on 9 clicks at 3% ACoS → exact campaign at break-even on 1 Oct (an adjacent-generic term — no product-defining word — so its exact is tagged Profitable Conversion under #36/#55), then negative exact in the discovery source.

---

## 13. Discovery candidacy and pricing

- **Reactive path:** a term needs **≥ 100 qualified clicks on its own exact history** before a broad / phrase / SB / SBV layer is built. **Proactive path:** a syntax coverage gap (e.g. primary root at 0% phrase), judged on closing the gap. State which path. [PB, #23]
- < 100 clicks → ineligible, **no pricing**; near-miss = within ~20. Keyword vs root-cluster count basis → ask the owner. Singular/plural share one count; word-order variants don't. Check for an existing broad / phrase / auto instance before building. [PB]
- **Price below exact, no placement modifier at launch: Broad ~60%, Phrase ~80% of the exact ceiling** — here the exact term's **break-even** CPC, never the 2× push ceiling (#47); relevancy tier sets position (highly → upper end, semi → lower end). [PB, #47]
- Judge discovery from **15 clicks**, on converting terms per $100 and graduation into exact — not on CPA in its first 30 days. Four auto groups reported separately. Utilisation floor 70%+. [PB, DR]
- Discovery campaigns advertise the size's **clearance variation** (≥ 180 days cover, or ≥ 90 days while selling ≤ size median); ranking stock is reserved for exact. [B6 R-C2, #29]
- Alternative (PF, not default): build phrase/broad only when non-branded cost/order < exact average — record if the owner prefers it. [PF]
- Gap seeding (B6, proposed): addressable core terms with ≥ 3,000 market traffic and no search-term row get an exact target inside the discovery campaign of their size at break-even; no push premium; judged by §10 after 15 clicks. [B6 R-CI8]

---

## 14. Phasing and launch selection

### 14.1 Phases, statuses, groups
- **200-keyword cap per phase**, syntax-priority order, same-syntax overflow into the next phase. Sort: phase ↑ → syntax priority ↑ → Hero first → aggregated SV ↓. [PH]
- Status per keyword: **New Build** (no PPC activity) · **Already Running** (exactly one match type live — expand to the remaining types only if the discovery rule allows) · **Existing Campaign** (≥ 2 match types live — do not duplicate; marked "(existing — skip)"). Restart-before-build applies to paused owners. [PH, B6 R-S2]
- **Campaign Group ID** `{SLUG}-P{phase}-G{n}`, sequential per (phase, syntax, tier, preferred SKU, match type, status) block, tier-capped (1 / 1 / 3 / 10 / 10 keywords). **A group never mixes phase, syntax, tier, SKU, match type or status** (breaks STR attribution). [PH]

### 14.2 Match type and objective
- **Default SP Exact for every keyword, every phase, every tier.** Never broad/phrase by default. Single override: the MKL flags the term already running in another match type → surface that type; precedence SP Phrase → SP Broad → SB Exact → SB Phrase → SB Broad. [PH]
- Objective from targeting and class (`06` §1, #15, #36): generic-niche exact (core / attribute / size) → Ranking (push only when it qualifies; otherwise non-push at break-even); colour / competitor / language / misspelling / adjacent generic exact → Profitable Conversion, never Ranking; existing non-exact → per `06` §1 (Broad / Phrase → Discovery, #35). **Bidding strategy for every new campaign: dynamic bids – down only.** [PH, B6 R-O1, #8]
- Variation routing (colour-aware): term contains a colour and a matching colour SKU exists → that SKU; else the syntax's preferred SKU (ranking → the size's best seller; discovery → clearance variation); **size never changes**; routed SKU needs ≥ 21 days of cover to launch (not the 60-day push gate). [PH, PB, B6, #29]

### 14.3 Launch selection by goal and relevancy tier
| Declared goal | Exact launch set |
|---|---|
| Growth / Scale, Mixed | Highly relevant, then semi-relevant (semi only after its opening conditions) |
| Profit-First, Clearance / LTSF | **Highly relevant only, permanently** |
| Undeclared | Treated as Profit-First |

[PB]

- Order within the set: **tightest rank target first**; SV floor ~250 (confirm). Singular/plural = one identity; word-order variants stay separate. Attribute in the query routes only to a matching SKU; that SKU OOS → hold at bid floor, no substitute; a term failing routing eligibility is never built (not built-then-paused). [PB]
- **Semi-relevant opens only when all six clear:** (1) rank target reached or closing; (2) five-property gate cleared (sized, dated, ceilinged, predicted, funded — `06`); (3) TACoS within the owner's band, only if the owner set one (otherwise monitored only, #17); (4) margin holding; (5) spend ≈ plan; (6) minimum data window met. If 2–3 cycles of real lever fixes still fail, semi opens anyway with the reason stated. [PB]
- **Launch price = break-even maths, not Amazon's suggested range** (owner rule): base and TOS modifier solved from the routed SKU's break-even CPC per placement (`07`). The source's placement shape is kept: Growth / Mixed / Profit-First start with a TOS modifier (source: +100%), Clearance with none. [PB, #18, #33]
- Expected spend per keyword (phasing) = (DSTR − our organic sales on the term, labelled proxy; 0 for a new build) × CPC ÷ CVR, with CPC = the routed SKU's break-even CPC and CVR = own achieved CVR (0.20 only as the phasing default when no own rate exists — label it). Never DSTR ÷ CVR without organic netting (WB D-78). [PH, #18, #19]
- No launches, folds or structural builds on deal days. Human confirmation: SV 500+, gate failures, structural change, bid moves > 25% outside an approved push plan, budget move > $50/day. [B6 E1, PB, #41]

---

## 15. Gap keywords

A gap is a relevant, demanded term we do not target (or target without delivery). Every untargeted row ends as either an **entry candidate with a full launch spec** (match type, price basis, routed SKU, kill condition) or **declined with the reason named** — a declined term stops counting as unexploited opportunity. [DR]

| Gap type | Test | Default treatment |
|---|---|---|
| SQP gap | SQP volume > 0 AND not targeted (PPC "Not Targeted" / Currently Targeting ∈ {NO, N, blank}) | Priority by the syntax's quadrant (below) [AP] |
| Coverage gap | Relevant term ≥ volume threshold → LIVE / PAUSED / MISSING; MISSING with **3+ competitors in the top 30** first | Launch per §14; PAUSED without justification = finding [LTSF] |
| Organic without paid | Ranks organically, no paid support | Cheapest fill; route aged SKUs there [LTSF] |
| Engine-blind | Addressable term with competitor traffic and no search-term row | Gap seeding (§13) [B6] |
| Range gap | Validated demand across competitors for a size/attribute we have no SKU for | Product-plan item for Brand Management, not a campaign (`09`) [LTSF] |

Priority map for SQP gaps by syntax diagnosis (editable per product): STRONG → P1 scale / launch exact ranking; VISIBILITY → P1 launch exact + bid up TOS; CONVERSION → P2 launch selectively, bid to CVR; BOTH FAILING → P2 fix listing / CVR first, hold; niche sizes (e.g. Twin XL, Full XL, RV / Short / Olympic Queen) → P3 backlog; unmapped → review relevance before launch. Never launch gaps on BOTH-FAILING syntaxes or off-category terms. [AP]

- Cross-check coverage against the STR: exact-text matching overstates the gap (close variants already serve). Backend terms close gaps first, free. Sibling-brand overlap = cross-brand bid conflict — resolve before building. Track **SV coverage %**, not keyword count. [LTSF, PB]

---

## 16. Per-keyword output columns (Keyword decisions tab)

Every term, one row, in this order. Missing = blank, never 0.

| Group | Columns |
|---|---|
| Decision | Search term · **Decision** · Rule (id in workbook only) · Why (numbers doing the work) · Action · Expected outcome · Re-read date · Reversal condition |
| Identity | Normalised key · Sources present · Class · Syntax · Root(s) · Hero/Halo · SV tier |
| Demand | SV/month (source) · Weekly SV (source) · SV% · Market traffic |
| Relevancy | Original label and % · Updated % · Source · Confidence · Decision tier · Launch tier |
| Position | Organic rank (30-d median, source) · Sponsored rank · Target rank · Rank gap · Indexing |
| SQP | Market impr / clicks / purchases · Shares · Market & brand CTR, CVR · Target CTR, CVR · Ratios · Listing flag |
| Ownership | Exact owner(s) + state · Owner status · Coexistence reason · Advertised SKU · Correct SKU |
| Performance (30 d and 90 d) | Impr, clicks, CTR, orders, CVR, CPC, spend, sales, ACoS · TOS share / CVR / CPC · PDP share / CVR · ROS share (keyword placement = estimate) |
| Economics | Break-even ACoS and CPC of the routed SKU · Ceiling (ranking terms) |
| Landscape | Rivals present · Rivals advertising · Our share · Landscape verdict (`08`) |

[B6, KCP, MDB, DR]

---

## 17. Anti-patterns

Summing SQP market columns · reordering words or collapsing word-order variants · King before California King · negating on spend alone, or negating brand / rank-target / highly relevant / exact-ranking terms · harvesting a head generic · building beside a paused owner or on deal days · treating the listing score as truth · parking a converting term for thin clicks · contradictory directions on one term · suggested bids or Cerebro CPC used as a price · gap lists padded with close-variant or off-category terms. [SQP, PH, STR, B6, LP, DR, AP]

---

## 18. Open questions for the owner

1. **Relevant zero-order term with no live exact owner.** Resolved — see 13 #38: REVIEW (fix queue); BLOCK only when irrelevant or another product type; with a live owner → REDUCE.
2. **Label mapping.** MKL labels "Relevant", "Lower Relevant" and "Generic" have no tier in any source. This file uses the numeric score (listing scorer if absent). Confirm or give a mapping.
3. **Head-generic guard threshold.** SV ≥ 50,000 comes from one B6 case ("bed sheets", 56,136). Confirm per product, or set a class-only rule (R-CI1: generic terms never pushed, whatever volume).
4. **Harvest ACoS tiers and the 45% runaway filter** are stated against a 30% break-even. Confirm scaling them as shares of the product's break-even.
