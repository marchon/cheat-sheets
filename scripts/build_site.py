"""Build a static HTML index of the cheat-sheet catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path

from urllib.parse import quote, unquote, urlparse

from classify import GROUPS
from jsonld import (
    BASE,
    SOURCE,
    WAYBACK,
    catalog_node,
    clean_title,
    full_graph,
    group_id,
    group_node,
    homepage_graph,
    indexing_work_node,
    page_graph,
    person_node,
    source_org,
    topic_graph,
    topic_id,
    wayback_node,
    website_node,
)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>cheat-sheets index</title>
  <!-- search-index-tags -->
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="description" content="Searchable index of cheat-sheets.org topics, grouped with official websites, saved copies, and Wikipedia clones.">
  <link rel="canonical" href="https://cheat-sheet-index.georgelambert.org/">
  <link rel="alternate" type="text/plain" href="https://cheat-sheet-index.georgelambert.org/llms.txt" title="LLM content">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://cheat-sheet-index.georgelambert.org/">
  <meta property="og:title" content="cheat-sheets index">
  <meta property="og:description" content="Searchable index of cheat-sheets.org topics, grouped with official websites, saved copies, and Wikipedia clones.">
  <meta property="og:site_name" content="cheat-sheet-index.georgelambert.org">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="cheat-sheets index">
  <meta name="twitter:description" content="Searchable index of cheat-sheets.org topics, grouped with official websites, saved copies, and Wikipedia clones.">
  <script type="application/ld+json">__JSONLD__</script>
  <!-- /search-index-tags -->
  <style>
    :root {
      color-scheme: light dark;
      --bg: #f6f3ee;
      --ink: #1c1916;
      --muted: #5c564e;
      --paper: #fffdf8;
      --line: #d9d2c6;
      --accent: #8a3b12;
      --focus: #0b57d0;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #161513;
        --ink: #ece7df;
        --muted: #b3aaa0;
        --paper: #221f1c;
        --line: #3a3530;
        --accent: #e0a070;
        --focus: #8ab4f8;
      }
    }
    * { box-sizing: border-box; }
    html { background: var(--bg); color: var(--ink); }
    body {
      margin: 0;
      font: 1rem/1.5 ui-sans-serif, system-ui, sans-serif;
    }
    a { color: var(--accent); }
    a:focus-visible, button:focus-visible, input:focus-visible {
      outline: 2px solid var(--focus);
      outline-offset: 2px;
    }
    header, footer, main { max-width: 72rem; margin-inline: auto; padding-inline: 1.25rem; }
    header { padding-block: 1.5rem 1rem; }
    h1 { font-size: 1.75rem; margin: 0 0 0.35rem; }
    .lede { color: var(--muted); margin: 0 0 1rem; }
    search {
      display: block;
      margin-block: 1rem;
    }
    search form {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      align-items: end;
    }
    label { display: block; font-size: 0.9rem; margin-block-end: 0.25rem; }
    input[type="search"] {
      font-size: 1rem;
      min-height: 48px;
      min-width: min(100%, 22rem);
      padding: 0.6rem 0.75rem;
      border: 1px solid var(--line);
      background: var(--paper);
      color: var(--ink);
      border-radius: 0.35rem;
    }
    button {
      font: inherit;
      min-height: 48px;
      padding: 0.5rem 0.9rem;
      border: 1px solid var(--line);
      background: var(--paper);
      color: var(--ink);
      border-radius: 0.35rem;
      cursor: pointer;
    }
    button.topic {
      display: block;
      width: 100%;
      text-align: start;
      padding: 0.7rem 0.8rem;
    }
    button.topic:hover { border-color: var(--accent); }
    nav ul {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem 0.85rem;
      list-style: none;
      padding: 0;
      margin: 0 0 1.25rem;
    }
    .status { color: var(--muted); margin: 0 0 1rem; }
    section.group {
      content-visibility: auto;
      contain-intrinsic-size: 1px 24rem;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 0.5rem;
      padding: 1rem 1.1rem 1.2rem;
      margin-block-end: 1rem;
    }
    section.group[hidden], article[hidden] { display: none; }
    section.group h2 { margin: 0 0 0.35rem; font-size: 1.2rem; }
    .printables {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
      gap: 0.4rem;
      list-style: none;
      padding: 0;
      margin: 0 0 1rem;
    }
    .printables a {
      display: block;
      min-height: 48px;
      padding: 0.55rem 0.7rem;
      border: 1px solid var(--line);
      background: var(--bg);
      text-decoration: none;
      color: var(--ink);
      border-radius: 0.35rem;
    }
    .printables a:hover { border-color: var(--accent); color: var(--accent); }
    .topics {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(18rem, 1fr));
      gap: 0.75rem;
    }
    .item-block {
      display: flex;
      flex-direction: column;
      border: 1px solid var(--line);
      background: var(--paper);
      border-radius: 0.5rem;
      min-height: 12rem;
    }
    .item-block h3 {
      margin: 0;
      padding: 0.7rem 0.8rem 0.25rem;
      font-size: 1.05rem;
    }
    .sheet-mains {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      padding: 0.4rem 0.75rem 0.6rem;
      flex: 1;
    }
    .sheet-main {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      min-height: 48px;
      padding: 0.45rem;
      border: 1px solid var(--line);
      border-radius: 0.35rem;
      text-decoration: none;
      color: inherit;
      background: var(--bg);
    }
    .sheet-main img {
      width: 100%;
      max-height: 12rem;
      object-fit: contain;
      background: #fff;
    }
    .sheet-kind {
      font-size: 0.75rem;
      letter-spacing: 0.04em;
      color: var(--muted);
    }
    .support-ref {
      margin-top: auto;
      padding: 0.65rem 0.8rem;
      border-top: 1px solid var(--line);
      font-size: 0.9rem;
    }
    .meta { color: var(--muted); font-size: 0.9rem; margin: 0 0 0.8rem; }
    .topics {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
      gap: 0.5rem;
    }
    dialog {
      width: min(44rem, 100%);
      max-height: min(90vh, 48rem);
      border: 1px solid var(--line);
      background: var(--paper);
      color: var(--ink);
      padding: 1.1rem 1.2rem 1.3rem;
    }
    dialog::backdrop { background: rgb(0 0 0 / 0.45); }
    dialog h1 { font-size: 1.35rem; }
    dialog .close {
      float: inline-end;
      margin-block-start: -0.2rem;
    }
    dialog ul { padding-inline-start: 1.2rem; }
    footer { padding-block: 1.5rem 2.5rem; color: var(--muted); font-size: 0.9rem; }
  </style>
</head>
<body>
  <header>
    <h1>cheat-sheets</h1>
    <p class="lede">Local index of cheat-sheets.org, grouped with official sites, saved copies, and Wikipedia clones.</p>
    <search>
      <form id="filter-form">
        <div>
          <label for="q">Filter topics</label>
          <input type="search" id="q" name="q" placeholder="python, awk, mysql…" autocomplete="off">
        </div>
        <button type="submit">Filter</button>
        <button type="reset">Clear</button>
      </form>
    </search>
    <nav aria-label="Groups">
      <ul id="group-nav"></ul>
    </nav>
    <p class="status" id="status" aria-live="polite"></p>
  </header>
  <main id="groups"></main>
  <footer>
    <p>Indexing, search, SEO, JSON-LD, and <a href="/llms.txt">llms.txt</a>:
    <a href="https://georgelambert.org/">George Lambert</a>
    &lt;<a href="mailto:marchon@gmail.com">marchon@gmail.com</a>&gt;,
    <a href="https://github.com/marchon">github.com/marchon</a>,
    <a href="https://github.com/marchon/cheat-sheets">github.com/marchon/cheat-sheets</a>.
    That credit is for the index and searchability only, not for the underlying cheat sheets.</p>
    <p>Source: <a href="https://cheat-sheets.org/">cheat-sheets.org</a>.
    Internet Archive snapshots:
    <a href="https://web.archive.org/web/20260000000000*/https://cheat-sheets.org/">Wayback Machine calendar for cheat-sheets.org</a>.
    Wikipedia extracts are CC BY-SA 4.0.
    JSON-LD graph: <a href="/graph.jsonld">graph.jsonld</a>.</p>
  </footer>
  <script type="application/json" id="catalog-data">__CATALOG__</script>
  <script>
    const catalog = JSON.parse(document.getElementById("catalog-data").textContent);
    const byId = Object.fromEntries(catalog.topics.map((t) => [t.id, t]));
    const groupsEl = document.getElementById("groups");
    const navEl = document.getElementById("group-nav");
    const statusEl = document.getElementById("status");
    const form = document.getElementById("filter-form");
    const q = document.getElementById("q");

    function linkList(items, hrefKey, labelKey) {
      if (!items || !items.length) return "<p>None listed.</p>";
      return "<ul>" + items.map((item) => {
        const href = item[hrefKey];
        const label = item[labelKey] || href;
        return `<li><a href="${href}">${escapeHtml(label)}</a></li>`;
      }).join("") + "</ul>";
    }

    function escapeHtml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;");
    }

    const PRINTABLE = new Set([".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ps", ".dvi", ".odt", ".doc", ".docx", ".rtf", ".epub"]);
    const IMAGE = new Set([".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"]);

    function localSaved(topic, file) {
      const url = file.url || "";
      let rel = "";
      if (url.includes("/saved-copy/")) {
        rel = decodeURIComponent(url.split("/saved-copy/")[1] || "");
        if (!rel || rel.endsWith("/") || !rel.split("/").pop().includes(".")) rel = rel.replace(/\\/+$/, "") + "/index.html";
        return encodeURI(`/${topic.path}/saved-copy/${rel}`);
      }
      if (url.includes("cheat-sheets.org") && (url.includes("/sites/") || url.includes("/own/"))) {
        try {
          rel = decodeURIComponent(new URL(url).pathname.replace(/^\\//, ""));
        } catch { rel = file.filename || ""; }
        if (!rel || rel.endsWith("/") || !rel.split("/").pop().includes(".")) rel = rel.replace(/\\/+$/, "") + "/index.html";
        return encodeURI(`/${topic.path}/hosted/${rel}`);
      }
      const name = (file.filename || "").replace(/^\\/+/, "");
      return encodeURI(`/${topic.path}/saved-copy/${name}`);
    }

    function isPrintable(file) {
      const name = (file.filename || file.url || "").split("?")[0];
      const ext = name.includes(".") ? ("." + name.split(".").pop().toLowerCase()) : "";
      return PRINTABLE.has(ext);
    }

    function fileLabel(file) {
      return (file.filename || "file").split("/").pop();
    }

    function sheetMain(topic, file) {
      const href = localSaved(topic, file);
      const name = fileLabel(file);
      const ext = name.includes(".") ? ("." + name.split(".").pop().toLowerCase()) : "";
      if (IMAGE.has(ext)) {
        return `<a class="sheet-main" href="${href}"><img src="${href}" alt="${escapeHtml(topic.title + " — " + name)}"><span class="sheet-name">${escapeHtml(name)}</span></a>`;
      }
      const kind = ext ? ext.slice(1).toUpperCase() : "FILE";
      return `<a class="sheet-main" href="${href}"><span class="sheet-kind">${escapeHtml(kind)}</span><span class="sheet-name">${escapeHtml(name)}</span></a>`;
    }

    function itemBlock(t) {
      const prints = (t.saved_copies || []).filter(isPrintable);
      const support = `/${t.path}/`;
      const mains = prints.length
        ? prints.map((s) => sheetMain(t, s)).join("")
        : `<a class="sheet-main" href="${support}">Open local files for ${escapeHtml(t.title)}</a>`;
      const text = [t.title, t.id, ...prints.map(fileLabel)].join(" ").toLowerCase();
      return `<article class="item-block" data-topic="${escapeHtml(t.id)}" data-text="${escapeHtml(text)}">
        <h3>${escapeHtml(t.title)}</h3>
        <div class="sheet-mains">${mains}</div>
        <a class="support-ref" href="${support}">Reference: sources and additional information</a>
      </article>`;
    }

    function render() {
      navEl.innerHTML = catalog.groups
        .filter((g) => g.topic_count)
        .map((g) => `<li><a href="${g.id}/">${escapeHtml(g.title)}</a></li>`)
        .join("");
      groupsEl.innerHTML = catalog.groups.filter((g) => g.topic_count).map((g) => {
        const members = catalog.topics.filter((t) => t.group === g.id);
        const cards = members.map(itemBlock).join("");
        return `<section class="group" id="${g.id}">
          <h2>${escapeHtml(g.title)}</h2>
          <p class="meta">${escapeHtml(g.description)} · ${g.topic_count} topics · ${g.saved_copy_count} saved copies</p>
          <div class="topics">${cards}</div>
        </section>`;
      }).join("");
      statusEl.textContent = `${catalog.topic_count} topics in ${catalog.group_count} groups.`;
    }

    function applyFilter(term) {
      const needle = term.trim().toLowerCase();
      let shown = 0;
      for (const article of groupsEl.querySelectorAll("article")) {
        const match = !needle || article.dataset.text.includes(needle);
        article.hidden = !match;
        if (match) shown += 1;
      }
      for (const section of groupsEl.querySelectorAll("section.group")) {
        section.hidden = !section.querySelector("article:not([hidden])");
      }
      statusEl.textContent = needle
        ? `${shown} topic${shown === 1 ? "" : "s"} matching “${term.trim()}”.`
        : `${catalog.topic_count} topics in ${catalog.group_count} groups.`;
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      applyFilter(q.value);
    });
    form.addEventListener("reset", () => {
      queueMicrotask(() => applyFilter(""));
    });
    q.addEventListener("input", () => applyFilter(q.value));
    render();
    const params = new URLSearchParams(location.search);
    if (params.has("q")) {
      q.value = params.get("q") || "";
      applyFilter(q.value);
    }
  </script>
</body>
</html>
"""


