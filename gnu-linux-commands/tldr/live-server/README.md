# live-server

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/live-server/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ansible pull
,
ntl
,
stolonctl
.
live-server
A simple development HTTP server with live reload capability.
More information:
https://github.com/tapio/live-server
.
Serve an
index.html
file and reload on changes:
live-server
Specify a port (default is 8080) from which to serve a file:
live-server --port={{8081}}
Specify a given file to serve:
live-server --open={{about.html}}
Proxy all requests for ROUTE to URL:
live-server --proxy={{/}}:{{http:localhost:3000}}
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
