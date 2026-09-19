# git-rev-list

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-rev-list/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
prosodyctl
,
git locked
,
rcat
.
git rev-list
List revisions (commits) in reverse chronological order.
More information:
https://git-scm.com/docs/git-rev-list
.
List all commits on the current branch:
git rev-list {{HEAD}}
Print the latest commit that changed (add/edit/remove) a specific file on the current branch:
git rev-list -n 1 HEAD -- {{path/to/file}}
List commits more recent than a specific date, on a specific branch:
git rev-list --since={{'2019-12-01 00:00:00'}} {{branch_name}}
List all merge commits on a specific commit:
git rev-list --merges {{commit}}
Print the number of commits since a specific tag:
git rev-list {{tag_name}}..HEAD --count
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
