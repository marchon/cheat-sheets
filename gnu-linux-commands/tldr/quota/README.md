# quota

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/quota/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wormhole
,
join
,
k8sec
,
hn
,
rmdir
.
quota
Display users' disk space usage and allocated limits.
More information:
https://manned.org/quota
.
Show disk quotas in human-readable units for the current user:
quota -s
Verbose output (also display quotas on filesystems where no storage is allocated):
quota -v
Quiet output (only display quotas on filesystems where usage is over quota):
quota -q
Print quotas for the groups of which the current user is a member:
quota -g
Show disk quotas for another user:
sudo quota -u {{username}}
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
