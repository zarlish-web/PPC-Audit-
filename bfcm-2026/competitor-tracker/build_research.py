"""BFCM 2026 Competitor Research workbook.

One tab per product and marketplace, US and CA dashboards with live product images
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
from openpyxl.drawing.image import Image as XLImage
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
    (32, "Bamboo", "SL B6", "Core"), (36, "Bamboo", "SL B4", "Not launched yet"),
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
# Scope confirmed by Shayan, Oct 14, 2026: the core BFCM set, and products not launched yet (no live price expected)
CORE = {59, 30, 73, 37, 31, 38, 32, 39, 48, 45, 42, 43, 44}   # DC bamboo + satin, SS-B6, SS-S4, all cooling (DC + SL)
NOT_LAUNCHED = {36, 74, 76, 40}                               # SL B4, SL Satin 6pc, SL Cooling 6pc, SL Bamboo Pillowcase
LAUNCHING = set()                                             # CL Cooling Sheets launched Oct 15, 2026 (all 60 children live)
def scope_of(pid):
    return ("Core" if pid in CORE else "Not launched" if pid in NOT_LAUNCHED else "Launching (partly live)" if pid in LAUNCHING else "Other")

cc = {(int(d["product_id"]), d["marketplace"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/cc/*.json")) if d}
ours = {(int(d["product_id"]), d["marketplace"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/ours/*.json")) if d}
skus = {(int(d["product_id"]), d["marketplace"]): d for d in (jl(f) for f in glob.glob(f"{DATA}/skus/*.json")) if d and "product_id" in d}
# ---- SKU reassignment (Shayan, Oct 14, 2026): a Twin in the 6 Pc satin set is a 4-piece set, so the
# SATIN-4PC-TWIN-* SKUs are listed on Amazon under the Satin 6pc parent (B0HDTF4MN2) and share its reviews.
# The Command Center maps them to Satin 4pc (pid 37); the tracker counts them under Satin 6pc (pid 31).
# Ad spend/sales stay where the Command Center attributes them (product-level PPC cannot be split by SKU).
REASSIGN = {}   # (mkt, asin) -> (from_pid, to_pid)
for _x in ((skus.get((37, "US")) or {}).get("skus") or []):
    if str(_x.get("sku", "")).upper().startswith("SATIN-4PC-TWIN") and _x.get("asin"):
        REASSIGN[("US", _x["asin"])] = (37, 31)
def _apply_reassign():
    for (m_, a_), (f_, t_) in REASSIGN.items():
        src, dst = skus.get((f_, m_)), skus.get((t_, m_))
        if not (src and dst):
            continue
        mv = [x for x in src["skus"] if x.get("asin") == a_]
        src["skus"] = [x for x in src["skus"] if x.get("asin") != a_]
        dst["skus"].extend(mv)
        for d_, sign in ((src, -1), (dst, 1)):
            if isinstance(d_["profile"].get("skuCount"), int):
                d_["profile"]["skuCount"] += sign * len(mv)
        u = sum((x.get("units28d") or 0) for x in mv)
        for pid_, sign in ((f_, -1), (t_, 1)):
            e_ = ((cc.get((pid_, m_)) or {}).get("our") or {}).get("economics") or {}
            if isinstance(e_.get("units_28d"), (int, float)):
                e_["units_28d"] += sign * u
            for b_ in e_.get("by_size") or []:
                if b_.get("size") == "Twin" and isinstance(b_.get("units_28d"), (int, float)):
                    b_["units_28d"] += sign * u
_apply_reassign()

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
# SellerBoard product list (US listing price per SKU, live when pulled). Used only where no Amazon-page / Xray price
# exists. "Amazon.Found.*" SKUs carry stale prices and are skipped. SellerBoard's Amazon.ca rows repeat the US
# price, so it is never used for Canada.
for _f in sorted(glob.glob(f"{DATA}/sellerboard/US_prices_*.csv")):
    _sd = re.search(r"(\d{4}-\d{2}-\d{2})", _f)
    for _r in csv.DictReader(open(_f, newline="", encoding="utf-8-sig")):
        if str(_r.get("sku", "")).startswith("Amazon.Found") or str(_r.get("hide", "")).lower() == "true":
            continue
        try:
            _p = float(_r["price"])
        except (TypeError, ValueError, KeyError):
            continue
        if _p > 0 and _r.get("asin"):
            our_now[("US", _r["asin"])] = {"price": _p, "lp": None, "src": "SellerBoard listing price",
                                          "date": _sd.group(1) if _sd else "2026-10-14", "rating": None, "reviews": None}

# Helium 10 Xray exports of our own catalog (child level): price, review family, BSR, est. sales, image.
# US file prices in USD ("Price  $"); Amazon.ca file (URLs on amazon.ca) prices in CAD ("Price  CA$").
xray = {}        # (mkt, asin) -> row summary
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
        _m = "CA" if ("amazon.ca" in (_r.get("URL") or "") or "Price  CA$" in _r) else "US"
        _pk, _fk = ("Price  CA$", "Fees  CA$") if _m == "CA" else ("Price  $", "Fees  $")
        _pool = (_r.get("Display Order") or "").split(".")[0]
        xray[(_m, _a)] = {"price": _n(_r.get(_pk)), "rating": _n(_r.get("Ratings")), "reviews": _n(_r.get("Review Count")),
                          "bsr": _n(_r.get("BSR")), "units_mo": _n(_r.get("ASIN Sales")), "bought": _n(_r.get("Recent Purchases")),
                          "fees": _n(_r.get(_fk)), "image": _r.get("Image URL"), "pool": _pool, "created": _r.get("Creation Date"),
                          "title": _r.get("Product Details"), "date": _xd}
        if xray[(_m, _a)]["price"] is not None:
            our_now[(_m, _a)] = {"price": xray[(_m, _a)]["price"], "lp": None,
                                 "src": "Helium 10 Xray" + (" (Amazon.ca, CAD)" if _m == "CA" else ""), "date": _xd,
                                 "rating": xray[(_m, _a)]["rating"], "reviews": xray[(_m, _a)]["reviews"]}
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

# Our price = Helium 10 Xray only (US Oct 13, CA Oct 14): the latest full read of our catalog, agreed Oct 15 as the single
# price source. Other reads (Amazon page check, Data Dive, SellerBoard listing price) are kept in our_now_other for reference
# but are never shown as our price; a variation missing from Xray shows no price.
our_now_other = our_now
our_now = {k: {"price": x["price"], "lp": None, "src": "Helium 10 Xray" + (" (Amazon.ca, CAD)" if k[0] == "CA" else ""), "date": x["date"],
               "rating": x["rating"], "reviews": x["reviews"]} for k, x in xray.items() if x.get("price") is not None}

# Confirmed launch prices (launch thread, final confirmation Oct 15, 2026: live on all 60 children with the Buy Box)
launch_price = {}
for _f in sorted(glob.glob(f"{DATA}/ours/*_launch_price_*.csv")):
    for _r in csv.DictReader(open(_f, encoding="utf-8-sig")):
        launch_price[(_r["marketplace"], int(_r["pid"]), _r["size"])] = float(_r["price"])

# Amazon page status of our own variations (page-check notes): redirects / no Buy Box
our_page_flag = {}   # (mkt, asin) -> text
for _f in sorted(glob.glob(f"{DATA}/our_prices/*_notes.txt")):
    _m = "CA" if "_ca" in os.path.basename(_f) else "US"
    _d = re.search(r"(\d{4}-\d{2}-\d{2})", _f)
    for _ln in open(_f, encoding="utf-8"):
        _mm = re.match(r"(B0[0-9A-Z]{8}): REDIRECT: requested \S+; page selected (B0[0-9A-Z]{8}).*?Destination size=([^,]+), colour=([^,]+)", _ln)
        if _mm:
            our_page_flag[(_m, _mm.group(1))] = (f"Not buyable on Amazon {_d.group(1) if _d else ''}: page redirects to {_mm.group(2)} "
                                                 f"({_mm.group(3)} {_mm.group(4)})")
            continue
        _mm = re.match(r"(B0[0-9A-Z]{8}): Exact child Buy Box price not shown", _ln)
        if _mm:
            _pp = re.search(r"Purchase panel: ([^|]+)\|", _ln)
            our_page_flag[(_m, _mm.group(1))] = (f"No Buy Box on Amazon {_d.group(1) if _d else ''}"
                                                 + (f" (page says '{_pp.group(1).strip()}')" if _pp else ""))

# DataHub stock for those variations (agent): explains each flag. Blank numeric = confirmed zero when the
# row notes say "Confirmed source zero ... <field>".
for _f in sorted(glob.glob(f"{DATA}/our_prices/*_stock_*.csv")):
    _m = "CA" if "/ca_" in _f else "US"
    for _r in csv.DictReader(open(_f, newline="", encoding="utf-8-sig")):
        _k = (_m, _r["asin"])
        if _k not in our_page_flag:
            continue
        _notes = _r.get("notes") or ""
        _zero = re.search(r"Confirmed source zero[^:]*: ([^.]+)\.", _notes)
        _zf = {z.strip() for z in _zero.group(1).split(",")} if _zero else set()
        _av = _r.get("fba_available") or ("0" if "fba_available" in _zf else "")
        _inb = _r.get("inbound") or ("0" if "inbound" in _zf else "")
        if _av == "0":
            why = f"FBA stock 0 since {_r.get('last_date_with_available_gt_0') or '?'}" + (f", {_inb} inbound" if _inb not in ("", "0") else ", nothing inbound")
        elif _av:
            why = f"{_av} units in FBA stock, so not a stock-out: offer / listing issue"
        else:
            why = "stock unknown"
        our_page_flag[_k] += f" - {why} (DataHub {_r.get('snapshot_date')})"
def now_txt(n):
    return f"{n['src']}, {n['date']}" if n else None

# Launched since the catalog pull: the live launch title and stage (launch thread, Listing B, live Oct 15, 2026)
LAUNCH_OVERRIDE = {(69, "US"): {"title": "COOLINENS Cooling Sheets Queen Size | 4 Piece Set for Hot Sleepers", "stage": "Launched Oct 15, 2026"}}
def our_title_and_image(pid, mkt):
    title, img, best, parent = _our_title_and_image(pid, mkt)
    ov = LAUNCH_OVERRIDE.get((pid, mkt))
    return ((ov["title"] if ov else title), img, best, parent)
def our_stage(pid, mkt, p, o):
    ov = LAUNCH_OVERRIDE.get((pid, mkt))
    return ov["stage"] if ov else (p.get("stage") or o.get("stage"))

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
    for v_ in our_variations(pid, mkt):
        if v_["asin"] == best and v_.get("price_now") is not None:
            return v_["price_now"], v_["now_src"]
    lq = launch_price.get((mkt, pid, "Queen"))
    if lq is not None:
        return lq, "Queen launch price, live Oct 15, 2026"
    return None, "No current price for this child"

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
FONT = "Comfortaa"   # agreed Oct 15, 2026; renders in Google Sheets and wherever the font is installed (Excel substitutes otherwise)
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
COMING_SOON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "coming_soon_small.jpg")

img_rows = []   # (role, product, marketplace, brand, asin, url) for the image download request

def _ours_manifest():
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "product_images", "manifest_ours.csv")
    pv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "product_images", "provenance_ours.csv")
    if not os.path.exists(f):
        return {"ok": 0, "scope": 0, "US": 0, "CA": 0, "nok": 0, "err": "", "src": ""}
    rows = list(csv.DictReader(open(f, encoding="utf-8-sig")))
    kinds = {(r["marketplace"], r["asin"]): r["source_kind"] for r in csv.DictReader(open(pv, encoding="utf-8-sig"))} if os.path.exists(pv) else {}
    for f2, pv2 in ((f.replace(".csv", "_part2.csv"), pv.replace(".csv", "_part2.csv")),):
        if os.path.exists(f2):
            rows += list(csv.DictReader(open(f2, encoding="utf-8-sig")))
            kinds.update({(r["marketplace"], r["asin"]): r["source_kind"] for r in csv.DictReader(open(pv2, encoding="utf-8-sig"))})
    ok = [r for r in rows if r["ok"] == "Y"]
    ck = collections.Counter(kinds.get((r["marketplace"], r["asin"])) or "unknown" for r in ok)
    lab = {"fresh_amazon_page": "fresh Amazon page", "cached_Keepa_exact_domain_MAIN": "cached Keepa main image, exact ASIN and marketplace", "saved_amazon_page": "saved Amazon page"}
    ce = collections.Counter("HTTP 404 on the exact page" if "404" in r["error"] else "page showed another ASIN" if "identity" in r["error"] else "pending" for r in rows if r["ok"] != "Y")
    return {"ok": len(ok), "scope": len(rows), "US": sum(1 for r in ok if r["marketplace"] == "US"), "CA": sum(1 for r in ok if r["marketplace"] == "CA"),
            "nok": len(rows) - len(ok), "err": ", ".join(f"{v:,} {k}" for k, v in ce.most_common()), "src": ", ".join(f"{v:,} {lab.get(k, k)}" for k, v in ck.most_common())}
_om = _ours_manifest()

xmkt_img = []   # (mkt, asin): photo taken from the other marketplace's listing of the SAME ASIN

def other_mkt_img(mkt, asin):
    """Same ASIN, other marketplace: US and CA share the listing, so its photo is the same product. Never a different ASIN."""
    o = "CA" if mkt == "US" else "US"
    if not asin:
        return None
    return (good_img((catalog.get(o, {}).get(asin) or {}).get("imageUrl")) or good_img((xray.get((o, asin)) or {}).get("image"))
            or (good_img((ddimg.get(asin) or {}).get("imageUrl")) if o == "US" else None))

def put_image(ws, cell, url, role, product, mkt, brand, asin):
    u = good_img(url)
    c = ws[cell]
    c.border = BOX
    c.alignment = CENTER
    if not u and other_mkt_img(mkt, asin):
        u = other_mkt_img(mkt, asin)
        xmkt_img.append((mkt, asin))
        c.comment = Comment(f"Photo from Amazon.{'ca' if mkt == 'US' else 'com'}: same ASIN {asin}, same listing in both marketplaces.", "Tracker")
    if u:
        img_rows.append((role, product, mkt, brand, asin, u))
        if NO_IMAGE_FORMULA:
            c.value = "[image]"
        else:
            c.value = f'=_xlfn.IMAGE("{u}")'
    else:
        # no verified photo yet: show the Coming Soon placeholder (never another product's photo)
        c.value = "COMING SOON"
        c.font = F(size=6, color="808080")
        pic = XLImage(COMING_SOON)
        pic.width = pic.height = 72
        ws.add_image(pic, cell)

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

def _our_title_and_image(pid, mkt):
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
_main_pool = {}
def split_note(pid, mkt, v):
    """None if the variation is in this product's main review family; otherwise a note. A variation that sits in
    another of our products' main family (e.g. 'SATIN-4PC-TWIN' SKUs: the Twin of the 6 Pc set is a 4-piece set,
    so Amazon lists it in the Satin 6pc family) is a Command Center mapping difference, not a split listing."""
    if not v.get("split"):
        return None
    for (p2, m2), pool in _main_pool.items():
        if m2 == mkt and p2 != pid and pool == v.get("x_pool"):
            return ("mapped", f"Listed in the {PINFO[p2][2]} family on Amazon (Command Center maps it here) - expected, not an error")
    return ("split", "SEPARATE listing - not in the main review family")
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
            "status": g(x, "status") or it.get("status"), "image": good_img(it.get("imageUrl")) or good_img((xray.get((mkt, asin)) or {}).get("image")),
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
        lp_ = launch_price.get((mkt, pid, r.get("size")))
        if lp_ is not None:   # launched product: the confirmed launch price, live on every child (all colours) since Oct 15
            r["price_now"], r["now_src"] = lp_, "launch price, live Oct 15, 2026"
        if (mkt, r["asin"]) in our_page_flag:
            r["status"] = our_page_flag[(mkt, r["asin"])]
        xr = xray.get((mkt, r["asin"]))
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
    _main_pool[(pid, mkt)] = main_pool
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

# SellerBoard actual sales (Ecotero account) by current Amazon parent ASIN, per marketplace and window
SB_DAYS = {"pre": 30, "bfcm": 12, "dec": 30}
sellerboard = {}   # (mkt, parent_asin) -> {window: row}
for _f in sorted(f_ for f_ in glob.glob(f"{DATA}/sellerboard/*.csv") if re.search(r"/(US|CA)_(pre|bfcm|dec)\.csv$", f_)):
    for _r in csv.DictReader(open(_f, newline="", encoding="utf-8-sig")):
        def _sn(z):
            try:
                return float(z)
            except (TypeError, ValueError):
                return None
        # a parent can appear twice (e.g. an "Amazon.Found" SKU row); add the rows together
        _slot = sellerboard.setdefault((_r["marketplace"], _r["parent_asin"]), {})
        _new = {k: (_sn(v) if k not in ("marketplace", "window", "parent_asin", "name") else v) for k, v in _r.items()}
        _old = _slot.get(_r["window"])
        if _old:
            for k, v in _new.items():
                if k in ("unit_session_pct", "avg_sales_price") or not isinstance(v, float):
                    continue
                _old[k] = (_old.get(k) or 0) + v
            _old["avg_sales_price"] = (_old["sales"] / _old["units"]) if _old.get("units") else None
            _old["unit_session_pct"] = (_old["units"] / _old["sessions"] * 100) if _old.get("sessions") else None
        else:
            _slot[_r["window"]] = _new

# SellerBoard rows listed under an older parent or a lone child ASIN, matched by product name (2025 listings that
# have since been re-parented or retired). Only sheet/bedding rows; other categories are not tracked here.
SB_NAME_MAP = {
    "B0F2G983W3": 39,   # "Sleep Sanctuary Satin Sheets 4Pcs"                -> SSS4
    "B0F55Y1P53": 32,   # "SLEEP SANCTUARY ... Viscose Derived from Bamboo"  -> SL B6 (SL B4 not launched)
    "B0F7LX9RP3": 45, "B0F7LY4RD6": 45, "B0F7LY3994": 45, "B0FTSWF3M7": 45,   # "SLEEPHORIA Cooling Sheets - BreezeWeave 4 PC" -> SL Cooling 4pc
    "B0CQ3GXLCJ": 30,   # "DECOLURE ... Bamboo Sheets Queen Size | 6 Pc"      -> DC B6
    "B0D9HRYKBW": 48,   # "DECOLURE Cooling Bed Sheets Microfiber"           -> DC Cooling 4pc
    "B0CRF7S2TH": 31,   # "DECOLURE Satin Sheets Set 6pcs"                   -> DC S6
    "B0CRVZ1TTS": 37,   # "DECOLURE Satin Sheets Set - Silky ..." (no piece count; 4pc is the main satin family) -> DC S4
}
_sb_owner = {}   # (mkt, key) -> (pid, rule)
def _build_sb_owner():
    child_pid = {}
    for (p_, m_), d_ in skus.items():
        for x in d_.get("skus") or []:
            if x.get("asin"):
                child_pid.setdefault(x["asin"], set()).add(p_)
    cat_parent_pid = {}
    for m_c, items in catalog.items():
        for a_, it in items.items():
            pa = it.get("parentAsin")
            if pa and a_ in child_pid:
                cat_parent_pid.setdefault(pa, set()).update(child_pid[a_])
    for (m_, k_) in sellerboard:
        own = {p_ for p_ in child_pid.get(k_, set())}
        if len(own) == 1:
            _sb_owner[(m_, k_)] = (own.pop(), "child ASIN of this product")
            continue
        par = cat_parent_pid.get(k_, set())
        if len(par) == 1:
            _sb_owner[(m_, k_)] = (next(iter(par)), "Amazon parent of this product's children")
            continue
        if k_ in SB_NAME_MAP:
            _sb_owner[(m_, k_)] = (SB_NAME_MAP[k_], "matched by product name")
_build_sb_owner()

def sb_keys(pid, mkt):
    """SellerBoard rows that belong to this product: its current Amazon parent, older parents whose children are this
    product's, rows listed under one of its child ASINs (any marketplace), and the name-matched list above."""
    keys = {k_ for (m_, k_), (p_, _) in _sb_owner.items() if m_ == mkt and p_ == pid}
    ap = amazon_parent(pid, mkt)
    if ap and (mkt, ap) in sellerboard:
        keys.add(ap)
    return keys

