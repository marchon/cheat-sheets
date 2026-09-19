# isisdl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/isisdl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
llvm nm
,
valgrind
,
shopt
,
hardhat
.
isisdl
A downloading utility for ISIS of TU-Berlin. Download all your files and videos from ISIS.
More information:
https://github.com/Emily3403/isisdl
.
Start the synchronization process:
isisdl
Limit the download rate to 20 MiB/s and download with 5 threads:
isisdl --download-rate {{20}} --max-num-threads {{5}}
Run the initialization configuration wizard:
isisdl --init
Run the additional configuration wizard:
isisdl --config
Initiate a full synchronization of the database and compute the checksum of every file:
isisdl --sync
Start ffmpeg to compress downloaded videos:
isisdl --compress
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
