# uncrustify

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/uncrustify/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
serve
,
xmllint
,
arp scan
,
pest
.
uncrustify
C, C++, C#, D, Java and Pawn source code formatter.
More information:
https://github.com/uncrustify/uncrustify
.
Format a single file:
uncrustify -f {{path/to/file.cpp}} -o {{path/to/output.cpp}}
Read filenames from stdin, and take backups before writing output back to the original filepaths:
find . -name "*.cpp" | uncrustify -F - --replace
Don't make backups (useful if files are under version control):
find . -name "*.cpp" | uncrustify -F - --no-backup
Use a custom configuration file and write the result to stdout:
uncrustify -c {{path/to/uncrustify.cfg}} -f {{path/to/file.cpp}}
Explicitly set a configuration variable's value:
uncrustify --set {{option}}={{value}}
Generate a new configuration file:
uncrustify --update-config -o {{path/to/new.cfg}}
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
