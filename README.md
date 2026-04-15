# Prompts (0.27.0)

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/license-GPL--3.0-491?style=flat-square" alt="License: GPL-3.0">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-6A7EC2?style=flat-square&logo=terminal&logoColor=white" alt="Platforms">
  <img src="https://img.shields.io/badge/docs-live-b31b1b" alt="Docs">
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</p>

<p align="center">
<strong>The <u>prompts</u> for <strong>useReq/req</strong> project.</strong><br>
This repository maintains the prompt set in `src/prompts/` and the documentation templates in `src/docs/` used by the useReq SRS-driven workflow.
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> |
  <a href="#feature-highlights">Feature Highlights</a> |
  <a href="#prompts-and-agents">Prompts and Agents</a> |
  <a href="#templates">Templates</a> |
  <a href="#usage">Usage</a>
</p>

<p align="center">
<br>
🚧 <strong>DRAFT</strong>: 👾 Alpha Development 👾 - Work in Progress 🏗️ 🚧<br>
⚠️ <strong>IMPORTANT NOTICE</strong>: Created with <a href="https://github.com/Ogekuri/useReq"><strong>useReq/req</strong></a> 🤖✨ ⚠️<br>
<br>
<p>


## Feature Highlights
- Prompt catalog with 15 task-specialized prompt cards in `src/prompts/` for SRS-driven workflows (`Requirements -> Design -> Implementation -> Verification`).
- Every prompt declares a `description`, `argument-hint`, and `usage` gate to make prompt selection explicit and deterministic.
- Shared shell-safety contract across prompts: linear commands only, explicit option termination for `rg`/`git grep` patterns that start with `-`/`--`, and no substitution-based shell composition.
- Reusable templates in `src/docs/` for SRS authoring, HDT test authoring, and Doxygen-style source documentation.
- Included guideline set in `guidelines/` (Google Python/C++ style guides) for `%%GUIDELINES_FILES%%` integrations.
- Tag-driven release workflow publishes versioned prompt/template assets from `src/`.


## Prompts and Agents
| Prompt | Purpose | Argument Hint | Select when |
| --- | --- | --- | --- |
| `analyze` | Produce an analysis report. | `Description of the analysis/investigation to perform` | You need read-only investigation and structured evidence output. |
| `change` | Update requirements and implement corresponding changes. | `Description of the requirements changes to implement` | Existing requirement behavior must change (non-additive edits in `REQUIREMENTS.md`). |
| `check` | Run the requirements check. | `Optional: context to focus the audit (can be empty)` | You need requirement-by-requirement compliance audit without implementation edits. |
| `cover` | Cover uncovered existing requirements. | `Optional: context to focus coverage work (can be empty)` | Requirements are already defined and only minimal implementation deltas are needed for uncovered IDs. |
| `create` | Draft SRS from existing source code. | `No arguments utilized by the prompt logic (English only)` | Implementation exists and you must bootstrap/update `REQUIREMENTS.md` from code evidence. |
| `fix` | Fix a defect without changing requirements. | `Description of the defect/bug to fix` | Behavior is incorrect relative to existing requirements and must be restored. |
| `implement` | Implement source code from requirements. | `No arguments utilized by the prompt logic` | `REQUIREMENTS.md` is authoritative and you must build missing implementation/test coverage. |
| `new` | Add a new requirement and corresponding implementation. | `Description of the new requirement/feature to implement` | Requested behavior is additive and can be implemented by appending new requirement IDs. |
| `readme` | Align root `README.md` with implementation evidence. | `Description of additional edits to perform on README.md file` | Only user-facing README coverage must be updated from external interface evidence. |
| `recreate` | Reorganize and update SRS from source evidence. | `No arguments utilized by the prompt logic (English only)` | You must rewrite SRS structure while preserving existing IDs and optionally appending new IDs. |
| `refactor` | Optimize internals without requirement changes. | `Description of the refactor goal` | Internal maintainability/performance improvements are required without user-visible behavior changes. |
| `references` | Generate `REFERENCES.md` from source code. | `No arguments utilized by the prompt logic` | You need to regenerate symbol/reference index documentation only. |
| `renumber` | Renumber SRS requirement IDs deterministically. | `No arguments utilized by the prompt logic (English only)` | You need deterministic ID renumbering and internal cross-reference updates only. |
| `workflow` | Generate `WORKFLOW.md` from source code. | `No arguments utilized by the prompt logic` | You need runtime execution model documentation regeneration only. |
| `write` | Draft SRS from user request text. | `Description of the application to be drafted from scratch (English only)` | No authoritative implementation exists; requirements must be drafted directly from user intent. |


## Templates
| Template | Purpose | How it works |
| --- | --- | --- |
| `src/docs/Document_Source_Code_in_Doxygen_Style.md` | Source-code documentation standard. | Enforces LLM-native Doxygen output with mandatory tag taxonomy and full symbol coverage rules. |
| `src/docs/HDT_Test_Authoring_Guide.md` | Unit-test authoring standard. | Defines Generator/Refactorer modes, deterministic HDT constraints, and fixed artifact output order. |
| `src/docs/Requirements_Template.md` | SRS authoring template. | Defines RFC 2119-only requirement writing rules, stable requirement IDs, and canonical SRS section structure. |


## Quick Start

1. Clone this repository and keep it versioned alongside your useReq project.
2. Copy the required prompt files from `src/prompts/` into your target prompt installation path.
3. Copy required templates from `src/docs/` into your target docs/template installation path.
4. Copy guideline files from `guidelines/` when your prompt installation resolves `%%GUIDELINES_FILES%%`.
5. Ensure installation-time placeholders are preserved exactly:
   - `%%ARGS%%`
   - `%%DOC_PATH%%`
   - `%%GUIDELINES_FILES%%`
   - `%%SRC_PATHS%%`
   - `%%TEST_PATH%%`
6. Select the prompt that matches the task type and provide prompt arguments according to each prompt `argument-hint`.



## Usage

Use this repository as the canonical source for prompt/template maintenance.

- Follow each prompt `usage` gate before invocation; prompts are intentionally specialized and non-interchangeable.
- For prompts that perform repository modifications, keep the req worktree lifecycle and `req --git-check` flow unchanged.
- Release publication is automated by `.github/workflows/release-markdown.yml`: push a tag matching `v<major>.<minor>.<patch>` on `master` to generate changelog and publish `src/**/*` assets.
