# import

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/import/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git archive
,
hg serve
,
llvm gcc
.
import
Capture some or all of an X server screen, and save the image to a file.
Part of the ImageMagick library.
More information:
https://imagemagick.org/script/import.php
.
Capture the entire X server screen in the PostScript image format:
import -window root {{output.postscript}}
Capture contents of a remote X server screen in the PNG format:
import -window root -display {{remote_host}}:{{screen}}.{{display}} {{output.png}}
Capture a specific window, given its ID as displayed by
xwininfo
, into the JPEG format:
import -window {{window_id}} {{output.jpg}}
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
