# unflatten

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/unflatten/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
doctl apps
,
vdir
,
theharvester
.
unflatten
Adjust directed graphs to improve the layout aspect ratio.
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
https://www.graphviz.org/pdf/unflatten.1.pdf
.
Adjust one or more directed graphs to improve the layout aspect ratio:
unflatten {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}
Use
unflatten
as a preprocessor for
dot
layout to improve aspect ratio:
unflatten {{path/to/input.gv}} | dot -T {{png}} {{path/to/output.png}}
Display help for
unflatten
:
unflatten -?
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
