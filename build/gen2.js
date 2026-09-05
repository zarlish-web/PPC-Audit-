const fs=require('fs');
const g=require('./gen.js');
const {body,add,P,RUNS,H1,H2,CODE,NOTE,TBL,D,W,INK,INK2,ACC,RED,AMB}=g;
const {Document,Packer,Paragraph,TextRun,HeadingLevel,PageBreak,LevelFormat,AlignmentType,convertInchesToTwip}=D;

// ---------- 4 ----------
add(H1('4 · The six tabs'));
add(P('Ranking is the full tier; every other tab is a reduction of it. Auto and Manual are not judged on ACoS — they are Discovery by definition, and a broad campaign at 80% ACoS feeding three profitable exact campaigns is working, while one at 30% producing no harvestable terms is a dead end wearing a good number.',{after:180}));

add(H2('4.1 · Tab 1 — Ranking'));
add(RUNS([{t:'Objective: Ranking. ',b:true,c:INK},{t:'Exact keyword campaigns. Brand-defence exact campaigns sit here under a Defensive chip and are judged on defence, not rank gap.'}],{after:160}));
add(CODE([
 'TARGET COMPOSITION',
 '  Primary target  = the enabled target with the MOST CLICKS in the window.',
 '                    NOT highest SV. The row’s ACoS, CVR, CPC and placement split',
 '                    are dominated by whichever target got the traffic; labelling',
 '                    the row with a high-SV target that got 3 clicks makes every',
 '                    metric beside it describe a different keyword.',
 '  Primary target SV',
 '  # enabled targets           FLAG RED if > 1. Row expands to list every enabled',
 '                              target with its clicks + SV, so the rest can be paused.',
 '  # other campaigns targeting this keyword    FLAG if > 0',
 '  Duplicate group chip        see section 6',
 '',
 'RANKING COMMITMENT',
 '  Target rank · Current rank',
 '  CPR (Helium 10) · DSTR (DataRova)',
 '  Required sales · Actual sales',
 '  Required clicks · Actual clicks · Gap',
 '  Required impressions = required clicks ÷ target CTR',
 '  Actual impressions · Impression gap',
 '  30-day organic rank strip, newest first',
 '',
 'CTR / CVR — three values each',
 '  CTR   Market (SQP) | Target | Actual | gap',
 '  CVR   Market (SQP) | Target | Actual | gap'
]));
add(P('',{after:160}));
add(RUNS([{t:'The chain runs: '},{t:'required sales → ÷ CVR → required clicks → ÷ CTR → required impressions → vs what TOS share can deliver.',b:true,c:INK},
 {t:' A CVR assumption is already inside Target Clicks ("at our own measured conversion") — this surfaces it, because when the assumption is wrong the required-clicks figure is wrong by the same factor, silently.'}],{after:200}));

add(H2('4.2 · Tab 2 — Auto'));
add(RUNS([{t:'Objective: Discovery. ',b:true,c:INK},{t:'No keywords exist here. Row = campaign, expanding to its four auto target types — bids are set per type, so that is the real grain underneath.'}],{after:160}));
add(CODE([
 'Per target type (close match / loose match / substitutes / complements):',
 '  state · bid · impressions · clicks · CTR · CPC · orders · sales · ACoS',
 '',
 'DISCOVERY YIELD           judge auto on this, NOT on ACoS',
 '  new harvestable search terms in the window',
 '  cost per harvested term',
 '  % of spend on terms already harvested elsewhere      = leakage',
 '',
 'NEGATIVE COVERAGE',
 '  # negatives · are harvested terms negated back here?',
 '  An auto campaign with no negatives leaks into its own exact campaigns.',
 '',
 'DRILL: search terms generated'
]));
add(P('',{after:200}));

add(H2('4.3 · Tab 3 — Manual (broad / phrase)'));
add(RUNS([{t:'Objective: Discovery. ',b:true,c:INK},{t:'Row = campaign, expanding to all targeted keywords.'}],{after:160}));
add(CODE([
 'Per keyword: keyword · SV · state · bid · clicks · sales · ACoS',
 'Same DISCOVERY YIELD + NEGATIVE COVERAGE block as Auto',
 'DRILL: search terms generated',
 '',
 'Amazon SP has Exact, Phrase and Broad only — there is no broad match modifier;',
 'that is a Google concept. Broad shaped by negatives is the coverage column above.'
]));
add(P('',{after:200}));

