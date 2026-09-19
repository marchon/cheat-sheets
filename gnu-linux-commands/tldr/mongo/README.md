# mongo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mongo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
atrm
,
fdroidcl
,
cargo build
,
mtr
.
mongo
MongoDB interactive shell client.
More information:
https://docs.mongodb.com/manual/reference/program/mongo
.
Connect to a database:
mongo {{database}}
Connect to a database running on a given host on a given port:
mongo --host {{host}} --port {{port}} {{database}}
Connect to a database with a given username; user will be prompted for password:
mongo --username {{username}} {{database}} --password
Evaluate a JavaScript expression on the database:
mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{database}}
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
