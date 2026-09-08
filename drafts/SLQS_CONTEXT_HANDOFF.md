# SLQS — Context Handoff

*Paste this whole file into a new chat. State as at 8 September 2026.*

Repo `zarlish-web/ppc-audit-`, branch `claude/ppc-audit-skill-9263gn`.
Full report: `drafts/SLQS_Full_Report_07Sep2026.md`. Read that for detail; this is the carry-over.

---

## 1. The product

**Sleephoria Quilt Set (SLQS)** — parent ASIN **B0GZW9QWJM**, 21 child SKUs: Twin / Queen / King × black, ivory, light grey, navy blue, sage green, taupe, white. Account: Inspiratek & Ecotero LLC.

It is an **aged-stock clearance product**, not a growth product. **2,283 units on hand** (7 Sep), no inbound, no pending removals. Twin White and Twin Sage Green already out of stock.

## 2. The economics — the numbers everything is judged against

| Line | Per unit |
|---|---|
| Selling price on deal | $30.08 |
| Amazon fees (referral + FBA) | −$16.58 |
| Cash received | **$13.50** |
| Deal commission 1% | −$0.30 |
| **Forward-cash ad ceiling** | **$13.20** ← the hard cap |
| Economic ceiling (incl. $3.81/unit/mo avoided storage) | $17.01 |
| Actually paid on 6 Sep | −$21.31 ← the problem |
| Cost of goods (sunk) | −$11.49 |

Plus a **fixed $70/day deal fee**. On a full-cost basis only $1.71/unit is left for ads — this is a clearance play, not a scale play.

**Standing recommendation: continue the deal, bring ads to ~$8/unit, hold volume above 25 units/day.** The loss is in the ad rate, not the deal. Liquidation returns $1.40/unit vs $13.20 through Amazon before ads — about **$26,900** across current stock, or ~$4,100 after ads at $8 and the deal fee.

## 3. Performance

Seven days (31 Aug – 6 Sep): **161 units, $17.10/unit in ads, −$1,119 after deal fees.** Only 3 Sep was positive (25 units at $9.93/unit, +$11). The 5–6 Sep bid push lifted volume to 30 then 53 units but drove the click price to $21.31.

Sponsored Products same window: **$2,737.94 spend · 3,996 clicks · 131 orders · $4,195.03 sales · $0.69 CPC · 3.28% CVR · $20.90 cost per sale · 65% ACoS.** $647 (26%) of live-target spend produced no orders. One Broad keyword — "king size bedspread" — took $351.22 at a $39.02 cost per sale against a $13.20 ceiling.

**Queen Sage Green is the working template** — 12 units at $9.84/unit ads, +$4.94 each. Proof it clears profitably at the deal price when the click price is right.
**Queen Ivory is the largest single loss** — $177 on 6 Sep. A rate problem from shared campaigns, not a SKU problem: its three dedicated campaigns ran a healthy $12.59 cost per sale.

## 4. The two live decisions

**(a) The Best Deal (promo 7993fa1d) ends 13 September** — every figure above describes the deal period, and nothing is decided for 14 Sep onward. Most time-sensitive item on the list.

**(b) The advertising is not pointed at the stock we hold.** Queen Light Grey, King Light Grey and King White hold **1,142 units — half the inventory** — sold 28 of 160 units, convert at 1.3% vs the 1.9% deal average, and clear in **326 days**. Meanwhile Queen Ivory has **16 days of stock** and takes the most spend ($19.37/unit). Whole catalogue at 20 units/day is **114 days to clear**. This is a routing fix, not a bid fix.

## 5. Deployed vs queued

**Deployed 5 Sep, verified** — every one of 796 decided values checked against the live 6 Sep export, zero mismatches (358 placement percentages, 279 keyword bids, 69 campaign budgets): bid/budget/placement/state changes, 18 new SP campaigns (501 rows, $300/day), the bid push (87 rows). Dayparting (11pm–3am pause) and manual re-optimisation applied 7 Sep.

**Built, ready to upload:** ceiling correction (26 rows — 15 pauses, 11 bid cuts) · 70 catalogue negatives · SD bulk (39 rows, 2 campaigns, $22/day).
**Spec ready, console entry needed:** 5 Sponsored Brands Product Collection campaigns, $54/day (needs a logo in the Creative Asset Library) · 3 SD audience campaigns, $20/day (no existing account example of the audience syntax to model from).

**Change loader plan** — 96 changes in four groups, 15/15 validation checks passed, every prior value matched to the live account:

| Group | Rows | Prediction |
|---|---|---|
| Pause targets that returned nothing | 15 | −$32.54/day, orders unchanged |
| Reprice "king size bedspread" | 1 | Cost per sale $39.02 → $17.17 |
| Bring ten targets to the ceiling | 10 | Cost per sale band near $17.30 |
| Catalogue negatives | 70 | −$24.65/week off-catalogue spend |

