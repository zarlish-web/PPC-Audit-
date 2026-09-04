---
name: ppc-plan-builder
description: >
  Build or update a standalone Amazon PPC product plan — from scratch, or by
  refining an existing plan against current data. Fully self-contained: does
  not require any other skill to be installed. It names `keyword-syntax-builder` in one place (§1B) as the source of a product's syntax taxonomy where one is being built from scratch; that is a pointer, not a dependency, and this skill runs without it.
  Covers intake, the decision order every row is judged in, objective
  assignment, a product-goal gate that decides whether ranking spend is even
  authorized, economic ceilings, per-placement bid/budget logic, the
  seven-state ranking progress test, the sufficiency stop that ends a ranking
  push, CVR baselines, ACoS reconciliation, inventory gating, SKU-provenance
  checking, the fixed-bid trial, the discovery-layer candidacy gate, the
  writing standard every verdict must meet, and reconciliation against a
  companion workbook if one exists. Trigger for "build the PPC plan", "make
  the product plan", "update the plan with new data", "does this plan match
  the workbook", or any request to decide, document, and justify a product's
  Amazon Sponsored Products/Brands strategy end to end.
---

# PPC Product Plan — standalone

This skill needs nothing else installed to run. Every rule a plan decision
depends on is stated here in full, not cited from elsewhere. If a workbook
already exists for the product, or gets built alongside this plan, the two
are checked against each other as part of this skill's own output rules
("Companion workbook" below) — that check doesn't require a separate skill
either.

**Forward-only, as a default.** A plan already delivered stands as
delivered. This skill's rules apply to the next plan built or the next
refinement pass explicitly requested — never a silent retroactive rewrite of
a plan someone already has, unless the user asks for that pass by name.

**A note on confidence, stated once here rather than repeated at every
rule:** this skill's rules fall into three tiers, and the plan should say
which tier governs a given decision when it matters. **Settled** —
corrected once already against a real mistake, safe to apply without
re-litigating. **Provisional, pending confirmation** — a reasoned rule
that hasn't been confirmed by whoever owns the account's standards yet.
**This tier is asked about before it's ever applied, not applied with a
flag attached.** An earlier version of this rule treated provisional as
"usable, but flagged as open when it drives a decision" — that was the
same mistake as the hold problem elsewhere in this skill: a genuinely
unconfirmed judgment call was being made silently and only labeled
afterward, which is not the same thing as actually confirming it. The
first time a provisional rule would drive a real decision on a product,
stop and ask whether to apply it as written, adjust it, or hold off —
**once answered for that product, the answer holds for every later cycle
on that same product without asking again**, tracked the same way any
other user override is tracked (§13B). This is not asking the same
question forever; it's asking it exactly once, at the point it first
matters. **Refinement proposed** — an existing, settled threshold with a
gap in how it's read (a missing near-miss state, an unresolved unit of
measurement), where the number itself isn't being questioned, only its
application; this tier follows settled's rule — it's the number that's
confirmed, not how it's applied. Each rule below states which tier it's
in.

**"Holds without asking again" is not the same as permanently frozen —
stated explicitly because the two can be read as identical when they
aren't.** The account's own standards genuinely change over time —
thresholds get revised, a prior call gets reconsidered, a number that
was right last quarter stops being right this one. A locked answer holds
until the person who confirmed it changes it, not forever regardless of
what changes around it. This works exactly like any other user
override: silence doesn't reopen the question, but an explicit new
instruction from whoever owns the standards always can, at any point, on
that same product — and once changed, the new answer holds the same
way the old one did. What this skill won't do is silently re-ask a
settled question just because a new cycle started, and what it also
won't do is treat an old confirmation as untouchable if the person who
gave it wants to revisit it.

**On a genuinely new product's first cycle, gather the likely
confirmations upfront in one batch rather than letting them surface one
at a time through the build — added to reduce
exactly the friction a first cycle otherwise generates.** Before
starting the build, scan what's already known about the product
(declared goal, category, whether any ranking terms are likely Cold
candidates, whether the family has shared terms with a sibling) and name
the provisional-tier questions this specific build is likely to hit —
the product-goal gate's nullification mechanics, the Defensive/Conquest
rules, the harvest mechanic, the discovery counting basis, the
sufficiency-stop exit mechanics, the graded push-sizing tiers — asking
what can reasonably be anticipated in one pass, before the build starts,
rather than each one interrupting mid-build the first time it happens to
apply. **This doesn't replace the ask-first rule for anything genuinely
unanticipated** — a provisional rule nobody could have predicted still
gets asked about the moment it first matters, same as always. It only
front-loads what's foreseeable, so a first cycle feels like one
conversation at the start rather than a series of interruptions spread
across the build. Once answered, every answer holds for that product
going forward, exactly as the rule above already states.

---

## Read this file in full before acting — the protocol, not the aspiration

**This file is read end to end before any action in a cycle, and that instruction is load-bearing rather than ceremonial.** The failures this file has actually produced were never gaps in it. Every one was a rule already written here, read once in the section the builder happened to open, applied in the one place that section discussed, and not carried to the second place the same rule governs. A builder working from a remembered summary will reproduce the summary's omissions exactly, and will do so confidently, because a summary of a rule reads like the rule.

**What reading in full means in practice, so it is done rather than claimed:**

1. **Read the section map first** — every `##` heading, in order. This is the index of what governs what, and it is what makes the rest navigable rather than a wall.
2. **Read every section that governs any decision this cycle will take**, word for word, before the first decision is written — not at the moment each decision comes up. Deciding what to read after you know what you want to do is how a rule that would have blocked the decision goes unread.
3. **Read the "contexts governed" line on every rule you apply**, and check each context listed against what you are about to write. A rule that names four contexts and gets applied in one is three-quarters unapplied.
4. **State, in the hand-off, which sections were read in full and which were skimmed.** "Ran the skill in full" is a claim a reader cannot check and a builder can make without it being true. Naming the sections is checkable.

**Where a cycle is genuinely too large to read the file end to end before every individual command, that is stated plainly rather than papered over** — and the sections governing the current action are still read in full, every time, from the file rather than from memory. The honest failure mode is a builder who says the file was run in full when what happened was a targeted read; the fix is not to pretend otherwise but to name the read that actually occurred.

### Three phases, because the plan is not one document written once

**The plan splits into sections that do not depend on the programme and sections that are the programme, and they cannot be written at the same time.** Analysis — the economics, the profitability diagnosis, the per-keyword mathematics, coverage with named declines, competitor position, the gaps register — rests on the account's data and is true before any decision is taken. The roster, the action plan, the five-property record, the expected outcome and the reconciliation are descriptions of decisions, and a description written before the decision is a forecast of what the builder expects to decide.

**Phase one: the basis, settled once, before either document produces a row.** Contribution per child with its unit sample named, the fee split that separates variable cost from allocated charge, the inventory zone per child, the routing per campaign read from its product-ad rows, measured conversion per placement, and the four bounds any bid will respect. **Every expensive correction on a real build was decidable here and surfaced late** — a contribution from two units that priced 597 rows, routing inferred from names that disagreed with the account's own product-ad rows on 212 of 251 campaigns, rank targets derived when 7,949 were supplied. None of those needed new data. They needed the basis settled before rows were produced against it.

**Phase two: the analysis sections of the plan, then the workbook.** The analysis sections are written from phase one and are stable — they do not move when the programme changes, and on a real build they were the only part that survived two full rebuilds intact. The workbook then decides the programme against that analysis.

**Phase three: the workbook freezes, and the plan's programme sections generate from it.** Not written alongside and reconciled afterwards — generated, from the frozen file, after it is final. A plan authored whole before the workbook exists describes a programme nobody has decided yet, and on a real build it described a two-term push at $17.10 a day while the workbook decided a 948-row programme. **Those sections were rebuilt twice, and the analysis sections were rebuilt never.** That difference is the whole argument for the split.

**What this does not change: the plan still opens the work.** A workbook cannot be built without the economics, the routing basis and the inventory gate, and those are plan-side analysis. The sequence is not workbook-first — it is basis, then analysis, then decisions, then the description of those decisions, in that order, with the freeze between the last two.

**Where a reviewer expects a complete plan before a workbook exists**, the programme sections ship as a marked addendum generated after the freeze rather than as first-draft prose. Say that is what is happening; do not fill them with expected decisions and correct them later.

### The reconciliation table is generated, never typed

**A plan and its workbook are one deliverable in two files, and the section that certifies they agree must be computed from one of them rather than written twice.** This is the engagement's terminal failure and it is worth stating precisely, because every decision in both files was sound when it happened. The plan reconciled against a workbook render; the workbook then advanced one render further — absorbing an enable decision, gaining three tabs and two gate checks — and neither file was wrong about itself. **The section titled "Figures to reconcile" certified agreement on twelve rows where six disagreed**, including a five-fold difference on the budget row and a hundred-row difference on the acting count. A reviewer who sets the two numbers side by side is holding the exhibit, and the exhibit is the certification layer.

**The rule is mechanical: the reconciliation figures are emitted from the workbook by the same code that runs its validation gate, so the plan's table and the gate output are one computation and cannot drift.** A plan that holds its own copy of the numbers has two accounts of one file, and two accounts diverge the moment either file moves. **Remove the second account and the class closes** — there is no "match" column to assert, because nothing is being compared: the plan prints what the workbook contains, read from the workbook.

**The plan's version stamp names the workbook file it was generated against, by hash.** Not the date, which two renders on the same day share, and not the filename, which does not change when the contents do. A hash makes the pairing checkable by anyone holding both files, and makes a stale plan self-evident rather than something a reviewer has to derive by re-deriving twelve figures.

**Freeze order, every round: the workbook renders last-and-final first, then the plan generates against it.** Any later change to the workbook, however small, invalidates the plan's reconciliation and the plan regenerates before either ships. **The two files never ship from different renders**, and a check that reads the plan against a fresh read of the workbook is what enforces it — the gate cannot certify itself, so that one check is scored outside the figure the plan prints.

### One verb, one operation, and the verb names the entity it changes

**An Action is an instruction to an executor, so it has to say what changes and on which entity — a verb that describes an outcome without naming the operation cannot be deployed and will be read differently by every person who reads it.** On a real build the verb `RE-ROUTE → BM-QUEEN-NAVY-BLUE` appeared on 503 rows and meant two entirely different operations. On 441 of them it meant *"this campaign already advertises Navy Blue — the campaign name says otherwise, and the bid has been re-derived against the child the product ads actually serve."* Nothing about the routing changed; only the bid moved. On the other 62 it meant *"this campaign advertises a child that cannot ship — enable Navy Blue's product ad and pause the current one."* Same words, same arrow, same destination format. **One is a re-pricing, the other is a structural change to what the campaign sells, and the file gave a deployer no way to tell them apart.**

**The consequence was that the second operation never shipped.** The decided file carried no Product Ad rows, so 62 campaigns keeping a bid priced for one child while advertising another read as complete and deployed as nothing. Worse than incomplete: the bid landed, so the file *looked* like it had worked while the spend kept going to the wrong product at a price computed for a different one.

**Rules that follow, and each closes a way this failed:**

- **The verb states the entity and the field.** `REPRICE (keyword bid)` and `SWITCH AD (product ad)` are different instructions; `RE-ROUTE` is a description of an intent that maps to either. Where a decision touches two entities, it is two verbs on two rows, not one verb hoping a reader infers the rest.
- **A verb that implies an entity the file has no rows for is a blocked decision, not a recorded one.** State it as blocked, name the entity the file lacks, and give it an owner — never let it sit as an action that reads as taken.
- **The reasoning template belongs to the operation, not to the verb.** The same sentence — "routes to X, read from the campaign's own product ad rows" — was correct on the 441 re-pricing rows and false on the 62 switching rows, where the product ads said something else entirely. **A sentence copied across two operations will be true of one and a misstatement of the other**, and it will pass every check that reads it as prose.
- **Where the same word covers two operations, rename one of them.** The cost of two verbs is a line in a legend. The cost of one verb is a reviewer who cannot tell what will happen, and a build that ships half of what it says.

**The test before any Action is written: could someone holding only this row and the account make the change, and would two people make the same one?** If the row does not name the entity, the field, and the direction, the answer is no — and every downstream file built from it inherits the ambiguity.

### A decided row that cannot deploy is not a decision

**Before a row is written, establish what has to be true for it to actually serve — and if that thing is not also being decided, the row does nothing.** A keyword priced, routed, reasoned and given a reversal condition still delivers nothing if its campaign is off. On a real build 525 rows were re-routed onto shippable children, each with a bid derived from that child's own contribution, and every one sat inside a campaign that stayed paused. The file reported them as the largest action in the programme. Deployment would have produced no change whatsoever on 525 of them.

**The failure was not the pricing — it was answering a lever question instead of the governing one.** Those campaigns each carried a campaign-level row, and that row asked *should the budget change?* Sixty-eight of them answered "budget held — not the binding constraint on a campaign with no delivery," which is true and beside the point. **The binding constraint was that the campaign was off, and nothing in the file asked whether it should be on.** A lever that was evaluated is not the same as the question that governs, and evaluating the wrong one produces a row that looks fully decided and changes nothing.

**Zero delivery is a fact to explain, not a reason to hold.** A campaign that never delivered because it was never enabled is not short of data — it is short of a decision. On that same build 233 of 238 paused campaigns had never served a single impression: built in earlier cycles and never switched on, not stopped after failing. Treating that as "no rate is decidable" holds a campaign for the absence of evidence its own paused state guarantees it can never produce. **Before recording zero delivery as a hold, establish why it is zero — never enabled, budget-blocked, ineligible, or genuinely tried and failed — because only the last of those is a performance verdict.**

**Every row states what must also happen for it to serve, and where that is another row, the two are decided together.** A keyword enable inside a paused campaign, a modifier on a campaign with no budget, a re-route onto a child with no inbound stock: in each case the row's own verdict is conditional on a second decision, and the file has to carry both or say plainly that the row is prepared rather than deployed. **"Prepared, not deployed" is an honest verdict; a row that reads as deployed and is not is a false one.**

### The account already supplies the answer more often than not

**Before deriving any value, look for the column that already holds it.** This is the most expensive
defect class this file has recorded, because a derived value looks exactly as authoritative as a
supplied one and nothing in the output distinguishes them. Four separate instances on one product,
each caught only when a reviewer asked why a number looked wrong:

- **Rank targets.** Derived from search-volume tiers, giving 10 / 15 / 20 / 30. The account's own
  keyword list carried a `rank targets` column populated on 7,949 rows with values of 3 to 8 — far
  more aggressive, and the number the account actually manages to.
- **Branded terms.** Screened with a hand-written pattern that caught one brand and missed five
  others sitting in the launch list. The keyword list carried a Final Categorization column marking
  994 terms Branded.
- **Routing.** Inferred from campaign names, which disagreed with the account's own product-ad rows
  on 212 of 251 campaigns — one campaign named for a single child was running fifteen.
- **Suggested bids.** Treated as unavailable and deferred to a later stage, when the ranges were a
  file away and the whole bid decision was blocked on them.

**The test before deriving anything: does a supplied column, export or file already answer this, and
have I opened it?** A derivation is a fallback for when the account has no answer, not a shortcut
past reading what it has. **Where a value is derived because no supplied source exists, say so on the
row** — "derived from search volume because no rank target is supplied" is checkable; a bare number
is not, and reads as though it came from the account.

**A supplied column that looks wrong is a finding to raise, never a reason to quietly substitute your
own.** The relevancy column on this product genuinely was wrong — it marked bamboo cooling terms Not
Relevant on a bamboo cooling product. The right response was to judge relevance against the listing's
own attributes and say that is what was done; the wrong response, equally available, would have been
to invent a relevancy score and let it read as the account's.

### The gate runs as code, not as a reading

**This skill ships with `references/anti-patterns.md`, and it is not
optional reading.** It lists the failures this file exists to prevent,
each with what it looked like in a real delivered document and what
catches it. **Read it before a build, not after one fails** — a rule
buried in a long section is hard to recognise in the moment, and the
sixteen shapes there are recognisable on sight. The executable gate ships
with the companion workbook skill and is run against the delivered file,
never the working state.

**Reading this file end to end before a build does not, on its own, prevent the failures this file keeps recording — and the evidence is that the instruction to do so has been added three separate times while the same classes of defect kept shipping.** Every rule below existed, in this file, before the build that broke it: the per-SKU sanity bound, forward-cash economics on aged stock, the exhaustive list for a silent hold, the same-day re-point on Red, routing read from product ads rather than campaign names. None was missing. Each was read, understood, applied in one place, and not carried to the second place it governed. **A rule held in a builder's head while they work is a rule that gets applied where they happen to be looking.**

**So the enforceable form of this file is a check that runs against the finished artifact, and every rule stated here that can be expressed as a check is written as one.** Not a reminder to look — a query that returns a number, run against the delivered file, whose non-zero result blocks delivery. The checks that have actually caught defects on this account, each of which a careful read had already missed: bids above the routed child's affordable price; modifiers written on keyword rows where the platform reads them on bidding-adjustment rows; correction steps exceeding the single-step cap; effective top-of-search prices above what a unit earns; rows of an entity carrying no verdict; holds citing no reason on the exhaustive list; spend routed to a child below the routing-switch threshold; reasoning strings repeated verbatim across rows; superseded figures surviving a correction.

**Three properties make a check worth having.** It reads the delivered artifact, not the working state, because the two diverge and only one ships. It returns a count rather than a judgment, so its result is not itself a thing to be interpreted. And it is demonstrated to fail against a known-bad case before it is trusted — a check that has never been seen to fire has not been shown to test anything, and on a real cycle three checks reported clean because the defect had been injected into one row that each overwrote in turn.

**The checking tool is itself checked, because a broken check reports success.** This is not a
hypothetical: on a real cycle the harness accepted a file path only after a `--file` flag, and a path
given plainly was silently discarded in favour of a hardcoded default. It printed "32 of 32 checks
pass" against a file nobody had asked about, while the file actually under review failed seventeen
times. Nothing in the output distinguished the two — a passing report on the wrong artifact looks
exactly like a passing report.

**Three properties, each of which has failed here at least once:**

- **It reads the artifact it was asked to read, and refuses rather than substituting.** A tool that
  falls back to a default when handed something it cannot open will eventually report on the wrong
  file, and the report will look clean. An unreadable input stops the run.
- **Its known-bad cases still fail.** An injector is written against a file's shape, and the shape
  moves — one stopped firing because it looked for a row type that a later hand-edit no longer
  contained, and reported BROKEN rather than quietly passing only because the self-test asserts that
  every injector fires. Injectors are re-run whenever the file structure changes, not only when a
  check is added.
- **Each defect is injected into its own row.** Three checks once reported clean because all three
  defects went into the same row and each overwrote the last.

**When a check fires, diagnose before believing it.** A failing check is a claim about the data, and
the claim is sometimes wrong: one flagged 59 rows by reading campaign names instead of actual
routing; another demanded full sizing on rows deliberately screened out of a launch; another rejected
formula cells that were the correct answer. **Fixing the data to satisfy a wrong check is worse than
having no check, because it moves a correct file toward a defect.** Read what the check actually
tests, confirm the rule it claims to enforce, then decide which of the two is wrong.

**Checks are re-run after every change, in dependency order, never once at the end.** Levers feed each other: a staged base moves the effective top-of-search price, a re-route moves the per-unit bound, a recovered routing makes a previously-uncomputable modifier computable. **A check that passed before the last edit says nothing about the file that ships.** On this account the same class of breach appeared three separate times, each time only after a downstream lever moved, each time invisible to a check run in the wrong order.

**Where a rule cannot be expressed as a check, it says so and names what a reviewer must read for.** Judgment calls — whether a hold is a mechanical fact or a decision nobody made, whether a term genuinely belongs to a sibling — cannot be counted. Those are the rules that earn a careful reading, and separating them from the countable ones is what makes the reading tractable.

## A rule names every context it governs

**A rule stated inside one section is silently assumed to govern only that section, and that assumption is where this file has failed repeatedly.** Four real cases, each a rule that was present, correct, and read: the attribute-match routing rule sat inside new-launch selection and was applied to new launches only, so a reactivation routed "white cooling sheets" to a black child; the multi-lever rule sat in the lever hierarchy and was applied to reactivations only, so live rows shipped carrying a bid and no budget or modifier; the click floor was applied at campaign level and not at placement level, so a single click reading as 100% conversion produced a $24.67 bid; and the tab-placement rule sat in the output structure while the writing standard never pointed at it, so live-row actions were written to the planning tab and new-launch actions to the decided file, exactly backwards.

**Every rule that governs more than one context names all of them, inline, in the rule itself.** Not in a cross-reference, not in an index elsewhere, not left to inference from where the rule happens to sit. The reader applying it must be able to see the full list of places it binds without leaving the paragraph. Where a rule genuinely governs one context only, it says so, so that silence is never ambiguous between "one context" and "nobody listed the rest."

## Read this file in full before acting — not the section you think you need

**Every command that decides, builds, or changes anything starts by reading this file end to end.** Not the section that seems relevant, not a summary written on a previous turn, not a procedure note carried between sessions. The file itself, every time.

**The reason is specific and it is not diligence theatre.** A rule almost always governs in more than one place, and reading only the section in front of you finds it in one of them. On a real build this produced four separate defects in four consecutive cycles, every one of them a rule already written here: the decided-file rule was read once and applied to the wrong tab; the multi-lever rule was read in §4A and then not applied to reactivation rows; the fifteen-click sample floor was applied at campaign level and not at placement level, which produced a $24.67 bid from a single click; the attribute-match rule was applied to new-launch routing and not to reactivation routing, which sent a query naming white to a black SKU. **None of these was a gap in the file. Every one was a rule read in one place and not carried to the second place it governed.**

**A summary of this file is not this file, and the difference is exactly where the defects live.** A summary keeps what its author noticed. The rules that get missed are the ones that did not seem to apply at the time — which is precisely the set a summary drops. Where a working note or procedure file exists for a product, it records what was *decided*, never what the rules *are*; the rules are re-read from here each cycle.

**Two habits that follow from this, both non-negotiable.** First: after applying any rule, ask where else it governs in the work in front of you, and apply it there in the same pass — routing rules govern reactivation as well as launch, sample floors govern placements as well as campaigns, lever rules govern every entity type the change touches. Second: never let a rule you already know stop you re-reading its section, because the failures above were all rules that were known, and knowing them is what created the confidence to skip the check.

## Where a rule belongs — read this before adding or changing one

This file is long enough that a rule added in the wrong place is a rule
nobody will find at the moment it applies. That has happened: a run of
corrections once landed as a block of appended paragraphs in the document
skeleton — a ranking rule, a placement rule and a formatting rule all in
the same pile, none of them where a builder working through §4 or §7
would ever meet them. **A rule lives in the section that governs the
decision it constrains, not in the section that happens to be open when
it is written.** The map below is the placement test.

| A rule about… | Belongs in |
|---|---|
| How the build is worked, intake, file and sheet ledgers, what a filter excluded, whether a gap is real | **Step 0** |
| **Which contexts a rule governs, and reading this file before acting** | **The two sections above this map** |
| Which mode is running, what inputs are required, halting on a missing input | **Step 0A** |
| The once-per-cycle sweep before any keyword decision, reverse-scope, price stability, account-level confidence read | **Step 0B** |
| The order every row is judged in | **§1** |
| The six levels and how they constrain each other, the waterfall table's own shape | **§1A** |
| Syntax diagnosis, the four quadrants, the scan table's columns | **§1B** |
| Product posture, TACoS bands, stage, concentration, margin freshness | **§1C** |
| Which objective a row carries | **§2**, with §2A–2C for launch selection, defensive/conquest, market share |
| Break-even, contribution, affordable price, funding arithmetic, envelopes, ramp exposure | **§3** |
| Placement judgement, modifiers, the backward-solve, what the placement table must show, **the ranking exception to the ceiling**, **the four bounds on any bid** | **§4** |
| Supplied sources before derivation, column units, formula cells | **front matter** |
| Deployability of a decided row, budget-as-ceiling, staging to an envelope | **front matter** |
| One verb one operation, state-vs-instruction columns, staging unit | **front matter** |
| Generated reconciliation, version-lock by file hash, freeze order, **the three build phases** | **front matter** |
| Section-scope regeneration, comparison arithmetic, name columns | **front matter** |
| Screen scope, prose regeneration, verifying the checking tool | **front matter** |
| Which lever clears first and which move together | **§4A** |
| Sample floors, correction-sizing caps, staging a move too large for one step, which window a decision is taken on | **§5** |
| Suggesting a goal from the product's own evidence | **§5A** |
| What the declared goal authorises, executing it rather than re-litigating it, the held-action sweep | **§6** |
| Ranking: the seven states, the five properties, loss ceilings, tapers, shared-term gating | **§7** |
| Fixed-bid trials | **§8** |
| Inventory zones, cover, projected cover at push velocity, routing | **§9** |
| Conversion and cost-of-sale as the performance lens | **§10** |
| Whether a row's history belongs to the SKU it is credited to | **§11** |
| Whether a discovery layer may be priced at all | **§12** |
| How a verdict must be written | **§13**, with §13A for what a reviewer is told and §13B for the gate |
| One final draft, correction sweeps with before-and-after counts, downstream figures moving with their source, the decision register and verdict sweep | **§14** |
| What the delivered document contains, its sections and subsections, tables, charts, provenance lines, enumeration | **Document skeleton** |
| Findings that belong to Brand Management rather than PPC | **Brand Management findings register** |

**Two placement tests before writing.** First: which decision does this
rule constrain? Write it where that decision is made. Second: if the rule
says what the *output* must contain rather than how a *decision* is
taken, it belongs in the document skeleton — and if it says both, the
decision half goes to the governing section and the output half to the
skeleton, cross-referenced, not duplicated.

**A rule that defines a calculation names where its result appears**, and
those are two placements, not one: the arithmetic in the governing
section, the table it lands in named in the skeleton.

## Step 0 — how this build is worked, before what it produces

**State every rule once, as current truth — this file does not narrate
its own history.** A rule reads as what is true now, never as what it
used to say, what was corrected, or when it changed. Revision history
belongs in a separate changelog, not inside a working rule.

**This is not housekeeping — it is the source of a real defect in the
output.** A file that narrates its own revisions teaches the document
built from it to do the same, and it did: a delivered plan carried
"an earlier read reported no defensive layer" into text a reviewer
saw. The checks against draft-history bleed in the writing standard
exist to catch that symptom, while prose modelling the behaviour sits
throughout this file. Remove the source, not only the symptom.

**This applies exactly as much to a single-keyword question as to a
full build — new, sourced directly from a real, dated correction, not
inferred.** On 28 August 2026, a keyword-level analysis fired off a
single Slack mention and was rejected outright: "that overall provides
hardly any useful analysis and information that the PPC team could
utilize and this should not just be triggered when I send a message for
a given keyword." **There is no lighter, ad-hoc version of this skill's
own writing standard (§14).** A one-keyword question gets that
keyword's own quarantine check, sample-gate read, syntax diagnosis and
campaign-type footprint the same as a row inside a full build — the
depth requirement does not shrink because the scope of the question
did. If a genuinely quick answer is wanted, say what's being traded
away explicitly (a same-day read with the full chain to follow, for
instance) rather than letting scope silently stand in for depth.

**Examine inputs first, and release them as you go.** For each file:
open it, extract what is decision-relevant, write that to a running
findings file, and move on. **Do not carry raw file contents forward
into the build.** A large product can arrive with fifty or more files;
holding their contents in working memory is what exhausts the room the
plan itself needs. Summarise and release. The findings file, not the
raw data, is what the plan is written from.

**A rule that defines a calculation also names where its result appears
in the delivered document — the single most productive gap found across
this skill's real use.** Section 4 specifies the backward-solve for
placement modifiers in full: base bid times modifier equals a held
target price, computed in that direction only, with rest-of-search
gated on its own fifteen clicks and product pages moving only through
base. All of it correct, all of it followed, and none of it visible in
the plan built from it — which carried a four-row portfolio placement
table, no modifier anywhere, and no bid arithmetic at all, while passing
every check in this file. **Where a section computes something a reader
would need to check, that section names the table it lands in and the
columns that table carries.** The three below were reconstructed after
the fact and are specified here so they are not reconstructed again.

**Never start the deliverable before intake is complete.** A build
that begins writing while still gathering produces sections that later
findings contradict — and the contradiction usually surfaces after the
document reads finished, which is the worst moment to find it.

**Keep a coverage ledger and report it.** Track which sections of this
file actually ran and state that count on delivery. A build that
skipped a section without noticing cannot know what it got wrong: on
the real product above, skipping the launch-selection section produced
an enable register carrying 338,332 search volume of keywords the
declared goal forbids, and the error was invisible until a person
caught it. **A section that did not run is a stated gap, not a silent
omission.**

**The intake protocol below is numbered because it is run in order and
each phase is reported. Prose describing good intake habits did not
prevent three separate real failures — files logged as reviewed after a
structure-only glance, whole workbook tabs never opened, and a
sixty-day window present in the data but absent from the analysis. A
phase that did not run is named on delivery.**

**I-1. Enumerate before reading anything.** List every file. For every
workbook, list every sheet inside it by name. **A workbook is not one
unit for ledger purposes — every sheet is, and an unopened tab is an
unread file.** The enumeration is written down before the first file is
opened, because a list built while reading is a list of what happened
to get read. On a real cycle a bulk export was read at its Sponsored
Products tab while its Sponsored Brands and Sponsored Display tabs went
unopened across all three windows, and the plan asserted from inference
a coverage claim those tabs would have settled as fact; a deal tracker
was read at two tabs of nineteen, leaving unread a ranking-variation
table naming the exact child ASIN an open provenance question needed.

**I-2. Read for content, never for structure.** Column names, row
counts and a spot-check against something already known establish that
a file exists in the expected shape. They establish nothing about what
is in it. **A shallow check returns "nothing new here" identically
whether the file is empty of new information or full of it.** On a real
cycle three files in a row were marked no-new-content this way: a
sixty-day dashboard checked only for which SKUs carried spend, when its
figures showed $3,705.60 of spend the current-week picture never
mentioned; an impression-share export checked only for row count, when
its rows carried weeks of rank and share data; a rank export waved
through as "same structure as one already used" without checking
whether its values agreed or diverged.

**I-3. Extract every decision-relevant figure to the findings file,
with its source file, its sheet, and the window it was measured in.**
The findings file — not the raw data — is what the plan is written
from. Raw contents are released as each file closes; a large product
arrives with seventy or more files and holding their contents is what
exhausts the room the plan itself needs. A figure entering the findings
file without its measurement window cannot later be stated with one,
and §13B's scope-label check will fail on it downstream.

**I-4. Compare every long-window file against the short-window picture
already formed, and record where they disagree.** The longest window
supplied is read for what it shows that the most recent week does not.
This is a distinct phase because a file can be genuinely read, its
figures genuinely extracted, and its implications still never reach the
analysis: on a real cycle the sixty-day window held fifteen keywords
with real order history, a per-placement conversion series that unblocked
the affordable-CPC ceiling, and competitor depth that unblocked the
ranking arithmetic — all extracted, none used, while the plan was
written against a six-row current week and declared three properties
uncomputable that the data could compute.

**I-5. Mark every sheet with one of four statuses, and no others.**
- **READ-FULL** — content read, figures extracted to the findings file.
- **READ-PARTIAL** — opened, some content extracted, the rest not; what
  was skipped and why is stated.
- **NOT-RELEVANT** — read far enough to establish it bears on nothing
  this cycle decides, with that reason stated.
- **NOT-OPENED** — a stated gap, carrying the same weight as an unrun
  section of this file.
**"Reviewed" and "checked" are not statuses**, because both were used on
a real cycle to mean a structure glance and a full read interchangeably,
and a reader of the ledger could not tell which had happened.

**I-6. A sheet earns NOT-RELEVANT only after its content was compared
against what the build already holds and found to genuinely add
nothing.** Not after its shape looked familiar. Where a file is too
large for full comparison, the ledger says so explicitly — "row count
and structure checked, full content not compared" — rather than
borrowing a label a real check would have earned.

**I-7. Report the ledger before writing begins, and halt on any
NOT-OPENED sheet that bears on a section about to be written.** Count
the sheets, not the files: "144 of 144 sheets across 73 files" is the
statement, and if it is short, which ones and why. A coverage claim
made about data in an unopened sheet is an assumption wearing a
finding's clothes.

**A file filtered to this product is not a file read, and what the filter excluded is unexamined, not absent.** The sheet-level ledger above catches an unopened tab; it does not catch a tab that was opened and then narrowed to one slice. Both failures produce the same sentence in the plan — "not supplied" — and only one of them is true. On a real cycle three bulk exports were filtered to a single portfolio and every other portfolio in them treated as missing: the plan declared sibling data unavailable, gated its entire ranking roster on obtaining it, and asked a colleague to supply files that were already in the folder. The same cycle used one of three placement windows and left the other two reading as a gap in the completeness register. **Before any file is filtered, enumerate what the unfiltered file contains — every portfolio, every campaign, every date range, every marketplace — and record that inventory on the ledger beside the slice actually used.** The inventory is what makes a later "not supplied" checkable.

**A gap is declared only after the supplied files have been searched for it, and the search is named.** "Not supplied", "unavailable" and "not in this cycle's file set" are findings about the folder, not about the analysis, and each is wrong the moment the data turns out to be inside a file already read. Before writing any of those phrases, search every supplied file for the thing being declared missing and state where you looked. **Data belonging to the same company is never "unavailable"** — a sibling brand's own portfolio, a second date range, another marketplace: these are either in the export or they are a request someone has to action, and the plan must say which. A gap that dissolves when someone opens the file already on the table costs more credibility than the gap itself ever cost analysis.
**A file that went unread is not evidence that the file was unnecessary.** This reasoning is circular and it produced a wrong recommendation on a real build: 74 files were supplied, 13 were opened, and the other 61 were written up as redundant — using the fact that they had not been read as the proof that they need not be. Three of them carried findings the delivered plan did not have. **A targeting report held the measured top-of-search impression share for every delivering target, all of them under one per cent**, where the plan had inferred that figure for a single row from placement clicks; the rule that a share under thirty per cent makes placement the first lever therefore applied to the whole product rather than to one row. **A parent-level search-query file showed click-through six times the market rate against near-zero purchase share**, which points at the listing rather than at bidding, and the plan diagnosed neither.

**The only honest way to call an input redundant is to open it and show that it changes no decision.** Name what it contains, name the decision it could have touched, and state why the decision stands without it. An input list built from what a previous build happened to read reproduces that build's blind spots and hands them to the next one as instructions.

**Where an input list is produced, it carries the reason each file is on it and the check that put it there.** A list saying "send these thirteen" is a rule about what to ignore, and it will be followed. It has to be at least as well evidenced as any other verdict this file produces, and where a file's contribution is genuinely uncertain, the honest entry is that it was read, its content is described, and no decision this cycle turned on it — not that it was unnecessary.

**Two instructions that contradict each other will be resolved by whichever is more convenient.** A build told to open every supplied file and also handed a list of files not to send has been given two rules, and the narrower one wins because it saves work. Where a list narrows what is asked for, it says so explicitly and says what is being traded away.

**Three gates are read and run every cycle regardless of the job, and
are not part of what a targeted read may skip: the inventory gate, the
SKU-provenance check, and the economic ceilings.** The rest of this
file is legitimately read by job. These three are not, because each can
invalidate a decision the pass never intended to reopen — a bid that is
arithmetically perfect on a child that is out of stock, or held, or
whose ceiling was built on a different SKU, is wrong in a way no other
section will catch. On a real correction pass all three were listed as
skipped because the job was described as a correction rather than a
build; the inventory gate, run afterwards, found a live campaign
spending into a red, held child and changed the verdict on it. **Run
them on the full population every cycle and state that they ran** —
their cost is small and the class of error they catch is the class that
reaches deployment.

**Every gate is evaluated against the state the account will be in after
this change lands, never the state it is in now.** A campaign that is
paused today and enabled by the same file is a serving campaign for
every gate's purposes, and a child that is enabled today but paused by
the same file is not. This is not a subtlety — on a real build it failed
three separate ways in one pass: the inventory gate missed an ad for a
zero-unit child because its campaign was paused at the moment of
checking and switched on two sections later; a settings fix covered
three campaigns when fourteen would be serving; and a stranding check
could not see the ads the file itself was enabling and reported eight
false failures. Build the post-change picture once — currently serving,
plus what this file enables, minus what it pauses — and run every gate
against that.

**If the room runs short, hand off — do not compress.** Say so at the
moment it becomes clear, state exactly what was and was not covered,
and write what has been established to a hand-off document so the next
pass starts from settled ground. **Delivering partial work as complete
is a failure of this skill, not a graceful degradation of it.** A plan
that reads finished and is not costs more than one that stops honestly
halfway, because only the second one is obviously unfinished.

## Step 0A — which mode, and what's needed

**Ask this first, before anything else in this section — and genuinely distinct from the from-scratch-vs-refinement
question below, not the same axis restated.** Is the request for an
**analysis** — a diagnostic read of what's happening and what should
change, grounded in Step 0B's full sweep, delivered as a focused
write-up — or for a **plan** — the complete, formal, structurally-fixed
deliverable this skill otherwise produces? **Do not assume "plan" by
default just because that's what this skill usually produces.** Someone
asking to look at what's been deployed and figure out what needs to
change, the way a mid-cycle check-in works, is asking for an analysis;
assuming they want the full plan regenerated when they only wanted a
diagnostic read either wastes effort producing structure nobody asked
for, or worse, buries the actual findings inside sections the person has
to dig through to find them.

- **Analysis** only makes sense where something already exists to
  analyze — a prior plan, a deployed set of actions, real data since a
  decision was made. **"Something already exists" means exactly that —
  a state that has to be true, not an action that has to happen in this
  session.** A prior plan or deployed history from any earlier session
  satisfies this, current and unchanged; analysis doesn't require that
  plan to be re-confirmed or brought up to date first. **If what exists
  is stale enough to matter, that becomes a finding the analysis itself
  surfaces, not a precondition blocking it from starting** — an
  analysis is exactly the right place to say "the plan this is checked
  against is six weeks old and the product's posture has likely moved,"
  not a reason to halt before saying anything at all. Run Step 0B's
  full sweep in full, then present findings and recommended changes
  directly: what's working, what isn't, what should change and why,
  organized by whatever the findings themselves call for — not forced
  into the fixed plan skeleton below, because an analysis is not a plan
  and doesn't owe that structure. Where a finding is significant enough
  to warrant a full plan update, say so explicitly and ask whether to
  proceed to one, rather than silently expanding an analysis into a
  full rebuild.
- **Plan** proceeds to the mode determination immediately below —
  from-scratch or refinement — and produces the complete, structurally-
  fixed deliverable this skill exists to build.
- **Ambiguous** → ask once, don't guess.

**Once "plan" is confirmed, determine this next**, because the two modes
need different intake and produce different output:

- **No plan exists yet, or the ask is to build one from source data** →
  from-scratch mode. Full intake below.
- **A plan exists and the ask is to complete, refine, correct, or update it**
  → refinement mode. Read the existing plan whole first; only gather data
  for what it's missing or what's gone stale.
- **Ambiguous** → ask once, don't guess.

### From-scratch intake (halt until satisfied)

**Three data-handling traps that have each produced a wrong finding on
a real build. Check for them before declaring anything about a file.**

**Probe the raw sheet before declaring a field missing.** A field is
frequently present in a form a first read does not surface. On a real
build, per-SKU cost of goods was reported as a gap for thirteen of
twenty SKUs; it was present for all of them, embedded inside the
product title string, one pattern-match away. **"Not in the column I
expected" is not the same as "not in the file."**

**Header rows are routinely offset — read the raw sheet first.** On
one real file set, three separate files had their true header below
row one (a SKU list at row 5, an inventory matrix at row 8, a charge
tab at row 3). Reading with a default header silently produces a
frame whose columns are data and whose data is missing.

**Scope by identifier, and check both directions.** Filtering by name
text misses records whose name does not contain the expected string —
on a real build, four genuine campaigns. More consequentially,
**scoping to the product's own portfolio captures the campaigns the
product owns and misses the campaigns that own the product's SKUs.**
A live defensive campaign in a different portfolio carried $1,518 of
this product's spend and 131 of its orders, and went unseen until a
second review. Every product-level total needs both reads, stated
separately. **State a join's scope explicitly before trusting what
it computed, not just whether the join found a match.** A derived metric
built from a join that runs at the wrong scope doesn't only produce
blanks on the rows it can't reach -- it silently corrupts rows that
looked complete, because the join still returns a number, just the wrong
one. On a real build, a halo-share join computed at portfolio scope
instead of full scope left two children dashed -- and also wronged three
children that carried no dash at all and looked fine (one read 174 units
and 49% halo where the correct full-scope figure was 181 units and
52%). A blank cell at least announces itself; a wrong number from an
under-scoped join does not. Before delivering any derived figure built
from a join -- halo share, own-units, wasted-spend split, or similar --
state the scope it ran at and confirm that scope matches what the metric
is actually supposed to measure.

**A fourth trap: a decision-support file can carry its own status field,
and that field can be stale relative to what actually happened in the
real world.** Where a file distinguishes a proposal from what was
actually chosen or executed -- a status flag, a "chosen for the
month" field, a draft marker -- that field is real evidence and is
checked, but it is not the only evidence and it is not assumed current.
On a real cycle, an LTSF what-if scenario's own metadata read "Plan
status: draft" and "Chosen for the month? no," while the person
supplying the file described it as the final actions taken -- a direct
conflict between the file's self-report and how it was described.
Neither side was trusted alone. The account's own Slack record settled
it: the scenario had been explicitly approved by the decision-maker
("that can be proceeding for the full execution") and the team had
already submitted and completed the actual removal and liquidation
orders against it, days before the file was pulled -- the dashboard
flag was simply never updated after the fact. Building a section on the
file's stale status field alone would have excluded 21 SKUs from a
ranking allowance they were never actually blocked from. **Where a
file's own status conflicts with how it was described, or is
ambiguous, resolve it against independent evidence of what was actually
done -- a dated message thread, a completion confirmation, an order log
-- not by trusting either the file's internal flag or the person's
description in isolation.**

**Everything below is asked for together, as one batch, before any work
begins on this product — not requested piecemeal as each item happens
to become needed.** "Halt until satisfied" means exactly that: this
build does not start, not even a partial or preliminary pass, until
every item below is either provided or explicitly confirmed as not
applicable to this product. A build that starts working through
whatever data happens to already be in hand, planning to circle back
for the rest, has already violated this — the point of the halt is
that a partial start produces partial, potentially wrong work that
then has to be redone once the missing piece changes the picture.

- **Sponsored Products bulk export**, ideally three placement windows —
  and their roles are distinct, stated explicitly here because an
  earlier version of this rule called the long window "primary
  evidence," which reads as backwards from what actually governs a
  decision: **the current 7-day window against the prior 7-day window is
  what a bid or placement action is actually judged against — that
  comparison is the evidence a live decision is made on.** The long
  window (60–90 days) is reference and context — it's what establishes a
  reliable baseline, confirms a minimum sample exists at all, and feeds
  the trend reads that need real history (§7's rank-trend read, §10's
  CVR baseline) — but it does not itself drive this cycle's action the
  way the 7-day comparison does. Check every tab name before declaring a
  file missing — a bulk export routinely carries no "bulk" in its
  filename.
- **Search term report**, same long window.
- **Unit economics** (contribution/CM2 per SKU, AOV, COGS) — the source
  every ceiling in this plan is built from. Never substitute a category
  average or a prior product's number for a SKU's own.
- **Search Query Performance (SQP) or equivalent market/brand share data**,
  and a **Master Keyword List** with search volume and syntax
  classification — **where syntax is already classified in the MKL
  provided, it's verified against the account's own taxonomy before
  being used, not accepted on trust (§1B).**
- **Inventory / days-of-cover per SKU**, current stock, inbound, any LTSF
  or aged-stock flag.
- **Rank history, minimum one month, ideally up to three** — required
  before the ranking progress test (§7) can run on any keyword; below one
  month, that keyword is OUT OF SCOPE for a ranking verdict.
- **The product's own declared strategic goal — this is a hard stop,
  not softened by §5A's existence.** Growth/Scale, Profit-First,
  Clearance/LTSF, or a stated combination. **This build does not
  proceed past this point — no coverage decisions, no bid or placement
  work, nothing in §2A or downstream — until the goal is actually
  established.** §5A exists so "not yet declared" doesn't mean the
  build stalls waiting on a person with nothing to go on — it computes
  a suggestion from the product's own data and presents it with the
  numbers behind it. But a suggestion is not an establishment. The goal
  counts as established only once the person has declared it directly,
  or confirmed a §5A suggestion — whichever happens, the halt lifts
  only at that point, never before it on the assumption the suggestion
  will probably be accepted.
- **Competitor data**, if conquest/PAT campaigns exist or are proposed —
  **source confirmed: AsinSight, Helium10, or Cerebro pulls**, dated, not
  an undated or estimated read.
- **Each sibling product's own bulk export**, where this product shares a
  head term with a sibling — required to compute the family-ownership
  formula (§1A) rather than approximate it from this product's numbers
  alone. Same windows as the primary bulk.
- **A structure source, if the user has one — and this skill works from
  any of three kinds, not only a formal blank template.** Generalized
  here because the earlier version of this rule only named one input
  type when the real requirement is broader:
  1. **A blank reference template** — an empty section shell with no
     content, defining the list, order, and names to clone exactly.
  2. **A fully-populated example plan** — a real, finished document for
     a *different* product. This skill reads it for its structure only —
     the section list, order, and names — never its content; a section
     titled "Market position" in the example produces a section titled
     "Market position" in the new build, populated with the new
     product's own findings, not the example's.
  3. **No structure given at all** — falls back to the document skeleton
     below, which is this skill's own best default, not a mandatory
     structure that overrides anything more specific. **Any given
     structure — template or example — always takes precedence over
     this skill's own default, including where the given structure
     differs from what this skill's own account-sourced skeleton
     describes.** The skeleton below reflects one real account's
     documented convention; a different account, a different team, or
     an explicitly different structure this account itself hands over
     is not an error to reconcile against that skeleton — it's simply
     the structure this build uses instead.
  
  **This is the actual mechanism behind the account's own standing
  requirement that output structure be identical across all three PPC
  team members, stated here explicitly because it was previously only
  implied.** Whichever structure source governs — template, example, or
  default — the section list, its order, and every section's name are
  fixed for that build and do not vary by who runs this skill: Ghazanfar's
  plan, Shayan Rana's plan, and Shayan Akhtar Taquie's plan carry the
  identical section list in the identical order once the structure is
  set, for the identical reason a reference gets cloned exactly rather
  than approximated. **What varies by analyst and product is content,
  never structure**: the findings, the numbers, the named risks — never
  whether a section exists, what it's titled, or where it sits in the
  sequence. A plan missing a section the governing structure requires,
  or carrying an extra one it doesn't, fails this requirement regardless
  of how good the content inside it is.

**A missing file is a named gap in the plan, never a silent guess.**

### Refinement-mode intake

Read the whole existing plan first. Classify each decision category as
**stated** (leave alone), **gap** (compute this skill's default against
real data), or **stale** (the plan states something current data
contradicts). Gather only what's needed for gaps and stale items.

**The full plan is what gets produced every cycle, every section
present whether it changed or not — that stays the source of truth and
never becomes a partial document. Alongside it, a change log is
required, not optional, previously unspecified in this skill.** The
change log lists only the decisions that actually changed since last
cycle — old value, new value, one line naming why — so a reviewer isn't
left re-reading the entire plan to find what actually moved. A cycle
where nothing changed produces a change log saying exactly that, not a
silently-omitted one that reads as if the check was skipped.

**The plan itself is always one clean, final document — never a
tracked-changes or redlined version of itself, stated explicitly
because "present it as one final draft" is the actual requirement, not
an implied one.** No strikethrough, no highlighted "before" values
sitting inside the working document, no dual old/new figures mixed into
the live narrative. A section that changed reads exactly as clean and
complete as a section that didn't — indistinct from a from-scratch
build in its own right. Every comparison against the prior cycle — what
changed, what it used to say — lives entirely in the separate change
log and Change Review Sheet described below, never inside the
deliverable itself. This is the same principle as refinement mode's own
instruction to regenerate a changed keyword's reasoning from current
facts rather than patch the old text — applied here to the whole
document, not just one keyword: the output is a finished draft, not a
marked-up in-progress one.
**A rendered deliverable (a .docx, a .xlsx) is only as current as its last regeneration, and that has to be checked, not assumed -- sourced from a real instance of the gap.** The working document this skill builds section by section and the rendered file handed to the person are two different artifacts once any edit lands after the last render. Saying "I'll show the file after every section" is a stated intention; it is not the same fact as the file actually being current, and the two were treated as interchangeable on a real cycle -- several sections' worth of real corrections landed in the working document while the person kept the same, now-stale rendered file, until asked directly whether it was current. **Before answering any question about a deliverable's state, compare the rendered file's own modification time against the working document's** -- not from memory of having intended to regenerate it, from the actual timestamps. Where they disagree, the honest answer is "stale, regenerating now," not a description of what the working document currently contains as if the rendered file already reflected it.

**A Change Review Sheet, defined here for the first time rather than
assumed to already exist:** a lightweight, reviewer-facing document
built from that same change log — one row per changed decision, the
keyword or campaign it touches, old value, new value, the one-line
reason, and a column for the reviewer's own mark (approve, reject, or
modify with their own value). It is not the full plan and doesn't try to
be; its purpose is letting a named reviewer (this account's own
peer-review-before-Erik practice) mark up a manageable list quickly
rather than needing to read the entire document to approve a cycle's
changes. **When it comes back marked up, those specific marks are
protected from being silently overwritten on the next refinement pass —
a reviewer's "reject" or "modify" on a specific decision holds the same
way an explicit user override does, until that same reviewer changes it
again.** This closes a real gap: this skill previously protected
explicit user overrides from silent re-computation but never stated the
same protection for a reviewer's own markup, even though both are the
same kind of decision that shouldn't be quietly recomputed away.

**Before any new decision is made, every keyword that carried a real
action in the prior plan is graded against what it predicted — this is
a required step, not an optional look-back.** The requirement itself is
sourced: every deployed action logs its prediction, and the next
cycle's first step scores that log against what actually happened.
**The specific four-word vocabulary below — worked, flat, backfired,
too soon — is this skill's own construction for organizing that
scoring, not a category set taken verbatim from the account's own
material, and it's flagged as such here rather than presented as if it
were.** For each keyword, pull its own prior cycle's stated prediction
(the metric, direction, and horizon named in its own reasoning) and its
own stated reversal condition, and compare both against what the
current data actually shows. Grade each as **worked** (the predicted
movement happened), **flat** (no meaningful movement either way),
**backfired** (moved the wrong direction), or **too soon** (the stated
horizon hasn't been reached yet — not gradable this cycle). **This
grade is required input to this cycle's decision for that keyword, not
a separate report filed alongside it.**

**Where the grade actually lives in the document, stated explicitly
because a requirement with no visible home tends to stay invisible in
practice.** A plan has no spreadsheet column to carry this the way the
companion workbook does, so it lives in two places instead: a short,
dated scoring table near the top of the oversight-cadence section
listing every graded keyword from last cycle with its grade stated
plainly, and a restatement in that keyword's own reasoning wherever the
grade is what's actually driving this cycle's verdict — a keyword
escalating to STOP-LOSS on its fourth flat grade states that plainly in
its own write-up, not only in the summary table. A grade sitting only in
the summary table with no trace in the reasoning that used it is as
incomplete as a reasoning statement with no table entry behind it — both
are required, not either-or.

**The scoring table needs a durable source outside this document, because
a table inside one plan cannot carry a counter across cycles.** The plan
states this cycle's grades; a persistent **impact ledger**, carried
forward as an input to the next build, holds the metric baseline captured
at decision time, the objective and stage the decision was made under,
every grade since, and a rolling count of consecutive grades showing no
effect. Without it, "the fourth consecutive flat grade" is a claim no
reviewer can check, because the earlier plans are closed documents. **A
counter that lives only in prose is not a counter.**

**Grading has a minimum observation window, and an action taken this
cycle is never graded.** It has produced no evidence yet, so a grade on
it is a verdict about noise. No grade before the action's own stated
horizon, and none on fewer than fifteen clicks of fresh evidence gathered
after the change landed. Failing either test is **too soon** — a real
verdict that stops the row being re-cut, not a blank.

**Execution verification comes before grading, because a decision that
never deployed cannot be graded.** Compare what the last cycle's files
*said* against what the account *now shows* — bids moved, states changed,
ads switched — and mark anything that never landed as **unexecuted**
rather than flat. On a real build 525 priced rows sat behind an enable
nobody made; graded without this step they would have read as flat and
escalated as a diagnosis failure, when the diagnosis was never tested.
**Grading an unexecuted action discards a decision that might have worked
and hides the deployment gap that stopped it.**

**Where a verdict escalates to a person, what that person did is recorded
and graded by the same rule.** An escalation that hands a decision to a
reviewer and never asks the outcome is fire-and-forget. Log the action
and its date, capture the baseline then, and grade it next cycle as any
other action. If it worked, the escalation clears. If it was also flat or
backfired, the lever is exhausted and the item goes to structural review
— listing, offer, price, inventory, or the objective — **never another
bid change**. Two failed attempts by two decision-makers on one lever is
evidence about the lever.

**A general escalation principle sits underneath this grading, sourced
directly and broader than just ranking rows: any verdict — on any
keyword, any objective — repeating for four consecutive cycles without
producing its predicted effect is treated as a diagnosis error, not
patience, and escalates regardless of what the verdict actually is.**
This isn't limited to a stalled ranking push; a Defensive row held at
the same floor for four cycles with impression share still slipping, or
a Discovery candidate sitting at the same formula-only correction for
four cycles with no order ever landing, escalate the same way. A
keyword graded "flat" for the fourth consecutive cycle is a different
decision from one graded "flat" for the first time, even though both
show the same raw numbers today — the repetition itself is the finding,
independent of which specific verdict kept repeating.

---

## Step 0B — the full product analysis sweep, run once per cycle before any keyword decision

**This runs top-down, matching the waterfall (§1A): product, then
family, then syntax, then cross-cutting checks — before a single
keyword's own bid or placement is touched.** Presenting "what needs to
change" without having run this list is presenting a partial analysis
as if it were complete.

**Product level:**
1. Cycle-over-cycle grading — did last cycle's real actions do what they
   predicted? (Step 0)
2. Structural placement sweep — what is the distribution of top-of-search
   modifiers across this portfolio, how many campaigns are structurally
   unable to isolate, and where do clicks and spend actually land by
   placement? A structural finding here changes what the cycle is for,
   and it is invisible from any single row.
3. Product-goal gate — what's actually authorized for this product
   right now? (§6)
4. The four-dimension read — rank trend, revenue trend, margin trend,
   inventory posture, combined and weighted by the declared goal (§1C)
5. TACoS band tier and its decomposition by objective (§1C)
6. Stage integrity — has this product actually earned its declared
   stage, or does it need graduation or demotion review? (§1C)
7. Structure hygiene — match-type and format spend-split against the
   account's own reference targets (§1C)
8. Event and season posture — any live or upcoming deal window, which
   way the seasonal index is moving (§1C)
9. Margin freshness, and whether a confirmed-but-not-yet-live COGS
   change needs its own parallel figure carried (§3, §1C)
10. Concentration — is spend dangerously bunched on one or five terms
   without it being a declared push? (§1C)

**Family level:**
10. Shared head-term ownership — computed, not assumed, per the
    margin/CVR/inventory-depth formula (§1A)
11. Cross-sibling cannibalization on the same term

**Syntax level, for every syntax on the product:**
12. Four-quadrant diagnosis with persistence — transient or chronic?
    (§1B)
13. Priority-class spend-share — is actual share tracking its target?
14. Match-type coverage gaps — any primary syntax at 0% phrase?
15. Organic/ad dependency ratio — earning this syntax's sales, or
    renting them?

**Keyword level, routed by objective — every objective actually present
on this product, not just Ranking:**
16. Ranking: candidacy class (Cold/Recovery/Structure-blocked), the
    five-property gate, the seven-state test, the TOS-share pre-check,
    the competitive-shock check, sufficiency-stop or taper status, the
    incrementality ladder on already-won terms, SBV arbitrage where a
    head term's CPC has run inflated (§7)
17. Market Share: which of the eight states applies to each root (§2C)
18. Defensive: which of the six states applies to each branded term
    (§2B)
19. Conquest: archetype, CPC-efficiency index, Open/Rotate/Exit status
    (§2B)
20. Profitable Conversion: CPA vs. ceiling, and whether a price-
    attribution hold applies (§10)
21. Discovery: candidacy gate, harvest test, wasted-spend share (WAS% —
    spend with no attributed order, as a share of total spend), which
    negation mode applies to any cut (§12, §13)

**Cross-cutting, applies regardless of objective:**
22. SKU-provenance — wrong-variation-from-the-start, borrowed ranking
    credit (§11)
23. Duplicate ownership — checked against the four legitimate
    coexistence reasons before consolidating anything (§1)
24. Inventory zone, re-read fresh for every routed SKU, not assumed
    unchanged from last cycle (§9)
25. For any keyword being considered for a new or continued ranking
    push specifically: projected days-of-cover at the push's own target
    velocity, not just current-velocity days-of-cover — does closing
    this push's own order gap run the SKU into Yellow or Red before its
    own checkpoint date? (§7's Sized property)
26. **Campaign-type footprint — which campaign types currently carry
    this term, against what its declared objective and stage actually
    require; a gap stated by name, not left implicit.** *(Restored —
    sourced directly from two account documents: the Deal Frameworks
    reference requires "campaign type" as a named field on every
    keyword's own action record, and the Master PPC Decision Framework
    names this exact gap directly -- "the current keyword view is
    Exact/Broad only" against a required read aggregated across Auto,
    PAT, SB, SBV and SD. This was never built into this skill's own
    per-row checklist despite being a documented account requirement,
    and its absence is what a real product owner flagged directly: a
    plan showing new campaigns with no accompanying read of what else
    is already running on the same term, or should be, "causing various
    misses in the strategic consideration that should be able to be
    had."* State the full set of campaign types this specific term
    currently has a live instance in -- not the syntax, the term itself
    -- against what its objective calls for: a Ranking term with no
    Broad/Auto layer feeding it discovery traffic is a gap even if its
    Exact instance is performing well; a term running in three campaign
    types with no stated reason for the third is worth naming too.
    Where the footprint matches what the objective requires, say so
    plainly rather than leaving the check invisible by only surfacing
    when something's wrong.

**An account-wide confidence or completeness bar is read for this
product specifically before it is treated as binding or ignored.**
Where the account manifest sits below its floor and that state bars
pushes, the plan states which of the underlying gaps are closed for
this product by the files actually supplied, and claims the clearance
on that evidence. Neither silently proceeding nor silently halting is
acceptable: both ask the reviewer to assume a check was run.

**The campaign scope is swept in both directions, and the reverse sweep is stated even when it returns nothing.** Scoping by portfolio finds the campaigns this product owns; it does not find campaigns in other portfolios that advertise this product's children. Both are real and only the first is easy. On a real build the reverse sweep found $1,518 of spend and 131 orders sitting in a brand-defence campaign in a different portfolio — money and orders that every portfolio-scoped figure in the plan had silently excluded. **Run the reverse sweep every cycle: take the product's own child ASINs, search every campaign in the account for them, and report what was found or that nothing was.** A plan that never states the reverse sweep ran leaves its reader unable to tell an empty result from an unrun check.

**Price stability across the measurement window is checked and stated before any trend verdict or ceiling is trusted.** A price change inside the window moves conversion, cost of sale and contribution together, and every rate computed across it is a blend of two different products. Where a deal or a price change lands inside a comparison window, that window is disqualified for trend verdicts and every ceiling is rebuilt on the post-change price, with the deal-state economics computed separately. **State the check explicitly — "price held at $X across the window" is a finding, and its absence from a plan is indistinguishable from the check never running.**

**Only after this sweep is complete does the analysis proceed to
individual keyword decisions and the full validation gate.** A finding
from this sweep that changes a keyword's verdict — a syntax newly
chronic, an inventory zone that flipped, a product that's moved into
Breach — is named as the reason for that keyword's changed verdict, not
left implicit.

---

## 1. Decision order — never vary it, applies to every row

**Every keyword row is evaluated independently against the full rule set,
using only its own data** — never as a batch pattern where one row's
verdict is copied or inferred from a sibling row, even when several rows
share the same campaign, syntax, or final action. Two rows reaching the
same verdict must arrive there through their own numbers, stated as such.
The same independence applies to placement decisions (§4 — a TOS/ROS/PDP
verdict is never copied from another keyword's same placement just
because they share a campaign), to budget decisions (a campaign's
budget is set from that campaign's own spend, delivery, and utilization,
never patterned from a sibling campaign or applied as a flat roster rule),
and to routing decisions. **A campaign's routed SKU is decided from that
campaign's own current advertised child, its own inventory and halo
reading, and its own attribute match to the keyword — never from a name
pattern.** "Every campaign with QUEEN in the name routes to
QUEEN-GRAPHITE" is a batch instruction, not nineteen decisions, even when
it happens to be right on all nineteen — the number of campaigns it's
applied to correctly doesn't make it the right *kind* of rule; each one
still needs its own attribute check (§2A) and its own halo evidence (§11)
stated, not inherited from the pattern the rest of the sweep followed.

**This independence runs across different rows, never within one
keyword's own bid and its own placement modifiers.** A keyword's base bid
and its TOS/ROS/PDP modifiers in the same campaign are one coordinated
decision, not three independent ones — §4's backward-solve requires
computing them together: each placement's target price is set from that
placement's own data, then the base bid and modifiers are solved as a set
so the target actually holds at every placement it touches. Deciding a
keyword's bid without reference to what its own placements need is the
failure the backward-solve rule exists to prevent, not something the
independence principle above reopens.

The first gate below that fires ends that row's evaluation.

1. **Validation quarantine.** Impossible or contradictory
   metrics — CVR or ACoS present with zero orders, CTR present with zero
   clicks, two different values reported for the same metric across
   sources (bulk vs. console vs. SellerBoard vs. SQP) — quarantine the
   row before anything else runs. No recommendation is produced from a
   quarantined row; a data-refresh task opens the same day, and no
   verdict is built by averaging or picking between two contradictory
   numbers. This gate runs first because every gate after it assumes the
   data feeding it is at least internally coherent.
2. **Indexing gate — NOT RUN for this account.** The keyword master's
   indexing field is known to be incorrect. It is set aside entirely:
   not blocked on, not asked about, not carried as a condition on any
   row. **Where a term's only obstacle is the indexing field, it
   proceeds on its other merits.** Record the exclusion in the data
   conditions register so a later cycle knows the field was set aside
   deliberately rather than overlooked. Re-open only if a validated
   indexing source becomes available.

   *An earlier version required an ask before blocking on this field.
   That was right while its status was uncertain; it is no longer
   uncertain. A field known to be wrong produces two failures if
   consulted — terms blocked that are fine, and an ask that wastes
   attention on a question the data cannot answer.*

   *The rule below is dormant. It does not apply to this account and is
   retained only so an account with a validated indexing field has it:
   a term that isn't indexed gets no spend, an indexing task first; a
   Ranking-tagged term indexed backend-only gets a listing-placement
   task before push funding; and where the field would change a real
   decision, ask rather than apply it silently.*

3. **Live state.** Effective state = keyword enabled AND campaign enabled.
   Either paused → paused, nothing else evaluated for that row.
4. **Inventory gate.** Routed SKU below its cover threshold → hold (§9).
5. **Duplicate ownership.** One live instance per term per match type,
   **matched on normalized text — lowercased and whitespace-collapsed,
   never reordered.** This catches a real literal duplicate (the same
   words in the same order, differing only by case or stray whitespace)
   without ever treating a word-order variant as the same term. **Word
   order is never a duplicate signal, in this gate or anywhere else in
   either skill — "queen cooling sheets" and "cooling sheets queen" are
   two distinct keywords, each entitled to its own live instance, full
   stop.** This was corrected here after an earlier version of this gate
   normalized by sorted word-set, which silently collapsed word-order
   pairs into one instance — directly undoing the launch-time decision
   (§2A) to launch them as separate terms in the first place, since the
   very next optimization cycle would immediately re-merge what launch
   had deliberately kept apart. **Before consolidating, check whether
   one of four legitimate reasons explains why both instances exist —
   sourced from the account's own framework, not previously checked in
   this skill:** a stage-stack (an earlier-stage campaign deliberately
   left running alongside a newer one, not yet retired); a genuine
   placement-split (each instance intentionally serves a different
   placement, not duplicated coverage); a variation-split (each instance
   is correctly routed to a different size or colour child, not the same
   SKU twice); or sibling ownership (a different product in the same
   family legitimately holds its own instance of a shared term, per
   §1A's family-level assignment). **If one of these four applies, both
   instances stand** — this isn't a duplicate to resolve, it's two
   deliberate campaigns that happen to look alike. Only once none of the
   four applies does the tie-break run: **the instance winning on higher
   CVR at lower CPC, with longer clean history breaking any remaining
   tie, owns the term** — a rate-based comparison, not a volume-based
   one; every other instance is withheld with no other field changed.
6. **Converting rows are never parked by the sample gate.** A row with any
   orders skips straight to the objective loop.
7. **Sample gate, graduated by what's being verdicted, not one flat
   floor.** A bid read needs 15+ clicks. A CVR verdict specifically needs
   100+ clicks — a bid can be corrected at 15 clicks (formula-only, §5),
   but a rate judgment about how well a term converts needs the deeper
   sample. A CTR verdict needs 1,000+ impressions. Below the relevant
   floor: hold, formula-only correction if price is off ceiling, no
   performance verdict of the kind that floor gates.
8. **Quality gate**, read at the delivering placement, never blended —
   this is the same check §7's State E investigation runs (price,
   inventory/stockout, review rating or count, content/images, a deal
   ending): confirm none of these explain the row's numbers before a bid
   verdict is trusted. Where one does, it's a Brand Management finding,
   never a PPC lever.
9. **Objective loop** (§2), then the full rule set (§3–§13).

---

## 1A. The waterfall — six levels, and how they constrain each other

Every decision in this skill sits at one of six levels, and a decision at
any level has to respect what the levels above have already decided and
hand down a boundary the levels below have to work inside:

1. **Product** — the spend envelope and TACoS band for the whole
   product, gated by inventory, stage, and the declared strategic goal
   (§6). Sets the outer boundary everything below has to fit inside.
2. **Family** — where sibling products share a search results page,
   this level declares which sibling owns a shared head term, calls out
   cannibalization where two siblings are both running ranking pushes on
   the same term, and keeps a shared plural variant as one managed
   identity rather than several. **A shared word-order variant is never
   collapsed, here or anywhere else** — corrected to match the confirmed
   rule that word order is never a duplicate signal (§2A), even when two
   siblings each hold a differently-ordered instance of what looks like
   the same head term. **Ownership is assigned by a
   real formula, sourced from the account's own framework, not a general
   precedence rule applied without arithmetic behind it:** margin per
   order, multiplied by that sibling's own conversion rate on the shared
   root term, multiplied by that sibling's own inventory depth in days.
   The sibling with the higher score owns the term; the others hold or
   route around it. This replaces "family outranks product" as an
   unstated intuition — the precedence still holds, but which specific
   sibling wins is now computed, not assumed. **The data this formula
   needs — a sibling's own conversion rate, CPC, ACoS, and match-type
   structure on the shared term — comes from that sibling's own bulk
   export, pulled alongside the primary product's, not estimated or
   left unsourced.** Where a sibling's own bulk isn't available, the
   comparison is named as a gap rather than approximated from the
   primary product's numbers alone — a sibling's performance on a shared
   term is not interchangeable with this product's own performance on
   it. **What this formula does not yet resolve: two siblings landing
   on a genuine tie, not just a close call.** No tie-breaking rule
   beyond this composite score is confirmed — if the account has one,
   it applies here; absent that, an exact tie is named as its own
   finding for a person to rule on, never silently broken by whichever
   sibling happens to be listed first or reviewed first.
3. **Syntax** — the level defined in full in §1B below. Diagnoses
   whether a keyword group is working, and if not, why, before any
   keyword inside it is priced.
4. **Keyword** — the objective, the target, and the one governing
   verdict for each term, computed from that term's own data, inside
   whatever boundary its syntax and product level have already set.
5. **Campaign** — how that keyword's objective is actually executed:
   structure, budget pacing, duplicate and coverage hygiene.
6. **Placement / Variation** — the deployment surface itself: the
   actual bid ladder, the actual placement modifiers, the actual routed
   SKU.

**The waterfall is a real table with a fixed row structure, not a
six-line summary of the levels — specified here because the level list
above describes the concept and never said what the table looks like,
and the gap was filled with a generic six-row summary.** Rows run:
the product, then **one row per syntax**, then **one row per campaign**.
Columns carry, for each row, its **target and its current value** side
by side for: cost per acquisition, spend, conversion rate,
click-through rate, total advertising cost of sale, and profitability
contribution. A row whose target cannot be computed states why in place
of the number. This is the table that makes the six levels above
operational — without it the constraint each level hands down to the
next is asserted rather than shown.

**A decision has to work in both directions on this list, not just
downward.** A keyword-level verdict that would push its own syntax past
that syntax's own spend-share target is a signal to revisit the
syntax-level allocation, not something the keyword pushes through
unilaterally. A placement-level read that a routed SKU is running low on
cover flows back up to the product-level inventory gate (§9), not a
placement-only concern.

**Oversight is not spent evenly across every keyword — it's tiered.**
Full analysis at the keyword, campaign, and placement levels runs on
every term at 250+ search volume or sitting in the account's top spend
decile — lowered from the source framework's own 500+ figure to match
this account's already-established 250 SV convention used elsewhere in
this skill for launch eligibility (§2A) — in practice, a wider set of
terms per product getting full narrative treatment than the framework's
own default would produce. Everything below that carries identity and
basic performance fields, runs on the same rules, but isn't
hand-reviewed the same way — an exception alert fires if something on
the tail breaches a threshold, but the tail isn't re-derived line by line
every cycle the way the head is. This is a deliberate allocation of
effort, not a shortcut: direction is set at the top of this list and the
verdicts that matter most are confirmed at the bottom; the analytical
volume concentrates in between.

---

## 1B. Syntax-level diagnosis — the four-quadrant system

**Syntax verification against the account's own taxonomy — checked
before any diagnosis runs.** Where an MKL is provided with syntax
already classified, this skill does not accept it as given — it
verifies the classification against the account's own real taxonomy
first, and **states that structure explicitly before correcting
anything**, so whoever built the MKL can see exactly what it's being
checked against rather than have changes appear unexplained. The full
methodology this check runs against lives in the account's dedicated
`keyword-syntax-builder` skill — this section states the confirmed
structure at the level needed to verify and diagnose; building a
syntax taxonomy from scratch for a product that doesn't have one yet
is that skill's job, not this one's.

**The structure being checked against, now confirmed rather than
ambiguous:** a variable-depth, pipe-delimited tag —
`Root | Product Form | Segment`, with a fourth level only where that
specific branch has a real sibling needing to be told apart from it
(`Cooling | Sheets | Queen | Core` exists because a `Color` sibling
exists under Queen; a size with no such sibling stays a clean
three-level tag with nothing trailing). **Segment is not limited to
named sizes** — a bare number plus a unit (inches, ounces, feet,
millilitres, whatever the category actually uses) is exactly as valid
at the segment position as a named size class, confirmed from the
listing and the full SKU list, never assumed from category guesswork.

**A listing can use two different product-form words with different
rules for each, confirmed against a real build — don't assume a
single word covers it.** A Cooling Comforter listing used "Comforter"
as the literal product name (unconditionally in-family) and "Blanket"
as a marketing synonym in the same title (in-family only when paired
with the attribute; bare or size-qualified "blanket" alone stayed
Generic). Check the actual title and bullets for a second word used
this way before assuming the provided syntax only needs one root
verified.

**The precedence order a term resolves through, first match wins:**
Branded → Competitor Branded → Irrelevant (material we don't sell, a
different product form, or a size/unit genuinely not carried and not
resolvable to a real SKU via a confirmed near-miss mapping) → Generic
→ Spanish (its own flat bucket for what would otherwise be relevant —
Irrelevant and Generic stay shared across languages, never split by
it) → In-family. **A near-miss mapping absent from the provided MKL
is a gap to flag, never a default to assume** — a real build shipped
one unconfirmed ("reasonable-seeming") near-miss pair, and it took the
person catching it to correct; state the absence and ask, don't fill
it in as if it were settled. **There is no accepted Unclassified
state.** A term matching nothing gets fixed directly when the answer
is actually known (a misspelling, a variant, a near-miss already
covered by a ruling) and escalated only when there's a genuine, stated
reason for doubt — never left in a permanent, unresolved bucket, and
never escalated when the answer was never actually in question.

**The actual check, once the structure is stated:** every keyword's
provided syntax tag is checked against this structure — does it
correctly separate root from segment, and does it match what the
keyword text and its routing requirement actually indicate? Where it
does, the provided tag is used exactly as given, unchanged — no
rewriting something that's already correct. Where it doesn't, the tag
is corrected, and the correction states which part changed and why,
the same standard this skill applies to any other correction.

**This check is not subject to the oversight-tiering that governs
everything else in this skill, stated explicitly because that tiering
is pervasive enough elsewhere that "every keyword" here could
otherwise be read as still meaning "every oversight-class keyword."
It doesn't.** A tail keyword sitting well below the 250+ SV threshold
still gets its syntax tag checked, same as any oversight-class term —
because a wrong tag on a tail keyword doesn't just affect that one
row, it corrupts the syntax-level rollup the oversight-class keywords
in that same syntax are being diagnosed against. Getting every
oversight-class keyword's syntax right while a tail keyword sits
mistagged inside the same syntax bucket doesn't protect the diagnosis
— it just hides the corruption in the rows nobody was looking at
closely. Every row, every time, no exception carried over from how
depth is otherwise tiered.

**Diagnosis runs at the syntax level — root plus size or defining
modifier — because a single keyword is too noisy to diagnose reliably
and the whole product is too coarse to act on.** Every syntax above a
stated minimum volume is scored on click-through rate and conversion
rate against a benchmark, and lands in one of four states:

- **Strong** — converting and clicking at or above benchmark. Scale it;
  these are the syntaxes funding the rest of the account.
- **Visibility** — converting fine, but not being seen enough. Buy
  placement and impression share; do not touch the listing, because the
  offer isn't the problem.
- **Conversion** — being seen fine, but not converting. Fix the listing
  or the offer; do not buy more traffic into a page that isn't closing
  the sale it already gets.
- **Both failing** — neither clicking nor converting at benchmark.
  Reduce spend and reallocate; this is the smallest-footprint state, not
  a scale-up candidate under any read.

**The benchmark is market data first, this account's own portfolio
median only as a named fallback.** Where real market click-through and
conversion figures exist for the syntax, they govern. Where they don't
yet, the portfolio's own median stands in — but that substitution is
stated on the record, because a Both Failing verdict against our own
average means something different from a Both Failing verdict against
the real market, and a reader needs to know which one produced the
label.

**How long a syntax has sat in its current state changes what the state
means.** One or two consecutive weeks in a failing quadrant is read as
transient — a deal hangover, a stockout echo, a fluctuation — and it's
held and watched, not acted on. Four or more consecutive weeks in the
same failing quadrant is chronic, and chronic changes the class of
action available: a chronic Conversion syntax has its bids frozen at
maintenance level, and nothing about clicks, CVR, or CPA on an
individual keyword inside it reopens a ranking allowance until the
listing or offer itself is fixed. This is the same shape as this skill's
product-goal gate (§6) — a higher level's diagnosis nullifying a lower
level's allowance — just applied one level down, at syntax rather than
product.

**Every syntax carries a priority class with a target share of spend,
checked against what it's actually getting.** Primary syntaxes are the
demand drivers and typically hold the majority of spend (commonly 60%
or more); Secondary syntaxes support at a smaller share (commonly capped
around 25% unless a dated test is explicitly running above that); Defend
syntaxes exist to hold a position already won, not to grow one;
Experimental syntaxes are being tried at a small, bounded footprint
specifically to generate the evidence that would justify reclassifying
them. A syntax running well outside its class's target share — spending
like a Primary while classified Secondary, for instance — is a finding
on its own, not something that resolves itself by the keyword-level
numbers looking fine.

**Coverage completeness is measured, not assumed.** For every syntax,
the real market search volume is compared against what's actually
funded, and the gap is quantified in search volume, not just counted in
keywords. Every meaningfully-sized gap is either funded or explicitly
declined with the reason named — an unfunded gap that's never been
looked at is a different, worse thing than one that's been evaluated and
deliberately passed on, and the two should never look the same on the
page.

**Listing coverage is checked before bidding is.** Whether a syntax's
terms are actually indexed, present in the title, present in the
bullets, or only reachable through backend search terms is its own read,
separate from performance. A syntax scoring badly on listing coverage
has a listing problem to fix first — no amount of bid correction closes
a gap that exists because the words themselves aren't on the page.

**Rank velocity is tracked as its own read, not inferred from the
diagnosis alone.** How fast a syntax's rank is actually moving, whether
that movement is accelerating or stalling, and an honest estimate of
when it would reach its target at the current rate — these are checked
directly, because a syntax can carry a Visibility diagnosis and still be
moving too slowly to be worth the spend it's getting, or moving fast
enough that less spend would still get there.

**Whether a syntax is earning its sales or renting them is checked by
comparing organic share against ad dependency over time.** A Primary
syntax where the ad-attributed share of its sales is rising while its
organic share is falling is a warning, even if every individual keyword
inside it looks fine on its own numbers — the syntax is becoming more
dependent on paid spend to hold the position it has, which is a
different and more precarious situation than a syntax whose organic
share is holding or growing alongside its ad spend.

**Each syntax carries its own economics — its own break-even ACoS, its
own contribution margin, and a stated ceiling on what's worth spending
purely to defend a position it already holds.** That ceiling is a cap,
not a target: spending up to it isn't automatically justified just
because the ceiling allows it. Alongside this, a syntax's own
competitive pressure is read directly — is the cost of bidding on this
syntax rising because the whole category is getting more expensive, or
because something specific to this account is driving its own price up
— since the two call for different responses.

**Match-type coverage is checked per syntax, not just per keyword.** A
Primary syntax running at 0% phrase-match coverage, for instance, is a
finding in its own right — not something that only shows up if an
individual keyword inside it happens to get flagged. This feeds directly
into this skill's discovery and harvest mechanics (§12): a coverage gap
like this is a standing, proactive reason to build discovery layers on
that syntax, not just something discovered reactively when a term
already inside Auto or Broad happens to clear its own harvest bar.

**Build status — a distinct read from coverage, computed directly from
the bulk file's own signals, not left as an unanswerable question.**
"Coverage" above asks whether a syntax has phrase or broad *at all*;
build status asks something more specific for each match type a syntax
does have: is it actually live, or built but not delivering? Read
straight from the bulk export, no additional data needed:
- **No campaign or ad group exists for a given match type on this
  syntax** — genuinely not built, not a delivery problem.
- **A campaign exists and its state reads paused** — built, deliberately
  turned off; state why if known, or name it as an open question if not.
- **A campaign exists, is enabled, and shows zero impressions across the
  current window** — built but not delivering, which is a different
  finding from either of the above and usually points to a bid, budget,
  or relevancy problem worth naming rather than a coverage gap requiring
  new construction.
- **A campaign exists, is enabled, and has impressions** — live and
  delivering; whatever performance-level diagnosis applies from here
  runs as normal.
This four-way read is what actually answers "what got built and what
didn't" for a syntax — stated per match type, not collapsed into one
blended coverage percentage that hides which specific gap is real.

**The syntax scan table carries every metric §1B names, not a subset.**
Keyword count, impressions, clicks, orders, spend, CTR, CVR, ACoS, rank,
the four-quadrant diagnosis, weeks in that state, priority class, and
actual-versus-target spend share — one row per syntax, no exceptions,
including syntaxes with zero delivery, whose zero is itself the finding.
A scan table missing spend and spend share cannot show which diagnosis
is expensive, which is the entire purpose of scanning before pricing.

**How this is presented — nine metric categories per syntax is too much
for one table, so this splits into two tiers, per the account's
existing table-and-visual standard, not a special format invented for
this section.**

- **A scan table, every syntax, no exceptions**: keyword count, spend,
  CTR, CVR, ACoS, rank, the four-quadrant diagnosis, weeks in that
  state, priority class, and actual-vs-target spend share. This extends
  the account's existing per-syntax table shape rather than replacing
  it. Followed by its own "what this table decides" synthesis, same as
  any other major table in the document.
- **A deeper narrative dossier, only for syntaxes that earn it**: a
  chronic state (four-plus weeks), a spend share materially off its
  class target, or a syntax in the oversight class (§1A). For those
  specifically, write out coverage completeness, listing coverage, rank
  velocity, the organic/ad dependency read, syntax economics, and
  match-type coverage in full — the same depth the account's framework
  defines for all of them, applied where the finding actually warrants
  the space. A tail syntax with none of those flags stays in the scan
  table only, per §1A's oversight-tiering rule; it does not get this
  dossier written for it every cycle.
- **A paired visual for spend-by-quadrant**, per the account's existing
  visual convention — one bar per quadrant, the prescribed action
  (scale / buy placement / no rank push / reduce and reallocate) stated
  directly on the chart, not left to a separate legend.

None of this is a new presentation standard — it's the same tiered-depth
and paired-visual convention already governing the rest of this
document, applied to a section with more metrics per row than most. The
same principle — a table without a chart is not a defect, a trend
buried only in table form when a chart would show it faster is a missed
opportunity — governs here exactly as it does everywhere else.

**New, not settled: how a syntax-level diagnosis actually constrains a
keyword's own verdict.** The source framework establishes that a
syntax's diagnosis governs its member keywords' mode of work — but the
specific mechanics of that constraint, stated for this skill's own
per-row logic, are new and should be flagged as such when they first
change a real verdict:

- **A syntax's diagnosis sets a ceiling or a mode, never a keyword's
  actual bid or action.** A chronic Conversion diagnosis freezes every
  member keyword's bid at its current maintenance level and removes any
  ranking allowance those keywords might otherwise have had under §6 and
  §7 — but it does not set what that maintenance bid actually is, and it
  does not decide which keywords inside the syntax get paused, cut, or
  held. Each keyword still computes that from its own clicks, orders,
  CPA, and history, inside the ceiling the syntax has set.
- **A Strong or Visibility diagnosis does not entitle every member
  keyword to a push.** It removes the syntax-level objection to
  pushing — it does not substitute for a keyword individually clearing
  whatever gate its own objective requires (the five-property gate for a
  ranking push, for instance, still has to clear on that keyword's own
  numbers).
- **The syntax rollup is signal, not verdict. The keyword is the
  decision.** A syntax-level finding never becomes one action applied to
  every keyword underneath it — every rule already in this skill about
  per-row independence (§1) still governs at the keyword level; the
  syntax layer adds a boundary above it, not a replacement for it.

---

## 1C. Product-level posture and TACoS — the same depth §1B gives syntax, one level up

**A product resolves its own posture once per cycle, before any keyword
cascade runs, and every keyword verdict beneath it inherits that
posture.** This is the Product level named in §1A — stated here in the
same depth §1B gives Syntax, because a product's own TACoS, margin, and
inventory state governs everything decided under it exactly as much as
a syntax's diagnosis does.

**The posture record — eight dimensions, read together, not in
isolation:**

- **Stage integrity** — the declared stage (Launch / Ranking push /
  Transition / Mature-defend / Harvest) checked against real graduation
  evidence (profitability, organic sales share, review posture, CVR
  stability), not left to run past its own evidence indefinitely.
  **Three specific mechanics, sourced from the account's own framework
  and not previously built into this skill:**
  - **Graduation** needs organic sales sitting above roughly 40–50% of
    total sales for the product, sustained — not just profitability
    alone — before a product is read as having earned its next stage.
  - **Each stage carries its own expected campaign mix**, checked against
    what's actually running: Launch leans discovery-heavy; Ranking push
    concentrates on Exact against the product's primary syntax; Mature
    carries a defensive layer, brand-format coverage, SD retargeting, and
    a low-budget Auto sentinel rather than an active ranking push. A
    product's actual campaign stack that doesn't match its declared
    stage is a named finding, not something to silently reconcile.
  - **Demotion has a real trigger, not just an informal sense that
    things are sliding**: organic sales share falling below its target
    for four consecutive weeks, or PPC dependency rising past its
    declared ceiling, formally reviews the product for demotion back to
    Transition. **Re-entering a ranking posture after that requires a
    fresh realism pass — drifting back into push-level spending without
    one is a violation of this rule, not a judgment call left open.**
- **TACoS vs. band, decomposed by objective** — covered in full below;
  this is the dimension your own question is really asking about.
- **Flywheel health** — organic share trend against target, and the
  product-level PPC dependency ratio: is this product earning its sales
  or renting them, the same question §1B asks per syntax, asked here for
  the whole product.
- **Revenue trend** Not
  organic share, not TACoS — total product revenue itself, read at two
  windows: week-over-week (this week against last) and month-over-month
  (this month's run rate against the prior month's). A product can be
  perfectly within its TACoS band and still be revenue-declining month
  over month; the band alone doesn't catch that, because a shrinking
  revenue base makes a stable percentage describe a shrinking dollar
  number. State both windows, and state plainly when they disagree — a
  week that's down against last week but a month that's still up against
  the prior month is a different situation from both windows agreeing.
- **Margin trend — and distinct from margin
  freshness below.** Freshness asks whether the margin *table* is
  current; this asks whether margin *itself* is moving, read the same
  two ways: week-over-week and month-over-month. A margin table can be
  perfectly up to date and still show a product whose margin has been
  quietly eroding for two months straight — rising COGS, a fee change,
  a competitive price hold — and nothing about table freshness would
  catch that decline. This is checked separately from freshness because
  they answer different questions: one is about whether the number is
  current, the other is about whether the number is good.
- **Margin freshness** — the margin table's own version date against a
  standing staleness rule (commonly 45 days) and against any known fee,
  price, or packaging change since. **Any FBA fee change (a size-tier
  move, a remeasurement result), price change, packaging change, or
  freight-cost step triggers re-derivation of the margin table and every
  ceiling it feeds within 48 hours, not at the next scheduled review** —
  this is the account's own specific trigger, sharper than the general
  45-day staleness rule alone. A SellerBoard true-up runs monthly
  regardless of whether any triggering event fired. A stale margin table
  is a named finding, not a silent assumption that old numbers still
  hold.
- **Inventory posture** — the aggregate read across the product's
  routed SKUs using §9's Green/Yellow/Red zones: Clear, Constrained, or
  Re-point active.
- **Listing and offer state** — open listing or price projects from
  Brand Management findings, and whether any syntax is currently in
  fix-first mode because of one (§1B's chronic Conversion state).
- **Structure hygiene** — a count of open structural findings: zero-Exact
  ranking terms (§9's same-day fix), duplicates, orphaned campaigns,
  coverage gaps, **and match-type/format spend-split deviation against
  the account's own reference targets** (Exact 55–60%, Broad 15–20%,
  Phrase 5–10%, Auto 5–10%, PAT ~5% of Sponsored Products spend; format
  split roughly SP 80%, SB 15–20%, SD 5–10%), reviewed monthly. **A
  deviation from these targets is a finding to explain, not an error to
  auto-correct** — a product genuinely concentrated in Exact because
  that's where its proven terms live isn't wrong just because it's off
  the reference split; the split is a portfolio-level check that prompts
  a look, not a rule that overrides what the product's own evidence
  supports.
- **Event and season posture** — any deal or peak window in the next few
  weeks, and which way the seasonal index for the product's major
  syntaxes is moving; the full operating mechanics are below, not just
  the flag.

**Three more standing checks, sourced from the account's own framework
and not previously built into this skill — read alongside the eight
dimensions above, not as a ninth item competing with them:**

- **Pacing deviation.** A product's actual spend pace swinging more than
  roughly 25% from its own normal day-of-week curve is flagged the same
  day it's noticed, not carried silently into the weekly read. This
  catches a budget or delivery problem while it's still a day old, not
  after a week of drift has already happened.
- **Manifest completeness.** Where the underlying data available for
  this product — pricing, competitor depth, cost inputs — falls below
  roughly 85% complete, the product is marked degraded rather than
  analyzed as if the missing 15% doesn't matter. A degraded read still
  produces verdicts, but every one of them carries the gap named, not
  silently assumed away.
- **MKL staleness.** Where the Master Keyword List itself hasn't been
  refreshed in roughly 30 days, it's flagged as stale before being
  trusted for a fresh build or a fresh set of verdicts — the same
  principle §1's indexing-gate fix applies to the indexing field applies
  here to the whole file: old data doesn't silently pass as current data.

**TACoS stage bands, the account's own reference bands, not this
skill's invention:** Launch ≤25% (dated, not open-ended); Ranking push
12–15%; Transition 8–12%; Mature-defend 4–7%; Harvest ≤4%.

**The actual derivation — the bands above are what to
check a number against; this is how the number itself gets set in the
first place, and it was missing entirely before now.**

**Weekly ad spend = target TACoS × projected weekly revenue.** That's
the whole mechanism. The projected revenue comes from the product's own
growth plan, if one exists; target TACoS comes from where the product
sits in its lifecycle. Once both are known, the dollar envelope for the
week is a single multiplication, not a judgment call.

**Target TACoS is set on weeks since launch, not just a stage label —
more precise than the bands alone suggest:** weeks 1–6 up to 1.5× the
product's own break-even ACoS; weeks 7–12 below break-even; weeks 13–25
below 75% of break-even; week 26 onward below 50% of break-even.
Break-even ACoS itself is margin per unit divided by AOV — the same
figure §3's ceiling logic already computes, cited here rather than
recomputed.

**"Weeks" here means weeks since the current push began, not weeks since
the product's original launch date — stated explicitly here because
nothing said this plainly before, and a literal reading would get a
legacy product wrong.** A product that has existed for years and is now
in a genuine growth push is not read against week 200-plus of its
original launch, landing it in the strictest, most conservative band by
a literal count that has nothing to do with what's actually happening
now. It's read against week 1 of *this* push — the same way a restocked
SKU's recovery push is funded toward its own pre-decline baseline (§9)
rather than treated as a brand-new, unproven campaign, and the same way
re-entering a ranking posture after stepping back requires its own fresh
start rather than a silent continuation of wherever the old count left
off. The clock restarts when the push restarts; it does not run
continuously from the product's first day in the catalog. **One discrepancy worth stating openly rather than silently
resolving:** the account's own source material states two different
figures for the launch ceiling in two different places — 25% in one
document, 35–45% in another. This skill defaults to the lower, more
conservative figure (25%) until the account confirms which one actually
governs; state this explicitly on any product where the launch-week
envelope is being set, rather than picking one silently.

**One named exception, not an open-ended allowance:** a single event
week may run up to 50% over its otherwise-derived envelope, pre-approved
before the event, never assumed after the fact because a week happened
to run hot.

**A weekly efficiency floor runs alongside the envelope, not instead of
it:** wasted spend (spend with no attributed order) should sit below
roughly 15% of total spend, checked at the same weekly cadence as
everything else in this section. A product can be within its TACoS
envelope in total dollars and still be failing this floor if a
meaningful share of that spend is landing on terms producing nothing.

**The formula above sets a number. It is never applied blind to that
number — the piece that actually connects the
formula to the product's real trajectory.** Before the derived envelope
is applied, adjusted, or escalated, four dimensions are read together,
not as separate, siloed checks each serving its own purpose: **rank
trend** (§7's three-window read — overall, 14-day, 7-day), **revenue
trend** (week-over-week and month-over-month, above), **margin trend**
(the same two windows, above), and **inventory posture** (§9's zones and
trajectory check).

**The product's declared goal (§6) is read first, and it's what decides
which of the four dimensions actually governs when they pull in
different directions — this was missing before now, and without it the
four-dimension read has no way to resolve a genuine conflict between
them.** The four dimensions aren't weighted identically regardless of
what the product is trying to do:

- **Growth/Scale** — rank trend leads. Margin softening is tolerated
  further, within the loss ceiling §7 already computes, because the
  declared goal is to buy the position; margin declining is a cost of
  the strategy, not automatically a reason to abandon it.
- **Profit-First** — margin trend and revenue trend lead; rank trend
  only matters for a campaign already protecting a won position (§6's
  carve-out), never for justifying a new push. A Profit-First product
  showing improving rank on a campaign with no funded push behind it is
  not a reason to scale spend — the goal doesn't call for that read.
- **Clearance/LTSF** — rank trend is dropped from this read entirely,
  consistent with §6's stricter nullification; it's irrelevant to a
  product being liquidated. Inventory and revenue lead, read specifically
  as recovery-per-unit against the declared clearance timeline, not
  against a growth trajectory.
- **Ranking and Profitability declared together** — the weighting
  splits by campaign, matching §6's own per-campaign objective split:
  Ranking-tagged campaigns read this four-dimension check the way
  Growth/Scale does; Profit-tagged campaigns on the same product read it
  the way Profit-First does. One product, two readings, resolved at the
  campaign level exactly as the objective tag already resolves it
  elsewhere.

**Only once the goal has set which dimensions lead does the combined
read below decide whether the formula's output gets applied as computed,
tightened below what the formula alone would allow, or flagged as a
finding requiring a decision above the row level:**

- **All four improving or holding** — the formula's derived envelope
  applies as computed; nothing here overrides it.
- **Rank improving but margin declining** — under Growth/Scale, this
  doesn't automatically mean cutting the push; it means recomputing the
  envelope against *current* margin, not the margin that was true when
  the push was originally sized, and stating which figure now governs.
  Under Profit-First, this same pattern reads differently: margin leads,
  so a declining margin is the finding that matters regardless of what
  rank is doing.
- **Revenue growing but inventory reading Yellow or Red** — the formula
  would authorize more spend than the product can actually fulfill.
  Inventory's zone caps the envelope regardless of what the revenue-based
  formula alone would produce, and regardless of declared goal — this is
  the product-level expression of the same precedence rule that already
  governs at the keyword level (§1A: gates outrank diagnosis outranks
  signals). Inventory is a gate, not a weighted dimension; it isn't
  reordered by which goal is declared.
- **Rank flat or declining alongside declining revenue and declining
  margin, together** — this is not a single-dimension problem to patch
  with a bid change; it's escalated as a product-level finding before
  any envelope adjustment is made mechanically, because a formula applied
  to a product moving backward on every dimension at once is treating a
  structural problem as a pricing problem.
- **Any single dimension moving sharply against the others** — named as
  a finding on the product's posture record even when the other three
  look fine; a divergence is exactly the signal this combined read
  exists to surface before it becomes a trend the blended envelope
  number would otherwise hide.

**The decomposition is the actual point, not the headline number.**
TACoS is never read as one figure — it's split by the objective the
spend is tagged under (Ranking ÷ total sales, Profit ÷ total sales,
Defense, Discovery, Conquest, each the same way), so a single TACoS
number can mean two entirely different things. **A 20% TACoS made of 4%
declared defense spend and 16% spend tagged "ranking" that is not
actually moving any rank is the exact failure pattern this decomposition
exists to catch** — the same headline number made of a properly sized,
dated, five-property-gated ranking push (§7) reads as a completely
different, defensible situation. This is the direct answer to "is a high
TACoS okay because we're buying rank" — it's okay when the decomposition
shows real, gated ranking spend actually producing rank movement; it is
not okay when the decomposition shows spend tagged "ranking" sitting on
terms with no five-property gate behind them, no matter how reasonable
the blended number looks.

**Clearing the five-property gate is necessary but not sufficient on its
own — inventory has to hold too, checked explicitly here, not left to be
inferred from the precedence rule below.** A ranking push can be
perfectly sized, dated, ceilinged, predicted, and funded on paper and
still be illegitimate spend if the routed SKU sits in a Yellow or Red
zone (§9): a push that would outrun its own inventory is not "buying
rank," it's buying demand the product can't fill, and the resulting
TACoS is not defensible no matter how clean the five-property gate looks
in isolation. **A high TACoS is validated as legitimate ranking spend
only when all three hold together and are named together**: the
five-property gate clears, the routed SKU reads Green, and actual rank
movement is showing in the data — not asserted from the first two alone.
State the inventory zone explicitly in the same breath as the
five-property status whenever a high TACoS is being justified as a
ranking push; citing the gate without citing the zone is an incomplete
justification even when the gate genuinely clears.

**TACoS-vs-band has four tiers, not a single trigger point — sourced
from the account's own framework, replacing this skill's earlier binary
version.** Read as a ratio of actual TACoS to the product's own stage
band:

- **Within — at or below 1.2× the band.** Normal; no action from this
  check alone.
- **Elevated — 1.2× to 1.5× the band.** A named finding, reviewed at the
  normal weekly cadence — not urgent, but not silently absorbed into
  "within normal range" either.
- **Breach — 1.5× to 2× the band.** New scale actions across the product
  freeze — a push freeze specifically, short of full code-red. Taper,
  fix-first, and defensive actions continue; nothing new starts until the
  product reads back below 1.5×.
- **Code-red — above 2× the band, or above 1.5× sustained for two
  consecutive weeks.** Every scale action across the product freezes
  (taper, fix-first, and defensive actions continue — this isn't a full
  stop, it's a stop on *growth*); every oversight-class term gets a full
  review within 48 hours; cadence moves to daily; exit requires two
  consecutive clean weeks with the decomposition able to explain every
  point of TACoS, not just an improved blended number. **This is not a
  hypothetical trigger — it is, in the account's own words, "the formal
  version of the current account situation," describing a real product
  running at roughly 20% TACoS against a ~7% mature target. This rule
  exists because that situation exists, not as an abstract policy.**

**What "full review within 48 hours" actually means, stated precisely
because this is the exact point worth getting right: it is the same
per-row decision sequence this skill already runs — every gate, every
diagnosis, the full rule set (§1's decision order start to finish) — run
on every important term, urgently, not a separate or different process
invented for the emergency.** The acceleration is in the *timeline*
(48 hours instead of the normal weekly pass, daily cadence afterward
instead of weekly), never in the *method*. This produces whatever
individual cuts, holds, or fixes each row's own data actually justifies
— one term might get cut hard, a neighboring term might not be touched
at all — because that's what running the real diagnostic system on each
one honestly produces. **It is never a blanket percentage taken off
every campaign to hit a number faster.** That would be the exact
across-the-board-cut failure this whole framework exists to prevent,
just done urgently instead of calmly — still cutting a genuinely working
push and pure waste with the same knife, only faster.

**A product sitting in Breach is not treated the same as one in
code-red** — this was the specific gap in the earlier binary version: a
moderately over-budget product and a badly over-budget one produced the
identical response (freeze everything, daily review) because there was
no tier between "fine" and "emergency." Breach gets the push freeze
without the daily-cadence, 48-hour-review escalation code-red requires.

**The product-level verdict vocabulary, parallel to but distinct from
any single keyword's verdict:** HOLD ENVELOPE / RAISE / CUT — the weekly
budget call, made from the TACoS read and the queue of sized pushes
waiting on it; envelope moves greater than 20% are human-confirmed, the
same discipline as any other large structural change. DECLARE CODE-RED —
as above. RENEW / DEMOTE STAGE — a stage tag expires on its own declared
date and needs real evidence to renew, not silent continuation. OPEN
LISTING / PRICE PROJECT — a chronic Conversion-diagnosed syntax (§1B) or
a price-competitiveness finding routes here, never absorbed as a PPC
bid problem.

**Pushes across the whole product are funded in order, not by
enthusiasm or recency.** Revenue potential at target rank, divided by
the cost to close the gap, ranks every candidate push against every
other one competing for the same capped envelope — subject to §7's
realism checks and §9's inventory gate. A push doesn't get funded because
it was proposed most recently or argued for most persuasively; it gets
funded because the arithmetic ranks it above the pushes it's displacing.

**After any scale step, check the marginal cost of that specific step,
not just the new blended number.** Marginal ACoS = the change in spend
divided by the change in ad-attributed sales, measured across the two
periods the step actually spans. Where marginal ACoS runs more than 2×
the running blended ACoS, that specific step bought little and is
unwound — regardless of how tolerable the new blended ACoS looks on its
own. A blended number can hide a bad last step inside a history of good
ones.

**Concentration is checked and requires a stated reason once it's
breached.** A single term carrying more than roughly 25% of the
product's clicks, or the top five terms carrying more than roughly 60%,
is fine when it's a declared, active head-term push — it's a finding
requiring an explanation when it isn't declared.

**Five precedence rules that resolve conflicts between this level and
everything below it, stated because they change what a keyword-level
verdict is allowed to do:**

- **Gates outrank diagnosis; diagnosis outranks signals.** A Red
  inventory zone (§9) or any other hard gate vetoes a scale verdict from
  any level below it, mechanically — a strong syntax diagnosis or a
  strong individual keyword case doesn't override a gate.
- **The product envelope outranks keyword ambition.** When multiple
  pushes compete for a capped budget, the funding order above decides;
  no keyword gets funded past the envelope because its own individual
  case looks strong. This is the product-level form of the same
  principle that already governs syntax spend-share caps (§1B) and
  per-row independence (§1) — the boundary tightens as you go down the
  waterfall, never loosens because a lower level argues hard enough.
- **A stale margin table blocks every ceiling-referencing verdict it
  would touch.** Margin freshness isn't a background housekeeping item —
  when margin and performance data disagree about urgency, the margin
  number wins, because an "efficient" campaign measured against wrong
  margin numbers isn't actually efficient.
- **Family term ownership outranks a strong product-level case (§1A).**
  A product doesn't unilaterally decide it deserves a shared head term
  because its own numbers look good; family-level ownership assignment
  governs, and overriding it requires a logged re-assignment at that
  level, not a product-level argument.
- **A weekly human audit outranks whatever an automated pass decided
  between cycles.** Where both touched the same target, the audit's
  value is the one that stands, and any automated action taken since is
  reviewed at the next audit rather than assumed correct because nothing
  flagged it.

**The account reaches its blended TACoS target product by product,
through these stage bands — never by an across-the-board cut.** A flat
percentage haircut applied to every campaign on every product cuts a
winning ranking push and genuine waste with the same knife. The target
is reached by managing each product's own band, its own decomposition,
and its own code-red triggers — not by a single number applied uniformly
regardless of what's actually happening underneath it.

### Event Mode — deals get their own operating state, not just a data flag

**A deal window switches the product into its own mode, on its own
timeline, not a passive adjustment to the weekly cadence.**

- **Pre-event ramp.** The moment a deal calendar window opens, budget
  caps are set in advance — not discovered live — and any dayparting
  boost is removed entirely for the window's duration. The event bid
  plan is pre-staged against **max-sales-day** days-of-cover, not average
  daily cover — a SKU can look comfortably stocked on an average day and
  still run out on the single highest-velocity day of a deal, and the
  pre-stage check exists specifically to catch that before the event
  starts, not during it.
- **Live event.** Pacing is checked same-day against the event's own
  projection, not the ordinary weekly cadence. Where actual pacing runs
  ahead of the projection, that's a deliberate call made at the product
  level — spend more into a deal that's clearly working — never
  unexamined drift discovered after the fact.
- **Post-event — a two-week guard, not just the event days themselves.**
  Event-week rates are excluded from trend verdicts for two weeks after
  the window closes, not only during it — a rank or CVR echo from the
  event genuinely lingers past the last day of the deal itself. Floors,
  ladders, and ceilings resume from their pre-event values once the
  guard lifts, unless the event itself produced real evidence
  (a genuinely higher sustainable rank, for instance) that justifies
  resetting them.

**The arithmetic that matters most: a discount cuts contribution by its
full depth, and that has to be computed before the window opens, not
inferred from how the event looks once it's live.** A price cut doesn't
shrink margin proportionally — COGS and fees are largely fixed, so the
entire discount comes out of contribution directly, and the affordable-
CPC ceiling can collapse far faster than the discount percentage alone
would suggest. **This is the specific trap: CVR typically rises during a
deal, and a rising CVR reads as "this is working, bid more" — but the
ceiling that bid is being measured against may have shrunk at the same
time, from the same event, for the opposite reason.** Compute the
deal-state ceiling from the deal price and deal-state CM2 before the
event starts; never let an in-event CVR reading justify a bid the
pre-computed deal-state ceiling wouldn't support.

**A deal window amplifies a push that's already been decided — it never
originates one on its own.** A term with no funded, gated ranking case
behind it doesn't get one manufactured just because a deal window is
open; the event is a visibility multiplier on a decision already made
under §7's ordinary gates, not a separate justification for spending that
wouldn't otherwise be authorized. Where a syntax's own seasonal search-
volume index is rising in the next several weeks, that's a green light
for **funding** a new push through the ordinary process — it doesn't
skip the process.

**A falling seasonal index does the opposite: it denies new pushes and
starts pre-emptive tapers on the affected syntaxes**, ahead of the actual
decline showing up in performance data — timing the wind-down to the
demand curve rather than reacting to it after spend has already been
sitting on a shrinking opportunity for weeks.

**Deals are also this account's designated clearance mechanism for
aged and terminal-tagged stock — not a PPC lever.** Where a SKU carries
an LTSF or terminal tag, the deal calendar is the primary tool for moving
it, and PPC's role is supporting visibility into an already-scheduled
clearance window, never substituting advertising spend for the discount
itself. This is consistent with §9's peak-vs-LTSF priority rule: peak
availability protects rank; deals liquidate aged stock. They're not the
same lever solving two different problems.

---

## 2. Objective assignment

Assigned at the campaign level, by targeting type, before any bid decision:

| Targeting | Objective |
|---|---|
| Brand name in the keyword | Defensive |
| Exact match | Ranking, or Market Share if declared (see note below) |
| Auto targeting | Discovery |
| Broad match | Discovery |
| Product/category targeting | Profitable Conversion / Conquest |

**Market Share is the one objective targeting type alone doesn't
settle, sourced from the account's own campaign architecture and not
previously built into this skill — a real, distinct sixth objective,
not a variant of Ranking.** An Exact-match campaign can be either
Ranking or Market Share, and the difference is what the campaign is
actually trying to buy: Ranking chases organic position; Market Share
chases impression share and paid auction presence, and is judged and
priced differently (§2C). State explicitly which one a campaign is
whenever both are plausible — never assume Ranking by default just
because the targeting type matches.

| Objective | Judged on | Never judged on |
|---|---|---|
| Ranking | The §7 progress test; rank movement against a computed loss ceiling, gated by §6's product-goal check | Weekly CPA alone |
| Market Share | Impression-share band migration and cost to hold it, per §2C | Organic rank movement |
| Profitable Conversion | CPA vs. ceiling; realized CPC vs. affordable CPC | Rank movement |
| Defensive | Share held and cost of defence, per §2B | CPA alone |
| Discovery | Harvest performance and graduation rate, per §12 | CPA in the first cycle |
| Conquest / ASIN targeting | CPA plus share of the target page, per §2B | Keyword-loop metrics |

**A campaign tagged Ranking by targeting type is not automatically entitled
to ranking treatment — §6 checks that before §7 ever runs.**

---

## 2A. Exact launch selection — which keywords qualify, and in what order

**1. Goal, read first — sets which tiers are even eligible before
anything else is checked.** Pull the product's declared strategic goal
(already a required intake input, not re-derived here):

- **Growth/Scale** — both relevancy tiers (below) are eligible this
  cycle, subject to everything that follows.
- **Mixed** — for the specific decision this section makes, Mixed
  behaves exactly like Growth/Scale. Every keyword this section
  selects is an Exact keyword, and an Exact keyword always tags
  Ranking regardless of the product's overall declared goal (§2) — so
  there is no separate Mixed rule to apply here. What "Mixed" actually
  changes is a different decision entirely — whether the product also
  runs product/category-targeting campaigns funded from the same
  budget (§6) — and that's untouched by this section.
- **Profit-First** — highly-relevant tier only, permanently. This is
  not "narrower for now" — semi-relevant never opens for this goal,
  cycle after cycle, regardless of how the highly-relevant tier
  performs.
- **Clearance/LTSF** — highly-relevant tier only, permanently, and at
  the specific bid/placement treatment named in the table below. The
  goal here is selling through what's already on hand, not building
  rank on inventory the product is exiting — semi-relevant never
  opens, and highly-relevant itself launches deliberately cheap.

**2. TACoS and margin, read second — sets the spend envelope within
whatever the goal just allowed.** Pull the product's current TACoS
position and margin trend (§1C, already resolved once per cycle, not
recomputed here). A goal that permits both tiers doesn't mean both
tiers get funded if the product is already at or past its TACoS
ceiling, or margin trend is declining — this step can narrow what
Step 1 allowed; it never expands past it.

**3. Already targeted?** If a term already carries a live keyword row
in the bulk, it is not a new launch — it is a reactivation, handled
directly in Final Bulk rather than through this selection process.

**4. Search volume floor.** A minimum search volume is required before
a term is worth a dedicated campaign — commonly 250 SV in this
account's practice, but confirm the number for the specific product
rather than assuming it carries over unchanged; it is the account's
own convention, not a fixed constant of this skill's logic.

**5. Relevancy — tiered, not a single pass/fail gate, and the tiers
launch in sequence, not all at once.**

- **Highly relevant**: the term names the product exactly as it is —
  every defining attribute present, not just the general category. For
  a cooling *fitted* sheet, "cooling fitted sheet" is highly relevant;
  "cooling fitted sheet queen" is highly relevant. This tier launches
  first, and fully — every eligible segment in it, not just the
  tightest-ranked ones — before semi-relevant is even considered.
- **Semi-relevant**: qualifies by **either of two independent
  mechanisms, one sufficient on its own:**
  1. *Missing the sibling-disambiguating feature* — the term names the
     correct general category but is missing the qualifier that
     distinguishes this specific product from an adjacent one in the
     same family. "Cooling sheet" (no "fitted") against a flat-sheet
     sibling is this case.
  2. *Secondary synonym, not the canonical name* — the listing markets
     itself under a second product-form word in addition to its
     literal name (§1B), and the term uses that second word rather
     than the canonical one. A Cooling Comforter listing that also
     markets as a "Cooling Blanket" makes "cooling blanket" queries
     this case — real intent, correctly paired with the attribute, but
     using the marketing synonym rather than the product's own name.

  **This tier is deliberately held, not simply lower-priority — see
  the opening gate below for exactly what has to clear before it
  opens, and what happens if it never does.**
- **Not relevant**: wrong category, wrong material, a competitor brand
  name (never targeted in Exact — conquest runs through product
  targeting only), an own-brand term (routed to the defensive campaign,
  not the launch roster), or a term that simply doesn't belong. Dropped
  outright, named with the specific reason.
- **Unclassified**: matched no rule cleanly. Not dropped, not launched —
  flagged for re-scoring next cycle rather than defaulted into either
  tier above.

**The mechanism above transfers to every product; the specific defining
attribute or secondary synonym it checks for does not, and has to be
re-derived fresh each time.** "Fitted" is what separates one cooling-
sheet product from its flat-sheet sibling; "blanket" is what a
different product's own listing happens to market itself under — never
carry either forward as if it generalizes on its own. Before this
tiering can run at all, identify the product's own defining attribute
from its listing and sibling family, and check its title and bullets
for whether it uses a second product-form word under either mechanism
above. Where a product has no close sibling and no secondary synonym in
its own listing, the highly-relevant tier may simply be "names the
product's core category correctly" — state that explicitly rather than
inventing a distinguishing feature that doesn't exist.

**The semi-relevant opening gate — six items, all of which must clear,
plus one advisory item — checked every cycle the tier stays closed, not
just once.** This only applies where Step 1 made semi-relevant eligible
at all (Growth/Scale or Mixed) — Profit-First and Clearance/LTSF never
reach this gate, regardless of status.

1. **Rank achieved vs. rank target** — has the highly-relevant tier's
   own evidence-based rank target (the segment-level scale from §1B)
   actually been reached, or moved meaningfully closer?
2. **Five-property push gate cleared** (§7) — the highly-relevant
   push has had a legitimate, properly-sized test, not an informal
   attempt that never actually qualified as a real push.
3. **TACoS still inside band**, after funding highly-relevant (§1C).
4. **Margin trend holding or improving**, not declining, as a result
   of the push (§1C).
5. **Spend realized vs. planned** — the highly-relevant campaigns are
   actually spending near their allocated budget, not badly
   under-delivering. A push that hasn't spent its own budget hasn't
   had a real test yet.
6. **Minimum data window satisfied** — enough real time has passed to
   trust the read, per this account's own data-window convention, not
   a snapshot.

**Advisory only, not blocking:** Discovery-layer overlap — check
whether Auto/Broad discovery campaigns are already surfacing this same
semi-relevant demand well enough that it would harvest through the
existing pathway on its own (§12's harvest-and-negate rule already
handles that case cleanly; this check exists for the residual case of
a semi-relevant candidate with no prior Discovery history to harvest
from at all).

**If the six-item gate doesn't clear, that isn't a passive "wait and
recheck" state.** Pull the levers already available — bid, placement,
budget — and make a genuine attempt to fix what isn't working, the
same grading discipline this account already applies to any lever
before repeating it. **After 2–3 cycles of real lever adjustments still
failing to clear the gate, persistent non-clearance itself becomes the
trigger** — semi-relevant opens not because the six items technically
passed, but because staying stuck on a demonstrably non-working push,
even after genuine correction attempts, is its own failure worth
acting on. State this explicitly as the reason when it happens, rather
than quietly opening semi-relevant and letting it look like the gate
cleared normally.

**Coverage order within whichever tier is open: rank-target order,
tightest first** — the segment-level scale from §1B, not launch order,
alphabetical order, or search volume alone. A tight-target segment
launches before a loose-target one within the same tier, every time.

**Bid and placement — driven entirely by the product's goal, not by
rank-target tightness.** The rank-target scale's job stops at
sequencing (above); it never touches bid or placement, so the two
mechanisms don't get conflated.

**Amazon's suggested bid range per keyword is asked for explicitly
before this table is applied to any row — never estimated, never
carried over from a different keyword or a prior cycle.** The table
below names a position *within* that range (middle, or lower end); it
has no meaning without the actual range to place it inside. Where a
suggested range hasn't been provided for a specific candidate keyword,
that's a named gap blocking a bid decision on that row, the same as
any other missing required input — not a reason to estimate one from
a similar keyword's range or a category norm.

**This table's position never overrides the account's own absolute
backstop — stated explicitly here since the table alone doesn't say
so.** Every keyword this section selects is Ranking-tagged (§2), and a
Ranking row is *not* capped by a plain CM2×CVR formula the way other
objectives are — capping the bid that way would cap the exact thing a
ranking push exists to do (§7). **What actually bounds it is the
account's flat, absolute sanity ceiling (commonly ~$8–9), which each
SKU's own CM2 may only tighten, never loosen past.** A suggested-range
midpoint landing above that flat ceiling on a thin-margin SKU still
gets clamped down to it — the goal table sets *where in the suggested
range* to aim, the flat ceiling sets the true outer wall no goal
overrides.

| Goal | Bid | Placement |
|---|---|---|
| Growth/Scale | Middle of Amazon's suggested range | 100% Top-of-Search, from launch |
| Mixed (Exact/Ranking side) | Lower end of suggested range | 100% Top-of-Search, from launch |
| Profit-First | Lower end of suggested range | 100% Top-of-Search, from launch |
| Clearance/LTSF | Lower end of suggested range | None |

**6. Malformed or junk.** ASIN fragments, garbled strings, and listing-
title scrapes (a long string that reads as a copy-pasted title rather
than a query a shopper would type) are dropped regardless of what tier
they'd otherwise fall into.

**7. Duplicate and singular/plural collapse — one identity, not
several.** Exact duplicates (same text, same match type, already
running in more than one campaign) collapse to whichever instance the
dedup rule already keeps. Singular and plural forms of the same term
collapse into one canonical identity, keeping whichever form carries
the higher search volume — running both would bid against each other
in the same auction for no benefit. **Word-order variants do not
collapse** and launch as separate terms; word order reflects genuinely
different search behavior, not the same query typed twice.

**8. Routing eligibility — checked per term, at the point each
surviving candidate would actually become a campaign, not as a
one-time filter over the whole tier.** By the time a term reaches this
step, Steps 1–2 have already set which tiers are in scope and how much
budget exists; this step is the last, individual gate before a
specific term gets its own campaign. The SKU the term would route to
must clear whichever inventory floor governs a fresh launch — the
lower threshold that governs whether a SKU is safe to route to at all
(commonly 21 days), not the higher 60-day gate that governs authorizing
more demand into an already-running push (§9). A brand-new launch is
answering the first question, not the second. **A term that fails this
check simply never gets a campaign built** — excluded from this
cycle's coverage and re-checked next cycle, never launched and then
paused after the fact.

**A query naming a specific attribute may only route to a SKU sharing
that attribute; an unqualified query may use the syntax's ordinary
priority flow. Contexts governed: new-launch routing, reactivation
routing, re-route of an existing row whose SKU no longer qualifies,
and any routing written into a coverage or discovery tab — every point
at which a term is paired with a SKU, without exception.** On a real
build this rule was applied to new launches only, and a reactivation
pass routed "white cooling sheets" to a black child, "black cooling
sheets" to a cool-grey one, and "grey cooling sheets queen" to navy —
three rows, each of which would have bought clicks for a colour the
shopper did not ask for. A colour, material, or other attribute stated in the
query is not negotiable at routing time — "purple sheets" routes to the
Purple child or nowhere, never to Lavender because Lavender happens to be
in stock.

**Close colour variants are the one exception, and only where the
account confirms the pair.** A bare colour word that names the same
colour family as a carried child — "green" against a Mint Green child,
"grey" against Light Grey — may route to it. This is not the same as
substituting an unavailable colour for a different one: the shopper
named the colour they want and the child genuinely is that colour, just
more precisely described on the listing than in the query.

**Three conditions, all required.** The pair is confirmed by the account
for this product, never inferred from the words looking similar — the
same discipline the near-miss size mapping carries, and for the same
reason. **Every other gate still applies unchanged**: a confirmed colour
pair settles the colour question only, and a child failing inventory,
relevancy, volume or duplication is still blocked on those grounds. And
the row states that its colour routing was ruled rather than derived, so
a later cycle can see which pairs rest on a ruling.

**What this does not license.** A query naming a colour the product does
not carry in any variant still routes nowhere. "Purple" against a range
with no purple child is declined, not routed to the nearest hue — the
exception covers a more-precisely-named version of the same colour, not
a different colour that happens to be adjacent. A generic or sizeless query carries no such constraint and may
route through the syntax's ordinary priority flow. Where the
attribute-matching SKU is out of stock and no substitute is permitted,
the term holds at the bid floor rather than being rerouted — restored on
restock, not substituted around.

**This same collapsing rule feeds the discovery candidacy count.** Once a
term clears launch and is live at Exact, its combined click history — its
own clicks plus whatever collapsed into it under step 7 — is what §12's
100-click candidacy threshold counts against. A term and its collapsed
singular/plural partner share one count; a term and its word-order
variant do not, because they were never the same identity to begin with.

**A routing change during the measurement window does not reduce the
candidacy count — that carve-out applies only to eligibility, not to
trust.** The 100-click threshold asks whether a term has earned enough
raw exposure to justify a Phrase/Broad attempt, and clicks generated
before a reroute still answered that question honestly. But once a term
is live in Phrase or Broad, its ongoing CPA, CVR, and ACoS are judged
under §11's SKU-provenance check exactly like any other row — a term
that cleared candidacy partly on a since-rerouted child still needs its
*current* performance checked against whichever SKU is actually running
now. Provenance doesn't gate whether a term gets to try discovery; it
still gates whether its results, once there, are trusted.

---

## 2B. Defensive and Conquest — what governs each

**Provisional tier — the Defensive and Conquest bid-setting rules below are asked about before they first drive a real decision on a product.** Both objectives previously carried only a summary of what they were judged on, with no bid-setting rule and no defined measurement; what follows is reasoned rather than confirmed against the account's own standard. The first time either would set a real bid or decide eligibility on a product, ask. Once confirmed for that product it holds for every later cycle without asking again.

### Defensive

**Priced to CM2 × CVR on the advertised SKU — the same ceiling logic as
every other objective, not a different formula because the campaign's
purpose is different.** A Defensive campaign's job is protecting a
branded query from a competitor sitting on it, not converting
incrementally, but that job still has a price past which it stops making
sense, and the ceiling is computed the same way it is everywhere else in
this skill.

**An above-ceiling allowance exists for Defensive, narrower than
Ranking's.** It opens only when a competitor or a non-brand seller is
actually appearing against the branded term — checked from the search-
term report or a placement capture, never assumed because the term is
branded. Where no such presence is found, there is nothing to defend
against and the campaign prices at plain CM2×CVR like any Profitable
Conversion row. Where a competitor is found, the allowance is bounded by
the same flat account-wide sanity ceiling that bounds Ranking's — it may
tighten per-SKU, never loosen past it.

**"Share held" is impression share, or search-term impression share where
available, measured per branded query — this specific keyword's own
share against its own prior baseline, not a figure blended across every
branded term the product runs.** Where an individual query genuinely
doesn't carry enough impressions to read on its own, a blended reading
across the branded set is a named fallback, stated as such, the same way
the pool-basis fallback in §11 is named rather than silently substituted
— it is not the default because it's convenient. A Defensive campaign is
judged on whether that share holds or erodes, read over the same cadence
as any other weekly review, never on CPA in isolation.

**Reverses when:** no competitor or non-brand presence is found on the
term across two consecutive reads. At that point the above-ceiling
allowance is withdrawn and the row prices back down to plain CM2×CVR —
defending against nothing is an ordinary Profitable Conversion decision
wearing a Defensive label, and pricing it as if a threat still existed
would be the same failure as an un-tapered Ranking push.

**Six named states, sourced from the account's own framework, cover the
rest of what a Defensive row actually needs — this skill's version above
was one paragraph where the account's own rule is a family:**

- **Correct state.** Impression share held, ACoS within 10–15% of
  ceiling: ladder the bid down roughly 10% a week to find the floor that
  still holds share, and record that floor once found. **Never scale
  past it** — branded scale is mostly cannibalized organic demand, not
  incremental sales, so a Defensive row earning more spend isn't
  evidence it should get more.
- **Share slipping, or a competitor's ad on our own detail page.**
  Restore one ladder step, and open or expand PAT self-targeting to
  occupy the page directly — a coordinated response across two levers,
  not a bid move alone. The syntax's own defense budget (§1B's economics
  dimension) is the ceiling on this response, not a blank check.
- **Utilization below 100%.** Defensive campaigns target full budget
  utilization specifically — unlike every other objective's utilization
  band, a Defensive row's budget is fixed to 100% before its bids are
  touched at all. A Defensive campaign not spending its full budget isn't
  "efficient," it's under-defended. **The other objectives carry their
  own utilization targets, sourced from the account's own framework and
  completed here rather than left partial: Ranking targets 80%+
  utilization** — a ranking push under-spending its own budget is
  leaving required clicks unfunded, the same finding as a traffic
  deficit (§7) approached from the budget side rather than the bid side
  — **and Discovery targets 70%+** — lower than Ranking's, because a
  genuinely new candidate's spend is expected to ramp rather than run at
  full utilization from day one, but still a floor, not an unbounded
  allowance to under-spend indefinitely.
- **A competitor actually conquesting our branded SERP** — their ad
  sitting above our own organic slot on our own brand term. This is a
  full-stack response, not a single lever: restore the ladder step, add
  a Sponsored Brands headline on the brand root (and SBV if none exists
  yet), and PAT self-target the specific ASINs under attack. Reviewed
  weekly until the attacker's presence actually drops, not assumed
  resolved after one cycle.
- **Branded ACoS drifting up while share holds.** Source the inflation
  first — if a competitor is bidding our own brand term up, cap at the
  defense budget and accept whatever share that budget can hold. **Never
  chase branded CPC past the ceiling, and never scale into it** — an
  auction someone else is deliberately inflating doesn't get out-bid by
  spending more, it gets defended within a stated limit.
- **Branded-term CVR collapse.** Check the listing first, always, before
  any bid read — suppression, buy-box loss, a review-score drop, a
  variation break. Branded CVR is the cleanest listing-health signal in
  the account, precisely because branded traffic already knows what it
  wants; a branded conversion collapse is a listing finding almost every
  time, not a bid problem wearing a Defensive label.

### Conquest

**Already targeted? Checked first, before the eligibility gate below — the same gap just closed for Broad/Phrase, closed
here too.** Before running any fresh eligibility test against a
candidate target ASIN, search for that same ASIN already targeted in
an existing Conquest campaign anywhere in the account. **If one exists,
pull its current state and its actual performance data and decide from
that** — reactivate, adjust the bid, or leave it running as-is —
rather than opening a second campaign against a target already being
watched. Only a genuinely new target, with no existing instance found,
proceeds to the eligibility gate below.

**The eligibility gate — named S-C1 elsewhere in this skill, defined
here in full rather than only cross-referenced.** A Conquest campaign
against a specific competitor ASIN opens only when the routed SKU wins
on at least two of three — price, rating, review count — against that
target, **or** the target is currently out of stock. Below that: held,
not opened, regardless of how attractive the target otherwise looks.
This is the same test §7's State E investigation uses to check whether a
competitor has genuinely earned an outranking position; here it governs
entry into a campaign rather than diagnosis of a rank collapse, but it is
one test, not two different ones that happen to share a name. **"S-C1"
is this skill's own shorthand for that test — the delivered reasoning
never uses the label itself, only the actual comparison it names:**
"we win on price and reviews, lose on rating — two of three, clears the
bar" reads the decision in the plan; "clears S-C1" does not, per the
no-jargon rule above.

**When this gate can't be run because price, rating, or review count for
the target hasn't been pulled, that gap is asked about directly before
it's logged as a wait.** This is the exact case the data-conditions
register's ask-first principle covers: missing competitor data is
something whoever is running this build might already have on hand or
can look up in a minute, not something that needs a cycle to pass. "Held
— evidence pending, revisit next cycle" on a row that could clear the
moment someone answers "what's their price and rating" is the row
sitting idle for no reason. Ask once; log it as a dated gap only if the
answer is genuinely "that data doesn't exist yet."

**Priced to a watch-CPA, benchmarked against the target's own economics,
not a flat number.** The ceiling is the lower of (a) the routed SKU's own
CM2×CVR, computed exactly as it is everywhere else, or (b) a price-gap-
adjusted figure reflecting how large the price advantage against this
specific target actually is — a bigger gap justifies a somewhat higher
watch-CPA, because a click landing on our page after comparing against a
more expensive listing converts at a better rate than the same click
would against a near-identical price. State which of the two governs on
the row, and the arithmetic behind it, the same as any other ceiling.

**"Share of the target page" is the impression or click share captured
on that competitor's own detail page** — read from the product-targeting
placement's own data, never inferred from account-wide traffic ratios
when a direct read is available.

**Reverses when:** the target is delisted (drop it, exclude from the next
read entirely, don't silently carry a dead target forward); the target no
longer clears S-C1 (their price, rating, or review count moved enough
that the win-on-two-of-three test now fails — hold, don't keep spending
against an edge that's gone); or measured CPA exceeds the watch-CPA for
two consecutive reads with no offsetting gain in page share.

**Every target carries a named archetype, sourced from the account's own
framework, so the response is decided before it's needed rather than
argued fresh each time a target clears entry.** Fortress (a deep review
or IP moat protects their position — conquesting is a long, expensive
game against this archetype, sized accordingly, not treated the same as
an easy target); Investor (spending heavily to buy position rather than
earning it organically — vulnerable to a spend war neither side wins,
worth watching for signs they stop funding it); Price Leader (their whole
position is the price — competing on relevance and proof works better
than competing on price against a listing built to win on price); Copier
(a newer entrant mimicking an established listing with no real
differentiation — often the easiest, most time-limited win); Fader
(declining reviews, rating, or rank velocity — a target worth taking
now, before it exits the market on its own and the opportunity
disappears with it). **The archetype doesn't change whether S-C1 clears
— it changes what happens after it does:** two targets can both clear
entry and still deserve very different watch-CPAs, campaign durations,
and review cadences depending on which archetype they are.

**A CPC efficiency check runs alongside the entry test, separating
market-wide inflation from a bid problem that's ours alone.** Compare
this row's own CPC against the family median CPC on the same term — a
gap above 1.5× the family median is flagged, and the two readings call
for different responses: family-wide inflation means the whole category
got more expensive and no amount of bid discipline changes that; a gap
that exists on our own row alone, with the family median unchanged,
means the bid itself is the problem, not the market.

**A Conquest campaign's lifecycle has three states, not two — Open,
Rotate, and Exit, sourced from the account's own verdict vocabulary.**
Open is everything above. Exit is a reversal above firing with no
comparable target available to replace the one being dropped. **Rotate
is the case in between: a reversal fires on the current target, but a
different competitor ASIN now clears S-C1 and is a genuinely better
candidate** — the campaign's budget and structure carry over to the new
target rather than being torn down and rebuilt, since the campaign
itself isn't the thing that failed. State explicitly which of the three
a Conquest verdict is; "exit" and "rotate" read very differently even
though both end the current target's campaign, and collapsing them into
one undifferentiated "stop" loses the difference between "this approach
is done" and "this specific target is done, the approach continues."

**Neither objective gets its own separate writing convention.** A
Defensive or Conquest row's reasoning still runs the full §13 chain — its
own numbers, its own history, the arithmetic shown inline, what reverses
it — exactly like a Ranking or Profitable Conversion row. These rules
supply what a Defensive or Conquest verdict is actually computed from;
they do not exempt the row from being written up the same way every
other row in this skill is.

---

## 2C. Market Share — a real, distinct objective, not a Ranking variant

**Market Share chases impression share and paid auction presence at the
syntax level — organic rank is not the point, and a row here is never
judged on it.** Where Ranking asks "can this term win organic position,"
Market Share asks "does this syntax hold enough paid presence in the
auction, at a cost that's still worth paying." Both can run on Exact
match; the objective tag is what tells them apart, and it's declared,
never inferred from targeting type alone.

**Eight states, sourced directly, covering entry, defense, structure,
and timing:**

- **Headroom.** A primary root sitting below roughly 12% impression
  share, still profitable within its normal band: expand coverage across
  the root — both the exact set and phrase — and step budget up,
  tracking where impression share actually migrates as spend rises
  rather than assuming it will.
- **Dominance bought too expensively.** Impression share at or above
  roughly 41% but ACoS above its band: the share itself isn't the
  problem, the price paid for it is. Hold the share already won, but
  ladder down to the minimum CPC that still preserves it — watch the
  same marginal-ACoS check (§3) that governs every other scale action.
- **Cap enforced.** A secondary syntax exceeding its own spend-share cap
  — regardless of how well it's performing — gets reduced back to the
  cap, with the excess budget returning to the primary syntax. A strong
  week on a secondary syntax does not change its priority class; good
  performance on the wrong syntax doesn't earn it a bigger share.
- **Coverage worklist.** A relevant taxonomy cell (a size, colour, or
  attribute variant) with zero funded campaigns is either funded or
  explicitly declined and logged — never left silently uncovered.
  Search-volume coverage percentage is the tracked outcome, not keyword
  count.
- **Step and verify.** A funded root whose impression share has been
  stuck at its band floor for two or more cycles, with ACoS still in
  band and budget healthy: one budget step within the existing envelope,
  then verify whether impression share actually moved in two weeks. If
  it's still stuck after that step, the constraint isn't budget — it's
  auction position — and the next move is checking the TOS modifier and
  the expected CPC, not adding more budget on top of a placement problem
  more money won't fix.
- **Structure gap.** A primary root running at 0% phrase coverage is a
  finding in its own right (§1B's match-type coverage check, applied
  here specifically): stand up phrase on the root at a modest budget to
  catch modifier-level demand phrase naturally reaches; any winners it
  surfaces graduate through the ordinary harvest mechanic (§12) like any
  other discovery find.
- **Do not chase falling demand.** Where the seasonal search-volume
  index for a root is declining, hold or contract rather than expand —
  share gained into a shrinking market is bought at peak cost for
  trough-level volume. Re-time any planned expansion to the rising side
  of the seasonal curve instead of pushing against a falling one.
- **Distribute via variation flow.** Where a root's share gains are
  concentrated on one variation while sibling variations starve or run
  thin, apply the variation priority map (§9) to rebalance spend across
  children — a share position that rides entirely on one
  stockout-vulnerable child is a fragile position, not a secure one, no
  matter how strong the headline share number looks.

**Market Share follows the same writing standard as every other
objective** — its own numbers, its own history, what reverses it — per
§13; nothing about being a newly-added objective exempts it from that.

---

## 3. Economic ceilings

- **Affordable CPC = SKU contribution (CM2) × the delivering placement's
  own conversion rate.**
  **That conversion rate is the product's own fixed planning assumption
  for that placement — set once for the product and held stable — never
  the campaign's own recent rate.** §10 governs this and the reason is
  circularity: a ceiling built from a campaign's own current conversion
  moves with that campaign's performance, so a row sitting near its own
  average is inside its ceiling by construction and the comparison
  measures nothing. It also shrinks a row's headroom in exactly the week
  a rough patch means it needs room, and inflates it on a temporary
  spike.

  **A campaign's own placement data answers a different question, and
  only that one: whether a placement has earned the right to be lifted
  toward the ceiling** (§4's rest-of-search gate — 15+ clicks converting
  at or above that campaign's own base rate). What the ceiling *is* comes
  from the product's planning assumption; whether a placement may rise
  *to* it comes from that campaign's own clicks. **Conflating the two
  reverses decisions in the dangerous direction.** On a real build the
  product's fixed rest-of-search assumption was 3.67%, giving a $1.02
  ceiling, while one campaign's own recent rate was 5.94% — and a ceiling
  built from that campaign's own number came out at $1.65, which was then
  used to justify holding a $1.25 bid that the product's actual economics
  do not support. The correct action was the cut to $1.02; the campaign's
  strong recent conversion was an argument for lifting its placement
  modifiers toward the ceiling, not for moving the ceiling.
- **No bid, and no effective price at any placement, may exceed this
  ceiling on any objective except the one narrow case in §7.**
  **Off-Amazon is a placement, and it is separated out before any cost
  figure is compared to any ceiling.** The placement report carries it as
its own row alongside top of search, rest of search and product pages.
Every ceiling in this file is built from on-Amazon economics, so a cost
per order that still has off-Amazon spend inside it cannot be measured
against one — the comparison is arithmetically meaningless and it reads
as a verdict. On a real build a child was declared unprofitable at
$34.75 an order against $27.69 of contribution and a routing argument
was built on top of that; separating the placement put its on-Amazon
cost at $25.36, comfortably profitable, and the argument collapsed.
Across that product off-Amazon had taken $994.74 and returned eight
orders.

**Where off-Amazon serving is unset, it is closed on every campaign that
will be serving after the change lands — not on the largest leaks
alone.** It is one field per campaign with no bid, budget or targeting
consequence, so there is no reason to stage it, and a campaign left open
re-opens the leak the moment it delivers. Treat the set of campaigns to
fix as the post-change serving set, which includes every campaign the
same file switches on.
- **Room left in the product's weekly spend envelope is never itself a
  reason to exceed a child's ceiling.** The envelope and the ceiling
  answer different questions and are not interchangeable. The envelope is
  a product-level dollar total — target TACoS × projected weekly revenue —
  and it caps how much can be spent in the week. A ceiling is per child,
  derived from that child's own contribution and the delivering
  placement's own conversion rate, and it caps what a single click may
  cost. Unspent envelope buys **more** clicks at or under their ceilings;
  it never buys **dearer** ones. **Where the envelope has headroom and
  every eligible row is already at its ceiling, the correct outcome is an
  underspent week**, and the spare goes to coverage, to a discovery layer
  that qualifies on its own gate, or nowhere at all.
- **The same applies in reverse across children: a child that clears its
  own ceiling comfortably does not lend that headroom to one that does
  not.** A product can be net positive while an individual child is
  losing money on every click, and reading the parent figure as
  permission for that child is how a structurally unprofitable variation
  survives indefinitely inside a healthy-looking parent. Contribution is
  measured per child because the decisions it drives are per child.
  **The only route by which a row may knowingly run below its own
  break-even is a sized push carrying a computed, dated loss ceiling
  (§7), and that route is opened by the declared goal, never by the
  parent's aggregate position.** Where the arithmetic genuinely appears
  to call for a child to run at a loss to carry the parent, that is a
  finding about the declared goal and is raised as one — it is not
  settled inside a bid.
- **Three fast reads, sourced from the account's own framework and not
  previously stated with this precision, worth citing inline rather
  than re-derived each time:** **max profitable CPC = margin × CVR** —
  the same affordable-CPC figure above, restated as a one-line check
  anyone can run without the full placement-CVR lookup; **clicks-to-loss
  = margin ÷ CPC** — at a $4.00 CPC on $10 margin, 2.5 clicks per order
  is the break-even point, so a term converting at one order per 10
  clicks is losing money on every sale, not just underperforming; **CPA
  = CPC ÷ CVR** — the plain arithmetic connecting the two numbers a
  reasoning statement already cites, stated so the loss or gain per order
  is never left as an exercise for the reader.
- **CPA ceiling applies to Profitable Conversion, Defensive, Discovery and
  Conquest rows** — not to a Ranking row cleared by §6 and still inside
  its ranking window (§7). - **Zero conversions on a thin sample means unknown, not zero** — never
  price a row at zero off a handful of clicks; flag instead. - **A confirmed-but-not-yet-live COGS change carries two parallel CM2
  figures, not one — previously only mentioned in
  passing in this document's own skeleton rather than actually built as
  a rule.** Where a cost change is genuinely confirmed and dated (a
  packaging change with a set switch date, a negotiated supplier rate
  that takes effect on a known date) but hasn't landed yet, the product
  carries **current-COGS CM2** (what's true today, what every live
  decision runs on) alongside **optimised-COGS CM2** (what will be true
  once the confirmed change takes effect), stated side by side rather
  than one replacing the other early. **Every decision that spends real
  money now runs on current-COGS CM2 — the optimised figure is context
  and forward planning, never the basis for a live bid or budget
  decision before its effective date.** This is a different mechanic
  from §1C's 48-hour margin-refresh protocol: that rule is reactive,
  re-deriving the margin table *after* a change has already happened;
  this rule is proactive, carrying a known, dated, *not-yet-happened*
  change alongside the current truth so the transition doesn't arrive as
  a surprise recomputation on the effective date. On that date,
  optimised-COGS CM2 becomes current-COGS CM2, and the margin-refresh
  protocol's own 48-hour re-derivation requirement takes over from
  there.
- **Aged/LTSF SKUs run forward-cash economics**, not CM2 — the deal or
  clearance mechanism is the primary lever; COGS never enters a live
  decision column on aged stock. - **CM2 and margin are computed separately for deal-state and clean-state,
  never averaged together into one blended figure.** A SKU or campaign's
  ceiling during an active deal/promotion window uses that window's own
  deal-state CM2; outside it, clean-state CM2 governs. A blended figure
  produces a ceiling that's wrong in both states — too loose during the
  deal, too tight outside it. - **This deal-state/clean-state separation is a standing principle, not a
  rule specific to CM2 — it applies to every calculation in this skill
  that reads across a trailing window and could have a deal or event week
  sitting inside it.** Wherever a deal window falls inside such a window,
  compute the figure twice: once from deal-state data only, once from
  clean-state data only. Neither is discarded and neither is blended into
  the other — a deal week's data is real and gets its own use, not thrown
  away as noise. The clean-state figure governs ordinary, between- and
  outside-deal decisions; the deal-state figure is a separate reading,
  kept for judging deal performance specifically, and never substitutes
  for the clean-state figure when judging a row's ordinary standing. §7's
  rank-trend read and sufficiency stop, and §10's CVR baseline, apply
  this same separation — see each for the specific mechanics.
- **A per-unit fee that rises as volume falls is a fixed charge being divided, not a cost of selling — separate the two before any child is called unprofitable.** Storage, long-term storage and removal fees are periodic charges on inventory that sits; divided across a small unit count they produce per-unit figures that look like catastrophic unit economics and are nothing of the kind. The test is direct: compare fee-per-unit against units sold across the child set. Where high-volume children pay one figure and low-volume children pay several times it, the difference is allocation, not cost. On a real build this read as thirteen children losing money per unit — one at negative $59.53 — and on marginal economics, variable fees only, **every one of them was positive, between $5.32 and $24.04 a unit.** The verdict that followed from the unseparated figure was to block advertising on 1,051 units of aged stock holding $9,907 of recoverable forward cash, which is the opposite of what those children needed. **State the variable fee benchmark, state the fixed charge being allocated, and judge the child on the first.**
- **Deal-state economics carry their own cost lines, not just a different
  CM2 input.** Deal fees (fixed + a percentage of deal sales) reduce net
  contribution and are stated separately from ordinary referral/FBA fees,
  not folded silently into deal-state CM2 without being named. Where a
  deal is active, report sales/units/glance views for the window, deal-
  page conversion rate, contribution at deal CM2 net of deal fees, and net
  contribution before ad spend — glance views specifically, because a SKU
  can burn engagement on a deal placement with zero units moving, which a
  sales-only view would miss entirely.
- **Auction density is a required input to any cut's safety judgment, not
  an assumption.** Before sizing a bid cut as "safe," check whether the
  term is actually contested by paid competitors (advertised-keyword count
  among tracked competitors, not just organic presence). A cut on an
  uncontested term is a pure efficiency gain with no share-of-voice risk;
  the same cut on a term several competitors bid on is a different
  decision and should be sized and reasoned differently. State which case
  governs, per keyword or per syntax cluster, not assumed account-wide.
- **Price position among tracked competitors is a required standing input,
  not optional colour.** Where a conversion or CVR gap exists on a term,
  check the account's own price rank against the tracked competitor set
  before concluding it's a PPC-fixable problem — a gap driven by price or
  offer position (not relevance, not bid) routes to Brand Management
  recommendations, never a bid correction that can't close a price gap.
- **Deployment sequencing is gated on deal-contamination per lever, not
  set by a single blanket timeline.** Split every proposed lever into
  "deploys now" and "waits for the clean week" based on whether *that
  lever's own supporting evidence* is contaminated by an active deal
  window — never by applying one date to everything the plan contains. A
  structural fix built on forward-looking ceiling math is deal-safe and
  deploys immediately; a cut arm or a launch batch whose read depends on
  clean-week CVR waits until the window closes, because deploying it
  earlier would judge it against contaminated data.

---

**A funding claim is proved at the rate the spend actually occurs, and
the envelope is re-derived for the declared goal before it is used.**
Two failures here are separable and a real build made both at once.
The first is unit mismatch: a release measured across sixty days set
against a commitment measured per day reads as generous cover and is
not — $1,962 over sixty days is $32.70 a day against a $73.69 daily
push, and the plan claimed the push was fully funded when it was
short by $40.99 every day it ran. **Convert both sides to the same
rate before any "funded by" sentence is written, and state the net
new requirement even when it is zero.** The second is a stale
envelope: a spend envelope derived at a profit-first target cost of
sale, then carried unchanged into a plan whose declared goal is
Growth/Scale, will bar the very push the goal authorises — on that
build the envelope read $76 a week against a programme of $758.62.
**Re-derive the envelope from break-even and the growth band the
declared goal sets, and show the derivation.**

**Where a push runs above the envelope during ramp, that is stated as a
ramp exposure with its bridge priced, not smoothed away.** Spend lands
before the revenue it buys. Name the weekly bridge, carry it as a
numbered decision, and show the post-delivery cost of sale that brings
the programme back inside band. A push whose economics close only after
it works is legitimate; a plan that hides the gap until it closes is
not.

## 4. Per-placement bid and placement logic

**TOS, ROS and PDP are judged independently** on their own clicks, orders
and CPA against their own ceiling. A keyword's blended number never stands
in for what any one placement is actually doing.

**Every placement modifier change is solved backward from a held target
effective price** — base bid × modifier = target, computed in that
direction only, never the reverse.

**Rest of search is judged on its own performance, on every objective, and
its profitable ceiling is a maximum it may never pass.** It is excluded
from the above-ceiling ranking allowance outright — that allowance is top
of search only, because top of search is the placement that moves organic
rank and rest of search is not.

**The lift is earned, and the entry condition is fifteen clicks on that
placement, on that specific campaign, converting at or above the
campaign's own product-page rate.** Below it, rest of search runs at base
— unmodified, not suppressed — because nothing yet evidences a premium
above base, which is the same standard applied everywhere else in this
file.

**Above the entry condition the lift is sized to how well it is actually
performing, not jumped to ceiling.** The ceiling is the maximum, not the
destination: a placement clearing the bar by a little earns a little, one
converting far above the product-page rate earns most of the range, and a
row may sit anywhere between base and ceiling. **A file where every
rest-of-search modifier sits at ceiling has sized nothing** — the same
failure as a roster of identical top-of-search premiums, in a different
column.

**Both data sources are read, because neither answers the question
alone.** The keyword row says whether the term converts at all; the
placement row says where those conversions happened. A term converting
well overall can be carrying rest of search on top-of-search performance,
and reading only the keyword row will lift a placement that has earned
nothing.

**Where the data is bad or absent, rest of search stays at base.** Not
suppressed below it, not lifted on expectation. This gate is
self-resolving: the moment the placement clears fifteen clicks above the
product-page rate, the lift becomes available at the next deploy with no
separate approval.

**A re-route or re-point resets this gate along with everything else §11's
SKU-provenance check resets.** A re-pointed campaign's rest of search
starts back at base until it re-earns the lift on the newly-routed child's
own data, regardless of what it was doing on the previous child.

**Non-ranking top of search follows the same shape inside its own
ceiling.** On Profit, Defensive, Conquest and Market Share the affordable
ceiling binds, and the lift toward that ceiling is sized to measured
performance in exactly the way rest of search is — earned by the same
fifteen-click entry condition on that placement, sized by how far above
the product-page rate it converts, and held at base where the data is bad
or absent. The difference between these objectives and Ranking is *what
price is permitted*, not *how the lift is sized*.

**Phrase, Broad, product targeting and every discovery campaign judge both
placements on their own performance, never on a rank gap.** An auto
campaign has no rank target, so a modifier derived from one is a number
with nothing behind it — and on a real build 350 per cent rank-gap
modifiers were written onto four auto campaigns that had no rank to close.
Top of search and rest of search are each read from that row's own
measured conversion, against the same fifteen-click entry condition, sized
the same way, and held at base where the evidence is absent. **The
above-ceiling allowance does not reach discovery rows at any placement**:
it belongs to a Ranking row inside a ranking window, and a discovery row
is neither.

**This gate is rest-of-search only, and the asymmetry is deliberate
rather than an omission.** Top of search carries no equivalent
15-click precondition, and the reason is structural: it is the one
placement that moves organic rank and the only one a ranking premium
can sit on, so gating it behind evidence it cannot generate without
running is circular. Where a base bid changes, top of search is
re-solved to its own target under the backward-solve above, never
zeroed for want of clicks. **Reading this gate as governing both
placements is a real, made error** — on a live build it took eleven
reactivations to a zero top-of-search modifier, which would have
restored the terms without restoring the position they were being
restored for. The one case where top of search legitimately runs at
zero or near it is the named ROS-weighted state: a term profitable only
at rest of search *with no rank case behind it*, which is an evidenced
finding about that term, not a default applied for absence of data.

**PDP has no modifier; it moves only through base bid.** When base bid
changes for PDP's sake, TOS and ROS modifiers are re-solved afterward from
their own already-decided targets: compute TOS's and ROS's own cycle
targets first, from their own data; set the new base bid; then re-solve
TOS modifier = TOS target ÷ new base, ROS modifier = ROS target ÷ new
base. A PDP-driven change must never silently drag TOS or ROS off what
they'd have independently earned.

**Bidding strategy is set by stage, not by objective — and this corrects an
earlier rule that opened Ranking rows on Fixed for "consistency of
pressure." Objective does not determine strategy at all.**

**Fixed at launch.** A new product has no conversion history, so dynamic
down-only has nothing to judge with: Amazon reduces the bid where it
predicts conversion is less likely, and on a launch that prediction rests
on absent data. It will suppress the delivery the product needs to
establish any rate at all. Fixed gives consistent pressure while the row
builds the history that makes a dynamic strategy meaningful.

**Down-only once legacy.** With real conversion data behind it, down-only
stops being a guess and becomes an asset. It reduces the bid where
conversion is less likely, which disproportionately suppresses
product-page delivery — measured at 7.7 per cent conversion against 19.8
per cent at top of search on this account. **That is the same direction
the whole placement strategy pushes, so it is free help**, and opening a
ranking row on Fixed throws it away. The switch is a stage transition,
not a performance verdict: it happens when the product graduates from
launch, not because a row is doing well or badly.

**Fixed again, as a last-resort escalation on a legacy row.** Reached only
when a row still is not buying top-of-search clicks after the base has
been staged down and the modifier raised. **The trigger is a specific
diagnostic signature: effective top-of-search bid held or raised while
top-of-search impression share stays flat or falls.** That pattern says
down-only is cutting the bid on the very auctions being bought, which
becomes a real risk once the base sits near its floor. **The switch is a
trade and the reasoning states it as one** — accepting more product-page
delivery to protect top-of-search presence. A legacy row on Fixed carries
the sentence explaining it was escalated there, so it is not read as a
setting someone forgot to change.

**Dynamic up-and-down stays gated behind months of validated conversion
and explicit ceiling math on file, and never runs on a ranking row** — it
lets Amazon raise the bid on the placement the row is trying to leave.

**The effective-price formula is two-factor for Fixed and Dynamic
down-only — base bid × (1 + placement modifier) — unchanged and correct
for both.** Down-only can suppress the realized price below this number
in real time but never raise it above; Fixed has no dynamic component at
all. Neither strategy needs a third factor.

**Dynamic up-and-down is the only strategy where a third factor is real**,
because it's the only one that can raise the realized price above base ×
(1 + modifier): a dynamic raise, up to +100%, at top of search only.
Authorized effective CPC under up-and-down = base × (1 + modifier) × (1 +
dynamic raise). This factor only enters the math for a row actually on
this strategy — which, per the paragraph above, is already a narrow,
evidence-gated subset. **The dynamic raise is capped twice, not once:**
the +100% ceiling on the factor itself, and separately, the resulting
authorized price still has to clear whichever ceiling governs the row. If
it doesn't, the correction is reverting the strategy to down-only, or
re-solving the base bid downward until the authorized price lands back
inside ceiling — never allowing the breach to stand.

---

**The placement table is per campaign against per placement, and it
carries the modifier currently set on each.** Not a portfolio roll-up:
one row per campaign per placement it served, with clicks, that
placement's share of the campaign's own clicks, orders, conversion,
cost per click and cost of sale, and — the column most often missing —
the placement modifier that is actually set on that campaign right now.
A portfolio-level placement table cannot show a modifier at all, and the
modifier is the lever. On a real build, building this table at campaign
level immediately exposed that nine of twelve modifiers across enabled
campaigns sat at zero, including on every campaign whose top-of-search
placement was its best converter — a finding invisible in the roll-up
that replaced it, and not a bidding judgement that went wrong but a
lever never set.

**The bid re-solve appears as arithmetic, per campaign, showing the
move.** Affordable price at each placement, computed as contribution
times that campaign's own conversion at that placement; the base bid now
and the base bid proposed; the modifier now and the modifier target;
and the step, stated as a staged sequence wherever the full correction
exceeds the single-step cap (§5). "Reprice to ceiling" is an
instruction to a person who already knows the arithmetic; "base $0.45 →
$0.34, top-of-search modifier 50% → 488%, staged 50/150/300/488" is the
decision itself, and only the second can be checked or deployed.

**A Ranking row's top-of-search bid is not capped by the affordable-CPC ceiling, and this is stated here rather than left in §7 because this is the section where the modifier actually gets computed.** Inside the ranking window — after §6's goal gate clears, before the sufficiency stop fires — no CM2×CVR-derived ceiling caps that row's top-of-search price. Rank, target rank, search volume and placement mix govern instead, bounded only by the flat account-wide sanity cap. **The failure this prevents is concrete: a builder working inside this section, computing a modifier from affordable prices, will cap a ranking push at its efficiency ceiling and call it correct — which funds the term without funding the position it was funded for.** Top of search is the only placement structurally capable of carrying that premium: rest of search is excluded from the allowance outright, and product pages have no modifier at all.

**The premium is sized from that row's own rank gap, never a flat percentage applied across the roster.** A keyword five positions from its target and one a hundred positions away are different decisions, and pricing both at the same modifier treats them as the same. Held near current where the gap is small; a moderate step where it is real but closing; the full computed premium where the gap is wide and the rank case is evidenced. **A build that writes the same modifier onto every ranking row has not sized anything — it has applied a default and labelled it a decision.**

**Where a row is not a Ranking row, the ceiling binds at every placement including top of search.** The allowance is not a general licence to overbid; it is the one authorised exception, and it expires with the ranking window.

### The portfolio-level structural sweep, run before any row is decided

**Every rule in this file is written for the row in front of you, and a whole class of defect is
invisible from there.** On a real portfolio 244 of 705 campaigns sat at a zero top-of-search
modifier. That is not 244 individually wrong decisions a reviewer could catch one at a time — it is
one structural condition nobody looked for, and no per-row rule surfaces it, because each row in
isolation reads as a legitimate "no premium evidenced yet."

**So before decisions start, read the portfolio in aggregate and state what it looks like.** Four
figures, and each has changed what a cycle was about:

- **The distribution of top-of-search modifiers across every campaign** — how many at zero, how many
  at or under fifty per cent, how many above a hundred, and the median. A portfolio where most
  campaigns sit at or near zero is configured to send its clicks to product pages, and no bid
  decision on any individual row corrects that.
- **How many campaigns carry a ranking objective while structurally unable to isolate** — a zero or
  near-zero modifier, or a base so high the top-of-search-to-product-page ratio cannot open.
- **The spread of top-of-search-to-product-page ratios**, not the spread of modifiers. A 95 per cent
  modifier on a $3.00 base and a 95 per cent modifier on a $0.60 base are different structures, and
  only the ratio distinguishes them.
- **Where the portfolio's clicks and spend actually land by placement**, against where they should.
  Impressions are the wrong column: product pages take about seventy per cent of impressions and a
  third of clicks, so an impression-weighted read makes a leak look like the normal state.

**A structural finding outranks the row-level pass and changes what the cycle is for.** Where the
sweep shows most of a portfolio mis-set, the cycle's work is the structural correction — the per-row
optimisation that follows would otherwise be tuning bids inside campaigns that cannot deliver the
placement those bids are buying. **Say that plainly at the top of the deliverable rather than
burying it in the rows**, because a reviewer reading row by row will not reconstruct it.

### The base floor, the staged descent, and what to do when pricing runs out

**What moves click distribution is the ratio between the top-of-search price and the product-page
price — not the base, and not the modifier.** Base and modifier are two handles that produce one
ratio. On a real account a campaign went from 168 to 449 clicks with top-of-search clicks flat: the
base had become more competitive and the growth landed wherever the base competes, which is product
pages at 71 per cent of impressions. **A 20 per cent modifier increase could not correct it, because
raising the modifier lifts what top of search pays and leaves the other two placements exactly where
they were.** The mix moves when the gap between them moves, and that needs both handles.

**And the ratio itself is stated on the row as a number, because it is the figure that explains the
result and nobody can see it without computing it.** A campaign carrying a 95 per cent top-of-search
modifier reads as aggressive; the same campaign at a $3.00 base is paying $5.85 at top of search and
$3.00 at product pages, and **the ratio is 1.95 to one** — nowhere near enough separation to isolate.
That single figure is what a reviewer needs, and it is invisible unless written: base and modifier
each look reasonable on their own. **"Top of search $5.85 against $3.00 on product pages, 1.95 to
one" is checkable. "95 per cent modifier" is not**, and on a real portfolio the second reading is
what let a structurally unisolating campaign pass review.

**A ranking row at a zero top-of-search modifier is a defect, not a decision.** Zero is legitimate
where no rank case exists and nothing evidences a premium — that is the rule elsewhere in this file
and it stands. **But a campaign built to rank, running a zero modifier, is structurally incapable of
the thing it exists for**: at zero it takes roughly four per cent of its clicks at top of search
against seventy per cent once a modifier is set. It is not underperforming; it is not configured to
perform. Where a ranking row carries zero, the verdict says whether the row is genuinely not a
ranking candidate — in which case its objective is wrong — or whether the modifier was never set.

**The base starts at the product-page profitable ceiling — contribution × product-page conversion —
and that is a reference point, not a floor.** If product pages still take more than 20 per cent of
clicks at that price, keep cutting. **"At worst break-even" is not good enough**: a product-page order
costs $17.60 against $10.91 at top of search on this account, so a break-even product-page click
still consumes budget that would buy a cheaper order elsewhere. The opportunity cost is the argument,
not the direct cost.

**The hard floor is $0.35 to $0.50, judged within that range, and it is not computed per campaign.**
Below it, base-bid eligibility suppression becomes the risk: a base too low can stop the campaign
qualifying for auctions before the modifier is ever applied, so the row is not in the auction it
appears to be in. The signature is unmistakable — effective bid unchanged or higher, top-of-search
impression share flat or falling.

**The descent is staged and never a single drop.** A bid well above the ceiling corrected in one move
changes delivery, conversion and clearing price at once, and the next reading cannot say which moved.
Each step re-solves the modifier upward so the top-of-search price holds or ratchets slightly up
while the base comes down.

**Step size is judged from three signals, and the bound is attribution rather than a percentage.**

- **How far rank sits from target.** Two positions off is a nudge. Twenty times target needs real
  movement, because a small step there buys nothing and spends the cycle.
- **Whether clicks are arriving at all.** Where campaign and keyword are both enabled and clicks are
  absent — or under fifteen on a ranking row — **hold the base and push the top-of-search modifier
  only.** Cutting the base of a row that is not delivering makes delivery worse; there is no
  distribution to fix on a row with no distribution. **Then read the 60-day placement history for
  that campaign and keyword before concluding**: if product pages took more than 20 per cent of
  clicks across that window, that is a real distribution finding and both levers move despite the
  thin current window. **A silent window is silent, not clean.**
- **Where the clicks are landing.** Product pages at 40 per cent is a different move from product
  pages at 22 per cent.

**No single move should be large enough that the result cannot be attributed.** If base, modifier and
delivery all shift at once, the next observation teaches nothing and the cycle is spent. That is the
real bound on step size — not a cap, but the fact that a large move destroys the read.

**Staging stops at either condition: product-page clicks under 20 per cent, or the base at its
floor.** Whichever comes first.

**When the floor is reached and product pages still take more than 20 per cent, the pricing lever is
exhausted and two moves remain, in this order.**

1. **Switch to Fixed and push top of search toward the cap in stages.** Stated as a trade in the
   reasoning: accepting more product-page delivery in exchange for stopping down-only cutting the bid
   on the top-of-search auctions the row needs at a thin base.
2. **Test the term in Phrase to buy the rank.** If Exact cannot hold the mix at the floor with the
   modifier raised, the structure is the constraint rather than the settings — a Phrase instance is a
   different auction with a different clearing price and a different placement profile. **This is a
   dated test running alongside the Exact row and graded against it, never a migration.**

**Negative product targeting is not on this ladder for Exact campaigns, and the reason is data rather
than doctrine.** It is the only lever that removes product-page delivery instead of repricing it, but
it needs the ASINs of the detail pages served on — and no report gives those for a keyword campaign.
The search-term report returns search terms; the advertised-product report returns our own ASIN.
**On Auto and product-targeting campaigns the target is an ASIN and is named in the report, so the
lever works there and belongs in that ladder instead.**

**The target is a share of clicks, never a share of impressions.** Product pages take 71 per cent of
impressions and produce 33 per cent of clicks and 27 per cent of spend on this account. Impressions
on a detail page are mostly free because nobody clicks them; optimising that column moves a number
that barely affects the outcome. **Manage 70–90 per cent of clicks at top of search with product
pages at or under 20 per cent** — and note that 20 per cent sits at the observed floor across every
modifier band measured, so under 20 is good rather than expected.

**Top-of-search impression share is a different metric with a different job, and conflating the two
is a real error.** Placement share of impressions is an output and does not matter. Top-of-search
impression share says whether the bid clears the auction at all — a row can hold 90 per cent of its
clicks at top of search while appearing in 1 per cent of the available auctions. **Mix is a spend
question; share is a volume question, and a ranking push needs both.** On a real product every
delivering target sat under 1 per cent share, which is a different diagnosis entirely from a mix
problem. Read it on ranking rows; do not read it as a mix metric anywhere.

**Between cycles this runs as a manual loop on the top 20 per cent of campaigns by clicks, until the
next full analysis.** Where product-page clicks exceed 20–30 per cent, cut the base by an amount the
leak justifies and lift the modifier so the top-of-search price ratchets slightly up. **A larger step
is defensible precisely because the observation is daily** — a bigger move with a fast read is safer
than a small one with none. The loop is a controller a person runs; the file carries the structure.

**Every branch of this states itself in the Action and Reasoning.** Which case applied and why: *no
delivery this window, base held, modifier lifted to buy clicks* — or *no delivery this window, but 60
days shows product pages at 34 per cent of clicks, so both levers move.* A reviewer finding a base
cut on a zero-click row should find the sentence explaining it, and one finding a base held should
find the sentence naming delivery as the binding problem.

### The four bounds on any bid, checked in order, every time

**Every bid this file produces passes four bounds, and they are gathered here because scattering them is what made them missable.** Each of the four already existed in this skill; each was written as a subordinate clause inside a passage about something else, and each was read past on a real build. The result was a $9.00 top-of-search click on a product whose unit earns $24.67 — a 321 per cent cost of sale against a 47 per cent break-even, losing $145 on every order it bought. No single rule was absent. The bounds were simply never assembled into something a builder could run.

**Routing is read from the account's own product-ad rows, never inferred from a campaign's name.** A campaign name records what it was built for; the product-ad rows record what it actually advertises today, and on a real account these diverge constantly — a campaign named for one child running ads on a different one, an auto campaign named for a single SKU running fifteen. Reading the name produced a routing verdict that disagreed with the account's own bulk on 212 of 251 campaigns. **The bulk export carries entity types the decided file does not: product ads, ad groups, campaign negative keywords, negative product targeting. Read all of them for context even where the decided file has no row for them**, because the routing question, the negation question and the eligibility question are each answered on an entity the decided file never shows.

**Adding rows to a decided file is a structure change and is not how a new decision gets recorded.** Where a decision has no row of its own — a negation, a re-route, a product-ad switch — it is written as the Action and Reasoning on the campaign or keyword row that carries it. The file's shape is the account's, not this skill's, and a reviewer opening it should find the same rows they exported plus decisions, never rows that appeared from somewhere.

**A column's units are read from the file, never assumed from its name.** A column called TOS% held
percentages on one pass (52, 257, 350) and multipliers on the next (1.5, 2.0) — the same header, a
different meaning, and every downstream calculation silently wrong if the change goes unnoticed. The
header did not change; the model did. **Before reading any numeric column, look at its actual values
and at any formula that consumes it**, because a formula referencing the column states its units
unambiguously where the header cannot: `= base * (1 + TOS)` says multiplier, `= base * (1 + TOS/100)`
says percentage.

**A formula in a cell is a live model and is preserved, not replaced with the number it currently
evaluates to.** Static values are a snapshot; a formula recomputes when its inputs move, which is the
difference between a workbook that stays right and one that was right once. Where a check or an edit
reads a cell and finds a formula, that is a valid value — the failure is a check that rejects it, and
on a real cycle one did, reporting 28 correctly-modelled rows as defects.

**Bound 1 — the base is derived, never inherited.** A bid already sitting on a row is not a starting point; it is a number of unknown provenance that some earlier cycle wrote for reasons nobody recorded. **Before any calculation reads a base bid, that base is recomputed from the routed child's own economics** — contribution for a fresh SKU, forward cash for aged stock — at the tighter of rest-of-search and product-pages affordable. On a real build 485 rows carried inherited bids up to $6.40 against affordable prices near $0.62, and every modifier computed on top of them inherited the error and multiplied it. **A modifier applied to an unvalidated base is not a placement decision; it is an unexamined bid wearing a percentage.**

**The objective sets the price bound, not the modifier cap — and this replaces an earlier rule that
capped every premium at 25 per cent over what top of search affords.** That cap contradicted this
file's own above-ceiling allowance and, on real economics, capped a ranking row at $1.54 against a
$2.16 clearing price: the row was funded and the position was not. **A Ranking Exact row may take its
top-of-search price above the affordable ceiling to buy rank. Every other objective stays inside the
ceiling, whatever modifier gets it there.** The modifier is a mechanism; the objective is what
decides whether the resulting price is allowed.

**The modifier cap is 900 per cent on every objective, because the cap was never the right
distinguisher.** A large modifier on a small base and a small modifier on a large base buy the same
click, so capping the modifier by objective bounds the wrong quantity. What differs by objective is
the price the modifier is solved toward, not the range available to solve within.

**Every premium is still sized from that row's own rank gap, and a file where every row sits at the
same number has sized nothing.** A term marginally off target takes a small lift; one far from target
takes a large one; a term with no rank against a stated target takes none at all.

**And the modifier saturates long before the cap, which is measured rather than assumed.** Across 113
live campaigns with real delivery, moving from 0 to 50 per cent takes the median campaign from 3.8
per cent of its clicks at top of search to 72.7 per cent. Moving from the 50–99 band to 100–199 moves
it three points. **Past roughly 100 per cent the modifier buys top-of-search auction share rather
than a further shift away from product pages** — worth having on a ranking push, where volume is the
point, but it should be called what it is. **Above 200 per cent has never run live on this account:
that range is mechanism and inference, not measurement**, and it is staged into with observation
between steps, never jumped to.

**Bound 2 — the modifier never exceeds 900 per cent, the platform maximum.** This bounds the mechanism, not the price: what the resulting top-of-search price is allowed to be comes from the objective, under Bound 3. A modifier at the wall is the rare case its own rank gap justifies, and the reasoning says why that specific price.

**Bound 3 — no click may cost more than the unit earns.** This is the per-SKU sanity bound derived from CM2, and it is absolute: at a hundred per cent conversion a click priced at CM2 exactly breaks even, so any price above it loses money at every conversion rate that exists. It tightens the flat account-wide ceiling and never loosens past it. **State it as a number on the row, not as a principle** — "top of search at $4.50 against $24.67 a unit" is checkable; "within the ceiling" is not.

**Bound 4 — the flat account-wide ceiling.** The last and loosest of the four. A price passing bounds 1 through 3 and failing this one is rare; a price passing this one alone means nothing, because the account ceiling is set for the account's most profitable product and says nothing about this one.

**Whichever bound binds first is named in the reasoning, with its arithmetic.** A row reading "modifier 350 per cent" tells a reviewer the cap was hit; a row reading "modifier solved backward from the $11.29 a unit of Full Cgrey divided by the $0.77 base" tells them which of the four bounds actually decided the number, which is the only version they can check.

**Every push states its loss ceiling in dollars per order, computed at the spend the push actually requires.** Cost per order at the proposed price, cost of sale against that child's own break-even, and the loss carried per order while the rank is being bought. **A ranking premium without this number stated is a premium nobody has priced** — the five-property gate's Ceilinged property is not satisfied by the ceiling existing somewhere in the method, only by the figure appearing on the row.

**Levers that feed each other are computed in dependency order, and re-solved when an upstream lever moves.** A staged base changes the effective top-of-search price, so a modifier solved before staging is solved against a number that no longer exists. **Order: validate the base, stage it if the move exceeds the correction cap, then solve the modifier against the staged value, then re-check every bound.** This ordering was violated twice on one build and both times the breach appeared only after staging — a check run before the last lever moves proves nothing about the file that ships.

## 4A. Lever hierarchy — which lever clears first, and which move together

**Budget clears first, on every objective — not because levers must move
in strict sequence, but because a truncated campaign's performance data
is contaminated evidence.** Inside a budget-truncated day, "bid too low"
and "campaign stopped serving" are indistinguishable, so no bid or
placement conclusion *drawn from that period's data* is valid until
budget is fixed. This is a precondition on trustworthy evidence, not a
timing rule that blocks other levers from moving in the same pass.
**The specific threshold, sourced from the account's own framework
rather than left as a qualitative judgment: in-budget delivery under 70%
of the day marks every rate on that campaign as truncated.** A campaign
delivering 70% or more of its own day isn't truncated in the sense this
rule means, even if it didn't spend its full budget — the 70% line is
what separates "the budget cap bound this campaign's delivery" from
"this campaign simply didn't need more."

**Once budget is clear (or is itself the lever being fixed this cycle),
bid and placement move together as one coordinated computation, not as
two sequential steps.** This is §4's backward-solve mechanism: the target
effective price at each placement is set from that placement's own data,
then the base bid and modifiers are solved as a set. A campaign needing a
budget increase, a new bid, and a re-solved modifier can take all three
in the same upload, in the same pass — as long as the new bid and
modifier are derived from forward-looking ceiling and target math, never
from the truncated period's own contaminated CVR cited as if it were
trustworthy evidence. Multiple levers on one campaign, moved together in
one coordinated pass, is the standard case, not an exception requiring
special justification.

**A campaign producing only one kind of lever change — every verdict on
it reading as a budget move, or every one a bid move, with nothing else
touched — is a signal to re-examine the campaign, not evidence the pass
was done correctly. Contexts governed: live-row optimisation,
reactivation of a paused row or campaign, a re-route, and the campaign
and bidding-adjustment entity rows that sit alongside every decided
keyword — all four, in the same pass.** This has been a real, repeated failure on this
account: outputs where budget, top-of-search modifier, and bid were each
capable of independently justified changes, but only one of the three was
ever actually written. Before calling a campaign's verdicts complete,
check whether its budget, its bids, and its placement modifiers were each
genuinely evaluated against their own data, not whether at least one of
them moved.

**This is distinct from, and does not conflict with, the one-lever-per-
row rule in §13/§14's writing standard** — that rule blocks stacking two
undiagnosed changes onto the same single keyword row without a clear
attribution line. It says nothing about a campaign's several different
rows (its budget line, its several keywords, their several placements)
each carrying their own lever change in the same pass. A campaign's
budget, one keyword's bid, and a different keyword's placement modifier
can all move in the same cycle; a single keyword's bid and its match type
cannot both change in the same pass without stacking two undiagnosed
levers on one row.

**No bid change at all — hold and name the real blocker instead — when
the diagnosis is:**

- **Both quality gates failing** (listing and offer) — a bid can't fix a
  product problem; this is Brand Management's lever, not PPC's.
- **CTR passing, CVR failing** — the ad earns the click; the offer isn't
  converting it. Same as above, not a bid problem.
- **Zero delivery** — eligibility, a bid floor, or a budget cap is
  blocking the row; find which one before touching the bid.
- **Budget truncation** — see above; the block is on trusting the period's
  data, not on moving other levers in the same pass once budget is fixed.
  **But time-in-budget reading 0% alongside $0 spend is not truncation —
  it's missing data.** The campaign never delivered enough to register a
  budget constraint at all, and raising budget in response to that
  reading fixes nothing, because nothing was actually constrained. Real
  truncation shows measurable spend cut short mid-day with clicks and
  impressions present; zero-and-zero is silence, not a signal, and needs
  a different diagnosis (eligibility, bid floor, or genuine zero demand)
  before budget is touched.
- **A plan exceeding what the campaign can structurally deliver** —
  escalate; this is a budget-or-objective decision above the row level.

**This list is exhaustive for a silent hold — one this skill applies on
its own, without asking anyone.** Every reason on it is a mechanical,
objective fact: a gate either fired or it didn't, the data either exists
or it doesn't. None of them require judgment about what *should* happen
next; they only require checking whether a specific, named condition is
true.

**Any other situation that would otherwise end in a hold is not silently
marked HOLD — it stops and asks first.** A row or campaign showing real,
evidenced unprofitability that doesn't cleanly match a reason on the list
above; a State E investigation (§7) that comes back "no cause
identified"; a syntax diagnosed Both Failing (§1B) with no listing fix in
motion and no clean reallocation target; a product carrying broad
unprofitability with no ranking allowance in force and no data-floor
reason to wait — none of these are mechanical facts. They're judgment
calls about what to actually do, and a hold produced by silently
defaulting through one of them is not the same thing as a hold produced
by a named gate above, even though both would read as "HOLD" on the
page. **The difference is asked about directly, before the row is
finalized either way** — the same ask-first principle already governing
the data conditions register (below) applies here with equal force: a
hold is a decision, not the absence of one, and it doesn't get to be the
path of least resistance just because it requires nothing further to
happen. Log the specific question asked and the answer received,
whichever way it resolves.

**A Conversion-diagnosis freeze (§1B) or a listing-dependent hold above
can be pre-positioned around a confirmed, dated fix — the same mechanic already governing a confirmed-but-not-yet-live
COGS change (§3), applied here to a listing/offer fix instead of a cost
change.** Structure and coverage work -- turning a paused syntax branch
back on, cleaning a negative-wall, getting campaigns ready to serve --
proceeds now; none of it is bid pressure into the currently-unconverting
page, so none of it needs to wait. **The ranking allowance itself opens
exactly on the confirmed effective date, never before it.** On a real
product, this fired against a confirmed listing update (title, images,
CRO) landing alongside a confirmed inventory restock date pulled
directly from the DOH export -- the restock date governed over a
looser verbal estimate ("next week") given in the same conversation,
because a dated export is firmer evidence than an approximate window,
and the two disagreed by nearly two weeks. **This does not extend to
any other hold reason on this list.** A budget-truncated campaign's
data does not become trustworthy because a listing fix is scheduled,
and a quality gate unrelated to the dated fix does not clear because of
it -- this pre-positioning is scoped to the specific diagnosis the
dated fix actually resolves, nothing broader.

---

## 5. Data floor and correction sizing

**The click floor applies at every level a rate is computed at, and
naming them matters because it has been applied at one and not the
others. Contexts governed: the campaign as a whole, each placement
within that campaign, and each individual keyword row.** A campaign
clearing the floor in total does not license a rate on a placement that
holds four clicks, and a placement clearing it does not license a rate
on a keyword that holds one. On a real build the floor was checked at
campaign level only and a single click with a single order read as 100
per cent conversion, producing a $24.67 bid on a product whose whole
contribution is $24.67 — the arithmetic was correct and the number was
nonsense.

**Which window a decision is taken on is stated, and it is not the same window used for context.** Actions are decided on the two most recent complete comparison windows — this week against last — because that is what a change can be attributed to and what the next cycle will read the result against. The long window exists to say what is normal, what a trend looks like, and whether a recent movement is a departure or a return. **Neither substitutes for the other, and a plan that never says which window a verdict rests on has left its reader unable to tell a decision from a description.**

**Where the action windows cannot carry the sample a decision needs, the decision moves to the long window and that move is stated on the decision itself.** This is the common case on a thin product and it is not a failure — a rate computed on two clicks is arithmetic, not evidence, and a ceiling built from it will be wrong in a direction nobody can predict. The honest construction names both: the conversion rate that sets a ceiling comes from the long window because the action weeks hold too few clicks per placement; the direction, the change and the thing being acted on come from the action windows. **What is never acceptable is taking the long-window figure silently and presenting it as though it described the week being acted on.**

**Every window stated carries its dates, and windows that overlap are reconciled rather than blended.** Two windows that share days are not independent readings, and a figure computed across a price change, a deal, or a stock-out inside its own window is a blend of two different products. Where that happens the window is disqualified for trend verdicts and said to be, rather than quietly averaged.

- **Nothing under 15 clicks and 1 order gets a performance verdict.**
  Formula-only correction applies below that floor.
- **A keyword under 15 clicks sitting 20–25% above the CPC ceiling is
  corrected to ceiling in one cycle** — pure formula correction, no
  performance judgement. This is the case where the gap is already
  smaller than the step cap below, so it clears in one move.
- **This fires independently of the fixed-bid trial (§8) — the two answer
  different questions** (is the price right, vs. is the bidding mechanism
  suppressing volume) and a row can need one, the other, both, or
  neither. **When both apply to the same row, this price correction lands
  first, in the same cycle as or before the switch to fixed bid** — never
  after. Testing suppression at a price that's still off ceiling produces
  an ambiguous result: a lack of clicks could mean suppression wasn't the
  issue, or could mean the price is still wrong. Correcting price first
  removes that ambiguity from the test.
- **A row corrected to ceiling under this rule is checked against §8's
  suppression signature at the next cycle by default — this is not
  conditional on anything else firing, it is the standing next step for
  every formula-only correction.** Correcting the price answers "is this
  bid affordable"; it says nothing about whether that price can win
  enough auctions to ever be tested. A row can be arithmetically correct
  and still sit at zero clicks indefinitely, technically compliant with
  every rule above and never actually read. The correction is not the end
  of this row's story — it's the setup for the one check that comes next.
- **25% and 50% are caps on a single step, not mandated step sizes.** The
  actual step taken sits inside whichever cap applies, chosen by what's
  genuinely at risk on the row: how much order volume currently depends on
  it, how much data supports the diagnosis, how confident the read is. A
  row with real sales riding on it takes a gentler step even where the cap
  would allow more — this is already the CVR-moderated rule below, stated
  here as the general principle it was quietly following. A row that's
  clearly broken with nothing left to protect (zero orders, extreme
  overshoot) can reasonably take the full cap, because there's no velocity
  a bigger step would put at risk. Neither cap is a target to hit by
  default.
- **A $0.50 absolute bid floor — provisional, pending confirmation, not
  previously marked as such.** Almost every other number in this section
  carries a source tag; this one didn't, and it should have — a $0.50
  floor is a meaningful constraint on a long-tail Defensive or Discovery
  row, and stating it as settled without a source overstates how
  confirmed it actually is. Per this skill's confidence-tier rule, ask
  before this floor first drives a real decision on a product — once
  confirmed, it holds for that product without asking again.
- **This floor never overrides the affordable-CPC ceiling for a
  non-Ranking row — a real tension worth naming, not papered over.** A
  Discovery candidate on Auto or Broad, particularly a low-relevancy or
  thin-margin one, can have an affordable ceiling genuinely below $0.50 —
  margin times conversion rate simply doesn't clear fifty cents for some
  legitimate candidates. Applying the floor "regardless of what the
  percentage math produces, on any row, at any cap," as an earlier
  version of this rule stated it, would force a bid *above* what that
  row can actually afford, which breaks the one rule in this whole
  skill with no stated exception for it: no bid exceeds CM2×CVR outside
  the single named Ranking allowance (§3). **Where the affordable
  ceiling for a specific row sits below $0.50, the ceiling wins — the
  floor applies only where it doesn't conflict with what the row can
  actually afford.**
- **Standard cap is 25% of current price per cycle, or the remaining gap
  if smaller.** Extreme overshoot (CPA more than 8× ceiling) can take the
  full 50% cap in one step, since there's typically nothing left on that
  row worth protecting — then reverts to choosing within the standard cap
  from its new base.
- **A gap wider than the cap chosen for that row does not ladder toward
  the target one undated step at a time.** It stages as two explicit,
  dated steps, with both target values written down upfront — never "step
  one now, continue next cycle" left open-ended. This still respects the
  one-step-per-week cadence; both steps are simply pre-committed rather
  than decided one at a time as the gap narrows.
  **Every placement modifier on a staged row is staged with it, in the
  same commitment.** A modifier solved once against the first step and
  left there does not hold its target as the base falls beneath it — it
  drags the placement down by exactly the proportion the base moved,
  which is the silent drag the per-placement rules forbid, arriving a
  cycle later than anyone is looking for it. On a real build a
  top-of-search modifier solved at the first step alone would have let
  that placement fall from $2.46 to $1.68 against an unchanged $2.47
  ceiling, across steps the file had already committed to. Compute the
  modifier for every committed step when the steps are written, and
  write all of them: the target price is what is held constant across
  the schedule, not the percentage.
- **Graded push sizing (orders, CVR and ACoS together, never flat) applies
  to non-ranking rows, and to ranking rows once they've cleared the §7
  sufficiency stop.** It does not apply to an active ranking push still
  inside its ranking window — that magnitude is set by §7's rank-gap
  scaling instead. Shape, *provisional*: CONFIRMED (15+ clicks, 2+ orders,
  CPA ≤~70% of ceiling) holds; STRONG (30+ clicks, 3+ orders, ≤~60%) earns
  up to +10%; PROVEN (50+ clicks, 5+ orders, ≤~50%) earns up to +15%. Per
  this skill's confidence-tier rule (Step 0), the first time a row on a
  product actually qualifies for one of these tiers, ask whether these
  thresholds govern as written or need adjusting for this product — once
  confirmed, they hold for every later cycle without asking again.

---

## 5A. Suggesting the goal — from the product's own
data, always confirmed before use

**Where the product's strategic goal isn't already declared, this
skill suggests one rather than stopping to ask for it cold.** The
suggestion is built from data already gathered elsewhere in this
skill, not a fresh analysis run just for this purpose.

**1. Check for a confirmed LTSF charge first — the one hard, objective
trigger.** A real, on-record LTSF charge suggests Clearance/LTSF, and
nothing else needs weighing once one is confirmed.

**Inventory aging *without* a confirmed charge is not the same
signal, and is never treated as one.** Aging inventory gets raised as
its own flag regardless of what goal ends up suggested below — it's
useful, real information — but it does not, by itself, suggest
Clearance/LTSF. A product can carry aging stock and still genuinely be
best served by Growth/Scale, Profit-First, or Mixed; the aging fact
and the goal suggestion are reported side by side, never conflated
into one trigger.

**2. Absent a confirmed charge, weigh stage, TACoS position, and
margin trend together** — the same three dimensions §1C already reads
every cycle, not a separate calculation:

- **Leans Growth/Scale** when the product is in Launch or Ranking-push
  stage, margin is healthy or improving, and TACoS has real room
  before its ceiling.
- **Leans Profit-First** when margin is thin or declining, TACoS is
  already at or near its ceiling, or the product has settled into
  Mature/Harvest stage.
- **Leans Mixed** only when the data genuinely splits by segment — some
  syntaxes show real, well-supported ranking opportunity while the
  product's broader economics call for a conservative posture
  elsewhere. Mixed is not a default reached by the other two being
  merely ambiguous; it requires the split to actually show up in the
  data.

**3. Present the suggestion with the actual numbers behind it, every
time — never the label alone.** "Suggesting Profit-First — TACoS is at
94% of its ceiling and margin trend is declining month-over-month" is
the standard; a bare goal name with no evidence attached doesn't meet
it.

**4. The suggestion is never treated as decided until the person
confirms or overrides it.** Nothing downstream — §6's gate, §2A's
tier eligibility, any bid or placement decision — runs on a suggested
goal as if it were already the declared one. It becomes the declared
goal, and everything that depends on it is unlocked, only once the
person has actually said so.

---

## 6. Product-goal gate — checked before any ranking exception is available

**Provisional tier — the nullification mechanism below is asked about before it first drives a real decision on a product.** It is untested against a live product. The first time this gate would nullify or authorise a real ranking allowance, ask; once confirmed for that product it holds thereafter. **This is a check on the gate mechanism itself, not on the product's declared goal** — the goal is a required input gathered at intake, and the question here is whether nullification should work this way for this product, not what the goal is.

A campaign tagged Ranking by targeting type (§2) is not automatically
entitled to the above-ceiling allowance in §7. Before that allowance is
ever checked, confirm the product's own declared strategic goal:

- **Growth/Scale** → the §7 allowance is available, subject to
  everything else §7 requires. **This does not mean every campaign on
  the product becomes a ranking push — the same discipline applies here
  as everywhere else in this gate, just less obviously since the
  product's own posture is aggressive.** Only Exact-tagged campaigns
  carry the ranking allowance, and even they still have to individually
  clear the five-property gate (§7) — a Growth/Scale declaration
  authorizes the allowance to be *available*, it doesn't hand it to
  every Exact keyword automatically. Discovery campaigns on the same
  product still run their own candidacy gate and harvest test (§12)
  exactly as they would under any other goal — a Growth/Scale posture
  doesn't lower the 100-click bar or the 3-order harvest threshold.
  Conquest and Profitable Conversion campaigns on product/category
  targeting still run their own CPA, archetype, and watch-CPA rules
  (§2B, §10) unchanged — an aggressive product-level posture funds more
  ranking pushes where they individually qualify, it doesn't convert
  every other campaign type on the product into a ranking campaign by
  association.
- **Ranking and Profitability declared together** — a named, distinct
  case, not a blend of the two pure ones — **each campaign still gets its
  own objective tag from the ordinary targeting-type rule (§2)**: Exact
  keywords tag Ranking and carry §7's allowance where they clear it;
  product/category targeting tags Profitable Conversion and runs under
  the standard ceiling. The product-level "Mixed" declaration is what
  *authorizes* both to exist funded from the same product envelope, not
  a rule that blends their economics together — §1C's TACoS decomposition
  keeps Ranking spend and Profit spend as separate lines precisely so
  this coexistence stays legible rather than one silently subsidizing
  the other unnoticed.
- **Profit-First** → new ranking pushes are nullified — the §7 allowance
  does not open for a fresh push. **But a campaign that has already
  achieved and is holding real rank can still be defensively protected**
  (the seven-state test's hold-arm logic, placement discipline, State
  E's investigation on a genuine collapse) without that protection
  requiring the above-ceiling spending allowance itself. Protecting an
  asset already won is not the same action as funding a new push toward
  one not yet won, and Profit-First blocks the second without requiring
  abandoning the first.
- **Clearance/LTSF is stricter than Profit-First, not the same rule
  applied to a different label — this distinction is** Every rank consideration is nullified outright, including the
  hold-and-protect carve-out Profit-First gets: no new pushes, and no
  defensive protection of an already-won rank either. A Clearance
  product has no future position worth defending — the objective is net
  recovery per unit on stock leaving the catalog, and preserving rank
  for a product that isn't being restocked doesn't serve that objective
  regardless of how cheaply that protection could be bought. Every row,
  including ones correctly tagged Ranking by targeting type, runs under
  the standard ceiling in §3–§5, full stop, with no exception the way
  Profit-First keeps one.

**Aged stock carries a declared archetype and tier per SKU, sourced from
the account's own long-term-storage standard, and the archetype selects
which levers are legal.** Clearance is not one posture applied uniformly
to everything old. Four archetypes, and a build that treats them alike
will run the wrong lever on three of them:

- **A — fix-demand.** The stock is not moving because something about
  the offer is broken. Traffic is rebuilt alongside the repair, and the
  play is never depth-led: discounting harder into an unfixed listing
  buys volume at a worse recovery per unit than fixing it first.
- **B — variation-overstock.** One child is long while the rest of the
  parent is fine. **Child-scoped moves only — no parent-level and no
  family-level action**, because the problem is one variation's depth
  and a parent move spends against children that do not have the
  problem. This is the one archetype that states the parent/child
  boundary outright, and it holds even where a parent move looks
  cheaper.
- **C — dead.** No experiments at all. A seven-day test window on dead
  stock is not a test, it is seven more days of pure carrying charge
  with the decision deferred; the test window and the decide window are
  the same seven days. Decide inside them.
- **D — aged-healthy.** Speed is the objective. Scale the syntaxes
  already proven, and **the ceiling here is computed as contribution
  above floor price rather than CM2 × CVR** — a different basis from every other goal in
  this file, and using the standard formula on a D SKU prices it wrong
  in both directions.

**Tier — GREEN, YELLOW, RED or CRITICAL — sets posture the same day it is
declared**, and is not re-derived here; it is read from the standard that
declares it. **The objective on tag day is net recovery per unit measured
against the declared alternative**, not ACoS, not TACoS, and not rank.
Where an archetype or tier has not been declared for a SKU, that is a
named blocker with an owner, not a reason to fall back on the
profit-goal rules.

**One arithmetic trap worth stating because the source standard's own
worked example contains it: the storage surcharge is billed per cubic
foot × unit volume, not per unit.** A per-unit rate quoted from that
example will be wrong by whatever the unit's volume is. Reconcile every
charge to the invoice before any figure derived from it is computed, and
never quote the worked example's rate as if it were the rate.

**None of this reopens the above-ceiling allowance.** "Every row runs under the standard ceiling" above governs whether a row may be priced *over* what it can afford, and the answer stays no on every archetype. Archetype D changes how that ceiling is *computed* on aged stock — contribution above floor price, consistent with aged SKUs running forward-cash economics rather than CM2 (§3) — it does not permit pricing above whatever the resulting figure is.
- **Anything else undeclared or unrecognized** → treated as Profit-First
  by default for the purposes of this gate specifically (nullified, with
  the hold-and-protect carve-out available) — never as Clearance's
  stricter rule, and never as Growth/Scale's full allowance, until the
  actual goal is confirmed.

This gate runs once per product, before §7 is read for any individual
keyword.

**The declared goal sets what's authorized; it is never one objective
applied to every campaign on the product.** This is a named, real
mistake, not a hypothetical one — declaring the product Profit-First (or
any other single goal) and then re-tagging or cutting every campaign
toward that objective regardless of what an individual campaign's own
rank history shows repeats the exact error this gate exists to prevent,
one level up. A product declared Profit-First can still carry campaigns
worth protecting if they've achieved real, held rank; the gate above
controls whether the ranking *allowance* is available at all, not whether
every campaign must be judged as if its own rank history were irrelevant.
State the product's goal once, then judge every campaign on its own
scenario against what that goal permits — never flatten the two steps
into a single blanket verdict for the whole product.

**This gate has a counterpart one level down.** A product clearing this
gate at the product level can still have the same allowance nullified at
the syntax level by §1B — a chronic Conversion diagnosis freezes the
ranking allowance for its own member keywords regardless of what the
product-wide goal permits. Check both: a product-level clearance doesn't
override a syntax-level freeze, and a syntax-level clearance doesn't
override a product-level nullification. Both have to hold for a keyword
to actually carry the allowance.

**A third check sits above both: §1C's product posture.** A product in
code-red has every scale action frozen regardless of what this gate or
§1B's syntax diagnosis would otherwise permit — code-red is a gate, not
a diagnosis, and per §1C's own precedence rule, gates outrank diagnosis
outranks signals. Confirm the product isn't in code-red before checking
either of the two below it.

---

**A declared goal is executed, not re-litigated — and sequencing inside
it is never written as a hold.** Where the account has declared
Growth/Scale, every section of the plan is written as that push being
executed. Ordering work inside a push is normal and necessary: bids
come to ceiling before they are raised, a negative wall lands before a
reactivation, a placement mix is corrected before rank spend is added
to it. **None of that is a hold, and writing it as one — "hold on
scale", "before any scale", "wait on", "held, not funded" — inverts the
declared goal into its opposite and hands the workbook build an
instruction the account never gave.** The workbook is built from the
plan's own verdicts; a row reading "hold" produces a paused or
unchanged row in the bulk, which is the opposite of what a growth
declaration authorizes.

**Every held, paused or blocked verdict is swept against the declared
goal before delivery, and the sweep is stated.** The goal rule above
bans sequencing written as a hold; it does not by itself catch a hold
that was written for a good reason under a different goal and never
revisited. List every verdict in the plan that stops or withholds
spend — paused campaigns, unfunded layers, blocked children, declined
terms — and against each, the reason and whether that reason survives
the declared goal. Stock, own-catalogue targeting, evidenced negative
return and sibling-owned demand survive any goal. **"No delivery
history yet" does not survive a growth declaration** — on a real build a
139-row broad layer sat held pending harvest history it could not
generate without running, which is the same circularity §4 already
rejects for top of search.

## 7. Ranking — the seven-state progress test, and the one authorized exception

*(The rejection of a formula ceiling and the seven states are settled,
corrected once already against a real account mistake. The sufficiency
stop's specific thresholds and its entry/exit mechanics are provisional,
pending confirmation from whoever owns the account's standards.)*

**No CM2×CVR-derived ceiling caps a Ranking row's bid, at any placement,
while that row is inside its ranking window (post the §6 gate, pre the
sufficiency stop below).** A Ranking objective exists specifically to buy
position; capping the bid at cost-plus math caps the exact thing the
campaign was built to do.

**What governs instead:** rank, target rank, search volume, and placement
mix — bounded only by an absolute per-SKU sanity bound. That bound is
derived from each SKU's own CM2, but **it may only tighten an existing
flat, account-wide sanity ceiling (commonly ~$8–9), never loosen past it.**
A high-margin SKU's math computing a bound above the flat ceiling does not
authorize a higher bid than the account has ever tested — the flat number
stays the outer wall regardless of what any single SKU's math suggests.

**In practice, this allowance concentrates entirely on top-of-search —
stated here explicitly, not left to be inferred from three separate
rules.** ROS is excluded from the allowance outright (§4 — "on every
objective, with no exception"). PDP has no modifier at all, so it has no
mechanism to carry an above-ceiling price in the first place; it moves
only through base bid, which stays anchored to the product-page-
affordable click. That leaves top-of-search as the only placement where
a ranking row's above-ceiling authorization can actually be expressed —
so a ranking push being TOS-aggressive isn't a separate policy choice
layered on top of these rules, it's what these rules already produce by
construction. State it plainly in any reasoning that justifies a ranking
premium: the premium lives on the TOS modifier because that's the only
placement structurally capable of carrying it, not because TOS was
picked as a preference.

**Whatever above-ceiling premium a ranking row's top-of-search bid
carries is sized from that row's own rank gap, never a single percentage
applied to every ranking keyword on the roster.** A keyword five
positions from target and one a hundred positions away are not the same
decision, and pricing both with the same flat premium treats them as if
they were. Use the same maintain/moderate/full shape already established
for State B below — held near current where the gap is small, a
moderate premium within roughly 1.5× the gap, a fuller one beyond that —
rather than inventing a second, ungraded sizing rule for the same
problem. A roster of ranking keywords will show a roster of different
premiums as a result; a flat number across all of them is the signal
that this wasn't actually derived per row.

### Three candidacy classes, checked before the five-property gate

- **Cold** — a genuinely new term with no meaningful prior ranking
  history. Must clear the full realism gauntlet below before any push is
  funded; nothing about this class gets a shortcut.
- **Recovery** — a term whose best rank in the last 12 months was top 10
  or better, now sitting deeper because of a logged, resolvable cause
  (most often a stockout). Inherits the ceiling already proven at that
  position and gets priority in the portfolio push-allocation ordering
  (§1C's push-funding order) over an equally-sized Cold candidate — the account has
  already paid to prove this position is winnable; a Cold candidate
  hasn't. This is the same mechanic as §9's recovery-push, cited here as
  what determines candidacy in the first place.
- **Structure-blocked** — no live Exact campaign exists for this term at
  all, so there is no real performance history to read a verdict from
  regardless of how the keyword otherwise looks. This isn't a state to
  diagnose — it's a structural fact that has to be fixed (§9's same-day
  Exact fix) before the term can be classified as Cold or Recovery at
  all.

**The realism gauntlet — Cold candidates only, sourced in full, and
considerably more specific than this skill's launch-selection criteria
alone previously required:** search volume above 500; indexed and
actually placed in the listing (§1's indexing gate); genuine purchase
intent behind the query, not just topical relevance; conversion rate at
or above the market benchmark; not meaningfully behind competitors on
reviews (below roughly 50% of the top-5 median review count, or rated
more than roughly 0.3 stars under them); not priced more than roughly
1.25× the category's median paid price; inventory reading Green; and for
a thin-margin product specifically, a tighter cost ceiling — the
affordable CPC caps at roughly a third of margin, not the standard
CM2×CVR figure, because a thin-margin product has much less room to
absorb a wrong bid. **A Cold candidate failing any one of these doesn't
get a partial push sized around the gap — it doesn't clear candidacy at
all**, and the specific failed check is named as the reason.

### The five-property gate — checked before the seven states, not after

A
Ranking row only reaches the seven-state test below once it clears five
properties, checked at standup and re-checked whenever the row is
reviewed. Spend moving toward rank without all five isn't a slow push —
it's unpriced subsidy paying full auction cost for no governed outcome.

- **Sized.** A complete sizing block exists: target rank, DSTR (the
  market's own daily sales at that target rank, derived from competitor
  data — not from this product's current sales), the resulting order gap,
  required clicks/day, and required budget/week, all populated together
  from the same version of the underlying data. **Sizing is not complete
  until the order gap is also projected forward against inventory — new
  to this skill, a real gap this closes rather than a refinement of what
  existed.** The order gap this push is designed to close is, by
  definition, additional daily unit consumption on top of whatever the
  SKU is already selling — current days-of-cover describes the SKU at
  its *current* velocity, not at the velocity this push is explicitly
  trying to create. **Compute a projected days-of-cover specifically:
  current stock plus any confirmed inbound (each on its own ETA), burned
  down day by day at baseline velocity plus the order gap, checked
  against whether that stays above the routing-switch threshold through
  at least this push's own checkpoint date below.** A push can show
  healthy current days-of-cover and still be sized to run itself out of
  stock before its own checkpoint ever arrives if this projection isn't
  run — current cover answers a different question than this one does,
  and neither substitutes for the other. Where the projection shows the
  SKU would drop into Yellow or Red before the checkpoint, this is a
  blocking finding, not a silent go-ahead: state it plainly and resolve
  it one of three ways — size the push to a smaller order-gap target the
  projected supply can actually sustain, delay the push until the
  specific confirmed inbound shipment lands, or accept and time-box the
  risk explicitly if the account has a stated reason to run it anyway.
  Silently authorizing a push whose own success would create the
  stockout it's supposed to help fix is exactly the failure this check
  exists to catch. **This projection is what actually connects this
  gate's sizing to §9's inventory gate, rather than leaving them as two
  separate checks that never speak to each other** — §9's zone reads
  where the SKU sits *today* and is still required regardless (a Red SKU
  gets no new push no matter what this projection shows), but it isn't
  sufficient on its own, since it says nothing about where a successful
  push would put the SKU. Both checks run; neither is skipped because
  the other cleared.
- **Dated.** A horizon date and a checkpoint date both exist — not blank,
  not "ongoing."
- **Ceilinged.** A weekly loss ceiling is computed, not estimated: (push
  ACoS − break-even ACoS) × projected sales at the spend the push actually
  requires — never at current spend or current ACoS. **This property
  means the number is computed and stated, not that it functions as an
  automatic stop.** A push can spend its full computed ceiling while rank
  is still genuinely improving, and nothing here halts it automatically —
  reaching the ceiling with the row still working is a human-judgment
  point, flagged for review, not a rule that fires on its own. What does
  stop a push automatically is rank genuinely stalling (the seven-state
  test below), never the ceiling being reached on its own.
- **Predicted.** A written prediction exists before money moves: metric,
  direction, magnitude, horizon.
- **Funded.** The push has a dated release, not an informal start. Spend
  moving toward rank without a dated release is the failure this property
  exists to catch, regardless of how good the sizing looks.

**A row missing any one property is not a push, whatever its data
otherwise shows.** It doesn't get the seven-state test's above-ceiling
treatment; it gets corrected toward ceiling like any other row, and the
missing property is named as the reason. Building the missing property
(sizing it, dating it, ceiling it, predicting it, funding it) is the
prerequisite for entering the seven-state test, not an afterthought once
a push is already spending.

**A restocked SKU with a proven prior rank fills Sized and Predicted
differently — see §9's recovery-push mechanic.** Not a separate gate;
the same five properties, populated from the pre-decline baseline rather
than derived fresh.

**One more check before the seven states run, and it's the reverse of the
candidacy gate: is this keyword's rank credit actually being earned by
its own Exact campaign, or is it really being carried by auto or broad
traffic sharing the same term?** A keyword can look like it's ranking
correctly while most of its actual clicks come from a loosely-targeted
auto or broad campaign rather than the dedicated Exact instance the
ranking story is being told about. If that's what's happening, the "rank
is improving" narrative is attached to the wrong campaign — the precise,
managed instance isn't the one doing the work, and no bid decision on the
Exact campaign will move rank that auto is actually driving.

Check: if auto and broad together carry more than roughly 40% of a
Ranking-tagged term's clicks, or the term has no live Exact instance at
all, this keyword is **OUT OF SCOPE for a ranking verdict** until fixed —
never given a state from the table below, regardless of how good its rank
or CVR looks. The fix is structural (stand up or strengthen the Exact
instance, wall it from auto/broad per the isolation-negative rule), not a
bid change, and the keyword re-enters the seven-state test once its own
Exact campaign is genuinely carrying the traffic.

**A second pre-check, run before the table below, not folded into it — closing a real gap: is top-of-search actually carrying
this keyword's clicks, or are total clicks being propped up by rest-of-
search and product-page traffic that doesn't move rank at all?** "Clicks
above plan" in the table below is a blended total across every placement
— it does not by itself confirm top-of-search is delivering. Where total
clicks clear plan but top-of-search's own share of those clicks sits
below 30%, that's **PLACEMENT FIX FIRST**: rebalance the placement split
before touching the table below at all, regardless of what the blended
click count and rank trend would otherwise suggest. A keyword with fine
total clicks and a thin top-of-search share is not "Working" (State A)
or merely needing a push (State B) — pushing the blended bid harder
without fixing the split spends more money on placements that were never
going to move rank in the first place.

**The fix itself is the coordinated backward-solve §4 already defines,
applied here specifically — not a separate mechanism, and not "rebalance"
left unspecified.** Since PDP has no modifier of its own and moves only
through base bid, PDP's disproportionate click share can only come down
by bringing the base bid down. But base bid is also what TOS's price is
built from — TOS price = base × TOS modifier — so simply lowering base
would drag TOS's own price down at the exact moment TOS needs to be
winning more, not less. **The two moves happen together, in one pass:**
solve for what TOS actually needs to cost to win the position (the TOS
target, from that placement's own rank-gap-scaled ranking premium if this
is a ranking push), set the new base bid down toward PDP's own affordable
level, then re-solve the TOS modifier upward so base × modifier still
lands on the TOS target — base down, TOS modifier up, computed as one
backward-solve rather than two separate, uncoordinated bid moves. ROS
gets the same treatment in the same pass: re-solved from its own earned
target (§4), not silently dragged wherever the PDP-driven base change
happens to leave it.

### The seven states

Say which state governs on every ranking-eligible row; never give a
verdict a state can't support.

| State | Condition | Verdict |
|---|---|---|
| A | Clicks above plan, rank improving | Working — raise budget 20–30% in one step to sustain momentum, per the account's own source rule; hold TOS at or above 30% |
| B | Clicks above plan, rank flat | **Estimate was low.** Push harder and rebase targets from actuals — magnitude below. **Persistence check: if this same keyword is graded "flat" for 4 consecutive cycles under Step 0's cycle-over-cycle grading, this is no longer "push harder" — it becomes STOP-LOSS: concede or defer, reallocate the budget to the next winnable term. A label existed for this before; nothing actually triggered it. This is the trigger.** |
| C | Clicks below plan, rank flat | Delivery problem — check placement, then budget, then competitiveness before spending more |
| D | Clicks below plan, rank improving | Estimate was high; position winning cheaply — hold |
| E | Rank collapsing more than 10 positions despite delivery | **Not** an undersized plan — investigate competitor, listing or category before spending more; never scale spend on this state |
| F | Delivery only just at plan (≈95–120%) | Too early to read — hold and re-read next cycle. **Same persistence check applies: 4 consecutive cycles reading "too early" is itself a finding — escalate to a full review rather than holding indefinitely on the same verdict.** |
| — | No sized plan or no tracked rank movement | **OUT OF SCOPE.** Never give a ranking verdict the data can't support |

**State E's investigation is a structured comparison, not a vague
instruction to "look into it."** Using competitor analysis and listing
detail against our own:

1. **Anchor the timing.** Find the point where rank actually started
   collapsing, not just that it has. Every check below is anchored to
   before/after that point, not looked at in the abstract.
2. **Check our own listing first — it's the cheapest data to check.** Did
   anything change on our side around that timing: price, inventory or a
   stockout, review rating or count, content or images, a coupon or deal
   ending. **If yes, this is a finding for Brand Management, not a PPC bid
   decision** — carried in the Recommendations to Brand Management
   section. PPC does not attempt to bid its way out of a listing problem.
3. **Check the competitor(s) now outranking this term, using the same
   structured test that already governs conquest eligibility (S-C1):**
   does the competitor win on at least two of price, rating, or review
   count — or has this competitor had a stockout that opened the
   position. If a specific competitor clears this test around the same
   timing, name them as the found cause. The routing is to whether a
   conquest/PAT campaign against that competitor is warranted — not a
   ranking-bid push on our own term, which was never going to out-bid a
   listing-level advantage.
4. **Check whether the collapse is isolated to this one keyword/product,
   or shows up across others in the same category**, using the account's
   own portfolio data. Isolated points to something specific to this term
   or its immediate competitor; widespread points to a category-level
   shift — a bigger finding than this row's plan can resolve on its own,
   and gets escalated rather than treated as this keyword's problem.
5. **If none of the above finds a cause**, the row is named explicitly
   as "investigated, no cause identified this cycle" — never left in a
   "held" state indistinguishable from one that was never actually
   checked. **This is exactly the case §4A's ask-first rule covers: "no
   cause identified" is not itself a legitimate silent-hold reason** —
   it means the investigation ran and came up empty, not that holding
   flat is now the settled answer. Ask what should happen next rather
   than re-reading on the same schedule indefinitely with nothing having
   changed.

**None of these checks authorize a bid change on their own.** State E's
rule stands regardless of what the investigation finds: never scale
spend on this state. What the investigation produces is a routed finding
— to Brand Management, to a conquest/PAT decision, to a category-level
escalation, or to "still unresolved" — never a bid verdict by itself.

**This investigation sequence is itself sourced from the account's own
named diagnostic sub-rules, not an internally-derived checklist:** step
2 (check the listing first) is the account's own routing of a confirmed
conversion cause to its owner; step 3 (the competitor check) is the
account's own competitor-block read, applied here to a rank collapse
rather than a Conquest entry decision; anchoring the timing in step 1 is
what lets a stockout-period overlay on the rank series separate genuine
cause from coincidence, rather than reading a collapse that merely
coincided with a stockout as caused by it. Naming these sources isn't
cosmetic — it's what lets a future pass extend this investigation
correctly if the account's own diagnostic layer gets built out further,
rather than treating this skill's version as the final word on what the
investigation should contain.

**A lighter, earlier check runs before a row ever reaches State E's
10-position threshold — sourced from the account's own framework, not
previously in this skill.** Where CVR still reads at or above benchmark
but rank is declining, and no logged product event explains it (no
price move, no listing change, no OOS), that's a competitive-shock
signal, not yet a full collapse: check specifically for a new entrant, a
competitor deal, or a competitor price cut in the same window. Where one
is found, defend with one ladder step within the existing ceiling —
not a full Conquest response, not a rank-collapse-level investigation —
and review again in one week, not the longer cycle a heavier finding
would warrant. Log the shock explicitly, because it re-tests the row's
own ceiling assumptions once the shock has passed: a floor that held
before a competitor's temporary deal may not be the right floor to
return to once that deal ends.

**Magnitude for State B — the only state that needs a push size computed —
is scaled to the rank gap**, not to CPA/CVR/ACoS: maintain at target,
moderate push within 1.5× the gap, full push beyond 1.5×. This is
distinct from and does not use §5's graded push tiers, which are reserved
for non-ranking rows and post-sufficiency ranking rows.

### The sufficiency stop — settled, sourced from the account's own framework

**A ranking push ends when organic rank reaches or holds at or below
target for 2 consecutive weeks.** At that point the row transitions:
the objective flips from Ranking to post-objective — maintain the rank
just won, reduce ACoS back toward CM2. **The step-down rate here is its
own, gentler rate — roughly 10% a week — not the general 25%-per-cycle
correction cap §5 uses elsewhere.** This is a real correction to what
this skill previously specified: a row easing off a rank it just won is
a different situation from a row being corrected for sitting at the
wrong price, and the two were incorrectly sharing one rate. The 10%/week
pace steps the bid down from its push level toward the floor that still
holds the rank, recording that floor once found, rather than snapping to
ceiling immediately or correcting at the faster rate meant for an
overpriced row. **That floor itself is priced by a specific formula,
sourced from the account's own framework and not previously built into
this skill: roughly 5–10 cents below the delivering placement's own
blended CPC on that term** — not an arbitrary stopping point wherever
the ladder happens to land, but a number computed from what the
placement is actually costing to win, set just under it. Two consecutive
weeks, not four — a shorter, cleaner confirmation window than this skill
previously used, and one now tied to the actual thing being achieved
(rank) rather than a proxy for it (click share).

**The taper doesn't step down blind to what's happening to rank while
it does — a specific slippage tolerance, sourced and not previously
built into this skill, is what triggers restoring a step rather than
continuing down:** more than 2 positions of slippage on a term that had
been holding top-5, or any slippage below target at all on a term
outside the top 5, restores the last step taken — that becomes the
recorded floor, re-tested quarterly or after a logged competitive shock
(§7's shock check). A top-5 position gets more room to absorb a small
wobble before the ladder reverses; a term outside the top 5 doesn't get
that same cushion, because there's less position there to protect in
the first place.

**Deal-state and clean-state rank reads are tracked separately, per §3's
standing principle and the rank-trend read below.** The two-week count
advances only on clean-state weeks — a deal week's rank improvement is
real and kept as its own reading, useful for understanding deal lift,
but it doesn't advance or satisfy this stop on its own; a row cannot
exit its ranking push on a promotional spike that doesn't reflect
sustained, ordinary demand.

### Rank-trend read (feeds the state determination above)

Minimum one month of rank history required; below that, OUT OF SCOPE.
Any stretch inside the window where the routed SKU had a stockout or was
rerouted is excluded or discounted — a rank read across a disrupted
stretch describes the disruption, not the keyword. If the clean remainder
is too short after exclusion, OUT OF SCOPE for that cycle. Target is
whatever rank-target figure the keyword master or bulk already states —
never a new number invented for this check.

**The read is three separate windows, not one blended figure — new to
this skill.** State the overall trend across the full clean history,
**and** the last 14 days on their own, **and** the last 7 days on their
own, as three distinct readings, not folded into a single average. What
matters is whether they agree: a keyword whose overall trend is
improving but whose last 7 days have gone flat or reversed is a
materially different situation from one where all three windows point
the same direction — and averaging across the full history is exactly
what would hide that divergence. Where the windows disagree, say so
directly and treat the shorter window as the earlier warning, not as
noise the longer trend overrides.

**A deal week is not treated the same way as a stockout or reroute.** A
stockout or reroute is excluded because the data describes something
other than the keyword; a deal week's rank movement is real and describes
the keyword, just under different conditions. Per §3's standing principle,
track a separate deal-state rank arc for any deal weeks inside the
history — do not discard them, and do not blend them into the clean-state
arc. **The clean-state arc is what governs the seven-state determination
above.** The deal-state arc is kept as its own reading, useful for
understanding how this keyword's rank behaves during deals specifically,
but it never substitutes for the clean-state trend when deciding a
state.

### The incrementality ladder — is a paid spend on an organically-won term actually buying anything

A term holding organic rank at or above 3, with clean logs
(no active event in the window), is a candidate to test whether its paid
spend is incremental at all. Step spend down 15% and hold for two weeks;
compare total orders — organic plus ad — against the baseline from
before the step, not just the ad-attributed count alone. **If total
orders hold**, the prior spend was renting sales the organic position
would have earned anyway — continue stepping down. **If total orders
fall more than 10%**, restore the last step and record that level as the
floor — the paid spend was doing real incremental work at that level,
even though the organic position alone couldn't fully replace it.

**This is a distinct question from the sufficiency stop above and runs
on its own schedule, not as a substitute for it.** The sufficiency stop
asks whether a *push* has achieved its target and should stop pushing;
the incrementality ladder asks whether spend that's already at
maintenance level on an *already-won* position is still earning its
keep at all, which can be tested well after the sufficiency stop has
already fired.

### SBV arbitrage — when Sponsored Brands Video is cheaper than the same click at Exact

Enter SBV on a term when its own CPC reads at or below
0.6× the equivalent Sponsored Products Exact CPC, and its CPA clears its
own ceiling — a genuinely cheaper surface for the same demand, not a
default preference for one ad type over another. Exit when SBV's own CPC
converges back past 0.8× of the SP Exact CPC, or its completion rate
fades for two consecutive weeks — either signal means the arbitrage that
justified the entry has closed. **Judge SBV rows on their own metrics —
view-through CTR, completion rate, new-to-brand percentage, and CPA —
never on Sponsored Products metrics**, which measure a different kind of
attention entirely and would misread a genuinely working SBV placement as
underperforming by SP standards it was never trying to meet.

---

**Every funded push carries its own five-property record, and the
account-state gate table is not that record.** A gate table reading the
account as it stands before deployment is a snapshot of the starting
position; the pushes the plan actually funds are the plan's own
decisions and each needs all five properties met on its own row —
sized, dated, ceilinged, predicted, funded. **Two of the five are
decisions the plan takes, not conditions it waits for**: dating and
funding are chosen, and a plan that reports them Not Met while
simultaneously dating and funding four pushes is contradicting itself
in the reader's hands.

**Every push carries a computed loss ceiling and a taper condition.**
The loss ceiling is (push cost of sale − break-even) × projected sales
across the push's own horizon, in dollars, dated — the number the push
stops on. The taper condition names the rank that ends the ranking
premium and what happens to the spend when it is reached. **A push
without a taper is this skill's named signature failure**: the account
has previously lost money on campaigns that succeeded and kept paying
the premium afterwards. Reversal conditions covering only failure paths
leave the success path unmanaged, which is the more expensive one.

**Where a shared head term has no declared owner, a push on it gates on
that ruling and the gate is written into the roster.** Naming the
ownership gap in a cross-comparison section and then opening pushes on
the same terms elsewhere in the document is not a gap honestly stated;
it is a gap stated and walked past. Either the pushes carry the gating
decision by number, or the plan asks for an explicit waiver. **Sibling
data inside the same company is never "unavailable"** — it is not yet
requested, and a reviewer reads the difference.

## 8. Fixed-bid trial

Triggers on **both conditions together, not clicks alone**:
CPC already sitting materially above ceiling by a wide margin, *and*
clicks still low. That combination is the suppression signature — a
price that should be winning auctions but isn't producing volume. Clicks
being low with CPC already at or near ceiling isn't this trigger; that's
simply a low-search-volume term behaving normally.

**This trigger is read on the bid actually in force, whichever rule set
it — not only on a bid that arrived here without §5 already touching
it.** A row §5 corrected to ceiling last cycle now has a CPC that reads
"at ceiling," not "above" it — read literally, that could look like it no
longer qualifies. It still does. A row corrected to ceiling this cycle is
checked against this trigger next cycle on its own terms: if clicks are
still low at the corrected price, that is the suppression signature, full
stop, regardless of whether the current price was always here or just
arrived by correction. Exempting a freshly-corrected row from this check
because its CPC technically isn't "above" ceiling anymore is exactly the
gap this rule exists to close — the two rules are meant to run in
sequence on the same row, not to hand off a row that then falls through
the gap between them.

Switch to fixed bid, same price, same match type, same wall — nothing
else changes. Evaluate normally at 15 clicks. **§5's price correction
runs first if the row also qualifies for it** — see the sequencing note
there. Single-keyword campaigns carry a $10–15 daily cap for the
duration; multi-keyword campaigns skip the cap and get a fixed 7–8 day
review instead.

**This same data-driven trigger, not a fixed objective-based default,
governs strategy switches on any already-running row, on any objective.**
A Ranking row showing the suppression signature switches to fixed the
same way a Profitable Conversion row would — objective doesn't override
what the data shows on a row already in flight. What objective *does*
set is the strategy a campaign opens on, per §4's bidding-strategy table.

---

## 9. Inventory gate — a graduated read, not a single cutoff

**Three zones, not a single 60-day cutoff:**

- **Green — 60+ days of cover.** No inventory restriction. Push,
  hold-above-ceiling authorization, and budget scaling are all available,
  subject to everything else this skill requires.
- **Yellow — below 60 days but at or above the routing-switch threshold
  (commonly 21 days).** Freeze the push at current spend. Not scaled
  further, not yet re-routed — held exactly where it is until cover
  recovers or degrades into Red. This is the zone the flat version of
  this gate used to collapse into an undifferentiated "hold flat," which
  lost the distinction between a SKU that's merely tightening and one
  that's about to run out.
- **Red — below the routing-switch threshold.** Taper to defense and
  re-point to the next child in this syntax's own priority flow **the
  same day** — not at the next scheduled cycle. **Rank preservation over
  rank progress**: the goal in Red is holding whatever position already
  exists through the routed child, not continuing to chase a target on
  a child that's about to go dark.

**Routing is a priority flow, not a single preferred-plus-one-backup
pair — this was previously built as a binary and needed correcting.**
Each syntax carries its own ordered list of which child to route to,
first choice through however many exist — not just one fallback with
nothing defined beyond it. **The list is per syntax, not one flat order
for the whole product**, because different syntaxes can genuinely have
different priority orders on the same product (a "queen size" syntax
and a "king size" syntax don't necessarily share the same available
variations or the same reasons to prefer one over another). When the
current child in a syntax's flow goes Red, route to the *next* child in
that same syntax's own list — not to whatever the product's other
syntaxes happen to be using, and not stopping at a single backup with no
plan for what happens if that one also runs low.

**The next child's own current inventory is checked before routing to
it — never assumed available just because it's next in the priority
order.** The priority order reflects business preference (margin,
historical performance, which variation the account would rather sell)
— it says nothing about which child actually has stock *right now*, and
those are two different questions. Before routing to the next name on
the list, read that child's own current zone the same way the departing
child's zone was read. Where it's also Yellow or Red, skip it and check
the one after that, continuing down the list until a Green (or at least
not-Red) child is found.

**Inventory is the gate; once it's cleared, current performance is what
actually decides among the candidates that clear it — not a static list
order treated as settled fact.** Where inventory rules out only some
candidates and more than one remains genuinely viable, the choice among
those survivors is re-checked against each one's own current order
velocity, margin, and recent conversion history — the same criteria this
skill already uses to break a duplicate tie (higher CVR at lower CPC,
longer clean history) — not a mechanical walk to "whichever name comes
next" on a list that may have been set once and never revisited. A
priority order is a reasonable starting point; it is never a substitute
for checking whether the assumed-best candidate is actually still the
best-performing one at the moment routing happens. Where the re-check
confirms the existing order, state that plainly rather than silently
skipping the check because the answer was expected to agree.

**Every reroute — whatever triggered it — carries a mandatory economics
rebuild for the newly-routed SKU, not just a routing update.** This
requirement already existed in this skill for one specific trigger
(§11's SKU-provenance check, for a campaign discovered to have been
pointed at the wrong variation from the start) but was never connected
to the far more common trigger that needs it just as much: an ordinary
inventory-driven reroute through this section's own priority flow, or a
reroute chosen on performance grounds among viable candidates, above.
**The same rebuild applies regardless of why the reroute happened**:
affordable CPC, the CPA target, break-even ACoS, and the margin and AOV
figures feeding all of them are recomputed from the *new* SKU's own real
numbers — never carried over from the SKU that was just left. A ceiling
still priced against the departing SKU's margin is exactly the failure
§11 already names for the wrong-from-the-start case, and it's no less
wrong here just because this reroute was routine rather than a discovered
error. The CVR baseline and rank-trend clock reset from the reroute date
forward, the same way §11 already requires — a keyword's history under
its old SKU doesn't carry over as if it describes the new one.

**Routing to a second child without checking
its own zone first is the same failure as never checking the first
child at all — it just moves the problem one step down the list instead
of solving it.** If every child in a syntax's flow is checked and all
are Red at once, that's escalated as its own finding — a genuine supply
problem, not a routing decision this skill can resolve on its own —
rather than silently holding on the last child in the list as if
routing had succeeded, or worse, routing to it anyway without having
verified it can actually carry the traffic.

**Audit the inventory export before trusting any zone assignment it
feeds.** Compute on-hand minus available minus reserved for the SKU in
question; any gap above 5 units is a signal to verify against the source
inventory system before acting. An available-column understatement can
silently place a SKU in the wrong zone — treat the inventory export as a
data source that can be wrong, not a number to act on unquestioned.

**A Yellow or Red zone assignment is not "hold and wait" — it carries a
named, dated re-entry plan.** State the specific restock date, the
specific keywords that resume on it, and the target rank each resumes
at. A hold with no dated resumption reads as abandonment by the time the
SKU restocks; the plan should already say what happens on that date
before it arrives, not leave restart as an undefined future event.

**Peak-week availability outranks aged-stock and LTSF economics in every
tradeoff at the margin, stated as a priority rule, not left implicit.**
Where a product's own demand calendar marks a week as peak and the
routed SKU's zone would otherwise pull toward a forward-cash, clearance-
minded posture, peak-week zone status governs instead — a stockout
during peak destroys rank at a cost this account prices at roughly a 3x
recovery multiplier, while carrying modest excess past peak costs
storage. Storage is the cheaper mistake. This only applies where a
demand calendar or deal schedule actually marks the week as peak; absent
that, LTSF and forward-cash rules govern as stated elsewhere in this
skill (§3).

**A high days-of-cover number is not automatically "safe to push" —
check the velocity trend before reading it that way.** A SKU sitting at
60+ days of cover with velocity declining 15% week-over-week for three
consecutive weeks is a trajectory problem, not a healthy SKU with room
to spare: the cover number is rising because demand is falling, not
because supply is generous. Confirm the trend before treating a
comfortable DOS figure as license to scale.

### Recovery push — the mechanic for a restocked SKU with a proven prior rank

**A term qualifies for a recovery push, not a cold ranking push, when
all of the following hold:** the routed SKU's zone has just returned to
Green from Yellow or Red; the term's rank history shows a genuine prior
position (commonly top 5–10) before the decline; current CVR is at or
above benchmark; and the cause of the prior rank loss is logged and
attributable to the inventory event, not a listing or offer problem.

**A recovery push is funded toward the pre-decline baseline, not toward
a freshly-derived target.** This is the specific difference from a cold
ranking push: §7's five-property gate ordinarily derives its target rank
and required-clicks math from scratch; a recovery push instead uses the
rank the term already held before the decline as both its target and its
evidence that the position is achievable — the listing has already
proven it can hold that spot, which a cold push has yet to prove for any
target. **Expect faster velocity than a cold push would show, and read
the term against that faster expectation, not the standard ramp** — a
recovery push that's moving at cold-push speed is underperforming its
own baseline even if it would look adequate as a fresh push.

**This does not bypass the five-property gate — it changes what fills
two of the five properties.** Sized and Predicted are populated from the
pre-decline baseline rather than derived fresh; Dated, Ceilinged, and
Funded still apply exactly as §7 states them. A recovery push missing
any of the five is still not a push, the same as any other row.

**The recovery play runs on a specific weekly sequence, sourced from the
account's own framework, not launched all at once.** Week 1: re-point the
campaign back to the restored variation and restore maintenance-level
bids — nothing more aggressive yet. Week 2: open the recovery push itself,
sized toward the pre-decline baseline as above. Checkpoint against the
term's own historical best rank at three weeks. **The play budgets for a
slower first week and does not panic-bid into it** — a rank echo (a
delayed response while the algorithm re-learns the restored variation) is
expected, not a sign the recovery is failing.

### A decided ranking term with no live Exact instance is a same-day fix, not a harvest candidate

Where a term has already been decided
as a ranking priority — named in the plan, carrying real search volume,
genuinely part of the product's ranking roster — but has zero live Exact
campaign and its traffic is being carried entirely by Broad or Auto,
this is not treated as a Discovery candidate waiting to clear the
100-click harvest bar. **It's a same-cycle structural fix**: stand up the
Exact campaign under this skill's naming and objective conventions,
sized per §7, and steering-negate the term inside the Broad/Auto
campaigns carrying it so evidence and control consolidate onto the new
Exact instance. A decided ranking term sitting in Auto or Broad only is
spend without intention — the traffic is real, but nothing is being
learned from it in a form that can inform a ranking decision.

---

## 10. CVR and ACoS as the performance lens

Applies to non-ranking rows, and to ranking rows
once they've cleared §7's sufficiency stop.

**The ceiling and the CVR baseline do two different jobs and must never
be built from the same number.** The ceiling (§3, §4) answers *what can
we afford* — it stays on a fixed planning assumption per placement, set
once per product and held stable for that product afterward, never
recomputed from a product's own ongoing results. **That planning
assumption is a per-product input, not a universal constant — this
needed correcting.** An earlier version of this rule stated one fixed
set of figures (6.0% PDP, 10.4% ROS, 14.7% TOS) as if it applied
permanently to every product; those numbers read as if they were derived
from one specific product's own category and carried over as a fixed
default, which a genuinely different product (a different category, a
different price point, a different kind of buyer) has no reason to
share. **Each product sets its own placement-level planning assumption
once, from that product's own category data or its own early real
performance, and that product's own figure then holds stable
afterward** — the anti-circularity principle below is about not letting
the ceiling chase a product's own *ongoing* performance week to week,
not about every product in the account sharing one number regardless of
category. The CVR baseline answers a different question — *is this row
earning what's normal for this product, here* — and it is the one
figure in this skill that's explicitly built from live, product-specific
data rather than a fixed assumption.

**If the ceiling moved with the product's own real CVR, the baseline
comparison would collapse into circularity** — a row converting near the
product's own average would look "at ceiling" almost by construction,
because the reference point would no longer be independent of what it's
measuring. Worse, a temporary rough patch (a stockout on the routed
child, a listing problem) would shrink the ceiling exactly when the
product needs room to recover, and a temporary spike (a deal week) would
inflate it past what the underlying economics actually support once the
spike passes. The ceiling holds the affordability line steady through
both; the baseline is what's allowed to move.

**Computing the baseline:** for the product currently being evaluated,
aggregate its own clicks and orders at each placement — TOS, ROS, PDP —
across its own bulk, and compute that product's own CVR at each one.
These three numbers, refreshed each cycle directly from the product's own
data, are the baseline a row's realized CVR gets compared against — a
keyword's TOS CVR against this product's own TOS baseline, never against
ROS's or PDP's, and never against a different product's figures. This
replaces the earlier provisional, cross-product estimate entirely: it is
no longer a guess to be re-derived later, but a live computation drawn
fresh from the bulk every time.

**Where a deal window falls inside the bulk this baseline is drawn from,
compute two baselines, per §3's standing principle** — a clean-state
baseline from non-deal weeks, and a deal-state baseline from deal weeks,
never blended into one figure. A row being judged during an ordinary week
is compared against the clean-state baseline; a row being judged during
an active deal is compared against the deal-state baseline, if one
exists. Comparing deal-week performance against a clean-state baseline
would make it look artificially strong for no meaningful reason — deals
generally convert higher, so the comparison would just be restating that
a deal is a deal, not surfacing anything about the row itself. If no
deal-state baseline exists yet for this product, a row's in-deal CVR is
flagged as unjudged for that context rather than measured against the
wrong reference point.

- **Break-even ACoS is computed per-SKU and stated alongside CPA-vs-
  ceiling on every push/cut decision** — a confirming lens, not a new
  variable. Where the two diverge, flag it; never resolve silently by
  either alone.
- **AOV source is set by objective:** advertised SKU for Ranking and
  Profitable Conversion; routed-to SKU for Conquest (never the competitor
  listing the ad appears on); campaign-blended AOV for Discovery before a
  child is confirmed.

**Three named Profit-objective states, sourced from the account's own
framework, not previously in this skill:**

- **Price attribution.** A CVR decline coinciding with a logged price
  increase in the product's own event log holds bids — it doesn't get
  judged as a conversion failure. Either the price move is reverted, or
  it's accepted and break-even, ceilings, and every target this row
  reads against are recomputed from the new price *before* any verdict
  resumes. Judging a row's CVR against ceilings built on a price that no
  longer applies produces a verdict about a product that doesn't exist
  anymore.
- **ROS-weighted strategy, named explicitly when it applies.** A term
  profitable only at rest-of-search, with no rank case behind it, runs
  with zero or a minimal top-of-search modifier — it's buying profit at
  the cheapest placement, not position, and the plan states this
  plainly rather than leaving a reader to infer why top-of-search is
  untouched.
- **An AOV shift from a variation-mix change voids every verdict built on
  the old figure.** Where the advertised SKU's own mix has shifted enough
  to move blended AOV, every ceiling and every verdict computed against
  the prior AOV is void until the economics block is refreshed and the
  row is re-run — not patched, re-run, since a verdict built on a
  since-moved AOV isn't a small error, it's a conclusion about numbers
  that no longer describe the row.

---

## 11. SKU-provenance check — before trusting any performance history

Before any push/hold/cut decision reads a keyword's CPA, CVR,
or rank history, confirm which SKU was actually enabled over the window
that history spans, using Product Ad states from the long-window bulk and
the two 7-day windows.

- **Match** → proceed with the normal evaluation.
- **Mismatch** (different SKU enabled the whole window) → correct to
  20–25% above ceiling immediately if over (§5), then start a clean read
  forward.
- **Mixed** (SKU changed mid-window) → isolate the clean portion after the
  last change; use it if it clears the 15-click floor, else formula-only.

**A second, different check: is the campaign even pointed at the right
variation to begin with — not "did routing change over time," but "was
it ever right."** A campaign can be nominally set to advertise one
variation (a specific size or style) while the search terms actually
converting on it mostly belong to a different variation in the same
family — the ad never routed away from anything; it was pointed at the
wrong one from the start, and every ceiling built on it has been computed
against the wrong variation's margin the whole time.

Check: for any keyword or campaign carrying meaningful volume, compare
the declared/routed variation against what the converting search terms
and orders actually indicate. Where a clear majority of conversions
belong to a different variation than the one the campaign is nominally
priced against, that's a routing error, not a performance problem — no
amount of bid correction fixes a ceiling computed on the wrong SKU's
economics. The fix is re-pointing the campaign to the variation it's
actually selling, rebuilding the full ceiling stack on that variation's
real contribution and AOV, and resetting the CVR baseline and rank-trend
clock from that point — the old history belongs to a campaign that,
economically, was advertising something else.

**When the readings conflict and re-pointing is not available this
cycle, the advertised SKU governs the pricing and the shipping split
becomes a finding.** The rule above resolves cleanly when a re-route
can be taken. When it cannot — a campaign whose name, whose advertised
SKU and whose converting orders point at up to three different children
— something still has to set the ceiling, and leaving that unstated
prices the row against whichever child the build happened to read
first. **Price on the child the ad actually serves, and raise the
divergence with the click and order counts attached.** A high share of
units shipping on a sibling is a halo pattern at the point of purchase,
not proof the campaign points at the wrong child, and it is not a
reason to move a ceiling; if the split is the intended outcome, the
advertised child is changed deliberately rather than through a bid.

**This resolution depends on the advertised SKU being readable, which
it is not in a file carrying no Product Ad rows.** Where the deliverable
has none, it cannot show which child is enabled inside a multi-ad
campaign, and every ceiling in it rests on a column no reader can
verify. State that limitation on the face of the file as a named
condition with an owner and a date — never leave the ceilings reading
as though the routing behind them were confirmed.

**Halo rate — the share of units shipping on a SKU other than the one
advertised — is a named, cited metric wherever a re-route is proposed,
distinct from the provenance check above.** Provenance asks what actually
ran historically; halo asks how much cross-sell already happens at the
point of purchase, right now. A high halo rate (the advertised SKU
functioning mainly as the thumbnail and entry point, not the item that
ships) is the specific evidence that makes a re-route low-risk — cite the
rate directly rather than asserting a re-route is safe without it.

**Where every row on a product fails this check at once — a mass
re-route, not a handful of mismatches — a temporary pooled estimate
across the affected rows is the only honest placement basis available,
and using it is correct.** But two things follow from that, and both are
required, not optional. First, the pooled figure is a stand-in for
missing data, never a shared verdict — it does not make the affected
keywords one decision; each one still carries its own SV, its own rank,
its own routed SKU stated by name, even while borrowing the same
placement rates. Second, and this is the part easy to get wrong: **the
row graduates from the pooled estimate to its own individual placement
read the moment *that specific keyword* clears its own 15-click floor on
the correct SKU — never on a single calendar date set for the whole
group.** A fixed re-derivation date for every affected row is the wrong
mechanism regardless of how reasonable the date sounds: some keywords
will earn real data well before it and sit needlessly on a shared guess
until the date arrives; others won't have earned enough by then and get
treated as settled anyway because the calendar said so, not because their
own data said so. State a re-derivation date as a checkpoint to review
progress, never as the trigger that graduates every row simultaneously.

---

## 12. Discovery candidacy gate — before any discovery layer is priced

*(The 100-click threshold is settled, an existing account requirement.
The near-miss state and the per-keyword-vs-per-cluster resolution are
refinements proposed to how the gate is read, not changes to the
threshold itself.)*

**Two paths into this gate, not one.** The reactive path is the 100-click
threshold below — an individual term earns its own way into Discovery by
proving out at Exact first. The proactive path comes from §1B: a syntax
carrying a match-type coverage gap (a Primary syntax at 0% phrase
coverage, for instance) is a standing reason to build a discovery layer
on that syntax *before* any individual term inside it has proven
anything — the gap itself is the evidence, not a substitute for it. State
which path opened a given campaign; a discovery build justified by a
coverage gap is judged on closing that gap, not retroactively held to the
100-click standard that governs the other path.

**A term needs 100+ qualified clicks on its own proven Exact-match history
before it is eligible for any Broad, Phrase, or Sponsored Brands/Video
launch under the reactive path.** Discovery layers never discover a
brand-new, never-before-run term this way — they only ever expand a term
that's already proven itself at Exact.

- **Below 100 clicks, the term is not eligible**, full stop — no pricing
  rule runs on an ineligible term.
- **Add a named near-miss state** rather than a silent binary: a term
  sitting close to the threshold (e.g. within 20 clicks of it) reads
  differently from one at a handful of clicks — both fail the gate today,
  but one is worth watching next cycle and the other isn't yet close.
- **Whether the count applies per literal keyword text or rolls up across
  a root cluster is unresolved.** Per this skill's confidence-tier rule
  (Step 0), the first time this choice would actually decide whether a
  term clears or misses the 100-click gate on a product, ask which
  counting basis governs — once confirmed for that product, it holds for
  every later cycle without asking again.

Once a term clears this gate, **check for an existing instance before
building anything new — a real gap this closes.**
The same duplicate-ownership rule that governs Exact (§2A: matched on
normalized text, never reordered) applies here just as much, and
nothing before this point had actually said so. Search for that same
term already targeted in a Broad, Phrase, or Auto campaign anywhere in
the account — a leftover from an earlier cycle, or sitting inside a
broader catch-all campaign. **If one exists, pull its current state
and its actual performance data and decide from that** — reactivate,
adjust, or leave it running as-is, whichever the data supports — rather
than building a second campaign for the same term blind to what's
already there. Only once this comes back clear does a genuinely new
campaign get built. Pricing follows: new Broad/Phrase/Auto
campaigns price below Exact, never above it, and carry no placement
modifier at launch — a campaign with no delivery history has no measured
basis to prefer one placement over another. **The specific ratio comes
from the candidate's own relevancy tier (§2A), not one flat number
applied to every launch regardless of fit.** A Highly Relevant term —
names the product exactly, every defining attribute present — prices
with more confidence, toward the higher end of what's affordable below
Exact; a Semi-relevant term — correct category, missing the qualifier
that would confirm it — prices more conservatively, toward the lower
end, because the uncertainty about fit is itself a reason to risk less on
it before it's proven. **The account's observed range combines two
dimensions, reconciled here into one statement rather than stated two
different ways across this skill's own two files** — the ratio starts
from match type (Broad commonly toward 60% of the Exact ceiling, Phrase
commonly toward 80%, since Phrase's tighter matching earns more
confidence than Broad's wider net), then moves within that starting
point by relevancy tier the same way described above — a Highly
Relevant Broad candidate can price toward the upper part of Broad's own
range, a Semi-relevant Phrase candidate toward the lower part of
Phrase's. Match type sets which range; relevancy tier sets where in it.

**Auto's four match types are not one undifferentiated bucket — split
reporting by group before judging any of them, per the account's own
source rule.** Close match, loose match, substitutes, and complements
are reported and judged separately, never blended into one Auto-wide
read: a substitute or complement match can be a real product with real
demand that simply isn't this one, and blending its clicks into close
match's own numbers hides that distinction rather than surfacing it.
Splitting the report is the mechanism; the harvest bar itself, below, is
the same **≥3 orders** for every group with one named exception, not a
harder bar for the more speculative ones.

**A converting term surfacing in a taxonomy cell with no syntax tag at
all is routed to classification first, before any harvest judgment.** A
term that hasn't been tagged into the account's syntax taxonomy can't
receive a priority class, a spend-share cap, or a correct objective — the
harvest question doesn't even apply until the classification gap is
closed.

**Discovery's own CPA/CVR judgment begins at the same 15-click floor as
every other objective in this skill (§5) — stated here explicitly rather
than left to be inferred by extension.** Below 15 clicks: no performance
verdict on the campaign itself, formula-only correction if price is off
ceiling, same as anywhere else. "Not judged on CPA in the first cycle"
means this floor, not an undefined grace period.

### Harvest — settled, sourced from the account's own framework

**A discovery search term harvests into its own dedicated Exact
campaign — priced and launched through the ordinary §2A selection
process — the moment it reaches 3 or more orders.** One test, not two:
not a click floor combined with a conversion-rate comparison, just orders
reaching 3. Below 3 orders, the term stays in Discovery, re-read every
cycle, exactly as before.

**One override, and it goes the opposite direction from what a "weaker
match type" intuition would suggest: a term already decided as a ranking
priority graduates even below 3 orders when Auto close-match is carrying
its traffic.** The 3-order rule is calibrated for an *unknown* term
proving itself for the first time; a term the plan has already named as
a ranking priority doesn't need to re-prove relevance through order
count — it needs its own Exact instance immediately, per §9's same-day
fix. Known heads move to Exact regardless of order count; unknown terms
still need their 3 orders. State explicitly which case a harvest is —
"decided head, graduated early via the override" reads very differently
from "unknown term, cleared 3 orders on its own," even though both end
in the same Exact campaign being created.

**A relevant term that isn't converting is never negated outright — it
routes to the fix queue, the same rule this skill applies everywhere
else** (§13's never-list). Wasted-spend share above the objective's own
limit (commonly 40% for a Discovery campaign, 10% elsewhere) triggers a
negation pass — but that pass pre-loads negatives from the account's own
taxonomy at launch, rather than being invented ad hoc per product; it
doesn't retroactively negate a term this skill would otherwise route to
a fix.

**The moment a term harvests, the plan states that it is negated inside
the campaign it came from, in the same deployment that creates its new
Exact campaign — never as a follow-up.** Skipping this means the new
Exact campaign and its own parent Discovery campaign compete against each
other indefinitely, with neither able to prove out cleanly against the
other's contamination.

**A term that draws clicks but never clears the harvest bar stays exactly
where it is, re-read every cycle under the same test.** Nothing pulls it
out early on a hunch, and nothing ages it out of Discovery on a timer
either — it graduates when its own data says so, or it doesn't, and the
plan states which for every candidate carrying meaningful volume rather
than leaving the ones that never cleared silently unaddressed.

---

## 13. The writing standard every verdict must meet

**Which tab or section a decision is written to is part of the writing standard, not a separate filing question, and it has been got backwards. Contexts governed: every Action, Reasoning and Reverses-If cell produced by this file or its companion workbook, on every entity type.** A row already built in the account — enabled, paused, or inside a paused campaign — is a live row, and its decision belongs in the decided uploadable file alongside the bid, budget and modifier fields it changes. A term not yet targeted is a new-launch proposal, and its decision belongs in the per-keyword planning tab, where routing, rank target and syntax live. On a real build these were written the wrong way round, so the uploadable output carried proposals and the planning tab carried changes to live campaigns. **The test is not what the decision is about, it is whether the row exists in the account today.**

**This standard applies uniformly across every section, every keyword,
and every objective in the plan — regardless of whether the underlying
rule was part of this skill's original build or added in a later pass.**
A verdict governed by a rule added recently doesn't get more scrutiny
than one governed by a rule that's been settled from the start, and a
verdict governed by a long-standing rule doesn't get to read thinner
just because the rule itself is familiar. The depth requirement below is
the floor for every decision in the document, not a target that only the
newest mechanics are held to.

**This floor is about honesty and specificity, not about matching the
length of an oversight-class section — that distinction is §1A's
tiering, and the two are not in tension even though they can read that
way stated separately.** Every keyword still gets its own reasoning,
computed from its own data, never templated regardless of size or spend.
What §1A's tiering changes is how much there is to say: a term below the
250 SV / top-spend-decile line, with no gate fired and no threshold
breached, has a short, honest, term-specific reasoning to give — its own
SV, its own clicks and orders against the sample floor, why nothing is
happening this cycle — not the full multi-part chain (market context,
the adjacent-lever comparison, a stated reversal condition) an
oversight-class term carries in full. **The moment an exception alert
fires on a tail term — a gate trips, a threshold is breached, a
genuinely new pattern shows up — that term is no longer exempt from the
full chain for this cycle,** regardless of its SV. Short is not the same
as templated: one line citing this term's own 15 clicks and its own zero
orders satisfies the floor; one line that would read identically on a
different keyword does not, no matter how far down the tail it sits.

A plan passes only when a reviewer can challenge any single decision and
the sentence answers for itself, without anyone re-deriving the analysis.
Displaying a metric next to a verdict is not the same as using it.

**Every reasoning statement runs the full chain, in order:** what is
happening → what the history says → what the market says → what the
objective is → what the actual numbers say versus the estimate → what
action follows → why this lever and not the adjacent one (§4A) → why it
is economically safe → what reverses it and when it is re-read.

**Mandatory content within that chain:**

- **Every cited number carries the date or date range it reflects, not
  left for a reader to guess how current it is** — and worth stating directly: "CVR 14%" without a window is a different,
  weaker claim than "CVR 14%, last 7 days (Aug 14–20)," and a reasoning
  statement citing the long 60–90 day window for context states that
  range too, so a reader can tell at a glance whether a figure is this
  cycle's live evidence or background context.
- **Named numbers doing work**, not adjectives — not "CVR is strong" but
  "CVR 14.8% against a target of 5.77%, 2.6× what the position requires."
- **The rank arc, not a point** — prior → recent → current, with the
  source of each figure and which one governs where they disagree.
- **The placement split stated before any bid recommendation** — §4's
  per-placement judgment, shown, not assumed.
- **The economic ceiling with its arithmetic shown**, inline, never a
  formula's name standing in for the number.
- **Why not the adjacent lever** — one clause minimum, citing §4A.
- **Every previously flagged condition touching this row, named** — a
  stockout, a SKU-provenance mismatch, an OUT OF SCOPE ranking state, a
  candidacy-gate failure — carried forward, never silently dropped.
- **The re-read** — what would change the verdict, and when it's next
  examined.
- **On any cut, whether the term is actually contested** — auction density
  (§3) named as part of "economically safe": a cut on a term no paid
  competitor bids is a different, safer decision than the same cut where
  several do, and the reasoning should say which case this row is.
- **The keyword's own syntax and that syntax's current diagnosis** (§1B)
  — a keyword inside a chronic Conversion syntax is a different situation
  from the same keyword's own numbers read in isolation, and the
  reasoning states which.
- **The term's own campaign-type footprint against what its objective
  requires** — a Ranking term with no discovery layer feeding it, or a
  term running in a campaign type with no stated reason, is named the
  same way a missing inventory zone is. *(Restored — sourced from the
  Deal Frameworks reference and Master PPC Decision Framework, both of
  which name campaign type as a required per-keyword field; absent from
  this skill until a real product owner named the gap directly on a
  live bulk file.)*
- **Provisional, pending confirmation: where at least one other keyword
  shares this term's syntax and has its own readable CVR/CPA (15+
  clicks), name where this row sits relative to that peer -- above,
  below, or in line -- not just the syntax's own aggregate diagnosis.**
  This is not directly stated in the account's own framework documents
  the way the campaign-type requirement above is; it is a reasoned
  extension of the existing syntax-rollup rule, answering a real
  product owner's request for "performance of other similar keywords"
  alongside syntax. Ask before applying on a product's first cycle, per
  this skill's own provisional-tier handling; once confirmed for a
  product, it holds without asking again.
- **On any row where above-ceiling spend is being justified as a
  ranking push, the routed SKU's inventory zone named alongside the
  five-property gate status, not the gate cited alone** (§1C). A
  five-property gate that clears while the SKU sits Yellow or Red is an
  incomplete justification, and the reasoning states the zone explicitly
  rather than leaving it assumed.
- **A formula-only correction's stated reversal condition names two
  separate tests, not one.** "Reverses if the term converts above the
  rate that makes its bid affordable" is the right test for a row with
  clicks already accumulating — but stated alone, on a row that has none
  yet, it silently assumes the row will get clicks to convert at all. It
  won't necessarily: a price corrected to ceiling can still be too low to
  win enough auctions to ever be tested, and that is a different failure
  mode from converting badly, with a different fix (§8's strategy switch,
  not another price move). Every formula-only correction states both —
  whether the row converts well once it has clicks, *and* whether it gets
  clicks at all at the corrected price — rather than the first alone
  standing in for both. A reasoning statement naming only the conversion
  test is incomplete even though it satisfies the general "re-read"
  requirement above.
- Where a decision rests on a thinner basis than the rest of the plan, say
  so — including which confidence tier (settled / provisional /
  refinement-proposed) it draws on.

**Specific is not the same as understandable, and both are required.** A
statement can use this row's own real numbers and still fail a reviewer
if those numbers are listed without a clear line from evidence to
verdict. The test: a reviewer with no other context should be able to
read the decision and its reasoning and answer, without a follow-up
question, three things — what changed, why this row's own metrics justify
it, and what would have to be true for the decision to be wrong. Accurate
and specific numbers that don't add up to an answer a reviewer can follow
have not met this chain's requirement, even though nothing in them is
false.

**Every internal label or code this skill draws on is scaffolding for
building the row, never text that reaches the delivered plan — and this
covers two sources, not one.** The first is this skill's own
cross-referencing: "State E," "the sufficiency stop," a confidence-tier
tag, "§5," "§8," "S5," any shorthand referencing this skill's own
section numbers. The second, just as real and easier to miss, is jargon
carried in from whatever source material this skill's rules were built
from — the account's own decision frameworks and SOPs use their own
dense internal codes ("ETT," "S-C1," and dozens like them), and pulling
a rule's *substance* from that source does not license pulling its
*labels* along with it. Neither source's shorthand means anything to a
reader who hasn't read that document, and a reviewer of the actual plan
never has.
**These never appear in delivered reasoning text, in any form — not
bare, and not in parentheses as a citation either.** An earlier version
of this rule permitted the label in parentheses "as a receipt, for
cross-referencing" — that was still wrong: a citation a reader can't
decode is not a receipt, it's opaque jargon, and putting it in
parentheses instead of stating it bare doesn't fix that. "State E, held"
tells a reviewer nothing evaluable. "§5 correction, 25% step" is the same
failure with a different symbol. **The mechanism the label refers to is
written out in plain language every time, with nothing left standing in
for it.** "Rank has collapsed 13 positions despite full delivery — never
read as an under-sized push, so held flat and escalated for a
listing/competitor check" states the actual decision and lets a reviewer
judge it, with no label anywhere in the sentence. That is the only form
this ever takes in a delivered plan. **A raw platform identifier is the same failure in a
different shape, and gets the same treatment.** A portfolio ID, campaign
ID, or any other bare internal number is exactly as opaque to a reviewer
as a framework code -- "Portfolio 119993222153930" tells a reader nothing
they can evaluate any more than a bare framework label does, and it
happened on a real plan: five raw portfolio IDs sat in delivered text
until a check caught them. Resolve every platform ID to the name it
refers to before it reaches delivered text -- the portfolio's name, the
campaign's own name -- never the bare number. ASINs and SKUs are the
stated exception, since the account reads those fluently and they are
themselves the identifying label, not a stand-in for one. Cross-reference this skill's own
sections freely while reasoning about *how to build* a row — that
scaffolding is this document talking to itself — but strip every one of
those references out before anything is written into the plan a reviewer
will actually read.

**Never:**

- A verdict with no arithmetic behind it.
- Blended figures where a delivering-placement figure exists.
- Treating an estimate (Target Sales, Target Clicks, Required Budget) as
  a gate rather than a direction-setter.
- Pausing a converting row for thin clicks — restated here because it's
  the most common single violation of this chain.
- A bid on a paused row, a withheld duplicate instance, or a SKU below its
  inventory gate (§9).
- A family-scoped action ("all King campaigns") — every row is decided on
  its own situation.
- More than one lever changed per row per cycle, except §4's PDP
  re-solve. **This restricts one entity instance — this specific keyword's
  bid, this specific placement's modifier, this specific campaign's
  budget — not the campaign as a whole.** A campaign's many rows can and
  should each carry their own lever change in the same cycle: a keyword's
  bid, a different keyword's placement modifier, and the campaign's
  budget can all move simultaneously if each has earned its own change
  from its own data. What's prohibited is stacking two levers onto one
  row (raising a single keyword's bid and changing its match type in the
  same pass), not limiting a whole campaign to one type of action per
  cycle.
- **Negating a term that is otherwise relevant to the product** — the
  relevance check precedes every negative decision. A relevant term that
  isn't converting routes to a fix queue (listing, bid, or placement
  correction), never straight to a negative; only genuinely off-target
  traffic (competitor brands, foreign ASIN codes, other categories) is
  ever walled off outright.

**An auto or catch-all campaign matching the product's own ASIN is
structurally off-target and is negated on sight.** It appears in the
search-term report as the ASIN itself, and it means the product is
paying to place an ad on its own listing, where the shopper has already
arrived. On a real build this was the single largest wasted term on the
product: 545 clicks and $184.95 across four campaigns for zero orders,
and it had gone unnoticed because an ASIN string does not read like a
search term. Scan the search-term report for the product's own parent
and child ASINs specifically — no click or spend threshold applies,
because there is no volume at which paying for one's own detail page
becomes correct.
- **Negating anything beyond a structurally off-target term without that
  specific term's own spend, click, and order history cited** — a
  category sweep applied on relevance alone. A competitor brand name or a
  foreign ASIN fragment is negated on relevance alone; no click or order
  count would make it the right call to keep. Everything else — a term
  plausibly off-topic but not structurally disqualified — needs *that
  specific occurrence's* own spend, clicks, and zero-order count named,
  not the root's general reputation applied to every row matching it. Two
  rows matching the same root can carry different histories on different
  campaigns; a blanket sweep will occasionally wall off a row that was
  actually converting.
- **State which of three modes a negation decision is, sourced from the
  account's own framework** — pre-load (loaded at launch, before spend
  accumulates, and including an own-catalog scan before the list is
  finalized — a term negated for this product can still be a real,
  sellable term for a sibling or a different brand this account
  carries), reactive (added after a search-term report shows a
  specific off-target occurrence), or steering (added to redirect traffic
  toward a preferred instance, the isolation-wall pattern). The evidence
  standard differs by mode; the plan names which one governs a given
  negation decision rather than leaving it to be inferred. **The actual
  scan runs in the workbook, where the cut is made — the plan states
  that it happened, not just that it should.**

---

## 13A. Review triggers — what a reviewer is told, and where

**No approval, confirmation or sign-off field exists in any delivered
document.** The triggers below fire the same way; what changes is where
the result is written. **They are reported in the handoff message that
accompanies the document, keyed to the rows or sections they apply to —
never inside it.**

A row is reported for review when it carries: an action on a 250+ SV
keyword; any gate failure; any structural change; a bid move greater
than 25% of current value; a budget move greater than $50/day.

**Reporting a row does not withhold it.** The row is decided, carries
its full reasoning, and is ready to deploy — the report marks it for
attention, not for completion.

**Every reported row states its trade-off in the reviewer's own units,
not just that a threshold fired** — "holds ~$180/wk of saving to keep
~66 orders/wk at $5.60 per order," not "bid move >25%." A reviewer
should be able to rule from the report without opening the document to
reconstruct the trade-off from raw numbers.
---

## 13B. Validation gate — zero failures before shipping either document

**Four checks added after an external reviewer found, in a plan whose
gate had returned clean, seven figures stated at conflicting scopes, a
section that deferred its own analysis, four paragraphs styled as
headings, and draft history in delivered text. The gate returning
clean is not evidence the document is clean if the gate did not run in
full.**

### 13B-0. The section check map — which checks are run against which section, and when

The checks below this map are a flat list of about fifty items run
against a finished document. That is where they fail: a defect written
into §2 is found, if at all, after §9 is drafted, and the reader
running the gate has no way to know which of the fifty bear on the
section actually in front of them. On a real build the gate returned
clean twice while a superseded margin figure survived downstream of the
correction that replaced it, a rank claim contradicted a rank table
eight sections away, and a required section had never been written at
all.

**Run the checks in the map's own rows as each section is completed,
and the full list once at the end.** The map is not a substitute for
the full pass — it is what stops a defect travelling eight sections
before anything looks for it.

| Document section | Checks run as the section is completed |
|---|---|
| **1. Product story** | 0-B scope labels on every figure · 0-E derived figures recomputed · every figure carries its measurement window (I-3) · rank stated at all three cadences where available · a metric named in one system is not restated as a different metric (0-W) |
| **2. What we did** | 0-B · 0-E · long-window comparison actually reached the narrative (I-4) · advertised-SKU provenance stated (§11) · own-catalogue terms checked (§12) |
| **2A. Earning potential** | 0-B · 0-M one threshold one value · spend envelope traces to a stated revenue base · posture record has every dimension populated or marked as a named gap |
| **2B. Recovered value** | 0-E every figure downstream of contribution recomputed · 0-H stated counts match · no action priced past what its sample supports · parallel-decision-system reconciliation stated |
| **3. Diagnosis** | persistence tested against the longest series available, not the current week (§1B) · 0-N exhaustive-list mapping on the quadrant set · sample-size caution stated on any syntax below the floor · spend-by-quadrant visual present |
| **4. Per-keyword mathematics** | 0-G correction-sizing cap on every bid and budget move · 0-K every gate run on its full population · 0-L each check names the property it tests · five-property gate stated property by property, met or not · 0-V caps belong to their own lever · placement table is per campaign per placement with the modifier on each · bid re-solve shown as arithmetic with the staged step · budget subsection carries budgets, not bids |
| **5. Coverage** | 0-K on the negation population · 0-N on the ad-type list · every ad type present in the source data appears in the table, including those returning zero · declines named individually, not summarised |
| **6. Competitor position** | 0-B on every competitor figure · set dated · our own row present in every comparison table · gaps routed to Brand Management, not written as advertising levers |
| **7 / 7A. Oversight and contingencies** | every checkpoint carries a date or a named trigger · every contingency names the signal that fires it · settle-window collisions named and ruled |
| **8. Execution register** | 0-Q values confirmed present · 0-R writes verified by reading back · 0-H counts match the source · every enabled entity listed, not only the delivering ones |
| **9. Reconciliation** | 0-A count stated in the handoff · 0-C no deferred analysis · every gap carries an owner · every verdict carries its reversal condition · decisions numbered and specific |
| **Whole document, once at the end** | **This file read end to end before the pass began** · **every derived value checked against a supplied source first** · **no input called redundant without being opened** · **every decided row confirmed able to deploy** · **every action naming its entity and field** · **the reconciliation table generated from the workbook, never typed** · **programme sections generated after the freeze, never authored ahead of it** · **every release-versus-commitment comparison re-derived** · **the programme total stated against an approved envelope** · **the checking tool verified to read the file it was given** · **every entity's row count set against its verdict count** · **every named plan decision traced into this file** · the full list, 0-A through 0-Y and 1 through 27, without exception · **every rule applied checked against every entity type the pass touched** · every data table carries a source-and-window line, dated, one format · every held, paused or blocked verdict swept against the declared goal, with the sweep stated · **the stale-string list run mechanically against the rendered file, output attached** · **every decision-bearing column checked against the decision register, by column not by reading** · reverse-scope campaign sweep stated · price stability across the window stated · **every declared gap searched for in the supplied files first** · **every verdict names the window it rests on** · **every multi-context rule applied checked against each context it names, not just the one in front of you** · **the sections read in full named in the hand-off** |

**Three checks are new, added because the map made their absence
visible:**

**0-W. A metric is never restated as a different metric.** Two
measurements with similar names are two measurements. On a real build
a competitive-visibility share — share of a tracked competitor set,
which reads zero when nothing places in the top ten — was written into
a plan as the product having no organic rank at all, while the daily
rank export for the same week carried 731 keyword-days at real ranks
between 18 and 144 across fifteen child ASINs. Both figures were
correct; the claim built from them was not. **Where two sources appear
to measure the same thing, state what each actually measures before
either is used, and if they disagree, that disagreement is a finding
rather than an error to resolve by picking one.**

**0-X. Every required section exists.** The skeleton is checked against
the document as a list of section numbers before the gate runs. On a
real build two required sections were skipped in the writing order and
their absence surfaced only when someone counted. A missing section
cannot fail any other check, which is precisely why it needs its own.

**0-Y. No cell in a delivered table is empty or holds a bare
placeholder.** A dash, an em-dash, "N/A" or "TBD" sitting in a table
cell tells the reader nothing about whether the figure is genuinely
undefined, not yet computed, or simply missed. Each of those is a
different fact and each has its own honest wording: a rate with a zero
denominator is **undefined**, and the reason sits beside it; a figure
not computed this cycle is a **named gap with an owner**; a value that
does not apply to that row says so in words. On a real build a plan
shipped with eight bare em-dashes in a performance table, every one of
them a cost-of-sale on a row with no orders — genuinely undefined, and
invisibly so. **Scan every table cell before delivery; the count of
empty and placeholder cells is zero, not low.**

**0-A. State the count. "27 of 27 run" appears on the delivered
document.** On the build above, ten of twenty-seven ran and the
document shipped; nothing in the process required stating that. A gate
whose completion is never asserted is a gate that can be silently
skipped. If the count is below full, the document is not ready — say
which did not run and why, rather than shipping and hoping.

**Where this meets 0-P, 0-P wins, and the count moves rather than
disappears.** 0-P bans anything in a delivered file describing the
build's own process, which a stated check count plainly is. Both rules
were in force and pointed opposite ways, and that ambiguity got
resolved silently, and differently, on more than one real build. **The
count is stated in full in the handoff message that accompanies the
deliverable, never inside it, and 0-A is satisfied there.** A build
stating no count anywhere still fails 0-A; a build stating it inside
the delivered file fails 0-P. Both survive; only the location is fixed.

**0-B. Every stated figure carries its scope label, and the same
figure never appears at two values unlabelled.** All seven
reconciliation defects found by that reviewer were one shape: a real
number measured at one scope, restated elsewhere at another, with
neither labelled. Weekly spend appeared as two values, a placement
leak as four, one campaign's cost of sale as three — each defensible
alone, none reconcilable together. **Scan for any figure appearing
more than once at different values; each instance either carries its
scope or the discrepancy is resolved.** This is the account's own
rejection trigger and it overrides how good the surrounding analysis
is.

**0-C. No section may say its own analysis "can be" or "will be"
computed.** Either it is computed, or it is a named gap with an owner
and a date. On that build, the cross-comparison section stated the
data was present in the file already supplied and then deferred —
which is the single item the account's reviewer names by name in his
standing feedback. "Can and will be computed" is neither an answer nor
an honest gap.

**0-D. No heading exceeds roughly 200 characters.** Paragraphs
inserted programmatically inherit the style of whatever they were
copied from, and a body paragraph carrying a heading style renders as
a page-wide heading. Four did on that build, one of them 1,055
characters. A length check catches it instantly and no reader should
have to.

0-E. **Derived figures must be recomputed when their source changes,
    and every headline figure must trace to a table in this document.**
    Three of the four residuals an external reviewer found after a
    clean gate were this one defect: a source number was corrected, and
    the figures derived from it were not. A weekly total survived as
    the stale daily rate times seven; a recovery figure appeared in two
    places at two values; a negation figure traced to no table at all.
    **Check 0-B catches the same figure stated twice. It does not catch
    a figure that is arithmetically downstream of one that moved.**
    Build the dependency list once — which headline numbers are derived
    from which — and after any correction, recompute every dependent
    and confirm it still ties. A headline figure that cannot be traced
    to a table in this document is a failure regardless of whether it
    appears once or twice.

0-F. **No dangling connective after an edit.** When content is removed,
    the words joining it to what remains survive and point at nothing.
    On a real build, deleting one of two withdrawn findings left a
    paragraph opening "was also wrong" and closing "Both are kept
    here," with only one finding present. Scan for "also," "both,"
    "the former," "the latter," "as above," "the second of these" and
    confirm each still has its referent. This is the one-final-draft
    rule failing in a way no reader can miss.

0-G. **Every action complies with the correction-sizing cap, or states
    why not.** The cap exists in this file and is applied in some rows
    and not others — on a real build, one action took a 40% single-step
    bid cut against a 25% cap, while another in the same document was
    correctly staged in two dated steps for the same reason. **A rule
    applied inconsistently is worse than a rule not stated**, because
    the inconsistency reads as a judgment nobody made. Check every bid
    or budget move against the cap; stage it, or name the exception.

**0-K. Every gate is applied to every row it governs, not only where it
was first noticed.** A gate written once and applied to the row that
prompted it, while other rows it equally governs go unchecked, produces
a document where two rows in the same condition got different verdicts and
nobody decided that. On a real build the indexing gate ran on the single
row where it was first spotted and not on the rest; applying it across
every launch row moved a keyword out that had otherwise passed. **The
build caught that by noticing, not because a check required it** — which
means the next one might not.

**This is distinct from 0-G**, which covers the correction-sizing cap on
bid and budget moves specifically. 0-K is the general form: for each
gate this plan applies — indexing, inventory zone, provenance, sample
size, relevancy floor, duplicate ownership — confirm it ran against the
full population it governs, and state the population it was tested on.
A gate whose stated scope is "every launch row" and whose actual scope
was "the rows I was looking at when I wrote it" is the same defect as a
threshold applied to one campaign and not its twin.

**Where a gate or a correction is applied by matching a pattern, the
pattern's own coverage is verified before its result is trusted.** This
is the same failure one level down: the gate ran, but only against the
rows its pattern happened to catch, and the count it reported was the
count of what it found rather than the count of what exists. On a real
build a repair for unlabelled number fragments matched only the
fragments following one particular word, reported and fixed 53, and
left 75 more of the identical defect standing behind a different lead-in
— then reported the file clean. **Count the defect class by a means
independent of the pattern doing the fixing, before and after.** A
broader, deliberately over-inclusive scan, a count of the underlying
condition rather than its surface form, or a manual read of a sample —
any of them establishes what the population actually is. A fix whose
population was defined by its own search string has not been shown to
have run against the full population it governs, whatever the gate says
afterwards.

**0-L. Every check states which property it tests, and "present" is
never sufficient on its own.** This is the most-repeated failure across
this plan's real use: four separate defects passed a check that was
looking at the wrong property. The reversal-condition check confirmed
every row carried text — it did, but one string was repeated across 132
rows, so nothing could be diffed. The metric-label rule said standard
names were *permitted*, which a document written entirely in paraphrase
passes cleanly. A cell was cleared with a call that silently did
nothing and reported success. A cell was filled with the literal string
"None", which reads back as empty.

**Each of the four properties below is separate, and a check asserting
one does not establish the others:**
- **Present** — a value exists in the cell
- **Unique** — it is specific to this row, not repeated across many
- **Correct** — it holds the right value, on the right scale, in the
  right units
- **Written** — the write actually landed, verified by reading the cell
  back rather than trusting the call's return

**Every gate item names which of the four it asserts.** Where a
requirement is really about substance — reasoning, reversal conditions,
routing notes, gate columns — the check tests uniqueness or correctness,
not existence. **A check that can be satisfied by a placeholder is not
testing the thing the rule exists to protect.**

**A fifth property, and the one that most often makes a clean gate
meaningless: the check has been shown capable of failing.** The four
above describe what a check asserts about the file. This one describes
the check itself. A check whose pattern matches nothing returns zero,
and a zero from a broken check is indistinguishable on the page from a
zero from a clean file. On a real run a bid-transition check matched a
price increase and a deal-state margin instead of any bid; a check for
a withdrawn action funding the arithmetic fired on the sentence that
withheld it; a check for stale values scanned a reference table that
legitimately carries every child's own figures. Each returned a number
that was read as a result.

**Before a check's zero is recorded, run it against a known-bad
instance and confirm it fires.** Build the failing case from the defect
the check exists to catch — the actual prior defect where one is known
— and confirm the check reports it.
**Build the failing case by reintroducing the defect into the data, never
by adjusting what the check reads.** A known-bad that edits the field the
check inspects makes the check agree with itself and proves nothing; a
known-bad drawn from a case that does not actually violate the rule
passes for the same reason. Both happened on a real run — one test set
the very source field being validated, another paused an ad on a
campaign that had others available, and both returned zero and were
briefly read as evidence. Reintroduce the original defect — the stale
value, the missing row, the wrong child — and confirm the check names it. A check that cannot be made to fail
has not been shown to test anything, and its zero is not evidence.

**A check iterates the population it protects, not the survivors of the
operation it is checking.** Anything the change removes entirely drops
out of the filtered set, so a check that walks what remains will never
examine the case it exists for. On a real build a check asking whether
any campaign was left with nothing to advertise walked the surviving ad
rows — and a campaign stripped of every ad had no surviving rows, so it
was silently skipped. The check passed twice on a file that contained
the exact defect. Enumerate every campaign, row or entity in scope and
ask each one directly, including the ones the operation emptied.
State alongside the count that each check was exercised this way.

**When the known-bad case does not make the check fire, the check is
what gets rewritten — never the known-bad case.** The temptation runs
the other way, because a check that stays silent looks correct and the
failing example looks unrepresentative. On a real run a staging check
returned zero against a deliberately gutted row because its own filter
excluded anything short; loosening the example would have hidden that,
while rewriting the filter to test what the text *is* rather than how
long it is exposed a real defect the same pass. A known-bad case that
has to be adjusted to make a check fire is evidence about the check.

**0-M. The same threshold or rule never appears at two values.** A
number stated in more than one place gets changed in all of them or in
none. On a real build the human-confirm trigger read 500 search volume
while oversight tiering, launch eligibility and the writing standard all
read 250 — one was lowered and the rest were not, leaving a term that
earned full analysis at 250 but needed sign-off only at 500. The same
thing happened to the routing rule, where an old and a new version sat
in the file saying opposite things.

Scan for any threshold, floor, cap or percentage stated more than once
and confirm every instance agrees. Where two genuinely differ for a
stated reason, say the reason at both sites, not one.

**0-N. Where a list is declared exhaustive, every use maps to it.**
Several rules here say a list is complete — the mechanical hold reasons,
the four duplicate-coexistence reasons, the negation modes. Declaring a
list closed does nothing on its own: on a real build 171 rows carried a
hold reason that appears nowhere on the exhaustive list, and nothing
caught it until a reviewer asked.

For each closed list, check every row invoking it against the list
itself. **Anything that does not map is not a silent verdict — it
becomes a question**, and the row says which list it failed to match.

**0-O. A row's reasoning is distinguishable by facts bearing on its own
decision, not by an incidental clause.** Uniqueness alone is not enough:
on a real build, 82 rows read as unique while differing only by a
boilerplate sentence about a field that had nothing to do with the
verdict. When that clause was removed for an unrelated reason, all 82
collapsed into shared strings — which means they had never been
genuinely row-specific, and a uniqueness check had passed them anyway.

**The test: if a single clause were struck from every row in the document,
would the remaining text still tell them apart?** If not, the
differentiation is decorative. What distinguishes a row must be what
drove its verdict — its own search volume, click and order counts, its
routed SKU's economics, its placement mix, its inventory position — not
a shared observation that happens to appear in each cell.

This is the layer beneath 0-L's uniqueness test, and it fails
differently: 0-L catches copies, 0-O catches rows that differ without
differing *about anything*.

**0-P. Nothing in a delivered document reveals how it was produced.** No
column, header, note or cell names a review step, a confirmation state,
an approval status, or anything describing the build's own process
rather than the account's work. A sign-off flag belongs in the handoff
message to the person reviewing, never as a field in the document — a
reader opening the document sees advertising decisions and their
evidence, not the machinery that produced them. This extends the
existing bans on self-reference and version history to *structural*
leakage: a column can disclose process even when every word inside it
is clean.

**0-Q. Every value a row's Action names is confirmed present where it
actually lives — including on another row.** Every other check in this
gate reads a row against itself, which is why the defect below survived
a clean pass: six keyword rows carried an Action stating a
top-of-search modifier had been re-solved, and the modifier lives on a
bidding-adjustment row joined by campaign ID. Three of them deployed at
$3.06 against a $2.85 ceiling while their Action text said otherwise.

**A row's Action is a claim about the file, not about itself.** Where it
names a bid, a modifier, a budget, a routed SKU or a state, confirm that
value is written wherever it belongs — the placement row, the campaign
row, the product-ad row — not only in the cell the Action sits beside. A
keyword's stated modifier is checked against the placement row carrying
it. A base bid is checked against every placement ceiling it has to
satisfy, not only the one it was solved from.

**This is check 17 extended across the join.** 17 catches an Action and
Reasoning that disagree within a row; 0-Q catches an Action that
disagrees with the row it actually acts on.

**0-R. Every write to a decision column is verified by reading the cell
back.** A call returning without error is not evidence the value landed.
This has failed three separate times on real builds: a clear performed
with a call that silently did nothing and reported success; a cell
filled with the literal string "None", which reads back as empty; and
six modifiers computed correctly, described accurately in the Action
text, and never written at all.

**In each case the decision was right and the file was wrong.** 0-L
already names "written" as one of the four properties a check can
assert; this makes it a required step rather than a definition. After
any pass that writes or clears decision columns, read them back and
confirm the count and the values match what the pass intended — and
report both numbers, not just the intent.

**0-S. A paragraph, row or cell inserted programmatically has its style
set explicitly, never inherited from whatever it was copied from.** This
is the cause behind 0-D rather than another symptom of it, and it has
now produced the same defect twice: four chart captions and a
1,055-character body paragraph rendering as headings on one build, then
a 1,319-character and a 2,174-character paragraph on the next. Both
times the insert worked by copying a nearby paragraph to get a valid
element, and both times the copy brought a heading style with it.

**Copying an existing element is a reasonable way to insert one; keeping
its formatting is not.** After any programmatic insert, set the style,
size, weight and colour explicitly on the new element — do not assume
the default, and do not assume the source's formatting was appropriate
for what is replacing it. **0-D catches this after the fact; this
prevents it.** Where both are in force, 0-D becomes a backstop rather
than the only thing standing between an inserted paragraph and a
page-wide heading.

**0-T. A campaign's own verdict must be supported by the rows it acts
on.** 0-Q checks that a value a row names exists elsewhere; it does not
check that a campaign-level *verdict* is consistent with the verdicts of
the rows beneath it. That gap shipped a campaign carrying ENABLE, whose
stated reason was that "a term it holds cleared the release test," while
all 200 of its keyword rows read OUT OF SCOPE, WITHHELD or NO ACTION and
not one carried a reactivation. Deploying it would have switched on 200
broad keywords the declared goal excludes — more search volume than
everything else in the file combined, on exactly the terms held.

**Before any campaign carries an enabling verdict, confirm at least one
row beneath it carries a matching acting verdict.** A campaign enabled
"so the term it holds can serve" must hold a row that is actually
serving. Where none does, the campaign's verdict is wrong, not its
rows'. **And check the reverse**: a campaign held while rows beneath it
carry acting verdicts is the same defect from the other side.

**This also catches a layer breach that no per-row check can see.** Each
of those 200 rows was individually correct — a broad term correctly
marked out of scope. The breach existed only at campaign level, where
one row would have enabled all of them. **A layer the plan holds cannot
be re-opened by a campaign row**, and that is checked at the campaign,
not by reading its members.

**Both terms are read off state, never off the wording of a verdict.**
A campaign is held when its own state cell reads paused, and a row is
acting when its verdict requires the campaign to be serving for that
verdict to take effect — a reactivation, a price correction on a live
row, a placement re-solve. A verdict that reduces or stops delivery — a
pause, a retirement, a negative loaded into other campaigns — is not an
acting verdict here, and a live campaign whose verdict happens to read
"no action" is not held. Reading either off the action text produces
false failures on campaigns running normally and, far worse, passes the
exact case this check exists for: a campaign carrying an enabling
verdict whose only acting row is a negative that takes effect
elsewhere.

**0-U. A written value must match the value its Action names, not
merely exist.** 0-R confirms a write landed; it does not compare the
landed value against what the Action claims. Seven rows stated "bid
$1.60 to $1.02" and wrote $1.20 — the correction cap applied to the
number while the text kept the uncapped figure. The placement modifiers
were then solved from $1.20 and landed above ceiling, with the Action
asserting they landed below it.

**Parse the value out of the Action text and compare it to the cell.**
Where a cap or a floor changes what can actually be written, the Action
is rewritten to the value that lands — never left stating the
pre-capped figure. A row whose text and cell disagree is wrong whichever
one is right, because a reviewer cannot tell which was intended.

**0-V. A cap belongs to the lever it was written for.** The 25%
correction cap is a bid cap. It was applied to budget on four truncated
campaigns, stepping a $1.00 daily budget to $1.25 — which fixes nothing
on a campaign delivering a third of its day, and contradicts the lever
hierarchy's own rule that budget clears first precisely because
truncated data contaminates every rate measured on it. **Before
applying any threshold, confirm it was written for that lever.** Budget
truncation is cleared by setting budget to what the campaign needs, or
the freeze is stated and the bid and placement verdicts on those
campaigns are deferred too — not both at once.

0-H. **Stated counts match what is actually there.** An action register
    header saying fourteen actions above fifteen rows is a defect a
    reviewer finds in seconds and it costs the document credibility on
    everything else. Count the rows, count the sections, count the
    checks, and confirm each stated total.

0-I. **No sentence addressed to a previous draft's reviewer.** A
    document is read cold by someone who never saw the prior version.
    "Computed, not deferred," "the comparison Erik asks for runs here,"
    "as previously requested" — each of these answers a question the
    reader never asked and exposes a seam. Related to the checks
    against self-reference and version history, but distinct: this one
    leaks the *review conversation* rather than the build's own history.

0-J. **The validation row is written last, and only if the gate
    actually passed.** On a real build the document asserted a clean
    pass — "three failures found and fixed, twelve figures re-derived"
    — while four figure mismatches remained that the gate's own checks
    would have caught. **This is the account's standing rule failing at
    the exact point it matters most: an output must never report work
    as complete that is not.** Write the row after the final pass
    returns clean, never before, and never as a description of an
    earlier pass. If the gate does not return clean, the row says what
    failed and what remains open — which is a more useful document than
    one claiming a pass it did not earn.

**This runs as its own discrete pass over the completed document — not
a running mental check kept in mind while building, and not assumed
satisfied because each rule was followed correctly in the moment it
applied.** Stated explicitly because of exactly the risk a long build
creates: a rule stated once, thousands of lines earlier, followed
correctly on the first section, can genuinely drift by the twentieth
without anyone having decided to abandon it — attention doesn't hold a
rulebook this size in working memory across a real build the way it can
be checked mechanically after the fact. Build the complete document
first. Then run every check below against the finished document, one at
a time, exactly as if reviewing someone else's work — not as a summary
of what was believed to be true while building it.

Run and state the result; each check must return zero:

1. Campaign blocks holding more than one objective.
2. Actioned rows without a reasoning statement meeting §13.
3. Converting rows parked by the sample gate.
4. A live term with more than one instance carrying a bid.
5. A non-ranking row's bid or effective price above its ceiling with no
   inventory or provenance exception applying.
6. A Ranking row bid above ceiling that hasn't cleared §6's product-goal
   gate, or has already crossed §7's sufficiency stop without
   transitioning to standard ceiling judgment.
7. Bids written on a non-live row.
8. A budget-infeasible plan not escalated per §4A.
9. A rank-collapsing row (State E) given a bid increase.
10. An at-plan row (State F) labelled a failure rather than too-early-to-
    read.
11. An OUT OF SCOPE row given a ranking verdict the data can't support.
12. Contradictory directions on the same term across campaigns.
13. Arithmetic mismatches between a stated figure and its recomputation.
14. A discovery-layer term priced (§12) without having cleared the
    100-click candidacy gate.
15. A performance verdict computed without a SKU-provenance check (§11)
    on the window it draws from.
16. **Reasoning text duplicated verbatim, or differing only by the row's
    own identifying value — keyword text, campaign name, or placement —
    across two or more rows of the same entity type.** Run a plain string
    comparison of every reasoning statement against every other reasoning
    statement of the same entity (keyword against keyword, placement
    against placement, campaign/budget against campaign/budget); this is
    the copy-paste test from §13, made checkable rather than left to feel.
17. **Action and Reasoning disagree on a row** — the arithmetic or
    mechanism stated in the reasoning doesn't actually point to the
    action taken. Re-derive the arithmetic independently from the row's
    own data and confirm it lands on the same number the action states.
17A. **A reasoning cell uses real, specific numbers but a reviewer
    couldn't follow the logic from them to the verdict without asking a
    follow-up question.** This is a different failure from #17 above —
    the arithmetic can be internally correct and still fail this check if
    it's listed rather than connected. Read the cell as a first-time
    reviewer would, cold: can you state what changed, why this row's own
    metrics justify it, and what would reverse it, using only what's
    written? If not, it fails even though nothing in it is false.
18. A campaign roster whose combined minimum budget floor exceeds the
    available cap, proposed without a stated pacing plan (e.g. releasing
    3–5 campaigns a week inside the cap, highest-value first, rather than
    launching all at once against a budget that can't support it).
19. An explicit user override from a prior round silently reverted by a
    later regeneration or resync pass — once a specific instruction
    overrides a default for a product, it holds for every subsequent edit
    to that document, not just the round it was given in; track active
    overrides somewhere durable and check new content against them.
    **The same check applies to a returned Change Review Sheet's marks**
    (Step 0) — a reviewer's reject or modify on a specific decision is
    checked against the current draft the same way an explicit override
    is; a plan that silently recomputed a rejected decision back to its
    original value fails this check exactly as if a user override had
    been reverted.
20. **A mechanism-level change rolled out across many campaigns with no
    control arm.** A per-keyword bid correction needs none — it's judged
    against its own before/after. But when the bidding *mechanism* itself
    changes (a placement re-solve, a strategy switch) and it's applied at
    scale, some campaigns should be deliberately held unchanged so the
    change's own causal effect is measurable against a control, not
    inferred from the whole treated set moving together.
21. **A batch of cuts not cross-validated for opportunity cost before
    shipping.** After sizing a batch of cuts, re-test each one: does the
    projected lost-order value exceed the projected spend saved, even at
    the more conservative (deal-state) margin? Withdraw any cut that fails
    this test before it ships — this is a check run once the batch exists,
    not a substitute for the per-row ceiling logic above.
22. **A projection built on an unnamed soft coefficient.** Any numeric
    assumption baked into a forward projection — an uplift multiplier, a
    click-elasticity estimate — that isn't a settled rule but a modelled
    input specific to this projection is named explicitly as soft, tied to
    when and how it will be measured, not silently absorbed into a
    headline projected number as if it carried the same confidence as the
    rules above.
23. **A skill-internal or source-document citation leaked into delivered
    text.** Scan the plan for a `§` symbol, or shorthand like "S5," "S8,"
    "State E," "the sufficiency stop," "PROVEN tier," "S-C1," "ETT,"
    "O3," "S-M1" or any S-prefixed rule code, or any other code, acronym,
    or internal taxonomy — whether it's this skill's own or carried in
    from an account SOP or decision framework this skill's rules were
    built from. Any match is a failure, full stop — this is checked as a
    plain text search, not a judgment call, and it is never satisfied by
    moving the reference into parentheses
    instead of removing it, or by the label having a real, authoritative
    source document behind it. A reader still can't decode it, and
    that's the only thing this check is protecting.
23-A. **Standard platform metrics are REQUIRED, not merely permitted —
    the paraphrase is the defect, and this check scans for the
    paraphrase, not for the label.** An earlier form of this rule said
    these metrics "are allowed and must not be converted." That is a
    permission, and a permission catches nothing: a document written
    with the long form from the start passes it cleanly, which is
    exactly what happened on a real build — twenty paraphrases shipped
    through a validation pass that returned clean.

    **Scan for these strings and replace each with its standard label:**
    "cost of sales" / "cost of sale" → **ACoS** · "cost per order" /
    "conversion cost" → **CPA** · "conversion rate" → **CVR** · "cost
    per click" → **CPC** · "click-through rate" → **CTR** · "cost of
    total sales" / "total advertising cost of sales" → **TACoS**. Also
    allowed and never paraphrased: ROAS, SV, impression share,
    top-of-search, ROI.

    **The one exception is genuine descriptive prose, not a metric
    label** — "a high cost of sales made largely of one campaign"
    describes a cost, it does not report a metric. Judge by whether a
    number follows or the phrase names a measured quantity.

    **The line this check draws:** does decoding the term require
    having read a specific internal document? If yes, it is banned. If
    it is vocabulary shared across the whole advertising field, it is
    required in its standard form. **CM2 falls on the banned side** —
    despite looking like a standard metric it is an internal accounting
    label, and is written as contribution margin in delivered text. So
    does anything naming a framework, a rule code, a state letter, a
    named gate, or a confidence tier.
23A. **Self-referential language about the skill itself, leaked the same
    way coded jargon leaks — a distinct failure from #23, since these
    are plain English words, not codes, and would slip past a search for
    acronyms alone.** Scan for "this skill," "not derived by this
    skill," "" "this skill's own," "not supplied by
    this skill," or any other phrasing that talks about an AI skill or
    tool as an entity within the delivered document. Erik, a reviewer,
    or Brand Management reading this plan has no reason to know or care
    that an AI skill exists behind it — the plan states findings, gaps,
    and decisions directly, in the plan's own voice, never in terms of
    what a skill does or doesn't do. Where a gap exists because a
    formula or threshold is the account's own and isn't restated here,
    the delivered plan states that plainly ("this arbitration mechanic
    is the account's own convention" or simply names the gap) without
    ever surfacing the word "skill." **This is a real risk, not a
    hypothetical one** — this build's own explanatory language uses
    "this skill" constantly when talking to the person building the
    plan, and that habit can bleed into the delivered document itself if
    a passage is drafted too close to how this skill describes its own
    reasoning rather than rewritten in the plan's own voice.
23B. **The skill's own version or revision history, leaked into the
    delivered document — a distinct failure from #23A, since this isn't
    about the word "skill" appearing at all.** Scan for phrasing like
    "," "this was
    unestablished in an earlier version," "v4," "v5," or any other
    reference comparing what this skill's own build produces now
    against what an earlier version of this skill produced. **This
    skill's own internal documentation legitimately uses language like
    this constantly — it's how a correction gets recorded honestly
    inside the skill file itself — and that is exactly the risk: the
    habit of writing that way can bleed into an actual delivered plan
    if a passage is drafted too close to this skill's own internal
    voice.** The plan's own version number (v1.2, v1.3) in its title
    block is not this — a document stating its own version is normal,
    expected front matter, and stays. What's banned is narrating that
    version *against* a prior one, or referencing this skill's own
    build history at all — the plan reads as a finished, standalone
    document each time, never as a diff against what an earlier
    version of this tool used to produce.
24. **A HOLD verdict whose stated reason isn't one of §4A's named,
    mechanical list, with no record that the human was asked first.**
    Scan every held row and check its stated reason against the
    exhaustive list — both quality gates failing, CTR-passing-CVR-
    failing, zero delivery, budget truncation, or a plan exceeding
    structural delivery. Any hold citing something outside that list — a
    vague "monitoring," an unprofitability finding with no clean next
    step, a syntax diagnosis with no action attached — is a failure
    unless the row also shows the question that was asked and the answer
    received. A hold that reads as reasonable in isolation still fails
    this check if it bypassed asking when asking was the actual rule.
25. **Any Provisional-tier rule driving a real verdict for the first time
    on a product, with no record it was confirmed first.** This is the
    same check as the one above, generalized past HOLD: the product-goal
    gate, the Defensive/Conquest rules, the harvest mechanic, the
    discovery cluster-vs-keyword count, the sufficiency-stop exit
    mechanics, and the graded push-sizing tiers are all tagged
    Provisional or New in this skill, and each one is supposed to be
    asked about before it first drives a real decision on a product, not
    applied with a flag. A plan where one of these fired for the first
    time with no recorded question fails this check, even if the outcome
    it produced looks defensible — the failure is in how it was decided,
    not necessarily in what was decided. Once a rule has been confirmed
    for a product, later cycles applying that same confirmed answer pass
    this check without needing to ask again.
26. **An internal section reference that doesn't actually resolve to a
    real section in this document — added after a
    real instance of exactly this bug was found and fixed.** This skill
    exists as a deliberately duplicated pair with its workbook
    counterpart, and the two files use different section numbers for
    analogous content by design — the writing standard sits at a
    different number in each, and other sections diverge the same way.
    That design is fine; what it invites is content being adapted from
    one file to the other with the source file's own section numbers
    still attached, unchecked against where those numbers actually land
    in the destination file. Before anything is finalized, every `§`
    reference in this document is checked against this document's own
    table of contents — not assumed correct because it was correct in
    whichever file the content was drafted from or ported out of. A
    reference that fails this check is a defect regardless of how minor
    it looks; a wrong pointer sends a reader to the wrong rule with full
    confidence it's the right one.
27. **A headline figure in this plan that disagrees with the companion
    workbook for the same product, with no reconciliation recorded — new
    to this skill, closing a real gap: the workbook already checks
    itself against the plan, but nothing checked the plan against the
    workbook, which is a one-directional check pretending to be a
    two-directional one.** Where a workbook exists for this product,
    cross-check every headline figure this plan states — roster counts,
    budget totals, the product-goal declaration, sufficiency-stop status
    per ranking keyword, the TACoS band and decomposition — against what
    the workbook's own rows actually show. Where the two genuinely
    disagree, state which governs and why, once, as a plain fact, and
    carry that resolution back to whichever document is stale so both
    state the same number. A plan that was never checked against an
    existing workbook fails this item regardless of how internally
    consistent the plan reads on its own.

**A standing rule for maintaining this skill itself, not for building a
plan or workbook — and worth stating plainly given
how the two files are actually kept.** This skill and its workbook
counterpart are a deliberately duplicated pair sharing roughly the same
rule set in two different formats. **Any substantive change to one file
is made to both, in the same pass, before either is considered
complete — never one file updated with the other left to catch up
later.** A rule corrected in this file but not its counterpart is worse
than the same rule being wrong in both, because the two documents now
actively disagree with each other about what governs the same decision,
and nothing about that disagreement is visible until someone happens to
compare them. Verify parity explicitly before finalizing any edit: the
same phrase, or the same substance in that file's own established
wording, actually present in both files, not merely intended to be. This
does not relax for a small fix — a one-word correction skipped in the
companion file is exactly the kind of drift this rule exists to prevent,
not too minor to matter.

---

## Handing a decided file to an actual bulk upload

*(These govern the moment a decided set of changes becomes a file the
platform will accept. They are mechanics of the upload format, not of
the decisions, and every one of them has already caused a rejection.)*

**One row per entity, per upload. Every lever decided on the same entity
merges into that single row.** The platform validates the whole sheet as
one transaction and rejects a file carrying two rows for the same
campaign, keyword, ad, target or placement id. A builder that emits one
row per decision — a row for the state change, another for the settings
change — produces exactly that collision. On a real upload seven
campaigns and one product ad collided this way and the entire file was
refused, 213 rows for 8 errors.

**In an update row, every populated field is an assertion, not context.**
This is the part that makes the duplicate dangerous rather than merely
annoying. Building a row by copying the source entity and changing one
field silently re-asserts every other field on it at its current value.
Where a second row for the same entity carries a decided value, the two
disagree, and the platform takes the last one it reads. On that same
upload seven campaigns carried one row setting them enabled and a second
row — the settings change — carrying their current paused state alongside
it. Had the file been accepted, seven campaigns the plan was switching on
would have been switched off instead, silently and with no error.
**Populate only the identifiers and the fields being decided; leave every
other column empty.**

**Before writing the file, group every decided change by entity id and
confirm two things:** that no id appears twice, and that no field on a
merged entity carries two different decided values. The second is not
implied by the first — merging two rows that disagree produces one row
with the wrong value in it. A disagreement is a build error and stops
the file; it is never resolved by taking one and dropping the other.

**Creates are not idempotent; updates are.** Re-uploading an update sets
the same value again and costs nothing. Re-uploading a create makes a
second negative keyword, a second product ad, a second campaign. Any file
mixing the two cannot be safely re-sent as a whole.

**After a failed or partial upload, re-export before re-sending
anything.** A platform's summary sheet and its upload console can report
the same result differently — on one occasion the summary read "no change
was applied, 0 records successful" while the console read "205 / 213 rows
processed, partial upload." **Neither is evidence about the account; only
the account is.** Pull a fresh export, diff it against the pre-upload
one, and build a delta containing only what is genuinely still
outstanding. Never assert what did or did not land on the strength of the
report alone, and never re-send a file containing creates until the
export confirms they are absent.

## Reconciling against the workbook

**A confirmed plan for this product exists before any workbook build
begins — this is a state that has to be true, not an action that has
to happen in this same session.** If a plan was already built and
confirmed in an earlier session and nothing about the product has
changed enough to need revisiting it, that existing plan already
satisfies this — the workbook build starts directly from it, with
nothing to rebuild first. This only becomes a same-session sequence
when no confirmed plan exists yet at all, or when a plan does exist
but is being brought current before this workbook build relies on it.
**Both skills work standalone, and this doesn't change that** — a
workbook can be refined on its own, using an already-confirmed plan's
existing decisions, without re-running the plan side at all. What this
rule actually rules out is a workbook being built or refined against
*no* confirmed plan whatsoever, or against one that's known to be
stale, not against re-doing work that's already settled. This
workbook's own build sequence starts from that plan's confirmed goal
and tier decisions, then layers this workbook's own granular,
row-level checks on top (this file's own build-order section covers
that sequence in full).

**The reconciliation record is regenerated from the file it ships in,
every round, and never carried forward from the last one.** This block
exists so a reviewer can see what was and was not done without reading
every row; carried forward unchanged, it does the opposite — it
describes a file that no longer exists and reads as proof the
corrections were never made. On a real build the block survived a full
correction pass verbatim: it still described budgets as staged in two
steps inside the correction cap when they were held uncapped and
unstepped, still priced an action on the wrong child four rows below
the condition that settled the ruling, still recorded a rename as
shipped when it had been withdrawn, still counted an enable register
that had shrunk by one, and carried no row at all for an action added
in the same pass. Every one of its statements was true of the previous
file and false of the one it sat in.

**Rebuild it from the corrected file, and check three things
specifically:** that every action in the companion document's current
register has a row here, including any added this round; that no row
describes a value the corrected file no longer carries; and that
actions withdrawn or held are recorded as withdrawn or held rather
than left reading as shipped. **A reconciliation block is the one part
of a deliverable whose whole purpose is to be trusted without
verification, which is exactly why a stale one does more damage than
no block at all.**

If a workbook exists for this product:

1. **Every headline figure this plan states traces to the workbook's own
   rows**, or to this skill's own rules where the workbook is silent.
2. **Cross-check every headline figure** — roster counts, budget totals,
   and sufficiency-stop status per ranking keyword — against the
   workbook, every round either changes.
2a. **Reconcile at the level of deployable actions and states, not only
   headline figures.** Roster counts and budget totals agreeing does not
   mean the two files agree about what happens on deployment. On a real
   build the plan ordered a campaign paused on the inventory gate while
   the companion file kept it enabled with a settings fix and a held
   budget — both documents internally consistent, both passing their own
   checks, and neither reconciliation block mentioning it. Whoever
   deployed would have kept spending into a child the other file had
   just ordered stopped. **For every campaign and every row carrying a
   deployable verdict, compare the state and the action the two files
   would produce, and treat any difference as a blocker rather than a
   divergence to note.** A divergence is two files describing the same
   outcome differently; this is two files ordering different outcomes,
   and it is not resolved by recording it.
3. **When this plan's stated row-level number and the workbook's real
   row-level number genuinely disagree, the workbook governs.** The
   workbook's checks are more granular and more mechanically verified
   than anything decided at plan level — per-keyword inventory routing,
   the SV floor, the existing-instance duplicate check — and a
   disagreement usually means the workbook caught something real the
   plan's higher-level description couldn't have anticipated. State the
   correction once, as a plain fact, never a narrated correction, and
   refine the plan to match. This applies to row-level figures only —
   see the named exception below.

**The product's declared goal and overall state are not row-level
figures, and are never resolved by the rule above.** The goal
(Growth/Scale, Mixed, Profit-First, Clearance/LTSF) and the product's
declared posture/stage must read identically in the plan and the
workbook at all times — this is a strategic declaration, not a number a
more granular process gets to overrule. **If anything in the workbook
build appears to require, imply, or drift toward a different goal or
state than what's declared, that is never resolved silently in either
direction — it is flagged explicitly, stated as its own finding, and
put in front of the person running this build before anything proceeds
on the assumption of either the old or the new state.** A workbook
quietly building out coverage that only makes sense under a different
goal than the one on record is exactly the failure this exception
exists to catch.

**The goal is written on the face of both documents as a named value,
not left implicit in the decisions that follow from it.** A file can
refer to "the declared goal" throughout and never state which of the
four it is — on a real build one did so 182 times — which leaves every
reader reconstructing it from the verdicts and leaves the parity
requirement above unverifiable in either direction. State it once,
plainly, in the document's own front matter or basis block, together
with what it authorises and what it nullifies: whether the ranking
allowance is available at all, whether top of search is funded, and
where in the suggested range an opening bid sits. Those consequences
are invisible in row-level output, so a reader cannot recover the goal
from the file even when every row is correct.

---

## Data conditions register

Every plan carries a register of open conditions: the condition, its
evidence, why it matters, which actions it gates, an owner, and a due
date. A gap without a named owner is not recorded as closed — it's
recorded as open. A withdrawn finding stays in the register too, with the
evidence that overturned it, so the reasoning behind a reversed call
isn't lost.

**Before a gap is logged with a due date, check whether it's actually
that kind of gap.** Some conditions genuinely need time to resolve — a
re-derivation cycle, a restock, a rank read that hasn't happened yet —
and a dated register entry is the right instrument for those. Others are
just missing information that whoever is running this build might
already have, or could get in the time it takes to ask: a competitor's
price, rating, or review count that hasn't been pulled yet is not a
"wait and see" condition, it's a "does anyone have this" one. **A gap in
the second category is asked about directly, once, before it's logged as
an open condition with a due date it doesn't actually need.** Logging
"HOLD — evidence pending, revisit next cycle" on a row that could clear
in one answered question isn't thoroughness, it's a missed shortcut —
the row sits idle for a cycle it didn't have to.

**This same "ask once before logging it as permanently unknown" rule
applies to structural and definitional gaps, not only per-row data
gaps — stated explicitly because the examples above are all data
questions, and a reader could otherwise assume this only covers that
narrower case.** Whether a section of the document itself is genuinely
undefined, whether a convention like the account's own six-state
ranking system actually exists, whether a specific threshold is a real
account rule or something this skill should drop — these are exactly
the same "does anyone have this" situation as a missing competitor
price, just at the level of the document's own structure rather than a
single row's data. The same discipline applies: ask once, directly,
before concluding something is permanently unknown and writing it into
the plan as an unresolved gap. Only after that question goes unanswered
does it get recorded as genuinely open — the same standard HOLD is held
to, applied here to what gets called a gap in the first place.

**The other half of this discipline, worth stating with equal
weight: not everything that looks unresolved is actually in doubt, and
asking about something already knowable is its own failure, not
caution.** A misspelled or word-order variant of a term already
handled elsewhere, a value derivable from data already in hand, a case
this skill's own rules already cover once looked at properly — these
get resolved directly, without a question, because the answer was
never actually missing. Reserve the ask for genuine doubt: where a
finding could reasonably go two different ways depending on a
judgment call the account hasn't made, or reveals something the
existing rules never anticipated — and when asking, state the actual
reason for the doubt, not just the bare item, so the person answering
isn't left guessing what's actually being asked. A list of confidently
resolved items dressed up as open questions wastes the same attention
this whole discipline exists to protect.

---

## What this skill cannot honestly produce at scale

A scripted or single-pass reasoning statement can reliably cover the
decision-order, objective, ceiling, and state/gate logic in §1–§13B above
— roughly the mechanical two-thirds of a fully-argued campaign record. It
cannot, at the same reliability, produce: every candidate cause named with
evidence for and against it, a single hypothesis carrying a numeric
confidence level, a falsification test, an argued counter-case, the
alternatives rejected and why, three outcome branches, the cost of being
wrong, the cost of not acting, and a graded prediction ledger. Those need
a focused human pass across a small batch of rows (3–5 campaigns at a
time, combined upward to syntax and then product) — not because the
mechanics above are wrong, but because that judgment layer is a different
kind of work. **State this gap on the face of the document.** Producing
that depth at full scale anyway generates text that reads complete and is
not — the failure mode is not an obviously thin answer, it's a
confidently thorough-looking one.

**This is a tracked, working gap, not a closed one.** The account has
asked directly for more of this depth — hypothesis, reasoning, and
future-state columns — as the metrics and app-level data available to
build them expand. Where the underlying data now supports a genuine
version of one of these (a named alternative explanation actually
checked, not invented; a stated future-state condition actually tied to
a re-read date), include it and say so plainly, rather than treating this
section as a permanent ceiling on what the plan can ever carry.

---

## 14. One-and-only final draft
**A correction is a defect class, not an instance, and it is swept with an independent count before and after.** This rule already exists for gates and repairs; it applies with equal force to any figure, claim or decision the build changes mid-cycle, and that extension is stated here because it was missed exactly once and produced a document arguing with itself. On a real build the spend envelope was re-derived and the funding claim rewritten in the section that owned it, and six further instances of the superseded figure survived in four other sections — so the same plan simultaneously read "this is not zero" and "without new budget", which is the reviewer's own named rejection trigger sitting inside one document. **When a number, a roster, a target or a verdict changes, list every string that expresses the old value, count each one across the whole file, replace them, and count again.** The count is the evidence; a search that found and fixed some instances has not been shown to have found all of them, and the reader who quotes the document against itself will not be looking in the section where the fix landed.

**Downstream figures move with their source in the same pass.** A resized roster changes its daily cost, its weekly cost, its net-new requirement, its loss ceiling, its term count, every action row that names a per-push figure, every expected-outcome row derived from it, and the decision that requests the money. These are not separate edits to be discovered later; they are one edit with many surfaces. Build the dependency list before touching the source figure, not after.
**The correction sweep is run mechanically against the rendered file, not mentally against the source, and its output is the evidence.** This rule already requires a before-and-after count on every changed figure. It kept passing anyway while stale strings shipped, because the sweep was performed in the builder's head over the working document and the rendered deliverable was never searched. On a real cycle five superseded strings survived three consecutive corrections and reached a reviewer — an old property count, an old term count, an old release figure, a conflated pair, and a sentence garbled into meaning its own opposite — in a document whose central argument is that counts must survive their own corrections. **Maintain a stale-string list as a real artifact: every value the plan has superseded, grouped by the class it belongs to — roster counts, daily costs, net-new figures, loss ceilings, release figures, contribution bases, property counts, gap language, funding claims.** Add to it on every correction, never remove from it, and run it against the rendered file before anything ships.
**A changed verdict leaves no string to search for, so the sweep is run by entity, not by string.** The count sweep above finds superseded *figures*, because a figure is a literal a search can match. A superseded *decision* is invisible to it: a term withdrawn from the roster still reads "Fund — best cost of sale" in the competitor table, a push reduced from four to one still reads "part of the wave-two push" in the wave table, and neither cell contains a single character that changed. On a real cycle the roster collapsed from five pushes to one and three sections kept their old verdicts — including a decision column that would have had a reader funding two terms the plan had deliberately surrendered on its own evidence, which is worse than an arithmetic error because it reverses the document's best decision rather than miscounting it.
**The unit of regeneration is the decision, not the cell — and the unit of checking has to match.** A
row's Action, its Reasoning, its reversal condition, and the campaign row that hosts it are four
surfaces of one decision. When the decision changes they all re-derive from the current record in the
same operation, because regenerating them separately does not remove staleness — it moves it. On a
real build the accreted-cell defect was fixed by regenerating cells one at a time, and the result was
sixty rows whose Action priced top of search at $7.35 beside a Reasoning stating no price could be
set, and fifty-four reversal conditions citing a per-order figure from a computation two passes
deleted. **A single row told three stories from three renders.** The in-cell accretion had become
cross-column contradiction, which is harder to see and worse to ship.

**A gate that reads columns independently will certify a file whose columns disagree**, and on this
account it did so three renders running while reporting zero failures. The row-integrity check reads
the four surfaces as one record and asks four questions of each row: does the Reasoning affirm the
figure the Action deploys; does the reversal cite only computations the Reasoning still states; does
the Action's own wording match the value in its cell; does the hosting campaign describe the program
its keywords actually carry. None of those is answerable one column at a time.

**Where a verdict changes, write every surface of it or none.** A half-regenerated row is not a
partial improvement over a stale one — it is a row that now contradicts itself, and a reviewer who
finds one contradiction stops trusting the rest of the file, including the parts that are right.

**The relevant-non-converter rule is enforced by a screen, not by remembering it.** This rule already existed in this file and was violated anyway: a negation pass built from a search-term report put "cooling sheets", "queen cooling sheets" and "cal king cooling sheets" on the negative list for a cooling sheets product, because the query that produced it filtered on clicks and zero orders and never asked whether the term was on-target. **Spend with no orders is what a negation screen naturally surfaces, and it is precisely the wrong filter** — it selects relevant terms that are underperforming just as readily as off-target ones.

**Build the screen structurally first, then let performance decide only among what survives.** A term is negatable on relevance alone when it names another product category, another material this listing is not, a competitor brand, or the account's own ASIN — those need no click history, because no volume makes them correct. Everything else is on-target by construction, and an on-target term that is not converting is a pricing or listing problem wearing a keyword's clothes. **Route it to a fix queue, priced to what its routed child affords and re-read at a stated click count, and record it somewhere a reviewer can see it was considered and deliberately not negated** — a term that simply vanishes from the negation list is indistinguishable from one nobody checked.

**The own-catalogue scan runs before the list is finalised, not after.** A term reading off-scope for this product is often real demand the account sells through a sibling, and negating it there blocks traffic the account still wants rather than steering it. That distinction is the difference between the reactive and steering modes, and it changes what the negative is for: one walls off traffic, the other redirects it.

**Prose is regenerated, never patched with a pattern match.** Removing a superseded sentence from a
reasoning cell by regular expression cut 556 rows mid-clause on a single pass, leaving fragments like
"rather than a layer to question.5 per cent conversion affords" — text that still cited real figures,
still carried its window, still passed every other check, and was unreadable. Each repair attempt cut
a new sentence in half, because a pattern written against one phrasing meets a dozen it was not
written for.
**A section whose governing decision changed is rewritten from the decision record, never patched by substitution — the cell-scope rule, restated at section scope.** Regenerating cells stopped in-cell accretion and moved the staleness across columns; the row-integrity gate stopped that and moved it up again, into sections whose surrounding sentences depended on a figure that changed underneath them. **The unit has to match the thing that moved.** When the decision a section describes is superseded, its prose, its tables and its arithmetic all re-derive from the current record together, and the superseded narrative is deleted rather than renumbered.

**Substituting a figure into a sentence built for a different one produces arithmetic that is false on its face.** On a real build a two-term push at $17.10 a day was replaced across twenty body locations by a budget-cap total of $378.56, without a single surrounding sentence being re-derived. The plan then asserted that $26.16 released "exceeds the $378.56 push" — wrong by fourteen times — and that committing $378.56 against $26.16 left "$9.06 a day left over." **A reviewer needs no rubric for those; they only need eyes,** and the correct funding account sat three sections below in the same document. The same pass replaced a child name with a descriptive phrase, producing "against Routed per row from product-ad rows's own ceiling" and a roster total fusing one design's per-unit economics with another design's placement count.

**Two checks make this mechanical, and both belong in the gate rather than in a reading.** Parse every sentence comparing a release to a commitment and re-derive the comparison — a claim that one figure exceeds another is arithmetic, and arithmetic can be run. And require that columns naming a child contain a child name, because a substituted phrase lands in a name column looking exactly like data. **A figure that changed scope needs its scope label carried with it:** a per-day release and a sixty-day total are not comparable, and the sentence that compares them reads as a contradiction even when both figures are right.

**Where a superseded design still deserves a record, it lives in the withdrawn-actions register and nowhere else.** A two-term push recorded once as superseded is history a reviewer can follow; the same push half-surviving in a roster table, a five-property row and a destination table is a document funding and un-funding the same thing in adjacent sections.

**Where a reasoning cell needs to change, rebuild it from the row's own data rather than editing the
string.** The inputs that produced it are still available; regenerating costs one more computation
and cannot corrupt what it does not touch. A pattern match may be used to *find* the rows needing
attention — never to perform the edit itself.

**A superseded figure surviving inside otherwise-correct prose is the specific danger.** A cell
stating both an old bid and a new one is worse than a cell stating neither, because a reviewer has no
way to tell which one the file will actually deploy. After any repricing pass, check that each cell
names its current figure once.

**A rule that governs two entity types is checked against both before the pass is called complete, and the check is written down.** This is the single defect class this file has produced most often, and it is not a knowledge failure — every instance was a rule already read, applied once, and not carried. The pairs that have actually failed on this account, each now named so the check has something concrete to run against:
**A column that records the current state and a column that carries the instruction are two different columns, and writing an instruction into the recording column destroys the record.** The decided file's State column holds what the account has today; the Action column holds the ruling. That convention held on 384 keyword rows and was broken on 247 more when a staging pass wrote target states — `enabled`, `paused` — into the recording column to mark which wave a row belonged to. **The before-state was overwritten and no longer recoverable from the file**, which matters twice over: the revert file is built from it, and a reader comparing Action against State now sees contradictions that are not there.

**It then produced a false defect report.** A row reading `State = enabled` beside `Action = PAUSE` is correct under the convention — the keyword is live and the ruling is to stop it. Read as though State were the target, 169 correct rows looked like contradictions, and a fix applied to them would have inverted every pause in the file. **A check that assumes the wrong convention will confidently break a correct file**, which is why the convention is stated on the face of the file rather than held in the builder's head.

**Where a row needs an attribute the export has no column for — a wave, a sequence, a gate — it gets its own column.** Never a spare field that already means something. The instruction to add nothing to a delivered file governs its rows, not its ability to record a decision that has nowhere else to live.

**Staging happens at the level the instruction names, and the projection is costed at that same level.** A request to release "a few keywords first" was implemented as a campaign-level release: 62 campaigns opened, and every keyword inside them opened with them — 227 in total, against a request for a few. The cost was then projected per campaign, so the file reported $230 a day for a set whose keywords, priced individually, came to four times that. **Two errors, one cause: the unit that was staged and the unit that was costed both differed from the unit that was asked for.** State the staging unit explicitly, cost the programme in that unit, and where the controlling constraint sits on a different entity — a budget on a campaign capping keywords beneath it — say which entity actually binds the spend.

**A budget is a ceiling, not a forecast, and the two are never reported as one number.** Summing the budget column produces the maximum the account could spend if every campaign delivered to its cap, which on a real build was $1,948 a day against actual spend of $60.84 — a figure quoted as though it were the programme's cost, and wrong by a factor of thirty. Live campaigns on that product were using 25 per cent of their own caps. **Where a spend figure is stated, say which of the three it is:** what was actually spent in a measured window, what the caps permit, or what delivery is projected to cost — and project from the account's own observed click rate per delivering row, not from the cap.

**A projection carries the sample it rests on.** The observed rate on that product was 2.69 clicks a day per delivering row, drawn from fifteen delivering rows — a thin base to project several hundred from, and the projection says so. A forecast whose basis is not stated invites the same trust as a measurement, and it has not earned it.

**A programme that grows across passes needs a total, and nobody supplies one unless it is asked for.** That build began as a two-term push and reached 948 acting rows through successive rounds of correcting defects, each correct in itself, none of them ever asking what the whole thing would cost. **State the programme's projected total against an approved envelope before it ships, and where no envelope exists, that absence is the finding** — not something to resolve by choosing a number.

**Where the projected total exceeds the envelope, the programme stages rather than shrinks arbitrarily.** Order by evidence — search volume, gap to a stated rank target, proven conversion — open the first wave inside the envelope, and gate each later wave on the previous one holding to its projection over a stated period. **The envelope is a ceiling at any moment, not a running total:** later waves take up the headroom earlier ones leave rather than stacking on top, and a staging plan that sums cumulatively past the ceiling has misunderstood what the ceiling is.

**A screen runs against the population the rule is about, and that population is named before the
screen runs.** An already-targeted screen was written against this portfolio's live keywords and
missed 51 terms live elsewhere in the same account — a term already running under a different
portfolio is no less already running. The same screen also checked only Phrase and Broad instances
while the launches being screened were Exact, so 275 Exact-targeted terms passed a check written for
a different match type.

**Two questions before any screen: which population does this rule govern, and does my query cover
it?** Portfolio, account, brand family and catalogue are four different scopes, and the right one
comes from the rule rather than from whatever data happens to be loaded. **State the scope in the
reasoning** — "screened against all 8,118 live keyword terms in the account, not just this
portfolio" is checkable; "not currently targeted" is not, and was true of the portfolio while false
of the account.

**Where a rule is about identity rather than instance, the screen collapses forms before comparing.**
Singular and plural are one identity; word-order variants are not. A screen comparing raw strings
will report a term as absent while its plural runs live.

**Every row of every entity carries a verdict, and the count is stated per entity before delivery.** Not every decided row, every row. A row left blank is indistinguishable from a row nobody reached, and on a real build 372 keyword rows were never decided at all while the file reported clean — including 140 bare-bamboo terms carrying live bids up to $6.40 in a portfolio that does not own bamboo demand. **Count the rows per entity type, count the verdicts, and state both.** Keyword, product targeting, campaign, bidding adjustment, negative keyword: each gets its own line, and a gap between the two numbers is a finding, not a rounding difference.

**A decision the plan already made is traced into the workbook by name, and its absence is a defect.** Where a companion plan names a wall, a withdrawal, a negation set or a funded roster, those decisions exist to be executed here — a plan that names a 117-term negative wall and a workbook that never writes one are not two documents disagreeing, they are one decision that was never carried out. **List the plan's own named decisions, find each one in this file, and state where it landed.** Anything unfound is either executed in the same pass or named as deliberately deferred with its reason.

- **Routing rules govern reactivation as well as new launch.** A query naming a size or colour may only route to a SKU sharing it — on launch *and* on any row being re-routed back into service.
- **Sample floors govern placements as well as campaigns.** A campaign clearing fifteen clicks says nothing about whether its top-of-search row did; a rate computed on a placement below the floor is arithmetic wearing evidence's clothes.
- **Lever rules govern every entity the change touches.** A repriced keyword implies a campaign whose budget was either changed or evaluated-and-held, and bidding-adjustment rows whose modifiers were either re-solved or explicitly held. Blank is not a verdict.
- **Ceiling exceptions govern the section that computes, not only the section that authorises.** An allowance stated in the ranking section binds the placement section that actually writes the number.
- **Decision columns govern every table that carries one.** A verdict changed in the roster is stale in the competitor table, the rank ladder and the wave register until each is checked.

**Before calling any pass complete, list the entity types the pass touched and confirm each rule applied was applied to all of them.** Where a rule genuinely does not reach an entity type, say so in one line rather than leaving the absence to be read as an oversight — an evaluated exclusion and a missed one look identical in a delivered file, and only one of them is defensible.

**Keep a decision register for the cycle: every entity the plan rules on — each term, child, campaign, layer — against its single current verdict.** When any verdict changes, walk the register entry to every table that carries a decision, action, verdict or status column and check that entity's row in each. **The question is never "does this section contain the old text" but "does this section still say the right thing about this entity".** A term appears in the roster, the competitor table, the rank ladder, the coverage tables, the wave register and the expected outcome; a verdict that changed in one and not the others is the normal failure, not the exceptional one.

**Every column that states a verdict is checked against the register before delivery, and the check is by column, not by reading.** List the document's decision-bearing columns once — Action, Decision, Verdict, Status, Owner, Result, Read — and for each, confirm every row agrees with the register. A document whose sections were each individually correct when written is still wrong if a later decision moved past some of them, and reading for sense will not catch it: the stale cell reads perfectly well on its own and only contradicts something twenty pages away.

**A string that legitimately survives is exempted by name, with the phrase that makes it legitimate.** A superseded figure quoted as history — "the earlier draft proposed five pushes", "priced against the portfolio line it ran at 39.6 per cent" — is correct writing and must not be swept away; a bare exemption list that only names the string would also silence the defect. Exempt on the surrounding phrase, so the same digits still fail everywhere else they appear. On the cycle above this distinction mattered immediately: of seven hits, two were live defects the reviewer had not found and five were legitimate history, and only a context-qualified exemption separates them.

**The gate is cheap, so it runs on every render, not on the final one.** A search across a rendered document costs seconds. The failure it prevents costs a reviewer's confidence in every count in the document, which is the one thing a plan built on arithmetic cannot afford to spend.

Zero revision narrative anywhere in the delivered document — the test is
whether a sentence would make sense to a reader who's never seen an
earlier draft, not a banned-word list. When a verdict changes during a
build, rewrite the paragraph to state the final answer as if it were the
only one ever computed. **Action owners are named individuals, never roles or teams** — this account's own standing instruction. "Ahmad Ilyas", not "Purchasing"; "Shayan R.", not "the PPC team". A role-based owner is an unassigned action.

When refining an existing plan, the delivered plan is rewritten as a
single clean final version — no version trail, no visible seam. The
reasoning behind why something changed belongs in a companion workbook's
audit trail, never narrated inside the plan's own prose.

Revision discipline on a multi-round build: search the whole document (and
companion workbook) for every place a changed headline number appears
before calling a pass done; run the outstanding fix list from the previous
review first, before opening the document to whatever's currently being
debated; land corrections before reversals.

---

## Brand Management findings register — built out in full, not left as a skeleton placeholder

**The standing principle: PPC outputs stay PPC-scoped.** Any finding
that requires a lever PPC doesn't control — a lever that belongs to
Brand Management, Supply Chain, or another team — is raised here, with
its evidence attached, and never executed by this skill on its own
initiative. **Raised, never silently dropped, and never quietly worked
around with a PPC lever that wasn't built to fix it.** A bid can't
correct a listing defect, and pretending it can just delays the actual
fix while spending money on a symptom.

**Named categories, drawn from established account practice and from
the specific routing instances already built elsewhere in this
skill — restated here as one list rather than left scattered:**

- **Price position** — a term's price sitting meaningfully above the
  category median, named in §7's realism gauntlet (the OUTPRICED check)
  and in §2B's Conquest entry test; a bid can't out-compete a genuine
  price disadvantage.
- **Listing defects** — a confirmed content, image, or A+ problem
  surfacing through §1B's chronic-Conversion syntax diagnosis, or
  through the quality gate (§1) that routes a conversion failure away
  from a bid verdict.
- **Returns drivers** — a return-rate finding that explains a CVR or
  rating problem no bid fixes.
- **Range gaps** — a real, sizeable search volume with no SKU to serve
  it (the kind of finding §12's coverage worklist or Market Share's
  coverage-worklist state surfaces without being able to act on it
  itself).
- **Inventory/PO conflicts** — including, specifically and newly
  wired in here, **§7's projected-days-of-cover finding**: a push sized
  to close its own order gap that would run a SKU into Yellow or Red
  before its own checkpoint date. This is exactly an inventory/PO
  conflict — the fix (expedite a shipment, adjust a PO date, hold a
  larger safety stock) is Supply Chain's lever, not PPC's, even though
  the finding itself surfaced from a PPC sizing calculation. State the
  specific SKU, the specific projected date it would drop out of Green,
  and the specific push that would cause it, so Brand Management or
  Supply Chain has exactly what they need to act without re-deriving it.
- **A competitor's structural advantage** — the archetype and
  competitor-check findings from §2B and §7's State E investigation
  that name a specific competitor's price, rating, or review advantage
  as the actual cause of a rank problem no bid can fix.

**Every entry carries its evidence, not just its conclusion** — the
specific numbers, the specific date, the specific row that surfaced it
— so the recommendation is actionable without anyone having to
reconstruct why it was made. An entry with a conclusion but no evidence
fails the same standard as any other unsupported claim in this skill.

---

## Document skeleton — the real hierarchical shape, confirmed for the opening, honest about the rest

**This account's real plans use a hierarchical shape, not a flat
numbered list — corrected here after direct evidence showed the flat
1–26 numbering this skill used before doesn't match how a real,
approved plan is actually built.** The real shape is numbered main
sections with lettered and dotted sub-parts underneath them (1.1, 1.2,
2A, 2B.1, 2B.2, and so on), evidenced directly against the SSS4 plan
Erik reviewed and approved. The flat list this skill carried
previously was an invented flattening of that real shape, and the
oddities that came from it — the section-6-vs-7 ambiguity, two blank
gaps that never resolved — trace back to that root cause, not to
missing content.

**This numbering is invariant across every plan this skill produces,
regardless of who runs it or which product it's for — the direct answer
to the account's own standing requirement that structure be identical
across all three PPC team members.** A build for Ghazanfar, a build for
Shayan Rana, and a build for Shayan Akhtar Taquie all carry this same
section list, in this same order, under these same names. Nothing about
per-product content — a thin section because the product genuinely has
little history, a gap flagged for one product and not another —
authorizes renumbering, reordering, or omitting a section. A thin
section stays present and says it's thin; it does not disappear.

**Template fidelity is exact, not approximate, whenever a reference
template or a fully-populated example is given — the same standard
applies to both, not only to a blank template, and it covers visual
presentation, not just the section list, previously unstated for the
plan side of this pair.** Same heading styles, same fonts, same heading
and body colors, same numbering format, same spacing conventions — read
past a fully-populated example's actual content to its formatting and
match that exactly, never approximate it because the source already had
real findings written into it. Where an example carries its own visual
inconsistency (one heading level styled differently than its siblings,
an odd color choice on one section), clone that inconsistency faithfully
rather than silently harmonizing it into a cleaner scheme the builder
assumes was intended — the same discipline the companion workbook
already applies to its own template fidelity.

**The invariance rule above governs the section list itself — it was
never meant to forbid adding anything inside a section that already
exists, and that distinction is worth stating directly rather than left
to be inferred.** Something specific to one product that doesn't have a
ready-made home in the fixed section list — an unusual finding, a
consideration this product's own situation calls for that the standard
sections don't anticipate — is added as a subsection nested under
whichever existing section it most belongs to, styled to match that
section's own formatting, not invented as a new top-level section.
"Never carrying an extra section the structure doesn't require" means
exactly that: no new item in the section list. It was never a ban on
extending what's inside a section that's already there. **That said, a
subsection is still something the build adds because it's actually
needed, not a habit — limited to what the situation genuinely calls for
or what's been explicitly asked for, same as any other content decision
in this skill, not scattered in speculatively because a section had
room.**

**Which phase each section belongs to, marked in the skeleton itself.** The section list below is not written in one pass. **Analysis sections — story and context-corrected metrics, actions taken and measured results, the profitability-first diagnosis, per-keyword and per-campaign mathematics, coverage with named declines, competitor position, oversight cadence, and the gaps register — are written before the workbook** and do not move when the programme changes. **Programme sections — the action-plan-at-a-glance, the roster, the five-property record, earning potential and declarations, recovered value per action, the expected outcome, and the reconciliation — are generated from the workbook after it freezes.** A draft carrying programme sections written ahead of the workbook is describing decisions nobody has taken, and it will be rebuilt rather than edited.

**What follows is confirmed to a real, evidenced degree for the
opening of the document, and openly less certain from there — stated
honestly rather than dressed up as equally confirmed throughout.**

**Front matter, confirmed:**
- **Title block** — product identity (name, parent ASIN, SKU count),
  plan date and version, the measurement windows the whole document
  runs on, which governing documents this plan is built against,
  any companion document (a BM-side plan this PPC plan is written to
  agree with), and the objective declaration. **The version number
  tracks Erik-facing milestones, not internal drafting passes — new
  guidance, since nothing previously said when it should actually
  change.** Any number of rounds correcting, adjusting, or refining the
  plan while it's still being built has not yet been shown to Erik, and
  the version number holds through all of them — v1.0 stays v1.0
  whether it took one pass or many to reach something worth presenting.
  It only advances once the plan has actually been presented to Erik
  and he's asked for a revision based on that presentation — that
  specific event is what earns the next number, not the act of editing
  itself. A plan that never went through that many internal correction
  rounds before its first real presentation is not "behind" some other
  plan that went through fewer; the version number was never counting
  drafting effort, only how many times Erik has actually seen it and
  sent it back.
- **"The plan in five lines"** — a short, dense summary at the very
  top. This does not replace the fuller numbered findings and detail
  that follow; it's a distinct, shorter component that exists
  alongside them, not instead of them. **The fuller findings below it
  are commonly five to seven, each carrying its own load-bearing
  number stated inline; a three-line compression defeats the point of
  having fuller findings at all.**
- **"Action plan at a glance"** — organized in waves tied to real
  dates or triggers (e.g. before a charge date, within the first
  week, weeks two through four), not one flat list. Each row: number,
  action, owner, recovered value, success measure, and a section
  reference pointing to where the full reasoning lives. Closes with
  what the plan costs and is worth **both in total and broken out by
  phase — a total alone hides whether cost is front-loaded
  or spread evenly, which changes how a reviewer reads it**, and a
  named, short list of the specific decisions that need someone
  outside PPC to make them — stated as their own callout, not folded
  into the action rows. **Each action names the entity it changes and
  how many rows deploy it**, because "deploy the re-route programme —
  537 rows" reads as one operation and was in fact two: a bid change on
  441 rows that shipped, and an advertised-SKU change on 62 that had no
  rows to ship in. **A count that mixes operations overstates what
  deployment achieves**, and the reviewer discovers it only when the
  numbers do not move.

**Section 1, confirmed — the product story:**
- **1.1 History** — what shaped this product's performance, dated:
  outages, deals, listing or price changes, prior ranking positions.
- **1.2 Current situation, on today's data** — the exact state as of
  the plan date, not a stale export: true inventory, campaign and
  keyword counts, spend, rank, listing state.
- **1.3 Context-corrected metrics** — current numbers read through
  what produced them, never at face value; each correction stated by
  name, with the reversal it implies. **The rank series is shown at
  three cadences side by side — daily, weekly, and monthly.** §7's rank-trend
  logic still governs what the numbers mean; this is the presentation
  requirement for how they're shown, which is a separate thing and
  was lost when the table row describing it was removed.

**Section 2, confirmed for its economics sub-part, less certain for
the rest:**
- **2B — Recovered value, every action priced in forward cash.**
  Sub-parts confirmed: **2B.1** the unit economics PPC is actually
  working with (per-SKU or per-unit contribution, the account's own
  version of what this skill's §3 computes); **2B.2** recovered value
  per individual action, action by action; **2B.3** resolving any
  conflict between PPC's own plan and a parallel decision system (an
  LTSF or BM-side plan this document has to agree with); a further
  sub-part continuing that reconciliation.
- **Other sub-parts under 2** (build status per syntax, zero-stock
  handling, search-term negation and harvest) are evidenced as real
  but their exact sub-numbering is inconsistent even within the one
  real plan checked — state the content, and don't force a specific
  sub-letter that isn't confidently known.

**Two account documents remain pending — not a deliberate retirement,
an unintended loss caught on review and corrected the same way any
other mistake in this skill is corrected.** The account's own Criteria
System v4.0 and Keyword Decision Record Template v3.0 would likely
settle several of the open questions this skill still carries —
including the exact position of the two genuinely blank spots
elsewhere in this document. As of this skill's most recent check, both
remain pending upload to this project rather than available to read.
The earlier version of this skeleton tracked that dependency
explicitly; the rewrite that corrected the flat-numbering problem swept
this note away along with it, even though the two problems were
unrelated. It belongs here regardless of the numbering shape, and its
disappearance was never a considered call — restored rather than left
gone with no record of why.

**The full shape is now confirmed, 1 through 9 plus 7A, evidenced
against the account's own exemplar and reproduced exactly by a
delivered plan built from it.** The numbering below is real, not
inferred:

**1** Product story · **2** What we did and what it produced · **2A**
Earning potential and the declarations · **2B** Recovered value ·
**3** Diagnosis: where the spend sits · **4** Per-keyword and
per-campaign mathematics · **5** Coverage · **6** Competitor position
· **7** Oversight · **7A** Contingencies and standing playbooks ·
**8** Execution register · **9** Reconciliation, gaps and what would
change the plan.

Sub-numbering inside each section is set by what that product actually
needs — add subsections rather than new top-level sections, styled to
match their parent. Where a reference plan or template is supplied for
a specific product, its numbering governs over this list (per Step 0's
structure-source mechanism).

**The sub-section list is fixed too, not only the twelve top-level
sections — and the freedom stated above was being read as licence to
omit.** "Sub-numbering is set by what that product actually needs"
governs *additions*: a product with an unusual finding nests it as a
new subsection. It was never licence to drop a subsection the exemplar
carries, and it was read that way on a real build, producing a plan
that carried all twelve top-level sections and roughly a quarter of the
exemplar's content — 7,172 words against 27,329, with §8 at 313 words
against 2,712. Every top-level heading was present and the analysis
underneath most of them was a fraction of what the same data supported.

**These subsections are required in every plan, on the same terms as
the top-level sections: present, or present and stating why they are
thin. Never absent.**

| Section | Required subsections |
|---|---|
| **1** | 1.1 History · 1.2 Current situation · 1.3 Context-corrected metrics · 1.4 Inventory, days of cover and SKU routing |
| **2** | 2.1 Parent-level performance · 2.2 Rank outcome · 2.3 Prior actions and their grading · 2.4 Build status per syntax and match type · 2.5 Advertised-SKU register and provenance |
| **2A** | 2A.1 The spend envelope · 2A.2 The posture record · 2A.3 Search terms — waste, negation and harvest · 2A.4 The waterfall |
| **2B** | 2B.1 The unit economics, **per child, never blended where per-child data exists** · 2B.2 Recovered value per action · 2B.3 Reconciliation with parallel decision systems |
| **3** | 3.1 Syntax diagnosis · 3.2 Spend by quadrant · 3.3 Scale, fund or redistribute · 3.4 Where spend comes out · 3.5 Where it goes · 3.6 Cross-comparison against siblings |
| **4** | 4.1 Objective declared per campaign · 4.2 Per-keyword plan · **4.2b Prior-window performance per keyword (W1 vs W2)** · **4.2c Top keywords against competitor position** · 4.3 How each budget is derived · **4.3a The rank ladder** · **4.3b Budget truncation and what it contaminates** · 4.4 Ranking diagnosis · 4.5 Placement · 4.6 Target-state roster and release sequence · **4.6b Inventory gate — eligibility per child, current zone and projected cover at push velocity** · **4.6c Held-action sweep against the declared goal** · 4.7 Duplicate ownership |
| **5** | 5.1 Keyword coverage · 5.2 The highest-value gaps · 5.3 Paused terms — reason or reactivate · 5.4 Named declines · 5.5 Ad-type coverage · 5.6 Ad-type plan |
| **6** | 6.1 The competitive set, priced and dated · **6.2 How competitors buy traffic — their ad-format mix against ours** · 6.3 Structural gaps |
| **7** | 7.1 Dated checkpoints · **7.2 Weekly cadence, full product** · **7.3 Divergence routing — what goes where, and what it does not** · 7.4 Prediction scoring · **7.5 Settle windows and read dates** |
| **7A** | One subsection per live contingency, each naming the signal that fires it, each with its own table of blocking condition, resolution and target |
| **8** | **8.1 Wave one, with a prediction per action** · **8.2 Wave two, same** · **8.3 Recommendations to Brand Management, as a table with evidence per row** · **8.4 Expected outcome — a before/after table** |
| **9** | **9.1 Figures to reconcile — this document against every other source** · 9.2 Named gaps, each with what it blocks and an owner · **9.3 Caveats and what the data could not show** · 9.4 What would reverse the main verdicts · 9.5 Decisions requested |

**"How each budget is derived" is a budget table, not a bid table.**
Per campaign: budget now, the platform's own recommendation where one
was issued, time in budget, and the action with its reason. Where no
campaign is truncated and no recommendation exists, that is the
finding — say it, and the table's value becomes the misallocation it
exposes rather than the constraint it fails to find.

**A subsection is thin only when the data is thin, and it says which.**
"This product has no prior cycle to grade" is a complete 2.3. "Not
computed" with no reason is not. Before writing any subsection short,
check the findings file for whether the data it needs was already
extracted — on the real build above, the prior-window comparison, the
twelve-month rank series, the budget-truncation result and the
per-placement series had all been extracted and none reached the
document, because each was summarised into a sentence in a neighbouring
subsection instead of given its own.

**Every subsection carries at least one table. This is not a stylistic
preference and it is the single largest driver of whether a plan reads
as analysis or as assertion.** The exemplar this account approved runs
68 tables across its subsections and has no prose-only subsection
anywhere in it; a plan built against the same skill delivered 38 tables
with 23 subsections carrying prose alone — every top-level section
present, every subsection present, and less than half the evidence on
the page. A paragraph asserting a finding and a table showing the rows
the finding rests on are not interchangeable: the reader can check the
second and can only trust the first. **Where a subsection's finding
rests on rows of data, those rows are tabled. Where it genuinely rests
on a single figure or a ruling, a two-column table stating the figure
and its basis still beats a sentence, because it forces the basis to be
written down.**

**State the sequence as funding, because that is what it is.**
Repricing above-ceiling bids does not delay a push, it pays for one:
the same envelope buys roughly twice the clicks once cost per click
sits at ceiling. The correct construction is "this funds that, in this
order, on these dates" — never "this waits on that." A verdict that
genuinely stops spend on a row stops it for a named, evidenced reason
that is not sequencing: the child is out of stock, the term is
own-catalogue, the contribution is negative at any bid. **Those are the
only holds a growth-declared plan carries, and each one names its
condition and its release date.**

**Where a push is sequenced across waves, the plan carries the wave
history that explains the order** — what each wave releases, what it
funds, what it unblocks in the wave after it, and what would make the
next wave start earlier or later. A wave table listing actions without
that chain reads as a schedule; with it, it reads as the argument for
why the money moves in that order.

**Charts are rendered images, not text approximations, and each one
carries its finding as its title.** The exemplar embeds real plotted
charts — a dual-axis bar chart, a combination line-and-bar with an
inverted rank axis and annotated callouts, a placement comparison —
each sized to the text width and titled with the conclusion it
demonstrates ("The inversion: the best-converting placement takes the
fewest clicks"), not with the variables it plots ("CVR by placement").
A plan built beside it used block characters typed into paragraphs, which
cannot carry a second axis, a value label, an annotation or a legend, and
which break entirely when the reader's font is not monospaced.
**Render charts with a plotting library, save as PNG at 150 dpi or
better, and insert at the document's text width.** Three to six charts
is the working range: fewer and the document is a wall of tables, more
and the reader stops reading them.

**A chart earns its place by showing a relationship a table cannot.**
The exemplar's three are all comparisons the eye resolves instantly and
a column of numbers does not: a metric inverted against its own funding,
two series moving together over time, a distribution against its
target. **A chart that restates one column of a table it sits beside is
noise; a chart showing two columns in tension is the finding.**

**Every data table in the delivered document carries its own source and
measurement window, directly beneath it.** The findings-file rule (I-3)
already requires each extracted figure to carry its source file, sheet
and window; that requirement stops at the findings file, and it needs to
reach the deliverable. A reader cannot check a figure whose origin is
stated only in a header block twenty pages earlier, and a plan whose
tables mix a sixty-day window, a measured week and a twelve-month series
— which most do — makes that header block actively misleading. On a real
build, 35 of 70 tables carried neither a window nor a source in their own
text while the document's opening block listed seven windows the reader
was expected to map to tables unaided.

**The line sits immediately below the table, before the explanatory
paragraph, in the format: source, then scope where scope is not obvious,
then window with its dates.** "Sponsored Products bulk export, campaign
entity · 30 June – 27 August 2026" is complete; "bulk export" is not,
because it names neither which entity level was read nor when. Where a
table combines sources, each is named against the columns it supplies.
Where a table states targets rather than measurements, the line says so
and names what the target was derived from.
**Provenance lines are checked for completeness and for a single format, not just for presence.** A line naming a source but no window is half a provenance and passes any check that only asks whether a line exists. Two date formats in one document — "30 Jun – 27 Aug 2026" beside "30 June – 27 August 2026" — is the kind of inconsistency a close reader notices before the analysis, and it costs attention that should be going to the numbers. **Confirm every provenance line carries a date or states explicitly that no window applies, and confirm one date format across the document.** Where a line genuinely has no measured window — a standing cadence, a routing rule — it says so in those words rather than trailing off after the source.

**This is the check that makes 0-B enforceable rather than aspirational.**
Every scope conflict found on that build — orders at two values, cost per
click at two values, phrase orders at two values — was a figure correct at
its own scope, sitting in a table that never stated which scope it was.
Tables carrying their own provenance make the conflict visible while the
table is being written, which is the only point at which it is cheap to
resolve.

**Every table is followed by prose that does the work the table cannot.**
The exemplar averages 226 words after each table and its median is 165;
a plan built beside it averaged 78. The gap is not padding — it is the
difference between showing rows and explaining what they mean. **The
paragraph after a table states what the table decides, names the
specific rows carrying the finding with their figures, says what the
reader should conclude, and connects it to the section that acts on
it.** A single sentence restating the table's headline is not the
requirement being met. Where a table genuinely needs only a line —
a reconciliation that ties, a checklist that passes — say so and move
on; that exception is the minority, not the pattern.

**Enumerate every entity the section governs; never summarise it into
groups.** This is the second half of the same failure and it is
invisible in a section count, because a five-row table and a
twenty-one-row table both look like "the section has a table". The
exemplar lists every child in its inventory section (21 rows), every
child in its provenance register (11 rows), every child in its unit
economics (17 rows), every campaign against every placement in its
placement section (19 rows), and every paused term with its own bid and
decision (10 rows). The plan built beside it grouped 57 children into 5
inventory categories, gave placement at portfolio level only, and
tabled no paused terms at all. **A grouped summary is a finding about
the groups; the decision is taken on the entities. If a routing
decision is per child, the table has one row per child — including the
children where the answer is "no change", because a reader cannot tell
an unexamined child from an unchanged one.** Where the population is
genuinely too large to table in full, the table carries every row that
carries spend, rank, stock risk or a decision, and states the count of
rows omitted and why.

**A table cell repeating its row label carries the label, not a blank.**
Grouped tables that leave the first column empty on continuation rows
read cleanly on the page and fail 0-Y, because a blank cell is
indistinguishable from a missed one to every check and to any reader
scanning a column. Repeat the label, or mark it explicitly as a
continuation.

**When an exemplar is supplied, derive the required subsection list from
the exemplar itself, not from the plan being built.** A list derived
from the draft in hand reproduces that draft's own omissions and
certifies them as complete. Walk the exemplar's headings in order, write
that list down, and treat it as the floor.

**Depth is set by the data available, not by the minimum the rule
names.** A rule saying a section must state its diagnosis is satisfied
by one sentence and by an eleven-column table across every syntax with
persistence and spend share; where the data supports the second, the
first is an incomplete section that passed a complete-looking check.

| Required content | What this skill supplies |
|---|---|
| Family/portfolio disambiguation — shared-root arbitration across siblings, ownership formula, sibling data sourced from that sibling's own bulk, boundary-class read on conquest-style rows | Fully supplied — §1A, including the confirmed sibling-bulk data source |
| Market position — dated niche/competitor pull, price ladder, opportunity/competition scores, **named colour or segment ownership by competitor** | Fully supplied — §3's price-position and auction-density requirements; source confirmed as AsinSight, Helium10, or Cerebro |
| **Top-N keyword table — search volume, current vs. prior performance, current rank, top competitors named with their price, a stated action per row.distinct from App B, which lists every targeted keyword but carries no competitor-and-price columns.** **App B itself carries one field the Top-N table doesn't need to repeat: each row's own campaign-type footprint against what its objective requires (the writing-standard requirement above) — every targeted keyword, not just the Top-N set, since a coverage gap on a lower-volume term is exactly as real as one on a head term, just smaller in dollars.** | Fully supplied — §3's price-position requirements and §7's rank data, combined into the summary table this row specifies |
| Placement performance — **one row per campaign per placement**, carrying the modifier currently set on each, with CVR, CPC and CPA at each, which placement leaks and which converts; **followed by the per-campaign bid re-solve arithmetic** (affordable price per placement, base now → base proposed, modifier now → modifier target, staged where the correction exceeds the cap) | Fully supplied — §4's per-placement judgment and backward-solve |
| Per-syntax diagnosis — four-quadrant read with persistence, priority class, coverage, match-type build status | Fully supplied — §1B, including the four-way built/paused/zero-impression/live read |
| Per-SKU contribution and break-even ceilings | Fully supplied — §3's economic ceilings |
| Deal state, where a deal window applies | Fully supplied — §3's deal-state reporting |
| Inventory / days-of-cover, zone status, stockout risk, production status, the recovery-push mechanic, projected days-of-cover before funding a push, named and dated re-entry plans on every Yellow/Red hold | Fully supplied — §9 |
| Campaign-level verdict rollup, match-type table, a subset far above ceiling moving immediately rather than laddering, a missing-layer list | Fully supplied — §5 |
| Ranking diagnosis — this skill's own seven-state test, flagged against the account's six-state convention where that's available | Supplied, with the flag stated explicitly per the note on this ambiguity above |
| Coverage universe, gap terms (term, syntax, search volume, rank target — no bids), relevance screens on suspect terms, named declines | Fully supplied — §12 |
| Competitor intelligence, SB/SBV build with wave gates, defensive vs. offensive posture, phase gates per ad type | Data source confirmed; the account's own wave-gate thresholds are not restated here |
| Spend targets, TACoS band by objective, product posture, code-red status, a bridge sentence funding any gap via gated releases | Fully supplied — §1C |
| Advertised-SKU register, pre-stockout tapering (not a flat continue) at a defined days-to-stockout threshold | Fully supplied — §9 |
| The lever-summary and deployment sequence, split by deal-contamination, each checkpoint naming what's judged and against what threshold, the workbook's own validation-gate pass count stated on the plan directly | Fully supplied — §3, §4A |
| Negation with a relevance gate, an own-catalog scan, drift clusters with a reverse test confirming genuine drift before acting on it, declared interim thresholds, and harvest criteria | Partially supplied — the relevance gate is this skill's own; interim thresholds are the account's |
| Recommendations to Brand Management | Fully supplied — the Brand Management findings register, with named categories |
| Oversight cadence, prediction scoring before new decisions, deploy path, any settle-window collisions named and ruled | Fully supplied in shape — §14; the account's own weekly rhythm is its own |
| The six-level waterfall, precedence rule, on the unit-economics section's numbers exactly — never a second margin source | Fully supplied — §1A |
| Reconciliation — data-completeness stamp, named gaps, what the data couldn't show, reversal conditions, a cross-agreement audit | Fully supplied — the data conditions register and validation gate |
| Expected outcome, modelled on the final decided file's own numbers — a before/after table (spend, orders, ACoS, CPA, contribution at both margin bases, TACoS) — never a separate estimate; where the plan stops short of a stated target, what closing that gap actually requires | Fully supplied — §3, §5, and the modelling-assumption check |
| Risks and what would falsify this plan, with a dated check on each | Fully supplied — this skill's own reversal-condition requirement, collected in one place |
| Decisions requested — specific, numbered, never a closing "let me know your thoughts" | Fully supplied as a category |
| Every campaign, with the CPC ceiling column labeled as such and a note that CPA is not measured against it directly, paused duplicates flagged | Fully supplied — §3, §1 |
| Every targeted keyword, syntax labels verified accurate | Fully supplied — §1 |

**Every row of the table above is checked against the delivered
document, not against this file.** Each row's right-hand column names
where the *rule* lives in this skill; that is not evidence the
requirement reached the plan. On a real build every row of this table
had a skill section behind it and four of its requirements — the
before/after outcome table, the two-wave execution register with a
prediction per action, the Brand Management recommendations table, and
per-child economic ceilings — were absent from the delivered document
entirely, while the sections that should have carried them were present
and read as complete. **Before delivery, walk this table row by row and
name the subsection of the plan where each requirement actually
landed.** A row that cannot be pointed at a location in the document is
an unmet requirement, whatever this file says supplies it.

**Risks/falsification and decisions-requested are always the plan's
final two pieces of content, in that order, on every plan** — not
conditional on whether the plan happens to be a revision. A first-time
plan needs a stated falsification test and a specific ask just as much
as a corrected one; neither is a revision artifact. Their exact section
numbers follow whichever real structure governs this product, per the
note above — what's fixed is that they come last, not what number they
carry.

**A "what changed since the prior version" section is not part of this
standard skeleton and is not produced by default.** Where refinement mode
(Step 0) is genuinely revising a prior plan, state what changed as part
of that mode's own output — a table of prior statement, current finding,
and effect on the plan is one reasonable way to do that — but this is
scoped to the refinement itself, never treated as permanent front matter
every plan must carry regardless of whether anything preceded it.

**If a section has nothing to report for this product this cycle**, it
stays in the document with a stated reason, per the rule below. **A
genuinely new section can be added** the same way — labeled as an
addition (e.g. "9A — Aged-Stock Risk Tier"), never silently folded into
the numbering above.

**Every section carries the actual data it's reasoning from — the real
table or breakdown, not a compressed prose summary of a conclusion with
the working hidden.** This applies uniformly across the whole document —
every section, regardless of whether it was part of this skill's
original build or added in a later pass, carries the same depth
requirement. A section doesn't earn lighter treatment by being
long-standing, and a newly-added section doesn't earn special attention
the rest of the document lacks; the standard is the same everywhere,
checked the same way everywhere. A syntax-diagnosis section states the
per-syntax numbers in a table, not "syntax performance was mixed." A
ranking-diagnosis section shows each keyword's state, its rank arc, and
its sufficiency-stop status in a table, not a paragraph asserting a
verdict. Where the underlying data is genuinely thin — a new product
with three weeks of history, a syntax with two keywords in it — the
section says so plainly and shows the thin table as it stands, rather
than being padded with prose to read as more complete than the data
supports. This is the same honesty standard as "What this skill cannot
honestly produce at scale" above, applied section by section: a visibly
thin table is honest; a full-looking paragraph built on the same thin
data is not.

**Every major data table carries two things beyond the numbers
themselves: a synthesis and, where a visual would surface the pattern
faster than the table, a paired chart.**

- **"What this table decides"** — a short, bulleted synthesis
  immediately following the table, connecting its evidence to a decision.
  Not a restatement of the table's contents; a table showing per-syntax
  spend and CVR is followed by which syntaxes are rank assets to protect,
  which are leaking, and what that implies — the line a reviewer would
  otherwise have to draw themselves. Required after every major table in
  the document, not just some of them.
- **A paired visual wherever a trend, a comparison across categories, or
  a distribution is genuinely easier to read as a chart than a table** —
  a rank arc over time, a placement or SKU comparison, a discount-depth-
  vs-conversion read. Conventions: the chart's title states the finding,
  not a caption number ("Rank trend, eight largest assets" with the
  actual pattern visible, not "Figure 3"); data labeled directly on the
  chart rather than requiring a legend lookup; a shaded reference band
  where a threshold matters (a top-10 band on a rank-trend chart). A
  table without a chart is not a defect by itself — plenty of tables are
  clearest as tables — but a trend or comparison buried only in table
  form, where a chart would make the finding legible at a glance, is a
  missed opportunity to make the same point better.

---

## Companion workbook

If a workbook exists or gets built alongside this plan:

1. **One control table of every headline fact stated more than once.**
   Generate every mention in the plan from that table; when a fact
   changes, update the table once and regenerate every mention.
2. **Regenerate the paragraph containing a changed number, don't patch
   inside it** — a find-and-replace inside hand-written prose is how stale
   framing survives a correction.
3. **Cross-check every headline number the workbook computes against what
   the plan states, every round either document changes** — not only
   before final delivery.

---

## Output

One document, final draft, per §14. If a workbook exists, deliver the
cross-check result alongside it.

**This skill does not invent product-specific campaign-structure or
targeting conventions** — a named conquest-posture grouping scheme, a
particular PAT-target classification, or any other structure specific to
one product's competitive situation. Those are stated by the plan for
that product, drawing on whatever precedent or convention the account
already uses; this skill supplies the universal decision logic that
applies once those structures exist, not the structures themselves.
