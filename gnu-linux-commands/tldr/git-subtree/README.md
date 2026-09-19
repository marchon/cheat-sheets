# git-subtree

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-subtree/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cvs
,
okular
,
ptpython3
,
uptime
.
git subtree
Tool to manage project dependencies as subprojects.
More information:
https://manpages.debian.org/testing/git-man/git-subtree.1.en.html
.
Add a Git repository as a subtree:
git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}
Update subtree repository to its latest commit:
git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}
Merge recent changes up to the latest subtree commit into the subtree:
git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{branch_name}}
Push commits to a subtree repository:
git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{branch_name}}
Extract a new project history from the history of a subtree:
git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}
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
