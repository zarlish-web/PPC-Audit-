# SOP-12 · P13 — Create a dated liquidation campaign

**Draft v0.1 · for review · proposed addition to SOP-12 v2.1 Element 4**

Status: DRAFT. Not yet ratified. Open items at Section C.

**This procedure carries zero local thresholds.** Every value is read from the arriving specification, from v4.0, or from the LTSF declaration.

---

## Why this procedure is needed

SOP-27 issues the dated liquidation campaign specification and states that #12 stands the campaigns up. Its interface contract I-13 gives the timing as *"same week as the tag, per R5"* and the non-arrival consequence as *"the campaign is not created and the tagged units keep serving inside standing campaigns… F3."*

**SOP-12 v2.1 carries no procedure that receives it.** Its twelve procedures cover creation, promotion, demotion, consolidation, taper, pause, event overlay, re-point, bid and budget mechanics, and intraday pacing. None builds a liquidation campaign, and the document does not use the words liquidation, terminal or LTSF anywhere.

So the handover is one-sided. In practice the operator either improvises the build from P1 — which carries rank-objective assumptions that R1 and R4 forbid on tagged units — or the campaign is never built and the units keep serving in standing campaigns, which is SOP-27 failure mode F3.

P13 is the receiving procedure. It **adds** to SOP-12; P1 to P12 stand unchanged.

---

## P13. Create a dated liquidation campaign (30 minutes for the first campaign on a product, 10 minutes per later variation)

**1. Confirm the specification arrived.** The build specification from #27 P15 must be present, carrying: the archetype, the risk tier, the cliff date, the R2 maximum liquidation CPC with its date, the advertised SKU set, the build class, and the P4 lane result. A verbal instruction or a recollection does not start this procedure. Where the specification is absent or a field is blank, the row returns to #27 and nothing is created. **This procedure computes no field it can read, and estimates none it cannot.**

**2. Confirm the lane is open.** Read the P4 result. **LANE CLOSED creates nothing** — the row returns to #27 for P14 closure. LANE SPLIT creates to the stated clearable residual only, never to the full unit count. Creating into a closed lane spends against arithmetic that has already been run.

**3. Confirm gates.** G4 eligibility live on every advertised child, because an ineligible ad on terminal stock accrues the bracket rate while buying nothing. G12 clear on every keyword in the set. G9 fresh where the specification's ceiling is dated inside the staleness window.

**Read G6 carefully and do not act on it alone.** G6 measures stockout risk. On an overstocked variation it reads GREEN, and that reading is correct — the variation is genuinely not at risk of running out. **It is not an authorisation to scale.** The LTSF declaration is a separate input describing the opposite failure, and this step is where the two are held apart.

**4. Name the campaign.** Per the naming convention at Appendix A, **with the declared cliff date carried in the name**, so the expiry is readable from the campaign list without opening the row. The objective segment parses to the liquidation objective set at #27 P2; a campaign reaching this step without that objective is UNMANAGED under rule O1 and does not deploy.

**5. Stage the campaign settings as bulk rows per #38.** Portfolio = the product's portfolio. Daily budget = the figure the specification carries, which is derived at #27 from required clicks per day times market CPC at that volume, sized by the charge band. The budget is never chosen here.

**Bidding strategy must not be able to raise a bid above the ceiling.** A strategy that adjusts bids upward can exceed the set bid at auction time, which breaches the R2 ceiling without any staged row showing it and closes the lane's economics silently. Stage a fixed or downward-only strategy. This is the one setting where a platform default defeats the rule, and it is checked at staging rather than discovered in the T+1 diff.

**6. Ad groups and advertised SKUs.** The advertised SKU set is the one the specification names, read from the D2 variation map — **the aged children, never the parent by default, and never a healthy child**. On Archetype B this is a hard rule from the LTSF system: the healthy children subsidise the fix and their economics and price anchors are not spent on it. A parent or healthy child appearing in the SKU list is failure mode F8 and the row is returned rather than corrected in place.

Where the specification names a wide build class, one ad group holds the charged SKU set. Where it names an attribute or band grouping, one ad group per group.

**7. Add the targets at the match types the specification names.** Automatic targeting or the broader match types for the reach classes; exact and automatic close match for the proven-converter class. **The match type is not substituted.** Exact match on a high-volume head term clears above the R2 ceiling, so bidding the ceiling there buys no impressions, and substituting it into a reach build produces a campaign that spends nothing and reads as a failed test.

**8. Set the starting bid to the value the specification carries, at or under the R2 maximum liquidation CPC.** The bid is never invented at creation time, and never stepped up from the ceiling to win volume. A creation carrying no specification bid returns as incomplete. Where the arriving ceiling is dated earlier than any of its five inputs, the row returns to #27 for recompute rather than deploying against a stale ceiling.

