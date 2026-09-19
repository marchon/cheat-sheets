# p7zip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/p7zip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nbtscan
,
sum
,
mutt
,
r
,
conan
,
task
.
p7zip
Wrapper of 7-Zip file archiver with high compression ratio.
Internally executes either 7za or 7zr command.
More information:
http://p7zip.sourceforge.net
.
Archive a file, replacing it with a 7zipped compressed version:
p7zip {{path/to/file}}
Archive a file keeping the input file:
p7zip -k {{path/to/file}}
Decompress a file, replacing it with the original uncompressed version:
p7zip -d {{compressed.ext}}.7z
Decompress a file keeping the input file:
p7zip -d -k {{compressed.ext}}.7z
Skip some checks and force compression or decompression:
p7zip -f {{path/to/file}}
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
