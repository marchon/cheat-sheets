# mysql

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mysql/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kubectl describe
,
jetifier
.
mysql
The MySQL command-line tool.
More information:
https://www.mysql.com/
.
Connect to a database:
mysql {{database_name}}
Connect to a database, user will be prompted for a password:
mysql -u {{user}} --password {{database_name}}
Connect to a database on another host:
mysql -h {{database_host}} {{database_name}}
Connect to a database through a Unix socket:
mysql --socket {{path/to/socket.sock}}
Execute SQL statements in a script file (batch file):
mysql -e "source {{filename.sql}}" {{database_name}}
Restore a database from a backup created with
mysqldump
(user will be prompted for a password):
mysql --user {{user}} --password {{database_name}} < {{path/to/backup.sql}}
Restore all databases from a backup (user will be prompted for a password):
mysql --user {{user}} --password < {{path/to/backup.sql}}
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
