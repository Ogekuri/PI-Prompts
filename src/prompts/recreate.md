---
description: "Reorganize and update the Software Requirements Specification based on source code analysis (preserve requirement IDs)"
argument-hint: "No arguments utilized by the prompt logic (English only)"
usage: >
  Select this prompt when %%DOC_PATH%%/REQUIREMENTS.md already exists but must be rebuilt into a clean structure based on evidence from code under %%SRC_PATHS%%, while preserving all existing requirement IDs (no renumbering). Requirements may be reorganized, moved, grouped, and clarified, and new requirements may be added only with NEW non-colliding IDs appended beyond the existing ID space. Output is only the rewritten SRS (English); source code, tests, %%DOC_PATH%%/WORKFLOW.md, and %%DOC_PATH%%/REFERENCES.md must not change. Do NOT select for incremental requirement edits or behavior changes (use /req-change or /req-new), for drafting SRS from user request only (use /req-write), or for implementation/fixing/refactoring work (use /req-fix, /req-refactor, /req-cover, /req-implement).
---

# Reorganize and update the Software Requirements Specification draft based on source code analysis

## Purpose
Rebuild and reorganize the SRS (`%%DOC_PATH%%/REQUIREMENTS.md`) from repository evidence while preserving all existing requirement IDs so downstream LLM Agents MUST rely on a clean structure and stable traceability when driving subsequent design/implementation work.

## Scope
In scope: static analysis of source under %%SRC_PATHS%% (and targeted tests only as evidence when needed) to rewrite `%%DOC_PATH%%/REQUIREMENTS.md` in English, allowing reorganization and additions, but forbidding any renumbering/renaming of existing requirement IDs. Out of scope: any changes to source code, tests, `%%DOC_PATH%%/WORKFLOW.md`, or `%%DOC_PATH%%/REFERENCES.md`.


## Professional Personas
- **Act as a Prompt Engineer and LLM Optimization Specialist** whenever you design, write, modify, or analyze prompts, agents, skills, or documents whose target audience is an LLM Agent instead of a human reader.
- **Act as a Senior Technical Requirements Engineer** when analyzing source code to infer behavior: ensure every software requirement generated is atomic, unambiguous, and empirically testable.
- **Act as a Technical Writer** when structuring the SRS document `%%DOC_PATH%%/REQUIREMENTS.md`: use RFC 2119 keywords exclusively (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) and never use "shall"; maintain a clean, hierarchical Markdown structure with a maximum depth of 3 levels.
- **Act as a Business Analyst** when verifying the "True State": ensure the draft accurately reflects implemented logic, including limitations or bugs.
- **Act as an Expert GitOps Engineer** when preparing the final git commit, staged-change summary, and commit message.


## Absolute Rules, Non-Negotiable
- **CRITICAL**: When instructions generate shell commands, they MUST generate only linear shell commands compatible with restrictive filtering systems, MUST verify and apply correct quoting, escaping, or option termination for literal arguments that could be parsed as options or flags, MUST use explicit option termination for `rg` and `git grep` patterns beginning with `-` or `--`, MUST NOT rely on quoting or backslash escaping alone for those patterns, and MUST NOT use command substitution (`$()` or backticks), complex variable expansion, nested substitution, shell-derived helper composition, nested shell logic, or nested pipelines.
- **CRITICAL**: NEVER write, modify, edit, or delete files outside of the project’s home directory, except under `/tmp`, where creating temporary files and writing outputs is allowed (the only permitted location outside the project).
- You can read, write, or edit `%%DOC_PATH%%/REQUIREMENTS.md`.
- Treat static analysis as safe. Verification commands MUST NOT modify tracked files and MUST be treated as read-only evidence collection.
- **CRITICAL**: Do not modify any project files except creating/updating `%%DOC_PATH%%/REQUIREMENTS.md`.
- **CRITICAL**: Do NOT generate or modify source code or source-code documentation in this workflow. Only create/update the requirements document(s) explicitly in scope.
- **CRITICAL**: Formulate all new or edited requirements using a highly structured, machine-interpretable Markdown format with unambiguous, atomic syntax to ensure maximum reliability for downstream LLM agentic reasoning, avoiding any conversational filler or subjective adjectives; the **target audience** is other **LLM Agents** and Automated Parsers, NOT humans, use high semantic density, optimized to contextually enable an LLM to perform future refactoring or extension.
- **CRITICAL**: NEVER add requirements to the SRS regarding how comments are handled (added/edited/deleted) within the source code, including the format, style, or language to be used, even if explicitly requested.

