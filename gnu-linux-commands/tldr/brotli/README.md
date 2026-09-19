# brotli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/brotli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
optipng
,
tlmgr install
,
encfs
.
brotli
Compress/uncompress files with Brotli compression.
More information:
https://github.com/google/brotli
.
Compress a file, creating a compressed version next to the file:
brotli {{file.ext}}
Decompress a file, creating an uncompressed version next to the file:
brotli -d {{file.ext}}.br
Compress a file specifying the output filename:
brotli {{file.ext}} -o {{compressed_file.ext.br}}
Decompress a Brotli file specifying the output filename:
brotli -d {{compressed_file.ext.br}} -o {{file.ext}}
Specify the compression level. 1=Fastest (Worst), 11=Slowest (Best):
brotli -q {{11}} {{file.ext}} -o {{compressed_file.ext.br}}
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
