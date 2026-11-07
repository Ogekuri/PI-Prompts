"""
@brief Verifies Node24-or-later runtime constraints of release automation.
@details Checks the tracked GitHub Actions release workflow asset against the
runtime requirement group: every job runs on Node24 or later with no Node20
fallback or transitional forcing variables, every JavaScript-based action
reference pins a Node24-or-later runtime version, release behavior remains
structurally preserved across the migration, and jobs target GitHub-hosted
`ubuntu-latest` runners only. Complexity: O(N) line scans over a single
workflow asset for N text lines.
@satisfies ACT-001, ACT-002, ACT-003, ACT-004
"""

from __future__ import annotations

import re
from pathlib import Path
import unittest

#: @brief Repository root directory.
#: @details Resolves the current test file ancestry to the repository root.
_REPO_ROOT = Path(__file__).resolve().parents[1]

#: @brief Relative path of the release workflow asset under test.
#: @details Single tracked automation artifact governed by requirement group ACT.
_WORKFLOW_RELATIVE_PATH = Path(".github/workflows/release-markdown.yml")

#: @brief Exact action references whose declared runtime is Node24 or later.
#: @details Membership is the complete allowlist for `uses:` references; any
#: other reference fails the check to keep runtime upgrades explicit.
_NODE24_ACTION_ALLOWLIST = frozenset(
    {
        "actions/checkout@v5",
        "mikepenz/release-changelog-builder-action@v6",
        "softprops/action-gh-release@v3",
    }
)

#: @brief Case-insensitive literals forbidden in workflow automation text.
#: @details Encodes the Node20 runtime, the transitional Node24-forcing
#: variable, and the Node20 opt-out variable that must not appear.
_FORBIDDEN_RUNTIME_LITERALS = (
    "node20",
    "force_javascript_actions_to_node24",
    "actions_allow_use_unsecure_node_version",
)

#: @brief Regex extracting `uses:` action references from workflow lines.
#: @details Tolerates list-item prefixes and surrounding quotes; captures the
#: `owner/repo@ref` token.
_USES_PATTERN = re.compile(r"^\s*(?:-\s+)?uses:\s*[\"']?(\S+?)[\"']?\s*$")

#: @brief Regex extracting `runs-on:` runner selectors from workflow lines.
#: @details Tolerates list-item prefixes and surrounding quotes; captures the
#: runner label token.
_RUNS_ON_PATTERN = re.compile(r"^\s*(?:-\s+)?runs-on:\s*[\"']?(\S+?)[\"']?\s*$")


def _load_workflow_text() -> str:
    """
    @brief Loads the release workflow asset text.
    @details Reads the tracked workflow file as UTF-8 text exactly once per
    call; performs no normalization beyond raw file content.
    @return {str} Raw workflow file content.
    @satisfies ACT-001, ACT-002, ACT-003, ACT-004
    """
    return (_REPO_ROOT / _WORKFLOW_RELATIVE_PATH).read_text(encoding="utf-8")


def _extract_pattern_matches(workflow_text: str, pattern: re.Pattern[str]) -> list[str]:
    """
    @brief Extracts ordered capture values from workflow lines.
    @details Applies the given line-oriented pattern to every workflow line and
    returns captured tokens in document order.
    @param workflow_text {str} Raw workflow file content.
    @param pattern {re.Pattern[str]} Compiled single-capture line pattern.
    @return {list[str]} Captured tokens in document order.
    @satisfies ACT-002, ACT-004
    """
    return [
        match.group(1)
        for match in (pattern.match(line) for line in workflow_text.splitlines())
        if match is not None
    ]


