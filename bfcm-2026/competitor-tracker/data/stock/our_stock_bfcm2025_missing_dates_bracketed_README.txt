BFCM 2025 STOCK: THE 6 MISSING SNAPSHOT DATES, BRACKETED (built 2026-10-14)
Missing dates (no DataHub snapshot, see revision2 README): US 2025-11-26, 2025-11-27, 2025-12-01; CA 2025-11-24, 2025-11-29, 2025-11-30.

One row per marketplace + child ASIN + missing date (3,936 rows), from our_stock_bfcm2025_by_child_asin.csv.
prev_* / next_* = nearest observed snapshot before / after the gap (out_of_stock flag and FBA available units; observed subtotal used when the SKU set is partial).

bracket:
- bracketed_in_stock: in stock with >= 20 available on both sides of the gap (US 2,271; CA 1,081). Very likely in stock on the missing date.
- bracketed_oos: out of stock on both sides (US 43; CA 4). Very likely out of stock.
- ambiguous: anything else, i.e. low stock (<20), a stock-out on one side, or an unknown side (US 215; CA 322; 201 children). Needs sales evidence.

This is INFERRED, not a stock reading. Actual stock columns stay blank for these dates; never cite these as observed units.

SellerBoard check (2026-10-14): the dashboard "Stock" field is today's stock, not historical (B08KQHRDDG reads 2,210 for both 2025-11-22 and 2025-12-01, against DataHub's 1,721 on 2025-11-22). So SellerBoard cannot fill the stock numbers. It does carry daily units sold per child, which is used as in-stock evidence for the ambiguous rows.
