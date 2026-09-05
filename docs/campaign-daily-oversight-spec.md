# Campaign Daily Oversight — build spec

The daily tier of the PPC Oversight System, as a screen. One product, one marketplace,
day grain. Sits alongside the existing Performance Monitor tables and reuses their
arithmetic, their placement estimator, and their attribution-settling treatment.

Read this with `README.md` (the three-tier system) and `config/thresholds.yml`
(every threshold referenced here by ID).

---

## 1 · Information architecture

```
[ PINNED — PRODUCT PROFILE ]                         does not scroll away
  Compact (default, one row)
  Expanded (click)

[ SUB-TAB BAR ]   each label carries its own exception count
  Ranking (n) | Auto (n) | Manual (n) | Product & Category (n) | SB (n) | SD (n)

[ SUBTOTAL STRIP ]
  This tab: spend · sales · ACoS · % of product ad spend

[ LENS TOGGLES ]  within each tab, not peers of it
  Keywords | Placement | Target | Ranks

[ TABLE ]
  Shared spine + that tab's own columns
```

Three rules that hold across the whole screen:

- **The profile is context, not content.** Every ceiling, gate and diagnosis below it
  reads from the profile. It stays pinned so nobody decides without it.
- **Profile figures stay product-total** and do not react to the selected sub-tab.
  If they did, TACoS and organic sales would stop being coherent. The per-tab
  subtotal strip carries the tab's own numbers.
- **Tabs are objective-led.** Objective is assigned from targeting type by the standing
  rule — Exact = Ranking, auto and broad = Discovery, product/category = Profitable
  Conversion, brand keyword = Defensive — so the objective tabs land on the targeting
  types listed above. Where the two diverge, objective wins: a brand-defence Exact
  campaign is Defensive and is judged as such, not as a ranking push. Keep a Defensive
  filter chip available inside the Ranking tab for exactly that case.

---

## 2 · Product Profile

### 2.1 Compact state (pinned, always visible)

One row. Only what gates a decision:

`price + deal flag` · `Buy Box %` · `days of cover` · `break-even ACoS` ·
`max allowable CPC` · `TACoS day / 7d` · `exceptions (n)`

Everything else lives in the expanded state. A full profile block is 300–400px and
would push the table off a laptop screen.

### 2.2 Expanded state

**Identity & economics**

| Field | Notes |
|---|---|
| Thumbnail, title, parent ASIN, child ASIN, SKU, marketplace | |
| Current price · net price after any running deal | |
| Deal | type (Lightning / Best / Coupon / Promo), discount %, start–end, live Y/N |
| Buy Box % | **over the window, not at read time** — a 9am snapshot reads 100% on a day you lost the box from noon. Flag < 90%, alert < 70% |
| Inventory | units on hand · days of cover · units inbound |
| COGS / landed cost · Amazon fees (referral + FBA) | |
| Return rate | compute margin on **net** units — gross overstates it |
| Contribution margin per unit, before ads | |
| **Break-even ACoS** | contribution margin per unit ÷ price (the ACoS at which CM2 = 0) |
| **Target ACoS** | the profit target, set below break-even by objective |
| Blended CVR | product, trailing 30d |
| **Break-even CPC @ blended CVR** | break-even ACoS × price × CVR |
| **Max allowable CPC @ blended CVR** | target ACoS × price × CVR |

Label both CPC figures *"@ blended CVR — per-keyword ceilings are on the rows."*
Recompute whenever price or the deal changes: price down pushes the ceiling down,
deal-lifted CVR pushes it back up. The net effect must be computed, not assumed.

**The day** — each with its 7-day rolling value beside it

Ad spend · Ad sales · Organic sales · Total sales · **TACoS (day + 7d)** ·
Sessions · Unit session % · Units ordered

- TACoS lives here, not in the segment tile row — there is no all-source sales figure
  per segment, so the empty segment tile is correct behaviour. Remove it or relabel it
  "product-level only" so it stops reading as broken.
