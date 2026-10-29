# open-saas

Skills from [wasp-lang/open-saas](https://github.com/wasp-lang/open-saas) at commit [`53dcb2c`](https://github.com/wasp-lang/open-saas/tree/53dcb2c066286248f633c1db62e7d7e9af3d5d0c), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> A 100% free modern JS SaaS boilerplate (React, NodeJS, Prisma). Full-featured: Auth (email, google, github, slack, MS), Email sending, Background jobs, Landing page, Payments (Stripe, Polar.sh), Shadcn UI, S3 file upload. AI-ready with tailored AGENTS.md, skills, and Claude Code plugin. One cmd…

All credit goes to the authors of wasp-lang/open-saas. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [add-wasp-skills](add-wasp-skills/) | Install Wasp agent skills (plugins) that add Wasp knowledge and best practices to your AI coding tools. | MIT |
| [getting-started](getting-started/) | Get started with your Open SaaS project — fetches docs, checks Wasp installation, and helps you start your database and app. | MIT |
| [guided-tour](guided-tour/) | Take a guided tour of Open SaaS — walks you through step-by-step through the project structure, features, and customization checklist. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/open-saas/add-wasp-skills -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
