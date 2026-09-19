# bmaptool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bmaptool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phpcbf
,
tuir
,
pfetch
,
hg push
,
tb
.
bmaptool
Create or copy block maps intelligently (designed to be faster than
cp
or
dd
).
More information:
https://source.tizen.org/documentation/reference/bmaptool
.
Create a blockmap from image file:
bmaptool create -o {{blockmap.bmap}} {{source.img}}
Copy an image file into sdb:
bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}
Copy a compressed image file into sdb:
bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}
Copy an image file into sdb without using a blockmap:
bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}
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
