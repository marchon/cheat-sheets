# f3fix

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/f3fix/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fc pattern
,
gh mintty
,
ghci
,
ldapsearch
.
f3fix
Edit the partition table of a fake flash drive.
See also
f3probe
,
f3write
,
f3read
.
More information:
http://oss.digirati.com.br/f3/
.
Fill a fake flash drive with a single partition that matches its real capacity:
sudo f3fix {{/dev/device_name}}
Mark the partition as bootable:
sudo f3fix --boot {{/dev/device_name}}
Specify the filesystem:
sudo f3fix --fs-type={{filesystem_type}} {{/dev/device_name}}
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
