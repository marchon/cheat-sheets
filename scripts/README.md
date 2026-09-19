# scripts

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Build tools that parse cheat-sheets.org, group topics, and download assets.

## Install

```sh
cd ..
python3 -m pip install beautifulsoup4
```

## Usage

```sh
PYTHONPATH=scripts python3 scripts/parse_index.py
PYTHONPATH=scripts python3 scripts/write_tree.py
PYTHONPATH=scripts python3 scripts/download_saved_copies.py
PYTHONPATH=scripts python3 scripts/clone_wikipedia.py
PYTHONPATH=scripts python3 scripts/fetch_tldr.py
PYTHONPATH=scripts python3 scripts/build_site.py
python3 -m http.server 8765
```

Pass a group id to limit downloads, for example `python3 scripts/download_saved_copies.py languages`.

## Contributing

Questions: open an issue. PRs that improve parsing or grouping are welcome.

## License

UNLICENSED © George Lambert
