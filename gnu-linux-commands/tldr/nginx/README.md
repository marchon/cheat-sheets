# nginx

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nginx/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tmuxinator
,
dokku
,
7zr
,
scheme
.
nginx
Nginx web server.
More information:
https://nginx.org/en/
.
Start server with the default config file:
nginx
Start server with a custom config file:
nginx -c {{config_file}}
Start server with a prefix for all relative paths in the config file:
nginx -c {{config_file}} -p {{prefix/for/relative/paths}}
Test the configuration without affecting the running server:
nginx -t
Reload the configuration by sending a signal with no downtime:
nginx -s reload
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
