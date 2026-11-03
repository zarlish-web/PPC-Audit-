"""Builds actuals/daily_child_<date>.csv for ONE day from saved dashboard_table results (product rows), in the
schema actuals_build.py reads. Pass every saved result file of that day's pulls (both passes, both pages); rows are
de-duplicated by (marketplace, Id), and only results whose resolved period is exactly that day are used.
Usage: python3 pull_day.py 2026-11-03 <saved result file> [<saved result file> ...]
Prints row counts and US / CA sums of sales and advertising to compare with dashboard_period's day totals."""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
day = sys.argv[1]
rows = {}
for f in sorted(sys.argv[2:], key=os.path.getmtime):   # oldest first, so the newest snapshot of a row wins
    t = open(f).read()
    j = json.loads(t[t.index("{"):])
    rp = j.get("resolvedPeriods") or []
    if not rp or rp[0].get("from") != day or rp[0].get("to") != day:
        continue
    for r in j.get("result") or []:
        i = r.get("Info") or {}
        m = "CA" if (i.get("Marketplace") or "").lower() == "amazon.ca" else "US"
        rows[(m, i.get("Id"))] = i
out = os.path.join(HERE, f"daily_child_{day}.csv")
cols = ["date", "marketplace", "asin", "sku", "name", "sales", "units", "sp", "sb", "sbv", "sd", "advertising", "sessions"]
agg = {}
with open(out, "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(cols)
    merged = {}
    for (m, _), i in rows.items():
        k = (m, i.get("ASIN"), i.get("SKU"))
        a = merged.setdefault(k, {"name": i.get("Name") or "", "sales": 0.0, "units": 0.0, "sp": 0.0, "sb": 0.0, "sbv": 0.0, "sd": 0.0, "advertising": 0.0, "sessions": 0.0})
        a["sales"] += i.get("Sales") or 0; a["units"] += i.get("Units") or 0
        a["sp"] += -(i.get("SponsoredADS") or 0); a["sb"] += -(i.get("HSA") or 0); a["sbv"] += -(i.get("VideoAds") or 0)
        a["sd"] += -(i.get("SponsoredDisplay") or 0); a["advertising"] += -(i.get("Advertising") or 0); a["sessions"] += i.get("sessions") or 0
    for (m, asin, sku), a in sorted(merged.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        w.writerow([day, m, asin, sku, a["name"], round(a["sales"], 2), int(a["units"]), round(a["sp"], 2), round(a["sb"], 2), round(a["sbv"], 2),
                    round(a["sd"], 2), round(a["advertising"], 2), int(a["sessions"])])
        s = agg.setdefault(m, [0, 0.0, 0.0]); s[0] += 1; s[1] += a["sales"]; s[2] += a["advertising"]
print(out)
for m, (n, sa, ad) in sorted(agg.items()):
    print(f"{m}: {n} rows, sales {sa:,.2f}, advertising {ad:,.2f}  (amounts as recorded; CA in US$)")
