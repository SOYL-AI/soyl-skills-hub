# ffmpeg-skill

Skills from [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) at commit [`1ce2c18`](https://github.com/kajisho5/ffmpeg-skill/tree/1ce2c186bf1dba96132d87274eee46df4f537e0e), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> Local video editor for coding agents: 42 FFmpeg tools with a machine-readable contract and an MCP server, for Claude Code, Cursor and Codex. Cut, captions, reframe, loudness, platform exports. No cloud, no API keys.

All credit goes to the authors of kajisho5/ffmpeg-skill. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [building-python-mcp-servers](building-python-mcp-servers/) | Builds robust Python MCP (Model Context Protocol) servers with FastMCP — tool design, error contracts, event-loop-safe blocking work, subprocess/CLI wrapping… | MIT |
| [ci-pipeline-synthesizer](ci-pipeline-synthesizer/) | Generate GitHub Actions CI/CD pipeline configurations for automated building and testing of library and package projects. Use when creating or updating CI workflows for… | MIT |
| [concurrent-branches](concurrent-branches/) | Resolve conflicts and merges when several branches are open against one repo at the same time — the hotspot files every change must touch (registry manifests, a single… | MIT |
| [guarding-destructive-operations](guarding-destructive-operations/) | Add and review preconditions on operations that delete, overwrite, rewrite history, or resolve a caller-supplied name to a filesystem path — refusing instead of warning… | MIT |
| [keeping-git-repos-clean](keeping-git-repos-clean/) | Prevents, detects, and remediates files that should never be committed — secrets (.env, API tokens, hardcoded credentials) and dev artifacts (build output, scratch… | MIT |
| [managing-python-releases](managing-python-releases/) | Manages Python library releases including semantic versioning, changelog maintenance (Keep a Changelog format), release automation with GitHub Actions, and deprecation… | MIT |
| [reproducing-ci-locally](reproducing-ci-locally/) | Run the CI gate on your machine so it agrees with the runner — deriving the exact command, paths, markers, and env from the workflow file instead of the Makefile… | MIT |
| [reviewing-ffmpeg-skill-changes](reviewing-ffmpeg-skill-changes/) | Review a change to the ffmpeg-skill repository for the failures its own contract makes possible — a claim in a result document that is true at one layer and false at the… | MIT |
| [running-github-actions-efficiently](running-github-actions-efficiently/) | Cut GitHub Actions minutes and wall-clock time without losing coverage — the OS billing multiplier (macOS 10x / Windows 2x / Linux 1x), trigger hygiene that stops… | MIT |
| [shipping-across-surfaces](shipping-across-surfaces/) | Land a change everywhere the same fact is stated — enumerating the full surface inventory (landing copy, docs, machine-readable summaries, changelog badges repeated… | MIT |
| [shipping-build-artifacts](shipping-build-artifacts/) | Make the build step a real gate on what you actually distribute — build scripts that warn and exit 0 on a missing input, size checks with only an upper bound… | MIT |
| [verifying-external-behavior](verifying-external-behavior/) | Confirms what a third-party library, remote API, build backend, or scraped document actually does before writing code that depends on it — throwaway probes that run in… | MIT |
| [writing-defect-reports](writing-defect-reports/) | Establish a finding before you publish it, and correct it after — headlines that overstate what actually reproduces at the layer a user sees, reporting code that no… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/ffmpeg-skill/building-python-mcp-servers -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