def slim_catalog(catalog: dict) -> dict:
    topics = []
    for t in catalog["topics"]:
        topics.append(
            {
                "id": t["id"],
                "slug": t["slug"],
                "title": re.sub(r"\s+W$", "", t["title"]).strip(),
                "group": t["group"],
                "path": t["path"],
                "source_anchor": t.get("source_anchor"),
                "wikipedia": t.get("wikipedia"),
                "wikipedia_urls": t.get("wikipedia_urls") or [],
                "official_websites": t.get("official_websites") or [],
                "see_also": t.get("see_also") or [],
                "saved_copies": [
                    {"filename": s["filename"], "url": s["url"]} for s in t.get("saved_copies") or []
                ],
                "items": [
                    {
                        "title": i["title"],
                        "online": (i.get("online") or [])[:3],
                        "saved": (i.get("saved") or [])[:3],
                    }
                    for i in t.get("items") or []
                ],
            }
        )
    groups = []
    for g in catalog["groups"]:
        if not g["topic_count"]:
            continue
        meta = GROUPS.get(g["id"], {})
        clean_topics = [
            {**tt, "title": re.sub(r"\s+W$", "", tt["title"]).strip()}
            for tt in g.get("topics") or []
        ]
        groups.append(
            {
                **g,
                "topics": clean_topics,
                "description": meta.get("description", g.get("description", "")),
            }
        )
    return {
        "source": catalog["source"],
        "topic_count": catalog["topic_count"],
        "group_count": catalog["group_count"],
        "groups": groups,
        "topics": topics,
    }


