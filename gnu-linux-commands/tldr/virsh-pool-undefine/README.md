# virsh-pool-undefine

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-undefine/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
runsv
,
bup
,
pastel
,
docker slim
.
virsh pool-undefine
Delete the configuration file in
/etc/libvirt/storage
for a stopped virtual machine storage pool.
See also:
virsh
,
virsh-pool-destroy
.
More information:
https://manned.org/virsh
.
Delete the configuration for the storage pool specified name or UUID (determine using
virsh pool-list
):
virsh pool-undefine --pool {{name|uuid}}
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
