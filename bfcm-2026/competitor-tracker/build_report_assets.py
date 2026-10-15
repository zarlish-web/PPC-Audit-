"""Charts, diagram, photos and data for the BFCM 2026 Word report (build_report.js turns them into the .docx).

Reads the verified dashboard data (competitor_dashboard.html + images.js / images2.js) and writes into OUT_DIR:
  charts/*.png   method diagram and every chart
  img/*.jpg      product and competitor photos (thumbnails)
  report.json    the numbers and text the report prints
Usage: python3 build_report_assets.py competitor_dashboard.html OUT_DIR
"""
import base64, json, os, statistics, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrub import scrub_obj

SRC, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{OUT}/charts", exist_ok=True)
os.makedirs(f"{OUT}/img", exist_ok=True)

# ---------------------------------------------------------------- style (validated reference palette, light mode)
for f in font_manager.findSystemFonts():
    if "omfortaa" in f:
        font_manager.fontManager.addfont(f)
FONT = "Comfortaa" if any("Comfortaa" == f.name for f in font_manager.fontManager.ttflist) else "DejaVu Sans"
BLUE, ORANGE, AQUA, YELLOW, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#a9a8a3"
RED, GREEN = "#e34948", "#008300"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
plt.rcParams.update({"font.family": FONT, "font.size": 9, "text.color": INK, "axes.labelcolor": INK2, "axes.edgecolor": GRID,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True, "figure.facecolor": SURF,
                     "axes.facecolor": SURF, "legend.frameon": False, "savefig.dpi": 200, "savefig.bbox": "tight"})
CLS_ORDER = ["Direct", "Material not verified", "Alternative material", "Different product type", "Not classified"]
CLS_COL = {"Direct": BLUE, "Material not verified": YELLOW, "Alternative material": ORANGE, "Different product type": GREY, "Not classified": "#d6d5d0"}
num = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)
cur = lambda m: "C$" if m == "CA" else "$"


def save(fig, name):
    fig.savefig(f"{OUT}/charts/{name}.png")
    plt.close(fig)
    return f"charts/{name}.png"


# ---------------------------------------------------------------- data
h = open(SRC).read()
i = h.index("const D = ") + len("const D = ")
D = json.loads(h[i:h.index("\nconst IMG")].rstrip().rstrip(";"))
IMG = {}
for js in ("images.js", "images2.js"):
    t = open(os.path.join(os.path.dirname(os.path.abspath(SRC)), js)).read()
    IMG.update(json.loads(t[t.index("{", t.index("window.IMG||{}") + 14):t.rindex(")")]))


def photo(key):
    """Write the thumbnail for key (or the Coming Soon image) and return its relative path."""
    k = key if key in IMG else "COMING_SOON"
    p = f"img/{k}.jpg"
    if not os.path.exists(f"{OUT}/{p}"):
        open(f"{OUT}/{p}", "wb").write(base64.b64decode(IMG[k].split(",", 1)[1]))
    return p


products, comps = D["products"], D["comps"]
by_prod = {}
for c in comps:
    by_prod.setdefault((str(c["pid"]), c["mkt"]), []).append(c)
checks = json.load(open(os.path.join(HERE, "data", "verification_report.json")))["checks"]
charts = {}

# ---------------------------------------------------------------- 1. method diagram
fig, ax = plt.subplots(figsize=(10, 3.2))
ax.set_xlim(0, 100); ax.set_ylim(0, 32); ax.axis("off")
steps = [("1", "Our products", "33 listings\nUS and Canada"), ("2", "Competitors", "744 mapped to\nthe product they rival"),
         ("3", "Classify", "Direct vs alternative\nmaterial and type"), ("4", "BFCM 2025", "deal type, price,\ndiscount, rank change"),
         ("5", "Today", "price, List Price,\nstrikethrough"), ("6", "BFCM 2026", "assumed deal price\nand stock to Nov 30"),
         ("7", "Verify", "16 checks against\nthe raw data")]
