# 25 Claude skills worth installing

You commented **SKILLS**. Here are all 25 from the reel, with the link, what each one is for, and how to install and use it.

I checked 59 skills on GitHub on 28 September 2026 and kept the ones that are real, recently updated and install cleanly. Star counts and "updated" dates are from that day. Nothing here is paid, and no link is an affiliate link.

- **Most starred, as in the reel:** [Superpowers](#19-superpowers) (292K stars), [Grill Me](#11-grill-me) (271K), [Anthropic's Excel, Word, PowerPoint and PDF skills](#2-excel-word-powerpoint-and-pdf) (179K), [Humanizer](#3-humanizer) (52K)
- **Top 3 for most people:** [Proposal Builder](#1-proposal-builder), [the Excel, Word, PowerPoint and PDF skills](#2-excel-word-powerpoint-and-pdf), [Humanizer](#3-humanizer)
- **Get paid:** 1, 4, 5, 6, 7
- **Office work and writing:** 2, 3, 8, 9, 25
- **Think it through:** 10, 11, 12
- **Research and content:** 13 to 18
- **For coders:** 19 to 24

---

## First: how to install a skill

A skill is a folder with a `SKILL.md` file of instructions (sometimes with scripts). Claude reads it only when your request needs it.

**On Claude.ai (web, desktop, mobile)**
1. Go to Settings > Capabilities and turn on **Code execution and file creation**. That also switches on Anthropic's built-in Excel, Word, PowerPoint and PDF skills.
2. Go to **Customize > Skills**. Toggle Anthropic's example skills on or off there.
3. To add someone else's skill: zip the skill folder (the one with `SKILL.md` in it), then in Customize > Skills click **+ > Create skill > Upload a skill**.

**In Claude Code (terminal)**
- Plugins: `/plugin marketplace add owner/repo`, then `/plugin install plugin-name@marketplace-name`. Anything in Anthropic's official marketplace installs with just `/plugin install name@claude-plugins-official`.
- The open skills installer: `npx skills add owner/repo` (works for Claude Code and 75+ other agents).
- By hand: put the folder at `~/.claude/skills/<skill-name>/SKILL.md`.

**In Cowork (Claude desktop app):** install plugins from [claude.com/plugins](https://claude.com/plugins/).

**Be careful with skills from strangers.** A skill can tell Claude to run code. Anthropic's own advice is to install skills only from sources you trust and to read the files first, especially scripts and anything that calls the internet. NVIDIA's [SkillSpector](https://github.com/NVIDIA/SkillSpector) scanner found vulnerabilities in 26.1% of the 31,132 skills it analysed, and signs of malicious intent in 5.2%. To scan one yourself:

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
skillspector scan ./the-skill-folder
```

---

## Get paid

### 1. Proposal Builder
[anthropics/knowledge-work-plugins > small-business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business/skills/proposal-builder) · by Anthropic · 25.8k stars · updated 15 Sep 2026

Turns call notes, a voice memo or an RFP, plus your price list, into a priced proposal or statement of work in your own template (DOCX and PDF).
- **Install:** Cowork: claude.com/plugins > Small Business. Claude Code: `claude plugin marketplace add anthropics/knowledge-work-plugins && claude plugin install small-business@knowledge-work-plugins`
- **Use:** "Build a proposal from these notes", then paste the notes and upload your rate card. It shows you the draft and sends nothing without your OK.

The same plugin has 44 skills, including a Grant and RFP Writer and a 30/60/90-day Cash Flow Snapshot.

### 4. Invoice Chase
[small-business/invoice-chase](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business/skills/invoice-chase) · by Anthropic · same plugin as #1

Drafts reminders for overdue invoices, gentle for good payers and firm for repeat late payers.
- **Install:** comes with #1.
- **Use:** "Who owes me money?" Connect QuickBooks, Xero or Stripe, or just upload your unpaid-invoices report as a CSV. Nothing is sent until you approve it.

### 5. Sales: Call Prep and Draft Outreach
[knowledge-work-plugins > sales](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales) · by Anthropic · updated 21 Sep 2026

A one-page brief before any sales call, plus personalised outreach emails and follow-up sequences.
- **Install:** `claude plugin marketplace add anthropics/knowledge-work-plugins && claude plugin install sales@knowledge-work-plugins` (or Cowork > claude.com/plugins)
- **Use:** `/sales:call-prep Acme` or `/sales:draft-outreach` followed by who you're writing to.

### 6. Marketing Skills
[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · by Corey Haines · 51.7k stars · updated 5 Sep 2026

About 45 marketing skills: copywriting, cold email, pricing pages, offers, landing-page conversion, SEO audits, launch plans.
- **Install:** `npx skills add coreyhaines31/marketingskills` (or `/plugin marketplace add coreyhaines31/marketingskills` then `/plugin install marketing-skills@marketingskills`)
- **Use:** "Write the copy for my pricing page" or "Draft a 3-email cold sequence for my offer."

### 7. Pitch Deck (Claude for Financial Services)
[anthropics/financial-services](https://github.com/anthropics/financial-services) · by Anthropic · 37.9k stars · updated 21 Sep 2026

Fills your pitch-deck template with numbers from Excel or CSV files; also builds comps, teasers and one-page company profiles.
- **Install:** `claude plugin marketplace add anthropics/financial-services && claude plugin install investment-banking@claude-for-financial-services`
- **Use:** "Populate this pitch deck template from comps.xlsx." Built for finance teams; check every number before it leaves your desk.

---

## Office work and writing

### 2. Excel, Word, PowerPoint and PDF
[anthropics/skills](https://github.com/anthropics/skills/tree/main/skills) · by Anthropic · 178.7k stars · updated 17 Jul 2026

Claude hands you real files: spreadsheets with working formulas, Word documents, slide decks and PDFs, instead of text you have to paste and format.
- **Install:** Claude.ai: they're built in. Turn on Settings > Capabilities > Code execution and file creation. Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills`
- **Use:** "Make this a spreadsheet with a formula for the monthly total" or "Turn these notes into a 10-slide deck."

### 3. Humanizer
[blader/humanizer](https://github.com/blader/humanizer) · by Siqi Chen · 52.4k stars · updated 6 Sep 2026 · MIT

Rewrites AI-sounding text so it reads like a person wrote it, based on Wikipedia's "Signs of AI writing" guide. Posts, emails and captions stop reading like ChatGPT without a manual rewrite.
- **Install:** `npx skills add blader/humanizer --global` (or `/plugin marketplace add blader/humanizer` then `/plugin install humanizer@humanizer`). Claude.ai: upload the `SKILL.md` in a zipped folder.
- **Use:** Paste a draft and type `/humanizer`, or say "make this sound human."
- **Upgrade:** my rebuilt version, with a rhythm pass and a specifics pass, tested on three AI detectors: [drops/humanesque](https://github.com/karthikodes/drops/tree/main/humanesque).

### 8. Contract and NDA Review
[knowledge-work-plugins > legal](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) · by Anthropic · updated 21 Sep 2026

Sorts an NDA into green, yellow or red, and reviews contracts against your own rules with suggested edits.
- **Install:** `claude plugin install legal@knowledge-work-plugins` (after adding the marketplace as in #5)
- **Use:** `/legal:triage-nda`, then upload the NDA. It's a first pass, not legal advice; a lawyer still signs off on the red ones.

### 9. Build Dashboard
[knowledge-work-plugins > data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data) · by Anthropic · updated 21 Sep 2026

Turns a spreadsheet into an interactive dashboard (an HTML file) with KPI cards, charts and filters.
- **Install:** `claude plugin install data@knowledge-work-plugins`
- **Use:** "Build a dashboard from sales.csv with monthly revenue and top customers."

### 25. Skill Creator
[anthropics/skills > skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) · by Anthropic · updated 20 Apr 2026

The one that builds new skills for you. It asks about a task you repeat, writes the skill, then tests and improves it.
- **Install:** Claude.ai: Customize > Skills, switch on **skill-creator**. Claude Code: `/plugin install skill-creator@claude-plugins-official`
- **Use:** "Help me make a skill for my weekly client report."

---

## Think it through

### 10. LLM Council
[aiwithremy/claude-skills-llm-council](https://github.com/aiwithremy/claude-skills-llm-council) · by Ole Lehmann · 2.3k stars · updated 26 Apr 2026

Runs a decision past five AI advisors who each take a different angle, review each other, then give one verdict showing where they agree and clash.
- **Install:** Claude.ai: download `SKILL.md`, put it in a folder called `llm-council`, zip it, upload it. Claude Code: `mkdir -p ~/.claude/skills/llm-council && curl -o ~/.claude/skills/llm-council/SKILL.md https://raw.githubusercontent.com/aiwithremy/claude-skills-llm-council/main/SKILL.md`
- **Use:** "Council this: should I launch a $97 workshop or a $497 course?"

### 11. Grill Me
[mattpocock/skills > grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) · by Matt Pocock · 270.8k stars · updated 18 Sep 2026

Claude interviews you about your plan, one hard question at a time, until nothing is left vague.
- **Install:** Claude Code: `/plugin install mattpocock-skills` (it's in the official marketplace) or `npx skills@latest add mattpocock/skills`
- **Use:** `/grill-me`, then describe the plan. (It uses the `grilling` skill too, so keep both.)

### 12. Prompt Master
[nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) · by Nidhin Joseph Nelson · 13.7k stars · updated 24 Aug 2026

Writes a tight prompt for another AI tool (Midjourney, Lovable, Cursor, ChatGPT, video generators) from your rough idea.
- **Install:** Claude.ai: Customize > Skills > Upload. Claude Code: `git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master`
- **Use:** "Write me a Midjourney prompt for a cosy reading nook at night."

---

## Research and content

### 13. last30days
[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · by Matt Van Horn · 63.0k stars · updated 23 Sep 2026

Finds what people actually said about a topic in the last 30 days across Reddit, YouTube, Hacker News, X and more, and sums it up.
- **Install:** Claude Code: `/plugin marketplace add mvanhorn/last30days-skill` then `/plugin install last30days@last30days-skill`. Claude.ai: download `last30days.skill` from the repo's latest release and upload it.
- **Use:** `/last30days` plus your topic. Works with no API keys (web only); optional keys add more sources.

### 14. LinkedIn Skills
[sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) · by Serge Bulaev · 3.6k stars · updated 23 Sep 2026

Twelve skills that plan, write and repurpose LinkedIn posts, comments and replies in your own voice.
- **Install:** `npx skills add sergebulaev/linkedin-skills`
- **Use:** "Turn this blog post into three LinkedIn posts in my voice." Drafting needs no keys; skip the optional auto-posting service and paste the posts yourself.

### 15. Obsidian Skills
[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · by Steph Ango, CEO of Obsidian · 49.0k stars · updated 15 Sep 2026

Teaches Claude to work with your Obsidian notes properly: links, bases, canvases and clean web clipping.
- **Install:** `/plugin marketplace add kepano/obsidian-skills` then `/plugin install obsidian@obsidian-skills`
- **Use:** Open Claude Code in your vault: "Turn today's meeting notes into linked notes."

### 16. Book to Skill
[virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) · by Virgilio Junior · 32.8k stars · updated 22 Sep 2026

Turns a book PDF or a folder of documents into a skill Claude can look things up in while you work.
- **Install:** `npx skills add virgiliojr94/book-to-skill`
- **Use:** `/book-to-skill path/to/book.pdf`, then ask questions about the book in any later chat.

### 17. Frontend Slides
[zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · by Zara Zhang · 29.9k stars · updated 23 Jun 2026

Makes animated web slide decks from a short brief, or converts an existing PowerPoint into one.
- **Install:** `/plugin marketplace add https://github.com/zarazhangrui/frontend-slides` then `/plugin install frontend-slides@frontend-slides`
- **Use:** "Make a 10-slide deck about my Q3 results" or "Convert deck.pptx to web slides."

### 18. HyperFrames
[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) · by HeyGen · 53.7k stars · updated 28 Sep 2026

Lets Claude make MP4 videos out of HTML: captions, motion graphics, explainers, promos. I build my reels with it.
- **Install:** `/plugin install hyperframes@claude-plugins-official`
- **Use:** "Make a 20-second captioned promo for my product page."

---

## For coders

### 19. Superpowers
[obra/superpowers](https://github.com/obra/superpowers) · by Jesse Vincent · 292.2k stars · updated 25 Sep 2026

A full method for coding with an agent: brainstorm, plan, test first, debug, review.
- **Install:** `/plugin install superpowers@claude-plugins-official`
- **Use:** Start with "let's build X". It asks questions and writes a plan before any code.

### 20. Frontend Design
[anthropics/skills > frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) · by Anthropic · updated 3 Sep 2026

Steers Claude away from the default purple-gradient AI look toward deliberate type and layout.
- **Install:** `/plugin install frontend-design@claude-plugins-official`
- **Use:** Just ask for a page; it applies itself.

### 21. Impeccable
[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · by Paul Bakaus · 71.9k stars · updated 25 Sep 2026

A design language plus 24 commands (polish, typography, contrast) and 61 checks for AI-looking interfaces.
- **Install:** `npx impeccable install`, then `/impeccable init` inside Claude Code
- **Use:** `/impeccable polish` on a page that looks off.

### 22. Graphify
[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) · by Graphify Labs · 121.9k stars · updated 27 Sep 2026

Maps your codebase, docs and PDFs into a knowledge graph that Claude queries instead of re-reading files.
- **Install:** `uv tool install graphifyy && graphify install` (yes, two y's)
- **Use:** `/graphify` in your project, then ask how things connect.

### 23. Planning with Files
[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) · by Ahmad Othman Ammar Adi · 27.2k stars · updated 27 Sep 2026

Keeps the plan, findings and progress in files on disk, so long tasks survive `/clear` and crashes.
- **Install:** `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`
- **Use:** Kicks in on multi-step tasks. It adds a hook that runs every turn; read it first.

### 24. Agent Browser
[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) · by Vercel · 43.3k stars · updated 22 Sep 2026

Gives Claude a real browser it drives from the terminal: open, click, fill, screenshot.
- **Install:** `npm install -g agent-browser && agent-browser install && npx skills add vercel-labs/agent-browser`
- **Use:** "Open my app on localhost and check the signup flow works." Keep it away from logged-in accounts you care about.

---

## Honest notes

- **Made by Anthropic (9 of 25):** 1, 2, 4, 5, 7, 8, 9, 20 and 25. The rest are community projects; read them before you install.
- **Needs Claude Code or Cowork:** most plugins here. #2 is built into Claude.ai and #25 is one of its example skills you switch on; #3, #10 and #12 upload to Claude.ai in a minute.
- **Connectors are optional.** #1, #4 and #5 get better with your accounting or CRM tools connected, but work from pasted notes and uploaded CSVs.
- **Numbers I didn't test are left out on purpose.** Some repos claim big token savings; I only list what each one does.
- **Want Humanizer upgraded?** My rebuilt version, with all the detector screenshots from my test, is in [drops/humanesque](https://github.com/karthikodes/drops/tree/main/humanesque) (keyword HUMAN).

Checked 28 September 2026 by [@karthikodes](https://instagram.com/karthikodes). *AI Without The Hype.*
