# claude-watch

Skills from [taoufik123-collab/claude-watch](https://github.com/taoufik123-collab/claude-watch) at commit [`7711231`](https://github.com/taoufik123-collab/claude-watch/tree/7711231e4c47e5d4e06bcf5326c4abf5b70ab4a9), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Give Claude the ability to watch any video — scene-change frames + transcript + a structured report, with a 0-10s hook microscope and optional Obsidian auto-save.

All credit goes to the authors of taoufik123-collab/claude-watch. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [watch](watch/) | Watch a video (URL or local path) like an editor. Extracts scene-change frames, pacing metrics (cuts/min, shot length), and a dense 0-10s hook microscope; pulls… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/claude-watch/watch -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
