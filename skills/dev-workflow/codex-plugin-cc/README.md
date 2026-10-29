# codex-plugin-cc

Skills from [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) at commit [`db52e28`](https://github.com/openai/codex-plugin-cc/tree/db52e28f4d9ded852ab3942cea316258ae4ef346), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> Use Codex from Claude Code to review code or delegate tasks.

All credit goes to the authors of openai/codex-plugin-cc. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [codex-cli-runtime](codex-cli-runtime/) | Internal helper contract for calling the codex-companion runtime from Claude Code | Apache-2.0 |
| [codex-result-handling](codex-result-handling/) | Internal guidance for presenting Codex helper output back to the user | Apache-2.0 |
| [gpt-5-4-prompting](gpt-5-4-prompting/) | Internal guidance for composing Codex and GPT-5.4 prompts for coding, review, diagnosis, and research tasks inside the Codex Claude Code plugin | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/codex-plugin-cc/codex-cli-runtime -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
