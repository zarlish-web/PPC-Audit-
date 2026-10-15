SellerBoard stock pull for BFCM 2026 competitor tracker - 2026-10-15 13:52 UTC
All data read-only from the SellerBoard MCP (mcp__Sellerborad__*). Nothing was changed in SellerBoard.
Every number was parsed with Python from the saved tool-result JSON (agent transcript + tool-results files).
Nothing was retyped.

FILES (data/stock/)
1. sellerboard_inventory_2026-10-15.csv            - one row per FNSKU row from mcp__Sellerborad__inventory
2. sellerboard_inbound_shipments_2026-10-15.csv    - one row per FBA shipment x SKU (see its own README)
   sellerboard_inbound_shipments_2026-10-15_README.txt
3. sellerboard_purchase_orders_2026-10-15.csv      - header only: 0 purchase orders exist
4. sellerboard_stock_2026-10-15_README.txt         - this file

ROW COUNTS
- Inventory: Ecotero Amazon.com 2113 rows, Ecotero Amazon.ca 833 rows,
  Inspiratek 0 rows (total 2946).
  API totals were Amazon.com 2177 and Amazon.ca 836. 64 (.com) and 3 (.ca)
  rows were dropped because their SKU starts with "Amazon.Found." and every stock field is 0
  (FBAStock, OnHand, OnHandReserve, OnHandStock, Reserved, reserved_*, SentToFBA, FBAPrepStock, Ordered, *AWD,
  prep_center_1-4). Amazon.Found rows that hold any stock were kept.
- Inbound shipments: 2636 rows / 64 shipments to Amazon.com, 302 rows / 14 shipments to
  Amazon.ca (marketplace inferred from FC code; see the inbound README). 78 shipments in total.
- Purchase orders: 0 rows. Status Ordered: total 0. Status Shipped: total 0. No status filter: total 0.
  The account has no purchase orders in SellerBoard, which matches inventory "ordered" = 0 on every row.

TOTALS PER MARKETPLACE (sum of CSV columns; each equals SellerBoard's own account summary in details.fba_fbm.units)
- Amazon.com: fba_stock 70217, on_hand 76216, reserved 11901, sent_to_fba (inbound) 22893
- Amazon.ca : fba_stock 10238, on_hand 11212, reserved 1274, sent_to_fba (inbound) 8062
- Inbound from the shipment file (units_still_inbound_calc): Amazon.com 26113 (14169 excluding
  READY_TO_SHIP), Amazon.ca 7574 (7518 excluding READY_TO_SHIP). These figures do not equal
  SellerBoard's SentToFBA because SellerBoard uses its own attribution. Use sent_to_fba for per-SKU inbound.
- stock_awd, inbound_awd, fba_prep_stock, ordered: 0 in both marketplaces.

WHAT WAS PULLED
- mcp__Sellerborad__inventory, account Ecotero, channel FBA, count 35, show_out_of_stock true, sort name asc:
  Amazon.com pages 1-63 (62x35 + 7 = 2177) and Amazon.ca pages 1-24 (23x35 + 31 = 836). Every call returned
  status "success"; none returned "preparing", and no 429 errors occurred. No row had hasMoreChildren=true, so
  inventory_children was not needed. Every row is type "fnsku".
- Inspiratek (4ff2aeee-...): page 1 only, as instructed. Amazon.com showed 35 of 65 rows; Amazon.ca 6 of 6.
  These are non-bedding Inspiratek items (kids and adult fitness trackers, bands, chargers, smartwatches,
  blue-light glasses, storage bags), plus one DECOLURE row, SCR-BEIGE
  ("DECOLURE Elegant Bathroom Sets with Shower Curtain and Rugs", 0 stock). That row is bathroom decor, not
  bedding, so it was excluded. Result: 0 Inspiratek rows in the CSV. Inspiratek .com page 2 (rows 36-65) were
  not checked.
- fba_shipments / fba_shipment / purchase_orders: see above and the inbound README.

ERRORS / FAILED PAGES / FIXES
- No call failed.
- Paging glitch: sorting by name has ties, so one Amazon.com row (SATIN-TWIN-BLACK, X002IU4X0T) came back on
  both page 35 and page 36. Another row with the same product name, GR-699U-0OJO (FNSKU B0839L7PJL, "DECOLURE
  Satin Sheets Twin Size | Softer Than Silk | Luxury 3 Pc Bed Set", all stock 0), was missing from the paged set.
  It was recovered with an extra inventory call using the same filters plus search_query "Satin Sheets Twin Size |
  Softer Than Silk | Luxury 3 Pc Bed Set". The duplicate was dropped. Unique Amazon.com rows = 2177 = API total.
- fba_shipment (detail) was fetched for only 8 of 78 shipments, for response size. See the inbound README.
  The 8 details match the list data exactly, and no ETA field exists in either.

COLUMN NOTES / AMBIGUITIES
- Values are verbatim. Blank means the API returned nothing. Zeros are real API zeros.
  recommended_ship_in_date is blank where SellerBoard returned its null date 0001-01-01T00:00:00 (2147 rows).
- reserved = inventory "Reserved". Per the tool docs it covers only FC transfers + FC processing. Customer-order
  reservations are in reserved_customerorders.
- sales_velocity = SalesVelocity (units/day). running_out_of_stock and time_to_reorder are flag strings
  (NO/SOON/YES), not dates.
- price and cost are in each marketplace's listing currency as SellerBoard returns them (USD for .com, CAD for .ca
  presumably). The API does not state the currency.
- sent_to_fba_details holds compact JSON of SentToFBA_Details. These lists are product-level, NOT
  marketplace-level: the same SKU shows an identical details list on its .com and .ca rows, and the lists include
  shipments to both countries (sum of details Inbound: .com rows 34013, .ca rows 30909, vs SentToFBA 22893 / 8062).
  Use sent_to_fba for marketplace inbound. The details only tell you which shipment and FC the units are in.
  Their ShipmentStatus is often stale (mostly READY_TO_SHIP).
- Several .com rows have the name " Name not found" (verbatim from SellerBoard).
- product_id (SellerBoard composite ProductID) and product_guid were added at the end for joining. They are extra
  columns beyond the ones requested.
