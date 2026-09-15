#!/usr/bin/env python3
"""Compact wiki candidate search for ingest reconciliation.

Searches filenames, frontmatter, and Index summaries locally, but prints only a small ranked
candidate set so an ingest does not have to load the full Index into model context.
"""
import argparse
import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

try:
    import yaml
except ImportError:  # The frontmatter checker has the same optional dependency.
    yaml = None


ROOT = Path(__file__).resolve().parent.parent
INDEX_ENTRY = re.compile(r"^- \[\[([^\]|#]+)(?:\|[^\]]+)?\]\]\s+[—-]\s+(.*)$")


def normalized(value):
    value = unicodedata.normalize("NFKD", str(value)).casefold()
    value = value.replace("_", " ").replace("-", " ")
    return " ".join(re.findall(r"[a-z0-9]+", value))


def tokens(value):
    return {part for part in normalized(value).split() if len(part) > 1}


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0 or yaml is None:
        return {}
    try:
        data = yaml.safe_load(text[4:end])
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def index_summaries(root):
    summaries = {}
    for line in (root / "Index.md").read_text(encoding="utf-8").splitlines():
        match = INDEX_ENTRY.match(line)
        if match:
            summaries[match.group(1)] = match.group(2)
    return summaries


def records(root):
    summaries = index_summaries(root)
    for path in sorted((root / "wiki").rglob("*.md")):
        meta = read_frontmatter(path)
        relative = path.relative_to(root).as_posix()
        slug = path.stem
        aliases = meta.get("aliases") or []
        tags = meta.get("tags") or []
        if not isinstance(aliases, list):
            aliases = [aliases]
        if not isinstance(tags, list):
            tags = [tags]
        yield {
            "path": relative,
            "slug": slug,
            "title": str(meta.get("title") or slug),
            "type": str(meta.get("type") or path.parent.name.rstrip("s")),
            "aliases": [str(item) for item in aliases],
            "tags": [str(item) for item in tags],
            "summary": summaries.get(slug, ""),
        }


def score(query, record):
    needle = normalized(query)
    if not needle:
        return 0
    primary = [record["slug"], record["title"], *record["aliases"]]
    secondary = [*record["tags"], record["summary"]]
    primary_norm = [normalized(value) for value in primary]
    secondary_norm = [normalized(value) for value in secondary]
    if needle in primary_norm:
        return 200
    result = 0.0
    if any(needle in value or (len(value) >= 6 and value in needle)
           for value in primary_norm if value):
        result = max(result, 120)
    if any(needle in value for value in secondary_norm if value):
        result = max(result, 60)
    query_tokens = tokens(query)
    if query_tokens:
        for weight, values in ((80, primary_norm), (35, secondary_norm)):
            for value in values:
                overlap = len(query_tokens & tokens(value)) / len(query_tokens)
                result = max(result, weight * overlap)
    for value in primary_norm:
        if value:
            result = max(result, 45 * SequenceMatcher(None, needle, value).ratio())
    return round(result, 1)


def search(root, queries, limit):
    catalog = list(records(root))
    output = []
    for query in queries:
        ranked = sorted(((score(query, item), item) for item in catalog),
                        key=lambda pair: (-pair[0], pair[1]["path"]))
        output.append((query, [pair for pair in ranked if pair[0] >= 18][:limit]))
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queries", nargs="+", help="entity slug or distinctive name")
    parser.add_argument("--limit", type=int, default=8, help="candidates per query")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    for query, matches in search(args.root.resolve(), args.queries, args.limit):
        print(f"QUERY: {query}")
        if not matches:
            print("  (no plausible title/alias/Index candidate)")
            continue
        for rank, (value, item) in enumerate(matches, 1):
            aliases = f"; aliases={', '.join(item['aliases'])}" if item["aliases"] else ""
            print(f"  {rank}. [{value:g}] {item['path']} | {item['type']} | {item['title']}{aliases}")
            if item["summary"]:
                print(f"     Index: {item['summary']}")


if __name__ == "__main__":
    main()
