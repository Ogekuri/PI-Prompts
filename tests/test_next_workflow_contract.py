"""
@brief Verifies next_workflow/next_commands emission-consistency contract.
@details Reproducer for the defect where bundled prompts could describe
required or suggested follow-up actions in `next_workflow` while emitting an
empty `next_commands` array. Asserts that every bundled prompt under
`src/prompts/` carries the shared CRITICAL consistency bullet, that the two
clarified `next_commands` contract bullets stay byte-identical across prompts
(DES-002, REQ-023, REQ-074, REQ-076), and that `analyze.md` defines the
Step 2 decision gate with an operationally defined trigger. Reads repository
Markdown documents as deterministic read-only fixtures.
Complexity: O(N) file reads for N bundled prompts.
@satisfies REQ-068, REQ-069, ANZ-STP-005, ANZ-STP-007
"""

from __future__ import annotations

from pathlib import Path
import unittest

#: @brief Repository root directory.
#: @details Resolves the repository root from this test file ancestry.
_REPO_ROOT = Path(__file__).resolve().parents[1]

#: @brief Directory containing the bundled prompt documents.
#: @details All bundled prompts share the final JSON output contract bullets.
_PROMPTS_DIR = _REPO_ROOT / "src" / "prompts"

#: @brief Expected shared CRITICAL consistency bullet.
#: @details Byte-exact line required in every bundled prompt under
#: `src/prompts/` by the next_workflow/next_commands emission contract.
_CONSISTENCY_BULLET = (
    "- **CRITICAL**: `next_workflow` and `next_commands` MUST agree before "
    "emission: if `next_workflow` describes any required or suggested "
    "follow-up action, the corresponding workflow-defined follow-up MUST be "
    "classified as triggered and its exact slash command MUST be present in "
    "`next_commands`; if `next_commands` is `[]`, `next_workflow` MUST state "
    "that no next action is required; MUST NOT describe an outcome-identified "
    "necessary follow-up action as optional or elective, MUST NOT invent "
    "follow-up actions outside the workflow-defined follow-up commands, and "
    "MUST execute this consistency cross-check immediately before emitting "
    "the final JSON response."
)

#: @brief Expected clarification clause in the shared field bullet.
#: @details Byte-exact sentence appended to the `next_commands` field
#: definition in every bundled prompt.
_FIELD_BULLET_CLAUSE = (
    "A follow-up action identified by this workflow's outcome as the correct "
    "next step is outcome-mandated and MUST NOT be classified as optional."
)

#: @brief Expected clarification clause in the present-results step bullet.
#: @details Byte-exact clause inserted into the present-results step bullet in
#: every bundled prompt.
_STEP_BULLET_CLAUSE = (
    "a follow-up action identified by this workflow's outcome as the correct "
    "next step is outcome-mandated and MUST NOT be omitted as optional"
)

#: @brief Expected decision-gate lead sentence in analyze.md Step 2.
#: @details Byte-exact prefix of the analyze-specific classification gate.
_DECISION_GATE_PREFIX = (
    "   - Decision gate: when Step 1 identifies ANY needed follow-up "
    "modification"
)

#: @brief Expected operationally defined trigger sentence in analyze.md.
#: @details Byte-exact sentence replacing the undefined trigger wording.
_TRIGGER_SENTENCE = (
    "If no needed follow-up modification is identified per the decision "
    "gate, use an empty array."
)


def _collect_prompt_texts() -> list[tuple[str, str]]:
    """
    @brief Collects bundled prompt documents as read-only fixtures.
    @details Reads every Markdown file under `src/prompts/` and returns
    name/text pairs sorted by file name.
    @return {list[tuple[str, str]]} Sorted (file name, document text) pairs.
    @satisfies REQ-074
    """
    prompt_paths = sorted(_PROMPTS_DIR.glob("*.md"))
    return [(path.name, path.read_text(encoding="utf-8")) for path in prompt_paths]


