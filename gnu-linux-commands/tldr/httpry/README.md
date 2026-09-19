# httpry

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/httpry/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
x11docker
,
qemu
,
kube fzf
,
xmllint
.
httpry
A lightweight packet sniffer for displaying and logging HTTP traffic.
It can be run in real-time displaying the traffic as it is parsed, or as a daemon process that logs to an output file.
More information:
http://dumpsterventures.com/jason/httpry/
.
Save output to a file:
httpry -o {{path/to/file.log}}
Listen on a specific interface and save output to a binary pcap format file:
httpry {{eth0}} -b {{path/to/file.pcap}}
Filter output by a comma-separated list of HTTP verbs:
httpry -m {{get|post|put|head|options|delete|trace|connect|patch}}
Read from an input capture file and filter by IP:
httpry -r {{path/to/file.log}} '{{host 192.168.5.25}}'
Run as daemon process:
httpry -d -o {{path/to/file.log}}
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
