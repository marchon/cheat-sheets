# git-maintenance

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-maintenance/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
install
,
edgepaint
,
nf core
,
ionic
.
git-maintenance
Run tasks to optimize Git repository data.
More information:
https://git-scm.com/docs/git-maintenance
.
Register the current repository in the user's list of repositories to daily have maintenance run:
git maintenance register
Start running maintenance on the current repository:
git maintenance start
Halt the background maintenance schedule for the current repository:
git maintenance stop
Remove the current repository from the user's maintenance repository list:
git maintenance unregister
Run a specific maintenance task on the current repository:
git maintenance run --task={{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}
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
