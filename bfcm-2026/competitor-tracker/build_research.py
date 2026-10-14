"""BFCM 2026 Competitor Research workbook.

One tab per product and marketplace, a filterable Dashboard with live product images
(Excel 365 / Google Sheets IMAGE()), and shared tabs (our BFCM 2025, Keepa request,
data gaps, event watch).

Inputs (all under ./data): cc/, ours/, dd_out/asins.json, pt_summary.json,
strategy/{pid}.json, catalog/catalog_{com,ca}.json, catalog/dd_images.json, skus/{pid}_{mkt}.json
Usage: python3 build_research.py OUT.xlsx IMAGES_CSV
"""
import json, glob, os, re, sys, csv, statistics, collections, datetime as dt
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

# ------------------------------------------------------------------ accuracy: our live price and real parent
# Command Center SKU prices come from the fee feed (feeDate, mostly 2026-03-30) and are stale. Live price priority:
# 1. Amazon page check of our own ASINs (data/our_prices/*.csv, AGENT_PROMPTS Prompt 12)
# 2. Data Dive niche snapshot dated on/after FRESH_FROM
# Command Center price is shown alongside with its date, never as "now".
FRESH_FROM = "2026-10-01"
OUR_BRANDS = ("DECOLURE", "SLEEPHORIA", "SLEEP SANCTUARY")
our_now = {}   # (mkt, asin) -> price record
for _a, _v in dd.items():
    if (_v.get("brand") or "").strip().upper() in OUR_BRANDS and isinstance(_v.get("price"), (int, float)):
        _d = (_v.get("nicheDate") or "")[:10]
        if _d >= FRESH_FROM:
            our_now[("US", _a)] = {"price": _v["price"], "lp": None, "src": "Data Dive", "date": _d,
                                  "rating": _v.get("rating"), "reviews": _v.get("reviewCount")}
# Helium 10 Xray export of our own catalog (child level, US): price, review pool, BSR, est. sales, image
xray = {}        # asin -> row summary
for _f in sorted(glob.glob(f"{DATA}/xray/helium10_xray_*.csv")):
    _xd = re.search(r"(\d{4}-\d{2}-\d{2})", _f).group(1)
    for _r in csv.DictReader(open(_f, newline="", encoding="utf-8-sig")):
        _a = (_r.get("ASIN") or "").strip()
        if not _a or (_r.get("Brand") or "").strip().upper() not in OUR_BRANDS + ("COOLINENS",):
            continue
        def _n(z):
            try:
                return float(str(z).replace(",", ""))
            except (TypeError, ValueError):
                return None
        _pool = (_r.get("Display Order") or "").split(".")[0]
        xray[_a] = {"price": _n(_r.get("Price  $")), "rating": _n(_r.get("Ratings")), "reviews": _n(_r.get("Review Count")),
                    "bsr": _n(_r.get("BSR")), "units_mo": _n(_r.get("ASIN Sales")), "bought": _n(_r.get("Recent Purchases")),
                    "fees": _n(_r.get("Fees  $")), "image": _r.get("Image URL"), "pool": _pool, "created": _r.get("Creation Date"),
                    "title": _r.get("Product Details"), "date": _xd}
        if xray[_a]["price"] is not None:
            our_now[("US", _a)] = {"price": xray[_a]["price"], "lp": None, "src": "Helium 10 Xray", "date": _xd,
                                  "rating": xray[_a]["rating"], "reviews": xray[_a]["reviews"]}
for _f in sorted(glob.glob(f"{DATA}/our_prices/*.csv")):
    for _r in csv.DictReader(open(_f, newline="", encoding="utf-8-sig")):
        _m, _a = (_r.get("marketplace") or "").strip().upper(), (_r.get("asin") or "").strip()
        try:
            _p = float(_r["price"]) if _r.get("price") not in (None, "") else None
        except ValueError:
            _p = None
        if _a and _m in ("US", "CA") and _p is not None:
            num_ = lambda z: float(z) if z not in (None, "") else None
            our_now[(_m, _a)] = {"price": _p, "lp": num_(_r.get("strikethrough_price")), "src": "Amazon page", "date": _r.get("check_date"),
                                 "rating": num_(_r.get("rating")), "reviews": num_(_r.get("reviews")),
                                 "label": _r.get("strikethrough_label"), "deal": _r.get("deal_badge"), "coupon": _r.get("coupon")}

def now_txt(n):
    return f"{n['src']}, {n['date']}" if n else None

def amazon_parent(pid, mkt):
    """Real Amazon parent ASIN: the parent the Data Dive catalog shows for our SKU children (Command Center's
    'parent_asin' is one of our child ASINs, not the Amazon parent)."""
    cat = catalog.get(mkt, {}) or {}
    kids = [x.get("asin") for x in ((skus.get((pid, mkt)) or {}).get("skus") or []) if x.get("asin")]
    cnt = {}
    for a in kids:
        pa = (cat.get(a) or {}).get("parentAsin")
        if pa:
            cnt[pa] = cnt.get(pa, 0) + 1
    return max(cnt, key=cnt.get) if cnt else None

def our_headline_price(pid, mkt, best, cc_price):
    """Live price of the best-selling child when held; otherwise the Command Center blended price, labelled stale."""
    n = our_now.get((mkt, best))
    if n:
        return n["price"], now_txt(n)
    if cc_price is not None:
        return cc_price, "Command Center blended, Mar 2026 - STALE"
    return None, "No price"

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
    parent = amazon_parent(pid, mkt) or p.get("parentAsin") or o.get("parent_asin")
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

