# virsh-pool-info

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-info/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gpg
,
plenv
,
vue serve
,
rc
,
hg
,
reflac
.
virsh pool-info
List information about a virtual machine storage pool.
See also:
virsh
.
More information:
https://manned.org/virsh
.
List the name, UUID, state, persistence type, autostart status, capacity, space allocated, and space available for the storage pool specified by name or UUID (determine using
virsh pool-list
):
virsh pool-info --pool {{name|uuid}}
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