- **TACoS numerator is SP + SB + SD spend.** SP alone against a total-sales denominator
  is not TACoS and drifts further the more SB and SD you run.
- Daily TACoS is noisy — organic sales swing far more day to day than spend does.
  The 7-day rolling figure is the real number; the daily value is a pulse, never a trigger.
- Mark the last 3 days as attribution still settling, same treatment the chart uses.

**Rank & position**

BSR today + Δ vs yesterday + 30-day sparkline · category and subcategory BSR ·
star rating + review count + Δ · our price rank within the competitive set ("4 of 11")

**Competitor strip** — top 10 ASINs, sorted by BSR

Per competitor: ASIN + brand name · price + Δ · deal running? type + % · BSR + Δ ·
rating / review count.

- **Highlight only what changed since yesterday.** Nobody scans 40 static cells daily.
- One derived line above the strip — this is the line people actually read:
  *"2 competitors dropped price · 1 started a deal · our price rank 4 of 11"*

**Today's exceptions**

Count + severity chips for D1–D7 (ad eligibility, delivery stopped, Buy Box, stock
cover, spend pacing, spend anomaly, budget cap time, runaway spend). Each clicks
through to the affected campaign or keyword.

### 2.3 Why this block exists

A window showing ad sales down 23.5% and orders down 21.0% on flat impressions cannot
be diagnosed from ad data alone. It is bidding, price, Buy Box, or a competitor — and
in three of those four cases no bid change would have fixed it.

---

## 3 · Shared column spine

Every tab carries these, in this order:

```
Campaign
Effective state            derived: Live / Paused-KW / Paused-Campaign / Archived
                           A keyword is live only if BOTH keyword state AND campaign
                           state are enabled. Raw values in the tooltip.
Objective                  Ranking | Discovery | Profitable Conversion | Defensive
Portfolio
Advertised SKU

Bid
TOS modifier % · PDP modifier % · ROS modifier %
Effective bid per placement = base bid × (1 + modifier)      context, not judgement

Budget · spend/budget % · in-budget % · cap time
                           cap time answers "when did it die"
                           in-budget % answers "how much of the day did we serve"
                           FLAG capped before 18:00 (20:00 if Ranking)

Max allowable CPC (row ceiling)
CPC vs ceiling — Total | TOS | PDP | ROS
                           show as headroom: "$1.95 of $1.50 (130%)"
                           amber 90–100%, red above

Placement block — Total | TOS | PDP | ROS
  impressions · clicks · click-share % · CTR · CVR · CPC · orders · sales · ACoS
```

