# nm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio package
,
berks
,
csvclean
.
nm
List symbol names in object files.
More information:
https://manned.org/nm
.
List global (extern) functions in a file (prefixed with T):
nm -g {{path/to/file.o}}
List only undefined symbols in a file:
nm -u {{path/to/file.o}}
List all symbols, even debugging symbols:
nm -a {{path/to/file.o}}
Demangle C++ symbols (make them readable):
nm --demangle {{path/to/file.o}}
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
