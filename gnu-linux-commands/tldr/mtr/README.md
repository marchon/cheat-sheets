# mtr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mtr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh environment
,
tb
,
aws s3api
.
mtr
Matt's Traceroute: combined traceroute and ping tool.
More information:
https://bitwizard.nl/mtr
.
Traceroute to a host and continuously ping all intermediary hops:
mtr {{host}}
Disable IP address and host name mapping:
mtr -n {{host}}
Generate output after pinging each hop 10 times:
mtr -w {{host}}
Force IP IPv4 or IPV6:
mtr -4 {{host}}
Wait for a given time (in seconds) before sending another packet to the same hop:
mtr -i {{seconds}} {{host}}
Display the Autonomous System Number (ASN) for each hop:
mtr --aslookup {{hostname}}
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
