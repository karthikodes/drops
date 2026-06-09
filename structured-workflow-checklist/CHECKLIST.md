# The structured-workflow checklist (the "STRUCTURE" drop)

The reel's claim in one page: with frontier models bunched at the top, your edge isn't the model you pick — it's the **harness** around it. This is the checklist, distilled from how Matt Pocock + Dex Horthy actually work. Credit to them; the framing is mine.

> Not a magic prompt. Not 10x. Just the engineering discipline that makes AI output you don't have to redo.

## 1. Plan first — get grilled before any code
- Make the model **interview you** about the plan before it writes a line (Pocock's `grill-me`). Answer the *low-fidelity* questions ("what route?"); for *high-fidelity* ones ("how should it feel?") — **prototype, don't argue**.
- Don't throw the planning away. Turn the conversation into a short handoff/PRD doc, not 100k tokens you discard.

## 2. Give it a shared language
- Keep a **`context.md` glossary** at the repo root: the same terms for the code, you, and the AI (DDD "ubiquitous language" — Pocock's `grill-with-docs`). Result: shorter prompts, fewer thinking tokens, code whose names match the glossary.
- Record only the **hard-to-reverse** decisions as short ADRs (architectural decision records). Don't document the obvious.

## 3. Guard the context window
- Treat ~**120k tokens** as the start of the "dumb zone" (Pocock's estimate) even if the model advertises 1M. Quality degrades well before the limit.
- **Hand off** a slice to a fresh session before you hit it; keep the working session clean. (Pocock's `handoff` skill writes a disposable doc a fresh agent continues from.)
- This is **Factor 3 of Dex Horthy's [12-Factor Agents](https://github.com/humanlayer/12-factor-agents)** (20k+ stars): *own your context window.*

## 4. Right-size the model to the job
- Use a **smart** model to *plan* (planning leans on the model's own knowledge); a **cheaper** model to *implement* (implementation is mostly following your plan + files). Don't pay frontier rates for boilerplate.

## 5. Gate the output with a real review
- Run an **ambitious automated review** that looks past the diff at the whole codebase — and that actually covers **tests + seams**, not just style. A review that doesn't run the code or check the tests is theater.
- Pairs with the two-model pattern (see the COMBO drop): one model writes, a second reviews against runnable tests.

---

**The honest part:** raw capability didn't flatline — reasoning models still climb. What converged is the *benchmarks*. So the durable advantage moved to structure. Plan first → shared language → guard the window → right-size → review.

*Credit: [Matt Pocock](https://youtube.com/@mattpocockuk) (grill-me / grill-with-docs / handoff) + [Dex Horthy](https://github.com/humanlayer/12-factor-agents) (12-Factor Agents). From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype.*
