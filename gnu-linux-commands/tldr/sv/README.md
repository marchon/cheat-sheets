# sv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
msmtp
,
git check ignore
,
gow
.
sv
Control a running runsv service.
More information:
https://manpages.ubuntu.com/manpages/latest/man8/sv.8.html
.
Start a service:
sudo sv up {{path/to/service}}
Stop a service:
sudo sv down {{path/to/service}}
Get service status:
sudo sv status {{path/to/service}}
Reload a service:
sudo sv reload {{path/to/service}}
Start a service, but only if it's not running and don't restart it if it stops:
sudo sv once {{path/to/service}}
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
