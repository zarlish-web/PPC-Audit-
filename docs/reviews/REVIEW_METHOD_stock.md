# Stock rules every audit review applies

Stock verdicts come from the **Sellerboard inventory planner**, never from the engine's hero read. The engine only sees SKUs the catalogue has sized. On DSS4 that is 19 of 124, so its stock gate can miss most of a product.

The planner pull for the 24 September satin runs (SSS4, DSFS, DSS4) is dated 25 Sep 2026. For every child it gives:

- FBA stock
- Reserved units
- Inbound (SentToFBA)
- Sales velocity (units a day)
- Days of stock left
- The running-out flag (YES / SOON / NO)
- Days to reorder

Command Center's last-14-day campaign report gives the ad orders each campaign carries.

## 1. Classify every child the product sells

| State | Test |
|---|---|
| **Out or under 14 days** | FBA = 0, or flag = YES, or days left < 14 |
| **At risk** | Not out, but flag = SOON, days left < 30, or FBA ÷ velocity < 14; **and** inbound does not cover another 30 days (inbound ÷ velocity < 30) |
| **In stock** | Everything else |

Where the run itself dates a hero's next arrival (its inventory context), that date wins: the hero is **at risk** when its planner days left end before the arrival. This first applied on DBS4, where Queen White has 22 days and its next 678 units land in 33.

Size is read from the SKU name (KING / QUEEN / FULL / TWIN). Pack is read the same way: 3PC is a different pack from 4PC. Colour comes from the catalogue's colour field. GRAY is read as GREY, and STRIPE is kept as its own pattern.

## 2. A swap (child re-point) passes only when all of these hold

1. **The source has to move.** It is out, under 14 days, or at risk. A swap off an in-stock child "by rule" is held, however much room the target has.
2. **Same size and same pack.** A cross-size or cross-pack swap is always held.
3. **The target carries the keyword's colour.** The colour is read from the campaign's plan keyword and the lower-case keyword part of its name. Upper-case SKUs stamped in the name are ignored, because they can name the wrong child.
4. **The target can carry the traffic.** Compute cover after the move = target FBA ÷ (target's own velocity + ad orders a day of every live campaign moving onto it). That counts this row's group and every other swap onto the same target from a child that has to move. It must stay at **30 days or more**.
   - Ad orders a day = the moving campaigns' 14-day orders ÷ 14. This replaces the stock addendum's worst case, which assumed the source's whole sales velocity would follow the ads.
5. **A much stronger target does not exist.** If another same-size child sells 3× the target's velocity and holds 3× its stock, the swap still passes, but the review names that child as the preferred target.

One exception to rule 1: a move off an in-stock child passes when the target is plainly the stronger seller. It must sell at least 2 a day and at least 1.5× the source, and keep 30 days once the moved traffic lands, counting its reserved units. It is still a manual task. On the satin runs no swap met this test; on DBS4 it passes King Creme → King White (9.8 a day against 5.0).

A swap that passes is a **manual task**, because the loader skips every swap today. A rename that stamps a passing swap's target ships **after the swap**. Any other rename that stamps a child the ad does not serve is held.

## 3. When the source must move and the engine's target fails

Pick an alternative in this order:

- same size and pack;
- the keyword's colour, if it names one;
- FBA above 0 and flag not YES or SOON;
- at least **45 days** of cover after the move: (FBA + inbound) ÷ (its own velocity + load already moving onto it + this campaign's ad orders);
- the highest velocity among those that qualify.

If none qualifies:

| Case | What to do |
|---|---|
| The keyword names a colour and the source is only at risk | Keep the ads on the source at floor bids while it lasts |
| The keyword names a colour and the source is out | Hold at floor bids, or pause, until the inbound lands. If nothing is inbound, pause: it is a reorder question, not a PPC one |
| The keyword names no colour | Pause until stock lands |

Never move a colour-named term onto another colour.

## 4. Colour pauses

The engine pauses a target when the child it resolves for a colour and size is out. Check every SKU of that colour and size, because some products carry two SKU families for the same variant.

| Case | Verdict |
|---|---|
| Another SKU of that colour and size has stock | **Hold.** Re-point the target to it, at floor bids if it is at risk |
| The named child still has units but is at risk | **Flag.** The pause is early, not wrong |
| No SKU of that colour and size has stock | **Pass.** Re-enable when the inbound lands |

## 5. Campaigns the run does not touch

List every enabled campaign whose advertised child is out or under 14 days and has no swap row and no campaign pause row. Add each one as a manual task:

- **A liquidation (LTSF) campaign** pauses with its closure record (SOP-27 P14). If it took 5 or more orders in 14 days, it evidently advertises other children, so check its ad roster first.
- **Any other campaign** is re-pointed to the alternative from §3, or paused.

## 6. Builds

Every build states its featured child's planner state. A build that features a child that is out or at risk needs a re-point before launch, even when the build is otherwise allowed.

## Where it shows in each review

- **A. Stock (inventory planner):** per-size totals, and every advertised child with its planner state, campaigns and 14-day spend.
- **C5:** every staged swap with the source and target planner stock, cover after the move, and the verdict.
- **C5b:** the campaigns on sold-out children that the run does not touch.
- **C13:** colour pauses.
- **Workbook:**
  - The *Rows* sheet carries planner columns for source and target.
  - *Stock by child* lists every SKU of the product.
  - *Swaps* and *Re-points not in run* carry the detail.
