# egrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/egrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vsce
,
gacutil
,
scan build
,
git rename remote
.
egrep
Find patterns in files using extended regular expression (supports
?
,
+
,
{}
,
()
and
|
).
More information:
https://manned.org/egrep
.
Search for a pattern within a file:
egrep "{{search_pattern}}" {{path/to/file}}
Search for a pattern within multiple files:
egrep "{{search_pattern}}" {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}
Search stdin for a pattern:
cat {{path/to/file}} | egrep {{search_pattern}}
Print file name and line number for each match:
egrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}
Search for a pattern in all files recursively in a directory, ignoring binary files:
egrep --recursive --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}
Search for lines that do not match a pattern:
egrep --invert-match "{{search_pattern}}" {{path/to/file}}
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
