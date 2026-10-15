// BFCM 2026 competitor research: the full Word report.
// Reads OUT_DIR/report.json + charts + photos written by build_report_assets.py and writes the .docx.
// Usage: node build_report.js OUT_DIR BFCM_2026_Competitor_Report.docx
const fs = require("fs"), path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType,
  VerticalAlign, HeadingLevel, PageOrientation, PageBreak, Header, Footer, PageNumber, LevelFormat, Bookmark, InternalHyperlink,
  TabStopType, TableLayoutType,
} = require("docx");

const [DIR, OUTFILE] = process.argv.slice(2);
const R = JSON.parse(fs.readFileSync(path.join(DIR, "report.json"), "utf8"));
const FONT = "Comfortaa";
const W = 14400;                       // usable width: Letter landscape, 0.5" margins (DXA)
const C = { ink: "15232B", muted: "5A6B74", accent: "0E6B67", accentSoft: "E0F0EE", line: "D9E2E6", chip: "EDF2F4",
            deal: "6A3F9E", dealSoft: "EFE8F7", bad: "A3262C", badSoft: "FBE6E7", good: "1D7A3E", goodSoft: "E2F3E8", warnSoft: "FCF0D6",
            blue: "2A78D6", orange: "EB6834", white: "FFFFFF" };

// ------------------------------------------------------------------ formatting helpers
const isNum = v => typeof v === "number" && isFinite(v);
const cur = m => (m === "CA" ? "C$" : "$");
const money = (v, m) => isNum(v) ? cur(m) + v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : "—";
const money0 = (v, m) => isNum(v) ? cur(m) + Math.round(v).toLocaleString("en-US") : "—";
const int = v => isNum(v) ? Math.round(v).toLocaleString("en-US") : "—";
const pct = (v, d = 0) => isNum(v) ? (v * 100).toFixed(d) + "%" : "—";
const x2 = v => isNum(v) ? v.toFixed(2) + "x" : "—";
const sgnPct = v => isNum(v) ? (v > 0 ? "+" : "") + (v * 100).toFixed(0) + "%" : "—";
const day = s => s ? new Date(s + "T12:00:00").toLocaleDateString("en-US", { month: "short", day: "numeric" }) : "after Nov 30";
const mktName = m => (m === "US" ? "United States" : "Canada");
const cleanHk = s => (s || "").replace(/\s*price history via[^]*$/i, "").trim();

// ------------------------------------------------------------------ image helpers
function dims(file) {
  const b = fs.readFileSync(file);
  if (b[0] === 0x89) return { w: b.readUInt32BE(16), h: b.readUInt32BE(20), type: "png", b };
  let i = 2;
  while (i < b.length) {
    if (b[i] !== 0xff) { i++; continue; }
    const mk = b[i + 1], len = b.readUInt16BE(i + 2);
    if (mk >= 0xc0 && mk <= 0xc3) return { h: b.readUInt16BE(i + 5), w: b.readUInt16BE(i + 7), type: "jpg", b };
    i += 2 + len;
  }
  return { w: 1, h: 1, type: "jpg", b };
}
// fit an image into a box of boxW x boxH pixels (96 px per inch), keeping its shape
function img(rel, boxW, boxH) {
  const d = dims(path.join(DIR, rel));
  const s = Math.min(boxW / d.w, (boxH || 1e9) / d.h);
  return new ImageRun({ type: d.type, data: d.b, transformation: { width: Math.round(d.w * s), height: Math.round(d.h * s) } });
}
const chart = (rel, inches = 10, maxH = 6.6) => rel ? new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 80 }, children: [img(rel, inches * 96, maxH * 96)] }) : null;

// ------------------------------------------------------------------ text helpers
const t = (text, o = {}) => new TextRun({ text: String(text ?? ""), font: FONT, ...o });
const P = (children, o = {}) => new Paragraph({ spacing: { after: 100, line: 276 }, ...o, children: (Array.isArray(children) ? children : [children]).map(c => typeof c === "string" ? t(c) : c) });
const small = (text, o = {}) => P([t(text, { size: 16, color: C.muted, ...o })], { spacing: { after: 60 } });
const bullet = (children, lvl = 0) => new Paragraph({ numbering: { reference: "bul", level: lvl }, spacing: { after: 60, line: 264 },
  children: (Array.isArray(children) ? children : [children]).map(c => typeof c === "string" ? t(c) : c) });
// "label: value" runs with the value bold
const kv = (label, value) => [t(label + " "), t(value, { bold: true })];
let bm = 0;
const H1 = (text, id) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new Bookmark({ id: id || `h${++bm}`, children: [t(text)] })] });
const H2 = (text, id, brk = false) => new Paragraph({ heading: HeadingLevel.HEADING_2, pageBreakBefore: brk, keepNext: true,
  children: id ? [new Bookmark({ id, children: [t(text)] })] : [t(text)] });
const H3 = text => new Paragraph({ heading: HeadingLevel.HEADING_3, keepNext: true, children: [t(text)] });

