# shred

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/shred/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fc match
,
unison
,
bmaptool
,
graphml2gv
.
shred
Overwrite files to securely delete data.
More information:
https://www.gnu.org/software/coreutils/shred
.
Overwrite a file:
shred {{file}}
Overwrite a file, leaving zeroes instead of random data:
shred --zero {{file}}
Overwrite a file 25 times:
shred -n25 {{file}}
Overwrite a file and remove it:
shred --remove {{file}}
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
