# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, prompt inventory, shared capability-level operational instructions, and no-source `static-check` success handling.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the migrated capability names `docs-check`, `git-status`, `static-check`, `find`, `files-find`, `base-path`, `git-path`, `worktree-name`, `worktree-create`, `worktree-delete`, and `references-generation`.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for analysis, worktree lifecycle, repository cleanliness checks, references generation, and verification.

## Updated Prompt Artifacts

- `src/prompts/analyze.md`, `src/prompts/check.md`: Read-only analysis prompts that now describe `docs-check`, `find`, `files-find`, and `static-check` capabilities without CLI transport literals for migrated operations.
- `src/prompts/change.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/implement.md`, `src/prompts/new.md`, `src/prompts/refactor.md`: Change and implementation prompts that now describe capability-level repository checks, worktree lifecycle, static analysis, construct extraction, and references generation while preserving workflow order and terminal strings.
- `src/prompts/flowchart.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, `src/prompts/workflow.md`: Maintenance prompts that now describe capability-level repository checks and worktree lifecycle operations instead of `req --...` transport literals.

## Repository Documentation Update

- `README.md`: Installation and usage guidance now refers to capability-level worktree and repository-cleanliness flow instead of `req --git-check` transport wording.

## References Generation Note

- Repository evidence indicates that `req --here --references` currently returns `Error: no source files found in configured directories.` for this prompt-only repository; `docs/REFERENCES.md` is therefore maintained manually to reflect the updated prompt surface.
