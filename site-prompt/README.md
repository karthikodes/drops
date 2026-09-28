# Build a website from a site you love

You commented **PROMPT**. Here's the prompt, built from how I made my site: one site you love as the reference, and the AI interviews you before it builds anything. Play with the result at [karthikodes.com](https://karthikodes.com) (move your mouse over my face).

## Why it works

Most AI-built sites look the same because they start from a prompt, and a prompt gets you the average website. A reference gives the AI your taste. And instead of you trying to describe a whole design in one message, the AI asks you questions, one at a time.

That second part has a name. Researchers call it the **Flipped Interaction pattern**: "flip the interaction flow so the LLM asks the user questions to achieve some desired goal" (White et al., 2023, [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/abs/2302.11382)).

## The prompt

Paste this into Claude (or any strong model), with your link in the first line:

```
I want a website like this one: [paste the link to a site you love]

First, look at it and tell me in plain words what makes it work: the layout, the type, and the one interaction people remember.

Then, before you build anything, ask me questions, one at a time, until you know:
1. Who the site is for, and the one thing a visitor should do next.
2. What should feel like the reference, and what must be mine.
3. My colours, fonts and photos. I'll send real photos; don't generate my face.
4. The one thing a visitor will want to play with.

After each answer, tell me what it changed in the plan. When you have enough, describe the first screen only and wait for my OK before you write any code.

Rules: don't copy their code, images, logo or words. Rebuild the idea with my content.
```

## How to use it

- **Claude.ai:** paste the prompt, answer the questions, and ask for the first screen as an artifact. Then build one section at a time.
- **Claude Code:** same prompt, in an empty folder. Ask it to run the site locally so you can see each change.
- **When something's off,** send a screenshot and say what feels wrong ("too dark", "not my colours", "the face doesn't look like me"). My site went through many versions this way.
- **Deploying:** once you like it, ask how to put it online for free. Many hosts have free plans for a static site.

## Host it for $0 a month (how mine runs)

My site sits in a private Amazon S3 bucket behind Amazon CloudFront on the **flat-rate Free plan: $0 a month, no overage charges** (AWS's CloudFront pricing page lists it). The domain name is separate and costs extra.

1. Ask Claude to build the site as static files (HTML, CSS, JS), or export it from wherever you built it.
2. Create a private S3 bucket and upload the files.
3. Create a CloudFront distribution with that bucket as the origin (Origin Access Control, so the bucket stays private), and pick the Free flat-rate plan.
4. Point your domain at CloudFront.
5. Set an AWS budget alert (a few dollars), just in case.

Or paste this into Claude Code in your site's folder:

```
Deploy this static site to a private S3 bucket behind CloudFront using the flat-rate Free plan. Keep the bucket private (Origin Access Control), add HTTPS, set a $5 AWS budget alert, and walk me through each step before you run it.
```

## Honest notes

- It took me a lot of back and forth. The prompt gets you started; your answers make it yours.
- Use a reference for its idea, not its assets. Their code, photos, logo and words belong to them.
