# SCS4 Cooling Sheets: Final Consolidated PPC Plan

As of 2026-10-01. Live doc: https://claude.ai/code/artifact/b41afb27-a8a4-4ee2-833f-dae01c6f4fa3

## Bottom line

Run a moderate, stock-gated plan instead of the audit's 3× re-rank push: about $265–280 a day against the audit's $641. Keep the audit's structural fixes.

- **Exact keeps its current structure.**
  - Queen stays on Queen Graphite.
  - King moves to King White, as the audit also proposed.
  - Full moves to Full Cool Grey.
  - Twin stays at maintenance until its inbound lands.
  - No doses and no climbs this write. Top-of-search price ≤ $3.22.
  - 27 base cuts move clicks from product pages to top of search.
- **Audit reconciliation.** All 395 actions are checked:
  - 242 agree;
  - 79 modify (mostly deeper base cuts, lower top-of-search prices and the right child);
  - 37 reject (doses, rank-gap climbs, budget raises);
  - 37 hold (Sponsored Brands, Video and Display builds, Twin creates and low-evidence Queen creates).
- **Kept from the audit:**
  - 38 King swaps to King White;
  - 6 revives of paused owners;
  - folding 4 discovery campaigns into Core Broad/Phrase, and pausing 6 inactive duplicates;
  - negative-exact walls (stop discovery campaigns buying terms Exact already owns);
  - rest-of-search modifier to 0;
  - 13 objective retags and 168 renames, using the plan child.
- **Gaps found:** 26 in total, 17 in the audit and 9 in my earlier plan. All are closed below.
- **Support layer.** Slower colours move through Broad, Phrase and Auto, one overstock Auto and three colour-matched Exacts (purple, pink, white-king).
- **Spend:** about $1,850–1,950 a week, TACoS ≤ 13% (September: 11.7%).

Workbook: `SCS4-FINAL-CONSOLIDATED-PLAN.xlsx` (26 sheets) on branch `claude/fervent-carson-x9x7vh`.

## Audit run vs final plan

The audit's diagnosis is mostly right. Its pricing and spend are not. All of its structural actions are kept; most of its price and budget actions are changed.

| Kind | Audit actions | Agree | Modify | Reject | Hold | Final position |
| --- | --- | --- | --- | --- | --- | --- |
| Child swaps | 38 | 38 | 0 | 0 | 0 | 31 King Graphite → King White; 6 King-term campaigns on Queen Graphite → King White; 1 PAT from Full White → Full Navy. |
| Top-of-search modifier | 37 | 6 | 8 | 23 | 0 | 15 doses and 8 rank-gap / thin-push climbs rejected. Re-solves kept, at the plan's lower price. |
| Base bids | 28 | 7 | 21 | 0 | 0 | All cuts kept. 21 go deeper (SOP: 25% with sales / 50% without, floor $0.50); 7 audit cuts adopted where my plan had none. |
| Budgets | 13 | 0 | 0 | 13 | 0 | 12 fund rejected doses or uncapped campaigns. The one capped row steps its price down instead. |
| Rest-of-search | 1 | 1 | 0 | 0 | 0 | ‘cooling bed sheets king’ 25% → 0. |
| Structure | 46 | 17 | 27 | 1 | 1 | Revives, freezes, folds, pauses and the eligibility check kept. 26 ‘not in the auction’ re-prices held, because they use the forbidden bound. Full pivot goes to Full Cool Grey, not Full Navy. |
| New builds | 43 | 1 | 6 | 0 | 36 | Pink Exact kept. 2 Queen tail terms with ≥ 2 orders go on Queen Graphite; 3 King tails on King White at ≤ $2.62; own-ASIN defence on tier-A children. Sponsored Brands, Video and Display builds, Twin creates and low-evidence Queen creates held. |
| Negatives | 8 | 8 | 0 | 0 | 0 | Negative-exact walls kept; purple-brand negatives added. |
| Retags | 13 | 13 | 0 | 0 | 0 | Objective labels only. |
| Renames | 168 | 151 | 17 | 0 | 0 | 17 names embed a stale child; renamed with the plan child after the swap. |
| **Total** | **395** | **242** | **79** | **37** | **37** |  |

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

