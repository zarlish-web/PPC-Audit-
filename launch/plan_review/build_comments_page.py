"""Build the plan review comment page and its Markdown twin.

Usage: python3 -I build_comments_page.py <comments.json> <canvas.json> <template.html> <out.html> <out.md>

canvas.json is the plan canvas's own board index; only board titles and order are read from it.
"""
import json
import sys

SECTION_ORDER = [
    "The growth plan", "The market", "Returns and ratings", "Keyword grading", "The push plan",
    "Pricing", "Promotions", "The PPC plan", "COGS and fees", "The financial plan", "Seasonality", "Decisions",
]


def main(comments_path, canvas_path, template_path, out_html, out_md):
    data = json.load(open(comments_path))
    canvas = json.load(open(canvas_path))
    order = [k.replace(".dc.html", "") for k in canvas["order"]]
    titles = {}
    for key, board in canvas["boards"].items():
        code = key.replace(".dc.html", "")
        if code.startswith("TCC_"):
            titles[code] = board.get("title", "").replace(" · CooLinens Cooling", "")
    pos = {code: i for i, code in enumerate(order)}

    comments = data["comments"]
    for c in comments:
        missing = [b for b in [c["board"], *c["also_on"]] if b not in titles]
        if missing:
            raise SystemExit(f"{c['id']}: unknown board {missing}")
        c["board_title"] = titles[c["board"]]
    comments.sort(key=lambda c: (SECTION_ORDER.index(c["section"]), pos[c["board"]], c["id"]))
    data["comments"] = comments
    data["titles"] = {b: titles[b] for c in comments for b in [c["board"], *c["also_on"]]}
    data["sections"] = [s for s in SECTION_ORDER if any(c["section"] == s for c in comments)]

    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = open(template_path).read().replace("/*__DATA__*/null", payload)
    open(out_html, "w").write(html)

    m = data["meta"]
    lines = [
        "# CooLinens plan review: comments for the board",
        "",
        f"Plan: {m['plan']} ({m['plan_url']}), {m['plan_version']}.",
        f"Live data: {m['live_window']}. {m['mode']}",
        "",
        "Each comment names the board to pin it on. P1 = this week or before the Oct 23 order; P2 = before targets are stored; P3 = clean-up.",
        "",
    ]
    for s in data["sections"]:
        lines += [f"## {s}", ""]
        for c in [c for c in comments if c["section"] == s]:
            also = f" (also {', '.join(c['also_on'])})" if c["also_on"] else ""
            refs = f" · {', '.join(c['refs'])}" if c["refs"] else ""
            lines += [
                f"### {c['id']} · {c['board']}{also}",
                f"{c['type']} · {c['priority']} · {c['owner']}{refs}",
                "",
                f"**{c['headline']}**",
                "",
                f"- **Issue:** {c['issue']}",
                f"- **Recommendation:** {c['rec']}",
                f"- **Evidence:** {c['evidence']}",
                f"- **Expected outcome:** {c['outcome']}",
                f"- **Needs:** {c['needs']}",
                "",
            ]
    lines += ["## Checked, no change needed", ""]
    lines += [f"- **{n['area']}:** {n['note']}" for n in data["no_change"]]
    open(out_md, "w").write("\n".join(lines) + "\n")
    print(f"{len(comments)} comments, {len(data['no_change'])} no-change notes")


if __name__ == "__main__":
    main(*sys.argv[1:6])
