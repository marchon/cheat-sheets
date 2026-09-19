# srm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/srm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab mr merge
,
raco
,
go vet
,
pio lib
.
srm
Securely remove files or directories.
Overwrites the existing data one or multiple times. Drop in replacement for rm.
More information:
http://srm.sourceforge.net/srm.html
.
Remove a file after a single-pass overwriting with random data:
srm -s {{path/to/file}}
Remove a file after seven passes of overwriting with random data:
srm -m {{path/to/file}}
Recursively remove a directory and its contents overwriting each file with a single-pass of random data:
srm -r -s {{path/to/directory}}
Prompt before every removal:
srm -i {{\*}}
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
