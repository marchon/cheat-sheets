# git-show

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-show/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pg_restore
,
bash
,
amass
,
docker system
.
git show
Show various types of Git objects (commits, tags, etc.).
More information:
https://git-scm.com/docs/git-show
.
Show information about the latest commit (hash, message, changes, and other metadata):
git show
Show information about a given commit:
git show {{commit}}
Show information about the commit associated with a given tag:
git show {{tag}}
Show information about the 3rd commit from the HEAD of a branch:
git show {{branch}}~{{3}}
Show a commit's message in a single line, suppressing the diff output:
git show --oneline -s {{commit}}
Show only statistics (added/removed characters) about the changed files:
git show --stat {{commit}}
Show only the list of added, renamed or deleted files:
git show --summary {{commit}}
Show the contents of a file as it was at a given revision (e.g. branch, tag or commit):
git show {{revision}}:{{path/to/file}}
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
