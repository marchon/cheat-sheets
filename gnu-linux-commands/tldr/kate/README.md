# kate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xidel
,
scc
,
groff
,
nextflow
,
msbuild
.
kate
KDE Text Editor.
More information:
https://kate-editor.org/
.
Launch Kate and open specific files:
kate {{path/to/file1}} {{path/to/file2}}
Open a remote document in Kate:
kate {{https://example.com/path/to/file}}
Launch Kate, creating a new instance even if one is already open:
kate --new
Open a file in Kate with the cursor at the specific line:
kate --line {{line_number}} {{path/to/file}}
Open a file in Kate with the cursor at the specific line and column:
kate --line {{line_number}} --column {{column_number}} {{path/to/file}}
Launch Kate, creating a new temporary file with contents read from stdin:
cat {{path/to/file}} | kate --stdin
Display help:
kate --help
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
