# The Stack — get Mythos-level output after the Fable 5 ban

You commented **STACK**. On June 12, 2026 a US export-control order forced Anthropic to disable **Claude Fable 5 and Mythos 5** for all customers ([Anthropic's statement](https://www.anthropic.com/news/fable-mythos-access) · [CNBC](https://www.cnbc.com/2026/06/12/anthropic-disables-access-to-fable-5-and-mythos-5-to-comply-with-government-directive.html)). If you're outside the US, your most powerful Claude is gone. Other models — including **Opus 4.8** — still work.

Here's the setup I switched to. It doesn't *replace* Fable. It claws back a lot of the lost ceiling by running **two models instead of one**.

## The idea

> One model is your **brain**. A second is your **hands**. The brain plans and reviews; the hands do the heavy implementation. You get more total output per session than either model gives you alone — and a second model family checks the first by construction.

- **Claude Opus 4.8 → the brain.** Architecture, planning, judgment, final review.
- **Codex (ChatGPT plan) → the hands.** Bulk implementation, mechanical edits, parallel grunt work.
- **One skill makes Claude delegate straight to Codex** — you stay in Claude, it dispatches the build work to Codex, reviews the result, and moves on.

## Install it (2 minutes)

The skill is one file — [`superpowers-codex/SKILL.md`](./superpowers-codex/SKILL.md):

```bash
mkdir -p ~/.claude/skills/superpowers-codex
curl -o ~/.claude/skills/superpowers-codex/SKILL.md \
  https://raw.githubusercontent.com/karthikodes/drops/main/stack/superpowers-codex/SKILL.md
```

Or claude.ai → Settings → Capabilities → Skills → upload. Then say *"execute this plan"* and the delegation is automatic. (Requires the Codex CLI + a ChatGPT plan. No Codex? The same recipe works with Gemini CLI — noted in the skill.)

## Does multi-model actually beat one model? (the honest answer)

Mixed — and worth knowing before you buy the hype:

- **For hard reasoning/coding, yes, often.** Multi-agent setups measurably lift weaker models: in the BIGMAS study, Claude Sonnet 4.5 went **48% → 68%** on Game-24 and DeepSeek-V3.2 **25% → 36%**; ensemble agents on HumanEval climb toward **~89%** with five agents ([arXiv 2603.15371](https://arxiv.org/pdf/2603.15371)). Multi-Agent Reflexion (MAR) also beats single-agent on reasoning + code ([arXiv 2512.20845](https://arxiv.org/html/2512.20845)).
- **But it's not free, and not always a win.** Tran & Kiela (2025) show that *under a fixed compute budget*, a single strong agent often matches or beats multi-agent. More agents = more tokens, more latency.
- **Our setup is delegation, not voting.** The benchmarks above are mostly ensembles; brain-hands routing (Opus plans → Codex builds) is a different shape. Treat the numbers as directional proof that "more than one model helps on hard work," not a guarantee you'll hit a specific score.

**Bottom line:** it's slower than one frontier model, and it won't fully replace Fable 5 — but it recovers a lot of the lost ceiling, spreads the work across two subscriptions, and gives you a built-in reviewer. For the post-ban reality, that's the best move available.

## The honest caveat
This is an **export-control fight, not a quality verdict** on Fable. Anthropic is contesting it; Fable 5 may return. Until it does, stack your models. Re-check this in a few weeks — the situation is moving fast.

---
*From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype. Companion: the model-routing table in the [route](https://github.com/karthikodes/drops/tree/main/route) drop.*
