# expand

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/expand/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gmssl
,
hg update
,
git sync
,
forever
.
expand
Convert tabs to spaces.
More information:
https://www.gnu.org/software/coreutils/expand
.
Convert tabs in each file to spaces, writing to standard output:
expand {{file}}
Convert tabs to spaces, reading from standard input:
expand
Do not convert tabs after non blanks:
expand -i {{file}}
Have tabs a certain number of characters apart, not 8:
expand -t={{number}} {{file}}
Use a comma separated list of explicit tab positions:
expand -t={{1,4,6}}
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
