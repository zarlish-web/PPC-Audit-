# SOP-32 Digest: Deal and Event Window Operations

Source: `PPC_SOP_32_Deal_and_Event_Window_Operations_v2_0.pdf` (17 pages). Digest of the plain-text extraction; nothing added beyond the text. Some tables were flattened in extraction and their columns were rebuilt from the content.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-32: Deal and Event Window Operations (Component #32 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead **jointly with the deals calendar owner** |
| Supersedes | SOP-32 v1.0 (2026-07-24) in full |
| Thresholds | Zero local thresholds; logs **12 ungoverned values** as Appendix A amendment items |
| Absorbs | The scheduled deal-window playbook deliverable and the scheduled annual-seasonality fold-in |
| Size | 13 procedures (v1.0: 7); 25-string KDR vocabulary + 2 v4.0-only strings + 10-string campaign-grain subset (v1.0: 5 locally invented strings); 4 worked examples (v1.0: 1); 12 failure modes (v1.0: 7); operator ramp; 18 interface contracts |

**Verdict / purpose.** An event window is "a priced distortion of four numbers at once" (traffic, conversion, CPC, price). It therefore gets its own plan, its own caps, its own reads, and a dated exclusion period before standing governance touches the data again. Because the price moves, **gate G9** marks every in-window CVR and ACOS read PROVISIONAL. A window generates "the most data of any 7 days in the quarter and the least usable data". The job is to buy the volume without letting the distortion enter a standing verdict.

Scope runs from calendar intake to scored close: classification, event plan and prediction, cap construction, modifier/placement posture, push amplification and in-window allowance, arming (freeze list + baseline snapshot), in-window daily block, cap-hit and stop decisions, close and revert, the settle and quarantine of window data, post-event scoring and class-factor calibration, liquidation windows on terminal-tagged units, and the annual seasonality calendar.

**The two governing rules (both v4.0):**
1. Every campaign touching the window carries an **explicit cap sized by rule M9**.
2. **Window-distorted data never feeds a standing verdict** (gate **G10**).

### Why a window distorts the numbers (Section 1.1)
- **Price falls.** Contribution per order falls by the full discount, and the break-even chain falls with it (rule **M1**: break-even ACOS = margin / AOV; Target = 50% of break-even; Max Acceptable = 75%). A 15% discount does not cut the ceiling by 15%. The window Max Profitable CPC is usually **below** the baseline ceiling even though traffic is higher.
- **Conversion rises.** This raises Max Profitable CPC (margin dollars x CVR, Family **F1**). The two moves partly cancel; the plan works out the net before the window opens.
- **Traffic rises.** Unchanged budgets run out by early afternoon, so rates read TRUNCATED under **G3**.
- **CPC rises** because competitors bid on the same days.
- A verdict on any one of the four in isolation is wrong in a direction the operator cannot predict.

### Five event classes (Section 1.2; carried from v1.0 Section 1 as institutional record)
| Class | Shape |
|---|---|
| Lightning deal | Hours, single variation, no ramp; the cap is the whole control |
| 7-day deal | The standard case, full plan (WE-1) |
| Tentpole (Prime Day, BFCM) | Multi-day, multi-product, twice-daily cadence; the only class where a first-time window has no own-history factor (WE-2) |
| Price-discount event | A standing price move rather than a badge; the price limb applies, the traffic limb largely does not |
| Liquidation deal on terminal-tagged units | Objective function is #27's, not the stage's (WE-4) |

v4.0 has no closed list of deal classes. Data Architecture v1.0 Section 9 carries "Deal window" as one value in the T5 closed event-type list, so the class is recorded in the plan, not the instrument (AM-10).

## 2. Scope and boundaries (Section 1.3)
Boundaries against components rebuilding concurrently in **Wave 5A (#24, #28, #33)** cite the Cross-Reference Ledger row rather than procedure numbers. The Ledger v2.5 correction register records roughly **40 owed corrections** of that class across six documents.

| Component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold, band, gate, scenario, lever limit, sizing rule, verdict string. A value v4.0 lacks goes to Appendix A |
| Pricing and deals calendar (P2.3, P3.5) | Decide whether a deal runs, its price, whether margin is approved. This SOP never re-litigates the price. Neither process document is in the corpus, which caps intake depth at what the calendar entry delivers (I-1) |
| #23 Ranking-push | Owns push sizing, M2 worksheet, funding, standup order, stop-loss, taper trigger release. Windows **amplify** live pushes and **never originate** them (origination = F8; violates **S-E1**). This SOP supplies the armed-window declaration |
| #24 Re-ranking and recovery | Owns loss diagnosis, baseline restoration, recovery sizing; the deal-hangover cause class. Handoff only at settle expiry and only where post-settle rank is still below armed baseline. Cited per Ledger row 24 |
| #15 Auto | Owns event autos end to end (standup, expiry naming, no-silent-conversion rule at SOP-15 P6 and P6.2) |
| #12 Exact | Owns exact structure; its **P9 event overlay** freezes structure changes inside an armed window and executes only what the plan names |
| #27 Terminal and LTSF-tier | Owns liquidation objective switch, **R2** allowable-ad-cost ceiling, **R3** cliff pacing, **R6** weekly expiry check. LTSF Master Decision and Operations System is outside the corpus per conflict **C6** |
| #28 Placement and modifier | Owns ceiling worksheet, ladder rungs, exit-bid discovery, modifier sizing, normalization of event premiums. This SOP decides only whether a premium is tested and books its removal. Ledger row 28 |
| #33 Sibling and family arbitration | Owns ownership declaration and guard enforcement. An undeclared contested root is noted in the plan; the G11 portfolio call runs there. Ledger row 33 |
| #26 Mature/defend, code red | Owns Recovery Mode execution. **Recovery outranks Event Mode**; a Recovery product runs the window at defense-and-proven-terms posture only (rule **T8**, rule **P7**) |
| #38 Bulk deployment | Owns staging format, upload, processing report, T+1 verification diff. Every arming/cap/raise/revert set stages in #38 format with event reference in reason string |
| #37 Automation rules | Owns rule register and change control. This SOP supplies the armed-window campaign list so #37 exclusion handling keeps platform rules off frozen scope |
| #35 Incrementality | Reads the event exclusion when voiding/deferring a test. This SOP publishes the exclusion dates |
| #31 Budget/envelope | Envelope law in the instrument layer (**T0 zone H, Account Rollup A2**) per open conflict **C3**; never cite a #31 procedure number. Window caps sum inside the product envelope |
| #34 Canada annex | Owns the CA delta; everything here applies in CA unless #34 overrides. CA deals calendar arrives on the same interface |
| #45 (hourly) | Dated deferral; its register line assigns event-window hourly boost removal to #32 until the Marketing Stream hourly feed lands |

## 3. Triggers (Section 2)
Monday cascade (Data Architecture v1.0 Section 12): **Raw Pull Pack lands Monday 06:00; workbooks refresh by 09:00; audit runs Monday; deployment Tuesday after BM huddle; daily checks on pushes and events** (rule **V4**).

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Calendar confirmation | Confirmed entry on deals calendar (**Economics and Context Pack Tab 4 "Deal calendar link (P3.5)"**) with class, dates, deal price | Same day; not later than the class intake date | P1, then P2 |
| Pre-event window opens | **T2 K2 "Event Mode"** = PRE-EVENT, **14 days** before start (Family F2 Event posture) | Same day | P2-P5 complete before P6 |
| Plan review due | Drafted plan + prediction held for joint sign-off (Authority Matrix "Event plans (#32)") | **Not later than 48 hours before arming** | P2 step 8 sign-off (text says step 7) |
| Arming mark | **T-1** relative to window start | Same day | P6 |
| Window live | T2 K2 Event Mode = IN-EVENT; T3 C2 shows staged values landed | Daily; **twice daily on tentpoles** | P7 |
| Cap reached | **T3 C3 "In-Budget Bucket"** and pacing read vs event projection; gate G7 event cadence | Same day, inside the block | P8 |
| Pacing deviation past line | Spend vs event projection deviating **more than 15%** (scenario **S-E2**) | Same day | P8 correction |
| Competitor deal on conquest target | Competitor deal-state flag in **T2 K8 "Competitor Depth (D8)"** | Same day | P7 step 5 stand-down (S-E3, S-C5) |
| Window close | Window end timestamp on calendar entry | Same day | P9 revert |
| Settle expiry | Exclusion ends **14 days after window** (G10) | Inside next Monday pass | P11; standing governance resumes |
| Terminal tag inside planned window | LTSF terminal or at-risk tag on a variation in the affected set | Same day | P12 |
| Seasonal SV Index turning | **T2 K1 "Seasonal SV Index Dir"** rising on a syntax outside any deal window (scenario **S-E6**) | Inside next Monday pass | P13 |
| Verification return | #38 T+1 diff flags landed-value mismatch on arming/raise/revert row | Same day | Redeploy delta; F7 if revert row |

## 4. Procedures

### Preconditions and gates (Section 3)
All read current in the **T7 Manifest** (Data Architecture Section 9). A missing or stale group suppresses its dependent execution class (G8); the plan records what it could not see.

| Precondition (T7 group) | Requirement / observable |
|---|---|
| Confirmed calendar entry | Class, start/end timestamps, deal price, deal fee. Economics and Context Pack Tab 4 row resolves; **T5 Product Log** has a "Deal window" entry with dates. No calendar row = does not arm |
| **A2** Deployment state | Current bulk state for every affected campaign: state, daily budget, bid, bidding strategy, placement multipliers. T3 C2 populated with current pull date. Without it F6 is already true |
| **A3** Pacing and in-budget | In-budget % and bucket per campaign, day-of-week spend curve. **T3 C3 "In-Budget Bucket"** and **"Pacing Deviation Flag"**. Workbook template records A3 as **PARTIAL** (day-of-week curve pending); where absent, pacing reads against the plan's own projection, substitution recorded |
| **A7** Eligibility | Every advertised SKU eligible, deal badge live at arming. **T3 C2 "Eligibility + Reason"**. G4 halts every lever on an ineligible/suppressed target and opens the listing fix the same day |
| **B8 and D1** Economics chain | **T0 zone C** named cells live (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC) with margin-table version and G9 state. Deal price is a price change: G9 marks in-window CVR/ACOS PROVISIONAL for the duration **and the trailing 7 days after price restores**; no conversion or fix-first verdict on those reads |
| Inventory cover (G6 band, days to stockout) | Cover clears projected window velocity **plus settle period** on every variation. **T2 K2 "Inventory Band"** GREEN and **"Days to Stockout"** > window days + settle days. **YELLOW freezes push spend at current level; RED tapers and re-points same day** (G6, scenarios **S-I2, S-I3**) |
| **D8** Competitor depth | Competitor price, rating, review count, deal state, stockout flags for conquest targets. **T2 K8 "Competitor Depth (D8)"** inside trailing week. Manifest template carries **D8 as MISSING**; S-E3 stand-down cannot be detected mechanically; downgrades to flag per G8 |
| **D9** Daily rank series | Daily organic rank on amplified terms. **T2 K4 "Organic Rank"** daily series link. Manifest carries **D9 PARTIAL at head terms only**; others read weekly |
| **E** Composite indices (Event Lift Index) | Event Lift Index for this product and class, from own history (Family **F16**, metric **E9**). Class factor resolves with number of prior windows. No prior window: M9 first-time path; borrowed category default is a gap (AM-4) |
| Family conflict state | Every root has declared owner or guard. **T2 K2 "Family Conflict"**, **T2 K8 "Term Owner (Family)"**. G11 |
| MKL hygiene | Every term in current MKL with syntax tag and relevancy (G12). MKL refresh date **inside 30 days** |

**Gates in force (v4.0 numbering; C9 alias noted):**
- **G1** quarantines impossible rows to flags.
- **G2**: bid reads need **>= 15 clicks (7d)**; CVR verdicts **>= 100 clicks**; CTR verdicts **>= 1,000 impressions**.
- **G3**: rates TRUNCATED **below 70% in-budget**; forces the budget lever before any bid conclusion (the standing state of a capped campaign in the back half of an event day).
- **G4** eligibility. **G6** inventory.
- **G7** envelope and pacing: campaign budgets reconcile to the product envelope; non-event pacing deviation **above 25%** vs the day-of-week curve alerts same day; during events, pacing is checked **daily against event projection**.
- **G8** packet completeness.
- **G9** price stability (fired by definition by a deal price).
- **G10** event exclusion: event weeks + **14 days following** excluded from trend verdicts. Event performance is evaluated only against the event projection and Event Lift Index, never baseline thresholds. Corpus calls it "G12", including the Data Architecture T5 column label "Trend-exclusion window flag (G12)".
- **G11** sibling conflict.
- **G12** MKL hygiene (no event clause in v4.0).
- **The freeze has no gate.** The in-window freeze on structure, main-image and un-named modifier moves is a standing account rule attributed to "G12" in five documents. It operates as a **plan state declared at P6**, enforced by lever holders (#12 P9, #15 P6, #37). **AM-1**, highest priority.

### P1. Event intake and classification (25-40 min per window)
1. Pull calendar entry from **Economics and Context Pack Tab 4 "Deal calendar link (P3.5)"**: event name, class, start/end timestamps, deal price, deal fee, affected ASINs and variations. Missing end timestamp or deal price means not confirmed; return to deals calendar owner the same day. Do not infer.
2. Classify into one of five classes; write it in the plan header. Terminal-tagged variation in affected set = **liquidation** regardless of calendar label, so go to P12.
3. Set intake date. Standard classes intake at PRE-EVENT open, **14 days** before start (F2: NONE / PRE-EVENT (14d window) / IN-EVENT / POST-EVENT (14d)). Tentpoles intake earlier per **A-to-Z System Map v0.9 Section 6** (event plans at **T-14 and T-30**); no v4.0 tentpole lead time (AM-2).
4. Read product posture in **T0** for every affected product and record 4 states: stage tag and TACOS band (**zone B row 3**); Recovery Mode (**zone A** verdict and code-red flag on **Account Rollup A0**); gate strip G1-G12 (**zone D**); earning-potential class (**zone E**). Recovery means defense-and-proven-terms only (T8, P7). A **CONSTRAINED** earning-class product with above-break-even spend runs **profit-only**; velocity needs route to deals and pricing (scenario **S-A10**).
5. Recompute window economics from T0 zone C (AOV, MarginPerOrder, margin-table version):
   - window AOV = deal price
   - window contribution = MarginPerOrder - discount $
   - window BE ACOS = window contribution / window AOV
   - window Target = 50% of that; window Max Acceptable = 75% (M1)
   - window Max Profitable CPC = window contribution x expected in-window CVR (F1)
   - Record all six. v4.0 does not say whether deal-price or baseline economics govern, so **compute both and state both** (AM-11).
6. Check inventory against the whole exposure: days of cover > window days + **14-day settle** on every variation (T2 K2 "Days to Stockout"). Clears the window but not the settle = YELLOW-class finding that caps the plan. Does not clear the window = return to deals owner with shortfall in units.
7. Log intake: one **T5 Product Log** entry, Event Type "Deal window", dates, affected scope, trend-exclusion flag set (read by rule **D5** attribution).

**Intake classification tree**
```
Affected set contains LTSF terminal or at-risk tag?        -> LIQUIDATION -> P12 (#27's objective; R2/R3 govern)
Duration under 24 hours, single variation?                 -> LIGHTNING -> P2 short form; cap is the control; no ramp, no modifier test
Multi-day, multi-product, category-wide traffic event?     -> TENTPOLE -> P2 full form at tentpole lead time; twice-daily P7; first-window path P3.4
Price move without deal badge or event traffic?            -> PRICE-DISCOUNT -> P2 full form, price limb only: recompute ceilings (P1.5), skip uplift cap basis
Otherwise                                                  -> 7-DAY DEAL -> P2 full form
```

### P2. The event plan and its prediction (60-90 min 7-day deal; 2-3 hours tentpole)
1. Affected-campaign set: filter **T3 Campaign Board** to live rows whose advertised SKU/ASIN is on the calendar entry. Record campaign name, type, objective tag, current daily budget, current bid or ad-group default, current placement multipliers **TOS and PP** (T3 C2). Nothing outside it is touched inside the window.
2. Halo scope: family and sibling campaigns not carrying the discounted SKU, as a separately labelled halo block. Halo rides the same caps but uses **baseline ceilings**. No v4.0 halo rule; the plan states its membership test (AM-8).
3. Name the live pushes to amplify: from **T2 K7**, every term on affected products with a Ranking objective and funded worksheet. Each gets an allowance line at P5. S-E1: no new experiments enter the window.
4. Contested roots: check T2 K2 "Family Conflict" and K8 "Term Owner (Family)"; note undeclared contested roots with guard; declaration is #33's.
5. Write caps (P3), modifier posture (P4), allowances (P5) as three tables. **The plan is the single change authority inside the window**; actions it does not name do not deploy.
6. Prediction with four values and a named horizon: **units sold across affected set; spend against total caps; post-settle rank delta on amplified terms vs P6 baseline; halo lift in orders**. V5 scores it at settle expiry. Missing any of the four = incomplete (rules **V1, P10**).
7. Stop conditions in numbers. v4.0 has S-E2's 15% correction trigger but no stop threshold; stop is a plan value with named owner (AM-6).
8. Joint sign-off: Authority Matrix v2.0 Section 1 row **"Event plans (#32)"**. PPC Lead signs the PPC side; deals owner signs calendar and price side; neither signs alone (standing rule 1 requires shared D cells to name their split). **Unsigned plans do not arm.**

### P3. Cap construction, the overspend guard (20-30 min)
1. Baseline: per affected campaign, trailing daily spend from **T3 C4** over a **clean 14-day window** with no prior event days and no logged price move (T5 confirms).
2. Size the cap (rule **M9**): event budget per priority term = baseline daily spend x Event Lift Index x event days. At campaign grain: **daily cap = baseline daily spend x class Event Lift Index; window budget = daily cap x event days**. The Event Lift Index is this product's own measured multiplier for this class (F16, E9).
3. Caps are **ceilings, not targets**. Reaching a cap is a decision (P8), never a silent raise or stop. An affected campaign with no cap = **F1** (worst in tentpoles).
4. First-window path: no prior window of this class means M9's clause (borrow category default and log variance) applies, but v4.0 has no category-default table. Open-decisions register item **PPC-DR-35** records tentpole factors as having no basis. **No first-window factor is written**: run at baseline with the named allowance as the only expansion authority, state the missing factor on the plan's face (AM-4; quantified in WE-2).
5. Reconcile to envelope: summed window caps + unaffected budgets inside the product weekly envelope on **T0 zone H**. Envelope outranks keyword ambition (rule **P2**). Over-subscription goes back to the plan for reduction by its own priority order: no across-the-board haircut, never an envelope raise here.
6. Stage caps as #38 rows (prior value, new value, reason string with event reference and plan version). **Deploy at arming (P6), not before.**

### P4. Modifier and placement posture (20-30 min)
1. Default posture: **no change**. A premium is earned from placement-level conversion evidence. Rule **L3** admits a premium only on a **TOS-EARNS** decomposition and cuts it on **TOS-VANITY**. Rule **M4** sizes multipliers so effective TOS CPC <= lower of (Max Profitable CPC for the objective, Expected CPC + tolerance).
2. If a premium is tested, the worksheet is #28's. The plan records: effective TOS CPC produced; the window Max Profitable CPC from P1 step 5 it is checked against; the dated removal on the P9 revert checklist. No booked removal = F7 waiting to happen.
3. Use the **window ceiling, not the baseline**. A multiplier legal last week can be illegal inside the window at the same bid. Called "the single most common arithmetic error in event planning".
4. **Bids hold.** The plan changes budgets and, where evidenced, multipliers. Bid moves only on the P8 exception path, never on a rate read (F2).
5. Hourly boost removal: any hourly boost or daypart adjustment from a prior window is removed at arming and goes on the P6 freeze list (assigned to #32 until #45 / Marketing Stream hourly feed lands).

### P5. Push amplification and in-window allowance (15-25 min per live push)
1. Confirm the push is live and funded in **T2 K7**: Objective Ranking, **Required Budget $/wk**, **Loss Ceiling $/wk** populated, **ETA Checkpoint** dated. No funded worksheet means no allowance. Funding a push inside a window = F8.
2. Allowance: a named dollar or percentage expansion of the push's window cap, available on a deliberate P8 call only. Rule **L4** single-step budget expansion **20-30%** is a standing-operation rule, not event authority. The allowance is a plan value (AM-5).
3. The worksheet's loss ceiling, ETA checkpoint, stop-loss stay #23's and are not suspended. P11 hands #23 realized CPC/CVR for the next worksheet.
4. Rank read cadence: daily where D9 series exists; weekly outside head set; plan says which.
5. Rank gained in window is provisional (**S-E5**): the **two-week at-target clock** starts only after the exclusion window. No taper on an event spike; taper release stays #23's.

### P6. Arming at T-1 (30-45 min)
1. Set **T2 K2 "Event Mode" = IN-EVENT** on every affected keyword row; T3 rows carry the window reference. The flip is the arming act (downstream reads it as the armed-window declaration).
2. Publish the **freeze list** naming every frozen class: (a) structure changes (creations, consolidations, promotions, demotions, archives, campaign or ad-group state changes) except those the plan names; (b) **main-image and A-plus** changes on affected ASINs; (c) modifier moves outside the plan; (d) platform-rule actions on affected campaigns. Sent to #12 (P9 overlay), #15 (event autos), #37 (exclusion handling), #38 (session pre-flight freeze check). No v4.0 gate (AM-1).
3. **Baseline snapshot.** Per affected term: organic rank (T2 K4), trailing CVR and CPC (T2 K5), current bid (T2 K8), price state (T0 zone C). Per affected campaign: daily budget, bid, multipliers TOS and PP, 14-day trailing daily spend (T3 C2, C4). Stored as a dated block against the plan; every post-event read compares to it and nothing else (missing = F6).
4. Deploy the arming set through #38 (caps, planned modifier changes, #15 event autos, plan-named state changes), with event reference in every reason string. Full T+1 verification; mismatch = same-day redeploy.
5. Confirm buyability at arming and at window open: offer live, buy box held, deal badge showing, variation orderable. Verified with the artifact.
6. T6 entries: one per deployed change (prior, new, plan reference as rule/scenario ID, expected outcome, **review date = settle expiry**). Rule V1.

### P7. In-window daily block (15-20 min; twice daily on tentpoles)
1. Pacing vs the plan's daily projection per campaign (not the day-of-week curve). G7 event clause: daily; **S-E2 correction trigger: deviation above 15%**. Record the deviation as a number. "On pace" without a figure is not a read.
2. Units and orders vs projection in the same block (S-E2's two branches need both).
3. Buyability and badge. A badge dropping mid-window is a calendar-side event: route to the deals owner same day with affected hours quantified.
4. Rank watch on amplified terms (daily where D9 series exists); recorded even when no decision follows.
5. Competitor deal check on conquest targets: a live competitor deal means stand down for the window and resume at window end (**S-E3** routing to **S-C5**). While D8 is MISSING, record that the check could not run.
6. Halo lift: record family spend and orders daily. Uncapped halo = F1 one level out.
7. **No reactive bid surgery.** In-window ACOS vs standing bands is not a decision input (G9 PROVISIONAL, G3 TRUNCATED, G10 excluded).

### P8. Cap-hit decisions and the plan stop condition (10-15 min per decision)
1. A cap hit is a decision. Record the hour, cumulative spend, cumulative units, deviation vs projection, and one of **RAISE** (within named allowance), **HOLD** at cap, or **plan stop condition**. Each writes a T6 row with evidence line.
2. RAISE needs the allowance and the worksheet: projected cost per order at the raised cap <= window contribution (P1 step 5). Otherwise HOLD regardless of unit pacing.
3. HOLD is the default on the under-performing branch. Over-pacing without matching sales lift is a leak; S-E2 directs truncating it the same day.
4. Under-pacing on priority terms (other S-E2 branch): budget or TOS steps toward projection inside rule **L2** limits (**50% per change, $0.50 floor**) and M4 effective-CPC ceiling.
5. Human confirmation: rule **P5** puts every **budget move above $50/day**, every **bid move above 25%**, and every gate failure in the human-mandatory tier. The Authority Matrix "Event plans (#32)" row holds every cap RAISE with both D-holders. Tentpole raises are confirmed before deploy, without exception.

**Cap-hit decision tree**
```
Cap reached on affected campaign
 +- In affected set with a written cap?   no -> F1: cap now from plan basis; root-cause plan omission
 +- Units pacing >= plan projection?      no (over-pacing w/o lift) -> S-E2 truncate: HOLD at cap; find leak same day
                                              (placement, irrelevant term, runaway bid), stage the fix
 +- Named allowance exists?               no -> HOLD; shortfall quantified; plan gap named at P11. No unallowanced raise, ever
 +- Worksheet: projected cost/order at raised cap <= window contribution/order?   no -> HOLD; record the arithmetic
 +- Confirmed by both plan D-holders?     no -> HOLD until confirmed
                                          yes -> RAISE to allowance ceiling; one #38 row per campaign w/ event ref; T6 evidence line
 Separately, every block: spend past plan stop threshold WITH units under it? -> PLAN STOP same day (only in-window scope reduction)
```

### P9. Close and revert (30-45 min)
1. Run the revert checklist **at the window end timestamp, not next Monday**: caps restore to P6 baseline; allowance raises step out; event modifiers step out via #28 normalization; event autos close per **SOP-15 P6.2** (fresh verdict, fresh objective tag, pre-load check before any event auto becomes standing); any hourly boost restored for the window removed; any state changed for the window returns to baseline.
2. Deploy the revert as one #38 staged set with event reference; read the **T+1 diff against the P6 snapshot line by line**. The gate artifact at close is the executed checklist with the diff attached.
3. Quantify anything that did not revert (F7): days lived and spend above baseline. "Premiums are rented by the window and returned with it."
4. **Do not lift the freeze at close.** The structure freeze runs through the settle.

### P10. The settle (10-15 min to set, then standing)
1. Set G10 exclusion marks on every affected T2 row: window days + **14 days**. Standing verdicts do not fire; the weekly pass reads them for gates only (as SOP-12 P9 step 3).
2. Quarantine from trailing averages: a 7-day window + 14-day settle removes **21 days**, so **T2 K5** four-period trend columns (**ACOS L30, P30, B30, L60**) cannot produce trend verdicts until clean days rebuild. A 30-day window holding 21 excluded days leaves 9 days, which won't clear G2 on most terms. State which rows are unreadable.
3. The hangover is expected and reads against the P6 baseline, never the window peak. A recovery push staged during settle = **F5**. Only a post-settle position still below armed baseline is a case (#24).
4. Publish exclusion dates to **#35** and the weekly audit.

### P11. Post-event scoring and class-factor calibration (45-60 min)
1. Score at **settle expiry**, not at close.
2. Event record, five lines: units vs predicted; spend vs total caps (incl. allowance raises); post-settle rank delta per amplified term vs P6 snapshot; halo lift in orders; **deal fees** (reported as own line, not folded into contribution; AM-12).
3. Score HIT / PARTIAL / MISS / WRONG-DIRECTION on T6. PARTIAL states which limb hit/missed, in numbers.
4. Calibrate: **realized spend multiplier = realized daily spend / P3 baseline; realized unit lift = realized units / predicted units**. The Event Lift Index moves toward the realized figures.
5. Return recalibration to #23 (next worksheet), #28 (if premium tested), deals calendar owner.
6. Post-settle tree:
```
Post-settle read per amplified term (vs P6 baseline)
 +- At or better than baseline?
 |    yes, and at/better than target rank for the required period after exclusion -> at-target clock starts (S-E5, T1); taper is #23's
 |    yes, but not at target -> standing governance resumes next pass; no event action
 +- Below baseline?
      Named cause is the window, no other log event -> recovery case: hand to #24 with P6 snapshot, window record, settle dates (Ledger row 24)
      Another T5 event in settle (price move, listing change, OOS, competitor entry) -> attribution contested; handoff carries both events (rules D5, X9)
```

### P12. Liquidation windows on terminal-tagged units (40-60 min)
1. #27 owns retag to liquidation, **R2** allowable-ad-cost ceiling, **R3** cliff pacing, **R4** what shuts off, **R5** structural quarantine into dated liquidation campaigns, **R6** weekly expiry check. This SOP contributes the window plan.
2. Take inputs from the LTSF row (salvage-parity price, alternative's per-unit value, remaining units, cliff date); do not derive. LTSF Master is outside the corpus (C6).
3. **Cap = R2 ceiling as a daily figure = allowable ad cost per unit x R3 required units per day.** The Event Lift Index does not outrank a recovery ceiling.
4. The window's value is the CVR move: a higher CVR raises R2 max liquidation CPC proportionally. If the lane still cannot buy the required clicks at the ceiling, route back to the LTSF system (closing a lane on arithmetic is correct).
5. Predict in units against the cliff schedule: units cleared, remaining units at close, revised units/day. No rank/share/ACOS.
6. Settle = #27's R6 weekly check resuming, not a 14-day quarantine (no trend verdicts to protect).

### P13. Annual seasonality calendar and pre-peak timing (3-4 h annual build; 10 min weekly)
1. Deal windows and demand seasonality are different machinery. This procedure absorbs the seasonality fold-in: index machinery, pre-peak timing rule, peak-readiness checklist.
2. Weekly: read **T2 K1 "Seasonal SV Index Dir"** per syntax per product. Rising index = candidate pushes get priority in the **M5** funding order. Pushes proposed after the peak are deferred to next cycle year (S-E6, rule **T4**: pushes time into a rising index, never after the peak).
3. Timing decision is made in the funding queue; the index is a standing input to the **O3** realism check and M5 allocation.
4. Annual calendar: category demand curve alongside confirmed deals windows, one per year. **Bedding category peak is Q4**, so build before Q4 opens. No v4.0 cadence/build date (AM-9).
5. Peak readiness (record per product): (a) inventory cover clearing peak + settle at peak velocity; (b) margin table refreshed (ceilings not provisional); (c) Event Lift Index seeded for every class the peak will run; (d) affected-set list drafted for tentpoles on the calendar.

## 5. Rules, thresholds and numbers

| Value | Meaning | Source |
|---|---|---|
| **14 days** | PRE-EVENT window before start; standard intake | Family F2 |
| **14 days** | POST-EVENT exclusion (settle) after window, all classes | G10, F2 |
| T-14 / T-30 | Event plans lead times; T-30 for tentpoles | A-to-Z System Map v0.9 Section 6 (AM-2) |
| **48 hours** | Plan signed not later than this before arming | Section 2 |
| **T-1** | Arming | Section 2 |
| **15%** | In-window pacing deviation vs event projection that triggers correction | S-E2 |
| **25%** | Non-event pacing deviation vs day-of-week curve alert | G7 |
| **70% in-budget** | Below = TRUNCATED | G3 |
| 15 clicks (7d) / 100 clicks / 1,000 impressions | G2 minima for bid / CVR / CTR reads | G2 |
| 7 days | Trailing PROVISIONAL after price restores | G9 |
| 30 days | MKL refresh freshness | G12 |
| 50% / 75% of break-even | Target / Max Acceptable ACOS | M1 |
| Daily cap = baseline daily spend x Event Lift Index; window budget = daily cap x event days | Cap formula | M9 |
| Clean 14-day window | Baseline spend basis (no prior event days, no price move) | P3 |
| 20-30% | L4 single-step budget expansion (standing operation; NOT event authority) | L4 |
| **50% per change; $0.50 floor** | L2 lever limits | L2 |
| **$50/day budget; 25% bid** | Human-mandatory moves | P5 |
| 0.8-1.0x of ceiling | AT-CEILING band | Family F1 |
| Two-week at-target clock | Starts only after exclusion window | S-E5 |
| 21 days | 7-day window + 14 settle removed from trailing series | P10 |
| Under 24 hours, single variation | Lightning class | P1 tree |
| Twice daily | Tentpole block cadence (no v4.0 basis, AM-7) | |
| Q4 | Bedding category peak | P13 |
| 2 clean audited windows (or 2 clean audited months) | Close ramp | Section 11 |
| R2 ceiling: allowable ad cost/unit = salvage net - alternative net; max liquidation CPC = allowable x CVR | Liquidation | #27 R2 (via WE-4) |
| R3 pace = remaining units / cliff days | Liquidation | #27 R3 |

### v4.0 rule / scenario IDs referenced

| ID | As described |
|---|---|
| G1-G4, G6-G12 | See gates list above |
| M1 | Break-even chain |
| M4 | Multiplier sizing; effective TOS CPC <= min(Max Profitable CPC, Expected CPC + tolerance) |
| M5 | Push funding order / queue |
| M9 | Event cap sizing; first-time events borrow category default and log variance |
| L1, L2, L3, L4 | Lever order; limits (50%, $0.50); TOS-EARNS/TOS-VANITY; 20-30% budget step |
| T1 | At-target clock / transition |
| T3 | Listed in deterministic logic references (not described further) |
| T4 | Pushes time into rising seasonal index, never after peak |
| T8 | Recovery outranks Event Mode |
| P2 | Product envelope outranks keyword ambition |
| P5 | Human-mandatory tier ($50/day, 25%, gate failures) |
| P7 | Mode precedence |
| P10 | Record completeness (prediction required) |
| V1, V4, V5 | Prediction / cadence / scoring |
| D5 | Product log consulted before crediting/blaming PPC |
| X9 | Contested attribution (cited in P11 tree) |
| O3 | Realism check (seasonal index input) |
| F1, F2, F16 (E9) | Product Economics; Product State and Strategy (Event posture); Extended Intelligence (Event Lift Index) |
| S-E1 | No new experiments enter window |
| S-E2 | 15% pacing correction; two branches (over-pacing w/o lift = truncate; under-pacing on priority = step toward projection) |
| S-E3 | Competitor deal stand-down routing to S-C5 |
| S-E5 | Rank gains provisional; clock starts after exclusion |
| S-E6 | Seasonal timing |
| S-C5 | Don't conquest into competitor's deal |
| S-A9 | Ceilings recompute immediately from new margin table |
| S-A10 | CONSTRAINED earning class: profit-only |
| S-I2, S-I3 | Inventory YELLOW / RED |
| #27 R2-R6 | Liquidation rules (not v4.0 R-series) |

### Verdict mapping (Section 5): KDR v3.0 25 strings + 2 v4.0-only (per C18)
v1.0's five strings (ARM EVENT PLAN; CAP HIT: RAISE (per allowance) / HOLD; PLAN STOP CONDITION; REVERT + SETTLE; SCORE EVENT) are **retired**. They map to P6, P8, P2 step 7, P9 and P11.

| Verdict | Event-window execution |
|---|---|
| QUARANTINE: DATA REFRESH | No changes (G1); refresh task runs same day; cap adherence unverifiable, recorded |
| UNLOCK TRAFFIC | S-E2 under-pacing branch with rank velocity intact; L2 unlock steps inside 50%; never on distorted rate read |
| FIX BUDGET (TRUNCATED) | Standing state of capped campaign late on event day; P8 decision, not uncapped raise |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | Test pauses its click quota; resumes at settle expiry excluding in-window clicks |
| FUND TEST (UNFUNDED PRIMARY) | Not executed in window (S-E1); stands up at settle expiry |
| RANK PUSH: FUND SIZED PUSH | Not originated (F8); funded-before-arming amplified; funded-during deploys at settle expiry unless plan named it |
| RECOVERY PUSH | Not during settle (F5) |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | Executes on amplified push when clicks under worksheet line, bounded by cap and allowance; named lever only |
| FIX CONVERSION FIRST; DEFER PUSH | Suppressed in window and settle (G9) |
| PLACEMENT FIX FIRST | #28 executes; removal booked on revert checklist |
| RE-POINT VARIATION | **Executes same day even inside frozen window** (G6 RED outranks freeze); added to revert checklist |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | Not on event spike (S-E5) |
| HOLD; DEFEND LIGHTLY AT RANK | No window action; gates only through settle |
| DEFEND AT FLOOR | Floors kept; drift restored in one staged step at settle expiry |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Suppressed through settle (F2); window Max Profitable CPC is in-window reference |
| INCREMENTALITY LADDER | No window execution; #35 voids/defers |
| ADD EXACT + RESTRUCTURE | Frozen unless plan names it; executes at #12 first clean day; exposure logged |
| CONSOLIDATE DUPLICATES | Frozen; executes at settle expiry at #12 |
| GRADUATE FROM DISCOVERY (v4.0: GRADUATE + STEER) | Frozen; #30 issuance continues, standup queues; event evidence read after settle |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) (v4.0: CUT / NEGATE) | Reactive negation on proven in-window waste is the one structure-adjacent action the freeze admits; event reference on negative |
| ENTER SBV ARBITRAGE | Not opened (S-E1); live arbitrage continues, rates excluded |
| OPEN / ROTATE / EXIT CONQUEST | #16's verdict; S-E3/S-C5 stand-down; opens frozen; exits execute |
| STOP-LOSS: CONCEDE OR DEFER | Executes; window does not suspend #23's stop-loss; freed budget returns at instrument layer |
| PAUSED-PENDING (REASON + RE-ENTRY) | Parking form; window parks' re-entry dated at settle expiry |
| LEAVE TO HARVEST | Term stays on discovery economics at capped bid; no exact in window |
| CONTINUE; VERIFY MOMENTUM (v4.0 13.1 only) | Standing state of amplified push pacing to plan; most frequent in-window state |
| PORTFOLIO CALL: ASSIGN LEAD (v4.0 13.1 only) | G11 catches two siblings amplified on one term; #33's call; both held at cap |

### Campaign-grain subset (Section 5.1; T3 **C6**, from Command Workbook REFERENCE tab validation list)

| T3 C6 verdict | When written |
|---|---|
| FUND BUDGET | Cap deployment at arming (P6) and confirmed allowance raise (P8) |
| HOLD | Default cap-hit outcome without allowance or refused worksheet; standing state of campaigns pacing to plan |
| TRIM BUDGET | S-E2 over-pacing-without-lift; plan stop. Only in-window scope reduction |
| RAISE MULTIPLIER | Evidenced premium sized by M4 vs window ceiling, removal booked same moment |
| CUT MULTIPLIER | Revert of premium at close; TOS-VANITY response |
| NEGATION PASS | Reactive negation on proven in-window waste, #29 standards |
| CONSOLIDATE | Frozen; written at settle expiry |
| RETAG OBJECTIVE | Event auto converting to standing (SOP-15 P6.2) |
| PAUSE | Event autos and dated event campaigns at close; stood-down conquest targets |
| ARCHIVE | **Never** inside a window or its settle |

## 6. Data inputs required
- **Deals calendar entry**: Economics and Context Pack **Tab 4 "Deal calendar link (P3.5)"**: event name, class, start/end timestamps, deal price, deal fee, affected ASINs and variations; margin approval from Pricing P2.3.
- **T0 PRODUCT COMMAND**: zone A (verdict, Recovery), zone B row 3 (stage tag, TACOS band), zone C named cells (AOV, MarginPerOrder, BE_ACOS, TargetACOS, MaxAccACOS, ExpectedCPC, margin-table version, G9 state, price state), zone D gate strip G1-G12, zone E earning-potential class, zone H weekly envelope / M5 funding queue.
- **Account Rollup**: A0 code-red flag, A2 envelope, A3 verification scoreboard.
- **T2 KEYWORD COMMAND**: K1 "Seasonal SV Index Dir"; K2 "Event Mode", "Inventory Band", "Days to Stockout", "Family Conflict"; K4 "Organic Rank" (daily series link); K5 trailing CVR, CPC, ACOS L30/P30/B30/L60; K7 push worksheet (Objective, Required Budget $/wk, Loss Ceiling $/wk, ETA Checkpoint); K8 current bid, "Term Owner (Family)", "Competitor Depth (D8)" (price, rating, review count, deal state, stockout flags).
- **T3 CAMPAIGN BOARD**: C2 (state, daily budget, bid, bidding strategy, placement multipliers TOS/PP, "Eligibility + Reason", pull date); C3 ("In-Budget Bucket", "Pacing Deviation Flag", in-budget %); C4 trailing daily spend (14-day clean baseline); C6 campaign verdict.
- **T5 PRODUCT LOG**: "Deal window" event entries, trend-exclusion flag ("Trend-exclusion window flag (G12)" column label), other events (price move, listing change, OOS, competitor entry).
- **T6 DECISION LOG**: rows with prior/new value, rule/scenario ID, expected outcome, review date, V5 score.
- **T7 MANIFEST** groups: A2, A3 (PARTIAL), A7, B8, D1, D2, D8 (MISSING), D9 (PARTIAL head terms), E composite (Event Lift Index), G6 inputs.
- **Event Lift Index** per product per class with prior window count (F16 E9).
- **Day-of-week spend curve** (pending in A3).
- **Raw Pull Pack** (for F6 reconstruction).
- **#38 T+1 verification diff** and processing report.
- **D2 inventory / ranked backup chain** (Economics and Context Pack, daily inventory cadence).
- **LTSF row** (salvage-parity price, alternative per-unit value, remaining units, cliff date) for P12.
- **MKL** (syntax tag, relevancy) and refresh date.
- **#23 live push registry/worksheets**; **#33 declarations**.
- Buyability artifacts: offer live, buy box, deal badge, variation orderable.

## 7. Outputs / artifacts

| Event | Artifacts | Storage / retention | Consumer |
|---|---|---|---|
| Intake (P1) | Classified calendar read; posture header (stage, mode, gate strip, earning class); window economics block (both bases); inventory cover read | Plan doc vs calendar entry; one T5 row ("Deal window", flag set). T5 retained for life of product | D5 attribution checks; #24; deals owner |
| Event plan (P2-P5) | Affected-campaign table w/ baselines; halo block + membership test; amplified-push list + allowances; cap table; modifier posture + booked removal; contested-root notes; 4-line prediction; stop conditions; two signatures | Plan doc, versioned, referenced by every staged row; **retained through following year's window of same class** | #12, #15, #16, #23, #26, #29, #33, #37, #38; BM owner at daily huddle |
| Arming (P6) | Freeze list (4 classes); baseline snapshot per term/campaign; arming set + T+1 diff; buyability confirmation; T6 rows | T2 K2 Event Mode, T3 window refs; dated snapshot block; T6 append-only, never purged | #12 P9, #15 P6, #37, #38 pre-flight; P11 |
| In-window blocks (P7, P8) | Dated block per day (twice on tentpoles): spend vs projection (deviation number), units/orders vs projection, buyability/badge, rank lines, competitor check or note, halo spend/orders, cap-hit decisions with worksheet | T6 rows; block record vs plan | P11; #23; PPC Lead; V5 |
| Close (P9) | Executed revert checklist (each line marked, dated); revert staged set; T+1 diff vs snapshot; exception list | Vs plan; diff with #38 session record | #28, #15, #37, P11. Checklist is the gate artifact |
| Settle (P10) | Exclusion marks w/ start/end; published exclusion range; settle T6 notes on drift | T2 marks; range in plan and weekly pass header | #35; weekly audit; #12 |
| Scoring (P11) | 5-line event record; V5 score with limb detail; class-factor calibration; recalibration returns | T6; Event Lift Index series retained across windows | #23, #28, deals owner, **Account Rollup A3**, next window |
| Liquidation (P12) | R2 ceiling / R3 pace at window price; daily cap; units-vs-cliff prediction; units cleared, revised pace | Plan + #27 liquidation campaign record | #27 R6; LTSF owner; deals owner |
| Seasonality (P13) | Weekly index read; annual calendar; peak-readiness on 4 states | Annual calendar re-issued yearly; weekly read in Monday pass | M5 queue (T0 zone H, Rollup A2); #23; inventory planning; deals owner |

Staged #38 rows: prior value, new value, reason string with event reference and plan version.

Alarm routing: **F1, F3, F10, F12** same day to operator queue + named escalation; **F2, F5, F9, F11** into block record and next pass worklist; **F4, F6, F7, F8** to PPC Lead with T6 history. Evidence-line format: campaign or term, signal value, gate/scenario reference, window reference.

## 8. Decision rights
- **"Event plans (#32)"**: D = PPC Lead **with** deals owner (PPC Lead signs PPC side; deals owner signs calendar/price side; neither alone); E = incoming operator, launch and CA operator (own scope), PPC Manager; R = BM owner at daily huddle.
- Human-mandatory: plan sign-off by both D-holders; every cap RAISE; every plan stop execution; tentpole arming; any plan revision inside a live window.
- "Weekly verdicts (established US)" (D PPC Lead; E assigned scope; R BM owner): resumption of standing governance at settle expiry; withdrawal of any verdict staged on an excluded row.
- "Push funding (the M5 queue)" (D PPC Lead within envelope, **CEO above it**): any allowance taking the affected set past the product envelope.
- "Bulk deployments (#38)" (E own scope; R PPC Lead): arming, raise, revert sets.
- "Code-red declaration + close" (D PPC Lead): F10 posture reduction.
- "Terminal/LTSF PPC lane" (D PPC Lead with LTSF owner): every liquidation window plan.
- "Sibling declarations (S-series)" (D PPC Lead): G11 hold on contested root.
- "Structure creation (all SOPs)": any structure change the plan names inside a frozen window.
- Standing rule 1 (shared D names its split); standing rule 5 (vacancy reverts D to PPC Lead, E to PPC Manager); standing rule 4 (Completion Directive still names PPC Lead on two rows the Transition Brief v1.2 assigns to incoming operator; **brief controls**).
- AI-executable with audit: plan drafting, cap arithmetic, window economics block, baseline snapshot assembly, pacing/deviation lines, cap-hit worksheet, revert checklist drafting, exclusion mark setting, event record and calibration, F1-F12 detection.
- Rule P5: budget >$50/day, bid >25%, gate failures human-mandatory.
- Escalation: F3 same day; F1 mid-tentpole immediately; F12 same day to deals owner + PPC Lead; F9 recurring to PPC Lead; F10 to code-red owner.
- Ramp: Week 1 reproduce WE-1 economics block to the cent; Week 2 supervised plan + 3 consecutive blocks + one cap-hit worksheet (pass bar: zero "on pace" without figure, zero untraceable caps); Week 4 unsupervised (plan sign-off and cap RAISE D-cells not delegated); close on **two clean audited windows or two clean audited months**.

## 9. Account-specific facts
- **Bedding category peak sits in Q4**; the annual calendar is built before Q4 opens.
- T7 manifest template status: **A3 PARTIAL** (day-of-week curve pending), **D8 MISSING**, **D9 PARTIAL at head terms only**.
- Ledger dependency **D4** (competitor feed) **open**.
- Open-decisions register item **PPC-DR-35**: tentpole factors have no basis; proposed interim treatment awaiting ratification.
- Ledger v2.5 correction register: about 40 owed corrections across six documents (Wave 5A: #24, #28, #33).
- Tier 3 live product economics spine was **not attached**; examples use the fictional base: AOV $80.00, contribution $28.00, BE ACOS 35.0%, Target 17.5%, Max Acceptable 26.3% (26.25%), baseline CVR 5.2%, baseline ceiling $1.46.
- v1.0 WE-1 spend-against-caps corrected from 96% to 94.6%.
- v1.0's worked case used a 7-day settle on a 7-day deal (shorter than G10's 14); v2.0 uses 14.

### Worked examples (illustrative)
- **WE-1 (7-day deal, 15% off)**: deal price $68.00; window contribution $16.00; window BE 23.5%; Target 11.8%; Max Acceptable 17.6%; CVR uplift 1.35x, so 7.02%; window ceiling $1.12 (exact 1.1232) vs baseline $1.46. Baselines: hero exact $28/day, family broad $16/day, sibling halo $8/day = $52/day. Event Lift Index **2.2** (from 2 prior windows). Caps $61.60 / $35.20 / $17.60 = $114.40/day; window budget $800.80. Allowance +20% on hero only. Prediction 640 units (91.4/day), rank +3. Day 2 hero cap at 14:00: spend deviation 71.4%; units 205 vs 182.9 (+12.1%). Raise to $73.92/day; CPC $1.05 gives 70.4 clicks, 4.94 orders, $14.96/order vs $16.00 (clears by $1.04); CPC at 0.93x ceiling (AT-CEILING 0.8-1.0x). T3 verdict FUND BUDGET. In-window ACOS 22.0% > window Max Acceptable 17.6%, but no bid moved. Rank 12 to 7 in window. Score: caps $813.12; spend $769.00 (94.6%); units 601 (93.9%, -6.1%); post-settle rank 9 vs 12 = +3. PARTIAL. Realized multiplier 2.11x, so index trims from 2.20 toward 2.11.
- **WE-2 (first BFCM)**: 5 campaigns, $146.00/day baseline, no factor. 11:00 spend $138.70 (deviation 107.3%); units 96 vs 54.1 (+77.5%). $12.61/hour; cap exhausts 11:35; 12.42 hours (51.8%) dark; forfeited spend $156.62; 0.692 orders/$; 108 orders forfeited; **$1,728.00 contribution not bought** on day 1 of a 2-day event. Raise of $156.62 to $302.62, confirmed by both D-holders and P5 (> $50/day). Second block 18:00.
- **WE-3 (edge)**: hero window spend $421.00, 401 clicks @ $1.05, 28 orders @ 6.98%, sales $1,904.00. Post-close pass read $15.04/order vs $28.00 (headroom $12.96) instead of true $0.96, overstating **13.5x**. ACOS 22.1% (deal-price sales) vs 18.8% (list-price sales of $2,240.00), a 3.3pp flattery. F9 withdrawal; would have been L4 25% step = $7.00/day x 14 = $98.00 unscoreable spend. F5: settle day 3 rank 14 vs baseline 12, recovery push blocked. Settle expiry (day 15) rank 13 vs 12 means recovery case to #24. 30-day column: 9 clean days, about 20 clicks/day, so about 180 clicks (clears 15-click bid bar, short of 100-click CVR bar "on most weeks").
- **WE-4 (liquidation)**: 480 terminal units, cliff 40 days; salvage $6.40/unit; LTSF alternative -$3.10/unit; allowable $9.50/unit; pace 12.0/day. Baseline CVR 4.0%: max CPC $0.38, 300 clicks/day needed, market CPC $0.55, so lane closed. Window CVR 6.5%: max CPC $0.62 > $0.55; 185 clicks/day. Cap $114.00/day; 207.3 clicks; 13.47 units/day; $8.46/unit vs $9.50. 7 days: 94 units; remaining 386 with 33 days, pace 11.7/day (0.3/day slack).

## 10. Open items

### Appendix A amendment items (12)
| Item | Gap | Operating path |
|---|---|---|
| **AM-1** (highest) | In-window freeze has no v4.0 gate (corpus calls it "G12": SOP-32 v1.0, SOP-12 v2.0 S3/P9, SOP-15 v2.0, SOP-23 v1.0, Transition Brief v1.2) | Plan state at P6, enforced by lever holders |
| AM-2 | Tentpole intake lead time (F2 only 14d; program T-14/T-30) | Lives on calendar entry and program cadence |
| AM-3 | Per-class settle lengths (G10 single 14d; v1.0 used 7d) | G10's 14 days governs all classes |
| AM-4 | First-window category default lift factors (M9; PPC-DR-35) | No factor; baseline + named allowance; WE-2 quantifies $1,728.00 |
| AM-5 | In-window allowance has no v4.0 basis (L4 20-30% is standing) | Plan value, both D-holders, P8 worksheet |
| AM-6 | Plan stop condition threshold | Plan value at P2 step 7, both limbs |
| AM-7 | Tentpole twice-daily cadence | Class carries cadence in plan |
| AM-8 | Halo scope definition | Plan states membership test; proposal: assign boundary to #33 |
| AM-9 | Annual calendar cadence/build date | Program cadence; proposal: V4 or component #40 |
| AM-10 | Event-class taxonomy (T5 has single "Deal window") | Classes in plan header; proposal: second T5 column |
| AM-11 | Basis for window ceilings (deal price vs baseline; S-A9) | Compute both; window basis governs in-window, baseline governs halo |
| AM-12 | Deal-fee treatment | Own line in P11, not in contribution |

### Conflicts / dependencies
- **C3** (#31 no procedural document); **C6** (LTSF Master outside corpus); **C9** (gate numbering); **C10** (vocabulary counts); **C18** (two v4.0-only strings).
- Ledger dependency **D4** open (competitor feed).
- Wave 5A rebuilds (#24, #28, #33): boundaries cited by Ledger row.

### Gaps / missing documents
- P2.3 Pricing and P3.5 Deals Calendar process documents **not held in corpus**.
- LTSF Master Decision and Operations System outside corpus.
- Tier 3 live economics spine not attached.
- Component #40 (named as a possible home for the annual calendar) and #45 (hourly; Marketing Stream hourly feed) not yet landed.
- Section 2 "Plan review due" points to P2 step 7 sign-off, but sign-off is P2 step 8 (step 7 is stop conditions).
- Referenced: Master PPC Decision Criteria System v4.0; KDR Template v3.0; PPC Strategic Doctrine v1.0 (Sections 2, 12, 13); Authority Matrix v2.0; Data Architecture v1.0; Command Workbook READ ME and REFERENCE tab; Cross-Reference Ledger (v2.5 correction register); A-to-Z System Map v0.9; Transition Brief v1.2; Completion Directive; open-decisions register; Supersession Map; SOP-12, 15, 16, 22, 23, 24, 26, 27, 28, 29, 31, 33, 34, 35, 37, 38, 41, 45.

### Version governance triggers
Review after every tentpole and quarterly; immediately on v4.0 increment (re-validate S-E, S-C5, M9, M1, G3, G6, G7, G9, G10, G11, G12, T3, T4, T8, L2, L3, L4, M4). Specific: (1) deals calendar field/cadence change; (2) v4.1 resolving any AM (AM-1 retires freeze gate-less status; AM-4 retires first-window path); (3) first tentpole on any product; (4) Amazon deal mechanics/badge/fee change; (5) D8 landing; (6) Marketing Stream hourly feed landing (retires P4 step 5); (7) rebuild of #24, #28, #33. Class factors version with P11 calibrations.

### Interface contracts (18), non-arrival consequences
| # | Interface | Non-arrival |
|---|---|---|
| I-1 | Deals calendar to P1 | No plan, no arming; unplanned window escalates to deals owner same day, hours quantified |
| I-2 | Pricing deal price + margin approval | Ceilings baseline-only, caps unpriced; arm only on deals owner's written price confirmation |
| I-3 | #41 economics to T0 | Ceilings PROVISIONAL; P13 peak readiness fails |
| I-4 | Inventory cover and bands (D2, G6) | Cannot arm (no workaround); unmapped variation bars RE-POINT |
| I-5 | Competitor deal state (D8) | Stand-down by hand; flag per G8; D4 open |
| I-6 | Daily rank series (D9) | Weekly cadence; plan records which terms |
| I-7 | #23 push registry | No allowance; cap hits resolve HOLD |
| I-8 | Armed-window declaration to #12, #15, #16, #22, #23, #26, #29, #37 | Standing ops run into window; consumers escalate. Recorded absence is valid; silence is not |
| I-9 | Event autos to #15 | None open (safe); missing close leaves auto live (SOP-15 F11 / F4 here) |
| I-10 | Exclusion state to #37 | Platform rules fire on frozen scope |
| I-11 | Staged sets to #38 | Plan not run; revert not deployed = F7 |
| I-12 | #38 verification diff | Score records unverified deployment |
| I-13 | Premium + normalization (#28) | No premium tested (correct default); no normalization = F7 |
| I-14 | #33 contested-root declaration | Both siblings hold at cap; G11 call requested |
| I-15 | Post-settle recovery handoff to #24 | Loss undiagnosed; refusal for lack of snapshot = F6 late |
| I-16 | Exclusion dates to #35 | Test reads window as treatment effect |
| I-17 | LTSF tier declaration via #27 | Cannot plan liquidation; entry returns to LTSF owner |
| I-18 | Scored record + class factor to #23, #28, deals owner, Account Rollup A3 | Class factor never converges; every window a first window |

### Failure modes (F1-F12)
F1 uncapped campaign in armed window; F2 bid surgery on window-distorted reads; F3 structure or main-image change in window (extend exclusion from revert date; SOP-12 mirror F8); F4 event autos live past close (SOP-15 F11); F5 hangover panic; F6 no baseline snapshot (rank limb unscoreable); F7 revert missed; F8 push originated in window (new); F9 trend verdict on excluded row (new); F10 Recovery-Mode product at full event posture (new); F11 competitor-deal stand-down missed (new; D4); F12 window armed into insufficient cover (new; forfeits deal fee too).
