// Build the Word version of the CooLinens full-year plan review.
// Usage: node build_review_docx.js <review_items.json> <ppc_answers.json> <out.docx>
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, HeadingLevel, LevelFormat, BorderStyle, Header, Footer, PageNumber, PageBreak,
  TableLayoutType, ExternalHyperlink,
} = require("docx");

const [itemsPath, answersPath, outPath] = process.argv.slice(2);
const data = JSON.parse(fs.readFileSync(itemsPath, "utf8"));
const answers = JSON.parse(fs.readFileSync(answersPath, "utf8"));

const FONT = "Arial";
const INK = "1B2A33";
const MUTED = "5A6B75";
const ACCENT = "0F6E7A";
const LABEL_FILL = "EAF1F3";
const HEAD_FILL = "0F6E7A";
const LINE = "C9D5DA";
const CLASS_COLOUR = { "Confirmed issue": "A3271F", "Potential gap": "8A5A00", "Open question": "1F58A3" };
const W = 9360; // content width at 1" margins on Letter

const border = { style: BorderStyle.SINGLE, size: 4, color: LINE };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 70, bottom: 70, left: 110, right: 110 };

const run = (text, o = {}) => new TextRun({ text, font: FONT, size: o.size || 19, bold: o.bold, italics: o.italics, color: o.color || INK });
const para = (children, o = {}) => new Paragraph({ children: Array.isArray(children) ? children : [children], spacing: { after: o.after ?? 80, before: o.before ?? 0, line: 276 }, alignment: o.align, keepNext: o.keepNext });
const text = (t, o = {}) => para(run(t, o), o);
const bullet = (t, o = {}) => new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40, line: 264 }, children: Array.isArray(t) ? t : [run(t, o)] });
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, font: FONT })], spacing: { before: 280, after: 120 }, keepNext: true });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, font: FONT })], spacing: { before: 220, after: 100 }, keepNext: true });
const h3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: t, font: FONT })], spacing: { before: 200, after: 80 }, keepNext: true, keepLines: true });

function cell(children, width, o = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    borders, margins: cellMargins,
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    children: Array.isArray(children) ? children : [children],
  });
}
const cellText = (t, o = {}) => para(run(String(t), o), { after: 0 });

function grid(headers, rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const head = new TableRow({ tableHeader: true, cantSplit: true, children: headers.map((h, i) => cell(cellText(h, { bold: true, color: "FFFFFF", size: 18 }), widths[i], { fill: HEAD_FILL })) });
  const body = rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((v, i) => cell(Array.isArray(v) ? v : cellText(v, { size: 18, bold: i === 0 && ri >= 0 && widths.length > 1 ? false : false }), widths[i], { fill: ri % 2 ? "F6F9FA" : undefined })) }));
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED, rows: [head, ...body] });
}

function itemTable(it) {
  const L = 2300, R = W - L;
  const label = (t) => cell(cellText(t, { bold: true, size: 17, color: ACCENT }), L, { fill: LABEL_FILL });
  const row = (lab, content) => new TableRow({ cantSplit: false, children: [label(lab), cell(content, R)] });
  const refs = it.refs.length ? `  ·  Calls: ${it.refs.join(", ")}` : "";
  const also = it.also_on.length ? ` (also ${it.also_on.join(", ")})` : "";
  const rows = [
    row("Section / area", para([run(`${it.section} · `, { size: 18 }), run(it.area, { size: 18, bold: true })], { after: 0 })),
    row("Status", para([run(it.class, { size: 18, bold: true, color: CLASS_COLOUR[it.class] }), run(`  ·  ${it.priority}  ·  Owner: ${it.owner}`, { size: 18 })], { after: 0 })),
    row("Board", cellText(`${it.board}${also}${refs}`, { size: 17, color: MUTED })),
    row("Current status & evidence", it.evidence.map((e) => bullet([run(e.t, { size: 18 }), run(`  (${e.src})`, { size: 16, italics: true, color: MUTED })]))),
    row("Our observation / concern", cellText(it.observation, { size: 18 })),
    row("Our query", cellText(it.query, { size: 18, bold: true, color: "1F58A3" })),
    row("Our recommendation", cellText(it.rec, { size: 18 })),
    row("Expected outcome / next step", cellText(it.next, { size: 18 })),
  ];
  if (it.unavailable) rows.push(row("Not available", cellText(it.unavailable, { size: 18, italics: true, color: "8A5A00" })));
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [L, R], layout: TableLayoutType.FIXED, rows });
}