The data ties out across Sellerboard, the Data Hub and the audit. Four SOP rules fail in the audit and are fixed in the plan; one target (placement mix) is still open.

| Check | Result | Status |
| --- | --- | --- |
| Sellerboard per-SKU units = family total, 1 Apr–30 Sep | 5,382 = 5,382 | Pass |
| Same, 15 Jul–30 Sep | 2,185 = 2,185 | Pass |
| September P&L | 816 units, $63,302 sales, $7,406 ads, $11,211 net (17.7%) | Pass |
| FBA stock = sum of sizes | 3,820 = 1,809 + 1,037 + 531 + 112 + 331 | Pass |
| Inbound (ready to ship) | 2,382 = 1,776 across 59 SKUs + 390 Queen and 216 King Cool Grey 4PCS | Pass |
| PPC rows vs Sellerboard ads | $7,462 (2 Sep–1 Oct) vs $7,406 (1–30 Sep): 0.8% apart, from the shifted window | Pass |
| Exact spend = plan rows | $5,837 = 146 rows | Pass |
| Audit actions reconciled | 395 of 395 | Pass |
| Every live Exact row on a child with stock | King Graphite (12) and Full Midnight Black (0) removed; Twin Graphite kept at maintenance | Pass |
| No climbs on tier B/C children | 0 climbs in the plan | Pass |
| TOS price ≤ $3.22 | Exceptions: 2 staged descents (‘cooling sheets king’ $4.15, ‘king size cooling sheets’ $3.82) and 2 rank-collapse holds at $3.27 | Pass (staged) |
| Requirement sum (SOP §7) | Audit: 551 units/wk vs \~190 sold | Fixed in plan |
| Contribution basis | Audit 39% vs realised 29.4% | Fixed in plan |
| Market bound | Audit uses own CPC + 15% | Fixed in plan |
| Engine stock read | Engine sell-through ≈ 2× Sellerboard (King White ‘179 days’ vs 641) | Fixed in plan |
| Placement mix (70/20) | Now 60% / 31%; 7 of 27 readable campaigns on target | Open — checks 15 and 29 Oct |

The stock tiers come from Sellerboard. Planning pace is the higher of September's rate and the Apr–Sep in-stock rate, so cover is never overstated.

## Gaps and missing logic

There are 26 gaps: 17 in the audit and 9 in my earlier plan. Each is closed in the consolidated plan.

