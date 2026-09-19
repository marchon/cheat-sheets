# arp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/arp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git clear
,
man
,
mcs
,
obs
,
docker build
.
arp
Show and manipulate your system's ARP cache.
More information:
https://manned.org/arp
.
Show the current ARP table:
arp -a
Clear the entire cache:
sudo arp -a -d
Delete a specific entry:
arp -d {{address}}
Create an entry in the ARP table:
arp -s {{address}} {{mac_address}}
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
