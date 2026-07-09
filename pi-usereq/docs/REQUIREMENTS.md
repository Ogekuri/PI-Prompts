---
title: "Prompts Project Requirements"
description: Software requirements specification
version: "0.2.3"
date: "2026-04-14"
author: "req-write"
scope:
  paths:
    - "src/prompts/**/*.md"
    - "src/docs/**/*.md"
  excludes:
    - ".*/**"
visibility: "draft"
tags: ["srs", "prompts", "templates"]
---

# Prompts Project Requirements

## 1. Introduction

### 1.1 Document Rules
Prefix `DOC` is reserved for document-authoring constraints in this section.

- **DOC-001**: MUST write and maintain this document in English.
- **DOC-002**: MUST use only RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and MUST NOT use modal verbs outside that set in requirement statements.
- **DOC-003**: MUST express every requirement bullet using the canonical format `- **<ID>**: <RFC2119 keyword> <single-sentence requirement>.`.
- **DOC-004**: MUST keep requirement IDs unique and non-repurposed within each published revision, and MUST update internal cross-references deterministically when IDs are renumbered.
- **DOC-005**: MUST write requirements for LLM Agents and automated parsers using high semantic density and no conversational filler.

### 1.2 Project Scope
This project defines and maintains prompt and template artifacts used by the useReq process to enforce SRS-driven development with the sequence Requirements -> Design -> Implementation -> Verification.

### 1.3 Assumptions
- No application runtime source code is in scope for this SRS.
- No mandatory third-party runtime library was requested.
- Verification can be implemented with deterministic textual checks on Markdown artifacts.
- **CRITICAL**: Workflows that modify source code MUST execute unit tests during verification only when relevant unit tests already exist in the repository, selecting commands via language-specific test-suite priority policy; read-only workflows MUST rely on static evidence only.

### 1.4 Persona
- When you edit prompts and templates, act as a Senior AI Prompt Engineer and Senior LLM-Ops Engineer.
- When performing checks and tests on prompts and templates, act as a Senior AI Prompt Engineer, Senior LLM-Ops Engineer, and an expert static code analyst. Your task is to validate and review the provided prompts and templates.

### 1.5 Absolute Rules, Non-Negotiable
- When editing prompt or template artifacts:
  - MUST preserve placeholder tokens `%%ARGS%%`, `%%DOC_PATH%%`, `%%GUIDELINES_FILES%%`, `%%SRC_PATHS%%`, and `%%TEST_PATH%%` exactly as-is.
  - MUST keep all prompt/template text free of typographical and grammatical errors.
  - MUST use uniform terminology and identical canonical instruction phrasing for identical actions, references, and process keywords.
  - MUST keep interruption rules explicit: prompts MUST NOT interrupt agent reasoning flow unless the interruption is required by defined workflow conditions.
  - MUST optimize prompts/templates for LLM-agent parsing, context efficiency, and token economy.
  - MUST target prompts/templates to LLM-agent execution and MUST NOT target human-only reading.
  - MUST require an explicit change request and corresponding `docs/REQUIREMENTS.md` update for any prompt/template file addition or removal.
  - MUST keep `src/prompts/` and `src/docs/` free of governance instructions about maintaining, editing, or verifying prompts/templates.
  - MUST NOT add instructions that increase hallucination risk unless explicitly required by a formal requirement.

## 2. Project Requirements

### 2.1 Project Functions
- **PRJ-001**: MUST maintain prompt artifacts in `src/prompts/` for SRS-driven workflows.
- **PRJ-002**: MUST maintain template artifacts in `src/docs/` as mandatory authoring guides and keep template taxonomy aligned with prompt-level Doxygen coverage directives.
- **PRJ-003**: MUST define each prompt with a single primary workflow intent and deterministic output objective.
- **PRJ-004**: MUST preserve the process order Requirements -> Design -> Implementation -> Verification when editing prompt instructions.

### 2.3 In-Scope Artifacts
| Category | Path | Intended Function |
| --- | --- | --- |
| Prompt | `src/prompts/analyze.md` | Produce an analysis report. |
| Prompt | `src/prompts/change.md` | Update requirements and implement corresponding changes. |
| Prompt | `src/prompts/check.md` | Run requirements compliance checks. |
| Prompt | `src/prompts/cover.md` | Implement deltas that cover unmet requirements. |
| Prompt | `src/prompts/create.md` | Draft SRS from project source evidence. |
| Prompt | `src/prompts/fix.md` | Fix defects without changing requirements. |
| Prompt | `src/prompts/flowchart.md` | Draft `FLOWCHART.md` as a Mermaid flowchart from source evidence. |
| Prompt | `src/prompts/implement.md` | Implement code from requirements. |
| Prompt | `src/prompts/new.md` | Add new requirements and implement corresponding changes. |
| Prompt | `src/prompts/recreate.md` | Reorganize and renumber the SRS. |
| Prompt | `src/prompts/refactor.md` | Optimize internals without requirement changes. |
| Prompt | `src/prompts/references.md` | Draft `REFERENCES.md` from source evidence. |
| Prompt | `src/prompts/readme.md` | Update `README.md` from user-visible implementation evidence. |
| Prompt | `src/prompts/renumber.md` | Renumber SRS requirements deterministically. |
| Prompt | `src/prompts/workflow.md` | Draft `WORKFLOW.md` from source evidence. |
| Prompt | `src/prompts/write.md` | Draft SRS from user-request text. |
| Template | `src/docs/Document_Source_Code_in_Doxygen_Style.md` | Mandatory source-code documentation guideline. |
| Template | `src/docs/HDT_Test_Authoring_Guide.md` | Mandatory unit-test authoring guideline. |
| Template | `src/docs/Requirements_Template.md` | Mandatory SRS authoring guideline. |

## 3. Requirements

### 3.1 Design and Implementation
- **DES-001**: MUST organize artifacts into dedicated prompt and template with explicit responsibilities.
- **DES-002**: MUST standardize repeated operational instructions, including Git-state checks and completion or error messages, using identical wording across prompts and forbidding bell-control output suffixes, except prompt-name specialization.
- **DES-003**: MUST implement text-first interaction semantics and MUST NOT require GUI-specific behavior.
- **DES-004**: MUST preserve reusable keyword tokens exactly so installation-time substitution remains valid.

Proposed repository structure (max depth 3, depth 4 for `src/`):

```text
└── src/
    ├── docs/
    │   ├── Document_Source_Code_in_Doxygen_Style.md
    │   ├── HDT_Test_Authoring_Guide.md
    │   └── Requirements_Template.md
    └── prompts/
        ├── analyze.md
        ├── change.md
        ├── check.md
        ├── cover.md
        ├── create.md
        ├── fix.md
        ├── flowchart.md
        ├── implement.md
        ├── new.md
        ├── recreate.md
        ├── refactor.md
        ├── references.md
        ├── readme.md
        ├── renumber.md
        ├── workflow.md
        └── write.md
```

