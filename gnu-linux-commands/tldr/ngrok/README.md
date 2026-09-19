# ngrok

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ngrok/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
more
,
sponge
,
calendar
,
diffstat
.
ngrok
Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service.
More information:
https://ngrok.com
.
Expose a local HTTP service on a given port:
ngrok http {{80}}
Expose a local HTTP service on a specific host:
ngrok http {{foo.dev}}:{{80}}
Expose a local HTTPS server:
ngrok http https://localhost
Expose TCP traffic on a given port:
ngrok tcp {{22}}
Expose TLS traffic for a specific host and port:
ngrok tls -hostname={{foo.com}} {{443}}
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
