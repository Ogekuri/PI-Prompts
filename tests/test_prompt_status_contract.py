"""
@brief Verifies final status-line emission on every prompt termination path.
@details Scans bundled prompt documents under `src/prompts` and the shared
commit-instruction snippet under `src/instructions`, selects every line that
instructs execution termination or final-line override, and asserts that each
selected line also instructs an exact `STATUS: OK` or `STATUS: ERROR` final
line. Rejects responses that end with an error string, a no-op message, or a
git warning without a status line.
Complexity: O(L) line scans for L lines across the selected documents.
@satisfies REQ-002, REQ-043
"""

from __future__ import annotations

from pathlib import Path
import unittest

#: @brief Repository root directory.
#: @details Resolves the current test file ancestry to the repository root.
_REPO_ROOT = Path(__file__).resolve().parents[1]

#: @brief Documents that declare prompt termination or final-line behavior.
#: @details Covers all bundled prompts and the shared commit workflow block.
_TERMINATION_GLOB_PATTERNS = (
    "src/prompts/*.md",
    "src/instructions/git_commit.md",
)

#: @brief Text fragments identifying a termination or final-line override path.
#: @details Any selected line must also declare an exact final status line.
_TERMINATION_MARKERS = (
    "terminate the execution",
    "terminate execution",
    "override the final line",
)

#: @brief Permitted exact final status lines.
_FINAL_STATUS_MARKERS = ("STATUS: OK", "STATUS: ERROR")


def _collect_termination_documents() -> list[Path]:
    """
    @brief Collects documents that declare termination behavior.
    @details Expands repository-relative glob patterns to absolute document
    paths, deduplicates matches, and returns them in sorted path order.
    @return {list[pathlib.Path]} Sorted termination-contract documents.
    @satisfies REQ-002
    """
    document_paths: set[Path] = set()
    for pattern in _TERMINATION_GLOB_PATTERNS:
        document_paths.update(_REPO_ROOT.glob(pattern))
    return sorted(document_paths)


def _collect_termination_contracts(
    document_path: Path,
) -> list[tuple[int, str]]:
    """
    @brief Collects termination-contract lines from one document.
    @details Reads the document as UTF-8, enumerates 1-based line numbers, and
    retains lines containing any termination or final-line override marker.
    @param document_path {pathlib.Path} Document to scan.
    @return {list[tuple[int, str]]} Ordered (line_number, line_text) contracts.
    @throws {OSError} If the document cannot be read.
    @satisfies REQ-002
    """
    document_text = document_path.read_text(encoding="utf-8")
    contracts: list[tuple[int, str]] = []
    document_lines = document_text.splitlines()
    for line_number, line_text in enumerate(document_lines, start=1):
        if any(marker in line_text for marker in _TERMINATION_MARKERS):
            contracts.append((line_number, line_text))
    return contracts


class PromptTerminationStatusTest(unittest.TestCase):
    """
    @brief Verifies prompt termination paths preserve the status contract.
    @details Enforces that termination branches cannot end a response without
    the fixed report schema's exact final status line.
    @satisfies REQ-002, REQ-043
    """

    def test_termination_paths_emit_final_status_line(self) -> None:
        """
        @brief Asserts every termination path declares an exact final status.
        @details Iterates termination-contract lines across all collected
        documents and fails per line when neither `STATUS: OK` nor
        `STATUS: ERROR` is declared on that same instruction.
        @return {None} No return value.
        @satisfies REQ-002, REQ-043
        """
        documents = _collect_termination_documents()
        self.assertTrue(
            documents,
            msg="No termination-contract documents found.",
        )
        for document_path in documents:
            contracts = _collect_termination_contracts(document_path)
            for line_number, line_text in contracts:
                with self.subTest(
                    document=document_path.relative_to(_REPO_ROOT),
                    line=line_number,
                ):
                    self.assertTrue(
                        any(marker in line_text for marker in _FINAL_STATUS_MARKERS),
                        msg=(
                            f"{document_path.relative_to(_REPO_ROOT)}:"
                            f"{line_number} terminates without an exact "
                            "final status line."
                        ),
                    )
