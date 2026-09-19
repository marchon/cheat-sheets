# hashid

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hashid/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg root
,
trash cli
,
bundletool dump
.
hashid
Python3 program that identifies data and password hashes.
More information:
https://github.com/psypanda/hashID
.
Identify hashes from standard input (through typing, copying and pasting, or piping the hash into the program):
hashid
Identify hashes passed as arguments (multiple hashes can be passed):
hashid {{hash}}
Identify hashes on a file (one hash per line):
hashid {{path/to/hashes.txt}}
Show all possible hash types (including salted hashes):
hashid --extended {{hash}}
Show
hashcat
's mode number and
john
's format string of the hash types:
hashid --mode --john {{hash}}
Save output to a file instead of printing to standard output:
hashid --outfile {{path/to/output.txt}} {{hash}}
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
