# bcomps

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bcomps/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zellij
,
mm2gv
,
bundletool validate
.
bcomps
Decompose graphs into their biconnected components.
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
https://graphviz.org/pdf/bcomps.1.pdf
.
Decompose one or more graphs into their biconnected components:
bcomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}
Print the number of blocks and cutvertices in one or more graphs:
bcomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}
Write each block and block-cutvertex tree to multiple numbered filenames based on
output.gv
:
bcomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv ...}}
Display help for
bcomps
:
bcomps -?
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
