# DBS6 corrections — run 20260921-f066a8f0

Same method as `tools/dbs4-corrections` (situations, push rules, Part D), applied to
Decolure Bamboo Sheets 6-Piece (product 30). Output:
`docs/DBS6_Corrections_by_Situation_20260921-f066a8f0.docx` and `.xlsx`.

Order: `parse.py` (rows.json from slim.json) → `run.py` (analysis.json) → `make_register.py`
(register.json) → `categorize.py` (cats.json) → `nonrank_defects.py` → `build_cat_doc.py`
(which executes `part_d.py`, using `diag.py`).

B6-specific choices (operator 2026-09-23):
- Same push as B4 even though B6 has no deal: daily step by delivery gap (+30/+20/+10%),
  halved where the 16 Sep raise bought no impression share; loss stop at 3x contribution per
  top-of-search order (own TOS conversion from 15 clicks, else the product rate 19.4%); spend
  envelope 1.5x current daily spend for 09-24..09-28; share stop at 40% and flat.
- B6 keeps its terms shared with B4; B4's document is left unchanged.
- Focus stays as the plan sets it on every syntax (Bamboo|Queen and cooling stay out). Out-of-focus
  campaigns converting at top of search above 3x market CVR (15+ TOS clicks, 90 days) get a
  two-week +10% TOS test (09-24..10-07) inside the loss stop, on a child that can ship (Queen on olive).
- The run has no per-campaign click requirement; it is taken from the brief's per-keyword
  weekly PPC-click target, split across in-focus campaigns sharing the keyword.
- The engine's market bound is per campaign in this run (parsed from the rationale).
- Change rounds read: 11 Sep (08–10 vs 12–15 Sep) and 16 Sep (12–15 vs 17–19 Sep).

The scripts expect the audit export as `a.json` (and `slim.json`, a projection of it) plus the
files in `data/` next to them; the Command Center keyword/syntax/ASINsight pulls used by
`diag.py` (~100 MB, `b46/b6_*`) are not committed.
