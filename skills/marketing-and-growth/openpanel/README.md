# openpanel

Skills from [Openpanel-dev/openpanel](https://github.com/Openpanel-dev/openpanel) at commit [`dda72e2`](https://github.com/Openpanel-dev/openpanel/tree/dda72e20d204c31cd71b01d219f861303b4bed52), copied into SOYL Hub on 2026-10-29. Licence: AGPL-3.0.

> OpenPanel is an open-source web and product analytics platform, an open-source alternative to Mixpanel with optional self-hosting.

All credit goes to the authors of Openpanel-dev/openpanel. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [clean-code](clean-code/) | Coding standards for this repo - concise, direct, no over-engineering, and no comments that carry no knowledge. Use when writing or reviewing any code here, and whenever… | AGPL-3.0 |
| [merge](merge/) | Squash merge a GitHub PR with a conventional-commit title and a body that describes everything the PR changed, so the release tooling can build the version bump and… | AGPL-3.0 |
| [pr](pr/) | Push the current branch, open a PR (or pick up the existing one), then wait for CodeRabbit's review and work through its comments, fixing the valid ones and replying to… | AGPL-3.0 |
| [sdk-testbed](sdk-testbed/) | Verify a change to the JavaScript SDKs (packages/sdks/sdk, packages/sdks/web and the wrappers built on them) the way a customer site would hit it - drive apps/testbed in… | AGPL-3.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/openpanel/clean-code -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