### 3.2 Common Requirements
- **REQ-001**: MUST define `analyze.md` to produce a read-only analysis report from available project artifacts.
- **REQ-002**: MUST define `change.md` to modify requirements and implement corresponding project changes in a single controlled workflow.
- **REQ-003**: MUST define `check.md` to evaluate requirement compliance and report requirement-level pass or fail outcomes.
- **REQ-004**: MUST define `cover.md` to implement focused deltas that satisfy explicitly uncovered requirement IDs.
- **REQ-005**: MUST define `create.md` to draft an SRS from repository evidence when source implementation already exists.
- **REQ-006**: MUST define `fix.md` to correct behavior defects without modifying requirement intent.
- **REQ-007**: MUST define `implement.md` to implement missing functionality from an authoritative SRS baseline.
- **REQ-008**: MUST define `new.md` to append strictly additive requirements and implement corresponding deltas.
- **REQ-009**: MUST define `recreate.md` to reorganize and NOT renumber an SRS while preserving requirement intent.
- **REQ-010**: MUST define `refactor.md` to improve internals while preserving externally observable behavior and requirement compliance.
- **REQ-011**: MUST define `references.md` to generate `REFERENCES.md` from source-code evidence only.
- **REQ-012**: MUST define `renumber.md` to enforce deterministic requirement ID sequencing in SRS documents.
- **REQ-013**: MUST define `workflow.md` to generate `WORKFLOW.md` from source-code execution evidence.
- **REQ-014**: MUST define `write.md` to generate an SRS from user-request text without relying on source-code evidence.
- **REQ-015**: MUST define `readme.md` to update root `README.md` from user-visible implementation evidence only.
- **REQ-016**: MUST define `flowchart.md` to generate `FLOWCHART.md` as a Mermaid flowchart of primary program flow from source-code evidence only.
- **REQ-017**: MUST validate placeholder tokens by allowing only `%%ARGS%%`, `%%DOC_PATH%%`, `%%GUIDELINES_FILES%%`, `%%SRC_PATHS%%`, and `%%TEST_PATH%%`, except artifacts that intentionally contain no placeholder tokens.
- **REQ-018**: MUST NOT contain typo and grammar errors, except fenced code blocks, inline-code spans, literal error strings, placeholders, and command snippets.
- **REQ-019**: MUST enforce canonical phrasing for shared operational instructions, including project-operation preference for `req` commands, `req --git-check`, `req --docs-check`, `req --get-base-path`, `req --git-path`, `req --git-wt-name`, `req --git-wt-create <WORKTREE_NAME>`, `req --git-wt-delete <WORKTREE_NAME>`, and the Source Code Analysis Toolkit four-pillar workflow ordering 1→2→3→4; when a workflow requires values retrieved from commands for later reuse, instructions MUST require literal `req` commands and simple sequential execution; worktree-generation instructions MUST explicitly require deriving `<BASE_PATH>` with `req --get-base-path` and `<GIT_PATH>` with `req --git-path` before generating `<WORKTREE_NAME>` with `req --git-wt-name`; instructions that execute `req --git-wt-create <WORKTREE_NAME>` MUST explicitly require `cd <GIT_PATH>/../<WORKTREE_NAME>` immediately after `req --git-wt-create <WORKTREE_NAME>` and before the next step; worktree-exit instructions MUST explicitly require deriving `<BASE_PATH>` with `req --get-base-path` when needed and executing `cd <BASE_PATH>` before merge instead of `req --git-wt-exit`; prompts that execute `req --git-wt-create <WORKTREE_NAME>` MUST include `## Pre-requisite: Execution Context` with `<WORKTREE_NAME>` generation via `req --git-wt-name`; prompts that do not execute `req --git-wt-create <WORKTREE_NAME>` MUST NOT include `<WORKTREE_NAME>`, `req --git-wt-name` generation instructions, or the `## Pre-requisite: Execution Context` section; every declared `Pre-requisite: Execution Context` section MUST explicitly require that all listed context information remains continuously available for the entire workflow and is never dropped, forgotten, or overwritten; final repository-cleanliness verification MUST use `req --git-check` and MUST NOT use `git status --porcelain`; after successful worktree creation, every early-termination branch before merge-phase cleanup MUST instruct only `req --git-wt-delete <WORKTREE_NAME>` for cleanup before termination and MUST NOT instruct `git restore .`, `git checkout .`, or `git clean -fd`; branches before the create step MUST NOT instruct `req --git-wt-delete <WORKTREE_NAME>`; and the create-failure branch for `req --git-wt-create <WORKTREE_NAME>` MUST NOT instruct `req --git-wt-delete <WORKTREE_NAME>`.
- **REQ-020**: MUST require prompt instructions that generate shell commands to emit only linear commands compatible with restrictive filtering systems.
- **REQ-021**: MUST optimize prompts/templates for parser efficiency and token economy, except mandatory compliance blocks (`Professional Personas`, `Execution Protocol`, `Execution Directives`, `Steps`) that are retained verbatim.
- **REQ-022**: MUST optimize prompts/templates for LLM-agent execution and MUST require the `## Professional Personas` section to include `Prompt Engineer and LLM Optimization Specialist` for prompt, agent, skill, and LLM-targeted document work.
- **REQ-023**: MUST use identical canonical instruction phrasing for identical actions across prompts, outside explicitly prompt specifications, except where explicitly allowed below.
  - Workflow identity literals MAY vary where required to bind the emitting prompt (`/req-<name>`, commit-type prefix, workflow-specific title/scope text, and step labels tied to workflow intent).
  - Workflow-scoped failure or warning strings MAY vary only in workflow-name specialization while preserving the same control action pattern (`OUTPUT exactly "<STRING>"`, then terminate or override final line as explicitly defined).
  - Numeric bounds and scoped nouns MAY vary when they encode workflow-specific semantics (for example step-count cardinality and requirement-type nouns), while shared operational commands MUST remain byte-identical.
- **REQ-024**: MUST avoid instructions that cause unnecessary token-heavy content, except where explicitly allowed below.
  - Mandatory compliance blocks MAY remain verbose when retained verbatim by policy (`Professional Personas`, `Execution Protocol`, `Execution Directives`, and `Steps`).
  - Canonical executable literals MAY remain fully expanded where determinism depends on exact text (shell commands, fixed report schema, fixed error strings, and WORKFLOW.md schema contracts).
  - High-detail enumerations MAY be used only when they constrain behavior and reduce ambiguity (supported tag sets, allowed temp/cache paths, and explicit termination-condition matrices).
- **REQ-025**: MUST reject unauthorized chain-interrupt instructions outside explicitly defined workflow interruption points, except where explicitly allowed below.
  - Authorized interruption points are only explicit Step branches that require exact-string output without bell-control suffixes and immediate stop/override (git-status failure, required-file absence, incompatibility guards, test-loop exhaustion, and no-op commit termination).
  - Any authorized interruption branch that executes after successful `req --git-wt-create <WORKTREE_NAME>` and before merge-phase cleanup MUST include explicit `req --git-wt-delete <WORKTREE_NAME>` cleanup instruction before termination and MUST NOT include rollback or revert instructions (`git restore .`, `git checkout .`, `git clean -fd`).
  - The interruption branch triggered by failure of `req --git-wt-create <WORKTREE_NAME>` MUST NOT include `req --git-wt-delete <WORKTREE_NAME>`.
  - Any branch in step positions before the first `req --git-wt-create <WORKTREE_NAME>` in the same prompt MUST NOT include `req --git-wt-delete <WORKTREE_NAME>`; prompts without create step MUST NOT include `req --git-wt-delete <WORKTREE_NAME>`.
  - Read-only or coverage workflows MAY emit a declared no-change terminal string when explicitly defined by that workflow step (for example "All requirements are already covered. No changes needed.").
  - Merge-conflict handling MAY override only the final status line with the predefined warning string, without adding new interruption branches.
