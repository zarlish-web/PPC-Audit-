# Prompts for the data-retrieval agent

Copy one prompt at a time and attach `keepa_request.csv` wherever a prompt says so. Each prompt names the exact output file, so the results load straight into the tracker.

---

## Prompt 1: Keepa price and rank history (P1, needed by Thu Oct 15)

```
Pull daily price and sales-rank history from Keepa (Amazon.com, domain 1) for every ASIN in the attached keepa_request.csv where priority = P1 (93 ASINs: 23 ours, 70 competitors).

Date windows (pull all three):
  A) 2025-09-01 to 2026-01-05   (BFCM 2025)
  B) 2026-06-01 to 2026-07-05   (Prime Day 2026)
  C) 2026-09-01 to 2026-10-13   (current pricing)

Output ONE CSV named keepa_history_all.csv, one row per ASIN per day, with exactly these columns:
  asin, date, buy_box_price, new_price, amazon_price, list_price, lightning_deal_price, coupon, sales_rank, sales_rank_category, sales_rank_subcategory, sales_rank_subcategory_name, out_of_stock

Rules:
- date as YYYY-MM-DD; prices in USD as plain numbers (no $ sign); blank if Keepa has no value that day (never 0).
- Keepa stores changes, not days. Carry each value forward to every following day until it changes, so every day has a row.
- coupon: the coupon value that day, e.g. "10%" or "5.00"; blank if none.
- sales_rank = main category rank (Home & Kitchen); also give the subcategory rank and its name.
- out_of_stock = Y if there was no Buy Box and no new offer that day, otherwise N.
- If an ASIN has no data for a window (not yet listed), keep the ASIN in a separate list called missing_asins.txt with the reason.

Also return a short summary: ASINs pulled, ASINs missing, and any ASIN whose parent or brand differs from the CSV.
```

## Prompt 2: Keepa history for the other 240 ASINs (P2, after Thursday)

```
Same as the previous Keepa pull, for every ASIN in keepa_request.csv where priority = P2 (240 ASINs). Same three windows, same columns, same rules. Output keepa_history_p2.csv and missing_asins_p2.txt.
```

## Prompt 3: Keepa Product Viewer snapshot (all 333 ASINs)

```
In Keepa (Amazon.com), open Product Viewer, paste every ASIN from the attached keepa_request.csv (333 ASINs), and export the CSV with all columns. Name it keepa_viewer.csv.

These columns must be present (rename to these names if Keepa labels differ):
  asin, title, brand, parent_asin, variation_count, variation_asins, listed_since, buy_box_current, buy_box_avg_90d, buy_box_lowest_90d, list_price_current, sales_rank_current, sales_rank_avg_30d, sales_rank_avg_90d, bought_past_month, lightning_deal_current, coupon_current, rating, review_count, offer_count, buy_box_seller

Prices as plain numbers, dates as YYYY-MM-DD. Return the CSV and the count of ASINs Keepa could not find.
```

## Prompt 4: Keepa deal history for BFCM 2025 (optional)

```
For every ASIN in keepa_request.csv where priority = P1, pull Keepa's deal history between 2025-11-20 and 2025-12-01 (Amazon.com).

Output keepa_deals_bfcm2025.csv with columns:
  asin, deal_type (Lightning Deal / Best Deal / Prime Exclusive / Coupon / Other), deal_start (YYYY-MM-DD HH:MM), deal_end, deal_price, list_or_reference_price, percent_claimed (if shown)

One row per deal. If an ASIN ran no deal in that window, write one row with deal_type = None.
```

## Prompt 5: Is the strikethrough showing today? (Command Center STR Panel, or a page check)

```
For every competitor ASIN in keepa_request.csv where priority = P1 (role = competitor, 70 ASINs), record what Amazon.com shows today for a US address, logged out.

Output str_check_<YYYY-MM-DD>.csv with columns:
  asin, check_date, check_time_et, price, strikethrough_shown (Y/N), strikethrough_price, strikethrough_label (List Price / Typical price / Was price / none), deal_badge (none / Limited time deal / Prime exclusive / other), coupon (blank or value), in_stock (Y/N), buy_box_seller

First try the Command Center STR Panel (Data Hub > Competitors > STR Panel): if it already has today's read for an ASIN, use it and note source = STR Panel. Otherwise read the product page and note source = page.
```

## Prompt 6: Our BFCM 2025 deals (Umair / Seller Central Promotions)

