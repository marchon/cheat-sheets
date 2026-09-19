# gv2gml

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gv2gml/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
s
,
mongo
,
sk
,
pyenv virtualenv
.
gv2gml
Convert a graph from
gv
to
gml
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
https://graphviz.org/pdf/gml2gv.1.pdf
.
Convert a graph from
gv
to
gml
format:
gv2gml -o {{output.gml}} {{input.gv}}
Convert a graph using stdin and stdout:
cat {{input.gv}} | gv2gml > {{output.gml}}
Display help:
gv2gml -?
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
