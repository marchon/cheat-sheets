# radare2

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/radare2/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nokogiri
,
neomutt
,
timetrap
,
sails
.
radare2
A set of reverse engineering tools.
More information:
https://radare.gitbooks.io/radare2book/
.
Open a file in write mode without parsing the file format headers:
radare2 -nw {{path/to/binary}}
Debug a program:
radare2 -d {{path/to/binary}}
Run a script before entering the interactive CLI:
radare2 -i {{path/to/script.r2}} {{path/to/binary}}
Show help text for any command in the interactive CLI:
> {{radare2_command}}?
Run a shell command from the interactive CLI:
> !{{shell_command}}
Dump raw bytes of current block to a file:
> pr > {{path/to/file.bin}}
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
