# plantuml

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/plantuml/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
khal
,
xephyr
,
meson
,
glab repo
.
plantuml
Create UML diagrams from a plain text language and render them in different formats.
More information:
https://plantuml.com/en/command-line
.
Render diagrams to default format (PNG):
plantuml {{diagram1.puml}} {{diagram2.puml}}
Render a diagram in given format (e.g.
png
,
pdf
,
svg
,
txt
):
plantuml -t {{format}} {{diagram.puml}}
Render all diagrams of a directory:
plantuml {{path/to/diagrams}}
Render a diagram to the output directory:
plantuml -o {{path/to/output}} {{diagram.puml}}
Render a diagram with the configuration file:
plantuml -config {{config.cfg}} {{diagram.puml}}
Display help:
plantuml -help
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
