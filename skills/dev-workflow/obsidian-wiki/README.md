# obsidian-wiki

Skills from [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) at commit [`c5dc0e2`](https://github.com/Ar9av/obsidian-wiki/tree/c5dc0e2d73ba958649e4b099fab1052a1e06033a), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Framework for AI agents to build and maintain a digital brain through Obsidian wiki \| Memory System for Agents

All credit goes to the authors of Ar9av/obsidian-wiki. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [claude-history-ingest](claude-history-ingest/) | Ingest Claude Code conversation/session history into Obsidian as distilled knowledge. Use for importing or mining past Claude sessions, .claude data, project/session… | MIT |
| [code-understand](code-understand/) | Map the load-bearing files, symbols, callers, and dependencies of an unfamiliar codebase before making changes. Use for architecture orientation, impact analysis… | MIT |
| [codex-history-ingest](codex-history-ingest/) | Ingest Codex CLI conversation/session history into Obsidian as distilled knowledge. Use for importing or mining ~/.codex sessions, rollout files, indexes, or transcript… | MIT |
| [copilot-history-ingest](copilot-history-ingest/) | Ingest GitHub Copilot CLI/session history into Obsidian as distilled knowledge. Use for importing or mining Copilot history; not for general Copilot help, simple session… | MIT |
| [cross-linker](cross-linker/) | Find and add missing cross-references between wiki pages. Use when pages are disconnected or after large ingestion. This modifies pages to add links; use wiki-lint for… | MIT |
| [daily-update](daily-update/) | Run or configure the daily wiki maintenance cycle: check source freshness, refresh the index and hot.md, and manage its scheduled 9 AM launchd/systemd/cron reminder. Use… | MIT |
| [graph-colorize](graph-colorize/) | Configure Obsidian graph colors by tag, folder, category, or visibility by updating .obsidian/graph.json. Use for graph colorization; preserve other graph settings and… | MIT |
| [hermes-history-ingest](hermes-history-ingest/) | Ingest Hermes agent history into Obsidian as distilled knowledge. Use for importing or mining ~/.hermes sessions, memories, or logs; use wiki-agent for targeted… | MIT |
| [impl-validator](impl-validator/) | Independently check whether an implementation matches its stated goal and return PASS/WARN/FAIL with actionable issues. Use for second-opinion validation of an… | MIT |
| [llm-wiki](llm-wiki/) | Explain and apply the foundational LLM Wiki architecture and knowledge-management strategy. Use for setup, architecture, schema, or organization decisions; operational… | MIT |
| [memory-bridge](memory-bridge/) | Browse or compare wiki knowledge by originating AI tool. Use for cross-tool memory questions, tool-specific knowledge, or gap/diff analysis between Codex, Claude… | MIT |
| [obsidian-layout-adjustment](obsidian-layout-adjustment/) | Adjust the user's Obsidian visual layout with CSS snippets. Use for restyling tabs, sidebars, note surfaces, properties, backlinks, graph or file-explorer UI, or… | MIT |
| [openclaw-history-ingest](openclaw-history-ingest/) | Ingest OpenClaw session/history data into Obsidian as distilled knowledge. Use for importing or mining ~/.openclaw sessions, memory files, or logs; use wiki-agent for… | MIT |
| [pi-history-ingest](pi-history-ingest/) | Ingest Pi coding-agent session history into Obsidian as distilled knowledge. Use for importing or mining ~/.pi/agent/sessions or Pi conversation logs; use wiki-agent for… | MIT |
| [session-brain](session-brain/) | Build or refresh a browser-viewable topic graph over Claude session history using local clustering. Use for mapping or clustering sessions, recent or stale topic… | MIT |
| [session-search](session-search/) | Search the session-brain graph for a past agent session by topic and load the winning transcript into the current conversation. Use for finding which session handled X… | MIT |
| [tag-taxonomy](tag-taxonomy/) | Apply and maintain the wiki's controlled tag vocabulary. Use for choosing, normalizing, auditing, or extending tags when creating or updating wiki pages; consult the… | MIT |
| [vault-skill-factory](vault-skill-factory/) | Create a reviewable Agent Skill package from mature curated wiki pages. Use when turning verified vault knowledge into a reusable skill. Reads the vault and writes only… | MIT |
| [wiki-agent](wiki-agent/) | Search one AI agent's raw history for a specific topic, ingest only matching sessions, and return a synthesized answer. Use for targeted cross-agent recall; use… | MIT |
| [wiki-capture](wiki-capture/) | Turn the current conversation or finding into a structured permanent wiki note. Use for save/capture/preserve requests; QUICK MODE writes a fast _raw/ note. Supports… | MIT |
| [wiki-context-pack](wiki-context-pack/) | Produce a token-bounded, citation-ready context slice from an existing Obsidian vault for a downstream agent or task. Use for "/wiki-context-pack", "use my vault as… | MIT |
| [wiki-dashboard](wiki-dashboard/) | Create dynamic, queryable Obsidian dashboard views using Bases or Dataview. Use for auto-updating tables, indexes, or structured views of vault content; not for ordinary… | MIT |
| [wiki-dedup](wiki-dedup/) | Detect and merge wiki pages representing the same concept under different names. Use for page-identity deduplication and consolidation. Destructive merges require… | MIT |
| [wiki-digest](wiki-digest/) | Produce a day/week/month knowledge digest summarizing what was learned, updated, and connected in the wiki. Use for readable recent-learning summaries; wiki-status… | MIT |
| [wiki-export](wiki-export/) | Export the Obsidian wiki graph to JSON, GraphML, Neo4j Cypher, Postgres/SQL, HTML, or OKF bundles. Use when transferring or visualizing wiki data in external tools… | MIT |
| [wiki-history-ingest](wiki-history-ingest/) | Route generic agent-history ingestion requests to the appropriate specialized history-ingest skill. Use when the user asks to ingest AI-agent history without directly… | MIT |
| [wiki-import](wiki-import/) | Import a wiki graph into the current vault from graph.json or an OKF/markdown bundle. Use for transferring previously exported wiki content between vaults; pair with… | MIT |
| [wiki-ingest](wiki-ingest/) | Ingest new documents, raw text, folders, or URLs into the Obsidian wiki as distilled, linked knowledge. Use for general wiki ingestion when no more specific ingest skill… | MIT |
| [wiki-lint](wiki-lint/) | Audit wiki health: broken links, orphans, contradictions, stale content, lifecycle and tag issues. Use for maintenance or health checks. Default is report-only; use… | MIT |
| [wiki-narrate](wiki-narrate/) | Turn a wiki topic into a cited Markdown briefing, plain-language explanation, or progressive lecture. Use this skill for topic-based briefing, explanation, and lecture… | MIT |
| [wiki-query](wiki-query/) | Search and synthesize answers from the compiled Obsidian wiki, including cited and multi-hop answers. Use for questions about existing wiki knowledge or fast index-only… | MIT |
| [wiki-rebuild](wiki-rebuild/) | Archive and rebuild wiki knowledge from source, or restore a prior archive. Use for full restart/recovery when incremental repair is inappropriate; this is broader and… | MIT |
| [wiki-research](wiki-research/) | Perform multi-round web research on a topic, synthesize the findings, and file structured results into the Obsidian wiki. Use for comprehensive web-sourced research… | MIT |
| [wiki-setup](wiki-setup/) | Initialize or repair an Obsidian wiki vault's required structure and configuration. Use for new-vault setup, .env/config creation, reconfiguration, or broken setup… | MIT |
| [wiki-stage-commit](wiki-stage-commit/) | Review staged wiki writes and promote accepted pages to final locations when WIKI_STAGED_WRITES is enabled. Use for staging approval/commit; rejected pages return to… | MIT |
| [wiki-status](wiki-status/) | Report wiki ingestion/completeness state, pending source delta, structural insights, or maintenance equilibrium. Use for remaining-work/status questions, hubs and… | MIT |
| [wiki-switch](wiki-switch/) | List, create, or switch named Obsidian wiki vault profiles under the global config directory. Use when changing the active vault, checking which vault is active, or… | MIT |
| [wiki-synthesize](wiki-synthesize/) | Find recurring concept combinations across the wiki that lack an explicit synthesis page, then create cross-cutting synthesis pages. Use for knowledge synthesis after… | MIT |
| [wiki-update](wiki-update/) | Sync knowledge from the current project into the Obsidian wiki. Use when work already in the current project should be distilled into the vault; named-vault routing… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/obsidian-wiki/claude-history-ingest -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