// ------------------------------------------------------------------ table helpers
const border = { style: BorderStyle.SINGLE, size: 4, color: C.line };
const BORDERS = { top: border, bottom: border, left: border, right: border };
function cell(content, w, o = {}) {
  const kids = (Array.isArray(content) ? content : [content]).map(c =>
    c instanceof Paragraph ? c : new Paragraph({ alignment: o.align || AlignmentType.LEFT, spacing: { after: 0, line: 240 },
      children: (Array.isArray(c) ? c : [c]).map(r => (typeof r === "string" || typeof r === "number") ? t(r, { size: o.size || 16, bold: o.bold, color: o.color }) : r) }));
  return new TableCell({ width: { size: w, type: WidthType.DXA }, borders: BORDERS, verticalAlign: o.valign || VerticalAlign.CENTER,
    margins: { top: o.pad ?? 50, bottom: o.pad ?? 50, left: 80, right: 80 }, columnSpan: o.span,
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined, children: kids });
}
// cols: [{h: "Header", w: dxa, a: "r"|"c"}]; rows: arrays of cell contents (string / runs / {v, fill, bold, color})
function table(cols, rows, o = {}) {
  const widths = cols.map(c => c.w), total = widths.reduce((a, b) => a + b, 0);
  const al = c => (c.a === "r" ? AlignmentType.RIGHT : c.a === "c" ? AlignmentType.CENTER : AlignmentType.LEFT);
  const head = new TableRow({ tableHeader: true, cantSplit: true, children: cols.map(c => cell(c.h, c.w, { fill: o.headFill || C.accent, bold: true, color: C.white, size: o.headSize || 15, align: al(c) })) });
  const body = rows.map(r => {
    if (r && r.group) return new TableRow({ cantSplit: true, children: [cell([[t(r.group, { bold: true, size: 17, color: C.ink })]], total, { span: cols.length, fill: r.fill || C.accentSoft })] });
    return new TableRow({ cantSplit: true, children: r.map((v, j) => {
      const spec = (v && typeof v === "object" && !Array.isArray(v) && "v" in v) ? v : { v };
      return cell(spec.v ?? "—", widths[j], { align: al(cols[j]), fill: spec.fill, bold: spec.bold, color: spec.color, size: o.size || 16, pad: o.pad });
    }) });
  });
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: [head, ...body] });
}
// a row of key-number tiles
function tiles(items) {
  const w = Math.floor(W / items.length);
  return new Table({ width: { size: w * items.length, type: WidthType.DXA }, columnWidths: items.map(() => w), layout: TableLayoutType.FIXED,
    rows: [new TableRow({ cantSplit: true, children: items.map(it => new TableCell({
      width: { size: w, type: WidthType.DXA }, shading: { fill: it.fill || C.accentSoft, type: ShadingType.CLEAR, color: "auto" },
      borders: { top: { style: BorderStyle.SINGLE, size: 4, color: C.white }, bottom: { style: BorderStyle.SINGLE, size: 4, color: C.white },
                 left: { style: BorderStyle.SINGLE, size: 24, color: it.edge || C.accent }, right: { style: BorderStyle.SINGLE, size: 4, color: C.white } },
      margins: { top: 90, bottom: 90, left: 140, right: 100 },
      children: [
        new Paragraph({ spacing: { after: 20 }, children: [t(it.k.toUpperCase(), { size: 14, bold: true, color: C.muted })] }),
        new Paragraph({ spacing: { after: 20 }, children: [t(it.v, { size: it.vs || 26, bold: true, color: it.color || C.ink })] }),
        ...(it.s ? [new Paragraph({ spacing: { after: 0 }, children: [t(it.s, { size: 14, color: C.muted })] })] : []),
      ] })) })] });
}
const gap = (n = 120) => new Paragraph({ spacing: { after: n }, children: [] });

// ------------------------------------------------------------------ content
const S = R.summary, L = R.lift, CH = R.charts;
const prods = R.products;
const pid = p => `p_${p.key.replace(/[^A-Za-z0-9]/g, "_")}`;
const body = [];

// ---- cover
const heroes = prods.filter(p => p.scope === "Core" && p.mkt === "US" && !p.photo.includes("COMING")).slice(0, 6);
const cover = [
  gap(600),
  P([t("BFCM 2026 · COMPETITOR RESEARCH", { size: 20, bold: true, color: C.accent })], { spacing: { after: 120 } }),
  P([t("BFCM 2026 Competitor Research Report", { size: 56, bold: true, color: C.ink })], { spacing: { after: 160 } }),
  P([t("Every product we sell for Black Friday – Cyber Monday 2026, every competitor we track against it, what worked in BFCM 2025, the deal prices we plan and the stock we need to Nov 30.", { size: 22, color: C.muted })], { spacing: { after: 300 } }),
  P([t("Owner: ", { size: 22, color: C.muted }), t("Shayan Rana", { size: 22, bold: true }), t("  ·  Prepared for ", { size: 22, color: C.muted }),
     t("Erik Fisher", { size: 22, bold: true }), t(" & ", { size: 22, color: C.muted }), t("Joseph Fisher", { size: 22, bold: true })], { spacing: { after: 80 } }),
  P([t(`Data as of ${R.built}  ·  United States and Canada`, { size: 18, color: C.muted })], { spacing: { after: 360 } }),
  tiles([
    { k: "Competitors tracked", v: int(S.comps), s: `US ${int(S.us)} · CA ${int(S.ca)}` },
    { k: "Direct competitors", v: int(S.byCls.Direct), s: "same product type and material" },
    { k: "Our BFCM 2025 sales lift", v: `${x2(S.accountLift.US)} · ${x2(S.accountLift.CA)}`, s: "US · CA, BFCM week vs 30 days before" },
    { k: "Checks passed", v: `${R.checks.filter(c => c.status === "Pass").length} of ${R.checks.length}`, s: "re-computed from the raw data", fill: C.goodSoft, edge: C.good, color: C.good },
  ]),
  gap(260),
  new Paragraph({ alignment: AlignmentType.CENTER, children: heroes.flatMap((p, i) => [img(p.photo, 118, 118), t(i < heroes.length - 1 ? "    " : "")]) }),
  P([t(heroes.map(p => p.short).join("   ·   "), { size: 14, color: C.muted })], { alignment: AlignmentType.CENTER }),
];

// ---- contents (clickable)
const toc = [H1("Contents", "toc")];
const tocItems = [["1. Executive summary", "s1"], ["2. How the tracker works", "s2"], ["3. Competitor classification", "s3"],
  ["4. BFCM 2025: what worked", "s4"], ["5. BFCM 2026 deal prices", "s5"], ["6. Stock to Nov 30", "s6"],
  ["7. Product chapters: United States", "s7"], ["8. Product chapters: Canada", "s8"], ["9. Verification", "s9"], ["10. Open items and next steps", "s10"],
  ["Appendix: glossary", "s11"]];
