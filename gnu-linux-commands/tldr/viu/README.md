# viu

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/viu/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ack
,
virsh pool define as
,
just
.
viu
A small command-line application to view images from the terminal.
More information:
https://github.com/atanunq/viu
.
Render an image or animated GIF:
viu {{path/to/file}}
Render an image or GIF from the internet using
curl
:
curl -s {{https://example.com/image.png}} | viu -
Render an image with a transparent background:
viu -t {{path/to/file}}
Render an image with a specific width and height in pixels:
viu -w {{width}} -h {{height}} {{path/to/file}}
Render an image or GIF and display its file name:
viu -n {{path/to/file}}
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
