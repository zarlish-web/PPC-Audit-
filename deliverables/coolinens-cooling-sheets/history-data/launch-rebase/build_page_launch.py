import json, html, statistics
D = json.load(open('/tmp/claude-0/cs/w/rebase/page_new.json'))
VR = {v['kw']: v for v in json.load(open('/tmp/claude-0/cs/w/verify_rows.json'))}
e = html.escape
money = lambda v, n=2: '' if v in (None, '') else f'${float(v):,.{n}f}'
pct = lambda v, n=1: '' if v in (None, '') else f'{float(v)*100:.{n}f}%'
num = lambda v, n=1: '' if v in (None, '') else f'{float(v):,.{n}f}'
OBJN = {'Full Push': 'Full push', 'Support': 'Support', 'Head Term (Capped)': 'Head term, capped', 'Capped Entry': 'Capped entry', 'Capped Long-Tail': 'Capped long tail', 'Brand Defense': 'Brand defence'}
K = D['K']; B1 = [k for k in K if k['b'] == 1]; B2 = [k for k in K if k['b'] == 2]; B3 = [k for k in K if k['b'] == 3]
REM = [k for k in K if k['b'] == 'Removed']
BS = D['BS']; OBJ = D['OBJ']; b1 = BS[0]; VS = D['VS']
OLD_T = {c[1]: c[2] for c in D['CH'] if c[0] == 'target'}; OLD_C = {c[1]: c[2] for c in D['CH'] if c[0] == 'cvr'}
SLTOS = {'cooling sheets queen': 2.16, 'cooling queen sheets': 4.46, 'queen cooling sheets': 3.19, 'queen bed sheets cooling': 3.87}
qp = sorted([k for k in B1 if k['obj'] == 'Full Push'], key=lambda x: -x['sv'])
import re as _re
path = lambda p: ', '.join(_re.findall(r'#\d+', str(p or ''))) or e(str(p or ''))

def tbl(head, rows, num_cols=(), tid=''):
    h = ''.join(f'<th class="{"n" if i in num_cols else ""}">{x}</th>' for i, x in enumerate(head))
    b = ''.join(('<tr>' if not isinstance(r, dict) else f'<tr data-o="{e(r["o"])}">') + ''.join(f'<td class="{"n" if i in num_cols else ""}">{c}</td>' for i, c in enumerate(r['c'] if isinstance(r, dict) else r)) + '</tr>' for r in rows)
    return f'<div class="tw"><table{(" id=" + chr(34) + tid + chr(34)) if tid else ""}><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
chip = lambda t, k='': f'<span class="chip {k}">{e(t)}</span>'

kpis = f'''<div class="kpis">
 <div class="kpi"><span class="lab">Campaigns on 15 Oct</span><span class="val">{b1[3]}</span><span class="sub">38 exact, 1 brand, 1 product targeting</span></div>
 <div class="kpi"><span class="lab">Targets</span><span class="val">{b1[2]} + 12</span><span class="sub">exact keywords and rival ASINs</span></div>
 <div class="kpi"><span class="lab">Planned spend a day</span><span class="val">{money(b1[7],0)}</span><span class="sub">budgets {money(b1[8],0)} a day</span></div>
 <div class="kpi"><span class="lab">Expected ACoS</span><span class="val">{pct(b1[9],0)}</span><span class="sub">Queen pushes {pct(OBJ[0][6],0)}, ceiling 63%</span></div>
</div>'''

brief = ''.join(f'<li>{t}</li>' for t in [
    'Lead with Queen. Eight Queen keywords get a full ranking push to <b>top 5 by week 8</b> (top 20 by week 2, top 10 by week 4), with the top of search bid at each keyword\'s ranking ceiling.',
    'Every other ranking keyword targets top 10. The head terms rank through Queen sales velocity; King, Full, Twin and Cal King run as capped probes until the size is assigned to CooLinens.',
    'Bids come from the market: Amazon\'s suggested median for this listing on every keyword, capped at our ranking ceiling. Sleephoria and Decolure are reference only.',
    f'Batch 1 plans about {num(b1[4],0)} clicks, {num(b1[5],1)} ad orders and {money(b1[6],0)} ad sales a day for {money(b1[7],0)} of spend.',
    'Batch 2 (40 keywords plus the other ad types) opens from 29 October when the Batch 1 gates pass. Batch 3 (6 keywords) runs in February to March with the re-order.'])

