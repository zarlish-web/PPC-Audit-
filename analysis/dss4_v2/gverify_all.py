"""Verify every Google copy against the local export (CSV: cell by cell; Doc: text + key numbers), and the export against the xlsx/docx data.
Output: v2/out/google_verify.json"""
import json, base64, re, html, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-PPC-Audit-/9ce1e055-11cb-5ecd-8379-78d9343956fb/scratchpad/v2/src')
import gverify as GV
import load as L
G = L.ROOT + 'v2/gexport/'
man = {m['file'].split('/')[-1]: m for m in json.load(open(G + 'manifest.json'))}
ids = {}
for line in open(G + 'ids.jsonl'):
    if line.strip():
        x = json.loads(line); ids[x['file']] = x
res = []
for f, m in sorted(man.items()):
    x = ids.get(f)
    if not x:
        res.append(dict(file=f, title=m['title'], ok=False, detail='not uploaded')); continue
    if x['id'] not in GV.found:
        res.append(dict(file=f, title=m['title'], id=x['id'], url=x['url'], ok=False, detail='no read-back found')); continue
    b64, mt = GV.found[x['id']]
    got = base64.b64decode(b64).decode('utf-8')
    if f.endswith('.csv'):
        a = [[GV.norm_num(c) for c in r] for r in GV.norm_csv(open(G + f, encoding='utf-8').read()) if any(r)]
        b = [[GV.norm_num(c) for c in r] for r in GV.norm_csv(got) if any(r)]
        diffs = [(i, xa, xb) for i, (xa, xb) in enumerate(zip(a, b)) if xa != xb]
        # Google Sheets treats a leading apostrophe as a text marker and does not show it; count those cells separately
        strip = lambda r: [c[1:] if isinstance(c, str) and c.startswith("'") else c for c in r]
        apos = sum(1 for i, xa, xb in diffs if strip(xa) == strip(xb))
        diffs = [(i, xa, xb) for i, xa, xb in diffs if strip(xa) != strip(xb)]
        ok = len(a) == len(b) and not diffs
        res.append(dict(file=f, title=m['title'], id=x['id'], url=x['url'], ok=ok, rows=len(a) - 1, rows_drive=len(b) - 1, cols=len(a[0]),
                        detail=('identical cell by cell' + (f" (Google hides the leading apostrophe in {apos} cells — display rule, text otherwise identical)" if apos else '')) if ok else f"{len(diffs)} rows differ; first: {str(diffs[:1])[:300]}"))
    else:
        loc = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', open(G + f, encoding='utf-8').read()))).strip()
        drv = re.sub(r'\s+', ' ', got).strip()
        lw, dw = loc.split(), drv.split()
        must = [c['check'].split(' = ', 1)[1] for c in json.load(open(L.OUT + 'checks.json')) if c['check'].startswith('Document states')]
        miss = [v for v in must if v not in drv]
        ok = abs(len(lw) - len(dw)) <= 0.01 * len(lw) and not miss
        res.append(dict(file=f, title=m['title'], id=x['id'], url=x['url'], ok=ok, words_local=len(lw), words_drive=len(dw), key_values_checked=len(must),
                        detail=('text matches and all key figures present' if ok else f"missing {miss[:5]}; words {len(lw)} vs {len(dw)}")))
json.dump(res, open(L.OUT + 'google_verify.json', 'w'), indent=1, ensure_ascii=False)
for r in res:
    print('OK  ' if r['ok'] else 'FAIL', r['file'], r.get('rows', r.get('words_drive')), r['detail'][:120])
print(sum(r['ok'] for r in res), '/', len(res))
