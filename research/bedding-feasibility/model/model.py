"""Unit economics + 12-month launch scenarios for the shortlisted products.
All inputs labelled ACTUAL / EST / ASSUMPTION in INPUTS; outputs written to model/out_*.csv"""
import json, csv, os
OUT = os.path.dirname(__file__)
FX = {"USD_PKR": 276.82, "USD_CAD": 1.3993, "GBP_USD": 1.3367}  # EST, research_fees_ads.md, 23-26 Oct 2026

# ---------- per-product inputs (local currency) ----------
P = {
 "P1_US_percale": dict(name="Pre-washed 100% long-staple cotton percale sheet set (4-pc)", mkt="US", cur="USD",
    mix={"Full":0.15,"Queen":0.40,"King":0.45}, price={"Full":59.99,"Queen":64.99,"King":69.99},
    fob_usd={"Full":13.00,"Queen":14.00,"King":15.50}, landed_mult=1.40, fba={"Full":8.80,"Queen":9.20,"King":9.20},
    referral=0.15, refund=0.065, unsellable_share=0.40, storage_inbound=1.00, promo=0.03, vat=0.0, cpc=2.40, cvr=0.08),
 "P2_US_waffle_duvet": dict(name="100% cotton waffle-weave duvet cover set (cover + 2 shams)", mkt="US", cur="USD",
    mix={"Queen":0.50,"King":0.50}, price={"Queen":74.99,"King":79.99},
    fob_usd={"Queen":17.50,"King":19.50}, landed_mult=1.40, fba={"Queen":9.50,"King":9.80},
    referral=0.15, refund=0.065, unsellable_share=0.40, storage_inbound=1.25, promo=0.03, vat=0.0, cpc=1.60, cvr=0.07),
 "P3_CA_percale": dict(name="Pre-washed cotton percale sheet set (4-pc), Canada", mkt="CA", cur="CAD",
    mix={"Full":0.15,"Queen":0.40,"King":0.45}, price={"Full":84.99,"Queen":89.99,"King":94.99},
    fob_usd={"Full":13.00,"Queen":14.00,"King":15.50}, landed_mult=1.38, fba={"Full":12.60,"Queen":13.00,"King":13.00},
    referral=0.15, refund=0.075, unsellable_share=0.40, storage_inbound=1.40, promo=0.03, vat=0.0, cpc=1.93, cvr=0.09),
 "P4_UK_percale_duvet": dict(name="Cotton percale duvet cover set, UK sizes (cover + 2 pillowcases)", mkt="UK", cur="GBP",
    mix={"Double":0.40,"King":0.40,"Super King":0.20}, price={"Double":34.99,"King":39.99,"Super King":44.99},
    fob_usd={"Double":10.50,"King":12.00,"Super King":13.50}, landed_mult=1.18, fba={"Double":4.40,"King":4.60,"Super King":4.90},
    referral=0.15, refund=0.05, unsellable_share=0.40, storage_inbound=0.80, promo=0.03, vat=0.20, cpc=1.00, cvr=0.08),
}
def to_local(usd, cur):
    return usd*FX["USD_CAD"] if cur=="CAD" else (usd/FX["GBP_USD"] if cur=="GBP" else usd)

def unit_econ(p, price_override=None, landed_mult=None, cpc=None, cvr=None, refund=None, fob_mult=1.0):
    mix=p["mix"]; pr=price_override or p["price"]
    price=sum(mix[s]*pr[s] for s in mix)
    fob=to_local(sum(mix[s]*p["fob_usd"][s] for s in mix), p["cur"])*fob_mult
    landed=fob*(landed_mult or p["landed_mult"])
    fba=sum(mix[s]*p["fba"][s] for s in mix)
    r=refund if refund is not None else p["refund"]
    net_rev=price/(1+p["vat"])*(1-r)            # revenue kept after VAT and refunds
    referral=price*p["referral"]*(1-r)           # referral on VAT-inclusive price, refunded on returns
    unsell=r*p["unsellable_share"]*landed
    promo=price*p["promo"]
    contrib=net_rev-referral-fba-landed-p["storage_inbound"]-unsell-promo
    be_acos=contrib/price
    c=cpc or p["cpc"]; v=cvr or p["cvr"]
    cpo=c/v
    return dict(price=price, vat=price-price/(1+p["vat"]), refunds=price/(1+p["vat"])*r, net_revenue=net_rev, fob=fob, freight_duty=landed-fob, landed=landed,
                referral=referral, fba=fba, storage_inbound=p["storage_inbound"], unsellable_returns=unsell, promo=promo,
                contribution_pre_ads=contrib, contribution_margin_pre_ads=contrib/price, breakeven_acos=be_acos,
                breakeven_roas=(1/be_acos if be_acos>0 else None), launch_cpo=cpo, launch_acos=cpo/price,
                contribution_after_launch_ads=contrib-cpo, ad_at_tacos12=price*0.12, contribution_after_tacos12=contrib-price*0.12,
                target_acos_for_10pct_margin=be_acos-0.10, target_acos_for_15pct_margin=be_acos-0.15)