w, gap = 12.2, 2.1
for j, (n, t, s) in enumerate(steps):
    x = 1 + j * (w + gap)
    ax.add_patch(FancyBboxPatch((x, 6), w, 20, boxstyle="round,pad=0.3,rounding_size=1.6", fc="#eef4fc" if j < 6 else "#e8f6ef",
                                ec=BLUE if j < 6 else GREEN, lw=1.2))
    ax.text(x + w / 2, 22.2, n, ha="center", va="center", fontsize=11, fontweight="bold", color=BLUE if j < 6 else GREEN)
    ax.text(x + w / 2, 17.4, t, ha="center", va="center", fontsize=9.5, fontweight="bold")
    ax.text(x + w / 2, 11.0, s, ha="center", va="center", fontsize=7.4, color=INK2, linespacing=1.4)
    if j < len(steps) - 1:
        ax.annotate("", xy=(x + w + gap - 0.2, 16), xytext=(x + w + 0.4, 16), arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.text(50, 1.5, "Every number flows left to right; the verification step re-computes them from the raw data before anything is shared.",
        ha="center", fontsize=8, color=INK2)
charts["flow"] = save(fig, "flow")

# ---------------------------------------------------------------- 2. classification diagram (decision tree)
fig, ax = plt.subplots(figsize=(10, 3.4))
ax.set_xlim(0, 100); ax.set_ylim(0, 34); ax.axis("off")
def box(x, y, w_, h_, t, fc, ec, fs=8.2, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w_, h_, boxstyle="round,pad=0.25,rounding_size=1.2", fc=fc, ec=ec, lw=1.1))
    ax.text(x + w_ / 2, y + h_ / 2, t, ha="center", va="center", fontsize=fs, fontweight="bold" if bold else "normal", linespacing=1.35)
def arrow(x1, y1, x2, y2, label=None):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
    if label:
        ax.text((x1 + x2) / 2 + 0.8, (y1 + y2) / 2, label, fontsize=7.2, color=INK2)
box(1, 13, 15, 8, "Competitor\nlisting", "#f4f4f2", GREY, bold=True)
box(23, 13, 19, 8, "Same product type?\n(sheet set vs fitted,\npillowcase, comforter)", "#f4f4f2", GREY)
box(49, 13, 19, 8, "Material known?\n(product page first,\nthen the title)", "#f4f4f2", GREY)
box(75, 24, 23, 8, "Same material family\n= DIRECT", "#eef4fc", BLUE, bold=True)
box(75, 13, 23, 8, "Other material\n= ALTERNATIVE MATERIAL", "#fdf0ea", ORANGE, bold=True)
box(75, 2, 23, 8, "No material shown\n= MATERIAL NOT VERIFIED", "#fdf6e3", YELLOW, bold=True)
box(23, 1, 19, 7.5, "No\n= DIFFERENT PRODUCT TYPE", "#f4f4f2", GREY, fs=7.6, bold=True)
arrow(16, 17, 23, 17); arrow(42, 17, 49, 17, "yes"); arrow(32.5, 13, 32.5, 8.6, "")
arrow(68, 19, 75, 27, "yes, same"); arrow(68, 17, 75, 17, "yes, other"); arrow(68, 15, 75, 7, "no")
charts["cls_tree"] = save(fig, "cls_tree")

# ---------------------------------------------------------------- 3. classification by product
for m in ("US", "CA"):
    ps = [p for p in products if p["mkt"] == m and by_prod.get((str(p["pid"]), m))]
    if not ps:
        continue
    ps.sort(key=lambda p: len(by_prod[(str(p["pid"]), m)]))
    fig, ax = plt.subplots(figsize=(10, 0.32 * len(ps) + 1.2))
    left = [0] * len(ps)
    for cl in CLS_ORDER:
        vals = [sum(1 for c in by_prod[(str(p["pid"]), m)] if (c.get("cls") or "Not classified") == cl) for p in ps]
        if not any(vals):
            continue
        ax.barh([p["short"] for p in ps], vals, left=left, color=CLS_COL[cl], height=0.66, label=cl, edgecolor=SURF, linewidth=1)
        left = [a + b for a, b in zip(left, vals)]
    for y, tot in enumerate(left):
        ax.text(tot + 0.4, y, str(tot), va="center", fontsize=7.6, color=INK2)
    ax.set_xlabel("Competitors mapped"); ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right", ncol=1, fontsize=7.6)
    ax.set_title(f"{'United States' if m == 'US' else 'Canada'}: competitors per product by type", loc="left", fontsize=10, fontweight="bold")
    charts[f"cls_{m}"] = save(fig, f"cls_{m}")

