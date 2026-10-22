# CooLinens Launch Tracker

CooLinens Daily Recommendations, the shareable page (data built in, opens for anyone it is shared with, no sign-in to the data store): https://claude.ai/artifact/BofUW9KoD7GxXXzuudiR4Z
Dashboard version (needs Claude sign-in): https://claude.ai/artifact/1MwntnQjbBBpMyt8cRSe6g

- `shareable_template.html` + `build_static.py` — bake `data/<date>/*.json` into the shareable page: `python3 -I build_static.py data/<date> shareable_template.html out.html <date>`.

- `data/<date>/` — the datasets published to the tracker that day, plus `tracker_text.json` (day notes, overlap findings, decisions, daily log).
- `source/` — raw pulls the datasets are built from (Sellerboard daily sales and ads, command-center campaigns, search terms and ranks).
- `build_tracker_data.py` — rebuilds the datasets: `python3 -I build_tracker_data.py <scratchpad>`.
- `index.html` — the tracker page.
- `day/<date>/` + `build_day_report.py` — the full report for one complete day, shown at the top of the shareable page (newest first, older days selectable): totals vs the day before, profit and loss, spend by ad type, by size and by campaign group, every campaign, every search term, organic rank and points to note. Each morning's update builds the report for the previous day: `python3 -I build_day_report.py <scratchpad> <date>` reads `v8/day/<date>/` (profit.csv, campaigns.tsv, terms.tsv, ranks.csv, notes.json; formats in the script header) and adds it to `day_reports.json`.

Each daily update adds a dated entry to the log and a new `data/<date>/` folder; decisions keep their id and get their status and outcome updated.

Days follow US Eastern time, as Sellerboard's own dashboard does. The Sellerboard API returns UTC days, so units, sales and profit per day are re-counted from the order list with `orders_to_et.py` (writes `source/orders_et.csv`). Ad spend, clicks and ad orders are date-level and are used as pulled.
