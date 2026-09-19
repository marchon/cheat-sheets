# virt-sysprep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virt-sysprep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
piactl
,
carp
,
scala
,
less
,
pax
,
lmms
.
virt-sysprep
Reset, unconfigure, or customize a virtual machine image.
More information:
https://manned.org/virt-sysprep
.
List all supported operations (enabled operations are indicated with asterisks):
virt-sysprep --list-operations
Run all enabled operations but don't actually apply the changes:
virt-sysprep --domain {{vm_name}} --dry-run
Run only the specified operations:
virt-sysprep --domain {{vm_name}} --operations {{operation1,operation2,...}}
Generate a new
/etc/machine-id
file and enable customizations to be able to change the host name to avoid network conflicts:
virt-sysprep --domain {{vm_name}} --enable {{customizations}} --hostname {{host_name}} --operation {{machine-id}}
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
