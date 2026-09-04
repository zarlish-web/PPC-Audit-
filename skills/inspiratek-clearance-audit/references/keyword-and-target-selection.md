# Choosing keywords, ASINs, products and categories

What goes in each campaign, and why. Applies to SP and SB keyword campaigns, SP/SB product targeting, and category targeting.

The governing idea: **a campaign is clean when everything inside it wants the same thing.** One intent, one ASIN family, one search-volume band, and no keyword eating another keyword's traffic. Clean campaigns are how you find out what actually works; mixed campaigns average two answers into one number that describes neither.

---

## 1 · Keyword intent, and the ASIN that must serve it

Every keyword carries an intent about **what the shopper wants**. The ASIN we advertise on it has to match that intent, or we buy a click that was never going to convert — and on a clearance product a mismatched click that *does* convert usually comes back, which costs twice.

Sort every keyword into one of four classes:

| Class | Example | What the shopper has specified | ASIN that may serve it |
|---|---|---|---|
| **Generic** | *bamboo sheets* | Nothing but the product | **Any** of our children — pick on charge and stock, not on intent |
| **Size-specific** | *queen bamboo sheets* | Size only | Queen children only, any colour |
| **Colour-specific** | *black bamboo sheets* | Colour only | Black children only, any size |
| **Fully specific** | *black queen bamboo sheets* | Both | **Exactly** the black queen child |

**The rule: never advertise a child the keyword has ruled out.** A king ASIN on a queen keyword is a wasted click every time, and no bid makes it work.

**On generic keywords, intent does not choose the ASIN — so the clearance objective does.** Route generic traffic to the child carrying the most charge with enough stock to absorb the volume. Generic terms are usually the highest-volume terms we have, so this is where the aged pool actually drains.

### Three things that break this in practice

**Our colour name is not the shopper's colour word.** A SKU called *Midnight Black* has to be matched to the term *black*, and *Graphite Grey* to *grey* and *gray*. Build the synonym map once from the actual child names, and write it into the plan — otherwise colour routing silently misses half its terms.

**A size or colour with no aged stock has no campaign.** If the queen children are cleared and only king remains, every queen keyword is unbuildable this cycle. Say so in the plan rather than routing queen terms to a king ASIN because the keyword looked good.

**The refund gate outranks intent.** If the black children are FLOOR-tier on returns, the black keyword tier is not scaled even though the intent matches perfectly. Intent decides *which* ASIN; the gates decide *whether* it is funded at all.

---

## 2 · Campaign purity — one family per campaign

**A campaign that targets queen keywords carries queen ASINs and nothing else.** No king children in the SKU list, no king keywords in the target list.

This is not tidiness. Mixing them means the campaign's cost per unit is an average of two different products with two different conversion rates and possibly two different ceilings, and no decision can be taken from it. It also means the king ASIN quietly serves queen searches, because Amazon rotates the ads in an ad group.

Same for colour. Same for any attribute the keyword set is built around.

**Catch-all campaigns are the deliberate exception.** The auto campaigns and the wide manual net carry every eligible child, because their job is discovery across the whole product — not a clean read on one attribute. That exception is stated on the campaign row so nobody later "fixes" it.

---

## 3 · The cannibalisation check — the one people skip

**Inside one campaign, a shorter keyword will eat a longer one.** This is how the match types work, and it is mechanical rather than a matter of judgement.

| Match type | A captures B when… | Example |
|---|---|---|
| **Phrase** | A's words appear in B **as a contiguous run, in the same order** | *bamboo sheets queen* captures *bamboo sheets queen deep pocket* — but **not** *bamboo queen sheets*, because the order changed |
| **Broad** | A's words are **all present in B, in any order** | *bamboo sheets* captures *queen bamboo cooling sheets* |

So if both sit in one campaign, the short one wins nearly every auction, spends the budget, and the long one draws almost nothing. You then have no data on the long one and conclude — wrongly — that it does not work.

**The check, run before any campaign is staged:**

1. For each pair of keywords in the campaign, test whether one captures the other under that campaign's match type.
2. If it does, they cannot both live there. Put the **shorter, higher-volume** one in its own campaign and move the longer one to a different campaign — usually a lower search-volume tier, where it belongs anyway.
3. Re-run until no pair inside any campaign captures another.

**Where a long-tail term genuinely deserves its own read**, isolate it and negative-phrase it out of the campaign holding its parent. Otherwise the parent keeps taking the traffic no matter which campaign the child sits in.

---

## 4 · Search-volume tiering — why a big keyword must never sit with a small one

Put a 10,000-search keyword and a 200-search keyword in the same campaign and the big one absorbs essentially the whole budget. The small one gets a handful of impressions, never reaches the click line, and stays unreadable forever. **Tiering is not neatness; it is the only way the small terms ever get a chance to prove themselves.**

Use the house tiers, so the clearance build lines up with the phasing standard:

| Tier | Monthly search volume |
|---|---|
| **VHSV** | 10,000 and above |
| **HSV** | 1,000 – 9,999 |
| **MSV** | 500 – 999 |
| **LSV** | 100 – 499 |
| **VLSV** | Under 100 |

**One tier per campaign.** A campaign never spans two tiers, because the higher tier will always starve the lower.

**Budget follows the tier, not the other way round.** A VHSV campaign needs enough to buy meaningful volume; a VLSV campaign needs the $5 floor and little more. Sizing a VLSV campaign like a VHSV one buys nothing, because the volume simply is not there to buy.

---

## 5 · Campaign size, and how many campaigns you can actually afford

**Four to five keywords and four to five ASINs per campaign.** Small and clean, many of them — so every child gets real visibility rather than being buried behind a sibling that happens to convert slightly better.

