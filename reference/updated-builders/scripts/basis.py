"""
basis.py — the deterministic foundation every bid prices against.

This module owns the facts that have one right answer given the inputs:
contribution per child with its sample named, which child a campaign
actually advertises, whether that child may receive traffic, and the four
bounds any bid must respect.

It exists because these were re-derived by hand every cycle and got
re-derived wrong: a contribution from 2 units priced 597 rows, routing
inferred from campaign names disagreed with the account's own product-ad
rows on 212 of 251 campaigns, and a per-unit figure was used as a
per-click ceiling. None of those are judgement calls. They are arithmetic
and lookups, and a machine does not forget them on the fourth pass.

Nothing here writes prose or decides an objective. It returns facts with
their provenance attached, so the reasoning layer can state where each
number came from instead of asserting it.
"""

from dataclasses import dataclass, field
from typing import Optional, Iterable

# ---------------------------------------------------------------- constants
# A rate needs a sample. The click floor was always applied; the unit floor
# was not, and that is how a 2-unit contribution came to price 597 rows.
UNIT_SAMPLE_FLOOR = 10
CLICK_SAMPLE_FLOOR = 15

# Inventory zones, in days of cover. Red is same-day re-point, not next cycle.
RED_MAX_DAYS = 21
YELLOW_MAX_DAYS = 60

# The objective sets the price bound, not the modifier cap. A Ranking row may
# take its top-of-search price above the affordable ceiling to buy rank; every
# other objective stays inside it, whatever modifier gets there. An earlier
# version capped every premium at 25% over affordable, which capped a ranking
# row at $1.54 against a $2.16 clearing price — funding the term and not the
# position.
MODIFIER_CAP = 900          # the platform maximum; bounds the mechanism, not the price
FLAT_CLICK_CEILING = 9.00   # account-wide; a child's own CM2 may only tighten it

# Below this the base can stop the campaign qualifying for auctions at all,
# before the modifier is ever applied. Judged within the range, not per campaign.
BASE_FLOOR_MIN = 0.35
BASE_FLOOR_MAX = 0.50

# Product pages take 71% of impressions and 33% of clicks. The target is a share
# of clicks, never of impressions; 20% sits at the observed floor.
PDP_CLICK_TARGET = 0.20

# Placement conversion multipliers, measured on this account. Replaceable
# per product — pass your own rather than editing these.
DEFAULT_PLACEMENT_FACTORS = {"top": 8.19 / 4.95, "rest": 1.0, "pdp": 3.77 / 4.95}


@dataclass
class Child:
    """One variation, with everything a bid needs and where it came from."""
    sku: str
    size: Optional[str] = None
    colour: Optional[str] = None
    units_60d: int = 0
    aov: Optional[float] = None
    cm2_own: Optional[float] = None       # this child's own arithmetic
    stock: int = 0
    inbound: int = 0
    doh: Optional[float] = None
    forward_cash: Optional[float] = None  # aged stock runs this, not CM2
    cvr: Optional[float] = None

    # filled by resolve_basis
    cm2: Optional[float] = None
    basis_source: str = ""
    basis_note: str = ""

    @property
    def zone(self) -> str:
        if self.inbound > 0:
            return "Green"
        if self.doh is None:
            return "No data"
        if self.doh < RED_MAX_DAYS:
            return "Red"
        if self.doh < YELLOW_MAX_DAYS:
            return "Yellow"
        return "Green"

    @property
    def may_receive_traffic(self) -> bool:
        return self.zone in ("Green", "Yellow") and (self.cm2 or 0) > 0


