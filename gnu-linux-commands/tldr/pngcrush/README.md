# pngcrush

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pngcrush/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
csvsort
,
exercism
,
fuck
,
play
,
ohdear cli
.
pngcrush
PNG compression utility.
More information:
https://pmt.sourceforge.io/pngcrush
.
Compress a PNG file:
pngcrush {{in.png}} {{out.png}}
Compress all PNGs and output them to the specified directory:
pngcrush -d {{path/to/output}} *.png
Compress PNG file with all 114 available algorithms and pick the best result:
pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}
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
