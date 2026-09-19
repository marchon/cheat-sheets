# sort

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sort/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vault
,
docker machine
,
az vm
.
sort
Sort lines of text files.
More information:
https://www.gnu.org/software/coreutils/sort
.
Sort a file in ascending order:
sort {{path/to/file}}
Sort a file in descending order:
sort --reverse {{path/to/file}}
Sort a file in case-insensitive way:
sort --ignore-case {{path/to/file}}
Sort a file using numeric rather than alphabetic order:
sort --numeric-sort {{path/to/file}}
Sort
/etc/passwd
by the 3rd field of each line numerically, using ":" as a field separator:
sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}
Sort a file preserving only unique lines:
sort --unique {{path/to/file}}
Sort a file, printing the output to the specified output file (can be used to sort a file in-place):
sort --output={{path/to/file}} {{path/to/file}}
Sort numbers with exponents:
sort --general-numeric-sort {{path/to/file}}
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
