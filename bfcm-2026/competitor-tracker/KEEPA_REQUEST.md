# Keepa request: BFCM 2026 competitor tracker

The Command Center gives each competitor's current price, List Price, BSR, weekly units, rating and tier. It cannot give last year's BFCM, because its competitor history starts in January–April 2026. These three Keepa files fill the yellow columns in the tracker.

The ASIN list is `keepa_request.csv` in this folder (Amazon.com, one row per ASIN, with priority, role, brand and the product each competitor is mapped to).

- **P1 (93 ASINs):** Aspirational and Beatable rivals on the hero and core products, plus our own best-selling child ASINs. These are needed for v1 on Thu Oct 15.
- **P2:** the rest of the mapped set.

## File 1: Product Viewer snapshot (one CSV, all ASINs)

Keepa → Data → Product Viewer → paste the ASIN list → Export CSV (all columns). Columns used:

| Column | Fills |
|---|---|
| ASIN, Title, Brand, Parent ASIN | identity check |
| Variation count / Variation ASINs | `Variations` where Data Dive is blank |
| Listed since | `Listing age` where Data Dive is blank |
| Buy Box: Current, Buy Box: 90 days avg, Buy Box: Lowest (90 days) | `Lowest price last 90d` |
| List Price: Current | cross-check of the Command Center List Price |
| Sales Rank: Current, 30 days avg, 90 days avg | rank trend going into Q4 |
| Bought in past month | sales cross-check |
| Lightning Deals: Current, Coupon | `Deal / coupon live now` |
| Reviews: Rating, Review Count, Count of offers, Buy Box Seller | listing health |

Name it `keepa_viewer.csv`.

## File 2: Daily price and rank history (main file)

One long CSV, or one per ASIN, with daily rows for three windows:

| Window | Why |
|---|---|
| **Sep 1, 2025 – Jan 5, 2026** | BFCM 2025: deal type, dates, pre-event price, BFCM low, discount, BSR before, during and after, out of stock |
| **Jun 1 – Jul 5, 2026** | Prime Day 2026, to compare with the Command Center visibility history |
| **Sep 1 – Oct 13, 2026** | current pricing trend, and whether they sold at their List Price in the last 90 days (the STR test) |

Columns: `asin, date, buy_box_price, new_price, amazon_price, list_price, lightning_deal_price, coupon, sales_rank, sales_rank_subcategory, out_of_stock`

- **Format:** dates as `YYYY-MM-DD`, prices in USD as plain numbers.
- **Name:** `keepa_history_all.csv`, or `keepa_history_<ASIN>.csv`.
- **API equivalent:** `product?domain=1&asin=...&history=1&days=420&stats=420&buybox=1&rating=1&offers=20`

## File 3 (optional): Keepa deal history, Nov 20 – Dec 1, 2025

This is the deal type and deal price exactly as Keepa logged them for the same ASINs. It makes the "BFCM 2025 deal type" column exact rather than inferred from price moves.

## How each tracker column is read from File 2

| Tracker column | Rule |
|---|---|
| BFCM 2025 deal type | lightning_deal_price present → Lightning Deal. Buy Box drop with a deal badge for several days → Best Deal. Prime-only price → PED. Coupon only → Coupon only. Plain drop → Price cut only. |
| Deal start / end | First and last day at the deal price within Nov 20 – Dec 1, 2025 |
| Pre-event typical price | Most common Buy Box price Oct 21 – Nov 19, 2025 (PBDD Oct 7–8 excluded) |
| BFCM 2025 low price | Lowest Buy Box price Nov 20 – Dec 1, 2025 |
| BSR pre / BFCM / Dec | Average main-category rank for Oct 21 – Nov 19 / Nov 20 – Dec 1 / Dec 2 – 31, 2025 |
| OOS / lost Buy Box | Any out_of_stock day, or no Buy Box price, during Nov 20 – Dec 1 |
| PBDD 2025 deal price | Lowest price Oct 7–8, 2025 |
| Sold at List Price in last 90d | Any day in the last 90 days where buy_box_price ≥ list_price |

## Canada

The Command Center holds no Canadian snapshots for any competitor. Once the CA rival set for B4, B6, S4, S6, SF and SSS4 is mapped, run the same Files 1–2 on Amazon.ca (domain 6).
