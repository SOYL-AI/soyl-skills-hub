# SOYL Hub

**Every open-source Claude skill we can find, in one place.** A skill teaches Claude how to do one job well:
script a reel, build a landing page, research a market, edit a video. New ones come out every day. SOYL Academy
collects them, checks each licence, and keeps them here so anyone can find one and start using it.

<!-- stats -->**1,799 skills** you can install from here, **932 more** listed with a link to their source, from **110 projects**. Updated 2026-10-30.<!-- /stats -->

[Browse the catalog](CATALOG.md) · [Install a skill](#install-a-skill) · [Design language](design-language/) · [Add a skill](CONTRIBUTING.md)

## Find a skill

The [catalog](CATALOG.md) sorts every skill into a category, with one line on what each one does:

[Video and motion](catalog/video-and-motion.md) · [Design](catalog/design-skills.md) ·
[Web animation](catalog/web-animation.md) · [Creative coding](catalog/creative-coding.md) ·
[UI components](catalog/ui-components.md) · [Marketing and growth](catalog/marketing-and-growth.md) ·
[Research and scraping](catalog/research-and-scraping.md) · [Developer workflow](catalog/dev-workflow.md) ·
[AI platforms](catalog/ai-platforms.md) · [Learning](catalog/learning.md) · [Sound](catalog/sound-effects.md) ·
[Big collections](catalog/skill-collections.md) · [Awesome lists](catalog/awesome-lists.md)

To search, press Ctrl+F (⌘F on a Mac) on a category page, or use [catalog/skills.json](catalog/skills.json).
Skills marked ↗ are listed with a link to their own repo: install those from there.

## Install a skill

**Claude Code, with one command.** Open the skill's folder on GitHub, copy the address, and run:

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/design-skills/emilkowalski-skills/emil-design-eng -g -a claude-code
```

Swap in the address of the skill you want. `-g` installs it for all your projects; leave it out to add it to
the current project only. This uses the open-source [skills CLI](https://github.com/vercel-labs/skills) and
needs Node.js. The CLI counts installs anonymously; put `DISABLE_TELEMETRY=1` in front of the command to stop it.

**Claude Code, by hand.** Download the skill's folder and put it in `~/.claude/skills/<skill-name>/` (for every
project) or `.claude/skills/<skill-name>/` inside a project. It loads in your next session.

**Ask Claude.** In Claude Code, paste the folder's address and say "install this skill for me".

**claude.ai and the Claude desktop app.** Turn on code execution under Settings > Capabilities. Then zip the
skill's folder and upload it under Customize > Skills.

## Use a skill

You don't have to call a skill. Claude reads each installed skill's description and uses the skill when your
request matches it. You can also ask for one by name ("use the emil-design-eng skill to review this page"),
or type `/` and its name in Claude Code. Read a skill's `SKILL.md` before the first run: it says what the skill
needs. Some skills need Node.js, Python, ffmpeg or a sign-in.

## Licences and credit

Every skill keeps its licence and credit.

- A skill is copied here only when its licence is open source (MIT, Apache 2.0, BSD, ISC, the GPL family,
  MPL, CC0 or CC BY), its folder is under 5 MB, and it holds no compiled programs.
- Each project's folder has a README that names the source, the exact commit it came from and its licence.
  Each skill folder carries its licence file.
- Other skills are listed with a link to their own repo, so you can install them from there. That covers
  skills with no licence, non-commercial, proprietary or source-available licences, and folders over 5 MB.
- We change nothing inside a copied skill. We only leave out build caches and plugin manifests, and add the
  licence file when a folder doesn't have one.

Is your skill here and you want it changed or taken down? [Open an issue](../../issues) and we'll act on it.

## Stay safe

A skill is a set of instructions, and sometimes scripts that run on your computer. Before a skill goes in, we
scan it for leaked keys and private details, but we don't audit its code. Read a skill before you install it.
Take extra care with any skill that runs commands, signs in to your accounts or sends data elsewhere.

## SOYL Academy design language

The [design-language](design-language/) folder holds the design system behind SOYL Academy's website: calm,
Apple-like pages, one typeface, one colour for actions, and motion only where it explains something. It has
the rules, the CSS tokens and the core components. It is also a skill: install it, and Claude builds pages
in this style.

## How SOYL Hub grows

When we find a new skill, we save it to our archive, check its licence and scan it. Then one command copies
it here, updates the catalog and publishes it. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to suggest a
skill and how the update works.

## About

SOYL Hub is made by [SOYL Academy](https://www.soylai.com), part of SOYL AI. SOYL's own files (the catalog,
the tools and the design language) are under the [MIT licence](LICENSE). Each skill in `skills/` keeps its own
licence. The SOYL and SOYL Academy names and logos are not covered by either.
