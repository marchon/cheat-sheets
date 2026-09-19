# magick

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/magick/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh pool delete
,
docker exec
.
magick
Create, edit, compose, or convert bitmap images.
ImageMagick version 7+. See
convert
for versions 6 and below.
More information:
https://imagemagick.org/
.
Convert file type:
magick {{image.png}} {{image.jpg}}
Resize an image, making a new copy:
magick convert -resize {{100x100}} {{image.jpg}} {{image.jpg}}
Create a GIF using images:
magick {{*.jpg}} {{images.gif}}
Create checkerboard pattern:
magick -size {{640x480}} pattern:checkerboard {{checkerboard.png}}
Convert images to individual PDF pages:
magick {{*.jpg}} +adjoin {{page-%d.pdf}}
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