batches = tbl(['Batch', 'Go live', 'Keywords', 'Campaigns', 'Clicks a day', 'Orders a day', 'Ad sales a day', 'Spend a day', 'Budgets a day', 'Expected ACoS'],
              [[f'<b>Batch {r[0]}</b>' if r[0] != 'All' else '<b>All batches</b>', e({1: '15 Oct 2026', 2: 'From 29 Oct 2026, gated', 3: 'Feb to Mar 2027'}.get(r[0], '')), r[2], r[3], num(r[4]), num(r[5], 2), money(r[6], 0), money(r[7], 0), money(r[8], 0), pct(r[9])] for r in BS],
              num_cols=(2, 3, 4, 5, 6, 7, 8, 9))

method = '''<div class="method">
 <div><b>Base bid</b>Amazon's suggested median for this listing on the keyword (paused bid check campaign, 10 Oct), capped at the ranking ceiling.</div>
 <div><b>Ranking ceiling</b>Price x ranking ceiling ACoS (1.5 x break-even, Queen 62.9% at $87.99) x expected conversion: the most a click can cost and still pay for rank.</div>
 <div><b>Queen pushes</b>Top of search modifier in 25 point steps, up to +200%, so the top of search bid lands on the ceiling. Amazon's suggested high understates top of search cost on head terms.</div>
 <div><b>Clicks needed</b>Searches a day x market clicks per search x the click share a target rank takes (top 5: 4.3%, top 10: 2.8%) x the 66% paid share during a push.</div>
</div>'''

qrows = []
for k in qp:
    sl = SLTOS.get(k['kw'])
    st = chip('we bid above', 'ok') if sl and k['eff'] >= sl else (chip('sibling above our ceiling', 'bad') if sl else chip('no sibling price', 'mute'))
    qrows.append([e(k['kw']), f'{int(k["sv"]):,}', f'#{k["tr"]}', path(k['path']), num(k['req'], 1), num(k['clk'], 1), money(k['med']), money(k['ceil']), money(k['base']), f'+{k["mod"]}%', f'<b>{money(k["eff"])}</b>', st, money(k['bud'], 0)])
queen = tbl(['Keyword', 'Searches / mo', 'Target', 'Rank path (wk 2, 4, 8)', 'Clicks needed', 'Clicks planned', 'Amazon median', 'Ceiling', 'Base bid', 'Top of search', 'Top of search bid', 'Auction vs Sleephoria', 'Budget'], qrows, num_cols=(1, 2, 4, 5, 6, 7, 8, 9, 10, 12))

order = ['Full Push', 'Support', 'Head Term (Capped)', 'Capped Entry', 'Capped Long-Tail', 'Brand Defense']
grp = {o: sorted([k for k in B1 if k['obj'] == o], key=lambda x: -x['sv']) for o in order}
krows = [{'o': o, 'c': [e(k['kw']), e(k['size']), f'{int(k["sv"]):,}', OBJN[o], f'#{k["tr"]}', num(k['req'], 2), num(k['clk'], 2), pct(k['cvr']), money(k['med']), money(k['ceil']), f'<b>{money(k["base"])}</b>', (f'+{k["mod"]}%' if k['mod'] else '0%'), money(k['eff']), money(k['bud'], 0), e(k['sku'])]} for o in order for k in grp[o]]
filters = '<div class="filters" role="group" aria-label="Filter by objective"><button type="button" class="f on" data-f="all">All 52</button>' + ''.join(f'<button type="button" class="f" data-f="{e(o)}">{OBJN[o]} ({len(grp[o])})</button>' for o in order) + '</div>'
alltbl = filters + tbl(['Keyword', 'Size', 'Searches / mo', 'Objective', 'Target', 'Clicks needed', 'Clicks planned', 'Expected CVR', 'Amazon median', 'Ceiling', 'Base bid', 'Top of search', 'Top of search bid', 'Budget', 'Advertised child'], krows, num_cols=(2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), tid='kwt')
objt = tbl(['Objective', 'Targets', 'Clicks a day', 'Orders a day', 'Ad sales a day', 'Spend a day', 'Expected ACoS'],
           [[e(o[0].replace('Ranking — ', '').replace(' (Profitable Conversion)', '')), o[1], num(o[2]), num(o[3], 2), money(o[4]), money(o[5]), pct(o[6]) if o[6] else ''] for o in OBJ], num_cols=(1, 2, 3, 4, 5, 6))
