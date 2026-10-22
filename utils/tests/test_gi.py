#!/usr/bin/env python3
"""Regression checks for inventory/validation semantics; no game or network access."""
from pathlib import Path
import tempfile
import unittest
import sys
import contextlib
import io

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check
import compare
import convars
import gi
import nondefaults
import stock_diff
import upstream_diff


FIXTURE = '''"GameInfo" {
    "ConVars" {
        example "1"
        // disabled "2" // retained candidate
        // END OF CONFIG
        // server_note "3"
        custom_after_marker "4"
        rate {
            min "98304"
            default "786432"
            max "1000000"
            // nested_disabled "5"
        }
        versioned { version "2" default "3" }
        example "6"
    }
}
'''


class InventoryTests(unittest.TestCase):
    def test_direct_inventory_and_real_tail(self):
        settings = gi.settings(FIXTURE.splitlines())
        self.assertEqual([(s.name, s.value, s.active, s.region) for s in settings], [
            ('example', '1', True, 'tweak'), ('disabled', '2', False, 'tweak'),
            ('server_note', '3', False, 'svdoc'), ('custom_after_marker', '4', True, 'tweak'),
            ('example', '6', True, 'tail'),
        ])

    def test_inline_blocks_and_multiple_assignments(self):
        text = 'GameInfo { ConVars { a "1" a "2" nested { min "3" } } }'
        self.assertEqual([(s.name, s.value) for s in gi.settings(text.splitlines())], [('a', '1'), ('a', '2')])

    def test_quoted_braces_do_not_change_depth(self):
        text = FIXTURE.replace('example "1"', 'example "{ // }"')
        self.assertEqual(len(gi.settings(text.splitlines())), 5)
        self.assertEqual(gi.convars_bounds(text.splitlines()), (1, 15))

    def test_missing_or_malformed_convars(self):
        for text in ('GameInfo { x "1" }', 'GameInfo { ConVars { x "1" }', 'GameInfo { ConVars { x } }'):
            with self.assertRaises(ValueError):
                gi.settings(text.splitlines())

    def test_bare_disabled_values_are_retained_without_treating_prose_as_settings(self):
        text = 'GameInfo {\nConVars {\n// boolean true\n// numeric 0.05\n// prose is not a setting\n}\n}'
        self.assertEqual([(s.name, s.value, s.active) for s in gi.settings(text.splitlines())],
                         [('boolean', 'true', False), ('numeric', '0.05', False)])

    def test_compare_preserves_direct_duplicates_and_separates_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.gi'
            path.write_text(FIXTURE)
            variables, metadata, duplicates = compare.load(path)
        self.assertEqual(variables['example'], ['1', '6'])
        self.assertNotIn('rate/min', variables)
        self.assertEqual(metadata['ConVars/rate/min'], '98304')
        self.assertEqual(duplicates, ['example'])

    def test_upstream_preserves_disabled_and_duplicate_assignments(self):
        state = upstream_diff.convar_state(FIXTURE)
        self.assertEqual(state['example'], [(True, '1'), (True, '6')])
        self.assertEqual(state['disabled'], [(False, '2')])
        self.assertNotIn('min', state)

    def test_duplicates_are_diagnostic_by_default_strict_when_requested(self):
        errors, warnings = [], []
        check.check_settings(FIXTURE.splitlines(), errors, warnings)
        self.assertFalse(errors)
        self.assertTrue(any('set 2 times' in warning for warning in warnings))
        check.check_settings(FIXTURE.splitlines(), errors, [], strict_duplicates=True)
        self.assertEqual(len(errors), 1)

    def test_dump_flags_ranges_and_unknown_scope(self):
        dump = gi.parse_dump('example 1 (archive, min: 0, max: 4)\n\tDescription.\n\nmissingflag 2 ()\n')
        self.assertEqual(dump['example'].flags, {'archive'})
        self.assertEqual(dump['example'].description, 'Description.')
        self.assertFalse(convars.in_range('5', dump['example']))
        self.assertEqual(convars.scope(dump['missingflag']), 'engine/unspecified')

    def test_stock_report_excludes_range_metadata_and_preserves_duplicates(self):
        self.assertEqual(nondefaults.stock_convars(FIXTURE), {'example': ['1', '6'], 'custom_after_marker': ['4']})

    def test_active_files_coverage_matches_keyvalues(self):
        for path in gi.config_paths('both'):
            lines = gi.read_lines(path)
            section = gi.gameinfo_root('\n'.join(lines)).section('ConVars')
            parsed = [(c.key, c.value, c.line) for c in section.children if c.value is not None]
            actual = [(s.name, s.value, s.line) for s in gi.settings(lines) if s.active]
            self.assertEqual(actual, parsed, str(path))

    def test_stock_compare_detects_conflict_even_when_duplicate_matches(self):
        stock = 'GameInfo { ConVars { example "1" } }'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.gi'
            path.write_text('GameInfo { ConVars { example "2" example "1" } }')
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = stock_diff.compare(path, stock)
        self.assertEqual(code, 0)  # Differences in ConVars are warnings, not structural errors.
        self.assertIn("ours '2'", output.getvalue())
        self.assertIn("1 warning(s)", output.getvalue())

    def test_stock_compare_includes_extra_nested_tail_metadata(self):
        ours = FIXTURE.replace('max "1000000"', 'max "1000000"\n            extra "7"')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'sample.gi'
            path.write_text(ours)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                stock_diff.compare(path, FIXTURE)
        self.assertIn('rate/extra', output.getvalue())

    def test_normalization_preserves_unknown_string_case(self):
        self.assertEqual(gi.normalize('TRUE'), '1')
        self.assertEqual(gi.normalize('1.0'), '1')
        self.assertNotEqual(gi.normalize('TextureName'), gi.normalize('texturename'))
        self.assertNotEqual(gi.normalize('one,two'), gi.normalize('one two'))

    def test_cache_refs_cannot_escape_cache_directory(self):
        self.assertEqual(gi.cache_ref('feature/test'), 'feature%2Ftest')
        self.assertNotIn('/', gi.cache_ref('../../other'))


if __name__ == '__main__':
    unittest.main()