- **REQ-026**: MUST reject new hallucination-risk instructions, except where explicitly allowed below.
  - Evidence-first high-recall directives MAY remain when uncertainty is explicitly downgraded to candidates and never asserted as complete without file-backed proof.
  - Autonomous disambiguation directives MAY remain only when constrained to least-invasive choices anchored to repository evidence and requirement traceability.
  - Tool-gated execution directives MAY require waiting for actual tool responses and exact-string outputs to prevent fabricated results.
- **REQ-027**: MUST ensure each prompt YAML header `usage` value is generated with length less than or equal to 1024 characters.
- **REQ-028**: MUST treat `req --here --static-check` as successful when output contains `Error: no source files found in configured directories.` because configured source directories are intentionally empty in this project.
- **REQ-029**: MUST require prompt instructions that generate shell commands to avoid command substitution (`$()` or backticks), complex variable expansion, nested substitution, shell-derived helper composition, nested shell logic, and nested pipelines.
- **REQ-030**: MUST require shell-command instructions to apply safe literal-argument handling and to use explicit option termination for `rg` and `git grep` patterns beginning with `-` or `--`.
- **REQ-031**: MUST require `rg` and `git grep` search patterns beginning with `-` or `--` to avoid reliance on quoting or backslash escaping alone.

### 3.3 Prompt's Specific Requirements

#### 3.3.1 Analyze Prompt

##### Context Requirements
- **ANZ-CTX-001**: MUST define the `## Purpose` section to instruct: Enable evidence-backed reasoning about a request or investigation by grounding conclusions in the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`), the runtime/workflow model (`%%DOC_PATH%%/WORKFLOW.md`), references (`%%DOC_PATH%%/REFERENCES.md`), and the actual implementation, so downstream LLM Agents MUST choose the correct follow-up workflow with minimal re-discovery.
- **ANZ-CTX-002**: MUST define the `## Scope` section to instruct: In scope: read-only analysis of the above documents plus source under %%SRC_PATHS%% (and tests only as evidence when explicitly needed), including tool-assisted extraction; output is an analysis report with concrete evidence (paths/line numbers); Out of scope: any repository modification (requirements/code/tests/docs), generating patches, or applying fixes.
- **ANZ-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code and directory structures to understand the system's architecture and logic; Act as a Business Analyst when cross-referencing code findings with `%%DOC_PATH%%/REQUIREMENTS.md` to ensure functional alignment; Act as a Technical Writer when producing the final analysis report or workflow descriptions, ensuring clarity, technical precision, and structured formatting; Act as a QA Auditor when reporting facts, requiring concrete evidence (file paths, line numbers) for every finding; Act as an Expert Debugger when you identify a failure symptom with concrete evidence (failure evidence, stack trace, reproducible output); Only explain the root cause, not propose or implement fixes; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **ANZ-CTX-004**: MUST define the `## Behavior` section to instruct: Only analyze the code and present the results; make no changes; Do NOT create or modify tests in this workflow; Report facts: for each finding include file paths and, when useful, line numbers or short code excerpts; Allowed git commands in this workflow (read-only only): `git status`, `git diff`, `git ls-files`, `git grep`, `git rev-parse`, `git branch --show-current`; Do NOT run any other git commands; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read files as needed (read-only only; eg, `cat`, `sed -n`, `head`, `tail`, `rg`, `less`); Do NOT use in-place editing flags (eg, `-i`, `perl -pi`) in this workflow.

##### Steps Requirements
- **ANZ-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **ANZ-STP-002**: MUST define Step 2 to instruct: Analyze the [User Request](#users-request) and present a human-readable analysis report using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.2 Change Prompt

##### Context Requirements
- **CHG-CTX-001**: MUST define the `## Purpose` section to instruct: Evolve existing system behavior safely by first updating the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) to encode the requested change, then implementing and verifying the corresponding code/test deltas with strict traceability to requirement IDs so downstream LLM Agents MUST reason over the change deterministically.
- **CHG-CTX-002**: MUST define the `## Scope` section to instruct: In scope: patch-style edits to `%%DOC_PATH%%/REQUIREMENTS.md`, an implementation plan, code/test changes under %%SRC_PATHS%% and %%TEST_PATH%%, verification via static analysis, requirements evidence checks, and conditional execution of existing unit tests using language-specific test-suite priority policy, and updates to `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, ending with a clean git commit; Out of scope: work that keeps requirements unchanged (use `/req-fix`, `/req-refactor`, or `/req-cover`), and any implementation not justified by the updated requirements.
- **CHG-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Business Analyst when generating Requirement Delta and during requirements analysis and update: your priority is requirement integrity, atomic description of changes, and ensuring no logical conflicts in `%%DOC_PATH%%/REQUIREMENTS.md`; Act as a Senior System Architect when generating the Implementation Delta: translate requirements into a robust, modular, and non-breaking technical implementation plan; Act as a Senior Software Developer during implementation: implement the planned changes with high-quality, idiomatic code that maps strictly to Requirement IDs; Act as a QA Engineer during verification and testing: verify compliance with zero leniency, using mandatory code evidence and strict fix loops based on static-analysis findings to ensure stability; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **CHG-CTX-004**: MUST define the `## Behavior` section to instruct: Propose changes based only on the requirements, user request, and repository evidence; Every proposed code change MUST reference at least one requirement ID or explicit text in user request; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as the primary technical inputs; keep decisions traceable to requirements and repository evidence; All newly written or edited content MUST be in English; Do NOT translate existing text outside the minimal change surface required by this workflow; if you detect non-English text elsewhere, report it in Evidence instead of rewriting it; Prefer clean implementation over legacy support; Do not add backward compatibility UNLESS the updated requirements explicitly mandate it; Do not implement migrations/auto-upgrades UNLESS the updated requirements explicitly include a migration/upgrade requirement; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ); Prefer read-only commands for analysis.

##### Steps Requirements
- **CHG-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **CHG-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **CHG-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **CHG-STP-004**: MUST define Step 4 to instruct: Generate and apply the Requirement Delta to change requirements.
- **CHG-STP-005**: MUST define Step 5 to instruct: Generate Design Delta and implement the Implementation Delta according to the Requirement Delta.
- **CHG-STP-006**: MUST define Step 6 to instruct: Generate Verification Delta by auditing ALL requirements with progressive-disclosure evidence (OK pointer-only, FAIL full), verifying static-analysis results, running existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **CHG-STP-007**: MUST define Step 7 to instruct: Update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **CHG-STP-008**: MUST define Step 8 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **CHG-STP-009**: MUST define Step 9 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **CHG-STP-010**: MUST define Step 10 to instruct: CRITICAL: Merge Conflict Management.
- **CHG-STP-011**: MUST define Step 11 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.3 Check Prompt

