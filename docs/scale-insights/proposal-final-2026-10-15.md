# Scale Insights: final proposal (Oct 15, 2026)

For: Erik Fisher, posted in #ppc-team-private as a reply to Erik's Oct 5 thread ("can we cancel it? Or at least downgrading to the minimum").
Sources:
- Scale Insights owner account screenshots, Oct 15: Manage subscriptions, Transactions, Automated ASINs, Connect to Amazon, and the Inspiratek login.
- Scale Insights Bulk Automate ASINs export, Oct 14.
- SellerBoard ad spend per ASIN and Command Center SP spend, both Sep 15 – Oct 14.
- Slack history about Scale Insights, Apr 2024 – Oct 2026.

---

## Slack message (paste as a reply in the thread)

<@Erik Fisher> sorry this is late. Here is the full Scale Insights analysis from the owner account (screenshots and files attached). **It corrects my Oct 13 post:** we are *not* on the 1% plan, and we do *not* need to remove ASINs.

**1. What we pay**
• **Ecotero: Scale 50 monthly, $388 list, charged $310.40/mo** with our 20% discount on every invoice since Jun 2025. Renews **Oct 17**. My ~$1,350/mo estimate was wrong.
• **Inspiratek: not active.** It's a separate login with no subscription, last charged **Mar 9, 2025**. There's nothing to cancel.
• History:
  - We've been customers since **Apr 2022**, and have paid **$24,359** in total ($18,645 Ecotero + $5,714 Inspiratek).
  - The expensive period was **Apr 2024 – Mar 2025**, when Ecotero was on Scale 500 at ~$600/mo and Inspiratek on Scale 50 at ~$200/mo. Both were cut in Mar 2025.
  - No keyword-tracking plan.

