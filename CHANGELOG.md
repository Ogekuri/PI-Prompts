# Changelog

## [0.27.0](https://github.com/Ogekuri/Prompts/compare/v0.26.0..v0.27.0) - 2026-04-14
### 🐛  Bug Fixes
- Fix src/prompts/flowchart.md file.

## [0.26.0](https://github.com/Ogekuri/Prompts/compare/v0.25.0..v0.26.0) - 2026-04-14
### 🚜  Changes
- normalize branch granularity rules [useReq] *(flowchart)*
  - refine flowchart Step 4 requirements for branch normalization and audit checks
  - update src/prompts/flowchart.md with comparability, wrapper, join, and skip rules
  - refresh docs/REFERENCES.md for the prompt-only change surface

## [0.25.0](https://github.com/Ogekuri/Prompts/compare/v0.24.0..v0.25.0) - 2026-04-14
### ⛰️  Features
- add flowchart prompt requirements [useReq] *(flowchart)*
  - add src/prompts/flowchart.md from the provided flowchart template\n- extend docs/REQUIREMENTS.md with REQ-016 and FCH requirement coverage\n- update docs/WORKFLOW.md and docs/REFERENCES.md for the new prompt

### 🐛  Bug Fixes
- Yaml fields.
- align prompt compliance wording [useReq] *(prompts)*
  - Normalize MUST wording in prompt purposes.
  - Switch targeted prompt Python execution guidance to .venv/bin/python.
  - Add no-source static-check handling to req-check.
  - Remove duplicate change commit-comment instruction.
  - Fix the evidence-oriented grammar defect in req-fix.

## [0.24.0](https://github.com/Ogekuri/Prompts/compare/v0.23.0..v0.24.0) - 2026-04-12
### 📚  Documentation
- align prompt and template usage coverage [useReq] *(readme)*
  - update prompt table with argument-hint driven selection guidance
  - document shared shell-safety and req worktree/git-check behaviors
  - clarify template contracts and release-tag publishing surface
- Update README.md file.

