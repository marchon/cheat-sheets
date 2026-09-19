# paste

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/paste/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git effort
,
pyenv
,
locust
,
kind
.
paste
Merge lines of files.
More information:
https://www.gnu.org/software/coreutils/paste
.
Join all the lines into a single line, using TAB as delimiter:
paste -s {{file}}
Join all the lines into a single line, using the specified delimiter:
paste -s -d {{delimiter}} {{file}}
Merge two files side by side, each in its column, using TAB as delimiter:
paste {{file1}} {{file2}}
Merge two files side by side, each in its column, using the specified delimiter:
paste -d {{delimiter}} {{file1}} {{file2}}
Merge two files, with lines added alternatively:
paste -d '\n' {{file1}} {{file2}}
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
