# SCS4 Cooling Sheets: Final Consolidated PPC Plan

As of 2026-10-01. Live doc: https://claude.ai/code/artifact/b41afb27-a8a4-4ee2-833f-dae01c6f4fa3

## Bottom line

Run a moderate, stock-gated plan instead of the audit's 3× re-rank push: about $265–280 a day against the audit's $641. Keep the audit's structural fixes. Your agent's seven findings (1 Oct) are built in.

- **Exact keeps its current structure.**
  - Queen stays on Queen Graphite.
  - King moves to King White with no end date: King Graphite has no reorder in production and no arrival date.
  - Full moves to Full Cool Grey.
  - Twin stays at maintenance and pauses before it runs out (\~3 Nov).
  - No doses and no climbs. Top-of-search price ≤ $3.22.
  - 27 base cuts move clicks from product pages to top of search.
- **Audit reconciliation.** All 395 actions are checked:
  - 241 agree;
  - 80 modify;
  - 37 reject (doses, rank-gap climbs, budget raises);
  - 37 hold.
- **Kept from the audit:**
  - the King White swaps;
  - 6 revives of paused campaigns;
  - merging duplicate discovery campaigns;
  - negative-exact walls;
  - rest-of-search modifier to 0;
  - retags and renames.
- **Inbound is provisional.** The 1 Oct shipment is planned to reach Amazon on 19 Nov, and stock counts only once received. 9 SKUs that relied on it are re-tiered, and stock triggers are added.
- **King White's ceiling** comes from forward contribution, $18.15 a unit, which puts it at $2.52.
- **No colour-volume case** for grey or navy Exacts, and **no blanket purple negatives**.
- **Gaps:** 30 in total, 17 in the audit and 13 in my earlier plans. All are closed below.
- **Spend:** about $1,850–1,950 a week, TACoS ≤ 13% (September: 11.7%).

Workbook: `SCS4-FINAL-CONSOLIDATED-PLAN.xlsx` (28 sheets) on branch `claude/fervent-carson-x9x7vh`.

## Agent findings (1 Oct) and what they change

| # | Topic | Finding | Plan change |
| --- | --- | --- | --- |
| 1 | 1 Oct shipment | Plan shows 2,334 units (Sellerboard: 2,382, so 48 are unresolved). Departs 10 Oct; Amazon arrival 19 Nov, provisional. Pickup not recorded; forwarder unassigned. | Inbound counts toward a tier only if current stock lasts to \~26 Nov (19 Nov + check-in). 9 SKUs re-tiered or flagged. Phase 3 is gated on receipt, not on the date. |
| 2 | King Graphite | 12 units, ≈ 5–8 days. No open production, no confirmed arrival. A 300-unit order needs MOQ, production and freight confirmation. The older 270-unit shipment is already received. | King White carries King Exact with no end date. Phase 4 is undated. Raise the PO now. |
| 3 | Cool Grey 4PCS | Parent B0H8PNVWP1. King B0HKNJ736G $74.99, Queen B0HKN34G76 $69.99. Both listings inactive and not buyable. Reviews on these children and landed cost unverified. Amazon SKUs carry ‘4PCS’; the PO and shipment SKUs don't. | Support only, and only once the listing is active, stock is received, reviews show and cost is confirmed. No ceilings priced. 216 / 390 inbound treated as provisional. |
| 4 | ‘AGED’ Sponsored Brands label | Origin unverified. Hold an ad for the unavailable child; check other products before pausing a shared campaign. | Hold the King 4PCS ad only. Pause the whole campaign only after checking its other products. |
| 5 | King White $539 fee | Not confirmed as one-off. Bid on expected contribution per order × paid CVR. Keep the charge in September's P&L. | It is the FBA inbound convenience fee. Spread per unit received (\~$0.70), forward contribution is $18.15 → top-of-search ceiling $2.52 (was $2.62). King revives and creates repriced. |
| 6 | Colour volume | DataRova tracks no colour terms (a coverage gap). SQP, March 2026: ‘cooling sheets full size grey’ 29/mo, ‘cal king sheet slate blue’ 25/mo, a navy fitted-sheet query 7/mo. | Grey Exact dropped; no navy Exact. Add colour terms to DataRova. |
| 7 | Purple negatives | No blanket approval. Brand-explicit terms only, as campaign-specific negative exact. Never phrase-negative ‘purple’. | No brand-explicit purple term has paid spend, so no purple negatives now. ‘purple sheets’ (22 clicks, 0 orders) is only 2.1 expected orders → watch; negative exact only at ≥ 31 clicks with 0 orders. |