patt = tbl(['Rival', 'Product', 'ASIN', 'Rival price', 'Our ad', 'Amazon median', 'Break-even cap', 'Bid'],
           [[e(p['brand']), e(p['prod']), f'<code>{p["asin"]}</code>', e(p['price']), e(p['sku']), money(p['med']), money(p['cap']), f'<b>{money(p["bid"])}</b>'] for p in D['PAT']], num_cols=(5, 6, 7))
removed = ''.join(f'<li><b>{e(k["kw"])}</b>: {e(str(k["note"]).split(". ", 1)[1] if ". " in str(k["note"]) else str(k["note"]))}</li>' for k in REM)

def btable(ks):
    return tbl(['Keyword', 'Size', 'Searches / mo', 'Objective', 'Target', 'Amazon median', 'Base bid', 'Advertised child'],
               [[e(k['kw']), e(k['size']), f'{int(k["sv"]):,}', OBJN.get(k['obj'], k['obj']), f'#{k["tr"]}', money(k['med']), money(k['base']), e(k['sku'])] for k in sorted(ks, key=lambda x: -x['sv'])], num_cols=(2, 4, 5, 6))

adtypes = tbl(['Ad type', 'Targeting', 'Bid basis', 'Budget a day', 'Read', 'Stop'], [
    ['Sponsored Display', 'Product-similar and views remarketing on Queen and King Graphite', 'Max acceptable ACoS x CVR (Queen about $1.47)', '$10', '30 clicks or 21 days', 'ACoS above break-even on 30 clicks'],
    ['Sponsored Brands video', 'TikTok demo footage on cooling sheets queen and cooling sheets; ranking exacts negated', 'Break-even per click', '$15', '30 clicks or 14 days', 'CVR under 60% of the SP top of search CVR on the same term'],
    ['Sponsored Brands collection', 'Queen colours on cooling sheets queen', 'Break-even per click', '$10', '30 clicks or 14 days', 'Same'],
    ['SP auto', 'Close match, Queen Graphite; every live exact negated', 'Max acceptable ACoS x CVR', '$10', 'Harvest weekly', 'ACoS above break-even on 40 clicks'],
    ['SP broad', 'Queen root and head root, each behind negative exact walls on every live exact', 'Max acceptable ACoS x CVR', '$10', 'Harvest weekly', 'Same']], num_cols=(3,))

# verification blocks
cost = tbl(['Size', 'Price', 'COGS (SellerBoard)', 'FBA fee', 'Referral 15%', 'Break-even ACoS', 'Ranking ceiling ACoS'],
           [[e(c[0]), money(c[1]), money(c[2]), money(c[3]), money(c[4]), pct(c[7]), pct(c[10])] for c in D['COST']], num_cols=(1, 2, 3, 4, 5, 6))
cvr_rows = []
for k, old in OLD_C.items():
    v = VR[k]; kk = next(x for x in K if x['kw'] == k)
    cvr_rows.append([e(k), f'Batch {kk["b"]}', pct(old), f'{v["sl_recent_clicks"]:,}', pct(v['sl_recent_orders'] / v['sl_recent_clicks']), f'<b>{pct(kk["cvr"])}</b>'])
cvrt = tbl(['Keyword', 'Batch', 'Lifetime basis', 'Clicks at $71 to $78', 'CVR at $71 to $78', 'Used (x 0.8)'], cvr_rows, num_cols=(2, 3, 4, 5))
vol_rows = []
for k in sorted(B1, key=lambda x: -x['sv'])[:12]:
    v = VR.get(k['kw'], {})
    if v.get('wsv'): vol_rows.append([e(k['kw']), f'{int(v["lw"]):,}', f'{v["wsv"]:,}', f'<b>{int(k["sv"]):,}</b>', pct(k['sv'] / v['lw'] - 1)])
volt = tbl(['Keyword', 'Seasonal estimate / mo', 'ASINsight weekly', 'Used: weekly x 4.33', 'Change'], vol_rows, num_cols=(1, 2, 3, 4))
tr_rows = []
for o in ['Full Push', 'Support', 'Head Term (Capped)', 'Capped Entry', 'Capped Long-Tail']:
    ks = grp[o]
    if not ks: continue
    olds = sorted({OLD_T.get(k['kw'], k['tr']) for k in ks})
    tr_rows.append([OBJN[o], len(ks), ', '.join('#' + str(x) for x in olds), f'<b>#{ks[0]["tr"]}</b>', path(ks[0]['path']), {'Full Push': 'Funded to 100% of the clicks the target needs, under the 10% supply cap', 'Support': 'Funded to its requirement', 'Head Term (Capped)': 'Ranks through Queen velocity; head exact capped at 3.57 clicks a day', 'Capped Entry': 'Target applies once the size is assigned; probe until then', 'Capped Long-Tail': 'Funded to its small requirement'}[o]])
