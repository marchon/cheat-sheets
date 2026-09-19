# hostess

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hostess/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zstd
,
psql
,
sdcv
,
chsh
,
kahlan
,
git brv
.
hostess
An idempotent command-line utility for managing the
/etc/hosts
file.
More information:
https://github.com/cbednarski/hostess
.
List domains, target IP addresses and on/off status:
hostess list
Add a domain pointing to your machine to your hosts file:
hostess add {{local.example.com}} {{127.0.0.1}}
Remove a domain from your hosts file:
hostess del {{local.example.com}}
Disable a domain (but don't remove it):
hostess off {{local.example.com}}
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
