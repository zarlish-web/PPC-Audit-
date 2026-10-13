BFCM 2025 STOCK EXPORT
Window: 2025-11-15 through 2025-12-05 inclusive. Marketplaces: US and CA.

FILES
our_stock_bfcm2025.csv: requested nine columns, one row per historically observed marketplace/SKU/day, including blank placeholders for missing dates.
our_stock_bfcm2025_oos_summary.csv: first and last OBSERVED OOS dates per marketplace/SKU, plus known/unknown-day counts. This is the requested fallback where daily evidence is incomplete.
our_stock_bfcm2025_coverage.csv: product/marketplace footprint and catalogue gaps, including products with no historical snapshot evidence.

COVERAGE
28,350 daily rows = 1,350 marketplace/SKU pairs x 21 days (879 US; 471 CA).
23,833 rows have verified available/inbound quantities. 4,517 stock rows are unknown: 4,050 on wholly missing marketplace dates, 467 where that SKU is absent from an otherwise available snapshot.
18/21 daily snapshots exist for each marketplace.
US missing: 2025-11-26, 2025-11-27, 2025-12-01 (Cyber Monday).
CA missing: 2025-11-24, 2025-11-29, 2025-11-30.
450 observed FBA-zero SKU-days across 77 marketplace/SKU pairs. Do not interpret these as total OOS exposure across the full window.

DEFINITIONS AND LIMITATIONS
fba_available_units = Amazon fulfillable units, available to sell at the dated snapshot; reserved and unfulfillable quantities are excluded.
inbound_units = Amazon inbound working + shipped + receiving, not available inventory. Inbound is separate from FBA available and is not a warehouse/production total.
out_of_stock: Y only when observed fulfillable = 0; N only when observed fulfillable > 0. Blank means unknown. This is FBA inventory OOS, not proof of whole-listing unavailability or absence of FBM offers.
restricted_or_capped: UNKNOWN with a note throughout because the historical inventory feed does not provide verified listing restriction or cap status. The requested Y/N cannot be established. A GoToStranded recommendation, when present, is retained as a signal only, not as proof of a restriction or cap. No restriction/cap value is assumed N.
Missing snapshots are not interpolated, forward-filled, or inferred from sales, present-day stock, or Keepa.
Dates are the source report's snapshot dates. Capture time/time zone is not exposed, so these are not claimed as midnight/end-of-day balances and intraday stockouts are not measured.
First/last observed OOS dates are not proven onset/recovery dates and do not describe a continuous interval. Blank first/last dates mean no OOS observed in the available evidence, not proof that the SKU never stocked out.

PRODUCT SCOPE AND IDENTITY
B4/B6/S4/S6 = DECOLURE Bamboo 4pc/6pc and Satin 4pc/6pc. Satin Fitted = DECOLURE Satin Fitted Sheet.
SSS4 = Sleep Sanctuary/Sleephoria Satin 4pc; SL B6 = Sleep Sanctuary/Sleephoria Bamboo 6pc. Display labels use the current catalogue brand; historical rebranding is not a different product.
All cooling sheets covers DECOLURE Cooling/Bamboo Microfiber 4pc, Sleephoria Cooling Fitted/4pc/6pc, and CooLinens Cooling Fitted/4pc/6pc. Cooling comforter covers Sleephoria and CooLinens. Silk pillowcase = DECOLURE Mulberry Silk Pillowcase. Cooling pillowcases are outside the requested sheet/comforter/silk-pillowcase scope.
Current products with no snapshot evidence in this window are listed in coverage, not assigned zero stock or assumed launched. The CA scope has no observed SL B6, cooling comforter, or DECOLURE Cooling 4pc records. CooLinens and Sleephoria Cooling 6pc have no observed records in either marketplace.
Historical seller SKU strings and historical child ASINs are preserved, including Amazon.Found.* SKUs as distinct SKUs. Multiple seller SKUs on one child ASIN are NOT deduplicated into one row.
67 additional historical marketplace/SKU identities were recovered by exact child-ASIN matches against the live catalogue and canonical master tag mapping. No stock quantities were inferred. The known S4/S6 twin-tag overlap was resolved using the canonical master tag for unmatched historical SKUs; those rows are included once only. Family labels do not claim historical parent-ASIN membership.
Only SKUs observed in at least one inventory snapshot in the requested window enter the daily file. Current catalogue SKUs absent throughout are counted in coverage; their historical listing status is unverified.

SOURCE AND VALIDATION
Read-only Ecotero DataHub MCP amazon_inventory: all pages for every available marketplace/date, retrieved 2026-10-13. Source identifies the feed as Amazon FBA inventory reports. Product identity: variations_our_sales(include_inactive=true) used ONLY for identity, plus docs/product-context/portfolio-tag-mapping.json (AB Master SKU Level files). Sales values were not used to derive inventory.
Validation passed: full pagination and report totals for all 36 snapshots, unique marketplace/SKU/date keys, all 21 date rows per included SKU, exact requested column order, nonnegative integer units, preserved missing values, and 36 SKU/day comparisons against the separate amazon_inventory_history endpoint.

NEXT ACTION
Use the OOS summary for an observed-stockout review (~10 minutes). Exact event exposure and restriction/cap analysis remain blocked on the missing dated inventory snapshots and historical listing/cap logs. No commercial action or human decision is needed to use the observed data.
