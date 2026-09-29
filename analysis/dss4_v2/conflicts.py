"""Stage 11 — Conflict register: every place two sources disagree, with the numbers, what was checked, and which value the plan uses (and why).
Output: v2/out/conflicts.json"""
import json, collections
import load as L

P = json.load(open(L.OUT + 'product.json'))
K = {k['keyword']: k for k in json.load(open(L.OUT + 'keywords.json'))}
C = json.load(open(L.OUT + 'campaigns_base.json'))
D = json.load(open(L.OUT + 'decisions.json'))
SUM = L.J(L.RAW + 'cc/summary.json')
SKU = {s['sku']: s for s in P['skus']}
rows = []


def add(area, a, b, checked, resolution, status):
    rows.append(dict(area=area, source_a=a, source_b=b, checked=checked, resolution=resolution, status=status))


# 1 unit economics
for c in P['econ_conflicts'][:8]:
    add('Profit per unit — ' + c['sku'], f"Command Center contribution ${c['cc_contribution']}/unit (list price ${c['cc_price']}, fee date {c['cc_fee_date']})",
        f"Sellerboard profit before ads ${c['sb_pba_unit']}/unit (realised price ${c['sb_price']}, 30 d)",
        f"Gap ${c['gap']}: price realised vs list ${c['gap_price']}, storage ${c['sb_storage']}, inbound fee ${c['sb_inbound']}, refunds ${c['sb_refunds']}, "
        f"FBA ${c['sb_fba']} vs ${c['cc_fulfil']}, COGS ${c['sb_cogs']} vs ${c['cc_landed']}",
        'Sellerboard used: it is what the account actually earned in the last 30 days (discounts, refunds, storage and inbound fees included)', 'Resolved')
# 2 stock
qb, kb = SKU['SATIN-QUEEN-BLACK']['inv'], SKU['SATIN-KING-BLACK']['inv']
add('Stock — Queen Black (B0839MKJMV)', f"Sellerboard 29 Sep: {qb['sellable']} sellable, {qb['on_hand']} on hand, {qb['reserved']} reserved",
    f"Data Dive 23 Sep: {L.DD_INV['B0839MKJMV']['totalSellableUnits']} sellable across FCs",
    'Six days of sales (~125 units) explain part of it; no inbound or removal found in the shipments; the other SKU on the ASIN (TF-XHNL-B3YJ) holds 0',
    'Plan uses the lower Sellerboard figure (stock-out risk is the binding constraint). Check Manage FBA Inventory in Seller Central before sizing the reorder', 'Open')
add('Stock — King Black (B0839LD2WQ)', f"Sellerboard 29 Sep: {kb['sellable']} sellable + {kb['res_transfer']} in FC transfer ({kb['on_hand']} on hand)",
    f"Data Dive 23 Sep: {L.DD_INV['B0839LD2WQ']['totalSellableUnits']} sellable",
    'Shipments sent 17 and 24 Aug were being received between 10 and 29 Sep; Sellerboard lost-sales units ' + str(kb.get('lost_sales_units')),
    'Resolved: King Black is restocked — it becomes the King ranking child', 'Resolved')
# 3 ads totals
tot = SUM.get('totals') or SUM
kw30 = sum((k['m30'] or {}).get('spend') or 0 for k in K.values())
add('Ad spend — keyword rows vs product total (30 d)', f"Command Center keyword rows ${kw30:,.0f}", f"Command Center product total ${tot.get('spend', 18484):,.0f}",
    'Keyword rows include search terms counted in more than one campaign lens', 'Product total used for shares; keyword rows only for term-level reads', 'Resolved')
sb = {c['campaign_id']: c['sb30'] for c in C if c['sb30']}
m = [(c['campaign_id'], c['m30']['spend'], sb[c['campaign_id']]['spend']) for c in C if c['m30'] and c['campaign_id'] in sb]
diff = [x for x in m if x[1] and abs(x[2] - x[1]) / x[1] > 0.03]
add('Campaign spend — Sellerboard vs Command Center (30 d)', f"Sellerboard ${sum(x[2] for x in m):,.0f} on {len(m)} matched campaigns",
    f"Command Center ${sum(x[1] for x in m):,.0f}", f"{len(diff)} campaigns differ by more than 3% (window edges)", 'Command Center used for campaign metrics; Sellerboard for budget, utilisation and live bids', 'Resolved')
