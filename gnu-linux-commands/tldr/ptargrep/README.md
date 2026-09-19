# ptargrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ptargrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vboxmanage
,
git sync
,
speedtest
.
ptargrep
Find regular expression patterns in one or more tar archive files.
More information:
https://manned.org/ptargrep
.
Search for a pattern within a tar file:
ptargrep "{{search_pattern}}" {{path/to/file}}
Search for a pattern within multiple files:
ptargrep "{{search_pattern}}" {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}
Extract to the current directory using the basename of the file from the archive:
ptargrep --basename "{{search_pattern}}" {{path/to/file}}
Search for a case-insensitive pattern matching within a tar file:
ptargrep --ignore-case "{{search_pattern}}" {{path/to/file}}
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
