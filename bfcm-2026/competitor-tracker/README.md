# BFCM 2026 competitor tracker

**Owner:** Shayan Rana. **Backup:** Zarlish. **v1 due:** Thu Oct 15, 2026 (BFCM-2026 ClickUp task "Competitor BFCM tracker").

| File | What it is |
|---|---|
| `BFCM_2026_Competitor_Tracker_v1.xlsx` | The tracker. Open the **README** tab first. |
| `keepa_request.csv` | The ASINs to pull from Keepa: 333 in total, 93 of them P1. |
| `KEEPA_REQUEST.md` | Which Keepa files are needed, the columns and windows, and how each one fills the tracker. |
| `build_tracker.py` | Rebuilds the workbook from `data/`. |
| `data/` | Snapshots pulled on Oct 13, 2026: Command Center rosters (`cc/`), our BFCM 2025 results (`ours/`), Data Dive listing details (`dd_out/`) and the Command Center visibility summary (`pt_summary.json`). |

To rebuild: `python3 build_tracker.py BFCM_2026_Competitor_Tracker_v1.xlsx keepa_request.csv`, then recalculate in Excel or LibreOffice.

## Tabs

| Tab | Contents |
|---|---|
| Key Insights | A computed, numbers-backed read for each product |
| Dashboard | One row per product: our SKUs and economics, the competitor set, price and STR position, our BFCM 2025 lift, Prime Day 2026 visibility |
| Competitors | All 616 mapped competitor rows |
| Our BFCM 2025 | Our BFCM 2025 results |
| Our Daily 2025 | Our daily results, Oct 15 – Dec 15, 2025 |
| Visibility History | Command Center visibility scores per ASIN |
| Lift Inputs | The inputs for Joseph's forecast |
| Keepa Request | The Keepa ASIN list |
| Data Gaps | What's missing and where to get it |
| Event Watch | Log for competitor checks, Nov 20 – Dec 1 |
