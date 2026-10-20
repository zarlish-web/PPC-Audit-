# CooLinens Launch Tracker

CooLinens Daily Recommendations, the shareable page (data built in, opens for anyone it is shared with, no sign-in to the data store): https://claude.ai/artifact/BofUW9KoD7GxXXzuudiR4Z
Dashboard version (needs Claude sign-in): https://claude.ai/artifact/1MwntnQjbBBpMyt8cRSe6g

- `shareable_template.html` + `build_static.py` — bake `data/<date>/*.json` into the shareable page: `python3 -I build_static.py data/<date> shareable_template.html out.html <date>`.

- `data/<date>/` — the datasets published to the tracker that day, plus `tracker_text.json` (day notes, overlap findings, decisions, daily log).
- `source/` — raw pulls the datasets are built from (Sellerboard daily sales and ads, command-center campaigns, search terms and ranks).
- `build_tracker_data.py` — rebuilds the datasets: `python3 -I build_tracker_data.py <scratchpad>`.
- `index.html` — the tracker page.

Each daily update adds a dated entry to the log and a new `data/<date>/` folder; decisions keep their id and get their status and outcome updated.
