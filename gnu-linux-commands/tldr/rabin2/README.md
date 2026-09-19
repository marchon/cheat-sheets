# rabin2

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rabin2/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
scc
,
ansible
,
llvm strings
,
csvsort
.
rabin2
Get information about binary files (ELF, PE, Java CLASS, Mach-O) - symbols, sections, linked libraries, etc.
Comes bundled with
radare2
.
More information:
https://manned.org/rabin2
.
Display general information about a binary (architecture, type, endianness):
rabin2 -I {{path/to/binary}}
Display linked libraries:
rabin2 -l {{path/to/binary}}
Display symbols imported from libraries:
rabin2 -i {{path/to/binary}}
Display strings contained in the binary:
rabin2 -z {{path/to/binary}}
Display the output in JSON:
rabin2 -j -I {{path/to/binary}}
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