##### Context Requirements
- **CHK-CTX-001**: MUST define the `## Purpose` section to instruct: Provide an evidence-backed compliance audit by running static analysis and mapping every requirement in the SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) to concrete implementation evidence, so downstream LLM Agents MUST decide whether coverage work is required and where to apply it.
- **CHK-CTX-002**: MUST define the `## Scope` section to instruct: In scope: read `%%DOC_PATH%%/REQUIREMENTS.md` (and related docs), run static analysis evidence (`req --here --static-check`) as evidence, mark ALL requirements as OK/FAIL with proof, and (only when FAILs exist) produce an implementation-only, patch-oriented technical report; Out of scope: any file modification (requirements/code/tests/docs) or applying fixes.
- **CHK-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code and directory structures to understand the system's architecture and logic; Act as a Business Analyst when cross-referencing code findings with `%%DOC_PATH%%/REQUIREMENTS.md` to ensure functional alignment; Act as a Technical Writer when producing the final analysis report or workflow descriptions, ensuring clarity, technical precision, and structured formatting; Act as a QA Auditor when reporting facts, requiring concrete evidence (file paths, line numbers) for every finding; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **CHK-CTX-004**: MUST define the `## Behavior` section to instruct: Only analyze the code and static-analysis execution results and present the results; make no changes; Do NOT create or modify tests in this workflow; Report facts: for each finding include file paths and, when useful, line numbers or short code excerpts; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read files as needed (read-only only; eg, `cat`, `sed -n`, `head`, `tail`, `rg`, `less`).

##### Steps Requirements
- **CHK-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **CHK-STP-002**: MUST define Step 2 to instruct: Run static analysis (`req --here --static-check`), check requirements coverage and generate Implementation Delta.
- **CHK-STP-003**: MUST define Step 3 to instruct: Present results and Implementation Delta for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.4 Cover Prompt

##### Context Requirements
- **COV-CTX-001**: MUST define the `## Purpose` section to instruct: Close coverage gaps by implementing the missing behaviors for uncovered requirement IDs in the existing codebase, so the implementation becomes fully compliant with the current SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) without changing that SRS.
- **COV-CTX-002**: MUST define the `## Scope` section to instruct: In scope: identify uncovered requirement IDs, implement minimal code changes under %%SRC_PATHS%%, add/adjust tests under %%TEST_PATH%% as needed, run verification with static analysis plus conditional execution of existing unit tests using language-specific test-suite priority policy, update `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and commit; Out of scope: editing `%%DOC_PATH%%/REQUIREMENTS.md`, introducing new requirements/features, or performing large-scale rewrites (use `/req-implement` for “from scratch” rebuilds).
- **COV-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a QA Automation Engineer when identifying uncovered requirements: you must prove the lack of coverage through code analysis or static-analysis evidence gaps; Act as a Business Analyst when mapping requirement IDs from `%%DOC_PATH%%/REQUIREMENTS.md` to observable behaviors; Act as a Senior System Architect when generating the Implementation Delta and planning the coverage strategy: ensure the new implementation integrates perfectly with the existing architecture without regressions; Act as a Senior Software Developer when implementing the missing logic: focus on satisfying the Requirement IDs previously marked as uncovered; Act as a QA Engineer during verification and testing Steps: verify compliance with zero leniency, using mandatory code evidence and strict fix loops based on static-analysis findings to ensure stability; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **COV-CTX-004**: MUST define the `## Behavior` section to instruct: Do not modify `%%DOC_PATH%%/REQUIREMENTS.md`; Always strictly respect requirements; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as the primary technical inputs; keep decisions traceable to requirements and repository evidence; All newly written or edited content MUST be in English; Do NOT translate existing text outside the minimal change surface required by this workflow; if you detect non-English text elsewhere, report it in Evidence instead of rewriting it; Prioritize backward compatibility; Do not introduce breaking changes; preserve existing interfaces, data formats, and features; If maintaining compatibility MUST require migrations/auto-upgrades conversion logic, report the conflict instead of implementing, and then terminate the execution; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ); Prefer read-only commands for analysis.

##### Steps Requirements
- **COV-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **COV-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **COV-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **COV-STP-004**: MUST define Step 4 to instruct: Check requirements coverage, generate Design Delta and implement the Implementation Delta to cover uncovered requirements.
- **COV-STP-005**: MUST define Step 5 to instruct: Generate Verification Delta by running static analysis (`req --here --static-check`), executing existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **COV-STP-006**: MUST define Step 6 to instruct: Update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **COV-STP-007**: MUST define Step 7 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **COV-STP-008**: MUST define Step 8 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **COV-STP-009**: MUST define Step 9 to instruct: CRITICAL: Merge Conflict Management.
- **COV-STP-010**: MUST define Step 10 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.5 Create Prompt

##### Context Requirements
- **CRT-CTX-001**: MUST define the `## Purpose` section to instruct: Bootstrap an SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) from repository evidence so downstream LLM Agents MUST start SRS-driven work grounded in what the code actually does (requirements → design → implementation → verification), without guessing undocumented behavior.
- **CRT-CTX-002**: MUST define the `## Scope` section to instruct: In scope: static analysis of source under %%SRC_PATHS%% (and targeted tests only as evidence when needed) to create/update `%%DOC_PATH%%/REQUIREMENTS.md` in English; Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.
- **CRT-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when analyzing source code to infer behavior: ensure every software requirement generated is atomic, unambiguous, and empirically testable; Act as a Technical Writer when structuring the SRS document `%%DOC_PATH%%/REQUIREMENTS.md`: use RFC 2119 keywords exclusively (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and never use the forbidden non-RFC modal verb; maintain a clean, hierarchical Markdown structure with a maximum depth of 3 levels; Act as a Business Analyst when verifying the "True State": ensure the draft accurately reflects implemented logic, including limitations or bugs.
- **CRT-CTX-004**: MUST define the `## Behavior` section to instruct: Write the document in English; Do not perform unrelated edits; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ), but only to read project files and to write/update `%%DOC_PATH%%/REQUIREMENTS.md`; Avoid in-place edits on any other path; Prefer read-only commands for analysis.

##### Steps Requirements
- **CRT-STP-001**: MUST define Step 1 to instruct: Generate the Software Requirements Specification.
- **CRT-STP-002**: MUST define Step 2 to instruct: Validate the Software Requirements Specification.
- **CRT-STP-003**: MUST define Step 3 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.6 Fix Prompt

