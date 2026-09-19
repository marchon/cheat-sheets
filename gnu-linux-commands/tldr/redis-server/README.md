# redis-server

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/redis-server/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
docker save
,
kdeconnect cli
.
redis-server
Persistent key-value database.
More information:
https://redis.io
.
Start Redis server, using the default port (6379), and write logs to stdout:
redis-server
Start Redis server, using the default port, as a background process:
redis-server --daemonize yes
Start Redis server, using the specified port, as a background process:
redis-server --port {{port}} --daemonize yes
Start Redis server with a custom configuration file:
redis-server {{path/to/redis.conf}}
Start Redis server with verbose logging:
redis-server --loglevel {{warning|notice|verbose|debug}}
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
