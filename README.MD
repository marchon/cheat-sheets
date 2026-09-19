# cheat-sheets

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Indexed archive of cheat-sheets.org, grouped with saved copies and Wikipedia clones.

Local mirror of [cheat-sheets.org](https://www.cheat-sheets.org/) topics, organized using the site's See also clusters and the groups listed in the original request: languages, databases, applications, business processes, GNU/Linux commands, file formats, and online data services.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Background](#background)
- [Groups](#groups)
- [Contributing](#contributing)
- [License](#license)

## Install

```sh
git clone .
python3 scripts/parse_index.py
python3 scripts/write_tree.py
```

## Usage

Rebuild the catalog from a saved homepage, then download assets:

```sh
python3 scripts/parse_index.py
python3 scripts/write_tree.py
python3 scripts/download_saved_copies.py
python3 scripts/clone_wikipedia.py
python3 scripts/fetch_tldr.py
```

Open the web index (searchable groups and topic pages):

```sh
python3 scripts/build_site.py
python3 -m http.server 8765
```

Then visit [http://127.0.0.1:8765/](http://127.0.0.1:8765/). The page is `index.html` at the repository root.

Browse group folders directly if you prefer files. Each topic folder keeps official websites, See also links, `saved-copy/` files, and a Wikipedia clone.

## Background

Original request (from the workspace README):

- Read every cheat sheet listed on https://www.cheat-sheets.org/
- Index them in groups (languages, databases, applications, business processes, GNU/Linux commands such as cat, less, more, awk, sed, ls, file formats, online data services, and similar logical groupings)
- Use See also clusters such as Linux and Unix as grouping patterns
- Keep every `saved-copy/` file in the correct category
- Record Official websites when listed
- Clone listed Wikipedia entries (example: https://en.wikipedia.org/wiki/Google_App_Engine)

Catalog snapshot: 285 topics, 668 saved copies, 276 Wikipedia links, 203 official websites.

## Groups

- [Languages](languages/) — 42 topics, 178 saved copies, 32 Wikipedia entries
- [Databases](databases/) — 19 topics, 29 saved copies, 18 Wikipedia entries
- [Applications](applications/) — 24 topics, 37 saved copies, 24 Wikipedia entries
- [Business processes](business-processes/) — 8 topics, 5 saved copies, 8 Wikipedia entries
- [GNU / Linux commands](gnu-linux-commands/) — 16 topics, 55 saved copies, 15 Wikipedia entries
- [File formats](file-formats/) — 30 topics, 105 saved copies, 28 Wikipedia entries
- [Online data services](online-data-services/) — 7 topics, 7 saved copies, 7 Wikipedia entries
- [Web](web/) — 23 topics, 43 saved copies, 23 Wikipedia entries
- [Operating systems](operating-systems/) — 12 topics, 15 saved copies, 12 Wikipedia entries
- [Mathematics and science](mathematics-and-science/) — 24 topics, 74 saved copies, 24 Wikipedia entries
- [Version control](version-control/) — 5 topics, 35 saved copies, 5 Wikipedia entries
- [Editors and IDEs](editors-and-ides/) — 10 topics, 41 saved copies, 9 Wikipedia entries
- [Networking and protocols](networking-and-protocols/) — 7 topics, 7 saved copies, 7 Wikipedia entries
- [Cloud and DevOps](cloud-and-devops/) — 19 topics, 4 saved copies, 17 Wikipedia entries
- [Graphics and design](graphics-and-design/) — 8 topics, 15 saved copies, 8 Wikipedia entries
- [Frameworks and libraries](frameworks-and-libraries/) — 25 topics, 37 saved copies, 25 Wikipedia entries
- [Security](security/) — 1 topics, 0 saved copies, 1 Wikipedia entries
- [Hardware and embedded](hardware-and-embedded/) — 4 topics, 6 saved copies, 4 Wikipedia entries
- [Other](other/) — 1 topics, 0 saved copies, 1 Wikipedia entries

Machine-readable catalog: [catalog/catalog.json](catalog/catalog.json).

## Contributing

Questions: open an issue in this repository. Pull requests that fix catalog grouping or add missing saved copies are welcome.

## License

UNLICENSED © George Lambert. Indexed cheat sheets, saved copies, and Wikipedia extracts remain under their original publishers' terms; Wikipedia text is CC BY-SA 4.0.
