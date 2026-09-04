# The clearance objective, and what may be built under it

Step 1.1 sets the objective. This file says what that objective then permits, and what the new-campaign tabs must carry.

---

## Part 1 — What the re-tag changes

A clearance campaign answers one question: **how cheaply can we move these units before the next fee bracket?** Rank, share and defence metrics stop applying to these units on the day of the tag.

| | Ranking objective | Clearance objective |
|---|---|---|
| Buys | Position | Volume at a price where losing costs little |
| Judged on | Rank movement against a sized push | Units shipped, cost per unit cleared, charge avoided |
| Bid may exceed break-even | Yes, sized, capped, time-boxed | **Yes** — that is the ruling. Capped at the forward-cash ceiling, dated, and logged against the charge avoided |
| Top-of-search premium | The primary lever | Barred as a rank lever; a modifier is set only where that placement's own CPA sits inside the ceiling |
| Exact match | The vehicle for the push | Proven converters only |
| Success looks like | A rank number | An empty shelf |

**Two layers run at once, and they are not the same campaign.**

**The proven-converter layer** holds terms with demonstrated conversion on this product. It keeps them at the ceiling and defends the orders already being won.

**The reach layer** buys width cheaply — the wide, cheap net. It exists because on aged stock a wide cheap net beats a narrow expensive one: the lane is buying volume at a price where losing costs little, not position.

---

## Part 2 — Build classes

Propose from this list. A build that is not one of these is a new concept and goes to the canon first.

| Class | What it is | Match / targeting | Bid basis |
|---|---|---|---|
| **B1 · Catch-all auto** | One auto campaign, four targeting groups isolated | close, loose, substitutes, complements | Floor, rising only where a group converts |
| **B2 · Catch-all manual** | Wide manual net on the head and body terms | Broad, and Phrase where Broad over-catches | At or under the ceiling |
| **B3 · Attribute groups** | One campaign per product attribute the stock actually has — size, tier count, material, colour | Phrase, Broad on the widest | Tiered by keyword, never by price on the same keyword |
| **B4 · Proven converters** | Terms with demonstrated conversion on this product | Exact | Ceiling × that term's own CVR |
| **B5 · Sponsored Brands** | Product Collection across Broad, Phrase, Exact and ASIN targeting — not Phrase-only | Mixed | Its own ceiling; SB clicks price differently from SP |
| **B6 · Category targeting** | The categories this product genuinely sits in, with refinements | SP category targets | At or under the ceiling |
| **B7 · Sponsored Display** | Competitor, category, views, purchase, audiences | Product and audience | Its own ceiling |

### The operating floors apply to every class

| Floor | Default |
|---|---|
| Minimum bid | **$0.25** |
| Minimum daily budget | **$5.00** |

A proposed campaign that cannot justify $5/day is not proposed. A bid the ceiling puts below $0.25 is written at $0.25, and the difference is logged as accepted over-ceiling spend against the charge it avoids. **Nothing is ever staged between zero and the floor** — that produces a lane that spends and cannot deliver.

**Intensity — how many classes open — is set by the charge band. Whether any open at all is set by the clearability gate, never by the charge.** The largest charge in a portfolio is frequently the least clearable stock in it, because low velocity is what aged it. A large charge on a closed lane is a reason to clear faster by another route, not to spend into it.

### Separation rules

These are what make the numbers readable afterwards, and every one is checkable from the file.

- **One keyword lives in one campaign per ad product.** An SP and an SB instance of the same term is coverage, not self-competition; two SP instances is self-competition and raises our own clearing price.
- **Proven converters are negative-exacted out of every reach campaign**, the same day the reach campaign opens.
- **Any term promoted from discovery into capture is added as negative exact to the campaign that found it**, the same day.
- **Bid tiers separate by keyword, never by price on the same keyword.** The point of a tier is to reach different keywords at different prices, not to bid twice on one.
- **Bidding strategy is fixed or down-only.** Up-and-down can breach the ceiling at auction, which makes the ceiling unenforceable from the file.
- **Placement multipliers per campaign per placement**, from that campaign's own data — never blanket, in either direction.
- **Archetype B (variation overstock): aged children only.** No parent, no healthy child, in any SKU list or group. The healthy children subsidise the fix; their economics and price anchors are not spent on it.

### The relevance gate

Strip terms describing a material, feature or size the product does not have. Buying traffic that expects something we do not offer converts, and then returns — which on a clearance product costs twice, because the unit re-enters the aged pool and re-accrues charge.

---

## Part 3 — The added tabs

The Final Bulk is filled in place. Anything the plan proposes to *create* goes in an added tab, one per ad product, never mixed.

### New-campaign tabs — `New SP`, `New SB`, `New SD`

One row per campaign to build, carrying at minimum:

| Column | Why |
|---|---|
| Build class | B1–B7 above |
| Campaign name | House naming convention |
| Targeting type / match | What it buys |
| SKU set | Which children, and only which children |
| Keyword or target set | With the tier each sits in |
| Bid | And the ceiling arithmetic behind it |
| Daily budget | And what it is sized against |
| Bidding strategy | Fixed or down-only |
| Placement modifiers | Set per placement, or 0% with the reason |
| Gate | Live now, or the named condition it waits on |
| Reasoning | The evidence, with the number in it |

**Gate what depends on something else.** Group into tranches — live now, gated on brand registry, gated on a reprice, gated on a quality fix — with the gate named on the campaign row. A campaign with an unnamed dependency gets built and then sits broken.

### The negation tab — `Negatives`

| Column | Why |
|---|---|
| Search term | |
| Campaign it goes into | A negative has a home, not a product |
| Match type | Negative exact or negative phrase |
| Mode | Reactive (it failed), steering (a sibling owns it), structural (own catalogue, irrelevant) |
| Clicks / orders / spend | The evidence |
| Evidence standard met | Which line it passed |

**Nothing is negated on performance below the click line** — 15 clicks with no orders at ordinary click prices, 20–25 where clicks cost about $0.15 or less. Below that the term has not had its chance and it stays. Reaching the line is a review trigger, not an automatic kill: look at the term itself before deciding.

Structural negatives — own catalogue, a material we do not sell, a size we do not stock — are exempt from any click count. Those are relevance decisions and are made on sight. The tab says which basis applied.

**Where nothing qualifies, the tab is delivered empty with the reason on it.** An empty negation tab that explains itself is a finding; a missing one is an omission.

---

## Part 4 — What a clearance build never proposes

- A rank target, or any campaign whose success measure is a rank position
- A top-of-search premium bought to hold position
- Exact-match expansion onto unproven terms
- A bid above the **forward-cash ceiling** — above break-even is expected and allowed; above the ceiling is not
- A family-wide budget move, a shared coupon, or a parent re-point on an overstock archetype
- More campaigns than the clearability gate says can be fed
- Any campaign, bid or budget below the operating floors
- A narrow term set justified as cost control — width is the point, and the bid is the cost control
- A hard cut or a pause on a campaign that is producing orders — those move 5 cents a cycle
- A budget reduction offered as an efficiency saving — waste is removed at target level, and a cut to an unspent cap saves nothing
