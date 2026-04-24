"""
@brief Verifies title-first standalone Markdown document layout.
@details Checks repository Markdown documents that are consumed as
standalone assets and asserts two invariants: the first line starts with a
level-1 title marker and the document does not start with YAML front matter.
Excludes `src/instructions/*.md` because those files are reusable injected
snippets rather than standalone documents. Complexity: O(N) file reads for N
tracked standalone Markdown documents.
@satisfies TST-047, TST-048
"""

from __future__ import annotations

from pathlib import Path
import unittest

#: @brief Repository root directory.
#: @details Resolves the current test file ancestry to the repository root.
_REPO_ROOT = Path(__file__).resolve().parents[1]

#: @brief Glob patterns for standalone Markdown documents.
#: @details Covers root docs, canonical docs, bundled prompts, and bundled
#: templates that must satisfy the title-first/no-front-matter contract.
_STANDALONE_GLOB_PATTERNS = (
    "README.md",
    "CHANGELOG.md",
    "TODO.md",
    "pi-usereq/docs/*.md",
    "src/prompts/*.md",
    "src/docs/*.md",
)


def _collect_standalone_markdown_paths() -> list[Path]:
    """
    @brief Collects standalone Markdown documents under test.
    @details Expands explicit repository-relative glob patterns, deduplicates
    matched paths, and returns them in sorted repository-relative order.
    @return {list[pathlib.Path]} Sorted standalone Markdown paths.
    @satisfies TST-047, TST-048
    """
    document_paths: set[Path] = set()
    for pattern in _STANDALONE_GLOB_PATTERNS:
        document_paths.update(_REPO_ROOT.glob(pattern))
    return sorted(document_paths)


class MarkdownDocumentLayoutTest(unittest.TestCase):
    """
    @brief Verifies standalone Markdown document layout constraints.
    @details Executes repository-wide checks for leading level-1 titles and
    YAML-front-matter removal across standalone prompt/template documents and
    canonical Markdown docs.
    @satisfies TST-047, TST-048
    """

    def test_documents_start_with_level_one_title(self) -> None:
        """
        @brief Verifies every standalone Markdown document starts with `# `.
        @details Reads each target document and asserts that the first line uses
        the required level-1 Markdown title prefix.
        @return {None} No return value.
        @satisfies TST-047
        """
        for document_path in _collect_standalone_markdown_paths():
            document_text = document_path.read_text(encoding="utf-8")
            document_lines = document_text.splitlines()
            with self.subTest(document=document_path.relative_to(_REPO_ROOT)):
                self.assertTrue(document_lines)
                self.assertTrue(document_lines[0].startswith("# "))

    def test_documents_omit_yaml_front_matter(self) -> None:
        """
        @brief Verifies standalone Markdown documents do not start with YAML.
        @details Reads each target document and asserts that the initial bytes do
        not match the canonical YAML front-matter delimiter.
        @return {None} No return value.
        @satisfies TST-048
        """
        for document_path in _collect_standalone_markdown_paths():
            document_text = document_path.read_text(encoding="utf-8")
            with self.subTest(document=document_path.relative_to(_REPO_ROOT)):
                self.assertFalse(document_text.startswith("---\n"))


if __name__ == "__main__":
    unittest.main()
