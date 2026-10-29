# compai-crm

Skills from [trycompai/crm](https://github.com/trycompai/crm) at commit [`c9473b8`](https://github.com/trycompai/crm/tree/c9473b82e3b4bfd5d0598bbdf7c1f36f3d2d68f0), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM.

All credit goes to the authors of trycompai/crm. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ai-elements](ai-elements/) | Build AI chat interfaces using ai-elements components — conversations, messages, tool displays, prompt inputs, and more. Use when the user wants to build a chatbot, AI… | MIT |
| [ai-sdk](ai-sdk/) | Answer questions about the AI SDK and help build AI-powered features. Use when developers: (1) Ask about AI SDK functions like generateText, streamText, ToolLoopAgent… | MIT |
| [better-accessibility](better-accessibility/) | Accessibility engineering for product interfaces, from focus states and keyboard support to ARIA, forms, and screen readers. Use when building or reviewing UI… | MIT |
| [better-auth-best-practices](better-auth-best-practices/) | Configure Better Auth server and client, set up database adapters, manage sessions, add plugins, and handle environment variables. Use when users mention Better Auth… | MIT |
| [better-colors](better-colors/) | OKLCH color space and color usage for web projects. Convert hex/rgb/hsl to oklch, generate palettes, check contrast, handle gamut boundaries, theme with Tailwind v4, and… | MIT |
| [better-interface](better-interface/) | User-invoked, cross-discipline interface review that coordinates better-accessibility, better-layout, better-writing, better-typography, better-colors, and better-ui… | MIT |
| [better-layout](better-layout/) | Layout structure for web interfaces, from grouping and alignment to reading order, progressive disclosure, and adaptive breakpoints. Use when structuring a page or… | MIT |
| [better-typography](better-typography/) | Web typography from choosing fonts to spacing, wrapping and accessibility. Use when picking or pairing typefaces, configuring variable fonts or OpenType features… | MIT |
| [better-ui](better-ui/) | Design engineering principles for making interfaces feel polished. Use when building UI components, reviewing frontend code, implementing animations, hover states… | MIT |
| [better-writing](better-writing/) | UX writing and interface copy, from voice and button labels to error messages and empty states. Use when writing or reviewing any user-facing text: button and link… | MIT |
| [code-refactor-review](code-refactor-review/) | Reviews code changes for reuse, composition, codebase consistency, and slop. Use when asked to review PRs/diffs, check code reuse, composition, cleanliness, or whether… | MIT |
| [create-draft-pr](create-draft-pr/) | Commit, push, and create a draft PR using the pr-description format, with UX flow context when relevant. | MIT |
| [diffs](diffs/) | Use when an app uses @pierre/diffs to render or edit code files, diffs, patches, merge conflicts, or CodeView review surfaces, including React, vanilla JavaScript, SSR… | MIT |
| [eve](eve/) | Build durable backend AI agents with the eve framework. Use when creating, editing, or debugging an eve project — agent instructions, skills, tools, connections… | MIT |
| [ga](ga/) | Kick off a new feature or fix in a parallel clone with Pi working autonomously. Takes a problem description, generates a concise branch name, runs ga to set up the… | MIT |
| [ga-pr](ga-pr/) | Kick off follow-up work on an existing PR in a parallel tmux/agent session. Use when the user asks to work on a PR, continue a branch, address PR feedback, or resolve… | MIT |
| [gh-stack](gh-stack/) | Manages stacked PRs and splits multi-part work into reviewable branches with gh-stack. Use for stack creation, viewing, edits, push, submit, sync, rebase, merge, or… | MIT |
| [install-anti-slop](install-anti-slop/) | Install and configure the anti-slop Oxlint plugin in a local TypeScript or JavaScript repository. Use whenever a user asks to add anti-slop lint rules, copy the… | MIT |
| [nestjs-best-practices](nestjs-best-practices/) | NestJS best practices and architecture patterns for building production-ready applications. This skill should be used when writing, reviewing, or refactoring NestJS code… | MIT |
| [nestjs-trpc](nestjs-trpc/) | Build end-to-end type-safe tRPC APIs inside NestJS using the nestjs-trpc adapter — @Router/@Query/@Mutation/@Subscription decorators, TRPCModule.forRoot, injectable… | MIT |
| [no-use-effect](no-use-effect/) | Enforce the no-useEffect rule when writing or reviewing React code. ACTIVATE when writing React components, refactoring existing useEffect calls, reviewing PRs with… | MIT |
| [nuqs](nuqs/) | nuqs (type-safe URL query state) best practices for Next.js and other React frameworks. This skill should be used when writing, reviewing, or refactoring code that uses… | MIT |
| [pit-of-success](pit-of-success/) | Review or refactor code so the correct behavior is the default path; use when APIs, setters, hooks, helpers, or component props have footguns where a natural call… | MIT |
| [posthog-instrumentation](posthog-instrumentation/) | Automatically add PostHog analytics instrumentation to code. Triggers when user asks to add tracking, instrument events, add analytics, or implement feature flags in… | MIT |
| [prepare-branch-context](prepare-branch-context/) | Analyze the current branch's diff from main and related PR to build context for followup requests. Triggers on "prepare context", "branch context", "catch me up"… | MIT |
| [prisma-database-setup](prisma-database-setup/) | Guides for configuring Prisma with different database providers (PostgreSQL, MySQL, SQLite, MongoDB, etc.). Use when setting up a new project, changing databases, or… | MIT |
| [seo-audit](seo-audit/) | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO… | MIT |
| [shadcn](shadcn/) | Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI, including chat interfaces. Provides project context, component… | MIT |
| [turborepo](turborepo/) | Turborepo monorepo build system guidance. Triggers on: turbo.json, task pipelines, dependsOn, caching, remote cache, the "turbo" CLI, --filter, --affected, CI… | MIT |
| [typescript-advanced-types](typescript-advanced-types/) | Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for building type-safe applications… | MIT |
| [ux-flow-plan](ux-flow-plan/) | Create UX-first plans as flow trees, then attach concrete function names, files, and implementation anchors after the high-level flow is clear. | MIT |
| [vercel-composition-patterns](vercel-composition-patterns/) | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable… | MIT |
| [zero-tech-debt](zero-tech-debt/) | Rework a change as if the intended UX and architecture existed from day one, deleting compatibility cruft and accidental complexity. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/compai-crm/ai-elements -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
