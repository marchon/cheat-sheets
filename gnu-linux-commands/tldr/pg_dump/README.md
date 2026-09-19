# pg_dump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pg_dump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab alias
,
llvm nm
,
meshlabserver
.
pg_dump
Extract a PostgreSQL database into a script file or other archive file.
More information:
https://www.postgresql.org/docs/current/app-pgdump.html
.
Dump database into an SQL-script file:
pg_dump {{db_name}} > {{output_file.sql}}
Same as above, customize username:
pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}
Same as above, customize host and port:
pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}
Dump a database into a custom-format archive file:
pg_dump -Fc {{db_name}} > {{output_file.dump}}
Dump only database data into an SQL-script file:
pg_dump -a {{db_name}} > {{path/to/output_file.sql}}
Dump only schema (data definitions) into an SQL-script file:
pg_dump -s {{db_name}} > {{path/to/output_file.sql}}
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
