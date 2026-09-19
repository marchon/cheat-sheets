# sccmap

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sccmap/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh repo
,
gh ssh key
,
nikto
,
vladimyr
.
sccmap
Extract strongly connected components of directed graphs.
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
https://www.graphviz.org/pdf/sccmap.1.pdf
.
Extract strongly connected components of one or more directed graphs:
sccmap -S {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}
Print statistics about a graph, producing no output graph:
sccmap -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}
Display help for
sccmap
:
sccmap -?
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
