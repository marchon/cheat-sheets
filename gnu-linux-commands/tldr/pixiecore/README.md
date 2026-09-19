# pixiecore

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pixiecore/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git commit graph
,
complete
.
pixiecore
Tool to manage the network booting of machines.
More information:
https://github.com/danderson/netboot/tree/master/pixiecore
.
Start a PXE boot server which provides a
netboot.xyz
boot image:
pixiecore {{quick}} xyz --dhcp-no-bind
Start a new PXE boot server which provides an Ubuntu boot image:
pixiecore {{quick}} ubuntu --dhcp-no-bind
Get a list of all available boot images for quick mode:
pixiecore quick --help
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
