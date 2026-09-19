# git-annex

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-annex/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mmls
,
git rebase
,
pueue stash
.
git annex
Manage files with Git, without checking their contents in.
When a file is annexed, its content is moved into a key-value store, and a symlink is made that points to the content.
More information:
https://git-annex.branchable.com
.
Help:
git annex help
Initialize a repo with Git annex:
git annex init
Add a file:
git annex add {{path/to/file_or_directory}}
Show the current status of a file or directory:
git annex status {{path/to/file_or_directory}}
Synchronize a local repository with a remote:
git annex {{remote}}
Get a file or directory:
git annex get {{path/to/file_or_directory}}
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
