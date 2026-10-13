BFCM 2025 STOCK REVISION 2 — CHILD-ASIN OOS CORRECTION
Requested by Shayan 2026-10-13 in the original stock-export thread.

USE THESE FILES
1. our_stock_bfcm2025_by_child_asin.csv: one row per marketplace + child ASIN + date. This is the primary inventory/OOS analysis view and replaces SKU-level OOS interpretation.
2. our_stock_bfcm2025_oos_by_child_asin.csv: first/last observed child-ASIN OOS dates and in-stock/OOS/unknown day counts. Replaces the earlier SKU OOS summary for variation analysis.
3. our_stock_bfcm2025_sku_with_child_status.csv: original SKU-level balances and SKU out_of_stock, with explicitly named child_asin_out_of_stock and child aggregate columns. The original out_of_stock column here STILL means SKU-level zero, not child stockout.
4. our_stock_bfcm2025_duplicate_sku_corrections.csv: 159 child-days where one SKU was zero but another SKU had stock, across 16 marketplace/child pairs.
5. our_stock_bfcm2025_missing_date_recovery.csv: exact status and dependency for each of the six missing dates.

CORRECTED COUNTS
27,552 child/day rows = 1,312 marketplace/child pairs x 21 dates (US 843; CA 469).
289 verified child-level OOS observations across 60 marketplace/child pairs; 22,962 in-stock child-days; 4,301 unknown child-days.
The earlier 450 SKU-zero observations resolve to: 289 verified child-OOS, 159 child-in-stock, 2 child-unknown because another linked SKU was missing. The earlier 450 figure must NOT be cited as child-ASIN stockout days.
Example: US B08KQHRDDG on 2025-11-22: BAMBOO-KING-WHITE=1,721 available; Amazon.Found.B08KQHRDDG=0. Child available=1,721, inbound=738, OOS=N.

AGGREGATION AND MISSINGNESS
Sum distinct seller-SKU inventory balances by marketplace/child/date. The source rows were checked for duplicate ASIN+FNSKU+condition within marketplace/date: none found. Amazon.Found is not blanket-discarded: it sometimes holds actual units under a different FNSKU. Its zero does not negate stock on the main SKU.
All raw snapshot SKU rows for included child ASINs are included. Marketplaces are never pooled.
Child OOS=N if ANY observed linked SKU has positive fulfillable units, even if another SKU is missing.
Child OOS=Y only if ALL seller SKUs observed for that child anywhere in this window have known inventory that day, and their combined fulfillable quantity is zero.
If only zeros are observed and another linked SKU is absent, OOS is blank/unknown, not Y. These conservative unknowns avoid treating absent data as zero.
fba_available_units and inbound_units are the complete linked-SKU sum only when every linked SKU is observed; otherwise blank. observed_fba_available_units and observed_inbound_units show the known subtotal (a lower bound), not a complete total. source_skus, missing_skus, and coverage make this auditable. There are 104 partial-SKU-coverage child-days.
Snapshot dates/time semantics and original product scope are unchanged. First/last OOS dates are observed dates, not continuous intervals or proven onset/recovery. Restriction/cap flags remain UNKNOWN.

MISSING-DATE RECOVERY RESULT: 0 OF 6 RECOVERED
US: 2025-11-26, 2025-11-27, 2025-12-01 (Cyber Monday).
CA: 2025-11-24, 2025-11-29, 2025-11-30.
The original full-marketplace daily snapshot requests returned no_snapshot. Fresh exact-date inventory-history queries for product B4 returned days=0/rows=[] for all six dates; the endpoint explicitly says a date missing from rows had no snapshot. Previous independent US/CA full-window history queries also omitted the same dates.
Current authenticated DataHub tool discovery exposes daily inventory/history but no Amazon inventory-ledger/report generation tool. The similarly named production-order ledger is a supplier PO ledger, not Amazon FBA history.
A documented archived 365-day ledger exists in the June LTSF workbook, but the Google Sheets read failed at authentication (RefreshError), before data retrieval. The earlier raw TSV referenced in May memory was a transient /tmp file and was not found. The local ledger summary is receipts-only with 2025-12-07 onward coverage, outside the requested window.
Seller Central ledger page redirected to sign-in; the existing-user Chrome connection was unavailable. Native Amazon report credentials were not present in the supported Gateway runtime, though stored vault references exist. This is a current access/source blocker, not proof the underlying history is permanently unrecoverable.
Ledger movements or sellable warehouse balances alone cannot reliably reproduce historical available-to-sell quantities without reserved customer-order/FC-transfer/FC-processing balances and inbound state. A reconstruction must be separately labeled and reconciled; no sales subtraction, interpolation or carry-forward was used.

NEXT RECOVERY INPUT
Highest priority: the archived US 2025-12-01 FBA Inventory/Inventory Planning export containing fulfillable and inbound fields. Then the other five dates. An authenticated full ledger plus opening balances and matched reserve/inbound histories could support a separately labeled reconstruction if snapshots cannot be recovered. Restoration of the Google archive/native report access is needed before that route can be evaluated. No new access grants, credential changes, external messages or commercial changes were made.

VALIDATION
Unique child/day keys; all 21 dates per child; every original in-scope raw SKU row retained; physical-FNSKU duplicate check; exact B08KQHRDDG example; no OOS=N without positive observed stock; no OOS=Y with missing linked SKU; unknown whole-marketplace dates preserved. Original data files retained unchanged. Raw recovery responses and build script saved under revision2/.
