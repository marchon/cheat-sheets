# mogrify

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mogrify/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sdk
,
groff
,
jenv
,
bitcoin cli
,
transcode
.
mogrify
Perform operations on multiple images, such as resizing, cropping, flipping, and adding effects.
Changes are applied directly to the original file.
More information:
https://imagemagick.org/script/mogrify.php
.
Resize all JPEG images in the directory to 50% of their initial size:
mogrify -resize {{50%}} {{*.jpg}}
Resize all images starting with "DSC" to 800x600:
mogrify -resize {{800x600}} {{DSC*}}
Convert all PNGs in the directory to JPEG:
mogrify -format {{jpg}} {{*.png}}
Halve the saturation of all image files in the current directory:
mogrify -modulate {{100,50}} {{*}}
Double the brightness of all image files in the current directory:
mogrify -modulate {{200}} {{*}}
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
