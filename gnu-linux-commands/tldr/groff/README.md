# groff

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/groff/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
r2e
,
haxelib
,
git tag
,
watch
,
pueue status
.
groff
GNU replacement for the
troff
and
nroff
typesetting utilities.
More information:
https://www.gnu.org/software/groff
.
Format output for a PostScript printer, saving the output to a file:
groff {{path/to/input.roff}} > {{path/to/output.ps}}
Render a man page using the ASCII output device, and display it using a pager:
groff -man -T ascii {{path/to/manpage.1}} | less --RAW-CONTROL-CHARS
Render a man page into an HTML file:
groff -man -T html {{path/to/manpage.1}} > {{path/to/manpage.html}}
Typeset a roff file containing [t]ables and [p]ictures, using the [me] macro set, to PDF, saving the output:
groff {{-t}} {{-p}} -{{me}} -T {{pdf}} {{path/to/input.me}} > {{path/to/output.pdf}}
Run a
groff
command with preprocessor and macro options guessed by the
grog
utility:
eval "$(grog -T utf8 {{path/to/input.me}})"
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
