# git-check-attr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-check-attr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
exit
,
rclone
,
vala
,
drupal check
.
git check-attr
For every pathname, list if each attribute is unspecified, set, or unset as a gitattribute on that pathname.
More information:
https://git-scm.com/docs/git-check-attr
.
Check the values of all attributes on a file:
git check-attr --all {{path/to/file}}
Check the value of a specific attribute on a file:
git check-attr {{attribute}} {{path/to/file}}
Check the value of a specific attribute on files:
git check-attr --all {{path/to/file1}} {{path/to/file2}}
Check the value of a specific attribute on one or more files:
git check-attr {{attribute}} {{path/to/file1}} {{path/to/file2}}
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
