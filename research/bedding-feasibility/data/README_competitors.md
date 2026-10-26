# Competitor, keyword-demand and search-market data: bedding feasibility (US / CA / UK)

Pulled on 2026-10-26 with read-only tools only: the ecotero-command-center MCP and the Data Dive MCP (no tokens spent, nothing created or edited).
The main analysis window is **year-to-date 2026 (2026-01-01 → 2026-10-26)**. The 2025 data is kept only for seasonality and year-on-year context.
The scripts that rebuild every CSV are in `../scripts/`. Every raw tool response is dumped to `../raw/calls.jsonl`.

## As-of dates for volatile values
| Source | As-of |
|---|---|
| Command-center roster (`competitors_roster`): price, reviews, rating, BSR, promotions, stock, listing assets | Weekly scrape, week starting **2026-10-25**. A few rows are older, e.g. Bedsure satin fitted, Candoury and Avolare at 2026-09-13 or 2026-08-30. Each row's date is in `scrape_week_start`. |
| Roster sales band (X-Ray bracket) | Same weekly scrape (2026-10-25) |
| Our own units and revenue in the roster | Week starting **2026-10-19** (`sales_week_start`) |
| `competitors_evidence` bands (US: 59, 30, 37, 39, 45, 46) | Scraped 2026-10-26. Our family units come from a 27-day window ending 2026-10-24. |
| BSR→units model (`competitors_sales_estimate`) | Season 2026-10, model v1 |
| Data Dive niches | The research date of each niche (2025-06-02 to 2026-10-26), given in each file |
| SQP | Weekly, from week 2025-01-05 (US) or 2025-08-24 (CA, the first week held) to week **2026-10-11** (the latest week held) |
| Keepa | Daily, 2025-07-01 → 2026-10-26 |
| ASINsight traffic | Our exports 2026-10-19 or 2026-10-26. Rival exports 2026-09-20 → 2026-10-15. |

## Files
**competitors.csv**: 559 rows. There is one row per (our product × marketplace × mapped rival), plus our own baseline rows (`is_ours=1`, one per marketplace).
- Products: the 16 in the brief, plus 3 extra bedding products (36 Sleephoria Bamboo 4pc, 74 Sleephoria Satin 6pc, 43 Sleephoria Cooling Pillowcases). These are flagged in `our_product`.
- Segment mapping:
  - bamboo: 59, 30, 32, 36
  - satin: 37, 31, 39, 74
  - cooling sheets: 45, 48, 69
  - quilt: 46
  - comforter: 42
  - pillowcases: 55, 70, 43
  - fitted: 38, 44, 73
