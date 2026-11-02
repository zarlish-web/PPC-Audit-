"""Builds the BFCM 2026 PPC plan review page (for Joseph and Erik) as one self-contained HTML file.
Consolidates: the plan workbook (recalculated copy), the independent verification, the year-over-year analysis,
and the competitor tracker (product photos, demand read, stock, 2025 price comparison).
Usage: python3 build_review_page.py <recalculated plan.xlsx> <out.html>"""
import json, os, re, sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(HERE, "..", "competitor-tracker")
VER = os.path.join(HERE, "..", "verification")
WB = load_workbook(sys.argv[1], data_only=True)
OUT = sys.argv[2]

PN = json.load(open(os.path.join(HERE, "plan_numbers.json")))
VR = json.load(open(os.path.join(VER, "verify_results.json")))
YO = json.load(open(os.path.join(VER, "yoy_results.json")))
SRC = json.load(open(os.path.join(VER, "source", "account_pulls_2026-11-02.json")))
h = open(os.path.join(TR, "competitor_dashboard.html")).read(); i = h.index("const D = ") + 10
D = json.loads(h[i:h.index("\nconst IMG")].rstrip().rstrip(";"))
IMG = {}
for fn in ("images.js", "images2.js"):
    s = open(os.path.join(TR, fn)).read()
    for k, v in re.findall(r'"([A-Za-z0-9_]+)":"(data:image/[^"]+)"', s):
        IMG[k] = v

# ---------------- plan workbook: product rows, budget by day, rules, summary
bp, bd, ru, sm, ap = WB["Budget by product"], WB["Budget by day"], WB["Bid and placement rules"], WB["Summary"], WB["Ad types by product"]
rows_bp = {}
blk = None
for r in range(1, bp.max_row + 1):
    a = bp.cell(r, 1).value
    if a in ("United States (US$)", "Canada (C$)"):
        blk = "US" if a.startswith("United") else "CA"
    elif blk and a and a not in ("Product", "Total") and isinstance(bp.cell(r, 21).value, (int, float)):
        g = lambda c: bp.cell(r, c).value
        rows_bp[(blk, a)] = {"deal": g(2), "stage": g(3), "band_lo": g(4), "band_hi": g(5), "units_lo": g(6), "units_hi": g(7), "units_mid": g(8), "asp": g(9),
                             "sales": g(10), "be": g(11), "be80": g(12), "tacos_now": g(13), "factor": g(14), "sp_share": g(16), "base": g(17), "floor": g(18),
                             "cap": g(19), "plan_tacos": g(20), "budget": g(21), "budget_lo": g(22), "budget_hi": g(23), "per_day": g(24), "now_day": g(25),
                             "change": g(26), "check": g(27), "note": g(28),
                             "split": [ap.cell(r, c).value for c in (17, 18, 19, 20)], "spend14": [ap.cell(r, c).value for c in (2, 3, 4, 5)],
                             "sales_day14": ap.cell(r, 10).value, "status_now": ap.cell(r, 15).value}
    elif blk and a == "Total":
        rows_bp[(blk, "Total")] = {"sales": bp.cell(r, 10).value, "budget": bp.cell(r, 21).value, "plan_tacos": bp.cell(r, 20).value,
                                   "budget_lo": bp.cell(r, 22).value, "budget_hi": bp.cell(r, 23).value, "per_day": bp.cell(r, 24).value, "now_day": bp.cell(r, 25).value}
DAYS = ["Thu Nov 19", "Fri Nov 20", "Sat Nov 21", "Sun Nov 22", "Mon Nov 23", "Tue Nov 24", "Wed Nov 25", "Thu Nov 26", "Fri Nov 27", "Sat Nov 28", "Sun Nov 29", "Mon Nov 30"]
byday, daytot, weights = {}, {}, {}
blk = None
for r in range(1, bd.max_row + 1):
    a = bd.cell(r, 1).value
    if a in ("United States (US$)", "Canada (C$)"):
        blk = "US" if a.startswith("United") else "CA"; continue
    if not blk or not a:
        continue
    vals = [bd.cell(r, 3 + k).value for k in range(12)]
    if a == "Day weight (share of the 12 days)":
        weights[blk] = vals
    elif a == "Total":
        daytot[blk] = vals
    elif isinstance(vals[0], (int, float)) and not str(a).startswith("BFCM 2025"):
        byday[(blk, a)] = vals
