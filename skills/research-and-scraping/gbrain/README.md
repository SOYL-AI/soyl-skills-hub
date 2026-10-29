# gbrain

Skills from [garrytan/gbrain](https://github.com/garrytan/gbrain) at commit [`7a066c2`](https://github.com/garrytan/gbrain/tree/7a066c21a212892fd191b63907506ddcfce94f7b), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Garry's Opinionated OpenClaw/Hermes Agent Brain

All credit goes to the authors of garrytan/gbrain. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [academic-verify](academic-verify/) | Verify a research claim or academic citation by tracing it through publication → methodology → raw data → independent replication. Routes through perplexity-research for… | MIT |
| [archive-crawler](archive-crawler/) | Universal archivist for personal file archives (Dropbox/B2/Gmail-takeout/local-mount/hard-drive-dump). Filters for high-value content (the user's own writing, ideas… | MIT |
| [article-enrichment](article-enrichment/) | Transform raw article text dumps in the brain into structured pages with executive summary, verbatim quotes, key insights, why-it-matters, and cross-references. Replaces… | MIT |
| [ask-user](ask-user/) | Reusable pattern for presenting the user with explicit choices and gating execution until they respond. Used by other skills when a decision point requires human input… | MIT |
| [blog-ingest](blog-ingest/) | Feed and whole-publication ingestion: turn an entire blog, newsletter, or RSS/Atom archive into brain source pages. Covers feed discovery, pagination walking… | MIT |
| [book-mirror](book-mirror/) | Take any book (EPUB/PDF), produce a personalized chapter-by-chapter analysis. Each chapter is preserved in detail (The Chapter) and mirrored back to the reader's actual… | MIT |
| [brain-ingest-gate](brain-ingest-gate/) | Pre-write quality gate for content entering the brain. No raw copies: a bare cp/mv into the brain repo is a bug. Before any new page lands, resolve named entities… | MIT |
| [brain-link-discipline](brain-link-discipline/) | When you report a brain page to the user — created, edited, committed, or relayed from a subagent — a working link is part of the deliverable, in the SAME message… | MIT |
| [brain-ops](brain-ops/) | Brain knowledge base operations. The core read/write cycle: brain-first lookup, read-enrich-write loop, source attribution, ambient enrichment, back-linking. Read this… | MIT |
| [brain-pdf](brain-pdf/) | Generate a publication-quality PDF from any brain page via the gstack make-pdf binary. Strips YAML frontmatter, sanitizes emoji, applies running headers and page… | MIT |
| [brain-taxonomist](brain-taxonomist/) | Filing gate for ALL brain writes. Consulted before creating any new brain page to determine the correct path. Reads the ACTIVE schema pack via `gbrain schema show… | MIT |
| [briefing](briefing/) | Compile daily briefing with meeting context, active deals, and citation tracking | MIT |
| [bulk-ingestion](bulk-ingestion/) | End-to-end discipline for turning any large data source (audio libraries, email takeouts, document corpora, chat exports, API dumps) into brain pages at scale. The… | MIT |
| [capture](capture/) | Save any thought or content into the brain via one CLI command. The single human-facing entrypoint that replaces "put_page vs commit-then-sync vs autopilot-wait" with… | MIT |
| [chat-connectors](chat-connectors/) | Connect a ChatGPT or Claude account and sync its conversation history into the brain automatically. Cookie paste-in is the primary lane; sync is incremental (watermark +… | MIT |
| [citation-fixer](citation-fixer/) | Audit and fix citation formatting across brain pages. Ensures every fact has an inline [Source: ...] citation matching the standard format. Extended in v0.25.1: scans… | MIT |
| [citation-graph-ingest](citation-graph-ingest/) | Build a TYPED citation/reference graph over an ingested corpus — not just embeddings. Flat similarity retrieval cannot tell you that document A *overrules* B… | MIT |
| [cold-start](cold-start/) | Day-one data bootstrapping for a new brain. Sequences the highest-leverage data sources to go from empty brain to useful brain in one session. Uses ClawVisor for safe… | MIT |
| [company-brainify](company-brainify/) | Extract a sanitized shared team/company brain from a personal brain. Strips internal ratings, compensation, performance assessments, retention and political dynamics… | MIT |
| [concept-synthesis](concept-synthesis/) | Deduplicate and synthesize raw concept stubs into a tiered intellectual map (T1 Canon to T4 Riff), tracing idea evolution across sources over time. Transforms thousands… | MIT |
| [context-audit](context-audit/) | Token-hygiene audit of the always-loaded context stack — CLAUDE.md, AGENTS.md, auto-memory MEMORY.md, and the bootstrap-rendered identity files (SOUL.md, USER.md… | MIT |
| [conversation-archive](conversation-archive/) | Import AI-assistant chat exports (ChatGPT, Claude, Perplexity) and agent session transcripts into the brain as one dated page per conversation under conversations/… | MIT |
| [correction-pipeline](correction-pipeline/) | When the user corrects a factual error, root-cause it immediately. Don't just note the correction — trace the error to its source, fix the source, and prevent… | MIT |
| [cron-scheduler](cron-scheduler/) | Schedule management with staggering, quiet hours, and wake-up override. Validates schedules, prevents collisions, and gates delivery during quiet hours. | MIT |
| [cross-modal-review](cross-modal-review/) | Quality gate via second model. Spawn a different AI model to review work before committing. Includes refusal routing: if one model refuses, switch silently to the next… | MIT |
| [daily-task-manager](daily-task-manager/) | Task lifecycle management with stable task IDs. Add, complete, defer, remove, and review tasks with deterministic action routing and fail-closed ambiguity handling… | MIT |
| [daily-task-prep](daily-task-prep/) | Morning preparation. Calendar lookahead, meeting context loading, open threads from yesterday, active task review. Extends briefing with actionable prep. | MIT |
| [data-loss-gate](data-loss-gate/) | Confirmation gate before any bulk delete, cleanup, or destructive operation that could result in data loss — shell-level (rm -rf, git rm, bulk sed) or brain-level (bulk… | MIT |
| [data-research](data-research/) | Structured data research: search sources, extract structured data, archive raw sources, maintain canonical tracker pages, deduplicate. Parameterized via YAML recipes for… | MIT |
| [db-repair](db-repair/) | Auto-fix gbrain's Postgres access so the brain stays available. When any gbrain command or MCP tool result carries a `GBRAIN_DB_ACCESS &lt;reason>` marker (or an… | MIT |
| [draft-in-voice](draft-in-voice/) | Ghostwrite content in a specific person's voice from a VALIDATED voice profile — tweets, replies, short posts, launch copy, recruiting blurbs, emails. Loads the… | MIT |
| [eiirp](eiirp/) | Everything In Its Right Place. The universal post-work organizer. After any significant work session, EIIRP runs a 7-phase audit: (1) inventory every output, (2) walk… | MIT |
| [enrich](enrich/) | Enrich brain pages with tiered enrichment protocol. Creates and updates person/company pages with compiled truth, timeline, and cross-links. Use when a new entity is… | MIT |
| [fact-check](fact-check/) | Systematic claim-by-claim verification for any content before it ships. Modeled on professional fact-checking desks (The New Yorker, ProPublica, IFCN standards): extract… | MIT |
| [frontmatter-guard](frontmatter-guard/) | Validate and auto-repair YAML frontmatter on brain pages. Catches malformed pages before they enter the brain (missing closing ---, nested quotes, slug mismatches, null… | MIT |
| [functional-area-resolver](functional-area-resolver/) | Compress an agent's routing file (RESOLVER.md or AGENTS.md) by converting granular skill-per-row tables into functional-area dispatchers. Each area lists sub-skills in a… | MIT |
| [gbrain](gbrain/) | Search and write the company knowledge brain. Use for any question about the org, people, projects, decisions, or history, and to persist durable knowledge beyond this… | MIT |
| [gbrain-advisor](gbrain-advisor/) | Proactive "make the most of gbrain" coaching. Runs `gbrain advisor` on a cadence and pings the user with the top high-leverage actions for their brain: version drift… | MIT |
| [gbrain-upgrade](gbrain-upgrade/) | Keep gbrain current. When a `gbrain` invocation prints an `UPGRADE_AVAILABLE &lt;old> &lt;new>` marker (or `gbrain self-upgrade --check-only` reports an update), apply… | MIT |
| [google-loops](google-loops/) | Set up and operate the Gmail/Calendar/Contacts connector and the open-loop engine: who is waiting on the user, what they promised, and the context needed to respond… | MIT |
| [idea-ingest](idea-ingest/) | Ingest links, articles, tweets, and ideas into the brain. Fetch content, save to brain with analysis, credit the author (people page only when they pass the notability… | MIT |
| [idea-lineage](idea-lineage/) | Trace one idea's evolution through the brain: first mention, best articulation, related concepts, reversals, contradictions, abandoned branches, and the current live… | MIT |
| [ingest](ingest/) | Route content to specialized ingestion skills. Detects input type and delegates. | MIT |
| [maintain](maintain/) | Brain health checks: back-link enforcement, citation audit, filing validation, stale info detection, orphan pages, and benchmarks. Use when asked to check brain health… | MIT |
| [mcp-access](mcp-access/) | Open the GBrain owner dashboard, manage MCP clients and permissions, or connect a native OAuth harness. Distinguishes owner administration from ordinary MCP access. | MIT |
| [measure-before-you-fix](measure-before-you-fix/) | Before fixing a slow/stale/timeout alert, measure the step yourself. Kill the theory with a stopwatch, not a code change. Measure-first ops triage for temporal alerts… | MIT |
| [media-ingest](media-ingest/) | Ingest video, audio, PDF, book, screenshot, and GitHub repo content into the brain. Multi-format handling with entity extraction and backlink propagation. Covers… | MIT |
| [meeting-ingestion](meeting-ingestion/) | Ingest meeting transcripts from ANY meeting recorder into brain pages with attendee enrichment, entity propagation, and timeline merge. One unified pipeline: normalize… | MIT |
| [migrate](migrate/) | Universal migration from Obsidian, Notion, Logseq, markdown, CSV, JSON, Roam | MIT |
| [minion-orchestrator](minion-orchestrator/) | Unified Minions skill for both deterministic shell jobs and LLM subagent orchestration. Replaces the older `gbrain-jobs` routing intent. Use when: submitting gbrain… | MIT |
| [perplexity-research](perplexity-research/) | Brain-augmented web research. Sends brain context about a topic to Perplexity, which searches the web with citations and returns what is NEW vs what the brain already… | MIT |
| [postgres-adopt](postgres-adopt/) | Detect which gbrain engine is in use (PGLite vs Postgres), prefer Postgres for agent-harness installs, install/provision Postgres (Supabase discovery via… | MIT |
| [publish](publish/) | Share brain pages as beautiful password-protected HTML with zero LLM calls | MIT |
| [query](query/) | Answer questions using the brain's knowledge with 3-layer search, synthesis, and citation propagation. Use when the user asks a question, wants a lookup, or needs… | MIT |
| [reference-pack](reference-pack/) | Reference skill demonstrating the 10/10 skillpack contract. Adds a "what does this skillpack do" answer to the user's agent. | MIT |
| [remote-mcp](remote-mcp/) | Publish the user's own gbrain over MCP so other devices, desktop apps and cloud agents can reach it. `gbrain mcp expose` installs and signs in Tailscale, publishes the… | MIT |
| [repo-architecture](repo-architecture/) | Where new brain files go. Decision protocol for filing brain pages by primary subject, not by format or source. Reference for all brain-writing skills. | MIT |
| [reports](reports/) | Save and load timestamped reports. Keyword routing for fast lookup. Cron jobs save output as reports; the agent or user queries them by keyword. Includes the… | MIT |
| [research-compendium](research-compendium/) | Deep-research a topic end to end and produce a permanent, reusable knowledge asset: archive every primary source verbatim (gated by the user's privacy/retention… | MIT |
| [resolve-before-asking](resolve-before-asking/) | Gate on identity questions to the user. Before any "who is X?" (or role / relationship question) reaches the user, exhaust the brain's lookup chain: think → search +… | MIT |
| [retrieval-reflex](retrieval-reflex/) | When/what to retrieve — open the brain page for a salient entity before answering from memory. | MIT |
| [schema-author](schema-author/) | Evolve your brain's schema pack. Add page types, propose new ones from corpus scans, backfill page.type on existing pages, audit pack health. Triggers when an agent… | MIT |
| [schema-unify](schema-unify/) | Migrate a brain from gbrain-base (or any pack) to gbrain-base-v2's 14-canonical-type taxonomy via gbrain onboard --check + the unify-types Minion handler. Collapses 94… | MIT |
| [setup](setup/) | Add keyless GBrain memory to an existing agent, or connect a hosted brain while preserving identity and configuration | MIT |
| [signal-detector](signal-detector/) | Opt-in ambient signal capture. After explicit enablement, applies on substantive inbound messages to detect original thinking and entity mentions. Use an authorized… | MIT |
| [skill-autobench](skill-autobench/) | Author an eval for an existing skill from its REAL usage history, not its spec. Mine invocations from the brain's conversation archive (conversations/) and per-harness… | MIT |
| [skill-creator](skill-creator/) | Create new skills following the GBrain conformance standard. Generates SKILL.md with frontmatter, Contract, Phases, Output Format, and Anti-Patterns. Checks MECE against… | MIT |
| [skill-optimizer](skill-optimizer/) | Self-evolving skill optimization via SkillOpt-paper-grounded text-space optimizer. | MIT |
| [skillify](skillify/) | The meta skill. Turn any raw feature into a properly-skilled, tested, resolvable unit of agent capability. Idempotent: running on an existing skill improves it (bug fix… | MIT |
| [skillpack-check](skillpack-check/) | Run `gbrain skillpack-check` to produce an agent-readable JSON health report for the gbrain install. Wraps `gbrain doctor` + `gbrain apply-migrations --list` so a host… | MIT |
| [skillpack-harvest](skillpack-harvest/) | Lift a proven skill from a host repo (e.g. your OpenClaw fork) back into gbrain's bundle so other clients can scaffold it. Editorial workflow: the CLI does the file copy… | MIT |
| [smoke-test](smoke-test/) | Health smoke tests + auto-fix for gbrain installs (and OpenClaw services when present). Run after machine/container restarts or whenever something seems broken. Tests… | MIT |
| [soul-audit](soul-audit/) | Re-run or deepen the agent's identity interview. Drives the SHARED bootstrap answer bank (state/interview.json) via `gbrain bootstrap interview --set/--show/--confirm`… | MIT |
| [strategic-reading](strategic-reading/) | Read a book, article, transcript, or case study through the lens of a specific strategic problem you're facing. Produces an applied playbook that maps the source onto… | MIT |
| [testing](testing/) | Skill validation framework PLUS daily test-suite health and regression intelligence. Validates skill conformance (frontmatter, manifest coverage, resolver coverage)… | MIT |
| [two-tier-extraction](two-tier-extraction/) | Tiered LLM extraction pattern for large corpus processing (email archives, document dumps, transcript libraries). A utility-tier model triages and classifies at speed… | MIT |
| [voice-note-ingest](voice-note-ingest/) | Ingest a voice note with exact-phrasing preservation (never paraphrased). Routes content to originals/, concepts/, people/, companies/, ideas/, personal/, or… | MIT |
| [voice-persona-mars](voice-persona-mars/) | Route to Mars (introspective thought partner / demo showman voice persona). Used when the operator wants depth, meaning, or impressive social demos rather than… | MIT |
| [voice-persona-venus](voice-persona-venus/) | Route to Venus (sharp executive-assistant voice persona). Used for logistics — calendar, tasks, recent messages, brain lookups — at sub-second phone-call latency. The… | MIT |
| [voice-post-call](voice-post-call/) | Post-call handling for a voice session — turn the transcript into a brain page, post the summary to the operator's messaging surface, archive the audio. The pipeline is… | MIT |
| [webhook-transforms](webhook-transforms/) | Generic framework for converting external events (SMS, meetings, social mentions) into brain-ingestible signals. Define a transform function, register a webhook URL, and… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/research-and-scraping/gbrain/academic-verify -g -a claude-code
```

Back to [Research and scraping](../../../catalog/research-and-scraping.md)