PRINTABLE_EXTS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".ps",
    ".dvi",
    ".odt",
    ".doc",
    ".docx",
    ".rtf",
    ".epub",
}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def is_printable(sc: dict) -> bool:
    name = sc.get("filename") or urlparse(sc.get("url") or "").path
    return Path(unquote(name)).suffix.lower() in PRINTABLE_EXTS


def local_asset_path(topic: dict, sc: dict) -> str:
    parsed = urlparse(sc.get("url") or "")
    path = unquote(parsed.path)
    if "/saved-copy/" in path:
        rel = path.split("/saved-copy/", 1)[1].lstrip("/")
        if not rel or rel.endswith("/") or not Path(rel).suffix:
            rel = rel.rstrip("/") + "/index.html"
        return f"{topic['path']}/saved-copy/{rel}"
    if parsed.netloc.endswith("cheat-sheets.org"):
        rel = path.lstrip("/")
        if not rel or rel.endswith("/") or not Path(rel).suffix:
            rel = rel.rstrip("/") + "/index.html"
        return f"{topic['path']}/hosted/{rel}"
    name = Path(path).name or (sc.get("filename") or "file").lstrip("/")
    return f"{topic['path']}/saved-copy/{name}"


def display_name(sc: dict) -> str:
    name = sc.get("filename") or urlparse(sc.get("url") or "").path
    return Path(unquote(name.rstrip("/"))).name or unquote(name)