# ---------------------------------------------------------------- 4. BFCM 2025 rank lift by deal type
lift = {}
for m in ("US", "CA"):
    rows = {}
    for c in comps:
        if c["mkt"] == m and c.get("bf_type") and num(c.get("bsr_lift_v")):
            rows.setdefault(c["bf_type"], []).append(c)
    lift[m] = sorted(({"type": t, "median": statistics.median(x["bsr_lift_v"] for x in v), "n": len(v),
                       "disc": statistics.median([x["bf_disc_v"] for x in v if num(x.get("bf_disc_v"))] or [0]),
                       "share_up": sum(1 for x in v if x["bsr_lift_v"] > 1) / len(v)}
                      for t, v in rows.items() if len(v) >= 3), key=lambda r: -r["median"])
fig, axs = plt.subplots(1, 2, figsize=(10, 3.0), gridspec_kw={"width_ratios": [len(lift["US"]) or 1, len(lift["CA"]) or 1]})
for ax, m in zip(axs, ("US", "CA")):
    rs = lift[m][::-1]
    ax.barh([f"{r['type']} ({r['n']})" for r in rs], [r["median"] for r in rs], color=[BLUE if r["median"] >= 1 else GREY for r in rs], height=0.6)
    ax.axvline(1, color=INK2, lw=0.8, ls=(0, (3, 3)))
    for y, r in enumerate(rs):
        ax.text(r["median"] + 0.02, y, f"{r['median']:.2f}x", va="center", fontsize=8, fontweight="bold")
    ax.set_xlim(0, max(1.8, max((r["median"] for r in rs), default=1) * 1.18)); ax.grid(axis="y", visible=False)
    ax.set_title("United States" if m == "US" else "Canada", loc="left", fontsize=10, fontweight="bold")
    ax.set_xlabel("Median rank improvement, BFCM week vs Nov 1–19 (1.00x = no change)", fontsize=7.6)
fig.tight_layout(w_pad=3)
charts["lift_deal"] = save(fig, "lift_deal")

# discount vs rank lift (three named deal types; others folded out)
fig, ax = plt.subplots(figsize=(10, 3.6))
for t, col in (("Price cut only", BLUE), ("Prime Exclusive Discount", ORANGE), ("Coupon only", AQUA)):
    xs = [(c["bf_disc_v"] * 100, c["bsr_lift_v"]) for c in comps if c["mkt"] == "US" and c.get("bf_type") == t and num(c.get("bf_disc_v")) and num(c.get("bsr_lift_v"))]
    xs = [(a, min(max(b, 0.2), 6)) for a, b in xs if 0 <= a <= 60]
    if xs:
        ax.scatter([a for a, _ in xs], [b for _, b in xs], s=22, color=col, label=f"{t} ({len(xs)})", edgecolor=SURF, linewidth=0.8, alpha=0.9)
ax.axhline(1, color=INK2, lw=0.8, ls=(0, (3, 3)))
ax.set_yscale("log"); ax.set_yticks([0.25, 0.5, 1, 2, 4, 6]); ax.set_yticklabels(["0.25x", "0.5x", "1x", "2x", "4x", "6x"])
ax.set_xlabel("BFCM 2025 discount vs the price before (%)"); ax.set_ylabel("Rank improvement (log scale)")
ax.legend(loc="upper left", fontsize=8)
ax.set_title("United States: deeper discounts vs rank change in BFCM 2025, by deal type", loc="left", fontsize=10, fontweight="bold")
charts["disc_lift"] = save(fig, "disc_lift")

