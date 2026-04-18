# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, prompt inventory, shared capability-level operational instructions, no-source `static-check` success handling, and structured-discovery preference for `find`/`files-find` over supplementary `rg`/`git grep` use.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the migrated capability names `docs-check`, `git-status`, `static-check`, `find`, `files-find`, `base-path`, `git-path`, `worktree-name`, `worktree-create`, `worktree-delete`, and `references-generation`, and requires post-WORKFLOW/REFERENCES discovery to prefer `find`/`files-find` while limiting `rg`/`git grep` to supplementary, fallback, or confirmation use.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for analysis, structured construct discovery preference, worktree lifecycle, repository cleanliness checks, references generation, and verification.

## Updated Prompt Artifacts

- `src/prompts/analyze.md`, `src/prompts/check.md`, `src/prompts/change.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/new.md`, and `src/prompts/refactor.md`: Toolkit and verification instructions now prefer `find`/`files-find` for named-symbol, declaration, construct, and known-file discovery, while reserving `rg`/`git grep` for supplementary free-text/body-content search, unexpressible fallback cases, or confirmation inside already targeted files.
- `src/prompts/flowchart.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, and `src/prompts/workflow.md`: Toolkit instructions now prefer `find`/`files-find` for structured discovery and reserve `rg`/`git grep` for supplementary, fallback, or confirmation use.
- `src/prompts/implement.md`: Verification guidance now applies the same `find`/`files-find` preference for requirement-evidence discovery even without a local toolkit section.

## References Generation Note

- Repository evidence indicates that `req --here --references` currently returns `Error: no source files found in configured directories.` for this prompt-only repository; `docs/REFERENCES.md` is therefore maintained manually to reflect the updated prompt surface.