rows=[]
for k,p in P.items():
    e=unit_econ(p); e.update(id=k, product=p["name"], marketplace=p["mkt"], currency=p["cur"]); rows.append(e)
with open(os.path.join(OUT,"out_unit_econ.csv"),"w",newline="") as f:
    w=csv.DictWriter(f, fieldnames=["id","product","marketplace","currency"]+[x for x in rows[0] if x not in ("id","product","marketplace","currency")]); w.writeheader(); w.writerows(rows)

# ---------- sensitivity (P1 US) ----------
base=unit_econ(P["P1_US_percale"])["contribution_pre_ads"]
sens=[]
def add(var,lo_kw,hi_kw,lo_lbl,hi_lbl):
    lo=unit_econ(P["P1_US_percale"],**lo_kw)["contribution_pre_ads"]; hi=unit_econ(P["P1_US_percale"],**hi_kw)["contribution_pre_ads"]
    sens.append(dict(variable=var, low_case=lo_lbl, high_case=hi_lbl, contrib_low=round(lo,2), contrib_base=round(base,2), contrib_high=round(hi,2), swing=round(abs(hi-lo),2)))
pp=P["P1_US_percale"]["price"]
add("Selling price ±10%",dict(price_override={s:v*0.9 for s,v in pp.items()}),dict(price_override={s:v*1.1 for s,v in pp.items()}),"-10%","+10%")
add("Factory FOB ±15%",dict(fob_mult=1.15),dict(fob_mult=0.85),"+15%","-15%")
add("Freight+duty uplift 1.31x–1.50x",dict(landed_mult=1.50),dict(landed_mult=1.31),"1.50x (freight spike)","1.31x (Sec.301 struck down)")
add("Refund rate 4%–10%",dict(refund=0.10),dict(refund=0.04),"10%","4%")
with open(os.path.join(OUT,"out_sensitivity_p1.csv"),"w",newline="") as f:
    w=csv.DictWriter(f, fieldnames=list(sens[0])); w.writeheader(); w.writerows(sorted(sens,key=lambda x:-x["swing"]))
# CPC / CVR sensitivity on launch cost per order
grid=[]
for c in [1.6,2.0,2.4,2.8,3.2]:
    for v in [0.06,0.08,0.10,0.12]:
        grid.append(dict(cpc=c,cvr=v,cost_per_order=round(c/v,2),acos_at_price=round(c/v/unit_econ(P["P1_US_percale"])["price"],3)))
with open(os.path.join(OUT,"out_cpc_cvr_grid.csv"),"w",newline="") as f:
    w=csv.DictWriter(f, fieldnames=list(grid[0])); w.writeheader(); w.writerows(grid)

# ---------- 12-month scenarios: P1 US launch (P2 added month 5 in base/upside) ----------
SCEN={
 "Conservative": dict(ramp=[2,4,6,7,8,9,9,10,10,11,11,12], cvr=[0.06,0.065,0.07,0.07,0.075,0.075,0.08,0.08,0.08,0.08,0.08,0.08], cpc=2.80,
                      organic=[0.08,0.12,0.15,0.18,0.20,0.22,0.24,0.25,0.26,0.28,0.29,0.30], price_disc=[0.15,0.10,0.05]+[0]*9, p2=False, initial_units=1500, reorder_units=1500),
 "Base":         dict(ramp=[3,7,11,14,17,19,21,23,24,25,26,27], cvr=[0.07,0.075,0.08,0.085,0.09,0.09,0.095,0.095,0.10,0.10,0.10,0.10], cpc=2.40,
                      organic=[0.10,0.15,0.20,0.25,0.29,0.32,0.35,0.38,0.40,0.42,0.44,0.45], price_disc=[0.10,0.05]+[0]*10, p2=True, initial_units=2500, reorder_units=2500),
 "Upside":       dict(ramp=[4,10,16,22,27,31,35,38,40,42,44,46], cvr=[0.08,0.09,0.10,0.105,0.11,0.11,0.115,0.12,0.12,0.12,0.12,0.12], cpc=2.10,
                      organic=[0.15,0.22,0.30,0.36,0.40,0.44,0.47,0.50,0.52,0.53,0.54,0.55], price_disc=[0.10]+[0]*11, p2=True, initial_units=4000, reorder_units=4000),
}
ONE_TIME={"Conservative":dict(samples_testing=3000,branding_trademark=3000,photo_video_aplus=3000,listing_localisation=1000,setup_ior_bond_3pl=2500,vine_launch_promos=2000),
          "Base":dict(samples_testing=6000,branding_trademark=5000,photo_video_aplus=6000,listing_localisation=1500,setup_ior_bond_3pl=4500,vine_launch_promos=4000),
          "Upside":dict(samples_testing=9000,branding_trademark=7000,photo_video_aplus=10000,listing_localisation=2000,setup_ior_bond_3pl=6000,vine_launch_promos=6000)}
