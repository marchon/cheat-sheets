# hg-remove

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hg-remove/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
batch
,
flac
,
quilt
,
virsh
,
gitlab ctl
.
hg remove
Remove specified files from the staging area.
More information:
https://www.mercurial-scm.org/doc/hg.1.html#remove
.
Remove files or directories from the staging area:
hg remove {{path/to/file}}
Remove all staged files matching a specified pattern:
hg remove --include {{pattern}}
Remove all staged files, excluding those that match a specified pattern:
hg remove --exclude {{pattern}}
Recursively remove sub-repositories:
hg remove --subrepos
Remove files from the repository that have been physically removed:
hg remove --after
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
