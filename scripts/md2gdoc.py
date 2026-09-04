#!/usr/bin/env python3
"""Markdown -> Google-Docs-friendly HTML.

Google Docs' HTML import keeps inline styles on table cells, so borders,
header shading and column widths survive. Fenced code and inline code do not
survive Markdown import at all, which is what this replaces.
"""
import re, sys, html

NAVY   = '#1F3864'
HEADBG = '#1F3864'
ALT    = '#F4F6FA'
BORDER = '1px solid #B7C0D0'

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    return t

def render(md):
    lines = md.split('\n')
    out, i = [], 0
    out.append(
      '<style>'
      'body,p,td,th,li{font-family:Arial,Helvetica,sans-serif;color:#202020}'
      'p,li{font-size:10.5pt;line-height:1.45}'
      'h1{color:#1F3864;font-size:21pt}h2{color:#1F3864;font-size:15pt}'
      'h3{color:#1F3864;font-size:12.5pt}h4{color:#1F3864;font-size:11pt}'
      'table.t{border-collapse:collapse;width:100%;margin:10px 0 16px 0}'
      'th.h{border:1px solid #B7C0D0;background-color:#1F3864;color:#FFFFFF;'
      'font-weight:bold;font-size:9.5pt;padding:5px 7px;text-align:left}'
      'td.c{border:1px solid #B7C0D0;font-size:9.5pt;padding:5px 7px;vertical-align:top}'
      'hr{border:none;border-top:2px solid #1F3864}'
      '</style>')
    while i < len(lines):
        ln = lines[i]

        # table
        if ln.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1]):
            head = [c.strip() for c in ln.strip().strip('|').split('|')]
            i += 2
            body = []
            while i < len(lines) and lines[i].startswith('|'):
                body.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            out.append('<table class=t>')
            out.append('<tr>' + ''.join(f'<th class=h>{inline(h)}</th>' for h in head) + '</tr>')
            for row in body:
                out.append('<tr>' + ''.join(f'<td class=c>{inline(c)}</td>' for c in row) + '</tr>')
            out.append('</table>')
            continue

        s = ln.strip()
        if s == '---':
            out.append('<hr/>')
        elif s.startswith('#### '):
            out.append(f'<h4>{inline(s[5:])}</h4>')
        elif s.startswith('### '):
            out.append(f'<h3>{inline(s[4:])}</h3>')
        elif s.startswith('## '):
            out.append(f'<h2>{inline(s[3:])}</h2>')
        elif s.startswith('# '):
            out.append(f'<h1>{inline(s[2:])}</h1>')
        elif s.startswith('- '):
            items = []
            while i < len(lines) and lines[i].strip().startswith('- '):
                items.append(lines[i].strip()[2:]); i += 1
            out.append('<ul>')
            for it in items:
                out.append(f'<li>{inline(it)}</li>')
            out.append('</ul>')
            continue
        elif s == '':
            pass
        else:
            out.append(f'<p>{inline(s)}</p>')
        i += 1
    return '\n'.join(out)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    h = render(open(src).read())
    open(dst, 'w').write(h)
    print(f'{len(h):,} chars of HTML')