**−$552.90/week (−$78.99/day).** Blended cost per sale $20.90 → **$16.68** (CVR holds) or **$18.17** (orders fall with bids). Mechanism checks 14 Sep, outcome checks 21 Sep. Cuts target **$17.30**, not $13.20 — step one of two, because a single move to $13.20 would drop these targets out of useful placements at once.

The 7 Sep stop-loss file (270 product-ad rows, 5 SKUs) is **superseded** by the ceiling correction.

## 6. The negation rule (came out of this cycle)

A term **outside the catalogue** can be blocked at **one click**. A term **inside the catalogue** needs **three or more clicks**. Relevance picks the lever; clicks decide whether there is evidence to pull it. A relevant term that costs too much gets a bid cut, not a negative.

That took an earlier 196-row / 14-root list down to **70 rows across 5 roots**: full size (24 clicks, $10.59), cal king (13, $6.81), california king (10, $4.14), super king (4, $2.53), bed skirt (1, $0.58) — all zero orders. Applied across the 14 Broad, Phrase and Auto campaigns; Exact and product-targeting excluded.

- **"split king" was blocking a sale** — "bedspread for split king bed" produced an order at $0.82. A Split King is two Twin XLs on a king base, so a King bedspread fits. Removed.
- **Eight roots had no evidence at all** — twin xl, crib, toddler, daybed, mattress pad, weighted, heated, sheet set have never taken a click. Held, not dropped.
- **177 terms with 3+ clicks and no orders ($868.70) are deliberately not negated** — they are the product's own market ("king size bedspread", "oversized king quilt"). Blocking them takes the product off its own market; the bid is the lever.
- **Colour roots excluded** — "solid charcoal lightweight quilt" was the best-converting term in the report at $0.64, despite charcoal not being stocked. Shoppers approximate colour. Size is different: a California King shopper cannot be satisfied by a King.

Twice now a root that looked safe to block was making money. That is what the click rule catches.

## 7. Open items

| # | Item | Owner |
|---|---|---|
| 1 | Upload the ceiling correction — 26 rows | PPC |
| 2 | Upload the catalogue negatives — 70 rows | PPC |
| 3 | Upload the SD bulk — 39 rows | PPC |
| 4 | Build the 3 SD audience campaigns in console | PPC |
| 5 | Build the 5 SB campaigns (logo asset first) | PPC |
| 6 | Review or rebuild the 18 Sep Lightning Deal — 17 of 19 products flagged | Deals |
| 7 | Re-run the LTSF workbook on current stock — totals overstated ~40% | Finance |
| 8 | Reach $8/unit while holding 25+ units/day | PPC |
| 9 | Settle landed cost — Sellerboard $11.49 vs LTSF workbook $16.50, ~$11,400 gap | Finance |
| 10 | **Decide what happens after 13 September** | Deals |
| 11 | **Point the advertising at the stock we hold** | PPC |
| 12 | Confirm what prices return to on 14 September | Deals |
| 13 | Re-verify the change plan against a fresh export (manual changes 7 Sep) | PPC |

## 8. The 18 September Lightning Deal (promo 4c755087)

Separate from the running Best Deal. 4:25am–4:25pm, **1 unit per product**, $70 fee. **17 of 19 products flagged "discount too low"** — 16 have the promotion price exactly equal to the live price, one (Twin Taupe) is priced $2.55 *above* it. Only King Taupe and King Ivory qualify, at 4.4% off.

Cause: the running deal already took prices down, so there is no headroom to discount from. **Do not rebuild it yet** — eligibility is measured against the featured offer, and those are Best Deal prices expiring 13 Sep. Re-read after 13 Sep and before 18 Sep, then rebuild with real discounts and a real unit commitment, or cancel.

## 9. Campaign structure

**Live — 18 new SP campaigns, $300/day:** Broad 3 campaigns / 42 keywords · Phrase 7 / 139 · Exact 2 / 21 · Auto 4 (one targeting group each, isolated) · Product & category targeting 2 / 19 targets. All placement modifiers open at 0%. Dynamic bids – down only throughout, so bids can fall but never escalate.

Note: Sponsored Brands cannot land on a product detail page; with no Store, the landing page would be Amazon's generated collection page.

## 10. Corrections that changed conclusions — carry these forward

