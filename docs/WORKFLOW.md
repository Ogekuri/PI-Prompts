## Execution Units Index

- `PROC:main` | type: process | parent: none | role: prompt-workflow execution orchestrator for repository prompt artifacts with bell-free terminal output contracts | entrypoint: prompt frontmatter documents under `src/prompts/*.md` consumed by external runtime | defining files: `src/prompts/analyze.md`, `src/prompts/change.md`, `src/prompts/check.md`, `src/prompts/cover.md`, `src/prompts/create.md`, `src/prompts/fix.md`, `src/prompts/flowchart.md`, `src/prompts/implement.md`, `src/prompts/new.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/refactor.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, `src/prompts/workflow.md`, `src/prompts/write.md`
- `PROC:gha-check-branch` | type: process | parent: none | role: validates tagged commit ancestry and emits release-gate output | entrypoint: workflow `Release (markdown)` job `check-branch` | defining files: `.github/workflows/release-markdown.yml`
- `PROC:gha-build-release` | type: process | parent: none | role: builds changelog and publishes GitHub release assets | entrypoint: workflow `Release (markdown)` job `build-release` | defining files: `.github/workflows/release-markdown.yml`

## Execution Units

### `PROC:main`

- Entrypoint(s):
  - Prompt frontmatter declarations consumed by external runtime [`src/prompts/analyze.md`, `src/prompts/change.md`, `src/prompts/check.md`, `src/prompts/cover.md`, `src/prompts/create.md`, `src/prompts/fix.md`, `src/prompts/flowchart.md`, `src/prompts/implement.md`, `src/prompts/new.md`, `src/prompts/readme.md`, `src/prompts/recreate.md`, `src/prompts/refactor.md`, `src/prompts/references.md`, `src/prompts/renumber.md`, `src/prompts/workflow.md`, `src/prompts/write.md`].
- Lifecycle/trigger:
  - Starts when an operator invokes the external prompt runtime with a selected prompt file.
- Executes the selected prompt steps with exact terminal strings that do not append bell-control suffixes; prompts that execute `req --git-wt-create <WORKTREE_NAME>` explicitly require deriving `<BASE_PATH>` via `req --get-base-path` and `<GIT_PATH>` via `req --git-path` before generating `<WORKTREE_NAME>` via `req --git-wt-name`; when workflows require values retrieved from commands for later reuse, the prompt instructions retain literal results and require literal `req` commands with simple sequential execution; prompt instructions that generate shell commands emit only linear commands compatible with restrictive filtering systems, require correct quoting, escaping, or option termination for literal arguments that could be parsed as options or flags, require explicit option termination for `rg` and `git grep` patterns beginning with `-` or `--`, forbid reliance on quoting or backslash escaping alone for those patterns, and disallow command substitution, backticks, complex variable expansion, nested substitution, shell-derived helper composition, nested shell logic, or nested pipelines; every step that executes `req --git-wt-create <WORKTREE_NAME>` explicitly requires `cd <GIT_PATH>/../<WORKTREE_NAME>` immediately after `req --git-wt-create <WORKTREE_NAME>` and before the next step; merge-preparation steps explicitly require deriving `<BASE_PATH>` via `req --get-base-path` when needed and executing `cd <BASE_PATH>` instead of `req --git-wt-exit`; prompts that do not execute `req --git-wt-create <WORKTREE_NAME>` do not declare `## Pre-requisite: Execution Context` and do not include `<WORKTREE_NAME>` generation via `req --git-wt-name`; every declared `Pre-requisite: Execution Context` section explicitly requires all listed context information to remain continuously available for the full workflow and never be dropped, forgotten, or overwritten; final repository-cleanliness verification uses `req --git-check` (not `git status --porcelain`); authorized early-termination branches after successful worktree creation use only explicit `req --git-wt-delete <WORKTREE_NAME>` cleanup before termination and do not include rollback or revert git-state commands (`git restore .`, `git checkout .`, `git clean -fd`), while pre-create branches, create-failure branches, and prompts without worktree creation do not use `req --git-wt-delete <WORKTREE_NAME>`; Stage & commit instructions explicitly state that a GPG-signed commit is not required; final report instructions preserve the fixed report schema and exact status line while explicitly targeting human readers with clear sentences and readable Markdown formatting; verification stages use requirement evidence plus `req --here --static-check`, treat `Error: no source files found in configured directories.` as successful no-source completion, execute existing unit tests only when relevant suites are present using language-specific test-suite priority policy, and for defect-fix workflow prefer a failing reproducer unit-test-first sequence before applying source fixes and require a three-column requirement-conflict table (`Requirement ID`, `Conflicting Excerpt`, `Conflict Reason + Interrupted Implementation Intent`) before the incompatible-requirements error termination branch; exits after workflow completion.
- Internal Call-Trace Tree:
  - No internal functions detected under `src/` or `.github/workflows`.
- External Boundaries:
  - External prompt runtime parses Markdown prompt artifacts and executes tool/shell instructions declared in prompt steps.
- Thread Model:
  - no explicit threads detected.

### `PROC:gha-check-branch`

- Entrypoint(s):
  - Workflow trigger `on.push.tags: v[0-9]+.[0-9]+.[0-9]+` activates workflow run [`.github/workflows/release-markdown.yml`].
  - Job definition `check-branch` on `ubuntu-latest` [`.github/workflows/release-markdown.yml`].
- Lifecycle/trigger:
  - Starts as first job in workflow graph.
  - Performs checkout and branch-containment check for `${GITHUB_SHA}`.
  - Writes `is_master` output to `$GITHUB_OUTPUT`; exits.
- Internal Call-Trace Tree:
  - No internal functions detected under `src/` or `.github/workflows`.
- External Boundaries:
  - `actions/checkout@v4` action execution [`.github/workflows/release-markdown.yml`].
  - Shell + git boundary (`git fetch`, `git branch -r --contains`, `grep`) [`.github/workflows/release-markdown.yml`].
  - GitHub Actions output-file boundary (`$GITHUB_OUTPUT`) [`.github/workflows/release-markdown.yml`].
- Thread Model:
  - no explicit threads detected.

### `PROC:gha-build-release`

- Entrypoint(s):
  - Job definition `build-release` with dependency `needs: check-branch` and gate `if: needs.check-branch.outputs.is_master == 'true'` [`.github/workflows/release-markdown.yml`].
- Lifecycle/trigger:
  - Starts only after `PROC:gha-check-branch` completion and positive gate output.
  - Performs checkout, changelog generation, and release publication.
  - Exits after release action completes.
- Internal Call-Trace Tree:
  - No internal functions detected under `src/` or `.github/workflows`.
- External Boundaries:
  - `actions/checkout@v4` action execution [`.github/workflows/release-markdown.yml`].
  - `mikepenz/release-changelog-builder-action@v6` boundary [`.github/workflows/release-markdown.yml`].
  - `softprops/action-gh-release@v2` boundary [`.github/workflows/release-markdown.yml`].
- Thread Model:
  - no explicit threads detected.

## Communication Edges

- `EDGE:gha-check-branch->gha-build-release`
  - direction: `PROC:gha-check-branch -> PROC:gha-build-release`
  - mechanism: GitHub Actions job dependency (`needs`) + job output propagation
  - endpoint/channel: `needs.check-branch.outputs.is_master`
  - payload/data-shape: string enum (`"true" | "false"`) written via `$GITHUB_OUTPUT`
  - evidence: `.github/workflows/release-markdown.yml`