_var_cache = {}
def our_variations(pid, mkt):
    """SKU rows joined to catalog children (image, title)."""
    if (pid, mkt) in _var_cache:
        return _var_cache[(pid, mkt)]
    p, o = our_profile(pid, mkt)
    parent = amazon_parent(pid, mkt) or p.get("parentAsin") or o.get("parent_asin")
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
            "price": g(x, "price"), "price_date": g(x, "feeDate"), "contribution": g(x, "contribution", "contributionPerUnit", "contribution_per_unit"),
            "be_acos": g(x, "beAcos", "breakEvenAcos", "be_acos", "break_even_acos"), "units_28d": g(x, "units28d", "units_28d", "units"),
            "status": g(x, "status") or it.get("status"), "image": good_img(it.get("imageUrl")) or (good_img((xray.get(asin) or {}).get("image")) if mkt == "US" else None),
        })
        if asin:
            seen.add(asin)
    for a, it in cat.items():   # catalog children not in the SKU list
        if it.get("parentAsin") == parent and a not in seen and a != parent:
            rows.append({"sku": None, "asin": a, "title": it.get("title"), "size": parse_size(it.get("title")),
                         "colour": parse_colour(it.get("title")), "price": None, "price_date": None, "contribution": None, "be_acos": None,
                         "units_28d": None, "status": it.get("status"), "image": good_img(it.get("imageUrl"))})
    for r in rows:
        if isinstance(r["be_acos"], (int, float)) and abs(r["be_acos"]) > 1.5:
            r["be_acos"] = r["be_acos"] / 100
        n = our_now.get((mkt, r["asin"]))
        r["price_now"], r["now_src"] = (n["price"], now_txt(n)) if n else (None, None)
        xr = xray.get(r["asin"]) if mkt == "US" else None
        r.update({"x_rating": xr["rating"] if xr else None, "x_reviews": xr["reviews"] if xr else None, "x_bsr": xr["bsr"] if xr else None,
                  "x_units": xr["units_mo"] if xr else None, "x_pool": xr["pool"] if xr else None})
        if not r.get("title") and xr:
            r["title"] = xr["title"]
    # review pool: the family most of this product's variations share; others are separate listings
    pools = {}
    for r in rows:
        if r.get("x_pool"):
            pools[r["x_pool"]] = pools.get(r["x_pool"], 0) + (r.get("units_28d") or 0) + 1
    main_pool = max(pools, key=pools.get) if pools else None
    for r in rows:
        r["split"] = bool(main_pool and r.get("x_pool") and r["x_pool"] != main_pool)
    rows.sort(key=lambda r: (-(r["units_28d"] or 0), r["size"] or "", r["colour"] or ""))
    _var_cache[(pid, mkt)] = rows
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
_sp_child = f"{DATA}/stock/our_stock_bfcm2025_by_child_asin.csv"
_sp = f"{DATA}/stock/our_stock_bfcm2025.csv"
if os.path.exists(_sp_child):
    # revision 2: one row per child ASIN per day; Y only when every linked SKU was observed at zero
    _flags = {}
    for row in csv.DictReader(open(_sp_child, encoding="utf-8-sig")):
        if not ("2025-11-20" <= row["date"] <= "2025-12-01") or row["out_of_stock"] not in ("Y", "N"):
            continue
        name = row["product_name"].split("|")[0].strip() if "|" in row["product_name"] else row["product_name"]
        pid_ = STOCK_ALIAS.get(name)
        if pid_ is not None:
            _flags[(pid_, row["marketplace"], row["child_asin"], row["date"])] = row["out_of_stock"] == "Y"
    _agg = {k: (0 if v else 1) for k, v in _flags.items()}
elif os.path.exists(_sp):
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
if "_agg" in globals():
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

DEAL_NAMES = {"Decolure Bamboo Sheets 4 Piece": 59, "Decolure Bamboo Sheets 6 Piece": 30, "Decolure Satin Sheets 4 Piece": 37,
              "Decolure Satin Sheets 6 Piece": 31, "Decolure Satin Fitted Sheet": 38, "Sleephoria Satin Sheets 4 Piece": 39,
              "Sleephoria Bamboo Sheets 6 Piece": 32, "Decolure Cooling Sheets 4 Piece": 48, "Sleephoria Cooling Sheets 4 Piece": 45,
              "Sleephoria Cooling Comforter": 42, "Decolure Silk Pillowcase": 55, "Decolure Waterproof Chair Cover": 33}
deals25 = {}      # (pid, mkt) -> list of campaigns
deals_cov = {}    # (pid, mkt) -> coverage note
_dp = f"{DATA}/deals/our_deals_bfcm2025_v2.csv"   # v2 = v1 + Keepa-observed price (agent checkpoint); falls back to v1
if not os.path.exists(_dp):
    _dp = f"{DATA}/deals/our_deals_bfcm2025.csv"
if os.path.exists(_dp):
    _camp = {}
    for row in csv.DictReader(open(_dp, encoding="utf-8-sig")):
        pid_ = DEAL_NAMES.get(row["product_name"])
        if pid_ is None:
            continue
        m_ = re.search(r"source_id=([0-9a-f]+)", row["notes"] or "")
        k = (pid_, row["marketplace"], m_.group(1) if m_ else row["deal_start"])
        c_ = _camp.setdefault(k, {"type": row["deal_type"], "status": row["status"], "start": row["deal_start"][:10], "end": row["deal_end"][:10], "kids": set(), "units": 0, "kobs": []})
        c_["kids"].add(row["child_asin"])
        if row.get("observed_deal_price_keepa"):
            try:
                c_["kobs"].append((float(row["observed_deal_price_keepa"]), row["child_asin"]))
            except ValueError:
                pass
        try:
            c_["units"] += int(float(row["units_sold"] or 0))
        except ValueError:
            pass
    for (pid_, mk_, _), c_ in _camp.items():
        deals25.setdefault((pid_, mk_), []).append(c_)
    for v_ in deals25.values():
        v_.sort(key=lambda c: c["start"])
    for row in csv.DictReader(open(f"{DATA}/deals/our_deals_bfcm2025_coverage.csv", encoding="utf-8-sig")):
        deals_cov[(int(row["product_id"]), row["marketplace"])] = row["coverage"]
ped_obs = {}   # (pid, mkt) -> Keepa price observations (not native campaigns)
_po = f"{DATA}/deals/sleephoria_keepa_observations.csv"
if os.path.exists(_po):
    for row in csv.DictReader(open(_po, encoding="utf-8-sig")):
        pid_ = DEAL_NAMES.get(row["product_name"])
        if pid_ is not None:
            ped_obs.setdefault((pid_, row["marketplace"]), []).append(row)

# ------------------------------------------------------------------ Keepa BFCM 2025 history (agent pull, US)
# Windows: pre-event = Nov 1-19, 2025 (the pull starts Nov 1); BFCM week = Nov 20 - Dec 1, 2025.
# Daily rows are Keepa's end-of-day (23:59 UTC) state, not intraday minima.
# BFCM low = lowest of Buy Box, Lightning Deal and Prime Exclusive price (coupon reported separately, not netted).
KP_PRE, KP_BF = ("2025-11-01", "2025-11-19"), ("2025-11-20", "2025-12-01")
keepa25 = {}   # asin -> summary
def _f(z):
    try:
        v = float(z)
        return v if v > 0 else None
    except (TypeError, ValueError):
        return None
