# Linen — building the SB and SD campaigns by hand

**10 September 2026 · DECOLURE Linen Blackout Curtains**

SP is deployed. This is the eleven campaigns that could not ride the SP bulk: **5 Sponsored Display** and **6 Sponsored Brands**.

Every keyword, target and SKU is in `LIN_SB_SD_CONSOLE_BUILD_10Sep2026.xlsx` in paste-ready columns — build from that, use this for the settings around it.

---

## Before you start

**Sponsored Display — build all five now.** Nothing gates them.

**Sponsored Brands — check two things first.** SB needs **brand registry** on the account, and a **brand logo in the Creative Asset Library** (400×400px minimum, white or transparent background). Without both, the campaign cannot be saved. If neither is in place, do the SD five and leave SB.

**One thing to know about SB landing pages.** Sponsored Brands cannot land on a product detail page. With no Store built, the landing page will be Amazon's generated collection page — that is expected, not a mistake. If a Store exists by the time you build, use it instead.

---

## Settings that apply to every campaign

| Setting | Value |
|---|---|
| Portfolio | The linen portfolio |
| Start date | Today |
| End date | **Leave blank** |
| Bidding strategy | Dynamic bids – down only |
| Placement modifiers | **0% on every placement** |
| Ad group default bid | **$0.53** |

The 0% modifiers are deliberate. The 23 August listing change contaminated the placement evidence, so no premium can be justified from current data. They get rebuilt from a clean read after 23 September.

---

## A. Sponsored Display — 5 campaigns, $39/day

All five advertise the same **11 FUND-tier SKUs** (the 0–16% refund group — ivory and light beige across every drop). SKU list is on the `SD SKUs` tab.

### A1. `SL-LC-SD-PT-COMPETITOR` — $12/day
- Targeting: **Product targeting → Individual products**
- Enter the **9 competitor ASINs** from the `SD targets` tab
- Bid **$0.55** on each

### A2. `SL-LC-SD-PT-CATEGORY` — $8/day
- Targeting: **Product targeting → Categories**
- Two categories, each with the same refinements:
  - **Blackout Curtains** — price $18–$40, rating under 4.5
  - **Window Curtains & Drapes** — price $18–$40, rating under 4.5
- Bid **$0.45** on each

### A3. `SL-LC-SD-VIEWS` — $8/day
- Targeting: **Audiences → Views remarketing**
- Lookback: **30 days**
- Bid **$0.53**

### A4. `SL-LC-SD-PURCHASE` — $5/day
- Targeting: **Audiences → Purchases remarketing**
- Bid **$0.53**

### A5. `SL-LC-SD-AUDIENCE` — $6/day
- Targeting: **Audiences → Amazon audiences**
- In-market and lifestyle segments for **home and window treatments**
- Bid **$0.53**

> A3, A4 and A5 are the three that could not be bulk-built — the account holds no example of views, purchase or in-market audience syntax to copy from. Pick the nearest matching segments in the console; exact segment names are yours to choose.

---

## B. Sponsored Brands — 6 campaigns, $84/day

All are **Product Collection** format. Five advertise the **3 hero FUND SKUs**; the size campaign advertises the **3 long-drop SKUs**. SKU lists on the `SB SKUs` tab, keywords on `SB keywords`.

| Campaign | Budget | Targeting | Count |
|---|---|---|---|
| `SL-LC-SB-BROAD-ROOM` | $16/day | Broad keywords | 4 |
| `SL-LC-SB-PHRASE-SIZE` | $14/day | Phrase keywords | 36 |
| `SL-LC-SB-PHRASE-FEATURE` | $12/day | Phrase keywords | 11 |
| `SL-LC-SB-EXACT-PROVEN` | $10/day | Exact keywords | 17 |
| `SL-LC-SB-PC-CONQUEST` | $12/day | Product targeting — the same 9 ASINs | 9 |
| `SL-LC-SB-BROAD-HEAD` | $20/day | Broad — `curtains`, `curtain` | 2 |

All keyword bids **$0.53**; ASIN target bids **$0.55**.

**`SL-LC-SB-PHRASE-SIZE` advertises different SKUs** — the 120 and 108 inch drops, not the hero three. Its keywords are all long-drop terms, so the ad has to show the product that actually fits them.

**Hold `SL-LC-SB-BROAD-HEAD`.** It carries a second gate: the **52x84 reprice**. Head terms are the most expensive on the product and only pay at the repriced 84. Build the other five first; this one waits.

---

## Why these bids and budgets

Every SKU advertised here is **FUND tier** — the 12 SKUs refunding 0–16%. The BLOCK tier (37.5–45.5% refunds) and FLOOR tier (25–30%) are deliberately excluded: their campaigns were just paused or budget-bounded in the SP deployment, and putting them on a new surface would undo that.

The $0.53 default is inherited from the SP build rather than derived from SB or SD economics. It is a reasonable opening number, not a measured one — worth re-reading at the first outcome check rather than treating as settled.

---

## After you build

Tell me what actually went live — campaign names and whether anything had to change. I will add them to the change loader plan so the 23 September read covers them, and so next cycle knows they exist.

Watch for: SB campaigns spending nothing (usually a rejected creative or a missing logo), and SD audience campaigns spending fast (the audience is wider than product targeting, so the $0.53 bid moves more volume there).

---

*Inspiratek & Ecotero LLC · Confidential*
