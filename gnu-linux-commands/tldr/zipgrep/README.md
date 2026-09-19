# zipgrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zipgrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
solo
,
kubectl delete
,
shasum
.
zipgrep
Find patterns in files in a ZIP archive using extended regular expression (supports
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
https://manned.org/zipgrep
.
Search for a pattern within a ZIP archive:
zipgrep "{{search_pattern}}" {{path/to/file.zip}}
Print file name and line number for each match:
zipgrep -H -n "{{search_pattern}}" {{path/to/file.zip}}
Search for lines that do not match a pattern:
zipgrep -v "{{search_pattern}}" {{path/to/file.zip}}
Specify files inside a ZIP archive from search:
zipgrep "{{search_pattern}}" {{path/to/file.zip}} {{file/to/search1}} {{file/to/search2}}
Exclude files inside a ZIP archive from search:
zipgrep "{{search_pattern}}" {{path/to/file.zip}} -x {{file/to/exclude1}} {{file/to/exclude2}}
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