_sb_cache = {}
def sb_of(pid, mkt):
    if (pid, mkt) in _sb_cache:
        return _sb_cache[(pid, mkt)]
    out = {}
    for k in sorted(sb_keys(pid, mkt)):
        for w, row in sellerboard[(mkt, k)].items():
            o = out.setdefault(w, {"rows": 0})
            o["rows"] += 1
            for f, v in row.items():
                if isinstance(v, float) and f not in ("unit_session_pct", "avg_sales_price"):
                    o[f] = (o.get(f) or 0) + v
    for o in out.values():
        o["avg_sales_price"] = (o["sales"] / o["units"]) if o.get("units") else None
        o["unit_session_pct"] = (o["units"] / o["sessions"] * 100) if o.get("sessions") else None
    _sb_cache[(pid, mkt)] = out
    return out

def lift_of(pid, mkt="US"):
    d = ours.get((pid, mkt)) or {}
    w1, w2, w3 = d.get("w1_bfcm") or {}, d.get("w2_pre30") or {}, d.get("w3_dec") or {}
    t1, t2, t3 = w1.get("total_sales_derived"), w2.get("total_sales_derived"), w3.get("total_sales_derived")
    sb = sb_of(pid, mkt)
    s_pre, s_bf, s_dec = ((sb.get(w) or {}).get("sales") for w in ("pre", "bfcm", "dec"))
    derived = ((t1 / 12) / (t2 / 30)) if (t1 and t2) else None
    if s_pre and s_bf:
        bf = sb["bfcm"]
        return {"lift": (s_bf / 12) / (s_pre / 30), "dec": ((s_dec / 30) / (s_pre / 30)) if s_dec else None, "src": "SellerBoard actual",
                "lift_derived": derived, "tacos": w1.get("tacos"), "pre_tacos": w2.get("tacos"),
                "tacos_actual": (abs(bf["advertising"]) / s_bf * 100) if bf.get("advertising") is not None and s_bf else None,
                "pre_tacos_actual": (abs(sb["pre"]["advertising"]) / s_pre * 100) if sb["pre"].get("advertising") is not None else None,
                "organic_share": (bf["units_organic"] / bf["units"]) if bf.get("units") and bf.get("units_organic") is not None else None,
                "bf_total": s_bf, "pre_total": s_pre, "dec_total": s_dec, "spend": w1.get("spend"), "ad_sales": w1.get("ad_sales")}
    if not derived:
        return None
    return {"lift": derived, "dec": ((t3 / 30) / (t2 / 30)) if t3 else None, "src": "derived (ad spend / TACoS)", "lift_derived": derived,
            "tacos": w1.get("tacos"), "pre_tacos": w2.get("tacos"), "tacos_actual": None, "pre_tacos_actual": None, "organic_share": None,
            "bf_total": t1, "pre_total": t2, "dec_total": t3, "spend": w1.get("spend"), "ad_sales": w1.get("ad_sales")}

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
        pid_ = (REASSIGN.get((row["marketplace"], row["child_asin"])) or (None, pid_))[1] if pid_ is not None else None
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
# The 6 dates with no inventory snapshot, inferred from sales that day (agent, DataHub amazon_sales) plus the
# readings either side (bracket). Kept apart from the observed figures above: an inference, not a stock reading.
stock_gap = {}   # (pid, mkt) -> Counter of status_inferred
_sg = f"{DATA}/stock/our_stock_bfcm2025_missing_dates_combined.csv"
if os.path.exists(_sg):
    for row in csv.DictReader(open(_sg, encoding="utf-8-sig")):
        name = row["product_name"].split("|")[0].strip() if "|" in row["product_name"] else row["product_name"]
        pid_ = STOCK_ALIAS.get(name)
        if pid_ is None:
            continue
        pid_ = (REASSIGN.get((row["marketplace"], row["child_asin"])) or (None, pid_))[1]
        c_ = stock_gap.setdefault((pid_, row["marketplace"]), {})
        c_[row["status_inferred"]] = c_.get(row["status_inferred"], 0) + 1
        if row["status_inferred"] == "sold_despite_zero_snapshots":
            c_.setdefault("_sold0", []).append(f"{row['child_asin']} {row['date'][5:]} ({row['units_ordered']} sold)")

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
    _drows = list(csv.DictReader(open(_dp, encoding="utf-8-sig")))
    # a few variations carry their long listing title instead of the product name; they belong to their campaign's product
    _sid = lambda row: (re.search(r"source_id=([0-9a-f]+)", row["notes"] or "") or [None, row["deal_start"]])[1]
    _camp_pid = {}
    for row in _drows:
        if DEAL_NAMES.get(row["product_name"]) is not None:
            _camp_pid.setdefault((row["marketplace"], _sid(row)), set()).add(DEAL_NAMES[row["product_name"]])
    for row in _drows:
        pid_ = DEAL_NAMES.get(row["product_name"])
        if pid_ is None:
            _cp = _camp_pid.get((row["marketplace"], _sid(row))) or set()
            pid_ = next(iter(_cp)) if len(_cp) == 1 else None
        if pid_ is None:
            continue
        pid_ = (REASSIGN.get((row["marketplace"], row["child_asin"])) or (None, pid_))[1]
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
# Our BFCM 2026 deal plan (BM, Slack, Oct 15, 2026); not yet visible in Amazon's deal feed (Command Center amazon_promotions)
plan26 = {}   # (pid, mkt) -> list of planned deals
_pp = f"{DATA}/deals/our_deals_bfcm2026_plan.csv"
if os.path.exists(_pp):
    for row in csv.DictReader(open(_pp, encoding="utf-8-sig")):
        if row["pid"]:
            plan26.setdefault((int(row["pid"]), row["marketplace"]), []).append(row)
def plan26_text(pid, mkt):
    out = []
    for d_ in plan26.get((pid, mkt)) or []:
        s_, e_ = d_["start"][5:].replace("-", "/"), d_["end"][5:].replace("-", "/")
        out.append(f"{d_['deal_type']} {s_}" + (f"-{e_}" if e_ != s_ else "") + (f" ({d_['status']}: {d_['note']})" if d_["status"] != "planned" else ""))
    return "; ".join(out) or None

# Deal pricing evidence and pre-BFCM decisions from Slack (Umair Tahir's deal reviews, AB's STR tests), Oct 13-15, 2026
slack_deal = {}   # (pid, mkt) -> rows; ("ALL", None) for account-wide rules
_sd = f"{DATA}/deals/slack_deal_pricing_2026-10-15.csv"
if os.path.exists(_sd):
    for row in csv.DictReader(open(_sd, encoding="utf-8-sig")):
        slack_deal.setdefault((int(row["pid"]), row["marketplace"]) if row["pid"] else ("ALL", None), []).append(row)

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
# US competitor files: keepa_history_p1.csv, keepa_history_p2_batch<N>.csv (or the cumulative keepa_history_p2.csv,
# which supersedes the batches). Canada (keepa_history_ca*.csv) is kept apart: same ASIN can sell in both markets.
_kfiles = sorted(f_ for f_ in glob.glob(f"{DATA}/keepa/keepa_history_*.csv")
                 if not re.search(r"_(coverage|provenance)\.csv$", f_) and "/keepa_history_ca" not in f_ and "/keepa_history_ours" not in f_)
if any(f_.endswith("/keepa_history_p2.csv") for f_ in _kfiles):
    _kfiles = [f_ for f_ in _kfiles if "_p2_batch" not in f_]
def _keepa_summaries(files, cur):
    """Keepa BFCM 2025 summary per ASIN for one marketplace (files of that marketplace only)."""
    out = {}
    _kd, _kcov = {}, {}
    for _kh in files:
        _seen_day = set()
        for row in csv.DictReader(open(_kh, encoding="utf-8-sig")):
            _kd.setdefault(row["asin"], {})[row["date"]] = row          # one row per ASIN per day, last file wins
        _cf = _kh[:-4] + "_coverage.csv"
        if os.path.exists(_cf):
            _kcov.update({r["asin"]: r for r in csv.DictReader(open(_cf, encoding="utf-8-sig"))})
    _kd = {a: list(d.values()) for a, d in _kd.items()}
    if _kd:
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
            elif cov.get("tracking_since") and cov["tracking_since"] > "2025-12-01":
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
                    notes.append(f"Buy Box RAISED in BFCM week (median {cur}{statistics.median(bb_bf):,.2f} vs {cur}{pre_med:,.2f} before)")
                lps = sorted({_f(r["list_price"]) for r in bf if _f(r["list_price"])})
                if lps:
                    notes.append("List Price " + "/".join(f"{cur}{x:,.2f}" for x in lps))
            oos_bf = [r["out_of_stock"] for r in bf if r["out_of_stock"] in ("Y", "N")]
            out[a] = {
                "bf_type": typ, "bf_dates": dates, "bf_pre": pre_eff, "bf_low": low,
                "bsr_pre": round(statistics.median(rk_pre)) if rk_pre else None, "bsr_bf": round(statistics.median(rk_bf)) if rk_bf else None,
                "bf_oos": ("Y" if "Y" in oos_bf else ("N" if len(oos_bf) == len(bf) and oos_bf else None)),
                "notes": "; ".join(notes) or None, "kp_days": len(bb_bf), "raised": any("RAISED" in n for n in notes),
            }
    return out

keepa25 = _keepa_summaries(_kfiles, "$")
# Canada (Amazon.ca, domain 6, CAD): kept apart, because the same ASIN can sell in both markets at different prices.
# The final keepa_history_ca.csv supersedes the partial delivery.
_kfiles_ca = sorted(f_ for f_ in glob.glob(f"{DATA}/keepa/keepa_history_ca*.csv") if not re.search(r"_(coverage|provenance)\.csv$", f_))
_kfiles_ca.sort(key=lambda f_: (0 if "_partial" in f_ else 1, f_))
if any(f_.endswith("/keepa_history_ca.csv") for f_ in _kfiles_ca):
    _kfiles_ca = [f_ for f_ in _kfiles_ca if f_.endswith("/keepa_history_ca.csv")]
keepa25_ca = _keepa_summaries(_kfiles_ca, "C$")
_ca_pending = set()
for _fc in glob.glob(f"{DATA}/keepa/keepa_history_ca*_coverage.csv"):
    _ca_pending |= {r["asin"] for r in csv.DictReader(open(_fc, encoding="utf-8-sig")) if r.get("acquisition_status") == "not_yet_fetched"}
_ca_pending -= set(keepa25_ca)

# Our hero children, BFCM 2025 (Command Center keepa_history, US, pulled 2026-10-14). Keepa holds no Buy Box series
# for our own ASINs, so price = lowest new offer (we are the only seller); daily values are Eastern days, carried forward.
HERO_PID = {"Decolure Bamboo Fitted Sheet": 73, "Decolure Bamboo Sheets 6 Piece": 30, "Decolure Bamboo Sheets 4 Piece": 59,
            "Sleephoria Bamboo Sheets 6 Piece": 32, "Sleephoria Bamboo Sheets 4 Piece": 36, "CooLinens Cooling Pillowcases 2 Piece": 70,
            "Decolure Cooling Sheets 4 Piece": 48, "Sleephoria Cooling Sheets 4 Piece": 45, "Sleephoria Cooling Fitted Sheet": 44,
            "Sleephoria Cooling Pillowcases": 43, "Sleephoria Cooling Comforter": 42, "Decolure Waterproof Chair Cover": 33,
            "Decolure Linen Curtains": 53, "Decolure Front Door Welcome Sign": 58, "Decolure Beach Towel": 49, "Sleephoria Quilt Set": 46,
            "Decolure Satin Sheets 4 Piece": 37, "Decolure Satin Sheets 6 Piece": 31, "Decolure Satin Fitted Sheet": 38,
            "Sleephoria Satin Sheets 4 Piece": 39, "Decolure Silk Pillowcase": 55, "Sleephoria Silk Sleep Mask - Velcro": 57,
            "Sleephoria Silk Sleep Mask - Contoured": 56}
hero25 = {}   # (pid, "US") -> summary for our hero child
_ho = f"{DATA}/keepa/keepa_history_ours_cc.csv"
if os.path.exists(_ho):
    _hp = {r["asin"]: HERO_PID.get(r["our_product"]) for r in csv.DictReader(open(f"{DATA}/keepa/keepa_history_ours_cc_coverage.csv", encoding="utf-8-sig"))}
    _hr = {}
    for row in csv.DictReader(open(_ho, encoding="utf-8-sig")):
        _hr.setdefault(row["asin"], []).append(row)
    for a, rs in _hr.items():
        if _hp.get(a) is None:
            continue
        def _eff(r):
            v_ = [x for x in (_f(r["price_new_offer"]), _f(r["lightning_deal_price"]), _f(r["prime_exclusive_price"])) if x]
            return min(v_) if v_ else None
        pre = [r for r in rs if KP_PRE[0] <= r["date"] <= KP_PRE[1]]
        bf = [r for r in rs if KP_BF[0] <= r["date"] <= KP_BF[1]]
        pp, bp = [_eff(r) for r in pre if _eff(r)], [_eff(r) for r in bf if _eff(r)]
        rp, rb = [_f(r["sales_rank"]) for r in pre if _f(r["sales_rank"])], [_f(r["sales_rank"]) for r in bf if _f(r["sales_rank"])]
        ped = [r["date"][5:] for r in bf if _f(r["prime_exclusive_price"])]
        cps = sorted({r["coupon"] for r in rs if r["coupon"]})
        hero25[(_hp[a], "US")] = {
            "asin": a, "pre": statistics.median(pp) if pp else None, "bf": statistics.median(bp) if bp else None, "low": min(bp) if bp else None,
            "rank_pre": round(statistics.median(rp)) if rp else None, "rank_bf": round(statistics.median(rb)) if rb else None,
            "ped": (f"{ped[0]} to {ped[-1]} ({len(ped)} days)" if ped else None), "coupons": ", ".join(cps) or None}

