# Output format

Step 9. Three artefacts, one house shape.

---

## 1 · The plan document

### Section spine

| # | Section | Must contain |
|---|---|---|
| — | The plan in five lines | The verdict, before any table |
| — | Action plan at a glance | Every action, rows touched, daily $ effect, owner, success measure, section |
| 0 | **Prior cycle graded** | Execution rate, every action's grade, what each changes in this plan — or "first cycle, nothing to grade" |
| 1 | Product story and context-corrected metrics | Current position, then the numbered Readings |
| 2 | **Leak audit** | Ten levers priced, ranked, owned, and the share PPC addresses |
| 3 | What we did and what it produced | Attributed performance, and the prior cycle's actuals |
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

**The audit fills those columns; the account team does not.** The file arrives blank and goes back decided, with each `Action` written so it can be executed directly on the campaign without re-reading the plan document. Rows left blank are blank because the analysis reached no decision, and each one is classified in the No-Action Census with the reason.

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
| three numbers | The floor, max profitable CPC and max click price all computed and shown per child |
| subsidy priced | Every bid above max profitable CPC states its subsidy per unit against the charge avoided per unit |
| subsidy justified | Where subsidy per unit exceeds the charge avoided, the gap is logged in dollars and routed to the pricing recommendation |
| bid placement | Bids sit low in the subsidy zone; the ceiling is a maximum, never used as a target |
| floors | No bid or budget below this product's floor anywhere in the file, staged or live |
| floor override | Any floor below $0.25 or $5.00 is stated in the plan with both numbers and a measured reason; absent one, the defaults govern |
| no starved lanes | No campaign cut to a value between zero and the floor — funded at the floor or paused |
| budget direction | No budget reduced as an efficiency action; reductions only on a pause, or from a lane genuinely at its cap |
| paper savings | Any budget released is stated against the lane's actual spend, so a cut to an unspent cap is never reported as a saving |
| waste located | Waste is removed at keyword or target level, never by reducing a campaign budget |
| click line | Nothing paused or negated on performance below 15 clicks, or below 20-25 where the click price is about $0.15 or under |
| over-ceiling log | Every bid above max profitable CPC carries its cap, its re-read date and the charge it avoids |
| build width | The build spans keywords, auto, category and product targeting — not keywords alone |
| intent routing | Every ASIN matches its keyword's intent class; no child a keyword has ruled out |
| campaign purity | No campaign mixes two attribute families, and none spans two search-volume tiers |
| cannibalisation | No keyword inside a campaign captures another under that campaign's match type |
| campaign count | Campaigns x $5.00 does not exceed the budget available for new builds |
| PAT edge | Every product target names the edge that justifies it, with the numbers |
| category refinements | Refinements set against our current price, rating and review count |
| labeled exception | Any spend above break-even is capped, dated and logged |
| exit | The stock threshold at which clearance exits is stated |
| window read | The clearance window is read from the declaration, not assumed; where unstated it was asked |
| charge basis | Avoided charge built from the file's ONE month figure, never a multi-month reading |
| billing date | The billing date is named, with units clearable before it and what that is worth |
| vocabulary | Every verdict comes from the closed list; no invented strings |
| one lever | No row carries two unrelated levers in one cycle |
| ladder applied | Every delivering campaign's bid move matches its ACoS band, and the band is named |
| break-even shown | The product's own break-even ACoS is stated beside the bands |
| 100% override | No campaign at or above 100% ACoS shielded by having orders |
| no hard cuts | No budget cut on a delivering campaign; the ladder corrects the bid, not the budget |
| walk stated | Every multi-cycle correction states its cycle count and completion date |
| sign-off | Every human-confirm trigger flagged, with its trade-off in reviewer units |
| deal state | No figure blends a deal window with a clean window |
| staleness | No anchor older than 45 days, or predating a price/fee/packaging/LTSF change |
| execution verified | Every prior action checked against the current bulk, not the prior plan |
| grades fed forward | No BACKFIRED lever re-proposed; no lever under half its prediction repeated unchanged |
| units cleared | Grades use units cleared, not units shipped, wherever returns data exists |
| provisional marked | Any grade inside the refund window carries a re-read date |
| drawdown reconciled | Aged-pool movement reconciles to sales plus removals, or the gap is named |
| predictions logged | This cycle logs predictions in the units the next cycle will measure |
| denominator | Ceiling tests use cost per unit cleared, not cost per attributed order |
| refund gate | No BLOCK SKU carries spend; no FLOOR SKU is scaled |
| sunk cost | COGS appears in no ceiling term |
| derived fields | Months-to-clear computed from counts, not read from a cover column |
| charge counted once | The surcharge is in the fees line or added back, not both |
| columns filled | No decided row returned with an empty decision column; no blank row missing from the No-Action Census |
| directly executable | Every Action states the change to make, not a suggestion to consider it |
| reasoning | Every action has a reasoning, and every reasoning carries a number |
| reversal | Every action has a Reverses If with a read date |
| negation | No term negated below the click line; no converting row parked by any gate |
| placement | No blanket modifier in either direction; each set from its own campaign's data |
| budget | A lane short of reach gets more targets, not more budget and not less |
| redeployment | Growth comes from targets and coverage; budget moves only between lanes that actually spend theirs |
| leak share | The document states what share of total monthly loss the PPC plan addresses |
| declaration | Archetype, risk tier, floor price and terminal option read, never derived |
| objective re-tag | Every campaign read on performance before re-labelling; profitable lanes kept running untouched; prior objective recorded on every campaign re-labelled |
| placement first | Every delivering campaign in a cutting band has its placement report read and its modifier corrected before the bid is moved |
| no rank artefacts | No rank target, TOS premium bought for position, or DSTR sizing survives the re-tag |
| build classes | Every proposed campaign is one of B1-B7; none invented |
| added tabs | New campaigns split by ad product; negations carry campaign, mode and evidence standard |
| gates named | Every proposed campaign is live-now or names the condition it waits on |

A check that fails on a missing input is reported as such — the input named, and the decision it blocks — rather than quietly passing.
