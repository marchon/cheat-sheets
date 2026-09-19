# duplicacy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/duplicacy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xargs
,
wapm
,
pg_dumpall
,
f3fix
.
duplicacy
A lock-free deduplication cloud backup tool.
More information:
https://github.com/gilbertchen/duplicacy/wiki
.
Use current directory as the repository, initialize a SFTP storage and encrypt the storage with a password:
duplicacy init -e {{snapshot_id}} {{sftp://user@192.168.2.100/path/to/storage/}}
Save a snapshot of the repository to the default storage:
duplicacy backup
List snapshots of current repository:
duplicacy list
Restore the repository to a previously saved snapshot:
duplicacy restore -r {{revision}}
Check the integrity of snapshots:
duplicacy check
Add another storage to be used for the existing repository:
duplicacy add {{storage_name}} {{snapshot_id}} {{storage_url}}
Prune a specific revision of snapshot:
duplicacy prune -r {{revision}}
Prune revisions, keeping one revision every
n
days for all revisions older than
m
days:
duplicacy prune -keep {{n:m}}
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
