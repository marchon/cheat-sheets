# catalog

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Machine-readable index of cheat-sheets.org topics, groups, and saved copies.

## Install

```sh
python3 scripts/parse_index.py
```

## Usage

```sh
python3 -c "import json; print(json.load(open('catalog/catalog.json'))['topic_count'])"
```

`source/index.html` is the saved homepage used to rebuild `catalog.json`.

## Contributing

Questions: open an issue. PRs that improve parsing are welcome.

## License

UNLICENSED © George Lambert
