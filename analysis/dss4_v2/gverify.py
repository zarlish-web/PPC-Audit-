"""Exact read-back check: find Drive download results (base64) for given file IDs in the session transcripts on disk, decode, and diff with the local file."""
import json, glob, base64, sys, csv, io, re
T = '/root/.claude/projects/-home-user-PPC-Audit-/9ce1e055-11cb-5ecd-8379-78d9343956fb'
files = [T + '.jsonl'] + glob.glob(T + '/subagents/*.jsonl')
saved = glob.glob(T + '/tool-results/mcp-Google_Drive-download_file_content-*.txt') + glob.glob(T + '/subagents/*/tool-results/*download_file_content*')
found = {}
for f in files:
    for line in open(f, errors='ignore'):
        if '"content' not in line or 'exportMimeType' in line and 'tool_use' in line:
            pass
        if 'tool_result' not in line:
            continue
        for m in re.finditer(r'\{\\?"content\\?":\\?"([A-Za-z0-9+/=]{20,})\\?",\\?"id\\?":\\?"([A-Za-z0-9_-]+)\\?",\\?"mimeType\\?":\\?"([^"\\]+)', line):
            found[m.group(2)] = (m.group(1), m.group(3))


for f in saved:
    try:
        d = json.load(open(f))
        if isinstance(d, list):
            d = json.loads(d[0]['text']) if d and isinstance(d[0], dict) and 'text' in d[0] else d
        found[d['id']] = (d['content'], d.get('mimeType'))
    except Exception:
        txt = open(f, errors='ignore').read()
        m = re.search(r'"content":\s*"([A-Za-z0-9+/=]{20,})",\s*"id":\s*"([A-Za-z0-9_-]+)",\s*"mimeType":\s*"([^"]+)"', txt)
        if m:
            found[m.group(2)] = (m.group(1), m.group(3))


def norm_csv(text):
    return [[c.strip() for c in r] for r in csv.reader(io.StringIO(text.replace('\r\n', '\n')))]


def norm_num(v):
    if isinstance(v, str) and v.lower() in ('true', 'false'):
        return v.lower()                       # Sheets writes booleans as TRUE/FALSE
    try:
        x = float(v.replace(',', '').replace('$', '').replace('%', ''))
        return round(x, 4)
    except Exception:
        return v


if __name__ == '__main__':
    pairs = json.loads(sys.argv[1])          # {file_id: local_path}
    out = {}
    for fid, path in pairs.items():
        if fid not in found:
            out[fid] = 'no download found in transcripts'; continue
        b64, mt = found[fid]
        got = base64.b64decode(b64).decode('utf-8')
        loc = open(path, encoding='utf-8').read()
        if path.endswith('.csv'):
            a, b = norm_csv(loc), norm_csv(got)
            a = [[norm_num(c) for c in r] for r in a if any(r)]
            b = [[norm_num(c) for c in r] for r in b if any(r)]
            diffs = [(i, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
            out[fid] = dict(rows_local=len(a), rows_drive=len(b), cells_differing_rows=len(diffs), first_diff=diffs[:2])
        else:
            out[fid] = dict(chars_local=len(loc), chars_drive=len(got))
    print(json.dumps(out, indent=1, ensure_ascii=False))
