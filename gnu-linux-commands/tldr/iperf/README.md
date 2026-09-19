# iperf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/iperf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cmatrix
,
youtube viewer
,
git rev parse
.
iperf
Measure network bandwidth between computers.
More information:
https://iperf.fr
.
Run on server:
iperf -s
Run on server using UDP mode and set server port to listen on 5001:
iperf -u -s -p {{5001}}
Run on client:
iperf -c {{server_address}}
Run on client every 2 seconds:
iperf -c {{server_address}} -i {{2}}
Run on client with 5 parallel threads:
iperf -c {{server_address}} -P {{5}}
Run on client using UDP mode:
iperf -u -c {{server_address}} -p {{5001}}
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
