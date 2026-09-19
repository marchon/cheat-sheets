# unzip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/unzip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jadx
,
p10k
,
pdftex
,
export
,
tlmgr check
.
unzip
Extract compressed files in a ZIP archive.
More information:
https://manned.org/unzip
.
Extract zip file(s) (for multiple files, separate file paths by spaces):
unzip {{file(s)}}
Extract zip files(s) to given path:
unzip {{compressed_file(s)}} -d {{path/to/put/extracted_file(s)}}
List the contents of a zip file without extracting:
unzip -l {{file.zip}}
Extract the contents of the file(s) to stdout alongside the extracted file names:
unzip -c {{file.zip}}
Extract a zip file created on Windows, containing files with non-ASCII (e.g. Chinese or Japanese characters) filenames:
unzip -O {{gbk}} {{file.zip}}
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
