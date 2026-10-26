# Sellerboard account settings - Ecotero (bedding account)
account_id: c81e7dde-c826-11e9-ab35-e4434b2f1e00 | currency: USD | marketplaces connected: Amazon.com, Amazon.ca, Amazon.com.mx, Amazon.com.br
Pulled 2026-10-26 via account_settings (read-only).

## VAT / tax
- Account for VAT (vat_use): false (sales are gross; no VAT deduction). vat_date 2017-12-31 (inactive)
- EU OSS: false; Amazon VCS: false; Amazon-fees-include-recoverable-VAT: false
- Add local VAT to advertising costs: false (rate 0)
- Treat TCS as recoverable: false; Swiss VAT exclusion: false

## Margin / COGS
- Use net sales for margin calculation: false (margin = net profit / gross sales)
- COGS for oversold FIFO batches: last_batch_price (oversold units costed at the last batch cost)
- principal_only (hide FBA shipping chargeback & giftwrap from sales and fees; no profit effect): true
- Ignore multi-channel (MCF) orders and their COGS: true
- Products grid shows CostPeriod = "By period" (cost entered per date period, not FIFO batches) for the bedding SKUs sampled.

## Shipping
- Use highest shipping cost per order: false

## Refunds
- Assume pending returns are unsellable (realistic_refunds): true -> COGS of a returned unit is lost until the return arrives and is graded sellable; then corrected.
- Ignore deferred refunds until released: false -> deferred refunds show immediately and later move to release date (past months can shift retroactively).
- Restocking fee by condition: false

## Pick & pack
- Price per package 0; price per item 0; tiered picking off (no 3PL pick/pack cost modelled)

## Amortization
- Storage fees applied to: charge_month (monthly storage/LTSF lands in the month Amazon charges it, i.e. usually the month after the stock was stored)
- Amortize Amazon fees daily: false (fee lumps land on charge dates)
- Auto write-off prep-center stock when shipping to FBA: false

## Cashflow / retention
- Cashflow payouts counted from: 2019-05-01
- Data retention: long, 120 months
- Walmart / eBay connected: false / false
