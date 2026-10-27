"""Builds the web Competitor Dashboard from the same data as the workbook.

Images: the artifact viewer only loads images shipped with the page, so a record shows its photo when
product_images/<ASIN>.jpg (or US_<ASIN>.jpg / CA_<ASIN>.jpg from the agent's image zip) exists; otherwise the
card says the photo arrives with the image file. No placeholder pictures are used.
Usage: python3 build_dashboard.py OUT.html
"""
import json, os, sys, glob, re, html, statistics, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
IMG_DIR = os.path.join(HERE, "product_images")
have_img = {os.path.splitext(f)[0]: f for f in os.listdir(IMG_DIR)} if os.path.isdir(IMG_DIR) else {}

# reuse the workbook builder's data assembly without writing a workbook
sys.argv = [sys.argv[0], os.devnull, os.devnull, "--no-image-formula", "--data-only"]
spec = importlib.util.spec_from_file_location("br", os.path.join(HERE, "build_research.py"))
br = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(br)
except SystemExit:
    pass

used_img = set()
def img_for(asin, mkt="US", other=True):
    """Key into images.js (photos shipped with the page as data URIs; the viewer blocks Amazon's image host)."""
    # last resort: the other marketplace's photo of the SAME ASIN (US and CA share the listing); never a different ASIN
    for k in (f"{mkt}_{asin}", asin) + ((f"{'CA' if mkt == 'US' else 'US'}_{asin}",) if other else ()):
        if asin and k in have_img and have_img[k].lower().endswith(".jpg"):
            used_img.add(k)
            return k
    return None

def num(v):
    return v if isinstance(v, (int, float)) and v == v else None

WINDOWS = (("pre", "Oct 21 – Nov 19, 2025 (30 days before)"), ("bfcm", "Nov 20 – Dec 1, 2025 (BFCM week)"), ("dec", "Dec 2 – 31, 2025"))

