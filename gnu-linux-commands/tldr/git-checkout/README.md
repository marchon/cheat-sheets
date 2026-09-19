# git-checkout

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-checkout/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
airmon ng
,
just
,
git sync
,
git replace
.
git checkout
Checkout a branch or paths to the working tree.
More information:
https://git-scm.com/docs/git-checkout
.
Create and switch to a new branch:
git checkout -b {{branch_name}}
Create and switch to a new branch based on a specific reference (branch, remote/branch, tag are examples of valid references):
git checkout -b {{branch_name}} {{reference}}
Switch to an existing local branch:
git checkout {{branch_name}}
Switch to the previously checked out branch:
git checkout -
Switch to an existing remote branch:
git checkout --track {{remote_name}}/{{branch_name}}
Discard all unstaged changes in the current directory (see
git reset
for more undo-like commands):
git checkout .
Discard unstaged changes to a given file:
git checkout {{filename}}
Replace a file in the current directory with the version of it committed in a given branch:
git checkout {{branch_name}} -- {{filename}}
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