_kh = f"{DATA}/keepa/keepa_history_p1.csv"
if os.path.exists(_kh):
    _kd = {}
    for row in csv.DictReader(open(_kh, encoding="utf-8-sig")):
        _kd.setdefault(row["asin"], []).append(row)
    _kcov = {r["asin"]: r for r in csv.DictReader(open(f"{DATA}/keepa/keepa_history_p1_coverage.csv", encoding="utf-8-sig"))} \
        if os.path.exists(f"{DATA}/keepa/keepa_history_p1_coverage.csv") else {}
    for a, rs in _kd.items():
        rs.sort(key=lambda r: r["date"])
        pre = [r for r in rs if KP_PRE[0] <= r["date"] <= KP_PRE[1]]
        bf = [r for r in rs if KP_BF[0] <= r["date"] <= KP_BF[1]]
        bb_pre = [_f(r["buy_box_price"]) for r in pre if _f(r["buy_box_price"])]
        bb_bf = [_f(r["buy_box_price"]) for r in bf if _f(r["buy_box_price"])]
        eff_bf = [min(x for x in (_f(r["buy_box_price"]), _f(r["lightning_deal_price"]), _f(r["prime_exclusive_price"])) if x)
                  for r in bf if any(_f(r[k]) for k in ("buy_box_price", "lightning_deal_price", "prime_exclusive_price"))]
        eff_pre = [min(x for x in (_f(r["buy_box_price"]), _f(r["lightning_deal_price"]), _f(r["prime_exclusive_price"])) if x)
                   for r in pre if any(_f(r[k]) for k in ("buy_box_price", "lightning_deal_price", "prime_exclusive_price"))]
        rk_pre = [_f(r["sales_rank"]) for r in pre if _f(r["sales_rank"])]
        rk_bf = [_f(r["sales_rank"]) for r in bf if _f(r["sales_rank"])]
        def span(key, rows_=rs):
            ds = [r["date"] for r in rows_ if (_f(r[key]) if key != "coupon" else r[key])]
            return (ds[0][5:] + " to " + ds[-1][5:], len(ds)) if ds else (None, 0)
        ld, ld_n = span("lightning_deal_price"); pe, pe_n = span("prime_exclusive_price"); cp, cp_n = span("coupon")
        ld_bf, pe_bf, cp_bf = span("lightning_deal_price", bf)[1], span("prime_exclusive_price", bf)[1], span("coupon", bf)[1]
        pre_med = statistics.median(bb_pre) if bb_pre else None          # Buy Box only (used for the "raised" check)
        pre_eff = statistics.median(eff_pre) if eff_pre else None        # what a Prime shopper paid before the event
        low = min(eff_bf) if eff_bf else None
        cov = _kcov.get(a, {})
        notes = []
        if ld_bf:
            typ, dates = "Lightning Deal", ld
        elif pe_bf:
            typ, dates = "Prime Exclusive Discount", pe
        elif cp_bf:
            typ, dates = "Coupon only", cp
        elif pre_eff and low is not None and low <= pre_eff * 0.95:
            ds = [r["date"][5:] for r in bf if _f(r["buy_box_price"]) and _f(r["buy_box_price"]) <= pre_eff * 0.95]
            typ, dates = "Price cut only", (ds[0] + " to " + ds[-1]) if ds else None
        elif bb_bf:
            typ, dates = "None", None
        elif (cov.get("tracking_since") or "9999") > "2025-12-01":
            typ, dates = "Not live in 2025", None
        else:
            typ, dates = None, None
            notes.append("No Buy Box history in Keepa for BFCM 2025")
        if typ != "Not live in 2025":
            if pe_n and typ != "Prime Exclusive Discount":
                notes.append(f"Prime Exclusive {pe}")
            if ld_n and typ != "Lightning Deal":
                notes.append(f"Lightning Deal {ld}")
            if cp_n and typ != "Coupon only":
                cps = sorted({r["coupon"] for r in rs if r["coupon"]})
                notes.append(f"Coupon {', '.join(cps)} ({cp})")
            elif typ == "Coupon only":
                notes.append("Coupon " + ", ".join(sorted({r["coupon"] for r in bf if r["coupon"]})))
            if pe and pe_n and pe.split(" to ")[0] < KP_BF[0][5:]:
                notes.append("Prime Exclusive already running before BFCM week")
            if pre_med and bb_bf and statistics.median(bb_bf) >= pre_med * 1.05:
                notes.append(f"Buy Box RAISED in BFCM week (median ${statistics.median(bb_bf):,.2f} vs ${pre_med:,.2f} before)")
            lps = sorted({_f(r["list_price"]) for r in bf if _f(r["list_price"])})
            if lps:
                notes.append("List Price " + "/".join(f"${x:,.2f}" for x in lps))
        oos_bf = [r["out_of_stock"] for r in bf if r["out_of_stock"] in ("Y", "N")]
        keepa25[a] = {
            "bf_type": typ, "bf_dates": dates, "bf_pre": pre_eff, "bf_low": low,
            "bsr_pre": round(statistics.median(rk_pre)) if rk_pre else None, "bsr_bf": round(statistics.median(rk_bf)) if rk_bf else None,
            "bf_oos": ("Y" if "Y" in oos_bf else ("N" if len(oos_bf) == len(bf) and oos_bf else None)),
            "notes": "; ".join(notes) or None, "kp_days": len(bb_bf), "raised": any("RAISED" in n for n in notes),
        }

