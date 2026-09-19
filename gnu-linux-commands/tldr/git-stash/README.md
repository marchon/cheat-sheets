# git-stash

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-stash/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
while
,
tabula
,
xprop
,
alias
,
dc
,
deluged
.
git stash
Stash local Git changes in a temporary area.
More information:
https://git-scm.com/docs/git-stash
.
Stash current changes, except new (untracked) files:
git stash [push -m {{optional_stash_message}}]
Stash current changes, including new (untracked) files:
git stash -u
Interactively select parts of changed files for stashing:
git stash -p
List all stashes (shows stash name, related branch and message):
git stash list
Apply a stash (default is the latest, named stash@{0}):
git stash apply {{optional_stash_name_or_commit}}
Apply a stash (default is stash@{0}), and remove it from the stash list if applying doesn't cause conflicts:
git stash pop {{optional_stash_name}}
Drop a stash (default is stash@{0}):
git stash drop {{optional_stash_name}}
Drop all stashes:
git stash clear
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
