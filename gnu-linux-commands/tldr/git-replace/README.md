# git-replace

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-replace/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git ignore io
,
go fix
,
pueue edit
.
git replace
Create, list, and delete refs to replace objects.
More information:
https://git-scm.com/docs/git-replace
.
Replace any commit with a different one, leaving other commits unchanged:
git replace {{object}} {{replacement}}
Delete existing replace refs for the given objects:
git replace --delete {{object}}
Edit an object’s content interactively:
git replace --edit {{object}}
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
