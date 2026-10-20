# CooLinens Launch Tracker

Live page: https://claude.ai/artifact/1MwntnQjbBBpMyt8cRSe6g (Dashboard artifact, owner Shayan Rana).

- `data/<date>/` — the datasets published to the tracker that day, plus `tracker_text.json` (day notes, overlap findings, decisions, daily log).
- `source/` — raw pulls the datasets are built from (Sellerboard daily sales and ads, command-center campaigns, search terms and ranks).
- `build_tracker_data.py` — rebuilds the datasets: `python3 -I build_tracker_data.py <scratchpad>`.
- `index.html` — the tracker page.

Each daily update adds a dated entry to the log and a new `data/<date>/` folder; decisions keep their id and get their status and outcome updated.
