# cradle-sql

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cradle-sql/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
circup
,
hyperfine
,
mongod
,
nginx
.
cradle sql
Manage Cradle SQL databases.
More information:
https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql
.
Rebuild the database schema:
cradle sql build
Rebuild the database schema for a specific package:
cradle sql build {{package_name}}
Empty the entire database:
cradle sql flush
Empty the database tables for a specific package:
cradle sql flush {{package_name}}
Populate the tables for all packages:
cradle sql populate
Populate the tables for a specific package:
cradle sql populate {{package_name}}
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
