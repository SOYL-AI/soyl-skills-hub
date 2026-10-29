# firecrawl

Skills from [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) at commit [`13673be`](https://github.com/firecrawl/firecrawl/tree/13673be17227b3af0131e7f9c96b5a05152a34bd), copied into SOYL Hub on 2026-10-29. Licence: AGPL-3.0.

> Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥

All credit goes to the authors of firecrawl/firecrawl. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [firecrawl-build](firecrawl-build/) | Integrate Firecrawl into application code whenever a product, agent, or workflow needs web data inside the app — web search, live search results, page scraping… | ISC |
| [firecrawl-build-interact](firecrawl-build-interact/) | Integrate Firecrawl `/interact` into product code for dynamic pages and browser actions after scraping. Use when a feature needs clicks, form fills, pagination… | ISC |
| [firecrawl-build-onboarding](firecrawl-build-onboarding/) | Get Firecrawl credentials and SDK setup into a project. Use when an application needs `FIRECRAWL_API_KEY`, when an agent should add Firecrawl to `.env`, when the user… | ISC |
| [firecrawl-build-scrape](firecrawl-build-scrape/) | Integrate Firecrawl `/scrape` into product code for single-page extraction. Use when an app already has a URL and needs markdown, HTML, links, screenshots, metadata, or… | ISC |
| [firecrawl-build-search](firecrawl-build-search/) | Integrate Firecrawl `/search` into product code and agent workflows. Use when an app needs discovery before extraction, when the feature starts with a query instead of a… | ISC |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/research-and-scraping/firecrawl/firecrawl-build -g -a claude-code
```

Back to [Research and scraping](../../../catalog/research-and-scraping.md)
