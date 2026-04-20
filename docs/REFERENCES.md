# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, placeholder-token preservation, `%%TEMPLATE_PATH%%` usage for template-guideline references, and shared workflow/tool constraints.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the capability names `git-status`, `static-check`, `find`, `files-find`, and `references-generation`, and constrains placeholder-token handling plus the removal of standalone docs-check and worktree-management prompt steps.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for analysis, direct-in-repository commit flow, repository cleanliness checks, placeholder-token preservation, and template-guideline path resolution through `%%TEMPLATE_PATH%%`.

## Updated Prompt Artifacts

- `src/prompts/analyze.md` and `src/prompts/check.md`: workflows now start directly with analysis or static-check execution and omit standalone docs-presence entry steps.
- `src/prompts/change.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/implement.md`, `src/prompts/new.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/refactor.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, `src/prompts/workflow.md`, and `src/prompts/flowchart.md`: workflows now operate directly in the active repository directory, omit worktree lifecycle and merge-management steps, and keep only final commit plus final repository-cleanliness verification.

## References Generation Note

- Repository evidence indicates that `req --here --references` currently returns `Error: no source files found in configured directories.` for this prompt-only repository; `docs/REFERENCES.md` is therefore maintained manually to preserve navigational utility for downstream LLM Agents.
