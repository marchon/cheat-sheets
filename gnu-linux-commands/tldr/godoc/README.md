# godoc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/godoc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git info
,
iconv
,
git ignore io
.
godoc
Show documentation for go packages.
More information:
https://godoc.org/
.
Display help for package "fmt":
godoc {{fmt}}
Display help for the function "Printf" of "fmt" package:
godoc {{fmt}} {{Printf}}
Serve documentation as a web server on port 6060:
godoc -http=:{{6060}}
Create an index file:
godoc -write_index -index_files={{path/to/file}}
Use the given index file to search the docs:
godoc -http=:{{6060}} -index -index_files={{path/to/file}}
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
