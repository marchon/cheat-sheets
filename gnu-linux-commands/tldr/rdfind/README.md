# rdfind

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rdfind/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kubectl
,
lua
,
z
,
paperkey
,
docsify
.
rdfind
Find files with duplicate content and get rid of them.
More information:
https://rdfind.pauldreik.se
.
Identify all duplicates in a given directory and output a summary:
rdfind -dryrun true {{path/to/directory}}
Replace all duplicates with hardlinks:
rdfind -makehardlinks true {{path/to/directory}}
Replace all duplicates with symlinks/soft links:
rdfind -makesymlinks true {{path/to/directory}}
Delete all duplicates and do not ignore empty files:
rdfind -deleteduplicates true -ignoreempty false {{path/to/directory}}
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
