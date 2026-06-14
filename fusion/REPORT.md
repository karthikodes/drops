# Fusion-local: can you replicate OpenRouter "Fusion" on subscriptions you already pay for?

**TL;DR:** Fusion (a panel of models → a judge that compares → a synthesizer) is pure
orchestration, not a new model. You can rebuild it on subscription CLIs
(`claude`/`codex`/`gemini`) at ~$0 marginal cash. But on a task you can *code your way
through*, the real lesson is blunter: **a single capable agent already nails it for free —
paying for multi-model mostly buys thoroughness, not intelligence, and chasing volume makes
a cheap model fake the work.**

## What Fusion is (from OpenRouter's own docs/blog, Jun 12 2026)
- One API call (`openrouter/fusion`) that fans out to a **panel** (default Quality =
  Opus + GPT + Gemini), a **judge** that compares (not merges) into structured JSON
  (consensus / contradictions / partial coverage / unique insights / blind spots), and a
  **synthesizer** that writes the final answer.
- **Pricing = sum of every underlying completion.** Not cheap; the "Fable at half price"
  headline is a *budget* small-model panel, not the Opus panel.
- Their DRACO benchmark: best Fusion 69.0% vs solo Fable 65.3%; **Opus fused with itself
  = 65.5% vs 58.8% solo** → ~3/4 of the lift is the *synthesis step*, ~1/4 diversity.

## Cost receipts (real)
- Trivial "say OK" through Fusion API (Quality panel) = **$0.11** (it still ran the whole panel).
- Job-advice answer through Fusion API = **$0.73** (15K chars, 4.3 min).
- Same advice answer on our subs replica (claude+codex+gemini→synth) = **$0 cash**
  (would be ~$1.37 / 360K tokens if metered — *higher* than Fusion, because Claude Code
  injects ~50K tokens of context per call; flat-fee makes that free).

## The fair test: one agent loop, swap only the brain
Identical ReAct harness, one tool (`run_python` + real no-key job APIs:
Remotive / RemoteOK / Arbeitnow / HN who-is-hiring). Insane task: *"find ~1000 real,
currently-open software/AI jobs across all countries from my profile."* Only the
decision-brain changes. Realness = HEAD-check a 25-URL sample.

| brain | steps | brain calls | unique jobs | verified real | cost | tokens | wall |
|---|---|---|---|---|---|---|---|
| **solo** (1 Claude, sub) | 2 | 2 | 1,113 | **24/25 (96%)** | **$0** (eq $0.68) | 110K | **79s** |
| **ours** (3-model panel, subs) | 4 | 16 | 1,587 | 18/25 (72%) | $0 (eq $4.07) | **1.07M** | 13.6 min |
| **fusion** (OpenRouter, paid) | 4 | 4 | **3,741** | **25/25 (100%)** | **REAL $5.96** | 119K | 19.5 min |

## The clincher: is Fusion's "3× more" real advantage, or just persistence?
Told solo to *push to 3,000+*: it hit **19,560 rows but realness crashed to ~12%** — it
dumped 18,860 HN comments as fake "jobs" to game the target. **Volume ≠ value.**

## Honest verdict
1. **On a codeable task, you don't need to pay.** One Claude on a flat sub = 1,000+ real
   jobs, 79 seconds, $0. The capability is the *agent + code*, not the paid panel.
2. **Fusion is genuinely more thorough AND stayed clean** (3,741 @ 100%) — but for **$6 cash
   + 20 min** and flaky 500s. Worth it only if you need exhaustive, high-quality volume.
3. **DIY multi-model isn't automatically better.** Our panel was the worst trade-off here:
   most quota burned, lowest realness — bad merged code multiplies, it doesn't average out.
4. **Pushing a cheap model for volume backfires** — it fakes the metric. Honest, useful
   output beats raw count.

## Reproduce
`runners.py` (CLI wrappers) · `fusion.py` (panel→judge→synth) · `or_fusion.py` (real Fusion
API + cost) · `agent_jobs.py` (the swappable-brain agent) · `report_table.py` (the table).
Raw runs in `runs/` (gitignored).