**9. Placement modifiers at zero on all three groups at creation.** Modifiers are earned from placement evidence at #28, and R4 removes the evidence base on tagged entities. There is no ladder here and no step to size.

**10. Build the negation walls in the same working session per #29.** Two jobs:

- Negative-exact every term in this campaign out of the standing campaigns that could serve it, so the tagged units stop serving in standing structure. This is what makes the R5 quarantine structural rather than nominal.
- Negative-exact every proven converter out of the reach campaigns, so one keyword has one home across the lane.

Record the wall list in the T3 row as the #29 wall-audit baseline. **A quarantine staged without its wall list is a status change wearing a structure's name**, and it fails staging.

**11. Add the campaign to the #37 automation exclusion list, and record the addition.** An automation rule tuned for efficiency bands will ladder a liquidation bid downward toward a standing ceiling that does not apply to it, and close the lane with nothing alarming, because the rule is doing what it was written to do. While the automation rules export reads OPEN on the Ledger, the exclusion is confirmed by manual read and the read is logged.

**12. Update the registry.** New T3 row carrying the liquidation objective tag, the cliff date, the owner, the wall list, and the #27 specification reference. T1 family spend formulas pick the campaign up through its syntax tag. The campaign is registered as a dated structure, so it appears in the expiry sweep at #27 P12 rather than in the standing review.

**13. Log the creation in T6 with the prediction the specification carries:** units expected cleared by the cliff date, the basis tag, and the dated read. A creation without a logged prediction is incomplete and does not deploy.

**14. Deployment routes through #38, same week as the tag per R5, without exception.** Same-day where the tier is RED or CRITICAL. Same-day deployments still receive the full T+1 verification pass, and the pass is read against the ceiling as well as against the staged values.

---

## A. Where P13 differs from P1, and why

An operator who reaches for P1 on a tagged variation imports assumptions that the terminal lane forbids. Stated so the difference is visible rather than remembered:

| | P1 — single-keyword exact | P13 — dated liquidation |
|---|---|---|
| Objective | Ranking, defence or conversions | Liquidation only |
| Bid source | The driving verdict's ladder start, floor or push sizing | The R2 ceiling from the specification, never stepped above it |
| Bidding strategy | Per objective | Fixed or downward-only, so the ceiling cannot be breached at auction |
| Match type | Exact | As specified; the exact head is avoided on reach builds |
| Advertised SKU | The D2-**preferred** variation | The D2-**aged** children |
| Expiry | Standing review date | The declared cliff date, in the campaign name |
| Gate G6 | GREEN authorises creation | GREEN is not an authorisation; the LTSF declaration governs |
| Registry | Standing review | Dated structure, swept at #27 P12 |

---

## B. Interface contract to add to SOP-12 Element 12

| ID | Artifact | Sender → receiver | Timing | On non-arrival |
|---|---|---|---|---|
| *(new)* | The dated liquidation campaign specification: archetype, tier, cliff date, R2 ceiling with its date, advertised SKU set, build class, P4 lane result, budget, prediction | #27 operator → this SOP's operator | Same week as the tag, per SOP-27 R5 | P13 does not start. The tagged units keep serving inside standing campaigns, both reads are mixed, and neither the standing product's economics nor the recovery mathematics is usable until a fresh baseline is set. SOP-27 failure mode F3. The units continue accruing the bracket rate throughout. |

SOP-27's I-13 is the sending half of this contract. Adding this row makes the handover two-sided.

---

## C. Open items

| ID | Item |
|---|---|
| OPEN-1 | **Naming convention source.** Step 4 cites Appendix A, as P1 does. The corpus cites v4.0 Section 4.2 for the convention and that section is not present in the Criteria System as held; SOP-13 records the same gap as its own amendment item. The convention needs a live authority before the cliff-date segment can be specified precisely. |
| OPEN-2 | **Bidding-strategy authority.** Step 5 requires a strategy that cannot raise a bid above the ceiling. P1 step 5 cites v4.0 Section 4.4 for bidding strategy by objective, and that section is likewise not present. No document currently states which strategy the liquidation objective takes, so step 5 states the constraint and leaves the named setting to the threshold owner. |
| OPEN-3 | **The R2 subtrahend**, carried from #27 P15. P13 reads the ceiling rather than computing it, so it is unaffected structurally — but every bid it stages sits under whichever quantity is chosen. |
| OPEN-4 | **Consolidation interaction.** A tagged term live in both a standing campaign and a liquidation campaign is not a duplicate awaiting P7 consolidation; it is a quarantine failure. P7 needs a line saying so, or an operator running a routine duplicate sweep will consolidate the lane back into standing structure. |

---

*Inspiratek & Ecotero LLC · Confidential · DRAFT — not for deployment until Section C is closed*