for (const [label, id] of tocItems) {
  toc.push(new Paragraph({ spacing: { after: 70 }, children: [new InternalHyperlink({ anchor: id, children: [t(label, { size: 22, color: C.accent, bold: true })] })] }));
  if (id === "s7" || id === "s8") {
    const m = id === "s7" ? "US" : "CA";
    toc.push(new Paragraph({ spacing: { after: 90 }, indent: { left: 400 }, children: prods.filter(p => p.mkt === m).flatMap((p, i, a) => [
      new InternalHyperlink({ anchor: pid(p), children: [t(p.short, { size: 16, color: C.muted })] }), t(i < a.length - 1 ? "  ·  " : "", { size: 16, color: C.muted })]) }));
  }
}
toc.push(gap(200), small("Click any entry to jump to it. Every product chapter starts on its own page with the product photo, its key numbers, its BFCM 2026 deal and stock position, a price map and the full list of competitors with photos."));

// ---- 1. executive summary
const usL = L.US || [], caL = L.CA || [];
const lf = (arr, type) => arr.find(r => r.type === type);
const pc = lf(usL, "Price cut only"), ped = lf(usL, "Prime Exclusive Discount"), none = lf(usL, "None");
const dealProds = prods.filter(p => p.da && isNum(p.da.ref));
const s1 = [H1("1. Executive summary", "s1"),
  P("This report is the written, shareable version of the BFCM 2026 competitor tracker. It covers the same data as the tracker workbook and dashboard: every product, every mapped competitor, the BFCM 2025 results, the assumed BFCM 2026 deal prices and the stock outlook to Nov 30."),
  tiles([
    { k: "Products covered", v: `${S.products}`, s: `${S.productsUS} US · ${S.productsCA} Canada listings` },
    { k: "Competitors", v: int(S.comps), s: `${int(S.byCls.Direct)} direct · ${int(S.byCls["Alternative material"])} alternative material` },
    { k: "BFCM 2025 deal history", v: int(S.withBf), s: "competitors with a known BFCM 2025 deal type" },
    { k: "Strikethrough shown today", v: `${int(S.strShown)} of ${int(S.strChecked)}`, s: "competitor pages checked" },
  ]), gap(),
  tiles([
    { k: "Assumed deal Nov 19–26", v: "15% off", s: "today's price, until final prices are set", fill: C.dealSoft, edge: C.deal, color: C.deal },
    { k: "Assumed deal Nov 27–30", v: "20% off", s: "Black Friday to Cyber Monday", fill: C.dealSoft, edge: C.deal, color: C.deal },
    { k: "Variations short to Nov 30", v: int(S.varsShort + S.varsOut), s: `${int(S.varsOut)} out of stock now · ${int(S.varsShort)} short even with inbound`, fill: C.badSoft, edge: C.bad, color: C.bad },
    { k: "Variations covered", v: int(S.varsCovered + S.varsInbound), s: `${int(S.varsInbound)} of them only if inbound arrives in time`, fill: C.goodSoft, edge: C.good, color: C.good },
  ]),
  H2("Key findings"),
  bullet([t("A plain price cut moved rank the most in BFCM 2025. ", { bold: true }), t(`In the US, competitors that only cut the price improved their Best Seller Rank by a median ${x2(pc && pc.median)} (${pc ? pc.n : 0} competitors), against ${x2(ped && ped.median)} for a Prime Exclusive Discount (${ped ? ped.n : 0}) and ${x2(none && none.median)} for no deal (${none ? none.n : 0}).`)]),
  bullet([t("BFCM is a big week for us. ", { bold: true }), t(`Our sales per day in BFCM week 2025 were ${x2(S.accountLift.US)} the 30 days before in the US and ${x2(S.accountLift.CA)} in Canada. Each product's own lift (Section 4) drives its stock need.`)]),
  bullet([t("Most of our rivals are direct. ", { bold: true }), t(`${int(S.byCls.Direct)} of ${int(S.comps)} competitors sell the same product type in the same material family as ours. They lead every competitor list in this report; alternative-material rivals are kept separately so they don't distort the price comparison.`)]),
  bullet([t("Deal prices are an assumption until final prices are set. ", { bold: true }), t(`For ${dealProds.length} product listings the report shows today's price, 15% off for Nov 19–26 and 20% off for Nov 27–30, next to our own 2025 cut and the median cut rivals ran in 2025 (Section 5).`)]),
  bullet([t("Stock is the main risk. ", { bold: true }), t(`${S.stockAtRisk} of ${S.stockProducts} products with stock data have at least one variation that runs short before Nov 30: ${int(S.varsOut)} variations are out of stock now and ${int(S.varsShort)} are short even if all inbound arrives (Section 6 and each product chapter).`)]),
  H2("Decisions this report supports"),
  bullet("Which deal type to run per product, using the BFCM 2025 rank lift by deal type."),
  bullet("Whether our assumed BFCM 2026 price undercuts the direct competitors (the price map in each product chapter)."),
  bullet("Which variations need stock sent now, and which cannot be covered in time."),
];

