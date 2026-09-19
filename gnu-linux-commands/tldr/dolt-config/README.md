# dolt-config

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dolt-config/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
minetest
,
jhipster
,
at
,
gradle
.
dolt config
Read and write local (per repository) and global (per user) Dolt configuration variables.
More information:
https://docs.dolthub.com/interfaces/cli#dolt-config
.
List all local and global configuration options and their values:
dolt config --list
Display the value of a local or global configuration variable:
dolt config --get {{name}}
Modify the value of a local configuration variable, creating it if it doesn't exist:
dolt config --add {{name}} {{value}}
Modify the value of a global configuration variable, creating it if it doesn't exist:
dolt config --global --add {{name}} {{value}}
Delete a local configuration variable:
dolt config --unset {{name}}
Delete a global configuration variable:
dolt config --global --unset {{name}}
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
