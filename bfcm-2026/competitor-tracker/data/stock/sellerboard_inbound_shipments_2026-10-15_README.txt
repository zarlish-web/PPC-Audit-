SellerBoard inbound FBA shipments - pulled 2026-10-15 13:52 UTC (read-only)
File: sellerboard_inbound_shipments_2026-10-15.csv  (one row per shipment x SKU)
Account: Ecotero (c81e7dde-c826-11e9-ab35-e4434b2f1e00)

HOW IT WAS PULLED
- mcp__Sellerborad__fba_shipments, count=8, one status at a time: WORKING (0 plans), READY_TO_SHIP (2),
  SHIPPED (7), IN_TRANSIT (5), DELIVERED (1), CHECKED_IN (0), RECEIVING (25, pages 1-4), plus ACTIVE (60 plans,
  pages 1-8). ACTIVE works but only returns open "working" plans: 57 of the 60 are stale draft plans with NO
  shipments (dated 2024-05 to 2026-08) and 3 hold 7 READY_TO_SHIP shipments. Shipped/in-transit/receiving plans are
  NOT in ACTIVE, which is why every status was also queried.
- The status filter applies to the nested shipments, so one plan can appear under several statuses with different
  shipments (e.g. plan "FBA STA (2026-08-28 10:04)" has IN_TRANSIT, RECEIVING and READY_TO_SHIP shipments).
  Unique nested shipments (shipments[].id) across all calls: 78.
- mcp__Sellerborad__fba_shipment was called for 8 of the 78 shipments, covering every status
  (SHIPPED FBA19RSBKFGZ; IN_TRANSIT FBA19P55072C, FBA19NP2BSG0, FBA19N7XSBR9, FBA19N7WSG18; DELIVERED FBA19KFX24C6;
  READY_TO_SHIP FBA19HT4BHCP; RECEIVING FBA19MDGSL3P). Each detail response is 20-60k characters, so calling it
  for all 78 would not fit in one working session. For those 8, every per-SKU units/UnitsReceived value, the status
  and the FBA number match the nested data in fba_shipments exactly (0 mismatches). The detail
  response has no field that the list lacks except closingDate, which was empty (0001-01-01) in all 8. Rows for the
  other 70 shipments come from fba_shipments shipments[].products (column data_source says which).

ETA / EXPECTED ARRIVAL
- NO ETA FIELD EXISTS in either tool. Fields returned by fba_shipment.result: OldFBA, id, date, number, Address,
  FromAddress, LabelType, PackingType, status, closingDate, Comment, AWD, sort_center, products[], printOptions.
  Fields on fba_shipments nested shipments: id, amazonId, sort_center, name, status, last_update_date, date,
  requiresAttention, Units, UnitsReceived, comment, AWD, PurchaseOrders, products[].
  There is no estimated arrival, delivery window or shipped date anywhere.
- eta, eta_source_field and shipped_date are therefore BLANK on every row; nothing was guessed. closing_date_utc is
  blank because closingDate was the null value -62135596800 (0001-01-01).
- Shipments without an ETA: all 78:
  FBA19HMX4HB0 (RECEIVING)
  FBA19HT4BHCP (READY_TO_SHIP)
  FBA19J4C00BN (RECEIVING)
  FBA19J4KYZX7 (RECEIVING)
  FBA19JDZKH56 (RECEIVING)
  FBA19JF0QLRY (RECEIVING)
  FBA19JN2Y9DR (RECEIVING)
  FBA19JV78FDM (RECEIVING)
  FBA19JVC0PQT (RECEIVING)
  FBA19JY3ZHW1 (RECEIVING)
  FBA19JY50HC5 (RECEIVING)
  FBA19KFX24C6 (DELIVERED)
  FBA19KFX3MVH (RECEIVING)
  FBA19KFXL40C (RECEIVING)
  FBA19KFZ7GP9 (RECEIVING)
  FBA19KG0QWDY (RECEIVING)
  FBA19KGF9QJN (SHIPPED)
  FBA19L31XWPR (RECEIVING)
  FBA19LC3BT3C (RECEIVING)
  FBA19LFYZTX8 (RECEIVING)
  FBA19LFZ1G3D (RECEIVING)
  FBA19LFZW0KV (RECEIVING)
  FBA19LG08Q1X (RECEIVING)
  FBA19LG2R10F (RECEIVING)
  FBA19LNJGNPQ (RECEIVING)
  FBA19LNL8KBZ (RECEIVING)
  FBA19LNLC0KK (RECEIVING)
  FBA19LNNN07V (RECEIVING)
  FBA19LNP787N (RECEIVING)
  FBA19LNPQH41 (RECEIVING)
  FBA19LP4SKXM (IN_TRANSIT)
  FBA19M1451NC (RECEIVING)
  FBA19M151HCM (RECEIVING)
  FBA19M16FS2J (RECEIVING)
  FBA19M1BX1SX (RECEIVING)
  FBA19MDGSL3P (RECEIVING)
  FBA19MDXQD7C (RECEIVING)
  FBA19MR6P408 (RECEIVING)
  FBA19MR798TN (RECEIVING)
  FBA19MR7ZMK6 (RECEIVING)
  FBA19MR9TT8D (RECEIVING)
  FBA19MRB64ZM (RECEIVING)
  FBA19MRBDTTW (RECEIVING)
  FBA19MV0YVFX (SHIPPED)
  FBA19N7RP6W7 (IN_TRANSIT)
  FBA19N7RQF4Q (READY_TO_SHIP)
  FBA19N7VGQ1C (RECEIVING)
  FBA19N7VTCHW (RECEIVING)
  FBA19N7WSG18 (IN_TRANSIT)
  FBA19N7XSBR9 (IN_TRANSIT)
  FBA19N82086K (READY_TO_SHIP)
  FBA19NP2BSG0 (IN_TRANSIT)
  FBA19P55072C (IN_TRANSIT)
  FBA19P570K3X (RECEIVING)
  FBA19P57BDB6 (RECEIVING)
  FBA19P57J59L (RECEIVING)
  FBA19P58DHV4 (RECEIVING)
  FBA19P58G37R (RECEIVING)
  FBA19P5HJ4RK (RECEIVING)
  FBA19QLJ0ZP4 (SHIPPED)
  FBA19QLJLR1F (SHIPPED)
  FBA19QLK9CYH (SHIPPED)
  FBA19QLKCVBW (SHIPPED)
  FBA19QLKHC6Q (SHIPPED)
  FBA19QLVD3FK (SHIPPED)
  FBA19R4G23HZ (SHIPPED)
  FBA19RRY5FBL (SHIPPED)
  FBA19RRY6QFT (SHIPPED)
  FBA19RRYCGHJ (SHIPPED)
  FBA19RS0N5K2 (SHIPPED)
  FBA19RS1HC4F (SHIPPED)
  FBA19RSBKFGZ (SHIPPED)
  FBA19STRJMC3 (READY_TO_SHIP)
  FBA19STYQSF4 (READY_TO_SHIP)
  FBA19STZ9LHZ (READY_TO_SHIP)
  FBA19SV1CLVT (READY_TO_SHIP)
  FBA19SV47PX1 (READY_TO_SHIP)
  FBA19SV5KWMR (READY_TO_SHIP)

