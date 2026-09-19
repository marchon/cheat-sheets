# tailscale-file

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tailscale-file/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pygmentize
,
xml unescape
,
assimp
.
tailscale file
Send files across connected devices on a Tailscale network.
It currently does not support sending files to devices owned by other users even on the same Tailscale network.
More information:
https://tailscale.com/kb/1106/taildrop/
.
Send a file to a specific node:
sudo tailscale file cp {{path/to/file}} {{hostname|ip}}:
Store files that were sent to the current node into a specific directory:
sudo tailscale file get {{path/to/directory}}
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