str_now = {}
for _f in sorted(glob.glob(f"{DATA}/str/str_check_*.csv")):
    for row in csv.DictReader(open(_f, encoding="utf-8-sig")):
        str_now[row["asin"]] = row

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
            sc = str_now.get(ch) or {}
            if sc:
                num = lambda z: float(z) if z not in (None, "") else None
                rec.update({"str_show": sc.get("strikethrough_shown") or "unknown", "str_label": sc.get("strikethrough_label") or None,
                            "str_price": num(sc.get("strikethrough_price")), "page_price": num(sc.get("price")),
                            "deal_now": ", ".join(z for z in [sc.get("deal_badge") if sc.get("deal_badge") not in ("", "none") else None,
                                                               ("coupon " + sc["coupon"]) if sc.get("coupon") else None] if z) or ("none" if sc.get("strikethrough_shown") else None),
                            "stock_now": sc.get("in_stock") or None, "str_checked": f"{sc.get('check_date')} {sc.get('check_time_et')}"})
            kp_ = keepa25.get(ch)
            if kp_:
                rec.update({k: kp_[k] for k in ("bf_type", "bf_dates", "bf_pre", "bf_low", "bsr_pre", "bsr_bf", "bf_oos", "notes")})
                rec["bf_disc_v"] = (1 - kp_["bf_low"] / kp_["bf_pre"]) if kp_["bf_pre"] and kp_["bf_low"] else None
                rec["bsr_lift_v"] = (kp_["bsr_pre"] / kp_["bsr_bf"]) if kp_["bsr_pre"] and kp_["bsr_bf"] else None
                rec["raised"] = kp_["raised"]
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
# live same-size price: median of our children of that size with a live (page / Data Dive) price
our_live_size = {}
for (pid, mkt) in cc:
    for v in our_variations(pid, mkt):
        sz = {"Cal King": "California King"}.get(v.get("size"), v.get("size"))
        if sz and v.get("price_now") is not None:
            our_live_size.setdefault((pid, mkt), {}).setdefault(sz, []).append((v["price_now"], v["now_src"]))
def _live(pid, mkt, sz):
    xs = (our_live_size.get((pid, mkt)) or {}).get(sz)
    if not xs:
        return None, None
    return statistics.median(x[0] for x in xs), f"{xs[0][1]}; {len(xs)} child{'ren' if len(xs) > 1 else ''}"
