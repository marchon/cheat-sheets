# git-commit-tree

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-commit-tree/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
route
,
vagrant
,
hg log
,
cradle
.
git commit-tree
Low level utility to create commit objects.
See also:
git commit
.
More information:
https://git-scm.com/docs/git-commit-tree
.
Create a commit object with the specified message:
git commit-tree {{tree}} -m "{{message}}"
Create a commit object reading the message from a file (use
-
for stdin):
git commit-tree {{tree}} -F {{path/to/file}}
Create a GPG-signed commit object:
git commit-tree {{tree}} -m "{{message}}" --gpg-sign
Create a commit object with the specified parent commit object:
git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}
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
