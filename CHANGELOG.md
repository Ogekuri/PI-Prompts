# Changelog

## [0.7.0](https://github.com/Ogekuri/PI-Prompts/compare/v0.6.0..v0.7.0) - 2026-10-05
### 🚜  Changes
- enforce exhaustive sentence-level README validation [useReq] *(readme)*
  - REQUIREMENTS.md v0.6.0: extend RDM-CTX-005; add RDM-STP-008/009/010.
  - src/prompts/readme.md: enumerate all README sections in document order.
  - Validate every sentence against implementation evidence with fixed
  - outcomes (CONFORMING/OUTDATED/UNSUPPORTED/NOT-ANALYZED-BY-DESIGN).
  - Completeness gate blocks commit until full validation coverage.
  - REFERENCES.md: readme.md purpose row updated; WORKFLOW.md not impacted.
- BREAKING CHANGE: rename src/docs to src/templates and adapt SRS [useReq] *(templates)*
  - Rename src/docs/ to src/templates/ preserving template contents (R100).
  - REQUIREMENTS.md v0.5.0: scope.paths, 1.5 rules, PRJ-002, 2.2 table, 3.1 tree.
  - tests: standalone-doc glob now src/templates/*.md (TST-047/TST-048 coverage kept).
  - WORKFLOW.md/REFERENCES.md: declaration paths updated to src/templates.
  - Pre-existing: unittest failures on REQUIREMENTS.md front matter (unrelated to rename);
  - references-generation cannot process .md-only sources (unsupported extension filter).

## [0.6.0](https://github.com/Ogekuri/PI-Prompts/compare/v0.5.0..v0.6.0) - 2026-10-02
### 🚜  Changes
- add /req-refactor branch to analysis follow-up dispatch [useReq] *(analyze)*
  - REQUIREMENTS.md: extend ANZ-STP-004 with the exact /req-refactor prompt
  - text trigger (source-code-only modifications keeping requirements
  - unchanged with improvement intent); restate ANZ-STP-005 as an
  - if-and-only-if printing rule per follow-up command.
  - analyze.md: add /req-refactor ELSE-IF branch to Step 2 classification
  - (after /req-change, before ELSE) and bind the print rule to the
  - identified trigger per command; workflow stays read-only.
  - REFERENCES.md: update analyze.md purpose row to include /req-refactor.
- add conditional follow-up prompt step to analyze [useReq] *(prompts)*
  - Requirements: split ANZ-STP-002 (analysis step) and add ANZ-STP-003..ANZ-STP-006
  - defining the follow-up-dispatch step between analysis and present-results.
  - analyze.md: new Step 2 generates the /req-fix prompt text when analysis finds
  - behavior conflicting with requirements, or the /req-change prompt text when
  - both source code and requirements need changes; the generated text is printed
  - only when source-code or requirements modifications are required, never
  - otherwise; former Present results step renumbered to Step 3.
  - REFERENCES.md: aligned analyze.md resource purpose line.
  - Note: 2 pre-existing unit-test failures on canonical-docs front matter exist
  - at HEAD and are unrelated to this change surface.

## [0.5.0](https://github.com/Ogekuri/PI-Prompts/compare/v0.4.0..v0.5.0) - 2026-07-09
### ⛰️  Features
- add Iteration and Context Economy compliance block to all prompts [useReq] *(prompts)*
  - Add new ICO-CTX-001..011 requirements in SRS section 3.19 covering iteration minimization and context economy
  - Insert byte-identical ## Iteration and Context Economy chapter between Professional Personas and Absolute Rules in all 15 src/prompts/*.md
  - Update REQ-021/REQ-024 exception lists and glossary prefix for the new mandatory compliance block
  - Bump SRS version to 0.4.0

### 🐛  Bug Fixes
- Formatting fix.
- correct stale step cross-refs and inline canonical git read-only block *(prompts)*
  - readme.md/fix.md/flowchart.md: fix stale 'Step 3'/'Step 4' cross-references to 'Step 1' (REQ-018)
  - analyze.md/check.md: inline verbatim canonical git read-only restriction block from src/instructions/git_read-only.md (REQ-033)
  - [useReq]
- Fix REFERENCES.md.
- Fix requirements.

### 🚜  Changes
- BREAKING CHANGE: rewrite Context Files description without CLI/runtime references [useReq] *(prompts)*
  - Update REQ-035 to require exactly one %%CONTEXT_FILES%% placeholder at the injection point
  - Reframe REQ-036 to instruct the agent on authoritative pre-loaded context usage
  - Add REQ-038 forbidding %%CONTEXT_FILES%% token, runtime, and CLI mechanism references in the Context Files description prose
  - Rewrite the ## Context Files description in all 15 src/prompts/*.md to give clear content and usage guidance to the agent without referencing the prompt-generation CLI or the %%CONTEXT_FILES%% substitution mechanism
- append %%CONTEXT_FILES%% section to all prompts *(prompts)*
  - Append an identical ## Context Files section as the last section of
  - every bundled prompt under src/prompts, ending with the %%CONTEXT_FILES%%
  - token as the final line for runtime context-file injection.
  - Update REQ-002 to include %%CONTEXT_FILES%% in the rendered-token list
  - and add REQ-165/REQ-166 covering the section and preamble contract.
  - Refresh WORKFLOW.md and REFERENCES.md to document the new section. [useReq]

### 🎯  Cover Requirements
- Fix git grep wording and add Expert GitOps Engineer persona [useReq] *(prompts)*
  - Replace grep with git grep in shell-safety contract across 15 prompts (REQ-030, REQ-031).
  - Fix analyze.md allowed-git list to use git grep (ANZ-CTX-004).
  - Add Expert GitOps Engineer persona to 11 prompts (CHG/COV/FIX/IMP/NEW/RFR/RCR/RNB/WFL/RDM/FCH-CTX).
  - No requirements, tests, or runtime-model changes.
  - Remaining REQ-027/RDM-CTX-001/FCH-CTX-001 (usage metadata) require /req-change (DES-006 conflict).

## [0.4.0](https://github.com/Ogekuri/PI-Prompts/compare/v0.3.0..v0.4.0) - 2026-07-08
### 🐛  Bug Fixes
- Update README.md file.

## [0.3.0](https://github.com/Ogekuri/PI-Prompts/compare/v0.2.0..v0.3.0) - 2026-07-08
### ⛰️  Features
- Add src/instructions/git_read-only.md file.

### 🐛  Bug Fixes
- Remove useReq support.
- Minor fixes.
- Fix ignore file.

### 🚜  Changes
- BREAKING CHANGE: remove YAML front matter from standalone docs [useReq] *(prompts)*
  - update the SRS for title-first standalone Markdown documents
  - strip YAML front matter from bundled prompts and the requirements template
  - add unittest coverage for title-first and no-front-matter checks
- remove extra prompt frontmatter keys [useReq] *(prompts)*
  - update REQ-163 and TST-047 for single-key prompt metadata
  - remove argument-hint and usage from all bundled prompt YAML headers
  - align WORKFLOW.md and REFERENCES.md with description-only front matter
- update usage routing metadata [useReq] *(prompts)*
  - add REQ-163 and TST-047 for bundled prompt usage fields
  - rewrite src/prompts YAML usage guidance without the literal Do NOT select if syntax
  - refresh WORKFLOW.md and REFERENCES.md for front-matter routing metadata
- BREAKING CHANGE: remove standalone references prompt [useReq] *(prompts)*
  - remove src/prompts/references.md
  - update prompt catalog and selection guidance
  - refresh requirements, workflow, and references docs
- rename summarize tool references [useReq] *(prompts)*
  - Change-Id: useReq-20260424-01
  - REQ-003 and REQ-162 now define canonical prompt tool naming and preserve the grep wording rule.
  - Replaced references-generation with summarize in the bundled prompt workflows that instruct agents to regenerate REFERENCES.md.
  - Verification: static-check reported no source files found in configured directories; no relevant tests exist in this repository.
- BREAKING CHANGE: rename find tools to search in prompts [useReq] *(prompts)*
  - update REQUIREMENTS.md tool names for the breaking rename\n- update bundled prompts to reference only search/files-search\n- keep WORKFLOW.md and REFERENCES.md unchanged because no runtime source changed
- replace git grep references with grep [useReq] *(prompts)*
  - REQ-003 TST-046\nUpdate bundled prompts in src/prompts by replacing every git grep reference with grep.\nKeep the change surface minimal and limited to prompt text plus aligned requirements metadata.
- centralize generic git guidance [useReq] *(prompts)*
  - REQ-159 REQ-161 TST-002 TST-045\nMove shared GitOps persona and commit-safety rules into src/instructions/git_commit.md.\nRemove duplicated prompt-level GitOps persona text and generic repository-write commit rules from bundled prompts.
- rename git commit artifact and align docs [useReq] *(instructions)*
  - rename src/instructions/commit.md to src/instructions/git_commit.md
  - add requirement coverage for src/instructions/git_read-only.md
  - align analyze/check prompts with the canonical git read-only restriction
- reserve %%PROMPT%% for commit type [useReq] *(commit)*
  - add %%PROMPT%% to placeholder requirements
  - preserve runtime-reserved %%COMMIT%% and %%PROMPT%% tokens
  - align workflow and references docs with commit instruction
- rename %%COMMIT%% token and align steps [useReq] *(prompts)*
  - rename the shared commit placeholder to %%COMMIT%% across prompts and docs
  - add the commit stage as the penultimate step in write.md and create.md
  - split analyze.md so Present results is explicit Step 2
- rename shared instruction directory [useReq] *(instructions)*
  - update docs/REQUIREMENTS.md path references to src/instructions
  - rename src/istructions/commit.md to src/instructions/commit.md
  - refresh docs/WORKFLOW.md and docs/REFERENCES.md traceability
- externalize shared commit step [useReq] *(prompts)*
  - Add src/istructions/commit.md as the canonical shared commit instruction.
  - Replace inline commit steps with %%COMMIT%%% in commit-bearing prompts.
  - Update docs requirements, workflow, and references for the shared commit placeholder.
- BREAKING CHANGE: remove worktree and preflight prompt steps [useReq] *(prompts)*
  - drop standalone docs-check and Check GIT Status steps
  - remove worktree lifecycle and merge-management instructions
  - keep final commit and final git-status verification
- BREAKING CHANGE: remove prompt worktree and precheck steps [useReq] *(core)*
  - Remove git-status and docs-check prompt steps.
  - Drop worktree and merge-management instructions.
  - Keep prompts limited to final commit generation.
  - Update requirements, workflow, and references docs.
- replace template doc paths with %%TEMPLATE_PATH%% [useReq] *(prompts)*
  - update requirements for placeholder token validation
  - replace literal .req/docs references in source prompts
  - refresh workflow and references docs
- prefer structured discovery over grep-first [useReq] *(prompts)*
  - Add REQ-048 and update prompt toolkit plus verification wording to prefer find/files-find over default grep-first discovery. Refresh WORKFLOW and REFERENCES to match the new prompt behavior.

### ◀️  Revert
- Roll back branch to 074edecc (074edecc4300e14f953888b5356dda60a93b12e1).
- Roll back branch to d56327a5 (d56327a58f68f5ea3da48a8c6070be9cf1e47bf4).

## [0.2.0](https://github.com/Ogekuri/PI-Prompts/compare/v0.1.0..v0.2.0) - 2026-04-15
### 🐛  Bug Fixes
- Fix github workflow.

## [0.1.0](https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.1.0) - 2026-04-15
### ⛰️  Features
- Reduce tool verbosity in prompts.
- Initial commit.

### 🐛  Bug Fixes
- Update documents.
- Revert to 0.0.0 version.

### 🚜  Changes
- migrate operations to tool capabilities [useReq] *(prompts)*
  - update SRS shared operational requirements
  - replace migrated req transport literals across prompts
  - refresh workflow, references, and README wording

### 📚  Documentation
- Update README.md.


# History

- \[0.1.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.1.0
- \[0.2.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.2.0
- \[0.3.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.3.0
- \[0.4.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.4.0
- \[0.5.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.5.0
- \[0.6.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.6.0
- \[0.7.0\]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.7.0

[0.1.0]: https://github.com/Ogekuri/PI-Prompts/releases/tag/v0.1.0
[0.2.0]: https://github.com/Ogekuri/PI-Prompts/compare/v0.1.0..v0.2.0
[0.3.0]: https://github.com/Ogekuri/PI-Prompts/compare/v0.2.0..v0.3.0
[0.4.0]: https://github.com/Ogekuri/PI-Prompts/compare/v0.3.0..v0.4.0
[0.5.0]: https://github.com/Ogekuri/PI-Prompts/compare/v0.4.0..v0.5.0
[0.6.0]: https://github.com/Ogekuri/PI-Prompts/compare/v0.5.0..v0.6.0
[0.7.0]: https://github.com/Ogekuri/PI-Prompts/compare/v0.6.0..v0.7.0