##### Context Requirements
- **FIX-CTX-001**: MUST define the `## Purpose` section to instruct: Restore required behavior by diagnosing and fixing a defect while keeping the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) unchanged, so downstream LLM Agents MUST treat the fix as a semantics-correcting change rather than a requirements change.
- **FIX-CTX-002**: MUST define the `## Scope` section to instruct: In scope: reproduce/triage defects with concrete evidence and, when relevant unit-test suites exist, prefer a test-first defect flow (create one failing reproducer unit test -> design smallest safe fix -> implement -> verify reproducer pass), then verify with requirement evidence plus static analysis and conditional execution of existing unit tests using language-specific test-suite priority policy, update `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and commit; Out of scope: editing requirements, adding new features, or unnecessary refactors.
- **FIX-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as an Expert Debugger when diagnosing defects: you MUST identify the failure symptom with concrete evidence (failure evidence, stack trace) before proposing the fix; Act as a Senior Software Developer when implementing a defect fix: apply the smallest safe change that restores required behavior while preserving public interfaces; Act as a Business Analyst when reading `%%DOC_PATH%%/REQUIREMENTS.md` to ensure that fixes or refactors never violate or change existing documented behaviors; Act as a QA Automation Engineer when validating the fix/refactor: ensure that static-analysis results are clean (or no-source positive) and no regressions in documented behavior are introduced; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **FIX-CTX-004**: MUST define the `## Behavior` section to instruct: Do not modify `%%DOC_PATH%%/REQUIREMENTS.md`; Always strictly respect requirements; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as primary inputs; keep decisions traceable to requirement evidence; when relevant unit-test suites exist, prefer analyze defect -> create one failing reproducer unit test -> design and implement smallest safe fix -> verify reproducer passes plus requirement evidence and `req --here --static-check`; use analyze -> implement -> verify fallback only when no relevant suite exists or one-test isolation is infeasible; if output is exactly `Error: no source files found in configured directories.`, treat verification as successful; All newly written or edited content MUST be in English; Do NOT translate unrelated existing text; preserve backward compatibility unless requirements explicitly change it; report migration conflicts instead of implementing them; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ); Prefer read-only commands for analysis.

##### Steps Requirements
- **FIX-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **FIX-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **FIX-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **FIX-STP-004**: MUST define Step 4 to instruct: Read requirements, analyze defect evidence, and when relevant unit-test suites exist create one failing reproducer unit test before designing and implementing the smallest safe fix.
- **FIX-STP-005**: MUST define Step 5 to instruct: Generate Verification Delta by auditing ALL requirements with progressive-disclosure evidence (OK pointer-only, FAIL full), verifying defect resolution with requirement evidence plus `req --here --static-check`, running existing unit tests with language-specific priority policy, explicitly confirming reproducer-unit-test success when created, and implementing needed bug fixes.
- **FIX-STP-006**: MUST define Step 6 to instruct: Update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **FIX-STP-007**: MUST define Step 7 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **FIX-STP-008**: MUST define Step 8 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **FIX-STP-009**: MUST define Step 9 to instruct: CRITICAL: Merge Conflict Management.
- **FIX-STP-010**: MUST define Step 10 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.
- **FIX-STP-011**: MUST define Step 4 incompatibility branch to output a three-column requirement-conflict table (`Requirement ID`, `Conflicting Excerpt`, `Conflict Reason + Interrupted Implementation Intent`) before emitting the exact error string and terminating.

#### 3.3.7 Implement Prompt

##### Context Requirements
- **IMP-CTX-001**: MUST define the `## Purpose` section to instruct: Produce a working implementation from the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) by building missing functionality end-to-end (including “from scratch” where needed), so the codebase becomes fully compliant with the documented requirement IDs without changing those requirements.
- **IMP-CTX-002**: MUST define the `## Scope` section to instruct: In scope: read `%%DOC_PATH%%/REQUIREMENTS.md`, implement/introduce source under %%SRC_PATHS%% (including new modules/files), add tests under %%TEST_PATH%%, verify via static analysis and conditional execution of existing unit tests using language-specific test-suite priority policy, update `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and commit; Out of scope: editing requirements or introducing features not present in the SRS (use `/req-change` or `/req-new` to evolve requirements first).
- **IMP-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a QA Automation Engineer when identifying uncovered requirements: you must prove the lack of coverage through code analysis or static-analysis evidence gaps; Act as a Business Analyst when mapping requirement IDs from `%%DOC_PATH%%/REQUIREMENTS.md` to observable behaviors; Act as a Senior System Architect when generating the Implementation Delta and planning the coverage strategy: ensure the new implementation integrates perfectly with the existing architecture without regressions; Act as a Senior Software Developer when implementing the missing logic: focus on satisfying the Requirement IDs previously marked as uncovered; Act as a QA Engineer during verification and testing Steps: verify compliance with zero leniency, using mandatory code evidence and strict fix loops based on static-analysis findings to ensure stability; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **IMP-CTX-004**: MUST define the `## Behavior` section to instruct: Do not modify `%%DOC_PATH%%/REQUIREMENTS.md`; Always strictly respect requirements; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as the primary technical inputs; keep decisions traceable to requirements and repository evidence; All newly written or edited content MUST be in English; Do NOT translate existing text outside the minimal change surface required by this workflow; if you detect non-English text elsewhere, report it in Evidence instead of rewriting it; Prioritize backward compatibility; Do not introduce breaking changes; preserve existing interfaces, data formats, and features; If maintaining compatibility MUST require migrations/auto-upgrades conversion logic, report the conflict instead of implementing, and then terminate the execution; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ); Prefer read-only commands for analysis.

##### Steps Requirements
- **IMP-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **IMP-STP-002**: MUST define Step 2 to instruct: CRITICAL: Worktree Generation & Isolation.
- **IMP-STP-003**: MUST define Step 3 to instruct: Read requirements, generate Design Delta and implement the Implementation Delta to cover all requirements.
- **IMP-STP-004**: MUST define Step 4 to instruct: Generate Verification Delta by running static analysis (`req --here --static-check`), executing existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **IMP-STP-005**: MUST define Step 5 to instruct: Static analysis: build the runtime model from %%SRC_PATHS%%.
- **IMP-STP-006**: MUST define Step 6 to instruct: Generate and overwrite `%%DOC_PATH%%/WORKFLOW.md` document using declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **IMP-STP-007**: MUST define Step 7 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **IMP-STP-008**: MUST define Step 8 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **IMP-STP-009**: MUST define Step 9 to instruct: CRITICAL: Merge Conflict Management.
- **IMP-STP-010**: MUST define Step 10 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.8 New Prompt

##### Context Requirements
- **NEW-CTX-001**: MUST define the `## Purpose` section to instruct: Introduce a new, backwards-compatible capability by first extending the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) with the new requirement(s), then implementing and verifying the corresponding code/test changes with strict traceability to requirement IDs so downstream LLM Agents MUST reason over the new feature deterministically.
- **NEW-CTX-002**: MUST define the `## Scope` section to instruct: In scope: patch-style updates to `%%DOC_PATH%%/REQUIREMENTS.md` that add the new feature requirements, an implementation plan, code/test changes under %%SRC_PATHS%% and %%TEST_PATH%%, verification via static analysis, requirements evidence checks, and conditional execution of existing unit tests using language-specific test-suite priority policy, updates to `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and a clean git commit; Out of scope: breaking changes, migrations/compatibility conversions, or any feature work not captured as explicit requirements (report conflicts and terminate per prompt rules).
- **NEW-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Business Analyst when generating Requirement Delta and during requirements analysis and update: your priority is requirement integrity, atomic description of changes, and ensuring no logical conflicts in `%%DOC_PATH%%/REQUIREMENTS.md`; Act as a Senior System Architect when generating the Implementation Delta: translate requirements into a robust, modular, and non-breaking technical implementation plan; Act as a Senior Software Developer during implementation: implement the planned changes with high-quality, idiomatic code that maps strictly to Requirement IDs; Act as a QA Engineer during verification and testing: verify compliance with zero leniency, using mandatory code evidence and strict fix loops based on static-analysis findings to ensure stability; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **NEW-CTX-004**: MUST define the `## Behavior` section to instruct: Propose changes based only on the requirements, user request, and repository evidence; Every proposed code change MUST reference at least one requirement ID or explicit text in user request; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as the primary technical inputs; keep decisions traceable to requirements and repository evidence; All newly written or edited content MUST be in English; Do NOT translate existing text outside the minimal change surface required by this workflow; if you detect non-English text elsewhere, report it in Evidence instead of rewriting it; Prioritize backward compatibility; Do not introduce breaking changes; preserve existing interfaces, data formats, and features; If maintaining compatibility MUST require migrations/auto-upgrades conversion logic, report the conflict instead of implementing, and then terminate the execution; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ); Prefer read-only commands for analysis.

