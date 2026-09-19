# masscan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/masscan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fg
,
acyclic
,
go mod
,
kompose
,
micro
.
Masscan
Network scanner for scanning as fast as possible.
Best run with elevated privileges. Nmap compatibility run
masscan --nmap
to find out more.
More information:
https://github.com/robertdavidgraham/masscan
.
Scan an IP or network subnet for port 80:
masscan {{ip_address|network_prefix}} --ports {{80}}
Scan a class B subnet for the top 100 ports at 100,000 packets per second:
masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}
Scan a class B subnet avoiding ranges from a specific exclude file:
masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{path/to/file}}
Scan the Internet for port 443:
masscan {{0.0.0.0/0}} --ports {{443}} --rate {{10000000}}
Scan the Internet for a specific port range and export to a file:
masscan {{0.0.0.0/0}} --ports {{0-65535}} -output-format {{binary|grepable|json|list|xml}} --output-filename {{path/to/file}}
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
