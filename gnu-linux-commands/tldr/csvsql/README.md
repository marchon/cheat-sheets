# csvsql

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csvsql/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rspec
,
aria2
,
xh
,
pg_ctl
,
pnpm
,
cargo doc
.
csvsql
Generate SQL statements for a CSV file or execute those statements directly on a database.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html
.
Generate a
CREATE TABLE
SQL statement for a CSV file:
csvsql {{path/to/data.csv}}
Import a CSV file into an SQL database:
csvsql --insert --db "{{mysql://user:password@host/database}}" {{data.csv}}
Run an SQL query on a CSV file:
csvsql --query "{{select * from 'data'}}" {{data.csv}}
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
