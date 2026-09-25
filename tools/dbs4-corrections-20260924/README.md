# DBS4 corrections — run 20260924-5e8a0f10

Scripts behind `docs/DBS4_Corrections_by_Situation_20260924-5e8a0f10.docx` (and its `.xlsx`
register): the 21 September corrections re-validated on data to 24 September, for the run that
moved B4's focus to Bamboo|California King and Bamboo|Cooling.

Pipeline (run from a folder holding the audit export as `a.json`, the files in `data/` next to
the scripts, and `b46/` for Part D): `parse.py` → `run.py` → `make_register.py` →
`categorize.py` → `nonrank_defects.py` → `build_cat_doc.py` (which runs `part_d.py`).

Data (Command Center, product 59, US):
- `placements_*.jsonl` — campaign placement reports: `d90` 06-27→09-24, `pre_deal30` 08-15→09-14,
  `deal8` (the deal so far) 09-15→09-24, `d14`, `d7`, `d3`, `pre0922` 09-19→09-21, `post0922` 09-23→09-24.
- `b4_targets_{30d,deal}_<campaign>.json` — per-target top-of-search impression share, 08-26→09-24 and
  09-15→09-24, for the 20 in-focus and 50 largest out-of-focus exact ranking campaigns.
- `b4_ranks_keywords.json` — daily keyword rank grid 06-24→09-24 (7-day medians are taken from it).
- `decisions_hist.jsonl` — the change record since 08-15, including the 22–24 September moves.
- `impact.json` — before/after reads of the 15/16 and 22 September rounds.

Not committed: the audit JSON export (8 MB) and the 30-day keyword pages Part D reads
(`b46/b4_keywords_30d_p*.json`, ~70 MB); both live in Command Center.

Operator decisions applied (25 September): push only the 20 in-focus campaigns; the out-of-focus
test (+10% top of search for two weeks on campaigns converting at 3× market) with the flagship held
flat and no budget cut; collapses frozen at >10 positions lost on the 7-day median and win over the
test; loss stop 3× contribution; envelope 1.5× in-focus spend; stop new steps if weekly TACoS passes
21.7%; only the in-focus Queen White campaign is re-pointed; raises on campaigns missing from the
export held until confirmed.
