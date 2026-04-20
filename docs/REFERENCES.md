# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, placeholder-token preservation, `%%TEMPLATE_PATH%%` usage for template-guideline references, shared workflow/tool constraints, and commit-step externalization through `%%COMMIT%%%` plus `src/istructions/commit.md`.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the capability names `git-status`, `static-check`, `find`, `files-find`, and `references-generation`, constrains placeholder-token handling, and requires commit-bearing prompts to replace inline stage-and-commit text with `%%COMMIT%%%`.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for analysis, direct-in-repository commit flow, repository cleanliness checks, placeholder-token preservation, shared commit-instruction delegation to `src/istructions/commit.md`, and template-guideline path resolution through `%%TEMPLATE_PATH%%`.

## Updated Prompt Artifacts

- `src/prompts/analyze.md` and `src/prompts/check.md`: workflows still start directly with analysis or static-check execution and omit standalone docs-presence entry steps.
- `src/prompts/change.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/implement.md`, `src/prompts/new.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/refactor.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, `src/prompts/workflow.md`, and `src/prompts/flowchart.md`: workflows now replace the inline stage-and-commit step body with the literal token `%%COMMIT%%%` while preserving step numbering and surrounding prompt text.

## Shared Instruction Artifact

- `src/istructions/commit.md`: Canonical shared stage-and-commit instruction referenced by commit-bearing prompts through `%%COMMIT%%%`.

## References Generation Note

- Repository evidence indicates that `req --here --references` currently returns `Error: no source files found in configured directories.` for this prompt-only repository; `docs/REFERENCES.md` is therefore maintained manually to preserve navigational utility for downstream LLM Agents.
