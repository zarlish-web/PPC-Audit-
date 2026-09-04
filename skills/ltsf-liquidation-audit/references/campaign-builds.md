# Campaign builds

Step 7 of the run. Read in full before staging anything.

Applies only where the clearability gate returned open or split. **A closed lane builds nothing.**

## Contents

1. The two layers
2. Why the exact head is avoided
3. The six build classes
4. Intensity by charge band
5. Bid tiers
6. The separation rules
7. Settings that defeat the ceiling
8. Staging checks

---

## 1. The two layers

| | Proven layer | Reach layer |
|---|---|---|
| Contents | Terms already carrying orders at or above the sufficiency line | Automatic targeting and the broader match types |
| Match types | Exact, automatic close match | Automatic, broad, broad modifier, phrase |
| Bid | Up to the ceiling | At or under the ceiling |
| Purpose | Certainty — terms known to convert | Coverage — find cheap sales anywhere |

Both run at the same time. Neither replaces the other, and the reach layer's existence does not weaken the proven-converters-only rule — that rule governs its own layer exactly as before.

The reasoning behind the reach layer: on a product being cleared, the proven converter set is usually small. Restricting to it guarantees clearing very little. Casting wide at a price where a run of clicks without a sale costs almost nothing finds volume the narrow set never reaches, and the downside is bounded by the bid rather than by judgement.

---

## 2. Why the exact head is avoided

Exact match on a high-volume term clears at a click price well above the ceiling. Bidding the ceiling there wins no impressions, so the spend buys silence — and a campaign that spends nothing reads as a failed test rather than as a mispriced one.

**This is a consequence of the ceiling, not a preference.** Where the ceiling rises — a deal window lifting conversion, for instance — re-run the comparison and the exact head may re-enter. Re-run it before the window opens, not after it closes.

---

## 3. The six build classes

| Class | Shape | Purpose |
|---|---|---|
| **B1** Widest net, automatic | One automatic-targeting campaign over the charged SKU set | Cheapest discovery, no keyword research needed |
| **B2** Widest net, manual | The charged SKU set against platform-suggested keywords on the broadest match type | Same reach, with keyword-level reporting so terms can be read and moved |
| **B3** Attribute groups | SKUs grouped by shared attribute — size, colour, or a shared keyword root. A small number of that attribute's highest-volume roots from the master list, on the controlled-broad match types | Relevance without cost. A queen-size group bidding on queen-size roots reaches buyers already asking for what the stock is |
| **B4** Charge-band groups | The charged set split by charge band, one campaign each | Steers budget and attention to where the charge actually is, and makes each band's result readable |
| **B5** Brand surface | The same wide, low-bid approach in Sponsored Brands, pointed at a clearance page where one exists | Adds a surface at the top band |
| **B6** Display surface | Retargeting and high-intent audiences on the aged stock | Judged on cost per acquisition against the allowable ad cost per unit, never on a standing efficiency band |

On B3, keep the keyword count per group small. The purpose is a controlled net over a defined attribute, not a keyword dump — a group with too many roots stops being readable and its results cannot be attributed to the attribute.

---

## 4. Intensity by charge band

Structure does not change with charge. **How much of the structure is built does.**

Band boundaries are read from the LTSF authority, not set here.

| Dial | Low band | Middle band | High band |
|---|---|---|---|
| Build classes | B1 | B1, B2, B3 | B1–B6 |
| Budget | Smallest | Moderate | Largest — the primary dial |
| Surfaces | Sponsored Products | Sponsored Products | Add Brands and Display |
| Grouping depth | Single group | By attribute | By attribute and by band |
| Check cadence | Weekly | Weekly | Daily inside the closing window |
| **Bid ceiling** | **unchanged** | **unchanged** | **unchanged** |

**The bottom row is the rule that matters.** A larger charge buys more coverage, more budget and more surfaces. It never buys a higher click price — the charge is already inside the ceiling's own arithmetic, so letting it raise the ceiling counts it twice.

