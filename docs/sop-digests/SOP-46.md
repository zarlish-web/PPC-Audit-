# SOP-46 Digest: Access and Permissions Operations

Source: `PPC_SOP_46_Access_and_Permissions_v1_0.pdf`. Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-46: Access and Permissions Operations (PPC Department, Operating SOP, Component #46) |
| Version | 1.0 (first build, no prior version; nothing superseded) |
| Date | 2026-07-28 (register component #46 due 2026-08-14) |
| Owner | PPC Lead |
| Authority | Decision rights live in PPC Authority Matrix v2.0 (#3); this SOP provisions the access that executes them. Thresholds in v4.0 only; Section 5.1 states the component has **no v4.0 threshold basis** |
| Content | 12 procedures (P1-P12), 10 failure modes (F1-F10), worked examples (text says 2; four are present: WE-1 to WE-4) |

**Verdict / purpose.** **Access is a provisioned state, never an accumulated one.** Every credential across the **10 platform surfaces of both entity accounts** exists as **one row in the Access Register** carrying a **role, an Authority Matrix basis, a permission class, a grant record, and a deprovision path**; a credential found live without its row is **suspended on discovery**, not tolerated. Account deploys **$6,000-8,000/day** of spend authority through these credentials (Data Architecture v1.0 Section 1). This SOP makes the Matrix physically true on platforms: a login can do exactly what Matrix letters say, nothing above, nothing after the person leaves. Governs: Access Register; provisioning on role fill; deprovisioning on exit/vacancy; scope changes on Matrix re-issue; platform addition/retirement; service & feed credentials; automation platform access; workbook layer access; external party access; unrecognized-actor response; emergency access under vacancy rule; weekly reconciliation diff.

## 2. Scope & boundaries

| Adjacent | Seam |
|---|---|
| #3 Authority Matrix | Decision rights themselves; SOP implements, never re-decides (permission class = translation of a Matrix letter) |
| #43 Billing continuity | Billing method continuity exclusively #43's; SOP records who holds billing-admin access; continuity procedure and 2026-08-01 failure response are #43's |
| #37 Automation rules | Rule change control & register #37's; SOP grants/revokes the platform seat, #37 governs what the seat does |
| #38 Bulk mechanics | Staging, upload, T+1 attribution #38's; SOP consumes attribution report as detection feed (P10) |
| #44 Onboarding & certification | Due 2026-09-25; consumes Element 11 |
| #39 Feed definitions & manifest | SOP keeps credentials behind feeds alive; reads T7 statuses as failure observable |
| #4 | Weekly calendar slots |
| #40 | Above-weekly calendar (not yet landed) |
| BM (Data Hub) | Hub is BM's single source of truth; PPC READ only |

### 1.1 Platform Inventory
| # | Surface | Entity scope | Access controls | Feed kept alive (T7 ID) |
|---|---|---|---|---|
| 1 | Amazon Ads console, US | **Ecotero LLC** | Campaign deploy, bid, budget, billing-admin (billing per #43) | A2, A3, A7, A8, B6 |
| 2 | Amazon Ads console, US | **Inspiratek LLC** | Same as row 1 | A2, A3, A7, A8, B6 |
| 3 | Amazon Ads console, CA | Per entity | Canada delta scope (**#34, held at v1.0-structure**) | CA parameter column pending (**Ledger D7**) |
| 4 | Seller Central, US | Per entity | SQP export, STIS, bulk operations, eligibility reads | B4, B11, D3 |
| 5 | **ScaleInsights** | Both | Automation rules (#37 governs rules; this SOP the seat) | T6 conflict flags (ScaleInsights change log) |
| 6 | **DataRova** | Both | Rank series, DSTR, top-ASIN pulls | D9 |
| 7 | **Keepa** | Both | Competitor depth pull | D8 |
| 8 | **SellerBoard** | Per entity | Financial source of truth; margin true-up reads | T0 zone B economics, D1 inputs |
| 9 | **BM Data Hub v2.0** | Both | **READ ONLY for every PPC role, without exception** (Data Architecture rule 2: PPC reads, PPC never edits) | B1, B3, C1-C8 |
| 10 | Workbook layer (Drive): Command Workbooks, Account Rollup, Ledger, this Register | Both | The decision surface; T6 append rights are the deploy log | B5, B10, D6, D7 |

### 1.2 Permission classes (five, closed; exactly one per platform per row)
- **OWNER**: can grant/revoke access for others (account root and PPC Lead per platform)
- **WRITE**: can deploy (bids, budgets, states, rule edits)
- **STAGE**: can draft & stage change sets, not deploy (#38 staging path)
- **READ**: view & export only
- **NONE**: explicit zero, recorded so absence is a decision
**Translation rule:** D -> WRITE (+ OWNER where row is PPC Lead); E -> WRITE on assigned scope, STAGE outside it; R and I -> READ; blank -> NONE. If mapping and Matrix disagree, **Matrix governs**, register row is the defect (Matrix standing rule 3 routes disagreements up).

## 3. Triggers

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Role fill (new operator/manager) | Authority Matrix re-issue or Transition Brief scope-stack update naming role | Before first credentialed working session; **0 platform actions pre-provisioning** | P2 |
| Role exit or vacancy | Org notice; Matrix standing rule 5 activating | **Same working session** as notice (interim; AM-3) | P3, P11 |
| Org change touching Matrix roles | Matrix re-issue (required within **1 week**, Matrix Section 2 rule 6) | Inside same 1-week window | P4 |
| New platform/tool adoption | Adoption decision record; T7 manifest row naming new source feed | Before first production use; register rows precede logins | P5 |
| Feed credential failure | T7 status flips to MISSING at **Monday 09:00 packet read** on a feed previously PRESENT | Same day; credential checked before feed debugged | P6 |
| Unrecognized actor | **#38 T+1 attribution report** carrying change no session and no rule claims (#38 unlogged-edit class; SOP-12 F10 console-edit detection) | Same day (SOP-12 F10 standard) | P10 |
| Automation seat event | **#37 weekly diff** finds rule owned by credential not in register | Same day; #37 F1 suspension carries seat question here | P7 |
| External engagement start/end | Engagement record (agency, contractor, auditor) | Start: before first login. End: same working session as end date | P9 |
| Weekly reconciliation | Monday cycle slot (#4; until #40 sets above-weekly calendar) | Inside Monday slot after 09:00 packet read | P1, P12 |
| Billing continuity event | #43 procedure activating (credit-card ad billing ends 2026-08-01) | Immediate; register answers "who holds billing-admin" in **under 5 minutes** | I-4 |

## 4. Procedures

### Preconditions & gates
| Gate | Requirement | ID | Observable |
|---|---|---|---|
| **AC-1 Matrix currency** | Matrix in hand is current; no org change post-dates its version date | #3, `PPC_Authority_Matrix_v2_0.pdf` | Matrix version date on/after latest org-change date; older than an org change by **>7 days** fails; P4 fires first |
| **AC-2 Register present** | Register at current version with **0 unresolved diff findings older than 1 cycle** | `PPC_Access_Register` | Register version cell dated within current cycle; open-findings count on DIFF sheet reads 0 carried rows |
| **AC-3 Feed credential proof** | Credentials behind Monday pull alive | **T7 rows A2, A7, B6, B11, D8, D9** (Data Architecture Section 9) | Each reads PRESENT or PARTIAL for a feed-content reason; MISSING with note naming login/token/permission failure = fail -> P6 |
| **AC-4 Scope stack available** | Operator scope assignments readable | Transition Brief v1.2 scope stack (Matrix rule 4) | Rows touched (PAT/conquest, D5/auto, incrementality) resolve to exactly one named role each |
| **AC-5 Downstream honesty** | Access failure breaking a feed is stated by analysis layer | v4.0 Section 5 gate **G8** | Affected verdict classes in T7 "Verdict Classes Blocked While Missing"; cycle header carries reduced completeness score |

### P1. Register maintenance & weekly access diff (20-35 min/week)
1. Open each platform's user/permissions page in Section 1.1 order: **Ads console per entity (Administration > Manage users)**; **Seller Central per entity (Settings > User Permissions)**; **ScaleInsights (Account > Team)**; DataRova, Keepa, SellerBoard (Account or Settings > Users); **Drive sharing panel** on each workbook; **Hub sharing panel** (read-only check).
2. Export/transcribe live user list per platform into register **DIFF** sheet: person, email, permission level as platform names it, last-activity date.
3. Diff vs register rows. Three classes: **UNREGISTERED** (live credential, no row: F1, suspend); **DRIFTED** (row exists, platform level ≠ class: F5); **GHOST** (row LIVE, platform shows no such user: correct row to REVOKED with evidence).
4. DRIFTED: **correct platform to register, never register to platform**, unless a P2/P4 record explains platform state (same as #38 workbook-over-bulk-file rule).
5. UNREGISTERED: suspend platform-side same session (lowest permission or remove seat); route to P2 or P3.
6. Write diff report: findings by class, actions, 0-findings weeks recorded (empty diff = passing artifact; SOP-12 P9 convention).

### P2. Provisioning on role fill (60-90 min per person, all platforms)
1. Confirm AC-1, AC-4. Pull role column from Matrix and scope rows from Transition Brief.
2. Translate letters to classes; one register row per platform incl. explicit NONE. **Row written before grant: register precedes login, always.**
3. Apply decision tree for compound/blank cells:
   - D -> WRITE (+ OWNER where PPC Lead on that platform)
   - E: inside Transition Brief scope? YES -> WRITE on executing platforms; NO -> STAGE
   - R or I -> READ
   - Blank / role absent -> NONE
   - Compound ("D, E" / "E, R") -> highest single class justified, split noted in scope-note field (Matrix standing rule 1)
4. **Human confirmation:** every WRITE/OWNER grant confirmed by **PPC Lead** before invitation; grants touching PPC Lead's own access confirmed by **CEO**.
5. Send invitations at mapped level. **Named human accounts only; one person, one email, per platform; no shared logins** (F2).
6. Enable strongest available login protection; record in **MFA column** (or that platform offers none).
7. Verify grant landed (log in with person present, or read user list); write grant date, granted-by, proof note. Grant without landed-proof incomplete.
8. Log in **EVENT** sheet: date, person-role, platforms, classes, Matrix basis cells, confirmed-by.

### P3. Deprovisioning on exit or vacancy (30-45 min, same working session as notice)
1. Vacancy rule activates: departing D -> PPC Lead, E -> PPC Manager (Matrix rule 5); P11 provisions reversions.
2. **Revoke in exposure order, highest spend authority first:** Ads consoles (both entities), ScaleInsights, Seller Central, workbook layer WRITE grants, then read-only tools.
3. **ScaleInsights:** before seat removal, reassign every rule whose owner field names departing credential to receiving role per **#37 P4 change control** (F6).
4. Set every row for person to **REVOKED** with date, revoked-by, per-platform proof. **Rows never deleted** (append-only like T6).
5. Log in EVENT sheet; hand row set to next Monday's P1 diff as verification target.

### P4. Scope change on Matrix re-issue (20-40 min per re-issue)
1. Diff new Matrix vs register's Matrix-basis column cell by cell.
2. Each changed cell -> one row edit (raised, lowered, zeroed). **Lowerings deploy same session; raisings follow P2 step 4 confirmation.**
3. Matrix-version column updates on every touched row.
4. Pending **Completion Directive two-cell edit** in the Matrix (brief controls until it lands) tracked here; when it lands it's a re-issue and P4 runs.

### P5. Platform addition or retirement (30-60 min per platform)
1. Addition: before first production use, platform enters inventory (register **REFERENCE** sheet), permission model mapped to five classes, rows written for every role incl. NONE; only then seats created (P2 steps 4-8).
2. If platform feeds the packet, T7 manifest row created same session (#39 owns definitions); AC-3 list gains row at next version increment.
3. Retirement: all seats revoked (P3 2-5); inventory row RETIRED with date; any T7 row it fed flips to MISSING with retirement named (G8).

### P6. Service & feed credentials (15-30 min per event)
1. Feed credentials (logins, tokens, API keys behind **Raw Pull Pack sheets, SQP export, DataRova, Keepa, SellerBoard, ScaleInsights change log**) are rows of credential type **SERVICE**, owned by **Data Operations** role, scoped to exactly what pull needs (READ where read-only key allowed).
2. On AC-3 fail: check service row first; three usual causes: **expired token, revoked seat, password rotation**; restore and re-run pull same day so Monday 09:00 assembly holds.
3. Service credentials never personal logins; pull under a departing human's seat (F1/F6) converts to SERVICE row same session.
4. Every service row carries a named human owner-role and backup role.

### P7. Automation platform access (15-25 min per event)
1. ScaleInsights WRITE seat = rule-authoring credential; held only by roles whose Matrix row "Automation rules (#37)" reads D or E (**PPC Lead D; incoming operator E, R; PPC Manager E**).
2. #37 weekly diff finds rule owned by unregistered credential: #37 suspends rule (its F1); this SOP suspends seat same day (P1 step 5); records cross-reference.
3. Seat grants/revocations always write a note into the #37 register's owner column path (dangling owner = F6).

### P8. Workbook layer access (15-25 min per event)
1. Drive sharing on Command Workbooks, Account Rollup, Ledger, register follows class mapping: **T2/T3/T4 verdict columns and T6 append rights = WRITE** for PPC Lead and scoped operators; **STAGE = comment-only sharing**; R/I = view-only links.
2. **BM Data Hub: every PPC role READ, permanently**; Hub is single source of truth for its **121+157 fields**; PPC edit grant = F9 on discovery.
3. Register itself: **WRITE for PPC Lead only**; diff drafted by any operator at STAGE (comment), applied by Lead.

### P9. External & agency access (20-30 min per engagement boundary)
1. EXTERNAL credential type (agency, contractor, auditor, platform support with delegated access) carrying **engagement end date at grant**; grant without end date doesn't deploy.
2. **Class ceiling: EXTERNAL caps at STAGE on deploy-capable platforms unless CEO confirms WRITE in writing** (above-envelope authority pattern).
3. On end date P3 runs mechanically; weekly diff flags EXTERNAL past end date still LIVE as F8, same session.

### P10. Unrecognized-actor response (30-60 min per incident)
1. Input: #38 T+1 line no session/#37 rule claims, or SOP-12 F10 console-edit finding. Change itself handled by owning SOP; this answers who could have made it.
2. Pull platform change history; identify acting credential.
3. Decision tree; every branch ends with EVENT entry (credential, branch, evidence):
   - Registered person outside staged path -> not access failure; route to #38/#12 change control; note on row; class review via P4 only if Matrix basis exceeded.
   - Registered person above their class -> DRIFTED; correct platform same session; record how.
   - **Departed person's live credential** -> F1 most dangerous; P3 immediately; root-cause line naming which P3 run skipped the platform.
   - **Unknown credential** -> potential compromise: suspend seat, **rotate account root password with CEO informed same day**, full out-of-cycle P1 sweep.
   - Service credential acting outside scope -> reduce to minimum class, re-key.
4. Second incident from same credential class **in 4 cycles** -> PPC Lead with both records.

### P11. Emergency access under vacancy rule (20-30 min per activation)
1. Trigger: vacancy (P3) or incapacity where D/E holder unavailable and a dated obligation (Monday cycle, funded push pacing, event window) lands before refill.
2. Provision rule 5 reversion (D -> PPC Lead, E -> PPC Manager) per P2 mechanics; rows marked **EMERGENCY** with the vacancy they cover.
3. EMERGENCY rows end on refill; weekly diff flags refilled-vacancy EMERGENCY row as F10, revoked same session.
4. **No other emergency path; nobody borrows a login, ever** (destroys #38 attribution & V5 owner-level scoring).

### P12. Reconciliation artifact & escalation (10-15 min/week)
1. Write weekly diff report into DIFF sheet with cycle date.
2. Roll counters: rows LIVE / SUSPENDED / REVOKED, findings by class, days-open. **Finding carried past 1 cycle breaches AC-2**, escalates to PPC Lead.
3. Until #40: **the 4th diff of each month doubles as deep pass** (every platform's permission detail, not just user list) (AM-3).

## 5. Rules, thresholds & numbers

### 5.1 Threshold basis
v4.0 contains **no access, credential, provisioning or deprovisioning threshold** in any of its **sixteen metric families, twelve gates, or scenario matrices**. Needed numbers (standalone deprovisioning deadline, standalone review cadence, dormancy threshold, emergency-access expiry) -> **AM-3**; interim standards attach to existing cadence (same working session, Monday slot).

### 5.2 v4.0 references
| Rule | Use |
|---|---|
| G8 (Section 5) | Downstream honesty (AC-5); G8 governs downstream on feed break |
| G1-class | Impossible reads on affected rows -> QUARANTINE: DATA REFRESH |
| P3 (Section 12) | Audit-outranks-automation chain (I-8) |
| P5 (Section 12 Layer 7) | Human confirmation on "every bid move >25%" and "every budget move >$50/day" |
| V3 (Section 14) | Framework changes only by versioned amendment |
| V5 (Section 14 Layer 9) | Scores per owner (borrowed logins destroy it) |
| J6 | Cited in companions list |

### 5.3 Verdict strings (KDR v3.0 "CLOSED VERDICT VOCABULARY (Framework Section 17): exactly one per Keyword Decision Record")
| Situation | String | Why |
|---|---|---|
| Access failure breaks feed, G1-class impossible reads on affected rows | QUARANTINE: DATA REFRESH | Owning pass issues; P6 is repair task |
| Unrecognized actor's change unwound; term needs re-entry | PAUSED-PENDING (REASON + RE-ENTRY) | Owning SOP parks term; P10 close = re-entry criterion |
Access-state outcomes **PROVISION, DEPROVISION, SUSPEND ON DISCOVERY, RECONCILE, EMERGENCY-GRANT** are procedure states, not verdicts; never in a Master Action Record (AM-2).

### 5.4 Numbers
| Item | Value |
|---|---|
| Platform surfaces | 10, both entities |
| Spend authority | $6,000-8,000/day ($42,000-56,000/week) |
| Permission classes | 5 |
| Credential types | HUMAN / SERVICE / EXTERNAL / EMERGENCY |
| Row statuses named | LIVE / SUSPENDED / REVOKED (RETIRED for platforms) |
| Matrix re-issue | Within 1 week of org change; AC-1 fails >7 days |
| Carried finding limit | 1 cycle |
| Billing-admin answer | Under 5 minutes; >=1 LIVE billing-admin row per entity |
| Repeat escalation | Same credential class twice in 4 cycles; same failure mode twice in 4 cycles from same root cause escalates checklist gap |
| Deep pass | 4th diff of each month |
| BM Hub fields | 121+157 |
| Matrix size (WE-3) | 16 decision-class rows x 6 role columns = 96 cells |
| Durations | P1 20-35/wk; P2 60-90/person; P3 30-45; P4 20-40; P5 30-60; P6 15-30; P7 15-25; P8 15-25; P9 20-30; P10 30-60; P11 20-30; P12 10-15 |

### 5.5 Failure modes
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Orphaned credential after exit | P1 live seat no LIVE row; P10 branch 3 | Suspend same session; complete P3; root-cause names skipped platform |
| F2 | Shared login | One credential, multiple humans | Break same week; named seats; #38 notes unattributable window |
| F3 | Access failure breaking Monday pull | T7 MISSING with credential note at 09:00 (AC-3) | P6 same day; G8 |
| F4 | Over-permission vs Matrix | P4 diff or DRIFTED class above letters | Lower same session (Completion Directive two-cell disagreement shows drift happens) |
| F5 | Register drift | Platform level ≠ row class | Correct platform to register |
| F6 | Ownerless automation rules | #37 owner column points at SUSPENDED/REVOKED row | Reassign per #37 P4 before/with seat removal |
| F7 | Billing-admin discontinuity | #43 activation or 0 LIVE billing-admin rows on an entity | Hand to #43 immediately; billing failure pauses every campaign in both accounts |
| F8 | External access past end | EXTERNAL row past end date LIVE | P3 same session |
| F9 | PPC edit access on BM Hub | Hub sharing panel; PPC role above READ | Reduce to READ same session; inform BM owner |
| F10 | Emergency access never revoked | EMERGENCY row with refilled vacancy | Revoke same session |
Escalation: F1 on deploy-capable platform and F7 same day to PPC Lead (F7 onward to #43 owner); any finding past 1 cycle; same failure mode twice in 4 cycles same root cause escalates checklist gap, not the person.

## 6. Data inputs required

- **Platform user/permission lists** (exports or transcriptions) per inventory: Ads console US (Ecotero, Inspiratek) Administration > Manage users; Ads console CA; Seller Central US Settings > User Permissions; ScaleInsights Account > Team; DataRova; Keepa; SellerBoard (Account/Settings > Users); Drive sharing panels; BM Data Hub v2.0 sharing panel. Fields: person, email, permission level, last-activity date.
- **Platform change history** (acting credential for P10).
- **PPC Access Register** (REFERENCE, ROWS, DIFF, EVENT sheets).
- **PPC Authority Matrix v2.0** (`PPC_Authority_Matrix_v2_0.pdf`): cells by row & role; version date; Standing Rules 1-6; Completion Directive pending two-cell edit.
- **Transition Brief v1.2** scope stack.
- **T7 manifest** statuses rows **A2, A7, B6, B11, D8, D9** (Monday 06:00 pull, read 09:00); "Verdict Classes Blocked While Missing"; cycle header completeness score.
- **#38 T+1 attribution report** unclaimed-change lines.
- **#37 rule register** owner column; #37 weekly diff.
- **SOP-12 F10** console-edit findings.
- **Engagement records** with end dates.
- Org notices; adoption decision records.
- Feed credentials: Raw Pull Pack sheets, SQP export, DataRova, Keepa, SellerBoard, ScaleInsights change log.

## 7. Outputs / artifacts

| Artifact | Contents | Storage | Retention | Consumer |
|---|---|---|---|---|
| **PPC Access Register v1.0** (new instrument) | **REFERENCE** sheet (inventory, class definitions); **ROWS** sheet (one row per person-role x platform: class, Matrix basis cell, Matrix version, credential type HUMAN/SERVICE/EXTERNAL/EMERGENCY, MFA state, grant & revocation records, status; scope-note field; engagement end date for EXTERNAL); **DIFF** sheet; **EVENT** sheet (append-only) | Program library folder beside Cross-Reference Ledger (Definition Register entry = AM-6) | Append-only, permanent; rows revoked never deleted | P1-P12; #44; #3 re-issues; audits |
| Weekly diff report | Findings by class (UNREGISTERED/DRIFTED/GHOST), actions, counters (LIVE/SUSPENDED/REVOKED, days-open), 0-findings weeks | DIFF sheet, one block per cycle date | Permanent | P12 escalation; deep pass; #1 |
| Provisioning/deprovisioning packets | EVENT entries: date, person-role, platforms, classes, Matrix basis, confirmations, landed-proof | EVENT sheet | Permanent | #38 attribution investigations (P10); #44 certification evidence |
| Incident records (P10) | Credential, branch, platform evidence, #37/#38 cross-references | EVENT sheet, incident-flagged | Permanent | Escalation; V3-style amendment proposals |
| Billing-admin answer | Current LIVE billing-admin rows per entity | ROWS sheet filtered view | Live | #43 exclusively |
Also: F1-F10 alarms with evidence lines; drafted row edits queued for human checkpoints.

## 8. Decision rights

- **Human-mandatory:** every WRITE/OWNER grant (**PPC Lead** confirms; **CEO** confirms grants touching PPC Lead, per D cells on "v4.0 threshold changes" and "Push funding... above envelope"); every EXTERNAL WRITE (**CEO**, in writing); every P3 deprovisioning confirm and P11 emergency grant (**PPC Lead**, or CEO where Lead is the vacancy); P10 unknown-credential branch (**CEO informed same day**).
- **AI-executable with audit:** P1 diff & draft findings; P4 Matrix-diff drafts; T7 credential-failure triage drafts; EXTERNAL/EMERGENCY expiry flags; EVENT drafting.
- Register WRITE: PPC Lead only. Service credentials owned by Data Operations role. Transition Brief owner: **Head of Amazon Ops**. Matrix owner: PPC Lead (per I-1).
- ScaleInsights WRITE: PPC Lead (D), incoming operator (E, R), PPC Manager (E).
- Ramp: Week 1 reproduce Section 1.2 translation for every role column with 0 errors, locate every user-management surface, observe P1 & P2/P3; Week 2 supervised P1 and one P2; Week 4 unsupervised with audit, **2 consecutive clean cycles** (0 unexplained findings, 0 checklist skips) before sign-off; P3 on deploy-capable platform and any P10 stay Lead-confirmed permanently.

## 9. Account-specific facts

- Entities: **Ecotero LLC** and **Inspiratek LLC**; US Ads consoles per entity; CA console (#34 held at v1.0-structure; CA parameter column pending Ledger **D7**).
- Tools in use: **ScaleInsights** (automation), **DataRova** (rank, DSTR, top-ASIN), **Keepa**, **SellerBoard** (financial source of truth), **BM Data Hub v2.0** (121+157 fields), Drive workbooks.
- Credit-card ad billing ends **2026-08-01**; #43 due 2026-07-31.
- Matrix has a pending **Completion Directive two-cell edit**; two Completion Directive cells disagree.
- Fictional base: AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max Acc 26.3%.
- **WE-1:** incoming operator Matrix column: D,E on PAT/conquest opens & exits; D,E on D5 conversions & auto operations; D,E on incrementality tests; E (assigned scope) on weekly verdicts; E,R on automation rules; E on bulk deployments, push funding, code-red execution, event plans, sibling declarations, terminal lane, structure creation; I on v4.0 threshold changes and launch verdicts. P2 -> **14 rows**: Ads US x2 WRITE; Ads CA NONE; Seller Central x2 READ (SQP/STIS pulls are Data Ops service rows); ScaleInsights WRITE (E,R split noted); DataRova & Keepa READ; SellerBoard x2 READ; BM Hub READ; workbook layer WRITE on T2/T3/T6 for assigned products, STAGE elsewhere (2 rows); register STAGE. 82 minutes; next Monday diff 0 findings.
- **WE-2:** launch-scope contractor exits Friday; ScaleInsights seat missed; owns **3 C-class ladder rules** on two tail campaigns; Sunday bid step $1.46 -> $2.10; CPO $42.00 vs $28.00 contribution; 40 clicks/wk -> $84.00 spend, 2.0 orders, $56.00, **$28.00/week ($4.00/day) loss**; detected Wednesday (5 days, $20.00); weekly-diff-only worst case 8 days, $32.00.
- **WE-3:** launch/CA operator role vacated, scope folds to incoming operator; 96 cells checked; 9 cells change (4 zeroings: launch-stage verdicts D,E; Canada weekly block D,E; push funding E; event plans E; 5 raisings: launch-stage verdicts D,E; Canada block E; 3 scope-note updates); 24 minutes.
- **WE-4:** agency engagement 2026-08-03 for 60 days, end **2026-10-02** (Friday); STAGE on Ads consoles, READ workbooks; WRITE request declined by CEO; missed end date -> detected Monday 2026-10-05, 3 days, $0.00 exposure (STAGE).

## 10. Open items

| ID | Amendment item |
|---|---|
| AM-1 | Threshold authority file (ruled v4.0 by owner 2026-07-28) carries internal label v3.0 on title page and every footer; re-issue corrected |
| AM-2 | Access-state vocabulary (PROVISION / DEPROVISION / SUSPEND ON DISCOVERY / RECONCILE / EMERGENCY-GRANT) not in closed vocabulary; admit or exclude by V3 |
| AM-3 | No numeric access thresholds in v4.0: standalone deprovisioning deadline, access-review cadence (interim Monday slot + 4th-diff monthly deep pass), dormant-credential threshold, emergency-access expiry |
| AM-4 | Verdict-count discrepancy: v4.0 13.1 = 18; KDR v3.0 and SOP-12 v2.0 = 25; Ledger, Data Architecture, Command Workbook REFERENCE header = 26 ("KW VERDICT (26)" over 25 strings) |
| AM-5 | Section-citation drift: SOP-12 v2.0 cites "v4.0 Section 4.2" (naming) and "Section 4.4" (bidding strategies); governing file's Section 4 is the Interaction Layer and contains neither |
| AM-6 | PPC Access Register v1.0 needs Definition Register entry under #1 |

**Interface contracts:**
| ID | Dir | From -> To | Artifact | Timing | Non-arrival |
|---|---|---|---|---|---|
| I-1 | Up from #3 | PPC Lead (Matrix owner) -> SOP | Current Matrix (PDF) | Within 1 week of org change | Last Matrix governs; AC-1 blocks raises (lowerings still deploy); >7 days escalate as #3 defect; vacancy rule covers |
| I-2 | Up from Transition Brief | Head of Amazon Ops -> SOP | Transition Brief v1.2 scope stack | Role fill; scope change | AC-4 fails: P2 provisions READ everywhere, STAGE nowhere-scoped; no WRITE |
| I-3 | Up from #38 | Bulk mechanics operator -> SOP | T+1 unclaimed-change lines | T+1 after every deployment day | Detection degrades to weekly diff (8-day worst case); 2 consecutive missing -> #38 owner |
| I-4 | Down to #43 | SOP -> billing continuity owner | Billing-admin filtered view | On demand <5 min; every P1 | 0 LIVE billing-admin rows = F7 same day |
| I-5 | Down to #37 | SOP -> automation rules owner | Seat grant/revocation notes into owner column | Same session as seat event | Dangling owners surface a cycle late |
| I-6 | Down to #44 | SOP -> onboarding owner | Element 11 + EVENT evidence | #44 build (2026-09-25) and every ramp | Element 11 runs directly; #44 lateness is Gap Register escalation |
| I-7 | Up from #39/Data Ops | Data Ops -> SOP | T7 rows A2, A7, B6, B11, D8, D9 (Monday 06:00 pull, read 09:00) | Weekly Monday | Test each login directly; missing manifest reported as G8-class fault |
| I-8 | Down to weekly cycle (#4, #36) | SOP -> Monday audit cascade | Passing P1 diff | Monday slot, before deployment Tuesday | Unresolved F1 / unknown credential blocks deploy confirms for that entity Tuesday (staged sets hold at STAGE) per P3 |

**Review triggers:** Matrix re-issue; platform addition/retirement; landing of #43; landing of #44; landing of #40; v4.1 resolving AM-2/AM-3.

**Text anomaly:** Length statement says 2 worked examples; four (WE-1 to WE-4) are present.

**Named documents not present:** PPC Authority Matrix v2.0; Master PPC Decision Criteria System v4.0; KDR Template v3.0; SOP-37; SOP-38; SOP-43 ("when built"); SOP-44 ("when built"); Master PPC Data Architecture v1.0; Cross-Reference Ledger; Transition Brief v1.2; SOP-12 v2.0.
