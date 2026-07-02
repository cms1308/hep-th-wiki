#!/usr/bin/env python3
"""citation-links.py [safe-id]

Computes the citation graph among INGESTED papers (those with a wiki/papers/<safe-id>.md
page) using the refs.json files produced by inspire-fetch.sh.

With a safe-id argument: prints what that paper cites / is cited by, among wiki papers.
Without arguments: prints the full adjacency for every wiki paper (for lint/audit).
"""
import json
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent


def norm(arxiv_id: str) -> str:
    return arxiv_id.replace("/", "-")


def load_papers():
    """safe-id -> set of normalized arXiv ids it references (wiki papers only later)."""
    papers = {}
    for d in sorted((VAULT / "sources" / "arxiv").iterdir()):
        if not (VAULT / "wiki" / "papers" / f"{d.name}.md").exists():
            continue  # in sources but not integrated into the wiki
        refs_file = d / "refs.json"
        refs = set()
        if refs_file.exists():
            data = json.loads(refs_file.read_text())
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


def main():
    papers = load_papers()
    targets = sys.argv[1:] or sorted(papers)
    for t in targets:
        report(norm(t), papers)


if __name__ == "__main__":
    main()
