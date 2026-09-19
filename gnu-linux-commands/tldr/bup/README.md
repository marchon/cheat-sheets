# bup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ajson
,
exenv
,
git checkout index
.
bup
Backup system based on the Git packfile format, providing incremental saves and global deduplication.
More information:
https://github.com/bup/bup
.
Initialize a backup repository in the specified local directory:
bup -d {{path/to/repository}} init
Prepare a given directory before taking a backup:
bup -d {{path/to/repository}} index {{path/to/directory}}
Backup a directory to the repository:
bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/directory}}
Show the backup snapshots currently stored in the repository:
bup -d {{path/to/repository}} ls
Restore a specific backup snapshot to a target directory:
bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}
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
