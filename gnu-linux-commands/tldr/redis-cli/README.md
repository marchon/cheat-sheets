# redis-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/redis-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws cur
,
ngs
,
runsvchdir
,
pueue stash
.
redis-cli
Opens a connection to a Redis server.
More information:
https://redis.io/topics/rediscli
.
Connect to the local server:
redis-cli
Connect to a remote server on the default port (6379):
redis-cli -h {{host}}
Connect to a remote server specifying a port number:
redis-cli -h {{host}} -p {{port}}
Connect to a remote server specifying a URI:
redis-cli -u {{uri}}
Specify a password:
redis-cli -a {{password}}
Execute Redis command:
redis-cli {{redis_command}}
Connect to the local cluster:
redis-cli -c
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
