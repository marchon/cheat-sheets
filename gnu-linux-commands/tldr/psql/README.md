# psql

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/psql/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue add
,
glances
,
xargs
,
aws iam
.
psql
PostgreSQL command-line client.
More information:
https://www.postgresql.org/docs/current/app-psql.html
.
Connect to the database. It connects to localhost using default port 5432 with default user as currently logged in user:
psql {{database}}
Connect to the database on given server host running on given port with given username, without a password prompt:
psql -h {{host}} -p {{port}} -U {{username}} {{database}}
Connect to the database; user will be prompted for password:
psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}
Execute a single SQL query or PostgreSQL command on the given database (useful in shell scripts):
psql -c '{{query}}' {{database}}
Execute commands from a file on the given database:
psql {{database}} -f {{file.sql}}
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
