"""Clone Wikipedia entries listed on cheat-sheets.org into each topic folder."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = (
    "cheat-sheets-archive/1.0 "
    "(local research mirror of https://www.cheat-sheets.org/; contact: local archive)"
)
API = "https://en.wikipedia.org/w/api.php"


def wiki_title(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    title = path.split("/wiki/", 1)[-1]
    return urllib.parse.unquote(title)


def fetch_extract(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "format": "json",
            "prop": "extracts|info",
            "explaintext": 1,
            "redirects": 1,
            "inprop": "url",
            "titles": title,
        }
    )
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))
    return page


def write_markdown(topic_dir: Path, source_url: str, page: dict, stem: str = "wikipedia") -> None:
    title = page.get("title") or wiki_title(source_url)
    extract = page.get("extract") or ""
    live = page.get("fullurl") or source_url
    pageid = page.get("pageid")
    missing = "missing" in page
    lines = [
        f"# {title}",
        "",
        f"Cloned from {live}.",
        "",
        "Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).",
        "",
    ]
    if missing:
        lines.append("This Wikipedia title was missing or could not be resolved.")
    else:
        if pageid is not None:
            lines.append(f"Page id: {pageid}.")
            lines.append("")
        lines.append(extract.rstrip())
        lines.append("")
    (topic_dir / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")
    (topic_dir / f"{stem}.json").write_text(
        json.dumps(
            {
                "source_url": source_url,
                "resolved_url": live,
                "title": title,
                "pageid": pageid,
                "missing": missing,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog" / "catalog.json").read_text(encoding="utf-8"))
    only_group = sys.argv[1] if len(sys.argv) > 1 else None
    jobs = []
    for t in catalog["topics"]:
        if only_group and t["group"] != only_group:
            continue
        urls = t.get("wikipedia_urls") or ([t["wikipedia"]] if t.get("wikipedia") else [])
        for n, url in enumerate(urls):
            jobs.append((t, url, n))
    ok = skip = fail = 0
    for i, (t, url, n) in enumerate(jobs, 1):
        stem = "wikipedia" if n == 0 else f"wikipedia-{n+1}"
        dest = root / t["path"] / f"{stem}.md"
        if dest.exists() and dest.stat().st_size > 50:
            skip += 1
        else:
            try:
                page = fetch_extract(wiki_title(url))
                write_markdown(root / t["path"], url, page, stem=stem)
                ok += 1
            except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, StopIteration) as err:
                print(f"FAIL {t['id']} {url} {err}", file=sys.stderr)
                fail += 1
            time.sleep(0.15)
        if i % 20 == 0 or i == len(topics):
            print(f"{i}/{len(topics)} ok={ok} skip={skip} fail={fail}")
    print(f"done ok={ok} skip={skip} fail={fail}")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
