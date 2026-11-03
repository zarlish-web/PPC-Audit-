SellerBoard stock / inbound / price pull for BFCM 2026 competitor tracker - 2026-11-03 15:01 UTC (data as of 2026-11-03)
All data read-only from the SellerBoard MCP (mcp__Sellerborad__*), account Ecotero (c81e7dde-c826-11e9-ab35-e4434b2f1e00).
Nothing was changed in SellerBoard. Every number was parsed with Python from the saved tool results; nothing was retyped.
Same method, filters, columns and rules as the 2026-10-15 pull (see sellerboard_stock_2026-10-15_README.txt and
sellerboard_inbound_shipments_2026-10-15_README.txt). Helper scripts: /tmp/claude-0/-home-user-PPC-Audit-/51b9bd0e-5fdd-5e9c-87d4-612ed5188e17/scratchpad/sbpull/

FILES
1. stock/sellerboard_inventory_2026-11-03.csv          2957 rows (one per FNSKU row of mcp__Sellerborad__inventory)
2. stock/sellerboard_inbound_shipments_2026-11-03.csv  2628 rows (one per FBA shipment x SKU), 62 shipments
3. stock/sellerboard_shipment_status_2026-11-03.csv    62 rows (one per shipment; columns as the 2026-10-27 file)
4. sellerboard/US_prices_2026-11-03.csv                271 rows (one per ASIN x SKU from mcp__Sellerborad__products)
5. stock/sellerboard_stock_2026-11-03_README.txt       this file

1) INVENTORY
Pulled: inventory, account Ecotero, channel FBA, count 35, show_out_of_stock true, sort name asc, one marketplace at a time.
- Amazon.com: API total 2178, unique rows received 2178 (duplicates across pages: 0), Amazon.Found rows dropped 63 -> 2115 rows in the CSV.
- Amazon.ca: API total 845, unique rows received 845 (duplicates across pages: 0), Amazon.Found rows dropped 3 -> 842 rows in the CSV.
- Drop rule (unchanged): SKU starts with "Amazon.Found." AND every stock field is 0 (FBAStock, OnHand, OnHandReserve, OnHandStock,
  Reserved, reserved_*, SentToFBA, FBAPrepStock, Ordered, *AWD, prep_center_1-4). Amazon.Found rows holding stock are kept (1 kept).
- Inspiratek: skipped, as instructed. No row had hasMoreChildren=true; every row is type "fnsku".
- Unique rows = API total in both marketplaces, so this time no paging tie glitch (duplicate/missing row) occurred.

TOTALS CHECK (sum of CSV columns vs SellerBoard account summary details.fba_fbm.units in the same responses)
- Amazon.com: fba_stock 75627 (summary 75627), on_hand 79533 (summary 79533), reserved 4493 (summary 4493), sent_to_fba 28348 (summary 28348)  -> ALL MATCH
    stock_awd 0, inbound_awd 0, fba_prep_stock 0, ordered 0
- Amazon.ca: fba_stock 12923 (summary 12923), on_hand 15556 (summary 15556), reserved 2677 (summary 2677), sent_to_fba 4485 (summary 4485)  -> ALL MATCH
    stock_awd 0, inbound_awd 0, fba_prep_stock 0, ordered 0
- Every page of a marketplace returned the identical summary, so the summary is a single consistent snapshot.
- Column meanings are unchanged (reserved = FC transfers + FC processing only; sent_to_fba_details is product-level, not
  marketplace-level; recommended_ship_in_date blank where SellerBoard returned 0001-01-01; 2151 rows).