add(H2('4.4 · Tab 4 — Product & Category targeting'));
add(RUNS([{t:'Objective: Profitable Conversion ',b:true,c:INK},{t:'(Defensive where the target is our own ASIN). Separate from Manual because a PAT row targets an ASIN and a Category row targets a node — neither has a keyword, SV, CPR or rank.'}],{after:160}));
add(CODE([
 'PAT       target ASIN + RESOLVED BRAND + product title    never a bare ASIN',
 'Category  category node + refinements (price band, rating, brand)',
 '',
 'CONQUEST CONTEXT   joined from the Product Profile competitor set',
 '  their price vs ours · their BSR · their rating · deal running?',
 '  This is what decides whether a target is worth defending or dropping.',
 '',
 'Expect PDP-dominant placement. FLAG a PAT campaign with high TOS share — it',
 'usually means the target is behaving like a keyword campaign.',
 '',
 'DRILL: which ASINs the ads actually served on'
]));
add(P('',{after:200}));

add(H2('4.5 · Tabs 5 & 6 — Sponsored Brands, Sponsored Display'));
add(TBL(['Tab','Columns unique to it'],[
 ['Sponsored Brands','Ad format (Product Collection / Store Spotlight / Video) · landing page (Store vs custom) · headline and creative.\nNEW-TO-BRAND: NTB orders, NTB sales, NTB % of orders. This is what SB exists for — judging it on ACoS alone misses the point entirely.\nTop-of-search impression share · viewable impressions.\nSB placements differ from SP — do not reuse the TOS/PDP/ROS block as-is.'],
 ['Sponsored Display','Targeting: contextual (product / category) vs audience (views remarketing, purchases remarketing, similar-to).\nCost type: CPC vs vCPM — not comparable, never sum them.\nViewable impressions · vCPM · view-through conversions · NTB.\nOn-Amazon vs off-Amazon lives here. The existing OFF-AMZ column reads 0 on every SP row because SP does not serve off-Amazon — it is structurally empty there, not sparse.'],
],[2400,7680]));

// ---------- 5 ----------
add(new Paragraph({children:[new PageBreak()]}));
add(H1('5 · The constraint column'));
add(P('The only column that outputs a decision rather than a number. Read in order, first match wins.',{after:180}));
add(TBL(['#','Condition','Verdict','Action'],[
 ['1','actual CVR < 60% of market CVR','Listing-constrained','Hold the push. Fix page, price or reviews. Do not fund.'],
 ['2','actual CTR < 60% of market CTR','Creative-constrained','Main image, title, price, badge. Bids will not fix CTR.'],
 ['3','impressions < required impressions','Impression-constrained','Raise bid OR TOS modifier. One, not both.'],
 ['4','budget capped before 20:00','Budget-constrained','Raise budget or reallocate.'],
 ['5','otherwise','On track','—'],
],[520,2900,2400,4260]));
add(P('',{after:160}));
add(NOTE([{t:'Sufficiency. ',b:true,c:INK},
 {t:'CVR needs ≥ 20 clicks, CTR needs ≥ 500 impressions. Below the floor: show the target, grey the actual, set the constraint to OBSERVING. A "listing-constrained" verdict off 4 clicks sends someone to rewrite a listing that was never the problem.'}]));
add(P('',{after:120}));
add(NOTE([{t:'The CVR floor is a funding gate. ',b:true,c:INK},
 {t:'Below rule 1 the campaign is not eligible for a bid or budget increase this cycle regardless of rank gap. Rank follows sales velocity — clicks that do not convert do not rank, they just spend the ranking budget.'}], RED));
add(P('',{after:160}));
add(RUNS([{t:'Sort the Ranking tab by this column, not by the rank gap. ',b:true,c:INK},
 {t:'A campaign 40 clicks short because it is impression-constrained gets a bid change today; one 40 clicks short because CVR collapsed gets escalated to whoever owns the listing.'}]));

