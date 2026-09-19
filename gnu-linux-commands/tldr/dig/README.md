# dig

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dig/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
transfersh
,
pdfjam
,
git verify commit
.
dig
DNS lookup utility.
More information:
https://manned.org/dig
.
Lookup the IP(s) associated with a hostname (A records):
dig +short {{example.com}}
Get a detailed answer for a given domain (A records):
dig +noall +answer {{example.com}}
Query a specific DNS record type associated with a given domain name:
dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}
Get all types of records for a given domain name:
dig {{example.com}} ANY
Specify an alternate DNS server to query:
dig @{{8.8.8.8}} {{example.com}}
Perform a reverse DNS lookup on an IP address (PTR record):
dig -x {{8.8.8.8}}
Find authoritative name servers for the zone and display SOA records:
dig +nssearch {{example.com}}
Perform iterative queries and display the entire trace path to resolve a domain name:
dig +trace {{example.com}}
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
