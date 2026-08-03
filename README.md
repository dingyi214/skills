# skills

Dingyi's agent skills. Install with the [skills CLI](https://skills.sh) — no manual copy.

## Install

```bash
# list skills in this repo
npx skills add dingyi214/skills --list

# install one skill (global, all detected agents)
npx skills add dingyi214/skills --skill excalidraw-marker -g

# install into the current project only
npx skills add dingyi214/skills --skill excalidraw-marker

# install everything in the repo
npx skills add dingyi214/skills --skill '*' -g
```

Equivalent short forms:

```bash
npx skills add dingyi214/skills -s excalidraw-marker -g
npx skills add dingyi214/skills@excalidraw-marker -g
```

## Available skills

| Skill | What it does |
|---|---|
| [`excalidraw-marker`](excalidraw-marker/) | Marker look + compose-from-atoms for Excalidraw diagrams |

## Repo layout

Each skill is a top-level folder with a `SKILL.md` (Agent Skills format). The CLI discovers those folders automatically — that is what makes `npx skills add dingyi214/skills --skill …` work.

## Requirements

- Node.js 18+
- Public GitHub repo (or GitHub auth that can clone it)
- An agent that loads skills (`~/.agents/skills`, `.agents/skills`, Cursor, Claude Code, …)