2) INBOUND SHIPMENTS (same logic as 2026-10-15)
Pulled: fba_shipments, count 8, one status at a time, every page:
  WORKING        total 0 (plans), pages [1]
  READY_TO_SHIP  total 3 (plans), pages [1]
  SHIPPED        total 10 (plans), pages [1, 2]
  IN_TRANSIT     total 2 (plans), pages [1]
  DELIVERED      total 0 (plans), pages [1]
  CHECKED_IN     total 0 (plans), pages [1]
  RECEIVING      total 13 (plans), pages [1, 2]
  ACTIVE         total 59 (plans), pages [1, 2, 3, 4, 5, 6, 7, 8]
  ACTIVE again returned mostly stale draft plans with no shipments; it also holds 6 READY_TO_SHIP shipments that the
  READY_TO_SHIP query did not return (Plan #330 . US x5 and FBA19VGNWM6M), which is why ACTIVE is still queried.
- Unique nested shipments: 62 (53 Amazon.com, 9 Amazon.ca); 2628 shipment x SKU rows (2433 .com / 195 .ca).
- fba_shipment (detail) fetched for 5 shipments (FBA19RSBKFGZ IN_TRANSIT, FBA19QLVD3FK READY_TO_SHIP, FBA19VGMD2JD SHIPPED,
  FBA19P58G37R RECEIVING, FBA19VY8LTYV READY_TO_SHIP in an ACTIVE plan). Mismatches vs list data: 0. Other rows come from the nested list data (column data_source).
- marketplace_inferred: same FC-code rule (all FCs start with "Y" -> Amazon.ca, else Amazon.com). An inference, not API data.
- NO ETA field exists in either tool (eta, eta_source_field, shipped_date blank on every row; closing_date_utc blank = 0001-01-01).
- units_over_received rows: 28. Unresolved product ids (no SKU): 0.
- inv_detail_* matched on 1833 of 2628 rows; their ShipmentStatus is stale as before.

OPEN SHIPMENTS BY STATUS (shipments / units_shipped / units_received / units_still_inbound_calc)
  Amazon.ca   IN_TRANSIT       1 shipments  shipped    688  received      0  still_inbound_calc    688
  Amazon.ca   READY_TO_SHIP    2 shipments  shipped   2862  received   2522  still_inbound_calc    362
  Amazon.ca   RECEIVING        3 shipments  shipped   1548  received   1554  still_inbound_calc      1
  Amazon.ca   SHIPPED          3 shipments  shipped   3334  received      0  still_inbound_calc   3334
  Amazon.com  IN_TRANSIT       1 shipments  shipped    516  received      0  still_inbound_calc    516
  Amazon.com  READY_TO_SHIP    9 shipments  shipped   5932  received   3125  still_inbound_calc   2830
  Amazon.com  RECEIVING       19 shipments  shipped  13584  received  13515  still_inbound_calc    134
  Amazon.com  SHIPPED         24 shipments  shipped  26348  received      0  still_inbound_calc  26348
  Amazon.com total still inbound (calc) = 29828 (excluding READY_TO_SHIP: 26998). SellerBoard SentToFBA for comparison = 28348.
  Amazon.ca total still inbound (calc) = 4385 (excluding READY_TO_SHIP: 4023). SellerBoard SentToFBA for comparison = 4485.
  By status (all marketplaces): IN_TRANSIT 2, READY_TO_SHIP 11, RECEIVING 22, SHIPPED 27

3) SHIPMENT STATUS (one row per shipment)
- Columns as in the 2026-10-27 file: units/units_received = shipment Units/UnitsReceived, fc = sort_center, plan = parent plan
  number, updated = shipment last_update_date (Unix seconds, verbatim). Sorted by shipment_id.
- It lists every open shipment found (62). The 10-27 file had 47 rows and left out some long-running RECEIVING
  shipments; those are included here. plan is filled from the API for every row (blank in a few 10-27 rows).
- In the 10-27 file but no longer open (6): FBA19MDXQD7C (CLOSED), FBA19MR6P408 (CLOSED), FBA19MR798TN (CLOSED), FBA19MR9TT8D (CLOSED), FBA19MRB64ZM (CLOSED), FBA19MRBDTTW (CLOSED).
  (Checked against CLOSED pages 1-2 sorted by last_update_date desc; 852 CLOSED plans exist, only 2 pages were read.)