| # | Gap in | Gap found | Fix |
| --- | --- | --- | --- |
| A1 | Audit | 11 Full Exact campaigns advertise Full Midnight Black at 0 stock; none are swapped | Full Cool Grey (best Full seller, 83 units) |
| A2 | Audit | 6 campaigns with Full / Cal King / Twin keywords advertise Queen Graphite | Route to the keyword's size |
| A3 | Audit | Prices on 39% contribution; realised is 29.4% ($22.81 a unit), so every ceiling is \~25% high | Ceilings per child on realised contribution |
| A4 | Audit | Market bound is own TOS CPC + 15% ($4.21–4.94), which the SOP forbids | $3.22 stand-in |
| A5 | Audit | 15 doses skip the 20–30% climb cap ($4.43 → $7.75) | No doses, no climbs this write |
| A6 | Audit | 40 rank targets need 551 units/wk against \~190 sold | Hold the top-10 ranks within ±3 |
| A7 | Audit | Spend 3.1× to $641/day at 44% ACoS, above break-even | ≈ $265–280/day, TACoS ≤ 13% |
| A8 | Audit | 29 builds promote Queen White (82 units, tier B) and 7 promote Twin White (11 units) | Queen Graphite only where the term has ≥ 2 orders; Twin held |
| A9 | Audit | 17 renames embed a stale child | Rename with the plan child, after the swap |
| A10 | Audit | 12 of 13 budget raises are on uncapped campaigns | Rejected |
| A11 | Audit | 26 ‘not in the auction’ re-prices use the forbidden bound | Hold prices; delivery is limited by the ceiling |
| A12 | Audit | ‘king size cooling sheets’ is at target and organic top 5 with no 15% step-down | $4.50 → $3.82 |
| A13 | Audit | Engine sell-through ≈ 2× Sellerboard | Tiers from Sellerboard |
| A14 | Audit | No purple-brand negatives (‘purple sheets’: 22 clicks, 0 orders) | Purple sheets / mattress / brand / pillow; silver infused; blue |
| A15 | Audit | Auto and Broad catch-all advertise Queen Regal Purple (59 days of cover) | Healthy slower colours instead |
| A16 | Audit | Cool Grey 4PCS has no price or cost in the engine; an ‘AGED / clearance’ Sponsored Brands campaign points at the 0-stock King 4PCS | Pause it; add price and cost |
| A17 | Audit | No supply actions; King Graphite is not in the 1 Oct plan | Reorder plan below |
| P1 | My plan | Only ‘cooling bed sheets’ revived; the audit names 8 paused owners | 6 revived; Twin held for stock; ‘cool sheets’ stays paused (33 clicks, 0 orders) |
| P2 | My plan | Kept 7 discovery broads and 6 phrases; SOP-13/14 allow one per family | Fold 4 into Core Broad/Phrase; pause 6 duplicates |
| P3 | My plan | No negative-exact walls | Adopt audit 1409–1415 |
| P4 | My plan | Rest-of-search modifier missing | Adopt audit 41 |
| P5 | My plan | 7 rows kept a base the audit cuts while holding the TOS price | Adopt the cuts |
| P6 | My plan | One base bid per multi-target campaign | Per-target bids in the reconciliation sheet |
| P7 | My plan | 4 paused campaigns with no 30-day data were missing | Exact plan is now 146 rows |
| P8 | My plan | No PAT or own-page defence changes | Adopt 1280 (Full Navy); own-ASIN defence on tier-A children |
| P9 | My plan | 2 live campaigns with 0 impressions in 90 days not flagged | Check eligibility before any price move |

## SKU priority ladder and stock gate

Each size stays on its best seller wherever that child's stock is healthy. Where it isn't, the next-highest seller with healthy stock takes over.

