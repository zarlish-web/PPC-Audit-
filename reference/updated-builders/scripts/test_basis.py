"""
test_basis.py — every test here is a defect that shipped once.

The test name is the failure, not the function. A test that passes proves
the file cannot ship that defect again; a test that has never failed on a
known-bad case proves nothing, so each one asserts the wrong answer is
actually rejected rather than only that the right one is produced.

Run: python3 test_basis.py
"""

import sys
from basis import (Child, resolve_basis, route_from_product_ads, affordable_cpc,
                   base_bid, size_premium, apply_bounds, stage, base_floor,
                   stage_base_down, size_placement_lift, ROS_ENTRY_CLICKS,
                   UNIT_SAMPLE_FLOOR, MODIFIER_CAP,
                   FLAT_CLICK_CEILING, BASE_FLOOR_MIN, BASE_FLOOR_MAX, PDP_CLICK_TARGET)

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILS.append(name)


def queens():
    """The real shape that broke a build: one thin outlier among sound peers."""
    return [
        Child("NAVY", "QUEEN", "navy", units_60d=2, aov=52.95, cm2_own=24.67,
              stock=54, inbound=216, doh=1890, cvr=5.3),
        Child("GRAPHITE", "QUEEN", "grey", units_60d=143, aov=37.95, cm2_own=11.78,
              stock=3, inbound=0, doh=1, cvr=5.3),
        Child("PINK", "QUEEN", "pink", units_60d=47, aov=37.52, cm2_own=8.34,
              stock=10, inbound=0, doh=13, cvr=5.3),
        Child("CREAM", "QUEEN", "cream", units_60d=13, aov=37.95, cm2_own=-1.64,
              stock=150, inbound=0, doh=620, cvr=5.3),
    ]


def test_thin_sample_does_not_set_the_basis():
    """A contribution from 2 units priced 597 rows. It must not again."""
    d = resolve_basis(queens())
    check("thin child does not use its own inflated figure",
          d["NAVY"].cm2 != 24.67, f"got {d['NAVY'].cm2}")
    check("thin child falls back to a peer median",
          d["NAVY"].basis_source == "peer-median", d["NAVY"].basis_source)
    check("the peer median excludes negative-contribution children",
          d["NAVY"].cm2 > 0, f"got {d['NAVY'].cm2}")
    check("a child clearing the unit floor keeps its own figure",
          d["GRAPHITE"].cm2 == 11.78 and d["GRAPHITE"].basis_source == "own")
    check("the sample is named in every basis note",
          all(str(c.units_60d) in c.basis_note for c in d.values()))


def test_peer_median_never_raises_a_thin_child():
    """A thin child must not be lifted by the median above its own claim."""
    kids = [Child("THIN", "KING", units_60d=2, cm2_own=3.00, cvr=5.5, doh=500),
            Child("A", "KING", units_60d=40, cm2_own=12.00, cvr=5.5, doh=500),
            Child("B", "KING", units_60d=40, cm2_own=14.00, cvr=5.5, doh=500)]
    d = resolve_basis(kids)
    check("peer median is capped by the thin child's own figure",
          d["THIN"].cm2 == 3.00, f"got {d['THIN'].cm2}")


def test_no_peer_clears_the_floor():
    kids = [Child("SOLO", "TWIN", units_60d=8, cm2_own=8.03, cvr=6.9, doh=400)]
    d = resolve_basis(kids)
    check("with no eligible peer the child's own figure is used",
          d["SOLO"].cm2 == 8.03 and d["SOLO"].basis_source == "own-thin-no-peer")
    check("and the thin sample is stated, not hidden",
          "thin sample is named" in d["SOLO"].basis_note)


def test_aged_stock_runs_forward_cash():
    kids = [Child("AGED", "FULL", units_60d=1, cm2_own=-9.90,
                  forward_cash=9.61, cvr=6.8, doh=900)]
    d = resolve_basis(kids)
    check("aged stock uses forward cash, not contribution",
          d["AGED"].cm2 == 9.61 and d["AGED"].basis_source == "forward-cash")
    check("and the seam is named on the row",
          "forward-cash economics" in d["AGED"].basis_note)


def test_routing_reads_product_ads_not_the_name():
    """212 of 251 campaign names disagreed with their own product ads."""
    ads = {"CAMPAIGN-FOR-GRAPHITE": [{"sku": "NAVY", "state": "enabled"},
                                     {"sku": "GRAPHITE", "state": "paused"}]}
    live, disagrees = route_from_product_ads("CAMPAIGN-FOR-GRAPHITE", ads)
    check("routing returns what the ads serve", live == {"NAVY"}, str(live))
    check("and flags the disagreement with the name", disagrees)