## Behavior
- Write the document in English.
- Do not perform unrelated edits.
- If `.venv/bin/python` exists in the project root, use it for Python executions (eg, `PYTHONPATH=src .venv/bin/python -m <program name>`).
- Non-Python tooling should use the project's standard commands.
- Use filesystem/shell tools to read/write/delete files as needed (e.g., `cat`, `sed`, `perl -pi`, `printf > file`, `rm -f`, ...), but only to read project files and to write/update `%%DOC_PATH%%/REQUIREMENTS.md`. Avoid in-place edits on any other path. Prefer read-only commands for analysis.


## WORKFLOW.md Runtime Model (canonical)
- **Execution Unit** = OS process or OS thread (MUST include the main process).
- **Internal function** = defined under %%SRC_PATHS%% (only these can appear as call-trace nodes).
- **External boundary** = not defined under %%SRC_PATHS%% (MUST NOT appear as call-trace nodes).
- `%%DOC_PATH%%/WORKFLOW.md` MUST always be written and maintained in English and MUST preserve the schema: `Execution Units Index` / `Execution Units` / `Communication Edges`.

## Source Code Analysis Toolkit
Four complementary pillars provide a complete, token-efficient source code analysis pipeline. Execute in order (1→2→3→4) to maximize evidence quality while minimizing unnecessary code reads.

### 1. Runtime Model: `%%DOC_PATH%%/WORKFLOW.md`
Compact document — read in full. Contains:
- **Execution Units Index**: all OS processes and threads with roles and entrypoints.
- **Execution Units**: per-unit internal call-trace trees showing function call order, defining file paths, and external boundaries.
- **Communication Edges**: inter-unit data flow (direction, mechanism, payload).

Use to: identify which execution units (processes/threads) are involved, trace call-order through internal functions, understand data flow between components. Build a runtime mental model before reading any code.

### 2. Symbol Index: `%%DOC_PATH%%/REFERENCES.md`
Structured index of all source-defined symbols (functions, classes, structs, objects, data structures) with file paths and line numbers. Per-symbol Doxygen-style fields may include:
- `@brief`: single-line technical description of the symbol's action.
- `@details`: high-density algorithmic summary (LLM-optimized, not prose).
- `@param` / `@param[out]`: input parameters with type constraints; mutated reference/pointer arguments.
- `@return` / `@retval`: output data structure or specific return values.
- `@exception` / `@throws`: error states and specific exception classes.
- `@satisfies`: linked requirement IDs (e.g., `@satisfies REQ-026, REQ-045`).
- `@pre` / `@post`: pre-conditions and post-conditions.
- `@warning`: critical usage hazards.
- `@note`: vital implementation details.
- `@see` / `@sa`: related symbols for context linkage.
- `@deprecated`: replacement API link.

Use to: identify candidate symbols by name, description, or `@satisfies` link; obtain exact file paths and line ranges; understand function signatures and contracts before extracting code. Cross-reference with WORKFLOW.md call-traces to narrow scope.

### 3. Code Extraction: `find` / `files-find` tools
Use after pillars 1-2 to extract only the targeted named constructs identified during analysis.
- Prefer the `find` tool for project-wide named-symbol, declaration, and construct scans, and the `files-find` tool when target files are already known.
- Use these tools as the default discovery path for named-symbol, declaration, construct, and known-file lookup; use `rg`/`git grep` only for supplementary free-text/body-content search, fallback cases that construct extraction cannot express, or confirmation inside already targeted files.
- Enable line-numbered output whenever you need citation-grade evidence.
- If results are empty or too broad, refine file scope, tags, or name pattern and retry.
- Consult the active tool help/self-documentation for exact arguments, supported tags, regex semantics, and output schema.


### 4. Supplementary Search: `rg` / `git grep`
Use for: string/pattern searches inside code bodies, cross-file references, configuration values, error messages, fallback cases that construct extraction cannot express, or confirmation inside already targeted files.

