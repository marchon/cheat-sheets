# ect

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ect/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nokogiri
,
yarn
,
typeset
,
xsv
,
git notes
.
ect
Efficient Compression Tool.
File optimizer written in C++. It supports
.png
,
.jpg
,
.gzip
and
.zip
files.
More information:
https://github.com/fhanau/Efficient-Compression-Tool
.
Compress a file:
ect {{path/to/file.png}}
Compress a file with specified compression level and multithreading (1=Fastest (Worst), 9=Slowest (Best), default is 3):
ect -{{9}} --mt-deflate {{path/to/file.zip}}
Compress all files in a directory recursively:
ect -recurse {{path/to/directory}}
Compress a file, keeping the original modification time:
ect -keep {{path/to/file.png}}
Compress a file, stripping metadata:
ect -strip {{path/to/file.png}}
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
