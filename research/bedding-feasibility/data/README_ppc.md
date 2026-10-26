# PPC and unit-economics extract (ecotero-command-center, read-only)

Pulled 2026-10-26, using read-only `ecotero-command-center` tools only. Nothing was staged or written back to the server.
Build scripts are in `../ppc_a497/` (`extract_a497.py` plus one `build_*.py` per file). Raw tool payloads are in `../ppc_a497/raw/`.

## Windows

- **YTD2026 is the primary window**: 2026-01-01 → 2026-10-26 (299 days). Its "prior" row is the 299 days before it (2025-03-08 → 2025-12-31).
- Presets are also kept, each ending 2026-10-26:
  - 30d starts 2026-09-27.
  - 90d starts 2026-07-29.
  - 180d starts 2026-04-30.
  - Each preset also has an equal-length prior window.
- **October 2026 is a partial month**: 1–26 October, and the 26th itself is a partial day.
- **The last 7 days are still settling.** Sales, orders, CVR and ACoS use 7-day attribution, so 2026-10-20 → 10-26 reads LOW. Only data through 2026-10-19 is settled. Rows touching that period carry `settling_days` or a note.
- Search-term data begins 2025-12-29, so YTD fully covers it.
- SQP market CTR/CVR covers 41 published weeks (2026-01-04 → 2026-10-17).

## Currency

- US figures are in USD.
- CA figures are in CAD. The tool's tiles label CA as "usd"; ignore that label.
- Every file has a `currency` column. Never add US and CA values together without converting.

## Files

| File | Rows | What it is |
|---|---|---|
| economics.csv | 119 | Unit economics as of today, per product × marketplace × size, plus a BLENDED row. See the notes below the table. |
| outliers.csv | 4 | SKUs whose landed cost is >1.6× its size median (HIGH), plus an extra <0.5× check (LOW). |
| ppc_windows.csv | 200 | `ppc_summary` per product × marketplace and per account (US/CA), for YTD2026 and 30/90/180d, current and prior. See the notes below the table. |
| ppc_product_table_ytd.csv | 51 | Full US and CA product tables for YTD, including units, TACoS and spend share. `in_bedding_set` = Y/N; the account row is included. |
| ppc_monthly_2026.csv | 218 | Jan–Oct monthly roll-up from `ppc_daily` (level=product per product × marketplace, plus level=account). Reconciles exactly to the YTD summaries. Includes `first_data_date`. |
| launch_curve.csv | 115 | Weekly rows (Monday weeks) from 2026-01-01 for 73, 69, 70, 48 and 59 US, with `week_index_since_first_data`. |
| launch_events.csv | 56 | Events and deals for the launch products, from `ppc_daily`. |
| perf_split_matchtype_ytd.csv, perf_split_ytd.json | 268 / 25 scopes | `ppc_performance_split` for YTD: total, by match type, by ad product and by objective, plus the account objective table. |
| perf_split_matchtype.csv, perf_split.json | 156 / 14 scopes | The same split for 180d, for the core six products (59, 30, 37, 31, 38, 39) in US and CA, plus account US and CA. |
| syntax_groups.csv | 192 | `ppc_syntax_groups` YTD with market=true. US: 59, 30, 37, 39, 38, 45, 46, 42, 55. CA: 30, 59, 37. **YTD only** (no 180d) to limit volume. |
| top_terms.csv | 960 | Top 60 search terms by spend per product × window (YTD2026 and 180d). US: 59, 30, 37, 39, 45, 46. CA: 30, 59. Taken from a top-200 pull sorted by spend. |
| wasted_terms.csv | 258 | Terms within the top 200 with ≥10 clicks and 0 orders. |
| wasted_spend_summary.csv | 16 | Count and spend of wasted terms per product × window, the top-200 share of all term spend, and the total term count. |
| placements.csv | 48 | 90d placement split (TOS, Rest of Search, Product Pages, Off Amazon) for the whole product. US: 59, 30, 37, 39, 38, 31, 32, 45. CA: 59, 30, 37, 31. |

**economics.csv notes**

- Price, fees and landed cost are weighted by units over the last 30 days.
- `contribution` and `breakeven_acos` are the tool's own values.
- The `_ex_outliers` columns repeat those values with outlier SKUs removed.
- `n_skus_incomplete` counts SKUs that are missing cost inputs.

**ppc_windows.csv notes**

- `ppc_summary` does not return units. Use ppc_product_table_ytd or ppc_monthly_2026 for units.
- `blank_reason` holds the tool's stated reason whenever a value is null.

Product 43 has no syntax library, so it has a summary, product table and perf split only.

