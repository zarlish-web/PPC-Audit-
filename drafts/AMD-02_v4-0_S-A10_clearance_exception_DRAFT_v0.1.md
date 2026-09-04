# AMD-02 — Amendment to Master PPC Decision Criteria System v4.0, §8.1 scenario S-A10

**Target:** Master PPC Decision Criteria System v4.0 → §8.1 Product-Level Scenarios (S-A)
**Status:** DRAFT v0.1 — not ratified
**Raised:** 4 September 2026
**Reason:** closes the S-A10 vs SOP-27 R2 conflict, which SOP-27 itself has been carrying as an open amendment request

---

## 1 · The problem, already documented in your own corpus

SOP-27 §10.5 lists ten items it needs and v4.0 does not carry. Item **AM-1** states this conflict in full:

> *"v4.0 Section 8.1 'Product-Level Scenarios (S-A). The posture every keyword inherits' scenario S-A10 puts CONSTRAINED, LTSF-burdened products on a profit-only posture and routes LTSF velocity requirements to deals and pricing rather than to PPC subsidy. Rule R2 authorizes allowable ad cost per unit that can exceed the unit's own contribution. **Both are correct in their own frame, and v4.0 carries no rule for a unit that is in both.** R5's quarantine is the operating separation this SOP uses; **v4.0 should state it or reject it.**"*

This amendment states it.

## 2 · The current text

§8.1, scenario S-A10:

| ID | Condition | Posture |
|---|---|---|
| S-A10 | CONSTRAINED earning class (LTSF-burdened, low ceiling) with any above-BE spend | Profit-only posture: no ranking pushes; Conversions and Defensive objectives only; LTSF velocity requirements route to deals/pricing (P1.4/P3.5), not to PPC subsidy |

## 3 · Why it conflicts

An aged product on a clearance objective is, by definition, in both frames at once:

- It is **CONSTRAINED and LTSF-burdened**, so S-A10 says profit-only, no PPC subsidy.
- It is running **above break-even by design under R2**, which is the whole mechanism by which advertising clears aged stock.

The same conflict exists between `decision_framework.md` §8.3 and `ppc-decision-reasoning` §4 — see AMD-01. **It is one disagreement appearing in two places**, and the 4 September 2026 ruling settles both the same way: forward cash governs, PPC subsidy on aged stock is authorised, capped, dated and logged.

## 4 · Proposed change

Add a carve-out to S-A10. The scenario is not deleted — it stays correct for every CONSTRAINED product **not** on a clearance objective.

| ID | Condition | Posture |
|---|---|---|
| S-A10 | CONSTRAINED earning class (LTSF-burdened, low ceiling) with any above-BE spend, **and not carrying a clearance objective** | Profit-only posture: no ranking pushes; Conversions and Defensive objectives only; LTSF velocity requirements route to deals/pricing (P1.4/P3.5), not to PPC subsidy |
| **S-A10a** | **CONSTRAINED, LTSF-burdened, and carrying a declared clearance objective** | **PPC subsidy authorised under SOP-27 R2.** Allowable ad cost per unit may exceed the unit's own contribution, capped at the forward-cash ceiling, dated, and logged against the charge avoided. Ranking pushes remain barred. Deals and pricing (P1.4/P3.5) route **in parallel**, never instead of the PPC push |

## 5 · What decides which one applies

The declared objective, and nothing else. A product is on S-A10a only when the LTSF declaration has put it on a clearance objective. Absent that declaration, S-A10 governs unchanged.

This keeps the profit-only posture doing its real job — stopping a CONSTRAINED product being pushed on rank or scaled on hope — while removing the reading that also stops the one thing that clears the stock.

## 6 · What does not change

- **Ranking pushes stay barred** on S-A10a. The carve-out authorises clearance subsidy, not rank spend.
- **R5's quarantine** remains the operating separation, exactly as SOP-27 already uses it.
- Every other S-A scenario.
- The requirement that above-BE spend is **capped, dated and logged**.

## 7 · Flagged for the ratifier — points I interpreted

1. **A new sub-scenario rather than an edit to S-A10.** SOP-27's AM-1 asks v4.0 to "state it or reject it" without saying which shape. A carve-out preserves S-A10 for the non-clearance case, which seemed safer than rewriting a rule other SOPs cite — SOP-24 §8.1 and SOP-26 both reference S-A10 directly, and SOP-32 references it too. **Those three references should be checked before ratification**, since they may assume the un-carved version.
2. **The ID `S-A10a`.** Invented for readability. v4.0's own numbering convention may prefer something else.
3. **AMD-01 and AMD-02 are one decision in two files.** Ratifying either alone leaves the corpus still contradicting itself.

## 8 · What this unblocks

SOP-27 has been carrying AM-1 as an open request. Closing it lets SOP-27's R2 and R5 stand on a stated rule rather than an operating workaround, and stops the next reader deriving "no PPC subsidy on aged stock" from a document that is meant to authorise exactly that.

---

*Inspiratek & Ecotero LLC · Confidential · DRAFT — not ratified*
