# convmv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/convmv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
elm
,
git standup
,
nim
,
wasm objdump
.
convmv
Convert filenames (NOT file content) from one encoding to another.
More information:
https://www.j3e.de/linux/convmv/man/
.
Test filename encoding conversion (don't actually change the filename):
convmv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}
Convert filename encoding and rename the file to the new encoding:
convmv -f {{from_encoding}} -t {{to_encoding}} --notest {{input_file}}
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
