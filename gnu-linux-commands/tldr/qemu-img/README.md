# qemu-img

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/qemu-img/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git bugreport
,
openttd
,
git filter repo
.
qemu-img
Tool for Quick Emulator Virtual HDD image creation and manipulation.
More information:
https://qemu.readthedocs.io/en/latest/tools/qemu-img.html
.
Create disk image with a specific size (in gigabytes):
qemu-img create {{image_name.img}} {{gigabytes}}G
Show information about a disk image:
qemu-img info {{image_name.img}}
Increase or decrease image size:
qemu-img resize {{image_name.img}} {{gigabytes}}G
Dump the allocation state of every sector of the specified disk image:
qemu-img map {{image_name.img}}
Convert a VMware .vmdk disk image to a KVM .qcow2 disk image:
qemu-img convert -f {{vmdk}} -O {{qcow2}} {{path/to/file/foo.vmdk}} {{path/to/file/foo.qcow2}}
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
