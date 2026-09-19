# ia

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ia/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
truncate
,
makepasswd
,
protoc
.
ia
Command-line tool to interact with
archive.org
.
More information:
https://archive.org/services/docs/api/internetarchive/cli.html
.
Configure
ia
with API keys (some functions won't work without this step):
ia configure
Upload one or more items to
archive.org
:
ia upload {{identifier}} {{path/to/file}} --metadata="{{mediatype:data}}" --metadata="{{title:example}}"
Download one or more items from
archive.org
:
ia download {{item}}
Delete one or more items from
archive.org
:
ia delete {{identifier}} {{file}}
Search on
archive.org
, returning results as JSON:
ia search '{{subject:"subject" collection:collection}}'
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
