# hg-status

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hg-status/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
elm
,
xdelta
,
swc
,
ocrmypdf
,
direnv
.
hg status
Show files that have changed in the working directory.
More information:
https://www.mercurial-scm.org/doc/hg.1.html#status
.
Display the status of changed files:
hg status
Display only modified files:
hg status --modified
Display only added files:
hg status --added
Display only removed files:
hg status --removed
Display only deleted (but tracked) files:
hg status --deleted
Display changes in the working directory compared to a specified changeset:
hg status --rev {{revision}}
Display only files matching a specified glob pattern:
hg status --include {{pattern}}
Display files, excluding those that match a specified glob pattern:
hg status --exclude {{pattern}}
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
