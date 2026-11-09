# Daily performance agent

This is a scheduled Claude agent. Every morning it reads Sellerboard and the command center for a product and runs 8 fixed checks. It updates the tracker page and posts a short summary to Slack. It does not change the ad account: it reads, checks and proposes, and the owner decides.

It starts with CooLinens. Adding a product means adding one file to `products/`.

| File | What it is |
|---|---|
| `products/<slug>.json` | Per-product config: SKUs, parent ASIN, sizes, break-even, gates, rank guards, stock boats, output links, Slack channel |
| `CHECKS.md` | The 8 checks: source, rule, and when each one flags |
| `RUNBOOK.md` | The step-by-step run the schedule follows each morning |
| `SLACK_POST.md` | The post format, with a real example |
| `../tracker/` | The data, the scripts and the published page for CooLinens |

## How it runs

- A scheduled task fires at 08:48 US Eastern and follows `RUNBOOK.md`.
- Outputs:
  - the shareable page
  - the dashboard
  - a commit to this repo
  - the Slack post
- Slack goes in two stages:
  - **Draft** (now): the post comes back in the run's reply, and a person pastes it.
  - **Post**: once Slack is connected to the agent and the owner signs off, it posts straight to the channel in `outputs.slack_channel`.

## Rollout

1. **Week 1 (CooLinens).** Run daily in draft mode. Check 3 drafts against Sellerboard by hand, then switch to posting in the agreed channel.
2. **Week 2 (second product).** Generalise the build scripts so they read `products/<slug>.json` instead of CooLinens constants. Add the second product's config and run it in draft for 3 days.
3. **Week 3 (approval loop and weekly roll-up).** The owner answers the "Asks" in the Slack thread, and the next run logs those answers as decisions. A Monday post sums up the week for each product.

## What the owner sets

- Slack channel or thread, and who is tagged.
- Break-even ACoS and stop-loss multiple for each product.
- Rank guards and stock boats.
- Which "Asks" the agent may raise.
