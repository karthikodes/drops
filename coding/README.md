# 4 Claude Code plugins to install before you vibe-code

You commented **CODING**. Here are the four plugins from the reel, what each one does, and how to install them. I run all four.

Type these inside Claude Code (not in your normal terminal).

## 1. Supabase: Claude talks to your database

Runs SQL, writes migrations, generates types and checks your security advisors, so you don't live in the dashboard.

```
/plugin install supabase@claude-plugins-official
```

Then connect your Supabase account when it asks.

## 2. Superpowers: plan first, then build

Before Claude writes code, it brainstorms with you, writes a plan, builds in small steps and tests as it goes (red/green TDD). Almost 300k stars on GitHub ([obra/superpowers](https://github.com/obra/superpowers)).

```
/plugin install superpowers@claude-plugins-official
```

## 3. frontend-design: stop the "every AI app looks the same" look

Anthropic's own plugin for distinctive, production-grade UI instead of generic AI styling.

```
/plugin install frontend-design@claude-plugins-official
```

Tip: tell it who the site is for and one reference you love, then ask for a design plan before code.

## 4. Codex: a second AI reviews Claude's code

OpenAI's official plugin ([openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)). Works with a ChatGPT account (free included) or an OpenAI API key.

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

Then, after Claude finishes a change: `/codex:review` (or `/codex:adversarial-review` for a tougher pass).

## If a plugin isn't found

Add Anthropic's official marketplace first, then retry:

```
/plugin marketplace add anthropics/claude-plugins-official
```
