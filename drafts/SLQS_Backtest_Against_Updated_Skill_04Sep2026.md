# SLQS back-test — the quilt set plan against the updated clearance skill

**Plan tested:** SLEEPHORIA Quilt Set — Product Audit and Clearance Plan, 28 August 2026 (version modified 2 September)
**Tested against:** `inspiratek-clearance-audit`, as at 4 September 2026
**Run:** 4 September 2026 · full document read, all 571 lines · arithmetic re-derived from the plan's own figures

---

## The verdict in five lines

The plan is strong where the skill is newest and weak where the skill is oldest — the opposite of what a back-test usually shows. The leak audit, the spend-to-volume curve, the placement ladder and the gap register are better than the skill's own written standard. The failures are concentrated in the economics: **the plan computes one ceiling number where the skill requires four**, and without the other three it cannot see that its own bid cap breaches the ceiling it set.

Two failures would change what gets deployed. Four are internal contradictions in the plan that a reader cannot resolve. One finding is against the skill, not the plan.

---

## 1 · What passes, and what is better than the skill asks for

| Area | Read |
|---|---|
| **Leak audit** | **Exemplary.** Nine leaks, $44,831/month, ranked by size not by owner, each with a named owner and a fixable-now flag. States plainly that a PPC-only plan addresses 15% of the loss. This is the standard the skill describes, executed better than the skill's own example |
| **Spend-to-volume curve** | **Exemplary.** Six spend points with CPC and CVR degradation modelled, then converted to months-to-clear and net benefit. Explicitly refuses straight-line extrapolation. Then states the real constraint: *"The real ceiling is stock, not spend"* |
| **Placement** | **Passes hard.** Per campaign per placement, against that campaign's own conversion data, on a four-step CPA ladder. 43 of 1,341 combinations earn a premium and the plan says why the other 1,298 do not. It explicitly refuses a blanket premium — *"a blanket premium would fund 428 campaigns on no evidence"* |
| **Denominator** | **Passes.** Ad cost per unit **shipped** ($17.88), not per ad-attributed order. Refund cost is carried inside contribution rather than applied twice — a different construction from the skill's, and internally consistent |
| **Charge basis** | **Passes.** $7.35/unit/month × 2 months = $14.70. One month's figure, correctly multiplied by the window |
| **Deal exclusion, forward** | **Passes.** Deal windows and the 14 days after are excluded from trend verdicts; the first clean read is dated 27 September |
| **Basis tags** | **Passes.** HIST / MARKET / TEST on essentially every claim |
| **Gap register** | **Passes.** Eight named gaps, each with why it matters, what is needed, and an owner |
| **Decisions requested** | **Passes.** Ten, owned, dated |
| **Data-trap discipline** | **Passes.** The Data Dive vs SellerSprite source conflict is named and adjudicated rather than averaged. The landed-cost correction in §4.1 caught a $3.80–$5.67/unit error in the plan of record |
| **Campaign count vs budget** | **Passes.** $599/day ÷ $5.00 = 120 campaigns affordable; 25 proposed |
| **Budget floors** | **Passes on the new builds.** Lowest proposed campaign is $12/day |

---

## 2 · The failures that change what gets deployed

### 2.1 · Only one of the four numbers is computed — and the cap breaches it

The plan adopts a ceiling of **$28.47** per unit and tests cost-per-order against it. The skill requires four numbers per child, and the other three are absent.

Derived here from the plan's own figures — contribution $13.77, ceiling $28.47, ad CVR 3.45%:

| Number | Value | Status in the plan |
|---|---|---|
| Break-even ACoS | **33.7%** | **Never stated** |
| Floor bid | $0.25 | Never stated as a number |
| **Max profitable CPC** — where profit ends | **$0.475** | **Never computed** |
| **Max click price** — the hard cap | **$0.982** | **Never computed** |

The subsidy zone is **$0.475 to $0.982**.

Testing the plan's own two bids against it:

