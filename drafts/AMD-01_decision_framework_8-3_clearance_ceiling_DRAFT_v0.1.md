# AMD-01 — Amendment to `decision_framework.md` §8.3 and §9.7

**Target:** `pmp-optimization-sr` → `reference/decision_framework.md`
**Sections:** §8.3 (LTSF / Aged-Inventory Surcharge), §9.7 (LTSF-Clearance scenarios)
**Status:** DRAFT v0.1 — not ratified
**Raised:** 4 September 2026
**Reason:** the canon contradicts itself on aged stock, and the contradiction produces opposite plans on the same product

---

## 1 · The problem

Two documents in the corpus give opposite instructions for an LTSF-burdened SKU.

**`ppc-decision-reasoning` §4** says:

> *"Aged/LTSF SKUs run forward-cash economics and an efficient-sales objective; the deal is the primary lever, not ranking spend."*

Forward-cash economics counts the storage charge **avoided** by selling now, which raises what a click may cost.

**`decision_framework.md` §8.3** says the opposite:

> *"The clearance target is **break-even ACoS (RPC × BE)** — sell the aged stock out up to break-even, no further."*
> *"Under negative CM the LTSF answer is pricing (BM), not bids."*

And **§9.7** carries it into the scenario table:

> *"LTSF-flagged, negative CM → **ROUTE TO BM** — the answer is pricing, not bids."*

**This is not academic.** On a live product (Hanging Closet Organizer, 4 Sep 2026) the two readings produced completely different plans:

| Reading | Max click price | Verdict |
|---|---|---|
| §8.3 as written | $0.067 – $0.091 | Stop all advertising, route to pricing |
| Forward cash | $0.234 – $0.236 | Fund the clearance push |

Both children carried negative CM after the surcharge, so §8.3 as written authorised no bid work at all on a product with 233 charge-bearing units accruing $849.89/month.

## 2 · The ruling being recorded

Stated 4 September 2026:

> On a liquidation product, **PPC is the lever that moves the stock.** Spending a little beyond profitable is accepted, because the charge avoided is worth more than the margin given up. A negative contribution does **not** stop the push and does **not** by itself send the product to pricing.
>
> Break-even is **not discarded** — it is computed every cycle as the reference point, so nobody bids without knowing where profit ended.

## 3 · Why the canon already permits this

§3 of the same document, unchanged:

> *"the profit ceiling (RPC × BE / margin × CVR) caps every bid — **except the three labeled investment objectives (Ranking, Discovery, LTSF-Clearance), which may exceed BE only while capped, dated, and logged.**"*

So §3 already authorises LTSF-Clearance to exceed break-even. §8.3 then forbids it. **The amendment brings §8.3 into line with §3, rather than introducing anything new.**

## 4 · Proposed change to §8.3

**Current:**

> **LTSF-burdened SKU → clearance objective (ring-fenced, labeled, tagged separately in TACoS).** The clearance target is **break-even ACoS (RPC × BE)** — sell the aged stock out up to break-even, no further.

**Proposed:**

> **LTSF-burdened SKU → clearance objective (ring-fenced, labeled, tagged separately in TACoS).** The clearance target is the **forward-cash ceiling**: contribution plus the charge avoided over `min(2 months, months to clear at realised velocity)`. This is one of §3's three labeled investment objectives and may exceed break-even **while capped, dated and logged**.
>
> **Break-even ACoS and max profitable CPC are computed every cycle as the reference point, not as the cap.** Every bid above max profitable CPC states its subsidy per unit — `(bid − max profitable CPC) ÷ CVR` — against the charge avoided per unit. Where the subsidy exceeds the charge avoided, the gap is logged in dollars and routed to pricing.

**Current:**

> Under negative CM the LTSF answer is pricing (BM), not bids.

**Proposed:**

> Under negative CM the pricing question routes to Brand Management **as a parallel recommendation, alongside the push — never as a reason to withhold it.** A negative contribution is expected on aged stock and is what the forward-cash ceiling exists to price.

## 5 · Proposed change to §9.7

**Current row:**

| LTSF-flagged, negative CM | ROUTE TO BM — the answer is pricing, not bids |

**Proposed row:**

| LTSF-flagged, negative CM | CLEARANCE at the forward-cash ceiling, capped/dated/logged **+** ROUTE TO BM in parallel on pricing |

## 6 · What does not change

Deliberately minimal. These all stand exactly as written:

- **The stock gate.** GREEN → push; not GREEN → do not push, it clears naturally. *This gate is about how much stock remains, not about whether the maths is profitable.*
- **Never run a clearance push while the hero size is RED.** Clear the aged variation, protect the hero.
- **Exit clearance when stock clears below the surcharge threshold.**
- **Ring-fenced, labeled, tagged separately in TACoS.**
- §3's requirement that any above-BE spend is **capped, dated and logged**.
- The break-even formula itself, and the CVAR, negative-CM and staleness anchors.

## 7 · Flagged for the ratifier — points I interpreted rather than was told

1. **The stock gate survives.** I read it as a stock-level test, not an economics test, so the ruling does not touch it. If the intent was that a not-GREEN SKU may also be pushed, this needs a second amendment.
2. **`min(2, months to clear)` as the acceleration window.** The two-month default is the account's; the cap at real clearance time is my reasoning — a variation clearing in six weeks cannot avoid two months of charge. Not yet confirmed.
3. **S-A10 is dealt with separately** in AMD-02, because it lives in v4.0 rather than here. Ratifying one without the other leaves the conflict half-closed.

## 8 · What this unblocks

Every clearance product in the corpus. Until it is ratified, two readers of the same canon will size the same product's bids differently by a factor of three, and the one following §8.3 as written will stop advertising products the account intends to clear through advertising.

---

*Inspiratek & Ecotero LLC · Confidential · DRAFT — not ratified*
