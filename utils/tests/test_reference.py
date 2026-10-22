"""Coverage invariants for the full reference, including non-ConVar examples."""
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gi
import reference


class ReferenceTests(unittest.TestCase):
    def test_active_inventory_equals_ast_without_collapsing_lists(self):
        for file in reference.CONFIGS.values():
            with self.subTest(file=file):
                text = file.read_text(encoding="utf-8")
                rows, _ = reference.inventory(text)
                actual = [(r["path"], r["value"], r["line"]) for r in rows
                          if r["active"] and r["kind"] == "scalar"]
                expected = [("/".join(p), v, line) for p, v, line in gi.flatten(gi.gameinfo_root(text))]
                self.assertEqual(expected, actual)

    def test_disabled_context_empty_sections_and_nonsetting_comments(self):
        rows, sections = reference.inventory('''GameInfo
{
    Empty {}
    NetworkSystem
    {
        // FakeReorderPct 0.05
        // This is explanatory prose
        FakeReorderPct "0"
    }
    ConVars
    {
        // example true
        range { min "0" default "2" max "3" }
        // range is not a scalar setting
    }
}''')
        disabled = [(r["path"], r["value"]) for r in rows if not r["active"]]
        self.assertEqual(disabled, [("NetworkSystem/FakeReorderPct", "0.05"), ("ConVars/example", "true")])
        self.assertEqual([r["path"] for r in rows if r["kind"] == "empty section"], ["Empty"])
        self.assertIn({"path": "ConVars/range", "line": 13}, sections)

    def test_disabled_note_names_where_the_example_exists(self):
        disabled = {"active": False}
        both = reference.applicability(None, "ConVars/x", [[disabled], [disabled]])
        stable_only = reference.applicability(None, "ConVars/x", [[disabled], []])
        self.assertIn("Disabled in both current files", both)
        self.assertIn("Disabled in stable; not present in the other file", stable_only)
        self.assertNotIn("both current files", stable_only)

    def test_refresh_rejects_changed_source_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "source.txt"
            file.write_bytes(b"expected")
            manifest = {"files": {"source.txt": {"sha256": hashlib.sha256(b"expected").hexdigest()}}}
            self.assertEqual(reference.read_sources(manifest, directory), {"source.txt": "expected"})
            file.write_bytes(b"different snapshot")
            with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                reference.read_sources(manifest, directory)


if __name__ == "__main__":
    unittest.main()
