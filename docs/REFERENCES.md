# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, direct-document reading, commit-only git workflow references, placeholder-token preservation, and shared workflow/tool constraints.

## Shared Capability Surface

- `docs/REQUIREMENTS.md`: Defines the capability names `static-check`, `find`, `files-find`, and `references-generation`, constrains final commit-generation instructions, and forbids `docs-check`, `git-status`, and worktree lifecycle references in prompt artifacts.
- `docs/WORKFLOW.md`: Describes prompt execution in capability-level terms for direct-document reading, commit-only git usage, placeholder-token preservation, and template-guideline path resolution through `%%TEMPLATE_PATH%%`.

## Updated Prompt Artifacts

- `src/prompts/analyze.md` and `src/prompts/check.md`: Remove dedicated `docs-check` gates and rely on direct reads of canonical docs.
- `src/prompts/change.md`, `src/prompts/cover.md`, `src/prompts/fix.md`, `src/prompts/implement.md`, `src/prompts/new.md`, and `src/prompts/refactor.md`: Remove standalone git-status, docs-check, worktree, and merge-management steps while keeping final commit-generation instructions.
- `src/prompts/flowchart.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, and `src/prompts/workflow.md`: Remove worktree-isolation and merge-management instructions and retain only direct final commit generation.

## References Generation Note

- Repository evidence indicates that automated references generation remains limited for this prompt-first repository; `docs/REFERENCES.md` is therefore maintained manually to preserve navigational utility for downstream LLM Agents.
