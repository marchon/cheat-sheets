# neato

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/neato/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xml edit
,
clockwork cli
,
diff
.
neato
Render an image of a
linear undirected
network graph from a
graphviz
file.
Layouts:
dot
,
neato
,
twopi
,
circo
,
fdp
,
sfdp
,
osage
&
patchwork
.
More information:
https://graphviz.org/doc/info/command.html
.
Render a
png
image with a filename based on the input filename and output format (uppercase -O):
neato -T {{png}} -O {{path/to/input.gv}}
Render a
svg
image with the specified output filename (lowercase -o):
neato -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}
Render the output in
ps
,
pdf
,
svg
,
fig
,
png
,
gif
,
jpg
,
json
, or
dot
format:
neato -T {{format}} -O {{path/to/input.gv}}
Render a
gif
image using stdin and stdout:
echo "{{graph {this -- that} }}" | neato -T {{gif}} > {{path/to/image.gif}}
Display help:
neato -?
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