class NextWorkflowContractTest(unittest.TestCase):
    """
    @brief Verifies the shared next_workflow/next_commands contract invariants.
    @details Level 1 document-compliance checks: presence and cross-file
    byte-identity of the shared contract bullets plus analyze-specific
    decision-gate coverage.
    @satisfies REQ-068, REQ-069, ANZ-STP-005, ANZ-STP-007
    """

    def _lines_containing(self, fragment: str) -> list[str]:
        """
        @brief Collects every prompt line containing a fragment.
        @details Scans all bundled prompt documents and gathers the exact
        lines containing the requested fragment.
        @param {str} fragment Literal line fragment to search for.
        @return {list[str]} Matching lines across all bundled prompts.
        """
        matched_lines: list[str] = []
        for _, document_text in _collect_prompt_texts():
            for line in document_text.splitlines():
                if fragment in line:
                    matched_lines.append(line)
        return matched_lines

    def test_prompts_contain_consistency_bullet(self) -> None:
        """
        @brief Verifies every bundled prompt contains the consistency bullet.
        @details Arranges the bundled prompt documents, acts by reading each
        document, and asserts the exact shared CRITICAL consistency bullet is
        present; expected outcome is full presence across all 15 prompts.
        @return {None} No return value.
        @satisfies REQ-068, REQ-069, REQ-074
        """
        prompt_texts = _collect_prompt_texts()
        self.assertEqual(len(prompt_texts), 15)
        for prompt_name, document_text in prompt_texts:
            with self.subTest(document=prompt_name):
                self.assertIn(_CONSISTENCY_BULLET, document_text)

    def test_consistency_bullet_is_byte_identical(self) -> None:
        """
        @brief Verifies the consistency bullet has exactly one shared variant.
        @details Asserts that the lines carrying the consistency bullet form a
        single byte-identical variant across all bundled prompts.
        @return {None} No return value.
        @satisfies DES-002, REQ-023, REQ-076
        """
        bullet_lines = self._lines_containing("MUST agree before emission")
        self.assertEqual(len(bullet_lines), 15)
        self.assertEqual(len(set(bullet_lines)), 1)
        self.assertEqual(set(bullet_lines), {_CONSISTENCY_BULLET})

    def test_field_bullet_clarification_is_byte_identical(self) -> None:
        """
        @brief Verifies the field bullet clarification is present and unique.
        @details Asserts that the `next_commands` field-definition bullet
        carries the outcome-mandated clarification in exactly one shared
        byte-identical variant across all bundled prompts.
        @return {None} No return value.
        @satisfies REQ-064, REQ-065, DES-002, REQ-023
        """
        clause_lines = self._lines_containing("MUST NOT be classified as optional")
        self.assertEqual(len(clause_lines), 15)
        self.assertEqual(len(set(clause_lines)), 1)
        self.assertIn(_FIELD_BULLET_CLAUSE, clause_lines[0])

    def test_step_bullet_clarification_is_byte_identical(self) -> None:
        """
        @brief Verifies the step bullet clarification is present and unique.
        @details Asserts that the present-results step bullet carries the
        outcome-mandated clarification in exactly one shared byte-identical
        variant across all bundled prompts.
        @return {None} No return value.
        @satisfies REQ-064, REQ-065, DES-002, REQ-023
        """
        clause_lines = self._lines_containing("MUST NOT be omitted as optional")
        self.assertEqual(len(clause_lines), 15)
        self.assertEqual(len(set(clause_lines)), 1)
        self.assertIn(_STEP_BULLET_CLAUSE, clause_lines[0])

    def test_analyze_decision_gate_is_defined(self) -> None:
        """
        @brief Verifies analyze.md defines the Step 2 decision gate.
        @details Asserts that `src/prompts/analyze.md` contains the decision
        gate lead sentence and the operationally defined no-trigger sentence.
        @return {None} No return value.
        @satisfies ANZ-STP-005, ANZ-STP-007
        """
        analyze_entries = [
            text for name, text in _collect_prompt_texts() if name == "analyze.md"
        ]
        self.assertEqual(len(analyze_entries), 1)
        self.assertIn(_DECISION_GATE_PREFIX, analyze_entries[0])
        self.assertIn(_TRIGGER_SENTENCE, analyze_entries[0])


if __name__ == "__main__":
    unittest.main()
