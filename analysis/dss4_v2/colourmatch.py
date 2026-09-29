"""Match a search term's colour to an LTSF SKU's colour. A term that names a shade (sage, dark, light, stone, sea, …) must contain the SKU's full
colour phrase; a plain colour word ('green', 'grey') matches a SKU whose colour ends in that word. Size: the term's own size if it names one."""
import re

MODS = ('sage', 'olive', 'emerald', 'hunter', 'forest', 'mint', 'light', 'dark', 'stone', 'sea', 'baby', 'navy', 'burnt', 'blush', 'dusty', 'charcoal', 'silver')
ALIAS = {'gray': 'grey'}


def norm(s):
    s = (s or '').lower()
    for a, b in ALIAS.items():
        s = re.sub(r'\b' + a + r'\b', b, s)
    return s


def term_size(term):
    t = term.lower()
    if re.search(r'cal(ifornia)? ?king', t):
        return 'Cal King'
    for z in ('king', 'queen', 'full', 'twin'):
        if re.search(r'\b' + z + r'\b', t):
            return z.title()
    return None


def matches(term, sku_colour, sku_name=''):
    t, c = norm(term), norm(sku_colour)
    if 'stripe' in (sku_name or '').lower() and 'stripe' not in t:
        return False
    if not c:
        return False
    if c in t:
        return True
    has_mod = any(re.search(r'\b' + m + r'\b', t) for m in MODS)
    last = c.split()[-1]
    return (not has_mod) and re.search(r'\b' + last + r'\b', t) is not None and len(c.split()) >= 1


def ltsf_for_term(term, ltsf_rows, sku_map, min_aged=20):
    z = term_size(term)
    for r in ltsf_rows:                       # in LTSF priority order
        s = sku_map.get(r['sku']) or {}
        if r['est_aged_left'] >= min_aged and matches(term, s.get('colour'), r['sku']) and (z is None or s.get('size') == z):
            return r
    return None
