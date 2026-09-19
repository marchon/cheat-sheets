# git-summary

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-summary/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lerna
,
mysqldump
,
llvm cat
,
stdbuf
.
git summary
Display information about a Git repository.
Part of
git-extras
.
More information:
https://github.com/tj/git-extras/blob/master/Commands.md#git-summary
.
Display data about a Git repository:
git summary
Display data about a Git repository since a commit-ish:
git summary {{commit|branch_name|tag_name}}
Display data about a Git repository, merging committers using different emails into 1 statistic for each author:
git summary --dedup-by-email
Display data about a Git repository, showing the number of lines modified by each contributor:
git summary --line
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
