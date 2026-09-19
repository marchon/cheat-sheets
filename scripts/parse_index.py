"""Parse cheat-sheets.org homepage HTML into a structured catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup

from classify import GROUPS, SKIP_IDS, group_for

BASE = "https://www.cheat-sheets.org/"
SAVED_PREFIX = "saved-copy/"


def slugify(topic_id: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", topic_id)
    s = s.replace("_", "-").replace(" ", "-")
    s = s.lower()
    s = re.sub(r"[^a-z0-9.+-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "topic"


def classify_href(href: str, img_alt: str | None) -> str | None:
    alt = (img_alt or "").lower()
    if alt in {"saved", "online", "archived"}:
        return alt
    if href.startswith(SAVED_PREFIX) or "/saved-copy/" in href:
        return "saved"
    if "web.archive.org" in href:
        return "archived"
    if href.startswith("#"):
        return None
    return "online"


def abs_url(href: str) -> str:
    return urljoin(BASE, href)


def saved_filename(href: str) -> str:
    path = urlparse(urljoin(BASE, href)).path
    name = path.split("/saved-copy/")[-1]
    return unquote(name)


def parse_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    topics = []
    for section in soup.select("section.csB"):
        h2 = section.find("h2")
        if not h2:
            continue
        aid = h2.find("a", id=True)
        if not aid:
            continue
        topic_id = aid.get("id")
        if topic_id in SKIP_IDS:
            continue
        extra_ids = [a.get("id") for a in h2.find_all("a", id=True) if a.get("id") and a.get("id") != topic_id]
        wiki_links = []
        for wiki_a in h2.find_all("a", class_="w"):
            href = (wiki_a.get("href") or "").strip()
            if href and href not in wiki_links:
                wiki_links.append(href)
        title_h2 = BeautifulSoup(str(h2), "html.parser").find("h2")
        for drop in title_h2.select("a.w, a.tp"):
            drop.decompose()
        title = re.sub(r"\s+", " ", title_h2.get_text(" ", strip=True)).strip(" ,")

        items = []
        saved_copies = []
        for li in section.select("li.iLi"):
            item_span = li.find("span", class_="item")
            item_title = item_span.get_text(" ", strip=True) if item_span else li.get_text(" ", strip=True)
            links = {"saved": [], "online": [], "archived": []}
            for a in li.find_all("a", href=True):
                href = a["href"].strip()
                img = a.find("img")
                alt = img.get("alt") if img else None
                kind = classify_href(href, alt)
                if not kind:
                    continue
                url = abs_url(href)
                links[kind].append(url)
                if kind == "saved":
                    saved_copies.append(
                        {
                            "url": url,
                            "filename": saved_filename(href),
                        }
                    )
            items.append({"title": item_title, **links})

        official = []
        see_also = []
        tools = []
        for div in section.select("div.bI, div.p"):
            text = div.get_text(" ", strip=True)
            low = text.lower()
            is_official = bool(div.find("span", class_="oWT")) or low.startswith("official website")
            is_see = bool(div.find("span", class_="sAT")) or low.startswith("see also") or low.startswith("see:")
            is_tools = low.startswith("tools:")
            if is_official:
                for a in div.find_all("a", href=True):
                    href = a["href"].strip()
                    if href.startswith("#"):
                        continue
                    entry = {"label": a.get_text(strip=True) or href, "url": abs_url(href)}
                    if entry not in official:
                        official.append(entry)
            if is_see:
                for a in div.find_all("a", href=True):
                    href = a["href"].strip()
                    if href.startswith("#"):
                        entry = {"id": href[1:], "label": a.get_text(strip=True)}
                        if entry not in see_also:
                            see_also.append(entry)
            if is_tools:
                for a in div.find_all("a", href=True):
                    entry = {"label": a.get_text(strip=True), "url": abs_url(a["href"].strip())}
                    if entry not in tools:
                        tools.append(entry)

        for node in section.find_all(string=re.compile(r"^\s*Tools:", re.I)):
            parent = node.parent
            if parent:
                for a in parent.find_all("a", href=True):
                    entry = {"label": a.get_text(strip=True), "url": abs_url(a["href"].strip())}
                    if entry not in tools:
                        tools.append(entry)

        group = group_for(topic_id)
        slug = slugify(topic_id)
        topics.append(
            {
                "id": topic_id,
                "slug": slug,
                "title": title,
                "group": group,
                "source_anchor": abs_url(f"#{topic_id}"),
                "extra_ids": extra_ids,
                "wikipedia": wiki_links[0] if wiki_links else None,
                "wikipedia_urls": wiki_links,
                "official_websites": official,
                "see_also": see_also,
                "tools": tools,
                "items": items,
                "saved_copies": saved_copies,
                "path": f"{group}/{slug}",
            }
        )
    return topics


def build_catalog(html: str) -> dict:
    topics = parse_html(html)
    groups = []
    by_group = {}
    for key, meta in GROUPS.items():
        members = [t for t in topics if t["group"] == key]
        by_group[key] = members
        groups.append(
            {
                "id": key,
                "title": meta["title"],
                "description": meta["description"],
                "topic_count": len(members),
                "saved_copy_count": sum(len(t["saved_copies"]) for t in members),
                "wikipedia_count": sum(1 for t in members if t["wikipedia"]),
                "topics": [{"id": t["id"], "slug": t["slug"], "title": t["title"]} for t in members],
            }
        )
    saved = []
    seen = set()
    for t in topics:
        for sc in t["saved_copies"]:
            key = sc["url"]
            if key in seen:
                continue
            seen.add(key)
            saved.append({**sc, "topic_id": t["id"], "group": t["group"], "path": t["path"]})
    return {
        "source": BASE,
        "topic_count": len(topics),
        "group_count": len([g for g in groups if g["topic_count"]]),
        "saved_copy_count": len(saved),
        "wikipedia_count": sum(len(t.get("wikipedia_urls") or ([t["wikipedia"]] if t.get("wikipedia") else [])) for t in topics),
        "official_website_count": sum(len(t["official_websites"]) for t in topics),
        "groups": groups,
        "topics": topics,
        "saved_copies": saved,
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    src = root / "catalog" / "source" / "index.html"
    html = src.read_text(encoding="utf-8", errors="replace")
    catalog = build_catalog(html)
    out = root / "catalog" / "catalog.json"
    out.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"topics={catalog['topic_count']} groups={catalog['group_count']} "
        f"saved={catalog['saved_copy_count']} wiki={catalog['wikipedia_count']} "
        f"official={catalog['official_website_count']}"
    )
    leftover = [t["id"] for t in catalog["topics"] if t["group"] == "other"]
    if leftover:
        print("other:", ", ".join(leftover))


if __name__ == "__main__":
    main()
