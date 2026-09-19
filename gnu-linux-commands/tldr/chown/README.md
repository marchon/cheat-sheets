# chown

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/chown/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh pr
,
sudo
,
hive
,
fping
,
gmssl
,
ptpython
.
chown
Change user and group ownership of files and directories.
More information:
https://www.gnu.org/software/coreutils/chown
.
Change the owner user of a file/directory:
chown {{user}} {{path/to/file_or_directory}}
Change the owner user and group of a file/directory:
chown {{user}}:{{group}} {{path/to/file_or_directory}}
Recursively change the owner of a directory and its contents:
chown -R {{user}} {{path/to/directory}}
Change the owner of a symbolic link:
chown -h {{user}} {{path/to/symlink}}
Change the owner of a file/directory to match a reference file:
chown --reference={{path/to/reference_file}} {{path/to/file_or_directory}}
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
