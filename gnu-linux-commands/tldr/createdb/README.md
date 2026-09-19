# createdb

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/createdb/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
htpasswd
,
iotop
,
subliminal
,
ant
.
createdb
Create a PostgreSQL database.
More information:
https://www.postgresql.org/docs/current/app-createdb.html
.
Create a database owned by the current user:
createdb {{database_name}}
Create a database owned by a specific user with a description:
createdb --owner={{username}} {{database_name}} '{{description}}'
Create a database from a template:
createdb --template={{template_name}} {{database_name}}
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