def href_for(path: str) -> str:
    return "/" + quote(path.lstrip("/"), safe="/")


def sorted_saved(copies: list[dict]) -> tuple[list[dict], list[dict]]:
    printable = [s for s in copies if is_printable(s)]
    other = [s for s in copies if not is_printable(s)]
    return printable, other


def existing_saved(root: Path, topic: dict, copies: list[dict]) -> list[dict]:
    kept = []
    for s in copies:
        if (root / local_asset_path(topic, s)).exists():
            kept.append(s)
    return kept


def sheet_anchor(topic: dict, sc: dict) -> str:
    href = href_for(local_asset_path(topic, sc))
    name = display_name(sc)
    ext = Path(name).suffix.lower()
    if ext in IMAGE_EXTS:
        return (
            f'<a class="sheet-main" href="{escape(href)}">'
            f'<img src="{escape(href)}" alt="{escape(topic["title"] + " — " + name)}">'
            f'<span class="sheet-name">{escape(name)}</span></a>'
        )
    kind = ext[1:].upper() if ext else "FILE"
    return (
        f'<a class="sheet-main" href="{escape(href)}">'
        f'<span class="sheet-kind">{escape(kind)}</span> '
        f'<span class="sheet-name">{escape(name)}</span></a>'
    )


def item_block_html(topic: dict, copies: list[dict]) -> str:
    printable, _other = sorted_saved(copies)
    support = f'/{topic["path"]}/'
    if printable:
        mains = "\n        ".join(sheet_anchor(topic, s) for s in printable)
    else:
        mains = f'<a class="sheet-main" href="{escape(support)}">Open local files for {escape(topic["title"])}</a>'
    return f'''    <article class="item-block">
      <h3>{escape(topic["title"])}</h3>
      <div class="sheet-mains">
        {mains}
      </div>
      <a class="support-ref" href="{escape(support)}">Reference: sources and additional information</a>
    </article>'''


