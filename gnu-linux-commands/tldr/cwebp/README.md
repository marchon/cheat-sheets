# cwebp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cwebp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
unar
,
license
,
cd
,
sha512sum
,
astyle
.
cwebp
Compress an image file to a WebP file.
More information:
https://developers.google.com/speed/webp/docs/cwebp
.
Compress a WebP file with default settings (q = 75) to the [o]utput file:
cwebp {{path/to/image_file}} -o {{path/to/output.webp}}
Compress a WebP file with the best [q]uality and largest file size:
cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{100}}
Compress a WebP file with the worst [q]uality and smallest file size:
cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{0}}
Compress a WebP file and apply resize to image:
cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -resize {{width}} {{height}}
Compress a WebP file and drop alpha channel information:
cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -noalpha
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