const m = data.meta;
const items = data.items;
const count = (f) => items.filter(f).length;
const P1 = items.filter((i) => i.priority === "P1");

const children = [];

// Title block
children.push(
  para(run("PPC TEAM REVIEW", { size: 18, bold: true, color: ACCENT }), { after: 60 }),
  para(run("CooLinens Cooling Sheets 4 Pc (69)", { size: 40, bold: true }), { after: 40 }),
  para(run("Full-Year Target Plan Review", { size: 32, color: MUTED }), { after: 240 }),
  grid(["Item", "Detail"], [
    ["Plan reviewed", `${m.plan}, ${m.plan_version}`],
    ["Live data", m.live_window],
    ["Prepared by", m.prepared_by],
    ["Date", "20 October 2026"],
    ["Scope", "Every section of the plan: growth plan, market and listing, returns, premium offer, competitors, keywords, push plan, pricing, promotions, PPC plan, COGS and fees, financial plan, seasonality, decisions"],
    ["Mode", m.mode],
  ], [2300, W - 2300]),
  para(run(""), { after: 120 }),
);

// 1. Executive summary
children.push(
  h1("1. Executive summary"),
  text(`The plan's direction is right: rank first at today's prices, use the light push as the pilot that sets the push budget, commit stock on the conservative line, and test every ad type. It needs revision before targets are stored. We logged ${items.length} items: ${count((i) => i.class === "Confirmed issue")} confirmed issues, ${count((i) => i.class === "Potential gap")} potential gaps and ${count((i) => i.class === "Open question")} open questions. ${P1.length} need an answer this week, most before the Oct 23 order.`),
  text("The three points that matter most:", { bold: true, after: 60 }),
  bullet([run("The size split runs opposite to sales. ", { bold: true }), run("The plan is Queen-led (45.8% of units) while King outsells Queen 1.4× before ads and 2.6× with ads. Re-split the Oct 23 order (F1).")]),
  bullet([run("Queen cannot move yet. ", { bold: true }), run("Its head keyword is held on profit bids, 8 of its 40 push keywords have no campaign, and Sleephoria is ranking-bidding the same search (K2, P4, P5).")]),
  bullet([run("The push cost is not calibrated. ", { bold: true }), run("Plan ads run about 4.5×, 7.8× and 19× live spend for Oct, Nov and Dec. Store the months only after the Nov 2 light-push read (A1, A8).")]),
  para(run(""), { after: 60 }),
  h2("How to read this document"),
  grid(["Label", "Meaning"], [
    ["Confirmed issue", "Verified on the boards or in live data: a contradiction, an error, or a mismatch with what is running"],
    ["Potential gap", "A risk or an assumption that early data puts in doubt"],
    ["Open question", "Needs an answer or a decision from the team"],
    ["P1 / P2 / P3", "P1 this week, before the Oct 23 order or the Oct 26 Cal King date · P2 before targets are stored · P3 clean-up"],
    ["Item IDs", "Reply with the ID (for example F1) so each answer maps to its item"],
  ], [2300, W - 2300]),
);

// 2. Key numbers
children.push(
  h1("2. Key numbers: plan against live"),
  text("October's plan pace matches live sales, but the size mix, the ad spend and the ACoS do not."),
  grid(["Measure", "Plan", "Live (13–20 Oct)", "Source"], [
    ["Units", "45,923 over 12 months; Oct 17.8/day, Nov 54.2/day, Dec 115.0/day", "17.25/day with ads (16–19 Oct); 9.7/day before ads (13–15 Oct)", "TCC_RU_PnL; Sellerboard"],
    ["Revenue", "$5.40M net of deal discounts ($5.57M gross at list, $5.15M after refunds)", "$6,107 sales on 16–19 Oct", "TCC_RU_PnL; Sellerboard"],
    ["Ads", "$753.4k (TACoS 14.0%); Oct $1,293/day, Nov $2,246/day, Dec $5,555/day", "$1,158.30 on 16–19 Oct (about $290/day); TACoS 19.0%", "TCC_RU_PnL, TCC_PPC_Money; Sellerboard"],
    ["ACoS vs break-even", "Break-even 39.1% after refunds (43.2% before)", "46.0% (29 orders, $2,517.71 ad sales)", "TCC_S1; Sellerboard"],
    ["CM4", "$1.92M; conservative $648.2k; stretch $4.29M", "Not measurable yet", "TCC_RU_Year, TCC_RU_Calls"],
    ["King : Queen", "Queen 21,027 units (45.8%), King 13,974 (30.4%); Oct Queen 7.9/day, King 6.4/day", "King 9.25/day, Queen 3.5/day with ads; 4.3 vs 3.0 before ads", "TCC_RU_Stock; Sellerboard"],
    ["FBA stock", "4,435 by colour at plan build", "4,365 on 20 Oct: King 1,099, Queen 1,808, Full 598, Twin 427, Cal King 433", "TCC_RU_Stock; Sellerboard"],
  ], [1500, 3000, 2860, 2000]),
);

