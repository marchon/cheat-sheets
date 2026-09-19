# git-grep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-grep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
chown
,
rip
,
git verify commit
.
git-grep
Find strings inside files anywhere in a repository's history.
Accepts a lot of the same flags as regular
grep
.
More information:
https://git-scm.com/docs/git-grep
.
Search for a string in tracked files:
git grep {{search_string}}
Search for a string in files matching a pattern in tracked files:
git grep {{search_string}} -- {{file_glob_pattern}}
Search for a string in tracked files, including submodules:
git grep --recurse-submodules {{search_string}}
Search for a string at a specific point in history:
git grep {{search_string}} {{HEAD~2}}
Search for a string across all branches:
git grep {{search_string}} $(git rev-list --all)
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
