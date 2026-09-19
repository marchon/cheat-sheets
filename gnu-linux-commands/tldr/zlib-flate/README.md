# zlib-flate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zlib-flate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dirs
,
glab auth
,
xmlto
,
git commit tree
.
zlib-flate
Raw zlib compression and decompression program.
Part of
qpdf
.
More information:
https://manned.org/zlib-flate
.
Compress a file:
zlib-flate -compress < {{path/to/input_file}} > {{path/to/compressed.zlib}}
Uncompress a file:
zlib-flate -uncompress < {{path/to/compressed.zlib}} > {{path/to/output_file}}
Compress a file with a specified compression level. 0=Fastest (Worst), 9=Slowest (Best):
zlib-flate -compress={{compression_level}} < {{path/to/input_file}} > {{path/to/compressed.zlib}}
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
