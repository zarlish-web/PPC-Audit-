# 03 — Profitability and guardrails

Read in Phases 1–2 (frame the product, economics gate) and Phase 7 (pricing, budgets, spend). Everything that decides *how much money a row may spend* lives here. Inventory gates are in `04-inventory-sku-ltsf.md`; placement mechanics (backward-solve, mix fix, DSTR) in `07-placement-and-bidding.md`.

Source tags: [SR] optimization engine · [PB] plan builder · [DR] decision reasoning · [WB] workbook builder · [PF] placement-first · [QA] quick audit · [LTSF] LTSF dossier · [B6] B6 engagement, Sep 2026.

## Contents
1. Product goal and the goal gate
2. Lifecycle stages
3. Per-SKU economics (margin, break-even ACoS, fallbacks, freshness)
4. Break-even CPC per placement and the conversion basis
5. Ceilings and push price
6. Objective ACoS bands and the layered non-ranking rule
7. CPA ceiling, clicks-to-loss
8. Weekly loss ceiling for ranking pushes
9. Spend limit, margin rule and event exceptions
10. Deal-state vs clean-state economics (event mode)
11. TACoS — monitor and decompose
12. Marginal ACoS unwind rule
13. Human-confirm thresholds
14. Financial guardrail checklist (used by the quality gate)
15. Open questions for the owner

---

## 1. Product goal and the goal gate

**Ask for the goal before any ranking, launch or push decision.** It is an owner setting, not something to infer.

| Goal | Ranking allowance (the 2× ceiling on push terms) | Launch scope for new Exact | Rows priced at | What leads the four-dimension read |
|---|---|---|---|---|
| **Growth / Scale** | Available — Exact ranking rows only, each clearing the 5-property gate (Sized, Dated, Ceilinged, Predicted, Funded; see 06) | Highly + semi-relevant | Push terms up to ceiling; all else ≤ 1× break-even | Rank leads; margin softening tolerated inside the loss ceiling [PB] |
| **Mixed** (ranking + profitability) | Available on Exact → Ranking rows; product targets stay Profitable Conversion at standard ceiling | Highly + semi | Split by campaign objective; TACoS decomposed by tag | Split by campaign tag [PB] |
| **Profit-First** | No new pushes. Rank already won may be protected (HOLD RANK, placement discipline, rank-loss investigation) without the allowance | Highly only, permanently | ≤ 1× break-even everywhere | Margin and revenue lead; rank only to protect won positions [PB] |
| **Clearance / LTSF** | None — all rank considerations nullified, including protection | Highly only | Standard ceiling (1× break-even, forward-cash economics for aged units — §3.7) | Inventory and revenue lead: recovery per unit vs clearance timeline [PB] |
| **Undeclared** | Treat as **Profit-First** for this gate; mark every ranking verdict "pending goal" | Highly only | ≤ 1× break-even | — [PB, SKILL] |

Rules:
1. **Gate order:** product goal → syntax clearance. A syntax in chronic Conversion quadrant (≥ 4 weeks) loses the ranking allowance even under Growth. Both must clear. [PB]
2. The goal **authorises** spend; it never re-tags campaigns. Objectives still come from targeting. [PB]
3. The first time the gate authorises or removes a real ranking allowance on a product, **ask the owner before applying it** (provisional rule); the answer then holds for that product. [PB]
4. For a **Plan** request, no ranking allowance, launch or push is written until the goal is declared or a suggestion is confirmed. For an **Analysis** request, proceed with Profit-First treatment and list "goal undeclared" as a finding. [PB, SKILL]
5. If a code-red TACoS tier is in force (only possible when the owner has set a TACoS target — §11), it freezes all scale before the goal is read. [PB]

