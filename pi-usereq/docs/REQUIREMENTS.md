---
title: "Prompts Project Requirements"
description: Software requirements specification
version: "0.6.0"
date: "2026-10-05"
author: "req-change"
scope:
  paths:
    - "src/prompts/**/*.md"
    - "src/templates/**/*.md"
    - "src/instructions/**/*.md"
  excludes:
    - ".*/**"
visibility: "draft"
tags: ["srs", "prompts", "templates", "instructions"]
---

# Prompts Project Requirements

## 1. Introduction

### 1.1 Document Rules
Prefix `DOC` is reserved for document-authoring constraints in this section. Prefixes `INS` (instruction snippets), `EXT` (extension-orchestrated runtime), and `ICO` (iteration and context economy) are introduced in this revision for new requirement groups.

- **DOC-001**: MUST write and maintain this document in English.
- **DOC-002**: MUST use only RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and MUST NOT use modal verbs outside that set in requirement statements.
- **DOC-003**: MUST express every requirement bullet using the canonical format `- **<ID>**: <RFC2119 keyword> <single-sentence requirement>.`.
- **DOC-004**: MUST keep requirement IDs unique and non-repurposed within each published revision, and MUST update internal cross-references deterministically when IDs are renumbered.
- **DOC-005**: MUST write requirements for LLM Agents and automated parsers using high semantic density and no conversational filler.

### 1.2 Project Scope
This project defines and maintains prompt, template, and reusable-instruction artifacts used by the useReq process to enforce SRS-driven development with the sequence Requirements -> Design -> Implementation -> Verification.

### 1.3 Assumptions
- No application runtime source code is in scope for this SRS; all tracked source under `src/` is static Markdown content.
- No mandatory third-party runtime library was requested.
- Verification can be implemented with deterministic textual checks on Markdown artifacts.
- Repository validation, worktree creation, and merge handling are externalized to the slash-command extension orchestrator and are not embedded in bundled prompts.
- **CRITICAL**: Workflows that modify source code MUST execute unit tests during verification only when relevant unit tests already exist in the repository, selecting commands via language-specific test-suite priority policy; read-only workflows MUST rely on static evidence only.

### 1.4 Persona
- When you edit prompts and templates, act as a Senior AI Prompt Engineer and Senior LLM-Ops Engineer.
- When performing checks and tests on prompts and templates, act as a Senior AI Prompt Engineer, Senior LLM-Ops Engineer, and an expert static code analyst. Your task is to validate and review the provided prompts and templates.

### 1.5 Absolute Rules, Non-Negotiable
- When editing prompt or template artifacts:
  - MUST preserve placeholder tokens `%%ARGS%%`, `%%COMMIT%%`, `%%CONTEXT_FILES%%`, `%%DOC_PATH%%`, `%%GUIDELINES_FILES%%`, `%%PROMPT%%`, `%%SRC_PATHS%%`, `%%TEMPLATE_PATH%%`, and `%%TEST_PATH%%` exactly as-is.
  - MUST keep all prompt/template text free of typographical and grammatical errors.
  - MUST use uniform terminology and identical canonical instruction phrasing for identical actions, references, and process keywords.
  - MUST keep interruption rules explicit: prompts MUST NOT interrupt agent reasoning flow unless the interruption is required by defined workflow conditions.
  - MUST optimize prompts/templates for LLM-agent parsing, context efficiency, and token economy.
  - MUST target prompts/templates to LLM-agent execution and MUST NOT target human-only reading.
  - MUST require an explicit change request and corresponding `docs/REQUIREMENTS.md` update for any prompt/template file addition or removal.
  - MUST keep `src/prompts/`, `src/templates/`, and `src/instructions/` free of governance instructions about maintaining, editing, or verifying prompts/templates.
  - MUST NOT add instructions that increase hallucination risk unless explicitly required by a formal requirement.

## 2. Project Requirements

### 2.1 Project Functions
- **PRJ-001**: MUST maintain prompt artifacts in `src/prompts/` for SRS-driven workflows.
- **PRJ-002**: MUST maintain template artifacts in `src/templates/` as mandatory authoring guides and keep template taxonomy aligned with prompt-level Doxygen coverage directives.
- **PRJ-003**: MUST define each prompt with a single primary workflow intent and deterministic output objective.
- **PRJ-004**: MUST preserve the process order Requirements -> Design -> Implementation -> Verification when editing prompt instructions.

### 2.2 In-Scope Artifacts
| Category | Path | Intended Function |
| --- | --- | --- |
| Prompt | `src/prompts/analyze.md` | Produce a read-only analysis report. |
| Prompt | `src/prompts/change.md` | Update requirements and implement corresponding changes. |
| Prompt | `src/prompts/check.md` | Run requirements compliance checks. |
| Prompt | `src/prompts/cover.md` | Implement deltas that cover unmet requirements. |
| Prompt | `src/prompts/create.md` | Draft SRS from project source evidence. |
| Prompt | `src/prompts/fix.md` | Fix defects without changing requirements. |
| Prompt | `src/prompts/flowchart.md` | Draft `FLOWCHART.md` as a Mermaid flowchart from source evidence. |
| Prompt | `src/prompts/implement.md` | Implement code from requirements. |
| Prompt | `src/prompts/new.md` | Add new requirements and implement corresponding changes. |
| Prompt | `src/prompts/recreate.md` | Reorganize the SRS while preserving requirement IDs. |
| Prompt | `src/prompts/refactor.md` | Optimize internals without requirement changes. |
| Prompt | `src/prompts/renumber.md` | Renumber SRS requirements deterministically. |
| Prompt | `src/prompts/workflow.md` | Draft `WORKFLOW.md` from source evidence. |
| Prompt | `src/prompts/write.md` | Draft SRS from user-request text. |
| Prompt | `src/prompts/readme.md` | Update `README.md` from user-visible implementation evidence. |
| Template | `src/templates/Document_Source_Code_in_Doxygen_Style.md` | Mandatory source-code documentation guideline. |
| Template | `src/templates/HDT_Test_Authoring_Guide.md` | Mandatory unit-test authoring guideline. |
| Template | `src/templates/Requirements_Template.md` | Mandatory SRS authoring guideline. |
| Instruction | `src/instructions/git_commit.md` | Reusable commit-workflow block injected via `%%COMMIT%%`. |
| Instruction | `src/instructions/git_read-only.md` | Reusable git read-only restriction block for read-only prompts. |

> Note: `src/prompts/references.md` was removed in this revision; `REFERENCES.md` generation is now performed by the `references-generation` tool.

## 3. Requirements

