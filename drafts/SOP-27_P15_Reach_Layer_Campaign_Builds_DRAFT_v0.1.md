# SOP-27 · P15 — Reach-Layer Campaign Builds (LTSF Clearance)

**Draft v0.4 · for review · proposed addition to SOP-27 v2.0 Element 4**

Status: DRAFT. Not yet ratified. Decisions recorded at Section 10, open items at Section 11.

**This procedure carries zero local thresholds.** Every number it uses is named by its source and read at run time. Where a value appears below it is a *placeholder in a formula*, never a setting. An operator who finds a threshold written into this document has found a defect.

---

## 0. What this procedure is

P15 is the **decision framework for building new campaigns on stock carrying an LTSF tag**. Given one product with a liquidation objective and the inputs at Section 1, it states the order the questions are asked in, the calculations that answer them, what each outcome permits, and the standard the written conclusion must meet.

It is built to be run. An operator or an agent holding this document and the required inputs should be able to produce the full analysis and defend every step of it without asking what a number should be — because every number is read, not chosen.

**P15 adds to SOP-27. It deletes nothing.** P2, P5, P6, P7, P8, P9, P10, P12 and P14 stand unchanged. SOP-27 covers what to do with campaigns that already exist when a tag lands. P15 covers building new ones.

---

## 1. Inputs

Analysis does not start until each row reads present and dated. A missing row suppresses its dependent step and is recorded in T7 Manifest per v4.0 gate G8. **No input is estimated, and no missing input is worked around.**

| # | Input | Source | What it decides here |
|---|---|---|---|
| I-1 | The seven declaration fields | LTSF row, per P1 | Whether P15 may run at all |
| I-2 | Archetype | LTSF declaration | The boundaries at Section 7 |
| I-3 | Risk tier | LTSF declaration | Cadence and posture |
| I-4 | Floor price, salvage value per unit, winning terminal option | LTSF declaration | The R2 ceiling |
| I-5 | Remaining units by bracket, cliff date | LTSF cliff calendar | The R3 pace |
| I-6 | Monthly charge per product | LTSF charge file | The intensity band at Section 6 |
| I-7 | Realised velocity per SKU | LTSF charge file or SellerBoard | The clearability gate at Section 5 |
| I-8 | Converter CVR on the proven set | T2 block K5, subject to gate G2 | The ceiling and the required-clicks figure |
| I-9 | Market CPC at the required volume | T4 "Expected CPC" and current suggested bids | Whether the lane opens |
| I-10 | Keyword set with syntax tag, relevancy, search volume, suggested bid | MKL, subject to gate G12 | Tier assignment at Section 8 |
| I-11 | Variation map naming the aged children | D2 | Archetype B scope |
| I-12 | Live campaign and keyword inventory for the product | Bulk export | The one-keyword-one-home check |

---

## 2. The decision order

Every question is answered in this order. **A later question is never used to overturn an earlier one**, and an unanswered question stops the run rather than being assumed.

```
Q1  Is the declaration complete?            no  -> STOP. Return to the LTSF Owner (P1).
Q2  What does the archetype permit?             -> sets boundaries (Section 7)
Q3  What is the economic ceiling?               -> R2 (Section 3)
Q4  What pace is required?                      -> R3 (Section 4)
Q5  Can traffic clear the units at all?     no  -> STOP building. Route to P14 (Section 5).
Q6  How much of the structure is built?         -> charge band (Section 6)
Q7  What is built, and how is it separated?     -> Sections 8 and 9
Q8  How is the conclusion written?              -> Section 12
```

Q5 is the gate. Everything after it is conditional on it.

---

## 3. Q3 — the economic ceiling

The ceiling is the maximum a click may cost. It is computed, never chosen, and it is recomputed whenever any of its inputs move.

**Terminal-tagged units:**

```
allowable ad cost per unit  =  net recovery at the salvage price
                             − the winning alternative's per-unit value

maximum liquidation CPC     =  allowable ad cost per unit × converter CVR
```

**Archetype D, where the units are aged but not terminal:**

```
spend ceiling per unit      =  contribution above the floor price
maximum CPC                 =  spend ceiling per unit × converter CVR
```

**Rules that govern the computation**

1. Both subtrahends are **read from the declaration**. PPC computes neither.
2. **Sunk COGS appears in no term.** A computation citing acquisition cost is failure mode F2 (R7, LTSF Principle 2).
3. The ceiling is a function of five declared inputs — floor price, salvage value, unit count, cliff date and CVR. It is **stale the moment any one moves**, and carrying a stale ceiling is failure mode F6.
4. Where gate G9 marks reads PROVISIONAL after a price or depth change, the ceiling **holds at its last dated value** and is not recomputed on a provisional CVR.
5. Where converter evidence sits below the gate G2 line, the ceiling **cannot be computed**. See Section 5.3.

