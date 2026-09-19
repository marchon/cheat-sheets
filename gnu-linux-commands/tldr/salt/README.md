# salt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/salt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fdupes
,
openconnect
,
psysh
,
git rm
.
salt
Execute commands and assert state on remote salt minions.
More information:
https://docs.saltstack.com/ref/cli/salt.html
.
List connected minions:
salt '*' test.ping
Execute a highstate on all connected minions:
salt '*' state.highstate
Upgrade packages using the OS package manager (apt, yum, brew) on a subset of minions:
salt '*.example.com' pkg.upgrade
Execute an arbitrary command on a particular minion:
salt '{{minion_id}}' cmd.run "ls "
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