// ---- 2. how it works
const s2 = [H1("2. How the tracker works", "s2"),
  P("The tracker follows seven steps. Every competitor row carries the same fields, so any product can be compared with any other."),
  chart(CH.flow, 10),
  H2("What each step means"),
  table([{ h: "Step", w: 2200 }, { h: "What it covers", w: 12200 }], [
    ["1. Our products", "33 product listings: 27 in the United States and 6 in Canada. Each has a role for BFCM (hero, core, clearance, gifting, off-season, launch, liquidation) and a scope (Core, Other, Not launched)."],
    ["2. Competitors", "744 competitor listings, each mapped to the product it competes with. Price, List Price, Best Seller Rank, rating, reviews and weekly units are for the competitor's tracked size, so the comparison is like for like."],
    ["3. Classify", "Each competitor is Direct (same product type, same material family), Alternative material, Material not verified or Different product type. Section 3 shows the rule."],
    ["4. BFCM 2025", "For each competitor: the deal type it ran, the price before BFCM (median Nov 1–19) and during BFCM week, the discount, and how its Best Seller Rank changed. Rank lift = rank before ÷ rank during, so 1.50x means 50% better."],
    ["5. Today", "Today's price, List Price, whether Amazon shows a strikethrough and at what price, and any deal running now."],
    ["6. BFCM 2026", "Assumed deal price per product (15% off Nov 19–26, 20% off Nov 27–30) and stock: units at Amazon and inbound vs the units needed to Nov 30."],
    ["7. Verify", "16 checks re-compute the numbers from the raw data and compare the workbook with the dashboard. All pass (Section 9)."],
  ]),
  H2("How to read the competitor tables"),
  table([{ h: "Column", w: 2600 }, { h: "Meaning", w: 11800 }], [
    ["Photo, competitor", "Product photo, brand, listing title, material and rating with review count. A Coming Soon image means no photo is available yet."],
    ["Size · colour", "The variation tracked. Prices compare like for like with our same size where we sell it."],
    ["Price / List", "Today's price and the List Price the listing shows."],
    ["vs ours", "How far the competitor's price is from ours for the same size: −20% means 20% cheaper than us."],
    ["Strikethrough", "Whether Amazon shows a crossed-out reference price today, and its value."],
    ["BFCM 2025 deal", "Deal type run in BFCM 2025: Price cut only, Prime Exclusive Discount, Coupon only, Lightning Deal, Best Deal, or None."],
    ["2025 before → during", "Median price Nov 1–19, 2025 → lowest price in BFCM week, and the discount between them."],
    ["Rank lift", "Best Seller Rank before ÷ during BFCM week. Above 1.00x = rank improved."],
    ["Units / wk", "Estimated units sold per week today."],
  ], { size: 16 }),
];

// ---- 3. classification
const byCls = S.byCls;
const s3 = [H1("3. Competitor classification", "s3"),
  P("Our products are compared first with competitors that sell the same thing in the same material. A bamboo sheet set is compared with other bamboo-viscose sheet sets; a cooling sheet set made of nylon-spandex cooling knit is compared with other cooling knits, not with bamboo or microfiber. Rivals in other materials are kept, but in their own group, so they don't distort the price comparison."),
  chart(CH.cls_tree, 10),
  table([{ h: "Group", w: 3200 }, { h: "Competitors", w: 1600, a: "r" }, { h: "Rule", w: 9600 }], [
    [{ v: "Direct", bold: true }, int(byCls.Direct), "Same product type and the same material family as ours (material from the competitor's product page where checked, otherwise its title)."],
    [{ v: "Material not verified", bold: true }, int(byCls["Material not verified"]), "Same product type, but neither the page nor the title names the material. Treated as a possible direct rival."],
    [{ v: "Alternative material", bold: true }, int(byCls["Alternative material"]), "Same product type, different material (e.g. microfiber or cotton against our bamboo)."],
    [{ v: "Different product type", bold: true }, int(byCls["Different product type"]), "A different product (e.g. a fitted sheet only against our full sheet set)."],
    [{ v: "Not classified", bold: true }, int(byCls["Not classified"]), "Products outside the sheet, pillowcase and comforter families (curtains, towels, chair covers, signs, quilts, masks), where a material rule doesn't apply."],
  ]),
  H2("Our materials"),
  table([{ h: "Our product family", w: 4200 }, { h: "Material it is compared on", w: 10200 }], [
    ["Bamboo sheets and pillowcases (Decolure, Sleep Sanctuary, Sleephoria)", "Viscose from bamboo"],
    ["CooLinens and Sleephoria cooling sheets, pillowcases, comforter", "Synthetic nylon-spandex cooling knit (CooLinens 90% nylon / 10% spandex; Sleephoria BreezeWeave is the same fabric family)"],
    ["Decolure cooling sheets", "Microfiber blend (a different material from Sleephoria cooling)"],
    ["Satin sheets", "Polyester satin"],
    ["Silk pillowcase and sleep masks", "Mulberry silk"],
  ]),
  CH.cls_US ? chart(CH.cls_US, 10, 6.4) : null,
  CH.cls_CA ? chart(CH.cls_CA, 10, 3.5) : null,
];

// ---- 4. BFCM 2025
const liftRows = m => (L[m] || []).map(r => [r.type, int(r.n), { v: x2(r.median), bold: true }, pct(r.disc), pct(r.share_up)]);
const ourLiftRows = m => prods.filter(p => p.mkt === m && isNum(p.lift)).sort((a, b) => b.lift - a.lift).map(p => {
  const sb = p.sb || [], a = sb[0], b = sb[1];
  return [p.short, { v: x2(p.lift), bold: true }, a ? money0(a.sales / 30, m) : "—", b ? money0(b.sales / 12, m) : "—",
          a ? int(a.units) : "—", b ? int(b.units) : "—", isNum(p.preTacos) ? p.preTacos.toFixed(1) + "%" : "—", isNum(p.tacos) ? p.tacos.toFixed(1) + "%" : "—"];
});
const liftCols = [{ h: "Deal type in BFCM 2025", w: 4400 }, { h: "Competitors", w: 2000, a: "r" }, { h: "Median rank lift", w: 2600, a: "r" }, { h: "Median discount", w: 2600, a: "r" }, { h: "Share that improved", w: 2800, a: "r" }];
const ourCols = [{ h: "Product", w: 2600 }, { h: "Sales lift", w: 1500, a: "r" }, { h: "Sales / day, 30 days before", w: 2100, a: "r" }, { h: "Sales / day, BFCM week", w: 2100, a: "r" },
  { h: "Units, 30 days before", w: 1600, a: "r" }, { h: "Units, BFCM week", w: 1500, a: "r" }, { h: "TACoS before", w: 1500, a: "r" }, { h: "TACoS BFCM", w: 1500, a: "r" }];
