# LTSF SKU for Auto / Broad / Phrase (operator, 28 Sep) — shared block for both builders
_LD = json.load(open(f'{S}/ltsf_detail.json'))
lead('Auto, Broad and Phrase — the LTSF SKU (operator, 28 September).', 'These campaigns advertise the size’s LTSF SKU — a child that sells little and carries a lot of stock — never White. Read on this product’s own stock and 30-day units: an LTSF SKU is a non-White child with 180+ days of Available cover, or 90+ days while selling at or below the size’s median child. Each size’s pick is the one with the most units beyond 90 days of cover among those that still sold 5+ units in 30 days (a child selling one a month would drag a discovery campaign’s conversion); where none sold 5, the largest excess is used.')
_lr = []
for sz, nm in (('KING', 'King'), ('QUEEN', 'Queen'), ('CALIFKING', 'Cal King'), ('FULL', 'Full'), ('TWIN', 'Twin')):
    xs = [x for x in _LD['rows'] if x['size'] == sz]
    pk = _LD['pick'].get(sz)
    px = next((x for x in xs if x['sku'] == pk), None)
    _lr.append([nm, (f"{pk.replace('BAMBOO-', '').replace('-6PCS', '').title()} — {px['units30']} sold, {px['available']} Available, {px['days'] or 'no sales'} days" if px else 'none qualifies — advertise a non-White child, never White'),
                ', '.join(f"{x['sku'].replace('BAMBOO-', '').replace('-6PCS', '').title()} ({x['days'] or '—'}d)" for x in xs if x['sku'] != pk) or '—'])
table(['Size', 'LTSF SKU for Auto / Broad / Phrase', 'Other LTSF children'], _lr, widths=[1.8, 7.4, 8.8], size=7.5)
_lt = [r for r in RV if r.get('ltsf_pick') is not None or any('no LTSF child' in i for i in r['issues'])]
_lw = [r for r in RV if any(i.startswith('SKU') and ('LTSF SKU is' in i or 'no LTSF child' in i) for i in r['issues'])]
lead('What the data shows.', f"{len(_lw)} Auto, Broad and Phrase campaigns advertise a child that is not their size’s LTSF SKU — most of them White (the register names each campaign and its LTSF SKU). Re-point them by hand; the loader skips every SKU swap. Clearance campaigns (Liquidation) and brand-term campaigns keep their own SKUs.")
