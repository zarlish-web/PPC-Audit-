# 08 — Competitor and market analysis

Phase 3 (market and competitors) and Phase 8 (competitor influence, gaps, ASIN targets). Competitor data decides **which terms, in which order, which pages, and how progress is judged**. It never sets a price: every price stays break-even-based (break-even CPC, ceiling, push price, TOS price = base × (1 + boost)).

## Contents
1. Data pulls, in order (what each gives, limits, coverage rule)
2. Roster, tiers, scoreboard, traffic trend
3. Per-rival profile checklist
4. Market view
5. Keyword landscape join
6. Engine-vs-landscape verdicts and first milestones
7. Competitor ASIN targeting (OFFENSIVE / TEST / AVOID / LOW TRAFFIC), conquest entry and exit
8. Competitor → engine influence rules R-CI1–R-CI12
9. Gap analysis (template, gap families, size battlegrounds, seed list)
10. Sponsored Brands / video test design
11. Limits (what no connected source gives)
12. Outputs and checks
13. Open questions for the owner

Thresholds tagged [B6] were set on one market (bamboo sheets, ASINsight 7-day traffic units). They are the defaults. For a much smaller or larger market the owner may rescale them — ask, and record the answer.

---

## 1. Data pulls, in order

Pull everything before you write a finding. Date every pull. Store raw JSON or exports beside the workbook.

### 1.1 Pull sequence