rules, agent = [], []
sec = rules
for r in range(4, ru.max_row + 1):
    v = [ru.cell(r, c).value for c in range(1, 5)]
    if v[0] == "Who":
        sec = agent; continue
    if v[0] and v[2] and v[0] not in ("Area",):
        sec.append({"a": v[0], "b": v[1], "c": v[2], "d": v[3] or ""})
calls = [str(sm.cell(r, 1).value)[2:] for r in range(14, 40) if str(sm.cell(r, 1).value or "").startswith("• ") and "Tabs" not in str(sm.cell(r, 1).value)]
calls = [c for c in calls if not c.startswith(("Budget by product:", "Budget by day:", "Bid and placement", "Inputs:", "Ad types by product:", "2025 vs 2026 check:"))]

# ---------------- per product
TRK = {(p["mkt"], int(p["pid"])): p for p in D["products"]}
VP = {(p["mkt"], p["name"]): p for p in VR["products"]}
YOY = {(m, r["pid"]): r for m in ("US", "CA") for r in YO["markets"][m]["rows"] if isinstance(r["pid"], int)}
BFC = {(r["market"], r["pid"]): r for r in YO["bfcm"]}
PNI = {(p["mkt"], p["pid"]): p for p in PN}
FAMILY = lambda n: ("CooLinens" if n.startswith("CooLinens") else "Sleephoria" if n.startswith(("Sleephoria", "Sleep Sanctuary")) else "Decolure")
prods = []
for (m, name), b in rows_bp.items():
    if name == "Total":
        continue
    v = VP[(m, name)]; pid = v["pid"]; t = TRK.get((m, pid), {}); pl = PNI.get((m, pid), {})
    st = t.get("stock26") or {}
    vrows = []
    for x in sorted(t.get("vars") or [], key=lambda x: -(x.get("u28") or 0))[:8]:
        srow = next((r_ for r_ in st.get("rows", []) if r_.get("asin") == x.get("asin")), {})
        vrows.append({"label": " ".join(z for z in (x.get("size"), x.get("colour")) if z), "u28": x.get("u28"), "price": x.get("price"), "deal": x.get("deal"),
                      "p25": x.get("p25"), "oh": srow.get("oh"), "vel": srow.get("vel"), "st": srow.get("st"), "img": x.get("img") if x.get("img") in IMG else None})
    counts = (st.get("counts") or {})
    y = YOY.get((m, pid), {}); bf = BFC.get((m, pid), {})
    rules_apply = []
    nm_short = name.replace("Decolure ", "")
    boost_txt = " ".join(r_["c"] for r_ in rules if r_["b"].startswith("Deal start"))
    if b["status_now"] and b["status_now"].startswith("Over"):
        rules_apply.append("Over its cap today: no bid raises; bring TACoS under the cap before Nov 19.")
    if (m, name) in (("US", "Decolure Bamboo 4 Pc"), ("CA", "Decolure Bamboo 4 Pc"), ("CA", "Decolure Bamboo 6 Pc")):
        rules_apply.append("Hero with room under the cap: +20% on converting exact-match keywords at deal start; top-of-search +50% (+100% on Black Friday and Cyber Monday).")
    if (m, name) in (("US", "Decolure Bamboo 6 Pc"), ("US", "Decolure Satin 4 Pc")):
        rules_apply.append("Hero at or just over its cap: raise bids and add the top-of-search boost only once daily TACoS is under the cap.")
    if pl.get("ld"):
        rules_apply.append(f"Lightning Deal on {pl.get('deal_dates')}: +50% bids and 4x the normal day budget for the deal hours only.")
    if not pl.get("deal_type"):
        rules_apply.append("No deal: hold today's daily spend (cut to the cap if above it); no BFCM increase.")
    if b["plan_tacos"] == 0:
        rules_apply.append("No ads beyond brand defence: break-even at the deal price is too thin.")
    if b["split"][2] and b["split"][2] > 1:
        rules_apply.append("Runs SB video: keep deal-badge creative live; cut SB video first if over the cap.")
    rules_apply.append("Agent every hour: pace vs the day's budget, TACoS vs cap, stop ads on any out-of-stock size.")
    pc = t.get("pc") or {}
    prods.append({
        "id": f"{pid}-{m}", "mkt": m, "pid": pid, "name": name, "family": FAMILY(name), "role": t.get("role"), "img": t.get("img") if t.get("img") in IMG else None,
        "stage": b["stage"], "band": [b["band_lo"], b["band_hi"]], "deal": pl.get("deal_type"), "deal_dates": pl.get("deal_dates"), "ld": bool(pl.get("ld")),
        "deal_price": pl.get("deal_price"), "cur_price": pl.get("cur_price"), "asp": b["asp"],
        "units": [b["units_lo"], b["units_hi"], b["units_mid"]], "lift": pl.get("lift"), "lift_src": pl.get("lift_src"),
        "u28_day": (v["u28"] or 0) / 28, "vel": v["vel"], "pace_now": v["pace14_units_per_day"], "sales": b["sales"],
        "be": b["be"], "cap": b["cap"], "tacos_now": b["tacos_now"], "factor": b["factor"], "floor": b["floor"], "plan_tacos": b["plan_tacos"],
        "budget": b["budget"], "budget_lo": b["budget_lo"], "budget_hi": b["budget_hi"], "per_day": b["per_day"], "now_day": b["now_day"], "change": b["change"],
        "split": b["split"], "spend14": b["spend14"], "sp_share": b["sp_share"], "check": b["check"], "note": b["note"], "status_now": b["status_now"],
        "budget_pace": v.get("alt_budget"), "days": byday.get((m, name)),
        "tacos25_pre": pl.get("tacos25_pre"), "tacos25_bf": pl.get("tacos25_bf"),
        "bf25": {"sales": bf.get("sales25"), "adv": bf.get("adv25"), "group": bf.get("class")},
        "yoy": {"group": y.get("class"), "sales25": y.get("sales25"), "sales26": y.get("sales26"), "ads25": y.get("adv25"), "ads26": y.get("adv26"),
                "sp25": y.get("sp25"), "sp26": y.get("sp26"), "nonsp25": y.get("nonsp25"), "nonsp26": y.get("nonsp26")},
        "stock": {"on_hand": st.get("onHand"), "inbound": st.get("inbound"), "need": st.get("need"), "short": st.get("short"), "counts": counts},
        "price_cmp": {"paid25": pc.get("paid25"), "deal26": pc.get("deal26"), "chg": pc.get("chg") if isinstance(pc, dict) else None},
        "vars": vrows, "rules": rules_apply,
    })