def test_per_unit_is_not_a_per_click_ceiling():
    """$8.99 a click passed once because the unit earned $17.35."""
    c = Child("K", "KING", units_60d=40, cm2_own=17.35, cvr=5.5, doh=500)
    resolve_basis([c])
    top = affordable_cpc(c, "top")
    check("top-of-search affordable is far below the unit contribution",
          top is not None and top < c.cm2 / 5, f"got {top} against cm2 {c.cm2}")
    b = base_bid(c)
    check("the base is the tighter of rest and product pages",
          b is not None and b <= top, f"base {b} vs top {top}")


def test_premium_is_sized_not_defaulted():
    """185 premiums once sat at exactly 350% because every band returned max."""
    lifts = {size_premium(r, 10)[0] for r in (8, 11, 15, 20, 40, 90, 300)}
    check("premiums spread across the roster", len(lifts) > 3, str(sorted(lifts)))
    check("a rank at target earns no premium", size_premium(10, 10)[0] == 0.0)
    check("no rank on record earns no premium", size_premium(None, 10)[0] == 0.0)
    check("the reason is stated, not implied",
          "no position is being bought" in size_premium(None, 10)[1])


def test_objective_sets_the_price_bound_not_the_cap():
    """A 25% premium cap once held a ranking row at $1.54 against $2.16 clearing."""
    c = Child("Q", "QUEEN", units_60d=40, cm2_own=6.21, cvr=11.4, doh=500)
    resolve_basis([c])
    b = base_bid(c)
    rank = apply_bounds(b, lift=2.0, child=c, objective="Ranking")
    prof = apply_bounds(b, lift=2.0, child=c, objective="Profit")
    aff = affordable_cpc(c, "top")
    check("a Ranking row may price above what the placement affords",
          rank["top_price"] > aff, f'{rank["top_price"]} vs affordable {aff}')
    check("a non-Ranking row may not", prof["top_price"] <= aff + 0.01,
          f'{prof["top_price"]} vs affordable {aff}')
    check("the non-Ranking bound names itself", "affords" in prof["binding"], prof["binding"])
    check("both still respect the per-unit bound",
          rank["top_price"] <= c.cm2 + 0.01 and prof["top_price"] <= c.cm2 + 0.01)
    check("the modifier cap is the platform maximum", MODIFIER_CAP == 900)


def test_base_floor_and_staged_descent():
    """The floor is hard, judged in range, and staging stops on two conditions."""
    c = Child("Q", "QUEEN", units_60d=40, cm2_own=6.21, cvr=11.4, doh=500)
    resolve_basis([c])
    check("the floor sits inside the stated range",
          BASE_FLOOR_MIN <= base_floor() <= BASE_FLOOR_MAX, str(base_floor()))
    r = stage_base_down(1.40, 0.38, c)
    check("a big leak takes a bigger step", r["base"] < 1.40 and not r["hold"], str(r))
    check("but never past the floor", r["base"] >= base_floor() - 0.005, str(r))
    check("the step is explained, not just taken", "20% target" in r["why"])
    ok = stage_base_down(1.40, 0.18, c)
    check("at or under 20% product-page clicks, staging stops", ok["hold"], str(ok))
    ex = stage_base_down(base_floor(), 0.35, c)
    check("at the floor with a leak still open, the lever is exhausted",
          ex.get("exhausted") is True, str(ex))
    check("and the next moves are named", "Phrase" in ex["why"] and "Fixed" in ex["why"])


def test_zero_delivery_holds_the_base():
    """Cutting the base of a row that is not delivering makes delivery worse."""
    c = Child("Q", "QUEEN", units_60d=40, cm2_own=6.21, cvr=11.4, doh=500)
    resolve_basis([c])
    r = stage_base_down(1.40, 0.45, c, delivering=False)
    check("a non-delivering row holds its base", r["hold"] and r["base"] == 1.40, str(r))
    check("and the reasoning says why", "no distribution to fix" in r["why"])
    check("and points at the 60-day history", "60-day" in r["why"])


def test_bounds_bind_in_order_and_name_the_binding_one():
    c = Child("N", "QUEEN", units_60d=40, cm2_own=10.06, cvr=5.3, doh=500)
    resolve_basis([c])
    r = apply_bounds(base=0.41, lift=0.25, child=c)
    check("top price never exceeds the unit contribution",
          r["top_price"] <= c.cm2 + 0.01, str(r))
    check("top price never exceeds the flat ceiling",
          r["top_price"] <= FLAT_CLICK_CEILING, str(r))
    check("the binding constraint is named", bool(r["binding"]), str(r))
    # A base above what the placement affords is a defect the modifier cannot
    # fix — it must be caught, not silently passed through at 0%.
    tiny = Child("T", "TWIN", units_60d=40, cm2_own=0.50, cvr=6.9, doh=500)
    resolve_basis([tiny])
    r2 = apply_bounds(base=1.00, lift=0.25, child=tiny)
    check("an unaffordable base is flagged, not passed at 0%",
          r2.get("base_breach") is True, r2["binding"])
    check("and the breach names both figures", "$1.00" in r2["binding"] and "$0.06" in r2["binding"])
    # a base correctly derived for the same child must pass cleanly
    good = apply_bounds(base=base_bid(tiny), lift=0.25, child=tiny)
    check("a derived base solves without breaching",
          not good.get("base_breach"), good["binding"])


