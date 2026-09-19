# virsh-pool-define-as

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-define-as/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
slackcat
,
arp scan
,
erl
,
csvkit
.
virsh pool-define-as
Create a configuration file in
/etc/libvirt/storage
for a persistent virtual machine storage pool from the provided arguments.
See also:
virsh
,
virsh-pool-build
,
virsh-pool-start
.
More information:
https://manned.org/virsh
.
Create the configuration file for a storage pool called pool_name using
/var/vms
as the underlying storage system:
virsh pool-define-as --name {{pool_name}} --type {{dir}} --target {{/var/vms}}
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
