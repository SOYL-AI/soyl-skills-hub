# langflow

Skills from [langflow-ai/langflow](https://github.com/langflow-ai/langflow) at commit [`504c02f`](https://github.com/langflow-ai/langflow/tree/504c02fc47e76087b82b0e7cbe4186e9cdd916d4), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

All credit goes to the authors of langflow-ai/langflow. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [backend-code-review](backend-code-review/) | Review backend code for quality, security, maintainability, and best practices based on established checklist rules. Use when the user requests a review, analysis, or… | MIT |
| [component-refactoring](component-refactoring/) | Refactor high-complexity React components in Langflow frontend. Use when manual complexity assessment shows complexity > 50 or lineCount > 300, when the user asks for… | MIT |
| [e2e-testing](e2e-testing/) | Write and review Playwright E2E tests for Langflow. Trigger when the user asks to write, fix, or review E2E tests, spec files, Playwright tests, or integration tests… | MIT |
| [frontend-code-review](frontend-code-review/) | Review frontend code (.tsx, .ts, .js files) for quality, performance, and correctness against Langflow's frontend conventions. Supports pending-change reviews and… | MIT |
| [frontend-i18n](frontend-i18n/) | Add, change, or review user-facing text in the Langflow frontend using the i18n system (i18next / react-i18next). Use whenever a change adds or edits UI strings —… | MIT |
| [frontend-query-mutation](frontend-query-mutation/) | Guide for implementing Langflow frontend query and mutation patterns with Axios and TanStack React Query v5. Trigger when creating or updating API hooks in… | MIT |
| [frontend-testing](frontend-testing/) | — | MIT |
| [ibm-a11y-level1-audit](ibm-a11y-level1-audit/) | Perform a scoped IBM Equal Access Level 1 compliance audit of a chosen Langflow frontend surface (routes, components, or a PR) and produce a findings report mapped to… | MIT |
| [ibm-a11y-pr-remediation](ibm-a11y-pr-remediation/) | Scan every frontend surface touched by the current PR/branch for IBM Equal Access Level 1 accessibility issues and fix all in-scope violations by default. Discovers… | MIT |
| [ibm-a11y-route-scan](ibm-a11y-route-scan/) | Batch-scan Langflow frontend routes for accessibility issues using the Python IBM Equal Access scanner (scripts/a11y/a11y_scan.py) and produce JSON/Markdown/HTML… | MIT |
| [ibm-a11y-testing-guide](ibm-a11y-testing-guide/) | Reference guide for writing and running Langflow frontend accessibility tests with axe (Jest) and IBM Equal Access (Playwright `page.runA11yScan`). Covers which… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/langflow/backend-code-review -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
