# Inspiratek Clearance Audit

Everything needed to run an Amazon clearance audit on one aged product, the same way, every time.

Built by merging the installed `inspiratek-clearance-audit` skill with a review of the SOP corpus, three live plan documents, two live decided bulks, and one full run on a real product — the Hanging Closet Organizer — whose findings corrected both.

---

## What's here

```
inspiratek-clearance-audit.skill        THE SKILL — install this

skills/inspiratek-clearance-audit/
├── SKILL.md                            the 9-step run
└── references/
    ├── data-traps.md                   the contradictions that recur, and how to check
    ├── leak-audit.md                   the ten levers, priced and ranked
    ├── refund-gate.md                  tiering SKUs before routing spend
    ├── ceiling-and-attribution.md      what spend is ours, and what a click may cost
    ├── placement-tiers.md              modifiers per campaign per placement
    └── output-format.md                document spine, workbook tabs, validation gate

drafts/                                 SOPs — review and ratify
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

You supply the **Final Bulk** — every row for the product, with Action, Reasoning, New Bids, New Budget and New Percentage blank — plus the raw data files. The run fills those columns in place and adds what it proposes to create.

| Stage | Skill |
|---|---|
| Analysis and economics | `pmp-optimization-sr` (canon) + this skill |
| The written plan | `ppc-plan-builder` |
| Filling the decision columns | `ppc-decision-reasoning` |
| Assembling the workbook | `ppc-workbook-builder` |

Back comes the plan document, the filled Final Bulk, added `New SP` / `New SB` / `New SD` tabs for anything proposed, and a `Negatives` tab.

**The one thing that makes a liquidation run different is the objective re-tag at step 1.** Ranking, Market Share, Discovery and Profitable Conversion all become LTSF-Clearance; only Defensive on a brand term survives. That re-tag bars rank targets, the top-of-search ladder, DSTR sizing and Exact expansion onto unproven terms — and makes velocity, months-to-clear and cost per unit cleared the governing measures.

## The nine steps

| Step | What it does |
|---|---|
| 1 | Intake, verify, **re-tag the objective** — every campaign on aged SKUs becomes clearance |
| 2 | **Leak audit** — ten levers, dollars per month, ranked, owned |
| 3 | Diagnose — exposure vs conversion, syntax, variant, competitors, reach |
| 4 | **Refund gate** — tier the SKUs before any spend is routed |
| 5 | **The ceiling** — storage-adjusted, per unit cleared, capped at two months |
| 6 | **Clearability gate** — can traffic move this at all: open, split, closed, unmeasured |
| 7 | Spend to volume — with degradation, and the stock ceiling |
| 8 | Decide the existing account |
| 9 | Build new campaigns, then write it up |

Steps 2, 4 and 6 are where plans get overturned. Step 2 stops the document fixing the tenth-largest problem. Step 4 stops money going at stock that comes back. Step 6 stops money going into stock advertising cannot move.

---

## The rules that came from real errors

Each exists because something went wrong on a live product.

**Attribute through product-ad rows, never campaign totals.** Catch-all campaigns carry hundreds of SKUs. One filter pulled in $1,501 of spend of which the product's share was $0.45.

**The acceleration window is capped at two months, and at the real clearance time.** Taking months-to-clear as the multiplier nearly doubled a ceiling and flipped the verdict on the child it was applied to.

**Ceiling tests use cost per unit cleared.** Not cost per ad-attributed order. Where advertising attributes a quarter of units the two differ by four times.

**Refund tier before routing.** A FLOOR SKU cannot be the growth story of a plan; refunded units re-enter the aged pool and re-accrue charge, so a refund costs twice.

**A blanket 0% placement modifier is the same mistake as a blanket 135%, just cheaper.** Finding them all at zero is evidence nobody set them.

**Never negate below the sufficiency line.** At conversion rate *c*, one order is not expected until roughly 1/c clicks. Below that, zero orders is not evidence.

**Released budget is not automatically redeployed.** Check that some lane inside its ceiling is actually budget-capped. Utilisation measures whether a lane can spend, never whether it should.

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
| Hanging Closet plan | Delivered, then corrected — see below |

**Open — one decision blocks everything else.** Two ceiling constructions are live in the account and they point opposite ways:

| | Construction | Hanging Closet result |
|---|---|---|
| **A** | Canon: the surcharge is a margin drag, so break-even gets *worse*; clear up to break-even, no further | Max profitable CPC **$0.067–$0.091**; CM after carry negative on both children → **ROUTE TO BM** |
| **B** | Forward cash: selling now avoids charge later, so the charge is added *to* the ceiling | Ceiling $7.99–$10.75, max click price **$0.23–$0.24** → fund a reach layer |

A plan built on A stops and sends the product to pricing. A plan built on B funds campaigns. **This is the highest-value open decision in the repo** and it is filed as such — the skill computes and shows both, names which one it acted on, and never picks silently.

The Hanging Closet plan was built on B, before the leak audit, the refund gate and the canon check existed. It needs re-running.

---

*Inspiratek & Ecotero LLC · Confidential*
