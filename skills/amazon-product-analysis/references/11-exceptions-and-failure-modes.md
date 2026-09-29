# 11 — Exceptions, BLOCK conditions and the failure register

Read **before finalising any decision**. Part A lists the conditions under which no automated change is made (the row is held, blocked, referred or asked about instead). Part B is the consolidated register of every known failure mode from the source skills and the B6 engagement, with a test for each. Run Part B's tests as part of the quality gate (reference 12).

Source tags: see reference 13. "(seen: B6 Fnn)" = the failure actually occurred in the B6 engine run of 28–29 Sep 2026. Examples marked "Ex (B6)" are illustrations from that case, not rules.

## Contents
- Part A — Exceptions and BLOCK conditions
  - A.1 Data, scope and intake
  - A.2 Events and deals
  - A.3 Goal, economics and pricing
  - A.4 Inventory, variations and LTSF
  - A.5 Structure and keywords
  - A.6 Quality, rank and market
  - A.7 Process, approval and the silent-hold list
- Part B — Failure register
  - B.1 Data and intake
  - B.2 Economics
  - B.3 Inventory and routing
  - B.4 Keywords and negation
  - B.5 Campaigns and objectives
  - B.6 Placement and pricing
  - B.7 Ranking
  - B.8 Competitors
  - B.9 Events and deals
  - B.10 Writing and deliverables
  - B.11 Process and engineering
- Open questions for the owner

---

# Part A — Exceptions and BLOCK conditions

**How to use:** check every row against this list after the master decision order produces a decision. If a condition fires, write the "instead" action, the decider, and the dated re-check. An exception is a decision, not a skipped row — it still gets a trail. Who decides: **Analyst** (the person running this skill), **Owner** (product owner), **Approver** (signs off uploads), **Brand Mgmt**, **Supply Chain**.

## A.1 Data, scope and intake

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-01 | A required input is missing and not confirmed absent | No partial start. Ask once, in one batch; record a named gap and the decisions it blocks [PB, QA, WB] | Analyst → Owner | — |
| A-02 | Data validity: CVR/ACoS with 0 orders, CTR with 0 clicks/impressions, values conflicting across bulk / console / Sellerboard / SQP | Quarantine: no recommendation; same-day refresh task [PB, SR, WB] | Analyst | — |
| A-03 | Source mismatch that moves money: DOH differs > 0.5 day or LTSF > $0.02 from source; target CTR/CVR drift > 2% on > 10% of rows; SKU not matched exactly (incl. colour) | Halt the run ("accuracy gate failed"); unmatched SKUs flagged, never filled [SR] | Analyst | — |
| A-04 | Advertised SKU has no economics; break-even outside 5–70%; fee ÷ price > 55% | Halt that SKU (never a default break-even); flag; contaminated fees → portfolio median fee ratio from clean SKUs (≥ 10 units), "verify with Brand Mgmt" [SR] | Analyst → Brand Mgmt | — |
| A-05 | Economics stale: margin > 45 days old, or any price / fee / packaging / LTSF change | Ceiling-based verdicts blocked; re-derive within 48 h; grades PROVISIONAL [SR, PB] | Analyst | — |
| A-06 | Missing state: campaign has no targets/bids in the audit, or isn't in the product's list | Confirm in the console; give break-even for reference only [B6 E7] | Analyst | Ex (B6): 29 campaigns; 6 found spending but missing from the list |
| A-07 | Read window ends inside the attribution period | Sales/orders read low; compare settled windows only [B6 E2] | Analyst | Every read |
| A-08 | Thin data: < 15 clicks (product targets < 11) | No change; formula-only correction allowed if over ceiling; converting rows are exempt [B6 E3, PB, SR] | Analyst | Ex (B6): 94 campaigns, 430 search terms |
| A-09 | Rank history < 1 month (or only stockout/re-route stretches) | OUT OF SCOPE for a ranking verdict; say "efficiency decision inside a ranking campaign" [PB, DR] | Analyst | — |
| A-10 | Budget truncation: in-budget < 70% of the day | No bid verdict; budget first. 0% in-budget with $0 spend = missing data, not truncation [PB] | Analyst | — |
| A-11 | No SQP targets; no impression-share data | Four-quadrant does not run ("no targets"); CTR root cause "undetermined" — no CTR-driven bid change [SR] | Analyst | — |
| A-12 | SKU provenance: a different SKU served all or part of the window | Correct price now if over ceiling; read only the post-change part if ≥ 15 clicks, else formula-only; rebuild economics, reset CVR baseline and rank clock [PB] | Analyst | — |
| A-13 | Shared campaign advertising other products | No colour or price automation from this product; review in its own product's audit [B6 E13] | Analyst | Ex (B6): DBS4 auto; B4 LTSF; LTSF multi-SKU |
| A-14 | Sponsored Brands / video / Display | Outside automated pricing; reported "not decided", never silently skipped; tests are hand-built with their own budget line and break-even bids [B6 E12, SR, B6 R-CI10] | Owner | Ex (B6): 33 campaigns; SB/video test approved, $85/day × 14 days |

## A.2 Events and deals

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-15 | Date inside a deal/event | No new campaigns, folds or structural changes; no ACoS/CVR verdicts on event data; pricing only per the push plan and cuts; bleed stops and over-ceiling cuts still run [B6 E1, SR] | Analyst | Ex (B6): 17 builds and 2 folds held on 29–30 Sep |
| A-16 | Event ahead with no deal-state economics | Compute the deal-state margin and ceiling (net of deal fees) before the event; in-deal CVR never justifies a bid above it [PB] | Analyst | Ex (B6): margin $18.81 → $18.18 at deal price |
| A-17 | Deal would originate a push; seasonal index falling | Deals amplify an already-gated push, never start one; falling index → deny new pushes, pre-emptive tapers [PB] | Owner | — |
| A-18 | Event spend above the normal limit | Only as a pre-approved, dated exception with its margin stated (≤ +50% one event week); never retroactive [PB, B6 R-F5] | Owner | Ex (B6): $1,300/day on 29–30 Sep |
| A-19 | Event closed | Taper event bids over 3–5 days (no cliff); 2-week guard on trend reads [SR, PB] | Analyst | — |

