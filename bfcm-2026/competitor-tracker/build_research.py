"""BFCM 2026 Competitor Research workbook.

One tab per product and marketplace, a filterable Dashboard with live product images
(Excel 365 / Google Sheets IMAGE()), and shared tabs (our BFCM 2025, Keepa request,
data gaps, event watch).

Inputs (all under ./data): cc/, ours/, dd_out/asins.json, pt_summary.json,
strategy/{pid}.json, catalog/catalog_{com,ca}.json, catalog/dd_images.json, skus/{pid}_{mkt}.json
Usage: python3 build_research.py OUT.xlsx IMAGES_CSV
"""
import json, glob, os, re, sys, csv, statistics, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.comments import Comment
from openpyxl.workbook.defined_name import DefinedName

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT, IMG_CSV = sys.argv[1], sys.argv[2]
NO_IMAGE_FORMULA = "--no-image-formula" in sys.argv   # validation build for LibreOffice

def jl(p, d=None):
    try:
        return json.load(open(p))
    except Exception:
        return d

# ------------------------------------------------------------------ products
PRODUCTS = [
    (59, "Bamboo", "DC B4", "Hero: rank and profit"), (30, "Bamboo", "DC B6", "Hero: rank and profit"),
    (32, "Bamboo", "SL B6", "Core"), (36, "Bamboo", "SL B4", "Core"),
    (73, "Bamboo", "DC Bamboo Fitted", "Excluded (ranking variations OOS to Dec 3)"), (40, "Bamboo", "SL Bamboo Pillowcase", "Other"),
    (37, "Satin", "DC S4", "Clearance with margin"), (31, "Satin", "DC S6", "Clearance with margin"),
    (39, "Satin", "SSS4", "Clearance with margin"), (74, "Satin", "SL Satin 6pc", "Clearance with margin"),
    (38, "Satin", "DC Satin Fitted", "Opportunistic"),
    (55, "Silk", "DC Silk Pillowcase", "Gifting"), (56, "Silk", "SL Mask Contoured", "Gifting"), (57, "Silk", "SL Mask Velcro", "Gifting"),
    (48, "Cooling", "DC Cooling 4pc", "Off-season (aged variations only)"), (45, "Cooling", "SL Cooling 4pc", "Off-season (aged variations only)"),
    (76, "Cooling", "SL Cooling 6pc", "Off-season (aged variations only)"), (69, "Cooling", "CL Cooling Sheets", "Launch"),
    (70, "Cooling", "CL Pillowcases", "Launch"), (43, "Cooling", "SL Cooling Pillowcase", "Off-season"),
    (42, "Cooling", "SL Cooling Comforter", "Off-season (lost $2.4K at BFCM 2025)"), (44, "Cooling", "SL Cooling Fitted", "Off-season"),
    (46, "Other", "SL Quilt Set", "Liquidation"), (53, "Other", "DC Linen Curtains", "Liquidation"),
    (49, "Other", "DC Beach Towel", "Other"), (58, "Other", "DC Welcome Sign", "Other"), (33, "Other", "DC Chair Cover", "Other"),
]
PINFO = {p[0]: p for p in PRODUCTS}

