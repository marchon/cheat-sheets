# xz

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xz/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cloudflared
,
live server
,
poetry
.
xz
Compress or decompress .xz and .lzma files.
More information:
https://tukaani.org/xz/format.html
.
Compress a file to the xz file format:
xz {{file}}
Decompress a xz file:
xz -d {{file.xz}}
Compress a file to the LZMA file format:
xz --format={{lzma}} {{file}}
Decompress an LZMA file:
xz -d --format={{lzma}} {{file.lzma}}
Decompress a file and write to stdout:
xz -dc {{file.xz}}
Compress a file, but don't delete the original:
xz -k {{file}}
Compress a file using the fastest compression:
xz -0 {{file}}
Compress a file using the best compression:
xz -9 {{file}}
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