### 1.1 Suggesting a goal (when none is declared) [PB]
Run in this order; present the suggestion **with its numbers**; nothing downstream uses it until the owner confirms or overrides.
1. **Confirmed LTSF charge on record → suggest Clearance/LTSF.** Nothing else is weighed. Aged stock *without* a confirmed charge is a separate flag, never a Clearance trigger.
2. Otherwise weigh stage + TACoS position + margin trend together (the same three dimensions read every cycle):
   - **Growth/Scale** — Launch or Ranking-push stage, margin healthy or improving, TACoS well inside its reference band.
   - **Profit-First** — margin thin or declining, TACoS at or near its reference band ceiling, or product in Mature/Harvest.
   - **Mixed** — only when the data really splits by segment (some syntaxes show supported ranking opportunity while product economics call for caution). Never the default for "ambiguous".
3. Write it with evidence, e.g. "Suggesting Profit-First — margin/unit fell from $21.40 to $18.10 month on month, TACoS 11.3% vs a Mature reference band of 4–7%, organic share 58% and flat." A bare label fails.

### 1.2 Four-dimension read (every cycle) [PB]
Rank trend (overall, 14 d, 7 d) · revenue WoW and MoM · margin WoW and MoM · inventory posture. Weighted by goal (table above). Combined outcomes:
- All improving → spend plan as computed.
- Rank up + margin down → Growth: recompute at current margin; Profit-First: margin finding governs.
- Revenue up + inventory Yellow/Red → inventory caps spend regardless of goal (gate, not a weight).
- Rank, revenue and margin all declining → escalate a product-level finding before any mechanical spend change.
- One dimension diverging sharply → named finding.

---

## 2. Lifecycle stages

| Stage | Expected campaign mix | Graduates when | Notes |
|---|---|---|---|
| Launch | Discovery-heavy | Organic sales > ~40–50% of total, sustained (not profitability alone) | Launch floor: routed SKU ≥ 21 days of cover (04) [PB] |
| Ranking push | Exact concentrated on the primary syntax | Rank targets held 2 clean weeks → HOLD RANK, then taper (06) | Push clock = weeks since *this* push began, restarts with a new push [PB] |
| Transition | Push tapering to maintenance | Organic share above target, CVR stable | — |
| Mature / defend | Defensive layer, brand-format coverage, display retargeting, low-budget auto sentinel; no active push | — | — |
| Harvest | Minimum spend, defend won positions | — | — |
| Clearance | Discovery on the clearance variation, break-even PPC on forward cash | Aged stock cleared or terminal decision made | See 04 §LTSF |

Rules:
1. Check the declared stage against evidence (profitability, organic share, review posture, CVR stability). A campaign stack that does not match the stage is a named finding, not something to reconcile silently. [PB]
2. **Demotion trigger:** organic sales share below target 4 consecutive weeks, or ad dependency rising past its declared ceiling → formal review for demotion to Transition. [PB]
3. Stage tags expire on their declared date; renewal needs evidence. Re-entering a ranking posture after stepping back needs a fresh realism check (06 gauntlet). [PB]
4. New-launch stage suppresses campaign turn-off and bidding-strategy changes. [SR]
5. Organic-share targets and dependency ceilings are **Owner decision — ask**; no source sets a default.

---

## 3. Per-SKU economics

