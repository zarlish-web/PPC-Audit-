# amazon-product-analysis — consolidated framework

One reusable skill that makes Claude run a deep, data-driven, decision-grade analysis of any Amazon product: economics and profitability, inventory and variations, keyword research, PPC campaign / keyword / placement decisions, competitor and market positioning, listing and offer, events (deals, LTSF), validation, and a written decision trail.

It consolidates 18 existing skills (decision engines, plan builder, decision reasoning, placement-first optimisation, workbook builder, STR audit, keyword master, SQP roll-up, phasing, objective correction, quick audit, action plan, campaign builder, inventory checkup, LTSF dossier, AdInsight competitor method) and the lessons of the B6 engagement into one rulebook. Every place the sources disagreed is resolved once in `references/13-source-map-and-conflicts.md`.

## How to give it to Claude

| Where | How |
|---|---|
| Claude.ai (web/desktop) | Settings → Capabilities → Skills → upload `amazon-product-analysis.skill` (the zip). Claude loads it automatically when a request matches. |
| Claude Code | Copy the `amazon-product-analysis/` folder to `~/.claude/skills/` (personal) or `.claude/skills/` in a repo. |
| A Claude Project or a single chat | Upload `AMAZON_PRODUCT_ANALYSIS_FRAMEWORK.md` (everything in one file) as project knowledge or an attachment, and say "follow the framework". |

Then ask naturally, e.g. *"Run a full analysis of B6 using the attached files"*, *"Audit the engine's decisions for Satin 4PC against the competition"*, *"What should we do with the aged King Grey stock?"* — and attach what you have. Claude will first send the intake request (`templates/intake-request.md`) listing anything missing and the owner settings to confirm.

## What you get

- A **decision document** (summary → current state → rules → findings per area → competitive landscape → tests → exceptions → next steps → engine fixes).
- A **decision workbook** (every campaign and every search term with a decision and its trail: Input → Metric → Logic → Decision → Action → Expected outcome → Validation; plus push plan, placement, variation & stock, guardrails, competitor tabs, exceptions, validation plan, checks).
- A **quality gate** that must pass before anything is presented.

## Files

| File | Content |
|---|---|
| `amazon-product-analysis/SKILL.md` | Workflow (phases 0–10), principles, owner-settings defaults, master decision order, output contract, quality-gate summary |
| `references/01-intake-and-data.md` | Every input, fields, windows, joins, reconciliation, halt rules |
| `references/02-metrics-and-formulas.md` | ~90 metrics: definition, formula, source, validation, thresholds, pitfalls |
| `references/03-profitability-and-guardrails.md` | Goal gate, per-SKU economics, break-even, ceilings, spend limits, deals, TACoS (monitor) |
| `references/04-inventory-sku-ltsf.md` | Cover, zones, variation routing, backup switch, LTSF maths and ladder |
| `references/05-keyword-research.md` | Universe, classification, tiers, relevancy scorer, SQP, ownership, keyword decision order, negation, harvest, phasing |
| `references/06-campaign-ppc-decisions.md` | Objectives, campaign classes, decision set, push qualification, ranking states, non-ranking rules, levers |
| `references/07-placement-and-bidding.md` | Placement-first diagnosis, push pricing, mix fix, backward-solve, DSTR → clicks → budget, fixed-bid trial |
| `references/08-competitor-market.md` | Data pulls, rival profiles, market view, keyword landscape, engine-vs-landscape verdicts, ASIN targeting, influence rules, gaps, SB/video test |
| `references/09-listing-positioning.md` | Four-quadrant diagnosis, listing audit, offer and price positioning, review-theme method |
| `references/10-longitudinal-validation.md` | Impact ledger, execution check, grading, escalation, validation plan |
| `references/11-exceptions-and-failure-modes.md` | Where not to automate; consolidated failure register (with B6 cases) |
| `references/12-writing-and-deliverables.md` | Writing standard, trail format, deliverables, full quality gate |
| `references/13-source-map-and-conflicts.md` | Which rule came from which skill; every conflict and its resolution |
| `templates/` | Intake request, report outline, workbook spec, 10 worked decision trails |
| `examples/b6-case-study.md` | End-to-end teaching case |
| `OWNER-DECISIONS.md` | Defaults the framework applies where no source rule exists — confirm or change per product |

## Updating it

Change a default in one place: the owner-settings table in `SKILL.md` and the matching row in `references/13-…`. Record product-specific rulings in the analysis itself, not in the skill.
