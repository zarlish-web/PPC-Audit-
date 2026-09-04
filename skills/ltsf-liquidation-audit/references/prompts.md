# Exact prompts, by step

Paste these as written. Each is built so the answer it produces can be checked by someone who was not in the room.

Placeholders in `[SQUARE BRACKETS]` are filled before sending.

---

## §0 — Intake request

Send this before any analysis. Every line names why the file is needed, so an operator who cannot supply one can say what it costs rather than silently omitting it.

```
I am running a liquidation / LTSF clearance audit for [PRODUCT] on [MARKETPLACE].
Please provide the following. If any does not exist for this cycle, say so
explicitly rather than leaving it out — a confirmed absence is recorded as a
named gap; a silent one produces an audit that looks complete and is not.

DECLARATION (required — the run stops without all seven)
 1. Archetype for this product, with date assigned and owner
 2. Risk tier
 3. Floor price
 4. Salvage value per unit, and the winning terminal option
 5. Remaining aged units, broken out by age bracket
 6. Cliff date of the largest bracket
 7. Contribution at the current price, and contribution at the floor price

ECONOMICS
 8. Profit export covering 30 days, weekly, and per SKU
 9. Refund rate and refund cost per unit, per child where available
10. Fee breakdown per unit — referral and fulfilment
11. Landed cost per unit if freight and duty sit outside the standard cost field

INVENTORY AND THE CLOCK
12. FBA inventory and aged-inventory snapshot, dated
13. The LTSF charge file for the current month
14. Any removal, liquidation or disposal orders in flight, with unit counts

ADVERTISING
15. Sponsored Products bulk export, full, current
16. Search term report, 30 or 60 day
17. Placement report
18. Any Sponsored Brands and Sponsored Display activity for this product
19. The previous cycle's decided file and its logged predictions, if one exists

KEYWORDS AND MARKET
20. Master keyword list with syntax tag, relevancy, search volume, suggested bid
21. Search query performance for the parent
22. Competitor set with prices, ratings and review counts

STRUCTURE
23. Variation map naming which children hold the aged units
24. Which children are preferred and which are backup
25. Listing content for the affected children — title, bullets, images status

Two questions that are not files:
 A. What has already been tried on this product, and what did it produce?
 B. Is there anything about this product I would not learn from the data?
```

---

## §1 — Read the declaration

```
Read the seven declared fields for [PRODUCT] and write them into a table with
each field's value, its date, and the source row reference.

Do not derive, estimate or infer any of them. If a field is blank or undated,
stop and name the field and the decision it blocks.

Then state, in one line each: what the archetype permits and forbids, and what
posture the tier sets.
```

---

## §2 — Context corrections

This prompt does most of the work in the audit. It is deliberately adversarial toward the raw numbers.

```
Before reading any performance number for [PRODUCT], find what would make those
numbers misleading.

Work these five, and add any others the data suggests:

1. SCOPE — are there campaigns outside this product's portfolio advertising its
   children? Compute spend both ways and state the difference.
2. ENTITY — does reading keyword rows alone capture all the spend? What share
   does it capture, and what does the cost per order look like at each level?
3. WINDOW — do any deal windows or price changes fall inside the comparison
   periods? Name the dates and say which comparisons are void.
4. TERM — does the performance story differ depending on which term is
   described? State each reading separately rather than averaging them.
5. PROVENANCE — which child was actually enabled over the window the history
   spans? Was every campaign advertising the child its name implies?

For each correction, write it as a numbered Reading in this form:

  Reading N — [the raw conclusion this reverses].
  [What is actually true, with the numbers.]
  The check that settles it: [an independent source that confirms it, if one exists].

If a correction cannot be settled, say so and mark what it makes unreadable.
A correction that reverses nothing does not need writing up.
```

---

## §3 — The ceiling

```
Build the ceiling for [PRODUCT] line by line, per unit shipped:

  realised average selling price          [read, with the window stated]
  minus referral fee
  minus fulfilment fee
  minus refund cost at the current rate
  = contribution before advertising
  plus the avoided charge over a BOUNDED acceleration window
  = CEILING ADOPTED

State the acceleration window you used and why that length. Do not count the
whole projected hold — that inflates the ceiling on exactly the stock least able
to justify it.

Then:
  - current ad cost per unit shipped, on a stated basis
  - headroom = ceiling minus current
  - the maximum click price implied, = ceiling x conversion rate

Sunk cost of goods appears in no line. It is identical across every option for
these units, so it cannot change which option wins.

State which declared value you subtracted and which direction it moved the
ceiling. Do not carry an assumption about its sign — both signs occur.
```

