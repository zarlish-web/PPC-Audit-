# Linen curtains — PPC upload pack

**For: Joseph · 9 September 2026 · Product: DECOLURE Linen Blackout Curtains**

Two files to upload, one edit to make by hand, one export to send back.

Upload the **updates first**, then the **creates** — the updates pause 297 campaigns and free the budget the new ones open into.

---

## 1. Upload these two, in this order

| # | File | Rows | What it does |
|---|---|---|---|
| 1 | `LIN_UPLOAD_SP_UPDATES_09Sep2026.xlsx` | 1,139 | 297 campaign pauses, 77 budget changes, 138 bid changes, 627 placement modifiers to 0% |
| 2 | `LIN_UPLOAD_SP_CREATES_TRANCHE_A_09Sep2026.xlsx` | 374 | Opens 15 new Sponsored Products campaigns at $256/day |

Both are Sponsored Products bulk files, single sheet, already validated — 21 of 21 checks pass on each.

> **Upload each file to Bulk Operations directly — do not open and re-save it in Excel or Google Sheets first.** A re-save round-trip converts blank cells to zeros and the upload will fail.

If Amazon returns an error report, send it over rather than fixing by hand — the summary sheet tells us whether a clean re-upload is safe or whether it needs a fix file for the failed rows only.

---

## 2. Nothing to do by hand

There is no console edit in this pack. The one change that would have needed it — a bid cut on a keyword-group target — has been dropped, along with five others: all six sat on targets with **zero clicks and zero spend**, so the cut was a verdict on no evidence.

---

## 3. One thing to send back

The two Sponsored Display product-targeting campaigns are ready to build, but **we need an SD bulk export from the account first** — the SD template's columns differ from Sponsored Products and we won't guess at them. Bulk Operations → Create spreadsheet for download → Sponsored Display, last 30 days, all entity types.

Once that lands we cut the SD file the same way.

---

## 4. What is deliberately not in this pack

| Held | Campaigns | Budget/day | Waiting on |
|---|---|---|---|
| SP tranche B | 2 | $65 | the 52x84 reprice |
| SP tranche C | 3 | $53 | the colour fix |
| SB tranche A | 5 | $64 | brand registry, plus a logo in the Creative Asset Library |
| SB tranche B | 1 | $20 | reprice **and** brand registry |
| SD views / purchase / audience | 3 | $19 | console build — no targeting expression exists to bulk from |

Nothing above should be uploaded yet. Tranche C in particular routes to the same colourways the refund gate just paused; it opens when the refund cause is fixed, not before.

---

## 5. The record, if you need to see why any row moved

`LIN_change_loader_plan_JOSEPH_ALL_09Sep2026.xlsx` — **one file, all 1,810 rows**, updates and creates together in the standard template. Prior value, new value, the mechanism check on **16 September**, the outcome check on **23 September**, and the fallback if it goes the wrong way. The `decision` column separates the eight update groups from the six create groups, and every gated group names its gate.

`LIN_SB_SD_BUILD_SPEC_09Sep2026.xlsx` carries the SB and SD builds in more detail, for when their gates lift.

---

## The short version of the reasoning

The product refunds heavily and unevenly. Twelve SKUs return 37.5–45.5% of what they sell — an effective **$20.66–$23.67 of ad cost per unit actually cleared, against a $19.69 ceiling** — so their campaigns come off. Eighteen more sit at 25–30% and are held at a bounded budget rather than paused. Twelve refund at 0–16% and are the ones the new campaigns advertise.

Separately, every placement modifier goes to 0%. The 23 August listing change contaminated the placement evidence, so no modifier can currently be justified from data; they get rebuilt from a clean read after 23 September.

---

*Inspiratek & Ecotero LLC · Confidential*
