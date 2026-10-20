"""Build the consolidated plan review page and its Markdown copy.

Usage: python3 -I build_review_page.py <review_items.json> <canvas.json> <template.html> <out.html> <out.md>

canvas.json is the plan canvas's own board index; only board titles are read from it.
"""
import json
import sys

PRIORITY = {"P1": "this week / before the Oct 23 order", "P2": "before targets are stored", "P3": "clean-up"}


def main(items_path, canvas_path, template_path, out_html, out_md):
    data = json.load(open(items_path))
    canvas = json.load(open(canvas_path))
    titles = {
        k.replace(".dc.html", ""): b.get("title", "").replace(" · CooLinens Cooling", "")
        for k, b in canvas["boards"].items() if k.startswith("TCC_")
    }
    items = data["items"]
    for it in items:
        missing = [b for b in [it["board"], *it["also_on"]] if b not in titles]
        if missing:
            raise SystemExit(f"{it['id']}: unknown board {missing}")
        if it["section"] not in data["sections"]:
            raise SystemExit(f"{it['id']}: unknown section {it['section']}")
        it["board_title"] = titles[it["board"]]
    ids = [it["id"] for it in items]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate item ids")
    items.sort(key=lambda it: data["sections"].index(it["section"]))
    data["titles"] = {b: titles[b] for it in items for b in [it["board"], *it["also_on"]]}

    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    open(out_html, "w").write(open(template_path).read().replace("/*__DATA__*/null", payload))

    m = data["meta"]
    out = [
        f"# {m['title']}",
        "",
        f"Plan: {m['plan']}, {m['plan_version']} ({m['plan_url']})",
        f"Live data: {m['live_window']}",
        f"{m['mode']}",
        "",
        "Status: **Confirmed issue** = verified on the boards or in live data · **Potential gap** = a risk or assumption to watch · **Open question** = needs an answer or decision.",
        "Priority: " + " · ".join(f"**{k}** {v}" for k, v in PRIORITY.items()),
        "",
        "## Key numbers",
        "",
        "| Measure | Value | Detail | Source |",
        "|---|---|---|---|",
    ]
    out += [f"| {k['label']} | {k['value']} | {k.get('note', '')} | {k['src']} |" for k in data["kpis"]]
    out.append("")
    for s in data["sections"]:
        sec = [it for it in items if it["section"] == s]
        if not sec:
            continue
        out += [f"## {s}", ""]
        for it in sec:
            refs = f" · {', '.join(it['refs'])}" if it["refs"] else ""
            also = f" (also {', '.join(it['also_on'])})" if it["also_on"] else ""
            out += [
                f"### {it['id']} · {it['area']}",
                f"{it['class']} · {it['priority']} · Board: {it['board']}{also}{refs}",
                "",
                "**Current status & evidence**",
            ]
            out += [f"- {e['t']} _({e['src']})_" for e in it["evidence"]]
            out += [
                "",
                f"**Our observation / concern:** {it['observation']}",
                "",
                f"**Our query:** {it['query']}",
                "",
                f"**Our recommendation:** {it['rec']}",
                "",
                f"**Expected outcome / next step:** {it['next']} (Owner: {it['owner']})",
            ]
            if it.get("unavailable"):
                out += ["", f"**Not available:** {it['unavailable']}"]
            out.append("")
    out += ["## Information not available", "", "| Item | Where | Impact |", "|---|---|---|"]
    out += [f"| {u['item']} | {u['where']} | {u['impact']} |" for u in data["unavailable"]]
    out += ["", "## Checked, no change needed", ""]
    out += [f"- **{n['area']}:** {n['note']}" for n in data["no_change"]]
    open(out_md, "w").write("\n".join(out) + "\n")
    counts = {c: sum(it["class"] == c for it in items) for c in ("Confirmed issue", "Potential gap", "Open question")}
    print(len(items), "items", counts)


if __name__ == "__main__":
    main(*sys.argv[1:6])
