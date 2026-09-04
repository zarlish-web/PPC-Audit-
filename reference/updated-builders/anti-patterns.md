# Anti-patterns — the failures this skill exists to prevent

Each is a real defect that shipped, with what it looked like and what
catches it. They are listed here because a failure buried inside a long
rule is hard to recognise in the moment; a reader who has seen the shape
spots it.

---

## 1. A value derived when the account already supplied it
**Looked like:** rank targets computed from search-volume tiers giving 10/15/20/30, while the account's own keyword list held 3–8 on 7,949 rows. Branded terms screened by a hand-written pattern that caught one brand and missed five, while a Final Categorization column marked 994.
**Why it survives:** a derived value looks exactly as authoritative as a supplied one.
**Catch:** before deriving anything, name the column that would already hold it and say you opened it.

## 2. Routing inferred from a campaign's name
**Looked like:** campaign names disagreed with the account's own product-ad rows on 212 of 251 campaigns. One auto campaign named for a single SKU was running fifteen.
**Catch:** routing is read from Product Ad rows. Report the disagreement count.

## 3. A rate computed on a sample too thin to carry one
**Looked like:** a child's $24.67 contribution came from 2 units at a price 40% above every sibling, and priced 597 rows.
**Why it survives:** the same builder applies a click-sample floor rigorously and never thinks to apply a unit floor.
**Catch:** every contribution figure names the unit count behind it.

## 4. A per-unit figure used as a per-click ceiling
**Looked like:** a $8.99 top-of-search price passed a check because the unit earns $17.35. That is break-even only at 100% conversion.
**Catch:** the bound is what the placement affords at its own conversion rate, not what the unit earns.

## 5. One flat value across a set that was supposed to be sized per row
**Looked like:** 185 top-of-search premiums at exactly 350%, because every unranked term hit the same band default.
**Catch:** a roster shows a spread. Fire when one value exceeds ~45% of the non-zero set.

## 6. A screen run against the wrong population
**Looked like:** an already-targeted screen checked this portfolio and missed 51 terms live elsewhere in the account, and checked Phrase/Broad while screening Exact launches — 275 slipped through.
**Catch:** name the population the rule governs before writing the query, and state it in the reasoning.

## 7. Prose patched by pattern match
**Looked like:** a regex removing superseded sentences cut 556 cells mid-clause. Later, a find-replace swapped one figure into sentences whose arithmetic depended on the old one, producing "$26.16 exceeds $378.56" — false by fourteen times.
**Catch:** regenerate the cell from its own data. Patterns may find rows, never edit them.

## 8. Regenerating at the wrong unit
**Looked like:** fixing accreted cells cell-by-cell moved staleness into the columns; fixing rows moved it into sections. One row told three stories from three renders.
**Catch:** the unit of regeneration is the decision. Action, reasoning, reversal and the hosting campaign row rebuild together.

## 9. A decided row that cannot deploy
**Looked like:** 525 rows priced, routed and reasoned inside campaigns that stayed paused. The file called it the largest action in the programme; deployment changed nothing.
**Catch:** every row states what else must be true for it to serve. "Prepared, not deployed" is an honest verdict.

## 10. One verb covering two operations
**Looked like:** RE-ROUTE meant both "re-price to the child the ads already serve" (441 rows) and "switch which child is advertised" (62 rows). The re-pricings shipped; the switches silently did not, because the file had no Product Ad rows.
**Catch:** the verb names the entity and the field.

## 11. A budget cap reported as spend
**Looked like:** $1,948/day quoted as a programme's cost while actual spend was $60.84 — wrong by thirty-fold, because the budget column was summed.
**Catch:** say which of three a figure is: spent, permitted, or projected.

## 12. An instruction written into a recording column
**Looked like:** target states written into the State column to mark waves, destroying the before-state on 247 rows and making 169 correct rows read as contradictions.
**Catch:** the column that records what is, and the column that says what to do, are different columns.

## 13. Two accounts of one file
**Looked like:** a plan's reconciliation table typed separately from the workbook it certified; the workbook advanced one render and six of twelve "Match" rows were false.
**Catch:** generate the table from the file by the same code that runs the gate.

## 14. A gate written to pass the defect
**Looked like:** an integrity check testing one fragment shape certified PASS over 564 damaged cells. A bounds check passed an over-priced click because it tested the wrong bound.
**Catch:** every check carries a known-bad injector, and a check that fires is diagnosed before it is believed.

## 15. Negating a relevant term that is underperforming
**Looked like:** "cooling sheets" itself on the negative list for a cooling sheets product, because the screen filtered on clicks-with-zero-orders.
**Catch:** screen structurally first. A relevant non-converter goes to a fix queue, recorded so a reviewer sees it was considered.

## 16. Grading an action that never deployed
**Looked like:** rows that never landed would grade as flat and escalate as a diagnosis failure, when the diagnosis was never tested.
**Catch:** execution verification runs before grading. Unexecuted is its own verdict.