# Canadian competitors from Amazon.ca page research (Prompt 9), by our product
CA_PRODUCT_PID = {"DC B4": 59, "DC B6": 30, "DC S4": 37, "DC S6": 31, "SSS4": 39, "DC Satin Fitted": 38}
ca_comp = {}
for _f in sorted(glob.glob(f"{DATA}/ca_competitors/ca_competitors*.csv")):
    for _r in csv.DictReader(open(_f, newline="", encoding="utf-8-sig")):
        _p = CA_PRODUCT_PID.get(_r.get("our_product"))
        if _p is not None:
            ca_comp.setdefault(_p, []).append(_r)

# Competitor details from the exact Amazon.com page (agent Part A, Oct 14): image, size and colour from the page's own
# variation attributes. Requests that redirected to another ASIN are left out (no substitution).
comp_det = {}
for _f in sorted(glob.glob(f"{DATA}/competitor_details/competitor_details_us*.csv")):
    for _r in csv.DictReader(open(_f, encoding="utf-8-sig")):
        if "identity unresolved" not in (_r.get("notes") or ""):
            comp_det[_r["asin"]] = _r

str_now = {}
for _f in sorted(glob.glob(f"{DATA}/str/str_check_*.csv")):
    for row in csv.DictReader(open(_f, encoding="utf-8-sig")):
        str_now[row["asin"]] = row

# Command Center Competitor Summary (competitors_roster, scrape week of Oct 11, 2026): one row per mapped rival and
# product. Its price, BSR and reviews belong to the rival's seed ASIN, often a different variation from the child
# tracked here, so they sit beside the child figures rather than replacing them. It also carries the current tier,
# the X-Ray sales band and listing assets, and rivals mapped after the tracker's snapshot are added from it.
roster = {}   # (pid, cid) -> roster row
for _f in glob.glob(f"{DATA}/cc_roster/*_US.json"):
    _d = jl(_f, {}) or {}
    for _r in _d.get("rows") or []:
        roster[(_d["productId"], _r["competitorProductId"])] = _r
_by_cid = {}
for (_p, _m), _dd in cc.items():
    if _m == "US":
        for _cp in _dd.get("competitors", []):
            _by_cid.setdefault(_cp["id"], _cp)
roster_added = 0
for (_p, _c), _r in sorted(roster.items()):
    _dd = cc.get((_p, "US"))
    if not _dd or any(_cp.get("id") == _c for _cp in _dd["competitors"]):
        continue
    _base = dict(_by_cid.get(_c) or {"id": _c, "child_asin": _r.get("parentAsin"), "parent_asin": None, "brand": (_r.get("brand") or "").strip(),
                                       "name": (_r.get("name") or "").split(" - ", 1)[-1], "price": _r.get("price"), "bsr": _r.get("bsr"),
                                       "rating": _r.get("rating"), "reviews": _r.get("reviews"), "seen_on": (_r.get("weekStartDate") or "")[:10]})
    _base["tier"] = _r.get("tier")
    _dd["competitors"].append(_base)
    roster_added += 1

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
            # The Command Center holds no CA competitors: use the Amazon.ca page research (AGENT_PROMPTS Prompt 9)
            for row in ca_comp.get(pid, []):
                f_ = lambda z: float(z) if z not in (None, "") else None
                ch = row["child_asin"]
                kp_ = keepa25_ca.get(ch)
                rec = {
                    "pid": pid, "mkt": "CA", "family": fam, "product": short, "tab": tab_name(pid, mkt), "role": role,
                    "cid": None, "brand": row["competitor_brand"].strip(), "parent": row["parent_asin"] or None, "child": ch,
                    "title": row["title"], "tier": "Untiered", "image": good_img(row["main_image_url"]), "image_asin": ch,
                    "price": f_(row["price_cad"]), "lp": None, "bsr": f_(row["bsr"]), "wk": None,
                    "rating": f_(row["rating"]), "reviews": f_(row["review_count"]), "seen": row["check_date"],
                    "size": row["size"] or None, "colour": row["colour"] or None,
                    "var": f_(row["variation_count"]), "var_src": "Amazon.ca page" if row["variation_count"] else None,
                    "ful": None, "country": None, "listed": None,
                    "str_show": row["strikethrough_shown"] or "unknown", "str_label": row["strikethrough_label"] or None,
                    "str_price": f_(row["strikethrough_price_cad"]), "page_price": f_(row["price_cad"]),
                    "deal_now": ", ".join(z for z in [row["deal_badge"] if row["deal_badge"] not in ("", "none") else None,
                                                     ("coupon " + row["coupon"]) if row["coupon"] else None] if z) or "none",
                    "stock_now": row["in_stock"] or None, "str_checked": f"{row['check_date']} {row['check_time_et']}",
                    "ca_rank": row["organic_rank"], "ca_keyword": row["keyword"], "material": row["material"],
                    "notes": (f"Amazon.ca organic #{row['organic_rank']} for '{row['keyword']}'; {row['material']}; "
                              f"{row['bought_past_month'] + ' bought past month; ' if row['bought_past_month'] else ''}{row['notes'][:160]}"),
                }
                if kp_:
                    rec.update({k: kp_[k] for k in ("bf_type", "bf_dates", "bf_pre", "bf_low", "bsr_pre", "bsr_bf", "bf_oos")})
                    rec["bf_disc_v"] = (1 - kp_["bf_low"] / kp_["bf_pre"]) if kp_["bf_pre"] and kp_["bf_low"] else None
                    rec["bsr_lift_v"] = (kp_["bsr_pre"] / kp_["bsr_bf"]) if kp_["bsr_pre"] and kp_["bsr_bf"] else None
                    rec["raised"] = kp_["raised"]
                    if kp_.get("notes"):
                        rec["notes"] = f"{rec['notes']} Keepa .ca: {kp_['notes']}"
                elif ch in _ca_pending:
                    rec["bf_type"] = None
                    rec["notes"] = f"{rec['notes']} Keepa .ca history still being pulled."
                records.append(rec)
            continue
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
            pg = comp_det.get(ch)
            if pg:
                if not rec["image"] and good_img(pg.get("main_image_url")):
                    rec["image"], rec["image_asin"] = pg["main_image_url"], ch
                rec["size"] = pg.get("size") or rec["size"]
                rec["colour"] = pg.get("color") or rec["colour"]
                # brand and parent as Amazon shows them today (page; Keepa agreed on every tracked case); Command Center value kept
                _pb = re.sub(r"^(Brand:\s*|Visit the\s+)|\s+Store$", "", pg.get("brand") or "").strip()
                if _pb and _pb.lower().replace(" ", "")[:5] != rec["brand"].lower().replace(" ", "")[:5]:
                    rec["brand_cc"], rec["brand"] = rec["brand"], _pb
                if pg.get("parent_asin") and pg["parent_asin"] != rec["parent"]:
                    rec["parent_cc"], rec["parent"] = rec["parent"], pg["parent_asin"]
            ro_ = roster.get((pid, cp.get("id")))
            if ro_ is not None:
                rec["tier"] = ro_.get("tier") or "Untiered"
                rec["ro"] = {k: ro_.get(k) for k in ("parentAsin", "price", "bsr", "reviews", "rating", "salesPerWeek", "salesBand", "reviewVelocity",
                                                     "bsrTrendPct", "bsrTrendDirection", "coupon", "deal", "strikethroughPct", "inStock", "hasAplus",
                                                     "imageCount", "bulletCount", "beatability", "beatabilityProfile", "tierRationale", "tierSetBy",
                                                     "relevance", "priceIndex", "weekStartDate")}
            sc = str_now.get(ch) or {}
            if sc:
                num = lambda z: float(z) if z not in (None, "") else None
                rec.update({"str_show": sc.get("strikethrough_shown") or "unknown", "str_label": sc.get("strikethrough_label") or None,
                            "str_price": num(sc.get("strikethrough_price")), "page_price": num(sc.get("price")),
                            "deal_now": ", ".join(z for z in [sc.get("deal_badge") if sc.get("deal_badge") not in ("", "none") else None,
                                                               ("coupon " + sc["coupon"]) if sc.get("coupon") else None] if z) or ("none" if sc.get("strikethrough_shown") else None),
                            "stock_now": sc.get("in_stock") or None, "str_checked": f"{sc.get('check_date')} {sc.get('check_time_et')}"})
            # price: the newest reading for this exact ASIN (Amazon page Oct 14, then Oct 13 page check, then the Command Center)
            rec["price_src"] = f"Command Center {(rec.get('seen') or '')[:10]}".strip()
            _fresh = None
            if pg and pg.get("current_price"):
                _fresh = (float(pg["current_price"]), f"Amazon page {pg.get('check_date') or '2026-10-14'}")
            elif rec.get("page_price"):
                _fresh = (rec["page_price"], f"Amazon page {(rec.get('str_checked') or '')[:10]}")
            if _fresh:
                if rec.get("price") is not None and abs(rec["price"] - _fresh[0]) > 0.005:
                    rec["price_cc"] = rec["price"]
                rec["price"], rec["price_src"] = _fresh
            kp_ = keepa25.get(ch)
            if kp_:
                rec.update({k: kp_[k] for k in ("bf_type", "bf_dates", "bf_pre", "bf_low", "bsr_pre", "bsr_bf", "bf_oos", "notes")})
                rec["bf_disc_v"] = (1 - kp_["bf_low"] / kp_["bf_pre"]) if kp_["bf_pre"] and kp_["bf_low"] else None
                rec["bsr_lift_v"] = (kp_["bsr_pre"] / kp_["bsr_bf"]) if kp_["bsr_pre"] and kp_["bsr_bf"] else None
                rec["raised"] = kp_["raised"]
            records.append(rec)

_allk = set().union(*(r_.keys() for r_ in records)) if records else set()
for r_ in records:            # CA rows lack the Command Center / ASINsight fields: give every row the same keys
    for k_ in _allk:
        r_.setdefault(k_, None)

# ASSUMED BFCM 2026 deal price, until BM sends the final prices (agreed with Shayan, Oct 15, 2026).
# Reference price = today's live price of the hero ASIN, assumed unchanged until Nov 18 (Amazon sets the deal's reference
# price the day before the deal). Deal price = last year's BFCM price for the same ASIN when the product ran a 2025 deal
# (the price that produced the 2025 lift); otherwise the reference cut by the median discount competitors used on this
# product in BFCM 2025 (price cuts). Canada takes the US product's discount on its own live CAD price.
# BFCM 2026 discount rule (Umair Tahir, relayed by Shayan Rana, Oct 15, 2026): 20% off on the high days, 15% on the other
# deal days. High days are taken as Black Friday to Cyber Monday (Nov 27-30, 2026) until Umair confirms the exact days.
RULE26 = {"std": 0.15, "peak": 0.20, "peak_days": "Nov 27-30, Black Friday to Cyber Monday", "std_days": "Nov 19-26",
          "src": "team rule agreed Oct 15, 2026"}

def deal_assumption(pid, mkt):
    """Assumed 2026 deal prices: today's live price of the hero ASIN cut by Umair's 15% / 20% rule, with the 2025 evidence beside it."""
    if not plan26.get((pid, mkt)):
        return None
    def live(m_, asin=None):
        vs = [v for v in our_variations(pid, m_) if v.get("price_now") is not None]
        if asin:
            vs = [v for v in vs if v["asin"] == asin] or vs[:0]
        if not vs:
            return None, None
        if not asin:
            best = our_title_and_image(pid, m_)[2]
            vs = [v for v in vs if v["asin"] == best] or sorted(vs, key=lambda v: -(v.get("units_28d") or 0))[:1]
        return vs[0]["asin"], vs[0]["price_now"]
    hk = hero25.get((pid, "US")) or {}
    if mkt == "US":
        asin, ref = live("US", hk.get("asin")) if hk.get("asin") else live("US")
        if not ref:
            asin, ref = live("US")
    else:
        asin, ref = live("CA")
    ev = {"asin": hk["asin"], "pre": hk["pre"], "bf": hk["bf"], "depth": 1 - hk["bf"] / hk["pre"]} if hk.get("pre") and hk.get("bf") else None
    comp = [x["bf_disc_v"] for x in records if x["pid"] == pid and x["mkt"] == "US" and x.get("bf_type") == "Price cut only" and isinstance(x.get("bf_disc_v"), float)]
    out = {"asin": asin, "ref": ref, "std": RULE26["std"], "peak": RULE26["peak"],
           "deal_std": round(ref * (1 - RULE26["std"]), 2) if ref else None, "deal_peak": round(ref * (1 - RULE26["peak"]), 2) if ref else None,
           "ev25": ev, "comp25": {"median": statistics.median(comp), "n": len(comp)} if comp else None,
           "basis": f"{RULE26['src']}: {RULE26['peak']:.0%} off on the high days ({RULE26['peak_days']}), {RULE26['std']:.0%} off on the other deal days ({RULE26['std_days']})"}
    out["deal"], out["depth"] = out["deal_std"], out["std"]
    return out

def deal_evidence_text(da):
    parts = []
    if da.get("ev25"):
        e = da["ev25"]
        parts.append(f"our BFCM 2025 deal on {e['asin']} (US, Keepa): ${e['pre']:,.2f} before, ${e['bf']:,.2f} during, {e['depth']:.0%} off")
    if da.get("comp25"):
        parts.append(f"US competitors' median price cut in BFCM 2025: {da['comp25']['median']:.0%} ({da['comp25']['n']} rivals)")
    return "; ".join(parts)

# ------------------------------------------------------------------ BFCM 2026 stock outlook (SellerBoard, Oct 15, 2026)
# Per child ASIN: stock at Amazon now (on hand = FBA stock + units moving between Amazon warehouses), units already sent to
# Amazon (SellerBoard "sent to FBA"), and SellerBoard's sales velocity (units a day). Demand is walked day by day:
# Oct 16 - Nov 18 at today's pace, Nov 19 - 30 at today's pace x the product's own BFCM 2025 lift (SellerBoard, BFCM week vs
# the 30 days before), where that lift is reliable; otherwise the account's BFCM 2025 lift is assumed and flagged.
# No ETA exists in SellerBoard, so inbound is shown by Amazon shipment status and the outlook is given with and without it.
STOCK_ASOF, PRE_DAYS, BF_DAYS = "2026-10-15", 34, 12
def _acct_lift(m):
    try:
        pre = sum(float(r["sales"] or 0) for r in csv.DictReader(open(f"{DATA}/sellerboard/{m}_pre.csv", encoding="utf-8-sig")))
        bf = sum(float(r["sales"] or 0) for r in csv.DictReader(open(f"{DATA}/sellerboard/{m}_bfcm.csv", encoding="utf-8-sig")))
        return (bf / 12) / (pre / 30) if pre and bf else None
    except FileNotFoundError:
        return None
ACCT_LIFT = {m: _acct_lift(m) for m in ("US", "CA")}

sb_inv = {}   # (mkt, asin) -> summed stock fields
_inv = f"{DATA}/stock/sellerboard_inventory_2026-10-15.csv"
if os.path.exists(_inv):
    for row in csv.DictReader(open(_inv, encoding="utf-8-sig")):
        k = ("CA" if row["marketplace"] == "Amazon.ca" else "US", row["asin"])
        d = sb_inv.setdefault(k, {"on_hand": 0.0, "fba": 0.0, "inbound": 0.0, "vel": 0.0, "skus": []})
        for f_, c_ in (("on_hand", "on_hand"), ("fba", "fba_stock"), ("inbound", "sent_to_fba"), ("vel", "sales_velocity")):
            d[f_] += float(row[c_] or 0)
        d["skus"].append(row["sku"])
sb_ship = {}  # (mkt, asin) -> [(shipment_id, status, units still inbound)]
_shp = f"{DATA}/stock/sellerboard_inbound_shipments_2026-10-15.csv"
if os.path.exists(_shp):
    for row in csv.DictReader(open(_shp, encoding="utf-8-sig")):
        u_ = float(row["units_still_inbound_calc"] or 0)
        if u_ > 0:
            sb_ship.setdefault(("CA" if row["marketplace_inferred"] == "Amazon.ca" else "US", row["asin"]), []).append((row["shipment_id"], row["status"], int(u_)))

