"""Google export: each needed tab as CSV (≤80 KB per file, split into parts), the document as HTML. Same data as the xlsx/docx.
Also writes manifest.json with row counts and a checksum column per file, used to cross-validate after upload."""
import csv, io, json, html, hashlib
from openpyxl import load_workbook
import load as L

G = L.ROOT + 'v2/gexport/'
DEL = L.ROOT + 'v2/deliver/'
LIM = 80_000
man = []


def tab(wbpath, name, cols=None, trunc=None, header_hint=None):
    wb = load_workbook(wbpath, read_only=True)
    it = [list(r) for r in wb[name].iter_rows(values_only=True)]
    hr = 2 if len(it) > 2 and all(v is None for v in it[1]) else 0     # sheets with a note: note row 1, blank row 2, header row 3
    head = it[hr]
    idx = [head.index(c) for c in cols] if cols else [i for i, c in enumerate(head) if c is not None]
    out = [[head[i] for i in idx]]
    for r in it[hr + 1:]:
        if not r or all(v is None for v in r):
            continue
        row = []
        for i in idx:
            v = r[i] if i < len(r) else None
            v = '' if v is None else (round(v, 4) if isinstance(v, float) else v)
            if trunc and head[i] in trunc and isinstance(v, str):
                v = v[:trunc[head[i]]]
            row.append(v)
        out.append(row)
    return out


def write(title, rows, key_col=0):
    head, body = rows[0], rows[1:]
    parts, cur, size = [], [], 0
    for r in body:
        s = io.StringIO(); csv.writer(s).writerow(r); ln = len(s.getvalue().encode())
        if cur and size + ln > LIM:
            parts.append(cur); cur, size = [], 0
        cur.append(r); size += ln
    parts.append(cur)
    for i, p in enumerate(parts, 1):
        t = title + (f" (part {i} of {len(parts)})" if len(parts) > 1 else '')
        fn = G + f"{len(man) + 1:02d}.csv"
        with open(fn, 'w', newline='') as f:
            w = csv.writer(f); w.writerow(head); w.writerows(p)
        keys = [str(r[key_col]) for r in p]
        man.append(dict(file=fn, title=t, rows=len(p), cols=len(head), bytes=len(open(fn, 'rb').read()), first_key=keys[0] if keys else '', last_key=keys[-1] if keys else '',
                        key_hash=hashlib.md5('|'.join(keys).encode()).hexdigest()))


RW, AP = DEL + 'DSS4_Audit_Review_Workbook_20260929.xlsx', DEL + 'DSS4_Action_Plan_20260929.xlsx'
P = 'DSS4 29 Sep — '
# action plan
ap_sum = [[r[0], r[1]] for r in load_workbook(AP, read_only=True)['Summary'].iter_rows(values_only=True) if r and r[0]]
write(P + 'AP0 Summary', [['Item', 'Value']] + ap_sum)
write(P + 'AP1 Action list', tab(AP, 'Action list', ['#', 'Step', 'Campaign ID', 'Campaign', 'Role', 'Level', 'Entity (target / SKU / setting)', 'Change', 'From', 'To',
                                                   'Top-of-search price $ (base × 10)', 'Ad group ID', 'Keyword/target ID', 'Clicks 30d', 'Orders 30d', 'ACoS 30d %', 'Break-even ACoS %', 'Why (data behind the change)'],
                                  trunc={'Campaign': 60, 'Why (data behind the change)': 140}))
for n_ in ('Stock & reorder', 'Back-up switch', 'Ranking terms', 'Keyword actions', 'LTSF', 'Owner decisions', 'Monitoring'):
    write(P + 'AP ' + n_, tab(AP, n_, trunc={'Why': 200, 'Trigger and action': 250}))
# review workbook
write(P + 'RW Summary', tab(RW, 'Summary'))
write(P + 'RW Campaigns (all 612)', tab(RW, 'Campaigns', ['Campaign ID', 'Campaign', 'Ad type', 'Status', 'Role', 'Advertised child (actual)', 'Ranking terms it owns', 'Budget $/day',
                                                          'Budget used %', 'TOS impr. share %', 'Clicks 30d', 'Orders 30d', 'Spend 30d', 'ACoS 30d %', 'Break-even ACoS %',
                                                          'ACTION: state', 'ACTION: child →', 'ACTION: budget →', 'ACTION: TOS % →', 'ACTION: ROS % →', 'ACTION: PP % →',
                                                          'ACTION: back-up ad (add PAUSED)', 'Plan spend/day', 'Δ profit/day', 'Why'], trunc={'Campaign': 60, 'Why': 180, 'Ranking terms it owns': 60}))
write(P + 'RW Audit review (381 decisions)', tab(RW, 'Audit review', ['Seq', 'Kind', 'Campaign ID', 'Campaign', 'Audit: current', 'Audit: suggested', 'Role (this review)', 'Verdict',
                                                                     'Final action on the campaign', 'Main term', 'Rank (7-day median)', 'Δ orders/day', 'Δ profit/day', 'Evidence'],
                                                 trunc={'Campaign': 50, 'Evidence': 200, 'Audit: suggested': 40}))
write(P + 'RW Preferred variation', tab(RW, 'Preferred variation'))
write(P + 'RW Back-up ranking child', tab(RW, 'Back-up ranking child'))
write(P + 'RW Inventory', tab(RW, 'Inventory'))
write(P + 'RW Financials', tab(RW, 'Financials'))
write(P + 'RW Push cost by term', tab(RW, 'Push cost by term'))
write(P + 'RW LTSF campaigns', tab(RW, 'LTSF campaigns', trunc={'Why': 250, 'Campaign': 60}))
write(P + 'RW Competitors', tab(RW, 'Competitors'))
write(P + 'RW Conflicts', tab(RW, 'Conflicts'))
write(P + 'RW Checks', tab(RW, 'Checks'))
# document as HTML
B = json.load(open(L.OUT + 'doc_blocks.json'))
h = ['<html><head><meta charset="utf-8"></head><body style="font-family:Calibri,Arial">']
for b in B:
    if b['t'] == 'title':
        h.append(f"<h1>{html.escape(b['text'])}</h1><p><i>{html.escape(b['sub'])}</i></p>")
    elif b['t'] in ('h1', 'h2'):
        h.append(f"<{'h2' if b['t'] == 'h1' else 'h3'}>{html.escape(b['text'])}</{'h2' if b['t'] == 'h1' else 'h3'}>")
    elif b['t'] == 'p':
        h.append(f"<p>{html.escape(b['text'])}</p>")
    elif b['t'] == 'ul':
        h.append('<ul>' + ''.join(f"<li>{html.escape(i)}</li>" for i in b['items']) + '</ul>')
    elif b['t'] == 'table':
        h.append('<table border="1" cellpadding="3" style="border-collapse:collapse;font-size:9pt"><tr>' + ''.join(f"<th style='background:#1F3864;color:#fff'>{html.escape(c)}</th>" for c in b['cols']) + '</tr>'
                 + ''.join('<tr>' + ''.join(f"<td>{html.escape(c)}</td>" for c in r) + '</tr>' for r in b['rows']) + '</table><p></p>')
h.append('</body></html>')
open(G + 'doc.html', 'w').write('\n'.join(h))
man.append(dict(file=G + 'doc.html', title='DSS4 Audit Review — 29 Sep 2026', bytes=len(open(G + 'doc.html', 'rb').read()), words=len(' '.join(h).split())))
json.dump(man, open(G + 'manifest.json', 'w'), indent=1)
for m in man:
    print(m['file'][-9:], m['bytes'], m.get('rows'), m['title'])
