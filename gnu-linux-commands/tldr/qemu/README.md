# qemu

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/qemu/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gxl2gv
,
kubectl describe
,
cdk
.
qemu
Generic machine emulator and virtualizer.
Supports a large variety of CPU architectures.
More information:
https://www.qemu.org
.
Boot from image emulating i386 architecture:
qemu-system-i386 -hda {{image_name.img}}
Boot from image emulating x64 architecture:
qemu-system-x86_64 -hda {{image_name.img}}
Boot QEMU instance with a live ISO image:
qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d
Specify amount of RAM for instance:
qemu-system-i386 -m 256 -hda image_name.img -cdrom os-image.iso -boot d
Boot from physical device (e.g. from USB to test bootable medium):
qemu-system-i386 -hda /dev/{{storage_device}}
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
