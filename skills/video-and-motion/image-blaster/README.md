# image-blaster

Skills from [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) at commit [`4acb43b`](https://github.com/neilsonnn/image-blaster/tree/4acb43ba126a12358f71838d1b1a05e856b10eaf), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> An image-to-world skillset for Claude.

All credit goes to the authors of neilsonnn/image-blaster. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [image-blast-3d](image-blast-3d/) | Generate one specified atomic 3D object. Use when the user names exactly one object instance to make, or provides one image plus the object name/description. | MIT |
| [image-blast-image-edit](image-blast-image-edit/) | Generate one image edit from explicit input images and a prompt. Use for source cleanup, clean plates, object removal, or other FAL-backed image edits. | MIT |
| [image-blast-plate](image-blast-plate/) | Generate one clean plate/source cleanup image for an IMAGE-BLASTER world. Use after confirmed objects exist, when removing foreground objects or other specified content… | MIT |
| [image-blast-project](image-blast-project/) | Create, inspect, and manage an IMAGE-BLAST project envelope under worlds/&lt;slug>. Use before other image-blast skills (image-blast-uncover, image-blast-world… | MIT |
| [image-blast-sfx](image-blast-sfx/) | Generate and post-process a clean sound effect, object impact, or ambient loop. | MIT |
| [image-blast-uncover](image-blast-uncover/) | Main image analysis skill, object generation, plate decisionmaking, and initial scene description. Use this skill when user wants to create objects and necessary for… | MIT |
| [image-blast-wildcard](image-blast-wildcard/) | Discover and run any FAL API model or operation the user requests. Use this as a generic FAL escape hatch when the user wants to generate something that does not fit a… | MIT |
| [image-blast-world](image-blast-world/) | Generate the 3D static environment of a world from a source or plate image. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/image-blaster/image-blast-3d -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
