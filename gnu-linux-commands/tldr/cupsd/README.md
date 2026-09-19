# cupsd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cupsd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hexo
,
cotton
,
cmark
,
virsh pool info
.
cupsd
Server daemon for the CUPS print server.
More information:
https://www.cups.org/doc/man-cupsd.html
.
Start
cupsd
in the background, aka. as a daemon:
cupsd
Start
cupsd
on the [f]oreground:
cupsd -f
[l]aunch
cupsd
on-demand (commonly used by
launchd
or
systemd
):
cupsd -l
Start
cupsd
using the specified [
c
]
upsd.conf
configuration file:
cupsd -c {{path/to/cupsd.conf}}
Start
cupsd
using the specified
cups-file
[
s
]
.conf
configuration file:
cupsd -s {{path/to/cups-files.conf}}
[t]est the [
c
]
upsd.conf
configuration file for errors:
cupsd -t -c {{path/to/cupsd.conf}}
[t]est the
cups-file
[
s
]
.conf
configuration file for errors:
cupsd -t -s {{path/to/cups-files.conf}}
Display all available options:
cupsd -h
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
