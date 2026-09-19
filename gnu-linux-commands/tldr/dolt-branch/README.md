# dolt-branch

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dolt-branch/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh undefine
,
bw
,
in toto run
.
dolt branch
Manage Dolt branches.
More information:
https://github.com/dolthub/dolt
.
List local branches (current branch is highlighted by
*
):
dolt branch
List all local and remote branches:
dolt branch --all
Create a new branch based on the current branch:
dolt branch {{branch_name}}
Create a new branch with the specified commit as the latest:
dolt branch {{branch_name}} {{commit}}
Rename a branch:
dolt branch --move {{branch_name1}} {{branch_name2}}
Duplicate a branch:
dolt branch --copy {{branch_name1}} {{branch_name2}}
Delete a branch:
dolt branch --delete {{branch_name}}
Display the name of the current branch:
dolt branch --show-current
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
