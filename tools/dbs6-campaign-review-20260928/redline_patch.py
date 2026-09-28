import sys, re
p = sys.argv[1] + '/review.py'; s = open(p).read()
def rep(a, b, cnt=1):
    global s
    assert a in s, a[:80]; s = s.replace(a, b, cnt)

# --- keyword paid units (units the term already sells through our ads)
rep("KT[r['keyword']] = dict(rank=t.get('rank'), units30=t.get('units'),", "KT[r['keyword']] = dict(rank=t.get('rank'), units30=t.get('units'), paid30=r.get('units') or 0,")

# --- planning rate (redline §2): the child's own 90-day rate at the placement with 50+ clicks there, else the same size and pack
rep("def blend(clicks, orders, child):", '''_ch = defaultdict(lambda: [0, 0, 0, 0]); _sz = defaultdict(lambda: [0, 0, 0, 0])
for c in ENABLED:
    r = read(c['campaign_id'], 'd90'); ch = c.get('child'); sz = child_size(ch)
    for g in ([_ch[ch]] if ch else []) + ([_sz[sz]] if sz else []):
        g[0] += r['tos']['c']; g[1] += r['tos']['o']; g[2] += r['pp']['c']; g[3] += r['pp']['o']


def plan_rate(c, which):
    """(rate, basis) — the child's own 90-day rate at the placement where it has 50+ clicks there; otherwise the rate across the
    children of the same size in this product (same pack); never a rate borrowed from another size or pack."""
    i = 0 if which == 'tos' else 2
    ch = c.get('child'); sz = child_size(ch) or term_size(term_text(c))
    a = _ch.get(ch)
    if a and a[i] >= 50:
        return a[i + 1] / a[i], f"{(ch or '').replace('BAMBOO-', '').lower()} own 90d ({a[i + 1]}/{a[i]})"
    b = _sz.get(sz)
    if b and b[i] >= 15:
        return b[i + 1] / b[i], f"{SIZE_NAME.get(sz, sz)} size 90d ({b[i + 1]}/{b[i]})"
    return (PLAN_TOS if which == 'tos' else PLAN_PP), 'product 90d (size too thin)'


def blend(clicks, orders, child):''')
rep('''def blend(clicks, orders, child):
    if clicks < 15:
        return child, 'child rate (under 15 clicks)'
    if clicks < 50:
        if not orders:
            return child, f'child rate (no order on {clicks} clicks)'
        w = (clicks - 15) / 35''', '''def blend(clicks, orders, child):
    # redline §2: under 15 clicks the planning rate; a zero is evidence once the clicks would have produced 3 orders at the
    # planning rate (clicks × rate ≥ 3) — from there it blends toward the campaign's own rate by click count like any other read
    if clicks < 15:
        return child, 'planning rate (under 15 clicks)'
    if not orders and clicks * child < 3:
        return child, f'planning rate (0 orders on {clicks} clicks, under 3 expected)'
    if clicks < 50:
        w = (clicks - 15) / 35''')
rep("        ctos, cpp = GR.get(grp, (PLAN_TOS, PLAN_PP))", "        ctos, tsrc0 = plan_rate(c, 'tos'); cpp, psrc0 = plan_rate(c, 'pp')")
rep("tos_rate, tos_src = blend(", "tos_rate, tos_src = blend(")
# --- requirement (redline §7): incremental units only, then reachability; the sum check runs after every row is read
rep("        units_day = (kt.get('units30') or 0) / 30 if kt.get('units30') else None",
    "        units_day = max(0.0, ((kt.get('units30') or 0) - (kt.get('paid30') or 0)) / 30) if kt.get('units30') else None   # target units − units the term already sells (paid; organic per term is not in the data, so this is an upper bound)")
# --- incrementality at organic top 5
rep("'; organic top 3 → 15% incrementality step' if rank_now <= 3", "'; organic top 5 → 15% incrementality step' if rank_now <= 5")
open(p, 'w').write(s)
print('ok', p)
