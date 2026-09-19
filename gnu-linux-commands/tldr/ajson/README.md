# ajson

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ajson/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lzop
,
ls
,
xml transform
,
csvkit
.
ajson
Executes JSONPath on JSON objects.
More information:
https://github.com/spyzhov/ajson
.
Read JSON from a file and execute a specified JSONPath expression:
ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}
Read JSON from stdin and execute a specified JSONPath expression:
cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'
Read JSON from a URL and evaluate a specified JSONPath expression:
ajson '{{avg($..price)}}' '{{https://example.com/api/}}'
Read some simple JSON and calculate a value:
echo '{{3}}' | ajson '{{2 * pi * $}}'
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
