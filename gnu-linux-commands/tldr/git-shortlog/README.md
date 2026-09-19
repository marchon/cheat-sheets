# git-shortlog

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-shortlog/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gvcolor
,
pylint
,
zcat
,
ld
,
pest
,
stdbuf
.
git shortlog
Summarizes the
git log
output.
More information:
https://git-scm.com/docs/git-shortlog
.
View a summary of all the commits made, grouped alphabetically by author name:
git shortlog
View a summary of all the commits made, sorted by the number of commits made:
git shortlog -n
View a summary of all the commits made, grouped by the committer identities (name and email):
git shortlog -c
View a summary of the last 5 commits (i.e. specify a revision range):
git shortlog HEAD~{{5}}..HEAD
View all users, emails and the number of commits in the current branch:
git shortlog -sne
View all users, emails and the number of commits in all branches:
git shortlog -sne --all
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
