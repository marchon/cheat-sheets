# guacd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/guacd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gacutil
,
gatsby
,
sslscan
,
exrex
.
guacd
Apache Guacamole proxy daemon.
Support loader for client plugins to interface between the Guacamole protocol and any arbitrary remote desktop protocol (e.g. RDP, VNC, Other).
More information:
https://guacamole.apache.org/
.
Bind to a specific port on localhost:
guacd -b {{127.0.0.1}} -l {{4823}}
Start in debug mode, keeping the process in the foreground:
guacd -f -L {{debug}}
Start with TLS support:
guacd -C {{my-cert.crt}} -K {{my-key.pem}}
Write the PID to a file:
guacd -p {{path/to/file.pid}}
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
