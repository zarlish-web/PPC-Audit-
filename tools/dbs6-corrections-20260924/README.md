# DBS6 corrections — run 20260924-981b2555

Scripts behind `docs/DBS6_Corrections_by_Situation_20260924-981b2555.docx` (and its `.xlsx`
register), built from the B4 pipeline in `tools/dbs4-corrections-20260924` with B6's windows,
contribution and rounds (11, 16 and 20 September). Same run order: `parse.py` → `run.py` →
`make_register.py` → `categorize.py` → `nonrank_defects.py` → `mkimpact.py` → `build_cat_doc.py`.

Data (Command Center, product 30, US): campaign placement reports `d90` 06-27→09-24,
`pre_deal30` 08-15→09-14, `deal8` (last 10 days) 09-15→09-24, `d14`, `d7`, `d3`, `pre0920`/`post0920`,
`pre0922`/`post0922`; per-target impression share for the 71 in-focus and 29 largest out-of-focus
exact ranking campaigns; keyword rank grid; the change record since 08-15.
Not committed: the audit JSON export and the 30-day keyword pages Part D reads.

Rules applied: the framework's blended conversion rate (25 September revision; the syntax-group
rate stands in for the child's); focus as the run sets it (Bamboo|Queen, Full, King, Cooling);
loss stop 3× contribution; envelope at the engine plan ($1,072/day); stop new steps above the
run's projected 14.1% TACoS; out-of-focus test with no budget cut, collapses frozen, flagship held.