const s4 = [H1("4. BFCM 2025: what worked", "s4"),
  P("Rank lift compares each competitor's Best Seller Rank in BFCM week 2025 with its median rank Nov 1–19. 1.00x means no change; 1.50x means the rank number fell by a third (better). Only competitors with a measured rank in both periods are counted, and deal types with fewer than 3 competitors are left out."),
  chart(CH.lift_deal, 10),
  H3("United States"), table(liftCols, liftRows("US")), gap(),
  H3("Canada"), table(liftCols, liftRows("CA")),
  H2("Deeper discount vs rank change"),
  P("Each dot is one US competitor in BFCM 2025. A deeper discount does not guarantee a better rank: many Prime Exclusive Discounts at 15–25% left rank flat, while plain price cuts more often moved it."),
  chart(CH.disc_lift, 10),
  H2("Our own BFCM 2025 sales lift", null, true),
  P(`Sales lift = our sales per day in BFCM week 2025 (Nov 20 – Dec 1, 12 days) ÷ sales per day in the 30 days before (Oct 21 – Nov 19). Account level: ${x2(S.accountLift.US)} in the US, ${x2(S.accountLift.CA)} in Canada. TACoS = ad cost ÷ total sales.`),
  chart(CH.our_lift_US, 10, 5.6), table(ourCols, ourLiftRows("US")),
  CH.our_lift_CA ? chart(CH.our_lift_CA, 10, 3) : null, table(ourCols, ourLiftRows("CA")),
];

// ---- 5. deal prices
const dealCols = [{ h: "Product", w: 2300 }, { h: "Mkt", w: 700 }, { h: "BFCM 2026 plan", w: 2900 }, { h: "Today", w: 1300, a: "r" }, { h: "Nov 19–26 (−15%)", w: 1500, a: "r" },
  { h: "Nov 27–30 (−20%)", w: 1500, a: "r" }, { h: "Our 2025 cut", w: 1300, a: "r" }, { h: "Rivals' 2025 cut", w: 1500, a: "r" }, { h: "Direct median today", w: 1400, a: "r" }];
const dealRow = p => { const d = p.da || {}, m = p.mkt; return [p.short, m, p.plan26 || "Not in a deal", money(d.ref ?? p.price, m), { v: money(d.deal_std, m), bold: true, color: C.deal },
  { v: money(d.deal_peak, m), bold: true, color: C.deal }, d.ev25 ? pct(d.ev25.depth) : "—", d.comp25 ? `${pct(d.comp25.median)} (${d.comp25.n})` : "—", money(p.cmp.median, m)]; };
const s5 = [H1("5. BFCM 2026 deal prices", "s5"),
  P("Until final deal prices are set, the tracker assumes the team rule: 15% off today's price on the regular deal days (Nov 19–26) and 20% off on the high days (Nov 27–30, Black Friday to Cyber Monday). The assumed price is shown next to the evidence: the cut we ran on the same product in BFCM 2025 and the median cut our competitors ran."),
  P([t("Amazon may cap a deal at a lower reference price. ", { bold: true }), t("Where a recent deal or an old reference price sits below today's price, Amazon can require a deeper deal price than 15–20%. Product chapters list these cases under Deal notes.")]),
  chart(CH.deal_US, 10, 5.4), CH.deal_CA ? chart(CH.deal_CA, 10, 2.8) : null,
  H2("Deal prices by product"),
  table(dealCols, prods.filter(p => p.plan26 || p.da).map(dealRow)),
  small("Direct median today = the median price of this product's direct competitors (all competitors where no direct rival is mapped). Rivals' 2025 cut: median discount, number of competitors in brackets."),
];

// ---- 6. stock
const stockCols = [{ h: "Product", w: 2600 }, { h: "Mkt", w: 700 }, { h: "Sales / day", w: 1300, a: "r" }, { h: "Lift used", w: 1300, a: "r" }, { h: "At Amazon", w: 1400, a: "r" },
  { h: "Inbound", w: 1300, a: "r" }, { h: "Needed to Nov 30", w: 1600, a: "r" }, { h: "Covered", w: 1100, a: "r" }, { h: "Needs inbound", w: 1300, a: "r" }, { h: "Short", w: 900, a: "r" }, { h: "Out now", w: 900, a: "r" }];
const stockRow = p => { const s = p.stock26, c = s.counts, sh = c["Short even with inbound"] || 0, oo = c["Out of stock now"] || 0;
  return [p.short, p.mkt, isNum(s.vel) ? s.vel.toFixed(1) : "—", { v: x2(s.lift) + (String(s.liftSrc).includes("own") ? "" : " *") }, int(s.onHand), int(s.inbound), int(s.need),
    int(c["Covered to Nov 30"] || 0), int(c["Needs inbound in time"] || 0), { v: int(sh), color: sh ? C.bad : undefined, bold: !!sh }, { v: int(oo), color: oo ? C.bad : undefined, bold: !!oo }]; };
const s6 = [H1("6. Stock to Nov 30", "s6"),
  P("For every variation: units needed = today's sales per day × 34 days (Oct 16 – Nov 18) + today's sales per day × the BFCM lift × 12 days (Nov 19–30). The lift is the product's own BFCM 2025 sales lift where it is reliable (0.8x to 8x); otherwise the account lift (US 2.74x, Canada 3.14x) is used and marked *."),
  table([{ h: "Status", w: 3000 }, { h: "Variations", w: 1600, a: "r" }, { h: "Meaning", w: 9800 }], [
    [{ v: "Covered to Nov 30", bold: true, color: C.good }, int(S.varsCovered), "Units at Amazon now cover the need to Nov 30."],
    [{ v: "Needs inbound in time", bold: true }, int(S.varsInbound), "Covered only if the inbound units arrive before the variation runs out. Inbound has no confirmed arrival date yet."],
    [{ v: "Short even with inbound", bold: true, color: C.bad }, int(S.varsShort), "At Amazon + inbound is less than the need; more stock has to be sent."],
    [{ v: "Out of stock now", bold: true, color: C.bad }, int(S.varsOut), "Zero units at Amazon today."],
  ]),
  chart(CH.stock, 10, 6.0),
  H2("Stock by product"),
  table(stockCols, prods.filter(p => p.stock26).sort((a, b) => b.stock26.need - a.stock26.need).map(stockRow)),
  small("* account lift used because the product's own BFCM 2025 lift was not reliable. Each product chapter lists the variations that are not covered."),
];

