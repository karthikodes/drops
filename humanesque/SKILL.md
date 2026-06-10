---
name: humanesque
description: Make AI text read like a person wrote it — pattern removal PLUS rhythm, specificity, and controlled imperfection. Use when rewriting or drafting anything a human will read and judge (emails, posts, docs). Goes beyond tell-deletion: it rebuilds the prose the way people actually write.
---

# Humanesque

Removing AI tells isn't enough — detectors (and readers) key on **uniform rhythm and probable word choices**, not just "delve" and em-dashes. This skill does both: strip the patterns, then rebuild the texture.

## Step 1 — Strip the tells (the standard pass)
Remove/replace, preserving meaning and length:
- **Puffery & significance**: "stands as", "testament to", "pivotal", "underscores", "marking a", "evolving landscape"
- **-ing trailers**: "...,(highlighting/showcasing/reflecting/ensuring) ..." → cut or make a plain second sentence
- **Promo voice**: "boasts", "vibrant", "seamless", "robust", "groundbreaking", "nestled", "stunning"
- **Weasel attributions**: "experts argue", "observers note", "industry reports" → name the source or cut the claim
- **Inflated verbs**: leverage→use, utilize→use, streamline→simplify, facilitate→help
- **Structural tells**: rule-of-three everywhere, negative parallelism ("It's not X. It's not Y. It's Z."), "Here's the thing", "Let's dive in", emoji section headers, bullet lists where two sentences would do, balanced "not only…but also"
- **Punctuation tells**: em-dash chains (max one per ~150 words), colon-led setups ("The result: …"), full stops are fine — but no ellipsis trailing…

## Step 2 — Rebuild the texture (what tell-deletion misses)
1. **Burstiness on purpose.** Sentence lengths must vary hard: put a 3–6 word sentence next to a 25+ word one. If three consecutive sentences are within ±4 words of each other, rewrite one.
2. **Concrete beats abstract.** Replace every vague quantity with a specific one the author would actually know ("a lot of files" → "4,312 files"; "much faster" → "41s down to 10s"). Specifics are the strongest human signal there is.
3. **One small imperfection per ~150 words** (where register allows): a sentence fragment. Starting with And or But. A short aside in parentheses. Don't stack them.
4. **First-person stakes** (casual/personal registers only): what it cost, what surprised, what's still unresolved. One honest uncertainty beats three insights.
5. **Kill the wrap-up bow.** No "In conclusion", no closing line that restates the lesson. End on the last concrete fact or a forward action.
6. **Transitions like a person**: drop "Additionally/Moreover/Furthermore". Just start the next point, or use "Also", "Turns out", "One more thing".
7. **Register check**: technical/reference text stays neutral and plain (that IS the human voice there) — apply 1–2 and 5–6 only; skip fragments and first-person.

## Step 3 — Read-aloud audit
Read the result as if speaking to one specific person. Any sentence you wouldn't say out loud, rewrite. Any sentence that could appear unchanged in 1,000 other people's text, sharpen with a specific.

## Output
Return only the rewritten text. Same coverage as the original (don't drop content), same approximate length (±15%), same register.

---
*From @karthikodes (AI Without The Hype). Built on Wikipedia's "Signs of AI writing" + detector-behavior testing — see the results table in this folder. Companion to (and tested against) blader/humanizer.*
