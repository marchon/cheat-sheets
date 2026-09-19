# mongodump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mongodump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git check attr
,
pio debug
,
uniq
.
mongodump
Utility to export the contents of a MongoDB instance.
More information:
https://docs.mongodb.com/database-tools/mongodump/
.
Create a dump of all databases (this will place the files inside a directory called "dump"):
mongodump
Specify an output location for the dump:
mongodump --out {{path/to/directory}}
Create a dump of a given database:
mongodump --db {{database_name}}
Create a dump of a given collection within a given database:
mongodump --collection {{collection_name}} --db {{database_name}}
Connect to a given host running on a given port, and create a dump:
mongodump --host {{host}} --port {{port}}
Create a dump of a given database with a given username; user will be prompted for password:
mongodump --username {{username}} {{database}} --password
Create a dump from a specific instance; host, user, password and database will be defined in the connection string:
mongodump --uri {{connection_string}}
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
