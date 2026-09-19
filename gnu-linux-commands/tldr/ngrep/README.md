# ngrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ngrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
acyclic
,
realpath
,
serverless
.
ngrep
Filter network traffic packets using regular expressions.
More information:
https://github.com/jpr5/ngrep
.
Capture traffic of all interfaces:
ngrep -d any
Capture traffic of a specific interface:
ngrep -d {{eth0}}
Capture traffic crossing port 22 of interface eth0:
ngrep -d {{eth0}} port {{22}}
Capture traffic from or to a host:
ngrep host {{www.example.com}}
Filter keyword 'User-Agent:' of interface eth0:
ngrep -d {{eth0}} '{{User-Agent:}}'
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
