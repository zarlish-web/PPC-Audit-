const fs = require('fs');
const D = require('docx');
const {Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow,
       TableCell, WidthType, BorderStyle, ShadingType, TableOfContents, PageBreak,
       LevelFormat, convertInchesToTwip} = D;

const W = 10080;                       // Letter (12240) - 2*1080 margins
const INK='111827', INK2='4B5563', MUT='6B7480', ACC='14496F', RULE='D2D9E1',
      SUR='F6F8FA', RED='A32620', GRN='1B6B45', AMB='8F5B00';

const P = (t,o={}) => new Paragraph({
  spacing:{before:o.before??0, after:o.after??120, line:o.line??280},
  alignment:o.align, indent:o.indent,
  children:[new TextRun({text:t, size:o.size??20, bold:o.bold, italics:o.i,
    color:o.color??INK2, font:o.font??'IBM Plex Sans'})]
});
const RUNS = (runs,o={}) => new Paragraph({
  spacing:{before:o.before??0, after:o.after??120, line:280}, indent:o.indent,
  children:runs.map(r=>new TextRun({text:r.t, size:r.size??20, bold:r.b, italics:r.i,
    color:r.c??INK2, font:r.f??'IBM Plex Sans'}))
});
const H = (t,lvl) => new Paragraph({
  heading:lvl, spacing:{before:lvl===HeadingLevel.HEADING_1?360:280, after:140},
  children:[new TextRun({text:t, font:'Archivo',
    size:lvl===HeadingLevel.HEADING_1?30:lvl===HeadingLevel.HEADING_2?24:21,
    bold:true, color:lvl===HeadingLevel.HEADING_1?ACC:INK})]
});
const H1=t=>H(t,HeadingLevel.HEADING_1), H2=t=>H(t,HeadingLevel.HEADING_2), H3=t=>H(t,HeadingLevel.HEADING_3);

// monospace rule block
const CODE = lines => new Table({
  width:{size:W,type:WidthType.DXA}, columnWidths:[W],
  borders:{top:{style:BorderStyle.SINGLE,size:4,color:RULE},bottom:{style:BorderStyle.SINGLE,size:4,color:RULE},
           left:{style:BorderStyle.SINGLE,size:4,color:RULE},right:{style:BorderStyle.SINGLE,size:4,color:RULE},
           insideHorizontal:{style:BorderStyle.NONE},insideVertical:{style:BorderStyle.NONE}},
  rows:[new TableRow({children:[new TableCell({
    width:{size:W,type:WidthType.DXA},
    shading:{type:ShadingType.CLEAR, fill:SUR, color:'auto'},
    margins:{top:140,bottom:140,left:160,right:160},
    children:lines.map(l=>new Paragraph({spacing:{after:0,line:240},
      children:[new TextRun({text:l||' ',font:'IBM Plex Mono',size:17,color:INK2})]}))
  })]})]
});

// callout
const NOTE = (runs, color) => new Table({
  width:{size:W,type:WidthType.DXA}, columnWidths:[W],
  borders:{top:{style:BorderStyle.NONE},bottom:{style:BorderStyle.NONE},right:{style:BorderStyle.NONE},
           insideHorizontal:{style:BorderStyle.NONE},insideVertical:{style:BorderStyle.NONE},
           left:{style:BorderStyle.SINGLE,size:18,color:color||AMB}},
  rows:[new TableRow({children:[new TableCell({
    width:{size:W,type:WidthType.DXA},
    shading:{type:ShadingType.CLEAR, fill:'FAFBFC', color:'auto'},
    margins:{top:140,bottom:140,left:180,right:160},
    children:[RUNS(runs,{after:0})]
  })]})]
});

