# open-seo

Skills from [every-app/open-seo](https://github.com/every-app/open-seo) at commit [`2d8236a`](https://github.com/every-app/open-seo/tree/2d8236a4fd5d799bf5c089187d0131f4dac4f38c), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Open source alternative to Semrush and Ahrefs

All credit goes to the authors of every-app/open-seo. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ai-prompt-research](ai-prompt-research/) | Find the questions people ask about a market, how ChatGPT answers them, and which sites get cited in the answers. Use when the user asks what people ask AI about their… | MIT |
| [ai-visibility-audit](ai-visibility-audit/) | Audit how a brand shows up in AI answers about its market and deliver a short report on the few changes most likely to get it mentioned or cited, such as a third-party… | MIT |
| [competitive-landscape](competitive-landscape/) | Map SEO market leaders, winning content themes, keyword coverage, backlinks, and strategic gaps. | MIT |
| [competitor-analysis](competitor-analysis/) | Analyze one competitor's organic footprint, ranking keywords, content themes, backlinks, and gaps. | MIT |
| [create-repo-skill](create-repo-skill/) | Create or update a skill in this repository the right way — canonical home in .agents/skills, internal-vs-public marking, symlink mirroring into .claude/skills, and… | MIT |
| [deslop](deslop/) | Remove AI writing patterns from prose so it reads like a person wrote it. Use when writing, editing, or reviewing user-facing text (blog posts, docs, marketing copy, PR… | MIT |
| [evaluate-skill](evaluate-skill/) | Test a candidate OpenSEO skill end to end by running fresh, isolated Codex sessions against the local backend and scoring the reports they save. Use when editing a… | MIT |
| [keyword-clustering](keyword-clustering/) | Cluster keywords by intent and map them to existing or proposed pages. | MIT |
| [keyword-research](keyword-research/) | Discover keyword opportunities, evaluate metrics and SERPs, and save/tag promising terms. | MIT |
| [link-prospecting](link-prospecting/) | Find link prospects, discover contact paths, and draft outreach from SERPs and backlink signals. | MIT |
| [local-seo](local-seo/) | Audit a Google Business Profile, compare it to local competitors, and map Maps visibility around a location. | MIT |
| [merge-ready](merge-ready/) | Get a branch ready for the maintainer's final review. Review it for security, simplicity, and billing abuse, fix what's real, get checks passing, and open or update the… | MIT |
| [observability-triage](observability-triage/) | Triage OpenSEO production errors in Cloudflare Workers Observability — verified query recipes, counting gotchas, a known-noise filter list applied automatically, and the… | MIT |
| [openseo-release-notes](openseo-release-notes/) | Cut an OpenSEO release — bump the version, draft user-facing release notes from commits since the last tag, run a review + subagent-verification pass, and open a… | MIT |
| [openseo-review-web-content](openseo-review-web-content/) | Write and review content for the OpenSEO website (web/), including blog posts, guides, feature pages, FAQs. Makes sure each page delivers real value to its target… | MIT |
| [papercuts](papercuts/) | Log genuine, recurring repository friction to .agents/PAPERCUTS.md — confusing setup, a flaky repo command or script, a misleading in-repo error, stale generated files… | MIT |
| [review-brief](review-brief/) | Produce a scannable review brief for a branch or PR so the maintainer can approve without reading the whole diff. Use when the user asks "how do I review this"… | MIT |
| [review-simplify](review-simplify/) | Review a PR for code that can be deleted or simplified. Use when asked to review for simplicity or unnecessary edge-case overengineering. | MIT |
| [review-ui-states](review-ui-states/) | Enumerate and screenshot every UI state a PR adds or changes. Use when asked to show, capture, or screenshot the UI states of a PR or branch. | MIT |
| [seo-audit](seo-audit/) | Audit a website, investigate its real search opportunities, and deliver a short data-backed report on the few changes most likely to grow organic traffic that converts. | MIT |
| [seo-coach](seo-coach/) | Enter a friendly OpenSEO coach mode that explains workflows, recommends next steps, and helps users use agents, web search, scraping, and MCP data effectively. | MIT |
| [seo-project-setup](seo-project-setup/) | Populate a project's shared OpenSEO context — site scope, goals, positioning, competitors, key pages, and preferences — plus MCP checks and Search Console intake. | MIT |
| [seo-report](seo-report/) | Write and save an OpenSEO report as one self-contained HTML page. Use when a skill has finished its research, and whenever the user asks for a report, check-in, or… | MIT |
| [setup-openseo](setup-openseo/) | Set up OpenSEO in the current AI agent. Use when a user pastes the OpenSEO installation prompt or asks to connect its plugin, MCP, and skills. | MIT |
| [simple-issue-description](simple-issue-description/) | Turn a rough bug report, feature request, support note, or pull request into a short, plain-language issue focused on the problem and desired behavior. Use when a… | MIT |
| [test-audit](test-audit/) | Invoke whenever writing, changing, reviewing, or sweeping Vitest tests in this repo. Authoring gate for new or changed tests, plus an audit workflow for low-value… | MIT |
| [verify-local-mcp](verify-local-mcp/) | Verify the OpenSEO MCP server end-to-end on a local dev server — protocol-level correctness against real DataForSEO, then a headless-agent consumer probe that tests tool… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/open-seo/ai-prompt-research -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
