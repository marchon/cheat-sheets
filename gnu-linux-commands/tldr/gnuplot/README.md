# gnuplot

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gnuplot/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws ecr
,
pueue edit
,
virsh pool autostart
.
gnuplot
A graph plotter that outputs in several formats.
More information:
http://www.gnuplot.info/
.
Start the interactive graph plotting shell:
gnuplot
Plot the graph for the specified graph definition file:
gnuplot {{path/to/definition.plt}}
Set the output format by executing a command before loading the definition file:
gnuplot -e "{{set output "path/to/filename.png" size 1024,768}}" {{path/to/definition.plt}}
Persist the graph plot preview window after gnuplot exits:
gnuplot --persist {{path/to/definition.plt}}
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
