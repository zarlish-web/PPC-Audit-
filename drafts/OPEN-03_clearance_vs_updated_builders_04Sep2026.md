# OPEN-03 — three conflicts between the clearance skill and the updated builders

**Raised:** 4 September 2026
**Between:** `inspiratek-clearance-audit` (this repo) and the updated `ppc-plan-builder` / `ppc-workbook-builder`
**Status:** OPEN — not resolved, not worked around. Needs a ruling.

The updated builders now carry clearance rules natively that they did not carry when this skill was merged. Most of it agrees. **Three things do not**, and each changes what ships on the Quilt Set.

Per the standing instruction — *"if there is any contradiction… instead of assuming it's better to ask"* — none of the three has been applied or silently reconciled.

---

## 1 · Is PPC the clearance lever, or is the deal?

**The updated builders say the deal is:**

> *"Deals are also this account's designated clearance mechanism for aged and terminal-tagged stock — **not a PPC lever.** Where a SKU carries an LTSF or terminal tag, the deal calendar is the primary tool for moving it, and PPC's role is **supporting visibility into an already-scheduled clearance window, never substituting advertising spend for the discount itself.**"*
> — `ppc-plan-builder` §1860, and identically in `ppc-workbook-builder`

**This skill says PPC is**, on your ruling of 4 September:

> *"On a liquidation product, PPC is the lever that moves the stock. Spending a little beyond profitable is accepted, because the charge avoided is worth more than the margin given up."*

### They may be reconcilable, or they may not

A reading that holds both: **the deal sets the pace, PPC buys the visibility that makes the deal convert** — and "never substituting ad spend for the discount" means *don't advertise your way out of a needed markdown*, not *don't advertise*. Under that reading this skill's forward-cash push is legitimate **inside a scheduled deal window** and much harder to justify outside one.

A reading that does not hold both: PPC is a support act on aged stock, full stop, and a $762/day advertising programme is the wrong instrument regardless of what the ceiling permits.

### What hangs on it

The Quilt Set plan asks for **$762/day of advertising** on a product whose deal calendar is already active (D120, 31 Aug – 13 Sep). Under the first reading that is correct and should be sequenced tight to the deal window. Under the second it is over-built, and the recommendation should be *more deal depth, less advertising*.

**This is the biggest open question in the whole plan and it is not a detail of sizing.**

---

## 2 · Semi-relevant keywords never open on a clearance goal

**The updated builders:**

> *"**Clearance/LTSF** — highly-relevant tier only, **permanently**, and at the specific bid/placement treatment named in the table below. The goal here is selling through what's already on hand, not building rank on inventory the product is exiting — **semi-relevant never opens**, and highly-relevant itself launches deliberately cheap."*
> — `ppc-plan-builder` §2A

**The Quilt Set plan opens four semi-relevant lanes:**

| Campaign | Budget | Keywords | Why it is semi-relevant |
|---|---|---|---|
| SL-QS-SP-PHRASE-XCAT | $29/day | 13 | comforter, duvet, bedding-set, blanket |
| SL-QS-SP-BROAD-XCAT-ES | $24/day | 21 | cross-category plus Spanish |
| SL-QS-SP-PHRASE-ES | $16/day | 7 | Spanish |
| SL-QS-SB-PHRASE-XCAT | $14/day | 15 | cross-category, Sponsored Brands |
| **Total** | **$83/day** | **56** | **$2,490/month — 11% of the ask** |

The plan's own defence was that the cross-category lane indexes 9.41× on purchases-per-impression and carries a 35% refund kill-switch. **The builders do not offer that as an exception.** "Permanently" and "never opens" are unusually absolute language for this corpus, which suggests it was written deliberately against exactly this argument.

**Note that this points the same way as the catalogue check.** Stripping Twin XL and California King was you removing terms for products we do not sell; this rule would remove terms for *categories we are not in*. The second is a bigger cut and rests on a rule, not on a catalogue fact.

---

## 3 · Placement modifiers on a clearance goal: none

**The updated builders' launch table:**

| Goal | Bid | Placement |
|---|---|---|
| Growth/Scale | Middle of suggested range | 100% Top-of-Search, from launch |
| Profit-First | Lower end of suggested range | 100% Top-of-Search, from launch |
| **Clearance/LTSF** | **Lower end of suggested range** | **None** |

**Where the Quilt Set stands:**

- **New builds already comply** — all 54 placement rows are at 0%. No conflict.
- **The existing account does not** — 37 of 1,341 placement combinations carry a +10% to +30% premium, each justified by that campaign's own conversion data.

The 37 premiums were set on a cost argument, which this skill authorises and which the ranking ban does not touch. The builders' table appears to bar them outright on a clearance goal.

**Narrow question:** does "Placement: None" govern only *new Exact launches* — the section that table sits in — or every campaign on a product carrying the clearance goal? If the former, there is no conflict at all and the 37 stand.

---

## What has been absorbed with no conflict

| From the builders | Status |
|---|---|
| **Aged/LTSF SKUs run forward-cash economics, not CM2. COGS never enters a live decision column on aged stock** | Already this skill's rule. The builders now carry it natively, which strengthens AMD-01 and AMD-02 rather than replacing them — those amend `decision_framework` and v4.0, which are different documents |
| **A fixed charge divided by few units is not a unit cost** | **New. Absorbed into `data-traps.md`.** Storage divided across low-volume children read as thirteen children losing money, one at −$59.53; on variable fees every one was positive at $5.32–$24.04. It nearly blocked advertising on 1,051 units holding $9,907 of forward cash |
| **Deal-state and clean-state CM2 computed separately, never blended** | Consistent with, and sharper than, this skill's no-clean-window rule. The builders say compute both and keep both; this skill says name the longest deal-free run. Both, not either |
| **Clearance/LTSF never reaches the product-goal gate for ranking** | Matches the objective re-tag exactly |
| **Rank trend dropped entirely from the read on Clearance/LTSF; inventory and revenue lead, read as recovery-per-unit against the declared clearance timeline** | Matches, and gives a cleaner name for what this skill calls cost per unit cleared |
| **Flat absolute sanity ceiling ~$8–9 per click, which a SKU's own CM2 may tighten but never loosen** | No conflict — the Quilt Set's highest bid is $1.10 |

---

## What is needed

| # | Question | What changes on the answer |
|---|---|---|
| **1** | On aged stock, is PPC the lever or the support act? | The entire $762/day ask, and whether the recommendation should shift toward deal depth |
| **2** | Does "semi-relevant never opens" bind here, or does the 9.41× index earn an exception? | Four campaigns, $83/day, 56 keywords |
| **3** | Does "Placement: None" govern the whole clearance product, or only new Exact launches? | 37 existing placement premiums |

Until these are answered the Quilt Set package stands as built, with all three flagged in the plan rather than resolved inside it.

---

*Inspiratek & Ecotero LLC · Confidential · OPEN — not ratified*
