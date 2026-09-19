# ping

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ping/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zellij
,
vzdump
,
warp cli
,
fdp
,
ar
.
ping
Send ICMP ECHO_REQUEST packets to network hosts.
More information:
https://manned.org/ping
.
Ping host:
ping {{host}}
Ping a host only a specific number of times:
ping -c {{count}} {{host}}
Ping host, specifying the interval in seconds between requests (default is 1 second):
ping -i {{seconds}} {{host}}
Ping host without trying to lookup symbolic names for addresses:
ping -n {{host}}
Ping host and ring the bell when a packet is received (if your terminal supports it):
ping -a {{host}}
Also display a message if no response was received:
ping -O {{host}}
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