CREDIT_HTML = (
    'Indexing, search, SEO, JSON-LD, and <a href="/llms.txt">llms.txt</a>: '
    '<a href="https://georgelambert.org/">George Lambert</a> '
    '&lt;<a href="mailto:marchon@gmail.com">marchon@gmail.com</a>&gt;, '
    '<a href="https://github.com/marchon">github.com/marchon</a>, '
    '<a href="https://github.com/marchon/cheat-sheets">github.com/marchon/cheat-sheets</a>. '
    "That credit is for the index and searchability only, not for the underlying cheat sheets. "
    f'Source: <a href="{SOURCE}">cheat-sheets.org</a>. '
    f'Internet Archive snapshots: <a href="{WAYBACK}">Wayback Machine calendar for cheat-sheets.org</a>. '
    "Wikipedia extracts are CC BY-SA 4.0."
)

CSS = """
:root { color-scheme: light dark; --bg:#f6f3ee; --ink:#1c1916; --muted:#5c564e; --paper:#fffdf8; --line:#d9d2c6; --accent:#8a3b12; --focus:#0b57d0; }
@media (prefers-color-scheme: dark) { :root { --bg:#161513; --ink:#ece7df; --muted:#b3aaa0; --paper:#221f1c; --line:#3a3530; --accent:#e0a070; --focus:#8ab4f8; } }
* { box-sizing: border-box; }
html { background: var(--bg); color: var(--ink); }
body { margin: 0; font: 1rem/1.5 ui-sans-serif, system-ui, sans-serif; }
a { color: var(--accent); }
a:focus-visible, button:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
header, footer, main { max-width: 52rem; margin-inline: auto; padding-inline: 1.25rem; }
header { padding-block: 1.5rem 1rem; }
h1 { font-size: 1.6rem; margin: 0 0 0.4rem; }
.lede, .meta, footer { color: var(--muted); }
main ul { padding-inline-start: 1.2rem; }
footer { padding-block: 1.5rem 2.5rem; font-size: 0.95rem; }
nav a { margin-inline-end: 0.75rem; }
.printables { display: grid; grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr)); gap: 0.4rem; list-style: none; padding: 0; }
.printables a, .sheet-main { display: block; min-height: 48px; padding: 0.55rem 0.7rem; border: 1px solid var(--line); background: var(--paper); text-decoration: none; color: var(--ink); border-radius: 0.35rem; }
.topics { display: grid; grid-template-columns: repeat(auto-fill, minmax(18rem, 1fr)); gap: 0.75rem; }
.item-block { display: flex; flex-direction: column; border: 1px solid var(--line); background: var(--paper); border-radius: 0.5rem; }
.item-block h2, .item-block h3 { margin: 0; padding: 0.7rem 0.8rem 0.25rem; font-size: 1.05rem; }
.sheet-mains { display: flex; flex-direction: column; gap: 0.4rem; padding: 0.4rem 0.75rem 0.6rem; flex: 1; }
.sheet-main img { width: 100%; max-height: 14rem; object-fit: contain; background: #fff; }
.sheet-kind { font-size: 0.75rem; color: var(--muted); }
.support-ref { margin-top: auto; padding: 0.65rem 0.8rem; border-top: 1px solid var(--line); font-size: 0.9rem; }
"""


