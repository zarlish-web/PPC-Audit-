# Inspiratek Clearance Audit

Everything needed to run an Amazon clearance audit on one aged product, the same way, every time.

Built by merging the installed `inspiratek-clearance-audit` skill with a review of the SOP corpus, three live plan documents, two live decided bulks, and one full run on a real product — the Hanging Closet Organizer — whose findings corrected both.

---

## What's here

```
inspiratek-clearance-audit.skill        THE SKILL — install this

skills/inspiratek-clearance-audit/
├── SKILL.md                            the ten steps, 0 through 9
└── references/
    ├── prior-cycle-grading.md          step 0 — verify execution, then grade it
    ├── data-traps.md                   the contradictions that recur, and how to check
    ├── leak-audit.md                   the ten levers, priced and ranked
    ├── refund-gate.md                  tiering SKUs before routing spend
    ├── ceiling-and-attribution.md      what spend is ours, and what a click may cost
    ├── objective-and-builds.md         the clearance re-tag, and build classes B1–B7
    ├── keyword-and-target-selection.md what to target, and which ASIN it routes to
    ├── placement-tiers.md              modifiers per campaign per placement
    └── output-format.md                document spine, workbook tabs, validation gate

drafts/                                 SOPs and amendments — review and ratify
├── AMD-01 decision_framework §8.3       the clearance ceiling contradiction
├── AMD-02 v4.0 §8.1 S-A10               the S-A10 vs SOP-27 R2 conflict
scripts/                                the reproducible run
├── build_hc.py                         decision rules applied to a bulk
├── write_hc.py                         workbook writer, 13 tabs
└── md2gdoc.py                          Markdown → Google Docs HTML
```

---

## Where this sits

The clearance skill is the **aged-stock branch** of the account's PPC family, not a standalone system. Economics, objective bands, per-SKU gates and the verdict vocabulary are governed by `pmp-optimization-sr` → `reference/decision_framework.md`, which is locked canon. Writing and validation are governed by `ppc-decision-reasoning`. The plan and workbook are built by `ppc-plan-builder` and `ppc-workbook-builder`.

What this skill actually owns: **the leak audit, the refund gate, product-ad attribution, the data traps, the clearability read, and publishing.**

## The governing idea

**Advertising is usually the smallest leak on an aged product.**

Quantify every lever first, rank by size, then size the PPC plan against what it can actually deliver. A plan that only addresses advertising typically addresses 8–15% of the loss — and it looks complete while doing it.

## How a run works

You supply the **Final Bulk** — every row for the product, with Action, Reasoning, New Bids, New Budget and New Percentage blank — plus the raw data files. **The run fills those columns in place** and adds what it proposes to create. Each Action is written so it can be executed directly on the campaign; rows left blank are classified in the No-Action Census with the reason. *(Confirmed 4 September 2026.)*

| Stage | Skill |
|---|---|
| Analysis and economics | `pmp-optimization-sr` (canon) + this skill |
| The written plan | `ppc-plan-builder` |
| Filling the decision columns | `ppc-decision-reasoning` |
| Assembling the workbook | `ppc-workbook-builder` |

Back comes the plan document, the filled Final Bulk, added `New SP` / `New SB` / `New SD` tabs for anything proposed, and a `Negatives` tab.

**The one thing that makes a liquidation run different is the objective re-tag at step 1.** Ranking, Market Share, Discovery and Profitable Conversion all become LTSF-Clearance; only Defensive on a brand term survives. That re-tag bars rank targets, the top-of-search ladder, DSTR sizing and Exact expansion onto unproven terms — and makes velocity, months-to-clear and cost per unit cleared the governing measures.

**The label always changes; performance decides the bids** *(confirmed 4 September 2026)*. Every campaign is re-labelled — none is left on Ranking because it was ranking well. We push for sales now, not position, regardless of placement and regardless of how the rank push was going. What each campaign's **bids** do is then read from what it is producing: profitable ACoS is left running exactly as it is, a delivering lane above profitable has its **placement diagnosed before its bid is moved**, moderate performers go to the ladder, poor ones are paused. So little is abandoned mid-push — what ends is the rank programme around a campaign, not the campaign.

Reading placement for cost and buying placement for rank are different things, and only the second is barred. Correcting a modifier because Top of Search runs at three times the campaign's ACoS is always allowed; raising one to hold a position is not.

## The ten steps

| Step | What it does |
|---|---|
| 0 | **Grade the prior cycle** — verify what was executed, grade what it produced |
| 1 | Intake, verify, **re-tag the objective** — every campaign on aged SKUs becomes clearance |
| 2 | **Leak audit** — ten levers, dollars per month, ranked, owned |
| 3 | Diagnose — exposure vs conversion, syntax, variant, competitors, reach |
| 4 | **Refund gate** — tier the SKUs before any spend is routed |
| 5 | **The ceiling** — three numbers, the subsidy zone, per unit cleared |
| 6 | **Clearability gate** — can traffic move this at all: open, split, closed, unmeasured |
| 7 | Spend to volume — with degradation, and the stock ceiling |
| 8 | Decide the existing account |
| 9 | Build new campaigns, then write it up |

Steps 2, 4 and 6 are where plans get overturned. Step 2 stops the document fixing the tenth-largest problem. Step 4 stops money going at stock that comes back. Step 6 stops money going into stock advertising cannot move.

---

## The rules that came from real errors

