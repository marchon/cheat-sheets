# typeorm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/typeorm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ipython
,
webstorm
,
mysql
,
firebase
.
typeorm
A JavaScript ORM that can run on Node.js, browser, Cordova, Ionic, React Native, NativeScript, and Electron platforms.
More information:
https://typeorm.io/
.
Generate a new initial TypeORM project structure:
typeorm init
Create an empty migration file:
typeorm migration:create --name {{migration_name}}
Create a migration file with the SQL statements to update the schema:
typeorm migration:generate --name {{migration_name}}
Run all pending migrations:
typeorm migration:run
Create a new entity file in a specific directory:
typeorm entity:create --name {{entity}} --dir {{path/to/directory}}
Display the SQL statements to be executed by
typeorm schema:sync
on the default connection:
typeorm schema:log
Execute a specific SQL statement on the default connection:
typeorm query {{sql_sentence}}
Display help for a subcommand:
typeorm {{subcommand}} --help
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