### 3.1 Design and Implementation
- **DES-001**: MUST organize artifacts into dedicated prompt, template, and instruction directories with explicit responsibilities.
- **DES-002**: MUST standardize repeated operational instructions, including the commit workflow and completion or error messages, using identical wording across prompts and forbidding bell-control output suffixes, except prompt-name specialization.
- **DES-003**: MUST implement text-first interaction semantics and MUST NOT require GUI-specific behavior.
- **DES-004**: MUST preserve reusable keyword tokens exactly so installation-time substitution remains valid.
- **DES-005**: MUST maintain reusable instruction snippets under `src/instructions/` as canonical blocks consumed by prompts via placeholder tokens or verbatim inlining.
- **DES-006**: MUST author bundled prompt and template documents as standalone Markdown starting with a level-1 title and omitting YAML front matter in `src/`.
- **DES-007**: MUST NOT embed repository validation, worktree creation, or merge-handling steps in bundled prompts because those concerns are externalized.

Proposed repository structure (max depth 3, depth 4 for `src/` directories):

```text
└── src/
    ├── templates/
    │   ├── Document_Source_Code_in_Doxygen_Style.md
    │   ├── HDT_Test_Authoring_Guide.md
    │   └── Requirements_Template.md
    ├── instructions/
    │   ├── git_commit.md
    │   └── git_read-only.md
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
        ├── readme.md
        ├── recreate.md
        ├── refactor.md
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
- **REQ-011**: MUST NOT maintain a bundled `references.md` prompt; `%%DOC_PATH%%/REFERENCES.md` MUST be generated from source-code evidence via the `references-generation` tool.
- **REQ-012**: MUST define `renumber.md` to enforce deterministic requirement ID sequencing in SRS documents.
- **REQ-013**: MUST define `workflow.md` to generate `WORKFLOW.md` from source-code execution evidence.
- **REQ-014**: MUST define `write.md` to generate an SRS from user-request text without relying on source-code evidence.
- **REQ-015**: MUST define `readme.md` to update root `README.md` from user-visible implementation evidence only.
- **REQ-016**: MUST define `flowchart.md` to generate `FLOWCHART.md` as a Mermaid flowchart of primary program flow from source-code evidence only.
- **REQ-017**: MUST validate placeholder tokens by allowing only `%%ARGS%%`, `%%COMMIT%%`, `%%CONTEXT_FILES%%`, `%%DOC_PATH%%`, `%%GUIDELINES_FILES%%`, `%%PROMPT%%`, `%%SRC_PATHS%%`, `%%TEMPLATE_PATH%%`, and `%%TEST_PATH%%`, except artifacts that intentionally contain no placeholder tokens.
- **REQ-018**: MUST NOT contain typo and grammar errors, except fenced code blocks, inline-code spans, literal error strings, placeholders, and command snippets.
- **REQ-019**: MUST enforce canonical phrasing for shared operational instructions across prompts using built-in tools (`static-check`, `references-generation`, `search`, `files-search`) and `%%COMMIT%%` injection, allowing workflow-name specialization only.
- **REQ-020**: MUST require prompt instructions that generate shell commands to emit only linear commands compatible with restrictive filtering systems.
- **REQ-021**: MUST optimize prompts/templates for parser efficiency and token economy, except mandatory compliance blocks (`Professional Personas`, `Iteration and Context Economy`, `Execution Protocol`, `Execution Directives`, `Steps`) that are retained verbatim.
- **REQ-022**: MUST optimize prompts/templates for LLM-agent execution and MUST require the `## Professional Personas` section to include `Prompt Engineer and LLM Optimization Specialist` for prompt, agent, skill, and LLM-targeted document work.
- **REQ-023**: MUST use identical canonical instruction phrasing for identical actions across prompts, outside explicitly prompt-specific specializations, except where explicitly allowed below.
  - Workflow identity literals MAY vary where required to bind the emitting prompt (`/req-<name>`, commit-type prefix, workflow-specific title/scope text, and step labels tied to workflow intent).
  - Workflow-scoped failure or warning strings MAY vary only in workflow-name specialization while preserving the same control action pattern (`OUTPUT exactly "<STRING>"`, then terminate or override final line as explicitly defined).
  - Numeric bounds and scoped nouns MAY vary when they encode workflow-specific semantics (for example step-count cardinality and requirement-type nouns), while shared operational commands MUST remain byte-identical.
- **REQ-024**: MUST avoid instructions that cause unnecessary token-heavy content, except where explicitly allowed below.
  - Mandatory compliance blocks MAY remain verbose when retained verbatim by policy (`Professional Personas`, `Iteration and Context Economy`, `Execution Protocol`, `Execution Directives`, and `Steps`).
  - Canonical executable literals MAY remain fully expanded where determinism depends on exact text (shell commands, fixed report schema, fixed error strings, and WORKFLOW.md schema contracts).
  - High-detail enumerations MAY be used only when they constrain behavior and reduce ambiguity (supported tag sets, allowed temp/cache paths, and explicit termination-condition matrices).
- **REQ-025**: MUST reject unauthorized chain-interrupt instructions except at explicitly defined interruption points that emit exact strings and terminate or override the final status line.
- **REQ-026**: MUST reject new hallucination-risk instructions, except where explicitly allowed below.
  - Evidence-first high-recall directives MAY remain when uncertainty is explicitly downgraded to candidates and never asserted as complete without file-backed proof.
  - Autonomous disambiguation directives MAY remain only when constrained to least-invasive choices anchored to repository evidence and requirement traceability.
  - Tool-gated execution directives MAY require waiting for actual tool responses and exact-string outputs to prevent fabricated results.
- **REQ-027**: MUST ensure each prompt `usage` metadata value is generated with length less than or equal to 1024 characters.
- **REQ-028**: MUST treat `static-check` tool output `Error: no source files found in configured directories.` as successful no-source completion.
- **REQ-029**: MUST require prompt instructions that generate shell commands to avoid command substitution (`$()` or backticks), complex variable expansion, nested substitution, shell-derived helper composition, nested shell logic, and nested pipelines.
- **REQ-030**: MUST require shell-command instructions to apply safe literal-argument handling and to use explicit option termination for `rg` and `git grep` patterns beginning with `-` or `--`.
- **REQ-031**: MUST require `rg` and `git grep` search patterns beginning with `-` or `--` to avoid reliance on quoting or backslash escaping alone.
- **REQ-032**: MUST define `src/instructions/git_commit.md` as the canonical commit-workflow block injected into committing prompts via the `%%COMMIT%%` placeholder.
- **REQ-033**: MUST define `src/instructions/git_read-only.md` as the canonical git read-only restriction block inlined verbatim into read-only prompts.
- **REQ-034**: MUST inject `%%COMMIT%%` only into prompts that perform commits and MUST NOT inject it into read-only `analyze.md` or `check.md`.
- **REQ-035**: MUST end every bundled prompt under `src/prompts/` with a `## Context Files` section containing exactly one `%%CONTEXT_FILES%%` placeholder at the dynamic-injection point.
- **REQ-036**: MUST define the `## Context Files` section description to instruct the agent that injected files are pre-loaded authoritative context it MUST reason over without re-reading, searching, or fetching, and proceed without assumptions when none are injected.
- **REQ-037**: MUST use the `static-check` tool for static-analysis verification and MUST NOT reference any `req --here --static-check` command.
- **REQ-038**: MUST keep the `## Context Files` section description prose free of references to the `%%CONTEXT_FILES%%` token, the prompt-host runtime, and the CLI substitution mechanism.