def stock_lift(pid, mkt):
    lf = lift_of(pid, mkt) or {}
    if lf.get("src") == "SellerBoard actual" and lf.get("lift") and 0.8 <= lf["lift"] <= 8:
        return lf["lift"], "own BFCM 2025 lift (SellerBoard)"
    return ACCT_LIFT.get(mkt), f"ASSUMED: account BFCM 2025 lift ({mkt}); product's own 2025 lift " + ("not reliable" if lf.get("lift") else "not available")

def oos_date(stock, v, lift):
    """Day stock runs out walking the demand calendar; None when it lasts past Nov 30 or nothing sells."""
    if not v:
        return None
    t0 = dt.date(2026, 10, 15)
    if stock < v * PRE_DAYS:
        return t0 + dt.timedelta(days=stock / v)
    if stock < v * PRE_DAYS + v * lift * BF_DAYS:
        return dt.date(2026, 11, 18) + dt.timedelta(days=(stock - v * PRE_DAYS) / (v * lift))
    return None

stock26 = {}
def stock_outlook(pid, mkt):
    if (pid, mkt) in stock26:
        return stock26[(pid, mkt)]
    lift, lift_src = stock_lift(pid, mkt)
    rows, seen_ = [], set()
    for v_ in our_variations(pid, mkt):
        inv = sb_inv.get((mkt, v_["asin"]))
        if not inv or v_["asin"] in seen_:   # one row per ASIN (two SKU rows can share an ASIN)
            continue
        seen_.add(v_["asin"])
        vel, vel_src = inv["vel"], "SellerBoard velocity"
        if not vel and (v_.get("units_28d") or 0) > 0:
            vel, vel_src = v_["units_28d"] / 28, "units last 28 days / 28 (no SellerBoard velocity: out of stock)"
        need = vel * PRE_DAYS + vel * (lift or 1) * BF_DAYS
        oh, ib = inv["on_hand"], inv["inbound"]
        if not vel and not oh and not ib:
            continue
        if oh <= 0 and vel > 0:
            status = "Out of stock now"
        elif oh >= need:
            status = "Covered to Nov 30"
        elif oh + ib >= need:
            status = "Needs inbound in time"
        else:
            status = "Short even with inbound"
        rows.append({"asin": v_["asin"], "sku": v_.get("sku") or ", ".join(inv["skus"]), "size": v_.get("size"), "colour": v_.get("colour"),
                     "on_hand": oh, "inbound": ib, "vel": vel, "vel_src": vel_src, "need": need, "short": max(0.0, need - oh - ib),
                     "oos": oos_date(oh, vel, lift or 1), "oos_in": oos_date(oh + ib, vel, lift or 1), "status": status,
                     "ships": sb_ship.get((mkt, v_["asin"]), []), "u28": v_.get("units_28d")})
    rows.sort(key=lambda r: -r["vel"])
    cnt = collections.Counter(r["status"] for r in rows)
    out = {"lift": lift, "lift_src": lift_src, "rows": rows, "on_hand": sum(r["on_hand"] for r in rows), "inbound": sum(r["inbound"] for r in rows),
           "vel": sum(r["vel"] for r in rows), "need": sum(r["need"] for r in rows), "short": sum(r["short"] for r in rows), "counts": dict(cnt),
           "risk_vel": sum(r["vel"] for r in rows if r["status"] != "Covered to Nov 30")}
    stock26[(pid, mkt)] = out
    return out

# ------------------------------------------------------------------ competitor classification: direct vs alternative
# A competitor is DIRECT only when it sells the same product type in the same material family as ours. Material comes from
# the competitor's own product page (material attribute) where checked, else from its title; product type from the title.
OUR_MATERIAL = {   # (material class, how we know)
    **{p: ("Bamboo viscose", "our listing: viscose from bamboo") for p in (59, 30, 32, 36, 73, 40)},
    **{p: ("Satin (polyester)", "our listing: polyester satin") for p in (37, 31, 39, 74, 38)},
    55: ("Silk", "our listing: mulberry silk"), 56: ("Silk", "our listing: silk"), 57: ("Silk", "our listing: silk"),
    69: ("Synthetic cooling knit", "product spec: CooLoom, 90% nylon / 10% spandex"),
    70: ("Synthetic cooling knit", "same CooLoom cooling fabric as the CooLinens sheets"),
    **{p: ("Synthetic cooling knit", "BreezeWeave cooling fabric (nylon-spandex family, as CooLoom)") for p in (45, 76, 44, 42, 43)},
    48: ("Microfiber / polyester", "different material from the Sleephoria cooling sheets: microfiber with some bamboo viscose"),
}
OUR_TYPE = {**{p: "Sheet set" for p in (59, 30, 32, 36, 37, 31, 39, 74, 48, 45, 76, 69)}, 73: "Fitted sheet", 38: "Fitted sheet", 44: "Fitted sheet",
            40: "Pillowcase", 55: "Pillowcase", 70: "Pillowcase", 43: "Pillowcase", 42: "Comforter"}
MAT_RULES = [   # order matters: first match wins
    ("Synthetic cooling knit", r"nylon|spandex|elastane|polyamide|arc-?chill|blendtek|q-?max|ice silk|coolmax|cool-?touch fib"),
    ("Lyocell / eucalyptus", r"lyocell|tencel|eucalyptus"),
    ("Bamboo viscose", r"bamboo|rayon|viscose"),
    ("Silk", r"\bsilk\b|mulberry"),
    ("Satin (polyester)", r"satin"),
    ("Linen", r"linen|flax"),
    ("Cotton", r"cotton|percale|sateen weave|egyptian"),
    ("Microfiber / polyester", r"microfiber|microfibre|polyester|brushed"),
]
def material_of(x):
    page = ((comp_det.get(x["child"]) or {}).get("material") or "").strip()
    for txt, how in ((page, "product page material"), (x.get("title") or "", "title")):
        t = txt.lower()
        for cls, pat in MAT_RULES:
            if re.search(pat, t):
                if cls == "Synthetic cooling knit" and re.search(r"bamboo|rayon|viscose", t) and not re.search(r"nylon|spandex|elastane|arc-?chill|blendtek", t):
                    continue
                return cls, f"{how}: {txt[:60]}"
    return None, "material not stated on the page or in the title"
def type_of(x):
    t = (x.get("title") or "").lower()
    if re.search(r"pillow ?cases?\b", t) and not re.search(r"sheet", t):
        return "Pillowcase"
    if re.search(r"comforter|duvet|blanket|quilt", t) and not re.search(r"sheet set|sheets set", t):
        return "Comforter"
    if re.search(r"fitted sheet only|fitted sheet\b", t) and not re.search(r"\bset\b|piece|pcs|\bpc\b|pillowcase", t):
        return "Fitted sheet"
    if re.search(r"sheet", t):
        return "Sheet set" if re.search(r"\bset\b|piece|pcs|\bpc\b|sheets\b", t) else None
    return None
CLS_RANK = {"Direct": 0, "Material not verified": 1, "Alternative material": 2, "Different product type": 3, "Not classified": 4}
for x in records:
    om = OUR_MATERIAL.get(x["pid"])
    ot = OUR_TYPE.get(x["pid"])
    if not om or not ot:
        x["cls"], x["cls_why"], x["mat"] = "Not classified", "Not a sheet, pillowcase or comforter product; competitors are compared on price and sales only.", None
        continue
    mat, how = material_of(x)
    ct = type_of(x)
    x["mat"] = mat
    if ct and ct != ot:
        x["cls"], x["cls_why"] = "Different product type", f"Sells a {ct.lower()}; ours is a {ot.lower()}."
    elif mat is None:
        x["cls"], x["cls_why"] = "Material not verified", f"{ot} like ours, but the material is not stated ({how}); verify before treating as direct."
    elif mat == om[0]:
        x["cls"], x["cls_why"] = "Direct", f"Same product ({ot.lower()}) in the same material family: {mat} ({how}); ours: {om[1]}."
    else:
        x["cls"], x["cls_why"] = "Alternative material", f"{ot} in {mat} ({how}); ours is {om[0]} ({om[1]}). Shopper may cross-shop, but not like-for-like."

