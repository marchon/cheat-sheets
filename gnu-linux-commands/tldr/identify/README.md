# identify

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/identify/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
consul
,
tldrl
,
transfersh
,
pwsh
.
identify
Command-line utility of Image Magick project to describe the format and characteristics of one or more image files.
More information:
https://imagemagick.org/script/identify.php
.
Describe the format and basic characteristics of an image:
identify {{path/to/image}}
Describe the format and verbose characteristics of an image:
identify -verbose {{path/to/image}}
Collect dimensions of all JPEG files under current directory:
identify -format "%f,%w,%h\n" *.{{jpg}} > {{path/to/filelist.csv}}
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
