# The AI scraper setup — and how to tell when it silently failed

Everyone is posting the "free Claude skill that scrapes unlimited leads." The tool underneath is real and good. It also fails in a way that will quietly cost you money if nobody warns you.

I ran it. Here's exactly what happened, and the setup I use.

## What it actually is

**[ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** — 28.7k stars, MIT licensed, actively maintained. A Python library that points an LLM at a web page and returns structured data from a plain-English prompt. It is genuinely good.

Two things the reels leave out:

1. **It is not "zero subscriptions."** It runs on *your* LLM API key. The repo's own comparison table lists the open-source cost model as *"LLM tokens + your own infra."* You are swapping a scraper subscription for token spend. It's only truly free if you run a local model via Ollama.
2. **`pip install` alone will not work.** You also need the Playwright browser binary (~92 MB).

## Install (the version that works)

```bash
pip install scrapegraphai
playwright install chromium        # ← the step nobody mentions
export OPENAI_API_KEY="sk-..."     # or OPENROUTER_API_KEY
```

## My real test results

Same library, same prompt style, three sites:

| Site | Time | Prompt tokens | Items | Result |
|---|---|---|---|---|
| books.toscrape.com (static) | 20.5s | 7,234 | **20** | works |
| news.ycombinator.com | 8.7s | 8,634 | **10** | works |
| remoteok.com (bot-protected) | **2.1s** | 6,564 | **0** | **silently empty** |

The third one is the problem. It returned:

```json
{ "job_openings": [] }
```

No error. No warning. It **still consumed 6,564 prompt tokens** to return nothing. If you didn't know better you'd conclude the page had no jobs on it.

## The tell

Look at the timings. The scrapes that genuinely worked took **8.7s and 20.5s**. The blocked one came back in **2.1s** — because there was nothing to read, so there was nothing to think about.

**Fast + empty = you got blocked.**

## The check

`check_scrape.py` in this folder wraps a normal run and refuses to let a silent failure pass. It flags any result that is empty *and* suspiciously fast, tells you how many tokens you were billed, and exits non-zero so you can use it in a pipeline.

```bash
python check_scrape.py "https://news.ycombinator.com" "top stories: title, points"
```

```
— 10 item(s) in 8.7s · 8,634 prompt tokens
✅ Result looks trustworthy.
```

```
— 0 item(s) in 2.1s · 6,564 prompt tokens
⚠️  LIKELY BLOCKED — empty result returned in 2.1s (real extractions take
   longer). You were still billed 6,564 tokens.
```

## What I did not test, and why

**LinkedIn.** Several reels claim this works there. Scraping LinkedIn violates their Terms of Service and is a well-documented way to get your account restricted or banned. I'm not going to demo that and I'd suggest you don't run it — use their official API or a licensed data provider if you need that data.

## Honest limits

- Bot-protected and heavily JavaScript-driven sites will fail, often silently. That's the norm, not the exception.
- Cost scales per page. At ~7–9k prompt tokens each, a few thousand pages is real money.
- The library's own `total_cost_USD` reported **0** on a non-native provider — don't trust it for budgeting.
- Respect `robots.txt` and site terms. "It's technically possible" is not the same as "you're allowed."

— @karthikodes · AI Without The Hype · you commented SCRAPE