CONT={"Conservative":0.10,"Base":0.15,"Upside":0.20}
p1=P["P1_US_percale"]; e1=unit_econ(p1)
p2=P["P2_US_waffle_duvet"]; e2=unit_econ(p2)
scen_rows=[]; summ=[]
for name,s in SCEN.items():
    inv=s["initial_units"]; cash=-(s["initial_units"]*e1["landed"]) ; cum_contrib=0; cash_min=cash; be_month=None
    one=sum(ONE_TIME[name].values()); cash-=one; cash_min=min(cash_min,cash)
    reorders=0; on_order=[]   # (arrival_month, units)
    totals=dict(units=0,revenue=0,ads=0,contrib=0)
    for m in range(12):
        # arrivals
        for a in [x for x in on_order if x[0]==m]: inv+=a[1]
        on_order=[x for x in on_order if x[0]!=m]
        d=s["ramp"][m]; units1=min(d*30, inv); inv-=units1
        units2=0
        if s["p2"] and m>=4: units2=int(round(units1*0.25))  # duvet line at ~25% of sheet units from month 5
        disc=s["price_disc"][m]
        rev1=units1*e1["price"]*(1-disc); rev2=units2*e2["price"]
        revenue=rev1+rev2
        org=s["organic"][m]; paid_units=(units1+units2)*(1-org)
        cpo=s["cpc"]/s["cvr"][m]; ads=paid_units*cpo
        contrib=units1*(e1["contribution_pre_ads"]-e1["price"]*disc*(1-p1["referral"]))+units2*e2["contribution_pre_ads"]-ads
        # cash: contribution arrives ~1 month later (payout lag simplified to same month) ; inventory purchased on reorder
        cash+=contrib+ (units1*e1["landed"]) + units2*e2["landed"]  # add back landed (already paid upfront) for units sold
        cash-= units2*e2["landed"]  # duvet stock bought just-in-time (simplification)
        # reorder trigger: cover < 4 months incl. lead time ~3 months
        pipeline=inv+sum(x[1] for x in on_order)
        nxt=s["ramp"][min(m+1,11)]*30
        if pipeline < nxt*4:
            on_order.append((m+3, s["reorder_units"])); cash-=s["reorder_units"]*e1["landed"]; reorders+=1
        cum_contrib+=contrib
        cash_min=min(cash_min,cash)
        if be_month is None and cum_contrib-one>=0: be_month=m+1
        totals["units"]+=units1+units2; totals["revenue"]+=revenue; totals["ads"]+=ads; totals["contrib"]+=contrib
        scen_rows.append(dict(scenario=name, month=m+1, units_sheets=units1, units_duvet=units2, revenue=round(revenue,0), price_discount=disc,
                              organic_share=org, cvr=s["cvr"][m], cpc=s["cpc"], ad_spend=round(ads,0), acos=round(ads/revenue,3) if revenue else None,
                              tacos=round(ads/revenue,3) if revenue else None, contribution_after_ads=round(contrib,0), inventory_end=inv,
                              on_order=sum(x[1] for x in on_order), cumulative_cash=round(cash,0)))
    cap_test=round((s["initial_units"]*e1["landed"]+one)*(1+CONT[name]) + max(0,-min(0,min(r["contribution_after_ads"] for r in scen_rows if r["scenario"]==name)))*3,0)
    summ.append(dict(scenario=name, units_12m=totals["units"], revenue_12m=round(totals["revenue"]), ad_spend_12m=round(totals["ads"]), tacos_12m=round(totals["ads"]/totals["revenue"],3),
                     contribution_12m=round(totals["contrib"]), one_time_costs=one, initial_inventory_landed=round(s["initial_units"]*e1["landed"]), contingency_pct=CONT[name],
                     peak_cash_need=round(-cash_min*(1+CONT[name])), reorders=reorders, cash_breakeven_month=(be_month or ">12"),
                     inventory_end=inv))
with open(os.path.join(OUT,"out_scenarios_monthly.csv"),"w",newline="") as f:
    w=csv.DictWriter(f, fieldnames=list(scen_rows[0])); w.writeheader(); w.writerows(scen_rows)
with open(os.path.join(OUT,"out_scenarios_summary.csv"),"w",newline="") as f:
    w=csv.DictWriter(f, fieldnames=list(summ[0])); w.writeheader(); w.writerows(summ)
json.dump(dict(P=P,ONE_TIME=ONE_TIME,SCEN=SCEN,CONT=CONT,FX=FX),open(os.path.join(OUT,"inputs.json"),"w"),indent=1)
for r in rows: print({k:(round(v,2) if isinstance(v,float) else v) for k,v in r.items()})
print(); [print(x) for x in summ]
