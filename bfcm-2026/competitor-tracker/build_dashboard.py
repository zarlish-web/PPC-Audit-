"""Builds the web Competitor Dashboard (dashboard.html) from the same data as the workbook.

Images: the artifact viewer only loads images shipped with the page, so a record shows its
photo when product_images/<ASIN>.jpg exists (from AGENT_PROMPTS Prompt 11); otherwise the card
says the image file is pending. No placeholder pictures are used.
Usage: python3 build_dashboard.py OUT.html
"""
import json, os, sys, glob, re, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
IMG_DIR = os.path.join(HERE, "product_images")
have_img = {os.path.splitext(f)[0] for f in os.listdir(IMG_DIR)} if os.path.isdir(IMG_DIR) else set()

# reuse the workbook builder's data assembly without writing a workbook
sys.argv = [sys.argv[0], os.devnull, os.devnull, "--no-image-formula", "--data-only"]
spec = importlib.util.spec_from_file_location("br", os.path.join(HERE, "build_research.py"))
br = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(br)
except SystemExit:
    pass

def img_for(asin):
    return f"product_images/{asin}.jpg" if asin and asin in have_img else None

products = []
for pid, mkt, tname in br.TABS:
    p, o = br.our_profile(pid, mkt)
    title, img, best, parent = br.our_title_and_image(pid, mkt)
    e = br.econ(o.get("economics"))
    lf = br.lift_of(pid, mkt)
    vars_ = br.our_variations(pid, mkt)
    products.append({
        "key": f"{pid}-{mkt}", "pid": pid, "mkt": mkt, "short": br.PINFO[pid][2], "family": br.PINFO[pid][1], "role": br.PINFO[pid][3],
        "brand": p.get("brand") or o.get("brand"), "name": p.get("name") or o.get("name"), "title": title, "parent": parent, "best": best,
        "img": img_for(best) or img_for(parent), "stage": p.get("stage") or o.get("stage"), "skus": p.get("skuCount") or o.get("sku_count"),
        "sizes": p.get("sizes") or o.get("sizes") or [], "colours": p.get("colours") or [], "price": br.our_headline_price(pid, mkt, best, e["price"])[0], "priceSrc": br.our_headline_price(pid, mkt, best, e["price"])[1], "contrib": e["contribution"],
        "be": e["be_acos"], "u28": e["units_28d"],
        "lift": lf["lift"] if lf else None, "tacos": lf["tacos"] if lf else None, "preTacos": lf["pre_tacos"] if lf else None, "dec": lf["dec"] if lf else None,
        "vars": [{"asin": v["asin"], "sku": v["sku"], "size": v["size"], "colour": v["colour"], "price": v["price_now"] if v.get("price_now") is not None else v["price"], "live": v.get("price_now") is not None, "u28": v["units_28d"],
                  "img": img_for(v["asin"])} for v in vars_],
    })

comps = []
for x in br.records:
    comps.append({k: x.get(k) for k in ("pid", "mkt", "family", "product", "tier", "brand", "title", "parent", "child", "price", "lp", "bsr", "wk",
                                         "rating", "reviews", "var", "size", "colour", "our_same", "basis", "asi_tr", "org_pct", "ad_pct", "top_kw",
                                         "r_sp", "r_sb", "r_sbv", "r_ac", "contested", "we_win", "we_lose", "theirs_only", "ppc_none", "ppc_aggr", "hero",
                                         "listed", "pd", "pd_pre", "str_show", "str_label", "str_price", "page_price", "deal_now", "stock_now", "seen", "our_live", "bf_type", "bf_dates", "bf_pre", "bf_low", "bf_disc_v", "bsr_lift_v", "raised")} | {"img": img_for(x.get("image_asin")) or img_for(x.get("child")), "key": f"{x['pid']}-{x['mkt']}"})

payload = json.dumps({"products": products, "comps": comps, "built": "2026-10-13", "imagesLoaded": len(have_img)}, separators=(",", ":"), default=str)
tpl = open(os.path.join(HERE, "dashboard_template.html")).read()
open(OUT, "w").write(tpl.replace("/*__DATA__*/null", payload))
print(json.dumps({"products": len(products), "comps": len(comps), "images_available": len(have_img), "bytes": os.path.getsize(OUT)}))
