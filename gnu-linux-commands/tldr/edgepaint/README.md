# edgepaint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/edgepaint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
uname
,
split
,
firebase
,
fastlane
.
edgepaint
Colorize edges of a graph layout to clarify crossing edges.
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
https://graphviz.org/pdf/edgepaint.1.pdf
.
Colorize edges of one or more graph layouts (that already have layout information) to clarify crossing edges:
edgepaint {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}
Colorize edges using a color scheme. (See
https://graphviz.org/doc/info/colors.html#brewer
):
edgepaint -color-scheme={{accent7}} {{path/to/layout.gv}} > {{path/to/output.gv}}
Lay out a graph and colorize its edges, then convert to a PNG image:
dot {{path/to/input.gv}} | edgepaint | dot -T {{png}} > {{path/to/output.png}}
Display help for
edgepaint
:
edgepaint -?
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