**The sign of the subtrahend is not assumed.** Whether subtracting the alternative raises or lowers the ceiling depends on the sign of the declared value in that cycle, and both signs occur. The analysis states the value it read and the direction it moved the ceiling. It never carries a stated expectation about the sign from this document or any other.

---

## 4. Q4 — the required pace

```
required units per day   =  remaining units ÷ days to the declared cliff date
required clicks per day  =  required units per day ÷ converter CVR
required daily budget    =  required clicks per day × market CPC at that volume
```

**Market CPC is read at the volume the lane needs, not at the volume it currently buys.** The price that clears a small number of clicks a day is not the price that clears a large one, and reading the current figure understates the cost of the pace.

Re-derive whenever remaining units, the cliff date or the CVR moves.

---

## 5. Q5 — the clearability gate

**P4 runs before P15 builds anything.**

| P4 result | What P15 does |
|---|---|
| **LANE OPEN** | Build at the band's intensity (Section 6). |
| **LANE SPLIT** | Build sized to the clearable residual only. State the residual routed to the terminal option. |
| **LANE CLOSED** | **Build nothing.** Route to P14 with the five closure numbers. |

### 5.1 Charge never overrides the gate

Charge measures what stock costs to hold. It says nothing about whether traffic can move it, and the two are frequently inverted — the largest charge in a portfolio is often the least clearable stock in it, because low velocity is what aged it.

**Clearability gates. Charge only sizes.** A closed lane at the top of the charge table receives no build, and the size of its charge is the reason to close it faster, not to spend into it.

### 5.2 The clearability read

```
months to clear at current velocity  =  aged units ÷ realised units per month
```

Read against the time remaining to the declared cliff. Where the figure exceeds the runway by a wide margin, the arithmetic has already answered Q5 and the P4 traffic check confirms it rather than rescuing it. **No bid, budget or coverage change closes a gap of that shape**, and proposing one is the error this section exists to prevent.

### 5.3 Where the ceiling cannot be computed

Where converter evidence sits below the gate G2 sufficiency line, the CVR is unreadable, so the ceiling and the required-clicks figure are both unavailable. The lane is neither open nor closed; it is **unmeasured**.

The resolution is the reach layer itself, at its floor bid, run to accumulate clicks to the sufficiency line. This is legal under Section 9 because it buys sales rather than position and costs a small fraction of the accruing charge. It is recorded as an unmeasured lane with a dated read, and Q3 and Q4 are answered once sufficiency lands.

**A lane is never left in this state undated.** An unmeasured lane accrues the charge exactly like a measured one.

---

## 6. Q6 — intensity

Structure does not change with charge. **How much of the structure is built does.**

**Band boundaries are read from the LTSF Master** — Section 7.1 for the CRITICAL tier line and Section 7.4 for the escalation line. They are not restated here and not set locally.

| Dial | Low band | Middle band | High band |
|---|---|---|---|
| Build types | Widest-net build only | Widest-net plus keyword-level builds | Full set, all surfaces |
| Budget | Smallest | Moderate | Largest — the primary dial |
| Surfaces | Sponsored Products | Sponsored Products | Add Sponsored Brands and Sponsored Display |
| Grouping depth | Single group | Group by attribute | Group by attribute and by band |
| Check cadence | The standing weekly pass | Weekly | Daily inside the closing window before the cliff |
| **Bid ceiling** | **R2** | **R2** | **R2 — unchanged** |

**The bottom row is a hard rule.** A larger charge buys more coverage, more budget and more surfaces. It never buys a higher click price. The charge is already inside the ceiling's own arithmetic; letting it raise the ceiling counts it twice.

---

## 7. Q2 — archetype boundaries

Structure is the same for all four. The archetype sets what may be touched.

| Archetype | Boundary on the reach layer |
|---|---|
| **A — Fixable Demand** | Reach traffic only. A conversion defect is not fixed by buying more clicks; the listing repair runs in parallel under LTSF Family 1. Scaling a defect multiplies it. |
| **B — Variation Overstock** | Only the aged children named by the D2 map enter any campaign. Parent and healthy children are excluded from every SKU list and every group. No family-wide move. LTSF hard rule; breaching it is failure mode F8. |
| **C — Structurally Dead** | The reach layer runs. **No ranking spend of any kind, at any charge level, ever.** |
| **D — Aged Healthy** | The product still sells at margin, so budget headroom is larger at the same band. No retag and no quarantine — reach campaigns sit alongside the standing structure. |

---

## 8. Q7a — what is built

