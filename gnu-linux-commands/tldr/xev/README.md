# xev

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xev/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cd
,
ocamlopt
,
javac
,
xo
,
mysqld
,
mitmdump
.
xev
Print contents of X events.
More information:
https://gitlab.freedesktop.org/xorg/app/xev
.
Monitor all occurring X events:
xev
Monitor all X events of the root window instead of creating a new one:
xev -root
Monitor all X events of a particular window:
xev -id {{window_id}}
Monitor X events from a given category (can be specified multiple times):
xev -event {{event_category}}
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
