# nkf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nkf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hsd cli
,
clockwork cli
,
sd
,
rspec
.
nkf
Network kanji filter.
Converts kanji code from one encoding to another.
More information:
https://manned.org/nkf
.
Convert to UTF-8 encoding:
nkf -w {{path/to/file.txt}}
Convert to SHIFT_JIS encoding:
nkf -s {{path/to/file.txt}}
Convert to UTF-8 encoding and overwrite the file:
nkf -w --overwrite {{path/to/file.txt}}
Set new line code to LF and overwrite (UNIX type):
nkf -d --overwrite {{path/to/file.txt}}
Set new line code to CRLF and overwrite (windows type):
nkf -c --overwrite {{path/to/file.txt}}
Decrypt mime file and overwrite:
nkf -m --overwrite {{path/to/file.txt}}
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
