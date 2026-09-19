# zstd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zstd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
umask
,
pyflakes
,
handbrakecli
.
zstd
Compress or decompress files with Zstandard compression.
More information:
https://github.com/facebook/zstd
.
Compress a file into a new file with the
.zst
suffix:
zstd {{file}}
Decompress a file:
zstd -d {{file}}.zst
Decompress to stdout:
zstd -dc {{file}}.zst
Compress a file specifying the compression level, where 1=fastest, 19=slowest and 3=default:
zstd -{{level}} {{file}}
Unlock higher compression levels (up to 22) using more memory (both for compression and decompression):
zstd --ultra -{{level}} {{file}}
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