## [0.23.0](https://github.com/Ogekuri/Prompts/compare/v0.22.0..v0.23.0) - 2026-04-03
### 🚜  Changes
- require explicit search option termination [useReq] *(prompts)*
  - Update REQ-030 for explicit option termination on rg and git grep.
  - Add REQ-031 to forbid relying only on quoting or backslash escaping.
  - Propagate the shared shell-command rule across src/prompts/*.md.
  - Refresh WORKFLOW.md and REFERENCES.md to document the change.

## [0.22.0](https://github.com/Ogekuri/Prompts/compare/v0.21.0..v0.22.0) - 2026-04-02
### 🚜  Changes
- tighten shell literal argument handling [useReq] *(core)*
  - split shell-command requirement into focused atomic rules
  - require quoting, escaping, or option termination for flag-like literals
  - update shared shell-safety instruction across prompt sources
  - refresh requirements, workflow, and references docs

## [0.21.0](https://github.com/Ogekuri/Prompts/compare/v0.20.0..v0.21.0) - 2026-04-01
### 🐛  Bug Fixes
- Fix git repository.

### 🚜  Changes
- tighten shell command generation rules [useReq] *(core)*
  - update REQ-019 and add REQ-020 for restrictive-filter-compatible shell commands
  - require linear shell commands and forbid command substitution/backticks
  - align prompt absolute rules and worktree execution phrasing
  - update WORKFLOW and REFERENCES traceability
- prevent shell-composed req worktree steps [useReq] *(core)*
  - Update REQ-019 with a global sequential req-command rule.
  - Align worktree-enabled prompts with literal result retention.
  - Align ignored runtime skill mirrors with the same canonical wording.
  - Update WORKFLOW.md and REFERENCES.md for the new prompt behavior.
  - Treat req static/references no-source output as verification evidence in this repo.
- harden worktree shell instructions [useReq] *(core)*
  - Update REQ-019 for shell-safe sequential req worktree steps.
  - Revise worktree setup and merge-return wording in prompts.
  - Mirror the shell-safety wording in req skill artifacts.
  - Refresh workflow and references documentation.

### ◀️  Revert
- Roll back branch to d8b055c5 (d8b055c56744af61caa0b8ed11614355ff0c6b79).

## [0.20.0](https://github.com/Ogekuri/Prompts/compare/v0.19.0..v0.20.0) - 2026-04-01
### 🚜  Changes
- clarify non-GPG commit requirement [useReq] *(core)*
  - update Stage & commit requirement IDs for non-GPG commit guidance\n- update affected prompt artifacts under src/prompts\n- refresh workflow and references documentation

## [0.19.0](https://github.com/Ogekuri/Prompts/compare/v0.18.0..v0.19.0) - 2026-04-01
### 🚜  Changes
- clarify human-readable final reports [useReq] *(core)*
  - Update final report instructions to target human readers.
  - Adjust SRS step requirements for report presentation.
  - Align prompt artifacts with clear-sentence Markdown guidance.
  - Refresh WORKFLOW.md and REFERENCES.md for traceability.

## [0.18.0](https://github.com/Ogekuri/Prompts/compare/v0.17.0..v0.18.0) - 2026-03-30
### 🚜  Changes
- add incompatibility conflict-table output [useReq] *(fix)*
  - Add FIX-STP-011 requirement for Step 4 incompatibility handling.
  - Require fix prompt to emit 3-column conflict table before exact error output.
  - Update WORKFLOW and REFERENCES to keep runtime/docs traceability aligned.

## [0.17.0](https://github.com/Ogekuri/Prompts/compare/v0.16.0..v0.17.0) - 2026-03-18
### 📚  Documentation
- Update README.md title.

## [0.16.0](https://github.com/Ogekuri/Prompts/compare/v0.15.0..v0.16.0) - 2026-03-18
### 🐛  Bug Fixes
- Update prompts.
- derive only BASE_PATH for worktree exit [useReq] *(prompts)*
  - Update merge-preparation instructions that execute cd <BASE_PATH> to derive only <BASE_PATH> with req --get-base-path.
  - Remove unnecessary <GIT_PATH> derivation from prompt exit bullets and align WORKFLOW/REFERENCES documentation.

### 🚜  Changes
- scope worktree context to worktree prompts [useReq] *(prompts)*
  - Update REQ-019 to require Pre-requisite/WORKTREE_NAME only where req --git-wt-create is used.
  - Remove Pre-requisite: Execution Context from analyze and check prompts.
  - Align WORKFLOW and REFERENCES docs with the new worktree-scoping rule.
- normalize worktree path commands [useReq] *(prompts)*
  - Replace req --base-path with req --get-base-path in operational prompt instructions.
  - Update worktree entry to cd <GIT_PATH>/../<WORKTREE_NAME> and exit to cd <BASE_PATH> with conditional derivation commands.
  - Add mandatory execution-context retention rule to Pre-requisite sections and align REQ-019/WORKFLOW/REFERENCES traceability.
- add base/git path derivation in step 3 [useReq] *(prompts)*
  - Update REQ-019 to include req --base-path and req --git-path in canonical worktree generation instructions.
  - Standardize Step-3 bullets across prompt artifacts to derive <BASE_PATH> and <GIT_PATH> before req --git-wt-name.
  - Update WORKFLOW and REFERENCES to preserve traceability for the new operational contract.
- require explicit post-create cd [useReq] *(prompts)*
  - Update REQ-019 to require cd ../<WORKTREE_NAME> after req --git-wt-create.
  - Align all Step-3 worktree instructions to run explicit cd before next step.
  - Refresh WORKFLOW and REFERENCES to encode the explicit directory-switch contract.

## [0.15.0](https://github.com/Ogekuri/Prompts/compare/v0.14.0..v0.15.0) - 2026-03-18
### 🚜  Changes
- clarify worktree create chdir semantics [useReq] *(prompts)*
  - Update REQ-019 to require explicit create-and-enter wording for req --git-wt-create.
  - Align Step 3 instructions across prompt artifacts with explicit cd/chdir behavior.
  - Update WORKFLOW and REFERENCES docs to reflect the new operational contract.
- enforce reproducer-test-first bug fix flow [useReq] *(fix)*
  - Update FIX requirement IDs and fix prompt behavior/steps.
  - When relevant suites exist, require failing reproducer unit test before fix.
  - Require explicit reproducer test pass evidence in verification.
  - Align WORKFLOW and REFERENCES traceability with the new fix policy.
- enforce conditional unit-test verification [useReq] *(prompts)*
  - Update SRS requirement IDs for change/fix/new/cover/implement/refactor verification.
  - Require running unit tests only when relevant suites already exist in repository.
  - Define language-specific priority policy for selecting test commands.
  - Align prompt verification steps and workflow/reference docs with new policy.

## [0.14.0](https://github.com/Ogekuri/Prompts/compare/v0.13.0..v0.14.0) - 2026-03-17
### 🚜  Changes
- use static-check-only verification [useReq] *(prompts)*
  - Remove mandatory pytest/unit-test-suite execution requirements.
  - Add REQ-028 to treat no-source static-check output as success.
  - Align implementation prompts to static-analysis verification flow.
  - Update WORKFLOW and REFERENCES traceability for the new policy.
- enforce full-SRS verification in final audits [useReq] *(prompts)*
  - update CHG-STP-006, NEW-STP-006, FIX-STP-005 for normative ALL-requirements audits
  - align change/new/fix verification wording with progressive disclosure pattern
  - update WORKFLOW and REFERENCES traceability for prompt behavior change

## [0.13.0](https://github.com/Ogekuri/Prompts/compare/v0.12.0..v0.13.0) - 2026-03-17
### 🐛  Bug Fixes
- Fix python venv in prompts.
- Remove .req dir.

### 📚  Documentation
- Update README.md document.

## [0.12.0](https://github.com/Ogekuri/Prompts/compare/v0.11.0..v0.12.0) - 2026-03-16
### 🚜  Changes
- use req --git-check for final clean check [useReq] *(prompts)*
  - Update REQ-019 to require final cleanliness verification with req --git-check.
  - Replace final step instructions in prompt set that used git status --porcelain.
  - Align WORKFLOW and REFERENCES docs with the new verification command.
- simplify git cleanup to worktree delete only [useReq] *(prompts)*
  - Update requirement constraints for interruption cleanup paths.
  - Remove rollback/revert git-state instructions from prompt failure branches.
  - Keep only req --git-wt-delete <WORKTREE_NAME> as cleanup command.
  - Align WORKFLOW and REFERENCES docs with new cleanup behavior.

## [0.11.0](https://github.com/Ogekuri/Prompts/compare/v0.10.0..v0.11.0) - 2026-03-16
### 🚜  Changes
- exclude create-failure delete [useReq] *(worktree-cleanup)*
  - Remove req --git-wt-delete from Worktree generation failed branches.
  - Keep delete only for post-create early exits except create-failure, and never for pre-create/doc-check exits.
- enforce pre-create delete guard [useReq] *(worktree-cleanup)*
  - Clarify step-order constraint for req --git-wt-delete usage.
  - Delete instruction is now forbidden before req --git-wt-create and in prompts without create step.
  - Align WORKFLOW and REFERENCES documentation with the scoped rule.
- scope cleanup to post-create exits [useReq] *(worktree-cleanup)*
  - Keep req --git-wt-delete <WORKTREE_NAME> only for early-termination branches between worktree creation and merge-phase cleanup.
- enforce early-exit worktree deletion [useReq] *(worktree-cleanup)*
  - Update REQ-019 and REQ-025 for post-create early termination cleanup.
  - Add req --git-wt-delete <WORKTREE_NAME> instruction to all affected prompt early exits.
  - Sync WORKFLOW and REFERENCES docs with the new cleanup contract.

## [0.10.0](https://github.com/Ogekuri/Prompts/compare/v0.9.0..v0.10.0) - 2026-03-16
### ⛰️  Features
- Update useReq files.

### 🐛  Bug Fixes
- Update .gitignore file.
- Fix bell string.

### 🚜  Changes
- use req --git-wt-exit [useReq] *(prompts)*
  - Specify req --git-wt-exit when returning to original branch after worktree usage.
  - Update REQ-019 to include req --git-wt-exit in canonical req operation commands.
  - Align Merge Conflict Management instructions across affected prompts.
- prefer req project ops [useReq] *(prompts)*
  - Refactor prompt workflows to use req utility for git/docs/worktree checks.
  - Replace legacy <EXECUTION_ID>/<ORIGINAL_BRANCH>/<PROJECT_NAME> worktree naming with <WORKTREE_NAME> from req --git-wt-name.
  - Consolidate worktree create/delete flow with req --git-wt-create and req --git-wt-delete error handling.
  - Simplify docs and git checks using req --docs-check and req --git-check.
  - Update REQ-019 canonical instruction requirement accordingly.
- enforce LLM prompt-engineer persona [useReq] *(prompts)*
  - Update REQ-022 to require Prompt Engineer and LLM Optimization Specialist persona.
  - Insert the persona rule in Professional Personas for all prompt sources in src/prompts.
  - No runtime workflow structure changes were required.
- BREAKING CHANGE: remove bell suffix from terminal literals [useReq] *(prompts)*
  - update DES-002/REQ-023/REQ-025 to require bell-free exact outputs
  - remove \x07 suffix from all prompt fixed terminal strings
  - update WORKFLOW/REFERENCES to reflect bell-free output contract

## [0.9.0](https://github.com/Ogekuri/Prompts/compare/v0.8.0..v0.9.0) - 2026-03-07
### ⛰️  Features
- Update .req/models.json file.

### 🐛  Bug Fixes
- Fix $\( in prompts.
- Fix error: Command blocked: contains dangerous shell expansion patterns (e.g., parameter transformation, indirect expansion, or nested command substitution) that could enable arbitrary code execution. Please rewrite the command without these expansion patterns.
- Update .req/docs/Document_Source_Code_in_Doxygen_Style.md template.

### 🚜  Changes
- enforce bell on terminal outputs [useReq] *(prompts)*
  - Update DES-002, REQ-023, and REQ-025 for terminal output bell suffix requirements.
  - Append \x07 to fixed terminal literals across prompt workflows (ERROR/WARNING/STATUS/no-op outputs).
  - Update WORKFLOW main prompt entrypoint coverage and REFERENCES change index.

## [0.8.0](https://github.com/Ogekuri/Prompts/compare/v0.7.0..v0.8.0) - 2026-03-04
### 🐛  Bug Fixes
- Include .req directory to support worktree.

### 🚜  Changes
- enforce path-only update rules [useReq] *(workflow)*
  - extend WORKFLOW-update step requirements across req-change/new/cover/fix/implement/refactor
  - require declaration-file paths only and forbid line numbers/ranges/internal file pointers
  - align workflow, implementation, references, and runtime-model docs
- enforce path-only WORKFLOW references [useReq] *(workflow)*
  - update WFL-CTX-003 and WFL-STP-004 requirements\n- update workflow prompt output contract to exclude line numbers/ranges\n- update WORKFLOW.md and REFERENCES.md for declaration-path-only references
- align doxygen component coverage [useReq] *(prompts)*
  - Update Doxygen coverage directives to explicitly include objects and structures.
  - Sync source templates and req runtime docs with the same component taxonomy.
  - Update PRJ-002, WORKFLOW.md, and REFERENCES.md for traceability.

### 📚  Documentation
- regenerate runtime model for prompt and release jobs [useReq] *(workflow)*
  - Regenerate docs/WORKFLOW.md from src/ and .github/workflows static analysis.\n- Capture explicit GitHub Actions inter-job communication edge.

## [0.7.0](https://github.com/Ogekuri/Prompts/compare/v0.6.0..v0.7.0) - 2026-03-03
### 🐛  Bug Fixes
- Fix readme prompt.

### 🚜  Changes
- enforce user-request extra README edits [useReq] *(readme-prompt)*
  - Update RDM-CTX-005 and RDM-STP-004 to require explicit additional edits from [User Request](#users-request).
  - Update src/prompts/readme.md Behavior and Step 4 to execute %%ARGS%%-driven additional edits using write.md-style user-request anchoring.
  - Refresh WORKFLOW.md and REFERENCES.md for traceability.
- BREAKING CHANGE: refactor Source Construct Extraction into Source Code Analysis Toolkit [useReq] *(prompts)*
  - REQ-019 updated: Source Code Analysis Toolkit with four-pillar pipeline
  - New section defines sequential analysis workflow: WORKFLOW.md (runtime model),
  - REFERENCES.md (symbol index with Doxygen metadata), req --find/--files-find
  - (code extraction), rg/git grep (supplementary search)
  - Recommended 1->2->3->4 analysis workflow for token-efficient code analysis
  - Replaced old section in 10 prompt files with identical canonical content
  - Preserved all existing req --find/--files-find command reference details
  - Added REFERENCES.md Doxygen field enumeration for LLM target identification

## [0.6.0](https://github.com/Ogekuri/Prompts/compare/v0.5.0..v0.6.0) - 2026-03-01
### 🐛  Bug Fixes
- Minor fixes.

## [0.5.0](https://github.com/Ogekuri/Prompts/compare/v0.4.0..v0.5.0) - 2026-03-01
### 🐛  Bug Fixes
- Remove placehoder from src.

## [0.4.0](https://github.com/Ogekuri/Prompts/compare/v0.3.0..v0.4.0) - 2026-03-01
### ⛰️  Features
- Add src/.place-holder file.

### 🐛  Bug Fixes
- Fix line numbers.
- Replace userReq with useReq.
- Fix .g.conf file.

### 🚜  Changes
- align req-find syntax and line prefixes [useReq] *(prompts)*
  - Update REQ-019 to codify req --find syntax semantics.
  - Apply Source Construct Extraction wording updates across affected prompts.
  - Set req --find examples without explicit --here, forbid --base wording, and use <n>: line prefix.
- enforce worktree cleanup verification [useReq] *(prompts)*
  - update REQ-019 with mandatory pre-step cleanup verification
  - add merge-success verification command to all worktree-based prompts
  - align WORKFLOW and REFERENCES docs with cleanup verification behavior
- Update <EXECUTION_ID> generation.

## [0.3.0](https://github.com/Ogekuri/Prompts/compare/v0.2.0..v0.3.0) - 2026-02-24
### 🐛  Bug Fixes
- Fix workflow file. *(core)*

## [0.2.0](https://github.com/Ogekuri/Prompts/compare/v0.1.0..v0.2.0) - 2026-02-24
### 🐛  Bug Fixes
- Remove src/.place-holder file. *(core)*

## [0.1.0](https://github.com/Ogekuri/Prompts/releases/tag/v0.1.0) - 2026-02-24
### ⛰️  Features
- add workflow. *(core)*
- add .place-holder files. *(core)*
- add guidelines/ and .gitignore. *(core)*
- cap prompt usage length [useReq] *(requirements)*
  - add REQ-027: YAML usage value length MUST be <= 1024
  - validate all prompt usage headers are within the limit
  - update workflow/references docs for traceability
- add readme prompt workflow [useReq] *(prompts)*
  - add src/prompts/readme.md derived from workflow prompt
  - append REQ-015 and RDM-* prompt-specific requirements
  - update WORKFLOW/REFERENCES docs for README-facing workflow
- add docs/REQUIREMENTS.md draft. *(core)*
- simplify doxygen templates. *(core)*
- review README.md. *(core)*
- add REQUIREMENTS.md. *(core)*
- initial commit. *(core)*

### 🐛  Bug Fixes
- Fix .g.conf file. *(core)*
- fix remove branch of worktree. *(core)*
- update the workflow script. *(core)*
- req. with req- *(core)*
- minor fix on src/prompts/change.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- update docs/REQUIREMENTS.md. *(core)*
- BRAKING typo. *(core)*
- update docs/REQUIREMENTS.md. *(core)*

### 🚜  Changes
- use worktree path for config cleanup [useReq] *(worktree)*
  - Update REQ-019 with explicit worktree cleanup target path.
  - Align all worktree-capable prompts to remove copied config from worktree path before merge.
- prioritize test-oriented defect fix flow [useReq] *(prompts)*
  - update FIX requirements for preferred test-first bug-fix sequence
  - add constrained no-test fallback when one-test reproduction is costly/infeasible
  - align fix prompt behavior/steps and workflow/references traceability
- tighten scoped README edit rules [useReq] *(readme)*
  - update RDM requirements for section-scoped README edits
  - require preserving non-analysis sections and existing format
  - align readme prompt behavior/steps plus workflow and references docs
- normalize workflow wording tokens [useReq] *(requirements)*
  - Refine section 3.3 step wording to use WORKFLOW document contract.
  - Keep DOC-002 and DOC-003 normalization valid after wording cleanup.
- normalize DOC-002 DOC-003 wording [useReq] *(requirements)*
  - Normalize requirement wording in docs/REQUIREMENTS.md section 3.3.
  - Replace non-RFC modal verbs with RFC2119-compliant wording.
  - Normalize listed requirement lines to single-sentence statements.
- rewrite prompt-specific semantics [useReq] *(requirements)*
  - Rework section 3.3 requirements to describe prompt-construction behavior.
  - Remove implementation-reference wording based on exact-text equality and file linkage.
  - Preserve prompt-specific IDs and step granularity while expressing normative intent directly.
- complete prompt section mappings [useReq] *(requirements)*
  - Replace all TODO placeholders in prompt-specific requirements.
  - Add atomic context requirements for Purpose, Scope, Professional Personas, and Behavior sections.
  - Add one step requirement per numbered Step for all prompts under src/prompts/.
  - Remove duplicate orphan TODO block under Renumber section.
- handle gitignored req config in worktree/merge [useReq] *(prompts)*
  - update REQ-019 for canonical .req/config.json handling
  - add copy step after worktree creation in affected prompts
  - add remove step before merge in affected prompts
  - refresh WORKFLOW.md and REFERENCES.md for changed artifacts
- add rule-coverage function requirements [useReq] *(requirements)*
  - Update REQ-015/REQ-016 wording for Section 2.3 traceability.
  - Add REQ-017..REQ-026 to encode Section 1.5 rule checks.
  - Embed explicit exception clauses so current prompt/template corpus remains valid.
- rewrite absolute rules for LLM clarity [useReq] *(core)*
  - update section 1.5 wording for LLM-focused clarity\n- remove redundant repeated action directives\n- keep requirement semantics and scope intact
- add governance constraints for prompt/template maintenance [useReq] *(requirements)*
  - Update PRJ-008 to require explicit change requests for prompt/template artifact changes.
  - Add CTN-013 and CTN-014 to keep prompt/template governance rules only in docs/REQUIREMENTS.md.
  - Add TST-009 and TST-010 for governance and change-request traceability checks.

### 📚  Documentation
- add readme prompt to prompt catalog [useReq] *(prompts)*
  - add `readme` prompt entry under Prompts and Agents\n- describe README alignment behavior from user-visible evidence


# History

- \[0.1.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.1.0
- \[0.2.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.2.0
- \[0.3.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.3.0
- \[0.4.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.4.0
- \[0.5.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.5.0
- \[0.6.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.6.0
- \[0.7.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.7.0
- \[0.8.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.8.0
- \[0.9.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.9.0
- \[0.10.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.10.0
- \[0.11.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.11.0
- \[0.12.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.12.0
- \[0.13.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.13.0
- \[0.14.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.14.0
- \[0.15.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.15.0
- \[0.16.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.16.0
- \[0.17.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.17.0
- \[0.18.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.18.0
- \[0.19.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.19.0
- \[0.20.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.20.0
- \[0.21.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.21.0
- \[0.22.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.22.0
- \[0.23.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.23.0
- \[0.24.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.24.0
- \[0.25.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.25.0
- \[0.26.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.26.0
- \[0.27.0\]: https://github.com/Ogekuri/Prompts/releases/tag/v0.27.0

[0.1.0]: https://github.com/Ogekuri/Prompts/releases/tag/v0.1.0
[0.2.0]: https://github.com/Ogekuri/Prompts/compare/v0.1.0..v0.2.0
[0.3.0]: https://github.com/Ogekuri/Prompts/compare/v0.2.0..v0.3.0
[0.4.0]: https://github.com/Ogekuri/Prompts/compare/v0.3.0..v0.4.0
[0.5.0]: https://github.com/Ogekuri/Prompts/compare/v0.4.0..v0.5.0
[0.6.0]: https://github.com/Ogekuri/Prompts/compare/v0.5.0..v0.6.0
[0.7.0]: https://github.com/Ogekuri/Prompts/compare/v0.6.0..v0.7.0
[0.8.0]: https://github.com/Ogekuri/Prompts/compare/v0.7.0..v0.8.0
[0.9.0]: https://github.com/Ogekuri/Prompts/compare/v0.8.0..v0.9.0
[0.10.0]: https://github.com/Ogekuri/Prompts/compare/v0.9.0..v0.10.0
[0.11.0]: https://github.com/Ogekuri/Prompts/compare/v0.10.0..v0.11.0
[0.12.0]: https://github.com/Ogekuri/Prompts/compare/v0.11.0..v0.12.0
[0.13.0]: https://github.com/Ogekuri/Prompts/compare/v0.12.0..v0.13.0
[0.14.0]: https://github.com/Ogekuri/Prompts/compare/v0.13.0..v0.14.0
[0.15.0]: https://github.com/Ogekuri/Prompts/compare/v0.14.0..v0.15.0
[0.16.0]: https://github.com/Ogekuri/Prompts/compare/v0.15.0..v0.16.0
[0.17.0]: https://github.com/Ogekuri/Prompts/compare/v0.16.0..v0.17.0
[0.18.0]: https://github.com/Ogekuri/Prompts/compare/v0.17.0..v0.18.0
[0.19.0]: https://github.com/Ogekuri/Prompts/compare/v0.18.0..v0.19.0
[0.20.0]: https://github.com/Ogekuri/Prompts/compare/v0.19.0..v0.20.0
[0.21.0]: https://github.com/Ogekuri/Prompts/compare/v0.20.0..v0.21.0
[0.22.0]: https://github.com/Ogekuri/Prompts/compare/v0.21.0..v0.22.0
[0.23.0]: https://github.com/Ogekuri/Prompts/compare/v0.22.0..v0.23.0
[0.24.0]: https://github.com/Ogekuri/Prompts/compare/v0.23.0..v0.24.0
[0.25.0]: https://github.com/Ogekuri/Prompts/compare/v0.24.0..v0.25.0
[0.26.0]: https://github.com/Ogekuri/Prompts/compare/v0.25.0..v0.26.0
[0.27.0]: https://github.com/Ogekuri/Prompts/compare/v0.26.0..v0.27.0