| Bid | Cost per order | vs $28.47 ceiling | Subsidy per unit | vs $14.70 charge avoided |
|---|---|---|---|---|
| **$0.53** open (Amazon's suggested median) | $15.36 | inside | $1.59 | **inside, comfortably** |
| **$1.10** winner cap | **$31.88** | **OVER** | **$18.11** | **OVER by $3.41** |

**The opening bid is well chosen and the plan cannot demonstrate it.** $0.53 sits low in the subsidy zone, which is exactly where the skill says a clearance bid belongs — but the plan reaches it by copying Amazon's suggested median, not by deriving it, so the fact that it is right is luck rather than method.

**The $1.10 cap is above the ceiling the plan itself set.** It is a round number, not a derived one. On the plan's blended CVR a $1.10 click costs $31.88 per order against a $28.47 ceiling, and the subsidy runs $3.41 per unit past the charge it is avoiding. A keyword converting well above blended may still clear it — but the plan never tests per keyword, so it cannot know which ones do.

**Consequence:** 66 winner keywords are raised 30–55% toward a cap that has not been shown to be affordable.

### 2.2 · A budget cap cut is reported as a saving

This is the exact error the skill was rewritten in September to prevent.

| | |
|---|---|
| Enabled daily budget (§5.1) | **$4,680.00** |
| Actual daily spend (§2: $7,391 ÷ 30) | **$246.37** |
| **Utilisation** | **5.3%** |
| Cap after the cut (§5.1) | $2,002.00 |
| **Cash actually released** | **$0.00** |

§13 books this as *"Budgets re-cut by days of cover · 447 rows · $4,680 to $2,960 a day · Closes leak 5, worth $2,414/month."*

**Leak 5 is real. The mechanism named does not deliver it.** $2,414/month of genuine spend is going to SKUs with 21–116 days of cover that clear without support. But that money is being *spent* at keyword and target level, and it stops only if those targets are paused or floored. Cutting a cap the account reaches 5% of releases nothing at all.

There is a second-order problem: $2,002/day across 447 campaigns is **$4.48 per campaign**, below the $5.00 floor. Some lanes will land in the dead zone between zero and the floor — funded, but not enough to deliver a readable day.

### 2.3 · 217 keywords are cut below the click line

| Bucket | Keywords | Plan's action | Skill |
|---|---|---|---|
| Zero orders, 15+ clicks | 43 | Paused | **Allowed** — at the line, reviewed on merits |
| **Zero orders, 5–14 clicks** | **83** | **Bids cut 40%** | **Barred** — under the line |
| **Zero orders, 1–4 clicks** | **134** | **"Small trim"** | **Barred** — under the line |

A term below 15 clicks with no orders has not had its chance. Cutting its bid removes the discovery surface that finds the cheapest orders — and on this product cheap discovery is the whole thesis, since Phrase winners run $0.32–$0.51 per click against $0.90–$1.45 for Exact.

The 15+ pause bucket is not checked against the cheap-click extension either (20–25 clicks where the click price is about $0.15 or under). At $24.79 average spend per keyword across the 43, most are probably above $0.15 — but it is not shown.

### 2.4 · Every headline figure is deal-contaminated, and the plan's own rule says so

The plan's §16 rule: *"Deal windows and the fourteen days after them are excluded from trend verdicts."* Correct, and applied rigorously going forward.

It is not applied backward. The 30-day window ending 26 August contains **five Lightning Deals** — 28 July, 6, 11, 19 and 24 August. There is no uncontaminated day in it. Every figure in §2, and therefore the entire spend-to-volume curve in §15, rests on a base the plan's own standard would reject.

The plan half-sees this — §7.1 notes *"no clean elasticity read is available"* — but does not carry it into §15, where the conclusion is drawn.

### 2.5 · The refund gate is reasoned around rather than applied

§10 gives per-SKU refund rates. Tiered against the skill's gate:

| SKU | Rate | Tier | Plan's treatment |
|---|---|---|---|
| QUEEN-WHITE | 27.3% | **FLOOR** | White gets a dedicated Phrase campaign; SP-PHRASE-COLOUR *"weighted to white"* |
| QUEEN-SAGE-GREEN | 26.9% | **FLOOR** | Existing coverage only — correct by accident |
| QUEEN-LIGHT-GREY | 25.0% | **FLOOR** | Routed to Generic, Auto, PAT, Display |
| KING-IVORY | 20.0% | FUND | Phrase, shared campaign |
| TWIN-IVORY | 20.0% | FUND | — |

**White is a FLOOR-tier SKU being made the growth story of the colour build.** A FLOOR SKU is funded, never scaled — a refunded unit re-enters the aged pool and re-accrues the charge, so it costs twice.

§10's reasoning is good and the ruling it invokes is right: *"PPC does not wait on this... storage costs $146,313 over the runway against roughly $22,000 of annualised refund cost."* But that argument answers a different question. The gate does not say stop advertising; it says **do not scale the SKU that comes back**. The plan proves it should keep pushing and takes that as permission to push hardest exactly where returns are worst.

Two supporting gaps: no unit counts behind the SKU rates, so the ≥10-unit sample guard cannot be checked; and the refund rate is a **rising series** (0.5% → 17.6% → 15.8% → 18.2% → 26.0%), which a point-in-time tier misreads.

### 2.6 · Attribution method never stated

The plan decides 2,322 Quilt Set rows and leaves Linen Curtains untouched, so scoping clearly happened. But the document never says **how** spend was attributed — product-ad rows, portfolio filter, or campaigns containing the product's ads — and never reconciles the attributed total against Sellerboard.

On Hanging Closet the wrong method overstated product spend by a factor of thousands. Until the method is named this cannot be checked, and every dollar figure downstream inherits the doubt.

---

## 3 · The build violates three structural rules

| Campaign | Keywords | Rule broken |
|---|---|---|
| SP-EXACT-SIZE-A / SIZE-B | 129, split in two (~65 each) | 4–5 per campaign; one SV tier per campaign |
| SP-PHRASE-COLOUR | 39 | 4–5 per campaign; campaign purity (one colour family) |
| SP-PHRASE-GENERIC | 38 | 4–5 per campaign; spans VHSV to LSV |
| SP-PHRASE-XCAT | 28 | 4–5 per campaign |

Three consequences, all mechanical:

**Cannibalisation goes unchecked.** Thirty-eight Phrase keywords in one campaign will contain pairs where one captures another as a contiguous run — *quilt set* eats *quilt set queen*. The short term takes the auctions, the long one draws nothing, and the plan concludes wrongly that the long one does not work.

**Volume tiers are mixed.** SP-PHRASE-GENERIC spans a 410,248-search pool. The big terms absorb the budget and the small ones never reach the click line, so they stay unreadable forever.

**Colour purity is broken, and the plan contradicts itself on it.** §8.2 routes White to a *dedicated* Phrase campaign and Ivory to one *shared with Taupe*. §14 puts all 39 colour terms in **one** campaign carrying all eight high-cover SKUs — so a *white quilt* search can serve a taupe ASIN. Weighting bids toward white does not fix serving the wrong colour.

---

## 4 · Four internal contradictions

These are not skill failures. They are places where the document contradicts itself and a reader cannot tell which figure is operative.

| # | Contradiction | Where |
|---|---|---|
| **1** | **Four different recommended budgets.** $600/day; $707/day; *"authorise the ramp to $420/day, or hold at $334/day"* | §15.1 · §15.3 · §18 decision 1 |
| **2** | **Two different current paces**, both called current. 5.3/day → 15.8 months → $146,313 storage, and 12.3/day → 6.8 months → $63,045. One is the week to 26 Aug, the other the 30 days — the plan does not say which governs | §6 · §15.2 |
| **3** | **Three different current budgets:** $4,680/day, $232.56/day, $246/day. These are caps, caps-after-cuts and actual spend respectively, and none is labelled as such | §5.1 · §15.3 · §15.1 |
| **4** | **Two different colour campaign structures** — dedicated per colour, and one campaign of 39 terms | §8.2 · §14 |

Contradiction 3 is the one that matters most: it is precisely the cap-versus-spend confusion that produced failure 2.2.

---

## 5 · Missing outputs

| Required | State |
|---|---|
| **Section 0 — prior cycle graded** | **Absent.** Grading exists but is scattered through §1, §15 and §16. No execution verification (were the prior actions actually deployed?), no per-action grade, no provisional marking for the refund lag |
| **Prior objective recorded per campaign** | Absent. Rank is correctly abandoned as an objective, but the previous value is not captured, so the change is not auditable |
| **Negatives tab** | Absent. Three appended sheets — SP, Brands, Display. No negation architecture beyond the isolation rule |
| **Reverses If column** | Absent. New Bids, New Budget, New Percentage, Action and Reasoning are populated; nothing says what would undo each decision |
| **Clearability gate per SKU** | Partial. Light grey gets a correct CLOSED-style read. Twin — 51 clicks, zero purchases, 0.00× index — is never classified and its route is never stated |
| **Exit threshold** | Absent. No stock level at which the clearance posture ends |
| **Billing date priced** | Partial — see below |
| **Verdict vocabulary** | FUND, EXPAND, RESTART, REBUILD, FUND FIRST are invented strings, not canon verdicts |
| **Build classes B1–B7** | Not assigned to the 25 proposed campaigns |
| **PAT edge per target** | 16 conquest ASINs proposed; 2 carry evidence (WDCOZY $14.86, Mybedsoul $15.25). 14 unjustified |

### The billing date is named but never priced

§5 names all three dates correctly — units cross 366 days in early September, resize decision 14 September, **bill lands 15 September**. The skill then requires the units clearable before that date and what they are worth.

From the plan's own figures, at $4.09 aged surcharge per unit and 18 days from the plan date:

| Pace | Units cleared before 15 Sep | Avoided on that bill |
|---|---|---|
| Current, 5.3/day | 95 | $390 |
| 30-day, 12.3/day | 221 | $906 |
| **Plan pace, 39/day** | **702** | **$2,872** |

**Deploying before 15 September is worth roughly $2,500 more than deploying after it**, on that one bill alone. The plan has a grading calendar but no deployment wave sequenced against the billing date. The D120 deal window (31 Aug – 13 Sep) happens to land correctly; the advertising build is not tied to it.

---

## 6 · What the back-test found in the SKILL, not the plan

**The ACoS correction ladder breaks when break-even is above 30%.**

This product's break-even ACoS is **33.7%**. The ladder's first band says *under 30% — working, no change*, and its second says *30–50% — cut 5 cents*.

So a campaign running at **32% ACoS on this product is profitable and the ladder cuts it.**

On Hanging Closet break-even was 7.68%, so "under 30% is working" meant tolerating four times break-even — the band was generous. Here the same band is *stricter* than break-even. The bands are absolute by design and that was ruled deliberately, but nothing in the skill covers the case where break-even sits above the first band boundary.

**This needs a rule and I have not written one.** The obvious candidate: no bid is cut on a campaign running below its own break-even ACoS — the working band extends to break-even wherever break-even exceeds 30%. That is my proposal, not a decision.

Two smaller gaps the same run exposed:

- **No rule for a baseline with no clean window.** The skill says never blend a deal window with a clean one. This product ran five deals in 28 days and has no clean 30-day read at all. The skill needs to say what to do when the clean window does not exist.
- **No rule for an existing account already built the other way.** The 4–5 keyword sizing assumes you are building. This account has 447 live campaigns sized 28–65 keywords. Rebuilding all of them is not a cycle's work, and the skill does not say how to stage it.

---

## 7 · Scored

| | Checks | Pass | Fail | Partial |
|---|---|---|---|---|
| Economics and ceiling | 11 | 4 | 6 | 1 |
| Budget and waste | 7 | 3 | 4 | 0 |
| Gates | 6 | 2 | 3 | 1 |
| Build structure | 9 | 3 | 5 | 1 |
| Outputs and format | 12 | 5 | 6 | 1 |
| Diagnosis and evidence | 8 | 8 | 0 | 0 |
| **Total** | **53** | **25** | **24** | **4** |

**Diagnosis scores full marks. Economics scores under half.** That is a consistent shape: the plan sees the product clearly and prices its decisions loosely.

---

## 8 · What to fix first, if this plan were re-run

1. **Compute the four numbers per child** and re-test every raised bid against max click price. This alone decides whether the 66 winner raises ship as written.
2. **Re-price leak 5 as a target-level action.** Pause or floor the low-cover SKUs' targets; leave the caps alone.
3. **Restore the 217 keywords cut below the click line.**
4. **Re-tier the refund gate and stop scaling White**, or state explicitly why the gate is being overridden and what the accepted cost is.
5. **Name the attribution method** and reconcile to Sellerboard.
6. **Resolve the four contradictions**, especially the recommended budget — a reader cannot execute against four figures.
7. **Sequence the deployment against 15 September**, and state what each wave is worth.
8. **Split the four oversized campaigns** by volume tier and colour family, and run the cannibalisation check.

---

*Inspiratek & Ecotero LLC · Confidential · Back-test, not a plan revision*
