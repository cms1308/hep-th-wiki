#!/usr/bin/env python3
"""citation-links.py [--update] [safe-id]

Computes the citation graph among INGESTED papers (those with a wiki/papers/<safe-id>.md
page) using the refs.json files produced by inspire-fetch.sh.

With a safe-id argument: prints what that paper cites / is cited by, among wiki papers.
Without arguments: prints the full adjacency for every wiki paper (for lint/audit).
With --update and one safe-id: add the graph edges to both ends of every relation while
preserving manual links and prose already present in each Citation graph section.
"""
import argparse
import json
import re
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

VAULT = Path(__file__).resolve().parent.parent


def norm(arxiv_id: str) -> str:
    return arxiv_id.replace("/", "-")


def load_papers(vault=VAULT):
    """safe-id -> set of normalized arXiv ids it references (wiki papers only later)."""
    papers = {}
    source_root = vault / "sources" / "arxiv"
    if not source_root.exists():
        return papers
    for d in sorted(source_root.iterdir()):
        if not (vault / "wiki" / "papers" / f"{d.name}.md").exists():
            continue  # in sources but not integrated into the wiki
        refs_file = d / "refs.json"
        refs = set()
        if refs_file.exists():
            data = json.loads(refs_file.read_text(encoding="utf-8"))
            refs = {norm(r["arxiv"]) for r in data.get("references", []) if r.get("arxiv")}
        papers[d.name] = refs
    return papers


def report(target: str, papers: dict) -> None:
    if target not in papers:
        print(f"{target}: no wiki paper page (or no sources entry)")
        return
    cites = sorted(t for t in papers[target] if t in papers)
    cited_by = sorted(p for p, refs in papers.items() if target in refs)
    print(f"{target}")
    print(f"  cites (in wiki):    {', '.join(cites) if cites else '-'}")
    print(f"  cited by (in wiki): {', '.join(cited_by) if cited_by else '-'}")


def paper_metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n") or yaml is None:
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    try:
        data = yaml.safe_load(text[4:end])
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def author_year_label(path: Path, safe_id: str) -> str:
    meta = paper_metadata(path)
    aliases = meta.get("aliases") or []
    if not isinstance(aliases, list):
        aliases = [aliases]
    for alias in aliases:
        alias = str(alias)
        if re.search(r"\b(?:19|20)\d{2}[a-z]?\b", alias) and "[[" not in alias:
            return alias
    authors = meta.get("authors") or []
    if not isinstance(authors, list):
        authors = [authors]
    surnames = [str(author).strip().split()[-1] for author in authors if str(author).strip()]
    year_match = re.match(r"((?:19|20)\d{2})", str(meta.get("date") or ""))
    year = year_match.group(1) if year_match else ""
    if len(surnames) == 1:
        names = surnames[0]
    elif len(surnames) <= 3:
        names = "–".join(surnames)
    elif surnames:
        names = f"{surnames[0]} et al."
    else:
        names = safe_id
    return f"{names} {year}".strip()


def paper_link(vault: Path, safe_id: str) -> str:
    page = vault / "wiki" / "papers" / f"{safe_id}.md"
    return f"[[{safe_id}|{author_year_label(page, safe_id)}]]"


def field_bounds(lines: list[str], field: str) -> tuple[int, int] | None:
    heading = next((i for i, line in enumerate(lines) if line.strip() == "## Citation graph"), None)
    if heading is None:
        return None
    section_end = next((i for i in range(heading + 1, len(lines))
                        if lines[i].startswith("## ")), len(lines))
    start = next((i for i in range(heading + 1, section_end)
                  if lines[i].startswith(f"{field}:")), None)
    if start is None:
        return None
    end = start + 1
    while end < section_end and lines[end].strip() and not lines[end].startswith("Cited by:"):
        end += 1
    return start, end


def ensure_edge(text: str, field: str, safe_id: str, link: str) -> tuple[str, bool]:
    lines = text.splitlines()
    bounds = field_bounds(lines, field)
    if bounds is None:
        heading = next((i for i, line in enumerate(lines) if line.strip() == "## Citation graph"), None)
        if heading is None:
            lines.extend(["", "## Citation graph", "", f"{field}: {link}"])
        else:
            lines.insert(heading + 1, f"{field}: {link}")
        return "\n".join(lines) + "\n", True
    start, end = bounds
    block = "\n".join(lines[start:end])
    if re.search(rf"\[\[{re.escape(safe_id)}(?:\||\]\])", block):
        return text, False
    value = lines[start].split(":", 1)[1].strip()
    if not value or value.startswith("<!--") or value in {"-", "—"}:
        lines[start] = f"{field}: {link}"
    else:
        insert_at = end - 1
        lines[insert_at] = lines[insert_at].rstrip().rstrip(",") + ", " + link
    return "\n".join(lines) + "\n", True


def bump_updated(text: str) -> str:
    today = date.today().isoformat()
    return re.sub(r"(?m)^updated:\s*(?:['\"])?\d{4}-\d{2}-\d{2}(?:['\"])?\s*$",
                  f'updated: "{today}"', text, count=1)


def add_relation(vault: Path, source: str, target: str, changed: set[Path]) -> None:
    """Record source -> target on both paper pages, without deleting existing material."""
    for paper, field, other in ((source, "Cites", target), (target, "Cited by", source)):
        path = vault / "wiki" / "papers" / f"{paper}.md"
        text = path.read_text(encoding="utf-8")
        new_text, did_change = ensure_edge(text, field, other, paper_link(vault, other))
        if did_change:
            path.write_text(bump_updated(new_text), encoding="utf-8", newline="\n")
            changed.add(path)


def update(target: str, papers: dict, vault=VAULT) -> list[Path]:
    if target not in papers:
        raise ValueError(f"{target}: no wiki paper page (or no sources entry)")
    changed = set()
    for cited in sorted(item for item in papers[target] if item in papers):
        add_relation(vault, target, cited, changed)
    for citer, refs in sorted(papers.items()):
        if target in refs:
            add_relation(vault, citer, target, changed)
    return sorted(changed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*")
    parser.add_argument("--update", action="store_true",
                        help="additively update both ends; requires exactly one target")
    args = parser.parse_args()
    papers = load_papers()
    targets = [norm(target) for target in args.targets] or sorted(papers)
    if args.update:
        if len(targets) != 1:
            parser.error("--update requires exactly one target")
        try:
            changed = update(targets[0], papers)
        except ValueError as error:
            parser.error(str(error))
        print(f"updated {len(changed)} paper page(s)")
        for path in changed:
            print(f"  {path.relative_to(VAULT).as_posix()}")
        return
    for t in targets:
        report(t, papers)


if __name__ == "__main__":
    main()
