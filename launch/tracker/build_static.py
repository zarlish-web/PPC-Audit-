"""Bake the tracker datasets into one standalone HTML page (no sign-in needed to read it).

Usage: python3 -I build_static.py <data_dir> <template.html> <out.html> <asof YYYY-MM-DD>
"""
import json, sys
data_dir, tpl, out, asof = sys.argv[1:5]
names = ['day_reports', 'daily', 'size_daily', 'sizes', 'actions', 'queen_terms', 'king_terms', 'queen_campaigns', 'ranks', 'stock', 'overlap', 'decisions', 'log']
D = {n: json.load(open(f'{data_dir}/{n}.json')) for n in names}
D['asof'] = asof
blob = json.dumps(D, ensure_ascii=False).replace('</', '<\\/')
html = open(tpl).read().replace('/*__DATA__*/null', blob)
open(out, 'w').write(html)
print(out, len(html))
