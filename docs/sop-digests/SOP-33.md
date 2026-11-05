# SOP-33 Digest: Sibling and Family Arbitration Operations

Source: `PPC_SOP_33_Sibling_and_Family_Arbitration_v2_0.pdf` (17 pages). Digest of the plain-text extraction; nothing added beyond the text. Some tables were flattened in extraction and their columns were rebuilt from the content.

## 1. Header

| Field | Value |
|---|---|
| Full title | SOP-33: Sibling and Family Arbitration Operations (Component #33 of the Operations Definition Register) |
| Version | 2.0 |
| Date | 2026-08-08 |
| Owner | PPC Lead |
| Supersedes | SOP-33 v1.0 (2026-07-24) in full |
| Build | Session 16, Wave 5A |
| Thresholds | Thresholds, bands, scenarios and verdicts live only in Criteria System v4.0. **Composite weights and factor definitions live in the Account Rollup Workbook v1.0 tab A1**, operating under v4.0. Zero local thresholds |
| Size | 14 procedures (v1.0: 7); 12 failure modes (v1.0: 6); 4 worked examples (v1.0: 1); full 25-string vocabulary + v4.0-only rows (v1.0: 5-row mapping); 12 amendment items; 18 interface contracts |

**Verdict / purpose.** When two family products can serve the same root, **ownership is decided by one arithmetic product read off one instrument**. Until that number is on the record, **guards hold on both siblings at once**. The composite is:

> **Composite = Margin $ per order x Root CVR x Inventory depth (days)**, computed on Account Rollup Workbook v1.0 **tab A1**. The output is a **relative index, never a per-click dollar value**.

v2.0 corrects v1.0's composite method, which computed a two-term "value per click" and then applied a separate inventory factor. That method does not reproduce the instrument's live cell and is retired. The SOP governs the whole arbitration life of a contested root: weekly detection, finding intake, guard enforcement, evidence assembly, the dated probe for a sibling with no served evidence, composite computation, the mandatory structural inspection before any auction explanation, declaration and same-day walls, non-owner posture, twin-set coordination, re-arbitration on named drivers, temporary stewardship on owner stockout, and quarterly drift review.

### Why three terms (Section 1.1)
Margin sets what a sale is worth; CVR sets how often a click becomes a sale; depth sets how long the product can hold ownership pressure. A sibling winning on the first two without the third is "an owner in name only", re-contested within a month by its own stockout. Multiplying makes depth a cost of ownership. **Proof: tab A1 reads 58.3358125 for the Bamboo 4-piece row; 28.37 x 0.04375 x 47 = 58.3358125 to seven decimals.** PPC Strategic Doctrine v1.0 Section 5.2 case 4 says the same: one family member owns the root on a margin x CVR x inventory-depth composite and the sibling defends at floor.

### Three states of a shared root (Section 1.2)
| State | Definition | Cost while it persists |
|---|---|---|
| **UNDECLARED** | Root appears in 2+ siblings' campaigns or served terms; no declaration record | Both siblings bid the same auction with the same money. Neither may open or lift a rank push. Existing spend continues at current levels (cost = opportunity + auction self-competition, not an immediate cut). Gate **G11** makes it a portfolio decision |
| **DECLARED** | One sibling holds root on a recorded composite table, dated, with named re-arbitration triggers | Nothing while drivers hold. Non-owner keeps its own modifier space and defends at floor there. Cost = walls + review obligation |
| **STEWARDED** | Declared owner out of stock; dated, reverting grant places root with strongest sibling until owner restocks and recovers | Live reversion obligation. Outliving its date = silent ownership change (F5). Every grant carries a computed reversion date at issue |

## 2. Scope and boundaries (Section 1.3)

| Component | Seam |
|---|---|
| Criteria System v4.0 (#8) | Every threshold, band, gate, scenario, verdict string. This SOP computes and declares; never sets a number |
| **Account Rollup Workbook v1.0 tab A1** | Owns composite formula, factor definitions, grid layout, **S-series finding format**. This SOP operates the instrument and returns inputs + declaration. Per Ledger row 33, composite weights are the instrument's |
| #29 Negation | Owns wall doctrine, wall levels, reverse test, removal control, monthly wall audit. This SOP issues the declaration causing a wall and consumes confirmation. Per Ledger row 29: that SOP's **I-8 inbound** and **I-9 outbound**. Cite by Ledger row: v2.5 correction register records the sibling-wall move **from P5 to P7 in SOP-29 v2.0**, and Ledger row 33 still carries the superseded number |
| #23 Ranking-push | Owns push sizing, funding, standup, in-flight, stop-loss. The guard here is a precondition there, recorded as **#23's I-3** in Ledger row 23 (non-arrival = indefinite hold on both siblings). This SOP never sizes/funds/stops a push |
| #12 Exact | Runs the **G11 declared-owner check** before any scale action on a shared term (Ledger row 33 downstream cell). This SOP issues no campaign-level bid/budget/status edit |
| #24 Re-ranking and recovery | Owns baseline restoration and post-restock recovery. This SOP reads restock date + recovery class to compute stewardship reversion |
| #32 Deal and event window | Owns event plan; this SOP requires a contested root to be named in any event plan touching either sibling |
| #22 Launch-stage PPC | Owns launch handoff; this SOP scans the newcomer's keyword set against declared roots |
| Envelope and funding | Cross-product push funding ranked on **Account Rollup tab A2** and product **T0 zone H** queue. Per Ledger conflict **C3**, #31 has no numbered procedures; name the instrument and tab |
| #38 Bulk mechanics | Every wall and campaign consequence deploys through #38; nothing edited in a console |
| #28 | Discovers and holds floor via ladder mechanics (named in P10) |
| #35 | Owns incrementality; a live test on a contested root suspends the P4 CVR read |
| #16 | Conquest; a conquest list containing a sibling's own ASIN is a catalogue defect routed to #16 |
| #17-19 | SBV/SD format substitution (with paired step-down at #12) |
| #30 | Graduation; a graduation standing up an exact on a root another sibling owns is held until the declaration is read |

**Depth statement (1.4):** a declaration is issued "perhaps a dozen times a year across five brands", but each binds two products' plans under precedence rule **P9**, survives until a named driver moves it, and has three failure directions that all look like success from inside one product's workbook.

## 3. Triggers (Section 2)
Lag is counted from when the artifact is readable.

| Trigger | Detecting artifact and signal | Max lag | Procedure |
|---|---|---|---|
| Shared-root finding | Cross-product registry scan across product Command Workbook **tab T2 block 8** columns + **search-term join**: root live in 2+ siblings' campaigns, or converting in 2+ siblings' served terms | Same cascade (Monday pass after product workbooks refresh at 09:00) | P1, then P2 intake + guard arming same session |
| Family Conflict cell opens | **T2 block 2 "Family Conflict"** moves off clean state on any oversight row (e.g. live B4 reading "OPEN: shared with B6 sibling, owner undeclared") | Same day (gate column) | P2; P3 guards armed before any verdict on that row |
| New sibling launch | #22 launch handoff into a family with declared roots, keyword set attached | Within one cascade | P1 restricted to newcomer's keyword set vs declaration register |
| Composite driver moves | Price/cost move on **D1 margin table**; root CVR read crossing its recorded trigger; inventory band change on **T2 block 2**; variation retirement on **D2 map** | Same cascade for margin and CVR; **same day for inventory band flip** | P12 |
| Owner stockout | Owner's serving variation reaches **G6 RED**, or stockout confirmed on Economics and Context Pack **D1 row** and **D2 backup chain exhausted** | Same day (re-point runs first) | P13 |
| Sibling CPC divergence | **A1 family grid divergence flag** on a shared root, read against rule **X6** trigger | Same cascade | P7; on undeclared root also opens P2 |
| Declaration deadline | Open finding reaches its recorded deadline with no declaration | Same day | P14 escalation; guards stay armed |
| Quarterly review | Review date on declaration register | Within review week | P14 drift check |

## 4. Procedures

### Preconditions (Section 3; T7 manifest groups)
| Group | Requirement | Observable |
|---|---|---|
| **B5** Coverage counts | Registry counts per match type current on both siblings | **T2 block 8** exact, phrase, broad, auto, SB/SBV/SD/PAT counts populated for root on both, refresh timestamp in current cycle |
| **B8** Row economics | Margin $/order for the variation the root lands on, not the blend | Economics and Context Pack v1.0 **tab D1 "Contribution $/unit"** + **"Version"** stamp on serving variation row. Blended-only means **G9 PROVISIONAL** rides onto composite and declaration |
| **D2** Variation map | Root mapped to targeted variation and ranked backup chain on both | **Tab D2 "Keyword-Variation Map"**: Preferred SKU and Backup SKU, status not unmapped. **Ledger dependency D2 OPEN**: most rows pending; depth capped to product-level read, stated |
| **A3** Pacing and **A2** deployment | Current bid, budget, placement multiplier state on every campaign serving root on both | **Tab T3** state, daily budget, bid, placement multipliers. Absent = P7 unreadable |
| **B3** Rank pack | Organic and target rank on root for both | **T2 block 4**. Rank does not enter the composite; it enters the record |
| Inventory feed | Days to stockout on preferred SKU for both, daily | **T2 block 2 "Days to Stockout"** with SKU (e.g. live B4: **47 days on KING-WHITE** preferred SKU) |

### Gates in force
| Gate | Effect |
|---|---|
| **G11** Sibling conflict | Two siblings with active push objectives on same term is a portfolio decision. Both are held from scaling until the portfolio call assigns a lead and a support-or-stand-down posture. Read in T2 Family Conflict cell. The reason this SOP exists |
| **G6** Inventory adequacy | Supplies depth. RED on owner's serving variation goes to P13 after re-point exhausted. YELLOW does not by itself re-open; it moves the composite and is read at next review unless it crosses a recorded trigger |
| **G9** Price stability | Price change in trailing window marks CVR PROVISIONAL; composite legal but flag carried onto record in engine's words (rule **J7**); suppressing = F11 |
| **G2** Sample sufficiency | Governs root CVR evidence; twin sets pool, so P11 precedes CVR read |
| **G8** Packet completeness | Degraded packet: composite becomes a flag; finding open, guards armed, no declaration |
| **G12** | v4.0 = MKL hygiene (untagged/no relevancy root goes to taxonomy maintenance, not arbitrated); corpus alias = event freeze (live event window on either sibling requires root named in event plan). Both apply (C9) |

### P1. Weekly cross-product shared-root detection scan (20 min five-brand account; 35 min first run of quarter)
1. Open Account Rollup Workbook v1.0 **after** product cascades close (product workbooks close Monday, rollup refreshes after). A scan before refresh reads last week's grid.
2. Two sources. **Source A**: each product Command Workbook **tab T2 filtered to Row Type = KW**, block 8 **"Sibling CPC View (D6)"** and **"Term Owner (Family)"**. **Source B**: the **search-term join** under each keyword's campaign child rows (exposes roots served without being a keyword). Source-B-only roots are the more expensive class.
3. Normalise to roots using **T2 block 1 "Syntax Tags"** (root|size|colour|attribute form). E.g. "bamboo sheets", "bamboo sheets queen", "queen bamboo sheet set" = one root.
4. Two conditions; **either opens a finding**: (1) root/term live in 2+ siblings' campaigns per block 8 counts; (2) root/term converted in 2+ siblings' served terms in trailing window. Both together raise priority only.
5. Exclude on evidence only, **three reasons exactly**: live declaration with no driver moved; one product not a family sibling under A1 family definition; second appearance a reporting artifact proven by registry read (no live campaign, no served term). Anything else = finding with a note.
6. Record the scan even when empty: date and count of roots tested in the declaration register (no artifact = F12).
- **Instrument gap to state every scan:** T2 block 8 "Sibling CPC View (D6)" is a **pending build** across the corpus, so Source A is thin and **Source B carries detection**. State which source produced each finding.

### P2. Finding intake, evidence snapshot, guard arming (15 min per finding)
1. Open an **S-series finding** on the A1 family grid in the instrument's format.
2. Snapshot both siblings from T2 at opening: current bid and suggested bid with gap, TOS modifier %, spend on root for window, term clicks, term orders, organic vs target rank, inventory band with days to stockout and SKU. Taken before guards change behaviour.
3. Write the declaration deadline: no v4.0 interval; use the instrument's family-grid review cadence (AM-2).
4. Set **T2 block 2 "Family Conflict"** to open on both siblings' workbooks, naming counterpart and finding (live B4 form: open marker, sibling named, gate reference).
5. Set **T2 block 8 "Term Owner (Family)"** to undeclared on both (empty and undeclared are different states; only undeclared is readable by #12's G11 check).
6. Arm guards per P3 in the same session.

### P3. Guard enforcement while undeclared (5 min to arm)
1. No sibling opens a rank push on the root; no live push is lifted (precondition inside #23, its I-3).
2. **Existing spend continues at current levels**: guards freeze escalation, not spend (cutting would corrupt the CVR evidence).
3. Root excluded from cross-product funding queue on **Account Rollup tab A2** until close. Queued asks are **withdrawn, not deferred**.
4. Any #32 event plan touching either sibling names the root explicitly; otherwise the root is out of the window.
5. Structural changes freeze on both siblings: no new exact, consolidation, promotion/demotion. Bid/budget inside existing structure continues via normal weekly verdict path.
6. **Guards lift on exactly one event: a filed declaration record with its wall confirmation attached.** Not on deadline passing, staleness, or preference. (Also lift on the LEAVE TO HARVEST declined-and-logged close; see Section 5.)

### P4. Composite input assembly and qualification (25 min per sibling; 40 min if variation unmapped)
| Input | Required source | Qualification test | If it fails |
|---|---|---|---|
| **Margin $ per order** | Economics and Context Pack v1.0 **tab D1**, row for variation root lands on per D2 | Row has Contribution $/unit + Version stamp; variation is D2-named, not blend | Read blended row, carry **G9 PROVISIONAL** onto composite and declaration, log variation row as owed. Blended without flag = **F11** |
| **Root CVR** | **T2 block 5** cross-type totals for root's terms: orders / clicks over cycle window | Clicks from sibling's own serving on root; sample clears G2 CVR bar; twin members pool per G2 | Run **P5**. Never impute from a sibling, a modifier term, or product average |
| **Inventory depth (days)** | **T2 block 2 "Days to Stockout"** on D2 preferred SKU | Figure names its SKU and it is the D2 preferred SKU for the root | Use product-level band read, state substitution, cap to a structural read (D2 OPEN) |
| **Window** | A1 grid's cycle window, identical for both | Both read same window (30-day vs 7-day is not a comparison) | Re-pull to common window; no v4.0 recency window (AM-5) |

1. Assemble all four inputs for both siblings before computing anything.
2. Write each input into the A1 grid row **with its source cell reference beside it**.
3. Record every flag (G9 provisional margin, thin sample, substituted depth, pooled twin CVR) in the engine's words (**J7**; "confidence theatre is a process violation").

### P5. The dated probe for a sibling with no served evidence (20 min to stage; 2-3 cycles to run)
1. Condition: sibling has **never served** the root (no CVR). A sibling that served and converted poorly is not a probe case.
2. Choose and record: **Path A** dated probe, finding held open; **Path B** declare the served sibling now with a dated re-check. **Path B is legal only when the served sibling's composite clears the unserved sibling's best arithmetically possible composite** = unserved sibling's margin x its depth x **the highest CVR any family member has recorded on the root**.
3. Size to the evidence bar: closed vocabulary caps a deliberate test at **50 clicks**; CVR verdict needs a larger G2 sample. Run in **tranches**: tranche 1 to the verdict cap, tranche 2 to the CVR sufficiency bar. Tranche 1 alone cannot be the CVR input (F7). No single verdict string (AM-7).
4. Probe bid = sibling's own **Expected CPC in T2 block 6**, not the counterpart's CPC. If per-term Expected CPC not landed, use the **account reference in T7 manifest**, substitution stated.
5. Stop conditions before opening: click cap per tranche, date, and the single early-stop: **sibling's own inventory band leaving GREEN**.
6. Feed result into P4 with sample-state flag; run P6.

### P6. Composite computation on the A1 grid (10 min)
1. Enter per sibling: **Margin $/Order, Term CVR, Inventory Depth (days), window**.
2. Grid computes Composite = Margin x CVR x Depth. **Do not overwrite the formula cell.** Units are relative, no currency.
3. Read **Share of Composite** per sibling; the record carries share.
4. **Do not declare yet.** P7 runs first, without exception.
5. Close shares mean the composite has not decided. v4.0 has no minimum separation. Its tiebreaks disagree: **S-B2** (margin-dollar class, then inventory depth) vs **M5** (margin-dollar class, then earning-potential class). Record near-tie, hold guards, log AM-1 (verdict EXTEND TEST).

### P7. Structural inspection before any auction explanation (30 min; 50 min if duplicate found)
Mandatory on every arbitration. Rule **X6** fixes the order: an auction explanation is accepted only after the five settings causes are excluded on evidence.

| Step | Read | Fires when |
|---|---|---|
| 1 Objective tags and intentionality | **T2 block 7 "Objective"**, **T3 "Objective Tag"** on every serving campaign, both siblings | UNTAGGED either side: route to objective assignment; composite waits |
| 2 Placement multipliers and effective TOS CPC | **T3 "Placement Mult TOS %"**, **T4 "Effective TOS CPC $"**. Effective TOS CPC = bid x (1 + TOS multiplier); compare vs sibling's own max profitable CPC = margin x CVR | Above it: divergence is a multiplier, not a market |
| 3 Bidding strategy | **T3 "Bidding Strategy"** both sides | Different strategies: not the same auction, CPCs not comparable |
| 4 Duplicate / legacy campaigns still bidding | **T2 block 8 "Duplicate Flag"** + campaign child rows | Live legacy instance: its spend and orders contaminate CVR and margin reads |
| 5 Targeted variation differences | **T2 block 2 "Targeted Variation(s)"** vs D2 map | Different variations mean different margin rows; blend input wrong on at least one side |
| 6 Genuine auction position difference | Only reachable when 1-5 clean; record evidence excluding each prior step | |

1. Work in order; a one-line valued finding for each, including clean ones.
2. Any step firing sends the composite **back to P4 for re-pull**; never adjust in place.
3. Step 4 or 5 repairs belong to **#12** (structure) and **#29** (walls); this SOP names the defect and re-runs once repaired.
4. Write the result even when nothing fires.

### P8. The declaration decision and record (20 min)
1. **Human-mandatory.** Authority Matrix v2.0 row **"Sibling declarations (S-series)"**: PPC Lead decides, incoming operator executes, Brand Management owner reviews.
2. Confirm on the record's face: P4 inputs qualified or flagged; P6 computed with separation the reviewer accepts; P7 complete, all six steps; packet not degraded (G8).
3. Record **six fields**: root; declared owner; full composite table (both siblings' four inputs + sources); date; named re-arbitration triggers; every flag. Missing table = **F2**.
4. Compute **three re-arbitration triggers** for the non-owner, solving the composite for each input with the other two fixed: **CVR trigger = owner composite / (non-owner margin x non-owner depth); depth trigger = owner composite / (non-owner margin x non-owner CVR); margin trigger = owner composite / (non-owner CVR x non-owner depth)**. A trigger stated as a direction cannot fire.
5. Issue wall instruction to #29 same session (P9).
6. Update both siblings' **T2 block 8 "Term Owner (Family)"** to the owner and clear **T2 block 2 "Family Conflict"** on both, **only after wall confirmation returns**.
7. Log in **tab T6** with dated prediction (rule **V1**): metric, direction, magnitude, horizon. Standard prediction: **family blended CPC on the root** and **family rank capture**.

### P9. Wall issue and confirmation (10 min; same-day return)
1. Send #29 the declaration with the **full source list**: every non-owner campaign that **can** serve the root (broad, phrase, auto, sibling discovery), not only those currently serving.
2. Wall level, mechanics, reverse test are #29's (Ledger row 29). This SOP **does not specify negative match type**.
3. The wall covers the root, **not the non-owner's model-specific variants** (P10). Handing over modifier space produces F4.
4. Confirmation back the same day (#29's I-9). Until attached, the declaration is **drafted, not filed**.
5. Re-arbitration: two-sided instruction (outgoing owner's discovery gains the wall; incoming owner's loses it), dated to the change; removal routes through #29's removal control.

### P10. Non-owner posture and the modifier-space boundary (15 min)
1. State in the same words every time: **ownership is of the root, not of the modifier space that names the sibling.** (A 6-piece set does not lose its count modifier because a 4-piece owns the family root.)
2. Non-owner holds exact defence at floor on its model-specific variants (root + size/count/colour/model terms). Posture verdict **DEFEND AT FLOOR** (v4.0 13.1).
3. **Enumerate protected variants at declaration time** from T2 block 1 "Syntax Tags".
4. Floor value discovered/held by #28 ladder, executed by #12; this SOP sets no bid.
5. At every wall audit cycle, read the non-owner's impressions on enumerated variants; collapse after a wall build = **F4** (wall one level too wide).

### P11. Twin-set registration and sequencing (15 min per family)
1. Read **T2 block 1 "Twin-Set ID"** for every term under the root on both siblings (normalised-token signature; plural/word-order variants share an ID).
2. Register in the **A1 twin-set registry**.
3. Pool evidence across the twin set for sufficiency **before** the P4 CVR read (G2).
4. Sequencing: **family-level experiments do not run simultaneously on twinned structures**; when one twin changes, flag the other for a read.
5. Record twin-set state on the declaration.

### P12. Re-arbitration on a named driver (45 min)
1. Confirm the trigger vs the record's numbers; a driver that moved but did not reach its trigger is noted at quarterly review only.
2. Re-run **P4 in full** on current inputs for both (no carry-forward; mixed windows are not a comparison).
3. Re-run **P7 in full**.
4. Re-run P6; the transfer log carries **both tables side by side**.
5. Owner changes: walls move the same day (P9 step 5); push rights transfer. Owner holds: re-date with refreshed table and new triggers (a real outcome).
6. Update T2 block 8 on both siblings; log transfer in T6 with fresh prediction.

### P13. Temporary stewardship on owner stockout (25 min at grant; 5 min/day while live)
1. Re-point first: under rule **L9**, a thinning variation re-points ranking spend to declared backup (#12's move). Stewardship only when D2 backup chain cannot carry the root.
2. Compute and record both composites at grant. State explicitly: **the steward's advantage at grant is an inventory artifact, not an ownership case.**
3. Reversion date at grant = **owner's confirmed restock + recovery period read from #24** (AM-3).
4. Grant record, **five fields**: root, steward, grant date, reversion date, owner's restock ETA used. Missing reversion date = F5 at writing.
5. Issue walls per P9, dated to grant **and** reversion (reversion move pre-staged).
6. Check reversion date daily vs restock state; if ETA moves, reversion moves, logged.
7. At reversion, root returns to owner. A stronger steward is a P12 case **after** reversion. "Stewardship never converts to ownership by continuing."

### P14. Quarterly review, register maintenance, escalation (90 min per quarter across account)
1. Read every live declaration vs its triggers on current inputs (driver check, not re-arbitration); output list of declarations whose drivers passed a trigger without P12.
2. Route each to P12.
3. Re-date held declarations with refreshed composite table.
4. Reconcile register vs instrument: every A1 contested root has a finding; every finding has a state; every declared root reads the same owner in A1 and both T2 block 8 cells. **Disagreements resolve in favour of the declaration record**; divergence logged.
5. Review artifact = **register diff**: declarations added, changed, re-dated, unchanged, with composite share each.
6. Escalate on: (a) any finding open past deadline, with days-open counted; (b) any declaration re-arbitrated **twice inside one review period** (structural signal). No v4.0 escalation clock (AM-12).
7. Route validated amendment items to the threshold owner per Matrix row **"v4.0 threshold changes"** (CEO decides; PPC Lead executes and reviews).

**Cadence summary:** P1 weekly with Monday cascade; P2, P3, P4, P6, P7 on finding, same cascade; P5 across 2-3 cycles; P8-P11 on declaration, same session, walls same day; P12 on named driver; P13 same day on exhausted backup chain then daily; P14 quarterly.

## 5. Rules, thresholds and numbers

| Value | Meaning | Source |
|---|---|---|
| Composite = Margin $/order x Root CVR x Depth days | Relative index, no currency | A1 instrument |
| Share of Composite | Each sibling's composite / total | A1 |
| Triggers = owner composite / (product of non-owner's other two inputs) | Equality points; no tolerance in v4.0 (AM-8) | P8 step 4 |
| Path B ceiling = unserved margin x unserved depth x highest family CVR on root | Probe vs declare decision | P5 |
| **50 clicks** | Closed-vocabulary cap on deliberate test (tranche 1) | KDR / v4.0 FUND DELIBERATE TEST (50-CLICK CAP) |
| G2 CVR sufficiency bar | Tranche 2 target (WE-3 treats 100 clicks cumulative as clearing) | G2 |
| G2 buckets 7, 30, 60 days | Sufficiency buckets (cited in AM-5) | G2 |
| Effective TOS CPC = bid x (1 + TOS multiplier) | P7 step 2 | |
| Max profitable CPC = margin x CVR | P7 step 2 ceiling | |
| BE ACOS = contribution / AOV; Target = 50%; Max Acceptable = 75% | Implied by WE-1 (35.0031% / 17.5015% / 26.2523%) | |
| X6 / S-B1 divergence trigger | Same-term sibling CPC divergence ratio. Numeric ratio **not stated** in this SOP; instrument flag set higher (AM-11). WE-2 2.19x is above both | X6, S-B1 |
| Rolling four quarters | Scan record retention | Section 8 |
| One year after close | S-series finding retention | |
| Two years | Stewardship grant record retention | |
| Four quarters | Quarterly register diff retention | |
| Permanent | Declaration record; T6 | |
| Twice inside one review period | Re-arbitrations triggering structural review / escalation | P14, 10.1 |
| ~a dozen per year across five brands | Declaration frequency | 1.4 |
| 4 consecutive scan records | Week 4 ramp evidence | Section 11 |

### v4.0 IDs referenced
| ID | As described |
|---|---|
| G2 | Sample sufficiency; twin sets pool |
| G6 | Inventory adequacy (depth term; RED to P13) |
| G8 | Packet completeness (degraded = flag, no declaration) |
| G9 | Price stability / provisional margin |
| G11 | Sibling conflict: portfolio call assigns lead + support-or-stand-down posture |
| G12 | MKL hygiene (v4.0) / event freeze (corpus alias) |
| G3 | Budget truncation (FIX BUDGET); root CVR void across truncated period |
| X4 | Traffic deficit condition |
| X6 | Fixed inspection order; sibling CPC divergence trigger |
| X12 | Incrementality mechanism |
| L3 | Placement condition (PLACEMENT FIX FIRST) |
| L9 | Thinning variation re-points ranking spend to backup |
| M5 | Lead by M5 value; tiebreak margin-dollar class + earning-potential class |
| P9 | Precedence rule binding a declaration on two products' plans |
| V1 | Prediction required; unscored actions do not accumulate |
| J7 (Section 13.3) | Flags in the same words the engine computed |
| S-B1 | Divergence trigger |
| S-B2 | Assign lead by M5 value; tiebreak margin-dollar class + inventory depth |
| S-B3, S-B5 | PORTFOLIO CALL: ASSIGN LEAD scenarios |
| S-B4 | Consolidate duplicates cross-map |
| S-R3, S-R7, S-R13 | Traffic deficit / placement / recovery push cross-maps |
| S-D1 | Defend posture |
| S-C1 to S-C6 | Conquest |
| Section 16 Worked Pass 2 | The satin divergence incident |

### Verdict mapping (Section 5): KDR v3.0 25 strings with v4.0 13.1 cross-map
| KDR verdict | v4.0 cross-map | Arbitration execution |
|---|---|---|
| QUARANTINE: DATA REFRESH | FLAG: DATA REPAIR | No composite on quarantined row; finding open, guards armed; record which input blocked (refresh is Data Operations') |
| UNLOCK TRAFFIC | Absent; nearest EXTEND TEST at sufficiency branch | Contested: held by P3 step 1. Declared: #12 on owner only |
| FIX BUDGET (TRUNCATED) | None; condition is G3 | No guard block (gate lever, not escalation); root CVR void across truncated period |
| CONTINUE TEST TO 50 CLICKS AT CAPPED BID | FUND DELIBERATE TEST (50-CLICK CAP) | P5 tranche-1 verdict; this SOP designs probe; #12 executes |
| FUND TEST (UNFUNDED PRIMARY) | FUND DELIBERATE TEST (50-CLICK CAP) | P5 opening verdict where unserved sibling never funded root |
| RANK PUSH: FUND SIZED PUSH | RANK PUSH AT CONTROLLED CPC | Blocked on contested root; released only to declared owner |
| RECOVERY PUSH | RANK PUSH AT CONTROLLED CPC at S-R13 | Same; under stewardship belongs to owner after reversion, never steward |
| TRAFFIC DEFICIT: FEED TO REQUIRED CLICKS | None; X4 and S-R3 | Held while undeclared; declared: owner only |
| FIX CONVERSION FIRST; DEFER PUSH | Same | Recorded; written as re-arbitration driver (moves CVR) |
| PLACEMENT FIX FIRST | None; L3 and S-R7 | Often P7 step 2 output; composite returns to P4 after fix |
| RE-POINT VARIATION | Same | Runs before stewardship reachable; successful re-point holds ownership, moves depth |
| TAPER: RANK ACHIEVED, STEP BIDS DOWN | TAPER TO FLOOR (POST-OBJECTIVE) | No effect on ownership (no input is a bid) |
| HOLD; DEFEND LIGHTLY AT RANK | None; inside DEFEND AT FLOOR and S-D1 | Recorded as owner's post-objective posture |
| DEFEND AT FLOOR | Same | Non-owner posture at P10 on enumerated variants |
| BID DOWN TO PROFITABLE CPC; CAP SYNTAX | Same | P7 step 2 repair; ownership is not a licence: owner above its ceiling still carries it |
| INCREMENTALITY LADDER | None; X12 | #35; live test suspends P4 CVR read |
| ADD EXACT + RESTRUCTURE | Same | Often P7 step 4/5 repair; #12; composite re-runs after validated window |
| CONSOLIDATE DUPLICATES | ADD EXACT + RESTRUCTURE at S-B4 | P7 step 4 repair; #12 survivor rule |
| GRADUATE FROM DISCOVERY | GRADUATE + STEER (C10) | Interlock: graduation on root another sibling owns held until declaration read (#30) |
| NEGATE (PRE-LOAD / REACTIVE / STEERING) | CUT / NEGATE (C10) | Wall class caused at P9, moved at P12; #29 owns |
| ENTER SBV ARBITRAGE | FORMAT SUBSTITUTION (SBV/SD) | Does not resolve ownership; #17-19 |
| OPEN / ROTATE / EXIT CONQUEST | None; S-C1 to S-C6 | #16; sibling ASIN in conquest list = catalogue defect |
| STOP-LOSS: CONCEDE OR DEFER | Same | Does not close finding; driver watch. **Live cycle-1 verdict on the Bamboo root** while undeclared |
| PAUSED-PENDING (REASON + RE-ENTRY) | PAUSE (LEVERS EXHAUSTED) | Never closes a finding |
| LEAVE TO HARVEST | Same | **The one verdict that closes a finding without a declaration** (declined-and-logged); coverage state written to both **T2 block 1 "Coverage State"**; guards lift |

**v4.0-only strings issued (quoted from v4.0 13.1):**
| Verdict | KDR member | Execution |
|---|---|---|
| **PORTFOLIO CALL: ASSIGN LEAD** | None (C18) | The verdict this component exists to issue (S-B2, S-B3, S-B5): P8 in full. Human-mandatory |
| CONTINUE; VERIFY MOMENTUM | None (C18) | P14 where drivers held; declaration re-dates |
| **EXTEND TEST** | None (this session's finding, same shape as C18) | P6 when composites have not separated; P5 when tranche below sufficiency. Guards hold; re-read dated |

Retired v1.0 strings (members of no vocabulary): **DECLARE OWNER, PROBE FIRST, RE-ARBITRATE, TEMPORARY STEWARDSHIP, GUARDS IN FORCE**. The stewardship grant, guard-in-force state and re-arbitration outcome carry no string (AM-10); recorded as gate outcomes on the finding.

## 6. Data inputs required
- **Account Rollup Workbook v1.0**: **tab A1** (family grid, composite formula cell, Share of Composite, divergence flag column, S-series findings, declaration register, scan log beneath family grids, twin-set registry, stewardship section, A1 family definition); **tab A2** (cross-product funding queue); **tab A3** (verification scoreboard).
- **Product Command Workbook (each sibling)**:
  - **T2 block 1**: "Twin-Set ID", "Syntax Tags" (root|size|colour|attribute), "Coverage State".
  - **T2 block 2**: "Family Conflict", "Inventory Band", "Days to Stockout" (with SKU), "Targeted Variation(s)".
  - **T2 block 4**: organic rank, target rank.
  - **T2 block 5**: cross-type clicks, orders, spend on root.
  - **T2 block 6**: "Margin $/Unit", "Max Profitable CPC", "Expected CPC", "Cost to Close Gap $".
  - **T2 block 7**: "Objective"; test status and stop date for probes.
  - **T2 block 8**: registry counts (exact, phrase, broad, auto, SB/SBV/SD/PAT), "Duplicate Flag", "TOS Modifier %", "Sibling CPC View (D6)" (pending build), "Term Owner (Family)"; current bid, suggested bid and gap.
  - T2 Row Type = KW filter; campaign child rows and **search-term join**.
  - **T3**: state, daily budget, bid, "Objective Tag", "Bidding Strategy", "Placement Mult TOS %".
  - **T4**: "Effective TOS CPC $".
  - **T6** decision log; **T7** manifest statuses for B5, B8, D2, A2, A3, B3 (and account Expected CPC reference).
  - **T0 zone H** funding queue.
- **Economics and Context Pack v1.0**: **tab D1** (Contribution $/unit, Version stamp, per variation; blended row); **tab D2 "Keyword-Variation Map"** (Preferred SKU, Backup SKU, status, backup chain).
- **Raw Pull Pack** (search-term and impression-share joins), Monday 06:00.
- #22 launch handoff keyword set; #32 armed event plan; #29 wall confirmation line; #24 confirmed restock date + recovery class.
- PPC Command Workbook TEMPLATE v1.0.

## 7. Outputs / artifacts

| Artifact | Storage | Retention | Consumer |
|---|---|---|---|
| Weekly scan record (date, tested-root count, source per finding) | A1, scan log beneath family grids | Rolling four quarters, then archived with register | PPC Lead at P14; F12 detection |
| S-series finding + evidence snapshot | A1, instrument format | Open until declaration or declined-and-logged; **one year after close** | #23 push-block precondition; P14 |
| Composite table (four inputs, source cell refs, share) | A1 family grid row | Every version retained; re-arbitration appends | Declaration; BM review; P12 |
| P7 inspection record (one valued line per step, all 6) | Attached to finding | Life of declaration | #12, #28; F8 detection |
| Declaration record (composite table, 3 triggers, flags, wall confirmation) | A1 declaration register | **Permanent**; superseded retained | #29 walls; #23 push release; #12 G11 check; both workbooks' owner cells |
| Term owner / family conflict cells | T2 block 8 and block 2, both siblings | Live; history in decision log | #12 G11 check; weekly pass |
| Probe design and result | Attached to finding; campaign rows in executing product's T2 block 7 with test status and stop date | With finding | P4; #12 |
| Stewardship grant (5 fields) | A1 stewardship section | **Two years** | #29 dated wall moves; #24; daily check |
| Twin-set registry | A1, mirrored to T2 block 1 | Live | G2 pooling; #12 and #29 one-strategy rule |
| Decision-log entries (rule/scenario ID, prior/new, expected outcome, review date) | T6, append-only | Permanent; cycle file snapshot | V5 at #6; Account Rollup A3 |
| Quarterly register diff | A1 | Four quarters | PPC Lead, BM owner; P14 step 7 |
| Amendment register | Section 10.3 of this SOP | Until resolved | v4.0 threshold owner |
| Composite Worksheet Card (Appendix A) | Field order for A1 grid row | | |

Gate artifacts: a declaration's is its record with wall confirmation; a cycle's is the scan record; a quarter's is the register diff; a stewardship's is its reversion, executed and logged.

**Appendix A Composite Worksheet Card fields:** ROOT, FAMILY, FINDING OPENED, DEADLINE; per sibling: Margin $/order + src [G9 flag Y/N], Root CVR (orders/clicks = %) [sample state], Inventory depth days + SKU [D2 mapped Y/N], Window (same both sides Y/N); COMPOSITE; SHARE; separation %; P7 lines 1 tags, 2 eff TOS CPC, 3 strategy, 4 duplicates, 5 variation, 6 auction; triggers CVR/depth/margin; DECLARED OWNER, DATE, WALL CONFIRMED, T6 PREDICTION; NON-OWNER PROTECTED VARIANTS.

Alarm routing: same day to operator queue **F1, F3, F5, F9**; to PPC Lead with void record **F2, F8, F11**; to #29 wall audit **F4**; weekly worklist **F6, F7, F10, F12**. Evidence-line: root, two siblings, signal value, gate/rule ref.

**Skill refusal conditions** (no declaration draft): unqualified composite input; degraded packet; incomplete P7 record; probe tranche below sufficiency bar; separation the operator has not accepted.

## 8. Decision rights
- **"Sibling declarations (S-series)"**: **PPC Lead decides** every declaration, re-arbitration, stewardship grant; **incoming operator executes**; **Brand Management owner reviews** at daily huddle (**review, not veto**; disagreement routes up, never into parallel spend).
- **"Push funding (the M5 queue)"**: guard state from this SOP; funding release PPC Lead within envelope, **CEO above it**.
- **"Structure creation (all SOPs)"**: wall issue and twin-set registration execute against a PPC Lead decision.
- **"v4.0 threshold changes"**: CEO decides; PPC Lead executes and reviews.
- **"Weekly verdicts (established US)"**: incoming operator executes within assigned scope; scan rides the cascade.
- Human-mandatory without exception: every declaration, re-arbitration outcome, stewardship grant, probe standup, post-declaration wall instruction.
- AI-executable with audit: scan, intake and snapshot, input assembly, composite and share, trigger solves, P7 read, reversion arithmetic, P14 drift detection, register diff.
- Vacancy rule: D reverts to PPC Lead, E to PPC Manager.
- Ramp: Week 1 reproduce A1 live composite cell by hand to two decimals, list open findings with deadlines/days-open; Week 2 supervised full sequence on one root; Week 4: four consecutive scan records with no gap, one finding to filed declaration with same-day wall confirmation, one correct refusal. Declarations remain human-mandatory permanently (not a ramp stage).
- Escalation: F1, F5 first occurrence; F9 on deadline with days-open; F2, F8, F11 to PPC Lead; F4 to #29 audit; second occurrence of same mode on same family in one review period escalates regardless.

## 9. Account-specific facts
- **Account Rollup tab A1 live cell: Bamboo 4-piece composite 58.3358125** (= 28.37 x 0.04375 x 47).
- **Live B4 Family Conflict reading: "OPEN: shared with B6 sibling, owner undeclared".**
- **Live B4 Days to Stockout: 47 days on KING-WHITE preferred SKU.**
- The **Bamboo root sat open across the first cycle** with the declaration cell reading pending entry (F2 motivating incident). The **live cycle-1 verdict on the Bamboo root was STOP-LOSS: CONCEDE OR DEFER**.
- Root **"bamboo sheets"**: SV **101,819**, primary syntax, purchase intent, oversight flag Y; live in two family siblings (4-piece and 6-piece). 4-piece economics (live, from D1): contribution **$28.37**/order, AOV **$81.05**, BE ACOS **35.0031%**, Target 17.5015%, Max Acceptable 26.2523%; root CVR **7 orders / 160 clicks = 4.375%**; depth **47 days** (KING-WHITE); margin from **blended row**, so G9 PROVISIONAL. Root spend **$522.05** on 160 clicks = CPC **$3.26** vs max profitable CPC **$1.24** (2.63x ceiling); CPA **$74.58**; root ACOS **92.02%**; **organic rank 39 vs target 4**; recorded **cost to close gap $88,495**. The 6-piece workbook has **not run a cycle** (6-piece figures illustrative: $41.60, 2.91%, 39 days).
- **Satin divergence incident** (v4.0 Section 16 Worked Pass 2; also v4.0 Section 1 named failure): **"satin sheets queen"** Product A CPC **$3.24**, rank 17; Product B CPC **$1.48**, rank 6; ratio **2.19x**; neither tagged. A: TOS +180% on $1.75 base (effective TOS $4.90); up-and-down vs B fixed; one legacy duplicate exact on A; A advertised parent rather than D2-preferred king variation (contribution **$19.85** vs blended **$34.10**).
- Live workbook shows **twin folds executed on cooling and bamboo roots in a single cycle**, several with reporting rolled under a parent after the fact (F10).
- Live **D1 table carries a blended row with a version stamp; variation rows still unfilled**, so **every current composite runs provisional** (F11).
- **"Sibling CPC View (D6)"** is a pending build; Source B (search-term join) carries detection.
- Ledger dependency **D2 OPEN**.
- Account has **five brands**.

### Worked examples (summary)
- **WE-1 Bamboo**: 4-piece 58.34 vs 6-piece 47.21 (41.60 x 0.0291 x 39); lead 11.12 (23.56% of 6-piece); shares **55.27% / 44.73%**. P7 all clean. Triggers: CVR **3.60%** (3.5956%), depth **48.19 days**, margin **$51.40**. Walls on 6-piece: family broad, family phrase, both autos, sibling discovery. 6-piece keeps count-modifier space at DEFEND AT FLOOR. Owner still carries BID DOWN TO PROFITABLE CPC; CAP SYNTAX.
- **WE-2 Satin**: pre-inspection A 103.32 (34.10 x 5.2239% x 58) vs B 60.17 (26.40 x 4.4693% x 51), share 63.19/36.81. Steps 1-5 all fire. Corrected A 60.14 (19.85 margin) vs B 60.17; share 49.99/50.01, gap **0.0264pp**, so **EXTEND TEST**. A's ceiling $1.04; effective TOS 4.73x; observed CPC 3.12x. Five repairs staged. A **42% error in one input produced a 71-point swing**.
- **WE-3 Probe (illustrative, Cooling root)**: C = 22.90 x (9/232) x 63 = 55.97; D ceiling = 31.20 x 0.0388 x 52 = 62.94 > C, so Path B illegal, probe mandatory. Expected CPC account reference **$2.80**. Tranche 1: 50 clicks, $140.00, 2 orders (4.00%, thin). Tranche 2: cumulative 100 clicks, 5 orders, 5.00% (clears). D = 81.12; share 59.17/40.83. Probe cost $280.00, contribution recovered $156.00, net **$124.00**.
- **WE-4 Stewardship ("bamboo sheets full size")**: owner 4-piece FULL preferred SKU 18 days cover; gate armed **2026-07-10** at projected 14 days; projected stockout **2026-07-24**; owner $28.37, CVR 4.12%; steward 6-piece $41.60, 3.33%, 51 days. At grant: owner 21.04 vs steward 70.65 (steward ahead 235.80%). Restock **2026-08-14** + #24 recovery **21 days** = reversion **2026-09-04**; grant 42 days. Post-reversion owner depth 74, so 86.49 vs 70.65; share 55.04/44.96. Depth-only swing **4.11x**.

## 10. Open items

### Amendment register (Section 10.3, 12 items)
| ID | Gap |
|---|---|
| **AM-1** (highest) | No minimum composite separation; S-B2 vs M5 tiebreaks disagree. Dead heat = EXTEND TEST with guards held |
| AM-2 | No declaration deadline interval (only the instrument's family-grid review cadence) |
| AM-3 | No stewardship reversion interval distinct from #24 post-restock recovery |
| AM-4 | No inventory-depth floor for ownership eligibility |
| AM-5 | No composite recency window (instrument cycle window vs G2 7/30/60 buckets) |
| AM-6 | No qualified-traffic definition for root CVR (auto/broad vs exact-only) |
| AM-7 | Probe sizing has no matching verdict string (50-click cap vs G2 CVR sample) |
| AM-8 | No minimum driver movement / tolerance around trigger equality points (churn risk) |
| AM-9 | Review cadence stated at two intervals (quarterly here vs monthly term-owner review in instrument layer) |
| AM-10 | Three arbitration states carry no verdict string; EXTEND TEST is a fourth string absent from KDR 25 |
| AM-11 | Divergence trigger stated at two ratios: X6/S-B1 one ratio; instrument family-grid flag higher, so it fires later and the intermediate band goes undetected |
| AM-12 | No escalation clock on overdue finding |

### Conflicts / dependencies
- **C3** (#31 no procedures), **C9** (gate numbering, G12), **C10** (vocabulary; GRADUATE + STEER, CUT / NEGATE), **C18** (v4.0-only strings; this SOP adds EXTEND TEST as a third).
- Ledger row 33 still carries the superseded SOP-29 sibling-wall procedure number (P5; moved to P7 in SOP-29 v2.0).
- #29 and #23 were rebuilt after the copies attached to this session; counterpart contracts cited by Ledger row.
- **D2** variation map OPEN; per-variation margin table not landed (G9 provisional everywhere).
- "Sibling CPC View (D6)" pending build.

### Version-governance triggers (10.1)
A1 formula/factor/grid/finding-format change; v4.0 increment touching G11, Section 8.11, M5, P9, 13.1; resolution of C10 or C18; D2 landing; per-variation margin table clearing G9; any new sibling or family reorganisation; increment to #29 or #23; two re-arbitrations on one root in one review period (structural review of the family instead of a third arbitration).

### Interface contracts (18)
| ID | Direction / party | Non-arrival |
|---|---|---|
| I-1 | Data Operations Raw Pull Pack joins (Mon 06:00 / 09:00) | Scan cannot run on working source; no new findings; F12 |
| I-2 | Finance via D1 (monthly true-up + on cost/fee event) | Blended margin + G9 PROVISIONAL |
| I-3 | Logistics and Catalog via D2 (monthly / assortment change) | Depth at product level; structural cap (D2 OPEN, largest cap) |
| I-4 | Data Operations via T2 block 2 (daily) | Live grants **suspend** |
| I-5 | Data Operations via A1 (Mondays after cascades) | No instrument; no declaration; **computing composite outside instrument prohibited** |
| I-6 | Data Operations via T7 (weekly) | Every composite becomes a flag |
| I-7 | #22 launch handoff | Newcomer bids family roots undetected; highest-risk window |
| I-8 | #32 armed event plan | Window adjudicates ownership by accident; root held out of window if unnamed |
| I-9 | #29 same-day wall confirmation (its I-9) | Declaration drafted; gate cells open; F3 |
| I-10 | #24 restock date + recovery class | Grants not issued |
| I-11 | To #23 guard state / declaration (its I-3) | Indefinite hold on both siblings |
| I-12 | To #29 declaration + full source list (its I-8) | Declaration cosmetic |
| I-13 | To #12 T2 block 8 / block 2 cells | G11 check scales undeclared root; divergence pattern re-forms |
| I-14 | To #12, #29 twin-set IDs | Sufficiency fails; manufactured probe case; negatives fail to propagate |
| I-15 | To A2 funding queue exclusion list | Queue funds a forbidden push |
| I-16 | To #6 V5 via T6 and A3 | Component never learns calibration |
| I-17 | To Brand Management owner (before filing) | F2 via review |
| I-18 | To v4.0 threshold owner (quarterly) | 12 ungoverned numbers persist silently |

### Failure modes (F1-F12)
F1 push open on contested root (escalate same day); F2 declaration by history (void); F3 walls lagging declaration; F4 over-walling the non-owner; F5 stewardship past its date; F6 stale composite; F7 composite on an imputed CVR (new); F8 auction explanation accepted before inspection (new; satin case); F9 finding open past deadline; F10 twins running split postures (new); F11 provisional margin without flag (new); F12 scan not run or on stale registry (new).

### Referenced documents
Master PPC Decision Criteria System v4.0; Account Rollup Workbook v1.0; KDR Template v3.0; PPC Authority Matrix v2.0; Master PPC Data Architecture v1.0; PPC Command Workbook TEMPLATE v1.0; Economics and Context Pack v1.0 (D1, D2); PPC Strategic Doctrine v1.0 (Section 5.2 case 4, Section 14); PPC Cross-Reference Ledger (v2.5 correction register); SOP Build Kit v1.0; SOP-6, 12, 16, 17-19, 22, 23, 24, 28, 29, 30, 32, 35, 38.