##### Steps Requirements
- **NEW-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **NEW-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **NEW-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **NEW-STP-004**: MUST define Step 4 to instruct: Generate and apply the Requirement Delta to cover new requirements.
- **NEW-STP-005**: MUST define Step 5 to instruct: Generate Design Delta and implement the Implementation Delta according to the Requirement Delta.
- **NEW-STP-006**: MUST define Step 6 to instruct: Generate Verification Delta by auditing ALL requirements with progressive-disclosure evidence (OK pointer-only, FAIL full), verifying static-analysis results, running existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **NEW-STP-007**: MUST define Step 7 to instruct: Update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **NEW-STP-008**: MUST define Step 8 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **NEW-STP-009**: MUST define Step 9 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **NEW-STP-010**: MUST define Step 10 to instruct: CRITICAL: Merge Conflict Management.
- **NEW-STP-011**: MUST define Step 11 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.9 ReCreate Prompt

##### Context Requirements
- **RCR-CTX-001**: MUST define the `## Purpose` section to instruct: Rebuild and reorganize the SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) from repository evidence while preserving all existing requirement IDs so downstream LLM Agents MUST rely on a clean structure and stable traceability when driving subsequent design/implementation work.
- **RCR-CTX-002**: MUST define the `## Scope` section to instruct: In scope: static analysis of source under %%SRC_PATHS%% (and targeted tests only as evidence when needed) to rewrite `%%DOC_PATH%%/REQUIREMENTS.md` in English, allowing reorganization and additions, but forbidding any renumbering/renaming of existing requirement IDs; Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.
- **RCR-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when analyzing source code to infer behavior: ensure every software requirement generated is atomic, unambiguous, and empirically testable; Act as a Technical Writer when structuring the SRS document `%%DOC_PATH%%/REQUIREMENTS.md`: use RFC 2119 keywords exclusively (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and never use the forbidden non-RFC modal verb; maintain a clean, hierarchical Markdown structure with a maximum depth of 3 levels; Act as a Business Analyst when verifying the "True State": ensure the draft accurately reflects implemented logic, including limitations or bugs; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **RCR-CTX-004**: MUST define the `## Behavior` section to instruct: Write the document in English; Do not perform unrelated edits; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ), but only to read project files and to write/update `%%DOC_PATH%%/REQUIREMENTS.md`; Avoid in-place edits on any other path; Prefer read-only commands for analysis.

##### Steps Requirements
- **RCR-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **RCR-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **RCR-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **RCR-STP-004**: MUST define Step 4 to instruct: Generate the Software Requirements Specification.
- **RCR-STP-005**: MUST define Step 5 to instruct: Validate the Software Requirements Specification.
- **RCR-STP-006**: MUST define Step 6 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **RCR-STP-007**: MUST define Step 7 to instruct: CRITICAL: Merge Conflict Management.
- **RCR-STP-008**: MUST define Step 8 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.10 Refactor Prompt

##### Context Requirements
- **RFR-CTX-001**: MUST define the `## Purpose` section to instruct: Improve maintainability, structure, and/or performance while strictly preserving externally observable behavior and keeping the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) unchanged, so downstream LLM Agents MUST treat the refactor as a semantics-preserving transformation.
- **RFR-CTX-002**: MUST define the `## Scope` section to instruct: In scope: internal refactors under %%SRC_PATHS%% (including private API reshaping) that preserve public interfaces/data formats, optional test adjustments only when objectively incorrect, verification via static analysis, requirements evidence checks, and conditional execution of existing unit tests using language-specific test-suite priority policy, updates to `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and a clean git commit; Out of scope: editing requirements, introducing new features, or making intentional behavioral changes (use `/req-change` or `/req-new`).
- **RFR-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Software Developer when refactoring: prioritize clean internal logic and performance while strictly preserving public interfaces and backward compatibility; Act as a Business Analyst when reading `%%DOC_PATH%%/REQUIREMENTS.md` to ensure that fixes or refactors never violate or change existing documented behaviors; Act as a QA Automation Engineer when validating the fix/refactor: ensure that static-analysis results are clean (or no-source positive) and no regressions in documented behavior are introduced; Act as an Expert Debugger only if tests fail or a defect emerges during refactor; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **RFR-CTX-004**: MUST define the `## Behavior` section to instruct: Always strictly respect requirements; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as the primary technical inputs; keep decisions traceable to requirements and repository evidence; All newly written or edited content MUST be in English; Do NOT translate existing text outside the minimal change surface required by this workflow; if you detect non-English text elsewhere, report it in Evidence instead of rewriting it; Prioritize clean implementation of internal logic; You are encouraged to refactor internals and private APIs freely to achieve refactor goals; However, you MUST strictly preserve all public interfaces, data formats, and externally observable behaviors; Do not maintain backward compatibility for internal/private components (ie, remove legacy internal code), but ensure strict backward compatibility for the public API; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ); Prefer read-only commands for analysis.

##### Steps Requirements
- **RFR-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **RFR-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **RFR-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **RFR-STP-004**: MUST define Step 4 to instruct: Generate Design Delta and implement the Implementation Delta to implement the refactor.
- **RFR-STP-005**: MUST define Step 5 to instruct: Generate Verification Delta by running static analysis (`req --here --static-check`), executing existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **RFR-STP-006**: MUST define Step 6 to instruct: Update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **RFR-STP-007**: MUST define Step 7 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **RFR-STP-008**: MUST define Step 8 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **RFR-STP-009**: MUST define Step 9 to instruct: CRITICAL: Merge Conflict Management.
- **RFR-STP-010**: MUST define Step 10 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.11 References Prompt

##### Context Requirements
- **REF-CTX-001**: MUST define the `## Purpose` section to instruct: Maintain a machine-usable reference index (`%%DOC_PATH%%/REFERENCES.md`) derived from repository evidence so downstream LLM Agents MUST quickly discover entrypoints, modules, dependencies, and other navigational anchors during SRS-driven work.
- **REF-CTX-002**: MUST define the `## Scope` section to instruct: In scope: generate/update only `%%DOC_PATH%%/REFERENCES.md` in English (following the prompt’s `req --references` workflow) and commit that doc change; Out of scope: changes to requirements, workflow docs, source code, or tests.
- **REF-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code and directory structures to understand the system's architecture and logic; Act as a Technical Writer when producing the final reference index, ensuring clarity, technical precision, and structured formatting; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **REF-CTX-004**: MUST define the `## Behavior` section to instruct: Do not perform unrelated edits; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ), but only to read project files and to write/update `%%DOC_PATH%%/REFERENCES.md`; Avoid in-place edits on any other path; Prefer read-only commands for analysis.

