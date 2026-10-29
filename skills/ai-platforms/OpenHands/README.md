# OpenHands

Skills from [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) at commit [`fee10e3`](https://github.com/OpenHands/OpenHands/tree/fee10e3d2909ebbf9950578575b1ee011492171e), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> 🙌 OpenHands: AI-Driven Development

All credit goes to the authors of OpenHands/OpenHands. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [desktop-electron](desktop-electron/) | This skill should be used when the user asks to "change the desktop app", "package Electron", "build a universal macOS app", "bundle Node or uv", "fix Electron startup"… | MIT |
| [e2e-testing](e2e-testing/) | This skill should be used when the user asks to "add an E2E test", "run live E2E", "run mock-LLM tests", "debug Playwright CI", "test the Docker image", or changes… | MIT |
| [frontend-api-contracts](frontend-api-contracts/) | This skill should be used when the user asks to "add an API call", "change a backend", "update settings persistence", "change conversation events", "fix backend auth"… | MIT |
| [frontend-development](frontend-development/) | This skill should be used when the user asks to "add UI copy", "add a translation", "optimize the frontend bundle", "change onboarding", "change conversation UI", "add a… | MIT |
| [local-stack-runtime](local-stack-runtime/) | This skill should be used when the user asks to "change the dev stack", "add a runtime service", "change the launcher", "update Docker", "bump Agent Server", "change… | MIT |
| [pr-design-doc](pr-design-doc/) | For a non-trivial pull request, write a self-contained HTML design doc under the temporary `.pr/` directory and link a visibility-appropriate preview in the PR… | MIT |
| [telemetry-analytics](telemetry-analytics/) | This skill should be used when the user asks to "add tracking", "add a PostHog event", "change telemetry consent", "instrument onboarding", "debug analytics", or changes… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/OpenHands/desktop-electron -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