### 3.1 Margin per unit — the number every price is built on
| Item | Rule | Tag |
|---|---|---|
| Source | Sellerboard **profit per unit before ads**, per advertised SKU/colour, last 30 days = (net profit + ad spend) ÷ units. Includes product cost, all Amazon fees, refunds, storage | [B6] |
| Price in force | Deal price during a deal (recompute margin at deal price, net of deal fees) | [B6, PB] |
| Granularity | Per advertised variation. **Never** a blended parent, category average or another product's number | [SR, PB, B6] |
| Component build (only when Sellerboard per-SKU profit is unavailable) | CM2 = (ASP − COGS/unit − Amazon fees/unit) ÷ ASP. COGS/unit and fees/unit = totals ÷ **gross units** (units + \|refund count\|). Fees = Sellerboard bundled (referral + FBA + storage + inbound). No returns term. Say which basis was used; never mix the two in one analysis | [SR] |
| AOV per objective | Ranking and Profitable Conversion: advertised SKU. Conquest: the routed-to SKU (never the competitor's price). Discovery: campaign-blended AOV until a child is confirmed | [PB] |

Why per SKU: colours of the same size differ widely. Example (B6): Queen White $19.51/unit vs Queen Olive $12.43/unit; the product blend was $18.81 ($18.18 at deal price), and the engine's $26.60 "profitability" figure put every ceiling ~40% too high — 154 of 180 ranking campaigns were already paying above true break-even at the top.

### 3.2 Break-even ACoS
- **Break-even ACoS = margin/unit ÷ price** (ASP; deal price in a deal). [B6, PB]
- Target ACoS for non-ranking rows = break-even. [B6]
- State break-even ACoS beside CPA-vs-ceiling on every push or cut; if the two disagree, flag it — never resolve silently. [PB]
- Example (B6): 23.8% break-even ACoS; 2× = 47.6%.

### 3.3 Fee-contamination fallback [SR]
If fees ÷ ASP > **55%**, the fee line is contaminated. Replace: fee/unit = **portfolio median fee/ASP × ASP**, median taken from clean SKUs only (≥ **10 units**, 0 < ratio ≤ 55%). Log "verify with Brand Management".

### 3.4 Sanity band and missing data
1. Break-even ACoS outside **5–70%** → flag the SKU; never use silently. [SR]
2. SKU with < 10 units: use the same-size median margin (SKUs with ≥ 10 units and positive margin), never higher than the SKU's own figure. [WB]
3. SKU with no economics at all → **halt pricing for that SKU**. Never fall back to a global default (the engine's silent 19.86% default is a known defect). [SR defect, 13 §3]
4. Negative margin → no click price can be profitable: affordable CPC = 0, leave the bid, no raises, refer to Brand Management (price/COGS/fees). Pull a 60–90-day window before recommending a stop. A negative margin is never "rescued" by a sibling's figure. [PB, WB, SR]

### 3.5 Freshness and change events
| Trigger | Action | Tag |
|---|---|---|
| Margin table > **45 days** old | Stale: blocks every ceiling-referencing verdict until refreshed | [SR, PB] |
| Any price, FBA fee, size-tier, remeasure, packaging, freight or LTSF change | Re-derive margin and ceilings within **48 h** | [PB] |
| Pending dated COGS change | Carry two columns: current-COGS margin (drives all live decisions) and future-COGS margin (context only) | [PB] |
| CVR drop coinciding with a logged price rise | Hold bids; revert the price, or accept it and recompute break-even, ceilings and targets before any verdict resumes | [PB] |
| AOV shift from a variation-mix change | Every ceiling and verdict on the old AOV is void; refresh economics and **re-run** the row (not patch) | [PB] |
| Economics differ > 10% from the value logged when an action was taken | Grade that action PROVISIONAL (no credit/blame) — see 10 | [SR] |
| Sellerboard true-up | Monthly | [PB] |

### 3.6 Re-route rebuild
Every change of advertised SKU (any cause) → rebuild margin, break-even and ceilings from the new SKU in the same write; reset CVR baseline, rank clock and ROS lift. Ceilings priced on a departing SKU are void. [PB, B6]

### 3.7 Aged stock — forward-cash economics
For units already aged or carrying LTSF: COGS is **sunk** and never enters the live decision column. Use forward cash: net proceeds/unit = price × (1 − discount) − referral − FBA fee, compared against salvage value and LTSF until sold. The deal (price/promo) is the clearance lever; PPC supports visibility. Full math, floor price and routing in `04-inventory-sku-ltsf.md`. [PB, LTSF]

---

## 4. Break-even CPC per placement and the conversion basis

**Break-even CPC = margin/unit × conversion rate of the placement being bought** (top of search, rest of search, product pages each separately). [B6, PB, DR]

Conversion basis (register #2) [B6]:
| Own placement clicks (90 d, campaign grain) | CVR used |
|---|---|
| ≥ 50 | Own placement CVR |
| 15–50 | Linear blend: w = (clicks − 15) ÷ 35; CVR = w × own + (1 − w) × size rate |
| < 15 | Size's placement rate for that placement (product rate if the size has none) |

Rules:
1. Placement data is campaign grain; any keyword-level placement split is an estimate — label it. [B6]
2. Exclude the last 7 days from CVR (7-day attribution settles late). [B6]
3. Deal days: separate deal-state CVR (§10); in-deal CVR never raises a clean-state ceiling. [PB]
4. Never set the planning CVR equal to the baseline being judged (circular). Baseline = the product's live CVR per placement each cycle. [PB]
5. Amazon suggested bids / "market price" are **not** inputs to any price. [B6 owner rule, register #18]

Arithmetic example (illustrative): margin $19.51 × TOS CVR 20% = break-even TOS CPC $3.90; ranking ceiling 2 × $3.90 = $7.80.

---

## 5. Ceilings and push price

| Row | Placement | Ceiling (default) | Tag |
|---|---|---|---|
| Ranking push term (goal gate passed, qualified — 06) | Top of search: **TOS price = base × (1 + boost)** | **2 × break-even TOS CPC** | [B6, register #3] |
| Ranking push term | Rest of search | 1 × break-even; lifted to ceiling only after 15+ ROS clicks converting ≥ the campaign's product-page rate, else runs at base | [PB] |
| Ranking push term | Product pages (base only, no modifier) | 1 × break-even PDP CPC | [PB, WB] |
| Ranking term at/beyond target (HOLD RANK) | TOS | Keep current price (≤ push ceiling), no raise; after 2 clean weeks taper ~10%/week to 5–10¢ under the placement's blended CPC (06) | [B6 R-P8, register #26] |
| Ranking campaign, not pushed | All | 1 × break-even. Walk down: 0 TOS clicks in 30 d → straight to BE; with TOS clicks → step down ≤ 50% per step toward BE, restore one step if rank falls > 10 places; price ≤ BE → hold | [B6 R-B1–B3] |
| All non-ranking objectives | Every placement | **≤ 1 × break-even CPC** | [register #3] |
| Conquest (competitor product targets) | Product page | ≤ break-even CPC; watch-CPA = lower of margin × CVR and a price-gap-adjusted figure (state which governs) | [B6, PB] |
| Discovery launch | — | Broad ~60%, Phrase ~80% of the Exact row's break-even price; no placement modifier at launch | [PB] |
| Cold candidate on a thin margin | — | CPC ≤ ~⅓ of margin/unit | [PB] |

Hard bounds on every write: TOS boost ≤ **900%**; base ≥ TOS price ÷ 10; base floor $0.35–0.50 (below it Amazon suppresses eligibility); the $0.50 minimum bid (provisional) loses to any lower ceiling. [B6, WB, SR, PB]

**Push price** (ranking push terms only) [B6, register #4]:
- Push price = break-even TOS CPC × (1 + premium), **capped at the ceiling**.
- Premium = +25% if rank ÷ target ≤ 1.5; else (rank ÷ target − 1) × 50%.
- Example: rank 30, target 10 → ratio 3.0 → premium 100% → push price 2 × BE = the ceiling.

Ceiling rules:
1. **Price above ceiling → cut to ceiling now.** Never deferred, never "owned by a later descent". Applies to raises and holds alike. [B6 R-P5]
2. Row under 15 clicks but over ceiling → formula-only correction to ceiling in one cycle; next cycle check for suppression (clicks collapse → fixed-bid trial, 07). [PB]
3. **Qualification:** a term is pushable only if its ceiling ≥ our current TOS cost per click; otherwise **WAIT** for an owner decision on a time-limited ceiling raise. [B6 R-P1, F25]
4. At ceiling **3 days** without top-3 sponsored position and ≥ 30% TOS impression share → **CHECK OWNER**: raise that term's ceiling for a stated period, or swap the term. [B6 R-P6]
5. TOS CVR below market on 50+ TOS clicks → stop the push, back to break-even. [B6 R-P7]
6. Up-and-down bidding doubles the TOS price the auction may charge: authorised TOS CPC = base × (1 + boost) × 2.0; breach if > ceiling × 1.05 → re-solve base = ceiling ÷ ((1 + boost) × 2.0). [SR]
7. Realised CPC ÷ target price > 1.0 = push-only territory; > 1.5 = unjustifiable, correct this cycle. [SR]
8. No price ever derives from a click requirement; click plans size volume and budget only. [B6 F21]

**Alternatives (owner settings, not defaults):** flat account ranking cap ~$8–9 with per-SKU margin only tightening it [PB, WB]; placement overlay 1.30 × break-even with push at 0.75 × [PF]; margin × CVR on every row including ranking (1×) [DR]. Record which the owner chose.

---

## 6. Objective ACoS bands and the layered non-ranking rule

### 6.1 Objective bands (reference — they report, break-even triggers) [SR]
| Objective | Band (max ACoS) | Note |
|---|---|---|
| Ranking / re-ranking | 50–80% | Reference only; ranking is judged on rank vs loss ceiling, never weekly ACoS |
| Market Share | 25–50% | Only when declared |
| Discovery | 15–30% | Core bid capped at break-even |
| Profitable Conversion | 15–25% | ≤ break-even |
| Defensive | 10–15% | |
| Brand Defensive | 5–10% | |
| Competitor / Conquest ASIN | 10–15% | |
| LTSF clearance | up to 50% | See open question 2 |
| Unknown | 25% | |

- Target ACoS = **50% of break-even**; Max acceptable = **75% of break-even** (house reporting thresholds). [SR, QA]
- RPC bid math: RPC = sales ÷ clicks; RPC ceiling = RPC × break-even ACoS; suggested bid = RPC × band max; **target bid = min(suggested, RPC × break-even)**. [SR]
- A band breach alone never cuts a row; only break-even does. [B6 F31]

### 6.2 Layered non-ranking rule (register #16) — first match wins
| # | Condition (non-ranking row) | Decision | Tag |
|---|---|---|---|
| 1 | < 15 clicks (30 d) | MONITOR — no change | [B6 E3] |
| 2 | ACoS > **2 × break-even** on ≥ 30 clicks (90 d) | BLOCK / stop (discovery: negative exact; product target: pause / negative ASIN); in the term's exact owner: REDUCE | [B6 R-K3, R-X5] |
| 3 | ACoS > break-even on **both** 30 and 90 days, ≥ 15 clicks | REDUCE: base × BE/ACoS, i.e. cut −(1 − BE ÷ ACoS), **max −30% of base per step** | [B6 R-N1] |
| 4 | ACoS > break-even on 30 d but inside on 90 d | MONITOR (watch) | [B6] |
| 5 | ACoS ≤ **50% of break-even** with orders | SCALE-eligible: raise ≤ +25%/cycle, never above the 1× ceiling | [register #16, #5] |
| 6 | Otherwise | KEEP | — |

Magnitude inside rule 5 (provisional — confirm with owner before first use): CONFIRMED 15+ clicks / 2+ orders / CPA ≤ ~70% of ceiling → hold; STRONG 30+ / 3+ / ≤ ~60% → up to +10%; PROVEN 50+ / 5+ / ≤ ~50% → up to +15%. [PB]

Exceptions: LTSF/liquidation campaigns are not cut on ACoS — judged on stock cleared [B6 R-N2]. Brand Defensive judged on ACoS ≤ break-even plus share held [B6 R-N3, PB]. Deal days: no verdicts; bleed stops still run (§10).

---

## 7. CPA ceiling and clicks-to-loss

- **CPA = CPC ÷ CVR.** [PB, B6]
- **CPA ceiling:** non-ranking rows ≤ margin/unit (= break-even); ranking push at ceiling ≤ 2 × margin/unit (bounded loss per push order, still below the order value). Applies to Profitable Conversion, Defensive, Discovery, Conquest — **not** to Ranking inside its push window. [B6 R-F3, PB]
- CPA > 8 × ceiling → a single cut up to 50% is allowed. [PB]
- **Clicks-to-loss = margin/unit ÷ CPC** — the clicks per order at which a row breaks even. Example: $10 margin ÷ $4 CPC = 2.5 clicks per order. A row whose clicks-per-order (1 ÷ CVR) exceeds this loses money on every order. [PB]
- Zero orders on a thin sample = unknown, not zero CVR (see 06 zero-order rule: ≥ 20 clicks). [PB, B6]

---

## 8. Weekly loss ceiling for ranking pushes

- **Weekly loss ceiling = (push ACoS − break-even ACoS) × projected ad sales at the required spend**; never less than one day's spend; basis stated on the row. [PB, WB]
- Hitting it = **CHECK OWNER** flag, not an automatic stop. [PB]
- Margin rule check (weekly): if product margin after ads falls below the owner's margin rule, cut pushes **from the bottom of the funded list** (funding order = revenue potential at target rank ÷ cost to close the gap). [B6 R-F6, PB]
- Example: push ACoS 38%, break-even 23.8%, projected ad sales $6,000/wk → loss ceiling (0.38 − 0.238) × $6,000 = $852/wk.

---

## 9. Spend limit, margin rule and event exceptions

| Rule | Detail | Tag |
|---|---|---|
| Spend limit | Owner-set daily/weekly $ for the product. **Refuse to size any push without one** | [B6 F03] |
| Margin rule | Owner-set, e.g. keep product margin after ads ≥ 10%. Margin after ads = (profit before ads − ad spend) ÷ sales | [B6] |
| Check | Push budgets + expected other spend ≤ limit. If over → scale push budgets down, cutting from the bottom of the funded list | [B6 R-F5, E19] |
| Spend basis | Product basis: campaign rows can include other products — product spend = row spend × (product tile ÷ row total). Shared multi-product campaigns are excluded from this product's price automation | [B6] |
| Not a TACoS rung | Never size spend on a TACoS "rung" or envelope unless the owner has set a TACoS target | [B6 F24] |
| Budgets | Push budget = plan clicks × price (+ expected product-page spend); ≥ required × 1.05, rounded up; budgets load **with** their price rows or not at all | [B6, PF, F14] |
| Minimums / referrals | Budget < $10/day → raise to $10; budget > $500/day → refer for review; budget moves > $50/day → human confirm | [SR, PB] |
| Event exception | Must be **explicit, time-boxed (dates), with the margin it produces stated**, approved before the event, never retroactively | [B6, PB] |

Example (B6): spend limit **$1,300/day on 29–30 Sep** — a stated two-day exception to the 10% margin rule, producing **~7% margin after ads** for those deal days; from 1 Oct the limit was reset by the post-deal audit.

---

## 10. Deal-state vs clean-state economics (event mode)

Deals distort price, margin, CVR and AOV at once (register #27). Rules:
1. **Compute deal-state margin, break-even and ceiling before the event** from deal price, net of deal fees (fixed + % of deal sales, stated separately from referral/FBA). A discount cuts contribution by its full depth, so the ceiling falls faster than the discount %. [PB]
2. Keep deal-state and clean-state **separately**: margin, CVR baseline, rank arc, sufficiency count. Never blend. The clean arc governs verdicts. [PB]
3. **No verdicts on deal data**: no ACoS/CVR judgement on a window with > 2 deal days; no new campaigns, folds or structural changes on deal days. [B6 E1, F01]
4. **Bleed stops still run** mid-deal (negations, placement leak cuts); a real loss (ACoS > deal-state break-even) is cut even mid-deal; gradual target-chasing cuts wait. [SR]
5. In-deal CVR never justifies a bid above the deal-state ceiling. [PB]
6. Deals **amplify an already-decided, gated push; they never originate one.** [PB]
7. Pre-event: set budget caps in advance; remove dayparting boosts; stage the bid plan against **max-sales-day** days of cover (04). Live: check pacing the same day against the event projection. [PB]
8. Post-event: exclude event days from trend reads for **2 weeks**; taper event bids over **3–5 days**; allow the 7-day attribution settle before any read. Floors/ceilings return to pre-event values unless the event produced durable evidence (e.g. sustained higher rank). [SR, PB, B6]
9. Deal report: sales, units, glance views, deal-page CVR, contribution at deal-state margin net of deal fees, net contribution before ads. [PB]
10. Pacing deviation > ~25% from the product's day-of-week curve → flag the same day. [PB]
11. Deployment sequencing: ceiling-math structural fixes deploy now; cut batches and launches that need clean-week CVR wait for the window to close. [PB]

---

## 11. TACoS — monitor and decompose (owner has not set targets)

**Default: TACoS is reported and explained, never a target, gate or bid input** (register #17). [B6 owner rule]

- TACoS = ad spend ÷ total sales (refund-net). [SR]
- Decompose every movement: TACoS = ACoS × (ad sales ÷ total sales). Report which moved — ad efficiency, paid share of sales (organic change), or both — and split by objective (push vs non-push) and by event days. [PB]
- A high TACoS is legitimate only alongside a gated push, a Green SKU and real rank movement. [PB]
- Never an across-the-board % cut to fix TACoS; any response runs the per-row decision order. [PB]

**Reference only — apply only if the owner sets a TACoS target:**
| Item | Values | Tag |
|---|---|---|
| Stage bands | Launch ≤ 25% (another source says 35–45%; 25% if asked), Ranking push 12–15%, Transition 8–12%, Mature 4–7%, Harvest ≤ 4% | [PB] |
| By weeks since current push | 1–6: ≤ 1.5 × BE ACoS · 7–12: < BE · 13–25: < 0.75 × BE · 26+: < 0.5 × BE | [PB] |
| Envelope | Weekly spend = target TACoS × projected weekly revenue; one pre-approved event week may run +50% | [PB] |
| Tiers (actual ÷ band) | Within ≤ 1.2× · Elevated 1.2–1.5× · Breach 1.5–2× (freeze new scale) · Code-red > 2× or > 1.5× for 2 weeks (freeze scale, per-row review within 48 h, daily cadence; exit after 2 clean weeks) | [PB] |
| Other house refs | Phase-4 TACoS ceiling 12%; organic sales floor 60% | [QA] |
| Routing use | TACoS ≤ 50% BE + broad-type row + orders > 0 + ACoS > BE + no aged/deal → hold bid and negate | [SR] — not applied by default |

---

## 12. Marginal ACoS unwind rule

After any scale step (bid, boost or budget raise), read the **step**, not the new blend:
- **Marginal ACoS = Δ spend ÷ Δ ad sales** across the two periods the step spans (marginal CPC = Δ spend ÷ Δ clicks). [PB, SR]
- Marginal ACoS > **1.5 ×** the running average → saturation: **freeze** further raises; record the prior rung (price and date). [SR]
- Marginal ACoS > **2 ×** the running blended ACoS → **unwind** the step to the prior rung, however acceptable the new blend looks. [PB]
- Judge only executed steps with ≥ 15 fresh clicks and no deal days in either period (10).

---

## 13. Human-confirm thresholds

Flagged rows are still written in full; they are marked for the reviewer, with the trade-off in the reviewer's units ("holds ~$180/wk of saving to keep ~66 orders/wk at $5.60 per order"). [PB]

| Trigger | Tag |
|---|---|
| Action on a keyword at ≥ 500 search volume | [PB] (WB change-review uses ≥ 250 — open question 3) |
| Any gate failure on the row (inventory, provenance, budget truncation, other) | [PB] |
| Structural change: new campaign, routing/colour switch, match-type change, bidding-strategy change | [PB, B6 E8] |
| Bid move > 25% of current | [PB] |
| Budget move > $50/day; budget > $500/day | [PB, SR] |
| Spend envelope/limit change > 20% | [PB] |
| Ceiling raise for a named term (at ceiling 3 days without holding the top) | [B6 R-P6] |
| Weekly loss ceiling reached | [PB] |
| Provisional rule used for the first time on a product (goal gate, Defensive/Conquest allowances, harvest, sufficiency exit, graded push tiers, $0.50 floor) | [PB] |
| Negative or out-of-band (5–70%) break-even; fee contamination fallback used | [SR] |
| Terminal inventory call (removal, liquidation, disposal) | [LTSF] |

---

## 14. Financial guardrail checklist (quality gate — every item must return 0)

1. Any row priced from a blended parent, category, global default or another product's margin.
2. Any row whose margin is > 45 days old, or predates a logged price/fee/packaging change, used for a ceiling verdict.
3. Any break-even outside 5–70% or negative, used without a flag.
4. Any ranking-push TOS price > 2 × break-even TOS CPC (or the owner's chosen alternative).
5. Any non-ranking price > 1 × break-even CPC at any placement.
6. Any over-ceiling price left in place ("deferred").
7. Any ranking allowance on a product whose goal is not Growth or Mixed (or undeclared and unconfirmed), or on a syntax in chronic Conversion.
8. Any push where ceiling < current TOS cost per click (should be WAIT).
9. Any raise > +30%/day on a push, > +25%/cycle elsewhere; any gradual cut > 15%/cycle, non-ranking ACoS cut > 30% of base, or base cut > 50% per step (13 register #5).
10. Any boost > 900% or base < TOS price ÷ 10.
11. Any price derived from a click requirement or from Amazon suggested bids.
12. Push budgets + expected other spend > the stated spend limit, with no dated, margin-stated exception.
13. Any spend sized on a TACoS target the owner has not set.
14. Any verdict computed on a window with > 2 deal days, or any launch/fold on a deal day.
15. Any in-deal CVR used to lift a price above the deal-state ceiling.
16. Any weekly loss ceiling missing its basis on a push row.
17. Any executed scale step with marginal ACoS > 2 × blend left in place.
18. Any flagged human-confirm row without its trade-off stated.
19. Any budget row loaded without its price row, or vice versa.
20. Break-even ACoS not stated beside CPA-vs-ceiling on a push or cut row.

---

## 15. Open questions for the owner

1. **Marginal-step thresholds:** SR freezes at marginal ACoS > 1.5 × average; PB unwinds at > 2 × blend. This file layers them (1.5× freeze, 2× unwind). Confirm or pick one.
2. **LTSF-clearance ceiling:** SR carries a band "up to 50% ACoS", an alternative "~18% product TACoS", and a separate rule "aggressive to break-even (RPC × BE)". This file uses 1 × break-even on forward-cash economics and lists the 50% band as reference. Confirm.
3. **Search-volume trigger for human review:** PB ≥ 500, WB change-review ≥ 250. This file uses 500 for mandatory confirm. Confirm, or lower to 250.
4. **Defensive above-ceiling allowance** (PB: only with verified competitor presence on the brand term, withdrawn after 2 reads without it): not adopted by default (brand rows held to ≤ 1 × break-even). Adopt?
5. Organic-share graduation target and ad-dependency ceiling for demotion: no house default — set per product.