Each exists because something went wrong on a live product.

**Attribute through product-ad rows, never campaign totals.** Catch-all campaigns carry hundreds of SKUs. One filter pulled in $1,501 of spend of which the product's share was $0.45.

**The charge file carries one month's charge, and the clearance window is a deadline handed to PPC.** Two months is the default, not a constant — it is read per product per cycle, capped again at the real clearance time, and asked for where unstated. And it is a deadline, never a pace: clearing sooner is always better.

**The charge bills on a date, so the value of clearing steps.** A unit sold the day before billing avoids the whole month; the day after, none of it. On one product that made 32 units clearable before the 15th worth $118 — which is what sequences the deployment waves.

**Ceiling tests use cost per unit cleared.** Not cost per ad-attributed order. Where advertising attributes a quarter of units the two differ by four times.

**Refund tier before routing.** A FLOOR SKU cannot be the growth story of a plan; refunded units re-enter the aged pool and re-accrue charge, so a refund costs twice.

**A blanket 0% placement modifier is the same mistake as a blanket 135%, just cheaper.** Finding them all at zero is evidence nobody set them.

**Never negate below the sufficiency line.** At conversion rate *c*, one order is not expected until roughly 1/c clicks. Below that, zero orders is not evidence.

**Budget is not a waste lever.** A budget is a cap, not a spend — cutting a cap the lane never reached saves nothing. On one product the enabled budget was $343.73/day against $38.12/day of actual spend, so cutting it to $89 released $0.00 and only removed headroom. Waste is a specific keyword taking clicks and returning nothing; it is removed where it lives, and the budget stays.

**The click line for waste.** 15 clicks with no orders at ordinary click prices, 20–25 where clicks cost about $0.15 or less. Below that a term has not had its chance. Reaching the line triggers a review, not an automatic pause.

**Prefer the count over the derived field**, and treat staleness as a property of the file, not the field.

**Ask rather than resolve** — a contradiction is a question for whoever prepared the data, not a puzzle. Never silently resolve a vocabulary difference.

**Publish as HTML, not Markdown.** Markdown into Google Drive loses fenced code and inline code.

---

## Status

| Item | State |
|---|---|
| The skill | Merged from the installed baseline plus one live run; not yet re-run end to end |
| SOP-27 P15 | Draft v0.4 — not ratified |
| SOP-12 P13 | Draft v0.1 — not ratified |
| AMD-01 · decision_framework §8.3 | Draft v0.1 — not ratified |
| AMD-02 · v4.0 §8.1 S-A10 | Draft v0.1 — not ratified |
| Hanging Closet plan | Delivered, then corrected — see below |

**RULED, 4 September 2026 — forward cash governs, break-even is the reference.** On a liquidation product PPC is the lever that moves the stock, and spending past profitable is accepted because the avoided charge pays for it. But break-even is not discarded — it is computed every time so nobody bids blind.

Three numbers per child, and the bid sits between them:

| | Formula | Meaning |
|---|---|---|
| Floor | $0.25 default | Below this nothing wins |
| **Max profitable CPC** | margin × CVR | **Where profit ends** |
| **Max click price** | (contribution + avoided charge) × CVR | **Where forward cash ends — the hard cap** |

The gap between the last two is the **subsidy zone**. Bid low in it; the cap is a maximum, never a target. And price the subsidy: `(bid − max profitable CPC) ÷ CVR` is the subsidy per unit, and it has to come in under the charge avoided per unit or the forward-cash argument does not hold and the gap is logged.

A negative contribution does not stop the push; pricing goes to Brand Management as a parallel recommendation.

**Operating floors — defaults, not universal constants. Confirmed 4 September 2026.**

| Floor | Default | Why |
|---|---|---|
| Minimum bid | **$0.25** | Below this the bid does not clear enough auctions to matter |
| Minimum daily budget | **$5.00** | Below this the campaign cannot deliver a readable day |

A product may set its own floor where its own click economics justify it — a category where clicks cost $0.08 can legitimately run a $0.15 floor. The override has to be stated in the plan with both numbers, backed by a measured figure from this product or its category, and it never becomes a way to fund a lane that cannot deliver. Nothing is ever cut to a value between zero and the floor, whatever the floor is set to.

**The correction ladder.** How hard a delivering campaign is corrected is set by its ACoS, not a flat rule:

| ACoS | Action |
|---|---|
| Under 30% | No change — working |
| 30–50% | A few cents, one step per cycle |
| 50–70% | Cut 20% |
| 70–100% | Cut 30% |
| 100%+ | Cut 50% even on one order; pause if still there next cycle |

Bands are absolute, with the product's own break-even stated beside them — on one product break-even was 7.68%, so "under 30% is working" means four times break-even. ACoS at or above 100% overrides the delivering protection; below it, orders shield the lane. The floors still bind, and budget is untouched by the ladder.

**Growth comes from targets, cost control from the bid.** Neither is the budget. A lane spending 11% of its cap is short of reach — it gets more keywords, auto groups, category and product targeting, not a smaller budget.

Where the computed ceiling falls below $0.25, the floor governs and the gap is logged as accepted over-ceiling spend against the charge it avoids.

**Still open:** the Hanging Closet plan predates the leak audit, the refund gate, the objective re-tag and these floors. Seven of its budget cuts land below $5/day and its bids land at $0.24. It needs re-running.

---

*Inspiratek & Ecotero LLC · Confidential*
