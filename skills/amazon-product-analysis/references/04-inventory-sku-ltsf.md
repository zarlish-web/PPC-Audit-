# 04 — Inventory, variations and LTSF

Read in Phase 2. Output of this file: **which variation each campaign should advertise, which SKUs block pushing, and what to do with aged stock.** Economics used here (margin, break-even, ceilings) come from `03-profitability-and-guardrails.md`.

Source tags: [INV] inventory checkup · [LTSF] LTSF dossier · [PB] plan builder · [WB] workbook builder · [PF] placement-first · [SR] optimization engine · [DR] decision reasoning · [PH] phasing · [B6] B6 engagement, Sep 2026.

## Contents
1. Inputs and counting rules
2. Velocity and cover formulas
3. Stock-out-before-arrival test (ROOM / TIGHT / SWITCH)
4. Zones Green / Yellow / Red and actions
5. Projected days of cover through checkpoints
6. Push stock gate
7. Variation roles and routing rules
8. SKU provenance, halo rate, economics rebuild
9. Backup switch simulation
10. Recovery push
11. Inbound onto overstock, trajectory and peak-week rules
12. Distorted-window velocity correction
13. Inventory × PPC decision table
14. LTSF and aged inventory
15. Anti-patterns
16. Open questions for the owner

---

## 1. Inputs and counting rules

| Input | Fields | Rule | Tag |
|---|---|---|---|
| Inventory export per SKU (full, unfiltered — never the variation page) | SKU, ASIN, available, reserved, on-hand, units in production, units shipped/in transit, next in-stock date (date / "Today" / "Not in horizon"), planned daily velocity | Read the unfiltered file before filtering; audit on-hand − available − reserved: gap > **5 units** → verify at source before zoning | [INV, PB, PF, WB] |
| Product Ad rows (bulk) | advertised SKU per ad group, state | The only source of routing (§7) | [WB] |
| Advertised product / targeting report | 7-day advertised SKU units, spend | Spend > 0 = actively advertised | [INV] |
| Preferred → Backup pairs | per size/syntax | **Ask the owner to paste them. Never auto-derive.** Dedupe repeats | [INV] |
| Lead time | days | Default **90 days** (confirm) | [INV] |
| Aged inventory / LTSF charge file | units per age bracket (all 8), cu ft per unit, invoice | See §14 | [LTSF] |
| Deal calendar | dates, SKUs, deal price | Needed for distorted-window correction (§12) and event cover | [B6, PB] |

**Counting rules** [B6 R-I6, WB]:
1. Count **available** units plus **dated, confirmed** arrivals within the horizon. Transfers count toward replenishment only; customer orders never count.
2. Inbound counts toward cover only if its ETA ≤ the SKU's current days of cover; otherwise there is a gap before it lands.
3. Stock status comes from velocity + inbound + lead time, **never from "units > 0"**. [SR]
4. If a report has no SKU column, map campaign → SKU by name substring, **longest SKU first** (CALIFKING before KING), fallback ASIN substring — then verify against Product Ad rows. [INV]

---

## 2. Velocity and cover formulas

| Metric | Formula | Tag |
|---|---|---|
| Units/day (gating pace) | Units sold ÷ days, **30-day window**; 7-day pace shown as an early warning | [B6] |
| Planned velocity | Inventory file's planned daily velocity ("Base SV") — show beside the actual; gate on the 30-day actual | [INV] (see open question 1) |
| PPC daily velocity | Σ 7-day advertised SKU units ÷ 7 (context: how much the ads move) | [INV] |
| Days of cover (available) | Available ÷ units/day | [INV, B6] |
| Total days incl. inbound | (Available + dated inbound in horizon) ÷ units/day | [INV] |
| Days to next arrival | Next dated arrival − today ("Today" = 0; none = blank → "no scheduled arrival") | [INV, B6] |
| Max affordable velocity (stock only) | Available ÷ lead time | [INV] |
| Max affordable velocity (incl. transit) | (Available + transit) ÷ lead time | [INV] |

