# lpinfo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lpinfo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git rebase
,
docker container
.
lpinfo
List connected printers and installed drivers for the CUPS print server.
More information:
https://www.cups.org/doc/man-lpinfo.html
.
List all the currently connected printers:
lpinfo -v
List all the currently installed printer drivers:
lpinfo -m
Search installed printer drivers by make and model:
lpinfo --make-and-model "{{printer_model}}" -m
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
