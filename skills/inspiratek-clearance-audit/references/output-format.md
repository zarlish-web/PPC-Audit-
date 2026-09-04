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
| negative CM | Any SKU whose CM after carry is negative is routed to BM, not bid |
| stock gate | No clearance push on a not-GREEN SKU, and none on a SKU whose hero size is RED |
| ceiling | No new bid above max profitable CPC for its routed child |
| both constructions | Canon break-even and the forward-cash ceiling both shown, with the acted-on one named |
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
| budget | No budget raised on a lane whose cost per unit cleared exceeds its ceiling |
| redeployment | Released budget is only redeployed into a lane that is inside its ceiling *and* budget-capped |
| leak share | The document states what share of total monthly loss the PPC plan addresses |
| declaration | Archetype, risk tier, floor price and terminal option read, never derived |

A check that fails on a missing input is reported as such — the input named, and the decision it blocks — rather than quietly passing.
