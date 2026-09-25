# Sleephoria Boho Blanket: Comprehensive PPC Launch Audit (Day 30)

**Product 41** · parent B0GGTMTB4Y · 16 SKUs (50x60 and 60x80 × 8 patterns) · US only · Launch stage · Portfolio *SLEEPHORIA - Boho Blanket*
**Audit window:** 2026-08-26 (campaigns live) → 2026-09-24 (last complete UTC day), 30 days · **Written:** 2026-09-25
**Section shape:** S0–S10, following the list in the brief. The Launch Audit Structure Template V4.1.1 and the Day 5 and Day 10 audits are **not in this repository**, and a Drive search on 2026-09-25 found none of them. I therefore could not check heading-level conformance or carry forward Day 5 and Day 10 figures; see §0.4.

---

## Headline finding: this product cannot be advertised profitably at its current price and cost base, at any conversion rate the category produces

- **Contribution per unit** (SellerBoard products grid, 2026-09-25):
  - 50x60: **$3.96**, break-even ACoS **14.7%**
  - 60x80: **$4.89**, break-even ACoS **14.0%**
  - The two advertised Butterfly SKUs are $4.05 and $5.11.
- **Market CVR.** SOP-23 O3 classes both sizes as **THIN**, meaning under $6/unit. The category's SQP market CVR on the Batch 1 terms is **1.71%** (Data Dive SQP: 288 purchases on 16,810 clicks, September).
- **Maximum profitable CPC** (SOP-41 F1: contribution × CVR):
  - At market CVR: **$0.07 / $0.08**.
  - At the framework target of 3.0 × market = 5.14%: **$0.20 / $0.25**.
- **What the product actually pays per click** (command-center, 30 days):
  - **$0.45** blended
  - **$0.89** for on-Amazon placements
  - **$1.42** at top of search, the placement a ranking push has to win
- **CVR needed to break even** at the blended CPC: **11.3% (50x60) / 9.2% (60x80)**. That is **5–7× the market rate**. At top of search it is **36% / 29%**, which is **17–21× market**.
- **Each order bought through PPC cost $40.86** (29 orders on $1,184.93). That is **8–10× the contribution it returns**.
- **Weekly loss at current spend ($276/week):**
  - at measured CVR: **−$250 / −$243**
  - at the framework's 5.14%: still **−$151 / −$122**
- **No bid fixes this.** SOP-23 WE-3 describes the same situation: "The failure is economic and routes to pricing and product, not to a bid." At the blended CPC and 3× market CVR, break-even needs **$8.74 contribution**, which means a price of **$32.61 (50x60)** and **$39.52 (60x80)**. That is **+$5.62 and +$4.53** on today's $26.99 / $34.99, with fees and COGS unchanged. At top-of-search CPC, the break-even prices are **$55.00 / $61.91**.
- **The whole-business P&L confirms it.** SellerBoard, 30 days: sales **$1,686.47**, ad spend **$1,181.70**, net **−$1,809.69**. That includes an **$829.86 storage charge** in the week of 1 Sep. Before ads and storage, realised contribution was **$201.87 on 54 units ($3.74/unit)**, which cross-checks the $3.96 and $4.89 list-price figures.

Five further findings sit on top of that:

1. **The launch model was never computed** (S3):
   - DSTR is empty on all 7,795 MKL rows.
   - Daily Target is 1 on all 49 Batch 1 rows.
   - The model's "Adjusted PPC CVR" (12.0–17.7%) is **SQP click share × 1.5**, not a conversion rate. It overstates the realised 1.10% by 11–16×.
2. **Rank went backwards, not forwards** (S2). "boho throw blanket" moved **#59 → #92** in Data Dive and **#68 → #104** in the command-center crawl. On 25 Sep, **0 of the 23 tracked Batch 1 terms were in the top 10**. The plan had assumed 52 of the tracked terms were already at rank 10 or better.
3. **The TOS modifier drifted** (S1). It went from the planned +100% to about +300% to +900% in live campaigns (spend-weighted 5.8× on 24 Sep). The top-of-search share bought stayed under 1% on the two largest terms.
4. **64% of all clicks (1,686 of 2,638) went Off-Amazon** at $0.20 each, between 4 and 18 Sep (S1). That traffic is what makes the blended CPC look cheap. It builds no search rank.
5. **Campaign and ad-group status fields in SellerBoard are unreliable** (S0). They show every campaign with either the campaign or its ad group Paused, but command-center delivery data shows **38 campaigns receiving impressions on 22–24 Sep** ($64.48 spend). Spend did fall to about $12/day on 23–24 Sep.

**Recommendation in one line:** keep paid rank-building stopped. Do not launch Batch 2. Send the price and COGS decision to the brand owner with the arithmetic in S9. Rebuild the MKL model with real inputs before any money is re-committed.

---

## Sources, dates and conventions