def resolve_basis(children: Iterable[Child]) -> dict:
    """Give every child a contribution basis, and name the sample behind it.

    A child at or above the unit floor uses its own figure. Below it, the
    basis is the median of same-size children that clear the floor AND earn
    a positive contribution — capped never to exceed what the thin sample
    itself claims, so a 2-unit outlier cannot raise a bid by being an
    outlier. Where no peer clears the floor, the child's own figure is used
    and the thin sample is named rather than hidden.

    Aged stock runs forward cash instead: a different question with a
    different sample, so it short-circuits before any of the above.
    """
    kids = list(children)
    by_size: dict = {}
    for c in kids:
        by_size.setdefault(c.size, []).append(c)

    for c in kids:
        if c.forward_cash is not None:
            c.cm2 = c.forward_cash
            c.basis_source = "forward-cash"
            c.basis_note = (
                f"{c.sku} is aged stock, so it runs forward-cash economics rather than "
                f"contribution — every unit sold returns money and stops paying storage."
            )
            continue

        peers = [
            p for p in by_size.get(c.size, [])
            if p.units_60d >= UNIT_SAMPLE_FLOOR
            and p.cm2_own is not None and p.cm2_own > 0
        ]

        if c.units_60d >= UNIT_SAMPLE_FLOOR and c.cm2_own is not None:
            c.cm2 = c.cm2_own
            c.basis_source = "own"
            c.basis_note = (
                f"{c.sku} contribution ${c.cm2_own:.2f} a unit, from {c.units_60d} units "
                f"sold — a sample that carries a rate."
            )
        elif peers:
            med = sorted(p.cm2_own for p in peers)[len(peers) // 2]
            # A thin sample is uncertain, not automatically better than it
            # looks. Where the child's own arithmetic is NEGATIVE, the peer
            # median must not rescue it: a loss is a finding about this
            # child's fees or price, and substituting a healthy sibling's
            # figure would open traffic to a child that loses money on every
            # unit. The cap runs in both directions — never above what the
            # thin sample claims, and never rescued from below it.
            if c.cm2_own is not None and c.cm2_own <= 0:
                c.cm2 = c.cm2_own
                c.basis_source = "own-negative"
                c.basis_note = (
                    f"{c.sku} sold only {c.units_60d} units, but its own arithmetic reads "
                    f"${c.cm2_own:.2f} — a loss. A peer median is a fallback for an "
                    f"uncertain rate, not a way to make a negative contribution positive, "
                    f"so this child's own figure stands and it may not receive traffic. "
                    f"The loss itself is a fee or price finding, raised not absorbed."
                )
                continue
            use = min(c.cm2_own, med) if (c.cm2_own or 0) > 0 else med
            c.cm2 = use
            c.basis_source = "peer-median"
            own = f"${c.cm2_own:.2f}" if c.cm2_own is not None else "no figure"
            c.basis_note = (
                f"{c.sku} sold only {c.units_60d} units, too thin to carry a contribution. "
                f"The basis is ${use:.2f}, the median of the {len(peers)} {c.size} children "
                f"clearing {UNIT_SAMPLE_FLOOR} units with a positive contribution; this "
                f"child's own arithmetic reads {own} and is not used."
            )
        else:
            c.cm2 = c.cm2_own
            c.basis_source = "own-thin-no-peer"
            c.basis_note = (
                f"{c.sku} sold {c.units_60d} units and no sibling in its size clears "
                f"{UNIT_SAMPLE_FLOOR} units with a positive contribution, so there is no "
                f"peer median to fall back to. Its own figure is used and the thin sample "
                f"is named rather than hidden."
            )
    return {c.sku: c for c in kids}


def route_from_product_ads(campaign: str, product_ads: dict) -> tuple:
    """Which child a campaign advertises, read from its product-ad rows.

    Never from the campaign name. On a real account the two disagreed on
    212 of 251 campaigns, and one auto campaign named for a single SKU was
    running fifteen. Returns (enabled_skus, disagrees_with_name).
    """
    ads = product_ads.get(campaign, [])
    live = {a["sku"] for a in ads if a.get("state") == "enabled"}
    named = None
    for sku in {a["sku"] for a in ads}:
        if sku and sku.upper() in campaign.upper():
            named = sku
    return live, (named is not None and named not in live)


def affordable_cpc(child: Child, placement: str,
                   factors: Optional[dict] = None) -> Optional[float]:
    """What a click at this placement affords on this child.

    This is the per-click bound. A child's per-unit contribution is NOT a
    per-click ceiling — it breaks even only at 100% conversion — and using
    it as one is how an $8.99 click passed a check because the unit earned
    $17.35.
    """
    factors = factors or DEFAULT_PLACEMENT_FACTORS
    if child.cm2 is None or child.cm2 <= 0 or child.cvr is None:
        return None
    return round(child.cm2 * (child.cvr * factors[placement]) / 100, 2)


def base_bid(child: Child, factors: Optional[dict] = None) -> Optional[float]:
    """Bound 1 — the base is derived from the routed child, never inherited.

    It is the tighter of rest-of-search and product pages, because the base
    must be affordable at every placement it can serve; the premium for top
    of search lives in the modifier, not in the base.
    """
    factors = factors or DEFAULT_PLACEMENT_FACTORS
    vals = [affordable_cpc(child, p, factors) for p in ("rest", "pdp")]
    vals = [v for v in vals if v is not None]
    return min(vals) if vals else None


def size_premium(rank: Optional[float], target: Optional[float]) -> tuple:
    """A rank premium sized from this row's own gap, as a lift over affordable.

    No cap here: what the resulting price is allowed to be comes from the
    objective in apply_bounds(). A file where every row carries the same lift
    has sized nothing. No rank against a stated target means no position is
    being bought, so no premium is available.
    """
    if not rank or not target:
        return 0.0, "no rank against a stated target, so no position is being bought"
    ratio = rank / target
    if ratio <= 1.0:
        return 0.0, f"rank {rank:.0f} is at or past its target of {target:.0f}"
    lift = round((ratio - 1) * 0.05, 4)
    return lift, f"rank {rank:.0f} against a target of {target:.0f}, {ratio:.1f} times it"


def apply_bounds(base: float, lift: float, child: Child,
                 factors: Optional[dict] = None, objective: str = "Profit") -> dict:
    """The four bounds, in dependency order, returning the binding one.

    Order matters: a staged base moves the effective top-of-search price,
    so a modifier solved before the base is solved against a number that
    no longer exists.
    """
    factors = factors or DEFAULT_PLACEMENT_FACTORS
    aff_top = affordable_cpc(child, "top", factors)
    if aff_top is None or base <= 0:
        return {"modifier": 0, "top_price": None, "binding": "no payable contribution"}

    # The base itself must be affordable before a modifier is solved on it.
    # Without this, a base of $1.00 against a $0.06 affordable top returns a
    # 0% modifier and a $1.00 click — technically "no premium applied", and
    # sixteen times what the placement earns. The modifier cannot correct a
    # base that was never derived; it can only fail to make it worse.
    if base > aff_top:
        return {"modifier": 0, "top_price": round(base, 2),
                "affordable_top": aff_top,
                "binding": f"BASE UNAFFORDABLE — ${base:.2f} already exceeds the "
                           f"${aff_top:.2f} top of search affords on {child.sku}; "
                           f"re-derive the base before solving a modifier",
                "base_breach": True}

    want = aff_top * (1 + lift)
    binding = "the premium the rank gap supports"

    # A Ranking row may price above what the placement affords — that is the
    # authorised exception and it is what buys rank. Every other objective is
    # held to the affordable ceiling however large the modifier would be.
    if objective != "Ranking" and want > aff_top:
        want, binding = aff_top, f"the ${aff_top:.2f} top of search affords on {child.sku}"

    if want > child.cm2:
        want, binding = child.cm2, f"the ${child.cm2:.2f} a unit {child.sku} earns"
    if want > FLAT_CLICK_CEILING:
        want, binding = FLAT_CLICK_CEILING, "the flat account ceiling"

    mod = max(0, int((want / base - 1) * 100))
    if mod > MODIFIER_CAP:
        mod, binding = MODIFIER_CAP, f"the {MODIFIER_CAP}% modifier wall"

    return {"modifier": mod,
            "top_price": round(base * (1 + mod / 100), 2),
            "affordable_top": aff_top,
            "binding": binding}


def stage(current: Optional[float], target: float, cap: float = 0.25) -> list:
    """A move beyond the correction cap stages, with both steps committed now.

    Returning both steps matters: a file that writes step one and leaves
    step two to a later cycle has recorded half a decision.
    """
    if current is None or current <= 0:
        return [target]
    if abs(target - current) / current <= cap:
        return [target]
    step1 = round(current * (1 - cap) if target < current else current * (1 + cap), 2)
    return [step1, target]


def base_floor(clearing: Optional[float] = None, cap: int = MODIFIER_CAP) -> float:
    """The hard floor a base may not go below, judged within $0.35-$0.50.

    Below it, base-bid eligibility suppression becomes the risk: the campaign
    can stop qualifying for auctions before the modifier is ever applied, so
    it is not in the auction it appears to be in.

    Where a clearing price is known, the floor also has to leave the modifier
    room to reach it — base x (1 + cap) must clear. That rarely binds at a 900%
    cap but is checked rather than assumed.
    """
    floor = BASE_FLOOR_MIN
    if clearing:
        needed = clearing / (1 + cap / 100)
        floor = max(floor, min(needed, BASE_FLOOR_MAX))
    return round(floor, 2)


def stage_base_down(base: float, pdp_click_share: float, child: Child,
                    clearing: Optional[float] = None,
                    delivering: bool = True) -> dict:
    """One step of the staged descent. Returns the step, never the destination.

    The bound on step size is attribution: a move large enough that base,
    modifier and delivery all shift at once leaves the next reading unable to
    say which moved, and the cycle teaches nothing.
    """
    floor = base_floor(clearing)
    if not delivering:
        return {"base": base, "hold": True,
                "why": ("campaign and keyword both enabled with no clicks — the base is held and the "
                        "top-of-search modifier lifted instead. Cutting the base of a row that is not "
                        "delivering makes delivery worse; there is no distribution to fix on a row "
                        "with no distribution. Read the 60-day placement history before concluding "
                        "the mix is clean — a silent window is silent, not clean.")}
    if pdp_click_share <= PDP_CLICK_TARGET:
        return {"base": base, "hold": True,
                "why": f"product pages at {pdp_click_share:.0%} of clicks, at or under the 20% target"}
    if base <= floor + 0.005:
        return {"base": floor, "hold": True, "exhausted": True,
                "why": (f"base is at its ${floor:.2f} floor with product pages still at "
                        f"{pdp_click_share:.0%} of clicks — the pricing lever is exhausted. Next: "
                        f"switch to Fixed and raise the modifier in stages, then test the term in "
                        f"Phrase. Cutting further risks eligibility suppression and buys nothing.")}
    # step scales with the size of the leak, bounded so the result stays readable
    step = 0.30 if pdp_click_share > 0.30 else 0.15
    new = round(max(base * (1 - step), floor), 2)
    return {"base": new, "hold": False, "step": step,
            "why": (f"product pages at {pdp_click_share:.0%} of clicks against a 20% target, so the "
                    f"base steps from ${base:.2f} to ${new:.2f} and the modifier re-solves upward to "
                    f"hold the top-of-search price. Staged rather than dropped, so the next reading "
                    f"can attribute what moved.")}


# Rest of search and non-ranking top of search share one shape: a lift earned by
# fifteen clicks converting at or above the product-page rate, then SIZED by how
# far above that rate it converts — the ceiling is a maximum, not a destination.
ROS_ENTRY_CLICKS = 15


def size_placement_lift(clicks: int, cvr: Optional[float], pdp_cvr: Optional[float],
                        ceiling: float, base: float) -> tuple:
    """Lift a placement toward its own ceiling, sized to measured performance.

    Governs rest of search on every objective, non-ranking top of search, and
    both placements on Phrase, Broad, PAT and discovery — none of which may use
    a rank gap, because an auto campaign has no rank target and a modifier
    derived from one is a number with nothing behind it.

    Returns (price, why). Bad data or absent data holds at base: not suppressed
    below it, not lifted on expectation.
    """
    if not clicks or clicks < ROS_ENTRY_CLICKS:
        return base, (f"{clicks or 0} clicks on this placement, under the {ROS_ENTRY_CLICKS}-click "
                      f"entry condition — held at base, unmodified rather than suppressed, because "
                      f"nothing yet evidences a premium above base")
    if cvr is None or pdp_cvr is None or pdp_cvr <= 0:
        return base, "no conversion rate readable for this placement — held at base"
    if cvr < pdp_cvr:
        return base, (f"converting at {cvr:.2f} per cent against the {pdp_cvr:.2f} per cent "
                      f"product-page rate — below the bar, so it holds at base")
    # how far above the bar it converts decides how much of base->ceiling it earns
    excess = (cvr / pdp_cvr) - 1.0
    share = min(1.0, excess / 1.0)          # 2x the product-page rate earns the full range
    price = round(base + (ceiling - base) * share, 2)
    where = "the full range" if share >= 0.999 else f"{share:.0%} of the range"
    return price, (f"{clicks} clicks converting at {cvr:.2f} per cent against the {pdp_cvr:.2f} per "
                   f"cent product-page rate, {excess:.0%} above the bar — earning {where} between "
                   f"the ${base:.2f} base and the ${ceiling:.2f} ceiling, at ${price:.2f}. The "
                   f"ceiling is the maximum, not the destination.")
