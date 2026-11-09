# Daily run: what the agent does each morning

The schedule fires this every day at 08:48 US Eastern. Each run reports on **yesterday**, the newest complete day, and refreshes the 7 days before it. Ad sales use 7-day attribution, so those days still change.

Hard rules:
- Read-only on the ad account: no bid, budget, status or targeting change, and no `tunes_stage`.
- No Sellerboard report creation. No DataDive token spend.
- Run Python with `python3 -I`.

## 0. Tools

- Load the tool schemas with ToolSearch `select:` after any reconnect (Sellerboard, command center, ArtifactData).
- Sellerboard `dashboard_period` often answers "preparing" on the first call. Call it again a minute later.
- On a 429, wait and retry. Keep bursts to 5 calls or fewer.
- Large results are saved to tool-results files. Copy them into `v8/raw/` in the scratchpad.

## 1. Pull (per product config)

- Sellerboard `dashboard_period`:
  - For yesterday and the day before: All (`sku_prefix`), then each size. Cal King = All minus the four sizes.
  - For today so far: All.
- Sellerboard `ppc_dashboard_period` with `brand_campaign_search` for the brand totals.
- Sellerboard `ppc_dashboard_table` (entry_type campaign, group_by campaign, `brand_campaign_search`, spend_min 0.01, count 35, every page) for each day. The rows must add up to the brand total.
- Sellerboard `dashboard_table` (product, group_by parent) for yesterday. This is the parent check.
- Sellerboard `inventory`, pages 1–2. Use only the SKUs already in `source/inv_now.csv`.
- Command center (`product_id`), per day:
  - `ppc_campaigns` (limit 200)
  - `ppc_keywords` (all_keywords)
  - `ppc_ranks` (the rank keyword list, all_keywords true)
  - `ppc_decisions` (scope = `decisions_scope`)

## 2. Build

1. Save the raw files: `camp_<date>.json`, `kw_<date>.json`, `decisions_<today>.json`, `ranks_kw.json`.
2. Run `python3 -I append_cc.py <scratchpad> <dates…>`.
3. Write `v19/brand<dd><mon>.tsv` from the brand table.
4. Update `sb_daily.csv`, `sb_ppc_daily.csv`, `sb_campaigns.csv` and `inv_now.csv`.
5. Write `day/<date>/`: `profit.csv`, `campaigns.tsv`, `terms.tsv`, `ranks.csv` and `notes.json`.
6. Update `tracker_text.json`:
   - day notes
   - `partial_day`
   - a new log entry
   - the status and outcome of each decision
   - new D/A ids for new items
7. Set `END` in `build_tracker_data.py` to today 12:00 UTC. Then run:
   - `build_day_report.py`
   - `build_tracker_data.py`
   - `build_static.py`
   - `shot.cjs`: it must report no errors and a phone scrollWidth of 400.

## 3. Run the 8 checks

Follow `CHECKS.md`. Each check gives one line, and a flag if it fails its rule.

## 4. Publish

1. Republish the shareable page (`outputs.shareable_page`) from the same file path.
2. Sync the dashboard (`outputs.dashboard`):
   - Upload each dataset JSON as an asset.
   - Run one ArtifactData batch that updates `datasets/<id>` with source.url, name and updated, each pinned to its version.
3. Copy the files to `launch/tracker/`:
   - `data/<today>/`
   - `day/<yesterday>/`
   - `source/`
   - `index.html`
4. Commit and push to the working branch.

## 5. Slack post

Write the post in the format in `SLACK_POST.md`.

- `slack_mode: "draft"`: put the post in the reply so a person can paste it.
- `slack_mode: "post"`, when Slack is connected: post it to `outputs.slack_channel`.

If any step fails, the post says which data is missing. It never fills a gap with a guess.

## 6. Reply

Send the headline, the 8-check post, what changed in decisions, and the shareable link.