```
From Seller Central (US and CA), Promotions / Deals history, list every deal we ran or scheduled between 2025-11-01 and 2025-12-05.

Output our_deals_bfcm2025.csv with columns:
  marketplace (US/CA), parent_asin, product_name, sku, child_asin, deal_type (Lightning Deal / Best Deal / Prime Exclusive Discount / Coupon), deal_start, deal_end, deal_price, reference_price, committed_units, units_sold, status (ran / cancelled / suppressed), notes

Cover at least these products: Decolure Bamboo Sheets 4 Piece and 6 Piece, Decolure Satin Sheets 4 Piece and 6 Piece, Decolure Satin Fitted Sheet, Sleephoria Satin Sheets 4 Piece, Sleephoria Bamboo Sheets 6 Piece, Decolure / Sleephoria Cooling Sheets 4 Piece, Sleephoria Cooling Comforter, Decolure Silk Pillowcase.
```

## Prompt 7: Our stock-outs during BFCM 2025 (Haroon / David)

```
For BFCM 2025, list our stock position per variation (US and CA) from 2025-11-15 to 2025-12-05.

Output our_stock_bfcm2025.csv with columns:
  marketplace, product_name, sku, child_asin, date, fba_available_units, inbound_units, out_of_stock (Y/N), restricted_or_capped (Y/N + note)

Products: B4, B6, S4, S6, Satin Fitted, SSS4, SL B6, all cooling sheets, cooling comforter, silk pillowcase. One row per SKU per day. If daily data is not available, give the first and last OOS date per SKU instead.
```

## Prompt 8: Our 2026 BFCM deal plan (Umair's deal coverage list)

```
For every product we sell in the US (and CA where registered), give our planned BFCM 2026 deal.

Output our_deals_bfcm2026_plan.csv with columns:
  marketplace, product_name, parent_asin, hero_sku, hero_child_asin, deal_type, deal_start, deal_end, hero_deal_price, reference_price, committed_units, status (scheduled / pending eligibility / suppressed / none)

Use the current Seller Central registrations (596 US and 438 CA SKUs registered). One row per parent product using the hero variation's price, plus a second file our_deals_bfcm2026_skus.csv with every registered SKU and its deal price.
```

## Prompt 9: Canada competitor set (Amazon.ca page research, then Keepa .ca)

The Command Center maps no Canadian competitors, so the 6 Canada tabs are empty. Keepa tokens go to P2 and our 23 heroes first; part B runs after those.

```
Read-only. Don't change, request or grant any access; don't add to cart or change any listing.

PART A - Find the Canadian competitor set (Amazon.ca page research, no Keepa)
Conditions: Amazon.ca desktop, logged out, delivery postal code M5V 3L9 (Toronto), prices in CAD.

For each of our products below, search each keyword and read page 1 organic results (skip "Sponsored" tiles). Keep products of the SAME type (same material and piece count). Exclude our own brands: DECOLURE, SLEEPHORIA, SLEEP SANCTUARY, CooLinens. Take up to 15 competitors per product, ranked by best organic position across its keywords.

  DC B4  (our parent B08LW37SB9; 4-piece bamboo/viscose sheet set): "bamboo sheets queen", "bamboo sheets king", "cooling bamboo sheets"
  DC B6  (our parent B0D71YJYNL; 6-piece bamboo/viscose sheet set): "6 piece bamboo sheets", "bamboo sheets queen 6 piece", "bamboo sheet set king"
  DC S4  (our parent B0CT3HF44M; 4-piece satin sheet set): "satin sheets queen", "satin sheets king", "silk satin sheets"
  DC S6  (our parent B0CJSDXDJW; 6-piece satin sheet set): "satin sheets 6 piece", "satin sheets queen 6 piece"
  SSS4   (our parent B0F2Z7C4ST; 4-piece satin): reuse the DC S4 list, no separate search
  DC Satin Fitted (our parent B0FQC9C5QT; satin fitted sheet only): "satin fitted sheet queen", "satin fitted sheet"

For each competitor open the product page, select the QUEEN size (if there is no Queen, King, and say so in notes), and record what a shopper sees.

Output ca_competitors.csv, one row per our_product + competitor, exactly these columns:
  our_product, our_parent_asin, keyword, organic_rank, competitor_brand, title, parent_asin, child_asin, size, colour, piece_count, material, price_cad, strikethrough_shown (Y/N), strikethrough_price_cad, strikethrough_label (List Price / Typical price / Was price / none), deal_badge, coupon, rating, review_count, bought_past_month, bsr, bsr_category, variation_count, in_stock (Y/N), buy_box_seller, main_image_url, check_date, check_time_et, notes

Rules:
- child_asin = the ASIN of the selected Queen variation, not the parent.
- price_cad = buy box price for that exact variation before coupon. Blank when not shown, never 0.
- main_image_url = full https://m.media-amazon.com/images/I/<id>.jpg URL.
- If a page redirects to another ASIN, keep the requested ASIN with blank commercial fields and name the redirect in notes. Don't substitute.
- Send ca_competitors_notes.txt with conditions, counts per product, and every exception.

PART B - Keepa history on Amazon.ca (domain 6), after the P2 and our-hero pulls finish
For every unique child_asin in ca_competitors.csv, pull Nov 1 - Dec 5, 2025, one row per ASIN per day, in exactly the format of keepa_history_p1.csv (asin, date, buy_box_price, list_price, lightning_deal_price, prime_exclusive_price, coupon, sales_rank, out_of_stock), prices in CAD. Output keepa_history_ca.csv plus keepa_history_ca_coverage.csv and keepa_history_ca_provenance.csv like P1. Blank never 0; no parent or redirect substitution.
```