// table
function TBL(head, rows, widths){
  const cw = widths || head.map(()=>Math.floor(W/head.length));
  const cell=(txt,i,isHead)=>new TableCell({
    width:{size:cw[i],type:WidthType.DXA},
    shading:isHead?{type:ShadingType.CLEAR,fill:SUR,color:'auto'}:undefined,
    margins:{top:90,bottom:90,left:120,right:120},
    children:String(txt).split('\n').map(line=>new Paragraph({spacing:{after:0,line:250},
      children:[new TextRun({text:line, size:isHead?15:18, bold:isHead,
        color:isHead?MUT:INK2, font:isHead?'IBM Plex Mono':'IBM Plex Sans',
        allCaps:isHead})]}))
  });
  return new Table({
    width:{size:W,type:WidthType.DXA}, columnWidths:cw,
    borders:{top:{style:BorderStyle.SINGLE,size:4,color:RULE},bottom:{style:BorderStyle.SINGLE,size:4,color:RULE},
             left:{style:BorderStyle.SINGLE,size:4,color:RULE},right:{style:BorderStyle.SINGLE,size:4,color:RULE},
             insideHorizontal:{style:BorderStyle.SINGLE,size:2,color:RULE},
             insideVertical:{style:BorderStyle.SINGLE,size:2,color:RULE}},
    rows:[new TableRow({tableHeader:true, children:head.map((h,i)=>cell(h,i,true))}),
          ...rows.map(r=>new TableRow({children:r.map((c,i)=>cell(c,i,false))}))]
  });
}
const BUL = (t,o={}) => new Paragraph({
  numbering:{reference:'bul',level:0}, spacing:{after:80,line:270},
  children:[new TextRun({text:t,size:20,color:INK2,font:'IBM Plex Sans'})]
});

const body = [];
const add = (...x)=>body.push(...x);

// ---------- cover ----------
add(new Paragraph({spacing:{after:100},children:[new TextRun({text:'BUILD SPECIFICATION — DAILY TIER',
  font:'IBM Plex Mono',size:17,bold:true,color:ACC,characterSpacing:40})]}));
add(new Paragraph({spacing:{after:200},children:[new TextRun({text:'Campaign Daily Oversight',
  font:'Archivo',size:52,bold:true,color:INK})]}));
add(RUNS([
  {t:'The daily tier of the PPC Oversight System, as a screen. One product, one marketplace, day grain. A '},
  {t:'pinned product profile',b:true,c:INK},
  {t:' that everything below it reads from, and '},
  {t:'objective-led sub-tabs',b:true,c:INK},
  {t:' — because what a row targets, and what it is for, decide which columns can exist and how they are judged.'}
],{after:240,size:22}));
add(TBL(['Field','Value'],[
  ['Scope','One product × one marketplace, Sponsored Products / Brands / Display'],
  ['Grain','Day'],
  ['Sub-tabs','Six, objective-led'],
  ['Reads with','PPC Oversight System manual · config/thresholds.yml'],
  ['Version','1.0 · 5 September 2026'],
],[2600,7480]));
add(P('',{after:240}));
add(NOTE([
  {t:'Where the standing SOPs disagree with this spec on a threshold, a definition or a lever, the SOPs win. ',b:true,c:INK},
  {t:'This document was written from a design conversation, not from the SOP set — reconcile SOP 15 (Auto), 16 (PAT & Conquest), 17/18/19 (SB/SD), 23 (Ranking Push), 28 (Placement & Modifier), 29 (Negation) and 30 (Harvest) before building.'}
], RED));
add(new Paragraph({children:[new PageBreak()]}));

// ---------- TOC ----------
add(H1('Contents'));
add(new TableOfContents('Contents',{hyperlink:true,headingStyleRange:'1-2'}));
add(new Paragraph({children:[new PageBreak()]}));

