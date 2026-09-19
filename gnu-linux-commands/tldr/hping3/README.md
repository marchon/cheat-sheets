# hping3

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hping3/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fgrep
,
spark
,
ibmcloud
,
transmission cli
.
hping3
Advanced ping utility which supports protocols such TCP, UDP, and raw IP.
Best run with elevated priviledges.
More information:
https://github.com/antirez/hping
.
Ping a destination with 4 ICMP ping requests:
hping3 --icmp --count {{4}} {{ip_or_hostname}}
Scan TCP port 80, scanning from the specific local source port 5090:
hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_or_hostname}}
Traceroute using a TCP scan to a specific destination port:
hping3 --traceroute --verbose --syn --destport {{80}} {{ip_or_hostname}}
Perform a TCP ACK scan to check if a given host is alive:
hping3 --count {{2}} --verbose --destport {{80}} -A {{ip_or_hostname}}
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