products = []
for pid, mkt, tname in br.TABS:
    p, o = br.our_profile(pid, mkt)
    title, img, best, parent = br.our_title_and_image(pid, mkt)
    e = br.econ(o.get("economics"))
    lf = br.lift_of(pid, mkt) or {}
    vars_ = br.our_variations(pid, mkt)
    bv = next((v for v in vars_ if v["asin"] == best), {})
    price, psrc = br.our_headline_price(pid, mkt, best, e["price"])
    vrows, cols, sizes = [], {}, {}
    for v in vars_:
        live = v.get("price_now") is not None
        u = v.get("units_28d") or 0
        vrows.append({"asin": v["asin"], "sku": v.get("sku"), "size": v.get("size"), "colour": v.get("colour"),
                      "price": v["price_now"] if live else None, "live": live, "src": v.get("now_src") if live else None,
                      "u28": num(v.get("units_28d")), "rating": num(v.get("x_rating")), "reviews": num(v.get("x_reviews")), "bsr": num(v.get("x_bsr")),
                      "status": v.get("status"), "img": img_for(v["asin"], mkt), "url": v.get("image"),
                      "deal": num(v.get("deal_price")), "dealDisc": num(v.get("deal_disc")), "dealSt": v.get("deal_status")})
        for d_, k in ((cols, v.get("colour")), (sizes, v.get("size"))):
            if k:
                d_.setdefault(k, {"name": k, "n": 0, "u28": 0})
                d_[k]["n"] += 1; d_[k]["u28"] += u
    so_ = br.stock_outlook(pid, mkt)
    srow = {x["asin"]: x for x in so_["rows"]}
    for vr in vrows:
        x = srow.get(vr["asin"])
        vr["stk"] = {"oh": x["on_hand"], "ib": x["inbound"], "st": x["status"], "oos": x["oos"].isoformat() if x["oos"] else None} if x else None
    stock26 = {"lift": so_["lift"], "liftSrc": so_["lift_src"], "onHand": so_["on_hand"], "inbound": so_["inbound"], "vel": so_["vel"], "need": so_["need"],
               "short": so_["short"], "counts": so_["counts"],
               "need28": sum((x["u28"] or 0) / 28 * (br.PRE_DAYS + (so_["lift"] or 1) * br.BF_DAYS) for x in so_["rows"] if isinstance(x.get("u28"), (int, float))),
               "rows": [{"asin": x["asin"], "sku": x["sku"], "size": x["size"], "colour": x["colour"], "oh": x["on_hand"], "ib": x["inbound"], "vel": x["vel"],
                         "velSrc": x["vel_src"], "need": x["need"], "short": x["short"], "oos": x["oos"].isoformat() if x["oos"] else None,
                         "oosIn": x["oos_in"].isoformat() if x["oos_in"] else None, "st": x["status"],
                         "ships": [{"id": a, "status": b, "units": u} for a, b, u in x["ships"]]} for x in so_["rows"]]} if so_["rows"] else None
    sb = br.sb_of(pid, mkt)
    sbrows = []
    for w, lab in WINDOWS:
        x = sb.get(w)
        if not x:
            continue
        ad = abs(x["advertising"]) if x.get("advertising") is not None else None
        sbrows.append({"label": lab, "sales": x.get("sales"), "units": x.get("units"), "org": x.get("units_organic"),
                       "ad": (x.get("units_ppc") or 0) + (x.get("units_sd") or 0), "adcost": ad,
                       "tacos": (ad / x["sales"]) if ad is not None and x.get("sales") else None, "sessions": x.get("sessions"),
                       "usp": (x["unit_session_pct"] / 100) if x.get("unit_session_pct") is not None else None, "avg": x.get("avg_sales_price")})
    hk = br.hero25.get((pid, mkt))
    hk_line = None
    if hk and (hk.get("pre") or hk.get("rank_pre")):
        bits = []
        if hk["pre"] and hk["bf"]:
            bits.append(f"{hk['asin']}: ${hk['pre']:,.2f} before (median Nov 1 – 19) → ${hk['bf']:,.2f} in BFCM week, "
                        + (f"{1 - hk['bf'] / hk['pre']:.0%} lower" if hk["bf"] < hk["pre"] else "no cut"))
        if hk["rank_pre"] and hk["rank_bf"]:
            bits.append(f"Best Seller Rank {hk['rank_pre']:,} → {hk['rank_bf']:,}")
        if hk.get("ped"):
            bits.append(f"Prime Exclusive price seen {hk['ped']}")
        hk_line = "; ".join(bits) + ". Keepa via the Command Center (lowest new offer; we are the only seller)."
    dl = br.deals25.get((pid, mkt)) or []
    deals = "; ".join(html.escape(f"{c['type']} {c['start'][5:]} to {c['end'][5:]} ({'ran' if c['status'] == 'ran' else 'cancelled'}, {len(c['kids'])} variations"
                                  + (f", {c['units']:,} units" if c['units'] else "") + ")") for c in dl) or None
    so, sg = br.stock_oos.get((pid, mkt)), br.stock_gap.get((pid, mkt))
    stock = (f"{so['oos_asins']} of {so['asins']} variations hit zero FBA stock on at least one observed day in BFCM week"
             + (f"; weighted by sales mix, about {so['weighted']:.1%} of variation-days were lost" if so.get("weighted") is not None else "") + ".") if so else None
    gap = None
    if sg:
        n_ = sum(v for k, v in sg.items() if not k.startswith("_"))
        gap = (f"{sg.get('in_stock', 0)} of {n_} variation-days in stock, {sg.get('out_of_stock', 0)} out of stock, {sg.get('unknown', 0)} unknown"
               + (f"; {sg['sold_despite_zero_snapshots']} sold although both readings were zero (stock arriving that day): {', '.join(sg['_sold0'])}" if sg.get("sold_despite_zero_snapshots") else "")
               + ". Inferred from units sold and the readings either side.")
    products.append({
        "key": f"{pid}-{mkt}", "pid": pid, "mkt": mkt, "short": br.PINFO[pid][2], "scope": br.scope_of(pid), "family": br.PINFO[pid][1], "role": br.PINFO[pid][3],
        "brand": p.get("brand") or o.get("brand"), "name": p.get("name") or o.get("name"), "title": title, "parent": parent, "best": best,
        "bestLabel": " ".join(x for x in (bv.get("size"), bv.get("colour")) if x) or best, "img": img_for(best, mkt, False) or img_for(parent, mkt, False) or img_for(best, mkt),
        "stage": br.our_stage(pid, mkt, p, o), "price": price, "priceSrc": psrc, "contrib": e["contribution"], "be": e["be_acos"], "u28": e["units_28d"],
        "lift": lf.get("lift"), "tacos": lf.get("tacos_actual") if lf.get("tacos_actual") is not None else lf.get("tacos"),
        "preTacos": lf.get("pre_tacos_actual") if lf.get("pre_tacos_actual") is not None else lf.get("pre_tacos"),
        "hk": hk, "hkCut": (1 - hk["bf"] / hk["pre"]) if hk and hk.get("pre") and hk.get("bf") else None, "hkLine": hk_line,
        "deals": deals, "plan26": br.plan26_text(pid, mkt), "slack": [{"topic": r_["topic"], "detail": r_["detail"], "source": r_["source"]} for r_ in br.slack_deal.get((pid, mkt)) or []], "da": br.deal_assumption(pid, mkt), "imgUrl": img, "stock": stock, "stockGap": gap, "sb": sbrows or None,
        "stock26": stock26, "vars": vrows, "colours": sorted(cols.values(), key=lambda c: -c["u28"]), "sizes": sorted(sizes.values(), key=lambda c: -c["u28"]),
    })

