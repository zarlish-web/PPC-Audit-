"""Stage 1 — Product: SKU economics (Sellerboard), size/colour mix, monthly trend, inventory and inbound, source conflicts.
Output: v2/out/product.json"""
import json, collections, re
import load as L

# ---------------------------------------------------------------- SKU identity
canon = {}
for r in L.SB_SKU30:
    i = r['Info']
    z = L.size_of_sku(i['SKU'], i['Name'])
    c = L.colour_of_sku(i['SKU'], i['Name'])
    if re.match(r'^(Amazon\.Found|[A-Z0-9]{2}-[A-Z0-9]{4}-)', i['SKU']):
        c = None
    canon[i['SKU']] = dict(sku=i['SKU'], asin=i['ASIN'], size=z, colour=c, title=i['Name'])
by_asin = collections.defaultdict(list)
for s, v in canon.items():
    by_asin[v['asin']].append(s)
for s, v in canon.items():                           # odd SKUs inherit the colour of the main SKU on the same ASIN
    if v['colour'] is None:
        main = [x for x in by_asin[v['asin']] if canon[x]['colour']]
        v['colour'] = canon[main[0]]['colour'] if main else (L.colour_of_sku('', v['title']) or '?')
        v['alias_of'] = main[0] if main else None


def fee(r, name):
    return sum(abs(x['sum']) for x in r.get('AmazonFeeDetails') or [] if x['fee'] == name)


def econ(rowsrc):
    out = {}
    for r in rowsrc:
        i = r['Info']
        u = i['Units'] or 0
        s = i['Sales'] or 0
        ads = abs(i.get('Advertising') or 0)
        net = i.get('NetProfit') or 0
        pba = net + ads
        fees = r.get('AmazonFeeDetails') or []
        e = dict(units=u, orders=i.get('Orders'), sales=round(s, 2), avg_price=round(s / u, 2) if u else None, list_price=i.get('Price'),
                 ads=round(ads, 2), sp=abs(i.get('SponsoredADS') or 0), sb=abs(i.get('HSA') or 0), sbv=abs(i.get('VideoAds') or 0),
                 net=round(net, 2), pba=round(pba, 2), pba_unit=round(pba / u, 2) if u else None, be_acos=round(pba / s, 4) if s else None,
                 margin_after_ads=round(net / s, 4) if s else None, tacos=round(ads / s, 4) if s else None,
                 referral=round(fee(r, 'Commission'), 2), fba=round(fee(r, 'FBAPerUnitFulfillmentFee'), 2), storage=round(fee(r, 'FBAStorageFee'), 2),
                 inbound_fee=round(fee(r, 'FBAInboundConvenienceFee') + fee(r, 'FBAInboundPlacementServiceFee'), 2),
                 other_fees=round(abs(i.get('AmazonFees') or 0) - fee(r, 'Commission') - fee(r, 'FBAPerUnitFulfillmentFee') - fee(r, 'FBAStorageFee')
                                  - fee(r, 'FBAInboundConvenienceFee') - fee(r, 'FBAInboundPlacementServiceFee'), 2),
                 amazon_fees=round(abs(i.get('AmazonFees') or 0), 2), cogs=round(abs(i.get('ProductCosts') or 0), 2), cost_unit=i.get('Cost'),
                 refunds_units=i.get('Refunds'), refund_cost=round(abs(i.get('ProductRefunds') or 0), 2), promo=round(abs(i.get('PromotionValue') or 0), 2),
                 units_ppc=i.get('UnitsPPC'), units_org=i.get('UnitsOrganic'), sales_ppc=i.get('SalesPPC'), sessions=i.get('sessions'),
                 usp=i.get('unitSessionPercentage'), bsr=i.get('BSR'), real_acos=i.get('RealACOS'))
        out[i['SKU']] = e
    return out


E30, E90, EDEAL = econ(L.SB_SKU30), econ(L.SB_SKU90), econ(L.SB_SKUDEAL)

