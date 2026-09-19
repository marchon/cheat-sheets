# zfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
z
,
play
,
git show tree
,
kubectl logs
.
zfs
Manage ZFS filesystems.
More information:
https://manned.org/zfs
.
List all available zfs filesystems:
zfs list
Create a new ZFS filesystem:
zfs create {{pool_name/filesystem_name}}
Delete a ZFS filesystem:
zfs destroy {{pool_name/filesystem_name}}
Create a Snapshot of a ZFS filesystem:
zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}
Enable compression on a filesystem:
zfs set compression=on {{pool_name/filesystem_name}}
Change mountpoint for a filesystem:
zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}
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
