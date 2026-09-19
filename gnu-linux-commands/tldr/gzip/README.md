# gzip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gzip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go env
,
git reflog
,
btm
,
nmap
,
deno
.
gzip
Compress/uncompress files with gzip compression (LZ77).
More information:
https://www.gnu.org/software/gzip/manual/gzip.html
.
Compress a file, replacing it with a gzipped compressed version:
gzip {{file.ext}}
Decompress a file, replacing it with the original uncompressed version:
gzip -d {{file.ext}}.gz
Compress a file, keeping the original file:
gzip --keep {{file.ext}}
Compress a file specifying the output filename:
gzip -c {{file.ext}} > {{compressed_file.ext.gz}}
Decompress a gzipped file specifying the output filename:
gzip -c -d {{file.ext}}.gz > {{uncompressed_file.ext}}
Specify the compression level. 1=Fastest (Worst), 9=Slowest (Best), Default level is 6:
gzip -9 -c {{file.ext}} > {{compressed_file.ext.gz}}
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
