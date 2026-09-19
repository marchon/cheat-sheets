# troff

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/troff/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
siege
,
phing
,
glab mr
,
puppet apply
.
troff
Typesetting processor for the groff (GNU Troff) document fomatting system.
See also
groff
.
More information:
https://manned.org/troff
.
Format output for a PostScript printer, saving the output to a file:
troff {{path/to/input.roff}} | grops > {{path/to/output.ps}}
Format output for a PostScript printer using the [me] macro package, saving the output to a file:
troff -{{me}} {{path/to/input.roff}} | grops > {{path/to/output.ps}}
Format output as [a]SCII text using the [man] macro package:
troff -T {{ascii}} -{{man}} {{path/to/input.roff}} | grotty
Format output as a [pdf] file, saving the output to a file:
troff -T {{pdf}} {{path/to/input.roff}} | gropdf > {{path/to/output.pdf}}
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