prods.sort(key=lambda p: (p["mkt"] != "US", -(p["budget"] or 0)))
used = {p["img"] for p in prods if p["img"]} | {x["img"] for p in prods for x in p["vars"] if x["img"]}
imgs = {k: IMG[k] for k in used}

# ---------------- account-level
tot = {m: rows_bp[(m, "Total")] for m in ("US", "CA")}
hist = {}
for m in ("US", "CA"):
    for x in VR["checks"]:
        if x["mkt"] == m and x["item"].startswith("History check A"): hist.setdefault(m, {})["A"] = x["source"]
        if x["mkt"] == m and x["item"].startswith("History check B"): hist.setdefault(m, {})["B"] = x["source"]
    hist[m]["pace"] = sum(p["alt_budget"] for p in VR["products"] if p["mkt"] == m)
    hist[m]["bf25"] = SRC["bfcm2025_total"][m]["adv"] * (1.4036 if m == "CA" else 1)
from collections import Counter
cc = Counter(x["status"] for x in VR["checks"])
data = {
    "built": "Nov 2, 2026",
    "totals": tot, "hist": hist, "days": DAYS, "daytot": daytot, "weights": weights,
    "rules": rules, "agent": agent, "calls": calls,
    "yoy": {m: YO["markets"][m]["decomp"] for m in ("US", "CA")},
    "bfgroups": [{"m": r["market"], "g": r["class"], "s25": r["adv25"], "p26": r["plan_budget26"]} for r in YO["bfcm"]],
    "daily25": SRC["daily_bfcm2025"], "weekly": SRC["weekly2026"],
    "checks": {"total": len(VR["checks"]), "ok": cc["OK"], "check": cc["CHECK"], "diff": cc.get("DIFF", 0)},
    "products": prods,
}
tpl = open(os.path.join(HERE, "review_template.html")).read()
html = tpl.replace("/*__DATA__*/null", json.dumps(data, default=str, separators=(",", ":"))).replace("/*__IMG__*/null", json.dumps(imgs, separators=(",", ":")))
open(OUT, "w").write(html)
print("products", len(prods), "images", len(imgs), "bytes", len(html))
