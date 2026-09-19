# git-revert

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-revert/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kubetail
,
hub
,
glib compile resources
.
git revert
Create new commits which reverse the effect of earlier ones.
More information:
https://git-scm.com/docs/git-revert
.
Revert the most recent commit:
git revert {{HEAD}}
Revert the 5th last commit:
git revert HEAD~{{4}}
Revert multiple commits:
git revert {{branch_name~5..branch_name~2}}
Don't create new commits, just change the working tree:
git revert -n {{0c01a9..9a1743}}
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
