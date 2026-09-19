# git-show-index

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-show-index/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mr
,
act
,
codespell
,
az
,
arch
,
waitress serve
.
git show-index
Show the packed archive index of a Git repository.
More information:
https://git-scm.com/docs/git-show-index
.
Read an IDX file for a Git packfile and dump its contents to stdout:
git show-index {{path/to/file.idx}}
Specify the hash algorithm for the index file (experimental):
git show-index --object-format={{sha1|sha256}} {{path/to/file}}
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