trt = tbl(['Objective', 'Keywords', 'Target before review', 'Target', 'Rank path (wk 2, 4, 8)', 'Funding'], tr_rows, num_cols=(1,))
checks = ''.join(f'<li>{t}</li>' for t in [
    f'<b>Costs.</b> COGS taken from SellerBoard for every size (Queen $25.90, King $30.02, Cal King $31.62, Full $24.61, Twin $19.94). FBA uses the Amazon fee preview of 8 Oct, which runs $0.26 to $0.55 above the 28 Sep pricing sheet: the conservative choice.',
    '<b>Search volume.</b> The seasonal estimate ran 5% to 15% above the current market on the main terms (ASINsight, 6 Oct). Every keyword with a current read now uses it.',
    f'<b>Click share by rank.</b> Top 5 = 4.3% and top 10 = 2.8% of a page\'s clicks. Consistent with the sister listing at #3 (6.7%) and #4 (4.9%), and with the top 3 positions taking a median {VS["median_top3"]*100:.0f}% of clicks on the Batch 1 pages.',
    f'<b>Conversion.</b> The sister listing converted 10.5% on our Batch 1 terms at $71 to $78 (3,010 clicks); x 0.8 = 8.4%, against a plan average of {VS["wcvr"]*100:.1f}%. Nine keywords with 100+ clicks now use their price-matched rate; cooling sheets queen moves from 9.5% to 7.7%.',
    '<b>Target ranks.</b> Raised: Queen pushes to top 5, every other ranking keyword to top 10. Each full push is funded to 100% of what its target needs.',
    '<b>Ceilings and bids.</b> Every ceiling recomputed outside the workbook (price x ceiling ACoS x CVR) matches; every base bid and top of search bid sits at or under its ceiling.',
    '<b>Budgets.</b> Every campaign budget is at least its planned spend x 1.25, minimum $10.',
    f'<b>Upload file.</b> Generated from the workbook and checked line by line: {VS["lines"]} of {VS["lines"]} bids, modifiers and budgets match; the Amazon 21 point gate passes.'])

fmt = tbl(['Format', 'Sleephoria ACoS', 'Decolure ACoS', 'Use in this plan'], [
    ['Exact', '38%', '59%', 'Batch 1, ranking'], ['Product targeting', 'not run', '15% (2,488 orders)', 'Batch 1, premium rival pages'],
    ['Auto', '6% (290 orders)', '30%', 'Batch 2'], ['Phrase', '16%', '51%', 'Batch 2 harvest'], ['Broad', '21%', '204%', 'Batch 2, behind negative walls'], ['Branded', '14%', '', 'Batch 1, sheets brand terms']], num_cols=())
price = tbl(['Window', 'Sleephoria price', 'Ad conversion', 'What happened'], [
    ['Launch week, Oct 2025', '$61', '18.3%', '13 of 14 heads reached the top 10 in 6 to 20 days'], ['Jan 2026', '$66', 'about 5.5%', 'Trough: cooling sheets queen #5 to #67 on $53 a day; back to #11 in February'],
    ['Feb to May 2026', '$65', 'about 13%', 'Best stretch: TACoS 5%, ACoS 24.5%'], ['17 Aug to 9 Oct 2026', '$71 to $78', '10.5% on our terms', 'The basis for this plan\'s conversion']], num_cols=(1, 2))
split = tbl(['Size', 'Sleephoria rank today', 'Owner in this plan'], [
    ['Queen: cooling sheets queen, queen sheets cooling, queen cooling sheets', '#45, #64, #13', chip('CooLinens', 'ok')], ['King: king size cooling sheets, cooling sheets king size', '#4, #17', chip('Sleephoria', 'mute')],
    ['Twin: cooling sheets twin', '#5', chip('Sleephoria', 'mute')], ['Head: cooling sheets, cooling bed sheets', '#18, #18', chip('capped, ranks via Queen', 'warn')]])