# ---------------------------------------------------------------- inventory & inbound
INV = {r['SKU']: r for r in L.SB_INV}
open_in = collections.defaultdict(lambda: dict(shipped=0, plan_only=0, lines=[]))
seen_plan = set()
for l in L.SB_SHIP['family_sku_lines']:
    st = l['shipment_status'] or ''
    if st.startswith(('CLOSED', 'CANCELLED', 'DELETED')):
        continue
    rem = (l['units'] or 0) - (l['units_received'] or 0)
    if rem <= 0:
        continue
    o = open_in[l['sku']]
    if st.startswith('NO_SHIPMENT'):
        o['plan_only'] += rem
    else:
        o['shipped'] += rem
    o['lines'].append(dict(ship=l['amazon_shipment'] or l['plan_id'], status=st, date=l['shipment_date'] or l['plan_date'], units=l['units'], received=l['units_received'], open=rem))

# seasonality: last year's Oct/Nov/Dec units vs Sep 2025 (family, Sellerboard)
MON = {m['month']: m['Info'] for m in L.SB_MONTHLY}
sep25 = MON['2025-09']['Units']
SEASON = {k: round(MON[k]['Units'] / sep25, 3) for k in ('2025-10', '2025-11', '2025-12', '2026-01')}

skus = []
for s, v in canon.items():
    e3, e9 = E30.get(s, {}), E90.get(s, {})
    iv = INV.get(s, {})
    sell = iv.get('FBAStock')
    vel30 = (e3.get('units') or 0) / 30
    vel90 = (e9.get('units') or 0) / 91
    o = open_in.get(s, {})
    days = round(sell / vel30) if sell and vel30 else None
    need_q4 = round(vel30 * (31 * SEASON['2025-10'] + 30 * SEASON['2025-11'] + 31 * SEASON['2025-12']))
    skus.append(dict(**v, e30=e3, e90=e9, deal_jul=EDEAL.get(s),
                     inv=dict(sellable=sell, on_hand=iv.get('OnHand'), reserved=iv.get('Reserved'), res_transfer=iv.get('reserved_fc_transfers'),
                              res_processing=iv.get('reserved_fc_processing'), res_customer=iv.get('reserved_customerorders'), sent_to_fba=iv.get('SentToFBA'),
                              awd=iv.get('StockAWD'), sb_days_left=iv.get('DaysOfStockLeft'), sb_velocity=iv.get('SalesVelocity'),
                              lost_sales_units=iv.get('LostSalesUnits'), inbound_shipped_open=o.get('shipped', 0), inbound_plan_only=o.get('plan_only', 0),
                              inbound_lines=o.get('lines', []), vel30=round(vel30, 2), vel90=round(vel90, 2),
                              days_sellable_30=days, days_all_30=round(((sell or 0) + (iv.get('reserved_fc_transfers') or 0) + o.get('shipped', 0)) / vel30) if vel30 else None,
                              q4_need_at_30d_pace=need_q4)))

# ---------------------------------------------------------------- by size and by colour (30 days)
def agg(keyf):
    g = collections.defaultdict(lambda: collections.Counter())
    for k in skus:
        e = k['e30']
        if not e:
            continue
        x = g[keyf(k)]
        for f in ('units', 'sales', 'ads', 'net', 'pba', 'units_ppc', 'units_org', 'sessions', 'cogs', 'amazon_fees', 'refund_cost'):
            x[f] += e.get(f) or 0
        x['stock'] += k['inv']['sellable'] or 0
        x['transfer'] += k['inv']['res_transfer'] or 0
        x['inbound'] += k['inv']['inbound_shipped_open'] or 0
    out = {}
    for key, x in g.items():
        out[key] = dict(x, pba_unit=round(x['pba'] / x['units'], 2) if x['units'] else None, be_acos=round(x['pba'] / x['sales'], 4) if x['sales'] else None,
                        avg_price=round(x['sales'] / x['units'], 2) if x['units'] else None, usp=round(x['units'] / x['sessions'] * 100, 2) if x['sessions'] else None)
    return out


