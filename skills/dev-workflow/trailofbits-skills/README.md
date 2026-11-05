# trailofbits-skills

Skills from [trailofbits/skills](https://github.com/trailofbits/skills) at commit [`470419e`](https://github.com/trailofbits/skills/tree/470419e16f97e112d01fc32f4898aea1755015d9), copied into SOYL Hub on 2026-11-05. Licence: CC0-1.0.

> Trail of Bits skills for security research, vulnerability detection, and audit workflows

All credit goes to the authors of trailofbits/skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [address-sanitizer](address-sanitizer/) | Builds and runs code under AddressSanitizer to catch buffer overflows, use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=address builds… | CC0-1.0 |
| [adjudicate-regression](adjudicate-regression/) | Use when deciding whether source and live reproduction evidence establish a new regression or an exclusion. | CC0-1.0 |
| [aflpp](aflpp/) | Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary… | CC0-1.0 |
| [agentic-actions-auditor](agentic-actions-auditor/) | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference… | CC0-1.0 |
| [algorand-vulnerability-scanner](algorand-vulnerability-scanner/) | Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control… | CC0-1.0 |
| [atheris](atheris/) | Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and… | CC0-1.0 |
| [audit-augmentation](audit-augmentation/) | Augments Trailmark code graphs with external audit findings from SARIF static analysis results, weAudit annotation files, and version-gated Trailmark 0.4.x… | CC0-1.0 |
| [audit-context-building](audit-context-building/) | Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit… | CC0-1.0 |
| [audit-prep-assistant](audit-prep-assistant/) | Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code… | CC0-1.0 |
| [burpsuite-project-parser](burpsuite-project-parser/) | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security… | CC0-1.0 |
| [c-review](c-review/) | Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native… | CC0-1.0 |
| [cairo-vulnerability-scanner](cairo-vulnerability-scanner/) | Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and… | CC0-1.0 |
| [cargo-fuzz](cargo-fuzz/) | Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses… | CC0-1.0 |
| [chrome-mcp-troubleshooting](chrome-mcp-troubleshooting/) | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave… | CC0-1.0 |
| [code-improver](code-improver/) | Runs an autonomous review-and-fix improvement loop over any code target — a skill, plugin, module, or directory — using a reviewer the user names: any installed skill or… | CC0-1.0 |
| [code-maturity-assessor](code-maturity-assessor/) | Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity… | CC0-1.0 |
| [codeql](codeql/) | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build… | CC0-1.0 |
| [constant-time-analysis](constant-time-analysis/) | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent… | CC0-1.0 |
| [constant-time-testing](constant-time-testing/) | Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing… | CC0-1.0 |
| [cosmos-vulnerability-scanner](cosmos-vulnerability-scanner/) | Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM +… | CC0-1.0 |
| [coverage-analysis](coverage-analysis/) | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. Covers baselining a new campaign, reading… | CC0-1.0 |
| [crypto-protocol-diagram](crypto-protocol-diagram/) | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid… | CC0-1.0 |
| [devcontainer-setup](devcontainer-setup/) | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project… | CC0-1.0 |
| [diagramming-code](diagramming-code/) | Generates Mermaid diagrams from Trailmark code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and… | CC0-1.0 |
| [differential-review](differential-review/) | Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting… | CC0-1.0 |
| [dimensional-analysis](dimensional-analysis/) | Audits code for unit and decimal-scaling bugs and annotates it with dimensional comments recording the units of each value. Use when someone asks to audit or review code… | CC0-1.0 |
| [dwarf-expert](dwarf-expert/) | Analyzes DWARF debug information in compiled binaries. Use when inspecting .debug_* sections, DIE trees, or DW_TAG_/DW_AT_ entries with dwarfdump/llvm-dwarfdump or… | CC0-1.0 |
| [entry-point-analyzer](entry-point-analyzer/) | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes… | CC0-1.0 |
| [firebase-apk-scanner](firebase-apk-scanner/) | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when… | CC0-1.0 |
| [fp-check](fp-check/) | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use… | CC0-1.0 |
| [fuzzing-dictionary](fuzzing-dictionary/) | Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers… | CC0-1.0 |
| [fuzzing-obstacles](fuzzing-obstacles/) | Patches past the barriers that stop a fuzzer making progress — checksum and hash verification, magic-value validation, time-based seeds, and other non-deterministic… | CC0-1.0 |
| [genotoxic](genotoxic/) | Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements… | CC0-1.0 |
| [gh-cli](gh-cli/) | Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or… | CC0-1.0 |
| [github-triage](github-triage/) | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs — incrementally merging passing automated/bot PRs and… | CC0-1.0 |
| [goal-prompt](goal-prompt/) | Drafts copy-paste-ready /goal commands for goal mode in Claude Code and Codex. Use when the user asks to create, write, rewrite, improve, compress, clean up, or prepare… | CC0-1.0 |
| [graph-evolution](graph-evolution/) | Compares Trailmark code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack… | CC0-1.0 |
| [guidelines-advisor](guidelines-advisor/) | Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check… | CC0-1.0 |
| [harness-writing](harness-writing/) | Designs and improves fuzzing harnesses for C/C++ and Rust. Covers mapping raw bytes onto a target API, generating structured inputs, avoiding non-determinism and false… | CC0-1.0 |
| [hunt-regressions](hunt-regressions/) | Use when discovering possible regressions from a pinned change and its callers before reproduction. | CC0-1.0 |
| [implement-patch](implement-patch/) | Use when a confirmed local bug needs an invariant-level fix, variant search, tests, and one local commit. | CC0-1.0 |
| [interpreting-culture-index](interpreting-culture-index/) | Interprets Culture Index (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis… | CC0-1.0 |
| [let-fate-decide](let-fate-decide/) | Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide… | CC0-1.0 |
| [libafl](libafl/) | Builds custom fuzzers with LibAFL, the modular Rust fuzzing library. Covers composing observers, feedbacks, mutators, schedulers, and executors into a fuzzer for targets… | CC0-1.0 |
| [libfuzzer](libfuzzer/) | Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds… | CC0-1.0 |
| [mermaid-to-proverif](mermaid-to-proverif/) | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model… | CC0-1.0 |
| [modern-cpp](modern-cpp/) | Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces raw… | CC0-1.0 |
| [modern-python](modern-python/) | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. | CC0-1.0 |
| [mutation-testing](mutation-testing/) | Configures mewt or muton campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign… | CC0-1.0 |
| [open-sourcing](open-sourcing/) | This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source… | CC0-1.0 |
| [ossfuzz](ossfuzz/) | Enrolls a project in OSS-Fuzz, Google's free continuous fuzzing service for open source, and drives it locally. Covers project.yaml, Dockerfile and build.sh setup, the… | CC0-1.0 |
| [patching-bugs](patching-bugs/) | Use when a known bug or falsifiable bug hypothesis in a local codebase needs a patch commit and reviewable proof report. | CC0-1.0 |
| [post-patch-validation](post-patch-validation/) | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and… | CC0-1.0 |
| [pr-improver](pr-improver/) | Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the… | CC0-1.0 |
| [prepare-regression](prepare-regression/) | Use when pinning before/after sources and collecting PR or commit context for a regression investigation. | CC0-1.0 |
| [property-based-testing](property-based-testing/) | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests… | CC0-1.0 |
| [prove-patch](prove-patch/) | Use when a local security patch commit needs independent scoped and three-arm proof. | CC0-1.0 |
| [regression-hunt](regression-hunt/) | Use when investigating regressions in PRs or commits, coordinating a regression campaign, or resuming saved progress. | CC0-1.0 |
| [replay-regression](replay-regression/) | Use when independently verifying a supplied PoC against fresh live before/after deployments. | CC0-1.0 |
| [report-regressions](report-regressions/) | Use when assembling or refreshing an evidence-linked regression report from saved campaign decisions. | CC0-1.0 |
| [reproduce-bug](reproduce-bug/) | Use when a named runtime or compiler bug in a local repository needs independent reproduction. | CC0-1.0 |
| [reproduce-regression](reproduce-regression/) | Use when deploying before/after systems and building a live-system PoC for a regression candidate. | CC0-1.0 |
| [review-walkthrough](review-walkthrough/) | Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called. | CC0-1.0 |
| [rust-review](rust-review/) | Performs comprehensive Rust security review for safe/unsafe boundary issues, memory safety in unsafe blocks, concurrency hazards, panic-induced DoS, FFI safety, and… | CC0-1.0 |
| [ruzzy](ruzzy/) | Sets up and runs Ruzzy, Trail of Bits' coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and… | CC0-1.0 |
| [sarif-parsing](sarif-parsing/) | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate… | CC0-1.0 |
| [second-opinion](second-opinion/) | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second… | CC0-1.0 |
| [secure-workflow-guide](secure-workflow-guide/) | Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration)… | CC0-1.0 |
| [semgrep](semgrep/) | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through… | CC0-1.0 |
| [semgrep-rule-creator](semgrep-rule-creator/) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis… | CC0-1.0 |
| [semgrep-rule-variant-creator](semgrep-rule-variant-creator/) | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input… | CC0-1.0 |
| [sharp-edges](sharp-edges/) | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas… | CC0-1.0 |
| [skill-improver](skill-improver/) | Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes… | CC0-1.0 |
| [slicing-code-context](slicing-code-context/) | Selects bounded, graph-informed source slices with Trailmark and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading… | CC0-1.0 |
| [solana-vulnerability-scanner](solana-vulnerability-scanner/) | Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when… | CC0-1.0 |
| [spec-to-code-compliance](spec-to-code-compliance/) | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document… | CC0-1.0 |
| [substrate-vulnerability-scanner](substrate-vulnerability-scanner/) | Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing… | CC0-1.0 |
| [supply-chain-risk-auditor](supply-chain-risk-auditor/) | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams… | CC0-1.0 |
| [testing-handbook-generator](testing-handbook-generator/) | Generates Claude Code skills from the Trail of Bits Testing Handbook (appsec.guide), analyzing handbook pages and emitting SKILL.md files with the structure each skill… | CC0-1.0 |
| [token-integration-analyzer](token-integration-analyzer/) | Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for… | CC0-1.0 |
| [ton-vulnerability-scanner](ton-vulnerability-scanner/) | Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas… | CC0-1.0 |
| [trailmark](trailmark/) | Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege… | CC0-1.0 |
| [trailmark-finding-triage](trailmark-finding-triage/) | Performs graph-assisted triage of a single security finding, SARIF result, weAudit annotation, suspicious function, or report excerpt using Trailmark reachability… | CC0-1.0 |
| [trailmark-review-gate](trailmark-review-gate/) | Runs a Trailmark structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed… | CC0-1.0 |
| [trailmark-structural](trailmark-structural/) | Runs full Trailmark structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface… | CC0-1.0 |
| [trailmark-summary](trailmark-summary/) | Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick… | CC0-1.0 |
| [trailmark-variant-neighborhood](trailmark-variant-neighborhood/) | Expands one confirmed or suspected vulnerability into a Trailmark graph neighborhood of variant candidates by finding sibling functions, shared callers and callees… | CC0-1.0 |
| [validate-bug](validate-bug/) | Use when a bug PoC package needs an independent rerun and judgment before patching. | CC0-1.0 |
| [variant-analysis](variant-analysis/) | Hunts for the other instances of a bug already found — the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or bad pattern… | CC0-1.0 |
| [vector-forge](vector-forge/) | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates… | CC0-1.0 |
| [vulnerability-triage-brocards](vulnerability-triage-brocards/) | This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid"… | CC0-1.0 |
| [writing-lean-proofs](writing-lean-proofs/) | Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or… | CC0-1.0 |
| [wycheproof](wycheproof/) | Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more… | CC0-1.0 |
| [yara-rule-authoring](yara-rule-authoring/) | Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conventions… | CC0-1.0 |
| [zeroize-audit](zeroize-audit/) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow… | CC0-1.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/trailofbits-skills/address-sanitizer -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