rules = tbl(['When', 'Check', 'Pass', 'If it fails'], [
    ['15 Oct', 'All 40 campaigns serving; 48 product ads and 12 targets eligible; Sleephoria Queen stand down applied', 'Impressions on every ad group by evening', 'Fix eligibility the same day; escalate D1'],
    ['18 Oct, day 3', 'Top of search clicks on the 8 Queen pushes', 'At least 60% of planned clicks', 'Bids already at the ceiling: escalate the sibling overlap'],
    ['Weekly from 22 Oct', 'Planned against actual spend per campaign', 'Within 1.5 x plan', 'Trim any capped campaign over 1.5 x plan'],
    ['24 Oct, day 9', 'cooling sheets queen at 50 clicks', 'CVR at least 4.6% (60% of plan)', 'Modifier down one step; re-read at 100 clicks'],
    ['29 Oct, week 2', 'Rank path and Batch 2 gate', 'Queen pushes at #20 or better; Queen Graphite CVR 7% on 100 clicks; every probe read', 'Hold Batch 2 one week'],
    ['12 Nov, week 4', 'Rank path', 'Queen pushes at #10 or better', 'Diagnose by keyword: bid, placement, listing or stock'],
    ['10 Dec, week 8', 'Target', 'Queen pushes at #5 or better', 'Taper 15% to 25% a cycle once held 2 weeks'],
    ['Capped keyword at 50 clicks', 'Probe exit', 'CVR 7% or more: full push in Batch 2 once assigned', '4% to 7% hold; under 4% pause'],
    ['Any time', 'Listing rating', '4.0 or higher', 'Hold every scale verdict'],
    ['Late Nov', 'Black Friday and Cyber Monday', 'Bids held at the ceiling', 'Expect a rank dip; no deal badge in the first 60 days'],
    ['Dec to Jan', 'Low season floor', '$25 to $30 a day on Queen', 'Keep sales history; do not pay to hold rank'],
    ['October', 'Re-order', 'Purchase order decided', 'Stock runs out about April at half the sister pace']])
weekly = ''.join(f'<li><b>{a}</b> {b}</li>' for a, b in [('Scale:', 'CVR at plan, rank up 25% week on week, ACoS within the ceiling. Keep the bid; raise the budget if it capped out.'), ('Hold:', 'rank improving under 25% with CVR at plan. Check top of search share.'),
    ('Reduce:', 'ACoS over the ceiling for 2 weeks, or CVR under 60% of plan on 50 clicks. Modifier down one step, then the base 15% to 25%.'), ('Taper:', 'target held 2 weeks. Bids down 15% to 25% per cycle toward the profitable CPC.'),
    ('Stock:', 'advertised child under 21 days of cover. Switch to the backup child the same day.'), ('Escalate:', 'a verdict that repeats 4 cycles without its predicted effect is a diagnosis error.')])
dec = tbl(['#', 'Decision', 'Recommendation', 'Owner'], [
    ['D1', 'Size ownership and Sleephoria stand down', 'CooLinens owns Queen and no size terms; Sleephoria owns King, Twin, Cal King. Sleephoria top of search 0% and bids below CooLinens on the 8 Queen exacts for 8 weeks.', 'Erik'],
    ['D2', 'Ranking ceiling', '1.5 x break-even, capped at 80% (Queen 62.9% at $87.99)', 'Erik'], ['D3', 'Price', 'Launch at the Vine row (Queen $87.99), set 14 Oct evening; next step $97.99 Queen on 29 Oct if the Featured Offer and week 2 gates pass', 'Joseph (14 Oct)'],
    ['D4', 'Batch 2 ad types', 'Sponsored Display, Sponsored Brands, video, auto and broad with Batch 2 from 29 Oct, about $55 a day', 'Erik'],
    ['D5', 'Re-order', 'Decide in October so stock lands before Batch 3', 'Ali'], ['D6', 'Conversion basis', 'Sister listing conversion at today\'s price x 0.8 until CooLinens has its own read', 'Erik'], ['D7', 'Campaign naming', 'CLCS4 names as in the upload file', 'PPC team']])