---

## §4 — Required pace

```
For [PRODUCT]:

  required units per day  = remaining units / days to the declared cliff date
  required clicks per day = required units per day / converter conversion rate
  required daily budget   = required clicks per day x market CPC at that volume

Read market CPC at the volume the lane needs, not the volume it currently buys,
and state both figures so the difference is visible.

Also compute, from realised velocity:
  months to clear at current velocity = aged units / realised units per month

Show that against the days remaining to the cliff.
```

---

## §5 — The clearability gate

```
Decide whether traffic can clear this stock, and route:

  LANE OPEN   — market CPC at the required volume is at or under the ceiling.
                Fund the full required-clicks budget.
  LANE SPLIT  — only a residual click volume clears at or under the ceiling.
                State how many units PPC clears and how many route to the
                terminal option.
  LANE CLOSED — no click volume clears at or under the ceiling. Build nothing.
                Hand back these five numbers and nothing else:
                  required clicks per day, the ceiling, market CPC at required
                  volume, units clearable at the ceiling, the residual.

A closure written as a conclusion rather than as those five numbers cannot be
acted on and will be returned.

Charge size does not override this gate. If this product carries a large charge
and the arithmetic closes the lane, the size of the charge is the reason to close
it faster, not to spend into it.

If converter evidence is too thin to read a conversion rate, the lane is
UNMEASURED, not closed. Say so, state the dated read that would resolve it, and
route to the reach layer at floor bids to accumulate the clicks.
```

---

## §6 — Decide the existing account

```
Work every live campaign and keyword for [PRODUCT] against the ceiling and the
archetype's boundaries.

Every row that changes carries:
  Action    — the concrete change, with prior and new values
  Reasoning — why that action follows, with the numbers it rests on

Cover at minimum:
  - rows above the ceiling
  - rows with clicks and no orders, at the sufficiency line
  - budget-truncated campaigns
  - placement premiums that do not earn their cost
  - spend resolving to stock that cannot be sold
  - duplicate ownership of the same term

Do not write a reasoning cell that contains no number. Do not write "optimise"
or "monitor".
```

---

## §7 — New campaign builds

```
Build the reach layer for [PRODUCT] at the intensity its charge band sets, given
the lane is open or split.

For each campaign state: build class, targeting, match type, SKU set, bid, daily
budget, and the keyword set with the tier each keyword sits in.

Rules that must hold and are checkable from the file:
  - No bid above the ceiling.
  - Bidding strategy cannot raise a bid at auction. Fixed or down-only.
  - One keyword lives in one campaign per ad product. Proven converters are
    negative-exacted out of every reach campaign.
  - Bid tiers separate by keyword, never by price on the same keyword.
  - Archetype B: aged children only. No parent, no healthy child.
  - Placement multipliers at zero.

Then run the staging checks and report each as pass or fail with evidence.
```

---

## §8 — Write the audit

```
Write the audit for [PRODUCT] following the section spine and writing standards.

Non-negotiables:
  - Every table states what it decides.
  - Every number carries a basis: measured on this product, inferred from
    market, or from a test.
  - Measured and modelled effects are separated.
  - State what the analysis deliberately does not claim, and why.
  - Empty sections are written with the reason they are empty, not omitted.
  - Every action carries one named owner and a date.
  - End with figures to reconcile, named gaps, what would reverse the main
    verdicts, and the numbered decisions requested.

Then run the validation gate. Report every failure. Nothing ships with one open.
```

---

## §9 — Closing a lane

Use when Step 5 returns closed.

```
Write the lane-closure handback for [PRODUCT]. Five numbers, nothing else:

  1. required clicks per day
  2. the ceiling
  3. market CPC at the required volume
  4. units clearable at the ceiling
  5. the residual routed to the terminal option

Then the re-entry criterion, written as the declaration change that would reopen
the lane — a lower floor price, a deal-window conversion rate, or more days to
the cliff — with a review date.

Do not widen the term set in response to a closure. The arithmetic is the
finding, and it is what the deciding system needs in order to move the price or
execute the terminal option.
```