### 3.3 Analyze Prompt
- **ANZ-CTX-001**: MUST define the `## Purpose` section to instruct: Enable evidence-backed reasoning about a request or investigation by grounding conclusions in the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`), the runtime/workflow model (`%%DOC_PATH%%/WORKFLOW.md`), references (`%%DOC_PATH%%/REFERENCES.md`), and the actual implementation, so downstream LLM Agents MUST choose the correct follow-up workflow with minimal re-discovery.
- **ANZ-CTX-002**: MUST define the `## Scope` section to instruct: In scope: read-only analysis of the above documents plus source under %%SRC_PATHS%% (and tests only as evidence when explicitly needed), including tool-assisted extraction; output is an analysis report with concrete evidence (paths/line numbers); Out of scope: any repository modification (requirements/code/tests/docs), generating patches, or applying fixes.
- **ANZ-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code and directory structures; Act as a Business Analyst when cross-referencing code findings with `%%DOC_PATH%%/REQUIREMENTS.md`; Act as a Technical Writer when producing the final analysis report; Act as a QA Auditor when reporting facts, requiring concrete evidence (file paths, line numbers) for every finding; Act as an Expert Debugger when you identify a failure symptom with concrete evidence, only explaining the root cause.
- **ANZ-CTX-004**: MUST define the `## Behavior` section to instruct: Only analyze the code and present the results; make no changes; Do NOT create or modify tests; Report facts with file paths and line numbers or short code excerpts; Allowed git commands (read-only only): `git status`, `git diff`, `git ls-files`, `git grep`, `git rev-parse`, `git branch --show-current`; Do NOT run any other git commands; Use filesystem/shell tools read-only (eg, `cat`, `sed -n`, `head`, `tail`, `rg`, `less`); Do NOT use in-place editing flags (eg, `-i`, `perl -pi`).
- **ANZ-STP-001**: MUST NOT embed a required-doc presence check step in `analyze.md` because doc validation is externalized outside the prompt.
- **ANZ-STP-002**: MUST define the analysis step to analyze the [User Request](#users-request).
- **ANZ-STP-003**: MUST define the follow-up-dispatch step positioned between the analysis step and the present-results step in `analyze.md`.
- **ANZ-STP-004**: MUST define the follow-up-dispatch step to generate the exact `/req-fix` prompt text when the analysis identifies an implementation behavior conflicting with requirements, the exact `/req-change` prompt text when the analysis identifies changes needed to both source code and requirements, and the exact `/req-refactor` prompt text when the analysis identifies source-code modifications that keep requirements unchanged with the intent of improving or adjusting the sources.
- **ANZ-STP-005**: MUST make the follow-up-dispatch step print each generated follow-up prompt text (`/req-fix`, `/req-change`, or `/req-refactor`) exactly when the analysis identified its corresponding source-code or requirements modification trigger and MUST NOT print any follow-up prompt text in any other case.
- **ANZ-STP-006**: MUST define the present-results step to present a human-readable analysis report preserving the fixed report schema and exact final status line.

### 3.4 Change Prompt
- **CHG-CTX-001**: MUST define the `## Purpose` section to instruct: Evolve existing system behavior safely by first updating the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) to encode the requested change, then implementing and verifying the corresponding code/test deltas with strict traceability to requirement IDs so downstream LLM Agents MUST reason over the change deterministically.
- **CHG-CTX-002**: MUST define the `## Scope` section to instruct: In scope: patch-style edits to `%%DOC_PATH%%/REQUIREMENTS.md`, an implementation plan, code/test changes under %%SRC_PATHS%% and %%TEST_PATH%%, verification via the `static-check` tool, requirements evidence checks, conditional execution of existing unit tests using language-specific test-suite priority policy, updates to `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, ending with a clean git commit; Out of scope: work that keeps requirements unchanged, and any implementation not justified by the updated requirements.
- **CHG-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Business Analyst when generating Requirement Delta and during requirements analysis; Act as a Senior System Architect when generating the Implementation Delta; Act as a Senior Software Developer during implementation; Act as a QA Engineer during verification with zero leniency; Act as an Expert GitOps Engineer when executing git workflows.
- **CHG-CTX-004**: MUST define the `## Behavior` section to instruct: Propose changes based only on requirements, user request, and repository evidence; Every proposed code change MUST reference at least one requirement ID or explicit user-request text; Use `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, and `%%DOC_PATH%%/REFERENCES.md` as primary inputs; All newly written or edited content MUST be in English; Prefer clean implementation over legacy support; Do not add backward compatibility UNLESS requirements mandate it.
- **CHG-STP-001**: MUST NOT embed a GIT-status check step in `change.md` because repository validation is externalized outside the prompt.
- **CHG-STP-002**: MUST NOT embed a required-doc presence check step in `change.md` because doc validation is externalized outside the prompt.
- **CHG-STP-003**: MUST NOT embed a worktree generation and isolation step in `change.md` because worktree routing is externalized outside the prompt.
- **CHG-STP-004**: MUST define the requirement-delta step to generate and apply the Requirement Delta to change requirements in `%%DOC_PATH%%/REQUIREMENTS.md`.
- **CHG-STP-005**: MUST define the implementation step to generate the Design Delta and implement the Implementation Delta according to the Requirement Delta.
- **CHG-STP-006**: MUST define the verification step to generate the Verification Delta by auditing ALL requirements with progressive-disclosure evidence, verifying static-analysis results, running existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **CHG-STP-007**: MUST define the WORKFLOW-update step to update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **CHG-STP-008**: MUST define the REFERENCES-update step to create/update `%%DOC_PATH%%/REFERENCES.md` with the `references-generation` tool.
- **CHG-STP-009**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **CHG-STP-010**: MUST NOT embed a merge-conflict management step in `change.md` because merge handling is externalized outside the prompt.
- **CHG-STP-011**: MUST define the present-results step to present results for human readers using clear sentences and readable Markdown while preserving the fixed report schema and exact final status line.

