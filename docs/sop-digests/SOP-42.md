# SOP-42 Digest: Ad Policy, Moderation and Claims

Source: `PPC_SOP_42_Ad_Policy_Moderation_and_Claims_v1_0.pdf` (14 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-42: Ad Policy, Moderation and Claims (PPC Department, Operating SOP, Component #42 of the Operations Definition Register) |
| Version | 1.0 (first build, no prior version; nothing carried forward) |
| Date | 2026-08-09 (due 2026-08-17, delivered ahead of date) |
| Owner | PPC Lead, **Creative seam** per the Gap Register charter |
| Coupled to | Components 17-19 (SB/SBV/SD playbook) |
| Thresholds | v4.0 only; **zero local thresholds**. v4.0 contains **zero moderation, ad-policy or claims rules**, so this SOP issues **zero closed-vocabulary verdicts**; every numeric control needed is on the v4.1 amendment register (Section 13) |
| Content | 1 standing instrument (Claims and Policy Register), 10 procedures, 8 failure modes, 11 interface contracts, 3 worked examples |

**Verdict / purpose.** Single owner of **ad-creative policy compliance, moderation handling, and claims review** (the three duties the Cross-Reference Ledger row #42 names and no shipped SOP performs). Until now, moderation rejections routed **interim to the PPC Lead with no procedure** (Ledger row #17, interface **I-9**, which retires on this SOP landing), and the **standing company claims rule for bamboo textile copy** ("**viscose derived from bamboo**" or "**rayon derived from bamboo**", **never raw fiber claims**, per PPC SOP Program Gap Register v1.0 Section 3 #42 entry) was enforced on listings, packaging and A+ but on **zero ad surfaces**. Ad headlines and video scripts are where claims violations recur, at **15-20% of mature ad spend on the SB side alone** (Strategic Doctrine v1.0 Section 7 heading). Follows the **SOP-43 v1.0 precedent** (register vocabulary, no closed-vocabulary verdicts), applied a second time.

**Three lanes:**
- **Lane 1 pre-submission claims compliance:** every SB headline, SBV script, SD headline, custom image, Store spotlight copy passes P2 against the Register before submission (caught at $0 spent).
- **Lane 2 moderation lifecycle:** detection of rejections and policy-driven serving stops, root-cause classification into **5 closed classes**, correction, resubmission, **2-rejection escalation trip** (component charter), appeal path.
- **Lane 3 standing policy state:** restricted-term list, keyword-level policy blocks, do-not-target exclusion content (couples to SOP-16), platform & company policy-change response, monthly audit line: **zero live ad assets carrying non-compliant claims**.

Depth note: Gap Register scoped at 3-4 pages under superseded 10-element standard (**conflict C1**); Build Kit v1.0 governs. 10 procedures vs SOP-12 exemplar's 12; not padded.

## 2. Scope & boundaries

**Owns:** Claims and Policy Register; pre-submission checklist; moderation detection, classification, correction, appeal; restricted-list content & rulings; policy-change response; event creative readiness; monthly compliance audit.
**Does not own:** creative execution; targeting; negative placement; SP mechanics; event plans; bulk staging; automation rules; billing; access grants; listing-side claims; setting new claims classes (company rules are set outside PPC).

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold/band/scenario/verdict; carries zero moderation/claims rules (verified vs Sections 3-14); needed controls are AM items per V3 |
| #17-19 SB/SBV/SD playbook | Owns creative execution: format roles, builds, creative precondition gate, S-F2/S-F4 scenario execution, SBV arbitrage workflow. This SOP supplies the P2 claims PASS its gate consumes and takes over its interim moderation route (I-9). Restates zero creative-execution steps |
| #16 PAT & conquest | Owns target opens, rotation, exits. This SOP owns the **policy-restricted portion of exclusion-list content** (P8), answering SOP-16's **AM-6**. #16 decides/executes targeting |
| #29 Negation architecture | Owns negative placement, wall standards, shared-list rules. This SOP rules restricted-term content; #29 places negatives |
| #12 Exact operations | Receives only incident freeze notices on affected targets; on "ENTER SBV ARBITRAGE", a rejected SBV creative suspends the paired step-down until approval; step-down stays SOP-12's |
| #32 Deal & event windows | Owns event plan, arming, ramp, reconciliation. This SOP supplies creative-readiness check at arming (P9) and same-day in-window rejection handling |
| #38 Bulk mechanics | Owns staging, upload, T+1 verification. This SOP reads T+1 report as detection evidence only |
| #37 Automation rules | Owns rule register. **No platform rule may act on an asset inside an open moderation incident**; this SOP feeds exclusion state (SOP-15 P11 pattern) |
| #43 Billing continuity / #46 Access | Account-level billing failures are #43's exclusively. Access to moderation surfaces & role notification inbox provisioned per #46 Access Register; consumes, never grants |
| Catalog, listings, A+ (Brand Management) | Listing-side claims enforcement stays with current owners; listing defects route to BM |
| Legal / company standing rules | Company claims rules set outside PPC; this SOP enforces on ad surfaces; unregistered claims class routes to PPC Lead + Creative seam for ruling |

## 3. Triggers

Same-day lags borrow v4.0 alert standards: Section 3 family **F4 "Listing, Creative & Review State"** (eligibility flips alert same day) and Section 5 **G4** (fix task opens same day). Formal lag table owed (AM-4).

| Trigger | Detecting artifact | Max lag |
|---|---|---|
| New creative submission upstream | Playbook build session presents asset set for P2 | Zero by construction (P2 precondition of submission) |
| Weekly cadence | **T3 CAMPAIGN BOARD** refreshed from SB/SBV/SD bulk (Data Ops lands Raw Pull Pack **Monday 06:00**; workbooks complete by **09:00**, Data Architecture v1.0 Section 12) | Same session: P3 inside Monday cascade |
| Moderation rejection or policy serving stop | Role notification inbox; **T3 C2 State and Eligibility + Reason** columns; **#38 T+1 report** on creative-carrying launches | **Same day** on any asset attached to a live push, armed event window, or arbitrage pairing; **next Monday pass** otherwise (interim pending AM-4) |
| Account-level policy notice/warning | Ads console / seller account policy notification to role inbox | **Same day, to P7, always** |
| Platform or company claims-rule change | Amazon policy update notice; Creative seam or Legal notice | Register update before next submission; live-asset sweep same week (P7) |
| Event window arming | #32 event plan declares armed window into **T2** (SOP-12 P9 arming pattern) | P9 at arming; daily in-window |
| Register ruling request | P2 hold (unregistered class) or P8 referral files ruling request line in register change log | Ruled before affected submission; PPC Lead + Creative seam rule open requests **inside the week at latest** |
| Monthly audit slot | Monthly review slot per v4.0 Section 14 **rule V4** | P10 in monthly slot; #40 assigns calendar day (AM-8) |

## 4. Procedures

### Preconditions (Element 3)
Missing precondition suppresses dependent procedure class and is recorded (G8 pattern).
| Precondition (manifest ID) | Requirement / observable / if missing |
|---|---|
| **A2 Deployment state** | T3 C2 State current from this week's SB/SBV/SD bulk join; T7 MANIFEST row A2 PRESENT with this Monday's date. Missing: P3 runs on inbox only; degraded read recorded |
| **A7 Eligibility** | Eligibility + Reason current per campaign in T3 C2; T7 row A7 PRESENT this week. Missing: inbox + console spot-read fallback |
| Claims and Policy Register current | Version-stamped; last-review date inside monthly cycle; header version cell & review date. Missing/stale: **P2 cannot issue PASS; submissions hold** (fail-safe). No Catalog manifest ID yet (AM-9) |
| Access provisioned (#46) | Executing role has ads-console access incl. campaign manager and role notification inbox; #46 Access Register filtered view shows role row live for **both entity accounts** |
| Event-plan visibility (#32) | Confirmed window dates entered into T2; armed-window record present for any product with event creative. Missing: P9 reports to #32 owner; arming decision #32's |
| Gates in force | **G4**: ineligible/suppressed ad halts all lever action for target, fix task same day; no bidding/budget/rate judgment on asset in open incident. **G10**: delivery-outage windows flagged are excluded from trend verdicts; observable T5 PRODUCT LOG row with Trend-Exclusion Flag set (P4 step 6) |

### P1. Build & maintain Claims and Policy Register (first build 90 min; weekly upkeep 15 min)
1. One workbook, four tabs, in instrument library beside Command Workbook set: **`Claims_and_Policy_Register_v1_0.xlsx`**; version in header cell (filename only for major versions).
2. **Tab 1 CLAIMS REGISTER** (one row per claim): Claim ID (CL-001 up); Claim text as used (verbatim); **Class** (closed list of 6: fiber-content / performance / pricing-promo / comparative / health-adjacent / certification); Brands and products covered; Approved wording (verbatim); Banned wording (verbatim); Substantiation source + date; Ad surfaces where live (SB headline / SBV script / SD headline / custom image / Store spotlight); **Status** (4: APPROVED / RESTRICTED / BANNED / PENDING-SUBSTANTIATION); Review date; Owner.
3. **Seed CL-001**: approved "viscose derived from bamboo" and "rayon derived from bamboo"; banned: any raw-fiber claim incl. "**bamboo fiber**", "**100% bamboo**", "**bamboo fabric**" used as fiber content; class fiber-content; APPROVED for two approved strings, BANNED for raw-fiber strings; all five surfaces. Never edited without Creative seam + PPC Lead ruling.
4. Performance class: every cooling, temperature, sleep-quality claim enters with substantiation source or as PENDING-SUBSTANTIATION; PENDING never ships.
5. Pricing-promo: discount & deal claims legal only inside a **platform-confirmed deal window** (P9).
6. Comparative: empty class with standing rule row: no comparative claim or competitor naming without named PPC Lead + Creative seam ruling on its own row.
7. Certification & health-adjacent: certification (fabric standard, safety mark) carries certificate reference and **expiry date**; lapsed certificate flips row to BANNED on expiry mechanically. Health-adjacent sleep claims follow performance rules with Creative seam ruling mandatory on first registration.
8. **Tab 2 SUBMISSION LOG** (append-only, one row per P2 run): Date; Asset ID; Campaign name per naming convention; Surfaces; Claim IDs touched; Checker role; Result PASS/RETURNED; Returned-for Claim ID.
9. **Tab 3 MODERATION INCIDENTS** (append-only): Incident ID (MI-001 up); Date; Asset; Campaign; Rejection reason verbatim; Root-cause class (P4); Rejection count on this asset; State (OPEN / CORRECTED / APPEALED / CLOSED); Case ID; T5 row link; Closure date.
10. **Tab 4 RESTRICTED LIST**: restricted copy terms; keyword-level policy blocks; do-not-target ASIN exclusions (siblings and declared partner ASINs, Gap Register fold-in to #16); each row with basis, date, receiving SOP (#29 or #16) and receipt date.
11. Weekly upkeep inside P3: review dates due confirmed or re-ruled; every change writes change-log line (date, row, prior, new, ruler role).
12. **Register upstream of every asset**: wording lands in register first, assets second (design-rule-2 pattern, Data Architecture v1.0 Section 2).

### P2. Pre-submission claims checklist (10-20 min per submission set)
1. Trigger: any playbook build/edit creating or changing creative text/imagery (SB headline, SBV script & on-screen text, SD headline, custom image overlay text, Store spotlight copy).
2. Inventory every text element: headline strings, script lines, image overlay text, display URLs to Store pages.
3. **Exact-string scan** vs Tab 1 banned wording. Hit -> RETURNED with Claim ID; back to Creative seam; **no partial passes on a set that shares a campaign**.
4. **Fiber-content check** on every bamboo-range asset regardless of scan: copy states one of two approved wordings wherever fiber content stated or implied; imagery implying raw-fiber content (bamboo stalks as fabric source) -> Creative seam ruling, asset holds.
5. **Claims-class walk** decision tree:
   - Matches APPROVED row -> pass element.
   - Matches BANNED/RESTRICTED -> RETURNED, cite row.
   - Performance claim, no row -> enter PENDING-SUBSTANTIATION; RETURNED until substantiated & APPROVED.
   - Pricing-promo -> pass only when P9 confirms platform-confirmed deal window covering flight dates; else RETURNED.
   - Comparative / competitor naming -> RETURNED to Restricted List ruling path.
   - Fiber-content, health-adjacent, or certification claim with no row -> hold; open register ruling (Creative seam + PPC Lead); never pass by judgment.
   - Descriptive non-claim text (color, size, set count) -> pass; register note only when checker had to think (signals class ruling owed).
6. Write SUBMISSION LOG row. PASS releases to playbook submission; RETURNED names failing Claim ID, no submit.
7. Per submission event, not per week: asset edited after PASS re-runs P2 in full.

### P3. Weekly moderation status pass, Monday cascade (15 min clean week)
1. After workbook refresh (by 09:00) and after T0/T1 read (cascade order).
2. T3 CAMPAIGN BOARD, filter Type SB, SBV, SD; read C2 **State** and **Eligibility + Reason**.
3. Flag moderation states (in review, rejected) or eligibility reason naming policy cause. Cross-check role inbox since last pass.
4. **Console verification** on every flagged row, per entity account & format: ads console -> Sponsored Brands (or Sponsored Display) via campaign-type filter -> campaign -> **Ads view** -> per-creative status & reason. SBV status on video creative entry; SD on ad entry. **Console is authoritative**; bulk is last pull; disagreement -> console wins.
5. Check console **notification center (the bell)** and **account health / policy notices** on both entity accounts; notice found here but not in inbox = **I-2 routing defect** logged same day.
6. Every rejected/policy-stopped asset opens P4 same session. Asset in review since before prior pass -> status check via case path if push- or window-coupled; log line otherwise.
7. Confirm closure evidence for CORRECTED incidents: T3 State delivering, or #38 T+1 report confirming corrected launch.
8. Run register upkeep (P1 step 11 - text says "step 9").
9. Write pass line to SUBMISSION LOG: date, rows read, incidents opened, incidents closed. Zero-incident week still logs (SOP-12 P9 deviation-log convention).

### P4. Rejection intake, root-cause classification, routing (20-40 min per incident)
1. Open MODERATION INCIDENTS row: reason verbatim, asset, campaign, timestamp, rejection count on asset (Tab 3 exact asset match). Capture from fuller source (console per-creative status detail usually has reason string and policy area name; mail sometimes has policy link); record both. **Screenshot console detail into incident folder named by Incident ID** (rejection text not exportable).
2. **Check trip first:** rejection count **2 on one asset -> P6** before further correction (charter; AM-3).
3. Classify root cause (closed list of 5):
   - **(a) Claims content** (claim, superlative, health/safety statement, restricted language) -> P5.
   - **(b) Creative-technical** (specs, resolution, logo, text-over-image ratio, video length or audio) -> Creative seam fix; this SOP tracks and re-runs P2 before resubmission.
   - **(c) Landing mismatch** (ad conflicts with Store/detail page) -> page owner via Brand Management; incident OPEN until aligned; which changes is page owner's call with PPC Lead.
   - **(d) Policy category** (product/format restricted as category) -> PPC Lead: contest via P6 with written policy text, or retire asset class and record in register.
   - **(e) Unclear/generic** -> one clarification request via case path, then classify; unanswered defaults to **class (a)** (conservative).
4. State OPEN; **daily check cadence** (inbox and console status daily while any incident OPEN).
5. **Freeze notice:** affected target takes **no lever action while OPEN** (G4); notify owning SOP operator same day on push- or arbitrage-coupled targets.
6. **Attribution write:** on any delivery-affecting incident, write **T5 PRODUCT LOG** row same day, event type **"eligibility flip"** (closed list of 8, Data Architecture v1.0 Section 9), detail naming moderation event, **Trend-Exclusion Flag set**. Lets attribution rules (v4.0 Section 4 "Layer X" **X9**; Section 7 **D5**) see the stop. Dedicated type owed (AM-6).

### P5. Claims correction & resubmission (30-60 min per incident)
1. Correct copy strictly to APPROVED register wording. No approved wording -> Creative seam drafts, PPC Lead rules, written to register, then to asset.
2. Re-run P2 in full; new SUBMISSION LOG row referencing incident ID.
3. Resubmit through owning playbook build procedure (Ledger row #17). State CORRECTED.
4. Verify on daily check: approval, T3 State delivering, and on relaunch-class corrections #38 T+1 report.
5. Close: CLOSED with closure date; closure line notes register change produced.
6. Resubmission rejected -> P4 step 2 (second rejection, trip fires).

### P6. Appeal & case escalation (30 min to open; daily checks)
1. Eligible if any: 2-rejection trip fired; class (e) after classification; PPC Lead judges rejection wrong vs written policy. **Unchanged asset never resubmitted a second time without a case** (F2).
2. Support case carries: asset ID & campaign; rejection reason verbatim; policy section quoted; register Claim ID with substantiation source & date. Can't cite substantiation -> not opened, back to P5.
3. Record Case ID; state APPEALED; daily checks.
4. Unresolved at next weekly pass -> PPC Lead with history; touching armed event window -> same day.
5. Outcome to register: upheld -> disputed wording **BANNED account-wide** with case as basis; overturned -> ruling recorded as precedent on claim row.

### P7. Policy & claims rule-change response (30-90 min per change)
1. Intake: branch 1 platform policy update / account-level notice to role inbox; branch 2 Creative seam/Legal changes company rule. Same-day; account-level warning read by PPC Lead the day it arrives, no exception.
2. Assess touched classes/rows; draft edits; PPC Lead rules with Creative seam.
3. Update register first, change-log line naming source notice.
4. **Live-asset sweep same week**: pull live SB/SBV/SD asset inventory; check every asset vs changed rows only; hits open P4-class incidents with correction staged same day.
5. Route restricted-list consequences per P8.
6. Log in **T6 DECISION LOG** with sweep result and review date; account-level notice also writes T5 row.

### P8. Restricted-term & exclusion-list maintenance (20 min monthly; 60 min quarterly)
1. Owns content & ruling of Tab 4; executes none in campaign surfaces. Three routes with receipts:
   - Restricted copy terms: enforced by P2 exact-string scan.
   - Keyword-level policy blocks -> **#29** same week (shared-list rules); receipt date recorded.
   - Do-not-target ASIN exclusions (siblings & declared partner ASINs never conquested) -> **#16** same week; #16 screens opens; receipt recorded. Resolves SOP-16 AM-6: owner is this SOP, PPC Lead ruling.
2. Additions from: P2 comparative returns; P4 class (d) retirements; P7 change events; #16/#29 referrals; partner & sibling declarations from #33 family records.
3. Quarterly (V4 quarterly class): walk full list; every row re-based or retired; list change without #16/#29 receipt inside the week = F8.
4. Every change writes change-log line; live target/term affected -> T6 entry with routing receipt.

### P9. Event-window creative readiness & in-window handling (20 min at arming; 10 min daily)
1. At #32 arming: pull plan's creative-carrying line items; verify each asset APPROVED in register, live-eligible in T3 C2, and for pricing-promo that deal is platform-confirmed for exact flight dates. Report to #32 owner (I-8); arming decision #32's.
2. Pricing-promo assets submit only after deal platform-confirmed (WE-2 failure; standing rule row after incident class first fires).
3. Inside window plus **14-day pre and post posture windows** (v4.0 Section 3 family **F2** Event posture row): moderation checks daily; any rejection same-day P4 regardless of coupling.
4. In-window rejection that can't be corrected/re-approved before flight date -> event plan fallback same day (fallback owned by playbook & #32); decision taken **day 0**.
5. No new claims wording enters register during armed window except via incident (**S-E1** no-new-experiments posture, v4.0 Section 8.12 Event-Mode Scenarios S-E1 to S-E6).

### P10. Monthly claims compliance audit (45-75 min)
1. Monthly slot (V4 monthly class; day assigned by #40, AM-8).
2. Pull live-asset inventory: T3 filtered SB/SBV/SD with State delivering, plus Store spotlight & custom-image asset list from Creative seam ("the asset is the unit").
3. Map every claim-bearing element of every live asset to an APPROVED row. Audit line: **zero live ad assets carrying non-compliant claims**. Miss -> P4-class incident, correction same day, even if platform approved (F3).
4. Cross-check SUBMISSION LOG vs inventory: live asset with no P2 row = **F4** -> retroactive P2 same day + root cause naming skipped build step.
5. Register hygiene: review dates current, PENDING rows aged out or resolved, incident rows terminal.
6. Write audit result line to register and **monthly compliance note to Account Rollup A4** beside playbook's format rollup (Data Architecture v1.0 Section 11). Repeated misses on one source -> PPC Lead.

## 5. Rules, thresholds & numbers

### 5.1 v4.0 references
| ID | Meaning as described |
|---|---|
| V3 | Rule amendment protocol (needed rules logged as AM items) |
| V4 | Monthly and quarterly review classes (P10 monthly, P8 quarterly) |
| F4 (Section 3 family) | "Listing, Creative & Review State": eligibility flips alert same day |
| F2 (Section 3 family) | Event posture row: 14-day pre and post posture windows |
| G4 | Ineligible/suppressed ad halts all lever action for target; fix task same day |
| G8 | Packet-completeness pattern (missing precondition suppresses dependent class) |
| G10 | Delivery-outage windows excluded from trend verdicts |
| X9 (Section 4 Layer X), D5 (Section 7) | Attribution rules that consume T5 event rows |
| S-F2, S-F4 (Section 8.10 Brand-Format Scenarios S-F1 to S-F8) | S-F2 re-creative branch; S-F4 creative refresh; replacement creative passes P2 |
| S-E1 (Section 8.12 Event-Mode Scenarios S-E1 to S-E6) | No-new-experiments posture |
| 13.1 Closed Verdict Vocabulary | Nothing issued from it here |

### 5.2 Closed-vocabulary verdicts touching scope (not originated here)
| Verdict (KDR v3.0) | Interaction |
|---|---|
| "PAUSED-PENDING (REASON + RE-ENTRY)" | Owning SOP issues; this SOP supplies reason string and re-entry criterion (approval landed and delivery confirmed) |
| "ENTER SBV ARBITRAGE" | Rejected SBV creative suspends entry; SP step-down doesn't execute against dark SBV surface |
| S-F2 / S-F4 | Replacement creative through P2 |

### 5.3 Register vocabularies (not closed-vocabulary; AM-2)
- Claim classes (6): fiber-content, performance, pricing-promo, comparative, health-adjacent, certification
- Register status (4): APPROVED, RESTRICTED, BANNED, PENDING-SUBSTANTIATION
- Incident states (4): OPEN, CORRECTED, APPEALED, CLOSED
- Checklist results: PASS, RETURNED
- Root-cause classes (5): (a) claims content, (b) creative-technical, (c) landing mismatch, (d) policy category, (e) unclear/generic
- Ad surfaces (5): SB headline, SBV script, SD headline, custom image, Store spotlight

### 5.4 Numbers
| Item | Value |
|---|---|
| Escalation trip | 2 rejections on one asset (charter, AM-3) |
| SB claims-violation recurrence | 15-20% of mature ad spend on SB side (Strategic Doctrine v1.0 Section 7) |
| Weekly feed | Raw Pull Pack Monday 06:00; workbooks by 09:00 |
| Event posture windows | 14 days pre and post |
| Ruling request deadline | Inside the week at latest |
| T5 event-type list | Closed list of 8; interim type "eligibility flip" |
| Durations | P1 90 min first / 15 weekly; P2 10-20; P3 15; P4 20-40; P5 30-60; P6 30 to open; P7 30-90; P8 20 monthly / 60 quarterly; P9 20 at arming / 10 daily; P10 45-75 |
| Version governance review | After closure of first 5 live moderation incidents |
| Interim fallback (I-5) | No incident response inside 1 day -> PPC Lead direct route resumes |
| #44 due | 2026-09-25; #40 due 2026-09-18 (per AM-8) |

### 5.5 Failure modes
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Rejection undetected | T3 C2 scan; daily inbox during incidents; spend flat at zero on format row | P3/P4 same session (structural: I-9 interim route existed because no detection owner) |
| F2 | Unchanged resubmission loop | SUBMISSION LOG same asset identical wording after rejection | Block; P6 |
| F3 | Approved-but-non-compliant claim live | P10 audit; P7 sweep | Correct same day; platform approval never overrides company rule (FTC-anchored bamboo rule) |
| F4 | Register bypass (no P2 row on live asset) | P10 cross-check | Retroactive P2 same day; recurring source -> PPC Lead |
| F5 | Event asset rejected in armed window | P9 daily check; #32 pacing anomaly | Same-day P4; fallback same day; G10 exclusion |
| F6 | Silent delivery stop misread as performance | Format row WoW spend collapse with no T5 row | Write T5 row; mark reads excluded (X9/D5) |
| F7 | Rule change not propagated | Register change-log date with no same-week sweep line | Sweep immediately; T6 entry incomplete until sweep line |
| F8 | Restricted-list drift | Quarterly P8 diff; no #16/#29 receipt inside week | Re-route with receipts same week |
Escalation: same failure twice in consecutive cycles on same scope -> PPC Lead; any account-level notice, any F5, any fired trip -> same day. Alarm routing: F1/F5 and trips same day to PPC Lead; F2/F6/F7 operator queue same session; F3/F4/F8 weekly worklist with monthly escalation on recurrence.

## 6. Data inputs required

- **T3 CAMPAIGN BOARD** (Command Workbook): Type filter SB/SBV/SD; **C2 State**; **C2 Eligibility + Reason** (from SB/SBV/SD bulk + **RAS sheets**, Monday 06:00 feed)
- **SB/SBV/SD bulk file** (weekly Raw Pull Pack)
- **T7 MANIFEST** rows **A2** (Deployment state) and **A7** (Eligibility)
- **T2** armed-window dates (from #32)
- **T5 PRODUCT LOG** (write and read; Trend-Exclusion Flag)
- **T6 DECISION LOG** (write)
- **T0/T1** (read first in cascade)
- **Role notification inbox** (PPC Manager role inbox; moderation & policy mail)
- **Ads console**: Sponsored Brands / Sponsored Display campaign Ads view per-creative status & reason; SBV video creative entry; SD ad entry; notification center (bell); account health / policy notices; both entity accounts
- **#38 T+1 verification report** (creative-carrying launches)
- **Claims_and_Policy_Register_v1_0.xlsx**: Tabs CLAIMS REGISTER, SUBMISSION LOG, MODERATION INCIDENTS, RESTRICTED LIST, change log
- **#32 event plan** (creative-carrying line items, flight dates, armed windows, fallbacks); platform deal confirmation status
- **#46 Access Register** filtered view
- **Creative seam asset list**: Store spotlight and custom-image assets; asset text, imagery, SBV scripts & on-screen text, overlay text, display URLs
- **#33 family records** (partner and sibling declarations)
- Amazon policy update notices; Legal/Creative seam company rule notices
- Substantiation sources; certificate references & expiry dates
- Support case responses (Case IDs)
- Incident folder with console screenshots
- **Account Rollup A4** (playbook format rollup, write compliance note)
- KDR Template v3.0 Bands & Verdicts Reference

## 7. Outputs / artifacts

All register tabs/logs append-only and permanent.
| Event | Artifacts | Storage / consumer |
|---|---|---|
| P1 | Claims_and_Policy_Register_v1_0.xlsx (4 tabs, version-stamped, change-logged) | Instrument library beside Command Workbook; playbook precondition gate, #16, #29, P10, #44 |
| P2 | SUBMISSION LOG rows (PASS/RETURNED with Claim IDs) | Tab 2; P10 cross-check, playbook build session |
| P3 | Weekly pass line (date, rows read, opened, closed) | SUBMISSION LOG |
| P3-P6 | MODERATION INCIDENTS rows (class, states, case IDs, closure notes); T5 rows; freeze notices; incident screenshot folders; support cases | Tab 3 & T5; X9/D5 attribution, weekly pass of affected SOPs |
| P7 | Change-log lines; sweep result; T6 entry with review date; T5 row on account-level notices | Register & T6; monthly review, v4.1 amendment owner |
| P8 | Tab 4 rows with basis & receipt dates; T6 entries on live-target effects | #29, #16 |
| P9/P10 | Arming check result to #32; monthly audit line (zero-or-miss count); monthly compliance note to Account Rollup A4 | #32, monthly structure review |
| Alarms | F1-F8 with evidence lines | Per routing |

**Appendix B evidence-line format:** `[Incident or F-ID] | [entity account] | [campaign name per convention] | [asset ID] | [signal: column or source + value] | [register or rule reference] | [state] | [next action + date]`. Missing register reference = incomplete, doesn't close.
Worked instance: `MI-014 | Ecotero | EBS4-SBV-bamboo sheets king-HSV-Video-Rank-B4-KING-WHITE | VID-2231 | Console creative status: Rejected, claims policy | CL-001 BANNED wording | CORRECTED | verify approval, daily check, close on delivery.`

## 8. Decision rights

- Authority Matrix v2.0 has **no #42 row** (AM-5). Interim via playbook I-9 route and **Standing Rule 5** (vacancy rule).
- **PPC Lead decides:** register status rulings (APPROVED/BANNED), appeal filings, class (d) retire-or-contest, every account-level notice response; with Creative seam on wording rulings, CL-001 edits, comparative claims, unregistered classes.
- **Operators execute** checklist (P2) and pass (P3) per "Structure creation (all SOPs)" row (operator E, Lead D on scope).
- **Event-window fallbacks** per "Event plans (#32)" row: PPC Lead decides with deals owner; launch/CA operator and PPC Manager execute; BM owner reviews (Standing Rule 3: daily huddle, review not veto).
- Incident classification per "Weekly verdicts (established US)" huddle convention.
- Page owner (BM) decides landing alignment with PPC Lead; Creative seam fixes technical assets; #32 owns arming; #16/#29 execute exclusions/negatives.
- Automatable: P2 exact-string scan, two class trees, P10 diff, P8 receipt-date check; skill drafts only, PASS blocked pending human release on any RETURNED history.
- Ramp: Week 1 memorize 6 classes, 4 statuses, 5 root causes, CL-001 wordings; observe P3. Week 2 supervised P2, P3, one P4 classification, draft P6 package. Week 4 unsupervised P2-P4, one full P10. Rulings/appeals/account notices stay with Lead.

## 9. Account-specific facts

- Two entity accounts (Inspiratek & Ecotero; "both entity accounts"); evidence-line example uses **Ecotero**.
- Bamboo range products (bamboo sheets; KING, WHITE variants). Example campaign: **EBS4-SBV-bamboo sheets king-HSV-Video-Rank-B4-KING-WHITE**, asset **VID-2231**, incident **MI-014**.
- Bamboo claim rule enforced on listings/packaging/A+ but zero ad surfaces prior to this SOP.
- WE fictional base: AOV $80.00, contribution $28.00/order, BE ACOS 35.0%, Target 17.5%, Max Acc 26.3%; E6 values SP exact CPC $2.10 at CVR 5.0%; SBV CPC $0.95 at CVR 3.2%.
- **WE-1:** SBV overlay "100% bamboo softness" rejected Tue 14:20; SBV daily budget $35.00; detected Wed 09:00 (18.7h); corrected to "viscose derived from bamboo"; resubmitted Wed 11:00; approved Fri 09:30 (46.5h review). Dark 67.17h = 2.80 days; undeployed $98.00; 103.2 clicks, 3.30 orders forgone; CPO SBV $29.69 vs SP $42.00; premium $12.31/order; $40.62 window; **$14.51/dark day**; weekly-pass counterfactual 5.78 days -> $83.85.
- **WE-2:** 2-day Fri-Sat deal window; SB headline "Sale: 30% off"; rejection 1 Monday class (b) logo; rejection 2 Wed 10:00 pricing (deal not platform-confirmed); case Wed 11:00; fallback deadline Thu 17:00; SB budget $600/day x 2 = $1,200; SB CPC $1.10, event CVR 6.5% vs 5.2% base; 1,090.9 clicks, 70.9 orders, $1,985.20 contribution, **$785.20 net at risk**; deal synced Thu 14:00, case cleared 16:00, Friday 06:00 re-check APPROVED.
- **WE-3:** SD headline "cools you 3x faster" delivering 24 days, no register row, skipped P2; 24 x $22.00 = $528.00 spend; CPC $1.15 -> 459.1 clicks; CVR 4.0% -> 18.4 orders; $515.20 contribution.

## 10. Open items

| ID | Amendment item |
|---|---|
| AM-1 | v4.0 has zero moderation/ad-policy/claims rules; whole rule class owed (rejection-response requirements, appeal limits, incident severity classes, compliance gate's place in gate order) |
| AM-2 | Register vocabulary admission to closed vocabulary or formal standing exception (SOP-43 AM-2 pattern, second instance) |
| AM-3 | 2-rejection trip: charter value from Gap Register v1.0 Section 3 #42, pending v4.0 admission |
| AM-4 | Element 2 lag table needs v4.0 basis (borrows F4/G4 same-day) |
| AM-5 | Authority Matrix v2.0 no #42 row |
| AM-6 | T5 closed event-type list of 8 has no moderation/policy type; interim "eligibility flip" (SOP-43 billing-outage pattern, second instance) |
| AM-7 | Fold-in proposal to #32: arming-checklist line holding arming pending I-8 result |
| AM-8 | Calendar slots for P10 monthly and P8 quarterly belong to #40 (due 2026-09-18) |
| AM-9 | Register owed a Definition Register entry under #1 |
| AM-10 | Ownership resolution: this SOP takes policy-restricted exclusion-list content, answering SOP-16 AM-6; SOP-16's row not edited; reported for Ledger close-out |

**Conflicts:** C1 (Gap Register 3-4 page scope under superseded 10-element standard).

**Interface contracts:**
| ID | Sender -> receiver: artifact | Timing | Non-arrival |
|---|---|---|---|
| I-1 | Data Ops -> SOP: SB/SBV/SD bulk + RAS state into T3 C2 | Mon 06:00; workbook 09:00 | P3 on inbox alone; T7 A2/A7 stale; detection claim downgraded |
| I-2 | Platform -> PPC Manager role inbox | Continuous | Personal-inbox landing = F1 standing condition; re-route via #46 |
| I-3 | Creative seam -> SOP: asset text/imagery | Before submission | Submission does not proceed |
| I-4 | SOP -> playbook: P2 result | Same session | Playbook holds launch; proceeding anyway = F4 |
| I-5 | SOP -> playbook: P4-P6 handling replacing interim route | On landing; I-9 retires | No response in 1 day -> PPC Lead direct; F1 line |
| I-6 | SOP -> #29: policy blocks & restricted terms | Same week with receipt | Walls stale; #29 monthly wall audit backstop; F8 |
| I-7 | SOP -> #16: do-not-target exclusions | Same week with receipt | #16 opens unscreened (S-C1 open test doesn't check policy exclusions); F8 |
| I-8 | SOP -> #32: creative-readiness at arming | Arming; daily in-window | Arms on unverified creative (WE-2 exposure); AM-7 |
| I-9 | SOP -> T5 PRODUCT LOG | Same day | F6; trend verdicts polluted until backfill |
| I-10 | SOP -> #44: Element 11 content | By 2026-09-25 | #44 builds certification blind |
| I-11 | SOP -> Account Rollup A4: compliance note | Monthly | No compliance line; backfills next P10 |

**Review triggers:** v4.0 increment admitting moderation/claims rules; Amazon ads policy change touching a register class; company claims rule change; #17-19 playbook version increment (re-validate I-3, I-4, I-5); Authority Matrix #42 row; closure of first 5 live incidents (review P4 class list).

**Text anomalies:** P3 step 8 says "Run the P1 step 9 register upkeep" but upkeep is P1 step 11; P5 step 1 cites "P1 step 10 order" for register-first rule (stated at P1 step 12); final footer reads "Page 10 of 10" on page 14 of 14.

**Named documents not present:** Master PPC Decision Criteria System v4.0; KDR Template v3.0; PPC SOP Program Gap Register v1.0; Cross-Reference Ledger; Master PPC Data Architecture v1.0; PPC Authority Matrix v2.0; Strategic Doctrine v1.0 Sections 7-8; Economics Worked-Example Set v1.0; SOP-16, SOP-17-19 playbook, SOP-15 P11, SOP-43.
