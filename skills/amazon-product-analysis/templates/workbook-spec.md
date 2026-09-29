# Template — decision workbook spec

Tab-by-tab specification of the decision workbook (xlsx), generalised from the 34-tab B6 reference workbook and the B6 campaign-decisions workbook. Writing rules and the full quality gate: `references/12-writing-and-deliverables.md`.

## Contents
1. Conventions (all tabs)
2. Tab list at a glance
3. Tab specs — front matter (1–8)
4. Tab specs — keywords and campaigns (9–13)
5. Tab specs — competitors (14–24)
6. Tab specs — placement, stock, money, exceptions (25–29)
7. Tab specs — rows, operations, validation (30–33)
8. Checks tab (34)
9. Optional tabs

---

## 1. Conventions (all tabs)
1. Tab names ≤31 characters; order as in §2; an empty tab states why in its first row ("No product targets in scope"). [WB]
2. Row 1 title, row 2 subtitle (sources, windows, date), then sections; tables have one header row, frozen panes on the identity columns, auto-filter on long tables. [B6]
3. Formats: $ 0.00 for prices/bids, $ 0 for budgets, 0.0% for rates and shares, integers for ranks; missing = blank or "—", never 0. [all]
4. Decision cells colour-filled by label (one colour per label, legend on Start here); stock zones Green / Yellow / Red. [B6]
5. "New" columns are blank when the value does not change. Top-of-search price always = base × (1 + boost). [WB]
6. Every decision row carries the trail: **Input → Metric → Logic (rule) → Decision → Action → Expected outcome → Validation**. Rule IDs appear only in Rule / Logic columns. [B6, register #28]
7. Every figure is produced by the build from source data, never typed; the column set is a contract — diff against the previous version and never drop a column silently. [WB, DR]
8. Reasoning cells follow the chain in reference 12 §1.2 and must not repeat verbatim across rows. [DR, PB]

## 2. Tab list at a glance
| # | Tab | Required? | Answers |
|---|---|---|---|
| 1 | Start here | Always | What this is, sources, how to read, tab index |
| 2 | Overview | Always | Spend vs limit, decisions at a glance, what needs the owner |
| 3 | Process map | Review of an engine/plan run | Pipeline stages: what it does, where it failed, corrected logic |
| 4 | Failure register | Review of an engine/plan run | Each wrong decision, the data, the correction, the test |
| 5 | Before → After | Review or refinement | Same measures on prior version(s) vs corrected |
| 6 | Metrics dictionary | Always | Every metric used |
| 7 | Decision rules | Always | Every rule applied (IF → THEN) |
| 8 | Decision trails | Always | Worked end-to-end examples |
| 9 | Keyword decisions | Always | Every search term with spend |
| 10 | Harvest & negate | Always | Keyword actions grouped |
| 11 | Campaign logic | Always | How each type × objective is treated |
| 12 | Campaign decisions | Always | Every campaign, one decision, full trail |
| 13 | Push plan | When ranking is authorised | Funded / waiting / at-target terms |
| 14 | Competitor targeting | When product targets exist | Product targets and their performance |
| 15 | Competitor landscape | Always (may be a separate file) | Market, share, trends, segments, price ladder, patterns |
| 16 | Competitor profiles | Always (may be separate) | Each measured rival vs us |
| 17 | Hero ASINs & trends | When trend data exists | Rival heroes, movers, where rising rivals gain |
| 18 | Competitive keywords | Always (may be separate) | Every addressable market keyword |
| 19 | Push terms vs field | When ranking is authorised | Who stands between us and each target |
| 20 | Gaps & how to fill | Always | Gaps with size, fill inside guardrails, validation |
| 21 | Competitor ASIN targets | Always | OFFENSIVE / TEST / AVOID per rival ASIN |
| 22 | Competitor → decisions | Always | Influence rules; what each never changes |
| 23 | Tests | When a test is proposed | Test design, rules, read dates |
| 24 | Landscape check | Always | Each keyword/campaign decision vs the field |
| 25 | Placement | Always | Campaign × placement read and mix fix |
| 26 | Variation & stock | Always | Preferred / backup / clearance per size; SKU margins |
| 27 | Inventory × PPC | Always | How stock gates each decision |
| 28 | Financial guardrails | Always | Break-even, ceilings, limits, per SKU |
| 29 | Exceptions & BLOCK | Always | No-automatic-change conditions, current cases |
| 30 | Source rows | Review of a run | Every proposed row with a verdict |
| 31 | New campaigns | When builds/restarts exist | Builds and restarts with decision and date |
| 32 | By hand | When needed | Changes that don't upload (switches, tags, budgets, SB/SD) |
| 33 | Validation plan | Always | Checkpoints, pass, fallback |
| 34 | Checks | Always | Computed integrity checks |

---

## 3. Front matter

### 1. Start here
- **Purpose**: orient a cold reader in two minutes.
- **Content**: what the workbook is (one paragraph); versions compared (if a review); how the trail works and where rule IDs point; status legend (e.g. Fixed / Partly fixed / Not fixed / New finding); sources with windows and dates.
- **Table**: Tab · What it answers.

### 2. Overview
- **Spend vs limit** table: Line · $ a day · Basis — current spend (event and settled), outside-push today and after cuts, push today and expected day one, expected total, push budgets (full plan and scale factor), the limit (with exception terms).
- Binding-constraint sentence (e.g. price-capped: N of M funded terms at or within 5% of ceiling).
- **Needs your decision**: # · Decision · Detail (options, trade-off, deadline); already-decided items marked with date.
- **Decisions at a glance**: counts by campaign group, campaign decision, keyword decision, failure status.

### 3. Process map (reviews only)
- Columns: Stage · What it does · Inputs · Where it failed (failure IDs) · Corrected logic · Rules / guardrails · Validation.
- Stages (generic): scope & calendar → data read → economics → classification → targets & requirements → qualification → pricing → structure → variation → budgets & limit → forecast → review & loader → validation & tuning.

### 4. Failure register (reviews only)
- Columns: ID · Area · Scenario · What was decided · Example and data · Why it was wrong · Correct decision · Logic / guardrail changed · Version A result · Version B result · Status · How recurrence is prevented · Validation test · Rules.

### 5. Before → After
- Columns: Measure · Version A · Version B · Corrected · Source.
- Rows (generic): events recorded; margin / break-even ACoS; decisions / campaigns changed; campaigns in list; changes outside own list; price/base changes; jumps above cap; prices above ceiling; variation switches (and size changes); budgets; withheld rows exported; wrong retags; restarts; new campaigns; brand negatives; head-term price; cap-bound campaigns; forecast spend, ACoS, TOS clicks; review verdict; funded push terms.

### 6. Metrics dictionary
- Columns: Metric · Family · What it means · How it is calculated · Source · Window · Validation · Thresholds used · How it influences the decision · Pitfalls.
- Minimum rows: impressions, clicks, CTR, orders/units, CVR, TOS CVR, CPC, TOS CPC, spend (tile vs rows), ad sales, ACoS, TACoS, ROAS, AOV, margin per unit, break-even ACoS, break-even CPC, ceiling, push price, CPA, margin after ads, TOS price, base, boost, placement click share, TOS impression share, sponsored rank, organic rank, target rank/date, rank drop, search volume, relevancy, term class, indexing, market CTR/CVR (SQP), plan clicks, available stock, days of cover, days to arrival, velocity, event flag, event-day spend, budget.

### 7. Decision rules
- Columns: Rule ID · Family · Applies to · IF · THEN · Thresholds · Why · Guardrail / limit · Exception → review.
- Families: push, break-even, placement, non-ranking, variation, objective, structure, keyword, competitor target, inventory, financial, competitor influence.

### 8. Decision trails
- One section per example; table Step · Detail with rows Input, Metric, Logic, Decision, Action, Expected outcome, Validation, and (reviews) "Previously decided".
- Minimum set: head push term; over-ceiling term; variation switch; rank collapse; cap-bound campaign; brand campaign; discovery campaign; harvest; reduce; competitor ASIN. Template: `templates/decision-trail-examples.md`.

## 4. Keywords and campaigns

### 9. Keyword decisions
- **Scope**: every search term with spend in 30 or 90 days (plus market terms seeded from gaps).
- Columns: Search term · Decision · Rule · Why · Action · Class · Relevancy · Search volume/month · Weekly SV (competitor tool) · Organic rank (30 d median) · Sponsored rank · Target rank · Indexing · Exact owner(s) · Impr 30 d · Clicks 30 d · CTR 30 d · Orders 30 d · CVR 30 d · CPC 30 d · Spend 30 d · Sales 30 d · ACoS 30 d · Clicks 90 d · Orders 90 d · CVR 90 d · CPC 90 d · Spend 90 d · Sales 90 d · ACoS 90 d · TOS share · TOS CVR · TOS CPC · PDP share · PDP CVR · ROS share.
- Decision labels: PUSH / WAIT / HOLD RANK / BREAK-EVEN / REDUCE / BLOCK / HARVEST / DEDUPLICATE / CHECK OWNER / DEFEND / MONITOR / KEEP.
- Note in subtitle: placement shares at keyword grain are estimates (placement is reported per campaign).

### 10. Harvest & negate
- Sections: Harvest · Block · Reduce · Deduplicate · Check owner — each titled with count and 90-day spend.
- Columns: Search term · Class · Relevancy · Clicks 90 d · Orders 90 d · ACoS 90 d · Spend 90 d · Owner(s) · Action (with timing and negation mode).
- Section for negatives proposed by the prior run: Seq · Campaign · Negatives now · After · Terms added · Verdict (Load / Hold, why).

### 11. Campaign logic
- Columns: Type · Objective · Purpose · Deciding metrics · Allowed actions · Not allowed · Advertised variation · Placement rule · Rules · Campaigns (count).
- Rows: Exact × Ranking / Conversions / Defensive; Broad-Phrase × Discovery; brand Broad × Defensive; Auto × Discovery; product targeting × Defensive (own) / Conquest (competitor) / cross-sell (own other product); SB/SBV; SD; Liquidation/LTSF.
- Paragraphs: how type is recognised (targeting, not name); how objective is set; what "focus" may and may not do.

### 12. Campaign decisions
- **Scope**: every campaign advertising the product (list + any spending on it but missing, marked).
- Identity: Group · Campaign · Campaign ID · In list · Ad type · Match · Size · Main term(s) · Status · Focus · Objective now → correct · Variation now → correct.
- Trail: INPUT · METRIC · LOGIC (rule) · DECISION · ACTION · EXPECTED OUTCOME · VALIDATION · Why (full reasoning) · Prior-run rows → verdict · When · How it loads.
- Numbers: Clicks 30 d · Orders 30 d · Spend 30 d · ACoS 30 d · ACoS 90 d · TOS share · PDP share · TOS clicks 90 d · TOS CVR 90 d · Margin/unit · CVR used (basis) · Break-even $ · Ceiling $ · Rank now → target · Base now/new · Boost now/new · TOS price now/new · Budget now/new · State new · Variation new · Objective new · Event-day spend.
- Sort: group order (push funded, waiting, at target, ranking break-even, conversions, discovery, defensive, liquidation, SB/SD), then spend desc.

### 13. Push plan
- Columns: Status (PUSH / WAIT / HOLD RANK) · Term · Campaign · Variation now → correct · Rank now → target · TOS CVR (90 d, basis) · Break-even $ · Push price $ · Ceiling $ · Our TOS CPC (90 d) $ · Price now $ · Price to write $ · Base now → new · Boost now → new · Plan TOS clicks/day · Today TOS clicks/day · Plan orders/day · Budget $ · First milestone · Re-read date · Why.
- Footer: funded total; formula notes; scaling to the limit.

## 5. Competitors
All competitor tabs state coverage ("measured N of M mapped") and export dates in the subtitle; unmeasured ≠ zero; ASINs resolved to brands. [B6 R-CI12, LP]

### 14. Competitor targeting
- A. Product targets with own reads: Campaign · ASIN · Brand · Product · Price · Rating · Reviews · Relation (own product / own other product / competitor same material / competitor other material / unmapped) · Campaigns targeting it · Clicks · Orders · CVR · Spend · ACoS · Decision (DEFEND / KEEP / SCALE / REDUCE / BLOCK / MONITOR) · Why.
- B. Product-targeting campaigns (30/90 d): Campaign · Tag · Advertises · Targets · funnel 30/90 d · Decision · Why.
- C. Proposed conquest builds: ASIN · Brand · Product · Price · Rating · Reviews · Relation · Assessment.

### 15. Competitor landscape
- Numbered patterns that should steer PPC (8–12, each with numbers).
- Sources and limits: Source · What it gives · Date · Limits (include "not available anywhere": review themes, competitor CPC/CVR/structure).
- Market size, reach, share: Measure · Keywords · 7-day traffic · Our traffic · Our share · Note (whole market, addressable, disqualified, unknown, contested, theirs-only, ours-only, per segment).
- Traffic trend: Seller · Tier · Earlier export · Traffic then · Latest · Traffic now · Change.
- Placement reach: Seller · Tier · Keywords · Organic · SP · SB · SB video · Amazon's Choice · Product-page recs · Read.
- Segments: Segment · Keywords · Market traffic · Paid share · Our traffic · Our share · Absent keywords · Wins vs beatable.
- Niche benchmarks: Niche · Researched · Keywords · Monthly SV · Median price · Median reviews · Median units.
- Price ladder: Brand · ASIN · Listing · Price · Pieces · $ per piece · Est. units/30 d · Est. revenue · BSR · Rating · Reviews · Variations.

### 16. Competitor profiles
- One row per measured rival + us: heroes · variations · price · units · revenue · BSR · reviews · review velocity · keywords · organic vs paid split · placement behaviour · strengths · weaknesses · what it means for us.
- Section: each rival's top addressable keywords — Rival · Keyword · Kind · Weekly SV · Their traffic · Their paid · Their organic rank · Their SP rank · Placements · Our traffic · Our organic.

### 17. Hero ASINs & trends
- Heroes: Seller · Tier · ASIN · Share of seller traffic · Keywords led · Price · Rating · Reviews · Est. units · BSR · placement-score change.
- Movers (price, BSR, reviews, discount) over the window.
- Where rising rivals gain on core terms and we are behind.

### 18. Competitive keywords
- Every addressable market keyword: Keyword · Kind · Size · Segment · Relevancy · Addressable · Weekly SV · Market traffic · Paid share · Rivals present · Rivals advertising · Leader · Our organic · Our SP · Our traffic · Opportunity · Our decision · Landscape verdict.

### 19. Push terms vs field
- Columns: Term · Decision · Group · Our rank now · Competitor-tool organic · SP · Target · Weekly SV · Market traffic · Organic field (top 6 tracked, with tier) · Best rival SP · Rivals at SP #1–5 · Rivals with brand banner · Our paid share · Market paid share · First milestone (next beatable rival ahead) · Landscape verdict (stretch / winnable / reachable / we lead) · Why · Notes.
- Paragraphs: what this changes in how the push is judged — never how it is priced.

### 20. Gaps & how to fill
- Columns: # · Gap · Evidence · Why it matters · How to fill (inside break-even, ceiling, step, limit) · Rule · Validation.
- Plus: size battlegrounds (Size · Core keywords · Market traffic · Our traffic · Share · Keywords we lead · Avg organic · Most frequent leader); seed list (Term · Kind · Size · Weekly SV · Market traffic · Paid share · Leader · Our organic · Opportunity · Owner · How · Advertised variation); campaign structure (Area · Today · What the data says · Change).

### 21. Competitor ASIN targets
- Columns: Seller · Tier · ASIN · Share of seller traffic · Listing · Size · Their price · Our same-size price · Rating · Reviews · Est. units/30 d · BSR · In proposed build · Our campaigns targeting it · Today (performance) · Class (OFFENSIVE / TEST / AVOID / LOW TRAFFIC) · Why · Action.
- Footer: class uses price, pieces, rating, reviews only; money decisions on already-targeted ASINs still follow their own clicks and ACoS (a profitable AVOID is held at break-even, never scaled).

### 22. Competitor → decisions
- Columns: Rule · Decision area · Competitor signal · IF → THEN · What it never changes · Today's example · Status (standing / proposed / approved).
- Section: where each signal enters the pipeline (stage · input · rules).

### 23. Tests
- The campaigns: Id · Format · Keyword(s) · Advertised variation · Landing · Replaces which proposed build · Market traffic · Weekly SV · Rivals with headline / video · Start bid (break-even) · Ceiling · Budget/day · Why.
- Not built: builds · what · why not.
- Rules: When · Rule (start, daily step, 15-click re-baseline, 0-order stop, >2× break-even stop, read date, halo check, report).
- Build notes (by hand, budget line, creative, negatives).

### 24. Landscape check
- Crosstab: decision × landscape verdict (agrees / stretch / reachable / challenge / blind).
- Keyword list: Keyword · Decision · Clicks/Orders/ACoS 90 d · Market traffic · Rivals present · Rivals advertising · Our organic · Verdict · Why.
- Campaign-level checks: Decision · Landscape check · Verdict.

## 6. Placement, stock, money, exceptions

### 25. Placement
- Rules paragraph (70–90% top / ≤20% product pages for ranking; mix fix; discovery/conversion judged on ACoS; product-level split).
- Columns (campaigns with ≥15 clicks): Campaign · Group · Clicks 30 d · Top share · Rest share · PDP share · Top CVR · Rest CVR · PDP CVR · Top CPC · Rest CPC · PDP CPC · Placement read (leak / not competing / healthy / judged on ACoS) · Base now · Base new · Boost now · Boost new · TOS price now · TOS price new · Decision.

### 26. Variation & stock
- Per size: Size · Preferred (ranking) · Available · Units/day 30 d · Units/day 7 d · Cover (30 d pace) · Next dated arrival · Days to arrival · Inbound shipped · Current serving variation · Stock gate (ROOM / TIGHT / switch / none) · Verdict · Backup (same size) · Clearance (discovery) · Don't advertise (near-out).
- Per SKU: SKU · Units 30 d · Margin before ads/unit · Price · Break-even ACoS · Stock · Units/day · Days of stock · Role.

### 27. Inventory × PPC
- Steps table: Step · Check · Rule · Rule ID — count sellable units; pace (30 d, 7 d warning, never push pace); cover; minimum (<7 days); against the arrival (ROOM / TIGHT ≤7-day gap / switch); out of stock; discovery colour; events.
- Where each size stands: Size · Available · Cover · Next arrival · Stock gate · Push allowed?

### 28. Financial guardrails
- Columns: Guardrail · Formula · Product value · Crossed when · What happens · Rule.
- Rows: margin per unit; break-even ACoS; 2× break-even ACoS; break-even CPC; push ceiling; cost per order (push); target ACoS (non-push); spend limit; margin after ads; TACoS (reported); step limits.
- Per SKU grid: SKU · Margin · Price · Break-even ACoS · Break-even price at 10/15/20/25% CVR · Ceiling at 20% CVR.

### 29. Exceptions & BLOCK
- Columns: Code · Name · Condition · Treatment · Scope · Current cases (computed).
- Standard set: event days; attribution window; thin data; rank drop; at ceiling; paused; missing state; variation switch; size change; brand negatives; duplicate build; formats outside automation; shared campaigns; stock; listing flag; cap; big step; objective; spend limit; unmapped competitor.

## 7. Rows, operations, validation

### 30. Source rows (reviews)
- Every row the prior run proposed: Seq · Kind · Campaign · Now · Proposed · Prior review verdict · Our verdict (load / replace / hold / don't load) · Why.

### 31. New campaigns
- Builds: Seq · Type · Proposed campaign · Targets · Budget · Prior review · Decision (build on date / don't build / restart instead / test).
- Restarts: Campaign · Term · Variation · Price · When.

### 32. By hand
- Sections: variation switches (Campaign · Group · Now · Should be · When); objective tags (Campaign · Term · Now · Correct); push budgets (Campaign · Budget now · Budget new); SB/SD builds.

### 33. Validation plan
- Columns: When · What · Metric · Pass · Fallback · Rule.
- Minimum rows: daily push step read; day 3 at ceiling; daily spend vs limit; rank-drop watch; hero stock; day 1 after event; 7 days after mix fix; first settled read of cuts (break-even and non-ranking); weekly push tune; 50-click conversion stop; 14 days after harvest; 14 days after block; product-goal date; next events; test daily and read date; brand-defence re-read.

## 8. Checks (tab 34)
- Columns: Check · Result. Result is computed by the build from the workbook's own rows (count and PASS / FAIL (n)), never typed.
- Minimum computed checks (B6 set):
  1. No push price above 2 × break-even.
  2. No boost above 900%.
  3. No base cut deeper than 50% in one step.
  4. No push raise above +30% in one step (below ceiling).
  5. No price raise on non-push ranking campaigns during an event.
  6. Push budgets + expected other spend ≤ the spend limit (show the total).
  7. Every in-focus campaign has a decision.
  8. Every prior-run row has a verdict (show count).
  9. Every search term has a decision (show count).
  10. Brand and push terms never blocked.
  11. No bidding-strategy change written.
  12. No variation switch changes the size (list any allowed wrong-size corrections).
  13. Every failure has a status and a validation test (reviews).
  14. Every push / waiting / at-target term has a landscape verdict.
  15. All addressable market keywords pulled; all measured competitors profiled (show counts).
  16. No competitor rule sets or raises a price.
  17. Row census: campaigns in scope = decision rows; how many added from outside the list.
- Then run the full quality gate (reference 12 §7) and record its result on this tab: RAN / NOT RUN per group, failures by check.

## 9. Optional tabs
| Tab | When | Columns |
|---|---|---|
| Data conditions | Any unresolved data issue | Condition · Evidence · Why it matters · Actions gated · Owner · Due · Status (withdrawn findings kept with overturning evidence) [DR, PB] |
| Impact ledger | Any refinement cycle | Key · Campaign · Target · Lever · Before → after · Logged · Expected metric/direction/tolerance/horizon · Execution (executed / not / partial) · Grade (worked / flat / backfired / too soon / event window / confounded / provisional) · Consecutive no-impact · Escalate [SR] |
| Timeline | Events in the window | When · What [B6] |
| Negatives | Many negatives | Seq · Campaign · Negatives now · After · Terms · Verdict · Why [B6] |
| Deployment waves | Multi-step rollouts | Wave · Date · Rows · Daily $ · Cumulative $ [WB] |
| Brand management log | Listing/offer findings | Finding · Evidence · Recommendation · Owner · Expected effect [PB, LTSF] |
