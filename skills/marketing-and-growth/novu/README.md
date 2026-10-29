# novu

Skills from [novuhq/novu](https://github.com/novuhq/novu) at commit [`85a346b`](https://github.com/novuhq/novu/tree/85a346ba38c8f1e8f50be0cbfe24b6f0b8795860), copied into SOYL Hub on 2026-10-29. Licence: MIT+Proprietary.

> The open-source communication infrastructure for agents and products

All credit goes to the authors of novuhq/novu. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [add-channel-connect-button](add-channel-connect-button/) | Build a new channel Connect button (e.g. WhatsApp, Discord, LINE) in @novu/js and @novu/react following the existing SlackConnectButton, MsTeamsConnectButton, and… | MIT |
| [add-channel-setup-guide](add-channel-setup-guide/) | Add a new chat channel's layer-1 setup guide — the in-dashboard &lt;Channel>SetupGuide that walks a developer through connecting the channel itself (create app/bot →… | MIT |
| [add-channel-whats-next-onboarding](add-channel-whats-next-onboarding/) | Add a new chat channel's layer-2 dashboard onboarding — the connected-state "What's next" / "FOR YOUR USERS" developer-rollout guide plus its connected details page — in… | MIT |
| [address-pr-review](address-pr-review/) | Critically triage pull request review comments against PR requirements and codebase reality, implement only valid fixes, and reply only when declining a suggestion. Use… | MIT |
| [better-auth-best-practices](better-auth-best-practices/) | Skill for integrating Better Auth - the comprehensive TypeScript authentication framework. | MIT |
| [email-best-practices](email-best-practices/) | Use when building email features, emails going to spam, high bounce rates, setting up SPF/DKIM/DMARC authentication, implementing email capture, ensuring compliance… | MIT |
| [enterprise-submodule](enterprise-submodule/) | — | MIT |
| [env-setup](env-setup/) | Create or update Novu environment variables in the user's project safely (never expose the secret key to the client). Complements the official Novu skills by covering… | MIT |
| [figma-use](figma-use/) | **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it… | MIT |
| [frontend-design](frontend-design/) | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters… | Apache-2.0 |
| [ink-tui-wizard](ink-tui-wizard/) | Build terminal user interfaces (TUIs) using Ink (React for CLIs) and @inkjs/ui with a reactive, session-driven wizard pattern. Use when creating interactive CLI… | MIT |
| [linear-release-setup](linear-release-setup/) | Generate CI/CD configuration for Linear Release. Use when setting up release tracking, configuring CI pipelines for Linear, or integrating deployments with Linear… | MIT |
| [novu-dashboard-workflows](novu-dashboard-workflows/) | Author step content for Novu workflows defined in the Dashboard or generated/edited via the Novu MCP. Use when filling in step controls (subject, body, editorType… | MIT |
| [novu-design-workflow](novu-design-workflow/) | Design notification workflows the Novu way — choose channels, set severity, decide when a workflow is critical, configure digests, and route based on subscriber state… | MIT |
| [novu-framework-integration](novu-framework-integration/) | Build code-first notification workflows with @novu/framework. Use when defining workflows in TypeScript (Zod / JSON Schema / Class Validator), composing channel steps… | MIT |
| [novu-inbox-integration](novu-inbox-integration/) | Integrate Novu's in-app notification inbox into web applications. Supports React, Next.js, and vanilla JavaScript. Includes the Inbox component (bell icon + notification… | MIT |
| [novu-manage-preferences](novu-manage-preferences/) | Configure notification preferences in Novu at the workflow and subscriber level. Set default channel preferences (email, SMS, push, chat, in-app), mark preferences as… | MIT |
| [novu-manage-subscribers](novu-manage-subscribers/) | Create, update, search, and delete subscribers in Novu. Manage topics for group-based notification targeting. Set subscriber credentials for push and chat channels. Use… | MIT |
| [novu-prepare-pr](novu-prepare-pr/) | Post-implementation PR prep for Novu feature branches — quality passes, commit/PR hygiene, CI triage, and review feedback. Use after feature work is done, when the user… | MIT |
| [novu-trigger-notification](novu-trigger-notification/) | Trigger Novu notification workflows to send messages across email, SMS, push, chat, and in-app channels. Supports single triggers, bulk triggers, broadcast to all… | MIT |
| [nv-endpoint-routed-tool-provider](nv-endpoint-routed-tool-provider/) | Build or refactor a Tool-channel provider (PagerDuty, Opsgenie, future incident/alerting tools) to be endpoint-routed: per-subscriber secrets encrypted on the channel… | MIT |
| [nv-implement](nv-implement/) | Implement planned work by fanning out parallel subagents on isolated worktrees — TDD at pre-agreed seams, per-slice nv-park-and-review, merge back, full suite once at… | MIT |
| [nv-onboard-dcr-mcp](nv-onboard-dcr-mcp/) | Onboard a new DCR OAuth MCP catalog entry with provider-doc vetting and curl probes. Use when adding or changing `mode: dcr` entries in MCP_SERVERS. Abort if the… | MIT |
| [nv-park-and-review](nv-park-and-review/) | Commit local changes as a baseline, hop into a lightweight review worktree, run a thermo-nuclear code quality review scoped to ONLY that commit, commit the resulting… | MIT |
| [nv-worktree-cleanup](nv-worktree-cleanup/) | Audits git worktrees and removes the ones that are safe to delete — merged into the base branch (including squash-merges via `gh`), missing on disk, or explicitly… | MIT |
| [nv-worktree-commands](nv-worktree-commands/) | Git worktree command reference: path naming, create/remove/prune, `.env` copy and cleanup. Use when implementing or debugging worktree setup — not as the primary… | MIT |
| [nv-worktree-create](nv-worktree-create/) | Create a sibling git worktree and a new branch with the same name, copy local `.env` files, optionally initialize the enterprise submodule (`--enterprise`), and move the… | MIT |
| [react-email](react-email/) | Use when creating HTML email templates with React components - welcome emails, password resets, notifications, order confirmations, newsletters, or transactional emails. | MIT |
| [run-api-e2e-tests](run-api-e2e-tests/) | Run e2e tests for the API service. Use when the user wants to run API E2E tests. | MIT |
| [sanity-changelog](sanity-changelog/) | Create and publish Novu changelog entries in Sanity (changelogPost documents), including feature posts, "improvements & fixes" roundups built from Linear releases, and… | MIT |
| [testerarmy-cli](testerarmy-cli/) | Use TesterArmy CLI to create, organize, and run dashboard-managed QA tests. Prefer saved tests, groups, project context, credentials, and remote runs over one-off local… | MIT |
| [triage-agent-eval-failures](triage-agent-eval-failures/) | Triage failing @novu/agent-evals scenarios to decide whether a failure is real or flaky, and whether to fix the playbook/prompt or the test (grader, tape, scenario, or… | MIT |
| [verify-in-box](verify-in-box/) | Verify a change end to end on the Novu Box, a full Novu Cloud stack in one container on Cloudflare. Use when a change to apps/, libs/, packages/, enterprise/ or… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/novu/add-channel-connect-button -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
