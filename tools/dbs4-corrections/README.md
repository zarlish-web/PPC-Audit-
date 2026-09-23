# DBS4 corrections — run 20260921-dbcd48b8

Scripts that produced `docs/DBS4_Bids_Placements_Corrections_20260921-dbcd48b8.docx` and
`docs/DBS4_Corrections_Register_20260921-dbcd48b8.xlsx`.

- `data/placements_*.jsonl` — Command Center campaign placement reports (product 59, US):
  `d90` 2026-06-23→09-20, `pre_deal30` 2026-08-15→09-14, `deal6` 2026-09-15→09-20, `deal8` 2026-09-15→09-22 (deal to date).
- `skus.json` — Command Center unit economics per SKU: `[price, fee-model contribution, units 28d]`.
- `parse.py` → structured fields from the audit export's rationale; `analysis.py` → per-campaign
  rebuild and judgement against "Bids and placements on Exact campaigns"; `findings.py` → issue
  detectors; `run.py` → `analysis.json`; `build_doc.py` → the document.

The scripts expect the audit JSON export as `a.json` and write intermediates next to themselves
(the JSON export is not committed: it is 8.9 MB and lives in Command Center).

## Situation-based version (current)

`categorize.py` sorts every enabled ranking-exact campaign into one situation (thin, leaking,
short of clicks, went dark, rank collapse, out of focus…) using 90-day, 14-day, 7-day, 3-day and
deal-to-date windows plus the change record; `nonrank_defects.py` reads the other campaign types
and lists the rows that should not load; `build_cat_doc.py` writes
`docs/DBS4_Corrections_by_Situation_20260921-dbcd48b8.docx` and its `.xlsx` register.
Extra data: `placements_d14/d7/d3/pre0910/post0910.jsonl`, `decisions_hist.jsonl` (the change
record since 2026-08-15) and `impact.json` (before/after of the 10 and 15 September rounds).

## Part D — B4 diagnosis (traffic gap vs performance gap)

`diag.py` reads Command Center pulls for B4 (product 59) — syntax groups, keyword rows with
placement split, target-level top-of-search impression share, rank grids, ASINsight
our-keywords — into a per-group and per-keyword verdict (traffic gap / performance gap / both /
not present / on track) against the app's bars (CTR 1.1× market, CVR 3× market) and the plan's
weekly click requirement. The 6-piece (product 30) keyword rows are read only to show where it
bids in B4's auctions. `charts46.py` draws the performance-vs-tuning timeline; `part_d.py` is
executed by `build_cat_doc.py` to write Part D. The raw pulls (~128 MB) are not committed;
`data/b46_diag.json` holds the computed B4 keyword and group tables and `data/chart_b4.png` the chart.
