# Fusion — for free, on subscriptions you already pay for

You commented **FUSION**. On June 12, 2026 OpenRouter launched the **[Fusion API](https://openrouter.ai/docs/guides/features/plugins/fusion)** — it runs a *panel* of models on your prompt, a *judge* model compares their answers, and a *synthesizer* writes one sharper final answer. It's genuinely clever. It also **bills you for every model it runs**.

This is the same thing — **panel → judge → synthesize** — rebuilt to run on the CLIs you already pay a flat fee for (`claude`, `codex`, `gemini`). **$0 in API credits.** Works on *any* task: research, coding, debugging, decisions, writing.

## Install (1 minute)

The skill is one file — [`fusion-local/SKILL.md`](./fusion-local/SKILL.md):

```bash
mkdir -p ~/.claude/skills/fusion-local
curl -o ~/.claude/skills/fusion-local/SKILL.md \
  https://raw.githubusercontent.com/karthikodes/drops/main/fusion/fusion-local/SKILL.md
curl -o ~/.claude/skills/fusion-local/fusion_panel.sh \
  https://raw.githubusercontent.com/karthikodes/drops/main/fusion/fusion-local/fusion_panel.sh
chmod +x ~/.claude/skills/fusion-local/fusion_panel.sh
```

Then in Claude just say **`fuse this`** on any hard question. Claude writes its own answer, runs Codex + Gemini in parallel on your subscriptions, judges all three (agree / clash / blind spots), and synthesizes the best one. (Codex + Gemini CLIs are optional — it degrades to Claude self-fusion, which OpenRouter's own data shows still lifts quality.)

## The honest part — when it's worth it (and when it isn't)

I raced this against the real paid Fusion API on an insane task — *"find me 1,000 real job openings, by writing code"*. The receipts ([full writeup](./REPORT.md)):

| brain | jobs found | verified real | cost | time |
|---|---|---|---|---|
| **one Claude** (free, my sub) | 1,113 | 96% | **$0** | 79s |
| my DIY 3-model panel (free) | 1,587 | 72% | $0 (1.07M tokens) | 13.6 min |
| **OpenRouter Fusion** (paid) | 3,741 | 100% | **$5.96 real** | 19.5 min |

**The lesson:** on a task you can *code*, a single model already wins — for free. Multi-model fusion buys thoroughness, not magic, and you can run the whole pattern yourself at $0. Save the panel for genuinely hard, ambiguous, easy-to-be-wrong questions — and even then, watch the quota (it's ~3× the calls). And don't chase volume: pushed to find *more*, a single model just starts making jobs up.

---
*From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype. Reproduce the whole test yourself: it's all in [REPORT.md](./REPORT.md).*
