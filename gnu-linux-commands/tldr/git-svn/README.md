# git-svn

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-svn/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
parallel lint
,
buku
,
psql
,
wasm2c
.
git svn
Bidirectional operation between a Subversion repository and Git.
More information:
https://git-scm.com/docs/git-svn
.
Clone an SVN repository:
git svn clone {{https://example.com/subversion_repo}} {{local_dir}}
Clone an SVN repository starting at a given revision number:
git svn clone -r{{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}
Update local clone from the remote SVN repository:
git svn rebase
Fetch updates from the remote SVN repository without changing the Git HEAD:
git svn fetch
Commit back to the SVN repository:
git svn dcommit
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