Six build classes. Which are used is set by Section 6; **all of them obey Sections 3, 7 and 9.**

| Class | Shape | Purpose |
|---|---|---|
| **B1** Widest net, automatic | One automatic-targeting campaign over the charged SKU set | Cheapest discovery with no keyword research |
| **B2** Widest net, manual | The charged SKU set against platform-suggested keywords on the broadest match available | The same reach with keyword-level reporting |
| **B3** Attribute groups | SKUs grouped by a shared attribute; a small number of that attribute's highest-volume roots from the MKL, on the controlled-broad match types | Relevance without cost |
| **B4** Band groups | The charged set split by charge band, one campaign each | Steers budget and attention to where the charge is |
| **B5** Brand surface | The same wide, low-bid approach in Sponsored Brands | Adds a surface at the high band |
| **B6** Display surface | Retargeting and high-intent audiences on the aged SKUs | Judged on cost per acquisition against the R2 allowable ad cost, per v4.0 S-F5 and S-F6 — never on a standing efficiency band |

### 8.1 Why the exact head is avoided

Exact match on a high-volume term clears above the R2 ceiling. Bidding the ceiling there wins no impressions, so the spend buys silence.

The reach layer therefore runs on the match types where a low bid still wins the tail. **This is a consequence of the ceiling, not a preference** — where the ceiling rises, for instance at a deal-window CVR under P11 step 4, the same comparison is re-run and the exact head may re-enter.

### 8.2 Bid tiers

On the broader match types, one keyword matches many search terms at widely different prices. **The bid decides which price band of terms is reachable at all.** It is a filter on reachable traffic, not a lever on position.

Where tiers are used, they are derived from the MKL's own suggested-bid distribution across the assigned keyword set, **all at or under the R2 ceiling**. The number of tiers follows from the spread in that distribution; a set with no spread takes one tier.

Each keyword sits in exactly one tier. Tiers are read against **cost per unit moved versus the R2 allowable ad cost**, never against a standing efficiency band.

---

## 9. Q7b — the separation rules

### 9.1 One keyword, one home

> **A keyword appears in exactly one campaign per ad product.**

**Scoped per ad product, not across the lane.** Sponsored Products, Sponsored Brands and Sponsored Display do not compete in the same auction, so the same keyword running in a Sponsored Products campaign and a Sponsored Brands campaign is correct coverage, not self-competition. The rule bites *within* an ad product, where two campaigns genuinely contest one slot.

Applies across the proven layer and the reach layer together, within each ad product. Two consequences at build:

1. Proven converters are negative-exacted out of every reach campaign.
2. A keyword appears in one bid tier only. **Tiers are separated by keyword, never by price on the same keyword.**

**Why.** The platform admits only one of an advertiser's campaigns into any one auction, normally the highest bidder. Where one keyword sits in several campaigns at several bids, the highest takes the traffic — including the cheap traffic the low-bid campaign was built to catch. The lower tiers then run near-idle, and their results read as failure when they never served. Separating by keyword removes the overlap and makes each tier's numbers real.

### 9.2 The two layers

| | Proven layer | Reach layer |
|---|---|---|
| Contents | Terms carrying orders at or above the G2 line | Automatic targeting and the broader match types |
| Bid | Up to the R2 ceiling | At or under the R2 ceiling |
| Purpose | Certainty | Coverage |
| Governed by | P6, P9 | P15 |

Both run at once. Neither replaces the other. **Proven-converters-only is not weakened by the existence of the reach layer**; it governs its own layer exactly as before.

### 9.3 The test boundary

R4 bars ranking spend on tagged units and P9 bars experiments on Archetype C. Those rules stand. This states what they reach.

> **Allowed — a reach test.** Buys sales at bids at or under the R2 ceiling. Tiers, match types, groups, surfaces. Costs little; a null result is cheap.
>
> **Barred — a ranking test.** Buys position. Any bid above the ceiling, any top-of-search premium, any funded push, any rank objective.

**The dividing line is checkable from the bulk file: does the bid sit above the R2 ceiling?** Above it, barred. At or under it, allowed.

This is consistent with SOP-27 §1.3.1, which excludes tests that spend real money to buy *information* inside a decision window too short to use it. A reach test buys sales, not information.

---

## 10. Q8 — the written analysis

The output of P15 is not a campaign list. It is **an analysis a reviewer can check without rebuilding it.** Every conclusion carries these, in this order:

| # | Element | Standard |
|---|---|---|
| 1 | **The declaration read** | The seven fields with their dates and the LTSF row reference. No field restated from memory. |
| 2 | **The ceiling** | The formula, each input with its source and date, the result, and which direction the subtrahend moved it. |
| 3 | **The pace** | Required units per day, required clicks per day, and the market CPC read at that volume — stated as a different figure from the current CPC. |
| 4 | **The clearability verdict** | Months to clear at current velocity against the runway, then the P4 result: open, split, closed or unmeasured. |
| 5 | **What follows from it** | The build set, the band that sized it, and the archetype boundary that scoped it. On a closed lane: the five P14 numbers and nothing else. |
| 6 | **The separation** | That one-keyword-one-home holds, evidenced from the bulk. |
| 7 | **The prediction** | Units expected cleared by the cliff date, its basis tag (HIST / MARKET / TEST), and the dated read. An untagged prediction is not a weak prediction; it is no prediction. |
| 8 | **The expiry** | The review date, set to the cliff date. No terminal decision is open-ended (LTSF Principle 5, R6). |

**Banned in this analysis:** any sentence without a number; any threshold not traced to v4.0 or the LTSF declaration; any recommendation to raise a bid above the ceiling; any conclusion stated as a word where the framework produces a figure. A lane closure written as "PPC cannot clear this" rather than as the five numbers is returned unread (failure mode F11).

---

## 11. Staging checks

Run before any set goes to #38.

1. No keyword string appears in more than one campaign **within the same ad product**. Cross-product repetition is expected and is not a finding.
2. Every proven converter present as a negative exact in every reach campaign.
3. No bid above the R2 ceiling, and the ceiling dated later than all five of its inputs.
4. No placement multiplier above zero on any tagged entity (R4).
5. No rank or push objective anywhere in the set (R1, R4).
6. Archetype B: no parent and no healthy child in any SKU list.
7. Every campaign carries the cliff date in its name (R5) and expires at it (R6).
8. Every campaign on the #37 automation exclusion list, and the addition recorded.
9. Every build carries a logged prediction with its basis tag and a dated read.
10. P4 result recorded for the SKU, and the build consistent with it.

---

## 12. Decisions recorded

| ID | Decision |
|---|---|
| D-1 | Proven-converters-only survives, governing its own layer, unweakened. |
| D-2 | The reach layer is added on top. Existing SOP-27 procedures unchanged. |
| D-3 | Testing is permitted where it buys sales at or under the ceiling. Ranking tests remain barred. |
| D-4 | The approach applies to all four archetypes. |
| D-5 | Intensity is gated by clearability and sized by charge band. The ceiling never scales with either. |
| D-6 | Archetype rules remain in force as boundaries. |
| D-7 | One keyword, one home, **per ad product**. Tiers separate by keyword, never by price on one keyword. Scoped per ad product at v0.4 after testing against a live decided bulk, where cross-product repetition proved correct and within-product overlap was already absent. |
| D-8 | The exact head is avoided as a consequence of the ceiling, re-testable when the ceiling moves. |
| D-9 | This procedure carries no local thresholds. Bands, gates and limits are read from their authorities at run time. |

---

## 13. Open items

Not written into the procedure. Each needs a decision before ratification.

| ID | Item |
|---|---|
| OPEN-1 | **The R2 subtrahend — answered by practice, wording still to correct.** SOP-27 §1.2 and P3 subtract the winning salvage option. WE-2 and Economics case E7 subtract the charge avoided. A live clearance audit reviewed at v0.4 builds its adopted ceiling as contribution before advertising **plus storage avoided over a bounded acceleration window**, which is the charge-avoided reading. Practice therefore follows E7, not the salvage wording in §1.2 and P3, and those two need correcting to match. Two details from that build are worth carrying into the rule: the avoided charge is counted over a **stated, bounded window** rather than the whole projected hold, and the ceiling is tracked as **ad cost per unit shipped against the ceiling**, not only as a CPC. |
| OPEN-2 | **v4.0 scenario S-A10** puts LTSF-burdened products on a profit-only posture and routes velocity requirements away from PPC. The reach layer is low-cost by construction, so the clash is narrower than for R2, but the rule as written still reaches this lane. |
| OPEN-3 | **A budget limit for the reach layer.** Budget is named the primary intensity dial and has no stated cap. The proven lane is sized by required clicks; the reach layer has no equivalent sizing rule. |
| OPEN-4 | **Counterparty procedures.** #12 carries no procedure that builds a liquidation campaign, #29 no wall specification for one, and #38 and #26 do not mention the lane. P15 cannot execute end to end until at least #12 and #29 carry matching steps. |
| OPEN-5 | **A sufficiency deadline for the unmeasured lane at 5.3.** The reach layer resolves an unmeasured lane, but nothing states how long it may stay unmeasured before the lane is closed on the absence of evidence. |

---

*Inspiratek & Ecotero LLC · Confidential · DRAFT — not for deployment until Section 13 is closed*