| Tag | Source | Scope / date |
|---|---|---|
| **SB-PPC** | SellerBoard `ppc_dashboard_period` then `ppc_dashboard_table` (same period and group_by), account Ecotero | search `B0GGT`; 2026-08-26 → 09-24; pulled 2026-09-25; campaign, ad_group, keyword and search_term levels all return identical period totals |
| **SB-BID** | SellerBoard `ppc_bidding_history`, `ppc_entry_settings` | daily points 08-26 → 09-25; bids and budgets only (no placement or status series) |
| **SB-P&L** | SellerBoard `dashboard_period` / `dashboard_table` | search `BOHO`, Amazon.com, same 30 days |
| **SB-PROD** | SellerBoard `products`, `product_cost_details` | read 2026-09-25 |
| **SB-INV** | SellerBoard `inventory`, `inventory_history` (Amazon.com entry, observed ≤ 09-24; the forecast tail is ignored) | read 2026-09-25 |
| **CC** | Ecotero command-center (`ppc_summary`, `ppc_performance_split`, `ppc_campaigns`, `ppc_campaign_targets`, `ppc_placements`, `ppc_daily`, `ppc_ranks`, `ppc_keywords`) | US, product 41, 08-26 → 09-24. Campaign-grain placement figures are **measured**; the daily placement split is an **estimated** redistribution (CC's own label) |
| **DD-RR** | Data Dive rank radar d22965b2 (ASIN **B0GGT3PZ8K**, Butterfly 60x80), 238 keywords | 2026-09-01 → 09-25 (no data before 1 Sep) |
| **DD-SQP** | SQP fields carried on that radar (5–19 days of data per term, all September) | child B0GGT3PZ8K's SQP view |
| **DD-N** | Data Dive niche nUARjsKofz "Boho Throw Blanket MKL" | researched 2026-09-21 |
| **WB** | *Sleephoria_Boho_Blanket_PPC_Launch.xlsx*: MKL, Campaign Structure (CS), Inventory, Sizing Analysis, PAT | as uploaded |
| **SOP-xx** | PPC SOPs in this repo (SOP-22, 23, 28, 41) | v1.0 / v2.0 |

- **[M]** = measured directly from a source.
- **[I]** = inferred by me; the reasoning is stated.
- **[S]** = stated in the brief and not independently verifiable in this session.
- AdSpend is reported as an absolute value throughout.
- "Amazon fees" = AmazonFees + AmazonFeesFBA + ReferralFee.

### Where sources disagree

| Metric | Source A | Source B | Trusted | Why |
|---|---|---|---|---|
| 30-day ad spend | CC $1,184.93 | SB-PPC $1,180.52 | CC for rates, both shown | CC attributes by ASIN, SB by campaign search filter; $4.41 (0.4%) gap |
| Impressions | CC 129,117 | SB-PPC 112,267 | CC | CC includes Off-Amazon and placement impressions; the SB search-term rows sum to 107,625 |
| Clicks / orders / ad sales | CC 2,638 / 29 / $905.70 | SB-PPC 2,631 / 29 / $905.70 | Agree | – |
| PPC-attributed sales | SB-PPC $905.70, 30 units | SB-P&L "SalesPPC" $320.89, 11 units | SB-PPC / CC for ACoS | The ad console attributes 7-day click-through sales, including other SKUs (SB `SameSKUSalesToAllSales` 0–70%). The P&L attributes to the advertised SKU only. The P&L is used for whole-business profit, the ad figures for ACoS |
| 60x80 COGS | SB-PROD $16.73–16.74 | CC landed cost $15.84 | **SB** | SB is the accounting cost used in every SB profit line since 2026-01-07. CC's value is a `cogs_defaults` placeholder. S9 shows the CC case as sensitivity, and the conclusion does not change |
| Organic rank | DD-RR (B0GGT3PZ8K) | CC crawl | Both | Same direction (e.g. boho throw blanket 59 → 92 in DD, 68 → 104 in CC). DD is used as primary because it has SQP |
| Search volume | MKL | DD-RR | DD for sizing | DD SV is a median **2.36×** MKL SV across 81 overlapping terms (e.g. boho throw blanket 9,420 vs 25,418) |

---

## S0: Execution audit (planned vs live)

### 0.1 Structure

| Item | Plan (WB) | Live (CC / SB-PPC, 25 Sep) | Verdict |
|---|---|---|---|
| Go-live | 2026-08-26 | First spend 2026-08-26 ($10.75, CC daily) [M] | ✅ |
| Batch 1 keywords | MKL: 49 rows; CS: 50 kw | 49 of 49 MKL keywords live as Exact targets [M]. 11 have zero spend, so SB omits them, but CC target lists confirm them. CS's 50th term **"white boho throw blanket" is not deployed** and is not in the MKL | ⚠️ CS and MKL disagree |
| Batch 1 campaigns | CS: 28 = 20 single-keyword + 7 Halo + 1 Branded | **30 keyword campaigns** = 20 single-keyword + **9** Halo + 1 Branded [M] | ⚠️ Halos regrouped. E.g. plan G7 (5 kw) became 4 + 1; plan G2/G3/G5 members were re-mixed into "scandinavian" and "throw blanket for couch" halos |
| PAT (conquest) | 10 ASINs → Bouquet 60x80, bid $0.45, budget $4.50 | 10 ASIN campaigns → Bouquet 60x80, budget $5, current bids **$0.59–$0.82** [M] | ⚠️ Bids +31% to +82% over plan |
| Batch 2 | Held (55 campaigns, 68–69 kw, $550/day) | Not launched [M] | ✅ (correct, and see S8/S9: keep it held) |
| SKU routing | Butterfly 50x60 (41 kw), Butterfly 60x80 (7), Bouquet 50x60 (2) | Matches, except **"boho blanket queen"**: MKL routes 50x60, CS routes 60x80, live follows MKL (50x60) [M] | ⚠️ A queen term routed to the smaller size |
| Match type | Exact only | Exact only, 45 keyword rows all EXACT [M] | ✅ |
| Bidding strategy | Fixed | Campaign names carry "Fixed". SB entry settings do not expose the Amazon bidding strategy [I] | Not verified |
| Base bids | ExpCPC × 0.5 ($0.50–$0.99) | First SB bid point on **28 Aug = plan value on all 45 rows** [M] | ✅ at launch, then changed (0.3) |
| TOS modifier | **+100%** on all 49 | **+300% to +900%** on all 49 keyword targets; +380% on 1 of 7 PAT (S1) [M] | ❌ Drift |
| Budgets | MKL Σ $407.90/day; CS subtotal $414/day | Deployed at plan values rounded (e.g. boho throw blanket $8.30 → $8). Two raises: boho blanket $6 → $25 (28 Aug) → $40 (4 Sep); boho throw blanket $8 → $30 (28 Aug) [M] | ⚠️ MKL and CS totals differ by $6.10 |
| Objective registry | CS: Ranking (27), Defensive (1); PAT: conquest | CC registry: 19 Ranking, 1 Conquesting, **20 not declared** [M] | ❌ Half the campaigns are invisible to objective-level reporting |
| Economics ceiling | – | CC economics block has **price, referral and fulfilment missing for all 16 SKUs**; break-even ACoS null [M]. No `product_targets` row [S]: I cannot query that table in this session, but the null ceiling is consistent with it | ❌ No ceiling exists in the system |
| Dated honeymoon exit (SOP-22 P2) | MKL "Reasoning" text says tightening is withheld "through the honeymoon window" | No date anywhere in WB [M] | ❌ Required field missing |
| Naming | `S-BB-SP-RAN-{tier}-FIX-{SKU}-[Segment]-{kw}` | `SL-BB-SP-{kw}-{syntax}-{tier}-Exact-Rank-Fixed-{SKU}` | ⚠️ Different convention; plan-to-live joins need keyword matching |

### 0.2 What is serving today (corrected 2026-09-25)

**SellerBoard status fields (read 25 Sep).** Every one of the 37 visible campaigns shows either the campaign or its ad group as Paused: 26 are campaign Active / ad group Paused, and 11 the reverse. Taken at face value, that means nothing can serve.

**Command-center delivery data contradicts this** (`ppc_campaigns`, 22–24 Sep; `ppc_daily`) [M]:
- **38 campaigns** received impressions in that window, and 23 of them spent ($64.48 in total). They include campaigns SellerBoard lists as paused at campaign level (boho blankets and throws $11.03, boho heated blanket $4.63, throw blanket for couch boho $3.69, throw blanket boho $2.50) and ones it lists as paused at ad-group level (bohemian throw blanket $15.11, boho throw blankets for couch $6.08).
- **Product-level delivery:**

| Date | Impressions | Clicks | Spend |
|---|---|---|---|
| 22 Sep | 4,309 | 41 | $40.08 |
| 23 Sep | 2,066 | 14 | $12.14 |
| 24 Sep | 1,721 | 17 | $12.26 |
| 25 Sep | 0 | 0 | $0 (the US day had only just begun when the data was pulled; not evidence of a pause) |

**Conclusion.** The SellerBoard status fields cannot be trusted for serving state. The exact campaign-vs-ad-group mismatch on all 37 campaigns looks like a mapping artifact [I]. Ads were serving through at least 24 Sep, at a lower level from 23 Sep. Neither tool provides status history, so the cause of that drop is not established.

### 0.3 Changes made during the window (SB-BID) [M]

| Date | Change | Rows |
|---|---|---|
| 27 Aug | Budgets first recorded (= plan, rounded) | 40 campaigns |
| 28 Aug | Keyword bids first recorded, all at plan value; budgets raised on boho blanket ($6 → $25) and boho throw blanket ($8 → $30) | 45 kw, 2 campaigns |
| 29 Aug | boho throw $0.50 → $0.60; boho throw blanket $0.50 → $0.65 | 2 |
| 2 Sep | Broad bid raise, typically +30% (e.g. $0.99 → $1.29, $0.52 → $0.75) | 44 |
| 4 Sep | boho blanket budget $25 → $40 | 1 |
| 6 Sep | Trim, typically −10% (e.g. $1.29 → $1.16) | 15 |
| 13 Sep | Cuts: boho throw $0.65 → $0.32; bohemian throw blanket $0.79 → $0.52; throw blanket boho $0.75 → $0.38 | 3 |
| 18 Sep | boho blanket throw $0.68 → $0.50 | 1 |
| 31 Aug → 17 Sep | **TOS modifier increases**: not in SB history, inferred from CC effective-bid ratios (S1) [I] | all keyword campaigns |
| 23 Sep → | Spend steps down from ~$40/day to ~$12/day; cause not recorded in either tool (0.2) | – |

- SB reports no actor (`who` = not stated).
- SellerBoard bid automation is **off** on all 40 campaigns. `automation_status` = off, `autobiding_enabled` = false. So every change was manual or came from another tool.

### 0.4 Comparability with the Day 5 and Day 10 audits

Neither the Day 5 nor the Day 10 document was available (repo and Drive searched 2026-09-25). This audit uses the S0–S10 order from the brief. Its window is the full 30 days since go-live, which contains both earlier checkpoints: Day 5 = 30 Aug, Day 10 = 4 Sep. The weekly table in S5 lets those points be read against this one.

The brief's "CVR 1.1–2.13%" range could not be fully reproduced:
- 1.10% is the 30-day blended figure [M].
- The nearest measured figures to 2.13% are **2.03%**, SB-PPC for 26 Aug–1 Sep, and **2.45%**, CC top-of-search placement for 30 days.

---

## S1: Bid mechanics (base bid vs TOS modifier, placement drift)

### 1.1 What the plan specified vs what is live

- **Plan (MKL columns AQ–AS).** Base bid = Expected CPC × 0.5, TOS +100%, so effective TOS bid = Expected CPC = **$1.00–$1.98** (mean $1.30).
- **Live.** Base bids now run $0.32–$1.29, with TOS multipliers of **4.0× to 10.0×**.
- Source: CC `ppc_campaign_targets`, bid note dated 25 Sep except boho throw blanket (13 Sep) [M].

| Campaign / target (SKU) | Plan base → eff. TOS | Live base | Live TOS modifier | Live eff. TOS bid | TOS CPC actually paid | TOS impression share (CC) |
|---|---|---|---|---|---|---|
| boho king size blanket halo (60x80) | $0.90 → $1.80 | $0.97 | **+440%** | **$5.24** | $2.46 | 3.5% |
| boho blanket | $0.52 → $1.04 | $0.75 | +300% | $3.00 | $1.26 | **0.86%** |
| boho throw blankets for couch | $0.99 → $1.98 | $1.29 | +400% | **$6.45** | $1.71 | 2.4% |
| boho throw | $0.50 → $1.00 | $0.32 | **+900%** | $3.20 | $1.21 | 12.8% |
| boho throw blanket | $0.50 → $1.00 | $0.65 | +300% | $2.60 | $1.39 | **2.1%** |
| scandinavian halo (5 kw) | $0.50–0.99 → $1.00–1.98 | $0.65–1.29 | +450% | $3.58–$7.10 | $1.22–1.60 | 7–26% |
| throw blanket for couch boho halo (5 kw) | $0.50–0.99 → $1.00–1.98 | $0.59–1.16 | +400% | $2.95–$5.80 | $0.85–2.47 | 13–21% |
| colorful halo (4 kw) | $0.56–0.92 → $1.12–1.84 | $0.76–1.24 | +380% | $3.65–$5.95 | $1.04–4.12 | 16–24% |
| boho couch blanket halo | $0.87 → $1.74 | $1.02 | +360% | $4.69 | $1.43 | 15% |
| rustic floral / patterned / branded | $0.50–0.56 | $0.60–0.75 | +380% | $2.88–$3.60 | $0.35–1.55 | 14–68% |

Remaining single-keyword campaigns and PAT (CC `ppc_campaign_targets`; bid note 25 Sep, modifier as of 24 Sep) [M]:

| Target (campaign) | Plan base → eff. TOS | Live base | Live TOS modifier | Live eff. TOS bid | TOS impression share |
|---|---|---|---|---|---|
| bohemian throw blanket | $0.73 → $1.46 | $0.52 | **+625%** | $3.77 | 11.2% |
| throw blanket boho | $0.50 → $1.00 | $0.38 | **+820%** | $3.50 | 9.3% |
| boho blankets and throws | $0.58 → $1.16 | $0.68 | +400% | $3.40 | 12.1% |
| boho blanket king (60x80) | $0.50 → $1.00 | $0.65 | +380% | $3.12 | 2.3% (98 of 108 clicks Off-Amazon) |
| boho cotton blanket | $0.54 → $1.08 | $0.63 | +400% | $3.15 | 20.2% |
| boho blanket throw | $0.58 → $1.16 | $0.50 | +460% | $2.80 | **0.7%** |
| boho picnic blanket | $0.79 → $1.58 | $0.93 | +330% | $4.00 | 7.3% |
| boho blanket king size (60x80) | $0.50 → $1.00 | $0.75 | +380% | $3.60 | 17.0% |
| boho heated blanket | $0.99 → $1.98 | $1.34 | +380% | **$6.43** | 1.4% (40 of 43 clicks Off-Amazon) |
| boho throw blanket for bed | $0.75 → $1.50 | $1.01 | +440% | $5.45 | 12.3% |
| bohemian blanket | $0.50 → $1.00 | $0.69 | +450% | $3.80 | 13.7% |
| boho blanket queen | $0.66 → $1.32 | $0.77 | +400% | $3.85 | 13.0% |
| king size boho blanket (60x80) | $0.50 → $1.00 | $0.65 | +440% | $3.51 | 15.1% |
| boho beach blanket | $0.78 → $1.56 | $1.01 | +440% | $5.45 | 17.9% |
| throw blankets for bed boho | $0.66 → $1.32 | $0.86 | +380% | $4.13 | 12.5% |
| boho cotton blankets queen size | $0.76 → $1.52 | $0.99 | +380% | $4.75 | 22.4% |
| boho king blanket (60x80) | $0.50 → $1.00 | $0.68 | +400% | $3.40 | 18.4% |
| boho cotton throw blanket no fringe | $0.50 → $1.00 | $0.68 | +380% | $3.26 | – (1 impression) |
| PAT B0BLRBXBX5 (Bouquet 60x80) | $0.45 (no TOS) | $0.59 | **+380%** | $2.83 | n/a (product target) |
| PAT ×6 other ASINs | $0.45 (no TOS) | $0.59–$0.82 | +0% | $0.59–$0.82 | n/a |

- **Coverage.** All 49 Batch 1 keyword targets carry a TOS modifier of **+300% to +900%**. The plan was **+100%**. The spend-weighted average implied on 24 Sep is +480% (1.2).
- **PAT inconsistency.** One PAT campaign carries +380% while its six siblings carry 0%. It is an un-planned setting, and a TOS modifier on a product-page conquest target is a structural error.

Reading:
- **The bid is not what limits top-of-search presence** [I]. Effective TOS bids are **2–5× the CPC actually cleared** ($1.42 on average). Yet TOS impression share on the two largest terms stayed under 1% (boho blanket) and at 2.1% (boho throw blanket). SB's own campaign `topOfSearch` field reads 0.40% and 0.64%.
- **Budget is not the constraint either.** Median budget utilisation is **4.6%** and the maximum is 53.3% (boho throw) [M, SB-PPC `BudgetUtilization`].
- **The constraint is therefore auction eligibility or relevance** at top of search for a new listing with no organic rank, not price [I]. Raising the modifier bought product-page and Off-Amazon traffic, not top-of-search share.
- **Every live effective TOS bid breaks SOP-28 M4.** M4 requires effective TOS CPC ≤ max profitable CPC for the objective. The largest max profitable CPC available at any category CVR is **$0.25** (S9). Live effective TOS bids are $2.60–$7.10, **10–28× over**.

### 1.2 Placement drift: the implied modifier over time

- **Method [I].** Implied multiple = CC spend-weighted effective TOS bid ÷ effective product-page bid. Product pages carry no modifier on these campaigns, so the ratio tracks the TOS multiplier. SB has no placement history, so this is the only dated evidence.
- **This is an estimate.** Mix changes between campaigns move the ratio slightly.

| Dates | Implied TOS multiple | ≈ Modifier | vs plan |
|---|---|---|---|
| 27–30 Aug | 2.0× | +100% | = plan |
| 31 Aug–2 Sep | 2.5–2.6× | +155% | ↑ |
| 3–11 Sep | 3.9–4.1× | +300% | ↑↑ |
| 12–16 Sep | 4.7–4.9× | +380% | ↑↑ |
| 17–24 Sep | 5.2–6.1× | +420% to +510% | ↑↑↑ |

- The 2 Sep **base**-bid raise of about +30% (S0.3) stacked on the modifier increase.
- Effective TOS bid (spend-weighted) went **$1.16 (27 Aug) → $4.95 (13 Sep) → $4.28 (24 Sep)**.
- The TOS CPC actually paid barely moved: about $1.0 in week 1, $1.2–$2.0 afterwards.

### 1.3 Daily placement table (CC `ppc_placements`, all keywords, estimated per-day split of campaign placement shares; 99.75% of spend and 99.85% of clicks covered)

ROS = rest of search. PDP = product pages. Eff. bid = CC spend-weighted effective bid.

| Date | Spend TOS | Spend ROS | Spend PDP | Spend Off-Amz | Clicks TOS | Clicks ROS | Clicks PDP | Clicks Off-Amz | CPC TOS | CPC PDP | CPC Off | Off-Amz % of clicks | Eff. bid TOS | Eff. bid PDP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 08-26 | 10.17 | 0.58 | 0.00 | 0.00 | 10.0 | 1.0 | 0.0 | 0 | $1.02 | – | – | 0% | – | – |
| 08-27 | 9.20 | 0.65 | 2.16 | 0.00 | 10.0 | 1.0 | 4.0 | 0 | $0.92 | $0.54 | – | 0% | $1.16 | $0.58 |
| 08-28 | 8.96 | 1.45 | 0.90 | 0.00 | 9.0 | 2.0 | 1.0 | 0 | $1.00 | $0.90 | – | 0% | $1.34 | $0.67 |
| 08-29 | 7.65 | 1.29 | 8.66 | 0.00 | 8.0 | 2.0 | 16.0 | 0 | $0.96 | $0.54 | – | 0% | $1.11 | $0.55 |
| 08-30 | 26.97 | 1.80 | 9.71 | 0.00 | 23.0 | 3.0 | 17.0 | 0 | $1.17 | $0.57 | – | 0% | $1.36 | $0.68 |
| 08-31 | 11.73 | 0.75 | 26.96 | 0.00 | 7.0 | 1.0 | 37.0 | 0 | $1.68 | $0.73 | – | 0% | $2.07 | $0.80 |
| 09-01 | 9.91 | 2.36 | 25.02 | 0.00 | 7.0 | 3.0 | 35.0 | 0 | $1.42 | $0.71 | – | 0% | $2.09 | $0.79 |
| 09-02 | 17.50 | 0.00 | 30.33 | 0.00 | 10.0 | 0.0 | 41.0 | 0 | $1.75 | $0.74 | – | 0% | $1.95 | $0.77 |
| 09-03 | 19.57 | 4.24 | 48.14 | 0.00 | 10.1 | 5.0 | 66.9 | 0 | $1.95 | $0.72 | – | 0% | $3.02 | $0.76 |
| 09-04 | 13.79 | 0.72 | 7.72 | 0.28 | 10.0 | 1.0 | 11.0 | 1 | $1.38 | $0.70 | $0.28 | 4% | $3.02 | $0.76 |
| 09-05 | 13.97 | 1.27 | 10.54 | 0.00 | 11.0 | 2.0 | 15.0 | 0 | $1.27 | $0.70 | – | 0% | $3.04 | $0.75 |
| 09-06 | 9.44 | 0.00 | 18.09 | 1.08 | 8.0 | 0.0 | 24.0 | 6 | $1.18 | $0.75 | $0.18 | 16% | $3.19 | $0.80 |
| 09-07 | 13.21 | 0.57 | 19.55 | 1.94 | 9.0 | 1.0 | 26.0 | 10 | $1.47 | $0.75 | $0.19 | 22% | $3.18 | $0.81 |
| 09-08 | 17.45 | 0.00 | 12.74 | 13.88 | 12.0 | 0.0 | 18.0 | 73 | $1.45 | $0.71 | $0.19 | 71% | $3.28 | $0.81 |
| 09-09 | 9.71 | 0.78 | 6.80 | 62.41 | 6.0 | 1.0 | 10.0 | 328 | $1.62 | $0.68 | $0.19 | 95% | $3.67 | $0.92 |
| 09-10 | 6.25 | 2.07 | 10.06 | 61.89 | 5.0 | 3.0 | 14.0 | 326 | $1.25 | $0.72 | $0.19 | 94% | $3.69 | $0.92 |
| 09-11 | 6.74 | 0.00 | 4.06 | 66.25 | 5.0 | 0.0 | 7.0 | 356 | $1.35 | $0.58 | $0.19 | 97% | $3.85 | $0.97 |
| 09-12 | 9.17 | 0.00 | 3.51 | 15.06 | 5.0 | 0.0 | 8.0 | 103 | $1.83 | $0.44 | $0.15 | 89% | $4.68 | $0.99 |
| 09-13 | 22.65 | 0.00 | 10.79 | 39.98 | 12.0 | 0.0 | 18.0 | 192 | $1.89 | $0.60 | $0.21 | 86% | $4.95 | $1.04 |
| 09-14 | 21.03 | 0.00 | 9.12 | 21.05 | 16.0 | 0.0 | 16.0 | 94 | $1.31 | $0.57 | $0.22 | 75% | $4.46 | $0.91 |
| 09-15 | 14.51 | 0.00 | 10.22 | 8.85 | 12.0 | 0.0 | 16.0 | 41 | $1.21 | $0.64 | $0.22 | 59% | $4.21 | $0.86 |
| 09-16 | 17.24 | 0.00 | 7.93 | 15.09 | 9.0 | 0.0 | 14.0 | 62 | $1.92 | $0.57 | $0.24 | 73% | $3.96 | $0.83 |
| 09-17 | 17.53 | 0.00 | 6.78 | 17.42 | 12.0 | 0.0 | 10.0 | 60 | $1.46 | $0.68 | $0.29 | 73% | $4.11 | $0.80 |
| 09-18 | 17.04 | 1.20 | 8.88 | 11.16 | 12.0 | 2.0 | 15.0 | 34 | $1.42 | $0.59 | $0.33 | 54% | $3.85 | $0.72 |
| 09-19 | 16.98 | 0.00 | 32.31 | 0.00 | 9.0 | 0.0 | 47.0 | 0 | $1.89 | $0.69 | – | 0% | $4.21 | $0.74 |
| 09-20 | 17.92 | 1.54 | 39.90 | 0.00 | 14.0 | 2.0 | 66.0 | 0 | $1.28 | $0.60 | – | 0% | $4.26 | $0.76 |
| 09-21 | 10.80 | 0.00 | 14.33 | 0.00 | 8.0 | 0.0 | 27.0 | 0 | $1.35 | $0.53 | – | 0% | $3.94 | $0.65 |
| 09-22 | 22.38 | 1.84 | 15.86 | 0.00 | 11.0 | 2.0 | 28.0 | 0 | $2.03 | $0.57 | – | 0% | $4.42 | $0.81 |
| 09-23 | 4.97 | 0.00 | 7.17 | 0.00 | 3.0 | 0.0 | 11.0 | 0 | $1.66 | $0.65 | – | 0% | $4.04 | $0.77 |
| 09-24 | 2.70 | 0.00 | 7.14 | 0.00 | 2.7 | 0.0 | 11.3 | 0 | $1.01 | $0.63 | – | 0% | $4.28 | $0.74 |
| **30 d** | **407.14** | **23.11** | **415.38** | **336.34** | **286** | **32** | **630** | **1,686** | **$1.42** | **$0.66** | **$0.20** | **64%** | | |

### 1.4 Placement outcome (CC campaign-grain, measured) [M]

| Placement | Spend | Share | Clicks | CPC | Orders | CVR | Cost per order |
|---|---|---|---|---|---|---|---|
| Top of search | $408.22 | 34.5% | 286 | $1.43 | 7 | 2.45% | $58.32 |
| Product pages | $417.21 | 35.2% | 631 | $0.66 | 5 | 0.79% | $83.44 |
| Rest of search | $23.16 | 2.0% | 32 | $0.72 | 1 | 3.1% | $23.16 |
| Off-Amazon | $336.34 | 28.4% | 1,686 | $0.20 | 16 [I] | 0.95% [I] | $21.02 [I] |
| **Total** | **$1,184.93** | | **2,635** | **$0.45** | **29** | **1.10%** | **$40.86** |

- **Off-Amazon orders are inferred.** They are total orders minus the measured on-Amazon orders. CC withholds an Off-Amazon CVR by rule (sales "too sparse to rate").
- **Almost all of it came from one campaign.** The 60x80 halo "boho king size blanket" (SV 94) produced 1,027 of the 1,686 Off-Amazon clicks and 15,936 of its 17,339 impressions. All 9 of its orders were outside TOS and product pages. That is inferred from its placement rows, which show 0 orders on 9 on-Amazon clicks.
- **Off-Amazon has no bid lever.** Sponsored Products carries no modifier for it (CC). It is a placement the plan never contemplated, and it cannot build search rank.
- **On-Amazon CVR is 1.37%** (13/949; 95% CI 0.63–2.11%). That is the relevant figure for a ranking push.

---

## S2: True organic rank vs the plan's assumed rank

### 2.1 Coverage

- **Plan's rank input.** MKL column R "Organic Rank" is **undated and unsourced**.
- **Data Dive.** The only rank radar on this product tracks **B0GGT3PZ8K (Butterfly 60x80)**. That is not the Butterfly 50x60 child (B0GGT7NYJ6) that 41 of 49 Batch 1 terms route to.
  - It began on 1 Sep, so **no 26 Aug baseline exists**.
  - It covers **23 of 49** Batch 1 terms.
  - Children in one variation family usually share search placement, so it is a reasonable proxy [I], but it is not the routed ASIN.
- **CC crawl.** It covers 38 of 49 terms, ran on 25 of 30 days, and did not run 26–30 Aug.

### 2.2 Batch 1: plan vs measured (DD-RR; "> 100" = beyond the tracked depth)

| Keyword | Plan rank (MKL) | Target | DD 2 Sep | DD 25 Sep | Best (date) | CC crawl first → latest |
|---|---|---|---|---|---|---|
| boho throw blanket | 7 | 5 | 59 | **92** | 59 (2 Sep) | #68 (31 Aug) → #104 (24 Sep) |
| boho blanket | 4 | 3 | 85 | **> 100** | 85 (2 Sep) | #100 → #136 |
| boho throw | 2 | 3 | > 100 | 92 | 68 (19 Sep) | |
| throw blanket boho | 7 | 4 | > 100 | > 100 | 94 (14 Sep) | |
| boho blanket throw | 5 | 4 | > 100 | > 100 | 49 (18 Sep) | |
| bohemian throw blanket | 11 | 4 | > 100 | 59 | 59 (25 Sep) | |
| boho beach blanket | 44 | 3 | > 100 | > 100 | – | never ranked |
| boho throw blanket for bed | 13 | 4 | > 100 | > 100 | 18 (8 Sep) | |
| bohemian blanket | 16 | 4 | > 100 | 87 | 70 (15 Sep) | |
| boho blanket queen | 43 | 4 | > 100 | > 100 | 40 (6 Sep) | |
| boho throw blankets for couch | 20 | 4 | > 100 | 80 | 49 (15 Sep) | |
| throw blankets for bed boho | 11 | 4 | > 100 | > 100 | 73 (7 Sep) | |
| boho cotton blanket | 2 | 4 | > 100 | **29** | 14 (6 Sep) | |
| boho blanket king size | 5 | 3 | > 100 | > 100 | – | never ranked |
| boho blankets and throws | 8 | 4 | 82 | > 100 | 82 (2 Sep) | |
| king size boho blanket | 21 | 3 | > 100 | > 100 | – | never ranked |
| boho blanket king | 21 | 3 | > 100 | > 100 | – | never ranked |
| throw blanket for couch boho | 14 | 4 | > 100 | > 100 | 41 (12 Sep) | |
| blanket boho | 4 | 4 | > 100 | > 100 | 95 (14 Sep) | |
| rustic floral boho blanket | 89 | 4 | > 100 | **23** | 23 (19 Sep) | |
| boho scandinavian cotton blanket | not indexed | 4 | 6 | **11** | 3 (11 Sep) | |
| cotton boho blanket | 1 | 4 | 34 | 39 | 25 (11 Sep) | |
| boho cotton throw blanket | 7 | 4 | 41 | 26 | 26 (24 Sep) | |
| boho picnic / king / heated blanket | 44 / 2 / 41 | 5 / 3 / 3 | not tracked by DD | | | CC: **never ranked** on any of 25 crawled days |

### 2.3 Findings

- **The plan's rank input does not describe this listing.**
  - 52 DD-tracked terms carry an MKL organic rank of 10 or better. **None** of them is at 10 or better today.
  - The radar summary reads **top-10 keywords: 0**, top-50 keywords: 15.
  - The largest assumed gaps, e.g. boho blanket assumed #4 against #85 or worse, mean the "climb of 1 position" stated in the MKL Reasoning was in fact a climb from page 2–3 or beyond [M].
- **Rank moved the wrong way on the head terms during the push** [M]:
  - boho throw blanket 59 → 92
  - boho blanket 85 → > 100
  - boho blankets and throws 82 → > 100
- **Gains were on long-tail cotton terms that bought little PPC:** boho cotton blanket, rustic floral, cotton throw terms. This is consistent with organic relevance for "cotton", not PPC velocity [I].
- **Nine Batch 1 terms were never ranked on any crawled day:** the king/queen size terms, picnic, heated, beach and blue. These are the terms S7 flags as mis-specified.

---

## S3: Plan vs reality (the MKL model's inputs against live data)

### 3.1 The model is uncomputed, not merely mis-baselined

MKL columns reverse-engineered on all 49 Batch 1 rows. Every identity holds exactly [M]:

```
Adjusted PPC CVR  = Click Share% × 1.5            (SV-to-CVR factor 0.5 → ×1.5)
No of Click Req.  = Daily Target ÷ Adjusted CVR   = 1 ÷ Adjusted CVR
PPC Daily Budget  = No of Click Req. × Expected CPC
Proposed Bid      = Expected CPC × 0.5            with TOS% = 1.0 (+100%)
```

| Model input (MKL) | State in WB | What it should be | Consequence |
|---|---|---|---|
| **DSTR / DSTR (30 Days)** | **Empty on all 7,795 rows** | Daily sales at target rank (from competitor or SQP velocity) | No sales requirement exists, so there is nothing to size |
| **Daily Target** | **1 on all 49 Batch 1 rows** | DSTR − organic contribution, floor 1 | Every term is sized to 1 order/day, regardless of whether it is 9,420 or 1 SV |
| Keyword Clicks / Sales / Conversion L4W, Conversion Share, Seller Benchmarked, Competitor, Expected Conversion Rate | **Empty** | Measured inputs | Target Rank has no benchmark behind it |
| Adjusted PPC CVR | 12.0–17.7% (mean 15.8%) = **click share × 1.5** | A conversion rate | **Unit error.** A share of clicks is not a probability of purchase. Measured: **1.10%** blended, 1.37% on-Amazon, **1.71% market (SQP)** |
| Expected CPC | $1.00–$1.98 (mean $1.30) | Measured clearing CPC | Measured TOS CPC $1.42: close for TOS, but the model has no placement dimension |
| No of Click Required | 5.7–8.3 per term per day (Σ 313.7/day) | Daily Target ÷ real CVR | At 1.71% market CVR, **58.5 clicks/day per term for 1 order** (7–10× the model) |
| PPC Daily Budget | Σ **$407.90/day** (CS says $414) | Clicks × CPC | Actual spend averaged **$39.50/day** (9.7% of plan) because bids, not budget, bound (S1) |
| Organic Rank | Undated | Dated tracker read | S2: 0 of 52 "top-10" terms actually top-10 |
| Search Volume | MKL | DD | DD is a median 2.36× MKL |
| Economics | **No margin, contribution or ceiling column** | Contribution $ and max profitable CPC per SKU (SOP-41) | No row can be tested against SOP-23 O3 or SOP-28 M4 |

### 3.2 What the empty DSTR and Daily Target = 1 invalidate

1. **Every budget, click requirement and bid in Batch 1.** They were derived from Daily Target = 1 and a CVR 9–16× too high. None of them sizes a rank climb.
   - At honest inputs (1 order/day at 1.71% market CVR, TOS CPC $1.42), one term needs about **$83/day**.
   - Batch 1's 49 terms would need about **$4,070/day**, before any DSTR above 1.
2. **The Reasoning column's stop rule.** "Stop when the term delivers its required clicks and rank does not move" uses required clicks of about 6/day. Almost every term cleared that threshold within days without moving rank. The stop condition was therefore met early and never actioned, or it is meaningless [I].
3. **Target Rank values** (3–5 on every term). With no DSTR, competitor or seller benchmark, the targets are assertions, not model outputs.
4. **The SOP-23 M2 loss ceiling.** Push ACoS minus break-even, times projected sales, cannot be computed without DSTR. So no push on this product has had a loss ceiling.
5. **The MKL's claim "launch spend here is deliberately unprofitable and priced that way"** has no price attached. Nothing in the workbook states the planned loss.

### 3.3 Planned vs realised, Batch 1 aggregate (30 days) [M]

| Metric | Plan (model, ×30) | Actual | Actual ÷ plan |
|---|---|---|---|
| Spend | $12,237 | $1,184.93 | 9.7% |
| Clicks | 9,411 | 2,638 (949 on-Amazon) | 28% (10%) |
| CVR | 15.8% | 1.10% | 7% |
| Orders | 1,470 (49/day) | 29 | 2.0% |
| Terms at target rank | 49 by "1–2 batch cycles" | 0 | 0% |

---

## S4: Match type analysis

- **All spend is Exact.** 100% of keyword spend (CC byMatchType covers 98.5% of product spend; the rest is ASIN-targeted PAT).
- **There is no Auto, Phrase or Broad.** So there is no discovery layer and no negative-keyword architecture [M].

| Exact serving mode (SB `st_by_keyword`) | Spend | Clicks | Orders | CVR |
|---|---|---|---|---|
| Search term identical to keyword | $972.59 | 2,118 | 22 | 1.04% |
| Close variants (plural, re-ordered, "for bed") | $204.92 | 509 | 7 | 1.38% |

Internal cannibalisation: Exact close variants that are themselves another campaign's keyword [M].
- "boho blankets and throws" served **"boho blanket throw"**: $56.42, 68 clicks, 0 orders. That is 2× what the "boho blanket throw" campaign itself spent on its own term ($25.35).
- "boho blanket king size" served "boho blanket king": $8.95, 0 orders.
- "boho cotton throw blanket" served "boho throw blanket": $1.29.

Irrelevant-intent exact terms were bought as launched (S7). The zero-order ones: heated $19.66, picnic $21.43, beach $6.03, boho blanket king size $19.66, king size boho blanket $10.74, boho king blanket $1.54, boho blanket queen $11.95, boho cotton blankets queen size $3.40. **Together $94.41, 0 orders.**

Two king-size terms did convert: the 60x80 halo "boho king size blanket" (9 orders) and "boho blanket king" (3). All 9 halo orders fall outside TOS and product pages, i.e. they came from Off-Amazon traffic [I].

**Verdict.** Exact-only is correct for a rank push. But with no Auto/Broad research lane, the listing's real converting queries were never discovered. The search-term report only contains the terms the plan chose.

---

## S5: Campaign analysis (utilisation, concentration, dormant campaigns)

### 5.1 Concentration (CC, 40 campaigns, $1,184.93) [M]

| Top N campaigns | Spend | Share |
|---|---|---|
| 1 (60x80 halo, boho king size blanket) | $205.77 | 17.4% |
| 3 | $459.59 | 38.8% |
| 5 | $619.40 | 52.3% |
| 10 | $892.54 | 75.3% |

- **31 of 40 campaigns produced 0 orders** ($390.88).
- The 9 order-producing campaigns account for all 29 orders.

### 5.2 Utilisation (SB-PPC `BudgetUtilization`, 30-day average) [M]

- Median **4.6%**, maximum 53.3% (boho throw, $6 budget).
- No campaign was budget-capped.
- The two budget raises (boho blanket to $40, boho throw blanket to $30) bought nothing: utilisation stayed at 13.5% and 5.0%.

### 5.3 Dormant (< 10 clicks in 30 days): 20 of 40 campaigns [M]

- **All 10 PAT campaigns.** $18.30, 29 clicks, 4,559 impressions, 0 orders; 2 had zero clicks.
- **Halos:** couch, patterned, no-fringe, rustic floral, queen size.
- **Single-keyword:** king size boho blanket, beach, throws-for-bed, boho king blanket, branded.
- **Reading:** 20 campaigns × one observation each is 20 campaigns that the Launch-stage cadence cannot read.

### 5.4 Weekly trend (SB-PPC; buckets as resolved by SellerBoard) [M]

| Week | Spend | Impr | Clicks | CPC | Orders | CVR | Sales | ACoS |
|---|---|---|---|---|---|---|---|---|
| 26 Aug–1 Sep | $166.61 | 14,504 | 197 | $0.85 | 4 | 2.03% | $123.96 | 134% |
| 2–8 Sep | $273.60 | 29,440 | 367 | $0.75 | 5 | 1.36% | $142.95 | 191% |
| 9–15 Sep | $422.96 | 33,692 | 1,594 | $0.27 | 14 | 0.88% | $433.86 | 97% |
| 16–22 Sep | $294.13 | 32,125 | 444 | $0.66 | 6 | 1.35% | $204.93 | 144% |
| 23–24 Sep* | $23.22 | 2,506 | 29 | $0.80 | 0 | 0% | $0 | – |

\*Settling: 7-day attribution, CC settled through 18 Sep.

- **Business side** (SB-P&L, calendar weeks): organic units rose **3 → 5 → 11 → 20** (26 Aug–21 Sep).
- **TACoS** was **81%** in week 1, 168% on 1–7 Sep and **44%** on 15–21 Sep (SB `RealACOS`).
- Organic lift is real but **cannot be attributed to PPC** [I]:
  - head-term rank fell in the same weeks (S2)
  - the growth sits in children not advertised (Sunflower and Bloom 60x80: 11 organic units)

---

## S6: Syntax analysis (four quadrants against SQP market benchmarks)

- **Command-center has no syntax library for product 41.** `ppc_syntax_groups` returns 0 groups, all 65 terms are unclaimed, and CC SQP market CTR/CVR is therefore unavailable [M].
- **Groups used instead:** the MKL "Syntax Groups" column.
- **Benchmark used instead:** DD-SQP market CTR/CVR on the terms it covers.

| Syntax group | Terms | Spend | Clicks | Orders | Our CTR | Our CVR | ACoS | SQP terms | Market CTR | Market CVR | Quadrant |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Core | 26 | $720.05 | 1,206 | 15 | 1.60% | 1.24% | 153% | 16 | 1.25% | 1.77% | **CTR ≥ mkt / CVR < mkt**: listing wins the click, loses the sale |
| Size | 8 | $286.54 | 1,173 | 12 | 6.29%† | 1.02% | 77% | 4 | 1.92% | 0.42% | CTR ≥ / CVR ≥ (†Off-Amazon inflated; the market figure is thin: 4 king terms, 2 purchases) |
| Material | 6 | $96.75 | 109 | 2 | 1.06% | 1.83% | 156% | 4 | 2.16% | 0.95% | **CTR < mkt / CVR ≥ mkt**: underexposed where the listing converts |
| Color | 2 | $24.07 | 79 | 0 | 7.09%† | 0% | – | 0 | – | – | no benchmark |
| Pattern | 2 | $4.93 | 4 | 0 | – | 0% | – | 1 | 2.88% | 0% | insufficient |
| PAT (ASIN) | 7 | $14.90 | 23 | 0 | 1.41% | 0% | – | – | – | – | insufficient |
| Not in MKL (plurals and variants) | 12 | $28.44 | 28 | 0 | – | 0% | – | – | – | – | – |

Caveats:
- Our CTR includes product-page and Off-Amazon impressions, while SQP market CTR is search-results only. **The CTR axis is not like-for-like**; the CVR axis is. The daggers mark groups dominated by Off-Amazon.

Reading [I]:
- **Core** (61% of spend) is the losing quadrant: a click-winner that converts below market. That is a listing, price or review problem, not a bid problem. The SOP-23 conversion clause ("Brand CVR ≥ Market CVR") fails for the syntax that carries the budget.
- **Material** (cotton) is the only quadrant where we out-convert the market. It is also where organic rank improved (S2). It is the one segment that deserves any residual attention, but S9 still applies to it.

---

## S7: Keyword research quality

| Check | Finding | Source |
|---|---|---|
| Volume of the MKL | 7,795 rows; **3,322 (42.6%) have SV = 0**; 3,143 syntax "Irrelevant" | WB [M] |
| Two relevancy systems disagree | **1,506 rows** are "Final Categorization = Relevant/Highly Relevant" **and** "Updated Relevancy % = 0" | WB [M] |
| Disqualified terms in Batch 1 | **14 of 49** Batch 1 rows carry Updated Relevancy 0%, including **boho heated blanket** and **boho picnic blanket**, whose source is `disqualifier_override:category` (the MKL's own disqualifier). Size terms "king/queen" are also 0% (product is 50x60 / 60x80 throw) | WB [M] |
| Categorisation mix of Batch 1 | 4 Highly Relevant, 25 Relevant, **18 Lower Relevant**, 2 Branded | WB [M] |
| Indexing | **13 of 49** Batch 1 terms "Not Indexed" at plan time | WB [M] |
| Rank input | 0 of 52 "top-10" terms verified top-10 (S2) | DD-RR [M] |
| SV scale | MKL SV ≈ 1/2.4 of Data Dive SV (median, 81 terms); the head term is 9,420 vs 25,418 | DD-RR [M] |
| Branded rows | MKL types them Halo/**Ranking**; CS types them **Defensive**; live is "Branded" | WB, CC [M] |
| Workbook integrity | Orphan truncated row **"d flower and butterfly throw blanket"** (Ranking/Exact, no batch). CS Batch 2 subtotal and "TOTAL" rows are **duplicated** (118 kw vs 123 kw). CS $414/day ≠ MKL $407.90/day. "boho blanket queen" routed to two different sizes | WB [M] |
| Catalogue identity | **B0GGTMTB4Y is both the "parent ASIN" in the brief and the Bloom 50x60 child SKU** in SB and CC. SB lists it with price $0, no image and a different title ("SLEEPHORIA Throw Blanket 50x60 Inches…"). It has never had stock | SB-PROD, SB-INV, CC [M] |
| Omitted high-intent material terms | "cotton throw blanket" (DD SV 31,206; SQP 4,256 market clicks in 7 days) and "100% cotton throw blanket" (7,232) sit in Batch 2, although Material is the one quadrant that out-converts (S6) | DD, WB [M] |
| Competitor set | DD niche nUARjsKofz (21 Sep, 17 competitors): **none of our 16 ASINs** in it. Niche benchmark price **$29.99**, 781 reviews, 1,034 units/month. Only niche mlBooc4oU0 includes B0GGT3PZ8K (ranking juice 356,598, highest in that 9-ASIN niche; median 270,951) | DD-N [M] |
| CC competitor mapping | Product 41 has **no mapped competitors** (`traffic_market_keywords`: unknown_product) | CC [M] |

**Verdict.** The MKL is broad but unreliable at the three points the launch depended on: rank, volume and relevancy. The Batch 1 selection admitted terms the list itself disqualifies.

---

## S8: Batch 1 sufficiency

| Test | Result |
|---|---|
| Were enough clicks bought to judge CVR? | Blended: **2,638 clicks, 29 orders; CVR 1.10% (95% CI 0.70–1.50%)**. On-Amazon: 949 clicks, 13 orders; 1.37% (CI 0.63–2.11%). **Sufficient to reject** every CVR above 2.1%, and so every CVR that S9 shows would be needed (≥ 9%) [M] |
| Per term | 16 of 49 terms reached ≥ 20 clicks; **6 reached ≥ 100** (the SOP-22 validated-CVR line): boho king size blanket 1,031; boho throw blankets for couch 446; boho blanket 185; boho throw 125; boho blanket king 108; bohemian throw blanket 104. Best of these: 2.9% |
| Were enough clicks bought to judge rank? | On the two head terms, **TOS share never exceeded 2.1%**, so the push did not test rank-for-velocity. It tested whether a new listing can win top of search, and it could not at 2–5× the clearing CPC (S1) |
| Is Batch 1, as a roster, sufficient? | No. 14/49 terms are disqualified or irrelevant (S7), 13/49 were not indexed, and 26/49 are not rank-tracked in DD. The strongest segment (Material/cotton) is under-weighted (6 terms, $96.75) |
| Should Batch 2 proceed? | **No.** Batch 2 is planned at $550/day across 55 campaigns, with the same model (Daily Target 1, click-share CVR) and the same THIN margin. The S9 gate fails before sizing |

---

## S9: Economics gate (SOP-41 F1: max profitable CPC = contribution $ × CVR)

**Contribution** = AOV − COGS − FBA fee − referral − freight-in.

Inputs:
- Price, fee and COGS: SB-PROD, 2026-09-25.
- Referral = 15% of price. SB's `ReferralFee` field shows 0 or $0.30 on SKUs with no recent sale, so the standard rate is applied.
- **Freight-in = $0.** SB carries a single COG element with `cost_of_shipping` = 0. CC labels its cost "manufacturing + shipping". For 50x60 both read $11.43, so freight is inside COGS. For 60x80, CC's $15.84 is the sensitivity case (9.4).

### 9.1 Per SKU

Max profitable CPC is shown at four CVRs: measured blended 1.10%, measured on-Amazon 1.37%, SQP market 1.71%, and the framework target (market × 3.0 = 5.14%).

| Pattern | Size | ASIN | Price | Referral | FBA | COGS | **Contribution** | **BE ACoS** | @1.10% | @1.37% | @1.71% | @5.14% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Butterfly | 50x60 | B0GGT7NYJ6 | 26.99 | 4.05 | 7.46 | 11.43 | **4.05** | 15.0% | $0.045 | $0.055 | $0.069 | $0.208 |
| Bouquet | 50x60 | B0GGT9SNJ1 | 26.99 | 4.05 | 7.55 | 11.43 | **3.96** | 14.7% | $0.044 | $0.054 | $0.068 | $0.204 |
| Botanical | 50x60 | B0GGT2LPZX | 26.99 | 4.05 | 7.55 | 11.43 | 3.96 | 14.7% | $0.044 | $0.054 | $0.068 | $0.204 |
| Mosaic | 50x60 | B0GGSXZBD9 | 26.99 | 4.05 | 7.55 | 11.42 | 3.97 | 14.7% | $0.044 | $0.054 | $0.068 | $0.204 |
| Sunflower | 50x60 | B0GGTBJDXK | 26.99 | 4.05 | 7.55 | 11.42 | 3.97 | 14.7% | $0.044 | $0.054 | $0.068 | $0.204 |
| Songbird | 50x60 | B0GGTC573S | 26.99 | 4.05 | 7.55 | 11.42 | 3.97 | 14.7% | $0.044 | $0.054 | $0.068 | $0.204 |
| Oasis | 50x60 | B0GGTD499H | 26.99 | 4.05 | 7.55 | 11.42 | 3.97 | 14.7% | $0.044 | $0.054 | $0.068 | $0.204 |
| Bloom | 50x60 | B0GGTMTB4Y | **$0 in SB** | – | – | 10.90 | **not computable** | – | – | – | – | – |
| Butterfly | 60x80 | B0GGT3PZ8K | 34.99 | 5.25 | 7.89 | 16.74 | **5.11** | 14.6% | $0.056 | $0.070 | $0.088 | $0.263 |
| Sunflower | 60x80 | B0GGT7JH3M | 34.99 | 5.25 | 7.89 | 16.70 | 5.15 | 14.7% | $0.057 | $0.071 | $0.088 | $0.265 |
| Bloom | 60x80 | B0GGTD46ZF | 34.99 | 5.25 | 8.12 | 16.73 | **4.89** | 14.0% | $0.054 | $0.067 | $0.084 | $0.251 |
| Bouquet | 60x80 | B0GGTFFB8R | 34.99 | 5.25 | 8.12 | 16.74 | 4.88 | 13.9% | $0.054 | $0.067 | $0.084 | $0.251 |
| Botanical | 60x80 | B0GGTMPDKC | 34.99 | 5.25 | 8.12 | 16.73 | 4.89 | 14.0% | $0.054 | $0.067 | $0.084 | $0.251 |
| Mosaic | 60x80 | B0GGTVBWN8 | 34.99 | 5.25 | 8.12 | 16.73 | 4.89 | 14.0% | $0.054 | $0.067 | $0.084 | $0.251 |
| Oasis | 60x80 | B0GGTHTHYH | 34.99 | 5.25 | 8.12 | 16.73 | 4.89 | 14.0% | $0.054 | $0.067 | $0.084 | $0.251 |
| Songbird | 60x80 | B0GGTP95BJ | 34.99 | 5.25 | 8.12 | 16.73 | 4.89 | 14.0% | $0.054 | $0.067 | $0.084 | $0.251 |

Known figures verified:
- **$3.96 (50x60) and $4.89 (60x80)**: ✅
- **BE ACoS 14.7% / 14.0%**: ✅
- **Trailing ACoS 130.8%**: ✅ (CC 130.8%; SB 130.34%)
- **CVR 1.10%**: ✅. The upper bound of 2.13% was not reproduced (S0.4).
- **SOP-23 O3 class:** every SKU is **THIN** (< $6). The O3 cap on Expected CPC = contribution ÷ 3 = **$1.32 (50x60) / $1.63 (60x80)**. **16 of 41** 50x60 Batch 1 rows and 1 of 8 60x80 rows were planned with an Expected CPC above that cap. **Candidacy should have closed at the planning stage.**

### 9.2 Per size: the CVR required to justify the bids actually running

| Size (contribution) | Blended CPC $0.45 | On-Amazon CPC $0.89 | TOS CPC $1.43 | Live effective TOS bid (range $2.60–$7.10) |
|---|---|---|---|---|
| 50x60 ($3.96) | **11.3%** (6.6× market) | 22.6% (13.2×) | **36.0%** (21×) | 66%–179%: impossible |
| 60x80 ($4.89) | **9.2%** (5.4× market) | 18.3% (10.7×) | **29.2%** (17×) | 53%–145%: impossible |

**Highest CVR the category produces.** SQP market CVR is 1.71% across the Batch 1 terms and 1.59% across all 40 SQP terms. The best single term is 3.92% ("throw blanket for couch decorative", 73 clicks). The best Batch 1 term is 3.68% ("throw blanket for couch boho", 148 clicks). **No observed term reaches even the lowest requirement (9.2%).**

### 9.3 Net profit / loss per week at current spend, by CVR scenario

Current run-rate (CC, 30 days ÷ 30 × 7): spend **$276.48/week**, clicks **615.5/week**, blended CPC $0.449. Contribution recovered = clicks × CVR × contribution.

| CVR scenario | CVR | Orders/wk | 50x60: contribution / **net** | 60x80: contribution / **net** |
|---|---|---|---|---|
| Actual blended | 1.10% | 6.77 | $26.80 / **−$249.69** | $33.09 / **−$243.39** |
| Actual on-Amazon | 1.37% | 8.43 | $33.39 / **−$243.09** | $41.23 / **−$235.25** |
| Actual TOS placement | 2.45% | 15.07 | $59.66 / **−$216.82** | $73.67 / **−$202.81** |
| SQP market | 1.71% | 10.55 | $41.76 / **−$234.72** | $51.57 / **−$224.92** |
| Framework target (3.0×) | 5.14% | 31.64 | $125.28 / **−$151.20** | $154.71 / **−$121.78** |
| Break-even | 11.3% / 9.2% | 69.8 / 56.5 | $276.48 / $0 | $276.48 / $0 |

These nets exclude storage and returns (9.5), so they flatter the result.

### 9.4 Cost to acquire one order vs contribution per unit

| Basis | Cost per order | ÷ 50x60 contribution ($3.96) | ÷ 60x80 contribution ($4.89) |
|---|---|---|---|
| All PPC (CC, $1,184.93 / 29) | **$40.86** | **10.3×** | **8.4×** |
| On-Amazon only ($848.59 / 13) | $65.28 | 16.5× | 13.4× |
| Top of search ($408.22 / 7) | $58.32 | 14.7× | 11.9× |
| Off-Amazon [I] ($336.34 / 16) | $21.02 | 5.3× | 4.3× |

- **Clicks-to-loss.** Contribution ÷ CPC is the number of clicks one order can pay for. At TOS CPC it is **2.8 (50x60) / 3.4 (60x80)**. At blended CPC it is 8.8 / 10.9. **Actual clicks per order: 91.**
- **Sensitivity (60x80 at CC's $15.84 COGS).** Contribution becomes $5.78–$6.01 (BE 16.5–17.2%). Max CPC at 3× market becomes $0.30–$0.31, against the $0.45 blended and $1.43 TOS actually paid. **The conclusion does not change.**

### 9.5 Costs outside the SOP-41 identity (SB-P&L, 30 days) [M]

| Line | $ | Per unit (54 units) |
|---|---|---|
| Sales | 1,686.47 | 31.23 |
| Referral (commission) | −253.05 | −4.69 |
| FBA fulfilment | −411.29 | −7.62 |
| COGS | −792.15 | −14.67 |
| Refunds | −28.11 | −0.52 |
| **Contribution before ads and storage** | **201.87** | **3.74** |
| FBA storage (billed in the week of 1 Sep) | −829.86 | −15.37 |
| Advertising | −1,181.70 | −21.88 |
| **Net profit** | **−1,809.69** | **−33.51** |

- **Storage alone** ($829.86 for the month, on about 4,225 units on hand; stock at cost $59,109) **exceeds the product's total monthly contribution 4×** at current velocity [M].
- The product is loss-making before any advertising. That is a price and inventory problem PPC cannot solve.
- **Price that would clear the gate** [I, arithmetic], with fees and COGS held:

| Case | Contribution needed | 50x60 price | 60x80 price |
|---|---|---|---|
| Blended CPC $0.45 at 3× market CVR | $8.74 | **$32.61** (+$5.62) | **$39.52** (+$4.53) |
| Blended CPC at market CVR | $26.22 | $53.17 | $60.08 |
| TOS CPC $1.43 at 3× market CVR | $27.77 | $55.00 | $61.91 |

- **DD niche benchmark price is $29.99.** Its 50x60 leaders sell at $17.99–$23.99 (VANJOROY, XIBLC, Wzvzss, ERZVND); the 60x80 leaders at $29.99–$43.99 (MSGKV, Bailix, LUTBM).
- **The 60x80 has price headroom to about $39.52.** Its competitors LUTBM ($43.99, 3,727 units/month) and jinchan ($52.99) prove buyers accept it [I]. **The 50x60 does not:** it is already priced $3–$9 above its best-selling competitors.

### 9.6 Gate verdict

> **FAIL: at the current price ($26.99 / $34.99) and cost base, Product 41 cannot be advertised profitably at any conversion rate the category produces.**
>
> - The CVR required at the CPC actually paid (9.2–11.3% blended; 29–36% at top of search) is 5–21× the SQP market rate. It is 2.5–7× the best single term observed (3.9%).
> - Even at the framework target of 3× market, every size loses $122–$151 per week at current spend.
> - The system holds no ceiling to stop this: no `product_targets` row [S], a null CC break-even, and an MKL without economics columns.
> - Per SOP-23 X5, the failure is economic and routes to pricing, COGS and inventory, not to a bid.

---

## S10: Actions (prioritised, each with owner and evidence)

- **P1** = today · **P2** = this week · **P3** = next weekly cycle · **P4** = monthly.
- **Owners:** Spec = PPC Specialist · Lead = PPC Lead / Manager · Brand = brand owner (P&L authority) · Data = command-center / data owner · Ops = inventory and catalogue.

| # | P | Action | Owner | Evidence and arithmetic |
|---|---|---|---|---|
| A1 | P1 | **Treat SellerBoard status fields as unreliable** and confirm the live state of all 40 campaigns and 37 ad groups in the Amazon console. Then take the S9 decision deliberately: if spend is to stop, pause at campaign level and record the date and reason ("S9 gate fail") in the change log | Spec | S0.2: SellerBoard shows 0 of 37 fully Active, yet command-center shows 38 campaigns delivering impressions on 22–24 Sep. Every order costs $40.86 against $3.96–$4.89 contribution |
| A2 | P1 | **Do not launch Batch 2.** Remove it from the queue until A4 and A5 are resolved | Lead | CS: $550/day = $3,850/week. Same uncomputed model (S3) and same THIN margin (S9.1). At the blended CPC of $0.449 and 3× market CVR (5.14%), a 50x60-routed Batch 2 would buy 8,575 clicks and 441 orders a week. That is $1,746 of contribution against $3,850 of spend: **−$2,105/week** |
| A3 | P1 | **Escalate the S9 verdict to the brand owner** as the headline: "cannot be advertised profitably at current price and cost". Options with arithmetic: (a) 60x80 price test to about **$39.52**, which clears break-even at blended CPC and 3× market CVR, supported by competitors at $43.99–$52.99; (b) COGS/FBA reduction worth about $4.78 per 50x60 unit; (c) an explicit, capped investment budget with a written loss ceiling (SOP-23 M2) and end date; (d) organic-only operation | Brand | S9.3–S9.6 |
| A4 | P2 | **Load economics into the system.** Create the `product_targets` / ceiling row. Complete CC fee snapshots for price, referral and fulfilment on all 16 SKUs. Set break-even ACoS 14.7% / 14.0% and max CPC per SKU | Data + Lead | S0.1: CC economics null on 16/16. SOP-41 G9 is PROVISIONAL until every active row carries contribution |
| A5 | P2 | **Rebuild the MKL model.** Populate DSTR (SQP or competitor velocity). Replace "click share × 1.5" with a measured CVR (1.37% on-Amazon, 1.71% market). Recompute Daily Target, required clicks, budgets and the SOP-23 loss ceiling. Add the dated honeymoon exit | Lead | S3.1: 7,795 empty DSTR; Daily Target = 1 on 49/49; model CVR 9–16× reality |
| A6 | P2 | **Before any re-enable, reset TOS modifiers** to a value that satisfies SOP-28 M4 (effective TOS ≤ max profitable CPC). Today that means **TOS 0% and base bids ≤ $0.25**, which will not win top of search. So re-enabling a rank push is **not recommended** until A3 changes contribution | Spec | S1.1: live +300% to +900%, effective $2.60–$7.10 against a $0.20–$0.25 ceiling |
| A7 | P2 | **Permanently retire the mis-specified, zero-order Batch 1 terms:** boho heated blanket, boho picnic blanket, boho beach blanket, beach blanket boho, king size boho blanket, boho blanket king size, boho king blanket, boho blanket queen, boho cotton blankets queen size. Negate them in any future discovery campaign. **Review, don't retire,** "boho king size blanket" and "boho blanket king": they converted (9 and 3 orders), but mostly via Off-Amazon traffic that builds no rank | Spec | S7: 0% relevancy / disqualifier override. S2: never ranked. S4: $94.41 at 0 orders |
| A8 | P2 | **Register objectives** for the 20 undeclared campaigns in the CC Campaign Registry. Rename to the plan convention, or document the live convention as the standard | Spec + Data | S0.1: 20/40 "not declared" ($341.48, 28.8% of spend invisible to objective reporting) |
| A9 | P2 | **Treat Off-Amazon as an ungoverned placement.** If any campaign is re-enabled, check whether the console exposes an Off-Amazon placement control. If not, keep such campaigns off, or budget-cap them and measure separately | Lead | S1.4: 64% of clicks, $336.34, no modifier lever. Conversion is unmeasurable by CC rule |
| A10 | P2 | **Fix the catalogue collision on B0GGTMTB4Y**: it is both the brief's parent ASIN and the Bloom 50x60 child, with $0 price, no image, a different title and never stocked. Correct the parent/child mapping in SB, CC and the workbook | Ops + Data | S7 |
| A11 | P3 | **Inventory decision for the 3,954 units** in Butterfly 50x60 (1,044), Butterfly 60x80 (904), Bouquet 50x60 (1,041) and Bouquet 60x80 (965), selling at 0.01–0.94 units/day. Storage cost $829.86 for the month. These units were first stocked 20–21 May, so they reach 181 days of age around **17 Nov 2026**. Check the current aged-inventory surcharge rates (not pulled here) and run the SOP-27 / LTSF decision: price, removal or liquidation | Ops + Brand | SB-INV; S9.5. **[I]** The aged-surcharge date is derived from first-stock dates. Rates are not verified |
| A12 | P3 | **Replenishment only where it pays.** Sunflower 60x80 (22 units, reorder flag YES, reorder date 25 Sep, qty 45) and Bloom 60x80 (19 units) are the two SKUs with organic sell-through and no ad spend. 10 SKUs are at 0 stock (6 since 22–25 Jul, Mosaic 60x80 since 1 Aug, Mosaic 50x60 since 5 Sep, Sunflower 50x60 since 24 Aug, and Bloom 50x60 never stocked). Do not reorder 50x60 until A3 resolves price | Ops | SB-INV, SB-P&L: Sunflower 60x80 +$28.92 and Bloom 60x80 +$39.41 net, the only profitable SKUs |
| A13 | P3 | **Rank tracking on the routed ASIN.** Add B0GGT7NYJ6 and the 26 untracked Batch 1 terms to a Data Dive rank radar, but only if a paid programme resumes. **Cost before spending:** RANK_RADAR_KEYWORDS 6,100 / 9,200 used (3,100 headroom); 26 terms would use about 26 if billed per keyword (billing unit not confirmed by the API). No quota was spent in this audit. No niche dive is needed: niche nUARjsKofz is 4 days old. Adding our ASIN to it would use DIVED_ASINS (765 / 2,500 used; refresh 9 Oct), and the per-dive consumption is not exposed | Lead | S2.1; DD quota read 25 Sep |
| A14 | P3 | **Workbook hygiene**: resolve "boho blanket queen" routing (MKL 50x60 vs CS 60x80); remove the orphan "d flower and butterfly throw blanket" row; de-duplicate the CS Batch 2 subtotal and TOTAL rows; reconcile $414 vs $407.90; align Branded objective (Defensive, not Ranking); add or drop "white boho throw blanket" | Lead | S0.1, S7 |
| A15 | P3 | **Close internal overlap** if any campaign is re-enabled: negate "boho blanket throw" in the "boho blankets and throws" campaign, and "boho blanket king" in "boho blanket king size" | Spec | S4: $56.42 + $8.95 at 0 orders |
| A16 | P4 | **Monthly (M1):** track the product on CM2 after storage, not ACoS. Re-run this S9 gate after any price or COGS change, before any spend is restored | Lead + Brand | S9.5: contribution $3.74/unit before storage and ads, −$11.63/unit after storage |

### What I measured, inferred, and could not see

- **Measured:**
  - every spend, click, order, bid, budget, status, rank, SQP, price, fee, COGS and stock figure, from the tagged sources on the dates shown
- **Inferred (marked [I]):**
  - Off-Amazon orders (the residual)
  - modifier dates (from CC effective-bid ratios)
  - pause timing
  - the diagnosis that relevance, not price, limits TOS share
  - the aged-inventory date
  - price-headroom judgements
- **Not available in this session:**
  - the V4.1.1 template, and the Day 5 and Day 10 audits
  - a direct read of the `product_targets` table
  - SellerBoard status and placement-modifier history (and SellerBoard's current status fields contradict the delivery data, S0.2)
  - CC syntax groups and SQP market CVR for product 41 (DD-SQP used instead)
  - DD rank before 1 Sep, and DD rank on the routed 50x60 child
  - CC competitor mapping
  - current Amazon aged-inventory surcharge rates