KEYS = ("pid", "mkt", "product", "tier", "brand", "title", "parent", "child", "price", "price_src", "price_cc", "lp", "bsr", "wk", "rating", "reviews", "seen",
        "var", "var_src", "size", "colour", "our_same", "basis", "listed", "dd30", "ful", "country", "asi_tr", "asi_kw", "org_pct", "ad_pct", "top_kw", "top_kw_pct",
        "r_sp", "r_sb", "r_sbv", "r_ac", "contested", "we_win", "we_lose", "theirs_only", "theirs_only_share", "ppc_none", "ppc_aggr", "hero",
        "pd", "pd_pre", "q2", "l30", "str_show", "str_label", "str_price", "deal_now", "stock_now", "str_checked",
        "bf_type", "bf_dates", "bf_pre", "bf_low", "bf_disc_v", "bsr_pre", "bsr_bf", "bsr_lift_v", "bf_oos", "notes", "parent_cc", "brand_cc", "ro", "cls", "cls_why", "mat")
comps = []
for i, x in enumerate(br.records):
    c = {k: x.get(k) for k in KEYS}
    c["uid"] = f"c{i}"
    c["key"] = f"{x['pid']}-{x['mkt']}"
    c["img"] = (img_for(x.get("image_asin"), x["mkt"], False) or img_for(x.get("child"), x["mkt"], False)
                or img_for(x.get("child"), x["mkt"]) or img_for(x.get("image_asin"), x["mkt"]))
    pr, wk = num(x.get("price")), num(x.get("wk"))
    c["rev"] = pr * wk * 52 / 12 if pr is not None and wk is not None else None
    c["gap"] = (pr / x["our_same"] - 1) if pr is not None and num(x.get("our_same")) else None
    comps.append(c)

# portfolio summary per marketplace
summary = {}
for m in ("US", "CA"):
    rs = [x for x in br.records if x["mkt"] == m]
    kids = {x["child"] for x in rs if x.get("child")}
    sbm = [v for (mk, _), v in br.sellerboard.items() if mk == m]
    pre = sum((v.get("pre") or {}).get("sales") or 0 for v in sbm)
    bf = sum((v.get("bfcm") or {}).get("sales") or 0 for v in sbm)
    summary[m] = {"comps": len(kids), "compRows": len(rs), "withBf": len({x["child"] for x in rs if x.get("bf_type")}),
                  "accountLift": ((bf / 12) / (pre / 30)) if pre and bf else None}

