# unrar

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/unrar/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xml transform
,
parallel lint
.
unrar
Extract RAR archives.
More information:
https://manned.org/unrar
.
Extract files with original directory structure:
unrar x {{compressed.rar}}
Extract files to a specified path with the original directory structure:
unrar x {{compressed.rar}} {{path/to/extract}}
Extract files into current directory, losing directory structure in the archive:
unrar e {{compressed.rar}}
Test integrity of each file inside the archive file:
unrar t {{compressed.rar}}
List files inside the archive file without decompressing it:
unrar l {{compressed.rar}}
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
