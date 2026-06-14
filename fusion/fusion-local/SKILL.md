---
name: fusion-local
description: Free multi-model "fusion" on subscriptions you already pay for. Run ANY hard task through a panel of models (Claude + Codex + Gemini), have a judge compare them, then synthesize one stronger answer. Replicates OpenRouter's paid Fusion API at $0 API cost. Use when the user says "fuse this", "ask the panel", "get a second opinion / other models", "deliberate", or on any high-stakes, ambiguous, or easy-to-get-wrong task worth cross-checking — research, coding, debugging, decisions, planning, writing, analysis.
---

# fusion-local — a free Fusion, on subscriptions you already pay for

OpenRouter's **Fusion API** runs a *panel* of models on your prompt, has a *judge* model
compare their answers, and a *synthesizer* write one sharper final answer — then bills you
for every model it ran. This skill does the same thing for **$0 in API credits** by driving
the CLIs you already pay a flat fee for. Works on **any task**, not just one domain.

> Mechanism (same as Fusion): **panel → judge (compare, don't merge) → synthesize.**

## When to fire
- The user says: "fuse this", "ask the panel", "second opinion", "what do the other models think", "deliberate", "cross-check this".
- Any **high-stakes / ambiguous / easy-to-be-wrong** task where one model could be confidently wrong: architecture & design calls, tricky debugging, research with sources, risky decisions, important writing, security/correctness reviews.

## When NOT to fire (be honest — this is the brand)
- Trivial or clearly-codeable tasks where one model already nails it. The panel is **overhead**: it burns ~3× the subscription quota and is slower. Use one model and move on.
- Anything time-critical (the panel + judge + synth is several model calls).

## Prerequisites
- `claude` — you (the running session) are the third panelist + judge + synthesizer. Always present.
- `codex` CLI (ChatGPT/Codex plan) — optional but recommended for diversity.
- `gemini` CLI (Google) — optional.
- It degrades gracefully: with no extra CLIs it becomes Claude self-fusion (answer twice, then synthesize) — OpenRouter's own data shows even that lifts quality.

## Procedure
1. **Capture the task.** Write the user's full prompt to `/tmp/fusion/q.txt`.
2. **Write your OWN answer first** (you are panelist #1). Answer the task independently, before reading the others, so you don't anchor. Save it to `/tmp/fusion/claude.md`.
3. **Run the rest of the panel IN PARALLEL** (one Bash call):
   ```bash
   bash <skill_dir>/fusion_panel.sh /tmp/fusion/q.txt /tmp/fusion
   ```
   This runs Codex + Gemini concurrently on your subscriptions and writes
   `/tmp/fusion/codex.md` and `/tmp/fusion/gemini.md` (whichever CLIs exist). $0 API cost.
4. **Judge (you).** Read `claude.md`, `codex.md`, `gemini.md`. Produce a short structured comparison — do **not** just merge:
   - **Consensus** — points all/most agree on (treat as high-confidence).
   - **Contradictions** — where they disagree, and which side is actually right (say why).
   - **Unique insights** — valuable points only one model raised.
   - **Blind spots** — important things none of them addressed.
5. **Synthesize (you).** Write the single best final answer: consensus as the backbone, contradictions resolved with your judgment, unique insights folded in, blind spots covered. For code tasks, output the best merged implementation, not three.
6. **Tell the user** which models actually answered and that it ran free on their subscriptions. Optionally show the one-paragraph judge comparison so they see *why* the answer is stronger.

## Honest limits (say these out loud)
- **$0 in API credits, but ~3× the subscription quota** (one call per panel model) and slower than a single model.
- Diversity helps on *hard* problems; on easy/codeable ones a single model already wins — don't fuse by reflex.
- More models ≠ automatically better: a sloppy panel can drag quality down. The judge step is what earns the lift.

## Provenance
Built + benchmarked by [@karthikodes](https://instagram.com/karthikodes) against the real
OpenRouter Fusion API — see the head-to-head receipts in the companion writeup. AI Without The Hype.