# cross-checks (numbers computed from the data where the comparison can be re-run here)
US = [x for x in br.records if x["mkt"] == "US"]
ro_pairs = [(x, x["ro"]) for x in US if x.get("ro")]
def same(a, b):
    return a is not None and b is not None and abs(float(a) - float(b)) < 1e-6
n_bsr = sum(1 for x, r in ro_pairs if same(x.get("bsr"), r.get("bsr")))
n_rev = sum(1 for x, r in ro_pairs if same(x.get("reviews"), r.get("reviews")))
n_rat = sum(1 for x, r in ro_pairs if same(x.get("rating"), r.get("rating")))
changed = sum(1 for x in US if x.get("price_cc") is not None)
paged = sum(1 for x in US if str(x.get("price_src") or "").startswith("Amazon page"))
checks = [
    {"name": "Competitor price, tracked ASIN", "compared": "Command Center snapshot (Oct 12) vs the competitor's own Amazon page (Oct 13 – 14)",
     "status": "Updated", "detail": f"{paged} of {len(US)} US rows now carry the Amazon page price for that exact ASIN; {changed} had moved since the Command Center snapshot and now show the newer page price (the older price is kept in the workbook cell comment)."},
    {"name": "Command Center weekly scrape vs tracker", "compared": "competitors_roster (week of Oct 11) vs the tracked child ASIN",
     "status": "Difference noted", "detail": f"All {len(US)} US rows found in the Command Center list. Best Seller Rank equal on {n_bsr}, rating on {n_rat}, reviews on {n_rev}. The Command Center list reads each rival's seed ASIN, often a different variation; checked against the Amazon page, the tracker's price was the exact-ASIN price in 493 of 549 rows and the seed price in 137. Both are shown, labelled."},
    {"name": "Competitors newly mapped", "compared": "Command Center mappings vs tracker", "status": "Updated",
     "detail": f"{br.roster_added} product–competitor pairs mapped after the tracker's snapshot were added (B4, B6, CooLinens Cooling). Keepa BFCM 2025 history pulled for the 6 new ASINs."},
    {"name": "Competitor Keepa, P2 file", "compared": "Final 240-ASIN file vs batches 1 – 4", "status": "Match", "detail": "8,400 rows, 240 of 240 ASINs; the 6,300 rows also in batches 1 – 3 and the 2,100 in batch 4 are identical."},
    {"name": "Competitor Keepa, agent pull", "compared": "Agent Keepa vs Command Center keepa_history", "status": "Match",
     "detail": "Buy Box, List Price, Lightning Deal, Prime Exclusive and coupon days identical on the spot-checked ASINs (B01N9L2O9P, B0CRTM5ZDN). Daily rank differs slightly: the agent reads 23:59 UTC, the Command Center reads per Eastern day."},
    {"name": "Canadian competitors' Keepa", "compared": "Final keepa_history_ca.csv vs partial file + batches 1 – 4", "status": "Match",
     "detail": f"68 of 68 ASINs, 2,380 rows; every row identical to the earlier deliveries. Amazon.ca only, in CAD, kept apart from the US history (7 ASINs sell in both markets). {sum(1 for v in br.keepa25_ca.values() if v['bf_type'] == 'Not live in 2025')} were not yet tracked by Keepa in Nov 2025; B0FNR1QR4J now redirects to B0FNQW1YT4 and is not substituted."},
    {"name": "Our BFCM 2026 deal plan", "compared": "BM's plan (Oct 15) vs Amazon's deal feed (Command Center amazon_promotions)", "status": "Difference noted",
     "detail": "None of the planned US or CA deals for Nov 19 – 30, 2026 shows in Amazon's deal feed yet (0 deals Nov 15 – Dec 5 in both markets). Deal price, depth, variations and committed units are not in the plan yet."},
    {"name": "Our BFCM 2025 deals", "compared": "Deals file (DataHub) vs Command Center amazon_promotions", "status": "Match",
     "detail": "Same 31 US campaigns, dates and units: 6 Best Deals ran Nov 20 – Dec 1 (B4 4,890 units, S4 4,311, B6 2,927, Satin Fitted 1,865, SSS4 1,152, S6 1,008); 25 cancelled. No US coupons Nov 1 – Dec 5."},
    {"name": "Our hero prices, BFCM 2025", "compared": "Keepa price (Command Center) vs Best Deal start", "status": "Match",
     "detail": "All 6 Best Deal heroes drop price on Nov 20: B4 $74.99 to $71.24, B6 $79.99 to $75.99, S4 $29.95 to $25.46, S6 $33.95 to $32.25, Satin Fitted $16.95 to $15.15, SSS4 $33.95 to $31.41. B4's $71.24 equals SellerBoard's average sale price that week."},
    {"name": "Our BFCM 2025 sales lift", "compared": "SellerBoard actual sales vs Command Center estimate", "status": "Match",
     "detail": "Actual lifts agree with the Command Center estimates (B4 4.25x, B6 2.49x, S4 2.64x). Each SellerBoard file sums exactly to SellerBoard's period totals."},
    {"name": "Stock on the 6 days with no snapshot", "compared": "Agent units sold (DataHub) vs SellerBoard", "status": "Match",
     "detail": "US units on Dec 1, 2025: 3,257 in both. 3,936 variation-days covered; 3,503 in stock, 39 out of stock, 386 unknown, 8 sold despite zero readings."},
    {"name": "Competitor brand and parent", "compared": "Amazon page vs Keepa (Command Center)", "status": "Match",
     "detail": "Both brand changes confirmed (B07M67HRKS WETCAT, B0D59BMBK7 Fafua); the page parent matched Keepa on all 11 tracked ASINs that list one. 27 competitors now show the current parent."},
    {"name": "Our live prices", "compared": "Helium 10 Xray vs Amazon page check", "status": "Match",
     "detail": "Xray matched every price also verified on the Amazon page. US core: 895 of 917 variations hold a live price; Canada core 495 of 590 (the rest are out of stock, have no Buy Box, or had no sales)."},
]
_vr = os.path.join(HERE, "data", "verification_report.json")
if os.path.exists(_vr):
    _rep = json.load(open(_vr))
    for r_ in _rep["checks"]:
        checks.append({"name": "Re-check: " + r_["name"], "compared": r_["compared"], "status": "Match" if r_["status"] == "Pass" else "Difference noted",
                       "detail": f"{r_['checked']:,} checked, {r_['mismatches']} mismatches." + (f" {r_['note']}." if r_.get("note") else "")
                                 + " Independent script (verify_tracker.py) recomputing from the raw files."})
