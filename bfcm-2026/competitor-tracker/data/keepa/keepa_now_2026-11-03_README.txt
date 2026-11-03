KEEPA "NOW" PULL - BFCM 2026 competitor tracker
Generated 2026-11-03 from the ecotero command center MCP, tool keepa_history (read-only).

CALLS
- Parameters on every call: from 2026-10-20, to 2026-11-03 (Eastern days), granularity daily,
  metrics BUY_BOX, NEW, LISTPRICE, LIGHTNING_DEAL, PRIME_EXCL, COUPON, SALES, RATING, COUNT_REVIEWS.
- US: 316 competitor child ASINs (scratchpad trk/us_children.txt) in 16 batches of up to 20; 16 calls, all succeeded first time.
- CA: 68 competitor child ASINs (scratchpad trk/ca_children.txt) in 4 batches; 5 calls (batch 4 repeated once to confirm the result; identical). All succeeded.
- Also one keepa_tracked call (marketplace CA, source auto) to confirm the CA gap: it returned 0 rows,
  with the note "in CA only ASINs enrolled for that marketplace are tracked".

FILES
- keepa_now_us_2026-11-03.csv / keepa_now_ca_2026-11-03.csv: long format, columns asin,date,metric,value,value2.
  value is blank where Keepa returned null (Keepa -1: no offer, no deal running, etc.). A null is never written as 0.
  value2 is BUY_BOX shipping, or COUPON Subscribe & Save coupon; blank for the other metrics.
  COUPON value: positive = amount off in currency, negative = percent off, 0 = no coupon (a real 0 from Keepa).
  Prices in USD (US) / CAD (CA). SALES is root sales rank (lower is better).
  When Keepa returned an empty list for a metric (no history at all for that ASIN), no rows are written for it;
  see empty_metrics in the coverage file.
- keepa_now_us_2026-11-03_coverage.csv / keepa_now_ca_2026-11-03_coverage.csv: one row per requested ASIN.
  tracked = yes/no, taken from Keepa's not_tracked list. last_price_date = last date in the window with a non-null
  BUY_BOX or NEW value (last_buy_box_date and last_new_date are given separately). has_nov2_or_nov3_price = yes when
  last_price_date is 2026-11-02 or 2026-11-03. Also gives batch, brand, parent_asin and empty_metrics.

COUNTS
US: 164 tracked, 152 not tracked (of 316). 20265 data rows, of which 4222 have a blank (null) value.
  Tracked ASINs with a BUY_BOX or NEW price on Nov 2 or Nov 3: 138 (137 have one on Nov 3).
  Tracked but no BUY_BOX/NEW price anywhere in the window: 23.
  Tracked, last price earlier than Nov 2: 2026-10-21: 1, 2026-10-26: 1, 2026-11-01: 1, 2026-11-02: 1.
  Metrics with no history at all (ASIN count): LIGHTNING_DEAL 76, COUPON 30, PRIME_EXCL 19.
CA: 0 tracked, 68 not tracked. No data rows; the CA CSV has the header only.

GAPS AND CAVEATS
- CA: none of the 68 CA children are tracked by the command center's Keepa Data Hub (keepa_tracked CA returns
  nothing). The October CA history in keepa_history_ca*.csv came from a different pull, not this tool.
  CA "now" data needs those ASINs enrolled for CA in the Data Hub, or another Keepa source.
- US: 152 of 316 children are not tracked. Likely cause (not verified per ASIN): the Data Hub auto-tracks only each rival's
  seed ASIN, not its whole variation family, so non-seed children come back as not_tracked.
- Daily granularity carries the last recorded value forward. A Nov 3 value can be a carried-forward reading
  rather than a fresh observation on Nov 3. The window ends today, so Nov 3 is a partial day.
- No parent or redirect substitution. Values are exactly as returned by Keepa.
