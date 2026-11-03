"""Turns daily per-child-ASIN pulls (actuals/daily_child_*.csv) into the tracker's database documents: one document per
market per day, id "{mkt}_{date}", with each plan product's spend by ad type, sales and units, the plan-products total
and the rest of the account. Canada is converted to C$ (recorded in US$) so it compares with the plan.
Child ASINs map to products exactly as in verification/yoy.py (SKU lists, any-market SKU match, the re-parented name
list, then name rules), the same mapping behind the plan's "TACoS now".
Usage: python3 actuals_build.py  -> actuals/db_actuals.json (list of {"id", "data"}) and a printed summary."""
import csv, glob, json, os, datetime as dt
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); TR = os.path.join(HERE, "..", "competitor-tracker", "data")
FX = 1.4036
skus = {}
for f in glob.glob(f"{TR}/skus/*.json"):
    d = json.load(open(f))
    if "product_id" in d:
        skus[(int(d["product_id"]), d["marketplace"])] = d
mv = [x for x in skus[(37, "US")]["skus"] if str(x.get("sku", "")).upper().startswith("SATIN-4PC-TWIN")]
skus[(37, "US")]["skus"] = [x for x in skus[(37, "US")]["skus"] if x not in mv]; skus[(31, "US")]["skus"] += mv
asin2pid = {}
for (pid, m), d in skus.items():
    for x in d["skus"]:
        if x.get("asin"):
            asin2pid[(m, x["asin"])] = pid
            asin2pid.setdefault(("ANY", x["asin"]), pid)
NAME_MAP = {"B0F2G983W3": 39, "B0F55Y1P53": 32, "B0F7LX9RP3": 45, "B0F7LY4RD6": 45, "B0F7LY3994": 45, "B0FTSWF3M7": 45,
            "B0CQ3GXLCJ": 30, "B0D9HRYKBW": 48, "B0CRF7S2TH": 31, "B0CRVZ1TTS": 37}
for a_, p_ in NAME_MAP.items():
    asin2pid.setdefault(("ANY", a_), p_)
NAME_RULES = [("BreezeWeave", 45), ("Hanging Closet", 52), ("Boho Throw Blanket", 41), ("Bamboo Sheets Queen Size | 6 Pc", 30)]
PLAN = defaultdict(set)
for r in json.load(open(os.path.join(HERE, "plan_numbers.json"))):
    PLAN[r["mkt"]].add(r["pid"])

K = ("sp", "sb", "sbv", "sd", "sales", "units")
days = defaultdict(lambda: {"products": defaultdict(lambda: dict.fromkeys(K, 0.0)), "other": dict.fromkeys(K, 0.0), "rows": 0})
# a day can appear in more than one file (a re-pull to catch late ad charges): the newest file for that day wins
_files = sorted(glob.glob(os.path.join(HERE, "actuals", "daily_child_*.csv")), key=os.path.getmtime)
_owner = {}
for f in _files:
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        _owner[(r["marketplace"], r["date"])] = f
for f in _files:
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        if _owner.get((r["marketplace"], r["date"])) != f:
            continue
        m = r["marketplace"]; fx = FX if m == "CA" else 1.0
        pid = asin2pid.get((m, r["asin"])) or asin2pid.get(("ANY", r["asin"]))
        if pid is None:
            pid = next((p_ for k_, p_ in NAME_RULES if k_.lower() in (r.get("name") or "").lower()), None)
        dd = days[(m, r["date"])]; dd["rows"] += 1
        tgt = dd["products"][str(pid)] if pid in PLAN[m] else dd["other"]
        for k in K:
            v = float(r.get(k) or 0)
            tgt[k] += v * (fx if k != "units" else 1)
now = dt.datetime.now(dt.timezone.utc).strftime("%b %-d %H:%M UTC")
docs = []
for (m, date), dd in sorted(days.items()):
    prods = {p: {k: round(v, 2) for k, v in s.items()} for p, s in dd["products"].items()}
    total = {k: round(sum(s[k] for s in dd["products"].values()), 2) for k in K}
    docs.append({"id": f"{m}_{date}", "data": {"mkt": m, "date": date, "cur": "C$" if m == "CA" else "US$", "products": prods, "total": total,
                                              "other": {k: round(v, 2) for k, v in dd["other"].items()}, "rows": dd["rows"], "updated": now}})
json.dump(docs, open(os.path.join(HERE, "actuals", "db_actuals.json"), "w"), indent=1)
for d in docs:
    t = d["data"]["total"]; o = d["data"]["other"]; sp = t["sp"] + t["sb"] + t["sbv"] + t["sd"]
    print(f"{d['id']}: plan products spend {sp:9,.0f} sales {t['sales']:10,.0f} TACoS {sp / t['sales'] * 100 if t['sales'] else 0:5.1f}% | other spend {o['sp'] + o['sb'] + o['sbv'] + o['sd']:7,.0f} sales {o['sales']:9,.0f}")