---

## 5. Bid tiers

On the broader match types one keyword matches many search terms at widely different prices. **The bid decides which price band of terms is reachable at all.** It is a filter on reachable traffic, not a lever on position.

### How to tier

Derive the tiers from the master keyword list's own suggested-bid distribution across the assigned set, all at or under the ceiling. The number of tiers follows from the spread in that distribution — a set with no spread takes one tier.

| Tier | Bid | Keywords assigned |
|---|---|---|
| Low | lowest | Long-tail, low-volume, low suggested bid |
| Mid | middle | Mid-volume roots |
| High | highest, still under the ceiling | Head roots, where even the tail of the match is contested |

### The rule, and why it exists

**Each keyword sits in exactly one tier. Never the same keyword at two prices.**

The platform admits only one of an advertiser's campaigns into any one auction, normally the highest bidder. Put one keyword in three campaigns at three bids and the highest takes everything — including the cheap traffic the low-bid campaign was built to catch. The lower tiers run near-idle, and their results read as failure when they never served at all.

That is not a bid test. It is one campaign serving and two idle, producing a conclusion that is exactly backwards.

### How to read the result

Compare tiers on **cost per unit moved against the allowable ad cost per unit**, never against a standing efficiency band. A tier returning no sales after a fair read is closed and its keywords route up a tier or out of the lane.

---

## 6. The separation rules

> **A keyword appears in exactly one campaign per ad product.**

**Scoped per ad product, not across the lane.** Sponsored Products, Sponsored Brands and Sponsored Display do not compete in the same auction, so the same keyword running in a Sponsored Products campaign and a Sponsored Brands campaign is correct coverage, not self-competition. The rule bites *within* an ad product, where two campaigns genuinely contest one slot.

Two consequences at build:

1. **Proven converters are negative-exacted out of every reach campaign.** The proven layer owns those terms. This is for attribution as much as for price — if both layers can serve a term, neither layer's numbers mean anything afterwards.
2. **One keyword, one tier**, per §5.

Where the tagged stock must also leave the standing structure, negative-exact its terms out of the standing campaigns in the same working session. Record the wall list as the audit baseline — a separation staged without its wall list is a status change wearing a structure's name.

---

## 7. Settings that defeat the ceiling

Two platform behaviours will breach the ceiling with nothing visible in the staged file. Both are checked at staging rather than discovered afterwards.

**Bidding strategy.** A strategy that adjusts bids upward can exceed the set bid at auction time. On a clearance campaign that breaks the ceiling with no staged row showing it, and the lane's economics are wrong while the file looks compliant. **Stage a fixed or downward-only strategy.**

**Placement multipliers.** A multiplier raises the effective bid at that placement above the set bid. Multipliers are earned from placement evidence, and clearance stock has no evidence base to earn them from. **Stage them at zero.**

---

## 8. Staging checks

Run all of these before the file goes anywhere. Report each as pass or fail with the evidence.

1. Clearability gate result recorded, and the build consistent with it.
2. No bid above the ceiling, and the ceiling dated later than all of its inputs.
3. Bidding strategy on every new campaign cannot raise a bid at auction.
4. No placement multiplier above zero on any tagged entity.
5. No keyword string appears in more than one campaign **within the same ad product**. Cross-product repetition is expected and is not a finding.
6. Every proven converter present as a negative exact in every reach campaign.
7. No rank or push objective anywhere in the set.
8. Variation-overstock case: no parent and no healthy child in any SKU list.
9. Every campaign carries its expiry, readable without opening the row.
10. Every campaign excluded from automation rules, and the exclusion recorded.
11. Every build carries a logged prediction with its basis and a dated read.
12. Every changed row carries both an Action and a Reasoning, and every Reasoning contains a number.

A failure is fixed, not noted. The point of running them at staging is that all twelve are cheap to fix before deployment and expensive afterwards.
