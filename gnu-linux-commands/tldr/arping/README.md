# arping

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/arping/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dep
,
gh cs
,
git imerge
,
pdfjam
.
arping
Discover and probe hosts in a network using the ARP protocol.
Useful for MAC address discovery.
More information:
https://github.com/ThomasHabets/arping
.
Ping a host by ARP request packets:
arping {{host_ip}}
Ping a host on a specific interface:
arping -I {{interface}} {{host_ip}}
Ping a host and stop at the first reply:
arping -f {{host_ip}}
Ping a host a specific number of times:
arping -c {{count}} {{host_ip}}
Broadcast ARP request packets to update neighbours' ARP caches:
arping -U {{ip_to_broadcast}}
Detect duplicated IP addresses in the network by sending ARP requests with a 3 second timeout:
arping -D -w {{3}} {{ip_to_check}}
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
