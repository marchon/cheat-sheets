# x11docker

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/x11docker/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
secrethub
,
black
,
mplayer
,
godot
.
x11docker
Securely run GUI applications and desktop UIs in Docker containers.
See also
xephyr
.
More information:
https://github.com/mviereck/x11docker
.
Launch VLC in a container:
x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}
Launch Xfce in a window:
x11docker --desktop {{x11docker/xfce}}
Launch GNOME in a window:
x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}
Launch KDE Plasma in a window:
x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}
Display help:
x11docker --help
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