### 3.5 Check Prompt
- **CHK-CTX-001**: MUST define the `## Purpose` section to instruct: Provide an evidence-backed compliance audit by running static analysis and mapping every requirement in the SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) to concrete implementation evidence, so downstream LLM Agents MUST decide whether coverage work is required and where to apply it.
- **CHK-CTX-002**: MUST define the `## Scope` section to instruct: In scope: read `%%DOC_PATH%%/REQUIREMENTS.md` (and related docs), run static-analysis evidence with the `static-check` tool, mark ALL requirements as OK/FAIL with proof, and (only when FAILs exist) produce an implementation-only, patch-oriented technical report; Out of scope: any file modification or applying fixes.
- **CHK-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code and directory structures; Act as a Business Analyst when cross-referencing code findings with `%%DOC_PATH%%/REQUIREMENTS.md`; Act as a Technical Writer when producing the final analysis report; Act as a QA Auditor when reporting facts, requiring concrete evidence for every finding.
- **CHK-CTX-004**: MUST define the `## Behavior` section to instruct: Only analyze the code and static-analysis execution results and present the results; make no changes; Do NOT create or modify tests; Report facts with file paths and line numbers or short code excerpts.
- **CHK-STP-001**: MUST NOT embed a required-doc presence check step in `check.md` because doc validation is externalized outside the prompt.
- **CHK-STP-002**: MUST define the coverage step to run the `static-check` tool, check requirements coverage, and generate the Implementation Delta.
- **CHK-STP-003**: MUST define the present-results step to present results and Implementation Delta for human readers while preserving the fixed report schema and exact final status line.

### 3.6 Cover Prompt
- **COV-CTX-001**: MUST define the `## Purpose` section to instruct: Close coverage gaps by implementing the missing behaviors for uncovered requirement IDs in the existing codebase, so the implementation becomes fully compliant with the current SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) without changing that SRS.
- **COV-CTX-002**: MUST define the `## Scope` section to instruct: In scope: identify uncovered requirement IDs, implement minimal code changes under %%SRC_PATHS%%, add/adjust tests under %%TEST_PATH%% as needed, run verification with the `static-check` tool plus conditional execution of existing unit tests using language-specific test-suite priority policy, update `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and commit; Out of scope: editing `%%DOC_PATH%%/REQUIREMENTS.md`, introducing new requirements/features, or large-scale rewrites.
- **COV-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a QA Automation Engineer when identifying uncovered requirements; Act as a Business Analyst when mapping requirement IDs to observable behaviors; Act as a Senior System Architect when generating the Implementation Delta; Act as a Senior Software Developer when implementing the missing logic; Act as a QA Engineer during verification with zero leniency; Act as an Expert GitOps Engineer when executing git workflows.
- **COV-CTX-004**: MUST define the `## Behavior` section to instruct: Do not modify `%%DOC_PATH%%/REQUIREMENTS.md`; Always strictly respect requirements; Use the canonical docs as primary inputs; All newly written or edited content MUST be in English; Prioritize backward compatibility and preserve existing interfaces, data formats, and features; Report migration conflicts instead of implementing them and terminate.
- **COV-STP-001**: MUST NOT embed a GIT-status check step in `cover.md` because repository validation is externalized outside the prompt.
- **COV-STP-002**: MUST NOT embed a required-doc presence check step in `cover.md` because doc validation is externalized outside the prompt.
- **COV-STP-003**: MUST NOT embed a worktree generation and isolation step in `cover.md` because worktree routing is externalized outside the prompt.
- **COV-STP-004**: MUST define the coverage step to check requirements coverage, generate the Design Delta, and implement the Implementation Delta to cover uncovered requirements.
- **COV-STP-005**: MUST define the verification step to generate the Verification Delta by running the `static-check` tool, executing existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **COV-STP-006**: MUST define the WORKFLOW-update step to update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **COV-STP-007**: MUST define the REFERENCES-update step to create/update `%%DOC_PATH%%/REFERENCES.md` with the `references-generation` tool.
- **COV-STP-008**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **COV-STP-009**: MUST NOT embed a merge-conflict management step in `cover.md` because merge handling is externalized outside the prompt.
- **COV-STP-010**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.7 Create Prompt
- **CRT-CTX-001**: MUST define the `## Purpose` section to instruct: Bootstrap an SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) from repository evidence so downstream LLM Agents MUST start SRS-driven work grounded in what the code actually does, without guessing undocumented behavior.
- **CRT-CTX-002**: MUST define the `## Scope` section to instruct: In scope: static analysis of source under %%SRC_PATHS%% (and targeted tests only as evidence when needed) to create/update `%%DOC_PATH%%/REQUIREMENTS.md` in English; Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.
- **CRT-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when analyzing source code to infer behavior; Act as a Technical Writer when structuring the SRS document using RFC 2119 keywords exclusively and a max depth of 3 levels; Act as a Business Analyst when verifying the True State, including limitations or bugs.
- **CRT-CTX-004**: MUST define the `## Behavior` section to instruct: Write the document in English; Do not perform unrelated edits; Use filesystem/shell tools to read project files and to write/update only `%%DOC_PATH%%/REQUIREMENTS.md`; Prefer read-only commands for analysis.
- **CRT-STP-001**: MUST define the generate step to produce the Software Requirements Specification from source evidence following `%%TEMPLATE_PATH%%/Requirements_Template.md`.
- **CRT-STP-002**: MUST define the validate step to validate the Software Requirements Specification against actual code behavior (True State).
- **CRT-STP-003**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.
- **CRT-STP-004**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.

