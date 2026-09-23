"""Tuning vs performance timeline charts for B4 / B6: panel 1 daily TOS clicks + TOS share, panel 2 group rank. Change rounds marked."""
import json, os, sys
from datetime import date
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
S = os.path.dirname(os.path.abspath(__file__)); B = f'{S}/b46'
BLUE, ORANGE, AQUA, GREY = '#2a78d6', '#eb6834', '#1baf7a', '#8a8f98'
D = lambda s: date.fromisoformat(s)


def series(prod):
    d = json.load(open(f'{B}/{prod}_placements_clicks.json'))
    out = {}
    for s in d['series']:
        out[s['key']] = {p['date']: (p.get('clicks') or p.get('value') or 0, p.get('share'), p.get('effBid')) for p in s['points']}
    return d['days'], out


def ranks(prod, groups):
    from diag import rank_grid
    g, _ = rank_grid(prod)
    return {k: g.get(k, {}) for k in groups}


def chart(prod, title, rounds, deal=('2026-09-15', '2026-09-22'), groups=('Bamboo', 'Bamboo|King', 'Bamboo|Queen'), out=None):
    days, s = series(prod)
    x = [D(d) for d in days]
    tos = [s['tos'].get(d, (0,))[0] for d in days]
    pdp = [s['detail'].get(d, (0,))[0] for d in days]
    eff = [s['tos'].get(d, (0, 0, None))[2] for d in days]
    fig, ax = plt.subplots(3, 1, figsize=(9, 8.2), sharex=True, gridspec_kw=dict(height_ratios=[1.2, 0.8, 1.2]))
    a = ax[0]
    a.plot(x, tos, color=BLUE, lw=2, label='Top of search clicks / day')
    a.plot(x, pdp, color=ORANGE, lw=2, label='Product page clicks / day')
    a.set_ylabel('Clicks / day'); a.legend(loc='upper left', frameon=False, fontsize=8)
    a = ax[1]
    a.plot(x, eff, color=BLUE, lw=2)
    a.set_ylabel('Effective TOS bid $\n(spend-weighted)')
    a = ax[2]
    rk = ranks(prod, groups)
    x0 = x[0]
    for g, c in zip(groups, (BLUE, ORANGE, AQUA)):
        pts = sorted((D(k), v) for k, v in rk[g].items() if D(k) >= x0 and v)
        if pts:
            a.plot([p[0] for p in pts], [p[1] for p in pts], color=c, lw=2, label=g)
    a.invert_yaxis(); a.set_ylabel('Organic rank (group)\nlower is better'); a.legend(loc='lower left', frameon=False, fontsize=8)
    for a in ax:
        a.axvspan(D(deal[0]), D(deal[1]), color=GREY, alpha=0.12, lw=0)
        for r in rounds:
            if D(r) >= x0:
                a.axvline(D(r), color=GREY, lw=1, ls='--')
        a.spines[['top', 'right']].set_visible(False); a.grid(axis='y', color='#e5e7eb', lw=0.6)
    for r in rounds:
        if D(r) >= x0:
            ax[0].text(D(r), ax[0].get_ylim()[1], r[5:], fontsize=7, color=GREY, ha='center', va='bottom')
    ax[0].text(D(deal[0]), ax[0].get_ylim()[1] * 0.92, ' Best Deal', fontsize=8, color='#555')
    ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    fig.suptitle(title, fontsize=11, x=0.01, ha='left')
    fig.tight_layout()
    fig.savefig(out or f'{S}/chart_{prod}.png', dpi=160)
    return out or f'{S}/chart_{prod}.png'


if __name__ == '__main__':
    print(chart('b6', 'B6 — daily placement clicks, effective TOS bid and group rank (dashed = bid-change rounds)', ['2026-08-26', '2026-09-10', '2026-09-15']))
