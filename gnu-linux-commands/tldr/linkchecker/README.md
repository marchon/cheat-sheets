# linkchecker

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/linkchecker/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
svn changelist
,
rtmpdump
,
odps inst
.
linkchecker
Command-line client to check HTML documents and websites for broken links.
More information:
https://linkchecker.github.io/linkchecker/
.
Find broken links on https://example.com/:
linkchecker {{https://example.com/}}
Also check URLs that point to external domains:
linkchecker --check-extern {{https://example.com/}}
Ignore URLs that match a specific regular expression:
linkchecker --ignore-url {{regular_expression}} {{https://example.com/}}
Output results to a CSV file:
linkchecker --file-output {{csv}}/{{path/to/file}} {{https://example.com/}}
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
