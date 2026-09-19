# jpegoptim

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jpegoptim/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gunzip
,
tlmgr shell
,
git reflog
.
jpegoptim
Optimise JPEG images.
More information:
https://github.com/tjko/jpegoptim
.
Optimise a set of JPEG images, retaining all associated data:
jpegoptim {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}
Optimise JPEG images, stripping all non-essential data:
jpegoptim --strip-all {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}
Force the output images to be progressive:
jpegoptim --all-progressive {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}
Force the output images to have a fixed maximum filesize:
jpegoptim --size={{250k}} {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}
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
