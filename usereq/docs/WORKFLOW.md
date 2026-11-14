# PI-Prompts Workflow

## Execution Units Index
- ID: `PROC:main`
  - Type: Process
  - Role: External prompt-host runtime loads bundled Markdown resources from `src/prompts`, `src/templates`, and `src/instructions`; standalone prompt/template documents start with level-1 titles and omit YAML front matter; every bundled prompt under `src/prompts` ends with a `## Context Files` section whose single `%%CONTEXT_FILES%%` token occurrence is expanded by the runtime to inject pre-loaded context files; the token appears exactly once per prompt and only inside that terminal section; the eight prompts `analyze`, `change`, `cover`, `fix`, `new`, `readme`, `refactor`, and `write` carry one byte-identical `CRITICAL` bullet inside their `## Absolute Rules, Non-Negotiable` section that binds the final response language to the `User's Request` language; every bundled prompt places its mandatory single-object JSON response contract in `## Absolute Rules, Non-Negotiable`, specifying common report fields and workflow-specific delta fields, a 1010-character summary, a result value, and an array containing only mandated next commands; early terminations and commit-workflow failures use the same JSON contract.
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
  - External prompt-host runtime resolves repository files, reads standalone prompt/template title lines plus instruction snippets, expands placeholders (including the single `%%CONTEXT_FILES%%` occurrence inside each bundled prompt's `## Context Files` section), and delivers rendered prompt text.
  - The response-language bullet constrains only final response text language, which mirrors the `User's Request` expression language while JSON keys, exact diagnostic strings, commands, and identifiers stay byte-identical; written repository artifacts remain English-only.
  - Git and repository tooling execute outside `src` after the rendered prompt is consumed.

## Communication Edges
- none detected between internal execution units under `src`; prompt selection, rendering, and delivery occur through external boundaries only.