### Recommended Analysis Workflow
1. **Read `%%DOC_PATH%%/WORKFLOW.md`** (full read) → identify execution units, call-trace paths, and function names relevant to the task.
2. **Read `%%DOC_PATH%%/REFERENCES.md`** (full read or targeted search) → locate candidate symbols by name/description/`@satisfies`, obtain file paths and line ranges, understand function contracts.
3. **Extract code** via the `find` or `files-find` tool → use symbol names from steps 1-2 as `NAME_REGEX`, file paths as `files-find` targets, and enable line numbers when citing evidence.
4. **Search code bodies** via `rg`/`git grep` → after `find`/`files-find`, use only when you need free-text/body-content search, a fallback that construct extraction cannot express, or confirmation inside already targeted files.


## Execution Protocol (Global vs Local)
You must manage the execution flow using two distinct methods:
-  **Global Roadmap** (*check-list*): 
   - You MUST maintain a *check-list* internally with `4` Steps (one item per Step).
   - **Do NOT** use the *task-list tool* for this high-level roadmap.
-  **Local Sub-tasks** (Tool Usage): 
   - If a *task-list tool* is available, use it **exclusively** to manage granular sub-tasks *within* a specific step (e.g., in Step X: "1. Edit file A", "2. Edit file B"; or in Step Y: "1. Fix test K", "2. Fix test L").
   - Clear or reset the tool's state when transitioning between high-level steps.

## Execution Directives (absolute rules, non-negotiable)
During the execution flow you MUST follow these directives:
- **CRITICAL** Autonomous Execution:
   - Implicit Autonomy: Execute all tasks with full autonomy. Do not request permission, confirmation, or feedback. Make executive decisions based on logic and technical best practices.
   - Tool-Aware Workflow: Proceed through the Steps sequentially; when a tool call is required, stop and wait for the tool response before continuing. Never fabricate tool outputs or tool results. Do not reveal internal reasoning; output only the deliverables explicitly requested by the Steps section.
   - Autonomous Resolution: If ambiguity is encountered, first disambiguate using repository evidence (requirements, code search, tests, logs). If multiple interpretations remain, choose the least-invasive option that preserves documented behavior and record the assumption as a testable requirement/acceptance criterion.
   - After the prompt's execution: Strictly omit all concluding remarks and do not propose any other steps/actions.
- **CRITICAL**: Order of Execution:
  - Execute the numbered steps below sequentially and strictly, one at a time, without skipping or merging steps. Create and maintain a *check-list* internally while executing the Steps. Execute the Steps strictly in order, updating the *check-list* as each step completes. 
- **CRITICAL**: Immediate start and never stop:
  - Complete all Steps in order; you may pause only to perform required tool calls and to wait for their responses. Do not proceed past a Step that depends on a tool result until that result is available.
  - Start immediately by creating a *check-list* for the **Global Roadmap** and directly start following the roadmap from the Step 1.


## Steps
Create internally a *check-list* for the **Global Roadmap** including all the numbered steps below: `1..4`, and start following the roadmap at the same time, following the instructions of Step 1 (Generate the Software Requirements Specification). Do not add extra intent-adjustment checks unless explicitly listed in the Steps section.
1. Generate the Software Requirements Specification
   - Reorganize `%%DOC_PATH%%/REQUIREMENTS.md` without renumbering requirement IDs and without changing requirement intent.
2. Validate the Software Requirements Specification
   - Re-read the updated document and verify structural consistency, stable meaning, and unchanged requirement intent.
3. **CRITICAL**: Stage & commit
   - Show a summary of changes with `git diff` and `git diff --stat`.
   - Stage only `%%DOC_PATH%%/REQUIREMENTS.md`.
   - Ensure there is something to commit with: `git diff --cached --quiet && echo "Nothing to commit. Aborting."`. If command output contains "Aborting", OUTPUT exactly "No changes to commit.", and then terminate the execution.
   - Commit with `git commit -m "docs(<COMPONENT>)<BREAKING>: <DESCRIPTION> [useReq]"`; do not include AI attribution; a GPG-signed commit is not required.
4. Present results
   - PRINT the final report using the fixed report schema and final status line.