Files go in `data/ca_competitors/` (Part A) and `data/keepa/` (Part B); the builder fills the 6 Canada tabs from them.

## Prompt 10: Competitor variations, with colours, sizes and images (Keepa)

```
For every competitor parent ASIN in the attached keepa_request.csv (column parent_asin, role = competitor; de-duplicate), list ALL its child variations on Amazon.com using Keepa (product?asin=<parent>&domain=1 returns the variations list; then pull each child).

Output competitor_variations.csv with one row per child ASIN and exactly these columns:
  parent_asin, child_asin, brand, title, color, size, style_or_pattern, other_attributes, current_buy_box_price, list_price, sales_rank, rating, review_count, bought_past_month, main_image_url, all_image_urls (pipe-separated), in_stock (Y/N)

Rules:
- color / size / style come from the variation attributes (Keepa "variations" attributes or the listing's dimension values), not guessed from the title.
- main_image_url must be the full https://m.media-amazon.com/images/I/<id>.jpg URL (Keepa imagesCSV first entry, prefixed with https://m.media-amazon.com/images/I/).
- Prices in USD as plain numbers. Blank when unknown, never 0.
Return the CSV plus a count of parents and children pulled and any parent that returned no variations.
```

## Prompt 11: Download the image files (for the web dashboard)

```
Download every image listed in the attached image_request.csv (column image_url) and the main_image_url of every row in competitor_variations.csv (from Prompt 10).

Save each file as <asin>.jpg, resized so the longest side is 400 px (JPEG quality 80). Put them all in one folder named product_images/, zip it as product_images.zip, and include a manifest CSV (asin, source_url, file_name, width, height, ok Y/N, error).
Do not substitute any other image when a download fails; mark ok = N with the error.
```

## Prompt 12: Our own live prices (Amazon page check of our child ASINs)

Why: the Command Center price for our SKUs comes from its fee feed, last dated Mar 30, 2026. Live prices are higher on several heroes (B6 King White $99.99 live vs $89.99 in the feed; B4 King White $94.99 vs $79.99), so every "their price vs ours" gap needs our live price.

```
Read-only. Don't change any price, deal or listing, and don't change, request or grant any access.

For every row in the attached our_price_request.csv where live_price_held = N (US rows on Amazon.com, CA rows on Amazon.ca), open the product page of child_asin with the size and colour selected, logged out or with a non-Prime view if possible, and record what a shopper sees right now.

Output our_price_check_<YYYY-MM-DD>.csv with exactly these columns:
  marketplace, asin, sku, check_date, check_time_et, price, strikethrough_shown (Y/N), strikethrough_price, strikethrough_label (List Price / Typical price / Was price / none), deal_badge (e.g. Limited time deal / none), coupon (e.g. 10% / $5 / blank), prime_exclusive_price, rating, reviews, bought_past_month, in_stock (Y/N), buy_box_seller, parent_asin_on_page

Rules:
- price = the price in the buy box for that exact size and colour, before any coupon. Plain numbers, USD for US and CAD for CA.
- Blank when not shown, never 0. Don't carry a value over from another colour or size.
- Start with the rows that have the most units_28d (heroes first); if you can't finish all of them, send what you have and say how many are left.
- Report any child_asin that redirects to another ASIN, shows "Currently unavailable", or sits under a different parent than the rest of its product.
```

Save the file in `data/our_prices/` and rebuild: live prices replace the stale Command Center price in every tab, the Product Index, the Dashboard and the same-size gaps.
