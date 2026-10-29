# Developer workflow

Planning, testing, debugging, code review, memory and shipping.

289 skills here and 1 linked to their source, from 16 projects. [All categories](../CATALOG.md)

**To install a skill**, open it, copy the address from your browser and run `npx skills add <that address> -g -a claude-code`. More ways in [How to install](../README.md#install-a-skill). Skills marked ↗ live in their own repos: install them from there.

## gstack

[garrytan/gstack](https://github.com/garrytan/gstack) · MIT · ★ 138.2k · 61 here, 1 linked

Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

62 skills: see [the full list](dev-workflow--gstack.md).

## ZCode

[zai-org/ZCode](https://github.com/zai-org/ZCode) · Apache-2.0 · ★ 8.4k · 51 here

Z.ai's coding agent harness. Powerful, intelligent, extensible.

| Skill | What it does |
|---|---|
| [agent-browser](../skills/dev-workflow/ZCode/agent-browser/) | Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots… |
| [ai-elements](../skills/dev-workflow/ZCode/ai-elements/) | Build AI chat interfaces using ai-elements components — conversations, messages, tool displays, prompt inputs, and more. Use when the user wants to build a chatbot, AI… |
| [android-dev](../skills/dev-workflow/ZCode/android-dev/) | Build, run, inspect, and lightly automate Android apps with the android-emulator MCP tools. |
| [architecture-governance](../skills/dev-workflow/ZCode/architecture-governance/) | Check ZCode module and layer boundaries for code changes. Generate bounded context for cross-module or ownership changes; skip documentation-only work. |
| [brainstorming](../skills/dev-workflow/ZCode/brainstorming/) | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and… |
| [computer-use](../skills/dev-workflow/ZCode/computer-use/) | Use when a task needs a native desktop app's own UI or the OS. For anything inside a web page, use Browser Use. Main agent only. |
| [control-browser](../skills/dev-workflow/ZCode/control-browser/) | Use when opening, navigating, inspecting, testing, clicking, typing, filling, screenshotting, or verifying web pages and local HTTP targets (localhost, 127.0.0.1, ::1)… |
| [dep-refs](../skills/dev-workflow/ZCode/dep-refs/) | Use when the agent needs to inspect TypeScript export references in the z-code workspace, list exports from a file, verify whether an export is unused before deletion… |
| [diagnosing-commands](../skills/dev-workflow/ZCode/diagnosing-commands/) | Use to diagnose and fix ZCode custom slash-command (/command) configuration problems in the ZCode client. Applies when a command is missing, is overridden by a… |
| [diagnosing-hooks](../skills/dev-workflow/ZCode/diagnosing-hooks/) | Use to diagnose and fix ZCode hook configuration problems in the ZCode client. Applies when a hook does not trigger, an event name is wrong, a matcher does not match a… |
| [diagnosing-mcp](../skills/dev-workflow/ZCode/diagnosing-mcp/) | Use to diagnose and fix ZCode MCP (Model Context Protocol) server configuration problems in the ZCode client. Applies when an MCP server will not connect, its tools… |
| [diagnosing-plugins](../skills/dev-workflow/ZCode/diagnosing-plugins/) | Use to diagnose and fix ZCode plugin and marketplace problems in the ZCode client. Applies when a plugin is not listed, adding a marketplace or installing a plugin… |
| [diagnosing-skills](../skills/dev-workflow/ZCode/diagnosing-skills/) | Use to diagnose and fix ZCode skill configuration problems in the ZCode client. Applies when a skill is not discovered, is installed but does not trigger automatically… |
| [dispatching-parallel-agents](../skills/dev-workflow/ZCode/dispatching-parallel-agents/) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| [docx](../skills/dev-workflow/ZCode/docx/) | Complete DOCX document creation, editing, and analysis capabilities with support for revisions, comments, formatting preservation, and text extraction. Also handles Word… |
| [docx-viewer](../skills/dev-workflow/ZCode/docx-viewer/) | View and discuss Word (.docx) files with the user in the Documents side panel. Use when the user wants to open, read, review or ask about a Word document in the… |
| [dogfood](../skills/dev-workflow/ZCode/dogfood/) | Systematically explore and test a web application to find bugs, UX issues, and other problems. Use when asked to "dogfood", "QA", "exploratory test", "find issues", "bug… |
| [dynamic-workflows](../skills/dev-workflow/ZCode/dynamic-workflows/) | Use when writing, debugging, or resubmitting a dynamic-workflow script for the CreateWorkflow tool: choosing subagent topology, typing subagent results, fanning out over… |
| [e2e-case-lifecycle](../skills/dev-workflow/ZCode/e2e-case-lifecycle/) | Plan, maintain, replay, and promote ZCode desktop E2E cases and their fixtures, coverage matrices, and CI admission evidence. |
| [electron](../skills/dev-workflow/ZCode/electron/) | Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via Chrome DevTools Protocol. Use when the user needs to… |
| [executing-plans](../skills/dev-workflow/ZCode/executing-plans/) | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| [feature-boundary-planner](../skills/dev-workflow/ZCode/feature-boundary-planner/) | Use when the agent needs to discover the blast radius of a ZCode feature or behavior change, answer "if I change X what other features or UI surfaces should I inspect?"… |
| [finishing-a-development-branch](../skills/dev-workflow/ZCode/finishing-a-development-branch/) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured… |
| [ios-dev](../skills/dev-workflow/ZCode/ios-dev/) | Build, run, inspect, and lightly automate iOS simulator apps with the ios-simulator MCP tools. |
| [opentui](../skills/dev-workflow/ZCode/opentui/) | Build terminal UIs with OpenTUI. Covers the core API, native audio, keymaps, React and Solid bindings, components, layout, keyboard input, plugins, and testing. |
| [pdf](../skills/dev-workflow/ZCode/pdf/) | Professional PDF toolkit covering four production workflows: reports, creative visuals, academic LaTeX, and existing PDF processing. Routes automatically by document… |
| [pdf-viewer](../skills/dev-workflow/ZCode/pdf-viewer/) | View and discuss PDF files with the user in the PDF side panel. Use when the user wants to open, read, review or ask about a PDF in the workspace, refers to something… |
| [plugin-creator](../skills/dev-workflow/ZCode/plugin-creator/) | Create or update ZCode plugin source and a local test marketplace, then guide the user to add, install, update and try it in the app. Use for new plugins or changes to… |
| [pptx](../skills/dev-workflow/ZCode/pptx/) | Use this skill any time a presentation file is the primary input or output. Covers: creating new .pptx decks from scratch or from an outline/document (pptxgenjs /… |
| [pptx-viewer](../skills/dev-workflow/ZCode/pptx-viewer/) | View and discuss PowerPoint (.pptx) decks with the user in the Presentations side panel. Use when the user wants to open, review or ask about a deck in the workspace… |
| [receiving-code-review](../skills/dev-workflow/ZCode/receiving-code-review/) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and… |
| [requesting-code-review](../skills/dev-workflow/ZCode/requesting-code-review/) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| [restore-legacy-sessions](../skills/dev-workflow/ZCode/restore-legacy-sessions/) | Use when ZCode needs to inspect, plan, or execute restoration of old ACP-era ZCode sessions from ~/.zcode/v2/sessions into the new ZCode task/session stores. Trigger… |
| [session-management](../skills/dev-workflow/ZCode/session-management/) | 修改 ZCode 会话管理（左侧任务列表、tasks-index.sqlite、sessions-index、CLI session store、标题/状态/置顶/归档/未读/删除、虚拟项目与 roots、workspace 身份、相关 migration）之前必读。它把 2026-09… |
| [skill-creator](../skills/dev-workflow/ZCode/skill-creator/) | Create new skills, edit existing skills, and iterate wording. Use when writing SKILL.md from scratch, improving existing skills, turning repeated workflows into reusable… |
| [subagent-driven-development](../skills/dev-workflow/ZCode/subagent-driven-development/) | Use when executing implementation plans with independent tasks in the current session |
| [systematic-debugging](../skills/dev-workflow/ZCode/systematic-debugging/) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| [test-driven-development](../skills/dev-workflow/ZCode/test-driven-development/) | Use when implementing any feature or bugfix, before writing implementation code |
| [using-git-worktrees](../skills/dev-workflow/ZCode/using-git-worktrees/) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native… |
| [using-superpowers](../skills/dev-workflow/ZCode/using-superpowers/) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| [vercel-react-best-practices](../skills/dev-workflow/ZCode/vercel-react-best-practices/) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to… |
| [vercel-react-view-transitions](../skills/dev-workflow/ZCode/vercel-react-view-transitions/) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`&lt;ViewTransition>` component, `addTransitionType`, and CSS view transition… |
| [verification-before-completion](../skills/dev-workflow/ZCode/verification-before-completion/) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before… |
| [visualize](../skills/dev-workflow/ZCode/visualize/) | Create visualizations and interactive tools directly in conversation. Proactively use to show how something works; explore 'what happens when', 'what changes', or 'help… |
| [web-gui-tester](../skills/dev-workflow/ZCode/web-gui-tester/) | Use the browser automation tooling available in the session to test web frontends interactively in a purely GUI-based, black-box manner: simulate real user clicks, text… |
| [writing-plans](../skills/dev-workflow/ZCode/writing-plans/) | Use when you have a spec or requirements for a multi-step task, before touching code |
| [writing-skills](../skills/dev-workflow/ZCode/writing-skills/) | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
| [xlsx](../skills/dev-workflow/ZCode/xlsx/) | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx… |
| [xlsx-viewer](../skills/dev-workflow/ZCode/xlsx-viewer/) | View and discuss Excel (.xlsx) workbooks with the user in the Spreadsheets side panel. Use when the user wants to open, look through or ask about a workbook in the… |
| [zcode-configuration-guide](../skills/dev-workflow/ZCode/zcode-configuration-guide/) | Use when configuring ZCode's extension resources (MCP servers, slash commands, skills, hooks, and plugins) or instruction files such as AGENTS.md in the ZCode client… |
| [zcode-large-task-fixture](../skills/dev-workflow/ZCode/zcode-large-task-fixture/) | Generate, verify, or remove large synthetic ZCode task fixtures in local ~/.zcode persistence for UI/session performance testing. Use when testing big conversation/task… |

## obsidian-wiki

[Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) · MIT · ★ 3.6k · 39 here

Framework for AI agents to build and maintain a digital brain through Obsidian wiki \| Memory System for Agents

| Skill | What it does |
|---|---|
| [claude-history-ingest](../skills/dev-workflow/obsidian-wiki/claude-history-ingest/) | Ingest Claude Code conversation/session history into Obsidian as distilled knowledge. Use for importing or mining past Claude sessions, .claude data, project/session… |
| [code-understand](../skills/dev-workflow/obsidian-wiki/code-understand/) | Map the load-bearing files, symbols, callers, and dependencies of an unfamiliar codebase before making changes. Use for architecture orientation, impact analysis… |
| [codex-history-ingest](../skills/dev-workflow/obsidian-wiki/codex-history-ingest/) | Ingest Codex CLI conversation/session history into Obsidian as distilled knowledge. Use for importing or mining ~/.codex sessions, rollout files, indexes, or transcript… |
| [copilot-history-ingest](../skills/dev-workflow/obsidian-wiki/copilot-history-ingest/) | Ingest GitHub Copilot CLI/session history into Obsidian as distilled knowledge. Use for importing or mining Copilot history; not for general Copilot help, simple session… |
| [cross-linker](../skills/dev-workflow/obsidian-wiki/cross-linker/) | Find and add missing cross-references between wiki pages. Use when pages are disconnected or after large ingestion. This modifies pages to add links; use wiki-lint for… |
| [daily-update](../skills/dev-workflow/obsidian-wiki/daily-update/) | Run or configure the daily wiki maintenance cycle: check source freshness, refresh the index and hot.md, and manage its scheduled 9 AM launchd/systemd/cron reminder. Use… |
| [graph-colorize](../skills/dev-workflow/obsidian-wiki/graph-colorize/) | Configure Obsidian graph colors by tag, folder, category, or visibility by updating .obsidian/graph.json. Use for graph colorization; preserve other graph settings and… |
| [hermes-history-ingest](../skills/dev-workflow/obsidian-wiki/hermes-history-ingest/) | Ingest Hermes agent history into Obsidian as distilled knowledge. Use for importing or mining ~/.hermes sessions, memories, or logs; use wiki-agent for targeted… |
| [impl-validator](../skills/dev-workflow/obsidian-wiki/impl-validator/) | Independently check whether an implementation matches its stated goal and return PASS/WARN/FAIL with actionable issues. Use for second-opinion validation of an… |
| [llm-wiki](../skills/dev-workflow/obsidian-wiki/llm-wiki/) | Explain and apply the foundational LLM Wiki architecture and knowledge-management strategy. Use for setup, architecture, schema, or organization decisions; operational… |
| [memory-bridge](../skills/dev-workflow/obsidian-wiki/memory-bridge/) | Browse or compare wiki knowledge by originating AI tool. Use for cross-tool memory questions, tool-specific knowledge, or gap/diff analysis between Codex, Claude… |
| [obsidian-layout-adjustment](../skills/dev-workflow/obsidian-wiki/obsidian-layout-adjustment/) | Adjust the user's Obsidian visual layout with CSS snippets. Use for restyling tabs, sidebars, note surfaces, properties, backlinks, graph or file-explorer UI, or… |
| [openclaw-history-ingest](../skills/dev-workflow/obsidian-wiki/openclaw-history-ingest/) | Ingest OpenClaw session/history data into Obsidian as distilled knowledge. Use for importing or mining ~/.openclaw sessions, memory files, or logs; use wiki-agent for… |
| [pi-history-ingest](../skills/dev-workflow/obsidian-wiki/pi-history-ingest/) | Ingest Pi coding-agent session history into Obsidian as distilled knowledge. Use for importing or mining ~/.pi/agent/sessions or Pi conversation logs; use wiki-agent for… |
| [session-brain](../skills/dev-workflow/obsidian-wiki/session-brain/) | Build or refresh a browser-viewable topic graph over Claude session history using local clustering. Use for mapping or clustering sessions, recent or stale topic… |
| [session-search](../skills/dev-workflow/obsidian-wiki/session-search/) | Search the session-brain graph for a past agent session by topic and load the winning transcript into the current conversation. Use for finding which session handled X… |
| [tag-taxonomy](../skills/dev-workflow/obsidian-wiki/tag-taxonomy/) | Apply and maintain the wiki's controlled tag vocabulary. Use for choosing, normalizing, auditing, or extending tags when creating or updating wiki pages; consult the… |
| [vault-skill-factory](../skills/dev-workflow/obsidian-wiki/vault-skill-factory/) | Create a reviewable Agent Skill package from mature curated wiki pages. Use when turning verified vault knowledge into a reusable skill. Reads the vault and writes only… |
| [wiki-agent](../skills/dev-workflow/obsidian-wiki/wiki-agent/) | Search one AI agent's raw history for a specific topic, ingest only matching sessions, and return a synthesized answer. Use for targeted cross-agent recall; use… |
| [wiki-capture](../skills/dev-workflow/obsidian-wiki/wiki-capture/) | Turn the current conversation or finding into a structured permanent wiki note. Use for save/capture/preserve requests; QUICK MODE writes a fast _raw/ note. Supports… |
| [wiki-context-pack](../skills/dev-workflow/obsidian-wiki/wiki-context-pack/) | Produce a token-bounded, citation-ready context slice from an existing Obsidian vault for a downstream agent or task. Use for "/wiki-context-pack", "use my vault as… |
| [wiki-dashboard](../skills/dev-workflow/obsidian-wiki/wiki-dashboard/) | Create dynamic, queryable Obsidian dashboard views using Bases or Dataview. Use for auto-updating tables, indexes, or structured views of vault content; not for ordinary… |
| [wiki-dedup](../skills/dev-workflow/obsidian-wiki/wiki-dedup/) | Detect and merge wiki pages representing the same concept under different names. Use for page-identity deduplication and consolidation. Destructive merges require… |
| [wiki-digest](../skills/dev-workflow/obsidian-wiki/wiki-digest/) | Produce a day/week/month knowledge digest summarizing what was learned, updated, and connected in the wiki. Use for readable recent-learning summaries; wiki-status… |
| [wiki-export](../skills/dev-workflow/obsidian-wiki/wiki-export/) | Export the Obsidian wiki graph to JSON, GraphML, Neo4j Cypher, Postgres/SQL, HTML, or OKF bundles. Use when transferring or visualizing wiki data in external tools… |
| [wiki-history-ingest](../skills/dev-workflow/obsidian-wiki/wiki-history-ingest/) | Route generic agent-history ingestion requests to the appropriate specialized history-ingest skill. Use when the user asks to ingest AI-agent history without directly… |
| [wiki-import](../skills/dev-workflow/obsidian-wiki/wiki-import/) | Import a wiki graph into the current vault from graph.json or an OKF/markdown bundle. Use for transferring previously exported wiki content between vaults; pair with… |
| [wiki-ingest](../skills/dev-workflow/obsidian-wiki/wiki-ingest/) | Ingest new documents, raw text, folders, or URLs into the Obsidian wiki as distilled, linked knowledge. Use for general wiki ingestion when no more specific ingest skill… |
| [wiki-lint](../skills/dev-workflow/obsidian-wiki/wiki-lint/) | Audit wiki health: broken links, orphans, contradictions, stale content, lifecycle and tag issues. Use for maintenance or health checks. Default is report-only; use… |
| [wiki-narrate](../skills/dev-workflow/obsidian-wiki/wiki-narrate/) | Turn a wiki topic into a cited Markdown briefing, plain-language explanation, or progressive lecture. Use this skill for topic-based briefing, explanation, and lecture… |
| [wiki-query](../skills/dev-workflow/obsidian-wiki/wiki-query/) | Search and synthesize answers from the compiled Obsidian wiki, including cited and multi-hop answers. Use for questions about existing wiki knowledge or fast index-only… |
| [wiki-rebuild](../skills/dev-workflow/obsidian-wiki/wiki-rebuild/) | Archive and rebuild wiki knowledge from source, or restore a prior archive. Use for full restart/recovery when incremental repair is inappropriate; this is broader and… |
| [wiki-research](../skills/dev-workflow/obsidian-wiki/wiki-research/) | Perform multi-round web research on a topic, synthesize the findings, and file structured results into the Obsidian wiki. Use for comprehensive web-sourced research… |
| [wiki-setup](../skills/dev-workflow/obsidian-wiki/wiki-setup/) | Initialize or repair an Obsidian wiki vault's required structure and configuration. Use for new-vault setup, .env/config creation, reconfiguration, or broken setup… |
| [wiki-stage-commit](../skills/dev-workflow/obsidian-wiki/wiki-stage-commit/) | Review staged wiki writes and promote accepted pages to final locations when WIKI_STAGED_WRITES is enabled. Use for staging approval/commit; rejected pages return to… |
| [wiki-status](../skills/dev-workflow/obsidian-wiki/wiki-status/) | Report wiki ingestion/completeness state, pending source delta, structural insights, or maintenance equilibrium. Use for remaining-work/status questions, hubs and… |
| [wiki-switch](../skills/dev-workflow/obsidian-wiki/wiki-switch/) | List, create, or switch named Obsidian wiki vault profiles under the global config directory. Use when changing the active vault, checking which vault is active, or… |
| [wiki-synthesize](../skills/dev-workflow/obsidian-wiki/wiki-synthesize/) | Find recurring concept combinations across the wiki that lack an explicit synthesis page, then create cross-cutting synthesis pages. Use for knowledge synthesis after… |
| [wiki-update](../skills/dev-workflow/obsidian-wiki/wiki-update/) | Sync knowledge from the current project into the Obsidian wiki. Use when work already in the current project should be distilled into the vault; named-vault routing… |

## mattpocock-skills

[mattpocock/skills](https://github.com/mattpocock/skills) · MIT · ★ 306.5k · 38 here

Skills for Real Engineers. Straight from my .agents directory.

| Skill | What it does |
|---|---|
| [ask-matt](../skills/dev-workflow/mattpocock-skills/ask-matt/) | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| [chief-of-staff](../skills/dev-workflow/mattpocock-skills/chief-of-staff/) | Pursue a long-running goal in a single session by co-ordinating subagents. |
| [claude-handoff](../skills/dev-workflow/mattpocock-skills/claude-handoff/) | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| [code-review](../skills/dev-workflow/mattpocock-skills/code-review/) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and… |
| [codebase-design](../skills/dev-workflow/mattpocock-skills/codebase-design/) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes… |
| [diagnosing-bugs](../skills/dev-workflow/mattpocock-skills/diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| [domain-modeling](../skills/dev-workflow/mattpocock-skills/domain-modeling/) | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. |
| [git-guardrails-claude-code](../skills/dev-workflow/mattpocock-skills/git-guardrails-claude-code/) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git… |
| [grill-me](../skills/dev-workflow/mattpocock-skills/grill-me/) | A relentless interview to sharpen a plan or design. |
| [grill-with-docs](../skills/dev-workflow/mattpocock-skills/grill-with-docs/) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| [grilling](../skills/dev-workflow/mattpocock-skills/grilling/) | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| [handoff](../skills/dev-workflow/mattpocock-skills/handoff/) | Compact the current conversation into a handoff document for another agent to pick up. |
| [implement](../skills/dev-workflow/mattpocock-skills/implement/) | Implement a piece of work based on a spec or set of tickets. |
| [implement-spec](../skills/dev-workflow/mattpocock-skills/implement-spec/) | Implement the result of /to-spec and /to-tickets in code. |
| [improve-codebase-architecture](../skills/dev-workflow/mattpocock-skills/improve-codebase-architecture/) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [loop-me](../skills/dev-workflow/mattpocock-skills/loop-me/) | Grill me about specs for the workflows I want to build, within this workspace. |
| [migrate-to-shoehorn](../skills/dev-workflow/mattpocock-skills/migrate-to-shoehorn/) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. |
| [pr](../skills/dev-workflow/mattpocock-skills/pr/) | Use when writing a PR body. |
| [prototype](../skills/dev-workflow/mattpocock-skills/prototype/) | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should… |
| [research](../skills/dev-workflow/mattpocock-skills/research/) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or… |
| [retro](../skills/dev-workflow/mattpocock-skills/retro/) | Conduct a retrospective on a coding session. |
| [scaffold-exercises](../skills/dev-workflow/mattpocock-skills/scaffold-exercises/) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise… |
| [setup-matt-pocock-skills](../skills/dev-workflow/mattpocock-skills/setup-matt-pocock-skills/) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other… |
| [setup-pre-commit](../skills/dev-workflow/mattpocock-skills/setup-pre-commit/) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky… |
| [setup-ts-deep-modules](../skills/dev-workflow/mattpocock-skills/setup-ts-deep-modules/) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point… |
| [tdd](../skills/dev-workflow/mattpocock-skills/tdd/) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| [teach](../skills/dev-workflow/mattpocock-skills/teach/) | Teach the user a new skill or concept, within this workspace. |
| [to-questionnaire](../skills/dev-workflow/mattpocock-skills/to-questionnaire/) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| [to-spec](../skills/dev-workflow/mattpocock-skills/to-spec/) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| [to-tickets](../skills/dev-workflow/mattpocock-skills/to-tickets/) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as… |
| [triage](../skills/dev-workflow/mattpocock-skills/triage/) | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| [wait-what](../skills/dev-workflow/mattpocock-skills/wait-what/) | Stop. That last message did not land: re-pitch it. |
| [wayfinder](../skills/dev-workflow/mattpocock-skills/wayfinder/) | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way… |
| [wizard](../skills/dev-workflow/mattpocock-skills/wizard/) | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets… |
| [writing-beats](../skills/dev-workflow/mattpocock-skills/writing-beats/) | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| [writing-for-agents](../skills/dev-workflow/mattpocock-skills/writing-for-agents/) | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| [writing-fragments](../skills/dev-workflow/mattpocock-skills/writing-fragments/) | Writing, explore: mine raw fragments, no structure yet. |
| [writing-shape](../skills/dev-workflow/mattpocock-skills/writing-shape/) | Writing, exploit: shape raw material into an article, paragraph by paragraph. |

## claude-mem

[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) · Apache-2.0 · ★ 104.6k · 32 here

Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

| Skill | What it does |
|---|---|
| [Agent Cost Report](../skills/dev-workflow/claude-mem/agent-cost-report/) | Believable agent cost report for any period, default the last 7 full days PT, not counting today. Measured tokens from Claude Code transcripts priced at OpenRouter list… |
| [babysit](../skills/dev-workflow/claude-mem/babysit/) | Watch a pull request or review cycle until it is ready to merge. Use when asked to babysit, monitor, or keep checking PR comments, reviews, and CI until all actionable… |
| [build-and-release](../skills/dev-workflow/claude-mem/build-and-release/) | Fully automate building and releasing a coding task. |
| [ccs-align](../skills/dev-workflow/claude-mem/ccs-align/) | Run the CCS Align seat's hourly breathing cycle — prove the local claude-mem worker is healthy, pull needle observations through search → timeline → get_observations… |
| [childhood](../skills/dev-workflow/claude-mem/childhood/) | Babysit a shipped release after merge, publication, or deployment. Verify published packages, production behavior, installed plugins, and late CI or user reports until… |
| [claude-mem-install](../skills/dev-workflow/claude-mem/claude-mem-install/) | Use this when setting up claude-mem on Cursor: local or remote worker, local host-login observer or remote cmem.ai inference. |
| [cloud-sync](../skills/dev-workflow/claude-mem/cloud-sync/) | Set up or check claude-mem cloud sync with cmem.ai Pro. Use when the user says "set up cloud sync", "sync my memories", "cmem pro", "cloud backup", "sync status", or… |
| [design-is](../skills/dev-workflow/claude-mem/design-is/) | Audit a design against Dieter Rams' ten "Good design is..." principles, then hand off a /make-plan prompt for one of three outcomes — new design, refine design, or… |
| [do](../skills/dev-workflow/claude-mem/openclaw/skills/do/) | — |
| [handoff](../skills/dev-workflow/claude-mem/handoff/) | Generate a HANDOFF.md that captures goal, current state, files touched, failed attempts, and next steps — so a fresh Claude session can continue exactly where this one… |
| [host-observer](../skills/dev-workflow/claude-mem/host-observer/) | Use this when fulfilling claude-mem observer jobs on Grok Bot: reply only skip_summary or one full observation XML, never prose. |
| [how-it-works](../skills/dev-workflow/claude-mem/how-it-works/) | Explain how claude-mem captures observations, when memory injection kicks in, and where data lives. Use when the user asks "how does claude-mem work?" or "what is this… |
| [knowledge-agent](../skills/dev-workflow/claude-mem/knowledge-agent/) | Build and query AI-powered knowledge bases from claude-mem observations. Use when users want to create focused "brains" from their observation history, ask questions… |
| [learn-codebase](../skills/dev-workflow/claude-mem/learn-codebase/) | Prime a codebase by reading every source file in full. Use when starting work on a new or unfamiliar project, or when the user asks to "learn the codebase", "read the… |
| [make-plan](../skills/dev-workflow/claude-mem/openclaw/skills/make-plan/) | — |
| [mem-search](../skills/dev-workflow/claude-mem/mem-search/) | Use this when the user asks to search memory, "did we already solve this?", "how did we do X last time?", or wants work from previous sessions. |
| [mem-setup](../skills/dev-workflow/claude-mem/mem-setup/) | This skill should be used when the user asks to "set up claude-mem", "pair claude-mem", "connect cmem", "add my cmem key", "set up cloud sync in Cowork", or provides… |
| [mode-creator](../skills/dev-workflow/claude-mem/mode-creator/) | Interactively create, install, activate, and verify custom claude-mem modes, including domain-specific observation types, concept tags, optional Telegram alerts, bot… |
| [oh-my-issues](../skills/dev-workflow/claude-mem/oh-my-issues/) | Cluster a GitHub issue backlog by root cause into a small set of plan-master issues, redirect children with a standardized comment, and bundle architectural-fix PRs that… |
| [openclaw](../skills/dev-workflow/claude-mem/openclaw/) | — |
| [owner-goals](../skills/dev-workflow/claude-mem/owner-goals/) | Map what the owner wants from the prompts they typed themselves (prompts an agent wrote are left out), then put their top priorities and open asks, each with dated… |
| [pathfinder](../skills/dev-workflow/claude-mem/pathfinder/) | Map a codebase into feature-grouped flowcharts, identify duplicated concerns across features, and propose a unified architecture. Use when asked to "find the ideal… |
| [release](../skills/dev-workflow/claude-mem/release/) | Fully automate a release with version-bump and childhood. |
| [request-progress](../skills/dev-workflow/claude-mem/request-progress/) | Group recent conversations into overall requests, review each one's progress from memory, link each to the owner goals it serves, and write the build story, so My Work… |
| [screenpipe](../skills/dev-workflow/claude-mem/screenpipe/) | Search screen and audio history recorded by Screenpipe and optionally save selected context into claude-mem. Use when the user asks to recall desktop activity, a… |
| [smart-explore](../skills/dev-workflow/claude-mem/smart-explore/) | Token-optimized structural code search using tree-sitter AST parsing. Use instead of reading full files when you need to understand code structure, find functions, or… |
| [standup](../skills/dev-workflow/claude-mem/standup/) | Facilitate a read-only standup across git worktrees, branches, or PRs to compare changes and produce one consolidation plan. |
| [timeline-report](../skills/dev-workflow/claude-mem/timeline-report/) | Generate a "Journey Into [Project]" narrative report analyzing a project's entire development history from claude-mem's timeline. Use when asked for a timeline report… |
| [version-bump](../skills/dev-workflow/claude-mem/version-bump/) | Automated semantic versioning and release workflow for Claude Code plugins. Handles version increments across package.json, marketplace.json, plugin.json manifests… |
| [weekly-digests](../skills/dev-workflow/claude-mem/weekly-digests/) | Generate a serial week-by-week narrative digest of a project's full claude-mem timeline. Splits the timeline into per-ISO-week files, then runs one consecutive subagent… |
| [what-the](../skills/dev-workflow/claude-mem/what-the/) | What the? Use when the user wants a plain-English breakdown of something technical — the who, what, where, why, and when. |
| [wowerpoint](../skills/dev-workflow/claude-mem/wowerpoint/) | Turn one document into a kawaii NotebookLM slide deck. Use for "wowerpoint this", "make a deck about &lt;file>", "turn this report into slides", or any request to render… |

## caveman

[JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) · Apache-2.0+MIT · ★ 116.1k · 22 here

🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.

| Skill | What it does |
|---|---|
| [cavecrew](../skills/dev-workflow/caveman/cavecrew/) | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or using… |
| [caveman](../skills/dev-workflow/caveman/caveman/) | Terse caveman voice: answer first, fluff gone, every technical fact kept. Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less tokens". Stays on… |
| [caveman-commit](../skills/dev-workflow/caveman/caveman-commit/) | Write a Conventional Commits message compressed to intent only. Use for "write a commit", "commit message", /commit or /caveman-commit. |
| [caveman-compress](../skills/dev-workflow/caveman/caveman-compress/) | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. Sends the file's text to the configured… |
| [caveman-discover](../skills/dev-workflow/caveman/caveman-discover/) | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket. Use for "discover workflows" or breaking LLM spend… |
| [caveman-evidence-review](../skills/dev-workflow/caveman/caveman-evidence-review/) | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings. Use when asked what Caveman found or where LLM spend… |
| [caveman-explore](../skills/dev-workflow/caveman/caveman-explore/) | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. Skip it when the exact file or symbol is already… |
| [caveman-help](../skills/dev-workflow/caveman/caveman-help/) | Quick-reference card for the three caveman skills and their commands. Trigger: /caveman-help or "caveman help". |
| [caveman-learn](../skills/dev-workflow/caveman/caveman-learn/) | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. Use when asked to… |
| [caveman-manage](../skills/dev-workflow/caveman/caveman-manage/) | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. Use when asked to start, approve, cancel, promote or roll back a Caveman experiment. |
| [caveman-optimize](../skills/dev-workflow/caveman/caveman-optimize/) | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation. Use when asked to inspect or evaluate a Caveman optimization… |
| [caveman-review](../skills/dev-workflow/caveman/caveman-review/) | Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review, "review this PR", or "review the diff". |
| [caveman-setup](../skills/dev-workflow/caveman/caveman-setup/) | Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior change. Use for "set up caveman" or adding LLM spend observability. |
| [caveman-stats](../skills/dev-workflow/caveman/caveman-stats/) | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's native usage report. Trigger… |
| [investigate-first](../skills/dev-workflow/caveman/investigate-first/) | Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hypotheses. |
| [lean-build](../skills/dev-workflow/caveman/lean-build/) | Build feature work with high overbuilding risk. Use for new behavior, product slices, or integrations where repository reuse, strict scope, and an explicit stop… |
| [megacave](../skills/dev-workflow/caveman/megacave/) | Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. Invoke only with /megacave or /caveman wenyan. Stays on until "stop caveman"… |
| [migration](../skills/dev-workflow/caveman/migration/) | Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preservation… |
| [safe-refactor](../skills/dev-workflow/caveman/safe-refactor/) | Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits. |
| [surgical-patch](../skills/dev-workflow/caveman/surgical-patch/) | Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved surrounding behavior, and task-relevant tests matter. |
| [ultracave](../skills/dev-workflow/caveman/ultracave/) | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. Invoke only with /ultracave or /caveman ultra. Stays on until "stop caveman"… |
| [verify-and-stop](../skills/dev-workflow/caveman/verify-and-stop/) | Prove existing work meets acceptance conditions without expanding scope. Use for validation-only tasks, completion checks, focused gate runs, and last-mile proof. |

## superpowers

[obra/superpowers](https://github.com/obra/superpowers) · MIT · ★ 308.4k · 15 here

An agentic skills framework & software development methodology that works.

| Skill | What it does |
|---|---|
| [brainstorming](../skills/dev-workflow/superpowers/brainstorming/) | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or… |
| [diagnosing-superpowers](../skills/dev-workflow/superpowers/diagnosing-superpowers/) | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it… |
| [dispatching-parallel-agents](../skills/dev-workflow/superpowers/dispatching-parallel-agents/) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| [executing-plans](../skills/dev-workflow/superpowers/executing-plans/) | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| [finishing-a-development-branch](../skills/dev-workflow/superpowers/finishing-a-development-branch/) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| [receiving-code-review](../skills/dev-workflow/superpowers/receiving-code-review/) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and… |
| [requesting-code-review](../skills/dev-workflow/superpowers/requesting-code-review/) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| [subagent-driven-development](../skills/dev-workflow/superpowers/subagent-driven-development/) | Use when executing implementation plans with independent tasks in the current session |
| [systematic-debugging](../skills/dev-workflow/superpowers/systematic-debugging/) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| [test-driven-development](../skills/dev-workflow/superpowers/test-driven-development/) | Use when implementing any feature or bugfix, before writing implementation code |
| [using-git-worktrees](../skills/dev-workflow/superpowers/using-git-worktrees/) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native… |
| [using-superpowers](../skills/dev-workflow/superpowers/using-superpowers/) | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| [verification-before-completion](../skills/dev-workflow/superpowers/verification-before-completion/) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before… |
| [writing-plans](../skills/dev-workflow/superpowers/writing-plans/) | Use when you have a spec or requirements for a multi-step task, before touching code |
| [writing-skills](../skills/dev-workflow/superpowers/writing-skills/) | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

## ponytail

[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) · MIT · ★ 180k · 6 here

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

| Skill | What it does |
|---|---|
| [ponytail](../skills/dev-workflow/ponytail/ponytail/) | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixing… |
| [ponytail-audit](../skills/dev-workflow/ponytail/ponytail-audit/) | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. Ranked, each… |
| [ponytail-debt](../skills/dev-workflow/ponytail/ponytail-debt/) | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for "ponytail debt", "what did ponytail defer", "list… |
| [ponytail-gain](../skills/dev-workflow/ponytail/ponytail-gain/) | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, "what does ponytail save", "ponytail impact". |
| [ponytail-help](../skills/dev-workflow/ponytail/ponytail-help/) | Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, "ponytail help", "how do I use ponytail". |
| [ponytail-review](../skills/dev-workflow/ponytail/ponytail-review/) | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. Reads the… |

## repomix

[yamadashy/repomix](https://github.com/yamadashy/repomix) · MIT · ★ 29.1k · 6 here

📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

| Skill | What it does |
|---|---|
| [agent-carnet](../skills/dev-workflow/repomix/agent-carnet/) | Use this skill when the user asks to save, recall, find, or organize notes. Triggers on: 'remember this', 'save this', 'note this', 'what did we discuss about...'… |
| [browser-extension-developer](../skills/dev-workflow/repomix/browser-extension-developer/) | Use this skill when developing or maintaining browser extension code in the `browser/` directory, including Chrome/Firefox/Edge compatibility, content scripts… |
| [contextual-commit](../skills/dev-workflow/repomix/contextual-commit/) | Write contextual commits that capture intent, decisions, and constraints alongside code changes. Use when committing code, finishing a task, or when the user asks to… |
| [repomix](../skills/dev-workflow/repomix/repomix/) | Pack and analyze codebases into AI-friendly single files using Repomix. Use when the user wants to explore repositories, analyze code structure, find patterns, check… |
| [repomix-explorer](../skills/dev-workflow/repomix/repomix-explorer/) | Analyze or explore a codebase (remote or local repository) by packing it with the Repomix CLI, then reading and searching the generated output. Use when the user wants a… |
| [website-maintainer](../skills/dev-workflow/repomix/website-maintainer/) | Use this skill when working on the Repomix documentation website in `website/` directory, including VitePress configuration, multi-language content, or translation… |

## rea

[morluto/rea](https://github.com/morluto/rea) · MIT · ★ 407.2k · 5 here

Reverse engineer anything with agents, from app behavior down to native binaries.

| Skill | What it does |
|---|---|
| [rea-analysis-optimization](../skills/dev-workflow/rea/rea-analysis-optimization/) | Optimize REA providers and shared analysis workflows for agent context, latency, CPU, and memory while preserving correctness and Evidence. Use for analysis bottlenecks… |
| [rea-changelog-update](../skills/dev-workflow/rea/rea-changelog-update/) | Prepare or rewrite REA release changelogs and GitHub release notes from pinned Git history, with verified contributor thanks and Release Please synchronization. |
| [rea-ci-tests-audit](../skills/dev-workflow/rea/rea-ci-tests-audit/) | Audit REA CI and test suites for correctness, fixture drift, false passes, and measured performance; use for suite or workflow investigations and efficiency changes… |
| [rea-tool-design](../skills/dev-workflow/rea/rea-tool-design/) | Design or change REA investigation tools, CLI/MCP contracts, provider capabilities, and Evidence semantics. |
| [reverse-engineer-anything](../skills/dev-workflow/rea/reverse-engineer-anything/) | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA, and build agent environments (AgentEnv bundles) of web… |

## codex-plugin-cc

[openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) · Apache-2.0 · ★ 34.7k · 3 here

Use Codex from Claude Code to review code or delegate tasks.

| Skill | What it does |
|---|---|
| [codex-cli-runtime](../skills/dev-workflow/codex-plugin-cc/codex-cli-runtime/) | Internal helper contract for calling the codex-companion runtime from Claude Code |
| [codex-result-handling](../skills/dev-workflow/codex-plugin-cc/codex-result-handling/) | Internal guidance for presenting Codex helper output back to the user |
| [gpt-5-4-prompting](../skills/dev-workflow/codex-plugin-cc/gpt-5-4-prompting/) | Internal guidance for composing Codex and GPT-5.4 prompts for coding, review, diagnosis, and research tasks inside the Codex Claude Code plugin |

## open-saas

[wasp-lang/open-saas](https://github.com/wasp-lang/open-saas) · MIT · ★ 16.2k · 3 here

A 100% free modern JS SaaS boilerplate (React, NodeJS, Prisma). Full-featured: Auth (email, google, github, slack, MS), Email sending, Background jobs, Landing page, Payments (Stripe, Polar.sh), Shadcn UI, S3 file upload. AI-ready with tailored AGENTS.md, skills, and Claude Code plugin. One cmd…

| Skill | What it does |
|---|---|
| [add-wasp-skills](../skills/dev-workflow/open-saas/add-wasp-skills/) | Install Wasp agent skills (plugins) that add Wasp knowledge and best practices to your AI coding tools. |
| [getting-started](../skills/dev-workflow/open-saas/getting-started/) | Get started with your Open SaaS project — fetches docs, checks Wasp installation, and helps you start your database and app. |
| [guided-tour](../skills/dev-workflow/open-saas/guided-tour/) | Take a guided tour of Open SaaS — walks you through step-by-step through the project structure, features, and customization checklist. |

## openwiki

[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) · MIT · ★ 17.6k · 3 here

OpenWiki is a CLI that writes and maintains agent documentation for your codebase.

| Skill | What it does |
|---|---|
| [mermaid-diagrams](../skills/dev-workflow/openwiki/mermaid-diagrams/) | Embed Mermaid diagrams in generated wiki pages. Use whenever documenting a runtime or request flow, a call sequence, a state machine or lifecycle, a data model or entity… |
| [openwiki](../skills/dev-workflow/openwiki/openwiki/) | Search and read an existing repository OpenWiki when requested or needed to resolve a concrete architecture or dependency uncertainty, or initialize and update one… |
| [write-connector](../skills/dev-workflow/openwiki/write-connector/) | Add a new built-in OpenWiki source connector. Use when a user asks to create or implement an OpenWiki connector. |

## vercel-skills-cli

[vercel-labs/skills](https://github.com/vercel-labs/skills) · MIT · ★ 37.1k · 3 here

The open agent skills tool - npx skills

| Skill | What it does |
|---|---|
| [find-skills](../skills/dev-workflow/vercel-skills-cli/find-skills/) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in… |
| [pr-labeling](../skills/dev-workflow/vercel-skills-cli/pr-labeling/) | Classify a skills CLI pull request from its description and patch, while respecting existing labels. |
| [triage](../skills/dev-workflow/vercel-skills-cli/triage/) | Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention. |

## andrej-karpathy-skills

[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) · ★ 226.4k · 1 here

A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

| Skill | What it does |
|---|---|
| [karpathy-guidelines](../skills/dev-workflow/andrej-karpathy-skills/karpathy-guidelines/) | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface… |

## skillspector

[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) · Apache-2.0 · ★ 23.3k · 1 here

Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.

| Skill | What it does |
|---|---|
| [skill-inspector](../skills/dev-workflow/skillspector/skill-inspector/) | Review AI agent skills before installation using NVIDIA SkillSpector and source-aware semantic review. Use when asked whether a skill or downloaded skill folder is safe… |
