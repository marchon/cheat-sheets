# deb-get

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/deb-get/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
caddy
,
atq
,
msbuild
,
meshlabserver
.
deb-get
apt-get
functionality for
.deb
packages published in third party repositories or via direct download.
Works with Linux distributions which use
apt-get
.
More information:
https://github.com/wimpysworld/deb-get
.
Update the list of available packages and versions:
sudo deb-get update
Search for a given package:
sudo deb-get search {{package}}
Show information about a package:
sudo deb-get show {{package}}
Install a package, or update it to the latest available version:
sudo deb-get install {{package}}
Remove a package (using
purge
instead also removes its configuration files):
sudo deb-get remove {{package}}
Upgrade all installed packages to their newest available versions:
sudo deb-get upgrade
List all available packages:
deb-get list
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