## Audit run vs final plan

The audit's diagnosis is mostly right. Its pricing and spend are not. All of its structural actions are kept; most of its price and budget actions are changed.

| Kind | Audit actions | Agree | Modify | Reject | Hold | Final position |
| --- | --- | --- | --- | --- | --- | --- |
| Child swaps | 38 | 38 | 0 | 0 | 0 | 31 King Graphite → King White; 6 King-term campaigns on Queen Graphite → King White; 1 PAT from Full White → Full Navy. |
| Top-of-search modifier | 37 | 5 | 9 | 23 | 0 | 15 doses and 8 rank-gap / thin-push climbs rejected. Re-solves kept, at the plan's lower price (King rows at King White's $18.15 contribution). |
| Base bids | 28 | 7 | 21 | 0 | 0 | All cuts kept. 21 go deeper (SOP: 25% with sales / 50% without, floor $0.50); 7 audit cuts adopted where my plan had none. |
| Budgets | 13 | 0 | 0 | 13 | 0 | 12 fund rejected doses or uncapped campaigns. The one capped row steps its price down instead. |
| Rest-of-search | 1 | 1 | 0 | 0 | 0 | ‘cooling bed sheets king’ 25% → 0. |
| Structure | 46 | 17 | 27 | 1 | 1 | Revives, freezes, folds, pauses and the eligibility check kept. 26 ‘not in the auction’ re-prices held, because they use the forbidden bound. Full pivot goes to Full Cool Grey, not Full Navy. |
| New builds | 43 | 1 | 6 | 0 | 36 | Pink Exact kept. 2 Queen tail terms with ≥ 2 orders go on Queen Graphite; 3 King tails on King White at ≤ $2.52; own-ASIN defence on tier-A children. Sponsored Brands, Video and Display builds, Twin creates and low-evidence Queen creates held. |
| Negatives | 8 | 8 | 0 | 0 | 0 | Negative-exact walls kept. No purple negatives added. |
| Retags | 13 | 13 | 0 | 0 | 0 | Objective labels only. |
| Renames | 168 | 151 | 17 | 0 | 0 | 17 names embed a stale child; renamed with the plan child after the swap. |
| **Total** | **395** | **241** | **80** | **37** | **37** |  |

| Strategy | Audit run 20260929 | Final plan |
| --- | --- | --- |
| Spend a day | $205.86 → $640.95 (3.1×) | ≈ $265–280 (+5–10%) |
| TACoS / ACoS | 21.6% / 44.2% | ≤ 13% / Exact ≤ 32% by 29 Oct |
| Break-even used | 39.0% (catalogue) | 29.4% realised ($22.81 a unit, Sept) |
| Market bound | Own TOS CPC + 15% ($4.21–4.94) | $3.22 SOP stand-in |
| Doses | 15, up to +331 pts | None |
| Rank targets | 40 targets = 551 units/wk vs \~190 sold | Hold top-10 ranks within ±3 |
| New campaigns | 43 builds, $309/day | 8 targeted, ≈ $45/day cap |
| Queen creates | Queen White (29 builds) | Queen Graphite, evidence-gated (2) |

The audit's own math says the push loses about $141 a day net until organic rank pays it back. That is priced on 39%. On the realised 29.4%, each paid order at 44% ACoS loses money, and the stock behind the push (King Graphite at 12 units) runs out in days.

Every row is in the sheet ‘Audit reconciliation (395)’, with the final value and the reason.

## End-to-end validation

The data ties out across Sellerboard, the Data Hub and the audit, with one exception: the 1 Oct shipment is 48 units short of what Sellerboard shows inbound. Four SOP rules fail in the audit and are fixed in the plan. Placement mix is still open.

