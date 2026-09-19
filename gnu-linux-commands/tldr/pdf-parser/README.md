# pdf-parser

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdf-parser/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
case
,
godoc
,
make
,
csvcut
,
git coauthor
.
pdf-parser
Identify fundamental elements of a PDF file without rendering it.
More information:
https://blog.didierstevens.com/programs/pdf-tools
.
Display statistics for a PDF file:
pdf-parser --stats {{path/to/file.pdf}}
Display objects of type
/Font
in a PDF file:
pdf-parser --type={{/Font}} {{path/to/file.pdf}}
Search for strings in indirect objects:
pdf-parser --search={{search_string}} {{path/to/file.pdf}}
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
