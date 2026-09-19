# xephyr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xephyr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fc
,
electron packager
,
lsd
,
slimrb
.
Xephyr
A nested X server that runs as an X application.
More information:
https://manned.org/xserver-xephyr
.
Create a black window with display ID ":2":
Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}
Start an X application on the new screen:
DISPLAY=:2 {{command_name}}
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