### 3.8 Fix Prompt
- **FIX-CTX-001**: MUST define the `## Purpose` section to instruct: Restore required behavior by diagnosing and fixing a defect while keeping the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) unchanged, so downstream LLM Agents MUST treat the fix as a semantics-correcting change rather than a requirements change.
- **FIX-CTX-002**: MUST define the `## Scope` section to instruct: In scope: reproduce/triage defects with concrete evidence and, when relevant unit-test suites exist, prefer a test-first defect flow (create one failing reproducer unit test -> design smallest safe fix -> implement -> verify reproducer pass), then verify with requirement evidence plus the `static-check` tool and conditional execution of existing unit tests using language-specific test-suite priority policy, update `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and commit; Out of scope: editing requirements, adding new features, or unnecessary refactors.
- **FIX-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as an Expert Debugger when diagnosing defects with concrete evidence before proposing the fix; Act as a Senior Software Developer when applying the smallest safe change that preserves public interfaces; Act as a Business Analyst when reading `%%DOC_PATH%%/REQUIREMENTS.md` to ensure fixes never violate documented behaviors; Act as a QA Automation Engineer when validating the fix; Act as an Expert GitOps Engineer when executing git workflows.
- **FIX-CTX-004**: MUST define the `## Behavior` section to instruct: Do not modify `%%DOC_PATH%%/REQUIREMENTS.md`; Always strictly respect requirements; Use the canonical docs as primary inputs; when relevant unit-test suites exist, prefer analyze -> create one failing reproducer -> implement smallest safe fix -> verify with requirement evidence and the `static-check` tool; use analyze -> implement -> verify fallback only when no relevant suite exists; treat no-source output as successful; All newly written or edited content MUST be in English; preserve backward compatibility unless requirements explicitly change it.
- **FIX-STP-001**: MUST NOT embed a GIT-status check step in `fix.md` because repository validation is externalized outside the prompt.
- **FIX-STP-002**: MUST NOT embed a required-doc presence check step in `fix.md` because doc validation is externalized outside the prompt.
- **FIX-STP-003**: MUST NOT embed a worktree generation and isolation step in `fix.md` because worktree routing is externalized outside the prompt.
- **FIX-STP-004**: MUST define the fix step to read requirements, analyze defect evidence, and when relevant unit-test suites exist create one failing reproducer unit test before designing and implementing the smallest safe fix.
- **FIX-STP-005**: MUST define the verification step to generate the Verification Delta by auditing ALL requirements with progressive-disclosure evidence, verifying defect resolution with requirement evidence plus the `static-check` tool, running existing unit tests with language-specific priority policy, confirming reproducer success when created, and implementing needed bug fixes.
- **FIX-STP-006**: MUST define the WORKFLOW-update step to update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **FIX-STP-007**: MUST define the REFERENCES-update step to create/update `%%DOC_PATH%%/REFERENCES.md` with the `references-generation` tool.
- **FIX-STP-008**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **FIX-STP-009**: MUST NOT embed a merge-conflict management step in `fix.md` because merge handling is externalized outside the prompt.
- **FIX-STP-010**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.
- **FIX-STP-011**: MUST define the fix-step incompatibility branch to output a three-column requirement-conflict table (`Requirement ID`, `Conflicting Excerpt`, `Conflict Reason + Interrupted Implementation Intent`) before emitting the exact error string and terminating.

