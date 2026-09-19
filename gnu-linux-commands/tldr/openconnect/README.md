# openconnect

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/openconnect/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tlmgr shell
,
git shortlog
,
p5
.
openconnect
A VPN client, for Cisco AnyConnect VPNs and others.
More information:
https://www.infradead.org/openconnect/manual.html
.
Connect to a server:
openconnect {{vpn.example.org}}
Connect to a server, forking into the background:
openconnect --background {{vpn.example.org}}
Terminate the connection that is running in the background:
killall -SIGINT openconnect
Connect to a server, reading options from a config file:
openconnect --config={{path/to/file}} {{vpn.example.org}}
Connect to a server and authenticate with a specific SSL client certificate:
openconnect --certificate={{path/to/file}} {{vpn.example.org}}
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
