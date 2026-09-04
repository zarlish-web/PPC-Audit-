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

## The governing idea

**Advertising is usually the smallest leak on an aged product.**

Quantify every lever first, rank by size, then size the PPC plan against what it can actually deliver. A plan that only addresses advertising typically addresses 8–15% of the loss — and it looks complete while doing it.

## The nine steps

| Step | What it does |
|---|---|
| 1 | Intake and verify — reconcile every source before analysing anything |
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

**Open:** the Hanging Closet plan was built before the leak audit, refund gate and two-month acceleration cap were folded in. Under those rules both children sit over ceiling and the higher-refund child is a FLOOR SKU that must not be scaled. The plan needs re-running through steps 2, 4 and 5.

---

*Inspiratek & Ecotero LLC · Confidential*
