# salt-call

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/salt-call/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tex
,
kubectx
,
bq
,
scp
,
hadolint
,
tsort
.
salt-call
Invoke salt locally on a salt minion.
More information:
https://docs.saltstack.com/ref/cli/salt-call.html
.
Perform a highstate on this minion:
salt-call state.highstate
Perform a highstate dry-run, compute all changes but don't actually perform them:
salt-call state.highstate test=true
Perform a highstate with verbose debugging output:
salt-call -l debug state.highstate
List this minion's grains:
salt-call grains.items
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
