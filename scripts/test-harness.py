#!/usr/bin/env python3
"""Offline maintenance tests; temporary fixtures never touch wiki/ or sources/."""
import importlib.util
import json
import tempfile
import tomllib
import unittest
from pathlib import Path


def load(filename):
    spec = importlib.util.spec_from_file_location(filename, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sync = load('sync-harness.py')
review = load('verification-record.py')


class HarnessTests(unittest.TestCase):
    def test_generated_agent_preserves_tex_and_unicode(self):
        outputs = sync.render(sync.ROOT)
        agent = tomllib.loads(outputs['.codex/agents/paper-analyst.toml'])
        body = outputs['.claude/agents/paper-analyst.md'].split('---\n', 2)[2].strip() + '\n'
        self.assertEqual(agent['developer_instructions'], body)
        self.assertIn('\\documentclass', body)
        self.assertIn('→', body)

    def test_frontends_differ_only_at_schema_reference(self):
        outputs = sync.render(sync.ROOT)
        self.assertEqual(outputs['AGENTS.md'].replace('AGENTS.md            this schema',
                         'CLAUDE.md            this schema'), outputs['CLAUDE.md'])
        for key, value in outputs.items():
            if key.startswith('.agents/skills/'):
                self.assertEqual(value.replace('AGENTS.md', 'CLAUDE.md'),
                                 outputs[key.replace('.agents/', '.claude/', 1)])

    def test_record_is_scoped_append_only_and_detects_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / 'wiki/papers/example.md'
            source = root / 'sources/arxiv/example/main.tex'
            for path in (page, source):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'original\r\n')
            manifest = dict(target='example', reviewer='agent; model unknown',
                            scope='R1 only', outcome='unresolved',
                            findings=[{'claim': 'R1', 'resolved': False}],
                            pages=[page.relative_to(root).as_posix()],
                            sources=[source.relative_to(root).as_posix()])
            first = review.record(root, manifest)
            original = first.read_bytes()
            data = json.loads(original)
            self.assertEqual(review.state(root, data), ('current', []))
            self.assertEqual(data['outcome'], 'unresolved')
            page.write_bytes(b'original\n')  # Exact bytes, including newline changes.
            self.assertEqual(review.state(root, data)[0], 'stale')
            second = review.record(root, manifest)
            self.assertNotEqual(first, second)
            self.assertEqual(first.read_bytes(), original)
            source.unlink()
            self.assertIn(manifest['sources'][0], review.state(root, data)[1])

    def test_rejects_outside_paths_and_empty_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            outside = root / 'private.txt'
            outside.write_text('test', encoding='utf-8')
            with self.assertRaises(ValueError):
                review.digest(root, 'wiki/../private.txt', 'wiki')
            with self.assertRaises(ValueError):
                review.record(root, dict(target='x', reviewer='x', scope='', outcome='clean',
                                         findings=[], pages=['x'], sources=['x']))


if __name__ == '__main__':
    unittest.main()
