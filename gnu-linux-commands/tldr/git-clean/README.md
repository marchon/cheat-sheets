# git-clean

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-clean/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
z
,
autoflake
,
rbenv
,
cpdf
,
fluxctl
.
git clean
Remove untracked files from the working tree.
More information:
https://git-scm.com/docs/git-clean
.
Delete files that are not tracked by Git:
git clean
Interactively delete files that are not tracked by Git:
git clean -i
Show what files would be deleted without actually deleting them:
git clean --dry-run
Forcefully delete files that are not tracked by Git:
git clean -f
Forcefully delete directories that are not tracked by Git:
git clean -fd
Delete untracked files, including ignored files in
.gitignore
and
.git/info/exclude
:
git clean -x
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