**Row flags** (colour the row, don't add columns): more than 1 enabled target ·
duplicate keyword · budget capped early · 0 orders at ≥ 3× target CPA ·
ACoS above SKU break-even on a Profitable Conversion campaign.

**Lens toggles** — Keywords / Placement / Target / Ranks stay *inside* each tab. They
are different views of the same campaigns, not different campaign types.

---

## 4 · Tab 1 — Ranking

Objective: **Ranking**. Exact keyword campaigns. This is the full tier; every other tab
is a reduction of it. Brand-defence exact campaigns sit here under a **Defensive** chip
and are judged on defence, not on rank gap.

**Target composition**

```
Primary target        = the enabled target with the MOST CLICKS in the window
                        NOT highest SV. The row's ACoS, CVR, CPC and placement split
                        are dominated by whichever target got the traffic; labelling
                        the row with a high-SV target that got 3 clicks makes every
                        metric beside it describe a different keyword.
Primary target SV
# enabled targets       FLAG RED if > 1. Row expands to list every enabled target
                        with its clicks + SV, so the rest can be paused.
# other campaigns targeting this keyword    FLAG if > 0
Duplicate group chip    see §9
```

**Ranking commitment**

```
Target rank · Current rank
CPR (Helium 10) · DSTR (DataRova)
Required sales · Actual sales
Required clicks · Actual clicks · Gap
Required impressions = required clicks ÷ target CTR
Actual impressions · Impression gap
30-day organic rank strip, newest first
```

**CTR / CVR — three values each**

```
CTR   Market (SQP) | Target | Actual | gap
CVR   Market (SQP) | Target | Actual | gap
```

The chain runs: **required sales → ÷ CVR → required clicks → ÷ CTR → required
impressions → vs what TOS share can deliver.** A CVR assumption is already inside
Target Clicks ("at our own measured conversion") — this surfaces it, because when the
assumption is wrong the required-clicks figure is wrong by the same factor, silently.

**Constraint column** — the only column that outputs a decision

Read in order, first match wins:

| # | Condition | Verdict | Action |
|---|---|---|---|
| 1 | Actual CVR < 60% of market CVR | **LISTING-CONSTRAINED** | Hold the push. Fix page / price / reviews. Do not fund. |
| 2 | Actual CTR < 60% of market CTR | **CREATIVE-CONSTRAINED** | Main image, title, price, badge. Bids won't fix CTR. |
| 3 | Impressions < required impressions | **IMPRESSION-CONSTRAINED** | Raise bid *or* TOS modifier. One, not both. |
| 4 | Budget capped before 20:00 | **BUDGET-CONSTRAINED** | Raise budget or reallocate. |
| 5 | otherwise | **ON TRACK** | |

**Sufficiency** — CVR needs ≥ 20 clicks, CTR needs ≥ 500 impressions. Below the floor:
show the target, grey the actual, set the constraint to **OBSERVING**. A
"listing-constrained" verdict off 4 clicks sends someone to rewrite a listing that was
never the problem.

**CVR floor as a funding gate.** Below the rule-1 floor the campaign is not eligible for
a bid or budget increase this cycle regardless of rank gap. Rank follows sales velocity —
clicks that don't convert don't rank, they just spend the ranking budget.

**Sort this tab by the constraint column, not the rank gap.** A campaign 40 clicks short
because it's impression-constrained gets a bid change today; one 40 clicks short because
CVR collapsed gets escalated to whoever owns the listing.

---

## 5 · Tab 2 — Auto

Objective: **Discovery**. No keywords exist here. Row = campaign, expandable to its four auto target types —
bids are set per target type, so that is the real grain underneath.

```
Per target type (close match / loose match / substitutes / complements):
  state · bid · impressions · clicks · CTR · CPC · orders · sales · ACoS

DISCOVERY YIELD          judge auto on this, NOT on ACoS
  new harvestable search terms in the window
  cost per harvested term
  % of spend on terms already harvested elsewhere   = leakage

NEGATIVE COVERAGE
  # negatives · are harvested terms negated back here?
  An auto campaign with no negatives leaks into its own exact campaigns.

DRILL: search terms generated
```

---

## 6 · Tab 3 — Manual (Broad / Phrase)

Objective: **Discovery**. Row = campaign, expandable to all targeted keywords.

```
Per keyword: keyword · SV · state · bid · clicks · sales · ACoS
Same DISCOVERY YIELD + NEGATIVE COVERAGE block as Auto
DRILL: search terms generated
```

Amazon SP has Exact, Phrase and Broad only — there is no broad match modifier (that is
a Google concept). Broad shaped by negatives is the negative-coverage column above.

**Auto and Manual are not judged on ACoS.** They are Discovery objective by definition.
A broad campaign at 80% ACoS feeding three profitable exact campaigns is working; one at
30% ACoS producing no new harvestable terms is a dead end wearing a good number.

---

## 7 · Tab 4 — Product & Category Targeting

Objective: **Profitable Conversion** (Defensive where the target is our own ASIN).
Row = campaign, expandable to each target. Separate from Manual because a PAT row
targets an ASIN and a Category row targets a category node — neither has a keyword,
an SV, a CPR or a rank.

```
PAT       target ASIN + RESOLVED BRAND + product title    never a bare ASIN
Category  category node + refinements (price band, rating, brand)

CONQUEST CONTEXT   joined from the Product Profile competitor set
  their price vs ours · their BSR · their rating · deal running?
  This is what decides whether a target is worth defending or dropping.

Expect PDP-dominant placement. FLAG a PAT campaign with high TOS share — it usually
means the target is behaving like a keyword campaign.

DRILL: which ASINs the ads actually served on
```

---

## 8 · Tabs 5 & 6 — Sponsored Brands, Sponsored Display

**SB**

```
Ad format (Product Collection / Store Spotlight / Video)
Landing page (Store vs custom) · headline / creative
NEW-TO-BRAND: NTB orders · NTB sales · NTB % of orders
  This is what SB exists for. Judging SB on ACoS alone misses it entirely.
Top-of-search impression share · viewable impressions
SB placements differ from SP — do not reuse the TOS/PDP/ROS block as-is.
```

**SD**

```
Targeting: Contextual (product / category) vs Audience (views remarketing,
           purchases remarketing, similar-to)
Cost type: CPC vs vCPM — NOT comparable, never sum them
Viewable impressions · vCPM · view-through conversions · NTB
On-Amazon vs OFF-AMAZON split lives HERE
```

The existing OFF-AMZ column reads 0 / 0.0% on every SP row because Sponsored Products
does not serve off-Amazon. It isn't "too sparse to rate" — it's structurally empty on
SP, and belongs on this tab.

---

## 9 · Duplicate keyword detection

Amazon exact match already serves close variants — plural, misspelling, stemming,
function words. Two targets that normalise to the same key are bidding in the **same
auction**. You are outbidding yourself.

```
MATCH KEY = norm(keyword) + match_type

norm():  lowercase
         strip punctuation (hyphen, apostrophe, comma, slash)
         drop stopwords: a an the for of with and or in on to by
         singularise each token

SINGULARISE CAREFULLY — not a trailing-s strip.
  ss / us / is        -> unchanged   (mattress, status, analysis)
  ies -> y                           (canopies -> canopy)
  es after s/x/z/ch/sh -> drop es    (boxes -> box)
  else trailing s -> drop            (sheets -> sheet)
  + irregulars list
A naive strip gives "mattres" and the team stops trusting the flag.
```

| Tier | Condition | Treatment | Action |
|---|---|---|---|
| **1** | Same key, word order preserved, **same match type** | filled cell wash + solid rail | Self-competition. Keep one, pause the rest. |
| **2** | Matches only after sorting tokens (word order differs) | no fill, dashed rail, same hue | Human confirms. |
| — | Same key, **different match type** | no shade — link icon + count | Intended Hero/Halo layering, not a defect. Check an isolation negative exists in the broader campaign; flag if not. |

**Shading — one keyword, one shade**

```
WHERE     keyword cell background + 3px left rail. NOT the full row — the row already
          carries the rank heatmap, placement purples, crawl markers and low-click
          greying, and a full-width wash fights all of them.

SLOT      slot = hash(norm(keyword)) mod 8
          Hash the NORMALISED key so plural/singular land on the same shade.
          Hash-based, not row-order-based, so the shade is stable across the keyword
          view, the campaign view and future sessions.

PALETTE   8 hues. No red (reads as error), no green (that's the rank heatmap).
          H = [42 amber, 25 orange, 340 rose, 300 magenta,
               265 violet, 225 indigo, 190 cyan, 165 teal]
          light  wash hsl(H 70% 95%)  rail hsl(H 65% 62%)
                 chip hsl(H 65% 35%) on hsl(H 70% 92%)
          dark   wash hsl(H 40% 14%)  rail hsl(H 55% 55%)
                 chip hsl(H 60% 72%) on hsl(H 40% 18%)
          Violet/indigo sit near the placement-estimate purple — check together.

CHIP      Group ID (D1, D2, D3...) in the keyword cell. The chip is the identifier,
          the shade is a scanning aid — so the signal survives colourblind viewing,
          greyscale export, and two unrelated groups landing on the same slot.
          Click to filter the table to that group.

KEEP/PAUSE  Within each Tier 1 group mark one row KEEP (most clicks; on a tie, the one
            in the Ranking-objective campaign) and the rest PAUSE.
```

Store the normalised key as a hidden sortable column so duplicate rows sort adjacent.

---

## 10 · Economic ceilings

```
Max allowable CPC = target ACoS × price × CVR
```

CVR is in the formula, and CVR varies per keyword — a keyword converting at 25% justifies
roughly double the CPC of one at 12% on the same product. **The profile carries a
reference ceiling at blended CVR; each row carries its own ceiling at its own CVR.**

```
WHICH CVR      >= 20 clicks in window -> the row's own measured CVR
               below that             -> SQP market CVR, marked estimated
               never a blended product CVR on a row

MULTI-SKU      If a campaign has product ads for more than one SKU, use the LOWEST
               ceiling across them and FLAG the row. One bid serves all of them,
               so the thinnest-margin SKU sets the limit.
```

**The decision this drives**

| Reading | Action |
|---|---|
| Over ceiling on TOS only, under on PDP/ROS | Cut the **TOS modifier**. Not the base bid — that would discard profitable PDP/ROS traffic. |
| Over ceiling on every placement | Cut the **base bid**. |
| Under ceiling everywhere but under-delivering | Headroom exists. Raise bid *or* modifier — one, not both. |

**Objective gating — the one place where acting on the number in front of you is wrong**

| Objective | Ceiling |
|---|---|
| Profitable Conversion, Defensive | **Enforce.** |
| Discovery (auto, broad, phrase) | Advisory only — judge on discovery yield. |
| **Ranking** | **Do not enforce.** Running above break-even is the point. The constraint is the ranking budget and the CVR gate, not ACoS. Enforcing here kills working pushes. |

---

## 11 · Data integrity rules

These apply to every tab and are not optional.

**Attribution settling.** Mark the last 3 days as still settling, same treatment as the
chart. **No deltas inside the settling window** — a conversion delta there compares a
settled number against one still arriving, so it always reads as a decline and will
manufacture a fake drop every morning.

**Delta baselines** — a naive "vs yesterday" on everything makes noisy metrics scream
until people stop looking:

| Baseline | Use for |
|---|---|
| vs yesterday | Competitor price, deal on/off, BSR, Buy Box, rating |
| vs 7-day mean | Spend, CPC, sessions (this is what D5 already uses) |
| vs target | Rank — distance to committed target, not yesterday's wobble |

**Sufficiency floors.** CVR ≥ 20 clicks. CTR ≥ 500 impressions. Bid decisions ≥ 10 clicks.
Below the floor the answer is *observing*, which is a logged decision, not silence.

**Data vintage.** The rank-crawl staleness banner is exactly the right instinct — extend
it. Required-clicks blends a rank up to 5 days old, weekly SQP, a monthly H10 CPR and a
measured CVR. Stamp the composite age on the derived column, not just on the crawl.

**Estimate coverage.** Per-cell placement coverage already exists in a tooltip. Surface a
small per-row indicator too — hover-only disclosure means people read estimates as
measurements, and a 32%-covered row currently looks identical to a 95%-covered one.

---

## 12 · Open items

1. **Composite data vintage** on required-clicks and the CPR/DSTR columns — see §11.
2. **Competitor data source.** Daily price, BSR and deal state for 10 ASINs per product
   is a real pipeline (Keepa / DataDive / H10). The most-specced, least-sourced part of
   the profile.
3. **TACoS numerator** — confirm it carries SP + SB + SD spend, not SP alone.
4. **Off-AMZ column** reads 0 on every SP row. Confirm it should move to the SD tab.
5. **Exception engine** — confirm D1–D7 fire against `config/thresholds.yml` and produce
   a queue, rather than the counts being read off columns by eye.
6. **Action-log grading** — confirm something reads the log back and scores actions
   worked / flat / backfired two cycles later. Without that the log is a diary, and the
   weekly W2 step has no input.
