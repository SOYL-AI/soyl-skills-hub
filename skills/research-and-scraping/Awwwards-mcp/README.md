# Awwwards-mcp

Skills from [INSANE0777/Awwwards-mcp](https://github.com/INSANE0777/Awwwards-mcp) at commit [`97bf8b7`](https://github.com/INSANE0777/Awwwards-mcp/tree/97bf8b7302c0e63bcb8fd11563babca727d48d4b), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Free, open-source MCP server that gives AI coding agents (Claude Code, Codex, Cursor, OpenCode, ZCode…) design inspiration from award-winning websites — search with real screenshots, pull design DNA, capture and record live sites. A Mobbin alternative. No API key.

All credit goes to the authors of INSANE0777/Awwwards-mcp. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [awwwards-doctor](awwwards-doctor/) | Use when awwwards-mcp scraping or tools stop working — BlockedError, "layout may have changed" parser errors, empty results, failed captures, stale searches — or when… | MIT |
| [awwwards-inspiration](awwwards-inspiration/) | Use when building a site that needs design references (e.g. "make it feel premium", "dark 3D portfolio vibes"), when the user asks for standalone inspiration research… | MIT |
| [awwwards-motion-study](awwwards-motion-study/) | Use when building a site whose reference has animation — before writing any motion code, and again when verifying a build. Teaches what to record from a live site (and… | MIT |
| [awwwards-section-loop](awwwards-section-loop/) | Use when recreating or rebuilding a multi-section page from a reference site — build section by section instead of all at once. Teaches the loop map… | MIT |
| [awwwards-setup](awwwards-setup/) | Use when the awwwards MCP server or its skills are invoked for the first time in a session or on a new machine — when no awwwards preferences exist yet, or the user asks… | MIT |
| [motion-authoring](motion-authoring/) | Use when a converted project (build_project --authored) needs its motion authored — turning motion.manifest.json + inert skeletons into real per-section/page motion with… | MIT |
| [recreate](recreate/) | Recreate a website from a link — evidence-driven reconstruction with the awwwards MCP. Use when the user says "recreate this site", "clone this page", "rebuild… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/research-and-scraping/Awwwards-mcp/awwwards-doctor -g -a claude-code
```

Back to [Research and scraping](../../../catalog/research-and-scraping.md)
