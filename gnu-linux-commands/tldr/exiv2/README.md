# exiv2

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/exiv2/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hangups
,
cppclean
,
pdfunite
,
jp2a
.
exiv2
Image metadata manipulation tool.
More information:
https://www.exiv2.org/manpage.html
.
Print a summary of the image Exif metadata:
exiv2 {{path/to/file}}
Print all metadata (Exif, IPTC, XMP) with interpreted values:
exiv2 -P kt {{path/to/file}}
Print all metadata with raw values:
exiv2 -P kv {{path/to/file}}
Delete all metadata from an image:
exiv2 -d a {{path/to/file}}
Delete all metadata, preserving the file timestamp:
exiv2 -d a -k {{path/to/file}}
Rename the file, prepending the date and time from metadata (not from the file timestamp):
exiv2 -r {{'%Y%m%d_%H%M%S_:basename:'}} {{path/to/file}}
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