// ---------- 1 ----------
add(H1('1 · Information architecture'));
add(P('One screen. The profile pins, the sub-tabs switch the table beneath it, and the lens toggles stay inside each tab — they are different views of the same campaigns, not different campaign types.',{after:180}));
add(CODE([
 '[ PINNED — PRODUCT PROFILE ]                      does not scroll away',
 '  Compact one row  ·  Expanded (click)',
 '',
 '[ SUB-TAB BAR ]   each label carries its exception count',
 '  Ranking (n) | Auto (n) | Manual (n) | Product & Category (n) | SB (n) | SD (n)',
 '',
 '[ SUBTOTAL STRIP ]',
 '  This tab: spend · sales · ACoS · % of product ad spend',
 '',
 '[ LENS TOGGLES ]  inside the tab, not peers of it',
 '  Keywords | Placement | Target | Ranks',
 '',
 '[ TABLE ]',
 '  Shared spine + that tab’s own columns'
]));
add(P('',{after:200}));
add(H2('1.1 · Date window'));
add(RUNS([{t:'The selector must offer 1d, and 1d is the default — this is the daily tier. ',b:true,c:INK},
 {t:'A bad yesterday is invisible inside a 30-day average, and the existing Performance Monitor defaults to 30d. Longer windows (7d / 14d / 30d / 90d) stay available for context, but the pass is run on 1d with the 7-day rolling figures beside it.'}],{after:200}));
add(H2('1.2 · Three rules that hold across the screen'));
add(TBL(['Rule','Why'],[
 ['The profile is context, not content','Every ceiling, gate and diagnosis below it reads from the profile. It stays pinned so nobody decides without it.'],
 ['Profile figures stay product-total','They do not react to the selected sub-tab — if they did, TACoS and organic sales would stop being coherent. The subtotal strip carries the tab’s own numbers.'],
 ['Tabs are objective-led','Objective is assigned from targeting type by the standing rule (Exact = Ranking, auto and broad = Discovery, product/category = Profitable Conversion, brand = Defensive), so the tabs land on the types listed above. Where the two diverge, objective wins: a brand-defence Exact campaign is Defensive and is judged on defence, not on rank gap. Keep a Defensive filter chip inside the Ranking tab for that case.'],
],[3000,7080]));

// ---------- 2 ----------
add(H1('2 · Product profile'));
add(P('Two states. A full profile block is 300–400px and would push the table off a laptop screen, so the pinned row carries only what gates a decision and everything else expands.',{after:180}));
add(H2('2.1 · Compact state (pinned)'));
add(CODE(['price + deal flag  ·  preferred variations (n live, lowest cover)',
          'advertised SKU now  ·  break-even ACoS  ·  max allowable CPC',
          'TACoS day / 7d  ·  exceptions (n)']));
add(P('',{after:200}));
add(H2('2.2 · Identity & economics'));
add(TBL(['Field','Notes'],[
 ['Thumbnail, title, parent & child ASIN, SKU, marketplace','—'],
 ['Current price · net price after deal','A running deal changes every number downstream of it.'],
 ['Deal','Type (Lightning / Best / Coupon / Promo), discount %, start–end, live Y/N'],
 ['Preferred variations','A table, not a single figure — days cover is per child ASIN, so a product-level number hides the variation actually at risk. One row per preferred variation: variation · SKU · advertised now? · units on hand · days cover · inbound · next shipment ETA. Backup variations listed beneath, marked as such.'],
 ['Days cover (per variation)','Read against the next shipment ETA, not in isolation: 19 days cover with stock landing on day 12 is fine; 19 days with nothing booked is a gate on ranking spend.'],
 ['COGS · Amazon fees · return rate','Compute margin on net units. Gross overstates it.'],
 ['Contribution margin per unit, before ads','—'],
 ['Break-even ACoS','contribution margin ÷ price  (the ACoS at which CM2 = 0)'],
 ['Target ACoS','The profit target, set below break-even by objective'],
 ['Break-even CPC @ blended CVR','break-even ACoS × price × CVR'],
 ['Max allowable CPC @ blended CVR','target ACoS × price × CVR'],
],[3400,6680]));
add(P('',{after:160}));
add(NOTE([{t:'Recompute the ceilings whenever price or the deal changes. ',b:true,c:INK},
 {t:'Price down pushes the ceiling down; deal-lifted CVR pushes it back up. The net effect must be computed, not assumed. Label both CPC figures “@ blended CVR — per-keyword ceilings are on the rows.”'}]));
