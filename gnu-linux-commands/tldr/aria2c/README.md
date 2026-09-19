# aria2c

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aria2c/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cups config
,
where
,
hg clone
.
aria2c
Fast download utility.
Supports HTTP(S), FTP, SFTP, BitTorrent, and Metalink.
More information:
https://aria2.github.io
.
Download a URI to a file:
aria2c {{url}}
Download the file pointed to by the specified URI with the specified output name:
aria2c --out={{filename}} {{url}}
Download multiple files in parallel:
aria2c --force-sequential {{url_1}} {{url_2}}
Download from multiple sources with each URI pointing to the same file:
aria2c {{url_1}} {{url_2}}
Download the URIs listed in a file with limited parallel downloads:
aria2c --input-file={{filename}} --max-concurrent-downloads={{number_of_downloads}}
Download with multiple connections:
aria2c --split={{number_of_connections}} {{url}}
FTP download with username and password:
aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}
Limit download speed in bytes/s:
aria2c --max-download-limit={{speed}} {{url}}
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
