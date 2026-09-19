# cloudflared

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cloudflared/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
is up
,
jwt
,
ledger
,
helm install
.
cloudflared
Command-line tool to create a persistent connection to the Cloudflare network.
More information:
https://developers.cloudflare.com/argo-tunnel/
.
Authenticate and associate the connection to a domain in the Cloudflare account:
cloudflared tunnel login
Establish a tunnel to a host in Cloudflare from the local server:
cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}}
Establish a tunnel to a host in Cloudflare from the local server, without verifying the local server's certificate:
cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}} --no-tls-verify
Save logs to a file:
cloudflared tunnel --hostname {{hostname}} http://localhost:{{port_number}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}}
Install cloudflared as a system service:
cloudflared service install
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
