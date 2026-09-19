"""Build a static HTML index of the cheat-sheet catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path

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
  <dialog id="topic-dialog" closedby="any" aria-labelledby="dialog-title">
    <form method="dialog"><button class="close" value="close">Close</button></form>
    <h1 id="dialog-title"></h1>
    <div id="dialog-body"></div>
  </dialog>
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
    const dialog = document.getElementById("topic-dialog");
    const dialogTitle = document.getElementById("dialog-title");
    const dialogBody = document.getElementById("dialog-body");
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

    function localSaved(topic, file) {
      const name = file.filename.replace(/^\\/+/, "");
      return encodeURI(`${topic.path}/saved-copy/${name}`);
    }

    function render() {
      navEl.innerHTML = catalog.groups
        .filter((g) => g.topic_count)
        .map((g) => `<li><a href="${g.id}/">${escapeHtml(g.title)}</a></li>`)
        .join("");
      groupsEl.innerHTML = catalog.groups.filter((g) => g.topic_count).map((g) => {
        const members = catalog.topics.filter((t) => t.group === g.id);
        const cards = members.map((t) => `
          <article data-topic="${escapeHtml(t.id)}" data-text="${escapeHtml((t.title + " " + t.id + " " + (t.official_websites || []).map((o) => o.label || o.url).join(" ")).toLowerCase())}">
            <button type="button" class="topic" data-open="${escapeHtml(t.id)}">${escapeHtml(t.title)}</button>
          </article>`).join("");
        return `<section class="group" id="${g.id}">
          <h2>${escapeHtml(g.title)}</h2>
          <p class="meta">${escapeHtml(g.description)} · ${g.topic_count} topics · ${g.saved_copy_count} saved copies</p>
          <div class="topics">${cards}</div>
        </section>`;
      }).join("");
      statusEl.textContent = `${catalog.topic_count} topics in ${catalog.group_count} groups.`;
    }

    function openTopic(id) {
      const t = byId[id];
      if (!t) return;
      dialogTitle.textContent = t.title;
      const wiki = (t.wikipedia_urls && t.wikipedia_urls.length ? t.wikipedia_urls : (t.wikipedia ? [t.wikipedia] : []));
      const saved = (t.saved_copies || []).map((s) => {
        const local = localSaved(t, s);
        return `<li><a href="${local}">${escapeHtml(s.filename)}</a> · <a href="${s.url}">source</a></li>`;
      }).join("");
      const sheets = (t.items || []).map((item) => {
        const href = (item.saved && item.saved[0]) || (item.online && item.online[0]) || t.source_anchor;
        return `<li><a href="${href}">${escapeHtml(item.title)}</a></li>`;
      }).join("");
      const see = (t.see_also || []).map((s) => {
        const other = byId[s.id];
        if (other) {
          return `<li><button type="button" class="topic" data-open="${escapeHtml(other.id)}">${escapeHtml(s.label || other.title)}</button></li>`;
        }
        return `<li>${escapeHtml(s.label || s.id)}</li>`;
      }).join("");
      dialogBody.innerHTML = `
        <p><a href="${t.path}/">topic page</a>
        · <a href="${t.source_anchor}">cheat-sheets.org#${escapeHtml(t.id)}</a></p>
        <h2>Official websites</h2>
        ${linkList(t.official_websites, "url", "label")}
        <h2>Wikipedia</h2>
        ${wiki.length ? "<ul>" + wiki.map((u, i) => `<li><a href="${u}">${escapeHtml(u)}</a>${i === 0 ? ` · <a href="${t.path}/wikipedia.md">local clone</a>` : ""}</li>`).join("") + "</ul>" : "<p>None listed.</p>"}
        <h2>Saved copies</h2>
        ${saved ? "<ul>" + saved + "</ul>" : "<p>None listed.</p>"}
        <h2>Cheat sheets</h2>
        ${sheets ? "<ul>" + sheets + "</ul>" : "<p>None listed.</p>"}
        <h2>See also</h2>
        ${see ? "<ul>" + see + "</ul>" : "<p>None listed.</p>"}
      `;
      dialog.showModal();
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

    groupsEl.addEventListener("click", (event) => {
      const btn = event.target.closest("[data-open]");
      if (btn) openTopic(btn.dataset.open);
    });
    dialogBody.addEventListener("click", (event) => {
      const btn = event.target.closest("[data-open]");
      if (btn) openTopic(btn.dataset.open);
    });
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      applyFilter(q.value);
    });
    form.addEventListener("reset", () => {
      queueMicrotask(() => applyFilter(""));
    });
    q.addEventListener("input", () => applyFilter(q.value));
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) dialog.close();
    });
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
        items = "\n".join(
            f'      <li><a href="/{t["path"]}/">{escape(t["title"])}</a></li>' for t in members
        )
        body = f"    <ul>\n{items}\n    </ul>"
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
        official = t.get("official_websites") or []
        saved = t.get("saved_copies") or []
        items = t.get("items") or []
        see = t.get("see_also") or []
        by_id = {x["id"]: x for x in topics}

        def ul(entries: list[str]) -> str:
            if not entries:
                return "    <p>None listed.</p>"
            return "    <ul>\n" + "\n".join(f"      <li>{e}</li>" for e in entries) + "\n    </ul>"

        body_parts = [
            f'    <p><a href="{escape(t.get("source_anchor") or SOURCE)}">Original listing on cheat-sheets.org</a></p>',
            "    <h2>Official websites</h2>",
            ul([f'<a href="{escape(o["url"])}">{escape(o.get("label") or o["url"])}</a>' for o in official]),
            "    <h2>Wikipedia</h2>",
            ul(
                [
                    f'<a href="{escape(u)}">{escape(u)}</a>'
                    + (f' · <a href="wikipedia.md">local clone</a>' if i == 0 else "")
                    for i, u in enumerate(wiki_urls)
                ]
            ),
            "    <h2>Saved copies</h2>",
            ul(
                [
                    f'<a href="saved-copy/{escape(s["filename"])}">{escape(s["filename"])}</a> · <a href="{escape(s["url"])}">source</a>'
                    if not str(s["filename"]).startswith("/")
                    else f'<a href="{escape(s["url"])}">{escape(s["filename"])}</a>'
                    for s in saved
                ]
            ),
            "    <h2>Cheat sheets</h2>",
            ul(
                [
                    f'<a href="{escape((i.get("saved") or i.get("online") or [SOURCE])[0])}">{escape(i["title"])}</a>'
                    for i in items
                ]
            ),
            "    <h2>See also</h2>",
            ul(
                [
                    f'<a href="/{by_id[s["id"]]["path"]}/">{escape(s.get("label") or s["id"])}</a>'
                    if s.get("id") in by_id
                    else escape(s.get("label") or s.get("id"))
                    for s in see
                ]
            ),
            f'    <p class="meta">Group: <a href="/{t["group"]}/">{escape(GROUPS.get(t["group"], {}).get("title", t["group"]))}</a></p>',
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
