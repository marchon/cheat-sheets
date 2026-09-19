# syncthing

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/syncthing/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git log
,
dumpcap
,
tesseract
,
pwgen
.
syncthing
Continuous bidirectional decentralised folder synchronisation tool.
More information:
https://docs.syncthing.net/
.
Start Syncthing:
syncthing
Start Syncthing without opening a web browser:
syncthing -no-browser
Print the device ID:
syncthing -device-id
Change the home directory:
syncthing -home={{path/to/directory}}
Force a full index exchange:
syncthing -reset-deltas
Change the address upon which the web interface listens:
syncthing -gui-address={{ip_address:port|path/to/socket.sock}}
Show filepaths to the files used by Syncthing:
syncthing -paths
Disable the Syncthing monitor process:
syncthing -no-restart
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
