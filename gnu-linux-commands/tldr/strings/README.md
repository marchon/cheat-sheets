# strings

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/strings/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hsd cli
,
atq
,
readlink
,
gitlab
.
strings
Find printable strings in an object file or binary.
More information:
https://manned.org/strings
.
Print all strings in a binary:
strings {{file}}
Limit results to strings at least *length* characters long:
strings -n {{length}} {{file}}
Prefix each result with its offset within the file:
strings -t d {{file}}
Prefix each result with its offset within the file in hexadecimal:
strings -t x {{file}}
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
