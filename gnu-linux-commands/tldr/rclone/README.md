# rclone

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rclone/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
minisign
,
fnm
,
iex
,
pip
,
nbtscan
.
rclone
CLI program to copy/sync/move files and directories to and from many cloud services.
More information:
https://rclone.org
.
List contents of a directory on an rclone remote:
rclone lsf {{remote_name}}:{{path/to/directory}}
Copy file or directory from local source to remote destination:
rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/destination_directory}}
Copy file or directory from remote source to local destination:
rclone copy {{remote_name}}:{{path/to/source_file_or_directory}} {{path/to/destination_directory}}
Sync local source to remote destination, changing the destination only:
rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}
Move file or directory from local source to remote destination:
rclone move {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}
Delete remote file or directory (use
--dry-run
to test, remove it to actually delete):
rclone --dry-run delete {{remote_name}}:{{path/to/file_or_directory}}
Mount rclone remote (experimental):
rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}
Unmount rclone remote if CTRL-C fails (experimental):
fusermount -u {{path/to/mount_point}}
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
