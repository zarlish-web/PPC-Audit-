# DBS4 corrections — run 20260921-dbcd48b8

Scripts that produced `docs/DBS4_Bids_Placements_Corrections_20260921-dbcd48b8.docx` and
`docs/DBS4_Corrections_Register_20260921-dbcd48b8.xlsx`.

- `data/placements_*.jsonl` — Command Center campaign placement reports (product 59, US):
  `d90` 2026-06-23→09-20, `pre_deal30` 2026-08-15→09-14, `deal6` 2026-09-15→09-20.
- `skus.json` — Command Center unit economics per SKU: `[price, fee-model contribution, units 28d]`.
- `parse.py` → structured fields from the audit export's rationale; `analysis.py` → per-campaign
  rebuild and judgement against "Bids and placements on Exact campaigns"; `findings.py` → issue
  detectors; `run.py` → `analysis.json`; `build_doc.py` → the document.

The scripts expect the audit JSON export as `a.json` and write intermediates next to themselves
(the JSON export is not committed: it is 8.9 MB and lives in Command Center).
