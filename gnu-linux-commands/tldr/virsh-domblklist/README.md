# virsh-domblklist

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virsh-domblklist/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git range diff
,
tlmgr option
.
virsh-domblklist
List information about block devices associated with a virtual machine.
See also:
virsh
.
More information:
https://manned.org/virsh
.
List the target name and source path of the block devices:
virsh domblklist --domain {{vm_name}}
List the disk type and device value as well as the target name and source path:
virsh domblklist --domain {{vm_name}} --details
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
