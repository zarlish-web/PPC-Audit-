"""Light, shareable 'boards' version of the BFCM 2026 tracker (no embedded photos).

Reads the data block of competitor_dashboard.html (already built and verified) and writes boards.html:
start-here summary, a product board (US / CA, dropdown), BFCM 2025 lift by deal type, stock risk, deal prices and the
verification board.  Usage: python3 build_boards.py competitor_dashboard.html boards.html
"""
import json, os, statistics, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrub import scrub_obj

SRC, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
h = open(SRC).read()
i = h.index("const D = ") + len("const D = ")
P = json.loads(h[i:h.index("\nconst IMG")].rstrip().rstrip(";"))

KEEP = ("pid", "mkt", "brand", "tier", "title", "child", "size", "colour", "price", "lp", "bsr", "wk", "rating", "reviews", "str_show", "str_price",
        "bf_type", "bf_pre", "bf_low", "bf_disc_v", "bsr_lift_v", "cls", "cls_why", "mat", "gap", "rev")
comps = [{k: c.get(k) for k in KEEP} for c in P["comps"]]
for c in comps:
    c["title"] = (c["title"] or "")[:110]

products = []
for p in P["products"]:
    st = p.get("stock26") or None
    risk = []
    if st:
        risk = [{k: x.get(k) for k in ("asin", "size", "colour", "oh", "ib", "vel", "need", "short", "oos", "oosIn", "st")}
                for x in sorted(st["rows"], key=lambda x: -x["vel"]) if x["st"] in ("Short even with inbound", "Out of stock now")][:12]
    products.append({k: p.get(k) for k in ("key", "pid", "mkt", "short", "family", "role", "scope", "brand", "name", "title", "best", "bestLabel", "price",
                                            "u28", "lift", "tacos", "plan26", "da", "hk", "pc")} | {"notes": p.get("slack") or []}
                    | {"stock": ({k: st[k] for k in ("lift", "liftSrc", "onHand", "inbound", "need", "short", "counts")} if st else None), "risk": risk,
                       "vars": len(p["vars"])})

# BFCM 2025 rank lift by deal type (competitors with a measured rank change), per marketplace
lift = {}
for m in ("US", "CA"):
    rows = {}
    for c in P["comps"]:
        if c["mkt"] == m and c.get("bf_type") and isinstance(c.get("bsr_lift_v"), (int, float)):
            rows.setdefault(c["bf_type"], []).append(c["bsr_lift_v"])
    lift[m] = sorted(({"type": t, "median": statistics.median(v), "n": len(v),
                       "disc": statistics.median([c["bf_disc_v"] for c in P["comps"] if c["mkt"] == m and c.get("bf_type") == t and isinstance(c.get("bf_disc_v"), (int, float))] or [0])}
                      for t, v in rows.items() if len(v) >= 3), key=lambda r: -r["median"])

checks = json.load(open(os.path.join(HERE, "data", "verification_report.json")))
data = {"products": products, "comps": comps, "lift": lift, "summary": {m: {k: v for k, v in P["summary"][m].items() if k != "comps"} for m in P["summary"]},
        "checks": [{"name": c["name"].replace("the inventory planner", "the stock plan"), "checked": c["checked"], "bad": c["mismatches"], "status": c["status"]} for c in checks["checks"]],
        "fx25": next((p["fx25"] for p in P["products"] if p.get("fx25")), None), "built": "Oct 15, 2026"}
tpl = open(os.path.join(HERE, "boards_template.html")).read()
open(OUT, "w").write(tpl.replace("/*__DATA__*/null", json.dumps(scrub_obj(data), separators=(",", ":"), default=str)))
print(json.dumps({"products": len(products), "comps": len(comps), "bytes": os.path.getsize(OUT)}))