BY_SIZE = agg(lambda k: k['size'])
BY_SIZE_COLOUR = agg(lambda k: f"{k['size']}|{k['colour']}")

# ---------------------------------------------------------------- family totals & monthly
fam30 = L.SB_FAMILY30
MONTHLY = []
for m in L.SB_MONTHLY:
    i = m['Info']
    ads = abs(i.get('Advertising') or 0)
    MONTHLY.append(dict(month=m['month'], partial=m.get('partial'), sales=round(i['Sales']), units=i['Units'], orders=i['Orders'], ads=round(ads),
                        sp=round(abs(i.get('SponsoredADS') or 0)), sb=round(abs(i.get('HSA') or 0)), sbv=round(abs(i.get('VideoAds') or 0)),
                        sd=round(abs(i.get('SponsoredDisplay') or 0)), net=round(i['NetProfit']), pba=round(i['NetProfit'] + ads),
                        tacos=round(ads / i['Sales'], 4), margin=round(i['NetProfit'] / i['Sales'], 4), units_ppc=i.get('UnitsPPC'), units_org=i.get('UnitsOrganic'),
                        org_share=round(i['UnitsOrganic'] / i['Units'], 4), sessions=i.get('sessions'), usp=round(i.get('unitSessionPercentage') or 0, 2),
                        avg_price=round(i['Sales'] / i['Units'], 2), promo=round(abs(i.get('PromotionValue') or 0)), refunds=i.get('Refunds')))

# ---------------------------------------------------------------- CC vs Sellerboard economics conflict, decomposed
CCE = {r['sku']: r for r in L.CC_CONTEXT['economics']['skus']}
conf = []
for k in skus:
    c = CCE.get(k['sku'])
    e = k['e30']
    if not c or not e or not e.get('units') or e['units'] < 20:
        continue
    u = e['units']
    sb = dict(price=e['avg_price'], referral=e['referral'] / u, fba=e['fba'] / u, cogs=e['cogs'] / u, storage=e['storage'] / u,
              inbound=e['inbound_fee'] / u, refunds=e['refund_cost'] / u, other=e['other_fees'] / u, promo=e['promo'] / u)
    conf.append(dict(sku=k['sku'], units=u, cc_price=c.get('price'), sb_price=sb['price'], cc_referral=c.get('referral'), sb_referral=round(sb['referral'], 2),
                     cc_fulfil=c.get('fulfilment'), sb_fba=round(sb['fba'], 2), cc_landed=c.get('landedCost'), sb_cogs=round(sb['cogs'], 2),
                     sb_storage=round(sb['storage'], 2), sb_inbound=round(sb['inbound'], 2), sb_refunds=round(sb['refunds'], 2), sb_other=round(sb['other'], 2),
                     sb_promo=round(sb['promo'], 2), cc_contribution=round(c['contribution'], 2) if c.get('contribution') is not None else None, sb_pba_unit=e['pba_unit'],
                     gap=round((c['contribution'] or 0) - (e['pba_unit'] or 0), 2) if c.get('contribution') is not None else None,
                     gap_price=round((c.get('price') or 0) - sb['price'], 2), cc_fee_date=c.get('feeDate')))
conf.sort(key=lambda x: -x['units'])

OUT = dict(skus=skus, by_size=BY_SIZE, by_size_colour=BY_SIZE_COLOUR, family30=fam30, family90=L.SB_FAMILY90, monthly=MONTHLY, season=SEASON,
           econ_conflicts=conf)
json.dump(OUT, open(L.OUT + 'product.json', 'w'), indent=1, default=str)
if __name__ == '__main__':
    print('family30', json.dumps(fam30)[:600])
    for z, v in BY_SIZE.items():
        print(z, {k: (round(v[k], 2) if isinstance(v[k], float) else v[k]) for k in ('units', 'sales', 'ads', 'pba', 'pba_unit', 'be_acos', 'avg_price', 'units_org', 'units_ppc', 'stock', 'transfer', 'inbound', 'usp')})
    print('season', SEASON)
    for c in conf[:12]:
        print(c)