// ---------- 6 ----------
add(H1('6 · Duplicate keyword detection'));
add(P('Amazon exact match already serves close variants — plural, misspelling, stemming, function words. Two targets that normalise to the same key are bidding in the same auction. You are outbidding yourself.',{after:180}));
add(CODE([
 'MATCH KEY = norm(keyword) + match_type',
 '',
 'norm():  lowercase → strip punctuation → drop stopwords',
 '         (a an the for of with and or in on to by) → singularise each token',
 '',
 'SINGULARISE CAREFULLY — not a trailing-s strip.',
 '  ss / us / is           → unchanged     (mattress, status, analysis)',
 '  ies → y                                (canopies → canopy)',
 '  es after s/x/z/ch/sh   → drop es       (boxes → box)',
 '  else trailing s        → drop          (sheets → sheet)',
 '  + irregulars list',
 '',
 'A naive strip gives "mattres" — and the team stops trusting the flag.'
]));
add(P('',{after:180}));
add(TBL(['Tier','Condition','Treatment','Action'],[
 ['1','Same key, word order preserved, same match type','Filled cell wash + solid rail','Self-competition. Keep one, pause the rest.'],
 ['2','Matches only after sorting tokens (word order differs)','No fill, dashed rail, same hue','Human confirms.'],
 ['—','Same key, different match type','No shade — link icon + count','Intended Hero/Halo layering, not a defect. Check an isolation negative exists in the broader campaign; flag if not.'],
],[620,3100,2500,3860]));
add(P('',{after:180}));
add(H2('6.1 · One keyword, one shade'));
add(CODE([
 'WHERE    keyword cell background + 3px left rail. NOT the full row — the row',
 '         already carries the rank heatmap, placement purples, crawl markers and',
 '         low-click greying, and a full-width wash fights all of them.',
 '',
 'SLOT     slot = hash(norm(keyword)) mod 8',
 '         Hash the NORMALISED key, so plural and singular land on the same shade.',
 '         Hash-based, not row-order-based, so the shade is stable across the',
 '         keyword view, the campaign view and future sessions.',
 '',
 'PALETTE  8 hues. No red (reads as error), no green (that is the rank heatmap).',
 '         H = [42 amber, 25 orange, 340 rose, 300 magenta,',
 '              265 violet, 225 indigo, 190 cyan, 165 teal]',
 '         light  wash hsl(H 70% 95%)   rail hsl(H 65% 62%)',
 '         dark   wash hsl(H 40% 14%)   rail hsl(H 55% 55%)',
 '         Violet and indigo sit near the placement-estimate purple — check together.',
 '',
 'CHIP     Group ID (D1, D2, D3…) in the keyword cell. The chip is the identifier,',
 '         the shade is a scanning aid — so the signal survives colourblind viewing,',
 '         greyscale export, and two unrelated groups sharing a slot.',
 '         Click the chip to filter the table to that group.',
 '',
 'KEEP     Within each Tier 1 group mark one row KEEP (most clicks; on a tie, the',
 '         one in the Ranking-objective campaign) and the rest PAUSE.',
 '',
 'Store the normalised key as a hidden sortable column so duplicates sort adjacent.'
]));

// ---------- 7 ----------
add(new Paragraph({children:[new PageBreak()]}));
add(H1('7 · Economic ceilings'));
add(RUNS([{t:'Max allowable CPC = target ACoS × price × CVR.',b:true,c:INK,f:'IBM Plex Mono',size:19},
 {t:' CVR is in the formula and CVR varies per keyword — a keyword converting at 25% justifies roughly double the CPC of one at 12% on the same product. The profile carries a reference ceiling at blended CVR; each row carries its own.'}],{after:180}));
add(CODE([
 'WHICH CVR   ≥ 20 clicks in window → the row’s own measured CVR',
 '            below that            → SQP market CVR, marked estimated',
 '            never a blended product CVR on a row',
 '',
 'MULTI-SKU   If a campaign has product ads for more than one SKU, use the LOWEST',
 '            ceiling across them and FLAG the row. One bid serves all of them, so',
 '            the thinnest-margin SKU sets the limit.'
]));
add(P('',{after:180}));
add(H2('7.1 · The decision this drives'));
add(TBL(['Reading','Action'],[
 ['Over ceiling on TOS only, under on PDP/ROS','Cut the TOS modifier. Not the base bid — that would discard the profitable PDP and ROS traffic.'],
 ['Over ceiling on every placement','Cut the base bid.'],
 ['Under ceiling everywhere but under-delivering','Headroom exists. Raise bid OR modifier — one, not both.'],
],[3800,6280]));
add(P('',{after:180}));
add(H2('7.2 · Objective gating'));
add(TBL(['Objective','Ceiling'],[
 ['Profitable Conversion · Defensive','Enforce.'],
 ['Discovery (auto, broad, phrase)','Advisory only — judge on discovery yield.'],
 ['Ranking','Do not enforce. Running above break-even is the point. The constraint is the ranking budget and the CVR gate, not ACoS.'],
],[3200,6880]));
add(P('',{after:160}));
add(NOTE([{t:'This is the one place where acting on the number in front of you is wrong. ',b:true,c:INK},
 {t:'Every other rule in this system is a threshold someone can act on. Enforce the ceiling on the Ranking tab and you will kill working pushes for being "over ceiling".'}], RED));

