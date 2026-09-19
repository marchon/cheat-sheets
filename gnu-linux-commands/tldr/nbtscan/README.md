# nbtscan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nbtscan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ufraw batch
,
git clear soft
.
nbtscan
Scan networks for NetBIOS name information.
More information:
https://github.com/resurrecting-open-source-projects/nbtscan
.
Scan a network for NetBIOS names:
nbtscan {{192.168.0.1/24}}
Scan a single IP address:
nbtscan {{192.168.0.1}}
Display verbose output:
nbtscan -v {{192.168.0.1/24}}
Display output in
/etc/hosts
format:
nbtscan -e {{192.168.0.1/24}}
Read IP addresses / networks to scan from a file:
nbtscan -f {{path/to/file.txt}}
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
