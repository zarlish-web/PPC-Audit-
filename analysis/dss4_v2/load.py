"""DSS4 v2 — loaders. Every source is read raw from v2/raw (pulled 29 Sep 2026) or the audit export; nothing is reused from other products."""
import json, glob, os, re, collections

ROOT = '/tmp/claude-0/-home-user-PPC-Audit-/9ce1e055-11cb-5ecd-8379-78d9343956fb/scratchpad/'
RAW = ROOT + 'v2/raw/'
OUT = ROOT + 'v2/out/'
os.makedirs(OUT, exist_ok=True)


def J(p):
    return json.load(open(p))


def rows(x):
    if isinstance(x, list):
        return x
    for k in ('rows', 'data', 'items'):
        if isinstance(x.get(k), list):
            return x[k]
    return []


# ------------------------------------------------------------------ audit export (the engine run being verified)
AUDIT = J(ROOT + 'dss/a.json')

# ------------------------------------------------------------------ Command Center
CC_CAMP30 = {r['campaignId']: r for r in J(ROOT + 'dss/cc_rows_30d.json')}    # 30d campaigns with measured placement split
CC_CAMP90 = {r['campaignId']: r for r in J(ROOT + 'dss/cc90.json')}          # 90d campaigns with placement split
CC_TARGETS = J(ROOT + 'dss/targets_extra.json') if os.path.exists(ROOT + 'dss/targets_extra.json') else {}
KW30 = rows(J(RAW + 'cc/kw_all_30d.json'))
KW90 = rows(J(RAW + 'cc/kw_all_90d.json'))
KW30P = {r['keyword']: r for r in J(ROOT + 'dss/kw30.json')}   # top 600 with estimated placement split
DAILY = J(RAW + 'cc/daily_180d.json')
RANKS = rows(J(RAW + 'cc/ranks_top200_90d.json')) + rows(J(RAW + 'cc/ranks_next200_90d.json'))
SYNTAX = J(RAW + 'cc/syntax_groups.json')
T = '/root/.claude/projects/-home-user-PPC-Audit-/9ce1e055-11cb-5ecd-8379-78d9343956fb/tool-results/'
CC_CONTEXT = J(T + 'mcp-ecotero-command-center-ppc_product_context-1790709033376.txt')

# ------------------------------------------------------------------ Sellerboard
SB_SKU30 = rows(J(RAW + 'sb_prod/sku_30d.json'))
SB_SKU90 = rows(J(RAW + 'sb_prod/sku_90d.json'))
SB_SKUDEAL = rows(J(RAW + 'sb_prod/sku_deal_jul.json'))
SB_MONTHLY = J(RAW + 'sb_prod/monthly.json')['months']
SB_INV = J(RAW + 'sb_prod/inventory.json')['rows']
SB_SHIP = J(RAW + 'sb_prod/shipments.json')
SB_FAMILY30 = J(RAW + 'sb_prod/sku_30d.json').get('family_totals')
SB_FAMILY90 = J(RAW + 'sb_prod/sku_90d.json').get('family_totals')
SB_PPC = {}
for f in glob.glob(RAW + 'sb_ppc/*.json'):
    try:
        SB_PPC[os.path.basename(f)[:-5]] = J(f)
    except Exception:
        pass

# ------------------------------------------------------------------ Data Dive
def _dd(pat):
    f = glob.glob(RAW + 'dd/' + pat)
    return rows(J(f[0])) if f else []


SQP = {q: {r['keyword']: r for r in _dd(f'radar_83cfb815*_sqp_{q}.json')} for q in ('q4_2025', 'q2', 'q3')}
RADAR = {r['keyword']: r for r in _dd('radar_83cfb815*_ranks.json')}
RADAR_PPC = {r['keyword']: r for r in _dd('radar_83cfb815*_ppc_30d.json')}
DD_INV = J(RAW + 'dd/inventory_distribution.json')['byAsin']
DD_LISTING = J(RAW + 'dd/listing_changes.json')['byAsin']
NICHES = {}
for f in glob.glob(ROOT + 'dssc/dd_comp_*.json') + glob.glob(RAW + 'dd/niche_*_comp.json'):
    nid = re.search(r'(?:dd_comp_|niche_)(\w+?)(?:_comp)?\.json', os.path.basename(f)).group(1)
    d = J(f)
    NICHES[nid] = d
NICHE_KW = {}
for f in glob.glob(ROOT + 'dssc/dd_kw_*.json') + glob.glob(RAW + 'dd/niche_*_kw.json'):
    nid = re.search(r'(?:dd_kw_|niche_)(\w+?)(?:_kw)?\.json', os.path.basename(f)).group(1)
    NICHE_KW[nid] = J(f)
NICHE_LIST = J(ROOT + 'dssc/dd_niches.json')

# ------------------------------------------------------------------ ASINsight (via Command Center)
MKT = J(ROOT + 'dssc/market_p1.json')
MKW = {r['keyword']: r for r in J(ROOT + 'dssc/mkw_all.json')}
COMP = J(ROOT + 'dssc/comp_raw.json')
HIST = J(ROOT + 'dssc/history.json')
TRENDS = J(ROOT + 'dssc/trends.json')
OUR_AS = {r['keyword']: r for r in J(ROOT + 'dssc/asinsight.json')}
SBV_BRAND = J(RAW + 'video/sbv_by_brand.json')
SBV_KW = J(RAW + 'video/sbv_keywords.json')
VIDEO = J(RAW + 'video/video_research.json')

# ------------------------------------------------------------------ SKU parsing (from the SKU text and Sellerboard ASIN/title)
SIZE_RE = [('King', r'(?<![A-Z])KING'), ('Queen', r'QUEEN'), ('Full', r'(?<![A-Z])FULL'), ('Twin', r'TWIN')]
TITLE_SIZE = [('King', r'\bking\b'), ('Queen', r'\bqueen\b'), ('Full', r'\bfull\b'), ('Twin', r'\btwin\b')]
DROP = {'SATIN', '4PC', '4PCS', '3PC', 'NEW', 'V2', 'V3', 'KING', 'QUEEN', 'FULL', 'TWIN'}


def size_of_sku(sku, title=''):
    s = (sku or '').upper()
    for z, p in SIZE_RE:
        if re.search(p, s):
            return z
    t = (title or '').lower()
    for z, p in TITLE_SIZE:
        if re.search(p, t):
            return z
    return None


def colour_of_sku(sku, title=''):
    toks = [t for t in re.split(r'-', (sku or '').upper()) if t and t not in DROP]
    c = ' '.join(toks).replace('STONEGREY', 'STONE GREY').replace('GRAY', 'GREY').strip()
    if (not c or re.match(r'^[A-Z0-9]{2}$', c.split()[0]) or c.startswith('AMAZON')) and title:
        m = re.search(r'\(([^)]+)\)\s*$', title)
        if m:
            c = m.group(1).upper()
    return c.title()
