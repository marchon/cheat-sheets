# pic

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pic/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio team
,
circo
,
ipython
,
uncrustify
.
pic
Picture preprocessor for the groff (GNU Troff) document formatting system.
See also
groff
and
troff
.
More information:
https://manned.org/pic
.
Process input with pictures, saving the output for future typesetting with groff to PostScript:
pic {{path/to/input.pic}} > {{path/to/output.roff}}
Typeset input with pictures to PDF using the [me] macro package:
pic -T {{pdf}} {{path/to/input.pic}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}
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