tier_rank = {"Aspirational": 0, "Beatable": 1, "Poor": 2, "Untiered": 3}
records.sort(key=lambda r: ([p[0] for p in PRODUCTS].index(r["pid"]), CLS_RANK.get(r.get("cls"), 4), tier_rank.get(r["tier"], 3), -(r["wk"] or 0)))

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
    m_ = r["mkt"]
    bys = our_size_price.get((r["pid"], m_), {})
    _m = re.match(r"\s*(California King|Cal King|Twin XL|King|Queen|Full|Twin)\b", r["size"] or "", re.I)
    want = {"cal king": "California King"}.get(_m.group(1).lower(), _m.group(1).title()) if _m else ("Queen" if not r["size"] else r["size"])
    want = {"Twin Xl": "Twin XL"}.get(want, want)
    lead = f"Same size ({want})" if r["size"] else "Size not stated - vs our Queen"
    if m_ == "CA":
        lead += ", CAD"
    lp_, src_ = _live(r["pid"], m_, want)
    if lp_ is not None:
        r["our_same"], r["basis"], r["our_live"] = lp_, f"{lead}. Ours live: {src_}", True
    elif bys.get(want) is not None:
        r["our_same"], r["basis"], r["our_live"] = bys[want], f"{lead}. Ours: Command Center fee feed, Mar 2026 - STALE", False
    elif our_blend.get((r["pid"], m_)) is not None:
        r["our_same"], r["basis"], r["our_live"] = our_blend[(r["pid"], m_)], "vs our blended price (Command Center, Mar 2026 - STALE)", False
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
    ("img", "Image", 11, "id", "Live product image (Excel 365 / Google Sheets IMAGE). 'COMING SOON' picture = no verified image yet; see Data Gaps.", None),
    ("brand", "Brand", 14, "id", None, None),
    ("title", "Product title", 34, "id", None, None),
    ("tier", "Tier", 9, "id", "Command Center mapping tier against this product.", None),
    ("cls", "Competitor type", 12, "id", "Direct = same product type and same material family as ours. Alternative material = same product type, different material (cross-shopped, not like-for-like). Material not verified = no material on the page or title. Different product type = e.g. fitted sheet only vs our set.", None),
    ("mat", "Material", 12, "id", "Material family from the competitor's product page where checked, else its title.", None),
    ("cls_why", "Why this type", 30, "id", None, None),
    ("parent", "Parent ASIN", 11, "id", None, None),
    ("child", "Tracked child ASIN", 11, "id", None, None),
    ("size", "Size", 8, "id", "From the competitor's Amazon page (variation attributes, Oct 14, 2026) where captured; otherwise parsed from the title.", None),
    ("colour", "Colour", 9, "id", "From the competitor's Amazon page (variation attributes, Oct 14, 2026) where captured; otherwise parsed from the title.", None),
    ("var", "Variations", 7, "dd", "Variation count: Data Dive family count, else ASINsight child-ASIN count.", "#,##0"),
    ("hero", "Hero child ASINs (share of their visibility)", 26, "st", "The fewest child ASINs carrying 80% of this competitor's ASINsight impressions.", None),
    ("price", "Price ($)", 8, "cc", "Newest price for this exact ASIN: Amazon page (Oct 13-14, 2026) where checked, otherwise the Command Center snapshot. A cell comment gives the older Command Center price when they differ.", "$#,##0.00"),
    ("lp", "List Price ($)", 8, "cc", None, "$#,##0.00"),
    ("lp_pct", "List Price % over", 7, "calc", None, "0.0%"),
    ("band", "STR band", 10, "calc", "How far List Price sits above price. Oct 13 page check of 154 core rivals: strikethrough shown on 2 of 3 at <=12%, 13 of 13 at 12-25%, 11 of 13 above 25% - the size of the gap does not stop Amazon showing it.", None),
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
               "st": "SEARCH STRATEGY - Command Center ASINsight", "str": "STR NOW - Amazon page check (Oct 13, P1 + P2)", "kp": "BFCM 2025 - Keepa (P1 filled; yellow = not pulled yet)"}

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
    t = ws.cell(row=1, column=1, value=f"{pname}  ·  {('Amazon.com (US)' if mkt == 'US' else 'Amazon.ca (CA)')}  ·  {fam}  ·  BFCM role: {role}  ·  Scope: {scope_of(pid)}")
    t.font = F(size=14, bold=True, color="FFFFFF"); t.fill = HDR; t.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 28
    if pid in NOT_LAUNCHED or pid in LAUNCHING:
        ws.merge_cells(start_row=2, start_column=3, end_row=2, end_column=NC)
        b_ = ws.cell(row=2, column=3, value=("NOT LAUNCHED YET (confirmed Oct 14, 2026): no live price, rating or sales expected; excluded from the gap counts on Data Check."
                                             if pid in NOT_LAUNCHED else
                                             "LAUNCHING: only part of this family is live (confirmed Oct 14, 2026). Variations without a live price are not launched yet, not missing data."))
        b_.font = F(bold=True, color="C00000"); b_.fill = FILL["flag"]
    ws.cell(row=2, column=1, value="← Dashboard").hyperlink = f"#'{mkt} Dashboard'!A1"
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
        ("Parent ASIN (Amazon)", parent or "Not in catalog pull"), ("Best-selling child ASIN", best), ("Stage", our_stage(pid, mkt, p, o)),
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
        ("BFCM 2025 lift", f"{lf['lift']:.2f}x" if lf else "n/a", f"daily sales, BFCM wk vs 30 days before ({lf['src']})" if lf else "no data"),
        ("BFCM 2025 TACoS", f"{lf['tacos']:.1f}%" if lf and lf.get("tacos") is not None else "n/a", f"vs {lf['pre_tacos']:.1f}% before" if lf and lf.get("pre_tacos") is not None else ""),
        ("Dec 2025 vs pre-event", f"{lf['dec']:.2f}x" if lf and lf.get("dec") else "n/a", "December daily sales vs Oct 21-Nov 19"),
        ("Competitors mapped", str(len(comps)) if comps else ("0 (CA not mapped)" if mkt == "CA" else "0"), "Command Center map" if mkt == "US" else "Amazon.ca page research"),
        ("Priced below us", str(sum(1 for x in comps if isinstance(x.get("price"), (int, float)) and x.get("our_same") and x["price"] < x["our_same"])) if comps else "n/a", "same size, else vs our Queen"),
        (("List Price within 12%", str(sum(1 for x in comps if isinstance(x.get("lp"), (int, float)) and isinstance(x.get("price"), (int, float)) and 0 < x["lp"] / x["price"] - 1 <= 0.12)) if comps else "n/a", "List Price set, <=12% above price")
         if mkt == "US" else
         ("Strikethrough shown", (f"{sum(1 for x in comps if x.get('str_show') == 'Y')} of {len(comps)}") if comps else "n/a", "on the Amazon.ca page, Oct 13")),
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
                  split_txt=(split_note(pid, mkt, v) or (None, None))[1],
                  price_date=(str(v["price_date"])[:10] if v.get("price_date") else None))
        for j, (key, _h, _w) in enumerate(VC[1:], 2):
            c = ws.cell(row=r, column=j, value=vv.get(key)); c.font = F(); c.border = BOX; c.alignment = WRAP
            if key in VF:
                c.number_format = VF[key]
            if key in ("price", "price_date") and vv.get(key) is not None:
                c.font = F(color="808080")
            if key == "price_now" and vv.get(key) is not None:
                c.font = F(bold=True)
            if key == "status" and str(vv.get(key) or "").startswith(("Not buyable", "No Buy Box")):
                c.fill = FILL["flag"]; c.font = F(bold=True)
            if key == "split_txt" and vv.get(key):
                c.fill = FILL["flag"] if vv[key].startswith("SEPARATE") else FILL["calc"]; c.font = F(bold=vv[key].startswith("SEPARATE"))
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
    sb = sb_of(pid, mkt)
    if sb:
        r += 1
        hdr = ("Actual sales (SellerBoard)", "Sales", "Units", "Organic units", "Ad units", "Ad cost", "TACoS (actual)", "Sessions", "Unit session %", "Avg price", "Refunds")
        cols_ = [1, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14]
        for j, val in enumerate(hdr):
            c = ws.cell(row=r, column=cols_[j], value=val); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.border = BOX
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        r += 1
        for w, lab in (("pre", "Pre-event Oct 21 - Nov 19, 2025 (30d)"), ("bfcm", "BFCM week Nov 20 - Dec 1, 2025 (12d)"), ("dec", "December 2 - 31, 2025 (30d)")):
            x = sb.get(w)
            if not x:
                continue
            vals = (lab, x.get("sales"), x.get("units"), x.get("units_organic"), (x.get("units_ppc") or 0) + (x.get("units_sd") or 0),
                    abs(x["advertising"]) if x.get("advertising") is not None else None,
                    (abs(x["advertising"]) / x["sales"]) if x.get("advertising") is not None and x.get("sales") else None,
                    x.get("sessions"), (x["unit_session_pct"] / 100) if x.get("unit_session_pct") is not None else None,
                    x.get("avg_sales_price"), x.get("refunds"))
            fm = ["@", "$#,##0", "#,##0", "#,##0", "#,##0", "$#,##0", "0.0%", "#,##0", "0.0%", "$#,##0.00", "#,##0"]
            for j, val in enumerate(vals):
                c = ws.cell(row=r, column=cols_[j], value=val); c.font = F(); c.border = BOX; c.number_format = fm[j]
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
            r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        ws.cell(row=r, column=1, value=(f"SellerBoard, Ecotero account, Amazon parent {amazon_parent(pid, mkt)} plus any of this product's child ASINs SellerBoard lists on their own, UTC days. Lift above uses these actual sales"
                                        + (f" ({lf['lift']:.2f}x; the ad-spend estimate was {lf['lift_derived']:.2f}x)." if lf and lf.get('lift_derived') else ".")
                                        + (" Amazon.ca sales here are in USD: SellerBoard converts to the account currency, while the Command Center table above is in CAD (ratio ~0.71). Lift is a ratio, so it is unaffected." if mkt == "CA" else ""))).font = F(size=8, italic=True, color=C_SUB)
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
    p26 = plan26_text(pid, mkt)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
    c = ws.cell(row=r, column=1, value=("BFCM 2026 plan (BM, Oct 15, 2026): " + p26 + ". Deal price and depth not yet given; not yet visible in Amazon's deal feed.")
                if p26 else "BFCM 2026 plan (BM, Oct 15, 2026): NOT IN A DEAL. BM confirmed that products without a planned deal are not in any BFCM 2026 deal; they sell at their regular price.")
    c.font = F(size=8.5, bold=True, color=("1F4E79" if p26 else "C00000")); c.alignment = WRAP
    ws.row_dimensions[r].height = 18
    r += 1
    for sd_ in slack_deal.get((pid, mkt)) or []:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        c = ws.cell(row=r, column=1, value=f"{sd_['topic']} (Slack): {sd_['detail']} [{sd_['source']}]")
        c.font = F(size=8.5, color="1F4E79"); c.alignment = WRAP
        ws.row_dimensions[r].height = 30 if len(c.value) > 180 else 18
        r += 1
    so_ = stock_outlook(pid, mkt)
    if so_["rows"]:
        c_ = so_["counts"]
        txt_ = (f"BFCM 2026 stock (SellerBoard, Oct 15): {so_['on_hand']:,.0f} units at Amazon + {so_['inbound']:,.0f} already sent (no ETA in SellerBoard); "
                f"selling {so_['vel']:,.1f} a day; need about {so_['need']:,.0f} to Nov 30 with a {so_['lift']:.2f}x BFCM lift ({so_['lift_src']}). "
                f"Variations: {c_.get('Covered to Nov 30', 0)} covered, {c_.get('Needs inbound in time', 0)} need the inbound in time, "
                f"{c_.get('Short even with inbound', 0)} short even with inbound ({so_['short']:,.0f} units), {c_.get('Out of stock now', 0)} out of stock now. Detail: BFCM Stock tab.")
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        c = ws.cell(row=r, column=1, value=txt_)
        c.font = F(size=8.5, bold=True, color=("C00000" if (c_.get("Short even with inbound") or c_.get("Out of stock now")) else "1F4E79")); c.alignment = WRAP
        ws.row_dimensions[r].height = 30
        r += 1
    da = deal_assumption(pid, mkt)
    if da:
        cur_ = "C$" if mkt == "CA" else "$"
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        c = ws.cell(row=r, column=1, value=(f"ASSUMED 2026 deal prices, until BM's final: {da['asin']} today {cur_}{da['ref']:,.2f}; {cur_}{da['deal_std']:,.2f} at {da['std']:.0%} off ({RULE26['std_days']}) and {cur_}{da['deal_peak']:,.2f} at {da['peak']:.0%} off ({RULE26['peak_days']}). "
                                            f"Rule: {RULE26['src']}. Evidence: {deal_evidence_text(da) or 'no 2025 history'}. Amazon may use a lower reference price than today's (it sets it the day before the deal), which would lower the deal price."
                                            if da.get("ref") else f"ASSUMED 2026 discount, until BM's final: {da['std']:.0%} / {da['peak']:.0%} ({RULE26['src']}); no live price for the hero ASIN."))
        c.font = F(size=8.5, italic=True, color="7F6000"); c.alignment = WRAP
        ws.row_dimensions[r].height = 18
        r += 1
    hk = hero25.get((pid, mkt))
    if hk and (hk["pre"] or hk["rank_pre"]):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        bits = []
        if hk["pre"] and hk["bf"]:
            bits.append(f"price ${hk['pre']:,.2f} before (median Nov 1-19) → ${hk['bf']:,.2f} in BFCM week (median Nov 20 - Dec 1), "
                        + (f"{1 - hk['bf'] / hk['pre']:.0%} lower" if hk["bf"] < hk["pre"] else "no cut") + f"; lowest ${hk['low']:,.2f}")
        if hk["rank_pre"] and hk["rank_bf"]:
            lr = hk["rank_pre"] / hk["rank_bf"]
            bits.append(f"Best Seller Rank {hk['rank_pre']:,} → {hk['rank_bf']:,} (" + (f"{lr:.2f}x better" if lr >= 1 else f"{1 / lr:.2f}x worse") + ")")
        if hk["ped"]:
            bits.append(f"Prime Exclusive price seen {hk['ped']}")
        if hk["coupons"]:
            bits.append(f"coupon {hk['coupons']}")
        txt = (f"Our hero child {hk['asin']} in Keepa (Command Center, US): " + "; ".join(bits)
               + ". Price is Keepa's lowest new offer (Keepa holds no Buy Box series for our own ASINs; we are the only seller).")
        c = ws.cell(row=r, column=1, value=txt); c.font = F(size=8.5, bold=True, color=C_INK); c.alignment = WRAP
        ws.row_dimensions[r].height = 30
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
               + (f". Most important: {so['top']}." if so['top'] else "."))
        sg = stock_gap.get((pid, mkt))
        if sg:
            n_ = sum(v for k, v in sg.items() if not k.startswith("_"))
            txt += (f" Days with no snapshot ({'Nov 26-27 and Dec 1, Cyber Monday' if mkt == 'US' else 'Nov 24, 29 and 30'}), inferred from sales that day and the readings either side: "
                    f"{sg.get('in_stock', 0)} of {n_} variation-days in stock, {sg.get('out_of_stock', 0)} out of stock, {sg.get('unknown', 0)} unknown"
                    + (f"; {sg['sold_despite_zero_snapshots']} sold despite 0 units on both sides (stock arriving that day): {', '.join(sg['_sold0'])}" if sg.get("sold_despite_zero_snapshots") else "")
                    + ". Inferred, not a stock reading.")
        else:
            txt += f" Snapshots missing: {'US Nov 26-27 and Dec 1 (Cyber Monday)' if mkt == 'US' else 'CA Nov 24, 29-30'}."
        c = ws.cell(row=r, column=1, value=txt); c.font = F(size=8.5, bold=True, color=C_INK); c.alignment = WRAP
        ws.row_dimensions[r].height = 26 if len(txt) < 330 else 40
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
    if mkt == "CA" and not comps:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        ws.cell(row=r, column=1, value="The Command Center holds no Amazon.ca competitor snapshots. Map the CA competitor set (Data Gaps #6) and pull Keepa .ca - see AGENT_PROMPTS Prompt 9.").font = F(bold=True, color="C00000")
        r += 2
        product_cells[(pid, mkt)] = {"tab": tname}
        continue
    if mkt == "CA":
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NC)
        ws.cell(row=r, column=1, value=("Canadian competitors from Amazon.ca page research (Oct 13, logged out, Toronto M5V 3L9): page-1 organic results for this product's keywords, "
                                        "same material and piece count, Queen size selected (2 King where no Queen). Prices in CAD. The Command Center columns (BSR trend, ASINsight search strategy, "
                                        "weekly units) do not exist for Canada; organic rank and keyword are in Notes. 'Our price, same size' is our live Amazon.ca price "
                                        "(Helium 10 Xray, CAD) where held, else the Command Center CAD price marked STALE.")).font = F(size=8.5, bold=True, color=C_INK)
        ws.cell(row=r, column=1).alignment = WRAP
        ws.row_dimensions[r].height = 30
        r += 1
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
            c.border = BOX; c.font = F(); c.alignment = WRAP if key in ("title", "hero", "top_kw", "basis", "cls_why") else Alignment(vertical="top")
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
        if "cls" in CK and x.get("cls"):
            ws.cell(row=r, column=CK["cls"]).fill = PatternFill("solid", fgColor={"Direct": "C6EFCE", "Alternative material": "DDEBF7", "Material not verified": "FFEB9C", "Different product type": "EDEDED"}.get(x["cls"], "FFFFFF"))
            ws.cell(row=r, column=CK["cls"]).font = F(bold=(x["cls"] == "Direct"))
        for key in ("parent", "child"):   # clickable product page on the competitor's own marketplace
            if vals.get(key):
                c = ws.cell(row=r, column=CK[key])
                c.hyperlink = f"https://www.amazon.{'ca' if x['mkt'] == 'CA' else 'com'}/dp/{vals[key]}"
                c.font = F(color="0563C1", underline="single")
        if x.get("price_cc") is not None:
            ws.cell(row=r, column=CK["price"]).comment = Comment(f"{x.get('price_src')}. The Command Center snapshot ({(x.get('seen') or '')[:10]}) has ${x['price_cc']:,.2f}.", "Tracker")
        for key, old in (("parent", "parent_cc"), ("brand", "brand_cc")):
            if x.get(old):
                ws.cell(row=r, column=CK[key]).comment = Comment(f"Amazon page, Oct 14, 2026. The Command Center still lists {x[old]}.", "Tracker")
        P, LPc = f"{CLt['price']}{r}", f"{CLt['lp']}{r}"
        ws[f"{CLt['lp_pct']}{r}"] = f'=IF(AND(ISNUMBER({LPc}),ISNUMBER({P}),N({P})>0),{LPc}/{P}-1,"")'
        q = f"{CLt['lp_pct']}{r}"
        ws[f"{CLt['band']}{r}"] = f'=IF({q}="","No List Price",IF({q}<=0,"At/below price",IF({q}<=0.12,"<=12% STR zone",IF({q}<=0.25,"12-25%",">25% over"))))'
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
    if comps and mkt == "US":
        ins.append(f"Strikethrough: {sum(1 for x in comps if isinstance(x.get('lp'), (int, float)) and isinstance(x.get('price'), (int, float)) and x['lp'] > x['price'])} of {len(comps)} rivals set a List Price above price; {len(z)} within 12%"
                   + (": " + ", ".join(f"{x['brand']} +{x['lp']/x['price']-1:.0%}" for x in z[:6]) if z else "") + ".")
    if comps:
        below = [x for x in comps if isinstance(x.get("price"), (int, float)) and x.get("our_same") and x["price"] < x["our_same"]]
        ins.append(f"Price: {len(below)} of {len(comps)} rivals sit below our price today (same size where the title states one). Cheapest strong rivals: "
                   + ", ".join(f"{x['brand']} {fmt(x['price'])}" for x in sorted([b for b in below if b['tier'] in ('Aspirational', 'Beatable') or mkt == 'CA'], key=lambda b: b['price'])[:4]) + "."
                   + (" CA prices are CAD; ours is the live Amazon.ca price (Helium 10 Xray) where held." if mkt == "CA" else ""))
    if comps and mkt == "CA":
        top_ = sorted(comps, key=lambda x: int(x.get("ca_rank") or 999))[:5]
        ins.append("Top organic on Amazon.ca (Oct 13): " + "; ".join(f"#{x['ca_rank']} {x['brand']} {fmt(x['price'])} ({x['ca_keyword']})" for x in top_) + ".")
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
            ins.append(f"BFCM 2025, {len(kc)} rivals with Keepa history: " + ", ".join(f"{k} {v}" for k, v in tc.most_common())
                       + (f". Median depth vs their Nov 1-19 price {statistics.median(ds):.0%}" if ds else "")
                       + (f"; median BSR lift {statistics.median(ls):.2f}x" if ls else "")
                       + (f". {rz} raised their Buy Box in BFCM week, so their deal looked deeper than it was." if rz else "."))
        nk = sum(1 for x in comps if x.get("bf_type") is None)
        if nk:
            ins.append(f"{nk} rival{'s' if nk != 1 else ''} not in the Keepa pulls yet (yellow BFCM 2025 columns) - remaining P2 batches, AGENT_PROMPTS Prompt 2.")
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
         "Search traffic", "Organic share", "We win", "We lose", "KWs they advertise we don't", "PD26 vis lift", "Tab", "BFCM25 discount", "BFCM25 BSR lift", "Size", "Colour",
         "match CA", "seq CA", "Competitor type", "Why this type"]
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
            ref("bf_disc"), ref("bsr_lift"), x.get("size"), x.get("colour"), None, None, x.get("cls"), x.get("cls_why")]
    for j, v in enumerate(vals, 1):
        dsh.cell(row=rr, column=j, value=v).font = F(size=8)
    dsh[f"P{rr}"] = f'=IF(AND(ISNUMBER(O{rr}),ISNUMBER(N{rr}),N(N{rr})>0),O{rr}/N{rr}-1,"")'
    dsh[f"R{rr}"] = f'=IF(AND(ISNUMBER(N{rr}),ISNUMBER(Q{rr}),N(Q{rr})>0),N{rr}/Q{rr}-1,"")'
    # filter match against the Dashboard selectors (C4 product, C5 marketplace, C6 brand, C7 tier, C8 family)
    for mk_, sh_, mc_, sc_ in (("US", "US Dashboard", "A", "B"), ("CA", "CA Dashboard", "AH", "AI")):
        dsh[f"{mc_}{rr}"] = (f"=AND(E{rr}=\"{mk_}\",OR('{sh_}'!$C$4=\"All\",'{sh_}'!$C$4=D{rr}),OR('{sh_}'!$C$5=\"All\",'{sh_}'!$C$5=G{rr}),"
                             f"OR('{sh_}'!$C$6=\"All\",'{sh_}'!$C$6=H{rr}),OR('{sh_}'!$C$7=\"All\",'{sh_}'!$C$7=F{rr}),OR('{sh_}'!$C$8=\"All\",'{sh_}'!$C$8=AJ{rr}))")
        dsh[f"{sc_}{rr}"] = f"=IF({mc_}{rr},{(sc_ + str(rr - 1)) if rr > DR0 else '0'}+1,{(sc_ + str(rr - 1)) if rr > DR0 else '0'})"
DR1 = DR0 + len(records) - 1
dsh.freeze_panes = "C2"
dsh.sheet_properties.tabColor = "BFBFBF"

# lists for dropdowns (per marketplace)
lst = wb.create_sheet("Lists")
lst.sheet_state = "hidden"
brands = ["All"] + sorted({x["brand"] for x in records if x["brand"]}, key=str.lower)
LISTS = (("Products_US", ["All"] + [PINFO[p][2] for p, m, t in TABS if m == "US"]), ("Products_CA", ["All"] + [PINFO[p][2] for p, m, t in TABS if m == "CA"]),
         ("Brands", brands), ("Tiers", ["All", "Aspirational", "Beatable", "Poor", "Untiered"]), ("Families", ["All", "Bamboo", "Satin", "Silk", "Cooling", "Other"]),
         ("Types", ["All", "Direct", "Alternative material", "Material not verified", "Different product type", "Not classified"]))
for j, (name, vals) in enumerate(LISTS, 1):
    for i, v in enumerate(vals, 1):
        lst.cell(row=i, column=j, value=v)
    wb.defined_names[name] = DefinedName(name, attr_text=f"Lists!${CL(j)}$1:${CL(j)}${len(vals)}")

# product lookup (hidden): one row per marketplace and product, read by the dashboards
lk = wb.create_sheet("Lookup")
lk.sheet_state = "hidden"
LKC = ["key", "Product", "Tab", "Title", "Image URL", "Brand", "Parent ASIN", "Best-selling child", "Variations", "Our price (best child)", "Units, last 28 days",
       "BFCM 2025 sales lift", "BFCM 2026 plan", "Assumed deal Nov 19-26", "Assumed deal Nov 27-30", "Stock at Amazon", "Inbound", "Units needed to Nov 30",
       "Short even with inbound", "Variations covered", "Variations needing inbound", "Variations short", "Variations out of stock", "Contribution per unit", "Break-even ACoS"]
for j, h in enumerate(LKC, 1):
    lk.cell(row=1, column=j, value=h).font = F(bold=True)
