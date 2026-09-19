# virsh-list

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-list/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
type
,
clj
,
core validate commit
.
virsh-list
List the ID, name, and state of virtual machines.
See also:
virsh
.
More information:
https://manned.org/virsh
.
List information about running virtual machines:
virsh list
List information about virtual machines regardless of state:
virsh list --all
List information about virtual machines with autostart either enabled or disabled:
virsh list --all --{{autostart|no-autostart}}
List information about virtual machines either with or without snapshots:
virsh list --all --{{with-snapshot|without-snapshot}}
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
