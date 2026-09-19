# git-squash

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-squash/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
choose
,
git rebase
,
csslint
,
mpv
.
git squash
Squash multiple commits into a single commit.
Part of
git-extras
.
More information:
https://github.com/tj/git-extras/blob/master/Commands.md#git-squash
.
Merge all commits from a specific branch into the current branch as a single commit:
git squash {{source_branch}}
Squash all commits starting with a specific commit on the current branch:
git squash {{commit}}
Squash the
n
latest commits and commit with a message:
git squash HEAD~{{n}} "{{message}}"
Squash the
n
latest commits and commit concatenating all individual messages:
git squash --squash-msg HEAD~{{n}}
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