sources = [
    {"data": "Competitor price, Best Seller Rank, reviews, weekly units", "source": "Command Center snapshot (tracked child ASIN)", "asof": "2026-10-12", "rows": len(US)},
    {"data": "Competitor price, newest", "source": "Amazon page for the exact ASIN (agent)", "asof": "2026-10-13 / 14", "rows": paged},
    {"data": "Competitor tier, X-Ray sales band, listing assets", "source": "Command Center Competitor Summary (competitors_roster)", "asof": "week of 2026-10-11", "rows": len(ro_pairs)},
    {"data": "Competitor image, size, colour", "source": "Amazon page (agent) and Data Dive", "asof": "2026-10-14", "rows": len(br.comp_det)},
    {"data": "Our product photos", "source": "Agent zips, Parts 1 and 2 (exact ASIN); the other marketplace's photo of the same ASIN where one market has none (labelled); otherwise Coming Soon with the Open photo link", "asof": "2026-10-15", "rows": br._om["ok"]},
    {"data": "Strikethrough shown, label, price", "source": "Amazon page check (agent)", "asof": "2026-10-13", "rows": len(br.str_now)},
    {"data": "Search and ads (ASINsight)", "source": "Command Center", "asof": "2026-09-29", "rows": sum(1 for x in US if x.get("asi_tr") is not None)},
    {"data": "Competitors' BFCM 2025 history", "source": "Keepa (agent P1 + P2; Command Center for 6 new ASINs)", "asof": "Nov 1 – Dec 5, 2025", "rows": len(br.keepa25)},
    {"data": "Canadian competitors", "source": "Amazon.ca page research (agent)", "asof": "2026-10-13", "rows": sum(len(v) for v in br.ca_comp.values())},
    {"data": "Canadian competitors' BFCM 2025 history", "source": "Keepa .ca (agent), CAD", "asof": "Nov 1 – Dec 5, 2025", "rows": len(br.keepa25_ca)},
    {"data": "Our live prices", "source": "Helium 10 Xray (US Oct 13, CA Oct 14), Amazon page, SellerBoard listing price", "asof": "2026-10-13 / 14", "rows": sum(1 for p in products for v in p["vars"] if v["live"])},
    {"data": "Our BFCM 2025 sales", "source": "SellerBoard (Ecotero account)", "asof": "Oct 21 – Dec 31, 2025", "rows": len(br.sellerboard)},
    {"data": "BFCM 2026 stock outlook", "source": "SellerBoard inventory and FBA shipments (Ecotero, read-only pull)", "asof": "2026-10-15", "rows": len(br.sb_inv)},
    {"data": "Deal pricing, pre-BFCM deal decisions, STR tests", "source": "Slack: Umair Tahir deal reviews (Oct 13–15), Abubakar Ishrat STR updates (Oct 13–15)", "asof": "2026-10-15", "rows": sum(len(v) for v in br.slack_deal.values())},
    {"data": "Our BFCM 2026 deal plan", "source": "BM (Slack)", "asof": "2026-10-15", "rows": sum(len(v) for v in br.plan26.values())},
    {"data": "Our BFCM 2025 deals", "source": "DataHub promotions, checked against Command Center amazon_promotions", "asof": "2026-10-14", "rows": sum(len(v) for v in br.deals25.values())},
    {"data": "Our heroes' BFCM 2025 price and rank", "source": "Command Center keepa_history", "asof": "Nov 1 – Dec 5, 2025", "rows": len(br.hero25)},
    {"data": "Our BFCM 2025 stock", "source": "DataHub inventory + units sold on days with no snapshot", "asof": "Nov 15 – Dec 5, 2025", "rows": 27552},
]

