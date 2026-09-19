# pg_ctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pg_ctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
stow
,
basename
,
jobs
,
convert
,
repren
.
pg_ctl
Utility for controlling a PostgreSQL server and database cluster.
More information:
https://www.postgresql.org/docs/current/app-pg-ctl.html
.
Initialize a new PostgreSQL database cluster:
pg_ctl -D {{data_directory}} init
Start a PostgreSQL server:
pg_ctl -D {{data_directory}} start
Stop a PostgreSQL server:
pg_ctl -D {{data_directory}} stop
Restart a PostgreSQL server:
pg_ctl -D {{data_directory}} restart
Reload the PostgreSQL server configuration:
pg_ctl -D {{data_directory}} reload
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