## A.3 Goal, economics and pricing

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-20 | Product goal undeclared | Hard stop for a plan; the ranking gate treats it as Profit-First; a suggested goal needs confirmation [PB] | Owner | — |
| A-21 | Goal is Profit-First or Clearance | Profit-First: no new push, protect won rank only. Clearance: no rank considerations, every row at the clearance ceiling (1 × break-even on forward-cash economics, register #43) [PB] | Owner | — |
| A-22 | Ceiling below our own top-of-search cost per click | WAIT; owner may raise that term's ceiling for a set time [B6 R-P1] | Owner | Ex (B6): "bamboo sheets king size" waiting |
| A-23 | 3 days at ceiling without top-3 sponsored and ≥ 30% TOS share | Owner: time-boxed ceiling raise, or swap the term [B6 E5] | Owner | Ex (B6): "bamboo sheets" |
| A-24 | Boost at 900% and target price unreachable | Review; raise base only to price ÷ (1 + boost), boost set in the same write [B6 E16] | Analyst | Ex (B6): Bamboo Sheets King Size |
| A-25 | Step too big: push raise > +30%/day, other raise > +25%/cycle, or base cut > 50% in one step (over-ceiling cuts go straight to the ceiling, register #5) | BLOCK; split into dated steps [B6 E17] | Analyst | Ex (B6): 12 "dose" rows |
| A-26 | Expected total spend > the limit | Scale push budgets; cut from the bottom of the funded list [B6 E19] | Analyst | Ex (B6): push budgets scaled to 45% on the three biggest |
| A-27 | Margin ≤ 0 on the advertised SKU; affordable CPC = 0 | Flag and refer pricing to Brand Mgmt (not a bid problem); leave the bid, flag [SR, PB] | Brand Mgmt | — |
| A-28 | Authorised TOS price (base × (1 + boost) × 2 under up-and-down) > ceiling × 1.05 | Referral with the exact correction; strategy changes are human-only [SR] | Owner | — |
| A-29 | Realised CPC > 1.5 × governing ceiling | State "unjustifiable"; cut the price to the ceiling this run. Above 1 × break-even CPC only on a sized push, up to its 2 × ceiling [SR, register #3] | Analyst | — |
| A-30 | Weekly loss ceiling reached on a push | Human flag, not auto-stop [PB] | Owner | — |
| A-31 | TACoS breach (only where the owner set a target): 1.5–2× band, or > 2× / > 1.5× two weeks | Breach → freeze new scale. Code-red → per-row review within 48 h, daily cadence; never a blanket % cut [PB] | Owner | — |
| A-32 | Budget > $500/day; budget change > $50/day | High-budget review; approval [SR, PB] | Approver | — |
| A-33 | Campaign ACoS and TOS ACoS both over the turn-off level on ≥ 15 clicks (Ranking 100%, Market Share 50%, Discovery 60%, Profitable Conversion 50%, Defensive/PAT 30%) | "Consider turning off — refer"; never auto-off; suppressed at New Launch [SR] | Owner | — |
| A-34 | Conversion deficit (≥ 40 clicks, CVR below target, exact/phrase) | No bid-up; refer listing/offer; bid −15% (hold during a deal) [SR] | Brand Mgmt | — |

## A.4 Inventory, variations and LTSF

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-35 | Hero available < 7 days, 0, or cover < days to arrival by > 7 days | BLOCK push; ranking ads to the backup colour, same size; gap ≤ 7 days = TIGHT: ease, don't swap [B6 E14, R-I1–I5] | Analyst | Ex (B6): Twin — White at 0, Sage Green serves |
| A-36 | Red zone (< 21 days, or stock-out before inbound) | Taper to defence; re-point same day to the next viable child; no raise. Deal + Red → hold + stock-out watch [PB, SR] | Analyst | — |
| A-37 | Yellow zone (21–59 days) | No new push, no raises; hold spend; dated re-entry plan [PB] | Analyst | — |
| A-38 | Every child Red; or a push drives projected cover out of Green | Escalate as supply problem; register entry naming SKU, date it leaves Green and the push causing it [PB] | Supply Chain | — |
| A-39 | Any change of advertised child | By hand (switches don't upload); confirm size unchanged [B6 E8] | Analyst | Ex (B6): 42 switches |
| A-40 | Switch that changes size | BLOCK, except correcting a wrong size [B6 E9] | Analyst | Ex (B6): one fix, Cal King campaign on King White → Cal King White |
| A-41 | Colour with < 7 days of cover | Never add to an ad or switch to it [B6 R-C5] | Analyst | — |
| A-42 | On backup and preferred SKU back above 21 days; backup pairs not supplied | Transition-back is a suggestion, never an auto-swap; backups pasted by the user, never derived [SR, INV] | Owner | — |
| A-43 | Clearance push with the hero size Red, or LTSF SKU not Green | No clearance push [SR] | Analyst | — |
| A-44 | LTSF terminal call (removal, liquidation, disposal, donation, deep discount; floor ≥ price; break-even discount > 100%) | Present salvage comparison + recommendation; not "settled" unless charge reconciliation passed; never dispose sellable stock unless both alternatives are net worse [LTSF] | Brand Mgmt + Supply Chain | — |
| A-45 | LTSF critical: 366+ days or product charge > $5,000/mo; portfolio > $25,000/mo two months | Exec review within 48 h; portfolio review + inbound-freeze evaluation; Red tier freezes POs [LTSF] | Brand Mgmt + Supply Chain | — |
| A-46 | Structurally dead SKU (no traction 6+ months, fixes tested) | Decide within 7 days; on a new launch → strategic review (exit / redesign / reposition) [LTSF] | Brand Mgmt | — |
| A-47 | "Tested and failed" SKU that never had dedicated spend | Not condemned; give it a test first [LTSF] | Analyst | — |
| A-48 | Calendar-marked peak week vs aged-stock economics | Peak availability governs [PB] | Owner | — |

## A.5 Structure and keywords

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-49 | Campaign or every keyword paused | No price change; RESTART decision instead [B6 E6] | Analyst | Ex (B6): 28 campaigns |
| A-50 | Keeper sits in a paused campaign; dormant singleton | Flag the campaign edit needed; ask before enabling singletons [LP] | Owner | — |
| A-51 | New campaign for a term that already has an exact (live or paused, close variants) | BLOCK; restart/reuse [B6 E11] | Analyst | Ex (B6): build 2035 |
| A-52 | Same term live in > 1 instance of one match type | DEDUPLICATE: coexistence test, else owner by rate; losers withheld (paused), nothing else changed [register #13] | Analyst | — |
| A-53 | Brand negatives before the receiving brand exacts are defensive, on the hero and funded | BLOCK the negatives [B6 E10] | Analyst | Ex (B6): row 2142 |
| A-54 | Ranking tag on a colour / competitor / Spanish / misspelled term | BLOCK the tag; Profitable Conversion [B6 E18, register #36] | Analyst | Ex (B6): 12 retags |
| A-55 | Exact and broad in one campaign | Ranking + structural flag; fix (pause broad, keep exact) needs confirmation [OC, PB] | Owner | — |
| A-56 | Rank credit out of scope: auto + broad > ~40% of the term's clicks, or no live exact | No ranking verdict; same-day exact build + steering negatives [PB] | Analyst | — |
| A-57 | Negation candidate is brand, an exact row, an exact ranking term, relevant but non-converting, or < 5 clicks | Brand/ranking exact: never. Exact rows: manual review. Relevant non-converter: fix queue. < 5 clicks: manual review [STR, PB] | Analyst | — |
| A-58 | Term not indexed, or ranking term backend-only | No spend; indexing / listing task [PB] | Brand Mgmt | — |
| A-59 | Category / keyword-group targets | Not bulk-changeable — console only [CB] | Analyst | — |
| A-60 | Competitor ASIN not mapped to a brand | No SCALE until mapped [B6 E20] | Analyst | Ex (B6): 10 ASIN targets with reads |
| A-61 | New Launch stage | No turn-off, no strategy change [SR] | Owner | — |

## A.6 Quality, rank and market

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-62 | Term lost > 10 places in 30 days while getting clicks | Freeze price moves; find the cause (colour, listing, keyword state, competitor) first [B6 E4] | Analyst | Ex (B6): 4 campaigns + "bamboo sheets queen" |
| A-63 | SQP: our CTR or CVR below market on ≥ 30 clicks | WAIT: no push until the listing is checked [B6 E15] | Brand Mgmt | Ex (B6): "bamboo sheets king size", "bamboo sheets king" |
| A-64 | Rank lost > 10 despite delivery | Never a bid change; own listing first → competitor wins 2 of price/rating/reviews → isolated vs category-wide; no cause → ask [PB] | Analyst → Owner | — |
| A-65 | Syntax in Conversion or Both-failing quadrant | No rank push; fix offer; ≥ 4 weeks = chronic → bids frozen at maintenance [PB, QA] | Brand Mgmt | — |
| A-66 | Branded CVR collapse | Listing check first (suppression, buy box, review score, variation break) [PB] | Brand Mgmt | — |
| A-67 | CVR drop coincides with a logged price rise; AOV shift from variation mix | Hold bids; revert price or recompute economics; void and re-run affected verdicts [PB] | Owner | — |
| A-68 | Competitive shock (CVR ≥ benchmark, rank falling, no own event); rival price cut > 15%, new discount, traffic > +50% | Investigate before any bid (new entrant, deal, price cut); hold our price 3 days after a rival move; only then one ladder step inside ceiling, re-read in 1 week; over-ceiling cuts still apply [PB, B6 R-CI11] | Analyst | Ex (B6): KRIMANO +123% traffic; Pure Bamboo 19% off |
| A-69 | Stretch target (only aspirational rivals at/above target) 14 days at ceiling, no rival passed | Owner decision [B6 R-CI2] | Owner | Ex (B6): "bamboo sheets" target #9 held only by two leaders |

## A.7 Process, approval and the silent-hold list

| # | Condition | What to do instead | Who decides | Example |
|---|---|---|---|---|
| A-70 | **Silent-hold list (exhaustive):** both quality gates fail; CTR passes and CVR fails; zero delivery; budget truncation; plan exceeds campaign capacity | Hold without asking; route CTR-pass/CVR-fail to Brand Mgmt; escalate capacity. **Any other HOLD → ask first and log the answer** [PB, DR] | Analyst | — |
| A-71 | Human-confirm thresholds: search volume ≥ 500; any gate failure; structural change (campaign, routing, match type, strategy); bid move > 25% outside an approved push plan (the plan covers its own +30%/day steps); budget move > $50/day [register #41, #54] | Change Review Sheet row with the trade-off in reviewer units [PB, WB] | Approver | — |
| A-72 | A provisional rule would drive a real decision for the first time on this product (goal-gate mechanics, Defensive/Conquest, harvest, discovery count basis, sufficiency exit, graded push tiers, $0.50 floor) | Ask before use; the answer holds for the product until the owner changes it [PB] | Owner | — |
| A-73 | Ledger row escalated; manager's action graded ineffective | Hold + refer; structural review (listing, offer, inventory, objective) [SR] | Owner | — |
| A-74 | Upload before approval | Never; upload file is PREPARED only after zero-failure validation [SR] | Approver | — |
| A-75 | Bidding-strategy change | Only through the fixed-bid trial with owner approval [register #8] | Owner | Ex (B6): no strategy written |
| A-76 | Amazon suggested bid / "market price" offered as a price | Not used [register #18] | — | — |

---

# Part B — Failure register

Columns: **Failure** · **Why it's wrong** · **Correct behaviour** · **Test** (how to detect it; a test that finds ≥ 1 row fails the quality gate).

## B.1 Data and intake

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| D-01 | Starting before every input is supplied or confirmed absent | Partial reads drive decisions later contradicted | One batch request; halt until each item is in or confirmed N/A | Intake register: every item READ-FULL / confirmed absent [PB, QA, WB] |
| D-02 | Guessing: filling unmatched SKUs, invented rank, TOS%, IS, prices, targets; 0 for a blank | A fabricated number is indistinguishable from a real one downstream | Blank + named gap; "Not available" | Every value traces to a file/sheet/window; no 0 where source is blank [A, E, D] |
| D-03 | Missing current ranks (38 of 40 targets) (seen: B6 F22) | Rank gap drives the premium; no rank, no push logic | Read the daily crawl rank; untracked = "not tracked" | Keyword tab rank column populated for every push/target term [B6] |
| D-04 | Unranked days counted as a rank; two rank tables used interchangeably | Median distorts; tables disagreed ~7 places | Median with unranked days as NR (NR if half the days unranked); name the governing source | Rank source column on every rank figure [B6] |
| D-05 | Fuzzy / reordered keyword matching; retyped portfolio name; mixed portfolios or marketplaces | Wrong joins; "0 rows"; blended markets | Exact lowercase/trim match; copy the portfolio string; one product, one marketplace | Join-miss count reported; marketplace single-valued [A, E] |
| D-06 | One portfolio when ranking spend lives in a sibling | Understates spend ("$94 artifact") | Include sibling campaign scope; reconcile openly | Campaign-scope vs product-scope reconciliation shown [QA] |
| D-07 | Summing SQP market columns across child ASINs; using SQP's precomputed rates | Multiplies market by child count; every share wrong | Market taken once, brand summed; recompute rates | Brand ≤ market; shares 0–100% [SQP] |
| D-08 | Recomputing SSOT product metrics from the bulk; deriving a value that was supplied | Two versions of one number | Supplied column beats derivation; wrong-looking column = finding | One figure, one value across tabs [QA, WB] |
| D-09 | Skipping quarantine (CVR with 0 orders, CTR with 0 clicks, conflicting sources) | Decisions on impossible data | Quarantine, no recommendation, refresh | Quarantine count reported; no action on quarantined rows [PB, SR] |
| D-10 | Judging thin data; small-sample placement verdicts (seen: B6 F32) | < 15 clicks measures nothing | No change under 15 clicks (11 PT); placement comparisons use the significance test, n < 30 = directional | No actioned row < floor except formula-only [B6, PF, WB] |
| D-11 | Parking a converting row for thin clicks | Most common single violation; loses proven orders | Converting rows skip the sample gate | Rows with orders > 0 and HOLD(thin) = 0 [DR, PB] |
| D-12 | Gate read on blended data (0.626% blended vs 2.955% TOS) | Blended hides the delivering placement | Read at the delivering placement; show both | Every CTR/CVR gate cites its placement [DR] |
| D-13 | Truncated-budget data used as bid evidence; 0%/$0 read as truncation | Rates from a campaign that stopped mid-day are not rates | Budget first; 0%/$0 = missing data | No bid verdict where in-budget < 70% [PB] |
| D-14 | Changes on campaigns with no current state (seen: B6 F13) | Can raise a price on a paused or mis-coloured campaign | Read every in-scope campaign before any write | Every decision's campaign is in the state list [B6] |
| D-15 | Shared multi-product campaigns automated (seen: B6 F29) | Moves another product's ads | Exclude from colour/price automation | Shared flag on every such campaign; no writes [B6] |
| D-16 | Velocity from a distorted window (stockout, suppression, deal) uncorrected; untagged multipliers | Over/understates cover and clearance | Stated correction factor + basis | Every velocity cites window and factor [LTSF] |
| D-17 | Inventory from the variation page or units > 0; market "weekly sales" read as ours | Not sellable stock; not our sales | Full inventory export; available + dated inbound; label market data | Inventory source = full export [PF, INV] |

## B.2 Economics

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| E-01 | Break-even from the wrong margin / blended parent / another product (seen: B6 F02) | B6: $26.60 vs $18.81 → ceilings ~40% too high; 154 of 180 ranking campaigns already above true break-even | Sellerboard profit/unit before ads per advertised SKU/colour at the price in force | Break-even on every row = SKU margin × placement CVR [B6, SR] |
| E-02 | Silent default break-even when a SKU has no economics | Prices a SKU on nobody's margin | Halt that SKU | No row priced without SKU economics [SR] |
| E-03 | Limit set by what we paid (TOS cost + 15%) (seen: B6 F23) | Drifts up with every raise; ignores profit | Ceiling = 2 × break-even CPC (ranking); ≤ 1 × break-even elsewhere | Price ≤ ceiling on every row [B6] |
| E-04 | Push sized on a TACoS rung; TACoS used as a bid gate (seen: B6 F24) | Owner rule is margin after ads and a spend limit | Size spend against the limit and margin rule; TACoS monitored only | Total ≤ limit; no TACoS-derived budget [B6, register #17] |
| E-05 | Cuts triggered by leaving a band, not break-even (seen: B6 F31) | A band isn't profit | Cut when over break-even on both 30 and 90 days | Every non-ranking cut cites both windows vs break-even [B6] |
| E-06 | Per-unit ceiling used as a per-click ceiling | Allows bids ~1 ÷ CVR too high | Break-even CPC = margin × CVR | Ceiling unit = $/click [WB] |
| E-07 | Returns added to break-even; COGS in LTSF decisions; LTSF floor = break-even | Mixes locked definitions; COGS is sunk in clearance | Locked break-even (no returns); forward net recovery; floor = salvage parity | Formula audit [SR, LTSF] |
| E-08 | LTSF read per unit or at a flat rate | Overstates 1.4–4.8×; understates near-cliff batches up to 3.6× | Per cubic foot per month by age bracket, assessed on the 15th | Charge reconciles to invoice [LTSF] |
| E-09 | Trimming rows already ≤ break-even; raising > break-even rows "to gather data" | Cuts profit; buys losses | Leave ≤ BE rows; data-gathering only inside ceiling | No cut on ACoS ≤ BE without an aged-clear reason [SR] |
| E-10 | Across-the-board cut while TACoS is healthy; blanket % cut under code-red | Destroys profitable volume | Negate/harvest the leaks; per-row review | No uniform % change across > 5 rows [SR, PB] |
| E-11 | Cut batch not checked for opportunity cost | Saved spend can be worth less than lost orders | Re-test each cut at the deal-state margin; withdraw failures | Lost-order value < spend saved, per cut [PB] |
| E-12 | Price/fee event credited to or blamed on a lever | False WORKED/BACKFIRED | Break-even shift > 10% → PROVISIONAL | Grade vs break-even delta [SR] |

## B.3 Inventory and routing

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| I-01 | Ranking ads switched to a slow colour (Queen → 7th seller) (seen: B6 F09) | Lowers CVR and margin; costs rank | Ranking advertises the size's best seller; backup only when it can't last to arrival | Every ranking campaign = hero of its size or listed exception [B6] |
| I-02 | Colour switch that changes size (seen: B6 F10) | Breaks the listing the shopper searched | Size locked on every switch | Size-changing switches = 0 (one wrong-size fix allowed) [B6] |
| I-03 | Discovery on best sellers (seen: B6 F11) | Hero stock is for ranking; discovery should move slow stock | Discovery advertises the size's clearance colour (≥ 180 days cover, or ≥ 90 while selling ≤ size median) | Discovery colour = clearance colour [B6] |
| I-04 | Cover computed on the engine's inflated push pace (seen: B6 F30) | Creates a stock-out that isn't there | 30-day pace (7-day warning); TIGHT ≤ 7 days = ease, don't swap | Cover column cites the 30-day pace [B6] |
| I-05 | Push or raise on Red/Yellow; bids on 0-stock or non-serving rows | Push into a stock-out loses rank | Zone gate before performance | No raise where zone ≠ Green [SR, PF, PB] |
| I-06 | Routing read from campaign names (212 of 251 wrong) | Names drift | Read Product Ad rows | Routing source = product ad rows [WB, PB] |
| I-07 | Backups auto-derived; backup self-competition ignored; inbound ignored | Wrong fallback; swapped ad competes with its own campaign; overstock regenerates | Backups pasted by user; note existing ads; inbound vs DOH ceiling | Backup source recorded [INV, LTSF] |
| I-08 | Ceilings carried from the departing SKU after a re-route; baselines not reset | Wrong economics | Rebuild economics; reset CVR baseline, rank clock, ROS gate | Re-routed rows show new SKU economics [PB] |
| I-09 | Stockout signature read as relevance loss | Rank collapse in one colour/size during an outage is stock | Check stock timeline first | State E notes cite stock timeline [LTSF] |
| I-10 | High cover read as safe while velocity declines 15% WoW for 3 weeks | Cover rises because demand falls | Treat as trajectory problem | Velocity trend beside DOH [PB] |
| I-11 | LTSF: discounting a fixable-demand SKU; parent-wide levers on variation overstock; stacking past cap; experimenting on a dead SKU > 7 days; removing profitable aged stock; disposing sellable stock; single-family plan | Wrong archetype = costliest LTSF error | Classify archetype first; child-scoped levers; ≥ 2 lever families | Archetype + scope on every lever [LTSF] |

## B.4 Keywords and negation

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| K-01 | Negating an exact ranking term, a brand term or a relevant term (SR zero-order branch) | Kills rank and the most profitable orders | Brand/ranking exact never; relevant non-converter → fix queue; ≥ 20 clicks 0 orders → REDUCE (relevant, live owner) / REVIEW (relevant, no owner) / BLOCK (irrelevant) [register #38] | Brand and push terms never blocked [SR defect, STR, B6] |
| K-02 | Negating on spend alone, < 5 clicks, root-wide sweeps, or with no mode stated | Removes demand without evidence | STR tree; cite that occurrence's clicks/spend/orders; mode = pre-load / reactive / steering | Every negative cites its own numbers + mode [STR, PB] |
| K-03 | Brand variants missing from the brand list | Brand terms flagged for negation | Brand name + misspellings list | Brand-list check before negation pass [STR] |
| K-04 | Brand negatives added before brand exacts could serve (seen: B6 F18) | Moves profitable brand traffic to campaigns that can't serve it | Gate: receiving exacts defensive, on the hero, funded | Brand negatives only where gate passed [B6] |
| K-05 | Existing duplicates and paused owners left (seen: B6 F28) | Split data; self-bidding | One owner per term, close variants counted; restart or retire paused owners | One live exact owner per term [B6] |
| K-06 | Duplicate built beside a paused keyword (seen: B6 F16) | Loses history; self-competition | Restart before build | Build path checks every exact (live/paused/close variant) [B6] |
| K-07 | Word-order variants collapsed; singular + plural exacts both kept; "King" matched before "California King" | Amazon treats word order as distinct; plurals are close variants; wrong size | Word order preserved; plurals merge; longest size token first | Normalisation audit [PH, PB, E] |
| K-08 | De-dup using Ad Group State; silently enabling singletons; paused-campaign keeper unflagged; edits beyond State | Wrong status; unexpected serving | Keyword State OR Campaign State; ask before enabling; flag | No group with > 1 enabled or 0 enabled [LP] |
| K-09 | Duplicate check run before re-enables | Re-enable creates new duplicates | Dup check on the post-re-enable population | Dup check timestamp after re-enable set [PF] |
| K-10 | Relevancy scorer: overwriting the original; disqualifying "pillowcase"; non-English ≈ 0 read as irrelevant; "fixing" copy in the scorer | Destroys the second opinion; false negatives | Add columns, keep original; hand-check regex hits | Original relevancy column intact [LP] |
| K-11 | Trusting a relevancy label that is wrong (e.g. "red bamboo sheets" Not Relevant) | Blocks a real colour demand | Cross-check label against the term classifier | Label/classifier disagreements listed [B6] |
| K-12 | Harvest without negating the source; harvesting on BOTH-FAILING or off-category terms | Double-serving; scaling a broken syntax | Build exact at break-even, negate source same upload; quadrant check | Every harvest has a paired negative [PB, AP] |
| K-13 | Coverage gap from exact-text match without STR cross-check; padded coverage | Overstates the gap | Cross-check STR; relevant terms only | Gap list cites STR check [LTSF] |
| K-14 | Product targets called "search terms"; campaign-level negative on a single-ASIN PAT | Wrong entity; kills the campaign | Target-level pause for dedicated single-ASIN PAT | Negation format per entity [SR] |

## B.5 Campaigns and objectives

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| C-01 | Colour, competitor, Spanish, misspelled exacts retagged Ranking (seen: B6 F12) | Nobody builds organic rank on those; unlocks push logic wrongly | Generic niche exact → Ranking; others → Profitable Conversion; brand → Defensive [register #36] | Retags carry a classifier verdict [B6] |
| C-02 | Objective per keyword then mode-averaged; campaign name trusted over targeting; Defensive on a generic term | Objective is a campaign property from targeting | Decide per campaign from targeting | Blocks with > 1 objective = 0; Defensive has a brand keyword [OC, DR] |
| C-03 | Exact and broad in one campaign; judging on one campaign row; merging exact-ranking with broad-discovery | Mixed loops, wrong metric | Separate; judge the unit across its rows | Mixed-block flag count [OC, SR] |
| C-04 | Contradictory directions on one term (−20% here, +15% there); label contradicting the written value (seen: B6 F06) | Incoherent; a "taper" that raised price | Term-level reconciliation; notes must match value | One direction per term; label vs value check [DR, B6] |
| C-05 | Family-scoped / name-pattern batch actions; blanket root scale or cut | Not derived per row | Each row on its own data | No action justified by a group name [DR, PB, SR] |
| C-06 | Acting on rows that can't deliver: paused, duplicate, Red (seen: B6 F16 — prices raised on paused keywords) | A bid can't make a paused row serve | Restart decision; no bid on non-live rows | Bids on non-live rows = 0 [DR, B6] |
| C-07 | One lever with no alternative considered; > 1 lever per row per cycle; only one lever type ever evaluated | Misses the real constraint; confounds reads | Name why this lever, not the adjacent one; one lever per row (base+boost backward-solve exempt) | Reasoning names the alternative [DR, PB] |
| C-08 | Bidding strategy changed by default; Fixed as a default | Confounds every read; owner rule | Leave strategies; new = dynamic down-only; Fixed via trial only | No strategy written without approval [register #8] |
| C-09 | Mechanism change across many campaigns with no control arm | Can't tell effect from trend | Hold some campaigns unchanged | Control arm listed [PB] |
| C-10 | Silent HOLD outside the list; hold on a condition already met | Parks rows without a reason | Ask first; verify condition still holds | Every HOLD reason ∈ silent-hold list or logged ask [PB, WB] |
| C-11 | Paused ad group re-enabled in a different upload than its bids | Half-deployed state | Re-enable and bulk changes upload together | Upload pairing check [PF] |

## B.6 Placement and pricing

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| P-01 | +75% "dose" jumps (seen: B6 F04) | $50–100 per order vs $16–22 profit | Push price = BE × (1 + premium) ≤ 2 × BE; ≤ +30%/day | No raise > +30%; no push price > 2 × BE [B6] |
| P-02 | Over-ceiling price left in place (seen: B6 F05) | Loses money every order | Cut to ceiling in the same run, never deferred | No new price above ceiling [B6] |
| P-03 | Boost raised while the base keeps buying product pages (seen: B6 F07) | Boost only applies at the top | Mix fix: base −50% (−25% if PDP sells) + boost holds TOS price, one write | Boost raise refused when PDP > 20% without pair [B6] |
| P-04 | Escaping the 900% cap by raising base (+180%); crediting a capped step (seen: B6 F08) | Triples PDP bids; phantom clicks | Base = price ÷ (1 + boost), boost set together | No boost > 900%; base changes paired [B6] |
| P-05 | Budgets blocked while prices go live (seen: B6 F14) | Push stops mid-afternoon | Price and budget rows load together; budget = plan clicks × price | Every funded term has a budget row [B6] |
| P-06 | Uniform TOS bump / blanket TOS shift; TOS falling as residue of a base cut; ranking at 0% TOS; orphan modifiers | Not derived; kills rank | Backward-solve per campaign; TOS held on base cuts | Flat-value share across a sized set ≤ 45% non-zero; no 0% ranking TOS [PF, WB, SR] |
| P-07 | Cuts > 15%/cycle when gradual; flat above-ceiling premium across the roster | Overshoots; not sized by rank gap | Caps per register #5; premium per row by rank gap | Step and premium audit [SR, PB] |
| P-08 | Base below the eligibility floor ($0.35–0.50) | Suppresses delivery | Floor ≥ clearing ÷ 10; ceiling wins if lower | Base ≥ floor [WB] |
| P-09 | Up-and-down doubling ignored ("$12.00 authorised click") | Real max CPC 2× the written price | Authorised price includes × 2 | Authorised-ceiling audit [SR] |
| P-10 | Budget cap reported as spend; empty new budget; round() instead of ceil() | Misstates exposure; under-funds | Committed = run-rate spend; budget ≥ required × 1.05, ceil | Budget column checks [WB, PF] |
| P-11 | Required clicks at a target CVR; DSTR ÷ CVR without organic netting; fractional DSTR; ladder + netting double count | Doubles spend ($5,595 vs $1,965/day) | Paid = DSTR − organic; clicks = paid ÷ achieved TOS CVR; DSTR ≥ 1 | organic + paid = DSTR ± 0.02 [PF, register #19] |
| P-12 | Amazon suggested bid used as the price | Anchors to Amazon's range | Break-even maths only | No suggested-bid source on any price [register #18] |

## B.7 Ranking

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| R-01 | Pushing where the ceiling is below what we already pay (seen: B6 F25) | Burns money without moving rank | Qualify only if ceiling ≥ own TOS CPC; else WAIT | Push rows: ceiling ≥ TOS CPC [B6] |
| R-02 | Listing problems pushed with money (seen: B6 F26) | More traffic loses more when the listing loses the click/sale | SQP ratio < 1.0 on ≥ 30 clicks → WAIT (listing) | Push rows pass the listing check [B6] |
| R-03 | Focus group overriding qualification (seen: B6 F06) | Biggest qualifying term tapered | Qualification per term before focus | Every qualifying term with a plan is PUSH or WAIT with a reason [B6] |
| R-04 | Inflated click forecast (seen: B6 F20) | Justifies unbuyable spend; fakes stock-outs | Credit steps with what steps of that size bought | Forecast ≤ step book [B6] |
| R-05 | Click requirements not reconciled to the product (seen: B6 F21) | Sum exceeds what the product sells | Scale to the product; volume/budget only, never price | Σ requirements ≤ product sales [B6] |
| R-06 | Cutting a ranking row in a DSTR deficit; bidding up a conversion deficit; traffic into a Conversion syntax | Cuts velocity rank needs; pays for a listing problem | Deficit → hold or raise; conversion → fix offer | No cut where orders/day < DSTR [SR, LTSF] |
| R-07 | Estimate treated as a gate; at-plan row called a failure; collapsing rank given a bid-up | Rank movement governs; collapse needs a cause | States A–F; State E never a bid change | Validation checks 3, 9, 10 [DR, PB] |
| R-08 | Capacity used as a disqualifier; rank target with no funded campaign called a plan; invented DSTR | Not a plan; no basis | 5-property gate (sized, dated, ceilinged, predicted, funded) | Every push row passes 5 properties [PF, PB, LTSF] |
| R-09 | Secondary syntax ranked; re-entering a ranking posture without a fresh realism pass | Spend outside the declared priority | Secondary = self-funding only; realism pass on re-entry | Ranking rows on secondary roots capped [PF, SR, PB] |
| R-10 | Paying for rank already held | Money with no rank to buy | HOLD RANK 2 weeks, then taper | At-target rows have no raise [B6, register #26] |

## B.8 Competitors

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| X-01 | Own listings treated as competitors; one ASIN targeted in several campaigns; price-mismatched targets beside conquest (seen: B6 F27) | Own-page targeting is defence/cross-sell; duplicates self-bid | Classify each ASIN (own product / own other / competitor / non-category / unmapped); one owner per ASIN | ASIN classifier column complete [B6] |
| X-02 | Bare ASINs; counting ASINs not brands; conflating visible vs account keyword totals | Overcounts rivals; misreads scale | Resolve brand for every ASIN; same brand = one competitor | No bare-ASIN tables [LP] |
| X-03 | Dismissing a quiet-but-equipped competitor; volume artifacts in totals | Recent pull-back may re-enter; totals inflated | Watch infrastructure mismatch; verify and exclude artifacts | Artifact list stated [LP] |
| X-04 | Competitor data setting a bid or price | Owner rule; prices stay break-even-based | Competitor data chooses terms, order, targets, read windows | No competitor rule sets or raises a price [B6 R-CI4] |
| X-05 | Conclusions about unmeasured competitors | Unknown ≠ absent | Report coverage (e.g. 13 of 32) | Every competitor claim states coverage [B6 R-CI12] |
| X-06 | Carrying an overturned finding ("2.71× market price, OUTPRICED" after the 74-ASIN pull showed 1.00–1.06×) | Wrong premise drives actions | Withdrawn-findings register | Findings trace to current pull [DR] |
| X-07 | Generic category terms pushed for volume; blocking a term that still sells and rivals buy | Push should be winnable core terms; block loses sales | Push only addressable core terms ranked on by a majority of measured rivals (B6: ≥ 7 of 13; register #46); REDUCE to break-even, not block (≥ 10 orders/90 d) | Push-term classifier; block-review list [B6 R-CI1, R-CI9] |

## B.9 Events and deals

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| V-01 | Deal not read (seen: B6 F01) | Deal changes margin (−20%), CVR and every read | Calendar gate before any rule | No build/fold on deal days; no verdict with > 2 deal days in window [B6] |
| V-02 | No goal, spend limit or clean baseline; baseline includes deal days (seen: B6 F03) | Forecast can't be judged; baseline ~80% high | Goal block before pricing; baseline excludes event/settling days | Push budgets + other spend ≤ limit [B6] |
| V-03 | New campaigns launched during a deal; two SB formats on one term (seen: B6 F17) | Learn on deal traffic; formats compete | No launches on event days; one SB format per term | Deal-day builds = 0 [B6] |
| V-04 | Structural folds mid-deal (seen: B6 F19) | Destroys history the post-event audit needs | Decide folds after the event | Deal-day folds = 0 [B6] |
| V-05 | Deal used to excuse a bleed; unflagged mid-deal cut | Real losses continue; confounded reads | Deal blocks gradual cuts only; bleed stops run; flagged | Bleed stops present in deal cycles [SR] |
| V-06 | Deal originates a push; in-deal CVR justifies a bid above the deal-state ceiling | Push without gates; overpays at lower margin | Gate the push first; ceiling at deal-state margin | Deal-state ceiling column [PB] |
| V-07 | Grading on deal weeks; cliff exit after an event | False verdicts; rank shock | DEAL_WINDOW; 3–5 day taper; 2-week guard | See reference 10 §5, §12 [SR] |

## B.10 Writing and deliverables

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| W-01 | Verdict with no arithmetic; metrics beside the verdict, not inside it | Reader can't follow or check | Numbers doing the work, inline arithmetic, reversal, re-read date | Reasoning contains the ceiling arithmetic [DR, PB] |
| W-02 | Templated verdicts; scripted output presented as the full record | "Shared rules are law; shared verdicts are templating" | Row-specific reasoning; state which fields are mechanical | > 5 rows with same status + same change % + same first 120 chars → review; string-compare duplicates [SR, PB] |
| W-03 | Internal codes, "this skill", version history, personal names in delivered text | Unreadable to owners; leaks process | Rule IDs only in workbook rule columns | Text search for §, rule codes, "this skill", versions [PB, register #28] |
| W-04 | Columns lost between revisions; duplicated sections; totals ≠ components; several files where one is expected | Contract broken; can't reconcile | Diff columns vs prior file; one consolidated file | Column diff; totals reconcile [DR, LTSF] |
| W-05 | Instruction written in a recording column (State); one verb for two operations; retired verbs; verdict with no entity | Undeployable or ambiguous | Grammar: `BID $x → $y`, `MODIFIER n% → m%`; action = cells | Action vs cell values match [WB] |
| W-06 | Unnamed soft coefficients; untagged multipliers; false precision; implausible forecasts; promising ACoS cuts in an invest week | Unfalsifiable | Name soft coefficients; ranges; basis tags | Every projection has a basis tag [PB, LTSF, AP] |
| W-07 | Inventing or contradicting the decision sheet in a write-up; padding sections without evidence | Report diverges from what ships | Explain the sheet's logic; sections only with evidence | Report actions = workbook actions [AP] |
| W-08 | Numbers without source and date | Can't be checked | Source + window on every figure | Figure-source audit [PB, LTSF] |

## B.11 Process and engineering

| # | Failure | Why it's wrong | Correct behaviour | Test |
|---|---|---|---|---|
| G-01 | Withheld rows exported as changes (seen: B6 F15) | Loader applies what the engine declined | Export filter on verdict | Exported rows ⊆ changed verdicts [B6] |
| G-02 | Uploading before approval; shipping without log + upload file | Unreviewed changes; no history | Zero-failure validation → approval → upload | Approval record before upload [SR] |
| G-03 | Grading undeployed actions; blaming un-uploaded recommendations | False failures | Execution verification first | Execution status on every grade [SR, WB, LTSF] |
| G-04 | Repeating a dead lever a 3rd time | Known-failed spend | Escalate after 2 | No lever with 2 failed grades re-issued [SR] |
| G-05 | Confounded reads: two levers in one window; windows straddling a lever change | Can't attribute | One lever per window | Window vs change-date check [LTSF] |
| G-06 | Owner override or reviewer mark silently reverted on regeneration | Breaks trust; loses decisions | Overrides persist | Override register diff [PB] |
| G-07 | Gate that passes the defect; PASS beside non-zero fails; check scoped to one tab; self-reported gate | False assurance | Gate must fire on a known-bad case; coverage over every action tab | Self-test with a known-bad row [WB] |
| G-08 | Answerable gap logged as "revisit next cycle"; provisional rule applied "with a flag" instead of asked | Delays a decision the owner could make now | Ask once; ask before first use | Q&A log [PB] |
| G-09 | Bulk file defects: extra sheets, blank State, numeric dates, names > 128 chars, symbols in keywords, formulas/NaN, guessed IDs, keyword-group targets in bulk, file re-saved in Excel, re-uploading succeeded rows | Upload fails or cascades | Bulk canon; fix-file of failed rows only | Upload gate prints all pass [CB] |
| G-10 | Known source-code defects copied: freeze/backfire branches crash (undefined variables), freeze/floor never recorded; fresh clicks = cycle total; zero-order branch negates exact ranking terms; turn-off thresholds doubled twice; column-name mismatches blanking log fields; syntax roll-up reading a column never written; "KING" parsed before "CALKING"; silent break-even 0.1986; tolerance bug (0.9 × 1.1 ≈ 0.99 bar); DOH rename disabling inventory gates; duplicate log rows; single-metric verify | Silent wrong decisions | Implement the rules in this skill, not the code; regression tests for each | Regression suite covers each item [SR, DE, register §3] |
| G-11 | Formulas unconverted (LET → #NAME?); CSV exported before recalc; renderer recomputing steps | Broken or divergent numbers | Values only; recalc before export; render from the decided record | Zero formula errors [MDB, WB] |

---

## Open questions for the owner

1. **Turn-off thresholds (A-33):** the SR code doubles the objective turn-off level twice; the framework intent listed here (Ranking 100%, Market Share 50%, Discovery 60%, Profitable Conversion 50%, Defensive/PAT 30%) is inferred from the source notes, not stated by register 13. Confirm the levels.
2. **Zero-order rule vs silent-hold list:** (decision labels per 13 #38: REDUCE with a live owner, REVIEW without.) The house rule "≥ 20 clicks, 0 orders → REDUCE (owned)" is not on the PB exhaustive silent-hold list, but it is a REDUCE, not a HOLD, so no ask is triggered. Confirm this reading.
3. **Conversion deficit (A-34):** Resolved — see 13 #39: bid −15% and refer to Brand Management; no rank push until the offer is fixed.
