# tlmgr-backup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tlmgr-backup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
conda
,
highlight
,
p4
,
upx
,
eget
,
htpasswd
.
tlmgr backup
Manage backups of TeX Live packages.
The default backup location is saved in the
backupdir
setting, which can be obtained with
tlmgr option
.
More information:
https://www.tug.org/texlive/tlmgr.html
.
Make a backup of one or more packages:
tlmgr backup {{package1 package2 ...}}
Make a backup of all packages:
tlmgr backup --all
Make a backup to a specific directory:
tlmgr backup {{package}} --backupdir {{path/to/backup_directory}}
Remove a backup of one or more packages:
tlmgr backup clean {{package1 package2 ...}}
Remove all backups:
tlmgr backup clean --all
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
