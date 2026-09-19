# zpool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zpool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mkvmerge
,
cradle
,
sync
,
pkill
,
gh run
.
zpool
Manage ZFS pools.
More information:
https://manned.org/zpool
.
Show the configuration and status of all ZFS zpools:
zpool status
Check a ZFS pool for errors (verifies the checksum of EVERY block). Very CPU and disk intensive:
zpool scrub {{pool_name}}
List zpools available for import:
zpool import
Import a zpool:
zpool import {{pool_name}}
Export a zpool (unmount all filesystems):
zpool export {{pool_name}}
Show the history of all pool operations:
zpool history {{pool_name}}
Create a mirrored pool:
zpool create {{pool_name}} mirror {{disk1}} {{disk2}} mirror {{disk3}} {{disk4}}
Add a cache (L2ARC) device to a zpool:
zpool add {{pool_name}} cache {{cache_disk}}
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
