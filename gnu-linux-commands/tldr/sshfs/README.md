# sshfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sshfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dart
,
dotnet restore
,
hexo
,
dolt blame
.
sshfs
Filesystem client based on SSH.
More information:
https://github.com/libfuse/sshfs
.
Mount remote directory:
sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}
Unmount remote directory:
umount {{mountpoint}}
Mount remote directory from server with specific port:
sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}
Use compression:
sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C
Follow symbolic links:
sshfs -o follow_symlinks {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}
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