### 3.9 Implement Prompt
- **IMP-CTX-001**: MUST define the `## Purpose` section to instruct: Produce a working implementation from the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) by building missing functionality end-to-end (including from scratch where needed), so the codebase becomes fully compliant with the documented requirement IDs without changing those requirements.
- **IMP-CTX-002**: MUST define the `## Scope` section to instruct: In scope: read `%%DOC_PATH%%/REQUIREMENTS.md`, implement/introduce source under %%SRC_PATHS%% (including new modules/files), add tests under %%TEST_PATH%%, verify via the `static-check` tool and conditional execution of existing unit tests using language-specific test-suite priority policy, update `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and commit; Out of scope: editing requirements or introducing features not present in the SRS.
- **IMP-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a QA Automation Engineer when identifying uncovered requirements; Act as a Business Analyst when mapping requirement IDs to observable behaviors; Act as a Senior System Architect when generating the Implementation Delta; Act as a Senior Software Developer when implementing the missing logic; Act as a QA Engineer during verification with zero leniency; Act as an Expert GitOps Engineer when executing git workflows.
- **IMP-CTX-004**: MUST define the `## Behavior` section to instruct: Do not modify `%%DOC_PATH%%/REQUIREMENTS.md`; Always strictly respect requirements; Use the canonical docs as primary inputs; All newly written or edited content MUST be in English; Prioritize backward compatibility and preserve existing interfaces, data formats, and features; Report migration conflicts instead of implementing them and terminate.
- **IMP-STP-001**: MUST NOT embed a GIT-status check step in `implement.md` because repository validation is externalized outside the prompt.
- **IMP-STP-002**: MUST NOT embed a worktree generation and isolation step in `implement.md` because worktree routing is externalized outside the prompt.
- **IMP-STP-003**: MUST define the implementation step to read requirements, generate the Design Delta, and implement the Implementation Delta to cover all requirements.
- **IMP-STP-004**: MUST define the verification step to generate the Verification Delta by running the `static-check` tool, executing existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **IMP-STP-005**: MUST define the static-analysis step to build the runtime model from %%SRC_PATHS%%.
- **IMP-STP-006**: MUST define the WORKFLOW step to generate and overwrite `%%DOC_PATH%%/WORKFLOW.md` using declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **IMP-STP-007**: MUST define the REFERENCES-update step to create/update `%%DOC_PATH%%/REFERENCES.md` with the `references-generation` tool.
- **IMP-STP-008**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **IMP-STP-009**: MUST NOT embed a merge-conflict management step in `implement.md` because merge handling is externalized outside the prompt.
- **IMP-STP-010**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.10 New Prompt
- **NEW-CTX-001**: MUST define the `## Purpose` section to instruct: Introduce a new, backwards-compatible capability by first extending the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) with the new requirement(s), then implementing and verifying the corresponding code/test changes with strict traceability to requirement IDs so downstream LLM Agents MUST reason over the new feature deterministically.
- **NEW-CTX-002**: MUST define the `## Scope` section to instruct: In scope: patch-style updates to `%%DOC_PATH%%/REQUIREMENTS.md` that add the new feature requirements, an implementation plan, code/test changes under %%SRC_PATHS%% and %%TEST_PATH%%, verification via the `static-check` tool, requirements evidence checks, conditional execution of existing unit tests using language-specific test-suite priority policy, updates to `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and a clean git commit; Out of scope: breaking changes, migrations/compatibility conversions, or any feature work not captured as explicit requirements.
- **NEW-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Business Analyst when generating Requirement Delta and during requirements analysis; Act as a Senior System Architect when generating the Implementation Delta; Act as a Senior Software Developer during implementation; Act as a QA Engineer during verification with zero leniency; Act as an Expert GitOps Engineer when executing git workflows.
- **NEW-CTX-004**: MUST define the `## Behavior` section to instruct: Propose changes based only on requirements, user request, and repository evidence; Every proposed code change MUST reference at least one requirement ID or explicit user-request text; Use the canonical docs as primary inputs; All newly written or edited content MUST be in English; Prioritize backward compatibility and preserve existing interfaces, data formats, and features; Report migration conflicts instead of implementing them and terminate.
- **NEW-STP-001**: MUST NOT embed a GIT-status check step in `new.md` because repository validation is externalized outside the prompt.
- **NEW-STP-002**: MUST NOT embed a required-doc presence check step in `new.md` because doc validation is externalized outside the prompt.
- **NEW-STP-003**: MUST NOT embed a worktree generation and isolation step in `new.md` because worktree routing is externalized outside the prompt.
- **NEW-STP-004**: MUST define the requirement-delta step to generate and apply the Requirement Delta to cover new requirements.
- **NEW-STP-005**: MUST define the implementation step to generate the Design Delta and implement the Implementation Delta according to the Requirement Delta.
- **NEW-STP-006**: MUST define the verification step to generate the Verification Delta by auditing ALL requirements with progressive-disclosure evidence, verifying static-analysis results, running existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **NEW-STP-007**: MUST define the WORKFLOW-update step to update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **NEW-STP-008**: MUST define the REFERENCES-update step to create/update `%%DOC_PATH%%/REFERENCES.md` with the `references-generation` tool.
- **NEW-STP-009**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **NEW-STP-010**: MUST NOT embed a merge-conflict management step in `new.md` because merge handling is externalized outside the prompt.
- **NEW-STP-011**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.11 ReCreate Prompt
- **RCR-CTX-001**: MUST define the `## Purpose` section to instruct: Rebuild and reorganize the SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) from repository evidence while preserving all existing requirement IDs so downstream LLM Agents MUST rely on a clean structure and stable traceability when driving subsequent design/implementation work.
- **RCR-CTX-002**: MUST define the `## Scope` section to instruct: In scope: static analysis of source under %%SRC_PATHS%% (and targeted tests only as evidence when needed) to rewrite `%%DOC_PATH%%/REQUIREMENTS.md` in English, allowing reorganization and additions, but forbidding any renumbering/renaming of existing requirement IDs; Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.
- **RCR-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when analyzing source code to infer behavior; Act as a Technical Writer when structuring the SRS using RFC 2119 keywords exclusively and a max depth of 3 levels; Act as a Business Analyst when verifying the True State; Act as an Expert GitOps Engineer when executing git workflows.
- **RCR-CTX-004**: MUST define the `## Behavior` section to instruct: Write the document in English; Do not perform unrelated edits; Use filesystem/shell tools to read project files and to write/update only `%%DOC_PATH%%/REQUIREMENTS.md`; Prefer read-only commands for analysis.
- **RCR-STP-001**: MUST NOT embed a GIT-status check step in `recreate.md` because repository validation is externalized outside the prompt.
- **RCR-STP-002**: MUST NOT embed a required-doc presence check step in `recreate.md` because doc validation is externalized outside the prompt.
- **RCR-STP-003**: MUST NOT embed a worktree generation and isolation step in `recreate.md` because worktree routing is externalized outside the prompt.
- **RCR-STP-004**: MUST define the generate step to produce the Software Requirements Specification from source evidence following `%%TEMPLATE_PATH%%/Requirements_Template.md`.
- **RCR-STP-005**: MUST define the validate step to validate the Software Requirements Specification against actual code behavior (True State).
- **RCR-STP-006**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **RCR-STP-007**: MUST NOT embed a merge-conflict management step in `recreate.md` because merge handling is externalized outside the prompt.
- **RCR-STP-008**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.12 Refactor Prompt
- **RFR-CTX-001**: MUST define the `## Purpose` section to instruct: Improve maintainability, structure, and/or performance while strictly preserving externally observable behavior and keeping the normative SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) unchanged, so downstream LLM Agents MUST treat the refactor as a semantics-preserving transformation.
- **RFR-CTX-002**: MUST define the `## Scope` section to instruct: In scope: internal refactors under %%SRC_PATHS%% (including private API reshaping) that preserve public interfaces/data formats, optional test adjustments only when objectively incorrect, verification via the `static-check` tool, requirements evidence checks, conditional execution of existing unit tests using language-specific test-suite priority policy, updates to `%%DOC_PATH%%/WORKFLOW.md` and `%%DOC_PATH%%/REFERENCES.md`, and a clean git commit; Out of scope: editing requirements, introducing new features, or making intentional behavioral changes.
- **RFR-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Software Developer when refactoring, prioritizing clean internal logic while preserving public interfaces; Act as a Business Analyst when reading `%%DOC_PATH%%/REQUIREMENTS.md` to ensure refactors never violate documented behaviors; Act as a QA Automation Engineer when validating; Act as an Expert Debugger only if tests fail or a defect emerges; Act as an Expert GitOps Engineer when executing git workflows.
- **RFR-CTX-004**: MUST define the `## Behavior` section to instruct: Always strictly respect requirements; Use the canonical docs as primary inputs; All newly written or edited content MUST be in English; Refactor internals and private APIs freely but MUST strictly preserve all public interfaces, data formats, and externally observable behaviors; Remove legacy internal code but ensure strict backward compatibility for the public API.
- **RFR-STP-001**: MUST NOT embed a GIT-status check step in `refactor.md` because repository validation is externalized outside the prompt.
- **RFR-STP-002**: MUST NOT embed a required-doc presence check step in `refactor.md` because doc validation is externalized outside the prompt.
- **RFR-STP-003**: MUST NOT embed a worktree generation and isolation step in `refactor.md` because worktree routing is externalized outside the prompt.
- **RFR-STP-004**: MUST define the refactor step to generate the Design Delta and implement the Implementation Delta to implement the refactor.
- **RFR-STP-005**: MUST define the verification step to generate the Verification Delta by running the `static-check` tool, executing existing unit tests with language-specific priority policy, and implementing needed bug fixes.
- **RFR-STP-006**: MUST define the WORKFLOW-update step to update `%%DOC_PATH%%/WORKFLOW.md` via targeted edits using the canonical WORKFLOW document contract (same terminology, same schema, same call-trace rules) and declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **RFR-STP-007**: MUST define the REFERENCES-update step to create/update `%%DOC_PATH%%/REFERENCES.md` with the `references-generation` tool.
- **RFR-STP-008**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **RFR-STP-009**: MUST NOT embed a merge-conflict management step in `refactor.md` because merge handling is externalized outside the prompt.
- **RFR-STP-010**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.13 References Prompt
- **REF-CTX-001**: MUST NOT maintain a bundled `src/prompts/references.md` prompt in this revision because it was removed.
- **REF-CTX-002**: MUST generate `%%DOC_PATH%%/REFERENCES.md` via the `references-generation` tool instead of a bundled prompt.
- **REF-CTX-003**: MUST NOT define `## Purpose`, `## Scope`, `## Professional Personas`, or `## Behavior` sections for a removed `references.md` prompt.
- **REF-CTX-004**: MUST NOT perform unrelated edits when maintaining `%%DOC_PATH%%/REFERENCES.md` via the `references-generation` tool.
- **REF-STP-001**: MUST NOT embed a GIT-status check step in a removed `references.md` prompt.
- **REF-STP-002**: MUST NOT embed a worktree generation and isolation step in a removed `references.md` prompt.
- **REF-STP-003**: MUST update `%%DOC_PATH%%/REFERENCES.md` via the `references-generation` tool.
- **REF-STP-004**: MUST NOT embed a stage-and-commit step in a removed `references.md` prompt.
- **REF-STP-005**: MUST NOT embed a merge-conflict management step in a removed `references.md` prompt.
- **REF-STP-006**: MUST NOT embed a present-results step in a removed `references.md` prompt.

