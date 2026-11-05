# bug-hunter

Skills from [codexstar69/bug-hunter](https://github.com/codexstar69/bug-hunter) at commit [`b412f98`](https://github.com/codexstar69/bug-hunter/tree/b412f9885e3ec074625a88c862c3f5b6724ec3b4), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> Adversarial AI bug hunter with auto-fix skill for Claude Code, Cursor, Codex CLI, GitHub Copilot CLI, Kiro CLI, Opencode, Pi Coding Agent, and more. Multi-agent pipeline finds security vulnerabilities, logic errors, and runtime bugs — then fixes them autonomously on a safe branch.

All credit goes to the authors of codexstar69/bug-hunter. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [commit-security-scan](commit-security-scan/) | Scan code changes for security vulnerabilities using Bug Hunter-native artifacts and STRIDE context. Use whenever the user asks for PR security review, commit-diff… | MIT |
| [doc-lookup](doc-lookup/) | Unified documentation lookup for Bug Hunter agents. Uses Context Hub (chub) as primary source with Context7 API fallback. Provides verified library/framework… | MIT |
| [fixer](fixer/) | Surgical code fixer for Bug Hunter. Implements minimal, precise fixes for verified bugs. Uses doc-lookup (Context Hub + Context7) to verify correct API usage in patches… | MIT |
| [hunter](hunter/) | Behavioral code analysis for Bug Hunter. Finds logic, security, concurrency, and contract defects with traced runtime triggers and structured JSON evidence. | MIT |
| [recon](recon/) | Triage enrichment for Bug Hunter. Maps tech stack, trust, state, error, concurrency, and service boundaries without reclassifying triage's files or reporting bugs. | MIT |
| [referee](referee/) | Final arbiter for Bug Hunter. Independently verifies behavioral findings, resolves Skeptic challenges, and calibrates severity and confidence. | MIT |
| [security-review](security-review/) | Run a focused STRIDE-based security review using Bug Hunter-native artifacts. Use whenever the user asks for a full security audit, repository security review, weekly… | MIT |
| [skeptic](skeptic/) | Adversarial reviewer for Bug Hunter. Challenges each behavioral finding against actual code, checks defenses, and preserves unresolved cases for independent review. | MIT |
| [threat-model-generation](threat-model-generation/) | Generate or refresh a STRIDE-based threat model for the current repository using Bug Hunter-native artifacts. Use whenever the repository has no threat model yet, the… | MIT |
| [vulnerability-validation](vulnerability-validation/) | Validate security findings for exploitability, reachability, and real-world impact using Bug Hunter-native findings artifacts. Use after security scans, before patch… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/bug-hunter/commit-security-scan -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
