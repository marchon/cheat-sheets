# virsh-connect

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-connect/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kak
,
gist
,
mutt
,
ts
,
flake8
,
git alias
.
virsh-connect
Connect to a virtual machine hypervisor.
See also:
virsh
.
More information:
https://manned.org/virsh
.
Connect to the default hypervisor:
virsh connect
Connect as root to the local QEMU/KVM hypervisor:
virsh connect qemu:///system
Launch a new instance of the hypervisor and connect to it as the local user:
virsh connect qemu:///session
Connect as root to a remote hypervisor using ssh:
virsh connect qemu+ssh://{{user_name@host_name}}/system
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
