# git-stage

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-stage/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git abort
,
entr
,
ioping
,
git locked
.
git stage
Add file contents to the staging area.
Synonym of
git add
.
More information:
https://git-scm.com/docs/git-stage
.
Add a file to the index:
git stage {{path/to/file}}
Add all files (tracked and untracked):
git stage -A
Only add already tracked files:
git stage -u
Also add ignored files:
git stage -f
Interactively stage parts of files:
git stage -p
Interactively stage parts of a given file:
git stage -p {{path/to/file}}
Interactively stage a file:
git stage -i
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
