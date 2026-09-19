# ipaggcreate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ipaggcreate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
openttd
,
tlmgr gui
,
az tag
,
[[
.
ipaggcreate
Produce aggregate statistics of TCP/IP dumps.
More information:
https://manned.org/ipaggcreate
.
Count the number of packets sent from each source address appearing in a pcap file:
ipaggcreate --src {{path/to/file.pcap}}
Group and count packets read from a network interface by IP packet length:
ipaggcreate --interface {{eth0}} --length
Count the number of bytes sent between each address pair appearing in a pcap file:
ipaggcreate --address-pairs --bytes {{path/to/file.pcap}}
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
