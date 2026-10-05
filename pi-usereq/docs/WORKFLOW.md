# PI-Prompts Workflow

## Execution Units Index
- ID: `PROC:main`
  - Type: Process
  - Role: External prompt-host runtime loads bundled Markdown resources from `src/prompts`, `src/templates`, and `src/instructions`; standalone prompt/template documents start with level-1 titles and omit YAML front matter; every bundled prompt under `src/prompts` ends with a `## Context Files` section whose `%%CONTEXT_FILES%%` token is expanded by the runtime to inject pre-loaded context files.
  - Entrypoints:
    - no internal executable entrypoints detected under `src`
  - Parent Process: none
  - Threads: no explicit threads detected

## Execution Units
### `PROC:main`
- Entrypoints:
  - none under `src`
- Lifecycle/trigger:
  - Start trigger: external prompt-host runtime selects one bundled Markdown asset from `src/prompts`, `src/templates`, or `src/instructions` and reads its leading Markdown title line or instruction body.
  - Stop trigger: external prompt-host runtime finishes reading or rendering the selected asset.
  - Looping model: one-shot resource load per prompt or document request.
  - Threads: no explicit threads detected.
- Internal Call-Trace Tree:
  - none; `src/` contains static Markdown resources only and declares no internal executable functions.
- External Boundaries:
  - External prompt-host runtime resolves repository files, reads standalone prompt/template title lines plus instruction snippets, expands placeholders (including `%%CONTEXT_FILES%%`), and delivers rendered prompt text.
  - Git and repository tooling execute outside `src` after the rendered prompt is consumed.

## Communication Edges
- none detected between internal execution units under `src`; prompt selection, rendering, and delivery occur through external boundaries only.