### 3.14 Renumber Prompt
- **RNB-CTX-001**: MUST define the `## Purpose` section to instruct: Deterministically renumber requirement IDs in `%%DOC_PATH%%/REQUIREMENTS.md` to produce a clean, progressive numbering scheme while preserving the exact requirement text and document order so downstream LLM Agents MUST rely on stable, sequential identifiers.
- **RNB-CTX-002**: MUST define the `## Scope` section to instruct: In scope: renumbering requirement identifiers in `%%DOC_PATH%%/REQUIREMENTS.md` in document order and updating internal cross-references to those identifiers, without modifying any requirement text, headings, or ordering; Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.
- **RNB-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when analyzing source code to infer behavior; Act as a Technical Writer when structuring the SRS using RFC 2119 keywords exclusively and a max depth of 3 levels; Act as a Business Analyst when verifying the True State; Act as an Expert GitOps Engineer when executing git workflows.
- **RNB-CTX-004**: MUST define the `## Behavior` section to instruct: Write the document in English; Do not perform unrelated edits; Do NOT change any requirement content or document structure; only change requirement IDs and requirement-ID cross-references; Use filesystem/shell tools to read project files and to write/update only `%%DOC_PATH%%/REQUIREMENTS.md`.
- **RNB-STP-001**: MUST NOT embed a GIT-status check step in `renumber.md` because repository validation is externalized outside the prompt.
- **RNB-STP-002**: MUST NOT embed a required-doc presence check step in `renumber.md` because doc validation is externalized outside the prompt.
- **RNB-STP-003**: MUST NOT embed a worktree generation and isolation step in `renumber.md` because worktree routing is externalized outside the prompt.
- **RNB-STP-004**: MUST define the renumber step to deterministically renumber requirement IDs in the Software Requirements Specification in document order.
- **RNB-STP-005**: MUST define the validate step to validate the Software Requirements Specification against actual code behavior (True State).
- **RNB-STP-006**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **RNB-STP-007**: MUST NOT embed a merge-conflict management step in `renumber.md` because merge handling is externalized outside the prompt.
- **RNB-STP-008**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.15 Workflow Prompt
- **WFL-CTX-001**: MUST define the `## Purpose` section to instruct: Maintain an LLM-oriented runtime/workflow model (`%%DOC_PATH%%/WORKFLOW.md`) derived from repository evidence so downstream LLM Agents MUST reason about execution units, communication edges, and internal call-traces during SRS-driven design/implementation.
- **WFL-CTX-002**: MUST define the `## Scope` section to instruct: In scope: static analysis of source under %%SRC_PATHS%% to generate/overwrite only `%%DOC_PATH%%/WORKFLOW.md` in English only, following the mandated schema, then commit that doc change; Out of scope: changes to requirements, references, source code, or tests.
- **WFL-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer when analyzing source code to trace execution flow across files and modules; Act as a Business Analyst when cross-referencing code findings with `%%DOC_PATH%%/REQUIREMENTS.md`; Act as a Technical Writer when producing the final workflow descriptions; Act as a QA Auditor requiring concrete evidence as declaration file paths only; Act as an Expert GitOps Engineer when executing git workflows.
- **WFL-CTX-004**: MUST define the `## Behavior` section to instruct: Write `%%DOC_PATH%%/WORKFLOW.md` in English; Do not perform unrelated edits; Use filesystem/shell tools to read project files and to write/update only `%%DOC_PATH%%/WORKFLOW.md`; Prefer read-only commands for analysis.
- **WFL-STP-001**: MUST NOT embed a GIT-status check step in `workflow.md` because repository validation is externalized outside the prompt.
- **WFL-STP-002**: MUST NOT embed a worktree generation and isolation step in `workflow.md` because worktree routing is externalized outside the prompt.
- **WFL-STP-003**: MUST define the static-analysis step to build the runtime model from %%SRC_PATHS%%.
- **WFL-STP-004**: MUST define the generate step to generate and overwrite `%%DOC_PATH%%/WORKFLOW.md` using declaration file paths only, excluding line numbers, line ranges, and internal file-reference pointers.
- **WFL-STP-005**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **WFL-STP-006**: MUST NOT embed a merge-conflict management step in `workflow.md` because merge handling is externalized outside the prompt.
- **WFL-STP-007**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.