// 3. Answers needed this week
children.push(
  h1("3. Answers needed this week"),
  text(`These ${P1.length} P1 items need an answer this week, most before the Oct 23 order. Cal King's push date is Oct 26.`),
  grid(["ID", "Topic", "Our query", "Owner"], P1.map((i) => [i.id, i.area, i.query, i.owner]), [600, 2300, 4560, 1900]),
);

// 4. PPC answers
children.push(
  h1("4. PPC answers"),
  text(answers.lead),
  h2("4.1 What the plan asks PPC to run"),
  grid(["Plan task", "Where", "Our status and answer (data to 20 Oct)", "Next"], answers.tasks.map((t) => [t.task, t.where, t.status, t.next]), [2300, 1300, 3660, 2100]),
  h2("4.2 Questions we expect from Joseph, with our answers"),
);
answers.qa.forEach((x) => {
  children.push(para(run(x.q, { bold: true, color: ACCENT }), { after: 30, keepNext: true }), text(x.a, { after: 120 }));
});

// 5. Findings by section
children.push(new Paragraph({ children: [new PageBreak()] }), h1("5. Findings by section"),
  text("Each item is mapped to the plan section and board it concerns, with the evidence and its source, our observation, our query, our recommendation and the expected outcome."));
let n = 0;
data.sections.forEach((s) => {
  const xs = items.filter((i) => i.section === s);
  if (!xs.length) return;
  n += 1;
  children.push(h2(`5.${n} ${s}`));
  xs.forEach((it) => children.push(h3(`${it.id} · ${it.area}`), itemTable(it), para(run(""), { after: 60 })));
});

// 6–8 appendices
children.push(
  h1("6. Information not available"),
  text("These inputs are missing from the plan files or not yet measurable. We have not assumed values for any of them."),
  grid(["Item", "Where it would sit", "Why it matters"], data.unavailable.map((u) => [u.item, u.where, u.impact]), [2600, 2500, 4260]),
  h1("7. Checked, no change needed"),
  text(`These ${data.no_change.length} parts of the plan were checked against the boards and live data and hold as they are.`),
  grid(["Area", "Finding"], data.no_change.map((x) => [x.area, x.note]), [3000, 6360]),
  h1("8. Sources and method"),
  text("Every figure quoted from a board was matched against that board's own text. Live figures were re-pulled on 20 Oct 2026. Calculations use only the figures named in the same item."),
  grid(["Label", "Source"], Object.entries(m.sources), [2000, 7360]),
  para([run("Plan board: ", { bold: true }), new ExternalHyperlink({ link: m.plan_url, children: [new TextRun({ text: m.plan_url, font: FONT, size: 19, color: ACCENT, underline: {} })] })], { before: 160 }),
  para([run("Daily recommendation board: ", { bold: true }), new ExternalHyperlink({ link: m.board_url, children: [new TextRun({ text: m.board_url, font: FONT, size: 19, color: ACCENT, underline: {} })] })]),
);

const doc = new Document({
  creator: "PPC team",
  title: "CooLinens Cooling Sheets 4 Pc: Full-Year Plan Review",
  styles: {
    default: { document: { run: { font: FONT, size: 19, color: INK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 30, bold: true, font: FONT, color: INK }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: FONT, color: ACCENT }, paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 21, bold: true, font: FONT, color: INK }, paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 300, hanging: 220 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1260, right: 1440, bottom: 1260, left: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE, space: 4 } }, children: [run("CooLinens Cooling Sheets 4 Pc · Full-Year Plan Review · PPC team", { size: 15, color: MUTED })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [run("Page ", { size: 15, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 15, color: MUTED }), run(" of ", { size: 15, color: MUTED }), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 15, color: MUTED })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outPath, buf); console.log("wrote", outPath, buf.length); });
