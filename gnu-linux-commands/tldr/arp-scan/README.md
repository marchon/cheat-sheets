# arp-scan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/arp-scan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arch
,
az appconfig
,
pio platform
.
arp-scan
Send ARP packets to hosts (specified as IP addresses or hostnames) to scan the local network.
More information:
https://github.com/royhills/arp-scan
.
Scan the current local network:
arp-scan --localnet
Scan an IP network with a custom bitmask:
arp-scan {{192.168.1.1}}/{{24}}
Scan an IP network within a custom range:
arp-scan {{127.0.0.0}}-{{127.0.0.31}}
Scan an IP network with a custom net mask:
arp-scan {{10.0.0.0}}:{{255.255.255.0}}
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