##### Steps Requirements
- **REF-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **REF-STP-002**: MUST define Step 2 to instruct: CRITICAL: Worktree Generation & Isolation.
- **REF-STP-003**: MUST define Step 3 to instruct: Update `%%DOC_PATH%%/REFERENCES.md` references file.
- **REF-STP-004**: MUST define Step 4 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **REF-STP-005**: MUST define Step 5 to instruct: CRITICAL: Merge Conflict Management.
- **REF-STP-006**: MUST define Step 6 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.12 Renumber Prompt

##### Context Requirements
- **RNB-CTX-001**: MUST define the `## Purpose` section to instruct: Deterministically renumber requirement IDs in `%%DOC_PATH%%/REQUIREMENTS.md` to produce a clean, progressive numbering scheme while preserving the exact requirement text and document order so downstream LLM Agents MUST rely on stable, sequential identifiers.
- **RNB-CTX-002**: MUST define the `## Scope` section to instruct: In scope: renumbering requirement identifiers in `%%DOC_PATH%%/REQUIREMENTS.md` in document order and updating internal cross-references to those identifiers, without modifying any requirement text, headings, or ordering; Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.
- **RNB-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when analyzing source code to infer behavior: ensure every software requirement generated is atomic, unambiguous, and empirically testable; Act as a Technical Writer when structuring the SRS document `%%DOC_PATH%%/REQUIREMENTS.md`: use RFC 2119 keywords exclusively (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and never use the forbidden non-RFC modal verb; maintain a clean, hierarchical Markdown structure with a maximum depth of 3 levels; Act as a Business Analyst when verifying the "True State": ensure the draft accurately reflects implemented logic, including limitations or bugs; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **RNB-CTX-004**: MUST define the `## Behavior` section to instruct: Write the document in English; Do not perform unrelated edits; Do NOT change any requirement content or document structure; only change requirement IDs and requirement-ID cross-references; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ), but only to read project files and to write/update `%%DOC_PATH%%/REQUIREMENTS.md`; Avoid in-place edits on any other path; Prefer read-only commands for analysis.

##### Steps Requirements
- **RNB-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **RNB-STP-002**: MUST define Step 2 to instruct: CRITICAL: Check `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md` file presence.
- **RNB-STP-003**: MUST define Step 3 to instruct: CRITICAL: Worktree Generation & Isolation.
- **RNB-STP-004**: MUST define Step 4 to instruct: CRITICAL: Renumber requirement IDs in the Software Requirements Specification.
- **RNB-STP-005**: MUST define Step 5 to instruct: Validate the Software Requirements Specification.
- **RNB-STP-006**: MUST define Step 6 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **RNB-STP-007**: MUST define Step 7 to instruct: CRITICAL: Merge Conflict Management.
- **RNB-STP-008**: MUST define Step 8 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.13 Workflow Prompt

##### Context Requirements
- **WFL-CTX-001**: MUST define the `## Purpose` section to instruct: Maintain an LLM-oriented runtime/workflow model (`%%DOC_PATH%%/WORKFLOW.md`) derived from repository evidence so downstream LLM Agents MUST reason about execution units, communication edges, and internal call-traces during SRS-driven design/implementation.
- **WFL-CTX-002**: MUST define the `## Scope` section to instruct: In scope: static analysis of source under %%SRC_PATHS%% to generate/overwrite only `%%DOC_PATH%%/WORKFLOW.md` in English only, following the mandated schema, then commit that doc change; Out of scope: changes to requirements, references, source code, or tests.
- **WFL-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code; your primary goal is to trace the execution flow (call stack) across files and modules, identifying exactly how data and control move from one function to another; Act as a Business Analyst when cross-referencing code findings with `%%DOC_PATH%%/REQUIREMENTS.md` to ensure functional alignment; Act as a Technical Writer when producing the final analysis report or workflow descriptions, ensuring clarity, technical precision, and structured formatting; Act as a QA Auditor when reporting facts, requiring concrete evidence as declaration file paths only (excluding line numbers and line ranges) for every finding; Act as an Expert GitOps Engineer when executing git workflows, especially when creating/removing/managing git worktrees to isolate changes safely.
- **WFL-CTX-004**: MUST define the `## Behavior` section to instruct: Write the `%%DOC_PATH%%/WORKFLOW.md` document in English; Do not perform unrelated edits; If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`); Non-Python tooling should use the project's standard commands; Use filesystem/shell tools to read/write/delete files as needed (eg, `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ), but only to read project files and to write/update `%%DOC_PATH%%/WORKFLOW.md`; Avoid in-place edits on any other path; Prefer read-only commands for analysis.

##### Steps Requirements
- **WFL-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **WFL-STP-002**: MUST define Step 2 to instruct: CRITICAL: Worktree Generation & Isolation.
- **WFL-STP-003**: MUST define Step 3 to instruct: Static analysis: build the runtime model from %%SRC_PATHS%%.
- **WFL-STP-004**: MUST define Step 4 to instruct: Generate and overwrite `%%DOC_PATH%%/WORKFLOW.md` document using declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **WFL-STP-005**: MUST define Step 5 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **WFL-STP-006**: MUST define Step 6 to instruct: CRITICAL: Merge Conflict Management.
- **WFL-STP-007**: MUST define Step 7 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.14 Write Prompt

