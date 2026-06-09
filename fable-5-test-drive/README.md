# Claude Fable 5 — the plan-by-plan breakdown + 14-day test drive

You commented **FABLE** on [@karthikodes](https://instagram.com/karthikodes). Here's the drop: page 1 is the breakdown from the reel, page 2 is the part that actually matters — **how to reach your own verdict before the free window closes on June 22.**

> No hype: Fable 5 is genuinely the strongest Claude yet (Anthropic's claim is "state-of-the-art on nearly every benchmark *they* tested"). It's also 2× the price of Opus 4.8 after the window. The only question that matters is whether it earns that on **your** work. That's testable. In 14 days. For free.

---

## Page 1 — Where you can use it (and what it costs)

| Surface | Status |
|---|---|
| **Free plan (claude.ai)** | ❌ Not included |
| **Pro / Max / Team / seat-based Enterprise** | ✅ Included at no extra cost **through June 22, 2026** |
| **June 23 onward** | Pulled from those plans → needs **usage credits** (pay-per-use) |
| **API (Claude Platform)** | `claude-fable-5` — **$10 / M input · $50 / M output** (= 2× Opus 4.8's $5/$25; less than half Mythos Preview) |
| **Claude Code / Cowork** | ✅ Live now — `/model` → Fable 5 |
| **GitHub Copilot** | ✅ Generally available (Jun 9) |
| **Amazon Bedrock / AWS** | ✅ Available |
| **Claude Mythos 5** | Restricted release (vetted cyberdefense/infra partners; some safeguards lifted) — not for general use |

Two honest footnotes most posts skip:
1. **The paywall might be temporary.** Anthropic, verbatim: *"If capacity allows, we'll extend the included window"* and they *"aim to restore Fable 5 as a standard part of subscription plans."* Watch their announcements around Jun 22.
2. **The safety fallback is loud, not silent.** Risky topics (cyber/bio/chem) get answered by Opus 4.8 instead — it triggers in <5% of sessions, and Claude tells you when it happens.

## Page 2 — You have 14 days. Test it like this.

**1. Switch (30 seconds)**
- Claude Code: type `/model` → pick **Fable 5**
- claude.ai (paid): model picker → Fable 5
- API: `model: "claude-fable-5"`

**2. Don't waste it on small prompts.** Anthropic's own claim: *the longer the task, the bigger Fable's lead.* Short Q&A won't show you anything Opus can't do. Point it at:
- a **multi-file refactor** you've been putting off
- one **feature end-to-end** (plan → code → tests → review) in a real repo
- a **long agentic run** — let it work a big task autonomously and count how often you had to step in
- a **research + synthesis** task with many sources

**3. Run your own A/B — once.** Same task, same prompt, Opus 4.8 vs Fable 5. Score what actually costs you money: turns to done, number of steers/corrections, whether the tests passed first try. Benchmarks converged; *your repo* is the benchmark that matters.

**4. Do the cost math before Jun 23.** Formula: `(input M tokens × $10) + (output M tokens × $50)`. Read your real usage from your provider's usage dashboard (Claude Code: `/cost`). Illustrative only: a day that burns 1M in + 200k out ≈ **$20/day** on credits — versus staying on Opus 4.8 at half that, or your existing plan allowance. Decide per task-type, not globally: heavy long-horizon work → maybe worth credits; the everyday short loop → cheaper models stay fine.

**5. The open question we're testing ourselves:** Boris Cherny (creator of Claude Code) says Fable needs *"less prompts and steers… higher trust & autonomy."* If that holds, some of the scaffolding you built for weaker models (heavy steering, micro-prompts) may matter less — but **structure still beats yelling** (plan-first, shared glossary, guard the context window). We're testing how much; treat it as a hypothesis, not a fact.

**Verdict rubric:** if Fable saved you real turns/steers on the long tasks in your A/B → keep it for those tasks on credits after Jun 23. If it didn't → you just saved yourself 2× the price, with receipts.

---

*Sources: [Anthropic launch post](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [Boris Cherny](https://www.threads.com/@boris_cherny/post/DZX7he_GsjP) · [GitHub changelog](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/) · [AWS](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/). Availability/dates checked 2026-06-10 — re-verify after Jun 22.*

*From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype.*
