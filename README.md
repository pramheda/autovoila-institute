# Voilà Institute

A GitHub-ready, prompt-native autonomous research institute.

The core idea is simple:

> Give a capable coding/research agent a scientific charter, institutional
> taste, adaptive hiring policy, a polymath programme, a navigable workspace,
> and permission to create independent branches. Keep the human able to
> inspect and steer everything.

The canonical output is the full research world, not a paper.

## Quick start

1. Clone or open this repository.

2. Validate and initialise the workspace.

```bash
python3 tools/vi.py doctor
python3 tools/vi.py init
```

3. Open the directory in your coding agent and give it exactly this prompt:

```text
Read voila.md and get started.
```

That is the intended entry point for Claude Code, Codex, Copilot coding agent,
or another capable filesystem-and-shell agent.

The agent will establish or load a charter, inspect the repository and
machine, then ask you a compact set of unresolved setup questions.

## Important files

| File | Purpose |
|---|---|
| `voila.md` | Executable operating prompt for a coding agent |
| `institute.md` | Institutional taste and director behaviour |
| `charter.md` | Generated current scientific mission, once established |
| `research-taste.md` | How to select important, rigorous, feasible work |
| `adaptive-hiring.md` | Living policy for choosing models and agents |
| `polymath.md` | Cross-domain, non-theatrical polymath programme |
| `human-plane.md` | Human control and attention rules |
| `research-world.md` | Paper-independent scientific representation |
| `confirmation.md` | Frozen confirmation discipline |
| `workspace/` | Mutable research world |

## Minimal helper

`tools/vi.py` is deliberately small. It creates and inspects branch
directories, appends attention requests, and validates repository state.

It does not try to be an agent framework.

Examples:

```bash
python3 tools/vi.py tree

python3 tools/vi.py new-branch \
  initial-landscape \
  --mission-file templates/branch-mission.md

python3 tools/vi.py attention decision \
  "Choose the primary direction" \
  --source workspace/branches/initial-landscape
```

## AutoVoila research philosophy

AutoVoila's current repository uses `voila.md` as its main prompt and
`research-philosophy.md` as the research-taste document. This repository keeps
its own `research-taste.md`, adapted to an institute whose canonical output is
a navigable research world rather than a paper.

## Design rule

Do not add infrastructure merely because autonomous research sounds like a
platform problem.

Use the file-and-process version until a concrete failure demonstrates the
need for more machinery.
