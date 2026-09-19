# git-worktree

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-worktree/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
valgrind
,
bvnc
,
encfs
,
who
,
darkhttpd
.
git worktree
Manage multiple working trees attached to the same repository.
More information:
https://git-scm.com/docs/git-worktree
.
Create a new directory with the specified branch checked out into it:
git worktree add {{path/to/directory}} {{branch}}
Create a new directory with a new branch checked out into it:
git worktree add {{path/to/directory}} -b {{new_branch}}
List all the working directories attached to this repository:
git worktree list
Remove a worktree (after deleting worktree directory):
git worktree prune
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