- Fields:
  - rival brand, parent ASIN, title, relevance (core / adjacent / unmarked, which reads as core), operator tier and who set it
  - price and price index vs us
  - `est_units_week` plus band lo/hi (the roster's X-Ray bracket, **estimate**), with month = week × 52/12 and revenue = units × current price
  - `model_units_month` (the BSR model, **estimate**; filled only where the roster band has no lower bound)
  - `units_month_used`, whose `units_basis_used` says which source was used
  - the evidence band (expected/lo/hi, basis, engine band, coverage-suspect flag) for the 6 products where evidence was pulled
  - reviews, review velocity per week, rating, BSR and its trend, coupon, deal, strikethrough %, stock, A+, image count, bullet count, scrape date
- **CA has no rivals mapped in the command center.** The roster for CA returns only our own rows. Keepa also tracks nothing in CA.

**leaderboard.csv / leaderboard_concentration.csv**
- Distinct rival listings per segment are de-duplicated by competitor id and aggregated by brand. Brands are ranked by estimated monthly units, with review count, rating and price of each brand's top listing, plus its scrape week.
- Two variants: `all_mapped`, and `excl_adjacent`, which drops rivals marked adjacent on every mapping in the segment.
- The concentration file gives top-3 and top-10 unit share across the mapped set, top-3 revenue share, the median price, the median and p75 reviews of the top-20, and our measured units against the mapped set.
- US only. CA has no mapped rivals.
- Limitations:
  - These are shares of the *mapped set*, not of the whole category.
  - The quilt-set rivals' `name` field carries a template artifact ("X – Bamboo Sheets"). The brands and ASINs are quilt sellers.

**niche_keywords.csv**: top 150 keywords by search volume for each of 27 Data Dive niches.
- Fields: search volume (Data Dive monthly estimate), relevancy, origin, count of tracked competitors ranking top-10, best competitor rank, competitor ranks ≤20, and suggested bid min/median/max in USD.
- Data Dive returns bids in cents. They are converted here.

**niche_competitors.csv**: competitors from 10 niches: bamboo RR, bamboo fitted, bamboo king, satin fitted, SS Satin 4pc, satin sheets, cooling, Sleephoria quilt, CA bamboo 4pc, CA satin 4pc.
- Fields:
  - ASIN, brand, title, price, reviews, rating, BSR
  - **Data Dive estimated monthly units and revenue**
  - listing creation date, fulfillment, seller country, variations, keywords and search volume ranked on page 1, advertised keywords, and the listing's Ranking Juice

**niche_roots.csv**: the top 60 roots for 15 niches, with frequency, broad search volume, ratio to the top root, and share of the niche's keyword search volume.

**niche_summary.csv**: one row per niche.
- Fields: keyword counts, total search volume (all MKL / top 150 / top 20), the top keyword, and, where competitors were pulled, price stats, review p25/p50/p75/p90, median rating, Data Dive total and top-3 revenue, % of competitors under 500 reviews, Data Dive benchmark and opportunity flags, and median/max competitor Ranking Juice.
- The optimized-listing Ranking Juice total is given only for 7qMjYEtaIG.
- 17 niches have keywords and roots only (`n_competitors` = "NOT PULLED"). Their competitor lists were skipped to stay within the session's context budget. They can be pulled later at no token cost.

**sqp_market.csv**: Brand Analytics Search Query Performance, rolled up by query.
- Rows are monthly (each week is assigned to the month of its Sunday start), plus three total rows per query and marketplace:
  - **YTD2026** (weeks 2026-01-04..2026-10-11)
  - **SamePeriod2025** (weeks 2025-01-05..2025-10-12)
  - **BFCM+Dec2025**
- Fields: market search volume, impressions, clicks, cart adds, purchases, CTR, CVR (purchases per click), purchases per search, and our impressions, clicks and purchases with our impression and purchase share. `weeks_in_data` shows how complete each period is.
- Missing queries:
  - "duvet cover" (US) has no exact match. It was replaced by the top-3 "duvet cover…" queries found with `query_contains` (see `matched_via`).
  - "percale sheets", "microfiber sheets", "quilt queen", "comforter set" and "sheets queen" appear in only a few weeks.
- Limitation: by-query rows carry no median price, so price was not available from SQP.

**keepa_samples.csv**: covers the top 10 rival seed ASINs by estimated sales in bamboo sheets and in satin sheets (US).
- One row per ASIN per month, plus three window rows:
  - **MAIN 2026-01-01..2026-10-26**
  - CONTEXT 2025-07..12
  - BFCM+Dec 2025
- Fields: average, minimum and maximum buy-box price, average list price, % of days with a coupon and the average coupon depth, Lightning Deal days, average and best BSR, reviews at start and end, review velocity per 30 days, rating at end, and the average and maximum "bought in past month" badge.
- The seeds are single child ASINs (for example B07MZ9223H is Pure Bamboo Queen/White).
- A negative review velocity means the review count was reset or re-pooled in a variation split (CozyLux, Lanest, Pure Bedding, DOZ). It is not real attrition.

**keepa_tracked_bedding.csv**: the 297 Keepa-tracked US ASINs that are bedding rival seeds or our parents. CA tracks 0.

**traffic_market_summary.csv / traffic_keywords.csv**
- ASINsight 7-day traffic, an impression-like figure: not clicks, not sales.
- Products: 59, 37, 30 (US). The summary gives coverage, export spread and comparability, tracked traffic, our share, and contested/own/rival-only keyword counts.
- The keywords file has the top 100 keywords by tracked traffic per product. Fields: state, addressability, segment, number of rivals ranking, rival traffic average/max/sum, top-3 rivals, our traffic, organic and SP rank, placements, and PPC opportunity flag.
- The exports span 21–36 days, so the tool marks them **not comparable** like-for-like.

## How the sales bands were derived (competitors_evidence summary)
- **Roster `salesBand` / `salesPerWeek`:**
  - This is the Helium 10 X-Ray bracket for the rival's parent family, converted to units per week. The point value is the bracket midpoint.
  - A null lower bound means only a ceiling is known.
  - **Estimate.**
- **Evidence `workingBand`, basis `pdp_badge_brackets` (≈93% of rivals):**
  - The engine scrapes every known child ASIN (coverage 1.0 on most families) and sums Amazon's "X+ bought in past month" badge brackets.
  - The badge floors give a *proven lower* bound. Badged and unbadged ceilings give the upper bound.
  - Unbadged children get a small expected value.
  - Result: expected units per week with lo/hi.
- **Review-velocity cross-check:**
  - The median non-negative week-over-week review gain, divided by an assumed **0.0279 reviews per sale**, gives an implied units/week.
  - Where the badge sum covers only a fraction of children, or the two methods disagree by about 10×, the band is flagged **coverage.suspect**.
  - Suspect counts: 3 of 60 rivals (59 and 30), 1 of 36 (45), 0 elsewhere.
  - Basis `review_velocity` is used for those rivals.
- **Engine band** (BEATABLE / ASPIRATIONAL / PEER / BELOW) places the rival's band against **our measured family units**. Our measured units/week over the 27 days to 2026-10-24:
  - 59: 444.9
  - 30: 524
  - 37: 816.1
  - 39: 261.3
  - 45: 97.5
  - 46: 7.5
  The engine band is evidence, not a grade. It agrees with the operator tier on only 2–10 rivals per product.
- **The two estimates disagree.** Across the 201 rivals where both exist (evidence band above 50 units/week), the X-Ray midpoint is a median of **1.40×** the PDP-badge expected value (interquartile range 1.25–1.55×). Treat X-Ray as the high side.
- **BSR model (`competitors_sales_estimate`):**
  - A Home & Kitchen BSR → units model fitted on *our own* sales (about 0.95× actual on our families), with the seasonal factor for bedding in October 2026.
  - It returns whole-family units with a range, and is extrapolated under BSR 2,000.
  - It is used here only for the 124 rows (58 rivals) whose X-Ray band had no lower bound.

## Limitations
- Every rival sales or revenue figure is an **estimate**: X-Ray, PDP badges, the BSR model or Data Dive. Revenue = estimated units × current price, so promotions are ignored.
- The roster's own-product `unitsPerWeek` can cover a single parent. The evidence `us.unitsPerWeek` covers the whole family, so for 59 the roster shows 156/week and evidence shows 444.9/week.
- The rival sets were hand-mapped to our products, so leaderboards and shares describe the mapped set, not the whole category.
- SQP is a sample. It shows only queries where our ASINs got impressions, so gaps are weeks with no data, not zero demand. Read it as ratios, shares and seasonality.
- **UK: no bedding data exists in either source.**
  - The command center covers US, CA and MX only.
  - The only co.uk Data Dive niche (5G5waxjaHe) is a *knee pillow* niche (head term "knee pillow", 13,156 search volume, research date 2026-06-27). It is not bedding.
- Data Dive search volumes are vendor monthly estimates at each niche's research date. Older niches (linen 2025-06, protector 2025-08) are stale.
