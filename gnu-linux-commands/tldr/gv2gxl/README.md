# gv2gxl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gv2gxl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gimp
,
timeout
,
shift
,
minifab
,
nix
.
gv2gxl
Convert a graph from
gv
to
gxl
format.
Converters:
gml2gv
,
gv2gml
,
gv2gxl
,
gxl2gv
,
graphml2gv
&
mm2gv
.
More information:
https://graphviz.org/pdf/gxl2gv.1.pdf
.
Convert a graph from
gv
to
gxl
format:
gv2gxl -o {{output.gxl}} {{input.gv}}
Convert a graph using stdin and stdout:
cat {{input.gv}} | gv2gxl > {{output.gxl}}
Display help:
gv2gxl -?
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
