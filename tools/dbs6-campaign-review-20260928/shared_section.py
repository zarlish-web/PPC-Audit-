# shared-term section, inserted into both builders; ME / OTHER are 'B4' / 'B6'
section('Terms B4 and B6 both bid — one family owner per term')
_other = json.load(open(f'{S}/../{OTHER_DIR}/review.json'))
def _best(rows, kw):
    xs = [r for r in rows if r.get('kw') == kw and r.get('ceil_tos') is not None]
    return max(xs, key=lambda r: r['d30']['spend']) if xs else None
_sh = sorted({r['kw'] for r in RV if r.get('sibling') and r.get('kw')})
_rows = []
for kw in _sh:
    m, o = _best(RV, kw), _best(_other, kw)
    if not (m and o):
        continue
    mo, oo = m['d30']['tos_o'], o['d30']['tos_o']
    mc, oc = m['d30']['tos_c'], o['d30']['tos_c']
    sug = ME if (mo, m['d30']['spend']) >= (oo, o['d30']['spend']) else OTHER
    _rows.append((m['d30']['spend'] + o['d30']['spend'], [kw, f"{m.get('rank_now') or '—'} / {o.get('rank_now') or '—'}", f"${m['d30']['spend']:,.0f} · {mc} → {mo}", f"${o['d30']['spend']:,.0f} · {oc} → {oo}", sug]))
_rows.sort(key=lambda t: -t[0])
lead('The rule (redline, 28 September).', 'Where another Decolure product bids the same term, the family owner prices it (SOP-33) and the others hold at their ceiling with no top-of-search premium. A ceiling computed as if the sibling were not in the auction is too high for both, and each one’s raise is a bid against the other.')
lead('What the data shows.', f"{ME} and {OTHER} both run enabled exact campaigns on {len(_sh)} of {ME}’s ranking terms ({sum(1 for r in RV if r.get('sibling'))} {ME} ranking campaigns). No owner is named for any of them, so no premium is allowed on either side until one is. The suggestion below gives each term to the product that took more top-of-search orders on it in the last 30 days — a starting point for the operator’s ruling, not the ruling.")
table(['Term', f'Rank {ME} / {OTHER}', f'{ME}: spend · TOS clicks → orders', f'{OTHER}: spend · TOS clicks → orders', 'Suggested owner'], [r for _, r in _rows[:18]], widths=[4.4, 2.2, 3.8, 3.8, 2.2], size=7.5)
lead('Correction.', f"Name an owner per shared term. The non-owner keeps its campaign at its ceiling (it still sells), takes no premium, and is not raised against the owner; where the owner is the other product and this product’s campaign adds nothing, pause it. All {len(_rows)} shared terms are in the register (“SIBLING”).")
