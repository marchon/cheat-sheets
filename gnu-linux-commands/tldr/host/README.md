# host

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/host/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
chars
,
quilt
,
mysqld
,
xxh
,
kubectl rollout
.
host
Lookup Domain Name Server.
More information:
https://manned.org/host
.
Lookup A, AAAA, and MX records of a domain:
host {{domain}}
Lookup a field (CNAME, TXT,...) of a domain:
host -t {{field}} {{domain}}
Reverse lookup an IP:
host {{ip_address}}
Specify an alternate DNS server to query:
host {{domain}} {{8.8.8.8}}
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
