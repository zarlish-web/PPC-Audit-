# SOP-43 Digest: Ad-Account Billing Continuity

Source: `PPC_SOP_43_Ad_Account_Billing_Continuity_v1_0.pdf` (10 pages). Digest of the plain-text extraction; nothing added beyond the text.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-43: Ad-Account Billing Continuity (PPC Department, Operating SOP, Component #43 of the Operations Definition Register) |
| Version | 1.0 (first build, no prior version) |
| Date | 2026-08-05 |
| Owner | PPC Lead |
| Thresholds | v4.0 only; **zero local thresholds**; every billing-specific operating number needed but absent from v4.0 is in the Closing Amendment List |
| Timing context | Written **4 days after** its own trigger event: **credit-card ad billing on the legacy method ended 2026-08-01**; component was **due 2026-07-31** |

**Verdict / purpose.** A billing failure on either entity ad account **pauses every campaign in that account** from the moment Amazon's charge attempt fails, halting **up to 100% of the $6,000-8,000/day account delivery envelope** and stopping every downstream SOP in the **46-component register** at once. Highest blast radius; Cross-Reference Ledger marks this component **the highest time criticality in the program**. SOP makes failure **preventable** (standing two-account Billing Continuity Register verified weekly), **detectable within the same day** (artifacts the stack already computes), and **reversible the same day** (pre-authorized response path with named escalation). Opens with an **immediate two-account state audit (P1)** rather than a pre-deadline migration plan; the 2026-08-01 change is the motivating incident class. The billing state P1 finds becomes **row 1 of the register**.

## 2. Scope & boundaries

**Owns exclusively (Ledger row):** billing method continuity across both entity ad accounts (**Ecotero LLC, Inspiratek LLC**) and the failure response: Billing Continuity Register & schema; weekly verification; primary/backup payment method doctrine in ad consoles; billing failure detection & triage; same-day remediation; restoration verification; post-incident reconciliation incl. trend-exclusion flagging; payment instrument lifecycle (expiry, replacement, entity banking changes as they touch console registration); quarterly continuity drill.

| Adjacent | Seam |
|---|---|
| Criteria System v4.0 (#8) | Decides every threshold/band/verdict; **zero billing rules today**; needed numbers are v4.1 items |
| #46 Access & Permissions | Owns billing-admin seat, provisioning, Access Register. This SOP consumes billing-admin filtered view; never grants, changes, audits access |
| #38 Bulk-File Deployment Mechanics | Owns staging, upload, T+1 verification. SOP reads T+1 report and A2 deployment state as detection evidence only; stages nothing |
| #37 Automation Platform Rules | Owns rule register & change control. Automation never touches billing surfaces; billing-adjacent rule proposals route to #37; #37 rule log read in triage to exclude rule-driven pauses |
| #3 Authority Matrix | No #43 row in v2.0; interim rights follow standing rules (vacancy reversion); AM-5 |
| #4 Weekly & daily cadence | P5 lands in Monday cascade; named billing slot and quarterly drill slot owed to #4 and #40 (AM-7) |
| Finance / entity officers | Own instruments (cards, bank accounts, credit lines, invoicing terms). SOP operates registration in consoles; never selects/negotiates |
| #32 Deal & Event Windows | Armed window multiplies outage exposure (F9); every event action is #32's |
| #24 Re-Ranking & Recovery | Owns rank restoration; P9 hands outage window & term list to #24 and stops |

## 3. Triggers

Billing lag ceilings tighter than same-day don't exist in v4.0 (AM-1); binding lag on alarm-class triggers is v4.0 same-day standard.

| Trigger | Detecting artifact | Max lag | Procedure |
|---|---|---|---|
| Weekly continuity check in Monday cascade | Billing Continuity Register + both ad consoles | Within Monday session (#4 slot) | P5 |
| Delivery collapse: product pacing deviation past **G7** line (**>25% vs day-of-week curve**) | **T0 zone D gates strip** / daily pacing alert (Data Architecture Section 4) | Same day, per G7 | P6 |
| Paused campaigns not traceable to any T6 entry or #37 rule | **#38 T+1 verification report**; **A2 deployment state** (T7 manifest row) | Same day of report | P6 |
| Amazon billing notification (failed charge, expiring instrument, unpaid invoice) | Routed alert inbox named in register row | Same day of receipt | P6, then P7 or P10 per content |
| Instrument lifecycle date approaching (card expiry month, invoice due day) | Register countdown columns, read at P5 | The P5 pass in which countdown first surfaces | P10 |
| Org change touching billing-admin seat | Authority Matrix re-issue; **#46 weekly reconciliation diff** | Within #46 weekly reconciliation | P11 access check |
| Billing incident closed (charge success confirmed) | Console Payment history entry written by P7 | Same day | P8, then P9 |

## 4. Procedures

### Preconditions (Element 3)
Missing artifact -> G8 honesty clause ("the analysis states what it could not see"); continue on direct console observation, record gap.
| Precondition | Source ID | Observable |
|---|---|---|
| Billing-admin access live on both consoles | #46 Access Register, billing-admin filtered view | Operator opens Billing page on both accounts without access error; #46 view shows seat row current. Fail: P11 |
| Deployment state current | **A2** (T7 manifest field group, per #39) | T7 row A2 PRESENT with current Monday refresh stamp; needed for P6 branches 2-4 |
| Decision log current & scored | **T6 Decision Log** (Data Architecture Section 9) | Last cycle's due rows carry V5 scores; pauses of record findable; needed for P6 branch 4 |
| Register at current version | Billing Continuity Register header | Header check-date = most recent Monday P5 stamp; stale -> P5 first |
| Automation rule log readable | #37 rule register ("the rule register, the sync check cadence, and change control") | Current export/log view opens; absent -> P6 branch 4 cannot clear; escalate (I-5) |
No billing-state manifest field group in #39; console is a manual read outside the Raw Pull Pack (AM-6).

### P1. Immediate two-account billing state audit (30-40 min both accounts; on adoption and after any entity-level account event)
1. Sign in to **Ecotero LLC** advertising console at **advertising.amazon.com** with billing-admin seat named in #46 view. No shared/personal credentials.
2. Account menu (**gear icon, top right**) -> **Billing**. Record from Billing summary: current payment method type (**charge card, direct debit, deduction from sales proceeds, monthly invoicing**); identifier (card network & last 4, bank last 4, or invoicing account reference); last successful payment date & amount from **Payment history**; any red failed-payment or unpaid-balance banner text verbatim.
3. Where entity advertises through seller account, also **Seller Central: Settings > Account Info > Payment Information > Advertising Charge Methods**: record charge method on file and whether set to **deduct advertising charges from sales proceeds** before charging the method. Both surfaces recorded (can disagree after migration).
4. Record outstanding unpaid balance & age. Unpaid balance with failed-charge banner = **live incident**: stop audit for this account, run P7 now; resume P1 after P8.
5. Repeat 1-4 for **Inspiratek LLC**; audited separately; nothing inferred across accounts.
6. One register row per account; State **VERIFIED** (method on file, no banner, last payment succeeded) or **FAILED** (banner or unpaid balance). Register vocabulary, not verdicts (AM-2).
7. Stamp audit date & executing role in header; log in **Incident and Check Log** sheet.

### P2. Build & maintain Billing Continuity Register (45 min first build; 5 min upkeep per P5)
1. Create **`Billing_Continuity_Register_v1_0.xlsx`**, two sheets: **Register** (one row per entity ad account) and **Incident and Check Log** (append-only).
2. Register columns, in order: **Entity; Ad account ID; Marketplace; Console URL surface (advertising console / Seller Central path); Billing mode; Primary instrument (type, network, last 4); Primary expiry (MM/YYYY); Backup instrument (same fields); Backup expiry; Deduct-from-proceeds state (Y/N/N-A); Invoicing terms and due day (or N-A); Billing-admin role holder (role, never a name); Alert inbox routing address; Last successful payment (date, amount); Last P5 check stamp (date, role); Next lifecycle date (computed: earliest of expiries and due days); State (VERIFIED / STALE / FAILED / INCIDENT-OPEN).**
3. Every value copied from a console surface or Finance confirmation, never remembered. No-source cell stays empty; row cannot read VERIFIED while a required cell is empty.
4. Version per #1 conventions: increments on schema change; row edits stamped in log. Definition Register entry owed (AM-8).
5. Storage: governance library folder holding **#46 Access Register**; access per #46 rules.

### P3. Configure primary & backup payment methods (20 min per account + Finance lead time)
1. Obtain instrument from Finance in writing (entity, account ID, primary or backup). Strongest backup is on a **different issuer or bank** than primary; reasoning recorded in request.
2. Console: gear icon > Billing > payment settings > **Add payment method**; complete verification challenge; confirm it appears in method list.
3. Set default: intended primary carries default marker; backup second. If console supports explicit backup designation, set it; otherwise backup's presence is the control and P7 step 3 switches manually.
4. Update register rows (primary & backup fields, expiries, State re-read); log with Finance request reference.
5. **Never remove old primary in same session as adding new**; remove one P5 cycle after new method's first successful charge appears in Payment history.

### P4. Monthly invoicing eligibility check & migration decision support (30 min per account + Amazon case latency + Finance review)
Decision owner: **Finance with the CEO**.
1. Look for invoicing eligibility notice or invoicing tab in Billing; if none, open Amazon ad support case asking about monthly invoicing qualification and credit line. Credit line read from Amazon/console, never assumed.
2. Compute: **trailing 30-day ad spend** (T0 zone B weekly spend summed over trailing period) vs offered credit line. **Line below trailing 30-day spend cannot carry the account alone; card/debit stays primary regardless of eligibility.** (WE-3 convention.)
3. Packet to Finance: eligibility state, line offered, trailing spend, due-day terms, current instrument state. Finance + CEO decide; decision & date logged.
4. On approved migration: console enrollment; terms & due day in register; keep card/debit as backup **until two invoice cycles have paid clean**.

### P5. Weekly continuity check (Monday cascade; 10-15 min both accounts)
1. Open register; confirm prior week's stamp exists (missing = skipped-check finding, F10 feeder).
2. Each console Billing surface: compare method list vs register (type, last 4, default marker). Mismatch: **console wins**, register corrects now, drift logged with cause (F7).
3. Payment history: confirm successful charge or paid invoice since prior check where cycle produced one; record date & amount.
4. Banner: failed-charge/unpaid -> row FAILED, P7 now in same session.
5. Next lifecycle date inside horizon (expiry month reached, or invoice due day this week) -> P10 this session.
6. Open routed alert inbox; clear billing notifications into log with disposition.
7. Stamp (date, role); row State VERIFIED, or **STALE** where console couldn't be opened (stamp says which surface not seen), or FAILED.
8. Route: FAILED -> P7; lifecycle -> P10; access failure -> P11.

### P6. Zero-delivery & unexplained-pause triage (15-30 min)
Runs **before any lever anywhere** (pulling a bid/budget lever on undiagnosed collapse = F8). Ordered; first match wins:
1. **Billing failure:** console Billing shows failed-charge banner or unpaid balance, and campaigns across entity's entire account paused/not delivering with no operator pause of record; halt entity-wide. -> declare incident (State INCIDENT-OPEN, log with detection time), run P7.
2. **Budget truncation:** specific campaigns show out-of-budget per **G3** (in-budget **<70% of the day** = truncated), Billing clean -> owning SOP's budget lever; close.
3. **Eligibility:** specific ads/SKUs ineligible (**G4** class), Billing clean -> owning SOP and listing task (G4 same day); close.
4. **Intended pause:** traces to T6 entry or #37 rule log line with matching date & target -> no incident; close with trace reference.
5. **Platform incident:** none match, both consoles anomalous, Amazon status/support confirm -> hold, record start time, re-check same day, log; no levers move.
If branch 4 evidence (T6 or #37 log) unavailable -> branch cannot clear; escalate to PPC Lead same day (I-5).

### P7. Billing failure response (same day; 30-60 min excl. bank/issuer latency)
Human-mandatory checkpoints on steps 3 and 5.
1. Identify failing instrument & failure text verbatim (declined, expired, removed, invoice unpaid).
2. **Transient retry:** if console offers retry/pay-now against existing method, execute **once**; second failure = instrument failure, no further retry.
3. **Switch to backup**: set backup as default (or pay balance with it). **Human-confirmed by PPC Lead before execution, same-hour where reachable.**
4. **No backup (F3):** escalate per P11 immediately; Finance provides instrument same day; Element 6 exposure math quoted in escalation.
5. Confirm success: Payment history shows settled; banner clears; record fix time. Balance settled but banner persists past same day -> Amazon support case; record case ID.
6. Hand to P8; INCIDENT-OPEN until P8 passes.

### P8. Restoration verification (20 min same day + next #38 T+1)
1. Campaign states back to pre-incident enabled states account-wide (Amazon resumes billing-paused campaigns after payment settles); any still paused past same day listed and routed to owning SOP.
2. Delivery resumed: spend accrues today; pacing recovers vs day-of-week curve (G7 artifact evidences recovery).
3. At T+1 reconcile #38 report & A2 vs expectations; residual mismatches per #38.
4. Row INCIDENT-OPEN -> VERIFIED; stamp restoration time; start P9.

### P9. Post-incident reconciliation (30 min, same day as P8 or next morning)
1. Closed incident record: detection time, P6 cause branch, remediation path, restoration time, **delivery gap** (expected spend by day curve minus actual) and implied foregone attributed sales.
2. **Flag outage window for trend exclusion**: no v4.0 gate covers non-event outage (**G10 event-only**); flag rides in register log, handed to Monday audit via I-7 until AM-3. Rate reads in window not used for verdicts.
3. Oversight-class term rank slipped across window -> window & term list to #24 (I-8); stop.
4. Feed Element 10: first live incident forces version review; record detection lag & response friction as candidate AM-1 figures.

### P10. Instrument lifecycle handling (15 min per event + Finance lead time)
1. Expiry approaching (surfaced at P5): request replacement from Finance same week citing expiry month; add per P3 while expiring instrument live; **never fewer than two working instruments**.
2. Check **#32 event calendar** for armed/upcoming windows overlapping expiry month (F9): handled in the week found, not queued (outage during event multiplies gap by event lift).
3. Entity banking changes (issuer change, account closure): Finance notifies (I-2); both rows re-verify per P1 steps 2-4.
4. Invoicing mode: due day in register; each P5 in due week confirms with Finance invoice scheduled/paid; unpaid at due day = FAILED; P7 step 5 confirmation with Finance executing payment.

### P11. Escalation & vacancy handling (routing table)
1. Billing-admin seat vacant/locked out: Matrix vacancy rule -> decisions revert to **PPC Lead**, execution to **PPC Manager**; emergency access via **#46 emergency access procedure**, never credential sharing.
2. Backup absent/failed during incident: Finance same day; unreachable Finance -> **CEO same day**.
3. Amazon-side failure (settled, campaigns still paused past same day): support case, case ID logged, daily follow-up.
4. Every escalation entry names blocked step, time, exposure figure (Element 6 math).

### P12. Quarterly continuity drill (45 min/quarter; V4 quarterly class; slot under #40 = AM-7)
1. Tabletop walk of P6-P8 vs 2026-08-01 incident class; narrate branch observables & console surfaces from memory, verify vs live consoles read-only.
2. Register audit: every cell re-verified vs console; drift per P5 step 2.
3. Backup viability: unexpired, listed, issuer relationship live per Finance; note proof if charged in trailing period; if never charged, Finance confirms active on issuer side, unproven state recorded.
4. Access test: seat opens both Billing surfaces; #46 view matches.
5. Drill stamp in log; missing at quarter end = F10.

## 5. Rules, thresholds & numbers

### 5.1 v4.0 rules consumed
| Rule | Section | Use |
|---|---|---|
| **G7**: pacing deviation **>25%** vs day-of-week curve alerts same day | Section 5 Layer 0 Gates (G1-G12) | Primary automatic billing-halt detection; P6 entry; P8 recovery evidence |
| **G3**: in-budget **<70% of the day** = campaign truncated | Section 5 | P6 branch 2 |
| **G4**: eligibility flips alert same day, halt work on target | Section 5 | P6 branch 3; same-day lag class |
| **G8**: "the analysis states what it could not see" | Section 5 | Element 3; P5 step 7 |
| **P8** (precedence): data-quality failure beats every other consideration incl. urgency | Section 12 Layer 7 (P1-P10) | P6: no lever on undiagnosed collapse |
| **V4**: quarterly cadence class | Section 14 Layer 9 (V1-V8) | P12 drill |
| G10 | Section 5 | Event-only exclusion; does not cover non-event outages (AM-3) |
| V3 | Section 14 | Amendment protocol for register vocabulary (AM-2) |
| V5 | Section 14 | T6 scores (precondition) |
| V6 | Section 14 | Sync rule: skill version-pins v4.0 |
| 13.1 | Closed Verdict Vocabulary | Contains no billing verdict; SOP issues zero verdicts, quotes zero verdict strings |

### 5.2 Numbers
| Item | Value |
|---|---|
| Account delivery envelope | $6,000-8,000/day (documented account fact) |
| Register size | 46-component register |
| Legacy card billing end | 2026-08-01; component due 2026-07-31; written 2026-08-05 |
| Transient retry | Once only |
| Old primary removal | One P5 cycle after new method's first successful charge |
| Invoicing backup retention | Until two invoice cycles paid clean |
| Minimum instruments | Never fewer than two working instruments |
| Migration test | Credit line vs trailing 30-day spend (line below spend -> card stays primary) |
| Durations | P1 30-40 min; P2 45 first / 5 upkeep; P3 20/account; P4 30/account; P5 10-15; P6 15-30; P7 30-60; P8 20; P9 30; P10 15/event; P12 45/quarter |
| Escalation | Same failure twice in consecutive quarters on same account -> PPC Lead |
| WE-2 detection lag | 7h40m (candidate AM-1 figure) |
| #40 due | 2026-09-18; #44 due 2026-09-25 |
Zero-local-thresholds statement: every other numeral is an identity/date, documented account fact, time estimate, or labeled illustrative input. Needed number classes (AM-1): detection lag ceiling tighter than same-day, remediation clock, expiry lead time, invoice-confirmation lead, register staleness horizon.

### 5.3 Register vocabulary (AM-2)
VERIFIED / STALE / FAILED / INCIDENT-OPEN.

### 5.4 Failure modes
| ID | Failure | Detection | Response |
|---|---|---|---|
| F1 | Silent decline (notification unrouted) | G7 alert with no inbox entry; banner found only at P6 | P6 then P7; alert-routing cell corrected to role inbox same day. Motivating incident: 2026-08-01 end of legacy card method |
| F2 | Wrong entity remediated | Banner persists; Payment history unchanged | Re-run P7 on correct account; rows keyed by ad account ID; P7 step 1 quotes ID |
| F3 | No backup instrument | P5 empty backup cell; P7 step 3 finds nothing | P3 same week; P11 same-day Finance on incident path with exposure figure |
| F4 | Access lockout at failure time | Billing page won't open; #46 vacancy/dead credential | P11 step 1 vacancy reversion; #46 emergency access |
| F5 | Invoice unpaid at due day | P5 due-day check finds no Finance confirmation | Finance pays same day; FAILED until settled; repeats route back to P4 |
| F6 | Campaigns not restored after settlement | P8 step 1 list; #38 T+1 mismatch | Owning SOPs repair; past same day support case |
| F7 | Register drift vs console | P5 step 2 mismatch; quarterly audit | **Console wins** (deliberate inverse of workbook-is-truth rule) |
| F8 | Billing halt misread as performance collapse | T6 lever entries inside outage window; rate verdicts on outage-week reads | Revert lever; trend-exclusion flag; re-teach P6 |
| F9 | Expiry inside armed event window | P10 step 2 overlap check vs #32 calendar | Replacement before window opens; log; event-lift exposure noted |
| F10 | Drill skipped; backup dead when needed | Missing quarterly drill stamp; backup switch fails | P12 re-arms; restore two instruments; cause named |

## 6. Data inputs required

- **Amazon Ads console (advertising.amazon.com)**, per entity (Ecotero LLC, Inspiratek LLC): gear icon > **Billing** summary (payment method type, identifier: network & last 4 / bank last 4 / invoicing reference); **Payment history** (last successful payment date & amount; unpaid balance & age); failed-payment / unpaid-balance **banner text**; payment settings method list & **default marker**; retry/pay-now control; invoicing eligibility notice/tab; campaign lists state account-wide.
- **Seller Central: Settings > Account Info > Payment Information > Advertising Charge Methods** (charge method; deduct-from-proceeds setting).
- **Billing_Continuity_Register_v1_0.xlsx** (Register sheet, all P2 columns; Incident and Check Log).
- **Routed alert inbox** (Amazon billing notifications: failed charge, expiring instrument, unpaid invoice).
- **T0 zone D gates strip** / daily pacing alert (G7 deviation vs day-of-week curve; expected spend by hour of day).
- **T0 zone B** weekly spend (trailing 30-day ad spend for P4).
- **T6 Decision Log** (pauses of record; V5 scores).
- **T7 manifest row A2** (deployment state).
- **#38 T+1 verification report**.
- **#37 automation rule log / rule register export**.
- **#46 Access Register** billing-admin filtered view; #46 weekly reconciliation diff; Authority Matrix re-issues.
- **#32 event calendar** (armed/upcoming windows).
- **Finance confirmations**: instruments, expiries, issuer, invoicing terms, due day, payment confirmations, banking changes.
- **Amazon support case** responses (credit line, platform incidents); Amazon status surfaces.
- Campaign in-budget/out-of-budget signals (G3), eligibility flags (G4).
- Oversight-class term rank data across outage window (for #24 handoff).
- **No Raw Pull Pack feed** for billing state (manual console read; AM-6).

## 7. Outputs / artifacts

| Artifact | Storage | Retention | Consumer |
|---|---|---|---|
| Billing Continuity Register (Register sheet; columns per P2) | Billing_Continuity_Register_v1_0.xlsx in governance library folder with #46 Access Register | Current live; superseded versions per #1 conventions | P5-P12; #46 on demand; quarterly drill |
| Incident and Check Log (append-only) | Same workbook | Permanent; never edited | Monday audit (trend-exclusion flags, I-7); #24 (I-8); Element 10 reviews; #6 scoring context |
| Weekly check stamp | Register header + log entry | With register | #4 cadence conformance; F10 detection |
| Incident record (closed): detection time, P6 branch, remediation path, restoration time, delivery gap, foregone sales | Log sheet | Permanent | AM-1 evidence base; P12 scenario library |
| Escalation entries (blocked step, time, exposure figure) | Log sheet | Permanent | PPC Lead; Matrix re-issue evidence |
| Incident broadcast INCIDENT-OPEN (freezes new deploys in affected account until P8) | To every operating SOP (12-38) | - | I-6 |
| Trend-exclusion flag for outage window | To Monday audit (#36 by absorption) | - | I-7 |
| Finance instrument requests; P4 migration packet; Amazon support cases | - | Logged | Finance/CEO |
Skill outputs: drafted register rows & stamps queued for confirmation; lifecycle & drift alarms with evidence lines (row, surface, observed vs registered value); P6 triage packets; drafted incident/escalation entries with exposure figure.

## 8. Decision rights

- Authority Matrix v2.0 has **no #43 row** (AM-5); interim per standing vacancy rule and **10-80-10 method (#7)**; checkpoint holder throughout = PPC Lead.
- **Human-mandatory always:** adding, removing, switching any payment method (**PPC Lead confirms; Finance supplies**); incident declaration & close (**PPC Lead**); P4 migration decision (**Finance with CEO**); any escalation past Finance (**CEO**).
- **AI-executable with audit:** register upkeep drafts, lifecycle countdown alarms, P6 evidence packets, log drafting, drill scheduling.
- Vacancy: decisions -> PPC Lead, execution -> PPC Manager.
- Finance/entity officers select & own instruments; #46 owns seat; #24 owns rank recovery.
- Ramp: Week 1 reproduce both register rows read-only, P6 on paper vs 3 historical T6 cases, name all interfaces; Week 2 supervised P5, one P10 staged, WE-2 incident entry draft; Week 4 two unsupervised Mondays, lead P12 tabletop, one deployment day with seeded false alarm exiting at branch 2 or 4.

## 9. Account-specific facts

- Two entity ad accounts: **Ecotero LLC** and **Inspiratek LLC**.
- Delivery envelope **$6,000-8,000/day**.
- Legacy-method credit-card ad billing ended **2026-08-01**; Ledger #43 row status was **NOT BUILT / DUE 2026-07-31** (superseded, AM-9).
- Illustrative (not live) entity split: Ecotero $4,000/day, Inspiratek $3,000/day ($7,000/day). Illustrative blended account ACOS 25.0%. Standard fictional base AOV $80.00, contribution $28.00, BE 35.0%, Target 17.5%, Max Acc 26.3%.
- **WE-1:** 2026-08-24 P5 finds Ecotero primary card expiry 09/2026; P10 fires. Missed-expiry exposure: 24h outage at $4,000/day -> $16,000 attributed sales (4,000/0.25), 200 orders, $5,600 contribution, **$1,600/day** direct contribution lost net of spend; **$666.67/hour** attributed sales.
- **WE-2 (2026-08-01 class):** Friday 05:40 Inspiratek retired-card charge fails; notification to unread personal inbox (F1). 13:00 pacing: expected 40% of $3,000 = $1,200 vs actual $120 -> **90.0% deviation** (>25% G7). Incident 13:20; backup set default 14:10; settled 14:25; day closes $1,920 = 64.0% of plan; gap $1,080; foregone $4,320 sales, 54 orders, $1,512 contribution, **$432 direct contribution lost** for 8.5-hour outage; #24 not opened; routing cell corrected; closed 15:05; detection lag 7h40m.
- **WE-3:** illustrative Ecotero credit line $40,000 vs trailing 30-day spend $120,000 -> covers 33.3%; defer; card stays primary.

## 10. Open items

| ID | Amendment item |
|---|---|
| AM-1 | No billing continuity thresholds in v4.0; needed: detection lag ceiling tighter than same-day (WE-2 7h40m first evidence), remediation clock (declaration to backup switch), expiry lead time in days, invoice-confirmation lead, register staleness horizon. Until then v4.0 same-day class binds |
| AM-2 | Register state vocabulary (VERIFIED/STALE/FAILED/INCIDENT-OPEN) needs admission under V3, mirroring #46 access-state vocabulary item |
| AM-3 | No v4.0 gate excludes non-event outage windows (G10 events only); proposed outage-exclusion clause of G10 pattern keyed to incident log |
| AM-4 | T5 Product Log closed event-type list (8 types, Data Architecture Section 9) has no billing-outage type |
| AM-5 | Authority Matrix v2.0 has no #43 row; owed cells: billing state checks, default-method switch, incident declare & close, migration decisions, escalation past Finance |
| AM-6 | No #39 manifest field group for billing state; console manual read outside Raw Pull Pack |
| AM-7 | #4 names no billing-check slot; quarterly drill has no calendar home until #40 (due 2026-09-18) |
| AM-8 | Register owes Definition Register entry under #1 |
| AM-9 | Ledger #43 row NOT BUILT / DUE 2026-07-31 superseded by this build |

**Pre-logged, not re-opened:** closed-vocabulary count discrepancy (18/25/26) logged by #41, #46, #17/18/19 builds; gate-numbering item (Data Architecture T5 labels trend-exclusion flag with a gate ID that v4.0 assigns to MKL hygiene) carried as #17/18/19 build's **C9**.

**Interface contracts:**
| ID | Dir | Sender -> receiver | Artifact | Timing | Non-arrival |
|---|---|---|---|---|---|
| I-1 | Up | #46 -> #43 | Billing-admin filtered Access Register view | On demand; every org change | P5 on console only; gap stamped; escalate to PPC Lead |
| I-2 | Up | Finance/officers -> #43 | Instruments, replacements, invoicing decisions | Before expiry month; same day on incident | P7 can't complete; CEO same day; single instrument logged as open F3 |
| I-3 | Up | Amazon -> alert inbox | Billing notifications | Event-driven | Fallback to G7 and #38 report; F1 logged; routing repaired |
| I-4 | Up | #38 -> #43 | T+1 report; A2 | T+1 after deploys; Monday refresh | P6 branches 2-4 lose evidence; no branch-4 closure on absence |
| I-5 | Up | #37 -> #43 | Automation rule log | Weekly; on demand | Branch 4 can't clear; escalate same day |
| I-6 | Down | #43 -> every operating SOP (12-38) | INCIDENT-OPEN broadcast freezing new deploys until P8 | Same day as declaration | Staged sets deploy into paused account; false F10-class investigations; F8 risk |
| I-7 | Down | #43 -> Monday audit (#36 by absorption) | Trend-exclusion flag | Before next Monday pass | Outage rates enter trends; wrong-direction V5 scores |
| I-8 | Down | #43 -> #24 | Outage window + rank-affected terms | Within P9 session | Rank damage compounds; misdiagnosed cold-start |
| I-9 | Down | #43 -> #1 | Definition Register entry; version notes | Each register version | Unregistered artifact; supersession unauditable |
| I-10 | Down | #43 -> #44 | Element 11 ramp content | When #44 builds (due 2026-09-25) | Certification omits this SOP |

**Review triggers:** Amazon change to ad payment surfaces/charge sequencing/invoicing terms; entity banking/issuer change; Authority Matrix re-issue touching billing-admin/Finance/CEO roles and AM-5 landing; first and every live incident; any AM item landing; #40 landing.

**Named documents not present:** Master PPC Decision Criteria System v4.0; PPC Cross-Reference Ledger (#43, #46, #37, #38 rows); PPC Authority Matrix v2.0; #46 Access & Permissions; #38; Master PPC Data Architecture v1.0; PPC Economics Worked Example Set v1.0.
