# pngcheck

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pngcheck/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
elixir
,
handbrakecli
,
ect
,
starship
.
pngcheck
Print detailed information about and verify PNG, JNG, and MNG files.
More information:
http://www.libpng.org/pub/png/apps/pngcheck.html
.
Print a summary for an image (width, height, and color depth):
pngcheck {{image.png}}
Print information for an image with [c]olorized output:
pngcheck -c {{image.png}}
Print [v]erbose information for an image:
pngcheck -cvt {{image.png}}
Receive an image from stdin and display detailed information:
cat {{path/to/image.png}} | pngcheck -cvt
[s]earch for PNGs within a specific file and display information about them:
pngcheck -s {{image.png}}
Search for PNGs within another file and e[x]tract them:
pngcheck -x {{image.png}}
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