def escape(text: str) -> str:
    return (
        str(text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def jsonld_script(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2).replace("<", "\\u003c")


def inner_page(title: str, canonical: str, description: str, body: str, ld: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <!-- search-index-tags -->
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <script type="application/ld+json">{jsonld_script(ld)}</script>
  <!-- /search-index-tags -->
  <style>{CSS}</style>
</head>
<body>
  <header>
    <nav><a href="/">Index</a></nav>
    <h1>{escape(title)}</h1>
    <p class="lede">{escape(description)}</p>
  </header>
  <main>
{body}
  </main>
  <footer>
    {CREDIT_HTML}
  </footer>
</body>
</html>
"""


def write_static_files(root: Path, catalog: dict, slim: dict) -> None:
    topics = slim["topics"]
    groups = slim["groups"]
    graph = full_graph(catalog, topics, groups)
    (root / "graph.jsonld").write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    urls = [f"{BASE}/", f"{BASE}/graph.jsonld"]
    by_group: dict[str, list] = {g["id"]: [] for g in groups}
    for t in topics:
        by_group.setdefault(t["group"], []).append(t)

    for g in groups:
        members = by_group.get(g["id"], [])
        blocks = []
        for t in members:
            copies = existing_saved(root, t, t.get("saved_copies") or [])
            blocks.append(item_block_html(t, copies))
        body = '    <div class="topics">\n' + "\n".join(blocks) + "\n    </div>"
        ld = page_graph(
            [
                person_node(),
                indexing_work_node(),
                source_org(),
                wayback_node(),
                website_node(),
                catalog_node(catalog, groups),
                group_node(g, members),
            ]
            + [n for t in members for n in topic_graph(t)]
        )
        gdir = root / g["id"]
        gdir.mkdir(parents=True, exist_ok=True)
        (gdir / "index.html").write_text(
            inner_page(
                g["title"],
                f"{BASE}/{g['id']}/",
                g.get("description") or g["title"],
                body,
                ld,
            ),
            encoding="utf-8",
        )
        urls.append(f"{BASE}/{g['id']}/")

    for t in topics:
        wiki_urls = t.get("wikipedia_urls") or ([t["wikipedia"]] if t.get("wikipedia") else [])
        saved = existing_saved(root, t, t.get("saved_copies") or [])
        see = t.get("see_also") or []
        by_id = {x["id"]: x for x in topics}
        printable, other = sorted_saved(saved)
        tdir = root / t["path"]

        def ul(entries: list[str], cls: str = "") -> str:
            if not entries:
                return "    <p>None stored locally.</p>"
            cls_attr = f' class="{cls}"' if cls else ""
            return f"    <ul{cls_attr}>\n" + "\n".join(f"      <li>{e}</li>" for e in entries) + "\n    </ul>"

        sheet_mains = "\n        ".join(sheet_anchor(t, s) for s in printable) if printable else ""
        support = []
        if (tdir / "README.md").exists():
            support.append('<a href="README.md">Topic notes (README)</a>')
        if (tdir / "topic.json").exists():
            support.append('<a href="topic.json">Catalog record (JSON)</a>')
        if (tdir / "wikipedia.md").exists():
            support.append('<a href="wikipedia.md">Wikipedia clone</a>')
        for s in other:
            support.append(
                f'<a href="{escape(href_for(local_asset_path(t, s)))}">{escape(display_name(s))}</a>'
            )
        for s in see:
            if s.get("id") in by_id:
                support.append(
                    f'<a href="/{by_id[s["id"]]["path"]}/">{escape(s.get("label") or s["id"])} (related topic)</a>'
                )

        body_parts = [
            f'    <p class="meta">Group: <a href="/{t["group"]}/">{escape(GROUPS.get(t["group"], {}).get("title", t["group"]))}</a></p>',
            "    <h2>Cheat sheets</h2>",
            f'    <div class="sheet-mains">\n        {sheet_mains}\n    </div>'
            if sheet_mains
            else "    <p>No local PDF or image cheat sheet is stored for this topic.</p>",
            '    <h2>Reference: sources and additional information</h2>',
            ul(support) if support else "    <p>None stored locally.</p>",
        ]
        ld = page_graph(
            [
                person_node(),
                indexing_work_node(),
                source_org(),
                wayback_node(),
                website_node(),
                *topic_graph(t),
            ]
        )
        tdir = root / t["path"]
        tdir.mkdir(parents=True, exist_ok=True)
        (tdir / "index.html").write_text(
            inner_page(
                t["title"],
                f"{BASE}/{t['path']}/",
                f"{t['title']} cheat sheets from cheat-sheets.org.",
                "\n".join(body_parts),
                ld,
            ),
            encoding="utf-8",
        )
        urls.append(f"{BASE}/{t['path']}/")

    sitemap = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        *[f"  <url><loc>{u}</loc></url>" for u in urls],
        "</urlset>",
        "",
    ]
    (root / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    (root / "robots.txt").write_text(
        "\n".join(
            [
                "User-agent: *",
                "Allow: /",
                f"Sitemap: {BASE}/sitemap.xml",
                "",
            ]
        ),
        encoding="utf-8",
    )
    llms = [
        "# cheat-sheets index",
        "",
        f"Canonical: {BASE}/",
        f"Source: {SOURCE}",
        f"Wayback Machine: {WAYBACK}",
        f"JSON-LD: {BASE}/graph.jsonld",
        f"Sitemap: {BASE}/sitemap.xml",
        "",
        "Indexing, searchability, SEO, JSON-LD, and this llms.txt file:",
        "George Lambert <marchon@gmail.com>, https://georgelambert.org/,",
        "https://github.com/marchon, https://github.com/marchon/cheat-sheets.",
        "That credit is for the index and searchability only, not for the underlying cheat sheets.",
        "",
        "This archive indexes cheat-sheets.org topics in groups, with official websites,",
        "saved copies, and Wikipedia clones. Credit cheat-sheets.org and the Internet Archive",
        "snapshots linked above for the source material.",
        "",
        "## Groups",
        "",
        *[f"- {g['title']}: {BASE}/{g['id']}/" for g in groups],
        "",
    ]
    (root / "llms.txt").write_text("\n".join(llms), encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog" / "catalog.json").read_text(encoding="utf-8"))
    slim = slim_catalog(catalog)
    for t in slim["topics"]:
        t["saved_copies"] = existing_saved(root, t, t.get("saved_copies") or [])
    payload = json.dumps(slim, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    ld = jsonld_script(homepage_graph(catalog, slim["topics"], slim["groups"]))
    html = PAGE.replace("__CATALOG__", payload).replace("__JSONLD__", ld)
    (root / "index.html").write_text(html, encoding="utf-8")
    write_static_files(root, catalog, slim)
    print(
        "wrote index.html",
        (root / "index.html").stat().st_size,
        "graph.jsonld",
        (root / "graph.jsonld").stat().st_size,
        "topics",
        slim["topic_count"],
    )


if __name__ == "__main__":
    main()