for r in records:
    bys = our_size_price.get((r["pid"], "US"), {})
    want = r["size"] if r["size"] else "Queen"
    lead = f"Same size ({want})" if r["size"] else "Size not stated - vs our Queen"
    lp_, src_ = _live(r["pid"], "US", want)
    if lp_ is not None:
        r["our_same"], r["basis"], r["our_live"] = lp_, f"{lead}. Ours live: {src_}", True
    elif bys.get(want) is not None:
        r["our_same"], r["basis"], r["our_live"] = bys[want], f"{lead}. Ours: Command Center fee feed, Mar 2026 - STALE", False
    elif our_blend.get((r["pid"], "US")) is not None:
        r["our_same"], r["basis"], r["our_live"] = our_blend[(r["pid"], "US")], "vs our blended price (Command Center, Mar 2026 - STALE)", False
    else:
        r["our_same"], r["basis"], r["our_live"] = None, "No price for us", False

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
    ("seen", "Snapshot date", 8, "cc", "Date the Command Center last captured this competitor's price, BSR and reviews. Orange = older than 7 days before the build.", "yyyy-mm-dd"),
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
    ("str_show", "STR showing now? (Y/N)", 7, "str", "From the Amazon page check (str_check_<date>.csv). Blank = not checked yet (P2 rows).", None),
    ("str_label", "STR label", 8, "str", None, None),
    ("str_price", "Strikethrough price ($)", 8, "str", None, "$#,##0.00"),
    ("page_price", "Page price at check ($)", 8, "str", None, "$#,##0.00"),
    ("deal_now", "Deal / coupon now", 10, "str", None, None),
    ("stock_now", "Orderable now (Y/N)", 6, "str", None, None),
    ("str_checked", "Checked (ET)", 10, "str", None, None),
    ("bf_type", "BFCM 2025 deal type", 10, "kp", None, None),
    ("bf_dates", "BFCM 2025 deal dates", 10, "kp", None, None),
    ("bf_pre", "Pre-event price ($)", 8, "kp", "Keepa: median daily lowest price (Buy Box, Lightning Deal or Prime Exclusive), Nov 1-19, 2025, end-of-day state - same basis as the BFCM low.", "$#,##0.00"),
    ("bf_low", "BFCM 2025 low ($)", 8, "kp", "Keepa: lowest of Buy Box, Lightning Deal and Prime Exclusive price, Nov 20 - Dec 1, 2025. Coupons not netted (see Notes).", "$#,##0.00"),
    ("bf_disc", "BFCM 2025 discount", 7, "calc", None, "0.0%"),
    ("bsr_pre", "BSR pre-event", 8, "kp", "Keepa: median daily sales rank, Nov 1-19, 2025.", "#,##0"),
    ("bsr_bf", "BSR BFCM wk", 8, "kp", "Keepa: median daily sales rank, Nov 20 - Dec 1, 2025. BSR lift = pre / BFCM (above 1 = sold faster).", "#,##0"),
    ("bsr_lift", "BSR lift (x)", 6, "calc", None, '0.0"x"'),
    ("bf_oos", "OOS in BFCM? (Y/N)", 6, "kp", None, None),
    ("notes", "Notes", 22, "kp", None, None),
]
CK = {c[0]: i + 1 for i, c in enumerate(COMP_COLS)}
CLt = {k: CL(v) for k, v in CK.items()}
NC = len(COMP_COLS)
GROUP_NAMES = {"id": "COMPETITOR", "cc": "PRICE & SALES - Command Center snapshot (date per row)", "dd": "LISTING - Data Dive", "calc": "",
               "st": "SEARCH STRATEGY - Command Center ASINsight", "str": "STR NOW - Amazon page check (Oct 13); blank = not checked", "kp": "BFCM 2025 - Keepa (P1 filled; yellow = not pulled yet)"}

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
    bn = our_now.get((mkt, best))
    vlist = our_variations(pid, mkt)
    nlive = sum(1 for v in vlist if v.get("price_now") is not None)
    cc_dates = sorted({str(v["price_date"])[:10] for v in vlist if v.get("price_date")})
    cc_asof = (cc_dates[-1] if cc_dates else "date unknown")
    facts = [
        ("Title", title or "Title not in catalog pull - see Data Gaps"), ("Brand", brand), ("Marketplace", "Amazon.com (US)" if mkt == "US" else "Amazon.ca (CA)"),
        ("Parent ASIN (Amazon)", parent or "Not in catalog pull"), ("Best-selling child ASIN", best), ("Stage", p.get("stage") or o.get("stage")),
        ("Total variations (SKUs)", p.get("skuCount") or o.get("sku_count")),
        ("Sizes", ", ".join(p.get("sizes") or o.get("sizes") or []) or None),
        ("Colours", ", ".join(p.get("colours") or []) or (f"{o.get('colour_count')} colours" if o.get("colour_count") else None)),
        ("Price now, best child", (f"${bn['price']:,.2f} ({now_txt(bn)})" if bn else "Not checked yet - AGENT_PROMPTS Prompt 12")),
        ("Rating / reviews now", (f"{bn['rating']} / {bn['reviews']:,.0f} ({now_txt(bn)})" if bn and bn.get("rating") is not None and bn.get("reviews") is not None else "Not checked yet")),
        ("Live prices held", f"{nlive} of {len(vlist)} variations"),
        ("Blended price (Command Center)", (fmt(e["price"]) + f" - fee feed as of {cc_asof}, STALE") if e["price"] is not None else None),
        ("Contribution / unit", fmt(e["contribution"])), ("Break-even ACoS", fmt(e["be_acos"], "%")),
        ("Units last 28 days", fmt(e["units_28d"], "n")),
        ("Command Center product ASIN", (p.get("parentAsin") or o.get("parent_asin") or "") + " (one of our child ASINs, not the Amazon parent)"),
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
          ("price_now", "Price now ($)", 8), ("now_src", "Price now: source, date", 10),
          ("price", "Command Center price ($)", 8), ("price_date", "CC price date (stale)", 9),
          ("contribution", "Contribution ($)", 8), ("be_acos", "Break-even ACoS", 7), ("units_28d", "Units 28d", 7), ("status", "Status", 8),
          ("hero", "Our hero ASIN? (share of our visibility)", 10),
          ("x_rating", "Rating (H10, review family)", 7), ("x_reviews", "Reviews (H10, review family)", 8), ("x_bsr", "BSR (H10)", 8),
          ("x_units", "Est units / month (H10)", 8), ("split_txt", "Own review family?", 12)]
    VF = {"price_now": "$#,##0.00", "price": "$#,##0.00", "contribution": "$#,##0.00", "be_acos": "0%", "units_28d": "#,##0",
          "x_rating": "0.0", "x_reviews": "#,##0", "x_bsr": "#,##0", "x_units": "#,##0"}
    header_row(ws, r, [(a, b, c) for a, b, c in VC], height=34)
    r += 1
    ourhero = {a: sh for a, sh in ((strat.get(pid) or {}).get("our_hero_asins") or []) if isinstance(sh, (int, float))} if mkt == "US" else {}
    if not vars_:
        ws.cell(row=r, column=1, value="No variation rows yet - our per-SKU pull or catalog is missing for this product (see Data Gaps).").font = F(italic=True, color="C00000")
        r += 1
    for v in vars_:
        ws.row_dimensions[r].height = IMG_ROW_H
        put_image(ws, f"A{r}", v["image"], "OURS - variation", pname, mkt, brand, v["asin"])
        vv = dict(v, hero=(f"Yes ({ourhero[v['asin']]:.0%})" if v["asin"] in ourhero else None),
                  split_txt=("SEPARATE listing - not in the main review family" if v.get("split") else None),
                  price_date=(str(v["price_date"])[:10] if v.get("price_date") else None))
        for j, (key, _h, _w) in enumerate(VC[1:], 2):
            c = ws.cell(row=r, column=j, value=vv.get(key)); c.font = F(); c.border = BOX; c.alignment = WRAP
            if key in VF:
                c.number_format = VF[key]
            if key in ("price", "price_date") and vv.get(key) is not None:
                c.font = F(color="808080")
            if key == "price_now" and vv.get(key) is not None:
                c.font = F(bold=True)
            if key == "split_txt" and vv.get(key):
                c.fill = FILL["flag"]; c.font = F(bold=True)
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
    dl = deals25.get((pid, mkt))
    cov = deals_cov.get((pid, mkt))
    if dl or cov:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        if dl:
            cur = "C$" if mkt == "CA" else "$"
            def _kp(c):
                if c["status"] != "ran" or not c.get("kobs"):
                    return ""
                lo = min(c["kobs"])
                return f"; Keepa lowest Buy Box during it {cur}{lo[0]:,.2f} on {lo[1]}"
            parts = [f"{c['type']} {c['start'][5:]} to {c['end'][5:]} ({c['status']}, {len(c['kids'])} variations" + (f", {c['units']:,} units" if c['units'] else "") + _kp(c) + ")" for c in dl]
            txt = ("Deals we ran or scheduled, Nov 1 - Dec 5, 2025 (DataHub promotions; scheduled deal price not in the feed. Keepa price = lowest Buy Box seen during the deal, "
                   "an observation for the hero child only, not the scheduled deal price): " + "; ".join(parts) + ".")
        else:
            txt = "Deals Nov 1 - Dec 5, 2025: no record returned by the DataHub promotions feed. Unknown, not proof that no deal ran."
        c = ws.cell(row=r, column=1, value=txt); c.font = F(size=8.5, bold=True, color=C_INK); c.alignment = WRAP
        ws.row_dimensions[r].height = 30 if len(txt) > 180 else 18
        r += 1
    po = ped_obs.get((pid, mkt))
    if po:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        by = {}
        for o_ in po:
            by.setdefault((o_["child_asin"], o_["observed_price_values"]), []).append((o_["observed_start_utc"][:10], o_["observed_end_utc"][:10]))
        parts = [f"{a_} ${p_} {min(x[0] for x in iv)[5:]} to {max(x[1] for x in iv)[5:]}" + (f" ({len(iv)} separate spells)" if len(iv) > 1 else "") for (a_, p_), iv in sorted(by.items())]
        txt = ("Prime Exclusive Discount seen in Keepa, BFCM 2025 (not in the DataHub deal feed): " + "; ".join(parts)
               + ". Keepa observation only - campaign, scheduled dates and discount depth not confirmed.")
        c = ws.cell(row=r, column=1, value=txt); c.font = F(size=8.5, bold=True, color="7030A0"); c.alignment = WRAP
        ws.row_dimensions[r].height = 30
        r += 1
    so = stock_oos.get((pid, mkt))
    if so:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        txt = (f"Stock in BFCM week 2025 (FBA inventory snapshots, child-ASIN level, revision 2): {so['oos_asins']} of {so['asins']} variations hit zero FBA stock on at least one observed day"
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
        seen = x.get("seen")
        if isinstance(seen, str) and len(seen) >= 10:
            try:
                seen = dt.date.fromisoformat(seen[:10])
            except ValueError:
                pass
        vals = dict(x, listed=listed, seen=seen)
        for key, hdr, w, grp, com, nf in COMP_COLS[1:]:
            c = ws.cell(row=r, column=CK[key])
            c.border = BOX; c.font = F(); c.alignment = WRAP if key in ("title", "hero", "top_kw", "basis") else Alignment(vertical="top")
            if grp in ("kp", "str"):
                c.fill = INPUT; c.font = F(color=BLUE)
                if grp == "str" and vals.get(key) is not None:
                    c.value = vals[key]; c.fill = FILL["str"]; c.font = F()
                if grp == "kp" and vals.get(key) is not None:
                    c.value = vals[key]; c.fill = FILL["kp"]; c.font = F()
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
        ws.conditional_formatting.add(f"{CLt['seen']}{first}:{CLt['seen']}{last}", FormulaRule(formula=[f'AND(ISNUMBER({CLt["seen"]}{first}),{CLt["seen"]}{first}<DATE(2026,10,6))'], fill=PatternFill("solid", fgColor="F8CBAD")))
        ws.conditional_formatting.add(f"{CLt['basis']}{first}:{CLt['basis']}{last}", FormulaRule(formula=[f'ISNUMBER(SEARCH("STALE",{CLt["basis"]}{first}))'], fill=PatternFill("solid", fgColor="F8CBAD")))
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
    chk = [x for x in comps if x.get("str_show") in ("Y", "N")]
    if chk:
        sh = [x for x in chk if x["str_show"] == "Y"]
        ins.append(f"Strikethrough on the page today (Oct 13 check): {len(sh)} of {len(chk)} checked rivals show one"
                   + (": " + ", ".join(f"{x['brand']} {x.get('str_label')} {fmt(x.get('str_price'))} vs {fmt(x.get('page_price'))} (+{x['str_price']/x['page_price']-1:.0%})" + (" with deal" if x.get('deal_now') not in (None, 'none') and 'deal' in (x.get('deal_now') or '') else "") for x in sh[:6] if x.get('str_price') and x.get('page_price')) if sh else "")
                   + ".")
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
        kc = [x for x in comps if x.get("bf_type") not in (None, "Not live in 2025")]
        if kc:
            tc = collections.Counter(x["bf_type"] for x in kc)
            ds = [x["bf_disc_v"] for x in kc if isinstance(x.get("bf_disc_v"), (int, float))]
            ls = [x["bsr_lift_v"] for x in kc if isinstance(x.get("bsr_lift_v"), (int, float))]
            rz = sum(1 for x in kc if x.get("raised"))
            ins.append(f"BFCM 2025, {len(kc)} P1 rivals with Keepa history: " + ", ".join(f"{k} {v}" for k, v in tc.most_common())
                       + (f". Median depth vs their Nov 1-19 price {statistics.median(ds):.0%}" if ds else "")
                       + (f"; median BSR lift {statistics.median(ls):.2f}x" if ls else "")
                       + (f". {rz} raised their Buy Box in BFCM week, so their deal looked deeper than it was." if rz else "."))
        nk = sum(1 for x in comps if x.get("bf_type") is None)
        if nk:
            ins.append(f"{nk} rivals not in the Keepa P1 pull yet (yellow BFCM 2025 columns) - AGENT_PROMPTS Prompt 2.")
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
            p.get("skuCount") or o.get("sku_count"), our_headline_price(pid, mkt, best, e["price"])[0], lf["lift"] if lf else None, best]
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
                                    ("Our price (best child; see Data Check)", 8, "$#,##0.00"), ("BFCM 2025 lift", 9, '0.00"x"')), 4):
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
PIH = [("Image", 11), ("Product tab", 18), ("Family", 8), ("Brand", 10), ("Title", 40), ("Mkt", 5), ("Parent ASIN (Amazon)", 11), ("Variations", 8), ("Sizes", 14),
       ("Colours", 8), ("Our price ($)", 9), ("Our price: source, date", 14), ("Units 28d", 8), ("Competitors mapped", 9), ("BFCM 2025 lift", 8), ("BFCM 2025 TACoS", 8), ("BFCM role", 20)]
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
            ", ".join(p.get("sizes") or o.get("sizes") or []), len(p.get("colours") or []) or o.get("colour_count"), *our_headline_price(pid, mkt, best, e["price"]), e["units_28d"],
            len([x for x in records if x["pid"] == pid and x["mkt"] == mkt]), lf["lift"] if lf else None, (lf["tacos"] / 100) if lf and lf.get("tacos") is not None else None, PINFO[pid][3]]
    for j, v in enumerate(vals[1:], 2):
        c = pi.cell(row=rr, column=j, value=v); c.font = F(); c.border = BOX; c.alignment = WRAP
    pi.cell(row=rr, column=2).hyperlink = f"#'{tname}'!A1"; pi.cell(row=rr, column=2).font = F(color="0563C1", underline="single")
    pi.cell(row=rr, column=11).number_format = "$#,##0.00"; pi.cell(row=rr, column=15).number_format = '0.00"x"'; pi.cell(row=rr, column=16).number_format = "0.0%"
    if "STALE" in str(pi.cell(row=rr, column=12).value):
        pi.cell(row=rr, column=12).fill = PatternFill("solid", fgColor="F8CBAD")
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
    ("Data Check (4th tab) shows the as-of date and accuracy of every source, and a spot check of the tracker against the live Amazon search page. Our own prices: 'Price now' is live (Amazon page / Data Dive, dated); the Command Center price is its fee feed from Mar 2026 and is marked STALE wherever it is still used.", {}),
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