lr = 2
for pid, mkt, tname in TABS:
    p, o = our_profile(pid, mkt)
    title, img, best, parent = our_title_and_image(pid, mkt)
    lf = lift_of(pid, mkt)
    e = econ(o.get("economics"))
    da = deal_assumption(pid, mkt)
    so_ = stock_outlook(pid, mkt)
    c_ = so_["counts"]
    vals = [f"{mkt}|{PINFO[pid][2]}", PINFO[pid][2], tname, title or f"{o.get('brand')} {o.get('name')}", good_img(img), p.get("brand") or o.get("brand"), parent, best,
            len(our_variations(pid, mkt)), our_headline_price(pid, mkt, best, e["price"])[0], e["units_28d"], lf["lift"] if lf else None,
            plan26_text(pid, mkt) or "Not in a deal", (da or {}).get("deal_std"), (da or {}).get("deal_peak"),
            so_["on_hand"] if so_["rows"] else None, so_["inbound"] if so_["rows"] else None, so_["need"] if so_["rows"] else None, so_["short"] if so_["rows"] else None,
            c_.get("Covered to Nov 30", 0), c_.get("Needs inbound in time", 0), c_.get("Short even with inbound", 0), c_.get("Out of stock now", 0),
            e["contribution"], e["be_acos"]]
    for j, v in enumerate(vals, 1):
        lk.cell(row=lr, column=j, value=v)
    lr += 1
LK_RANGE, LK_KEYS = f"Lookup!$A$2:${CL(len(LKC))}${lr - 1}", f"Lookup!$A$2:$A${lr - 1}"

def build_dashboard(mkt, sname, mcol, scol, pos):
    """One dashboard per marketplace: product dropdown + our product panel + competitor gallery for that marketplace."""
    cur = "C$" if mkt == "CA" else "$"
    money = f'"{cur}"#,##0.00'
    db = wb.create_sheet(sname, pos)
    db.sheet_view.showGridLines = False
    db.sheet_view.zoomScale = 90
    db.sheet_properties.tabColor = "1F4E79" if mkt == "US" else "C00000"
    W = [2, 13, 18, 34, 10, 9, 9, 8, 9, 9, 8, 7, 8, 9, 8, 8, 9, 14]
    for i, w in enumerate(W, 1):
        db.column_dimensions[CL(i)].width = w
    db.merge_cells("B1:R1")
    c = db["B1"]; c.value = f"BFCM 2026 Tracker · {'Amazon.com (US)' if mkt == 'US' else 'Amazon.ca (Canada)'}"; c.font = F(size=18, bold=True, color="FFFFFF")
    c.fill = HDR; c.alignment = Alignment(vertical="center", indent=1)
    db.row_dimensions[1].height = 34
    db.merge_cells("B2:R2")
    db["B2"] = "Pick a product in the yellow cell. Competitor type (Direct = same product and material as ours), brand, tier and family narrow the competitor list. Everything below updates instantly."
    db["B2"].font = F(italic=True, color=C_SUB)
    for i, (lab, name) in enumerate((("Product", f"Products_{mkt}"), ("Brand", "Brands"), ("Tier", "Tiers"), ("Family", "Families"), ("Competitor type", "Types")), 4):
        a = db.cell(row=i, column=2, value=lab); a.font = F(bold=True, color=C_SUB)
        b = db.cell(row=i, column=3, value="DC B4" if lab == "Product" else "All")
        b.fill = INPUT; b.font = F(bold=True, size=10, color=BLUE); b.border = BOX
        dv = DataValidation(type="list", formula1=f"={name}", allow_blank=False); db.add_data_validation(dv); dv.add(b.coordinate)
    other = "CA Dashboard" if mkt == "US" else "US Dashboard"
    db["B9"] = f"→ {other}"; db["B9"].hyperlink = f"#'{other}'!A1"; db["B9"].font = F(color="0563C1", underline="single", size=9)
    db["B10"] = "→ BFCM Stock"; db["B10"].hyperlink = "#'BFCM Stock'!A1"; db["B10"].font = F(color="0563C1", underline="single", size=9)
    def lk_(col):
        return f'IFERROR(INDEX({LK_RANGE},MATCH("{mkt}|"&$C$4,{LK_KEYS},0),{col}),"")'
    db.merge_cells("E4:E10")
    db["E4"] = (f'=IF($C$4="All","",{lk_(5)})' if NO_IMAGE_FORMULA else f'=IF($C$4="All","",IFERROR(_xlfn.IMAGE({lk_(5)}),"IMAGE COMING SOON"))')
    db["E4"].alignment = CENTER; db["E4"].border = BOX
    facts = (("Our product", 4, None), ("Brand · parent ASIN", None, None), ("Our price (best child)", 10, money), ("Units, last 28 days", 11, "#,##0"),
             ("BFCM 2026 plan", 13, None), ("Assumed deal price (15% / 20%)", None, None), ("BFCM 2025 sales lift", 12, '0.00"x"'))
    for i, (lab, col, nf) in enumerate(facts, 4):
        a = db.cell(row=i, column=6, value=lab); a.font = F(bold=True, color=C_SUB, size=8)
        db.merge_cells(start_row=i, start_column=7, end_row=i, end_column=11)
        if lab == "Brand · parent ASIN":
            fx = f'=IF($C$4="All","",{lk_(6)}&" · "&{lk_(7)})'
        elif lab.startswith("Assumed deal"):
            fx = f'=IF(OR($C$4="All",{lk_(14)}=""),"No deal planned",TEXT({lk_(14)},"{cur}0.00")&" (Nov 19-26) · "&TEXT({lk_(15)},"{cur}0.00")&" (Nov 27-30)")'
        else:
            fx = f'=IF($C$4="All","All products",{lk_(col)})' if col == 4 else f'=IF($C$4="All","",{lk_(col)})'
        b = db.cell(row=i, column=7, value=fx); b.font = F(bold=(lab == "Our product"), size=9); b.alignment = Alignment(wrap_text=True, vertical="center")
        if nf:
            b.number_format = nf
        db.row_dimensions[i].height = 22
    db.row_dimensions[4].height = 30
    db.cell(row=11, column=6, value="Open the product tab:").font = F(bold=True, color=C_SUB, size=8)
    db.merge_cells("G11:K11")
    db["G11"] = f'=IF($C$4="All","",HYPERLINK("#\'"&{lk_(3)}&"\'!A1",{lk_(3)}))'
    db["G11"].font = F(color="0563C1", underline="single")
    # stock tiles + competitor tiles
    rng = lambda col: f"Data!${col}${DR0}:${col}${DR1}"
    tiles = [("Stock at Amazon", f'=IF($C$4="All","",{lk_(16)})', "#,##0"), ("Inbound", f'=IF($C$4="All","",{lk_(17)})', "#,##0"),
             ("Units needed to Nov 30", f'=IF($C$4="All","",{lk_(18)})', "#,##0"),
             ("Variations short / out of stock", f'=IF($C$4="All","",{lk_(22)}&" / "&{lk_(23)})', "General"),
             ("Competitors shown", f"=COUNTIF({rng(mcol)},TRUE)", "#,##0"),
             ("Median competitor price", f'=IFERROR(MEDIAN(IF(({rng(mcol)}=TRUE)*ISNUMBER({rng("N")}),{rng("N")})),"")', money),
             ("Priced below us", f'=COUNTIFS({rng(mcol)},TRUE,{rng("R")},"<0")', "#,##0"),
             ("Avg BFCM 2025 discount", f'=IFERROR(AVERAGEIFS({rng("AD")},{rng(mcol)},TRUE),"")', "0.0%")]
    for i, (lab, fx, nf) in enumerate(tiles):
        col = 12 + (i % 4) * 2
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
    GR = 14
    stile = None
    db.merge_cells(f"B{GR - 1}:R{GR - 1}")
    db[f"B{GR - 1}"] = "COMPETITORS (first 80 matches, in tier then weekly-units order)"
    db[f"B{GR - 1}"].font = F(size=11, bold=True, color=C_NAVY); db[f"B{GR - 1}"].fill = SEC
    GH = [("#", 1, None), ("Image", 10, None), ("Brand · Tier", 7, None), ("Title", 9, None), ("Competitor type", 36, None), ("Size · colour", None, None), ("Price", 14, money),
          ("List Price", 15, money), ("List % over", 16, "0%"), ("vs our price", 18, "+0%;-0%;0%"), ("BSR", 19, "#,##0"), ("Wk units", 20, "#,##0"),
          ("Rating", 21, "0.0"), ("Reviews", 22, "#,##0"), ("Variations", 13, "#,##0"), ("BFCM 2025 discount", 30, "0%"), ("ASIN", 12, None)]
    for j, (h, src, nf) in enumerate(GH, 2):
        c = db.cell(row=GR, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CENTER; c.border = BOX
    for k in range(1, 81):
        rr = GR + k
        db.row_dimensions[rr].height = IMG_ROW_H
        m = f"MATCH({k},Data!${scol}${DR0}:${scol}${DR1},0)"
        def gv(col):
            x_ = f"INDEX(Data!${CL(col)}${DR0}:${CL(col)}${DR1},{m})"
            return f'IFERROR(IF({x_}="","",{x_}),"")'
        for j, (h, src, nf) in enumerate(GH, 2):
            c = db.cell(row=rr, column=j); c.border = BOX; c.font = F(size=8); c.alignment = WRAP
            if h == "#":
                c.value = f'=IF({k}<=COUNTIF({rng(mcol)},TRUE),{k},"")'
            elif h == "Image":
                c.alignment = CENTER
                c.value = (f'=IF(B{rr}="","",{gv(10)})' if NO_IMAGE_FORMULA else f'=IF(B{rr}="","",IFERROR(_xlfn.IMAGE({gv(10)}),"IMAGE COMING SOON"))')
            elif h == "Brand · Tier":
                c.value = f'=IF(B{rr}="","",{gv(7)}&CHAR(10)&{gv(8)})'
                c.font = F(size=8, bold=True)
            elif h == "Size · colour":
                c.value = f'=IF(B{rr}="","",TRIM({gv(32)}&" "&{gv(33)}))'
            else:
                c.value = f'=IF(B{rr}="","",{gv(src)})'
            if nf:
                c.number_format = nf
    db.column_dimensions["E"].width = 34
    db.conditional_formatting.add(f"K{GR + 1}:K{GR + 80}", FormulaRule(formula=[f'AND(ISNUMBER(K{GR + 1}),K{GR + 1}<0)'], fill=FILL["flag"]))
    db.conditional_formatting.add(f"J{GR + 1}:J{GR + 80}", FormulaRule(formula=[f'AND(ISNUMBER(J{GR + 1}),J{GR + 1}>0,J{GR + 1}<=0.12)'], fill=FILL["ok"]))
    for t_, col_ in (("Direct", "C6EFCE"), ("Alternative material", "DDEBF7"), ("Material not verified", "FFEB9C"), ("Different product type", "EDEDED")):
        db.conditional_formatting.add(f"F{GR + 1}:F{GR + 80}", FormulaRule(formula=[f'F{GR + 1}="{t_}"'], fill=PatternFill("solid", fgColor=col_)))
    db.freeze_panes = f"A{GR + 1}"
    return db

build_dashboard("US", "US Dashboard", "A", "B", 1)
build_dashboard("CA", "CA Dashboard", "AH", "AI", 2)

# ================================================================== Product Index
pi = wb.create_sheet("Product Index", 2)
pi.sheet_view.showGridLines = False
PIH = [("Image", 11), ("Product tab", 18), ("Family", 8), ("Brand", 10), ("Title", 40), ("Mkt", 5), ("Parent ASIN (Amazon)", 11), ("Variations", 8), ("Sizes", 14),
       ("Colours", 8), ("Our price ($)", 9), ("Our price: source, date", 14), ("Units 28d", 8), ("Competitors mapped", 9), ("BFCM 2025 lift", 8), ("BFCM 2025 TACoS", 8), ("BFCM role", 20), ("Scope", 14)]
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
            len([x for x in records if x["pid"] == pid and x["mkt"] == mkt]), lf["lift"] if lf else None, (lf["tacos"] / 100) if lf and lf.get("tacos") is not None else None, PINFO[pid][3], scope_of(pid)]
    for j, v in enumerate(vals[1:], 2):
        c = pi.cell(row=rr, column=j, value=v); c.font = F(); c.border = BOX; c.alignment = WRAP
    pi.cell(row=rr, column=2).hyperlink = f"#'{tname}'!A1"; pi.cell(row=rr, column=2).font = F(color="0563C1", underline="single")
    pi.cell(row=rr, column=11).number_format = "$#,##0.00"; pi.cell(row=rr, column=15).number_format = '0.00"x"'; pi.cell(row=rr, column=16).number_format = "0.0%"
    if "STALE" in str(pi.cell(row=rr, column=12).value) and pid not in NOT_LAUNCHED:
        pi.cell(row=rr, column=12).fill = PatternFill("solid", fgColor="F8CBAD")
    pi.cell(row=rr, column=18).fill = PatternFill("solid", fgColor={"Core": "C6EFCE", "Not launched": "D9D9D9", "Launching (partly live)": "FFEB9C"}.get(scope_of(pid), "FFFFFF"))
    rr += 1
pi.freeze_panes = "C2"