##### Context Requirements
- **WRT-CTX-001**: MUST define the `## Purpose` section to instruct: Capture the user's intent as an SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) suitable for automated, SRS-driven development (requirements → design → implementation → verification), so downstream LLM Agents MUST implement the system without inventing unstated requirements.
- **WRT-CTX-002**: MUST define the `## Scope` section to instruct: In scope: author/update only `%%DOC_PATH%%/REQUIREMENTS.md` from [User Request](#users-request) in English, using explicit Assumptions for missing details and the canonical template structure; Out of scope: using repository source code as evidence, changing any other project file, generating workflow/references docs, or committing code changes.
- **WRT-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when drafting software requirements: ensure every requirement is atomic, unambiguous, and formatted for maximum testability using RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and never use the forbidden non-RFC modal verb; Act as a Technical Writer when structuring the SRS document `%%DOC_PATH%%/REQUIREMENTS.md`: apply a clean, hierarchical Markdown structure (max depth 3) and ensure technical precision, clarity, and adherence to professional documentation standards; Act as a Business Analyst when interpreting project goals: bridge the gap between technical implementation and user needs, ensuring the document provides clear value and aligns with the system's intended purpose; Act as a Senior System Architect when describing components or relationships: ensure the technical descriptions reflect a modular, scalable, and robust architecture consistent with industry best practices.
- **WRT-CTX-004**: MUST define the `## Behavior` section to instruct: Do not perform unrelated edits; (See "Absolute Rules, Non-Negotiable" for file-operation constraints).

##### Steps Requirements
- **WRT-STP-001**: MUST define Step 1 to instruct: Generate the Software Requirements Specification.
- **WRT-STP-002**: MUST define Step 2 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.15 Readme Prompt

##### Context Requirements
- **RDM-CTX-001**: MUST define the `usage` YAML field to instruct README-only maintenance from repository evidence and MUST keep the field length less than or equal to 1024 characters.
- **RDM-CTX-002**: MUST define the `## Purpose` section to instruct: Maintain root `README.md` as the first user-facing guide by documenting only externally visible behavior derived from repository evidence.
- **RDM-CTX-003**: MUST define the `## Scope` section to instruct: In scope: analyze user-visible implementation deltas under %%SRC_PATHS%% and update only root `README.md`; Out of scope: internal implementation details, requirements/workflow/references regeneration, source-code edits, and tests.
- **RDM-CTX-004**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer to locate externally visible behaviors; Act as a Business Analyst to map behavior to user outcomes; Act as a Senior Technical Writer to produce concise user-centric README content; Act as a QA Auditor for evidence-backed claims; Act as an Expert GitOps Engineer for isolated worktree and merge flow.
- **RDM-CTX-005**: MUST define the `## Behavior` section to instruct: Analyze implementation evidence for user-visible changes (features, CLI flags/parameters, GUI UX, distributed APIs, configuration schema); identify the exact root `README.md` sections impacted by analysis before editing; execute additional README edits explicitly requested in [User Request](#users-request) using the same `%%ARGS%%`-backed reference pattern used by `write.md`; update only those sections; keep non-analysis documentary parts unchanged (headers, versioning, context/scope narratives, personal motivations, related projects, high-level graphics/descriptions); preserve existing structure and formatting when possible; keep all new or edited text in English.

##### Steps Requirements
- **RDM-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **RDM-STP-002**: MUST define Step 2 to instruct: CRITICAL: Worktree Generation & Isolation.
- **RDM-STP-003**: MUST define Step 3 to instruct: Analyze user-visible implementation surface from %%SRC_PATHS%% and candidate related files.
- **RDM-STP-004**: MUST define Step 4 to instruct: Identify exact root `README.md` sections impacted by detected user-visible implementation changes and additional edits explicitly requested in [User Request](#users-request), then update only those sections while preserving unrelated content and existing structure/formatting whenever possible.
- **RDM-STP-005**: MUST define Step 5 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **RDM-STP-006**: MUST define Step 6 to instruct: CRITICAL: Merge Conflict Management.
- **RDM-STP-007**: MUST define Step 7 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

#### 3.3.16 Flowchart Prompt

##### Context Requirements
- **FCH-CTX-001**: MUST define the `usage` YAML field to instruct FLOWCHART-only maintenance from repository evidence and MUST keep the field length less than or equal to 1024 characters.
- **FCH-CTX-002**: MUST define the `## Purpose` section to instruct runtime-flowchart maintenance for `%%DOC_PATH%%/FLOWCHART.md` from repository evidence only.
- **FCH-CTX-003**: MUST define the `## Purpose` section to instruct downstream LLM Agents to reason about primary execution flow, decision branches, and grouped internal operations.
- **FCH-CTX-004**: MUST define the `## Scope` section to limit changes to `%%DOC_PATH%%/FLOWCHART.md` and the commit that records that document update.
- **FCH-CTX-005**: MUST define the `## Scope` section to exclude requirements, workflow, references, source-code, and test changes.
- **FCH-CTX-006**: MUST define the `## Professional Personas` section to instruct Senior System Architect and Senior System Engineer roles for runtime-flow and call-trace analysis.
- **FCH-CTX-007**: MUST define the `## Professional Personas` section to instruct the Business Analyst role for cross-referencing code evidence with `%%DOC_PATH%%/REQUIREMENTS.md`.
- **FCH-CTX-008**: MUST define the `## Professional Personas` section to instruct Technical Writer and Expert Mermaid.js Developer roles for structurally valid Mermaid output.
- **FCH-CTX-009**: MUST define the `## Professional Personas` section to instruct QA Auditor and Expert GitOps Engineer roles.
- **FCH-CTX-010**: MUST define the `## Behavior` section to write `%%DOC_PATH%%/FLOWCHART.md` in English and to avoid unrelated edits.
- **FCH-CTX-011**: MUST define the `## Behavior` section to allow writing only `%%DOC_PATH%%/FLOWCHART.md` and to prefer read-only commands for analysis.
- **FCH-CTX-012**: MUST define the `## Behavior` section to use the repository's standard toolchain and the Python preference order `uv`, then `.venv`, when applicable.
- **FCH-CTX-013**: MUST define a `## FLOWCHART.md Output Contract` section.
- **FCH-CTX-014**: MUST require `%%DOC_PATH%%/FLOWCHART.md` to contain only a fenced `mermaid` block with `graph TD`.
- **FCH-CTX-015**: MUST require flowchart nodes to encode alphabetical phases and numbered parameterless function prototypes.
- **FCH-CTX-016**: MUST require decision nodes to use pseudo-code criteria and MUST hide internal working tags from visible node text.
- **FCH-CTX-017**: MUST require cross-reference verification against the runtime model and source before writing `%%DOC_PATH%%/FLOWCHART.md`.

##### Steps Requirements
- **FCH-STP-001**: MUST define Step 1 to instruct: CRITICAL: Check GIT Status.
- **FCH-STP-002**: MUST define Step 2 to instruct: CRITICAL: Worktree Generation & Isolation.
- **FCH-STP-003**: MUST define Step 3 to instruct: Static analysis: build the runtime model from %%SRC_PATHS%%.
- **FCH-STP-004**: MUST define Step 4 to instruct: Generate and overwrite `%%DOC_PATH%%/FLOWCHART.md` with a Mermaid flowchart of the primary execution flow.
- **FCH-STP-005**: MUST define Step 4 to instruct grouping non-atomic functions into sequential alphabetical phases.
- **FCH-STP-006**: MUST define Step 4 to instruct extracting sequentially numbered atomic operations as parameterless function prototypes.
- **FCH-STP-007**: MUST define Step 4 to instruct deducing control flow, decisions, and joins from the Step 3 code analysis before writing the file.
- **FCH-STP-008**: MUST define Step 5 to instruct: CRITICAL: Stage & commit, including an explicit statement that a GPG-signed commit is not required.
- **FCH-STP-009**: MUST define Step 6 to instruct: CRITICAL: Merge Conflict Management.
- **FCH-STP-010**: MUST define Step 7 to instruct: Present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.
- **FCH-STP-011**: MUST define Step 4 to instruct sibling branches from one decision node to use comparable semantic granularity.
- **FCH-STP-012**: MUST define Step 4 to instruct normalizing equivalent branches by expanding or collapsing composite helpers to remove hidden-step ambiguity.
- **FCH-STP-013**: MUST define Step 4 to instruct keeping a composite helper collapsed only when sibling branches do not expose its internal operations.
- **FCH-STP-014**: MUST define Step 4 to instruct placing joins only after sibling branches are normalized to comparable semantic granularity.
- **FCH-STP-015**: MUST define Step 4 to instruct rendering skipped work only when source code enforces a real skip or bypass condition.
- **FCH-STP-016**: MUST define Step 4 to instruct a strict internal audit before writing `%%DOC_PATH%%/FLOWCHART.md`.
- **FCH-STP-017**: MUST define Step 4 to instruct auditing sibling granularity, hidden helper operations, real skips, and post-normalization joins against runtime-model and source evidence.
