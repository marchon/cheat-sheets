# mysqldump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mysqldump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
web ext
,
middleman
,
az storage
.
mysqldump
Backups MySQL databases.
See also
mysql
for restoring databases.
More information:
https://dev.mysql.com/doc/refman/en/mysqldump.html
.
Create a backup (user will be prompted for a password):
mysqldump --user {{user}} --password {{database_name}} --result-file={{path/to/file.sql}}
Backup a specific table redirecting the output to a file (user will be prompted for a password):
mysqldump --user {{user}} --password {{database_name}} {{table_name}} > {{path/to/file.sql}}
Backup all databases redirecting the output to a file (user will be prompted for a password):
mysqldump --user {{user}} --password --all-databases > {{path/to/file.sql}}
Backup all databases from a remote host, redirecting the output to a file (user will be prompted for a password):
mysqldump --host={(ip_or_hostname)} --user {{user}} --password --all-databases > ({path/to/file.sql}}
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
