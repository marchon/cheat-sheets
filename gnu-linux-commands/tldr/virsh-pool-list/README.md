# virsh-pool-list

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-pool-list/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sccmap
,
test
,
borg
,
nm
,
git commit tree
.
virsh pool-list
List information about virtual machine storage pools.
See also:
virsh
,
virsh-pool-autostart
,
virsh-pool-define-as
.
More information:
https://manned.org/virsh
.
List the name, state, and whether autostart is enabled or disabled for active storage pools:
virsh pool-list
List information for active and inactive or just inactive storage pools:
virsh pool-list --{{all|inactive}}
List extended information about persistence, capacity, allocation, and available space for active storage pools:
virsh pool-list --details
List information for active storage pools with either autostart enabled or disabled:
virsh pool-list --{{autostart|no-autostart}}
List information for active storage pools that are either persistent or transient:
virsh pool-list --{{persistent|transient}}
List the name and UUID of active storage pools:
virsh pool-list --name --uuid
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
