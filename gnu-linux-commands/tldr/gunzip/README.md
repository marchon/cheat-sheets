# gunzip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gunzip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh api
,
tee
,
git switch
,
stack
.
gunzip
Extract file(s) from a gzip (.gz) archive.
More information:
https://manned.org/gunzip
.
Extract a file from an archive, replacing the original file if it exists:
gunzip {{archive.tar.gz}}
Extract a file to a target destination:
gunzip --stdout {{archive.tar.gz}} > {{archive.tar}}
Extract a file and keep the archive file:
gunzip --keep {{archive.tar.gz}}
List the contents of a compressed file:
gunzip --list {{file.txt.gz}}
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
