# virsh-pool-start

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-start/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cargo build
,
git instaweb
,
rip
.
virsh pool-start
Start a previously configured but inactive virtual machine storage pool.
See also:
virsh
,
virsh-pool-define-as
,
virsh-pool-destroy
.
More information:
https://manned.org/virsh
.
Start the storage pool specified by name or UUID (determine using
virsh pool-list
) and create the underlying storage system if it doesn't exist:
virsh pool-start --pool {{name|uuid}} --build
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
