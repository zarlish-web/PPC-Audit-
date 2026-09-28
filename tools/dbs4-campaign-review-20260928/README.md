# DBS4 — campaign-by-campaign review, run 20260928-9e6e6bb5

`review.py` reads every enabled campaign in the run export (`a.json`, not committed) against
"Bids and Placements on Exact Campaigns" (25 Sep revision) and writes `review.json`; `build_b4.py`
writes `docs/DBS4_Campaign_Review_20260928-9e6e6bb5.docx` and its `.xlsx` register.

Data (Command Center, product 59, to 2026-09-27): campaign placement reports (`d90`, `pre_deal30`,
`d30`, `d14`, `d7`), per-target top-of-search impression share for 184 ranking campaigns (not
committed, ~4 MB), keyword rank grid, keyword targets (DataRova target rank/units), keyword-by-campaign
split for the 40 largest ranking terms; Sellerboard stock and 30-day units by child.

Operator decisions (28 Sep): maintenance after the deal (no premium until a push is funded); ranking on
White, or the size's highest-selling child with healthy stock while White cannot carry it (Queen → Light
Blue, Full → Olive, Twin → Navy Blue); Auto/Broad/Phrase advertise LTSF SKUs (list pending).
