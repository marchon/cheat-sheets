# unison

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/unison/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
st flash
,
pkill
,
ghost
,
john
,
fswatch
.
unison
Bidirectional file synchronisation tool.
More information:
https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html
.
Sync two directories (creates log first time these two directories are synchronized):
unison {{path/to/directory_1}} {{path/to/directory_2}}
Automatically accept the (non-conflicting) defaults:
unison {{path/to/directory_1}} {{path/to/directory_2}} -auto
Ignore some files using a pattern:
unison {{path/to/directory_1}} {{path/to/directory_2}} -ignore {{pattern}}
Show documentation:
unison -doc {{topics}}
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