Never compute cover on a push pace or an engine forecast — an inflated pace invents stock-outs. Example (B6): "White runs out at push pace 3 days before arrival" moved 75 Queen campaigns to the 7th-best colour; on the 30-day pace there was no stock-out. [B6 F30]

**Per-SKU velocity status (diagnostic, first match)** [INV]:
| Condition | Status | Implied action |
|---|---|---|
| Arrival scheduled and cover < days to arrival | OOS RISK | Protect: cut PPC aggression, pause ranking pushes until the shipment lands |
| Velocity > max affordable velocity (stock only) | Demand outruns stock | Reduce PPC aggression / slow velocity |
| Velocity < max affordable velocity (incl. transit) | Healthy | PPC OK — continue / scale carefully |
| Otherwise | Stable | Hold and monitor |
Sort: OOS RISK → Demand outruns stock → Stable → Healthy, then days left ascending. Zones (§4) still govern the decision; this status explains it.

---

## 3. Stock-out-before-arrival test

Run for every advertised SKU with a dated inbound. Cover on the 30-day pace. [B6, INV, register #9]

| Result | Condition | Zone | Action | Tag |
|---|---|---|---|---|
| ROOM | Cover ≥ days to next arrival | per §4 | Push allowed only if cover ≥ days to arrival **+ 7** and the SKU is Green | [B6 R-I2, register #9] |
| TIGHT | Cover < days to arrival by **≤ 7 days** | **Red** | Ease (taper) the push so stock lasts to the arrival; **no colour swap** — a swap costs more than a short ease | [B6 R-I3] |
| SWITCH | Cover < days to arrival by **> 7 days** | **Red** | Switch ranking ads to the size's backup colour (same size, same price) if the backup passes §9 | [B6 R-I4] |
| OUT | Available = 0 | Red | Pause the push; ranking ads to backup | [B6 R-I5] |
| — | Available < 7 days of cover | Red | No push; break-even pricing only | [B6 R-I1] |
| No arrival | No dated inbound | per §4 | Zone by cover alone | [INV] |

Why: stock-out before inbound arrives destroys rank regardless of how many days of cover the headline figure shows.

---

## 4. Zones and actions (resolved defaults)

| Zone | Condition (advertised variation) | Action | Tag |
|---|---|---|---|
| **Green** | ≥ **60** days of cover, and no stock-out before arrival | Push and scale allowed (other gates permitting) | [PB, WB] |
| **Yellow** | **21–59** days | **No new push, no raises; keep current spend**; write a dated re-entry plan: restock date, keywords resuming, target rank each resumes at | [register #10, PB] |
| **Red** | **< 21** days, **or** stock-out before inbound arrives (TIGHT/SWITCH/OUT) | Protect: taper to defence; re-point the same day to the next viable child of the same size (§7); no bids on zero-stock rows unless re-pointed | [PB, WB, PF, register #9] |

Rules:
1. Re-point order: follow the syntax's priority list; check each candidate's own zone; skip Yellow/Red; among viable children pick by velocity, margin and recent CVR (tie: higher CVR at lower CPC, then longer clean history). **All children Red → escalate as a supply problem.** [PB]
2. Taper size on Red rows: gradual cut cap (≤ 15%/cycle) unless the re-point makes the cut unnecessary; during a deal hold price and watch the stock-out date. [SR]
3. A Red child that is still selling keeps its ad; an ad is paused only at zero stock or on the owner's approved list. Re-pointing = enable/add the next child's ad. [WB]
4. Every Yellow/Red hold carries its dated re-entry plan; a hold without one fails the quality gate. [PB]
5. New campaign launch needs the routed SKU ≥ **21 days** of cover (launch floor, not the 60-day push gate); else no campaign. [PB]
6. Traffic of any kind only while the SKU is Green or Yellow **and** margin > 0. [WB]
7. The engine's 14/30-day bands are superseded (lead times of 60–90 days make them too late). [register #9]

---

## 5. Projected days of cover through checkpoints

- **Projected cover at checkpoint** = (available + dated inbound landing by then − (baseline units/day + the push's extra units/day) × days to checkpoint) ÷ baseline units/day. [PB, WB]
- A push whose projected cover drops into Yellow or Red before its checkpoint is **blocking**: shrink the rank gap, wait for the inbound, or get an explicit time-boxed owner acceptance. [PB]
- Log the conflict to the Supply Chain register: SKU, projected date it leaves Green, the push causing it, fix (expedite, PO date, safety stock). [PB]
- Events: stage the bid plan against **max-sales-day** days of cover, not average daily cover. [PB]

---

## 6. Push stock gate (all must pass for PUSH)

1. Advertised variation is the size's hero (or its approved backup after a switch). [B6 R-C1]
2. Zone **Green** (≥ 60 days, 30-day pace). [PB]
3. Cover ≥ days to next dated arrival **+ 7**. [register #9]
4. Available ≥ 7 days of cover. [B6 R-I1]
5. Projected cover stays Green through every checkpoint (§5). [PB]
6. No trajectory flag (§11). [PB]
7. For a clearance push: the hero of that size is not Red. [SR]
Fail any → WAIT (name the failing item and its re-entry date).

---

## 7. Variation roles and routing rules

| Role | Definition | Advertised by | Tag |
|---|---|---|---|
| **Preferred / hero** | The size's best seller (Example (B6): White in every size; Twin used Sage Green while White was 0) | Ranking campaigns; brand/defensive campaigns | [B6 R-C1, R-N3] |
| **Backup** | Owner-named same-size alternative | Ranking campaigns when the hero fails §3 | [B6 R-C6, INV] |
| **Clearance colour** | Per size: ≥ **180 days** of cover, or ≥ **90 days** while selling ≤ the size's median velocity | Discovery (auto/broad/phrase) campaigns | [B6 R-C2] |
| **Named colour** | Colour in the search term | Campaigns on colour-named terms | [B6 R-C3, PH] |

Why: rank accrues to the hero; discovery traffic is broad and cheaper, so it should move slow stock while the hero's stock is reserved for ranking.

Routing rules (register #29):
1. **Read routing from Product Ad rows, never from campaign names.** In one audited account, 212 of 251 name-derived routings were wrong. [WB]
2. Ranking advertises the size's best seller; discovery advertises the clearance colour; colour-named terms advertise the named colour in the term's size. Sizeless terms → the size hero, else the product hero. [B6, SR]
3. **Size never changes** on any switch — hard block (only exception: correcting a wrong size). [B6 R-C4, E9]
4. Never add or switch to a colour with < **7 days** of cover. [B6 R-C5]
5. Attribute in the query (size/colour) routes only to the matching SKU; if that SKU is OOS, hold at the bid floor — no substitute. Close colours only where the account has ruled them equivalent. [PB, WB]
6. Colour target is set per objective before any other write on the campaign. [B6]
7. Switches are applied by hand (they do not upload), flagged for human confirmation, with size confirmed unchanged. [B6 E8]
8. Backup self-competition: if the backup is already advertised in another campaign, say "swapping competes with its own campaign"; else "clean to redeploy". [INV]
9. Transition back: suggest (never auto-swap) returning to the preferred SKU when its cover > **21 days**; pushing resumes only when it is Green again. [SR]
10. Live keyword for another product form (off-listing, e.g. for sheets: body, travel, sham, toddler, protector, insert, topper) → pause. [WB]
11. Foreign SKU (another product's child) in this product's campaign = finding. Shared multi-product campaigns are excluded from colour and price automation; decide them in their own product's audit. [WB, B6 E13]
12. Shared head term across sibling products: owner = highest **margin/order × sibling CVR on the shared root × sibling inventory days**; exact tie → human. [PB]
13. Routing actions: REPRICE TO ROUTED CHILD (bid only) ≠ SWITCH AD (two ad rows: enable new, keep/pause old). A held row with a Green sibling → SWITCH AD; Yellow sibling → time-boxed switch with a flip-back date; none → stay paused, naming the siblings checked. [WB]

---

## 8. SKU provenance, halo rate, economics rebuild

Before reading any CPA, CVR or rank on a row, establish **which SKU was advertised over the window** (Product Ad states over the long window and both 7-day windows). [PB §11, WB]

| Case | Meaning | Action | Tag |
|---|---|---|---|
| **Match** | Intended SKU advertised all window | Proceed | [PB] |
| **Mismatch** | Another SKU advertised all window | Correct price now if over the correct SKU's ceiling; read cleanly forward only | [PB] |
| **Mixed** | Changed mid-window | Use the post-change portion if ≥ 15 clicks; else formula-only corrections | [PB, WB] |
| **Wrong from the start** | Clear majority of conversions belong to another variation | Routing error: re-point, rebuild ceilings on the true margin/AOV, reset CVR baseline and rank clock | [PB] |

- **Halo rate** = units shipping on a non-advertised SKU ÷ total units attributed to the ad. Cite it on every re-route (e.g. basket sales incl. halo reached 81% in one product). [PB, PF]
- **Economics rebuild on re-route** (any cause): margin, break-even, ceilings from the new SKU in the same write; reset CVR baseline, rank clock, ROS lift. [PB, B6]
- Mass re-route: a pooled placement estimate may stand in, never as a shared verdict; each row graduates when **it** reaches 15 clicks on the correct SKU. [PB]
- Rank collapse concentrated in one colour/size family during an outage = **stock signature**, not a demand or relevance problem. [LTSF]

---

## 9. Backup switch simulation

Only for pairs whose preferred SKU is currently advertised. Apply the **preferred SKU's velocity** to the backup. [INV]

- Backup cover (stock) = backup available ÷ preferred velocity.
- Backup cover (incl. transit) = (backup available + transit) ÷ preferred velocity.

| Verdict | Condition | Written recommendation |
|---|---|---|
| **No — backup also OOS** (red) | Backup stock + transit = 0 | Needs production |
| **Yes — covers full lead time** (green) | Cover incl. transit ≥ lead time (default 90 d) | Switch fully sustains until replenishment |
| **Partial** (amber) | Cover incl. transit ≥ **30 days** | Partial bridge; watch |
| **No — only N days** (red) | Otherwise | Insufficient |
Extra wording: backup stock 0 but transit > 0 → "covers only after transit lands". Suffix per §7 rule 8. The switch also needs backup cover ≥ 7 days today (§7 rule 4).

---

## 10. Recovery push

Conditions (all): SKU back to Green; its best rank in the last 12 months was top 5–10; CVR ≥ benchmark; the loss is logged as an inventory cause. → Fund to the **pre-decline baseline**: week 1 re-point + maintenance, week 2 push, checkpoint at week 3. Recovery candidates inherit their prior ceiling and are funded before an equal Cold candidate. [PB]

---

## 11. Inbound onto overstock, trajectory and peak-week rules

1. **Inbound onto overstock:** compare units in production + transit with current days of cover and the product's cover ceiling. Inbound landing on an overstocked product regenerates LTSF exposure — a clear-only plan that ignores it treats the symptom. Cover ceiling: **Owner decision — ask** (engine carries an unused 120-day overstock marker). [LTSF, SR]
2. **Trajectory:** ≥ 60 days of cover with velocity down **15% WoW for 3 consecutive weeks** = cover rising because demand is falling. Not safe to push; diagnose first. [PB]
3. **Peak week:** where a demand calendar or deal schedule marks a week as peak, peak-week availability outranks aged-stock/LTSF economics (peak stock-out costs ~3× to recover; excess past peak only costs storage). Only when a calendar actually marks the week. [PB]
4. RED tier LTSF SKUs freeze future purchase orders (§14.5). [LTSF]

---

## 12. Distorted-window velocity correction

Never take velocity from an OOS, suppressed or deal window at face value. Record: trailing velocity, correction factor (e.g. 0.67), and its basis (which days removed, what replaced them). An unstated haircut or uplift is an untagged assumption and is **rejected**. [LTSF] Deal days are excluded from settled reads for 2 weeks (03 §10). [SR]

---

## 13. Inventory × PPC decision table

What each stock state allows, per objective, for the variation a campaign advertises. First apply 03's economics; this table only restricts further.

| Stock state | Ranking (push terms) | Ranking (HOLD RANK / non-push) | Defensive / brand | Profitable Conversion / Conquest | Discovery | Clearance (aged SKU) |
|---|---|---|---|---|---|---|
| **Green** (≥ 60 d, ROOM + 7) | PUSH allowed if goal gate + qualification pass | Hold / walk to break-even per 03 | Normal; keep on hero with enough budget | Normal; SCALE-eligible per 03 §6.2 | Advertise clearance colour; normal | Break-even PPC on forward cash; clearance push only if the size's hero is not Red |
| **Yellow** (21–59 d) | No new push, no raises; keep current spend; dated re-entry | Hold price; no raises | Hold; no raises | No raises; cuts per economics still run | No raises | No raises; continue ladder levers that are not PPC |
| **Red — TIGHT** (short ≤ 7 d before arrival) | Ease the push so stock reaches arrival; no swap | Ease; no swap | Ease; keep on hero | Taper | Must not advertise this SKU (clearance colour has ≥ 90 d) | n/a |
| **Red — SWITCH** (short > 7 d) or < 21 d | Stop push; re-point same day to backup (same size) if §9 passes; else taper to defence | Re-point or taper | Re-point to backup; keep the brand shelf | Taper ≤ 15%/cycle or re-point | Re-point | Never push; if hero Red, no clearance push on that size |
| **OUT** (available 0) | Pause push; ads to backup | Ads to backup | Ads to backup | No bids on this SKU | No bids on this SKU | — |
| **LTSF YELLOW/RED/CRITICAL** (§14.5) | Goal likely Clearance → no allowance (03 §1) | Standard ceiling | Unchanged | Standard ceiling | Route discovery to aged child | Ladder rung per §14.10; PPC is family 2 of 5 |
Always: ≤ 1 lever change per row per cycle; every hold names its re-entry date. [DR, PB, B6, SR, WB]

---

## 14. LTSF and aged inventory

Governing principles [LTSF]: rank options by **forward net recovery**; **COGS is sunk and never enters**; **floor = salvage parity, not break-even**; diagnose demand-curve defects before discounting; every decision has an expiry date.

### 14.1 Rate card — $ per **cubic foot** per month (never per unit)
Assessed on the **15th** of each month on the bracket held that day; surcharge starts at 181 days.

| Age (days) | $/cu ft/month | Per-unit minimum | × 181–210 rate | Rate one bracket later |
|---|---|---|---|---|
| 0–180 | 0.00 | — | — | 0.50 |
| 181–210 | 0.50 | — | 1.0× | 1.00 |
| 211–240 | 1.00 | — | 2.0× | 1.50 |
| 241–270 | 1.50 | — | 3.0× | 5.45 |
| **271–300** | **5.45** | — | **10.9× — the cliff** | 5.70 |
| 301–330 | 5.70 | — | 11.4× | 5.90 |
| 331–365 | 5.90 | — | 11.8× | 6.90 |
| 366–455 | 6.90 | $0.30/unit if greater | 13.8× | 7.90 |
| 456+ | 7.90 | $0.35/unit if greater | 15.8× | 7.90 |

- Effective $/unit/month = rate × cu ft per unit (from 366 d: the greater of that and the per-unit minimum).
- Reading it per unit overstates holding cost 1.4–4.8×. Examples: quilt set 0.704 cu ft → $3.84/unit at 271–300 d (per-unit reading $5.45 = 1.42× too high); satin sheet set 0.246 cu ft → $1.34 (3.7×). Same-age SKUs can differ 60% on volume, so allocation is not a pure velocity ranking. [LTSF]
- A flat-rate projection understates a batch approaching the cliff by up to 3.6×; always age units forward. [LTSF]

### 14.2 Fee defaults and timing [LTSF]
| Item | Default |
|---|---|
| Removal fee | $0.97–1.17/unit → use **$1.07** |
| Disposal fee | $1.07/unit |
| Liquidation recovery | 5–10% of ASP → **7.5%**; liquidation fee 2–3% → **2.5%** |
| Coupon redemption | $0.60 |
| 3PL handling (removal to resale) | $0.90/unit |
| Referral | 15% |
| Salvage resale value | 50% of price (replace with a real figure before any terminal call) |
| Critical product charge | $5,000/month |
| Months-to-clear cap | 12 |
Timing: units cleared or removed before the 15th avoid that month's charge; a removal order submitted by 23:59 PT on the deadline exempts the units even if unshipped. Outlet deals take 1–4 weeks to accept → submit **60–90 days before the cliff**; unaccepted as the cliff nears → price drop or removal now.

### 14.3 Decision math (run as a script; never hand-calculate) [LTSF]
```
Net proceeds/unit   = price × (1 − discount) − referral fee − FBA fee          (no COGS)
Removal net/unit    = resale salvage − removal fee − 3PL cost
Liquidation net     = price × recovery% − price × liquidation fee%
Disposal net        = − disposal fee
Salvage/unit        = MAX(removal net, liquidation net, disposal net)
LTSF/unit/month     = monthly charge ÷ aged units   (or rate × cu ft)
LTSF until sold     = LTSF/unit/month × min(months to clear, 12)
Floor price         = (salvage + LTSF until sold + FBA fee) ÷ (1 − referral%)
Break-even discount = LTSF until sold ÷ net proceeds at current price   (n/a if net ≤ 0)
Max combined depth  = max(0, 1 − floor ÷ price)        ← per-child stacking cap
Removal ROI/unit    = LTSF until sold − removal fee
Months to clear     = aged units ÷ monthly velocity
Weekly vel. to cliff= aged units ÷ weeks to next rate step
Age-forward charge  = Σ (units per bracket × next bracket's rate × cu ft)
Scenario recovery   = Σ months (units sold × net proceeds) − ad spend − LTSF at escalating rates − terminal salvage cost
```
- Highest forward net recovery wins, even if negative.
- Break-even discount **> 100%** → no depth pays for the storage → salvage comparison.
- **Floor ≥ price** → no discount authority; removal/salvage wins.
- Stacked promotions on one child never exceed its max combined depth.

### 14.4 Archetypes (classify first — misclassification is the costliest error) [LTSF]
| Archetype | Signals | Levers | Never |
|---|---|---|---|
| **A — Fixable demand** | Peers at the same price/rating sell far more; CTR/CVR below category; stock aged pre-launch | Listing repair (**48-hour SLA**); competitor keyword replication; break-even PPC after CVR recovers | Lead with a deep discount (40% off → 6 sales instead of 4) |
| **B — Variation overstock** | Parent healthy; specific colours/sizes hold the aged units | **Child-scoped only**: tailored promos, child coupons, targeting on non-preferred variations, virtual bundles | Parent price cut or family discount (scope violation) |
| **C — Structurally dead** | No organic traction for **6+ months** of genuine effort; return-defect signal; fixes already tested | Clear at floor now, or terminal | More experiments — decide within **7 days** |
| **D — Aged but healthy** | Sells, margin holds; batch aged via stock-out, season or overbuy | Velocity at/near break-even; PPC up on proven syntaxes; deals before the next bracket | Remove profitable units |
Parent B with C children → say so. C on a new launch = product-market-fit failure → strategic review (exit / redesign / reposition), not an LTSF problem. Before accepting "tested and failed", confirm the SKU ever had **dedicated** spend (5 SKUs were nearly liquidated on portfolio-wide evidence).

### 14.5 Risk tiers (first match, top down)
| Tier | Trigger | Cadence | Standing action |
|---|---|---|---|
| **CRITICAL** | Any units 366+ d, or product LTSF > **$5,000/month** | 2×/week | Removal, liquidation or deep discount within **48 h** |
| **RED** | Any units 271–365 d, **or** LTSF/unit > net proceeds/unit, **or months to clear > 6**, or velocity falling despite a boost | Weekly minimum | Execute, not plan; **freeze POs** on the SKU |
| **YELLOW** | Months to clear > 3 (units 181–270 d), or a large batch reaching 181 d within 60 days | Weekly | PPC velocity boost live; outlet deal submitted; break-even discount computed |
| **GREEN** | No aged units, or clears within 3 months | Weekly | Track; start velocity work if a batch nears 181 d |
Resolution note: the dossier text and its script differ. This framework uses the **union**: "months to clear > 6" is a RED trigger (script), and YELLOW starts at > 3 months (script) — the text's "2–6 months" lower bound overlapped GREEN. "Large batch" size: Owner decision — ask. [LTSF]
Escalations: product > $5k/month → executive review within 48 h. Portfolio > $25k/month two consecutive months → portfolio review + inbound freeze evaluation. Run-rate ÷ trailing-year charge > ~**1.5×** → the aged pool is forming faster than it clears → raise urgency. [LTSF]

### 14.6 Routing thresholds (precedence top down) [LTSF]
| # | Condition | Route |
|---|---|---|
| 1 | Units 366+ d and velocity < 2/month | REMOVAL — full stop |
| 2 | Units 271–365 d and velocity < 5/month | REMOVAL likely cheapest |
| 3 | Floor ≥ price | SALVAGE comparison — no discount authority |
| 4 | Break-even discount not computable | REVIEW — insufficient data |
| 5 | Break-even discount > 100% | SALVAGE comparison — no depth pays |
| 6 | Break-even discount > 40% | SALVAGE comparison — deep discount vs removal vs liquidation, cheapest total path |
| 7 | Break-even discount 20–40% | OUTLET deal at the computed depth |
| 8 | Break-even discount < 20% | COUPON / price drop at the computed depth |
Also: net margin after LTSF > 0 → keep selling, velocity focus; < 0 → floor discount or terminal **this week**. 100+ units at 456+ d → urgent removal/liquidation. Outlet unaccepted near the cliff → act now. Terminal calls belong to Brand Management + Supply Chain: present the comparison and a recommendation, never "settled" unless the Step-0 charge reconciliation passed.

### 14.7 Clearable vs structural split [LTSF]
- **Clearable** = best-case velocity (routing + max in-cap depth, basis-tagged) × weeks to the relevant cliff (monthly velocity ÷ 4.33 × weeks).
- **Structural** = max(aged − clearable, 0).
- Clearable → ladder (§14.10). Structural → salvage comparison **now** (paying bracket rates on units no realistic velocity can clear is waste).
- Removed structural stock on a continuing product → store for re-send or other channels; **never dispose of sellable stock** unless the side-by-side shows both alternatives net worse. Re-split every cycle.

### 14.8 Lever families [LTSF]
1. **Listing repair** — image, A+, title/bullets, offer, reviews, Vine.
2. **PPC velocity** — break-even scaling, competitor keyword replication, discovery routed to the aged child, targeting on non-preferred variations, bid/budget up on proven syntaxes, display retargeting, Sponsored Brands → store clearance page.
3. **Price / promotion** — coupons, Prime-exclusive, price drop, outlet, lightning/7-day deals, tailored promotions, social codes, virtual bundles, BOGO, Subscribe & Save, creator connections.
4. **Cross-channel** — TikTok Shop, DTC, FBM via 3PL, marketplace transfer.
5. **Terminal** — removal, liquidation, donation, disposal.
A single-family plan is incomplete. On variation overstock, price levers are scoped to the aged children only; a parent-wide lever is a scope violation, reported even if it worked.

### 14.9 Prediction rule [LTSF]
Every lever launches with a predicted uplift and a basis tag: **HIST** (measured response of this SKU or a close sibling to the same lever), **MARKET** (competitor-benchmarked ceiling), **TEST** (pre-registered). Read at **day 7** (and day 14). Actual **< 50% of prediction → replace, not extend** (verdicts: continue / replace / pending). Untagged uplift = blank and blocks scenario ranking. Two levers in the same window = confounded read.

### 14.10 Escalation ladder [LTSF]
Each aged SKU gets rungs with a velocity target and an expiry date anchored to its cliff calendar; a missed target fires the next rung automatically.
| Rung | Action | Target |
|---|---|---|
| 1 | Routing + shallow child-scoped depth; outlet deals submitted | 60% of velocity-to-cliff |
| 2 | Break-even PPC scaling; bundles / hero-as-X promotions | 100% of velocity-to-cliff during promo weeks |
| 3 | Off-anchor codes at clearance depth | Sustained 100% of velocity-to-cliff |
| 4 | Child base-price cut toward the floor, with a written restoration step | 80%+ of clearable units gone |
| 5 | Terminal execution on the remainder per salvage comparison | Zero positive-ROI cliff crossings |
**Skip-forward:** a SKU within **30 days** of its next rate step skips forward regardless of sequence. Depth is bought by the calendar, not by impatience.

### 14.11 Step-0 checks [LTSF]
1. **Charge reconciliation** — rebuild units × cu ft × rate per bracket vs the invoice; should agree within a fraction of a percent. A miss is almost always a per-unit rate somewhere.
2. **Bracket granularity** — request all 8 brackets; a 4-bracket source makes charges approximate (state it).
3. **SKU coverage** — SKUs in the charge file vs SKUs analysed; unrouted units are a stated gap.
4. **Velocity basis** — every haircut/uplift documented (§12).
5. **Untagged multipliers** — treated as blank.
6. **Scope violations** — parent-wide levers on variation overstock reported as findings.
7. **Inbound** — production + transit vs cover and ceiling (§11).
8. **Deployment verification** — what actually went live, before grading any lever.
A failed check is a **finding, not a blocker**: report it prominently, show both scenarios, name the document that would settle it, and continue. Terminal calls stay unsettled until check 1 passes.

### 14.12 PPC on aged stock [SR, B6, PB]
- Clearance/LTSF campaigns are judged on **stock cleared**, not ACoS. [B6 R-N2]
- SKU Green + aged units → PPC up to break-even on forward-cash economics (03 §3.7). Not Green → no push; move to price levers. Never a clearance push while the size's hero is Red. [SR]
- Negative contribution after LTSF → pricing decision (Brand Management), not a bid lever. [SR]
- Exit the clearance posture when aged stock drops below the next surcharge threshold. [SR]
- Deals are the clearance mechanism; PPC supports visibility of an already-scheduled clearance window. [PB]

---

## 15. Anti-patterns [LTSF, INV, WB, B6]

- LTSF per unit; flat-rate projections; no charge reconciliation.
- COGS in a clearance decision; floor set at break-even; deeper discount when break-even discount > 100% or floor ≥ price.
- Discounting Archetype A; parent-wide levers on B; stacking past the child cap; single-family plans; experimenting on C beyond 7 days; removing D stock; disposing sellable stock.
- Uncorrected distorted-window velocity; untagged multipliers; confounded reads; read windows straddling lever changes; grading undeployed actions; condemning SKUs that never had dedicated spend.
- Traffic into Conversion-quadrant syntaxes; stock signature read as relevance loss.
- Auto-derived backup pairs; ignoring backup self-competition; ignoring inbound.
- Cover computed on push pace; switches that change size; ranking on a slow colour; discovery on the hero; routing read from names.
- Pushing Yellow/Red stock; a hold with no re-entry date; zoning from "units > 0".

---

## 16. Open questions for the owner

1. **Velocity driver:** the inventory checkup defaults to planned velocity (Base SV) on a 7-day window; B6 gates on the 30-day actual pace with 7-day as warning. This file gates on the 30-day actual and shows planned beside it. Confirm.
2. **TIGHT vs Red re-point:** the register makes any stock-out before arrival Red (re-point same day), while B6's TIGHT rule (shortfall ≤ 7 days) eases without swapping. This file treats TIGHT as Red with the swap waived. Confirm.
3. **Projected-cover threshold for a push:** plan builder blocks when projected cover drops into Yellow (< 60); workbook builder requires > 21 days through the checkpoint. This file uses the plan builder rule. Confirm.
4. **Cover ceiling** (overstock) for the inbound check, and **"large batch"** size for LTSF YELLOW — no house values.
