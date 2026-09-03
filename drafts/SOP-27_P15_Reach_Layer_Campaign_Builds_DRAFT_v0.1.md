# SOP-27 · P15 — Reach-Layer Campaign Builds (LTSF Clearance)

**Draft v0.2 · for review · proposed addition to SOP-27 v2.0 Element 4**

Status: DRAFT. Not yet ratified. Built from the decisions recorded in Section 8 below.

---

## Why this procedure exists

SOP-27 v2.0 covers what to do with campaigns that **already exist** when a tag lands: retag them, quarantine them, shut off the wrong spend, keep proven converters at the ceiling.

It says nothing about **building new campaigns to bring in more traffic**. That work is done in practice and had no written procedure. P15 is that procedure.

P15 **adds to** SOP-27. It deletes nothing. P2, P5, P6, P7, P8, P9, P10, P12 and P14 stand unchanged.

---

## 1. Verdict and scope

**VERDICT: the reach layer buys cheap traffic, never position.** Its job is to convert aged units into sales from traffic the proven-converter set does not touch, at a click price low enough that a run of clicks without a sale costs very little. Every rule below exists to keep the click price down and the coverage wide. A bid raised to win a position is not this layer and is barred by R4.

**Runs on:** any SKU carrying an LTSF terminal or at-risk tag, all four archetypes.

**Does not decide:** archetype, tier, floor price, salvage value, units, cliff date, or the terminal option. Those are read from the LTSF declaration per P1 and are never derived here.

### 1.1 The two layers

| | Proven layer (existing) | Reach layer (this procedure) |
|---|---|---|
| Contents | Terms carrying orders at or above the G2 sufficiency line | Auto targeting, broad, broad-modifier and phrase |
| Match types | Exact and auto close match | Auto, broad, broad modifier, phrase |
| Bid | Up to the R2 maximum liquidation CPC | At or below the R2 maximum liquidation CPC |
| Purpose | Certainty — terms known to convert | Coverage — find cheap sales anywhere |
| Governed by | P6, P9 | P15 |

Both run at the same time. Neither replaces the other.

### 1.2 Why exact head terms are avoided

Exact match on a high-volume term clears at a CPC well above the R2 ceiling. Bidding the ceiling on such a term wins no impressions, so the spend buys silence. The reach layer therefore runs on the match types where a low bid still wins the tail: auto, broad, broad modifier and phrase. This is not a preference; it follows from the ceiling, and where the ceiling rises (a deal window per P11 step 4) the same test is re-run and exact may re-enter.

---

## 2. The one-keyword-one-home rule

> **A keyword appears in exactly one liquidation campaign.**

Applies across the whole liquidation lane — proven layer and reach layer together.

Two consequences at build:

1. **Proven converters are negative-exacted out of every reach campaign.** The proven layer owns those terms.
2. **A keyword appears in one bid tier only.** Tiers are separated by keyword, never by putting the same keyword at two prices.

**Why.** Amazon admits only one of an advertiser's campaigns into any one auction, and normally selects the highest bidder. Where the same keyword sits in several campaigns at different bids, the highest-bid campaign takes the traffic — including the cheap traffic the low-bid campaign was built to catch. The lower tiers then run near-idle and their results read as failure when they never served. Separating by keyword removes the overlap and makes each tier's numbers real.

**Checkable at staging:** no duplicate keyword string across the lane's campaigns; every proven converter present as a negative exact in every reach campaign.

---

## 3. Build types

All six are available. How many are built is set by charge (Section 4).

### 3.1 B1 — Catch-all auto

One auto campaign holding every SKU currently carrying a charge. Bid at or below the R2 ceiling. One ad group. Let it run and read the search-term report weekly.

Purpose: cheapest possible discovery across the whole charged set, with no keyword research required.

### 3.2 B2 — Catch-all manual broad

Every charged SKU, plus the keywords Amazon suggests for them, on broad match at a low bid.

Purpose: the same wide net as B1 but with keyword-level reporting, so terms can be read and moved.

### 3.3 B3 — Tiered attribute groups

Where the charged set spans many SKUs, group them by a shared attribute — same size, same colour, or a shared keyword root. For each group take the top search-volume keywords for that attribute from the MKL, **2 to 5 keywords per group**, and run them on **phrase** or **broad modifier**.

Broad modifier is written with a `+` before each token (`+bamboo +sheets +queen`). It gives more control than plain broad while still reaching a wide term pool.

Purpose: relevance without cost. A queen-size group bidding on queen-size roots reaches buyers already asking for what the aged units are.

This is the layer that tiers by bid (Section 5).

### 3.4 B4 — Charge-band campaigns

Split the charged SKUs into high, medium and low charge bands and give each band its own campaign, so budget and attention can be steered to where the charge actually is.

Band measure: **dollars of LTSF charge per month per product**, read from the LTSF row. Boundaries per 4.0.

