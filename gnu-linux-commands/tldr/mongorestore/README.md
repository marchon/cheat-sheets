# mongorestore

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mongorestore/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kosmorro
,
plesk
,
git checkout
.
mongorestore
Utility to import a collection or database from a binary dump into a MongoDB instance.
More information:
https://docs.mongodb.com/database-tools/mongorestore/
.
Import a BSON data dump from a directory to a MongoDB database:
mongorestore --db {{database_name}} {{path/to/directory}}
Import a BSON data dump from a directory to a given database in a MongoDB server host, running at a given port, with user authentication (user will be prompted for password):
mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/directory}} --password
Import a collection from a BSON file to a MongoDB database:
mongorestore --db {{database_name}} {{path/to/file}}
Import a collection from a BSON file to a given database in a MongoDB server host, running at a given port, with user authentication (user will be prompted for password):
mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password
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
