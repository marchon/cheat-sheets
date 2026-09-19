# quilt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/quilt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nbtscan
,
tlmgr shell
,
flask
,
kafkacat
.
quilt
Tool to manage a series of patches.
More information:
https://savannah.nongnu.org/projects/quilt
.
Import an existing patch from a file:
quilt import {{path/to/filename.patch}}
Create a new patch:
quilt new {{filename.patch}}
Add a file to the current patch:
quilt add {{path/to/file}}
After editing the file, refresh the current patch with the changes:
quilt refresh
Apply all the patches in the series file:
quilt push -a
Remove all applied patches:
quilt pop -a
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
