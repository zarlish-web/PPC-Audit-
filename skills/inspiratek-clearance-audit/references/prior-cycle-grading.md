# Grading the prior cycle

Step 0. Runs **before** any analysis, whenever a prior cycle exists.

A clearance product is worked in cycles, and a cycle that does not read the last one is just the first cycle done again. The whole value of running this repeatedly is that each pass knows what the last pass tried, whether it happened, and whether it worked.

The canon already owns the machinery — `pmp-optimization-sr` runs an impact review against a prior Action Log and keeps a persistent ledger, grading each action **worked / flat / backfired**. This file adds what is specific to clearance, which is mostly about the fact that **the answer arrives late.**

---

## 1 · Verify execution before grading anything

**An action that was never deployed cannot be graded, and grading it produces a false lesson.**

The trap is real and recurring: a placement inversion described as deployed was not in the account nine days later; a 233-unit removal leg, 39% of an approved order, was never filed and nobody noticed for two weeks.

For every action in the prior decided file, check the **current** bulk and the **current** inventory — never the plan that describes them:

| Result | What it means | What to do |
|---|---|---|
| **Deployed as written** | The value in the account matches the decided value | Grade it |
| **Deployed differently** | Someone changed it, or a later edit overwrote it | Grade what was actually live, and note the divergence |
| **Not deployed** | The decided value never appeared | **Not a failed lever — an unexecuted one.** Do not conclude anything about the lever. Re-issue or drop it, and say which |
| **Deployed then reverted** | It went in and came out | Find out who reverted it and why before re-issuing |

Report the execution rate as a number. A cycle where half the actions never shipped is a process finding, and it outranks every performance finding in the same document.

---

## 2 · What gets graded on a clearance product

Not ACoS. Not ad-attributed orders. **The objective was to empty a shelf**, so grade against that:

| Measure | Predicted | Actual | Why this one |
|---|---|---|---|
| **Units cleared** | From the prior plan | Net of returns | The actual objective |
| **Aged pool drawdown** | Units × cycle length | Charge file, this month vs last | The only measure that cannot be flattered by attribution |
| **Cost per unit cleared** | The ceiling | Attributed spend ÷ units cleared | Whether the push stayed affordable |
| **Months to clear** | Prior estimate | Recomputed at current velocity | Whether the clock actually moved |
| **Charge accrued** | Prior charge minus avoided | This month's charge file | Whether the saving was real |
| **Subsidy per unit** | Logged at plan time | Recomputed at realised CVR | Whether the forward-cash case held |

**Triangulate the drawdown rather than trusting one source.** The aged pool should fall by roughly `units sold + units removed`. On one product it fell 3,220 → 2,776, a drop of 444, which resolved into ~296 sales plus ~148 completed removals. That reconciliation is what settles whether the units really left.

---

## 3 · The refund lag — the thing that makes clearance grading different

**A unit shipped is not a unit cleared.** On a product returning 22%, roughly one in five units counted as cleared this cycle comes back next cycle, re-enters the aged pool, and starts accruing charge again.

So:

- **Grade on units cleared, never units shipped.** Cleared means shipped and not returned.
- **A grade taken before the refund window closes is provisional**, and says so. Mark it `PROVISIONAL — re-read after [date]`.
- **Returns from cycle 1 land in cycle 2's pool.** A cycle that looks like it cleared 60 units and then sees the pool fall by only 47 has not lost 13 units to a counting error — it has had 13 returned. Say that, rather than hunting for a data fault.

A clearance plan that grades itself the week after deployment is grading the shipping, not the clearing.

---

## 4 · Grade categories, and what each one licenses

| Grade | Condition | What this cycle does |
|---|---|---|
| **WORKED** | Delivered at or above prediction | Continue. Do not scale on one cycle's evidence |
| **FLAT** | Delivered, no measurable movement either way | Hold one more cycle, then treat as flat twice = replace |
| **BACKFIRED** | Moved the wrong way | Reverse it, and record what the reversal cost |
| **TOO EARLY** | Read window shorter than the lever's own lag | No verdict. Name the date it becomes readable |
| **NOT EXECUTED** | Never appeared in the account | No verdict on the lever. A verdict on the process |
| **CONTAMINATED** | A deal window, price change or listing edit sits inside the read | No verdict. Name the dates and what they void |

**The escalation rule: a lever below half its prediction is replaced, not deepened.** If a bid walk was meant to hold units and units fell 60%, the answer is not a bigger walk. It is a different lever. Repeating a lever that already underperformed is the most common way a product loses three cycles in a row.

---

## 5 · Grading the multi-cycle walk

The gradual correction runs across several cycles by design, so each cycle checks the walk itself:

- **Is it progressing?** Bid moved 5 cents as decided, or it did not deploy.
- **Are units holding?** The point of walking slowly was to keep clearance while cost comes down. If units collapsed on the first 5 cents, the lane was more price-sensitive than assumed — stop the walk and say so.
- **Is the completion date still right?** Recompute cycles remaining at the current bid.
- **Has the ceiling moved underneath it?** Price, velocity or charge changes reset the target mid-walk, and the walk re-aims rather than continuing to its old destination.

---

## 6 · The first cycle

There is nothing to grade, and that is stated rather than skipped.

What the first cycle owes the second:

1. **A prediction on every action**, in the units the next cycle will actually measure — units cleared, cost per unit cleared, months to clear.
2. **A read date** for each, accounting for the refund lag.
3. **The baseline**, dated: aged units by bracket, velocity, charge per month, cost per unit cleared, subsidy per unit.
4. **The decided file itself, retained**, so execution can be verified against it rather than against memory.

A first cycle that logs no predictions makes the second cycle another first cycle.

---

## 7 · What the grading changes in this cycle's plan

Grading is not a retrospective section at the back. It **feeds the decisions**:

- A lever graded BACKFIRED is not proposed again this cycle.
- A lever graded FLAT twice is replaced, and the replacement names what it does differently.
- A term that reached the click line since last cycle now has its verdict.
- A child whose velocity changed gets a recomputed ceiling, months-to-clear and required pace before anything is staged against it.
- An execution rate below 100% raises the process finding to the top of the document, above the performance work.

---

## 8 · Checks

1. Every prior action has an execution status verified against the current bulk, not the prior plan
2. Every grade names the window it was read over, with deal weeks excluded
3. Grades taken inside the refund window are marked provisional with a re-read date
4. Aged-pool drawdown reconciles to sales plus removals, or the gap is named
5. No lever graded on units shipped where units cleared is available
6. No lever below half its prediction is proposed again unchanged
7. This cycle's predictions are logged in the units the next cycle will measure
8. The baseline is restated and dated, so the next cycle has something to measure against