### 3.5 B5 — Sponsored Brands

The same wide, low-bid approach in Sponsored Brands, pointed at the Brand Store clearance page where one exists (P11 step 2).

### 3.6 B6 — Sponsored Display

Retargeting detail-page viewers of the family, and high-intent audiences, with creative featuring the aged SKUs. Bids low. Judged on cost per acquisition against the R2 allowable ad cost per unit, per P11 step 1 and v4.0 scenarios S-F5 and S-F6 — never on a standing efficiency band.

---

## 4. Intensity is set by charge, gated by clearability

### 4.0 The gate runs first

**P4 runs before P15.** P15 builds nothing until the P4 lane test has returned a result for the SKU.

| P4 result | What P15 does |
|---|---|
| **LANE OPEN** | Build at the charge band's intensity (4.1). |
| **LANE SPLIT** | Build at the charge band's intensity, sized to the clearable residual only. State the residual routed to the terminal option. |
| **LANE CLOSED** | **P15 does not run.** Route to P14. No reach campaign is built on a lane arithmetic has closed. |

**Charge alone must never set intensity.** Charge measures what the stock costs to hold; it says nothing about whether traffic can move it. The two are frequently inverted: the September charge file carries a product at 27% of the portfolio charge whose aged units clear in 253 months at current velocity. Under a charge-only rule that product draws the largest build in the lane and clears nothing. Clearability gates, charge sizes.

**Charge band boundaries** are the thresholds the LTSF Master already carries, and are not set locally:

| Band | Boundary | Source |
|---|---|---|
| High | ≥ $5,000 per month per product | LTSF Section 7.1, the CRITICAL tier definition |
| Medium | $2,000 to $4,999 per month | LTSF Section 7.4, the RED-tier escalation line |
| Low | under $2,000 per month | the remainder |

### 4.1 The intensity dials

The structure above does not change with charge. **How much of it gets built does.**

| Dial | Low charge | Medium charge | High charge |
|---|---|---|---|
| Build types | B1 | B1, B2, B3 | B1–B6 |
| Budget | Small | Moderate | Large — this is the primary dial |
| Surfaces | SP only | SP | SP + SB + SD |
| Tier depth | One group | Group by attribute | Group by attribute and charge band |
| Check cadence | Weekly (P12) | Weekly | Daily inside the final 14 days |
| **Bid ceiling** | **R2 ceiling** | **R2 ceiling** | **R2 ceiling — unchanged** |

**The bottom row is a hard rule.** A larger charge buys more coverage, more budget and more surfaces. It never buys a higher click price. A charge cannot raise the R2 ceiling, because the ceiling is a function of the declared salvage economics and the conversion rate, and the charge is already inside it.

---

## 5. Bid tiers

Within B3, several bid levels may run at once — for example $0.25, $0.35 and $0.50.

**What the tiers are for.** On broad, broad modifier and phrase, one keyword matches many search terms at widely different prices. The bid decides which price band of terms the campaign can win at all. A low bid reaches only the cheap tail; a higher bid opens a more contested band. The bid is a filter on reachable traffic, not a lever on position.

**How tiers are assigned.** Each keyword goes in exactly one tier. Assign from the MKL, using search volume and suggested bid as the guide:

| Tier | Bid | Keywords assigned |
|---|---|---|
| Low | lowest | Long-tail, low-volume, low suggested bid |
| Mid | middle | Mid-volume roots |
| High | highest, still at or under the R2 ceiling | Head roots, where even the tail of the match is contested |

**Never** put one keyword in two tiers at two prices. That is not a test; it is one campaign serving and two idle.

**Reading the result.** Compare tiers on cost per unit moved against the R2 allowable ad cost, not on ACOS against a standing band. A tier returning no sales after a fair read is closed and its keywords route to the next tier up or out of the lane.

---

## 6. The test rule

R4 bars ranking spend on tagged units, and P9 step 4 bars experiments on Archetype C. Those rules stand. This section states what they do and do not reach, because the reach layer is a form of testing and was being caught by wording aimed at something else.

> **Allowed — a reach test.** Buys sales at bids at or below the R2 ceiling. Bid tiers, new match types, new attribute groups, a new surface. It costs little, and if it returns nothing the loss is small.
>
> **Barred — a ranking test.** Buys position. Any bid above the R2 ceiling, any top-of-search premium, any funded push, any rank objective.

**The dividing line, checkable from the bulk file: does the bid sit above the R2 ceiling?** Above it, the action is a ranking test and is barred. At or below it, the action is a reach test and is allowed.

This resolves the Archetype C problem in SOP-27 §1.3.1. The bar there is on tests that spend real money to buy information inside a decision window too short to use it. A reach test buys sales, not information, and costs a fraction of the bracket rate while running. It is therefore not the class of experiment §1.3.1 excludes.