risks = ''.join(f'<li>{t}</li>' for t in [
    'Sibling auction: Sleephoria pays more than our ceiling on cooling queen sheets ($4.46 against $4.18) and queen bed sheets cooling ($3.87 against $3.54), even at the launch price. Without D1 those two pushes cannot win top of search.',
    'Conversion: every expected rate is the sister listing\'s at today\'s price x 0.8. If CooLinens converts lower, the reduce rule and the day 9 read on cooling sheets queen act first.',
    'Price premium: CooLinens launches at $87.99 Queen against Sleephoria at $78.39 (October average), same knit. The listing and 167 Vine reviews carry the premium; conversion at this price is unproven until the day 9 read.',
    'Stock: 4,024 units and nothing inbound; Queen Graphite (373 units) carries every Queen push and switches to Cool Grey at 21 days of cover.',
    'Season: searches run at a quarter of the summer level, so rank is cheap but slow; the return comes in spring.'])


SD = json.load(open('/tmp/claude-0/cs/w/rebase/side_new.json'))
SIZES = ['Queen', 'King', 'Cal King', 'Full', 'Twin']
VINE = {'Queen': 97.99, 'King': 104.99, 'Cal King': 105.99, 'Full': 82.99, 'Twin': 76.99}
ec = SD['econ']
def erow(label, fn, fmtf):
    return [f'<b>{label}</b>'] + [fmtf(fn(sz)) for sz in SIZES]
econ_rows = [
    erow('Launch price', lambda z: ec[z][0], money), erow('COGS (SellerBoard)', lambda z: ec[z][1], money), erow('FBA fee', lambda z: ec[z][2], money),
    erow('Referral 15%', lambda z: ec[z][3], money), erow('Returns and storage allowance', lambda z: ec[z][4], money), erow('Margin a unit before ads', lambda z: ec[z][5], money),
    erow('Break-even ACoS', lambda z: ec[z][6], pct), erow('Target ACoS (0.5 x break-even)', lambda z: ec[z][7], pct), erow('Max acceptable ACoS (0.75 x)', lambda z: ec[z][8], pct),
    erow('Ranking ceiling ACoS (1.5 x, max 80%)', lambda z: ec[z][9], pct),
    erow('Next price step (29 Oct, if the gates pass)', lambda z: VINE[z], money),
    erow('Margin a unit at the next step', lambda z: VINE[z] - ec[z][1] - ec[z][2] - 0.15 * VINE[z] - ec[z][4], money),
    erow('Units on hand / at FBA', lambda z: SD['stock'][z], lambda v: f'{v[0]:,} / {v[1]:,}'),
    erow('Advertised child (FBA units)', lambda z: SD['pref'][z], lambda v: f'{e(v[0])} ({v[1]})'),
    erow('Days of cover at plan pace', lambda z: SD['pref'][z][2], lambda v: f'{float(v):.0f}'),
    erow('Batch 1 role', lambda z: z, lambda v: {'Queen': 'Full push, top 5', 'King': 'Capped probe', 'Cal King': 'Capped probe', 'Full': 'Capped probe', 'Twin': 'Capped probe'}[v]),
]
econ_side = tbl(['Per unit'] + SIZES, econ_rows, num_cols=(1, 2, 3, 4, 5))
srows = []
for k in sorted(SD['rows'], key=lambda x: (x['b'], ['Full Push','Support','Head Term (Capped)','Capped Entry','Capped Long-Tail','Brand Defense'].index(x['obj']) if x['obj'] in ['Full Push','Support','Head Term (Capped)','Capped Entry','Capped Long-Tail','Brand Defense'] else 9, -(x['sv'] or 0))):
    srows.append({'o': f'b{k["b"]}', 'c': [e(k['kw']), f'{k["b"]}', e(k['size']), OBJN.get(k['obj'], k['obj']),
        f'{int(k["mkl"]):,}' if k['mkl'] else '', f'{int(k["seas"]):,}' if k['seas'] else '', f'{int(k["wk"]):,}' if k['wk'] else '', f'<b>{int(k["sv"] or 0):,}</b>', num(k['spd'], 0), pct(k['mcvr']) if k['mcvr'] else '',
        num(k['mcd'], 0), pct(k['cs']) if k['cs'] else '', f'#{k["tr"]}', num(k['req'], 2), num(k['plan'], 2), pct(k['cvr']), num(k['ords'], 2), money(k['sales']),
        money(k['med']), money(k['ceil']), money(k['base']), (f'+{round(k["mod"]*100)}%' if k['mod'] else '0%'), money(k['eff']), money(k['spend']), money(k['bud'], 0), pct(k['acos']) if k['acos'] not in (None, '') else '']})
