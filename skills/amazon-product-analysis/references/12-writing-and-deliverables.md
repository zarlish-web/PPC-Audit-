# 12 — Writing standard, deliverables and the quality gate

Read at Phase 10, and again before writing any reasoning cell. Everything here applies to every product; B6 numbers appear only as labelled examples.

## Contents
1. Writing standard (voice, reasoning chain, mandatory elements, banned content)
2. Action-string grammar
3. The decision trail (format + 3 filled examples)
4. Finding / Why it matters / Action / Expected impact (thesis and execution sequence)
5. Forecasting rules
6. Deliverables (decision document, decision workbook, competitor workbook, change review sheet, upload file, Google delivery)
7. Quality gate — consolidated checklist (run last, all must pass)
8. Open questions for the owner

---

## 1. Writing standard

### 1.1 Voice
1. Plain language for an owner who is not a PPC analyst. Short sentences. Name the thing ("product pages", "top of search"), not the jargon ("PDP", "TOS") in narrative text; abbreviations are fine in workbook column headers once defined in the Metrics dictionary. [B6, AP]
2. Write in the analysis's own voice: "this is the account's convention", never "this skill decided". [PB 23A]
3. Every verdict is falsifiable: it says what should happen, by when, and what would prove it wrong. [SKILL]
4. Say "this is a [waste / placement / visibility] problem, not a [demand / supply] problem" when the distinction drives the action. [AP]
5. End each diagnostic table with one **Conclusion** line that names the action it leads to ("What this table decides"). [AP, PB]
6. Measured vs estimated is stated in the text ("measured, 90 days" / "estimate, labelled proxy"). Conflicting sources → show both and name the one that governs. [LP, PB]
7. Missing value → "—" or "Not available", never 0; unmeasured ≠ zero. [all]

### 1.2 Reasoning chain — every reasoning cell, in this order [DR, PB]
1. **What is happening** — the row's current state in numbers (window stated).
2. **History** — what was done before, when, and whether it worked (grade from the impact ledger).
3. **Market** — SQP / competitor context for this term or target.
4. **Objective** — which objective the campaign has and which metric judges it.
5. **Actual vs estimate** — delivery vs plan (clicks, orders, rank); estimates size direction, rank movement governs.
6. **Action** — the exact change (action-string grammar, §2).
7. **Why this lever, not the adjacent one** — name the alternative considered (placement vs budget vs price vs listing vs colour) and why it loses.
8. **Why it is economically safe** — ceiling arithmetic inline; loss bounded; stock covers it.
9. **What reverses it, and when it is re-read** — a condition and a date.

Cold-reviewer test: a first-time reader must be able to answer, without a follow-up question, *what changed, why these numbers justify it, what would make it wrong*. Real numbers that do not connect to the verdict fail the test. [PB 17A]

### 1.3 Mandatory elements
| # | Element | Example (B6) | Source |
|---|---|---|---|
| 1 | **Named numbers doing work** — each number is inside the argument, not beside it; state the comparison and the ratio | "converts 19.1% at the top against a market of ~2% (≈9×)" | DR anti-pattern 1 |
| 2 | **Dated sources and windows** on every figure | "Sellerboard, 27 Aug–25 Sep"; "30 days to 29 Sep" | PB, B6 |
| 3 | **Rank arc** prior → recent → current, with the source of each and which one governs; overall, 14-day and 7-day stated separately; clean arc governs over deal arc | "27 (end Aug) → 33 (deal start) → 55 (29 Sep), daily crawl" | DR, PB |
| 4 | **Placement split before any bid** — top / rest / product pages share of clicks (and CVR where it decides) | "39% top / 56% product pages on 776 clicks" | DR, WB |
| 5 | **Ceiling arithmetic inline** — margin × CVR = break-even; × 2 = ceiling; price vs both | "$15.97 × 19.1% = $3.05; ceiling $6.10; today $6.10" | DR, B6 |
| 6 | **Why this lever, not the adjacent one** | "base cut, not a boost raise: the boost only applies at the top and the campaign isn't winning there" | DR, B6 |
| 7 | **Reversal and re-read** — condition + date | "restore one step if rank falls >10 places; read 8–14 Oct" | DR, PB |
| 8 | Previously flagged conditions on the row named (listing flag, rank drop, deal, stock) | "listing flag stands (CVR 0.68× market)" | DR |
| 9 | On cuts: auction density (how many rivals advertise the term) and opportunity cost | "11 rivals advertise it; 61 orders in 90 days → reduce, not block" | PB, B6 R-CI9 |
| 10 | On ranking premiums: inventory zone and stock cover beside the push | "King White 1,388 Available, 133 days" | PB |
| 11 | Formula-only corrections (thin data, over ceiling) name two reversal tests: converts once clicked AND gets clicks at all | — | PB |
| 12 | Confidence where thin; soft coefficients named with when/how they will be measured | "credit +5–15% steps with 0.85× net of drift (from own step history)" | PB 22 |
| 13 | Grade of the prior action on the same row (worked / flat / backfired / too soon / not executed) | — | SR, PB |

