# ccomps

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ccomps/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
airmon ng
,
lsd
,
rabin2
,
qmv
,
openscad
.
ccomps
Decompose graphs into their connected components.
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
https://graphviz.org/pdf/ccomps.1.pdf
.
Decompose one or more graphs into their connected components:
ccomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}
Print the number of nodes, edges, and connected components in one or more graphs:
ccomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}
Write each connected component to numbered filenames based on
output.gv
:
ccomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv ...}}
Display help for
ccomps
:
ccomps -?
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