- **The selling price came from the wrong source.** The bid push was sized on the ad platform's $41.51 attributed ASP; the real figure is Sellerboard's **$30.08** net of the deal. A 38% error that set the ceiling more than twice too high. **Rule: the ad ceiling comes from Sellerboard net of fees, never from the advertising platform's attributed sales.**
- The ceiling moved three times: $29.93 → $13.50 (real price known) → $13.20 (1% deal commission). The $70/day fee sits on top of all three.
- **Budget utilisation was misread** — 30 days of spend compared against a daily budget. Corrected: 26.9% across enabled quilt campaigns. Budget was never the constraint.
- **79 decided rows contradicted themselves** — "No change" alongside 40–45% bid cuts, inherited from an earlier file. Would have deployed as real cuts on keywords marked undecided.
- **The inventory age report returned blank columns** — every age bucket and LTSF field read zero across all 1,221 SKUs. Empty, not zero.
- **A count was quoted from memory** — 585 changing rows claimed; 892 counted.
- **The liquidation comparison was overstated** — $1.79/unit and a $40,700 gap, built on the workbook's stale 3,530-unit count. Correct: **$1.40/unit, ~$26,900** on the 2,283 units actually on hand. Amazon still wins by a wide margin; the advantage was overstated by about half.
- **Cost of goods disagrees between two company files** — Sellerboard $11.49, LTSF workbook $16.50 weighted. Does not change the forward-cash plan; does change the full-cost read. Finance to settle.

## 11. Sources

Sellerboard grouped by parent, daily (31 Aug – 6 Sep) · SP bulk export (31 Aug – 6 Sep) · SB/SD bulk export (31 Aug – 6 Sep) · FBA inventory report (7 Sep) · LTSF September workbook (uploaded 3 Sep, internal data 17 Aug) · Best Deal page 7993fa1d (read 7 Sep) · Lightning Deal page 4c755087 (read 7 Sep 14:57 UTC) · SP Search Term Report, quilt campaigns only (31 Aug – 6 Sep) · Helium 10 Xray competitor pull (4 Sep) · Seller Central variation family (4 Sep).

## 12. Where the files are

**In the repo (committed, survives):**
- `drafts/SLQS_Full_Report_07Sep2026.md` — the full report
- `drafts/SLQS_PPC_Plan_v6_04Sep2026.md` / `.html`, `drafts/SLQS_PPC_Plan_v7_05Sep2026.md` / `.html`
- `drafts/SLQS_Backtest_Against_Updated_Skill_04Sep2026.md`
- `skills/inspiratek-clearance-audit/` — SKILL.md (steps 0–9) + 9 references
- `inspiratek-clearance-audit.skill` — the installable skill
- `scripts/` — `build_hc.py`, `write_hc.py`, `md2gdoc.py`

**Session scratchpad only — these are LOST when the container is reclaimed:** decided bulks v6–v16, `SLQS_UPLOAD_SP_CEILING_07Sep2026.xlsx`, `SLQS_UPLOAD_SP_NEGATIVES_v2_08Sep2026.xlsx`, `SLQS_UPLOAD_SD_CREATES_05Sep2026.xlsx`, the SB/SD build specs, and `SLQS_change_loader_plan_FINAL_08Sep2026.csv`. **Re-download anything still needed before leaving this session.**

## 13. Governing rules the quilt work runs under

Clearance is the aged-stock branch of the account's PPC family. Economics, objective bands and verdict vocabulary are locked canon in `pmp-optimization-sr` → `reference/decision_framework.md`. Writing and validation: `ppc-decision-reasoning`. Plan and workbook: `ppc-plan-builder`, `ppc-workbook-builder`.

- **Advertising is usually the smallest leak on an aged product** — quantify all ten levers first, then size the PPC plan against what it can deliver.
- **The objective re-tag at step 1 is what makes a liquidation run different.** Ranking, Market Share, Discovery and Profitable Conversion all become LTSF-Clearance; only Defensive on a brand term survives. **The label always changes; performance decides the bids.** Reading placement for cost is allowed; buying placement for rank is barred.
- **Three numbers per child, bid sits between them:** floor $0.25 · max profitable CPC (margin × CVR) · max click price ((contribution + avoided charge) × CVR). The gap is the subsidy zone — bid low in it, the cap is a maximum, never a target.
- **The correction ladder:** <30% no change · 30–50% a few cents · 50–70% cut 20% · 70–100% cut 30% · 100%+ cut 50% even on one order, pause if still there next cycle.
- **Operating floors:** $0.25 minimum bid, $5.00 minimum daily budget. Nothing is ever cut to a value between zero and the floor.
- **Budget is not a waste lever** — a cap is not a spend. Growth comes from targets, cost control from the bid.
- **Never negate below the sufficiency line** — 15 clicks with no orders at ordinary click prices, 20–25 where clicks cost ≤$0.15. Reaching the line triggers a review, not an automatic pause.
- **Attribute through product-ad rows, never campaign totals.**
- **Ceiling tests use cost per unit cleared,** not cost per ad-attributed order.
- **Ask rather than resolve** — a contradiction is a question for whoever prepared the data.
- **Publish as HTML, not Markdown** — Markdown into Google Drive loses fenced and inline code.

---

*Inspiratek & Ecotero LLC · Confidential*
