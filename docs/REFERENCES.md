# References

## Requirements Source

- `docs/REQUIREMENTS.md`: Canonical requirements set for prompt behavior, prompt inventory, and shared operational instructions.

## Updated Prompt Artifacts

- `src/prompts/flowchart.md`: Defines FLOWCHART-only maintenance workflow that generates `docs/FLOWCHART.md` as a Mermaid primary-flow graph, normalizes sibling-branch granularity, exposes hidden helper steps when required for comparability, and audits joins/skips against source evidence.

## Requirement Updates

- `docs/REQUIREMENTS.md`: Refines `FCH-STP-007` and adds `FCH-STP-011..017` for Step 4 control-flow deduction, sibling-branch normalization, hidden-step removal, skip validation, and strict pre-write audit rules.

## Workflow Model Update

- `docs/WORKFLOW.md`: No runtime-model change required; execution units and communication edges remain unchanged for this prompt-only Step 4 instruction update.
