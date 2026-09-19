# sequelize

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sequelize/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phpcbf
,
ngs
,
envsubst
,
chgrp
,
glab
.
sequelize
Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server.
More information:
https://sequelize.org/
.
Create a model with 3 fields and a migration file:
sequelize model:generate --name {{table_name}} --attributes {{field1:integer,field2:string,field3:boolean}}
Run the migration file:
sequelize db:migrate
Revert all migrations:
sequelize db:migrate:undo:all
Create a seed file with the specified name to populate the database:
sequelize seed:generate --name {{seed_filename}}
Populate database using all seed files:
sequelize db:seed:all
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