### 3.16 Write Prompt
- **WRT-CTX-001**: MUST define the `## Purpose` section to instruct: Capture the user's intent as an SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) suitable for automated, SRS-driven development, so downstream LLM Agents MUST implement the system without inventing unstated requirements.
- **WRT-CTX-002**: MUST define the `## Scope` section to instruct: In scope: author/update only `%%DOC_PATH%%/REQUIREMENTS.md` from [User Request](#users-request) in English, using explicit Assumptions for missing details and the canonical template structure; Out of scope: using repository source code as evidence, changing any other project file, generating workflow/references docs, or committing code changes.
- **WRT-CTX-003**: MUST define the `## Professional Personas` section to instruct: Act as a Senior Technical Requirements Engineer when drafting software requirements using RFC 2119 keywords; Act as a Technical Writer when structuring the SRS document with a max depth of 3; Act as a Business Analyst when interpreting project goals; Act as a Senior System Architect when describing components or relationships.
- **WRT-CTX-004**: MUST define the `## Behavior` section to instruct: Do not perform unrelated edits; observe the Absolute Rules, Non-Negotiable for file-operation constraints.
- **WRT-STP-001**: MUST define the generate step to produce the Software Requirements Specification from the [User Request](#users-request) following `%%TEMPLATE_PATH%%/Requirements_Template.md`.
- **WRT-STP-002**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.
- **WRT-STP-003**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.

### 3.17 Readme Prompt
- **RDM-CTX-001**: MUST define the `usage` metadata to instruct README-only maintenance from repository evidence and MUST keep the field length less than or equal to 1024 characters.
- **RDM-CTX-002**: MUST define the `## Purpose` section to instruct: Maintain root `README.md` as the first user-facing guide by documenting only externally visible behavior derived from repository evidence.
- **RDM-CTX-003**: MUST define the `## Scope` section to instruct: In scope: analyze user-visible implementation deltas under %%SRC_PATHS%% and update only root `README.md`; Out of scope: internal implementation details, requirements/workflow/references regeneration, source-code edits, and tests.
- **RDM-CTX-004**: MUST define the `## Professional Personas` section to instruct: Act as a Senior System Engineer to locate externally visible behaviors; Act as a Business Analyst to map behavior to user outcomes; Act as a Senior Technical Writer to produce concise user-centric README content; Act as a QA Auditor for evidence-backed claims; Act as an Expert GitOps Engineer for isolated worktree and merge flow.
- **RDM-CTX-005**: MUST define the `## Behavior` section to instruct: Analyze implementation evidence for user-visible changes; validate every enumerated root `README.md` section sentence-by-sentence against implementation evidence, recording per-sentence outcomes without skipping parts or sections; identify the exact root `README.md` sections impacted before editing; execute additional README edits explicitly requested in [User Request](#users-request); update only those sections; keep non-analysis documentary parts unchanged; keep all new or edited text in English.
- **RDM-STP-001**: MUST NOT embed a GIT-status check step in `readme.md` because repository validation is externalized outside the prompt.
- **RDM-STP-002**: MUST NOT embed a worktree generation and isolation step in `readme.md` because worktree routing is externalized outside the prompt.
- **RDM-STP-003**: MUST define the analysis step to detect the user-visible implementation surface from %%SRC_PATHS%% and candidate related files.
- **RDM-STP-004**: MUST define the update step to identify exact root `README.md` sections impacted by detected user-visible changes and additional requested edits, then update only those sections while preserving unrelated content and existing structure/formatting.
- **RDM-STP-005**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **RDM-STP-006**: MUST NOT embed a merge-conflict management step in `readme.md` because merge handling is externalized outside the prompt.
- **RDM-STP-007**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.
- **RDM-STP-008**: MUST define the update step to enumerate all root `README.md` sections and headings in document order before validation to fix the complete validation surface.
- **RDM-STP-009**: MUST define the update step to validate every non-excluded sentence in each enumerated section against repository implementation evidence, recording a per-sentence conformance outcome.
- **RDM-STP-010**: MUST define the update step to enforce a completeness gate that blocks step completion until every enumerated section and sentence has a recorded outcome.

### 3.18 Flowchart Prompt
- **FCH-CTX-001**: MUST define the `usage` metadata to instruct FLOWCHART-only maintenance from repository evidence and MUST keep the field length less than or equal to 1024 characters.
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
- **FCH-STP-001**: MUST NOT embed a GIT-status check step in `flowchart.md` because repository validation is externalized outside the prompt.
- **FCH-STP-002**: MUST NOT embed a worktree generation and isolation step in `flowchart.md` because worktree routing is externalized outside the prompt.
- **FCH-STP-003**: MUST define the static-analysis step to build the runtime model from %%SRC_PATHS%%.
- **FCH-STP-004**: MUST define the generate step to overwrite `%%DOC_PATH%%/FLOWCHART.md` with a Mermaid flowchart of the primary execution flow.
- **FCH-STP-005**: MUST define the generate step to group non-atomic functions into sequential alphabetical phases.
- **FCH-STP-006**: MUST define the generate step to extract sequentially numbered atomic operations as parameterless function prototypes.
- **FCH-STP-007**: MUST define the generate step to deduce control flow, decisions, and joins from the static-analysis step before writing the file.
- **FCH-STP-008**: MUST define the commit step as the `%%COMMIT%%` placeholder that injects the canonical commit-workflow block from `src/instructions/git_commit.md`, including an explicit statement that a GPG-signed commit is not required.
- **FCH-STP-009**: MUST NOT embed a merge-conflict management step in `flowchart.md` because merge handling is externalized outside the prompt.
- **FCH-STP-010**: MUST define the present-results step to present results for human readers while preserving the fixed report schema and exact final status line.
- **FCH-STP-011**: MUST define the generate step to instruct sibling branches from one decision node to use comparable semantic granularity.
- **FCH-STP-012**: MUST define the generate step to normalize equivalent branches by expanding or collapsing composite helpers to remove hidden-step ambiguity.
- **FCH-STP-013**: MUST define the generate step to keep a composite helper collapsed only when sibling branches do not expose its internal operations.
- **FCH-STP-014**: MUST define the generate step to place joins only after sibling branches are normalized to comparable semantic granularity.
- **FCH-STP-015**: MUST define the generate step to render skipped work only when source code enforces a real skip or bypass condition.
- **FCH-STP-016**: MUST define the generate step to perform a strict internal audit before writing `%%DOC_PATH%%/FLOWCHART.md`.
- **FCH-STP-017**: MUST define the generate step to audit sibling granularity, hidden helper operations, real skips, and post-normalization joins against runtime-model and source evidence.

### 3.19 Iteration and Context Economy
- **ICO-CTX-001**: MUST insert a `## Iteration and Context Economy` section in every prompt under `src/prompts/` immediately after `## Professional Personas` and immediately before `## Absolute Rules, Non-Negotiable`.
- **ICO-CTX-002**: MUST keep the `## Iteration and Context Economy` section byte-identical across all prompts under `src/prompts/`.
- **ICO-CTX-003**: MUST define the `## Iteration and Context Economy` section as a list of `CRITICAL` rules that are mandatory and non-negotiable.
- **ICO-CTX-004**: MUST require the rules to instruct the agent to minimize the number of iterations by batching independent operations and dispatching parallel tool calls whenever no dependency forces sequencing.
- **ICO-CTX-005**: MUST require the rules to forbid re-reading, re-searching, or re-fetching files already provided as injected `%%CONTEXT_FILES%%` context or already read in the current session.
- **ICO-CTX-006**: MUST require the rules to forbid restating requirement text, prior tool output, or unchanged file contents and to cite them by file path, symbol, and line range instead.
- **ICO-CTX-007**: MUST require the rules to instruct the agent to add only information required by the active Step, a requirement ID, or explicit user-request text, omitting narration, filler, and speculative commentary.
- **ICO-CTX-008**: MUST require the rules to select the most token-efficient evidence path in order: `%%DOC_PATH%%/REQUIREMENTS.md`, `%%DOC_PATH%%/WORKFLOW.md`, `%%DOC_PATH%%/REFERENCES.md`, then `search`/`files-search`, then `rg`/`grep` fallback.
- **ICO-CTX-009**: MUST require the rules to instruct the agent to gather all evidence a Step needs before producing its output and to not split a single logical operation across multiple iterations when one suffices.
- **ICO-CTX-010**: MUST require the rules to instruct the agent to pause for a tool response only when a Step explicitly depends on it and to otherwise proceed autonomously without requesting confirmation.
- **ICO-CTX-011**: MUST require the rules to govern how the agent organizes and sequences the work described in the `## Steps` section.

<!-- Performance optimizations: No explicit performance optimizations identified. Source under src/ is static Markdown content with no executable code paths. -->
