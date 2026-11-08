> [!CAUTION]
> ### 🚨 STRICTLY EXPERIMENTAL — PROOF OF CONCEPT (PRE-ALPHA)
>
> ![Status: Proof of Concept](https://img.shields.io/badge/Status-Proof_of_Concept-red?style=flat-square) ![Stage: Pre-Alpha](https://img.shields.io/badge/Stage-Pre--Alpha-critical?style=flat-square) ![Maintenance: Personal Use Only](https://img.shields.io/badge/Scope-Personal_Use_Only-important?style=flat-square) ![Issues: Closed](https://img.shields.io/badge/Issues_%26_PRs-Not_Accepted-inactive?style=flat-square)
>
> **PLEASE READ CAREFULLY BEFORE USING THIS SOFTWARE:**
>
> * **Very Early Stage:** This project is currently a raw **Proof of Concept (PoC)** in a **pre-alpha** state. It is nowhere near production-ready and may contain severe bugs, breaking changes, or incomplete logic.
> * **Personal Use Only:** This repository is developed, maintained, and shared strictly for **personal use**.
> * **No Support or Feature Requests:** Please **do not** open issues, bug reports, or feature requests. They will not be addressed or accepted at this stage of development.
> * **No Warranty:** This software is provided **"AS IS"**, without warranty of any kind, express or implied. You may use it strictly for **testing and evaluation purposes** at your own sole risk.

# PI-Prompts / pi-prompts (0.10.0)

<p align="center">
  <img src="https://img.shields.io/badge/license-GPL--3.0-491?style=flat-square" alt="License: GPL-3.0">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-6A7EC2?style=flat-square&logo=terminal&logoColor=white" alt="Platforms">
  <img src="https://img.shields.io/badge/docs-live-b31b1b" alt="Docs">
</p>

<p align="center">
<strong>The <u>prompts</u> for <strong>useReq/req</strong> project.</strong><br>
This repository maintains the prompt set in `src/prompts/`, the documentation templates in `src/templates/`, and the reusable instruction snippets in `src/instructions/` used by the useReq SRS-driven workflow, which enforces the deterministic process `Requirements -> Design -> Implementation -> Verification`.
</p>

<p align="center">
  <a href="#feature-highlights">Feature Highlights</a> |
  <a href="#quick-start">Quick Start</a> |
  <a href="#requirements">Requirements</a> |
  <a href="#users-guide">User's Guide</a> |
  <a href="#acknowledgments">Acknowledgments</a>
</p>

<p align="center">
🚧 <strong>STAGE:</strong> PRE-ALPHA 📝 - Proof-of-Concept (PoC) - Work in Progress 🏗️ 🚧<br>
⚠️ <strong>IMPORTANT NOTICE</strong>: Created with <a href="https://www.npmjs.com/package/pi-usereq"><strong>PI-useReq/pi-usereq</strong></a> 🤖✨ ⚠️
</p>

# Feature Highlights

A prompt-only repository: no executable application is bundled, and every asset is a Markdown artifact consumed by SRS-driven agent workflows.

- Prompt catalog with 15 task-specialized prompt cards in `src/prompts/` for SRS-driven workflows (`Requirements -> Design -> Implementation -> Verification`).
- Every bundled prompt/template document starts with a level-1 title and omits YAML front matter.
- Shared shell-safety contract across prompts: linear commands only, explicit option termination for `rg`/`git grep` patterns that start with `-`/`--`, and no substitution-based shell composition.
- Reusable templates in `src/templates/` for SRS authoring, HDT test authoring, and Doxygen-style source documentation.
- Reusable instruction snippets in `src/instructions/`: the canonical commit-workflow block injected via `%%COMMIT%%` and the git read-only restriction block inlined into read-only prompts.
- Guideline files for `%%GUIDELINES_FILES%%` are resolved from the host project at installation time; none are bundled in this repository.
- Tag-driven release workflow publishes versioned prompt/template assets from `src/` on GitHub-hosted `ubuntu-latest` runners with a Node24-or-later runtime.

# Quick Start

Bring-up follows the flow Install -> Configure -> Execute.

1. **Install:** clone this repository (or download a release bundle) and keep it versioned alongside your useReq project.
2. **Configure:** copy the prompts from `src/prompts/`, the templates from `src/templates/`, and — when your installation substitutes `%%COMMIT%%` — the snippets from `src/instructions/` into your target installation paths.
3. **Execute:** select the prompt that matches the task type (see the [User's Guide](#users-guide) prompt catalog) and provide only the request details required by that workflow.

# Requirements

- A Git client to clone and version this repository alongside the host project.
- A prompt-host runtime that renders the bundled Markdown prompts and orchestrates repository validation, worktree isolation, and merge handling (for example, PI-useReq/pi-usereq); this repository bundles no executable code.
- GitHub-hosted `ubuntu-latest` runners with a Node24-or-later JavaScript runtime, required only to execute the release automation when publishing a release.
- Python 3.8 or later (standard library only) to run the repository unit tests.
- No third-party runtime libraries are required.

# User's Guide

## Install

1. Clone this repository, or download the `src/**/*` asset bundle attached to a GitHub Release for a tagged version (`v<major>.<minor>.<patch>`).
2. Copy the required prompt files from `src/prompts/` into your target prompt installation path.
3. Copy the required templates from `src/templates/` into your target docs/template installation path.
4. Copy the instruction snippets from `src/instructions/` when your installation substitutes `%%COMMIT%%`; the read-only restriction block is inlined verbatim into read-only prompts.
5. Keep installation-time placeholders preserved exactly (see [Advanced Configuration](#advanced-configuration)); guideline files for `%%GUIDELINES_FILES%%` come from your host project, not from this repository.

## Execute

- Select prompts by their documented purpose and scope; prompts are intentionally specialized and non-interchangeable.
- Provide the change request text plus the canonical documentation set of the host project (`usereq/docs/` with `REQUIREMENTS.md`, `WORKFLOW.md`, `REFERENCES.md`).
- Read-only prompts (`analyze`, `check`) never modify tracked files; all other workflows end with a staged, targeted commit.

## Advanced Configuration

- Installation-time placeholders MUST remain byte-identical so host-side substitution stays valid:
  - `%%ARGS%%`
  - `%%COMMIT%%`
  - `%%CONTEXT_FILES%%`
  - `%%DOC_PATH%%`
  - `%%GUIDELINES_FILES%%`
  - `%%PROMPT%%`
  - `%%SRC_PATHS%%`
  - `%%TEMPLATE_PATH%%`
  - `%%TEST_PATH%%`
- `%%DOC_PATH%%` points at the host project canonical docs directory (for example `usereq/docs/`); `REFERENCES.md` is generated by the `references-generation` tool, not by a bundled prompt.
- Adding or removing prompt/template files requires an explicit change request with a corresponding `REQUIREMENTS.md` update.

## Prompt Catalog

| Prompt | Purpose | Select when |
| --- | --- | --- |
| `analyze` | Produce an analysis report. | You need read-only investigation and structured evidence output. |
| `change` | Update requirements and implement corresponding changes. | Existing requirement behavior must change (non-additive edits in `REQUIREMENTS.md`). |
| `check` | Run the requirements check. | You need requirement-by-requirement compliance audit without implementation edits. |
| `cover` | Cover uncovered existing requirements. | Requirements are already defined and only minimal implementation deltas are needed for uncovered IDs. |
| `create` | Draft SRS from existing source code. | Implementation exists and you must bootstrap/update `REQUIREMENTS.md` from code evidence. |
| `fix` | Fix a defect without changing requirements. | Behavior is incorrect relative to existing requirements and must be restored. |
| `flowchart` | Generate `FLOWCHART.md` from source code. | You need primary execution-flow documentation regeneration only. |
| `implement` | Implement source code from requirements. | `REQUIREMENTS.md` is authoritative and you must build missing implementation/test coverage. |
| `new` | Add a new requirement and corresponding implementation. | Requested behavior is additive and can be implemented by appending new requirement IDs. |
| `readme` | Align root `README.md` with implementation evidence. | Only user-facing README coverage must be updated from external interface evidence. |
| `recreate` | Reorganize and update SRS from source evidence. | You must rewrite SRS structure while preserving existing IDs and optionally appending new IDs. |
| `refactor` | Optimize internals without requirement changes. | Internal maintainability/performance improvements are required without user-visible behavior changes. |
| `renumber` | Renumber SRS requirement IDs deterministically. | You need deterministic ID renumbering and internal cross-reference updates only. |
| `workflow` | Generate `WORKFLOW.md` from source code. | You need runtime execution model documentation regeneration only. |
| `write` | Draft SRS from user request text. | No authoritative implementation exists; requirements must be drafted directly from user intent. |

## Uninstall

1. Remove the prompt, template, and instruction files copied into the host project installation paths during Install.
2. Delete the cloned repository directory.
3. No registry entries, caches, or other persistent artifacts are created by this repository.

# Documentation

## Repository Layout

```text
├── .github/workflows/release-markdown.yml   # tag-triggered release automation (Node24-or-later runners)
├── src/
│   ├── prompts/                             # 15 task-specialized prompt cards
│   ├── templates/                           # SRS, HDT test, and Doxygen authoring guides
│   └── instructions/                        # commit-workflow and git read-only snippets
├── tests/                                   # standard-library Python unit tests
└── usereq/docs/                             # canonical SRS set: REQUIREMENTS, WORKFLOW, REFERENCES
```

## Bundled Templates

| Template | Purpose | How it works |
| --- | --- | --- |
| `src/templates/Document_Source_Code_in_Doxygen_Style.md` | Source-code documentation standard. | Enforces LLM-native Doxygen output with mandatory tag taxonomy and full symbol coverage rules. |
| `src/templates/HDT_Test_Authoring_Guide.md` | Unit-test authoring standard. | Defines Generator/Refactorer modes, deterministic HDT constraints, and fixed artifact output order. |
| `src/templates/Requirements_Template.md` | SRS authoring template. | Defines RFC 2119-only requirement writing rules, stable requirement IDs, and canonical SRS section structure. |

## Bundled Instruction Snippets

| Instruction | Purpose |
| --- | --- |
| `src/instructions/git_commit.md` | Canonical commit-workflow block injected through `%%COMMIT%%` into committing prompts. |
| `src/instructions/git_read-only.md` | Git read-only restriction block inlined verbatim into read-only prompts. |

## Release Process

1. Push a tag matching `v<major>.<minor>.<patch>` on the `master` branch.
2. The release workflow verifies the tag is on `master`, generates the changelog, and publishes `src/**/*` as release assets.
3. All workflow jobs run on GitHub-hosted `ubuntu-latest` runners with a Node24-or-later JavaScript runtime; no Node20 fallback or transitional forcing variables are used.

## Running the Tests

```bash
python3 -m unittest discover -s tests -t tests
```

## Changelog

Release history is maintained in `CHANGELOG.md`, generated per release by the release automation.

# License

This project is licensed under the [GNU General Public License v3.0](LICENSE). The software is provided "AS IS", for personal use only — see the caution notice at the top of this document.

# Acknowledgments

- [PI-useReq](https://github.com/Ogekuri/PI-useReq): companion project where the prompts of this repository are used to populate the prompts in its `src/resources` folder.
- Prompt management is implemented in this separate project to keep prompt-content maintenance focused on this project's own requirements, independent of their subsequent use in PI-useReq.
- The release automation builds on [actions/checkout](https://github.com/actions/checkout), [mikepenz/release-changelog-builder-action](https://github.com/mikepenz/release-changelog-builder-action), and [softprops/action-gh-release](https://github.com/softprops/action-gh-release).