f30 = P['family30']['Info']
add('Ad-attributed orders vs units sold', f"Command Center ad orders 1,572 / ${48393:,} (30 d, 7-day attribution, any child of the brand)",
    f"Sellerboard PPC units {f30.get('UnitsPPC')} / ${f30.get('SalesPPC'):,.0f} (same-SKU attribution)", 'Queen Black: ad orders 28.3/day vs 20.8 units/day sold',
    'Stock projections scale ad-order changes by units ÷ ad orders per child; ACoS stays on Command Center for campaign comparisons', 'Resolved (definitions differ)')
# 4 ranks
for t in ('silk sheets', 'silk sheets king', 'satin sheets'):
    k = K[t]
    add(f"Organic rank — '{t}'", f"Rank Radar (Queen Black) 7-day median {k.get('radar_med7')}, today {k.get('radar_now')}",
        f"Command Center crawl {k.get('cc_rank_last')}; ASINsight {(k.get('asinsight') or {}).get('organic')}",
        'Different crawl times and ASINs (Rank Radar tracks B0839MKJMV; ASINsight takes the family’s best position)', 'Rank Radar used for trend and targets (daily, one ASIN, 91 days)', 'Resolved')
add('Search volume', 'Keyword library (Helium 10) e.g. silk sheets 51,852/month', 'Amazon SQP Q3: silk sheets ' + f"{K['silk sheets']['sqp_q3']['volume']:,}/quarter",
    'Different sources and definitions', 'SQP used (Amazon’s own counts, with purchases)', 'Resolved')
add('SQP scope', 'SQP “our” counts (Data Dive radar on B0839MKJMV)', 'Ad orders on the same terms (all children)', 'silk sheets: SQP our purchases 20 in Q3 vs 30 ad orders in 30 days',
    'SQP “our share” read as Queen Black’s share, not the family’s — targets are set on that basis', 'Resolved (scope noted)')
# 5 campaign identity
nm = sum(1 for c in C if c['name_mismatch'])
dd1 = sum(1 for c in C if c['child_source'].startswith('Data Dive'))
add('Advertised child — campaign name vs actual', f"{nm} campaigns whose name names a different SKU than they advertise", f"Data Dive product ads: {dd1} single-ASIN campaigns checked",
    'Data Dive agrees with the audit export on every one of them (0 conflicts)', 'The actual advertised child is used everywhere; names are not relied on', 'Resolved')
# 6 audit rules
b6 = sum(1 for d in L.AUDIT['decisions'] if 'B6' in json.dumps(d))
add('Audit rules from another product', f"{b6} audit decisions cite the B6 corrections document", 'This product’s data',
    'Each re-decided on this product’s data (see the audit review)', 'B6 rules not used', 'Resolved')
ch = sum(1 for d in L.AUDIT['decisions'] if d['kind'] == 'child' and d['current_at_audit'] == 'SATIN-QUEEN-BLACK' and d['suggested'] == 'SATIN-4PCS-QUEEN-STONE-GREY')
add('Audit “hero rule” — ranking child', f"Audit moves {ch} Queen Black campaigns to Queen Stone Grey (21 paid clicks, 1 order: CVR 4.8%)",
    'Queen Black: 18.2% top-of-search CVR on 90 d; LTSF #1 for Queen is Queen Grey, not Stone Grey', 'Checked against the LTSF sheet (column V) and 90-day placement reads',
    'Ranking stays on Queen Black; non-ranking Queen traffic goes to Queen Grey (LTSF #1), then Stone Grey (#2)', 'Resolved')
add('LTSF sheet date', 'S4-LTSF sheet: aged snapshot 15 Jul, sales to 27 Aug', 'Sellerboard stock 29 Sep',
    'Aged units left estimated = aged − sheet sales − 30-day pace × 33 days', 'Estimate used for routing; refresh the aged-inventory report before the next review', 'Open (estimate)')
json.dump(rows, open(L.OUT + 'conflicts.json', 'w'), indent=1)
if __name__ == '__main__':
    for r in rows:
        print(r['status'], '|', r['area'], '|', r['resolution'][:90])
