# lz4

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lz4/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gdu
,
gifsicle
,
kubectx
,
dfc
,
micro
.
lz4
Compress or decompress .lz4 files.
More information:
https://github.com/lz4/lz4
.
Compress a file:
lz4 {{file}}
Decompress a file:
lz4 -d {{file.lz4}}
Decompress a file and write to stdout:
lz4 -dc {{file.lz4}}
Package and compress a directory and its contents:
tar cvf - {{path/to/directory}} | lz4 - {{dir.tar.lz4}}
Decompress and unpack a directory and its contents:
lz4 -d {{dir.tar.lz4}} | tar -xv
Compress a file using the best compression:
lz4 -9 {{file}}
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
