# soundbox

Skills from [HamSanders/soundbox](https://github.com/HamSanders/soundbox) at commit [`085e0ec`](https://github.com/HamSanders/soundbox/tree/085e0ecef754734e8bc62d6126e51638872c14c6), copied into SOYL Hub on 2026-11-01. Licence: MIT.

> Free, open-source, local alternative to ElevenLabs and Suno. AI sound effects, music with lyrics, text-to-speech and voice cloning on your own GPU (Stable Audio, ACE-Step and more). No account, no credits, offline. Windows/macOS app, HTTP API and a 21-tool MCP server for Claude Code and Cursor.

All credit goes to the authors of HamSanders/soundbox. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [soundbox-sfx](soundbox-sfx/) | Generate sound effects, foley and ambience locally through the Soundbox MCP server (soundbox.generate / list_sounds / list_models). Use whenever the user wants a sound… | MIT |
| [soundbox-sound-pass](soundbox-sound-pass/) | Do a full "sound pass" on a project — read the code/design of a game, app, video or prototype, derive the list of sound events it needs, generate every one through the… | MIT |
| [soundbox-voice-story](soundbox-voice-story/) | Write, voice and arrange spoken audio locally through the Soundbox MCP server — one-off narration with soundbox.speak, or a persistent multi-track "story" (create_story… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/sound-effects/soundbox/soundbox-sfx -g -a claude-code
```

Back to [Sound](../../../catalog/sound-effects.md)