## Caveats (read before using)

1. **All rates are blended**: window total over window total, never an average of daily rates.

2. **Attribution and settling.** Attribution is 7-day and data is settled through 2026-10-19. The 30d window and October are the most affected. Compare settled windows with settled windows.

3. **Economics is a snapshot taken today**, units-weighted over the last 30 days. It is not a YTD average.
   - Product 70 has only 1 settled month and a refund rate of 0.
   - Product 69's refund rate is null; the tool used 0.

4. **perf_split uses a campaign lens.** A campaign is credited whole to the product it spent most on, so totals can exceed the product-day spend. Examples (YTD):
   - Product 48: 31,344 vs 16,369.
   - 59 US: 300,970 vs 282,126.
   - Defensive campaigns are shared across 42, 45 and 48.

5. **Match type covers only keyword-targeted SP spend.** `coverage_pct` gives the share. For example, at 180d it is 37.6% for 31 US and 99.9% for 39 CA.
   - Auto campaigns, SB and SD are excluded.
   - Ad product "not declared" corresponds to SB/SD and other campaigns with no reported ad product.

6. **Objectives come from the campaign registry.**
   - The account meta says the registry holds only the US profile.
   - Yet the CA product-level splits show declared objectives (e.g. 30 CA: Discovery 56%).
   - Treat CA objective splits with caution.
   - The budget-usage collector has been stale since 2026-08-28.

7. **Syntax groups are overlapping facets, not a partition**, so their rows cannot be summed.
   - `search_volume_library` comes from a mixed vendor cascade: sqp is weekly, while helium10, asinsight and datadive are monthly. Use it as a size order only. It does not depend on the window.
   - Market CTR/CVR comes from SQP and reflects a sample, not the full market.

8. **Top terms are search terms (what shoppers typed), not bid keywords.**
   - Term rows are attributed by campaign, so the term spend total is about 5% above the product tile.
   - **Wasted spend is a lower bound.** Only the top 200 terms by spend were scanned; these cover 59–92% of term spend, and each pull's cut-off spend is in the summary. Most ≥10-click, 0-order terms sit below the cut-off.

9. **Placements are estimates.** Amazon reports placement by campaign and performance by keyword, and the tool redistributes between the two. In placements.csv:
   - `spend`, `est_clicks` and `impressions` are additive.
   - `cpc` = spend ÷ est_clicks.
   - `ctr_pct` = est_clicks ÷ impressions. It is very low for Product Pages and high for TOS by construction.
   - `cvr_est_pct` is the clicks-weighted mean of the tool's trailing-7-day placement CVR. It is approximate.
   - `acos_est_pct` is the spend-weighted mean of the daily ACoS values that passed the tool's 10-order campaign gate. It is **weak**; check `acos_days_drawn`, which is often under 10 of 90.
   - Off Amazon has no CVR or ACoS (withheld by a tool ruling dated 2026-08-30).
   - The 90d split total is about 5% above the tile spend (`coverage_pct`).

10. **Launch products**:
    - 73's first data is 2026-07-09.
    - 70's first data is 2026-09-14, with real spend from 2026-10-04.
    - 69's first data is 2026-10-16 (about one week, all of it settling).
    - 48 has 2025 history.
    - 46 had no advertising before 2026-04-30, so its 180d and YTD figures are identical.

## Data problems found

- **COGS outliers**:
  - 59 US BAMBOO-QUEEN-LIGHTBLUE: landed cost 60.89 (2.35× the size median), 75 units.
  - 59 US BAMBOO-CALIFKING-BLACK: 51.71 (1.69×).
  - 73 Light Blue King: 2.00 (LOW).
  - 73 Light Blue Queen: 1.83 (LOW).
- **CA fulfilment fees** are high on some SKUs (about 18–20 vs 12–13 typical). On 38 CA, many SKUs have negative contribution and the blended break-even ACoS is 7.1%.
- **Many SKUs have incomplete cost inputs** (`n_skus_incomplete`), e.g. 39 CA: 63, 32 US: 36, 44 US: 20.
- **30 US lists both "California King" and "Cal King"** as sizes (one sage SKU).
- **Stock-outs are widespread** (per the 180d perf_split cover tile): 39 US has 38 OOS SKUs, 32 US has 42, and 59 CA has 17. This depresses recent sales and CVR.
- **Some tool calls timed out after 60s** (perf_split 59 US 180d and 31 US YTD). Both succeeded on retry. The timeout stubs in raw/ are skipped by the builders.
- **perf_split 180d was pulled only for the core six products and the account.** The other products have YTD only.
