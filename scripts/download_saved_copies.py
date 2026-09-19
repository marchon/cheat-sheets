"""Download every cheat-sheets.org saved-copy file into its topic folder."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

UA = (
    "cheat-sheets-archive/1.0 "
    "(local research mirror of https://www.cheat-sheets.org/; +https://www.cheat-sheets.org/)"
)


def dest_for(root: Path, sc: dict) -> Path:
    parsed = urllib.parse.urlparse(sc["url"])
    path = urllib.parse.unquote(parsed.path)
    topic = root / sc["path"]
    if "/saved-copy/" in path:
        rel = path.split("/saved-copy/", 1)[1].lstrip("/")
        dest = topic / "saved-copy" / rel
    elif parsed.netloc.endswith("cheat-sheets.org"):
        dest = topic / "hosted" / path.lstrip("/")
    else:
        dest = topic / "saved-copy" / Path(path).name
    if dest.suffix == "" or path.endswith("/"):
        dest = dest / "index.html"
    dest = dest.resolve()
    if root.resolve() not in dest.parents:
        raise RuntimeError(f"refusing to write outside repo: {dest}")
    return dest


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
                if "text/html" in ctype and dest.suffix.lower() not in {".html", ".htm"}:
                    head = data[:2000]
                    if b"<title>Cheat Sheet : All Cheat Sheets" in head:
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
    workers = 6

    def job(sc: dict) -> tuple[str, dict, str | None]:
        dest = dest_for(root, sc)
        try:
            return download(sc["url"], dest), sc, None
        except Exception as err:  # noqa: BLE001 — log and continue the archive
            return "fail", sc, str(err)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(job, sc) for sc in items]
        for i, fut in enumerate(as_completed(futures), 1):
            status, sc, err = fut.result()
            if status == "ok":
                ok += 1
            elif status == "exists":
                exists += 1
            elif status == "missing":
                missing += 1
                print(f"MISSING {sc['filename']}")
            else:
                fail += 1
                print(f"FAIL {sc['url']} {err}", file=sys.stderr)
            if i % 25 == 0 or i == len(items):
                print(f"{i}/{len(items)} ok={ok} exists={exists} missing={missing} fail={fail}", flush=True)
    print(f"done ok={ok} exists={exists} missing={missing} fail={fail}", flush=True)
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