| Check | Result | Status |
| --- | --- | --- |
| Sellerboard per-SKU units = family total, 1 Apr–30 Sep | 5,382 = 5,382 | Pass |
| Same, 15 Jul–30 Sep | 2,185 = 2,185 | Pass |
| September P&L | 816 units, $63,302 sales, $7,406 ads, $11,211 net (17.7%) | Pass |
| FBA stock = sum of sizes | 3,820 = 1,809 + 1,037 + 531 + 112 + 331 | Pass |
| Inbound | Sellerboard 2,382 (1,776 + 390 + 216 Cool Grey 4PCS) vs shipment plan 2,334: 48 units unresolved | Open |
| Inbound timing | Arrival 19 Nov is provisional; inbound counts only if stock lasts to \~26 Nov | Rule applied |
| PPC rows vs Sellerboard ads | $7,462 (2 Sep–1 Oct) vs $7,406 (1–30 Sep): 0.8% apart, from the shifted window | Pass |
| Exact spend = plan rows | $5,837 = 146 rows | Pass |
| Audit actions reconciled | 395 of 395 | Pass |
| Every live Exact row on a child with stock | King Graphite and Full Midnight Black removed; Twin Graphite and Queen Midnight Black carry stock triggers | Pass |
| No climbs on any child | 0 climbs | Pass |
| TOS price ≤ $3.22 | Exceptions: 2 staged descents ($4.15, $3.82), 2 rank-collapse holds ($3.26–3.27), 2 holds within 5% of the bound ($3.30, $3.35) | Pass (staged) |
| King White ceiling basis | Forward $18.15 a unit, not September's strict $3.87 or $18.86 | Pass |
| Requirement sum (SOP §7) | Audit: 551 units/wk vs \~190 sold | Fixed in plan |
| Contribution basis | Audit 39% vs realised 29.4% | Fixed in plan |
| Market bound | Audit uses own CPC + 15% | Fixed in plan |
| Engine stock read | Engine sell-through ≈ 2× Sellerboard (King White ‘179 days’ vs 641) | Fixed in plan |
| Placement mix (70/20) | Now 60% / 31%; 7 of 27 readable campaigns on target | Open — checks 15 and 29 Oct |

Stock tiers come from Sellerboard. Planning pace is the higher of September's rate and the Apr–Sep in-stock rate, so cover is never overstated. Price moves under 5% are not written.

## Gaps and missing logic

There are 30 gaps: 17 in the audit and 13 in my earlier plans, four of which surfaced from your agent's findings. Each is closed in the consolidated plan.

