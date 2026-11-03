# Daily tracker update (BFCM 2026 budget plan)

The plan page's tracker reads one database document per market per day (`actuals/{US|CA}_{YYYY-MM-DD}`) from
https://claude.ai/artifact/VUqJYuXVXchwQZMp9BnECg. This is how a day is added. Everything is read-only on the account side.

1. **Which days.** List the `actuals` collection of the artifact (ArtifactData `list`). Fill every UTC day from the day
   after the newest document up to yesterday (UTC). Also re-pull the newest existing day once: late ad charges post a day late.
2. **Pull a day** (SellerBoard connector, Ecotero account `c81e7dde-c826-11e9-ab35-e4434b2f1e00`):
   - `dashboard_period` with that single day as the only period (start = end = the day's 00:00 UTC timestamp), no search and
     no marketplace filter. Re-call while it says "preparing". Note the day's Sales and Advertising for Amazon.ca and for the rest.
   - `dashboard_table`, entry_type `product`, count 35, same day and filters: page with sort `sales desc` until a page's rows all
     have Sales 0, then with sort `advertising asc` until a page's rows all have Advertising 0. One call at a time.
   - Large results are saved to files; pass all of that day's saved files to
     `python3 pull_day.py <YYYY-MM-DD> <files...>`. It writes `daily_child_<day>.csv` and prints US / CA sums.
   - Check: the printed sales and advertising sums are within 1% of the dashboard_period totals (CA = Amazon.ca; US = the rest,
     which includes small Amazon Mexico sales). If not, fetch the missing pages before going on.
3. **Build and write.** `python3 actuals_build.py` (from `ppc-plan/`) rebuilds `actuals/db_actuals.json` from all daily files.
   Write the new and re-pulled days' documents with one ArtifactData `batch` of `set` operations (collection `actuals`,
   doc id `{mkt}_{date}`, the document's `data`); documents that already exist need `if_version` from the list in step 1.
4. **Commit** the new `daily_child_*.csv` and `db_actuals.json` on branch `claude/friendly-fermi-jcnfii` and push.
5. **Report** in one short message: each market's spend, sales and TACoS for the newest day, plus the products over their cap
   (TACoS above the plan's cap), from the written documents and `plan_numbers.json` / the plan workbook.

Stop after Dec 2, 2026: the event ends Nov 30 and Dec 1 – 2 cover late charges.
