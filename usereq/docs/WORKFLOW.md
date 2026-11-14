# PI-Prompts Workflow

## Execution Units Index
- ID: `PROC:main`
  - Type: Process
  - Role: External prompt-host runtime loads bundled Markdown resources from `src/prompts`, `src/templates`, and `src/instructions`; standalone prompt/template documents start with level-1 titles and omit YAML front matter; every bundled prompt under `src/prompts` ends with a `## Context Files` section whose single `%%CONTEXT_FILES%%` token occurrence is expanded by the runtime to inject pre-loaded context files; the token appears exactly once per prompt and only inside that terminal section; the eight prompts `analyze`, `change`, `cover`, `fix`, `new`, `readme`, `refactor`, and `write` carry one byte-identical `CRITICAL` bullet inside their `## Absolute Rules, Non-Negotiable` section that binds the final response language to the `User's Request` language; every bundled prompt specifies a human-readable `## **Summary**` in one `~~~RESULT_SUMMARY` fenced block, limited to 1010 Unicode characters encoded as UTF-8; two byte-identical present-results bullets govern `## **Next Workflow**` and the terminal status line: the first places a human-readable description before one `~~~NEXT_WORKFLOW` fenced block containing only mandated commands separated by blank lines, or an empty block when none are mandated; the second emits `STATUS_OK` or `STATUS_ERROR` as the terminal status line after that section with no content after it; early error and no-change terminations emit `STATUS_ERROR` after any required diagnostic, including commit-workflow failures.
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
  - The response-language bullet constrains only final response text language, which mirrors the `User's Request` expression language while report-schema literals, exact strings, status lines, commands, and identifiers stay byte-identical; written repository artifacts remain English-only.
  - Git and repository tooling execute outside `src` after the rendered prompt is consumed.

## Communication Edges
- none detected between internal execution units under `src`; prompt selection, rendering, and delivery occur through external boundaries only.