**Tiers** (planning pace = the higher of September's rate and the Apr–Sep in-stock rate):

- **A – healthy:** ≥ 90 days at 1.5× pace. Can carry Exact.
- **B – steady:** ≥ 60 days on hand, or ≥ 90 including inbound. Maintain; no push.
- **C – protect:** below both. Cut bids; no push.
- **OUT:** ≤ 5 units.

| Size | Preferred (best seller) | Exact child now | Next priority / backup | Later |
| --- | --- | --- | --- | --- |
| Queen | Queen Graphite: 476 units, 168 days, A | Queen Graphite | Queen Navy: 416 units, 347 days, A; 36 units Sep | Queen Cool Grey 4PCS (390 inbound): support |
| King | King Graphite: 12 units, out \~6 Oct, C | King White: 769 units, 641 days, A | King White | King Graphite once reordered; Cool Grey 4PCS support only |
| Twin | Twin Graphite: 30 + 30, 34 days, C | Twin Graphite (maintenance) | Twin Cool Grey / Light Blue after inbound | Re-gate mid-Nov |
| Cal King | Cal King Graphite: 90 + 6, 138 days, A | Cal King Graphite | Cal King White: 69 + 30, A | — |
| Full | Full Cool Grey: 83 units, 88 days, B | Full Cool Grey | Full Midnight Black / Light Blue after inbound | Full Navy etc.: overstock layer |

- **King White beats King Cool Grey on the data:**
  - \#2 in-stock King seller in September (36 units).
  - Best King conversion: 12.6% unit session.
  - The only King stock that can absorb Exact traffic.
  - Cool Grey 4PCS lands around mid-Nov with 216 units, about 99 days at its own pace. It is support until it beats King White after 4 weeks live.
- **King White's caveat is margin.** It earns $18.86 a unit (excluding a one-off $539 inbound fee), against King Graphite's $28.54. So King Exact prices step down rather than climb.
- **Queen Graphite is the landing child.** It took 2,796 Queen sessions in September (no other Queen colour took more than 745), so Exact traffic on it sells the whole Queen family.

All 61 SKUs, with stock, inbound, velocity, cover, sessions, conversion and contribution, are in ‘SKU master’.

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
  - 108 hold.
  - 20 step down: at most 30% per write above $3.22, at most 20% above ceiling + 25%.
  - 0 climb.
  - ‘cooling sheets’ holds at $2.60 (defend only).
  - 4 rank-collapse rows freeze.
  - ‘king size cooling sheets’ steps down 15% (at target, organic top 5).
- **Revives (6), as the audit proposed, at plan prices:**
  - ‘cooling bed sheets’ at $2.31 (196 clicks, 14 orders in 90 days).
  - ‘king sheets cooling’ and ‘cooling king sheets’ on King White at $2.62.
  - ‘queen size cooling sheets’, ‘cooling bed set’ and ‘cold sheets’ at $2.00, read at 15 clicks.
  - Twin owner held for stock. ‘cool sheets’ stays paused.
- **Budgets:** no raises. ‘cooling sheets king’ was the only capped campaign; its price steps down 20% instead.
- **Rest of search:** ‘cooling bed sheets king’ modifier 25% → 0.
- **G32 (‘cool king sheets’, now King White):** pause its ‘cold bed sheets queen’ target, or Queen shoppers see a King set.

| Keyword | Child now → plan | Spend 30d | Orders | TOS / PP clicks | TOS price now → plan | Base now → plan | TOS ceiling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cooling sheets king | King Graphite → King White | $723 | 18 | 83% / 16% | $5.19 → $4.15 | $1.72 → $1.72 | $2.52 |
| king size cooling sheets | King Graphite → King White | $677 | 23 | 54% / 44% | $4.50 → $3.82 | $1.80 → $1.35 | $2.49 |
| cooling sheets king size | King Graphite → King White | $596 | 19 | 47% / 47% | $4.59 → $3.22 | $1.70 → $1.27 | $2.97 |
| cooling sheets | Queen Graphite | $398 | 17 | 64% / 32% | $2.60 → $2.60 | $1.00 → $0.75 | $2.05 |
| cooling queen sheets | Queen Graphite | $288 | 7 | 64% / 34% | $4.43 → $3.22 | $1.50 → $1.12 | $2.17 |
| cool sheets queen | Queen Graphite | $175 | 5 | 60% / 18% | $2.94 → $2.94 | $1.20 → $0.90 | $1.94 |
| cooling bed sheets king | King Graphite → King White | $172 | 8 | 45% / 15% | $3.84 → $3.22 | $1.60 → $1.20 | $3.38 |
| cooling sheets for hot sleepers | Queen Graphite | $152 | 5 | 78% / 22% | $3.08 → $3.08 | $1.23 → $0.92 | $2.54 |
| cold sheets for hot sleepers | Queen Graphite | $142 | 5 | 64% / 34% | $3.22 → $2.58 | $1.34 → $1.01 | $2.03 |
| cooling sheets full size | Full Midnight Black → Full Cool Grey | $133 | 3 | 35% / 59% | $3.00 → $2.40 | $0.75 → $0.56 | $1.79 |
| cool king sheets | Queen Graphite → King White | $131 | 2 | 84% / 5% | $4.16 → $3.22 | $1.81 → $1.60 | $1.98 |

‘cooling sheets twin’ ($155, 9 orders) stays at maintenance; its bid isn't in the export, so set it by hand. All 146 rows are in ‘Exact plan (146)’.

## Support layer and new campaigns

Broad, Phrase and Auto carry the slower colours. In 30 days they spent $1,625 for 170 orders (ACoS \~13%), against Exact's $5,837 for 204 orders (36%).

- **Fold (audit 1890–1893).**
  - Queen-Broad and the Feature broads fold into Core Broad; Queen-Phrase folds into Core Phrase.
  - Pause 6 inactive duplicates (audit 2072).
  - Core Broad and Core Phrase keep Queen Graphite and add Queen Navy, Beige and Light Grey.
- **Negatives.**
  - Negative-exact walls on 7 discovery campaigns (audit 1409–1415), so discovery stops buying terms Exact already owns.
  - Purple-brand negatives: ‘purple sheets’, ‘purple mattress’, ‘purple brand’, ‘purple pillow’.
  - Also ‘silver infused’ and ‘blue’ (exact).
- **Auto (8.9% ACoS):**
  - Swap out Queen Regal Purple (59 days of cover).
  - Advertise Queen Navy, Sage, Beige and Light Grey; King White; Cal King White; Cal King Regal Purple.
  - Budget $10 → $15.
- **Broad catch-all:** Queen Sage, Navy and Beige; Full Navy and Beige; Twin Cream. Retag as Discovery.
- **King Broad / Phrase:**
  - King White now; re-enable King Broad.
  - Add King Light Grey and Cream after their inbound, and Cool Grey 4PCS when it is live.
- **Cal King Broad / Phrase:** add Cal King White and Regal Purple.
- **PAT:** the B0C14BKYXL conquest moves to Full Navy (audit 1280).
- **Sponsored Brands:** pause the ‘AGED’ Cool Grey 4PCS campaign until stock is live.

| New / changed campaign | Advertised SKU | Bid | Budget | Evidence |
| --- | --- | --- | --- | --- |
| Overstock Auto | Full Navy, Beige, Sage, Cream; Twin Cream; Cal King Regal Purple | $0.70 | $10/day | 190–300 days of cover; aged-inventory risk from January |
| Purple Exact | Queen Regal Purple | Base $0.60, TOS ≈ $1.50 | $5/day | 32 clicks, 2 orders, 15% ACoS |
| Pink Exact (audit 1610) | Queen Light Pink | Base $0.60, TOS ≈ $1.50 (not $2.90) | $5/day | Search volume 641; organic #63 |
| White-King Exact | King White | Base $0.60, TOS ≈ $1.50 | $5/day | ‘white cooling sheets’ search volume 644 |
| ‘queen sheets cooling’ (audit 1442) | Queen Graphite (not Queen White) | Base $1.00, TOS ≤ $2.45 | $6.41/day | 25 clicks, 2 orders; search volume 4,964 |
| ‘cooling sheets hot sleepers’ (audit 1574) | Queen Graphite | Base $1.00, TOS ≤ $2.45 | $6.21/day | 8 clicks, 2 orders |
| 3 King tail Exacts (audit 1502, 1514, 1778) | King White | TOS ≤ $2.62 (not $3.36) | $7.20/day each | Fits the King White ladder |
| Own-ASIN defence PAT (audit 1826) | Queen Graphite, Queen Navy, King White | $0.86 | $10/day | Cheapest page defence |
| Grey Exact (mid-Nov) | Cool Grey 4PCS, Queen and King | Base $0.60, TOS +150% | $5/day | Test once stock is live |

- **Black:** the existing Exact on Queen Midnight Black holds its price until the 90 inbound land. Add ‘cooling black sheets’ and ‘black cooling sheets queen’ to it.
- **Held for now:**
  - Sponsored Brands, Video and Display shelf builds (9).
  - The new conquest PAT: the 10 existing ones had no delivery.
  - Twin creates (5).
  - 21 Queen tail creates without order evidence. Re-check 29 Oct; build on Queen Graphite once a term has ≥ 2 orders.

## Budget, phases, checkpoints and supply

Spend rises 5–10%, not 3×. The structural fixes go first, child swaps today, and the main ranking push waits for spring stock.

| Bucket | Now $/wk | Plan $/wk |
| --- | --- | --- |
| Exact (146 campaigns) | 1,362 | 1,200–1,350 |
| Revives, evidence-gated creates, own-ASIN defence | 0 | ≤ 150 |
| Branded defence | 154 | \~155 |
| Broad / Phrase / Auto discovery | 225 | \~260 |
| Overstock Auto | 0 | ≤ 70 |
| Colour Exacts (purple, pink, white-king; grey from mid-Nov) | 0 | ≤ 105 |
| **Total** | **1,741** | **\~1,850–1,950 (≈ $265–280/day)** |

1. **Phase 0, 1–3 Oct: structure and children.**
   - Retags; fold 4 discovery campaigns and pause 6; negative-exact walls; rest-of-search to 0.
   - King Exact → King White; pause King Graphite ads. Full Exact → Full Cool Grey.
   - Revive 6 owners. Pause the AGED Sponsored Brands campaign.
   - Renames last, with the plan child.
2. **Phase 1, 3–15 Oct: placement and support.**
   - 27 base cuts, 20 price step-downs, no climbs.
   - Non-exact SKU swaps and negatives.
   - Launch the overstock Auto, the colour Exacts and the 5 evidence-gated creates.
3. **Phase 2, 15 Oct – mid-Nov: steady state.**
   - Queen Graphite at 2.0–2.6 units a day.
   - Re-tier every SKU weekly from Sellerboard.
4. **Phase 3, \~mid-Nov (2,382 units land): re-gate.**
   - Twin, Full, King Light Grey / Cream, Queen Regal Purple / Midnight Black.
   - Cool Grey 4PCS goes to support, plus the grey test. Revive the Twin owner.
5. **Phase 4, King Graphite reorder lands.** King head terms go back to King Graphite once it has ≥ 90 days at 1.5× pace.
6. **Phase 5, Feb–Apr 2027.** The main ranking push, with stock in place.

| Checkpoint | Date | Pass if |
| --- | --- | --- |
| Mix and swaps | 15 Oct | Exact TOS click share ≥ 65% (heading to 70%), product pages ≤ 25%; King White TOS CVR ≥ 9% |
| Rank and cost | 29 Oct | Top-10 Queen / King ranks within ±3 of 1 Oct; Exact ACoS ≤ 32%; TACoS ≤ 13% |
| Inbound | mid-Nov | 2,382 received; 4PCS listings in the parent, with price and cost set |
| Spring order | 1 Dec | Order placed, sized to March 2026's pace (\~1,900 units a month) |

**Supply.**

- King Graphite: reorder about 300 units now; there are none in the 1 Oct plan.
- Queen Graphite: include in the December order.
- Twin Graphite: about 120 units.
- King Light Blue: about 100 units.
- Reorder rule: trigger at 90 days of cover for the top-10 colours.

## Open questions

Seven facts would firm up the plan. Each one has a place to look it up.

| Question | Why it matters | Where to check |
| --- | --- | --- |
| ETA of the 1 Oct shipment plan (2,382 units) | Phase 3 timing; assumed \~mid-Nov | Sellerboard FBA shipments / forwarder |
| Can King Graphite be reordered (\~300), and the earliest arrival? | How long King White carries King Exact | Supplier / ops |
| Are the Cool Grey 4PCS ASINs (B0HKNJ736G King, B0HKN34G76 Queen) in the parent, with reviews? Price and landed cost? | The engine can't price them without these | Seller Central / Sellerboard product settings |
| Why is the Sponsored Brands campaign for King Cool Grey 4PCS labelled AGED / clearance? | It points at a 0-stock SKU we treat as support | Campaign owner |
| Is King White's $539 September inbound fee a one-off? | Sets King White's ceiling ($18.86 vs $3.87 a unit) | Sellerboard fee detail |
| Search volume for grey/gray and navy/blue colour terms | Decides the grey and navy colour Exacts | Helium10 / DataDive |
| Approve the purple-brand negatives? | Blocks brand-intent waste; may block a few colour shoppers | Account owner |

The audit's own open item stands as well: name the cause of the four rank collapses before any lever moves on those rows.
