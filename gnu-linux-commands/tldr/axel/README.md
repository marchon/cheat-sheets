# axel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/axel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tail
,
git stage
,
hexo
,
bash
,
salt run
.
axel
Download accelerator.
Supports HTTP, HTTPS, and FTP.
More information:
https://github.com/axel-download-accelerator/axel
.
Download a URL to a file:
axel {{url}}
Download and specify filename:
axel {{url}} -o {{filename}}
Download with multiple connections:
axel -n {{connections_num}} {{url}}
Search for mirrors:
axel -S {{mirrors_num}} {{url}}
Limit download speed (bytes per second):
axel -s {{speed}} {{url}}
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
