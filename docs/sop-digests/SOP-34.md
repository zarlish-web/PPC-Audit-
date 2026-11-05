# SOP-34 Digest: The Canada Marketplace Annex

Source: `PPC_SOP_34_Canada_Marketplace_Annex_v2_0.pdf` (page footer counts 28 pages; closing line says "18 pages"). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-34: The Canada Marketplace Annex (Operating SOP, Component #34 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-11 |
| Owner | The CA operator under the PPC Lead (Authority Matrix v2.0 "Canada weekly block" row: D and E launch and CA operator; R PPC Lead) |
| Supersedes | SOP-34 v1.0-structure (2026-07-24) in full |
| Build standard | SOP Build Kit v1.0 twelve-element standard |
| Thresholds | Master PPC Decision Criteria System v4.0 only; **zero local thresholds**; 15 ungoverned values logged as Appendix A items (AM-1 to AM-15) |
| Absorbs | Scheduled marketplace-expansion trigger clause registered against #34 in SOP Program Gap Register v1.0, Section 4 (now P13) |
| Growth vs v1.0 | Procedures 0 -> 13; 6-row PENDING-CA table -> 14-row parameter register; worked examples 0 -> 4; failure modes 4 -> 12; adds operator ramp, 16 interface contracts, marketplace-expansion procedure |
| Definition Register status | #34 stays **PARTIAL** until the fifth CA packet item lands and P12 step 7 closes |

**Verdict / purpose.** Canada runs the same decision system on **CAD-native economics** at a **weekly cadence**. The annex is complete when every CA parameter carries a **definition, source, derivation, scaling relation and named consumer** - not when its value is populated. The logic transfers whole; every number re-parameterizes. The single structural finding: **Criteria System v4.0 carries no marketplace dimension at all**, so a CA value is "not a number waiting in a column that exists, it is a column that does not yet exist." No CA value is written anywhere in the document; every number is either quoted from v4.0, computed in a worked example on the fictional training base, or listed in Appendix A.

**Standing transfer rule.** All operating SOPs 12 through 38 apply in Canada exactly as written unless a row in Sections 2, 3, 4 or 5 of this annex explicitly overrides them (naming the US rule and the CA treatment). **Silence is not an override**; an operator who cannot find an override row executes the US procedure. Marketplace splits are doctrine (PPC Strategic Doctrine v1.0 Section 5.3 "Multiple phrase and broad campaigns": US vs CA always separate campaigns), so **no CA campaign shares a structure, budget or data pool with a US campaign**.

### 1.1 The unresolved dependency (D7 / conflict C7)
Component held on dependency **D7** and conflict **C7**: the **CA account packet (5 items, per v1.0 Section 7) has not landed**. The build proceeds to the boundary on the component owner's scope direction (annex is a process document); that direction supersedes the Cross-Reference Ledger's C7 resolution ("hold SOP-34 out of the build queue") **for structure, not for values**.

| Decision the annex cannot make | Packet item it waits on | What runs meanwhile |
|---|---|---|
| Any CA ceiling: break-even ACOS, Target, Max Acceptable, Max Profitable CPC per product | Item 1, per-product CAD economics | P3 builds spine structure and named cells; CA workbook computes nothing until cells hold CAD-native values. **No CA campaign runs before P3 closes (F5)** |
| CA volume floor register (numeric floors replacing v4.0 Section 6 rule O2 SV floors) | Item 2, CA keyword export with volumes and ranks | P4 fixes derivation (measured CA-to-US demand ratio per syntax family) and review cadence; WE-1 proves arithmetic on illustrative volumes |
| CA campaign registry state and consolidation plan | Item 3, CA campaign registry as-is | P5 fixes structure rule and promotion test; as-is registry decides only how much consolidation work exists, never whether the rule applies |
| CA conquest target lists and CA competitor depth read | Item 4, CA competitor set with price and rating states | Flag-obvious cases only (Section 4.4); block records mechanical check could not run, per gate G8 |
| CA event class factors and pre-peak calendar | Item 5, 12 months of CA seasonality by family | P11 runs CA windows at CA baseline with named allowance, no borrowed factor (same first-window path as SOP-32) |
| CA mature band, CA code-red trip, CA TACOS stage bands | Items 1 and 2 together, then a v4.1 release | **Nothing.** No operating substitute: #26 P3 code-red trips on a multiple of a band that does not exist in Canada. AM-6, AM-7; the only rows that **block** rather than degrade |

## 2. Scope and boundaries

**Owns:** the Canada delta and nothing else (parameter register, CAD-native economics spine, scaled volume floor register, CA structure instantiation, the weekly CA block, CA event inputs, packet-landing conversion, marketplace instantiation for any future marketplace).

**Does not own / does not decide:** any threshold (v4.0's); CA price, strikethrough, promotions (CA pricing owner); CA cover/restock/backup chain (CA inventory owner); never converts a US price into a CA one; never edits an automation rule; never infers LTSF tier rules.

| Adjacent component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, gate, scenario, lever limit, sizing rule, verdict string, in every marketplace. Annex executes, never decides. v4.0 has no marketplace dimension, so every CA-specific value is an Appendix A item |
| CA pricing and strikethrough owner | Decides CA price, strikethrough, whether a CA promotion runs. Annex reads and executes PPC consequences |
| CA inventory and stock owner | Decides CA cover, restock timing, CA backup chain. Annex executes gate G6 responses on what that owner publishes |
| #12 Exact | Owns exact structure, creation, weekly pass, taper. Same procedures run on CA workbook at CA cadence; CA delta = which terms qualify for a dedicated campaign (4.5) and pass frequency (4.6) |
| #13 Phrase, #14 Broad | Own discovery structure and weekly search-term triage. CA pass (P9) executes SOP-14's three-route triage unchanged; only the read window and accumulation rule change |
| #15 Auto | Owns auto structure and D5 targeting-group split end to end incl. Canada; Ledger defers CA delta to this annex = cadence and volume qualification only |
| #16 PAT and conquest | Owns candidate intake, target list, open/rotate/exit. In CA, full machinery activates only when CA volume clears scaled criteria; until then flag-obvious cases only |
| #23 Ranking push | Owns push sizing, M2 worksheet, funding order, standup, stop-loss, taper release. CA push uses same worksheet with CA DSTR, CA velocity, CA Expected CPC; no CA push sized on a US reference (F5) |
| #26 Mature, defend, code red | Code-red protocol (its P3) transfers unchanged, trips on v4.0 multiple of mature band; CA band does not exist (AM-7), so CA code red is declared on the PPC Lead's call |
| #27 Terminal and LTSF-tier | Owns liquidation switch and R-series rules on CA fee schedule and CA salvage values. LTSF Master Decision and Operations System is outside this corpus per conflict **C6**; annex infers no tier rule |
| #28 Placement and modifiers | Ladder mechanics transfer; CA ladder prices against CA blended CPC and CA ceiling, never converted US. Cited per Ledger row 28 |
| #29 Negation, #30 Harvest | Transfer unchanged. Graduation bar is v4.0's and does not scale (4.9); only the window to reach it changes |
| #32 Deal and event window | Owns event plan, cap, arming, in-window block, revert, settle, scoring in every marketplace. Annex supplies CA calendar seam and CA class factors |
| #33 Sibling arbitration | Family boards per marketplace; CA contest arbitrated on CA composites, never on US declaration. Cited per Ledger row 33 |
| #35 Incrementality | Owns test design, register, call. Annex publishes CA volume state; #35 decides whether a CA test is possible |
| #37 Automation rules | Owns rule register and change control. CA campaigns enter as own scope with own values; annex never edits a rule, never lets a US rule address a CA campaign (F6) |
| #38 Bulk-file deployment | Owns staging, upload, processing report, T+1 verification diff. Every CA change stages in #38 format with **marketplace key in the reason string**; annex consumes the diff |
| #31 Budget and envelope | Envelope law lives in instrument layer (T0 zone H, Account Rollup A2) per open conflict **C3**; annex never cites a #31 procedure number. CA envelope is its own, never a share of US |

## 3. Triggers

Lags use v4.0 Section 14 (Layer 9, V1-V8) rule **V4** cadence terms, read against the Monday cascade (Master PPC Data Architecture v1.0 Section 12): Raw Pull Pack lands **Monday 06:00**, workbooks refresh by **09:00**, audit Monday, deployment **Tuesday after BM huddle**. CA cadence is **weekly-only**; daily limb of V4 fires in Canada only where a gate response is same-day by its own rule (G4, G6 RED, G9 on price move).

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| CA account packet lands (whole or part) | Delivery from Head of Amazon Operations against 5-item list (4.12); each item received against its own parameter-register row | Same week; conversion runs in next Monday block | P12, then P1-P5 in order for whatever arriving items unblock |
| CA workbook not instantiated on a product with live CA spend | No CA Command Workbook for a product carrying CA campaigns in CA registry | Same week the spend is found | P1; spend recorded as **ungoverned** in block until P1 closes |
| CA parameter row has value but no source/derivation/consumer | P2 register completeness column | Same session | P2 step 6 reconciliation; value suspended from use (F7) |
| Weekly CA block due | Monday cascade slot after CA feeds refresh | Same day; late = run late and logged, never skipped (F3) | P6-P10 in order, one session |
| Two consecutive CA blocks missed | No CA session record for two consecutive weeks in CA T6 | Same day second gap found | Escalate to PPC Lead (Section 7, F3); block runs before any CA deployment resumes |
| CA price or strikethrough change | CA pricing owner's change mirrored to CA T5 Product Log as event type "Price move" | Same day | P8 step 2; gate G9 marks CA CVR and ACOS PROVISIONAL for trailing 7 days |
| CA cover falls / CA variation OOS | CA inventory owner's cover in CA T2 K2 "Inventory Band" and "Days to Stockout" | Same day (G6 RED is same-day) | P8 step 3; G6 responses at CA scope |
| CA campaign truncated | CA T3 C3 "In-Budget Bucket" below v4.0 gate G3 line | Inside the block that found it | P7 pacing and truncation sweep |
| CA term crosses its scaled volume floor (either direction) | CA volume refresh vs CA floor register (P4) | Inside next Monday block | P4 step 5 re-qualification, then P5 where structure class changes |
| CA syntax family demand ratio moves past recorded review band | Quarterly ratio re-measure at P4 step 6 | Inside quarter's first block after re-measure | P4 full re-derivation; every floor moves together or none does |
| Confirmed CA deal or event window | CA deals calendar entry with class, dates, CA deal price | Same day confirmed, no later than class lead time | P11, which hands plan to #32 |
| CA verification return mismatch | #38 T+1 verification diff flagging landed-value mismatch on a CA row | Same day | Redeploy delta per #38; F9 response where row is a revert or gate-driven |
| v4.1 release carrying any CA parameter | Criteria System increment notice | Before next CA block | P2 step 7 retirement of the Appendix A item, then Section 10 revalidation |
| New marketplace proposed | Expansion decision from CEO or Head of Amazon Operations | Before any spend in that marketplace | P13 |

## 4. Procedures

Time estimates are planning figures only (not thresholds). **P1-P5** = standing-up sequence (once per product; re-run when a parameter moves). **P6-P10** = weekly block, every Monday, one session. **P11-P13** = conditional.

### Preconditions (CA T7 Manifest, Master PPC Data Architecture v1.0 Section 9). Missing/stale field group suppresses its dependent execution class (v4.0 gate G8). CA manifest is its own; a US PRESENT says nothing about Canada (mechanism of F6).

| Precondition | Requirement / observable |
|---|---|
| CA parameter register (P2) | Every row: definition, source, derivation, scaling relation, consumers, status. Completeness column complete on every row whose consumer is exercised this cycle. Value with no source = suspended same session; source with no value suppresses only decisions in its consumers cell |
| B8 and D1 economics chain, CAD-native | CA T0 zone C named cells in CAD (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, WeeklyEnvelope) with CA margin-table version; zone C shows version and G9 state; currency label reads CAD. No ceiling from converted US value, ever (F2) |
| A2 CA deployment state | Current bulk state in-row per CA campaign: state, daily budget, bid, bidding strategy, placement multipliers. CA T3 C2 populated with current CA pull date |
| A3 CA pacing and in-budget | CA T3 C3 "In-Budget Bucket" and "Pacing Deviation Flag" resolved. Template records A3 PARTIAL (day-of-week curve pending); while absent, pacing reads against CA weekly envelope only and block records the substitution |
| A7 CA eligibility | CA T3 C2 "Eligibility + Reason" reads live. Gate G4 halts every lever on a target the day its ad reads ineligible/suppressed; opens listing fix task same day |
| CA inventory cover | CA T2 K2 "Inventory Band" and "Days to Stockout" resolved on every CA-advertised variation, CA backup chain named. G6: GREEN scales; YELLOW freezes push spend at current level; RED tapers to defense and re-points to declared backup same day |
| CA volume feed (item 2 + refresh) | CA T2 K1 "SV" populated with CA source and pull date. While MISSING: no qualification/de-qualification; whole family recorded unqualified, no US floor default (F1) |
| CA MKL and syntax taxonomy (G12) | Every CA term in CA MKL with syntax tag and relevancy score; CA MKL refresh date inside G12 window. Taxonomy tags **shared with US taxonomy by contract** (else P4 ratio uncomputable) |
| CA competitor depth (D8 equivalent) | CA T2 K8 populated inside trailing week. Template manifest carries D8 MISSING; no CA equivalent before item 4 -> flag-obvious only; downgrades to flag per G8 |
| CA rank series | CA T2 K4 "Organic Rank" with CA source and pull date. US daily rank series (D9) says nothing about CA; CA push read on US rank = F5 |
| Marketplace key | Every CA packet row, registry row, staged bulk row carries a marketplace value; resolves on CA T3 registry and every #38 staged row's reason string. Open decision **PPC-DR-20** (recommend tagging from day one). Without it: F6 |

**Gate classes (all 12 v4.0 Section 5 gates apply unchanged):**
- **Absolute, identical in CA:** G1 validation quarantine, G2 sample sufficiency, G3 budget truncation, G4 eligibility, G5 indexing/listing placement, G8 packet completeness, G9 price stability, G10 event exclusion, G11 sibling conflict, G12 MKL hygiene. G2 is statistical; a CVR estimate on 40 clicks has same width in Toronto as Denver; time to reach bar changes, hence 60-day window standard in CA.
- **Demand-relative, re-parameterized:** G6 inventory adequacy (CA cover vs CA velocity), G7 envelope and pacing (CA envelope). Rules unchanged; inputs CA.
- **Floors that are not gates:** v4.0 Section 6 rule O2 SV floors (>500 Ranking, >1000 Market Share) are objective-assignment criteria; "single most consequential US-scaled value in the system for Canada"; subject of P4 and WE-1; AM-3.
- **Oversight-class problem:** v4.0 Section 12 rule **P5** puts every action on a keyword >500 SV in the human-mandatory tier; almost no CA term reaches it. Annex therefore runs **the whole CA block in the human-mandatory tier** (stricter, never looser). AM-13.

### P1. Instantiate the CA Command Workbook (45-70 min per product)
1. Clone PPC Command Workbook TEMPLATE v1.0, named per its CLONE PROCEDURE step 1 with **marketplace token in the code position**. Ten tabs: T0 Product Command, T1 Syntax Board, T2 Keyword Command, T3 Campaign Board, T4 Placement and Bid, T5 Product Log, T6 Decision Log, T7 Manifest, REFERENCE.
2. **Set marketplace key** in workbook header and T3 registry key column (first step, prevents F6).
3. **Leave economics spine empty and say so.** T0 zone C cells stay empty until item 1; T0 zone D gate strip reads G9 blocked on CA margin table; no ceiling computes. Never seed with converted US values (F2 with evidence hidden).
4. Load what exists: Data Operations loads CA MKL into T2 and CA campaign registry into T3, deleting example rows (CLONE step 3). If items 2/3 absent, T2/T3 stay empty and T7 names both MISSING with verdict classes blocked.
5. Build CA manifest honestly from CA feed reality (own status, source feed, "Verdict Classes Blocked While Missing" cell per field group). CA completeness score computed on CA manifest, stamped on block header. CA workbook reporting US completeness = "most expensive single defect".
6. Register file in Account Rollup Workbook **A0** as its own row (not folded into US row). Family boards at **A1** per marketplace.

### P2. Build and maintain the CA Parameter Register (2-3 h first build; 15-25 min weekly reconciliation)
1. Columns fixed: parameter, definition, source, derivation, scaling relation to US, consumers, status. **Value is a seventh column, the only one allowed to read pending.**
2. Definition written in the terms the consuming rule uses (e.g. as M2 reads it).
3. Source named to the artifact (packet item number, feed, tab/column), not "the CA packet".
4. Derivation written as executable arithmetic; if a measurement, name window and refresh cadence.
5. Scaling relation, three classes only: **Class T (transfers)** - US value applies unchanged (ratio, bar or procedure constant); **Class N (native)** - computed natively from CA inputs, no relation to US; **Class R (ratio-derived)** - US value scaled by a measured CA-to-US relation (row names which and where). Parameter with no class is unusable.
6. List consumers by rule ID and procedure (converts missing number into named suspended decisions).
7. Reconcile weekly (block reads register first): (a) no row has value without source; (b) no row's consumers include a decision made this week while pending; (c) every row whose value arrived since last block has been through step 6. On v4.1: row status flips to governed, Appendix A item retires same increment, Section 10 re-validation runs.

**The register at v2.0 (14 rows; value pending on all):**

| Parameter | Class | Source | Derivation / scaling relation | Consumers (suspended while pending) |
|---|---|---|---|---|
| CA per-product economics spine | N | Packet item 1 -> CA T0 zone C named cells | CAD: CA AOV - CA landed cost - CA referral fee - CA fulfilment fee - CA returns provision. US spine not an input. Refresh monthly with CA margin-table version stamped | M1 break-even chain; every ceiling; M2 push budgets; M4 effective-CPC ceilings; #26 floor economics; #27 CA terminal math |
| CA break-even, Target, Max Acceptable ACOS | T | Derived in-workbook from spine | M1: break-even = margin / AOV; Target = 50% of BE; Max Acceptable = 75% of BE. Ratios transfer; inputs are CA | Every CA ACOS verdict; CA ladder; #26 CA floors |
| CA Expected CPC reference | N | Items 2 and 3, then CA auction observed in CA bulk | CA auction levels per category from CA delivered CPC by syntax family. US reference never a proxy or starting point | L2 bid references; M2 required budget; M4 multiplier sizing; #28 ladder seeds; O3 realism |
| CA search-volume floors (floor register) | R | Item 2, refreshed on CA volume feed | O2 floors x measured CA-to-US demand ratio per syntax family (P4) = CA family SV / US family SV on matched set. Re-measured quarterly; all floors in a family move together | O2 objective assignment; O3 realism; oversight-class filter; P5 structure class; #23 push candidacy; #16 conquest candidacy |
| CA demand ratio per syntax family | N | P4 measurement on item 2 vs US T2 for matched family | Measured, not assumed; v1.0's "roughly an order of magnitude under the US" is institutional record, not a divisor | Floor register; P5 structure class; CA pool minimums; #35 CA test feasibility |
| CA sample-sufficiency bars | T | v4.0 Section 5 gate G2, unchanged | No scaling (statistical). Only window to reach them changes (4.9) | Every CA rate verdict; read-limit flag; #35 test windows |
| CA DSTR and rank velocity references | N | Item 2 ranks, then CA rank series | CA daily sales-to-rank at CA volumes on CA competitors. US DSTR over-sizes CA push by ratio of markets | M2 clicks-to-rank; #23 push sizing, funding, ETA; #24 CA recovery sizing |
| CA TACOS stage bands | N | Item 1 + CA stage declaration; awaiting v4.1 | From CA contribution and CA stage posture; no derivation from US bands defensible (bands encode a market's paid-share structure) | T2 stage gates; T7 stage renewal; R1 Recovery trigger; #25 and #26 stage postures |
| CA mature band and code-red trip multiple | N | CA TACOS band row; awaiting v4.1 | Trip = multiple of CA mature band; the multiple is v4.0's and transfers; without band nothing to multiply | #26 P3 code-red; CA T0 zone A verdict banner; Account Rollup A0 code-red flag |
| CA structure and format targets | R | Item 3 + CA registry as it develops | M6 splits are destinations not quotas; CA exact/consolidated split moves toward tail-consolidation as volume qualifies terms; target stated as a **direction with a review date**, not a band | M6 structure review; P5 structure class; monthly CA structure finding |
| CA event class factors (Event Lift Index) | N | Item 5, then CA window history | Per CA event class from CA windows only. Boxing Day has no US counterpart; US Prime differs in CA in dates and depth | M9 event sizing; #32 cap construction and scoring; P11 |
| CA competitor set and depth | N | Item 4, refreshed weekly once feed exists | CA competitors on CA listings at CA prices; US overlap never assumed | O3 credibility; #16 CA conquest; G6 context reads; #26 CA incursion detection |
| CA envelope | N | CA stage band + CA sales -> CA T0 zone H | From CA stage TACOS ceiling on CA revenue; never a share of US; CA pushes compete only in CA M5 queue | G7; P2 precedence; M5 allocation; every CA budget verdict |
| CA read minimums for SD pools and AMC | R | Demand ratio row + CA registry | Pool/instance minimums scale with demand ratio (volume-qualification bars, not statistical). Re-checked semi-annually | SD audience build; #20 CA AMC instance decision; #35 CA test feasibility |

Nine of fourteen rows are class N ("the finding"); FX shortcut is "a different and wrong answer" (WE-2).

### P3. Build the CAD-native economics spine (60-90 min per product at packet landing)
1. CA inputs only from item 1: CA list price, CA landed cost per unit incl. inbound to CA fulfilment, CA referral rate for category, CA fulfilment fee for size tier, CA returns provision. A US-only figure is not an input; row stays pending.
2. Compute in CAD: CA contribution = CA AOV - four cost lines. CA BE ACOS = contribution / AOV. Target = 50% of BE; Max Acceptable = 75% (v4.0 Section 10 Layer 5 rule **M1**). CA Max Profitable CPC = contribution x CA CVR (v4.0 Section 3 Layer M, Family **F1** "Product economics").
3. Write values into CA T0 zone C named cells only, with currency label and CA margin-table version; derived ceilings repoint automatically.
4. **Exchange rate recorded nowhere in the decision chain**; FX belongs to the reporting layer only (whole of F2).
5. Set CA margin staleness clock (own clock per Economics and Context Pack's margin-table rule; CA fee schedule changes on its own calendar). G9 marks PROVISIONAL on a price change.
6. Publish spine to consumers (#23 push worksheets, #28 ladder ceilings, #26 floor economics, #27 CA terminal math); block record names version and date.

### P4. Derive the CA volume floor register (2-3 h first build; 30-45 min per quarterly re-measure)
1. Match term sets per syntax family: CA set from item 2, US set from US T2. **Match by syntax tag, not string.** Terms present in only one market stay in their own side's count.
2. Demand ratio = total CA family SV / total US family SV over matched sets. Record ratio, both totals, term counts, measurement date. **Per family, never per account.**
3. CA floor per objective = O2 floor x family ratio. Record US and CA figures. Round to nearest whole SV unit; record rounding.
4. State what did not scale: G2 sample-sufficiency bars, recorded on same page (mirror error = F8).
5. Qualify every CA term: Ranking-qualified, Market Share-qualified, or below both. Drives O2 assignment, P5 structure class, oversight filter. Crossing in either direction between refreshes -> re-qualified next block; structure follows at P5.
6. Re-measure quarterly and immediately on CA category event, CA listing expansion or US category shift. When ratio moves, every floor in that family moves together in one staged change.

**Term qualification decision tree (one term, one CA volume refresh):**
- CA volume feed present and inside refresh window? No -> no qualification; whole family unqualified; US floors NOT substituted (F1); feed gap named at G8.
- Term has CA syntax tag and relevancy score in CA MKL (G12)? No -> CA MKL maintenance; no objective, structure or spend.
- CA volume >= family's scaled Market Share floor? Yes -> Market Share-qualified, subject to O2 syntax-priority cap (secondary-syntax terms cannot carry Market Share).
- CA volume >= scaled Ranking floor? Yes -> Ranking candidate; O3 realism on CA inputs next (CA indexing, CA CVR vs CA benchmark, CA competitor credibility, CA inventory GREEN). Realism failure -> Discovery, not a push.
- Term converting inside CA consolidated structure? Yes -> LEAVE TO HARVEST at CA discovery economics, re-tested each refresh. No -> Discovery or Paused-pending per O2's tail, with re-entry criterion written as the floor to cross.

### P5. Instantiate CA structure at CA volume (2-4 h first build per product)
1. **Start consolidated** (consolidated-tail-first, v1.0 Section 4; Strategic Doctrine v1.0 Section 5.1 two-class doctrine: dedicated = budget isolation + rank attribution; consolidated syntax-exact = data density, which dominates at CA volume). Class boundary = oversight flag set by P4 floor register.
2. Dedicated CA campaign only on a term that clears the scaled Ranking floor **and** carries a funded push or declared distinct role (Doctrine Section 5.2 legitimacy test). Else consolidated CA syntax-exact campaign, ad group size per SOP-12 consolidation rules.
3. **Never clone US structure** 1:1 (F4). Registry built from CA qualified set upward.
4. Build walls same session per #29: graduated CA exact is negative-exact in CA phrase, broad and auto the same session. CA walls never reference US campaigns and vice versa.
5. Format posture: **SP-heavier** until CA-scale asset economics for SB/SD exist (v1.0 Section 3); SD audiences largely inactive (CA remarketing pools rarely clear read minimums). Re-checked **semi-annually** against P2 read-minimum row.
6. Stage everything through #38 with marketplace key and CA plan reference in reason string; deploy on CA block's slot; verify against T+1 diff.
7. Promote/demote on floor register: consolidated term crossing scaled Ranking floor + passing O3 -> own campaign; dedicated term below floor for **two consecutive refreshes** -> demoted back into consolidated at taper. Both logged with prediction and scored at review dates.

### P6. Weekly CA block Part 1: Cascade-lite (25-40 min)
Weekly not daily because CA volume accrues decision-grade evidence weekly; G2 says thin-sample swings are noise. Daily V4 limb only for G4, G6 RED, G9 price move.
1. Score last week first: CA T6 Decision Log rows whose review date arrived: **HIT, PARTIAL, MISS, WRONG-DIRECTION** (v4.0 Section 14 rule **V1**). No backlog.
2. Read parameter register (P2 step 7 three checks) **before any metric**.
3. Read CA manifest: T7 statuses and CA completeness score stamped on header; name every MISSING/STALE group and blocked verdict classes.
4. T0 Product Command: CA verdict banner, six-number header, CA economics block with margin-table version and G9 state, CA gate strip G1-G12, CA envelope zone H. Any RED -> AT RISK styling naming blocked action class; do not proceed past G1 quarantine or G6 RED without executing gate response first.
5. T1 Syntax Board: spend share vs target, cap status, four-quadrant diagnosis with weeks-in-diagnosis, coverage. Syntax caps transfer; CA cap is share of CA envelope.
6. T2 Keyword Command, oversight view: CA oversight filter = P4 qualified set (not a raw SV threshold). Verify gate columns before metrics: sample state, in-budget, eligibility, indexing, inventory band, family conflict, event mode.

### P7. Part 2: Pacing and truncation sweep (15-25 min)
1. In-budget per CA campaign from CA T3 C3, bucketed vs G3 line. Below line -> every rate marked **TRUNCATED**; budget lever evaluated before any bid conclusion. Record percentage as a number.
2. Utilisation vs objective-conditional target (v4.0 Section 9 Layer 4 rule **L4**), not a single account figure.
3. Reconcile summed CA budgets to CA weekly envelope (CA T0 zone H, G7). Over-subscription resolves by **CA M5 rank order**, never across-the-board cut, never borrowing from US.
4. Stage budget responses inside L4 step limits, one lever per row per cycle. If day-of-week curve absent, pace against weekly envelope and record substitution.

### P8. Part 3: Pricing, strikethrough, stock interfaces (10-20 min)
1. Read, do not decide (interfaces I-7, I-8, I-9).
2. Price/strikethrough: current state + any change in trailing 7 days. CA price change fires G9: CVR and ACOS PROVISIONAL for trailing **7 days**; no fix-first or conversion verdict; log CA T5 "Price move". Block states which rows are unreadable this week.
3. Stock: CA cover and band per variation. G6 at CA scope same day: YELLOW freezes CA push spend; RED tapers to defense and re-points CA ranking campaigns to declared CA backup. No CA backup in variation map -> re-point unavailable; only taper remains.
4. Route non-PPC (CA listing suppression, buy-box loss, offer problem) to owner same day with affected spend quantified; targets carry G4 halt until clear.

### P9. Part 4: CA search-term pass (25-40 min)
1. Run SOP-14 P3 three-route triage unchanged: converters -> #30 graduation queue; proven waste -> negative exact; drift clusters -> negative phrase on cluster root.
2. Read on the window the sample supports: **60-day window is the standing read window for CA rate verdicts** (G2 fallback becomes standard). Weekly: accumulate, route, stage; 60-day: rate verdicts.
3. Compute read-limit line = **G2 CVR bar / number of weeks in 60-day window**. Terms below flagged **read-limited** with current click rate; governed by structure and gates, not rate verdicts.
4. Hold graduation bar at v4.0 Section 9 rule **L6** order count (**three orders**), unscaled. CA harvest queue built by accumulation across passes. Scaled-down graduation = F8.
5. Stage negatives with evidence line in reason string: marketplace key, route, evidence window.

### P10. Part 5: Verdicts, staging, session record (25-40 min)
1. One verdict per CA oversight row from closed vocabulary (Section 5) with scenario ID and the **eight-element justification grammar** (Keyword Decision Record Template v3.0 "Read Me" sheet). Record is a Master Action Record (v4.0 Section 13.2 "Master Action Record v2").
2. State flags honestly (fallback benchmarks, provisional reads, read-limited terms, manifest gaps). "A record with no flags is more likely incomplete than clean."
3. One-lever rule and L1 order: budget (where G3 failing) -> bid -> placement -> negation -> structure -> status. One lever per row per cycle unless the verdict names two.
4. Stage through #38 with marketplace key, verdict, scenario ID, prior and new values in reason string; deploy on CA slot after sign-off; read T+1 diff line by line; mismatch = same-day redeploy of delta.
5. Sign-off: Authority Matrix v2.0 "Canada weekly block" row (D, E launch and CA operator; R PPC Lead; I CEO, BM owner). Every CA verdict human-mandatory; sign-off is the gate.
6. Session record (one per block): manifest state and completeness score, register check, gate findings, read-limited list, verdicts with predictions and review dates, staged set and diff result, what the block could not see. No session record = F3.

### P11. CA events, deals, seasonality (45-90 min per window)
1. CA calendar is its own (Boxing Day class has no US counterpart; CA Prime differs in dates and depth).
2. Hand plan to #32; supply CA class list, CA spine at CA deal price, CA affected set, CA class factor where exists.
3. First CA window of every class runs with **no borrowed factor**: M9 directs first-time events to category default; no CA default table exists and US factor is not one. Run at CA baseline with a **named dollar allowance** as only expansion authority (as SOP-32 for unseeded class). AM-11.
4. Window ceiling computed on CA deal price (cuts contribution in full; CVR rises; net answered before window). Method #32's, inputs CA spine.
5. Scored CA window seeds CA Event Lift Index for that class.
6. CA seasonality read separately; rule **T4** times pushes into a rising seasonal index, never after the peak, on a CA index (several bedding families peak in a different month).

### P12. Packet-landing conversion (1 day for all 5 items)
1. Receive item by item; partial arrival normal. Item 1 alone unblocks every ceiling (> half the blocked surface).
2. Item 1 (per-product CAD economics): run P3 in full; set CA T0 zone C; stamp margin-table version; clear G9 blocked; publish spine.
3. Item 2 (CA keyword export with volumes and ranks): run P4 in full, then P5.
4. Item 3 (CA campaign registry as-is): load to CA T3; reconcile to P5 qualified structure; produce consolidation and closure list as staged #38 rows.
5. Item 4 (CA competitor set): load to CA T2 K8; re-open conquest and defence surfaces per #16.
6. Item 5 (12 months CA seasonality by family): build CA annual demand calendar alongside CA deals calendar; seed class factors where history supports; otherwise first window remains the seed.
7. Reconcile register (every arriving value through P2 step 6). When all five landed and every row governed or has a named v4.1 item, annex increments and #34's PARTIAL closes. First weekly block on converted system the following Monday.

### P13. Marketplace instantiation: expansion trigger (2-3 h per new marketplace)
1. Trigger = expansion decision, not first campaign. Spend in uninstantiated marketplace is ungoverned; no acceptable threshold.
2. Copy annex; re-answer four questions: what transfers, what re-parameterizes, what stays deliberately simpler, what the packet must contain.
3. Build parameter register first (P2), before any workbook clone.
4. Name the marketplace packet and owner with a date (model: CA 5-item packet, owner at I-1).
5. Set marketplace key before first row exists.
6. Declare cadence from volume, not habit.

## 5. Rules, thresholds and numbers

### 5.1 Numeric values quoted or used

| Value | Meaning / source |
|---|---|
| 5 items | CA account packet (v1.0 Section 7) |
| 14 rows / 9 class N | Parameter register size; class N count |
| 3 scaling classes | T (transfers), N (native), R (ratio-derived) |
| > 500 SV | v4.0 rule O2 Ranking objective floor (US, unscaled) |
| > 1,000 SV | v4.0 rule O2 Market Share objective floor (US, unscaled) |
| > 500 SV | v4.0 rule P5 human-mandatory review tier keyword trigger |
| 50% / 75% of break-even | M1 Target ACOS / Max Acceptable ACOS (class T) |
| BE ACOS = contribution / AOV | M1 |
| Max Profitable CPC = contribution x CVR | v4.0 Family F1 |
| Target CPC = AOV x Target ACOS x CVR | WE-2 arithmetic (109.99 x 0.18 x 0.046) |
| >= 15 clicks in 7-day window | G2 bid-read bar (WE-1) |
| >= 100 clicks | G2 CVR verdict bar (WE-1, WE-4) |
| 60-day window | G2 fallback window; standing CA rate-verdict window; = 60/7 = 8.571 weeks |
| 11.67 clicks/week | Read-limit line = 100 / 8.571 (arithmetic on two v4.0 numbers; written into block record, never a rule) |
| 7 days | G9 PROVISIONAL window after a price change; trailing window for pricing interface |
| 3 orders | L6 graduation bar; does not scale |
| 50 clicks | Verdict "CONTINUE TEST TO 50 CLICKS AT CAPPED BID" quota; does not scale |
| 50% per change | L2 per-change bid limit (UNLOCK TRAFFIC) |
| 2 consecutive refreshes | Below floor -> demote dedicated CA campaign |
| 2 consecutive missed blocks | Escalation (F3) |
| 2nd consecutive week | I-7 pricing gap escalates to pricing owner |
| Monday 06:00 / 09:00 / Tuesday | Raw Pull Pack lands / workbooks refresh / deployment after BM huddle |
| 12 gates | G1-G12 all apply |
| 25 + 2 + 10 verdict strings | KDR v3.0 closed vocabulary + two v4.0 Section 13.1 strings + campaign-grain subset |
| 8-element | Justification grammar (KDR v3.0 Read Me) |
| 12 months | CA seasonality by family (item 5) |
| Monthly / quarterly / semi-annually | Margin-table refresh and M6 structure finding / ratio re-measure, M3 floor re-tests, SD/AMC read-minimum re-check / format-posture re-check |
| 16 interface contracts; 12 failure modes; 13 procedures; 4 worked examples; 15 AM items | Document structure |

### 5.2 Criteria System v4.0 rule IDs referenced

| Rule | Meaning as described |
|---|---|
| G1 | Validation quarantine (absolute) |
| G2 | Sample sufficiency; statistical click/impression bars; 60-day fallback (absolute) |
| G3 | Budget truncation line; below it rates TRUNCATED (absolute) |
| G4 | Eligibility; halts every lever on ineligible/suppressed ad same day (absolute) |
| G5 | Indexing and listing placement (absolute) |
| G6 | Inventory adequacy: GREEN scales, YELLOW freezes push spend, RED tapers to defense + re-point (demand-relative) |
| G7 | Envelope and pacing (demand-relative) |
| G8 | Packet completeness; missing field group suppresses dependent class; finding downgrades to flag (absolute) |
| G9 | Price stability; PROVISIONAL marks 7 days after price change (absolute) |
| G10 | Event exclusion (absolute) |
| G11 | Sibling conflict (absolute) |
| G12 | MKL hygiene; refresh window (absolute) |
| O1 | Objective requirement (campaign without objective blocks evaluation) |
| O2 | Objective assignment with SV floors; syntax-priority cap (secondary syntax cannot carry Market Share) |
| O3 | Realism (indexing, CVR vs benchmark, competitor credibility, inventory GREEN) |
| O5-O7 | Referenced (O5 with L7 on pause re-entry) |
| D1-D10 | Diagnosis order and benchmark hierarchy |
| L1 | Lever order: budget, bid, placement, negation, structure, status |
| L2 | Bid limits: 50% per-change limit and floor rule; bid references use Expected CPC |
| L4 | Budget steps; objective-conditional utilisation targets |
| L5 | Negation modes (pre-load / reactive / steering) |
| L6 | Structure; graduation order count (three orders) |
| L7 | Status (pause with reason + re-entry) |
| M1 | Break-even chain |
| M2 | Clicks-to-rank push sizing (needs DSTR, velocity, Expected CPC) |
| M3 | Taper ladder incl. step size and recorded minimum viable CPC; recorded-floor re-tests quarterly |
| M4 | Effective-CPC ceilings / multiplier sizing |
| M5 | Allocation; rank order for over-subscription; push funding queue |
| M6 | Structure targets (splits are destinations, not quotas) |
| M9 | Event sizing from measured lift; first-time events -> category default |
| T1, T2, T4, T7, T8 | T2 stage selects TACOS band; T4 time pushes into rising seasonal index, never after peak; T7 stage renewal; T1/T8 referenced |
| R1 | Recovery trigger (consumes TACOS bands) |
| P1, P2, P5, P10 | P2 precedence (envelope); P5 human-mandatory tier keyed on >500 SV |
| V1 | Scoring: HIT / PARTIAL / MISS / WRONG-DIRECTION |
| V4 | Cadence (daily, weekly, monthly, quarterly) |
| V5 | Referenced |
| F1 (family) | Product economics (Max Profitable CPC) |
| Section 13.1 / 13.2 | Closed verdict vocabulary / Master Action Record v2 output contract |

### 5.3 Verdict-to-execution mapping (CA execution conditions; meanings unchanged)

| Verdict (verbatim) | CA execution condition |
|---|---|
| QUARANTINE: DATA REFRESH | G1 as in US; commonest CA cause is a join gap; refresh task names the CA feed; no change deploys |
| UNLOCK TRAFFIC | L2 step under bid-read click bar, within 50% per-change limit and floor; frequently correct (under-fed) |
| FIX BUDGET (TRUNCATED) | P7 response below G3 line; CA envelope only; deliberate discovery caps recorded in CA T3 |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Unchanged quota; carries expected fill date from CA click rate; reviewed on that date |
| FUND TEST (UNFUNDED PRIMARY) | CA primary-syntax term with no CA coverage; bid seeds at CA Expected CPC; suspended while pending |
| RANK PUSH: FUND SIZED PUSH | **Suspended** until CA DSTR, velocity, Expected CPC exist; largest class the packet unblocks |
| RECOVERY PUSH | Same suspension; proven ceiling must be CA rank history |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Live CA push, clicks under worksheet line, CA velocity intact; named lever only |
| FIX CONVERSION FIRST; DEFER PUSH | Needs CA CVR vs CA benchmark; suspended in G9 window and on read-limited rows |
| PLACEMENT FIX FIRST | #28 executes; waits on CA placement data |
| RE-POINT VARIATION | Same day on G6 RED, outranks freeze; needs CA backup chain |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | M3 ladder whole; reads CA rank series |
| HOLD; DEFEND LIGHTLY AT RANK | Standing state; correct on more rows than in US |
| DEFEND AT FLOOR | Recorded CA floors from #28 ladder vs CA blended CPC |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Ceiling = CA Max Profitable CPC; suspended until P3 closes; barred under G2 CVR bar (60-day window) |
| INCREMENTALITY LADDER | #35; feasibility first; "no CA test possible this cycle" with numbers |
| ADD EXACT + RESTRUCTURE | #12 on CA registry; fires on P4 floor crossing, not head-share read |
| CONSOLIDATE DUPLICATES | Commonest during conversion; list from P12 step 4 |
| GRADUATE FROM DISCOVERY (v4.0: GRADUATE + STEER) | L6 order count unchanged; queue carried across passes |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) (v4.0: CUT / NEGATE) | Per #29; evidence line carries marketplace key and window |
| ENTER SBV ARBITRAGE | Needs CA SP and SBV reads; suspended; SP-heavier |
| OPEN / ROTATE / EXIT CONQUEST | #16; flag-obvious only until item 4 |
| STOP-LOSS: CONCEDE OR DEFER | Worksheet condition not relaxed; freed budget returns to CA envelope |
| PAUSED-PENDING (REASON + RE-ENTRY) | Parking for rows blocked on pending parameter; re-entry = parameter + packet item |
| LEAVE TO HARVEST | Converting CA term below scaled floor; stays consolidated; re-tested each refresh |
| CONTINUE; VERIFY MOMENTUM (v4.0 13.1 only) | Healthy line inside caps; one of two most frequent CA outputs |
| PORTFOLIO CALL: ASSIGN LEAD (v4.0 13.1 only) | G11 two CA siblings on one CA root; #33 on CA composites |

**Campaign-grain subset (CA T3 C6; Command Workbook TEMPLATE REFERENCE "CAMPAIGN VERDICT" list; Data Architecture Section 7):** FUND BUDGET (truncated campaign in CA envelope; key in reason string); HOLD (default, most frequent); TRIM BUDGET (over-subscribing CA envelope by M5 order; dated test at stop-loss); RAISE MULTIPLIER (suspended until CA placement evidence); CUT MULTIPLIER (cloned multiplier with no CA evidence; routine at conversion); NEGATION PASS (P9 output per #29); CONSOLIDATE (campaign count exceeds qualified set; F4 remedy); RETAG OBJECTIVE (objective mismatched after floor refresh, or no objective - blocks O1); PAUSE (reason + re-entry per L7 and O5; commonest re-entry = floor crossing or parameter landing); ARCHIVE (rare; pause instead unless product exits Canada).

## 6. Data inputs required

| Input | Location / field | Notes |
|---|---|---|
| CA account packet item 1: per-product CAD economics | -> CA T0 zone C | CA list price, CA landed cost per unit incl. inbound to CA fulfilment, CA referral rate for category, CA fulfilment fee for size tier, CA returns provision; in CAD, monthly, version-stamped (I-2) |
| CA margin table (version) | CA T0 zone C | Own staleness clock; per Economics and Context Pack margin-table rule |
| Item 2: CA keyword export with volumes and ranks | -> CA T2 K1 "SV" (with source, pull date), CA T2 K4 "Organic Rank" | Per term per syntax family; with matched US family totals (I-3) |
| US T2 (US Keyword Command) | Matched US family term set and SV | For demand ratio |
| Item 3: CA campaign registry as-is | -> CA T3 | Campaign, ad group, target inventory with budgets, bids, states (I-4); thereafter via CA bulk |
| Item 4: CA competitor set | -> CA T2 K8 | Price, rating, review count, stockout flags/state; weekly (I-5) |
| Item 5: 12 months CA seasonality by family | CA annual demand calendar | CA demand by family by month; annual re-issue (I-6) |
| CA bulk / A2 deployment state | CA T3 C2 | State, daily budget, bid, bidding strategy, placement multipliers, current CA pull date; "Eligibility + Reason" (A7) |
| A3 pacing / in-budget | CA T3 C3 "In-Budget Bucket", "Pacing Deviation Flag" | Day-of-week curve pending (PARTIAL) |
| CA inventory owner report | CA T2 K2 "Inventory Band", "Days to Stockout" | Per variation with ranked CA backup chain / variation map (I-8) |
| CA pricing owner report | CA T5 Product Log event "Price move" | Current price, strikethrough, changes in trailing 7 days (I-7) |
| CA deals calendar | P11 / #32 | Confirmed windows with class, dates, CA deal price (I-9) |
| CA feed refresh | CA workbook | CA bulk, CA search-term rows, CA rank, weekly before block (I-10) |
| CA search-term report rows | P9 | 7-day and 60-day windows; clicks, orders, spend per term |
| CA MKL | CA T2 | Syntax tag (shared US taxonomy), relevancy score, refresh date (G12) |
| CA placement data | #28 | CA feed, needed before placement verdicts |
| CA T0 Product Command | Zones A (verdict banner), C (economics), D (gate strip), H (envelope) | Six-number header |
| CA T1 Syntax Board | Spend share vs target, cap status, four-quadrant diagnosis, weeks-in-diagnosis, coverage | |
| CA T2 Keyword Command oversight view | Gate columns: sample state, in-budget, eligibility, indexing, inventory band, family conflict, event mode; campaign child rows | |
| CA T6 Decision Log | Prior rows with review dates | Append-only |
| CA T7 Manifest | Statuses, source feed, "Verdict Classes Blocked While Missing", CA completeness score | |
| CA parameter register (P2) | All 7 columns | Read first each block |
| CA floor register (P4) | Per family | |
| #38 T+1 verification diff | Line by line | I-12 |
| Account Rollup Workbook | A0 (product rows, code-red flag), A1 (family boards per marketplace), A2 (envelope), A3 (verification scoreboard) | |
| Marketplace key | Every registry, staged, rollup row | PPC-DR-20 |
| Authority Matrix v2.0 rows | Sign-off | |
| Keyword Decision Record Template v3.0 | "Bands & Verdicts Reference", "Read Me" | Closed vocabulary, 8-element grammar |
| PPC Command Workbook TEMPLATE v1.0 | CLONE PROCEDURE, REFERENCE tab | |
| Not usable as CA inputs | US feeds, US daily rank series (D9), US DSTR, US Expected CPC, US floors, US seasonal factors, FX-converted US margins | Hard stops |

## 7. Outputs / artifacts

| Event | Artifact set | Storage / retention | Consumer |
|---|---|---|---|
| P1 | CA Command Workbook (10 tabs), marketplace key, CA T7 from feed reality with CA completeness score | One per product, versioned; CA row in Account Rollup A0; CA family board A1 | Every later CA procedure; PPC Lead; Definition Register |
| P2 | Parameter register (definition, source, derivation, scaling class, consumers, status, value) + weekly reconciliation result | Standing document, versioned on every change, retained across annex versions | Every CA decision; v4.1 amendment owner (Appendix A); incoming CA operator |
| P3 | CA T0 zone C cells in CAD with margin-table version, currency label, staleness clock | CA T0, refreshed monthly; prior versions retained | #23, #28, #26, #27, every CA ceiling |
| P4 | Per family: matched term counts, both SV totals, ratio, scaled floors with rounding, qualified term list, did-not-scale statement | Re-issued quarterly, prior retained; qualification state lands in CA T2 K1 | O2, P5, #23, #16, #35, oversight filter |
| P5 | CA registry with objective tags and roles; consolidation and closure list; wall list per structure event; staged #38 set | CA T3; #38 session record; T6 rows with structure predictions | #12, #29, #38, monthly M6 finding |
| Weekly block (P6-P10) | Dated session record: manifest state + completeness score, register check, scored prior rows, gate findings, pacing/truncation numbers, interface receipts, search-term routes with counts, read-limited list with click rates, verdicts with prediction + review date, staged set, T+1 diff result | CA T6 append-only; session record retained for life of product | Next week's scoring; PPC Lead sign-off; Account Rollup A3; #38; components receiving routed candidates |
| P8 interface receipts | CA pricing/strikethrough state, stock state and band per variation, each dated, incl. "nothing changed" | Session record; CA T5 row where a change occurred | G9 marks; G6 responses; attribution checks |
| P11 | CA class declaration, affected set, spine at deal price, scored window with class-factor seed | Against #32's CA event plan; class factor as CA series | #32, #23, deals calendar owner, next window |
| P12 | Per-item conversion record: what landed, register rows closed, AM items retired, decisions resumed | Against annex and Definition Register #34 row | Definition Register; Ledger row #34; PPC Lead |
| P13 | Four answers, parameter register, named packet with dated owner, marketplace key | New annex registered in Supersession Map | CEO, Head of Amazon Ops; every operating SOP |
| Staged #38 rows | Reason string: marketplace key, verdict, scenario ID, prior and new values (negatives also: route and evidence window) | | #38 |
| CA harvest queue | Candidates with running order counts and expected arrival dates | | #30 |
| Alarms F1-F12 | Evidence line: CA campaign or term, signal value, gate/rule ref, register row, marketplace key | | Per routing tier |

## 8. Decision rights

| Authority Matrix v2.0 row | Rights |
|---|---|
| "Canada weekly block" | D and E: launch and CA operator; R: PPC Lead; I: CEO and BM owner. Sign-off is human-mandatory, not delegated (even at Week 4) |
| "v4.0 threshold changes" | D: CEO; E and R: PPC Lead; I: CA operator (never decides a threshold) |
| "Structure creation (all SOPs)" | E: launch and CA operator in own scope (inside signed block) |
| "Bulk deployments (#38)" | E: own scope; R: PPC Lead; T+1 diff read before block closes |
| "Event plans (#32)" | E: launch and CA operator; plan's D stays with PPC Lead and deals owner |
| "Push funding (the M5 queue)" | E: launch scope; D: PPC Lead within envelope, CEO above it; no CA push funded inside the block |
| "Launch-stage verdicts + batches" | D and E: launch and CA operator |
| "Code-red declaration + close" | D: PPC Lead (CA code red on judgement while band pending); CA operator executes |
| "Automation rules (#37)" | I: CA operator |
| Standing rule 5 | Unfilled role's D reverts to PPC Lead, E to PPC Manager (operative when CA seat vacant) |
| Standing rule 4 | Completion Directive names PPC Lead on two rows Transition Brief v1.2 assigns to incoming operator; the brief controls |
| Pricing / inventory / deals owners | Decide price, stock, deals; annex reads only (F11) |
| Head of Amazon Operations | Delivers CA packet (I-1); with CEO, makes expansion decisions |
| Data Operations | Loads CA MKL, registry, keyword export, competitor set, feed refresh |
| Human-mandatory | Weekly sign-off in full, every CA verdict, every CA structure change, every parameter admitted to register |
| AI-executable with audit | Cascade-lite drafting, register completeness check, ratio measurement and floor scaling, term qualification, pacing/truncation sweep, search-term triage draft, read-limit computation, verdict drafting, staged-set drafting with key, diff read, F1-F12 detection |

**Escalation:** F1, F8 -> PPC Lead on discovery with affected verdict count and demand/evidence share; F2 -> same day PPC Lead and finance seam; F3 on second consecutive gap; F6 -> PPC Lead and Head of Amazon Operations; F11 -> owner of the decision taken. Alarm routing: F1, F2, F5, F8 to PPC Lead same session; F3, F6 to PPC Lead and Head of Amazon Ops on second occurrence; F4, F7, F9, F10, F12 into block record and next worklist; F11 to decision owner same day.

**Operator ramp:** Week 1 observation (shadow one block; read register, manifest, zone C, floor register, T5, session record; reproduce WE-2 spine to the cent and FX comparison). Week 2 supervised (three consecutive blocks; one family's ratio end to end; one structure recommendation). Pass bar: **zero pacing lines without a figure, zero rate verdicts under G2 bar, zero staged rows without marketplace key**. Week 4 unsupervised (PPC Lead audits after the fact); close = **two clean audited blocks in a row plus one correctly refused verdict** (parameter and packet item named).

## 9. Account-specific facts

- **No live CA values exist in this document**; CA packet (5 items) has not landed; CA Command Workbook and registry state unknown. Tier 3 live product economics spine was not attached to the build.
- Worked examples use the **standard fictional training base**: AOV $80.00 USD, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3% (exact 26.25%), baseline CVR 5.2%.
- v1.0 characterised CA volume as "roughly an order of magnitude under the US" (institutional record, not a divisor).
- Several bedding families have a CA seasonal curve in a different month from US (stated as fact in P11 step 6).
- Illustrative (not live) worked-example figures:
  - **WE-1:** CA family 40 terms, total 4,180 SV (heads 620, 410, 355, 290; 36 others 2,505, none >190). US floors: 1/40 Ranking, 0/40 Market Share, 14.8% demand governed, 85.2% excluded. US matched family 46,200 SV; ratio 0.0905 (1:11.05); scaled Ranking floor 45.24 -> 45. Qualified 18/40 (4 heads + 14 at >=45 = 1,930 SV; 22 below = 575), 3,605 SV = 86.2%; 5.7x more permissive on volume qualification. Clicks 96/week (22, 14, 11, 9, 40 across 36); 1/40 has legal 7-day bid read; read-limit 11.67 clicks/week; 60-day clicks 188.6, 120.0 (clear), 94.3, 77.1 (do not); 2/40 can carry CVR verdict, 38 read-limited.
  - **WE-2:** CA AOV CAD $109.99; landed CAD $41.20; referral 15% = $16.50; fulfilment $8.85; returns 3.5% = $3.85; contribution CAD $39.59 (36.0%); BE 36.0%, Target 18.0%, Max Acc 27.0%; CVR 4.6%; Max Profitable CPC CAD $1.82; target CPC CAD $0.91. FX shortcut at 1.3600: contribution $38.08 on AOV $108.80, BE 35.0%, Max CPC $1.75; understates by $1.51 (3.8%). At 1.4100 (3.68% move): $39.48, CPC $1.82. 240 clicks/week x $0.07 = CAD $15.46/week; 13 x = CAD $200.93/quarter on zero business change.
  - **WE-3:** CA envelope CAD $420.00; spend $381.50 = 90.8%; CA-EX-01 hero exact $14.00/day budget, spent $92.40 ($13.20/day) = 94.3% utilisation, in-budget 96%; CA-BR-01 family broad in-budget 58% -> FIX BUDGET (TRUNCATED). T6: 2 HIT, 1 PARTIAL, 1 MISS. 41 served terms; Route B 2 negative exact; Route C 3-term cluster -> 1 negative phrase; Route A none. 11 verdicts: 6 HOLD/CONTINUE, 1 FIX BUDGET, 2 NEGATE, 2 PAUSED-PENDING (on CA Expected CPC); 8 read-limited.
  - **WE-4:** CA-EX-02 7-day: spend $58.90, 19 clicks, 1 order; CPC $3.10; CVR 5.26%; ACOS 53.6% (1.49x BE, 2x Max Acc); loss $19.31/order; in-budget 62% (truncated). 60-day: $402.60, 141 clicks, 9 orders, CPC $2.855, CVR 6.38%, cost/order $44.73, loss $5.14; 7-day overstated 3.76x. Correct ceiling 39.59 x 0.0638 = CAD $2.53 (11.5% step); 7-day ceiling would be $2.08 (17.5% too low); 16.45 clicks/week; ~65.8 clicks over four weeks.

## 10. Open items

### Appendix A amendment items (AM-1 to AM-13 to Criteria System; AM-14, AM-15 to other documents)

| Item | Gap | Operating path | Proposal |
|---|---|---|---|
| AM-1 (highest priority) | CA parameter column does not exist in v4.0 (v1.0 cited "v4.0's CA column"); program remaining-work list carries it in v4.1 batch | Every CA value lives in P2 register with status | Marketplace dimension as conditional column on every threshold with marketplace content; populate from P2 at same release |
| AM-2 | v4.0 has no marketplace dimension at all; single-marketplace by construction, unstated which | Three scaling classes substitute | State marketplace assumption in v4.0 Section 1; mark each threshold's class in Dictionary |
| AM-3 | O2 SV floors absolute (exclude 85.2% of WE-1 family) | P4 ratio scaling per family | Demand-relative floors with named basis, or per-marketplace floor table |
| AM-4 | G2 bars carry no statement they are absolute | P4 step 4 did-not-scale statement; F8 detects | One sentence in G2 (cheapest amendment) |
| AM-5 | No rule for read window where click rates cannot reach bars weekly (60-day is exception in G2, standard in CA) | 60-day standard; read-limit line; flag | Admit a read-limited state to the Dictionary |
| AM-6 | CA TACOS stage bands do not exist (T2) | **None**; PPC Lead declares stage posture on judgement | Admit CA bands from CA contribution, or state US bands apply with evidence |
| AM-7 | CA mature band and code-red trip multiple do not exist (#26 P3) | **None**; PPC Lead declares code red on judgement with entry figures | Admit with AM-6 |
| AM-8 | No CA Expected CPC and no derivation rule (L2, M2, M4) | Measured from delivered CA CPC by family after items 2-3; consumers suspended | Cold-start derivation for a new marketplace |
| AM-9 | No CA DSTR / rank-velocity references (M2) | CA pushes suspended | Admit with item 2; state DSTR is marketplace-scoped in M2 |
| AM-10 | No CA structure/format targets (M6) | Direction with review date | Marketplace-conditional targets or declare M6 US-only |
| AM-11 | No CA event class list or factors (M9); Boxing Day | First window at baseline + named allowance | CA class list; class factors marketplace-scoped |
| AM-12 | CA weekly cadence has no basis in V4 | Section 4.6 states cadence; same-day gate exceptions | Volume-conditional cadence in V4 |
| AM-13 | P5 human-mandatory tier keys on US SV figure | Whole CA block in tier | Express trigger as oversight-class membership |
| AM-14 | Master PPC Data Architecture v1.0 / Command Workbook TEMPLATE v1.0: no marketplace key schema position; Raw Pull Pack single-marketplace | Key written by convention (P1 step 2), not enforced | Marketplace as first-class key on workbook, registry, manifest, rollup |
| AM-15 | Cross-Reference Ledger #34 row has no Interfaces cell | 16 interface rows returned with this build's Ledger row | Adopt returned cell at next Ledger version |

### Conflicts, dependencies and open decisions
- **D7 / C7:** CA account packet not landed; C7 Ledger resolution ("hold SOP-34 out of build queue") superseded for structure only.
- **C3:** #31 budget/envelope absorbed into instrument layer (T0 zone H, Account Rollup A2); no #31 procedure cited.
- **C6:** LTSF Master Decision and Operations System outside this corpus; no LTSF tier rule inferred.
- **PPC-DR-20:** open decision on marketplace scope (tag every packet and registry key from day one).
- v1.0 corrections: v1.0 attributed in-window freeze to G12 and named G10 the objective gate (v4.0: G12 = MKL hygiene, G10 = event exclusion). Change note says the "corpus alias divergence" is recorded in Appendix A, but **no Appendix A item (AM-1 to AM-15) addresses gate aliasing** - gap in the text.
- A3 day-of-week curve PARTIAL in template; D8 competitor depth MISSING in template.
- Authority Matrix standing rule 4: Completion Directive vs Transition Brief v1.2 conflict on two rows (brief controls).
- Page count inconsistency: footer "18 pages" vs page numbering "of 28".

### 16 interface contracts (non-arrival consequences)
I-1 CA packet (Head of Amazon Ops -> P12): annex stays structure; #34 PARTIAL. I-2 item 1 economics (Head of Ops + finance -> P3): no ceiling; CA campaign does not run / spend recorded ungoverned. I-3 item 2 keyword export (Data Ops -> P4): every family unqualified; structure holds consolidated; no promotion. I-4 item 3 registry (Data Ops -> P5, P12): no consolidation list; F4 persists. I-5 item 4 competitors (Data Ops -> P4 realism, #16): O3 on rank and economics alone; flag-obvious; G8 flag. I-6 item 5 seasonality (Head of Ops -> P11): every window a first window; T4 has no CA index. I-7 price/strikethrough (pricing owner -> P8.2): treat as unknown, suppress conversion verdicts; escalate second consecutive week. I-8 cover/bands/backup (inventory owner -> P8.3): G6 cannot be evaluated - one precondition with no workaround; unmapped variation bars re-point. I-9 deals calendar (deals owner -> P11, #32): no window arms; unplanned window escalates same day with hours quantified. I-10 feed refresh (Data Ops -> P6): run and state staleness; skipping = F3. I-11 staged sets (P5, P10 -> #38): verdicts undeployed, predictions unscoreable. I-12 verification diff (#38 -> P10.4): F9; record gap. I-13 register + Appendix A (P2 -> PPC Lead): gaps invisible. I-14 marketplace key (P1 -> #37, #38, Rollup): F6; restate totals. I-15 CA scope declarations (P5, P10 -> #33, #16): contest settled by whoever spends more. I-16 marketplace instantiation (CEO/Head of Ops -> P13): ungoverned spend.

### Failure modes (summary)
F1 raw US thresholds on CA volume; F2 FX-converted margins in decision chain; F3 skipped weekly block; F4 US structure cloned 1:1; F5 CA decision on a US input; F6 CA spend mixing into US totals; F7 parameter with value and no source; F8 sample-sufficiency bars scaled down; F9 change deployed without verification diff; F10 CA event on US class factors/calendar; F11 pricing/strikethrough/stock decided inside annex; F12 packet items used before register reconciles them.

### Named documents referenced (not present in this file)
Master PPC Decision Criteria System v4.0; Keyword Decision Record Template v3.0; PPC Strategic Doctrine v1.0 (Sections 5.1, 5.2, 5.3, 11); PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0 (READ ME, CLONE PROCEDURE, REFERENCE); PPC Cross-Reference Ledger; SOP Program Gap Register v1.0; SOP Build Kit v1.0; Operations Definition Register; Supersession Map; Economics and Context Pack; Transition Brief v1.2; Completion Directive; LTSF Master Decision and Operations System (outside corpus); SOP-34 v1.0-structure; SOPs 12-16, 20, 23-33, 35, 37, 38.
