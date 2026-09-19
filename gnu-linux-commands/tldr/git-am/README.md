# git-am

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-am/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git remote
,
umount
,
mlr
,
git bisect
.
git am
Apply patch files. Useful when receiving commits via email.
See also
git format-patch
, which can generate patch files.
More information:
https://git-scm.com/docs/git-am
.
Apply a patch file:
git am {{path/to/file.patch}}
Abort the process of applying a patch file:
git am --abort
Apply as much of a patch file as possible, saving failed hunks to reject files:
git am --reject {{path/to/file.patch}}
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
