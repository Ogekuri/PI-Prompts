# PI-Prompts References

## Source Surface Summary
- Source root: `src`
- Source kind: static Markdown resources only; bundled standalone prompt/template documents start with level-1 titles and omit YAML front matter
- Executable source symbols under `src`: none detected
- Prompt resources under `src/prompts`: 15 standalone Markdown prompt documents with leading level-1 titles
- Template resources under `src/docs`: 3 standalone Markdown documents
- Instruction resources under `src/instructions`: 2 reusable Markdown instruction snippets
- Removed prompt in this revision: `src/prompts/references.md`

## Files Structure
```text
src/
├── docs/
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

## Resource Index

### `src/prompts`
| Path | Lines | Purpose |
| --- | ---: | --- |
| `src/prompts/analyze.md` | 122 | Read-only investigation workflow that produces an evidence-backed analysis report. |
| `src/prompts/change.md` | 182 | Requirements-change workflow that updates the SRS, implements the change, verifies it, and refreshes workflow/reference docs. |
| `src/prompts/check.md` | 130 | Repository-read-only compliance audit workflow that evaluates every requirement ID. |
| `src/prompts/cover.md` | 174 | Minimal implementation workflow for uncovered existing requirement IDs without changing the SRS. |
| `src/prompts/create.md` | 98 | Source-grounded workflow that writes or updates `REQUIREMENTS.md` from implementation evidence. |
| `src/prompts/fix.md` | 176 | Defect-remediation workflow that restores behavior without changing requirements. |
| `src/prompts/flowchart.md` | 178 | Docs-only workflow that regenerates `FLOWCHART.md` from source evidence. |
| `src/prompts/implement.md` | 120 | Greenfield or major-gap workflow that builds implementation from an authoritative SRS without editing requirements. |
| `src/prompts/new.md` | 181 | Additive-feature workflow that appends new requirement IDs and implements the corresponding behavior. |
| `src/prompts/readme.md` | 139 | Docs-only workflow that aligns root `README.md` with user-visible implementation evidence. |
| `src/prompts/recreate.md` | 175 | Reorganization workflow that rebuilds the SRS from source evidence while preserving existing requirement IDs. |
| `src/prompts/refactor.md` | 168 | Internal-improvement workflow that preserves observable behavior and keeps requirements unchanged. |
| `src/prompts/renumber.md` | 81 | Deterministic renumbering workflow for requirement IDs and internal requirement cross-references. |
| `src/prompts/workflow.md` | 159 | Docs-only workflow that regenerates `WORKFLOW.md` from source evidence. |
| `src/prompts/write.md` | 93 | Greenfield workflow that drafts `REQUIREMENTS.md` directly from user intent. |

### `src/docs`
| Path | Lines | Purpose |
| --- | ---: | --- |
| `src/docs/Document_Source_Code_in_Doxygen_Style.md` | 130 | Parser-first Doxygen documentation standard for source-code comments and metadata. |
| `src/docs/HDT_Test_Authoring_Guide.md` | 318 | Deterministic HDT unit-test authoring guide for Generator and Refactorer modes. |
| `src/docs/Requirements_Template.md` | 58 | Canonical template for authoring or rebuilding `REQUIREMENTS.md`. |

### `src/instructions`
| Path | Lines | Purpose |
| --- | ---: | --- |
| `src/instructions/git_commit.md` | 16 | Reusable commit-workflow instruction block injected through `%%COMMIT%%`. |
| `src/instructions/git_read-only.md` | 2 | Reusable git read-only restriction block for analysis-only workflows. |

## Symbol Status
- Internal functions/classes/modules under `src`: none detected.
- Reason: every tracked file under `src` in this revision is Markdown content intended for prompt delivery, documentation templating, or instruction injection.
- Implication: navigation in this repository is file-oriented rather than symbol-oriented.
