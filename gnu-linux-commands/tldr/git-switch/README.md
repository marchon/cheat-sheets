# git-switch

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-switch/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git status
,
nginx
,
docker system
.
git switch
Switch between Git branches. Requires Git version 2.23+.
See also
git checkout
.
More information:
https://git-scm.com/docs/git-switch
.
Switch to an existing branch:
git switch {{branch_name}}
Create a new branch and switch to it:
git switch --create {{branch_name}}
Create a new branch based on an existing commit and switch to it:
git switch --create {{branch_name}} {{commit}}
Switch to the previous branch:
git switch -
Switch to a branch and update all submodules to match:
git switch --recurse-submodules {{branch_name}}
Switch to a branch and automatically merge the current branch and any uncommitted changes into it:
git switch --merge {{branch_name}}
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
