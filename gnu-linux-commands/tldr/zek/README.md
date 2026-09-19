# zek

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zek/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nodemon
,
umount
,
ex
,
git annex
.
zek
Generate a Go struct from XML.
More information:
https://github.com/miku/zek
.
Generate a Go struct from a given XML from stdin and display output on stdout:
cat {{path/to/input.xml}} | zek
Generate a Go struct from a given XML from stdin and send output to a file:
curl -s {{https://url/to/xml}} | zek -o {{path/to/output.go}}
Generate an example Go program from a given XML from stdin and send output to a file:
cat {{path/to/input.xml}} | zek -p -o {{path/to/output.go}}
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
