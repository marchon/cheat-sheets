# gvpack

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gvpack/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
osage
,
pio init
,
virsh pool destroy
.
gvpack
Combine several graph layouts (that already have layout information).
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
https://graphviz.org/pdf/gvpack.1.pdf
.
Combine several graph layouts (that already have layout information):
gvpack {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}
Combine several graph layouts at the graph level, keeping graphs separate:
gvpack -g {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}
Combine several graph layouts at the node level, ignoring clusters:
gvpack -n {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}
Combine several graph layouts without packing:
gvpack -u {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}
Display help for
gvpack
:
gvpack -?
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
