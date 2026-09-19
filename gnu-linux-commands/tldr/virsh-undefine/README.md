# virsh-undefine

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-undefine/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ed
,
pueue switch
,
join
,
timeout
.
virsh-undefine
Delete a virtual machine.
More information:
https://manned.org/virsh
.
Delete only the virtual machine configuration file:
virsh undefine --domain {{vm_name}}
Delete the configuration file and all associated storage volumes:
virsh undefine --domain {{vm_name}} --remove-all-storage
Delete the configuration file and the specified storage volumes using the target name or the source name (as obtained from the
virsh domblklist
command):
virsh undefine --domain {{vm_name}} --storage {{sda,path/to/source}}
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