# ---------------------------------------------------------------- 5. our BFCM 2025 sales lift by product
for m in ("US", "CA"):
    ps = sorted([p for p in products if p["mkt"] == m and num(p.get("lift"))], key=lambda p: p["lift"])
    if not ps:
        continue
    acct = D["summary"][m]["accountLift"]
    fig, ax = plt.subplots(figsize=(10, 0.3 * len(ps) + 1.1))
    ax.barh([p["short"] for p in ps], [p["lift"] for p in ps], color=[BLUE if p["lift"] >= 1 else GREY for p in ps], height=0.62)
    ax.axvline(acct, color=ORANGE, lw=1.2); ax.text(acct, len(ps) - 0.3, f"  account {acct:.2f}x", color=INK, fontsize=8, va="bottom")
    for y, p in enumerate(ps):
        ax.text(p["lift"] + 0.05, y, f"{p['lift']:.2f}x", va="center", fontsize=7.6)
    ax.grid(axis="y", visible=False); ax.set_xlabel("Sales per day, BFCM week 2025 vs the 30 days before")
    ax.set_title(f"{'United States' if m == 'US' else 'Canada'}: our BFCM 2025 sales lift by product", loc="left", fontsize=10, fontweight="bold")
    charts[f"our_lift_{m}"] = save(fig, f"our_lift_{m}")

# ---------------------------------------------------------------- 6. assumed BFCM 2026 deal ladder
for m in ("US", "CA"):
    ps = [p for p in products if p["mkt"] == m and p.get("da") and num(p["da"].get("ref"))]
    if not ps:
        continue
    ps.sort(key=lambda p: p["da"]["ref"])
    fig, ax = plt.subplots(figsize=(10, 0.36 * len(ps) + 1.2))
    for y, p in enumerate(ps):
        d = p["da"]
        ax.plot([d["deal_peak"], d["ref"]], [y, y], color=GRID, lw=3, solid_capstyle="round", zorder=1)
        ax.scatter([d["ref"]], [y], color=GREY, s=34, zorder=3, label="Today" if y == 0 else None)
        ax.scatter([d["deal_std"]], [y], color=BLUE, s=34, zorder=3, label="Nov 19–26 (−15%)" if y == 0 else None)
        ax.scatter([d["deal_peak"]], [y], color=ORANGE, s=34, zorder=3, label="Nov 27–30 (−20%)" if y == 0 else None)
        ax.text(d["ref"] + 1, y, f"{cur(m)}{d['ref']:.2f} → {cur(m)}{d['deal_std']:.2f} → {cur(m)}{d['deal_peak']:.2f}", va="center", fontsize=7.4, color=INK2)
    ax.set_yticks(range(len(ps))); ax.set_yticklabels([p["short"] for p in ps]); ax.grid(axis="y", visible=False)
    ax.set_xlim(min(p["da"]["deal_peak"] for p in ps) * 0.8, max(p["da"]["ref"] for p in ps) * 1.45)
    ax.set_xlabel(f"Price ({cur(m)})"); ax.legend(loc="lower right", fontsize=7.8)
    ax.set_title(f"{'United States' if m == 'US' else 'Canada'}: assumed BFCM 2026 deal prices", loc="left", fontsize=10, fontweight="bold")
    charts[f"deal_{m}"] = save(fig, f"deal_{m}")

