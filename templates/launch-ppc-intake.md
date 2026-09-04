# Launch → PPC Intake Request

**Product:** `<product code / parent ASIN>` · **Go-live target:** `<date>` · **Requested by:** PPC ·
**Due:** day −5 · **Returned by:** Launch Manager, countersigned

The PPC plan is built from this pack. PPC executes inside the launch plan and does not author plan
values — a missing field is not filled with an assumption, it moves the standup date or drops the
affected terms from batch 1. Every row below states what PPC does when it is missing, so the cost of
a gap is visible before it is paid.

**How to return it:** one row per SKU in Blocks 1–2, one row per keyword in Block 3, every number
dated with its source named. Fields you cannot supply come back as a dated blocker line with an
owner — never as a blank.

---

## Block 1 — SKU and cost register (one row per child SKU)

| Field | Notes |
|---|---|
| Parent ASIN / child ASIN / seller SKU / FNSKU | |
| Variation attributes | size, colour, count, style |
| Selling price at launch | |
| Coupon / promo at launch | % or $, and the dates |
| Landed COGS per unit | |
| FBA fulfilment fee | |
| Referral fee | |
| Inbound freight per unit | |
| **Contribution margin $ per unit (CM2)** | after all of the above |
| Expected AOV | units per order × price |
| Margin table version + date | and whether it is provisional |

PPC **derives** the ceilings from these and never types them: BE_ACoS = margin ÷ AOV,
Target ACoS = 50% of BE, Max acceptable = 75% of BE. A blended or account-level cost is unusable —
ceilings are per variation.

**If missing:** the economics spine runs on the launch model, tagged PROVISIONAL, and every
ceiling-referencing action inherits that flag. It does not block the launch; an *unflagged*
provisional read is a process failure.

---

## Block 2 — Inventory and variation state (one row per child SKU)

| Field | Notes |
|---|---|
| On-hand FBA units | |
| Inbound / in-transit units + ETA | |
| Reserved units | |
| Days of cover at planned launch velocity | |
| **Days to stockout against the full batching horizon** | not batch 1 alone |
| Replenishment lead time | |
| Next PO date and quantity | |
| Adequacy band | GREEN / YELLOW / RED — RED = projected stockout ≤ 14 days |
| **D2 preferred variation** | the child SKU the ranking programme runs on |
| **Ranked backup chain** | 1st, 2nd, 3rd — used when the gate flips |
| Do-not-advertise SKUs | with the reason |

**If missing:** no term deploys ranking-sized. Campaigns may stand up at capped test level on the
declared preferred SKU with a D2-pending flag on every row.

---

## Block 3 — Keyword set / Master Keyword List (one row per keyword)

| Field | Notes |
|---|---|
| Keyword | |
| Search volume + source + pull date | |
| **Syntax tag** | |
| **Relevancy score** | re-scored against the *live* listing copy, not carried from research |
| Page-one relevancy flag | is this a page-one objective term or a later batch |
| **Indexed? (Y/N) against the preferred variation** | dated inside the batch window |
| Listing placement | title / bullet / backend / none — required on any rank-objective term |
| Current organic rank + date measured | |
| **Target rank + target date** | |
| SQP market CVR, market CTR, brand share | |
| Competitor CPC benchmark | |
| Intended batch | 1 / 2 / 3 |
| Objective | ranking / discovery / defensive / profitable conversion |
| Hero or halo | |

**Two confirmations required:** MKL refresh date inside 30 days, and relevancy re-scored against the
live title and bullets.

**If missing:** an unindexed term does not enter batch 1 at any bid — no bid level ranks an unindexed
term; it routes to the indexing owner with a ticket reference and waits for a later batch. An
untagged or unscored term routes to MKL maintenance, not to a campaign.

---

## Block 4 — Syntax and page-one priority

- Which syntaxes carry the page-one objective, and which are deliberately deferred
- The root map behind that priority
- Head / mid / long-tail split
- Syntaxes excluded on purpose, with the reason

