# fmt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fmt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
adb install
,
ftp
,
az storage blob
.
fmt
Reformat a text file by joining its paragraphs and limiting the line width to given number of characters (75 by default).
More information:
https://www.gnu.org/software/coreutils/fmt
.
Reformat a file:
fmt {{path/to/file}}
Reformat a file producing output lines of (at most)
n
characters:
fmt -w {{n}} {{path/to/file}}
Reformat a file without joining lines shorter than the given width together:
fmt -s {{path/to/file}}
Reformat a file with uniform spacing (1 space between words and 2 spaces between paragraphs):
fmt -u {{path/to/file}}
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