COLUMNS
- shipment_id = Amazon FBA number (amazonId / detail "number"); shipment_internal_id = SellerBoard shipments[].id.
- plan_id / plan_number / plan_status = the parent shipping plan row (wf... id). Plan status is "SHIPPED" for most
  plans even when the nested shipment is RECEIVING etc.; use the per-shipment status column.
- status = per-shipment status (detail status where fetched, else the nested status).
- destination_fc = sort_center (verbatim). created_date_utc = shipment "date"; plan_created_date_utc = plan "date";
  last_update_date_utc = shipment last_update_date (Unix seconds converted to UTC).
- marketplace_inferred: NOT returned by the API. Set to Amazon.ca when every destination FC code starts with "Y"
  (YYZ7, YVR4, YYC4, YHM1, YEG2, YXU1 are Canadian FCs) and Amazon.com otherwise (XYY4 and RYY2 do not start
  with Y, so they are Amazon.com). This is an inference from the FC code. Treat it as a label, not API data.
- units_shipped / units_received = Units / UnitsReceived (verbatim).
- units_still_inbound_calc = max(units_shipped - units_received, 0). This is computed, not returned by the API.
  units_over_received = received - shipped where received > shipped (31 rows, e.g. a SKU with
  Units 0 and UnitsReceived 2 in FBA19HT4BHCP).
- inv_detail_* = the matching entry (same FBA id + SKU) in the inventory row's SentToFBA_Details, verbatim
  (Inbound/Shipped/Received/ShipmentStatus). Blank when the inventory details do not list that shipment/SKU.
  The ShipmentStatus there is often stale (READY_TO_SHIP for shipments that are now SHIPPED/IN_TRANSIT).

TOTALS (still_inbound_calc by inferred marketplace and status)
  Amazon.com  READY_TO_SHIP  shipments=8   units_shipped=12448  units_received=504    still_inbound_calc=11944
  Amazon.com  SHIPPED        shipments=11  units_shipped=9464   units_received=0      still_inbound_calc=9464
  Amazon.com  IN_TRANSIT     shipments=5   units_shipped=4292   units_received=0      still_inbound_calc=4292
  Amazon.com  DELIVERED      shipments=1   units_shipped=180    units_received=0      still_inbound_calc=180
  Amazon.com  RECEIVING      shipments=39  units_shipped=28024  units_received=27906  still_inbound_calc=233
  Amazon.ca   READY_TO_SHIP  shipments=1   units_shipped=464    units_received=410    still_inbound_calc=56
  Amazon.ca   SHIPPED        shipments=4   units_shipped=6272   units_received=0      still_inbound_calc=6272
  Amazon.ca   IN_TRANSIT     shipments=1   units_shipped=1164   units_received=0      still_inbound_calc=1164
  Amazon.ca   RECEIVING      shipments=8   units_shipped=5054   units_received=4990   still_inbound_calc=82
  Amazon.com total still inbound (calc) = 26113  (excluding READY_TO_SHIP: 14169)
  Amazon.ca  total still inbound (calc) = 7574  (excluding READY_TO_SHIP: 7518)

AMBIGUITIES
- FBA19N7RQF4Q (ITX3) and FBA19HT4BHCP (YYC4) are READY_TO_SHIP in SellerBoard but already show 504 and 410 units
  received. The status looks stale; the units are reported as returned.
- The 8 READY_TO_SHIP shipments created 2026-08-28 to 2026-10-12 (FBA19N82086K, FBA19SV5KWMR, FBA19STZ9LHZ,
  FBA19STRJMC3, FBA19SV47PX1, FBA19SV1CLVT, FBA19STYQSF4, plus FBA19N7RQF4Q) have not left yet, as far as
  SellerBoard knows.
- FBA19KFX24C6 is DELIVERED with 0 of 180 units received.
