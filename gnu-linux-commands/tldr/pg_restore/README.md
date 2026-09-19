# pg_restore

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pg_restore/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wuzz
,
vala
,
speed test
,
theharvester
.
pg_restore
Restore a PostgreSQL database from an archive file created by pg_dump.
More information:
https://www.postgresql.org/docs/current/app-pgrestore.html
.
Restore an archive into an existing database:
pg_restore -d {{db_name}} {{archive_file.dump}}
Same as above, customize username:
pg_restore -U {{username}} -d {{db_name}} {{archive_file.dump}}
Same as above, customize host and port:
pg_restore -h {{host}} -p {{port}} -d {{db_name}} {{archive_file.dump}}
List database objects included in the archive:
pg_restore --list {{archive_file.dump}}
Clean database objects before creating them:
pg_restore --clean -d {{db_name}} {{archive_file.dump}}
Use multiple jobs to do the restoring:
pg_restore -j {{2}} -d {{db_name}} {{archive_file.dump}}
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
