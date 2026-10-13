BFCM 2025 V2 — IN-PROGRESS CHECKPOINT, NOT COMPLETE
Window: Nov 1–Dec 5 2025 inclusive, US and CA separate, UTC.

our_deals_bfcm2025_v2.csv retains all 3,080 native campaign-child rows and the original 14 columns, plus price_source and observed_deal_price_keepa. Original v1 is unchanged (SHA256 2fb5ec3bb9cbd908df4fa9579408f8f1c8417e7b03b0f00aa1867339be94d1f4).
This checkpoint fills 24 row-level observed-price fallbacks: 21 US / 3 CA. These are reused/live-read histories, not coverage of the entire requested set. Read summary.json and the coverage CSV for progress at checkpoint creation. A token-paced pull is continuing separately for the full 1,378 marketplace/ASIN pairs; this downloaded checkpoint will not update itself.

SOURCE ACCESS
1) DataHub Amazon-native promotions readable, earliest history US2025-08-07/CA2025-08-08, latest2026-10-13. Includes historical APPROVED and CANCELED campaigns. However, the granted amazon_promotions tool omits SKU-level deal price, reference price and committed units. The distinct DataHub browser page requires sign-in in both profiles; stopped there. Full table minimum date and unpublished columns cannot be verified. No access changes, requests, grants or login attempts made.
2) No PED table/query tool exposed among61 currently granted tools. Browser requires sign-in. Earliest PED TABLE date unknown for both marketplaces. Stopped this source. This is not proof the underlying database has no PED table.
3) Coupon history readable from2024-08-19 for both marketplaces. Latest snapshot US2026-10-13 / CA2026-08-06. No readable newer CA table exposed; stopped that route. Old CA history remains usable with a stale-source caveat.
4) Keepa US(domain1) and CA(domain6) Buy Box and promotion PRICE histories readable. Verified testASIN B08KQHRDDG: BuyBox earliest US2021-01-20T06:32Z / CA2021-10-29T23:40Z; Lightning earliest US2021-09-23T18:10Z / CA2023-02-17T18:40Z; PrimeExclusive earliest US2024-10-08T07:22Z / CA2025-10-08T06:24Z. Earliest dates vary by ASIN and series; these are sample-specific, NOT universal coverage guarantees.

PRICE METHOD
observed_deal_price_keepa = lowest positive Keepa Buy Box item price + known nonnegative shipping within each FULL native campaign's UTC bounds, using Keepa change-point intervals. The state immediately before campaign start is considered only until the next recorded change. Nonpositive prices and unknown shipping do not become zero-valued prices. No Amazon/New/list-price substitution, and no revenue / units calculation.
Values are USD for US and CAD for CA. No currency conversion. The ASIN-wide Buy Box winner may not be our offer. Even for a cancelled campaign, a price observed during its scheduled interval does NOT show that the deal ran or that this was its intended deal price.
price_source=keepa_observed only where the separate fallback field is populated; otherwise blank. seller_central_pull will be used only for verified native deal-price additions. deal_price, reference_price and committed_units remain blank because no permitted source exposed them.
Source join is marketplace + campaignID (source_id in notes) + childASIN. Product names are not join keys. Existing known native units_sold=0 remain valid facts; unknown fields are blank, never filled with0.

THREE SLEEPHORIA FAMILIES
Native deal/coupon queries and exact-ASIN legacy-name checks remain without matching records for Cooling Comforter, Bamboo6 and Cooling4. Absence remains unverified, particularly PED/suppression history and CA Bamboo6 identity (no current CA product mapping; US ASINs are secondary search candidates).
Keepa has supplied Prime Exclusive PRICE observations for US Bamboo6 and Cooling Comforter in this checkpoint. See sleephoria_keepa_observations.csv for exact ASINs, price values and observed intervals. These observations do not establish native campaign IDs, scheduled dates, discount/reference amounts or ran/cancelled/suppressed status. Therefore no synthetic native PED campaigns were appended to the main CSV. Cooling4 and unpulled child ASINs remain unresolved; more observations may arrive as the pull proceeds.
Current product mapping anomaly B0HK541FW9 is Decolure Satin6 despite product45 mapping and is excluded from the target-family Keepa pull. Other v1 mappings and financial values remain unchanged.

FILES
our_deals_bfcm2025_v2.csv — requested16-column ledger, partial checkpoint.
our_deals_bfcm2025_v2_coverage.csv — per-marketplace/ASIN retrieval coverage, including unpulled rows.
our_deals_bfcm2025_v2_price_evidence.csv — native campaign key, currency, minimum observation time and raw source reference for every v1 row.
sleephoria_keepa_observations.csv — observed price/coupon signals only, not native campaign records.
summary.json — checkpoint counts and original hash.

REMAINING
Continue token-paced read-only Keepa retrieval; normal cost3tokens/product with BuyBox, refill1token/minute, reserve5tokens. Full run may take about3days, longer with shared token consumption. No subscription or access changes. Native prices/commitments/PED-status completion still requires source access or exports handled by Shayan, not by this agent.
