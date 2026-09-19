# grap

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/grap/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ioping
,
deb get
,
fd
,
eslint
,
stat
.
grap
A charting preprocessor for the groff (GNU Troff) document formatting system.
See also
pic
and
groff
.
More information:
https://manned.org/grap
.
Process a
grap
file and save the output file for future processing with
pic
and
groff
:
grap {{path/to/input.grap}} > {{path/to/output.pic}}
Typeset a
grap
file to PDF using the [me] macro package, saving the output to a file:
grap {{path/to/input.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}
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
