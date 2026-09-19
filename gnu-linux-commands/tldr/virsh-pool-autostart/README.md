# virsh-pool-autostart

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-autostart/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
umount
,
xml
,
lumen
,
zm
,
googler
,
tlmgr shell
.
virsh pool-autostart
Enable or disable autostart for a virtual machine storage pool.
See also:
virsh
.
More information:
https://manned.org/virsh
.
Enable autostart for the storage pool specified by name or UUID (determine using
virsh pool-list
):
virsh pool-autostart --pool {{name|uuid}}
Disable autostart for the storage pool specified by name or UUID:
virsh pool-autostart --pool {{name|uuid}} --disable
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
