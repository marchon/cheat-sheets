# xprop

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xprop/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zoxide
,
git whatchanged
,
svgcleaner
.
xprop
A tool for displaying window and font properties in an X server.
More information:
https://manned.org/xprop
.
Display the name of the root window:
xprop -root WM_NAME
Display the window manager hints for a window:
xprop -name "{{window_name}}" WM_HINTS
Display the point size of a font:
xprop -font "{{font_name}}" POINT_SIZE
Display all the properties of the window with the id 0x200007:
xprop -id {{0x200007}}
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
