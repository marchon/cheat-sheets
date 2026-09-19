"""Archive cheat-sheets.org TLDR command pages used as GNU/Linux command sheets."""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from bs4 import BeautifulSoup

UA = "cheat-sheets-archive/1.0 (local research mirror of https://www.cheat-sheets.org/)"
LIST_URL = "https://www.cheat-sheets.org/project/tldr/command/special-most-used-linux-commands/"
ALL_URL = "https://www.cheat-sheets.org/project/tldr/command/special-all-language-commands/"
POPULAR_URL = "https://www.cheat-sheets.org/project/tldr/command/special-top-commands/"
# Commands called out in the original README, plus common siblings.
SEED_COMMANDS = [
    "cat",
    "less",
    "more",
    "awk",
    "sed",
    "ls",
    "grep",
    "find",
    "chmod",
    "chown",
    "curl",
    "wget",
    "tar",
    "ps",
    "top",
    "head",
    "tail",
    "sort",
    "uniq",
    "cut",
    "tr",
    "xargs",
    "man",
    "bash",
    "ssh",
]


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def command_names_from_html(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    names = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        m = re.search(r"/project/tldr/command/([^/]+)/?", href)
        if not m:
            continue
        name = urllib.parse.unquote(m.group(1))
        if name.startswith("special-"):
            continue
        names.append(name)
    # also data attributes / json blobs
    for m in re.finditer(r"/project/tldr/command/([a-zA-Z0-9_+:.-]+)/", html):
        name = m.group(1)
        if not name.startswith("special-"):
            names.append(name)
    # de-dupe, preserve order
    seen = set()
    out = []
    for n in names:
        key = n.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(n)
    return out


def article_markdown(cmd: str, html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup.find("main") or soup.body
    text = article.get_text("\n", strip=True) if article else soup.get_text("\n", strip=True)
    live = f"https://www.cheat-sheets.org/project/tldr/command/{urllib.parse.quote(cmd)}/"
    return "\n".join(
        [
            f"# {cmd}",
            "",
            f"TLDR page cloned from {live}.",
            "",
            "Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).",
            "",
            text,
            "",
        ]
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    dest_root = root / "gnu-linux-commands" / "tldr"
    dest_root.mkdir(parents=True, exist_ok=True)
    names = list(SEED_COMMANDS)
    for url in (LIST_URL, POPULAR_URL, ALL_URL):
        try:
            html = get(url)
            names.extend(command_names_from_html(html))
            (dest_root / (urllib.parse.urlparse(url).path.strip("/").replace("/", "_") + ".html")).write_text(
                html, encoding="utf-8"
            )
        except Exception as err:  # noqa: BLE001
            print(f"list fail {url}: {err}")
        time.sleep(0.2)
    # de-dupe
    seen = set()
    uniq = []
    for n in names:
        k = n.lower()
        if k in seen:
            continue
        seen.add(k)
        uniq.append(n)
    print(f"commands to fetch: {len(uniq)}", flush=True)
    ok = skip = fail = 0

    def fetch_one(cmd: str) -> str:
        folder = dest_root / cmd.replace("/", "-")
        folder.mkdir(exist_ok=True)
        md = folder / "README.md"
        if md.exists() and md.stat().st_size > 80:
            return "skip"
        url = f"https://www.cheat-sheets.org/project/tldr/command/{urllib.parse.quote(cmd)}/"
        html = get(url)
        (folder / "source.html").write_text(html, encoding="utf-8")
        md.write_text(article_markdown(cmd, html), encoding="utf-8")
        return "ok"

    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(fetch_one, cmd): cmd for cmd in uniq}
        for i, fut in enumerate(as_completed(futures), 1):
            cmd = futures[fut]
            try:
                status = fut.result()
            except Exception as err:  # noqa: BLE001
                print(f"FAIL {cmd} {err}", flush=True)
                fail += 1
            else:
                if status == "skip":
                    skip += 1
                else:
                    ok += 1
            if i % 100 == 0 or i == len(uniq):
                print(f"{i}/{len(uniq)} ok={ok} skip={skip} fail={fail}", flush=True)
    index = {
        "source": "https://www.cheat-sheets.org/project/tldr/",
        "most_used": LIST_URL,
        "all_commands": ALL_URL,
        "popular": POPULAR_URL,
        "command_count": len(uniq),
        "commands": uniq,
    }
    (dest_root / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    (dest_root / "README.md").write_text(
        "\n".join(
            [
                "# TLDR command pages",
                "",
                "[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)",
                "",
                "GNU/Linux command cheat sheets from the cheat-sheets.org TLDR wrapper.",
                "",
                "Includes cat, less, more, awk, sed, ls, and the site's most-used Linux list.",
                "",
                "## Install",
                "",
                "```sh",
                "python3 scripts/fetch_tldr.py",
                "```",
                "",
                "## Usage",
                "",
                "```sh",
                "ls gnu-linux-commands/tldr/cat",
                "```",
                "",
                "## Commands",
                "",
                *[f"- [{c}]({c}/)" for c in uniq[:400]],
                "",
                f"{len(uniq)} commands archived. Full list: [index.json](index.json).",
                "",
                "## Contributing",
                "",
                "Questions: open an issue. PRs welcome.",
                "",
                "## License",
                "",
                "UNLICENSED © George Lambert. TLDR page text is CC BY 4.0 from tldr-pages.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"done ok={ok} skip={skip} fail={fail} total={len(uniq)}")


if __name__ == "__main__":
    main()
