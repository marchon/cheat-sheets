# sd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
terminalizer
,
gocryptfs
,
ogrinfo
.
sd
Intuitive find & replace CLI.
More information:
https://github.com/chmln/sd
.
Trim some whitespace using a regular expression:
{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''
Replace words using capture groups:
{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'
Find and replace in a file printing the result to stdout:
sd -p {{'window.fetch'}} {{'fetch'}} {{http.js}}
Find and replace across a project changing each file in place:
sd {{'from "react"'}} {{'from "preact"'}} $(find . -type f)
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
