# minetestserver

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/minetestserver/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dolt config
,
live server
,
drush
.
minetestserver
Multiplayer infinite-world block sandbox server.
See also
minetest
, the graphical client.
More information:
https://wiki.minetest.net/Setting_up_a_server
.
Start the server:
minetestserver
List available worlds:
minetestserver --world list
Specify the world name to load:
minetestserver --world {{world_name}}
List the available game IDs:
minetestserver --gameid list
Specify a game to use:
minetestserver --gameid {{game_id}}
Listen on a specific port:
minetestserver --port {{34567}}
Migrate to a different data backend:
minetestserver --migrate {{sqlite3|leveldb|redis}}
Start an interactive terminal after starting the server:
minetestserver --terminal
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