| # | Gap in | Gap found | Fix |
| --- | --- | --- | --- |
| A1 | Audit | 11 Full Exact campaigns advertise Full Midnight Black at 0 stock; none are swapped | Full Cool Grey (best Full seller, 83 units) |
| A2 | Audit | 6 campaigns with Full / Cal King / Twin keywords advertise Queen Graphite | Route to the keyword's size |
| A3 | Audit | Prices on 39% contribution; realised is 29.4% ($22.81 a unit), so every ceiling is \~25% high | Ceilings per child on realised contribution |
| A4 | Audit | Market bound is own TOS CPC + 15% ($4.21–4.94), which the SOP forbids | $3.22 stand-in |
| A5 | Audit | 15 doses skip the 20–30% climb cap ($4.43 → $7.75) | No doses, no climbs |
| A6 | Audit | 40 rank targets need 551 units/wk against \~190 sold | Hold the top-10 ranks within ±3 |
| A7 | Audit | Spend 3.1× to $641/day at 44% ACoS, above break-even | ≈ $265–280/day, TACoS ≤ 13% |
| A8 | Audit | 29 builds promote Queen White (82 units, tier B) and 7 promote Twin White (11 units) | Queen Graphite only where the term has ≥ 2 orders; Twin held |
| A9 | Audit | 17 renames embed a stale child | Rename with the plan child, after the swap |
| A10 | Audit | 12 of 13 budget raises are on uncapped campaigns | Rejected |
| A11 | Audit | 26 ‘not in the auction’ re-prices use the forbidden bound | Hold prices; delivery is limited by the ceiling |
| A12 | Audit | ‘king size cooling sheets’ is at target and organic top 5 with no 15% step-down | $4.50 → $3.82 |
| A13 | Audit | Engine sell-through ≈ 2× Sellerboard | Tiers from Sellerboard |
| A14 | Audit | No rule for ambiguous colour/brand terms (‘purple sheets’: 22 clicks, 0 orders) | Watch rule: negative exact only at ≥ 31 clicks with 0 orders, brand-explicit terms only; never phrase-negative ‘purple’ |
| A15 | Audit | Auto and Broad catch-all advertise Queen Regal Purple (59 days of cover) | Healthy slower colours instead |
| A16 | Audit | Cool Grey 4PCS has no price or cost in the engine; an ‘AGED’ Sponsored Brands campaign points at the inactive King 4PCS | Hold that ad; activate listings, confirm cost, fix the SKU mapping |
| A17 | Audit | No supply actions; King Graphite not in the 1 Oct plan | Raise the King Graphite PO; reconcile the shipment |
| P1 | My plan | Only ‘cooling bed sheets’ revived; the audit names 8 paused owners | 6 revived; Twin held for stock; ‘cool sheets’ stays paused (33 clicks, 0 orders) |
| P2 | My plan | Kept 7 discovery broads and 6 phrases; SOP-13/14 allow one per family | Fold 4 into Core Broad/Phrase; pause 6 duplicates |
| P3 | My plan | No negative-exact walls | Adopt audit 1409–1415 |
| P4 | My plan | Rest-of-search modifier missing | Adopt audit 41 |
| P5 | My plan | 7 rows kept a base the audit cuts while holding the TOS price | Adopt the cuts |
| P6 | My plan | One base bid per multi-target campaign | Per-target bids in the reconciliation sheet |
| P7 | My plan | 4 paused campaigns with no 30-day data were missing | Exact plan is now 146 rows |
| P8 | My plan | No PAT or own-page defence changes | Adopt 1280 (Full Navy); own-ASIN defence on tier-A children |
| P9 | My plan | 2 live campaigns with 0 impressions in 90 days not flagged | Check eligibility before any price move |
| P10 | My plan | Inbound counted as stock regardless of arrival | Counts only if stock lasts to \~26 Nov; 9 SKUs re-tiered or flagged |
| P11 | My plan | No action before an advertised child runs out ahead of inbound | Bids −50% at < 21 days of cover, pause at ≤ 5 units |
| P12 | My plan | King White priced at $18.86, treating the fee as one-off (unconfirmed) | Forward $18.15 → ceiling $2.52 |
| P13 | My plan | Blanket purple phrase negatives recommended | Removed: no brand-explicit purple spend |

## SKU priority ladder and stock gate

Each size stays on its best seller wherever that child's stock is healthy. Where it isn't, the next-highest seller with healthy stock takes over.

