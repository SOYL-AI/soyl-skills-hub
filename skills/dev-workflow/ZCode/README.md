# ZCode

Skills from [zai-org/ZCode](https://github.com/zai-org/ZCode) at commit [`3c5b227`](https://github.com/zai-org/ZCode/tree/3c5b227649371507ddc4eb46ac5133afe6db1cab), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> Z.ai's coding agent harness. Powerful, intelligent, extensible.

All credit goes to the authors of zai-org/ZCode. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [agent-browser](agent-browser/) | Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots… | Apache-2.0 |
| [ai-elements](ai-elements/) | Build AI chat interfaces using ai-elements components — conversations, messages, tool displays, prompt inputs, and more. Use when the user wants to build a chatbot, AI… | Apache-2.0 |
| [android-dev](android-dev/) | Build, run, inspect, and lightly automate Android apps with the android-emulator MCP tools. | Apache-2.0 |
| [architecture-governance](architecture-governance/) | Check ZCode module and layer boundaries for code changes. Generate bounded context for cross-module or ownership changes; skip documentation-only work. | Apache-2.0 |
| [brainstorming](brainstorming/) | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and… | MIT |
| [computer-use](computer-use/) | Use when a task needs a native desktop app's own UI or the OS. For anything inside a web page, use Browser Use. Main agent only. | Apache-2.0 |
| [control-browser](control-browser/) | Use when opening, navigating, inspecting, testing, clicking, typing, filling, screenshotting, or verifying web pages and local HTTP targets (localhost, 127.0.0.1, ::1)… | Apache-2.0 |
| [dep-refs](dep-refs/) | Use when the agent needs to inspect TypeScript export references in the z-code workspace, list exports from a file, verify whether an export is unused before deletion… | Apache-2.0 |
| [diagnosing-commands](diagnosing-commands/) | Use to diagnose and fix ZCode custom slash-command (/command) configuration problems in the ZCode client. Applies when a command is missing, is overridden by a… | Apache-2.0 |
| [diagnosing-hooks](diagnosing-hooks/) | Use to diagnose and fix ZCode hook configuration problems in the ZCode client. Applies when a hook does not trigger, an event name is wrong, a matcher does not match a… | Apache-2.0 |
| [diagnosing-mcp](diagnosing-mcp/) | Use to diagnose and fix ZCode MCP (Model Context Protocol) server configuration problems in the ZCode client. Applies when an MCP server will not connect, its tools… | Apache-2.0 |
| [diagnosing-plugins](diagnosing-plugins/) | Use to diagnose and fix ZCode plugin and marketplace problems in the ZCode client. Applies when a plugin is not listed, adding a marketplace or installing a plugin… | Apache-2.0 |
| [diagnosing-skills](diagnosing-skills/) | Use to diagnose and fix ZCode skill configuration problems in the ZCode client. Applies when a skill is not discovered, is installed but does not trigger automatically… | Apache-2.0 |
| [dispatching-parallel-agents](dispatching-parallel-agents/) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | MIT |
| [docx](docx/) | Complete DOCX document creation, editing, and analysis capabilities with support for revisions, comments, formatting preservation, and text extraction. Also handles Word… | Apache-2.0 |
| [docx-viewer](docx-viewer/) | View and discuss Word (.docx) files with the user in the Documents side panel. Use when the user wants to open, read, review or ask about a Word document in the… | Apache-2.0 |
| [dogfood](dogfood/) | Systematically explore and test a web application to find bugs, UX issues, and other problems. Use when asked to "dogfood", "QA", "exploratory test", "find issues", "bug… | Apache-2.0 |
| [dynamic-workflows](dynamic-workflows/) | Use when writing, debugging, or resubmitting a dynamic-workflow script for the CreateWorkflow tool: choosing subagent topology, typing subagent results, fanning out over… | Apache-2.0 |
| [e2e-case-lifecycle](e2e-case-lifecycle/) | Plan, maintain, replay, and promote ZCode desktop E2E cases and their fixtures, coverage matrices, and CI admission evidence. | Apache-2.0 |
| [electron](electron/) | Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via Chrome DevTools Protocol. Use when the user needs to… | Apache-2.0 |
| [executing-plans](executing-plans/) | Use when you have a written implementation plan to execute in a separate session with review checkpoints | MIT |
| [feature-boundary-planner](feature-boundary-planner/) | Use when the agent needs to discover the blast radius of a ZCode feature or behavior change, answer "if I change X what other features or UI surfaces should I inspect?"… | Apache-2.0 |
| [finishing-a-development-branch](finishing-a-development-branch/) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured… | MIT |
| [ios-dev](ios-dev/) | Build, run, inspect, and lightly automate iOS simulator apps with the ios-simulator MCP tools. | Apache-2.0 |
| [opentui](opentui/) | Build terminal UIs with OpenTUI. Covers the core API, native audio, keymaps, React and Solid bindings, components, layout, keyboard input, plugins, and testing. | Apache-2.0 |
| [pdf](pdf/) | Professional PDF toolkit covering four production workflows: reports, creative visuals, academic LaTeX, and existing PDF processing. Routes automatically by document… | Apache-2.0 |
| [pdf-viewer](pdf-viewer/) | View and discuss PDF files with the user in the PDF side panel. Use when the user wants to open, read, review or ask about a PDF in the workspace, refers to something… | Apache-2.0 |
| [plugin-creator](plugin-creator/) | Create or update ZCode plugin source and a local test marketplace, then guide the user to add, install, update and try it in the app. Use for new plugins or changes to… | Apache-2.0 |
| [pptx](pptx/) | Use this skill any time a presentation file is the primary input or output. Covers: creating new .pptx decks from scratch or from an outline/document (pptxgenjs /… | Apache-2.0 |
| [pptx-viewer](pptx-viewer/) | View and discuss PowerPoint (.pptx) decks with the user in the Presentations side panel. Use when the user wants to open, review or ask about a deck in the workspace… | Apache-2.0 |
| [receiving-code-review](receiving-code-review/) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and… | MIT |
| [requesting-code-review](requesting-code-review/) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | MIT |
| [restore-legacy-sessions](restore-legacy-sessions/) | Use when ZCode needs to inspect, plan, or execute restoration of old ACP-era ZCode sessions from ~/.zcode/v2/sessions into the new ZCode task/session stores. Trigger… | Apache-2.0 |
| [session-management](session-management/) | 修改 ZCode 会话管理（左侧任务列表、tasks-index.sqlite、sessions-index、CLI session store、标题/状态/置顶/归档/未读/删除、虚拟项目与 roots、workspace 身份、相关 migration）之前必读。它把 2026-09… | Apache-2.0 |
| [skill-creator](skill-creator/) | Create new skills, edit existing skills, and iterate wording. Use when writing SKILL.md from scratch, improving existing skills, turning repeated workflows into reusable… | Apache-2.0 |
| [subagent-driven-development](subagent-driven-development/) | Use when executing implementation plans with independent tasks in the current session | MIT |
| [systematic-debugging](systematic-debugging/) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | MIT |
| [test-driven-development](test-driven-development/) | Use when implementing any feature or bugfix, before writing implementation code | MIT |
| [using-git-worktrees](using-git-worktrees/) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native… | MIT |
| [using-superpowers](using-superpowers/) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions | MIT |
| [vercel-react-best-practices](vercel-react-best-practices/) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to… | MIT |
| [vercel-react-view-transitions](vercel-react-view-transitions/) | Guide for implementing smooth, native-feeling animations using React's View Transition API (`&lt;ViewTransition>` component, `addTransitionType`, and CSS view transition… | MIT |
| [verification-before-completion](verification-before-completion/) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before… | MIT |
| [visualize](visualize/) | Create visualizations and interactive tools directly in conversation. Proactively use to show how something works; explore 'what happens when', 'what changes', or 'help… | Apache-2.0 |
| [web-gui-tester](web-gui-tester/) | Use the browser automation tooling available in the session to test web frontends interactively in a purely GUI-based, black-box manner: simulate real user clicks, text… | Apache-2.0 |
| [writing-plans](writing-plans/) | Use when you have a spec or requirements for a multi-step task, before touching code | MIT |
| [writing-skills](writing-skills/) | Use when creating new skills, editing existing skills, or verifying skills work before deployment | MIT |
| [xlsx](xlsx/) | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx… | Apache-2.0 |
| [xlsx-viewer](xlsx-viewer/) | View and discuss Excel (.xlsx) workbooks with the user in the Spreadsheets side panel. Use when the user wants to open, look through or ask about a workbook in the… | Apache-2.0 |
| [zcode-configuration-guide](zcode-configuration-guide/) | Use when configuring ZCode's extension resources (MCP servers, slash commands, skills, hooks, and plugins) or instruction files such as AGENTS.md in the ZCode client… | Apache-2.0 |
| [zcode-large-task-fixture](zcode-large-task-fixture/) | Generate, verify, or remove large synthetic ZCode task fixtures in local ~/.zcode persistence for UI/session performance testing. Use when testing big conversation/task… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/ZCode/agent-browser -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