# ---------------------------------------------------------------- 7. stock to Nov 30
ps = [p for p in products if p.get("stock26")]
ps.sort(key=lambda p: p["stock26"]["need"])
fig, ax = plt.subplots(figsize=(10, 0.34 * len(ps) + 1.3))
lab = [f"{p['short']} ({p['mkt']})" for p in ps]
oh = [p["stock26"]["onHand"] for p in ps]; ib = [p["stock26"]["inbound"] for p in ps]; nd = [p["stock26"]["need"] for p in ps]
ax.barh(lab, oh, color=BLUE, height=0.62, label="At Amazon now")
ax.barh(lab, ib, left=oh, color=AQUA, height=0.62, label="Inbound", edgecolor=SURF, linewidth=1)
ax.scatter(nd, range(len(ps)), marker="|", s=170, color=INK, linewidths=2, zorder=4, label="Needed to Nov 30")
ax.set_xscale("symlog", linthresh=100); ax.grid(axis="y", visible=False)
ax.set_xlabel("Units (log scale)"); ax.legend(loc="lower right", fontsize=7.8)
ax.set_title("Stock vs what each product needs to Nov 30 (today's pace × BFCM lift)", loc="left", fontsize=10, fontweight="bold")
charts["stock"] = save(fig, "stock")

# ---------------------------------------------------------------- 8. per product: competitor price map
def price_map(p, cs):
    m = p["mkt"]
    rows = [cl for cl in CLS_ORDER if any((c.get("cls") or "Not classified") == cl and num(c.get("price")) for c in cs)]
    if not rows:
        return None
    fig, ax = plt.subplots(figsize=(10, 0.42 * len(rows) + 1.25))
    for y, cl in enumerate(rows):
        xs = [c["price"] for c in cs if (c.get("cls") or "Not classified") == cl and num(c.get("price"))]
        ys = [y + ((k % 5) - 2) * 0.07 for k in range(len(xs))]
        ax.scatter(xs, ys, s=26, color=CLS_COL[cl], edgecolor=SURF, linewidth=0.8, zorder=3)
        ax.text(max(xs), y, f"   median {cur(m)}{statistics.median(xs):.2f} · {len(xs)}", va="center", fontsize=7.4, color=INK2)
    if num(p.get("price")):
        ax.axvline(p["price"], color=INK, lw=1.3, zorder=2)
        ax.text(p["price"], len(rows) - 0.45, f" ours today {cur(m)}{p['price']:.2f}", fontsize=7.8, fontweight="bold", va="bottom")
    if p.get("da") and num(p["da"].get("deal_peak")):
        ax.axvline(p["da"]["deal_peak"], color=ORANGE, lw=1.1, ls=(0, (4, 3)), zorder=2)
        ax.text(p["da"]["deal_peak"], -0.75, f"assumed Nov 27–30 {cur(m)}{p['da']['deal_peak']:.2f} ", fontsize=7.4, ha="right", va="bottom", color=INK)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows); ax.set_ylim(-0.8, len(rows) - 0.2)
    ax.grid(axis="y", visible=False); ax.set_xlabel(f"Competitor price today ({cur(m)}, the tracked size)")
    lo = min([c["price"] for c in cs if num(c.get("price"))] + ([p["price"]] if num(p.get("price")) else []))
    hi = max([c["price"] for c in cs if num(c.get("price"))] + ([p["price"]] if num(p.get("price")) else []))
    ax.set_xlim(lo * 0.85, hi * 1.25)
    return save(fig, f"price_{p['key']}")

# ---------------------------------------------------------------- report data
COMP_KEYS = ("brand", "title", "child", "size", "colour", "price", "lp", "gap", "str_show", "str_label", "str_price", "deal_now", "stock_now",
             "bf_type", "bf_dates", "bf_pre", "bf_low", "bf_disc_v", "bsr_pre", "bsr_bf", "bsr_lift_v", "bf_oos", "wk", "rating", "reviews",
             "bsr", "tier", "cls", "cls_why", "mat", "listed", "ful", "notes")
