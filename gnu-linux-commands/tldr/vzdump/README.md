# vzdump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vzdump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aria2
,
pdfjoin
,
ibmcloud
,
bzip2
.
vzdump
Backup Utility for virtual machines and containers.
More information:
https://pve.proxmox.com/pve-docs/vzdump.1.html
.
Dump a guest virtual machine into the default dump directory (usually
/var/lib/vz/dump/
), excluding snapshots:
vzdump {{vm_id}}
Back up the guest virtual machines with the IDs 101, 102, and 103:
vzdump {{101 102 103}}
Dump a guest virtual machine using a specific mode:
vzdump {{vm_id}} --mode {{suspend|snapshot}}
Back up all guest systems and send an notification email to the root and admin users:
vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}
Use snapshot mode (no downtime required) and a non-default dump directory:
vzdump {{vm_id}} --dumpdir {{path/to/directory}} --mode {{snapshot}}
Back up all guest virtual machines excluding the IDs 101 and 102:
vzdump --mode {{suspend}} --exclude {{101, 102}}
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
