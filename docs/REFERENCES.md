# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, placeholder-token preservation including `%%PROMPT%%`, `%%TEMPLATE_PATH%%` usage for template-guideline references, shared workflow/tool constraints, commit-step externalization through `%%COMMIT%%` plus `src/instructions/git_commit.md`, and the canonical read-only git restriction in `src/instructions/git_read-only.md`.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the capability names `git-status`, `static-check`, `find`, `files-find`, and `references-generation`, constrains placeholder-token handling, and requires commit-bearing prompts to replace inline stage-and-commit text with `%%COMMIT%%` while reserving `%%PROMPT%%` for commit-message `<TYPE>` substitution.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for analysis, direct-in-repository commit flow, repository cleanliness checks, placeholder-token preservation, shared commit-instruction delegation to `src/instructions/git_commit.md`, read-only git restriction reuse from `src/instructions/git_read-only.md`, commit-message `<TYPE>` substitution through `%%PROMPT%%`, and template-guideline path resolution through `%%TEMPLATE_PATH%%`.

## Updated Prompt Artifacts

- `src/prompts/analyze.md` and `src/prompts/check.md`: workflows still start directly with analysis or static-check execution, omit standalone docs-presence entry steps, and preserve the canonical read-only git restriction that forbids repository-state mutation; `analyze.md` now exposes `Present results` as explicit Step 2.
- `src/prompts/change.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/implement.md`, `src/prompts/new.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/refactor.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, `src/prompts/workflow.md`, and `src/prompts/flowchart.md`: workflows now replace the inline stage-and-commit step body with the literal token `%%COMMIT%%` while preserving step numbering and surrounding prompt text.
- `src/prompts/create.md` and `src/prompts/write.md`: workflows now insert the literal token `%%COMMIT%%` as the penultimate numbered step before `Present results`.

## Shared Instruction Artifact

- `src/instructions/git_commit.md`: Canonical shared stage-and-commit instruction referenced by commit-bearing prompts through `%%COMMIT%%` and parameterized with `%%PROMPT%%` for commit-message `<TYPE>`.
- `src/instructions/git_read-only.md`: Canonical git read-only restriction for prompts that audit or analyze repository evidence without mutating repository state.

## References Generation Note

- Repository evidence indicates that `req --here --references` currently returns `Error: no source files found in configured directories.` for this prompt-only repository; `docs/REFERENCES.md` is therefore maintained manually to preserve navigational utility for downstream LLM Agents.
