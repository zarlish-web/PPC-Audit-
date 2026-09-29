// Renders v2/out/doc_blocks.json to DOCX (US Letter). Usage: node render_doc.js <blocks.json> <out.docx>
const fs = require('fs');
const path = require('path');
const D = require(path.resolve('/tmp/claude-0/-home-user-PPC-Audit-/9ce1e055-11cb-5ecd-8379-78d9343956fb/scratchpad/node_modules/docx'));
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType, LevelFormat, BorderStyle } = D;
const blocks = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const FULL = 9360; // 6.5in content width in DXA
const children = [];
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
for (const b of blocks) {
  if (b.t === 'title') {
    children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun({ text: b.text, bold: true, size: 36 })] }));
    children.push(new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: b.sub, italics: true, color: '595959' })] }));
  } else if (b.t === 'h1') {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 280, after: 120 }, children: [new TextRun({ text: b.text })] }));
  } else if (b.t === 'h2') {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: b.text })] }));
  } else if (b.t === 'p') {
    children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: b.text })] }));
  } else if (b.t === 'ul') {
    for (const it of b.items) children.push(new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 80 }, children: [new TextRun({ text: it })] }));
  } else if (b.t === 'table') {
    const n = b.cols.length;
    let w = b.widths && b.widths.length === n ? b.widths.slice() : Array(n).fill(Math.floor(FULL / n));
    const sum = w.reduce((a, c) => a + c, 0);
    w = w.map(x => Math.floor(x * FULL / sum));
    w[n - 1] += FULL - w.reduce((a, c) => a + c, 0);
    const mk = (txt, head) => new TableCell({
      borders, width: { size: 0, type: WidthType.DXA }, margins: { top: 40, bottom: 40, left: 80, right: 80 },
      shading: head ? { fill: '1F3864', type: ShadingType.CLEAR, color: 'auto' } : undefined,
      children: [new Paragraph({ children: [new TextRun({ text: String(txt), size: 16, bold: !!head, color: head ? 'FFFFFF' : undefined })] })] });
    const rows = [new TableRow({ tableHeader: true, children: b.cols.map((c, i) => { const x = mk(c, true); x.options = x.options; return x; }) })];
    for (const r of b.rows) rows.push(new TableRow({ children: r.map(c => mk(c, false)) }));
    // set per-cell widths
    rows.forEach(row => row.options && row.options.children);
    const tbl = new Table({ width: { size: FULL, type: WidthType.DXA }, columnWidths: w,
      rows: [b.cols, ...b.rows].map((r, ri) => new TableRow({ tableHeader: ri === 0, children: r.map((c, ci) => new TableCell({
        borders, width: { size: w[ci], type: WidthType.DXA }, margins: { top: 40, bottom: 40, left: 80, right: 80 },
        shading: ri === 0 ? { fill: '1F3864', type: ShadingType.CLEAR, color: 'auto' } : undefined,
        children: [new Paragraph({ children: [new TextRun({ text: String(c), size: 16, bold: ri === 0, color: ri === 0 ? 'FFFFFF' : undefined })] })] })) })) });
    children.push(tbl);
    children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
  }
}
const doc = new Document({
  styles: { default: { document: { run: { font: 'Calibri', size: 20 } } } },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] }] },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1440, right: 1440 } } }, children }] });
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(process.argv[3], buf); console.log('wrote', process.argv[3], buf.length); });
