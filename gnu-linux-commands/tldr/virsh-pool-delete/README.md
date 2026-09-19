# virsh-pool-delete

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-delete/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tox
,
ffprobe
,
iconv
,
q
,
standard
.
virsh pool-delete
Delete the underlying storage system of an inactive virtual machine storage pool.
See also:
virsh
,
virsh-pool-destroy
,
virsh-pool-undefine
.
More information:
https://manned.org/virsh
.
Delete the underlying storage system for the storage pool specified by name or UUID (determine using
virsh pool-list
):
virsh pool-delete --pool {{name|uuid}}
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
