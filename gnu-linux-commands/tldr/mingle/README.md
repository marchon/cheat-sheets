# mingle

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mingle/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
decaffeinate
,
openssl req
,
git check mailmap
.
mingle
Bundle the edges of a graph layout.
Graphviz filters:
acyclic
,
bcomps
,
comps
,
edgepaint
,
gvcolor
,
gvpack
,
mingle
,
nop
,
sccmap
,
tred
, &
unflatten
.
More information:
https://www.graphviz.org/pdf/mingle.1.pdf
.
Bundle the edges of one or more graph layouts (that already have layout information):
mingle {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}
Perform layout, bundling, and output to a picture with one command:
dot {{path/to/input.gv}} | mingle | dot -T {{png}} > {{path/to/output.png}}
Display help for
mingle
:
mingle -?
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
