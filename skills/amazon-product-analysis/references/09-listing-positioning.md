# 09 — Listing, offer and positioning

Phase 5. Answers the question the PPC numbers raise but cannot settle alone: **is the problem visibility (buy placement), conversion (fix the offer — no rank push), or both?** Output: a quadrant per syntax, a listing and offer comparison against the true competitor set, and a Brand Management findings register with owners. Keyword-level SQP metrics and targets are defined in `05` §8; competitor roster and tiers in `08`.

## Contents
1. Four-quadrant diagnosis per syntax
2. Listing audit — element criteria
3. Competitor comparison per element (1–10)
4. Offer and price positioning
5. Conversion diagnostics
6. Brand Management findings register
7. Review themes — manual read method
8. Open questions for the owner

---

## 1. Four-quadrant diagnosis per syntax

### 1.1 Benchmark and thresholds (resolution #20)
- Unit = syntax (root + modifier, e.g. `Bamboo|Queen`), from `05` §5.
- **Target CTR = Market CTR × 1.10; Target CVR = Market CVR × 1.10** (syntax level, SQP market rates recomputed from the parent roll-up). A metric **fails below 0.9 × target**. [QA, #20]
- Keyword-level CVR bar is **Market CVR × 3.0** (`05` §8.2) — use it for keyword diagnostics, never for the syntax quadrant.
- No SQP → portfolio medians, labelled **provisional** (medians are relative: half the syntaxes fail by construction). [LTSF, #20]
- Read CTR and CVR **at the delivering placement**, not blended. Example: blended CTR 0.626% vs a 1.75% target looked like a listing failure; top-of-search read 2.955% and passed by 1.68×. Show both. [DR]

### 1.2 Quadrants
| CTR | CVR | Diagnosis | Action | Examine | Do not |
|---|---|---|---|---|---|
| pass | pass | **STRONG** | Scale; protect | Nothing | Touch a working listing to solve another syntax's problem |
| fail | pass | **VISIBILITY** | Buy placement (TOS share, modifier — `07`) | Main image vs neighbouring thumbnails, title first 80 characters, price shown in results, badges | Rewrite bullets — shoppers who arrive convert |
| pass | fail | **CONVERSION** | Fix the offer; **no rank push until the fix ships** | Bullets, A+, gallery positions 2–7, price position, rating and review count vs the set | Main-image work (the click already happens); more traffic |
| fail | fail | **BOTH FAILING** | Reduce and reallocate; fix listing first | Whole offer — first check the syntax is genuinely relevant | Polish presentation on a term we should decline |

[LTSF, QA, PB]

- **Syntax sets the mode, never a keyword's bid.** [PB]
- **More traffic cannot fix a conversion problem.** A rank target on a CONVERSION syntax without a funded ranking plan is not a plan. [LTSF]
- Gap keywords on a BOTH-FAILING syntax are held; on CONVERSION launched selectively, bid to CVR (`05` §15). [AP]

### 1.3 CTR root cause (VISIBILITY and BOTH FAILING only)
Needs search-term impression share (IS), TOS impression share and IS rank:

| Reading | Cause | First lever |
|---|---|---|
| IS < 5%, TOS IS < 15%, IS rank > 4 | Placement + auction | Price step within ceiling, then TOS modifier, then base below the bleeding placement |
| TOS IS < 15%, IS rank ≤ 4 | Placement only | TOS modifier up (within ceiling) |
| TOS IS 15–30% | Moderate gap | TOS modifier up (within ceiling) |
| TOS IS > 30% | **Listing issue** | Brand Management finding (§6); no CTR bid change |
| No IS and no rank | Undetermined | No CTR bid change; get the data |

[SR] Percentage steps from the source (+15–25%, +20–25%) are bounded by the step caps and ceilings in `07`.

### 1.4 Spend by quadrant, chronic vs transient
- **Report spend by quadrant** — the most actionable single number (how much money sits on CONVERSION and BOTH FAILING syntaxes). [LTSF]
- Also per syntax: keyword count, spend, CTR, CVR, ACoS, rank, quadrant, **weeks in state**, priority class, actual vs target spend share. Dossier only for chronic, off-share or oversight syntaxes; one scan table for the rest. [PB]
- **Chronic = ≥ 4 consecutive weeks in a state; transient = 1–2 weeks.** Chronic CONVERSION → bids frozen at maintenance, no ranking allowance for that syntax, open a listing / price project. [PB]
- Syntax spend shares: primary commonly ≥ ~60%, secondary ≤ ~25% unless a dated test runs above. Off-share = finding. [PB]

---

## 2. Listing audit — element criteria

Standard: every word, image and bullet is intentional and its job can be named. A word that cannot be justified is a candidate for replacement. Enter with the quadrant result; it decides which elements to examine (§1.2). [LTSF]

| Element | Criteria | Evidence to record |
|---|---|---|
| **Title** | First **80 characters** carry the lead syntax + the primary differentiator. **First 3 words** = the highest-volume, highest-intent syntax we rank for | Word-by-word table: word → syntax or claim served → SV / driver share. Flag dead words. High-volume terms we rank on but omit from the title = free relevance |
| **Main image** | Judged against the **top 8 thumbnails** on the head term, at thumbnail size, on mobile — "on a page of 48 results, what makes ours the click?" Name the category convention (bedding: sheen rendering, colour accuracy, set-contents clarity) and whether we follow it | What each rival thumbnail emphasises, what ours does, the specific difference |
| **Gallery 2–7** | One conversion job per position: fit and dimensions · construction close-up · lifestyle for the lead persona · objection kill · social proof · variation range. Secondary-segment imagery from position 4 onward, never the hero slots | Job per position and the objection/driver it addresses; missing jobs |
| **Bullets** | Ordered by decision priority; each answers one named objection or confirms one named driver, in customer language. A bullet mapping to nothing is deleted | Bullet → objection/driver map |
| **A+ / Brand Story** | Narrative, construction story, comparison module against the audited gaps, placements for secondary segments | Modules present, what each does |
| **Video** | Parity is the entry cost wherever category leaders have it. Existing creator/UGC assets unused = finding | Rivals with video; our assets and their use |
| **Backend search terms** | From the category listings report. Coverage gaps close here first, free. A ranking term that is backend-only needs a listing task before funding (`05` §7) | Terms present, gaps vs the coverage list |
| **Variation-range surfaces** | The variation-range image and the A+ comparison table are **routing surfaces** for aged colourways — show them by use case, not as leftovers | Which variations appear where |

[LTSF, PB]

- **Listing-copy defects:** bullets contradicting the title variant (King title, "Queen" / "4-piece" bullets) → flag to be fixed at source. [LP]
- **Range findings:** validated demand across several competitors for a size/attribute we have no SKU for = range gap (product plan, not campaigns). Low-demand variations carrying aged units justify themselves numerically or become retirement candidates — "a narrower range that turns beats a wide range that ages". [LTSF]
- Archetype A (fixable demand, `04`): listing repair runs on a **48-hour SLA** before any deep discount. [LTSF]

---

## 3. Competitor comparison per element (1–10)

- Set: the **top 5–8 true competitors** — same intent, same material, same category. State the inclusion rule and list what was excluded and why; a padded set invalidates the comparison. [LTSF]
- Score **title, main image, secondary images, bullets, A+, video — each 1–10**, with a note on what is emphasised and how. Our listing scored the same way. [LTSF]
- **No weighted listing-quality score exists in any source.** Do not invent weights or sum the scores into one index; report the element scores side by side and let the gaps speak. [13 §4]
- Per competitor also record: **angle and moat** (reason to exist, what protects it) · **traffic and ad strategy** (organic vs paid mix, share of voice on head terms, presence by ad type — SP / SB / SBV / product pages) · **trajectory** (what changed when their performance changed: price move, image refresh, review milestone, stock-out). [LTSF, B6]
- Conclude with a **gap list**, each item classed **Product** (needs specification investment) / **Offer** (positioning, price, messaging) / **Execution** (content quality), plus a **defensibility note**: how fast could the incumbent close it if we exploit it? [LTSF]

---

## 4. Offer and price positioning

Price position among tracked competitors is a **required input before calling a CVR gap fixable by PPC**. Price and offer gaps go to Brand Management, not to bids. [PB]

| Dimension | Read | Thresholds / rules in sources |
|---|---|---|
| **Price ladder** | Every mapped rival's price by size; our rank on the ladder; category median; SQP market price vs brand price (`05` §8) | Cold ranking candidate needs price ≤ ~1.25 × category median [PB] |
| **Value per unit** | Price ÷ pieces (or per unit of the product's natural measure) | Used for offensive ASIN targets: rival above us on price for fewer pieces [B6 R-CI7] |
| **Pieces / bundle** | Set contents vs rivals (e.g. 4-pc vs 6-pc) | Name the comparison unit |
| **Rating** | Star rating vs top-5 | Cold candidate: ≤ ~0.3★ below top-5 [PB] |
| **Review count and velocity** | Count vs top-5 median; reviews gained per month (trend) | Cold candidate: ≥ ~50% of top-5 median count [PB]; offensive ASIN: same price with < 50% of our reviews [B6 R-CI7] |
| **Variation breadth** | Sizes × colours offered vs rivals; missing cells | Range gaps → §6 |
| **Claims** | Material, certifications, benefit claims (cooling, deep pocket…) vs what the listing proves | Claims must match the SKU and be policy-safe |
| **Discounts / coupons** | Rival list vs sale price, coupons, deals running | Rival price cut > 15%, new discount or traffic growth > 50% in a push term's top 10 → hold our price 3 days before reading a CVR drop as a bid problem [B6 R-CI11] |

How to read positioning against the set:
1. Place us per rival tier (Aspirational / Beatable / Poor, `08`) — winning on price against an Aspirational rival means something different from winning against a Poor one. [B6]
2. **Win ≥ 2 of 3 (price, rating, review count)** vs a target → conquest entry is open; the same test answers "is a rival's win explaining our rank loss?" State it plainly: "we win on price and reviews, lose on rating — two of three". [PB]
3. Check whether the field is our product at all: a generic field of lower-priced substitutes means our CVR cannot carry our price there — decline, don't push. Example (B6): generic "sheets" terms were led by $15–$50 microfiber sets; a $72 bamboo set could not convert there at break-even. [B6]
4. **State coverage on every competitor claim** ("13 of 32 mapped rivals measured"); unmeasured is unknown, not absent. [B6 R-CI12]
5. **Withdraw overturned findings** into the register with the overturning evidence. Example (B6 source): "2.71× market price, OUTPRICED" was withdrawn after a 74-ASIN pull put the median at $79.99 and ours at 1.00–1.06×. [DR]
6. Competitor price data never sets our bid; prices stay break-even-based. [B6 R-CI4]

---

## 5. Conversion diagnostics

Separate offer, visibility, stock and event causes **before** any bid change.

| Signature | Diagnosis | Route |
|---|---|---|
| **Rank holds, CVR falls** | Offer problem | Listing / price / reviews → Brand Management; no bid increase [LTSF] |
| **Rank falls, CVR steady** | Visibility problem | Placement / delivery (`07`); check competitor moves [LTSF] |
| **Rank collapse concentrated in one size or colour family, coinciding with an outage** | **Stock signature** — not demand, not relevance | Inventory (`04`); do not attribute to the listing [LTSF] |
| CVR drop coinciding with a logged price increase | Price attribution | Hold bids; revert the price, or accept it and recompute break-even, ceilings and targets first [PB] |
| AOV shift from a variation-mix change | Economics changed | Every verdict on the old AOV is void; re-run the rows [PB] |
| CVR ≥ benchmark, rank falling, no own event | Competitive shock | Check new entrant / deal / price cut; one ladder step within ceiling; re-read in 1 week; log [PB] |
| Branded-term CVR collapse | Listing health | Check suppression, buy-box loss, review-score drop, variation break — almost always a listing finding, not a bid problem [PB] |
| Deal days in the window | Distorted | No CVR verdict on deal data; separate deal-state baseline; 2-week guard after the deal [PB, B6 E1] |

**Rank lost > 10 places despite delivery** (rank-drop freeze): no price moves; investigate in order — anchor the timing → own listing first (price, stock-out, reviews, content, coupon/deal ending → Brand Management) → competitor wins ≥ 2 of price / rating / reviews, or competitor went OOS (name it; route to conquest) → isolated vs category-wide (escalate if category-wide) → none found: "investigated, no cause identified" and ask. **Never a bid increase on a collapsing term.** [PB, B6 E4]

Quality gate at the delivering placement (decision order step 8): price, stock-out, rating/reviews, content, deal ending — any of these explains the row → Brand Management finding, no bid. [PB]

---

## 6. Brand Management findings register

Every non-PPC cause found in Phases 3–5 goes here — not into a bid. One row per finding.

| Column | Content |
|---|---|
| # / Category | **Price · Listing · Returns · Range gaps · Inventory / PO · Competitor advantage** |
| Finding | One sentence, with the real figure |
| Evidence | Numbers, source, window, date (quadrant, CVR vs market, rank arc, competitor comparison, SQP ratio) |
| Why it matters | Mechanism: profit, rank, velocity, inventory, share |
| Recommendation | Exact change (e.g. "move 'cooling' into the first 80 characters"; "reorder Full White") |
| Owner | Brand Management / Listing & creative / Supply chain / PPC (for coordination only) |
| PPC decisions gated | Which keyword or campaign decisions wait on it (e.g. WAIT on two push terms) |
| Expected effect | Magnitude-appropriate, labelled measured or estimated |
| Due / re-read date · Status | Open / in progress / shipped / withdrawn (with overturning evidence) |

[PB, LTSF, DR]

What triggers each category:
- **Price** — price above ~1.25 × category median on a ranking candidate; CVR drop after a price change; rivals discounting in a push term's top 10; deal-state margin too thin for the ceiling.
- **Listing** — CONVERSION or BOTH-FAILING syntax; SQP CTR or CVR < market on ≥ 30 clicks (listing flag → push WAIT); TOS IS > 30% with CTR failing; element scores below rivals; copy defects; ranking term backend-only.
- **Returns** — return / defect signal (e.g. a Structurally-dead archetype); branded CVR collapse traced to reviews.
- **Range gaps** — demand without a SKU; low-demand variations holding aged units.
- **Inventory / PO** — projected days of cover leaving Green because of a push (name SKU, date, the push causing it: fix = expedite, PO date, safety stock); stock signature on rank. [PB]
- **Competitor advantage** — a rival wins ≥ 2 of price / rating / reviews on our head terms; rival video/SB presence where we have none; rivals conquesting our brand terms.

Order the register by expected effect, not ease; mark **zero-cost items** (backend terms, variation ordering, A+ module changes) to execute now regardless of what else is agreed. [LTSF]

Example (B6): "bamboo sheets king size" and "bamboo sheets king" were held at WAIT — SQP showed conversion 0.68× / 0.81× and click-through 0.55× / 0.42× the market; the listing check on King White was logged as a Brand Management item gating both pushes.

---

## 7. Review themes — manual read method

Review themes are **not in any connected data source**. Either read them manually or use an external review tool; label the result "manual read" with its coverage. [13 §4]

Method:
1. **Scope:** our listing (per size/colour family where reviews are split) and the same top 5–8 true competitors as §3. Sample size and recency window: No source rule; decide and record (state N per listing and the date range).
2. **Capture per listing:** star distribution; review count and monthly velocity; top recurring **positive** themes (the drivers shoppers name); top recurring **negative** themes (objections: fit / sizing, material feel, durability / pilling, colour accuracy vs images, set contents, smell, shrinkage — adapt per category); claims that reviews confirm or contradict; reasons given for returns; review photos that show a mismatch with the main image.
3. **Count, don't quote:** record each theme as mentions ÷ reviews read, with one short example.
4. **Map each theme** to a listing element (objection → gallery "objection kill" image, bullet, A+ comparison) and to the quadrant it explains (negative themes on a CONVERSION syntax are the first place to look).
5. **Compare:** our negative themes that rivals do not share = offer/product gaps; rivals' negative themes we avoid = claims to promote (defensibility note, §3).
6. File every actionable theme in the register (§6) with evidence and owner.

---

## 8. Open questions for the owner

1. **Syntax CVR target.** Resolution #20 sets syntax CVR target = Market × 1.10 (quick-audit), while one source (SR) compares syntax to the sheet's keyword-style targets (CVR × 3.0). This file uses × 1.10 at syntax level and × 3.0 at keyword level; confirm.
2. **Review-read sample.** No source defines how many reviews or which window to read; set a house default.
