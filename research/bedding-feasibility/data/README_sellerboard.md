# Sellerboard extract – bedding feasibility study (pulled 2026-10-26)

Source: Sellerboard MCP (read-only tools only: list_accounts, account_settings, products, search_products, dashboard_period, dashboard_table, inventory, fba_shipments, purchase_orders, suppliers, product_cost_details). Nothing was created or modified; no Amazon reports were created.

**Bedding account = Ecotero** (account_id c81e7dde-c826-11e9-ab35-e4434b2f1e00). Brands seen: DECOLURE (bamboo viscose sheets, satin sheets & fitted sheets, mulberry-silk pillowcases), SLEEPHORIA (cooling sheets/fitted sheets/comforter/pillowcases, quilt, cotton throws), SLEEP SANCTUARY (satin + bamboo sheets – a 4th brand not in the brief), COOLINENS (cooling pillowcases/sheets, launched mid-2026), BAMBOO RESERVE (new bamboo listings). >99% of Ecotero sales are bedding; small non-bedding tail (chair covers, beach towels, curtains, welcome sign) is flagged `is_bedding=0`.
Inspiratek (4ff2aeee-…) holds NO bedding (searches for sheet/bamboo/satin/quilt returned 0) – see "Inspiratek" below.

**Currency: USD for every figure, including amazon.ca** (Sellerboard account currency is USD; CA values are converted by Sellerboard). Costs/fees/ads are negative numbers, as Sellerboard reports them.
**Primary window: YTD 2026 = 2026-01-01 → 2026-10-26** (299 days; includes the partial current day 10-26). Prior-year comparison = 2025-01-01 → 2025-10-26.

## Files
| file | content | window / grain |
|---|---|---|
| sb_settings.md | account_settings for Ecotero (VAT off, COGS/refund/storage logic) | current settings |
| sb_monthly.csv | monthly P&L, rows per month × {amazon.com, amazon.ca, com+ca} | 2023-10 → 2026-10 (Oct-26 = 1–25 Oct, 25 days; `days` column) |
| sb_yoy.csv | account totals + YoY deltas: YTD-2026 vs YTD-2025 (com, ca, com+ca); last 30/90/180/365d vs same window a year earlier (amazon.com); 365d & 90d current for amazon.ca | rolling windows end 2026-10-25 (complete days); YTD ends 2026-10-26 |
| sb_products_ytd2026.csv | child-SKU rows (entry_type product), every row paged: com 1,199 rows, ca 1,073 rows | 2026-01-01 → 2026-10-26 |
| sb_parent_ytd2026.csv | parent-ASIN groups (group_by parent) + a RESIDUAL row per marketplace = child total − listed parents | YTD 2026 |
| sb_parent_365d.csv | same structure as sb_parent_ytd2026.csv | 2025-10-26 → 2026-10-25 |
| sb_products_365d.csv | child rows: com 1,190 of 1,210 (20 zero-sales tail rows came back inline and were not transcribed – they carry $0 sales/units), ca 1,089 of 1,089 | 2025-10-26 → 2026-10-25 |
| sb_products_90d.csv | child rows: com 1,126/1,126, ca 950/950 | 2026-07-28 → 2026-10-25 |
| sb_inventory.csv | inventory tool, in-stock rows (934 rows, all FBA): FBA stock, reserved split, inbound (SentToFBA), AWD, velocity, days of stock, reorder flags, lead-time settings, stock at cost | snapshot 2026-10-26 |
| sb_fba_shipments_12m.csv | 155 FBA shipping plans created 2025-10-26 → 2026-10-26 with nested shipment status/units | 12 months |
| sb_cogs_components.csv | (a) current unit COGS + YTD avg COGS/unit for top-15 bedding SKUs (com & ca); (b) full dated COGS history for BAMBOO-KING-WHITE-6PCS and SATIN-QUEEN-BLACK | see notes |
| sb_scope_other.csv | Ecotero amazon.com.mx / amazon.com.br size (365d, YTD) and Inspiratek totals | 365d / YTD |
| sb_history_annual.csv | Ecotero all-marketplace annual totals 2019–2023-09 (context) | annual |

