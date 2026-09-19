# unexpand

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/unexpand/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
read
,
ipcs
,
f3fix
,
killall
,
ocrmypdf
.
unexpand
Convert spaces to tabs.
More information:
https://www.gnu.org/software/coreutils/unexpand
.
Convert blanks in each file to tabs, writing to standard output:
unexpand {{file}}
Convert blanks to tabs, reading from standard output:
unexpand
Convert all blanks, instead of just initial blanks:
unexpand -a {{file}}
Convert only leading sequences of blanks (overrides -a):
unexpand --first-only {{file}}
Have tabs a certain number of characters apart, not 8 (enables -a):
unexpand -t {{number}} {{file}}
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
