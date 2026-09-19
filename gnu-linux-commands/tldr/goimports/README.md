# goimports

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/goimports/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go fix
,
virsh pool build
,
csvstat
.
goimports
Updates Go import lines, adding missing ones and removing unreferenced ones.
More information:
https://godoc.org/golang.org/x/tools/cmd/goimports
.
Display the completed import source file:
goimports {{file}}.go
Write the result back to the source file instead of the standard output:
goimports -w {{file}}.go
Display diffs and write the result back to the source file:
goimports -w -d {{file}}.go
Set the import prefix string after 3rd-party packages (comma-separated list):
goimports -local {{path/to/package}} {{file}}.go
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
