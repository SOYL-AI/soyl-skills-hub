# Research and scraping

Web and paper research, notebooks, scraping and second brains.

124 skills here and 7 linked to their source, from 11 projects. [All categories](../CATALOG.md)

**To install a skill**, open it, copy the address from your browser and run `npx skills add <that address> -g -a claude-code`. More ways in [How to install](../README.md#install-a-skill). Skills marked ↗ live in their own repos: install them from there.

## gbrain

[garrytan/gbrain](https://github.com/garrytan/gbrain) · MIT · ★ 31.3k · 81 here

Garry's Opinionated OpenClaw/Hermes Agent Brain

81 skills: see [the full list](research-and-scraping--gbrain.md).

## deer-flow

[bytedance/deer-flow](https://github.com/bytedance/deer-flow) · MIT · ★ 84.7k · 27 here

An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

| Skill | What it does |
|---|---|
| [academic-paper-review](../skills/research-and-scraping/deer-flow/academic-paper-review/) | Use this skill when the user requests to review, analyze, critique, or summarize academic papers, research articles, preprints, or scientific publications. Supports… |
| [blocking-io-guard](../skills/research-and-scraping/deer-flow/blocking-io-guard/) | Ensure async-path backend code that could block the asyncio event loop is protected by a teeth-verified runtime anchor in tests/blocking_io/. Use when changing backend… |
| [bootstrap](../skills/research-and-scraping/deer-flow/bootstrap/) | Generate a personalized SOUL.md through a warm, adaptive onboarding conversation. Trigger when the user wants to create, set up, or initialize their AI partner's… |
| [chart-visualization](../skills/research-and-scraping/deer-flow/chart-visualization/) | This skill should be used when the user wants to visualize data. It intelligently selects the most suitable chart type from 26 available options, extracts parameters… |
| [claude-to-deerflow](../skills/research-and-scraping/deer-flow/claude-to-deerflow/) | Interact with DeerFlow AI agent platform via its HTTP API. Use this skill when the user wants to send messages or questions to DeerFlow for research/analysis, start a… |
| [code-documentation](../skills/research-and-scraping/deer-flow/code-documentation/) | Use this skill when the user requests to generate, create, or improve documentation for code, APIs, libraries, repositories, or software projects. Supports README… |
| [consulting-analysis](../skills/research-and-scraping/deer-flow/consulting-analysis/) | Use this skill when the user requests to generate, create, or write professional research reports including but not limited to market analysis, consumer insights, brand… |
| [data-analysis](../skills/research-and-scraping/deer-flow/data-analysis/) | Use this skill when the user uploads Excel (.xlsx/.xls) or CSV files and wants to perform data analysis, generate statistics, create summaries, pivot tables, SQL… |
| [deep-research](../skills/research-and-scraping/deer-flow/deep-research/) | Use this skill instead of WebSearch for ANY question requiring web research. Trigger on queries like "what is X", "explain X", "compare X and Y", "research X", or before… |
| [deerflow-maintainer-orchestrator](../skills/research-and-scraping/deer-flow/deerflow-maintainer-orchestrator/) | Use when a DeerFlow maintainer needs comment-only GitHub issue or PR handling: resolve issue/PR scopes with gh, analyze issues, post or draft issue comments, perform PR… |
| [engineer-system-change](../skills/research-and-scraping/deer-flow/engineer-system-change/) | Evaluate and carry out non-trivial software-system changes from first principles. Use when assessing RFCs, issues, designs, features, refactors, migrations, dependency… |
| [find-skills](../skills/research-and-scraping/deer-flow/find-skills/) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in… |
| [frontend-design](../skills/research-and-scraping/deer-flow/frontend-design/) | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters… |
| [github-deep-research](../skills/research-and-scraping/deer-flow/github-deep-research/) | Conduct multi-round deep research on any GitHub Repo. Use when users request comprehensive analysis, timeline reconstruction, competitive analysis, or in-depth… |
| [image-generation](../skills/research-and-scraping/deer-flow/image-generation/) | Use this skill when the user requests to generate, create, imagine, or visualize images including characters, scenes, products, or any visual content. Supports… |
| [music-generation](../skills/research-and-scraping/deer-flow/music-generation/) | Use this skill when the user requests to generate, create, compose, or produce music or songs — background music, theme songs, jingles, or instrumental tracks. Generates… |
| [newsletter-generation](../skills/research-and-scraping/deer-flow/newsletter-generation/) | Use this skill when the user requests to generate, create, write, or draft a newsletter, email digest, weekly roundup, industry briefing, or curated content summary… |
| [podcast-generation](../skills/research-and-scraping/deer-flow/podcast-generation/) | Use this skill when the user requests to generate, create, or produce podcasts from text content. Converts written content into a two-host conversational podcast audio… |
| [ppt-generation](../skills/research-and-scraping/deer-flow/ppt-generation/) | Use this skill when the user requests to generate, create, or make presentations (PPT/PPTX). Creates visually rich slides by generating images for each slide and… |
| [skill-creator](../skills/research-and-scraping/deer-flow/skill-creator/) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing… |
| [skill-reviewer](../skills/research-and-scraping/deer-flow/skill-reviewer/) | Reviews DeerFlow skill packages for readiness, triggers, safety boundaries, resources, and evidence. Invoke when users ask to audit, grade, or production-check an… |
| [smoke-test](../skills/research-and-scraping/deer-flow/smoke-test/) | End-to-end smoke test skill for DeerFlow. Guides through: 1) Pulling latest code, 2) Docker OR Local installation and deployment (user preference, default to Local if… |
| [surprise-me](../skills/research-and-scraping/deer-flow/surprise-me/) | Create a delightful, unexpected "wow" experience for the user by dynamically discovering and creatively combining other enabled skills. Triggers when the user says… |
| [systematic-literature-review](../skills/research-and-scraping/deer-flow/systematic-literature-review/) | Use this skill when the user wants a systematic literature review, survey, or synthesis across multiple academic papers on a topic. Also covers annotated bibliographies… |
| [vercel-deploy](../skills/research-and-scraping/deer-flow/vercel-deploy/) | Deploy applications and websites to Vercel. Use this skill when the user requests deployment actions such as "Deploy my app", "Deploy this to production", "Create a… |
| [video-generation](../skills/research-and-scraping/deer-flow/video-generation/) | Use this skill when the user requests to generate, create, or imagine videos. Supports structured prompts and reference image for guided generation. |
| [web-design-guidelines](../skills/research-and-scraping/deer-flow/web-design-guidelines/) | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against… |

## Awwwards-mcp

[INSANE0777/Awwwards-mcp](https://github.com/INSANE0777/Awwwards-mcp) · MIT · ★ 373 · 7 here

Free, open-source MCP server that gives AI coding agents (Claude Code, Codex, Cursor, OpenCode, ZCode…) design inspiration from award-winning websites — search with real screenshots, pull design DNA, capture and record live sites. A Mobbin alternative. No API key.

| Skill | What it does |
|---|---|
| [awwwards-doctor](../skills/research-and-scraping/Awwwards-mcp/awwwards-doctor/) | Use when awwwards-mcp scraping or tools stop working — BlockedError, "layout may have changed" parser errors, empty results, failed captures, stale searches — or when… |
| [awwwards-inspiration](../skills/research-and-scraping/Awwwards-mcp/awwwards-inspiration/) | Use when building a site that needs design references (e.g. "make it feel premium", "dark 3D portfolio vibes"), when the user asks for standalone inspiration research… |
| [awwwards-motion-study](../skills/research-and-scraping/Awwwards-mcp/awwwards-motion-study/) | Use when building a site whose reference has animation — before writing any motion code, and again when verifying a build. Teaches what to record from a live site (and… |
| [awwwards-section-loop](../skills/research-and-scraping/Awwwards-mcp/awwwards-section-loop/) | Use when recreating or rebuilding a multi-section page from a reference site — build section by section instead of all at once. Teaches the loop map… |
| [awwwards-setup](../skills/research-and-scraping/Awwwards-mcp/awwwards-setup/) | Use when the awwwards MCP server or its skills are invoked for the first time in a session or on a new machine — when no awwwards preferences exist yet, or the user asks… |
| [motion-authoring](../skills/research-and-scraping/Awwwards-mcp/motion-authoring/) | Use when a converted project (build_project --authored) needs its motion authored — turning motion.manifest.json + inert skeletons into real per-section/page motion with… |
| [recreate](../skills/research-and-scraping/Awwwards-mcp/recreate/) | Recreate a website from a link — evidence-driven reconstruction with the awwwards MCP. Use when the user says "recreate this site", "clone this page", "rebuild… |

## firecrawl

[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) · AGPL-3.0 · ★ 196.7k · 5 here

Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥

| Skill | What it does |
|---|---|
| [firecrawl-build](../skills/research-and-scraping/firecrawl/firecrawl-build/) | Integrate Firecrawl into application code whenever a product, agent, or workflow needs web data inside the app — web search, live search results, page scraping… |
| [firecrawl-build-interact](../skills/research-and-scraping/firecrawl/firecrawl-build-interact/) | Integrate Firecrawl `/interact` into product code for dynamic pages and browser actions after scraping. Use when a feature needs clicks, form fills, pagination… |
| [firecrawl-build-onboarding](../skills/research-and-scraping/firecrawl/firecrawl-build-onboarding/) | Get Firecrawl credentials and SDK setup into a project. Use when an application needs `FIRECRAWL_API_KEY`, when an agent should add Firecrawl to `.env`, when the user… |
| [firecrawl-build-scrape](../skills/research-and-scraping/firecrawl/firecrawl-build-scrape/) | Integrate Firecrawl `/scrape` into product code for single-page extraction. Use when an app already has a URL and needs markdown, HTML, links, screenshots, metadata, or… |
| [firecrawl-build-search](../skills/research-and-scraping/firecrawl/firecrawl-build-search/) | Integrate Firecrawl `/search` into product code and agent workflows. Use when an app needs discovery before extraction, when the feature starts with a query instead of a… |

## agent-reach

[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) · MIT · ★ 106.2k · 1 here

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

| Skill | What it does |
|---|---|
| [agent-reach](../skills/research-and-scraping/agent-reach/agent-reach/) | MUST USE when user wants to 调研/research/搜索/search/查/找/look up anything on the internet — e.g. 全网调研 X / 帮我调研一下 X / 查一下 X / 搜搜 X / 看看大家怎么评价 X / X 上有什么讨论 / research this… |

## anydoc

[firecrawl/anydoc](https://github.com/firecrawl/anydoc) · MIT · ★ 23.2k · 1 here

Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean Markdown. Built in Rust, with Node.js and Python bindings.

| Skill | What it does |
|---|---|
| [convert-documents-to-markdown](../skills/research-and-scraping/anydoc/convert-documents-to-markdown/) | Convert Word (.doc, .docx), PowerPoint (.ppt, .pptx), Excel (.xls, .xlsx), OpenDocument (.odt, .ods, .odp), RTF, EPUB, CSV, and PDF files to GitHub-Flavored Markdown… |

## google-maps-scraper

[gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) · MIT · ★ 7k · 1 here

scrape data from Google Maps. Extracts data such as the name, address, phone number, website URL, rating, reviews number, latitude and longitude, reviews,email and more for each place

| Skill | What it does |
|---|---|
| [google-maps-scraper](../skills/research-and-scraping/google-maps-scraper/google-maps-scraper/) | Find businesses, leads, emails, reviews, ratings, and contact details from Google Maps. Use for requests such as "find dentists in Berlin", "scrape Google Maps", "get… |

## notebooklm-skill

[PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) · MIT · ★ 7.8k · 1 here

Use this skill to enable Claude Code to communicate directly with your Google NotebookLM notebooks. Query your uploaded documents and get source-grounded, citation-backed answers from Gemini. Features browser automation, library management, persistent authentication, and answers exclusively from…

| Skill | What it does |
|---|---|
| [notebooklm](../skills/research-and-scraping/notebooklm-skill/notebooklm/) | Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library… |

## academic-research-skills

[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) · Non-commercial · ★ 54.5k · 5 linked

Academic Research Skills for Claude Code: research → write → review → revise → finalize

| Skill | What it does |
|---|---|
| [academic-paper ↗](https://github.com/Imbad0202/academic-research-skills/tree/main/academic-paper) | 12-agent academic paper writing pipeline. 11 modes… *(Non-commercial licence: install it from the source.)* |
| [academic-paper-reviewer ↗](https://github.com/Imbad0202/academic-research-skills/tree/main/academic-paper-reviewer) | Multi-perspective academic paper review with dynamic reviewer personas. Runs a 5-seat, role-separated review panel (Journal-Fit Reviewer + 3 peer-review roles + Devil's… *(Non-commercial licence: install it from the source.)* |
| [academic-pipeline ↗](https://github.com/Imbad0202/academic-research-skills/tree/main/academic-pipeline) | Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review -> re-revise -> final integrity check ->… *(Non-commercial licence: install it from the source.)* |
| [deep-research ↗](https://github.com/Imbad0202/academic-research-skills/tree/main/deep-research) | Universal deep research agent team. 13-agent pipeline for rigorous academic research on any topic. 8 modes: full research, quick brief, paper review, lit-review… *(Non-commercial licence: install it from the source.)* |
| [sr-screener ↗](https://github.com/Imbad0202/academic-research-skills/tree/main/sr-screener) | Protocol-driven study screening for systematic, scoping and rapid reviews. Turns a proposal or PROSPERO protocol into confirmed eligibility rules, then screens… *(Non-commercial licence: install it from the source.)* |

## last30days-skill

[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · MIT · ★ 65.9k · 1 linked

AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

| Skill | What it does |
|---|---|
| [last30days ↗](https://github.com/mvanhorn/last30days-skill/tree/main/skills/last30days) | Research what people actually say about any topic in the last 30 days. Pulls posts and engagement from Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, and… *(Too big to copy here (18 MB): install it from the source.)* |

## notebooklm-py

[teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) · MIT · ★ 20k · 1 linked

Unofficial Python API and agentic skill for Google Gemini Notebook. Full programmatic access to Gemini Notebook's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.

| Skill | What it does |
|---|---|
| [notebooklm ↗](https://github.com/teng-lin/notebooklm-py) | Install, authenticate, troubleshoot, and operate Gemini Notebook through the notebooklm-py CLI or typed async Python API. Use for notebook and source management… *(Too big to copy here (124 MB): install it from the source.)* |
