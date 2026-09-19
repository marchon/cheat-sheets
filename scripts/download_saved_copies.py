"""Download every cheat-sheets.org saved-copy file into its topic folder."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

UA = (
    "cheat-sheets-archive/1.0 "
    "(local research mirror of https://www.cheat-sheets.org/; +https://www.cheat-sheets.org/)"
)


def download(url: str, dest: Path, retries: int = 4) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return "exists"
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
                ctype = resp.headers.get("Content-Type", "")
                # The site serves the homepage HTML for missing files.
                if "text/html" in ctype and not dest.suffix.lower() in {".html", ".htm"}:
                    if data[:32].lstrip().lower().startswith(b"<!doctype") or b"<title>Cheat Sheet" in data[:2000]:
                        return "missing"
            tmp.write_bytes(data)
            tmp.replace(dest)
            return "ok"
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            last_err = err
            time.sleep(min(8, attempt * 2))
    raise RuntimeError(f"{url}: {last_err}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog" / "catalog.json").read_text(encoding="utf-8"))
    only_group = sys.argv[1] if len(sys.argv) > 1 else None
    items = catalog["saved_copies"]
    if only_group:
        items = [s for s in items if s["group"] == only_group]
    ok = exists = missing = fail = 0
    for i, sc in enumerate(items, 1):
        dest = root / sc["path"] / "saved-copy" / sc["filename"]
        try:
            status = download(sc["url"], dest)
        except Exception as err:  # noqa: BLE001 — log and continue the archive
            print(f"FAIL {sc['url']} {err}", file=sys.stderr)
            fail += 1
            continue
        if status == "ok":
            ok += 1
        elif status == "exists":
            exists += 1
        else:
            missing += 1
            print(f"MISSING {sc['filename']}")
        if i % 25 == 0 or i == len(items):
            print(f"{i}/{len(items)} ok={ok} exists={exists} missing={missing} fail={fail}")
    print(f"done ok={ok} exists={exists} missing={missing} fail={fail}")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