**Tiers** (planning pace = the higher of September's rate and the Apr–Sep in-stock rate):

- **A – healthy:** ≥ 90 days at 1.5× pace. Can carry Exact.
- **B – steady:** ≥ 60 days on hand, or ≥ 90 including inbound if current stock lasts to the provisional sellable date (\~26 Nov). Maintain; no push.
- **C – protect:** everything else with stock. Cut bids; no push.
- **OUT:** ≤ 5 units.

| Size | Preferred (best seller) | Exact child now | Next priority / backup | Later |
| --- | --- | --- | --- | --- |
| Queen | Queen Graphite: 476 units, 168 days, A | Queen Graphite | Queen Navy: 416 units, 347 days, A; 36 units Sep | Queen Cool Grey 4PCS: support once active |
| King | King Graphite: 12 units, ≈ 5–8 days, no arrival date, C | King White: 769 units, 641 days, A | King White | King Graphite once a reorder is confirmed and lands; Cool Grey 4PCS support only |
| Twin | Twin Graphite: 30 + 30, out \~3 Nov, C | Twin Graphite (maintenance, triggers) | Twin Cool Grey / Light Blue after receipt | Re-gate on receipt |
| Cal King | Cal King Graphite: 90 + 6, 138 days, A | Cal King Graphite | Cal King White: 69 + 30, A | — |
| Full | Full Cool Grey: 83 units, 88 days, B | Full Cool Grey | Full Midnight Black / Light Blue after receipt | Full Navy etc.: overstock layer |

- **King White beats King Cool Grey on the data:**
  - \#2 in-stock King seller in September (36 units).
  - Best King conversion: 12.6% unit session.
  - The only King stock that can absorb Exact traffic.
  - Cool Grey 4PCS is an inactive listing ($74.99), with 216 units due 19 Nov (provisional) and its cost unverified.
- **King White's caveat is margin.** Forward contribution is $18.15 a unit: September's $18.86 less the $539 inbound fee spread per unit received (\~$0.70). King Graphite earns $28.54. So King Exact prices step down rather than climb.
- **Queen Graphite is the landing child.** It took 2,796 Queen sessions in September (no other Queen colour took more than 745).

**Stock that runs out before the 1 Oct shipment can be sold** (sellable \~26 Nov):

| SKU | Units Sep | Stock + inbound | Runs out | Days short | Action |
| --- | --- | --- | --- | --- | --- |
| King Graphite | 78 | 12 + 0 | \~6 Oct | 52 | Ads off now; King → King White |
| King Light Blue | 37 | 68 + 0 | \~25 Nov | 1 | Support only; add to next PO |
| King Cream | 28 | 51 + 126 | \~24 Nov | 2 | Re-tiered B → C |
| Queen Midnight Black | 22 | 31 + 90 | \~10 Nov | 16 | Black Exact: bids −50% \~20 Oct, pause at ≤ 5 units (\~4 Nov) |
| Twin Graphite | 22 | 30 + 30 | \~3 Nov | 23 | Twin Exact: bids −50% \~12 Oct, pause at ≤ 5 units (\~29 Oct) |
| King Regal Purple | 19 | 32 + 60 | \~12 Nov | 14 | Re-tiered B → C |
| Twin Navy | 19 | 16 + 0 | \~24 Oct | 33 | Not advertised |
| Twin Cool Grey | 15 | 8 + 48 | \~17 Oct | 40 | Re-tiered B → C |
| Full Light Blue | 12 | 17 + 54 | \~30 Oct | 27 | Re-tiered B → C; out of Full backup |

All 61 SKUs — with stock, inbound, velocity, cover, stock-out date, triggers, sessions, conversion and contribution — are in ‘SKU master’ and ‘Inbound timing risk’.

## Exact campaigns

The 146 Exact campaigns keep their structure. Exact spend moves to top of search through base cuts, not price climbs.

- **Now (last 30 days):** top of search takes 60% of clicks and 76% of spend; product pages take 31% of clicks. Median top-of-search impression share is 9%. Target: 70–90% top of search, ≤ 20% product pages.
- **Child changes (54):**
  - 39 King campaigns → King White.
  - 11 Full campaigns → Full Cool Grey.
  - 3 off-size terms on Queen Graphite → Full Cool Grey; 2 → Twin Graphite; 1 → Cal King Graphite.
  - ‘green cooling sheets’ stays on Queen Sage Green.
- **Base bids (27 cuts):**
  - 25% on rows with sales, 50% without, floor $0.50. Seven of the cuts are the audit's, adopted.
  - Multi-target campaigns cut every target by the same %.
  - The modifier is re-solved so the top-of-search price holds.
- **Top-of-search price (128 live rows):**
  - 112 hold.
  - 16 step down: at most 30% per write above $3.22, at most 20% above ceiling + 25%. Moves under 5% are not written.
  - 0 climb.
  - ‘cooling sheets’ holds at $2.60 (defend only).
  - 4 rank-collapse rows freeze.
  - ‘king size cooling sheets’ steps down 15% (at target, organic top 5).
- **King rows** are priced on King White's forward contribution of $18.15, with a top-of-search ceiling of about $2.52.
- **Revives (6), as the audit proposed, at plan prices:**
  - ‘cooling bed sheets’ at $2.31 (196 clicks, 14 orders in 90 days).
  - ‘king sheets cooling’ and ‘cooling king sheets’ on King White at $2.52.
  - ‘queen size cooling sheets’, ‘cooling bed set’ and ‘cold sheets’ at $2.00, read at 15 clicks.
  - Twin owner held until receipt. ‘cool sheets’ stays paused.
- **Stock triggers:**
  - Twin Exact on Twin Graphite: bids −50% from \~12 Oct, pause at ≤ 5 units (\~29 Oct).
  - Black Exact on Queen Midnight Black: bids −50% from \~20 Oct, pause at ≤ 5 units (\~4 Nov).
  - Restart each once the inbound is received.
- **Budgets:** no raises. ‘cooling sheets king’ was the only capped campaign; its price steps down 20% instead.
- **Rest of search:** ‘cooling bed sheets king’ modifier 25% → 0.
- **G32 (‘cool king sheets’, now King White):** pause its ‘cold bed sheets queen’ target, or Queen shoppers see a King set.

| Keyword | Child now → plan | Spend 30d | Orders | TOS / PP clicks | TOS price now → plan | Base now → plan | TOS ceiling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cooling sheets king | King Graphite → King White | $723 | 18 | 83% / 16% | $5.19 → $4.15 | $1.72 → $1.72 | $2.43 |
| king size cooling sheets | King Graphite → King White | $677 | 23 | 54% / 44% | $4.50 → $3.82 | $1.80 → $1.35 | $2.40 |
| cooling sheets king size | King Graphite → King White | $596 | 19 | 47% / 47% | $4.59 → $3.22 | $1.70 → $1.27 | $2.86 |
| cooling sheets | Queen Graphite | $398 | 17 | 64% / 32% | $2.60 → $2.60 | $1.00 → $0.75 | $2.05 |
| cooling queen sheets | Queen Graphite | $288 | 7 | 64% / 34% | $4.43 → $3.22 | $1.50 → $1.12 | $2.17 |
| cool sheets queen | Queen Graphite | $175 | 5 | 60% / 18% | $2.94 → $2.94 | $1.20 → $0.90 | $1.94 |
| cooling bed sheets king | King Graphite → King White | $172 | 8 | 45% / 15% | $3.84 → $3.22 | $1.60 → $1.20 | $3.25 |
| cooling sheets for hot sleepers | Queen Graphite | $152 | 5 | 78% / 22% | $3.08 → $3.08 | $1.23 → $0.92 | $2.54 |
| cold sheets for hot sleepers | Queen Graphite | $142 | 5 | 64% / 34% | $3.22 → $2.58 | $1.34 → $1.01 | $2.03 |
| cooling sheets full size | Full Midnight Black → Full Cool Grey | $133 | 3 | 35% / 59% | $3.00 → $2.40 | $0.75 → $0.56 | $1.79 |
| cool king sheets | Queen Graphite → King White | $131 | 2 | 84% / 5% | $4.16 → $3.22 | $1.81 → $1.60 | $1.91 |

The King rows still sit above their ceilings after this write. They step down at most 30% per write and are re-read on 15 Oct. ‘cooling sheets twin’ ($155, 9 orders) stays at maintenance; its bid isn't in the export, so set it by hand. All 146 rows are in ‘Exact plan (146)’.

## Support layer and new campaigns

Broad, Phrase and Auto carry the slower colours. In 30 days they spent $1,625 for 170 orders (ACoS \~13%), against Exact's $5,837 for 204 orders (36%).

- **Fold (audit 1890–1893).**
  - Queen-Broad and the Feature broads fold into Core Broad; Queen-Phrase folds into Core Phrase.
  - Pause 6 inactive duplicates (audit 2072).
  - Core Broad and Core Phrase keep Queen Graphite and add Queen Navy, Beige and Light Grey.
- **Negatives.**
  - Negative-exact walls on 7 discovery campaigns (audit 1409–1415), so discovery stops buying terms Exact already owns.
  - **No purple negatives.** No brand-explicit purple term (‘purple mattress’, ‘purple brand’) has paid spend in 90 days. ‘purple sheets’ has 22 clicks and 0 orders, but that is only 2.1 expected orders, so the zero is not yet evidence. Add a campaign-specific negative exact only at ≥ 31 clicks with 0 orders, after checking that no conquest campaign targets Purple on purpose. Never phrase-negative ‘purple’.
  - Campaign-specific negative-exact candidates: ‘blue’ (Not Relevant, 12 clicks, 0 orders) and ‘silver infused bed sheets’.
- **Auto (8.9% ACoS):**
  - Swap out Queen Regal Purple (59 days of cover).
  - Advertise Queen Navy, Sage, Beige and Light Grey; King White; Cal King White; Cal King Regal Purple.
  - Budget $10 → $15.
- **Broad catch-all:** Queen Sage, Navy and Beige; Full Navy and Beige; Twin Cream. Retag as Discovery.
- **King Broad / Phrase:**
  - King White now; re-enable King Broad.
  - Add King Light Grey and Cream after their inbound is received.
  - Add Cool Grey 4PCS only once its listing is active and buyable.
- **Cal King Broad / Phrase:** add Cal King White and Regal Purple.
- **PAT:** the B0C14BKYXL conquest moves to Full Navy (audit 1280).
- **Sponsored Brands ‘…AGED…COOLGREY-KING-4PCS’:**
  - The label's origin is unverified, and a name doesn't prove inventory age.
  - Hold the King 4PCS ad only.
  - If it is a shared collection or store campaign, check its other products before pausing the whole campaign.

| New / changed campaign | Advertised SKU | Bid | Budget | Evidence |
| --- | --- | --- | --- | --- |
| Overstock Auto | Full Navy, Beige, Sage, Cream; Twin Cream; Cal King Regal Purple | $0.70 | $10/day | 190–300 days of cover; aged-inventory risk from January |
| Purple Exact | Queen Regal Purple | Base $0.60, TOS ≈ $1.50 | $5/day | 32 clicks, 2 orders, 15% ACoS |
| Pink Exact (audit 1610) | Queen Light Pink | Base $0.60, TOS ≈ $1.50 (not $2.90) | $5/day | Search volume 641; organic #63 |
| White-King Exact | King White | Base $0.60, TOS ≈ $1.50 | $5/day | ‘white cooling sheets’ search volume 644 |
| ‘queen sheets cooling’ (audit 1442) | Queen Graphite (not Queen White) | Base $1.00, TOS ≤ $2.45 | $6.41/day | 25 clicks, 2 orders; search volume 4,964 |
| ‘cooling sheets hot sleepers’ (audit 1574) | Queen Graphite | Base $1.00, TOS ≤ $2.45 | $6.21/day | 8 clicks, 2 orders |
| 3 King tail Exacts (audit 1502, 1514, 1778) | King White | TOS ≤ $2.52 (not $3.36) | $7.20/day each | Fits the King White ladder |
| Own-ASIN defence PAT (audit 1826) | Queen Graphite, Queen Navy, King White | $0.86 | $10/day | Cheapest page defence |

- **Black:** the existing Exact on Queen Midnight Black follows its stock trigger. Add ‘cooling black sheets’ and ‘black cooling sheets queen’ to it.
- **Not built:**
  - **Grey Exact.** DataRova tracks no colour terms; SQP showed one grey query at 29 a month (March); the listings are inactive. Grey shoppers are reached through Broad and Auto once 4PCS is live.
  - **Navy Exact.** SQP shows 7–25 a month.
  - Add colour terms to DataRova so the next cycle has volumes.
- **Held for now:**
  - Sponsored Brands, Video and Display shelf builds (9).
  - The new conquest PAT: the 10 existing ones had no delivery.
  - Twin creates (5).
  - 21 Queen tail creates without order evidence. Re-check 29 Oct; build on Queen Graphite once a term has ≥ 2 orders.

## Budget, phases, checkpoints and supply

Spend rises 5–10%, not 3×. The structural fixes go first and the child swaps happen today. Re-gating waits for the shipment to be received, and the main ranking push waits for spring stock.

| Bucket | Now $/wk | Plan $/wk |
| --- | --- | --- |
| Exact (146 campaigns) | 1,362 | 1,200–1,350 |
| Revives, evidence-gated creates, own-ASIN defence | 0 | ≤ 150 |
| Branded defence | 154 | \~155 |
| Broad / Phrase / Auto discovery | 225 | \~260 |
| Overstock Auto | 0 | ≤ 70 |
| Colour Exacts (purple, pink, white-king) | 0 | ≤ 105 |
| **Total** | **1,741** | **\~1,850–1,950 (≈ $265–280/day)** |

1. **Phase 0, 1–3 Oct: structure and children.**
   - Retags; fold 4 discovery campaigns and pause 6; negative-exact walls; rest-of-search to 0.
   - King Exact → King White; ads off King Graphite. Full Exact → Full Cool Grey.
   - Revive 6 owners.
   - Hold the King 4PCS ad in the AGED Sponsored Brands campaign.
   - Renames last, with the plan child.
2. **Phase 1, 3–15 Oct: placement and support.**
   - 27 base cuts, 16 price step-downs, no climbs.
   - Non-exact SKU swaps.
   - Launch the overstock Auto, the three colour Exacts and the 5 evidence-gated creates.
   - Twin trigger: bids −50% \~12 Oct.
3. **Phase 2, 15 Oct – receipt of the 1 Oct shipment: steady state.**
   - Queen Graphite at 2.0–2.6 units a day.
   - Re-tier every SKU weekly from Sellerboard.
   - Black trigger \~20 Oct. Twin pause \~29 Oct; black pause \~4 Nov.
4. **Phase 3, once the shipment is received in Sellerboard** (plan: departs 10 Oct, arrives 19 Nov — provisional): re-gate.
   - Twin, Full, King Light Grey / Cream, Queen Regal Purple / Midnight Black.
   - Revive the Twin owner; restart the Twin and black triggers.
   - Cool Grey 4PCS goes to support only if its listing is active, reviews show and cost is confirmed.
5. **Phase 4, King Graphite reorder lands** (no PO or date yet). King head terms go back to King Graphite once it has ≥ 90 days at 1.5× pace.
6. **Phase 5, Feb–Apr 2027.** The main ranking push, with stock in place.

| Checkpoint | Date | Pass if |
| --- | --- | --- |
| Mix and swaps | 15 Oct | Exact TOS click share ≥ 65% (heading to 70%), product pages ≤ 25%; King White TOS CVR ≥ 9% |
| Rank and cost | 29 Oct | Top-10 Queen / King ranks within ±3 of 1 Oct; Exact ACoS ≤ 32%; TACoS ≤ 13% |
| Shipment departs | 10 Oct | Pickup recorded, forwarder assigned, 48-unit gap reconciled |
| Inbound | on receipt (plan 19 Nov) | Units received match the plan; 4PCS listings active, with price and cost set |
| Spring order | 1 Dec | Order placed, sized to March 2026's pace (\~1,900 units a month) |

**Supply.**

- **King Graphite:** raise a PO now for about 300 units, subject to MOQ. Confirm supplier availability, production time and freight. The earlier 270-unit shipment is already received, so it isn't new stock.
- **1 Oct shipment:** reconcile 2,334 against 2,382; record the pickup; assign a forwarder.
- **Cool Grey 4PCS:**
  - Activate both listings.
  - Check that reviews show on these children.
  - Confirm landed cost.
  - Fix the SKU mapping (4PCS vs the PO SKUs). Don't copy the old SKUs' costs or quantities.
- **Queen Graphite:** include in the December order.
- **Twin Graphite:** about 120 units.
- **King Light Blue:** about 100 units; it runs out \~25 Nov.
- **Reorder rule:** trigger at 90 days of cover for the top-10 colours.

## Open items

The agent answered the seven questions. Nine follow-ups remain, and none of them blocks Phase 0 or Phase 1.

| Item | Owner | By |
| --- | --- | --- |
| 48-unit gap: shipment plan 2,334 vs Sellerboard 2,382 | Ops / forwarder | Before 10 Oct departure |
| Pickup record and forwarder for the 1 Oct plan | Ops | Before 10 Oct |
| King Graphite PO: MOQ, production lead time, freight, earliest arrival | Supplier / ops | Now |
| Cool Grey 4PCS: activate listings, reviews on the children, landed cost, SKU mapping | Catalog / finance | Before receipt |
| King White $539 fee: shipment and allocated units; is inbound placement already in the $30.62 landed cost? | Finance | 15 Oct |
| AGED Sponsored Brands campaign: list its advertised products | PPC | 3 Oct |
| Add colour terms to DataRova and pull current volumes | PPC / research | 15 Oct |
| Does any conquest campaign target Purple on purpose? | PPC | 15 Oct |
| Name the cause of the four rank collapses before any lever moves on them | PPC | 15 Oct |
