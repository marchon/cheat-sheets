# subfinder

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/subfinder/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az account
,
wc
,
sequelize
,
cmark
.
subfinder
A subdomain discovery tool that discovers valid subdomains for websites.
Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
More information:
https://github.com/subfinder/subfinder
.
Find subdomains for a specific domain:
subfinder -d {{example.com}}
Show only the subdomains found:
subfinder --silent -d {{example.com}}
Use a brute-force attack to find subdomains:
subfinder -d {{example.com}} -b
Remove wildcard subdomains:
subfinder -nW -d {{example.com}}
Use a given comma-separated list of resolvers:
subfinder -r {{8.8.8.8}},{{1.1.1.1}} -d {{example.com}}
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
