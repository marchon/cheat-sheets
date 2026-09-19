# lzop

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lzop/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
doas
,
pipenv
,
cradle elastic
.
lzop
Compress or decompress files with LZO compression.
More information:
https://www.lzop.org/
.
Compress a file into a new file with the
.lzo
suffix:
lzop {{file}}
Decompress a file:
lzop -d {{file}}.lzo
Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3):
lzop -{{level}} {{file}}
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
