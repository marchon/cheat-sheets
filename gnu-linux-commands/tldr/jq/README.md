# jq

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jq/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wat2wasm
,
boot
,
corepack
,
ln
,
odps table
.
jq
A command-line JSON processor that uses a domain-specific language.
More information:
https://stedolan.github.io/jq/manual/
.
Execute a specific expression (print a colored and formatted json):
{{cat path/to/file.json}} | jq '{{.}}'
Execute a specific script:
{{cat path/to/file.json}} | jq --from-file {{path/to/script.jq}}
Pass specific arguments:
{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'
Print specific keys:
{{cat path/to/file.json}} | jq '{{.key1, .key2, ...}}'
Print specific array items:
{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'
Print all array items/object keys:
{{cat path/to/file.json}} | jq '.[]'
Add/remove specific keys:
{{cat path/to/file.json}} | jq '{{.}} {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'
This is a
tldr pages
(
source
, CC BY 4.0) web wrapper for
cheat-sheets.org
.
All commands
,
popular commands
,
most used linux commands
.
Referrals
.
Progressive Web Application (PWA) version to install on your device
.
