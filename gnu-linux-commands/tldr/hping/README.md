# hping

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hping/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kotlin
,
go test
,
scrcpy
,
git missing
.
hping
Command-line oriented TCP/IP packet assembler and analyzer.
Inspired by the
ping
command.
More information:
http://www.hping.org
.
Ping localhost over TCP:
hping3 {{localhost}}
Ping an IP address over TCP on a specific port:
hping3 -p {{80}} -S {{192.168.1.1}}
Ping an IP address over UDP on port 80:
hping3 --udp -p {{80}} -S {{192.168.1.1}}
Scan a set of TCP ports on a specific IP address:
hping3 --scan {{80,3000,9000}} -S {{192.168.1.1}}
Perform a charge test on port 80:
hping3 --flood -p {{80}} -S {{192.168.1.1}}
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