**It also unblocks the ceiling.** The R2 ceiling needs a conversion rate; a conversion rate needs clicks; gate G2 requires 100 clicks for a CVR read. On a thin set the old wording barred the only activity that could produce those clicks. The reach layer supplies them at a price that does not matter.

---

## 7. Archetype boundaries

Structure is the same for all four. The archetype sets what the reach layer may touch.

| Archetype | Boundary on the reach layer |
|---|---|
| **A — Fixable Demand** | Reach traffic only. Do not attempt to fix a conversion defect by buying more clicks; the listing repair runs in parallel under LTSF Family 1 and its 48-hour SLA. Scaling a defect multiplies the defect. |
| **B — Variation Overstock** | Only the aged children enter any reach campaign. The parent and the healthy children are excluded from every SKU list, every catch-all, and every attribute group. No family-wide budget move. This is an LTSF hard rule and breaching it is failure mode F8. |
| **C — Structurally Dead** | The reach layer runs. No ranking spend of any kind, ever, at any charge level. |
| **D — Aged Healthy** | The product still sells at margin, so budget headroom is larger at the same charge band. No retag and no quarantine — the reach campaigns sit alongside the standing structure rather than replacing it. |

---

## 8. Decisions this procedure records

Recorded from the review session. Each is a ratified position, not an inference.

| ID | Decision |
|---|---|
| D-1 | Proven-converters-only survives. It governs the proven layer and is not weakened. |
| D-2 | The reach layer is added on top. Existing SOP-27 procedures are unchanged. |
| D-3 | Testing is allowed where it buys sales at low bids. Aggressive ranking tests remain barred. |
| D-4 | The catch-all approach applies to all four archetypes. |
| D-5 | Intensity scales with charge, gated first by the P4 lane test. The bid ceiling never scales with charge. Revised at v0.2 against the September charge file: charge alone inverted the priority, sending the largest build to the least clearable stock. |
| D-6 | The archetype rules remain in force as boundaries on the reach layer. |
| D-7 | One keyword, one home, across the whole lane. Bid tiers are separated by keyword, never by price on the same keyword. |
| D-8 | High-volume exact at high bids is avoided, because the lane is not buying rank. |

---

## 9. Open items

Not written into the procedure. Each needs a decision before ratification.

| ID | Item |
|---|---|
| ~~OPEN-1~~ | ~~**Charge band boundaries.**~~ **CLOSED.** Bands read from LTSF Section 7.1 ($5,000, the CRITICAL tier line) and Section 7.4 ($2,000, the RED-tier escalation line). No local threshold required. Recorded at 4.0. |
| OPEN-2 | **The R2 subtrahend — now urgent.** SOP-27 §1.2 and P3 say subtract the winning salvage option (removal, liquidation or disposal net). WE-2 and Economics Set case E7 subtract the LTSF charge avoided. These are different amounts and give different ceilings. **The September charge file settles the sign question against the documents:** all 516 SKUs in the SKU Cash Action Tracker carry a *positive* exit value, $0.37 to $12.14 per unit, with no negatives. P3 step 2's stated basis — *"Because the alternative is usually negative, the subtraction usually raises the ceiling"* — and LTSF §4.2's *"all typically negative or near zero"* are both contradicted by live data. Under the salvage reading every ceiling in the lane is *lower* than the procedure implies, not higher. Every bid in P15 depends on this. |
| OPEN-3 | **v4.0 scenario S-A10.** It puts LTSF-burdened products on a profit-only posture and routes LTSF velocity requirements to deals and pricing, "not to PPC subsidy". The reach layer is low-cost by design, so the clash is smaller than it is for R2, but the rule as written still reaches this lane. |
| OPEN-4 | **Budget cap on the reach layer.** Budget is named as the primary intensity dial but has no stated limit. The P4 required-clicks figure sizes the proven lane; the reach layer has no equivalent. |
| OPEN-5 | **Counterparty procedures.** #12 has no procedure that builds a liquidation campaign, #29 has no liquidation wall spec, #38 and #26 do not mention the lane. P15 cannot execute until at least #12 and #29 carry matching steps. |

---

## 10. Staging checks

Run before any reach-layer set goes to #38.

1. No keyword string appears in more than one campaign in the lane.
2. Every proven converter is present as a negative exact in every reach campaign.
3. No bid exceeds the R2 maximum liquidation CPC, dated within its five inputs.
4. No placement multiplier above zero on any tagged entity (R4).
5. No rank or push objective on any campaign in the set (R1, R4).
6. Archetype B: no parent ASIN and no healthy child in any SKU list.
7. Every campaign carries the cliff date in its name (R5) and an expiry at that date (R6).
8. Every campaign added to the #37 automation exclusion list, and the addition recorded.
9. Every deployed build carries a logged prediction with its basis tag (HIST / MARKET / TEST) and a day-7 read date.

---

*Inspiratek & Ecotero LLC · Confidential · DRAFT — not for deployment until Section 9 is closed*
