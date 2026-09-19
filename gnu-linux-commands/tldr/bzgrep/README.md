# bzgrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bzgrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tlmgr remove
,
gvpack
,
cpdf
,
hakyll init
.
bzgrep
Find patterns in bzip2 compressed files using grep.
More information:
https://manned.org/bzgrep
.
Search for a pattern within a compressed file:
bzgrep "{{search_pattern}}" {{path/to/file}}
Use extended regular expressions (supports
?
,
+
,
{}
,
()
and
|
), in case-insensitive mode:
bzgrep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}
Print 3 lines of context around, before, or after each match:
bzgrep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}
Print file name and line number for each match:
bzgrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}
Search for lines matching a pattern, printing only the matched text:
bzgrep --only-matching "{{search_pattern}}" {{path/to/file}}
Recursively search files in a bzip2 compressed tar archive for a pattern:
bzgrep --recursive "{{search_pattern}}" {{path/to/tar/file}}
Search stdin for lines that do not match a pattern:
cat {{/path/to/bz/compressed/file}} | bzgrep --invert-match "{{search_pattern}}"
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
