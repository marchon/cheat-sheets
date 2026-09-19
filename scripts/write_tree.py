"""Write grouped topic folders and README indexes from catalog.json."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from classify import GROUPS

CONTRIBUTING = (
    "Questions: open an issue in this repository. Pull requests that fix "
    "catalog grouping or add missing saved copies are welcome."
)
LICENSE_LINE = (
    "UNLICENSED © George Lambert. Indexed cheat sheets, saved copies, and "
    "Wikipedia extracts remain under their original publishers' terms; "
    "Wikipedia text is CC BY-SA 4.0."
)
BADGE = (
    "[![standard-readme compliant]"
    "(https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)]"
    "(https://github.com/RichardLitt/standard-readme)"
)


def md_link(text: str, url: str) -> str:
    text = text.replace("[", "\\[").replace("]", "\\]")
    return f"[{text}]({url})"


def topic_readme(t: dict, group_meta: dict) -> str:
    lines = [
        f"# {t['title']}",
        "",
        BADGE,
        "",
        f"Cheat-sheets.org topic in the {group_meta['title']} group.",
        "",
        f"Source: {md_link(t['source_anchor'], t['source_anchor'])}.",
        "",
        "## Table of Contents",
        "",
        "- [Install](#install)",
        "- [Usage](#usage)",
        "- [Official websites](#official-websites)",
        "- [Wikipedia](#wikipedia)",
        "- [Saved copies](#saved-copies)",
        "- [Cheat sheets](#cheat-sheets)",
        "- [See also](#see-also)",
        "- [Contributing](#contributing)",
        "- [License](#license)",
        "",
        "## Install",
        "",
        "This folder is part of the local archive. Clone the repository:",
        "",
        "```sh",
        "git clone .",
        "```",
        "",
        "## Usage",
        "",
        "Open this README, the Wikipedia clone, and files under `saved-copy/`.",
        "",
        "```sh",
        f"ls saved-copy wikipedia.md",
        "```",
        "",
        "## Official websites",
        "",
    ]
    if t["official_websites"]:
        for ow in t["official_websites"]:
            lines.append(f"- {md_link(ow['label'] or ow['url'], ow['url'])}")
    else:
        lines.append("None listed on cheat-sheets.org.")
    lines += ["", "## Wikipedia", ""]
    wiki_urls = t.get("wikipedia_urls") or ([t["wikipedia"]] if t.get("wikipedia") else [])
    if wiki_urls:
        for i, url in enumerate(wiki_urls):
            local = "wikipedia.md" if i == 0 else f"wikipedia-{i+1}.md"
            lines.append(f"- Live: {md_link(url, url)}")
            lines.append(f"- Local clone: [{local}]({local})")
    else:
        lines.append("No Wikipedia link listed on cheat-sheets.org.")
    lines += ["", "## Saved copies", ""]
    if t["saved_copies"]:
        for sc in t["saved_copies"]:
            rel = f"saved-copy/{sc['filename']}"
            lines.append(f"- {md_link(sc['filename'], rel)} — `{sc['url']}`")
    else:
        lines.append("No saved-copy files listed for this topic.")
    lines += ["", "## Cheat sheets", ""]
    if t["items"]:
        for item in t["items"]:
            bits = []
            for kind in ("saved", "online", "archived"):
                for url in item.get(kind) or []:
                    bits.append(md_link(kind, url))
            extra = f" ({', '.join(bits)})" if bits else ""
            lines.append(f"- {item['title']}{extra}")
    else:
        lines.append("No cheat-sheet items listed.")
    lines += ["", "## See also", ""]
    if t["see_also"]:
        for sa in t["see_also"]:
            lines.append(f"- {sa['label']} (`#{sa['id']}`)")
    else:
        lines.append("None listed.")
    if t.get("tools"):
        lines += ["", "## Tools", ""]
        for tool in t["tools"]:
            lines.append(f"- {md_link(tool['label'] or tool['url'], tool['url'])}")
    lines += ["", "## Contributing", "", CONTRIBUTING, "", "## License", "", LICENSE_LINE, ""]
    return "\n".join(lines)


def group_readme(group_id: str, meta: dict, members: list[dict]) -> str:
    toc = [
        "- [Install](#install)",
        "- [Usage](#usage)",
        "- [Topics](#topics)",
        "- [Contributing](#contributing)",
        "- [License](#license)",
    ]
    lines = [
        f"# {meta['title']}",
        "",
        BADGE,
        "",
        meta["description"][:119],
        "",
        f"{len(members)} topics from [cheat-sheets.org](https://www.cheat-sheets.org/).",
        "",
        "## Table of Contents",
        "",
        *toc,
        "",
        "## Install",
        "",
        "```sh",
        "git clone .",
        "```",
        "",
        "## Usage",
        "",
        "```sh",
        "ls -1 */README.md",
        "```",
        "",
        "## Topics",
        "",
    ]
    for t in members:
        wiki = f" — Wikipedia: {t['wikipedia']}" if t.get("wikipedia") else ""
        off = ""
        if t.get("official_websites"):
            labels = ", ".join(ow["url"] for ow in t["official_websites"])
            off = f" — Official: {labels}"
        lines.append(f"- [{t['title']}]({t['slug']}/){wiki}{off}")
    lines += ["", "## Contributing", "", CONTRIBUTING, "", "## License", "", LICENSE_LINE, ""]
    return "\n".join(lines)


def root_readme(catalog: dict) -> str:
    group_lines = []
    toc = [
        "- [Install](#install)",
        "- [Usage](#usage)",
        "- [Background](#background)",
        "- [Groups](#groups)",
        "- [Contributing](#contributing)",
        "- [License](#license)",
    ]
    for g in catalog["groups"]:
        if not g["topic_count"]:
            continue
        group_lines.append(
            f"- [{g['title']}]({g['id']}/) — {g['topic_count']} topics, "
            f"{g['saved_copy_count']} saved copies, {g['wikipedia_count']} Wikipedia entries"
        )
    return "\n".join(
        [
            "# cheat-sheets",
            "",
            BADGE,
            "",
            "Indexed archive of cheat-sheets.org, grouped with saved copies and Wikipedia clones.",
            "",
            "Local mirror of [cheat-sheets.org](https://www.cheat-sheets.org/) topics, "
            "organized using the site's See also clusters and the groups listed in the original request: "
            "languages, databases, applications, business processes, GNU/Linux commands, "
            "file formats, and online data services.",
            "",
            "## Table of Contents",
            "",
            *toc,
            "",
            "## Install",
            "",
            "```sh",
            "git clone .",
            "python3 scripts/parse_index.py",
            "python3 scripts/write_tree.py",
            "```",
            "",
            "## Usage",
            "",
            "Rebuild the catalog from a saved homepage, then download assets:",
            "",
            "```sh",
            "python3 scripts/parse_index.py",
            "python3 scripts/write_tree.py",
            "python3 scripts/download_saved_copies.py",
            "python3 scripts/clone_wikipedia.py",
            "python3 scripts/fetch_tldr.py",
            "```",
            "",
            "Browse groups under the directories listed below. Each topic folder keeps "
            "official websites, See also links, `saved-copy/` files, and a Wikipedia clone.",
            "",
            "## Background",
            "",
            "Original request (from the workspace README):",
            "",
            "- Read every cheat sheet listed on https://www.cheat-sheets.org/",
            "- Index them in groups (languages, databases, applications, business processes, "
            "GNU/Linux commands such as cat, less, more, awk, sed, ls, file formats, "
            "online data services, and similar logical groupings)",
            "- Use See also clusters such as Linux and Unix as grouping patterns",
            "- Keep every `saved-copy/` file in the correct category",
            "- Record Official websites when listed",
            "- Clone listed Wikipedia entries (example: https://en.wikipedia.org/wiki/Google_App_Engine)",
            "",
            f"Catalog snapshot: {catalog['topic_count']} topics, "
            f"{catalog['saved_copy_count']} saved copies, "
            f"{catalog['wikipedia_count']} Wikipedia links, "
            f"{catalog['official_website_count']} official websites.",
            "",
            "## Groups",
            "",
            *group_lines,
            "",
            "Machine-readable catalog: [catalog/catalog.json](catalog/catalog.json).",
            "",
            "## Contributing",
            "",
            CONTRIBUTING,
            "",
            "## License",
            "",
            LICENSE_LINE,
            "",
        ]
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog" / "catalog.json").read_text(encoding="utf-8"))
    by_group: dict[str, list] = defaultdict(list)
    for t in catalog["topics"]:
        by_group[t["group"]].append(t)

    (root / "README.md").write_text(root_readme(catalog), encoding="utf-8")

    for group_id, meta in GROUPS.items():
        members = by_group.get(group_id, [])
        gdir = root / group_id
        gdir.mkdir(parents=True, exist_ok=True)
        (gdir / "README.md").write_text(group_readme(group_id, meta, members), encoding="utf-8")
        for t in members:
            tdir = gdir / t["slug"]
            tdir.mkdir(parents=True, exist_ok=True)
            (tdir / "saved-copy").mkdir(exist_ok=True)
            (tdir / "README.md").write_text(topic_readme(t, meta), encoding="utf-8")
            meta_path = tdir / "topic.json"
            meta_path.write_text(json.dumps(t, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("wrote tree for", catalog["topic_count"], "topics")
    from build_site import main as build_site
    build_site()


if __name__ == "__main__":
    main()
