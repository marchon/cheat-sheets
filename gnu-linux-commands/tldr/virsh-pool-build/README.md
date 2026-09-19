# virsh-pool-build

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-build/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hostess
,
duplicacy
,
7za
,
source
.
virsh pool-build
Build the underlying storage system for a virtual machine storage pool as defined in it's configuration file in
/etc/libvirt/storage
.
See also:
virsh
,
virsh-pool-define-as
,
virsh-pool-start
.
More information:
https://manned.org/virsh
.
Build the storage pool specified by name or UUID (determine using
virsh pool-list
):
virsh pool-build --pool {{name|uuid}}
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
