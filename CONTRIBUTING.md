# Contributing

## Suggest a skill

[Open an issue](../../issues/new) with a link to the skill (a GitHub repo or folder with a `SKILL.md`) and a
line on what it's good for. We check its licence, scan it, and add it.

A skill gets copied here when it meets all of these:

- Its licence is open source: MIT, Apache 2.0, BSD, ISC, the GPL family, MPL, CC0, CC BY or CC BY-SA.
- Its folder is under 5 MB and holds no compiled programs.
- Nothing in it looks like a key, a token or someone's personal details.

Any other skill is listed in the catalog with a link to its own repo.

## Change or remove a skill

Did you write a skill that's here? Open an issue to have it updated, credited differently or taken down, and
we'll act on it.

## How the hub is updated

SOYL keeps an archive of skill projects: one git clone per project, sorted into category folders
(`<category>/<project>`). [`tools/hub.py`](tools/hub.py) builds this repo from that archive and never changes
the archive. You need Python 3.9 or newer and git. The GitHub CLI (`gh`) is optional and adds descriptions and
stars.

First, tell the tool where the archive is, in `hub.local.json` (this file is never committed):

```json
{ "archive": "/path/to/the/archive", "private_words": ["anything that must never be published"] }
```

**Add a new skill** after you've cloned its project into the archive and scanned it:

```bash
python -I tools/hub.py sync --only <category>/<project>
```

The output shows what will be copied in, what will only be linked and why, and anything the key and privacy
check held back. Look over `git status`, then run the same command with `--push` to commit and publish it.

| Task | Command |
|---|---|
| Sync the whole archive again (after updating copies) | `python -I tools/hub.py sync --push` |
| Rebuild the catalog pages only | `python -I tools/hub.py catalog` |
| Scan everything for keys and private details | `python -I tools/hub.py check` |

The tool can't make every decision on its own. A person records the rest in `tools/`:

- [`licence-overrides.json`](tools/licence-overrides.json): cases where the automatic licence check is wrong or
  unsure, each with a note saying why.
- [`exclude.txt`](tools/exclude.txt): projects or skills to leave out completely.
- [`check-allow.txt`](tools/check-allow.txt): findings from the key and privacy check that turned out to be
  harmless.

`skills/`, `catalog/` and `CATALOG.md` are generated, so to change them, change the archive or the tools, not
the output. Never commit `hub.local.json`, keys, tokens or private files.