sys.path.insert(0, HERE)
from scrub import scrub_obj
for s_ in sources:
    s_.pop("source", None)
for p_ in products:
    for x_ in p_.get("slack") or []:
        x_.pop("source", None)
products, comps, checks, sources = scrub_obj(products), scrub_obj(comps), scrub_obj(checks), scrub_obj(sources)
payload = json.dumps({"products": products, "comps": comps, "summary": summary, "checks": checks, "sources": sources,
                      "built": "2026-10-14", "imagesLoaded": len(used_img)}, separators=(",", ":"), default=str)
import base64, io
from PIL import Image as _PIL

def _thumb(path, side=160):
    """Re-encode as a small thumbnail so the photo files stay under the artifact's 16 MB per-file limit."""
    im = _PIL.open(path).convert("RGB")
    im.thumbnail((side, side))
    b = io.BytesIO()
    im.save(b, "JPEG", quality=72, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

_items = [("COMING_SOON", _thumb(os.path.join(HERE, "assets", "coming_soon.jpg"), 400))] + [(k, _thumb(os.path.join(IMG_DIR, have_img[k]))) for k in sorted(used_img)]
_half = (len(_items) + 1) // 2
for _fn, _part in (("images.js", _items[:_half]), ("images2.js", _items[_half:])):
    with open(os.path.join(os.path.dirname(os.path.abspath(OUT)), _fn), "w") as fh:
        fh.write("window.IMG=Object.assign(window.IMG||{},{" + ",".join(f'"{k}":"{v}"' for k, v in _part) + "});")
tpl = open(os.path.join(HERE, "dashboard_template.html")).read()
open(OUT, "w").write(tpl.replace("/*__DATA__*/null", payload))
print(json.dumps({"products": len(products), "comps": len(comps), "images_used": len(used_img), "bytes": os.path.getsize(OUT)}))
