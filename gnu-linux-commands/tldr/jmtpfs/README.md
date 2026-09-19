# jmtpfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jmtpfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git create branch
,
keepassxc cli
.
jmtpfs
FUSE-based filesystem for accessing MTP devices.
More information:
https://manned.org/jmtpfs
.
Mount an MTP device to a directory:
jmtpfs {{path/to/directory}}
Set mount options:
jmtpfs -o {{allow_other,auto_unmount}} {{path/to/directory}}
List available MTP devices:
jmtpfs --listDevices
If multiple devices are present, mount a specific device:
jmtpfs -device={{bus_id}},{{device_id}} {{path/to/directory}}
Unmount MTP device:
fusermount -u {{path/to/directory}}
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
