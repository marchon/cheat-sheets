# eqn

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/eqn/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
expose
,
recsel
,
lerna
,
flask
,
dolt checkout
.
eqn
Equation preprocessor for the groff (GNU Troff) document formatting system.
See also
troff
and
groff
.
More information:
https://manned.org/eqn
.
Process input with equations, saving the output for future typesetting with groff to PostScript:
eqn {{path/to/input.eqn}} > {{path/to/output.roff}}
Typeset an input file with equations to PDF using the [me] macro package:
eqn -T {{pdf}} {{path/to/input.eqn}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}
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