cc = {(int(d["product_id"]), d["marketplace"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/cc/*.json")) if d}
ours = {(int(d["product_id"]), d["marketplace"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/ours/*.json")) if d}
skus = {(int(d["product_id"]), d["marketplace"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/skus/*.json")) if d and "product_id" in d}
strat = {int(d["pid"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/strategy/*.json")) if d and "pid" in d}
ddj = jl(f"{DATA}/dd_out/asins.json", {}) or {}
dd, ddb = ddj.get("asins", {}), ddj.get("benchmarks", {})
pt = jl(f"{DATA}/pt_summary.json", {}) or {}
ddimg = jl(f"{DATA}/catalog/dd_images.json", {}) or {}
for _k, _v in (jl(f"{DATA}/catalog/dd_images_extra.json", {}) or {}).items():
    ddimg.setdefault(_k, _v)
catalog = {}
for mk, f in (("US", "catalog_com.json"), ("CA", "catalog_ca.json")):
    c = jl(f"{DATA}/catalog/{f}", {}) or {}
    catalog[mk] = {it["asin"]: it for it in c.get("items", []) if it.get("asin")}

IMG_RE = re.compile(r"^https://[a-z0-9.-]*amazon\.com/images/I/[A-Za-z0-9+%._-]+\.(jpg|png|jpeg|gif)$")
def good_img(u):
    return u if isinstance(u, str) and IMG_RE.match(u) else None

def econ(e):
    e = e or {}
    b = e.get("blended") if isinstance(e.get("blended"), dict) else e
    g = lambda *ks: next((b.get(k) for k in ks if b.get(k) is not None), None)
    units = g("units_28d", "units28d", "units", "units_28d_sum_of_sizes")
    if units is None and isinstance(e.get("by_size"), list):
        us = [s.get("units_28d") for s in e["by_size"] if s.get("units_28d") is not None]
        units = sum(us) if us else None
    be = g("break_even_acos", "be_acos")
    if be is not None and abs(be) > 1.5:
        be = be / 100
    return {"price": g("blended_price", "price"), "contribution": g("contribution_per_unit", "contribution"), "be_acos": be, "units_28d": units}

SIZE_RE = re.compile(r"\b(california king|cal king|split king|king|queen|full|twin xl|twin|standard|euro|one size)\b", re.I)
def parse_size(t):
    m = SIZE_RE.search(t or "")
    if not m:
        return None
    s = m.group(1).lower()
    return {"cal king": "California King", "california king": "California King", "twin xl": "Twin XL", "split king": "Split King"}.get(s, s.title())

COLOURS = ["white", "black", "grey", "gray", "silver", "navy", "blue", "light blue", "baby blue", "sage", "green", "olive", "taupe", "beige", "ivory",
           "cream", "creme", "champagne", "gold", "pink", "blush", "rose", "rosewood", "burgundy", "wine", "red", "purple", "lavender", "lilac",
           "charcoal", "brown", "chocolate", "mocha", "khaki", "sand", "linen", "teal", "aqua", "mint", "coral", "yellow", "orange", "graphite", "slate"]
def parse_colour(t):
    t = t or ""
    m = re.search(r"\(([^()]*)\)\s*$", t)
    if m:
        parts = [p.strip() for p in m.group(1).split(",")]
        for p in parts:
            if not SIZE_RE.fullmatch(p.strip() or "x"):
                if any(c in p.lower() for c in COLOURS) or len(parts) > 1:
                    if not re.search(r"\d", p) or any(c in p.lower() for c in COLOURS):
                        return p
    tl = t.lower()
    hits = [c for c in COLOURS if re.search(rf"\b{c}\b", tl)]
    return max(hits, key=len).title() if hits else None

def fmt(x, kind="$"):
    if not isinstance(x, (int, float)):
        return "n/a"
    return f"${x:,.2f}" if kind == "$" else f"{x:.0%}" if kind == "%" else f"{x:,.0f}"

# ------------------------------------------------------------------ styles
FONT = "Arial"
def F(**k):
    k.setdefault("size", 9)
    return Font(name=FONT, **k)
C_INK, C_NAVY, C_SUB = "1B2A41", "1F3864", "5B6B82"
HDR = PatternFill("solid", fgColor=C_NAVY)
SEC = PatternFill("solid", fgColor="E8EDF5")
FILL = {k: PatternFill("solid", fgColor=v) for k, v in {
    "cc": "E2EFDA", "dd": "DDEBF7", "st": "EDE7F6", "vis": "F3E5F5", "kp": "FCE4D6", "str": "FFF2CC", "calc": "F2F2F2",
    "ours": "FFF8E1", "flag": "F8CBAD", "ok": "C6EFCE", "tile": "F7F9FC"}.items()}
INPUT = PatternFill("solid", fgColor="FFFF99")
thin = Side(style="thin", color="C9D1DE")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
BLUE = "0000FF"
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
IMG_ROW_H = 62

img_rows = []   # (role, product, marketplace, brand, asin, url) for the image download request

def put_image(ws, cell, url, role, product, mkt, brand, asin):
    u = good_img(url)
    c = ws[cell]
    c.border = BOX
    c.alignment = CENTER
    if u:
        img_rows.append((role, product, mkt, brand, asin, u))
        if NO_IMAGE_FORMULA:
            c.value = "[image]"
        else:
            c.value = f'=_xlfn.IMAGE("{u}")'
    else:
        c.value = "IMAGE MISSING"
        c.font = F(size=7, color="C00000", bold=True)

def section(ws, row, text, ncols, sub=None):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row=row, column=1, value=text)
    c.font = F(size=11, bold=True, color=C_NAVY)
    c.fill = SEC
    c.alignment = Alignment(vertical="center")
    ws.row_dimensions[row].height = 20
    if sub:
        ws.merge_cells(start_row=row + 1, start_column=1, end_row=row + 1, end_column=ncols)
        s = ws.cell(row=row + 1, column=1, value=sub)
        s.font = F(size=8, italic=True, color=C_SUB)
        return row + 2
    return row + 1

def header_row(ws, row, cols, start_col=1, height=48):
    for i, c in enumerate(cols):
        h = ws.cell(row=row, column=start_col + i, value=c[1])
        h.font = F(bold=True, color="FFFFFF", size=8)
        h.fill = HDR
        h.alignment = CENTER
        h.border = BOX
        if len(c) > 3 and c[3]:
            h.comment = Comment(c[3], "Tracker")
    ws.row_dimensions[row].height = height

# ------------------------------------------------------------------ shared lookups
def our_profile(pid, mkt):
    s = skus.get((pid, mkt)) or skus.get((pid, "US")) or {}
    p = s.get("profile") or {}
    o = (cc.get((pid, mkt)) or cc.get((pid, "US")) or {}).get("our", {})
    return p, o

def our_title_and_image(pid, mkt):
    p, o = our_profile(pid, mkt)
    cat = catalog.get(mkt, {}) or {}
    best = (p.get("thumbnail") or {}).get("childAsin") or o.get("best_child_asin")
    parent = p.get("parentAsin") or o.get("parent_asin")
    title = None
    img = good_img((p.get("thumbnail") or {}).get("url"))
    for a in (best, parent):
        it = cat.get(a) or catalog.get("US", {}).get(a)
        if it:
            title = title or it.get("title")
            img = img or good_img(it.get("imageUrl"))
    if not title:
        kids = [it for it in cat.values() if it.get("parentAsin") == parent]
        if kids:
            title = kids[0].get("title")
            img = img or good_img(kids[0].get("imageUrl"))
    return title, img, best, parent

def our_variations(pid, mkt):
    """SKU rows joined to catalog children (image, title)."""
    p, o = our_profile(pid, mkt)
    parent = p.get("parentAsin") or o.get("parent_asin")
    cat = catalog.get(mkt, {}) or {}
    s = (skus.get((pid, mkt)) or {}).get("skus") or []
    rows, seen = [], set()
    def g(x, *ks):
        return next((x.get(k) for k in ks if x.get(k) not in (None, "")), None)
    for x in s:
        asin = g(x, "asin", "childAsin", "child_asin", "ASIN")
        it = cat.get(asin) or catalog.get("US", {}).get(asin) or {}
        title = it.get("title")
        rows.append({
            "sku": g(x, "sku", "SKU", "sellerSku"), "asin": asin, "title": title,
            "size": g(x, "size") or parse_size(title), "colour": g(x, "colour", "color") or parse_colour(title),
            "price": g(x, "price"), "contribution": g(x, "contribution", "contributionPerUnit", "contribution_per_unit"),
            "be_acos": g(x, "beAcos", "breakEvenAcos", "be_acos", "break_even_acos"), "units_28d": g(x, "units28d", "units_28d", "units"),
            "status": g(x, "status") or it.get("status"), "image": good_img(it.get("imageUrl")),
        })
        if asin:
            seen.add(asin)
    for a, it in cat.items():   # catalog children not in the SKU list
        if it.get("parentAsin") == parent and a not in seen and a != parent:
            rows.append({"sku": None, "asin": a, "title": it.get("title"), "size": parse_size(it.get("title")),
                         "colour": parse_colour(it.get("title")), "price": None, "contribution": None, "be_acos": None,
                         "units_28d": None, "status": it.get("status"), "image": good_img(it.get("imageUrl"))})
    for r in rows:
        if isinstance(r["be_acos"], (int, float)) and abs(r["be_acos"]) > 1.5:
            r["be_acos"] = r["be_acos"] / 100
    rows.sort(key=lambda r: (-(r["units_28d"] or 0), r["size"] or "", r["colour"] or ""))
    return rows

def comp_image(cp):
    for a in (cp.get("child_asin"), cp.get("parent_asin")):
        if a and good_img((ddimg.get(a) or {}).get("imageUrl")):
            return ddimg[a]["imageUrl"], a
    st = None
    for h in (cp.get("_hero") or []):
        if good_img((ddimg.get(h[0]) or {}).get("imageUrl")):
            return ddimg[h[0]]["imageUrl"], h[0]
    return None, None

def comp_title(cp):
    for a in (cp.get("child_asin"), cp.get("parent_asin")):
        t = (ddimg.get(a) or {}).get("title") or (dd.get(a) or {}).get("title")
        if t:
            return t
    return (cp.get("name") or "").strip()

def lift_of(pid, mkt="US"):
    d = ours.get((pid, mkt)) or {}
    w1, w2, w3 = d.get("w1_bfcm") or {}, d.get("w2_pre30") or {}, d.get("w3_dec") or {}
    t1, t2, t3 = w1.get("total_sales_derived"), w2.get("total_sales_derived"), w3.get("total_sales_derived")
    if not (t1 and t2):
        return None
    return {"lift": (t1 / 12) / (t2 / 30), "dec": ((t3 / 30) / (t2 / 30)) if t3 else None, "tacos": w1.get("tacos"),
            "pre_tacos": w2.get("tacos"), "bf_total": t1, "pre_total": t2, "dec_total": t3, "spend": w1.get("spend"), "ad_sales": w1.get("ad_sales")}

STOCK_ALIAS = {"B4": 59, "B6": 30, "S4": 37, "S6": 31, "Satin Fitted": 38, "SSS4": 39, "SL B6": 32,
               "Decolure - Cooling Sheets 4 Piece": 48, "Sleephoria - Cooling Sheets 4 Piece": 45, "Sleephoria - Cooling Fitted Sheet": 44,
               "Sleephoria - Cooling Comforter": 42, "Decolure - Silk Pillowcase": 55}
stock_oos = {}
_sp = f"{DATA}/stock/our_stock_bfcm2025.csv"
if os.path.exists(_sp):
    _agg = {}
    for row in csv.DictReader(open(_sp, encoding="utf-8-sig")):
        if row["fba_available_units"] in ("", None) or not ("2025-11-20" <= row["date"] <= "2025-12-01"):
            continue
        name = row["product_name"].split("|")[0].strip() if "|" in row["product_name"] else row["product_name"]
        pid_ = STOCK_ALIAS.get(name)
        if pid_ is None:
            continue
        k = (pid_, row["marketplace"], row["child_asin"], row["date"])
        _agg[k] = _agg.get(k, 0) + float(row["fba_available_units"])
    _vel = {}
    for (pid_, m_), sd in skus.items():
        for x in sd.get("skus") or []:
            if x.get("asin"):
                _vel[(m_, x["asin"])] = _vel.get((m_, x["asin"]), 0) + (x.get("units28d") or 0)
    per = {}
    for (pid_, m_, a_, dt_), q in _agg.items():
        e_ = per.setdefault((pid_, m_), {}).setdefault(a_, [0, 0])
        e_[1] += 1
        e_[0] += (q == 0)
    for key, asins in per.items():
        tot = sum(_vel.get((key[1], a_), 0) for a_ in asins)
        oos = {a_: v for a_, v in asins.items() if v[0] > 0}
        w = sum(_vel.get((key[1], a_), 0) * v[0] / v[1] for a_, v in oos.items()) / tot if tot else None
        top = sorted(oos.items(), key=lambda kv: -_vel.get((key[1], kv[0]), 0))[:4]
        stock_oos[key] = {"asins": len(asins), "oos_asins": len(oos), "weighted": w,
                          "top": "; ".join(f"{a_} {v[0]}/{v[1]} days" for a_, v in top)}

# ------------------------------------------------------------------ assemble competitor records
records = []      # one per (product, marketplace, competitor) for the Data sheet and the dashboard
TABS = []         # (pid, mkt, tab name)
def tab_name(pid, mkt):
    short = PINFO[pid][2]
    return f"{mkt} {short}"[:31]

for pid, fam, short, role in PRODUCTS:
    for mkt in ("US", "CA"):
        d = cc.get((pid, mkt))
        if not d:
            continue
        TABS.append((pid, mkt, tab_name(pid, mkt)))
        if mkt == "CA":
            continue     # Command Center holds no CA competitor snapshots
        st = {r["cid"]: r for r in (strat.get(pid) or {}).get("competitors", []) if "cid" in r and "error" not in r}
        for cp in d.get("competitors", []):
            s = st.get(cp.get("id")) or {}
            cp["_hero"] = s.get("hero_child_asins") or []
            ch = cp.get("child_asin")
            ddr = dd.get(ch) or dd.get(cp.get("parent_asin")) or {}
            v = pt.get(ch) or {}
            img, img_asin = comp_image(cp)
            title = comp_title(cp)
            reach = s.get("reach") or {}
            rec = {
                "pid": pid, "mkt": mkt, "family": fam, "product": short, "tab": tab_name(pid, mkt), "role": role,
                "cid": cp.get("id"), "brand": (cp.get("brand") or "").strip(), "parent": cp.get("parent_asin"), "child": ch,
                "title": title, "tier": cp.get("tier") or "Untiered", "image": img, "image_asin": img_asin,
                "price": cp.get("price"), "lp": cp.get("list_price"), "bsr": cp.get("bsr"), "wk": cp.get("est_weekly_sales"),
                "rating": cp.get("rating"), "reviews": cp.get("reviews"), "seen": cp.get("seen_on"),
                "size": parse_size(title), "colour": parse_colour(title),
                "var": ddr.get("numberOfVariations") or (ddimg.get(ch) or {}).get("numberOfVariations") or s.get("child_asins_total"),
                "var_src": "Data Dive" if ddr.get("numberOfVariations") or (ddimg.get(ch) or {}).get("numberOfVariations") else ("ASINsight child ASINs" if s.get("child_asins_total") else None),
                "listed": ddr.get("listingCreationDate"), "dd30": ddr.get("sales"), "ful": ddr.get("fulfillment"),
                "country": ddr.get("sellerCountry"), "adkw": ddr.get("advertisedKwsPercent"), "tos": ddr.get("tosSvAdsPercent"),
                "asi_tr": cp.get("asinsight_traffic_7d"), "asi_kw": s.get("keywords") or cp.get("asinsight_keywords") or None,
                "org_pct": s.get("organic_pct"), "ad_pct": s.get("ad_pct"), "top_kw": s.get("top_kw"), "top_kw_pct": s.get("top_kw_pct"),
                "r_sp": reach.get("SP"), "r_sb": reach.get("SB"), "r_sbv": reach.get("SBV"), "r_ac": reach.get("AC"),
                "contested": s.get("contested"), "we_win": s.get("we_win"), "we_lose": s.get("we_lose"),
                "theirs_only": s.get("theirs_only_kw"), "theirs_only_share": s.get("theirs_only_share"),
                "ppc_none": s.get("ppc_we_run_none"), "ppc_aggr": s.get("ppc_they_more_aggressive"), "ad_gap": s.get("ad_gap"),
                "comparable": s.get("comparable"), "hero": ", ".join(f"{a} ({sh:.0%})" for a, sh in (s.get("hero_child_asins") or [])[:5] if isinstance(sh, (int, float))),
                "pd_pre": v.get("pd26_pre_org"), "pd": v.get("pd26_org"), "pd_pre_ad": v.get("pd26_pre_ad"), "pd_ad": v.get("pd26_ad"),
                "q2": v.get("q2_org"), "l30": v.get("last30_org"),
            }
            records.append(rec)

tier_rank = {"Aspirational": 0, "Beatable": 1, "Poor": 2, "Untiered": 3}
records.sort(key=lambda r: ([p[0] for p in PRODUCTS].index(r["pid"]), tier_rank.get(r["tier"], 3), -(r["wk"] or 0)))

# our same-size price per product
our_size_price, our_blend = {}, {}
for (pid, mkt), d in cc.items():
    e = d.get("our", {}).get("economics") or {}
    bs = e.get("by_size") or (e.get("blended") or {}).get("by_size") or []
    our_size_price[(pid, mkt)] = {({"Cal King": "California King"}.get(x.get("size"), x.get("size"))): x.get("price") for x in bs if x.get("price") is not None}
    our_blend[(pid, mkt)] = econ(e)["price"]
for r in records:
    bys = our_size_price.get((r["pid"], "US"), {})
    if r["size"] and bys.get(r["size"]) is not None:
        r["our_same"], r["basis"] = bys[r["size"]], f"Same size ({r['size']})"
    elif bys.get("Queen") is not None:
        r["our_same"], r["basis"] = bys["Queen"], "Size not stated - vs our Queen"
    elif our_blend.get((r["pid"], "US")) is not None:
        r["our_same"], r["basis"] = our_blend[(r["pid"], "US")], "vs our blended price"
    else:
        r["our_same"], r["basis"] = None, "No price for us"

if "--data-only" in sys.argv:
    raise SystemExit(0)

# ------------------------------------------------------------------ workbook
wb = Workbook()
wb.calculation.fullCalcOnLoad = True
rd = wb.active
rd.title = "README"
rd.sheet_view.showGridLines = False

# ================================================================== per-product tabs
COMP_COLS = [
    # key, header, width, group, comment, numfmt
    ("img", "Image", 11, "id", "Live product image (Excel 365 / Google Sheets IMAGE). 'IMAGE MISSING' = no verified image URL; see Data Gaps.", None),
    ("brand", "Brand", 14, "id", None, None),
    ("title", "Product title", 34, "id", None, None),
    ("tier", "Tier", 9, "id", "Command Center mapping tier against this product.", None),
    ("parent", "Parent ASIN", 11, "id", None, None),
    ("child", "Tracked child ASIN", 11, "id", None, None),
    ("size", "Size (title)", 8, "id", None, None),
    ("colour", "Colour (title)", 9, "id", None, None),
    ("var", "Variations", 7, "dd", "Variation count: Data Dive family count, else ASINsight child-ASIN count.", "#,##0"),
    ("hero", "Hero child ASINs (share of their visibility)", 26, "st", "The fewest child ASINs carrying 80% of this competitor's ASINsight impressions.", None),
    ("price", "Price ($)", 8, "cc", None, "$#,##0.00"),
    ("lp", "List Price ($)", 8, "cc", None, "$#,##0.00"),
    ("lp_pct", "List Price % over", 7, "calc", None, "0.0%"),
    ("band", "STR band", 10, "calc", "<=12% over price = zone where Amazon reliably shows the strikethrough (if sold at it).", None),
    ("our_same", "Our price, same size ($)", 8, "calc", None, "$#,##0.00"),
    ("gap", "Their price vs ours", 7, "calc", None, "+0%;-0%;0%"),
    ("basis", "Comparison basis", 11, "calc", None, None),
    ("bsr", "BSR", 8, "cc", None, "#,##0"),
    ("wk", "Est weekly units", 7, "cc", None, "#,##0"),
    ("rev", "Est monthly revenue ($)", 9, "calc", None, "$#,##0"),
    ("rating", "Rating", 5, "cc", None, "0.0"),
    ("reviews", "Reviews", 7, "cc", None, "#,##0"),
    ("listed", "Listed", 9, "dd", None, "yyyy-mm-dd"),
    ("ful", "Fulfil.", 5, "dd", None, None),
    ("country", "Seller country", 6, "dd", None, None),
    ("asi_tr", "ASINsight 7d traffic", 9, "st", "Impression-like 7-day figure, not clicks or sales. Blank = unmeasured.", "#,##0"),
    ("asi_kw", "Keywords ranked", 7, "st", None, "#,##0"),
    ("org_pct", "Organic share of traffic", 7, "st", None, "0%"),
    ("ad_pct", "Ad share of traffic", 7, "st", None, "0%"),
    ("top_kw", "Top keyword", 14, "st", None, None),
    ("r_sp", "SP reach", 6, "st", "Share of their traffic on keywords where they hold a Sponsored Products placement.", "0%"),
    ("r_sb", "SB reach", 6, "st", None, "0%"),
    ("r_sbv", "SB video reach", 6, "st", None, "0%"),
    ("r_ac", "Amazon's Choice reach", 6, "st", None, "0%"),
    ("contested", "Shared keywords", 7, "st", "Keywords both they and we rank on (our latest ASINsight export).", "#,##0"),
    ("we_win", "We win", 6, "st", None, "#,##0"),
    ("we_lose", "We lose", 6, "st", None, "#,##0"),
    ("theirs_only", "Their keywords we miss", 7, "st", None, "#,##0"),
    ("ppc_none", "KWs they advertise, we don't", 7, "st", None, "#,##0"),
    ("ppc_aggr", "KWs they out-advertise us", 7, "st", None, "#,##0"),
    ("pd_lift", "Prime Day 2026 organic vis lift", 7, "calc", "Organic visibility score Jun 23-26 vs Jun 1-20, 2026 (baseline score 5+).", '0.00"x"'),
    ("trend", "Organic trend (Aug-Sep vs Q2)", 7, "calc", None, "+0%;-0%;0%"),
    ("str_show", "STR showing now? (Y/N)", 7, "str", None, None),
    ("str_label", "STR label", 8, "str", None, None),
    ("bf_type", "BFCM 2025 deal type", 10, "kp", None, None),
    ("bf_dates", "BFCM 2025 deal dates", 10, "kp", None, None),
    ("bf_pre", "Pre-event price ($)", 8, "kp", None, "$#,##0.00"),
    ("bf_low", "BFCM 2025 low ($)", 8, "kp", None, "$#,##0.00"),
    ("bf_disc", "BFCM 2025 discount", 7, "calc", None, "0.0%"),
    ("bsr_pre", "BSR pre-event", 8, "kp", None, "#,##0"),
    ("bsr_bf", "BSR BFCM wk", 8, "kp", None, "#,##0"),
    ("bsr_lift", "BSR lift (x)", 6, "calc", None, '0.0"x"'),
    ("bf_oos", "OOS in BFCM? (Y/N)", 6, "kp", None, None),
    ("notes", "Notes", 22, "kp", None, None),
]
CK = {c[0]: i + 1 for i, c in enumerate(COMP_COLS)}
CLt = {k: CL(v) for k, v in CK.items()}
NC = len(COMP_COLS)
GROUP_NAMES = {"id": "COMPETITOR", "cc": "PRICE & SALES - Command Center (Oct 12)", "dd": "LISTING - Data Dive", "calc": "",
               "st": "SEARCH STRATEGY - Command Center ASINsight", "str": "STR NOW (fill)", "kp": "BFCM 2025 - fill from Keepa"}

product_cells = {}   # (pid, mkt) -> dict of key cell refs for dashboard
comp_cells = {}      # record index -> (tab, row)

for pid, mkt, tname in TABS:
    fam, short, role = PINFO[pid][1], PINFO[pid][2], PINFO[pid][3]
    ws = wb.create_sheet(tname)
    ws.sheet_view.showGridLines = False
    ws.sheet_view.zoomScale = 90
    for i, c in enumerate(COMP_COLS, 1):
        ws.column_dimensions[CL(i)].width = c[2]
    p, o = our_profile(pid, mkt)
    title, img, best, parent = our_title_and_image(pid, mkt)
    e = econ(o.get("economics"))
    lf = lift_of(pid, mkt)
    brand = p.get("brand") or o.get("brand")
    pname = f"{brand or ''} {p.get('name') or o.get('name') or short}".strip()

    # ---- title band
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=NC)
    t = ws.cell(row=1, column=1, value=f"{pname}  ·  {('Amazon.com (US)' if mkt == 'US' else 'Amazon.ca (CA)')}  ·  {fam}  ·  BFCM role: {role}")
    t.font = F(size=14, bold=True, color="FFFFFF"); t.fill = HDR; t.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 28
    ws.cell(row=2, column=1, value="← Dashboard").hyperlink = "#'Dashboard'!A1"
    ws.cell(row=2, column=1).font = F(color="0563C1", underline="single")

    # ---- section 1: our product
    r = section(ws, 3, "1 · OUR PRODUCT", NC)
    ws.merge_cells(start_row=r, start_column=1, end_row=r + 5, end_column=2)
    put_image(ws, f"A{r}", img, "OURS - parent/best child", pname, mkt, brand, best)
    for rr in range(r, r + 6):
        ws.row_dimensions[rr].height = 22
    facts = [
        ("Title", title or "Title not in catalog pull - see Data Gaps"), ("Brand", brand), ("Marketplace", "Amazon.com (US)" if mkt == "US" else "Amazon.ca (CA)"),
        ("Parent ASIN", parent), ("Best-selling child ASIN", best), ("Stage", p.get("stage") or o.get("stage")),
        ("Total variations (SKUs)", p.get("skuCount") or o.get("sku_count")), ("Sizes", ", ".join(p.get("sizes") or o.get("sizes") or []) or None),
        ("Colours", ", ".join(p.get("colours") or []) or (f"{o.get('colour_count')} colours" if o.get("colour_count") else None)),
        ("Blended price", fmt(e["price"])), ("Contribution / unit", fmt(e["contribution"])), ("Break-even ACoS", fmt(e["be_acos"], "%")),
        ("Units last 28 days", fmt(e["units_28d"], "n")),
    ]
    for i, (k, v) in enumerate(facts):
        rr, cc0 = r + (i % 7), 3 + (i // 7) * 8
        a = ws.cell(row=rr, column=cc0, value=k); a.font = F(bold=True, color=C_SUB, size=8)
        ws.merge_cells(start_row=rr, start_column=cc0 + 1, end_row=rr, end_column=cc0 + 6)
        b = ws.cell(row=rr, column=cc0 + 1, value=v); b.font = F(size=9, bold=(k == "Title")); b.alignment = Alignment(wrap_text=(k == "Title"), vertical="center")
    if title:
        ws.row_dimensions[r].height = 34
    r += 7

    # ---- KPI strip (BFCM 2025 + market position)
    comps = [x for x in records if x["pid"] == pid and x["mkt"] == mkt]
    kpis = [
        ("BFCM 2025 lift", f"{lf['lift']:.2f}x" if lf else "n/a", "daily sales, BFCM wk vs 30 days before (derived)"),
        ("BFCM 2025 TACoS", f"{lf['tacos']:.1f}%" if lf and lf.get("tacos") is not None else "n/a", f"vs {lf['pre_tacos']:.1f}% before" if lf and lf.get("pre_tacos") is not None else ""),
        ("Dec 2025 vs pre-event", f"{lf['dec']:.2f}x" if lf and lf.get("dec") else "n/a", "December daily sales vs Oct 21-Nov 19"),
        ("Competitors mapped", str(len(comps)) if mkt == "US" else "0 (CA not mapped)", "Command Center map"),
        ("Priced below us", str(sum(1 for x in comps if isinstance(x.get("price"), (int, float)) and x.get("our_same") and x["price"] < x["our_same"])) if comps else "n/a", "same size, else vs our Queen"),
        ("List Price within 12%", str(sum(1 for x in comps if isinstance(x.get("lp"), (int, float)) and isinstance(x.get("price"), (int, float)) and 0 < x["lp"] / x["price"] - 1 <= 0.12)) if comps else "n/a", "most likely to show a strikethrough"),
    ]
    for i, (k, v, sub) in enumerate(kpis):
        c0 = 1 + i * 4
        ws.merge_cells(start_row=r, start_column=c0, end_row=r, end_column=c0 + 3)
        ws.merge_cells(start_row=r + 1, start_column=c0, end_row=r + 1, end_column=c0 + 3)
        ws.merge_cells(start_row=r + 2, start_column=c0, end_row=r + 2, end_column=c0 + 3)
        a = ws.cell(row=r, column=c0, value=k.upper()); a.font = F(size=7, bold=True, color=C_SUB); a.fill = FILL["tile"]
        b = ws.cell(row=r + 1, column=c0, value=v); b.font = F(size=16, bold=True, color=C_INK); b.fill = FILL["tile"]
        s = ws.cell(row=r + 2, column=c0, value=sub); s.font = F(size=7, color=C_SUB); s.fill = FILL["tile"]
    ws.row_dimensions[r + 1].height = 24
    r += 4

    # ---- section 2: our variations
    vars_ = our_variations(pid, mkt)
    r = section(ws, r, f"2 · OUR VARIATIONS ({len(vars_)} listed)", NC,
                "Every SKU / child ASIN with its image, size, colour, price and 28-day units. Images from the Data Dive seller catalog; sizes and colours from the SKU data, else read from the title.")
    VC = [("img", "Image", 11), ("asin", "Child ASIN", 11), ("sku", "SKU", 14), ("title", "Title", 34), ("size", "Size", 8), ("colour", "Colour", 9),
          ("price", "Price ($)", 8), ("contribution", "Contribution ($)", 8), ("be_acos", "Break-even ACoS", 7), ("units_28d", "Units 28d", 7), ("status", "Status", 8),
          ("hero", "Our hero ASIN? (share of our visibility)", 10)]
    header_row(ws, r, [(a, b, c) for a, b, c in VC], height=34)
    r += 1
    ourhero = {a: sh for a, sh in ((strat.get(pid) or {}).get("our_hero_asins") or []) if isinstance(sh, (int, float))} if mkt == "US" else {}
    if not vars_:
        ws.cell(row=r, column=1, value="No variation rows yet - our per-SKU pull or catalog is missing for this product (see Data Gaps).").font = F(italic=True, color="C00000")
        r += 1
    for v in vars_:
        ws.row_dimensions[r].height = IMG_ROW_H
        put_image(ws, f"A{r}", v["image"], "OURS - variation", pname, mkt, brand, v["asin"])
        vals = [None, v["asin"], v["sku"], v["title"], v["size"], v["colour"], v["price"], v["contribution"], v["be_acos"], v["units_28d"], v["status"],
                (f"Yes ({ourhero[v['asin']]:.0%})" if v["asin"] in ourhero else None)]
        for j, val in enumerate(vals[1:], 2):
            c = ws.cell(row=r, column=j, value=val); c.font = F(); c.border = BOX; c.alignment = WRAP
        ws.cell(row=r, column=7).number_format = "$#,##0.00"; ws.cell(row=r, column=8).number_format = "$#,##0.00"
        ws.cell(row=r, column=9).number_format = "0%"; ws.cell(row=r, column=10).number_format = "#,##0"
        r += 1
    r += 1

    # ---- section 3: our BFCM 2025 & visibility
    r = section(ws, r, "3 · OUR BFCM 2025 RESULT & EVENT VISIBILITY", NC)
    d = ours.get((pid, mkt)) or {}
    w1, w2, w3 = d.get("w1_bfcm") or {}, d.get("w2_pre30") or {}, d.get("w3_dec") or {}
    rows3 = [("Window", "Ad spend", "Ad sales", "ACoS", "TACoS", "Total sales (derived)", "Ad orders", "CVR"),
             ("Pre-event Oct 21 - Nov 19, 2025 (30d)",) + tuple(w2.get(k) for k in ("spend", "ad_sales", "acos", "tacos", "total_sales_derived", "orders", "cvr")),
             ("BFCM week Nov 20 - Dec 1, 2025 (12d)",) + tuple(w1.get(k) for k in ("spend", "ad_sales", "acos", "tacos", "total_sales_derived", "orders", "cvr")),
             ("December 2 - 31, 2025 (30d)",) + tuple(w3.get(k) for k in ("spend", "ad_sales", "acos", "tacos", "total_sales_derived", "orders", "cvr"))]
    for i, row_ in enumerate(rows3):
        for j, val in enumerate(row_):
            c = ws.cell(row=r, column=[1, 4, 5, 6, 7, 8, 10, 11][j], value=val)
            c.border = BOX
            if i == 0:
                c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR
            else:
                c.font = F()
                c.number_format = ["@", "$#,##0", "$#,##0", '0.0"%"', '0.0"%"', "$#,##0", "#,##0", '0.00"%"'][j]
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        r += 1
    v = pt.get(best) or {}
    vis = (f"Command Center visibility for our best child {best}: organic score {v.get('bf25_pre_org')} before BFCM 2025 → {v.get('bf25_org')} in BFCM week; "
           f"Prime Day 2026 {v.get('pd26_pre_org')} → {v.get('pd26_org')}; Aug-Sep 2026 {v.get('last30_org')}." if v else "No Command Center visibility history for our best child ASIN.")
    if mkt == "CA":
        vis = "Figures above are Amazon.ca in CAD. Visibility history is held for US ASINs only."
    so = stock_oos.get((pid, mkt))
    if so:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        txt = (f"Stock in BFCM week 2025 (Command Center FBA snapshots, child-ASIN level): {so['oos_asins']} of {so['asins']} variations hit zero FBA stock on at least one observed day"
               + (f"; weighted by today's sales mix that is ~{so['weighted']:.1%} of variation-days lost" if so['weighted'] is not None else "")
               + (f". Most important: {so['top']}." if so['top'] else ".")
               + " Snapshots missing: US Nov 26-27 and Dec 1 (Cyber Monday); CA Nov 24, 29-30.")
        c = ws.cell(row=r, column=1, value=txt); c.font = F(size=8.5, bold=True, color=C_INK); c.alignment = WRAP
        ws.row_dimensions[r].height = 26
        r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
    ws.cell(row=r, column=1, value=vis).font = F(size=8, italic=True, color=C_SUB)
    if not d:
        ws.cell(row=r + 1, column=1, value="No BFCM 2025 PPC data for this product (not advertised or launched after BFCM 2025).").font = F(italic=True, color="C00000")
        r += 1
    r += 2

    # ---- section 4: competitor landscape
    r = section(ws, r, f"4 · COMPETITOR LANDSCAPE ({len(comps)} mapped)", NC,
                "Sorted by tier, then estimated weekly units. Green = Command Center price/sales; blue = Data Dive listing; purple = Command Center search strategy (ASINsight); yellow = fill from Keepa / page check.")
    if mkt == "CA":
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        ws.cell(row=r, column=1, value="The Command Center holds no Amazon.ca competitor snapshots. Map the CA competitor set (Data Gaps #6) and pull Keepa .ca - see AGENT_PROMPTS Prompt 9.").font = F(bold=True, color="C00000")
        r += 2
        product_cells[(pid, mkt)] = {"tab": tname}
        continue
    # group row
    gr = r
    spans, prev, start = [], None, 1
    for i, c in enumerate(COMP_COLS, 1):
        g = c[3] if c[3] != "calc" else prev
        if g != prev:
            if prev is not None:
                spans.append((prev, start, i - 1))
            prev, start = g, i
    spans.append((prev, start, NC))
    for g, a, b in spans:
        if b > a:
            ws.merge_cells(start_row=gr, start_column=a, end_row=gr, end_column=b)
        cell = ws.cell(row=gr, column=a, value=GROUP_NAMES.get(g, ""))
        cell.font = F(bold=True, color=C_NAVY, size=8); cell.fill = FILL.get(g, FILL["calc"]); cell.alignment = CENTER
    r += 1
    header_row(ws, r, [(c[0], c[1], c[2], c[4]) for c in COMP_COLS])
    hdr_row = r
    r += 1
    first = r
    for x in comps:
        ws.row_dimensions[r].height = IMG_ROW_H
        put_image(ws, f"A{r}", x["image"], "COMPETITOR", pname, mkt, x["brand"], x["image_asin"] or x["child"])
        listed = x.get("listed")
        if isinstance(listed, str) and len(listed) >= 10:
            try:
                listed = dt.date.fromisoformat(listed[:10])
            except ValueError:
                pass
        vals = dict(x, listed=listed)
        for key, hdr, w, grp, com, nf in COMP_COLS[1:]:
            c = ws.cell(row=r, column=CK[key])
            c.border = BOX; c.font = F(); c.alignment = WRAP if key in ("title", "hero", "top_kw", "basis") else Alignment(vertical="top")
            if grp in ("kp", "str"):
                c.fill = INPUT; c.font = F(color=BLUE)
            elif grp == "calc" and key not in ("our_same", "basis"):
                c.fill = FILL["calc"]
            elif key in vals:
                c.value = vals[key]
            if nf:
                c.number_format = nf
        P, LPc = f"{CLt['price']}{r}", f"{CLt['lp']}{r}"
        ws[f"{CLt['lp_pct']}{r}"] = f'=IF(AND(ISNUMBER({LPc}),ISNUMBER({P}),N({P})>0),{LPc}/{P}-1,"")'
        q = f"{CLt['lp_pct']}{r}"
        ws[f"{CLt['band']}{r}"] = f'=IF({q}="","No List Price",IF({q}<=0,"At/below price",IF({q}<=0.12,"<=12% STR zone",IF({q}<=0.25,"12-25%",">25% likely ignored"))))'
        ws[f"{CLt['gap']}{r}"] = f'=IF(AND(ISNUMBER({P}),ISNUMBER({CLt["our_same"]}{r}),N({CLt["our_same"]}{r})>0),{P}/{CLt["our_same"]}{r}-1,"")'
        ws[f"{CLt['rev']}{r}"] = f'=IF(AND(ISNUMBER({P}),ISNUMBER({CLt["wk"]}{r})),{P}*{CLt["wk"]}{r}*52/12,"")'
        pd_pre, pd_ = x.get("pd_pre"), x.get("pd")
        ws[f"{CLt['pd_lift']}{r}"] = (pd_ / pd_pre) if (isinstance(pd_, (int, float)) and isinstance(pd_pre, (int, float)) and pd_pre >= 5) else None
        ws[f"{CLt['trend']}{r}"] = (x["l30"] / x["q2"] - 1) if (isinstance(x.get("l30"), (int, float)) and isinstance(x.get("q2"), (int, float)) and x["q2"] >= 5) else None
        ws[f"{CLt['bf_disc']}{r}"] = f'=IF(AND(ISNUMBER({CLt["bf_pre"]}{r}),ISNUMBER({CLt["bf_low"]}{r}),N({CLt["bf_pre"]}{r})>0),1-{CLt["bf_low"]}{r}/{CLt["bf_pre"]}{r},"")'
        ws[f"{CLt['bsr_lift']}{r}"] = f'=IF(AND(ISNUMBER({CLt["bsr_pre"]}{r}),ISNUMBER({CLt["bsr_bf"]}{r}),N({CLt["bsr_bf"]}{r})>0),{CLt["bsr_pre"]}{r}/{CLt["bsr_bf"]}{r},"")'
        x["_cell"] = (tname, r)
        r += 1
    last = r - 1
    if comps:
        ws.conditional_formatting.add(f"{CLt['band']}{first}:{CLt['band']}{last}", FormulaRule(formula=[f'{CLt["band"]}{first}="<=12% STR zone"'], fill=FILL["ok"]))
        ws.conditional_formatting.add(f"{CLt['gap']}{first}:{CLt['gap']}{last}", FormulaRule(formula=[f'AND(ISNUMBER({CLt["gap"]}{first}),{CLt["gap"]}{first}<0)'], fill=FILL["flag"]))
        for lst, keys in (('"Y,N"', ("str_show", "bf_oos")), ('"List Price,Typical price,Was price,None"', ("str_label",)),
                          ('"Lightning Deal,Best Deal,Prime Exclusive Discount,Coupon only,Price cut only,None,Not live in 2025"', ("bf_type",))):
            dv = DataValidation(type="list", formula1=lst, allow_blank=True); ws.add_data_validation(dv)
            for k in keys:
                dv.add(f"{CLt[k]}{first}:{CLt[k]}{last}")
        ws.auto_filter.ref = f"B{hdr_row}:{CL(NC)}{last}"
    r += 1

    # ---- section 5: insights
    r = section(ws, r, "5 · WHAT THIS MEANS FOR BFCM", NC)
    ins = []
    top = sorted([x for x in comps if isinstance(x.get("wk"), (int, float))], key=lambda x: -x["wk"])[:5]
    if top:
        tot = sum(x["wk"] for x in comps if isinstance(x.get("wk"), (int, float)))
        ourwk = (e["units_28d"] or 0) / 4
        ins.append("Who sells most: " + "; ".join(f"{x['brand']} ~{x['wk']:,}/wk at {fmt(x.get('price'))}" + (f" (List {fmt(x['lp'])}, +{x['lp']/x['price']-1:.0%})" if isinstance(x.get('lp'), (int, float)) and isinstance(x.get('price'), (int, float)) and x['lp'] > x['price'] else "") for x in top)
                   + (f". Tracked rivals ~{tot:,.0f} units/wk; we sell ~{ourwk:,.0f}/wk ({ourwk/(ourwk+tot):.1%} of the tracked set)." if tot else ""))
    z = [x for x in comps if isinstance(x.get("lp"), (int, float)) and isinstance(x.get("price"), (int, float)) and 0 < x["lp"] / x["price"] - 1 <= 0.12]
    if comps:
        ins.append(f"Strikethrough: {sum(1 for x in comps if isinstance(x.get('lp'), (int, float)) and isinstance(x.get('price'), (int, float)) and x['lp'] > x['price'])} of {len(comps)} rivals set a List Price above price; {len(z)} within 12%"
                   + (": " + ", ".join(f"{x['brand']} +{x['lp']/x['price']-1:.0%}" for x in z[:6]) if z else "") + ".")
        below = [x for x in comps if isinstance(x.get("price"), (int, float)) and x.get("our_same") and x["price"] < x["our_same"]]
        ins.append(f"Price: {len(below)} of {len(comps)} rivals sit below our price today (same size where the title states one). Cheapest strong rivals: "
                   + ", ".join(f"{x['brand']} {fmt(x['price'])}" for x in sorted([b for b in below if b['tier'] in ('Aspirational', 'Beatable')], key=lambda b: b['price'])[:4]) + ".")
    agg = [x for x in comps if isinstance(x.get("ppc_aggr"), (int, float))]
    if agg:
        a3 = sorted(agg, key=lambda x: -(x.get("ad_gap") or 0))[:3]
        ins.append("Search: we lose most shared keywords to " + ", ".join(f"{x['brand']} (we win {x.get('we_win')}, lose {x.get('we_lose')})" for x in sorted(agg, key=lambda x: -(x.get('we_lose') or 0))[:3])
                   + ". Biggest ad gaps (they advertise where we don't or harder): " + ", ".join(f"{x['brand']} {x.get('ppc_none') or 0:,} + {x.get('ppc_aggr') or 0:,} KWs" for x in a3) + ".")
        hi = [x for x in agg if (x.get("r_sbv") or 0) >= 0.5 or (x.get("r_sb") or 0) >= 0.5]
        if hi:
            ins.append("Brand ads: " + ", ".join(f"{x['brand']} (SB {x.get('r_sb') or 0:.0%}, SBV {x.get('r_sbv') or 0:.0%})" for x in hi[:5]) + " hold Sponsored Brands / video on most of their traffic - the plan has our SB, SBV and display live by Nov 1.")
    if lf:
        ins.append(f"Our BFCM 2025: {lf['lift']:.2f}x daily sales in BFCM week vs the 30 days before; TACoS {lf['tacos']:.1f}% vs {lf['pre_tacos']:.1f}% before; December {lf['dec']:.2f}x." if lf.get("dec") and lf.get("tacos") is not None and lf.get("pre_tacos") is not None else f"Our BFCM 2025: {lf['lift']:.2f}x.")
    cpd = [x["pd"] / x["pd_pre"] for x in comps if isinstance(x.get("pd"), (int, float)) and (x.get("pd_pre") or 0) >= 5]
    if cpd and (pt.get(best) or {}).get("pd26_pre_org", 0) and (pt.get(best) or {}).get("pd26_pre_org", 0) >= 5:
        ov = pt[best]["pd26_org"] / pt[best]["pd26_pre_org"]
        ins.append(f"Prime Day 2026: our organic visibility {ov:.2f}x vs rivals' median {statistics.median(cpd):.2f}x (n={len(cpd)}) - " + ("rivals gained more event visibility than we did." if statistics.median(cpd) > ov else "we held or out-gained rivals."))
    if mkt == "US" and comps:
        ins.append("Still needed for the lift forecast: competitors' BFCM 2025 deal type, depth and BSR change (yellow columns) - Keepa, AGENT_PROMPTS Prompt 1.")
    for line in ins or ["No competitor data for this product yet."]:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        c = ws.cell(row=r, column=1, value="•  " + line); c.font = F(size=9); c.alignment = WRAP
        ws.row_dimensions[r].height = 30 if len(line) > 180 else 18
        r += 1
    ws.freeze_panes = "B3"
    product_cells[(pid, mkt)] = {"tab": tname}

# ================================================================== Data sheet (one row per competitor, feeds the dashboard)
dsh = wb.create_sheet("Data")
DCOLS = ["match", "seq", "pid", "Product", "Marketplace", "Family", "Brand", "Tier", "Title", "Image URL", "Parent ASIN", "Child ASIN",
         "Variations", "Price", "List Price", "List % over", "Our price same size", "Gap vs ours", "BSR", "Est weekly units", "Rating", "Reviews",
         "ASINsight traffic", "Organic share", "We win", "We lose", "KWs they advertise we don't", "PD26 vis lift", "Tab", "BFCM25 discount", "BFCM25 BSR lift", "Size", "Colour"]
for j, h in enumerate(DCOLS, 1):
    c = dsh.cell(row=1, column=j, value=h); c.font = F(bold=True, color="FFFFFF"); c.fill = HDR
DR0 = 2
for i, x in enumerate(records):
    rr = DR0 + i
    tab, prow = x.get("_cell") or (None, None)
    ref = (lambda k: f"='{tab}'!{CLt[k]}{prow}") if tab else (lambda k: None)
    vals = [None, None, x["pid"], x["product"], x["mkt"], x["family"], x["brand"], x["tier"], x["title"], good_img(x["image"]), x["parent"], x["child"],
            x["var"], x["price"], x["lp"], None, x.get("our_same"), None, x["bsr"], x["wk"], x["rating"], x["reviews"],
            x["asi_tr"], x["org_pct"], x["we_win"], x["we_lose"], x["ppc_none"],
            (x["pd"] / x["pd_pre"]) if isinstance(x.get("pd"), (int, float)) and (x.get("pd_pre") or 0) >= 5 else None, tab,
            ref("bf_disc"), ref("bsr_lift"), x.get("size"), x.get("colour")]
    for j, v in enumerate(vals, 1):
        dsh.cell(row=rr, column=j, value=v).font = F(size=8)
    dsh[f"P{rr}"] = f'=IF(AND(ISNUMBER(O{rr}),ISNUMBER(N{rr}),N(N{rr})>0),O{rr}/N{rr}-1,"")'
    dsh[f"R{rr}"] = f'=IF(AND(ISNUMBER(N{rr}),ISNUMBER(Q{rr}),N(Q{rr})>0),N{rr}/Q{rr}-1,"")'
    # filter match against the Dashboard selectors (C4 product, C5 marketplace, C6 brand, C7 tier, C8 family)
    dsh[f"A{rr}"] = (f'=AND(OR(Dashboard!$C$4="All",Dashboard!$C$4=D{rr}),OR(Dashboard!$C$5="All",Dashboard!$C$5=E{rr}),'
                     f'OR(Dashboard!$C$6="All",Dashboard!$C$6=G{rr}),OR(Dashboard!$C$7="All",Dashboard!$C$7=H{rr}),OR(Dashboard!$C$8="All",Dashboard!$C$8=F{rr}))')
    dsh[f"B{rr}"] = f"=IF(A{rr},{('B' + str(rr - 1)) if rr > DR0 else '0'}+1,{('B' + str(rr - 1)) if rr > DR0 else '0'})"
DR1 = DR0 + len(records) - 1
dsh.freeze_panes = "C2"
dsh.sheet_properties.tabColor = "BFBFBF"

# lists for dropdowns
lst = wb.create_sheet("Lists")
lst.sheet_state = "hidden"
prods = ["All"] + list(dict.fromkeys(PINFO[p][2] for p, m, t in TABS))
brands = ["All"] + sorted({x["brand"] for x in records if x["brand"]}, key=str.lower)
for j, (name, vals) in enumerate((("Products", prods), ("Markets", ["All", "US", "CA"]), ("Brands", brands),
                                  ("Tiers", ["All", "Aspirational", "Beatable", "Poor", "Untiered"]), ("Families", ["All", "Bamboo", "Satin", "Silk", "Cooling", "Other"])), 1):
    for i, v in enumerate(vals, 1):
        lst.cell(row=i, column=j, value=v)
    wb.defined_names[name] = DefinedName(name, attr_text=f"Lists!${CL(j)}$1:${CL(j)}${len(vals)}")

# ================================================================== Dashboard
db = wb.create_sheet("Dashboard", 1)
db.sheet_view.showGridLines = False
db.sheet_view.zoomScale = 90
W = [2, 13, 18, 34, 10, 9, 9, 8, 9, 9, 8, 7, 8, 9, 8, 8, 9, 14]
for i, w in enumerate(W, 1):
    db.column_dimensions[CL(i)].width = w
db.merge_cells("B1:R1")
c = db["B1"]; c.value = "BFCM 2026 Competitor Dashboard"; c.font = F(size=18, bold=True, color="FFFFFF"); c.fill = HDR; c.alignment = Alignment(vertical="center", indent=1)
db.row_dimensions[1].height = 34
db.merge_cells("B2:R2")
db["B2"] = "Pick a product, marketplace, brand, tier or family in the yellow cells. The competitor list, images and numbers below update instantly. Images render in Excel 365 and Google Sheets."
db["B2"].font = F(italic=True, color=C_SUB)
for i, (lab, name) in enumerate((("Product", "Products"), ("Marketplace", "Markets"), ("Brand", "Brands"), ("Tier", "Tiers"), ("Family", "Families")), 4):
    a = db.cell(row=i, column=2, value=lab); a.font = F(bold=True, color=C_SUB)
    b = db.cell(row=i, column=3, value="DC B4" if lab == "Product" else ("US" if lab == "Marketplace" else "All"))
    b.fill = INPUT; b.font = F(bold=True, size=10, color=BLUE); b.border = BOX
    dv = DataValidation(type="list", formula1=f"={name}", allow_blank=False); db.add_data_validation(dv); dv.add(b.coordinate)
# our product panel (driven by the selected product)
db.merge_cells("E4:E8")
prod_rows = []
lst2 = wb["Lists"]
# product lookup table on Lists (cols G..P): short, tab, title, image, brand, parent, skus, price, lift, comps
lst2.cell(row=1, column=7, value="short")
pr = 2
for pid, mkt, tname in TABS:
    if mkt != "US":
        continue
    p, o = our_profile(pid, mkt)
    title, img, best, parent = our_title_and_image(pid, mkt)
    lf = lift_of(pid, mkt)
    e = econ(o.get("economics"))
    vals = [PINFO[pid][2], tname, title or f"{o.get('brand')} {o.get('name')}", good_img(img), p.get("brand") or o.get("brand"), parent,
            p.get("skuCount") or o.get("sku_count"), e["price"], lf["lift"] if lf else None, best]
    for j, v in enumerate(vals, 7):
        lst2.cell(row=pr, column=j, value=v)
    pr += 1
LP_RANGE = f"Lists!$G$2:$P${pr - 1}"
def plook(col):
    return f'IFERROR(INDEX({LP_RANGE},MATCH($C$4,Lists!$G$2:$G${pr - 1},0),{col}),"")'
if NO_IMAGE_FORMULA:
    db["E4"] = f'=IF($C$4="All","",{plook(4)})'
else:
    db["E4"] = f'=IF($C$4="All","",IFERROR(_xlfn.IMAGE({plook(4)}),"IMAGE MISSING"))'
db["E4"].alignment = CENTER; db["E4"].border = BOX
for i, (lab, col, nf) in enumerate((("Our product", 3, None), ("Brand", 5, None), ("Parent ASIN", 6, None), ("Variations (SKUs)", 7, "#,##0"),
                                    ("Blended price", 8, "$#,##0.00"), ("BFCM 2025 lift", 9, '0.00"x"')), 4):
    a = db.cell(row=i, column=6, value=lab); a.font = F(bold=True, color=C_SUB, size=8)
    db.merge_cells(start_row=i, start_column=7, end_row=i, end_column=11)
    b = db.cell(row=i, column=7, value=f'=IF($C$4="All","All products",{plook(col)})' if col == 3 else f'=IF($C$4="All","",{plook(col)})')
    b.font = F(bold=(col == 3), size=9); b.alignment = Alignment(wrap_text=True, vertical="center")
    if nf:
        b.number_format = nf
db.cell(row=9, column=6, value="Open the product tab:").font = F(bold=True, color=C_SUB, size=8)
db.merge_cells("G9:K9")
db["G9"] = f'=IF($C$4="All","",HYPERLINK("#\'"&{plook(2)}&"\'!A1",{plook(2)}))'
db["G9"].font = F(color="0563C1", underline="single")
for rr in range(4, 9):
    db.row_dimensions[rr].height = 22
db.row_dimensions[4].height = 30
# KPI tiles
rng = lambda col: f"Data!${col}${DR0}:${col}${DR1}"
tiles = [("Competitors shown", f"=COUNTIF({rng('A')},TRUE)", "#,##0"),
         ("Median price", f'=IFERROR(MEDIAN(IF(({rng("A")}=TRUE)*ISNUMBER({rng("N")}),{rng("N")})),"")', "$#,##0.00"),
         ("Priced below us", f'=COUNTIFS({rng("A")},TRUE,{rng("R")},"<0")', "#,##0"),
         ("List Price set", f'=COUNTIFS({rng("A")},TRUE,{rng("P")},">0")', "#,##0"),
         ("List Price ≤12% over", f'=COUNTIFS({rng("A")},TRUE,{rng("P")},">0",{rng("P")},"<=0.12")', "#,##0"),
         ("Est weekly units (sum)", f'=SUMIFS({rng("T")},{rng("A")},TRUE)', "#,##0"),
         ("Keepa BFCM rows filled", f'=COUNTIFS({rng("A")},TRUE,{rng("AD")},">=0")', "#,##0"),
         ("Avg BFCM 2025 discount", f'=IFERROR(AVERAGEIFS({rng("AD")},{rng("A")},TRUE),"")', "0.0%")]
for i, (lab, fx, nf) in enumerate(tiles):
    col = 12 + (i % 4) * 2 - 1 + 1
    row = 4 + (i // 4) * 3
    cA, cB = CL(col), CL(col + 1)
    db.merge_cells(f"{cA}{row}:{cB}{row}"); db.merge_cells(f"{cA}{row + 1}:{cB}{row + 2}")
    a = db[f"{cA}{row}"]; a.value = lab.upper(); a.font = F(size=7, bold=True, color=C_SUB); a.fill = FILL["tile"]; a.alignment = CENTER
    b = db[f"{cA}{row + 1}"]; b.font = F(size=15, bold=True, color=C_INK); b.fill = FILL["tile"]; b.alignment = CENTER; b.number_format = nf
    if "MEDIAN(IF(" in fx:
        from openpyxl.worksheet.formula import ArrayFormula
        b.value = ArrayFormula(f"{cA}{row + 1}", fx)
    else:
        b.value = fx
# competitor gallery
GR = 12
db.merge_cells(f"B{GR - 1}:R{GR - 1}")
db[f"B{GR - 1}"] = "COMPETITORS (first 80 matches, in tier then weekly-units order)"
db[f"B{GR - 1}"].font = F(size=11, bold=True, color=C_NAVY); db[f"B{GR - 1}"].fill = SEC
GH = [("#", 1, None), ("Image", 10, None), ("Brand · Tier", 7, None), ("Title", 9, None), ("Our product", 4, None), ("Mkt", 5, None), ("Price", 14, "$#,##0.00"),
      ("List Price", 15, "$#,##0.00"), ("List % over", 16, "0%"), ("vs our price", 18, "+0%;-0%;0%"), ("BSR", 19, "#,##0"), ("Wk units", 20, "#,##0"),
      ("Rating", 21, "0.0"), ("Reviews", 22, "#,##0"), ("Variations", 13, "#,##0"), ("We win / lose", 25, None), ("ASIN", 12, None)]
for j, (h, src, nf) in enumerate(GH, 2):
    c = db.cell(row=GR, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CENTER; c.border = BOX
for k in range(1, 81):
    rr = GR + k
    db.row_dimensions[rr].height = IMG_ROW_H
    m = f"MATCH({k},Data!$B${DR0}:$B${DR1},0)"
    def gv(col):
        x_ = f"INDEX(Data!${CL(col)}${DR0}:${CL(col)}${DR1},{m})"
        return f'IFERROR(IF({x_}="","",{x_}),"")'
    for j, (h, src, nf) in enumerate(GH, 2):
        c = db.cell(row=rr, column=j); c.border = BOX; c.font = F(size=8); c.alignment = WRAP
        if h == "#":
            c.value = f'=IF({k}<=COUNTIF({rng("A")},TRUE),{k},"")'
        elif h == "Image":
            c.alignment = CENTER
            c.value = (f'=IF(B{rr}="","",{gv(10)})' if NO_IMAGE_FORMULA else f'=IF(B{rr}="","",IFERROR(_xlfn.IMAGE({gv(10)}),"IMAGE MISSING"))')
        elif h == "Brand · Tier":
            c.value = f'=IF(B{rr}="","",{gv(7)}&CHAR(10)&{gv(8)})'
            c.font = F(size=8, bold=True)
        elif h == "We win / lose":
            c.value = f'=IF(OR(B{rr}="",{gv(25)}=""),"",{gv(25)}&" / "&{gv(26)})'
        else:
            c.value = f'=IF(B{rr}="","",{gv(src)})'
        if nf:
            c.number_format = nf
db.column_dimensions["E"].width = 34
db.conditional_formatting.add(f"K{GR + 1}:K{GR + 80}", FormulaRule(formula=[f'AND(ISNUMBER(K{GR + 1}),K{GR + 1}<0)'], fill=FILL["flag"]))
db.conditional_formatting.add(f"J{GR + 1}:J{GR + 80}", FormulaRule(formula=[f'AND(ISNUMBER(J{GR + 1}),J{GR + 1}>0,J{GR + 1}<=0.12)'], fill=FILL["ok"]))
db.freeze_panes = f"A{GR + 1}"

# ================================================================== Product Index
pi = wb.create_sheet("Product Index", 2)
pi.sheet_view.showGridLines = False
PIH = [("Image", 11), ("Product tab", 18), ("Family", 8), ("Brand", 10), ("Title", 40), ("Mkt", 5), ("Parent ASIN", 11), ("Variations", 8), ("Sizes", 14),
       ("Colours", 8), ("Blended price", 9), ("Units 28d", 8), ("Competitors mapped", 9), ("BFCM 2025 lift", 8), ("BFCM 2025 TACoS", 8), ("BFCM role", 20)]
for j, (h, w) in enumerate(PIH, 1):
    c = pi.cell(row=1, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CENTER; c.border = BOX
    pi.column_dimensions[CL(j)].width = w
pi.row_dimensions[1].height = 30
rr = 2
for pid, mkt, tname in TABS:
    p, o = our_profile(pid, mkt)
    title, img, best, parent = our_title_and_image(pid, mkt)
    e = econ(o.get("economics"))
    lf = lift_of(pid, mkt)
    pi.row_dimensions[rr].height = IMG_ROW_H
    put_image(pi, f"A{rr}", img, "OURS - parent/best child", f"{p.get('brand') or o.get('brand')} {p.get('name') or o.get('name')}", mkt, p.get("brand") or o.get("brand"), best)
    vals = [None, tname, PINFO[pid][1], p.get("brand") or o.get("brand"), title, mkt, parent, p.get("skuCount") or o.get("sku_count"),
            ", ".join(p.get("sizes") or o.get("sizes") or []), len(p.get("colours") or []) or o.get("colour_count"), e["price"], e["units_28d"],
            len([x for x in records if x["pid"] == pid and x["mkt"] == mkt]), lf["lift"] if lf else None, (lf["tacos"] / 100) if lf and lf.get("tacos") is not None else None, PINFO[pid][3]]
    for j, v in enumerate(vals[1:], 2):
        c = pi.cell(row=rr, column=j, value=v); c.font = F(); c.border = BOX; c.alignment = WRAP
    pi.cell(row=rr, column=2).hyperlink = f"#'{tname}'!A1"; pi.cell(row=rr, column=2).font = F(color="0563C1", underline="single")
    pi.cell(row=rr, column=11).number_format = "$#,##0.00"; pi.cell(row=rr, column=14).number_format = '0.00"x"'; pi.cell(row=rr, column=15).number_format = "0.0%"
    rr += 1
pi.freeze_panes = "C2"

# ================================================================== README
lines = [
    ("BFCM 2026 Competitor Research", dict(bold=True, size=16)),
    ("Owner: Shayan Rana · Backup: Zarlish · v1 for Thu Oct 15, 2026 · Built from the Command Center (primary) and Data Dive on Oct 13, 2026", dict(italic=True)),
    ("", None),
    ("How to use it", dict(bold=True, size=11)),
    ("1. Dashboard - choose Product / Marketplace / Brand / Tier / Family in the yellow cells; the competitor gallery, images and tiles update. 'Open the product tab' jumps to the full analysis.", {}),
    ("2. Product Index - every one of our products with its image, variations and BFCM 2025 result; click a tab name to open it.", {}),
    (f"3. One tab per product and marketplace ({len(TABS)} tabs, named 'US ...' / 'CA ...'): 1 Our product · 2 Our variations (every SKU with image, size, colour, price, units) · 3 Our BFCM 2025 result · 4 Competitor landscape (image, title, ASINs, variations, price, List Price, STR band, same-size gap, BSR, units, reviews, search strategy, Prime Day visibility, BFCM 2025 columns) · 5 What it means for BFCM.", {}),
    ("4. Data Gaps lists what is still missing (with the agent prompt that fills it); Data feeds the dashboard. The Keepa request list, lift inputs and the Nov 20 - Dec 1 event-watch log stay in BFCM_2026_Competitor_Tracker_v1.xlsx.", {}),
    ("", None),
    ("Images", dict(bold=True, size=11)),
    ("Images are live IMAGE-function formulas pointing at the verified Amazon image URLs held by Data Dive (seller catalog for our variations, niche research for competitors) and the Command Center thumbnail. They render in Excel 365 (Windows / Mac / web) and Google Sheets; older Excel and LibreOffice show an error in those cells instead of the picture.", {}),
    ("A cell reading IMAGE MISSING means no verified image URL was available - it is never replaced by an unrelated picture. The list of missing images is on Data Gaps; image_request.csv lists every image URL for download.", {}),
    ("", None),
    ("Colour legend", dict(bold=True, size=11)),
    ("Green group = Command Center price/sales snapshot · Blue = Data Dive listing · Purple = Command Center search strategy (ASINsight) · Grey = formula · YELLOW / blue text = to fill (Keepa or page check).", {}),
    ("", None),
    ("Definitions", dict(bold=True, size=11)),
    ("BFCM 2025 = Nov 20 - Dec 1, 2025; pre-event = Oct 21 - Nov 19, 2025. Our total sales are derived as ad spend / TACoS. Prime Day 2026 = Jun 23-26 vs Jun 1-20.", {}),
    ("STR band: List Price <=12% over price is where Joseph's study found Amazon shows the strikethrough (if the item sold at it recently); >25% over is usually ignored.", {}),
    ("Search strategy (Command Center ASINsight): shared keywords, we win / lose, their keywords we miss, keywords they advertise and we don't, and their SP / SB / SB-video / Amazon's Choice reach. Exports can be up to 2 weeks apart; treat as direction, not exact share.", {}),
    ("Estimated weekly units (Command Center) and 30-day units (Data Dive) are estimates - use them to rank competitors, not as exact sales.", {}),
]
for i, (t, f) in enumerate(lines, 1):
    c = rd.cell(row=i, column=1, value=t)
    if f is not None:
        c.font = F(**f) if f else F(size=10)
    c.alignment = WRAP
rd.column_dimensions["A"].width = 165

# ================================================================== image request + gaps
seen = set()
with open(IMG_CSV, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["role", "our_product", "marketplace", "brand", "asin", "image_url", "save_as"])
    for role, prod, mk, br, asin, u in img_rows:
        if u in seen:
            continue
        seen.add(u)
        w.writerow([role, prod, mk, br, asin, u, f"{asin or 'x'}_{u.rsplit('/', 1)[-1]}"])
missing_comp = sorted({(x["product"], x["brand"], x["child"]) for x in records if not good_img(x["image"])})
gaps = wb.create_sheet("Data Gaps")
gaps.sheet_view.showGridLines = False
G = [("Gap", "Why it matters", "How to fill it (AGENT_PROMPTS.md)"),
     ("Competitors' BFCM 2025 deal type, dates, prices, discount, BSR change", "Core of the lift forecast and deal-depth benchmark", "Prompt 1 (Keepa history) + Prompt 4 (Keepa deals)"),
     ("Competitor variation detail: every child ASIN with colour, size, price and image", "Command Center and Data Dive hold one tracked child per competitor plus the variation count only", "Prompt 10 (Keepa variations)"),
     (f"Competitor images missing: {len(missing_comp)} competitor rows", "No verified image URL in Data Dive for these ASINs", "Prompt 10 returns images for every child; list below"),
     ("Whether the strikethrough shows today, and its label", "Command Center holds List Price, not whether Amazon shows it", "Prompt 5 (STR Panel / page check)"),
     ("Canada competitor set", "No Amazon.ca competitor snapshots in the Command Center", "Prompt 9"),
     ("Our BFCM 2025 deals and stock-outs", "To read our 2025 lift fairly", "Prompts 6 and 7"),
     ("Our 2026 deal plan per product", "Undercut flags and the forecast scenario", "Prompt 8"),
     ("Image files for the web dashboard", "The web dashboard cannot load images from Amazon; it needs the files", "Prompt 11 (download image_request.csv)")]
for i, row in enumerate(G, 1):
    for j, v in enumerate(row, 1):
        c = gaps.cell(row=i, column=j, value=v); c.font = F(bold=(i == 1), color=("FFFFFF" if i == 1 else "000000")); c.border = BOX; c.alignment = WRAP
        if i == 1:
            c.fill = HDR
rr = len(G) + 2
gaps.cell(row=rr, column=1, value="Competitor rows with no verified image").font = F(bold=True, size=10)
rr += 1
for prod, br, ch in missing_comp:
    gaps.cell(row=rr, column=1, value=prod).font = F(); gaps.cell(row=rr, column=2, value=br).font = F(); gaps.cell(row=rr, column=3, value=ch).font = F()
    rr += 1
for j, w_ in enumerate((40, 50, 50), 1):
    gaps.column_dimensions[CL(j)].width = w_

# order: README, Dashboard, Product Index, product tabs..., Data Gaps, Data
wb.move_sheet("Data Gaps", offset=-(len(wb.sheetnames) - 1 - wb.sheetnames.index("Data Gaps")) + 0)
wb.save(OUT)
print(json.dumps({"tabs": len(TABS), "competitor_rows": len(records), "image_cells": len(img_rows), "unique_images": len(seen),
                  "comp_missing_img": len(missing_comp), "strategy_products": len(strat), "sku_files": len(skus),
                  "catalog_us": len(catalog.get("US", {})), "catalog_ca": len(catalog.get("CA", {})), "dd_images": len(ddimg)}))