Then the constraint nobody remembers until deployment:

```
maximum campaigns = budget available for new builds ÷ $5.00 minimum daily budget
```

The attribute matrix explodes fast. Five sizes × four colours × five volume tiers is 100 campaigns, which needs **$500/day minimum** just to keep them at the floor. If the budget is $150/day, the build is 30 campaigns and no more — and the plan says which 30 and why those.

**Prioritise, in this order:**

1. **Generic × VHSV/HSV** — the largest reachable volume, and any child can serve it
2. **The attribute tiers holding the most aged units** — clear the biggest pile first
3. **Fully-specific terms with proven conversion** — small volume, high intent, cheap
4. **Everything else**, as budget allows

A campaign that does not make the cut is listed as **proposed, not funded**, with the budget it would need. That way the next cycle can open it without re-deriving the whole build.

---

## 6 · Sponsored Brands

Same keyword logic, three differences:

- **SB clicks price differently from SP.** Compute its ceiling separately; do not inherit the SP bid.
- **One keyword may live in one SP campaign *and* one SB campaign.** That is coverage across ad products, not self-competition. Two SP instances of the same term is self-competition.
- **Product Collection carries three ASINs in the creative.** Choose them to match the campaign's intent — a queen keyword campaign shows queen children. The creative is part of the intent match, not decoration.

Run SB across Broad, Phrase, Exact and ASIN targeting, not Phrase alone.

---

## 7 · Product targeting (PAT) — which ASINs to conquest

We are buying a place on someone else's product page. The shopper is already looking at a competing product, so the only question is: **when they see us next to it, do we win?**

Target an ASIN when we beat it on something the shopper can see in the placement:

| Signal | Target when | Why it works on clearance |
|---|---|---|
| **Price** | Their price is above ours | A clearance product is usually discounted, so this is our strongest and most common edge |
| **Reviews** | Their review count is below ours | We look like the safer choice at a glance |
| **Rating** | Their star rating is below ours | Same, and it shows in the placement |
| **Relevance** | Same size, same material, same use | A mismatch converts and then returns |

**Do not target when the review moat is deep.** A competitor with 85,000 reviews against our 2,000 will not lose the comparison on price alone, and the click is spent regardless. Skip it and say so on the row, with both review counts, rather than leaving it looking unconsidered.

**Also worth targeting:** complements — products bought alongside ours, where we are an addition rather than a replacement. These convert lower but cost much less, which suits a clearance objective.

**Never target:** our own catalogue. Those go straight into the negatives as structural, on sight.

**Intent matching applies here too.** A queen-sized competitor ASIN gets our queen child, not our king.

Every PAT row carries the target, its price, rating and review count, our edge in one phrase, the entry bid, and the cap. A target with no stated edge is not a target — it is a guess.

---

## 8 · Category targeting — four strategies, run in parallel

Category targeting reaches shoppers browsing rather than searching, which is volume we cannot get any other way. On a clearance objective that is exactly what we want.

Run these as **separate campaigns**, never blended, so each strategy can be read on its own:

| Strategy | Refinement | What it buys |
|---|---|---|
| **C1 · Whole category** | None | Maximum reach, lowest precision — the wide cheap net |
| **C2 · Priced above us** | Price refinement set above our selling price | Shoppers comparing on price, where we win |
| **C3 · Fewer reviews than us** | Review-count refinement below our count | Shoppers comparing on trust, where we win |
| **C4 · Rated below us** | Star-rating refinement below our rating | Same, on the other visible signal |

C2 and C3 are usually the best value on a clearance product, because the discount that makes the stock move is also what wins those comparisons.

**Choose the category the product genuinely sits in**, not the widest one available. A category that describes the shelf we actually compete on converts; a broader parent category buys impressions from people shopping for something else.

**Refinements are checked against our own current numbers, not remembered ones.** Our price moves on a clearance product, so a "priced above us" refinement set against last month's price targets the wrong band.

---

## 9 · How aggressive to go

Aggression is not a preference. It is arithmetic against the clock:

```
required units per day = aged units remaining ÷ days available
current pace           = units per day actually shipping now
push multiple          = required ÷ current
```

The push multiple sets how much structure opens and how hard it is funded. A multiple near 1 needs maintenance; a multiple of 4 needs every class in the build.

**There is no artificial horizon and no target to pace against.** If the stock can clear sooner than the fee bracket demands, clear it sooner — the charge stops accruing the day the unit ships, and every day earlier is money kept. A horizon is a deadline not to miss, never a speed limit.

**What does cap it:** the ceiling, the operating floors, the stock gate, the refund gate, and the reach the market actually has. Aggression buys more *structure* and more *coverage* — more campaigns, more terms, more surfaces. It never buys a bid above the ceiling.

---

## 10 · The checks before anything is staged

Run these over the proposed build and report each as pass or fail with the evidence:

1. Every keyword's intent class is recorded, and every ASIN in its campaign matches that class
2. No campaign mixes two attribute families — one size family, one colour family
3. No keyword in a campaign captures another under that campaign's match type
4. No campaign spans two search-volume tiers
5. Every campaign holds 4–5 keywords and 4–5 ASINs, catch-alls excepted and marked
6. Campaign count × $5.00 does not exceed the budget available for new builds
7. Every routed child actually holds aged stock
8. No FLOOR-tier child is scaled, and no BLOCK-tier child carries spend
9. Every PAT target names the edge that justifies it, with the numbers
10. Category refinements are set against our current price, rating and review count
11. The colour and size synonym map is written down, not assumed
12. Proposed-but-unfunded campaigns are listed with the budget they would need
