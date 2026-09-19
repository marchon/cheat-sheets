# dwebp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dwebp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git cp
,
oc
,
opt
,
awk
,
git credential
.
dwebp
dwebp
decompresses WebP files into PNG, PAM, PPM or PGM images.
Animated WebP files are not supported.
More information:
https://developers.google.com/speed/webp/docs/dwebp/
.
Convert a
webp
file into a
png
file:
dwebp {{path/to/input.webp}} -o {{path/to/output.png}}
Convert a
webp
file into a specific filetype:
dwebp {{path/to/input.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{path/to/output}}
Convert a
webp
file, using multi-threading if possible:
dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -mt
Convert a
webp
file, but also crop and scale at the same time:
dwebp {{input.webp}} -o {{output.png}} -crop {{x_pos}} {{y_pos}} {{width}} {{height}} -scale {{width}} {{height}}
Convert a
webp
file and flip the output:
dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -flip
Convert a
webp
file and don't use in-loop filtering to speed up the decoding process:
dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -nofilter
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
