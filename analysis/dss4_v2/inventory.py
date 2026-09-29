"""Stage 9 — Stock against the plan: for each ranking child and each LTSF target, today's stock (Sellerboard), the pace under the plan
(today's non-ad sales + the plan's ad orders on that child) scaled by last year's Oct–Jan seasonality, the stock-out date, and what must be
ordered to reach 31 Jan. Output: v2/out/inventory.json"""
import json, datetime as dt, collections
import load as L

P = json.load(open(L.OUT + 'product.json'))
D = json.load(open(L.OUT + 'decisions.json'))
R = json.load(open(L.OUT + 'ranking.json'))
LT = json.load(open(L.OUT + 'ltsf.json'))
SKU = {s['sku']: s for s in P['skus']}
SEASON = P['season']                                   # month units ÷ Sep-2025 units (Sellerboard, family)
MON = {10: SEASON['2025-10'], 11: SEASON['2025-11'], 12: SEASON['2025-12'], 1: SEASON['2026-01']}
now_ads = collections.Counter()
plan_ads = collections.Counter()
for d in D['decisions']:
    now_ads[d['child']] += d['now']['orders_day']
    plan_ads[d['action']['child_to'] or d['child']] += d['plan']['orders_day']
for n in D['new_campaigns']:
    o = next(x for x in R['opportunities'] if x['keyword'] == n['term'])
    plan_ads[n['child']] += (o['target_clicks_day'] or 0) * (o['paid_cvr'] or 0.15)

TODAY = dt.date(2026, 9, 29)
END = dt.date(2027, 1, 31)


def run(sku):
    s = SKU[sku]
    iv, e3 = s['inv'], s['e30']
    units_day = (e3.get('units') or 0) / 30
    ads_now = now_ads.get(sku, 0)
    # ad-attributed orders on a child can exceed its own units (7-day attribution counts other children bought after the click);
    # so the plan's change in ad orders lands on this child in the proportion units ÷ ad orders (capped at 1)
    land = min(1.0, units_day / ads_now) if ads_now else 1.0
    base = units_day
    pace_sep = max(0.0, units_day + (plan_ads.get(sku, 0) - ads_now) * land)
    stock = (iv['sellable'] or 0) + (iv['res_transfer'] or 0) + (iv['inbound_shipped_open'] or 0)
    sq_out, sq_need = sim(stock, units_day)
    pl_out, pl_need = sim(stock, pace_sep)
    return dict(sku=sku, size=s['size'], colour=s['colour'], sellable=iv['sellable'], in_transfer=iv['res_transfer'], inbound_shipped=iv['inbound_shipped_open'],
                inbound_plan_only=iv['inbound_plan_only'], stock_total=stock, units_day_30=round(units_day, 2), ad_orders_day_now=round(ads_now, 2),
                land_share=round(land, 2), plan_ad_orders_day=round(plan_ads.get(sku, 0), 2), plan_pace_sep_equiv=round(pace_sep, 2),
                stockout_now_pace=sq_out, short_now_pace=sq_need, stockout_date=pl_out, units_short_to_31jan=pl_need, lost_sales_units_sb=iv.get('lost_sales_units'))


def sim(stock, pace_sep):
    left, day, out_date, need = stock, TODAY, None, 0.0
    while day <= END:
        f = MON.get(day.month, 1.0)
        use = pace_sep * f
        if left >= use:
            left -= use
        else:
            if out_date is None:
                out_date = day
            need += use - max(left, 0)
            left = 0
        day += dt.timedelta(days=1)
    return (str(out_date) if out_date else None), round(need)


kids = sorted(set(v['chosen'] for v in R['preferred'].values()) | set(s for v in D['ltsf_targets'].values() for s in v) | {'SATIN-QUEEN-GREY', 'SATIN-4PC-KING-GREY'})
OUT = dict(season=MON, rows=[run(k) for k in kids if k in SKU])
json.dump(OUT, open(L.OUT + 'inventory.json', 'w'), indent=1)
if __name__ == '__main__':
    for r in OUT['rows']:
        print(r['sku'][:26].ljust(26), 'stock', r['stock_total'], '(sell', r['sellable'], 'trf', r['in_transfer'], 'inb', r['inbound_shipped'], ')', 'u/d', r['units_day_30'],
              'ads now', r['ad_orders_day_now'], 'plan ads', r['plan_ad_orders_day'], 'pace', r['plan_pace_sep_equiv'], '| out now-pace', r['stockout_now_pace'], 'plan', r['stockout_date'], 'short to 31 Jan', r['units_short_to_31jan'])


# ---------------------------------------------------------------- back-up switch: when the preferred child falls under SWITCH_DAYS of stock, its ranking
# ad orders move to the back-up (at the level the back-up can carry). Project the switch date and how long the back-up lasts after it.
SWITCH_DAYS = 14
rank_orders = collections.Counter()                  # plan ad orders/day of ranking campaigns, per preferred child
for d in D['decisions']:
    if d['role'].startswith('Ranking –'):
        rank_orders[d['action']['child_to'] or d['child']] += d['plan']['orders_day']
BK = []
for size, v in R['preferred'].items():
    pref, chain = v['chosen'], v.get('backups') or []
    pr = next((r for r in OUT['rows'] if r['sku'] == pref), None) or run(pref)
    left, day, sw = pr['stock_total'], TODAY, None
    while day <= END:
        use = pr['plan_pace_sep_equiv'] * MON.get(day.month, 1.0)
        if sw is None and left < SWITCH_DAYS * use:
            sw = day
        left = max(0.0, left - use)
        day += dt.timedelta(days=1)
    take = sw                                          # back-up 1 takes over at the switch; back-up 2 when back-up 1 runs out
    for i, b in enumerate(chain):
        s = SKU[b['sku']]
        iv = s['inv']
        stock = (iv['sellable'] or 0) + (iv['res_transfer'] or 0) + (iv['inbound_shipped_open'] or 0)
        own = run(b['sku'])['plan_pace_sep_equiv']
        pr_land = pr.get('land_share') or 1.0
        extra = rank_orders.get(pref, 0) * pr_land * (1.0 if b['level'].startswith('push') else 0.5)   # maintain level ≈ half the push clicks
        left2, d2, out2 = stock, TODAY, None
        while d2 <= END:
            use = (own + (extra if (take and d2 >= take) else 0)) * MON.get(d2.month, 1.0)
            if left2 < use and out2 is None:
                out2 = d2
            left2 = max(0.0, left2 - use)
            d2 += dt.timedelta(days=1)
        BK.append(dict(size=size, preferred=pref, backup=b['sku'], order=i + 1, level=b['level'], switch_date=str(take) if take else None, backup_stock=stock,
                       backup_own_pace=round(own, 2), ranking_orders_moved=round(extra, 2), backup_stockout=str(out2) if out2 else None))
        take = out2 if (take and out2 and out2 > take) else (take if not take else None)
OUT['backups'] = BK
json.dump(OUT, open(L.OUT + 'inventory.json', 'w'), indent=1)
if __name__ == '__main__':
    for b in BK:
        print(b)
