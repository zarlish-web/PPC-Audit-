"""Per-campaign issue detectors: compare each engine row with what the document requires,
on that campaign's own keyword, placement and budget data."""
import re

PREV_HELD = {  # previous run's review (2026-09-19) held or corrected these same levers
    'DBS4-SP-Bamboo Cooling Sheets-(MSV)-Exact-(Ranking)-DO-BAMBOO-QUEEN-WHITE': ('hold', '718 → 795 held: open record 2150 AHEAD, budget-bound in the deal, 795% over the 500% cap'),
    'DBS4-SP-Cal King Bamboo Sheets-[Bamboo|California King]-(VLSV)-Exact-(Ranking)-DO-BAMBOO-CALIFKING-WHITE': ('correct', '276 → 455 corrected to 389 (+30% step); hero had 61 units, no dated arrival'),
    'DBS4-SP-Bed Sheets Bamboo King-(VLSV)-Exact-(Ranking)-DO-BAMBOO-KING-WHITE': ('hold', '213 → 241 held: record 2113 AHEAD to 2026-10-05; effective TOS $5.95 already over the $4.60 market bound'),
    'DBS4-SP-Queen Size Bamboo Sheets-[Bamboo|Queen]-(LSV)-Exact-(Ranking)-DO-BAMBOO-QUEEN-WHITE': ('hold', '238 → 338 held: 71 impressions in 90 days — check eligibility before price'),
}


def pct(x):
    return '—' if x is None else f'{x:.0%}'


def usd(x):
    return '—' if x is None else f'${x:,.2f}'


