#!/usr/bin/env python3
"""check_scrape — run ScrapeGraphAI and tell you when it silently failed.

The problem this solves: on bot-protected pages ScrapeGraphAI returns a
well-formed EMPTY result — no error, no warning — and still bills you for the
prompt tokens. If you don't check, you conclude "there was nothing there."

Two tells, both measured on real runs:
  1. Empty/near-empty payload.
  2. Suspiciously FAST. Real extractions took 8.7s and 20.5s; the blocked
     page came back in 2.1s because there was nothing to read.

Usage:
    python check_scrape.py <url> "<what you want>"
Exit code 0 = trustworthy result, 1 = probably blocked.
"""
import json, os, sys, time, warnings
warnings.filterwarnings("ignore")

FAST_FAIL_SECONDS = 4.0   # under this + empty  => almost certainly blocked
MIN_ITEMS         = 1

def count_items(out):
    if isinstance(out, list):
        return len(out)
    if isinstance(out, dict):
        best = 0
        for v in out.values():
            if isinstance(v, list):
                best = max(best, len(v))
            elif isinstance(v, dict):
                best = max(best, count_items(v))
        return best
    return 0

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    url, prompt = sys.argv[1], sys.argv[2]

    api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY (or OPENROUTER_API_KEY) first.")
        print("Reminder: this tool is NOT subscription-free — you pay per page in LLM tokens.")
        return 2

    from scrapegraphai.graphs import SmartScraperGraph
    cfg = {"llm": {"api_key": api_key, "model": "openai/gpt-4o-mini"}, "verbose": False, "headless": True}
    if os.environ.get("OPENROUTER_API_KEY"):
        cfg["llm"]["base_url"] = "https://openrouter.ai/api/v1"

    t0 = time.time()
    graph = SmartScraperGraph(prompt=prompt, source=url, config=cfg)
    out = graph.run()
    secs = time.time() - t0

    n = count_items(out)
    tokens = 0
    try:
        info = graph.get_execution_info() or []
        if isinstance(info, list):
            tokens = sum(s.get("prompt_tokens", 0) or 0 for s in info)
    except Exception:
        pass

    print(json.dumps(out, indent=1)[:2000])
    print(f"\n— {n} item(s) in {secs:.1f}s · {tokens} prompt tokens")

    if n < MIN_ITEMS and secs < FAST_FAIL_SECONDS:
        print(f"\n⚠️  LIKELY BLOCKED — empty result returned in {secs:.1f}s "
              f"(real extractions take longer). You were still billed {tokens} tokens.")
        print("   Try: headless=False, a different page, or an official API.")
        return 1
    if n < MIN_ITEMS:
        print(f"\n⚠️  EMPTY RESULT — no error raised, but nothing was extracted. "
              f"Billed {tokens} tokens. Check the page actually contains this data.")
        return 1

    print("\n✅ Result looks trustworthy.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