**2. What we get and use**
• Scale Insights counts an automated ASIN as **one child ASIN (the ad group's associated ASIN) per marketplace**; the same ASIN in the US and CA counts as 2 (Scale Insights docs, "How are automated ASINs calculated?"). So Scale 50 normally allows 50 child ASINs. Our Automated ASINs page shows **2,001 allowed, with 222 child ASINs in use** (123 US, 98 CA, 1 MX). That's a non-standard allowance, most likely carried over from our Scale 500 period (Apr 2024 – Mar 2025). **We get more than we pay for, so there's no overpayment and no refund case.**
• If Scale Insights ever enforces the 50 limit, the best 50 ASINs by spend cover **75%** of ad spend, which is more than the current 222 (60%). So we'd still be fine.
• We use **dayparting only** (the overnight pause, confirmed live in Marketing Stream Oct 6–7). The bid and budget rules that were overriding our manual changes (Aug 25 review) are all removed.
• The 2022–2026 history is backed up to Drive (Shayan Rana, Oct 1): <https://drive.google.com/drive/folders/14jrmIifOSSjIWWuv2-dNAut6vaCywgZa|link>.

**3. Gap found**
• The 222 dayparted ASINs carry only **60% of our ad spend** ($78K of $130K, US+CA, last 30 days, SellerBoard).
• **135 of them spend under $25/mo.** Meanwhile big spenders aren't dayparted: Satin Full Black US ($2.8K), Bamboo King Taupe CA ($2.1K), SS Satin Grey King US ($2.0K), Sleephoria Cooling Fitted Queen White US ($1.8K) and 20 others.
• **Fix, at no extra cost:** turn automation on for the **24 high-spend ASINs** that are currently off. Coverage goes from 60% to **82%**, using 246 of our 2,001 slots. List attached.

**4. Recommendation**
1. **Don't downgrade now.**
   - Any plan change would very likely reset us to that tier's real limit: Scale 35 = 35 ASINs at $230.40, Scale 20 = 20 at $142.40, Scale 5 = 5 at $62.40.
   - It may also drop the 20%.
   - We'd save $80–$248/mo but lose dayparting on most ASINs.
2. **Enable the 24 high-spend ASINs.** Do it after the overnight pause ends, and check under Assigned rules that only the dayparting rule applies. Confirm the next morning.
3. **Move dayparting in-house, then cancel before the Nov 17 renewal.**
   - <@Joseph Fisher> builds the overnight pause and resume (SOP-45 and the dayparting runbook already exist; Joseph listed "Scale Insights daypart" as an open decision on Oct 12).
   - Run both side by side for 3 nights.
   - Download the archived data and cancel. **Saving: $310.40/mo ($3,725/yr).**
   - This also removes the clash where the nightly bid snapshot runs inside the Scale Insights pause window (Oct 7).
4. **Refund:** no basis, since we haven't overpaid. Asking would also draw attention to the 2,001 limit. Optional: ask for a loyalty discount for the last month (4.5 years, $24.4K paid).
5. **Before cancelling:** confirm the Drive backup is complete, as you asked on Jul 22. Download the Ecotero and Inspiratek archives from the "Download archived data" menu.

**5. Needed from you**
• Approve 2 (enable 24 ASINs) and 3 (keep Scale 50 until in-house dayparting is live, then cancel before Nov 17).
• <@Joseph Fisher> what date can the in-house overnight pause be ready? It needs to be live by **about Nov 12** to leave 3 nights of parallel running before the Nov 17 renewal.

_If there's no reply by Oct 16, 8 PM ET: Ecotero renews on Scale 50 at $310.40 and nothing else changes._

---

## What changed since the Oct 13 post (and why)

| Oct 13 post said | Owner account shows | Effect |
|---|---|---|
| Likely the 1% plan, ~$1,350/mo | Scale 50 monthly, $310.40/mo since Jun 2025 | No big monthly saving from a downgrade |
| 2,001 slots means we're overpaying | We pay for 50 and the account allows 2,001 | No overpayment, so no refund case |
| Downgrade to 100 ($550) or 50 ($310) | Already on 50 at $310.40 | Those options don't apply |
| Remove ~121–171 ASINs to downgrade | Not needed, 1,779 slots free | Keep all 222, add 24 |
| Cancel Inspiratek | No subscription since Mar 9, 2025 | Nothing to cancel |

## Options compared (Ecotero)

| Option | Price/mo | ASINs that can be dayparted | Saving/mo | Spend covered |
|---|---|---|---|---|
| **Keep Scale 50 + enable 24 (recommended)** | $310.40 | 2,001 (246 used) | — | **82%** |
| Keep Scale 50 as is | $310.40 | 2,001 (222 used) | — | 60% |
| Scale 35 (best 35 ASINs) | $230.40* | 35 | $80 | 69% |
| Scale 20 (best 20 ASINs) | $142.40* | 20 | $168 | 57% |
| Scale 5 (best 5 ASINs) | $62.40* | 5 | $248 | 33% |
| Cancel after in-house is live | $0 | handled by our own system | $310.40 | in-house |

*Only if the 20% carries over after a plan change. Without it: $288 / $178 / $78. Spend covered = share of US+CA ad spend, Sep 15 – Oct 14 (SellerBoard, all ad types).

## Payment history

**Ecotero** ($18,645.30 in total):

| Period | Plan | Price |
|---|---|---|
| Apr – Jul 2022 | Basic | $29/mo |
| Jul 2022 – Jan 2023 | Scale 20 | $178/mo |
| Feb – Jun 2023 | Scale 35 | $288/mo, then $777/quarter |
| Jun 2023 – Mar 2024 | Scale 50 | $1,047/quarter |
| Apr 2024 – Mar 2025 | Scale 500 ($2,788 list, $2,188 off) | ~$600/mo |
| Mar 2025 | Scale 75 | $548 |
| Apr 29, 2025 | Scale 50 with 20% off | $227.66 credit |
| Jun 2025 – Sep 2026 | Scale 50 | **$310.40/mo**, 16 payments |

**Inspiratek** ($5,713.69 in total):

| Period | Plan | Price |
|---|---|---|
| Apr 2022 | Basic | $29 |
| May – Dec 2022 | Essential | $99/mo |
| Dec 2022 – Mar 2023 | Scale 20 | $178/mo |
| Mar 2023 – Mar 2024 | Scale 20 | $480/quarter |
| Apr 2024 – Mar 2025 | Scale 50 | ~$200/mo |
| After Mar 9, 2025 | none | — |

## Slack context used

| Date | Who / where | What |
|---|---|---|
| 2024-05 | Erik, #amazon-ppc | Asked for a Scale Insights settings proposal and a meeting with their team |
| 2025-06-17 | Erik, #amazon-ppc | Asked whether the Scale Insights billing was accurate (receipt 2872-3038, Scale 50 at $310.40); Zaid confirmed it was |
| 2025-11-29 | Erik, #amazon-ppc | Asked for all Scale Insights data to be backed up, plus a monthly download |
| 2026-07-20/22 | Erik, #ppc-team-private | Asked for the full Scale Insights history in Command Center, "completely comprehensive". Shayan Rana pulled it week by week from 2022 |
| 2026-08-08 and 08-24 | Erik, #ppc-team-private | "We likely will not be needing Scale Insights in the long run"; phase it out once the app handles everything |
| 2026-08-25 | Zarlish, #ppc-team-private | Rule review: the override setting was blank on 83 bidding rules, budget rules had no maximum, dayparting paused 11 pm – 3 am |
| 2026-08-30 | Joseph and Erik | In-house dayparting tab offered; SOP-45 and the dayparting runbook shared |
| 2026-10-01 | Shayan Rana, #amazon-ppc | 2022–2026 PPC history backed up to Drive |
| 2026-10-05 | Erik | Cancel or downgrade? Joseph: "Yeah I think we could downgrade". Zarlish: "downgrade for now, we have to set up the dayparting system" |
| 2026-10-06/07 | Joseph | Live check: the Scale Insights overnight pause is visible in Marketing Stream; the nightly snapshot clashes with the pause window |
| 2026-10-12 | Erik | "please downgrade", report the lowest price, check Inspiratek, explain ASIN removal. Joseph listed "Scale Insights daypart" as an open decision |
| 2026-10-13 | Zarlish, then Erik | Zarlish posted an estimate-based answer; Erik shared owner access and asked about a refund for overpaying and a loyalty discount |
| Not found | — | No date for in-house dayparting. No confirmation that the Inspiratek archive was downloaded |

## Files
- `asins-to-enable-2026-10-14.csv`: the 24 high-spend ASINs to switch on (attach to the post).
- `automated-asins-vs-spend-2026-10-14.csv`: every ASIN with spend and its automation status.

## Steps once Erik approves
1. **Enable the 24 ASINs.**
   - Scale Insights → Assigned rules: check that only the dayparting rule applies.
   - The next morning, after the pause has ended: Automated ASINs → Automation disabled → search each ASIN → tick it → Enable.
   - The following morning, check those campaigns paused and resumed overnight.
2. **In-house dayparting.** Joseph sets the date. Run in parallel for 3 nights, comparing the pause and resume times in Marketing Stream.
3. **Cancel, before Nov 17.**
   - Download archived data (Ecotero, then the Inspiratek login).
   - Confirm the Drive backup is complete.
   - Account → Subscription → Cancel Subscription. Screenshot the confirmation.
   - The next morning, check that in-house dayparting ran.
