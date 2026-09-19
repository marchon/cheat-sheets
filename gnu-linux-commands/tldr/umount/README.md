# umount

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/umount/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
streamlink
,
task
,
inkview
,
guile
.
umount
Unlink a filesystem from its mount point, making it no longer accessible.
A filesystem cannot be unmounted when it is busy.
More information:
https://manned.org/umount.8
.
Unmount a filesystem, by passing the path to the source it is mounted from:
umount {{path/to/device_file}}
Unmount a filesystem, by passing the path to the target where it is mounted:
umount {{path/to/mounted_directory}}
Unmount all mounted filesystems (except the
proc
filesystem):
umount -a
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
