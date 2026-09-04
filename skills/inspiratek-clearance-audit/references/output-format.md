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

**Do not invent a tab list.** The account has a real one, and inventing a structure organised around this skill's own logic is a mistake `ppc-workbook-builder` has already made once and corrected. The workbook is built by `ppc-workbook-builder` against the account's real tab set; this skill supplies the clearance content that goes into it.

**Template fidelity is exact, not approximate.** Same tab names, same order, same column headers — including wording that predates the build and reads oddly for the current product. Same fonts, fills, widths, freeze panes, number formats. The real template is not internally uniform, and that is not a defect to correct: clone each tab's actual styling, including the inconsistencies.

**The tab list is invariant; what goes inside a tab is not.** A finding specific to this product with no ready-made home is added as extra columns or a grouped sub-block inside the relevant existing tab, styled to match its neighbours — never as a new top-level tab.

The original bulk is preserved exactly — every sheet, every column, in order — with `New Bids`, `New Budget`, `New Percentage`, `Action`, `Reasoning` and `Reverses If` filled on rows that change.

Where this skill's own content needs somewhere to live, it goes in the tab that already covers that subject:

| Clearance content | Goes in |
|---|---|
| The ranked leak table | The summary or findings tab, as a grouped block |
| Refund tier per SKU | The inventory tab, as extra columns |
| Per-SKU ceilings, both constructions | The inventory tab, side by side, labeled |
| Campaigns excluded as multi-product | The summary tab, named with their SKU counts |
| No-action classification | The census or validation tab |
| Findings that are not PPC levers | The Brand Management findings log |
| Campaigns proposed for build | Added tabs `New SP` / `New SB` / `New SD`, one per ad product |
| Negatives to add | Added tab `Negatives`, or delivered empty with the reason |
| Prior objective before the clearance re-tag | The campaign tab, as a column, so the change is auditable |

Colour follows the template, not this skill.

---

## 3 · The validation gate

Nothing ships with a failure open that is not a named missing input.

| Check | Rule |
|---|---|
| structure | Rows not added to or removed from the source file |
| coverage | Every row carries either a verdict or a census class |
| scope | No campaign advertising a foreign SKU is in the file |
| attribution | Spend reconciles to product-ad attribution, not campaign totals |
| break-even | Break-even ACoS computed per SKU from the canon formula, no return allowance |
| negative CM | Pricing routed to BM as a parallel recommendation, never used to withhold the push |
| stock gate | No clearance push on a not-GREEN SKU, and none on a SKU whose hero size is RED |
| ceiling | No new bid above the forward-cash ceiling for its routed child |
| both constructions | Canon break-even and the forward-cash ceiling both shown; forward cash is the one acted on, per the standing ruling |
| floors | No bid under $0.25 and no budget under $5.00 anywhere in the file, staged or live |
| no starved lanes | No campaign cut to a value between zero and the floor — funded at the floor or paused |
| over-ceiling log | Every bid above max profitable CPC carries its cap, its re-read date and the charge it avoids |
| build width | The build spans keywords, auto, category and product targeting — not keywords alone |
| labeled exception | Any spend above break-even is capped, dated and logged |
| exit | The stock threshold at which clearance exits is stated |
| vocabulary | Every verdict comes from the closed list; no invented strings |
| one lever | No row carries two unrelated levers in one cycle |
| sign-off | Every human-confirm trigger flagged, with its trade-off in reviewer units |
| deal state | No figure blends a deal window with a clean window |
| staleness | No anchor older than 45 days, or predating a price/fee/packaging/LTSF change |
| denominator | Ceiling tests use cost per unit cleared, not cost per attributed order |
| refund gate | No BLOCK SKU carries spend; no FLOOR SKU is scaled |
| sunk cost | COGS appears in no ceiling term |
| derived fields | Months-to-clear computed from counts, not read from a cover column |
| charge counted once | The surcharge is in the fees line or added back, not both |
| reasoning | Every action has a reasoning, and every reasoning carries a number |
| reversal | Every action has a Reverses If with a read date |
| negation | No term negated below the negation line; no converting row parked by the sample gate |
| placement | No blanket modifier in either direction; each set from its own campaign's data |
| budget | Budget raised only where the lane can actually deliver more; a lane short of reach gets targets instead |
| redeployment | Released budget goes to new reachable surface, or to a lane at its cap — never to a lane short of reach |
| leak share | The document states what share of total monthly loss the PPC plan addresses |
| declaration | Archetype, risk tier, floor price and terminal option read, never derived |
| objective re-tag | Every campaign on aged SKUs carries the clearance objective, with its prior value recorded |
| no rank artefacts | No rank target, TOS premium bought for position, or DSTR sizing survives the re-tag |
| build classes | Every proposed campaign is one of B1-B6; none invented |
| added tabs | New campaigns split by ad product; negations carry campaign, mode and evidence standard |
| gates named | Every proposed campaign is live-now or names the condition it waits on |

A check that fails on a missing input is reported as such — the input named, and the decision it blocks — rather than quietly passing.
