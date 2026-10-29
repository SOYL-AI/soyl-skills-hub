# Ghost

Skills from [TryGhost/Ghost](https://github.com/TryGhost/Ghost) at commit [`5677193`](https://github.com/TryGhost/Ghost/tree/56771938ea0e6304555e1c2360875093dd62ba66), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Independent technology for modern publishing, memberships, subscriptions and newsletters.

All credit goes to the authors of TryGhost/Ghost. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [Add Admin API Endpoint](add-admin-api-endpoint/) | Add a new endpoint or endpoints to Ghost's Admin API at `ghost/api/admin/**`. | MIT |
| [add-private-feature-flag](add-private-feature-flag/) | Use when adding a new private (developer experiments) feature flag to Ghost, including the backend registration and settings UI toggle. | MIT |
| [admin7-feature-flags](admin7-feature-flags/) | Add, consume, review, or remove Admin 7 milestone flags using Ghost's existing Labs conventions. | MIT |
| [commit](commit/) | Commit message formatting and guidelines | MIT |
| [convert-internal-package-to-typescript](convert-internal-package-to-typescript/) | Convert a legacy internal Ghost workspace package from JavaScript or CommonJS to the repository's TypeScript and ESM golden path while preserving file history and… | MIT |
| [Create database migration](create-database-migration/) | Create a database migration to add a table, add columns to an existing table, add a setting, or otherwise change the schema of Ghost's MySQL database. Use this skill… | MIT |
| [Format numbers](format-numbers/) | Format numbers using the formatNumber function from Shade whenever someone edits a TSX file. | MIT |
| [migrate-internal-package](migrate-internal-package/) | Move a package from another TryGhost repository into Ghost as an internal-only workspace package while preserving its Git history. Use for package migrations from… | MIT |
| [migrate-service](migrate-service/) | Migrate one existing Ghost Core service to the boot-owned defineService pattern. Use when asked to migrate or prepare an individual service, including its dependency… | MIT |
| [Shade component decision](shade-component-decision/) | Decide which Shade layer (Token, Primitive, Component, Recipe, Pattern) a new piece of UI belongs in — and whether it should be added to Shade at all. Trigger when… | MIT |
| [Shade dropdown surface contract](shade-dropdown-surface-contract/) | DropdownMenu, Select, and Popover share one visual recipe (bg-surface-elevated-2 + border-border/60 dark:border-border/30 + shadow-md). Change them together. Trigger… | MIT |
| [Shade imports](shade-imports/) | Import Shade from layer-specific subpaths (primitives, components, patterns, page-templates, utils), never the root barrel. Trigger when editing TSX/TS in… | MIT |
| [Shade inputSurface recipe](shade-inputsurface-recipe/) | Use the inputSurface() recipe for form-control chrome (border, background, radius, focus ring, invalid state) — don't roll your own. Trigger when editing… | MIT |
| [Shade new component](shade-new-component/) | Acceptance checklist for adding or editing a Shade component or pattern file — naming, sibling story, className forwarding, cva variants, required states, recipe usage… | MIT |
| [Shade no dark variants](shade-no-dark-variants/) | Don't write dark: Tailwind variants for colour in Shade or admin apps — semantic tokens flip in dark mode automatically. Trigger when editing TSX in Shade-consuming apps. | MIT |
| [Shade page header](shade-page-header/) | Construct or revise Admin page headers and header controls using the shared PageHeader contract. Use when adding a header, changing its actions, or reviewing ordering… | MIT |
| [Shade page templates](shade-page-templates/) | Pick the right Shade page template (ListPage, PageHeader) for a new admin page instead of inventing chrome. Trigger when creating new admin pages or routes in apps/admin… | MIT |
| [Shade ShadCN install](shade-shadcn-install/) | Guardrails for running `pnpm dlx shadcn@latest add` in Shade — never overwrite existing components, fresh branch first, swap raw colours for semantic tokens after… | MIT |
| [Shade tokens, not hex](shade-tokens-not-hex/) | Use Shade semantic tokens (bg-background, text-foreground, border-border-default, bg-surface-elevated) — never hex, hsl(), or bg-gray-200-style raw palette utilities for… | MIT |
| [Shade use primitives](shade-use-primitives/) | Replace bare divs that only carry flex/grid/gap utilities with Shade primitives (Stack, Inline, Box, Grid, Container, Text). Use semantic gap="md" instead of gap-4… | MIT |
| [tinybird](tinybird/) | Tinybird file formats, SQL rules, optimization patterns, and best practices for datasources, pipes, endpoints, and materialized views. | MIT |
| [tinybird-cli-guidelines](tinybird-cli-guidelines/) | Tinybird CLI commands, workflows, and operations. Use when running tb commands, managing local development, deploying, or working with data operations. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/Ghost/add-admin-api-endpoint -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
