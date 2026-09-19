# fls

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fls/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
waitress serve
,
clamdscan
,
rails db
.
fls
List files and directories in an image file or device.
More information:
https://wiki.sleuthkit.org/index.php?title=Fls
.
Build a recursive fls list over a device, output paths will start with C:
fls -r -m {{C:}} {{/dev/loop1p1}}
Analyze a single partition, providing the sector offset at which the filesystem starts in the image:
fls -r -m {{C:}} -o {{sector}} {{path/to/image_file}}
Analyze a single partition, providing the timezone of the original system:
fls -r -m {{C:}} -z {{timezone}} {{/dev/loop1p1}}
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
