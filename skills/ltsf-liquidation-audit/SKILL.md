---
name: ltsf-liquidation-audit
description: Run a complete Amazon PPC audit and clearance plan for ONE product carrying aged inventory or long-term storage fee (LTSF) exposure, producing a decided bulk file plus a written audit that defends every decision. Use this whenever someone asks for a liquidation audit, clearance plan, LTSF plan, aged-stock plan, terminal or at-risk product analysis, "what do we do about this old inventory", or hands over an LTSF charge file, inventory-age export, or a PPC bulk for a product whose objective is clearing stock rather than ranking — even if they never say "LTSF", "liquidation" or "audit". Also use it when asked to decide bids and budgets on a product that is being cleared, to size clearance campaigns, or to judge whether advertising can clear a batch before its next fee bracket. Do NOT use it for products whose objective is rank (use the ranking plan skill), for portfolio-wide LTSF decisions above the PPC layer, or for building bulk files with no analysis behind them.
---

# LTSF Liquidation Audit

## What this produces

Three deliverables, every time:

1. **The audit document** — the written analysis. Every decision defended with the number it rests on.
2. **The decided bulk** — the product's bulk export with Action, Reasoning, New Bids, New Budget and New Percentage populated on every row that changes, plus new-campaign build sheets.
3. **The decisions-requested list** — what needs a human outside PPC, each blocking something named in the audit.

## The one thing to hold on to

**PPC executes a declaration it does not make.**

The LTSF system decides the archetype, the risk tier, the floor price, the salvage value, the unit count, the cliff date and the terminal option. This audit reads all seven and never derives any of them. Where a field is missing, the run stops and returns the row — it does not estimate.

What PPC owns is narrow and worth doing well: whether traffic can clear these units before the next fee bracket, at what click price, and what to build.

## Why the objective changes everything

Normally advertising buys rank and market share. On aged stock the fee rises with age and steps sharply at bracket boundaries, so the objective becomes **net recovery per unit moved against the declared alternative**. Rank, share and defence metrics stop applying to these units on the day of the tag.

This is why a bid that loses money against price can still be correct: every advertised sale also avoids a charge. And why a wide, cheap net beats a narrow, expensive one — the lane is buying volume at a price where losing costs little, not position.

---

## How to run it

Eight steps. Do them in order — a later step never overturns an earlier one, and an unanswered question stops the run rather than being assumed.

`references/prompts.md` carries the exact prompt for each step, ready to paste.

### Step 0 — Intake

Ask for every input before starting. A partial intake produces an audit that looks complete and is not, which is worse than no audit.

Send the intake request in `references/prompts.md` §0. It lists each file, why it is needed, and what cannot be assessed without it.

Do not begin until the operator has supplied the inputs **or explicitly confirmed which do not exist for this cycle**. Record the confirmed absences — they become the named gaps in the final section.

### Step 1 — Read the declaration

Read the seven declared fields. Any blank or undated field stops the procedure.

Copy them into the audit's opening table with their dates and the source row reference. Everything downstream cites these rather than restating them from memory.

### Step 2 — Correct the context before any verdict

**This is the step most audits skip, and skipping it is how an audit confidently reports the wrong thing.**

Before reading any performance number, ask what would make it misleading. Write each correction as a numbered *Reading* that names the raw conclusion it reverses and the evidence that reverses it. Where an independent source can settle it, state **the check that settles it**.

The corrections that recur on this class of product:

- **Wrong scope.** Campaigns in other portfolios advertise this product's children. Portfolio-scoped numbers miss them.
- **Wrong entity.** Keyword rows alone capture a fraction of spend and produce a cost per order far from the real one.
- **Contaminated windows.** A deal window or a price change inside the comparison period makes a week-on-week read meaningless.
- **Wrong term.** Rank and performance stories differ completely depending on which term is described.
- **Provenance.** Which child was actually enabled over the window the history spans.

Read `references/decision-framework.md` §2 for how to work each one.

### Step 3 — Build the ceiling

The maximum a click may cost. Computed, never chosen.

Build it line by line from realised price down through fees and refund cost to contribution before advertising, then add the objective's own term, ending in one **ceiling adopted** figure with headroom against current ad cost per unit.

Two things that are easy to get wrong and expensive:

- **The avoided charge is counted over a stated, bounded acceleration window** — not the whole projected hold. Counting the full runway inflates the ceiling on exactly the stock least able to justify it.
- **Sunk cost of goods appears in no term.** It is identical across every option for the same units, so it can never change which option wins, and showing it makes every option on an underwater product look like a loss.

Formulas and the full rule set: `references/decision-framework.md` §3.

### Step 4 — Compute the required pace

Units left divided by days to the cliff gives units per day. Divided by conversion gives clicks per day. Then read market click price **at that volume, not at the volume the lane currently buys** — the price that clears a small number of clicks is not the price that clears a large one.

### Step 5 — The clearability gate

**Ask whether traffic can clear this stock at all, before deciding anything about how to build.**

Three answers: open, split, or closed. A closed lane is a correct outcome, not a failure — it is the finding the deciding system needs in order to move the price or take the terminal option.

**Charge size never overrides this gate.** The largest charge in a portfolio is frequently the least clearable stock in it, because low velocity is what aged it. Clearability decides whether to build; charge only decides how much.

Where converter evidence is too thin to read a conversion rate, the lane is neither open nor closed but **unmeasured** — see `references/decision-framework.md` §5.3 for the resolution.

### Step 6 — Decide the existing account

Work the live campaigns against the ceiling and the archetype's boundaries. Every row that changes carries an Action and a Reasoning.

Reasoning standard: `references/output-format.md` §3.

### Step 7 — Build the new campaigns

Six build classes, how many depending on the charge band. The reach layer buys cheap traffic; the proven layer keeps its terms at the ceiling. Both run at once.

The separation rules are what make the numbers readable afterwards — read `references/campaign-builds.md` in full before staging anything.

### Step 8 — Write it up

Follow the section spine and the writing standards in `references/output-format.md`. Then run the validation gate at the end of that file. **Nothing ships with a failure open.**

---

## The decisions this audit does not make

Route these out with the evidence attached, and do not quietly work around them with a bid:

- The floor price, the salvage comparison, the archetype, the risk tier, the terminal option
- Discount, coupon and deal depth
- Whether to remove, liquidate or dispose
- Anything needing a number that neither the criteria authority nor the LTSF declaration carries — name what the decision needs, state that neither answers it, and file it rather than inventing a value

An operator who computes one of these has made the most common and most expensive error available on this lane.

---

## Reference files

| File | Read it when |
|---|---|
| `references/prompts.md` | Every run. Carries the exact prompt for each step |
| `references/decision-framework.md` | Steps 1–5. Inputs, decision order, ceiling and pace formulas, gates, archetype boundaries |
| `references/campaign-builds.md` | Step 7. The six build classes, bid tiering, separation rules, staging checks |
| `references/output-format.md` | Step 8, and skim before Step 2. Section spine, writing standards, validation gate |
| `references/worked-example.md` | When a step is ambiguous. A real run with its numbers, including where it went wrong |

## Scale honesty

A fully argued case for every row — every candidate cause named, evidence for and against, a falsification test, the alternatives rejected and why — cannot be produced reliably across hundreds of rows at once. Produce it in batches, highest-spend first, and say which rows got that depth.

Producing it at full scale anyway generates text that reads complete and is not. The failure mode is not an obviously thin answer; it is a confidently thorough-looking one.
