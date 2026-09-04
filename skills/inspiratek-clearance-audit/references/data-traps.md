# Data traps

Every one of these cost real time on a live product. Check for them before trusting any figure.

## FBA `units-shipped` columns are unreliable

The FBA inventory report's `units-shipped-t7/t30/t60/t90` fields overstated volume by 65% on one product — 686 against Sellerboard's 416 for the same window. Two rounds of analysis were built on the wrong number before it was caught.

**Check:** reconcile against Sellerboard *and* against physical inventory drawdown. On the product where this was caught, the aged pool fell from 3,220 to 2,776 — a drop of 444 — which resolved cleanly into ~296 Sellerboard sales plus ~148 completed removals. That triangulation is what settled it.

**Use FBA for stock, age bands and fees only.** Sellerboard governs velocity and economics.

## A margin-only ad ceiling is far too tight

A CM2 calculation gave $13.26 per unit where the storage-adjusted figure was $28.47. Working from the margin-only number nearly produced a recommendation to cut spend when the correct move was to increase it.

**Check:** always add storage per unit per month × months of acceleration. On aged stock, COGS is sunk.

## COGS may be unit-only, not landed

Sellerboard held $12.64 for a King size; the LTSF file held $17.74. The gap was freight and duty — `DomesticShippingCost` was null on all 21 SKUs.

**Check:** compare the Sellerboard product cost export against the LTSF SKU detail. A consistent 40%+ uplift means freight is held elsewhere. A single blended figure that matches no actual SKU is a warning sign on its own.

## Data Dive's advertised-keyword field under-reports badly

It reported 0 for eight of ten competitors that AdInsight showed running 42 to 675 keywords each. The field is a single point-in-time scrape of one fixed 500-keyword list, so a competitor running 655 keywords that day reads as zero if none fall inside that list.

This produced a flatly wrong conclusion in a delivered document — "twenty of twenty-one competitors do not advertise" — when the tracked set was actually running 4.7 million monthly ad impressions between them.

**Use AdInsight for all advertising activity. Use Data Dive for sales, rank, price, reviews and variation counts.**

## Third-party keyword tools show a truncated set

Data Dive's visible 500 keywords showed zero ivory and zero taupe terms. The 2,795-row MKL had 56 and 18, and one of them converted at 4.49% market CVR.

**Check:** always confirm against the full MKL before concluding a variant has no demand.

## Weekly reporting sheets can be defective

One history table listed "Week 1" twice, carried identical values for Weeks 7 and 8, and had no rows at all for two weeks that contained a Lightning Deal.

**Prefer Sellerboard's own weekly view over any hand-assembled tracker.**

## Plan-of-record figures may be conditional, not forecast

A velocity threshold of 128.46/day was being treated as a target. It was stated twice in the source model as "the pace at which the call changes, never a forecast that we reach it" — the pace at which keeping beat liquidating.

**Check:** read the Assumptions and Basis tabs of any what-if model, not just its outputs. Ask whether a number is a target or a condition, and what decision it was answering.

## Decisions may not have been executed

A placement inversion described as deployed was never in the account nine days later. A 233-unit removal leg — 39% of an approved order — was never filed and nobody noticed for two weeks.

**Check:** verify against the current bulk and the current inventory, not against the plan that describes them.

## The syntax classifier may discard your best traffic

An "Irrelevant" bucket indexed at 9.41× on purchases per impression — the best-performing traffic on the product. It was catching clearance, comforter and Spanish terms.

Separately, brand lists containing single common words (amazon, lux, rest, eden, bella, zen, cozy, bliss, kate) over-catch generic phrases that merely contain them.

**Check:** index every syntax bucket including the discard bucket before trusting the labels.

## Placement conclusions do not transfer between products

On one product Top of Search cost 65% more per order than Rest of Search and the premium was pure waste. On its sibling, Top of Search was the *cheapest* placement.

**Never carry a placement conclusion across products.** Run the per-campaign test on each product's own data.

## Listing changes contaminate the window

A title, main image and secondary image change mid-window makes the placement and conversion data unreadable for that period.

**Check the Slack thread for listing changes before setting any modifier from a blended window.**

## Cost per ad-attributed order is not cost per unit

Two denominators produce very different numbers. On one product CPA per ad-attributed order was $36.61 while cost per unit shipped was $12.91, because advertising attributed only a quarter of units.

**Use cost per unit shipped for ceiling tests.** Use CPA per order only for keyword-level decisions.

## Campaign totals are not this product's spend

A campaign carrying this product's ad may carry hundreds of other SKUs. Filtering the bulk to "campaigns that contain this product" and summing their spend pulls in every one of those SKUs.

On one product this dragged in three catch-all and brand-defence campaigns carrying $1,501 of spend between them, advertising 19 to 589 SKUs each. The product's real share of that $1,501 was **$0.45**.

**Check:** attribute through Product ad rows filtered to this product's SKUs, then reconcile the total against an independent source. Where the two agree to within a percent or two, the attribution is settled. A campaign whose product ads include any foreign SKU is excluded from the decided bulk and named as excluded.

## Placement conclusions do not transfer, and neither does a blanket zero

Covered above for premiums. The same applies in reverse: finding every modifier already at 0% is not evidence that 0% is correct. It is evidence that nobody set them. Run the per-campaign test, or state that the placement report is missing and that no modifier may be set in either direction until it arrives.

## An acceleration window longer than the clearance window inflates the ceiling

The ceiling adds storage per unit per month multiplied by months of acceleration. Taking months-to-clear as that multiplier — 4.4 months on a slow variant — nearly doubles the ceiling against the two-month default, and it does so on precisely the stock with the weakest case for spending.

**Check:** the multiplier is `min(2, months to clear)`. If a ceiling in a draft looks generous, this is the first line to re-read.

## A verdict computed on one denominator and tested against another

Judging campaigns on cost per ad-attributed order and comparing that against a ceiling expressed per unit shipped mixes two denominators. Where advertising attributes three quarters of units the two differ by a third; where it attributes a quarter they differ by four times.

**Check:** ceiling tests use cost per unit shipped, converted to per unit cleared. CPA per order is for keyword-level decisions only.
