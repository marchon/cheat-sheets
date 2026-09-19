# git-commit-graph

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-commit-graph/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
stat
,
x_x
,
promtool
,
core validate commit
.
git commit-graph
Write and verify Git commit-graph files.
More information:
https://git-scm.com/docs/git-commit-graph
.
Write a commit-graph file for the packed commits in the repository's local
.git
directory:
git commit-graph write
Write a commit-graph file containing all reachable commits:
git show-ref --hash | git commit-graph write --stdin-commits
Write a commit-graph file containing all commits in the current commit-graph file along with those reachable from
HEAD
:
git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append
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