- New since 10-27 (21): FBA19J4C00BN RECEIVING, FBA19J4KYZX7 RECEIVING, FBA19JN2Y9DR RECEIVING, FBA19KFX24C6 RECEIVING, FBA19KFZ7GP9 RECEIVING, FBA19KG0QWDY RECEIVING, FBA19LNL8KBZ RECEIVING, FBA19LNPQH41 RECEIVING, FBA19LP4SKXM RECEIVING, FBA19VGLBJ6C SHIPPED, FBA19VGMD2JD SHIPPED, FBA19VGMKQ5L SHIPPED, FBA19VGMMRPM SHIPPED, FBA19VGN64ZP SHIPPED, FBA19VGNWM6M READY_TO_SHIP, FBA19VGPP9WR SHIPPED, FBA19VY5H8ZX READY_TO_SHIP, FBA19VY72JCZ READY_TO_SHIP, FBA19VY75V99 READY_TO_SHIP, FBA19VY7MPXC READY_TO_SHIP, FBA19VY8LTYV READY_TO_SHIP.
- Status changes vs 10-27: FBA19N7WSG18 IN_TRANSIT->RECEIVING, FBA19N7XSBR9 RECEIVING->READY_TO_SHIP, FBA19N82086K IN_TRANSIT->RECEIVING, FBA19QLKCVBW RECEIVING->READY_TO_SHIP, FBA19R4G23HZ SHIPPED->IN_TRANSIT, FBA19RSBKFGZ SHIPPED->IN_TRANSIT.
- PROBLEM: units_received went DOWN vs 10-27 on 10 shipments (FBA19N7RP6W7 1217->1205, FBA19N7RQF4Q 1199->1193, FBA19N7VGQ1C 1195->1189, FBA19N7VTCHW 970->958, FBA19N7XSBR9 592->585, FBA19P55072C 1003->1002, FBA19P58DHV4 948->947, FBA19P58G37R 324->322, FBA19QLJ0ZP4 895->888, FBA19QLKCVBW 934->928).
  Two shipments moved backwards from RECEIVING to READY_TO_SHIP (see list above). This is how SellerBoard reports them today;
  treat SellerBoard shipment status as unreliable/stale, especially READY_TO_SHIP shipments that already show units received.

4) US PRICES
- Source identified from the 10-14 pull scripts: mcp__Sellerborad__products with the products filter = ASIN lists (35 per call,
  paged when total > 35). Columns map: asin=ASIN, sku=SKU, price=Price, cost=Cost, fba_fees=FBAFees, referral_fee=ReferralFee,
  sales_velocity=SalesVelocity, hide=Hide (true/false), channel=Channel. Values verbatim. All rows come back as Amazon.com listings.
- Same 248-ASIN universe as 10-14 (8 batches) -> 256 rows (10-14 had 256): no SKU added or removed.
- PLUS 15 extra rows (at the end of the file) for the 10 White bamboo ASINs (BAMBOO-*-WHITE*), which were NOT in the
  10-14 file. 5 of the 15 are Amazon.Found.* placeholder rows that SellerBoard returns with their own (different) price.
