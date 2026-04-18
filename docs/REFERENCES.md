# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, placeholder-token preservation, `%%TEMPLATE_PATH%%` usage for template-guideline references, and shared workflow/tool constraints.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the capability names `docs-check`, `git-status`, `static-check`, `find`, `files-find`, `base-path`, `git-path`, `worktree-name`, `worktree-create`, `worktree-delete`, and `references-generation`, and constrains placeholder-token handling across prompt artifacts.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for analysis, worktree lifecycle, repository cleanliness checks, placeholder-token preservation, and template-guideline path resolution through `%%TEMPLATE_PATH%%`.

## Updated Prompt Artifacts

- `src/prompts/change.md`, `src/prompts/check.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/implement.md`, `src/prompts/new.md`, and `src/prompts/refactor.md`: Doxygen and test-guideline references now resolve through `%%TEMPLATE_PATH%%` instead of literal `.req/docs/...` paths.
- `src/prompts/create.md`, `src/prompts/recreate.md`, and `src/prompts/write.md`: Requirements-template references now resolve through `%%TEMPLATE_PATH%%/Requirements_Template.md`.

## References Generation Note

- Repository evidence indicates that `req --here --references` currently returns `Error: no source files found in configured directories.` for this prompt-only repository; `docs/REFERENCES.md` is therefore maintained manually to preserve navigational utility for downstream LLM Agents.
