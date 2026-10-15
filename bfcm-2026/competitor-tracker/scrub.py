"""Remove data-source names from every text the tracker shows (agreed Oct 15, 2026: the workbook and the dashboard
never name where a number came from). Tool, vendor, person and file names become neutral words; dates and numbers stay."""
import re

_RULES = [
    # whole attributions first
    (r"\s*\[[^\]]*(?:Slack|Umair|Abubakar|Erik|Joseph|#[a-z0-9-]+)[^\]]*\]", ""),
    (r"\s*\((?:[^()]*?\b(?:Slack|Umair Tahir|Abubakar Ishrat|Erik Fisher|Joseph Fisher|BM)\b[^()]*)\)", ""),
    (r"Umair Tahir via Shayan Rana,?\s*", ""),
    (r"\b(?:Umair Tahir|Abubakar Ishrat \(AB\)|Abubakar Ishrat|Erik Fisher|Joseph Fisher|Joseph's|Joseph|Erik|Umair's|Umair)\b", "the team"),
    (r"\bBM's\b", "the team's"),
    (r"\bBM(?=[,)\s:])(?!-)", "the team"),
    (r"(?:,\s*)?(?:shared|relayed) by Shayan(?: Rana)?", ""),
    (r"\s*#[a-z][a-z0-9-]+(?:\s\d{4}-\d{2}-\d{2}(?:/\d{2})*)?", ""),
    (r"\(?\bdata/[^\s,;)]*\)?", ""),
    (r"\bproduct_images/[^\s,;)]*", ""),
    (r"AGENT_PROMPTS(?:\.md)?\s*(?:Prompt\s*\d+)?", ""),
    (r"\bPrompts? \d+(?: \([^)]*\))?(?:\s*(?:\+|and)\s*Prompt \d+(?: \([^)]*\))?)*", ""),
    # tools and vendors
    (r"Helium 10 Xray \(Amazon\.ca, CAD\)", "catalog price (CAD)"),
    (r"Helium 10 Xray", "catalog price"),
    (r"Helium 10", "catalog"),
    (r"\bX-?[Rr]ay\b", "catalog"),
    (r"\bX-Ray sales band\b", "sales band"),
    (r"Command Center (?:keepa_history|competitors_roster|amazon_promotions|amazon_coupons|Competitor Summary)", "market data"),
    (r"Command Center", "market data"),
    (r"\bCC\b(?= (?:price|snapshot|roster|blended))", "market data"),
    (r"SellerBoard(?: MCP)?(?:,? Ecotero account)?", "account data"),
    (r"\bSellerboard\b", "account data"),
    (r"\bEcotero\b;?\s*", ""),
    (r"\bKeepa(?: \.ca)?\b", "price history"),
    (r"\bkeepa(?:_history\w*)?\b", "price history"),
    (r"Data ?Dive", "catalog data"),
    (r"Data ?Hub", "deal records"),
    (r"\bASINsight\b", "search data"),
    (r"Data ?Rova", "rank data"),
    (r"\b[Cc]laude-code-mcp\b|\b[Cc]laude's\b|\b[Cc]laude\b", "analyst"),
    (r"\bMCP\b", ""),
    (r"\bSlack\b:?\s*", ""),
    (r"\(the agent[^)]*\)|\(agent[^)]*\)", ""),
    (r"\bthe agent'?s?\b|\bagent\b|\bAgent\b", ""),
    (r"\bShayan(?: Rana)?\b(?! Rana ·)", "the team"),
]
_COMPILED = [(re.compile(p), r) for p, r in _RULES]
_TIDY = [(re.compile(r"\(\s*[,;·]?\s*\)"), ""), (re.compile(r"\(\s*,\s*"), "("), (re.compile(r"\s+,"), ","), (re.compile(r",\s*\)"), ")"),
         (re.compile(r"\s{2,}"), " "), (re.compile(r"\s+([.;:])"), r"\1"), (re.compile(r"(the team)(?:,? (?:and )?the team)+"), r"\1"),
         (re.compile(r"(account data|market data|catalog data|price history)\s+\1"), r"\1"), (re.compile(r"^[\s,;:·-]+"), "")]


def scrub(text):
    if not isinstance(text, str) or not text or text.startswith("="):
        return text
    if text.startswith("Owner:"):
        return text
    out = text
    for p, r in _COMPILED:
        out = p.sub(r, out)
    for p, r in _TIDY:
        out = p.sub(r, out)
    return out.strip() if out.strip() else out


SKIP_KEYS = {"img", "imgUrl", "url", "asin", "child", "parent", "best", "sku", "key", "uid", "image", "id"}


def scrub_obj(o, key=None):
    if isinstance(o, dict):
        return {k: (v if k in SKIP_KEYS else scrub_obj(v, k)) for k, v in o.items()}
    if isinstance(o, list):
        return [scrub_obj(v, key) for v in o]
    if isinstance(o, str):
        return scrub(o)
    return o
