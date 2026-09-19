# json5

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/json5/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
transcrypt
,
robo
,
texdoc
,
git archive
.
json5
A command-line tool for converting JSON5 files to JSON.
More information:
https://json5.org
.
Convert JSON5 stdin to JSON stdout:
echo {{input}} | json5
Convert a JSON5 file to JSON and output to stdout:
json5 {{path/to/input_file.json5}}
Convert a JSON5 file to the specified JSON file:
json5 {{path/to/input_file.json5}} --out-file {{path/to/output_file.json}}
Validate a JSON5 file:
json5 {{path/to/input_file.json5}} --validate
Specify the number of spaces to indent by (or "t" for tabs):
json5 --space {{indent_amount}}
View available options:
json5 --help
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
