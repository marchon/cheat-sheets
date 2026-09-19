# traceroute

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/traceroute/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xephyr
,
kustomize
,
enscript
,
patchwork
.
traceroute
Print the route packets trace to network host.
More information:
https://manned.org/traceroute
.
Traceroute to a host:
traceroute {{host}}
Disable IP address and host name mapping:
traceroute -n {{host}}
Specify wait time for response:
traceroute -w {{0.5}} {{host}}
Specify number of queries per hop:
traceroute -q {{5}} {{host}}
Specify size in bytes of probing packet:
traceroute {{host}} {{42}}
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
