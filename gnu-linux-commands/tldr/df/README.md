# df

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/df/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xz
,
dig
,
git mergetool
,
bshell
.
df
Gives an overview of the filesystem disk space usage.
More information:
https://www.gnu.org/software/coreutils/df
.
Display all filesystems and their disk usage:
df
Display all filesystems and their disk usage in human-readable form:
df -h
Display the filesystem and its disk usage containing the given file or directory:
df {{path/to/file_or_directory}}
Display statistics on the number of free inodes:
df -i
Display filesystems but exclude the specified types:
df -x {{squashfs}} -x {{tmpfs}}
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