# our-price request list for AGENT_PROMPTS Prompt 12 (every child ASIN we sell, US and CA)
with open(os.path.join(HERE, "our_price_request.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["marketplace", "product_tab", "sku", "child_asin", "size", "colour", "units_28d", "command_center_price", "command_center_price_date", "live_price_held"])
    for pid, mkt, tname in TABS:
        for v in our_variations(pid, mkt):
            if v.get("asin") and v.get("sku"):
                w.writerow([mkt, tname, v["sku"], v["asin"], v["size"], v["colour"], v["units_28d"], v["price"],
                            str(v["price_date"])[:10] if v.get("price_date") else "", "Y" if v.get("price_now") is not None else "N"])

# ================================================================== Data Check (accuracy log)
chk = wb.create_sheet("Data Check")
chk.sheet_view.showGridLines = False
for j, w_ in enumerate((34, 16, 16, 16, 16, 12, 60), 1):
    chk.column_dimensions[CL(j)].width = w_
row = 1
chk.cell(row=row, column=1, value="Data Check - how current and how accurate every number is").font = F(bold=True, size=14)
row += 1
chk.cell(row=row, column=1, value="Read this before quoting a number. Orange cells in product tabs = stale value; 'STALE' in Comparison basis = our price there is the Command Center fee-feed price, not today's.").font = F(italic=True, size=9)
row += 2
US_recs = [x for x in records if x["mkt"] == "US"]
seen_cnt = {}
for x in US_recs:
    seen_cnt[x.get("seen") or "no snapshot"] = seen_cnt.get(x.get("seen") or "no snapshot", 0) + 1
latest_seen = max((k for k in seen_cnt if k != "no snapshot"), default=None)
old_seen = sum(v for k, v in seen_cnt.items() if k != "no snapshot" and k < "2026-10-06")
all_vars = [(pid, mkt, v) for pid, mkt, _t in TABS for v in our_variations(pid, mkt)]
live_vars = sum(1 for *_x, v in all_vars if v.get("price_now") is not None)
live_cmp = sum(1 for x in US_recs if x.get("our_live"))
str_rows = len({x["child"] for x in records if x.get("str_checked")})
S = [("Data", "Source", "As of", "Rows", "Status", "", "Notes"),
     ("Competitor price, List Price, BSR, rating, reviews", "Command Center", latest_seen, sum(v for k, v in seen_cnt.items() if k == latest_seen), "Current",
      "", f"{old_seen} US rows are older (Jul 20 - Sep 21, 2026) and are shaded orange in the 'Snapshot date' column. Price is for the one tracked child ASIN; Amazon search may show another size of the same listing."),
     ("Strikethrough now (shown / label / price)", "Amazon page check", "2026-10-13", str_rows, "Current", "", f"{str_rows} competitor ASINs checked (P1); the others are blank, not assumed."),
     ("Our price now", "Helium 10 Xray (Oct 13) / Data Dive (Oct 12-13) / Amazon page check", "2026-10-13", live_vars, "Partial", "",
      f"{live_vars} of {len(all_vars)} of our variations (US + CA) have a live price; US {sum(1 for _p, _m, v in all_vars if _m == 'US' and v.get('price_now') is not None)} of {sum(1 for _p, _m, v in all_vars if _m == 'US')}. The rest show only the Command Center fee-feed price (Mar 2026), which is out of date (B6 King White: $89.99 there vs $99.99 live). Xray matched every price already verified on the Amazon page. Prompt 12 (our_price_request.csv, rows with live_price_held = N) fills the rest; Canada has no live source yet."),
     ("Our listings outside the main review family", "Helium 10 Xray", "2026-10-13", sum(1 for *_x, v in all_vars if v.get("split")), "Check", "",
      "Variations that sit in their own review family (own rating and review count) instead of the product's main one, flagged in each tab's variation table. Several have weak ratings (e.g. Bamboo Full 3.9 / 61, Cooling Cal King 3.0 / 15, Satin 6pc King 4.0 / 28). Check the variation family in Seller Central."),
     ("Same-size price gap vs ours", "Calculated", "2026-10-13", live_cmp, "Partial", "",
      f"{live_cmp} of {len(US_recs)} US competitor rows compare against our live price; the rest are marked STALE in 'Comparison basis'."),
     ("Our contribution / break-even ACoS", "Command Center", "2026-03-30 prices", None, "Stale", "",
      "Calculated on the Mar 2026 fee-feed price. Where our live price is higher (e.g. B6 King +$10, B4 King +$15) contribution and break-even ACoS are understated."),
     ("Our parent ASIN", "Data Dive seller catalog", "2026-10-13", len(TABS), "Fixed", "",
      "Command Center's 'parent_asin' is one of our child ASINs. Tabs now show the Amazon parent from the catalog; the Command Center ASIN is listed separately."),
     ("Our BFCM 2025 ad spend, ad sales, ACoS, TACoS, orders", "Command Center", "2025-11-20 to 2025-12-01", None, "Exact", "", "Total sales = ad spend / TACoS (derived, not reported)."),
     ("Our BFCM 2025 deals", "DataHub promotions + Keepa (agent, v2 checkpoint)", "2026-10-13", None, "Partial", "",
      "Scheduled deal price, reference price and committed units are still blank. Keepa lowest Buy Box during each deal is filled for 24 of 3,080 rows (hero children; full pull ~3 days). Prime Exclusive Discounts on SL Bamboo 6pc and SL Cooling Comforter are Keepa observations only, not confirmed campaigns."),
     ("Our BFCM 2025 stock", "DataHub inventory, revision 2 (agent)", "2026-10-13", None, "Partial", "", "US Nov 26, 27, Dec 1 and CA Nov 24, 29, 30 have no snapshot."),
     ("Canada competitors", "None", None, 0, "Missing", "", "No Amazon.ca competitor snapshots in the Command Center."),
     ("Competitors' BFCM 2025 history (US)", "Keepa via agent (keepa_history_p1.csv)", "Nov 1 - Dec 5, 2025", len(keepa25), "Partial", "",
      f"All 70 P1 rivals pulled; {sum(1 for x in US_recs if x.get('bf_type') is None)} US rows (P2 rivals) still yellow. Pre-event = Nov 1-19 (pull starts Nov 1), BFCM = Nov 20 - Dec 1. Daily end-of-day state, so a deal of a few hours can be missed. Coupons are listed, not netted into the low price.")]
for i, r_ in enumerate(S):
    for j, v in enumerate(r_, 1):
        c = chk.cell(row=row, column=j, value=v); c.border = BOX; c.alignment = WRAP
        c.font = F(bold=(i == 0), color=("FFFFFF" if i == 0 else "000000"))
        if i == 0:
            c.fill = HDR
        elif j == 5:
            c.fill = PatternFill("solid", fgColor={"Current": "C6EFCE", "Exact": "C6EFCE", "Fixed": "C6EFCE", "Partial": "FFEB9C", "Check": "FFEB9C", "Stale": "F8CBAD", "Missing": "F8CBAD"}.get(v, "FFFFFF"))
    row += 1
row += 1
chk.cell(row=row, column=1, value="Spot check: Amazon search 'DECOLURE 100% Viscose from Bamboo Sheets King Size | 6 Pc Cooling Bed Set' (screenshot shared by Shayan, Oct 13, 2026)").font = F(bold=True, size=11)
row += 1
def _cmp(asin):
    for x in US_recs:
        if x["child"] == asin:
            return x
    return {}
def _var(asin):
    for pid, mkt, v in all_vars:
        if mkt == "US" and v["asin"] == asin:
            return v
    return {}
b6, b4, cl4 = _var("B0CQ2XQF9N"), _var("B08KQHRDDG"), _var("B0C9LS8Z18")
pb, bb1, bb2, bc = _cmp("B07DZTQ4JC"), _cmp("B07TBHLZJM"), _cmp("B08M9QK14J"), _cmp("B08L86VLZB")
SC = [("Listing on the search page", "Page price ($)", "Page rating / reviews", "Tracker price ($)", "Tracker rating / reviews", "Price match?", "Finding"),
      ("DECOLURE Bamboo 6 Pc, King (B0CQ2XQF9N)", 99.99, "4.4 / 3.1K", b6.get("price_now"), f"{(our_now.get(('US','B0CQ2XQF9N')) or {}).get('rating')} / {(our_now.get(('US','B0CQ2XQF9N')) or {}).get('reviews')}",
       None, f"Tracker now uses the live price ({b6.get('now_src')}). Command Center fee feed still says ${b6.get('price')} ({str(b6.get('price_date'))[:10]}) - stale, no longer used for comparisons."),
      ("DECOLURE Bamboo 4 Pc, King (B08KQHRDDG)", 94.99, "4.5 / 5.9K", b4.get("price_now"), f"{(our_now.get(('US','B08KQHRDDG')) or {}).get('rating')} / {(our_now.get(('US','B08KQHRDDG')) or {}).get('reviews')}",
       None, f"Live price from {b4.get('now_src')}. Command Center fee feed: ${b4.get('price')} ({str(b4.get('price_date'))[:10]}) - stale."),
      ("DECOLURE Cooling 4pcs, King Purple (B0C9LS8Z18)", 37.95, "4.2 / 1.2K", (cl4.get("price_now") or cl4.get("price")),
       f"{cl4.get('x_rating')} / {cl4.get('x_reviews'):,.0f}" if cl4.get("x_reviews") is not None else "not held",
       None, f"Live price from {cl4.get('now_src') or 'Command Center (Mar 2026)'}."),
      ("Pure Bamboo, King (B07DZTQ4JC)", 109.99, "4.5 / 21.9K", pb.get("price"), f"{pb.get('rating')} / {pb.get('reviews')}", None, f"Exact match (Command Center {pb.get('seen')})."),
      ("Bamboo Bay 6 Piece, King", 89.99, "4.5 / 2.6K", bb1.get("price"), f"{bb1.get('rating')} / {bb1.get('reviews')}", None,
       f"Same family (reviews match). Tracker prices tracked child {bb1.get('child')} ({bb1.get('size') or 'size not in title'}), not the King 6 Pc shown on the page."),
      ("Bamboo Bay 6 Piece, King ($27.99/count)", 111.94, "4.4 / 739", bb2.get("price"), f"{bb2.get('rating')} / {bb2.get('reviews')}", None,
       f"Same family (739 reviews). Tracked child {bb2.get('child')} is a 4 Piece Queen, so the price differs by design; compare on the same-size basis."),
      ("Bella Coterie 6 Piece, King", 194.99, "4.4 / 5.8K", bc.get("price"), f"{bc.get('rating')} / {bc.get('reviews')}", None,
       f"Same family. Tracked child {bc.get('child')} is another size/pack; it also moved from ${bc.get('price')} (Oct 12) to ${bc.get('page_price')} on the Oct 13 page check."),
      ("TWK Real 100% Viscose, King", 79.00, "5.0 / 76", None, "not in map", None,
       "Shows List $99.00, 'Limited time deal' and a 10% coupon. No TWK row in the map has 76 reviews - likely a TWK listing not yet mapped. Add it to the competitor map."),
      ("DECOLURE Bamboo 6 Pc, California King", 106.99, "3.5 / 16", None, "not matched", None,
       "Our own detail page with only 16 reviews - looks split from the main family (B6 now sits under parent B0H6335KNV). Check the variation family in Seller Central."),
      ("DECOLURE Bamboo 6 Pc, Full", 79.99, "4.2 / 27", None, "not matched", None, "Same as above: an own listing with 27 reviews, outside the main review pool.")]
first_sc = row
for i, r_ in enumerate(SC):
    for j, v in enumerate(r_, 1):
        c = chk.cell(row=row, column=j, value=v); c.border = BOX; c.alignment = WRAP
        c.font = F(bold=(i == 0), color=("FFFFFF" if i == 0 else "000000"))
        if i == 0:
            c.fill = HDR
        elif j in (2, 4):
            c.number_format = "$#,##0.00"
    if i:
        chk.cell(row=row, column=6, value=f'=IF(OR(B{row}="",D{row}=""),"n/a",IF(ABS(B{row}-D{row})<0.01,"Match","Differs"))').border = BOX
    row += 1
chk.conditional_formatting.add(f"F{first_sc + 1}:F{row - 1}", FormulaRule(formula=[f'F{first_sc + 1}="Match"'], fill=PatternFill("solid", fgColor="C6EFCE")))
chk.conditional_formatting.add(f"F{first_sc + 1}:F{row - 1}", FormulaRule(formula=[f'F{first_sc + 1}="Differs"'], fill=PatternFill("solid", fgColor="FFEB9C")))
row += 1
chk.cell(row=row, column=1, value="Page values typed from the screenshot (Source: Amazon.com search, Oct 13, 2026, shared by Shayan). 'Differs' on a competitor is expected when the tracked child is a different size; it is an error only for the same ASIN.").font = F(italic=True, size=8)

# order: README, Dashboard, Product Index, product tabs..., Data Gaps, Data
wb.move_sheet("Data Gaps", offset=-(len(wb.sheetnames) - 1 - wb.sheetnames.index("Data Gaps")) + 0)
wb.move_sheet("Data Check", offset=3 - wb.sheetnames.index("Data Check"))
wb.save(OUT)
print(json.dumps({"tabs": len(TABS), "competitor_rows": len(records), "image_cells": len(img_rows), "unique_images": len(seen),
                  "comp_missing_img": len(missing_comp), "strategy_products": len(strat), "sku_files": len(skus),
                  "catalog_us": len(catalog.get("US", {})), "catalog_ca": len(catalog.get("CA", {})), "dd_images": len(ddimg)}))
