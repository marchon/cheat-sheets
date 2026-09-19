# tac

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tac/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mat2
,
diff pdf
,
virt install
.
tac
Display and concatenate files with lines in reversed order.
See also:
cat
.
More information:
https://www.gnu.org/software/coreutils/tac
.
Concatenate specific files in reversed order:
tac {{path/to/file1 path/to/file2 ...}}
Display
stdin
in reversed order:
{{cat path/to/file}} | tac
Use a specific [s]eparator:
tac -s {{separator}} {{path/to/file1 path/to/file2 ...}}
Use a specific [r]egex as a [s]eparator:
tac -r -s {{separator}} {{path/to/file1 path/to/file2 ...}}
Use a separator [b]efore each file:
tac -b {{path/to/file1 path/to/file2 ...}}
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
