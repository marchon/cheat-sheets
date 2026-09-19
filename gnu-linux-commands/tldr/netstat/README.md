# netstat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/netstat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fluxctl
,
git bundle
,
webpack
.
netstat
Displays network-related information such as open connections, open socket ports, etc.
More information:
https://man7.org/linux/man-pages/man8/netstat.8.html
.
List all ports:
netstat --all
List all listening ports:
netstat --listening
List listening TCP ports:
netstat --tcp
Display PID and program names:
netstat --program
List information continuously:
netstat --continuous
List routes and do not resolve IP addresses to hostnames:
netstat --route --numeric
List listening TCP and UDP ports (+ user and process if you're root):
netstat --listening --program --numeric --tcp --udp --extend
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