def test_staging_commits_both_steps():
    """A file that writes step one and defers step two records half a decision."""
    check("a move inside the cap does not stage", stage(1.00, 0.90) == [0.90])
    s = stage(1.25, 0.58)
    check("a move beyond the cap returns two committed steps",
          len(s) == 2 and s[-1] == 0.58, str(s))
    check("step one respects the correction cap",
          abs(s[0] - 1.25) / 1.25 <= 0.2501, str(s))
    up = stage(0.40, 1.00)
    check("staging works upward too", len(up) == 2 and up[-1] == 1.00, str(up))


def test_inventory_zone_and_traffic_gate():
    red = Child("R", "QUEEN", units_60d=143, cm2_own=11.78, stock=3, inbound=0, doh=1, cvr=5.3)
    green = Child("G", "QUEEN", units_60d=40, cm2_own=12.00, stock=74, inbound=126, doh=740, cvr=5.3)
    loss = Child("L", "QUEEN", units_60d=40, cm2_own=-1.64, stock=150, inbound=0, doh=620, cvr=5.3)
    resolve_basis([red, green, loss])
    check("a child under 21 days with nothing inbound is Red", red.zone == "Red", red.zone)
    check("inbound stock makes a child Green", green.zone == "Green", green.zone)
    check("Red children may not receive traffic", not red.may_receive_traffic)
    check("a loss-making child may not receive traffic", not loss.may_receive_traffic)
    check("a healthy child may", green.may_receive_traffic)


def test_peer_median_never_rescues_a_negative_child():
    """A thin child with a real loss must not be made positive by its peers.

    Caught against live data: four children with negative contribution were
    lifted into eligibility by a healthy sibling's median, which would have
    opened traffic to products losing money on every unit.
    """
    kids = [Child("LOSS", "FULL", units_60d=6, cm2_own=-27.06, cvr=6.8, doh=620),
            Child("A", "FULL", units_60d=19, cm2_own=11.29, cvr=6.8, doh=500),
            Child("B", "FULL", units_60d=40, cm2_own=11.20, cvr=6.8, doh=500)]
    d = resolve_basis(kids)
    check("a negative child keeps its own figure",
          d["LOSS"].cm2 == -27.06, f"got {d['LOSS'].cm2}")
    check("and is barred from traffic", not d["LOSS"].may_receive_traffic)
    check("and the loss is named as a finding",
          "raised not absorbed" in d["LOSS"].basis_note)
    check("while a healthy thin child still gets the median",
          resolve_basis([Child("THIN", "FULL", units_60d=2, cm2_own=9.00, cvr=6.8, doh=500),
                         Child("A", "FULL", units_60d=19, cm2_own=11.29, cvr=6.8, doh=500),
                         Child("B", "FULL", units_60d=40, cm2_own=11.20, cvr=6.8, doh=500)]
                        )["THIN"].cm2 == 9.00)


def test_placement_lift_is_sized_not_jumped():
    """The ceiling is a maximum, not a destination — for ROS, non-ranking TOS,
    and both placements on discovery, which may never use a rank gap."""
    base, ceiling, pdp = 0.50, 1.50, 8.0
    below, why = size_placement_lift(9, 20.0, pdp, ceiling, base)
    check("under the entry condition it holds at base", below == base, str(below))
    check("and says it is held, not suppressed", "rather than suppressed" in why)
    weak, _ = size_placement_lift(30, 7.0, pdp, ceiling, base)
    check("converting below the product-page rate holds at base", weak == base, str(weak))
    nodata, why2 = size_placement_lift(30, None, pdp, ceiling, base)
    check("no readable rate holds at base", nodata == base and "held at base" in why2)
    a, _ = size_placement_lift(30, 9.0, pdp, ceiling, base)
    b, _ = size_placement_lift(30, 12.0, pdp, ceiling, base)
    c, whyc = size_placement_lift(30, 20.0, pdp, ceiling, base)
    check("a small excess earns a small lift", base < a < b, f"{a} then {b}")
    check("a large excess earns more", b < c, f"{b} then {c}")
    check("nothing exceeds the ceiling", c <= ceiling + 0.001, str(c))
    check("the lift states its arithmetic", "above the bar" in whyc and "ceiling is the maximum" in whyc)
    check("a roster shows a spread, not one value",
          len({a, b, c}) == 3, str({a, b, c}))


if __name__ == "__main__":
    for t in [v for k, v in sorted(globals().items()) if k.startswith("test_")]:
        print(f"\n{t.__name__}")
        t()
    print(f"\n{'='*60}")
    if FAILS:
        print(f"{len(FAILS)} FAILED: {FAILS}")
        sys.exit(1)
    print("all basis tests pass")