### 1.4 Banned in delivered text
| Banned | Why / test | Source |
|---|---|---|
| Internal codes: "§", rule IDs (R-P3, E15, S-C1), "State E", "PROVEN tier", "the sufficiency stop", gate numbers — even in parentheses | Owners can't decode them. **Rule IDs are allowed only in the workbook's Rule / Logic columns** | PB 23, register #28 |
| Tool, script and run names in narrative (script/function names, run IDs, "the engine's stage 7") | Data sources are named in source lines and captions ("Sellerboard", "search query data", "rank crawl"); internal tooling is not | PB 23 |
| "this skill", "not derived by this skill" | Self-reference | PB 23A |
| Version narration ("restored after the rewrite", "v5") | The document's own version number in the title block is fine | PB 23B |
| Personal names | Use roles: "the product owner", "the PPC manager", "the reviewer" | PB |
| Tracked changes, redlines, "we changed our mind" narrative | Deliver the clean current position; withdrawn findings go to the register with the overturning evidence | PB, DR 11 |
| Verdict without arithmetic; blended figure where a placement figure exists; estimate used as a gate | DR prohibited list | DR |
| Generic advice ("consider optimising bids") | Fails the bar in SKILL.md | SKILL |
| Templated reasoning: identical text (or identical except the row's own name) across rows of one entity type | String-compare every reasoning cell | PB 16, SR |

### 1.5 Number conventions
- Prices and bids $0.00; budgets $0; ACoS/CVR/CTR/share 0.0%; ranks integers; ratios "0.68×".
- Top-of-search price is always written as **TOS price = base × (1 + boost)**, with base and boost shown when either changes.
- Every % change shows its base: "$5.93 → $7.71 (+30%)".
- A value that does not change is left blank in "new" columns (same-value → blank). [WB]

---

## 2. Action-string grammar

One string per entity (keyword, target, placement, campaign, ad). Decision label first, then every changed value as before → after, then timing/how.

```
<DECISION> — <lever> <before> → <after> (<±%>)[; <lever> <before> → <after>] — <when / how it loads>
```

| Case | String (B6 example values) | Rule |
|---|---|---|
| Price with pair write | `PUSH — TOS price $5.93 → $7.71 (+30%): base $1.37 → $1.03, boost 333% → 649% (one write); budget → $156 — load now` | Base and boost of one campaign are one backward-solve [PB, B6] |
| Cut to ceiling | `CUT — TOS price $8.43 → $6.24 (−26%, to ceiling): base $1.87 → $0.94, boost 351% → 564%` | Over-ceiling never deferred [B6] |
| Staged move | `BREAK-EVEN — TOS price $6.06 → $3.03 (−50%) now → $2.77 on <date>` | Gap > cap = dated steps [PB, WB] |
| Hold | `HOLD RANK — TOS price $5.18 held; base $2.50 → $1.88, boost 107% → 176%` | Reason must be on the mechanical list or asked [PB 24] |
| State change | `RESTART — enable campaign; bid blank (unchanged) — 1 Oct` | State changes leave the bid blank on purpose [DR] |
| Duplicate | `DEDUPLICATE — pause; owner is <campaign>` | Nothing else changes on the loser [PB] |
| Negative | `BLOCK — negative exact "silk sheets" in <discovery campaigns> — reactive` | Mode named: pre-load / reactive / steering [PB] |
| Harvest | `HARVEST — build Exact "<term>" at $<BE> on <SKU>; negative exact in <source>, same upload — <date>` | [PB, B6] |
| Ad switch | `SWITCH AD — Queen Olive → Queen White (same size), by hand, before the price loads` | Size never changes [B6] |
| Owner call | `REVIEW — owner: raise ceiling $6.10 → $7.63 until 14 Oct, or hold $6.10` | Time-boxed [B6] |
| Placement only | `MIX FIX — base $1.60 → $1.20, boost 281% → 408%; TOS price $6.10 held` | Boost raise without the base pair is refused when product pages >20% [B6] |

Rules: never write instructions into the State column; retired verbs "RE-ROUTE" and "HOLD ENABLED" are not used; one lever per entity per cycle except the base+boost backward-solve; an action string must equal the values in the row's New Bid / New % / New Budget cells. [WB, DR]

---

## 3. The decision trail

Every campaign, keyword and competitor-target row carries this trail (workbook columns; narrative examples in the document use the same order without rule IDs).

| Step | Contents | Test |
|---|---|---|
| **Input** | Raw facts with windows: clicks, orders, spend, ACoS (30/90 d), placement split, price (base × (1+boost)), advertised SKU, rank now → target, stock | Every figure has a window and a source |
| **Metric** | The derived numbers that decide: break-even = margin × CVR (basis stated: own ≥50 / blend 15–50 / size <15), ceiling, push price, ACoS vs BE, PDP share, SQP ratio | Recomputes from Input |
| **Logic (rule)** | The gate that fired (master decision order) and the rule(s) applied; **rule IDs allowed here only** | First gate that fires is named |
| **Decision** | One label: PUSH / WAIT / HOLD RANK / BREAK-EVEN / CUT / MIX FIX / DEFEND / HARVEST / REDUCE / BLOCK / DEDUPLICATE / CHECK OWNER / MONITOR / RESTART / KEEP / REVIEW / SCALE (targets: OFFENSIVE / TEST / AVOID) | Exactly one |
| **Action** | Action string (§2) | Equals the New cells |
| **Expected outcome** | Metric, direction, magnitude, horizon (a range, §5) | Falsifiable |
| **Validation** | Date(s), pass condition, fallback if it fails | Has a date and a fallback |

Full worked set (10 scenarios): `templates/decision-trail-examples.md`.

### Example 1 (B6) — head term already at its ceiling
| Step | Detail |
|---|---|
| Input | "bamboo sheets" exact, 30 d: 776 clicks, 119 orders, $3,037, ACoS 31.7%; 39% top / 56% product pages; top-of-search impression share 2.4%; TOS price $6.10 = $1.60 × (1 + 281%); advertises King White (1,388 Available, 133 days); rank 26 → target 9; plan 69 top-of-search clicks/day, getting 10; our TOS cost per click $5.66. |
| Metric | Break-even $3.05 = King White $15.97 × 19.1% (own TOS CVR, 90 d, ≥50 clicks); ceiling $6.10; premium (26 ÷ 9 − 1) × 50% = 94% → push price $5.93; market CVR ~2%. |
| Logic (rule) | Qualifies on all push gates (demand, CVR above market, reach, stock, live, ceiling ≥ cost) [R-P1]. Price $6.10 sits between push price and ceiling → hold [R-P4]. Product pages 56% on ≥15 clicks and they sell → base −25%, boost re-solved [R-M1]. At ceiling for weeks without holding the top → owner [R-P6]. |
| Decision | PUSH (at ceiling) + REVIEW (owner ceiling decision). |
| Action | `MIX FIX — base $1.60 → $1.20, boost 281% → 408%; TOS price $6.10 held; budget → $201` + `REVIEW — owner: ceiling 2.5× = $7.63 until 14 Oct, or hold $6.10`. |
| Expected outcome | Top-of-search share of clicks rises from 39% toward 70%; impression share up from 2.4%; organic rank moves within ~5–19 days of the clicks landing. |
| Validation | Daily: impression share and sponsored rank. Day 7: placement split (product pages >20% → cut base again). 8–14 Oct (settled): rank vs 26. Stop if TOS CVR falls below market on 50+ clicks. |

### Example 2 (B6) — non-ranking campaign over break-even on both windows
| Step | Detail |
|---|---|
| Input | "red bamboo sheets" exact (colour term), advertises Queen Burgundy; 30 d: 45 clicks, 5 orders, $120.29, ACoS 30.5%; 90 d ACoS 33.2%; base $1.12; tagged Ranking. |
| Metric | Break-even ACoS 23.8%; over on 30 d AND 90 d; cut = 1 − 23.8 ÷ 30.5 = 22% (≤30% cap). |
| Logic (rule) | Colour term → Conversions, not Ranking [R-O1, E18]. Over break-even on both windows, ≥15 clicks → base cut ≤30% [R-N1]. Colour-named term keeps its colour [R-C3]. |
| Decision | CUT (objective retag to Conversions). |
| Action | `CUT — base $1.12 → $0.87 (−22%); objective Ranking → Conversions`. |
| Expected outcome | ACoS toward 23.8% with orders held within about −30%. |
| Validation | 14 settled days after the cut: ACoS and orders; if orders fall >30%, restore half the cut. |

### Example 3 (B6) — brand broad: defend and hold the negatives
| Step | Detail |
|---|---|
| Input | Brand broad ("Decolure"), 30 d: 621 clicks, 123 orders, ACoS 11.7% (most profitable campaign on the product); advertises Queen Olive; tagged Discovery. Proposed: brand negatives added to it. Receiving brand exacts: Queen 2 clicks in 30 d on Queen Olive; King 33 clicks. |
| Metric | ACoS 11.7% vs break-even 23.8%; receiving campaigns not defensive-ready (wrong colour, no volume). |
| Logic (rule) | Brand broad → Defensive [R-O2]; keep on its history colour, Queen White [R-N3]; brand negatives only when receiving exacts are defensive, on the hero, funded [R-S4, E10]. |
| Decision | DEFEND. |
| Action | `DEFEND — objective Discovery → Defensive; SWITCH AD Queen Olive → Queen White by hand; brand negatives held`. |
| Expected outcome | Brand orders held (~123 per 30 d at ≤ break-even ACoS). |
| Validation | Brand exacts serve on White with budget for 7 days → then load the negatives; weekly brand-term share and orders. |

---

## 4. Finding / Why it matters / Action / Expected impact

Every section of the decision document is built from items in this four-part form. [AP]

| Part | Content | Rule |
|---|---|---|
| **Finding** | The real figure, dated | Never a generality |
| **Why it matters** | The mechanism: profit, rank, velocity, inventory, share or efficiency | Say which one |
| **Action** | The exact change with the target value from the workbook | Never invent or contradict a workbook decision |
| **Expected impact** | Magnitude-appropriate range and horizon (§5) | Directional labelled as such |

Number actions within a section (Action 5.1, 5.2 …) so the Next steps list can cite them.

### 4.1 Thesis (decide first; it governs every section) [AP]
Read the signals: ACoS vs break-even; TACoS trend (monitor only unless owner target); inventory (in-stock SKUs, cover, stock-out-before-arrival); top-of-search impression share; velocity vs peak; rank week on week (terms up vs down, % at target); wasted-spend share vs 10% (discovery 40%).

| Thesis | When | What the document leads with |
|---|---|---|
| **INVEST / DEFEND** | Profit green, inventory green, waste low, but visibility / rank / velocity slipping | Lift top-of-search on priority ranking terms (placement-first), fix BOTH-FAILING syntaxes before scaling, seal concentrated leaks, expand only proven syntaxes. ACoS may tick up — say so and bound it |
| **PROTECT-AND-CUT** | Over break-even, high waste, or stock-out risk | Protect at-risk SKUs (routing, backup switches), kill waste, reallocate off losing placements, fund starved winners, expand only proven syntaxes |

State the thesis in the Summary with **one binding constraint** (e.g. B6: "the push is capped by price, not money — 11 of 13 funded terms are at or near their ceiling on day one").

### 4.2 Execution sequence [AP]
Order actions and the Next steps list: **protect revenue → stop bleeding → reallocate → expand.**
1. Protect revenue: stock routing, hero colour on ranking ads, brand defence, over-ceiling cuts on converting rows.
2. Stop bleeding: over-ceiling prices, zero-order waste, over-break-even non-ranking cuts, placement leaks.
3. Reallocate: mix fix, fund budget-truncated winners, push budgets within the limit.
4. Expand: harvests, seeds, discovery builds, tests (after events, never on deal days).

### 4.3 Summary block
3–4 prose paragraphs (condition + thesis + binding constraint; 2–3 root causes; offence vs clean-up split from wasted-spend share) → the decisions list → "Needs your decision" (numbered, each with options and trade-off in reviewer units, e.g. "holds ~$180/wk of saving to keep ~66 orders/wk") → a headline-numbers box of 6–8 KPIs with windows. [AP, PB]

---

## 5. Forecasting rules

1. **Ranges, not false precision**: "ACoS ~38–42%", not "39.7%". [AP]
2. **Anchored**: every forecast starts from a workbook figure with its window; say which. [AP]
3. **Settled baselines**: exclude deal days and the 7-day attribution tail; exclude stock-out and re-route stretches. Example (B6): a baseline of $515/day included four deal days; normal spend was ~$283/day. [B6 F03, SR]
4. **Credit steps with what similar steps bought** in the product's own history; nothing for paused keywords, retags or capped steps. Example (B6): +5–15% steps bought 0.85× clicks net of drift; a +75% jump credited with 2.5× clicks was not supported. [B6 F20]
5. **Requirements set volume and budget, never price**; reconcile summed click requirements to what the product sells before presenting them (B6: plan 187 TOS clicks/day ≈ 36 orders/day vs ~30 in the deal and 14 before it → a plan to grow toward, not a day-one forecast). [B6 F21]
6. **Typical magnitudes** (directional unless measured): a clean placement or negation fix moves the affected entity's ACoS 5–15 points over 1–2 cycles; coverage expansion +10–15 points SV-weighted coverage; funding a starved campaign buys a clean read (15+ clicks), not instant ROI; total spend roughly flat when reallocating. [AP]
7. **Name every soft coefficient** (uplift, elasticity, organic share proxy) and when it will be measured. [PB 22]
8. **Ranking pushes state their loss ceiling** = (push ACoS − break-even ACoS) × projected sales at the required spend, and state the payback (organic units once rank holds). [PB, B6]
9. **Spend forecasts** = today's spend moved by the price change, capped by budgets and the spend limit; show expected vs limit. [B6]
10. **Cut batches** carry an opportunity-cost check: projected lost-order value vs spend saved, at the more conservative (deal-state) margin; withdraw cuts that fail. [PB 21]
11. Never promise ACoS cuts in an INVEST week; never round implausibly. [AP]

---

## 6. Deliverables

### 6.1 Decision document (Word or Google Doc)
Skeleton: `templates/report-outline.md` (17 sections + appendix). Minimum: Summary with decisions and what needs the owner · How to read this · Where things stand · Rules applied · Goals and spend limit · Calendar / transition plan · area sections in Finding → Why → Action → Impact form · Competitive landscape (with coverage) · Tests · Exceptions · Next steps with dates · Appendix of engine/process fixes. Every major table followed by "What this table decides"; charts titled with the finding, direct labels, threshold bands shaded. Last two content sections: risks/falsification (dated checks) and numbered decisions requested. [SKILL, PB, AP]

### 6.2 Decision workbook (xlsx)
Full tab-by-tab spec with columns: `templates/workbook-spec.md`. Required tab set and purpose:

| Tab | Purpose | Key columns (full list in spec) |
|---|---|---|
| Start here | What the workbook is, sources and windows, how to read the trail, tab index | Tab · What it answers |
| Overview | Spend vs limit, decisions at a glance, needs the owner's decision | Line · $ a day · Basis; Decision · count |
| Metrics dictionary | Every metric used | Metric · Family · Meaning · Formula · Source · Window · Validation · Thresholds · Influence · Pitfalls |
| Decision rules | Every rule applied | Rule ID · Family · Applies to · IF · THEN · Threshold · Why · Guardrail · Exception |
| Decision trails | Worked examples end to end | Step · Detail |
| Campaign decisions | Every campaign, one decision, full trail | Identity · Objective now → correct · Input · Metric · Logic (rule) · Decision · Action · Expected · Validation · When · How it loads · metrics |
| Keyword decisions | Every search term with spend | Term · Decision · Rule · Why · Action · Class · Relevancy · SV · Rank · Target · Indexing · Owner · 30/90 d funnel · placement |
| Harvest & negate | Keyword actions grouped | Term · Class · Relevancy · Clicks/Orders/ACoS/Spend 90 d · Owner · Action |
| Push plan | Funded / waiting / at-target terms | Status · Term · Rank → target · TOS CVR · BE · Push price · Ceiling · TOS CPC · Price now → write · Base/Boost · Plan clicks · Budget · Why |
| Placement | Campaign × placement read and mix fix | Shares · CVR · CPC per placement · Read · Base/Boost/Price now → new |
| Variation & stock | Preferred / backup / clearance per size; per-SKU margins | Size · Available · Pace 7/30 · Cover · Next arrival · Verdict · Backup · Clearance |
| Inventory × PPC | How stock gates each decision | Step · Check · Rule |
| Financial guardrails | Break-even, ceilings, limits, per colour | Guardrail · Formula · Value · Crossed when · What happens |
| Competitor landscape / profiles / keywords / ASIN targets / gaps | See 6.3 (inside the workbook or as a separate file) | — |
| Exceptions & BLOCK | No-automatic-change conditions with current cases | Code · Condition · Treatment · Scope · Current cases |
| Validation plan | Checkpoints | When · What · Metric · Pass · Fallback · Rule |
| Checks | Integrity checks computed from the workbook | Check · Result (derived) |

Also, when relevant: Data conditions register; Impact ledger / prior-cycle grades; Source rows (every engine/audit row with a verdict); New campaigns & restarts; By hand (colour switches, objective tags, budgets); Before → After; Failure register. [WB, PB, B6]

### 6.3 Competitor workbook (optional separate file)
Use when the competitor pull is large or the reader differs. Tabs: Competitor landscape (patterns, sources & limits, market size/share, traffic trend, placement reach, segments, niche benchmarks, price ladder) · Competitor profiles · Hero ASINs & trends · Competitive keywords · Push terms vs field · Gaps & how to fill · Competitor ASIN targets (OFFENSIVE / TEST / AVOID) · Competitor → decisions (influence rules; what each never changes) · Landscape check. Every tab states coverage (measured of mapped competitors) and export dates. Resolve every ASIN to a brand. [B6, LP]

### 6.4 Change Review Sheet (own file, generated last)
- One row per (target, lever), sorted by exposure ($/day at stake). Actions copied verbatim from the workbook. [WB]
- Columns: identity (campaign, target, SKU) · funnel (impr, clicks, orders, spend, window) · placement split · ceiling and price multiple before/after · before / after / Δ · argument (why; why not the alternative; effect + when; reversal) · exposure · **Reviewer decision** (approve / reject / modify) · **Reviewer note** (both blank).
- Reviewer marks are applied literally and persist through every later regeneration (a reverted mark is a gate failure). [PB 19]
- Rows that must go to review: any gate failure; structural change (campaign, routing, match type, strategy); bid move >25%; budget move >$50/day; search volume above the owner's hand-off threshold (see §8). State the trade-off in reviewer units. [PB, WB]

### 6.5 Upload file
Only rows that change; true Bulksheets 2.0 layout (one sheet `Sponsored Products Campaigns`, exact 54-column header, State on every row, IDs as text, dates as text `yyyyMMdd`, no formulas/NaN, names ≤128 chars, no symbols in keyword text); price and budget rows of one campaign load together or not at all; withheld rows never exported; colour switches and SB/SD builds listed "by hand". Tell the user to upload directly without re-saving in Excel/Sheets. [CB, B6 F14–F15]

### 6.6 Google Docs / Sheets delivery
- **Connector limits**: creating a Google Sheet from CSV gives **one tab per Sheet and no formatting**. Either one Sheet per workbook tab, or one Sheet per file with sections stacked under a title row ("■ Tab name"), a blank row between sections.
- Split any payload over ~90,000 characters into parts, repeating the header row in each part. Prefix cells starting with `=`, `+` or `@` with a space so they are not read as formulas. Write $ and % values as formatted text (the CSV carries no number formats). Truncate very long reasoning cells only with a visible "…". [B6]
- **For the full workbook with formatting and all tabs, upload the .xlsx to Drive and open/convert it with Google Sheets (Drive import)**; use CSV Sheets only for quick views.
- Docs: upload the .docx and convert, or write natively; check tables and headings survive conversion.
- Link every delivered file in the reply; say which version governs if Doc and xlsx differ (the workbook governs row-level numbers). [PB]

---

## 7. Quality gate — consolidated checklist

Run as a separate pass over the finished files, as if reviewing someone else's work. Every check returns a count; **all must be 0 failures**. Fix the cause, not the row, then re-run the whole gate. Record RAN / NOT RUN per check; the Checks tab result is computed from the count, never typed; "PASS" beside a non-zero count is itself a failure. [PB, PF, WB]

### 7.A Inputs and data validity
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| A1 | Every requested input received or confirmed N/A | Intake checklist complete | No blank "Received" | PB, QA |
| A2 | Every sheet of every file enumerated and read | Status per sheet READ-FULL / READ-PARTIAL / NOT-RELEVANT / NOT-OPENED | No relevant sheet NOT-OPENED | WB |
| A3 | Sources reconciled | Bulk vs Command Center spend; Sellerboard units vs orders; on-hand − available − reserved | Differences explained; inventory gap ≤5 units or verified | SKILL, PB |
| A4 | SQP aggregated correctly | Market columns taken once per query, brand summed; rates recomputed | Brand ≤ market; shares 0–100% | SQP |
| A5 | Targets recompute | Target CTR = market CTR × 1.10; keyword target CVR = market CVR × 3.0 | Drift ≤2% on ≥90% of rows | SR, PF 1 |
| A6 | Quarantine applied | Rows with CVR/ACoS on 0 orders, CTR on 0 impressions, conflicting sources | No recommendation on them; refresh task logged | PB, DR |
| A7 | SKU provenance checked | Every performance verdict's window has advertised-SKU check (match / mismatch / mixed) | 0 verdicts without it | PB 15 |
| A8 | Economics fresh and per SKU | Margin age ≤45 days, no price/fee/packaging change since; no global default | 0 stale or defaulted rows | PB, SR |
| A9 | Missing ≠ zero | Search for 0 in fields with no source value | 0 | all |
| A10 | Event windows excluded | Verdicts using a window with >2 deal days; last-7-day attribution unflagged | 0 | B6 F01, E2 |
| A11 | Scope complete and clean | Campaigns spending on the product but missing from the list; shared multi-product campaigns under automation | Missing ones added and marked; shared ones excluded | B6 F13, F29 |
| A12 | Labels and totals | Blank syntax/SV/objective rows dropped; paused-ad-group rows with spend; keyword + target spend vs advertised-product report | Flagged, not dropped; totals match | PF 3–5 |
| A13 | DSTR feasible | Stated DSTR vs market purchases/30 | >50% re-scoped with reason | PF 2 |

### 7.B Objectives and structure
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| B1 | One objective per campaign | Count distinct objectives per campaign block (PT rows in keyword campaigns excepted) | 0 blocks with >1 | DR 1, OC |
| B2 | Objective present and consistent with targeting | Blocks with none; Defensive without brand keyword; Ranking without Exact; PT tagged Ranking | 0 | OC, WB |
| B3 | No Ranking on colour / competitor / other-language / misspelled terms | Classifier tokens vs objective | 0 | B6 E18 |
| B4 | One live bid-carrying instance per term | Normalised term (word order kept, plural/symbol merged) across enabled campaigns | 0 without a coexistence reason | DR 4, PB |
| B5 | Restart before build | New builds on terms with an existing exact (live or paused, close variants) | 0 | B6 E11 |
| B6 | No bids on non-deliverable rows | Bids on paused keyword/campaign, withheld duplicates, non-serving ads, Red / 0-stock SKUs (unless substitute) | 0 | DR 7, PF 17–18 |
| B7 | No structure on event days | Builds, folds, brand negatives dated inside a deal | 0 | B6 E1 |
| B8 | Brand negatives gated | Brand negatives added before receiving exacts are defensive, on the hero, funded | 0 | B6 E10 |
| B9 | Re-enables deduplicated | Duplicate check run on the post-re-enable population; re-enable and bulk in one upload | Yes | PF 21 |
| B10 | Modifier ↔ keyword pairing | TOS modifier with no funded keyword; funded ranking keyword on a 0% modifier | 0 | PF 20, WB |
| B11 | Only allowed columns changed | Diff source bulk vs output: only decision columns (and approved state/ad ops) differ; rows in = rows out; spend to the cent | 0 other diffs | PF 6–8, OC |

### 7.C Economics and pricing
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| C1 | Break-even per advertised SKU | Each row's break-even = that SKU's margin × its CVR basis; no blended parent; deal price in deal | 0 mismatches | SKILL, B6 F02 |
| C2 | No price above its ceiling | Ranking TOS price ≤ 2 × break-even CPC (or owner's time-boxed raise); non-ranking bid and effective price ≤ 1.0 × break-even at every placement | 0 | DR 5–6, PB 5, PF 13–15 |
| C3 | Above-break-even ranking authorised | Ranking rows above break-even without goal-gate clearance, or past the sufficiency point | 0 | PB 6 |
| C4 | Over-ceiling cut now | Rows above ceiling left in place or deferred | 0 | B6 F05 |
| C5 | Arithmetic recomputes | base × (1 + boost) = TOS price ±$0.03; every stated figure recomputed | 0 mismatches | PF 12, DR 13, PB 13 |
| C6 | Amazon limits | Boost >900%; base < price ÷ 10 on capped rows | 0 | B6 |
| C7 | Step caps | Push raise >+30%/day; other raise >+25%/cycle; gradual cut >15%/cycle (decisive ≤50%); base cut >50%; non-ranking cut >30% | 0 (caps, not targets) | B6, SR, PB |
| C8 | Strategy unchanged unless decided | Bidding-strategy diffs | 0 without fixed-bid-trial approval | B6, register #8 |
| C9 | No outside price anchors | Prices citing suggested bids, competitor CPCs or click requirements | 0 | register #18, B6 F21 |
| C10 | Deal-state ceiling respected | In-deal CVR used to justify a price above the deal-state ceiling | 0 | PB |

### 7.D Placement
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| D1 | Placement split before bids | Price rows without the campaign's placement split in reasoning | 0 | DR |
| D2 | Mix fix paired | Ranking campaigns with product pages >20% on ≥15 clicks given a boost raise without the base cut in the same write | 0 | B6 R-M1 |
| D3 | No TOS residue | Ranking TOS price lowered only as a side effect of a base cut | 0 | WB |
| D4 | Thin placement comparisons labelled | Two-rate comparisons with n <30 not marked "directional" | 0 | PF |

### 7.E Ranking and push
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| E1 | Qualifying terms decided | Terms passing every push gate not PUSH or WAIT-with-reason | 0 | B6 F06 |
| E2 | No unqualified push | PUSH on Red/Yellow stock, ceiling < own TOS CPC, listing flag, below-floor sample | 0 | SKILL, B6 |
| E3 | Rank collapse not funded | Rows that lost >10 places given a bid increase | 0 | DR 9 |
| E4 | At-plan not called failure | Delivery 95–120% of plan labelled failure / "estimate low" | 0 | DR 10 |
| E5 | Out-of-scope honoured | Ranking verdicts with <1 month rank history or no sized plan | 0 | DR 11 |
| E6 | No contradictory directions | Same term priced up in one campaign, down in another | 0 | DR 12 |
| E7 | Push terms complete | Target rank, date, clicks/day, budget, first milestone, re-read date on every push term | All present | PB, B6 |
| E8 | Sizing arithmetic | DSTR ≥1; organic + paid = DSTR ±0.02 (organic labelled proxy); clicks = paid ÷ own achieved TOS CVR; budget ≥ required × 1.05 (rounded up) | 0 failures | PF 9–11, 19, register #19 |
| E9 | Provisional rules confirmed | First use on this product of a provisional rule without a recorded confirmation | 0 | PB 25 |
| E10 | Holds justified | HOLD outside the mechanical list (both quality gates fail, CTR pass + CVR fail, zero delivery, budget truncation, plan > capacity) without a recorded ask | 0 | PB 24 |
| E11 | Infeasible plans escalated | Budget-infeasible plans not escalated; roster minimum budgets above cap without a pacing plan | 0 | DR 8, PB 18 |

### 7.F Inventory and variation
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| F1 | Stock gates on post-change state | Zone and stock-out-before-arrival computed after the planned change, 30-day pace | 0 pushes failing | SKILL, B6 F30 |
| F2 | Size locked | Ad switches that change size (except correcting a wrong size) | 0 | B6 E9 |
| F3 | Near-out colours kept out | SKUs with <7 days cover added to any ad | 0 | B6 R-C5 |
| F4 | Routing correct | Ranking ads on the size's best seller (or dated backup); discovery on the clearance colour; colour-named terms on their colour; routing read from Product Ad rows | 0 exceptions without reason | B6, WB |
| F5 | Economics rebuilt on reroute | Rerouted rows still priced on the departing SKU | 0 | PB |

### 7.G Budget and spend
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| G1 | Within the spend limit | Push budgets + expected other spend vs owner limit; event exceptions dated | ≤ limit | B6 R-F5 |
| G2 | Funded pushes have budgets | Push rows without budget; price and budget rows not paired in one load | 0 | B6 F14 |
| G3 | Truncation read first | Rate verdicts on campaigns in budget <70% of the day | 0 | PB |
| G4 | No invented TACoS target | Numeric TACoS target not set by the owner | 0 | register #17 |
| G5 | Cuts opportunity-checked | Cut batch without lost-order vs saved-spend test | 0 | PB 21 |
| G6 | Control arm | Mechanism change across many campaigns with none held unchanged | 0 | PB 20 |
| G7 | Soft coefficients named | Projections using an unnamed uplift/elasticity | 0 | PB 22 |

### 7.H Keywords, negatives, harvest
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| H1 | Every term decided | Search terms with spend and no decision | 0 | SKILL, B6 |
| H2 | Protected terms | Brand or push terms blocked; exact ranking terms negated | 0 | SKILL, register #12 |
| H3 | Negation evidence | Negatives without that occurrence's clicks/spend/orders or a structural reason; mode not named | 0 | PB |
| H4 | Relevant non-converters | Relevant terms negated instead of fix queue / reduce | 0 | PB, STR |
| H5 | Discovery candidacy | Broad/phrase/SB builds priced without 100 exact clicks or a stated coverage gap | 0 | PB 14 |
| H6 | Harvest complete | Harvests without ≥3 orders at ≤ break-even ACoS, or without the source negative in the same upload | 0 | register #22 |

### 7.I Competitor
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| I1 | Coverage stated | Competitor claims without "measured of mapped" and export date | 0 | B6 R-CI12 |
| I2 | No price from competitors | Any price or ceiling traced to competitor data | 0 | B6 R-CI4 |
| I3 | ASINs resolved | Targets without brand / own-product classification | 0 | LP, B6 R-X6 |
| I4 | Landscape verdicts | Push / waiting / at-target terms without a landscape verdict | 0 | B6 |
| I5 | Roster profiled | Measured competitors without a profile | 0 | B6 |

### 7.J Deliverable integrity
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| J1 | Full census | Campaigns in scope vs decision rows; in-focus campaigns without a decision | Counts equal; 0 undecided | SKILL, WB |
| J2 | Source rows verdicted | Every engine/audit row has a verdict; withheld rows absent from the upload | 0 | B6 F15 |
| J3 | Totals reconcile | Tab totals vs sums of components; plan headline figures vs workbook | Equal, or reconciliation recorded | SKILL, PB 27 |
| J4 | Overrides persist | Prior owner overrides / reviewer marks reverted | 0 | PB 19 |
| J5 | Column contract | Columns dropped vs previous version; tab names >31 chars; empty tabs without a reason | 0 | WB, DR 12 |
| J6 | Every action closable | Actions without re-read date and reversal condition | 0 | SKILL |
| J7 | Upload canon | Bulk file vs §6.5 rules | All pass | CB |
| J8 | Gate honesty | Checks typed rather than computed; PASS beside non-zero count | 0 | WB |

### 7.K Writing
| # | Check | How to test | Pass | Source |
|---|---|---|---|---|
| K1 | Reasoning present and complete | Actioned rows without reasoning covering the §1.2 chain | 0 | DR 2, PB 2 |
| K2 | Converting rows not parked | Rows with orders held for "thin clicks" | 0 | DR 3 |
| K3 | No templated text | String-compare reasoning within each entity type; >5 rows sharing decision, % change and first 120 characters | 0 duplicates | PB 16, SR, PF 22 |
| K4 | Action = reasoning | Re-derive the number from the row's own data | 0 mismatches | PB 17 |
| K5 | Cold-reviewer test | Sample the 3–5 highest-exposure rows per tab and read cold | Followable without questions | PB 17A |
| K6 | Banned content | Search delivered narrative for §, rule-ID patterns, "State ", "tier", "this skill", version strings, personal names, script/run names | 0 hits | PB 23/23A/23B |
| K7 | Sources and dates | Figures without window/source | 0 | SKILL |
| K8 | References resolve | Section references vs the document's own contents | 0 broken | PB 26 |
| K9 | Ranking reasoning extras | Push rows missing organic-proxy label, front-load note, review date | 0 | PF 24–26 |

---

## 8. Open questions for the owner
1. **Hand-off search-volume threshold** for the Change Review Sheet: workbook builder uses SV ≥250, plan builder SV ≥500. Not in the conflict register — owner decision; ask and record.
2. **Push daily steps vs the >25% hand-off rule**: the approved push plan steps prices up to +30% a day; the plan builder sends any bid move >25% to review. Ask whether approving the push plan covers its daily steps (proposed) or each step needs sign-off.
3. **Which bulk columns may change**: the placement-first method allows only New Bid / New Percentage / New Budget; the workbook builder also writes state and ad operations. Default here: decision columns plus approved state/ad changes, colour switches by hand — confirm.
4. **Rule-ID scheme**: rule IDs are allowed in workbook rule columns, but the consolidated skill does not fix one ID set; examples use the B6 IDs (R-P1…, E1…). Confirm the IDs the Decision rules tab should carry.
