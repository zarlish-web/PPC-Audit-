# Instructions — Joseph, 10 September 2026

Two products in this pack. **Linen** is a re-send answering your loader feedback. **Quilt** is new.

---

## A. LINEN — re-send, answering the loader feedback

### A1. Two files to upload, in this order

| # | File | Rows |
|---|---|---|
| 1 | `LIN_UPLOAD_SP_UPDATES_09Sep2026.xlsx` | 1,139 |
| 2 | `LIN_UPLOAD_SP_CREATES_TRANCHE_A_09Sep2026.xlsx` | 374 |

Updates first — they pause 297 campaigns and free the budget the new ones open into.

> **Upload each file to Bulk Operations directly. Do not open and re-save it in Excel or Google Sheets first.** A re-save round-trip turns blank cells into zeros and the upload fails.

If Amazon returns an error report, send it back rather than fixing rows by hand. The summary sheet tells us whether a clean re-upload is safe or whether it needs a fix file for the failed rows only.

### A2. The five holds — what changed

**`check_date` missing on the gated rows — fixed.** All 221 now carry **2026-09-23**. The gate is an event, not a date, so that is the date to re-check whether the gate has opened, not the date to deploy.

**Three campaigns matching nothing — use IDs, not names.** Those names are verbatim from the account export; the account really does call them `96 + inches long`. **Seven** live campaigns carry a `+`. `LIN_campaign_id_map_09Sep2026.csv` maps all 439 campaign names in the plan to their Campaign ID. Match on the ID and the string stops mattering.

**The 4 AUTO builds, 2 PAT builds, 6 SB and 5 SD builds — wrong file, not missing data.** The change loader plan is a *change* format: prior value → new value, plus a mechanism. A campaign that does not exist yet has no prior value, and the template has no column for `targetingType`, a targeting expression, a start date or a default bid. That is why `create_target` is not a ledger field — correctly so.

Everything the loader reported missing is already in **`LIN_UPLOAD_SP_CREATES_TRANCHE_A_09Sep2026.xlsx`**: `Targeting Type = Auto` on all four auto campaigns, real `asin=` expressions on the PAT targets, start dates, bidding strategy, and Campaign → Ad Group → Product Ad → Keyword ordering. Upload it directly rather than rebuilding the creates from the ledger.

**SB and SD stay outside the SP path regardless.** If the write path is `/sp/*` only, those eleven campaigns are manual whichever file they sit in — and five of the six SB are gated on brand registry anyway.

### A3. What must NOT be uploaded

| Held | Campaigns | Budget/day | Waiting on |
|---|---|---|---|
| SP tranche B | 2 | $65 | the 52x84 reprice |
| SP tranche C | 3 | $53 | the colour fix |
| SB tranche A | 5 | $64 | brand registry + a logo in the Creative Asset Library |
| SB tranche B | 1 | $20 | reprice **and** brand registry |
| SD views / purchase / audience | 3 | $19 | console build — no targeting expression exists to bulk from |

Tranche C routes to the same colourways the refund gate just paused. It opens when the refund cause is fixed, not before.

### A4. Please send back

An **SD bulk export** — Bulk Operations → Create spreadsheet for download → Sponsored Display, last 30 days, all entity types. Two SD campaigns are ready to build but the SD template's columns differ from SP and we will not guess at them.

A **current SP bulk export** would also help: it lets us match on IDs everywhere instead of names, which is the fix for the whole class of problem behind the three name mismatches.

---

## B. QUILT (Sleephoria Quilt Set) — new

### B1. One file

`SLQS_change_loader_plan_JOSEPH_09Sep2026.xlsx` — **63 actions**, all on existing campaigns. No creates, so none of the linen create problems apply here.

| Decision | Rows | What it does |
|---|---|---|
| Confirmed pause | 45 | Campaigns, ad groups, product ads and targets past the click line, returning nothing or costing more than $13.20 per order |
| Placement premium removed | 15 | Modifiers to 0% where the premium is not earning it |
| Placement premium stepped down | 3 | 50%→30% and 30%→20% where the placement still converts |

Second tab, **watch, no action** — nine campaigns deliberately left running. Six cost $13.36–$16.30 per order, barely over the $13.20 cap on real orders; three passed the click line with no order but on $4–$21 of spend. None is worth acting on yet. Re-read 23 September.

### B2. The one thing to know about the quilt numbers

The cap is **$13.20 per unit cleared** — the forward-cash ceiling at the deal price. **The Best Deal ends 13 September.** If prices return to normal on the 14th, that cap moves and so does every threshold in this file. Deploying now gets four days of effect at the current economics.

### B3. Not in this file

Twenty-seven "remove from negation" marks were withdrawn by the analyst before this build. Nothing in this plan touches negation.

---

## C. Both products — the checks

| Date | What we read |
|---|---|
| **16 September** | Mechanism — did spend move where the plan said, at the campaigns and placements named |
| **23 September** | Outcome — did units cleared hold, and have the linen gates opened |

Every row carries its own `fallback` — what to do if it goes the wrong way. Nothing in either file needs a judgement call at upload time.

---

## D. One question, when you have a moment

Does the loader read **only** the change loader template, or can it take Amazon bulk files too?

If it is ledger-only, every future cycle's new campaigns need a route decided now rather than per-product. If it can take bulks, the split is just: ledger for changes, bulk for creates, and we stop hitting this.

---

*Inspiratek & Ecotero LLC · Confidential*
