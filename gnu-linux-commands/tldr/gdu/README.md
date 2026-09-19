# gdu

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gdu/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pass otp
,
vlc
,
csvclean
,
git rename tag
.
gdu
Disk usage analyzer with console interface.
More information:
https://github.com/dundee/gdu
.
Interactively show the disk usage of the current directory:
gdu
Interactively show the disk usage of a given directory:
gdu {{path/to/directory}}
Interactively show the disk usage of all mounted disks:
gdu --show-disks
Interactively show the disk usage of the current directory but ignore some sub-directories:
gdu --ignore-dirs {{path/to/directory1,path/to/directory2,...}}
Ignore paths by regular expression:
gdu --ignore-dirs-pattern '{{.*[abc]+}}'
Ignore hidden directories:
gdu --no-hidden
Only print the result, do not enter interactive mode:
gdu --non-interactive {{path/to/directory}}
Do not show the progress in non-interactive mode (useful in scripts):
gdu --no-progress {{path/to/directory}}
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
