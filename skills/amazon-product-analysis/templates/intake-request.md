# Template — intake request

Send the message in Part 1 in **one batch** before any analysis. Do not start partially: wait until every item is received or confirmed "doesn't exist / not needed this cycle". Record each answer in the Part 2 checklist and keep it with the deliverables. [PB, QA, SR]

Fill the `<…>` fields before sending. Delete a group only when the scope rules it out (a one-area request still needs groups A–C and G, because every area depends on economics, inventory and events).

---

## Part 1 — message to send

> **Subject: Inputs needed for the `<product / parent ASIN>` analysis (`<marketplace>`)**
>
> To analyse `<product>` properly I need the files and answers below, all in one go. Please send each as the raw export (not a filtered or re-saved copy), keep the original column headers, and tell me the date range of each. If something doesn't exist, just say so — I'll record it as a gap rather than guess.
>
> **A. Advertising data**
> 1. **Sponsored Products bulk file** (Bulksheets 2.0, all tabs, including paused and archived items) for three windows: **last 7 days**, **the 7 days before that**, and **the last 60–90 days**. `.xlsx`.
> 2. **Search term report** (Sponsored Products), daily rows, **last 60–90 days**, all campaigns in the portfolio(s). `.xlsx`. Please give me the exact portfolio name(s) as they appear in the report.
> 3. **Placement report** (campaign × top of search / rest of search / product pages) for **30 and 90 days**, and the **Sponsored Products targeting report** (for top-of-search impression share) for the same windows. `.xlsx` or `.csv`.
> 4. **Advertised product report** for the same windows (which child ASIN/SKU each ad served), so I can check which variation actually earned each result.
> 5. **Sponsored Brands / video / Display** campaign reports (30 and 90 days), if any run on this product.
> 6. If you use a dashboard (e.g. Command Center): the product-level ad spend, sales and orders **by day for the last 90 days**, and any **shared campaigns** that advertise other products too.
> 7. **Last cycle's outputs**, if there was one: the decision workbook or plan, the action log / change list with dates it was uploaded, and any reviewer marks or owner overrides.
>
> **B. Economics**
> 8. **Sellerboard (or equivalent) per SKU/colour, last 30 days**: units, price, refunds, Amazon fees, product cost, storage, and **profit per unit before ads**. `.xlsx` or `.csv`.
> 9. Any **price change, fee change, packaging change or new product cost** coming up, with dates.
> 10. **Business report** (child-ASIN detail, weekly, last 90 days): sessions, units, total sales — for organic share and TACoS.
>
> **C. Inventory and variations**
> 11. **Inventory per SKU** (full export, not the variation page): Available, reserved, inbound with **dated confirmed arrivals**, transfers, units in production; units sold per day over **7 and 30 days**; days of cover. `.xlsx`.
> 12. For each size (or syntax): the **preferred** variation for ranking, the **backup** variation, and any **clearance** colour you want pushed through discovery. Please list them — I won't derive them.
> 13. If any stock is aging: the **inventory-age export (all age brackets)**, the latest **long-term storage fee charge file**, and cubic feet per unit per SKU.
>
> **D. Keywords and rank**
> 14. **Master keyword list** (no older than ~30 days): search volume, relevancy, syntax/root, categorisation, indexed yes/no, currently targeted yes/no.
> 15. **Search Query Performance** (Brand Analytics) for the parent or all child ASINs, **last 13 weeks** (and monthly if you have it), raw export.
> 16. **Target ranks**: target organic rank and target date per search term.
> 17. **Rank history, daily, at least 1 month (ideally 3)** — organic and sponsored rank per term (Data Rova, Data Dive, Helium 10 or your rank crawl).
> 18. Your **syntax taxonomy** (if you have one) and every spelling of the **brand name** shoppers use.
>
> **E. Competitors**
> 19. The **competitor roster**: ASIN → brand, and which you consider aspirational / beatable.
> 20. **Competitor exports, dated**: ASINsight / AdInsight per competitor, Data Dive niches, Helium 10 Cerebro/X-ray multi-ASIN pulls, and any price / BSR / review movement brief. Tell me which mapped competitors have **no** export.
>
> **F. Listing**
> 21. The **live listing**: title, bullets, backend search terms, main and secondary images, A+ content, video, price, coupon, rating and review count — as they are today.
>
> **G. Calendar**
> 22. **Deals and events**, past 90 days and next 90 days: dates, deal type, deal price, deal fees; Prime Day / Black Friday plans; planned price or listing changes.
>
> **H. How you want it built**
> 23. Campaign naming convention and any structure template or example I should follow.
> 24. Output format: Excel + Word, Google Sheets + Docs, or both.
>
> **Questions about how you want the product run** (I'll use the house default in brackets only if you confirm it):
> 1. **Goal for this product**: Growth/Scale, Mixed (rank some terms, profit on the rest), Profit-First, or Clearance/LTSF? *(No default — this decides whether any ranking spend is allowed.)*
> 2. **Is this an analysis** of what exists, or a **plan** of what to do next? From scratch, or a refinement of an existing plan?
> 3. **Spend limit** for the product: $ per day or week, and any **event exceptions** (dates and how much). *(No default.)*
> 4. **Margin rule**: minimum margin after ads (e.g. "above 10%"), and any time-boxed exception. *(No default.)*
> 5. **Margin source**: Sellerboard profit per unit before ads, per SKU, last 30 days, deal price during deals? *(Default: yes.)*
> 6. **Ranking ceiling**: 2 × break-even cost per click on the top-of-search price? Any named term where you'd allow more for a set time? *(Default 2×; alternative: a flat account cap ~$8–9.)*
> 7. **Push step**: up to +30% a day while a pushed term isn't holding the top? *(Default: yes.)*
> 8. **TACoS**: do you want a numeric TACoS target, or monitor only? *(Default: monitor only.)*
> 9. **Bidding strategies**: leave existing ones as they are; new campaigns dynamic down-only; fixed bids only through a trial you approve? *(Default: yes.)*
> 10. **Amazon suggested bids**: never used to set prices? *(Default: not used.)*
> 11. **Stock zones**: Green ≥60 days of cover, Yellow 21–59, Red <21, and "stock-out before the next arrival" counts as Red? *(Default: yes.)*
> 12. **Zero-order rule**: ≥20 clicks and 0 orders → reduce (relevant, with a live exact owner), fix list (relevant, no live exact owner) or block (irrelevant or another product type); exact ranking and brand terms are never negated? *(Default: yes.)*
> 13. **Harvest**: ≥3 orders at or below break-even ACoS with no exact owner → build an exact campaign and negate at the source? *(Default: yes.)*
> 14. **Approvals**: which changes need your sign-off before upload (default: structural changes, bid moves >25% outside an approved push plan — the plan's own +30%/day steps are covered by approving it — budget moves >$50/day, any failed check, terms with search volume ≥ 500).
> 15. **Rules that need your confirmation before first use on this product**: defensive-campaign ladder and competitor-presence allowance; conquest entry/exit; harvest bar; discovery count basis (keyword vs root cluster); how a ranking push ends after target is held; graded raise tiers for non-ranking terms; a $0.50 minimum bid.
> 16. **Portfolios in scope**: this portfolio only, or also a sibling portfolio that buys the same head terms? Marketplace: US or CA (never mixed)?
>
> Thanks — once I have these I'll confirm what's in, what's missing, and which decisions each gap blocks before I start.

---

## Part 2 — receipt checklist

Status: **Y** received · **N** missing (named gap) · **N/A** confirmed not applicable. "Blocks" = what cannot be decided without it.

| # | Item | Window | Format | Status | Received on | File name | Freshness / check | Blocks if missing |
|---|---|---|---|---|---|---|---|---|
| 1 | SP bulk ×3 windows | 7 d / prior 7 d / 60–90 d | xlsx | | | | every tab listed; campaign count vs dashboard | all campaign decisions |
| 2 | Search term report | 60–90 d daily | xlsx | | | | portfolio name exact; min/max date | keyword decisions, harvest, negatives |
| 3 | Placement + targeting reports | 30 / 90 d | xlsx/csv | | | | campaign grain | placement, mix fix, ceilings |
| 4 | Advertised product report | same | xlsx/csv | | | | SKU per ad over window | SKU provenance, every verdict |
| 5 | SB / SBV / SD reports | 30 / 90 d | xlsx/csv | | | | — | brand-format decisions |
| 6 | Dashboard product totals, shared campaigns | 90 d daily | csv | | | | spend tile vs rows | spend reconciliation, event baseline |
| 7 | Prior cycle outputs | last cycle | xlsx/docx | | | | upload dates known | grading, escalation (else first cycle) |
| 8 | Sellerboard per SKU | 30 d | xlsx/csv | | | | ≤45 days old | break-even, every price |
| 9 | Price/fee/COGS changes | next 90 d | text | | | | — | future ceilings |
| 10 | Business report | 90 d weekly | csv | | | | — | organic share, TACoS |
| 11 | Inventory per SKU | snapshot + 7/30 d pace | xlsx | | | | full export, unfiltered | stock gates, pushes |
| 12 | Preferred / backup / clearance | — | list | | | | user-supplied | routing, colour switches |
| 13 | Age export, LTSF charge, cu ft | latest | xlsx | | | | all brackets | clearance decisions |
| 14 | MKL | ≤30 d old | xlsx/csv | | | | syntax verified | keyword universe |
| 15 | SQP | 13 weeks | csv | | | | market once, brand summed | four-quadrant, targets |
| 16 | Target ranks | — | csv | | | | — | push premium, HOLD RANK |
| 17 | Rank history | ≥1 month daily | csv | | | | <1 month → ranking out of scope | ranking verdicts |
| 18 | Syntax taxonomy, brand variants | — | list | | | | — | classification, brand protection |
| 19 | Competitor roster | — | list | | | | brands resolved | competitor sections |
| 20 | Competitor exports | dated | xlsx/json | | | | coverage n of mapped | landscape, ASIN targets |
| 21 | Live listing | today | text/images | | | | — | listing checks, relevancy |
| 22 | Deal / event calendar | −90 / +90 d | text | | | | — | event gate, windows |
| 23 | Naming / structure template | — | any | | | | — | builds |
| 24 | Output format | — | answer | | | | — | delivery |

### Owner settings — answers

| # | Setting | Answer | Default used? (Y/N) | Date confirmed | Notes |
|---|---|---|---|---|---|
| 1 | Product goal | | | | undeclared → treat as Profit-First for the ranking gate |
| 2 | Analysis / plan; scratch / refinement | | | | |
| 3 | Spend limit + event exceptions | | | | |
| 4 | Margin rule + exceptions | | | | |
| 5 | Margin source | | | | |
| 6 | Ranking ceiling (+ named raises, end dates) | | | | |
| 7 | Push step | | | | |
| 8 | TACoS target | | | | |
| 9 | Bidding strategy policy | | | | |
| 10 | Suggested bids | | | | |
| 11 | Stock zones | | | | |
| 12 | Zero-order rule | | | | |
| 13 | Harvest rule | | | | |
| 14 | Approval thresholds (default SV ≥ 500) | | | | |
| 15 | Provisional rules confirmed (list each) | | | | |
| 16 | Portfolios, marketplace | | | | |

### After receipt (before analysis)
1. List every sheet in every file; read each; mark READ-FULL / READ-PARTIAL / NOT-RELEVANT / NOT-OPENED. [WB]
2. Reconcile: bulk vs dashboard spend; Sellerboard units vs orders; inventory on-hand − available − reserved (gap >5 units → verify at source). [PB]
3. Reply once with: what's in, what's missing, which decisions each gap blocks, and any answerable question still open (ask once; don't log an answerable gap as "next cycle"). [PB]