def trunc(t, n=300):
    t = re.sub(r'\s+', ' ', t or '').strip()
    if len(t) <= n:
        return t
    cut = t[:n]
    k = max(cut.rfind('. '), cut.rfind('; '))
    if k > n * 0.5:
        return cut[:k + 1] + ' …'
    return cut[:cut.rfind(' ')] + ' …'


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def detect(a):
    J, X, sh, ceil = a['J'], a['X'], a['share'], a['ceil']
    out = []
    ch = a['changes']
    tos, pp, ros = X['tos'], X['detail'], X['other']
    kinds = {r['kind'] for r in ch}
    tos_rows = [r for r in ch if r['kind'] == 'tos']
    bid_rows = [r for r in ch if r['kind'] == 'bid']
    bud_rows = [r for r in ch if r['kind'] == 'budget']
    ranking = a['obj'] == 'Ranking'

    def add(code, title, what, why, issue, fix, rows=None, sev='High'):
        out.append(dict(code=code, title=title, what=what, why=why, issue=issue, fix=fix,
                        rows=rows or [], sev=sev))

    seqs = lambda rs: ', '.join(str(r['seq']) for r in rs)

    # --- 1. rank collapse freeze with moves on it
    if a['frozen'] and ch:
        add('FREEZE', 'Levers moved on a campaign under a rank-collapse freeze',
            f"The engine's own rank-freeze list names this campaign, yet rows {seqs(ch)} change it.",
            'The freeze says every bid, modifier and budget write holds until the cause of the collapse is named.',
            'Doc §12: rank collapsing >10 positions despite delivery — never scale spend; check listing, the rival now ahead, then whether it is category-wide.',
            'Hold every price and budget row on this campaign; keep negatives. Re-open only once the cause is written on the row.', ch)

    # --- 2. withheld-in-text but exported as change
    wh = [r for r in ch if r.get('withheld')]
    if wh:
        add('WITHHELD', 'Rows the rationale withholds are exported as changes',
            f"Rows {seqs(wh)} carry verdict 'change', but their RISKS section reads 'change → HOLD' because the rank claim is UNGRADEABLE.",
            'The engine requires a gradeable rank claim for a ranking move; with none it withholds the change.',
            'The export and the rationale disagree — the loader would deploy a move the engine itself refused. This is an engine defect (a row with no gradeable prediction), not a judgement call.',
            'Remove these rows from the deploy (verdict HOLD). Re-open when a rank observation exists for the term.', wh, 'Critical')

    # --- 3. previous review held / corrected the same lever
    pv = PREV_HELD.get(a['name'])
    if pv and tos_rows:
        r = tos_rows[0]
        add('HISTORY', "Re-proposes a move last week's review held",
            f"Row {r['seq']} proposes the top-of-search modifier {r['now']}% → {r['to']}%.",
            f"Previous review (run 20260919-20efcefa): {pv[1]}.",
            'The same lever comes back without the condition that held it having been read (the open tuner record / the deal guard are still running).',
            'Hold until the open record is graded after the deal (2026-09-28) — or, if re-proposed, apply at most the previous corrected size.', [r])

    # --- 4. deal contamination: checkpoints inside the deal, rates including deal days
    dd = a['WD']
    d_clicks = sum(dd[k]['c'] for k in ('tos', 'detail', 'other'))
    all90 = sum(a['W90'][k]['c'] for k in ('tos', 'detail', 'other'))
    in_deal = [r for r in ch if re.search(r'checkpoint 2026-09-(1[5-9]|2[0-8])', r.get('claim') or '')]
    if ch and (in_deal or d_clicks):
        share_deal = d_clicks / all90 if all90 else 0
        dd_cvr = (dd['tos']['o'] / dd['tos']['c']) if dd['tos']['c'] else None
        ex_cvr = (tos['o'] / tos['c']) if tos['c'] else None
        add('DEAL', 'Reads and checkpoints sit inside the Best Deal (2026-09-15 → 09-28)',
            f"{d_clicks} of this campaign's {all90} ninety-day clicks ({share_deal:.0%}) fell in the six deal days read; TOS CVR in the deal {pct(dd_cvr)} vs {pct(ex_cvr)} ex-deal."
            + (f" Checkpoints of rows {seqs(in_deal)} fall on dates inside the deal." if in_deal else ''),
            "The engine read no deal ('engine_read: null'; the workbook Summary says 'No deal in the window').",
            "Doc §12: a deal week inside the window contaminates every rate and voids the read until resolved. Rank 'now' (2026-09-20) is itself an in-deal reading.",
            'Price on the ex-deal window (06-23 → 09-14, used throughout this document). Move every checkpoint to data from 2026-09-29 onwards (first read 2026-10-06); grade no step on deal days.',
            ch, 'High')

    # --- 5. read-floor misstatement
    mis = [r for r in ch if 'under the 15-click read floor' in (r.get('text_flags') or '') ]
    if a.get('floor_misstated'):
        add('FLOOR', 'Read floor mis-stated: engine uses 100 clicks and calls it "15"',
            f"The rationale says top of search 'carries {a['floor_misstated']} clicks in 90 days, under the 15-click read floor'.",
            "The engine's own floor is 100 clicks ('the read floor is ... 100 clicks ÷ 22 days').",
            f"Doc §3: 15 clicks is the floor, a blend from 15 to 50, own rate from 50. At {tos['c']} ex-deal TOS clicks this campaign's own rate {'carries full weight' if tos['c'] >= 50 else 'is blended in'}; it is readable.",
            f"Price on the blended rate: {a['why_rate']['tos']} → TOS ceiling {usd(ceil['tos'])}.", ch, 'Medium')

    # --- 6. base cut when PP ≤ 20%, or missing when PP > 20%
    cuts = [r for r in bid_rows if fnum(r['to']) is not None and fnum(r['now']) and fnum(r['to']) < fnum(r['now'])]
    raises = [r for r in bid_rows if fnum(r['to']) is not None and fnum(r['now']) and fnum(r['to']) > fnum(r['now'])]
    if ranking and a['tot'] >= 15 and sh['detail'] is not None:
        if sh['detail'] <= 0.20 and cuts and not any('TAPER' in (r.get('engine') or '') for r in cuts):
            add('BASE-CUT-NOT-OWED', 'Base cut on a campaign whose mix is already right',
                f"Rows {seqs(cuts)} cut the base while product pages take {pct(sh['detail'])} of ex-deal clicks ({pp['c']} of {a['tot']}).",
                'Rationale cites the distribution fix.',
                'Doc §10: under 20% product pages the base is doing its job — no reason to touch it. A cut here only thins delivery.',
                f"Hold the base at {usd(a['base'])}; if a price move is owed it is at top of search via the modifier.", cuts)
        if sh['detail'] > 0.20 and not cuts and not a['frozen']:
            add('BASE-CUT-MISSING', 'Product pages over 20% and the base is not cut',
                f"Product pages take {pct(sh['detail'])} of ex-deal clicks ({pp['c']} of {a['tot']}, {pp['o']} orders at {usd(a['cpc']['detail'])} CPC).",
                'The engine held the base' + (' (hold rationale: "nothing to correct")' if not bid_rows else '') + '.',
                'Doc §5/§12: product pages must sit at or under 20% — always; above it, cut the base and re-solve the modifier so the TOS price holds.',
                f"Base {usd(a['base'])} → {usd(J['base'])} ({J['base_why']}); TOS price held at {usd(J['price'])} with modifier {J['mod']}%.",
                [], 'High')
    if cuts and a['tot'] < 15 and ranking:
        add('BASE-CUT-NO-DELIVERY', 'Base cut on a row that is not delivering',
            f"Rows {seqs(cuts)} cut the base; the campaign took {a['tot']} clicks in 84 ex-deal days (TOS {tos['c']}, PP {pp['c']}, ROS {ros['c']}).",
            trunc(cuts[0].get('decision'), 250),
            'Doc §10/§12: whether clicks are arriving at all — none arriving means there is no distribution to fix; hold the base and move the modifier only. Cutting the base of a row that is not delivering makes delivery worse.',
            f"Hold the base at {usd(a['base'])}.", cuts)
    if raises:
        add('BASE-RAISE', 'Base raised',
            f"Rows {seqs(raises)} raise the base ({', '.join(r['now'] + '→' + r['to'] for r in raises)}).",
            trunc(raises[0].get('decision'), 300),
            'Doc §10: a base goes up only when the derived price moved (15-click crossing, child change, contribution change, correcting an inherited bid below what product pages afford) — cap 25%. It is not a way to buy clicks.',
            f"Keep the base unless it is below what product pages afford ({usd(ceil['detail'])}); here base {usd(a['base'])} vs PP ceiling {usd(ceil['detail'])}.", raises, 'Medium')

    # --- 7. TOS price moves
    if tos_rows and a['price_now'] and a['price_eng']:
        r = tos_rows[0]
        up = a['price_eng'] > a['price_now'] * 1.001
        step = a['price_eng'] / a['price_now'] - 1
        if up and J['mix_first']:
            add('CLIMB-MIX-FIRST', 'Price climb on a campaign whose top of search is under 30% of clicks',
                f"Row {r['seq']}: TOS {usd(a['price_now'])} → {usd(a['price_eng'])} (+{step:.0%}); TOS carries {pct(sh['tos'])} of ex-deal clicks.",
                trunc(r.get('decision'), 300),
                'Doc §12/§14: below 30% at top of search the distribution fix takes precedence — no price climb and no budget move until the mix is corrected.',
                f"No climb. Base {usd(a['base'])} → {usd(J['base'])}; TOS held at {usd(a['price_now'])} (modifier re-solved to {J['mod']}%).", [r])
        if up and not J['push_case']:
            why = []
            if not a['in_focus']:
                why.append('out of focus (taper)')
            if a['rank_now'] is None:
                why.append('no rank on file')
            if J['hero_bad']:
                why.append('advertised hero cannot sustain a push')
            if a['frozen']:
                why.append('rank collapse freeze')
            if a['obj'] != 'Ranking':
                why.append(f"objective {a['obj']}")
            if 'Exact' not in a['name']:
                why.append('not an exact row')
            if a['price_eng'] > ceil['tos'] * 1.02:
                add('PREMIUM-UNFUNDED', 'Top of search priced above its ceiling on a row that is not a push',
                    f"Row {r['seq']}: TOS {usd(a['price_now'])} → {usd(a['price_eng'])} against a TOS ceiling of {usd(ceil['tos'])} ({a['why_rate']['tos']}); why not a push: {', '.join(why) or 'fails a push property'}.",
                    trunc(r.get('decision'), 300),
                    f"Doc §8/§11: only a funded Ranking-Exact push may price top of search above what it affords; everything else is bounded at every placement. Loss per order at {usd(a['price_eng'])}: {usd(a['price_eng'] / a['rate']['tos'] - a['contrib'])}.",
                    f"TOS price {usd(J['price'])} ({'; '.join(J['write_kind'])}); modifier {J['mod']}% on base {usd(J['base'])}.", [r])
        if up and step > 0.301:
            add('CLIMB-CAP', 'Climb larger than the 30% per-write cap',
                f"Row {r['seq']}: TOS price +{step:.0%} in one write ({usd(a['price_now'])} → {usd(a['price_eng'])}).",
                trunc(r.get('decision'), 300),
                'Doc §10: top-of-search climb 20–30% of the current price per write; no single move so large it cannot be attributed.',
                f"Cap at +30%: {usd(a['price_now'] * 1.30)}.", [r])
        if up and J['push_case'] and not J.get('premium_ok') and a['price_eng'] > ceil['tos'] * 1.02:
            c = J['conditions']
            miss = [n for n, v in (('funded', J['funded']), ('CTR above market', c['ctr']), ('CVR above market', c['cvr'])) if not v]
            add('PUSH-UNPROVEN', 'Premium climb above the ceiling on a push that does not meet the document\'s tests',
                f"Row {r['seq']}: TOS {usd(a['price_now'])} → {usd(a['price_eng'])} against a TOS ceiling of {usd(ceil['tos'])}. Not shown: {', '.join(miss)}. "
                + (f"Requirement {J['req_day']:.1f} TOS clicks/day × {usd(a['price_now'])} = {usd(J['need_budget'])}/day against a {usd(a['budget'])} budget. " if J['req_day'] else 'No click requirement on file. ')
                + f"TOS CTR {pct(a['tos_ctr'])} vs market {a['mkt_ctr'] if a['mkt_ctr'] is not None else '—'}%; TOS CVR {pct(a['rate']['tos'])} vs market {a['mkt_cvr'] if a['mkt_cvr'] is not None else '—'}%.",
                trunc(r.get('decision'), 300),
                'Doc §6: a premium needs velocity, click-through above market, conversion above market and stock after — any missing and the term takes maintenance (ceiling, no premium). Doc §11: sized, dated, ceilinged, predicted, funded — miss one and the row is priced inside the ceiling with the reason named; an unfunded push is stated as a dollar shortfall.',
                (J['budget_why'] or '') + f" Write: {'; '.join(J['write_kind'])} at {usd(J['price'])}.", [r])
        if not up and a['price_eng'] < a['price_now'] * 0.98:
            cut = 1 - a['price_eng'] / a['price_now']
            if J['push_case'] and J['below70'] and not a['frozen']:
                add('CUT-BEFORE-70', 'Top-of-search price cut on a push that never received its clicks',
                    f"Row {r['seq']}: TOS {usd(a['price_now'])} → {usd(a['price_eng'])} (−{cut:.0%}); delivery {a['tos_wk']:.1f}/wk vs plan {a['plan_wk']}/wk.",
                    trunc(r.get('decision'), 300),
                    'Doc §14: no cut to the TOS price until the push has delivered 70% of required clicks with PP under 20%. Below that: continue, fix delivery, or stop on the dated loss ceiling.',
                    f"{'; '.join(J['write_kind'])} at {usd(J['price'])}.", [r])
    # TOS price falling as a residue of a base cut
    if cuts and not tos_rows and a['tos_mod'] and a['price_now'] and a['price_eng'] and a['price_eng'] < a['price_now'] * 0.99:
        add('RESIDUE', 'TOS price falls as a by-product of the base cut',
            f"Rows {seqs(cuts)} cut the base, the modifier is not re-solved: TOS {usd(a['price_now'])} → {usd(a['price_eng'])}.",
            trunc(cuts[0].get('engine') or cuts[0].get('decision'), 300),
            'Doc §9/§17: the TOS price never falls as a residue of a base cut. If it comes down, that is its own decision landing on a named point.',
            f"Either re-solve the modifier to hold TOS at {usd(a['price_now'])} ({round((a['price_now'] / fnum(cuts[0]['to']) - 1) * 100)}% on the new base), or name the point it descends to (the TOS ceiling {usd(ceil['tos'])}).", cuts)

    # --- 8. modifiers above caps
    mods = [r for r in tos_rows if fnum(r['to']) and fnum(r['to']) > 500]
    if mods:
        add('MOD-CAP', 'Modifier above the 500% working cap',
            f"Rows {seqs(mods)} write {', '.join(r['to'] + '%' for r in mods)}.", '', 'Doc §8: 900% is the platform wall; the account routes >500% to a person. A very high modifier on a low base means the base is not where product-page economics put it — state the trade.',
            'Route to a person; show both prices on the row.', mods, 'Medium')

    # --- 9. ROS / PP
    for r in [x for x in ch if x['kind'] == 'ros']:
        earned = ros['c'] >= 15 and ros['c'] and (ros['o'] / ros['c']) >= (a['rate']['detail'] or 0)
        if not earned:
            add('ROS-OK', 'Rest-of-search modifier to zero — agrees with the document',
                f"Row {r['seq']}: {r['now']}% → {r['to']}%. ROS ex-deal {ros['c']} clicks, {ros['o']} orders ({pct(ros['o'] / ros['c'] if ros['c'] else None)}) vs product-page rate {pct(a['rate']['detail'])}.",
                '', 'Doc §8 item 10: ROS sits at zero until 15+ clicks convert at or above the product-page rate (a switch, not a blend).', 'Keep.', [r], 'OK')
    for r in [x for x in ch if x['kind'] == 'pp']:
        add('PP-OK', 'Product-page modifier to zero — agrees with the document',
            f"Row {r['seq']}: {r['now']}% → {r['to']}%.", '', 'Doc §1: product pages are priced by the base alone.', 'Keep.', [r], 'OK')

    # --- 10. budgets
    for r in bud_rows:
        t = r.get('text') or ''
        util = re.search(r'spend \$([\d.]+) of \$([\d.]+)/day = (\d+)% utilisation', t)
        u = int(util.group(3)) if util else None
        taper = 'TAPER' in t
        issue = []
        if u is not None and u < 95:
            issue.append(f'{u}% utilisation is not exhaustion (and it is measured on deal-inflated days)')
        if taper:
            issue.append('the same campaign is on the taper — the engine raises and releases it in one run')
        if J['mix_first']:
            issue.append('TOS under 30% — no budget move until the mix is fixed')
        req = re.search(r'Sized as ([\d.]+) clicks needed/day', t)
        plan = re.search(r'leaves PPC ([\d.]+) clicks/wk', t)
        chain = re.search(r'= (\d+) paid clicks/wk', t)
        if req and plan and float(req.group(1)) * 7 > 1.5 * float(plan.group(1)):
            issue.append(f"sized on {float(req.group(1)):.1f} clicks/day = {float(req.group(1))*7:.0f}/wk while the TARGET section asks {plan.group(1)}/wk" + (f" (chain {chain.group(1)}/wk)" if chain else ''))
        pre = J['pre_spend']
        add('BUDGET', 'Budget raise not supported by the campaign\'s own read' if issue else 'Budget raise',
            f"Row {r['seq']}: ${r['now']} → ${r['to']}/day. Pre-deal spend {usd(pre)}/day; 14-day (deal-inflated) {usd(a['spend_day'])}/day.",
            trunc(r.get('decision'), 250) + ' | ' + trunc(r.get('engine'), 250),
            ('; '.join(issue) + '. Doc §6/§12: budget is raised only when the campaign ran out of money; otherwise the question is price (share low) or demand (share high).') if issue else 'Consistent with doc §12 on its face.',
            'Hold the budget at $' + r['now'] + ('/day' if issue else '/day unless ex-deal days show the campaign capping out.'),
            [r], 'High' if issue else 'OK')

    # --- 11. bid strategy
    if a['bid_strategy'] == 'AUTO_FOR_SALES' and ranking:
        add('STRATEGY', 'Up-and-down bidding on a ranking push',
            f"Bid strategy AUTO_FOR_SALES (dynamic up and down): Amazon may lift the TOS bid by up to 100%, so the {usd(a['price_eng'] or a['price_now'])} written price can clear at up to {usd((a['price_eng'] or a['price_now']) * 2)}. It already does: ex-deal TOS CPC {usd(a['cpc']['tos'])} against today's written TOS price {usd(a['price_now'])}.",
            "The engine prices as if the written price were the ceiling ('authorized ceiling $13.39 → $16.23').",
            f"Doc §8: the market bound and the per-unit bound must hold on every click. {usd((a['price_eng'] or a['price_now']) * 2)} is above the TOS ceiling {usd(ceil['tos'])} and the unit's contribution {usd(a['contrib'])}.",
            'Switch to fixed bids (doc §10: fixed while launching/re-launching, or as the last-resort trade) or down-only, then write the TOS price.', [], 'High')

    # --- 12. hero stock
    if J['hero_bad'] and ch and a['child_after'] == 'hold':
        st = a['stock']
        add('STOCK', 'Push on a hero that cannot ship through the window',
            f"Campaign advertises {a['serving']}; {st['size']} hero reads {st.get('hero_room') or 'under horizon'} — {trunc(st['why'].split('read on the SERVING child')[-1], 330)}",
            'The engine rides the push under the size pick while the advertised child stays on the hero.',
            'Doc §12: the serving child cannot ship → every read is void; §6: a position taken then lost to a stockout is rented, not bought.',
            f"Re-point the ad to the serving child {st['serving_child']} ({st['serving_available']} available) before any price climb, or hold the price.", ch)

    # --- 13. prediction realism
    for r in tos_rows:
        m = re.search(r'claim asks x([\d.]+) what steps this size have bought', r.get('text') or '')
        rc = re.search(r'rank (\d+) now → ≤ (\d+) by', r.get('claim') or '')
        big = rc and int(rc.group(1)) - int(rc.group(2)) >= 15
        if (m and float(m.group(1)) >= 2) or big:
            add('PREDICTION', 'Prediction the step cannot deliver',
                (f"Row {r['seq']}: mechanism claim asks x{m.group(1)} what steps this size have bought. " if m else f"Row {r['seq']}: ")
                + (f"Rank claim {rc.group(1)} → ≤{rc.group(2)} in 14 days." if rc else ''),
                "The engine files the plan's requirement as the step's prediction.",
                'Doc §11: the prediction is the written expectation of THIS step; account hit rate on graded predictions is 4.8% (5 of 104). A claim sized from the plan grades as a miss even when the step is right, and teaches nothing.',
                "Predict what the step buys (the book's rate for this size), dated to post-deal data; keep the plan as the destination.", [r], 'Medium')
    # --- 14. premium rows with no dollar loss ceiling
    prem = [r for r in tos_rows if r.get('loss')]
    if prem and not any('loss ceiling' in (r.get('text') or '') for r in prem):
        r = prem[0]
        add('CEILINGED', 'Premium written with no dollar loss ceiling',
            f"Row {r['seq']}: loss ${r['loss']}/order stated, no weekly loss ceiling.", '',
            'Doc §7/§11: loss ceiling = that week\'s spend at risk, in dollars, at the spend the push needs. Without it the push cannot be stopped on a dated number.',
            f"Write it: required {J['req_day'] or 0:.1f} clicks/day × {usd(J['price'])} × 7 = {usd((J['req_day'] or 0) * (J['price'] or 0) * 7)}/week at risk.", [r], 'Medium')
    # --- 14b. bid row labelled with a different keyword than the target it changes
    lab = []
    for r in bid_rows:
        lbl = r['entity'].replace('target · ', '')
        tg = [t for t in a['targets'] if t['label'] == lbl]
        if tg and not any(abs((t['bid'] or 0) - (fnum(r['now']) or -1)) < 0.005 for t in tg):
            real = [t['label'] for t in a['targets'] if abs((t['bid'] or 0) - (fnum(r['now']) or -1)) < 0.005 and t['bid_to'] is not None]
            lab.append((r, real))
    if lab:
        add('LABEL', 'Bid row names a different keyword from the one it changes',
            '; '.join(f"Row {r['seq']} is labelled '{r['entity'].replace('target · ', '')}' at ${r['now']}, but that keyword bids ${next(t['bid'] for t in a['targets'] if t['label']==r['entity'].replace('target · ', ''))}; the target at ${r['now']} is " + (', '.join(repr(x) for x in real) or 'another keyword') for r, real in lab) + '.',
            'The row carries the plan keyword as its entity label.',
            'A reviewer reading the row judges the wrong keyword — here a 0-click keyword is presented as the campaign\'s head term.',
            'Label rows by the target they change (the entity id is correct; the label is not).', [x[0] for x in lab], 'Medium')
    # --- 15. no-op rows and duplicate target rows
    noop = [r for r in ch if str(r['now']) == str(r['to'])]
    if noop:
        add('NOOP', 'Row changes nothing', f"Rows {seqs(noop)}: {', '.join(str(r['now']) + ' → ' + str(r['to']) for r in noop)}.",
            trunc(noop[0].get('decision'), 200),
            "The code check 'value' is meant to confirm the proposal actually moves the value — it passed a row that does not.",
            'Drop from the deploy (the campaign is already in the target state); fix the code check.', noop, 'Medium')
    seen = {}
    dups = []
    for r in bid_rows:
        k = (r['entity'], r['now'], r['to'])
        if k in seen:
            dups.append(r)
        seen[k] = r
    if dups:
        add('DUP', 'Same target written twice', f"Rows {seqs(dups)} repeat an entity already written in this run ({', '.join(sorted({r['entity'] for r in dups}))}).",
            '', 'Two ad groups carry the same keyword, or the loader emits one row twice; either way two instances split the read (SOP-29 F11 on the engine\'s own terms).',
            'Deploy once; consolidate the duplicate keyword into one ad group.', dups, 'Medium')
    # --- 16. TOS modifier cut on a non-ranking campaign already inside its ceiling
    tcpo = (tos['s'] / tos['o']) if tos['o'] else None
    if a['obj'] in ('Conversions', 'Discovery') and tos_rows and not a['price_now'] and tcpo and tos['c'] >= 15 and tcpo < a['contrib']:
        r = tos_rows[0]
        if fnum(r['to']) is not None and fnum(r['now']) is not None and fnum(r['to']) < fnum(r['now']):
            add('NONRANK-TOS-CUT', 'TOS modifier cut on a campaign whose top of search pays',
                f"Row {r['seq']}: {r['now']}% → {r['to']}%. Ex-deal top of search: {tos['c']} clicks, {tos['o']} orders, cost per order {usd(tcpo)} against {usd(a['contrib'])} contribution.",
                trunc(r.get('decision'), 220),
                'Doc scope: other objectives are priced inside their ceilings. Top of search here costs less per order than the order earns — it is inside its ceiling; “the premium buys rank” is not a pricing reason.',
                'Hold the modifier.', [r], 'Medium')
    if a['obj'] in ('Conversions', 'Discovery') and tos_rows and a['price_now'] and ceil['tos'] and a['price_now'] <= ceil['tos']:
        r = tos_rows[0]
        if fnum(r['to']) is not None and fnum(r['now']) is not None and fnum(r['to']) < fnum(r['now']):
            add('NONRANK-TOS-CUT', 'TOS modifier cut on a campaign already inside its ceiling',
                f"Row {r['seq']}: {r['now']}% → {r['to']}%; TOS price {usd(a['price_now'])} vs ceiling {usd(ceil['tos'])} ({a['why_rate']['tos']}).",
                trunc(r.get('decision'), 220),
                'Doc scope: other objectives are priced inside their ceilings. This one already is; the cut has no pricing reason and removes top-of-search clicks that pay.',
                'Hold the modifier. Cut only if the TOS price is above its ceiling.', [r], 'Medium')
    return out


