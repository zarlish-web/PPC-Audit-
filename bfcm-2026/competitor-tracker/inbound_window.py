"""BFCM 2026 inbound check: which inbound units become sellable before or during the deal window (Nov 19-30).

Joins the inbound ETAs per shipment (data/stock/inbound_eta_2026-10-22.csv, from the Oct 22 T-7 inbound check) with the
SKU contents of each shipment (Oct 15 shipment pull; Ready-to-Ship batch contents from the Oct 21 plans) and today's
shipment status (data/stock/sellerboard_shipment_status_2026-10-23.csv), then maps every SKU to our product and variation.

Sellable date = latest arrival date + RECEIVE_DAYS (Amazon check-in to available in peak season; an assumption, shown).
Usage: python3 inbound_window.py competitor_dashboard.html OUT_DIR
"""
import csv, datetime as dt, json, os, sys
from collections import defaultdict

SRC, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
STOCK = os.path.join(HERE, "data", "stock")
DEAL_START, DEAL_END = dt.date(2026, 11, 19), dt.date(2026, 11, 30)
RECEIVE_DAYS = 5          # peak-season check-in to sellable; 3 (fast) to 7 (slow) shown as the range
MODES = {"Air": ("2026-11-05", "2026-11-09"), "Fastest": ("2026-11-22", "2026-11-27"), "Fast": ("2026-11-27", "2026-12-02")}
D = lambda s: dt.date.fromisoformat(s) if s else None

h = open(SRC).read()
i = h.index("const D = ") + len("const D = ")
P = json.loads(h[i:h.index("\nconst IMG")].rstrip().rstrip(";"))
var = {}                                   # (mkt, asin) -> product / variation / Oct 15 stock outlook
for p in P["products"]:
    stk = {r["asin"]: r for r in ((p.get("stock26") or {}).get("rows") or [])}
    for v in p.get("vars") or []:
        r = stk.get(v["asin"], {})
        var[(p["mkt"], v["asin"])] = {"product": p["short"], "size": v.get("size"), "colour": v.get("colour"), "status_oct15": r.get("st"),
                                      "need": r.get("need"), "short_oct15": r.get("short"), "oh_oct15": r.get("oh"), "oos": r.get("oos"), "vel": r.get("vel")}

eta = {r["shipment_id"]: r for r in csv.DictReader(open(os.path.join(STOCK, "inbound_eta_2026-10-22.csv")))}
status = {r["shipment_id"]: r for r in csv.DictReader(open(os.path.join(STOCK, "sellerboard_shipment_status_2026-10-23.csv")))}
contents = defaultdict(list)               # shipment -> [(asin, sku, units, received_oct15)]
for r in csv.DictReader(open(os.path.join(STOCK, "sellerboard_inbound_shipments_2026-10-15.csv"))):
    if r["shipment_id"] in eta:
        contents[r["shipment_id"]].append((r["asin"], r["sku"], int(float(r["units_shipped"] or 0)), int(float(r["units_received"] or 0))))
rts = defaultdict(list)                    # batch -> [(asin, sku, units)]
for r in csv.DictReader(open(os.path.join(STOCK, "ready_to_ship_2026-10-21_contents.csv"))):
    rts[r["batch"]].append((r["asin"], r["sku"], int(r["units"])))

def bucket(sellable):
    if sellable is None:
        return "Mode pending"
    if sellable < DEAL_START:
        return "Sellable before Nov 19"
    if sellable <= DEAL_START + dt.timedelta(days=2):
        return "Tight: sellable around Nov 19-21"
    if sellable <= DEAL_END:
        return "Sellable during the deal (Nov 22-30)"
    return "After Nov 30 (outside the deal)"

ship_rows, sku_rows = [], []
for sid, e in eta.items():
    s = status.get(sid, {})
    batch = "USA260" if "USA260" in e["eta_note"] else "CA0108" if "CA0108" in e["eta_note"] else None
    items = [(a, k, u, 0) for a, k, u in rts[batch]] if batch else contents.get(sid, [])
    if batch:                                # Ready-to-Ship batch: contents are for the whole batch, listed once
        if sid not in ("FBA19TYN6F53", "FBA19TY7ML4M"):
            items = []
    to, frm = D(e["eta_to"]), D(e["eta_from"])
    sellable = to + dt.timedelta(days=RECEIVE_DAYS) if to else None
    units = int(s.get("units") or sum(x[2] for x in items))
    rec = int(s.get("units_received") or 0)
    b = bucket(sellable)
    ship_rows.append({"shipment": sid, "mkt": e["mkt"], "status_now": s.get("status", ""), "units": units,
                      "received_so_far": rec, "eta": e["eta_note"], "sellable_by_est": sellable.isoformat() if sellable else "", "sellable_range": (f"{(to + dt.timedelta(days=3)).isoformat()} to {(to + dt.timedelta(days=7)).isoformat()}" if to else ""),
                      "window": b, "batch": batch or ""})
    for a, k, u, r0 in items:
        v = var.get((e["mkt"], a)) or var.get(("US", a)) or {}
        sku_rows.append({"shipment": sid, "mkt": e["mkt"], "window": b, "sellable_by_est": sellable.isoformat() if sellable else "mode pending", "asin": a, "sku": k,
                         "product": v.get("product", "not in tracker"), "size": v.get("size", ""), "colour": v.get("colour", ""), "units": u,
                         "status_oct15": v.get("status_oct15") or "", "short_oct15": round(v["short_oct15"]) if v.get("short_oct15") else 0,
                         "runs_out_oct15": v.get("oos") or ""})

os.makedirs(OUT, exist_ok=True)
for name, rows in (("inbound_by_shipment.csv", ship_rows), ("inbound_by_sku.csv", sku_rows)):
    with open(os.path.join(OUT, name), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# summaries
order = ["Sellable before Nov 19", "Tight: sellable around Nov 19-21", "Sellable during the deal (Nov 22-30)", "Mode pending", "After Nov 30 (outside the deal)"]
tot = defaultdict(lambda: defaultdict(int))
for r in ship_rows:
    tot[r["window"]][r["mkt"]] += r["units"] - (r["received_so_far"] if r["status_now"] == "RECEIVING" else 0)
print("UNITS STILL TO BE RECEIVED BY WINDOW (US / CA)")
for b in order:
    print(f"  {b:40s} US {tot[b]['US']:>6,}  CA {tot[b]['CA']:>6,}")
prod = defaultdict(lambda: defaultdict(int))
for r in sku_rows:
    prod[(r["mkt"], r["product"])][r["window"]] += r["units"]
print("\nBY PRODUCT (units):")
for (m, pr), d in sorted(prod.items(), key=lambda kv: (kv[0][0], -sum(kv[1].values()))):
    print(f"  {m} {pr:24s} " + " | ".join(f"{b.split(':')[0].split(' (')[0]}: {d[b]:,}" for b in order if d[b]))
risk = [r for r in sku_rows if r["status_oct15"] in ("Short even with inbound", "Out of stock now")]
print("\nAT-RISK VARIATIONS (Oct 15) THAT GET UNITS:", len({(r['mkt'], r['asin']) for r in risk}))
json.dump({"ships": ship_rows, "skus": sku_rows}, open(os.path.join(OUT, "inbound_window.json"), "w"))