out_products = []
order = {"Core": 0, "Launched (partly live)": 1, "Other": 2, "Not launched": 3}
for p in sorted(products, key=lambda p: (p["mkt"] != "US", order.get(p["scope"], 4), p["family"], p["short"])):
    cs = sorted(by_prod.get((str(p["pid"]), p["mkt"]), []), key=lambda c: (CLS_ORDER.index(c.get("cls") or "Not classified"), -(c.get("wk") or 0)))
    st = p.get("stock26")
    risk = []
    if st:
        risk = [{k: x.get(k) for k in ("size", "colour", "oh", "ib", "vel", "need", "short", "oos", "st")}
                for x in sorted(st["rows"], key=lambda x: -(x.get("vel") or 0)) if x["st"] != "Covered to Nov 30"]
    direct = [c for c in cs if c.get("cls") == "Direct"]
    base = direct or cs
    prices = [c["price"] for c in base if num(c.get("price"))]
    out_products.append({
        **{k: p.get(k) for k in ("key", "mkt", "short", "family", "role", "scope", "brand", "name", "title", "parent", "best", "bestLabel", "stage",
                                 "price", "u28", "lift", "tacos", "preTacos", "hk", "hkLine", "deals", "plan26", "da", "stock", "stockGap", "sb",
                                 "colours", "sizes")},
        "notes": p.get("slack") or [], "nvars": len(p.get("vars") or []),
        "nlive": sum(1 for v in (p.get("vars") or []) if v.get("live")),
        "photo": photo(p.get("img") or ""),
        "stock26": ({k: st[k] for k in ("lift", "liftSrc", "onHand", "inbound", "vel", "need", "short", "counts", "need28")} if st else None),
        "risk": risk,
        "priceChart": price_map(p, cs) if cs else None,
        "cmp": {"n": len(cs), "direct": len(direct), "median": statistics.median(prices) if prices else None,
                "below": sum(1 for c in base if num(c.get("gap")) and c["gap"] < 0), "basisDirect": bool(direct),
                "byCls": {cl: sum(1 for c in cs if (c.get("cls") or "Not classified") == cl) for cl in CLS_ORDER}},
        "comps": [{**{k: c.get(k) for k in COMP_KEYS}, "photo": photo(c.get("img") or "")} for c in cs],
    })

summary = {
    "comps": len(comps), "us": sum(1 for c in comps if c["mkt"] == "US"), "ca": sum(1 for c in comps if c["mkt"] == "CA"),
    "byCls": {cl: sum(1 for c in comps if (c.get("cls") or "Not classified") == cl) for cl in CLS_ORDER},
    "withBf": sum(1 for c in comps if c.get("bf_type")), "strShown": sum(1 for c in comps if c.get("str_show") == "Y"),
    "strChecked": sum(1 for c in comps if c.get("str_show") in ("Y", "N")),
    "accountLift": {m: D["summary"][m]["accountLift"] for m in ("US", "CA")},
    "products": len(products), "productsUS": sum(1 for p in products if p["mkt"] == "US"), "productsCA": sum(1 for p in products if p["mkt"] == "CA"),
    "stockAtRisk": sum(1 for p in products if p.get("stock26") and (p["stock26"]["counts"].get("Short even with inbound") or p["stock26"]["counts"].get("Out of stock now"))),
    "stockProducts": sum(1 for p in products if p.get("stock26")),
    "varsShort": sum(p["stock26"]["counts"].get("Short even with inbound", 0) for p in products if p.get("stock26")),
    "varsOut": sum(p["stock26"]["counts"].get("Out of stock now", 0) for p in products if p.get("stock26")),
    "varsInbound": sum(p["stock26"]["counts"].get("Needs inbound in time", 0) for p in products if p.get("stock26")),
    "varsCovered": sum(p["stock26"]["counts"].get("Covered to Nov 30", 0) for p in products if p.get("stock26")),
}
data = {"built": "Oct 15, 2026", "summary": summary, "lift": lift, "charts": charts, "products": out_products,
        "checks": [{"name": c["name"].replace("the inventory planner", "the stock plan"), "checked": c["checked"], "bad": c["mismatches"],
                    "status": c["status"], "note": c.get("note") or ""} for c in checks]}
json.dump(scrub_obj(data), open(f"{OUT}/report.json", "w"), default=str)
print(json.dumps({"products": len(out_products), "comps": len(comps), "charts": len(charts) + sum(1 for p in out_products if p["priceChart"]),
                  "photos": len(os.listdir(f"{OUT}/img")), "font": FONT}))
