#!/usr/bin/env python3
"""Internal maintenance: render both CLI front-ends from harness/, or check drift."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def render(root):
    source = root / 'harness'
    schema = (source / 'schema.md').read_text(encoding='utf-8')
    outputs = {'AGENTS.md': schema, 'CLAUDE.md': schema.replace('{{SCHEMA}}', 'CLAUDE.md')}
    outputs['AGENTS.md'] = schema.replace('{{SCHEMA}}', 'AGENTS.md')
    for skill in sorted((source / 'skills').glob('*/SKILL.md')):
        body = skill.read_text(encoding='utf-8')
        for folder, name in [('.agents', 'AGENTS.md'), ('.claude', 'CLAUDE.md')]:
            outputs[f'{folder}/skills/{skill.parent.name}/SKILL.md'] = body.replace('{{SCHEMA}}', name)
    analyst = (source / 'paper-analyst.md').read_text(encoding='utf-8')
    outputs['.claude/agents/paper-analyst.md'] = analyst
    header, body = analyst.split('---\n', 2)[1:]
    fields = dict(line.split(': ', 1) for line in header.strip().splitlines())
    outputs['.codex/agents/paper-analyst.toml'] = '\n'.join(
        f'{key} = {json.dumps(value, ensure_ascii=False)}' for key, value in [
            ('name', fields['name']), ('description', fields['description']),
            ('developer_instructions', body.strip() + '\n')]) + '\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changed = []
    for relative, content in render(ROOT).items():
        path = ROOT / relative
        if path.exists() and path.read_text(encoding='utf-8') == content:
            continue
        changed.append(relative)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
    if args.check and changed:
        print('FAIL: generated harness differs: ' + ', '.join(changed))
        return 1
    print(f'OK: harness {"consistent" if args.check else "rendered"} ({len(changed)} changes)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