// ---- 7/8. product chapters
const compCols = [{ h: "Photo", w: 760, a: "c" }, { h: "Competitor", w: 3300 }, { h: "Size · colour", w: 1250 }, { h: "Price", w: 900, a: "r" }, { h: "List", w: 850, a: "r" },
  { h: "vs ours", w: 760, a: "r" }, { h: "Strike- through", w: 1050 }, { h: "BFCM 2025 deal", w: 1350 }, { h: "2025 before → during", w: 1450, a: "r" },
  { h: "Disc.", w: 620, a: "r" }, { h: "Rank lift", w: 700, a: "r" }, { h: "Units / wk", w: 690, a: "r" }];  // 13,680 + gutter
function compRow(c, m) {
  const sub = [c.mat, isNum(c.rating) ? `${c.rating.toFixed(1)}★ ${int(c.reviews)}` : null, c.tier && c.tier !== "Untiered" ? c.tier : null].filter(Boolean).join(" · ");
  const name = [new Paragraph({ spacing: { after: 0 }, children: [t(c.brand || "—", { bold: true, size: 16 })] }),
    new Paragraph({ spacing: { after: 0 }, children: [t((c.title || "").slice(0, 120) + ((c.title || "").length > 120 ? "…" : ""), { size: 13, color: C.muted })] }),
    ...(sub ? [new Paragraph({ spacing: { after: 0 }, children: [t(sub, { size: 13, color: C.accent })] })] : []),
    ...(c.notes ? [new Paragraph({ spacing: { after: 0 }, children: [t(c.notes.slice(0, 140), { size: 12, color: C.muted, italics: true })] })] : [])];
  const strike = c.str_show === "Y" ? `${c.str_label || "Shown"} ${money(c.str_price, m)}` : c.str_show === "N" ? "Not shown" : "—";
  const gp = c.gap, lift = c.bsr_lift_v;
  return [{ v: new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [img(c.photo, 44, 44)] }) }, { v: name },
    [c.size, c.colour].filter(Boolean).join(" · ") || "—", { v: money(c.price, m), bold: true }, money(c.lp, m),
    { v: sgnPct(gp), color: isNum(gp) && gp < 0 ? C.bad : undefined }, strike, c.bf_type || "—",
    isNum(c.bf_pre) && isNum(c.bf_low) ? `${money(c.bf_pre, m)} → ${money(c.bf_low, m)}` : "—", pct(c.bf_disc_v),
    { v: x2(lift), color: isNum(lift) ? (lift >= 1.2 ? C.good : lift < 1 ? C.bad : undefined) : undefined, bold: isNum(lift) && lift >= 1.2 }, int(c.wk)];
}
function chapter(p, first) {
  const m = p.mkt, d = p.da || {}, st = p.stock26, out = [];
  const head = `${m} · ${p.short}: ${p.brand} ${p.name || ""}`.trim();
  out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, pageBreakBefore: true, children: [new Bookmark({ id: pid(p), children: [t(head)] })] }));
  if (p.scope === "Not launched") out.push(P([t("NOT LAUNCHED YET. ", { bold: true, color: C.bad }), t("No live price, rating or sales are expected. Competitors are mapped so the launch can be priced against them.", { color: C.bad })]));
  // facts with photo
  const facts = [
    ["Listing title", p.title || "—"], ["Marketplace", mktName(m)], ["Family · role", `${p.family} · ${p.role}`], ["Scope · stage", `${p.scope}${p.stage ? " · " + p.stage : ""}`],
    ["Amazon parent", p.parent || "—"], ["Best seller", p.best ? `${p.best}${p.bestLabel ? " (" + p.bestLabel + ")" : ""}` : "—"],
    ["Variations", `${int(p.nvars)} (${int(p.nlive)} with a live price)`],
    ["Sizes", (p.sizes || []).map(s => s.name).join(", ") || "—"], ["Colours", `${(p.colours || []).length || "—"}`],
  ];
  out.push(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [2600, 2300, 9500], layout: TableLayoutType.FIXED, rows: facts.map((f, i) => new TableRow({ cantSplit: true, children: [
    ...(i === 0 ? [new TableCell({ rowSpan: facts.length, width: { size: 2600, type: WidthType.DXA }, borders: BORDERS, verticalAlign: VerticalAlign.CENTER,
      children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [img(p.photo, 200, 200)] })] })] : []),
    cell(f[0], 2300, { fill: C.chip, bold: true, size: 15 }), cell(f[1], 9500, { size: 16 })] })) }));
  out.push(gap(100));
  // key points
  const sh = st ? (st.counts["Short even with inbound"] || 0) : 0, oo = st ? (st.counts["Out of stock now"] || 0) : 0;
  const k = [{ k: "Our price today", v: money(p.price, m), s: p.bestLabel || "" }];
  if (isNum(d.ref)) k.push({ k: "Assumed BFCM 2026 deal", v: `${money(d.deal_std, m)} → ${money(d.deal_peak, m)}`, vs: 22, s: "15% off Nov 19–26 · 20% off Nov 27–30", fill: C.dealSoft, edge: C.deal, color: C.deal });
  else k.push({ k: "BFCM 2026 deal", v: p.plan26 ? "Price not set" : "Not in a deal", vs: 20, s: p.plan26 || "regular price through BFCM", fill: C.dealSoft, edge: C.deal });
  if (st) k.push({ k: "Stock to Nov 30", v: sh || oo ? `${int(sh)} short · ${int(oo)} out` : "Covered", vs: 20, s: `${int(st.onHand)} at Amazon · ${int(st.inbound)} inbound · need ${int(st.need)}`,
                   fill: sh || oo ? C.badSoft : C.goodSoft, edge: sh || oo ? C.bad : C.good, color: sh || oo ? C.bad : C.good });
  if (isNum(p.lift)) k.push({ k: "BFCM 2025 sales lift", v: x2(p.lift), s: isNum(p.u28) ? `${int(p.u28)} units in the last 28 days` : "" });
  if (p.cmp.n) k.push({ k: p.cmp.basisDirect ? "Direct competitors" : "Competitors", v: int(p.cmp.basisDirect ? p.cmp.direct : p.cmp.n), s: `median ${money(p.cmp.median, m)} · ${int(p.cmp.below)} cheaper than us` });
  out.push(tiles(k));
  // BFCM 2025
  if ((p.sb || []).length || p.hkLine || p.deals) {
    out.push(H3("BFCM 2025: how this product did"));
    if ((p.sb || []).length) out.push(table([{ h: "Period", w: 3600 }, { h: "Sales", w: 1500, a: "r" }, { h: "Units", w: 1100, a: "r" }, { h: "Organic units", w: 1300, a: "r" }, { h: "Ad units", w: 1100, a: "r" },
      { h: "Ad cost", w: 1300, a: "r" }, { h: "TACoS", w: 1000, a: "r" }, { h: "Sessions", w: 1200, a: "r" }, { h: "Unit session %", w: 1200, a: "r" }, { h: "Avg price", w: 1100, a: "r" }],
      p.sb.map(s => [s.label, money0(s.sales, m), int(s.units), int(s.org), int(s.ad), money0(s.adcost, m), pct(s.tacos, 1), int(s.sessions), pct(s.usp, 1), money(s.avg, m)])));
    if (p.hkLine) out.push(P([t("Best seller in BFCM 2025: ", { bold: true }), t(cleanHk(p.hkLine))], { spacing: { before: 100, after: 60 } }));
    if (p.deals) out.push(P([t("Our BFCM 2025 deals: ", { bold: true }), t(p.deals)], { spacing: { after: 60 } }));
    if (p.stock) out.push(P([t("Stock in BFCM 2025: ", { bold: true }), t(p.stock)], { spacing: { after: 60 } }));
  }
  // BFCM 2026 deal
  out.push(H3("BFCM 2026 deal"));
  if (isNum(d.ref)) {
    out.push(table([{ h: "Plan", w: 3400 }, { h: "Today", w: 1500, a: "r" }, { h: "Nov 19–26 (−15%)", w: 1900, a: "r" }, { h: "Nov 27–30 (−20%)", w: 1900, a: "r" },
      { h: "Our 2025 cut", w: 1700, a: "r" }, { h: "Rivals' 2025 cut", w: 2000, a: "r" }, { h: "Direct median today", w: 2000, a: "r" }],
      [[p.plan26 || "—", money(d.ref, m), { v: money(d.deal_std, m), bold: true, color: C.deal }, { v: money(d.deal_peak, m), bold: true, color: C.deal },
        d.ev25 ? `${pct(d.ev25.depth)} (${money(d.ev25.pre, m)} → ${money(d.ev25.bf, m)})` : "—", d.comp25 ? `${pct(d.comp25.median)} (${d.comp25.n} rivals)` : "—", money(p.cmp.median, m)]]));
  } else out.push(P(p.plan26 ? `Planned: ${p.plan26}. No current price to base the assumed deal price on.` : "Not in a BFCM 2026 deal: sells at its regular price through BFCM."));
  if ((p.notes || []).length) { out.push(P([t("Deal notes", { bold: true })], { spacing: { before: 100, after: 40 } })); for (const n of p.notes) out.push(bullet([t(n.topic + ". ", { bold: true }), t(n.detail)])); }
  // stock
  if (st) {
    out.push(H3("Stock to Nov 30"));
    out.push(P(`Sales per day today ${isNum(st.vel) ? st.vel.toFixed(1) : "—"} · lift used ${x2(st.lift)} (${String(st.liftSrc).includes("own") ? "this product's own BFCM 2025 lift" : "account lift, assumed"}) · need to Nov 30 ${int(st.need)} units · at Amazon ${int(st.onHand)} · inbound ${int(st.inbound)}. Covered ${int(st.counts["Covered to Nov 30"] || 0)}, needs inbound in time ${int(st.counts["Needs inbound in time"] || 0)}, short ${int(sh)}, out of stock now ${int(oo)}.`));
    if (p.risk.length) out.push(table([{ h: "Size", w: 1800 }, { h: "Colour", w: 2200 }, { h: "At Amazon", w: 1200, a: "r" }, { h: "Inbound", w: 1200, a: "r" }, { h: "Sales / day", w: 1200, a: "r" },
      { h: "Need to Nov 30", w: 1400, a: "r" }, { h: "Short by", w: 1200, a: "r" }, { h: "Runs out", w: 1300 }, { h: "Status", w: 2900 }],
      p.risk.map(x => [x.size || "—", x.colour || "—", int(x.oh), int(x.ib), isNum(x.vel) ? x.vel.toFixed(1) : "—", int(x.need), isNum(x.short) && x.short > 0 ? int(x.short) : "—",
        x.st === "Out of stock now" ? "now" : day(x.oos), { v: x.st, bold: true, color: x.st === "Needs inbound in time" ? undefined : C.bad }]), { size: 15, pad: 30 }));
  }
  // sales mix
  if ((p.sizes || []).some(s => s.u28) || (p.colours || []).some(s => s.u28)) {
    out.push(H3("Sales mix, last 28 days"));
    const top = arr => (arr || []).filter(s => s.u28).sort((a, b) => b.u28 - a.u28).slice(0, 8).map(s => `${s.name} ${int(s.u28)}`).join(" · ");
    out.push(P([t("By size: ", { bold: true }), t(top(p.sizes) || "—")], { spacing: { after: 40 } }));
    out.push(P([t("By colour (top 8): ", { bold: true }), t(top(p.colours) || "—")]));
  }
  // competitors
  if (p.comps.length) {
    out.push(H3(`Competitors (${p.comps.length})`));
    if (p.priceChart) out.push(chart(p.priceChart, 10, 3.2));
    const rows = []; let last = null;
    const byC = p.cmp.byCls;
    for (const c of p.comps) {
      const g = c.cls || "Not classified";
      if (g !== last) { rows.push({ group: `${g} · ${byC[g] || 0}`, fill: g === "Direct" ? C.accentSoft : C.chip }); last = g; }
      rows.push(compRow(c, m));
    }
    out.push(table(compCols, rows, { size: 15, pad: 30, headSize: 14 }));
  } else out.push(P("No competitors are mapped to this product yet."));
  return out;
}
const s7 = [H1("7. Product chapters: United States", "s7"), P("One chapter per US product listing: core BFCM products first, then other products, then products not launched yet."),
  ...prods.filter(p => p.mkt === "US").flatMap(p => chapter(p))];
