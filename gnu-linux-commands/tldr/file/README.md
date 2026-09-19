# file

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/file/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git stripspace
,
cksum
,
whereis
.
file
Determine file type.
More information:
https://manned.org/file
.
Give a description of the type of the specified file. Works fine for files with no file extension:
file {{filename}}
Look inside a zipped file and determine the file type(s) inside:
file -z {{foo.zip}}
Allow file to work with special or device files:
file -s {{filename}}
Don't stop at first file type match; keep going until the end of the file:
file -k {{filename}}
Determine the mime encoding type of a file:
file -i {{filename}}
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