## Column notes (sb_monthly / sb_yoy)
Sales = gross product sales (principal only; shipping/giftwrap hidden by setting). RefundUnits = units refunded **in the period** (by refund date, not by order date); RefundUnitPct = RefundUnits/Units. RefundCostNet = Sellerboard "ProductRefunds" (refunded principal − refunded referral fee + value of items returned sellable, i.e. the P&L hit); RefundPrincipal = gross refunded amount. Promo = promotional rebates (coupons/deals). Ads = total ad spend; SP=Sponsored Products, SB=Sponsored Brands (HSA), SBV=Sponsored Brands Video, SD=Sponsored Display. AmazonFees = all Amazon fees net of reimbursements; Referral=Commission, FBAFulfil=FBA per-unit fee, Storage=monthly FBA storage, LTSF=long-term storage/overage, OtherAmazonFeesNet = remainder (removals, disposals, inbound convenience/placement, deal/Vine/coupon fees, liquidation proceeds, reimbursements, subscription). COGS = Sellerboard ProductCosts. NetProfit = GrossProfit (no business expenses are entered in Sellerboard: expenses tool empty, Expenses=0). Margin = NetProfit/Sales. ROI as reported (com+ca ROI recomputed as NP/COGS). Sessions/USP = Amazon Business-Report sessions & unit-session %. Residual_check = NetProfit − (Sales+Promo+Ads+Fees+COGS+RefundCostNet) – 0.00 on every row (transcription verified). For amazon.ca months where no storage/LTSF line appeared the field is 0.
Product files: refund_pct_units = refund_units/units; amazon_fees includes storage/LTSF allocated to the SKU; account-level ("notProductLevel") fees such as deal, Vine, coupon, subscription and liquidation fees are NOT in product rows, so Σ product net_profit > account net profit (YTD com +$91.6k gap, ca −$0.1k). unit_cogs_setting = current Cost field; fba_stock/reserved/days_of_stock are the snapshot at pull time.

## Caveats
* Refund timing: refunds are booked on refund date; deferred refunds show immediately (setting `show_only_released_refunds=false`) and pending returns are assumed unsellable (COGS lost until the return is graded) – recent months' refund cost can move.
* COGS: single all-in "COG" element per unit, entered "by period" (weekly/periodic updates; latest entries commented "Command Center CoGS … 30-day sold cost – weekly update pilot"). **No component split (product/freight/duty/prep) exists in Sellerboard**; oversold FIFO units use last batch cost. Example history: BAMBOO-KING-WHITE-6PCS $32.9–33.5 most of 2024-25, spiking to $41–43 May–Jul 2025, back to $33.2 in 2026; SATIN-QUEEN-BLACK $7.7–11.3 range, $10.03 now.
* Suppliers & purchase orders: suppliers tool and purchase_orders tool both return 0 records → no supplier names, PO unit costs or country of manufacture are recorded in Sellerboard. Inventory lead-time fields are a uniform 30 d production / 10 d to prep / 5 d to FBA on every SKU (likely defaults, not real lead times).
* Storage fees are booked in the month Amazon charges them (charge_month), not amortized.
* Recompute drift: Sellerboard recomputes warm slots; repeated pulls of the same window differed by a few dollars (e.g. CA 365d NP −186,477.52 vs −186,481.79). Product pages of one window can come from two warm computes; differences are cents–tens of dollars.
* YTD window includes the partial day 2026-10-26; monthly Oct-2026 rows run 1–25 Oct only.
* Parent files: Sellerboard returned parent groups without children; com YTD lists 90/97 parents (7 zero-sales parents not retrievable because of tie ordering; residual NP −$48.69), ca YTD lists 34/77 parents (remaining 43 small parents = 38 units / $1,577 sales in the residual row). 365d parent file: com lists 68/101 parents (the 33 unlisted are tail parents with 2 units / $64 sales but NP −$2,644, driven by Amazon fees −$2,737 incl. LTSF −$1,279 and storage −$429, in the residual row); ca lists 34/79 (residual 70 units / $3,072 sales / NP +$34).
* FBA plans: 24 plans have no shipments attached (drafts/abandoned STA plans, 22,055 planned units) and one plan is a "TEST — do not ship" plan – excluded from shipped totals.
* Data history: Ecotero's first sales month is 2019-08 (all marketplaces, $609); amazon.com/ca monthly data exists for every month from 2023-10 onward.

## Inspiratek
Inspiratek sells non-bedding consumer goods under the Inspiratek / PuraBella labels: kids' fitness-tracker watches and accessories (bands, chargers), smartwatches, posture correctors, reusable silicone/produce/storage bags and beeswax wraps, blue-light glasses, palm-leaf plates, spy camera, plantar-fasciitis splints, magnetic lashes. It is winding down: last 365 days (2025-10-26→2026-10-25, all marketplaces) sales $6,807 (238 units), net profit −$8,584 — amazon.com $4,405 (NP −$5,169), amazon.ca $2,401 (NP −$3,415), MX/BR the small remainder; prior 365 days $84,901 / NP −$11,241. Not relevant to the bedding study.