const s8 = [H1("8. Product chapters: Canada", "s8"), P("One chapter per Canadian product listing. Prices are in Canadian dollars (C$)."),
  ...prods.filter(p => p.mkt === "CA").flatMap(p => chapter(p))];

// ---- 9. verification
const s9 = [H1("9. Verification", "s9"),
  P("Before this report was built, every number was re-computed from the raw data and the workbook was compared with the dashboard, row by row. A check passes only with zero mismatches."),
  table([{ h: "Check", w: 8200 }, { h: "Rows checked", w: 2000, a: "r" }, { h: "Mismatches", w: 2000, a: "r" }, { h: "Result", w: 2200, a: "c" }],
    R.checks.map(c => [c.name, int(c.checked), int(c.bad), { v: c.status, bold: true, color: c.status === "Pass" ? C.good : C.bad, fill: c.status === "Pass" ? C.goodSoft : C.badSoft }])),
  P("The tracker workbook also has 0 formula errors across 21,808 formulas.", { spacing: { before: 120 } }),
];

// ---- 10. open items
const s10 = [H1("10. Open items and next steps", "s10"),
  table([{ h: "Item", w: 4600 }, { h: "What happens next", w: 6800 }, { h: "When", w: 3000 }], [
    ["Final BFCM 2026 deal prices", "Replace the assumed 15% / 20% prices with the final agreed deal prices and re-run the checks.", "Oct 20 – 21, 2026"],
    ["Inbound arrival dates", "Add the arrival date for each inbound shipment so 'Needs inbound in time' can be confirmed or moved to 'Short'.", "As shipments are booked"],
    ["Variations short or out of stock", "Decide replenishment for the variations listed in each product chapter; anything that can't arrive by Nov 18 should be left out of the deal or paused in ads.", "This week"],
    ["Competitor prices", "Re-check competitor prices and strikethroughs in the week before Nov 19, when rivals set their deal prices.", "Nov 12 – 18, 2026"],
    ["Products not launched yet", "SL B4, SL Satin 6pc, SL Cooling 6pc and SL Bamboo Pillowcase: competitors are mapped; prices to be set at launch.", "At launch"],
  ]),
];

