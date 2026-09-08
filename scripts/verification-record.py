#!/usr/bin/env python3
"""Internal helper for wiki-verify (record) and wiki-lint (status); no model calls."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def digest(root, relative, prefix):
    path = (root / relative).resolve()
    base = (root / prefix).resolve()
    if not path.is_relative_to(base) or not path.is_file():
        raise ValueError(f'Expected existing file under {prefix}/: {relative}')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(root, manifest):
    for field in ('target', 'reviewer', 'scope', 'outcome', 'findings', 'pages', 'sources'):
        if field not in manifest or (field != 'findings' and not manifest[field]):
            raise ValueError(f'Missing or empty {field}')
    if manifest['outcome'] not in ('clean', 'corrected', 'unresolved'):
        raise ValueError('outcome must be clean, corrected, or unresolved')
    if not isinstance(manifest['findings'], list):
        raise ValueError('findings must be a list (empty for clean)')
    for field in ('target', 'reviewer', 'scope'):
        if not isinstance(manifest[field], str):
            raise ValueError(f'{field} must be text')
    snapshots = {}
    for field, prefix in [('pages', 'wiki'), ('sources', 'sources')]:
        items = manifest[field]
        if not isinstance(items, list) or not all(isinstance(p, str) for p in items):
            raise ValueError(f'{field} must list file paths')
        snapshots[field] = {p: digest(root, p, prefix) for p in items}
    result = {key: manifest[key] for key in ('target', 'reviewer', 'scope', 'outcome', 'findings')}
    result.update(schema_version=1, checked_at=datetime.now(timezone.utc).isoformat(), **snapshots)
    dest = root / 'verification'
    dest.mkdir(parents=True, exist_ok=True)
    filename = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json'
    path = dest / filename
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    return path


def state(root, data):
    changes = []
    for field, prefix in [('pages', 'wiki'), ('sources', 'sources')]:
        if not isinstance(data.get(field), dict) or not data[field]:
            raise ValueError(f'Invalid record: missing {field} hashes')
        for relative, expected in data[field].items():
            try:
                actual = digest(root, relative, prefix)
            except ValueError:
                actual = None
            if actual != expected:
                changes.append(relative)
    return ('stale' if changes else 'current'), changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--record', type=Path, help='JSON manifest prepared after review and fixes')
    group.add_argument('--status', action='store_true', help='Check recorded file versions, not physics')
    args = parser.parse_args()
    if args.record:
        print(record(ROOT, json.loads(args.record.read_text(encoding='utf-8'))).relative_to(ROOT))
        return 0
    records = sorted((ROOT / 'verification').glob('*.json'))
    if not records:
        print('UNREVIEWED: no verification records (legacy reviews may exist in Log.md)')
    invalid = False
    for path in records:
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            status, changes = state(ROOT, data)
            print(f'{status.upper()} {path.name}: {data["target"]}; outcome={data["outcome"]}; scope={data["scope"]}')
            if changes:
                print('  changed/missing: ' + ', '.join(changes))
        except (ValueError, KeyError, TypeError, OSError) as error:
            print(f'INVALID {path.name}: {error}')
            invalid = True
    # Staleness is informational: on-demand verification is not an ingest gate.
    return int(invalid)


if __name__ == '__main__':
    raise SystemExit(main())