- All 258 requested ASINs came back. Rows with a non-zero price: 252 of 271 (239 real SKUs + 13 Amazon.Found rows). Price 0: 19 rows (cost, FBA fee and referral fee are also 0 on all of them; mostly new SKUs).
- Cross-check: products Price equals inventory "price" for every SKU present in both (mismatches: 0).
- Price changed vs 10-14 (same ASIN+SKU): 20 SKUs:
    B08KQJ61T7 BAMBOO-KING-TAUPE: 79.99 -> 94.99
    B0BZQ1FBJ9 BAMBOO-QUEEN-BLACK: 74.99 -> 109.99
    B08KQJBRKM BAMBOO-FULL-TAUPE: 64.99 -> 74.99
    B08KQHSWSJ BAMBOO-CALIFKING-LIGHTBLUE: 84.99 -> 94.99
    B0CQ33KG5X BAMBOO-KING-CREME-6PCS: 89.99 -> 99.99
    B0CQ311KCT BAMBOO-FULL-TAUPE-6PCS: 74.99 -> 79.99
    B0CQ2ZSDMN BAMBOO-FULL-NAVYBLUE-6PCS: 74.99 -> 79.99
    B0CQ32JTTK BAMBOO-CALIFKING-CHARCOAL-6PCS: 84.99 -> 89.99
    B0CQ33BH1K BAMBOO-TWIN-LIGHT PINK-6PCS: 87.99 -> 69.99
    B0CRHYS5KT BAMBOO-FULL-BURGUNDY-NEW: 64.99 -> 74.99
    B0CQ32CNNX BAMBOO-CALIFKING-PURPLE-6PCS: 84.99 -> 99.99
    B0CQ31V52K BAMBOO-CALIFKING-LIGHTOLIVE-6PCS: 84.99 -> 99.99
    B0CQ32LWVD BAMBOO-TWIN-BURGUNDY-6PCS: 59.99 -> 69.99
    B0F7LJRWB6 SL-CLG-PC-LIGHT-GREY-QUEEN-2PCS: 19.99 -> 21.99
    B0F7LLM71K SL-CLG-PC-LIGHT-GREY-STANDARD-2PCS: 18.99 -> 20.99
    B0F7LLBQH3 SL-CLG-PC-WHITE-KING-2PCS: 19.99 -> 23.99
    B0DDTZCKGQ SS-BAMBOO-CREME-QUEEN-6PCS: 59.99 -> 64.99
    B0F7M3YTBN SL-COOLING-FITTED-TWIN-LIGHT-GREY: 24.99 -> 32.99
    B0F7M6WTWR SL-COOLING-FITTED-TWIN-GRAPHITE: 24.99 -> 32.99
    B0HCZLGTWV BAMBOO-FULL-LIGHTBLUE-6PC: 0 -> 79.99
  Cost / FBA fee / referral fee changed on 48 rows of the same 256 (not listed here; compare the files).
- White bamboo (BAMBOO-*-WHITE*): no 10-14 price exists. Current price, and for reference the 10-15 inventory price field:
    B0CQ2XQF9N BAMBOO-KING-WHITE-6PCS: now 94.99 (10-15 inventory 99.99)
    B08KQHRDDG BAMBOO-KING-WHITE: now 89.99 (10-15 inventory 94.99)
    B0CQ2ZWGNQ BAMBOO-QUEEN-WHITE-6PCS: now 89.99 (10-15 inventory 94.99)
    B08KQJGM74 BAMBOO-QUEEN-WHITE: now 84.99 (10-15 inventory 89.99)
    B08KQKBM4Q BAMBOO-TWIN-WHITE: now 59.99 (10-15 inventory 64.99)
    B0CQ31Q559 BAMBOO-FULL-WHITE-6PCS: now 74.99 (10-15 inventory 79.99)
    B08KQJV49M BAMBOO-FULL-WHITE: now 69.99 (10-15 inventory 64.99)
    B08KQKQ44M BAMBOO-CALIFKING-WHITE: now 89.99 (10-15 inventory 94.99)
    B0CQ2ZYZJT BAMBOO-CALIFKING-WHITE-6PCS: now 94.99 (10-15 inventory 99.99)
    B0CQ34D2QS BAMBOO-TWIN-WHITE-6PCS: now 64.99 (10-15 inventory 64.99)

PROBLEMS / GAPS / FIXES
- 5 inventory calls (Amazon.com pages 52-56) failed with Cloudflare 502 Bad Gateway; re-run after a 65 s back-off, all succeeded.
- 6 inventory results were lost because two parallel calls saved to the same tool-result file name (.com 59/60, .ca 1/2 and 19/20); all six pages were re-fetched one at a time. Final page coverage is complete for both marketplaces.
- No call returned status "preparing"; no 429 occurred.
- No ETA / shipped date exists in SellerBoard for any shipment.
- CLOSED shipments were not part of the 10-15 logic; only 2 pages of 852 CLOSED plans were read, to explain shipments that left the open list.
- White bamboo SKUs cannot be compared to 10-14 because the 10-14 price file never contained them.
