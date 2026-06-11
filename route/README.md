# The Model Routing Table — which AI for which task (and what it actually costs)

You commented **ROUTE**. This is the exact table I use — not "the best model," but the right model per task. Updated 2026-06-11, the week Claude Fable 5 launched.

## Install the skill (the fast path)

This folder ships **[superpowers-codex/SKILL.md](./superpowers-codex/SKILL.md)** — a Claude skill that does the routing FOR you: Claude (Fable 5) stays the brain — planning, task specs, two-stage review — and every implementation task auto-delegates to your Codex subscription. It's the Superpowers workflow with Codex as the subagents: same structure, but the execution tokens land on the second plan instead of your Claude limits.

```bash
mkdir -p ~/.claude/skills/superpowers-codex
curl -o ~/.claude/skills/superpowers-codex/SKILL.md \
  https://raw.githubusercontent.com/karthikodes/drops/main/superpowers-codex/SKILL.md
```

Or claude.ai: Settings → Capabilities → Skills → upload SKILL.md. Then say "execute this plan" — delegation is automatic. (Gemini CLI can slot into the same recipe; the skill notes how.)

## The one-line rule

> Route by task value, not by model strength. The strongest model goes on the 20% of work that decides quality; volume work goes where tokens are cheap.

## The table

| Task type | Model I use | Why | Cost reality |
|---|---|---|---|
| Architecture decisions, hard debugging, final review | **Claude (Fable 5 / Opus)** | Best judgment on ambiguous problems; catches what others miss | The expensive one: Fable 5 API = $10 in / $50 out per M tokens (2× Opus). Worth it HERE, nowhere else |
| Bulk implementation, parallel grunt work, mechanical edits | **Codex** | Runs many tasks in parallel; volume is where my usage actually goes | Flat $100/mo plan absorbs huge volume — this is the workhorse |
| Long-context reading, research sweeps, cheap first drafts | **Gemini** | 1M-token context window; reads whole repos/docs in one pass | Cheapest per token of the three for this shape of work |

## My actual bill (the receipts from the reel)

- Claude Code: **$100/mo** (plan) — the brain. Measured last 30 days: **~32 billion tokens** through this one flat plan (≈$60K+/month if bought as Fable 5 API credits)
- Codex: **$100/mo** (plan) — the hands. Same 30 days: ~288M tokens; every task delegated there is implementation volume that never touches the Claude limits
- Total: $200/mo for both, predictable. The trap: running EVERYTHING through the flagship — after June 22, Fable 5 leaves subscriptions and bills as usage credits ($10/$50 per M) ON TOP of what you already pay. Flagship prices for grunt work is how a $200 bill stops being $200.

## When the expensive model IS worth it

Honest beat from the reel: when a task is genuinely hard — multi-step architecture, a bug two other models bounced off, a final pass where wrong = expensive — Fable 5 one-shots things that used to take three passes. That's exactly where $50/M out is cheap. Pay for judgment, not for typing.

## Caveats (the no-hype part)

- Your mix is not my mix. **Measure one week of your own usage before copying this** — most people discover 70%+ of their tokens are volume work that never needed the flagship.
- Prices/availability move fast: Fable 5 numbers above are from Anthropic's launch announcement (Jun 9, 2026); re-check before budgeting.
- Subscriptions ≠ API: plan limits and per-token prices are different regimes; this table is about plans first, credits second.

---
*From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype.*