sfilters = '<div class="filters" role="group" aria-label="Filter by batch"><button type="button" class="g on" data-g="all">All 98</button>' + ''.join(f'<button type="button" class="g" data-g="b{b}">Batch {b} ({sum(1 for k in SD["rows"] if k["b"] == b)})</button>' for b in (1, 2, 3)) + '</div>'
side_tbl = sfilters + tbl(['Keyword', 'Batch', 'Size', 'Objective', 'MKL / mo', 'Seasonal est. / mo', 'ASINsight weekly', 'Used / mo', 'Searches / day', 'Market CVR', 'Market clicks / day', 'Click share at target', 'Target', 'Clicks needed', 'Clicks planned', 'Expected CVR', 'Orders / day', 'Ad sales / day', 'Amazon median', 'Ceiling', 'Base bid', 'Top of search', 'Top of search bid', 'Spend / day', 'Budget', 'Expected ACoS'],
    srows, num_cols=tuple(range(4, 26)), tid='sidet')

css = open('/tmp/claude-0/cs/w/page_css.txt').read()
page = f'''<title>CooLinens Sheets Launch Plan</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{css}</style>
<div class="wrap">
<nav class="idx" aria-label="Sections">
 <a href="#top">Overview</a><a href="#batches">The three batches</a><a href="#b1">Batch 1</a><a href="#queen">Queen pushes</a><a href="#all">Batch 1 keywords</a><a href="#pat">Product targeting</a>
 <a href="#b2">Batch 2</a><a href="#b3">Batch 3</a><a href="#side">Side by side</a><a href="#verify">Verification</a><a href="#evidence">Evidence</a><a href="#tracking">Launch tracking</a><a href="#decisions">Decisions</a><a href="#risks">Risks</a>
</nav>
<main>
<header id="top">
 <div class="eyebrow">CooLinens · Cooling Sheets 4 Piece · Amazon US · PPC launch 15 Oct 2026</div>
 <h1>CooLinens Cooling Sheets launch plan</h1>
 <p class="lede">The PPC plan for the 15 October launch, in three batches. Bids are set by the market for this listing, targets are sized to where the clicks are, and every number has been checked against its source and against the upload file.</p>
 <div class="status">{chip('Upload file matches the workbook: ' + str(VS['lines']) + ' of ' + str(VS['lines']), 'ok')}{chip('Workbook: 5,483 formulas, 0 errors', 'ok')}{chip(str(VS['cnt']['PASS'] + VS['cnt']['UPDATED']) + ' input checks, 0 failures', 'ok')}{chip('D1 Sleephoria stand down: awaiting sign off', 'warn')}</div>
 {kpis}
 <h3>The plan in brief</h3><ol class="five">{brief}</ol>
</header>

<section id="batches"><h2>The three batches</h2>{batches}
<p class="note">Batch 1 includes the product targeting and brand campaigns. Batches 2 and 3 carry the same rules and are re-priced from their own Amazon suggested bids (already captured) when they open.</p></section>

<section id="b1"><h2>Batch 1 · 15 October 2026</h2>
<p>52 exact keywords in 38 keyword campaigns, the sheets brand campaign and one product targeting campaign on 12 rival pages. Exact match and fixed bids; no auto on day 1.</p>
<h3>How bids are set</h3>{method}
</section>

<section id="queen"><h3 class="h2like">The eight Queen pushes</h3>
<p class="note">Auction vs Sleephoria compares our top of search bid with what Sleephoria paid at top of search on the same term (10 Sep to 9 Oct 2026, reference).</p>
{queen}
<p class="note">cooling sheets queen alone needs about 15 clicks a day to reach top 5: the largest single line in Batch 1 at about $65 a day at the launch price. Two pushes cannot clear the sibling within our ceiling, which is decision D1.</p>
</section>

<section id="all"><h3 class="h2like">All Batch 1 keywords</h3>
<p class="note">Filter by objective. Clicks needed = what the target rank requires; clicks planned = what the campaign is funded for.</p>
{alltbl}
<h3>Batch 1 by objective</h3>{objt}
<h3>Kept out of the plan</h3><ul class="plain">{removed}</ul>
</section>

<section id="pat"><h3 class="h2like">Product targeting on rival pages</h3>
<p class="note">One campaign at $20 a day, Queen and King ad groups. Every target is priced above our $87.99 to $93.99, except the $89.90 to $89.99 Queen pages, now within $2 of us. Bid = Amazon median, capped at break-even per click at 8% conversion. Read at 30 clicks per ASIN or 21 days; pause an ASIN with no order after 25 clicks.</p>
{patt}
<h3>Brand</h3><p>coolinens cooling sheets and coolinens sheets, exact, $1.50, $10 a day. coolinens on its own belongs to the live pillowcase brand campaign and is not used here.</p>
</section>

<section id="b2"><h2>Batch 2 · from 29 October 2026, gated</h2>
<p><b>Opens when:</b> Queen Graphite converts at 7% or more on 100 clicks, the Queen pushes reach #20 or better and are improving, and every capped probe has its 50 click read.</p>
<p>40 exact keywords: the next tier of Queen and no size wording, colour terms, and the King, Full, Twin and Cal King terms that become full pushes once their size is assigned to CooLinens. The other ad types open with it at about $55 a day.</p>
{adtypes}
<details><summary>All 40 Batch 2 keywords</summary>{btable(B2)}</details>
</section>

<section id="b3"><h2>Batch 3 · February to March 2027</h2>
<p>6 keywords with generic or seasonal wording (bed sheets cooling, best sheets for hot sleepers), launched with the second sized push before the April to July peak, when CooLinens has its own conversion and the re-order has landed.</p>
{btable(B3)}
</section>

<section id="side"><h2>Side by side</h2>
<h3>Economics by size</h3>
<p class="note">Margin = price minus COGS, FBA fee, 15% referral and a $3.50 returns and storage allowance. The ceilings set the most a click can cost.</p>
{econ_side}
<h3>Every keyword: demand, clicks, conversion, bids and spend</h3>
<p class="note">Used / mo is the search volume the plan runs on (ASINsight weekly x 4.33 where available). Clicks needed = market clicks a day x click share at the target rank x 66% paid share. Filter by batch; the table scrolls sideways.</p>
{side_tbl}
</section>

<section id="verify"><h2>Verification</h2>
<p class="note">Every input checked against its source on 10 October 2026. Full detail on the Verification tab of the workbook.</p>
<ul class="plain">{checks}</ul>
<h3>Target ranks by objective</h3>{trt}
<h3>Costs, margin and ceilings by size</h3>{cost}
<h3>Conversion re-based to today's price</h3>{cvrt}
<h3>Search volume: seasonal estimate against the current market (largest Batch 1 terms)</h3>{volt}
</section>

<section id="evidence"><h2>Evidence used for judgement</h2>
<p class="note">Sleephoria (same product) and Decolure (adjacent product) are reference and context, not limits.</p>
<h3>Cheapest orders by format</h3>{fmt}
<h3>Price and conversion on the sister listing</h3>{price}
<h3>Who holds which size today</h3>{split}
</section>

<section id="tracking"><h2>Launch tracking</h2>{rules}
<h3>Weekly rule for every ranking keyword, from week 2</h3><ul class="plain">{weekly}</ul></section>

<section id="decisions"><h2>Decisions requested</h2>{dec}</section>
<section id="risks"><h2>Risks</h2><ul class="plain">{risks}</ul>
<h3>Files</h3><ul class="plain files"><li>Upload: <code>COOLINENS_Cooling_Sheets_4PC_Batch1_Launch_Bulk_20261015.xlsx</code></li><li>Workbook: <code>CooLinens_Cooling_Sheets_4PC_Launch_Strategy.xlsx</code></li><li>Bid check exports: <code>deliverables/coolinens-cooling-sheets/bid-check/</code></li></ul></section>
</main></div>
<script>
(function(){{
  var btns=document.querySelectorAll('.f'), rows=document.querySelectorAll('#kwt tbody tr');
  btns.forEach(function(b){{ b.addEventListener('click',function(){{
    btns.forEach(function(x){{x.classList.toggle('on',x===b)}});
    var f=b.getAttribute('data-f');
    rows.forEach(function(r){{ r.hidden = !(f==='all' || r.getAttribute('data-o')===f); }});
  }}); }});
  var gb=document.querySelectorAll('.g'), sr=document.querySelectorAll('#sidet tbody tr');
  gb.forEach(function(b){{ b.addEventListener('click',function(){{
    gb.forEach(function(x){{x.classList.toggle('on',x===b)}});
    var f=b.getAttribute('data-g');
    sr.forEach(function(r){{ r.hidden = !(f==='all' || r.getAttribute('data-o')===f); }});
  }}); }});
}})();
</script>
'''
for ch in '—–≥≤→×':
    assert ch not in page, ch
open('/tmp/claude-0/cs/w/rebase/plan_only.html', 'w').write(page)
print(len(page))
