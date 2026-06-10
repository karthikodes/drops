# humanesque — make Claude sound human

You commented **HUMAN**. Here's the skill, plus every screenshot from the test that produced it.

The viral Humanizer skill (23k★) cut Claude's average "AI probability" from **39% → 17%** across three real detectors. This rebuilt version takes the same texts to **~0%** — including a README both others failed at 99.5% / 100%.

---

## 1 · Install it (2 minutes)

The whole skill is one file: [`SKILL.md`](./SKILL.md).

**Claude.ai (web/desktop):**
1. Download [`SKILL.md`](./SKILL.md)
2. Claude → **Settings → Capabilities → Skills → Upload skill**
3. Done. Claude now applies it whenever you ask for human-sounding text.

**Claude Code:**
```bash
mkdir -p ~/.claude/skills/humanesque
curl -o ~/.claude/skills/humanesque/SKILL.md \
  https://raw.githubusercontent.com/karthikodes/drops/main/humanesque/SKILL.md
```

**No Claude at all?** Open [`SKILL.md`](./SKILL.md) and paste the three passes straight into any model's prompt. It's just instructions.

## 2 · Use it

After installing, prompt like this:

> Rewrite this with the humanesque skill: *[your draft]*

Or bake it into real work:

> Write the launch email for X. Run it through humanesque before showing me.

What it does to your text, in one example:

| | |
|---|---|
| **Before (raw Claude)** | *"This update streamlines the workflow, ensuring a seamless experience and significantly faster processing times."* |
| **After (humanesque)** | *"Processing dropped from 41s to 10s. The workflow lost two steps. That's the whole update."* |

Same information. One reads like a press release, one reads like a person who actually ran the thing.

## 3 · The receipts

Three texts (an email, a LinkedIn post, a README) × three versions (**A** raw Claude, **B** viral Humanizer, **C** humanesque) × three detectors, all run in a real browser, all screenshotted.

The hardest case — a plain README that detectors hate:

| A · raw Claude — **99.5%** | B · Humanizer — **100%** | C · humanesque — **0.1%** |
|---|---|---|
| ![raw](./cards/sapling_A.png) | ![humanizer](./cards/sapling_B.png) | ![humanesque](./cards/sapling_C.png) |

- **All 27 detector runs:** [`shots/`](./shots) (named `detector_VERSION_text.png`)
- **Full score matrix + averages:** [`results.md`](./results.md) · [`results.csv`](./results.csv)
- **The exact test texts:** [`test-texts/`](./test-texts) — read A vs C of the same text, the difference is obvious
- **The prompts used to generate each version:** [`prompts.md`](./prompts.md)

## 4 · Why the viral skill wasn't enough

[blader/humanizer](https://github.com/blader/humanizer) (Siqi Chen, 23k★) strips the famous tells — "delve", em-dash chains, puffery, rule-of-three. That genuinely works: it cut our average from 39% to 17%.

But detectors (and readers) key on two things tell-deletion can't fix:

1. **Rhythm.** Humans don't write same-length sentences. Models do.
2. **Specifics.** "Significantly faster" is a model phrase. "41s down to 10s" is a person who measured it.

Humanesque keeps the pattern-stripping (Pass 1), then **rebuilds the texture** — burstiness, concrete numbers, one controlled imperfection per ~150 words, no wrap-up bow (Pass 2), and a read-aloud audit (Pass 3). That's what took the 100%-AI README to 0.1%.

## The honest part

AI detectors are **not truth**. They flag plain technical writing as "AI" no matter who wrote it — our raw *and* humanized READMEs both scored ~100% until the texture pass. And one detector (QuillBot) timed out on all three email runs; those cells are excluded from the averages, not hidden.

Treat detector scores as a proxy for "does this read like a bot" — because that's the same heuristic your readers run in their heads.

---

*From [@karthikodes](https://instagram.com/karthikodes) — AI Without The Hype. Tested 2026-06-10 with ZeroGPT, QuillBot, Sapling. Built on Wikipedia's "Signs of AI writing" + detector-behavior testing.*