add(P('',{after:200}));
add(H2('2.3 · The day'));
add(P('Each figure with its 7-day rolling value beside it: ad spend · ad sales · organic sales · total sales · TACoS (day + 7d) · sessions · unit session % · units ordered.',{after:160}));
add(CODE([
 'TACoS lives here, not in the segment tile row.',
 '  There is no all-source sales figure per segment, so the empty segment tile is',
 '  correct behaviour — remove it or relabel it "product-level only" so it stops',
 '  reading as broken.',
 '',
 'Numerator is SP + SB + SD spend.',
 '  SP alone against a total-sales denominator is not TACoS, and it drifts further',
 '  the more SB and SD you run.',
 '',
 'The 7-day rolling figure is the real number.',
 '  Organic sales swing far more day to day than spend does. The daily value is a',
 '  pulse, never a trigger.',
 '',
 'Mark the last 3 days as attribution still settling.'
]));
add(P('',{after:200}));
add(H2('2.4 · Rank, competitors, exceptions'));
add(TBL(['Block','Contents'],[
 ['Rank & position','BSR today + Δ + 30-day sparkline · category and subcategory BSR · rating + review count + Δ · our price rank in the set ("4 of 11")'],
 ['Competitor strip\n(top 10 by BSR)','Per competitor: ASIN + brand · price + Δ · deal? type + % · BSR + Δ · rating.\nHighlight only what changed since yesterday — nobody scans 40 static cells daily.\nOne derived line above it is what people actually read: "2 competitors dropped price · 1 started a deal · our price rank 4 of 11"'],
 ['Today’s exceptions','Count + severity chips for D1–D7, each clicking through to the affected campaign or keyword'],
],[2600,7480]));
add(P('',{after:160}));
add(NOTE([{t:'Why this block exists. ',b:true,c:INK},
 {t:'A window showing ad sales down 23.5% and orders down 21.0% on flat impressions cannot be diagnosed from ad data alone. It is bidding, price, stock, or a competitor — and in three of those four cases no bid change would have fixed it.'}], ACC));

// ---------- 3 ----------
add(H1('3 · Shared column spine'));
add(P('Carried by every tab, in this order. The effective state and the budget cap time are the two columns most often missing from tools like this, and both decide daily action.',{after:180}));
add(CODE([
 'Campaign',
 'Effective state       derived: Live / Paused-KW / Paused-Campaign / Archived',
 '                      A keyword is live only if BOTH keyword state AND campaign',
 '                      state are enabled. Raw values in the tooltip.',
 'Objective             Ranking | Discovery | Profitable Conversion | Defensive',
 'Portfolio · Advertised SKU',
 '',
 'Bid',
 'TOS % · PDP % · ROS % modifiers',
 'Effective bid per placement = base bid × (1 + modifier)   context, not judgement',
 '',
 'Budget · spend/budget % · in-budget % · cap time',
 '                      cap time    = "when did it die"',
 '                      in-budget % = "how much of the day did we serve"',
 '                      FLAG capped before 18:00 (20:00 if Ranking)',
 '',
 'Max allowable CPC (row ceiling)',
 'CPC vs ceiling — Total | TOS | PDP | ROS',
 '                      headroom form: "$1.95 of $1.50 (130%)"',
 '                      amber 90–100%, red above',
 '',
 'Placement block — Total | TOS | PDP | ROS',
 '  impressions · clicks · click-share % · CTR · CVR · CPC · orders · sales · ACoS'
]));
add(P('',{after:160}));
add(RUNS([{t:'Row flags ',b:true,c:INK},
 {t:'colour the row rather than adding columns: more than one enabled target · duplicate keyword · budget capped early · zero orders at ≥ 3× target CPA · ACoS above SKU break-even on a Profitable Conversion campaign.'}]));

fs.writeFileSync('/tmp/part1.json','ok');
module.exports = {body, add, P, RUNS, H1, H2, H3, CODE, NOTE, TBL, BUL, D, W, INK, INK2, ACC, RED, GRN, AMB};