def detect_extra(a):
    out = []
    X = a['X']
    eng = next((r for r in a['changes'] if r.get('tos_clk90') is not None), None)
    if eng:
        cc = a['W90']['tos']['c']
        e = eng['tos_clk90']
        cc_tot = sum(a['W90'][k]['c'] for k in ('tos', 'detail', 'other'))
        if cc and abs(e / cc - 1) > 0.2:
            mix = eng.get('mix') or eng.get('mix2')
            out.append(dict(code='PLACEMENT-READ', sev='Critical',
                title="The engine's placement read does not match the campaign's placement report",
                what=f"Engine reads top of search at {e} clicks in 90 days" + (f" and the mix as '{mix}'" if mix else '') +
                     f". Amazon's campaign placement report (Command Center, same 90 days) shows TOS {cc}, product pages {a['W90']['detail']['c']}, rest of search {a['W90']['other']['c']} of {cc_tot} clicks — PP {a['W90']['detail']['c']/cc_tot:.0%}.",
                why='The engine prices and grades on a term-level estimate of placement (the keyword grain, which Amazon never reports by placement).',
                issue='Doc §16 Table 2: placement is read per campaign per placement — the grain Amazon reports. A term estimate at a fraction of the real clicks mis-states the mix, the TOS conversion, the ceiling and whether the distribution fix is owed.',
                fix=f"Re-derive on the campaign report: ex-deal TOS {X['tos']['c']} clicks / {X['tos']['o']} orders, PP {X['detail']['c']} / {X['detail']['o']}, ROS {X['other']['c']} / {X['other']['o']}; ceilings TOS {usd(a['ceil']['tos'])}, PP {usd(a['ceil']['detail'])}.",
                rows=[eng]))
    ec = a.get('eng_contrib')
    econ = a['econ']
    if ec and econ.get('fee_model') and abs(ec - econ['be_basis']) / econ['be_basis'] > 0.08:
        out.append(dict(code='CONTRIB', sev='Medium', title='Contribution behind the prices differs from the serving child',
            what=f"Engine prices on ${ec:.2f} per order (campaign basket × break-even ACoS). Serving child {a['serving']}: list ${econ['price']:.2f} × 33.87% = ${econ['be_basis']:.2f}; fee-model contribution ${econ['fee_model']:.2f}.",
            why="The engine uses the campaign's own basket.", issue='Doc §2/§8 bound 1: the base is derived from the serving child, never inherited; if contribution is wrong every price is wrong.',
            fix='Price on the serving child\'s contribution; publish one per-child figure (see systemic finding S6).', rows=[]))
    return out