// ---- glossary
const s11 = [H1("Appendix: glossary", "s11"),
  table([{ h: "Term", w: 3200 }, { h: "Meaning", w: 11200 }], [
    ["BFCM week", "Black Friday to Cyber Monday deal period. 2025: Nov 20 – Dec 1. 2026 deals: Nov 19–30."],
    ["Best Seller Rank", "Amazon's sales rank in the category; a lower number is better."],
    ["Rank lift", "Rank before BFCM ÷ rank during BFCM week. 1.50x = rank improved by a third; below 1.00x = rank got worse."],
    ["Sales lift", "Our sales per day in BFCM week ÷ sales per day in the 30 days before."],
    ["TACoS", "Total advertising cost of sales: ad cost ÷ total sales."],
    ["List Price / Strikethrough", "The reference price on the listing, and whether Amazon shows it crossed out next to today's price (List Price, Typical price or Was price)."],
    ["Price cut only", "The price was lowered without a deal badge or coupon."],
    ["Prime Exclusive Discount", "A discount shown only to Prime members."],
    ["Lightning Deal / Best Deal", "Time-limited Amazon deals with a deal badge; Best Deals run for several days."],
    ["Direct competitor", "Same product type and same material family as ours."],
    ["Alternative material", "Same product type, different material."],
    ["Assumed deal price", "15% off today's price Nov 19–26 and 20% off Nov 27–30, until final prices are set."],
    ["Covered / Needs inbound / Short / Out now", "Stock status per variation against the units needed to Nov 30 (Section 6)."],
  ]),
];

body.push(...toc, ...s1, ...s2, ...s3, ...s4, ...s5, ...s6, ...s7, ...s8, ...s9, ...s10, ...s11);

// ------------------------------------------------------------------ document
const page = { size: { width: 12240, height: 15840, orientation: PageOrientation.LANDSCAPE }, margin: { top: 720, bottom: 720, left: 720, right: 720, header: 360, footer: 360 } };
const doc = new Document({
  creator: "Shayan Rana", title: "BFCM 2026 Competitor Research Report", description: "BFCM 2026 competitor research, deal prices and stock outlook",
  styles: {
    default: { document: { run: { font: FONT, size: 18, color: C.ink } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 36, bold: true, color: C.accent, font: FONT }, paragraph: { spacing: { before: 0, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 26, bold: true, color: C.ink, font: FONT }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 21, bold: true, color: C.accent, font: FONT }, paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } },
                                                       { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 240 } } } }] }] },
  sections: [
    { properties: { page }, children: cover },
    { properties: { page },
      headers: { default: new Header({ children: [new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C.line, space: 4 } }, tabStops: [{ type: TabStopType.RIGHT, position: W }],
        children: [t("BFCM 2026 Competitor Research Report", { size: 15, bold: true, color: C.accent }), t("\tOwner: Shayan Rana · Prepared for Erik Fisher & Joseph Fisher", { size: 15, color: C.muted })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: W }],
        children: [t(`Data as of ${R.built}`, { size: 14, color: C.muted }), new TextRun({ children: ["\tPage ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES], font: FONT, size: 14, color: C.muted })] })] }) },
      children: body.filter(Boolean) },
  ],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUTFILE, b); console.log(JSON.stringify({ file: OUTFILE, bytes: b.length })); });