# ================================================================== README
lines = [
    ("BFCM 2026 Competitor Research", dict(bold=True, size=16)),
    ("Owner: Shayan Rana · Backup: Zarlish · Final for Thu Oct 15, 2026 · Data as of Oct 13-15, 2026", dict(italic=True)),
    ("", None),
    ("How to use it", dict(bold=True, size=11)),
    ("1. US Dashboard and CA Dashboard - pick a product in the yellow cell (brand, tier and family narrow the competitors). Our product panel, stock tiles, competitor tiles and the competitor gallery update. 'Open the product tab' jumps to the full analysis.", {}),
    ("2. Product Index - every product in both marketplaces with its image, variations and BFCM 2025 result; click a tab name to open it.", {}),
    ("3. BFCM Stock - every variation: stock at Amazon, inbound, sales a day, units needed to Nov 30, run-out date with and without inbound, and status. Filter by product or status.", {}),
    (f"4. Product tabs - US tabs (blue) then CA tabs (orange), {len(TABS)} in all. Each has: 1 Our product (plan, assumed deal prices, stock outlook, deal pricing notes) · 2 Our variations · 3 Our BFCM 2025 result · 4 Competitor landscape.", {}),
    ("5. Data Check - the as-of date, coverage and verification result of every data set; Data Gaps - what is still missing.", {}),
    ("", None),
    ("Key rules", dict(bold=True, size=11)),
    ("Our price = the latest catalog price read (US Oct 13, CA Oct 14); a variation without one shows no price.", {}),
    ("Assumed BFCM 2026 deal price, until final prices are set: 15% off today's price on Nov 19-26 and 20% off on Nov 27-30 (Black Friday to Cyber Monday). Amazon sets the reference price the day before the deal and can use a lower reference, which would lower the deal price.", {}),
    ("BFCM 2026 stock: demand at today's pace to Nov 18, then x the product's BFCM 2025 lift for Nov 19-30 (the account's lift where the product's own is missing or unreliable, labelled ASSUMED). Inbound has no arrival date, so each variation shows its run-out date with and without inbound.", {}),
    ("BFCM 2025 = Nov 20 - Dec 1, 2025; pre-event = Nov 1-19 for prices and Oct 21 - Nov 19 for sales.", {}),
    ("A COMING SOON picture means no verified photo yet - it is never replaced by another product's photo. Images render in Excel 365 and Google Sheets.", {}),
    ("Estimated weekly units and sales bands for competitors are estimates - use them to rank competitors, not as exact sales.", {}),
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
    row = row[:2]
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
    w.writerow(["marketplace", "product_tab", "scope", "sku", "child_asin", "size", "colour", "units_28d", "command_center_price", "command_center_price_date", "live_price_held"])
    for pid, mkt, tname in sorted(TABS, key=lambda t: (scope_of(t[0]) != "Core", t[1] != "US")):
        if pid in NOT_LAUNCHED:
            continue
        for v in our_variations(pid, mkt):
            if v.get("asin") and v.get("sku"):
                w.writerow([mkt, tname, scope_of(pid), v["sku"], v["asin"], v["size"], v["colour"], v["units_28d"], v["price"],
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
all_vars = [(pid, mkt, v) for pid, mkt, _t in TABS if pid not in NOT_LAUNCHED for v in our_variations(pid, mkt)]
def _cov(sel):
    xs = [v for pid_, mk_, v in all_vars if sel(pid_, mk_)]
    return sum(1 for v in xs if v.get("price_now") is not None), len(xs)
core_us, core_ca = _cov(lambda p_, m_: p_ in CORE and m_ == "US"), _cov(lambda p_, m_: p_ in CORE and m_ == "CA")
core_gap = {}
for pid_, mk_, v in all_vars:
    if pid_ in CORE and mk_ == "US" and v.get("price_now") is None:
        core_gap[PINFO[pid_][2]] = core_gap.get(PINFO[pid_][2], 0) + 1
live_vars = sum(1 for *_x, v in all_vars if v.get("price_now") is not None)
live_cmp = sum(1 for x in US_recs if x.get("our_live"))
str_rows = len({x["child"] for x in records if x.get("str_checked")})
S = [("Data", "Source", "As of", "Rows", "Status", "", "Notes"),
     ("Competitor price, List Price, BSR, rating, reviews", "Command Center", latest_seen, sum(v for k, v in seen_cnt.items() if k == latest_seen), "Current",
      "", f"{old_seen} US rows are older (Jul 20 - Sep 21, 2026) and are shaded orange in the 'Snapshot date' column. Price is for the one tracked child ASIN; Amazon search may show another size of the same listing."),
     ("Strikethrough now (shown / label / price)", "Amazon page check", "2026-10-13", str_rows, "Current", "", f"{str_rows} competitor ASINs checked on the Amazon page Oct 13 (70 P1 at 12:10 ET, 240 P2 at 23:35 ET; logged out, ZIP 10001). Blank = redirect or not shown, never assumed. Redirects left blank, not substituted: B0D1RBXBNG (David's Home) now opens B0DBHFTF8W, a different variation (3-pc Twin vs 4-pc Twin) of the same family; B0CP3NX181, B0DG2HRZKK, B09G8P3X6L, B0D4PKVNWB."),
     ("Our price now", "Helium 10 Xray US (Oct 13) and Amazon.ca (Oct 14) / SellerBoard listing price (US gap-fill) / Data Dive / Amazon page check", "2026-10-13 to 14", core_us[0] + core_ca[0], "Partial", "",
      f"Core products: US {core_us[0]} of {core_us[1]} variations live, Canada {core_ca[0]} of {core_ca[1]}. Core US still without a live price: "
      + (", ".join(f"{k} {v}" for k, v in sorted(core_gap.items(), key=lambda kv: -kv[1])) or "none")
      + ". Not-launched products (SL B4, SL Satin 6pc, SL Cooling 6pc, SL Bamboo Pillowcase) are excluded. Without a live price the tabs show the Command Center fee-feed price (Mar 2026), which is out of date. Xray matched every price already verified on the Amazon page. Canada: Helium 10 Xray of Amazon.ca (Oct 14, CAD). Prompt 12 (our_price_request.csv, live_price_held = N) fills the rest."),
     ("Our variations not buyable on Amazon", "Amazon.ca page check (agent)", "2026-10-14", len(our_page_flag), "Check", "",
      f"Of 20 selling Canadian variations with no Xray price, {sum(1 for t in our_page_flag.values() if t.startswith('Not buyable'))} redirect to another size and {sum(1 for t in our_page_flag.values() if t.startswith('No Buy Box'))} show no Buy Box. "
      f"DataHub stock (Oct 14): {sum(1 for t in our_page_flag.values() if 'FBA stock 0' in t)} are out of FBA stock ({sum(1 for t in our_page_flag.values() if 'FBA stock 0' in t and 'nothing inbound' not in t)} with stock inbound, {sum(1 for t in our_page_flag.values() if 'nothing inbound' in t)} with nothing inbound); "
      f"{sum(1 for t in our_page_flag.values() if 'not a stock-out' in t)} have stock but no Buy Box (offer / listing issue - one page says 'Price higher than typical', i.e. Buy Box suppressed on price). Reason shown per variation in each Canada tab's Status column."),
     ("Our listings outside the main review family", "Helium 10 Xray", "2026-10-13", sum(1 for p_, m_, v in all_vars if (split_note(p_, m_, v) or ("",))[0] == "split"), "Check", "",
      "Variations with their own rating and review count instead of the product's main family, flagged in each tab's variation table: DC B4 Full Light Blue 3.9 / 61, DC S6 King White 4.0 / 28, DC Cooling Cal King Graphite 3.0 / 15, and CL Cooling launch variations not yet merged. "
      f"Reassigned: {len(REASSIGN)} 'SATIN-4PC-TWIN' SKUs moved from DC S4 to DC S6 (a Twin in the 6 Pc set is a 4-piece set; Amazon lists them in the Satin 6pc family). Their variations, units, deals and stock now count under DC S6; ad spend stays under DC S4 as the Command Center attributes it."),
     ("SKU reassignment vs Command Center", "Tracker rule (Shayan, Oct 14)", "2026-10-14", len(REASSIGN), "Fixed", "",
      f"DC S4 and DC S6 SKU counts and 28-day units differ from the Command Center by {len(REASSIGN)} SKUs / {sum((x.get('units28d') or 0) for x in (skus.get((31, 'US')) or {}).get('skus', []) if ('US', x.get('asin')) in REASSIGN)} units. Blended price and contribution are still the Command Center's (effect under 1%)."),
     ("Same-size price gap vs ours", "Calculated", "2026-10-13", live_cmp, "Partial", "",
      f"{live_cmp} of {len(US_recs)} US competitor rows compare against our live price; the rest are marked STALE in 'Comparison basis'."),
     ("Our contribution / break-even ACoS", "Command Center", "2026-03-30 prices", None, "Stale", "",
      "Calculated on the Mar 2026 fee-feed price. Where our live price is higher (e.g. B6 King +$10, B4 King +$15) contribution and break-even ACoS are understated."),
     ("Our parent ASIN", "Data Dive seller catalog", "2026-10-13", len(TABS), "Fixed", "",
      "Command Center's 'parent_asin' is one of our child ASINs. Tabs now show the Amazon parent from the catalog; the Command Center ASIN is listed separately."),
     ("Our BFCM 2025 ad spend, ad sales, ACoS, TACoS, orders", "Command Center", "2025-11-20 to 2025-12-01", None, "Exact", "", "Ad metrics as reported by the Command Center."),
     ("Our BFCM 2025 total sales and lift", "SellerBoard (Ecotero account), via connector", "Oct 21 - Dec 31, 2025", len(sellerboard), "Exact", "",
      "Actual sales, units (organic / PPC / SD), ad cost, sessions and refunds per Amazon parent for the 30 days before, BFCM week and December, US and CA. Every file sums exactly to SellerBoard's period totals; 99%+ of US sales map to a tracked product. Actual lifts match the Command Center estimates (B4 4.25x, B6 2.49x, S4 2.64x). Amazon.ca amounts are in USD (SellerBoard converts)."),
     ("Our BFCM 2025 deals", "DataHub promotions (agent, v2), checked against Command Center amazon_promotions / amazon_coupons", "2026-10-14", None, "Exact", "",
      "Re-verified Oct 14 against the Command Center deal feed: the same 31 US campaigns, dates and units (6 Best Deals ran Nov 20 - Dec 1: B4 4,890 units, S4 4,311, B6 2,927, Satin Fitted 1,865, SSS4 1,152, S6 1,008; 3 Best Deals and 22 Lightning Deals cancelled). The Command Center coupon feed has no US coupons Nov 1 - Dec 5. Scheduled deal price is not in either feed; the hero child's actual price during the deal comes from Keepa (next row). Prime Exclusive Discounts on SL Bamboo 6pc and SL Cooling Comforter are Keepa observations only."),
     ("How Amazon sets the BFCM deal price", "Slack: {src}".format(src=next(r_["source"] for r_ in slack_deal.get(("ALL", None), []) if r_["topic"] == "How Amazon sets the BFCM deal price")) if any(r_["topic"] == "How Amazon sets the BFCM deal price" for r_ in slack_deal.get(("ALL", None), [])) else "Slack", "2026-10-15", None, "Current", "",
      next((r_["detail"] for r_ in slack_deal.get(("ALL", None), []) if r_["topic"] == "How Amazon sets the BFCM deal price"), "")),
     ("STR (strikethrough) tests", "Slack: {src}".format(src=next(r_["source"] for r_ in slack_deal.get(("ALL", None), []) if r_["topic"] == "STR (strikethrough) tests")) if any(r_["topic"] == "STR (strikethrough) tests" for r_ in slack_deal.get(("ALL", None), [])) else "Slack", "2026-10-15", None, "Current", "",
      next((r_["detail"] for r_ in slack_deal.get(("ALL", None), []) if r_["topic"] == "STR (strikethrough) tests"), "")),
     ("Deal pricing and pre-BFCM decisions per product", "Slack threads of Umair Tahir (Oct 13-15); data/deals/slack_deal_pricing_2026-10-15.csv", "2026-10-15", sum(len(v) for k_, v in slack_deal.items() if k_[0] != "ALL"), "Current", "",
      "Shown on each product tab under the BFCM 2026 plan: Amazon's current reference and max deal price, and the decision on each pre-BFCM deal (B4 US and CA, B6, S4, Satin Fitted, Quilt, SL B6, S6, Silk Pillowcase, SL Cooling Fitted)."),
     ("BFCM 2026 stock outlook", "SellerBoard MCP, Ecotero account, read-only (data/stock/sellerboard_inventory_2026-10-15.csv, sellerboard_inbound_shipments_2026-10-15.csv)", "2026-10-15", len(sb_inv), "Partial", "",
      f"Inventory: every page pulled (Amazon.com 2,177 rows, Amazon.ca 836); totals match SellerBoard's own account summary (US 70,217 FBA stock, 22,893 sent to FBA; CA 10,238 and 8,062). 78 open FBA shipments listed by Amazon status; SellerBoard has NO ETA field, so arrival dates are not shown and the outlook is given with and without inbound. No purchase orders in SellerBoard. Demand uses SellerBoard's velocity, which runs about 1.5x the 28-day units on the big products (includes Prime Big Deal Days and late-September deals), so the 28-day pace is shown beside it. BFCM lift = product's own 2025 lift where reliable, else ASSUMED at the account lift (US {ACCT_LIFT['US']:.2f}x, CA {ACCT_LIFT['CA']:.2f}x)."),
     ("Stock outlook cross-check (inventory planner)", "", "2026-10-15", 44, "Exact", "",
      "44 key variations (each product's best seller plus the biggest risks) checked against the inventory planner's own forecast: sales pace matches on every row; where we see a run-out before Nov 18, the planner's date is within 3 days on 17 of 19 (the other 2 within 15 days); where we show 'covered', the planner's run-out date is after Nov 30 on all 15. Our dates are earlier when the run-out falls in BFCM week because we add the BFCM lift."),
     ("Competitor type: direct vs alternative material", "", "2026-10-15", len(records), "Current", "",
      f"Every competitor is classified against our product: Direct = same product type and same material family ({sum(1 for x in records if x.get('cls') == 'Direct')} rows); Alternative material = same product, different material ({sum(1 for x in records if x.get('cls') == 'Alternative material')}); Material not verified = no material on the page or in the title ({sum(1 for x in records if x.get('cls') == 'Material not verified')}); Different product type = e.g. fitted sheet only vs our set ({sum(1 for x in records if x.get('cls') == 'Different product type')}). Materials: competitor's product page where checked, else its title. Ours: CooLinens and Sleephoria cooling = synthetic nylon-spandex cooling knit (CooLinens confirmed 90% nylon / 10% spandex); Decolure Cooling = microfiber blend (a different material from Sleephoria); bamboo = viscose from bamboo; satin = polyester satin; silk = mulberry silk. Direct rivals lead every list."),
     ("CooLinens Cooling Sheets price", "", "2026-10-15", 5, "Current", "",
      "Launch prices confirmed live with the Buy Box on all 60 children on Oct 15, 2026 (the latest confirmed figure, replacing the earlier $79.99 Queen planning price): Twin $69.99, Full $74.99, Queen $87.99, King $93.99, Cal King $95.99. Same price for all 12 colours of a size; used for our price and every price comparison on this product."),
     ("Our prices", "Helium 10 Xray only (US Oct 13, CA Oct 14)", "2026-10-14", len(our_now), "Current", "",
      "Agreed Oct 15: Xray is the single source for our price. Amazon page check, Data Dive and SellerBoard listing prices are no longer shown as our price; a variation missing from Xray shows no price."),
     ("Our BFCM 2026 deal plan", "BM (Slack, Oct 15, 2026); data/deals/our_deals_bfcm2026_plan.csv", "2026-10-15", sum(len(v) for v in plan26.values()), "Partial", "",
      "US: 13 Best Deals Nov 19-30 (12 tracked products plus the Hanging Closet Organizer) and 3 Lightning Deals (S6 Nov 23 cancelled, trying for a Best Deal; Silk Pillowcase Nov 23; SL Cooling Fitted Nov 25). CA: 6 Best Deals Nov 19-30. Every tracked product not on this list is NOT in a deal (BM confirmed Oct 15), e.g. DC Cooling 4pc. The Hanging Closet Organizer is not a bedding product, so it stays outside this tracker. Deal price, depth, variations and committed units not given yet. Command Center amazon_promotions shows no Nov 15 - Dec 5, 2026 deals in either market yet."),
     ("Independent re-verification", "verify_tracker.py: recomputes from the raw files and compares with this workbook and the dashboard", "2026-10-15",
      (jl(f"{DATA}/verification_report.json", {}) or {}).get("total"), "Exact" if (jl(f"{DATA}/verification_report.json", {}) or {}).get("passed") == (jl(f"{DATA}/verification_report.json", {}) or {}).get("total") else "Check", "",
      "; ".join(f"{r_['name']}: {r_['checked']:,} checked, {r_['mismatches']} mismatches" for r_ in (jl(f"{DATA}/verification_report.json", {}) or {}).get("checks", []))),
     ("ASSUMED BFCM 2026 deal prices", "Tracker assumption (agreed Oct 15, 2026) until BM sends final prices", "2026-10-15", None, "Check", "",
      "Why an assumption: BFCM 2026 pricing is not finalized yet because of price fluctuations (Umair Tahir, Slack, Oct 15, 2026), and Amazon fixes the deal reference price the day before the event. Rule (Umair Tahir via Shayan Rana, Oct 15): 20% off on the high days and 15% off on the other deal days; high days taken as Black Friday to Cyber Monday, Nov 27-30, until confirmed. Base = today's live price of the hero ASIN (US) or best seller (CA). Evidence beside each product: our own BFCM 2025 cut on the hero (Keepa median price Nov 1-19 vs Nov 20 - Dec 1) and the US competitors' median cut. Amazon's reference can be lower than today's price (B4 King White: live $94.99, Amazon reference $79.99, Oct 16 Lightning Deal max $67.99, per Umair Tahir, Oct 15), which would push the deal price lower. Replace with BM's prices when they arrive."),
     ("Our heroes' BFCM 2025 price and Best Seller Rank (US)", "Command Center keepa_history (data/keepa/keepa_history_ours_cc.csv)", "Nov 1 - Dec 5, 2025", len(hero25), "Exact", "",
      f"Daily Keepa for our {len(hero25)} US hero child ASINs, pulled Oct 14. Keepa holds no Buy Box series for our own ASINs, so price = lowest new offer (we are the only seller). Price drops on Nov 20 match the Best Deals start: B4 $74.99 to $71.24, B6 $79.99 to $75.99, S4 $29.95 to $25.46, S6 $33.95 to $32.25, Satin Fitted $16.95 to $15.15, SSS4 $33.95 to $31.41. No price history for Bamboo Fitted, Decolure Cooling 4pc, CL Pillowcases, Linen Curtains and Quilt Set in this window."),
     ("Our BFCM 2025 stock", "DataHub inventory, revision 2 (agent) + data/stock/our_stock_bfcm2025_missing_dates_bracketed.csv", "2026-10-14", None, "Partial", "", "US Nov 26, 27, Dec 1 and CA Nov 24, 29, 30 have no snapshot. Filled by inference (data/stock/our_stock_bfcm2025_missing_dates_combined.csv) from units sold that day (agent, DataHub amazon_sales, 1,761 variation-days with a sale) and the readings either side: 3,503 of 3,936 variation-days in stock, 39 out of stock, 386 unknown (low or no stock either side and no sale), and 8 sold despite 0 units on both sides (inbound stock arriving that day, e.g. B4 Queen Mid Grey B0BZQ18QJB sold 87 on Cyber Monday). Stock unit columns stay blank for these days."),
     ("Competitor tier, X-Ray sales band, listing assets; newly mapped rivals", "Command Center Competitor Summary (competitors_roster, data/cc_roster)", "week of 2026-10-11", len(roster), "Current", "",
      f"All 27 US products pulled Oct 14 (661 product-competitor pairs). Tier now follows the Command Center's current grade. {roster_added} pairs mapped after the tracker's snapshot were added (B4, B6, CooLinens Cooling); Keepa BFCM 2025 history for the 6 new ASINs came from the Command Center (keepa_history_cc_added.csv). The Command Center list reads each rival's seed ASIN, often a different variation from the child tracked here, so its price, rank and reviews are shown beside the child figures, not in place of them."),
     ("Competitor price, newest", "Amazon page for the exact ASIN (agent, Oct 13 and 14)", "2026-10-14", sum(1 for x in records if str(x.get('price_src') or '').startswith('Amazon page')), "Current", "",
      f"Price column uses the Amazon page price for that exact ASIN where checked; {sum(1 for x in records if x.get('price_cc') is not None)} had changed since the Command Center snapshot and the cell comment keeps the older price. The page price matched the tracked child in 493 of 549 checkable rows on Oct 13-14."),
     ("Competitor image, size and colour (US)", "Amazon.com exact-ASIN pages (agent, Part A; data/competitor_details)", "2026-10-14", len(comp_det), "Current", "",
      f"257 US competitor ASINs that lacked an image, size or colour were checked on their own Amazon page (signed out, ZIP 10001). {len(comp_det)} kept their ASIN; 4 redirected to another ASIN and are left blank, not substituted (B0DG2HRZKK, B09G8P3X6L, B0D4PKVNWB, B0D1RBXBNG). Fills 165 of the 169 missing images. Size and colour come from the page's variation attributes, never the title. Brand and parent now follow Amazon as of Oct 14: B07M67HRKS is WETCAT (Command Center: Chakir Turkish) and B0D59BMBK7 is Fafua (CC: NORTHERN BROTHERS); 28 competitors have a new parent ASIN (Amazon re-parented them; the old Command Center parent is kept in the cell comment). Keepa (Command Center keepa_history) confirmed both brands and agreed with the page on all 11 tracked ASINs where Keepa lists a parent; the other 17 rest on the page alone."),
     ("Our product photos (web dashboard)", "Agent zips: product_images_ours.zip Part 1 update (SHA-256 52e6570b...8ec109e) and product_images_ours_part2.zip (SHA-256 147ac537...b67dfc); product_images/manifest_ours*.csv + provenance_ours*.csv", "2026-10-15", _om["ok"], "Partial", "",
      f"Parts 1 and 2: {_om['ok']:,} exact-ASIN main images of our {_om['scope']:,} listed child ASINs ({_om['US']:,} US, {_om['CA']:,} CA), all checked as 200 px RGB JPEGs matching the manifest; all 45 best-selling children covered. "
      f"Sources: {_om['src']}. Not available: {_om['nok']:,} ({_om['err']}), never filled with a placeholder or another ASIN."
      "US and CA share the same listing for the same ASIN, so where one marketplace has no photo the other marketplace's photo of that SAME ASIN is used (flagged in the cell comment and on the dashboard tile); a different ASIN is never used. Anything still without a photo shows the COMING SOON picture. In the workbook our images come from the Data Dive / Xray image URLs."),
     ("Canada competitors", "Amazon.ca page research (agent, Prompt 9)", "2026-10-13", sum(len(v) for v in ca_comp.values()), "Partial" if ca_comp else "Missing", "",
      "Page-1 organic results per product keyword, same material and piece count, Queen selected (2 King), CAD, logged out Toronto. 15 rivals each for DC B4, S4, S6, SSS4 (reuses S4) and Satin Fitted; 8 for DC B6 (only 8 qualifying 6-piece bamboo sets). No Command Center fields (weekly units, ASINsight) exist for Canada; Keepa .ca BFCM 2025 history follows after the US pulls. Our Canadian comparison price is the live Amazon.ca price from Helium 10 Xray (Oct 14, CAD)."),
     ("Competitors' BFCM 2025 history (Canada)", "Keepa .ca via agent (" + ", ".join(os.path.basename(f_) for f_ in _kfiles_ca) + ")", "Nov 1 - Dec 5, 2025", len(keepa25_ca), "Partial" if _ca_pending else "Exact", "",
      f"{len(keepa25_ca)} of 68 Canadian competitor ASINs delivered (Amazon.ca, domain 6, CAD); {len(_ca_pending)} still being pulled. Kept apart from the US history: 7 of these ASINs also sell in the US at different prices, and earlier builds showed their US figures on the Canada tabs. B0FNR1QR4J now redirects to B0FNQW1YT4 and is not substituted."),
     ("Competitors' BFCM 2025 history (US)", "Keepa via agent (" + ", ".join(os.path.basename(f_) for f_ in _kfiles) + ")", "Nov 1 - Dec 5, 2025", len(keepa25), ("Partial" if any(x.get("bf_type") is None for x in US_recs) else "Exact"), "",
      f"{len(keepa25)} US competitor ASINs pulled (P1 70 + P2 240, complete); {sum(1 for x in US_recs if x.get('bf_type') is None)} US rows without a BFCM 2025 result (ASINs Keepa has no history for). Spot-checked Oct 14 against the Command Center's own Keepa (keepa_history): Buy Box, List Price, Lightning Deal, Prime Exclusive and coupon days identical; daily rank values differ slightly because the agent reads 23:59 UTC and the Command Center reads per Eastern day. Pre-event = Nov 1-19 (pull starts Nov 1), BFCM = Nov 20 - Dec 1. Daily end-of-day state, so a deal of a few hours can be missed. Coupons are listed, not netted into the low price.")]
for i, r_ in enumerate(S):
    r_ = (r_[0],) + tuple(r_[2:])   # the source column is never shown
    for j, v in enumerate(r_, 1):
        c = chk.cell(row=row, column=j, value=v); c.border = BOX; c.alignment = WRAP
        c.font = F(bold=(i == 0), color=("FFFFFF" if i == 0 else "000000"))
        if i == 0:
            c.fill = HDR
        elif j == 4:
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

# ------------------------------------------------------------------ BFCM Stock tab
stk = wb.create_sheet("BFCM Stock")
stk.sheet_view.showGridLines = False
stk["A1"] = "BFCM 2026 stock outlook: will each variation last to Nov 30?"; stk["A1"].font = F(size=13, bold=True, color=C_NAVY)
stk["A2"] = (f"SellerBoard inventory pulled Oct 15, 2026 (Ecotero; Amazon.com {sum(1 for k in sb_inv if k[0] == 'US'):,} and Amazon.ca {sum(1 for k in sb_inv if k[0] == 'CA'):,} ASINs). "
             "On hand = units at Amazon (FBA stock + moving between warehouses). Inbound = units already sent to Amazon (SellerBoard 'sent to FBA'); SellerBoard holds no ETA, "
             "so shipments are listed by Amazon status. Demand: Oct 16 - Nov 18 (34 days) at SellerBoard's current velocity, Nov 19 - 30 (12 days) at velocity x BFCM lift. "
             f"Lift = the product's own BFCM 2025 lift where reliable; otherwise ASSUMED at the account's BFCM 2025 lift (US {ACCT_LIFT['US']:.2f}x, CA {ACCT_LIFT['CA']:.2f}x). SellerBoard's velocity runs about 1.5x the 28-day units on the big products (its window includes Prime Big Deal Days and the late-September deals), so the outlook leans cautious; the 28-day pace is shown beside it as a cross-check. Blue cells are inputs; the rest are formulas.")
stk["A2"].font = F(size=8.5, italic=True); stk["A2"].alignment = WRAP; stk.merge_cells("A2:T2"); stk.row_dimensions[2].height = 52
SC = [("tab", "Product tab", 16), ("mkt", "Mkt", 5), ("asin", "Child ASIN", 12), ("sku", "SKU", 22), ("size", "Size", 9), ("colour", "Colour", 11),
      ("on_hand", "On hand at Amazon", 9), ("inbound", "Inbound (sent to FBA)", 9), ("ships", "Inbound shipments (status: units)", 30),
      ("vel", "Sales a day now", 8), ("vel_src", "Velocity source", 16), ("lift", "BFCM lift used", 7), ("lift_src", "Lift source", 22),
      ("need", "Units needed Oct 16 - Nov 30", 10), ("short", "Short even with inbound", 9), ("oos", "Runs out (on hand only)", 11),
      ("oos_in", "Runs out (with inbound)", 11), ("status", "Status", 18), ("v28", "Sales a day, 28-day units / 28 (cross-check)", 9),
      ("need28", "Units needed at the 28-day pace", 10)]
# product summary (formulas over the detail rows below)
sum_rows = [(pid, mkt) for pid, *_ in PRODUCTS for mkt in ("US", "CA") if (pid, mkt) in cc and stock_outlook(pid, mkt)["rows"]]
hdr_s = 4
SUMC = ["Product tab", "Mkt", "Variations", "On hand", "Inbound", "Sales a day", "BFCM lift", "Units needed to Nov 30", "Short even with inbound",
        "Covered", "Need inbound in time", "Short with inbound", "Out of stock now", "Lift source", "Units needed at the 28-day pace (cross-check)"]
for j, h in enumerate(SUMC, 1):
    c = stk.cell(row=hdr_s, column=j, value=h); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CENTER; c.border = BOX
stk.row_dimensions[hdr_s].height = 36
det_hdr = hdr_s + len(sum_rows) + 3
d0, d1 = det_hdr + 1, det_hdr + sum(len(stock_outlook(pid, mkt)["rows"]) for pid, mkt in sum_rows)
rng = lambda col: f"${col}${d0}:${col}${d1}"
for i, (pid, mkt) in enumerate(sum_rows):
    rr_ = hdr_s + 1 + i
    so_ = stock_outlook(pid, mkt)
    tab_ = f"{mkt} {next(p_[2] for p_ in PRODUCTS if p_[0] == pid)}"[:31]
    vals = [tab_, mkt, f'=COUNTIFS({rng("A")},A{rr_},{rng("B")},B{rr_})', f'=SUMIFS({rng("G")},{rng("A")},A{rr_},{rng("B")},B{rr_})',
            f'=SUMIFS({rng("H")},{rng("A")},A{rr_},{rng("B")},B{rr_})', f'=SUMIFS({rng("J")},{rng("A")},A{rr_},{rng("B")},B{rr_})', so_["lift"],
            f'=SUMIFS({rng("N")},{rng("A")},A{rr_},{rng("B")},B{rr_})', f'=SUMIFS({rng("O")},{rng("A")},A{rr_},{rng("B")},B{rr_})']
    vals += [f'=COUNTIFS({rng("A")},A{rr_},{rng("B")},B{rr_},{rng("R")},"{st_}")' for st_ in ("Covered to Nov 30", "Needs inbound in time", "Short even with inbound", "Out of stock now")]
    vals.append(so_["lift_src"])
    vals.append(f'=SUMIFS({rng("T")},{rng("A")},A{rr_},{rng("B")},B{rr_})')
    for j, v in enumerate(vals, 1):
        c = stk.cell(row=rr_, column=j, value=v); c.border = BOX; c.font = F(size=8.5)
        c.number_format = {4: "#,##0", 5: "#,##0", 6: "#,##0.0", 7: "0.00x", 8: "#,##0", 9: "#,##0", 15: "#,##0"}.get(j, "General")
    stk.cell(row=rr_, column=1).hyperlink = f"#'{tab_}'!A1"
stk.cell(row=det_hdr - 1, column=1, value="Every variation with stock, inbound or sales (sorted by sales a day within each product)").font = F(bold=True, size=10, color=C_NAVY)
for j, (k_, h_, w_) in enumerate(SC, 1):
    c = stk.cell(row=det_hdr, column=j, value=h_); c.font = F(bold=True, color="FFFFFF", size=8); c.fill = HDR; c.alignment = CENTER; c.border = BOX
    stk.column_dimensions[CL(j)].width = w_
stk.row_dimensions[det_hdr].height = 40
rr_ = d0
BLUE = "0000FF"
for pid, mkt in sum_rows:
    so_ = stock_outlook(pid, mkt)
    tab_ = f"{mkt} {next(p_[2] for p_ in PRODUCTS if p_[0] == pid)}"[:31]
    for x in so_["rows"]:
        vals = {"tab": tab_, "mkt": mkt, "asin": x["asin"], "sku": x["sku"], "size": x["size"], "colour": x["colour"], "on_hand": x["on_hand"],
                "inbound": x["inbound"], "ships": "; ".join(f"{a} {b.lower().replace('_', ' ')}: {u:,}" for a, b, u in x["ships"]) or None,
                "vel": round(x["vel"], 3), "vel_src": x["vel_src"], "lift": round(so_["lift"], 4) if so_["lift"] else None, "lift_src": so_["lift_src"],
                "need": f"=J{rr_}*{PRE_DAYS}+J{rr_}*L{rr_}*{BF_DAYS}", "short": f"=MAX(0,N{rr_}-G{rr_}-H{rr_})",
                "oos": f'=IF(J{rr_}=0,"",IF(G{rr_}<J{rr_}*{PRE_DAYS},DATE(2026,10,15)+G{rr_}/J{rr_},IF(G{rr_}<N{rr_},DATE(2026,11,18)+(G{rr_}-J{rr_}*{PRE_DAYS})/(J{rr_}*L{rr_}),"after Nov 30")))',
                "oos_in": f'=IF(J{rr_}=0,"",IF(G{rr_}+H{rr_}<J{rr_}*{PRE_DAYS},DATE(2026,10,15)+(G{rr_}+H{rr_})/J{rr_},IF(G{rr_}+H{rr_}<N{rr_},DATE(2026,11,18)+(G{rr_}+H{rr_}-J{rr_}*{PRE_DAYS})/(J{rr_}*L{rr_}),"after Nov 30")))',
                "status": f'=IF(AND(G{rr_}<=0,J{rr_}>0),"Out of stock now",IF(G{rr_}>=N{rr_},"Covered to Nov 30",IF(G{rr_}+H{rr_}>=N{rr_},"Needs inbound in time","Short even with inbound")))',
                "v28": round(x["u28"] / 28, 3) if isinstance(x.get("u28"), (int, float)) else None, "need28": f'=IF(S{rr_}="","",S{rr_}*{PRE_DAYS}+S{rr_}*L{rr_}*{BF_DAYS})'}
        for j, (k_, h_, w_) in enumerate(SC, 1):
            c = stk.cell(row=rr_, column=j, value=vals[k_]); c.border = BOX; c.font = F(size=8.5, color=(BLUE if k_ in ("on_hand", "inbound", "vel", "lift", "v28") else "000000"))
            c.number_format = {"on_hand": "#,##0", "inbound": "#,##0", "vel": "#,##0.00", "lift": "0.00x", "need": "#,##0", "short": "#,##0", "oos": "mmm d", "oos_in": "mmm d", "v28": "#,##0.00", "need28": "#,##0"}.get(k_, "General")
            if k_ in ("ships", "lift_src", "vel_src"):
                c.alignment = WRAP
        rr_ += 1
stk.conditional_formatting.add(f"R{d0}:R{d1}", FormulaRule(formula=[f'OR(R{d0}="Short even with inbound",R{d0}="Out of stock now")'], fill=PatternFill("solid", fgColor="FFC7CE")))
stk.conditional_formatting.add(f"R{d0}:R{d1}", FormulaRule(formula=[f'R{d0}="Needs inbound in time"'], fill=PatternFill("solid", fgColor="FFEB9C")))
stk.freeze_panes = stk.cell(row=d0, column=4)
stk.auto_filter.ref = f"A{det_hdr}:T{d1}"

# order: README, Dashboard, Product Index, product tabs..., Data Gaps, Data
# order: README, US Dashboard, CA Dashboard, Product Index, BFCM Stock, US product tabs, CA product tabs, Data Check, Data Gaps, data sheets
_front = ["README", "US Dashboard", "CA Dashboard", "Product Index", "BFCM Stock"]
_us = [t for p_, m_, t in TABS if m_ == "US"]
_ca = [t for p_, m_, t in TABS if m_ == "CA"]
_back = ["Data Check", "Data Gaps", "Data", "Lists", "Lookup"]
_order = _front + _us + _ca + _back
_rest = [w_ for w_ in wb._sheets if w_.title not in _order]
wb._sheets = [wb[n_] for n_ in _order if n_ in wb.sheetnames] + _rest
for t_ in _us:
    wb[t_].sheet_properties.tabColor = "9DC3E6"
for t_ in _ca:
    wb[t_].sheet_properties.tabColor = "F4B183"
wb["Data"].sheet_state = "hidden"
wb.active = 0
# never name a data source in the workbook (agreed Oct 15, 2026)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrub import scrub as _scrub
from openpyxl.comments import Comment as _Cm
for ws_ in wb.worksheets:
    for row_ in ws_.iter_rows():
        for c_ in row_:
            if isinstance(c_.value, str) and not c_.value.startswith("="):
                c_.value = _scrub(c_.value)
            if c_.comment is not None:
                t_ = _scrub(c_.comment.text)
                c_.comment = _Cm(t_, "Tracker") if t_ else None
wb.save(OUT)
print(json.dumps({"tabs": len(TABS), "other_mkt_photos": len(xmkt_img), "competitor_rows": len(records), "image_cells": len(img_rows), "unique_images": len(seen),
                  "comp_missing_img": len(missing_comp), "strategy_products": len(strat), "sku_files": len(skus),
                  "catalog_us": len(catalog.get("US", {})), "catalog_ca": len(catalog.get("CA", {})), "dd_images": len(ddimg)}))
