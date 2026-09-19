# acyclic

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/acyclic/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lp
,
arc
,
kate
,
deluge console
,
git delta
.
acyclic
Make a directed graph acyclic by reversing some edges.
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
https://graphviz.org/pdf/acyclic.1.pdf
.
Make a directed graph acyclic by reversing some edges:
acyclic {{path/to/input.gv}} > {{path/to/output.gv}}
Print if a graph is acyclic, has a cycle, or is undirected, producing no output graph:
acyclic -v -n {{path/to/input.gv}}
Display help for
acyclic
:
acyclic -?
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