class ReleaseWorkflowRuntimeTest(unittest.TestCase):
    """
    @brief Verifies release automation runtime constraints.
    @details Executes atomic text checks against the single tracked release
    workflow asset; all checks are deterministic, read-only, and independent.
    @satisfies ACT-001, ACT-002, ACT-003, ACT-004
    """

    def test_workflow_asset_exists(self) -> None:
        """
        @brief Verifies the release workflow asset is present at its canonical path.
        @details Asserts the tracked automation artifact exists before any
        content-level check runs, giving a precise failure for missing assets.
        @return {None} No return value.
        @satisfies ACT-001
        """
        # Arrange
        workflow_path = _REPO_ROOT / _WORKFLOW_RELATIVE_PATH
        # Act
        asset_exists = workflow_path.is_file()
        # Assert
        self.assertTrue(asset_exists, "release workflow asset must exist")

    def test_workflow_text_excludes_node20_fallback_literals(self) -> None:
        """
        @brief Verifies workflow text contains no Node20 fallback or forcing literals.
        @details Scans the workflow content case-insensitively for the Node20
        runtime literal, the transitional Node24-forcing variable, and the
        Node20 opt-out variable; any occurrence fails with its offending literal.
        @return {None} No return value.
        @satisfies ACT-001
        """
        # Arrange
        workflow_text = _load_workflow_text().lower()
        # Act
        occurrences = {
            literal
            for literal in _FORBIDDEN_RUNTIME_LITERALS
            if literal in workflow_text
        }
        # Assert
        self.assertEqual(set(), occurrences)

    def test_action_references_use_node24_capable_versions(self) -> None:
        """
        @brief Verifies every `uses:` reference is in the Node24 allowlist.
        @details Extracts all `uses:` tokens in document order and asserts each
        matches the verified Node24-or-later allowlist exactly; empty reference
        sets also fail to prevent silent contract loss.
        @return {None} No return value.
        @satisfies ACT-002
        """
        # Arrange
        workflow_text = _load_workflow_text()
        expected_references = set(_NODE24_ACTION_ALLOWLIST)
        # Act
        action_references = _extract_pattern_matches(workflow_text, _USES_PATTERN)
        # Assert
        self.assertTrue(action_references, "at least one action reference must exist")
        for action_reference in action_references:
            with self.subTest(action=action_reference):
                self.assertIn(action_reference, expected_references)

    def test_jobs_run_on_ubuntu_latest_hosted_runners(self) -> None:
        """
        @brief Verifies every job targets the `ubuntu-latest` hosted runner.
        @details Extracts all `runs-on:` selectors in document order and asserts
        each equals the GitHub-hosted Linux label, excluding Node24-incompatible
        macOS and ARM32 targets.
        @return {None} No return value.
        @satisfies ACT-004
        """
        # Arrange
        workflow_text = _load_workflow_text()
        expected_runner = "ubuntu-latest"
        # Act
        runner_selectors = _extract_pattern_matches(workflow_text, _RUNS_ON_PATTERN)
        # Assert
        self.assertTrue(runner_selectors, "at least one runner selector must exist")
        for runner_selector in runner_selectors:
            with self.subTest(runner=runner_selector):
                self.assertEqual(expected_runner, runner_selector)

    def test_release_behavior_contract_is_preserved(self) -> None:
        """
        @brief Verifies structural release-behavior keys survive the migration.
        @details Asserts the canonical-version tag trigger, the branch-gate job
        with its `needs` edge, the changelog step in COMMIT mode, the release
        step uploading `src/**/*` with unmatched-file failure, and the
        contents/id-token/attestations write permissions remain present.
        @return {None} No return value.
        @satisfies ACT-003
        """
        # Arrange
        workflow_text = _load_workflow_text()
        expected_contract_fragments = (
            "'v[0-9]+.[0-9]+.[0-9]+'",
            "check-branch:",
            "build-release:",
            "needs: check-branch",
            "is_master: ${{ steps.check.outputs.is_master }}",
            "if: needs.check-branch.outputs.is_master == 'true'",
            'mode: "COMMIT"',
            "files: src/**/*",
            "fail_on_unmatched_files: true",
            "generate_release_notes: false",
            "permissions:",
            "contents: write",
            "id-token: write",
            "attestations: write",
        )
        # Act
        missing_fragments = {
            fragment
            for fragment in expected_contract_fragments
            if fragment not in workflow_text
        }
        # Assert
        self.assertEqual(set(), missing_fragments)


if __name__ == "__main__":
    unittest.main()
