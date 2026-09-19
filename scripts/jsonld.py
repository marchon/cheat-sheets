"""JSON-LD graph for every catalog group, topic, saved copy, and Wikipedia clone."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote, urlparse

from classify import GROUPS

BASE = "https://cheat-sheet-index.georgelambert.org"
SOURCE = "https://cheat-sheets.org/"
SOURCE_WWW = "https://www.cheat-sheets.org/"
WAYBACK = "https://web.archive.org/web/20260000000000*/https://cheat-sheets.org/"
WIKI_LICENSE = "https://creativecommons.org/licenses/by-sa/4.0/"
GITHUB_PROFILE = "https://github.com/marchon"
GITHUB_REPO = "https://github.com/marchon/cheat-sheets"
CREDIT_TEXT = (
    "Source: cheat-sheets.org. Internet Archive snapshots: "
    "https://web.archive.org/web/20260000000000*/https://cheat-sheets.org/. "
    "Indexing, searchability, SEO, JSON-LD, and llms.txt: George Lambert "
    "<marchon@gmail.com>, https://georgelambert.org/, https://github.com/marchon, "
    "https://github.com/marchon/cheat-sheets. "
    "George Lambert takes credit only for indexing and searchability, not for the underlying cheat sheets."
)
GEORGE_ID = "https://georgelambert.org/#person"
INDEXING_ID = f"{BASE}/#indexing"
INDEXER_ROLE = "Indexing, searchability, SEO, JSON-LD, and llms.txt only"

MIME = {
    ".pdf": "application/pdf",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
    ".html": "text/html",
    ".htm": "text/html",
    ".txt": "text/plain",
    ".md": "text/markdown",
    ".tex": "application/x-tex",
    ".zip": "application/zip",
    ".gz": "application/gzip",
    ".tgz": "application/gzip",
    ".doc": "application/msword",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".odt": "application/vnd.oasis.opendocument.text",
    ".xls": "application/vnd.ms-excel",
    ".epub": "application/epub+zip",
    ".rtf": "application/rtf",
    ".ps": "application/postscript",
    ".dvi": "application/x-dvi",
}


def clean_title(title: str) -> str:
    return re.sub(r"\s+W$", "", title or "").strip()


def mime_for(name: str) -> str:
    return MIME.get(Path(name).suffix.lower(), "application/octet-stream")


def topic_url(topic: dict) -> str:
    return f"{BASE}/{topic['path']}/"


def topic_id(topic: dict) -> str:
    return f"{topic_url(topic)}#topic"


def group_url(group_id: str) -> str:
    return f"{BASE}/{group_id}/"


def group_id(group_id: str) -> str:
    return f"{group_url(group_id)}#collection"


def local_saved_url(topic: dict, sc: dict) -> str:
    raw = sc.get("url") or ""
    parsed = urlparse(raw)
    path = parsed.path
    if "/saved-copy/" in path:
        rel = path.split("/saved-copy/", 1)[1].lstrip("/")
        if not rel or rel.endswith("/") or not Path(rel).suffix:
            rel = rel.rstrip("/") + "/index.html"
        return f"{BASE}/{topic['path']}/saved-copy/{quote(rel)}"
    if parsed.netloc.endswith("cheat-sheets.org"):
        rel = path.lstrip("/")
        if not rel or rel.endswith("/") or not Path(rel).suffix:
            rel = rel.rstrip("/") + "/index.html"
        return f"{BASE}/{topic['path']}/hosted/{quote(rel)}"
    name = Path(path).name or "file"
    return f"{BASE}/{topic['path']}/saved-copy/{quote(name)}"


def saved_node_id(topic: dict, index: int) -> str:
    return f"{topic_url(topic)}#saved-{index + 1}"


def sheet_node_id(topic: dict, index: int) -> str:
    return f"{topic_url(topic)}#sheet-{index + 1}"


def wiki_node_id(topic: dict, index: int = 0) -> str:
    return f"{topic_url(topic)}#wikipedia-{index + 1}"


def source_org() -> dict:
    return {
        "@type": "Organization",
        "@id": f"{SOURCE}#org",
        "name": "Cheat-Sheets.org",
        "url": SOURCE,
        "sameAs": [SOURCE_WWW, WAYBACK],
    }


def wayback_node() -> dict:
    return {
        "@type": "WebSite",
        "@id": f"{WAYBACK}#archive",
        "name": "Internet Archive snapshots of Cheat-Sheets.org",
        "url": WAYBACK,
        "isBasedOn": SOURCE,
    }


def person_node() -> dict:
    return {
        "@type": "Person",
        "@id": GEORGE_ID,
        "name": "George Lambert",
        "email": "mailto:marchon@gmail.com",
        "url": "https://georgelambert.org/",
        "sameAs": [GITHUB_PROFILE, GITHUB_REPO],
        "identifier": [
            {"@type": "PropertyValue", "propertyID": "GitHub", "value": GITHUB_PROFILE},
            {"@type": "PropertyValue", "propertyID": "GitHub repository", "value": GITHUB_REPO},
        ],
        "description": (
            "Created the grouping index, search UI, SEO markup, JSON-LD graph, and llms.txt "
            "for this archive. Not the author of the underlying cheat sheets."
        ),
    }


def indexing_work_node() -> dict:
    return {
        "@type": "CreativeWork",
        "@id": INDEXING_ID,
        "name": "Cheat-sheet index, searchability, SEO, JSON-LD, and llms.txt",
        "url": f"{BASE}/",
        "description": (
            "George Lambert created only the catalog grouping, searchability, SEO, "
            "JSON-LD, and llms.txt. Source cheat sheets remain the work of cheat-sheets.org "
            "and their original authors; snapshots also exist at the Internet Archive."
        ),
        "creator": {"@id": GEORGE_ID},
        "accountablePerson": {"@id": GEORGE_ID},
        "sdPublisher": {"@id": GEORGE_ID},
        "isBasedOn": SOURCE,
        "sameAs": [SOURCE, SOURCE_WWW, WAYBACK, GITHUB_REPO],
        "license": "UNLICENSED",
        "encoding": [
            {"@type": "MediaObject", "url": f"{BASE}/graph.jsonld", "encodingFormat": "application/ld+json"},
            {"@type": "MediaObject", "url": f"{BASE}/llms.txt", "encodingFormat": "text/plain"},
        ],
    }


def indexer_role() -> dict:
    return {
        "@type": "Role",
        "roleName": INDEXER_ROLE,
        "contributor": {"@id": GEORGE_ID},
    }


def credit_fields() -> dict:
    return {
        "creditText": CREDIT_TEXT,
        "isBasedOn": SOURCE,
        "citation": [
            {"@id": f"{SOURCE}#org"},
            {"@id": f"{WAYBACK}#archive"},
            {"@id": INDEXING_ID},
        ],
        "acquireLicensePage": SOURCE,
        "contributor": indexer_role(),
        "sdPublisher": {"@id": GEORGE_ID},
        "accountablePerson": {"@id": GEORGE_ID},
    }


def website_node() -> dict:
    return {
        "@type": "WebSite",
        "@id": f"{BASE}/#website",
        "url": f"{BASE}/",
        "name": "cheat-sheets index",
        "description": (
            "Searchable index of cheat-sheets.org topics, grouped with official "
            "websites, saved copies, and Wikipedia clones."
        ),
        "inLanguage": "en",
        "publisher": {"@id": GEORGE_ID},
        "sameAs": [SOURCE, SOURCE_WWW, WAYBACK, GITHUB_REPO],
        **credit_fields(),
        "potentialAction": {
            "@type": "SearchAction",
            "target": f"{BASE}/?q={{search_term_string}}",
            "query-input": "required name=search_term_string",
        },
    }


def catalog_node(catalog: dict, groups: list[dict]) -> dict:
    return {
        "@type": "DataCatalog",
        "@id": f"{BASE}/#catalog",
        "url": f"{BASE}/",
        "name": "cheat-sheets index",
        "description": (
            f"{catalog['topic_count']} cheat-sheet topics in {catalog['group_count']} groups, "
            "archived from cheat-sheets.org with official websites, saved copies, and Wikipedia clones."
        ),
        "inLanguage": "en",
        "isPartOf": {"@id": f"{BASE}/#website"},
        "license": "https://www.cheat-sheets.org/",
        "creator": {
            "@type": "Role",
            "roleName": INDEXER_ROLE,
            "creator": {"@id": GEORGE_ID},
        },
        "hasPart": [{"@id": group_id(g["id"])} for g in groups if g.get("topic_count")],
        "numberOfItems": catalog["topic_count"],
        "keywords": [g["title"] for g in groups if g.get("topic_count")],
        "sameAs": [SOURCE, SOURCE_WWW, WAYBACK, GITHUB_REPO],
        **credit_fields(),
    }


def group_node(group: dict, members: list[dict]) -> dict:
    return {
        "@type": ["Collection", "CollectionPage"],
        "@id": group_id(group["id"]),
        "url": group_url(group["id"]),
        "name": group["title"],
        "description": group.get("description") or GROUPS.get(group["id"], {}).get("description", ""),
        "isPartOf": {"@id": f"{BASE}/#catalog"},
        "hasPart": [{"@id": topic_id(t)} for t in members],
        "numberOfItems": len(members),
        "inLanguage": "en",
        **credit_fields(),
    }


def saved_node(topic: dict, sc: dict, index: int) -> dict:
    name = sc.get("filename") or f"saved-copy-{index + 1}"
    return {
        "@type": "DigitalDocument",
        "@id": saved_node_id(topic, index),
        "name": name,
        "url": local_saved_url(topic, sc),
        "encodingFormat": mime_for(name),
        "isPartOf": {"@id": topic_id(topic)},
        "sameAs": [sc["url"]] if sc.get("url") else [],
        "learningResourceType": "cheat sheet",
        **credit_fields(),
    }


def wiki_node(topic: dict, url: str, index: int) -> dict:
    local = f"{topic_url(topic)}wikipedia.md" if index == 0 else f"{topic_url(topic)}wikipedia-{index + 1}.md"
    return {
        "@type": "Article",
        "@id": wiki_node_id(topic, index),
        "name": f"{clean_title(topic['title'])} (Wikipedia clone)",
        "url": local,
        "sameAs": [url],
        "isBasedOn": url,
        "license": WIKI_LICENSE,
        "inLanguage": "en",
        "isPartOf": {"@id": topic_id(topic)},
        **credit_fields(),
    }


def sheet_node(topic: dict, item: dict, index: int) -> dict:
    hrefs = (item.get("saved") or []) + (item.get("online") or [])
    node = {
        "@type": "LearningResource",
        "@id": sheet_node_id(topic, index),
        "name": item.get("title") or f"Cheat sheet {index + 1}",
        "learningResourceType": "cheat sheet",
        "educationalUse": "reference",
        "isPartOf": {"@id": topic_id(topic)},
        "inLanguage": "en",
        **credit_fields(),
    }
    if hrefs:
        node["url"] = hrefs[0]
        if len(hrefs) > 1:
            node["sameAs"] = hrefs[1:]
    return node


def topic_node(topic: dict) -> dict:
    title = clean_title(topic["title"])
    same_as = []
    if topic.get("source_anchor"):
        same_as.append(topic["source_anchor"])
    for url in topic.get("wikipedia_urls") or ([topic["wikipedia"]] if topic.get("wikipedia") else []):
        same_as.append(url)
    for ow in topic.get("official_websites") or []:
        if ow.get("url"):
            same_as.append(ow["url"])
    parts = []
    parts.extend(saved_node_id(topic, i) for i in range(len(topic.get("saved_copies") or [])))
    wiki_urls = topic.get("wikipedia_urls") or ([topic["wikipedia"]] if topic.get("wikipedia") else [])
    parts.extend(wiki_node_id(topic, i) for i in range(len(wiki_urls)))
    parts.extend(sheet_node_id(topic, i) for i in range(len(topic.get("items") or [])))
    related = []
    for sa in topic.get("see_also") or []:
        related.append({"@type": "Thing", "name": sa.get("label") or sa.get("id"), "identifier": sa.get("id")})
    node = {
        "@type": ["LearningResource", "WebPage"],
        "@id": topic_id(topic),
        "url": topic_url(topic),
        "name": title,
        "headline": title,
        "description": (
            f"{title} cheat sheets archived from cheat-sheets.org in the "
            f"{GROUPS.get(topic['group'], {}).get('title', topic['group'])} group."
        ),
        "inLanguage": "en",
        "isPartOf": {"@id": group_id(topic["group"])},
        "learningResourceType": "cheat sheet",
        "educationalUse": "reference",
        "sameAs": same_as + [SOURCE, SOURCE_WWW, WAYBACK, GITHUB_PROFILE, GITHUB_REPO],
        **credit_fields(),
        "hasPart": [{"@id": p} for p in parts],
        "significantLink": [ow["url"] for ow in topic.get("official_websites") or [] if ow.get("url")],
    }
    if related:
        node["mentions"] = related
    if wiki_urls:
        node["about"] = [{"@id": wiki_node_id(topic, i)} for i in range(len(wiki_urls))]
    return node


def topic_graph(topic: dict) -> list[dict]:
    nodes = [topic_node(topic)]
    for i, sc in enumerate(topic.get("saved_copies") or []):
        nodes.append(saved_node(topic, sc, i))
    wiki_urls = topic.get("wikipedia_urls") or ([topic["wikipedia"]] if topic.get("wikipedia") else [])
    for i, url in enumerate(wiki_urls):
        nodes.append(wiki_node(topic, url, i))
    for i, item in enumerate(topic.get("items") or []):
        nodes.append(sheet_node(topic, item, i))
    return nodes


def full_graph(catalog: dict, topics: list[dict], groups: list[dict]) -> dict:
    graph = [
        person_node(),
        indexing_work_node(),
        source_org(),
        wayback_node(),
        website_node(),
        catalog_node(catalog, groups),
    ]
    by_group = {g["id"]: [] for g in groups}
    for t in topics:
        by_group.setdefault(t["group"], []).append(t)
    for g in groups:
        if not g.get("topic_count"):
            continue
        graph.append(group_node(g, by_group.get(g["id"], [])))
    for t in topics:
        graph.extend(topic_graph(t))
    return {"@context": "https://schema.org", "@graph": graph}


def homepage_graph(catalog: dict, topics: list[dict], groups: list[dict]) -> dict:
    """Compact homepage graph plus every topic @id so the catalog is fully linked."""
    live_groups = [g for g in groups if g.get("topic_count")]
    item_list = {
        "@type": "ItemList",
        "@id": f"{BASE}/#topic-list",
        "name": "All cheat-sheet topics",
        "numberOfItems": len(topics),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "url": topic_url(t),
                "name": clean_title(t["title"]),
                "item": {"@id": topic_id(t)},
            }
            for i, t in enumerate(topics)
        ],
    }
    webpage = {
        "@type": "WebPage",
        "@id": f"{BASE}/#webpage",
        "url": f"{BASE}/",
        "name": "cheat-sheets index",
        "description": (
            "Searchable index of cheat-sheets.org topics, grouped with official "
            "websites, saved copies, and Wikipedia clones."
        ),
        "isPartOf": {"@id": f"{BASE}/#website"},
        "about": {"@id": f"{BASE}/#catalog"},
        "mainEntity": {"@id": f"{BASE}/#topic-list"},
        "inLanguage": "en",
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".lede"]},
    }
    webpage = {**webpage, **credit_fields(), "sameAs": [SOURCE, SOURCE_WWW, WAYBACK, GITHUB_PROFILE, GITHUB_REPO]}
    graph = [
        person_node(),
        indexing_work_node(),
        source_org(),
        wayback_node(),
        website_node(),
        catalog_node(catalog, live_groups),
        webpage,
        item_list,
    ]
    by_group = {g["id"]: [] for g in live_groups}
    for t in topics:
        by_group.setdefault(t["group"], []).append(t)
    for g in live_groups:
        graph.append(group_node(g, by_group.get(g["id"], [])))
    for t in topics:
        graph.extend(topic_graph(t))
    return {"@context": "https://schema.org", "@graph": graph}


def page_graph(nodes: list[dict]) -> dict:
    return {"@context": "https://schema.org", "@graph": nodes}
