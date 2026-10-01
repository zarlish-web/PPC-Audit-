# SCS4 Exact campaigns: SKU, stock and top-of-search check against the Bids & Placements SOP (redline)

As of 2026-10-01.

Data:
- **Sellerboard:** September P&L per SKU, used for realised contribution; current stock and inbound per SKU.
- **Data Hub:** 30- and 90-day placement reports for all 142 Exact campaigns.
- **Audit run 20260929:** bids, modifiers, budgets, children and the engine's proposed values.

Workbook: `SCS4-exact-bids-placements-SOP-check.xlsx`. It holds the stock gate, plus the SOP's Table 1 (child economics), Table 2 (placement), Table 3 (bid re-solve, all 142 rows) and Table 4 (push candidates).

## Findings
- **Children.**
  - Queen campaigns advertise Queen Graphite. It is the best seller (389 units Apr–Sep) with 275 days of cover, so it passes the gate.
  - King campaigns advertise King Graphite, the best King seller, but it has 12 units, runs out around 6 Oct, and has nothing inbound. The backup is King White (769 units, ~640 days; no advertising history, priced on the King size's 13.9% top-of-search conversion).
  - Twin has no child that passes the gate. Hold at maintenance until the November inbound.
  - The Full exact campaigns advertise Full Midnight Black, which is at 0 stock. Swap them to Full Cool Grey.
- **Placement** (all Exact, last 30 days):
  - Top of search takes 60% of clicks and 76% of spend; product pages take 31% of clicks. The SOP target is 70–90% / ≤20%.
  - 7 of 27 readable campaigns meet the target; 6 are under 30% top of search.
  - Median top-of-search impression share is 9%.
  - Only one campaign is budget-capped ("cooling sheets king", 96% used).
- **Places where the run's pricing breaks the SOP:**
  1. **Contribution.** The run prices on ~$28–30 a unit; the realised September figure is $22.81 (29.4%). Every ceiling is ~25% high.
  2. **Market bound.** It is built from the campaign's own top-of-search CPC + 15%, which the redline forbids. The SOP stand-in is $3.22.
  3. **Climb cap.** Doses skip the 20–30% per-write cap (e.g. $4.43 → $7.75).
  4. **Requirement sum.** The 40 rank targets add up to 551 units a week against ~190 sold. The plan must be re-based (§7).
  5. **Ranking rules not applied:**
     - Rows under 30% top of search get price climbs; the distribution fix should come first.
     - A rank-collapse row ("cooling sheets queen", 32 → 46) gets a spend raise; the rule says never scale spend.
     - "king size cooling sheets" is at its #3 target and organic top 5, but gets no 15% step-down.

## Direction
1. **Swap children today:**
   - King terms → King White, including the six G-series campaigns still on Queen Graphite.
   - Full exact campaigns → Full Cool Grey.
   - Stop King Graphite ads.
2. **Distribution fix on every row with product pages over 20%.** Cut the base 25% (rows with sales) or 50% (rows without), floor $0.50. Re-solve the modifier so the top-of-search price holds.
3. **Top-of-search price ≤ $3.22** until a per-term clearing price exists. Move at most 30% per write. Deploy no doses. Name the gap on every row the bound stops.
4. **Push only Queen (Queen Graphite) and King (King White),** from a named envelope of about $1,600 a week for Exact.
5. **Twin, Cal King, Full and the colour terms stay at maintenance.** Raise the Twin Graphite quantity in the 1 Oct plan (it has only 30).
6. **Budget:** raise only "cooling sheets king" ($25 → $31).
7. **Checkpoint 15 Oct:** top-of-search click share ≥70%, product pages ≤20%, top-of-search clicks per week, and rank.

## Corrections to REVIEW.md and INVENTORY.md
- **Dose corrections (24/70/89/121):** use $3.22, not the engine's own-CPC bound.
- **Reshape pairs 146/149 and 266/269:** pass them; only fix their predictions.
- **"cooling sheets queen":** hold at $2.60, run a fixed-bidding suppression test, keep the $10 budget.
- **"cooling bed sheets":** revive at a top-of-search price of ~$2.16–2.31, not $3.30.
- **Break-even:** use the realised 29.4%, not 38.9%.
