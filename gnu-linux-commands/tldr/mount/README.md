# mount

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mount/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
thunderbird
,
xcaddy
,
ufraw batch
.
mount
Provides access to an entire filesystem in one directory.
More information:
https://manned.org/mount.8
.
Show all mounted filesystems:
mount
Mount a device to a directory:
mount -t {{filesystem_type}} {{path/to/device_file}} {{path/to/target_directory}}
Mount a CD-ROM device (with the filetype ISO9660) to
/cdrom
(readonly):
mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}
Mount all the filesystem defined in
/etc/fstab
:
mount -a
Mount a specific filesystem described in
/etc/fstab
(e.g.
/dev/sda1 /my_drive ext2 defaults 0 2
):
mount {{/my_drive}}
Mount a directory to another directory:
mount --bind {{path/to/old_dir}} {{path/to/new_dir}}
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
