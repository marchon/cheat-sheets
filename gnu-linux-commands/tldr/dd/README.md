# dd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
micro
,
sdiff
,
buzzphrase
,
cosign
.
dd
Convert and copy a file.
More information:
https://www.gnu.org/software/coreutils/dd
.
Make a bootable USB drive from an isohybrid file (such like
archlinux-xxx.iso
) and show the progress:
dd if={{file.iso}} of=/dev/{{usb_drive}} status=progress
Clone a drive to another drive with 4 MiB block, ignore error and show progress:
dd if=/dev/{{source_drive}} of=/dev/{{dest_drive}} bs=4M conv=noerror status=progress
Generate a file of 100 random bytes by using kernel random driver:
dd if=/dev/urandom of={{random_file}} bs=100 count=1
Benchmark the write performance of a disk:
dd if=/dev/zero of={{file_1GB}} bs=1024 count=1000000
Generate a system backup into an IMG file and show the progress:
dd if=/dev/{{drive_device}} of={{path/to/file.img}} status=progress
Restore a drive from an IMG file and show the progress:
dd if={{path/to/file.img}} of=/dev/{{drive_device}} status=progress
Check progress of an ongoing dd operation (Run this command from another shell):
kill -USR1 $(pgrep ^dd)
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