| # | Source / call | What it gives | Limits / traps |
|---|---|---|---|
| 1 | Command Center `traffic_products` → `traffic_competitors` | Our product id. Mapped roster: parent ASIN, brand, marketplace, **mapping tier** (Aspirational / Beatable / Poor), keyword count, 7-day traffic, import date | No export → traffic null. That means **unmeasured**, not zero [B6] |
| 2 | `traffic_market` | Roster state per rival (loaded / unmeasured / undated), coverage (loaded of mapped), tracked traffic, **our share of tracked traffic**, freshness spread | Compare exports only when the spread is ≤ 2 days ("comparable"). Totals describe the loaded rivals, not the category [B6] |
| 3 | `traffic_history` | Our traffic and keyword count per snapshot. The same per rival. Contested/won per rival snapshot. Roster joins and leaves | A rival snapshot is compared with our nearest snapshot on or before it. A tie is not a win |
| 4 | `traffic_market_keywords` — first page with `summary=true`, then **every addressable page** (`addressability=addressable`, `limit=200`, `summary=false`) until exhausted | Per keyword: consensus (rivals present), tracked traffic and ad traffic, ours, state (contested / ours_only / theirs_only), leader, addressability, segment, relevancy, weekly SV, opportunity (`we_run_none` / `they_are_more_aggressive`), ad gap, `rivalMetrics` per rival (traffic, ad traffic, organic rank, SP rank, placements). Summary blocks: scoreboard, segment gap, segment × tier grid, placement reach, PPC opportunities, byConsensus | Pull **all** addressable rows, not the top page. The biggest market pages are generic terms. Basis defaults to market average (avg); state the basis you used. 7-day traffic is impression-like: **not clicks, not sales** |
| 5 | `traffic_competitor` per loaded rival (comparison rows; `state=theirs_only` pages) | Rival totals, organic % / paid %, top-10 keyword share, top keyword. Segments (owned / matched-no-owner / unclassified). Relevancy mix. Placement reach per code. **Hero ASINs** (the fewest child ASINs carrying 80% of its traffic). Contested (we win / we lose / our zero-traffic), ours-only, theirs-only (keywords, their traffic), PPC openings, our share. Also **our** hero ASINs | Theirs-only rows page at 100. Page through them, or state that you sampled |
| 6 | `traffic_position_trends` (rival hero ASINs + `our_asins`) | Daily placement **scores** per child: organic, SP, SB, SB video, summary organic, summary advertising | **Scores, not traffic.** Never add them to 7-day traffic. The feed was retired and the series ends at a fixed date. The response states the newest day, so quote it. ASINs with no rows are listed as missing; say which |
| 7 | `traffic_addressability` | Addressable / disqualified / unknown keywords with traffic. Disqualified split by reason (disqualifier term, other brand, size not sold, fit tag). Share nothing classifies. Conflicts (a disqualifier and a fit tag disagree) | Review the conflict rows by hand before you use them in a gap list |
| 8 | `traffic_our_keywords` | Our export: 7-day traffic, organic/ad split, organic and SP rank and page, SV, SFR, top-3 click/conversion share, variations reached | Our ranks here are one week. Rank history comes from the rank source (ref 05) |
| 9 | Data Dive: `list_niches` → `get_niche_competitors` per niche (`create_niche_dive` / `create_niche_dive_from_competitors_list` if missing — these spend tokens, so confirm first). Optional: `get_niche_keywords`, `get_niche_roots`, `get_ranking_juice` | Per listing: price, est. units/30 d, est. revenue/30 d, BSR, rating, reviews, listing date, variations, page-1 keyword coverage (count and % of niche SV), advertised keywords, top-of-search keywords and SV, fulfilment, seller country. Per niche: keyword count, SV, median price / reviews / units, launch keywords | **Pull several niches:** (a) the broad size or category niche, all materials — this shows who owns the generic field and at what price; (b) the material / type niche for our product; (c) a size-specific material niche. Units and revenue are **estimates**. Ad detection sees only some sellers, so "0 advertised keywords" ≠ no ads |
| 10 | Command Center product brief — competitors section | Per mapped brand (all mapped, measured or not): price first → latest (Δ%), BSR first → latest, review count and Δ, **reviews/week**, discount now (depth %). Summary: on discount now, price cutters, price raisers | About 32 days and 6 weekly snapshots. Only strike-through discounts are seen: **coupons and lightning deals are not scraped** |
| 11 | AdInsight per-ASIN files `AdInsight_US_<ASIN>_<start>to<end>.xlsx` (when supplied) | Daily ad traffic score (cumulative on the latest row). Ad keyword count (daily, change rate, Total on the latest row). Ad position traffic ratio and keyword count per ad type (SP / SB / SBV / HR / TRB / CPF / SOR). Top 10 keywords per ad type (rank, keyword, 7-day traffic, ratio, SFR, weekly SV) | Visible keywords ≤ 70 per ASIN (10 × 7 types). "Ad Keyword Count (Total)" is account scale; never report it as the list you can see. `(None…)` sheets mean the ad type is not run. **Files carry no brand**, so resolve it (1.3) [LP] |
| 12 | Helium10 Cerebro (own + multi-ASIN competitor pull) | Keyword × ASIN organic/sponsored ranks, SV. Used for the coverage audit: each relevant term ≥ the volume threshold → **LIVE / PAUSED / MISSING**. Priority list = MISSING terms with **3+ competitors in the top 30** [LTSF] | Cerebro suggested bid / CPC is **never** used to set prices (owner rule, register #18). Cross-check the search-term report before you call a gap: exact-text matching overstates gaps [LTSF] |

When a product has conquest or PAT campaigns, dated competitor pulls (ASINsight / Helium10 / Cerebro) are a **required input** [PB, WB].

### 1.2 Coverage rule (applies to every competitor number)

1. **Profile all mapped competitors** that carry an export, not a sample. Profile the unmeasured ones from the brief and Data Dive.
2. **Unmeasured ≠ zero.** Draw no conclusion about a rival with no export. Report "unmeasured".
3. **State coverage on every share or contest figure**: "13 of 32 mapped competitors measured; figures describe those 13" [B6, R-CI12].
4. **Map the missing big sellers.** List every listing in the Data Dive niches that has high est. units or a low BSR and is **not mapped** (or mapped but unmeasured). Request mapping and an export for each, Beatable ones first. Example (B6): four unmapped sellers, one at BSR 456–691 and ~24k units/month.
5. Set a coverage target for the next audit. Example (B6): ≥ 20 of 32 measured.
6. Count **brands, not ASINs**. Two ASINs of one brand are one competitor in any "N rivals do X" count [LP].
7. Keep no padded competitor sets. A rival has to share our intent, material and category to count [LTSF].

### 1.3 Brand resolution (bare ASINs are rejected) [LP]

Resolve every ASIN to a brand before you present anything. Try in order: `"<ASIN>" amazon` → `site:amazon.com <ASIN>` → add the category words → aggregators (Ubuy, Walmart cross-listings, camelcamelcamel, roundup posts). Use the brand as the primary label and put the ASIN beside it. If a brand stays unresolved, list it as "unresolved". It cannot be scaled as a conquest target (R-X6).

### 1.4 AdInsight reads (per ASIN) [LP]

| Read | Formula / signal | Meaning |
|---|---|---|
| Traffic per keyword | latest ad traffic score ÷ latest Ad Keyword Count (Total) | High = tight, well-converting set. Low = long-tail spray |
| 7-day trend | latest score − earliest score | Call out sharp moves either way |
| Infrastructure mismatch | large keyword count, most ad types active, score ≈ 0 | Recent pull-back. Watch for re-entry; don't dismiss them as small |
| True dormancy | 0 score, 0 keywords, no ad types | Say it plainly |
| Isolated ad type | SBV or HR alone, no SP | Test or awareness play, not a push |

---

## 2. Roster, tiers, scoreboard, traffic trend

### 2.1 Tiers (mapping tier, set in Command Center)

| Tier | How the scoreboard treats it | How this skill uses it |
|---|---|---|
| **Aspirational** | Not beaten → severity *none* (no failure) | Leaders. A target rank held only by Aspirational rivals is a **stretch** (R-CI2). Their pages are usually AVOID or TEST |
| **Beatable** | Not beaten → severity **failure** | The rivals to pass. They set the first milestones and the winnable ground (R-CI3) |
| **Poor** | Beaten → *ok* | They should sit below us. If a Poor rival is ahead, that is a finding |

The tier is a mapping input. No source defines how to assign it. If a rival is untiered, or the evidence contradicts its tier (e.g. a "Poor" rival ahead of us on traffic and contests), raise it with the owner. Never retier silently.

### 2.2 Scoreboard reads (per rival)

| Field | Definition | Read |
|---|---|---|
| Traffic verdict | our 7-day traffic vs theirs | ahead / behind |
| Contest verdict | our wins on the keywords we both hold | ahead when we win most contested keywords (as observed: contest rate > 50%) |
| **Call** | beaten (both ahead) · not_beaten (both behind) · mixed (split) · unmeasured | Headline per rival |
| Severity | failure = Beatable/Poor not beaten · watch = mixed · ok = beaten · none = Aspirational not beaten | Count failures by tier |
| **Contest rate** | contest wins ÷ contested keywords (a tie is not a win) | Share of shared ground we win |
| **Distance** | their traffic ÷ our traffic | > 1 = they are bigger. Example (B6): Aspirational leader 15.0×; a Beatable 3-piece set 1.01× (level) |

The per-segment × tier grid gives the same call per segment. The worst call per segment is the one to act on, and the "push gap" is the Beatable traffic we don't have.

### 2.3 Traffic trend: season or share loss?

1. **Our trend**: our 7-day traffic across all snapshots (`traffic_history`). State the first → last and the Δ%.
2. **Rival trend**: each rival's previous export → latest export, as Δ%.
3. **Hero placement scores**: compare the average of the first 7 days with the average of the last 7 days, for organic and advertising. Report the change only when the first-week score is ≥ 50 (below that it is noise) [B6]. For rivals, sum their top 3 heroes. For us, sum our heroes.
4. **Verdict:**
   - If most rivals fell by a similar amount, the fall is **season**.
   - If our fall is larger than the median rival fall, the gap is **share loss**. Name the child ASIN and the placement (organic vs ad) that lost it.
   - If one rival rose while the field fell, it is a **mover**. Profile it and check the terms where it sits (5.6).
5. Split the read before and during events (deal run-ups lift everyone).

Example (B6): our traffic fell 37% over 7 weeks. Every measured rival but one also fell 7–24% between exports, but our four heroes' organic score fell by more than the rival median. King White (the ranking colour) lost the most, so the verdict was part season and part share loss on the hero.

---

## 3. Per-rival profile checklist

Fill every field for every measured rival. Unmeasured rivals get the fields that the brief and Data Dive can fill. A blank field is written as blank with a reason, never 0.

| # | Field | Source | How |
|---|---|---|---|
| 1 | Brand, parent ASIN, product name, tier, call | roster, scoreboard | brand-resolved |
| 2 | ASINs carrying traffic; **variation structure** (variation count, sizes, colours, packs) | hero list, Data Dive `variations` | |
| 3 | **Hero ASINs** with share of the rival's traffic and the keywords each leads | `traffic_competitor` heroAsins (80% coverage) | top 4 |
| 4 | **Pieces / bundle** (pack size, what's included) | listing title (Data Dive) | parse the piece count and flag "no flat sheet"-type omissions |
| 5 | **Price range** (min–max across listings read) and **price movement** | Data Dive, brief | first → latest (Δ%) |
| 6 | **Discount now** (depth %) | brief | strike-through only |
| 7 | **Units / revenue** (est. 30 d, best-selling listing) and **velocity** | Data Dive | label as estimate; best listing, not the whole brand |
| 8 | **BSR** (lead listing) and **BSR movement** | Data Dive reads on different dates; brief | "12,485 (28 Sep) → 10,390 (29 Sep)" style, dated |
| 9 | **Rating, reviews, review velocity** + method + source | brief (reviews/week over its window) where the brand is a mover. Otherwise two Data Dive reads of the same listing: (latest − first) ÷ days × 7. For a parent family with a shared count, use it only when the two counts differ by ≤ 3% of the base [B6] | name the source. A falling count is a finding (review loss) |
| 10 | **Keyword count and coverage** | export totals; Data Dive page-1 keywords (count, % of niche SV) | |
| 11 | **Organic % vs paid %**, top-10 keywords' share, top keyword (% of their traffic) | `traffic_competitor` totals | |
| 12 | **Top keywords** (their top 8 addressable, with their rank and ours) | `rivalMetrics` join | 5.1 |
| 13 | **Placement behaviour**: keywords with OR / SP / SB / SBV / AC / SOR | placement reach; Data Dive advertised and top-of-search keywords | → PPC behaviour label (3.1) |
| 14 | **Contest vs us**: contested, we win, we lose, our traffic ÷ theirs | comparison | |
| 15 | **Their-only keywords** (count, their traffic, share of theirs) | comparison | |
| 16 | Traffic change export → export; hero organic/ad score change | history, trends | |
| 17 | **Strengths / weaknesses** | rules 3.2 | |
| 18 | **Conquest archetype** (Fortress / Investor / Price Leader / Copier / Fader) | 7.5 | |
| 19 | **What it means for us** (3.3) | synthesis | one paragraph |

### 3.1 PPC behaviour label [B6]

Apply every tag that fires (kw = the rival's keyword count):

| Test | Tag |
|---|---|
| paid % ≥ 60% | ad-led |
| paid % ≤ 20% | organic-led, light ads |
| (SB + SBV keywords) ÷ kw > 0.3 | heavy Sponsored Brands + video (brand funnel) |
| else SBV ÷ kw > 0.3 | video-heavy |
| SP ÷ kw > 0.5 | SP on most keywords |
| SOR ÷ kw > 0.4 | strong product-page ads |
| none | mixed |

Add the AdInsight reads (1.4) when those files exist.

### 3.2 Strength / weakness rules [B6 values; rescale per category with the owner]

| Strength if | Weakness if |
|---|---|
| reviews > 10,000 | reviews < 1,000 |
| organic > 60% of traffic | paid > 60% of traffic (share falls when spend stops) |
| SB + SBV keywords > 1,000 | keyword count < 1,500 (narrow) |
| keyword count > 4,000 | price > our same-size price + $15 for fewer pieces |
| traffic Δ > +30% since previous export | traffic Δ < −15% |
| price < our price − $5 | rating ≤ 4.3 |
| variations > 150 | review count falling |
| rating ≥ 4.5 | fewer pieces than ours (e.g. 3-piece, missing component) |
| hero organic score > +25% | hero organic score < −25% |

Always compare against **our same-size, same-variation** listing (the advertised hero), never a blended parent.

### 3.3 "What it means for us" — write every paragraph to this pattern

1. The price and value position vs us: price, pieces, value per piece, reviews, rating.
2. Where they beat us: which terms, and at what rank.
3. Do they bound any of our targets? Say whether they make a target a stretch or show that it is reachable.
4. Their pages: OFFENSIVE / TEST / AVOID (section 7), and why.
5. What to watch: a price move, a discount, a traffic surge, an ad pull-back.

Example (B6): "Fastest-growing rival (+123% traffic): new 4-piece at our price with a tenth of our reviews, now #6–#11 on King terms. OFFENSIVE target; passing it is the first milestone on King terms."

---

## 4. Market view

Report each block with its coverage and its date.

| Block | Contents | Source |
|---|---|---|
| Tracked market | keywords, 7-day traffic, our traffic, **our share of tracked** | `traffic_market` totals |
| Addressable | keywords, traffic, our traffic, our share | addressability |
| Disqualified | keywords, traffic, split by reason (disqualifier term / other brand / size not sold / fit tag) | addressability |
| Unknown | keywords, traffic, % of traffic nothing classifies | addressability |
| **Contested** | keywords, market traffic, ours, we win / we lose, keywords where we have zero traffic | `contested` |
| **Theirs only** | keywords, traffic, share of tracked | `theirsOnly` |
| **Ours only** | keywords, our traffic | `oursOnly` |
| By consensus | keywords and traffic by the number of rivals present; where we are absent | `byConsensus` |
| PPC opportunities | `we_run_none` and `they_are_more_aggressive`: keywords, ad gap, all vs addressable | `ppcOpportunities` |
| **By kind (addressable only)** | per kind (5.2): keywords, traffic, ours, our share; "they advertise, we don't" (kw / traffic); "they out-advertise us" (kw / traffic) | keyword join |
| **Segment gaps + tier grid** | per segment: keywords, traffic, paid share, our traffic / share, keywords we are absent from, wins vs Beatable (of contested), wins vs Aspirational, worst call | `segmentGap`, `segmentTierGrid` |
| **Placement reach comparison** | us and each rival: keywords with OR / SP / SB / SBV / AC / SOR + behaviour label | `placementReach` + profiles |
| **Price ladder** | every relevant listing across the niches (latest read per ASIN): brand, ASIN, price, pieces, **$ per piece**, est. units, est. revenue, BSR, rating, reviews, variations, listed date, page-1 keywords, read date; sorted by price | Data Dive |
| **Niche benchmarks** | per niche: keywords, SV, median price, median reviews, median units, launch keywords, date | Data Dive |
| Offer vs field | our price, pieces, reviews, rating vs niche medians and vs each tier | derived |

**Offer checks carried into refs 06 and 09.**
- Price position among the tracked competitors is a **required standing input** before a CVR gap can be called PPC-fixable. Price and offer gaps go to Brand Management [PB].
- WB's cold-term parity reference for a new ranking term: reviews ≥ 50% of the top-5 median, rating within 0.3★, price ≤ 1.25× median [WB]. Report it; the push gates themselves live in ref 06.

**Where we win / where they win / where no one is strong.** End Phase 3 with three lists: kinds and segments where we lead; where Aspirational or Beatable rivals lead, with the size of the gap; and where the paid share is low and no tracked rival ranks in the top 10 (open ground).

Example (B6): "13 of 32 measured. We hold 2.1% of tracked traffic, and on 1,899 contested keywords we win 11 and lose 1,660. On core-material terms we advertise on almost all of them, so the gap there is ad intensity, not coverage. Cooling wording is the uncovered segment. Generic head terms are led by $15–50 microfiber sets."

---

## 5. Keyword landscape join

Join every market keyword (all addressable pages) with our keyword decisions (ref 05/06), the live owners (bulk / campaign targets) and the search-term report.

### 5.1 Field metrics per keyword

| Column | Definition |
|---|---|
| Kind, size | 5.2. Size by token (Cal King before King; Full = double) |
| Segment, relevancy, addressable | from the market pull |
| Weekly SV, market traffic, market paid share, rivals present (of N measured), traffic leader | market pull |
| **Best rival organic** | lowest organic rank among rivals, with its name and tier |
| **Best rival SP** | lowest SP rank, with its name |
| **Beatable rivals in organic top 10** | names and ranks |
| Aspirational in top 5 | names and ranks |
| **Rivals advertising** | rivals with an SP rank; separately, how many sit at SP #1–5 |
| **Rivals with brand banners** | rivals with SB or SBV among their placements |
| Top-3 rivals by traffic | names, traffic |
| **Our position** | our traffic, share, organic rank, SP rank, placements, paid share |
| Opportunity, ad gap | market pull |
| Our decision and evidence | decision, clicks / orders / ACoS 30 d, TOS CVR, owner campaign(s) — or "no search-term row" |
| Position class, landscape verdict, why, notes | 5.3, 6 |

Notes to add: "N rivals run SB/video on it — a banner sits above our top-of-search slot" when ≥ 3 rivals have banners; "rivals out-advertise us (their ad share X%, ours Y%)" when the opportunity is `they_are_more_aggressive` [B6].

### 5.2 Kinds (classify by tokens, first match wins) [B6, generalised]

| Kind | Definition | Example (B6) |
|---|---|---|
| Brand (own) | contains our brand | "decolure bamboo sheets" |
| Core | contains the product's defining material or type | bamboo / viscose / rayon |
| Benefit | the listing's main benefit wording, without the core word | cooling, hot sleepers, night sweats, breathable, moisture wicking |
| Pack match | our pack configuration | "6 piece", "six piece" |
| Generic — attribute | attributes that don't define our product | silk, satin, luxury, hotel, soft, deep pocket, organic |
| Generic | category head terms | "bed sheets", "king sheets" |

Competitor-brand, language, colour and other-product classes come from ref 05. Competitor-brand terms are evaluate-only (trademark risk) unless a conquest keyword already runs on that brand, in which case it is a "confirmed live tactic" [LP]. Spanish and other-language terms are usually uncontested, so read low volume as low volume, not as irrelevance [LP].

### 5.3 Position classes (first match wins) [B6]

| Class | Test |
|---|---|
| **Absent — they own it** | we have no traffic and no organic rank |
| **We lead** | our organic ≤ the best rival's organic (or no rival ranks organically) |
| **Direct fight** | our organic ≤ 20, or our SP ≤ 5 |
| **Within reach** | our organic ≤ 60 and ≥ 1 Beatable rival in the organic top 10 |
| **Within reach — Aspirational-led** | our organic ≤ 60, no Beatable rival in the top 10 |
| **Competitor advantage** | everything else |

### 5.4 High-value keywords

Revenue per keyword is **not available** from any connected source. Use the proxy **market traffic × weekly SV** to rank keywords within a kind, and label it as a proxy. Sort landscape tables by market traffic.

### 5.5 Data artifacts [LP]

A term with a weekly SV that is implausible for its SFR, or an identical, oddly specific SV repeated across several rivals' files, is a scrape artifact. Flag it, ask for it to be verified in the source tool, and **exclude it from totals**.

### 5.6 Rising-rival exposure (proxy)

Keyword-level history does not exist (each export is one week). Instead:
1. Take the rivals that are rising: traffic Δ > +50% (R-CI11), hero ad or organic score > +25%, or a mover in the brief.
2. List the core and benefit keywords where such a rival sits in the organic top 10 or the SP top 3 **and ranks ahead of us**.
3. Sort by market traffic.
4. Label the list "rival-level movement × current rank, not keyword history" [B6].

---

## 6. Engine-vs-landscape verdicts

Give every keyword decision that appears in the market pull a landscape verdict, and give every addressable keyword without one a gap verdict. The verdict **changes ordering, judging and gap-filling — never a price** (R-CI4).

### 6.1 Terms we have a decision on

| Decision | Test (in order) | Verdict |
|---|---|---|
| PUSH / WAIT / HOLD RANK | our organic ≤ best rival organic | **AGREES — we lead the tracked field** (the push is against untracked sellers; cap it to the stock plan) |
| | a rival sits at or above the target rank, and at least one of them is not Aspirational | **AGREES — reachable** (proof that a listing like ours can hold the target; name the rivals to pass first) |
| | every rival at or above the target is Aspirational | **AGREES — stretch target** (judge progress on the Beatable rivals passed, R-CI2) |
| | Beatable rivals hold the ranks between us and the target | **AGREES** — winnable ground (fund first, R-CI3) |
| | otherwise | AGREES (state the field) |
| DEFEND | rivals advertise on our brand term | **AGREES — defence needed** (state the rival count, the market ad share and our organic rank) |
| REDUCE | the term sells (≥ 10 orders in 90 d) and rivals buy it | **AGREES — keep live at break-even** (the cut is a price cut to break-even, never a block — R-CI9) |
| BLOCK / REDUCE | addressable, market traffic ≥ 10,000, ≥ 5 rivals advertise | **CHALLENGE — re-test later**: the cut stands (the money rule wins on the day), tagged re-test (R-CI9) |
| BLOCK / REDUCE | otherwise | AGREES (thin or low-value field) |
| MONITOR | addressable, market traffic ≥ 20,000, core or benefit kind | **CHALLENGE — under-funded**: give it an exact owner in discovery at break-even, no push premium, so it can be read |
| MONITOR | generic kind | AGREES (the field is priced for another product tier) |
| CHECK OWNER / DEDUPLICATE | — | **AGREES — fix owner first** (one live owner before any push) |
| HARVEST | — | AGREES (a real market term; give it an exact owner) |

### 6.2 Addressable terms with no search-term row (the engine is blind to them)

| Test (in order) | Verdict |
|---|---|
| not addressable | **Out of scope** |
| core kind, market traffic ≥ 3,000 | **GAP — engine blind**: seed an exact owner at break-even (R-CI8) |
| generic kind | **GAP — leave**: discovery only |
| benefit or pack kind, market traffic ≥ 3,000 | **GAP — engine blind** |
| generic-attribute kind, relevancy Highly Relevant / Relevant, market traffic ≥ 5,000 | **GAP — test**: discovery at break-even before any owner |
| generic-attribute kind, otherwise | **GAP — leave** |
| any kind, market traffic ≥ 5,000 | **GAP — engine blind** |
| otherwise | GAP — small: leave to auto/broad discovery |

Traffic thresholds are [B6] (ASINsight 7-day units).

### 6.3 First milestone (every push, waiting and at-target term)

- **First milestone** = the closest Beatable or Poor rival ranked **ahead of us** organically (the rival with the highest rank number still below ours).
- If only Aspirational rivals are ahead, write "none — only Aspirational rivals ahead".
- If no tracked rival is ahead, write "we lead the tracked field".
- Report progress at 7 and 14 days as **rivals passed**, alongside the distance to the target. A slow climb past Beatable rivals is not a failure at day 7 (R-CI2, R-CI5).
- If winnable-ground terms don't move in 7 days at the push price, the cause is ours (listing, colour, conversion), not the field.

Example (B6): on "bamboo sheets" the target #9 was held only by two Aspirational rivals, so the term was a stretch, and the first milestone was the Beatable rival sitting just above our #30. On King terms, a Beatable rival launched within the year already held #6–7, so those targets were reachable.

### 6.4 Summary outputs

- Pivot of decision × verdict, with counts.
- The share of our terms that appear in the market pull, and why the rest don't (ASIN targets, misspellings, colour terms, terms too small).
- Campaign-level checks, one row per campaign family:

| Campaign family | Checks |
|---|---|
| Ranking | fields, banners, stretch vs winnable |
| Waiting (ceiling below cost) | "keep the block; the owner decides a ceiling raise" |
| Brand DEFEND | rivals on our brand; add own-ASIN defence |
| Discovery | missing benefit and engine-blind terms |
| Conquest PAT | how much spend sits on AVOID vs OFFENSIVE pages; own ASINs mixed in |
| SB / video | presence vs rivals |
| Generic MONITOR | whether the field supports leaving it there |

---

## 7. Competitor ASIN targeting

### 7.1 Candidate set

Include every rival hero ASIN, every relevant-material listing in the Data Dive niches, the extra ASINs read, and every ASIN already targeted in our campaigns. Classify each candidate first [B6 R-X1/X2]:

| Class | Treatment |
|---|---|
| Own product (this family) | defence (DEFEND, low bid, judged ACoS ≤ break-even). Never conquest |
| Own brand, other product | cross-sell, judged on its own ACoS. Report it apart from conquest |
| Competitor, same material | 7.2 |
| Competitor, other material | 7.2 (usually AVOID) |
| Unmapped (brand unknown) | no SCALE until mapped (R-X6) |

### 7.2 Class tests (first match wins) [B6]

Compare against **our same-size advertised listing** (size read from the target's title; default = our main size): our price P, our rating R, our reviews N.

| # | Test | Class |
|---|---|---|
| 1 | est. units on that listing < **500/month** | **LOW TRAFFIC — skip** (too few shoppers on the page) |
| 2 | different material (e.g. microfiber / cotton / satin with no core-material word) | **AVOID — different material** |
| 3 | no price available (even after the family fallback, 7.3) | **TEST — no price read** |
| 4 | (price < 0.85 × P **and** reviews > N) **or** (price < P **and** reviews > 5 × N) | **AVOID — cheaper and better reviewed** |
| 5 | price < 0.70 × P | **AVOID — price gap too wide** |
| 6 | price ≥ 1.10 × P **and** rating ≤ R + 0.1 | **OFFENSIVE — we are cheaper** (state pieces: "for 6 pieces vs their 4") |
| 7 | reviews < 0.5 × N **and** price ≥ 0.90 × P | **OFFENSIVE — more reviews at the same price** |
| 8 | otherwise | **TEST — close match** |

Pieces and value per piece are stated in the "why" of every class. No source weights pieces inside the tests beyond R-CI7's wording ("above us on price for fewer pieces"). If pieces should change a class, that is an owner decision; record it.

### 7.3 Family-price fallback

If the listing has no price read, use the rival family's lowest price, its rating and its largest review count, and append "(family price/reviews)" to the why [B6].

### 7.4 Actions by class (targets that already exist keep their money rules)

| Class | Not targeted | Already targeted |
|---|---|---|
| OFFENSIVE | add to the conquest campaign at break-even | keep; judge by R-X3–X5 |
| TEST | optional test after the OFFENSIVE set | keep; judge after 15 clicks |
| AVOID | don't target; negate if auto/PAT finds it | ≥ 3 orders: **hold at break-even while it sells, never scale**. Otherwise remove / negate |
| LOW TRAFFIC | leave | keep only if it sells; judge after 15 clicks |

**Money on an existing target is decided by R-X3–X5 on its own 90-day clicks and orders, summed across every campaign that targets it** [B6]. The class never cuts a profitable target.

| Rule | Test | Action |
|---|---|---|
| R-X3 | mapped competitor, ≥ 15 clicks, ACoS ≤ break-even | SCALE: bid up ≤ +25% per cycle (register #5; B6 used ≤ 30% a step), never above the break-even CPC |
| R-X4 | ACoS > break-even on ≥ 15 clicks | REDUCE toward break-even (gradual cut ≤ 15%/cycle; a decisive cut ≤ 50%) |
| R-X5 | ≥ 20 clicks, 0 orders; or ACoS > 2 × break-even on ≥ 30 clicks | BLOCK (pause the target / negative ASIN) |
| R-X6 | same ASIN in > 1 campaign, or brand not mapped | one owner; no SCALE until mapped |

Product targets use the 11-click floor for a verdict (SKILL sample floors) and 15 clicks for R-X3/X4.

Example (B6): a microfiber page at $24.99 sat at 21% ACoS in one campaign. It is AVOID by class, yet kept at break-even and not scaled. Most conquest spend sat on AVOID pages while no OFFENSIVE page was targeted, so the campaign-level check was **CHALLENGE — shift new conquest to OFFENSIVE ASINs**.

### 7.5 Conquest entry, ceiling and exit [PB, provisional — confirm with the owner before it first drives a decision]

1. **Already targeted?** Search the account for the ASIN in any conquest campaign first. If it is there, decide from its state and performance (reactivate / adjust / leave). Only new targets go through the gate.
2. **Entry gate**: our routed SKU wins **≥ 2 of 3** (price, rating, review count) against the target, **or** the target is out of stock. Write it plainly: "we win on price and reviews, lose on rating — two of three." If data is missing, ask before logging a wait. Default here: a **new** target needs OFFENSIVE **and** 2-of-3. An OFFENSIVE ASIN that fails 2-of-3 is run as TEST. See Open questions.
3. **Ceiling (watch-CPA)** = the lower of: (a) routed SKU margin × CVR, i.e. the break-even CPC; (b) a price-gap-adjusted figure. State which governs. No source sizes the adjustment, so decide and record it. Either way it never goes above the break-even CPC (non-ranking ceiling, register #3).
4. **AOV** = the routed SKU's AOV, never the competitor's price.
5. **Share of target page** = impression or click share on that detail page from PT placement data. Never infer it from account ratios.
6. **Exit / rotate**: the target is delisted (drop it); it no longer loses 2-of-3 to us (hold); or CPA > watch-CPA for **2 consecutive reads** (2 validated weeks, SR) with no page-share gain (exit). Flag CPC > 1.5 × the family median.
7. **Archetypes** change watch-CPA, duration and review cadence, never entry:

| Archetype | Signal | Play |
|---|---|---|
| Fortress | deep review / IP moat | long, expensive game; size accordingly |
| Investor | spends heavily to buy position (ad-led) | spend-war risk; watch for them to stop funding |
| Price Leader | position is price | compete on relevance and proof, not price |
| Copier | newer entrant mimicking an established listing | often the easiest, time-limited win |
| Fader | reviews, rating or rank velocity declining | take it now |

8. **Rank-loss check (ranking state E)**: if a push term lost > 10 places while getting clicks, work through the causes in order. Own listing first (price, stock, reviews, content, coupon or deal end). Then competitor: a rival that wins ≥ 2 of 3 on price, rating and reviews, or a rival stock-out → name it and route to conquest/PAT. Then isolated vs category-wide. Never answer with a bid change [PB].

---

## 8. Competitor → engine influence rules R-CI1–R-CI12

Status: **Standing** = always applies · **Default** = applies unless the owner rules otherwise (B6 proposed it; confirm per product) · **Owner decision** = needs explicit approval per product.

| Rule | Area | Competitor signal | IF → THEN | Never changes | Example (B6) | Status |
|---|---|---|---|---|---|---|
| R-CI1 | Keyword selection | addressability, rivals present, organic field by tier | A term is a push candidate only if it is **addressable**, ranked on by **a majority of measured rivals** (B6: ≥ 7 of 13), and is core or benefit wording. | Generic terms never enter the push, whatever their volume | "bed sheets" (155k traffic) stays MONITOR; "bamboo sheets" qualifies | Default |
| R-CI2 | Ranking strategy | organic ranks of tracked rivals, by tier | If only Aspirational rivals sit at or above the target, the target is a **stretch**. Judge progress on rivals passed (first milestone). After **14 days at the ceiling with no rival passed**, take it to the owner. | Price rules; no automatic ceiling raise | "bamboo sheets" target #9 held only by 2 Aspirational rivals | Default |
| R-CI3 | Push order | Beatable rivals between us and the target | When plan budget exceeds room, fund **winnable-ground** terms first and stretch terms second. | Total push budget; scale factor | King and Full core terms before the Queen head term | Default |
| R-CI4 | Bids | — | Competitor data never sets a bid or price. Push price = break-even × (1 + premium), capped at 2 × break-even. | No competitor CPC, no suggested bid, no "market price" | — | Standing |
| R-CI5 | Read windows | rivals with brand banners; rivals at SP #1–5 | On push terms with **≥ 5 rivals at SP #1–5**, judge rank after **7 days** (not 3). Top-of-search impression share alone is not a pass/fail signal. | The +30%/day step and the ceiling still apply daily | all 13 funded terms had 5–9 banners | Default |
| R-CI6 | Defence | rivals advertising on our brand terms; our organic rank there | Brand terms with **≥ 3 rivals advertising** → DEFEND at top of search, funded first, plus own-ASIN product targeting. | Brand campaigns are judged at break-even like any other (defensive allowance per 7.5 / ref 06 only with verified presence) | "decolure bamboo sheets": 10 rivals, our organic #9 | Default |
| R-CI7 | Offence | price, pieces, rating, reviews vs our same-size set | Target **OFFENSIVE** ASINs only (above us on price for fewer pieces, or the same price with < 50% of our reviews). Negate **AVOID** ASINs in auto/PAT. | Each ASIN is judged by R-X3–X5 after 15 clicks | 4 rival heroes OFFENSIVE; 3 AVOID | Default |
| R-CI8 | Gap seeding | `we_run_none` / no search-term row on addressable core and benefit terms | Addressable core or benefit terms with **≥ 3,000 market traffic** and no search-term row get an **Exact target in the discovery campaign of their size, at break-even**. | No push premium; discovery colour rules; judged by keyword rules after 15 clicks | cooling list; engine-blind core terms | Default |
| R-CI9 | Block review | rivals advertising on a term we BLOCK or REDUCE | A REDUCE on a term that still sells (**≥ 10 orders / 90 d**) and that rivals buy is a price cut to break-even, **never a block**. A BLOCK on an addressable term with **≥ 10,000 market traffic** that **≥ 5 rivals** advertise on stands, tagged "re-test": it goes back into discovery at break-even after **30 days** or after a listing or price change. | The money rule always wins on the day | a set term with 61 orders, 29.8% ACoS, 11 rivals advertising → reduce to break-even | Default |
| R-CI10 | Campaign structure | rivals' Sponsored Brands / video reach | SB / video is outside the automated engine: a hand-built test on core push terms and brand terms, with its **own budget line**, priced by the same break-even rules (section 10). | Not written by the engine; excluded from push budgets; **counted in the product spend limit** | us: SB on 4 keywords vs the leader's 3,791 | Owner decision |
| R-CI11 | Competitor moves | brief movers: price cut > 15%, new discount, traffic growth > 50% | If a rival in a push term's top 10 makes such a move, **hold our price for 3 days** instead of reading a conversion drop as a bid problem; re-check after. | Cuts for money (over ceiling) still apply | a rival at +123% traffic; the leader on 19% discount | Default |
| R-CI12 | Measurement | competitor coverage | Report share, contest and "we win" figures with coverage (loaded of mapped). Draw no conclusion about an unmeasured competitor. | — | 13 of 32 measured; big sellers unmapped | Standing |

### 8.1 Where each rule enters the pipeline

| Pipeline stage (SKILL master order / phase) | Competitor input | Rules |
|---|---|---|
| Keyword classing (Phase 4) | addressability, kind, rivals present | R-CI1, R-CI9 |
| Push qualification (step 9, objective loop) | the gates are unchanged; the field read adds ordering and judging | R-CI2, R-CI3, R-CI5 |
| Price and ceiling (steps 3, 10) | **none** | R-CI4 |
| Budgets (step 10) | funding order only | R-CI3 |
| Discovery / harvest | seed list of engine-blind terms | R-CI8 |
| Product targeting | OFFENSIVE / TEST / AVOID class | R-CI7 (+ R-X1–X6) |
| Brand defence | rivals on our brand terms | R-CI6 |
| Quality gate (step 8) — competitor shock | movers | R-CI11 |
| Landscape check (step 11) | verdicts, section 6 | all |
| Validation (Phase 9) | rivals passed, competitor moves | R-CI2, R-CI5, R-CI11 |
| Reporting | coverage | R-CI12 |

Before calling a cut safe, also check **auction density** (the competitor advertised-keyword count on the term) [PB].

---

## 9. Gap analysis

### 9.1 Gap row template (every gap)

| Field | Content |
|---|---|
| # / Gap | short name |
| **Evidence** | the numbers, with coverage and date |
| **Size** | traffic, keywords, ad gap, or orders at stake |
| **Why it matters** | one or two sentences, in money or rank terms |
| **How to fill inside the guardrails** | the action; every fill keeps break-even, the ceiling, the step caps and the spend limit |
| **Rule** | rule id(s), in the workbook only |
| **Validation** | metric, threshold, read date |

### 9.2 Standard gap families (check every one; write "no gap" with evidence when one is clean)

| Family | Detect | Typical fill | Rule |
|---|---|---|---|
| **Brand defence** | rivals advertising on our brand terms; our organic rank on them; market paid share on brand terms | Brand exacts funded at top of search on the hero (DEFEND). Add an own-ASIN product-targeting defence. Brand negatives in generic discovery only after that is live. If a rival sits above our organic slot on our brand SERP: restore one ladder step, add an SB headline on the brand root (+ SBV if none), PAT self-target the ASINs under attack, and review weekly until the attacker drops [PB]. Never chase branded CPC past the ceiling | R-CI6, R-X1, R-K8, E10 |
| **SB / video lane** | our SB/SBV keyword reach vs rivals; banners on push terms | section 10 test | R-CI10 |
| **Core ad intensity** | `they_are_more_aggressive` on core terms (keywords, traffic, ad gap) | no new rule: the push list is the fill; competitor data orders it (winnable first) | R-P*, R-CI1–3 |
| **Benefit wording** | benefit kind: our share vs traffic; `we_run_none` count | Exact in the discovery campaign of each size at break-even, no premium. Check the listing states the benefit first | R-CI8 |
| **Engine-blind terms** | addressable, ≥ 3,000 traffic, no search-term row | seed list (9.4). If an owner exists but gets no traffic, check it is live and bid at break-even rather than building new | R-CI8 |
| **Protect leads with thin stock** | position "We lead" on terms whose advertised variation is Yellow/Red or short of the next arrival | keep push budgets to the stock plan; reorder; don't hand the ranking campaign to the backup colour | inventory rules (ref 04) |
| **Stretch head terms** | push terms with verdict "stretch" | no price change; report the first milestone; at 14 days at the ceiling with no rival passed → owner: a time-limited ceiling raise or step back to break-even | R-CI2 |
| **Competitor pages** | OFFENSIVE ASINs not targeted; spend on AVOID pages | OFFENSIVE into conquest at break-even; AVOID never targeted | R-CI7, R-X* |
| **Generic terms (deliberately not filled)** | generic kind: traffic, `we_run_none` | Leave to auto/broad discovery at break-even; never push. Exception: pack-match terms we already lead → harvest to exact at 3 orders | R-CI9, harvest |
| **Visibility loss** | hero organic/ad score Δ vs rival median (2.3) | the push fixes ads; on organic, a listing check on the hero (ref 09) and keep the hero advertised | R-C1, E15 |
| **Rivals moving** | brief movers, traffic surges | apply the 3-day hold; re-check movers every run | R-CI11 |
| **Measurement** | unmeasured and unmapped big sellers | exports for Beatable unmeasured rivals first; map the missing sellers; set a coverage target | R-CI12 |

### 9.3 Size battlegrounds

For core terms, give one row per size (then per segment, if segments differ from sizes): core keywords, market traffic, our traffic, our share, keywords we lead, our average organic rank, the most frequent traffic leader (top 2). Read it against stock per size. Our best position on the thinnest stock is a protect gap, not a push opportunity.

Example (B6): we led every tracked rival on the Full and Twin core terms, while the Full hero had 68 units.

### 9.4 Seed list (engine-blind and GAP — test terms)

One row per term, with these columns:

| Column | Content |
|---|---|
| Term, kind, size | from 5.2 |
| Weekly SV, market traffic, paid share, leader, our organic, opportunity | from the market pull |
| **Proposed owner** | the existing owner campaign if there is one; otherwise "New Exact in the <size> discovery campaign" (size unknown → the product's main size) |
| **How** | Exact, break-even base, no push premium |
| **Advertised variation** | discovery rule: the size's clearance colour, or "as the owner" |
| Verdict | from 6.2 |

- Judge each term with the keyword rules after 15 clicks: CVR ≥ the size rate → exact owner; 20 clicks and 0 orders → negate.
- No builds on deal days (E1).

### 9.5 Campaign-structure read

For each campaign family (ranking, discovery, brand defence, conquest PAT, SB/video) record: today's state → what the competitor data says → the change. Prefer adding terms to existing campaigns over new campaign types.

---

## 10. Sponsored Brands / video test design

Use this when rivals' brand banners sit above the top-of-search slot we buy (≥ 3 rivals with SB/SBV on push terms) and we have little or no SB/SBV reach. The test is an **owner decision** (R-CI10), built by hand.

| Element | Rule |
|---|---|
| Terms | Core push terms with the most rival banners, plus the main brand term(s). **Skip** terms we already lead with thin stock |
| **One format per term** | headline (product collection / store spotlight) **or** video, never both on one term, so each read is clean [B6 F17]. Choose the format the field uses most on that term |
| Match | Exact only; no new negatives |
| Advertised / landing | the size's hero (the ranking colour) or its product page; a collection for the head term; the store for brand terms |
| **Start bid** | break-even of the advertised variation = margin/unit × the size's top-of-search CVR (own CVR per the SKILL conversion basis) |
| Steps | while the banner isn't showing: raise ≤ 30% a day, never above the ceiling. The ceiling is 2 × break-even on push terms, and on brand terms only with verified rival presence (defensive allowance, ref 06). Otherwise 1 × break-even |
| At 15 clicks | switch from the size rate to the campaign's own CVR (blend 15–50, own from 50); break-even and the ceiling move with it |
| Keyword stops | 20 clicks, 0 orders → pause the keyword. ACoS > 2 × break-even on ≥ 30 clicks → back to the break-even bid; pause if it stays there 7 days |
| **Budget** | a **separate budget line**, $/day × test days, counted in the product's total spend limit and excluded from SP push budgets |
| Dates | Never start on deal days. Read before the next deal |
| **Read** (end of the test, 14 days by default [B6]) | ACoS ≤ break-even ACoS (full-price margin) → keep; budget may grow ≤ 30% a step. Between break-even and 2× break-even → keep at the break-even bid. > 2× break-even → stop |
| **Halo check** (same dates) | The SP campaign on the same term: orders and TOS CVR not below the 7 days before the test, and organic rank not worse. If SP orders fall by more than SB adds, the banner is taking our own clicks → stop |
| Report | impressions, CTR, CPC, orders, ACoS, new-to-brand share; for brand terms, the rivals' share of the term in the next ASINsight export |
| Creative | the value position against the field (e.g. pieces vs rivals' sets); logo; no price claim; video 15–30 s showing the product and its main benefit. No video ready → run headline until it is |
| Registration | Register each SB campaign with the SP campaign on the same term as a cross-format pair |

Reference split for the ad-format mix: SP ~80% / SB 15–20% / SD 5–10% [QA, PB]. It is a reference, not a target.

Example (B6): SB-1 was a headline collection on "bamboo sheets". SBV-2 to SBV-4 were video on two size head terms and the cooling term, which had 8 rivals on video. SB-5 was a store spotlight on the brand terms, and SD-6 covered own product pages. Bids started at break-even (King $15.97 × 20.0% = $3.19), with a ceiling of $6.38. The test ran $85/day for 14 days (≈ $1,190) and was read the day before the next deal. The second format on the same term, and the Full term (led by us, 68 units in stock), were not built.

---

## 11. Limits (state them in the report)

| Not available | Consequence / workaround |
|---|---|
| **Review themes** (what buyers praise or complain about) | Not in any connected source. Needs a manual read of reviews or an external review tool; list it as a data gap in ref 09 |
| **Competitor bids, CPCs, CVR, campaign structure** | Not available, and deliberately not used (R-CI4). Placement reach and banners are the only paid-behaviour signals |
| **Keyword-level history** | Each export is one week. Use rival-level trend × current rank (5.6) and label it a proxy |
| Revenue per keyword | Use the proxy traffic × SV (5.4) |
| Sales / clicks from ASINsight | 7-day traffic is impression-like. Never convert it to sales |
| Placement trends | scores only; retired feed with a fixed end date; heroes may be missing |
| Units / revenue | Data Dive estimates, for the best listing only |
| Discounts | strike-through only; coupons and lightning deals are unseen |
| Unmeasured competitors | no keyword data; brief and Data Dive only |

---

## 12. Outputs and checks

**Workbook tabs**: Competitor landscape (findings, sources and limits, market size, trend, reach, segments, niche benchmarks, price ladder) · Competitor profiles (+ each rival's top keywords) · Hero ASINs & trends (+ movers, rising-rival exposure) · Competitive keywords (every pulled keyword, filterable) · Push terms vs field (first milestones) · Gaps & how to fill (+ size battlegrounds, seed list, campaign structure) · Competitor ASIN targets · Competitor → engine (R-CI table + pipeline) · SB & video test (if approved) · Engine vs landscape (pivot, per term, campaign checks).

**Document**: 8–12 numbered findings, each Finding → Why it matters → Action → Expected impact, ordered by money at stake. No tool names or rule ids in the narrative.

**Checks (fail = fix before you present):**
- Every share, contest or "we win" figure states its coverage and date.
- No unmeasured rival is reported as zero.
- Every rival is labelled by brand.
- Every measured rival has a full profile (every blank field has a reason).
- All addressable pages were pulled (the count equals the addressability total).
- Every push, waiting and at-target term has a verdict and a first milestone.
- Every OFFENSIVE / AVOID class shows the price, rating and reviews comparison against the same-size listing.
- Every gap has size, fill and validation.
- No competitor figure changed a price or ceiling.
- Estimates are labelled as estimates.
- Artifacts are excluded from totals.

---

## 13. Open questions for the owner

1. **Conquest entry: B6 class vs PB 2-of-3.** The B6 OFFENSIVE test (we are ≥ 10% cheaper with rating within +0.1, or they have < 50% of our reviews at ≥ 90% of our price) and PB's gate (we win ≥ 2 of price / rating / reviews) can disagree: we can be cheaper yet lose on both rating and reviews. Register #31 adopts the R-CI rules but doesn't rule on PB's gate. Default used here: a new target needs both, and one that fails 2-of-3 runs as TEST. Confirm.
2. **R-X3 step size.** B6 scales conquest bids by ≤ 30% a step. Register #5 caps non-push raises at ≤ 25% per cycle, and that cap is applied here. Confirm that R-X3 falls under #5.
3. **Absolute thresholds** (500 units, 3,000 / 5,000 / 10,000 / 20,000 traffic, 10,000 reviews, 4,000 keywords, ±$5 / $15 price) are calibrated on one market. Should they scale with market size, and how?
4. **SB/video ceiling.** B6 priced the test up to 2 × break-even on push and brand terms. For a non-push, non-brand term this file applies 1 × break-even (register #3). Confirm.
