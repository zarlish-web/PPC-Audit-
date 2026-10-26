# Bedding market entry feasibility — Amazon US, Canada, UK

Research package prepared 26 Oct 2026. Primary analysis window: year to date 2026 (1 Jan – 26 Oct).

**Decision in one line:** conditional go — launch a new cotton-only brand on Amazon US with one pre-washed
100% cotton percale sheet set ($59.99–69.99), a ~$130k capped test budget and hard gates at week 6 and
month 4 of selling; Canada follows on the same SKUs, the UK is a later selective test.

| File | What it is |
| --- | --- |
| `report.md` | Executive report + decision memo (Deliverables A, D, E). Live, editable version: the Claude doc "Bedding Market Entry Feasibility — Amazon US, Canada & UK" |
| `Bedding_Market_Entry_Feasibility_Workbook.xlsx` | Deliverable B — 20 numbered worksheets plus supporting data tabs and charts; economics, budget, scenarios and the go/no-go dashboard are formula-driven |
| `charts/` | Deliverable C — eight evidence charts (PNG) |
| `model/` | `model.py` (unit economics + scenarios), `charts.py`, `build_xlsx.py`, inputs and outputs |
| `data/` | Internal extracts (Sellerboard, Ecotero Command Center, Data Dive, Keepa, SQP) with README files per source |
| `research_notes/` | External research on fees/ads, duties/compliance and market/UK landscape, with source URLs and access dates |

Labels used everywhere: ACTUAL (our accounts) · CALC · EST (third-party) · ASSUMPTION (replace with mill and
forwarder quotes first — see workbook tab `18_Assumptions_Evidence`).

Rebuild: `python3 model/model.py && python3 model/charts.py && python3 model/build_xlsx.py` (paths inside the
scripts point at the session scratchpad and need adjusting to `data/`).
