# cpio

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cpio/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
psql
,
influx
,
puppet apply
,
mp4box
.
cpio
Copies files in and out of archives.
Supports the following archive formats: cpio's custom binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, and POSIX.1 tar.
More information:
https://www.gnu.org/software/cpio
.
Take a list of file names from standard input and add them [o]nto an archive in cpio's binary format:
echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{archive.cpio}}
Copy all files and directories in a directory and add them [o]nto an archive, in [v]erbose mode:
find {{path/to/directory}} | cpio -ov > {{archive.cpio}}
P[i]ck all files from an archive, generating [d]irectories where needed, in [v]erbose mode:
cpio -idv < {{archive.cpio}}
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