// ---------- 8 ----------
add(H1('8 · Data integrity rules'));
add(P('These apply to every tab and are not optional. The existing screen already gets the hardest one right — the settling band and dashed tails — and these extend the same honesty to the rest.',{after:180}));
add(TBL(['Rule','Detail'],[
 ['Attribution settling','Mark the last 3 days. No deltas inside the settling window — a conversion delta there compares a settled number against one still arriving, so it always reads as a decline and manufactures a fake drop every morning.'],
 ['Delta baselines','vs yesterday for competitor price, deal, BSR, Buy Box, rating · vs 7-day mean for spend, CPC, sessions · vs target for rank. A naive "vs yesterday" on everything makes noisy metrics scream until people stop looking.'],
 ['Sufficiency floors','CVR ≥ 20 clicks · CTR ≥ 500 impressions · bid decisions ≥ 10 clicks. Below the floor the answer is observing, which is a logged decision, not silence.'],
 ['Data vintage','The rank-crawl staleness banner is the right instinct — extend it. Required-clicks blends a rank up to 5 days old, weekly SQP, a monthly H10 CPR and a measured CVR. Stamp the composite age on the derived column, not only on the crawl.'],
 ['Estimate coverage','Per-cell coverage already exists in a tooltip. Surface a per-row indicator too — hover-only disclosure means people read estimates as measurements, and a 32%-covered row looks identical to a 95%-covered one.'],
],[2400,7680]));

// ---------- 9 ----------
add(H1('9 · Open items'));
add(P('Six things to settle before or during the build. Items 5 and 6 decide whether this is an oversight system or a very good reporting tool.',{after:180}));
add(TBL(['#','Item','Detail'],[
 ['1','Composite data vintage','On required-clicks and the CPR/DSTR columns — see section 8.'],
 ['2','Competitor data source','Daily price, BSR and deal state for 10 ASINs per product is a real pipeline (Keepa / DataDive / H10). The most-specced, least-sourced part of the profile.'],
 ['3','TACoS numerator','Confirm it carries SP + SB + SD spend, not SP alone.'],
 ['4','Off-AMZ column','Reads 0 on every SP row. Confirm it moves to the SD tab.'],
 ['5','Exception engine','Confirm D1–D7 fire against config/thresholds.yml and produce a queue, rather than counts being read off columns by eye.'],
 ['6','Action-log grading','Confirm something reads the log back and scores actions worked / flat / backfired two cycles later. Without it the log is a diary and the weekly W2 step has no input.'],
],[520,2300,7260]));
add(P('',{after:240}));
add(NOTE([{t:'Companion to the PPC Oversight System manual. ',b:true,c:INK},
 {t:'Every threshold referenced here by ID lives in config/thresholds.yml.'}], ACC));

const doc = new Document({
  creator:'Inspiratek / DECOLURE', title:'Campaign Daily Oversight — build spec',
  description:'Build specification for the daily tier of the PPC Oversight System',
  numbering:{config:[{reference:'bul', levels:[{level:0, format:LevelFormat.BULLET, text:'•',
    alignment:AlignmentType.LEFT, style:{paragraph:{indent:{left:360,hanging:200}}}}]}]},
  styles:{default:{document:{run:{font:'IBM Plex Sans', size:20, color:INK2}}}},
  sections:[{properties:{page:{size:{width:12240,height:15840}, margin:{top:1080,bottom:1080,left:1080,right:1080}}},
             children:body}]
});
Packer.toBuffer(doc).then(b=>{
  fs.writeFileSync('/home/user/PPC-Audit-/build/Campaign-Daily-Oversight-Spec.docx', b);
  console.log('written', b.length, 'bytes');
});
