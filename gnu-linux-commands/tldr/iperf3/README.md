# iperf3

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/iperf3/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hello
,
plesk
,
phpenv
,
git commits since
.
iperf3
Traffic generator for testing network bandwidth.
More information:
https://iperf.fr
.
Run iperf3 as a server:
iperf3 -s
Run an iperf3 server on a specific port:
iperf3 -s -p {{port}}
Start bandwidth test:
iperf3 -c {{server}}
Run iperf3 in multiple parallel streams:
iperf3 -c {{server}} -P {{streams}}
Reverse direction of the test. Server sends data to the client:
iperf3 -c {{server}} -R
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
