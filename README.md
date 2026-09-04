# PPC Liquidation Skill Set

Everything needed to run an Amazon PPC clearance audit on one product, the same way, every time.

Built from a review of the SOP corpus, two live plan documents, a live decided bulk, and one full run on a real product — the Hanging Closet Organizer — whose findings then corrected the skill twice.

---

## What's here

```
skills/ltsf-liquidation-audit/     THE SKILL — install this
├── SKILL.md                       the 8-step run
└── references/
    ├── prompts.md                 exact prompts, copy-paste, one per step
    ├── decision-framework.md      steps 1–5: inputs, corrections, ceiling, pace, gate
    ├── campaign-builds.md         step 7: build classes, bid tiers, separation, staging checks
    ├── output-format.md           step 8: document spine, writing standards, validation gate
    └── worked-example.md          a real run including where it went wrong

drafts/                            THE SOPs — review and ratify
├── SOP-27_P15_Reach_Layer_Campaign_Builds       new procedure: building clearance campaigns
├── SOP-12_P13_Dated_Liquidation_Campaign        the receiving procedure #12 was missing
├── Product_Audit_Format_Standard                merged format from the ranking + clearance plans
└── HC_Liquidation_Audit_04Sep2026               the first live run, as the reference output
```

---

## How to use it

**To run an audit.** Install the skill (`ltsf-liquidation-audit.skill`), then ask for a clearance audit on a product. It triggers on its own. Step 0 sends the intake list; nothing starts until the inputs arrive or their absence is confirmed.

**To run it manually without the skill.** Work through `references/prompts.md` in order — §0 through §8, plus §9 if the lane closes. Each prompt is written to be pasted as-is.

**To understand a decision it made.** `decision-framework.md` for anything about the ceiling, pace or the gate. `campaign-builds.md` for anything about structure or bids.

**To check work before shipping.** The validation gate at the end of `output-format.md`. Sixteen checks; the first six are traceability and are the ones that fail quietly.

---

## The eight steps

| Step | What it does |
|---|---|
| 0 | Intake — 25 inputs, each with why it's needed |
| 0b | Ask before assuming — contradictions go back to whoever supplied the data |
| 1 | Read the declaration — seven fields, none derived |
| 2 | **Context corrections** — find what makes the raw numbers misleading, *before* any verdict |
| 3 | Build the ceiling — computed, never chosen |
| 4 | Required pace — market click price read at the volume needed, not the volume bought |
| 5 | **Clearability gate** — can traffic clear this at all? Open, split, closed or unmeasured |
| 6 | Decide the existing account |
| 7 | Build new campaigns — two layers, six classes, separation rules |
| 8 | Write it up, then run the validation gate |

Step 2 and step 5 are where the value is. Step 2 stops an audit being confidently wrong. Step 5 stops money going into stock that advertising cannot move.

---

## The rules that came from real errors

Each of these exists because something went wrong on a live run.

**Ask rather than resolve.** A contradiction is a question for whoever prepared the data, not a puzzle to solve alone. Ask when the answer touches the ceiling, the pace, the archetype or the disposition. Mark blocked branches blocked — a blocked branch is visible, an assumed one is not.

**Never silently resolve a vocabulary difference.** *Liquidate*, *aged*, *clear*, *terminal*, *floor* carry house meanings. Reading one in its ordinary sense produced a decision request for a conflict that did not exist.

**Prefer counts over derived fields.** A count is an observation. Days-on-hand, months-to-clear and break-even are calculations that inherit every error beneath them — and they are what feed the ceiling.

**Staleness is a property of the file, not the field.** One stale field means no clean fields, only unchecked ones. Verify two or three against independent sources; quarantine the file if any fails.

**Charge size never overrides the clearability gate.** The largest charge in a portfolio is often the least clearable stock in it, because low velocity is what aged it.

**The avoided charge is counted over a bounded window.** Counting the whole projected hold inflates the ceiling most on the stock least able to justify it.

**Count the charge once.** It sits either in the fees line reducing contribution, or added back as avoided — never both.

---

## What the first run found

On a product carrying 233 charge-bearing units and $849.89/month:

- **The two child SKUs needed opposite decisions.** One had roughly a third of the other's allowable ad cost, and was taking 64% of the spend.
- **11% of enabled budget could spend.** The lane was impression-constrained — nine times short — not budget-constrained.
- **52% of budget sat in campaigns that could not serve.** An 18-campaign expansion book spent about $20 in nineteen days.
- **The cheap wide lanes were the only ones working, and were starved** — one at 96% of a $5/day budget.
- **Exact took 58% of keyword spend at the worst cost per order** in the account.
- **A prior plan's break-even line did not exist**, and the error was inherited from a stale source file rather than invented — so correcting the plan alone would have fixed nothing.

---

## Status

| Item | State |
|---|---|
| The skill | Drafted, run once on live data, corrected twice from it |
| SOP-27 P15 | Draft v0.4 — not ratified |
| SOP-12 P13 | Draft v0.1 — not ratified |
| Format standard | Draft v0.1 |
| Counterparty procedures at #29, #38, #26 | Not started |

**Open decisions** are listed at the end of each draft. The ones that block execution: a budget cap for the reach layer, a deadline for an unmeasured lane, and the conflict between the criteria system's profit-only posture for LTSF-burdened products and this lane's allowance to spend against avoided charge.

---

*Inspiratek & Ecotero LLC · Confidential*
