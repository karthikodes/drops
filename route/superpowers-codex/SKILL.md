---
name: superpowers-codex
description: Use when executing an implementation plan, a multi-file coding task, bulk mechanical work, or any approved spec — and a Codex CLI subscription is available. Replaces the Claude implementer subagent with a headless Codex run per task while Claude stays the brain (planning, task specs, spec-compliance review, code-quality review). Execution tokens land on the Codex plan instead of your Claude limits. Drop-in execution layer for the Superpowers plugin's subagent-driven-development; also works standalone. Keywords: delegate to codex, execute plan, implement plan, save tokens, codex exec, second model, route models.
---

# Superpowers × Codex — Claude is the brain, Codex is the hands

Claude (best judgment) plans, writes specs, and reviews. Codex (separate subscription, separate limits) implements. Two wins: implementation tokens never touch your Claude limits, and a second model family checks the work by construction.

**Announce at start:** "I'm using the superpowers-codex skill to execute this plan."

**Core loop (identical to Superpowers' subagent-driven-development, with the implementer swapped):**
plan → TodoWrite per task → per task: spec → **Codex implements** → Claude spec-compliance review → Claude code-quality review → commit → next task.

## Requirements

- Codex CLI installed + authenticated (`codex --version`; `codex login`). Usage counts against Codex limits, not Claude's.
- Strongly prefer a git repo (clean diffs per task). Not strictly required (`--skip-git-repo-check`), but you lose the review mechanism without diffs.
- No Codex? Gemini CLI slots into the same recipe (`gemini --approval-mode yolo -p "$(cat spec.md)"`), or fall back to native Claude subagents (Superpowers' default) and lose only the token savings.

## The Process

### 1. Plan first (Superpowers does this part better than anyone)
If the Superpowers plugin is installed: run its brainstorming → writing-plans skills, then use THIS skill in place of `subagent-driven-development`'s implementer dispatch. The orchestrator loop, TodoWrite-per-task, and two-stage review gates stay exactly as Superpowers defines them — only the implementer changes. Without Superpowers: break work into bite-size tasks (one outcome, exact file paths, acceptance checks each).

### 2. Write the task spec — Codex sees ONLY this file, never your conversation
Anything not in the spec does not exist for Codex. Create `/tmp/task-N-spec.md`:

```markdown
# Task: <one-line outcome>
## Repo & ground rules
- Repo root: <absolute path> · branch: <name> (do not create branches, do not commit)
- Write set (the ONLY files you may modify): <exact paths>
- Read these first: <files to inspect> · Copy the pattern in: <file:lines — point, don't say "existing patterns">
- Policies: deps <may/may not add> · tests <may/may not add> · no formatter sweeps · no generated files · network <yes/no>
## Do
<numbered, concrete steps with product behavior spelled out>
## Do NOT
<refactor unrelated code / touch files outside the write set / invent APIs or facts>
## Acceptance (observable — must prove the artifact WORKS, not just exists)
<run the artifact: tests pass, app renders/serves, output frames/responses verified — with exact commands. Lint alone is NOT acceptance.>
## Final response shape
Report: STATUS (DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT), changed files, commands run + results, concerns.
```

Spec mistakes that most often produce wrong code (from Codex itself): vague "make it better", unnamed files, no acceptance examples, "use the existing pattern" without pointing at it, constraints that live only in your conversation, stale paths.

> Field note on acceptance: in our controlled A/B, an implementation passed every lint and grep check but rendered a 100% black video — caught only because the reviewer ran the artifact. Write acceptance that exercises the thing (render a frame, hit the endpoint, run the binary), and run it yourself at review.

### 3. Dispatch (headless, sandboxed, time-boxed)

```bash
perl -e 'alarm 1200; exec @ARGV' \
  codex exec \
  --cd /absolute/repo/path \
  -s workspace-write -c approval_policy="never" \
  -c model_reasoning_effort="medium" \
  --json -o /tmp/task-N-last.md \
  - < /tmp/task-N-spec.md > /tmp/task-N-events.jsonl 2>&1
```

- **Reasoning effort tiering:** `medium` for mechanical work · `high` for cross-file logic · `xhigh` only to rescue a gnarly failure. This is your cost dial.
- `-o` (output-last-message) gives you the report to review; `--json` events include the **session id — capture it** for fix loops.
- `-s read-only` for analysis/review-only tasks. Note `workspace-write` is repo-scoped by default but expandable via `--add-dir` — don't add dirs you don't want touched.
- The `perl alarm` kills runaway runs at 20 min (macOS has no `timeout`; on Linux use `timeout 1200`).

### 4. Two-stage review — Claude judges, never rubber-stamps
1. **Spec compliance:** `git diff` — exactly what the spec says, nothing more? Out-of-scope edits → revert, tighten the "Do NOT", redispatch.
2. **Quality:** read the diff as a reviewer (edge cases, conventions, tests that actually assert). Run the acceptance commands yourself — never trust the log's claim that they passed.

### 5. Fix loops — resume, don't restart
- Nuanced review feedback → same worker, with its context: `codex exec resume <session_id> - < /tmp/task-N-feedback.md` (use the captured session id; never `resume --last` in automation — parallel runs make "last" ambiguous).
- First attempt drifted badly → fresh `codex exec` with the tightened spec (clean-room beats arguing).
- Max 2 fix passes, then Claude implements the remainder directly.

### 6. Parallel dispatch (2–4 workers)
Only with **truly disjoint write sets**. Unique spec/log/last files per task. **Workers never commit** — Claude reviews and commits serially after each lands (interleaved diffs are unreviewable). Watch for shared-state contention: lockfiles, formatters, ports, test caches.

## Token economics (measured, one user — anecdotal, not predictive)

Controlled A/B (same task spec, same orchestrator, June 2026): the native Claude-subagent implementer spent **52,929 Claude-plan tokens** in 208s; this skill delivered the same scope in 199s for **~zero Claude tokens** (506K in / 7.5K out, all on the Codex plan) — and in that run, the Codex build was the only one whose output actually rendered. At plan scale (a 10-task Superpowers plan ≈ 30 dispatches) that's roughly 0.5–1.5M Claude tokens per plan moved to the second subscription. Background context: the author's 30-day logs show ~32B tokens through Claude Code — execution volume is exactly what eats a Claude plan. One user's numbers, not a guarantee; your mix will differ, and judgment-heavy work shouldn't move at all.

## Red flags — stop and reread this skill if you catch yourself…

| Rationalization | Reality |
|---|---|
| "The task is clear from our conversation, I'll keep the spec short" | Codex never sees the conversation. Spec = the whole world. |
| "Codex said tests pass, moving on" | Run the acceptance commands yourself. Always. |
| "I'll let it commit to save a step" | Workers never commit. Review-then-commit is the quality gate. |
| "This design decision is mechanical, Codex can choose" | Design and judgment stay with Claude. Codex executes decided specs. |
| "Third fix pass will do it" | Two passes max. Then take it back inline. |

## When NOT to use
Ambiguous design work, architecture, anything needing conversation context → Claude directly. Single-file trivial edits → dispatch overhead beats savings. Secrets/credentials handling → keep where you can watch it.

---
*From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype. Companion to the model-routing table in this folder. Built on (and compatible with) [obra/superpowers](https://github.com/obra/superpowers); complements OpenAI's official [codex-plugin-cc](https://github.com/openai/codex-plugin-cc) (reviews + one-shot rescue) by adding the structured plan→dispatch→review execution layer. Invocation details verified against Codex CLI's own guidance, June 2026.*
