# pvecm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pvecm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go fix
,
apg
,
httpflow
,
qrencode
.
pvecm
Proxmox VE Cluster Manager.
More information:
https://pve.proxmox.com/pve-docs/pvecm.1.html
.
Add the current node to an existing cluster:
pvecm add {{hostname_or_ip}}
Add a node to the cluster configuration (internal use):
pvecm addnode {{node}}
Return the version of the cluster join API available on this node:
pvecm apiver
Generate new cluster configuration:
pvecm create {{clustername}}
Remove a node from the cluster configuration:
pvecm delnode {{node}}
Display the local view of the cluster nodes:
pvecm nodes
Display the local view of the cluster status:
pvecm status
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
