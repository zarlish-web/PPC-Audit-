# Output format

Step 9. Three artefacts, one house shape.

---

## 1 · The plan document

### Section spine

| # | Section | Must contain |
|---|---|---|
| — | The plan in five lines | The verdict, before any table |
| — | Action plan at a glance | Every action, rows touched, daily $ effect, owner, success measure, section |
| 1 | Product story and context-corrected metrics | Current position, then the numbered Readings |
| 2 | **Leak audit** | Ten levers priced, ranked, owned, and the share PPC addresses |
| 3 | What we did and what it produced | Attributed performance, and the prior cycle graded |
| 4 | Earning potential and the declarations | Spend envelope, posture record, search terms |
| 5 | Recovered value | Every action priced in forward cash |
| 6 | Diagnosis — where the spend sits | The affordability test, campaign by campaign |
| 7 | Per-keyword and per-campaign mathematics | How each budget and bid is derived |
| 8 | Coverage | Keyword layers, gaps, ad-type coverage |
| 9 | Competitor position | Verified set, how they buy traffic, structural gaps |
| 10 | Oversight cadence | Dated checkpoints, divergence routing, prediction scoring |
| 11 | Execution register | Waves, and what is deliberately not done |
| 12 | Reconciliation, gaps, and what would change this plan | Figures to reconcile, named gaps, what the analysis does not claim, reversals, decisions requested |

Empty sections are written with the reason they are empty, never omitted. "Not assessed — no competitor export was supplied, and here is what that blocks" is information; silence is not.

### Writing standards

- Every table states what it decides
- Every number carries a basis tag: **HIST** measured on this product, **MARKET** inferred from category or a named competitor, **TEST** no product-specific observation
- Measured and modelled effects are separated
- Every action carries one named owner and a date
- No reasoning cell without a number in it. No "optimise", no "monitor"
- Corrections are written as numbered Readings that name the raw conclusion they reverse, the evidence, and the check that settles it
- State what the analysis deliberately does not claim

### Publishing

**Author in Markdown, publish as HTML.** Markdown uploaded to Google Drive loses fenced code blocks and inline code — they render as shaded bars with empty rows. Convert first: real `h1`/`h2`/`h3`, bordered tables with a navy header row, no construct the importer cannot carry.

Never put a data grid in a code fence. If it is data, it is a table with headers, and the headers say what each column means.

Visual standard: Arial. H1 navy `1F3864`, H2 `2E5496`. Tables navy header, white bold header text, `9.5pt` body, thin `B7C0D0` borders. Sections numbered continuously. Footer carries product, document name, date, page.

---

## 2 · The decided bulk workbook

The original file preserved exactly — every sheet, every column, in order — plus the decision columns and the supporting tabs.

| Tab | Contains |
|---|---|
| Summary | Declarations, ceilings, actuals, scope, and what was excluded |
| **Final Bulk** | Every row, source column order, plus `New Bids` `New Budget` `New Percentage` `Scenario` `Placement Scenario` `Action` `Reasoning` `Reverses If` |
| Change Review Sheet | Only rows that change: entity, campaign, target, field, from, to, action, why, what reverses it |
| Campaign Decisions | Every campaign, one row, with its own ceiling and utilisation |
| Leak Audit | The ranked table from §2 |
| Inventory | Per SKU: units, velocity, months to clear, economics, ceiling, refund tier, gate verdict |
| Search Terms | Every term with a verdict and the sufficiency test |
| Negatives | What is negated and on what evidence — or empty, with the reason |
| Fix Queue | Spending terms held rather than negated, and what happens instead |
| Placement | Per campaign per placement, modifier set and why — or the reason none may be set |
| No-Action Census | Every unchanged row classified, with the mechanical reason |
| BM Recommendations | Findings that are not PPC levers, routed with evidence and an owner |
| Deployment Waves | What opens when, the daily $ effect, and what gates each wave |
| Validation Gate | The checks below, pass or fail with a count |
| Not Built | Tabs this cycle cannot support, why, and the input that would build them |

Colour: amber on a filled decision column, red on a cut or pause, green on a raise or hold.

---

## 3 · The validation gate

Nothing ships with a failure open that is not a named missing input.

| Check | Rule |
|---|---|
| structure | Rows not added to or removed from the source file |
| coverage | Every row carries either a verdict or a census class |
| scope | No campaign advertising a foreign SKU is in the file |
| attribution | Spend reconciles to product-ad attribution, not campaign totals |
| ceiling | No new bid above `ceiling × CVR` for its routed child |
| acceleration | Acceleration window is `min(2, months to clear)` on every SKU |
| denominator | Ceiling tests use cost per unit cleared, not cost per attributed order |
| refund gate | No BLOCK SKU carries spend; no FLOOR SKU is scaled |
| sunk cost | COGS appears in no ceiling term |
| derived fields | Months-to-clear computed from counts, not read from a cover column |
| charge counted once | The surcharge is in the fees line or added back, not both |
| reasoning | Every action has a reasoning, and every reasoning carries a number |
| reversal | Every action has a Reverses If with a read date |
| negation | No term negated below the sufficiency line |
| placement | No blanket modifier in either direction; each set from its own campaign's data |
| budget | No budget raised on a lane whose cost per unit cleared exceeds its ceiling |
| redeployment | Released budget is only redeployed into a lane that is inside its ceiling *and* budget-capped |
| leak share | The document states what share of total monthly loss the PPC plan addresses |
| declaration | Archetype, risk tier, floor price and terminal option read, never derived |

A check that fails on a missing input is reported as such — the input named, and the decision it blocks — rather than quietly passing.
