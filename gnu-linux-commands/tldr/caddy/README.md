# caddy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/caddy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kubens
,
joe
,
meteor
,
complete
,
aws vault
.
caddy
A powerful, enterprise-ready, open source web server with automatic HTTPS, written in Go.
More information:
https://caddyserver.com
.
Start Caddy in the foreground:
caddy run
Start Caddy with the specified Caddyfile:
caddy run --config {{path/to/Caddyfile}}
Start Caddy in the background:
caddy start
Stop a background Caddy process:
caddy stop
Run a simple file server on the specified port with a browsable interface:
caddy file-server --listen :{{8000}} --browse
Run a reverse proxy server:
caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}
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