Launch supplies the tags and the priority order. PPC decides which get funded first, at what size,
and in which batch.

**If missing:** batch 1 is assembled on search volume alone, which funds demand the listing cannot
convert.

---

## Block 5 — Product detail pack (packaged per product)

Material · dimensions and weight · full specifications · pack size / count · certifications and
compliance · use cases and occasions · key differentiators vs the top 3 competitors · restricted or
ad-policy-sensitive claims · live title, bullets and backend terms · A+ status · image and video
readiness date.

**If missing:** relevancy scoring is unauditable, page-one placement cannot be verified, and no
Sponsored Brands / Video creative can be briefed.

---

## Block 6 — Targets and budget

| Field | Notes |
|---|---|
| **Declared launch envelope ($/week)** | plus funding-queue position |
| Monthly ceiling | |
| Units / sales target by week | |
| Target page-one date per head term | |
| **Model CVR, with its source named** | it is a model, not a benchmark — it is labelled as such so the standing system never inherits it |
| Review count expected at week 2 / 4 / 8, and the review plan | |
| Price, coupon and deal calendar for 8 weeks | |
| **Dated honeymoon exit** | written into the standup record as a calendar fact |
| Sign-off owner for launch TACoS readings | launch TACoS reads far above band by construction — near-zero organic revenue — and trips code red mechanically; the reading is recorded, flagged and routed, never silently suspended |

**If missing (envelope):** there are no batch sizes and the standup does not open. Sizing without a
declared envelope is how a launch quietly becomes an envelope increase nobody approved.

---

## Block 7 — Competitor and market analysis

Top 10 competitor ASINs with price, review count, rating and main-image style · market search volume
on the head terms · share of voice of the incumbents · our price positioning · conquest target ASINs
· category BSR benchmarks used to set the rank targets.

**If missing:** rank targets have no basis and product targeting / conquest cannot be planned.

---

## Block 8 — Strategy declarations PPC needs from launch

| Declaration | Why PPC needs it |
|---|---|
| **Product type: subjective or non-subjective** | Decides when a placement premium may be tested. Non-subjective → modifiers stay at zero until conversion evidence exists on the term. Subjective → top-of-search and rest-of-search test together and discovery enters earlier. |
| **Batch lists and the batching cadence** | Batch 1 deploys as SP Exact single-keyword campaigns at fixed bids. Broad, auto and phrase are Phase 2 and stand up only on verified entry conditions. |
| Phase 2 condition set and expected date | So the discovery surfaces are planned, not improvised. |
| Brand Registry status + video / lifestyle assets | Decides whether SB, SBV and SD are in scope and in the envelope. |
| Existing campaign export (if any) | PPC decides keep-or-rebuild and consolidation. |
| **Lead-product declaration on shared terms** | Any term a live sibling also targets needs a declared lead product before it is funded here — two family pushes on one term bid against each other with the family's own money. |
| **Armed deal / event window with dates — including an explicit "none"** | A recorded absence is what makes the launch date defensible later; silence is not. |
| Ad eligibility confirmed on the advertised SKU | An eligibility flip halts lever activity the same day. |
| No price move in the trailing 7 days, or the dated row | Otherwise every CVR and ACoS read in the window is marked provisional. |

Settled already, not a question for launch: **batch-1 exacts run fixed bids, one campaign / one
keyword / one ad group**, with negative walls pre-loaded in the same session.

---

## Block 9 — Access and operations

Portfolio name and product code / slug · marketplace · go-live date · ad account and billing
continuity confirmed · approver for launch-stage verdicts · pointer to the launch department's audit
series · dayparting position (deferred by default).

---

## Return condition

The pack is accepted when every row carries an evidence line — a value with its source and date, or
a named blocker with an owner and a date. An assertion is not evidence. Failing rows either move the
standup date or drop the affected terms from batch 1, and the drop is logged before the standup
proceeds.
